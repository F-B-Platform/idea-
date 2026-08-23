# 📋 BÁO CÁO BÀN GIAO KHẢO SÁT & BẢN THIẾT KẾ UAT TEST CASES (HANDOFF REPORT)
## Dự án: Smart F&B Operating System — Master Spec v2.5.0

> **Tệp báo cáo:** `d:\Idea_DoAn\.agents\explorer_survey_uat\handoff.md`  
> **Tệp phân tích chi tiết:** `d:\Idea_DoAn\.agents\explorer_survey_uat\analysis.md`  
> **Subagent:** Explorer (`explorer_survey_uat`)  
> **Parent Orchestrator:** `parent` (`0b2ef8ca-1df6-462d-9760-dfcd010abad2`)  
> **Loại bàn giao:** Hard Handoff (Hoàn tất khảo sát, sẵn sàng triển khai viết mới 100%)

---

## 1. OBSERVATION (QUAN SÁT THỰC TẾ)

Qua việc trực tiếp đọc và phân tích toàn diện 7 tệp tài liệu trong hệ thống bằng các công cụ `view_file` và `grep_search`:

1. **`d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (Dòng 23-37):**
   - Yêu cầu viết lại toàn diện `05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md` theo chuẩn Master Spec v2.5.0.
   - Bắt buộc có Kịch bản Demo 5 phút kết nối liên hoàn (7 scenes/actors) và hơn 35 Test Cases UAT chi tiết (đủ 7 trường tiêu chuẩn) kèm ma trận 10 kịch bản biên (TC-EDGE-01 ~ TC-EDGE-10).
   - Yêu cầu loại bỏ triệt để: Staff Mobile App, GPS 50m, QR xoay 30s, mã tính năng lỗi thời C-23/C-24.

2. **`d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md` (Dòng 106-202):**
   - Xác lập 5 trụ cột nghiệp vụ: (1) Dine-in 2 nhánh (A: PayOS VietQR trước, B: Tiền mặt trả sau -> KDS nhận Confirmed ngay -> In bill có VietQR), (2) QR Delivery (SĐT + Đ/c bắt buộc, phí ship 20k, 100% VietQR trước, khóa COD), (3) Takeaway Staff Web POS (Tra cứu CRM, Tích 10 ly tặng 1 ly, Thu tiền sau), (4) Chấm công WiFi (BSSID/IP vs 4G từ chối), (5) Hợp nhất 100% Web Stack (Xóa Staff Mobile App).
   - Danh mục 62 tính năng cốt lõi phân theo 4 Actors (`C-01` ~ `C-20`, `S-01` ~ `S-13`, `M-01` ~ `M-12`, `A-01` ~ `A-17`).

3. **`d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md` (Dòng 100-1580):**
   - Đặc tả chi tiết 16 Workflows (`WF-00` đến `WF-16`), Máy trạng thái đơn hàng 4 kênh, Ma trận chuyển đổi trạng thái, Ma trận 10 Edge Cases và 4 SignalR Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`).

4. **`d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md` (Dòng 118-300):**
   - Ma trận kiểm thử 3 kênh bán hàng, 10 kịch bản biên kèm Automated C# Test Assertions, SLA hiệu năng (SignalR < 500ms, FCP < 1.2s, VietQR < 1.0s).

5. **`d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md` (Dòng 44-985):**
   - 10 Sequence Diagrams chuẩn hóa chi tiết từng giao thức API, RedLock, Soft Inventory Reservation (TTL 600s), BOM deduction gam/ml, 86-Toggle, Z-Report variance explanation > 50k, và AI-2 Apriori combo approval.

6. **`d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md` (Tệp hiện hữu, 582 dòng):**
   - Phiên bản cũ v2.0.0 chỉ mới mô tả 1 luồng Dine-in Pre-payment, thiếu phân nhánh Nhánh B Tiền mặt trả sau có in bill VietQR; thiếu kịch bản chi tiết của Admin Regional Pricing & Seasonal Menu; thiếu chi tiết về Soft Inventory Reservation và giải trình Z-Report > 50k. Cần được viết lại mới 100% để đạt độ phủ toàn diện và Zero Placeholders.

