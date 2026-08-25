# BÁO CÁO ĐẶC TẢ KỸ THUẬT BACKEND (BACKEND TECHNICAL SPECIFICATION)
## HỆ THỐNG SMART F&B OPERATING SYSTEM (.NET 8 CLEAN ARCHITECTURE)

- **Mã tài liệu:** `SPEC-MINER-BACKEND-01`
- **Phiên bản:** `v2.5.0-Production-Ready`
- **Tác giả:** Backend Specification Miner Agent
- **Thời gian thực hiện:** 2026-08-25
- **Nguồn sự thật tham chiếu:**
  1. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md` (62 Features)
  2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md` (25 Tables 3NF)
  3. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md` (10 API Groups, 4 Hubs)
  4. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md` (10 Architectural Sequences)
  5. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md` (ERD Data Dictionary)
  6. `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`

---

## 1. Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| 01 | Auth | Login & Token Issuance | Xác thực người dùng bằng Username/EmployeeCode và Password, cấp Access Token JWT (15 phút) và Refresh Token (7 ngày). | `LoginUserCommand(Username, Password)` | `AuthResultDto(AccessToken, RefreshToken, ExpiresIn, UserProfileDto)` | 400 Bad Request nếu validation lỗi; 401 Unauthorized nếu sai mật khẩu/tài khoản bị khóa. | API Contract 2.1, Sequence Spec |
| 02 | Auth | Refresh Token Rotation | Cấp lại Access Token mới bằng Refresh Token hợp lệ và xoay vòng Refresh Token. | `RefreshTokenCommand(RefreshToken)` | `AuthResultDto` | 401 Unauthorized nếu Refresh Token hết hạn, bị thu hồi hoặc không hợp lệ. | API Contract 2.1 |
| 03 | Auth | User & RBAC Management | Quản lý danh sách, tạo mới, phân bổ vai trò (`ChainAdmin`, `BranchManager`, `BaristaStaff`, `CashierStaff`, `ServiceStaff`) cho nhân viên. | `CreateUserCommand`, `UpdateUserCommand` | `UserProfileDto` | 409 Conflict nếu trùng EmployeeCode/Username; 403 Forbidden nếu không đủ quyền. | Database 4.3, API Contract 2.1 |
| 04 | Branches | Branch Management | Full CRUD chi nhánh toàn chuỗi, địa chỉ, hotline, giờ mở/đóng cửa. | `CreateBranchCommand`, `UpdateBranchCommand` | `BranchDto` | 409 Conflict nếu trùng mã chi nhánh (`Code`). | Database 4.2, API Contract 2.2 |
| 05 | Branches | Branch WiFi Configuration | Thiết lập danh sách MAC BSSID của Access Points và dải IP Subnet hợp lệ cho từng chi nhánh. | `UpdateBranchWifiConfigsCommand(BranchId, List<WifiConfigItemDto>)` | `ApiResponse<bool>` | 400 Bad Request nếu định dạng MAC/IP Subnet không hợp lệ. | Database 4.2, API Contract 2.2 |
| 06 | Tables | Table Layout & Management | Quản lý sơ đồ bàn theo khu vực, sức chứa, trạng thái phục vụ. | `CreateTableCommand`, `UpdateTableStatusCommand` | `TableDto` | 409 Conflict nếu trùng `(branch_id, table_number)`. | Database 4.2, API Contract 2.2 |
| 07 | Tables | Table QR Generation | Sinh mã QR động gắn bàn kèm token URL bảo mật có chữ ký HMAC chống giả mạo. | `GenerateTableQrCommand(TableId)` | `TableQrDto(QrCodeUrl, DeepLinkUrl)` | 404 Not Found nếu không tìm thấy bàn. | ERD 3.2, API Contract 2.2 |
| 08 | Products | Category Management & Reordering | Quản lý danh mục thực đơn, kéo thả cập nhật thứ tự hiển thị (`display_order`). | `ReorderCategoriesCommand(List<CategoryOrderItemDto>)` | `ApiResponse<bool>` | 400 Bad Request nếu thiếu danh mục. | Database 4.4, API Contract 2.3 |
| 09 | Products | Master Product Catalog CRUD | Toàn quyền tạo, sửa, xóa mềm (Soft Delete) món ăn, hình ảnh WebP, calo, dị ứng, nhãn Best-Seller. | `CreateProductCommand`, `UpdateProductCommand` | `ProductDto` | 409 Conflict nếu trùng SKU; 400 Bad Request nếu giá âm. | Database 4.4, API Contract 2.3 |
| 10 | Products | Product Size Variants | Định nghĩa các kích cỡ (Size S/M/L) và chênh lệch giá (`price_adjustment`) theo từng món. | `CreateProductSizeCommand` | `ProductSizeDto` | 409 Conflict nếu trùng tên kích cỡ trên cùng 1 món. | Database 4.4, API Contract 2.3 |
| 11 | Products | Product Modifiers & Options | Định nghĩa tùy chọn mức đường (0-100%), mức đá (0-100%), sữa hạt, topping và giá phụ thu. | `AddProductModifierCommand` | `ModifierDto` | 400 Bad Request nếu cấu hình sai kiểu modifier. | Database 4.4, API Contract 2.3 |
| 12 | Products | Recipe Bill of Materials (BOM) | Thiết lập định mức nguyên vật liệu tiêu chuẩn (g, ml) cho từng món ăn và kích cỡ cụ thể. | `CreateRecipeBomCommand` | `RecipeBomDto` | 400 Bad Request nếu định lượng `<= 0`; 409 Conflict nếu trùng `(product_id, size_id, ingredient_id)`. | Database 4.4, API Contract 2.3 |
| 13 | Products | Regional Pricing Override | Thiết lập bảng giá bán riêng biệt theo vùng địa lý hoặc chi nhánh đặc thù (Sân bay vs Trung tâm). | `SetRegionalPriceCommand(BranchId, ProductId, PriceOverride)` | `ProductBranchPriceDto` | 404 Not Found nếu không tìm thấy món hoặc chi nhánh. | Database 4.4, API Contract 2.3 |
| 14 | Products | Seasonal Menu Scheduling | Lên lịch phát hành thực đơn mùa vụ (Tết, Hè, Giáng Sinh) kèm ngày kích hoạt/ẩn tự động. | `CreateSeasonalMenuCommand(Title, ActiveFrom, ActiveTo, ProductIds)` | `SeasonalMenuDto` | 400 Bad Request nếu `ActiveTo <= ActiveFrom`. | API Contract 2.3, Core Spec 8.4 |
| 15 | Products | Product Replacement (Replace Product) | Thay thế món cũ bằng món mới trên menu, tự động kế thừa lịch sử báo cáo tài chính mà không phá vỡ liên kết. | `ReplaceProductCommand(OldProductId, NewProductId, Reason)` | `ApiResponse<bool>` | 404 Not Found nếu món cũ/mới không tồn tại. | API Contract 2.3, Core Spec 8.4 |
| 16 | Orders | Dine-In Prepaid (Nhánh A) | Khách quét Table QR, chọn món, thanh toán VietQR trả trước (TTL 10m). Bếp KDS CHỈ nhận đơn khi Webhook PayOS xác nhận `Paid`. | `CreateDineInPrepaidOrderCommand(BranchId, TableId, Items, CustomerPhone, VoucherCode)` | `PrepaidOrderResultDto(OrderId, TotalAmount, VietQr)` | 422 Unprocessable nếu món hết hàng 86-out hoặc bàn đang khóa. | Core Spec 2.1, Sequence Seq-01 |
| 17 | Orders | Dine-In Postpaid (Nhánh B) | Khách quét Table QR, chọn Tiền mặt trả sau. Đơn vào bếp KDS NGAY LẬP TỨC (`Confirmed`). Khi Barista bấm Ready, in bill kèm VietQR động để phục vụ mang ra bàn thu tiền mặt/quét QR. | `CreateDineInPostpaidOrderCommand(BranchId, TableId, Items, CustomerPhone)` | `PostpaidOrderResultDto(OrderId, Status, EstimatedMinutes)` | 400 Bad Request nếu giỏ hàng rỗng; 422 Unprocessable nếu vi phạm trạng thái bàn. | Core Spec 2.1, Sequence Seq-02 |
| 18 | Orders | QR Delivery Order | Khách quét Delivery QR, nhập SĐT, Tên, Địa chỉ chi tiết. Tự động cộng **Phí ship cố định 20.000 VNĐ**. **100% VietQR trả trước** (Khóa COD). | `CreateDeliveryOrderCommand(BranchId, RecipientName, RecipientPhone, DeliveryAddress, Items)` | `DeliveryOrderResultDto(OrderId, TotalAmount, DeliveryFee=20000, VietQr)` | 400 Bad Request nếu SĐT không đúng 10 số hoặc địa chỉ `< 10` ký tự. | Core Spec 2.2, Sequence Seq-03 |
| 19 | Orders | Takeaway Web POS Order | Thu ngân tạo đơn mang về tại quầy Web POS (không QR), tra cứu SĐT CRM, áp dụng ưu đãi **Tích 10 Ly = Tặng 1 Ly Miễn Phí**, thu tiền sau khi giao món. | `CreateTakeawayOrderCommand(BranchId, CustomerPhone, CustomerName, Items, RedeemFreeCup, PaymentMethod)` | `TakeawayOrderResultDto(OrderId, SubTotal, LoyaltyDiscount, FinalAmount, CashChange)` | 422 Unprocessable nếu quỹ ly `< 10` mà yêu cầu đổi thưởng. | Core Spec 2.3, Sequence Seq-04 |
| 20 | Orders | Order Real-Time Tracking | Theo dõi tiến độ đơn hàng theo thời gian thực qua SignalR WebSocket (`PendingPayment` -> `Paid` -> `Confirmed` -> `Preparing` -> `Ready` -> `Served`/`Completed`). | `GetOrderTrackingQuery(OrderId)` | `OrderTrackingDto(Status, QueuePosition, EstimatedMinutes)` | 404 Not Found nếu không tìm thấy đơn hàng. | API Contract 2.4, Sequence Spec |
| 21 | Payments | Dynamic VietQR Generation | Sinh chuỗi mã QR thanh toán chuẩn NAPAS 247 nạp sẵn số tiền chính xác và cú pháp nội dung chuyển khoản theo mã đơn. | `GenerateVietQRCommand(OrderId)` | `VietQrDto(QrCodeUrl, AccountNumber, TransferContent, ExpiresAtUtc)` | 404 Not Found nếu không tìm thấy đơn; 409 Conflict nếu đơn đã thanh toán. | API Contract 2.5, Sequence Spec |
| 22 | Payments | PayOS Webhook Ingestion | Tiếp nhận Webhook thanh toán VietQR từ cổng PayOS. Xác minh chữ ký HMAC-SHA256, khóa phân tán Redis chống duplicate (Idempotency), cập nhật đơn sang `Paid`, bắn SignalR tới Bếp KDS. | `ProcessPayOSWebhookCommand(PayOSWebhookData)` | `ApiResponse<bool>` | 400 Bad Request nếu sai chữ ký HMAC-SHA256. | API Contract 2.5, Sequence Seq-01 |
| 23 | Payments | Cash Payment Confirmation | Thu ngân xác nhận đã thu tiền mặt tại quầy hoặc tại bàn, tính tiền thối, cập nhật đơn `Paid`/`Completed` và ghi tăng doanh thu ca két tiền. | `ConfirmCashPaymentCommand(OrderId, ReceivedAmount)` | `CashConfirmationResultDto(ChangeAmount, Status)` | 400 Bad Request nếu số tiền khách đưa nhỏ hơn tổng đơn. | API Contract 2.5, Sequence Seq-02 |
| 24 | Payments | Payment Status Polling | Truy vấn trạng thái thanh toán đơn hàng làm kênh dự phòng fallback khi kết nối WebSocket gián đoạn. | `GetPaymentStatusQuery(OrderId)` | `PaymentStatusDto(IsPaid, Status, PaidAt)` | 404 Not Found nếu không tìm thấy giao dịch. | API Contract 2.5 |
| 25 | CRM & Loyalty | Loginless Customer Identification | Nhận diện khách hàng trên PWA bằng Số điện thoại (không cần mật khẩu), trả về hồ sơ, hạng thẻ, số ly tích lũy và voucher khả dụng. | `IdentifyCustomerCommand(Phone, BranchId)` | `CustomerProfileDto(CustomerId, Phone, CupBalance, Vouchers)` | 400 Bad Request nếu định dạng SĐT sai. | Core Spec 8.1, API Contract 2.6 |
| 26 | CRM & Loyalty | Takeaway Loyalty (10 Cups = 1 Free) | Chính sách tích 10 ly đổi 1 ly miễn phí: **DUY NHẤT ÁP DỤNG CHO KÊNH TAKEAWAY**. Khi đổi, trừ 10 ly trong `cup_balance` và giảm 100% giá của 1 ly tiêu chuẩn. | `RedeemLoyaltyCupCommand(CustomerId, OrderId, FreeProductId)` | `LoyaltyRedemptionResultDto` | 422 Unprocessable nếu đơn hàng không phải Takeaway hoặc `cup_balance < 10`. | Core Spec 2.3, Sequence Seq-04 |
| 27 | CRM & Loyalty | Voucher Validation & Campaign | Áp dụng mã khuyến mãi giảm giá (% hoặc FixedAmount), kiểm tra giá trị đơn tối thiểu, hạn sử dụng và ngân sách chiến dịch. | `ValidateVoucherCommand`, `CreateVoucherCommand` | `VoucherValidationDto(IsValid, DiscountAmount)` | 422 Unprocessable nếu voucher hết hạn, quá lượt dùng hoặc chưa đạt min order. | Database 4.6, API Contract 2.6 |
| 28 | Kitchen KDS | Real-time Ticket Stream | Quầy Bar/Bếp nhận vé đơn hàng mới thời gian thực qua SignalR `KitchenHub` (Đơn Dine-In VietQR Paid, Dine-In Cash Confirmed, Delivery Paid, Takeaway Confirmed). | `GetKdsTicketsQuery(BranchId, StationType)` | `List<KdsTicketDto>` | 403 Forbidden nếu người dùng không phải Barista/Manager. | Core Spec 8.2, API Contract 2.7 |
| 29 | Kitchen KDS | Order Status Transition & Auto BOM Deduction | Barista chuyển trạng thái pha chế (`Preparing` -> `Ready`). Khi bấm `Ready`, hệ thống **tự động trừ tồn kho nguyên liệu theo định mức BOM chuẩn** đến từng gam/ml. | `UpdateKdsOrderStatusCommand(OrderId, NewStatus)` | `ApiResponse<bool>` | 422 Unprocessable nếu chuyển trạng thái không hợp lệ trong State Machine. | Core Spec 8.2, Sequence Seq-06 |
| 30 | Kitchen KDS | Order Batching (Gom Món) | Gom các món cùng loại từ nhiều đơn đang chờ (ví dụ: "5 Cà phê muối") để Barista pha chế đồng loạt tối ưu thời gian. | `StartKdsBatchCommand(OrderItemIds)`, `CompleteKdsBatchCommand(BatchId)` | `KdsBatchResultDto` | 400 Bad Request nếu danh sách order items không cùng loại sản phẩm. | Core Spec 8.2, API Contract 2.7 |
| 31 | Kitchen KDS | 86-Toggle (Emergency Out-of-Stock) | Barista bật/tắt công tắc hết hàng của món ngay tại quầy bar khi cạn nguyên liệu, đồng bộ tức thời khóa món trên QR Menu PWA và Web POS. | `ToggleProductAvailabilityCommand(BranchId, ProductId, IsAvailable)` | `Item86ToggledEvent` | 404 Not Found nếu không tìm thấy món tại chi nhánh. | Core Spec 8.2, Sequence Seq-06 |
| 32 | HRM & Attendance | WiFi-Locked Attendance (Dual Check) | Chấm công vào ca/ra ca bằng xác thực kép: (1) BSSID Router WiFi + Dải IP Subnet chi nhánh, (2) Mã nhân viên hợp lệ theo ca. Chống 100% Fake GPS. | `WifiClockInCommand(BranchId, EmployeeCode, ClientBssid, ClientIp)` | `AttendanceRecordDto(Status="OnTime", CheckInTime)` | 400 Bad Request / 403 Forbidden nếu thiết bị dùng 4G hoặc mạng ngoài quán. | Core Spec 2.4, Sequence Seq-05 |
| 33 | Staff Ops | Service Call Request & Resolution | Khách tại bàn bấm chuông gọi phục vụ (Lấy nước, Dọn bàn, Khăn giấy). Phát chuông SignalR tới POS quầy; nhân viên bấm "Đã xử lý" để giải phóng cảnh báo. | `CallStaffCommand(TableId, Reason)`, `ResolveServiceCallCommand(CallId)` | `ApiResponse<bool>` | 429 Too Many Requests nếu khách bấm chuông quá 1 lần trong 60 giây. | Core Spec 8.1, Sequence Seq-07 |
| 34 | Shifts & Cash | Cash Drawer Shift Open | Mở ca làm việc thu ngân đầu ngày, nhập số tiền mặt lẻ bàn giao ban đầu và cơ cấu mệnh giá tiền mặt. | `OpenCashShiftCommand(BranchId, InitialCash, CashDenominations)` | `ShiftDto(ShiftId, OpeningTime, Status="Open")` | 409 Conflict nếu chi nhánh đang có ca mở chưa kết ca. | Core Spec 8.3, Sequence Seq-09 |
| 35 | Shifts & Cash | Cash Drawer Shift Close & Z-Report | Kết ca đếm tiền mặt thực tế theo mệnh giá, đối chiếu tự động với tiền hệ thống. Nếu lệch `\|varianceAmount\| > 50.000 VNĐ`, bắt buộc nhập giải trình `varianceNotes`. Lập biên bản Z-Report. | `CloseCashShiftCommand(ShiftId, ActualCashDenominations, TotalActualCash, VarianceNotes)` | `ZReportResultDto(SystemCash, ActualCash, VarianceAmount, Status)` | 422 Unprocessable nếu lệch `> 50k` mà không có giải trình. | Core Spec 8.3, Sequence Seq-09 |
| 36 | Inventory | Bar Stock Export Requisition | Lập phiếu xuất nguyên vật liệu từ kho lưu trữ tổng ra quầy pha chế, trừ kho tổng và tăng kho khả dụng tại bar. | `CreateBarExportRequisitionCommand(BranchId, Items)` | `BarExportRequisitionDto` | 422 Unprocessable nếu kho tổng không đủ số lượng xuất. | Core Spec 8.3, API Contract 2.9 |
| 37 | Inventory | Supplier Stock Import | Nhập kho nguyên liệu mua từ nhà cung cấp kèm giá vốn và tải ảnh hóa đơn VAT đối chiếu. | `CreateSupplierStockImportCommand(BranchId, SupplierName, TotalCost, InvoiceImageUrl, Items)` | `StockImportDto` | 400 Bad Request nếu tổng chi phí không khớp danh sách nguyên liệu. | Core Spec 8.3, API Contract 2.9 |
| 38 | Inventory | Stock Audit & Variance Report | Kiểm kê định kỳ tồn kho thực tế, tính toán tỷ lệ hao hụt nguyên liệu so với định mức BOM lý thuyết. | `AuditInventoryVarianceCommand(BranchId, AuditItems)` | `StockAuditReportDto` | 400 Bad Request nếu danh sách kiểm kê rỗng. | Core Spec 8.3, API Contract 2.9 |
| 39 | Customer Reviews | 1-5 Star Review & Photo Upload | Khách đánh giá chất lượng món 1-5 sao, nhận xét, tải 1-3 ảnh thực tế, tùy chọn ẩn danh. Tự động bật `is_urgent_alert = true` nếu `Rating <= 2`. | `CreateReviewCommand(OrderId, Rating, Comment, PhotoUrls, IsAnonymous)` | `ReviewDto` | 400 Bad Request nếu `Rating` không từ 1 đến 5 hoặc quá 3 ảnh. | Database 4.6, Sequence Seq-08 |
| 40 | Customer Reviews | Urgent Low-Rating Red Alert | Khi có đánh giá `<= 2 sao`, hệ thống tự động phát cảnh báo khẩn (Red Alert) qua SignalR `NotificationHub` tới Quản lý chi nhánh để xử lý tại bàn trong 3 phút. | Trigger nội bộ sau khi `CreateReviewCommand` thực thi | `LowRatingAlertEvent(BranchId, TableNumber, Rating, Comment)` | N/A | Core Spec 8.3, Sequence Seq-08 |
| 41 | Customer Reviews | Photo Moderation | Quản lý chi nhánh xem xét và phê duyệt ảnh đánh giá do khách tải lên trước khi công khai lên trang menu PWA. | `ModerateReviewPhotoCommand(ReviewId, PhotoId, IsApproved)` | `ApiResponse<bool>` | 404 Not Found nếu không tìm thấy đánh giá. | Core Spec 8.3, API Contract 2.9 |
| 42 | AI Modules | AI-1 Gemini 1.5 Flash RAG Chatbot | Tư vấn món ăn cá nhân hóa bằng ngôn ngữ tự nhiên dựa trên ngữ cảnh thời tiết thực tế, calo, dị ứng và lịch sử CRM. | `GetGeminiRecommendationQuery(BranchId, UserQuery, CustomerPhone)` | `AiRecommendationResultDto(ResponseText, RecommendedProducts)` | 503 Service Unavailable -> Fallback trả về danh sách Best-Seller nếu AI lỗi. | Core Spec 4.1, API Contract 2.10 |
| 43 | AI Modules | AI-2 Market Basket Combo Mining (Apriori) | Khai phá dữ liệu giỏ hàng lịch sử tìm cặp món thường mua cùng nhau (`Support >= 0.02`, `Confidence >= 0.4`, `Lift > 1.2`), tính toán giá vốn BOM và biên lợi nhuận. | `MineMarketBasketCombosCommand(BranchId, MinSupport, MinConfidence)` | `List<ComboCandidateDto>` | 400 Bad Request nếu tham số thuật toán không hợp lệ. | Core Spec 4.1, API Contract 2.10 |
| 44 | AI Modules | AI-2 Combo Approval (Human-in-the-loop) | Chủ chuỗi xem xét đề xuất combo từ AI-2, điều chỉnh mức chiết khấu giá và bấm phê duyệt để phát hành combo lên menu PWA. | `ApproveAiComboCommand(ComboCandidateId, ComboName, FinalPrice, ActiveFrom, ActiveTo)` | `ComboDto` | 400 Bad Request nếu `FinalPrice < TotalBomCost`. | Core Spec 4.1, API Contract 2.10 |
| 45 | Analytics & Reports | Consolidated Multi-Branch P&L Report | Báo cáo Lợi Nhuận & Lỗ hợp nhất toàn chuỗi thời gian thực (Doanh thu thuần, Chi phí COGS theo BOM, Lãi gộp, Tỷ suất lợi nhuận). | `GetConsolidatedPLReportQuery(FromDate, ToDate, BranchIds)` | `ConsolidatedPLReportDto` | 400 Bad Request nếu `ToDate < FromDate`. | Core Spec 8.4, API Contract 2.10 |
| 46 | Analytics & Reports | Menu Engineering BCG Matrix | Phân loại món ăn thành 4 nhóm (Stars, Plowhorses, Puzzles, Dogs) dựa trên sản lượng bán và biên lợi nhuận đóng góp. | `GetMenuEngineeringMatrixQuery(BranchId, FromDate, ToDate)` | `MenuEngineeringDto` | 400 Bad Request nếu khoảng thời gian không hợp lệ. | Core Spec 8.4, API Contract 2.10 |
| 47 | Analytics & Reports | Immutable Audit Trail Logging | Lưu vết bất biến toàn bộ thao tác nhạy cảm (đổi giá, hủy đơn, sửa chấm công, mở két) ghi rõ UserId, IP, Thời gian, OldValues, NewValues. | `GetAuditLogsQuery(UserId, Action, FromDate, ToDate, PageIndex, PageSize)` | `PagedResponse<AuditLogEntryDto>` | 403 Forbidden nếu không phải ChainAdmin. | Database 4.3, API Contract 2.10 |
| 48 | Analytics & Reports | Financial & Operations File Export | Xuất toàn bộ dữ liệu tài chính, kho, chấm công ra định dạng chuẩn Excel (.xlsx) / CSV phục vụ kế toán và thuế. | `ExportReportFileQuery(ReportType, Format, FromDate, ToDate)` | Binary File Stream (`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`) | 400 Bad Request nếu loại báo cáo không được hỗ trợ. | Core Spec 8.4, API Contract 2.10 |

---

## 2. Edge Cases Matrix

| # | Feature | Input Scenario | Observed / Specified Behavior |
|---|---|---|---|
| 01 | Dine-In Prepaid (Nhánh A) | Khách quét mã VietQR và thanh toán sau khi hết hạn 10 phút (TTL Expired). | Cổng PayOS gửi Webhook -> Hệ thống kiểm tra đơn đã ở trạng thái `Cancelled` do TTL -> Chuyển vào trạng thái `PaymentReceivedLate` -> Tự động kích hoạt thông báo tới Quản lý chi nhánh để hoàn tiền hoặc khôi phục đơn thủ công. |
| 02 | Dine-In Postpaid (Nhánh B) | Khách vừa trả tiền mặt cho nhân viên thu ngân, đồng thời quét mã VietQR trên hóa đơn để chuyển khoản. | Thu ngân bấm xác nhận tiền mặt trước -> Đơn chuyển sang `Completed`. Khi Webhook VietQR về sau, kiểm tra Idempotency Lock và trạng thái đơn đã `Completed` -> Ghi nhận giao dịch thừa `DuplicatePaymentAlert` và cảnh báo thu ngân hoàn tiền mặt cho khách. |
| 03 | QR Delivery | Khách nhập số điện thoại sai định dạng (ví dụ: 9 chữ số hoặc chữ cái) hoặc địa chỉ chỉ có 3 chữ cái. | `FluentValidation` chặn ngay tại Ingress Pipeline, trả về HTTP 400 Bad Request RFC 7807 ProblemDetails với thông báo lỗi chi tiết từng trường dữ liệu trước khi chạm vào Database. |
| 04 | QR Delivery | Khách cố tình chọn phương thức thanh toán tiền mặt (COD) qua API giả lập. | Validator từ chối với HTTP 422: "Đơn hàng Delivery bắt buộc phải thanh toán 100% chuyển khoản VietQR trước khi chế biến". |
| 05 | Takeaway Web POS Loyalty | Khách hàng chỉ có 8 ly tích lũy nhưng thu ngân cố tình bấm đổi 1 ly miễn phí. | Backend kiểm tra `customers.cup_balance >= 10`. Do `8 < 10`, ném `DomainException` vi phạm quy tắc nghiệp vụ, trả về HTTP 422 Unprocessable Entity: "Khách hàng chưa đủ 10 ly để quy đổi quà tặng". |
| 06 | Takeaway Web POS Loyalty | Khách gọi đơn Dine-In hoặc Delivery và yêu cầu tích lũy vào quỹ 10 ly. | Nghiệp vụ quy định **CHỈ TÍCH VÀ ĐỔI LY CHO ĐƠN TAKEAWAY**. Khi tạo đơn `DineIn` hoặc `Delivery`, trường `LoyaltyCupTransactions` hoàn toàn không sinh bản ghi tích lũy. |
| 07 | WiFi-Locked Attendance | Nhân viên đứng ở quán nhưng bật 4G/5G để chấm công hoặc kết nối WiFi quán cà phê kế bên. | Địa chỉ IP gửi lên không thuộc `allowed_ip_subnets` hoặc BSSID không khớp bảng `branch_wifi_configs` -> Trả về HTTP 403 Forbidden với cảnh báo: "Bạn chưa kết nối đúng WiFi chi nhánh". |
| 08 | WiFi-Locked Attendance | Nhân viên chấm công vào ca 2 lần liên tiếp trong vòng 5 phút mà chưa ra ca. | Hệ thống kiểm tra bản ghi chấm công gần nhất của nhân viên trong ngày. Nếu đã có `check_in_time` mà chưa có `check_out_time`, từ chối tạo lượt vào ca mới (HTTP 409 Conflict). |
| 09 | Kitchen KDS 86-Toggle | Khách hàng đang mở giỏ hàng chứa món "Cà Phê Muối" trên PWA thì Barista tại quầy gạt công tắc 86-out khóa món. | Khi khách bấm "Đặt Hàng", Backend kiểm tra `product_branch_prices.is_available_86 == false` -> Trả về HTTP 422: "Món Cà Phê Muối vừa hết hàng tại chi nhánh. Vui lòng chọn món khác". Đồng thời SignalR `KitchenHub` phát sự kiện `Item86Toggled` cập nhật ngay menu trên client. |
| 10 | Cash Drawer Shift Close | Số tiền mặt thực tế kiểm đếm lệch so với hệ thống tính toán (ví dụ: Thiếu 150.000 VNĐ). | Do `\|-150.000đ\| > 50.000đ`, hệ thống bắt buộc Quản lý phải điền `varianceNotes` giải trình lý do. Nếu bỏ trống, validator trả về HTTP 422: "Chênh lệch két tiền vượt ngưỡng 50.000 VNĐ bắt buộc phải có nội dung giải trình chi tiết". |
| 11 | PayOS Webhook Concurrency | Cổng PayOS gửi đồng thời 2 webhook trùng lặp do cơ chế retry mạng. | Redis Distributed Lock (`lock:webhook:payos:{paymentLinkId}`) chỉ cho phép 1 luồng thực thi trong 60 giây. Luồng thứ 2 gặp khóa đã tồn tại -> Trả về ngay HTTP 200 OK mà không cập nhật DB lần 2. |
| 12 | Customer Reviews Alert | Khách gửi đánh giá 1 sao hoặc 2 sao kèm lời phàn nàn về đồ uống. | Database Trigger / Domain Event tự động thiết lập `is_urgent_alert = true` và phát ngay sự kiện `LowRatingAlert` qua SignalR `NotificationHub` tới tài khoản Quản lý chi nhánh để xử lý trong 3 phút. |

---

## 3. Đặc Tả Chi Tiết 25 Entity Classes (Domain Layer — 3NF)

Toàn bộ các thực thể kế thừa từ `BaseEntity` (Khóa chính `Guid Id`, `CreatedAtUtc`, `UpdatedAtUtc`) hoặc `AuditableEntity` (thêm `CreatedBy`, `LastModifiedBy`, `IsDeleted`, `DeletedAtUtc`).

### 3.1 Nhóm 1: Hệ Thống & Chi Nhánh (Core & Branches)

#### 1. `Branch` (`branches`)
```csharp
public class Branch : AuditableEntity
{
    public string Code { get; set; } = null!; // UK, MaxLength(50)
    public string Name { get; set; } = null!; // MaxLength(150)
    public string Address { get; set; } = null!; // MaxLength(300)
    public string Phone { get; set; } = null!; // MaxLength(20)
    public string OperatingHours { get; set; } = "07:00 - 22:30"; // MaxLength(100)
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual ICollection<BranchWifiConfig> WifiConfigs { get; set; } = new List<BranchWifiConfig>();
    public virtual ICollection<Table> Tables { get; set; } = new List<Table>();
    public virtual ICollection<User> Users { get; set; } = new List<User>();
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
    public virtual ICollection<Shift> Shifts { get; set; } = new List<Shift>();
    public virtual ICollection<Attendance> Attendances { get; set; } = new List<Attendance>();
    public virtual ICollection<ProductBranchPrice> ProductBranchPrices { get; set; } = new List<ProductBranchPrice>();
}
```

#### 2. `BranchWifiConfig` (`branch_wifi_configs`)
```csharp
public class BranchWifiConfig : BaseEntity
{
    public Guid BranchId { get; set; }
    public string SsidName { get; set; } = null!; // MaxLength(100)
    public string BssidList { get; set; } = null!; // Text: "00:14:22:01:23:45,00:14:22:01:23:46"
    public string AllowedIpSubnets { get; set; } = null!; // Text: "192.168.1.0/24"
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
}
```

#### 3. `Table` (`tables`)
```csharp
public class Table : BaseEntity
{
    public Guid BranchId { get; set; }
    public string TableNumber { get; set; } = null!; // MaxLength(50), UK(BranchId, TableNumber)
    public string Zone { get; set; } = "Tầng 1"; // MaxLength(50)
    public int Capacity { get; set; } = 4; // CHECK > 0
    public string? QrCodeUrl { get; set; } // MaxLength(500)
    public TableStatus Status { get; set; } = TableStatus.Available; // Enum: Available, Occupied, AwaitingFood, Cleaning, Inactive
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
}
```

---

### 3.2 Nhóm 2: Người Dùng & Phân Quyền RBAC (Users & Roles)

#### 4. `User` (`users`)
```csharp
public class User : AuditableEntity
{
    public Guid? BranchId { get; set; }
    public string Username { get; set; } = null!; // UK, MaxLength(100)
    public string PasswordHash { get; set; } = null!; // MaxLength(255)
    public string FullName { get; set; } = null!; // MaxLength(150)
    public string? Email { get; set; } // MaxLength(150)
    public string? Phone { get; set; } // MaxLength(20)
    public string Status { get; set; } = "Active"; // Active, Inactive, Suspended

