# 📋 BÁO CÁO PHÂN TÍCH LỖ HỔNG & BLUEPRINT TÁI THIẾT 5 TÀI LIỆU ĐẶC TẢ GỐC
## DỰ ÁN: SMART F&B OPERATING SYSTEM (SMART F&B OS)
> **Thư mục mục tiêu:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`  
> **Tác giả:** Explorer Subagent (`explorer_5docs_diff`)  
> **Thời điểm lập báo cáo:** 2026-08-22  
> **Nguồn sự thật:** `Smart_FB_OS_Revised_4members.docx` (và `ORIGINAL_REQUEST.md`)  
> **Trạng thái:** Hoàn tất khảo sát 100% — Sẵn sàng bàn giao cho Worker Agents

---

# 1. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

Đợt kiểm toán toàn diện trên 5 file tài liệu đặc tả gốc tại thư mục `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc/`:
1. `Smart_FB_Operating_System.md` (Đặc tả tổng thể)
2. `Actor_Phan_Quyen_Chuc_Nang.md` (Actor & RBAC)
3. `Workflow_Quy_Trinh_Nghiep_Vu.md` (16 Workflows)
4. `Tong_Quan_Kien_Truc_He_Thong.md` (Kiến trúc hệ thống)
5. `Tom_Tat_1_Trang_Executive_Summary.md` (Tóm tắt 1 trang)

### Kết quả thẩm định cốt lõi:
- **Tình trạng chung:** Bộ tài liệu đã chuyển đổi phần lớn cấu trúc sang mô hình Web First và Clean Architecture, nhưng **vẫn tồn tại 4 sai lệch nghiệp vụ nghiêm trọng** và **2 tính năng cấm chưa được xóa triệt để**.
- **Sai lệch 1 (🔴 Nghiêm trọng):** Luồng Dine-In (Tại bàn) hiện tại đang bị ghi nhận đơn tuyến chỉ có *100% VietQR trả trước*, bỏ sót hoàn toàn **Nhánh B: Tiền mặt trả sau** (Đơn vào bếp ngay với trạng thái `Confirmed`, nhân viên phục vụ kèm hóa đơn in mã VietQR, khách thanh toán tiền mặt hoặc quét VietQR trên bill).
- **Sai lệch 2 (🔴 Nghiêm trọng):** Chương trình Loyalty "Tích 10 ly tặng 1 ly" tại một số vị trí (WF-14, Presentation Tier, Customer Feature list) đang bị mô tả áp dụng cho mọi loại đơn hàng (Dine-in, Takeaway, Delivery), vi phạm quy tắc thép: **Loyalty 10 ly = 1 ly CHỈ ÁP DỤNG DUY NHẤT CHO ĐƠN TAKEAWAY**.
- **Sai lệch 3 (🔴 Vi phạm yêu cầu xóa bỏ):** Tính năng `C-23` (Chia sẻ món ăn MXH) và `C-24` (Push Notification khuyến mãi PWA) vẫn còn xuất hiện trong `Smart_FB_Operating_System.md` và `Actor_Phan_Quyen_Chuc_Nang.md`, khiến tổng số tính năng bị tính sai thành 66 (chuẩn phải là **64 tính năng core**).
- **Sai lệch 4 (🟡 Cần bổ sung):** Quyền hạn Admin Full CRUD đối với Menu/Sản phẩm (Tạo, Sửa, Xóa, Thay thế món, Tạo combo, Upload ảnh, Giá chi nhánh, Menu mùa & lên lịch) chưa được diễn giải chi tiết và đầy đủ trong các workflow và ma trận RBAC.

---

# 2. MA TRẬN ĐỐI CHIẾU 6 QUY TẮC NGHIỆP VỤ THÉP (GAP ANALYSIS MATRIX)

| STT | Quy Tắc Nghiệp Vụ Nghiêm Ngặt | Trạng Thái Trong 5 Files Hiện Tại | Vị Trí Phát Hiện Sai Lệch & Chi Tiết Lỗ Hổng | Đánh Giá & Hướng Khắc Phục |
|:---:|---|:---:|---|---|
| **1** | **Dine-In 2 Phương Thức Thanh Toán:**<br>• *Path A (VietQR Pre-pay):* `Pending Payment` ➔ `Paid` ➔ `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served`<br>• *Path B (Cash Post-pay):* `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served` ➔ `Pending Payment` ➔ `Paid` (Kèm hóa đơn in mã VietQR) | ❌ **Chưa đạt** (Thiếu Path B) | • `Smart_FB_Operating_System.md`: Dòng 121-127, 247, 310 chỉ nhắc VietQR trả trước.<br>• `Actor_Phan_Quyen_Chuc_Nang.md`: Dòng 63 (Sơ đồ), 115 (`C-06`) chỉ có VietQR trả trước.<br>• `Workflow_Quy_Trinh_Nghiep_Vu.md`: Dòng 15, 55-70 (`WF-01`) chỉ mô tả 1 luồng trả trước.<br>• `Tong_Quan_Kien_Truc_He_Thong.md`: Dòng 173-176 chỉ có pre-payment engine.<br>• `Tom_Tat_1_Trang_Executive_Summary.md`: Dòng 15, 33 chỉ nhắc trả trước. | **Bắt buộc viết lại toàn bộ:** Bổ sung song song 2 nhánh thanh toán cho Dine-in, ghi rõ trạng thái chuyển giao của từng nhánh, làm rõ thao tác nhân viên mang đồ uống kèm hóa đơn in mã VietQR cho nhánh tiền mặt. |
| **2** | **QR Delivery (Đặt hàng tận nơi):**<br>• QR riêng (poster, fanpage)<br>• Bắt buộc SĐT + Địa chỉ (`delivery_address`)<br>• Phí ship cố định 20.000 VNĐ (`delivery_fee`)<br>• 100% VietQR trả trước (Không COD)<br>• Enum `OrderType`: `DineIn`, `TakeAway`, `Delivery` | ✅ **Đạt cơ bản** (Cần chuẩn hóa thuộc tính ERD) | • Đã có trong cả 5 files (`C-07`, `WF-15`, Section 2.2).<br>• Cần đồng bộ chính xác tên trường dữ liệu `delivery_address`, `delivery_fee` (20000) và `order_type` enum trong toàn bộ tài liệu kiến trúc. | **Duy trì & làm sắc nét:** Đảm bảo tất cả 5 file đều nhấn mạnh 100% VietQR, 0% COD, phí ship 20k cố định. |
| **3** | **Takeaway (Bán mang đi tại quầy):**<br>• Giao diện Web Staff POS (Không QR cho khách)<br>• Tra cứu CRM bằng SĐT (Tạo mới hoặc xem số ly)<br>• Thanh toán SAU khi nhận món (Tiền mặt/VietQR)<br>• **Loyalty 10 ly = 1 ly: CHỈ áp dụng Takeaway** | ⚠️ **Vi phạm phạm vi Loyalty** | • `Workflow_Quy_Trinh_Nghiep_Vu.md` dòng 290 (`WF-14`) ghi sai: *"áp dụng cho Dine-in, Takeaway, hoặc Delivery"*.<br>• `Smart_FB_Operating_System.md` dòng 315 liệt kê `C-11` trên PWA mà không ghi chú Takeaway-only.<br>• `Actor_Phan_Quyen_Chuc_Nang.md` dòng 120 (`C-11`) chưa ghi rõ ràng. | **Sửa triệt để:** Khẳng định ở MỌI nơi: Tích lũy và đổi thưởng 10 ly = 1 ly CHỈ áp dụng cho đơn Takeaway tại quầy POS. Đơn Dine-in và Delivery hoàn toàn không tích/đổi ly. |
| **4** | **Chấm Công Khóa Mạng WiFi (WiFi-Locked):**<br>• Kết nối WiFi quán (SSID/BSSID/IP Gateway)<br>• Quét QR tĩnh + Nhập Mã NV (Staff ID)<br>• Dual Check (Mạng + Hồ sơ ca)<br>• **XÓA HOÀN TOÀN GPS 50m & QR động 30s** | ✅ **Đạt tốt** | • Đã thể hiện tốt trong cả 5 files (`S-12`, `M-09`, `WF-07`, Section 2.4).<br>• Đã loại bỏ GPS và QR 30s trong nội dung vận hành. | **Duy trì:** Giữ vững mô hình xác thực kép WiFi SSID/BSSID + Mã NV, kiểm tra cấu hình `branch_wifi_configs`. |
| **5** | **Admin Toàn Quyền Quản Trị (Full CRUD):**<br>• CRUD sản phẩm: Tạo, Sửa, Xóa, Thay thế món<br>• Quản lý Combo (Tạo thủ công + Duyệt AI)<br>• Upload hình ảnh món/danh mục<br>• Giá bán theo chi nhánh (Price override/groups)<br>• Khóa hết món (86 Toggle)<br>• Quản lý danh mục & Thứ tự hiển thị<br>• Menu mùa (Seasonal Menu) & Lên lịch ẩn/hiện | ⚠️ **Cần làm phong phú & chi tiết** | • Các file hiện tại đã có `A-02`, `A-03`, `A-06`, `WF-12` nhưng mô tả còn ngắn gọn, chưa nhấn mạnh rõ quyền Thay thế món, Menu mùa theo lịch, Upload ảnh CDN và Quản lý thứ tự hiển thị. | **Mở rộng đặc tả:** Bổ sung đầy đủ 7 phân hệ CRUD của Admin trong `Smart_FB_Operating_System.md`, `Actor_Phan_Quyen_Chuc_Nang.md` và `Workflow_Quy_Trinh_Nghiep_Vu.md`. |
| **6** | **Loại Bỏ Tuyệt Đối & Phân Vùng Future Work:**<br>• **Staff Mobile App:** XÓA HOÀN TOÀN (Dùng Web)<br>• **C-23 (Chia sẻ MXH):** XÓA 100% (0 mentions)<br>• **C-24 (PWA Push Khuyến mãi):** XÓA 100% (0 mentions)<br>• Tính năng ngoài docx ➔ Chuyển vào Scale Up | ❌ **Còn sót C-23 & C-24** | • `Smart_FB_Operating_System.md`: Dòng 327 (`C-23`), dòng 328 (`C-24`). Tổng tính năng ghi 66.<br>• `Actor_Phan_Quyen_Chuc_Nang.md`: Dòng 132 (`C-23`), dòng 133 (`C-24`). Tổng tính năng ghi 66. | **Xóa vĩnh viễn:** Xóa bỏ hoàn toàn mã `C-23` và `C-24` khỏi danh mục tính năng và bảng RBAC. Điều chỉnh tổng số tính năng Customer từ 24 xuống **22 tính năng**, tổng toàn hệ thống từ 66 xuống **64 tính năng core**. |

---

# 3. CHI TIẾT LỖ HỔNG TỪNG FILE (DEEP-DIVE FILE-BY-FILE GAP AUDIT)

## 3.1 File 1: `Smart_FB_Operating_System.md`
- **Dòng 111 & 121–127 (Section 2.1):** Trụ cột 1 khẳng định *"DINE-IN PRE-PAYMENT: Bắt buộc thanh toán VietQR TRƯỚC -> Bếp mới nhận đơn"*.  
  *Nguyên nhân & Hậu quả:* Bỏ sót hoàn toàn lựa chọn trả tiền mặt của khách ngồi tại bàn. Cần viết lại thành: **ĐẶT MÓN TẠI BÀN (DINE-IN) VỚI 2 PHƯƠNG THỨC THANH TOÁN (VIETQR TRẢ TRƯỚC HOẶC TIỀN MẶT TRẢ SAU)**.
- **Dòng 247 (Bảng so sánh đối thủ):** Cột Smart F&B OS ghi *"100% Pre-payment Gate"*.  
  *Sửa đổi:* Sửa thành *"Linh hoạt 2 phương thức: VietQR trả trước HOẶC Tiền mặt trả sau kèm hóa đơn in QR"*.
- **Dòng 287–300 (Phần VII - Tổng quan tính năng):** Ghi tổng số 66 tính năng (Customer: 24).  
  *Sửa đổi:* Cập nhật thành **64 tính năng cốt lõi** (Customer: **22 tính năng**, Staff: 12, Manager: 12, Admin: 18).
- **Dòng 310 (`C-06`):** Mô tả *"Thanh toán VietQR trả trước (Pre-payment Gate)"*.  
  *Sửa đổi:* Cập nhật thành *"Lựa chọn phương thức thanh toán: Nhánh A (VietQR trả trước) hoặc Nhánh B (Tiền mặt trả sau kèm bill có QR)"*.
- **Dòng 315 (`C-11`):** Liệt kê tích 10 ly chung chung trên PWA.  
  *Sửa đổi:* Làm rõ: Xem thông tin tích lũy CRM, nhưng tích lũy và đổi ly miễn phí chỉ phát sinh khi mua Takeaway tại quầy.
- **Dòng 327–328 (`C-23`, `C-24`):** Còn tồn tại 2 dòng định nghĩa `C-23` và `C-24`.  
  *Sửa đổi:* **XÓA BỎ HOÀN TOÀN**. Không để lại bất kỳ dấu vết nào.
- **Dòng 358–377 (Admin Features):** Cần làm nổi bật rõ Admin Full CRUD: Sản phẩm (Tạo/Sửa/Xóa/Thay thế), Combo, Upload ảnh, Giá chi nhánh, Menu mùa.

## 3.2 File 2: `Actor_Phan_Quyen_Chuc_Nang.md`
- **Dòng 63–65 (Mermaid Diagram):** Luồng khách hàng vẽ `C2 -->|Bắt buộc| C4[Thanh toán VietQR Trả Trước] --> C5[Paid] --> Bếp`.  
  *Sửa đổi:* Phân tách thành 2 nhánh:
  - Nhánh 1: Khách chọn VietQR ➔ Trả trước ➔ `Paid` ➔ Bếp nhận đơn.
  - Nhánh 2: Khách chọn Tiền mặt ➔ Đơn vào bếp ngay (`Confirmed`) ➔ Bếp pha chế ➔ NV mang món kèm Bill có VietQR ➔ Khách trả mặt hoặc quét QR ➔ NV xác nhận `Paid`.
- **Dòng 106 & 108–134 (Bảng tính năng Customer):** Đang có 24 dòng từ `C-01` đến `C-24`.  
  *Sửa đổi:* Xóa dòng `C-23` và `C-24`. Bảng chỉ còn 22 dòng (`C-01` đến `C-22`). Cập nhật `C-06` phản ánh 2 nhánh thanh toán Dine-in.
- **Dòng 120 (`C-11`):** Cần ghi chú rõ điều kiện: Chương trình 10 ly tặng 1 ly chỉ áp dụng cho đơn Takeaway.
- **Dòng 197 (`A-02`):** Mở rộng mô tả: Toàn quyền CRUD (Tạo, Sửa, Xóa, Thay thế sản phẩm), Quản lý danh mục, Thứ tự hiển thị, Upload ảnh sản phẩm lên CDN, và Lên lịch thực đơn mùa.
- **Dòng 229–262 (Ma trận RBAC):** Cập nhật Endpoint `/api/v1/orders/*` để phân định quyền tạo đơn Dine-in nhánh tiền mặt và nhánh VietQR.

## 3.3 File 3: `Workflow_Quy_Trinh_Nghiep_Vu.md`
- **Dòng 15 & 55–70 (`WF-01`):** Tiêu đề đang là *"WF-01: ĐẶT MÓN TẠI BÀN (DINE-IN) — VIETQR TRẢ TRƯỚC BẮT BUỘC"*.  
  *Sửa đổi:* Đổi tên thành **WF-01: ĐẶT MÓN TẠI BÀN (DINE-IN) — 2 PHƯƠNG THỨC THANH TOÁN (VIETQR TRẢ TRƯỚC / TIỀN MẶT TRẢ SAU KÈM HÓA ĐƠN QR)**.
  Xây dựng 2 sơ đồ khối và 2 quy trình chi tiết (Nhánh A: VietQR trả trước và Nhánh B: Tiền mặt trả sau).
- **Dòng 250–263 (`WF-12`):** Quản lý Menu tập trung cần mở rộng chi tiết các bước: Tạo món mới, Thay thế món cũ (Replace Product), Upload hình ảnh, Cấu hình danh mục và Lên lịch menu mùa.
- **Dòng 281–296 (`WF-14`):** Dòng 290 ghi sai nghiêm trọng: *"Mỗi khi khách hàng hoàn tất một đơn hàng hợp lệ (Dine-in, Takeaway, hoặc Delivery)..."*.  
  *Sửa đổi:* Sửa thành: *"Mỗi khi khách hàng mua đơn hàng Mang Về (Takeaway) tại quầy có cung cấp Số điện thoại CRM, hệ thống mới ghi nhận cộng dồn số ly vào `CupBalance`. Đơn Dine-in và Delivery không áp dụng chương trình này."*
- **Dòng 316–333 (`WF-16`):** Làm rõ quy trình Takeaway POS: Tra cứu SĐT ➔ Hiển thị số ly x/10 ➔ Áp dụng ly miễn phí nếu đủ 10 ly ➔ Bếp làm ➔ Giao món ➔ Thu tiền mặt (tính tiền thừa) hoặc VietQR quầy.

## 3.4 File 4: `Tong_Quan_Kien_Truc_He_Thong.md`
- **Dòng 47 (Presentation Tier):** Ghi `(customer): ... Tích 10 Ly ...`. Cần làm rõ là hiển thị hồ sơ CRM/Voucher, còn tích điểm 10 ly diễn ra ở Takeaway POS.
- **Dòng 173–176 (Section 7.1):** Chỉ có "Dine-in Pre-payment Engine".  
  *Sửa đổi:* Cập nhật thành **Dine-In Dual-Payment Engine** với 2 State Machines song song:
  - VietQR Path: `PendingPayment` ➔ `Paid` ➔ `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served`
  - Cash Path: `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served` ➔ `PendingPayment` ➔ `Paid`
- **Dòng 153–159 (PostgreSQL Entities):** Khẳng định danh sách 25 thực thể chuẩn hóa, trong đó bảng `orders` chứa `order_type` enum (`DineIn`, `TakeAway`, `Delivery`), `delivery_address`, `delivery_fee`, và bảng `branch_wifi_configs` chứa thông tin mạng WiFi.

## 3.5 File 5: `Tom_Tat_1_Trang_Executive_Summary.md`
- **Dòng 15 & 33 (Trụ cột 1):** Cập nhật nội dung Trụ cột 1: Đặt món tại bàn với 2 phương thức thanh toán (VietQR trả trước hoặc Tiền mặt trả sau kèm bill in VietQR).
- **Dòng 17 & 35 (Trụ cột 3):** Nhấn mạnh: Takeaway POS với chương trình tích 10 ly tặng 1 ly (CHỈ áp dụng đơn Takeaway).
- **Dòng 23–24 & 45–48:** Duy trì các chỉ số kinh tế ROI và kế hoạch thực thi 16 tuần / 4 thành viên.

---

# 4. BLUEPRINT TÁI THIẾT CHI TIẾT CHO TỪNG FILE (REWRITING BLUEPRINTS)

Dưới đây là thiết kế chi tiết cấu trúc, phân mục và nội dung bắt buộc cho từng file để các Worker Agents triển khai viết lại 100% đầy đủ, không placeholder.

---

## 📐 BLUEPRINT FILE 1: `Smart_FB_Operating_System.md`

### 1. Cấu trúc chương mục chuẩn hóa:
- **Tiêu đề & Metadata:** Phiên bản v2.0.0, Source of Truth `Smart_FB_OS_Revised_4members.docx`, 4 thành viên Capstone, 16 tuần, Tech Stack chuẩn.
- **PHẦN 0: 8 Bất Cập Thực Tế Của Quán Cà Phê Hiện Nay & Giải Pháp:**
  - 0.1: Máy POS lỗi thời & xếp hàng nghẽn quầy ➔ QR Self-Order & Web Staff.
  - 0.2: Chấm công gian lận ➔ Chấm công khóa mạng WiFi chi nhánh (SSID/BSSID + Mã NV).
  - 0.3: Thất thoát nguyên liệu ➔ Trừ tồn kho tự động theo định mức BOM trên KDS.
  - 0.4: Tài chính rời rạc & mù mờ P&L ➔ VietQR tự động + Quản lý mở/kết ca đếm két tiền + Báo cáo P&L tự động.
  - 0.5: Lệch vị pha chế & thiếu feedback ➔ KDS hiển thị công thức BOM chuẩn + QR Feedback 1-5 sao có tải ảnh & alert <= 2 sao.
  - 0.6: 80% khách vãng lai không có data ➔ CRM qua SĐT + Loyalty Takeaway 10 ly = 1 ly.
  - 0.7: Báo cáo EOD thủ công tốn 30-60p ➔ Tự động khóa sổ và tổng hợp doanh thu theo kênh (Dine-in, Takeaway, Delivery).
  - 0.8: Ra quyết định cảm tính ➔ AI-2 Combo Discovery (Apriori/FP-Growth) khai phá giỏ hàng.
- **PHẦN I: Tổng Quan Dự Án & Phạm Vi Vận Hành:** Đồ án Capstone 16 tuần, 4 thành viên (2 BE + 2 FE).
- **PHẦN II: 5 Trụ Cột Nghiệp Vụ Cốt Lõi:**
  - 2.1: Đặt món tại bàn (Dine-in) — 2 phương thức: Nhánh A VietQR trả trước (bếp nhận khi Paid) & Nhánh B Tiền mặt trả sau (bếp nhận ngay Confirmed, mang món kèm bill có VietQR, thu tiền mặt hoặc quét QR).
  - 2.2: Đặt hàng giao tận nơi (QR Delivery) — QR riêng, form bắt buộc SĐT + Địa chỉ (`delivery_address`), phí ship cố định 20.000 VNĐ (`delivery_fee = 20000`), 100% VietQR trả trước.
  - 2.3: Bán hàng mang đi tại quầy (Takeaway Staff POS) — Giao diện Web Staff POS (không QR khách), tra cứu SĐT CRM, chương trình 10 ly tặng 1 ly (CHỈ áp dụng Takeaway), thanh toán sau (Tiền mặt / VietQR).
  - 2.4: Chấm công khóa mạng WiFi (WiFi-locked Attendance) — Xác thực kép WiFi chi nhánh (SSID/BSSID/IP) + Mã NV. Xóa 100% GPS và QR 30s.
  - 2.5: Hợp nhất toàn bộ vận hành trên nền tảng Web Responsive — Xóa 100% Staff Mobile App; 3 Web Portals (KDS, Staff POS, Manager/Admin).
- **PHẦN III: Phân Rã & Định Hình Các Module Trí Tuệ Nhân Tạo (AI Modules):**
  - 3.1 Active MVP (2 Modules): AI-1 Chatbot RAG Gemini Flash (Tư vấn cá nhân hóa theo thời tiết/dị ứng/calo, đo bằng Precision@K, NDCG@K, Latency <= 1.5s); AI-2 Combo Discovery Engine (Apriori/FP-Growth, Support/Confidence/Lift, Human-in-the-loop chủ chuỗi duyệt).
  - 3.2 Scale Up / Future Work (3 Modules): AI-3 NLQ Text-to-SQL; AI-4 Churn Prediction RFM; AI-5 Demand Forecasting.
- **PHẦN IV: Giá Trị Kinh Tế, Bài Toán Hiệu Quả & Phân Tích ROI:** Bảng so sánh tiết kiệm chi phí POS, nhân sự, thất thoát và tăng thu từ Combo (15 - 22 triệu VNĐ/tháng/quán).
- **PHẦN V: Điểm Độc Đáo Khác Biệt & Bảng So Sánh Đối Thủ (iPOS, KiotViet, CukCuk, Smart F&B OS).**
- **PHẦN VI: Kiến Trúc Hệ Thống, Công Nghệ & Luồng Dữ Liệu Thời Gian Thực.**
- **PHẦN VII: Danh Mục 64 Tính Năng Cốt Lõi Phân Theo 4 Nhóm Actor:**
  - 7.1: Khách hàng (Customer) — **22 Tính năng** (`C-01` đến `C-22`). TUYỆT ĐỐI KHÔNG CÓ `C-23` và `C-24`.
  - 7.2: Nhân viên / Pha chế (Staff / Barista) — **12 Tính năng** (`S-01` đến `S-12`).
  - 7.3: Quản lý chi nhánh (Branch Manager) — **12 Tính năng** (`M-01` đến `M-12`).
  - 7.4: Chủ chuỗi / Admin (Chain Admin) — **18 Tính năng** (`A-01` đến `A-18`) — Bao gồm Full CRUD Món/Combo/Ảnh/Giá/Menu mùa.
- **PHẦN VIII: Yêu Cầu Phi Chức Năng (NFRs) & Tiêu Chuẩn Vận Hành.**
- **PHẦN IX: Định Hướng Mở Rộng & Kiến Trúc Tương Lai (Scale Up / Future Work):** AI-3, AI-4, AI-5, Third-party Delivery API, Chấm công sinh trắc học Face AI, Đồng bộ Mesh Offline.

---

## 📐 BLUEPRINT FILE 2: `Actor_Phan_Quyen_Chuc_Nang.md`

### 1. Cấu trúc chương mục chuẩn hóa:
- **PHẦN 1: Tổng Quan 4 Nhóm Actor & Thiết Bị Truy Cập:**
  - Bảng tổng quan 4 Actor: Khách hàng (PWA di động), Nhân viên quầy/Barista (Web KDS + Staff Web POS), Quản lý chi nhánh (Manager Portal), Chủ chuỗi (Admin Portal).
  - 3 Nguyên tắc bất biến: (1) KHÔNG Staff Mobile App, (2) Chấm công WiFi Quán, (3) Takeaway POS qua Nhân viên với tích 10 ly chỉ áp dụng mang về.
- **PHẦN 2: Sơ Đồ Tương Tác Actor (Mermaid Diagram):**
  - Vẽ lại sơ đồ Mermaid thể hiện rõ ràng 2 nhánh của Dine-in (VietQR trả trước vs Tiền mặt trả sau), Delivery (QR riêng + ship 20k + VietQR), Takeaway POS (Tra CRM + 10 ly + Trả sau), và Chấm công WiFi.
- **PHẦN 3: Đặc Tả Chi Tiết Actor 1: Khách Hàng (Customer — 22 Tính Năng):**
  - Bảng 22 tính năng từ `C-01` đến `C-22`.
  - `C-06`: Lựa chọn thanh toán Dine-in (Nhánh A: VietQR trả trước; Nhánh B: Tiền mặt trả sau kèm hóa đơn in mã QR).
  - `C-07`: Đặt hàng giao tận nơi QR Delivery (SĐT + Địa chỉ bắt buộc + Phí ship 20k + VietQR 100%).
  - `C-11`: Hiển thị hồ sơ tích lũy CRM (Ghi rõ quyền lợi 10 ly đổi 1 áp dụng khi mua Takeaway).
  - **XÓA HOÀN TOÀN** `C-23` và `C-24`.
- **PHẦN 4: Đặc Tả Chi Tiết Actor 2: Nhân Viên Vận Hành Quầy (Staff — 12 Tính Năng):**
  - `S-01` đến `S-12`: KDS nhận đơn (đơn Paid của VietQR hoặc đơn Confirmed của Tiền mặt), BOM, đổi trạng thái, 86-toggle, in bill/tem, Takeaway POS, tra CRM 10 ly, thu tiền sau takeaway/dine-in tiền mặt, sơ đồ bàn, nhận chuông gọi, chấm công WiFi.
- **PHẦN 5: Đặc Tả Chi Tiết Actor 3: Quản Lý Chi Nhánh (Branch Manager — 12 Tính Năng):**
  - `M-01` đến `M-12`: Mở/kết ca đếm két tiền, phân ca đổi ca, giám sát chấm công WiFi, xuất kho bar, nhập kho NCC, kiểm kê kho hao hụt, sơ đồ bàn & giá riêng chi nhánh, cấu hình WiFi chấm công (SSID/BSSID/IP), dashboard vận hành, tiếp nhận alert review <= 2 sao, duyệt ảnh feedback.
- **PHẦN 6: Đặc Tả Chi Tiết Actor 4: Chủ Chuỗi / Admin (Chain Admin — 18 Tính Năng):**
  - `A-01` đến `A-18`: Quản trị chi nhánh, **Full CRUD Menu & BOM chuẩn** (Tạo, Sửa, Xóa, Thay thế món, Upload ảnh CDN, Quản lý danh mục & Thứ tự hiển thị, Lên lịch thực đơn mùa), Nhóm giá vùng, Khuyến mãi voucher, Cấu hình loyalty 10 ly takeaway toàn chuỗi, Duyệt AI-2 Combo Apriori, Dashboard P&L hợp nhất, So sánh chi nhánh, Phân tích Menu Engineering, CRM toàn chuỗi, Nhân sự bảng lương, Quản lý NCC, Sinh QR bàn/Delivery, Audit Log bất biến, Xuất Excel/PDF, Cấu hình VietQR/PayOS, Cấu hình AI Gemini, Sao lưu DB.
- **PHẦN 7: Ma Trận Phân Quyền Chi Tiết RBAC (Role-Based Access Control):**
  - Bảng ma trận 6 Roles (`GuestCustomer`, `AuthCustomer`, `BaristaStaff`, `CashierStaff`, `BranchManager`, `ChainAdmin`) đối chiếu với 8 nhóm API Resources.
- **PHẦN 8: Định Hướng Mở Rộng Actor & Quyền Hạn (Scale Up / Future Work):** Third-Party Delivery Driver, Supplier Portal, AI Chief Analyst.

---

## 📐 BLUEPRINT FILE 3: `Workflow_Quy_Trinh_Nghiep_Vu.md`

### 1. Cấu trúc chương mục chuẩn hóa:
- **Mục lục 16 quy trình nghiệp vụ cốt lõi (`WF-00` đến `WF-16`):**
- **Đặc tả chi tiết từng quy trình:**
  - **`WF-00`:** Nhận diện Khách hàng qua SĐT & Khởi tạo CRM trên PWA.
  - **`WF-01` (Trọng tâm cập nhật):** Đặt món tại bàn (Dine-in) — 2 Phương thức thanh toán:
    - *Sơ đồ khối 2 nhánh:* Rõ ràng, trực quan.
    - *Nhánh A (VietQR Pre-pay):* Khách chọn VietQR ➔ Sinh QR động ➔ Khách quét chuyển khoản ➔ PayOS Webhook xác nhận ➔ Đơn chuyển `Paid` ➔ SignalR phát `KitchenHub` ➔ Bếp KDS nhận đơn ➔ Pha chế (`Preparing`) ➔ Sẵn sàng (`Ready`) ➔ Phục vụ (`Served`) ➔ Hoàn tất (`Completed`).
    - *Nhánh B (Cash Post-pay):* Khách chọn Tiền mặt ➔ Đơn tạo với trạng thái `Confirmed` ➔ Đẩy NGAY vào KDS bếp ➔ Barista pha chế (`Preparing` ➔ `Ready`) ➔ Nhân viên bưng món ra bàn **KÈM HÓA ĐƠN IN SẴN MÃ VIETQR** ➔ Khách lựa chọn: Trả tiền mặt cho nhân viên HOẶC quét mã VietQR trên hóa đơn ➔ Nhân viên bấm xác nhận thanh toán trên Web Staff POS ➔ Trạng thái chuyển `Paid` ➔ `Completed`.
  - **`WF-02`:** Pha chế & Điều phối đơn hàng trên Kitchen Display System (Web KDS).
  - **`WF-03`:** Gọi thêm món & Gọi nhân viên hỗ trợ từ bàn.
  - **`WF-04`:** Chatbot AI Tư vấn món & Gợi ý cá nhân hóa (AI-1 Active RAG).
  - **`WF-05`:** Đánh giá chất lượng 1-5 sao, Tải ảnh Feedback & Cảnh báo quản lý <= 2 sao.
  - **`WF-06`:** Báo hết món (86-Toggle / Out of Stock) tức thì từ quầy bar.
  - **`WF-07`:** Chấm công Khóa mạng WiFi chi nhánh (WiFi-locked Attendance — SSID/BSSID/IP + Mã NV).
  - **`WF-08`:** Mở ca / Kết ca & Đối soát két tiền mặt (Cash Drawer Reconciliation).
  - **`WF-09`:** Xuất kho quầy Bar, Luân chuyển & Kiểm kê nguyên liệu định kỳ.
  - **`WF-10`:** Nhập kho từ Nhà cung cấp & Đối chiếu hóa đơn mua hàng.
  - **`WF-11`:** Báo cáo Doanh thu, P&L Lãi Lỗ & Vận hành ngày.
  - **`WF-12` (Trọng tâm cập nhật):** Quản trị Thực đơn Toàn diện (Admin Full CRUD):
    - Tạo mới sản phẩm & Định nghĩa BOM chi tiết.
    - Chỉnh sửa thông tin, giá bán, thành phần calo/dị ứng.
    - Xóa mềm món và chức năng **Thay thế món (Replace Product)** trên menu.
    - Tải ảnh sản phẩm lên CDN / Cloud Storage.
    - Quản lý danh mục và kéo thả sắp xếp thứ tự hiển thị.
    - Thiết lập **Menu Mùa (Seasonal Menu)** và lên lịch tự động xuất hiện/ẩn theo ngày.
    - Phân quyền giá bán theo nhóm chi nhánh.
  - **`WF-13`:** Khai phá & Đề xuất Combo tự động (AI-2 Active Apriori).
  - **`WF-14` (Trọng tâm cập nhật):** Quản lý Chương trình Loyalty Tích 10 Ly Tặng 1 (**CHỈ áp dụng cho Đơn Mang Về - Takeaway**) & Voucher khuyến mãi:
    - Nhấn mạnh: Chỉ khi mua đơn Takeaway tại quầy và có SĐT thì số ly mới được cộng vào `CupBalance`.
    - Đơn Dine-in và Delivery hoàn toàn không tích/đổi ly.
  - **`WF-15`:** Đặt hàng Giao tận nơi (QR Delivery) — Form SĐT + Địa chỉ bắt buộc, Phí ship 20k & 100% VietQR.
  - **`WF-16`:** Khách mua Mang Về tại Quầy (Takeaway Staff POS) — Tra cứu SĐT CRM, Tích 10 ly, Thu tiền sau (Tiền mặt / VietQR).
- **Phần Scale Up Workflows:** `WF-FW-01` (AI-3 NLQ), `WF-FW-02` (AI-4 Churn), `WF-FW-03` (AI-5 Demand), `WF-FW-04` (Third-Party Delivery Dispatch).

---

## 📐 BLUEPRINT FILE 4: `Tong_Quan_Kien_Truc_He_Thong.md`

### 1. Cấu trúc chương mục chuẩn hóa:
- **PHẦN 1: Nguyên Tắc Thiết Kế & Phong Cách Kiến Trúc:** Clean Architecture (.NET 8), CQRS MediatR, Event-Driven WebSocket SignalR, Micro-Frontend Next.js 14 Monorepo, Zero Hardware Dependency.
- **PHẦN 2: Sơ Đồ Kiến Trúc 4 Tầng Tổng Thể (4-Tier Layered Architecture):** Presentation Tier, Application Tier, Domain Tier, Infrastructure Tier.
- **PHẦN 3: Thiết Kế Tầng Giao Diện Người Dùng (Presentation Tier):** Cấu trúc 5 Route Groups: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.
- **PHẦN 4: Thiết Kế Tầng Ứng Dụng & Nghiệp Vụ (.NET 8 CQRS MediatR):** Commands, Queries, Behaviors, Domain Event Handlers.
- **PHẦN 5: Hạ Tầng Giao Tiếp Thời Gian Thực (SignalR Hubs):** `OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`.
- **PHẦN 6: Kiến Trúc Dữ Liệu & Lưu Trữ:**
  - PostgreSQL 16: Danh sách 25 thực thể chuẩn hóa. Chi tiết các bảng quan trọng: `orders` (chứa `order_type` enum `DineIn`/`TakeAway`/`Delivery`, `order_status`, `delivery_address`, `delivery_fee`), `branch_wifi_configs`, `attendances`, `products`, `combos`, `customer_reviews`, `audit_logs`.
  - Redis 7 Caching: Menu Cache-aside, Distributed Locks, SignalR Redis Backplane.
- **PHẦN 7: Kiến Trúc 5 Phân Hệ Nghiệp Vụ Cốt Lõi:**
  - 7.1: **Dine-In Dual-Payment Engine:** Hỗ trợ 2 State Machines độc lập:
    - Path A: `PendingPayment` ➔ `Paid` ➔ `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served`
    - Path B: `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served` ➔ `PendingPayment` ➔ `Paid`
  - 7.2: **QR Delivery Subsystem:** Form validation SĐT + Địa chỉ, Cố định `delivery_fee = 20000`, 100% Pre-payment PayOS Webhook.
  - 7.3: **Takeaway POS & Loyalty CRM Subsystem:** Tra cứu SĐT ➔ `CupBalance` (Takeaway only: 10 ly = 1 ly free) ➔ Thanh toán sau (Tiền mặt / VietQR).
  - 7.4: **WiFi-Locked Attendance Engine:** Xác thực kép BSSID/IP Subnet chi nhánh + Mã NV.
  - 7.5: **Consolidated Web Platform:** Thay thế 100% Staff App bằng Web Responsive.
- **PHẦN 8: Kiến Trúc Module Trí Tuệ Nhân Tạo (AI Pipelines):** AI-1 RAG Chatbot Gemini Flash Pipeline & AI-2 Apriori Combo Engine Pipeline.
- **PHẦN 9: Tô-pô Mạng, Bảo Mật & Triển Khai Hạ Tầng (Docker Compose, NGINX SSL, PostgreSQL, Redis).**
- **PHẦN 10: Điểm Nối Mở Rộng Kiến Trúc Tương Lai (Scale Up Extension Points):** `ITextToSqlEngine` (AI-3), `IChurnPredictor` (AI-4), `IDemandForecaster` (AI-5), `IDeliveryDispatchPartner`.

---

## 📐 BLUEPRINT FILE 5: `Tom_Tat_1_Trang_Executive_Summary.md`

### 1. Cấu trúc chương mục chuẩn hóa:
- **Header & Slogan:** 1 trang tóm tắt điều hành, cô đọng, sắc sảo.
- **Bức Tranh Tổng Thể Dưới Dạng Khung ASCII Bảng 6 Ô:**
  - Ô 1: 8 Bất cập quán cà phê hiện nay.
  - Ô 2: 5 Đột phá nghiệp vụ cốt lõi (Nêu rõ Dine-in 2 nhánh, QR Delivery 20k, Takeaway POS 10 ly, Chấm công WiFi, 100% Web).
  - Ô 3: Tech Stack hiện đại (.NET 8 Clean Arch + Next.js 14 + Postgres 16 + Redis 7 + SignalR).
  - Ô 4: 2 Module AI Active (AI-1 Chatbot RAG + AI-2 Combo Apriori).
  - Ô 5: Hiệu quả kinh tế (Tiết kiệm 15 - 22 triệu/tháng/quán, 0đ POS).
  - Ô 6: Quy mô thực thi (16 tuần, 4 thành viên, 64 tính năng core).
- **Mục 1: Bối Cảnh & Vấn Đề Thực Tiễn (Problem Statement):** Tóm tắt 8 bất cập thực tế.
- **Mục 2: Giải Pháp Toàn Diện — 5 Trụ Cột Đột Phá:**
  1. Đặt món tại bàn (Dine-in): 2 Phương thức thanh toán (VietQR trả trước hoặc Tiền mặt trả sau kèm hóa đơn có QR).
  2. Đặt giao tận nơi (QR Delivery): QR riêng, bắt buộc SĐT + Địa chỉ, phí ship cố định 20.000 VNĐ, 100% VietQR trả trước (No COD).
  3. Bán mang đi tại quầy (Takeaway Staff POS): Web POS quầy, tra SĐT CRM, chương trình tích lũy 10 ly = 1 ly (CHỈ áp dụng Takeaway), thanh toán sau.
  4. Chấm công khóa mạng WiFi: Xác thực WiFi quán (SSID/BSSID/IP) + Mã NV, xóa 100% GPS và QR 30s.
  5. Hợp nhất 100% Nền tảng Web: Xóa bỏ hoàn toàn Staff Mobile App.
- **Mục 3: Phân Rã 2 Module AI Active & 3 Module AI Scale Up.**
- **Mục 4: Giá Trị Kinh Tế, Khả Năng Khả Thi & Cam Kết Tiến Độ (16 tuần / 4 thành viên).**

---

# 5. KẾ HOẠCH BÀN GIAO & TIÊU CHÍ NGHIỆM THU (VERIFICATION CHECKLIST)

### Danh sách lệnh kiểm chứng tự động sau khi viết xong 5 files:

1. **Kiểm tra tính năng bị cấm C-23 và C-24 (Bắt buộc = 0 matches):**
   ```bash
   grep -rn "C-23" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   grep -rn "C-24" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   ```
2. **Kiểm tra Staff Mobile App (Chỉ xuất hiện trong ngữ cảnh 'loại bỏ'):**
   ```bash
   grep -rn "Staff Mobile App" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   ```
3. **Kiểm tra 2 nhánh thanh toán Dine-in (Tìm thấy trong cả 5 files):**
   ```bash
   grep -rn "tiền mặt" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   grep -rn "hóa đơn" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   ```
4. **Kiểm tra quy tắc Loyalty 10 ly Takeaway-only (Tìm thấy kèm điều kiện mang về):**
   ```bash
   grep -rn "10 ly" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   ```
5. **Kiểm tra QR Delivery phí ship 20.000 VNĐ:**
   ```bash
   grep -rn "20.000" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   ```
6. **Kiểm tra Zero Placeholder (Bắt buộc = 0 matches):**
   ```bash
   grep -rn "TODO" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   grep -rn "TBD" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   grep -rn "rest of code" d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\
   ```

---
*Báo cáo được lập hoàn tất bởi Explorer Subagent. Toàn bộ blueprint đã sẵn sàng để chuyển giao cho các Worker Agents thực thi tái thiết 5 tài liệu.*
