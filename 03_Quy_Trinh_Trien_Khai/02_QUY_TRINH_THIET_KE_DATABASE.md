# 🗄️ QUY TRÌNH 2: THIẾT KẾ DATABASE & CẤU TRÚC DỮ LIỆU

> **Mục tiêu:** Xây dựng sơ đồ Database (ERD) chuẩn hóa 28 bảng, tối ưu Indexing và thiết lập EF Core Code-First Migration.

---

## 1. NHỮNG ĐIỂM BẮT BUỘC PHẢI LÀM RÕ TRONG BƯỚC NÀY

### 1.1 Cấu Trúc 28 Bảng Theo 7 Nhóm Logic
1. **Core Group (7 bảng):** `Branch`, `Table`, `QrCode`, `Category`, `Product`, `ProductVariant`, `Topping`.
2. **Order Group (4 bảng):** `Order`, `OrderItem`, `OrderItemTopping`, `Payment`.
3. **User & Auth Group (3 bảng):** `User`, `BranchUser`, `Customer`.
4. **Inventory Group (4 bảng):** `Ingredient`, `ProductIngredient`, `InventoryStock`, `StockTransaction`.
5. **HRM & Finance Group (3 bảng):** `Attendance`, `CashShift`, `Shift`.
6. **CRM & Loyalty Group (5 bảng):** `LoyaltyTransaction`, `Voucher`, `VoucherUsage`, `Review`, `ReviewImage`.
7. **System Group (2 bảng):** `Notification`, `AuditLog`.

---

### 1.2 Ràng Buộc & Quy Chuẩn Thiết Kế Dữ Liệu

| Quy chuẩn | Chi tiết quy định | Lý do |
|---|---|---|
| **Khóa chính (PK)** | Sử dụng `UUID` (`Guid.NewGuid()`) cho toàn bộ bảng. | Dễ scale, không lộ số lượng record, hỗ trợ Offline Sync. |
| **Tiền tệ (Money)** | Kiểu `decimal(12,0)` (không dùng float/double, không lấy số thập phân cho VNĐ). | Tránh sai số làm tròn khi tính tổng tiền đơn hàng. |
| **Khóa ngoại (FK)** | Khai báo quan hệ Fluent API rõ ràng (`OnDelete(DeleteBehavior.Restrict)`). | Tránh xoá dây chuyền (Cascade delete) làm mất dữ liệu lịch sử đơn. |
| **Thời gian (Timestamp)** | Dùng `DateTime.UtcNow` cho `CreatedAt`, `UpdatedAt`, `CompletedAt`. | Đồng bộ múi giờ giữa Backend và Database PostgreSQL. |

---

### 1.3 Chiến Lược Đánh Index (Indexing Strategy)

```sql
-- 1. Query danh sách món theo danh mục & trạng thái (QR Menu)
CREATE INDEX idx_products_category_available ON "Products" ("CategoryId", "IsAvailable");

-- 2. Query đơn hàng theo chi nhánh & ngày (KDS & Admin Dashboard)
CREATE INDEX idx_orders_branch_created ON "Orders" ("BranchId", "CreatedAt" DESC);

-- 3. Query đơn hàng theo trạng thái (KDS Kanban)
CREATE INDEX idx_orders_status ON "Orders" ("Status");

-- 4. Nhận diện khách hàng nhanh qua SĐT (CRM)
CREATE UNIQUE INDEX idx_customers_phone ON "Customers" ("Phone");

-- 5. Query tồn kho chi nhánh
CREATE UNIQUE INDEX idx_inventory_branch_ingredient ON "InventoryStocks" ("BranchId", "IngredientId");
```

---

## 2. QUY TRÌNH THỰC THI THEO VAI TRÒ

```
┌────────────────────────────────────────────────────────────────────────┐
│                        QUY TRÌNH THIẾT KẾ DB                           │
│                                                                        │
│  [BE2] Viết Entity Classes (Domain Layer)                             │
│     │                                                                  │
│     ▼                                                                  │
│  [BE2] Cấu hình Fluent API Mapping & DbContext (Infrastructure Layer)  │
│     │                                                                  │
│     ▼                                                                  │
│  [BE1] Review ERD, Foreign Keys & Precision                            │
│     │                                                                  │
│     ▼                                                                  │
│  [BE2] Chạy Command: `dotnet ef migrations add InitialCreate`         │
│     │                                                                  │
│     ▼                                                                  │
│  [BE2] Viết Script Seed Data Mẫu (3 chi nhánh, 20 bàn, 30 món)         │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📥 INPUT & 📤 OUTPUT CỦA QUY TRÌNH 2

* **Input:** Scope MVP Tier 1 & Business Rules từ Quy trình 1.
* **Output:**
  * 28 C# Entity classes trong `SmartFB.Domain`.
  * `AppDbContext.cs` & 28 Configuration classes trong `SmartFB.Infrastructure`.
  * Migration file đầu tiên & Seed Data script tự động.
* **Bước tiếp theo:** Chuyển sang **Quy trình 3: Thiết kế Hợp đồng API & SignalR Contract**.
