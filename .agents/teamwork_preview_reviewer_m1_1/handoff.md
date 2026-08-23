# 📋 BÁO CÁO ĐÁNH GIÁ & PHẢN BIỆN CHẤT LƯỢNG (REVIEW & ADVERSARIAL CRITIC REPORT)
## Milestone M1: Requirements Analysis & Database Architecture
**Người thực hiện:** Reviewer 1 (Reviewer & Adversarial Critic — Milestone M1)  
**Ngày hoàn thành:** 2026-08-23  
**Working Directory:** `d:\Idea_DoAn\.agents\teamwork_preview_reviewer_m1_1\`  
**Target Files Reviewed:**
1. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md` (827 lines, 97,709 bytes)
2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md` (1340 lines, 56,261 bytes)

---

## Review Summary

**VERDICT: APPROVE ✅**

Hai tài liệu bàn giao thuộc Milestone M1 (`01_Phan_Tich_Yeu_Cau.md` và `02_Thiet_Ke_Database.md`) đạt chất lượng kỹ thuật xuất sắc, đáp ứng 100% các tiêu chí nghiệm thu khắt khe từ Master Spec v2.5.0 và Project Scope, tuân thủ triệt để nguyên tắc **Zero Placeholder**, bảo toàn chuẩn hóa dữ liệu 3NF và không chứa bất kỳ lỗ hổng toàn vẹn (integrity violation) nào.

---

## 1. Observation (Quan Sát Trực Tiếp)

### 1.1 Kiểm tra phạm vi 62 Tính năng cốt lõi (01_Phan_Tich_Yeu_Cau.md)
- **Đếm số lượng tính năng thực tế:**
  - Customer (`C-01` đến `C-20`): **20/20 tính năng** (dòng 206 - 367)
  - Staff / Barista (`S-01` đến `S-13`): **13/13 tính năng** (dòng 373 - 485)
  - Branch Manager (`M-01` đến `M-12`): **12/12 tính năng** (dòng 491 - 588)
  - Chain Admin (`A-01` đến `A-17`): **17/17 tính năng** (dòng 594 - 738)
  - **Tổng cộng: 62/62 tính năng** được định nghĩa chi tiết với đầy đủ 5 trường bắt buộc: *Mô tả, Quy tắc & Ràng buộc, Hợp đồng dữ liệu (Input/Output Schema), Kịch bản biên & Xử lý ngoại lệ, Tiêu chí nghiệm thu định lượng*.
- **Ma trận truy vết (RTM):** 62/62 dòng ánh xạ hoàn chỉnh từ Feature Code sang Database Table (02), API Endpoint (03) và UI Screen Route (04) tại dòng 759 - 822.
- **Loại bỏ các khái niệm phế truất:** 
  - Khái niệm `Staff Mobile App (Flutter/React Native)`, `Chấm công GPS 50m`, `Mã QR Động Xoay 30s`, `C-23 (Chia sẻ MXH)`, `C-24 (Push PWA)`, `Ví Voucher riêng`, `Tra cứu Calo riêng` đã được loại bỏ 100% khỏi luồng nghiệp vụ hoạt động và gom vào Bảng giải trình loại bỏ vĩnh viễn (Phần 3, dòng 163 - 187).

### 1.2 Kiểm tra kiến trúc Cơ sở dữ liệu 25 Bảng chuẩn 3NF (02_Thiet_Ke_Database.md)
- **Danh mục 25 bảng thực thể PostgreSQL 16:**
  1. `branches` | 2. `branch_wifi_configs` | 3. `tables` | 4. `users` | 5. `roles` | 6. `user_roles` | 7. `audit_logs` | 8. `categories` | 9. `products` | 10. `product_sizes` | 11. `product_branch_prices` | 12. `modifiers` | 13. `product_modifiers` | 14. `ingredients` | 15. `recipes_bom` | 16. `customers` | 17. `orders` | 18. `order_items` | 19. `order_item_modifiers` | 20. `payments` | 21. `loyalty_cup_transactions` | 22. `vouchers` | 23. `customer_reviews` | 24. `shifts` | 25. `attendances`.
- **Toàn vẹn khóa ngoại (Foreign Keys):** 33/33 ràng buộc khóa ngoại `REFERENCES` tham chiếu chính xác đến bảng và cột khóa chính tồn tại trong hệ thống.
- **Kiểu dữ liệu và độ chính xác:**
  - Tiền tệ: `DECIMAL(12,0)` cho toàn bộ các trường giá bán, phụ thu, chiết khấu, tổng tiền, tiền két (loại trừ sai số dấu phẩy động).
  - Tồn kho & Định lượng BOM: `DECIMAL(10,3)` cho `current_stock`, `min_stock_threshold`, `standard_quantity` (đạt độ chính xác 0.001 g/ml).
  - Tỷ lệ hao hụt: `DECIMAL(5,2)` cho `wastage_percentage`.
  - Khóa chính: 100% dùng `UUID` với hàm sinh mặc định `gen_random_uuid()`.
- **Triggers & Indexes:**
  - 8 Triggers PL/pgSQL: 7 triggers cập nhật `updated_at` và 1 trigger tự động bật cờ cảnh báo khẩn cấp `is_urgent_alert` khi `rating_stars <= 2`.
  - 17 Indexes tối ưu hóa: Composite indexes (Menu, KDS, CRM, Shifts, Orders), GIN Full-Text Search index cho `products.name` không dấu, GIN JSONB index cho `audit_logs` và `customer_reviews.photo_urls`.
- **C# EF Core 8 Fluent API:** 4 Configurations mẫu (`OrderConfiguration`, `RecipeBomConfiguration`, `AttendanceConfiguration`, `ShiftConfiguration`) được viết hoàn chỉnh 100% C# code với Fluent API, ánh xạ quan hệ 1-N, N-N, Precision và Default Values.

### 1.3 Kiểm tra cú pháp sơ đồ Mermaid & Zero Placeholders
- `01_Phan_Tich_Yeu_Cau.md`: Sơ đồ `flowchart TD` phân định 2 nhánh Dine-In (Nhánh A: VietQR trước vs Nhánh B: Tiền mặt sau kèm Bill QR) có cú pháp hợp lệ 100%.
- `02_Thiet_Ke_Database.md`: Sơ đồ `erDiagram` thể hiện đủ 25 thực thể và liên kết quan hệ có cú pháp hợp lệ 100%.
- **Zero Placeholders:** Quét toàn bộ 2 file với regex `TODO`, `TBD`, `/* rest of code */`, `// tương tự`, `...` -> **0 lỗi vi phạm**.

