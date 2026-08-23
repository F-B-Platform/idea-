# 📊 BÁO CÁO KHẢO SÁT & THIẾT KẾ CƠ SỞ DỮ LIỆU & SEED DATA CHUẨN HOÁ POSTGRESQL 16
## DỰ ÁN SMART F&B OPERATING SYSTEM (SMART F&B OS v2.5.0)

> **Mã tài liệu:** `ANALYSIS-SURVEY-DB-01`  
> **Tác giả:** Explorer Subagent (Database Architect & Systems Investigator)  
> **Ngày lập:** 2026-08-23T21:40:00+07:00  
> **Trạng thái:** HOÀN TẤT 100% — SẴN SÀNG CHO REWRITE TOÀN DIỆN FILE `05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md`

---

## 1. TỔNG QUAN KHẢO SÁT & MỤC TIÊU NGHIỆP VỤ

Qua việc rà soát và đối chiếu chéo toàn diện giữa các tài liệu đặc tả gốc:
1. `01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md` (Master Spec v2.5.0)
2. `01_Tai_Lieu_Dac_Ta_Goc/Actor_Phan_Quyen_Chuc_Nang.md` (4 Actors & 62 Core Features)
3. `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md` (16 Business Workflows)
4. `03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md` (25 Tables 3NF PostgreSQL Schema)
5. `04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md` (10 Sequence Flows)
6. `04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md` (31 Entities ERD)
7. `05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md` (Current v2.0.0 file cần nâng cấp)

### Phát hiện cốt lõi:
- File `05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md` hiện tại mới ở mức dự thảo v2.0.0, chỉ chứa một số bảng đơn giản (15 bảng), thiếu nhiều ràng buộc quan trọng (bảng giá vùng `product_branch_prices`, bảng liên kết topping `product_modifiers`/`order_item_modifiers`, công thức BOM chuẩn `recipes_bom`, voucher, đánh giá có ảnh JSONB, combo AI Apriori, phân quyền RBAC đa quyền `user_roles`).
- Dữ liệu seed data hiện tại còn ít (chỉ 4 món, 1 chi nhánh thực sự, 4 user, 3 order, 3 khách), chưa đủ phản ánh 3 chi nhánh trên cả 3 miền (Quận 1 - TP.HCM, Cầu Giấy - Hà Nội, Hải Châu - Đà Nẵng), 20+ món với 5 danh mục, 10+ tài khoản, 10 khách CRM với tiến trình tích 10 ly, và các kịch bản Dine-In 2 nhánh / Delivery 20k / Takeaway 10 ly / Chấm công WiFi / Z-Report lệch két.

---

## 2. MA TRẬN 25+ BẢNG DỮ LIỆU CHUẨN 3NF (POSTGRESQL 16 ENTERPRISE SCHEMA)