    // Navigation Properties
    public virtual Branch? Branch { get; set; }
    public virtual ICollection<UserRole> UserRoles { get; set; } = new List<UserRole>();
    public virtual ICollection<AuditLog> AuditLogs { get; set; } = new List<AuditLog>();
    public virtual ICollection<Shift> ShiftsAsCashier { get; set; } = new List<Shift>();
    public virtual ICollection<Attendance> Attendances { get; set; } = new List<Attendance>();
}
```

#### 5. `Role` (`roles`)
```csharp
public class Role : BaseEntity
{
    public string RoleName { get; set; } = null!; // UK, MaxLength(50) - ChainAdmin, BranchManager, BaristaStaff, CashierStaff, ServiceStaff
    public string? Description { get; set; } // MaxLength(255)

    // Navigation Properties
    public virtual ICollection<UserRole> UserRoles { get; set; } = new List<UserRole>();
}
```

#### 6. `UserRole` (`user_roles`)
```csharp
public class UserRole
{
    public Guid UserId { get; set; }
    public Guid RoleId { get; set; }
    public DateTime AssignedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual User User { get; set; } = null!;
    public virtual Role Role { get; set; } = null!;
}
```

#### 7. `AuditLog` (`audit_logs`)
```csharp
public class AuditLog
{
    public Guid AuditId { get; set; } = Guid.NewGuid();
    public Guid? UserId { get; set; }
    public string Action { get; set; } = null!; // MaxLength(100)
    public string EntityName { get; set; } = null!; // MaxLength(100)
    public string EntityId { get; set; } = null!; // MaxLength(100)
    public string? OldValues { get; set; } // JSONB
    public string? NewValues { get; set; } // JSONB
    public string? IpAddress { get; set; } // MaxLength(50)
    public DateTime TimestampUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual User? User { get; set; }
}
```

---

### 3.3 Nhóm 3: Thực Đơn, Món Ăn & Định Lượng BOM (Menu & BOM)

#### 8. `Category` (`categories`)
```csharp
public class Category : AuditableEntity
{
    public string Name { get; set; } = null!; // MaxLength(100)
    public string? Description { get; set; }
    public int DisplayOrder { get; set; } = 0;
    public string? ImageUrl { get; set; } // MaxLength(500)
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual ICollection<Product> Products { get; set; } = new List<Product>();
}
```

#### 9. `Product` (`products`)
```csharp
public class Product : AuditableEntity
{
    public Guid CategoryId { get; set; }
    public string Sku { get; set; } = null!; // UK, MaxLength(50)
    public string Name { get; set; } = null!; // MaxLength(150)
    public string? Description { get; set; }
    public decimal BasePrice { get; set; } // Precision(12,0), CHECK >= 0
    public string? ImageUrl { get; set; } // MaxLength(500)
    public bool IsAvailable { get; set; } = true;
    public bool IsBestSeller { get; set; } = false;
    public int CaloriesApprox { get; set; } = 0;
    public string? AllergenInfo { get; set; }

