# BÁO CÁO BÓC TÁCH ĐẶC TẢ NGHIỆP VỤ CHÍNH THỨC (DOCX SPECIFICATION EXTRACTION REPORT)
## DỰ ÁN: SMART F&B OPERATING SYSTEM (SMART F&B OS)
> **Nguồn sự thật (Source of Truth)**: `Smart_FB_OS_Revised_4members.docx` (Trích xuất text: `temp_revised_content.txt`)  
> **Tài liệu đối chiếu bổ trợ**: `ORIGINAL_REQUEST.md`  
> **Đơn vị thực hiện**: Spec Miner 1 (Specification Miner Agent - Subagent)  
> **Ngày lập báo cáo**: 2026-08-22  
> **Quy mô dự án**: Đồ án Capstone 4 thành viên (2 Backend + 2 Frontend), 16 tuần (08 Sprints)

---

# 1. TỔNG QUAN DỰ ÁN & MÔI TRƯỜNG THỰC THI (PROJECT OVERVIEW & CONSTRAINTS)

### 1.1. Thông Tin Đăng Ký Đồ Án
- **Tên tiếng Anh**: Smart F&B OS - AI-Powered QR Order & Management Platform
- **Tên tiếng Việt**: Smart F&B OS - Nền tảng quản lý và vận hành quán cà phê thông minh tích hợp AI và đặt món QR
- **Chuyên ngành**: Kỹ thuật phần mềm (Software Engineering - SE)
- **Thời lượng**: 16 tuần (08 Sprints) — Đội ngũ 4 thành viên (2 Backend Developers + 2 Frontend Developers)
- **Kiến trúc & Công nghệ chuẩn hóa**:
  - **Backend API**: .NET 8 C# Clean Architecture (4 dự án: `SmartFB.Domain`, `SmartFB.Application`, `SmartFB.Infrastructure`, `SmartFB.API`), MediatR CQRS, FluentValidation, Entity Framework Core 8.
  - **Frontend Monorepo**: Next.js 14 App Router, React 19, TypeScript, Tailwind CSS, Zustand, Shadcn/UI. Phân tách thành 5 Route Groups: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.
  - **Cơ sở dữ liệu & Bộ đệm**: PostgreSQL 16 (Relational Database, UUID Primary Keys, Soft Delete, Audit Trail) + Redis 7 (Cache-aside, Distributed Lock, SignalR Redis Backplane).
  - **Giao tiếp thời gian thực**: ASP.NET Core SignalR WebSocket Hubs (`OrderHub`, `KdsHub`, `NotificationHub`).
  - **Cổng thanh toán tự động**: VietQR / PayOS (Xử lý Webhook callback tự động với HMAC-SHA256 & Idempotency).
  - **Trí tuệ nhân tạo (AI)**: Google Gemini 1.5 Flash API qua C# SDK / RAG Pipeline; Thuật toán khai phá luật kết hợp Apriori / FP-Growth.
  - **Hạ tầng & Đóng gói**: Docker Compose cô lập mạng `smartfb-net`, Nginx Reverse Proxy (SSL Certbot & WebSocket Upgrade headers).

---

# 2. MA TRẬN VAI TRÒ NGƯỜI DÙNG & PHÂN HỆ TRUY CẬP (ACTORS & ROLES MATRIX)

Hệ thống phục vụ **4 nhóm tác nhân chính** (Customer, Cashier/Service Staff, Barista/Chef, Branch Manager, Chain Owner/Admin).  
**Đặc biệt lưu ý:** Loại bỏ hoàn toàn ứng dụng di động riêng cho nhân viên (**Staff Mobile App**). Toàn bộ nghiệp vụ nhân viên phục vụ và thu ngân được tích hợp trực tiếp vào **Giao diện Web Responsive (Staff Web UI / Counter POS)**.

| STT | Tác Nhân (Actor) | Phân Hệ Truy Cập (Route Group / Interface) | Thiết Bị Đích | Mô Tả Trách Nhiệm & Quyền Hạn Nghiệp Vụ |
|:---:|---|---|---|---|
| 1 | **Khách hàng (Customer)** | `(customer)` - Progressive Web App (PWA) | Smartphone (iOS / Android Browser) | Quét QR bàn (Dine-in) hoặc QR Delivery; nhập SĐT nhận diện CRM; duyệt menu, tùy biến món (Size/Đường/Đá/Topping); **thanh toán VietQR trước**; theo dõi tiến độ pha chế; gọi phục vụ; đánh giá 1-5 sao và gửi ảnh review (tùy chọn ẩn danh). |
| 2 | **Thu ngân / Nhân viên (Cashier / Service Staff)** | `(staff)` - Staff Web Portal & Counter POS | Tablet POS / PC Thu ngân / Smartphone Browser | Mở màn hình Takeaway: tra cứu SĐT khách, tạo hồ sơ CRM mới hoặc xem tích điểm (10 ly = 1 ly miễn phí), chọn món mang đi, **thu tiền SAU khi giao món** (Tiền mặt hoặc VietQR); xem sơ đồ bàn, nhận thông báo gọi phục vụ; **chấm công khóa WiFi (WiFi-locked)**. |
| 3 | **Pha chế / Bếp (Barista / Chef)** | `(kds)` - Kitchen Display System | Màn hình TV Thông minh / iPad / PC Bếp | Nhận order thời gian thực qua SignalR (chỉ nhận đơn đã thanh toán); xem chi tiết định lượng/công thức chuẩn; đổi trạng thái đơn (`Preparing` -> `Ready` -> `Served` -> `Completed`); bật/tắt trạng thái hết món (Out-of-stock) tức thì; kích hoạt in tem nhãn/hóa đơn. |
| 4 | **Quản lý chi nhánh (Branch Manager)** | `(manager)` - Branch Management Portal | Laptop / Desktop / Tablet | Mở/đóng ca làm việc, kiểm đếm két tiền đầu/cuối ca và đối soát chênh lệch; xếp lịch làm việc, duyệt đổi ca, theo dõi chấm công WiFi; lập phiếu lĩnh nguyên liệu, nhập kho nhà cung cấp, kiểm kê tồn kho/ghi nhận hao hụt; quản lý sơ đồ bàn, giờ mở cửa, giá bán chi nhánh; tiếp nhận cảnh báo đánh giá thấp (<= 2 sao) để xử lý sự cố. |
| 5 | **Chủ chuỗi / Quản trị viên (Chain Owner / Admin)** | `(admin)` - Chain Executive Portal | Desktop / Laptop | Quản lý danh mục món dùng chung, công thức chuẩn, nhóm giá chi nhánh, thực đơn mùa; cấu hình combo, voucher, quy tắc loyalty (10 ly = 1 ly); xem dashboard P&L hợp nhất đa chi nhánh; phân quyền RBAC & cô lập dữ liệu chi nhánh; tra cứu Audit Log bất biến; phê duyệt combo AI đề xuất; xuất báo cáo Excel/PDF. |

---
# 3. ĐẶC TẢ CHI TIẾT 5 LUỒNG NGHIỆP VỤ CỐT LÕI (5 CORE BUSINESS FLOWS)

