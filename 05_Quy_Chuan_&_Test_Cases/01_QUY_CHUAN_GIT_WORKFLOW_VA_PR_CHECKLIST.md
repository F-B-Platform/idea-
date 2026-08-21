# 📘 QUY CHUẨN GIT WORKFLOW, CODING STANDARDS VÀ CHECKLIST PULL REQUEST
## HỆ THỐNG QUẢN LÝ VÀ VẬN HÀNH CHUỖI NHÀ HÀNG SMART F&B OPERATING SYSTEM

---

## 1. QUY CHUẨN ĐẶT TÊN VÀ CODING STANDARDS (.NET 8 & NEXT.JS 14)

### 1.1 Backend .NET 8 (C#) Standards
Hệ thống Backend được phát triển trên nền tảng .NET 8 C# áp dụng kiến trúc Clean Architecture. Toàn bộ mã nguồn phải tuân thủ nghiêm ngặt các quy tắc đặt tên sau:

- **Classes, Structs, Enums**: Sử dụng định dạng `PascalCase`.
  - *Ví dụ*: `OrderService`, `OrderStatus`, `PaymentType`, `TableSession`, `RestaurantDbContext`, `CustomerFeedback`.
- **Interfaces**: Sử dụng tiền tố `I` kết hợp với `PascalCase`.
  - *Ví dụ*: `IOrderRepository`, `IPaymentGatewayService`, `ISignalRNotificationService`, `IAuthService`, `IKitchenDisplayService`.
- **Async Methods**: Sử dụng `PascalCase` và bắt buộc có hậu tố `Async`.
  - *Ví dụ*: `GetOrderByIdAsync`, `CreatePaymentTransactionAsync`, `UpdateTableStatusAsync`, `BroadcastOrderStatusAsync`, `ProcessRefundAsync`.
- **Private Fields**: Sử dụng tiền tố gạch dưới `_` kết hợp `camelCase`.
  - *Ví dụ*: `_dbContext`, `_logger`, `_configuration`, `_hubContext`, `_redisCache`, `_httpClientFactory`.
- **Local Variables & Parameters**: Sử dụng định dạng `camelCase`.
  - *Ví dụ*: `orderId`, `customerPhone`, `totalAmount`, `paymentCallbackPayload`, `tableSessionId`, `itemQuantity`.
- **Data Transfer Objects (DTOs)**: Sử dụng tên Entity hoặc Hành động kết hợp hậu tố `Dto`.
  - *Ví dụ*: `CreateOrderDto`, `OrderResponseDto`, `UpdateTableStatusDto`, `PaymentCallbackDto`, `KdsOrderStatusUpdateDto`.
- **Constants (Hằng số)**: Sử dụng định dạng `PascalCase` cho class constants hoặc `UPPER_SNAKE_CASE` cho enum-like values.
  - *Ví dụ*: `MaxRetryAttempts`, `DEFAULT_PAGE_SIZE`, `JwtClaims.UserId`, `CacheKeys.MENU_CATALOG`.

### 1.2 Frontend Next.js 14 & TypeScript Standards
Hệ thống Frontend bao gồm ứng dụng QR Menu PWA, Kitchen Display System (KDS), Staff Mobile App và Admin Dashboard được xây dựng trên Next.js 14 App Router và React/TypeScript.

- **Components & Component Folders**: Sử dụng định dạng `PascalCase`.
  - *Ví dụ*: `MenuCard.tsx`, `CartDrawer.tsx`, `KdsOrderGrid.tsx`, `PaymentQrModal.tsx`, `TableStatusBadge.tsx`.
- **App Router Pages & Layouts**: Sử dụng tên file mặc định chuẩn của Next.js App Router.
  - *Ví dụ*: `app/(customer)/menu/page.tsx`, `app/(kitchen)/kds/page.tsx`, `app/layout.tsx`, `app/loading.tsx`, `app/error.tsx`.
- **Custom Hooks**: Sử dụng tiền tố `use` kết hợp `PascalCase`.
  - *Ví dụ*: `useCartStore.ts`, `useSignalRHub.ts`, `useOrderNotification.ts`, `useSunmiPrinter.ts`, `useTableSession.ts`.
- **Utility / Helper Files**: Sử dụng định dạng `kebab-case.ts`.
  - *Ví dụ*: `format-currency.ts`, `api-client.ts`, `date-utils.ts`, `signalr-connection-builder.ts`, `vietqr-generator.ts`.