    // Navigation Properties
    public virtual Category Category { get; set; } = null!;
    public virtual ICollection<ProductSize> ProductSizes { get; set; } = new List<ProductSize>();
    public virtual ICollection<ProductBranchPrice> BranchPrices { get; set; } = new List<ProductBranchPrice>();
    public virtual ICollection<ProductModifier> ProductModifiers { get; set; } = new List<ProductModifier>();
    public virtual ICollection<RecipeBom> RecipeBoms { get; set; } = new List<RecipeBom>();
    public virtual ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
    public virtual ICollection<CustomerReview> CustomerReviews { get; set; } = new List<CustomerReview>();
}
```

#### 10. `ProductSize` (`product_sizes`)
```csharp
public class ProductSize : BaseEntity
{
    public Guid ProductId { get; set; }
    public string SizeName { get; set; } = null!; // MaxLength(50) - Size S, Size M, Size L
    public decimal PriceAdjustment { get; set; } = 0; // Precision(12,0), CHECK >= 0
    public int DisplayOrder { get; set; } = 0;

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual ICollection<RecipeBom> RecipeBoms { get; set; } = new List<RecipeBom>();
    public virtual ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
}
```

#### 11. `ProductBranchPrice` (`product_branch_prices`)
```csharp
public class ProductBranchPrice
{
    public Guid BranchPriceId { get; set; } = Guid.NewGuid();
    public Guid ProductId { get; set; }
    public Guid BranchId { get; set; }
    public decimal PriceOverride { get; set; } // Precision(12,0), CHECK >= 0
    public bool IsAvailable86 { get; set; } = true; // 86-Toggle
    public DateTime UpdatedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual Branch Branch { get; set; } = null!;
}
```

#### 12. `Modifier` (`modifiers`)
```csharp
public class Modifier : BaseEntity
{
    public string Name { get; set; } = null!; // MaxLength(100)
    public ModifierType Type { get; set; } // Enum: Sweetness, Ice, Topping, MilkOption
    public decimal ExtraPrice { get; set; } = 0; // Precision(12,0), CHECK >= 0
    public bool IsAvailable { get; set; } = true;

