# 📋 BÁO CÁO ĐẶC TẢ SỰ THẬT TOÀN DIỆN (SPECIFICATION MINING REPORT)
## Smart F&B Operating System — AI-Powered QR Order & Management Platform
> **Mã đặc tả:** SPEC-MINER-TRUTH-V2
> **Nguồn sự thật tối thượng (Primary Truth):** `Smart_FB_OS_Revised_4members.docx` (Text extract: `d:\\Idea_DoAn\\temp_revised_content.txt`)
> **Tài liệu đối chiếu bổ trợ (Directives & Clarifications):** `ORIGINAL_REQUEST.md` (Follow-up chốt nghiệp vụ 2026-08-22)
> **Phạm vi thực thi:** Đồ án Capstone 16 tuần (08 Sprints) — Nhóm 4 Kỹ sư Phần mềm (2 Backend + 2 Frontend)
> **Nguyên tắc đóng băng:** Zero Placeholders, Zero Unverified Claims, Full Evidence Traceability.

---

# 1. TỔNG QUAN DỰ ÁN & KIỂM TOÁN NGUỒN SỰ THẬT

## 1.1 Thông tin Dự án
- **Tên tiếng Anh:** Smart F&B OS - AI-Powered QR Order & Management Platform
- **Tên tiếng Việt:** Smart F&B OS - Nền tảng quản lý và vận hành quán cà phê thông minh tích hợp AI và đặt món QR
- **Mục tiêu cốt lõi:** Thay thế hoàn toàn hệ thống máy POS cồng kềnh, đắt đỏ và các quy trình ghi sổ/chấm công/kiểm kê thủ công trong quán cà phê và chuỗi F&B bằng một nền tảng Web-First duy nhất, ứng dụng AI hỗ trợ tư vấn và tối ưu doanh số.
- **Tech Stack chuẩn hóa:**
  - **Backend:** .NET 8 Web API, Clean Architecture (Domain, Application, Infrastructure, WebAPI), MediatR CQRS, FluentValidation, EF Core 8.
  - **Frontend:** Next.js 14 App Router Monorepo, TypeScript, Tailwind CSS, Shadcn UI, TanStack Query.
  - **Cơ sở dữ liệu:** PostgreSQL 16 (25 thực thể chuẩn hóa 3NF, quan hệ toàn vẹn ACID).
  - **Bộ nhớ đệm & Khóa:** Redis 7 (Cache-aside, Distributed Locks, SignalR Backplane).
  - **Thời gian thực:** SignalR WebSockets (4 Hubs: OrderHub, KitchenHub, PaymentHub, NotificationHub).
  - **Trí tuệ Nhân tạo:** Google Gemini 1.5 Flash SDK (RAG Chatbot) + Thuật toán Apriori/FP-Growth (Khai phá Combo).
  - **Tích hợp thanh toán:** PayOS / VietQR Gateway qua Webhook bảo mật.

## 1.2 Kết quả Kiểm toán Nguồn Sự Thật (Source of Truth Audit)
1. **Nghiệp vụ Dine-In:** Docx gốc mô tả quy trình đặt món không cần trả trước trực tuyến, sau đó khách yêu cầu hóa đơn và thanh toán tiền mặt/VietQR kèm xác nhận của nhân viên. ORIGINAL_REQUEST.md làm rõ và chuẩn hóa thành **2 nhánh thanh toán song song**: (A) VietQR thanh toán trước (Bếp mới nhận đơn) và (B) Tiền mặt thanh toán sau (Bếp nhận ngay, phục vụ kèm hóa đơn có in QR VietQR).
2. **Nghiệp vụ Delivery (Mới 100%):** Bổ sung kênh QR Delivery riêng (poster/fanpage/web), bắt buộc nhập SĐT + Địa chỉ, cộng phí ship cố định **20.000 VNĐ**, thanh toán **100% VietQR trả trước** (No COD).
3. **Nghiệp vụ Takeaway:** Loại bỏ QR Takeaway cho khách; Nhân viên thu ngân thao tác trực tiếp trên **Giao diện Web POS Quầy**, tra cứu SĐT CRM, áp dụng chính sách **Tích 10 ly tặng 1 ly miễn phí** (CHỈ áp dụng cho Takeaway), thu tiền sau (Tiền mặt/VietQR).
4. **Nghiệp vụ Chấm công:** Bỏ hoàn toàn GPS và mã QR 30 giây; Chấm công **Khóa Mạng WiFi (WiFi-locked)** — Nhân viên kết nối WiFi quán (kiểm tra BSSID/IP Subnet) + Nhập Mã NV trên Web.
5. **Loại bỏ Staff Mobile App:** 100% nghiệp vụ nhân viên (KDS, POS Quầy, Sơ đồ bàn, Chấm công, Gọi phục vụ) chuyển sang Web Responsive.
6. **XÓA HOÀN TOÀN C-23 & C-24:** Tính năng chia sẻ MXH (`C-23`) và Push thông báo khuyến mãi PWA (`C-24`) bị loại bỏ triệt để, không xuất hiện ở bất kỳ đâu, kể cả Future Work.
7. **Admin Full CRUD:** Chủ chuỗi có toàn quyền quản trị sản phẩm (Tạo/Sửa/Xóa/Thay thế), Combo, Upload ảnh, Giá chi nhánh, Khóa 86, Danh mục, Menu Mùa.

---

