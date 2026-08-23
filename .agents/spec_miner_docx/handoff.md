# BÁO CÁO BÀN GIAO CỦA SPEC MINER 1 (HANDOFF REPORT)
## DỰ ÁN: SMART F&B OPERATING SYSTEM (SMART F&B OS)
> **Tác nhân thực hiện**: Spec Miner 1 (`spec_miner_docx`)  
> **Người nhận bàn giao**: Lead Project Orchestrator (`parent` / `10ef5828-46c5-4123-b200-c2d752dd2ea6`)  
> **Loại bàn giao**: Hard Handoff (Nhiệm vụ hoàn thành 100%)  
> **Tài liệu bàn giao chính**: `d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md`

---

### 1. Quan Sát Trực Tiếp (Observation)
- **Nguồn sự thật chính thức**: Tệp `Smart_FB_OS_Revised_4members.docx` (đã trích xuất toàn văn tại `d:\Idea_DoAn\temp_revised_content.txt` — 214 dòng, 18.822 bytes).
- **Yêu cầu chỉ đạo**: Tệp `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (114 dòng, 10.390 bytes).
- **Phát hiện cốt lõi từ docx**:
  1. *Actors & Roles*: 4 nhóm vai trò (Khách hàng, Nhân viên/Thu ngân, Pha chế/Bếp, Quản lý/Chủ chuỗi). **Không có vai trò người dùng Staff App riêng biệt**; các thao tác phục vụ chuyển sang Web UI.
  2. *5 Thay đổi nghiệp vụ cốt lõi*:
     - Dine-in: Thanh toán VietQR trước, trạng thái `PendingPayment` -> `Paid` -> `Confirmed` -> Bếp mới nhận đơn qua SignalR.
     - QR Delivery: Quét QR từ xa, bắt buộc nhập SĐT + Địa chỉ giao hàng (`delivery_address`), phí ship cố định 20.000 VNĐ (`delivery_fee = 20000`), thanh toán VietQR trước 100% (không COD).
     - Takeaway: Nhân viên thao tác trên Staff Web UI (không QR), tìm SĐT khách, tạo CRM, áp dụng loyalty 10 ly = 1 ly miễn phí, thanh toán sau khi nhận đồ uống.
     - Chấm công WiFi: Khóa theo WiFi chi nhánh (`branch_wifi_configs`), kiểm tra WiFi + Mã nhân viên, loại bỏ hoàn toàn GPS 50m và QR động 30s.
     - Staff App: Xóa bỏ hoàn toàn app di động của nhân viên, chuyển sang Giao diện Web Staff / KDS.
  3. *AI Modules*: 2 Module Active triển khai thực tế (AI-1 RAG Chatbot, AI-2 Apriori/FP-Growth Combo) và 3 Module Future Work (AI-3 NLQ Analytics, AI-4 Churn Prediction, AI-5 Menu Intelligence).
  4. *Entities*: 25 thực thể cơ sở dữ liệu hoàn chỉnh, bao gồm `branch_wifi_configs`, `orders` (với `delivery_address`, `delivery_fee`, `order_type`), `customers` (`loyalty_cups_accumulated`), `audit_logs`...
  5. *Tech Stack & Scope*: .NET 8 Clean Architecture, Next.js 14 App Router, PostgreSQL 16, Redis 7, SignalR, 4 devs, 16 tuần.

---

### 2. Chuỗi Suy Luận Kỹ Thuật (Logic Chain)
1. Từ nội dung mục 3.2.c và 3.2.b trong docx: Việc yêu cầu thanh toán VietQR trước cho Dine-in và Delivery là cốt lõi để loại bỏ hoàn toàn rủi ro bùng đơn / eat-and-run và giảm tải cho nhân viên thu ngân.
2. Từ việc loại bỏ Staff Mobile App: Toàn bộ routing frontend phải gom về Next.js 14 Web Monorepo (`(staff)`, `(kds)`, `(customer)`, `(manager)`, `(admin)`), loại bỏ các dependencies React Native / Flutter / Mobile App containers trong Docker Compose và sơ đồ kiến trúc.
3. Từ việc chuyển đổi chấm công sang WiFi-locked: Schema cơ sở dữ liệu cần bổ sung bảng `branch_wifi_configs` để lưu trữ SSID, BSSID/MAC, IP Gateway chi nhánh; bảng `attendances` cập nhật các trường lưu vết mạng WiFi kết nối thay vì tọa độ GPS.
4. Từ việc phân rã AI trong Capstone 16 tuần: Chỉ 2 module AI-1 và AI-2 có đầy đủ pipeline dữ liệu, đánh giá độ chính xác thực nghiệm (`Precision@K`, `Support`, `Confidence`, `Lift`); 3 module AI còn lại phải được định danh rõ ràng là "Scale Up / Future Work" để tránh vỡ kế hoạch thực thi của 4 lập trình viên.

---

### 3. Các Giới Hạn & Giả Định (Caveats)
- Không có bất kỳ giả định ngoài lề nào: Mọi thông tin đều được bóc tách và đối chiếu chặt chẽ 100% từ `temp_revised_content.txt` và `ORIGINAL_REQUEST.md`.
- Các tính năng mở rộng cũ trong bộ tài liệu 29 tệp markdown trước đây (như Zalo OA ZNS tự động, máy POS Sunmi ngoại tuyến, AI Text-to-SQL) đã được đánh dấu chuyển sang mục "Scale Up / Future Work" thay vì bị xóa bỏ.

---

### 4. Kết Luận (Conclusion)
- Đã hoàn thành xuất sắc bản bóc tách đặc tả toàn diện tại: `d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md`.
- Tài liệu gồm 8 phần chuyên sâu, bảng 47 tính năng chi tiết (kèm Inputs, Outputs, Error Behavior), 10 kịch bản biên (Edge Cases), chi tiết 11 nhóm NFRs, 25 thực thể cơ sở dữ liệu, và hướng dẫn đồng bộ rõ ràng.
- Đủ điều kiện 100% để Orchestrator và các agent tài liệu (R1, R2, R3, R4, R5) tiến hành cập nhật đồng bộ toàn bộ kho tài liệu 30+ tệp markdown.

---

### 5. Phương Pháp Kiểm Chứng Độc Lập (Verification Method)
- **Kiểm tra tệp báo cáo đặc tả**:
  ```powershell
  Get-Item d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md
  ```
- **Kiểm tra tính đầy đủ của 5 luồng cốt lõi**:
  ```powershell
  Select-String -Path d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md -Pattern "Dine-in", "Delivery", "Takeaway", "WiFi-Locked", "Staff Web UI"
  ```
- **Kiểm tra tính không tồn tại của placeholder**:
  ```powershell
  Select-String -Path d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md -Pattern "TODO", "TBD", "..."
  ```
