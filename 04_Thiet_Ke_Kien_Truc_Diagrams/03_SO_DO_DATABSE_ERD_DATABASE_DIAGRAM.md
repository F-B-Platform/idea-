# 🗄️ SƠ ĐỒ DATABASE ERD CHI TIẾT (28 BẢNG)

> **Database:** PostgreSQL 16  
> **ORM Framework:** Entity Framework Core 8 Code-First  
> **Mô tả:** Sơ đồ quan hệ thực thể (ERD) hoàn chỉnh 28 bảng dữ liệu chuẩn hóa của hệ thống Smart F&B OS.

---

## 1. SƠ ĐỒ QUAN HỆ THỰC THỂ (FULL MERMAID ERD DIAGRAM)

```mermaid
erDiagram
    %% ========== 1. CORE GROUP ==========
    Branch ||--o{ Table : "quản lý"
    Branch ||--o{ BranchUser : "gán nhân sự"
    Branch ||--o{ InventoryStock : "tồn kho"
    Branch ||--o{ CashShift : "quản lý ca"
    Branch ||--o{ Order : "nhận đơn"
    Branch ||--o{ BusinessHours : "giờ mở cửa"
    Branch ||--o{ QrCode : "phát hành QR"

    Table ||--o{ QrCode : "gắn mã"
    Table ||--o{ Order : "đặt tại bàn"

    Category ||--o{ Product : "chứa"
    Product ||--o{ ProductVariant : "có biến thể Size"
    Product ||--o{ ProductIngredient : "có công thức"
    Product ||--o{ OrderItem : "được đặt trong"
    Product ||--o{ ComboItem : "nằm trong combo"

    Ingredient ||--o{ ProductIngredient : "dùng làm công thức"
    Ingredient ||--o{ InventoryStock : "theo dõi tồn kho"

    Combo ||--o{ ComboItem : "chứa các món"

    %% ========== 2. ORDER GROUP ==========
    Order ||--o{ OrderItem : "chứa các món"
    Order ||--o| Payment : "thanh toán bằng"
    Order }o--o| Customer : "đặt bởi"
    Order }o--o| Voucher : "áp dụng"

    OrderItem ||--o{ OrderItemTopping : "thêm topping"
    OrderItem }o--o| ProductVariant : "chọn biến thể"

    Topping ||--o{ OrderItemTopping : "áp dụng vào món"

    %% ========== 3. USER & AUTH GROUP ==========
    User ||--o{ BranchUser : "thuộc chi nhánh"
    User ||--o{ Attendance : "chấm công"
    User ||--o{ CashShift : "mở/kết ca"
    User ||--o{ AuditLog : "thực hiện thao tác"

    %% ========== 4. CRM & LOYALTY GROUP ==========
    Customer ||--o{ Order : "thực hiện đơn"
    Customer ||--o{ LoyaltyTransaction : "tích/tiêu điểm"
    Customer ||--o{ Review : "đánh giá"
    Customer ||--o{ VoucherUsage : "sử dụng mã"

    Voucher ||--o{ VoucherUsage : "đã dùng"

    Review ||--o{ ReviewImage : "chứa ảnh"

    %% ========== 5. INVENTORY GROUP ==========
    InventoryStock ||--o{ StockTransaction : "lịch sử biến động"

    %% ========== ENTITY DETAILS ==========
    Branch {
        Guid Id PK
        String Name
        String Address
        String Phone
        Boolean IsActive
        DateTime CreatedAt
    }

    Table {
        Guid Id PK
        Guid BranchId FK
        String TableNumber
        String Zone
        Int Capacity
        String Status
        Boolean IsActive
    }

    QrCode {
        Guid Id PK
        Guid TableId FK
        Guid BranchId FK
        String Code UK
        String QrType
        Boolean IsActive
    }

    Category {
        Guid Id PK
        String Name
        String Icon
        Int DisplayOrder
        Boolean IsActive
    }

    Product {
        Guid Id PK
        Guid CategoryId FK
        String Name
        String Description
        String ImageUrl
        Decimal BasePrice
        String Allergens
        Int Calories
        Boolean IsAvailable
        Boolean IsBestSeller
        String RecipeInstructions
        Int DisplayOrder
    }

    ProductVariant {
        Guid Id PK
        Guid ProductId FK
        String Name
        Decimal AdditionalPrice
        Boolean IsDefault
    }

    Topping {
        Guid Id PK
        String Name
        Decimal Price
        Boolean IsAvailable
    }

    Order {
        Guid Id PK
        String OrderNumber UK
        Guid BranchId FK
        Guid TableId FK
        Guid CustomerId FK
        String OrderType
        String Status
        Decimal Subtotal
        Decimal DiscountAmount
        Decimal TotalAmount
        Guid VoucherId FK
        String Note
        Boolean IsOffline
        DateTime CreatedAt
        DateTime CompletedAt
    }

    OrderItem {
        Guid Id PK
        Guid OrderId FK
        Guid ProductId FK
        Guid ProductVariantId FK
        Int Quantity
        Decimal UnitPrice
        Decimal TotalPrice
        Int SugarLevel
        String IceLevel
        String SpecialNote
        String Status
    }

    OrderItemTopping {
        Guid Id PK
        Guid OrderItemId FK
        Guid ToppingId FK
        Decimal Price
    }

    Payment {
        Guid Id PK
        Guid OrderId FK UK
        String PaymentMethod
        Decimal Amount
        String Status
        String VietQrCode
        Guid ConfirmedBy FK
        DateTime ConfirmedAt
    }

    User {
        Guid Id PK
        String FullName
        String Email UK
        String Phone
        String PasswordHash
        String Role
        Boolean IsActive
    }

    Customer {
        Guid Id PK
        String Phone UK
        String Name
        Int TotalVisits
        Decimal TotalSpent
        Int LoyaltyPoints
        String LoyaltyTier
        DateTime LastVisitAt
    }

    Ingredient {
        Guid Id PK
        String Name
        String Unit
        Decimal MinStockLevel
    }

    InventoryStock {
        Guid Id PK
        Guid BranchId FK
        Guid IngredientId FK
        Decimal CurrentQuantity
        DateTime LastUpdated
    }

    StockTransaction {
        Guid Id PK
        Guid InventoryStockId FK
        String TransactionType
        Decimal Quantity
        String Reason
        Guid PerformedBy FK
    }

    CashShift {
        Guid Id PK
        Guid BranchId FK
        Guid OpenedBy FK
        Guid ClosedBy FK
        Decimal OpeningCash
        Decimal ClosingCash
        Decimal SystemCash
        Decimal CashDifference
        String Status
    }
```

