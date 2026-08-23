# BÁO CÁO BÀN GIAO CÔNG VIỆC (HANDOFF REPORT) — WORKER_WORKFLOWS

> **Đơn vị thực hiện:** `worker_workflows` (teamwork_preview_worker)  
> **Tài liệu bàn giao:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`  
> **Thời điểm hoàn tất:** 2026-08-22T15:14:00Z  
> **Mã công việc:** `WF-REWRITE-FULL-v2.5`  

---

## 1. OBSERVATION (Quan sát trực tiếp)

- **Tệp nguồn và yêu cầu chỉ đạo:**
  - `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (Follow-up 2026-08-22T15:06:50Z)
  - `d:\Idea_DoAn\temp_revised_content.txt` (Source of Truth từ `Smart_FB_OS_Revised_4members.docx`)
  - `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\report.md`
  - `d:\Idea_DoAn\.agents\spec_miner_doc_truth\report.md`
- **Tệp đích được viết lại hoàn toàn:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- **Quy mô tệp sau khi viết lại:**
  - Tổng số dòng: 1.649 dòng Markdown chuẩn hóa.
  - Dung lượng: 122.015 bytes (~122 KB).
  - Tổng số sơ đồ Mermaid: 1 sơ đồ tổng quan `graph TD` + 17 sơ đồ tuần tự `sequenceDiagram` chi tiết (tổng cộng 18 sơ đồ Mermaid hoàn chỉnh).
  - Số lượng quy trình nghiệp vụ cốt lõi: 17 quy trình chi tiết (WF-00 đến WF-16, bao gồm cả WF-01A và WF-01B).
  - Số lượng kịch bản xử lý trường hợp biên: 10 kịch bản vận hành thực tế.
  - Số lượng quy trình mở rộng tương lai (Scale Up): 4 quy trình (WF-FW-01 đến WF-FW-04).
- **Kiểm tra từ khóa cấm / placeholder:**
  - Grep search `TODO`: 0 vi phạm (chỉ xuất hiện trong câu quy chuẩn cấm).
  - Grep search `TBD`: 0 vi phạm (chỉ xuất hiện trong câu quy chuẩn cấm).
  - Grep search `C-23`, `C-24`: Đã loại bỏ hoàn toàn khỏi các quy trình (chỉ lưu vết xóa trong header).
  - Không có Staff Mobile App; 100% chuyển sang Web Responsive và Web KDS.

---

## 2. LOGIC CHAIN (Chuỗi lập luận & Logic thiết kế)

1. **Chuẩn hóa 2 nhánh Đặt món tại bàn (Dine-In):**
   - *Nhánh WF-01A (VietQR Trả trước):* Bắt buộc khách thanh toán trước qua VietQR. Khi PayOS gửi Webhook xác nhận (`Paid`), hệ thống mới phát sự kiện `OrderPaid` qua SignalR `KitchenHub` để KDS bếp nhận đơn. Vòng đời: `PendingPayment` ➔ `Paid` ➔ `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served`.
   - *Nhánh WF-01B (Tiền mặt Trả sau):* Khách chọn tiền mặt, đơn vào bếp ngay (`Confirmed`) mà không cần trả trước. Khi Barista bấm `Ready`, máy in nhiệt tự động in Hóa đơn tạm tính có sẵn **Mã VietQR động**. Nhân viên bưng nước kèm hóa đơn ra bàn. Khách có thể trả tiền mặt trực tiếp (nhân viên xác nhận trên Web Staff) hoặc quét VietQR in trên hóa đơn. Vòng đời: `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Served` ➔ `PendingPayment` ➔ `Paid`.
2. **Chuẩn hóa Quy trình Giao tận nơi QR Delivery (WF-02):**
   - Áp dụng mã QR Delivery riêng; bắt buộc nhập SĐT + Địa chỉ giao hàng (>= 10 ký tự).
   - Tự động cộng **Phí ship cố định 20.000 VNĐ** vào giỏ hàng.
   - **100% Trả trước qua VietQR** (Không chấp nhận tiền mặt COD).
   - KDS quầy bar nhận đơn với huy hiệu nổi bật **[DELIVERY]** kèm địa chỉ và SĐT người nhận.
3. **Chuẩn hóa Quy trình Bán mang về tại quầy Takeaway (WF-03):**
   - Khách không quét QR; Nhân viên thu ngân thao tác trực tiếp trên giao diện **Web POS Quầy**.
   - Tra cứu CRM bằng SĐT: Khách mới tạo nhanh hồ sơ; Khách cũ hiển thị số ly tích lũy (x/10).
   - **Chương trình Loyalty 10 ly = tặng 1 ly miễn phí:** Quy định chặt chẽ **CHỈ áp dụng cho đơn Takeaway** (không áp dụng Dine-in, không áp dụng Delivery). Giảm 100% giá 1 ly tiêu chuẩn cao nhất trong đơn.
   - Khách nhận món và thanh toán sau (Tiền mặt tính tiền thối tự động hoặc VietQR quầy).
4. **Chuẩn hóa Quy trình Chấm công Khóa mạng WiFi (WF-04):**
   - Bỏ hoàn toàn GPS 50m và mã QR xoay vòng 30 giây.
   - Xác thực 2 yếu tố: Client IP / BSSID Access Point thuộc cấu hình `branch_wifi_configs` + Mã nhân viên (`EmployeeCode`) hợp lệ đang hoạt động.
