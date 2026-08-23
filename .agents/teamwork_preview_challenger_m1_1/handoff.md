# 🛡️ BÁO CÁO KIỂM CHỨNG & THÁCH THỨC ĐỘC LẬP (CHALLENGER REPORT)
## Milestone M1: Requirements & Database Architecture
**Người thực hiện:** Challenger 1 (Adversarial Critic & Empirical Verification Specialist)  
**Ngày thực hiện:** 2026-08-23  
**Working Directory:** `d:\Idea_DoAn\.agents\teamwork_preview_challenger_m1_1\`  
**Phạm vi kiểm chứng:**
1. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md`
2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`

**Phán quyết tổng thể (Overall Verdict):** **APPROVE (CHẤP THUẬN 100%)**

---

## 1. Observation (Quan Sát Thực Chứng)

Tất cả các kiểm chứng đều được thực thi tự động qua test harness Python 3.14 trên dữ liệu thực tế của hai tệp bàn giao.

### 1.1 Kiểm chứng 62 Tính Năng Cốt Lõi (`01_Phan_Tich_Yeu_Cau.md`)
- **Tổng số tính năng:** Phát hiện chính xác **62 tính năng** phân bổ trên 4 nhóm Actor:
  - **Customer (20 tính năng):** `C-01` đến `C-20` (Đầy đủ, liên tục, không nhảy số, không thiếu mã).
  - **Staff / Barista (13 tính năng):** `S-01` đến `S-13` (Đầy đủ, liên tục).
  - **Branch Manager (12 tính năng):** `M-01` đến `M-12` (Đầy đủ, liên tục).
  - **Chain Admin (17 tính năng):** `A-01` đến `A-17` (Đầy đủ, liên tục).
  - *Tổng cộng:* $20 + 13 + 12 + 17 = 62$ tính năng.
- **Tính toàn vẹn cấu trúc từng tính năng:** Cả 62 tính năng đều chứa đầy đủ 5 thành phần bắt buộc:
  1. *Mô tả (Description)*
  2. *Quy tắc nghiệp vụ & Ràng buộc (Business Rules & Constraints)*
  3. *Hợp đồng dữ liệu (Input/Output Schema)*
  4. *Kịch bản biên & Xử lý ngoại lệ (Edge Cases & Handling)*
  5. *Tiêu chí nghiệm thu (Acceptance Criteria)*
- **Ma trận truy vết (RTM):** Bảng RTM ở Mục 6 ánh xạ chính xác 62 dòng từ `C-01` ~ `A-17` sang Database Tables (02), API Endpoints (03) và UI Routes (04).

### 1.2 Kiểm chứng 25 Bảng Cơ Sở Dữ Liệu (`02_Thiet_Ke_Database.md`)
- **Số câu lệnh DDL `CREATE TABLE`:** Đạt chính xác **25 câu lệnh**.
- **Danh sách 25 thực thể 3NF hoàn chỉnh:**
  1. `branches`
  2. `branch_wifi_configs`
  3. `tables`
  4. `users`
  5. `roles`
  6. `user_roles`
  7. `audit_logs`
  8. `categories`
  9. `products`
  10. `product_sizes`
  11. `product_branch_prices`
  12. `modifiers`
  13. `product_modifiers`
  14. `ingredients`
  15. `recipes_bom`
  16. `customers`
  17. `orders`
  18. `order_items`
  19. `order_item_modifiers`
  20. `payments`
  21. `loyalty_cup_transactions`
  22. `vouchers`
  23. `customer_reviews`
  24. `shifts`
  25. `attendances`
- **Mermaid ERD:** Sơ đồ `erDiagram` định nghĩa trọn vẹn 25 thực thể và các mối quan hệ `||--o{`, `||--||`.

### 1.3 Kiểm chứng Tính Toàn Vẹn Khóa Ngoại & Tính Phi Chu Trình (DAG Acyclicity)
- **Tổng số lỗi khóa ngoại (Foreign Key Errors):** `0` lỗi. Tất cả các bảng được tham chiếu (`REFERENCES`) đều tồn tại trong schema.
- **Kiểm định sắp xếp Tô-pô (Topological Sort):** Đồ thị phụ thuộc quan hệ là một Đồ thị có hướng phi chu trình (Directed Acyclic Graph - DAG) 100%. Thứ tự khởi tạo cơ sở dữ liệu hợp lệ:
  1. `ingredients`, `branches`, `categories`, `vouchers`, `modifiers`, `customers`, `roles` (Bảng độc lập - In-degree = 0)
  2. `branch_wifi_configs`, `tables`, `users` (Phụ thuộc `branches`)
  3. `products` (Phụ thuộc `categories`)
  4. `orders` (Phụ thuộc `branches`, `tables`, `customers`)
  5. `user_roles`, `audit_logs`, `shifts`, `attendances` (Phụ thuộc `users`, `roles`, `branches`)
  6. `product_sizes`, `product_branch_prices`, `product_modifiers` (Phụ thuộc `products`, `modifiers`, `branches`)
  7. `payments`, `loyalty_cup_transactions`, `customer_reviews` (Phụ thuộc `orders`, `customers`, `products`)
  8. `recipes_bom`, `order_items` (Phụ thuộc `product_sizes`, `ingredients`, `products`, `orders`)
  9. `order_item_modifiers` (Phụ thuộc `order_items`, `modifiers`)

### 1.4 Kiểm tra Các Từ Khóa Bị Cấm & Quy Tắc Zero Placeholder
- **Placeholder (`TODO`, `TBD`, `/* rest of code */`, `// tương tự`):** `0` vi phạm trên cả 2 tệp.
- **Các khái niệm phế truất (`Flutter`, `GPS 50m`, `QR 30s`, `C-23`, `C-24`):**
  - Trong `02_Thiet_Ke_Database.md`: Tuyệt đối không xuất hiện (0 lần).
  - Trong `01_Phan_Tich_Yeu_Cau.md`: Không xuất hiện trong bất kỳ yêu cầu chức năng nào. Các từ khóa chỉ xuất hiện duy nhất trong bảng *"Danh mục các khái niệm cũ đã loại bỏ vĩnh viễn"* (Mục 3) và phần phân tích bối cảnh để giải thích rõ lý do kỹ thuật thay thế bằng Chấm công WiFi, Web Responsive và 62 Core Features.

---

## 2. Logic Chain (Chuỗi Lập Luận Đánh Giá)

1. *Về Tính Đầy Đủ & Nhất Quán Nghiệp Vụ:*
   - Yêu cầu gốc `ORIGINAL_REQUEST.md` và `PROJECT.md` quy định 62 tính năng cốt lõi (20 C, 13 S, 12 M, 17 A). Deliverable `01_Phan_Tich_Yeu_Cau.md` thỏa mãn chính xác 100% số lượng, mã định danh và nội dung chi tiết.
   - 4 Động cơ cốt lõi (Dine-In 2 nhánh, Delivery 20k VietQR, Takeaway POS 10 ly, Chấm công WiFi BSSID/IP) được trình bày xuyên suốt từ sơ đồ Mermaid, đặc tả chi tiết đến bảng RTM.

2. *Về Độ Tin Cậy Của Cơ Sở Dữ Liệu:*
   - Deliverable `02_Thiet_Ke_Database.md` triển khai đúng 25 bảng chuẩn 3NF.
   - Các trường dữ liệu quan trọng như `orders.delivery_address`, `orders.delivery_fee = 20000`, `branch_wifi_configs.bssid_list`, `branch_wifi_configs.allowed_ip_subnets`, `loyalty_cup_transactions.cups_earned/cups_redeemed` đều được định nghĩa chặt chẽ với kiểu dữ liệu tối ưu (`DECIMAL(12,0)` cho tiền VNĐ, `DECIMAL(10,3)` cho định lượng BOM, `UUID` cho ID).
   - Kiểm chứng đồ thị khóa ngoại chứng minh không xảy ra deadlock hay circular foreign key constraint khi sinh migration hoặc seed data.

---

## 3. Caveats (Lưu Ý Kỹ Thuật Cho Các Milestone Tiếp Theo)

1. **Khóa Ngoại Tự Phục Hồi:** Khi sinh migration EF Core trong Milestone M3 (`05_Quy_Trinh_Backend.md`), cần thiết lập `OnDelete(DeleteBehavior.Restrict)` cho các quan hệ cha con nhạy cảm (như `Branch -> Orders`, `Product -> OrderItems`) để đảm bảo không mất dữ liệu kiểm toán khi xóa mềm.
2. **Định dạng Mảng JSONB/Text:** Bảng `branch_wifi_configs` sử dụng kiểu mảng hoặc chuỗi cho `bssid_list` và `allowed_ip_subnets`. Backend cần cấu hình ValueComparer trong EF Core 8 để theo dõi thay đổi chính xác.

---

## 4. Conclusion (Phán Quyết Hoàn Thành)

**Phán quyết:** **APPROVE (CHẤP THUẬN 100%)**

- `01_Phan_Tich_Yeu_Cau.md` đạt chuẩn tài liệu yêu cầu phần mềm kỹ thuật cao (SRS v2.5.0 Production-Ready).
- `02_Thiet_Ke_Database.md` đạt chuẩn kiến trúc cơ sở dữ liệu PostgreSQL 16 3NF, DDL hoàn chỉnh, không chu trình khóa ngoại.
- Cả hai tài liệu sẵn sàng làm nền tảng vững chắc (Source of Truth) cho Milestone M2 (API Contracts & UI/UX Design System).

---

## 5. Verification Method (Phương Pháp Kiểm Chứng Độc Lập)

Bất kỳ reviewer/auditor nào cũng có thể kiểm chứng lại toàn bộ kết quả bằng lệnh Python:

```powershell
# 1. Kiểm tra 62 tính năng
python -c "import re; t=open('d:/Idea_DoAn/03_Quy_Trinh_Trien_Khai/01_Phan_Tich_Yeu_Cau.md',encoding='utf-8').read(); m=re.findall(r'^###\s+([CSMA]-\d{2})', t, re.M); print(len(m), len([x for x in m if 'C-' in x]), len([x for x in m if 'S-' in x]), len([x for x in m if 'M-' in x]), len([x for x in m if 'A-' in x]))"
# Output kỳ vọng: 62 20 13 12 17

# 2. Kiểm tra 25 bảng DDL
python -c "import re; t=open('d:/Idea_DoAn/03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md',encoding='utf-8').read(); print(len(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)', t, re.I)))"
# Output kỳ vọng: 25

# 3. Kiểm tra Zero Placeholders
python -c "import re; t1=open('d:/Idea_DoAn/03_Quy_Trinh_Trien_Khai/01_Phan_Tich_Yeu_Cau.md',encoding='utf-8').read(); t2=open('d:/Idea_DoAn/03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md',encoding='utf-8').read(); print('Placeholders in Doc1:', len(re.findall(r'\b(TODO|TBD)\b', t1))); print('Placeholders in Doc2:', len(re.findall(r'\b(TODO|TBD)\b', t2)))"
# Output kỳ vọng: Placeholders in Doc1: 0, Placeholders in Doc2: 0
```