# 2. BẢNG DANH MỤC TÍNH NĂNG ĐƯỢC PHÁT HIỆN (FEATURES DISCOVERED)

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| **C-01** | Customer | Quét QR Bàn Tự Động | Nhận diện chi nhánh và số bàn từ tham số URL mã QR bàn để mở đúng menu. | URL Param: `branch_id`, `table_id`, `signature` | Chuyển hướng vào trang Menu đúng bàn & chi nhánh. | Mã QR sai chữ ký/bàn bị khóa -> Báo lỗi bàn không hợp lệ. | Docx §3.2.c & Request |
| **C-02** | Customer | Duyệt Menu Đa Dạng | Xem danh mục món, ảnh, mô tả, trạng thái còn/hết, nhãn best-seller, giá chi nhánh. | `branch_id`, `category_id` | Danh sách món ăn kèm trạng thái và giá chi nhánh. | Chi nhánh không tồn tại -> Báo lỗi 404, fallback chi nhánh chính. | Docx §3.2.c |
| **C-03** | Customer | Tùy Biến Món Sâu | Khách chọn Size (S/M/L), mức Đường (0-100%), Đá (0-100%), Topping đính kèm. | `product_id`, `size_id`, `sugar_level`, `ice_level`, `toppings[]` | Cấu hình món tùy biến được định giá và đưa vào giỏ. | Topping hết hàng -> Disable topping, cảnh báo khách chọn lại. | Docx §3.2.c |
| **C-04** | Customer | Ghi Chú Đơn Hàng | Nhập ghi chú tự do cho pha chế (ví dụ: 'ít sữa đặc', 'không lấy ống hút nhựa'). | Chuỗi text ghi chú (tối đa 200 ký tự) | Ghi chú đính kèm từng dòng món trong giỏ hàng. | Quá 200 ký tự -> Cắt chuỗi hoặc báo lỗi độ dài. | Docx §3.2.c |
| **C-05** | Customer | Quản Lý Giỏ Hàng | Xem danh sách món đã chọn, tăng/giảm số lượng, xóa món, tính tổng tiền tức thời. | Thao tác trên `cart_items[]` | Tổng giá trị giỏ hàng được cập nhật thời gian thực. | Giỏ hàng rỗng khi bấm đặt -> Báo lỗi 'Giỏ hàng đang trống'. | Docx §3.2.c |
| **C-06** | Customer | **Dine-In Nhánh A: VietQR Trả Trước** | Khách chọn VietQR -> Sinh mã VietQR động -> Khách quét chuyển khoản -> Bếp mới nhận đơn. | `order_id`, `amount`, `payment_method = VIETQR` | Mã VietQR động kèm luồng SignalR đón kết quả `Paid`. | Không thanh toán sau 10 phút -> Đơn tự động hủy (Expired). | Request Follow-up & Docx |
| **C-07** | Customer | **Dine-In Nhánh B: Tiền Mặt Trả Sau** | Khách chọn Tiền mặt -> Đơn vào bếp ngay -> NV phục vụ kèm hóa đơn có QR -> Khách trả mặt/quét QR -> NV xác nhận. | `order_id`, `payment_method = CASH` | Đơn tạo ở trạng thái `Confirmed`, gửi KDS ngay. | Bàn đang có đơn chưa hoàn tất -> Gom vào phiên bàn. | Request Follow-up & Docx |
| **C-08** | Customer | **Đặt Hàng QR Delivery** | Quét QR Delivery -> Nhập SĐT + Địa chỉ bắt buộc -> Phí ship 20k -> 100% VietQR trả trước. | `recipient_name`, `phone`, `delivery_address`, `fee = 20000` | Đơn Delivery tạo ở trạng thái `PendingPayment`. | Địa chỉ rỗng hoặc SĐT sai -> Validate form chặn submit. | Request Core Change 2 |
| **C-09** | Customer | Theo Dõi Tiến Độ Đơn Hàng | Theo dõi trạng thái đơn hàng thời gian thực qua SignalR (`Preparing` -> `Ready` -> `Served`). | `order_id` qua SignalR OrderHub | Thanh tiến trình và thông báo trạng thái cập nhật tức thì. | Mất kết nối WebSocket -> Tự động kích hoạt cơ chế Polling. | Docx §3.2.c |
| **C-10** | Customer | Đếm Ngược Thời Gian Pha Chế | Hiển thị thời gian chờ dự kiến đếm ngược dựa trên hàng đợi bếp KDS. | `queue_position`, `estimated_minutes` | Đồng hồ đếm ngược phút/giây trên PWA. | Bếp dồn tải -> Cập nhật tăng thời gian ước tính. | Docx §3.2.c |
| **C-11** | Customer | Nhận Diện Khách CRM Qua SĐT | Nhập SĐT để hệ thống nhận diện hồ sơ thành viên, lịch sử gọi món và số ly tích lũy. | `phone_number` | Tên khách, số ly tích lũy (`CupBalance`), voucher khả dụng. | SĐT chưa có trong DB -> Tự động tạo hồ sơ khách mới. | Docx §3.2.c |
| **C-12** | Customer | Áp Dụng Mã Voucher | Nhập mã giảm giá hoặc chọn voucher ưu đãi để giảm trừ trực tiếp vào hóa đơn. | `voucher_code`, `order_total` | Số tiền chiết khấu được trừ vào tổng bill thanh toán. | Voucher hết hạn/không đủ điều kiện -> Báo lỗi chi tiết. | Docx §3.2.c |
| **C-13** | Customer | **AI-1: Chatbot Tư Vấn RAG Gemini** | Chat bằng ngôn ngữ tự nhiên, AI tư vấn món dựa trên thời tiết, calo, dị ứng và CRM. | Câu hỏi tự nhiên của khách (text) | Câu trả lời kèm gợi ý 2-3 món và nút 'Thêm vào giỏ'. | API AI lỗi/timeout -> Fallback gợi ý danh sách Best-Seller. | Docx §3.2.c AI-1 & Research |
| **C-14** | Customer | Xem Món Best-Seller & Món Mới | Xem danh sách món bán chạy nhất và món mới theo thống kê đơn hàng chi nhánh. | `branch_id` | Danh mục món ăn nổi bật kèm badge Best-Seller. | Không có dữ liệu bán -> Hiển thị món mặc định của Admin. | Docx §3.2.c |
| **C-15** | Customer | Gọi Nhân Viên Hỗ Trợ Tại Bàn | Bấm chuông gọi phục vụ trên PWA kèm lý do (lấy nước, dọn bàn, giấy ăn, thanh toán). | `table_id`, `call_reason` | Tín hiệu chuông và pop-up phát tức thì trên Web Staff/KDS. | Khách spam gọi liên tục -> Giới hạn tần suất 60s/lần. | Docx §3.2.c |
| **C-16** | Customer | Đánh Giá Món & Sao Trải Nghiệm | Chấm 1-5 sao và viết bình luận sau khi hoàn tất đơn hàng. | `order_id`, `rating_stars (1-5)`, `comment` | Ghi nhận feedback, cập nhật điểm trung bình món ăn. | Rating <= 2 sao -> Tự động kích hoạt alert khẩn cấp Quản lý. | Docx §3.2.c Feedback |
| **C-17** | Customer | Tải Ảnh Đánh Giá Thực Tế | Tải 1-3 hình ảnh chụp thực tế món ăn từ thiết bị di động đính kèm đánh giá. | Files ảnh (JPEG/PNG/WebP, <= 5MB) | Ảnh được lưu trữ trên Object Storage và chờ duyệt. | File độc hại/quá dung lượng -> Báo lỗi từ chối upload. | Docx §3.2.c Feedback |
| **C-18** | Customer | Tùy Chọn Đánh Giá Ẩn Danh | Khách chọn ẩn danh tính khi đánh giá để bảo vệ quyền riêng tư cá nhân. | Boolean `is_anonymous = true` | Tên hiển thị thành `K***h h**g`, giấu SĐT công khai. | Hệ thống vẫn lưu ID nội bộ để phục vụ đối soát khiếu nại. | Docx §3.2.c Privacy |
| **C-19** | Customer | Xem Thành Phần Dị Ứng & Calo | Xem cảnh báo thành phần gây dị ứng (sữa, hạt, gluten) và bảng tính calo ước tính. | `product_id` | Chi tiết dinh dưỡng và cảnh báo sức khỏe hiển thị trên modal. | Món chưa cập nhật BOM -> Hiển thị 'Đang cập nhật'. | Docx §3.2.c |
| **C-20** | Customer | Đặt Lại Nhanh Món Yêu Thích | Xem lịch sử đơn hàng cũ và bấm 1 chạm để thêm toàn bộ món cũ vào giỏ. | `customer_id`, `previous_order_id` | Toàn bộ món và tùy biến cũ được nạp lại vào giỏ hàng. | Có món cũ hiện đang hết hàng -> Cảnh báo bỏ qua món hết. | Docx §3.2.c |
| **C-21** | Customer | Xem Hóa Đơn Điện Tử VAT | Xem chi tiết hóa đơn số hóa kèm mã tra cứu và chi tiết thuế. | `order_id` | Màn hình hóa đơn điện tử chuẩn định dạng, hỗ trợ tải ảnh. | Đơn chưa hoàn tất -> Không cho xuất hóa đơn cuối. | Docx §3.2.c |
| **C-22** | Customer | Nhận Thông Báo Món Sẵn Sàng | Nhận thông báo âm thanh và hiệu ứng rung trên PWA khi Barista bấm Ready. | Event SignalR `OrderReady` | Màn hình PWA đổi màu và phát âm thanh báo khách nhận món. | Khách tắt tab PWA -> Không nhận được WebSocket trực tiếp. | Docx §3.2.c |
| **S-01** | Staff | Màn Hình KDS Nhận Đơn Real-Time | Nhận đơn hàng mới qua SignalR WebSocket tức thời (Dine-in VietQR đã Paid, Tiền mặt Confirmed). | Event `NewOrderForKitchen` từ SignalR | Đơn xuất hiện trên KDS cột 'Chờ pha chế' kèm âm báo. | Mất mạng -> KDS tự động reconnect và fetch lại queue. | Docx §3.2.c KDS |
| **S-02** | Staff | Hiển Thị Chi Tiết & Công Thức BOM | Xem chi tiết Size, Đường, Đá, Topping, Ghi chú và định lượng ml/gam pha chế chuẩn. | `order_id` | Thẻ đơn hàng mở rộng với định lượng chi tiết từng món. | Món không có BOM -> Hiển thị công thức mặc định. | Docx §3.2.c KDS |
| **S-03** | Staff | Cập Nhật Trạng Thái Pha Chế | Barista chuyển trạng thái đơn (`Preparing` -> `Ready` -> `Served`/`Completed`) bằng 1 chạm. | `order_id`, `target_status` | Cập nhật database và phát SignalR tới PWA khách hàng. | Chuyển sai luồng trạng thái -> State Machine từ chối. | Docx §3.2.c KDS |
| **S-04** | Staff | Phân Loại & Gom Đơn (Batching) | Gom các món cùng loại của nhiều đơn hàng đang chờ để pha chế đồng loạt tối ưu thời gian. | Filter mode: 'Theo Bàn' hoặc 'Theo Món' | Danh sách gom món (ví dụ: '5 Cà phê muối cần làm ngay'). | Đơn bị hủy -> Tự động trừ khỏi số lượng batching. | Docx §3.2.c KDS |
| **S-05** | Staff | Khóa Hết Món Tức Thì (86-Toggle) | Barista bật/tắt trạng thái hết hàng của món ngay trên KDS khi quầy bar hết nguyên liệu. | `product_id`, `is_available = false` | Cập nhật DB và phát SignalR khóa món trên toàn bộ QR Menu. | Quản lý nhận cảnh báo nguyên liệu cạn kiệt. | Docx §3.2.c KDS |
| **S-06** | Staff | In Hóa Đơn & Tem Dán Ly ESC/POS | Lệnh in tự động hoặc in lại hóa đơn tính tiền và tem dán ly qua máy in nhiệt LAN/USB. | `order_id`, `printer_ip` | Máy in nhiệt in hóa đơn/tem dán ly có mã vạch và thông tin. | Máy in kẹt giấy/mất mạng LAN -> Báo lỗi trên Web Staff. | Docx §3.2.c Staff |
| **S-07** | Staff | **Web POS Quầy Takeaway** | Thu ngân tạo đơn mang về trực tiếp cho khách đến quầy (không dùng mã QR). | `products[]`, `modifiers[]`, `customer_phone` | Tạo đơn hàng `OrderType = TakeAway` đẩy xuống KDS. | Khách đổi ý hủy món trước khi làm -> Cho phép hủy có log. | Request Core Change 3 |
| **S-08** | Staff | **Tra Cứu CRM & Tích 10 Ly Quầy** | Nhập SĐT khách tại quầy, hiển thị số ly tích lũy (x/10), áp dụng tặng ly thứ 11 miễn phí. | `customer_phone` | Hiển thị hồ sơ CRM, số ly hiện có, nút áp dụng ly miễn phí. | Khách chưa có hồ sơ -> Nhập tên tạo nhanh tài khoản CRM. | Request Core Change 3 |
| **S-09** | Staff | **Thu Tiền Sau Cho Takeaway** | Thu tiền mặt (tự động tính tiền thừa) hoặc xuất mã VietQR thanh toán sau tại quầy. | `payment_method`, `cash_tendered` | Ghi nhận thanh toán, mở két tiền mặt, in hóa đơn kết thúc. | Tiền khách đưa nhỏ hơn tổng bill -> Cảnh báo thiếu tiền. | Request Core Change 3 |
| **S-10** | Staff | Quản Lý Sơ Đồ Bàn Trực Quan | Xem trạng thái các bàn (Trống - Xanh, Có khách - Vàng, Cần dọn - Đỏ) trên Web Staff. | `branch_id` | Sơ đồ mặt bằng chi nhánh cập nhật trạng thái thời gian thực. | Khách chuyển bàn -> Cho phép thao tác đổi bàn trên Web. | Docx §3.2.c Staff |
| **S-11** | Staff | Nhận Cảnh Báo Gọi Phục Vụ | Nhận pop-up và âm thanh khi khách bấm chuông gọi từ bàn; bấm 'Đã xử lý' để tắt. | Event SignalR `ServiceCallAlert` | Banner cảnh báo nhấp nháy trên Web Staff POS và KDS. | Không có NV nhận sau 3 phút -> Đổi màu cảnh báo đỏ. | Docx §3.2.c Staff |
| **S-12** | Staff | **Chấm Công Khóa Mạng WiFi** | Chấm công vào/ra ca trên Web khi kết nối đúng WiFi quán (BSSID/IP) + Nhập Mã NV. | `employee_code`, `client_ip`, `bssid` | Ghi nhận bản ghi chấm công hợp lệ vào ca làm việc. | Dùng 4G/WiFi lạ bên ngoài -> Hệ thống từ chối chấm công. | Request Core Change 4 |
| **S-13** | Staff | **Xác Nhận Thu Tiền Dine-In Nhánh B** | Nhân viên mang món ra bàn kèm hóa đơn có QR, thu tiền mặt hoặc xác nhận khách đã quét QR. | `order_id`, `payment_method`, `staff_id` | Cập nhật đơn sang `Paid`, giải phóng trạng thái bàn. | Khách không thanh toán -> Báo sự cố lên Quản lý chi nhánh. | Request Follow-up |
| **M-01** | Manager | Mở Ca Làm Việc Đầu Ngày | Khởi tạo ca trực mới, đếm và nhập số tiền mặt lẻ ban đầu bàn giao trong két. | `shift_id`, `opening_cash`, `staff_ids[]` | Ca làm việc chuyển trạng thái `Open`. | Ca trước chưa đóng -> Chặn không cho mở ca mới. | Docx §3.2.c Branch |
| **M-02** | Manager | Kết Ca & Đối Soát Két Tiền Mặt | Kiểm đếm tiền mặt thực tế cuối ca, hệ thống tính toán chênh lệch thừa/thiếu tự động. | `actual_cash_counted`, `shift_notes` | Báo cáo chênh lệch két (Z-Report), khóa sổ ca (`Closed`). | Chênh lệch > 50.000đ -> Bắt buộc nhập lý do giải trình. | Docx §3.2.c Branch |
| **M-03** | Manager | Lập Lịch Phân Ca & Duyệt Đổi Ca | Phân chia ca trực tuần cho nhân viên (Barista/Thu ngân) và phê duyệt yêu cầu đổi ca. | `schedule_matrix[]`, `swap_request_id` | Bảng phân ca tuần được phát hành cho nhân viên. | Trùng ca/vượt giờ quy định -> Cảnh báo vi phạm chính sách. | Docx §3.2.c Branch |
| **M-04** | Manager | Giám Sát Bảng Chấm Công WiFi | Xem nhật ký chấm công thời gian thực, quản lý đi trễ, về sớm, duyệt giải trình công bù. | `branch_id`, `date_range` | Bảng tổng hợp công chi nhánh chi tiết từng nhân viên. | Quản lý sửa công thủ công -> Ghi log kiểm toán bắt buộc. | Docx §3.2.c Branch |
| **M-05** | Manager | Lập Phiếu Xuất Kho Quầy Bar | Xuất nguyên liệu từ kho lưu trữ ra quầy bar phục vụ pha chế trong ngày. | `ingredient_id`, `quantity`, `export_reason` | Giảm tồn kho lưu trữ, tăng tồn kho khả dụng tại quầy bar. | Xuất vượt tồn kho thực tế -> Báo lỗi không đủ tồn kho. | Docx §3.2.c Branch |
| **M-06** | Manager | Nhập Kho Từ Nhà Cung Cấp | Nhập nguyên liệu mua từ NCC, kiểm đếm số lượng vs đơn mua, chụp ảnh hóa đơn đính kèm. | `supplier_id`, `items[]`, `invoice_photo` | Lưu phiếu nhập kho, tăng tồn kho và cập nhật giá vốn. | Hàng hỏng/sai quy cách -> Lập biên bản trả hàng NCC. | Docx §3.2.c Branch |
| **M-07** | Manager | Kiểm Kê Kho & Xử Lý Hao Hụt | Kiểm kê định kỳ tồn kho thực tế, đối chiếu số dư phần mềm, lập biên bản hao hụt. | `counted_stock[]`, `spoilage_reason` | Biên bản kiểm kê ghi nhận tỷ lệ hao hụt, điều chỉnh số dư. | Hao hụt vượt định mức 3% -> Tự động alert lên Chủ chuỗi. | Docx §3.2.c Branch |
| **M-08** | Manager | Cấu Hình Sơ Đồ Bàn & Giá Chi Nhánh | Bật/tắt bàn phục vụ, sắp xếp vị trí bàn trên bản đồ, điều chỉnh giá đặc thù chi nhánh. | `table_layout`, `branch_price_overrides` | Cập nhật cấu hình mặt bằng và bảng giá riêng của chi nhánh. | Giá chỉnh vượt biên độ Admin -> Báo lỗi vượt quyền hạn. | Docx §3.2.c Branch |
| **M-09** | Manager | **Cấu Hình WiFi Chấm Công Chi Nhánh** | Khai báo danh sách BSSID Access Point và dải IP Subnet được phép chấm công tại quán. | `ssid_name`, `bssid_list[]`, `allowed_subnets[]` | Cập nhật cấu hình xác thực WiFi chấm công cho chi nhánh. | BSSID không hợp lệ -> Báo lỗi định dạng MAC Address. | Request Core Change 4 |
| **M-10** | Manager | Dashboard Báo Cáo Vận Hành Ngày | Theo dõi doanh thu theo giờ, số lượng đơn theo kênh (Dine-in, Takeaway, Delivery), AOV. | `branch_id`, `selected_date` | Biểu đồ doanh thu, top món bán chạy, hiệu suất phục vụ. | Mất mạng -> Xem dữ liệu cache offline gần nhất. | Docx §3.2.c Branch |
| **M-11** | Manager | Tiếp Nhận Alert Review Khẩn Cấp | Nhận thông báo đẩy tức thời khi có đánh giá <= 2 sao kèm số bàn/SĐT để xử lý khiếu nại. | Event `LowRatingAlert` | Pop-up cảnh báo đỏ trên Manager Portal kèm thông tin chi tiết. | Quản lý chưa phản hồi -> Nhắc lại sau 15 phút. | Docx §3.2.c Branch |
| **M-12** | Manager | Kiểm Duyệt Ảnh Đánh Giá Khách | Xem và phê duyệt hình ảnh do khách tải lên trước khi cho phép hiển thị công khai trên menu. | `feedback_id`, `approval_status` | Ảnh được duyệt xuất hiện trên trang đánh giá món của PWA. | Ảnh phản cảm/spam -> Bấm từ chối và xóa ảnh khỏi CDN. | Docx §3.2.c Branch |
| **A-01** | Admin | Quản Trị Chi Nhánh & Phân Quyền RBAC | Tạo chi nhánh mới, thiết lập thông tin liên hệ, gán quyền Quản lý chi nhánh theo RBAC. | `branch_data`, `manager_id`, `role_configs` | Chi nhánh mới kích hoạt, tài khoản được cấp quyền hạn chuẩn. | Trùng mã chi nhánh -> Báo lỗi Unique Constraint. | Docx §3.2.c Admin |
| **A-02** | Admin | **Admin Full CRUD: Món Ăn & BOM** | Toàn quyền Tạo mới, Sửa, Xóa, Thay thế sản phẩm, tải ảnh món, định nghĩa công thức BOM. | `product_info`, `image_file`, `bom_recipes[]` | Sản phẩm được lưu trữ, đồng bộ Menu toàn chuỗi và KDS. | Tên món trùng lặp -> Báo lỗi trùng tên sản phẩm. | Request Follow-up & Docx |
| **A-03** | Admin | **Quản Lý Danh Mục & Thứ Tự Menu** | Tạo/sửa/xóa danh mục sản phẩm, kéo thả sắp xếp thứ tự hiển thị của menu trên PWA. | `category_data`, `display_order` | Cây danh mục menu được cập nhật và lưu trữ thứ tự chuẩn. | Xóa danh mục đang chứa món -> Yêu cầu chuyển món trước. | Request Follow-up & Docx |
| **A-04** | Admin | **Quản Lý Menu Mùa & Lên Lịch** | Tạo thực đơn theo mùa vụ (Tết, Giáng Sinh), cài đặt lịch tự động xuất hiện/ẩn theo ngày. | `seasonal_menu_data`, `start_date`, `end_date` | Menu mùa tự động kích hoạt/hết hạn đúng khung thời gian. | Trùng khung giờ áp dụng -> Cảnh báo xung đột lịch trình. | Request Follow-up & Docx |
| **A-05** | Admin | Quản Lý Nhóm Giá & Bảng Giá Chi Nhánh | Thiết lập chính sách giá khác nhau cho từng khu vực chi nhánh (Giá Sân Bay vs Giá Phố). | `pricing_group_id`, `price_matrix` | Bảng giá vùng áp dụng chính xác cho các chi nhánh tương ứng. | Giá bán nhỏ hơn giá vốn BOM -> Cảnh báo lợi nhuận âm. | Docx §3.2.c Admin |
| **A-06** | Admin | **AI-2: Quản Trị & Duyệt Combo Apriori** | Xem gợi ý combo do thuật toán Apriori/FP-Growth khai phá, chỉnh giá ưu đãi và duyệt phát hành. | `combo_suggestions[]`, `discount_rate` | Combo chính thức xuất hiện trên Menu và đầu trang PWA. | Giảm giá quá 50% -> Cảnh báo xác nhận mức chiết khấu cao. | Docx §3.2.c AI-2 & Request |
| **A-07** | Admin | Quản Lý Chiến Dịch Khuyến Mãi & Voucher | Tạo mã voucher giảm giá (%, số tiền, freeship), giới hạn lượt dùng, ngân sách và thời hạn. | `voucher_rules`, `usage_limit`, `time_range` | Voucher phát hành vào hệ thống, áp dụng được trên PWA. | Ngân sách vượt trần -> Tự động dừng chiến dịch. | Docx §3.2.c Admin |
| **A-08** | Admin | Cấu Hình Chính Sách Loyalty Toàn Chuỗi | Cấu hình quy tắc tích lũy 10 ly = tặng 1 ly miễn phí và các chính sách tri ân khách hàng. | `loyalty_parameters` | Áp dụng chính sách tích điểm chung cho toàn bộ chuỗi. | Thay đổi chính sách -> Ghi log kiểm toán bất biến. | Docx §3.2.c Admin |
| **A-09** | Admin | Dashboard Báo Cáo P&L Hợp Nhất | Báo cáo Lợi Nhuận & Lỗ (P&L) hợp nhất toàn chuỗi thời gian thực (Doanh thu, COGS BOM, Lãi gộp). | `date_range`, `branch_filters[]` | Báo cáo tài chính chi tiết với biểu đồ tăng trưởng đa chiều. | Thiếu dữ liệu giá vốn -> Cảnh báo số liệu tạm tính. | Docx §3.2.c Admin |
| **A-10** | Admin | Báo Cáo Phân Tích So Sánh Đa Chi Nhánh | So sánh doanh thu, số đơn, AOV và tăng trưởng giữa các chi nhánh trong chuỗi. | `comparison_metrics[]`, `branch_ids[]` | Bảng xếp hạng chi nhánh và biểu đồ radar so sánh hiệu quả. | Chi nhánh mới mở < 7 ngày -> Gắn nhãn chi nhánh mới. | Docx §3.2.c Admin |
| **A-11** | Admin | Phân Tích Biên Lợi Nhuận Từng Món | Đánh giá tỷ suất lợi nhuận đóng góp của từng món (Menu Engineering: Stars, Plowhorses...). | `sales_history`, `cogs_history` | Ma trận phân loại món ăn giúp tối ưu hóa thực đơn chuỗi. | Món bán chạy nhưng lãi âm -> Đưa ra khuyến nghị tăng giá. | Docx §3.2.c Admin |
| **A-12** | Admin | Quản Trị Danh Bạ Khách Hàng CRM | Quản lý hồ sơ khách hàng toàn chuỗi, xem lịch sử mua, phân khúc VIP/Mới/Nguy cơ rời bỏ. | `customer_query_filters[]` | Danh sách khách hàng kèm phân khúc và tổng chi tiêu. | Truy cập trái phép SĐT -> Chặn và ghi log bảo mật. | Docx §3.2.c Admin |
| **A-13** | Admin | Quản Lý Nhân Sự & Tổng Hợp Lương | Quản lý hồ sơ nhân viên, hợp đồng, mức lương giờ và tổng hợp bảng lương từ công WiFi. | `payroll_period`, `timesheet_data` | Bảng tính lương tự động dựa trên giờ công thực tế. | Nhân viên thiếu chấm công -> Đánh dấu ca chưa hoàn tất. | Docx §3.2.c Admin |
| **A-14** | Admin | Quản Lý Danh Mục Nhà Cung Cấp | Quản lý danh bạ NCC, bảng giá nguyên liệu nhập và lịch sử công nợ mua hàng toàn chuỗi. | `supplier_data`, `price_history` | Hồ sơ nhà cung cấp và đánh giá chất lượng nguyên liệu. | Giá nhập tăng > 20% -> Cảnh báo biến động giá vốn. | Docx §3.2.c Admin |
| **A-15** | Admin | Sinh Mã QR Bàn & QR Delivery Hàng Loạt | Tạo và xuất file in ấn mã QR cho từng bàn và mã QR Delivery kích thước chuẩn có chữ ký số. | `branch_id`, `table_count`, `theme` | File PDF vector chất lượng cao sẵn sàng in ấn standee/decal. | Trùng lặp bàn -> Báo lỗi bàn đã tồn tại. | Docx §3.2.c Admin |
| **A-16** | Admin | Nhật Ký Kiểm Toán Bất Biến (Audit Log) | Lưu vết toàn bộ các thao tác nhạy cảm (sửa giá, hủy đơn, sửa chấm công, đổi mật khẩu). | `audit_query_params[]` | Bảng nhật ký bất biến ghi rõ User, Thời gian, IP, Hành động. | Thao tác can thiệp xóa log -> Cấm hoàn toàn ở tầng DB. | Docx §3.2.c Admin |
| **A-17** | Admin | Xuất Báo Cáo Đa Định Dạng | Xuất toàn bộ dữ liệu tài chính, kho, bán hàng và nhân sự ra các định dạng Excel, CSV, PDF. | `report_type`, `export_format` | File xuất dữ liệu chuẩn hóa phục vụ kế toán và thuế. | File quá lớn > 50MB -> Nén zip và gửi link tải qua mail. | Docx §3.2.c Admin |
| **A-18** | Admin | Cấu Hình Cổng Thanh Toán VietQR | Quản lý tài khoản ngân hàng thụ hưởng, API Key cổng PayOS và tham số Webhook. | `bank_account`, `client_id`, `api_key` | Cấu hình cổng thanh toán tự động khớp giao dịch. | Chữ ký Webhook không hợp lệ -> Từ chối xử lý Webhook. | Docx §3.2.c Admin |
| **A-19** | Admin | Cấu Hình Tham Số AI Gemini & RAG | Quản lý API Key Google Gemini, ngưỡng tương đồng RAG và tham số khai phá Apriori. | `gemini_api_key`, `min_confidence` | Cấu hình vận hành tối ưu cho 2 active AI modules. | Hết hạn mức Gemini Quota -> Chuyển sang Fallback engine. | Docx §3.2.c AI |
| **A-20** | Admin | Quản Trị Sao Lưu & An Toàn Dữ Liệu | Thiết lập lịch sao lưu tự động PostgreSQL, kiểm tra toàn vẹn và khôi phục sự cố. | `backup_schedule`, `storage_path` | Các bản sao lưu nén định kỳ trên lưu trữ an toàn. | Sao lưu thất bại -> Gửi thông báo khẩn cấp cho Admin. | Docx §3.2.c Admin |