- **Interfaces & Types**: Sử dụng định dạng `PascalCase` (KHÔNG sử dụng tiền tố `I`).
  - *Ví dụ*: `CartItem`, `OrderResponse`, `PaymentStatus`, `TableState`, `KdsItemStatus`, `UserProfile`.
- **CSS Variables & Design Tokens**: Sử dụng định dạng `kebab-case`.
  - *Ví dụ*: `--brand-primary-500`, `--surface-dark`, `--status-cooking`, `--status-ready`, `--text-secondary`.

---

## 2. CHIẾN LƯỢC GITFLOW CHO TEAM 4 LẬP TRÌNH VIÊN

### 2.1 Team Ownership Matrix (Phân Công Trách Nhiệm)
Đội ngũ kĩ thuật bao gồm 4 lập trình viên chính (2 Backend + 2 Frontend) được phân chia phạm vi sở hữu mã nguồn như sau:

1. **BE-Dev-1 (Backend Core & Database Lead)**:
   - Quản lý PostgreSQL Database, Entity Framework Core Mappings và Migration Scripts.
   - Phát triển Core Domain Modules: Order Management API, Menu Catalog API, Table Session API, Payment Gateway Integrations (VietQR, PayOS).
2. **BE-Dev-2 (Backend Real-time & Security Developer)**:
   - Phát triển Authentication & Authorization Engine (JWT Tokens, Refresh Token Rotation, RBAC Middleware).
   - Quản lý và xây dựng hệ thống SignalR Hubs (`OrderHub`, `KitchenHub`, `NotificationHub`, `TableHub`).
   - Xây dựng KDS Backend APIs, Inventory Management APIs và Background Job Processing.
3. **FE-Dev-1 (Frontend Customer & Kitchen Specialist)**:
   - Phát triển ứng dụng Web QR Menu PWA phục vụ khách hàng gọi món tại bàn.
   - Phát triển ứng dụng KDS (Kitchen Display System) phục vụ điều phối làm món tại khu vực bếp.
4. **FE-Dev-2 (Frontend Mobile POS & Admin Dashboard Specialist)**:
   - Phát triển ứng dụng Staff Mobile App (dành cho nhân viên phục vụ bàn).
   - Phát triển ứng dụng Sunmi POS App (tích hợp máy in nhiệt cầm tay Sunmi).
   - Phát triển ứng dụng Quản lý Admin & Manager Dashboard (Next.js 14 App Router).

### 2.2 Branch Hierarchy (Cấu Trúc Nhánh Git)

- **`main`**: Nhánh mã nguồn chính thức đã kiểm thử sẵn sàng phát hành Production. Nhánh này được bảo vệ nghiêm ngặt (Strictly Protected). Cấm mọi thao tác commit trực tiếp. Chỉ cho phép merge thông qua Pull Request có tối thiểu 2 Approvals và kết quả CI Build vượt qua 100%.
- **`staging`**: Nhánh môi trường tiền phát hành (Pre-production). Được tự động deploy lên Staging VPS để phục vụ kiểm thử tích hợp (UAT) trước khi release.
- **`develop`**: Nhánh tích hợp trung tâm dành cho hoạt động phát triển hằng ngày. Tất cả tính năng mới hoàn thành sẽ được merge vào đây. Nhánh này là nguồn để chạy Nightly Builds.
- **`feature/<scope>-<description>`**: Nhánh phát triển tính năng mới. Được tạo ra từ `develop`.
  - *Ví dụ*: `feature/backend-order-api`, `feature/frontend-kds-grid`, `feature/mobile-pos-checkout`, `feature/signalr-hub-reconnect`.
- **`bugfix/<issue-id>-<description>`**: Nhánh sửa lỗi phát sinh trong sprint phát triển. Được tạo ra từ `develop`.
  - *Ví dụ*: `bugfix/FNB-102-fix-cart-calculation`, `bugfix/FNB-204-fix-signalr-reconnect`, `bugfix/FNB-305-fix-sunmi-printer-paper-cut`.
- **`hotfix/<version>-<description>`**: Nhánh sửa lỗi khẩn cấp phát sinh trên môi trường Production. Được tạo ra trực tiếp từ `main` và sau khi sửa xong phải được merge về cả `main` và `develop`.
  - *Ví dụ*: `hotfix/v1.0.1-fix-vietqr-callback`, `hotfix/v1.0.2-fix-jwt-token-expiration`.
