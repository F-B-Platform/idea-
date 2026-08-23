# 📋 BÁO CÁO BÀN GIAO KỸ THUẬT (HANDOFF REPORT)
**Tác nhân (Agent):** Spec Miner 3 (`spec_miner_flows`)  
**Mã phiên (Conv ID):** `4f49f677-925d-4452-93b2-cb5145506525`  
**Người nhận (Recipient):** Orchestrator (`10ef5828-46c5-4123-b200-c2d752dd2ea6`)  
**Tài liệu sản phẩm bàn giao:** `d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md`

---

## 1. OBSERVATION (QUAN SÁT THỰC TẾ)

1. **Văn bản Nguồn sự thật (`ORIGINAL_REQUEST.md` & `temp_revised_content.txt`):**
   - File `ORIGINAL_REQUEST.md` (dòng 32-57) xác lập 5 thay đổi nghiệp vụ cốt lõi bắt buộc:
     - Change 1: Dine-in thanh toán VietQR trước khi bếp nhận đơn (`PendingPayment` -> `Paid` -> `Confirmed` -> `Preparing` -> `Ready` -> `Completed`).
     - Change 2: QR Delivery đặt tận nơi, phí ship cố định 20.000 VNĐ, thanh toán VietQR 100% trước, thêm trường `delivery_address`, `delivery_fee`, `order_type`.
     - Change 3: Takeaway qua giao diện Nhân viên (bỏ QR Takeaway), tra cứu SĐT CRM, loyalty 10 ly tặng 1 ly, thanh toán tiền mặt/VietQR tại quầy.
     - Change 4: Chấm công WiFi-locked (bỏ GPS 50m & QR động 30s), xác thực `wifi_ssid`, `wifi_bssid`, subnet IP + Mã nhân viên.
     - Change 5: Xóa hoàn toàn Staff Mobile App, hợp nhất vào Web KDS, Web POS và Manager Web Portal.
   - File `temp_revised_content.txt` (dòng 124-128) xác nhận chỉ có 2 AI modules được triển khai thực tế (AI-1 Chatbot gợi ý RAG, AI-2 Khai phá Combo Apriori), 3 AI còn lại là Future Work.

2. **Các điểm xung đột trong tài liệu hiện tại:**
   - Trong `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md` (dòng 2131-2162): API `POST /api/v1/staff/clock-in` vẫn yêu cầu tham số `latitude`, `longitude`, `posRotatingQrCode`.
   - Trong `04_Thiet_Ke_Kien_Truc_Diagrams/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md` (dòng 86-120): Sequence Diagram số 3 vẫn mô tả luồng khách ăn xong mới yêu cầu bill thanh toán (`POST /api/v1/orders/001/request-bill`).
   - Trong `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` (dòng 86-94, 267): Bảng `Attendances` và `QrCodes` vẫn chứa cơ chế cũ; bảng `Orders` thiếu các trường `DeliveryAddress`, `DeliveryFee`, và thiếu quan hệ `LoyaltyCupTransactions`.
   - Trong `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS_Revised.md` (dòng 18, 98): Vẫn còn đề cập đến "Staff App (Mobile)" và luồng thanh toán sau khi nhận món.

---

## 2. LOGIC CHAIN (CHUỖI SUY LUẬN KỸ THUẬT)

1. **Từ Quan sát 1 và 2 (Change 1):** Để bếp không bao giờ phải chuẩn bị món cho các đơn chưa thanh toán hoặc bị "bùng", vòng đời đơn hàng bắt buộc phải bổ sung trạng thái `PendingPayment` với cơ chế Time-to-Live (TTL 10 phút). Khi tạo đơn, hệ thống chỉ lưu `PendingPayment` và sinh mã VietQR. Chỉ khi Webhook từ cổng thanh toán/ngân hàng gọi về xác thực `Status = Success` thì hệ thống mới chuyển `Status = Confirmed` và phát tín hiệu SignalR `NewOrderTicket` xuống KDS.
2. **Từ Quan sát 1 và 2 (Change 2):** Đơn giao hàng (Delivery) là kênh bán hàng từ xa, không có mặt khách tại quán. Do đó, phải bắt buộc thu thập `DeliveryAddress`, `RecipientPhone` và cộng tự động `DeliveryFee = 20000` VNĐ vào `TotalAmount`. Đồng thời, phương thức thanh toán phải là 100% VietQR trả trước (không áp dụng COD) để đảm bảo thu được tiền trước khi pha chế và giao hàng.
3. **Từ Quan sát 1 và 2 (Change 3):** Khách mua mang về thường đứng trực tiếp tại quầy gọi nhanh. Bỏ QR Takeaway tự quét giúp tối ưu tốc độ. Nhân viên POS chỉ cần gõ SĐT khách để truy vấn CRM; cơ chế tích điểm phức tạp cũ được thay thế bằng quy tắc trực quan: `CupBalance / 10`. Cứ đủ 10 ly đồ uống hoàn tất thì khách được tặng 1 ly miễn phí trị giá tối đa 35.000 VNĐ.
4. **Từ Quan sát 1 và 2 (Change 4):** GPS Geofence thường bị trôi sai số trong nhà và dễ bị fake GPS, còn QR xoay 30s đòi hỏi thiết bị hiển thị phụ. Chuyển sang xác thực mạng WiFi nội bộ (đối chiếu IP Client Subnet và BSSID Access Point của chi nhánh) kết hợp Employee ID là giải pháp gọn nhẹ, tin cậy tuyệt đối và không phát sinh chi phí phần cứng.
5. **Từ Quan sát 1 và 2 (Change 5):** Việc duy trì ứng dụng di động riêng (Flutter/React Native) cho nhân viên phục vụ làm tăng gấp đôi khối lượng công việc frontend và bảo trì hạ tầng di động (APNs/FCM, App Store). Hợp nhất toàn bộ giao diện phục vụ, bếp và thu ngân vào nền tảng Web Responsive (Next.js 14 App Router với các route `/kds`, `/pos`, `/manager`) giúp tinh gọn hệ thống, dễ triển khai qua Docker và phù hợp hoàn hảo với nhóm 4 thành viên.

