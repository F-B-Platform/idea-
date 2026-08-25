# ☕ SMART F&B OPERATING SYSTEM (v2.5.0)
### NỀN TẢNG VẬN HÀNH QUÁN CÀ PHÊ THÔNG MINH ĐA PHÂN HỆ (WEB-FIRST)

[![.NET 8](https://img.shields.io/badge/.NET-8.0-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/)
[![Next.js 14](https://img.shields.io/badge/Next.js-14.2-black?logo=next.js&logoColor=white)](https://nextjs.org/)
[![PostgreSQL 16](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Redis 7](https://img.shields.io/badge/Redis-7.0-DC382D?logo=redis&logoColor=white)](https://redis.io/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![SignalR](https://img.shields.io/badge/SignalR-Realtime-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/apps/aspnet/signalr)
[![Git Branch](https://img.shields.io/badge/Git%20Branch-dev-brightgreen?logo=git&logoColor=white)](https://github.com/F-B-Platform/idea-/tree/dev)

---

## 📖 1. TỔNG QUAN DỰ ÁN

**Smart F&B OS** là nền tảng quản lý và vận hành chuyển đổi số toàn diện cho chuỗi 3 quán cà phê thông minh (Quận 1 - HCM, Cầu Giấy - HN, Hải Châu - ĐN).

Hệ thống được thiết kế theo triết lý **Web-First 100%** (chạy trực tiếp trên trình duyệt Web Responsive & PWA, không cần cài đặt App native), kết nối thời gian thực qua **SignalR WebSockets**, thanh toán tự động qua **VietQR PayOS** và tích hợp trí tuệ nhân tạo **Google Gemini AI & Apriori Combo Mining**.

---

## 🎯 2. CÁC QUY TẮC NGHIỆP VỤ BẤT BIẾN (CORE BUSINESS INVARIANTS)

Để đảm bảo toàn bộ team code đúng chuẩn và đồng nhất luồng, các thành viên cần nắm rõ 5 quy tắc cốt lõi sau:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   5 QUY TẮC NGHIỆP VỤ CỐT LÕI (v2.5.0)                                 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1️⃣ DINE-IN (Gọi tại bàn - 2 Nhánh):                                                                   │
│    • Nhánh A (VietQR Trước): Khách quét QR Bàn ➔ Chọn món ➔ Quét VietQR ➔ Webhook PayOS xác nhận      │
│      'Paid' ➔ Bếp KDS mới nhận đơn pha chế.                                                            │
│    • Nhánh B (Tiền mặt Sau): Khách chọn 'Tiền mặt' ➔ Đơn vào Bếp KDS ngay ('Confirmed') ➔ Pha chế     │
│      ➔ Nhân viên mang món ra bàn KÈM HÓA ĐƠN CÓ IN MÃ VIETQR ➔ Khách trả tiền mặt hoặc quét VietQR     │
│      trên bill ➔ Nhân viên/Thu ngân xác nhận đơn hoàn tất.                                             │
│                                                                                                        │
│ 2️⃣ DELIVERY (Giao tận nhà):                                                                           │
│    • Khách quét QR Delivery riêng ➔ Bắt buộc nhập SĐT + Địa chỉ chi tiết ➔ Tự động cộng phí ship cố    │
│      định 20.000 VNĐ ➔ 100% VietQR trả trước (Khóa hoàn toàn thanh toán COD).                          │
│                                                                                                        │
│ 3️⃣ TAKEAWAY (Mang về tại quầy POS):                                                                   │
│    • Thu ngân thao tác trực tiếp trên Web POS (Khách KHÔNG quét QR) ➔ Tra cứu SĐT CRM khách hàng      │
│      ➔ CHƯƠNG TRÌNH TÍCH 10 LY TẶNG 1 LY MIỄN PHÍ CHỈ ÁP DỤNG DUY NHẤT CHO TAKEAWAY ➔ Đơn vào KDS ngay │
│      ➔ Khách nhận đồ uống ➔ Thu tiền sau (Tiền mặt tính tiền thối / VietQR quầy).                      │
│                                                                                                        │
│ 4️⃣ CHẤM CÔNG (Attendance):                                                                             │
│    • Khóa chặt theo mạng WiFi Chi nhánh (Xác thực BSSID Router AP / IP Subnet + Mã Số NV).            │
│    • Tuyệt đối KHÔNG sử dụng GPS và KHÔNG dùng QR động xoay.                                           │
│                                                                                                        │
│ 5️⃣ ĐIỀU HÀNH BẾP & QUẢN LÝ (KDS & Management):                                                        │
│    • Bếp KDS nhận đơn realtime qua SignalR ➔ Xem định mức BOM (trừ kho theo gam/ml) ➔ Có công tắc      │
│      khẩn cấp 86-Toggle để báo hết món tức thì.                                                        │
│    • Quản lý mở ca két tiền, kết ca kiểm đếm và in biên bản đối soát Z-Report (giải trình khi lệch >50k)│
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏛️ 3. CẤU TRÚC KIẾN TRÚC HỆ THỐNG (PROJECT STRUCTURE)

```
Idea_DoAn/
├── backend/                                   # Solution .NET 8 Clean Architecture
│   ├── SmartFB.slnx                           # File Solution chính
│   ├── src/
│   │   ├── SmartFB.Domain/                    # 25 Entities 3NF, Enums, BaseEntity, IAggregateRoot
│   │   ├── SmartFB.Application/               # CQRS MediatR, Behaviors, DTOs, 10 Feature Modules:
│   │   │   └── Features/                      # (Auth, Branches, Tables, Products, Orders, Payments,
│   │   │                                      #  Attendances, KitchenKDS, ShiftsAndCash, AdminAnalytics)
│   │   ├── SmartFB.Infrastructure/            # EF Core 8 PostgreSQL 16, 29 Configurations, Redis Lock
│   │   └── SmartFB.API/                       # Controllers REST, 4 Hubs SignalR, JWT Auth, Swagger
│   └── tests/
│       ├── SmartFB.UnitTests/                 # Unit Tests (xUnit & FluentAssertions)
│       └── SmartFB.IntegrationTests/          # Integration Tests (WebApplicationFactory)
│
├── frontend/                                  # Next.js 14 App Router Monorepo
│   ├── package.json                           # Next.js 14, React 18, Tailwind CSS, Zustand, SignalR
│   └── src/
│       ├── app/                               # 5 Route Groups phân rã vai trò:
│       │   ├── (customer)/                    # PWA Khách: Menu, Cart, Delivery, Tracking, VietQR, Review
│       │   ├── (kds)/                         # Màn hình KDS Bếp Realtime, 86-Toggle, Batch View
│       │   ├── (staff)/                       # Web POS Quầy Takeaway (CRM 10 ly), Sơ đồ bàn, Chấm công WiFi
│       │   ├── (manager)/                     # Portal Quản lý Chi nhánh: Ca két, Z-Report, Kho BOM
│       │   └── (admin)/                       # Portal Chủ chuỗi: CRUD Menu, BOM từng size, Giá vùng, P&L
│       ├── components/ui/                     # Thư mục UI Components dùng chung
│       ├── hooks/                             # Custom hooks: useSignalR, useAttendanceWifi, useApiQuery
│       ├── stores/                            # Zustand Stores: useAuthStore, useCartStore, usePosStore
│       └── types/                             # Shared TypeScript Interfaces & DTOs
│
├── scripts/                                   # Scripts Khởi Chạy Tự Động
│   ├── start-dev-db.ps1                       # Bật PostgreSQL 16 & Redis 7 (Windows PowerShell)
│   ├── start-dev-db.sh                        # Bật PostgreSQL 16 & Redis 7 (Linux/macOS)
│   └── init-db.sql                            # Kích hoạt uuid-ossp, pg_trgm
│
├── docker-compose.dev.yml                     # Cấu hình Database & Redis cho Local Dev
├── docker-compose.yml                         # Cấu hình Full Deployment Production
├── nginx/nginx.conf                           # NGINX Reverse Proxy, SSL & WebSocket Config
└── DEVELOPER_ONBOARDING.md                    # Hướng dẫn chi tiết cho từng thành viên trong team
```

---

## 👥 4. PHÂN CHIA NHIỆM VỤ CHO 4 THÀNH VIÊN (TEAM MATRIX)

| Thành Viên | Vai Trò | Trọng Tâm Nhiệm Vụ Chi Tiết | Thư Mục Phụ Trách |
|:---:|:---:|---|---|
| 👨‍💻 **BE 1** | **Backend Lead** | • Xây dựng CQRS Handlers cho module `Orders` (3 kênh: DineIn 2 nhánh, Delivery phí 20k, Takeaway).<br>• Tích hợp thanh toán `Payments` (PayOS Webhook HMAC-SHA256 & Tiền mặt).<br>• Thiết lập realtime qua 4 SignalR Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`). | `backend/src/SmartFB.Application/Features/Orders/`<br>`backend/src/SmartFB.Application/Features/Payments/`<br>`backend/src/SmartFB.API/Hubs/` |
| 👨‍💻 **BE 2** | **Backend Dev** | • Chạy EF Core Migrations & Seed Data cho 25 bảng thực thể.<br>• Module `Attendances` (Xác thực WiFi BSSID/IP) & `ShiftsAndCash` (Két tiền & Z-Report).<br>• Module `KitchenKDS` (Trừ kho BOM theo gam/ml, 86-Toggle).<br>• Tích hợp Google Gemini Chatbot API & Thuật toán Combo Apriori. | `backend/src/SmartFB.Infrastructure/Persistence/`<br>`backend/src/SmartFB.Application/Features/Attendances/`<br>`backend/src/SmartFB.Application/Features/KitchenKDS/`<br>`backend/src/SmartFB.Application/Features/ShiftsAndCash/` |
| 🎨 **FE 1** | **Frontend Lead** | • Xây dựng PWA Khách hàng: `(customer)/menu`, `(customer)/delivery`.<br>• Quản lý giỏ hàng `useCartStore`, kết nối PayOS QR và Tracking đơn realtime.<br>• Xây dựng Widget AI Chatbot tư vấn đồ uống. | `frontend/src/app/(customer)/`<br>`frontend/src/stores/useCartStore.ts`<br>`frontend/src/components/` |
| 💻 **FE 2** | **Frontend Dev** | • Xây dựng giao diện Web POS Quầy Takeaway (CRM tra SĐT, tích 10 ly tặng 1).<br>• Xây dựng Web KDS Bếp TV realtime & Chấm công WiFi.<br>• Xây dựng Portal Quản lý `(manager)` và Portal Chủ chuỗi `(admin)`. | `frontend/src/app/(staff)/`<br>`frontend/src/app/(kds)/`<br>`frontend/src/app/(manager)/`<br>`frontend/src/app/(admin)/` |

---

## 🚀 5. HƯỚNG DẪN KHỞI ĐỘNG NHANH TRONG 3 BƯỚC (QUICK START)

### 📌 Bước 1: Kéo Code Về Máy Local
```bash
git fetch origin
git checkout dev
git pull origin dev

# Tạo file môi trường từ mẫu
cp .env.example .env
cp frontend/.env.example frontend/.env.local
```

### 📌 Bước 2: Bật Database & Redis Local (1 Lệnh Duy Nhất)
- **Trên Windows (PowerShell):**
  ```powershell
  .\scripts\start-dev-db.ps1
  ```
- **Trên Linux / macOS (Bash):**
  ```bash
  chmod +x ./scripts/start-dev-db.sh
  ./scripts/start-dev-db.sh
  ```
> **Thông số kết nối:** PostgreSQL: `localhost:5432` (`postgres` / `postgres_password_dev_2026` / DB: `smart_fb_db`) | Redis: `localhost:6379` | pgAdmin: `http://localhost:5050` (`admin@smartfb.vn` / `admin123`).

### 📌 Bước 3: Khởi Chạy Backend & Frontend

#### Chạy Backend API (Port 5000):
```bash
cd backend
dotnet restore SmartFB.slnx
dotnet run --project src/SmartFB.API/SmartFB.API.csproj
```
- **Swagger Documentation:** [http://localhost:5000/swagger](http://localhost:5000/swagger)
- **Health Check API:** [http://localhost:5000/api/v1/health](http://localhost:5000/api/v1/health)

#### Chạy Frontend Web (Port 3000):
```bash
cd frontend
npm install
npm run dev
```
- **Developer Portal Landing Page:** [http://localhost:3000](http://localhost:3000)

---

## 🌿 6. QUY CHUẨN PHÂN NHÁNH & COMMIT (GITFLOW)

Mọi tính năng mới trong Sprint được tạo nhánh từ `dev`:

```bash
# Tạo nhánh cho Backend
git checkout -b feature/be-orders dev

# Tạo nhánh cho Frontend
git checkout -b feature/fe-customer-pwa dev
```

### Chuẩn Conventional Commits:
- `feat(order): add create dine-in order command with fluent validation`
- `feat(pos): implement takeaway 10-cup loyalty calculation`
- `fix(wifi): validate bssid mac address format`
- `test(attendance): add unit tests for wifi attendance validator`

---

## 📚 7. TÀI LIỆU THAM CHIẾU KỸ THUẬT (DOCS DIRECTORY)

- 📂 [`01_Tai_Lieu_Dac_Ta_Goc/`](./01_Tai_Lieu_Dac_Ta_Goc/): Đặc tả 62 tính năng, 4 Actor và 16 Workflows chuẩn hóa.
- 📂 [`03_Quy_Trinh_Trien_Khai/`](./03_Quy_Trinh_Trien_Khai/): 8 Tài liệu thiết kế kỹ thuật (Database 25 bảng, 10 API Groups, Clean Architecture .NET 8, Next.js 14, Test Plan, Deployment).
- 📂 [`04_Thiet_Ke_Kien_Truc_Diagrams/`](./04_Thiet_Ke_Kien_Truc_Diagrams/): 22 Sơ đồ Mermaid (C4 Model, 10 Sequence Diagrams, ERD 25 bảng, Deployment 6 tầng).
- 📂 [`05_Quy_Chuan_&_Test_Cases/`](./05_Quy_Chuan_&_Test_Cases/): 47 UAT Test Cases, SQL DDL/DML Seed Data mẫu và Quy chuẩn Coding GitFlow.
- 📄 [`DEVELOPER_ONBOARDING.md`](./DEVELOPER_ONBOARDING.md): Hướng dẫn chi tiết dành cho lập trình viên mới vào dự án.

---
*Smart F&B OS — Đồ Án Chuyên Nghiệp v2.5.0 (2026)*
