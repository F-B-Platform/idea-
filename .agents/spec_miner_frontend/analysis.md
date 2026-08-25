# 🎨 BÁO CÁO ĐẶC TẢ CHI TIẾT KIẾN TRÚC FRONTEND (FRONTEND SPECIFICATION REPORT)
## DỰ ÁN: SMART F&B OPERATING SYSTEM (SMART F&B OS) — NEXT.JS 14 MONOREPO
**Mã tài liệu:** `SPEC-MINER-FE-01` | **Phiên bản:** `v2.5.0-Production-Ready`  
**Ngày lập:** 2026-08-25 | **Tác giả:** Frontend Specification Miner Agent  
**Nguồn sự thật đối chiếu (Source of Truth):**
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
- `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md`
- `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`

---

# 📑 MỤC LỤC

1. [Tổng Quan Kiến Trúc Frontend Next.js 14 App Router](#1-tổng-quan-kiến-trúc-frontend-nextjs-14-app-router)
2. [Chi Tiết 5 Route Groups & Sơ Đồ Điều Hướng](#2-chi-tiết-5-route-groups--sơ-đồ-điều-hướng)
   - 2.1 [Route Group 1: `(customer)` — Mobile-First PWA Khách Hàng](#21-route-group-1-customer--mobile-first-pwa-khách-hàng)
   - 2.2 [Route Group 2: `(kds)` — Kitchen Display System TV & Barista](#22-route-group-2-kds--kitchen-display-system-tv--barista)
   - 2.3 [Route Group 3: `(staff)` — Web POS Quầy & Nhân Viên Vận Hành](#23-route-group-3-staff--web-pos-quầy--nhân-viên-vận-hành)
   - 2.4 [Route Group 4: `(manager)` — Cổng Web Quản Lý Chi Nhánh](#24-route-group-4-manager--cổng-web-quản-lý-chi-nhánh)
   - 2.5 [Route Group 5: `(admin)` — Cổng Web Điều Hành Chuỗi Trung Tâm](#25-route-group-5-admin--cổng-web-điều-hành-chuỗi-trung-tâm)
3. [Hệ Thống Thành Phần UI Dùng Chung (Shared UI Components Catalog)](#3-hệ-thống-thành-phần-ui-dùng-chung-shared-ui-components-catalog)
4. [Đặc Tả Quản Lý Trạng Thái Toàn Cục (Zustand Stores Catalog)](#4-đặc-tả-quản-lý-trạng-thái-toàn-cục-zustand-stores-catalog)
5. [Đặc Tả Custom Hooks & Real-time WebSockets (SignalR & Web Audio)](#5-đặc-tả-custom-hooks--real-time-websockets-signalr--web-audio)
6. [Hệ Thống Kiểu Dữ Liệu TypeScript (TypeScript Types & DTOs)](#6-hệ-thống-kiểu-dữ-liệu-typescript-typescript-types--dtos)
7. [Bảng Ma Trận Khám Phá Tính Năng (Features Discovered Table — 62 Features)](#7-bảng-ma-trận-khám-phá-tính-năng-features-discovered-table--62-features)
8. [Ma Trận Kịch Bản Biên & Ngoại Lệ (Edge Cases & Resilience Matrix)](#8-ma-trận-kịch-bản-biên--ngoại-lệ-edge-cases--resilience-matrix)

---

# 1. TỔNG QUAN KIẾN TRÚC FRONTEND NEXT.JS 14 APP ROUTER

Hệ thống Frontend của Smart F&B OS được xây dựng dưới dạng **Next.js 14 App Router Monorepo**, hợp nhất toàn bộ trải nghiệm của 5 nhóm người dùng trên nền tảng Web duy nhất, loại bỏ hoàn toàn chi phí phát triển ứng dụng di động riêng biệt (Native App) hay máy POS phần cứng đắt đỏ.

```
frontend/src/
├── app/
│   ├── (customer)/                      # PWA Khách hàng Mobile-First (Dine-in, Delivery, Tracking, Review)
│   ├── (kds)/                           # Màn hình Bếp / Bar KDS Full-Screen High-Contrast Dark Mode
│   ├── (staff)/                         # Web POS Quầy Takeaway, Sơ đồ bàn, Chuông gọi, Chấm công WiFi
│   ├── (manager)/                       # Portal Quản lý Chi nhánh (Két tiền Z-Report, Kho BOM, Router WiFi)
│   ├── (admin)/                         # Portal Chủ chuỗi (CRUD Menu/BOM, Giá vùng, AI Combo, Báo cáo P&L)
│   ├── layout.tsx                       # Root Layout (Font, Global Providers, Toaster)
│   └── globals.css                      # Tailwind Directives & CSS Custom Properties Design Tokens
├── components/
│   ├── ui/                              # Atomic Shadcn UI Components (Button, Input, Badge, Dialog, Drawer)
│   ├── order/                           # OrderCard, ModifierSelector, CustomizationDrawer, LiveStepper
│   ├── kds/                             # KdsTicketCard, BomRecipeModal, Emergency86Modal, BatchActionModal
│   ├── pos/                             # CrmLookupBar, LoyaltyProgress, CashTenderCalculator, ReceiptPrint
│   ├── manager/                         # DenominationCounter, ZReportPrint, StockAuditTable, WifiConfigModal
│   ├── admin/                           # ComboApprovalCard, SeasonalScheduler, PricingMatrixTable, PlChart
│   └── layout/                          # CustomerNavbar, StaffSidebar, ManagerSidebar, AdminSidebar, Header
├── stores/                              # Zustand Global Stores (Auth, Cart, POS, Shift, KDS, Tables)
├── hooks/                               # Custom Hooks (useSignalR, useAttendanceWifi, useApiQuery, useWebAudio)
├── types/                               # TypeScript Domain Interfaces, DTOs & SignalR Event Contracts
└── lib/                                 # Axios Client, Utils (cn, currency, datetime, escpos)
```

### Tiêu chuẩn Design Tokens Bất Biến
- **Màu sắc Thương hiệu (Customer & POS):** Primary Warm Amber (`#8B4513`), Secondary Gold (`#D97706`), Neutral Cream (`#FAF8F5`), Text Main (`#1A1A1A`).
- **Màu sắc Chuyên dụng Bếp KDS:** Slate Dark Background (`#0F172A`), Surface Card (`#1E293B`), Text White High-Contrast (`#F8FAFC`).
- **Màu sắc Trạng thái (SLA / Alerts):** Success Green (`#10B981` - KDS < 3m, Paid, WiFi Valid), Warning Amber (`#F59E0B` - KDS 3-5m, Cash Variance), Danger Red (`#EF4444` - KDS > 5m Flashing, <= 2 Star Alert, WiFi Forbidden).
- **Quy chuẩn WCAG 2.1 AA:** Vùng cảm ứng Touch Target `>= 44 x 44px` trên toàn bộ thiết bị di động và tablet quầy bar.

---

# 2. CHI TIẾT 5 ROUTE GROUPS & SƠ ĐỒ ĐIỀU HƯỚNG

---

## 2.1 Route Group 1: `(customer)` — Mobile-First PWA Khách Hàng

Giao diện PWA siêu nhẹ tải dưới 1.5s, không cần cài đặt App từ App Store, hỗ trợ đầy đủ tiếng Việt có dấu (`Be Vietnam Pro` font).

### 1. `app/(customer)/table/[tableId]/page.tsx` — Menu Gọi Món Tại Bàn
- **Mục đích:** Khách quét mã `Table QR` gắn trên bàn, tự động nhận diện `tableId`, `branchId` và xác thực chữ ký HMAC bảo mật.
- **Thành phần chức năng:**
  * Header cố định: Tên Quán, Chi nhánh, Tên Bàn (ví dụ: `Bàn 05 - Tầng 1`), Mã định danh khách hàng & thanh tiến trình tích lũy ly (nếu đã lưu SĐT).
  * Thanh tìm kiếm đồ uống kèm bộ lọc danh mục dạng thanh trượt ngang (Tất cả, Cà phê, Trà trái cây, Đá xay, Bánh ngọt).
  * Banner Gợi ý Món AI-1 (Google Gemini 1.5 Flash RAG) đề xuất món phù hợp với thời tiết/nhiệt độ hiện tại.
  * Danh sách thẻ món ăn (Product Card) hiển thị: Ảnh WebP nén tối ưu, Tên món, Giá cơ bản, Nhãn Best-seller, Nút `[+ THÊM]`.
  * Drawer tùy biến định lượng món (Customization Drawer): Chọn Size (S/M/L), Mức đường (0%, 30%, 50%, 100%), Mức đá (Không đá, 50%, 100%), Topping thêm (Trân châu, Kem Cheese), Ghi chú đặc biệt.
  * Bottom Floating Bar: Hiển thị tổng số món trong giỏ và tổng tiền tạm tính, nút chuyển tới trang Giỏ hàng `/cart`.

### 2. `app/(customer)/cart/page.tsx` — Giỏ Hàng & Lựa Chọn 2 Nhánh Dine-In
- **Mục đích:** Kiểm tra lại danh sách món đã chọn, áp dụng mã khuyến mãi và lựa chọn 1 trong 2 nhánh thanh toán.
- **Thành phần chức năng:**
  * Danh sách món ăn chi tiết kèm danh sách modifier đã chọn, nút tăng/giảm số lượng `[ - ] [ 1 ] [ + ]` và nút xóa món.
  * Form nhập mã giảm giá Voucher (`/api/v1/vouchers/apply`), hiển thị số tiền chiết khấu tức thì.
  * Bảng tổng hợp chi phí: Tạm tính, Giảm giá voucher, Tổng thanh toán cuối cùng.
  * **Bộ chọn 2 Nhánh Thanh Toán Dine-In:**
    1. **(•) Nhánh A: VIETQR TRẢ TRƯỚC (Prepaid):** Sinh mã VietQR động, thanh toán xong Bếp KDS mới nhận đơn.
    2. **( ) Nhánh B: TIỀN MẶT TRẢ SAU (Postpaid):** Đơn gửi thẳng xuống KDS Bếp ngay lập tức, nhân viên mang đồ uống ra bàn kèm hóa đơn có mã VietQR để thanh toán sau.
  * Nút CTA `[ XÁC NHẬN ĐẶT ĐƠN ]`.

### 3. `app/(customer)/checkout/vietqr/page.tsx` — Màn Hình Thanh Toán VietQR Động
- **Mục đích:** Cung cấp mã VietQR động đếm ngược 10 phút để khách quét chuyển khoản.
- **Thành phần chức năng:**
  * Bộ đếm ngược thời gian thực `[ 09:59 ]` (Tự động hủy đơn và hoàn kho tạm giữ sau 10 phút nếu không nhận được tiền).
  * Ảnh mã VietQR động sinh từ PayOS (`qrCodeDataUrl`) kèm nút `[ TẢI MÃ QR ]` và deeplink mở thẳng ứng dụng ngân hàng.
  * Khối thông tin chuyển khoản: Tên ngân hàng, Số tài khoản, Tên chủ tài khoản, Số tiền, Nội dung chuyển khoản chuẩn hóa (`ORD_XXXX`), kèm nút Copy 1-chạm.
  * Animation vòng xoay chờ tín hiệu SignalR `PaymentSucceeded`. Ngay khi Webhook PayOS khớp lệnh, màn hình tự động chuyển hướng sang `/tracking/[orderId]`.
  * Nút `[ HỦY ĐƠN HÀNG ]` và `[ KIỂM TRA LẠI TRẠNG THÁI ]`.

### 4. `app/(customer)/delivery/page.tsx` — Đặt Giao Hàng QR Delivery
- **Mục đích:** Phục vụ khách hàng quét mã `Delivery QR` trên poster, banner hoặc website từ xa.
- **Thành phần chức năng:**
  * Form thông tin người nhận (Bắt buộc): Họ và tên, Số điện thoại (Regex 10 số VN), Địa chỉ giao hàng chi tiết, Ghi chú shipper.
  * Giỏ hàng đồ uống giao tận nơi.
  * **Tự động áp dụng Phí giao hàng cố định 20.000 VNĐ** (`delivery_fee = 20000`).
  * **Khóa cứng 100% hình thức Thanh toán VietQR Trả Trước** (Ẩn hoàn toàn tùy chọn COD để chống bùng đơn).
  * Nút chuyển tiếp tới thanh toán VietQR PayOS.

### 5. `app/(customer)/tracking/[orderId]/page.tsx` — Theo Dõi Tiến Độ Đơn Hàng Live
- **Mục đích:** Theo dõi trạng thái đơn hàng thời gian thực qua kết nối SignalR `OrderHub`.
- **Thành phần chức năng:**
  * Header: Mã đơn hàng, Số bàn / Địa chỉ giao hàng, Thời gian dự kiến hoàn thành.
  * **Live Stepper Trực quan:**
    - Đơn Dine-In: `(✓) Đã Tiếp Nhận` ➔ `(●) Đang Pha Chế` ➔ `( ) Hoàn Tất / Sẵn Sàng` ➔ `( ) Đã Phục Vụ`.
    - Đơn Delivery: `(✓) Đã Tiếp Nhận` ➔ `(●) Đang Pha Chế` ➔ `( ) Đang Giao Hàng` ➔ `( ) Giao Thành Công`.
  * Thẻ thông tin hàng đợi: Hiển thị vị trí đơn hàng trong hàng đợi pha chế của quán (ví dụ: `#2 trong hàng đợi`).
  * Danh sách chi tiết các món trong đơn hàng.
  * **Nút Chuông Gọi Phục Vụ Bàn `[ 🔔 BẤM CHUÔNG GỌI PHỤC VỤ ]`:** Gửi sự kiện SignalR tới nhân viên quầy, có cơ chế debounce chống spam (chỉ được bấm 1 lần mỗi 60 giây).
  * Nút `[ 📜 XEM HÓA ĐƠN ĐIỆN TỬ ]`.

### 6. `app/(customer)/review/[orderId]/page.tsx` — Đánh Giá 1-5 Sao & Tải Ảnh Thực Tế
- **Mục đích:** Thu thập phản hồi khách hàng ngay sau khi hoàn thành đơn.
- **Thành phần chức năng:**
  * Bộ chọn sao 1-5 Sao với mô tả cảm xúc tương ứng.
  * Nhãn cảm nhận nhanh: `[ Pha chế nhanh ]`, `[ Đồ uống ngon ]`, `[ Nhân viên nhiệt tình ]`, `[ Không gian sạch sẽ ]`.
  * Ô nhập đánh giá chi tiết (Textarea).
  * Component tải 1 - 3 ảnh thực tế (Drag & Drop / Camera capture, tự động chuyển đổi sang WebP).
  * Tùy chọn `[x] Đánh giá ẩn danh`.
  * **Cơ chế Red Alert:** Nếu khách chấm `<= 2 sao`, hệ thống gửi dữ liệu kèm cờ kích hoạt Red Alert qua SignalR `NotificationHub` tới Quản lý chi nhánh ngay tức khắc.

### 7. `app/(customer)/history/page.tsx` — Lịch Sử Đơn Hàng & Reorder 1-Chạm
- **Mục đích:** Xem lại các đơn hàng đã đặt theo SĐT khách hàng, nút `[ ĐẶT LẠI ]` nạp toàn bộ món và modifier vào giỏ hàng chỉ bằng 1 thao tác chạm.

### 8. `app/(customer)/ai-chat/page.tsx` — Chatbot AI-1 Gemini RAG Tư Vấn Khẩu Vị
- **Mục đích:** Trợ lý ảo AI tư vấn đồ uống theo ngữ cảnh, nhiệt độ thời tiết, sở thích calo hoặc tâm trạng.
- **Thành phần chức năng:** Cửa sổ chat hội thoại 2 chiều, phản hồi văn bản tự nhiên kèm theo thẻ đề xuất món (Product Card) có nút `[ + THÊM VÀO GIỎ ]` gắn trực tiếp vào giỏ hàng khách.

---

## 2.2 Route Group 2: `(kds)` — Kitchen Display System TV & Barista

Màn hình KDS tối ưu cho Barista/Bếp thao tác cảm ứng nhanh hoặc hiển thị trên Smart TV quầy pha chế, giao diện Nền Tối Chống Lóa (`#0F172A`).

### 1. `app/(kds)/page.tsx` — Ticket Board Pha Chế Real-Time
- **Mục đích:** Tiếp nhận và quản lý toàn bộ vé đơn hàng chế biến tại quầy Bar/Bếp.
- **Thành phần chức năng:**
  * Header: Đồng hồ thời gian thực, Bộ lọc trạm (Tất cả, Quầy Bar, Bếp Nấu), Tổng số đơn đang chờ, Nút bật/tắt chuông báo Web Audio, Nút mở Modal 86-Toggle.
  * **Kanban / Grid Thẻ Đơn Hàng (Order Tickets):**
    - Thông tin vé: Mã đơn (`#ORD-0042`, `#TK-0089`, `#DEL-0015`), Loại đơn (`[BÀN 05]`, `[MANG VỀ]`, `[GIAO HÀNG]`), Trạng thái thanh toán (Đã thanh toán VietQR / Tiền mặt trả sau).
    - **Bộ đếm thời gian SLA & Đổi màu thông minh:**
      * Xanh lá (`state-success`): Thời gian chờ `< 3 phút` (Kịp tiến độ).
      * Vàng cam (`state-warning`): Thời gian chờ `3 - 5 phút` (Cảnh báo chuẩn bị trễ).
      * Đỏ nhấp nháy (`state-danger`): Thời gian chờ `> 5 phút` (Quá hạn SLA — Kích hoạt âm thanh cảnh báo xung 440Hz).
    - Chi tiết món: Tên món, Size, Chi tiết modifier (50% đường, 70% đá, topping), Ghi chú đặc biệt.
    - Nút tra cứu nhanh công thức BOM của từng món `[ 🧪 XEM BOM ]`.
    - Nút chuyển trạng thái thao tác lớn (>= 48px): `[ BẮT ĐẦU ]` (`Preparing`) và `[ HOÀN TẤT ]` (`Ready`).
    - Khi bấm `[ HOÀN TẤT ]`: Hệ thống tự động kích hoạt trừ tồn kho Bar theo định mức BOM trong Database và phát lệnh in Bill cho đơn tiền mặt.

### 2. `app/(kds)/86-toggle/page.tsx` — Modal Khóa Món Khẩn Cấp (86-Toggle)
- **Mục đích:** Barista khóa nhanh món khi quầy bar đột ngột hết nguyên liệu.
- **Thành phần chức năng:**
  * Thanh tìm kiếm nhanh món ăn/đồ uống.
  * Danh sách công tắc Toggle Switch (Xanh: Đang bán, Đỏ: Khóa món).
  * Khi gạt tắt: Gửi request `PATCH /api/v1/kds/products/{id}/86-toggle` và phát sự kiện SignalR `Item86Toggled` khóa món tức thì trên toàn bộ PWA khách và POS thu ngân.

### 3. `app/(kds)/batch/page.tsx` — Chế Độ Gom Món Pha Chế Đồng Loạt (KDS Batching)
- **Mục đích:** Gom các món giống nhau từ nhiều đơn hàng khác nhau để pha chế một lần trong giờ cao điểm (ví dụ: gom 6 ly Cà Phê Muối từ 3 đơn `#ORD-0042`, `#TK-0089`, `#ORD-0045`).
- **Thành phần chức năng:** Hiển thị tổng định lượng nguyên liệu cần rót một mẻ (ml cốt cà phê, ml kem muối) và nút `[ HOÀN TẤT TẤT CẢ TRONG MẺ ]` tự động cập nhật `Ready` cho toàn bộ các đơn liên quan.

---

## 2.3 Route Group 3: `(staff)` — Web POS Quầy & Nhân Viên Vận Hành

Giao diện Web POS quầy thu ngân và hỗ trợ nhân viên phục vụ bàn chạy mượt mà trên Tablet iPad/Android hoặc Laptop cảm ứng.

### 1. `app/(staff)/pos/page.tsx` — Web POS Quầy Takeaway & Tra Cứu CRM 10 Ly
- **Mục đích:** Thu ngân bán mang về tại quầy, tra cứu khách hàng hội viên, áp dụng chính sách 10 ly tặng 1 và thu tiền.
- **Thành phần chức năng:**
  * **Cột trái (Tra cứu CRM & Thực đơn):**
    - Ô tra cứu Số điện thoại khách hàng: Tự động tải hồ sơ Tên khách, Lịch sử mua hàng, và Quỹ ly tích lũy (`CupBalance`).
    - Thanh tiến trình tích lũy ly: `[██████████] 10/10 Ly`.
    - **Nút Đổi Ly Miễn Phí `[ 🎁 BẤM ĐỔI 1 LY MIỄN PHÍ (-35.000đ) ]`:** Chỉ hiển thị khi `CupBalance >= 10` và là đơn Takeaway. Tự động giảm trừ 100% giá trị 1 ly trong đơn.
    - Lưới chọn món (Product Grid) phân theo danh mục, hỗ trợ chạm nhanh thêm vào giỏ.
  * **Cột phải (Giỏ hàng & Thu tiền):**
    - Chi tiết danh sách món mang về, tổng tiền món, ưu đãi giảm trừ ly free.
    - Bộ chọn phương thức thanh toán: `[ (•) TIỀN MẶT ]` hoặc `[ ( ) VIETQR ]`.
    - Bộ tính tiền thừa thông minh (Cash Calculator): Nhập số tiền khách đưa (hoặc các nút chọn nhanh 50k, 100k, 200k, 500k) ➔ Tự động tính tiền thối lại cho khách.
    - Nút `[ IN BILL & GỬI BẾP ]`: Kích hoạt máy in nhiệt in hóa đơn ESC/POS và gửi vé đơn hàng xuống KDS Bếp qua SignalR.

### 2. `app/(staff)/tables/page.tsx` — Sơ Đồ Bàn Mặt Bằng & Tiếp Nhận Chuông Báo
- **Mục đích:** Nhân viên phục vụ giám sát trạng thái từng bàn và tiếp nhận yêu cầu gọi phục vụ.
- **Thành phần chức năng:**
  * Sơ đồ lưới bố cục bàn phân theo tầng/khu vực (Tầng 1, Tầng 2, Ngoài trời).
  * **Mã màu trạng thái bàn thời gian thực:**
    - 🟢 Xanh lá (`Available`): Bàn trống, sẵn sàng đón khách.
    - 🔵 Xanh dương (`Occupied_Paid`): Bàn đang có khách đã thanh toán VietQR trả trước.
    - 🟡 Vàng cam (`Occupied_PendingPayment`): Bàn đang có khách chọn tiền mặt trả sau / Chờ in bill.
    - 🔴 Đỏ nhấp nháy (`ServiceRequested`): **Khách tại bàn vừa bấm chuông gọi phục vụ**. Phát chuông âm thanh `SoundServiceCall` (587Hz).
  * Thao tác trên bàn: Chạm vào bàn để xem chi tiết đơn hàng hiện tại, mở bàn mới, hoặc bấm `[ TIẾP NHẬN ]` để tắt chuông gọi bàn.

### 3. `app/(staff)/attendance/page.tsx` — Chấm Công Khóa Mạng WiFi
- **Mục đích:** Nhân viên chấm công vào/ra ca thông qua kết nối WiFi nội bộ của quán.
- **Thành phần chức năng:**
  * Thẻ hiển thị trạng thái mạng WiFi: SSID, BSSID (MAC router) và IP thiết bị.
  * Cảnh báo trực quan: Màu xanh (Đúng WiFi quán) hoặc Màu đỏ (Sai WiFi / 4G - Từ chối chấm công).
  * Ô nhập Mã số nhân viên (`EmployeeCode`) và chọn Ca làm việc.
  * Hai nút thao tác lớn: `[ 🟢 CHẤM CÔNG VÀO CA (CLOCK-IN) ]` và `[ 🔴 CHẤM CÔNG RA CA (CLOCK-OUT) ]`.
  * Lịch sử các lần chấm công gần nhất trong tuần.

### 4. `app/(staff)/shift-report/page.tsx` — Báo Cáo Tổng Kết Ca Nhân Viên
- **Mục đích:** Xem lại tổng số đơn hàng đã phục vụ trong ca, tổng doanh số bán và thực hiện bàn giao ca.

---

## 2.4 Route Group 4: `(manager)` — Cổng Web Quản Lý Chi Nhánh

Cổng thông tin dành cho Quản lý chi nhánh theo dõi doanh thu thời gian thực, quản lý kho định mức BOM, mở/kết ca két tiền và xử lý khiếu nại đánh giá khách hàng.

### 1. `app/(manager)/dashboard/page.tsx` — Dashboard Vận Hành Chi Nhánh
- **Mục đích:** Theo dõi các chỉ số KPI vận hành trong ngày: Doanh thu theo giờ, Tỷ lệ thanh toán VietQR vs Tiền mặt, Tuân thủ SLA KDS, Cảnh báo nguyên liệu sắp hết.

### 2. `app/(manager)/shifts/page.tsx` — Mở/Kết Ca Két Tiền & Đối Soát Z-Report
- **Mục đích:** Quản lý tiền mặt đầu ca và đối soát kết ca cuối ngày chặt chẽ.
- **Thành phần chức năng:**
  * Mở ca: Khai báo số tiền mặt đầu ca (Opening Cash, ví dụ: 1.000.000đ).
  * **Kết ca & Đối soát Z-Report:**
    - Hiển thị tiền mặt lý thuyết: `Tiền đầu ca` + `Doanh thu tiền mặt trong ca` = `Tổng lý thuyết hệ thống`.
    - **Bảng đếm tiền thực tế theo 6 mệnh giá:** Ô nhập số lượng từng tờ tiền cho các mệnh giá `500.000đ`, `200.000đ`, `100.000đ`, `50.000đ`, `20.000đ`, `10.000đ`.
    - Tự động tính tổng tiền thực đếm và tính chênh lệch (`Variance = PhysicalTotal - SystemExpected`).
    - **Ô nhập lý do giải trình bắt buộc:** Bắt buộc nhập khi chênh lệch khác 0 (Nếu lệch `> 50.000đ`, hệ thống tự động gửi cảnh báo khẩn cấp tới Chủ chuỗi).
    - Nút `[ XÁC NHẬN ĐÓNG CA KÉT & IN Z-REPORT ]`.

### 3. `app/(manager)/inventory/page.tsx` — Quản Lý Kho BOM & Kiểm Kê Hao Hụt
- **Mục đích:** Quản lý xuất nhập tồn kho nguyên vật liệu theo định mức BOM.
- **Thành phần chức năng:**
  * Tạo phiếu nhập kho từ Nhà cung cấp kèm tải ảnh hóa đơn chứng từ.
  * Tạo phiếu xuất kho nội bộ từ Kho tổng ra Quầy Bar.
  * **Bảng kiểm kê định kỳ đối soát Hao hụt:** Đối chiếu Tồn kho lý thuyết (sau khi trừ tự động qua BOM của các đơn đã pha chế) với Số lượng thực đếm ➔ Tính số lượng chênh lệch và tỷ lệ % hao hụt (Cảnh báo vàng/đỏ khi hao hụt vượt định mức 3%).

### 4. `app/(manager)/wifi-configs/page.tsx` — Cấu Hình Router BSSID & IP Subnet
- **Mục đích:** Quản lý khai báo danh sách BSSID (địa chỉ MAC) của các cục phát WiFi quán và dải IP Subnet hợp lệ để phục vụ tính năng Chấm công khóa mạng.

### 5. `app/(manager)/reviews/page.tsx` — Cảnh Báo Khẩn Đánh Giá <= 2 Sao & Kiểm Duyệt Ảnh
- **Mục đích:** Tiếp nhận các phản hồi tiêu cực của khách hàng tại bàn trong vòng 3 phút để xin lỗi/đổi món kịp thời, đồng thời kiểm duyệt các hình ảnh do khách hàng tải lên trước khi cho phép hiển thị công khai trên menu.

---

## 2.5 Route Group 5: `(admin)` — Cổng Web Điều Hành Chuỗi Trung Tâm

Cổng điều hành trung tâm dành cho Chủ chuỗi (Chain Owner) quản lý danh mục toàn chuỗi, bảng giá vùng, cấu hình AI Combo và báo cáo tài chính P&L hợp nhất.

### 1. `app/(admin)/dashboard/page.tsx` — Dashboard P&L Hợp Nhất Toàn Chuỗi
- **Mục đích:** Báo cáo tài chính hợp nhất đa chi nhánh: Doanh thu thuần, Giá vốn nguyên vật liệu COGS (tính chính xác theo công thức BOM), Lãi gộp toàn chuỗi, Ma trận phân loại món ăn BCG (Star, Cash Cow, Dog, Question Mark).
- **Thành phần chức năng:** Bộ lọc chi nhánh và khoảng thời gian, Biểu đồ doanh thu/lợi nhuận Recharts, Nút xuất báo cáo Excel/CSV.

### 2. `app/(admin)/menu/products/page.tsx` — Full CRUD Món Ăn & Định Nghĩa BOM
- **Mục đích:** Quản trị danh mục món ăn, hình ảnh, các kích cỡ (Size S/M/L) và công thức BOM định lượng chi tiết (ml cốt trà, gam bột sữa, gam cà phê) cho từng kích cỡ. Hỗ trợ tính năng Thay thế món ăn (Replace Product).

### 3. `app/(admin)/menu/categories/page.tsx` — Sắp Xếp Thứ Tự Danh Mục Kéo Thả
- **Mục đích:** Kéo thả (Drag & Drop) để sắp xếp thứ tự hiển thị danh mục món trên ứng dụng PWA của khách hàng.

### 4. `app/(admin)/menu/seasonal/page.tsx` — Lên Lịch Thực Đơn Mùa Vụ (Seasonal Menu)
- **Mục đích:** Thiết lập thời gian tự động mở bán hoặc đóng bán các món theo mùa (ví dụ: Thực đơn Trà Trái Cây Mùa Hè từ 01/06 đến 31/08).

### 5. `app/(admin)/pricing/page.tsx` — Quản Lý Bảng Giá Vùng Chi Nhánh
- **Mục đích:** Ma trận định giá linh hoạt theo vùng chi nhánh (ví dụ: Chi nhánh Quận 1 áp dụng bảng giá Vùng Trung Tâm +15% so với Chi nhánh Vùng Ngoại Thành).

### 6. `app/(admin)/ai/combos/page.tsx` — AI-2 Khai Phá & Phê Duyệt Combo Apriori
- **Mục đích:** Module AI-2 phân tích ma trận giỏ hàng lịch sử, tìm ra các cặp món mua kèm tiềm năng (Support, Confidence, Lift > 1.2).
- **Thành phần chức năng:**
  * Thanh trượt tham số Min Support và Min Confidence, nút `[ CHẠY KHAI PHÁ GIỎ HÀNG ]`.
  * Danh sách thẻ Combo đề xuất: Tên cặp món, Giá gốc, Giá vốn BOM, Biên lợi nhuận.
  * **Thanh trượt điều chỉnh mức chiết khấu (% Discount Slider):** Kéo từ 5% - 30% để xem biến động giá bán mới và lợi nhuận gộp tương ứng.
  * Cơ chế phê duyệt Human-in-the-loop: Nút `[ TỪ CHỐI ]` hoặc `[ PHÊ DUYỆT & PHÁT HÀNH LÊN MENU PWA ]`.

### 7. `app/(admin)/crm/page.tsx` — Quản Trị Danh Bạ Hội Viên & Phân Khúc RFM
- **Mục đích:** Quản lý toàn bộ tệp khách hàng theo số điện thoại, phân loại nhóm khách VIP, Khách trung thành, Khách có nguy cơ rời bỏ (Churn risk).

### 8. `app/(admin)/audit-logs/page.tsx` — Nhật Ký Kiểm Toán Bất Biến
- **Mục đích:** Truy vết toàn bộ thao tác nhạy cảm (Sửa giá, Xóa món, Đóng két tiền, Đăng nhập) kèm địa chỉ IP, User ID và dấu thời gian UTC.

---

# 3. HỆ THỐNG THÀNH PHẦN UI DÙNG CHUNG (SHARED UI COMPONENTS CATALOG)

Hệ thống thành phần dùng chung được xây dựng trên thư viện **Shadcn/UI** và **Tailwind CSS**, bảo đảm tính tái sử dụng cao và chuẩn mực tương tác WCAG 2.1 AA.

```
frontend/src/components/
├── ui/
│   ├── Button.tsx               # Nút bấm đa biến thể (Primary, Secondary, Destructive, Outline, Ghost, Link)
│   ├── Input.tsx                # Input text/number chuẩn với nhãn lỗi validation
│   ├── SearchInput.tsx          # Ô tìm kiếm có icon kính lúp và nút xóa nhanh 1-chạm
│   ├── Textarea.tsx             # Ô nhập văn bản nhiều dòng cho ghi chú/đánh giá
│   ├── Switch.tsx               # Công tắc Toggle cho trạng thái bật/tắt (86-toggle, Active)
│   ├── Slider.tsx               # Thanh trượt cho chiết khấu AI Combo và lọc giá
│   ├── Badge.tsx                # Nhãn hiển thị trạng thái và danh mục
│   ├── Dialog.tsx               # Modal popup tương tác
│   ├── Drawer.tsx               # Bottom sheet trượt lên từ đáy màn hình cho PWA Mobile
│   ├── Table.tsx                # Bảng dữ liệu chuẩn cho Admin/Manager portal
│   └── Toast.tsx                # Thông báo nổi góc màn hình
├── order/
│   ├── OrderCard.tsx            # Thẻ tóm tắt đơn hàng dùng cho Khách hàng & Staff
│   ├── ModifierSelector.tsx     # Bộ chọn Đường (0-100%), Đá (0-100%), Size (S/M/L)
│   ├── CustomizationDrawer.tsx  # Drawer tùy biến toàn diện món ăn trước khi thêm giỏ
│   └── LiveStepper.tsx          # Thanh tiến trình trạng thái đơn hàng thời gian thực
├── kds/
│   ├── KdsTicketCard.tsx        # Thẻ vé đơn hàng KDS nền tối, đổi màu theo SLA
│   ├── BomRecipeModal.tsx       # Popup xem nhanh công thức định lượng nguyên liệu
│   ├── Emergency86Modal.tsx     # Cửa sổ khóa hết món nhanh cho Barista
│   └── BatchActionModal.tsx     # Cửa sổ gom món pha chế đồng loạt
├── pos/
│   ├── CrmLookupBar.tsx         # Thanh tra cứu SĐT khách hàng kèm hiển thị tên/quỹ ly
│   ├── LoyaltyProgress.tsx      # Thanh tiến trình 10 ly đồ uống kèm nút đổi ly free
│   ├── CashTenderCalculator.tsx # Bàn phím số tính tiền khách đưa & tiền thối lại
│   └── ReceiptPrint.tsx         # Mẫu in hóa đơn nhiệt ESC/POS tích hợp mã VietQR động
├── manager/
│   ├── DenominationCounter.tsx  # Bảng nhập 6 mệnh giá tiền mặt đối soát Z-Report
│   ├── ZReportPrint.tsx         # Mẫu in biên bản chốt ca Z-Report cuối ngày
│   └── StockAuditTable.tsx      # Bảng kiểm kê hao hụt nguyên liệu kho BOM
├── admin/
│   ├── ComboApprovalCard.tsx    # Thẻ đề xuất Combo AI-2 kèm slider chiết khấu
│   ├── SeasonalScheduler.tsx    # Bộ chọn lịch thời gian mở/đóng thực đơn mùa
│   └── PricingMatrixTable.tsx   # Bảng ma trận giá theo vùng chi nhánh
└── layout/
    ├── CustomerNavbar.tsx       # Thanh tiêu đề PWA (Bàn, Chi nhánh, Giỏ hàng)
    ├── StaffSidebar.tsx         # Sidebar điều hướng Web POS & Sơ đồ bàn
    ├── ManagerSidebar.tsx       # Sidebar điều hướng Cổng Quản lý Chi nhánh
    └── AdminSidebar.tsx         # Sidebar điều hướng Cổng Chủ chuỗi
```

---

# 4. ĐẶC TẢ QUẢN LÝ TRẠNG THÁI TOÀN CỤC (ZUSTAND STORES CATALOG)

Hệ thống sử dụng **Zustand** để quản lý trạng thái Client UI nhẹ và đồng bộ tức thời:

### 1. `useAuthStore` — Quản Lý Phiên Đăng Nhập & Phân Quyền
```typescript
interface UserProfile {
  id: string;
  employeeCode: string;
  fullName: string;
  role: 'CashierStaff' | 'BaristaStaff' | 'BranchManager' | 'ChainAdmin';
  branchId?: string;
  branchName?: string;
}

interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
  user: UserProfile | null;
  isAuthenticated: boolean;
  login: (tokens: { accessToken: string; refreshToken: string }, user: UserProfile) => void;
  logout: () => void;
  updateUser: (user: Partial<UserProfile>) => void;
}
```

### 2. `useCartStore` — Quản Lý Giỏ Hàng PWA Khách Hàng
```typescript
export interface CartItemModifier {
  modifierId: string;
  name: string;
  price: number;
}

export interface CartItem {
  cartItemId: string;
  productId: string;
  productName: string;
  sizeId: string;
  sizeName: string;
  unitPrice: number;
  quantity: number;
  sugarLevel: '0%' | '30%' | '50%' | '100%';
  iceLevel: '0%' | '50%' | '100%';
  toppings: CartItemModifier[];
  notes?: string;
  totalItemPrice: number;
}

interface CartState {
  tableId: string | null;
  branchId: string | null;
  orderType: 'DineIn' | 'Delivery';
  items: CartItem[];
  voucherCode: string | null;
  discountAmount: number;
  deliveryFee: number;
  paymentMethod: 'VIETQR' | 'CASH';
  recipientName?: string;
  recipientPhone?: string;
  deliveryAddress?: string;
  shipperNotes?: string;
  
  // Actions
  setTableAndBranch: (tableId: string | null, branchId: string) => void;
  setOrderType: (type: 'DineIn' | 'Delivery') => void;
  addItem: (item: Omit<CartItem, 'cartItemId' | 'totalItemPrice'>) => void;
  updateItemQuantity: (cartItemId: string, delta: number) => void;
  removeItem: (cartItemId: string) => void;
  applyVoucher: (code: string, discount: number) => void;
  removeVoucher: () => void;
  setPaymentMethod: (method: 'VIETQR' | 'CASH') => void;
  setDeliveryInfo: (info: { recipientName: string; recipientPhone: string; deliveryAddress: string; shipperNotes?: string }) => void;
  clearCart: () => void;
  
  // Selectors
  getSubtotal: () => number;
  getTotalAmount: () => number;
  getTotalItemsCount: () => number;
}
```

### 3. `usePosStore` — Quản Lý Trạng Thái Quầy Thu Ngân Takeaway
```typescript
interface PosCustomer {
  customerId: string;
  phone: string;
  fullName: string;
  cupBalance: number;
  eligibleForFreeCup: boolean;
}

interface PosState {
  currentCustomer: PosCustomer | null;
  cartItems: CartItem[];
  freeCupRedeemed: boolean;
  tenderAmount: number;
  paymentMethod: 'CASH' | 'VIETQR';
  
  // Actions
  setCustomer: (customer: PosCustomer | null) => void;
  addItem: (item: CartItem) => void;
  updateQuantity: (cartItemId: string, qty: number) => void;
  removeItem: (cartItemId: string) => void;
  redeemFreeCup: () => void;
  cancelFreeCup: () => void;
  setTenderAmount: (amount: number) => void;
  setPaymentMethod: (method: 'CASH' | 'VIETQR') => void;
  resetPos: () => void;
  
  // Selectors
  getGrossTotal: () => number;
  getDiscountTotal: () => number;
  getNetTotal: () => number;
  getChangeAmount: () => number;
}
```

### 4. `useShiftStore` — Quản Lý Ca Két Tiền & Đối Soát Z-Report
```typescript
export interface DenominationEntry {
  denomination: 500000 | 200000 | 100000 | 50000 | 20000 | 10000;
  count: number;
}

interface ShiftState {
  currentShiftId: string | null;
  openingCash: number;
  theoreticalCash: number;
  denominations: Record<number, number>;
  physicalCashTotal: number;
  variance: number;
  justificationReason: string;
  isClosed: boolean;
  
  openShift: (shiftId: string, openingCash: number) => void;
  setTheoreticalCash: (amount: number) => void;
  setDenominationCount: (denomination: number, count: number) => void;
  setJustificationReason: (reason: string) => void;
  calculateVariance: () => void;
  closeShift: () => void;
  resetShift: () => void;
}
```

### 5. `useKdsStore` — Quản Lý Trạng Thái Vé Bếp & Barista
```typescript
export interface KdsTicket {
  orderId: string;
  orderNumber: string;
  orderType: 'DINE_IN' | 'TAKEAWAY' | 'DELIVERY';
  tableNumber?: string;
  createdAtUtc: string;
  elapsedSeconds: number;
  status: 'Pending' | 'Preparing' | 'Ready';
  items: {
    orderItemId: string;
    productName: string;
    sizeName: string;
    quantity: number;
    sugarLevel: string;
    iceLevel: string;
    toppings: string[];
    notes?: string;
  }[];
}

interface KdsState {
  tickets: KdsTicket[];
  stationFilter: 'ALL' | 'BAR' | 'KITCHEN';
  batchMode: boolean;
  soundEnabled: boolean;
  
  setTickets: (tickets: KdsTicket[]) => void;
  addTicket: (ticket: KdsTicket) => void;
  updateTicketStatus: (orderId: string, status: 'Preparing' | 'Ready') => void;
  removeTicket: (orderId: string) => void;
  setStationFilter: (filter: 'ALL' | 'BAR' | 'KITCHEN') => void;
  toggleBatchMode: () => void;
  toggleSound: () => void;
}
```

### 6. `useTableStore` — Quản Lý Sơ Đồ Bàn & Chuông Gọi Phục Vụ Live
```typescript
export interface TableItem {
  id: string;
  tableNumber: string;
  capacity: number;
  floor: number;
  status: 'Available' | 'Occupied_Paid' | 'Occupied_PendingPayment' | 'ServiceRequested';
  activeOrderId?: string;
  activeOrderCode?: string;
  activeAmount?: number;
  serviceRequestedAt?: string;
}

interface TableState {
  tables: TableItem[];
  selectedFloor: number;
  setTables: (tables: TableItem[]) => void;
  updateTableStatus: (tableId: string, status: TableItem['status'], extra?: Partial<TableItem>) => void;
  setSelectedFloor: (floor: number) => void;
  resolveServiceCall: (tableId: string) => void;
}
```

---

# 5. ĐẶC TẢ CUSTOM HOOKS & REAL-TIME WEBSOCKETS (SIGNALR & WEB AUDIO)

### 1. `hooks/useSignalR.ts` — Quản Lý Kết Nối WebSocket Real-Time
- Tự động kết nối tới các SignalR Hubs (`/hubs/orders`, `/hubs/kitchen`, `/hubs/payments`, `/hubs/notifications`).
- Cơ chế Auto-reconnect với backoff lũy thừa: `0s`, `2s`, `5s`, `10s`.
- Tự động tham gia Client Group (`JoinOrderGroup`, `JoinKitchenGroup`, `JoinPaymentGroup`, `JoinBranchNotifications`).
- Cleanup event listeners khi component unmount.

### 2. `hooks/useWebAudio.ts` — Bộ Phát Âm Thanh Tổng Hợp Không Cần File Tải Nặng
```typescript
export const useWebAudio = () => {
  const playNewTicketSound = () => {
    // 880Hz -> 1174Hz Sine wave 300ms (Vé đơn mới)
    const ctx = new (window.AudioContext || (window as any).webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(880, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1174, ctx.currentTime + 0.3);
    gain.gain.setValueAtTime(0.3, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.3);
  };

  const playOverdueAlertSound = () => {
    // 440Hz xung 3 nhịp cảnh báo đơn trễ > 5 phút
    const ctx = new (window.AudioContext || (window as any).webkitAudioContext)();
    [0, 0.2, 0.4].forEach((timeOffset) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'square';
      osc.frequency.setValueAtTime(440, ctx.currentTime + timeOffset);
      gain.gain.setValueAtTime(0.2, ctx.currentTime + timeOffset);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + timeOffset + 0.15);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(ctx.currentTime + timeOffset);
      osc.stop(ctx.currentTime + timeOffset + 0.15);
    });
  };

  const playServiceCallSound = () => {
    // 587Hz Chuông gọi bàn êm dịu
    const ctx = new (window.AudioContext || (window as any).webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(587, ctx.currentTime);
    gain.gain.setValueAtTime(0.25, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.5);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.5);
  };

  return { playNewTicketSound, playOverdueAlertSound, playServiceCallSound };
};
```

### 3. `hooks/useAttendanceWifi.ts` — Lấy Thông Tin Mạng WiFi & Thực Hiện Chấm Công
- Đọc thông tin mạng và gửi request tới `/api/v1/attendances/wifi-checkin` và `/api/v1/attendances/wifi-checkout`.

### 4. `hooks/useApiQuery.ts` & `hooks/useApiMutation.ts`
- Bọc TanStack Query v5 với Axios Instance, tự động đính kèm Token JWT, trích xuất `ApiResponse<T>` và hiển thị Toast báo lỗi RFC 7807 tự động.

---

# 6. HỆ THỐNG KIỂU DỮ LIỆU TYPESCRIPT (TYPESCRIPT TYPES & DTOS)

Toàn bộ Type definitions được định nghĩa tại `frontend/src/types/index.ts` khớp 100% với DTOs của Backend .NET 8 Clean Architecture:

```typescript
// ==========================================
// 1. DOMAIN ENUMS
// ==========================================
export type OrderType = 'DineIn' | 'TakeAway' | 'Delivery';
export type OrderStatus = 'PendingPayment' | 'Paid' | 'Confirmed' | 'Preparing' | 'Ready' | 'Delivering' | 'Completed' | 'Cancelled';
export type PaymentMethod = 'VIETQR' | 'CASH';
export type PaymentStatus = 'Pending' | 'Success' | 'Failed' | 'Expired';
export type UserRole = 'CashierStaff' | 'BaristaStaff' | 'BranchManager' | 'ChainAdmin';
export type TableStatus = 'Available' | 'Occupied_Paid' | 'Occupied_PendingPayment' | 'ServiceRequested';

// ==========================================
// 2. CORE RESPONSE ENVELOPES
// ==========================================
export interface ApiResponse<T> {
  success: boolean;
  statusCode: number;
  message: string;
  data: T;
  timestampUtc: string;
}

export interface PagedResponse<T> extends ApiResponse<T[]> {
  pageIndex: number;
  pageSize: number;
  totalCount: number;
  totalPages: number;
  hasPreviousPage: boolean;
  hasNextPage: boolean;
}

export interface ProblemDetails {
  type: string;
  title: string;
  status: number;
  detail: string;
  instance?: string;
  errors?: Record<string, string[]>;
  timestampUtc: string;
}

// ==========================================
// 3. PRODUCT & MENU MODELS
// ==========================================
export interface ProductModifierDto {
  id: string;
  name: string;
  priceAdjustment: number;
  isDefault: boolean;
}

export interface ProductSizeDto {
  id: string;
  sizeName: string;
  price: number;
  isDefault: boolean;
}

export interface ProductDto {
  id: string;
  name: string;
  sku: string;
  description?: string;
  imageUrl?: string;
  basePrice: number;
  categoryId: string;
  categoryName: string;
  isAvailable: boolean;
  sizes: ProductSizeDto[];
  modifiers: ProductModifierDto[];
}

export interface CategoryDto {
  id: string;
  name: string;
  displayOrder: number;
  isActive: boolean;
  itemCount: number;
}

// ==========================================
// 4. ORDER & PAYMENT MODELS
// ==========================================
export interface CreateDineInPrepaidOrderRequest {
  branchId: string;
  tableId: string;
  customerPhone?: string;
  voucherCode?: string;
  items: {
    productId: string;
    sizeId: string;
    quantity: number;
    sugarLevel: string;
    iceLevel: string;
    selectedModifierIds: string[];
    notes?: string;
  }[];
}

export interface CreateDineInPostpaidOrderRequest extends CreateDineInPrepaidOrderRequest {}

export interface CreateDeliveryOrderRequest {
  branchId: string;
  recipientName: string;
  recipientPhone: string;
  deliveryAddress: string;
  shipperNotes?: string;
  voucherCode?: string;
  items: {
    productId: string;
    sizeId: string;
    quantity: number;
    sugarLevel: string;
    iceLevel: string;
    selectedModifierIds: string[];
    notes?: string;
  }[];
}

export interface CreateTakeawayOrderRequest {
  branchId: string;
  customerPhone: string;
  redeemFreeCup: boolean;
  paymentMethod: PaymentMethod;
  tenderAmount: number;
  voucherCode?: string;
  items: {
    productId: string;
    sizeId: string;
    quantity: number;
    sugarLevel: string;
    iceLevel: string;
    selectedModifierIds: string[];
    notes?: string;
  }[];
}

export interface OrderDetailDto {
  id: string;
  orderNumber: string;
  orderType: OrderType;
  status: OrderStatus;
  branchId: string;
  branchName: string;
  tableId?: string;
  tableNumber?: string;
  recipientName?: string;
  recipientPhone?: string;
  deliveryAddress?: string;
  deliveryFee: number;
  subtotalAmount: number;
  discountAmount: number;
  totalAmount: number;
  paymentMethod: PaymentMethod;
  paymentStatus: PaymentStatus;
  qrCodeUrl?: string;
  createdAtUtc: string;
  estimatedMinutes: number;
  queuePosition: number;
  items: {
    id: string;
    productName: string;
    sizeName: string;
    unitPrice: number;
    quantity: number;
    totalPrice: number;
    sugarLevel: string;
    iceLevel: string;
    modifiers: string[];
    notes?: string;
  }[];
}

// ==========================================
// 5. CRM & LOYALTY MODELS
// ==========================================
export interface CustomerLookupDto {
  id: string;
  phone: string;
  fullName: string;
  cupBalance: number;
  eligibleForFreeCup: boolean;
  totalOrdersCount: number;
  lastOrderDate?: string;
}

// ==========================================
// 6. SHIFTS & Z-REPORT MODELS
// ==========================================
export interface OpenShiftRequest {
  branchId: string;
  openingCash: number;
}

export interface CloseShiftRequest {
  shiftId: string;
  denominations: Record<number, number>;
  physicalCashTotal: number;
  justificationReason?: string;
}

export interface ZReportDto {
  id: string;
  shiftId: string;
  branchName: string;
  cashierName: string;
  openedAtUtc: string;
  closedAtUtc: string;
  openingCash: number;
  cashSales: number;
  vietQrSales: number;
  totalRevenue: number;
  theoreticalCash: number;
  physicalCash: number;
  variance: number;
  justificationReason?: string;
  denominations: Record<number, number>;
}

// ==========================================
// 7. AI & APRIORI COMBO MODELS
// ==========================================
export interface MineCombosRequest {
  minSupport: number;
  minConfidence: number;
}

export interface ComboCandidateDto {
  id: string;
  productIds: string[];
  productNames: string[];
  originalPrice: number;
  bomCost: number;
  grossMarginPercent: number;
  support: number;
  confidence: number;
  lift: number;
  suggestedDiscountPercent: number;
  proposedPrice: number;
}

export interface ApproveComboRequest {
  comboCandidateId: string;
  comboName: string;
  discountPercent: number;
  finalPrice: number;
  startDateUtc: string;
  endDateUtc: string;
}
```

---

# 7. BẢNG MA TRẬN KHÁM PHÁ TÍNH NĂNG (FEATURES DISCOVERED TABLE — 62 FEATURES)

## Features Discovered
| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Customer PWA | Table QR Scanner & Dine-in Menu | Quét QR bàn mở thực đơn số | `tableId`, `branchId`, `sig` | Menu DTOs, Table info | 400 Invalid HMAC, 404 Table Not Found | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 2 | Customer PWA | AI-1 Gemini Drink Recommender | Chatbot tư vấn đồ uống theo thời tiết/khẩu vị | Prompt text, Calorie/Taste pref | AI Response Text + Product Cards | Fallback to Default Popular items | `01_Smart_FB_OS.md`, `03_API_Contract.md` |
| 3 | Customer PWA | Product BOM Customizer | Tùy biến Size (S/M/L), Đường, Đá, Toppings | Size, Sugar, Ice, Toppings | Updated Cart Item + Price | Validate min/max toppings | `04_Thiet_Ke_UI_UX.md` |
| 4 | Customer PWA | Dine-In Branch A: VietQR Prepaid | Tạo đơn trả trước qua VietQR PayOS | Cart Items, Phone, BranchId | Dynamic VietQR + 10m Timer | 400 Validation, 409 Conflict Table | `01_Smart_FB_OS.md`, `02_Sequence_Diagrams.md` |
| 5 | Customer PWA | Dine-In Branch B: Cash Postpaid | Tạo đơn trả sau gửi thẳng xuống bếp | Cart Items, TableId | Confirmed Order DTO | 400 Validation, 409 Table Occupied | `01_Smart_FB_OS.md`, `02_Sequence_Diagrams.md` |
| 6 | Customer PWA | 10-Minute VietQR Timer & Status Poll | Bộ đếm ngược 10p & lắng nghe thanh toán | OrderId, SignalR event | Payment Confirmed -> Redirect Tracking | Auto-cancel & Release soft stock on timeout | `04_Thiet_Ke_UI_UX.md`, `02_Sequence_Diagrams.md` |
| 7 | Customer PWA | QR Delivery Form (Ship 20k, 100% VietQR) | Đặt giao tận nơi, cộng 20k ship, khóa COD | Name, Phone (10-digit), Address, Note | Order Created + VietQR | 400 Invalid Phone/Address | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 8 | Customer PWA | Live Order Stepper Tracking | Theo dõi tiến độ đơn hàng thời gian thực | OrderId, SignalR `OrderStatusUpdated` | Realtime status, queue position | 404 Order Not Found | `04_Thiet_Ke_UI_UX.md`, `03_API_Contract.md` |
| 9 | Customer PWA | Service Bell Calling Button | Khách bấm chuông gọi phục vụ bàn | TableId, OrderId | SignalR `ServiceRequested` to staff | Rate limit 1 press / 60 seconds | `04_Thiet_Ke_UI_UX.md`, `03_API_Contract.md` |
| 10 | Customer PWA | 1-5 Star Review & Photo Upload | Chấm điểm trải nghiệm, upload 1-3 ảnh | Rating (1-5), Tags, Text, 1-3 WebP Images | Review Submitted Confirmation | If <= 2 Stars, triggers SignalR Red Alert | `04_Thiet_Ke_UI_UX.md`, `03_API_Contract.md` |
| 11 | Customer PWA | CRM Loyalty Progress Viewer | Xem tiến độ tích lũy ly (Phone lookup) | Phone number | CupBalance (e.g. 7/10) | Return 0 if new customer | `04_Thiet_Ke_UI_UX.md` |
| 12 | Customer PWA | Quick Reorder 1-Tap | Đặt lại đơn hàng từ lịch sử | Past OrderId | Pre-filled Cart Items | Skip unavailable/86-locked items | `04_Thiet_Ke_UI_UX.md` |
| 13 | Kitchen KDS | Real-time Ticket Stream | Nhận vé đơn hàng mới qua WebSocket | BranchId, StationId | KdsTicket DTOs stream | Auto reconnect on socket drop | `04_Thiet_Ke_UI_UX.md`, `03_API_Contract.md` |
| 14 | Kitchen KDS | SLA Color-Coded Timers | Thẻ vé đổi màu: Xanh (<3m), Vàng (3-5m), Đỏ (>5m) | Ticket elapsed seconds | Visual color + pulsing badge | Pulse sound at > 5m | `04_Thiet_Ke_UI_UX.md` |
| 15 | Kitchen KDS | Web Audio Synthesizer Alerts | Phát âm thanh chuông vé mới & báo trễ | Web Audio trigger | 880-1174Hz or 440Hz chime | Silent if audio context blocked | `04_Thiet_Ke_UI_UX.md` |
| 16 | Kitchen KDS | BOM Recipe Formula Popup | Tra cứu định lượng pha chế từng size | ProductId, SizeId | Modal listing ml/grams | 404 Recipe Not Found | `04_Thiet_Ke_UI_UX.md` |
| 17 | Kitchen KDS | Status Update & Auto BOM Deduct | Bấm Bắt đầu / Hoàn tất (Trừ kho BOM) | OrderId, Status (`Ready`) | Status updated + Stock deducted | 400 Invalid transition | `01_Smart_FB_OS.md`, `02_Sequence_Diagrams.md` |
| 18 | Kitchen KDS | 86-Toggle Emergency Out-of-Stock | Khóa hết món nhanh tại quầy bar | ProductId, isAvailable (false) | Broadcast `Item86Toggled` | 403 Non-barista role | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 19 | Kitchen KDS | KDS Batching Mode | Gom các món giống nhau pha chế 1 mẻ | Grouped ProductId, Batch Qty | Multi-order Ready status update | Partial complete handling | `04_Thiet_Ke_UI_UX.md` |
| 20 | Staff POS | Takeaway POS Phone Lookup | Thu ngân tra cứu SĐT khách tại quầy | Customer Phone | FullName, CupBalance, FreeCup status | Create new profile if phone not found | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 21 | Staff POS | 10-Cup Loyalty Free Redemption | Đổi 1 ly miễn phí (-35k) cho đơn Takeaway | CupBalance >= 10, Redeem flag | Discount applied (-100% 1 cup), CupBalance -10 | 422 If DineIn or Delivery or Balance < 10 | `01_Smart_FB_OS.md`, `05_UAT_Test_Cases.md` |
| 22 | Staff POS | Cash Tender & Change Calculator | Nhập tiền khách đưa, tự tính tiền thừa | Tender Amount, Order Total | Change Amount to return | Error if Tender < Total | `04_Thiet_Ke_UI_UX.md` |
| 23 | Staff POS | ESC/POS Thermal Receipt Print | In hóa đơn thanh toán kèm VietQR động | Order Details, VietQR Data | ESC/POS raw print stream | Alert if printer disconnected | `04_Thiet_Ke_UI_UX.md`, `02_Sequence_Diagrams.md` |
| 24 | Staff Ops | Floor Plan & Table Status Map | Xem sơ đồ bàn trực quan, đổi màu live | Floor ID, SignalR Table events | Table Grid with statuses | 404 Branch Not Found | `04_Thiet_Ke_UI_UX.md` |
| 25 | Staff Ops | Service Bell Alert & Resolution | Nhận chuông gọi bàn (Đỏ) & bấm Tiếp nhận | TableId, StaffId | Dismiss alert, return to normal | Rate limit spam calls | `04_Thiet_Ke_UI_UX.md`, `03_API_Contract.md` |
| 26 | Staff Ops | WiFi-Locked Attendance Check-in | Chấm công vào ca khóa mạng WiFi | EmployeeCode, BSSID, Subnet IP | Clock-in Success DTO | 400/403 Bad WiFi / 4G blocked | `01_Smart_FB_OS.md`, `05_UAT_Test_Cases.md` |
| 27 | Staff Ops | WiFi-Locked Attendance Check-out | Chấm công ra ca khóa mạng WiFi | EmployeeCode, BSSID, Subnet IP | Clock-out Success DTO | 400/403 Invalid WiFi | `01_Smart_FB_OS.md` |
| 28 | Staff Ops | Shift Handover Summary | Xem tổng kết ca nhân viên & bàn giao | StaffId, ShiftId | Handover Summary Sheet | 400 Shift Not Open | `04_Thiet_Ke_UI_UX.md` |
| 29 | Manager Portal | Cash Drawer Shift Open | Mở ca két tiền, khai báo tiền mặt đầu ca | BranchId, OpeningCash (e.g. 1.000.000đ) | Shift Opened Record | 409 If shift already open | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 30 | Manager Portal | Z-Report 6 Denominations Counter | Đếm tiền thực tế 6 mệnh giá (500k-10k) | Counts for 500k, 200k, 100k, 50k, 20k, 10k | Physical Total, Variance calculation | Require reason if variance != 0 | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 31 | Manager Portal | Cash Variance Red Alert (>50k) | Bắt buộc giải trình & bắn alert nếu lệch > 50k | Variance, Justification Text | Shift Closed + Alert Admin | Block closing if no reason entered | `01_Smart_FB_OS.md`, `05_UAT_Test_Cases.md` |
| 32 | Manager Portal | BOM Stock Physical vs Theoretical Audit | Kiểm kê kho, tính hao hụt thực tế vs BOM | Physical Counts per Ingredient | Variance Amount, % Wastage | Warning if wastage > 3% | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 33 | Manager Portal | Supplier Goods Receipt with Photo | Nhập kho NCC, tải ảnh hóa đơn chứng từ | Supplier, Items, Quantities, Invoice Image | Goods Receipt Note Created | 400 Missing Invoice photo | `04_Thiet_Ke_UI_UX.md` |
| 34 | Manager Portal | Internal Bar Stock Dispatch Note | Lập phiếu xuất kho tổng ra quầy pha chế | Ingredient IDs, Quantities | Stock Transferred to Bar | 400 Exceeds Main Stock | `04_Thiet_Ke_UI_UX.md` |
| 35 | Manager Portal | Branch WiFi BSSID & IP Config | Khai báo MAC Router & IP Subnet chấm công | BSSID strings, Subnet CIDRs | Updated BranchWifiConfigs | 400 Invalid MAC format | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 36 | Manager Portal | Red Alert <= 2 Star Review Inbox | Nhận cảnh báo tức thời khi khách đánh giá tệ | SignalR `LowRatingAlert` | Alert Popup with Table & Phone | Log manager action response | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 37 | Manager Portal | Review Customer Photo Moderation | Duyệt hoặc từ chối ảnh khách tải lên menu | ReviewImageId, Action (Approve/Reject) | Image status updated | 404 Image Not Found | `04_Thiet_Ke_UI_UX.md` |
| 38 | Admin Portal | Consolidated Multi-Branch P&L | Báo cáo Doanh thu, Chi phí BOM, Lãi gộp | Date Range, Branch Filter | Consolidated P&L Cards & Charts | 403 Forbidden non-admin | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 39 | Admin Portal | BCG Menu Matrix Analysis | Phân tích món Ngôi sao, Bò sữa, Chó mực | Historical Sales Data | BCG Quadrant Chart | Min 30 days data required | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 40 | Admin Portal | Full CRUD Products & Sizes | Thêm/sửa/xóa món ăn, kích cỡ S/M/L | Product Form, Image, Sizes | Product Created/Updated | 400 Duplicate SKU | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 41 | Admin Portal | BOM Recipe Definition per Size | Định lượng ml/grams từng nguyên liệu theo size | ProductId, SizeId, Ingredients list | ProductBOM entries created | 400 Total qty <= 0 | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 42 | Admin Portal | Product Replacement Workflow | Thay thế món ăn cũ bằng món mới an toàn | OldProductId, NewProductId | Transferred recipes & mappings | Soft delete old product | `04_Thiet_Ke_UI_UX.md` |
| 43 | Admin Portal | Drag-and-Drop Category Reorder | Kéo thả sắp xếp thứ tự danh mục menu PWA | Ordered Category ID List | Updated `display_order` | 400 Invalid ID list | `04_Thiet_Ke_UI_UX.md` |
| 44 | Admin Portal | Seasonal Menu Scheduler | Lên lịch mở/đóng bán thực đơn theo mùa vụ | Menu Name, Item IDs, Start/End Date | Scheduled Seasonal Campaign | Auto activate on start date | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 45 | Admin Portal | Regional Matrix Pricing Manager | Thiết lập bảng giá theo vùng chi nhánh | Region ID, Product ID, Price Delta | Branch Price Matrix | Apply instant to branch menu | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 46 | Admin Portal | AI-2 Apriori Combo Mining Engine | Khai phá giỏ hàng lịch sử tìm combo | Min Support, Min Confidence | Candidate Combo Pairs + Lift | Min 100 orders required | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 47 | Admin Portal | AI-2 Combo Discount Slider & Publish | Kéo slider giảm giá 5-30% & duyệt lên PWA | Combo Candidate ID, Discount %, Dates | Published Combo on Customer Menu | 400 Negative profit margin | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 48 | Admin Portal | Voucher Campaign Management | Tạo mã giảm giá (Theo %, Cố định, Hạn dùng) | Code, Discount Type, Value, Min Order | Active Voucher Campaign | 409 Code already exists | `04_Thiet_Ke_UI_UX.md` |
| 49 | Admin Portal | CRM RFM Customer Segmentation | Phân tích khách hàng theo Recency, Frequency | Customer Transactions | Segmented Customer Lists | Exportable CSV | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 50 | Admin Portal | Immutable Audit Logs Viewer | Xem nhật ký kiểm toán bất biến hệ thống | Filters (User, Action, Date) | Paginated Audit Log Entries | Read-only strictly | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 51 | Admin Portal | PayOS Payment Gateway Configuration | Cấu hình Client ID, Api Key, Checksum Key | PayOS Credentials, Webhook URL | Config Encrypted in Database | 400 Invalid API Key | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 52 | Admin Portal | RBAC User & Role Management | Tạo tài khoản, phân quyền 4 vai trò | User Profile, Role, Branch Assignment | User Created / Updated | 409 Duplicate EmployeeCode | `03_API_Contract.md`, `04_Thiet_Ke_UI_UX.md` |
| 53 | Admin Portal | Excel/CSV Data Exporter | Xuất toàn bộ báo cáo P&L, Kho, Ca, Đơn hàng | Report Type, Date Range | `.xlsx` / `.csv` File Download | Error toast if query empty | `04_Thiet_Ke_UI_UX.md` |
| 54 | Shared Core | SignalR Auto-Reconnect & Offline Banner | Tự động kết nối lại khi rớt mạng | WebSocket lifecycle | Visual banner "Đang kết nối lại..." | Fallback to polling if failed | `03_API_Contract.md`, `04_Thiet_Ke_UI_UX.md` |
| 55 | Shared Core | RFC 7807 ProblemDetails Error Toast | Hiển thị thông báo lỗi thân thiện | RFC 7807 JSON Response | Form field error highlight & Toast | Generic toast for 500 error | `03_API_Contract.md` |
| 56 | Shared Core | Dark/Light Mode Theme Provider | Hỗ trợ Light (PWA/POS/Admin) & Dark (KDS) | Next-themes provider | Theme CSS classes applied | Prevent flash on load | `04_Thiet_Ke_UI_UX.md` |
| 57 | Shared Core | Responsive Layout System | Tối ưu 375px (PWA), 1024px (Tablet), 1920px (TV) | Viewport media queries | Tailored layout per route group | Zero horizontal scroll bug | `04_Thiet_Ke_UI_UX.md` |
| 58 | Customer PWA | Anonymous Review Toggle | Đánh giá không lưu SĐT công khai | Toggle boolean | Review saved without user link | Store order link internally | `04_Thiet_Ke_UI_UX.md` |
| 59 | Customer PWA | WebP Image Client-Side Compressor | Tự nén ảnh trước khi upload giảm băng thông | Raw Camera/File Blob | Compressed WebP Blob (< 500KB) | Fallback if WebP unsupported | `04_Thiet_Ke_UI_UX.md` |
| 60 | Kitchen KDS | Multi-Station Order Routing | Phân luồng món ra máy Bar vs Bếp riêng | Category / Station mapping | Filtered Ticket View per Station | View all option available | `01_Smart_FB_OS.md`, `04_Thiet_Ke_UI_UX.md` |
| 61 | Manager Portal | Low Stock Alert Notification | Bắn thông báo khi nguyên liệu dưới ngưỡng an toàn | Stock Level < MinThreshold | Notification Bell + Highlight row | Audio alert in manager portal | `03_API_Contract.md`, `04_Thiet_Ke_UI_UX.md` |
| 62 | Staff POS | Offline Local Order Draft Storing | Lưu nháp giỏ hàng tạm khi mạng lag | LocalStorage Zustand Persist | Restored Cart on Reconnect | Warn cashier before submit | `04_Thiet_Ke_UI_UX.md` |

---

# 8. MA TRẬN KỊCH BẢN BIÊN & NGOẠI LỆ (EDGE CASES & RESILIENCE MATRIX)

## Edge Cases
| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | Dine-In VietQR | Khách không chuyển khoản sau 10 phút đếm ngược | Timer về `00:00`, hiển thị "Mã QR đã hết hạn", hệ thống tự động hoàn lại Tồn kho tạm giữ trong Redis (`inventory:reserved`), mở khóa bàn về `Available`. |
| 2 | Dine-In VietQR | 2 khách tại 2 bàn cùng đặt món cuối cùng trong kho | Khách thứ nhất tạo đơn kích hoạt RedLock và giữ tồn kho thành công; khách thứ hai nhận thông báo lỗi RFC 7807: "Món ăn vừa hết nguyên liệu khả dụng". |
| 3 | QR Delivery | Khách nhập số điện thoại không hợp lệ (9 số hoặc có chữ) | Form kích hoạt validator ngay trên giao diện (Client-side regex), hiển thị nhãn đỏ: "Số điện thoại người nhận phải có 10 chữ số bắt đầu bằng 03, 05, 07, 08, 09". |
| 4 | Takeaway POS | Thu ngân bấm đổi ly miễn phí cho đơn Dine-In hoặc Delivery | Nút đổi ly bị khóa (Disabled) hoặc Backend trả về HTTP 422: "Chương trình tích 10 ly đổi 1 ly chỉ áp dụng duy nhất cho đơn hàng Mua mang về (Takeaway)". |
| 5 | Takeaway POS | Khách hàng mới chưa có trong hệ thống CRM | Thu ngân nhập SĐT, hệ thống tự động khởi tạo hồ sơ khách hàng mới với `CupBalance = 0`, cho phép tạo đơn bình thường. |
| 6 | WiFi Attendance | Nhân viên bật 4G hoặc kết nối WiFi ngoài quán để chấm công | Ứng dụng đọc BSSID/IP không khớp với `BranchWifiConfigs`, hiển thị cảnh báo đỏ và trả về HTTP 403 Forbidden: "Vui lòng kết nối vào mạng WiFi chính thức của quán". |
| 7 | KDS SLA | Barista chưa hoàn thành đơn sau 5 phút | Thẻ đơn hàng chuyển sang màu Đỏ viền nhấp nháy (`state-danger`), kích hoạt chuỗi 3 xung âm thanh cảnh báo 440Hz từ Web Audio API. |
| 8 | 86-Toggle | Barista gạt khóa món đang có trong giỏ hàng khách chưa đặt | Khi khách bấm đặt hàng, Backend kiểm tra cờ khả dụng và trả về HTTP 422 ProblemDetails; giỏ hàng tự động đánh dấu đỏ món bị khóa và yêu cầu xóa món. |
| 9 | Z-Report | Tiền thực đếm lệch 100.000đ so với lý thuyết hệ thống | Hệ thống tính `Variance = -100.000đ`, đổi màu đỏ cảnh báo, bắt buộc Quản lý phải nhập nội dung giải trình chênh lệch trước khi nút [Xác Nhận Đóng Ca] được kích hoạt. Gửi Red Alert tới Admin. |
| 10 | Review | Khách hàng chấm điểm 1 sao kèm ảnh phàn nàn đồ uống | Màn hình Quản lý chi nhánh lập tức rung chuông và xuất hiện thẻ cảnh báo khẩn cấp (Red Alert) hiển thị Số bàn và SĐT khách để quản lý tới xin lỗi trực tiếp tại bàn trong 3 phút. |
| 11 | Network Drop | Thiết bị POS hoặc KDS mất kết nối mạng Internet đột ngột | Hiển thị Banner màu vàng trên đỉnh màn hình: "Mất kết nối WebSocket. Đang tự động kết nối lại...", lưu giỏ hàng vào Zustand LocalStorage và tự động đồng bộ khi có mạng lại. |
| 12 | Apriori AI-2 | Chủ chuỗi kéo slider chiết khấu 30% khiến giá bán thấp hơn giá vốn BOM | Thẻ Combo hiển thị cảnh báo viền đỏ "Lợi nhuận âm (-5%)" và khóa nút [Phê Duyệt], bảo vệ chuỗi khỏi chiến dịch khuyến mãi lỗ vốn. |

---

*Báo cáo đặc tả Frontend Spec Miner cho hệ thống Smart F&B OS đã hoàn thành toàn diện — 100% Zero Placeholder — Sẵn sàng cung cấp dữ liệu cho quá trình phát triển mã nguồn Next.js 14.*