---

## 2. MA TRẬN TỔNG HỢP 28 BẢNG DỮ LIỆU

| # | Tên Bảng | Tầng Logic | Chức năng chính |
|---|---|---|---|
| 1 | `Branches` | Core | Quản lý thông tin 3 chi nhánh chuỗi quán |
| 2 | `Tables` | Core | Quản lý danh sách bàn, khu vực và sức chứa |
| 3 | `QrCodes` | Core | Lưu mã QR động mã hóa cho từng bàn / takeaway |
| 4 | `Categories` | Core | Phân loại danh mục (Cà phê, Trà, Bánh, Dessert) |
| 5 | `Products` | Core | Thông tin món, giá gốc, ảnh, tag dị ứng, recipe JSON |
| 6 | `ProductVariants` | Core | Biến thể Size món (Size S, Size M, Size L) |
| 7 | `Toppings` | Core | Danh sách topping chọn thêm (Trân châu, Thạch) |
| 8 | `ProductIngredients` | Core | Công thức định lượng pha chế (dùng cho KDS & Kho) |
| 9 | `Combos` | Core | Thông tin các gói Combo ưu đãi |
| 10 | `ComboItems` | Core | Món ăn nằm trong gói Combo |
| 11 | `Orders` | Order | Đơn hàng tổng hợp (Status, TotalAmount, TableId) |
| 12 | `OrderItems` | Order | Chi tiết từng món trong đơn (Size, Đường, Đá, Ghi chú) |
| 13 | `OrderItemToppings` | Order | Topping chọn kèm cho từng món |
| 14 | `Payments` | Order | Giao dịch thanh toán (Tiền mặt, VietQR, Status) |
| 15 | `Users` | User & Auth | Tài khoản Admin, Quản lý, Phục vụ, Phân quyền |
| 16 | `BranchUsers` | User & Auth | Bảng trung gian gán Nhân sự vào Chi nhánh |
| 17 | `Customers` | CRM | Hồ sơ Khách hàng (SĐT, Tích điểm, Hạng thẻ) |
| 18 | `Ingredients` | Inventory | Danh mục Nguyên liệu thô (CF hạt, Sữa, Đường) |
| 19 | `InventoryStocks` | Inventory | Số lượng tồn kho nguyên liệu theo từng chi nhánh |
| 20 | `StockTransactions` | Inventory | Nhật ký lịch sử Nhập/Xuất/Kiểm kê kho |
| 21 | `Attendances` | HRM | Dữ liệu chấm công nhân viên (Check-in, Check-out + GPS) |
| 22 | `CashShifts` | HRM & Finance | Quản lý Két tiền ca làm (Tiền đầu ca, Kết ca, Lệch két) |
| 23 | `Shifts` | HRM | Lịch phân ca nhân viên |
| 24 | `LoyaltyTransactions`| CRM | Lịch sử Tích điểm / Tiêu điểm của Khách |
| 25 | `Vouchers` | CRM | Danh sách mã giảm giá Khuyến mãi |
| 26 | `VoucherUsages` | CRM | Lịch sử khách hàng sử dụng mã Voucher |
| 27 | `Reviews` | CRM | Feedback đánh giá 1-5 sao từ khách |
| 28 | `ReviewImages` | CRM | Ảnh đính kèm trong feedback khách |
