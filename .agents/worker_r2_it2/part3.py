import sys

def get_part3():
    return """
---

# 5. SEQ-05: QUY TRÌNH CHẤM CÔNG NHÂN VIÊN KHÓA WIFI — XÁC THỰC BSSID & IP SUBNET

### 📌 Mô tả Nghiệp vụ (Business Context)
Nhân viên chi nhánh đến quán làm việc, truy cập cổng Chấm công Web `(staff)/attendance` trên thiết bị di động hoặc máy tính bảng.
- **Quy tắc bảo mật bất biến:** Loại bỏ 100% định vị GPS 50m (sai số lớn trong nhà) và mã QR 30 giây.
- **Cơ chế Xác thực kép (Double Verification Gate):**
  1. **Lớp mạng (Network Infrastructure):** Backend kiểm tra địa chỉ IP Client (`X-Forwarded-For`) phải nằm trong dải `allowed_ip_subnets` của chi nhánh (ví dụ: `192.168.1.0/24`) VÀ BSSID của Access Point WiFi chi nhánh (`bssid_list` từ bảng `branch_wifi_configs`).
  2. **Lớp nhân sự (Employee Identity):** Kiểm tra `users.employee_code` có tồn tại, đang ở trạng thái `is_active = true` và thuộc chi nhánh `users.branch_id`.
- Lưu kết quả vào bảng `staff_attendances` (`is_wifi_verified = true`, `status = 'OnTime'`).

```mermaid
sequenceDiagram
    autonumber
    actor ST as 👨‍🍳 Nhân Viên Ca Trực
    participant BROWSER as 📱 Trình Duyệt Web Staff ((staff)/attendance)
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (AttendanceController)
    participant DB as 🐘 PostgreSQL 16 (branch_wifi_configs, users, staff_attendances)
    participant HUB as 📡 SignalR NotificationHub
    actor MGR as 🏪 Quản Lý Chi Nhánh (Manager Portal)

    %% Bước 1: Kết nối WiFi & Nhập mã chấm công
    ST->>ST: Kết nối thiết bị vào WiFi nội bộ quán ("SmartFB_Q1_Staff")
    ST->>BROWSER: Truy cập https://smartfb.vn/staff/attendance
    ST->>BROWSER: Nhập Mã NV: "NV-Q1-008" & Chọn [VÀO CA (CHECK-IN)]
    
    BROWSER->>NGINX: POST /api/v1/attendance/check-in (BranchId: "B01", EmployeeCode: "NV-Q1-008", ClientBssid: "00:1A:2B:3C:4D:5E")
    NGINX->>API: Forward kèm Header: X-Forwarded-For: "192.168.1.142", X-Real-IP: "192.168.1.142"

    activate API
    %% Bước 2: Kiểm tra Lớp 1 - Mạng WiFi Chi Nhánh
    API->>DB: SELECT bssid_list, allowed_ip_subnets FROM branch_wifi_configs WHERE branch_id = 'B01' AND is_active = true
    DB-->>API: ConfigData { allowed_ip_subnets: "192.168.1.0/24", bssid_list: "00:1A:2B:3C:4D:5E,00:1A:2B:3C:4D:5F" }

    API->>API: Lớp 1: IPNetwork.Parse("192.168.1.0/24").Contains("192.168.1.142") == true && bssid_list.Contains("00:1A:2B:3C:4D:5E")

    alt Trường hợp 1: Không đúng WiFi quán (Dùng 4G/5G hoặc WiFi nhà)
        API-->>BROWSER: HTTP 403 Forbidden (RFC 7807: "WIFI_NETWORK_MISMATCH - Thiết bị chưa kết nối đúng WiFi chi nhánh")
        BROWSER-->>ST: 🔴 Cảnh báo đỏ: "Vui lòng kết nối WiFi SmartFB_Q1_Staff tại quán để chấm công!"
    else Trường hợp 2: Đúng mạng WiFi chi nhánh
        %% Bước 3: Kiểm tra Lớp 2 - Nhân sự & Ghi nhận
        API->>DB: SELECT u.id, u.full_name, u.branch_id, r.name as role_name FROM users u JOIN user_roles ur ON u.id = ur.user_id JOIN roles r ON ur.role_id = r.id WHERE u.employee_code = 'NV-Q1-008' AND u.branch_id = 'B01' AND u.is_active = true AND u.is_deleted = false
        
        alt Mã NV không hợp lệ hoặc bị khóa
            DB-->>API: Null
            API-->>BROWSER: HTTP 404 Not Found (RFC 7807: "Mã nhân viên không tồn tại hoặc đã bị khóa")
            BROWSER-->>ST: 🔴 Thông báo lỗi tài khoản nhân sự
        else Nhân sự hợp lệ
            DB-->>API: UserRecord { id: "u-9912", full_name: "Trần Văn Nam", role_name: "Barista" }
            
            API->>DB: INSERT INTO staff_attendances (user_id, branch_id, employee_code, check_in_time, verified_ip, verified_bssid, verified_ssid, is_wifi_verified, status, notes) VALUES ('u-9912', 'B01', 'NV-Q1-008', NOW(), '192.168.1.142', '00:1A:2B:3C:4D:5E', 'SmartFB_Q1_Staff', true, 'OnTime', 'Vào ca đúng giờ') RETURNING id
            DB-->>API: AttendanceRecordCreated (Id="att-9912", Time="06:55:10")
            
            API->>HUB: NotificationHub.Clients.Group("branch_B01_manager").SendAsync("StaffAttendanceLogged", { employeeName: "Trần Văn Nam", code: "NV-Q1-008", time: "06:55:10", status: "OnTime" })
            API-->>BROWSER: HTTP 200 OK (EmployeeName="Trần Văn Nam", CheckInTime="06:55:10", Status="OnTime")
        end
    end
    deactivate API

    par Thông báo Giao diện Nhân Viên & Quản Lý
        BROWSER-->>ST: 🟢 Màn hình chuyển xanh: "Chấm công vào ca thành công lúc 06:55:10. Chúc bạn ca làm việc vui vẻ!"
        HUB-->>MGR: Manager Portal cập nhật Dashboard nhân sự: "Trần Văn Nam (Barista) vừa vào ca lúc 06:55:10"
    end
```

---

# 6. SEQ-06: QUY TRÌNH XỬ LÝ ĐƠN BẾP (KDS), KHẤU TRỪ BOM & CÔNG TẮC 86-TOGGLE

### 📌 Mô tả Nghiệp vụ (Business Context)
1. **Xử lý KDS & Trừ Tồn BOM:** Barista nhận đơn qua SignalR WebSocket. Khi bấm `Ready` (Hoàn thành pha chế), hệ thống tự động kích hoạt **BOM Inventory Deduction Engine** tra cứu công thức từ `product_recipes` của từng món trong đơn, trừ chính xác số lượng nguyên liệu tồn kho trong `inventory_stocks` theo đơn vị gam/ml và ghi nhật ký vào `inventory_logs`. Nếu nguyên liệu tụt xuống dưới `min_stock_threshold` trong bảng `ingredients`, hệ thống phát cảnh báo `LowStockAlert` tới Quản lý.
2. **Khóa Món Khẩn Cấp (86-Toggle):** Khi Barista phát hiện hết nguyên liệu (ví dụ: Hết Đào ngâm), Barista gạt công tắc `86-Toggle` trên màn hình KDS. Hệ thống lập tức cập nhật PostgreSQL (`products.is_available = false`), đồng bộ Redis Cache (`branch:{branch_id}:out_of_stock`) và phát sự kiện SignalR tới toàn bộ khách hàng trong quán để làm mờ món và khóa nút đặt hàng trong thời gian dưới 1 giây.

```mermaid
sequenceDiagram
    autonumber
    actor KDS as 🧋 Barista (Web KDS)
    participant UI as 💻 Next.js KDS App
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (KDS & Inventory Controller)
    participant DB as 🐘 PostgreSQL 16 (product_recipes, inventory_stocks, inventory_logs, ingredients, products)
    participant RD as ⚡ Redis 7 Cache & Hash Store
    participant HUB as 📡 SignalR (Kitchen & Notification Hub)
    participant PWA as 📱 QR Menu Khách Hàng (Tất cả bàn)
    actor MGR as 🏪 Quản Lý Chi Nhánh

    %% PHẦN 1: PHA CHẾ & TỰ ĐỘNG TRỪ KHO THEO BOM (GAM / ML)
    Note over KDS,DB: PHẦN 1: PHA CHẾ HOÀN TẤT & KHẤU TRỪ ĐỊNH LƯỢNG BOM
    KDS->>UI: Chạm nút [Hoàn Tất Pha Chế] trên thẻ đơn #ORD-B01-9942 (2x Matcha Latte Size L)
    UI->>NGINX: PATCH /api/v1/kds/orders/ord-9942/complete-prep
    NGINX->>API: Forward Request

    activate API
    API->>DB: BEGIN TRANSACTION
    API->>DB: UPDATE orders SET status='Ready' WHERE id='ord-9942'
    
    API->>DB: SELECT r.ingredient_id, r.quantity, r.wastage_rate FROM product_recipes r WHERE r.product_id='prod-matcha' AND r.size_id='size-L'
    DB-->>API: Recipe Data: { Bột Matcha: 15g, Sữa Tươi: 180ml, Nước Đường: 20ml } (x2 Ly = 30g Matcha, 360ml Sữa)
    
    API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 30, updated_at=NOW() WHERE ingredient_id='ing-matcha' AND branch_id='B01'
    API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 360, updated_at=NOW() WHERE ingredient_id='ing-milk' AND branch_id='B01'
    API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-30, notes='Auto deduct KDS Ready')
    API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-360, notes='Auto deduct KDS Ready')
    
    API->>DB: SELECT i.name, s.current_quantity, i.min_stock_threshold FROM inventory_stocks s JOIN ingredients i ON s.ingredient_id = i.id WHERE s.branch_id='B01' AND s.current_quantity <= i.min_stock_threshold
    DB-->>API: AlertList: [{ name: "Sữa Tươi Thanh Trùng", current_quantity: 1200, min_stock_threshold: 2000 }]
    API->>DB: COMMIT TRANSACTION

    API->>HUB: KitchenHub.Clients.Group("branch_B01_kitchen").SendAsync("OrderStatusUpdated", "Ready")
    opt Phát hiện nguyên liệu dưới ngưỡng tối thiểu
        API->>HUB: NotificationHub.Clients.Group("branch_B01_manager").SendAsync("LowStockAlert", { ingredient: "Sữa Tươi Thanh Trùng", current: "1.2L", min: "2.0L" })
    end
    API-->>UI: HTTP 200 OK (Status="Ready", StockDeducted=true)
    deactivate API

    HUB-->>MGR: Manager Portal hiển thị cảnh báo đỏ nhấp nháy: "⚠️ Sữa Tươi Thanh Trùng sắp hết (Còn 1.2L)"

    %% PHẦN 2: CÔNG TẮC 86-TOGGLE KHÓA MÓN HẾT HÀNG TỨC THÌ
    Note over KDS,PWA: PHẦN 2: CÔNG TẮC KHẨN CẤP 86-TOGGLE (KHÓA MÓN HẾT HÀNG)
    KDS->>UI: Phát hiện hết Đào ngâm -> Mở tab [Tồn Món] -> Gạt Toggle món "Trà Đào Cam Sả" sang [HẾT HÀNG]
    UI->>NGINX: PATCH /api/v1/kds/menu-items/prod-tra-dao/availability { branchId: "B01", isAvailable: false, reason: "Hết Đào Ngâm" }
    NGINX->>API: Forward Request

    activate API
    API->>DB: UPDATE products SET is_available = false, updated_at = NOW() WHERE id='prod-tra-dao'
    API->>RD: HSET branch:B01:out_of_stock "prod-tra-dao" "1"
    API->>RD: DEL menu:branch:B01:active (Xóa cache thực đơn chi nhánh)
    
    API->>HUB: KitchenHub.Clients.Group("branch_B01_kitchen").SendAsync("Item86Toggled", { productId: "prod-tra-dao", isAvailable: false })
    API->>HUB: OrderHub.Clients.Group("branch_B01_customers").SendAsync("Item86Toggled", { productId: "prod-tra-dao", isAvailable: false })
    API-->>UI: HTTP 200 OK (Message: "Đã khóa món Trà Đào Cam Sả thành công")
    deactivate API

    par Đồng bộ tức thời dưới 1 giây
        UI-->>KDS: Nút chuyển sang trạng thái đỏ [86 - HẾT HÀNG]
        HUB-->>PWA: WebSocket Event `Item86Toggled` -> Toàn bộ điện thoại khách trong quán tự động làm mờ món "Trà Đào Cam Sả", hiện nhãn "Tạm Hết Món" và khóa nút [Thêm vào giỏ]
    end
```

---

# 7. SEQ-07: QUY TRÌNH GỌI PHỤC VỤ TẠI BÀN & TIẾP NHẬN CHUÔNG BÁO SIGNALR

### 📌 Mô tả Nghiệp vụ (Business Context)
Khách hàng đang ngồi tại bàn cần hỗ trợ (Xin thêm nước đá/nước lọc, Khăn giấy, Dọn bàn, Hỗ trợ thanh toán).
- Khách bấm biểu tượng Chuông 🔔 trên giao diện PWA.
- **Cơ chế chống Spam Rate-Limit:** Redis áp dụng giới hạn tối thiểu 60 giây giữa 2 lần gọi từ cùng 1 bàn (`lock:ratelimit:call:T04`).
- **Xử lý Realtime Transient State & Audit:** Backend phát sự kiện `ServiceCallAlert` qua SignalR `NotificationHub`. Màn hình Web Staff POS và KDS quầy bar phát âm thanh chuông cảnh báo và hiển thị Banner màu cam nhấp nháy cho đến khi nhân viên bấm "Đã Xử Lý".

```mermaid
sequenceDiagram
    autonumber
    actor C as 👤 Khách Hàng (Tại Bàn 04)
    participant PWA as 📱 Next.js Customer PWA
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (ServiceCallController)
    participant RD as ⚡ Redis 7 (Rate Limit Lock)
    participant HUB as 📡 SignalR (Notification & Staff Hub)
    actor ST as 🧑‍💼 Nhân Viên Phục Vụ / Thu Ngân
    participant POS as 💻 Web Staff POS / KDS Portal

    %% Bước 1: Khách bấm chuông gọi hỗ trợ
    C->>PWA: Chạm icon Chuông 🔔 -> Chọn lý do: "Lấy thêm nước đá" -> Bấm [Gửi Yêu Cầu]
    PWA->>NGINX: POST /api/v1/tables/T04/service-calls { branchId: "B01", tableNumber: "04", requestType: "EXTRA_ICE", notes: "Cho 2 ly đá thêm" }
    NGINX->>API: Forward Request

    activate API
    %% Bước 2: Kiểm tra Rate Limit trên Redis
    API->>RD: SET lock:ratelimit:call:T04 "1" NX EX 60 (Giới hạn 1 lần / 60s)
    RD-->>API: Lock Result (true = Hợp lệ, false = Bị Spam)

    alt Khách bấm gọi liên tục dưới 60 giây (Spam)
        API-->>PWA: HTTP 429 Too Many Requests (RFC 7807: "Yêu cầu đã được gửi, nhân viên đang tới bàn của bạn!")
        PWA-->>C: Hiển thị thông báo Toast nhắc nhở nhẹ nhàng
    else Yêu cầu hợp lệ
        API->>RD: HSET branch:B01:active_service_calls "call-5542" "{ table: '04', type: 'EXTRA_ICE', time: '14:20:05' }"
        
        API->>HUB: NotificationHub.Clients.Group("branch_B01_staff").SendAsync("ServiceCallAlert", { callId: "call-5542", tableNumber: "04", requestType: "EXTRA_ICE", reason: "Lấy thêm nước đá", timestamp: "14:20:05" })
        API-->>PWA: HTTP 201 Created (CallId="call-5542", Message="Đã thông báo tới nhân viên phục vụ")
    end
    deactivate API

    par Phản hồi Khách & Chuông Báo Nhân Viên
        PWA-->>C: Màn hình hiện trạng thái: "Đã gọi phục vụ! Nhân viên sẽ đến trong giây lát."
        HUB-->>POS: Web Staff POS & KDS phát âm thanh "Ting-Ting" 🔔 + Banner Cam nhấp nháy: "⚠️ BÀN 04: Lấy thêm nước đá (14:20)"
    end

    %% Bước 3: Nhân viên phục vụ & Tắt cảnh báo
    ST->>C: Mang 2 ly đá lạnh đến phục vụ Bàn 04
    ST->>POS: Chạm nút [ĐÃ XỬ LÝ] trên Banner cảnh báo Bàn 04
    POS->>NGINX: POST /api/v1/service-calls/call-5542/resolve { resolvedBy: "staff-02" }
    NGINX->>API: Forward Request

    activate API
    API->>RD: HDEL branch:B01:active_service_calls "call-5542"
    API->>HUB: NotificationHub.Clients.Group("branch_B01_staff").SendAsync("ServiceCallResolved", { callId: "call-5542" })
    API-->>POS: HTTP 200 OK (Status="Resolved")
    deactivate API

    HUB-->>POS: Tắt âm thanh chuông cảnh báo & Ẩn Banner nhấp nháy
```
"""
