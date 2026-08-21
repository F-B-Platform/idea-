# 📡 QUY TRÌNH 3: THIẾT KẾ HỢP ĐỒNG API & SIGNALR CONTRACT

> **Mục tiêu:** Thống nhất "Hợp đồng giao tiếp" giữa Backend và Frontend trước khi viết code, đảm bảo ghép nối KHÔNG BỊ LỆCH.

---

## 1. NHỮNG ĐIỂM BẮT BUỘC PHẢI LÀM RÕ TRONG BƯỚC NÀY

### 1.1 Chuẩn Định Dạng JSON Response Envelope
Tất cả API (dù thành công hay thất bại) đều phải trả về đúng cấu trúc chuẩn:

**Format Thành công (Single Object):**
```json
{
  "success": true,
  "data": { "id": "uuid", "name": "Bạc Xỉu", "price": 35000 },
  "message": "Lấy thông tin món thành công"
}
```

**Format Thành công (Danh sách có Phân trang):**
```json
{
  "success": true,
  "data": [ { ... }, { ... } ],
  "pagination": { "page": 1, "pageSize": 20, "totalItems": 45, "totalPages": 3 }
}
```

**Format Lỗi (Error Envelope):**
```json
{
  "success": false,
  "error": {
    "code": "PRODUCT_OUT_OF_STOCK",
    "message": "Món Latte hiện đã hết hàng tại chi nhánh này"
  }
}
```

---

### 1.2 Phân Nhóm 45+ RESTful Endpoints

```
/api/v1/auth/
  ├── POST /login
  ├── POST /register
  └── POST /refresh-token

/api/v1/products/
  ├── GET  /                 (Public Menu)
  ├── GET  /{id}
  ├── POST /                 (Admin create)
  ├── PUT  /{id}
  └── PATCH /{id}/toggle    (Admin/Manager disable)

/api/v1/orders/              (CORE)
  ├── POST  /                (Khách đặt đơn)
  ├── GET   /{id}            (Khách xem tiến trình)
  ├── GET   /                (KDS / Staff xem danh sách đơn)
  ├── PATCH /{id}/status     (KDS chuyển trạng thái đơn)
  ├── PATCH /{id}/items/{itemId}/complete
  └── POST  /{id}/request-bill

/api/v1/payments/
  ├── POST  /                (Sinh mã VietQR động)
  └── PATCH /{id}/confirm    (NV xác nhận đã nhận tiền)

/api/v1/reports/
  ├── GET   /revenue         (Doanh thu theo ngày/giờ)
  └── GET   /top-products
```

---

### 1.3 Thống Nhất Các Sự Kiện Real-time (SignalR Contract)

| Hub | Tên Event | Nguồn → Đích | Payload Data |
|---|---|---|---|
| `OrderHub` | `NewOrder` | Server → KDS | `{ orderId, orderNumber, tableNumber, items: [...] }` |
| `OrderHub` | `OrderStatusChanged` | Server → Customer | `{ orderId, status: "Preparing" | "Ready" }` |
| `OrderHub` | `ItemCompleted` | Server → Customer | `{ orderId, itemId, itemName }` |
| `KitchenHub` | `BillRequested` | Server → Staff App | `{ orderId, tableNumber, amount }` |
| `KitchenHub` | `CallStaff` | Server → Staff App | `{ tableNumber, message: "Cần lấy thêm đá" }` |

---

## 2. QUY TRÌNH THỰC THI THEO VAI TRÒ

```
┌────────────────────────────────────────────────────────────────────────┐
│                      QUY TRÌNH LẬP API SPEC                            │
│                                                                        │
│  [BE1] Soạn thảo file OpenAPI / Swagger Specification                  │
│     │                                                                  │
│     ▼                                                                  │
│  [FE1 & FE2] Review danh sách Request/Response JSON                     │
│     │                                                                  │
│     ▼                                                                  │
│  [BE1 & FE1] Thống nhất Event Name & Data Payload cho SignalR Hubs     │
│     │                                                                  │
│     ▼                                                                  │
│  [Cả Team] Chốt file `api_specification.md` làm HỢP ĐỒNG DÙNG CHUNG    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📥 INPUT & 📤 OUTPUT CỦA QUY TRÌNH 3

* **Input:** Business Rules & Database ERD từ Quy trình 1 & 2.
* **Output:** Document `api_specification.md` đầy đủ 45+ endpoints & SignalR events contract.
* **Bước tiếp theo:** Chuyển sang **Quy trình 4: Thiết kế Giao diện UI/UX (Wireframe)**.