---

# 3. ĐẶC TẢ CHI TIẾT 6 NGHIỆP VỤ CỐT LÕI (CORE DEEP-DIVE SPECIFICATIONS)

## 3.1 DINE-IN — 2 PHƯƠNG THỨC THANH TOÁN (VIETQR TRẢ TRƯỚC VS TIỀN MẶT TRẢ SAU)
Hệ thống hỗ trợ 2 nhánh thanh toán độc lập và linh hoạt cho khách ăn uống tại quán (Dine-In):

`
                                      ┌──► [PHƯƠNG THỨC A: VIETQR TRẢ TRƯỚC] ──► [Sinh mã VietQR] ──► [Thanh toán Paid] ──► [BẾP KDS MỚI NHẬN ĐƠN]
                                      │
[Khách quét QR bàn] ➔ [Chọn món] ─────┤
                                      │
                                      └──► [PHƯƠNG THỨC B: TIỀN MẶT TRẢ SAU] ──► [ĐƠN VÀO BẾP NGAY] ──► [NV bưng món + Bill có QR] ──► [Thu tiền / Khách quét QR]
`

### Chi tiết 2 nhánh:
1. **Nhánh A — VietQR (Thanh toán trước):**
   - **Luồng:** Khách chọn VietQR -> Hệ thống sinh mã VietQR động -> Khách quét chuyển khoản qua App ngân hàng -> Cổng PayOS gửi Webhook xác nhận -> Trạng thái chuyển `Paid` -> **Bếp KDS mới nhận đơn qua SignalR** -> Barista pha chế -> Phục vụ món.
   - **Order Status Flow:** `Pending Payment (0)` ➔ `Paid (1)` ➔ `Confirmed (2)` ➔ `Preparing (3)` ➔ `Ready (4)` ➔ `Served (5)`.
   - **Lợi ích:** Triệt tiêu hoàn toàn rủi ro bùng đơn, giảm tải thao tác in bill và thu tiền của nhân viên.
