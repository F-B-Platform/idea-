# 🚀 HƯỚNG DẪN KHỞI ĐỘNG DỰ ÁN CHO ĐỘI NGŨ PHÁT TRIỂN (DEVELOPER ONBOARDING)
## HỆ THỐNG SMART F&B OPERATING SYSTEM (SMART F&B OS v2.5.0)

> **Nhánh Git Hạ Tầng:** `feature/infrastructure-setup`  
> **Quy mô dự án:** 16 tuần (8 Sprints) — Đội ngũ 4 thành viên (2 Backend + 2 Frontend)  
> **Kiến trúc:** .NET 8 Clean Architecture (CQRS MediatR, EF Core 8, SignalR) + Next.js 14 App Router (TypeScript, Tailwind, Zustand) + PostgreSQL 16 + Redis 7  

---

## 📑 MỤC LỤC

1. [Yêu Cầu Môi Trường Cài Đặt (Prerequisites)](#1-yêu-cầu-môi-trường-cài-đặt-prerequisites)
2. [Hướng Dẫn Lấy Code & Chuyển Nhánh (Git Setup)](#2-hướng-dẫn-lấy-code--chuyển-nhánh-git-setup)
3. [Khởi Động Nhanh Cơ Sở Dữ Liệu Local (Docker Compose)](#3-khởi-động-nhanh-cơ-sở-dữ-liệu-local-docker-compose)
4. [Hướng Dẫn Dành Cho Đội Ngũ BACKEND (BE 1 & BE 2)](#4-hướng-dẫn-dành-cho-đội-ngũ-backend-be-1--be-2)
5. [Hướng Dẫn Dành Cho Đội Ngũ FRONTEND (FE 1 & FE 2)](#5-hướng-dẫn-dành-cho-đội-ngũ-frontend-fe-1--fe-2)
6. [Bản Đồ Thư Mục Mã Nguồn (Project Structure)](#6-bản-đồ-thư-mục-mã-nguồn-project-structure)
7. [Quy Tắc Phân Chia Công Việc & Nhánh Tính Năng](#7-quy-tắc-phân-chia-công-việc--nhánh-tính-năng)

---

## 1. YÊU CẦU MÔI TRƯỜNG CÀI ĐẶT (PREREQUISITES)

Trước khi bắt đầu, các thành viên cần cài đặt đầy đủ các công cụ sau:
- **.NET 8 SDK** (hoặc .NET 10 SDK tương thích): Kiểm tra bằng `dotnet --version` (yêu cầu >= 8.0).
- **Node.js**: Phiên bản LTS 20.x hoặc 22.x/24.x (`node -v` và `npm -v`).
- **Docker Desktop**: Cần bật Docker để chạy PostgreSQL 16 và Redis 7 local (`docker --version`).
- **IDE / Trình soạn thảo**:
  - *Backend:* Visual Studio 2022, JetBrains Rider hoặc VS Code (cài C# Dev Kit extension).
  - *Frontend:* Visual Studio Code (cài Tailwind CSS IntelliSense, ESLint, Prettier extensions).

---

## 2. HƯỚNG DẪN LẤY CODE & CHUYỂN NHÁNH (GIT SETUP)

```bash
# 1. Clone repository về máy local (nếu chưa clone)
git clone <repo-url>
cd Idea_DoAn

# 2. Fetch toàn bộ nhánh từ remote
git fetch origin

# 3. Chuyển sang nhánh cấu hình hạ tầng
git checkout feature/infrastructure-setup

# 4. Sao chép file cấu hình môi trường mẫu
cp .env.example .env
cp frontend/.env.example frontend/.env.local
```

---

## 3. KHỞI ĐỘNG NHANH CƠ SỞ DỮ LIỆU LOCAL (DOCKER COMPOSE)

Chỉ cần chạy 1 lệnh duy nhất để bật toàn bộ cơ sở dữ liệu PostgreSQL 16, Redis 7 và pgAdmin:

### Trên Windows (PowerShell):
```powershell
.\scripts\start-dev-db.ps1
```

### Trên Linux / macOS (Bash):
```bash
chmod +x ./scripts/start-dev-db.sh
./scripts/start-dev-db.sh
```

### 🔑 Thông số kết nối mặc định:
- **PostgreSQL 16:** `localhost:5432` (Database: `smart_fb_db`, User: `postgres`, Password: `postgres_password_dev_2026`)
- **Redis 7:** `localhost:6379`
- **pgAdmin 4 Web UI:** `http://localhost:5050` (Email: `admin@smartfb.vn`, Password: `admin123`)

---

## 4. HƯỚNG DẪN DÀNH CHO ĐỘI NGŨ BACKEND (BE 1 & BE 2)

### 4.1. Mở Solution và Biên Dịch
```bash
# Di chuyển vào thư mục backend
cd backend

# Restore và build toàn bộ solution
dotnet restore SmartFB.slnx
dotnet build SmartFB.slnx

# Chạy Unit Tests & Integration Tests
dotnet test SmartFB.slnx
```

### 4.2. Khởi Chạy API Server (Port 5000)
```bash
dotnet run --project src/SmartFB.API/SmartFB.API.csproj
```
- **API Base URL:** `http://localhost:5000`
- **Swagger Documentation:** `http://localhost:5000/swagger`
- **Health Check Endpoint:** `http://localhost:5000/api/v1/health`
- **SignalR Hubs:**
  - `http://localhost:5000/hubs/order` (OrderHub)
  - `http://localhost:5000/hubs/kitchen` (KitchenHub)
  - `http://localhost:5000/hubs/payment` (PaymentHub)
  - `http://localhost:5000/hubs/notification` (NotificationHub)

### 4.3. Phân Công Backend
- 👨‍💻 **BE 1 (Lead & Core Architect):**
  - Tầng Application CQRS: Xây dựng Handlers/Validators cho phân hệ `Orders`, `Payments` (PayOS Webhook), `Products`.
  - Thiết lập SignalR Broadcast events trong `OrderHub` và `KitchenHub`.
- 👨‍💻 **BE 2 (Data, Operations & AI):**
  - EF Core Migrations & Seed Data theo tài liệu `05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md`.
  - Phân hệ `Attendance` (xác thực WiFi BSSID/IP), `CashShift` (Z-Report), `LoyaltyCup` (10 ly tặng 1).
  - Tích hợp Google Gemini AI Chatbot & Apriori Combo Engine.

---

## 5. HƯỚNG DẪN DÀNH CHO ĐỘI NGŨ FRONTEND (FE 1 & FE 2)

### 5.1. Cài Đặt và Khởi Chạy Web Server (Port 3000)
```bash
# Di chuyển vào thư mục frontend
cd frontend

# Cài đặt thư viện (nếu chưa cài)
npm install

# Kiểm tra lỗi TypeScript
npm run typecheck

# Khởi chạy server phát triển
npm run dev
```
- **Trang chủ Điều Hướng Phân Hệ:** `http://localhost:3000`

### 5.2. Các Phân Hệ Web Đã Cấu Hình Sẵn Khung:
| Tuyến Đường (Route) | Phân Hệ & Vai Trò | Trọng Tâm Giao Diện |
|---|---|---|
| `/menu` | `(customer)` | PWA Gọi món tại bàn (Dine-in): Chọn món, xem giỏ hàng, VietQR hoặc Tiền mặt kèm Bill QR. |
| `/delivery` | `(customer)` | PWA QR Delivery: Form nhập SĐT & địa chỉ bắt buộc, tự động cộng ship 20k, thanh toán 100% VietQR trước. |
| `/kitchen` | `(kds)` | Web KDS Bếp: Màn hình TV Barista nhận đơn realtime qua SignalR, xem BOM và 86-Toggle. |
| `/pos` | `(staff)` | Web POS Quầy: Thu ngân tạo đơn mang về, tra cứu CRM SĐT, tích 10 ly tặng 1, thu tiền sau. |
| `/attendance` | `(staff)` | Chấm công Khóa mạng WiFi: Kiểm tra BSSID Router và nhập Mã NV. |
| `/branch-dashboard` | `(manager)` | Portal Quản lý Chi nhánh: Ca két Z-Report, Kho BOM, cấu hình BSSID WiFi. |
| `/admin-dashboard` | `(admin)` | Portal Chủ chuỗi: CRUD Thực đơn, BOM từng size, Bảng giá vùng, duyệt Combo AI-2, P&L. |

### 5.3. Phân Công Frontend
- 🎨 **FE 1 (Lead & Customer UX):**
  - Xây dựng hoàn thiện PWA Khách hàng: `(customer)/menu` và `(customer)/delivery`.
  - Tích hợp Zustand `useCartStore`, SignalR client nhận thông báo đơn sẵn sàng, Widget AI Chatbot.
- 💻 **FE 2 (Operations & Dashboards):**
  - Xây dựng giao diện Web POS Quầy `(staff)/pos`, Chấm công `(staff)/attendance` và KDS Bếp `(kds)/kitchen`.
  - Xây dựng Dashboard Quản lý `(manager)/branch-dashboard` và Chuỗi `(admin)/admin-dashboard`.

---

## 6. BẢN ĐỒ THƯ MỤC MÃ NGUỒN (PROJECT STRUCTURE)

```
Idea_DoAn/
├── backend/                             # .NET 8 Clean Architecture Solution
│   ├── SmartFB.slnx                     # Solution file
│   ├── src/
│   │   ├── SmartFB.Domain/              # Thực thể 25 bảng 3NF, Enums, BaseEntity, IAggregateRoot
│   │   ├── SmartFB.Application/         # CQRS MediatR, DTOs, FluentValidation, Exceptions, Behaviors
│   │   ├── SmartFB.Infrastructure/      # EF Core 8 DbContext, Npgsql PostgreSQL, Redis Cache & Lock
│   │   └── SmartFB.API/                 # REST Controllers, 4 Hubs SignalR, JWT Auth, Swagger, Middleware
│   └── tests/
│       ├── SmartFB.UnitTests/           # xUnit & FluentAssertions Unit Tests
│       └── SmartFB.IntegrationTests/    # WebApplicationFactory Integration Tests
│
├── frontend/                            # Next.js 14 App Router Monorepo
│   ├── package.json                     # Next.js 14, React 18, Tailwind, Zustand, Lucide, SignalR
│   ├── tsconfig.json                    # TypeScript strict mode
│   ├── tailwind.config.ts               # Tailwind CSS theme
│   └── src/
│       ├── app/                         # 5 Route Groups: (customer), (kds), (staff), (manager), (admin)
│       ├── components/                  # UI Components dùng chung
│       ├── lib/                         # api-client.ts, signalr.ts, utils.ts
│       ├── stores/                      # useAuthStore.ts, useCartStore.ts, usePosStore.ts
│       └── types/                       # Shared TypeScript interfaces & types
│
├── scripts/                             # Scripts khởi động tự động
│   ├── init-db.sql                      # Kích hoạt uuid-ossp, pg_trgm
│   ├── start-dev-db.ps1                 # Script bật database trên PowerShell
│   └── start-dev-db.sh                  # Script bật database trên Linux/Mac
│
├── nginx/
│   └── nginx.conf                       # Reverse Proxy, SSL, WebSocket & Rate Limiting config
│
├── docker-compose.dev.yml               # PostgreSQL 16 + Redis 7 + pgAdmin 4 cho Local Dev
├── docker-compose.yml                   # Cấu hình Full Deployment Production
├── .editorconfig                        # Chuẩn format mã nguồn C# & TypeScript
├── .env.example                         # Biến môi trường mẫu
├── .gitignore                           # Loại bỏ file nhạy cảm và build artifacts
└── DEVELOPER_ONBOARDING.md              # Tài liệu hướng dẫn onboarding (Tệp này)
```

---

## 7. QUY TẮC PHÂN CHIA CÔNG VIỆC & NHÁNH TÍNH NĂNG (GITFLOW)

Khi bắt đầu code một tính năng cụ thể trong Sprint, các thành viên tạo nhánh mới từ nhánh phát triển theo quy tắc:

```bash
# Tạo nhánh tính năng Backend
git checkout -b feature/be-order-engine feature/infrastructure-setup

# Tạo nhánh tính năng Frontend
git checkout -b feature/fe-customer-pwa feature/infrastructure-setup
```

### Chuẩn Commit Message (Conventional Commits):
- `feat(order): add create dine-in order command with fluent validation`
- `feat(kds): connect kitchen hub and render active orders`
- `fix(auth): correct jwt token expiration calculation`
- `test(order): add unit tests for dine-in cash payment branch`
