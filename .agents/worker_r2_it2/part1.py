import sys

def get_part1():
    return """# 🔄 SƠ ĐỒ TUẦN TỰ TOÀN DIỆN (SEQUENCE DIAGRAMS SPECIFICATION)
## SMART F&B OPERATING SYSTEM — 10 CORE ARCHITECTURAL FLOWS

> [!NOTE]
> **Mã tài liệu:** `SPEC-SEQ-02` | **Phiên bản:** `v2.5.0-Production-Ready`  
> **Hệ thống:** Smart F&B Operating System (Smart F&B OS) — Nền tảng F&B Chuỗi Đa Chi Nhánh  
> **Kiến trúc nền tảng:** .NET 8 Web API Clean Architecture & CQRS + Next.js 14 App Router + PostgreSQL 16 Enterprise (31 Bảng Chuẩn 3NF) + Redis 7 (RedLock Khóa Phân Tán & Soft Inventory Reservation) + SignalR WebSockets (4 Hubs Chuyên Biệt) + PayOS VietQR Gateway + Google Gemini 1.5 Flash AI  
> **Tiêu chuẩn thiết kế:** 100% Cú pháp Mermaid `sequenceDiagram`, Zero Placeholders, đặc tả chi tiết giao thức RESTful (Payloads, Status Codes, RFC 7807), WebSockets Real-time Hubs, Khóa phân tán RedLock, HMAC-SHA256 Webhook Ingestion, cơ chế Soft Inventory Reservation (chống Overselling giờ cao điểm), và cơ chế Rollback/Idempotency.

---

# 📑 MỤC LỤC 10 SƠ ĐỒ TUẦN TỰ HỆ THỐNG

1. [Seq-01: Quy Trình Gọi Món Tại Bàn (Dine-In) — Nhánh A: Trả Trước Qua VietQR (Soft Inventory Reservation, PayOS Webhook & SignalR KDS Push)](#1-seq-01-quy-trình-gọi-món-tại-bàn-dine-in--nhánh-a-trả-trước-qua-vietqr)
2. [Seq-02: Quy Trình Gọi Món Tại Bàn (Dine-In) — Nhánh B: Trả Sau (Tiền Mặt / Quét QR In Trên Bill Tại Quầy POS)](#2-seq-02-quy-trình-gọi-món-tại-bàn-dine-in--nhánh-b-trả-sau-tiền-mặt--quét-qr-bill)
3. [Seq-03: Quy Trình Đặt Món Giao Hàng (QR Delivery) — Phí Ship 20.000 VNĐ, Soft Inventory Reservation & 100% VietQR Trả Trước](#3-seq-03-quy-trình-đặt-món-giao-hàng-qr-delivery--phí-ship-20k--100-vietqr)
4. [Seq-04: Quy Trình Bán Hàng Mang Đi (Takeaway Web POS) — Tích Điểm CRM 10 Ly Tặng 1 & In Hóa Đơn](#4-seq-04-quy-trình-bán-hàng-mang-đi-takeaway-web-pos--tích-điểm-10-ly)
5. [Seq-05: Quy Trình Chấm Công Nhân Viên Khóa WiFi — Xác Thực Kép BSSID Router & IP Subnet Chi Nhánh](#5-seq-05-quy-trình-chấm-công-nhân-viên-khóa-wifi--xác-thực-bssid--ip-subnet)
6. [Seq-06: Quy Trình Xử Lý Đơn Bếp (KDS), Khấu Trừ Định Lượng BOM Theo Gam/Ml & Công Tắc 86-Toggle Khóa Món](#6-seq-06-quy-trình-xử-lý-đơn-bếp-kds-khấu-trừ-bom--công-tắc-86-toggle)
7. [Seq-07: Quy Trình Gọi Phục Vụ Tại Bàn & Tiếp Nhận Chuông Báo Thời Gian Thực Qua SignalR](#7-seq-07-quy-trình-gọi-phục-vụ-tại-bàn--tiếp-nhận-chuông-báo-signalr)
8. [Seq-08: Quy Trình Đánh Giá 1-5 Sao, Phân Tích Cảm Xúc Gemini AI & Kích Hoạt Red Alert Quản Lý (Rating <= 2)](#8-seq-08-quy-trình-đánh-giá-1-5-sao-ai-sentiment--kích-hoạt-red-alert)
9. [Seq-09: Quy Trình Mở Ca, Kết Ca & Đối Soát Doanh Thu Z-Report (Bắt Buộc Giải Trình Chênh Lệch > 50k)](#9-seq-09-quy-trình-mở-ca-kết-ca--đối-soát-z-report-giải-trình-chênh-lệch)
10. [Seq-10: Quy Trình Quản Trị Viên (Admin Operations) — CRUD Menu/BOM, Menu Mùa Vụ & Phê Duyệt AI-2 Combo](#10-seq-10-quy-trình-quản-trị-admin--crud-menubom-menu-mùa--ai-2-combo-apriori)

---

## 🏛️ BẢNG TỔNG HỢP CÁC THÀNH PHẦN THAM GIA (SYSTEM PARTICIPANTS)

| Ký hiệu Participant | Loại hình | Trách nhiệm kiến trúc & Công nghệ |
|---|---|---|
| `👤 Khách Hàng / Nhân Sự` | **Actor** | Người dùng tương tác trực tiếp (Thực khách, Thu ngân, Barista, Quản lý, Chủ chuỗi). |
| `📱 Next.js Web App` | **Boundary (Client)** | Ứng dụng Frontend Next.js 14 App Router (Customer PWA, Web POS, Web KDS, Manager/Admin Portal). |
| `🛡️ NGINX Reverse Proxy` | **Ingress Gateway** | Điều phối tải, chấm dứt SSL/TLS Let's Encrypt, trích xuất Header `X-Forwarded-For`, Rate Limiting. |
| `⚙️ .NET 8 API Controller` | **Control (Backend)** | ASP.NET Core 8 Web API, MediatR CQRS Command/Query Handlers, FluentValidation, Domain Services. |
| `⚡ Redis 7 (RedLock/Cache)` | **Distributed Cache & Lock** | Khóa phân tán RedLock, Bộ đếm Tồn kho Tạm giữ (Soft Reservation TTL 600s), Cache Menu, Rate Limiting. |
| `🐘 PostgreSQL 16 DB` | **Database (Storage)** | Cơ sở dữ liệu quan hệ chuẩn hóa 31 thực thể 3NF, lưu trữ giao dịch ACID qua Entity Framework Core 8. |
| `📡 SignalR Realtime Hubs` | **Realtime Transport** | 4 Hubs WebSockets chuyên biệt (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) với Redis Backplane. |
| `🏦 Cổng PayOS (VietQR)` | **External Gateway** | Cổng thanh toán quốc gia VietQR, sinh mã QR động và gửi Webhook giao dịch kèm chữ ký HMAC-SHA256. |
| `🤖 Google Gemini 1.5 Flash` | **External AI Engine** | Xử lý ngôn ngữ tự nhiên (RAG Chatbot), phân tích cảm xúc đánh giá (Sentiment Analysis), dự báo nhu cầu. |
| `🖨️ Máy In Hóa Đơn (ESC/POS)` | **Hardware Device** | Máy in nhiệt tại quầy/bar in hóa đơn tạm tính, mã VietQR, tem dán ly và biên bản kết ca Z-Report. |

---

# 1. SEQ-01: QUY TRÌNH GỌI MÓN TẠI BÀN (DINE-IN) — NHÁNH A: TRẢ TRƯỚC QUA VIETQR

### 📌 Mô tả Nghiệp vụ (Business Context)
Khách hàng ngồi tại bàn, quét mã QR vật lý gắn trên bàn để mở thực đơn số PWA. Khách tùy biến đồ uống (Size, Mức đường, Mức đá, Topping), nhập số điện thoại tích điểm CRM và lựa chọn **"Thanh toán Chuyển khoản VietQR (Trả trước)"**. 
- **Cơ chế Khóa Phân Tán & Giữ Tồn Kho Tạm Thời (Soft Inventory Reservation):**
  1. Khi nhận yêu cầu tạo đơn, Backend sử dụng RedLock khóa tài nguyên bàn (`lock:table:T04`) và kiểm tra tồn kho khả dụng (`available_stock = physical_stock - reserved_stock >= required_bom_qty`) dựa trên bảng `product_recipes` và `inventory_stocks`.
  2. Hệ thống tạm giữ số lượng nguyên liệu trong Redis (`HINCRBY inventory:reserved:{branch_id} {ingredient_id} {qty}` với TTL 600s) và đổi trạng thái bàn thành `Occupied_PendingPayment` trong DB/Redis để chặn tạo đơn trùng tại cùng 1 bàn.
  3. Đơn hàng khởi tạo ở trạng thái `PendingPayment` với thời hạn quét mã QR là 10 phút (`expires_at = NOW() + INTERVAL '10 min'`). Màn hình KDS quầy pha chế **TUYỆT ĐỐI CHƯA HIỂN THỊ** đơn hàng này.
- **Xử lý Webhook PayOS (HMAC-SHA256) & Khấu trừ Thực tế:**
  - Ngay khi PayOS gửi Webhook xác nhận thanh toán thành công (kèm chữ ký bảo mật HMAC-SHA256), hệ thống đổi trạng thái đơn sang `Confirmed` và `paid_at = NOW()`, khấu trừ trực tiếp tồn kho vật lý trong `inventory_stocks`, giải phóng `inventory:reserved` trong Redis, ghi nhật ký `inventory_logs`, và bắn sự kiện thời gian thực qua SignalR `KitchenHub` để KDS quầy bar phát chuông tiếp nhận pha chế.
- **Xử lý Quá hạn / Hủy đơn (Compensation Rollback):**
  - Nếu quá thời hạn 10 phút hoặc khách hủy đơn, worker tự động hủy đơn, giải phóng nguyên liệu tạm giữ trong Redis (`HINCRBY inventory:reserved -qty`) và mở khóa bàn về trạng thái `Available`.

```mermaid
sequenceDiagram
    autonumber
    actor C as 👤 Khách Hàng (Tại bàn)
    participant PWA as 📱 Next.js PWA (Customer)
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (OrderController)
    participant REDIS as ⚡ Redis 7 (RedLock & Soft Reservation)
    participant DB as 🐘 PostgreSQL 16 (EF Core)
    participant PAY as 🏦 Cổng PayOS (VietQR)
    participant HUB as 📡 SignalR (Kitchen & Payment Hub)
    actor KDS as 🧋 Barista (Web KDS Bếp)
    actor ST as 🧑‍💼 Nhân Viên Phục Vụ

    %% Bước 1: Quét QR & Chọn món
    C->>PWA: Quét mã QR Bàn 04 (URL: /menu?branch=B01&table=T04&sig=a8f9...)
    PWA->>NGINX: GET /api/v1/menu/items?branchId=B01
    NGINX->>API: Forward request
    API->>REDIS: GET menu:branch:B01:active
    REDIS-->>API: Trả về Cache Menu DTOs
    API-->>PWA: HTTP 200 OK (Danh mục, Món, Topping, Giá vùng)
    C->>PWA: Tùy biến món: 2x Cà Phê Muối Size L, 50% Đường, 70% Đá
    C->>PWA: Nhập SĐT "0901234567" & Chọn [Thanh toán VietQR Trả Trước]

    %% Bước 2: Tạo Đơn Hàng, Khóa Bàn & Soft Inventory Reservation
    PWA->>NGINX: POST /api/v1/orders/dine-in (TableId: "T04", Items, Phone, PaymentMethod="VIETQR")
    NGINX->>API: Forward kèm Header Idempotency-Key
    
    activate API
    API->>REDIS: RedLock.AcquireAsync("lock:table:T04", expire=5s)
    REDIS-->>API: Lock Acquired (Thành công)
    
    %% Kiểm tra trạng thái bàn và tồn kho BOM khả dụng
    API->>DB: SELECT status, is_active FROM tables WHERE id='T04'
    DB-->>API: TableRecord { status: "Available", is_active: true }
    
    API->>DB: SELECT r.ingredient_id, r.quantity FROM product_recipes r WHERE r.product_id='prod-cf-muoi' AND r.size_id='size-L'
    DB-->>API: RecipeData { Coffee: 40g, Milk: 60ml, SaltCream: 30ml } (x2 Ly = 80g Coffee, 120ml Milk, 60ml SaltCream)
    
    API->>DB: SELECT s.ingredient_id, s.current_quantity FROM inventory_stocks s WHERE s.branch_id='B01' AND s.ingredient_id IN ('ing-coffee', 'ing-milk', 'ing-salt')
    DB-->>API: CurrentStockData { Coffee: 5000g, Milk: 10000ml, SaltCream: 2000ml }
    
    API->>REDIS: HGETALL inventory:reserved:B01
    REDIS-->>API: ReservedData { Coffee: 200g, Milk: 500ml, SaltCream: 100ml }
    
    API->>API: Kiểm tra: available_stock = current_quantity - reserved_stock >= required_qty (Đủ tồn kho khả dụng)
    
    %% Thực hiện Giữ Tồn Kho Tạm Thời (Soft Reservation) trên Redis (TTL 600s)
    API->>REDIS: HINCRBY inventory:reserved:B01 ing-coffee 80
    API->>REDIS: HINCRBY inventory:reserved:B01 ing-milk 120
    API->>REDIS: HINCRBY inventory:reserved:B01 ing-salt 60
    API->>REDIS: EXPIRE inventory:reserved:B01 600
    
    API->>DB: BEGIN TRANSACTION
    API->>DB: INSERT INTO orders (order_code='ORD-B01-9942', branch_id='B01', table_id='T04', order_type='DINE_IN', status='PendingPayment', total_amount=90000, expires_at=NOW()+INTERVAL '10 min')
    API->>DB: INSERT INTO order_items (order_id, product_id, size_id, quantity=2, unit_price=45000, total_price=90000, sugar_level='50%', ice_level='70%', status='PendingPayment')
    API->>DB: INSERT INTO payments (order_id, payment_method='VIETQR', amount=90000, status='Pending', transfer_content='ORD_B01_9942')
    API->>DB: UPDATE tables SET status='Occupied_PendingPayment', updated_at=NOW() WHERE id='T04'
    API->>DB: COMMIT TRANSACTION
    
    API->>REDIS: SET table:T04:active_order "ord-9942" EX 600
    API->>REDIS: RedLock.ReleaseAsync("lock:table:T04")
    
    %% Bước 3: Gọi PayOS Gateway sinh VietQR
    API->>PAY: POST /v2/payment-requests (Amount=90000, Description="ORD_B01_9942", CancelUrl=..., ReturnUrl=...)
    PAY-->>API: Trả về PaymentLinkResponse (PaymentLinkId="plink_8841", QrCodeDataUrl="vietqr_payload_string", CheckoutUrl=...)
    
    API-->>PWA: HTTP 201 Created (OrderId="ord-9942", QrCodeUrl, TotalAmount=90000, ExpiresAt="10:00")
    deactivate API

    %% Bước 4: Hiển thị VietQR cho khách
    PWA-->>C: Hiển thị mã VietQR động + Bộ đếm ngược 10:00 + DeepLink App Ngân hàng
    Note over KDS: ⚠️ Màn hình KDS Bếp CHƯA hiển thị đơn này (Chặn đơn chưa thanh toán)

    %% Bước 5: Chuyển khoản & Webhook Xử lý (2 Nhánh)
    alt Nhánh A1: Khách Chuyển Khoản Thành Công Qua PayOS
        C->>PAY: Mở App Ngân Hàng (NAPAS 24/7) -> Quét VietQR -> Chuyển 90.000đ
        PAY->>NGINX: POST /api/v1/webhooks/payos (Header: x-payos-signature: "d7a8e5b...")
        NGINX->>API: Forward Webhook Payload
        
        activate API
        API->>API: Xác minh chữ ký HMAC-SHA256 với PayOS_Checksum_Key
        API->>REDIS: SETNX lock:webhook:payos:ORD_B01_9942 "1" EX 60 (Chống duplicate webhook)
        
        API->>DB: BEGIN TRANSACTION
        API->>DB: UPDATE payments SET status='Success', confirmed_at=NOW() WHERE transfer_content='ORD_B01_9942'
        API->>DB: INSERT INTO transactions (payment_id, gateway_transaction_id='FT2623598124', amount=90000, is_verified=true, raw_webhook_payload=...)
        API->>DB: UPDATE orders SET status='Confirmed', paid_at=NOW() WHERE id='ord-9942'
        API->>DB: UPDATE tables SET status='Occupied_Paid' WHERE id='T04'
        
        %% Khấu trừ Tồn kho Vật lý Vĩnh viễn (Physical Stock Deduction)
        API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 80, updated_at=NOW() WHERE branch_id='B01' AND ingredient_id='ing-coffee'
        API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 120, updated_at=NOW() WHERE branch_id='B01' AND ingredient_id='ing-milk'
        API->>DB: UPDATE inventory_stocks SET current_quantity = current_quantity - 60, updated_at=NOW() WHERE branch_id='B01' AND ingredient_id='ing-salt'
        
        API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-80, notes='Deducted for ord-9942')
        API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-120, notes='Deducted for ord-9942')
        API->>DB: INSERT INTO inventory_logs (branch_id, ingredient_id, order_id, change_type='BOM_AUTO_DEDUCT', quantity_changed=-60, notes='Deducted for ord-9942')
        API->>DB: COMMIT TRANSACTION
        
        %% Giải phóng Giữ Tồn Kho Tạm Thời (Release Soft Reservation) trên Redis
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-coffee -80
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-milk -120
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-salt -60
        
        %% Bước 6: Realtime Broadcast
        API->>HUB: PaymentHub.Clients.Group("order_ord-9942").SendAsync("PaymentReceived", { orderId: "ord-9942", status: "Paid" })
        API->>HUB: KitchenHub.Clients.Group("branch_B01_kitchen").SendAsync("NewKitchenOrder", OrderTicketDto)
        API-->>PAY: HTTP 200 OK (Webhook Processed Successfully)
        deactivate API
        
        par Đồng bộ Giao diện Khách & KDS
            HUB-->>PWA: Event `PaymentReceived` -> PWA chuyển sang màn hình "Đã Thanh Toán! Bếp đang nhận đơn ☕"
            HUB-->>KDS: Event `NewKitchenOrder` -> KDS phát chuông 🔔 Ting-Ting & Thẻ đơn trượt vào cột "Chờ Pha Chế"
        end
    else Nhánh A2: Hết Hạn 10 Phút Quét QR Hoặc Khách Hủy Đơn (Compensation Rollback)
        API->>DB: BEGIN TRANSACTION
        API->>DB: UPDATE orders SET status='Cancelled', expires_at=NOW() WHERE id='ord-9942'
        API->>DB: UPDATE payments SET status='Cancelled' WHERE order_id='ord-9942'
        API->>DB: UPDATE tables SET status='Available' WHERE id='T04'
        API->>DB: COMMIT TRANSACTION
        
        %% Hoàn lại Số lượng Giữ Tồn Kho Tạm Thời trong Redis
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-coffee -80
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-milk -120
        API->>REDIS: HINCRBY inventory:reserved:B01 ing-salt -60
        API->>REDIS: DEL table:T04:active_order
        
        API->>HUB: PaymentHub.Clients.Group("order_ord-9942").SendAsync("OrderExpired", { orderId: "ord-9942" })
        HUB-->>PWA: PWA thông báo: "Đơn hàng đã hết hạn thanh toán. Vui lòng tạo đơn mới!"
    end

    %% Bước 7: Pha chế & Phục vụ (Dành cho đơn đã Paid)
    KDS->>API: PATCH /api/v1/kds/orders/ord-9942/status { status: "Preparing" }
    API->>DB: UPDATE orders SET status='Preparing' WHERE id='ord-9942'
    API->>HUB: OrderHub.Clients.Group("order_ord-9942").SendAsync("OrderStatusUpdated", "Preparing")
    HUB-->>PWA: PWA cập nhật thanh tiến trình: "Quán đang pha chế đồ uống của bạn..."

    KDS->>API: PATCH /api/v1/kds/orders/ord-9942/status { status: "Ready" }
    API->>DB: UPDATE orders SET status='Ready' WHERE id='ord-9942'
    API->>HUB: OrderHub.Clients.Group("order_ord-9942").SendAsync("OrderStatusUpdated", "Ready")
    HUB-->>PWA: PWA rung chuông thông báo: "Đồ uống đã sẵn sàng! Nhân viên đang mang tới bàn."

    ST->>C: Bưng khay đồ uống ra Bàn 04
    ST->>API: PATCH /api/v1/orders/ord-9942/status { status: "Served" }
    API->>DB: UPDATE orders SET status='Completed', completed_at=NOW() WHERE id='ord-9942'
    API->>DB: UPDATE tables SET status='Available' WHERE id='T04'
    API->>HUB: OrderHub.Clients.Group("order_ord-9942").SendAsync("OrderStatusUpdated", "Completed")
    HUB-->>PWA: PWA hiển thị Modal Đánh Giá 1-5 Sao ⭐
```

---

# 2. SEQ-02: QUY TRÌNH GỌI MÓN TẠI BÀN (DINE-IN) — NHÁNH B: TRẢ SAU (TIỀN MẶT / QUÉT QR BILL)

### 📌 Mô tả Nghiệp vụ (Business Context)
Khách hàng tại bàn lựa chọn hình thức **"Thanh toán Tiền mặt (Trả sau khi nhận món)"**. 
- **Quy tắc cốt lõi:** Đơn hàng được xác nhận và chuyển thẳng xuống KDS Bếp ngay lập tức (`status='Confirmed'`) để quầy bar pha chế không có độ trễ. 
- Khi Barista hoàn thành pha chế (`status='Ready'`), hệ thống tự động gửi lệnh in **Hóa đơn tạm tính có in sẵn Mã VietQR Động** trên máy in nhiệt quầy bar.
- Nhân viên phục vụ mang đồ uống cùng Hóa đơn VietQR ra bàn. Khách hàng có 2 lựa chọn thanh toán linh hoạt: **(1) Trả tiền mặt cho nhân viên thu ngân**, hoặc **(2) Dùng Mobile Banking quét mã VietQR in trên hóa đơn**.

```mermaid
sequenceDiagram
    autonumber
    actor C as 👤 Khách Hàng (Tại bàn)
    participant PWA as 📱 Next.js PWA (Customer)
    participant NGINX as 🛡️ NGINX Reverse Proxy
    participant API as ⚙️ .NET 8 API (OrderController)
    participant DB as 🐘 PostgreSQL 16 (EF Core)
    participant HUB as 📡 SignalR (Kitchen & Order Hub)
    actor KDS as 🧋 Barista (Web KDS Bếp)
    participant PRN as 🖨️ Máy In Nhiệt Bar (ESC/POS)
    actor ST as 🧑‍💼 Phục Vụ / Thu Ngân
    participant POS as 💻 Web Staff POS Portal
    participant PAY as 🏦 Cổng PayOS Gateway

    %% Bước 1: Tạo Đơn Trả Sau
    C->>PWA: Chọn món & Bấm chọn [Thanh toán Tiền Mặt / Trả Sau Tại Bàn]
    PWA->>NGINX: POST /api/v1/orders/dine-in (TableId: "T04", Items: [...], PaymentMethod="CASH")
    NGINX->>API: Forward Request

    activate API
    API->>DB: BEGIN TRANSACTION
    API->>DB: INSERT INTO orders (order_code='ORD-B01-9943', branch_id='B01', table_id='T04', order_type='DINE_IN', status='Confirmed', payment_method='CASH', total_amount=70000)
    API->>DB: INSERT INTO order_items (order_id, product_id, size_id, quantity=2, unit_price=35000, total_price=70000, status='Confirmed')
    API->>DB: UPDATE tables SET status='Occupied_PendingPayment' WHERE id='T04'
    API->>DB: COMMIT TRANSACTION
    
    API->>HUB: KitchenHub.Clients.Group("branch_B01_kitchen").SendAsync("NewKitchenOrder", OrderTicketDto)
    API-->>PWA: HTTP 201 Created (OrderId="ord-9943", Status="Confirmed", TotalAmount=70000)
    deactivate API

    par Cập nhật Giao diện Đặt món & KDS
        PWA-->>C: Thông báo: "Đơn hàng đã gửi bếp! Quý khách sẽ thanh toán khi nhận đồ uống."
        HUB-->>KDS: KDS phát chuông 🔔 & Hiển thị thẻ đơn Bàn 04 ở cột "Chờ Pha Chế"
    end

    %% Bước 2: Pha chế & In Bill kèm VietQR
    KDS->>API: PATCH /api/v1/kds/orders/ord-9943/status { status: "Preparing" }
    API->>DB: UPDATE orders SET status='Preparing' WHERE id='ord-9943'
    
    KDS->>API: PATCH /api/v1/kds/orders/ord-9943/status { status: "Ready" }
    activate API
    API->>DB: UPDATE orders SET status='Ready' WHERE id='ord-9943'
    API->>PAY: GenerateVietQrPayload(Amount=70000, Description="ORD_B01_9943")
    PAY-->>API: Trả về Chuỗi VietQR Payload Base64
    API->>PRN: SendRawEscPosPrintJob (Chi tiết đơn + Tổng tiền 70k + Mã VietQR In Sẵn)
    deactivate API

    PRN-->>KDS: In ra Phiếu Hóa Đơn Tạm Tính có in sẵn mã VietQR
    KDS->>ST: Bàn giao khay đồ uống kèm tờ Hóa Đơn VietQR
    ST->>C: Bưng nước ra Bàn 04 + Đặt tờ Hóa Đơn lên bàn
    ST->>API: PATCH /api/v1/orders/ord-9943/status { status: "Served" }
    API->>DB: UPDATE orders SET status='Served' WHERE id='ord-9943'

    %% Bước 3: Khách hàng Thanh toán (2 Nhánh)
    alt Nhánh B1: Khách Trả Tiền Mặt Cho Phục Vụ
        C->>ST: Đưa 100.000đ tiền mặt
        ST->>POS: Mở đơn Bàn 04 -> Nhập Tiền Khách Đưa: 100.000đ -> Bấm [Xác nhận thu tiền mặt]
        POS->>API: POST /api/v1/payments/cash-confirm { orderId: "ord-9943", cashGiven: 100000 }
        activate API
        API->>DB: BEGIN TRANSACTION
        API->>DB: INSERT INTO payments (order_id, payment_method='CASH', amount=70000, status='Success', confirmed_at=NOW())
        API->>DB: UPDATE orders SET status='Completed', paid_at=NOW(), completed_at=NOW() WHERE id='ord-9943'
        API->>DB: UPDATE tables SET status='Available' WHERE id='T04'
        API->>DB: UPDATE work_shifts SET cash_sales_system = cash_sales_system + 70000 WHERE id=current_shift_id AND status='Open'
        API->>DB: COMMIT TRANSACTION
        
        API->>HUB: OrderHub.Clients.Group("order_ord-9943").SendAsync("OrderPaid", { orderId: "ord-9943" })
        API-->>POS: HTTP 200 OK (ChangeAmount=30000, Status="Paid")
        deactivate API
        POS-->>ST: Mở két tiền -> Hiển thị tiền thối: 30.000đ
        ST->>C: Thối lại 30.000đ tiền mặt cho khách
    else Nhánh B2: Khách Quét Mã VietQR Trên Hóa Đơn
        C->>C: Mở App Ngân Hàng -> Quét mã VietQR in trên tờ hóa đơn -> Chuyển 70.000đ
        PAY->>API: POST /api/v1/webhooks/payos (HMAC-SHA256, ORD_B01_9943, 70000đ)
        activate API
        API->>API: Xác thực chữ ký HMAC-SHA256 & Idempotency Key
        API->>DB: BEGIN TRANSACTION
        API->>DB: INSERT INTO payments (order_id, payment_method='VIETQR', amount=70000, status='Success', confirmed_at=NOW(), transfer_content='ORD_B01_9943')
        API->>DB: INSERT INTO transactions (payment_id, gateway_transaction_id=..., amount=70000, is_verified=true)
        API->>DB: UPDATE orders SET status='Completed', paid_at=NOW(), completed_at=NOW() WHERE id='ord-9943'
        API->>DB: UPDATE tables SET status='Available' WHERE id='T04'
        API->>DB: COMMIT TRANSACTION
        
        API->>HUB: OrderHub.Clients.Group("order_ord-9943").SendAsync("OrderPaid", { orderId: "ord-9943" })
        API->>HUB: NotificationHub.Clients.Group("branch_B01_staff").SendAsync("TablePaidNotification", "Bàn 04 đã chuyển khoản thành công!")
        API-->>PAY: HTTP 200 OK
        deactivate API
        HUB-->>POS: Web POS quầy tự động chuyển trạng thái Bàn 04 sang [ĐÃ THANH TOÁN XANH LÁ]
    end

    HUB-->>PWA: PWA chuyển sang trạng thái "Đã thanh toán thành công!" & Mở Form Review
```
"""
