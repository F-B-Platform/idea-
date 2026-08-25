## 2026-08-25T02:36:33Z

Lead Backend Engineer assignment for Smart F&B Operating System project:
Implement the complete, production-ready, 100% zero-placeholder .NET 8 Clean Architecture backend scaffolding for Smart F&B OS:
1. `backend/src/SmartFB.Domain/`:
   - 25 3NF Entity classes: `Users`, `Customers`, `LoyaltyCupTransactions`, `Reviews`, `ReviewImages`, `Branches`, `BranchWifiConfigs`, `Tables`, `PriceGroups`, `Categories`, `Products`, `ProductModifiers`, `ProductBOMs`, `Ingredients`, `InventoryTransactions`, `Orders`, `OrderItems`, `Payments`, `PayOSTransactions`, `Vouchers`, `Attendances`, `StaffShifts`, `CashShifts`, `ZReports`, `AuditLogs`.
   - `BaseEntity`, `AuditableEntity`, `ISoftDelete`, Domain Enums, Domain Exceptions.
2. `backend/src/SmartFB.Application/`:
   - Common interfaces (`IAppDbContext`, `IPayOSService`, `ISignalRHubService`, `ICurrentUserService`, `IDateTimeService`, `IWifiAttendanceValidator`, etc.).
   - 10 CQRS feature modules in `Features/`:
     * `Auth`
     * `Branches`
     * `Tables`
     * `Products`
     * `Orders` (Handling Dine-In prepaid/postpaid, Delivery 20k, Takeaway POS)
     * `Payments` (PayOS Webhook, Cash Payment, Confirmations)
     * `Attendances` (WiFi BSSID & IP dual verification)
     * `KitchenKDS` (KDS ticket stream, status transition, 86-toggle)
     * `ShiftsAndCash` (Open/Close cash shift, Z-Report)
     * `AdminAndAnalytics` (Revenue analytics, Apriori AI-2 combo, P&L)
   - Complete Commands, Queries, DTOs, FluentValidation Validators.
3. `backend/src/SmartFB.Infrastructure/`:
   - 25 Entity Configuration classes in `Persistence/Configurations/` with UUID v4 primary keys, foreign keys, column types, composite/partial indexes, and soft delete global query filters.
   - `AppDbContext` implementing `IAppDbContext` with 25 `DbSet<T>`, audit log interceptor.
   - External services implementation skeletons (PayOSService, WifiAttendanceValidator, JwtTokenProvider, etc.).
4. `backend/src/SmartFB.API/`:
   - 10 REST Controllers mapped to API groups.
   - 4 SignalR WebSocket Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) with client/server event contracts.
   - `Program.cs` configured with DI, Swagger/OpenAPI, CORS, JWT Auth, SignalR endpoints, and Global Exception Handler Middleware.
5. VERIFICATION:
   - Run `dotnet build backend/SmartFB.slnx` using terminal execution and verify 100% build success with 0 errors.
   - Document execution commands and output in your handoff.