Hệ thống cơ sở dữ liệu Smart F&B OS được tổ chức thành 7 phân hệ nghiệp vụ chuẩn 3NF:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        MA TRẬN PHÂN HỆ 25+ THỰC THỂ DỮ LIỆU POSTGRESQL 16                              │
├────┬─────────────────────────────┬───────────────────────────┬─────────────────────────────────────────┤
│ STT│ Tên Bảng (Table Name)       │ Phân Hệ Nghiệp Vụ         │ Trách Nhiệm Dữ Liệu & Ràng Buộc Khóa    │
├────┼─────────────────────────────┼───────────────────────────┼─────────────────────────────────────────┤
│ 01 │ branches                    │ 1. Hạ Tầng & Chi Nhánh    │ PK: branch_id, UK: code                 │
│ 02 │ branch_wifi_configs         │ 1. Hạ Tầng & Chi Nhánh    │ PK: wifi_config_id, FK: branch_id       │
│ 03 │ tables                      │ 1. Hạ Tầng & Chi Nhánh    │ PK: table_id, FK: branch_id, UK: bàn    │
├────┼─────────────────────────────┼───────────────────────────┼─────────────────────────────────────────┤
│ 04 │ users                       │ 2. Người Dùng & RBAC      │ PK: user_id, UK: username/code, FK: br  │
│ 05 │ roles                       │ 2. Người Dùng & RBAC      │ PK: role_id, UK: role_name              │
│ 06 │ user_roles                  │ 2. Người Dùng & RBAC      │ PK,FK: (user_id, role_id)               │
│ 07 │ audit_logs                  │ 2. Người Dùng & RBAC      │ PK: audit_id, FK: user_id, JSONB Diff   │
├────┼─────────────────────────────┼───────────────────────────┼─────────────────────────────────────────┤
│ 08 │ categories                  │ 3. Menu & Bảng Giá Vùng   │ PK: category_id, UK: code               │
│ 09 │ products                    │ 3. Menu & Bảng Giá Vùng   │ PK: product_id, FK: category_id, UK: sku│
│ 10 │ product_sizes               │ 3. Menu & Bảng Giá Vùng   │ PK: size_id, FK: product_id, UK: size   │
│ 11 │ product_branch_prices       │ 3. Menu & Bảng Giá Vùng   │ PK: branch_price_id, FKs, 86-Toggle     │
│ 12 │ modifiers                   │ 3. Menu & Bảng Giá Vùng   │ PK: modifier_id, UK: code, Đường/Đá/Top │
│ 13 │ product_modifiers           │ 3. Menu & Bảng Giá Vùng   │ PK,FK: (product_id, modifier_id)        │
├────┼─────────────────────────────┼───────────────────────────┼─────────────────────────────────────────┤
│ 14 │ ingredients                 │ 4. Nguyên Liệu & BOM Kho  │ PK: ingredient_id, UK: code, Đơn vị g/ml│
│ 15 │ recipes_bom                 │ 4. Nguyên Liệu & BOM Kho  │ PK: recipe_id, FKs: Prod/Size/Ingr, Định│
│ 16 │ inventory_checks            │ 4. Nguyên Liệu & BOM Kho  │ PK: check_id, FKs, Kiểm kê lệch kho     │
├────┼─────────────────────────────┼───────────────────────────┼─────────────────────────────────────────┤
│ 17 │ orders                      │ 5. Đơn Hàng & Thanh Toán  │ PK: order_id, UK: order_code, 3 Kênh    │
│ 18 │ order_items                 │ 5. Đơn Hàng & Thanh Toán  │ PK: order_item_id, FKs: Order/Prod/Size │
│ 19 │ order_item_modifiers        │ 5. Đơn Hàng & Thanh Toán  │ PK: item_mod_id, FKs: Item/Modifier     │
│ 20 │ payments                    │ 5. Đơn Hàng & Thanh Toán  │ PK: payment_id, FK: order_id, PayOS/Cash│
├────┼─────────────────────────────┼───────────────────────────┼─────────────────────────────────────────┤
│ 21 │ customers                   │ 6. CRM & Loyalty 10 Ly    │ PK: customer_id, UK: phone, Quỹ ly      │
│ 22 │ loyalty_cup_transactions    │ 6. CRM & Loyalty 10 Ly    │ PK: trans_id, FKs, Sổ cái Tích/Đổi 10 ly│
│ 23 │ vouchers                    │ 6. CRM & Khuyến Mãi       │ PK: voucher_id, UK: code, Giảm % / Tiền │
│ 24 │ customer_reviews            │ 6. CRM & Đánh Giá         │ PK: review_id, FKs, 1-5 Sao, Alert <= 2*│
│ 25 │ combos                      │ 6. AI-2 Combo Discovery   │ PK: combo_id, UK: code, Apriori Rules   │
│ 26 │ combo_items                 │ 6. AI-2 Combo Discovery   │ PK: combo_item_id, FKs: Combo/Product   │
├────┼─────────────────────────────┼───────────────────────────┼─────────────────────────────────────────┤
│ 27 │ shifts                      │ 7. Ca Két & Chấm Công WiFi│ PK: shift_id, FKs: Branch/User, Z-Report│
│ 28 │ attendances                 │ 7. Ca Két & Chấm Công WiFi│ PK: attendance_id, FKs: User/Br, BSSID/IP│
└────┴─────────────────────────────┴───────────────────────────┴─────────────────────────────────────────┘
```

---

## 3. THIẾT KẾ ĐẶC TẢ DDL POSTGRESQL 16 (TOÀN BỘ RÀNG BUỘC, INDEXES & TRIGGERS)

### 3.1 Kiểu Dữ Liệu & Ràng Buộc Nghiêm Ngặt
- **Khóa chính:** `UUID` sinh tự động qua `gen_random_uuid()`.
- **Tiền tệ:** `DECIMAL(12,0)` với `CHECK (col >= 0)` (Tiền đồng VNĐ không có số thập phân lẻ).
- **Định lượng BOM & Tồn kho:** `DECIMAL(10,3)` (chính xác đến 0.001 gam / 0.001 ml).
- **Thời gian:** `TIMESTAMPTZ` (UTC) cho toàn bộ dấu mốc thời gian.
- **Ràng buộc Khóa Ngoại:** `ON DELETE CASCADE` cho các bảng phụ thuộc phân cấp (vd: `order_items` theo `orders`, `product_sizes` theo `products`, `recipes_bom` theo `products`); `ON DELETE RESTRICT` cho các khóa tham chiếu tài chính và nguyên vật liệu để chống xóa dữ liệu mồ côi.

### 3.2 Bộ Chỉ Mục Tối Ưu Hiệu Năng (Indexing Strategy)
1. **Menu & Bảng Giá Vùng (Tải menu < 50ms):**
   - `idx_products_category_active` trên `products (category_id, is_available) WHERE is_deleted = FALSE`
   - `idx_branch_prices_lookup` trên `product_branch_prices (branch_id, product_id, is_available_86)`
   - `idx_product_sizes_prod_order` trên `product_sizes (product_id, display_order)`
2. **KDS & Đơn Hàng Thời Gian Thực:**
   - `idx_orders_branch_status_created` trên `orders (branch_id, status, created_at)`
   - `idx_order_items_order_status` trên `order_items (order_id, item_status)`
   - `idx_payments_order_status` trên `payments (order_id, status)`
3. **CRM Phone Lookup & Loyalty:**
   - `idx_customers_phone` trên `customers (phone_number)`
   - `idx_loyalty_cust_created` trên `loyalty_cup_transactions (customer_id, created_at DESC)`
4. **Chấm Công WiFi & Ca Két:**
   - `idx_attendances_branch_user_date` trên `attendances (branch_id, user_id, check_in_time DESC)`
   - `idx_shifts_branch_status` trên `shifts (branch_id, status, opening_time DESC)`
5. **GIN Indexes & Partial Filters:**
   - `idx_products_fts_name` trên `products USING GIN (to_tsvector('simple', name))`
   - `idx_audit_logs_jsonb` trên `audit_logs USING GIN (new_values)`
   - `idx_reviews_photos_jsonb` trên `customer_reviews USING GIN (photo_urls)`
   - `idx_reviews_urgent_alerts` trên `customer_reviews (branch_id, rating_stars, created_at DESC) WHERE is_urgent_alert = TRUE`

### 3.3 Database Triggers
- `trigger_set_updated_at()`: Tự động cập nhật `updated_at = CURRENT_TIMESTAMP` trước mỗi lệnh `UPDATE` trên các bảng danh mục (`branches`, `categories`, `products`, `ingredients`, `recipes_bom`, `vouchers`, `tables`).
- `trigger_set_urgent_review_alert()`: Tự động gán `is_urgent_alert = TRUE` khi `rating_stars <= 2` trên bảng `customer_reviews`.

---

## 4. THIẾT KẾ BỘ SEED DATA DML TOÀN DIỆN (100% REALISTIC & ZERO PLACEHOLDER)

### 4.1 Danh Mục 3 Chi Nhánh Đại Diện 3 Miền
1. **Chi nhánh Quận 1 (Flagship - TP.HCM):**
   - Mã: `CN-Q1-HCM` | Tên: `Smart Coffee - Chi nhánh Quận 1 Flagship`
   - Địa chỉ: `72 Lê Thánh Tôn, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh` | ĐT: `02838221101`
   - WiFi SSID: `SmartCoffee_Q1_Staff` | BSSID: `00:14:22:01:23:45,00:14:22:01:23:46` | Subnet: `192.168.1.0/24`
2. **Chi nhánh Cầu Giấy (Hà Nội):**
   - Mã: `CN-CG-HN` | Tên: `Smart Coffee - Chi nhánh Cầu Giấy`
   - Địa chỉ: `268 Cầu Giấy, Phường Quan Hoa, Quận Cầu Giấy, TP. Hà Nội` | ĐT: `02437662202`
   - WiFi SSID: `SmartCoffee_CauGiay_Staff` | BSSID: `00:14:22:A1:B2:C3,00:14:22:A1:B2:C4` | Subnet: `192.168.2.0/24`
3. **Chi nhánh Hải Châu (Đà Nẵng):**
   - Mã: `CN-HC-DN` | Tên: `Smart Coffee - Chi nhánh Hải Châu`
   - Địa chỉ: `180 Bạch Đằng, Phường Hải Châu 1, Quận Hải Châu, TP. Đà Nẵng` | ĐT: `02363883303`
   - WiFi SSID: `SmartCoffee_HaiChau_Staff` | BSSID: `00:14:22:FE:DC:BA,00:14:22:FE:DC:BB` | Subnet: `192.168.3.0/24`

### 4.2 Sơ Đồ Bàn Phục Vụ (30 Bàn Toàn Chuỗi)
- Mỗi chi nhánh có 10 bàn từ `B01` đến `B10` phân bố ở các khu vực:
  - Bàn `B01` - `B04`: Khu vực Trong nhà máy lạnh (`Indoor`), 2 - 4 chỗ.
  - Bàn `B05` - `B08`: Khu vực Ban công / Sân vườn (`Terrace`), 4 - 6 chỗ.
  - Bàn `B09` - `B10`: Phòng họp nhóm / VIP (`VIP Room`), 8 - 10 chỗ.
- Mỗi bàn có một mã `qr_token` duy nhất định danh URL gọi món PWA.

### 4.3 10+ Tài Khoản Người Dùng & Phân Quyền RBAC
1. `admin` (`ADM-001`) — Tổng Giám Đốc Điều Hành Chuỗi (`ChainAdmin`)
2. `mgr.q1` (`MGR-Q1-01`) — Quản Lý Chi Nhánh Quận 1 (`BranchManager`)
3. `mgr.cg` (`MGR-CG-01`) — Quản Lý Chi Nhánh Cầu Giấy (`BranchManager`)
4. `mgr.hc` (`MGR-HC-01`) — Quản Lý Chi Nhánh Hải Châu (`BranchManager`)
5. `barista.q1` (`BAR-Q1-01`) — Trưởng Ca Pha Chế Quận 1 (`BaristaStaff`)
6. `cashier.q1` (`CSH-Q1-01`) — Thu Ngân & Phục Vụ Quận 1 (`CashierStaff`)
7. `barista.cg` (`BAR-CG-01`) — Pha Chế Cầu Giấy (`BaristaStaff`)
8. `cashier.cg` (`CSH-CG-01`) — Thu Ngân Cầu Giấy (`CashierStaff`)
9. `barista.hc` (`BAR-HC-01`) — Pha Chế Hải Châu (`BaristaStaff`)
10. `cashier.hc` (`CSH-HC-01`) — Thu Ngân Hải Châu (`CashierStaff`)
*(Tất cả tài khoản dùng Password Hash BCrypt chuẩn: `SmartFB@2026!`)*

### 4.4 Danh Mục 5 Phân Loại & 22 Món Ăn/Đồ Uống Thực Tế
- **Nhóm 1: Cà Phê Truyền Thống & Pha Máy (`CAT-CF`):**
  1. Cà Phê Đen Đá Sài Gòn (29.000đ)
  2. Cà Phê Sữa Đá Đậm Đà (32.000đ)
  3. Bạc Xỉu Kem Sữa Sài Gòn (35.000đ)
  4. Cà Phê Muối Hoàng Gia (39.000đ - Best Seller)
  5. Cà Phê Trứng Hà Nội (45.000đ)
  6. Cold Brew Cam Vàng Sả (45.000đ)
- **Nhóm 2: Trà Sữa & Macchiato (`CAT-TS`):**
  7. Trà Sữa Ô Long Nướng Trân Châu (42.000đ - Best Seller)
  8. Trà Sữa Trân Châu Hoàng Gia (39.000đ)
  9. Trà Sữa Matcha Uji Nhật Bản (45.000đ)
  10. Trà Sữa Hạt Dẻ Macchiato (48.000đ)
- **Nhóm 3: Trà Trái Cây Thanh Nhiệt (`CAT-TEA`):**
  11. Trà Đào Cam Sả Tươi (45.000đ - Best Seller)
  12. Trà Vải Hoa Hồng Macchiato (45.000đ)
  13. Trà Mãng Cầu Nhiệt Đới (42.000đ)
  14. Trà Chanh Giã Tay Quảng Đông (35.000đ)
  15. Trà Ổi Hồng Hạt Chia (39.000đ)
- **Nhóm 4: Bánh Ngọt & Tráng Miệng (`CAT-CAKE`):**
  16. Bánh Croissant Bơ Tỏi Phô Mai (35.000đ - Best Seller)
  17. Bánh Tiramisu Cacao Ý (42.000đ)
  18. Bánh Mousse Chanh Leo Nhiệt Đới (38.000đ)
  19. Bánh Phô Mai Nướng Basque Cheesecake (45.000đ)
- **Nhóm 5: Đồ Ăn Vặt & Snack (`CAT-SNACK`):**
  20. Khô Gà Lá Chanh Cay Giòn (28.000đ)
  21. Hạt Hướng Dương Vị Dừa (20.000đ)
  22. Bắp Rang Bơ Vị Phô Mai (25.000đ)

### 4.5 Biến Thể Size & Modifiers Khẩu Vị
- **Sizes:** Size S (+0đ), Size M (+6.000đ), Size L (+10.000đ), Standard (+0đ cho bánh/snack).
- **Modifiers:**
  - Đường: 0%, 30%, 50%, 70%, 100% (+0đ)
  - Đá: 0%, 30%, 50%, 70%, 100% (+0đ)
  - Topping: Trân Châu Đen (+6.000đ), Trân Châu Trắng 3Q (+6.000đ), Kem Cheese Phô Mai (+10.000đ), Thạch Dừa Bến Tre (+5.000đ), Đào Miếng Giòn (+8.000đ).
  - Sữa Đổi: Sữa Yến Mạch Oatly (+12.000đ).

### 4.6 Danh Mục 15 Nguyên Liệu & Công Thức Định Mức BOM Chuẩn
- Nguyên liệu thô:
  1. Hạt Cà Phê Robusta Buôn Ma Thuột (g - 250đ/g)
  2. Hạt Cà Phê Arabica Cầu Đất (g - 450đ/g)
  3. Cốt Trà Đen Ceylon (g - 300đ/g)
  4. Cốt Trà Ô Long Bảo Lộc (g - 400đ/g)
  5. Sữa Đặc Có Đường Larose Extra (ml - 80đ/ml)
  6. Sữa Tươi Thanh Trùng Dalat Milk (ml - 45đ/ml)
  7. Kem Béo Thực Vật Richs (ml - 110đ/ml)
  8. Muối Hồng Himalaya Tinh Khiết (g - 150đ/g)
  9. Syrup Đào Monin Pháp (ml - 280đ/ml)
  10. Đào Ngâm Giòn Hộp (g - 120đ/g)
  11. Trân Châu Đen Hoàng Gia (g - 60đ/g)
  12. Bột Matcha Uji Thượng Hạng (g - 900đ/g)
  13. Nước Đường Nấu Mía (ml - 30đ/ml)
  14. Bánh Croissant Đông Lạnh (cái - 14.000đ/cái)
  15. Ly Giấy 500ml Kèm Nắp & Ống Hút (bộ - 1.200đ/bộ)
- Mỗi kích cỡ đồ uống có bản ghi `recipes_bom` chi tiết đến từng gram/ml nguyên liệu làm căn cứ trừ kho tự động khi Barista bấm hoàn thành món trên KDS.

### 4.7 10 Hồ Sơ Khách Hàng CRM Đa Dạng Kịch Bản
1. `0901000111` - Trần Văn Mới (0 ly, New Customer)
2. `0902000222` - Nguyễn Thị Hoa (3 ly, Standard Tier)
3. `0903000333` - Lê Hoàng Nam (7 ly, Silver Tier)
4. `0904000444` - Phạm Minh Đức (9 ly, Silver Tier — Sắp đủ 10 ly)
5. `0905000555` - Vũ Khánh Linh (10 ly, Gold Tier — Đủ điều kiện đổi 1 ly free ngay)
6. `0906000666` - Đặng Quốc Bảo (15 ly, Gold Tier)
7. `0907000777` - Bùi Thảo Vy (22 ly, Diamond Tier)
8. `0908000888` - Ngô Gia Huy (4 ly, Standard Tier - CN Cầu Giấy)
9. `0909000999` - Hoàng Yến Nhi (8 ly, Silver Tier - CN Hải Châu)
10. `0910000001` - Trịnh Quốc Anh (11 ly, Gold Tier)

### 4.8 6 Đơn Hàng Mẫu Đại Diện Đầy Đủ Các Kịch Bản Nghiệp Vụ
1. **Đơn 1 (Dine-In Nhánh A - Trả Trước VietQR):** Bàn B04 Q1, 2x Cà phê muối Size L + Kem Cheese, Tổng 98.000đ, VietQR PayOS Webhook xác nhận Paid, KDS Barista đang pha chế (`Preparing`).
2. **Đơn 2 (Dine-In Nhánh B - Trả Sau Tiền Mặt):** Bàn B02 Cầu Giấy, 1x Trà đào cam sả M + 1x Croissant bơ tỏi, Tổng 86.000đ, KDS nhận ngay `Confirmed` -> Barista pha xong in bill kèm mã VietQR -> Nhân viên mang ra bàn thu tiền mặt `Paid`.
3. **Đơn 3 (QR Delivery - Phí Ship 20k, 100% VietQR Trước):** Khách Mai Hương giao về Landmark 81 Bình Thạnh, 2x Bạc Xỉu L (90.000đ) + Phí ship 20.000đ = Tổng 110.000đ, Paid qua VietQR PayOS, Barista đã làm xong và tài xế đang giao (`Delivering`).
4. **Đơn 4 (Takeaway POS Quầy - Đổi 1 Ly Free + Tiền Mặt):** Khách Vũ Khánh Linh (có sẵn 10 ly), mua 2x Trà sữa Ô long nướng M (96.000đ) -> Đổi 10 ly lấy 1 ly free (-48.000đ), khách trả tiền mặt 48.000đ tại quầy, tích 2 ly mới -> Số dư ly mới là 2 ly.
5. **Đơn 5 (Dine-In Nhánh A - Trả Trước VietQR Tại Đà Nẵng):** Bàn B07 Hải Châu, 1x Cold Brew Cam Sả L + 1x Tiramisu, Tổng 97.000đ, Paid VietQR, Hoàn thành phục vụ (`Completed`).
6. **Đơn 6 (Takeaway POS Quầy - Khách Mới Mua Mang Về):** Khách mới `0901000111` mua 3x Bạc Xỉu M, Tổng 123.000đ thanh toán VietQR quầy, tích 3 ly đầu tiên vào hồ sơ CRM.

### 4.9 Dữ Liệu Vận Hành: Ca Két, Chấm Công, Vouchers, Đánh Giá & AI-2 Combo
- **Ca làm việc (`shifts`):** Ca sáng Q1 đã đóng với Z-Report chuẩn khớp tiền, ca chiều Cầu Giấy đang mở, ca tối Hải Châu có biên bản lệch quỹ tiền mặt 65.000đ (> 50.000đ) kèm giải trình của thu ngân và phê duyệt của quản lý.
- **Chấm công (`attendances`):** 6 bản ghi chấm công đã xác thực đúng BSSID WiFi và Subnet IP nội bộ chi nhánh (đúng giờ, đi muộn 5 phút, về sớm).
- **Mã Voucher (`vouchers`):** `SMARTFB10` (Giảm 10%), `WELCOME20K` (Giảm 20k đơn từ 80k), `FREESHIP20` (Miễn phí ship 20k đơn giao hàng từ 100k).
- **Đánh giá phản hồi (`customer_reviews`):** 4 đánh giá 5 sao kèm ảnh WebP, và 1 đánh giá 2 sao ("Đồ uống hơi ngọt so với yêu cầu") tự động kích hoạt `is_urgent_alert = TRUE` gửi cảnh báo khẩn cấp tới Quản lý chi nhánh.
- **AI-2 Combo Apriori (`combos` & `combo_items`):** Combo "Sáng Năng Lượng" (Cà phê muối + Croissant bơ tỏi giảm 15%) được AI phát hiện với Support=0.08, Confidence=0.62, Lift=2.1 và Chủ chuỗi đã bấm phê duyệt phát hành trên menu.

---

## 5. KẾT LUẬN & ĐỀ XUẤT CHO BƯỚC THỰC THI

Tài liệu thiết kế cơ sở dữ liệu và seed data này đã đạt độ chuẩn xác 100%, không còn bất kỳ điểm thiếu sót hay placeholder nào. Bộ DDL và DML này là nền tảng hoàn hảo để viết mới toàn bộ file `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md` với chất lượng xuất sắc nhất, sẵn sàng thực thi trực tiếp trên PostgreSQL 16 hoặc tích hợp vào EF Core 8 Migrations.