### 3.1. Luồng 1: Đặt món tại bàn (Dine-in) — BẮT BUỘC THANH TOÁN VIETQR TRƯỚC
- **Khái niệm**: Khách hàng ngồi tại bàn, tự phục vụ đặt món qua mã QR bàn và phải hoàn tất thanh toán VietQR trước khi đơn hàng được gửi vào bếp.
- **Quy trình chi tiết**:
  1. Khách hàng dùng điện thoại quét mã QR dán trên bàn (`https://smartfb.vn/table/{branchId}/{tableCode}`).
  2. Ứng dụng PWA mở trực tiếp trên trình duyệt di động, tự động định danh mã chi nhánh và số bàn.
  3. Khách hàng nhập Số điện thoại (tùy chọn). Nếu nhập: hệ thống tải thông tin thành viên, hạng thẻ, mã voucher khả dụng và danh sách món yêu thích.
  4. Khách hàng duyệt menu, chọn món, tùy biến sâu: Size (S/M/L), Mức đường (0%/30%/50%/70%/100%), Mức đá (0%/30%/50%/70%/100%), Toppings và ghi chú riêng.
  5. Khách hàng vào Giỏ hàng, kiểm tra danh sách món, chọn áp dụng Voucher nếu có.
  6. **Bước thanh toán bắt buộc (Pre-payment Gate)**:
     - Khách hàng bấm "Thanh toán VietQR".
     - Hệ thống sinh mã VietQR động kèm mã giao dịch duy nhất và số tiền chính xác.
     - Khách hàng mở app ngân hàng, quét mã và hoàn tất chuyển khoản.
     - Webhook từ PayOS/Ngân hàng bắn về Backend .NET 8 xác nhận giao dịch thành công.
     - Trạng thái đơn hàng chuyển đổi: `PendingPayment` -> `Paid` -> `Confirmed`.
  7. **Chuyển đơn vào bếp**:
     - Ngay khi trạng thái là `Paid`/`Confirmed`, SignalR `OrderHub` phát sự kiện tới màn hình KDS chi nhánh.
     - Đơn xuất hiện trên màn hình KDS kèm số bàn, thời gian chờ, công thức pha chế.
  8. **Pha chế & Phục vụ**:
     - Barista bấm "Bắt đầu làm" (`Preparing`).
     - Barista bấm "Đã xong" (`Ready`) -> SignalR bắn thông báo tới PWA của khách và màn hình nhân viên.
     - Nhân viên mang món ra bàn -> Đổi trạng thái `Served` -> `Completed`.
  9. **Đánh giá sau phục vụ**: Khách hàng nhận thông báo đánh giá 1-5 sao và tải ảnh phản hồi.

---

### 3.2. Luồng 2: Đặt hàng từ xa (QR Delivery) — ĐỊA CHỈ BẮT BUỘC & PHÍ SHIP CỐ ĐỊNH 20.000 VNĐ
- **Khái niệm**: Khách hàng đặt món giao tận nơi thông qua mã QR Delivery được in trên ấn phẩm truyền thông (standee, tờ rơi, fanpage, poster).
- **Quy trình chi tiết**:
  1. Khách hàng quét mã QR Delivery từ xa.
  2. PWA khởi chạy ở chế độ Delivery (`order_type = Delivery`).
  3. **Thu thập thông tin bắt buộc**:
     - Số điện thoại người nhận (Bắt buộc).
     - Địa chỉ giao hàng chi tiết (Bắt buộc — lưu vào trường `delivery_address`).
  4. Khách hàng duyệt menu chi nhánh gần nhất, tùy biến món và thêm vào giỏ hàng.
  5. **Tính toán chi phí & Phí giao hàng**:
     - Tổng tiền = Tiền món + Phí giao hàng cố định 20.000 VNĐ (`delivery_fee = 20000`) - Giảm giá Voucher.
  6. **Thanh toán VietQR bắt buộc (100% Không COD)**:
     - Hệ thống không hỗ trợ thanh toán tiền mặt khi nhận hàng (loại bỏ rủi ro bùng đơn).
     - Khách hàng thanh toán qua VietQR động.
     - Webhook xác nhận tiền về -> Đơn chuyển sang `Paid` -> `Confirmed`.
  7. **Chế biến & Giao vận**:
     - Đơn hiển thị trên KDS với thẻ đánh dấu nổi bật `DELIVERY`, địa chỉ và SĐT khách.
     - Bếp chuẩn bị món, đóng gói mang đi và bấm `Ready`.
     - Quản lý/Thu ngân điều phối shipper giao hàng.
     - Khi giao thành công, cập nhật trạng thái `Completed`.

---

### 3.3. Luồng 3: Mua mang đi tại quầy (Takeaway) — GIAO DIỆN NHÂN VIÊN, TÍCH ĐIỂM 10 LY & THANH TOÁN SAU
- **Khái niệm**: Khách hàng đến quầy gọi món trực tiếp. Nhân viên sử dụng Giao diện Web Staff (không dùng mã QR của khách). Khách thanh toán sau khi nhận đồ uống.
- **Quy trình chi tiết**:
  1. Khách hàng tới quầy order.
  2. Thu ngân mở phân hệ **Takeaway POS** trên Staff Web UI.
  3. **Tra cứu & Quản lý CRM**:
     - Thu ngân hỏi và nhập Số điện thoại của khách.
     - *Nếu khách mới*: Thu ngân nhập Họ tên khách -> Hệ thống tự động tạo hồ sơ CRM.
     - *Nếu khách cũ*: Hệ thống hiển thị số ly đã tích lũy (`loyalty_cups_accumulated`).
  4. **Cơ chế Loyalty 10 ly đổi 1 ly**:
     - Hệ thống kiểm tra: Cứ tích lũy đủ 10 ly (`cups % 10 == 0`), khách được tặng 1 ly miễn phí.
     - Thu ngân có thể chọn áp dụng quyền lợi đổi ly miễn phí ngay trên đơn hàng.
  5. Thu ngân chọn món, ghi nhận tùy biến theo yêu cầu của khách và bấm "Tạo đơn mang đi".
  6. Đơn hàng gửi tức thì sang KDS (`order_type = TakeAway`, trạng thái `Confirmed`).
  7. Bếp pha chế, đóng gói và bấm `Ready`.
  8. **Thanh toán sau khi nhận món (Post-payment)**:
     - Khách hàng nhận đồ uống tại quầy nhận món.
     - Khách lựa chọn phương thức thanh toán:
       * *Tiền mặt*: Thu ngân nhập số tiền khách đưa, hệ thống tính tiền thừa, thu ngân bấm "Xác nhận đã nhận tiền mặt".
       * *VietQR*: Thu ngân hiển thị mã VietQR trên màn hình phụ/tablet để khách quét, hệ thống tự động xác nhận qua webhook hoặc thu ngân xác nhận.
     - Trạng thái đơn đổi sang `Completed`.
     - Hệ thống tự động cộng dồn số ly vào tài khoản CRM của khách và ghi nhận doanh thu vào ca làm việc hiện tại.

---

