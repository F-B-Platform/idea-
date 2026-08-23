# 📚 TÀI LIỆU HƯỚNG DẪN KỸ THUẬT VẬN HÀNH & BẢN ĐỒ TRUY VẾT HỆ THỐNG
# SMART F&B OPERATING SYSTEM (SMART F&B OS)

> [!NOTE]
> **Mã định danh:** `MASTER-README-03` | **Phiên bản:** `v2.5.0-Production-Ready`  
> **Quy mô dự án:** Đồ án Capstone 4 thành viên (2 Backend Engineers + 2 Frontend Engineers) | Thời lượng: 16 tuần (08 Sprints)  
> **Tech Stack Toàn Diện:** .NET 8 Clean Architecture (C# 12) | EF Core 8 | PostgreSQL 16 (25 Thực thể 3NF) | Redis 7 (Cache-aside & RedLock) | SignalR 4 Real-time Hubs | PayOS (VietQR) | Google Gemini 1.5 Flash SDK (RAG) | Apriori Mining Engine | Next.js 14 App Router (5 Route Groups) | React 19 | Tailwind CSS | Shadcn UI | Zustand 4.5 | TanStack Query v5 | Docker Compose Multi-Container (5 Dịch vụ) | NGINX Reverse Proxy (SSL & WSS) | GitHub Actions CI/CD  
> **Nguồn sự thật tham chiếu:** `01_Tai_Lieu_Dac_Ta_Goc/` (`Smart_FB_Operating_System.md`, `Tong_Quan_Kien_Truc_He_Thong.md`, `Workflow_Quy_Trinh_Nghiep_Vu.md`, `Actor_Phan_Quyen_Chuc_Nang.md`, `Actor_KhachHang_Luong_Chay.md`)  
> **Cam kết chất lượng:** Bản đồ kiến trúc kỹ thuật chuẩn mực kết nối 8 quy trình chi tiết từ Phân tích yêu cầu (01), Thiết kế Cơ sở dữ liệu (02), Hợp đồng API (03), Thiết kế UI/UX (04), Hiện thực hóa Backend (05), Hiện thực hóa Frontend (06), Kế hoạch Kiểm thử (07) đến Triển khai Hạ tầng (08). Bảng ma trận truy vết toàn diện 100% 62 tính năng cốt lõi (`C-01` ~ `C-20`, `S-01` ~ `S-13`, `M-01` ~ `M-12`, `A-01` ~ `A-17`). Toàn bộ mã lệnh hoàn chỉnh 100%, không placeholder.

---

# 📑 MỤC LỤC BẢN ĐỒ HỆ THỐNG

1. [Tổng Quan Kiến Trúc & Cây Thư Mục 8 Quy Trình Triển Khai](#1-tổng-quan-kiến-trúc--cây-thư-mục-8-quy-trình-triển-khai)
2. [Bảng Ma Trận Khái Niệm Bị Cấm & Chuẩn Hóa Kiến Trúc](#2-bảng-ma-trận-khái-niệm-bị-cấm--chuẩn-hóa-kiến-trúc)
3. [Bản Đồ Phân Phối Trách Nhiệm 4 Thành Viên Đội Ngũ (Capstone Matrix)](#3-bản-đồ-phân-phối-trách-nhiệm-4-thành-viên-đội-ngũ-capstone-matrix)
4. [Ma Trận Truy Vết Kỹ Thuật Toàn Diện 62 Tính Năng (End-to-End Traceability)](#4-ma-trận-truy-vết-kỹ-thuật-toàn-diện-62-tính-năng-end-to-end-traceability)
   - 4.1 [Phân Hệ Khách Hàng (Customer: C-01 ~ C-20)](#41-phân-hệ-khách-hàng-customer-c-01--c-20)
   - 4.2 [Phân Hệ Nhân Viên (Staff: S-01 ~ S-13)](#42-phân-hệ-nhân-viên-staff-s-01--s-13)
   - 4.3 [Phân Hệ Quản Lý Chi Nhánh (Manager: M-01 ~ M-12)](#43-phân-hệ-quản-lý-chi-nhánh-manager-m-01--m-12)
   - 4.4 [Phân Hệ Quản Trị Trung Tâm (Admin: A-01 ~ A-17)](#44-phân-hệ-quản-trị-trung-tâm-admin-a-01--a-17)
5. [Hướng Dẫn Khởi Chạy Môi Trường Nhanh (Quick Start Guide)](#5-hướng-dẫn-khởi-chạy-môi-trường-nhanh-quick-start-guide)
   - 5.1 [Yêu Cầu Tiên Quyết Hệ Thống (Prerequisites)](#51-yêu-cầu-tiên-quyết-hệ-thống-prerequisites)
   - 5.2 [Quy Trình 4 Bước Khởi Chạy Môi Trường Phát Triển](#52-quy-trình-4-bước-khởi-chạy-môi-trường-phát-triển)
   - 5.3 [Lệnh Thực Thi Bộ Kiểm Thử Tự Động Hóa (Unit, Integration, k6, E2E)](#53-lệnh-thực-thi-bộ-kiểm-thử-tự-động-hóa-unit-integration-k6-e2e)
6. [Chỉ Số Cam Kết Vận Hành & SLA Hiệu Năng Hệ Thống](#6-chỉ-số-cam-kết-vận-hành--sla-hiệu-năng-hệ-thống)

---

# 1. TỔNG QUAN KIẾN TRÚC & CÂY THƯ MỤC 8 QUY TRÌNH TRIỂN KHAI

Hệ thống tài liệu kỹ thuật trong thư mục `03_Quy_Trinh_Trien_Khai/` được xây dựng theo cấu trúc phân tầng khép kín từ Đặc tả yêu cầu đến Triển khai hạ tầng:

```
d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai/
├── README.md                      # 📚 Bản đồ trung tâm & Ma trận truy vết End-to-End 62 tính năng
├── 01_Phan_Tich_Yeu_Cau.md        # 📋 Đặc tả SRS, 62 FRs (C-01..20, S-01..13, M-01..12, A-01..17), 10 NFRs
├── 02_Thiet_Ke_Database.md        # 🗄️ Sơ đồ ERD 3NF (25 thực thể), DDL PostgreSQL 16, Indexing & Audit Logs
├── 03_Thiet_Ke_API_Contract.md    # 🔌 OpenAPI 3.1 Contract (10 nhóm API), PayOS Webhook HMAC, 4 SignalR Hubs
├── 04_Thiet_Ke_UI_UX.md           # 🎨 Design Tokens, 5 Route Groups Next.js 14, Wireframes ASCII Responsive
├── 05_Quy_Trinh_Backend.md        # ⚙️ .NET 8 Clean Architecture, MediatR CQRS, RedLock, SignalR, AI-1 & AI-2
├── 06_Quy_Trinh_Frontend.md       # 💻 Next.js 14 App Router Monorepo, 5 Zustand Stores, TanStack Query v5, PWA
├── 07_Ke_Hoach_Kiem_Thu.md        # 🧪 Testing Pyramid (60/25/10/5), 10 Edge Cases, k6 1.000 VUs, SignalR 500 CCU
└── 08_Trien_Khai_He_Thong.md      # 🚀 Docker Compose 5 Containers, NGINX SSL/WSS, GitHub Actions CI/CD, Backup
```

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                DANH MỤC 8 QUY TRÌNH TRIỂN KHAI KỸ THUẬT                          │
├─────┬──────────────┬───────────────────────────────┬─────────────────────────────────────────────┤
│ STT │ Mã Tài Liệu  │ Tên Tệp Quy Trình Kỹ Thuật    │ Trọng Tâm Kiến Trúc & Nội Dung Bàn Giao     │
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 01  │ `SPEC-SRS-01`│ `01_Phan_Tich_Yeu_Cau.md`     │ Đặc tả 62 Tính năng, 4 Actors, 10 NFRs,     │
│     │              │                               │ Business Invariants, 3 Kênh bán hàng.       │
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 02  │ `SPEC-DB-02` │ `02_Thiet_Ke_Database.md`     │ Sơ đồ ERD 3NF 25 thực thể, DDL PostgreSQL 16│
│     │              │                               │ hoàn chỉnh, GIN/B-Tree Indexes, Audit Logs. │
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 03  │ `SPEC-API-03`│ `03_Thiet_Ke_API_Contract.md` │ OpenAPI 3.1 Spec (10 Nhóm REST Endpoints),  │
│     │              │                               │ PayOS Webhook HMAC, Đặc tả 4 SignalR Hubs.  │
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 04  │ `SPEC-UI-04` │ `04_Thiet_Ke_UI_UX.md`        │ Hệ thống Design Tokens, 5 Route Groups      │
│     │              │                               │ Next.js 14, Wireframes ASCII chuẩn PWA/Web. │
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 05  │ `SPEC-BE-05` │ `05_Quy_Trinh_Backend.md`     │ .NET 8 Clean Architecture, MediatR CQRS,    │
│     │              │                               │ Redis 7 RedLock, Gemini 1.5 & Apriori AI.   │
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 06  │ `SPEC-FE-06` │ `06_Quy_Trinh_Frontend.md`    │ Next.js 14 App Router, 5 Zustand Stores,    │
│     │              │                               │ TanStack Query v5, SignalR Hooks, PWA Cache.│
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 07  │ `SPEC-TEST-07`│`07_Ke_Hoach_Kiem_Thu.md`     │ Testing Pyramid, 10 Critical Edge Cases,    │
│     │              │                               │ k6 Load Test 1.000 VUs, SignalR 500 CCU.    │
├─────┼──────────────┼───────────────────────────────┼─────────────────────────────────────────────┤
│ 08  │ `SPEC-OPS-08`│ `08_Trien_Khai_He_Thong.md`   │ Docker Compose 5 Containers, NGINX SSL/WSS, │
│     │              │                               │ CI/CD GitHub Actions, PostgreSQL Backup/DR. │
└─────┴──────────────┴───────────────────────────────┴─────────────────────────────────────────────┘
```

---

# 2. BẢNG MA TRẬN KHÁI NIỆM BỊ CẤM & CHUẨN HÓA KIẾN TRÚC

Để đảm bảo tính nhất quán tuyệt đối trên toàn bộ 8 tài liệu, các khái niệm lỗi thời hoặc sai lệch kiến trúc bị loại bỏ và chuẩn hóa theo bảng sau:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             MA TRẬN CHUẨN HÓA KIẾN TRÚC & LOẠI BỎ KHÁI NIỆM LỖI THỜI             │
├──────────────────────────────┬───────────────────────────────┬───────────────────────────────────┤
│ Khái Niệm Bị Cấm / Lỗi Thời  │ Chuẩn Hóa Thay Thế Chính Thức │ Lý Do Kiến Trúc & Phạm Vi Áp Dụng │
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ ❌ **Staff Mobile App**      │ ✅ **Responsive Web POS & KDS**│ Nhân viên và Barista chỉ sử dụng  │
│                              │   `(staff)` & `(kds)`         │ Web POS trên máy tính/tablet bàn. │
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ ❌ **Chấm công GPS 50m**     │ ✅ **WiFi-Locked Attendance** │ Chấm công khóa mạng 2 lớp: Subnet │
│                              │   (Subnet IP + AP BSSID)      │ IP mạng quán + BSSID Access Point.│
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ ❌ **QR xoay vòng 30s**      │ ✅ **Mã QR bàn tĩnh kèm chữ** │ Mã QR bàn in mica tĩnh, xác thực  │
│                              │   **ký số URL HMAC (sig)**    │ bằng chữ ký số bảo mật HMAC-SHA256│
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ ❌ **Tính năng C-23 & C-24** │ ✅ **Chuẩn hóa đúng 62 FRs**  │ Giới hạn danh mục tính năng đúng: │
│                              │   (C: 20, S: 13, M: 12, A: 17)│ `C-01`~`C-20`, `S-01`~`S-13`...   │
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ ❌ **Màn hình Voucher/Calo** │ ✅ **Tích hợp trong Giỏ hàng**│ Drawer tùy biến món chọn calo và  │
│    **tách riêng biệt**       │   **và Drawer tư vấn AI-1**   │ Giỏ hàng chọn voucher trực tiếp.  │
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ ❌ **Database 30 Bảng Cũ**   │ ✅ **25 Thực Thể 3NF Chuẩn**  │ Tối ưu hóa 25 thực thể nghiệp vụ  │
│                              │   (kèm bảng `audit_logs`)     │ quan hệ, loại bỏ bảng thừa.       │
└──────────────────────────────┴───────────────────────────────┴───────────────────────────────────┘
```

---

# 3. BẢN ĐỒ PHÂN PHỐI TRÁCH NHIỆM 4 THÀNH VIÊN ĐỘI NGŨ (CAPSTONE MATRIX)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 PHÂN BỔ TRÁCH NHIỆM 4 THÀNH VIÊN CAPSTONE                        │
├──────────────┬────────────────────────┬──────────────────────────────────────────────────────────┤
│ Thành Viên   │ Vai Trò Đảm Nhận       │ Module & Trọng Tâm Kỹ Thuật Phụ Trách                    │
├──────────────┼────────────────────────┼──────────────────────────────────────────────────────────┤
│ **BE1**      │ Lead Backend Engineer  │ • Core Order State Machine (Dine-In 2 nhánh, Delivery,   │
│              │                        │   Takeaway) & Validation Pipeline.                       │
│              │                        │ • Cổng Thanh Toán PayOS VietQR & Xử lý Webhook HMAC.     │
│              │                        │ • 4 SignalR Real-time Hubs & Redis Backplane.            │
│              │                        │ • AI-1 Google Gemini 1.5 Flash SDK RAG Advisor Client.   │
├──────────────┼────────────────────────┼──────────────────────────────────────────────────────────┤
│ **BE2**      │ Backend Specialist     │ • Chấm công WiFi-Locked (IP Subnet & BSSID Verification).│
│              │                        │ • Quản lý Ca Két tiền mặt & Thuật toán Đối soát Z-Report.│
│              │                        │ • Quản lý Kho, Master BOM Recipes & Trừ kho tự động.     │
│              │                        │ • AI-2 Thuật toán Khai phá Luật kết hợp Apriori Engine.  │
├──────────────┼────────────────────────┼──────────────────────────────────────────────────────────┤
│ **FE1**      │ Lead Frontend Engineer │ • Route Group `(customer)` Mobile PWA (Menu, Cart, QR).  │
│              │                        │ • `useCartStore` & Drawer Tùy biến món (ModifierDrawer). │
│              │                        │ • Form Đặt hàng QR Delivery (Phí ship 20k) & VietQR Timer│
│              │                        │ • Widget AI-1 Chatbot Gemini & PWA Service Worker Cache. │
├──────────────┼────────────────────────┼──────────────────────────────────────────────────────────┤
│ **FE2**      │ Frontend Specialist    │ • Route Group `(staff)` Web POS Quầy Takeaway (Tích 10 ly│
│              │                        │ • Route Group `(kds)` Màn hình Bếp Dark Mode Fullscreen. │
│              │                        │ • Route Group `(manager)` Mở/Đóng ca Z-Report Modal.     │
│              │                        │ • Route Group `(admin)` Executive Dashboard P&L Charts.  │
└──────────────┴────────────────────────┴──────────────────────────────────────────────────────────┘
```

---

# 4. MA TRẬN TRUY VẾT KỸ THUẬT TOÀN DIỆN 62 TÍNH NĂNG (END-TO-END TRACEABILITY)

Ma trận đối soát khép kín giữa 62 Tính năng nghiệp vụ qua toàn bộ 8 quy trình triển khai kỹ thuật:

### 4.1 Phân Hệ Khách Hàng (Customer: `C-01` ~ `C-20`)

| Mã | Tên Tính Năng | 01 SRS | 02 DB Entities | 03 API Endpoints | 04 UI Routes | 05 Backend Handlers | 06 Frontend State | 07 QA Test Suites | 08 Containers |
|:---:|---|:---:|---|---|---|---|---|---|:---:|
| **C-01** | Quét QR bàn tại quán | `C-01` | `tables`, `branches` | `POST /tables/verify-qr` | `(customer)/table/[b]/[t]` | `VerifyTableQrQueryHandler` | `useCartStore` | `TableQrVerificationTests` | `be`, `fe`, `db` |
| **C-02** | Quét QR đặt tận nơi | `C-02` | `branches` | `GET /branches/{id}/delivery-info` | `(customer)/delivery` | `GetDeliveryInfoQueryHandler` | `useCartStore` | `BranchDeliveryTests` | `be`, `fe`, `db` |
| **C-03** | Xem thực đơn số | `C-03` | `categories`, `products` | `GET /menu/branch/{id}` | `(customer)/menu` | `GetBranchMenuQueryHandler` | `useMenuQuery` | `MenuQueryTests` | `be`, `fe`, `redis`|
| **C-04** | Tìm kiếm & Lọc món | `C-04` | `products`, `categories` | `GET /menu/search` | `(customer)/menu/search` | `SearchMenuQueryHandler` | `useMenuQuery` | `MenuSearchTests` | `be`, `fe`, `db` |
| **C-05** | Tùy biến món & BOM | `C-05` | `modifiers`, `product_modifiers` | `GET /products/{id}/modifiers` | `(customer)/menu/product/[id]` | `GetProductModifiersHandler` | `ModifierDrawer` | `ProductModifierTests` | `be`, `fe`, `db` |
| **C-06** | Quản lý giỏ hàng | `C-06` | (Client Local State) | `POST /cart/validate` | `(customer)/cart` | `ValidateCartCommandHandler` | `useCartStore` | `useCartStore.test.ts` | `fe` |
| **C-07** | Áp dụng Voucher | `C-07` | `vouchers`, `voucher_redemptions` | `POST /vouchers/apply` | `(customer)/cart` | `ApplyVoucherCommandHandler` | `useCartStore` | `VoucherCommandTests` | `be`, `fe`, `db` |
| **C-08** | Đặt món VietQR trước | `C-08` | `orders`, `order_items`, `payments` | `POST /orders/vietqr` | `(customer)/checkout/vietqr` | `CreateOrderCommandHandler` | `useCartStore` | `CreateOrderCommandTests` | `be`, `fe`, `db`, `redis` |
| **C-09** | Đặt món Tiền mặt sau | `C-09` | `orders`, `order_items`, `tables` | `POST /orders/cash-dinein` | `(customer)/checkout/cash` | `CreateOrderCommandHandler` | `useCartStore` | `CreateOrderCommandTests` | `be`, `fe`, `db` |
| **C-10** | Đặt đơn Delivery 20k | `C-10` | `orders` (`delivery_fee=20k`) | `POST /orders/delivery` | `(customer)/delivery` | `CreateOrderCommandHandler` | `useCartStore` (`fee:20k`) | `CreateOrderCommandTests` | `be`, `fe`, `db` |
| **C-11** | Theo dõi đơn Real-time | `C-11` | `orders` | `SignalR /hubs/orders` | `(customer)/tracking/[id]` | `OrderHubBroadcaster` | `useSignalRHub` | `OrderTrackingHubTests` | `be`, `fe`, `redis`|
| **C-12** | Gọi nhân viên tại bàn | `C-12` | `tables` | `POST /service-requests` | `(customer)/service-action` | `CreateServiceRequestHandler` | `useSignalRHub` | `ServiceRequestTests` | `be`, `fe`, `redis`|
| **C-13** | Yêu cầu in tạm tính | `C-13` | `orders`, `tables` | `POST /orders/{id}/request-bill` | `(customer)/orders/[id]/bill` | `RequestBillCommandHandler` | `useSignalRHub` | `BillRequestTests` | `be`, `fe`, `db` |
| **C-14** | Chatbot AI-1 Gemini | `C-14` | `products`, `recipes_bom` | `POST /ai/chatbot-query` | `(customer)/ai-consultant` | `GeminiAdvisorService` | `AiChatbotWidget` | `GeminiAdvisorTests` | `be`, `fe`, `gemini` |
| **C-15** | Đăng nhập OTP CRM | `C-15` | `customers` | `POST /auth/verify-otp` | `(customer)/auth/phone-login` | `VerifyOtpCommandHandler` | `useAuthStore` | `CustomerAuthTests` | `be`, `fe`, `db` |
| **C-16** | Xem lịch sử đơn hàng | `C-16` | `orders`, `order_items` | `GET /customers/orders` | `(customer)/profile/orders` | `GetCustomerOrdersHandler` | `useAuthStore` | `CustomerOrderQueryTests`| `be`, `fe`, `db` |
| **C-17** | Sổ địa chỉ & Hồ sơ | `C-17` | `customers` | `PUT /customers/profile` | `(customer)/profile/addresses` | `UpdateCustomerProfileHandler`| `useAuthStore` | `CustomerProfileTests` | `be`, `fe`, `db` |
| **C-18** | Đánh giá 1-5 sao | `C-18` | `customer_reviews` | `POST /reviews` | `(customer)/orders/[id]/review`| `CreateReviewCommandHandler` | `ReviewDialog` | `CustomerReviewTests` | `be`, `fe`, `db` |
| **C-19** | Tải ảnh feedback | `C-19` | `customer_reviews` | `POST /reviews/{id}/photos` | `(customer)/orders/[id]/review`| `UploadReviewPhotosHandler` | `ReviewDialog` | `ReviewMediaTests` | `be`, `fe`, `db` |
| **C-20** | Gợi ý món kèm AI-2 | `C-20` | `products` | `GET /recommendations/cross-sell` | `(customer)/cart` | `GetCrossSellQueryHandler` | `useCartStore` | `CrossSellQueryTests` | `be`, `fe`, `db` |

---

### 4.2 Phân Hệ Nhân Viên (Staff: `S-01` ~ `S-13`)

| Mã | Tên Tính Năng | 01 SRS | 02 DB Entities | 03 API Endpoints | 04 UI Routes | 05 Backend Handlers | 06 Frontend State | 07 QA Test Suites | 08 Containers |
|:---:|---|:---:|---|---|---|---|---|---|:---:|
| **S-01** | Đăng nhập ca POS | `S-01` | `users`, `user_roles`, `shifts` | `POST /auth/staff-login` | `(staff)/login` | `StaffLoginCommandHandler` | `useAuthStore` | `StaffAuthTests` | `be`, `fe`, `db` |
| **S-02** | Chấm công WiFi | `S-02` | `attendances`, `branch_wifi_configs`| `POST /attendance/verify-wifi` | `(staff)/attendance` | `WifiAttendanceCommandHandler`| `useNetworkDetector`| `WifiAttendanceTests` | `be`, `fe`, `db` |
| **S-03** | Màn hình KDS Queue | `S-03` | `orders`, `order_items` | `SignalR /hubs/kitchen` | `(kds)/kds` | `KdsHubBroadcaster` | `useKdsStore` | `KdsDisplayTests` | `be`, `fe`, `redis`|
| **S-04** | Xem công thức BOM | `S-04` | `recipes_bom`, `ingredients` | `GET /bom/recipe/{id}` | `(kds)/kds` | `GetBomRecipeQueryHandler` | `BomRecipeModal` | `BomRecipeQueryTests` | `be`, `fe`, `db` |
| **S-05** | Cập nhật pha chế KDS | `S-05` | `orders`, `order_items` | `PUT /orders/{id}/status` | `(kds)/kds` | `UpdateKdsStatusCommandHandler`| `useKdsStore` | `KdsStatusCommandTests` | `be`, `fe`, `db` |
| **S-06** | Tạo đơn Takeaway POS | `S-06` | `orders`, `order_items` | `POST /orders/takeaway` | `(staff)/pos/takeaway` | `CreateTakeawayOrderHandler` | `usePosStore` | `TakeawayOrderTests` | `be`, `fe`, `db` |
| **S-07** | CRM 10 ly Takeaway | `S-07` | `customers`, `loyalty_cup_transactions`| `GET /crm/lookup` | `(staff)/pos/takeaway` | `LookupCustomerCrmHandler` | `usePosStore` (`cupBal`)| `LoyaltyCrmQueryTests` | `be`, `fe`, `db` |
| **S-08** | Thu tiền Takeaway | `S-08` | `payments`, `orders`, `shifts` | `POST /payments/takeaway` | `(staff)/pos/takeaway` | `ProcessTakeawayPaymentHandler`| `usePosStore` | `TakeawayPaymentTests` | `be`, `fe`, `db` |
| **S-09** | Xác nhận tiền mặt B | `S-09` | `payments`, `orders`, `tables` | `POST /payments/cash-confirm` | `(staff)/tables` | `ConfirmCashPaymentHandler` | `usePosStore` | `DineInCashConfirmTests` | `be`, `fe`, `db` |
| **S-10** | Xem sơ đồ bàn | `S-10` | `tables`, `orders` | `GET /tables/status` | `(staff)/tables` | `GetTablesStatusQueryHandler` | `usePosStore` | `TableManagementTests` | `be`, `fe`, `db` |
| **S-11** | Nhận chuông gọi bàn | `S-11` | `tables` | `PUT /service-requests/{id}/ack` | `(staff)/tables` | `AcknowledgeRequestHandler` | `useAudioAlert` | `ServiceRequestAckTests` | `be`, `fe`, `redis`|
| **S-12** | In bill & Tem dán ly | `S-12` | `orders`, `order_items` | `POST /print/job` | `(staff)/pos/takeaway` | `EscPosPrinterClient` | `PrintClient` | `PrintServiceTests` | `be`, `printer` |
| **S-13** | Báo cáo doanh thu ca | `S-13` | `orders`, `payments`, `shifts` | `GET /shifts/my-summary` | `(staff)/shifts` | `GetStaffShiftSummaryHandler` | `useShiftStore` | `StaffShiftReportTests` | `be`, `fe`, `db` |

---

### 4.3 Phân Hệ Quản Lý Chi Nhánh (Manager: `M-01` ~ `M-12`)

| Mã | Tên Tính Năng | 01 SRS | 02 DB Entities | 03 API Endpoints | 04 UI Routes | 05 Backend Handlers | 06 Frontend State | 07 QA Test Suites | 08 Containers |
|:---:|---|:---:|---|---|---|---|---|---|:---:|
| **M-01** | Mở ca két tiền | `M-01` | `shifts` | `POST /shifts/open` | `(manager)/shifts` | `OpenShiftCommandHandler` | `useShiftStore` | `CashShiftCommandTests` | `be`, `fe`, `db` |
| **M-02** | Đóng ca Z-Report | `M-02` | `shifts` (`z_report_json`) | `POST /shifts/close` | `(manager)/shifts` | `CloseCashShiftCommandHandler` | `useShiftStore` | `ZReportCommandTests` | `be`, `fe`, `db` |
| **M-03** | Lập lịch phân ca | `M-03` | `shifts`, `users` | `POST /schedules/weekly` | `(manager)/schedules` | `CreateWeeklyScheduleHandler` | `ScheduleForm` | `ShiftSchedulingTests` | `be`, `fe`, `db` |
| **M-04** | Giám sát chấm công | `M-04` | `attendances` | `GET /attendance/branch` | `(manager)/attendance` | `GetBranchAttendanceHandler` | `AttendanceTable` | `AttendanceMonitorTests` | `be`, `fe`, `db` |
| **M-05** | Kiểm kê tồn kho BOM | `M-05` | `ingredients`, `recipes_bom` | `POST /inventory/reconcile` | `(manager)/inventory` | `ReconcileInventoryHandler` | `StockCountTable` | `InventoryCountTests` | `be`, `fe`, `db` |
| **M-06** | Lập phiếu nhập kho | `M-06` | `ingredients`, `inventory_transactions`| `POST /inventory/requisitions` | `(manager)/inventory` | `CreateStockRequisitionHandler`| `RequisitionForm` | `StockRequisitionTests` | `be`, `fe`, `db` |
| **M-07** | Cấu hình sơ đồ bàn | `M-07` | `tables` | `PUT /tables/layout` | `(manager)/tables/config` | `UpdateTableLayoutHandler` | `TableGridCanvas` | `TableLayoutConfigTests`| `be`, `fe`, `db` |
| **M-08** | Khóa món hết hàng 86 | `M-08` | `product_branch_prices` | `PUT /menu/overrides/86` | `(manager)/menu` | `Toggle86CommandHandler` | `useKdsStore` | `ProductAvailabilityTests`| `be`, `fe`, `redis`|
| **M-09** | Cấu hình WiFi quán | `M-09` | `branch_wifi_configs` | `PUT /branch-wifi/config` | `(manager)/wifi-config` | `UpdateBranchWifiConfigHandler`| `WifiConfigForm` | `BranchWifiConfigTests` | `be`, `fe`, `db` |
| **M-10** | Nhận alert review <=2*| `M-10` | `customer_reviews` | `SignalR /hubs/notifications` | `(manager)/reviews` | `ReviewNotificationBroadcaster`| `useAudioAlert` | `ReviewNotificationTests`| `be`, `fe`, `redis`|
| **M-11** | Duyệt ảnh feedback | `M-11` | `customer_reviews` | `PUT /reviews/{id}/moderate` | `(manager)/reviews` | `ModerateReviewPhotoHandler` | `PhotoGallery` | `ReviewModerationTests` | `be`, `fe`, `db` |
| **M-12** | Dashboard KPI CN | `M-12` | `orders`, `payments` | `GET /reports/branch-kpi` | `(manager)/dashboard` | `GetBranchKpiDashboardHandler` | `KpiMetricsBar` | `BranchKpiDashboardTests`| `be`, `fe`, `db` |

---

### 4.4 Phân Hệ Quản Trị Trung Tâm (Admin: `A-01` ~ `A-17`)

| Mã | Tên Tính Năng | 01 SRS | 02 DB Entities | 03 API Endpoints | 04 UI Routes | 05 Backend Handlers | 06 Frontend State | 07 QA Test Suites | 08 Containers |
|:---:|---|:---:|---|---|---|---|---|---|:---:|
| **A-01** | Quản lý chi nhánh | `A-01` | `branches`, `branch_wifi_configs`| `POST /admin/branches` | `(admin)/branches` | `CreateBranchCommandHandler` | `BranchForm` | `AdminBranchTests` | `be`, `fe`, `db` |
| **A-02** | Quản lý RBAC nhân sự| `A-02` | `users`, `roles`, `user_roles` | `POST /admin/users` | `(admin)/users` | `CreateUserRbacCommandHandler` | `UserRbacTable` | `AdminUserRbacTests` | `be`, `fe`, `db` |
| **A-03** | Tạo món ăn mới | `A-03` | `products`, `categories` | `POST /admin/products` | `(admin)/menu/create` | `CreateProductCommandHandler` | `ProductEditor` | `AdminProductTests` | `be`, `fe`, `db` |
| **A-04** | Sửa món & Biến thể | `A-04` | `products`, `product_sizes` | `PUT /admin/products/{id}` | `(admin)/menu/[id]/edit` | `UpdateProductCommandHandler` | `ProductEditor` | `AdminProductTests` | `be`, `fe`, `db` |
| **A-05** | Xóa mềm món ăn | `A-05` | `products` (`is_deleted=true`) | `DELETE /admin/products/{id}` | `(admin)/menu` | `SoftDeleteProductCommandHandler`| `ProductTable` | `AdminProductTests` | `be`, `fe`, `db` |
| **A-06** | Thay thế món cũ | `A-06` | `products`, `audit_logs` | `POST /admin/products/replace` | `(admin)/menu/[id]/replace` | `ReplaceProductCommandHandler` | `ProductReplaceModal`| `AdminProductTests` | `be`, `fe`, `db` |
| **A-07** | Quản lý ảnh WebP | `A-07` | `products`, `categories` | `POST /admin/media/upload` | `(admin)/media` | `UploadWebPMediaCommandHandler`| `MediaLibrary` | `AdminMediaTests` | `be`, `fe`, `db` |
| **A-08** | Sắp xếp danh mục | `A-08` | `categories` (`display_order`) | `PUT /admin/categories/reorder` | `(admin)/categories` | `ReorderCategoriesCommandHandler`| `CategoryTree` | `AdminCategoryTests` | `be`, `fe`, `db` |
| **A-09** | Lên lịch thực đơn | `A-09` | `products`, `categories` | `POST /admin/menu/schedules` | `(admin)/seasonal-menus` | `ScheduleMenuCommandHandler` | `SeasonalScheduler` | `SeasonalMenuTests` | `be`, `fe`, `db` |
| **A-10** | Định nghĩa Master BOM| `A-10` | `recipes_bom`, `ingredients` | `POST /admin/bom` | `(admin)/bom` | `DefineMasterBomCommandHandler` | `BomRecipeEditor` | `MasterBomTests` | `be`, `fe`, `db` |
| **A-11** | Quản lý giá vùng | `A-11` | `product_branch_prices` | `POST /admin/pricing/groups` | `(admin)/pricing` | `SetRegionalPricingHandler` | `RegionalPriceTable`| `RegionalPricingTests` | `be`, `fe`, `db` |
| **A-12** | Khai phá AI-2 Apriori| `A-12` | `orders`, `order_items` | `POST /admin/ai/apriori/mine` | `(admin)/ai/combos` | `MineAprioriCombosCommandHandler`| `AprioriDashboard` | `AprioriEngineTests` | `be`, `fe`, `db` |
| **A-13** | Phê duyệt AI Combo | `A-13` | `products`, `product_sizes` | `POST /admin/ai/combos/approve`| `(admin)/ai/combos` | `ApproveAprioriComboHandler` | `AprioriComboCard` | `AdminComboApprovalTests`| `be`, `fe`, `db` |
| **A-14** | Thiết lập Voucher | `A-14` | `vouchers` | `POST /admin/vouchers` | `(admin)/vouchers` | `CreateVoucherCommandHandler` | `VoucherForm` | `AdminVoucherTests` | `be`, `fe`, `db` |
| **A-15** | Chính sách Loyalty | `A-15` | `customers`, `loyalty_cup_transactions`| `PUT /admin/crm/policy` | `(admin)/loyalty` | `UpdateLoyaltyPolicyHandler` | `LoyaltyPolicyForm` | `AdminLoyaltyPolicyTests`| `be`, `fe`, `db` |
| **A-16** | Báo cáo P&L hợp nhất | `A-16` | `orders`, `order_items`, `recipes_bom` | `GET /reports/pl-consolidated` | `(admin)/reports/pnl` | `GetConsolidatedPlReportHandler`| `PnLChartDashboard` | `AdminPlReportTests` | `be`, `fe`, `db` |
| **A-17** | Nhật ký kiểm toán | `A-17` | `audit_logs` | `GET /admin/audit-logs` | `(admin)/audit-logs` | `GetAuditLogsQueryHandler` | `AuditLogsTable` | `AuditLogsQueryTests` | `be`, `fe`, `db` |

---

# 5. HƯỚNG DẪN KHỞI CHẠY MÔI TRƯỜNG NHANH (QUICK START GUIDE)

### 5.1 Yêu Cầu Tiên Quyết Hệ Thống (Prerequisites)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 BẢNG CÔNG CỤ & PHIÊN BẢN TIÊN QUYẾT                              │
├──────────────────────────────┬───────────────────────────────┬───────────────────────────────────┤
│ Công Cụ / Môi Trường         │ Phiên Bản Yêu Cầu Tối Thiểu   │ Mục Đích Sử Dụng                  │
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ **Docker Engine**            │ `26.0+`                       │ Chạy môi trường container hóa     │
│ **Docker Compose Plugin**    │ `v2.27+`                      │ Điều phối cụm 5 dịch vụ           │
│ **.NET SDK**                 │ `8.0.300+`                    │ Biên dịch và kiểm thử Backend C#  │
│ **Node.js**                  │ `20.14.0 LTS (Iron)`          │ Runtime Frontend Next.js 14       │
│ **npm**                      │ `10.8.0+`                     │ Quản lý gói thư viện JavaScript   │
│ **k6**                       │ `0.51.0+`                     │ Thực thi kịch bản kiểm thử tải    │
└──────────────────────────────┴───────────────────────────────┴───────────────────────────────────┘
```

---

### 5.2 Quy Trình 4 Bước Khởi Chạy Môi Trường Phát Triển

```bash
# ------------------------------------------------------------------------------
# BƯỚC 1: TẢI MÃ NGUỒN VÀ KHỞI TẠO BIẾN MÔI TRƯỜNG
# ------------------------------------------------------------------------------
git clone https://github.com/smartfb/smartfb-operating-system.git
cd smartfb-operating-system

# Sao chép tệp biến môi trường mẫu
cp .env.production.example .env

# ------------------------------------------------------------------------------
# BƯỚC 2: KHỞI ĐỘNG HẠ TẦNG DỮ LIỆU BẰNG DOCKER COMPOSE
# ------------------------------------------------------------------------------
# Khởi động PostgreSQL 16 và Redis 7 dưới nền
docker compose up -d postgres-db redis-cache

# Kiểm tra trạng thái sẵn sàng của Database & Redis
docker compose ps

# ------------------------------------------------------------------------------
# BƯỚC 3: CẬP NHẬT DATABASE MIGRATION & SEED DỮ LIỆU MẪU
# ------------------------------------------------------------------------------
cd backend/src/SmartFB.API

# Thực thi Migration CSDL Entity Framework Core 8
dotnet ef database update --project ../SmartFB.Infrastructure

# Chạy Backend WebAPI (Lắng nghe tại http://localhost:5000)
dotnet run

# ------------------------------------------------------------------------------
# BƯỚC 4: KHỞI CHẠY FRONTEND NEXT.JS 14 APP ROUTER
# ------------------------------------------------------------------------------
# Mở một cửa sổ Terminal mới:
cd frontend
npm ci
npm run dev
# Truy cập giao diện tại: http://localhost:3000
```

---

### 5.3 Lệnh Thực Thi Bộ Kiểm Thử Tự Động Hóa (Unit, Integration, k6, E2E)

```bash
# ==============================================================================
# 1. THỰC THI KIỂM THỬ BACKEND (xUnit + Testcontainers)
# ==============================================================================
cd backend
dotnet test SmartFB.Backend.sln --verbosity normal --collect:"XPlat Code Coverage"

# ==============================================================================
# 2. THỰC THI KIỂM THỬ FRONTEND (Vitest + React Testing Library)
# ==============================================================================
cd frontend
npm run test:run

# ==============================================================================
# 3. THỰC THI KIỂM THỬ TẢI TRỌNG k6 (1.000 VUs & SignalR 500 CCU)
# ==============================================================================
# Kiểm thử tải RESTful API
k6 run tests/load/load-test-1000vu.js

# Kiểm thử chịu tải SignalR WebSockets
k6 run tests/load/signalr-stress-500ccu.js

# ==============================================================================
# 4. THỰC THI KIỂM THỬ TOÀN TRÌNH E2E (Playwright)
# ==============================================================================
cd frontend
npx playwright test
```

---

# 6. CHỈ SỐ CAM KẾT VẬN HÀNH & SLA HIỆU NĂNG HỆ THỐNG

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                BẢNG CHỈ SỐ CAM KẾT VẬN HÀNH (SLA & NFRA)                         │
├───────────────────────────────────┬──────────────────────┬───────────────────────────────────────┤
│ Chỉ Số Đo Lường                   │ Cam Kết Đạt Chuẩn    │ Cơ Chế Hiện Thực Hóa                  │
├───────────────────────────────────┼──────────────────────┼───────────────────────────────────────┤
│ **Thời Gian Phản Hồi Menu (P95)** │ **< 200ms**          │ Cache-Aside Redis 7 + Gzip NGINX      │
│ **Độ Trễ Tạo Đơn Hàng (P95)**     │ **< 500ms**          │ RedLock Phân Tán + Async Pipeline     │
│ **Độ Trễ Phân Phát KDS (P95)**    │ **< 200ms**          │ SignalR WebSocket + Redis Backplane   │
│ **Độ Trễ Chatbot AI Gemini (P95)**│ **< 1.5 Giây**       │ Google Gemini 1.5 Flash SDK Stream    │
│ **Khả Năng Phục Hồi Thảm Họa RTO**│ **< 1 Giờ**          │ Script Khôi Phục Tự Động 1 Lệnh       │
│ **Mất Mát Dữ Liệu Tối Đa RPO**    │ **< 24 Giờ**         │ Sao Lưu PostgreSQL Hàng Ngày Lúc 2h   │
│ **Tỷ Lệ Sẵn Sàng Vận Hành**       │ **99.9% Uptime**     │ Multi-Container Auto-Restart & NGINX  │
└───────────────────────────────────┴──────────────────────┴───────────────────────────────────────┘
```

---

*Tài liệu Tổng quan Kỹ thuật & Bản đồ Truy vết Hệ thống được biên soạn và chuẩn hóa toàn diện bởi Worker M4 (Lead QA, DevOps & Master Documentation Specialist) — Đạt chuẩn Production-Grade v2.5.0.*
