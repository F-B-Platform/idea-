import sys

def get_part2():
    return """
---

# 3. SEQ-03: QUY TRÌNH ĐẶT MÓN GIAO HÀNG (QR DELIVERY) — PHÍ SHIP 20K & 100% VIETQR

### 📌 Mô tả Nghiệp vụ (Business Context)
Khách hàng quét mã QR Delivery từ standee/fanpage hoặc truy cập đường link giao hàng từ xa.
- **Quy tắc cốt lõi:** Form đặt hàng bắt buộc xác thực Họ tên, **Số điện thoại (10 chữ số chuẩn VN regex `^0[0-9]{9}$`)** và **Địa chỉ nhận hàng chi tiết** (tối thiểu 10 ký tự).
- Hệ thống tự động áp dụng **Phí giao hàng cố định 20.000 VNĐ** (`delivery_fee = 20000`) vào tổng đơn.
- **100% Bắt buộc thanh toán trước qua VietQR** (Khóa hoàn toàn hình thức COD/Tiền mặt).
- **Cơ chế Soft Inventory Reservation:** Kiểm tra tồn kho khả dụng và tạm giữ nguyên liệu trong Redis (`inventory:reserved:{branch_id}`) trong 10 phút. Nếu quá hạn không thanh toán, worker tự động hoàn trả số lượng tạm giữ.
- Bếp nhận vé có huy hiệu xanh lục nổi bật **`[DELIVERY]`** kèm thông tin địa chỉ & SĐT để pha chế, dán tem nắp chống tràn và đóng gói bàn giao cho Shipper nội bộ chi nhánh.

```mermaid
sequenceDiagram
    autonumber
    actor C as 👤 Khách Hàng (Tại nhà / Cơ quan)
    participant PWA as 📱 Next.js Delivery PWA
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (DeliveryController)
    participant REDIS as ⚡ Redis 7 (RedLock & Soft Reservation)
    participant DB as 🐘 PostgreSQL 16 (EF Core)
    participant PAY as 🏦 Cổng PayOS Gateway
    participant HUB as 📡 SignalR (Kitchen & Order Hub)
    actor KDS as 🧋 Barista / Đóng Gói (Web KDS)
    actor SHP as 🛵 Shipper Chi Nhánh

    %% Bước 1: Khách nhập thông tin & Chọn món
    C->>PWA: Quét QR Delivery / Truy cập Web Delivery
    C->>PWA: Nhập Họ tên: "Trần Thị Lan", SĐT: "0988776655", Địa chỉ: "Tòa Diamond Plaza, 34 Lê Duẩn, Q1"
    C->>PWA: Chọn 2x Trà Đào Cam Sả Size L (80.000đ)
    PWA->>PWA: Tự động cộng Phí giao hàng cố định: +20.000đ -> Tổng thanh toán: 100.000đ
    C->>PWA: Bấm chọn [Thanh toán VietQR & Đặt Giao Hàng]

    %% Bước 2: Backend Validation, Tồn kho Khả dụng & Tạo Đơn
    PWA->>NGINX: POST /api/v1/orders/delivery
    Note over PWA,API: Payload: { recipientName, recipientPhone, deliveryAddress, deliveryFee: 20000, items: [...] }
    NGINX->>API: Forward Request

    activate API
    API->>API: FluentValidation: Kiểm tra Phone Regex & Length(Address) >= 10 & DeliveryFee == 20000
    
    alt Dữ liệu không hợp lệ (Ví dụ: Thiếu địa chỉ / SĐT sai)
        API-->>PWA: HTTP 422 Unprocessable Entity (RFC 7807 ProblemDetails: "Địa chỉ giao hàng không hợp lệ")
        PWA-->>C: Báo lỗi trên Form nhập liệu
    else Dữ liệu hợp lệ
        API->>REDIS: RedLock.AcquireAsync("lock:inventory:branch:B01", expire=5s)
        API->>DB: SELECT r.ingredient_id, r.quantity FROM product_recipes r WHERE r.product_id='prod-tra-dao' AND r.size_id='size-L'
        DB-->>API: RecipeData { TraDao: 30g, DaoNgam: 50g, CamTuoi: 40g } (x2 Ly = 60g Trà, 100g Đào, 80g Cam)
        
        API->>DB: SELECT s.ingredient_id, s.current_quantity FROM inventory_stocks s WHERE s.branch_id='B01' AND s.ingredient_id IN ('ing-tea', 'ing-peach', 'ing-orange')
        DB-->>API: CurrentStockData { Tra: 3000g, Dao: 2000g, Cam: 1500g }
        
        API->>REDIS: HGETALL inventory:reserved:B01
        REDIS-->>API: ReservedData { Tra: 100g, Dao: 200g, Cam: 100g }
        
        API->>API: Kiểm tra: current_quantity - reserved_stock >= required_qty (Đủ hàng)
        
        %% Soft Reserve nguyên liệu trong Redis (TTL 600s)
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-tea 60
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-peach 100
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-orange 80
        API->>REDIS: EXPIRE inventory:reserved:B01 600
        API->>REDIS: RedLock.ReleaseAsync("lock:inventory:branch:B01")
        
        API->>DB: BEGIN TRANSACTION
        API->>DB: INSERT INTO orders (order_code='DEL-B01-0055', branch_id='B01', order_type='DELIVERY', status='PendingPayment', sub_total=80000, delivery_fee=20000, total_amount=100000, expires_at=NOW()+INTERVAL '10 min')
        API->>DB: INSERT INTO order_items (order_id, product_id, size_id, quantity=2, unit_price=40000, total_price=80000, status='PendingPayment')
        API->>DB: INSERT INTO delivery_orders (order_id, recipient_name='Trần Thị Lan', recipient_phone='0988776655', delivery_address='Tòa Diamond Plaza, 34 Lê Duẩn, Q1', delivery_fee=20000, delivery_status='PendingPayment')
        API->>DB: INSERT INTO payments (order_id, payment_method='VIETQR', amount=100000, status='Pending', transfer_content='DEL_B01_0055')
        API->>DB: COMMIT TRANSACTION

        API->>PAY: POST /v2/payment-requests (Amount=100000, Description="DEL_B01_0055")
        PAY-->>API: Trả về PaymentLink (PaymentLinkId="plink_9912", QrCodeDataUrl, CheckoutUrl)
        API-->>PWA: HTTP 201 Created (OrderId="del-0055", QrCodeUrl, TotalAmount=100000, ExpiresAt="10:00")
    end
    deactivate API

    %% Bước 3: Thanh toán VietQR & Nhận Webhook
    PWA-->>C: Hiển thị mã VietQR 100.000 VNĐ kèm đồng hồ đếm ngược 10:00
    
    alt Nhánh A1: Khách Chuyển Khoản Thành Công
        C->>PAY: Mở App Ngân Hàng -> Quét QR -> Chuyển 100.000đ
        PAY->>NGINX: POST /api/v1/webhooks/payos (HMAC-SHA256, DEL_B01_0055, 100000đ)
        NGINX->>API: Forward Webhook

        activate API
        API->>API: Verify HMAC-SHA256 & Idempotency Key (SETNX lock:webhook:payos:DEL_B01_0055 EX 60)
        API->>DB: BEGIN TRANSACTION
        API->>DB: UPDATE payments SET status='Success', confirmed_at=NOW() WHERE transfer_content='DEL_B01_0055'
        API->>DB: INSERT INTO transactions (payment_id, gateway_transaction_id=..., amount=100000, is_verified=true)
        API->>DB: UPDATE orders SET status='Confirmed', paid_at=NOW() WHERE id='del-0055'
        API->>DB: UPDATE delivery_orders SET delivery_status='Preparing' WHERE order_id='del-0055'
        
        %% Khấu trừ Tồn kho Vật lý Vĩnh viễn
        API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 60 WHERE branch_id='B01' AND ingredient_id='ing-tea'
        API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 100 WHERE branch_id='B01' AND ingredient_id='ing-peach'
        API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 80 WHERE branch_id='B01' AND ingredient_id='ing-orange'
        
        API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-60, notes='Deducted for del-0055')
        API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-100, notes='Deducted for del-0055')
        API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-80, notes='Deducted for del-0055')
        API->>DB: COMMIT TRANSACTION
        
        %% Giải phóng Tồn kho Tạm giữ trên Redis
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-tea -60
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-peach -100
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-orange -80
        
        API->>HUB: OrderHub.Clients.Group("order_del-0055").SendAsync("PaymentReceived", { orderId: "del-0055" })
        API->>HUB: KitchenHub.Clients.Group("branch_B01_kitchen").SendAsync("NewKitchenOrder", DeliveryTicketDto)
        API-->>PAY: HTTP 200 OK
        deactivate API

        par Phản hồi Realtime
            HUB-->>PWA: Event `PaymentReceived` -> PWA: "Thanh toán thành công! Quán đang pha chế & đóng gói 🛵"
            HUB-->>KDS: KDS hiện vé `[DELIVERY #DEL-0055]` (Xanh lục nổi bật kèm SĐT & Địa chỉ giao hàng)
        end
    else Nhánh A2: Đơn Giao Hàng Quá Hạn Quét Mã 10 Phút
        API->>DB: UPDATE orders SET status='Cancelled' WHERE id='del-0055'
        API->>DB: UPDATE delivery_orders SET delivery_status='Cancelled' WHERE order_id='del-0055'
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-tea -60
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-peach -100
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-orange -80
        API->>HUB: OrderHub.Clients.Group("order_del-0055").SendAsync("OrderExpired", { orderId: "del-0055" })
    end

    %% Bước 4: Pha chế, Đóng gói & Giao hàng
    KDS->>API: PATCH /api/v1/kds/orders/del-0055/status { status: "Preparing" }
    KDS->>KDS: Pha chế đồ uống -> Dán tem nắp ly chống tràn -> Đóng túi niêm phong -> Dán tem địa chỉ
    KDS->>API: PATCH /api/v1/kds/orders/del-0055/status { status: "Ready" }
    API->>DB: UPDATE delivery_orders SET delivery_status='ReadyForPickup' WHERE order_id='del-0055'
    API->>HUB: NotificationHub.Clients.Group("branch_B01_staff").SendAsync("DeliveryReadyForPickup", "del-0055")
    
    SHP->>KDS: Nhận túi đồ uống niêm phong
    SHP->>API: PATCH /api/v1/delivery/del-0055/assign-driver { driverName: "Lê Văn Hùng", driverPhone: "0912345678" }
    API->>DB: UPDATE delivery_orders SET driver_name='Lê Văn Hùng', driver_phone='0912345678', delivery_status='Delivering', dispatched_at=NOW() WHERE order_id='del-0055'
    
    SHP->>C: Vận chuyển đến "Tòa Diamond Plaza, 34 Lê Duẩn, Q1" -> Giao tận tay khách hàng
    SHP->>API: POST /api/v1/orders/del-0055/delivery-complete
    API->>DB: UPDATE delivery_orders SET delivery_status='Delivered', delivered_at=NOW() WHERE order_id='del-0055'
    API->>DB: UPDATE orders SET status='Completed', completed_at=NOW() WHERE id='del-0055'
    API->>HUB: OrderHub.Clients.Group("order_del-0055").SendAsync("OrderStatusUpdated", "Completed")
    HUB-->>PWA: PWA thông báo: "Đơn hàng đã giao thành công! Chúc bạn thưởng thức ngon miệng 🎉"
```

---

# 4. SEQ-04: QUY TRÌNH BÁN HÀNG MANG ĐI (TAKEAWAY WEB POS) — TÍCH ĐIỂM 10 LY

### 📌 Mô tả Nghiệp vụ (Business Context)
Khách hàng tới quầy mua đồ uống mang về.
- **Quy tắc cốt lõi:** Khách hàng **KHÔNG QUÉT QR**; Thu ngân thao tác 100% trên giao diện **Web POS Quầy** `(staff)/pos`.
- Thu ngân tra cứu CRM bằng Số điện thoại từ bảng `customers`. 
- **Chính sách Loyalty (10 ly tặng 1 ly):** CHỈ áp dụng riêng cho đơn Takeaway tại quầy. Khi khách tích lũy đủ 10 ly (`cup_balance >= 10`), hệ thống kích hoạt nút `[Đổi 1 Ly Free]`, tự động trừ 100% giá của 1 ly tiêu chuẩn trong giỏ hàng.
- Lưu lại lịch sử biến động điểm trong bảng `loyalty_cup_transactions` (`cups_changed = -10` khi đổi thưởng, `cups_changed = +N` khi tích mới).
- Khách nhận đồ uống và thanh toán sau bằng Tiền mặt (POS tính tiền thối) hoặc VietQR quầy.

```mermaid
sequenceDiagram
    autonumber
    actor C as 👤 Khách Hàng (Tại quầy)
    actor CS as 🧑‍💼 Thu Ngân (Cashier)
    participant POS as 💻 Web Staff POS Portal
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (PosOrder & CRM Controller)
    participant DB as 🐘 PostgreSQL 16 (customers & loyalty_cup_transactions)
    participant HUB as 📡 SignalR KitchenHub
    actor KDS as 🧋 Barista (Web KDS Bếp)
    participant PRN as 🖨️ Máy In Hóa Đơn POS

    %% Bước 1: Khách đọc SĐT & Tra cứu CRM
    C->>CS: "Cho mình 2 Cà phê Muối mang về, SĐT mình: 0909123456"
    CS->>POS: Nhập "0909123456" vào ô tìm kiếm CRM
    POS->>NGINX: GET /api/v1/crm/customers/lookup?phone=0909123456
    NGINX->>API: Forward Request

    activate API
    API->>DB: SELECT id, full_name, cup_balance, total_cups_earned FROM customers WHERE phone = '0909123456' AND is_deleted = false
    DB-->>API: CustomerRecord { id: "c-8821", full_name: "Nguyễn Hoàng Nam", cup_balance: 10, total_cups_earned: 24 }
    API-->>POS: HTTP 200 OK (CustomerId="c-8821", Name="Nguyễn Hoàng Nam", CupBalance=10, CanRedeem=true)
    deactivate API

    POS-->>CS: Hiển thị Huy hiệu Vàng: "🎁 KHÁCH ĐỦ 10 LY — ĐỦ ĐIỀU KIỆN ĐỔI 1 LY MIỄN PHÍ"
    CS->>C: "Anh Nam đang có 10 ly tích lũy, anh có muốn đổi 1 ly miễn phí hôm nay không ạ?"
    C->>CS: "Có, đổi giúp mình 1 ly nhé!"

    %% Bước 2: Chọn món & Áp dụng Đổi Thưởng
    CS->>POS: Chọn 2x Cà phê Muối (70.000đ) -> Bấm [Áp Dụng Đổi 1 Ly Free (-35.000đ)]
    POS->>POS: Tính lại Tổng thanh toán: 70.000đ - 35.000đ = 35.000 VNĐ
    CS->>POS: Bấm [Tạo Đơn & Gửi Bếp]

    POS->>NGINX: POST /api/v1/pos/orders/takeaway
    Note over POS,API: Payload: { customerId: "c-8821", items: [...], redeemFreeCup: true, totalAmount: 35000 }
    NGINX->>API: Forward Request

    activate API
    API->>DB: BEGIN TRANSACTION
    API->>DB: INSERT INTO orders (order_code='TK-B01-0089', branch_id='B01', customer_id='c-8821', order_type='TAKEAWAY', status='Confirmed', table_id=NULL, sub_total=70000, discount_amount=35000, total_amount=35000)
    API->>DB: INSERT INTO order_items (order_id, product_id, size_id, quantity=2, unit_price=35000, total_price=70000, status='Confirmed')
    API->>DB: COMMIT TRANSACTION

    API->>HUB: KitchenHub.Clients.Group("branch_B01_kitchen").SendAsync("NewKitchenOrder", TakeawayTicketDto)
    API-->>POS: HTTP 201 Created (OrderId="tk-0089", OrderCode="TK-B01-0089", TotalAmount=35000)
    deactivate API

    HUB-->>KDS: KDS phát chuông 🔔 & Xuất hiện vé `[MANG VỀ #TK-B01-0089]`
    KDS->>API: PATCH Status -> Preparing -> Ready (Pha chế & Đóng túi mang đi)
    HUB-->>POS: Web POS báo chuông: "Đơn mang về #TK-B01-0089 đã sẵn sàng!"

    %% Bước 3: Thu tiền & Cập nhật Loyalty CRM
    CS->>C: Bàn giao túi đồ uống: "Tổng tiền của anh là 35.000đ ạ."
    C->>CS: Đưa 100.000đ tiền mặt
    CS->>POS: Nhập Tiền Khách Đưa: 100.000đ -> POS tính Tiền Thối: 65.000đ -> Bấm [Hoàn Tất & In Bill]

    POS->>NGINX: POST /api/v1/pos/orders/tk-0089/finalize-payment
    Note over POS,API: Payload: { paymentMethod: "CASH", amountGiven: 100000, changeAmount: 65000 }
    NGINX->>API: Forward Request

    activate API
    API->>DB: BEGIN TRANSACTION
    API->>DB: UPDATE orders SET status='Completed', paid_at=NOW(), completed_at=NOW() WHERE id='tk-0089'
    API->>DB: INSERT INTO payments (order_id, payment_method='CASH', amount=35000, status='Success', confirmed_at=NOW())
    
    %% Cập nhật bảng customers và ghi sổ loyalty_cup_transactions
    API->>DB: UPDATE customers SET cup_balance = (10 - 10 + 2), total_free_cups_redeemed = total_free_cups_redeemed + 1, total_cups_earned = total_cups_earned + 2, total_spent = total_spent + 35000, last_visit_at=NOW() WHERE id='c-8821'
    API->>DB: INSERT INTO loyalty_cup_transactions (customer_id, order_id, transaction_type='REDEEM_FREE_CUP', cups_changed=-10, cup_balance_after=0, notes='Đổi 1 ly miễn phí đơn mang về')
    API->>DB: INSERT INTO loyalty_cup_transactions (customer_id, order_id, transaction_type='EARN_CUPS', cups_changed=+2, cup_balance_after=2, notes='Tích lũy 2 ly từ đơn mang về TK-0089')
    
    API->>DB: UPDATE work_shifts SET cash_sales_system = cash_sales_system + 35000 WHERE id=current_shift_id AND status='Open'
    API->>DB: COMMIT TRANSACTION

    API-->>POS: HTTP 200 OK (NewCupBalance=2, ChangeReturned=65000)
    deactivate API

    POS->>PRN: Lệnh in Bill ESC/POS (Hóa đơn bán lẻ + Thông tin tích lũy: 2/10 ly)
    PRN-->>CS: In ra tờ Hóa đơn thanh toán
    CS->>C: Gửi lại 65.000đ tiền thừa + Hóa đơn: "Cảm ơn anh Nam, anh đã tích lũy lại 2 ly mới ạ!"
```
"""