- **`release/v<version>`**: Nhánh đóng đóng gói phục vụ kiểm thử regression trước khi đưa lên production.
  - *Ví dụ*: `release/v1.1.0`.
- **`chore/<description>`**: Nhánh thực hiện các công việc nâng cấp thư viện, cấu hình môi trường CI/CD.
  - *Ví dụ*: `chore/upgrade-dotnet-packages`, `chore/setup-docker-compose`.

### 2.3 Branch Protection Rules & Merge Strategy
- **Số lượng Reviewer tối thiểu**: Bắt buộc có tối thiểu **2 approvals** từ các thành viên trong team (1 Lead/Peer BE + 1 Peer FE hoặc QA) mới đủ điều kiện merge PR vào `develop` hoặc `main`.
- **Automated Status Checks**: PR bắt buộc phải vượt qua 100% các bước kiểm tra tự động trên GitHub Actions / CI Server (0 lỗi biên dịch, unit tests 100% pass, linter status clean).
- **Chiến lược Merge (Merge Strategy)**:
  - Cho nhánh `feature/*` -> `develop`: Bắt buộc sử dụng quy tắc **`Squash and Merge`**. Toàn bộ lịch sử commit ngắn của nhánh tính năng sẽ được gộp thành 1 commit duy nhất, giúp nhật ký tích hợp trên `develop` luôn phẳng và dễ truy vết.
  - Cho nhánh `release/*` -> `main` và `hotfix/*` -> `main`: Bắt buộc sử dụng quy tắc **`Merge Commit`** (no fast-forward) và phải đánh nhãn Tag phiên bản Semantic Versioning (ví dụ: `v1.0.0`).

### 2.4 Conflict Resolution Protocol (Giao Thức Xử Lý Xung Đột Code)
Khi xảy ra xung đột mã nguồn (merge conflict) giữa nhánh `feature` và nhánh `develop`, lập trình viên bắt buộc phải sử dụng phương pháp **Git Rebase** theo trình tự câu lệnh chuẩn như sau:

```bash
# Bước 1: Chuyển sang nhánh develop và cập nhật mã nguồn mới nhất từ remote server
git checkout develop
git pull origin develop

# Bước 2: Chuyển sang nhánh feature cần cập nhật
git checkout feature/backend-order-api

# Bước 3: Thực hiện Rebase nhánh feature dựa trên nền develop mới nhất
git rebase develop

# Bước 4: Kiểm tra các file bị xung đột mã nguồn bằng lệnh git status
git status

# Bước 5: Mở từng file xung đột trong Code Editor, giải quyết thủ công các khối code <<< HEAD và >>>
# Sau khi sửa xong xung đột của từng file, đánh dấu file đã giải quyết:
git add src/Backend/SmartFnB.Api/Controllers/OrderController.cs

# Bước 6: Tiếp tục quá trình rebase
git rebase --continue

# Lưu ý: Nếu còn xung đột ở các commit tiếp theo, lặp lại Bước 5 và Bước 6.
# Trường hợp muốn hủy bỏ quá trình rebase để quay lại trạng thái ban đầu: git rebase --abort

# Bước 7: Push nhánh feature đã rebase lên remote server bằng tham số force-with-lease (an toàn hơn -f)
git push --force-with-lease origin feature/backend-order-api
```

---

## 3. QUY ĐỊNH CONVENTIONAL COMMITS VÀ MẪU COMMIT CHUẨN

### 3.1 Cấu Trúc Commit Message Chuẩn
Mọi commit trong repository bắt buộc phải tuân thủ định dạng Conventional Commits 1.0.0:

