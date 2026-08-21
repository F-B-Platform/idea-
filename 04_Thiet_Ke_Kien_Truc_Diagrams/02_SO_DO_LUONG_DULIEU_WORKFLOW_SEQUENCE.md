# 🔄 SƠ ĐỒ LUỒNG DỮ LIỆU & SEQUENCE DIAGRAMS

> **Dự án:** Smart F&B Operating System  
> **Mô tả:** Chi tiết các luồng tương tác giữa Khách hàng, Hệ thống, Bếp (KDS), Nhân viên và AI Engine qua Sequence Diagrams.

---

## 1. SEQUENCE DIAGRAM 1: KHÁCH ĐẶT MÓN QR & SIGNALR BROADCAST TỚI KDS BẾP (WF-01 & WF-02)

```mermaid
sequenceDiagram
    autonumber
    actor Customer as 👤 Khách hàng (PWA)
    participant NextJS as 📱 Next.js Client
    participant OrderAPI as ⚙️ .NET Order Controller
    participant DB as 🐘 PostgreSQL DB
    participant Hub as ⚡ SignalR OrderHub
    actor Barista as 🧋 Barista (KDS App)

    Customer->>NextJS: Scan QR bàn 5 → Mở Menu PWA
    NextJS->>OrderAPI: GET /api/v1/products?branchId=xyz
    OrderAPI->>DB: Query Menu còn hàng (IsAvailable=true)
    DB-->>OrderAPI: Tra dữ liệu 30 món
    OrderAPI-->>NextJS: Response 200 (JSON Menu)
    NextJS-->>Customer: Hiển thị giao diện Menu

    Customer->>NextJS: Chọn Bạc Xỉu Size M (50% đường, 100% đá, thêm Trân châu)
    Customer->>NextJS: Nhấn nút "Gửi Đơn Hàng"
    NextJS->>OrderAPI: POST /api/v1/orders (OrderPayload JSON)

    activate OrderAPI
    OrderAPI->>DB: Check tồn kho món & bàn hợp lệ
    OrderAPI->>DB: Begin DB Transaction
    OrderAPI->>DB: INSERT INTO "Orders" & "OrderItems" (Status='Confirmed')
    OrderAPI->>DB: Commit Transaction
    DB-->>OrderAPI: Trả về OrderID & OrderNumber (#001)

    OrderAPI->>Hub: Broadcast Event `NewOrder` (Payload Order #001)
    deactivate OrderAPI

    par SignalR Event Delivery
        Hub-->>Barista: SignalR Event `NewOrder` → KDS phát chuông 🔔 & hiện Card đơn #001
        Hub-->>NextJS: Response Order Success → Chuyển sang màn hình Tracking
    end

    NextJS-->>Customer: Hiển thị màn hình Thanh tiến trình (Trạng thái: "Đã nhận đơn")
```

---

## 2. SEQUENCE DIAGRAM 2: BARISTA PHA CHẾ & HOÀN THÀNH MÓN (KDS ➔ KHÁCH)

```mermaid
sequenceDiagram
    autonumber
    actor Barista as 🧋 Barista (KDS)
    participant KDSApp as 📺 KDS App
    participant ItemAPI as ⚙️ .NET Order Controller
    participant DB as 🐘 PostgreSQL DB
    participant Hub as ⚡ SignalR OrderHub
    actor Customer as 👤 Khách hàng (PWA)

    Barista->>KDSApp: Xem công thức Bạc Xỉu trên Card đơn #001
    Barista->>KDSApp: Nhấn nút "Bắt đầu Pha chế"
    KDSApp->>ItemAPI: PATCH /api/v1/orders/001/status (Status='Preparing')
    ItemAPI->>DB: UPDATE "Orders" SET Status='Preparing'
    ItemAPI->>Hub: Broadcast Event `OrderStatusChanged` ('Preparing')
    Hub-->>Customer: SignalR Event → Tiến trình nhảy sang "Đang pha chế ☕"

    Note over Barista: Barista pha chế món Bạc Xỉu theo định lượng...

    Barista->>KDSApp: Bấm nút "Hoàn Thành Món"
    KDSApp->>ItemAPI: PATCH /api/v1/orders/001/items/item123/complete
    ItemAPI->>DB: UPDATE "OrderItems" SET Status='Completed'
    ItemAPI->>DB: CHECK if all items completed → SET Order Status='Ready'
    ItemAPI->>Hub: Broadcast Event `OrderStatusChanged` ('Ready')

    par Multi-client Notification
        Hub-->>Customer: SignalR Event → Tiến trình nhảy "Món đã sẵn sàng! 🥳"
        Hub-->>Barista: KDS Card đổi sang màu Xanh Lá (Hoàn tất)
    end
```

---

## 3. SEQUENCE DIAGRAM 3: KHÁCH YÊU CẦU BILL & THÀNH TOÁN VIETQR (WF-01)

