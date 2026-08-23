# 🤝 BIÊN BẢN BÀN GIAO ĐẶC TẢ SỰ THẬT (SPECIFICATION MINING HANDOFF)
## Subagent: `spec_miner_doc_truth` (Teamwork Specification Miner)
> **Trạng thái:** HARD HANDOFF (Nhiệm vụ hoàn thành 100%, sẵn sàng bàn giao cho Parent Orchestrator)  
> **Thời điểm:** 2026-08-22T22:30:00+07:00  
> **Workspace:** `d:\Idea_DoAn\.agents\spec_miner_doc_truth\`  
> **Báo cáo toàn văn:** `d:\Idea_DoAn\.agents\spec_miner_doc_truth\report.md`

---

## 1. QUAN SÁT THỰC TẾ (OBSERVATION)

### 1.1 Nguồn dữ liệu đã kiểm toán trực tiếp:
1. **Tập tin Docx Gốc:** `Smart_FB_OS_Revised_4members.docx` (đã trích xuất văn bản đầy đủ vào `d:\Idea_DoAn\temp_revised_content.txt` - 17.587 ký tự, 3 bảng cấu trúc).
2. **Yêu cầu chỉ đạo & Chốt nghiệp vụ:** `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (Phiên làm việc 2026-08-22T15:06:50Z).
3. **Bộ 5 tài liệu đặc tả hiện hữu trong `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:**
   - `Smart_FB_Operating_System.md` (669 dòng, v2.0 baseline)
   - `Actor_Phan_Quyen_Chuc_Nang.md` (310 dòng, RBAC baseline)
   - `Workflow_Quy_Trinh_Nghiep_Vu.md` (547 dòng, 16 quy trình baseline)
   - `Tong_Quan_Kien_Truc_He_Thong.md` (340 dòng, Kiến trúc 4 tầng baseline)
   - `Tom_Tat_1_Trang_Executive_Summary.md` (176 dòng, Tóm tắt 1 trang baseline)

### 1.2 Trích dẫn bằng chứng quan sát từ nguồn sự thật (Verbatim Quotes):
- **Về Nghiệp vụ Dine-In:**
  - *Docx §3.2.c:* "Quy trình gọi món Dine-In không cần trả trước trực tuyến, khách gọi món -> Barista pha chế -> Khách nhận món -> Khách yêu cầu thanh toán (Tiền mặt/VietQR) -> Nhân viên xác nhận."
  - *ORIGINAL_REQUEST.md:* "Dine-In có 2 payment paths: Path A (VietQR pre-pay: quét QR -> trả tiền -> Paid -> Bếp mới nhận đơn); Path B (Cash post-pay: gọi món -> vào bếp ngay -> phục vụ kèm hóa đơn có QR VietQR -> khách trả tiền mặt hoặc quét QR hóa đơn -> NV xác nhận)."
- **Về Nghiệp vụ Delivery:**
  - *ORIGINAL_REQUEST.md:* "Delivery: QR Delivery trên poster/mạng xã hội -> bắt buộc nhập SĐT + Địa chỉ -> cộng phí ship 20k -> 100% VietQR pre-pay (no COD)."
- **Về Nghiệp vụ Takeaway:**
  - *ORIGINAL_REQUEST.md:* "Takeaway: Staff UI trên Web POS -> NV nhập SĐT tra cứu CRM -> post-pay tiền mặt/VietQR -> loyalty rule '10 cups = 1 free cup' STRICTLY áp dụng cho Takeaway only."
- **Về Nghiệp vụ Chấm công:**
  - *ORIGINAL_REQUEST.md:* "Attendance: WiFi-locked check-in (store WiFi BSSID/IP subnet + Staff ID) trên web, no GPS / no 30s QR."
- **Về Admin Full CRUD:**
  - *ORIGINAL_REQUEST.md:* "Admin Full CRUD: Product create/edit/delete/replace, BOM recipes, Combos, image upload, branch price, 86 toggle, categories, seasonal menus with auto schedule."
- **Về Loại bỏ Staff Mobile App & C-23 & C-24:**
  - *ORIGINAL_REQUEST.md:* "Staff Mobile App complete removal -> Web Responsive KDS/Staff portal instead. C-23 (Social food sharing) và C-24 (PWA push promo notifications) MUST BE DELETED ENTIRELY — must NOT appear anywhere, not even in Future Work."
- **Về Phân định AI Modules:**
  - *Docx §3.2.c AI Modules:* AI-1 (RAG Chatbot Gemini Flash) và AI-2 (Combo Apriori) là 2 module chính thức triển khai. AI-3 (Text-to-SQL), AI-4 (Churn), AI-5 (Demand Forecasting) là Future Work.

---

## 2. CHUỖI SUY LUẬN LOGIC (LOGIC CHAIN)

1. **Khớp nối Nghiệp vụ Bán hàng Đa kênh (Multi-Channel Order Fulfillment):**
   - Từ Quan sát 1.2, hệ thống có 3 kênh đặt hàng riêng biệt với các luồng trạng thái (`OrderStatus`) khác nhau:
     - **Dine-In Nhánh A (VietQR):** `Pending Payment (0)` ➔ `Paid (1)` ➔ `Confirmed (2)` ➔ `Preparing (3)` ➔ `Ready (4)` ➔ `Served (5)`. (Bếp chỉ nhận khi đã `Paid`).
     - **Dine-In Nhánh B (Tiền mặt):** `Confirmed (2)` ➔ `Preparing (3)` ➔ `Ready (4)` ➔ `Served (5)` ➔ `Pending Payment (0)` ➔ `Paid (1)`. (Bếp nhận ngay khi bấm đặt, bill in mã QR VietQR phục vụ bàn).
     - **Delivery:** `Pending Payment (0)` ➔ `Paid (1)` ➔ `Confirmed (2)` ➔ `Preparing (3)` ➔ `Ready (4)` ➔ `Delivering (6)` ➔ `Completed (5)`. (Bắt buộc SĐT, Địa chỉ, Phí 20k, 100% VietQR).
     - **Takeaway:** Thu ngân nhập Web POS ➔ KDS nhận ➔ Pha chế ➔ Tra CRM tích lũy 10 ly tặng 1 ➔ Thu tiền mặt/VietQR tại quầy.
2. **Khóa Định Danh & Chống Gian Lận Vận Hành (Anti-Fraud & Attendance):**
   - Thay vì phụ thuộc GPS trong nhà có sai số 15-50m và mã QR 30s gây tắc nghẽn quầy, việc chuyển sang **WiFi-locked Check-in** (kiểm tra BSSID Access Point / IP Subnet của quán kết hợp Mã NV trên Web) vừa bảo đảm nhân viên phải có mặt tại quán, vừa đơn giản hóa kiến trúc và giảm thiểu 100% chi phí phần cứng.
3. **Chuẩn Hóa Giao Diện Đơn Nền Tảng (Web-First Responsive Architecture):**
   - Loại bỏ Native Staff Mobile App giúp nhóm 4 người (2 FE) tập trung 100% nguồn lực hoàn thiện hệ sinh thái Next.js 14 Web Monorepo: PWA Khách hàng (`(customer)`), Web POS Thu ngân & Sơ đồ bàn (`(staff)`), Web KDS Barista (`(kds)`), Web Quản lý Chi nhánh (`(manager)`), Web Quản trị Chủ chuỗi (`(admin)`).
4. **Bảo Tồn & Di Chuyển Tính Năng Kế Thừa (Preservation Rule):**
   - Áp dụng triệt để nguyên tắc: Tất cả các tính năng có trong tài liệu cũ nhưng không xuất hiện trong docx 4 thành viên (như AI-3, AI-4, AI-5, FaceID, AhaMove API...) đều được **bảo lưu toàn vẹn chuyển sang mục Scale Up / Future Work** (có thiết kế sẵn Interface/Extension Points).
   - Ngoại lệ duy nhất: `C-23` và `C-24` bị **xóa bỏ triệt để 100%** không xuất hiện ở bất kỳ đâu.

---

## 3. CÁC ĐIỀU KIỆN LO TRỪ & GIẢ ĐỊNH (CAVEATS)

1. **Giả định về Webhook Thanh toán:** Giả định môi trường triển khai thực tế có kết nối Internet ổn định để nhận Webhook từ cổng thanh toán PayOS/VietQR. Trong trường hợp gián đoạn Internet, hệ thống hỗ trợ cơ chế Polling thủ công từ phía client.
2. **Giả định về BSSID WiFi trên Trình duyệt Web:** Do một số trình duyệt trên di động hạn chế API đọc trực tiếp BSSID phần cứng vì lý do bảo mật quyền riêng tư của W3C, hệ thống hỗ trợ xác thực qua **Dải IP Gateway/Subnet quán** (`client_ip` thuộc subnet của quán) kết hợp mã xác thực phiên hoặc QR Portal nội bộ quán.
3. **Phạm vi Module AI:** AI-1 sử dụng trực tiếp Google Gemini 1.5 Flash SDK với prompt engineering và context injection (RAG), không yêu cầu fine-tuning mô hình riêng trên máy chủ cục bộ trong phạm vi 16 tuần Capstone.

---

## 4. KẾT LUẬN & ĐỀ XUẤT HÀNH ĐỘNG (CONCLUSION)

1. **Đặc tả đã hoàn thiện 100%:** File `d:\Idea_DoAn\.agents\spec_miner_doc_truth\report.md` đã được khởi tạo hoàn chỉnh, bao gồm:
   - Toàn bộ 67 tính năng chuẩn hóa (C-01 đến C-22, S-01 đến S-13, M-01 đến M-12, A-01 đến A-20).
   - Chi tiết sâu sắc 6 nghiệp vụ trọng tâm (Dine-in 2 nhánh, Delivery 20k, Takeaway POS CRM, WiFi attendance, Admin Full CRUD, Xóa Staff App & C-23 & C-24).
   - Phân định rành mạch 5 module AI (2 Active MVP vs 3 Future Work).
   - Ma trận phân định ranh giới phạm vi 16 tuần MVP vs Scale Up.
   - Ma trận 35 kịch bản biên (Edge Cases E-01 đến E-35) với hành vi chuẩn mực.
2. **Hành động đề xuất kế tiếp cho Parent Orchestrator:**
   - Sử dụng dữ liệu từ `report.md` làm Nguồn Sự Thật Duy Nhất (Single Source of Truth) để chỉ đạo cập nhật đồng bộ toàn bộ 5 tệp tài liệu trong thư mục `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`.

---

## 5. PHƯƠNG PHÁP KIỂM CHỨNG ĐỘC LẬP (VERIFICATION METHOD)

Để kiểm chứng tính xác thực và hoàn thiện của bàn giao này, thực hiện các bước sau:
1. **Kiểm tra sự tồn tại và dung lượng file báo cáo:**
   - File: `d:\Idea_DoAn\.agents\spec_miner_doc_truth\report.md` (Dung lượng: ~54 KB, 303 dòng).
2. **Kiểm tra tính toàn vẹn của 6 nghiệp vụ trọng tâm trong `report.md`:**
   - Xem mục 3.1: Dine-In 2 nhánh thanh toán (VietQR pre-pay vs Tiền mặt post-pay kèm bill QR).
   - Xem mục 3.2: Delivery (bắt buộc SĐT + Địa chỉ, phí cố định 20.000đ, 100% VietQR trả trước).
   - Xem mục 3.3: Takeaway (Web POS thu ngân, tích 10 ly tặng 1 ly chỉ áp dụng cho Takeaway).
   - Xem mục 3.4: Chấm công WiFi-locked (BSSID/IP Subnet + Mã NV, bỏ GPS & QR 30s).
   - Xem mục 3.5: Admin Full CRUD (Món ăn, BOM, Combo, Upload ảnh, Giá chi nhánh, Khóa 86, Menu mùa).
   - Xem mục 3.6 & Bảng C-23/C-24: Xác nhận xóa bỏ hoàn toàn Staff Mobile App, C-23 và C-24.
3. **Kiểm tra Ma trận Biên:**
   - Xem mục 6: 35 kịch bản biên từ E-01 đến E-35 được mô tả chi tiết đầu vào và hành vi xử lý.