```text
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### 3.2 Phân Loại Commit Types (10 Types Bắt Buộc)
1. **`feat`**: Thêm mới một tính năng, API endpoint hoặc thành phần giao diện.
2. **`fix`**: Sửa lỗi công năng, xử lý bug logic hoặc vá lỗ hổng bảo mật.
3. **`docs`**: Cập nhật tài liệu kỹ thuật, API docs (OpenAPI), README hoặc hướng dẫn setup.
4. **`style`**: Thay đổi về định dạng code, khoảng trắng, dấu chấm phẩy, format (không ảnh hưởng logic).
5. **`refactor`**: Tái cấu trúc code nhằm nâng cao chất lượng mà không làm thay đổi hành vi tính năng.
6. **`perf`**: Cải thiện hiệu năng xử lý, tối ưu câu lệnh SQL, truy vấn EF Core hoặc caching.
7. **`test`**: Bổ sung mới hoặc chỉnh sửa các bộ kịch bản Unit Test, Integration Test.
8. **`build`**: Thay đổi cấu hình build hệ thống hoặc cập nhật dependencies (`package.json`, `.csproj`).
9. **`ci`**: Thay đổi cấu hình quy trình CI/CD pipelines (`.github/workflows`, Dockerfile).
10. **`chore`**: Các công việc bảo trì định kỳ, cập nhật cấu hình môi trường, script phụ trợ.

### 3.3 Danh Sách Scopes Cho Phép (Allowed Scopes)
- **Backend Scopes**: `auth`, `order`, `kds`, `table`, `menu`, `payment`, `inventory`, `staff`, `analytics`, `signalr`, `db`, `config`.
- **Frontend Scopes**: `frontend-qr`, `frontend-kds`, `frontend-pos`, `mobile`, `shared`, `ui`, `state`, `api-client`.

### 3.4 Quy Định Breaking Changes
Khi commit chứa thay đổi phá vỡ tương thích ngược (Breaking Changes), bắt buộc thêm ký tự `!` ngay sau scope hoặc ghi rõ khối `BREAKING CHANGE:` tại phần footer của commit.
- *Ví dụ*: `feat(api-client)!: refactor order response structure to strictly follow RFC 7807`

### 3.5 Danh Sách 15 Ví Dụ Commit Thực Tế Cụ Thể (Full Real-World Commit Examples)
1. `feat(order): add API POST /api/v1/orders to process QR ordering table sessions`
2. `fix(payment): resolve VietQR callback signature verification failed on duplicate webhooks`
3. `feat(kds): implement SignalR KitchenHub listener for realtime order item state change`
4. `refactor(auth): rewrite JWT token generator service to support refresh token rotation`
5. `perf(db): add composite index IX_Orders_RestaurantId_Status on Orders PostgreSQL table`
6. `docs(api): add complete OpenAPI 3.0 specs for menu catalog and pricing endpoints`
7. `style(frontend-qr): format Tailwind CSS utility classes in MenuCard component`
8. `test(order): add unit test suite for OrderService calculate total price logic`
9. `build(backend): update Microsoft.EntityFrameworkCore.Npgsql package to version 8.0.4`
10. `ci(github): add workflow step for automated dotnet build and test execution`
11. `chore(env): add Redis connection string default variables to .env.example`
12. `feat(frontend-pos): add offline draft order local storage caching mechanism`
13. `fix(signalr): reconnect automatic exponential backoff retry policy for KDS hub client`
14. `feat(mobile): integrate Sunmi inner printer SDK for instant bill printing on POS terminal`
15. `feat(inventory)!: change stock deduction endpoint payload structure to batch item updates`

---

## 4. QUY TRÌNH VÀ CHECKLIST DUYỆT PULL REQUEST (PR QUALITY GATES)

### 4.1 Định Dạng Tiêu Đề PR (PR Title Format)
Tiêu đề của Pull Request phải tuân thủ chuẩn Conventional Commits: `<type>(<scope>): <mô tả rõ ràng>`
- *Tiêu đề đúng*: `feat(payment): integrate PayOS payment gateway webhook handler`
- *Tiêu đề sai*: `fixed bug`, `update code`, `PR for order module`, `fix bug kds`

### 4.2 Template Mô Tả Pull Request (PR Description Template)

```markdown
## 📝 Summary
Brief description of changes made in this Pull Request.

## 🔗 Related Issues / Tasks
- Closes #FNB-102
- Fixes #FNB-145

## 🧪 Type of Change
- [ ] 🚀 New Feature
- [ ] 🐛 Bug Fix
- [ ] ♻️ Refactoring
- [ ] ⚡ Performance Optimization
- [ ] 📚 Documentation Update
- [ ] 🔧 Configuration / Chore