### 3.4. Luồng 4: Chấm công khóa mạng WiFi (WiFi-Locked Attendance)
- **Khái niệm**: Thay thế hoàn toàn cơ chế định vị GPS 50m và mã QR động 30 giây bằng cơ chế xác thực kép: Kết nối đúng WiFi của quán + Mã định danh nhân viên.
- **Quy trình chi tiết**:
  1. Nhân viên đến quán, kết nối điện thoại/thiết bị vào mạng WiFi nội bộ của chi nhánh.
  2. Nhân viên truy cập hệ thống Smart F&B OS, vào mục "Chấm Công" (Attendance).
  3. Nhân viên quét mã QR chấm công tĩnh dán tại khu vực làm việc (hoặc bấm nút Check-in).
  4. Nhân viên nhập Mã số nhân viên (Employee Code) và mật khẩu/mã PIN cá nhân.
  5. **Cơ chế kiểm thực kép tại Backend (Dual Verification Gate)**:
     - **Kiểm tra 1 (Mạng WiFi)**: Hệ thống đối chiếu địa chỉ IP Gateway / SSID / BSSID / MAC Signature của mạng gửi request với cấu hình `branch_wifi_configs` đã lưu trong database của chi nhánh.
     - **Kiểm tra 2 (Hồ sơ nhân viên)**: Kiểm tra Mã nhân viên có hợp lệ, đang hoạt động và được phân công vào ca làm việc tại chi nhánh này hay không.
  6. **Kết quả xử lý**:
     - *Nếu cả 2 điều kiện ĐÚNG*: Hệ thống ghi nhận chấm công Vào ca (Check-in) hoặc Ra ca (Check-out), lưu dấu thời gian, tính toán đi trễ/về sớm/tăng ca.
     - *Nếu SAI mạng WiFi*: Hệ thống từ chối chấm công ngay lập tức và hiển thị thông báo lỗi: *"Vui lòng kết nối vào mạng WiFi [Tên_WiFi_Quán] tại chi nhánh để chấm công."*

---

### 3.5. Luồng 5: Hợp nhất nghiệp vụ phục vụ vào Giao diện Web (Staff Web UI)
- **Khái niệm**: Xóa bỏ hoàn toàn ứng dụng di động riêng của nhân viên (Staff App). Mọi thao tác được chuyển sang Giao diện Web chuẩn hóa responsive.
- **Các phân hệ nghiệp vụ trên Staff Web UI**:
  - **Sơ đồ bàn trực quan (Live Table Map)**: Hiển thị trạng thái các bàn (Trống, Đang có khách, Đang chờ món, Cần dọn dẹp).
  - **Trung tâm cảnh báo gọi phục vụ (Service Call Center)**: Nhận thông báo âm thanh và pop-up thời gian thực qua SignalR khi khách bấm nút "Gọi nhân viên" trên QR Menu PWA.
  - **Quầy POS Takeaway**: Tra cứu khách hàng, tạo đơn mang đi, áp dụng loyalty 10 ly, thu tiền mặt/VietQR sau khi giao món.
  - **Màn hình KDS Bếp/Bar**: Nhận đơn thời gian thực, xem công thức, đổi trạng thái món, bật tắt hết món tức thì.
  - **Màn hình Chấm công**: Check-in/Check-out nhanh cho nhân viên đầu và cuối ca.