---

## 2. LOGIC CHAIN (CHUỖI SUY LUẬN LOGIC)

1. **Từ Quan sát 1 & 2:** Master Spec v2.5.0 đã chuẩn hóa 5 trụ cột nghiệp vụ và 62 tính năng. Đặc biệt, Dine-In có 2 nhánh thanh toán song song độc lập (Nhánh A: PayOS VietQR trả trước; Nhánh B: Tiền mặt trả sau bưng kèm Hóa đơn có in VietQR). Do đó, UAT Test Cases bắt buộc phải có `TC-DINE-01A` và `TC-DINE-01B` để xác minh độc lập cả 2 nhánh.
2. **Từ Quan sát 2 & 3:** Chương trình Loyalty tích 10 ly đổi 1 ly miễn phí là chính sách áp dụng **DUY NHẤT cho đơn Takeaway tại quầy**. Đơn Dine-In và Delivery hoàn toàn không được áp dụng. Do đó, cần có test case xác minh tích ly và đổi ly trên POS (`TC-TAKE-01`, `TC-TAKE-02`) và test case ngoại lệ chặn áp dụng sai kênh (`TC-TAKE-04` / `TC-EDGE-08`).
3. **Từ Quan sát 2 & 5:** Chấm công nhân viên dựa trên xác thực 2 lớp: Subnet IP (`192.168.1.0/24`) và BSSID Access Point của chi nhánh, không dùng GPS 50m hay QR 30s. Do đó, cần có test case chấm công thành công đúng WiFi (`TC-ATT-01`) và test case từ chối 100% khi dùng 4G/WiFi ngoài (`TC-ATT-02` / `TC-EDGE-05`).
4. **Từ Quan sát 3, 4 & 5:** Quy trình kết ca đối soát Z-Report yêu cầu nếu chênh lệch két tiền $|variance| > 50.000$ VNĐ thì bắt buộc phải nhập lý do giải trình của thu ngân và mã PIN phê duyệt của quản lý. Do đó, cần test case `TC-SHIFT-02` và `TC-EDGE-06` mô phỏng chính xác trường hợp thừa 70k.
5. **Từ Quan sát 3, 5 & 6:** Kịch bản Demo 5 phút phải là một chuỗi liên hoàn 7 scenes kết nối 7 vai trò/bối cảnh từ lúc mở ca đầu ngày, chấm công WiFi, đặt món 2 nhánh, giao hàng 20k ship, mua mang về đổi 10 ly, KDS trừ kho BOM & 86-toggle, đóng ca Z-report giải trình 70k, đến Admin duyệt AI-2 combo.

---

## 3. CAVEATS (ĐIỀU KHOẢN LOẠI TRỪ & GIẢ ĐỊNH)

- **Không có mã nguồn can thiệp trực tiếp trong lượt này:** Bản khảo sát được thực hiện ở chế độ Read-Only, toàn bộ phân tích được lưu trong `.agents/explorer_survey_uat/analysis.md` và `.agents/explorer_survey_uat/handoff.md`.
- **Giả định hạ tầng tích hợp:** Các dịch vụ bên thứ ba (PayOS VietQR Gateway, Google Gemini 1.5 Flash API, OpenWeatherMap API) được giả định hoạt động bình thường trong điều kiện chuẩn và có cơ chế Mock/Fallback khi kiểm thử ngoại lệ.
- **Không có cảnh báo chưa rõ:** Mọi quy chuẩn kỹ thuật v2.5.0 đã rõ ràng 100% và đóng băng.

---

## 4. CONCLUSION (KẾT LUẬN & ĐỀ XUẤT HÀNH ĐỘNG)

Hệ thống đã có đầy đủ 100% cơ sở dữ liệu và bản thiết kế chi tiết để tiến hành viết lại hoàn toàn tệp `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md` đạt chuẩn v2.5.0 Production-Ready.