## 🔍 Pre-PR Author Checklist
- [ ] Code compiles cleanly with 0 compilation errors (`dotnet build` / `npm run build`).
- [ ] All unit tests and integration tests pass successfully (`dotnet test` / `npm test`).
- [ ] No hardcoded passwords, JWT secrets, database credentials, or private API keys.
- [ ] Removed all abandoned debug logs (`console.log`, `Console.WriteLine`, `Debugger`).
- [ ] Added new environment variables to `.env.example` with working local default values.
- [ ] Code strictly follows naming conventions for .NET 8 and Next.js 14.
- [ ] Branch is rebased onto the latest `develop` branch without merge conflicts.
- [ ] Self-reviewed code diff thoroughly before opening PR.
- [ ] PR Title follows Conventional Commits specification format.
- [ ] Linked relevant Jira issue / Task ticket ID in the description.

## 🛠️ Test Instructions & Evidence
1. Run `docker-compose up -d` to ensure PostgreSQL and Redis are running.
2. Execute `dotnet run` in `src/Backend/SmartFnB.Api`.
3. Call `POST /api/v1/orders` using Postman with payload attached below.
4. Verify response status HTTP 201 Created and SignalR event broadcasted to `KitchenHub`.
```

### 4.3 Quy Tắc Quality Gates & Duyệt PR Tự Động
1. **Tối thiểu 2 Approvals**: PR phải nhận được 2 lượt phê duyệt chính thức từ các thành viên trong team trước khi tính năng Merge được kích hoạt.
2. **Automated Pipeline Check**:
   - `dotnet build` / `npm run build`: Phải hoàn tất với 0 lỗi biên dịch.
   - `dotnet test` / `npm run test`: Phải vượt qua 100% số lượng test cases.
3. **Quy Tắc Nghiêm Cấm Zero Placeholders (Strict Zero Placeholder Enforcement)**:
   - Nghiêm cấm tuyệt đối mã nguồn dở dang chứa các ký tự giữ chỗ, ghi chú công việc dở dang, ký tự ba chấm rút gọn, biến chưa điền giá trị hoặc thông tin mật khẩu mẫu chưa thay thế.
   - Nếu reviewer phát hiện bất kỳ ký tự placeholder nào trong code diff, PR sẽ bị REJECT ngay lập tức mà không cần thỏa thuận.

### 4.4 Checklist Dành Cho Author (10 Điểm Kiểm Tra)
1. [ ] Code biên dịch 100% không có lỗi (`dotnet build` / `npm run build`).
2. [ ] Toàn bộ Unit Test và Integration Test đã vượt qua 100% (`dotnet test` / `npm test`).
3. [ ] Đã loại bỏ hoàn toàn các thông tin nhạy cảm (passwords, JWT secrets, connection strings).
4. [ ] Đã xóa các lệnh debug dở dang (`console.log`, `Debugger.Break()`, `System.Console.WriteLine`).
5. [ ] Đã cập nhật tất cả biến môi trường mới vào file `.env.example` với giá trị mặc định chạy được.
6. [ ] Tên biến, tên hàm, tên class tuân thủ đúng quy chuẩn .NET 8 / Next.js 14.
7. [ ] Đã rebase thành công nhánh làm việc trên nền nhánh `develop` mới nhất.
8. [ ] Đã tự mình review toàn bộ code diff (Self-Review) trước khi tạo PR.
9. [ ] Tiêu đề PR tuân thủ đúng định dạng Conventional Commits.
10. [ ] Đã gán thẻ Task ID / Issue ID tương ứng vào mô tả PR.

### 4.5 Checklist Dành Cho Reviewer (10 Điểm Kiểm Tra)
1. [ ] Kiến trúc code tuân thủ Clean Architecture và SoC (Separation of Concerns).
2. [ ] Bảo mật: Ngăn chặn triệt để SQL Injection, XSS và kiểm tra phân quyền RBAC/JWT thích hợp.
3. [ ] Hiệu năng: Sử dụng `async/await` hợp lý, không gặp lỗi N+1 Query trong truy vấn EF Core.
4. [ ] Xử lý lỗi: Mọi Exception được catch và trả về format chuẩn RFC 7807 `ProblemDetails`.
5. [ ] Real-time: Kết nối SignalR và sự kiện broadcast được quản lý bộ nhớ và reconnect đúng cách.
6. [ ] Validation: Có đầy đủ FluentValidation hoặc DataAnnotations cho dữ liệu đầu vào DTO.
7. [ ] Giao diện: Layout hiển thị chuẩn trên màn hình di động (PWA/POS) và desktop (Admin).
8. [ ] Accessibility (a11y): Đảm bảo độ tương phản WCAG AA và kích thước mảng cảm ứng ≥ 44px.
9. [ ] Tính đọc được & Không trùng lặp code (DRY - Don't Repeat Yourself).
10. [ ] Tài liệu: Đã cập nhật OpenAPI/Swagger specification nếu có thay đổi API contract.

---

## 5. COMPLETE ENVIRONMENT MATRIX VÀ MA TRẬN BIẾN MÔI TRƯỜNG (.ENV.EXAMPLE)

### 5.1 Full Environment Matrix Table (Ma Trận Cấu Hình 3 Môi Trường)

| Thành Phần Hệ Thống | Môi Trường Local Dev (Docker) | Môi Trường Staging VPS | Môi Trường Production Cloud |
| :--- | :--- | :--- | :--- |
| **API Gateway / URL Host** | `http://localhost:5000` | `https://staging-api.smartfnb.io` | `https://api.smartfnb.vn` |
| **Database Engine** | PostgreSQL 16 (Docker Container) | PostgreSQL 16 Managed VPS | PostgreSQL Managed Cluster (HA) |
| **Database Host & Port** | `localhost:5432` | `10.0.1.15:5432` | `db-cluster.internal.smartfnb.vn:5432` |
| **Cache Engine** | Redis 7.2 (Docker Container) | Redis 7.2 Container | Redis Cluster (Primary-Replica) |
| **Storage Engine** | MinIO Local S3 Container | MinIO Staging Server | Cloudinary / AWS S3 Standard |
| **Logging & Tracing** | Console & Local Seq (`localhost:5341`) | Seq Centralized Server | Seq Cluster + OpenTelemetry Datadog |
| **Payment Gateways** | Sandbox VietQR & PayOS Test Credentials | Staging Merchant Accounts | Production Verified Merchant Accounts |
| **SignalR Transport** | WebSockets / SSE | WebSockets với Nginx Reverse Proxy | Azure SignalR Service / Cluster |