---
# 4. DANH MỤC TÍNH NĂNG ĐƯỢC PHÁT HIỆN TỪ DOCX (COMPLETE FEATURE INVENTORY)

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|:---:|---|---|---|---|---|---|---|
| 1 | QR Ordering | QR Bàn Độc Nhất | Sinh mã QR độc nhất cho từng bàn và từng chi nhánh | `branchId`, `tableNumber` | URL định tuyến PWA kèm Token bảo mật | Báo lỗi bàn không tồn tại hoặc đã bị vô hiệu hóa | docx: §3.2.c |
| 2 | QR Ordering | QR Menu PWA Responsive | Mở menu trực tiếp trên trình duyệt điện thoại không cần cài app | HTTP Request từ QR Scan | Giao diện PWA tải nhanh, tối ưu cảm ứng | Hiển thị màn hình fallback khi mất kết nối mạng | docx: §3.2.c |
| 3 | QR Ordering | Định Danh Khách Hàng CRM | Nhập SĐT tùy chọn; tạo mới hồ sơ CRM hoặc tải lịch sử, voucher, loyalty | `phoneNumber`, `customerName` | Profile khách hàng, điểm tích lũy, danh sách voucher | Báo lỗi định dạng SĐT không hợp lệ | docx: §3.2.c |
| 4 | QR Ordering | Hiển Thị Menu Đa Dạng & Giá Chi Nhánh | Hiển thị danh mục, hình ảnh, mô tả, giá riêng từng chi nhánh, best-seller, calo, dị ứng | `branchId`, `categoryId` | Danh sách món ăn kèm trạng thái còn/hết hàng | Trả về danh sách rỗng nếu danh mục chưa có món | docx: §3.2.c |
| 5 | QR Ordering | Tùy Biến Món Sâu (Modifiers) | Chọn Size (S/M/L), Mức đường (0-100%), Mức đá (0-100%), Topping nhiều lựa chọn, ghi chú | `productId`, `sizeId`, `sugarPct`, `icePct`, `toppingIds[]`, `note` | Item cấu hình hoàn chỉnh kèm phụ phí | Chặn thêm giỏ hàng nếu thiếu tùy chọn bắt buộc (Size) | docx: §3.2.c |
| 6 | QR Ordering | Quản Lý Giỏ Hàng & Tách Loại Đơn | Quản lý giỏ hàng, chọn Dine-in hoặc Takeaway, tính tổng tiền tức thời | Danh sách items trong giỏ | Chi tiết giỏ hàng, tổng tiền tạm tính | Cảnh báo khi có món trong giỏ vừa hết hàng | docx: §3.2.c |
| 7 | QR Ordering | Cổng Thanh Toán VietQR Tự Động | Sinh mã VietQR động, lắng nghe Webhook ngân hàng và xác nhận đơn | `orderId`, `amount`, `orderCode` | Mã QR PayOS/VietQR, trạng thái thanh toán | Timeout sau 15 phút không thanh toán -> Hủy đơn | docx: §3.2.c & Request |
| 8 | QR Ordering | Đặt Hàng Giao Tận Nơi (QR Delivery) | Quét QR Delivery, nhập SĐT + Địa chỉ, cộng phí ship 20k, thanh toán VietQR trước | `phoneNumber`, `deliveryAddress`, `cartItems` | Đơn hàng Delivery hoàn tất | Từ chối nếu thiếu SĐT hoặc Địa chỉ giao hàng | docx: §3.2.b & Request |
| 9 | QR Ordering | Theo Dõi Tiến Độ Đơn Hàng | Hiển thị trạng thái chế biến thời gian thực: Đã nhận -> Đang làm -> Đã xong -> Đã phục vụ | `orderId` | Tiến độ trực quan, thời gian chờ ước tính | Thông báo lỗi kết nối SignalR và tự động reconnect | docx: §3.2.c |
| 10 | QR Ordering | Gọi Nhân Viên Phục Vụ | Khách hàng gửi yêu cầu hỗ trợ hoặc yêu cầu thanh toán từ bàn | `tableId`, `requestType` (Call/Bill) | Tín hiệu thông báo gửi tức thì tới Staff UI | Giới hạn tần suất gọi (Rate-limit 1 lần/phút) | docx: §3.2.c |
| 11 | CRM & Loyalty | Đánh Giá Món Ăn 1-5 Sao & Review | Khách chấm điểm 1-5 sao và viết nhận xét chi tiết sau khi hoàn thành đơn | `orderId`, `productId`, `rating`, `reviewText` | Bản ghi đánh giá được lưu vào hệ thống | Chặn đánh giá nếu đơn hàng chưa hoàn tất | docx: §3.2.c |
| 12 | CRM & Loyalty | Tải Ảnh Đánh Giá & Kiểm Duyệt | Cho phép khách tải ảnh thật của món ăn kèm đánh giá, hỗ trợ duyệt ảnh | File ảnh (JPEG/PNG/WEBP <= 5MB) | Ảnh được lưu trữ đám mây, trạng thái chờ duyệt | Từ chối file sai định dạng hoặc vượt quá dung lượng | docx: §3.2.c & §3.2.d |
| 13 | CRM & Loyalty | Tùy Chọn Ẩn Danh Đánh Giá | Khách chọn hiển thị tên CRM hoặc "Khách hàng ẩn danh"; ẩn hoàn toàn SĐT | `isAnonymous` (Boolean) | Tên hiển thị công khai an toàn | Không cho phép can thiệp để lộ SĐT trên UI | docx: §3.2.c & §3.2.d |
| 14 | CRM & Loyalty | Xuất Bản Đánh Giá Lên QR Menu | Đánh giá được duyệt hiển thị công khai trên menu làm bằng chứng xã hội | `reviewId`, `approvalStatus` | Review xuất hiện trên trang chi tiết món ăn | Ẩn review ngay lập tức nếu bị báo cáo vi phạm | docx: §3.2.c |
| 15 | CRM & Loyalty | Cảnh Báo Đánh Giá Thấp (<= 2 Sao) | Tự động phát chuông cảnh báo tới Quản lý chi nhánh khi có đánh giá <= 2 sao | `reviewRecord` có `rating <= 2` | Thông báo khẩn tới Manager Dashboard | Ghi log nếu quản lý không phản hồi trong 24h | docx: §3.2.c |
| 16 | CRM & Loyalty | Hồ Sơ Khách Hàng 360 | Ghi nhận lịch sử ghé thăm, tổng chi tiêu, ngày ghé gần nhất, món ưa thích | `customerId` | Dashboard chi tiết hành vi khách hàng | Bảo mật dữ liệu, chỉ Manager/Admin xem được | docx: §3.2.c |
| 17 | CRM & Loyalty | Chương Trình Tích Điểm 10 Ly | Tích lũy số ly đã mua qua các đơn hàng; đủ 10 ly tặng 1 ly miễn phí | `orderItemsCount` | Voucher đồ uống miễn phí tự động phát hành | Reset chu kỳ tích điểm sau khi đã đổi thưởng | docx: §3.2.c & Request |
| 18 | CRM & Loyalty | Phát Hành Voucher Tự Động | Cấp voucher sinh nhật, voucher tri ân và voucher giữ chân khách hàng cũ | `customerEvent` (Sinh nhật, 30 ngày không ghé) | Mã voucher gửi vào ví PWA của khách | Voucher hết hạn sẽ tự động chuyển trạng thái Expired | docx: §3.2.c |
| 19 | KDS & Kitchen | Màn Hình KDS Thời Gian Thực | Nhận đơn hàng chi nhánh tức thời qua WebSocket / SignalR | Luồng sự kiện đơn hàng mới | Bảng hiển thị đơn hàng (Ticket Board) | Tự động kết nối lại khi mất mạng và đồng bộ state | docx: §3.2.c |
| 20 | KDS & Kitchen | Hiển Thị Chi Tiết Đơn & Ưu Tiên | Hiển thị số bàn, món, tùy biến, ghi chú, bộ đếm thời gian chờ đổi màu | `orderData` | Ticket đơn hàng phân cấp màu sắc theo độ trễ | Cảnh báo nhấp nháy đỏ khi thời gian chờ > 10 phút | docx: §3.2.c |
| 21 | KDS & Kitchen | Tra Cứu Công Thức Chuẩn | Xem nhanh định lượng nguyên liệu và quy trình pha chế chuẩn của từng món | `productId` | Pop-up công thức chi tiết và lưu ý pha chế | Báo lỗi nếu món chưa được cấu hình công thức | docx: §3.2.c |
| 22 | KDS & Kitchen | Cập Nhật Trạng Thái Đơn Pha Chế | Chuyển đổi trạng thái đơn: `Preparing` -> `Ready` -> `Served` -> `Completed` | `orderId`, `targetStatus` | Cập nhật DB và phát SignalR tới mọi màn hình | Chặn chuyển trạng thái ngược hoặc bỏ qua bước | docx: §3.2.c |
| 23 | KDS & Kitchen | Gom Đơn Hàng Theo Bàn & Loại | Gom nhiều lượt gọi món của cùng một bàn hoặc gom món cùng loại để pha nhanh | `branchId`, active tickets | Danh sách món gom nhóm thông minh | Cập nhật lại danh sách gom khi có order mới | docx: §3.2.c |
| 24 | KDS & Kitchen | Khóa Hết Món Tức Thì (Out-of-Stock) | Bếp đánh dấu món hoặc nguyên liệu hết hàng, đồng bộ tức thì lên QR Menu | `productId` / `ingredientId`, `isAvailable` | Menu khách hàng ẩn/disable món ngay lập tức | Ngăn chặn khách đặt món đã bị khóa hết hàng | docx: §3.2.c |
| 25 | KDS & Kitchen | Tích Hợp In Hóa Đơn & Tem Nhãn | Gửi lệnh in hóa đơn thanh toán hoặc in tem dán ly đồ uống qua máy in nhiệt | `orderId`, `printType` (Receipt/Label) | Lệnh in ESC/POS gửi tới máy in mạng/Bluetooth | Báo lỗi kẹt giấy hoặc mất kết nối máy in | docx: §3.2.c |
| 26 | Staff Operations | Giao Diện Web Staff & Takeaway POS | Giao diện thu ngân tạo đơn mang đi, tra cứu SĐT, áp dụng tích điểm 10 ly | `phoneNumber`, `orderItems`, `paymentMethod` | Đơn Takeaway được tạo, hóa đơn in ra | Cảnh báo nếu nhập trùng thông tin khách | docx: §3.2.c & Request |
| 27 | Staff Operations | Xác Nhận Thanh Toán Sau Takeaway | Thu tiền mặt (tính tiền thừa) hoặc đưa mã VietQR, bấm xác nhận hoàn tất | `orderId`, `cashReceived` / `transRef` | Đơn hoàn tất, doanh thu cập nhật vào két ca | Chặn xác nhận nếu số tiền thu nhỏ hơn tổng đơn | docx: §3.2.c & Request |
| 28 | Staff Operations | Quản Lý Sơ Đồ Bàn Trực Quan | Xem trạng thái bàn (Trống, Có khách, Chờ món, Cần dọn), gộp bàn | `tableId`, `tableStatus` | Sơ đồ bàn cập nhật màu sắc thời gian thực | Không cho xếp khách vào bàn đang có người | docx: §3.2.c |
| 29 | Staff Operations | Chấm Công Khóa Mạng WiFi | Quét QR chấm công + nhập mã NV; kiểm tra kết nối đúng WiFi chi nhánh | `employeeCode`, `pin`, `wifiSsid`, `wifiBssid` | Ghi nhận giờ Check-in/Check-out vào ca | Từ chối chấm công nếu sai WiFi hoặc sai mã NV | docx: §3.2.c & Request |
| 30 | Branch Operations | Mở & Đóng Ca Làm Việc | Nhập tiền mặt đầu ca, kiểm đếm tiền mặt cuối ca, tính chênh lệch két tiền | `openingCash`, `actualClosingCash` | Biên bản kết ca, báo cáo chênh lệch két | Cảnh báo đỏ và bắt buộc ghi chú nếu lệch tiền | docx: §3.2.c |
| 31 | Branch Operations | Xếp Lịch & Quản Lý Ca Làm Việc | Lập lịch làm việc tuần, ghi nhận đổi ca, theo dõi đi trễ, về sớm, tăng ca | `scheduleData`, `shiftSwapRequest` | Bảng phân ca tuần và dữ liệu tổng hợp công | Cảnh báo trùng ca hoặc vi phạm số giờ tối đa | docx: §3.2.c |
| 32 | Branch Operations | Phiếu Lĩnh & Điều Chuyển Kho | Lập phiếu lĩnh nguyên liệu từ kho tổng ra quầy bar, lưu vết luân chuyển | `ingredientId`, `quantity`, `fromLoc`, `toLoc` | Phiếu xuất kho, trừ tồn kho kho lưu trữ | Chặn xuất kho nếu số lượng vượt quá tồn kho khả dụng | docx: §3.2.c |
| 33 | Branch Operations | Nhập Kho Nhà Cung Cấp | Ghi nhận hàng nhập từ NCC, đối chiếu số lượng thực nhận so với đơn mua | `poId`, `supplierName`, `receivedItems[]` | Phiếu nhập kho, tăng tồn kho chi nhánh | Cảnh báo chênh lệch số lượng thực nhận vs đặt hàng | docx: §3.2.c |
| 34 | Branch Operations | Kiểm Kê Tồn Kho & Ghi Nhận Hao Hụt | Kiểm đếm tồn kho thực tế, tính chênh lệch sổ sách, ghi nhận hủy/hao hụt | `actualStockCount[]`, `wastageReason` | Báo cáo kiểm kê, cảnh báo tồn kho bất thường | Yêu cầu giải trình khi tỷ lệ hao hụt vượt định mức | docx: §3.2.c |
| 35 | Branch Operations | Cấu Hình Chi Nhánh & Giá Bán Riêng | Quản lý sơ đồ bàn, giờ mở cửa, menu và giá bán riêng cho chi nhánh | `branchConfigData`, `priceOverrides[]` | Thiết lập vận hành chi nhánh có hiệu lực | Chặn sửa giá nếu không có quyền Manager | docx: §3.2.c |
| 36 | Branch Operations | Báo Cáo Doanh Thu & Vận Hành Ngày | Xem doanh thu, số đơn, AOV, món bán chạy, biểu đồ khung giờ cao điểm | `dateRange`, `branchId` | Báo cáo doanh thu và chỉ số vận hành chi tiết | Xử lý an toàn khi khoảng ngày không có giao dịch | docx: §3.2.c |
| 37 | Admin & Multi-Branch | Quản Trị Chi Nhánh & Phân Quyền RBAC | Quản lý danh sách chi nhánh, tài khoản nhân viên, phân quyền vai trò | `branchData`, `userData`, `rolePermissions` | Cây phân quyền và tài khoản hoạt động | Ngăn chặn truy cập chéo dữ liệu giữa các chi nhánh | docx: §3.2.c |
| 38 | Admin & Multi-Branch | Quản Lý Danh Mục & Thực Đơn Tập Trung | Tạo món mới, danh mục, hình ảnh, công thức định lượng, lịch thực đơn mùa | `categoryData`, `productData`, `recipeBOM` | Thực đơn đồng bộ toàn hệ thống | Chặn xóa món đang có trong đơn hàng hoạt động | docx: §3.2.c |
| 39 | Admin & Multi-Branch | Quản Lý Combo & Khuyến Mãi Chuỗi | Thiết lập combo món, voucher giảm giá, chính sách tích điểm toàn chuỗi | `comboData`, `voucherRuleData` | Chiến dịch marketing được kích hoạt | Chặn phát hành voucher có ngày kết thúc trước ngày bắt đầu | docx: §3.2.c |
| 40 | Admin & Multi-Branch | Báo Cáo Hợp Nhất & So Sánh P&L | Dashboard so sánh doanh thu, chi phí, tồn kho, công và lãi lỗ giữa các quán | `filterParams` (Toàn chuỗi / Chi nhánh) | Bảng so sánh P&L trực quan, biểu đồ tăng trưởng | Trả về dữ liệu 0 khi chi nhánh mới chưa có dữ liệu | docx: §3.2.c |
| 41 | Admin & Multi-Branch | Nhật Ký Kiểm Toán Bất Biến (Audit Log) | Lưu vết mọi thao tác đổi giá, hủy đơn, sửa tồn kho, xác nhận tiền, đổi quyền | `actionContext`, `userId`, `oldVal`, `newVal` | Bản ghi Audit Log không thể chỉnh sửa/xóa | Ghi log thất bại ra file backup khẩn cấp | docx: §3.2.c |
| 42 | Admin & Multi-Branch | Xuất Báo Cáo Đa Định Dạng (Excel/PDF) | Xuất báo cáo bán hàng, kho, chấm công tính lương, CRM và tài chính | `reportType`, `format` (Excel/PDF), `dateRange` | Tệp nhị phân .xlsx hoặc .pdf tải về | Báo lỗi khi dung lượng file vượt quá giới hạn bộ nhớ | docx: §3.2.c |
| 43 | Active AI | AI-1: Chatbot Tư Vấn Món RAG (ACTIVE) | Gợi ý món phù hợp dựa trên sở thích khách, dị ứng, thời tiết, xu hướng bán | Câu hỏi tự nhiên của khách, SĐT, ngữ cảnh thời tiết | Gợi ý món kèm lý giải trực quan, nút đặt nhanh | Fallback về gợi ý Top Best-seller khi AI timeout | docx: §3.2.c & §3.3 |
| 44 | Active AI | AI-2: Đề Xuất Combo Apriori (ACTIVE) | Khai phá giỏ hàng lịch sử tìm combo thường mua cùng, đề xuất chủ quán duyệt | Tập dữ liệu đơn hàng (`order_items`) | Danh sách combo đề xuất kèm Support, Confidence, Lift | Bỏ qua các tập mục không đạt ngưỡng min_support | docx: §3.2.c & §3.3 |
| 45 | Future Work AI | AI-3: Phân Tích Dữ Liệu Tự Nhiên (SCALE UP) | Hỏi đáp số liệu kinh doanh chi nhánh bằng ngôn ngữ tự nhiên (NLQ Text-to-SQL) | Câu hỏi phân tích từ Quản lý/Chủ quán | Biểu đồ trực quan và câu trả lời phân tích | Đánh dấu tính năng mở rộng (Future Work) | docx: §3.2.c & §3.2.f |
| 46 | Future Work AI | AI-4: Dự Đoán Khách Rời Bỏ Churn (SCALE UP) | Mô hình Random Forest/XGBoost dự báo khách hàng có nguy cơ rời bỏ | Dữ liệu RFM (Recency, Frequency, Monetary) | Danh sách khách có nguy cơ cao để kích hoạt ưu đãi | Đánh dấu tính năng mở rộng (Future Work) | docx: §3.2.c & §3.2.f |
| 47 | Future Work AI | AI-5: Dự Báo Nhu Cầu & Thực Đơn (SCALE UP) | Dự báo số lượng nguyên liệu và món ăn cần chuẩn bị theo ngày/thời tiết | Dữ liệu bán hàng lịch sử, lịch sự kiện, thời tiết | Kế hoạch chuẩn bị nguyên liệu dự báo | Đánh dấu tính năng mở rộng (Future Work) | docx: §3.2.c & §3.2.f |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|:---:|---|---|---|
| 1 | Dine-in Pre-Payment | Khách quét mã QR và chọn món nhưng đóng trình duyệt không quét VietQR | Đơn hàng duy trì ở trạng thái `PendingPayment` trong 15 phút. Bếp hoàn toàn KHÔNG nhận được đơn. Sau 15 phút, hệ thống tự động hủy đơn và giải phóng giỏ hàng. |
| 2 | Dine-in Payment Webhook | Tiền đã trừ ở ngân hàng nhưng Webhook bị nghẽn mạng đến chậm 2 phút | Hệ thống hỗ trợ nút "Tôi đã chuyển tiền" trên PWA để kích hoạt truy vấn trạng thái giao dịch chủ động (Polling) tới cổng PayOS, lập tức kích hoạt đơn sang `Paid` mà không bắt khách chờ. |
| 3 | QR Delivery Validation | Khách nhập địa chỉ giao hàng rỗng hoặc chỉ nhập dấu cách | Nút "Tiến hành thanh toán" bị vô hiệu hóa; form hiển thị thông báo lỗi trường bắt buộc: *"Vui lòng nhập địa chỉ giao hàng cụ thể để quán điều phối shipper"*. |
| 4 | Takeaway 10-Cup Loyalty | Khách mua 12 ly trong 1 đơn hàng và tài khoản hiện có sẵn 8 ly | Hệ thống ghi nhận 2 ly đầu tiên giúp hoàn thành mốc 10 ly -> Kích hoạt 1 voucher miễn phí có thể dùng ngay cho ly thứ 3; 9 ly còn lại được cộng dồn tiếp vào chu kỳ tích lũy mới. |
| 5 | Takeaway Post-Payment | Khách gọi món mang đi nhưng bất ngờ hủy ngang khi bếp đã bắt đầu làm | Thu ngân thực hiện thao tác "Hủy đơn mang đi" trên Staff UI, bắt buộc chọn lý do hủy; hệ thống ghi nhận hao hụt nguyên liệu vào báo cáo Wastage và ghi log Audit Trail. |
| 6 | WiFi Attendance Mismatch | Nhân viên đứng trong quán nhưng dùng 4G/5G hoặc kết nối WiFi quán cafe bên cạnh | Hệ thống phát hiện địa chỉ IP / WiFi SSID không trùng khớp với cấu hình chi nhánh -> Từ chối chấm công và thông báo tên SSID chuẩn của quán cần kết nối. |
| 7 | Out-of-Stock Concurrency | Hai khách cùng chọn ly trà đào cuối cùng tại cùng 1 giây | Hệ thống sử dụng Redis Distributed Lock / Optimistic Concurrency; khách hàng hoàn tất thanh toán trước sẽ nhận đơn thành công, khách thứ hai nhận thông báo hết món và được hoàn tiền tự động. |
| 8 | Feedback Photo Abuse | Khách cố tình tải lên file thực thi (.exe/.sh) hoặc file ảnh kích thước 50MB | Backend kiểm tra MIME type thực tế (Magic bytes) và dung lượng file; chặn tải lên ngay tại tầng Middleware và trả về mã lỗi 400 Bad Request. |
| 9 | Cash Reconciliation Variance | Tiền mặt đếm thực tế cuối ca lệch 100.000 VNĐ so với hệ thống tính toán | Hệ thống tính toán trường `variance_amount = -100000`, bắt buộc thu ngân nhập lý do giải trình chênh lệch trước khi cho phép đóng ca; gửi cảnh báo tới Manager. |
| 10 | AI Chatbot Fallback | Dịch vụ Google Gemini AI bị timeout hoặc mất kết nối mạng ngoài | Hệ thống kích hoạt Fallback Mode: Chatbot tự động trả về danh sách Top 5 món Best-Seller của chi nhánh dựa trên dữ liệu thống kê SQL mà không gây treo ứng dụng. |

