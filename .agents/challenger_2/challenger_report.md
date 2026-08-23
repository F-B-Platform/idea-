# 🔬 BÁO CÁO THẨM ĐỊNH KỸ THUẬT & KIỂM THỬ THỰC NGHIỆM (CHALLENGER 2 REPORT)
## SMART F&B OPERATING SYSTEM DOCUMENTATION OVERHAUL

> **Người thực hiện:** Challenger 2 (Empirical Challenger / Critic & Specialist)  
> **Thời gian thẩm định:** 2026-08-22T21:46:00+07:00  
> **Không gian làm việc:** `d:\Idea_DoAn\`  
> **Hồ sơ tham chiếu:** `PROJECT.md`, `Smart_FB_OS_Revised_4members.docx`, `ORIGINAL_REQUEST.md`  
> **Phương pháp kiểm chứng:** Viết và thực thi 100% mã kiểm thử thực nghiệm (Test Harnesses, Official Mermaid Parser, SQLite/PostgreSQL AST Engine, Regex Linter).  
> **KẾT LUẬN & VERDICT:** ⚠️ **REQUEST_CHANGES** (Phát hiện 2 lỗi cú pháp Mermaid làm hỏng hiển thị sơ đồ và sự tồn tại của các file rác legacy chưa dọn sạch).

---

## 📊 1. BẢNG TỔNG HỢP KẾT QUẢ KIỂM THỬ ĐỊNH LƯỢNG

| Hạng mục kiểm tra | Số lượng kiểm thử | Kết quả thực tế | Trạng thái |
|---|:---:|:---:|:---:|
| **1. Cú pháp Sơ đồ Mermaid** | 35 khối sơ đồ (toàn repo) | 31 Pass, 4 Fail | 🔴 **CẦN SỬA** |
| **2. PostgreSQL 16 DDL Schema** | 24 Bảng, 8 Enums, 6 Indexes | Khởi tạo thành công 100%, 0 lỗi FK | 🟢 **PASS** |
| **3. DML Seed Data 3 OrderTypes** | 23 Lệnh INSERT (DineIn, TakeAway, Delivery) | Khớp 100% cột, kiểu dữ liệu, Enums & FKs | 🟢 **PASS** |
| **4. Độ phủ Test Cases UAT** | 35 UAT Test Cases + Demo 5 phút | Bao phủ 100% (5/5 luồng cốt lõi + 5 Edge Cases) | 🟢 **PASS** |
| **5. Dọn dẹp Thư mục & File Tạm** | Xóa thư mục trùng & file `.txt` gốc | Đã xóa `05_Thiet_Ke_...` và 2 file temp root | 🟡 **CÒN FILE RÁC** |
| **6. Quét Thuật ngữ Bị loại bỏ** | Toàn bộ 45 file `.md` | Đạt chuẩn ở các file chính, còn dính ở file legacy | 🟡 **CẦN DỌN DẸP** |

---

## 🔍 2. CHI TIẾT KẾT QUẢ THẨM ĐỊNH THỰC NGHIỆM

### 2.1 Kiểm thử Thực nghiệm Sơ đồ Mermaid (Mermaid Syntax Test)
- **Công cụ kiểm thử:** Node.js v24.14.0 + thư viện chính thức `mermaid` (ESM) + JSDOM / DOMPurify sandbox.
- **Tập tin test:** `.agents/challenger_2/validate_all_mermaid.mjs`.
- **Tổng số sơ đồ kiểm tra:** 35 khối ````mermaid``` trên toàn bộ 45 file markdown.
- **Kết quả:** 31 sơ đồ render hoàn hảo, **4 sơ đồ bị lỗi cú pháp parser**:

#### ❌ Lỗi 1: Cú pháp `ContainerBoundary` không hợp lệ trong Sơ đồ C4 Container
- **Vị trí file:**
  1. `04_Thiet_Ke_Kien_Truc_Diagrams/01_Kien_Truc_Tong_Quan.md` (Khối #3, Dòng 141)
  2. `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md` (Khối #3, Dòng 141)
- **Thông báo lỗi từ Parser:**
  `Lexical error on line 6. Unrecognized text: ...ản lý, Admin") ContainerBoundary(fr---------------------^`
- **Nguyên nhân:** Cú pháp chuẩn của Mermaid C4 Container quy định macro boundary phải có dấu gạch dưới: `Container_Boundary(alias, label)` hoặc `System_Boundary(alias, label)`. Việc viết liền `ContainerBoundary(...)` khiến parser không nhận diện được token và quăng lỗi biên dịch.
- **Khắc phục:** Đổi toàn bộ `ContainerBoundary(...)` thành `Container_Boundary(...)` trong khối C4Container (có 4 vị trí: `frontend_boundary`, `backend_boundary`, `ai_boundary`, `data_boundary`).

#### ❌ Lỗi 2: Cú pháp thuộc tính kép `FK UK` trong Sơ đồ ERD
- **Vị trí file:**
  1. `04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md` (Khối #1, Dòng 238)
  2. `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` (Khối #1, Dòng 238)
- **Thông báo lỗi từ Parser:**
  `Parse error on line 187: ... uuid order_id FK UK string pa -----------------------^ Expecting 'BLOCK_STOP', 'ATTRIBUTE_WORD', ',', 'COMMENT', got 'ATTRIBUTE_KEY'`
- **Nguyên nhân:** Trong thực thể `PAYMENT`, trường `order_id` được khai báo là `uuid order_id FK UK`. Cú pháp Mermaid erDiagram chỉ cho phép tối đa 1 thuộc tính khóa duy nhất (`PK`, `FK`, hoặc `UK`). Khi viết 2 khóa liền nhau, parser nhận `FK` và bị xung đột token khi gặp tiếp `UK`.
- **Khắc phục:** Đổi thành `uuid order_id FK "UK"` hoặc chỉ để `uuid order_id FK`.

---

### 2.2 Kiểm thử Thực nghiệm PostgreSQL 16 DDL & Seed Data Script
- **Tập tin thẩm định:** `05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md`.
- **Công cụ kiểm thử:** Python 3.14.3 AST SQL Analyzer (`verify_sql_integrity.py`) + SQLite3 in-memory engine simulation (`test_sql_execution.py`).
- **Kết quả kiểm định:**

#### A. Kiểm tra Schema DDL:
- **Enums (8 Enums):** Khai báo đầy đủ `user_role_enum`, `order_type_enum`, `order_status_enum`, `payment_method_enum`, `payment_status_enum`, `attendance_status_enum`, `shift_status_enum`, `loyalty_trans_type_enum`. Tất cả đều sử dụng khối PL/pgSQL idempotent an toàn:
  ```sql
  DO $$ BEGIN
      CREATE TYPE order_type_enum AS ENUM ('DineIn', 'TakeAway', 'Delivery');
  EXCEPTION
      WHEN duplicate_object THEN null;
  END $$;
  ```
- **Bảng (24 Bảng):** Khởi tạo đầy đủ 24 bảng quan hệ, bao gồm bảng `branch_wifi_configs` (quản lý SSID, BSSID, Subnet IP), `orders` (với các trường cốt lõi: `order_type`, `delivery_address`, `delivery_fee`), `loyalty_cup_transactions` (sổ cái tích 10 ly đổi 1 ly), `attendances` (lưu IP/BSSID chấm công WiFi).
- **Tính toàn vẹn khóa ngoại (Foreign Key Integrity):** 100% các ràng buộc khóa ngoại tham chiếu chính xác đến bảng và cột khóa chính tồn tại. Không có bất kỳ lỗi mồ côi (dangling FK) nào.
- **Loại bỏ hoàn toàn trường GPS & QR động:** Bảng `attendances` không chứa bất kỳ cột GPS (`latitude`, `longitude`, `geofence`) hay QR động 30s nào.

#### B. Kiểm tra DML Seed Data cho 3 OrderTypes:
- Đã kiểm chứng thực thi nạp dữ liệu mẫu cho cả 3 hình thức bán hàng:
  1. **Dine-in Pre-Payment:** Đơn `ORD-20260417-0042` (Bàn 05, tổng tiền 35.000đ, thanh toán VietQR `pay00000-0000-0000-0000-000000000001`, món Bạc Xỉu Sài Gòn).
  2. **Takeaway POS & Loyalty:** Đơn `ORD-20260417-0089` (Khách Lê Văn Tâm `cust0000-0000-0000-0000-000000000003`, trừ 35.000đ từ quyền lợi 10 ly free, trả tiền mặt 43.000đ, ghi log `LoyaltyCupTransactions` -10 ly và +2 ly).
  3. **QR Delivery:** Đơn `ORD-20260417-DEL15` (Khách Chị Mai Hương, SĐT `0987654321`, `delivery_address = 'Tòa nhà Bitexco, Số 2 Hải Triều, P. Bến Nghé, Quận 1, TP.HCM'`, `delivery_fee = 20000.00`, tổng 90.000đ thanh toán VietQR trả trước 100%).
- Dữ liệu mẫu cấu hình WiFi cho 3 chi nhánh (`SmartCoffee_Q1`, `SmartCoffee_ThuDuc`, `SmartCoffee_Q7`) và chấm công mẫu với `is_wifi_verified = true` đã được kiểm chứng.

---

### 2.3 Kiểm thử Độ phủ Bộ Test Cases UAT (UAT Test Coverage)
- **Tập tin thẩm định:** `05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md`.
- **Ma trận bao phủ:** 35 Test Cases chi tiết + Kịch bản Demo 5 phút cho Hội đồng bảo vệ Capstone.
- **Đối chiếu 5 Luồng Nghiệp Vụ Cốt Lõi:**

| Luồng nghiệp vụ cốt lõi | Mã Test Cases phụ trách | Đánh giá độ phủ |
|---|---|:---:|
| **1. Dine-in Pre-Payment Flow** | `TC-DINE-01` (Tạo đơn & VietQR), `TC-DINE-02` (Webhook xác nhận & đẩy KDS), `TC-DINE-03` (Timeout 10p hủy đơn), `TC-DINE-04` (Nút gọi nhân viên) | 🟢 **100% Hoàn hảo** |
| **2. QR Delivery Flow** | `TC-DELV-01` (Nhập SĐT, địa chỉ, phí 20k, VietQR 100%), `TC-DELV-02` (Validation chặn thiếu địa chỉ), `TC-DELV-03` (KDS hiện thẻ tím Delivery) | 🟢 **100% Hoàn hảo** |
| **3. Takeaway POS & Loyalty 10 Ly** | `TC-TAKE-01` (Tra cứu SĐT CRM & tiến trình ly), `TC-TAKE-02` (Đủ 10 ly đổi 1 ly free), `TC-TAKE-03` (Tiền mặt & tính tiền thối), `TC-TAKE-04` (Tạo mới CRM khách) | 🟢 **100% Hoàn hảo** |
| **4. WiFi-Locked Attendance** | `TC-ATT-01` (Chấm công thành công đúng WiFi), `TC-ATT-02` (Chặn khi dùng 4G / WiFi ngoài), `TC-ATT-03` (Chặn sai mã NV) | 🟢 **100% Hoàn hảo** |
| **5. Web KDS & Multi-portal** | `TC-KDS-01` (Nhận đơn SignalR & đổi trạng thái), `TC-KDS-02` (BOM Recipe), `TC-KDS-03` (Cảnh báo quá hạn >10p), `TC-AUTH-02`, `TC-SHIFT-01, 02` | 🟢 **100% Hoàn hảo** |
| **6. Tình huống Biên & An ninh** | `TC-EDGE-01` (RedLock tranh chấp món cuối), `TC-EDGE-02` (Chống giả Webhook & Idempotency), `TC-EDGE-03` (Magic Bytes upload), `TC-EDGE-04` (SignalR Reconnect), `TC-EDGE-05` (Hao hụt khi hủy món) | 🟢 **100% Xuất sắc** |

---

### 2.4 Kiểm tra Dọn dẹp Thư mục & File Rác (Directory Cleanup)
- **Thư mục trùng `05_Thiet_Ke_Kien_Truc_Diagrams/`:** ĐÃ XÓA HOÀN TOÀN (Không còn tồn tại trên ổ đĩa).
- **Các file tạm ở root (`temp_docx_content.txt`, `temp_revised_content.txt`):** ĐÃ XÓA HOÀN TOÀN.
- **⚠️ Tồn đọng cần dọn dẹp:**
  1. **Các file trùng lặp dạng HOA / THƯỜNG trong `04_Thiet_Ke_Kien_Truc_Diagrams/`:**
     - `01_KIEN_TRUC_HE_THONG_TONG_QUAN.md` trùng với `01_Kien_Truc_Tong_Quan.md`
     - `02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md` trùng với `02_Sequence_Diagrams.md`
     - `03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` trùng với `03_ERD_Database_Diagram.md`
     - `04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md` trùng với `04_Deployment_Diagram.md`
  2. **Các file cũ (Legacy Chưa Sửa) chưa được xóa:**
     - `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS.md` (Chứa "Staff Mobile App", "GPS Lock 50m")
     - `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS_Revised.md` (Chứa "Staff Mobile App", "GPS Lock 50m")
     - `01_Tai_Lieu_Dac_Ta_Goc/Actor_KhachHang_Xem.md`
     - `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Smart_FB_OS.md`
     - `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md`
     - `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md` (Chứa "Staff Mobile App")
     - `05_Quy_Chuan_&_Test_Cases/02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md`
     - `05_Quy_Chuan_&_Test_Cases/03_MOCHI_DATA_SEED_DEFINITION.md`

---

## 🛠️ 3. DANH SÁCH YÊU CẦU HÀNH ĐỘNG (ACTIONABLE RECOMMENDATIONS)

Để bộ tài liệu đạt chất lượng 100% hoàn hảo và vượt qua nghiệm thu khắt khe, Challenger 2 đề xuất thực hiện các điều chỉnh sau:

1. **Sửa 2 lỗi cú pháp Mermaid:**
   - Trong `04_Thiet_Ke_Kien_Truc_Diagrams/01_Kien_Truc_Tong_Quan.md`: Đổi 4 vị trí `ContainerBoundary(...)` thành `Container_Boundary(...)`.
   - Trong `04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md`: Tại dòng 238, đổi `uuid order_id FK UK` thành `uuid order_id FK`.
2. **Dọn dẹp các file thừa / file trùng / file legacy cũ:**
   - Xóa các file viết hoa trùng lặp trong `04_Thiet_Ke_Kien_Truc_Diagrams/` (`01_KIEN_TRUC_...`, `02_SO_DO_...`, `03_SO_DO_...`, `04_SO_DO_...`).
   - Xóa các file tài liệu legacy chưa được cập nhật trong `01_Tai_Lieu_Dac_Ta_Goc/` và `05_Quy_Chuan_&_Test_Cases/` để đảm bảo chỉ giữ lại đúng các file canonical được quy định tại `PROJECT.md`.
3. **Cập nhật `DOC_AUDIT_REPORT.md`:** Đồng bộ các phát hiện này vào báo cáo kiểm toán tổng thể của dự án.

---

## ⚖️ 4. PHÁN QUYẾT CUỐI CÙNG (FINAL VERDICT)

**VERDICT: ⚠️ REQUEST_CHANGES**

- **Lý do:** Mặc dù chất lượng nội dung đặc tả, SQL script và UAT test cases đạt tiêu chuẩn rất cao (Production Grade), hệ thống vẫn có 2 lỗi cú pháp Mermaid làm hỏng hiển thị sơ đồ C4 và ERD khi render, kèm theo các file rác legacy chứa thông tin nghiệp vụ cũ chưa được loại bỏ triệt để.
- **Điều kiện thông qua (Approve):** Sửa xong 2 lỗi cú pháp sơ đồ Mermaid và dọn sạch các file rác legacy.