    // Navigation Properties
    public virtual ICollection<ProductModifier> ProductModifiers { get; set; } = new List<ProductModifier>();
    public virtual ICollection<OrderItemModifier> OrderItemModifiers { get; set; } = new List<OrderItemModifier>();
}
```

#### 13. `ProductModifier` (`product_modifiers`)
```csharp
public class ProductModifier
{
    public Guid ProductId { get; set; }
    public Guid ModifierId { get; set; }
    public bool IsDefault { get; set; } = false;
    public int MaxQuantity { get; set; } = 1; // CHECK >= 1

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual Modifier Modifier { get; set; } = null!;
}
```

#### 14. `Ingredient` (`ingredients`)
```csharp
public class Ingredient : AuditableEntity
{
    public string Code { get; set; } = null!; // UK, MaxLength(50)
    public string Name { get; set; } = null!; // MaxLength(150)
    public string Unit { get; set; } = null!; // ml, g, piece, can, pack
    public decimal CurrentStock { get; set; } = 0; // Precision(10,3), CHECK >= 0
    public decimal MinStockThreshold { get; set; } = 0; // Precision(10,3), CHECK >= 0
    public decimal UnitCost { get; set; } = 0; // Precision(12,0), CHECK >= 0

    // Navigation Properties
    public virtual ICollection<RecipeBom> RecipeBoms { get; set; } = new List<RecipeBom>();
}
```

#### 15. `RecipeBom` (`recipes_bom`)
```csharp
public class RecipeBom : AuditableEntity
{
    public Guid RecipeId { get; set; } = Guid.NewGuid();
    public Guid ProductId { get; set; }
    public Guid SizeId { get; set; }
    public Guid IngredientId { get; set; }
    public decimal StandardQuantity { get; set; } // Precision(10,3), CHECK > 0 (gam/ml)
    public decimal WastagePercentage { get; set; } = 0; // Precision(5,2), CHECK >= 0

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual ProductSize ProductSize { get; set; } = null!;
    public virtual Ingredient Ingredient { get; set; } = null!;
}
```

---

### 3.4 Nhóm 4: Đơn Hàng & Thanh Toán (Orders & Payments)

#### 16. `Order` (`orders`)
```csharp
public class Order : AuditableEntity
{
    public Guid BranchId { get; set; }
    public Guid? TableId { get; set; }
    public Guid? CustomerId { get; set; }
    public string OrderCode { get; set; } = null!; // UK, MaxLength(50)
    public OrderType OrderType { get; set; } // Enum: DineIn, TakeAway, Delivery
    public OrderStatus Status { get; set; } = OrderStatus.PendingPayment; // Enum: PendingPayment, Paid, Confirmed, Preparing, Ready, Completed, Cancelled
    public decimal SubTotal { get; set; } // Precision(12,0), CHECK >= 0
    public decimal DiscountAmount { get; set; } = 0; // Precision(12,0)
    public decimal DeliveryFee { get; set; } = 0; // Precision(12,0) - 20.000 VNĐ cho Delivery
    public decimal TotalAmount { get; set; } // Precision(12,0), CHECK >= 0
    public string? DeliveryAddress { get; set; } // MaxLength(500)
    public string? RecipientName { get; set; } // MaxLength(150)
    public string? RecipientPhone { get; set; } // MaxLength(20)
    public string? DeliveryNotes { get; set; }
    public DateTime? ExpiresAtUtc { get; set; } // TTL 10m cho VietQR
    public DateTime? PaidAtUtc { get; set; }
    public DateTime? CompletedAtUtc { get; set; }

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual Table? Table { get; set; }
    public virtual Customer? Customer { get; set; }
    public virtual ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
    public virtual ICollection<Payment> Payments { get; set; } = new List<Payment>();
    public virtual ICollection<CustomerReview> CustomerReviews { get; set; } = new List<CustomerReview>();
    public virtual ICollection<LoyaltyCupTransaction> LoyaltyCupTransactions { get; set; } = new List<LoyaltyCupTransaction>();
}
```

#### 17. `OrderItem` (`order_items`)
```csharp
public class OrderItem : BaseEntity
{
    public Guid OrderId { get; set; }
    public Guid ProductId { get; set; }
    public Guid SizeId { get; set; }
    public int Quantity { get; set; } = 1; // CHECK > 0
    public decimal UnitPrice { get; set; } // Precision(12,0), CHECK >= 0
    public decimal SubtotalPrice { get; set; } // Precision(12,0), CHECK >= 0
    public string? Note { get; set; } // MaxLength(255)
    public string ItemStatus { get; set; } = "Pending"; // Pending, Preparing, Ready, Served, Cancelled