5. **Chuẩn hóa Hệ thống KDS & Vận hành Quầy (WF-05 đến WF-10):**
   - WF-05: Web KDS Full-screen qua SignalR `KitchenHub`, hỗ trợ chế độ Gom món thông minh (Item Batching).
   - WF-06: Khóa món khẩn cấp 86-Toggle, đồng bộ mờ món trên PWA trong < 1 giây qua `MenuHub`.
   - WF-07: Gọi phục vụ tại bàn, rate limit 60s/lần, chuông báo và banner cam nhấp nháy trên Web Staff POS.
   - WF-08: Đánh giá 1-5 sao, tải ảnh (kiểm tra Magic Bytes, WebP nén, CDN S3), đánh giá <= 2 sao kích hoạt sự kiện khẩn cấp `CriticalLowRatingAlert` tới Quản lý chi nhánh.
   - WF-09: Mở/kết ca két tiền, đối soát chênh lệch thừa/thiếu theo mệnh giá, xuất Z-Report.
   - WF-10: Xuất kho quầy Bar, trừ tồn tự động theo BOM khi đơn `Completed`, cảnh báo tồn kho thấp `LowStockAlert`.
6. **Chuẩn hóa Quản trị Admin, Menu, AI & Tài chính (WF-11 đến WF-16):**
   - WF-11: Admin Full CRUD Món ăn, Danh mục, Công thức định lượng BOM, Tải ảnh nén WebP.
   - WF-12: AI-2 Khai phá Combo tự động (Apriori Support >= 0.03, Confidence >= 0.6, Lift > 1.5), Admin duyệt phát hành lên Menu PWA.
   - WF-13: Kéo thả thứ tự danh mục, Lên lịch thực đơn theo mùa tự động bật/tắt qua Hangfire.
   - WF-14: Quản lý nhóm giá đa chi nhánh (Sân Bay, Trung Tâm, Tiêu Chuẩn).
   - WF-15: AI-1 Gemini 1.5 Flash Active RAG kết hợp Thời tiết OpenWeatherMap, Menu calo/dị ứng, CRM.
   - WF-16: Báo cáo tài chính P&L hợp nhất đa chi nhánh lúc 23:59, tính COGS theo BOM, Gross Profit, Gross Margin.

---

## 3. CAVEATS (Lưu ý & Giới hạn)

- **Phạm vi tài liệu:** Bản đặc tả này tập trung vào 100% chi tiết các luồng nghiệp vụ, hợp đồng dữ liệu và sơ đồ tuần tự. Phần thiết kế schema cơ sở dữ liệu chi tiết nằm ở `03_Quy_Trinh_Trien_Khai/02_Database_Design.md` và mã nguồn Backend/Frontend sẽ hiện thực hóa chuẩn xác theo bản đặc tả này.
- **Không có lưu vết thừa:** Các tính năng ngoài scope (AI-3, AI-4, AI-5, 3PL Dispatching) đã được đóng gói an toàn trong Chương 8 (Scale Up / Future Workflows) theo đúng yêu cầu người dùng.

---

## 4. CONCLUSION (Kết luận)

Tệp `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md` đã được viết lại hoàn chỉnh 100%, đáp ứng đầy đủ tất cả các yêu cầu khắt khe nhất của dự án:
1. Đầy đủ 16+ quy trình nghiệp vụ (WF-00 đến WF-16) với mô tả 8 mục chi tiết cho từng quy trình.
2. 18 sơ đồ Mermaid hợp lệ 100%, trực quan, chuẩn cú pháp `sequenceDiagram` và `graph TD`.
3. Tách biệt rõ ràng 2 nhánh Dine-In (VietQR trả trước vs Tiền mặt trả sau có bill VietQR).
4. Phản ánh chuẩn xác luồng Delivery (Phí ship 20k, VietQR 100%, SĐT + Địa chỉ).
5. Phản ánh chuẩn xác luồng Takeaway (Web POS quầy, CRM, tích 10 ly tặng 1 chỉ áp dụng Takeaway, thu tiền sau).
6. Phản ánh chuẩn xác Chấm công Khóa WiFi (BSSID/IP + Mã NV).
7. Xóa bỏ hoàn toàn Staff Mobile App, C-23 và C-24.
8. Bảng Ma trận trạng thái 4 kênh và Ma trận 10 Edge Cases hoàn chỉnh, zero placeholder.

---

## 5. VERIFICATION METHOD (Phương pháp kiểm chứng độc lập)

1. **Kiểm tra cấu trúc và tính toàn vẹn của tệp:**
   - Đường dẫn tệp: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
   - Số dòng: 1.649 dòng.
2. **Kiểm tra Zero Placeholder:**
   - Chạy lệnh tìm kiếm chuỗi: Không tồn tại `// TODO`, `[TBD]`, `...`, `/* rest of code */`.
3. **Kiểm tra cú pháp Mermaid:**
   - 18 khối mã Mermaid đều bắt đầu bằng ````mermaid` và kết thúc hợp lệ bằng ````. Mọi thẻ `sequenceDiagram` đều có cấu trúc `autonumber`, `participant`/`actor` rõ ràng, các khối `alt`/`else`/`end` đóng mở chuẩn xác.
4. **Kiểm tra tính nhất quán với Nguồn sự thật (`temp_revised_content.txt`):**
   - Đầy đủ 5 thay đổi cốt lõi: Dine-in 2 nhánh, Delivery 20k VietQR, Takeaway Web POS 10 ly = 1, Chấm công WiFi, Bỏ Staff App + C-23/C-24.