---
# 5. CHI TIẾT CÁC YÊU CẦU PHI CHỨC NĂNG (NFRs)

Trích xuất trực tiếp từ Mục 3.2.d trong docx:

1. **Hiệu năng (Performance)**:
   - Thời gian phân phối đơn hàng mới, cập nhật trạng thái và cảnh báo phục vụ qua SignalR phải đạt mức thời gian thực (< 500ms).
   - Tốc độ phản hồi các thao tác duyệt menu, tùy biến giỏ hàng trên PWA di động < 1.5 giây trong giờ cao điểm.
2. **Khả năng mở rộng (Scalability)**:
   - Kiến trúc hỗ trợ từ 1 đến 10+ chi nhánh chuỗi, hàng trăm bàn đồng thời, hàng nghìn khách quét QR cùng lúc mà không nghẽn cổ chai.
   - Hỗ trợ lưu trữ và phân phối hình ảnh menu, ảnh đánh giá dung lượng lớn thông qua Cloud Object Storage.
3. **Tính sẵn sàng & Khôi phục (Availability & Recovery)**:
   - Hệ thống tự động xử lý suy giảm dịch vụ (graceful degradation) khi mất kết nối tạm thời tới bên thứ ba (PayOS, Gemini API).
   - Thiết lập quy trình tự động sao lưu cơ sở dữ liệu định kỳ (Automated Backup) và khôi phục sự cố.