2. **Nhánh B — Tiền mặt (Thanh toán sau):**
   - **Luồng:** Khách chọn Tiền mặt -> **Đơn hàng vào bếp KDS ngay lập tức** (không cần thanh toán trước) -> Barista pha chế -> Nhân viên bưng món ra bàn **kèm theo Hóa Đơn có in mã QR VietQR trên hóa đơn** -> Khách có thể **trả Tiền mặt HOẶC quét mã QR trên hóa đơn** để chuyển khoản -> Nhân viên xác nhận thanh toán trên hệ thống.
   - **Order Status Flow:** `Confirmed (2)` ➔ `Preparing (3)` ➔ `Ready (4)` ➔ `Served (5)` ➔ `Pending Payment (0)` ➔ `Paid (1)`.
   - **Lợi ích:** Phục vụ nhóm khách hàng lớn tuổi, khách quen thích trả tiền mặt sau hoặc khách không sẵn sàng internet banking tại thời điểm gọi món.

---

## 3.2 DELIVERY — ĐẶT HÀNG GIAO TẬN NƠI (QR DELIVERY)
- **Điểm tiếp cận:** Mã QR Delivery riêng biệt (in trên poster, banner, fanpage, standee hoặc truy cập link web đặt hàng).
- **Dữ liệu bắt buộc:** Tên người nhận, Số điện thoại người nhận (`recipient_phone`), Địa chỉ giao hàng chi tiết (`delivery_address`).
- **Phí giao hàng cố định:** Luôn tự động cộng **20.000 VNĐ** (`delivery_fee = 20000`) vào tổng giá trị của mọi đơn hàng giao tận nơi.
- **Phương thức thanh toán:** **100% VietQR trả trước**. Khóa hoàn toàn tùy chọn tiền mặt COD để bảo vệ quán trước rủi ro hủy đơn khi đang giao hàng.
- **Cấu trúc Dữ liệu & Schema:** Thêm `delivery_address` (VARCHAR 500), `delivery_fee` (DECIMAL 18,2), `order_type` enum (`DineIn = 1`, `TakeAway = 2`, `Delivery = 3`) vào bảng `Orders`.
- **Order Status Flow:** `Pending Payment` ➔ `Paid` ➔ `Confirmed` ➔ `Preparing` ➔ `Ready` ➔ `Delivering` ➔ `Completed`.

