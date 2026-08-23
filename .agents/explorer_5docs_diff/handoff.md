# 🤝 HANDOFF REPORT — EXPLORER 5 DOCS GAP ANALYSIS & REWRITING BLUEPRINT

- **From**: Explorer Agent (`explorer_5docs_diff`)
- **To**: Orchestrator Agent (`parent`) / Worker Agents
- **Timestamp**: 2026-08-22T15:10:45Z
- **Target Folder**: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`

---

## 1. OBSERVATION (Quan sát trực tiếp & Bằng chứng xác thực)

Sau khi kiểm tra chi tiết cả 5 file tài liệu đặc tả gốc tại `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc/`, các bằng chứng kỹ thuật cụ thể được ghi nhận như sau:

### 1.1 Về Tính Năng Bị Cấm `C-23` & `C-24` (Còn sót lại trong 2 files):
- **File `Smart_FB_Operating_System.md`:**
  - Dòng 327: `- 'C-23': Chia sẻ thông tin món ăn lên mạng xã hội.`
  - Dòng 328: `- 'C-24': Nhận thông báo ưu đãi và voucher tri ân qua tin nhắn PWA.`
  - Dòng 295: `│ 👤 Customer │ Mobile Browser PWA ('(customer)') │ 24 Tính năng ('C-01' ~ 'C-24')│`
- **File `Actor_Phan_Quyen_Chuc_Nang.md`:**
  - Dòng 132: `| 'C-23' | Chia Sẻ Món Ăn Mạng Xã Hội | Tạo liên kết hoặc hình ảnh món... |`
  - Dòng 133: `| 'C-24' | Nhận Thông Báo Khuyến Mãi PWA | Đăng ký nhận thông báo Web Push... |`
  - Dòng 106: `### Bảng Danh Mục 24 Tính Năng Khách Hàng ('C-01' đến 'C-24')`

### 1.2 Về Nghiệp Vụ Dine-In (Thiếu hoàn toàn Nhánh B Tiền Mặt Trả Sau):
- **File `Smart_FB_Operating_System.md`:**
  - Dòng 121–124: `2.1 TRỤ CỘT 1: ĐẶT MÓN TẠI BÀN (DINE-IN) — THANH TOÁN VIETQR TRƯỚC (PRE-PAYMENT) - Quy tắc bất biến: Khách hàng ngồi tại bàn quét mã QR chỉ được xem là hoàn tất đặt món khi đã thanh toán VietQR thành công. Bếp pha chế (KDS) tuyệt đối KHÔNG nhận đơn khi đơn hàng còn ở trạng thái chờ thanh toán (PendingPayment).`
- **File `Actor_Phan_Quyen_Chuc_Nang.md`:**
  - Dòng 63: Sơ đồ Mermaid chỉ vẽ: `C2 -->|Bắt buộc| C4[Thanh toán VietQR Trả Trước] --> C5[Paid] --> S1[KDS Bếp]`.
  - Dòng 115: `| 'C-06' | Thanh Toán VietQR Trả Trước (Pre-payment) | BẮT BUỘC: Sinh mã VietQR động... Bếp chỉ nhận đơn sau khi Paid. |`
- **File `Workflow_Quy_Trinh_Nghiep_Vu.md`:**
  - Dòng 15 & 55–70: `WF-01: ĐẶT MÓN TẠI BÀN (DINE-IN) — VIETQR TRẢ TRƯỚC BẮT BUỘC` (Không hề có nhánh Tiền mặt).
- **File `Tong_Quan_Kien_Truc_He_Thong.md`:**
  - Dòng 173–176: `1. DINE-IN PRE-PAYMENT ENGINE: Cổng KDS được bảo vệ bằng Guard Clause: Chỉ nạp đơn khi Order.Status == OrderStatus.Paid.`
- **File `Tom_Tat_1_Trang_Executive_Summary.md`:**
  - Dòng 33: `1. Đặt Món Tại Bàn (Dine-in Pre-payment): ... bắt buộc thanh toán VietQR trước.`

### 1.3 Về Nghiệp Vụ Loyalty 10 Ly (Ghi sai phạm vi áp dụng):
- **File `Workflow_Quy_Trinh_Nghiep_Vu.md`:**
  - Dòng 290: `Mỗi khi khách hàng hoàn tất một đơn hàng hợp lệ (Dine-in, Takeaway, hoặc Delivery) có nhập Số điện thoại CRM, hệ thống tự động đếm tổng số ly...` (Sai lệch vì chỉ Takeaway mới được tích 10 ly).

### 1.4 Về Admin Full CRUD:
- Chưa có mô tả cụ thể về chức năng "Thay thế món" (Replace Product), quản lý thứ tự danh mục và lên lịch Menu Mùa (Seasonal Menus) trong `Smart_FB_Operating_System.md` và `Actor_Phan_Quyen_Chuc_Nang.md`.

---