---

## 2. Logic Chain (Chuỗi Lập Luận Đánh Giá)

1. *Từ đối chiếu Master Spec (`01_Tai_Lieu_Dac_Ta_Goc`) và `PROJECT.md`:* Yêu cầu cốt lõi của Milestone M1 là thiết lập một nền tảng đặc tả nghiệp vụ 62 tính năng và cơ sở dữ liệu 25 bảng chuẩn 3NF không sai lệch một chi tiết nào.
2. *Từ phân tích ma trận tác động (Impact Mapping):*
   - `01_Phan_Tich_Yeu_Cau.md` đã thiết kế chuẩn 4 động cơ vận hành:
     * *Dine-In 2 nhánh:* Nhánh A KDS chỉ nhận đơn khi `Paid`, Nhánh B KDS nhận đơn ngay `Confirmed` và in hóa đơn có sẵn Bill QR.
     * *Delivery 20k:* Khóa COD, 100% VietQR trước, phí ship 20.000 VNĐ cố định, bắt buộc tên/SĐT/địa chỉ.
     * *Takeaway Web POS:* Bán mang về thao tác trên Web POS quầy, tích 10 ly đổi 1 ly miễn phí chỉ áp dụng Takeaway, thu tiền sau.
     * *Chấm công WiFi:* Xác thực kép BSSID Router + IP Subnet + Mã NV, từ chối 4G/5G.
   - `02_Thiet_Ke_Database.md` ánh xạ trực tiếp và trọn vẹn các yêu cầu này vào cấu trúc schema: `orders.order_type`, `orders.delivery_fee`, `loyalty_cup_transactions`, `branch_wifi_configs`, `recipes_bom`, `shifts`, `attendances`.
3. *Từ kiểm tra 3NF và An toàn dữ liệu:*
   - Thiết kế database tuân thủ chuẩn 3NF: Bảng `recipes_bom` gộp trực tiếp `product_id`, `size_id`, `ingredient_id` kèm unique index, tránh tách bảng thừa thãi.
   - Các bảng trung gian (`user_roles`, `product_modifiers`) có khóa chính kết hợp hợp lệ.
   - Xóa cascade/restrict được phân định chuẩn xác (`ON DELETE RESTRICT` cho master data/finance, `ON DELETE CASCADE` cho sub-items phụ thuộc).
4. *Kết luận chuỗi lập luận:* Sản phẩm bàn giao hoàn toàn hợp lệ, đáng tin cậy và sẵn sàng làm đầu vào cho Milestone M2 (API Contracts & UI/UX Design System).