**Đề xuất cấu trúc tệp UAT Test Cases mới (v2.5.0):**
1. **Phần I:** Tổng Quan Phạm Vi & Tiêu Chuẩn Nghiệm Thu UAT v2.5.0 (5 Trụ Cột Đột Phá).
2. **Phần II:** Kịch Bản Demo Hội Đồng Bảo Vệ Capstone (5 Phút Liên Hoàn 7 Scenes).
3. **Phần III:** Ma Trận Kiểm Thử Nghiệm Thu Tổng Thể (47 Test Cases / 12 Phân Hệ).
4. **Phần IV:** Bộ Test Cases UAT Chi Tiết (47 Test Cases đầy đủ 7 trường thông tin, Payloads JSON, Mã HTTP, Logic State Machine):
   - 4.1 Phân hệ Xác thực & Phân quyền (Auth & RBAC: `TC-AUTH-01` ~ `TC-AUTH-04`)
   - 4.2 Phân hệ Thực đơn & Tùy biến món (Menu & Modifiers: `TC-MENU-01` ~ `TC-MENU-04`)
   - 4.3 Phân hệ Đặt món Tại bàn Dine-In (Dine-In 2 Flows: `TC-DINE-01A`, `TC-DINE-01B`, `TC-DINE-02` ~ `TC-DINE-04`)
   - 4.4 Phân hệ Đặt hàng Giao tận nơi (QR Delivery: `TC-DEL-01` ~ `TC-DEL-04`)
   - 4.5 Phân hệ Bán hàng Quầy & Tích Ly (Takeaway POS & Loyalty 10 Ly: `TC-TAKE-01` ~ `TC-TAKE-04`)
   - 4.6 Phân hệ Chấm công Khóa mạng WiFi (WiFi-Locked Attendance: `TC-ATT-01` ~ `TC-ATT-04`)
   - 4.7 Phân hệ Điều phối Bếp & BOM Kho (Web KDS & Inventory: `TC-KDS-01` ~ `TC-KDS-04`)
   - 4.8 Phân hệ Quản lý Ca & Đối soát Két tiền (Shift & Z-Report: `TC-SHIFT-01` ~ `TC-SHIFT-03`)
   - 4.9 Phân hệ Đánh giá & Phản hồi (Reviews & Red Alert: `TC-REV-01` ~ `TC-REV-03`)
   - 4.10 Phân hệ Trí tuệ Nhân tạo (AI-1 Chatbot & AI-2 Combo: `TC-AI-01` ~ `TC-AI-03`)
   - 4.11 Phân hệ Quản trị Trung tâm (Admin Operations: `TC-ADM-01` ~ `TC-ADM-03`)
   - 4.12 Ma trận 10 Kịch bản Biên & An ninh Ngoại lệ (Edge Cases: `TC-EDGE-01` ~ `TC-EDGE-10`)
5. **Phần V:** Tiêu Chí Đánh Giá Nghiệm Thu, Bàn Giao & Biên Bản Ký Duyệt.

---

## 5. VERIFICATION METHOD (PHƯƠNG PHÁP KIỂM CHỨNG ĐỘC LẬP)

Để kiểm chứng tính chính xác và độc lập của báo cáo:

1. **Kiểm tra tệp phân tích chi tiết:**
   - Đọc tệp `d:\Idea_DoAn\.agents\explorer_survey_uat\analysis.md`.
2. **Kiểm tra tính nhất quán với Master Spec:**
   - Đối chiếu các mã kịch bản `TC-DINE-01A`, `TC-DINE-01B`, `TC-DEL-01`, `TC-TAKE-01`, `TC-ATT-01`, `TC-KDS-01`, `TC-SHIFT-01`, `TC-ADM-01`, `TC-EDGE-01~10` với `Workflow_Quy_Trinh_Nghiep_Vu.md` và `07_Ke_Hoach_Kiem_Thu.md`.
3. **Điều kiện không hợp lệ (Invalidation Conditions):**
   - Nếu xuất hiện bất kỳ tham chiếu nào về "Staff Mobile App", "GPS 50m", "QR 30s", "C-23/C-24", hoặc chỉ có 1 luồng Dine-in -> Báo cáo bị xem là không đạt chuẩn v2.5.0.
