# -*- coding: utf-8 -*-
"""
Generator for Git_Workflow_&_Branching_Strategy.md
100% Full Content, Zero Placeholders, 4-Member Team Ownership Matrix, Rebase Protocol, PR Checklist, Full .env.example
"""
import os

target = r'd:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md'
os.makedirs(os.path.dirname(target), exist_ok=True)

content = """# 🌿 QUY CHUẨN MÃ NGUỒN, CHIẾN LƯỢC NHÁNH GIT & CHECKLIST PULL REQUEST
## HỆ THỐNG QUẢN LÝ VÀ VẬN HÀNH QUÁN CÀ PHÊ THÔNG MINH SMART F&B OS

> **Phiên bản:** v2.0.0 (Production Grade & Formal Capstone Defense)  
> **Áp dụng cho:** Đội ngũ phát triển 4 thành viên (2 Backend Engineers + 2 Frontend Engineers)  
> **Công nghệ chủ đạo:** .NET 8 (Clean Architecture) | Next.js 14 (App Router & Tailwind CSS) | PostgreSQL 16 | Redis 7  
> **Tài liệu tham chiếu:** `PROJECT.md`, `technical_contracts.md`, `Smart_FB_OS_Revised_4members.docx`  
> **Mục tiêu:** Thiết lập quy trình phát triển phần mềm chuẩn mực doanh nghiệp, phân định quyền sở hữu mã nguồn (Code Ownership), quy tắc đặt tên nhánh/commit và hàng rào kiểm soát chất lượng (Quality Gates) ngăn chặn 100% xung đột mã nguồn.

---

## 📑 MỤC LỤC

1. [QUY CHUẨN LẬP TRÌNH & KIẾN TRÚC MÃ NGUỒN (CODING CONVENTIONS)](#1-quy-chuẩn-lập-trình--kiến-trúc-mã-nguồn-coding-conventions)
   - [1.1 Backend .NET 8 C# Standards](#11-backend-net-8-c-standards)
   - [1.2 Frontend Next.js 14 / TypeScript Standards (Web Only)](#12-frontend-nextjs-14--typescript-standards-web-only)
2. [MA TRẬN PHÂN CHIA TRÁCH NHIỆM & CODE OWNERSHIP (4 DEVS)](#2-ma-trận-phân-chia-trách-nhiệm--code-ownership-4-devs)
3. [CHIẾN LƯỢC NHÁNH GIT (GITFLOW FOR 4-MEMBER TEAM)](#3-chiến-lược-nhánh-git-gitflow-for-4-member-team)
   - [3.1 Cấu trúc Phân tầng Nhánh (Branch Hierarchy)](#31-cấu-trúc-phân-tầng-nhánh-branch-hierarchy)
   - [3.2 Quy tắc Bảo vệ Nhánh (Branch Protection Rules)](#32-quy-tắc-bảo-vệ-nhánh-branch-protection-rules)
   - [3.3 Quy trình Đồng bộ & Xử lý Xung đột bằng Git Rebase](#33-quy-trình-đồng-bộ--xử-lý-xung-đột-bằng-git-rebase)
4. [QUY CHUẨN CONVENTIONAL COMMITS 1.0.0 & CÁC VÍ DỤ THỰC TẾ](#4-quy-chuẩn-conventional-commits-100--các-ví-dụ-thực-tế)
5. [MẪU PULL REQUEST & HÀNG RÀO KIỂM DUYỆT (PR QUALITY GATES)](#5-mẫu-pull-request--hàng-rào-kiểm-duyệt-pr-quality-gates)
6. [TÀI LIỆU CẤU HÌNH BIẾN MÔI TRƯỜNG TOÀN DIỆN (.ENV.EXAMPLE)](#6-tài-liệu-cấu-hình-biến-môi-trường-toàn-diện-envexample)

---

## 1. QUY CHUẨN LẬP TRÌNH & KIẾN TRÚC MÃ NGUỒN (CODING CONVENTIONS)

### 1.1 Backend .NET 8 C# Standards
- **Quy tắc Đặt tên (Naming Rules)**:
  * Classes, Interfaces, Records, Enums, Public Methods, Properties: `PascalCase` (vd: `CreateOrderCommandHandler`, `IOrderRepository`).
  * Private Fields: `_camelCase` (vd: `_dbContext`, `_logger`, `_mediator`).
  * Parameters, Local Variables: `camelCase` (vd: `orderId`, `branchWifiConfig`).
  * Async Methods: Bắt buộc có hậu tố `Async` (vd: `GetActiveOrdersAsync`, `ProcessVietQrWebhookAsync`).
  * Constants: `UPPER_SNAKE_CASE` hoặc `PascalCase` (vd: `DEFAULT_DELIVERY_FEE = 20000.00m`).
- **Clean Architecture Layers**:
  * `Domain`: Chứa Entities, Value Objects, Enums, Domain Events (Không phụ thuộc bất kỳ thư viện ngoài nào).
  * `Application`: Chứa CQRS Commands/Queries, MediatR Handlers, DTOs, FluentValidation, Interfaces.
  * `Infrastructure`: Chứa PostgreSQL EF Core DbContext, Redis Cache, SignalR Hubs, PayOS Client, Gemini AI Client.
  * `WebApi`: Chứa Controllers, Minimal APIs, Middlewares, Swagger OpenAPI 3.1 configuration.
- **Xử lý Ngoại lệ (Exception & Result Pattern)**:
  * Trả về kết quả theo cấu trúc `Result<T>` hoặc RFC 7807 `ProblemDetails` chuẩn RESTful.
  * Nghiêm cấm bọc `try-catch` rỗng nuốt lỗi (`catch (Exception) {}`).

### 1.2 Frontend Next.js 14 / TypeScript Standards (Web Only)
- **Quy tắc Đặt tên (Naming Rules)**:
  * React Components, Pages: `PascalCase` (vd: `DineInCartModal.tsx`, `KdsTicketCard.tsx`).
  * Custom Hooks: `useCamelCase` (vd: `useSignalRKitchenHub.ts`, `useOrderCartStore.ts`).
  * Utility Files, Helpers: `kebab-case.ts` (vd: `format-currency.ts`, `vietqr-generator.ts`).
  * State Stores: Zustand Slices đặt trong `/stores` (vd: `useCartStore.ts`, `useAuthStore.ts`).
- **Kiến trúc Responsive Web Portals (Loại bỏ Mobile App)**:
  * `(customer)`: Customer PWA Responsive cho Khách quét QR Bàn / QR Delivery.
  * `(staff)`: Quầy Thu Ngân Web POS `/staff/pos` & Chấm công `/staff/attendance`.
  * `(kds)`: Bảng Điều phối Bếp `/kds` với SignalR WebSocket.
  * `(manager)`: Quản lý Ca, Đối soát két tiền, Menu `/manager`.
  * `(admin)`: Quản trị Toàn chuỗi, Báo cáo P&L, Cấu hình WiFi `/admin`.

---

## 2. MA TRẬN PHÂN CHIA TRÁCH NHIỆM & CODE OWNERSHIP (4 DEVS)

Để đảm bảo tốc độ phát triển song song không bị nghẽn (bottleneck) và không xung đột mã nguồn, dự án phân chia quyền sở hữu module rõ ràng cho 4 kỹ sư:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        MA TRẬN PHÂN CHIA CODE OWNERSHIP (4 KỸ SƯ CAPSTONE)                             │
├──────────────────────┬────────────────────────────────────────────┬────────────────────────────────────┤
│ THÀNH VIÊN           │ PHẠM VI TRÁCH NHIỆM CHÍNH (OWNERSHIP)     │ MODULES & REPOSITORY PATHS         │
├──────────────────────┼────────────────────────────────────────────┼────────────────────────────────────┤
│                      │ • Core Domain & Database Entities          │ `src/Domain/*`                     │
│ 👨‍💻 **BE-1**           │ • PostgreSQL Migrations & Seeding          │ `src/Infrastructure/Persistence/*` │
│ (Backend Lead)       │ • Đơn hàng (Dine-in, Takeaway, Delivery)   │ `src/Application/Orders/*`         │
│                      │ • Tích hợp Thanh toán VietQR / PayOS       │ `src/Infrastructure/Payments/*`    │
│                      │ • Định lượng món & Tồn kho (BOM Recipe)    │ `src/Application/Inventory/*`      │
├──────────────────────┼────────────────────────────────────────────┼────────────────────────────────────┤
│                      │ • Identity, JWT Auth & Phân quyền RBAC     │ `src/Infrastructure/Identity/*`    │
│ 👨‍💻 **BE-2**           │ • Chấm công WiFi BSSID/IP Subnet           │ `src/Application/Attendance/*`     │
│ (Backend Specialist) │ • SignalR Real-time Hubs (Kitchen, Pay)    │ `src/Infrastructure/SignalR/*`     │
│                      │ • Quản lý Ca & Đối soát Két tiền           │ `src/Application/Shifts/*`         │
│                      │ • AI-1 Chatbot & AI-2 Apriori Combo Engine │ `src/Infrastructure/AI/*`          │
├──────────────────────┼────────────────────────────────────────────┼────────────────────────────────────┤
│                      │ • Customer PWA (Quét QR Bàn Dine-in)       │ `src/app/(customer)/table/*`       │
│ 👩‍💻 **FE-1**           │ • Customer PWA (Quét QR Delivery 20K Ship) │ `src/app/(customer)/delivery/*`    │
│ (Frontend Lead)      │ • Web KDS Điều phối Bếp Real-time          │ `src/app/(kds)/*`                  │
│                      │ • Khung Chatbot AI-1 & RAG Catalog Client  │ `src/components/chatbot/*`         │
│                      │ • Shared UI Components & Design Tokens     │ `src/components/ui/*`              │
├──────────────────────┼────────────────────────────────────────────┼────────────────────────────────────┤
│                      │ • Web POS Thu Ngân & CRM Tra Cứu SĐT       │ `src/app/(staff)/pos/*`            │
│ 👨‍💻 **FE-2**           │ • Đổi Thưởng 10 Ly Miễn Phí & Tính Tiền    │ `src/app/(staff)/pos/loyalty/*`    │
│ (Frontend Engineer)  │ • Web Chấm Công Khóa WiFi Chi Nhánh        │ `src/app/(staff)/attendance/*`     │
│                      │ • Web Manager Mở/Đóng Ca & Két Tiền        │ `src/app/(manager)/*`              │
│                      │ • Web Admin Dashboard Báo Cáo P&L          │ `src/app/(admin)/*`                │
└──────────────────────┴────────────────────────────────────────────┴────────────────────────────────────┘
```

---

## 3. CHIẾN LƯỢC NHÁNH GIT (GITFLOW FOR 4-MEMBER TEAM)

### 3.1 Cấu trúc Phân tầng Nhánh (Branch Hierarchy)

```
main (Production Release - Protected)
 │
 ├── release/v2.0.0 (Release Candidate Stabilization)
 │
 ├── staging (Demo / UAT Testing Environment)
 │    │
 └── develop (Main Integration Branch - Protected)
      │
      ├── feature/be1/ORD-101-dinein-prepay-flow
      ├── feature/be2/ATT-202-wifi-locked-attendance
      ├── feature/fe1/KDS-303-realtime-signalr-board
      ├── feature/fe2/POS-404-staff-counter-loyalty-10cups
      ├── bugfix/BUG-505-fix-delivery-address-whitespace
      └── hotfix/HOT-901-fix-payos-webhook-timeout
```

- `main`: Nhánh triển khai Production, chỉ chứa mã nguồn đã nghiệm thu UAT đạt 100%. Cấm push trực tiếp.
- `staging`: Nhánh phục vụ chạy bản Demo Hội đồng và kiểm thử nghiệm thu người dùng (UAT).
- `develop`: Nhánh tích hợp chính của cả 4 thành viên. Mọi tính năng sau khi test xong đều merge vào đây.
- `feature/{dev}/{ticket-id}-{desc}`: Nhánh phát triển tính năng mới. Tách từ `develop` và merge lại vào `develop`.
- `bugfix/{ticket-id}-{desc}`: Nhánh sửa lỗi phát hiện trong quá trình kiểm thử trên `develop`.
- `hotfix/{ticket-id}-{desc}`: Nhánh sửa lỗi khẩn cấp phát sinh trên `main`.

### 3.2 Quy tắc Bảo vệ Nhánh (Branch Protection Rules)
Cấu hình trên GitHub Repository Settings:
1. **Require Pull Request before merging**: Bắt buộc tạo PR, cấm `git push --force` hoặc direct commit vào `main` và `develop`.
2. **Require Approvals**: Tối thiểu **1 Approval** từ thành viên cùng chuyên môn (BE review BE, FE review FE) và **1 Approval** từ Lead.
3. **Require Status Checks to Pass**:
   - Backend CI: `dotnet build` (Exit Code 0) + `dotnet test` (100% Unit/Integration tests Passed).
   - Frontend CI: `npm run lint` (0 ESLint errors) + `npm run build` (Next.js build compilation passed).
4. **Require Linear History & Squash Merge**: Bắt buộc Squash and Merge đối với các nhánh `feature/*` để giữ lịch sử Git rõ ràng.

### 3.3 Quy trình Đồng bộ & Xử lý Xung đột bằng Git Rebase

Tuyệt đối **KHÔNG dùng `git merge develop`** vào nhánh feature vì gây rác lịch sử commit. Bắt buộc dùng `git rebase`:

```bash
# Bước 1: Lưu tạm các thay đổi đang dở dang (nếu có)
git stash

# Bước 2: Chuyển về nhánh develop và kéo mã nguồn mới nhất
git checkout develop
git pull origin develop

# Bước 3: Quay lại nhánh feature của mình
git checkout feature/be1/ORD-101-dinein-prepay-flow

# Bước 4: Thực hiện Rebase nhánh feature trên nền develop mới nhất
git rebase develop

# Bước 5: Nếu có xung đột (Conflict):
# - Mở VS Code kiểm tra từng file xung đột, chọn Accept Current / Incoming Change
# - Sau khi xử lý xong, đánh dấu file:
git add <file-da-fix>
# - Tiếp tục rebase:
git rebase --continue
# (Tuyệt đối không chạy git commit trong quá trình rebase)

# Bước 6: Phục hồi stash (nếu có)
git stash pop

# Bước 7: Chạy build & test cục bộ xác nhận 100% pass
dotnet test # hoặc npm run test

# Bước 8: Push lên remote với --force-with-lease (an toàn hơn --force)
git push origin feature/be1/ORD-101-dinein-prepay-flow --force-with-lease
```

---

## 4. QUY CHUẨN CONVENTIONAL COMMITS 1.0.0 & CÁC VÍ DỤ THỰC TẾ

Cấu trúc Commit Message chuẩn:
```
<type>(<scope>): <mô tả ngắn gọn bằng tiếng Anh hoặc tiếng Việt rõ nghĩa>

[optional body: mô tả chi tiết lý do và giải pháp]

[optional footer: Closes #issue-id, BREAKING CHANGE: ...]
```

### 4.1 Bảng 10 Commit Types Được Phép Sử Dụng
| Type | Ý nghĩa & Phạm vi áp dụng |
|---|---|
| `feat` | Thêm tính năng hoặc luồng nghiệp vụ mới |
| `fix` | Sửa lỗi logic hoặc bug kỹ thuật |
| `docs` | Thêm hoặc sửa tài liệu kỹ thuật, markdown |
| `style` | Định dạng lại code, format prettier, không đổi logic |
| `refactor` | Tái cấu trúc mã nguồn (không thêm tính năng, không sửa bug) |
| `perf` | Tối ưu hóa hiệu năng, giảm thời gian phản hồi, tối ưu query |
| `test` | Thêm mới hoặc cải thiện unit test, integration test |
| `build` | Thay đổi cấu hình build, dependencies NuGet / npm |
| `ci` | Thay đổi cấu hình CI/CD pipeline (GitHub Actions) |
| `chore` | Các công việc bảo trì định kỳ, cập nhật cấu hình nhỏ |

### 4.2 Danh sách Scopes Hợp lệ trong Smart F&B OS
`auth`, `menu`, `order`, `payment`, `attendance`, `kds`, `pos`, `crm`, `shift`, `ai`, `db`, `infra`.

### 4.3 15 Ví dụ Thực tế Cho Dự Án Smart F&B OS
1. `feat(order): implement dine-in pre-payment flow with pending payment status`
2. `feat(payment): integrate VietQR PayOS webhook with HMAC-SHA256 signature verification`
3. `feat(delivery): enforce mandatory phone and address with flat 20k shipping fee`
4. `feat(pos): implement takeaway staff order with phone CRM lookup and 10-cup loyalty`
5. `feat(attendance): add 2-layer verification using branch wifi BSSID and subnet IP`
6. `feat(kds): connect kitchen screen to SignalR KitchenHub for real-time ticket updates`
7. `feat(ai): integrate Google Gemini 1.5 Flash for contextual drink recommendation`
8. `feat(ai): implement Apriori algorithm for automated combo rule mining`
9. `fix(shift): correct cash variance calculation when closing drawer with expense logs`
10. `fix(order): prevent KDS ticket broadcast before payment confirmation webhook`
11. `perf(db): add composite index on orders(branch_id, status) for KDS speedup`
12. `refactor(web): remove deprecated mobile app artifacts and consolidate into Next.js portals`
13. `test(attendance): add unit tests for wifi locked check-in with invalid BSSID`
14. `docs(uat): update 35 UAT test cases reflecting pure web architecture`
15. `feat(order)!: deprecate post-payment dine-in flow and require 100% pre-payment`

---

## 5. MẪU PULL REQUEST & HÀNG RÀO KIỂM DUYỆT (PR QUALITY GATES)

Mọi Pull Request tạo vào nhánh `develop` hoặc `main` phải tuân theo mẫu `.github/pull_request_template.md`:

```markdown
## 📌 Tóm tắt Thay đổi (Summary)
- Mô tả ngắn gọn: [vd: Bổ sung logic tính phí ship 20.000 VNĐ cố định cho đơn QR Delivery]
- Module liên quan: `Orders / Delivery`
- Liên kết Ticket / User Story: Closes #DEL-102

## 🛠️ Loại Thay đổi (Type of Change)
- [x] `feat`: Tính năng mới
- [ ] `fix`: Sửa lỗi
- [ ] `refactor`: Tái cấu trúc
- [ ] `perf`: Tối ưu hiệu năng
- [ ] `test`: Bổ sung kiểm thử

## 📋 Tự Kiểm Tra Trước Khi Gửi PR (Author Self-Checklist)
- [x] Đã chạy `git rebase develop` và giải quyết 100% conflicts.
- [x] Đã đọc lại toàn bộ code diff trên VS Code / GitHub.
- [x] Đã chạy `dotnet test` hoặc `npm run test` - Toàn bộ tests đều PASS.
- [x] Không để lại mã nguồn khung, mã nguồn lười hoặc đánh dấu giữ chỗ chưa hoàn thiện.
- [x] Không hardcode secret keys, passwords, hoặc API keys trong mã nguồn.
- [x] Đã bổ sung Unit Test bao phủ các trường hợp biên (Null, Empty, Timeout).

## 🔍 Checklist Dành Cho Reviewer (Reviewer Gate)
- [ ] Code tuân thủ đúng Clean Architecture và Coding Standards.
- [ ] Không có nguy cơ rò rỉ bộ nhớ hoặc N+1 Query.
- [ ] Các thay đổi DB đều có Migration script đồng bộ.
- [ ] Xác nhận đã kiểm chứng thực tế trên môi trường staging.
```

---

## 6. TÀI LIỆU CẤU HÌNH BIẾN MÔI TRƯỜNG TOÀN DIỆN (.ENV.EXAMPLE)

### 6.1 Backend Configuration (`appsettings.json` / `.env`)
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Host=localhost;Port=5432;Database=smartfb_db;Username=postgres;Password=YourSecurePassword123;Pooling=true;Minimum Pool Size=5;Maximum Pool Size=50;",
    "RedisConnection": "localhost:6379,password=RedisPassword123,ssl=False,abortConnect=False"
  },
  "JwtSettings": {
    "Secret": "SmartFB_Super_Secret_Key_For_JWT_Authentication_2026_Minimum_32_Chars!",
    "Issuer": "https://api.smartfb.vn",
    "Audience": "https://smartfb.vn",
    "AccessTokenExpirationMinutes": 60,
    "RefreshTokenExpirationDays": 7
  },
  "VietQrPayOS": {
    "ClientId": "your-payos-client-id-here",
    "ApiKey": "your-payos-api-key-here",
    "ChecksumKey": "your-payos-checksum-hmac-sha256-key",
    "WebhookUrl": "https://api.smartfb.vn/api/v1/payments/vietqr/webhook",
    "ReturnUrl": "https://smartfb.vn/payment-success",
    "CancelUrl": "https://smartfb.vn/payment-cancelled"
  },
  "BusinessRules": {
    "DefaultDeliveryFee": 20000.0,
    "PaymentTimeoutMinutes": 10,
    "LoyaltyCupsForFreeDrink": 10,
    "FreeDrinkMaxDiscount": 35000.0
  },
  "GoogleGemini": {
    "ApiKey": "AIzaSyYourGeminiApiKeyHere123456789",
    "ModelName": "gemini-1.5-flash",
    "TimeoutSeconds": 3.0
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.EntityFrameworkCore.Database.Command": "Warning"
    }
  }
}
```

### 6.2 Frontend Configuration (`.env.local.example`)
```bash
# NEXT.JS FRONTEND ENVIRONMENT VARIABLES

# API Gateway Endpoint
NEXT_PUBLIC_API_URL=https://api.smartfb.vn/api/v1
NEXT_PUBLIC_SIGNALR_KITCHEN_HUB_URL=https://api.smartfb.vn/hubs/kitchen
NEXT_PUBLIC_SIGNALR_PAYMENT_HUB_URL=https://api.smartfb.vn/hubs/payment

# App Domain
NEXT_PUBLIC_APP_DOMAIN=https://smartfb.vn

# Static Assets CDN
NEXT_PUBLIC_CDN_URL=https://cdn.smartfb.vn

# Feature Flags
NEXT_PUBLIC_ENABLE_AI_CHATBOT=true
NEXT_PUBLIC_ENABLE_VIETQR_PREPAY=true
NEXT_PUBLIC_DEFAULT_DELIVERY_FEE=20000
```
"""

with open(target, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {target} with size: {os.path.getsize(target)} bytes")