## 2. LOGIC CHAIN (Chuỗi suy luận từ quan sát đến kết luận)

1. **Từ Quan sát 1.1:** Người dùng yêu cầu xóa 100% C-23 và C-24 khỏi toàn bộ tài liệu (không giữ lại kể cả trong Future Work). Vì C-23 và C-24 vẫn tồn tại ở 2 file nên số lượng tính năng Customer bị tính sai là 24 (chuẩn là 22), tổng số tính năng hệ thống bị sai là 66 (chuẩn là 64). ➔ **Cần xóa C-23, C-24 và điều chỉnh tổng số thành 22 tính năng Customer, 64 tính năng toàn hệ thống.**
2. **Từ Quan sát 1.2:** Người dùng quy định rõ ràng: Dine-In có **2 phương thức thanh toán**:
   - Path A: VietQR (Pre-pay): `Pending Payment` ➔ `Paid` ➔ `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served`.
   - Path B: Cash (Post-pay): `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served` ➔ `Pending Payment` ➔ `Paid` (Đơn vào bếp ngay, nhân viên bưng món kèm hóa đơn có mã VietQR, khách trả tiền mặt hoặc quét VietQR trên hóa đơn).  
   Hiện tại cả 5 file đều chỉ viết 1 nhánh trả trước ➔ **Cần cập nhật đồng bộ cả 5 file để hỗ trợ 2 nhánh thanh toán Dine-in.**
3. **Từ Quan sát 1.3:** Người dùng quy định "Loyalty 10 ly = 1 ly miễn phí CHỈ ÁP DỤNG ĐƠN TAKEAWAY". Tuy nhiên dòng 290 trong `Workflow_Quy_Trinh_Nghiep_Vu.md` lại ghi áp dụng cho cả Dine-in và Delivery ➔ **Cần sửa lại định nghĩa WF-14 và các mô tả CRM để nhấn mạnh Takeaway-only.**
4. **Từ Quan sát 1.4:** Admin cần toàn quyền CRUD (Tạo, sửa, xóa, thay thế sản phẩm, combo, upload ảnh, giá chi nhánh, 86 toggle, danh mục, menu mùa) ➔ **Cần đưa đầy đủ chi tiết này vào bảng tính năng Admin (`A-02`), ma trận RBAC và quy trình `WF-12`.**

---

## 3. CAVEATS (Giới hạn & Lưu ý)

- **Phạm vi thẩm định:** Báo cáo này tập trung vào 5 file tài liệu đặc tả gốc tại `01_Tai_Lieu_Dac_Ta_Goc/`. File HTML `Actor_KhachHang_Xem.html` là file export cũ không nằm trong danh sách 5 file markdown cần viết lại nhưng cũng cần được xóa/merge trong đợt dọn dẹp tổng thể sau này.
- **Tính khả thi:** Các bản vẽ Mermaid đã được kiểm tra cú pháp và đảm bảo render mượt mà khi triển khai.
- **Tính trọn vẹn (Zero Placeholders):** Các worker agents khi viết lại tuyệt đối không được sử dụng bất kỳ ký hiệu giữ chỗ nào (`// TODO`, `...`, `TBD`).

---

## 4. CONCLUSION (Kết luận & Đề xuất hành động)

Đã hoàn thành toàn bộ tài liệu phân tích lỗ hổng và blueprint chi tiết tại:
`d:\Idea_DoAn\.agents\explorer_5docs_diff\report.md`

### Các bước tiếp theo đề xuất cho Orchestrator:
1. Giao nhiệm vụ cho các Worker Agents viết lại toàn bộ 5 file trong `01_Tai_Lieu_Dac_Ta_Goc/` bám sát 100% theo Blueprint trong `report.md`.
2. Chạy bộ lệnh kiểm chứng (Verification Commands) ở Mục 5 để nghiệm thu chất lượng.

---

## 5. VERIFICATION METHOD (Phương pháp kiểm chứng độc lập)

Để kiểm chứng tính chính xác của báo cáo này và kết quả sau khi các workers viết xong:

```powershell
# 1. Kiểm tra không còn C-23 và C-24
Get-ChildItem -Path "d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\*.md" | Select-String -Pattern "C-23|C-24"

# 2. Kiểm tra xuất hiện luồng Tiền mặt trong Dine-in
Get-ChildItem -Path "d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\*.md" | Select-String -Pattern "Tiền mặt.*kèm hóa đơn|Nhánh B"

# 3. Kiểm tra loyalty 10 ly Takeaway only
Get-ChildItem -Path "d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\*.md" | Select-String -Pattern "10 ly"

# 4. Kiểm tra QR Delivery 20k
Get-ChildItem -Path "d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\*.md" | Select-String -Pattern "20.000"

# 5. Kiểm tra không còn placeholder
Get-ChildItem -Path "d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\*.md" | Select-String -Pattern "TODO|TBD|\.\.\.|rest of"
```
