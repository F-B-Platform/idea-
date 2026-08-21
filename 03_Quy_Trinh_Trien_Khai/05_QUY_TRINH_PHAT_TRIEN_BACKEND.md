# ⚙️ QUY TRÌNH 5: PHÁT TRIỂN BACKEND (.NET 8 CLEAN ARCHITECTURE)

> **Mục tiêu:** Xây dựng hệ thống REST API chuẩn Clean Architecture, xử lý Transaction an toàn, hiệu năng cao và tích hợp SignalR Real-time.

---

## 1. NHỮNG ĐIỂM BẮT BUỘC PHẢI LÀM RÕ TRONG BƯỚC NÀY

### 1.1 Luồng Dữ Liệu Qua 4 Tầng Clean Architecture

```
[ HTTP Request ]
       │
       ▼
┌──────────────┐
│  SmartFB.API │ ──► Controllers (nhận DTO, validate), SignalR Hubs, Middleware
└──────────────┘
       │
       ▼
┌──────────────────────┐
│ SmartFB.Application  │ ──► Services (Business logic), DTOs, Mapping (AutoMapper)
└──────────────────────┘
       │
       ▼
┌──────────────┐
│ SmartFB.Domain│ ──► Entities, Enums, Domain Rules, Repository Interfaces
└──────────────┘
       ▲
       │
┌─────────────────────────┐
│ SmartFB.Infrastructure  │ ──► AppDbContext (EF Core), Repository Impl, External Services
└─────────────────────────┘
```

---

### 1.2 Thứ Tự Code Từng Module Backend (Strict Order)

```
Bước 5.1: Auth & User Module (JWT + RBAC Middleware)
   ↓
Bước 5.2: CRUD Menu & Branch (Product, Variant, Category, Table)
   ↓
Bước 5.3: Core Order Engine (POST /orders với EF Transaction)
   ↓
Bước 5.4: SignalR Real-time Hubs (Broadcast NewOrder đến KDS)
   ↓
Bước 5.5: Payment & VietQR Module (Generate QR + Confirm Payment)
   ↓
Bước 5.6: Inventory & HRM Module (Mở/Kết ca, Xuất/Kiểm kho)
   ↓
Bước 5.7: Report & Analytics Module (Doanh thu, Top món)
```

---

### 1.3 Quy Tắc Xử Lý Error & Validation

1. **Input Validation:** Sử dụng `FluentValidation` validate DTO trước khi vào Controller.
2. **Global Exception Handling:** Viết `ExceptionHandlingMiddleware` bắt ngoại lệ tập trung, trả về đúng Error Envelope JSON:
```csharp
public async Task InvokeAsync(HttpContext context)
{
    try { await _next(context); }
    catch (DomainException ex) { await HandleCustomExceptionAsync(context, ex, HttpStatusCode.BadRequest); }
    catch (Exception ex) { await HandleCustomExceptionAsync(context, ex, HttpStatusCode.InternalServerError); }
}
```

---

## 2. PHÂN CÔNG THỰC THI (BE1 vs BE2)

| Module | BE1 (Backend Lead) | BE2 (Backend Dev) |
|---|---|---|
| **Solution & Infra** | Setup Solution, JWT Auth, Middleware | AppDbContext, EF Configurations, Seed Data |
| **Menu & Core** | Order Service, SignalR Hubs | Product Service, Category/Table CRUD |
| **Operations** | Payment VietQR, CRM Loyalty | Inventory Service, CashShift Mở/Kết ca |
| **Analytics & AI** | AI Chatbot Service (Gemini API) | Report Queries, Export Excel/PDF |

---

## 📥 INPUT & 📤 OUTPUT CỦA QUY TRÌNH 5

* **Input:** Hợp đồng API Spec, SignalR Contract & Database Migration từ Quy trình 2 & 3.
* **Output:** Backend API chạy hoàn chỉnh trên `http://localhost:5000`, có tài liệu Swagger UI tự động.
* **Bước tiếp theo:** Chuyển sang **Quy trình 6: Phát triển Frontend (Next.js 14)**.