### 5.2 Mẫu File Cấu Hình `.env.example` Hoàn Chỉnh (Zero Placeholders - Over 40 Real Variables)

```env
# ==============================================================================
# SMART F&B OPERATING SYSTEM - COMPLETE ENVIRONMENT TEMPLATE
# File: .env.example
# Target Tech Stack: .NET 8 Web API & Next.js 14 App Router
# Rule: Zero Placeholders. All keys have complete, realistic local dev defaults.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BACKEND SERVICE CONFIGURATION (.NET 8 WEB API)
# ------------------------------------------------------------------------------
ASPNETCORE_ENVIRONMENT=Development
PORT=5000
ASPNETCORE_URLS=http://+:5000

# Primary PostgreSQL Database Connection String
ConnectionStrings__DefaultConnection=Host=localhost;Port=5432;Database=smart_fnb_db;Username=postgres;Password=PostgresSecure2026!;Pooling=true;Minimum Pool Size=5;Maximum Pool Size=100;

# Fallback SQL Server Connection String (For Legacy Migration Support)
ConnectionStrings__SqlServerConnection=Server=localhost,1433;Database=SmartFnBDb;User Id=sa;Password=SqlServerSecure2026!;TrustServerCertificate=True;

# JWT Authentication & Token Security Configuration
Jwt__SecretKey=SuperSecretKeyForSmartFnBOperatingSystem2026SecureKeyMin256Bits!
Jwt__Issuer=https://api.smartfnb.local
Jwt__Audience=https://app.smartfnb.local
Jwt__AccessTokenExpirationMinutes=60
Jwt__RefreshTokenExpirationDays=7

# Distributed Cache Configuration (Redis)
Redis__ConnectionString=localhost:6379,password=RedisSecurePass2026!,abortConnect=false,connectTimeout=5000
Redis__InstanceName=SmartFnBCache_

# SignalR Real-Time WebSocket Hub Configuration
SignalR__EnableDetailedErrors=true
SignalR__KeepAliveIntervalSeconds=15
SignalR__ClientTimeoutIntervalSeconds=30

# Payment Gateway Integration - VietQR Specification
VietQR__BaseUrl=https://api.vietqr.io/v2
VietQR__ClientId=vietqr_client_demo_id_2026
VietQR__ApiKey=vietqr_api_key_secret_2026_x89f7
VietQR__BankId=970422
VietQR__AccountNo=19035678901018
VietQR__AccountName=SMART FNB SYSTEM

# Payment Gateway Integration - PayOS Specification
PayOS__ClientId=payos_client_id_demo_882
PayOS__ApiKey=payos_api_key_demo_secret_991
PayOS__ChecksumKey=payos_checksum_key_secret_2026

# Cloud Object Storage Configuration (Cloudinary / MinIO S3)
Cloudinary__CloudName=smartfnb-demo
Cloudinary__ApiKey=123456789012345
Cloudinary__ApiSecret=abcdefghijklmnopqrstuvwxyz12345
MinIO__Endpoint=localhost:9000
MinIO__AccessKey=minio_admin_local_2026
MinIO__SecretKey=minio_secret_pass_2026
MinIO__BucketName=smartfnb-assets

# Sunmi POS Hardware SDK Configuration
Sunmi__PrinterBaudRate=115200
Sunmi__PaperWidthMm=80
Sunmi__AutoCutPaper=true

# AI Recommendation Engine API Configuration
AiEngine__BaseUrl=https://api.openai.com/v1
AiEngine__ApiKey=sk-proj-demo-smart-fnb-ai-key-2026-secure-token-value
AiEngine__ModelName=gpt-4o-mini
AiEngine__TimeoutSeconds=30

# Centralized Logging & Diagnostic Configuration (Seq Server)
Seq__ServerUrl=http://localhost:5341
Seq__ApiKey=seq_api_key_local_dev_2026

# Cross-Origin Resource Sharing (CORS) Security Policies
Cors__AllowedOrigins=http://localhost:3000,http://localhost:3001,http://localhost:3002,https://app.smartfnb.local

# API Gateway Rate Limiting Policy
RateLimiting__PermitLimit=100
RateLimiting__WindowInSeconds=60

# ------------------------------------------------------------------------------
# 2. FRONTEND CLIENT CONFIGURATION (NEXT.JS 14 APP ROUTER)
# ------------------------------------------------------------------------------
# Next.js Application Server Port
NODE_ENV=development

# Base API Gateway Endpoint URL
NEXT_PUBLIC_API_BASE_URL=http://localhost:5000/api/v1

# Real-time SignalR WebSocket Endpoint URL
NEXT_PUBLIC_SIGNALR_HUB_URL=http://localhost:5000/hubs

# Public Application Metadata & Environment Identity
NEXT_PUBLIC_APP_NAME=Smart F&B Operating System
NEXT_PUBLIC_APP_ENV=development
NEXT_PUBLIC_DEFAULT_LOCALE=vi

# Public Security & Feature Toggles
NEXT_PUBLIC_ENABLE_ANALYTICS=false
NEXT_PUBLIC_MOCK_PAYMENT=true
```