---

## 3. Adversarial Challenges & Stress Testing (Phản Biện Đối Kháng)

### Challenge 1: Xử lý tranh chấp số dư ly Takeaway (Race condition on 10-Cup Loyalty)
- **Tình huống tấn công:** Khách hàng có 9 ly, đặt cùng lúc 2 đơn Takeaway tại quầy và trực tuyến hoặc 2 thu ngân thao tác đồng thời.
- **Đánh giá phòng thủ:** Bảng `loyalty_cup_transactions` lưu từng giao dịch EARN/REDEEM với FK `customer_id` và `order_id`. Cần đảm bảo ở M3 Backend áp dụng Serializable Transaction / Redis Distributed Lock trên `customer_id` khi tính toán `cup_balance`.
- **Kết luận:** Cấu trúc DB hiện tại đã chuẩn bị đầy đủ trường dữ liệu để tầng Backend thực thi lock an toàn.

### Challenge 2: Nguy cơ gian lận BSSID WiFi bằng Fake MAC
- **Tình huống tấn công:** Nhân viên ở nhà tự phát WiFi có SSID và MAC Address (BSSID) trùng với quán để chấm công.
- **Đánh giá phòng thủ:** Hệ thống thiết kế kiểm thực kép (Dual-Check): vừa kiểm tra BSSID vừa kiểm tra dải IP Subnet nội bộ (`allowed_ip_subnets`). Trường hợp cần thiết, Router Gateway nội bộ cấp IP tĩnh hoặc VPN cục bộ.
- **Kết luận:** Mô hình kép trong `branch_wifi_configs` là tối ưu vượt trội so với GPS 50m và QR 30s.

### Challenge 3: Đơn Delivery bị quá tải hoặc thay đổi địa chỉ
- **Tình huống tấn công:** Khách nhập sai địa chỉ hoặc chi nhánh đang quá tải không thể giao hàng.
- **Đánh giá phòng thủ:** Trong `C-02` và `C-10` đã có Edge Case handling: Chi nhánh tự động đóng nhận đơn Delivery khi quá tải (chuyển cờ branch); trường hợp thanh toán xong nhưng không thể giao, hệ thống chuyển trạng thái `Cancelled` và hoàn tiền tự động qua PayOS.
- **Kết luận:** Thiết kế hoàn chỉnh.

---

## 4. Caveats (Lưu Ý & Ranh Giới)

1. **Phạm vi kiểm thử thực tế của DB:** Đánh giá này xác minh tính toàn vẹn của DDL SQL, Trigger PL/pgSQL và C# EF Core mappings. Việc chạy migration thực tế lên container PostgreSQL sẽ được kiểm chứng tự động tại Milestone M3/M4.
2. **Kích thước dữ liệu ảnh Review:** `customer_reviews.photo_urls` sử dụng kiểu `JSONB` để lưu danh sách URL ảnh (sau khi upload lên Cloudflare R2 / AWS S3), không lưu nhị phân trực tiếp vào database, bảo đảm hiệu năng tối ưu.

---

## 5. Conclusion & Verdict (Kết Luận Nghiệm Thu)

### 🏆 VERDICT: APPROVE (CHẤP THUẬN 100%)

- **Chất lượng nội dung:** Đạt chuẩn kỹ thuật doanh nghiệp (Enterprise Production-Grade).
- **Tính đầy đủ:** 62/62 Features, 25/25 Database Tables, 100% 3NF, 100% DDL/Indexes/Triggers/EF Core.
- **Tính trung thực & liêm chính:** 0% Placeholder, không có facade hay hardcode vi phạm.
- **Khuyến nghị cho Orchestrator:** Cho phép đóng Milestone M1 và chuyển giao sang **Milestone M2 (API Contracts & UI/UX Design System)**.

---

## 6. Verification Method (Phương Pháp Tái Kiểm Chứng)

Để tái kiểm chứng độc lập báo cáo này, chạy các lệnh sau trong môi trường dự án:

```powershell
# 1. Chạy script kiểm tra toàn diện M1
python d:\Idea_DoAn\.agents\teamwork_preview_reviewer_m1_1\verify_m1.py

# 2. Chạy script kiểm tra toàn vẹn Database & Foreign Keys
python d:\Idea_DoAn\.agents\teamwork_preview_reviewer_m1_1\check_db_integrity.py

# 3. Kiểm tra tính hợp lệ của sơ đồ Mermaid
python d:\Idea_DoAn\.agents\teamwork_preview_reviewer_m1_1\check_mermaid.py
```