---

## 3.3 TAKEAWAY — KHÁCH MUA MANG VỀ TẠI QUẦY (STAFF POS)
- **Giao diện thao tác:** Loại bỏ hoàn toàn mã QR Takeaway cho khách; Nhân viên thu ngân thao tác trực tiếp trên **Giao diện Web POS Quầy** `(staff)/pos`.
- **Tra cứu CRM & Khởi tạo tài khoản:**
  - Thu ngân hỏi và nhập Số điện thoại của khách hàng.
  - *Nếu khách mới:* Nhập tên khách -> Hệ thống tự động tạo bản ghi CRM mới với `CupBalance = 0`.
  - *Nếu khách cũ:* Hệ thống hiển thị tên, lịch sử gọi món gần nhất và số ly đã tích lũy (`CupBalance`).
- **Chính sách Loyalty 10 ly = tặng 1 ly miễn phí:**
  - **CHỈ áp dụng cho đơn Takeaway** (Không áp dụng cho Dine-In, không áp dụng cho Delivery).
  - Hệ thống đếm số ly đồ uống tiêu chuẩn trong đơn mua mang đi. Cứ mỗi 10 ly tích lũy -> Khách được tặng 1 ly miễn phí (ly thứ 11 miễn phí).
- **Thanh toán linh hoạt sau khi nhận món (Post-payment):**
  - Thu ngân chọn phương thức: **Tiền mặt** (nhập số tiền khách đưa -> hệ thống tự tính tiền thừa và mở két) hoặc **VietQR** tại quầy (hiển thị mã QR trên tablet/màn hình phụ để khách quét).