---

## 6. HƯỚNG DẪN SETUP MÔI TRƯỜNG LOCAL VÀ DỌN DẸP FILE TÀI LIỆU CŨ

### 6.1 Hướng Dẫn Kích Hoạt Môi Trường Phát Triển Local (Local Setup Protocol)
Để khởi chạy toàn bộ hệ thống trên máy local của từng lập trình viên, thực hiện chính xác các bước sau:

1. **Clone mã nguồn từ Git Repository**:
   ```bash
   git clone https://github.com/smartfnb/smart-fnb-operating-system.git
   cd smart-fnb-operating-system
   ```
2. **Khởi tạo file cấu hình môi trường cá nhân**:
   ```bash
   cp .env.example .env
   ```
3. **Khởi chạy hạ tầng Infrastructure dịch vụ bằng Docker Compose**:
   ```bash
   docker-compose up -d postgres redis seq minio
   ```
4. **Khởi chạy Backend Service (.NET 8)**:
   ```bash
   cd src/Backend/SmartFnB.Api
   dotnet ef database update
   dotnet run
   ```
5. **Khởi chạy Frontend Web Apps (Next.js 14)**:
   ```bash
   cd src/Frontend/smart-fnb-web
   npm install
   npm run dev
   ```

### 6.2 File Migration & Cleanup Instructions
- Tài liệu quy chuẩn kỹ thuật chính thức và duy nhất của dự án được lưu tại đường dẫn:  
  `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md`
- File dở dang cũ tại đường dẫn:  
  `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md`  
  phải được cập nhật trỏ về file chính thức này hoặc xóa bỏ hoàn toàn nhằm tránh gây nhầm lẫn trong quá trình phát triển của team.