---

## 3. CAVEATS (CÁC ĐIỂM GIỚI HẠN & GIẢ ĐỊNH)

1. **Ranh giới Scale-Up của Delivery:** Hệ thống trong phạm vi hiện tại (MVP Capstone) chưa tích hợp API tự động đẩy đơn qua đối tác vận chuyển thứ ba (AhaMove, GrabExpress) mà do nhân viên/shipper nội bộ chi nhánh đảm nhiệm giao hàng sau khi KDS bấm `Ready`.
2. **Trình duyệt Web và thông tin BSSID WiFi:** Trình duyệt web tiêu chuẩn (trên máy tính/di động) có thể bị hạn chế quyền truy cập trực tiếp vào MAC Address (BSSID) của Access Point do chính sách sandbox bảo mật của trình duyệt. Do đó, logic xác thực WiFi ở backend hỗ trợ cả 2 cơ chế: (a) Kiểm tra địa chỉ IP Public / Gateway Subnet của kết nối HTTP/WebSocket (cơ chế chính), và (b) BSSID Header nếu chạy qua PWA hoặc thiết bị cho phép.
3. **Giá trị quy đổi Ly miễn phí:** Ly miễn phí quy đổi từ 10 ly tích lũy được mặc định áp dụng cho 1 ly đồ uống tiêu chuẩn có giá trị tối đa 35.000 VNĐ.

---

## 4. CONCLUSION (KẾT LUẬN & KẾ HOẠCH BÀN GIAO)

Đã hoàn thành 100% bộ tài liệu hợp đồng kỹ thuật chi tiết tại `d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md` với đầy đủ:
- Chi tiết 5 thay đổi nghiệp vụ cốt lõi kèm Ma trận trạng thái (State Machine).
- DDL Schema PostgreSQL 16 hoàn chỉnh với 4 ENUMs, các bảng `Orders`, `Payments`, `Customers`, `LoyaltyCupTransactions`, `Branches`, `Attendances`.
- Đặc tả REST API chuẩn OpenAPI 3.1 & RFC 7807 ProblemDetails (Request JSON Schema, Response JSON Schema, Webhook callbacks).
- Hợp đồng SignalR Hubs (`PaymentHub`, `KitchenHub`, `OrderHub`) với sự kiện và JSON payload chi tiết.
- 4 Sơ đồ tuần tự (Mermaid Sequence Diagrams) chuẩn cú pháp và 4 Khung giao diện UI Wireframe ASCII chi tiết.
- Ma trận phân định ranh giới MVP vs Scale-Up / Future Work.

---

## 5. VERIFICATION METHOD (HƯỚNG DẪN KIỂM CHỨNG ĐỘC LẬP)

1. **Kiểm tra tệp Hợp đồng kỹ thuật:**
   - Đọc tệp `d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md`.
   - Kiểm tra tính đầy đủ của các mục từ Mục 1 đến Mục 8.
2. **Kiểm tra cú pháp Mermaid Diagrams:**
   - Rà soát tất cả 4 khối mã ````mermaid```` trong tệp `technical_contracts.md` để đảm bảo hợp lệ về mặt cú pháp và có thể render trực quan.
3. **Kiểm tra tính nhất quán với Nguồn sự thật:**
   - Đối chiếu các trạng thái đơn (`PendingPayment`, `Paid`, `Confirmed`, `Preparing`, `Ready`, `Completed`) và phí ship 20.000 VNĐ với `ORIGINAL_REQUEST.md`.