---

## 3.4 CHẤM CÔNG KHÓA MẠNG WIFI (WIFI-LOCKED ATTENDANCE)
- **Công nghệ bị loại bỏ:** Xóa bỏ hoàn toàn cơ chế định vị vệ tinh GPS (sai số lớn trong nhà) và mã QR động thay đổi mỗi 30 giây.
- **Cơ chế xác thực WiFi 2 lớp (Dual Verification):**
  1. *Lớp mạng:* Kiểm tra địa chỉ IP Gateway / Subnet hoặc BSSID Access Point của thiết bị gửi yêu cầu có khớp với cấu hình `branch_wifi_configs` của chi nhánh hay không.
  2. *Lớp định danh:* Kiểm tra Mã số nhân viên (`EmployeeCode`) và ca làm việc hợp lệ.
- **Quy trình vận hành:**
  - Nhân viên kết nối mạng WiFi của quán -> Truy cập `(staff)/attendance` -> Quét QR chấm công trong hệ thống hoặc nhập Mã NV -> Hệ thống kiểm tra: (a) Đúng WiFi quán? (b) Mã NV hợp lệ? -> Đúng cả 2 -> Ghi nhận vào ca/ra ca thành công. Nếu dùng 4G hoặc WiFi ngoài -> Từ chối chấm công ngay lập tức.
- **Cấu hình Quản lý:** Quản lý chi nhánh cấu hình danh sách BSSID và Allowed IP Subnets trong phần cài đặt chi nhánh.

---

## 3.5 ADMIN FULL CRUD & TOÀN QUYỀN QUẢN TRỊ
Admin (Chủ chuỗi) có toàn quyền kiểm soát tuyệt đối toàn bộ tài nguyên hệ thống:
1. **CRUD Sản Phẩm Đầy Đủ:** Tạo mới món ăn/đồ uống, Sửa thông tin, Xóa món (Soft Delete), Thay thế sản phẩm tương đương.
2. **Quản Lý Định Lượng BOM:** Định nghĩa công thức chi tiết từng ml/gam nguyên liệu cho từng kích cỡ (Size S/M/L) của món.
3. **Quản Lý Combo Sản Phẩm:** Tạo các gói combo nhiều món với giá ưu đãi cố định hoặc giảm theo phần trăm.
4. **Upload Hình Ảnh:** Tải lên hình ảnh sản phẩm chất lượng cao, hình ảnh danh mục, hỗ trợ nén và tối ưu hóa WebP.
5. **Quản Lý Bảng Giá Chi Nhánh (`branch_price_overrides`):** Thiết lập chính sách giá bán khác nhau theo từng chi nhánh hoặc vùng địa lý.
6. **Bật/Tắt Khóa Món (86 Toggle):** Can thiệp bật/tắt trạng thái hết hàng của món toàn chuỗi hoặc tại từng chi nhánh.
7. **Quản Lý Danh Mục & Menu Mùa:** Tạo danh mục, sắp xếp thứ tự hiển thị, tạo thực đơn theo mùa vụ (Tết, Giáng Sinh) kèm lịch hẹn giờ xuất hiện/ẩn tự động.
8. **Báo Cáo & Nhật Ký:** Xem Dashboard P&L hợp nhất toàn chuỗi, phân tích so sánh đa chi nhánh, tra cứu Audit Log bất biến.

---

## 3.6 XÓA HOÀN TOÀN STAFF MOBILE APP, C-23 VÀ C-24
1. **Staff Mobile App:** Bị loại bỏ 100%. Không phát triển ứng dụng di động native/hybrid riêng. Mọi vai trò nhân viên phục vụ, pha chế, thu ngân chạy trên Web Responsive và Web KDS qua các Route Groups Next.js 14 (`(kds)`, `(staff)`).
2. **C-23 (Chia sẻ món ăn lên mạng xã hội):** XÓA HOÀN TOÀN khỏi tài liệu đặc tả, bảng tính năng, ERD, API contracts và không xuất hiện trong Future Work.
3. **C-24 (Nhận thông báo khuyến mãi qua PWA Push):** XÓA HOÀN TOÀN khỏi tài liệu đặc tả, bảng tính năng, ERD, API contracts và không xuất hiện trong Future Work.

---
# 4. ĐẶC TẢ MODULE TRÍ TUỆ NHÂN TẠO (AI MODULES SPECIFICATION)

`
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             PHÂN RÃ 5 MODULE TRÍ TUỆ NHÂN TẠO (AI)                               │
├─────────────────────────────────────────────────────────────────┬────────────────────────────────┤
│           ✅ PHẠM VI TRIỂN KHAI CHÍNH THỨC (ACTIVE MVP)          │   🔮 MỞ RỘNG TƯƠNG LAI (SCALE) │
├─────────────────────────────────────────────────────────────────┼────────────────────────────────┤
│ 1. AI-1: Chatbot Tư Vấn Khẩu Vị RAG (Recommendation Chatbot)    │ 3. AI-3: NLQ Business Analytics│
│    • Google Gemini 1.5 Flash + Hybrid Recommendation Engine.    │ 4. AI-4: Customer Churn (RFM)  │
│    • Đánh giá khoa học: Precision@K, Recall@K, NDCG, Latency.   │ 5. AI-5: Menu Demand Forecast  │
│ 2. AI-2: Khai Phá & Đề Xuất Combo Món Tự Động (Apriori/FP-Growth│                                │
│    • Market Basket Analysis (Support, Confidence, Lift).        │                                │
│    • Human-in-the-loop: Chủ chuỗi phê duyệt trước khi áp dụng.  │                                │
└─────────────────────────────────────────────────────────────────┴────────────────────────────────┘
`

## 4.1 Hai Module AI Triển Khai Trong 16 Tuần (Active MVP)
1. **AI-1: Recommendation Chatbot (RAG + Gemini 1.5 Flash):**
   - **Mục tiêu nghiên cứu:** Đề tài nghiên cứu khoa học chính của đồ án Capstone.
   - **Kiến trúc:** Khách chat tự nhiên trên PWA -> Backend xây dựng ngữ cảnh (Context Builder) kết hợp: (a) Dữ liệu thời tiết hiện tại từ OpenWeatherMap API, (b) Dữ liệu calo và thành phần dị ứng từ BOM, (c) Lịch sử tiêu dùng CRM của khách -> Gửi prompt có cấu trúc tới Google Gemini 1.5 Flash -> Trả về câu trả lời tự nhiên kèm danh sách 2-3 món gợi ý và nút 'Thêm vào giỏ hàng ngay'.
   - **Chỉ số đánh giá định lượng:** Precision@K, Recall@K, NDCG@K, Catalog Coverage, Response Latency (<= 1.5s). So sánh trực tiếp với Popularity Baseline và Random Baseline.
2. **AI-2: Combo Discovery Engine (Market Basket Analysis - Apriori / FP-Growth):**
   - **Mục tiêu kinh doanh:** Khai phá giỏ hàng lịch sử để tìm các cặp/nhóm món thường xuyên mua kèm nhằm tăng giá trị đơn hàng trung bình (AOV).
   - **Thuật toán & Chỉ số:** Apriori / FP-Growth chạy ngầm định kỳ; Tính toán Support(X -> Y), Confidence(X -> Y), Lift(X -> Y) > 1.2.
   - **Cơ chế Human-in-the-loop:** Hệ thống sinh danh sách gợi ý combo -> Chủ chuỗi xem xét trên Admin Dashboard, điều chỉnh mức chiết khấu giá -> Chủ chuỗi phê duyệt phát hành lên Menu và PWA.