    // Navigation Properties
    public virtual Order Order { get; set; } = null!;
    public virtual Product Product { get; set; } = null!;
    public virtual ProductSize ProductSize { get; set; } = null!;
    public virtual ICollection<OrderItemModifier> OrderItemModifiers { get; set; } = new List<OrderItemModifier>();
}
```

#### 18. `OrderItemModifier` (`order_item_modifiers`)
```csharp
public class OrderItemModifier
{
    public Guid ItemModId { get; set; } = Guid.NewGuid();
    public Guid OrderItemId { get; set; }
    public Guid ModifierId { get; set; }
    public int Quantity { get; set; } = 1; // CHECK > 0
    public decimal ExtraPrice { get; set; } = 0; // Precision(12,0), CHECK >= 0
    public DateTime CreatedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual OrderItem OrderItem { get; set; } = null!;
    public virtual Modifier Modifier { get; set; } = null!;
}
```

#### 19. `Payment` (`payments`)
```csharp
public class Payment : BaseEntity
{
    public Guid OrderId { get; set; }
    public PaymentMethod PaymentMethod { get; set; } // Enum: VietQR, Cash
    public decimal Amount { get; set; } // Precision(12,0), CHECK >= 0
    public string? TransactionCode { get; set; } // UK, MaxLength(100)
    public PaymentStatus Status { get; set; } = PaymentStatus.Pending; // Enum: Pending, Paid, Failed, Refunded
    public string? PayosPaymentLinkId { get; set; } // MaxLength(100)
    public DateTime? PaidAtUtc { get; set; }

