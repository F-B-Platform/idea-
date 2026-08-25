# Original User Request

## Initial Request — 2026-08-25T02:32:54Z

You are the PROJECT ORCHESTRATOR for the Smart F&B Operating System project.

Working Directory: d:\Idea_DoAn\.agents\teamwork_preview_orchestrator_infrastructure\
Original Request File: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md
Workspace Root: d:\Idea_DoAn\

## MISSION
Thiết lập và cấu hình toàn diện bộ khung thư mục, file interfaces, DTOs, Controllers, EF Core entity configurations, Route groups, components, stores, hooks và test scaffolding cho toàn bộ hệ thống Smart F&B OS trong thư mục `d:\Idea_DoAn\` dựa trên bộ tài liệu đặc tả v2.5.0 (`01_`, `03_`, `04_`, `05_`), đảm bảo 100% cấu trúc sẵn sàng để đội ngũ lập trình bắt đầu code.

## Nguồn Sự Thật Tham Chiếu (Source of Truth)
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md` (62 Features)
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md` (25 Tables 3NF)
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md` (10 API Groups)
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md` (5 Route Groups)
- `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md` (10 Sequences)
- `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md` (ERD)
- `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md` (47 UAT Tests)

## Requirements & Scope of Work

### R1. Bộ Khung Backend .NET 8 Clean Architecture Toàn Diện
1. **Domain Layer (`backend/src/SmartFB.Domain/`)**:
   - 25 Entity classes chuẩn 3NF: `Users`, `Customers`, `LoyaltyCupTransactions`, `Reviews`, `ReviewImages`, `Branches`, `BranchWifiConfigs`, `Tables`, `PriceGroups`, `Categories`, `Products`, `ProductModifiers`, `ProductBOMs`, `Ingredients`, `InventoryTransactions`, `Orders`, `OrderItems`, `Payments`, `PayOSTransactions`, `Vouchers`, `Attendances`, `StaffShifts`, `CashShifts`, `ZReports`, `AuditLogs`.
   - Base entities, Audit fields (`CreatedAt`, `UpdatedAt`, `IsDeleted`, `DeletedAt`), Domain Enums, Domain Exceptions.
2. **Application Layer (`backend/src/SmartFB.Application/`)**:
   - Phân rã 10 Phân hệ CQRS Features trong `Features/`:
     * `Auth` (Login, Register, RefreshToken, Profile)
     * `Branches` (CRUD, WifiConfig)
     * `Tables` (CRUD, QR, Status)
     * `Products` (CRUD, Categories, Modifiers, BOM recipes)
     * `Orders` (Dine-in 2 nhánh trả trước/sau, Delivery 20k, Takeaway POS tích 10 ly)
     * `Payments` (PayOS Webhook, Cash Payment, Confirmations)
     * `Attendances` (WiFi BSSID/Subnet IP check-in/out)
     * `KitchenKDS` (KDS ticket stream, status transition, 86-toggle)
     * `ShiftsAndCash` (Open/Close cash drawer shift, Z-Report)
     * `AdminAndAnalytics` (Revenue analytics, AI-2 combo Apriori approval, P&L)
   - Mỗi Feature có đầy đủ cấu trúc: `Commands/`, `Queries/`, `DTOs/`, `Validators/` với interfaces, MediatR handlers hoặc signatures hoàn chỉnh.
   - Common interfaces: `IAppDbContext`, `ICurrentUserService`, `IDateTimeService`, `IPayOSService`, `ISignalRHubService`.
3. **Infrastructure Layer (`backend/src/SmartFB.Infrastructure/`)**:
   - 25 Entity Configuration classes (`IEntityTypeConfiguration<T>`) trong `Persistence/Configurations/` với khóa chính UUID, khóa ngoại, kiểu dữ liệu, index và Soft Delete query filters.
   - `AppDbContext` kế thừa `DbContext` / `IAppDbContext`, `DbSet<T>` cho 25 entities, audit log interception.
   - External services implementation skeletons (PayOS gateway client, WiFi validator, Hash/JWT token provider).
4. **API Layer (`backend/src/SmartFB.API/`)**:
   - 10 REST Controllers tương ứng 10 nhóm Endpoint API trong `03_Thiet_Ke_API_Contract.md`.
   - 4 SignalR Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) với đầy đủ client/server event contracts.
   - `Program.cs` cấu hình đầy đủ DI, Swagger/OpenAPI, CORS, JWT Auth, SignalR endpoints, global Exception Handler middleware.

### R2. Bộ Khung Frontend Next.js 14 App Router Toàn Diện
1. **5 Route Groups trong `frontend/src/app/`**:
   - `(customer)`: Menu gọi món Dine-in, Giỏ hàng, Chi tiết đơn hàng & trạng thái món, QR Delivery form (SĐT + địa chỉ + ship 20k), Trang thanh toán VietQR & Xác nhận.
   - `(kds)`: Màn hình TV Bếp KDS Real-time, Kanban board phân loại trạng thái, Modal công tắc khẩn cấp 86-Toggle.
   - `(staff)`: Web POS Quầy Takeaway (CRM tra cứu SĐT, Tích 10 ly), Sơ đồ quản lý bàn, Tiếp nhận chuông gọi phục vụ, Chấm công WiFi.
   - `(manager)`: Mở/kết ca két tiền, Báo cáo Z-Report, Quản lý kho định mức BOM, Cấu hình BSSID WiFi chi nhánh.
   - `(admin)`: Full CRUD Menu & BOM từng size, Thiết lập bảng giá vùng, Lên lịch Seasonal Menu, Phê duyệt Combo AI-2 Apriori, Dashboard P&L hợp nhất.
2. **UI Components & Layout Skeletons (`frontend/src/components/`)**:
   - Components dùng chung: Buttons, Inputs, Badges, Modals, ReceiptPrint, OrderCard, StatusBadge, Navbar, Sidebar.
3. **Zustand Stores & Custom Hooks (`frontend/src/stores/` & `frontend/src/hooks/`)**:
   - Zustand Stores: `useAuthStore`, `useCartStore`, `usePosStore`, `useShiftStore`, `useKdsStore`, `useTableStore`.
   - Custom Hooks: `useSignalR`, `useAttendanceWifi`, `useApiQuery`.
   - Type definitions trong `frontend/src/types/`.

### R3. Bộ Khung Kiểm Thử & CI/CD Pipelines
1. **Unit & Integration Tests Scaffolding**:
   - `backend/tests/SmartFB.UnitTests/`: Test suites bao phủ các feature handlers và domain logic.
   - `backend/tests/SmartFB.IntegrationTests/`: Test suites bao phủ API endpoints, database interactions và kịch bản UAT.
2. **DevOps CI/CD (`.github/workflows/ci.yml`)**:
   - GitHub Actions pipeline kiểm tra `dotnet build`, `dotnet test`, `npm run typecheck`, linting trên mỗi PR / push.

## BẮT BUỘC KIỂM CHỨNG KỸ THUẬT (Hard Verification Gate)
- `dotnet build backend/SmartFB.slnx` thành công 100% (Exit Code 0, 0 Errors).
- `dotnet test backend/SmartFB.slnx` thành công 100% (Exit Code 0).
- `npm --prefix frontend run typecheck` thành công 100% (Exit Code 0, 0 TS errors).
- Zero Placeholders: Không `TODO`, không mã giả, không hàm rỗng thiếu logic cơ bản.
- Tất cả mã nguồn được commit sạch sẽ vào branch `feature/infrastructure-setup`.