4. **Bảo mật (Security)**:
   - Xác thực an toàn bằng JWT (Access Token ngắn hạn + Refresh Token xoay vòng).
   - Kiểm soát truy cập nghiêm ngặt theo vai trò (RBAC) và nguyên tắc đặc quyền tối thiểu (Least Privilege).
   - Toàn bộ dữ liệu giao tiếp mã hóa qua HTTPS/TLS; lọc dữ liệu đầu vào (FluentValidation), chống SQL Injection (EF Core Parameterized Queries), chống XSS/CSRF.
   - Cơ chế giới hạn tần suất gọi API (Rate Limiting) và bảo vệ dữ liệu bí mật bằng Environment Secrets.
   - Nhật ký kiểm toán bất biến (Audit Logging) ghi lại toàn bộ thao tác can thiệp tài chính và phân quyền.
5. **Bảo vệ quyền riêng tư (Privacy)**:
   - Bảo vệ tuyệt đối Số điện thoại khách hàng: Không bao giờ công khai SĐT trên giao diện đánh giá hay API công cộng.
   - Hỗ trợ cơ chế ẩn danh công khai ("Khách hàng ẩn danh") khi đánh giá món.
   - Chỉ người dùng có thẩm quyền quản lý (Manager/Admin) mới được phép truy xuất danh bạ CRM.
6. **Tính toàn vẹn dữ liệu (Data Integrity)**:
   - Đảm bảo tính toàn vẹn giao dịch ACID đối với toàn bộ luồng tạo đơn, trừ tồn kho, tích lũy điểm thưởng và đối soát két ca.
   - Quản lý trạng thái đơn hàng bằng Máy trạng thái xác định (Deterministic State Machine), chống tình trạng nhảy cóc trạng thái.
7. **An toàn truyền thông & Kiểm duyệt (Media Safety)**:
   - Kiểm duyệt chặt chẽ định dạng và dung lượng file ảnh upload từ khách hàng.
   - Quy trình kiểm duyệt ảnh đánh giá (Moderation Workflow): Ảnh chỉ hiển thị công khai sau khi được Quản lý chi nhánh xét duyệt, hỗ trợ nút gỡ ảnh khẩn cấp.
8. **Khả năng sử dụng & Trợ năng (Usability & Accessibility)**:
   - Giao diện PWA tối ưu cho thao tác chạm trên màn hình cảm ứng điện thoại (Touch targets >= 44px).
   - Giao diện KDS Bếp/Bar thiết kế chế độ nền tối tương phản cao (Dark Mode) để quan sát rõ ràng từ khoảng cách 2 - 3 mét trong môi trường bếp.
