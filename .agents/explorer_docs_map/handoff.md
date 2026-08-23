# 📋 BÁO CÁO BÀN GIAO KIỂM TOÁN TÀI LIỆU & BẢN ĐỒ LỆCH NGHIỆP VỤ (HANDOFF REPORT)
## DỰ ÁN: SMART F&B OS DOCUMENTATION OVERHAUL

> **Người thực hiện:** Explorer 2 (`explorer_docs_map`)  
> **Người nhận:** Parent Orchestrator (`10ef5828-46c5-4123-b200-c2d752dd2ea6`)  
> **Tệp kết quả chính:** `d:\Idea_DoAn\.agents\explorer_docs_map\docs_audit_map.md`  
> **Thời gian:** 2026-08-22T21:20:15+07:00  

---

## 1. OBSERVATION (QUAN SÁT THỰC TẾ)

Qua quá trình rà soát toàn diện cấu trúc thư mục `d:\Idea_DoAn\`, chúng tôi đã kiểm tra **31 tệp Markdown** và các tệp phái sinh liên quan:

1. **Thư mục `01_Tai_Lieu_Dac_Ta_Goc/` (5 tệp):**
   - `Actor_KhachHang_Xem.md` (dòng 13, 149): Đề cập `Mobile App nội bộ nhân viên`, `Chấm công GPS & QR` (dòng 148), `Yêu cầu in bill / thanh toán tại bàn` (dòng 85-86).
   - `Actor_Smart_FB_OS.md` & `Actor_Smart_FB_OS_Revised.md`: Đều còn chứa `Staff Mobile App` (F-31), `Chấm công QR 30s + GPS 50m` (F-32), `Yêu cầu bill` (F-30), thiếu nghiệp vụ Delivery và Takeaway NV.
   - `Smart_FB_Operating_System.md` (882 dòng): Mục 3 mô tả luồng trả sau ("BƯỚC 3: YÊU CẦU THANH TOÁN -> NV mang bill ra bàn"), Mục 3.3 mô tả QR Takeaway cũ, Mục 4 mô tả GPS 50m / QR 30s.
   - `Workflow_Smart_FB_OS.md` (595 dòng): `WF-01` là luồng đặt món gửi đơn không thanh toán; `WF-07` là chấm công GPS 50m; thiếu hẳn Workflow cho QR Delivery và Takeaway Counter Web POS.

2. **Thư mục `02_Bao_Gia_Chi_Phi/` (1 tệp):**
   - `BaoGia_KhachHang.md` (dòng 44): Có mục `Bảng QR Takeaway tại quầy (30.000 VNĐ x 3)`; thiếu bảng QR Delivery.

3. **Thư mục `03_Quy_Trinh_Trien_Khai/` (9 tệp):**
   - `01_QUY_TRINH_PHAN_TICH_YEU_CAU.md`: MVP 12 tính năng có `Yêu Cầu Bill & Gọi NV`; thiếu Business Rules cho Delivery, Takeaway, WiFi attendance.
   - `02_QUY_TRINH_THIET_KE_DATABASE.md`: 28 bảng chỉ có danh sách tên, chưa đặc tả các trường `delivery_address`, `delivery_fee`, `OrderType`, WiFi config cho Branch.
   - `03_QUY_TRINH_THIET_KE_API_CONTRACT.md` & `03_..._CHI_TIET.md`: Có endpoint `POST /orders/{id}/request-bill` và SignalR `BillRequested`; endpoint chấm công `POST /attendance/check-in` còn dùng GPS geofence (<50m) và QR xoay 30s; thiếu endpoint Delivery và Takeaway POS chi tiết.
   - `04_QUY_TRINH_THIET_KE_UI_UX.md` & `04_THIET_KE_UI_UX_DESIGN_SYSTEM.md` (1,294 dòng): Toàn bộ Chương 4 (5 màn hình `SCR-STAFF-01` đến `SCR-STAFF-05`) được vẽ riêng cho Staff Mobile App + GPS 50m/QR 30s; Chương 2 PWA thiếu màn hình đặt hàng Delivery.
   - `05_BACKEND.md`, `06_FRONTEND.md`, `07_TESTING.md`: Cần cập nhật Route Groups (loại bỏ `(staff)` di động), SignalR event order payment trigger, và phân định 2 AI core vs 3 scale up.

4. **Thư mục `04_Thiet_Ke_Kien_Truc_Diagrams/` (4 tệp):**
   - `01_KIEN_TRUC_HE_THONG_TONG_QUAN.md`: Sơ đồ 4 tầng có `Staff Mobile App (Phục vụ PWA)`.
   - `02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md`: Sequence 1 gửi đơn sang KDS trước khi thanh toán; Sequence 3 mô tả yêu cầu bill trả sau; thiếu Sequence Delivery, Takeaway POS, WiFi check-in.
   - `03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md`: Thực thể `Order` thiếu trường Delivery, `Branch` thiếu trường WiFi, `Attendance` còn ghi GPS.
   - `04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md`: Cần chuẩn hóa client device labels.

5. **Thư mục `05_Quy_Chuan_&_Test_Cases/` (4 tệp):**
   - `02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md`: Kịch bản demo 5 phút và 15 UAT cases vận hành theo luồng trả sau (Dine-in post-pay); thiếu test cases cho Delivery, Takeaway 10 ly, WiFi attendance.
   - `03_MOCHI_DATA_SEED_DEFINITION.md`: Thiếu Seed Data cho WiFi branch, Delivery QR/Fee, Takeaway 10 ly.

6. **Thư mục trùng lặp & Tệp rác:**
   - `05_Thiet_Ke_Kien_Truc_Diagrams/` là bản sao trùng lặp 100% của `04_Thiet_Ke_Kien_Truc_Diagrams/`.
   - Xuất hiện các tệp tạm: `temp_docx_content.txt`, `temp_revised_content.txt`, `~$ieu_Dang_Ky_Capstone_Smart_FB_OS.docx`.
   - Xuất hiện PDF trùng lặp: `01_.../Tóm Tắt F&B.pdf` trùng `TomTat_HeThong_Smart_FB_OS.pdf`, `02_.../BẢNG BÁO GIÁ...pdf` trùng `BaoGia_KhachHang.pdf`.

---

## 2. LOGIC CHAIN (CHUỖI LẬP LUẬN)

1. **Từ Source of Truth (`Smart_FB_OS_Revised_4members.docx` & `ORIGINAL_REQUEST.md`)**:
   - Hệ thống vận hành trên 5 trụ cột nghiệp vụ mới: Dine-in thanh toán trước, QR Delivery giao hàng tận nơi (phí cố định 20k), Takeaway nhân viên quầy tạo đơn (loyalty 10 ly = 1 ly), Chấm công WiFi-locked, và Bỏ hoàn toàn Staff Mobile App.
   - 2 AI Module nghiên cứu cốt lõi: AI-1 (Recommendation Chatbot RAG) và AI-2 (Combo Apriori/FP-Growth). Ba module còn lại (AI-3 NLQ, AI-4 Churn, AI-5 Menu Intelligence) thuộc diện "Scale Up / Future Work".

2. **So sánh với hiện trạng 31 tệp Markdown**:
   - Hầu hết các tệp cốt lõi (`01_`, `03_`, `04_`, `05_`, `ROADMAP.md`) được soạn thảo từ giai đoạn trước khi chốt 5 thay đổi, do đó mang các khái niệm cũ (Staff App di động, GPS 50m, QR xoay 30s, gọi bill trả sau).
   - Sự bất đồng bộ này tạo ra mâu thuẫn trực tiếp giữa các tầng: ERD không có trường Delivery nhưng API contract có enum; Sequence diagram mô tả gửi đơn vào KDS trước thanh toán nhưng yêu cầu thực tế là trả trước mới vào bếp.

3. **Yêu cầu chuyển dịch (Migration Strategy)**:
   - Thay vì xóa bỏ các tính năng nâng cao không có trong docx, toàn bộ các tính năng đó (AI-3, AI-4, AI-5, máy chấm công sinh trắc học mở rộng) phải được gom vào mục "Scale Up / Future Work".
   - Tất cả 31 tệp Markdown phải được cập nhật đồng bộ, liên kết chặt chẽ theo Ma trận phụ thuộc chéo đã thiết lập trong `docs_audit_map.md`.

---

## 3. CAVEATS (ĐIỀU KHOẢN LOẠI TRỪ & GIẢ ĐỊNH)

- **Quyền hạn Read-only**: Bản thân Explorer không sửa đổi trực tiếp 31 tệp tài liệu nguồn mà xuất toàn bộ phát hiện, chỉ dẫn và bản đồ sửa đổi vào `docs_audit_map.md`.
- **Tệp phái sinh nhị phân / HTML / PDF**: Các tệp HTML/PDF trong `01_` và `02_` là sản phẩm xuất bản từ Markdown. Sau khi sửa Markdown nguồn, các tệp này cần được re-generate hoặc dọn dẹp theo quy trình phát hành.

---

## 4. CONCLUSION (KẾT LUẬN & ĐỀ XUẤT HÀNH ĐỘNG)

1. Đã hoàn thành lập bản đồ kiểm toán toàn bộ 31 tệp Markdown tại `d:\Idea_DoAn\.agents\explorer_docs_map\docs_audit_map.md`.
2. Đã phân loại rõ ràng 4 giai đoạn đại phẫu tài liệu cho đội ngũ Writers.
3. Đề xuất Parent Orchestrator phân công các Writer Agents tiếp nhận theo từng thư mục nghiệp vụ:
   - **Writer 1 (Domain & Business Specs)**: Phụ trách `01_Tai_Lieu_Dac_Ta_Goc/` & `02_Bao_Gia_Chi_Phi/`.
   - **Writer 2 (Architecture & Diagrams)**: Phụ trách `04_Thiet_Ke_Kien_Truc_Diagrams/` & Xóa bỏ thư mục trùng `05_`.
   - **Writer 3 (Implementation Processes)**: Phụ trách `03_Quy_Trinh_Trien_Khai/` (Đặc biệt đại phẫu `04_THIET_KE_UI_UX_DESIGN_SYSTEM.md`).
   - **Writer 4 (QA, Test Cases, Roadmap & Audit)**: Phụ trách `05_Quy_Chuan_&_Test_Cases/`, `ROADMAP.md`, `DOC_AUDIT_REPORT.md` và dọn dẹp tệp rác.

---

## 5. VERIFICATION METHOD (PHƯƠNG PHÁP KIỂM CHỨNG ĐỘC LẬP)

Sau khi hoàn thành đợt viết lại tài liệu, có thể kiểm chứng độc lập tính nhất quán bằng các lệnh grep sau:

1. **Kiểm tra loại bỏ hoàn toàn các khái niệm cũ (Kết quả phải = 0, trừ mục Scale Up):**
   - `grep -inr "Staff Mobile App" d:\Idea_DoAn\`
   - `grep -inr "GPS 50m" d:\Idea_DoAn\`
   - `grep -inr "QR động 30" d:\Idea_DoAn\`
   - `grep -inr "yêu cầu bill" d:\Idea_DoAn\` (trong luồng Dine-in)

2. **Kiểm tra xuất hiện đầy đủ các khái niệm mới (Ít nhất $\ge 5$ tệp):**
   - `grep -inr "delivery_address" d:\Idea_DoAn\`
   - `grep -inr "20.000" d:\Idea_DoAn\` (phí ship)
   - `grep -inr "WiFi" d:\Idea_DoAn\` (chấm công)
   - `grep -inr "10 ly" d:\Idea_DoAn\` (loyalty Takeaway)

3. **Kiểm tra cấu trúc thư mục:**
   - Thư mục `05_Thiet_Ke_Kien_Truc_Diagrams/` không còn tồn tại.
   - Toàn bộ tệp tạm `temp_*.txt`, `~$*` đã được xóa sạch.
