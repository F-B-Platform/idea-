# 5-Component Handoff Report: Functional Review of 5 Specification Documents

- **Agent Name:** `reviewer_5docs_functional`
- **Recipient:** `parent` (`2f276ad2-ad97-4bca-96be-6ea74949ded0`)
- **Working Directory:** `d:\Idea_DoAn\.agents\reviewer_5docs_functional\`
- **Review Target:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\` (5 Markdown files)
- **Verdict:** **REQUEST_CHANGES**

---

## 1. Observation (Trực Tiếp Quan Sát Được)

1. **Về 6 quy tắc nghiệp vụ cốt lõi:**
   - **Dine-In 2 nhánh thanh toán:** Cả 5 file (`Smart_FB_Operating_System.md`, `Actor_Phan_Quyen_Chuc_Nang.md`, `Workflow_Quy_Trinh_Nghiep_Vu.md` [WF-01A, WF-01B], `Tong_Quan_Kien_Truc_He_Thong.md`, `Tom_Tat_1_Trang_Executive_Summary.md`) đều đặc tả chính xác:
     - Nhánh A (VietQR trả trước): `PendingPayment` ➔ `Paid` ➔ `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served`. Bếp KDS chỉ nhận đơn khi nhận webhook PayOS báo `Paid`.
     - Nhánh B (Tiền mặt trả sau): `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served` ➔ `PendingPayment` ➔ `Paid`. Đơn vào bếp ngay; khi bấm Ready in bill có sẵn mã VietQR động; nhân viên mang món ra bàn kèm hóa đơn có in QR; khách trả tiền mặt hoặc quét QR trên hóa đơn; nhân viên xác nhận.
   - **QR Delivery:** Quét QR Delivery riêng; bắt buộc `recipient_name`, `recipient_phone`, `delivery_address`; tự động cộng phí ship cố định 20.000 VNĐ (`delivery_fee = 20000`); bắt buộc 100% VietQR trả trước (khóa hoàn toàn COD); KDS hiển thị badge `[DELIVERY]`.
   - **Takeaway:** Thao tác trên Web POS Quầy `(staff)/pos` (không dùng QR); tra cứu CRM SĐT; thanh toán sau khi nhận món; chính sách Loyalty 10 ly = tặng 1 ly miễn phí được nhấn mạnh **CHỈ ÁP DỤNG CHO TAKEAWAY** (không áp dụng Dine-in và Delivery).
   - **Chấm công WiFi:** Bỏ hoàn toàn GPS 50m và QR xoay 30s; xác thực kép qua BSSID / IP Subnet trong `BranchWifiConfigs` + Mã NV (`EmployeeCode`) hợp lệ; nếu sai WiFi từ chối 403 ngay lập tức.
   - **Admin Full CRUD:** Toàn quyền Tạo, Sửa, Xóa mềm, Thay thế món (`Replace Product`), Master BOM recipes, tạo combo & duyệt AI-2 Apriori, upload ảnh WebP, bảng giá vùng chi nhánh, 86-toggle, sắp xếp thứ tự danh mục, lên lịch Seasonal Menu.
   - **Loại bỏ Staff Mobile App:** 100% chuyển sang Web Responsive (`(kds)`, `(staff)`).
   - **AI Phân rã:** 2 Active MVP Modules (AI-1 Gemini RAG & AI-2 Apriori Combo); 3 Future Work Modules (AI-3 Text-to-SQL, AI-4 Churn RFM, AI-5 Demand Forecasting) kèm Extension Points.

2. **Các điểm sai sót trực tiếp phát hiện được:**
   - **Phát hiện 1 (Major):** Tại dòng 11 tệp `Workflow_Quy_Trinh_Nghiep_Vu.md`:
     `> 2. **Đã loại bỏ vĩnh viễn:** C-23 (Chia sẻ món ăn MXH) và C-24 (Push Notification khuyến mãi PWA).`
     Lệnh kiểm thử tự động `Grep "C-23"` trả về 1 kết quả (không đạt yêu cầu kết quả = 0).
   - **Phát hiện 2 (Minor):** Tại dòng 95 tệp `Tom_Tat_1_Trang_Executive_Summary.md`:
     Ghi `- Quy mô bàn giao: **64 Tính năng cốt lõi** phân bổ cho 4 nhóm Actor (22 Khách hàng C-01–C-22, 12 Nhân viên S-01–S-12, 12 Quản lý M-01–M-12, 18 Chủ chuỗi A-01–A-18).`
     Lệch so với 4 file còn lại: Staff là 13 tính năng (`S-01` ~ `S-13`) và Admin là 17 tính năng (`A-01` ~ `A-17`).
   - **Phát hiện 3 (Hygiene):** Thư mục `01_Tai_Lieu_Dac_Ta_Goc\` vẫn tồn tại tệp cũ `Actor_KhachHang_Xem.html` chứa nội dung obsolete.

---

## 2. Logic Chain (Chuỗi Lập Luận Suy Diễn)

1. *Từ Quan sát 1:* Bộ tài liệu đáp ứng hoàn hảo 100% các yêu cầu nghiệp vụ chuyên sâu và các quy tắc thiết kế kiến trúc Clean Architecture, CQRS, SignalR real-time hubs, PostgreSQL 25 entities và Redis caching/locking.
2. *Từ Quan sát 2 (Phát hiện 1):* Yêu cầu acceptance criteria trong `ORIGINAL_REQUEST.md` chỉ định rõ: *"Grep 'C-23' và 'C-24' trong 5 file output → kết quả = 0"*. Dù tác giả tài liệu đã xóa logic C-23/C-24 trong danh mục tính năng, việc để lại tên mã định danh literal tại dòng 11 làm thất bại bài kiểm tra tự động.
3. *Từ Quan sát 2 (Phát hiện 2):* Sự không đồng nhất giữa `Tom_Tat_1_Trang_Executive_Summary.md` (ghi 12 Staff, 18 Admin) và `Smart_FB_Operating_System.md` / `Actor_Phan_Quyen_Chuc_Nang.md` (ghi 13 Staff, 17 Admin) gây ra mâu thuẫn số liệu cần chuẩn hóa.
4. *Tổng hợp:* Vì vậy, phán quyết bắt buộc là **REQUEST_CHANGES** để tác giả cập nhật 2 điểm nhỏ trên trước khi phê duyệt chính thức toàn bộ.

---

## 3. Caveats (Khu Vực Chưa Khảo Sát & Giả Định)

- **Phạm vi xem xét:** Đánh giá chức năng tập trung độc quyền vào 5 file Markdown trong `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`.
- **Giả định:** Cấu trúc 64 tính năng (22 Customer + 13 Staff + 12 Manager + 17 Admin) là cấu trúc chuẩn hóa cuối cùng được quy định tại `Smart_FB_Operating_System.md` và `Actor_Phan_Quyen_Chuc_Nang.md`.

---

## 4. Conclusion (Kết Luận & Yêu Cầu Hành Động)

- **Phán quyết:** **REQUEST_CHANGES**
- **Hành động cần thực hiện:**
  1. Chỉnh sửa dòng 11 file `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md` để loại bỏ chuỗi literal `C-23` và `C-24`.
  2. Chỉnh sửa dòng 95 file `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tom_Tat_1_Trang_Executive_Summary.md` sửa `12 Nhân viên S-01–S-12` thành `13 Nhân viên S-01–S-13` và `18 Chủ chuỗi A-01–A-18` thành `17 Chủ chuỗi A-01–A-17`.
  3. Xóa file rác `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Xem.html`.
- Sau khi thực hiện 2 điểm chỉnh sửa trên, bộ tài liệu sẽ đạt điều kiện **APPROVE 100%**.

---

## 5. Verification Method (Phương Pháp Kiểm Chứng Độc Lập)

Chạy các lệnh grep kiểm tra độc lập trên terminal:
1. `grep_search(SearchPath="d:\\Idea_DoAn\\01_Tai_Lieu_Dac_Ta_Goc", Query="C-23")` ➔ Mục tiêu: 0 matches.
2. `grep_search(SearchPath="d:\\Idea_DoAn\\01_Tai_Lieu_Dac_Ta_Goc", Query="C-24")` ➔ Mục tiêu: 0 matches.
3. `grep_search(SearchPath="d:\\Idea_DoAn\\01_Tai_Lieu_Dac_Ta_Goc", Query="A-18")` ➔ Mục tiêu: 0 matches.
4. Kiểm tra dòng 95 của `Tom_Tat_1_Trang_Executive_Summary.md` khớp chính xác `13 Nhân viên S-01–S-13` và `17 Chủ chuỗi A-01–A-17`.