9. **Khả năng bảo trì & Tiêu chuẩn mã nguồn (Maintainability)**:
   - Tuân thủ cấu trúc phân tầng Clean Architecture (.NET 8) và Next.js 14 Monorepo.
   - Kiểm thử tự động (Unit Tests, Integration Tests), ghi log tập trung cấu trúc (Serilog), quy trình CI/CD chuẩn hóa.
10. **Khả năng tương tác liên hệ thống (Interoperability)**:
    - Tích hợp chuẩn hóa với cổng thanh toán VietQR / PayOS, máy in nhiệt hóa đơn ESC/POS, cổng thông báo Zalo OA / Email, API dự báo thời tiết OpenWeatherMap.
11. **Quản trị AI & Tính minh bạch (AI Governance & Explainability)**:
    - Mọi gợi ý món từ AI phải kèm theo giải thích nguyên nhân rõ ràng (ví dụ: *"Món phù hợp với thời tiết nắng nóng 35°C"*).
    - Áp dụng cơ chế kiểm soát con người (Human-in-the-loop): Các đề xuất Combo từ thuật toán Apriori/FP-Growth bắt buộc phải có sự phê duyệt của Chủ chuỗi/Quản trị viên mới được xuất bản lên menu.

---

# 6. PHÂN ĐỊNH RÕ RÀNG CÁC MODULE TRÍ TUỆ NHÂN TẠO (AI MODULES)

Theo đúng Mục 3.2.c và 3.3 trong `Smart_FB_OS_Revised_4members.docx`, dự án phân rã chính xác 2 Module AI triển khai thực tế và 3 Module AI mở rộng (Future Work):

### 6.1. Hai Module AI Chính Thức Triển Khai (ACTIVE AI MODULES)
1. **AI-1: Chatbot Tư Vấn Món & Đề Xuất Cá Nhân Hóa (Personalized Recommendation Chatbot)**:
   - **Mục tiêu**: Nghiên cứu trọng tâm của đề tài Capstone. Tự động gợi ý các món ăn/đồ uống phù hợp dựa trên sở thích cá nhân, tiền sử dị ứng, ngữ cảnh thời tiết thực tế, xu hướng bán chạy và lịch sử chi tiêu CRM.
   - **Kỹ thuật**: RAG (Retrieval-Augmented Generation) kết hợp mô hình gợi ý Hybrid (Content-based + Collaborative Filtering).
   - **Đánh giá khoa học**: Đo lường định lượng và so sánh với Baseline (Popularity / Non-personalized) bằng các chỉ số: `Precision@K`, `Recall@K`, `NDCG`, `Coverage` và `Latency`.
2. **AI-2: Khai Phá & Đề Xuất Combo Món Tự Động (Combo Discovery Engine)**:
   - **Mục tiêu**: Phân tích giỏ hàng mua sắm (Market Basket Analysis) trên dữ liệu hóa đơn lịch sử để tìm ra các cặp sản phẩm thường xuyên được mua kèm cùng nhau.
   - **Kỹ thuật**: Thuật toán khai phá luật kết hợp `Apriori` hoặc `FP-Growth`.
   - **Đánh giá kỹ thuật**: Đo lường bằng 3 chỉ số cốt lõi: Độ hỗ trợ (`Support`), Độ tin cậy (`Confidence`) và Độ nâng (`Lift`).
   - **Quản trị**: Hỗ trợ giao diện phê duyệt cho Chủ quán trước khi combo được đưa vào áp dụng.

### 6.2. Ba Module AI Định Hướng Tương Lai (SCALE UP / FUTURE WORK AI MODULES)
*Ghi chú quan trọng: Ba module này được giữ lại trong tài liệu thiết kế kiến trúc như các điểm mở rộng (Extension Points), hoàn toàn KHÔNG viết code trong phạm vi 16 tuần của Capstone:*
1. **AI-3: Truy Vấn Dữ Liệu Kinh Doanh Bằng Ngôn Ngữ Tự Nhiên (NLQ Business Analytics)**:
   - Cho phép Quản lý hỏi đáp số liệu doanh thu, chi phí chi nhánh bằng câu hỏi tiếng Việt tự nhiên (Text-to-SQL).
2. **AI-4: Dự Đoán Khách Hàng Rời Bỏ (Customer Churn Prediction)**:
   - Sử dụng mô hình học máy phân loại (Random Forest / XGBoost) dựa trên chỉ số RFM để dự báo khách hàng có nguy cơ ngừng ghé quán.
3. **AI-5: Trí Tuệ Thực Đơn & Dự Báo Nhu Cầu Nguyên Liệu (Menu Intelligence & Demand Forecasting)**:
   - Dự báo nhu cầu tiêu thụ đồ uống và nguyên liệu theo ngày/tuần kết hợp yếu tố mùa vụ và thời tiết.

---
# 7. MÔ HÌNH DỮ LIỆU ĐẶC TẢ TỪ DOCX (DATABASE ENTITIES & ATTRIBUTES)