## 4.2 Ba Module AI Định Hướng Tương Lai (Scale Up / Future Work)
*(Thiết kế sẵn Extension Points, không triển khai code trong 16 tuần)*:
1. **AI-3: Natural Language Business Analytics (Text-to-SQL):** Hỏi đáp số liệu kinh doanh bằng tiếng Việt cho Chủ chuỗi.
2. **AI-4: Customer Churn Prediction (RFM + Random Forest/XGBoost):** Dự báo khách quen có nguy cơ ngừng ghé quán.
3. **AI-5: Dynamic Menu Intelligence & Demand Forecasting:** Dự báo nhu cầu nguyên liệu và gợi ý giá động.

---

# 5. MA TRẬN PHÂN ĐỊNH PHẠM VI (16-WEEK MVP VS SCALE UP / FUTURE WORK)

| Phân Hệ / Tính Năng | 16-Tuần 4-Thành Viên MVP (Active) | Scale Up / Future Work | Lý Do Phân Định & Trạng Thái |
|---|:---:|:---:|---|
| **Đặt món tại bàn (Dine-In)** | ✅ 2 Nhánh (VietQR trước / Tiền mặt sau) | — | Nghiệp vụ cốt lõi bắt buộc. |
| **Đặt hàng giao tận nơi (QR Delivery)** | ✅ Form SĐT + Địa chỉ, Phí 20k, VietQR | — | Nghiệp vụ cốt lõi mở rộng kênh bán. |
| **Bán mang về tại quầy (Takeaway)** | ✅ Web POS NV, Tích 10 ly, Thu sau | — | Nghiệp vụ cốt lõi tại quầy thu ngân. |
| **Chấm công nhân viên** | ✅ Khóa Mạng WiFi (BSSID/IP + Mã NV) | 🔮 Sinh trắc học FaceID | WiFi đủ đáp ứng chống gian lận trong MVP. |
| **Nền tảng ứng dụng nhân viên** | ✅ 100% Web Responsive (KDS/POS/Admin)| ❌ Xóa Staff Mobile App | Bỏ hoàn toàn App native để tối ưu nguồn lực. |
| **Chương trình Loyalty** | ✅ Tích 10 ly tặng 1 ly (Chỉ Takeaway) | 🔮 Hạng thẻ VIP đa tầng phức tạp| Đơn giản hóa cơ chế tích điểm theo docx. |
| **Tính năng Chia sẻ MXH (C-23)** | ❌ ĐÃ XÓA TRIỆT ĐỂ | ❌ ĐÃ XÓA TRIỆT ĐỂ | Loại bỏ hoàn toàn theo yêu cầu người dùng. |
| **Tính năng Push Promo PWA (C-24)** | ❌ ĐÃ XÓA TRIỆT ĐỂ | ❌ ĐÃ XÓA TRIỆT ĐỂ | Loại bỏ hoàn toàn theo yêu cầu người dùng. |
| **AI-1 Chatbot Tư Vấn Khẩu Vị** | ✅ RAG Gemini 1.5 Flash + Đánh giá NDCG | — | Module nghiên cứu chính Capstone. |
| **AI-2 Khai Phá Combo Món** | ✅ Apriori/FP-Growth + Chủ chuỗi duyệt | — | Module AI gia tăng AOV bắt buộc. |
| **AI-3 Hỏi Đáp Số Liệu Kinh Doanh** | — | 🔮 Text-to-SQL Analytics | Extension Point `ITextToSqlEngine`. |
| **AI-4 Dự Báo Khách Rời Bỏ (Churn)**| — | 🔮 XGBoost RFM Model | Extension Point `IChurnPredictor`. |
| **AI-5 Dự Báo Nhu Cầu Nguyên Liệu** | — | 🔮 Demand Forecasting Engine | Extension Point `IDemandForecaster`. |
| **Điều phối Ship bên thứ ba** | — | 🔮 AhaMove / GrabExpress API | Tự giao hàng trong phạm vi gần trước. |
| **Đồng bộ Dữ liệu Offline Mesh** | — | 🔮 IndexedDB P2P Sync | Hoạt động dựa trên kết nối Internet ổn định. |
| **Cổng tự phục vụ Nhà Cung Cấp** | — | 🔮 Supplier Self-Service Portal | Quản lý nhập thủ công qua Manager Portal. |

---

# 6. MA TRẬN CÁC KỊCH BẢN BIÊN (EDGE CASES MATRIX)

