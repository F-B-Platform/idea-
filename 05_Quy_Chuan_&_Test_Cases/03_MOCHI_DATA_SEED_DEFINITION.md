# 🌱 DỮ LIỆU MẪU BAN ĐẦU (SEED DATA SPECIFICATION)

> **Dự án:** Smart F&B Operating System  
> **Mục tiêu:** Cung cấp bộ dữ liệu mẫu chuẩn hóa để tự động chèn vào Database khi khởi chạy ứng dụng lần đầu (`dotnet ef database update`).

---

## 1. DỮ LIỆU TÀI KHOẢN MẶC ĐỊNH (USERS & ACCOUNTS)

Mật khẩu mặc định cho tất cả tài khoản test: **`SmartFB@2026!`** (đã hash BCrypt).

| Full Name | Email (Login ID) | Role | Chi nhánh gán |
|---|---|---|---|
| Nguyễn Admin | `admin@smartfb.vn` | `Admin` | Toàn bộ 3 chi nhánh |
| Trần Quản Lý Q1 | `manager.q1@smartfb.vn` | `Manager` | Chi nhánh Quận 1 |
| Lê Quản Lý Thủ Đức | `manager.thuduc@smartfb.vn` | `Manager` | Chi nhánh Thủ Đức |
| Phạm Barista | `barista.q1@smartfb.vn` | `Staff` | Chi nhánh Quận 1 |
| Hoàng Phục Vụ | `staff.q1@smartfb.vn` | `Staff` | Chi nhánh Quận 1 |

---

## 2. DỮ LIỆU CHI NHÁNH & BÀN (BRANCHES & TABLES)

### 2.1 Chi Nhánh
1. **Smart Coffee Quận 1:** `123 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP.HCM` | SĐT: `02838111222`
2. **Smart Coffee Thủ Đức:** `45 Võ Văn Ngân, Phường Bình Thọ, TP. Thủ Đức` | SĐT: `02838333444`
3. **Smart Coffee Quận 7:** `88 Nguyễn Thị Thập, Phường Tân Phú, Quận 7, TP.HCM` | SĐT: `02838555666`

### 2.2 Danh Sách Bàn (Mỗi chi nhánh seed 10 bàn)
* **Khu vực Trong Nhà (Indoor Zone):** Bàn 1 ➔ Bàn 6 (Sức chứa 4 chỗ)
* **Khu vực Sân Thượng (Terrace Zone):** Bàn 7 ➔ Bàn 9 (Sức chứa 2 chỗ)
* **Khu vực VIP (VIP Zone):** Bàn VIP-1 (Sức chứa 8 chỗ)

---

## 3. DỮ LIỆU MENU MÓN ĂN UỐNG (CATEGORIES, PRODUCTS, VARIANTS, TOPPINGS)

### 3.1 Danh Mục (Categories)
1. **Cà Phê Truyền Thống** ☕ (DisplayOrder: 1)
2. **Trà & Trà Sữa** 🧋 (DisplayOrder: 2)
3. **Bánh Ngọt & Croissant** 🥐 (DisplayOrder: 3)

### 3.2 Sản Phẩm Mẫu (Products)

| Tên Món | Danh mục | Giá gốc (BasePrice) | Tag | Allergens | Recipe Instructions (Hiển thị KDS) |
|---|---|---|---|---|---|
| **Bạc Xỉu Sài Gòn** | Cà Phê | 35.000 VNĐ | Best Seller | Sữa | Espresso 1 shot (18ml) + Sữa đặc 30ml + Sữa tươi 40ml + Đá 150g |
| **Cà Phê Muối** | Cà Phê | 39.000 VNĐ | Hot | Sữa | Espresso 2 shot (36ml) + Kem béo mặn 40ml + Đá 150g |
| **Americano Đá** | Cà Phê | 32.000 VNĐ | - | Không | Espresso 2 shot (36ml) + Nước lọc 150ml + Đá 100g |
| **Trà Đào Cam Sả** | Trà | 45.000 VNĐ | Best Seller | Không | Cốt trà Black Tea 150ml + Siro Đào 30ml + Nước sả 20ml + 2 lát đào |
| **Trà Sữa Ô Long Oolong**| Trà Sữa | 42.000 VNĐ | Hot | Sữa | Cốt trà Ô long 150ml + Bột kem sữa 30g + Đường 25ml + Đá 150g |
| **Bánh Croissant Bơ Tỏi**| Bánh Ngọt | 38.000 VNĐ | New | Lúa mì, Bơ | Nướng lò 180°C trong 3 phút ➔ Phết sốt bơ tỏi ➔ Rắc hành tây |

### 3.3 Biến Thể Size (ProductVariants)
* **Size S:** Cộng thêm `0 VNĐ` (Default)
* **Size M:** Cộng thêm `5.000 VNĐ`
* **Size L:** Cộng thêm `10.000 VNĐ`

### 3.4 Toppings Chosen
* **Trân Châu Đen Oolong:** `10.000 VNĐ`
* **Thạch Dừa Giòn:** `8.000 VNĐ`
* **Kem Cheese Macchiato:** `12.000 VNĐ`