```mermaid
sequenceDiagram
    autonumber
    actor Customer as 👤 Khách hàng (PWA)
    participant CustomerPWA as 📱 Customer PWA
    participant PayAPI as ⚙️ .NET Payment Controller
    participant VietQR as 🏦 VietQR / NAPAS API
    participant Hub as ⚡ SignalR Hub
    actor Staff as 🧋 Phục vụ (Staff App)
    participant DB as 🐘 PostgreSQL DB

    Customer->>CustomerPWA: Nhấn nút "Yêu Cầu Thanh Toán VietQR"
    CustomerPWA->>PayAPI: POST /api/v1/orders/001/request-bill

    PayAPI->>VietQR: Generate QR Code (Số tiền: 95.000 VNĐ, Nội dung: "DH001")
    VietQR-->>PayAPI: Trả về URL ảnh QR Code VietQR
    PayAPI->>DB: INSERT INTO "Payments" (Status='Pending', VietQRUrl=...)

    PayAPI->>Hub: Broadcast Event `BillRequested` (Bàn 5, Số tiền 95k)
    Hub-->>Staff: Staff App & KDS rung chuông "Bàn 5 yêu cầu bill 💳"

    PayAPI-->>CustomerPWA: Response VietQR Image URL
    CustomerPWA-->>Customer: Hiển thị mã VietQR trên điện thoại khách

    Note over Customer, Staff: Khách dùng App Ngân hàng quét QR chuyển khoản...<br/>Nhân viên phục vụ đến bàn/quầy kiểm tra app ngân hàng.

    Staff->>PayAPI: PATCH /api/v1/payments/pay123/confirm
    PayAPI->>DB: UPDATE "Payments" SET Status='Confirmed'
    PayAPI->>DB: UPDATE "Orders" SET Status='Paid'
    PayAPI->>Hub: Broadcast Event `OrderStatusChanged` ('Paid')
    Hub-->>CustomerPWA: Thông báo "Thanh toán thành công! Cảm ơn quý khách ❤️"
```

---

## 4. SEQUENCE DIAGRAM 4: MỞ CA / KẾT CA KÉT TIỀN & ĐỐI SOÁT (WF-08)

```mermaid
sequenceDiagram
    autonumber
    actor Manager as 🏪 Quản lý Chi nhánh
    participant App as 💻 Manager App
    participant ShiftAPI as ⚙️ .NET Shift Controller
    participant DB as 🐘 PostgreSQL DB

    Note over Manager: ĐẦU CA LÀM VIỆC (MỞ CA)
    Manager->>App: Nhập số tiền mặt đầu két (VD: 2.000.000 VNĐ)
    App->>ShiftAPI: POST /api/v1/cash-shifts/open (OpeningCash=2000000)
    ShiftAPI->>DB: INSERT INTO "CashShifts" (Status='Open', OpenedAt=NOW())
    ShiftAPI-->>App: Response "Mở ca thành công"

    Note over Manager: TRONG CA: Hệ thống bán hàng liên tục...

    Note over Manager: CUỐI CA LÀM VIỆC (KẾT CA)
    Manager->>App: Đếm tiền mặt thực tế trong két (VD: 5.450.000 VNĐ) & Bấm Kết Ca
    App->>ShiftAPI: POST /api/v1/cash-shifts/shift123/close (ClosingCash=5450000)

    activate ShiftAPI
    ShiftAPI->>DB: Query Tổng Doanh thu Tiền mặt trong ca từ "Payments"
    DB-->>ShiftAPI: CashRevenue = 3.500.000 VNĐ
    
    ShiftAPI->>ShiftAPI: Tính SystemCash = OpeningCash (2M) + CashRevenue (3.5M) = 5.500.000 VNĐ
    ShiftAPI->>ShiftAPI: Tính Difference = ClosingCash (5.45M) - SystemCash (5.5M) = -50.000 VNĐ (Thiếu 50k)

    ShiftAPI->>DB: UPDATE "CashShifts" SET Status='Closed', ClosedAt=NOW(), Difference=-50000
    deactivate ShiftAPI

    ShiftAPI-->>App: Response Báo cáo đối soát (Cảnh báo: Lệch két -50.000 VNĐ)
```

---

## 5. SEQUENCE DIAGRAM 5: AI CHATBOT GỢI Ý MÓN ĂN (GEMINI INTEGRATION)

```mermaid
sequenceDiagram
    autonumber
    actor Customer as 👤 Khách hàng
    participant PWA as 📱 QR Order PWA
    participant AiAPI as ⚙️ .NET AI Controller
    participant DB as 🐘 PostgreSQL DB
    participant Gemini as 🤖 Google Gemini API

    Customer->>PWA: Nhập chat: "Tôi bị dị ứng sữa, muốn uống món gì đắng nhẹ?"
    PWA->>AiAPI: POST /api/v1/ai/chat (Message JSON)

    activate AiAPI
    AiAPI->>DB: Query Danh sách món đang còn bán của Chi nhánh
    DB-->>AiAPI: Trả về Danh sách món (Name, Allergens, Description)

    AiAPI->>AiAPI: Build Prompt Context:<br/>"Menu hiện tại: [Americano (không sữa), Espresso, Bạc xỉu (sữa)]...<br/>Khách hỏi: Dị ứng sữa, thích đắng nhẹ. Hãy gợi ý món phù hợp."

    AiAPI->>Gemini: Call Gemini API (Prompt + Context)
    Gemini-->>AiAPI: Response JSON Text:<br/>"Gợi ý Americano đá (không chứa sữa, vị đắng thanh nhẹ)..."

    deactivate AiAPI
    AiAPI-->>PWA: Response JSON (Reply Text + Product IDs)
    PWA-->>Customer: Hiển thị câu trả lời AI + Nút "Thêm Americano vào giỏ"
```
