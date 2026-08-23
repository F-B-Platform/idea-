# 🗺️ LỘ TRÌNH TRIỂN KHAI DỰ ÁN 16 TUẦN (8 SPRINTS) — SMART F&B OS

> **Dự án:** Smart F&B Operating System (Smart F&B OS) — Nền tảng Quản lý & Vận hành Quán Cà phê Thông minh  
> **Quy mô Nhân sự:** 4 Thành viên Capstone (2 Backend Developers + 2 Frontend Developers)  
> **Thời gian Thực hiện:** 16 Tuần (8 Sprints — 2 tuần/sprint)  
> **Tech Stack Chuẩn:**  
> • **Backend:** .NET 8 (C#) Clean Architecture + EF Core 8 + MediatR + SignalR + FluentValidation  
> • **Frontend:** Next.js 14 App Router (TypeScript) + Tailwind CSS + Zustand + TanStack Query  
> • **Cơ sở dữ liệu & Cache:** PostgreSQL 16 + Redis 7  
> • **Hạ tầng:** Docker Compose + Nginx Reverse Proxy  
> • **Trí tuệ Nhân tạo (MVP):** AI-1 RAG Recommendation Chatbot (Google Gemini API) + AI-2 Smart Combo (Apriori Engine)  

---

## 📑 MỤC LỤC

1. [CƠ CẤU PHÂN CÔNG VAI TRÒ NHÓM 4 THÀNH VIÊN](#1-cơ-cấu-phân-công-vai-trò-nhóm-4-thành-viên)
2. [5 NGUYÊN TẮC BẢN LỀ TRONG QUY TRÌNH PHÁT TRIỂN](#2-5-nguyên-tắc-bản-lề-trong-quy-trình-phát-triển)
3. [MA TRẬN TIẾN ĐỘ 8 SPRINTS THEO VAI TRÒ](#3-ma-trận-tiến-độ-8-sprints-theo-vai-trò)
4. [CHI TIẾT KẾ HOẠCH TỪNG SPRINT (SPRINT 1 ĐẾN SPRINT 8)](#4-chi-tiết-kế-hoạch-từng-sprint-sprint-1-đến-sprint-8)
   - [Sprint 1 (Tuần 1–2): Khởi Tạo Kiến Trúc & Thiết Kế Hợp Đồng Dữ Liệu](#-sprint-1-tuần-12-khởi-tạo-kiến-trúc--thiết-kế-hợp-đồng-dữ-liệu)
   - [Sprint 2 (Tuần 3–4): Xây Dựng Core Services & Khung Giao Diện Monorepo](#-sprint-2-tuần-34-xây-dựng-core-services--khung-giao-diện-monorepo)
   - [Sprint 3 (Tuần 5–6): Luồng Dine-in Trả Trước & Web KDS Real-time](#-sprint-3-tuần-56-luồng-dine-in-trả-trước--web-kds-real-time)
   - [Sprint 4 (Tuần 7–8): Quầy Thu Ngân Takeaway & Tích Ly CRM Tự Động](#-sprint-4-tuần-78-quầy-thu-ngân-takeaway--tích-ly-crm-tự-động)
   - [Sprint 5 (Tuần 9–10): Luồng Đặt Hàng Giao Tận Nơi QR Delivery](#-sprint-5-tuần-910-luồng-đặt-hàng-giao-tận-nơi-qr-delivery)
   - [Sprint 6 (Tuần 11–12): Chấm Công Khóa WiFi & Hợp Nhất Web Portal](#-sprint-6-tuần-1112-chấm-công-khóa-wifi--hợp-nhất-web-portal)
   - [Sprint 7 (Tuần 13–14): Tích Hợp Module AI & Đóng Gói Nghiên Cứu](#-sprint-7-tuần-1314-tích-hợp-module-ai--đóng-gói-nghiên-cứu)
   - [Sprint 8 (Tuần 15–16): Kiểm Thử UAT Toàn Diện, Docker Deploy & Bảo Vệ Đồ Án](#-sprint-8-tuần-1516-kiểm-thử-uat-toàn-diện-docker-deploy--bảo-vệ-đồ-án)
5. [KẾ HOẠCH QUẢN TRỊ RỦI RO & DỰ PHÒNG KỸ THUẬT](#5-kế-hoạch-quản-trị-rủi-ro--dự-phòng-kỹ-thuật)
6. [QUY CHUẨN ĐÁNH GIÁ NGHIỆM THU TỪNG GIAI ĐOẠN](#6-quy-chuẩn-đánh-giá-nghiệm-thu-từng-giai-đoạn)

---

## 1. CƠ CẤU PHÂN CÔNG VAI TRÒ NHÓM 4 THÀNH VIÊN

Hệ thống phân rã trách nhiệm rõ ràng giữa 4 kỹ sư, bảo đảm tính độc lập module và khả năng kiểm thử chéo:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          CƠ CẤU ĐỘI NGŨ 4 KỸ SƯ CAPSTONE                               │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│         BACKEND TEAM (2 KỸ SƯ)            │          FRONTEND TEAM (2 KỸ SƯ)           │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│  👨‍💻 BE 1 (Backend Lead & Core Architect)   │  🎨 FE 1 (Frontend Lead & Customer UX)     │
│  • Thiết kế Clean Architecture & CQRS     │  • Khởi tạo Monorepo Next.js 14 App Router │
│  • Order Engine: Dine-in, Delivery, POS   │  • Xây dựng Design System & Shared UI      │
│  • Tích hợp VietQR Gateway & Webhooks     │  • Customer PWA: Dine-in & QR Delivery     │
│  • Hạ tầng SignalR Hubs thời gian thực    │  • Tích hợp AI Chatbot Widget & Cart Combo │
│  • Tích hợp AI-1 Gemini RAG Chatbot API   │  • PWA Service Worker & Real-time Client   │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│  👨‍💻 BE 2 (Data, Operations & AI Engine)    │  💻 FE 2 (Internal Operations & Dashboard) │
│  • PostgreSQL EF Core Schema & Migrations │  • Staff Web POS Quầy (Takeaway, CRM)      │
│  • Branch WiFi Config & WiFi Check-in API │  • Web KDS Màn hình Bếp (Kitchen Kanban)   │
│  • Phone CRM & Loyalty 10 Ly Tặng 1       │  • WiFi Attendance Portal & Shift Check-in │
│  • Quản lý Kho, Nguyên liệu & Đối soát Ca │  • Manager Table Map & Staff Alert System  │
│  • Tích hợp AI-2 Apriori Combo Engine     │  • Admin Dashboard & Business Analytics UI │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

---

## 2. 5 NGUYÊN TẮC BẢN LỀ TRONG QUY TRÌNH PHÁT TRIỂN

Toàn bộ 8 Sprints phải tuân thủ nghiêm ngặt 5 thay đổi nghiệp vụ cốt lõi đã được chốt:

1. **Dine-in Thanh Toán Trước (100% Pre-payment):** Khách quét QR bàn → Chọn món → Bắt buộc thanh toán VietQR thành công qua Webhook/Polling (`PendingPayment` → `Paid` → `Confirmed`) → Bếp KDS mới nhận đơn. Tuyệt đối không phát đơn vào KDS khi chưa thanh toán.
2. **QR Delivery Độc Lập:** Phân hệ đặt giao tận nhà riêng biệt qua mã QR Delivery / Link PWA. Bắt buộc nhập Tên, SĐT, Địa chỉ giao hàng, tự động tính **phí ship cố định 20.000 VNĐ**, thanh toán 100% VietQR trước (không hỗ trợ COD).
3. **Takeaway Web POS Tại Quầy (Không dùng QR):** Bỏ hoàn toàn mã QR Takeaway cho khách quét. Nhân viên thu ngân thao tác trên giao diện Web POS riêng: Tra cứu SĐT khách CRM, hiển thị cơ chế Loyalty đơn giản hóa (**10 ly = tặng 1 ly miễn phí**), tạo đơn và thu tiền sau (Tiền mặt hoặc VietQR).
4. **Chấm Công Khóa WiFi (WiFi-Locked):** Loại bỏ hoàn toàn GPS 50m và mã QR động xoay 30 giây. Nhân viên kết nối WiFi quán, hệ thống kiểm tra IP Subnet / BSSID khớp với cấu hình chi nhánh + xác thực Mã nhân viên để ghi nhận vào/ra ca.
5. **Hợp Nhất Web Responsive (Loại bỏ Staff Mobile App):** Không phát triển ứng dụng di động riêng cho nhân viên. Toàn bộ tính năng phục vụ, KDS bếp, gọi bàn, sơ đồ bàn và chấm công được tích hợp trong giao diện Web Responsive chạy trên máy tính, tablet hoặc điện thoại.

---

## 3. MA TRẬN TIẾN ĐỘ 8 SPRINTS THEO VAI TRÒ

| Sprint | Thời Gian | Trọng Tâm Nghiệp Vụ | BE 1 (Lead BE) | BE 2 (Data & AI) | FE 1 (Lead FE) | FE 2 (Internal UI) |
|:---:|:---:|---|---|---|---|---|
| **S1** | Tuần 1–2 | Architecture & Setup | Clean Arch, Docker, API Spec | EF Core, 28 Tables, Seed Data | Next.js Monorepo, UI Kit | Admin Layout, Auth Guard |
| **S2** | Tuần 3–4 | Core Services & Menu | Auth JWT, RBAC, Product API | Branch WiFi Config, Table API | Customer Menu PWA, Cart Store | Admin Menu CRUD, Branch UI |
| **S3** | Tuần 5–6 | **Dine-in Pre-pay & KDS** | Dine-in API, VietQR, SignalR | Inventory Deduction, CashShift | Dine-in PWA, VietQR Modal | Web KDS Bếp Kanban Real-time |
| **S4** | Tuần 7–8 | **Takeaway POS & Loyalty** | Takeaway API, Cash Calculator | Phone CRM, 10-Cup Loyalty | Order Tracking UI, Toasts | Staff Takeaway POS, Loyalty UI |
| **S5** | Tuần 9–10 | **QR Delivery Flow** | Delivery API, 20k Ship Fee | Dispatch Engine, Packaging Hub | Customer Delivery PWA Flow | KDS Packaging & Dispatch UI |
| **S6** | Tuần 11–12 | **WiFi Attendance & Portal** | Table Map API, Call Hub | WiFi Check-in API, Shift Rpt | Call Staff Button, Reviews | WiFi Attendance, Table Map UI |
| **S7** | Tuần 13–14 | **AI Modules (AI-1 & AI-2)** | AI-1 Gemini RAG Chatbot API | AI-2 Apriori Combo Engine | Chatbot Widget, Combo Pop-up | Manager AI Reports Preview |
| **S8** | Tuần 15–16 | **UAT, Deploy & Defense** | Production Docker, Nginx SSL | Database Seeding, Data Load | E2E Testing Customer Flows | E2E Testing Staff/Admin, Demo |

---

## 4. CHI TIẾT KẾ HOẠCH TỪNG SPRINT (SPRINT 1 ĐẾN SPRINT 8)

---

### 🟢 SPRINT 1 (Tuần 1–2): KHỞI TẠO KIẾN TRÚC & THIẾT KẾ HỢP ĐỒNG DỮ LIỆU

> **Mục tiêu Sprint:** Thiết lập toàn bộ nền tảng kỹ thuật, đóng băng hợp đồng API, cấu hình Database Schema với đầy đủ 28 thực thể phục vụ 5 thay đổi nghiệp vụ, và khởi tạo dự án monorepo cho cả Backend lẫn Frontend.

```
                     ┌────────────────────────────────────────────────────────┐
                     │                 SPRINT 1 DELIVERABLES                  │
                     ├────────────────────────────┬───────────────────────────┤
                     │  Backend (.NET 8 Clean)    │  Frontend (Next.js 14)    │
                     │  • Solution 4 Projects     │  • Monorepo 4 Groups      │
                     │  • Docker Postgres & Redis │  • Design System Tokens   │
                     │  • EF Core Migration Init  │  • Common Components Kit  │
                     └────────────────────────────┴───────────────────────────┘
```

#### Phân công Công việc Chi tiết:
* **BE 1 (Backend Lead):**
  * Khởi tạo .NET 8 Solution theo Clean Architecture: `SmartFB.Domain`, `SmartFB.Application`, `SmartFB.Infrastructure`, `SmartFB.API`, `SmartFB.Tests`.
  * Thiết lập `docker-compose.yml` cho PostgreSQL 16 và Redis 7, tạo file cấu hình `.env.example`.
  * Viết tài liệu API Specification Envelope chuẩn RFC 7807 (`ProblemDetails`) và Swagger OpenAPI 3.1 configuration.
  * Cài đặt các thư viện lõi: `MediatR`, `FluentValidation.AspNetCore`, `Serilog`, `Microsoft.AspNetCore.Authentication.JwtBearer`.
* **BE 2 (Backend Dev):**
  * Định nghĩa toàn bộ thực thể C# trong `SmartFB.Domain` phản ánh đúng các trường mới:
    * `Order`: Thêm `OrderType` (`DineIn`, `TakeAway`, `Delivery`), `DeliveryAddress`, `DeliveryFee`, `RecipientPhone`, `RecipientName`, `PaidAt`, `ConfirmedAt`.
    * `Branch`: Thêm `WifiSsid`, `WifiBssid`, `AllowedIpSubnet`.
    * `Customer`: Thêm `CupBalance`, `TotalCupsEarned`, `TotalFreeCupsRedeemed`.
    * `Attendance`: Xóa GPS, thêm `ConnectedWifiSsid`, `ConnectedWifiBssid`, `ClientIpAddress`.
  * Cấu hình EF Core Fluent API mappings và quan hệ Foreign Keys trong `SmartFB.Infrastructure`.
  * Tạo bản Migration khởi tạo `Initial_Schema_v2` và viết script Seed Data chuẩn cho 3 chi nhánh, 20 bàn, menu 30 món.
* **FE 1 (Frontend Lead):**
  * Khởi tạo dự án Next.js 14 (App Router) với TypeScript, Tailwind CSS và ESLint/Prettier.
  * Cấu hình 4 Route Groups chính: `(customer)`, `(kds)`, `(staff)` / `(portal)`, `(admin)`.
  * Xây dựng bộ Design System Tokens (Bảng màu Primary Amber `#D97706`, Background `#FFFBEB`, Dark KDS `#0F172A`).
  * Xây dựng thư viện thành phần dùng chung (Atomic UI Kit): `Button`, `Input`, `Card`, `Modal`, `Badge`, `Toast`, `SkeletonLoader`.
* **FE 2 (Frontend Dev):**
  * Thiết lập Layout cơ sở cho Admin Dashboard và Staff Portal (Sidebar, Header responsive, Breadcrumb, Notification badge).
  * Dựng trang Login xác thực cho nhân viên và quản trị viên (`/admin/login`, `/staff/login`).
  * Cấu hình Zustand Auth Store lưu trữ JWT Access Token, Refresh Token và phân quyền vai trò (Role Guards).

#### Sản phẩm Bàn giao (Deliverables):
1. Solution .NET 8 build thành công với 0 cảnh báo/lỗi, swagger hiển thị tại `http://localhost:5000/swagger`.
2. PostgreSQL 16 khởi tạo thành công 28 bảng có đầy đủ ràng buộc dữ liệu thông qua lệnh `dotnet ef database update`.
3. Next.js 14 chạy mượt mà tại `http://localhost:3000`, hiển thị đúng giao diện đăng nhập và layout mẫu.

---

### 🟢 SPRINT 2 (Tuần 3–4): XÂY DỰNG CORE SERVICES & KHUNG GIAO DIỆN MONOREPO

> **Mục tiêu Sprint:** Hoàn thiện hạ tầng Xác thực/Phân quyền (Auth/RBAC), các dịch vụ CRUD Menu, Danh mục, Cấu hình Chi nhánh WiFi và kết nối dữ liệu Menu tĩnh lên Customer PWA.

#### Phân công Công việc Chi tiết:
* **BE 1 (Backend Lead):**
  * Xây dựng Module Authentication: `POST /api/v1/auth/login`, `POST /api/v1/auth/refresh-token`, `POST /api/v1/auth/logout`.
  * Thiết lập JWT Token Generator với Claims (`UserId`, `Role`, `BranchId`, `Permissions`).
  * Xây dựng CRUD API cho Danh mục và Món ăn: `GET /api/v1/categories`, `GET /api/v1/products`, `POST /api/v1/products`, `PUT /api/v1/products/{id}`, `PATCH /api/v1/products/{id}/toggle-status`.
  * Cài đặt Caching Redis cho Menu công khai để tối ưu tốc độ phản hồi (Cache-aside pattern, TTL 30 phút).
* **BE 2 (Backend Dev):**
  * Xây dựng CRUD API cho Chi nhánh: `GET /api/v1/branches`, `POST /api/v1/branches`, `PUT /api/v1/branches/{id}/wifi-config` (quản lý SSID, BSSID, Subnet IP).
  * Xây dựng CRUD API cho Bàn và Mã QR: `GET /api/v1/tables`, `POST /api/v1/tables`, `POST /api/v1/tables/generate-qr`.
  * Viết Service quản lý Biến thể (Size M/L) và Toppings đi kèm từng món đồ uống.
  * Viết Unit Tests xUnit kiểm thử các Command/Query của Product và Branch.
* **FE 1 (Frontend Lead):**
  * Dựng trang Menu QR Khách hàng (`/customer/menu`): Tab danh mục trượt ngang, danh sách món dạng thẻ có ảnh và giá tiền.
  * Dựng Modal Tùy chỉnh Món (Item Detail Modal): Chọn Size (M/L), thanh gạt mức Đường (0%, 30%, 50%, 70%, 100%), mức Đá (0%, 50%, 100%, Nóng), chọn Topping kèm giá cộng thêm, nhập Ghi chú đặc biệt.
  * Xây dựng Zustand Cart Store: Thêm món, sửa số lượng, tính toán tạm tính, lưu giỏ hàng vào `localStorage`.
* **FE 2 (Frontend Dev):**
  * Kết nối trang Login với API Backend thật, xử lý lưu Token và tự động điều hướng theo Role (`Admin` → `/admin/dashboard`, `Cashier`/`Staff` → `/staff/pos`, `Barista` → `/kds`).
  * Dựng trang Admin Quản lý Thực đơn (`/admin/menu`): Bảng danh sách món, thanh tìm kiếm, bộ lọc danh mục, nút bật/tắt bán nhanh.
  * Dựng Form Thêm/Sửa Món ăn (`/admin/menu/[id]`): Nhập tên, giá, tải ảnh, cấu hình định lượng và công thức pha chế.
  * Dựng trang Cấu hình Chi nhánh & WiFi (`/admin/branches`): Nhập tên quán, địa chỉ, SSID, BSSID và dải IP mạng cho phép chấm công.

#### Sản phẩm Bàn giao (Deliverables):
1. Hệ thống Auth JWT hoạt động chuẩn xác với 4 vai trò (`Admin`, `StoreManager`, `Staff`, `Customer`).
2. Khách hàng quét mã QR bàn truy cập được Menu trực tiếp từ Database qua API công khai có Redis Cache.
3. Quản trị viên thêm, sửa, xóa món ăn và cấu hình thông tin WiFi chi nhánh thành công trên giao diện Admin.

---

### 🟢 SPRINT 3 (Tuần 5–6): LUỒNG DINE-IN TRẢ TRƯỚC & WEB KDS REAL-TIME

> **Mục tiêu Sprint:** Hiện thực hóa **Thay Đổi Nghiệp Vụ 1 (Dine-in Pre-Payment)**: Khách quét QR bàn → Đặt món → Bắt buộc thanh toán VietQR trước → Webhook/Polling xác nhận → SignalR đẩy đơn xuống màn hình Bếp KDS thời gian thực.

```
  ┌─────────────────┐       VietQR Payment Success       ┌────────┐      Auto Broadcast Event       ┌───────────┐
  │ PendingPayment  │ ─────────────────────────────────► │  Paid  │ ──────────────────────────────► │ Confirmed │
  └─────────────────┘   (Webhook / Polling Callback)     └────────┘       (SignalR KitchenHub)      └─────┬─────┘
                                                                                                          │
                                                                 Barista Click "Bắt đầu pha chế"          ▼
  ┌─────────────────┐       Barista Click "Hoàn thành"   ┌────────┐                                 ┌───────────┐
  │      Ready      │ ◄───────────────────────────────── │ Serving│ ◄────────────────────────────── │ Preparing │
  └─────────────────┘                                    └────────┘                                 └───────────┘
```

#### Phân công Công việc Chi tiết:
* **BE 1 (Backend Lead):**
  * Xây dựng API Tạo đơn Dine-in: `POST /api/v1/orders/dine-in` (Nhận `tableId`, danh sách items, ghi chú; sinh `orderNumber`, tạo bản ghi trạng thái `PendingPayment`, TTL 10 phút).
  * Tích hợp Dịch vụ Thanh toán VietQR: Sinh mã QR động chuẩn VietQR NAPAS 247 kèm cú pháp chuyển khoản duy nhất (ví dụ: `ORD0042`).
  * Xây dựng Endpoint Webhook Thanh toán: `POST /api/v1/payments/webhook/vietqr` (Kiểm tra chữ ký HMAC-SHA256, đối soát số tiền và nội dung CK, cập nhật đơn sang `Paid` và `Confirmed`).
  * Cấu hình SignalR Hubs:
    * `PaymentHub`: Gửi sự kiện `PaymentReceived` về PWA của khách ngay khi tiền vào tài khoản.
    * `KitchenHub`: Gửi sự kiện `NewOrderTicket` xuống Web KDS Bếp chỉ sau khi đơn đã `Confirmed`.
* **BE 2 (Backend Dev):**
  * Xây dựng Logic Tự động Trừ Tồn Kho Nguyên Liệu: Khi đơn chuyển sang `Confirmed`, tính toán định lượng theo công thức (Recipe) và trừ `InventoryStock`.
  * Xây dựng API Quản lý Ca Tiền Két: `POST /api/v1/cash-shifts/open` (Khai báo tiền đầu ca), `POST /api/v1/cash-shifts/close` (Kết toán doanh thu và tiền thực đếm).
  * Xây dựng Background Service (Quartz.NET/HostedService) tự động hủy đơn `PendingPayment` quá hạn 10 phút (`Cancelled`).
* **FE 1 (Frontend Lead):**
  * Dựng trang Checkout Dine-in (`/customer/checkout`): Xem lại giỏ hàng, áp mã giảm giá, kiểm tra số bàn hiện tại.
  * Dựng Modal Thanh Toán VietQR Chờ Bếp: Hiển thị ảnh QR VietQR, thông tin tài khoản, số tiền chính xác, đồng hồ đếm ngược 10:00 và nút sao chép thông tin.
  * Tích hợp SignalR Client lắng nghe `PaymentReceived`: Tự động đóng modal QR và chuyển hướng khách sang màn hình Tracking Trạng Thái Đơn (`/customer/order-status/[id]`).
  * Dựng màn hình Tracking Tiến Trình: Hiển thị các bước trực quan (*Đã thanh toán* → *Bếp đang pha chế* → *Món đã sẵn sàng*).
* **FE 2 (Frontend Dev):**
  * Dựng Màn hình KDS Bếp Full-screen (`/kds`): Bảng Kanban chia 3 cột (*Chờ làm*, *Đang pha chế*, *Đã hoàn thành*).
  * Thiết kế Card Đơn Hàng Bếp: Hiển thị số bàn, số thứ tự đơn, thời gian chờ (đổi màu Xanh $\le 5$p, Vàng 5–10p, Đỏ $>10$p), chi tiết từng ly (Size, Đường, Đá, Topping, Recipe).
  * Tích hợp SignalR Client vào KDS: Phát âm thanh chuông báo 🔔 và hiển thị card mới ngay lập tức khi nhận sự kiện `NewOrderTicket`.
  * Nút tương tác chuyển trạng thái trên KDS: Bấm "Bắt đầu pha chế" (`PATCH /api/v1/kds/orders/{id}/preparing`) và "Hoàn thành món" (`PATCH /api/v1/kds/orders/{id}/ready`).

#### Sản phẩm Bàn giao (Deliverables):
1. Luồng Dine-in khép kín: Khách quét QR Bàn 5 → Chọn món → Quét VietQR thanh toán → Webhook kích hoạt → KDS Bếp rung chuông hiện đơn tức thì.
2. Màn hình KDS cho phép Barista đổi trạng thái pha chế và SignalR cập nhật ngay lập tức lên màn hình điện thoại của khách hàng.
3. Không một đơn hàng nào xuất hiện trên KDS nếu chưa có xác nhận thanh toán thành công.

---

### 🟢 SPRINT 4 (Tuần 7–8): QUẦY THU NGÂN TAKEAWAY & TÍCH LY CRM TỰ ĐỘNG

> **Mục tiêu Sprint:** Hiện thực hóa **Thay Đổi Nghiệp Vụ 3 (Takeaway Staff Web POS & Simplified Loyalty)**: Nhân viên quầy thao tác trên Web POS, tra cứu SĐT khách hàng, quản lý chương trình tích ly (10 ly = tặng 1 ly miễn phí), tạo đơn mang về và thu tiền sau (Tiền mặt / VietQR).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ SMART F&B POS — QUẦY THU NGÂN CHI NHÁNH QUẬN 1                           [ 10:45:12 ] │
├─────────────────────────────────────────────┬──────────────────────────────────────────┤
│  🔍 TÌM KHÁCH: [ 0909123456              ]  │  GIỎ HÀNG: ĐƠN MANG VỀ (TAKEAWAY)        │
│  👤 Khách hàng: NGUYỄN HOÀNG NAM            │  1. Cà phê Muối (Size M)       35.000 đ  │
│  🏆 Tích lũy: [██████████] 10/10 LY        │  2. Cà phê Muối (Size M)       35.000 đ  │
│  🎁 [  BẤM ĐỔI 1 LY MIỄN PHÍ (-35.000đ)  ]  │  Ưu đãi 10 Ly tặng 1:         -35.000 đ  │
│                                             │  KHÁCH CẦN TRẢ:                35.000 đ  │
│                                             │  Tiền khách đưa: [ 100.000 ]             │
│                                             │  Tiền thối lại:   65.000 đ               │
│                                             │  [   HỦY   ]    [  IN BILL & GỬI BẾP  ]  │
└─────────────────────────────────────────────┴──────────────────────────────────────────┘
```

#### Phân công Công việc Chi tiết:
* **BE 1 (Backend Lead):**
  * Xây dựng API Tạo đơn Takeaway tại Quầy: `POST /api/v1/pos/orders/takeaway` (Nhận thông tin món, hình thức thanh toán `Cash` hoặc `VietQR`, cờ `redeemFreeCup`).
  * Xây dựng Logic Thanh toán Tiền mặt: Tính toán số tiền khách đưa (`cashGiven`), số tiền thối lại (`changeReturned`), ghi nhận người thu ngân xác nhận (`ConfirmedBy`).
  * Tích hợp luồng in hóa đơn tạm tính và phiếu lấy nước (Order Ticket #TK-xxxx) gửi xuống máy in nhiệt hoặc hiển thị pop-up in trình duyệt.
  * Tối ưu hóa SignalR KitchenHub: Phân loại đơn Takeaway trên KDS với nhãn riêng `[MANG VỀ]` để Barista dùng ly nắp mang đi.
* **BE 2 (Backend Dev):**
  * Xây dựng API Tra cứu & Quản lý CRM Khách hàng: `GET /api/v1/pos/customers/lookup?phone=0909123456`.
  * Xây dựng Logic Tích Ly Đơn Giản Hóa:
    * Khách mua $N$ ly đồ uống $\rightarrow$ Cộng $N$ ly vào `CupBalance`.
    * Nếu `CupBalance >= 10`: Cho phép đổi 1 ly miễn phí (giảm trừ giá trị ly tiêu chuẩn 35.000 VNĐ) và trừ 10 ly trong quỹ tích lũy (`CupBalance = CupBalance - 10`).
  * Lưu vết lịch sử giao dịch điểm ly vào bảng `LoyaltyCupTransactions` (`CustomerId`, `OrderId`, `CupsCount`, `BalanceAfter`).
  * Viết API Báo Cáo Doanh Thu Quầy: Thống kê doanh thu theo phương thức (Tiền mặt vs VietQR), tổng số ly đã tặng trong ca.
* **FE 1 (Frontend Lead):**
  * Tối ưu hóa trải nghiệm trên Customer PWA: Thêm hiệu ứng Skeleton loading khi tải dữ liệu menu, cải thiện tốc độ render danh sách món.
  * Bổ sung Toast thông báo trạng thái đơn hàng thời gian thực mượt mà cho khách hàng.
  * Hỗ trợ lưu trữ số điện thoại khách hàng trên PWA để tự động điền khi đặt hàng lần sau.
* **FE 2 (Frontend Dev):**
  * Dựng Giao diện Staff Web POS Quầy (`/staff/pos`):
    * Thanh tìm kiếm số điện thoại khách hàng thông minh (tự động gợi ý, hiển thị tên và hạng thành viên).
    * Thanh tiến trình tích lũy ly trực quan (Visual Cup Meter `x/10 ly`) kèm nút bấm nổi bật `[Áp dụng Đổi 1 Ly Miễn Phí]`.
    * Bảng chọn món nhanh dạng lưới (Grid View) phân theo tab Cà phê, Trà, Bánh.
    * Khung giỏ hàng bên phải hỗ trợ tùy chỉnh nhanh Size/Đường/Đá.
    * Bộ tính tiền mặt thông minh: Các nút chọn nhanh mệnh giá (50k, 100k, 200k, 500k) và hiển thị số tiền thối lại khổ lớn chống nhầm lẫn.
  * Dựng giao diện Modal hiển thị mã VietQR tại quầy cho khách quét thanh toán nếu chọn phương thức chuyển khoản.

#### Sản phẩm Bàn giao (Deliverables):
1. Giao diện Staff Web POS hoàn chỉnh, nhân viên gõ SĐT khách là hiện ngay tiến trình tích ly (`7/10` hoặc `10/10 ĐỦ ĐIỀU KIỆN`).
2. Tạo đơn mang về thành công, tự động giảm trừ tiền ly miễn phí khi tích đủ 10 ly, tính tiền thối chuẩn xác.
3. KDS Bếp nhận đúng ticket đơn mang về kèm nhãn phân biệt rõ ràng.

---

### 🟢 SPRINT 5 (Tuần 9–10): LUỒNG ĐẶT HÀNG GIAO TẬN NƠI QR DELIVERY

> **Mục tiêu Sprint:** Hiện thực hóa **Thay Đổi Nghiệp Vụ 2 (QR Delivery Flow)**: Khách hàng quét mã QR Delivery dán trên poster/standee hoặc vào link web → Nhập SĐT, Tên và Địa chỉ giao hàng bắt buộc → Tự động cộng **Phí ship cố định 20.000 VNĐ** → Thanh toán 100% VietQR trước → Đơn chuyển sang bếp đóng gói và điều phối giao hàng.

```
┌────────────────────────────────────────────────────────┐
│  SMART F&B — ĐẶT GIAO TẬN NƠI              [ 10:15 ]   │
├────────────────────────────────────────────────────────┤
│  📍 THÔNG TIN GIAO HÀNG                                │
│  Họ và tên: [ Chị Mai Hương                          ] │
│  Số điện thoại: [ 0987654321                         ] │
│  Địa chỉ: [ Tòa nhà Bitexco, 2 Hải Triều, Q1, TP.HCM ] │
│  Ghi chú: [ Giao sảnh lễ tân tầng 1                  ] │
├────────────────────────────────────────────────────────┤
│  🛒 GIỎ HÀNG: 2x Trà Đào Cam Sả (Size L)      70.000 đ │
│  Phí giao hàng (Cố định):                     20.000 đ │
│  ────────────────────────────────────────────────────  │
│  TỔNG THANH TOÁN (VIETQR 100%):               90.000 đ │
│  (Quán không áp dụng hình thức thu tiền mặt COD)       │
│                                                        │
│  [  TIẾP TỤC THANH TOÁN VIETQR (90.000 Đ)  ]           │
└────────────────────────────────────────────────────────┘
```

#### Phân công Công việc Chi tiết:
* **BE 1 (Backend Lead):**
  * Xây dựng API Tạo đơn Delivery: `POST /api/v1/orders/delivery`.
  * Ràng buộc nghiệp vụ (Validation Rules):
    * Bắt buộc có `RecipientName`, `RecipientPhone` (đúng định dạng số di động VN), `DeliveryAddress` (tối thiểu 10 ký tự).
    * `OrderType = Delivery`, `TableId = NULL`.
    * Tự động gán trường `DeliveryFee = 20000` VNĐ vào tổng tiền đơn hàng.
  * Tích hợp luồng VietQR Delivery: Sinh mã QR thanh toán tổng số tiền = Tiền món + 20.000 VNĐ phí ship.
  * Cấu hình Webhook cập nhật đơn Delivery sang `Confirmed` và broadcast tới KDS Đóng gói.
* **BE 2 (Backend Dev):**
  * Xây dựng Service Điều phối Giao hàng Chi nhánh: Gán đơn giao hàng cho chi nhánh gần nhất hoặc chi nhánh được chọn.
  * Xây dựng API Quản lý Đơn Giao Hàng cho Manager: `GET /api/v1/delivery/orders`, `PATCH /api/v1/delivery/orders/{id}/assign-shipper`, `PATCH /api/v1/delivery/orders/{id}/dispatched`.
  * Viết tài liệu đánh dấu ranh giới kiến trúc: Tích hợp API đối tác vận chuyển thứ 3 (AhaMove, GrabExpress) và tính phí theo km động được quy hoạch vào phần "Scale Up / Future Work".
* **FE 1 (Frontend Lead):**
  * Dựng Luồng Giao diện QR Delivery PWA (`/customer/delivery`):
    * Màn hình chào mừng khi quét mã QR Delivery (Standee/Poster).
    * Form nhập thông tin người nhận trực quan: Họ tên, Số điện thoại, Địa chỉ chi tiết (Số nhà, Tên đường, Phường/Quận, Tỉnh/TP), Ghi chú giao hàng.
    * Khung hiển thị giỏ hàng kèm dòng tách biệt rõ ràng: **"Phí giao hàng (Cố định): 20.000 đ"**.
    * Cam kết thanh toán: Thông báo rõ ràng quán chỉ nhận chuyển khoản VietQR, không nhận tiền mặt COD để tránh rủi ro bùng hàng.
  * Dựng màn hình Thanh toán VietQR Delivery và Trang Theo Dõi Tiến Trình Đơn Giao Hàng (`/customer/delivery/tracking/[id]`) với các trạng thái: *Đã thanh toán* → *Đang pha chế & đóng gói* → *Đang giao hàng* → *Đã giao thành công*.
* **FE 2 (Frontend Dev):**
  * Dựng Giao diện Quản lý Đơn Delivery trên KDS và Staff Portal:
    * Card đơn giao hàng trên KDS có viền màu Tím nổi bật và nhãn `[GIAO HÀNG #DELxxxx]`.
    * Hiển thị đầy đủ Tên khách, SĐT và Địa chỉ giao hàng trên phiếu in dán miệng túi đồ uống.
    * Nút thao tác dành cho nhân viên: "Đã đóng gói xong" và "Đã bàn giao cho Shipper".

#### Sản phẩm Bàn giao (Deliverables):
1. Khách hàng quét mã QR Delivery trên poster, nhập địa chỉ, hệ thống tự động cộng đúng 20.000 VNĐ phí ship.
2. Thanh toán VietQR 100% thành công, đơn hàng lập tức chuyển xuống KDS bếp để pha chế và đóng gói dán nhãn giao hàng.
3. Khách hàng theo dõi được tiến trình giao hàng theo thời gian thực trên PWA.

---

### 🟢 SPRINT 6 (Tuần 11–12): CHẤM CÔNG KHÓA WIFI & HỢP NHẤT WEB PORTAL

> **Mục tiêu Sprint:** Hiện thực hóa **Thay Đổi Nghiệp Vụ 4 (WiFi-Locked Attendance)** và **Thay Đổi Nghiệp Vụ 5 (Elimination of Staff Mobile App)**: Xây dựng hệ thống chấm công xác thực qua mạng WiFi quán + Mã nhân viên (loại bỏ hoàn toàn GPS và QR xoay 30s), đồng thời hoàn thiện hệ thống Staff Web Portal hợp nhất (Sơ đồ bàn, Nhận chuông gọi phục vụ, Báo hết món).

#### Phân công Công việc Chi tiết:
* **BE 1 (Backend Lead):**
  * Xây dựng API và SignalR Hub cho Sơ đồ bàn & Gọi phục vụ:
    * `POST /api/v1/tables/{id}/call-staff` (Khách bấm chuông gọi hỗ trợ từ bàn).
    * `StaffHub`: Phát sự kiện `TableCallAlert` kèm âm thanh thông báo đến toàn bộ máy quầy/tablet nhân viên đang mở web portal.
    * `PATCH /api/v1/tables/{id}/status` (Cập nhật trạng thái bàn: Trống, Đang có khách, Đã đặt trước).
  * Xây dựng API Báo hết món nhanh (`86 List`): `PATCH /api/v1/products/{id}/out-of-stock` → Tự động ẩn món trên toàn bộ QR Menu của khách trong 1 giây.
* **BE 2 (Backend Dev):**
  * Xây dựng Thuật toán Xác thực Chấm Công Khóa WiFi:
    * API: `POST /api/v1/hrm/attendance/wifi-checkin`.
    * Logic kiểm tra: Đọc IP Client từ HttpContext (`X-Forwarded-For`) đối chiếu với `AllowedIpSubnet` của chi nhánh HOẶC kiểm tra thông tin `WifiBssid`/`WifiSsid` gửi lên từ client.
    * Xác thực `EmployeeCode` có đang trong lịch làm việc (Shift Schedule) hợp lệ hay không.
    * Nếu thỏa mãn cả 2 điều kiện $\rightarrow$ Ghi nhận bản ghi `Attendance` (Check-in / Check-out). Nếu sai mạng WiFi $\rightarrow$ Ném lỗi `403 Forbidden` kèm thông báo: "Bạn chưa kết nối đúng mạng WiFi của quán!".
  * Xây dựng API Báo cáo Chấm công & Bảng công tháng cho Quản lý cửa hàng.
* **FE 1 (Frontend Lead):**
  * Dựng Nút "Gọi nhân viên hỗ trợ" nổi bật trên Customer PWA: Cho phép khách chọn lý do (Cần lấy thêm khăn/đá, Cần hỗ trợ khác).
  * Dựng Modal Đánh giá Dịch vụ & Góp ý (`/customer/feedback`): Chọn số sao (1–5 sao), nhập nhận xét, cảnh báo nội bộ nếu đánh giá $\le 2$ sao.
  * Tối ưu PWA Service Worker: Caching tài nguyên tĩnh để app tải tức thì dưới 1 giây.
* **FE 2 (Frontend Dev):**
  * Dựng Màn hình Chấm Công Khóa WiFi Nhân Viên (`/staff/attendance`):
    * Giao diện kiểm tra trạng thái mạng: Hiển thị tên WiFi đang kết nối, biểu tượng sóng WiFi xanh/đỏ.
    * Nút Quét QR Chấm công chi nhánh + Ô nhập Mã số Nhân viên (PIN Code).
    * Hiển thị ca làm việc hôm nay, giờ vào ca thực tế và nút Bấm "Chấm công Ra ca".
  * Dựng Giao diện Staff Web Portal Hợp Nhất (`/staff/dashboard`):
    * Sơ đồ bàn trực quan theo tầng/khu vực: Đổi màu theo trạng thái (Xanh = Trống, Vàng = Đang dùng món, Đỏ = Đang có chuông gọi).
    * Thanh thông báo khẩn cấp (Alert Bar) trên đầu màn hình phát âm báo khi có bàn cần phục vụ.
    * Bảng gạt Báo hết món nhanh (Quick 86 Toggle) cho phép nhân viên quầy khóa món tạm thời khi hết nguyên liệu.

#### Sản phẩm Bàn giao (Deliverables):
1. Chấm công WiFi hoạt động chuẩn xác: Đứng tại quán bắt đúng WiFi thì chấm công thành công; dùng 4G hoặc WiFi ngoài bị từ chối ngay lập tức.
2. Staff Web Portal hợp nhất hoàn chỉnh trên trình duyệt web, không cần bất kỳ ứng dụng di động riêng nào.
3. Khách hàng bấm gọi bàn là quầy thu ngân và nhân viên nhận được thông báo âm thanh và pop-up tức thì.

---

### 🟢 SPRINT 7 (Tuần 13–14): TÍCH HỢP MODULE AI & ĐÓNG GÓI NGHIÊN CỨU

> **Mục tiêu Sprint:** Tích hợp 2 Module Trí Tuệ Nhân Tạo chính thức của đồ án: **AI-1 (Recommendation Chatbot sử dụng RAG trên nền Google Gemini API)** và **AI-2 (Smart Combo Engine sử dụng thuật toán Apriori/FP-Growth)**. Phân định rõ ràng 3 module còn lại (AI-3 NLQ Analytics, AI-4 Churn Prediction, AI-5 Demand Forecasting) thuộc phần "Scale Up / Future Work".

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              AI MODULES INTEGRATION SCOPE                              │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│     ACTIVE MVP AI (TRIỂN KHAI 100%)       │       SCALE-UP / FUTURE WORK (PHASE 2)     │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│  🤖 AI-1: RAG Menu Advisor Chatbot        │  📊 AI-3: NLQ Text-to-SQL Analytics        │
│  • Google Gemini 1.5 Flash API (C# SDK)   │  • Truy vấn ngôn ngữ tự nhiên thành SQL    │
│  • Khẩu vị khách hàng, dị ứng, thời tiết  │  • Đã thiết kế kiến trúc, triển khai sau   │
│  • RAG Knowledge Base đồ uống chi nhánh   │                                            │
│                                           │  🔮 AI-4: Customer Churn Prediction        │
│  🧋 AI-2: Smart Combo Recommender         │  • Dự báo nguy cơ khách rời bỏ (XGBoost)   │
│  • Thuật toán Apriori / FP-Growth (C#)    │                                            │
│  • Phân tích giỏ hàng khai phá luật kết hợp│  📈 AI-5: Menu Demand Forecasting          │
│  • Gợi ý combo bánh + nước tại Giỏ hàng   │  • Dự báo sức mua và lượng nguyên liệu     │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

#### Phân công Công việc Chi tiết:
* **BE 1 (Backend Lead):**
  * Xây dựng Module AI-1 Chatbot: `POST /api/v1/ai/chat`.
  * Tích hợp Google Gemini 1.5 Flash API thông qua REST Client .NET với cơ chế RAG (Retrieval-Augmented Generation):
    * Trích xuất danh mục sản phẩm, thành phần, độ ngọt, lượng calo và gợi ý kết hợp từ Database vào Context Prompt.
    * Tiếp nhận câu hỏi của khách hàng (ví dụ: *"Tôi đang buồn ngủ và thích vị béo, quán có món nào phù hợp?"* hoặc *"Tôi bị dị ứng sữa bò"*).
    * Trả về câu trả lời tự nhiên kèm danh sách Product IDs đề xuất có cấu trúc JSON (Structured Outputs).
  * Xây dựng cơ chế Giới hạn tần suất gọi API (Rate Limiting 10 req/phút/IP) và Caching câu hỏi tương tự qua Redis.
* **BE 2 (Backend Dev):**
  * Xây dựng Module AI-2 Smart Combo Engine: `POST /api/v1/ai/combos/suggest`.
  * Cài đặt Thuật toán Khai phá Dữ liệu Apriori / FP-Growth trong C# phân tích lịch sử hóa đơn:
    * Tính toán chỉ số Hỗ trợ (Support $\ge 0.05$), Độ tin cậy (Confidence $\ge 0.3$) và Độ nâng (Lift $> 1.2$).
    * Tự động phát hiện các cặp sản phẩm thường mua cùng nhau (ví dụ: `Cà Phê Muối` $\rightarrow$ `Bánh Croissant Trứng Muối`).
    * Sinh gợi ý Combo kèm mức giảm giá ưu đãi khi khách thêm món chính vào giỏ hàng.
  * Lập tài liệu phân tích kỹ thuật và bảng đánh giá độ chính xác thuật toán phục vụ Báo cáo Đồ án.
* **FE 1 (Frontend Lead):**
  * Dựng Giao diện AI Chatbot Widget trên Customer PWA:
    * Nút biểu tượng Robot lơ lửng góc phải màn hình Menu.
    * Khung chat trượt mượt mà với các nút gợi ý câu hỏi nhanh (*"Tư vấn món ít ngọt"*, *"Món hot nhất hôm nay"*, *"Thức uống giải nhiệt"*).
    * Thẻ sản phẩm gợi ý hiển thị trực tiếp trong khung chat có nút `[+ Thêm vào giỏ]` thao tác 1 chạm.
  * Dựng Pop-up Gợi Ý Combo AI Thông Minh tại trang Giỏ hàng: *"Thêm Bánh Croissant chỉ với +20.000đ (Tiết kiệm 15.000đ)"*.
* **FE 2 (Frontend Dev):**
  * Dựng trang Quản trị Khuyến Mãi & Gói Combo trên Admin Portal (`/admin/combos`): Cho phép chủ quán xem các cặp sản phẩm do thuật toán AI-2 đề xuất và bật áp dụng giảm giá.
  * Dựng giao diện xem trước (Mock Preview) cho tính năng AI-3 NLQ Analytics trên Admin Dashboard và ghi chú rõ nhãn "Khu vực Nâng cấp Scale-Up".

#### Sản phẩm Bàn giao (Deliverables):
1. AI Chatbot tư vấn khẩu vị chuẩn xác bằng tiếng Việt, phản hồi dưới 2 giây và đưa ra đúng món ăn phù hợp với yêu cầu của khách.
2. Giỏ hàng hiển thị đúng gợi ý Combo thông minh theo dữ liệu giỏ hàng thực tế.
3. Bộ tài liệu phân tích thuật toán và benchmark phục vụ bảo vệ đồ án tốt nghiệp.

---

### 🟢 SPRINT 8 (Tuần 15–16): KIỂM THỬ UAT TOÀN DIỆN, DOCKER DEPLOY & BẢO VỆ ĐỒ ÁN

> **Mục tiêu Sprint:** Kiểm thử toàn diện hệ thống (End-to-End Testing), tối ưu hóa hiệu năng, đóng gói Docker Compose triển khai Production, chuẩn bị dữ liệu Demo mẫu và hoàn thiện Báo cáo Đồ án Tốt nghiệp cùng Slide thuyết trình bảo vệ.

#### Phân công Công việc Chi tiết:
* **BE 1 & BE 2 (Backend Team):**
  * Đóng gói Docker Compose Production hoàn chỉnh: 4 Containers (`smartfb-postgres`, `smartfb-redis`, `smartfb-backend`, `smartfb-frontend`) giao tiếp nội bộ qua mạng `smartfb-net`.
  * Cấu hình Nginx Reverse Proxy: SSL Certbot HTTPS, định tuyến WebSocket Upgrade cho SignalR, nén Gzip/Brotli.
  * Nạp Dữ Liệu Seed Data Hoàn Chỉnh cho buổi Demo:
    * 3 Chi nhánh (Smart Coffee Q1, Q3, Bình Thạnh) với đầy đủ cấu hình WiFi thực tế.
    * 20 Bàn kèm mã QR bàn chuẩn.
    * 40 Món ăn đồ uống đa dạng, công thức định lượng và hình ảnh chất lượng cao.
    * 100 Đơn hàng mẫu lịch sử đủ 3 loại (`DineIn`, `TakeAway`, `Delivery`) và dữ liệu tích ly CRM.
  * Chạy kịch bản Kiểm thử Tải (Load Testing) bằng k6: Đạt chỉ tiêu 100 req/s với độ trễ $p95 < 200$ms.
* **FE 1 & FE 2 (Frontend Team):**
  * Kiểm tra tính tương thích Responsive trên mọi thiết bị: iPhone, Android, iPad, Laptop POS và Màn hình TV KDS.
  * Tối ưu hóa Web Vitals: First Contentful Paint (FCP) $< 1.2$s, Largest Contentful Paint (LCP) $< 2.0$s.
  * Thực thi toàn bộ bộ 20+ Kịch bản Kiểm thử UAT (UAT Test Cases) bao trùm cả 5 Core Business Flows:
    * `TC-01` đến `TC-05`: Luồng Dine-in quét QR và thanh toán VietQR trước.
    * `TC-06` đến `TC-10`: Luồng Takeaway nhân viên quầy, tra SĐT và tích ly 10/10 nhận quà.
    * `TC-11` đến `TC-15`: Luồng QR Delivery đặt tại nhà, cộng 20k ship và theo dõi giao hàng.
    * `TC-16` đến `TC-20`: Luồng Chấm công WiFi đúng/sai mạng và điều phối KDS bếp.
* **Cả 4 Thành Viên (Toàn Đội):**
  * Hoàn thiện Báo cáo Đồ Án Tốt Nghiệp (Capstone Project Report) 5 chương theo quy chuẩn học thuật.
  * Thiết kế Slide Thuyết Trình Bảo Vệ chuyên nghiệp, súc tích, làm nổi bật 5 Thay đổi nghiệp vụ và điểm sáng AI.
  * Quay Video Demo 5 phút dự phòng (Backup Demo Video) bao quát trọn vẹn kịch bản vận hành thực tế.
  * Tổng duyệt (Rehearsal) thuyết trình và trả lời phản biện trước Hội đồng 3 lần.

#### Sản phẩm Bàn giao (Deliverables):
1. Hệ thống chạy trực tiếp trên Server Internet thông qua Docker Compose và tên miền HTTPS.
2. 100% Test Cases UAT chạy thành công không có lỗi nghiêm trọng (Zero Critical Bugs).
3. Bộ hồ sơ bảo vệ đồ án hoàn chỉnh: Báo cáo Word/PDF, Slide thuyết trình, Video Demo và Source Code sạch.

---

## 5. KẾ HOẠCH QUẢN TRỊ RỦI RO & DỰ PHÒNG KỸ THUẬT

| Rủi Ro Kỹ Thuật / Vận Hành | Mức Độ | Phương Án Phòng Ngừa & Xử Lý Dự Phòng | Phụ Trách |
|---|:---:|---|:---:|
| **Webhook VietQR bị chậm hoặc nghẽn mạng ngân hàng** | 🔴 Cao | Frontend PWA triển khai cơ chế Polling song song (`GET /api/v1/payments/{id}/status`) mỗi 3 giây; cung cấp nút bấm "Tôi đã chuyển khoản" để kích hoạt kiểm tra chủ động. | BE 1 & FE 1 |
| **Mất kết nối mạng Internet tại quán cà phê** | 🟡 Vừa | Staff Web POS lưu dữ liệu đơn hàng tạm thời vào LocalStorage/IndexedDB; PWA Service Worker cache sẵn Menu để khách duyệt món ngoại tuyến. | FE 1 & FE 2 |
| **Thiết bị nhân viên không đọc được BSSID WiFi qua trình duyệt** | 🟡 Vừa | Cơ chế Fallback chấm công: Xác thực dựa trên địa chỉ IP Public/Subnet mạng quán gửi trong Header request + Mã PIN định danh cá nhân. | BE 2 & FE 2 |
| **Hết hạn mức Quota Gemini API trong buổi Demo** | 🟡 Vừa | Cấu hình Fallback sang chế độ Mock Rule-based Response nếu Gemini API trả về lỗi 429 hoặc Timeout quá 3 giây. | BE 1 |
| **Xung đột mã nguồn khi tích hợp các nhánh Sprint** | 🟢 Thấp | Áp dụng nghiêm ngặt quy trình GitFlow: Mỗi tính năng làm trên branch riêng, bắt buộc PR Review chéo (BE duyệt BE, FE duyệt FE) trước khi merge vào `develop`. | Toàn đội |

---

## 6. QUY CHUẨN ĐÁNH GIÁ NGHIỆM THU TỪNG GIAI ĐOẠN

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                         BẢNG TIÊU CHÍ NGHIỆM THU TỪNG CỘT MỐC                          │
├──────────────┬──────────────────┬──────────────────────────────────────────────────────┤
│ Cột Mốc      │ Thời Điểm        │ Tiêu Chí Nghiệm Thu Bắt Buộc (Pass Criteria)         │
├──────────────┼──────────────────┼──────────────────────────────────────────────────────┤
│ **Gate 1**   │ Cuối Sprint 2    │ • Solution .NET 8 Clean Architecture & Next.js sạch  │
│ (Foundation) │ (Tuần 4)         │ • EF Core Migration 28 bảng hoàn tất, Auth JWT chạy  │
│              │                  │ • Customer PWA hiển thị Menu tĩnh thành công         │
├──────────────┼──────────────────┼──────────────────────────────────────────────────────┤
│ **Gate 2**   │ Cuối Sprint 4    │ • Dine-in thanh toán VietQR thành công mới vào KDS   │
│ (Core MVP)   │ (Tuần 8)         │ • Staff Takeaway POS tra SĐT, tích 10 ly đổi 1 ly    │
│              │                  │ • SignalR KDS cập nhật trạng thái thời gian thực     │
├──────────────┼──────────────────┼──────────────────────────────────────────────────────┤
│ **Gate 3**   │ Cuối Sprint 6    │ • QR Delivery tự cộng 20k ship, thanh toán VietQR    │
│ (Operations) │ (Tuần 12)        │ • Chấm công WiFi-locked từ chối khi sai mạng         │
│              │                  │ • Staff Web Portal tích hợp Sơ đồ bàn & Gọi phục vụ  │
├──────────────┼──────────────────┼──────────────────────────────────────────────────────┤
│ **Gate 4**   │ Cuối Sprint 8    │ • AI Chatbot RAG & Combo Apriori hoạt động mượt mà   │
│ (Final Demo) │ (Tuần 16)        │ • Hệ thống Deploy Docker Compose Production trên VPS │
│              │                  │ • 100% UAT Test Cases Pass, Báo cáo & Slide hoàn tất │
└──────────────┴──────────────────┴──────────────────────────────────────────────────────┘
```

---

> 📌 **KẾT LUẬN ROADMAP:**  
> Lộ trình 16 tuần phân bổ cân bằng năng lực giữa 4 thành viên, tập trung tuyệt đối vào việc chuyển đổi thành công 5 nghiệp vụ cốt lõi, loại bỏ toàn bộ các thành phần lỗi thời (Staff Mobile App, GPS 50m, QR xoay 30s, Dine-in trả sau) và đưa 2 Module AI thiết thực nhất vào thực tiễn, bảo đảm đồ án đạt điểm số tối đa trong kỳ bảo vệ Capstone.
