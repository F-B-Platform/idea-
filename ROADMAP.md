# 🗺️ ROADMAP & KẾ HOẠCH CHUẨN BỊ TRIỂN KHAI DỰ ÁN SMART F&B OS

> **Mục tiêu:** Đồ án tốt nghiệp & Định hướng Thương mại  
> **Quy mô Team:** 4 người (2 Backend + 2 Frontend)  
> **Tech Stack:** .NET 8 (C#) + Next.js 14 (TypeScript) + PostgreSQL 16 + Redis + SignalR  
> **Thời gian:** 16 tuần (8 Sprints)

---

## 📌 PHẦN 1: NHỮNG VIỆC BẮT BUỘC LÀM TRƯỚC KHI CODE (PRE-PROJECT PREREQUISITES)

> ⚠️ **CẢNH BÁO:** Không gõ bất kỳ dòng code nào cho đến khi **TẤT CẢ 4 BƯỚC THIẾT KẾ** dưới đây được cả team chốt 100%.

```
┌─────────────────────────────────────────────────────────────────────────┐
│              CÁC BƯỚC CHUẨN BỊ NỀN TẢNG (GIAI ĐOẠN PRE-CODE)             │
│                                                                         │
│  1. CHỐT PHẠM VI (MVP) ──► 2. THIẾT KẾ DB & API ──► 3. THIẾT KẾ UI/UX   │
│  (Chốt 12 nhóm core)      (ERD 28 bảng & API Spec)  (Wireframe 15 màn)  │
│                                                                  │      │
│                                                                  ▼      │
│  5. BẮT ĐẦU CODE ◄───────── 4. CHUẨN BỊ MÔI TRƯỜNG & GIT STRATEGY ──────┘
│  (Sprint 2 trở đi)          (Docker Compose, .NET Solution, Next.js)   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### BƯỚC 1: Phân Tích & Chốt Phạm Vi Tính Năng (Scope & MVP)
* **Nhiệm vụ:** Chọn ra danh sách tính năng **BẮT BUỘC** phải chạy mượt để demo (MVP Tier 1), hoãn lại các tính năng nâng cao sang Phase sau.
* **Chi tiết MVP Tier 1 (12 nhóm tính năng cốt lõi):**
  1. **QR Order:** Khách quét QR → Xem Menu → Tùy chỉnh (Size/Đường/Đá/Topping) → Giỏ hàng → Đặt món.
  2. **KDS (Bếp):** Nhận đơn real-time → Xem công thức pha → Cảnh báo chờ lâu (Xanh/Vàng/Đỏ) → Bấm hoàn thành.
  3. **Tracking đơn:** Khách xem trạng thái tiến trình (Chờ xác nhận → Đang pha → Đã xong).
  4. **Yêu cầu bill & Gọi NV:** Khách nhấn nút → Phát alert tới Staff/KDS.
  5. **Thanh toán:** Nhân viên phát hành VietQR / Tiền mặt → Xác nhận thu tiền.
  6. **Mở/Kết ca:** Quản lý khai báo tiền đầu két, đối soát tiền thực đếm cuối ca.
  7. **Admin Menu CRUD:** Quản lý Danh mục, Món ăn, Biến thể, Topping, Ẩn/Hiện món.
  8. **Admin Dashboard:** Biểu đồ doanh thu real-time, số đơn trong ngày, top món bán chạy.
  9. **Xác thực & Phân quyền (RBAC):** JWT Auth cho 4 vai trò (Admin, Manager, Staff, Customer).
  10. **Quản lý Chi nhánh & Bàn:** Quản lý sơ đồ bàn, vùng, mã QR bàn.
  11. **CRM SĐT cơ bản:** Khách nhập SĐT → Tích điểm Loyalty tự động.
  12. **SignalR Real-time:** Kết nối 2 chiều giữa Khách ↔ Bếp ↔ Nhân viên ↔ Quản lý.

---

### BƯỚC 2: Thiết Kế Hợp Đồng Dữ Liệu (Database Schema & API Spec)
* **Nhiệm vụ:** Thiết kế chi tiết cấu trúc Database và Hợp đồng API trước khi viết bất kỳ hàm Controller hay Service nào.
* **Database Schema (ERD 28 Bảng):**
  * *Nhóm Core (7 bảng):* `Branch`, `Table`, `QrCode`, `Category`, `Product`, `ProductVariant`, `Topping`.
  * *Nhóm Order (4 bảng):* `Order`, `OrderItem`, `OrderItemTopping`, `Payment`.
  * *Nhóm User & CRM (3 bảng):* `User`, `BranchUser`, `Customer`.
  * *Nhóm Kho (4 bảng):* `Ingredient`, `ProductIngredient`, `InventoryStock`, `StockTransaction`.
  * *Nhóm Vận hành (3 bảng):* `Attendance`, `CashShift`, `Shift`.
  * *Nhóm Loyalty & Khuyến mãi (5 bảng):* `LoyaltyTransaction`, `Voucher`, `VoucherUsage`, `Review`, `ReviewImage`.
  * *Nhóm Hệ thống (2 bảng):* `Notification`, `AuditLog`.
* **API Specification (JSON Contracts):**
  * Định nghĩa chuẩn Response chung (`success`, `data`, `message`, `error`, `pagination`).
  * Danh sách 45+ endpoints RESTful chi tiết cho Auth, Products, Orders, Payments, Customers, Inventory, Shifts, Reports.
  * Thống nhất danh sách sự kiện SignalR Real-time (`NewOrder`, `OrderStatusChanged`, `ItemCompleted`, `BillRequested`).

---

### BƯỚC 3: Thiết Kế Giao Diện UI/UX (Wireframe)
* **Nhiệm vụ:** Vẽ khung phác thảo (Wireframe) toàn bộ các màn hình chính để Frontend dev nắm rõ Layout.
* **Các màn hình bắt buộc thiết kế Wireframe:**
  1. *QR Order (Khách hàng):* Trang Menu, Detail món (Modal chọn size/topping), Giỏ hàng, Trạng thái đơn, Trang Bill.
  2. *KDS (Barista):* Màn hình Bếp full-screen, Card đơn hàng dạng Kanban, Modal xem công thức.
  3. *Staff App:* Alert bar (Thông báo gọi bàn/bill), Sơ đồ bàn trực quan.
  4. *Manager App:* Form mở/kết ca, Form nhập/xuất kho.
  5. *Admin Dashboard:* Trang tổng quan (Charts), Bảng quản lý Menu, Bảng phân quyền.

---

### BƯỚC 4: Chuẩn Bị Môi Trường Dev & Quy Trình Team (Setup & Git Strategy)
* **Nhiệm vụ:** Thiết lập bộ khung dự án tiêu chuẩn, đảm bảo 4 thành viên kéo về là chạy được ngay.
* **Môi trường & Tooling:**
  * Cài đặt .NET 8 SDK, Node.js v20+, Docker Desktop.
  * Cấu hình `docker-compose.yml` chạy PostgreSQL 16 & Redis 7.
* **Cấu trúc Monorepo:**
  * `src/backend/`: Solution .NET 8 Clean Architecture (`SmartFB.API`, `SmartFB.Application`, `SmartFB.Domain`, `SmartFB.Infrastructure`, `SmartFB.Tests`).
  * `src/frontend/`: Monorepo Next.js 14 với các Route Groups (`(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`).
* **Quy trình Git & Workflow:**
  * Branch chính: `main` (Production), `develop` (Integration).
  * Branch tính năng: `feature/be1-auth`, `feature/be2-inventory`, `feature/fe1-menu`, `feature/fe2-admin`.
  * Quy định: 100% code vào `develop` phải qua Pull Request (PR) và có ít nhất 1 thành viên review.

---

## 👥 PHẦN 2: PHÂN CÔNG VAI TRÒ TEAM 4 NGƯỜI

```
┌────────────────────────────────────────────────────────────────────────┐
│                        CƠ CẤU PHÂN CÔNG TEAM                           │
│                                                                        │
│   BACKEND TEAM (2 NGƯỜI)               FRONTEND TEAM (2 NGƯỜI)         │
│   ┌──────────────────────────┐         ┌───────────────────────────┐   │
│   │ BE1 (Backend Lead)       │         │ FE1 (Frontend Lead)       │   │
│   │ • Auth, Order Flow       │ ◄─────► │ • QR Order (Khách)        │   │
│   │ • SignalR Real-time      │ (Nối    │ • KDS Bếp (Barista)       │   │
│   │ • VietQR Payment, CRM    │  API)   │ • Staff App               │   │
│   └──────────────────────────┘         └───────────────────────────┘   │
│   ┌──────────────────────────┐         ┌───────────────────────────┐   │
│   │ BE2 (Backend Dev)        │         │ FE2 (Frontend Dev)        │   │
│   │ • DB, EF Core, Migration │ ◄─────► │ • Admin Dashboard         │   │
│   │ • Kho hàng & Chấm công   │ (Nối    │ • Manager App (Kho/Ca)    │   │
│   │ • Báo cáo Doanh thu & AI │  API)   │ • CRM & Analytics UI      │   │
│   └──────────────────────────┘         └───────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📅 PHẦN 3: ROADMAP CHI TIẾT 16 TUẦN (8 SPRINTS)

---

### 🟢 SPRINT 1 (Tuần 1–2): GIAI ĐOẠN THIẾT KẾ & SETUP MÔI TRƯỜNG
> **Mục tiêu:** Hoàn thành 100% thiết kế ERD, API Spec, Wireframe và khởi tạo bộ khung project.

* **BE1 (Backend Lead):**
  * Thống nhất ERD 28 bảng và lập tài liệu API Specification (45+ endpoints).
  * Khởi tạo .NET 8 Solution Clean Architecture (4 projects).
  * Viết file `docker-compose.yml` (PostgreSQL + Redis) & `.env.example`.
* **BE2 (Backend Dev):**
  * Định nghĩa toàn bộ 28 C# Entity classes trong `SmartFB.Domain`.
  * Cấu hình EF Core `AppDbContext` và Fluent API mappings trong `SmartFB.Infrastructure`.
  * Tạo bản Migration đầu tiên và viết script Seed Data mẫu (Chi nhánh, Bàn, Menu, User).
* **FE1 (Frontend Lead):**
  * Vẽ Wireframe UI cho QR Order (Menu, Cart, Detail, Order Status) & KDS Bếp.
  * Khởi tạo dự án Next.js 14 (App Router) với Route Groups `(customer)` và `(kds)`.
  * Xây dựng bộ thư viện UI Component dùng chung (Button, Card, Modal, Toast, Badge).
* **FE2 (Frontend Dev):**
  * Vẽ Wireframe UI cho Admin Dashboard và Manager App.
  * Thiết lập Layout Admin (Sidebar, Header, Main Container) trong Route Group `(admin)`.
  * Dựng trang Login và cấu hình Auth Context / JWT Token Storage.

🎯 **Milestone M0 (Cuối Tuần 2):** ERD & API Spec đã chốt ✅ | `docker compose up` chạy thành công ✅ | .NET Solution & Next.js khởi tạo sạch ✅.

---

### 🟢 SPRINT 2 (Tuần 3–4): BACKEND CORE & FRONTEND SKELETON
> **Mục tiêu:** Hoàn thành module Auth, RBAC, CRUD Menu/Chi nhánh và kết nối màn hình Menu tĩnh.

* **BE1:**
  * Xây dựng API Auth: Register, Login, Refresh Token (JWT + ASP.NET Identity).
  * Viết Middleware Auth & Phân quyền RBAC 4 vai trò (`Admin`, `Manager`, `Staff`, `Customer`).
  * Xây dựng CRUD API cho Product & Category (GET, POST, PUT, DELETE, Toggle).
* **BE2:**
  * Xây dựng CRUD API cho Branch, Table và QrCode.
  * Tối ưu Seed Data mẫu (3 chi nhánh, 20 bàn/chi nhánh, 30 món ăn uống).
  * Cấu hình Swagger/OpenAPI UI tự động hiển thị đầy đủ tài liệu API.
* **FE1:**
  * Dựng giao diện trang Menu Khách (`/customer/menu`): Tabs danh mục, lưới sản phẩm, Best seller badge.
  * Dựng Modal xem chi tiết món: Chọn Size, Mức đường/đá, Toppings, Ghi chú.
  * Xây dựng Zustand Store quản lý trạng thái Giỏ hàng (Cart Store).
* **FE2:**
  * Kết nối trang Login với API Auth thật, lưu Token và xử lý Guard Redirect theo Role.
  * Dựng trang Admin Quản lý Menu (`/admin/menu`): Bảng danh sách món, thanh tìm kiếm, bộ lọc.
  * Dựng Form Thêm/Sửa sản phẩm (`/admin/menu/new`): Upload ảnh, nhập giá, chọn biến thể.

🎯 **Milestone M1 (Cuối Tuần 4):** Login JWT thành công ✅ | API CRUD Menu chạy chuẩn ✅ | Khách hàng xem được Menu thật từ DB ✅.

---

### 🟢 SPRINT 3 (Tuần 5–6): MẠCH SỐNG HỆ THỐNG — ORDER FLOW & KDS REAL-TIME
> **Mục tiêu:** Hoàn thành luồng cốt lõi: Khách đặt món → KDS nhận đơn real-time → Barista pha chế xong.

* **BE1:**
  * Xây dựng Order API: `POST /orders` (Tạo đơn), `GET /orders/{id}` (Lấy chi tiết đơn).
  * Cấu hình SignalR `OrderHub`: Phát sự kiện `NewOrder` khi có đơn mới đặt.
  * Viết API cập nhật trạng thái món: `PATCH /orders/{id}/items/{itemId}/complete`.
* **BE2:**
  * Viết Entities & Service Quản lý Kho quầy (Ingredient, InventoryStock, StockTransaction).
  * Xây dựng API Mở ca / Kết ca (`POST /cash-shifts/open`, `POST /cash-shifts/close`).
  * Xây dựng API Xuất kho quầy và Kiểm kê nguyên liệu.
* **FE1:**
  * Dựng trang Checkout (`/customer/checkout`) và trang Trạng thái đơn (`/customer/order-status`).
  * Dựng màn hình KDS Bếp (`/kds/kitchen`): Layout Kanban full-screen, Card đơn hàng, Timer màu sắc.
  * Tích hợp SignalR Client vào KDS: Nhận đơn mới tức thì không cần reload trang.
* **FE2:**
  * Dựng trang Admin Quản lý Danh mục, Bàn và Chi nhánh.
  * Dựng giao diện Quản lý Sơ đồ bàn cho Manager.

🎯 **Milestone M2 (Cuối Tuần 6 - QUAN TRỌNG NHẤT):** Khách đặt món → KDS hiện đơn tức thì qua SignalR → Barista bấm xong → Khách thấy thanh tiến trình nhảy ✅.

---

### 🟢 SPRINT 4 (Tuần 7–8): THANH TOÁN VIETQR & DASHBOARD BÁO CÁO
> **Mục tiêu:** Hoàn thiện luồng Thanh toán, Tích điểm CRM và Dashboard Doanh thu Admin (Hoàn tất Tier 1).

* **BE1:**
  * Xây dựng Payment API: Sinh mã VietQR động (`POST /payments`), API Xác nhận thu tiền (`PATCH /payments/{id}/confirm`).
  * Viết API Yêu cầu bill (`POST /orders/{id}/request-bill`) & Gọi nhân viên hỗ trợ.
  * Xây dựng CRM API: Nhận diện SĐT khách (`POST /customers/identify`), Tích điểm Loyalty tự động.
* **BE2:**
  * Xây dựng Report API: Doanh thu theo ngày/ca/chi nhánh, Top món bán chạy, Biểu đồ theo giờ.
  * Viết API Chấm công nhân viên (`POST /attendance/check-in`, `check-out`).
* **FE1:**
  * Dựng trang Thanh toán (`/customer/bill`): Hiển thị mã VietQR động, tổng tiền, nút Gọi nhân viên.
  * Tích hợp SignalR Alert hiển thị thông báo "Bàn X yêu cầu bill / cần hỗ trợ" trên KDS & Staff App.
  * Dựng Modal nhập SĐT tích điểm cho khách hàng khi đặt món.
* **FE2:**
  * Dựng Admin Dashboard tổng quan (`/admin/dashboard`): Các thẻ KPI (Doanh thu, Đơn hàng, Khách hàng), Biểu đồ đường & cột.
  * Dựng trang Quản lý Ca làm việc cho Manager (`/manager/shift`): Nhập tiền đầu ca, kết ca, xem chênh lệch két.

🎯 **Milestone M3 (Cuối Tuần 8 - HOÀN THÀNH TIER 1 MVP):** Toàn bộ luồng từ Đặt món → Pha chế → Thanh toán VietQR → Cập nhật Doanh thu trên Admin Dashboard hoạt động 100% mượt mà ✅.

---

### 🟢 SPRINT 5 (Tuần 9–10): MỞ RỘNG TÍNH NĂNG TIER 2
> **Mục tiêu:** Bổ sung Quản lý Kho nâng cao, Feedback đánh giá, Voucher khuyến mãi và Staff App.

* **BE1:**
  * Xây dựng Voucher API: CRUD Voucher, Validation áp mã giảm giá vào đơn hàng.
  * Xây dựng API Gọi thêm món (`POST /orders/{id}/items` gộp vào đơn hiện tại).
  * Xây dựng Combo API (CRUD gói Combo giảm giá).
* **BE2:**
  * Xây dựng Review API: Đánh giá 1-5 sao, Upload ảnh review, Cảnh báo review bad (<=2 sao).
  * Viết Background Job kiểm tra Tồn kho tối thiểu → Tự động gửi Notification cảnh báo.
  * Viết API Báo hết món (`PATCH /products/{id}/out-of-stock`) → Tự ẩn trên Menu QR.
* **FE1:**
  * Dựng Staff Mobile App (`/staff/alerts`): Nhận thông báo đẩy gọi bàn, sơ đồ bàn xem trạng thái.
  * Dựng trang Feedback Khách hàng (`/customer/feedback`): Đánh giá sao, nhập nhận xét, tải ảnh.
  * Bổ sung nút "Gọi thêm món" và "Áp mã Voucher" trên trang QR Order.
* **FE2:**
  * Dựng giao diện Manager Quản lý Kho (`/manager/inventory`): Nhập kho NCC, Xuất kho quầy, Kiểm kê.
  * Dựng giao diện Admin Quản lý Voucher & Combo.

---

### 🟢 SPRINT 6 (Tuần 11–12): TÍCH HỢP AI ENGINE & TỐI ƯU CẢI TIẾN
> **Mục tiêu:** Tích hợp các tính năng AI (Chatbot tư vấn, Thống kê thông minh), Tối ưu PWA và Polish UI.

* **BE1:**
  * Tích hợp Google Gemini API vào .NET: Xây dựng AI Chatbot tư vấn món ăn dựa trên khẩu vị khách (`POST /ai/chat`).
  * Xây dựng AI Analytics (`POST /ai/analytics`): Chuyển câu hỏi tiếng Việt của Admin thành dữ liệu thống kê.
* **BE2:**
  * Xây dựng AI Combo Suggest: Phân tích tần suất món mua cùng nhau trong đơn hàng.
  * Xây dựng AI Churn Prediction: Phân tích khoảng cách ngày ghé của khách để cảnh báo nguy cơ rời bỏ.
  * Viết Service xuất báo cáo ra file Excel / PDF.
* **FE1:**
  * Dựng giao diện AI Chatbot Widget trên QR Order Menu.
  * Tối ưu PWA: Cấu hình Service Worker, Caching Menu để xem khi mất mạng tạm thời.
  * Polish toàn bộ hiệu ứng chuyển trang, Skeleton loading, Micro-animations cho QR Order.
* **FE2:**
  * Dựng giao diện AI Analytics Dashboard cho Admin (Ô hỏi đáp thông minh + hiển thị đồ thị).
  * Dựng trang Danh sách Khách hàng có nguy cơ Churn.
  * Tối ưu giao diện Responsive cho Tablet và Mobile.

---

### 🟢 SPRINT 7 (Tuần 13–14): KIỂM THỬ TOÀN DIỆN & FIX BUG (TESTING & UAT)
> **Mục tiêu:** Đảm bảo hệ thống đạt độ ổn định tối đa, zero bug nghiêm trọng trước khi deploy.

* **Cả Team:**
  * **Tuần 13 - Kiểm thử Chúng (Cross-Testing):**
    * FE1 & FE2 test toàn bộ API của BE.
    * BE1 & BE2 test trải nghiệm người dùng trên các màn hình FE.
  * **Tuần 14 - UAT & Chuẩn bị dữ liệu Demo:**
    * Chạy thử nghiệm các Kịch bản vận hành thực tế (100 đơn hàng mẫu, 3 chi nhánh, 20 tài khoản nhân viên).
    * Test hiệu năng SignalR khi có 50 kết nối đồng thời.
    * Fix triệt để các lỗi đơ, giật lag, sai lệch dữ liệu két tiền hoặc tồn kho.

---

### 🟢 SPRINT 8 (Tuần 15–16): DEPLOYMENT, BÁO CÁO & BẢO VỆ ĐỒ ÁN
> **Mục tiêu:** Hệ thống live trên Internet, hoàn thiện Báo cáo Đồ án, Slide và Video Demo.

* **BE1 & BE2:**
  * Deploy hệ thống lên VPS Server sử dụng Docker Compose (PostgreSQL, Redis, .NET Web API).
  * Cấu hình Nginx Reverse Proxy, Tên miền (Domain) và SSL Certbot (HTTPS).
  * Khởi tạo Seed Data sản phẩm chính thức cho buổi Demo.
* **FE1 & FE2:**
  * Deploy Frontend Next.js lên Vercel hoặc VPS.
  * Quay Video Demo giới thiệu trọn vẹn luồng hệ thống (Khách → Bếp → NV → QL → Admin).
* **Cả Team:**
  * Viết Báo cáo Đồ án Tốt nghiệp (Chương 1 đến 5 theo mẫu nhà trường).
  * Thiết kế Slide thuyết trình chuyên nghiệp.
  * Tổng duyệt (Rehearsal) kịch bản bảo vệ trước Hội đồng 2-3 lần.

---

## 🛠️ PHẦN 4: THỦ TỤC VÀ QUY TẮC LÀM VIỆC NHÓM

1. **Họp nhóm định kỳ (Weekly Sync):** Họp 20 phút vào tối Chủ Nhật hàng tuần để review checklist của Sprint và gỡ vướng (unblock).
2. **Quy tắc Code & PR:**
   * Không commit trực tiếp vào `main` hay `develop`.
   * Tạo Pull Request từ branch cá nhân vào `develop`, gán ít nhất 1 bạn cùng team (FE review FE, BE review BE) duyệt trước khi Merge.
3. **Nguyên tắc "Mock First" cho Frontend:**
   * Trong lúc chờ Backend viết API ở các Sprint 2-3, Frontend viết giao diện với dữ liệu Mock (Data giả) trước, khi BE xong API chỉ cần thay URL là chạy ngay, **không ngồi chờ nhau**.