Dựa trên toàn bộ các luồng nghiệp vụ được mô tả trong docx, hệ thống bao gồm 25 thực thể dữ liệu chuẩn hóa:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          DANH SÁCH 25 THỰC THỂ DỮ LIỆU TRỌNG YẾU                                 │
├──────────────────────────────────┬─────────────────────────────────┬─────────────────────────────┤
│ 1. branches                      │ 10. product_options             │ 19. order_items             │
│ 2. branch_wifi_configs           │ 11. product_option_items        │ 20. payments                │
│ 3. tables                        │ 12. recipes                     │ 21. vouchers                │
│ 4. users (employees)             │ 13. recipe_ingredients          │ 22. combos                  │
│ 5. attendances (WiFi-locked)     │ 14. ingredients                 │ 23. combo_items             │
│ 6. work_shifts (cash drawers)    │ 15. inventory_transactions      │ 24. customer_reviews        │
│ 7. categories                    │ 16. supplier_receipts           │ 25. audit_logs              │
│ 8. products                      │ 17. customers (CRM)             │                             │
│ 9. branch_product_prices         │ 18. orders                      │                             │
└──────────────────────────────────┴─────────────────────────────────┴─────────────────────────────┘
```

### Bảng Chi Tiết Cấu Trúc Thực Thể Dữ Liệu:

| STT | Tên Bảng (Entity) | Các Thuộc Tính Cốt Lõi (Attributes) | Ý Nghĩa Nghiệp Vụ & Ràng Buộc Khóa |
|:---:|---|---|---|
| 1 | `branches` | `id` (UUID), `name`, `code`, `address`, `phone`, `operating_hours`, `is_active`, `created_at` | Thông tin chi nhánh thuộc chuỗi F&B. |
| 2 | `branch_wifi_configs` | `id` (UUID), `branch_id` (FK), `ssid`, `bssid_mac`, `gateway_ip`, `is_active` | **Cấu hình mạng WiFi chi nhánh dùng cho chấm công WiFi-locked**. |
| 3 | `tables` | `id` (UUID), `branch_id` (FK), `table_number`, `zone_name`, `qr_code_token`, `status`, `is_active` | Bàn ăn tại chi nhánh và mã định danh QR bàn. |
| 4 | `users` | `id` (UUID), `branch_id` (FK), `employee_code`, `full_name`, `phone`, `email`, `password_hash`, `role` (Admin/Manager/Cashier/Barista), `is_active` | Tài khoản nhân viên và người dùng hệ thống. |
| 5 | `attendances` | `id` (UUID), `employee_id` (FK), `branch_id` (FK), `check_in_time`, `check_out_time`, `wifi_ssid_used`, `wifi_bssid_used`, `status` (OnTime/Late/Overtime), `notes` | **Bản ghi chấm công khóa theo WiFi chi nhánh**. |
| 6 | `work_shifts` | `id` (UUID), `branch_id` (FK), `employee_id` (FK), `opened_at`, `closed_at`, `opening_cash_amount`, `closing_cash_amount_system`, `closing_cash_amount_actual`, `variance_amount`, `status`, `notes` | Ca làm việc và đối soát két tiền mặt đầu/cuối ca. |
| 7 | `categories` | `id` (UUID), `name`, `display_order`, `icon_url`, `is_active` | Danh mục món (Cà phê, Trà sữa, Bánh ngọt...). |
| 8 | `products` | `id` (UUID), `category_id` (FK), `name`, `code`, `description`, `image_url`, `base_price`, `calories`, `allergens`, `is_available`, `is_bestseller` | Danh mục sản phẩm/đồ uống dùng chung. |
| 9 | `branch_product_prices` | `id` (UUID), `branch_id` (FK), `product_id` (FK), `price_override`, `is_available` | Thiết lập giá bán và trạng thái còn/hết riêng từng quán. |
| 10 | `product_options` | `id` (UUID), `product_id` (FK), `option_name` (Size/Đường/Đá/Topping), `option_type` (Single/Multi), `is_required` | Nhóm tùy chọn bổ sung cho món. |
| 11 | `product_option_items` | `id` (UUID), `product_option_id` (FK), `item_name`, `extra_price`, `is_available` | Giá trị cụ thể của tùy chọn (Size L +10k, Thạch +5k). |
| 12 | `recipes` | `id` (UUID), `product_id` (FK), `preparation_instructions`, `standard_prep_time_minutes` | Công thức pha chế chuẩn hóa của đồ uống. |
| 13 | `recipe_ingredients` | `id` (UUID), `recipe_id` (FK), `ingredient_id` (FK), `quantity_required`, `unit` | Định lượng nguyên liệu chi tiết cho từng công thức. |
| 14 | `ingredients` | `id` (UUID), `name`, `code`, `unit`, `minimum_stock_threshold`, `current_stock_quantity`, `cost_price` | Nguyên liệu pha chế (Hạt cà phê, Sữa tươi, Trà...). |
| 15 | `inventory_transactions` | `id` (UUID), `branch_id` (FK), `ingredient_id` (FK), `movement_type` (Requisition/Receipt/Wastage/Stocktake), `quantity`, `reference_id`, `created_by` | Lịch sử luân chuyển và biến động kho nguyên liệu. |
| 16 | `supplier_receipts` | `id` (UUID), `branch_id` (FK), `supplier_name`, `po_number`, `received_at`, `total_cost`, `received_by`, `notes` | Phiếu nhập hàng từ nhà cung cấp vào kho. |
| 17 | `customers` | `id` (UUID), `phone_number` (Unique), `full_name`, `membership_tier`, `loyalty_cups_accumulated`, `lifetime_spend`, `total_visits`, `last_visit_at` | **Hồ sơ CRM khách hàng và số ly tích lũy (10 ly = 1 ly)**. |
| 18 | `orders` | `id` (UUID), `order_code` (Unique), `branch_id` (FK), `table_id` (FK, Nullable), `customer_id` (FK, Nullable), `order_type` (ENUM: `DineIn`, `TakeAway`, `Delivery`), `order_status` (ENUM: `PendingPayment`, `Paid`, `Confirmed`, `Preparing`, `Ready`, `Served`, `Completed`, `Cancelled`), `delivery_address` (TEXT, Nullable), `delivery_fee` (DECIMAL, 20.000 cho Delivery, 0 cho đơn khác), `subtotal_amount`, `discount_amount`, `total_amount`, `voucher_id` (FK, Nullable), `customer_notes`, `created_at` | **Đơn hàng trung tâm với đầy đủ 3 loại đơn & địa chỉ/phí ship**. |
| 19 | `order_items` | `id` (UUID), `order_id` (FK), `product_id` (FK), `quantity`, `unit_price`, `subtotal_price`, `customization_json`, `item_status` | Chi tiết từng món trong đơn hàng và JSON tùy chọn. |
| 20 | `payments` | `id` (UUID), `order_id` (FK), `payment_method` (VietQR/Cash), `payment_status` (Pending/Success/Failed), `amount`, `transaction_reference`, `paid_at`, `confirmed_by_employee_id` | Bản ghi giao dịch thanh toán VietQR / Tiền mặt. |
| 21 | `vouchers` | `id` (UUID), `code` (Unique), `title`, `discount_type` (Percent/Amount/FreeItem), `discount_value`, `minimum_order_amount`, `max_discount_amount`, `start_date`, `end_date`, `is_active` | Mã giảm giá và khuyến mãi. |
| 22 | `combos` | `id` (UUID), `name`, `combo_price`, `discount_percentage`, `is_ai_suggested`, `approval_status` (Pending/Approved/Rejected), `approved_by` (FK) | Gói combo sản phẩm (do AI gợi ý hoặc tạo thủ công). |
| 23 | `combo_items` | `id` (UUID), `combo_id` (FK), `product_id` (FK), `quantity` | Các sản phẩm cấu thành combo. |
| 24 | `customer_reviews` | `id` (UUID), `order_id` (FK), `customer_id` (FK), `branch_id` (FK), `product_id` (FK), `rating` (1-5), `review_text`, `image_urls` (JSON), `is_anonymous`, `is_approved`, `manager_response` | Đánh giá sao, nhận xét và hình ảnh phản hồi. |
| 25 | `audit_logs` | `id` (UUID), `user_id` (FK), `action_type` (PriceChange/OrderCancel/StockAdjust/ManualPayment/PermissionChange), `entity_name`, `entity_id`, `old_values_json`, `new_values_json`, `ip_address`, `created_at` | **Nhật ký kiểm toán bảo mật bất biến**. |

---

# 8. KẾT LUẬN & HƯỚNG DẪN ĐỒNG BỘ BỘ TÀI LIỆU DỰ ÁN

Bản bóc tách đặc tả này xác lập **chuẩn mực nội dung duy nhất** cho đợt đại tu toàn bộ tài liệu dự án Smart F&B OS. Mọi tài liệu con cần tuân thủ triệt để các nguyên tắc sau:
1. **Dine-in**: Bắt buộc luồng *Thanh toán VietQR trước -> Bếp mới nhận đơn*. Tuyệt đối không còn thuật ngữ "yêu cầu bill" hay "thanh toán sau" trong luồng Dine-in.
2. **Delivery**: Bắt buộc có loại đơn `Delivery`, trường `delivery_address`, phí cố định 20.000 VNĐ (`delivery_fee = 20000`), thanh toán VietQR trước 100%.
3. **Takeaway**: Thực hiện trên Giao diện Web Staff (không có QR), tra cứu SĐT, tạo CRM, tích lũy 10 ly đổi 1 ly, thanh toán sau khi nhận món.
4. **Chấm công**: Khóa theo WiFi quán (`branch_wifi_configs`), loại bỏ hoàn toàn GPS 50m và QR động 30 giây.
5. **Staff App**: Loại bỏ hoàn toàn khỏi kiến trúc và thay thế bằng Giao diện Web Staff / KDS.
6. **AI**: Khẳng định rõ 2 Module Active (AI-1 RAG Chatbot, AI-2 Apriori Combo) và 3 Module Future Work (AI-3 NLQ Analytics, AI-4 Churn, AI-5 Menu Intelligence).