| # | Feature / Subsystem | Input / Kịch Bản Biên | Hành Vi Xử Lý Chuẩn Mực Của Hệ Thống |
|---|---|---|---|
| **E-01** | Dine-In VietQR | Khách tạo đơn nhưng không chuyển khoản sau 10 phút. | Hệ thống tự động hủy đơn (`Status = Cancelled`), thu hồi mã QR, phát SignalR giải phóng giỏ hàng. |
| **E-02** | Dine-In VietQR | Khách chuyển khoản thiếu số tiền yêu cầu (ví dụ: bill 75k nhưng chuyển 70k). | Cổng PayOS ghi nhận giao dịch không khớp, đơn giữ nguyên `PendingPayment`, báo lỗi số tiền không đủ. |
| **E-03** | Dine-In VietQR | Khách chuyển khoản thừa số tiền (ví dụ: bill 75k nhưng chuyển 100k). | Đơn vẫn chuyển `Paid` vào bếp, hệ thống ghi nhận khoản thu thừa vào số dư tài khoản/chờ thu ngân hoàn tiền. |
| **E-04** | Dine-In Tiền Mặt | Khách chọn Tiền mặt, bếp đã pha xong nhưng khách rời bàn không thanh toán. | NV phục vụ báo sự cố, Quản lý ghi nhận đơn 'Hủy do khách bỏ về' kèm log kiểm toán và camera bàn. |
| **E-05** | Dine-In Tiền Mặt | Khách quét mã QR in trên hóa đơn để chuyển khoản khi nhân viên mang món ra bàn. | Hệ thống nhận Webhook thanh toán, tự động cập nhật đơn sang `Paid`, máy Staff POS đổi trạng thái 'Đã thu tiền'. |
| **E-06** | Dine-In Gọi Thêm Món | Khách tại bàn đã gọi 1 đơn thành công, muốn gọi thêm 2 ly nước nữa. | Hệ thống cho phép chọn món và tạo đơn phụ (Sub-order) gắn cùng `table_id` và cùng phiên bàn hiện tại. |
| **E-07** | QR Delivery | Khách nhập địa chỉ giao hàng rỗng hoặc chỉ có khoảng trắng. | Frontend validate chặn submit; Backend FluentValidation ném lỗi 400 'Địa chỉ giao hàng là bắt buộc'. |
| **E-08** | QR Delivery | Khách nhập Số điện thoại sai định dạng (ví dụ: '12345' hoặc chứa chữ cái). | Regex validation chặn submit; thông báo 'Số điện thoại người nhận không hợp lệ (10 chữ số)'. |
| **E-09** | QR Delivery | Khách yêu cầu thanh toán tiền mặt COD khi giao hàng. | Hệ thống không cung cấp tùy chọn COD, hiển thị thông báo 'Đơn giao hàng chỉ chấp nhận VietQR trả trước'. |
| **E-10** | QR Delivery | Phí giao hàng có bị thay đổi khi khách mua nhiều món không? | Phí giao hàng luôn cố định đúng **20.000 VNĐ** bất kể số lượng món hoặc tổng giá trị đơn hàng. |
| **E-11** | Takeaway Staff POS | Khách mua mang đi yêu cầu tích điểm nhưng không nhớ số điện thoại. | Thu ngân cho phép tạo đơn vãng lai không tích điểm (`customer_id = null`), đơn vẫn xử lý bình thường. |
| **E-12** | Takeaway Loyalty | Khách đã tích lũy đủ 10 ly, trong đơn mới mua 2 ly (1 ly 45k, 1 ly 35k). | Hệ thống tự động giảm giá 100% cho ly có giá cao nhất (45k), khách chỉ trả 35k, trừ 10 ly khỏi `CupBalance`. |
| **E-13** | Takeaway Loyalty | Khách đặt đơn Dine-In hoặc Delivery có được tích điểm 10 ly tặng 1 không? | **KHÔNG.** Hệ thống chỉ cộng số ly tích lũy cho các đơn hàng có `OrderType = TakeAway`. |
| **E-14** | Takeaway Thu Tiền | Thu ngân nhập số tiền khách đưa nhỏ hơn tổng bill (ví dụ: bill 50k nhập 40k). | Giao diện Web POS báo đỏ, nút 'Xác nhận thanh toán' bị vô hiệu hóa cho đến khi nhập đủ tiền. |
| **E-15** | Takeaway Thu Tiền | Khách chọn thanh toán VietQR tại quầy nhưng mạng ngân hàng khách bị gián đoạn. | Thu ngân có quyền chuyển đổi phương thức thanh toán sang Tiền mặt trên Web POS bằng 1 thao tác. |
| **E-16** | Chấm Công WiFi | Nhân viên bật 4G/5G để chấm công khi đang ở ngoài quán. | Backend kiểm tra Client IP/BSSID không khớp danh sách cho phép -> Từ chối và ném lỗi 403 Forbidden. |
| **E-17** | Chấm Công WiFi | Quán bị đổi thiết bị phát WiFi mới (BSSID Access Point thay đổi). | Quản lý truy cập Manager Portal cập nhật BSSID mới; nhân viên sau đó chấm công bình thường. |
| **E-18** | Chấm Công WiFi | Nhân viên nhập sai Mã số nhân viên (`EmployeeCode`). | Hệ thống báo lỗi 'Mã nhân viên không tồn tại hoặc đã bị khóa tài khoản', ghi log lần chấm công thất bại. |
| **E-19** | Chấm Công WiFi | Nhân viên chấm công Check-in 2 lần liên tiếp trong vòng 5 phút. | Hệ thống ghi nhận lần đầu tiên, lần thứ 2 hiển thị thông báo 'Bạn đã check-in ca làm việc lúc [HH:mm]'. |
| **E-20** | KDS Barista | Hai Barista cùng chạm vào một đơn hàng để bấm 'Pha chế' đồng thời. | Redis Distributed Lock bảo vệ `lock:order:{id}`, chỉ 1 thao tác hợp lệ, giao diện Barista kia cập nhật theo. |
| **E-21** | KDS 86-Toggle | Barista khóa 86 món 'Trà sữa olong' đúng lúc khách hàng đang xem món đó trên PWA. | SignalR MenuHub phát event tức thì, nút 'Thêm vào giỏ' trên PWA khách mờ đi và chuyển thành 'Tạm hết món'. |
| **E-22** | KDS 86-Toggle | Khách đã thêm món vào giỏ hàng trước khi Barista khóa 86, sau đó bấm Thanh toán. | Backend kiểm tra lại tính khả dụng (Invariants check) trước khi tạo đơn, báo lỗi 'Món [X] vừa hết hàng'. |
| **E-23** | Mở/Kết Ca Két | Quản lý quên kết ca hôm trước, sáng hôm sau mở ca mới. | Hệ thống phát hiện ca cũ còn mở, yêu cầu hoàn tất kiểm đếm két kết ca cũ trước khi được phép mở ca mới. |
| **E-24** | Mở/Kết Ca Két | Kết ca phát hiện tiền mặt thực tế thiếu 100.000đ so với số dư phần mềm. | Hệ thống ghi nhận chênh lệch -100.000đ, bắt buộc Quản lý nhập lý do giải trình trước khi đóng ca. |
| **E-25** | Quản Lý Kho BOM | Đơn hàng hoàn tất nhưng nguyên liệu trong kho không đủ để trừ theo BOM. | Hệ thống vẫn cho hoàn tất đơn để phục vụ khách, số lượng tồn kho chuyển sang giá trị âm và gửi alert khẩn. |
| **E-26** | Quản Lý Kho | Quản lý nhập hàng từ NCC nhưng chưa có hóa đơn giấy chính thức. | Hệ thống cho phép lưu phiếu nhập ở trạng thái 'Bản nháp' (Draft), khi có hóa đơn thì duyệt chính thức. |
| **E-27** | AI-1 Chatbot | Khách hỏi câu hỏi không liên quan đến menu (ví dụ: 'Thời tiết Paris hôm nay thế nào?'). | System Prompt hướng dẫn Gemini từ chối lịch sự và khéo léo dẫn dắt về menu đồ uống của quán. |
| **E-28** | AI-1 Chatbot | API Key Gemini bị hết hạn mức hoặc mất kết nối mạng ngoài. | Graceful Fallback: Chatbot thông báo 'Trợ lý đang bận' và tự động hiển thị danh sách Top 3 Best-Seller. |
| **E-29** | AI-2 Combo | Thuật toán Apriori đề xuất combo nhưng quán hiện đang hết 1 món trong combo. | Hệ thống tự động ẩn combo đó khỏi Menu PWA cho đến khi món thành phần được mở khóa 86 trở lại. |
| **E-30** | Đánh Giá Feedback | Khách hàng đánh giá 1 sao nhưng không nhập bình luận. | Hệ thống vẫn ghi nhận 1 sao, tính điểm trung bình và lập tức kích hoạt Alert khẩn cấp gửi Quản lý. |
| **E-31** | Đánh Giá Feedback | Khách tải lên file thực thi .exe hoặc file dung lượng 20MB thay vì file ảnh. | Middleware chặn upload, chỉ chấp nhận mime-type image/jpeg, image/png, image/webp, dung lượng <= 5MB. |
| **E-32** | Gọi Phục Vụ | Khách bấm chuông gọi phục vụ liên tục 10 lần trong 10 giây. | Rate Limiter chặn các lần bấm sau, hiển thị thông báo 'Yêu cầu của bạn đã được gửi, vui lòng chờ trong giây lát'. |
| **E-33** | Admin Phân Quyền | Quản lý chi nhánh A cố gắng truy cập dữ liệu doanh thu của chi nhánh B. | Multi-tenant Data Filter tại tầng Repository chặn truy vấn, trả về lỗi 403 Forbidden. |
| **E-34** | Sơ Đồ Bàn | Khách quét QR bàn 05 nhưng chuyển sang ngồi bàn 08 mà không báo nhân viên. | NV phục vụ có thể dùng Web Staff POS để thao tác 'Chuyển đơn từ Bàn 05 sang Bàn 08' tức thì. |
| **E-35** | Báo Cáo EOD | Đường truyền mạng chi nhánh bị mất lúc 23:59 khi chạy tác vụ tổng hợp ngày. | Background Job có cơ chế Retry tự động mỗi 15 phút, khi có mạng trở lại sẽ tổng hợp bù dữ liệu. |

---

# 7. KẾT LUẬN & KIẾN NGHỊ CHO CÁC BƯỚC TIẾP THEO

1. **Tính hoàn chỉnh của đặc tả:** Toàn bộ các yêu cầu từ file docx Smart_FB_OS_Revised_4members.docx và các chỉ thị nghiệp vụ tại ORIGINAL_REQUEST.md đã được bóc tách và phân rã 100% thành các bảng danh mục tính năng, kịch bản biên và ma trận phân quyền rõ ràng.
2. **Khóa phạm vi nghiệp vụ (Scope Freeze):**
   - Dine-In 2 nhánh (VietQR trả trước vs Tiền mặt trả sau kèm bill có QR).
   - Delivery 100% VietQR, bắt buộc SĐT + Địa chỉ, phí ship 20k cố định.
   - Takeaway Web POS, tích 10 ly tặng 1 ly miễn phí chỉ cho takeaway, thu tiền sau.
   - Chấm công WiFi-locked, bỏ GPS/QR 30s.
   - Admin Full CRUD sản phẩm, combo, ảnh, menu mùa, giá chi nhánh, khóa 86.
   - Xóa bỏ triệt để Staff Mobile App, C-23 và C-24.
   - 2 Active AI Modules (AI-1 RAG Gemini & AI-2 Apriori Combo); 3 AI modules còn lại là Future Work.
3. **Sẵn sàng chuyển giao:** Tài liệu 
eport.md này là nền tảng sự thật duy nhất (Single Source of Truth) để đội ngũ tiến hành cập nhật 5 file tài liệu đặc tả trong d:\\Idea_DoAn\\01_Tai_Lieu_Dac_Ta_Goc\\.
