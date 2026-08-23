import sys

def get_part4():
    return """
---

# 8. SEQ-08: QUY TRÌNH ĐÁNH GIÁ 1-5 SAO, AI SENTIMENT & KÍCH HOẠT RED ALERT

### 📌 Mô tả Nghiệp vụ (Business Context)
Sau khi đơn hàng hoàn tất, PWA hiển thị form đánh giá trải nghiệm: Chấm điểm 1-5 sao (`rating_stars`), viết bình luận, đính kèm 1-3 ảnh thực tế (`photo_urls`) và tùy chọn ẩn danh (`is_anonymous`).
- **Tích hợp Google Gemini 1.5 Flash:** Phân tích cảm xúc (Sentiment Analysis) và phân loại vi phạm/khiếu nại tự động.
- **Cơ chế Leo thang Khẩn cấp (Red Alert Escalation):**
  - **Rating >= 3 sao:** Đánh giá tốt/trung bình, lưu vào `customer_feedbacks` với `is_urgent_alert = false`.
  - **Rating <= 2 sao (Trải nghiệm tệ):** Hệ thống lưu bản ghi với `is_urgent_alert = true` và lập tức kích hoạt sự kiện `UrgentRedAlert` qua SignalR gửi thẳng tới Manager Portal của Quản lý chi nhánh. Màn hình Quản lý phát còi báo động đỏ khẩn cấp để Quản lý trực tiếp đến bàn giải quyết khiếu nại trước khi khách rời quán. Sau khi xử lý, ghi nhận `resolution_notes` và `resolved_by`.

```mermaid
sequenceDiagram
    autonumber
    actor C as 👤 Khách Hàng (Tại bàn)
    participant PWA as 📱 Customer PWA (Feedback Modal)
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (FeedbackController)
    participant S3 as 🗄️ Object Storage CDN
    participant AI as 🤖 Google Gemini 1.5 Flash API
    participant DB as 🐘 PostgreSQL 16 (customer_feedbacks)
    participant HUB as 📡 SignalR NotificationHub
    actor MGR as 🏪 Quản Lý Chi Nhánh (Manager Web Portal)

    %% Bước 1: Khách gửi đánh giá 1 sao kèm ảnh
    C->>PWA: Đơn hàng hoàn tất -> PWA mở Modal Đánh Giá
    C->>PWA: Chấm 1 Sao ⭐, Nhập bình luận: "Cà phê quá ngọt và bị khét, phục vụ chậm hơn 20 phút!", Tải 1 ảnh ly nước, Bật [x] Ẩn danh
    
    PWA->>S3: Upload ảnh review -> Nhận CDN URL: "https://cdn.smartfb.vn/reviews/img_9912.webp"
    PWA->>NGINX: POST /api/v1/reviews
    Note over PWA,API: Payload: { orderId: "ord-9942", branchId: "B01", ratingStars: 1, comment: "...", photoUrls: ["https://..."], isAnonymous: true }
    NGINX->>API: Forward Request

    activate API
    %% Bước 2: AI Sentiment Analysis qua Gemini 1.5 Flash
    API->>AI: POST /v1beta/models/gemini-1.5-flash:generateContent (Prompt: Analyze Sentiment, Toxicity & Complaint Categories for: "Cà phê quá ngọt và bị khét...")
    activate AI
    AI-->>API: Trả về JSON: { sentiment: "Negative", severity: "High", categories: ["DrinkQuality", "ServiceSpeed"], summary: "Khách chê cà phê khét và phục vụ chậm" }
    deactivate AI

    %% Bước 3: Lưu DB & Phân nhánh Escalation
    API->>DB: INSERT INTO customer_feedbacks (order_id, branch_id, rating_stars, comment, photo_urls, is_anonymous, is_urgent_alert, created_at) VALUES ('ord-9942', 'B01', 1, 'Cà phê quá ngọt và bị khét...', '["https://..."]', true, true, NOW()) RETURNING id
    DB-->>API: FeedbackRecordId = "rev-001"
    
    alt Đánh giá xấu (Rating <= 2 Sao) — KÍCH HOẠT RED ALERT
        API->>HUB: NotificationHub.Clients.Group("branch_B01_manager").SendAsync("UrgentRedAlert", { feedbackId: "rev-001", orderId: "ord-9942", tableNumber: "04", ratingStars: 1, comment: "Cà phê khét & phục vụ chậm", aiSummary: "Chất lượng pha chế kém", timestamp: "14:35:10" })
        API-->>PWA: HTTP 201 Created (Message: "Ý kiến của bạn đã được ghi nhận. Quản lý sẽ hỗ trợ bạn ngay lập tức!")
        
        HUB-->>MGR: Manager Portal PHÁT CÒI BÁO ĐỘNG ĐỎ 🚨 & Mở Pop-up Khẩn Cấp: "RED ALERT: Đánh giá 1 sao tại Bàn 04!"
        
        %% Bước 4: Quản lý xử lý khiếu nại tại bàn
        MGR->>C: Quản lý trực tiếp tới Bàn 04 cúi chào, xin lỗi chân thành, đổi ngay ly cà phê mới ít ngọt & tặng Voucher giảm 50k
        C->>MGR: Khách hàng hài lòng với thái độ xử lý nhanh của Quản lý
        
        MGR->>API: PUT /api/v1/reviews/rev-001/resolve { resolutionNotes: "Đã pha lại ly mới chuẩn vị & Tặng voucher 50k xin lỗi, khách hài lòng", managerId: "mgr-01" }
        API->>DB: UPDATE customer_feedbacks SET is_urgent_alert=false, resolution_notes='Đã pha lại ly mới chuẩn vị & Tặng voucher 50k xin lỗi, khách hài lòng', resolved_by='mgr-01', resolved_at=NOW() WHERE id='rev-001'
        API-->>MGR: HTTP 200 OK (Ghi nhận biên bản xử lý khiếu nại thành công)
    else Đánh giá tốt (Rating >= 3 Sao)
        API->>DB: UPDATE customer_feedbacks SET is_urgent_alert=false WHERE id='rev-001'
        API-->>PWA: HTTP 201 Created (Message: "Cảm ơn bạn đã đánh giá! Chúc bạn một ngày tốt lành ❤️")
    end
    deactivate API
```

---

# 9. SEQ-09: QUY TRÌNH MỞ CA, KẾT CA & ĐỐI SOÁT Z-REPORT (GIẢI TRÌNH > 50K)

### 📌 Mô tả Nghiệp vụ (Business Context)
Quản trị chặt chẽ dòng tiền mặt tại quầy thu ngân và chống thất thoát:
1. **Đầu ca (Mở Ca):** Thu ngân khai báo số tiền mặt lẻ ban đầu (`initial_cash`, ví dụ: 1.500.000 VNĐ) lưu vào bảng `work_shifts`.
2. **Trong ca:** Hệ thống tự động ghi nhận doanh thu tiền mặt vào `cash_sales_system`.
3. **Cuối ca (Kết Ca & Đối Soát Z-Report):** Thu ngân kiểm đếm tiền mặt thực tế (`actual_cash_counted`). Hệ thống tự động tính số tiền lý thuyết: $\text{SystemCash} = \text{initial\_cash} + \text{cash\_sales\_system} - \text{cash\_refunds}$ và tính chênh lệch $\text{cash\_difference} = \text{actual\_cash\_counted} - \text{SystemCash}$.
- **Quy tắc giải trình bắt buộc:** Nếu $|\text{cash\_difference}| > 50.000\text{ VNĐ}$, hệ thống khóa nút kết ca, bắt buộc Thu ngân nhập `cashier_explanation` và Quản lý nhập mã PIN duyệt điện tử (`is_approved = true`), đồng thời lưu biên bản vào bảng `shift_handover_discrepancies` mới cho phép xuất báo cáo Z-Report.

```mermaid
sequenceDiagram
    autonumber
    actor CS as 🧑‍💼 Thu Ngân / Trưởng Ca
    participant POS as 💻 Web Staff/Manager Portal ((manager)/shifts)
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (ShiftController)
    participant DB as 🐘 PostgreSQL 16 (work_shifts, payments, shift_handover_discrepancies)
    participant PRN as 🖨️ Máy In Nhiệt Quầy POS
    actor MGR as 🏪 Quản Lý Chi Nhánh

    %% GIAI ĐOẠN 1: MỞ CA ĐẦU NGÀY
    Note over CS,DB: GIAI ĐOẠN 1: MỞ KÉT TIỀN ĐẦU CA
    CS->>POS: Truy cập (manager)/shifts/open -> Đếm tiền lẻ két: 1.500.000đ -> Bấm [Mở Ca]
    POS->>NGINX: POST /api/v1/shifts/open { branchId: "B01", cashierId: "u-cashier-01", shiftName: "Ca Sáng 06:00 - 14:00", initialCash: 1500000 }
    NGINX->>API: Forward Request
    
    activate API
    API->>DB: INSERT INTO work_shifts (branch_id, cashier_id, shift_name, initial_cash, status, opening_time) VALUES ('B01', 'u-cashier-01', 'Ca Sáng', 1500000, 'Open', NOW()) RETURNING id
    DB-->>API: ShiftId = "shift-8831"
    API-->>POS: HTTP 201 Created (ShiftId="shift-8831", Status="Open")
    deactivate API
    POS-->>CS: Màn hình POS chuyển sang trạng thái "Ca đang mở — Sẵn sàng bán hàng!"

    %% GIAI ĐOẠN 2: BÁN HÀNG TRONG CA
    Note over CS,DB: GIAI ĐOẠN 2: BÁN HÀNG TRONG CA (Hệ thống tự động cộng dồn doanh thu Cash vs VietQR)

    %% GIAI ĐOẠN 3: KẾT CA & ĐỐI SOÁT CUỐI NGÀY
    Note over CS,DB: GIAI ĐOẠN 3: KẾT CA & ĐỐI SOÁT Z-REPORT
    CS->>POS: Bấm [Kết Ca & Kiểm Đếm Két Tiền]
    CS->>POS: Nhập bảng kiểm đếm mệnh giá: 10x 500k, 20x 200k, 15x 100k, 10x 50k -> Thực tế: 11.000.000 VNĐ
    
    POS->>NGINX: POST /api/v1/shifts/shift-8831/close-preview { actualCashCounted: 11000000, denominations: [...] }
    NGINX->>API: Forward Request

    activate API
    API->>DB: SELECT initial_cash FROM work_shifts WHERE id='shift-8831'
    DB-->>API: InitialCash = 1500000
    
    API->>DB: SELECT COALESCE(SUM(amount), 0) FROM payments WHERE work_shift_id='shift-8831' AND payment_method='CASH' AND status='Success'
    DB-->>API: CashSales = 9430000
    
    API->>API: SystemCash = 1.500.000 + 9.430.000 - 0 = 10.930.000 VNĐ
    API->>API: CashDifference = 11.000.000 - 10.930.000 = +70.000 VNĐ (Thừa 70k > 50k threshold!)

    API-->>POS: HTTP 200 OK { expectedCash: 10930000, actualCashCounted: 11000000, cashDifference: 70000, requireExplanation: true }
    deactivate API

    %% Bước 4: Bắt buộc giải trình chênh lệch > 50k
    POS-->>CS: ⚠️ Cảnh báo: "Lệch két: +70.000 VNĐ (> 50k). Bắt buộc nhập giải trình & Quản lý ký duyệt PIN!"
    CS->>POS: Nhập lý do: "Khách mua mang về gửi lại 70k tiền bo vào két"
    MGR->>POS: Quản lý kiểm tra & Nhập Mã PIN bảo mật: "9988"
    
    POS->>NGINX: POST /api/v1/shifts/shift-8831/close-finalize
    Note over POS,API: Payload: { actualCashCounted: 11000000, cashierExplanation: "Khách gửi 70k tiền bo", managerPin: "9988" }
    NGINX->>API: Forward Request

    activate API
    API->>DB: BEGIN TRANSACTION
    API->>DB: UPDATE work_shifts SET status='Closed', closing_time=NOW(), cash_sales_system=9430000, actual_cash_counted=11000000, cash_difference=70000, shift_notes='Khách bo 70k' WHERE id='shift-8831'
    API->>DB: INSERT INTO shift_handover_discrepancies (work_shift_id, branch_id, cashier_id, manager_id, discrepancy_amount, discrepancy_type, cashier_explanation, manager_assessment, is_approved, resolved_at) VALUES ('shift-8831', 'B01', 'u-cashier-01', 'mgr-01', 70000, 'SURPLUS', 'Khách mua mang về gửi lại 70k tiền bo vào két', 'Đã đối chiếu hóa đơn hợp lệ', true, NOW())
    API->>DB: COMMIT TRANSACTION

    API-->>POS: HTTP 200 OK (Message: "Đóng ca & Xuất Z-Report thành công")
    deactivate API

    POS->>PRN: Lệnh in Báo Cáo Z-Report ESC/POS (Doanh thu Tiền mặt, VietQR, Chênh lệch, Chữ ký Thu ngân & Quản lý)
    PRN-->>CS: In ra phiếu Báo Cáo Kết Ca Z-Report hoàn tất
```

---

# 10. SEQ-10: QUY TRÌNH QUẢN TRỊ ADMIN — CRUD MENU/BOM, MENU MÙA & AI-2 COMBO

### 📌 Mô tả Nghiệp vụ (Business Context)
1. **CRUD Thực Đơn & BOM Kích Cỡ:** Chủ Chuỗi (`ChainAdmin`) tải ảnh sản phẩm (tự động nén WebP đa kích thước qua ImageSharp và lưu CDN S3), thiết lập công thức BOM chi tiết theo từng kích cỡ (Size M / L) vào các bảng `products`, `product_sizes`, `product_recipes` và phát hành thực đơn đồng bộ qua SignalR.
2. **Lên Lịch Thực Đơn Theo Mùa (Seasonal Menu):** Lên lịch thực đơn Tết / Giáng Sinh tự động kích hoạt vào ngày `start_date` và ẩn khi hết hạn `end_date` thông qua Hangfire Cron Scheduler.
3. **Khai Phá Giỏ Hàng AI-2 (Apriori Engine) & Dự Báo Doanh Thu (Gemini AI):** Thuật toán Apriori tự động phân tích lịch sử đơn hàng 30 ngày từ bảng `orders` và `order_items`, phát hiện các mẫu món mua kèm có chỉ số Lift cao ($\text{Lift} > 1.5$). Admin xem xét, điều chỉnh mức chiết khấu combo và bấm "Phê Duyệt & Xuất Bản" lên Menu PWA.

```mermaid
sequenceDiagram
    autonumber
    actor ADM as 👑 Chủ Chuỗi / Chain Admin
    participant FE as 💻 Next.js Admin Portal ((admin)/menu, /ai)
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (AdminMenu & AI Controller)
    participant S3 as 🗄️ ImageSharp & CDN S3
    participant DB as 🐘 PostgreSQL 16 (products, product_sizes, product_recipes)
    participant RD as ⚡ Redis 7 Cache Store
    participant AI_MINING as 📊 AI-2 Mining Worker (Apriori Engine)
    participant AI_GEMINI as 🤖 Google Gemini 1.5 Flash (Forecasting)
    participant HUB as 📡 SignalR KitchenHub
    participant PWA as 📱 QR Menu Khách Hàng

    %% PHẦN 1: TẢI ẢNH, CRUD MÓN ĂN & CÔNG THỨC BOM
    Note over ADM,DB: PHẦN 1: QUẢN TRỊ THỰC ĐƠN & CÔNG THỨC BOM THEO SIZE
    ADM->>FE: Tải ảnh món "Matcha Latte" (matcha.png, 4MB)
    FE->>NGINX: POST /api/v1/admin/media/upload
    NGINX->>API: Forward File Multipart
    
    activate API
    API->>S3: Validate Magic Bytes -> ImageSharp nén sang WebP (1200px Original & 400px Thumbnail) -> Upload CDN S3
    S3-->>API: Trả về CDN URLs: { originalUrl: "https://cdn.../matcha.webp", thumbUrl: "https://cdn.../thumb.webp" }
    API-->>FE: HTTP 200 OK (CDN URLs)
    deactivate API

    ADM->>FE: Nhập Tên món, Giá cơ bản 55k, Cấu hình BOM Size M (10g Matcha, 150ml Sữa) & Size L (15g Matcha, 200ml Sữa)
    ADM->>FE: Bấm [Lưu & Phát Hành Món]
    FE->>NGINX: POST /api/v1/admin/products
    Note over FE,API: Payload: { name: "Matcha Latte", basePrice: 55000, sizes: [...], recipes: [...], imageUrl: "https://..." }
    NGINX->>API: Forward Request

    activate API
    API->>DB: BEGIN TRANSACTION
    API->>DB: INSERT INTO products (category_id, sku, name, base_price, image_url, is_available) VALUES ('cat-01', 'SKU-MATCHA', 'Matcha Latte', 55000, 'https://...', true) RETURNING id
    DB-->>API: ProductId = "prod-matcha"
    
    API->>DB: INSERT INTO product_sizes (product_id, size_name, price_adjustment, is_default) VALUES ('prod-matcha', 'M', 0, true), ('prod-matcha', 'L', 10000, false)
    API->>DB: INSERT INTO product_recipes (product_id, size_id, ingredient_id, quantity, wastage_rate) VALUES ('prod-matcha', 'size-M', 'ing-matcha', 10, 0.05), ('prod-matcha', 'size-L', 'ing-matcha', 15, 0.05)
    API->>DB: COMMIT TRANSACTION

    API->>RD: DEL menu:branch:* (Xóa toàn bộ Cache Menu cũ)
    API->>HUB: KitchenHub.Clients.All.SendAsync("MenuStructureChanged", { action: "CREATE", productId: "prod-matcha" })
    API-->>FE: HTTP 201 Created (Message: "Tạo món và định mức BOM thành công!")
    deactivate API
    HUB-->>PWA: PWA làm mới danh mục thực đơn tức thì

    %% PHẦN 2: LÊN LỊCH THỰC ĐƠN THEO MÙA (SEASONAL MENU)
    Note over ADM,DB: PHẦN 2: LÊN LỊCH THỰC ĐƠN MÙA VỤ (HANGFIRE SCHEDULER)
    ADM->>FE: Tạo "Thực Đơn Giáng Sinh" (Từ 01/12/2026 đến 31/12/2026) -> Chọn 3 món lễ hội -> Bấm [Lên Lịch]
    FE->>API: POST /api/v1/admin/seasonal-menus { name: "Thực Đơn Giáng Sinh", startDate: "2026-12-01", endDate: "2026-12-31", productIds: [...] }
    API->>DB: INSERT INTO categories (code, name, is_active) VALUES ('CAT-SEASON-XMAS', 'Thực Đơn Giáng Sinh', true)
    API-->>FE: HTTP 201 Created (Message: "Lên lịch thực đơn mùa vụ thành công!")

    %% PHẦN 3: KHAI PHÁ AI-2 APRIORI COMBO & GEMINI FORECASTING
    Note over AI_MINING,PWA: PHẦN 3: KHAI PHÁ APRIORI COMBO & GEMINI DỰ BÁO NHU CẦU
    AI_MINING->>DB: Quét tập 5.000 đơn hàng 30 ngày qua từ orders & order_items -> Chạy Apriori (Support >= 0.05, Confidence >= 0.70, Lift > 1.5)
    AI_MINING->>RD: HSET ai:combo_suggestions "sug-102" "{ rule: '{Matcha Latte} => {Croissant Bơ}', lift: 2.45, support: 0.08, status: 'Pending' }"
    
    ADM->>FE: Mở tab [AI Combo Suggestions] -> Xem đề xuất: "Matcha Latte + Bánh Croissant (Lift: 2.45)"
    ADM->>FE: Đặt tên "Combo Chiều Thư Thái", chỉnh Giảm giá 15% (Từ 90k còn 76.500đ) -> Bấm [Phê Duyệt & Xuất Bản]
    
    FE->>API: POST /api/v1/admin/ai/combos/approve { suggestionId: "sug-102", comboName: "Combo Chiều Thư Thái", discountRate: 0.15 }
    activate API
    API->>DB: INSERT INTO products (sku, name, base_price, is_available) VALUES ('SKU-COMBO-01', 'Combo Chiều Thư Thái', 76500, true)
    API->>RD: DEL menu:combos:*
    API-->>FE: HTTP 200 OK (Message: "Combo mới đã được phát hành lên đầu Menu PWA!")
    deactivate API

    FE-->>ADM: Banner Xanh: "Combo Chiều Thư Thái đã hiển thị ưu tiên trên trang chủ PWA!"
    PWA->>RD: GET menu:combos -> Tải Combo mới lên vị trí đầu trang thực đơn
```

---

# 11. BẢNG ĐỐI CHIẾU 10 SEQUENCE VỚI MA TRẬN 62 TÍNH NĂNG VÀ 16 WORKFLOWS

| Sơ đồ Tuần tự | Mã Nghiệp Vụ Cốt Lõi | Mã Tính Năng Phân Quyền (RBAC) | Giao thức Thời Gian Thực (SignalR Events) | Khóa Phân Tán / Transaction & Bảng 3NF Chuẩn |
|---|---|---|---|---|
| **Seq-01** | `WF-01A` (Dine-In VietQR Trước) | `C-01` ~ `C-06`, `C-10`, `S-03` | `PaymentReceived`, `NewKitchenOrder`, `OrderStatusUpdated`, `OrderExpired` | `RedLock.AcquireAsync("lock:table:{id}")`, Redis Soft Reservation `inventory:reserved:{id}` (TTL 600s), `orders`, `order_items`, `payments`, `transactions`, `inventory_stocks`, `inventory_logs`, `tables` |
| **Seq-02** | `WF-01B` (Dine-In Tiền Mặt Trả Sau) | `C-01` ~ `C-06`, `S-04`, `S-07` | `NewKitchenOrder`, `OrderStatusUpdated`, `OrderPaid`, `TablePaidNotification` | In nhiệt ESC/POS VietQR Bill, `orders`, `order_items`, `payments`, `work_shifts.cash_sales_system`, `tables` |
| **Seq-03** | `WF-02` (QR Delivery Ship 20k) | `C-07`, `C-08`, `S-03`, `S-05` | `PaymentReceived`, `NewKitchenOrder`, `DeliveryReadyForPickup`, `OrderStatusUpdated` | FluentValidation Phone/Address, Soft Reservation `inventory:reserved`, `orders`, `delivery_orders`, `payments`, `transactions`, `inventory_stocks`, `inventory_logs` |
| **Seq-04** | `WF-03` (Takeaway Web POS 10 Ly) | `S-01`, `S-02`, `S-04`, `C-13` | `NewKitchenOrder`, `OrderStatusUpdated` | Atomic Calculation CRM `(10 - 10 + N)`, `customers.cup_balance`, `loyalty_cup_transactions`, `orders`, `payments`, `work_shifts` |
| **Seq-05** | `WF-04` (Chấm Công Khóa WiFi) | `S-11`, `M-06`, `A-07` | `StaffAttendanceLogged` | Double Verification: `branch_wifi_configs.allowed_ip_subnets` + `bssid_list`, `users`, `roles`, `user_roles`, `staff_attendances` |
| **Seq-06** | `WF-05`, `WF-06`, `WF-10` | `S-03`, `S-06`, `M-02`, `M-03` | `NewKitchenOrder`, `Item86Toggled`, `LowStockAlert` | BOM Auto-deduction `product_recipes`, `inventory_stocks.current_quantity`, `inventory_logs`, Redis Hash 86-Out-of-stock, `products.is_available` |
| **Seq-07** | `WF-07` (Gọi Phục Vụ Tại Bàn) | `C-11`, `S-08` | `ServiceCallAlert`, `ServiceCallResolved` | Redis Rate Limit `SET lock:ratelimit:call:{id} EX 60`, Redis Transient State `branch:{id}:active_service_calls` |
| **Seq-08** | `WF-08` (Review & Red Alert <= 2) | `C-14`, `M-07`, `A-11` | `UrgentRedAlert` | Gemini 1.5 Flash Sentiment Analysis, S3 CDN Upload, `customer_feedbacks.rating_stars`, `is_urgent_alert`, `resolution_notes`, `resolved_by` |
| **Seq-09** | `WF-09` (Mở/Kết Ca & Z-Report) | `S-12`, `M-04`, `M-05`, `A-15` | `ShiftStatusChanged` | Z-Report Cash Reconciliation, Mandatory Explanation > 50k, `work_shifts`, `payments`, `shift_handover_discrepancies` |
| **Seq-10** | `WF-11`, `WF-12`, `WF-13`, `WF-15` | `A-01` ~ `A-06`, `A-13`, `A-14` | `MenuStructureChanged` | ImageSharp WebP Pipeline, Apriori Mining Engine, `products`, `product_sizes`, `product_recipes`, `categories`, `ingredients` |

---

# 12. HƯỚNG DẪN KIỂM CHỨNG & TÍCH HỢP HỆ THỐNG

> [!IMPORTANT]
> **Quy chuẩn tích hợp:**
> 1. **SignalR Reconnect Strategy:** Tất cả các Client (PWA, Web POS, Web KDS) bắt buộc cài đặt cơ chế tự động kết nối lại (`withAutomaticReconnect([0, 2000, 5000, 10000, 30000])`) khi mất kết nối mạng.
> 2. **Webhook Idempotency:** Mọi Webhook từ PayOS bắt buộc kiểm tra khóa phân tán `SETNX lock:webhook:payos:{paymentId} EX 60` trong Redis trước khi xử lý DB Transaction nhằm loại bỏ 100% rủi ro cộng trùng tiền khi Gateway retry.
> 3. **Cơ chế Soft Inventory Reservation:** Mọi đơn hàng thanh toán trả trước (VietQR) bắt buộc thực hiện kiểm tra tồn kho và giữ chỗ tạm thời (Soft Reserve) trong Redis với thời gian hết hạn (TTL 600s). Khi thanh toán thành công, hệ thống chuyển từ giữ chỗ sang trừ tồn kho vật lý vĩnh viễn trong `inventory_stocks` và ghi `inventory_logs`. Trường hợp quá hạn hoặc hủy đơn, hệ thống tự động hoàn trả số lượng đã giữ chỗ để đảm bảo không bị rò rỉ tồn kho hay bán vượt số lượng thực tế (Overselling).
> 4. **Audit Trail & Biên Bản Bất Biến:** Mọi thao tác hủy món, hoàn tiền, giải trình chênh lệch két tiền > 50.000 VNĐ bắt buộc ghi bản ghi vào bảng `shift_handover_discrepancies` và `inventory_logs` kèm ID người thực hiện và xác nhận điện tử của Quản lý.
"""