    // Navigation Properties
    public virtual Order Order { get; set; } = null!;
}
```

---

### 3.5 Nhóm 5: CRM, Loyalty & Đánh Giá (CRM & Reviews)

#### 20. `Customer` (`customers`)
```csharp
public class Customer : AuditableEntity
{
    public string PhoneNumber { get; set; } = null!; // UK, MaxLength(20)
    public string? FullName { get; set; } // MaxLength(150)
    public string? Email { get; set; } // MaxLength(150)
    public DateOnly? BirthDate { get; set; }
    public string MembershipTier { get; set; } = "Standard"; // Standard, Silver, Gold, Diamond
    public int CupBalance { get; set; } = 0; // CHECK >= 0 (Quỹ ly Takeaway)
    public int TotalPoints { get; set; } = 0; // CHECK >= 0
    public DateTime LastVisitedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
    public virtual ICollection<LoyaltyCupTransaction> LoyaltyCupTransactions { get; set; } = new List<LoyaltyCupTransaction>();
    public virtual ICollection<CustomerReview> CustomerReviews { get; set; } = new List<CustomerReview>();
}
```

#### 21. `LoyaltyCupTransaction` (`loyalty_cup_transactions`)
```csharp
public class LoyaltyCupTransaction
{
    public Guid TransId { get; set; } = Guid.NewGuid();
    public Guid CustomerId { get; set; }
    public Guid? OrderId { get; set; }
    public int CupsEarned { get; set; } = 0; // CHECK >= 0
    public int CupsRedeemed { get; set; } = 0; // CHECK >= 0 (Trừ 10 khi đổi)
    public LoyaltyTransactionType TransactionType { get; set; } // Enum: TakeawayAccumulate, TakeawayRedeem10Free, ManualAdjustment
    public string? Notes { get; set; } // MaxLength(255)
    public DateTime CreatedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual Customer Customer { get; set; } = null!;
    public virtual Order? Order { get; set; }
}
```

#### 22. `Voucher` (`vouchers`)
```csharp
public class Voucher : AuditableEntity
{
    public string Code { get; set; } = null!; // UK, MaxLength(50)
    public VoucherDiscountType DiscountType { get; set; } // Enum: Percentage, FixedAmount
    public decimal DiscountValue { get; set; } // Precision(12,2), CHECK > 0
    public decimal MinOrderValue { get; set; } = 0; // Precision(12,0), CHECK >= 0
    public decimal? MaxDiscountAmount { get; set; } // Precision(12,0), CHECK >= 0
    public DateTime StartDateUtc { get; set; }
    public DateTime EndDateUtc { get; set; } // CHECK EndDateUtc > StartDateUtc
    public int UsageLimit { get; set; } = 1000; // CHECK >= 0
    public int UsedCount { get; set; } = 0; // CHECK >= 0
    public bool IsActive { get; set; } = true;
}
```

#### 23. `CustomerReview` (`customer_reviews`)
```csharp
public class CustomerReview
{
    public Guid ReviewId { get; set; } = Guid.NewGuid();
    public Guid OrderId { get; set; }
    public Guid? ProductId { get; set; }
    public Guid? CustomerId { get; set; }
    public int RatingStars { get; set; } // CHECK BETWEEN 1 AND 5
    public string? Comment { get; set; }
    public string? PhotoUrls { get; set; } // JSONB mảng URLs
    public bool IsAnonymous { get; set; } = false;
    public bool IsApproved { get; set; } = false;
    public bool IsUrgentAlert { get; set; } = false; // Tự động true nếu Rating <= 2
    public DateTime CreatedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual Order Order { get; set; } = null!;
    public virtual Product? Product { get; set; }
    public virtual Customer? Customer { get; set; }
}
```

---

### 3.6 Nhóm 6: Vận Hành Ca Két & Chấm Công (Operations & HRM)

#### 24. `Shift` (`shifts`)
```csharp
public class Shift
{
    public Guid ShiftId { get; set; } = Guid.NewGuid();
    public Guid BranchId { get; set; }
    public Guid CashierId { get; set; }
    public DateTime OpeningTimeUtc { get; set; } = DateTime.UtcNow;
    public DateTime? ClosingTimeUtc { get; set; }
    public decimal InitialCash { get; set; } // Precision(12,0), CHECK >= 0
    public decimal? ActualCashCounted { get; set; } // Precision(12,0), CHECK >= 0
    public decimal SystemCashCalculated { get; set; } = 0; // Precision(12,0)
    public decimal CashDifference { get; set; } = 0; // Precision(12,0)
    public string? ShiftNotes { get; set; }
    public ShiftStatus Status { get; set; } = ShiftStatus.Open; // Enum: Open, Closed, Audited
    public DateTime CreatedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual User Cashier { get; set; } = null!;
}
```

#### 25. `Attendance` (`attendances`)
```csharp
public class Attendance
{
    public Guid AttendanceId { get; set; } = Guid.NewGuid();
    public Guid BranchId { get; set; }
    public Guid UserId { get; set; }
    public string EmployeeCode { get; set; } = null!; // MaxLength(50)
    public DateTime CheckInTimeUtc { get; set; } = DateTime.UtcNow;
    public DateTime? CheckOutTimeUtc { get; set; }
    public string VerifiedIp { get; set; } = null!; // MaxLength(50)
    public string VerifiedBssid { get; set; } = null!; // MaxLength(50)
    public AttendanceStatus Status { get; set; } = AttendanceStatus.OnTime; // Enum: OnTime, Late, Overtime, Excused
    public DateTime CreatedAtUtc { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual User User { get; set; } = null!;
}
```

---

## 4. Đặc Tả 10 Phân Hệ CQRS Feature Modules (Application Layer)

Mỗi Feature Module trong `SmartFB.Application/Features/<FeatureName>/` có cấu trúc:
- `Commands/` (Command class + CommandHandler + IRequest)
- `Queries/` (Query class + QueryHandler + IRequest)
- `DTOs/` (C# Records truyền nhận dữ liệu)
- `Validators/` (FluentValidation `AbstractValidator<T>`)

### 4.1 Module 1: `Auth`
- **Commands**:
  * `LoginUserCommand(string Username, string Password) -> ApiResponse<AuthResultDto>`
  * `RefreshTokenCommand(string RefreshToken) -> ApiResponse<AuthResultDto>`
  * `LogoutUserCommand(Guid UserId) -> ApiResponse<bool>`
  * `CreateUserCommand(string EmployeeCode, string FullName, string Email, string Phone, string Password, string Role, Guid BranchId) -> ApiResponse<UserProfileDto>`
  * `UpdateUserCommand(Guid Id, string FullName, string Phone, string Role, Guid BranchId, bool IsActive) -> ApiResponse<UserProfileDto>`
- **Queries**:
  * `GetUsersQuery(Guid? BranchId, string? Role, int PageIndex, int PageSize) -> PagedResponse<UserProfileDto>`
  * `GetUserByIdQuery(Guid Id) -> ApiResponse<UserProfileDto>`
  * `GetRolesQuery() -> ApiResponse<List<RoleDto>>`
- **Validators**: `LoginUserCommandValidator`, `CreateUserCommandValidator`, `RefreshTokenCommandValidator`.

### 4.2 Module 2: `Branches`
- **Commands**:
  * `CreateBranchCommand(string Code, string Name, string Address, string Phone, string OperatingHours) -> ApiResponse<BranchDto>`
  * `UpdateBranchCommand(Guid Id, string Name, string Address, string Phone, string OperatingHours, bool IsActive) -> ApiResponse<BranchDto>`
  * `DeleteBranchCommand(Guid Id) -> ApiResponse<bool>` (Soft Delete)
  * `UpdateBranchWifiConfigsCommand(Guid BranchId, List<WifiConfigItemDto> WifiConfigs) -> ApiResponse<bool>`
- **Queries**:
  * `GetBranchesQuery(bool IncludeInactive) -> ApiResponse<List<BranchDto>>`
  * `GetBranchByIdQuery(Guid Id) -> ApiResponse<BranchDto>`
  * `GetBranchWifiConfigsQuery(Guid BranchId) -> ApiResponse<List<WifiConfigItemDto>>`
- **Validators**: `CreateBranchCommandValidator`, `UpdateBranchWifiConfigsValidator`.

### 4.3 Module 3: `Tables`
- **Commands**:
  * `CreateTableCommand(Guid BranchId, string TableNumber, string Zone, int Capacity) -> ApiResponse<TableDto>`
  * `UpdateTableCommand(Guid Id, string TableNumber, string Zone, int Capacity) -> ApiResponse<TableDto>`
  * `UpdateTableStatusCommand(Guid Id, TableStatus NewStatus) -> ApiResponse<bool>`
  * `GenerateTableQrCommand(Guid TableId) -> ApiResponse<TableQrDto>`
- **Queries**:
  * `GetBranchTablesQuery(Guid BranchId) -> ApiResponse<List<TableDto>>`
  * `GetTableByIdQuery(Guid Id) -> ApiResponse<TableDto>`
- **Validators**: `CreateTableCommandValidator`, `UpdateTableStatusCommandValidator`.

### 4.4 Module 4: `Products`
- **Commands**:
  * `CreateProductCommand(Guid CategoryId, string Sku, string Name, string Description, decimal BasePrice, string ImageUrl, int Calories, List<SizeOptionDto> Sizes, List<BomRecipeDto> BomRecipes) -> ApiResponse<ProductDto>`
  * `UpdateProductCommand(Guid Id, string Name, string Description, decimal BasePrice, string ImageUrl, int Calories, bool IsAvailable, bool IsBestSeller) -> ApiResponse<ProductDto>`
  * `SoftDeleteProductCommand(Guid Id) -> ApiResponse<bool>`
  * `ReplaceProductCommand(Guid OldProductId, Guid NewProductId, string Reason) -> ApiResponse<bool>`
  * `ReorderCategoriesCommand(List<CategoryOrderItemDto> OrderedCategories) -> ApiResponse<bool>`
  * `CreateSeasonalMenuCommand(string Title, DateTime ActiveFrom, DateTime ActiveTo, List<Guid> ProductIds) -> ApiResponse<SeasonalMenuDto>`
  * `SetRegionalPriceCommand(Guid BranchId, Guid ProductId, decimal PriceOverride) -> ApiResponse<bool>`
- **Queries**:
  * `GetBranchMenuQuery(Guid BranchId, Guid? CategoryId, string? Search) -> ApiResponse<BranchMenuDto>`
  * `GetProductByIdQuery(Guid Id) -> ApiResponse<ProductDetailDto>`
  * `GetProductRecipeQuery(Guid ProductId, string SizeCode) -> ApiResponse<RecipeBomDetailDto>`
  * `GetCategoriesQuery() -> ApiResponse<List<CategoryDto>>`
- **Validators**: `CreateProductCommandValidator`, `ReplaceProductCommandValidator`, `ReorderCategoriesValidator`.

### 4.5 Module 5: `Orders`
- **Commands**:
  * `CreateDineInPrepaidOrderCommand(Guid BranchId, Guid TableId, string? CustomerPhone, string? CustomerNote, string? VoucherCode, List<OrderItemRequestDto> Items) -> ApiResponse<PrepaidOrderResultDto>`
  * `CreateDineInPostpaidOrderCommand(Guid BranchId, Guid TableId, string? CustomerPhone, string? CustomerNote, List<OrderItemRequestDto> Items) -> ApiResponse<PostpaidOrderResultDto>`
  * `CreateDeliveryOrderCommand(Guid BranchId, string RecipientName, string RecipientPhone, string DeliveryAddress, string? CustomerNote, List<OrderItemRequestDto> Items) -> ApiResponse<DeliveryOrderResultDto>`
  * `CreateTakeawayOrderCommand(Guid BranchId, string CustomerPhone, string? CustomerName, bool RedeemFreeCup, Guid? FreeProductId, PaymentMethod PaymentMethod, decimal? CashGiven, List<OrderItemRequestDto> Items) -> ApiResponse<TakeawayOrderResultDto>`
  * `CancelOrderCommand(Guid OrderId, string Reason) -> ApiResponse<bool>`
- **Queries**:
  * `GetOrderByIdQuery(Guid Id) -> ApiResponse<OrderDetailDto>`
  * `GetOrderTrackingQuery(Guid Id) -> ApiResponse<OrderTrackingDto>`
  * `GetOrderHistoryQuery(string CustomerPhone, int PageIndex, int PageSize) -> PagedResponse<OrderHistoryDto>`
- **Validators**: `CreateDineInPrepaidOrderValidator`, `CreateDeliveryOrderValidator`, `CreateTakeawayOrderValidator`.

### 4.6 Module 6: `Payments`
- **Commands**:
  * `GenerateVietQRCommand(Guid OrderId) -> ApiResponse<VietQrDto>`
  * `ProcessPayOSWebhookCommand(PayOSWebhookData Data) -> ApiResponse<bool>`
  * `ConfirmCashPaymentCommand(Guid OrderId, decimal ReceivedAmount) -> ApiResponse<CashConfirmationResultDto>`
- **Queries**:
  * `GetPaymentStatusQuery(Guid OrderId) -> ApiResponse<PaymentStatusDto>`
- **Validators**: `ConfirmCashPaymentCommandValidator`.

### 4.7 Module 7: `Attendances`
- **Commands**:
  * `WifiClockInCommand(Guid BranchId, string EmployeeCode, string ClientBssid, string ClientIp) -> ApiResponse<AttendanceRecordDto>`
  * `WifiClockOutCommand(Guid BranchId, string EmployeeCode, string ClientBssid, string ClientIp) -> ApiResponse<AttendanceRecordDto>`
- **Queries**:
  * `GetBranchAttendancesQuery(Guid BranchId, DateTime Date) -> ApiResponse<List<AttendanceRecordDto>>`
  * `GetMyAttendanceHistoryQuery(Guid UserId, int Month, int Year) -> ApiResponse<List<AttendanceRecordDto>>`
- **Validators**: `WifiClockInValidator`, `WifiClockOutValidator`.

### 4.8 Module 8: `KitchenKDS`
- **Commands**:
  * `UpdateKdsOrderStatusCommand(Guid OrderId, OrderStatus NewStatus) -> ApiResponse<bool>` (Kích hoạt trừ tồn kho BOM khi `Ready`)
  * `StartKdsBatchCommand(List<Guid> OrderItemIds) -> ApiResponse<KdsBatchResultDto>`
  * `CompleteKdsBatchCommand(Guid BatchId) -> ApiResponse<bool>`
  * `ToggleProductAvailabilityCommand(Guid BranchId, Guid ProductId, bool IsAvailable) -> ApiResponse<Item86ToggledEvent>`
- **Queries**:
  * `GetKdsTicketsQuery(Guid BranchId, string? StationType) -> ApiResponse<List<KdsTicketDto>>`
  * `GetKdsSlaMetricsQuery(Guid BranchId, DateTime Date) -> ApiResponse<KdsSlaMetricsDto>`
- **Validators**: `UpdateKdsOrderStatusValidator`, `ToggleProductAvailabilityValidator`.

### 4.9 Module 9: `ShiftsAndCash`
- **Commands**:
  * `OpenCashShiftCommand(Guid BranchId, decimal InitialCash, Dictionary<string, int> CashDenominations) -> ApiResponse<ShiftDto>`
  * `CloseCashShiftCommand(Guid ShiftId, Dictionary<string, int> ActualCashDenominations, decimal TotalActualCash, string? VarianceNotes) -> ApiResponse<ZReportResultDto>`
  * `CreateBarExportRequisitionCommand(Guid BranchId, List<InventoryItemRequisitionDto> Items) -> ApiResponse<BarExportRequisitionDto>`
  * `CreateSupplierStockImportCommand(Guid BranchId, string SupplierName, decimal TotalCost, string InvoiceImageUrl, List<StockImportItemDto> Items) -> ApiResponse<StockImportDto>`
  * `AuditInventoryVarianceCommand(Guid BranchId, List<StockAuditItemDto> AuditItems) -> ApiResponse<StockAuditReportDto>`
  * `CallStaffCommand(Guid TableId, string Reason) -> ApiResponse<bool>`
  * `ResolveServiceCallCommand(Guid ServiceCallId) -> ApiResponse<bool>`
  * `CreateReviewCommand(Guid OrderId, int Rating, string? Comment, List<string>? PhotoUrls, bool IsAnonymous) -> ApiResponse<ReviewDto>`
  * `ModerateReviewPhotoCommand(Guid ReviewId, Guid PhotoId, bool IsApproved) -> ApiResponse<bool>`
- **Queries**:
  * `GetCurrentShiftQuery(Guid BranchId) -> ApiResponse<ShiftDto>`
  * `GetShiftByIdQuery(Guid ShiftId) -> ApiResponse<ZReportResultDto>`
  * `GetStockLevelsQuery(Guid BranchId) -> ApiResponse<List<StockLevelDto>>`
- **Validators**: `OpenCashShiftValidator`, `CloseCashShiftValidator`, `CreateReviewValidator`.

### 4.10 Module 10: `AdminAndAnalytics`
- **Commands**:
  * `MineMarketBasketCombosCommand(Guid? BranchId, double MinSupport, double MinConfidence) -> ApiResponse<List<ComboCandidateDto>>`
  * `ApproveAiComboCommand(string ComboCandidateId, string ComboName, decimal FinalPrice, DateTime ActiveFrom, DateTime ActiveTo) -> ApiResponse<ComboDto>`
  * `CreateVoucherCommand(string Code, VoucherDiscountType DiscountType, decimal DiscountValue, decimal MinOrderAmount, decimal? MaxDiscountAmount, DateTime StartDate, DateTime EndDate, int UsageLimit) -> ApiResponse<VoucherDto>`
  * `ValidateVoucherCommand(string VoucherCode, decimal OrderAmount, Guid BranchId) -> ApiResponse<VoucherValidationResultDto>`
  * `IdentifyCustomerCommand(string Phone, Guid BranchId) -> ApiResponse<CustomerProfileDto>`
- **Queries**:
  * `GetGeminiRecommendationQuery(Guid BranchId, string UserQuery, string? CustomerPhone) -> ApiResponse<AiRecommendationResultDto>`
  * `GetConsolidatedPLReportQuery(DateTime FromDate, DateTime ToDate, List<Guid>? BranchIds) -> ApiResponse<ConsolidatedPLReportDto>`
  * `GetMenuEngineeringMatrixQuery(Guid? BranchId, DateTime FromDate, DateTime ToDate) -> ApiResponse<MenuEngineeringDto>`
  * `GetAuditLogsQuery(Guid? UserId, string? Action, DateTime? FromDate, DateTime? ToDate, int PageIndex, int PageSize) -> PagedResponse<AuditLogEntryDto>`
  * `ExportReportFileQuery(string ReportType, string Format, DateTime FromDate, DateTime ToDate) -> FileStreamResult`
- **Validators**: `ApproveAiComboValidator`, `CreateVoucherValidator`, `IdentifyCustomerValidator`.

---

## 5. Đặc Tả 25 EF Core Configurations (Infrastructure Layer)

Toàn bộ 25 Configurations kế thừa `IEntityTypeConfiguration<T>` trong `SmartFB.Infrastructure/Persistence/Configurations/`:

1. `BranchConfiguration`: `builder.ToTable("branches")`, PK `branch_id`, UK `code`, Global query filter `IsDeleted == false`.
2. `BranchWifiConfigConfiguration`: `builder.ToTable("branch_wifi_configs")`, PK `wifi_config_id`, FK `BranchId` CASCADE, Index `(branch_id, is_active)`.
3. `TableConfiguration`: `builder.ToTable("tables")`, PK `table_id`, FK `BranchId` CASCADE, UK `(branch_id, table_number)`, Enum `TableStatus` as string.
4. `UserConfiguration`: `builder.ToTable("users")`, PK `user_id`, UK `username`, UK `email`, Global filter `IsDeleted == false`.
5. `RoleConfiguration`: `builder.ToTable("roles")`, PK `role_id`, UK `role_name`.
6. `UserRoleConfiguration`: `builder.ToTable("user_roles")`, Composite PK `(user_id, role_id)`, FKs CASCADE.
7. `AuditLogConfiguration`: `builder.ToTable("audit_logs")`, PK `audit_id`, Column `old_values` & `new_values` as `jsonb`, GIN Index on `new_values`.
8. `CategoryConfiguration`: `builder.ToTable("categories")`, PK `category_id`, Global filter `IsDeleted == false`.
9. `ProductConfiguration`: `builder.ToTable("products")`, PK `product_id`, UK `sku`, FK `CategoryId` RESTRICT, FTS GIN Index on `name`, Precision(12,0) `base_price`, Global filter `IsDeleted == false`.
10. `ProductSizeConfiguration`: `builder.ToTable("product_sizes")`, PK `size_id`, UK `(product_id, size_name)`, FK `ProductId` CASCADE.
11. `ProductBranchPriceConfiguration`: `builder.ToTable("product_branch_prices")`, PK `branch_price_id`, UK `(branch_id, product_id)`, FKs CASCADE, Index `(branch_id, product_id, is_available_86)`.
12. `ModifierConfiguration`: `builder.ToTable("modifiers")`, PK `modifier_id`, Enum `ModifierType` as string, Precision(12,0) `extra_price`.
13. `ProductModifierConfiguration`: `builder.ToTable("product_modifiers")`, Composite PK `(product_id, modifier_id)`, FKs CASCADE.
14. `IngredientConfiguration`: `builder.ToTable("ingredients")`, PK `ingredient_id`, UK `code`, Precision(10,3) `current_stock` & `min_stock_threshold`, Global filter `IsDeleted == false`.
15. `RecipeBomConfiguration`: `builder.ToTable("recipes_bom")`, PK `recipe_id`, UK `(product_id, size_id, ingredient_id)`, Precision(10,3) `standard_quantity`, Precision(5,2) `wastage_percentage`.
16. `OrderConfiguration`: `builder.ToTable("orders")`, PK `order_id`, UK `order_code`, Enums `OrderType` & `OrderStatus` as string, Precision(12,0) `total_amount`, `sub_total`, `delivery_fee`, Composite Index `(branch_id, status, created_at)`.
17. `OrderItemConfiguration`: `builder.ToTable("order_items")`, PK `order_item_id`, FK `OrderId` CASCADE, FK `ProductId` RESTRICT, FK `SizeId` RESTRICT, Precision(12,0) `unit_price`, Index `(order_id, item_status)`.
18. `OrderItemModifierConfiguration`: `builder.ToTable("order_item_modifiers")`, PK `item_mod_id`, FK `OrderItemId` CASCADE, FK `ModifierId` RESTRICT, Precision(12,0) `extra_price`.
19. `PaymentConfiguration`: `builder.ToTable("payments")`, PK `payment_id`, UK `transaction_code`, Enums `PaymentMethod` & `PaymentStatus` as string, Precision(12,0) `amount`, Index `(order_id, status)`.
20. `CustomerConfiguration`: `builder.ToTable("customers")`, PK `customer_id`, UK `phone_number`, Index `phone_number`, Global filter `IsDeleted == false`.
21. `LoyaltyCupTransactionConfiguration`: `builder.ToTable("loyalty_cup_transactions")`, PK `trans_id`, FK `CustomerId` CASCADE, Enum `LoyaltyTransactionType` as string, Index `(customer_id, created_at DESC)`.
22. `VoucherConfiguration`: `builder.ToTable("vouchers")`, PK `voucher_id`, UK `code`, Enum `VoucherDiscountType` as string, Precision(12,2) `discount_value`, Global filter `IsDeleted == false`.
23. `CustomerReviewConfiguration`: `builder.ToTable("customer_reviews")`, PK `review_id`, Column `photo_urls` as `jsonb`, GIN Index on `photo_urls`, Partial Index on `(branch_id, rating_stars) WHERE is_urgent_alert = true`.
24. `ShiftConfiguration`: `builder.ToTable("shifts")`, PK `shift_id`, Enum `ShiftStatus` as string, Precision(12,0) `initial_cash`, `actual_cash_counted`, `system_cash_calculated`, `cash_difference`, Index `(branch_id, status, opening_time DESC)`.
25. `AttendanceConfiguration`: `builder.ToTable("attendances")`, PK `attendance_id`, FK `BranchId` RESTRICT, FK `UserId` CASCADE, Enum `AttendanceStatus` as string, Index `(branch_id, user_id, check_in_time DESC)`.

---

## 6. Đặc Tả 10 RESTful API Controllers (API Layer)

| Controller | Route Base | Actions & HTTP Methods | Quyền Hạn (Auth Policy) |
|---|---|---|---|
| `AuthController` | `/api/v1/auth`, `/api/v1/users`, `/api/v1/roles` | `POST /login`, `POST /refresh-token`, `POST /logout`, `GET /users`, `POST /users`, `PUT /users/{id}`, `GET /roles` | `Public`, `Authenticated`, `BranchManager`, `ChainAdmin` |
| `BranchesController` | `/api/v1/branches`, `/api/v1/branch-wifi-configs` | `GET /`, `POST /`, `GET /{id}`, `PUT /{id}`, `DELETE /{id}`, `GET /{id}/wifi-configs`, `PUT /{id}/wifi-configs` | `Public`, `ChainAdmin`, `BranchManager` |
| `TablesController` | `/api/v1/tables`, `/api/v1/branches/{branchId}/tables` | `GET /{branchId}/tables`, `POST /{branchId}/tables`, `PUT /tables/{id}`, `PATCH /tables/{id}/status`, `POST /tables/{id}/qr` | `Public`, `Staff`, `BranchManager`, `ChainAdmin` |
| `ProductsController` | `/api/v1/products`, `/api/v1/categories`, `/api/v1/seasonal-menus`, `/api/v1/pricing` | `GET /menu`, `POST /`, `PUT /{id}`, `DELETE /{id}`, `POST /{id}/replace`, `GET /{id}/recipe`, `GET /categories`, `PUT /categories/reorder`, `POST /seasonal-menus`, `PUT /pricing/regional` | `Public`, `BaristaStaff`, `BranchManager`, `ChainAdmin` |
| `OrdersController` | `/api/v1/orders` | `POST /dine-in/prepaid`, `POST /dine-in/postpaid`, `POST /delivery`, `POST /takeaway`, `GET /{id}`, `GET /{id}/tracking`, `GET /history`, `PATCH /{id}/cancel` | `Public`, `CashierStaff`, `BranchManager`, `ChainAdmin` |
| `PaymentsController` | `/api/v1/payments`, `/api/v1/webhooks/payos` | `POST /vietqr/generate`, `POST /webhooks/payos`, `POST /cash/confirm`, `GET /{orderId}/status` | `Public`, `Public (HMAC)`, `CashierStaff`, `BranchManager` |
| `AttendancesController` | `/api/v1/attendances` | `POST /wifi-checkin`, `POST /wifi-checkout`, `GET /branch/{branchId}`, `GET /my-history` | `Authenticated Staff`, `BranchManager`, `ChainAdmin` |
| `KitchenKdsController` | `/api/v1/kds` | `GET /tickets`, `PATCH /orders/{id}/status`, `POST /batch-start`, `PATCH /batch/{batchId}/complete`, `PATCH /products/{id}/86-toggle`, `GET /sla-metrics` | `BaristaStaff`, `BranchManager`, `ChainAdmin` |
| `ShiftsAndCashController` | `/api/v1/shifts`, `/api/v1/inventory`, `/api/v1/reviews`, `/api/v1/staff/service-calls` | `POST /shifts/open`, `POST /shifts/close`, `GET /shifts/current`, `POST /inventory/export-bar`, `POST /inventory/import-supplier`, `POST /inventory/audit-variance`, `POST /service-calls`, `PATCH /service-calls/{id}/resolve`, `POST /reviews`, `PATCH /reviews/{id}/moderate-photo` | `Public`, `CashierStaff`, `BranchManager`, `ChainAdmin` |
| `AdminAndAnalyticsController` | `/api/v1/admin`, `/api/v1/ai`, `/api/v1/reports`, `/api/v1/crm`, `/api/v1/vouchers` | `POST /ai/chatbot/recommend`, `POST /ai/combos/mine`, `POST /ai/combos/approve`, `GET /reports/pl-consolidated`, `GET /reports/menu-engineering`, `GET /admin/audit-logs`, `GET /admin/reports/export`, `POST /crm/customers/identify`, `GET /crm/customers/lookup`, `POST /crm/loyalty/redeem-cup`, `POST /vouchers/validate`, `POST /admin/vouchers` | `Public`, `Customer`, `CashierStaff`, `ChainAdmin` |

---

## 7. Đặc Tả 4 SignalR WebSocket Hubs

### 7.1 `OrderHub` (`/hubs/orders`)
- **Server Methods**:
  * `JoinOrderGroup(string orderId)`
  * `LeaveOrderGroup(string orderId)`
- **Client Event Contracts**:
  * `OrderStatusUpdated(OrderStatusUpdatedEvent payload)`
  * `OrderReady(OrderReadyEvent payload)`
  * `EstimatedTimeAdjusted(EstimatedTimeAdjustedEvent payload)`
  * `OrderExpired(OrderExpiredEvent payload)`

### 7.2 `KitchenHub` (`/hubs/kitchen`)
- **Server Methods**:
  * `JoinKitchenGroup(string branchId)` (Yêu cầu Role `BaristaStaff`, `BranchManager`, `ChainAdmin`)
- **Client Event Contracts**:
  * `NewPaidOrder(KdsTicketDto ticket)`
  * `OrderConfirmedCash(KdsTicketDto ticket)`
  * `Item86Toggled(Item86ToggledEvent payload)`
  * `ItemBatchUpdated(ItemBatchUpdatedEvent payload)`

### 7.3 `PaymentHub` (`/hubs/payments`)
- **Server Methods**:
  * `JoinPaymentGroup(string orderId)`
- **Client Event Contracts**:
  * `PaymentSucceeded(PaymentSucceededEvent payload)`
  * `PaymentFailed(PaymentFailedEvent payload)`
  * `PaymentExpired(PaymentExpiredEvent payload)`
  * `PaymentReceived(PaymentReceivedEvent payload)`

### 7.4 `NotificationHub` (`/hubs/notifications`)
- **Server Methods**:
  * `JoinBranchNotifications(string branchId)` (Tự động map group `Branch_{id}_Staff` hoặc `Branch_{id}_Manager` theo Claims)
- **Client Event Contracts**:
  * `ServiceRequested(ServiceRequestedEvent payload)` (Khách bấm chuông tại bàn)
  * `ServiceCallResolved(ServiceCallResolvedEvent payload)`
  * `LowRatingAlert(LowRatingAlertEvent payload)` (Khách đánh giá `<= 2 sao`)
  * `CashVarianceAlert(CashVarianceAlertEvent payload)` (Lệch két `> 50.000 VNĐ`)
  * `InventoryShortageAlert(InventoryShortageAlertEvent payload)` (Tồn kho chạm ngưỡng tối thiểu)
  * `StaffAttendanceLogged(StaffAttendanceEvent payload)`

---

## 8. Core Interfaces & Kế Hoạch Đăng Ký Dependency Injection

### 8.1 Danh Mục Core Interfaces

1. **`IAppDbContext`**:
   - `DbSet<T>` cho toàn bộ 25 Entities.
   - `Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);`
   - `DatabaseFacade Database { get; }`

2. **`IPayOSService`**:
   - `Task<VietQrResult> GeneratePaymentLinkAsync(PaymentLinkRequest request, CancellationToken ct);`
   - `Task<PaymentInfo> GetPaymentLinkInformationAsync(string paymentLinkId, CancellationToken ct);`
   - `bool VerifyWebhookSignature(string rawBody, string signature);`

3. **`ISignalRHubService`**:
   - `Task NotifyOrderStatusChangedAsync(Guid orderId, OrderStatus status, CancellationToken ct);`
   - `Task PushTicketToKitchenAsync(Guid branchId, KdsTicketDto ticket, CancellationToken ct);`
   - `Task NotifyPaymentReceivedAsync(Guid orderId, decimal amount, CancellationToken ct);`
   - `Task BroadcastLowRatingAlertAsync(Guid branchId, LowRatingAlertDto alert, CancellationToken ct);`
   - `Task BroadcastServiceCallAsync(Guid branchId, ServiceCallDto call, CancellationToken ct);`

4. **`ICurrentUserService`**:
   - `Guid? UserId { get; }`
   - `string? Username { get; }`
   - `string? Role { get; }`
   - `Guid? BranchId { get; }`
   - `bool IsAuthenticated { get; }`

5. **`IDateTimeService`**:
   - `DateTime UtcNow { get; }`

6. **`IWifiAttendanceValidator`**:
   - `Task<bool> ValidateBranchWifiAsync(Guid branchId, string clientIp, string clientBssid, CancellationToken ct);`

7. **`IStockDeductionService`**:
   - `Task DeductBomStockForOrderAsync(Guid orderId, CancellationToken ct);`

8. **`IGeminiRAGService`**:
   - `Task<AiRecommendationResultDto> GetRecommendationAsync(Guid branchId, string query, string? customerPhone, CancellationToken ct);`

9. **`IAprioriMiningEngine`**:
   - `Task<List<ComboCandidateDto>> MineCombosAsync(Guid? branchId, double minSupport, double minConfidence, CancellationToken ct);`

### 8.2 Kế Hoạch Cấu Hình DI Trong `Program.cs`
- **Application Services**:
  * `builder.Services.AddMediatR(cfg => cfg.RegisterServicesFromAssembly(typeof(IAppDbContext).Assembly));`
  * `builder.Services.AddValidatorsFromAssembly(typeof(IAppDbContext).Assembly);`
  * `builder.Services.AddTransient(typeof(IPipelineBehavior<,>), typeof(ValidationBehavior<,>));`
- **Infrastructure Services**:
  * `builder.Services.AddDbContext<AppDbContext>(opts => opts.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));`
  * `builder.Services.AddScoped<IAppDbContext>(sp => sp.GetRequiredService<AppDbContext>());`
  * `builder.Services.AddSingleton<IConnectionMultiplexer>(ConnectionMultiplexer.Connect(builder.Configuration.GetConnectionString("Redis")!));`
  * `builder.Services.AddScoped<IPayOSService, PayOSService>();`
  * `builder.Services.AddScoped<ISignalRHubService, SignalRHubService>();`
  * `builder.Services.AddScoped<ICurrentUserService, CurrentUserService>();`
  * `builder.Services.AddSingleton<IDateTimeService, DateTimeService>();`
  * `builder.Services.AddScoped<IWifiAttendanceValidator, WifiAttendanceValidator>();`
  * `builder.Services.AddScoped<IStockDeductionService, StockDeductionService>();`
  * `builder.Services.AddScoped<IGeminiRAGService, GeminiRAGService>();`
  * `builder.Services.AddScoped<IAprioriMiningEngine, AprioriMiningEngine>();`
- **Real-Time SignalR**:
  * `builder.Services.AddSignalR().AddStackExchangeRedis(builder.Configuration.GetConnectionString("Redis")!, opts => opts.Configuration.ChannelPrefix = "SmartFB_SignalR");`

---

## 9. Bảng Quy Tắc Nghiệp Vụ Cốt Lõi (Business Rules Matrix)

| Quy Tắc Nghiệp Vụ | Mô Tả Kỹ Thuật | Điểm Thực Thi Trong Code |
|---|---|---|
| **Dine-In 2 Nhánh** | • Nhánh A (VietQR Trả trước): Đơn khởi tạo `PendingPayment`, TTL 10m. Bếp KDS chỉ nhận đơn khi PayOS Webhook xác nhận `Paid`.<br>• Nhánh B (Tiền mặt Trả sau): Đơn vào bếp ngay (`Confirmed`). Khi Barista bấm Ready, in hóa đơn có VietQR động ra máy in nhiệt; phục vụ mang ra bàn thu tiền mặt hoặc khách quét QR trên bill. | `CreateDineInPrepaidOrderHandler`, `CreateDineInPostpaidOrderHandler`, `PayOSWebhookController`, `KitchenHub` |
| **QR Delivery 20k** | Khách quét QR Delivery riêng, bắt buộc nhập SĐT, Tên, Địa chỉ chi tiết. Tự động cộng cố định **Phí ship 20.000 VNĐ**. **100% VietQR trả trước** (Khóa hoàn toàn COD). | `CreateDeliveryOrderCommandValidator`, `CreateDeliveryOrderHandler` |
| **Takeaway POS & Loyalty 10 Ly** | Thu ngân tạo đơn mang về trên Web POS, tra cứu SĐT CRM. Chương trình tích 10 ly = tặng 1 ly miễn phí **CHỈ ÁP DỤNG DUY NHẤT CHO KÊNH TAKEAWAY**. Khi tích đủ 10 ly, khách được tặng 1 ly miễn phí (giảm 100% giá 1 ly tiêu chuẩn). | `CreateTakeawayOrderHandler`, `RedeemLoyaltyCupHandler`, `LoyaltyCupTransaction` |
| **86-Toggle Khóa Món** | Barista bật/tắt trạng thái hết món ngay trên Web KDS khi cạn nguyên liệu, phát SignalR cập nhật menu tức thời trên PWA và Web POS, chặn tạo đơn mới cho món đó. | `ToggleProductAvailabilityHandler`, `KitchenHub.Item86Toggled` |
| **Chấm Công Khóa WiFi** | Xác thực kép: Thiết bị phải kết nối đúng WiFi chi nhánh (kiểm tra BSSID của Access Point + IP Subnet nội bộ) và nhập đúng Mã nhân viên. Bỏ hoàn toàn GPS và QR 30s. | `WifiAttendanceValidator`, `WifiClockInHandler` |
| **Lệch Két Z-Report > 50k** | Khi kết ca kiểm đếm tiền mặt thực tế, nếu độ lệch `\|varianceAmount\| > 50.000 VNĐ`, bắt buộc người dùng phải điền `varianceNotes` giải trình lý do trước khi chốt biên bản Z-Report. | `CloseCashShiftCommandValidator`, `CloseCashShiftHandler` |
| **Tự Động Báo Động Review <= 2 Sao** | Khi khách đánh giá 1-2 sao, hệ thống tự động bật cờ `is_urgent_alert = true` và phát cảnh báo đỏ qua `NotificationHub` tới Quản lý chi nhánh để xử lý tại bàn trong 3 phút. | `CreateReviewHandler`, `NotificationHub.LowRatingAlert` |
| **Trừ Tồn Kho Theo BOM Khi Ready** | Khi Barista chuyển trạng thái đơn sang `Ready`, hệ thống tự động trừ tồn kho nguyên liệu quầy bar theo công thức định lượng chuẩn (ml, g) của từng món trong đơn. | `UpdateKdsOrderStatusHandler`, `StockDeductionService` |

---
*Tài liệu đặc tả Backend đã được khai phá và hoàn thiện 100% chuẩn mực không giữ chỗ (Zero Placeholders).*
