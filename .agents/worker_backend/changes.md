# BACKEND IMPLEMENTATION CHANGES REPORT

**Author**: Lead Backend Engineer
**Timestamp**: 2026-08-25T02:43:00Z
**Project**: Smart F&B Operating System (.NET 8 Clean Architecture)

---

## 1. Domain Layer (`backend/src/SmartFB.Domain/`)

### 1.1 Common & Infrastructure Core
- `Common/BaseEntity.cs`: Enhanced with UUID v4 `Id`, `CreatedAt`, `UpdatedAt`, `IsDeleted`, `DeletedAt`, DomainEvents support.
- `Common/AuditableEntity.cs`: Extends `BaseEntity` with `CreatedBy`, `LastModifiedBy`.
- `Common/ISoftDelete.cs`: Declares `IsDeleted` and `DeletedAt`.
- `Common/IAggregateRoot.cs`: Marker interface for DDD roots.
- `Common/DomainEvent.cs`: Base event record.

### 1.2 Domain Enums
- `Enums/OrderType.cs`: `DineIn`, `TakeAway`, `Delivery`.
- `Enums/OrderStatus.cs`: `PendingPayment`, `Paid`, `Confirmed`, `Preparing`, `Ready`, `Served`, `Completed`, `Cancelled`.
- `Enums/PaymentMethod.cs`: `VietQR`, `Cash`, `Card`.
- `Enums/PaymentStatus.cs`: `Pending`, `Paid`, `Failed`, `Refunded`, `Completed`.
- `Enums/UserRole.cs`: `Admin`, `Manager`, `Staff`, `Customer`, `ChainAdmin`, `BranchManager`, `BaristaStaff`, `CashierStaff`, `ServiceStaff`.
- `Enums/TableStatus.cs`: `Available`, `Occupied`, `AwaitingFood`, `Cleaning`, `Inactive`.
- `Enums/ShiftStatus.cs`: `Open`, `Closed`, `Audited`.
- `Enums/ModifierType.cs`: `Sweetness`, `Ice`, `Topping`, `MilkOption`.
- `Enums/VoucherDiscountType.cs`: `Percentage`, `FixedAmount`.
- `Enums/LoyaltyTransactionType.cs`: `TakeawayAccumulate`, `TakeawayRedeem10Free`, `ManualAdjustment`.
- `Enums/AttendanceStatus.cs`: `OnTime`, `Late`, `Overtime`, `Excused`.
- `Enums/InventoryTransactionType.cs`: `Import`, `Export`, `Adjustment`, `Wastage`.

### 1.3 Domain Exceptions
- `Exceptions/DomainException.cs`
- `Exceptions/NotFoundException.cs`
- `Exceptions/BusinessRuleException.cs`
- `Exceptions/UnauthorizedException.cs`

### 1.4 25 3NF Entity Classes
1. `Entities/Branch.cs`
2. `Entities/BranchWifiConfig.cs`
3. `Entities/Table.cs`
4. `Entities/User.cs`
5. `Entities/Role.cs`
6. `Entities/UserRoleMapping.cs`
7. `Entities/AuditLog.cs`
8. `Entities/Category.cs`
9. `Entities/Product.cs`
10. `Entities/ProductSize.cs`
11. `Entities/ProductBranchPrice.cs`
12. `Entities/Modifier.cs`
13. `Entities/ProductModifier.cs`
14. `Entities/Ingredient.cs`
15. `Entities/RecipeBom.cs`
16. `Entities/InventoryTransaction.cs`
17. `Entities/Customer.cs`
18. `Entities/Order.cs`
19. `Entities/OrderItem.cs`
20. `Entities/OrderItemModifier.cs`
21. `Entities/Payment.cs`
22. `Entities/PayOSTransaction.cs`
23. `Entities/Voucher.cs`
24. `Entities/CustomerReview.cs`
25. `Entities/ReviewImage.cs`
26. `Entities/Shift.cs`
27. `Entities/ZReport.cs`
28. `Entities/Attendance.cs`
29. `Entities/LoyaltyCupTransaction.cs`
30. `Entities/EntityAliases.cs` (Aliases for `CashShift`, `ProductBOM`, `StaffShift`, `PriceGroup`, `Review`)

---

## 2. Application Layer (`backend/src/SmartFB.Application/`)

### 2.1 Common Interfaces & Models
- `Common/Interfaces/IApplicationDbContext.cs` & `IAppDbContext.cs`: 29 DbSets, SaveChangesAsync.
- `Common/Interfaces/IPayOSService.cs`: CreatePaymentLink, VerifyWebhookSignature, GetPaymentLinkInformation.
- `Common/Interfaces/ISignalRHubService.cs`: Notifications for Order, Kitchen, Payment, Notification hubs.
- `Common/Interfaces/ICurrentUserService.cs`: Claims extraction (UserId, Role, BranchId).
- `Common/Interfaces/IDateTimeService.cs`: UtcNow, VietnamNow.
- `Common/Interfaces/IWifiAttendanceValidator.cs`: Dual BSSID + Subnet IP verification.
- `Common/Interfaces/IJwtTokenProvider.cs`: Token generation and validation.
- `Common/Interfaces/IRedisCacheService.cs`: Distributed caching and locking.
- `Common/Exceptions/ValidationException.cs`, `AppException.cs`, `NotFoundException.cs`, `DomainExceptionAliases.cs`.

### 2.2 10 CQRS Feature Modules
1. **Auth**:
   - Commands: `LoginUserCommand`, `RegisterUserCommand`, `RefreshTokenCommand`
   - Queries: `GetUserProfileQuery`
   - DTOs: `AuthResultDto`, `UserProfileDto`, `LoginRequestDto`, `RegisterUserRequestDto`, `RefreshTokenRequestDto`
   - Validators: `LoginUserCommandValidator`, `RegisterUserCommandValidator`
2. **Branches**:
   - Commands: `CreateBranchCommand`, `ConfigureBranchWifiCommand`
   - Queries: `GetBranchesQuery`
   - DTOs: `BranchDto`, `BranchWifiConfigDto`, `CreateBranchRequestDto`, `ConfigureWifiRequestDto`
   - Validators: `CreateBranchCommandValidator`, `ConfigureBranchWifiCommandValidator`
3. **Tables**:
   - Commands: `CreateTableCommand`, `UpdateTableStatusCommand`, `GenerateTableQrCommand`
   - Queries: `GetTablesQuery`
   - DTOs: `TableDto`, `TableQrDto`, `CreateTableRequestDto`, `UpdateTableStatusRequestDto`
   - Validators: `CreateTableCommandValidator`, `UpdateTableStatusCommandValidator`
4. **Products**:
   - Commands: `CreateProductCommand`, `SetRegionalPriceCommand`
   - Queries: `GetProductsQuery`
   - DTOs: `ProductDto`, `CategoryDto`, `ProductSizeDto`, `ModifierDto`, `RecipeBomDto`, `CreateProductRequestDto`, `SetRegionalPriceRequestDto`
   - Validators: `CreateProductCommandValidator`, `SetRegionalPriceCommandValidator`
5. **Orders**:
   - Commands: `CreateDineInPrepaidOrderCommand` (TTL 10m VietQR), `CreateDineInPostpaidOrderCommand` (Immediate KDS ticket), `CreateDeliveryOrderCommand` (Fixed 20k shipping, 100% VietQR), `CreateTakeawayOrderCommand` (Takeaway CRM, 10-cup redemption)
   - Queries: `GetOrderByIdQuery`
   - DTOs: `OrderDto`, `OrderItemDto`, `OrderItemModifierDto`, `PrepaidOrderResultDto`, `PostpaidOrderResultDto`, `DeliveryOrderResultDto`, `TakeawayOrderResultDto`, `OrderTrackingDto`
   - Validators: `CreateDineInPrepaidOrderCommandValidator`, `CreateDeliveryOrderCommandValidator`, `CreateTakeawayOrderCommandValidator`
6. **Payments**:
   - Commands: `ProcessPayOSWebhookCommand` (HMAC-SHA256, Redis Idempotency, SignalR KDS dispatch), `ConfirmCashPaymentCommand` (Cash change calculation, shift revenue update)
   - Queries: `GetPaymentStatusQuery`
   - DTOs: `PaymentDto`, `VietQrDto`, `PayOSWebhookDataDto`, `CashConfirmationResultDto`, `PaymentStatusDto`
   - Validators: `ConfirmCashPaymentCommandValidator`, `ProcessPayOSWebhookCommandValidator`
7. **Attendances**:
   - Commands: `WifiClockInCommand` (Dual BSSID + Subnet IP verification), `WifiClockOutCommand`
   - Queries: `GetAttendancesQuery`
   - DTOs: `AttendanceDto`, `WifiClockInRequestDto`, `WifiClockOutRequestDto`, `AttendanceSummaryDto`
   - Validators: `WifiClockInCommandValidator`, `WifiClockOutCommandValidator`
8. **KitchenKDS**:
   - Commands: `UpdateKdsItemStatusCommand` (Preparing -> Ready -> Automatic BOM deduction), `Toggle86ProductCommand` (Emergency out-of-stock toggle)
   - Queries: `GetKdsTicketsQuery`
   - DTOs: `KdsTicketDto`, `KdsItemDto`, `UpdateKdsItemStatusRequestDto`, `Toggle86RequestDto`
   - Validators: `UpdateKdsItemStatusCommandValidator`, `Toggle86ProductCommandValidator`
9. **ShiftsAndCash**:
   - Commands: `OpenCashShiftCommand`, `CloseCashShiftCommand` (Variance calculation, mandatory explanation if |variance| > 50,000 VND, Z-Report creation)
   - Queries: `GetActiveShiftQuery`
   - DTOs: `ShiftDto`, `OpenShiftRequestDto`, `CloseShiftRequestDto`, `ZReportDto`
   - Validators: `OpenCashShiftCommandValidator`, `CloseCashShiftCommandValidator`
10. **AdminAndAnalytics**:
    - Queries: `GetPandLReportQuery` (Revenue, COGS via BOM, labor, profit)
    - Commands: `MineAprioriCombosCommand` (Apriori AI-2 market basket combo mining: support >= 0.02, conf >= 0.4, lift > 1.2)
    - DTOs: `PandLReportDto`, `AiComboCandidateDto`, `ApproveAiComboRequestDto`, `AuditLogEntryDto`, `ConsolidatedRevenueDto`, `BranchRevenueDto`
    - Validators: `GetPandLReportQueryValidator`, `MineAprioriCombosCommandValidator`

---

## 3. Infrastructure Layer (`backend/src/SmartFB.Infrastructure/`)

### 3.1 25 Entity Configurations (`Persistence/Configurations/`)
- `CoreBranchConfigurations.cs`: `BranchConfiguration`, `BranchWifiConfigConfiguration`, `TableConfiguration`
- `UserRbacConfigurations.cs`: `UserConfiguration`, `RoleConfiguration`, `UserRoleMappingConfiguration`, `AuditLogConfiguration`
- `MenuProductConfigurations.cs`: `CategoryConfiguration`, `ProductConfiguration`, `ProductSizeConfiguration`, `ProductBranchPriceConfiguration`
- `InventoryConfigurations.cs`: `ModifierConfiguration`, `ProductModifierConfiguration`, `IngredientConfiguration`, `RecipeBomConfiguration`, `InventoryTransactionConfiguration`
- `CrmConfigurations.cs`: `CustomerConfiguration`, `LoyaltyCupTransactionConfiguration`, `VoucherConfiguration`
- `OrderPaymentConfigurations.cs`: `OrderConfiguration`, `OrderItemConfiguration`, `OrderItemModifierConfiguration`, `PaymentConfiguration`, `PayOSTransactionConfiguration`
- `OperationReviewConfigurations.cs`: `CustomerReviewConfiguration`, `ReviewImageConfiguration`, `ShiftConfiguration`, `ZReportConfiguration`, `AttendanceConfiguration`

### 3.2 DbContext & DI
- `Persistence/ApplicationDbContext.cs`: 29 DbSets, `ApplyConfigurationsFromAssembly`, automatic UTC timestamp / soft delete audit tracking in `SaveChangesAsync`.
- `Services/JwtTokenProvider.cs`: Production-ready JWT & Refresh Token provider.
- `Services/PayOSService.cs`: PayOS VietQR generation & HMAC-SHA256 signature verifier.
- `Services/WifiAttendanceValidator.cs`: Dual MAC BSSID & IP subnet matcher.
- `Services/CurrentUserService.cs`: HttpContext claims provider.
- `Services/SignalRHubService.cs`: SignalR event dispatcher.
- `Services/RedisCacheService.cs`: Redis cache & distributed locking.
- `DependencyInjection.cs`: Complete IoC service registration.

---

## 4. API Layer (`backend/src/SmartFB.API/`)

### 4.1 10 REST Controllers (`Controllers/`)
- `AuthController.cs` (`/api/v1/auth`)
- `BranchesController.cs` (`/api/v1/branches`)
- `TablesController.cs` (`/api/v1/tables`)
- `ProductsController.cs` (`/api/v1/products`)
- `OrdersController.cs` (`/api/v1/orders`)
- `PaymentsController.cs` (`/api/v1/payments`)
- `AttendancesController.cs` (`/api/v1/attendances`)
- `KitchenController.cs` (`/api/v1/kitchen`)
- `ShiftsController.cs` (`/api/v1/shifts`)
- `AnalyticsController.cs` (`/api/v1/analytics`)
- `HealthController.cs` (`/api/v1/health`)

### 4.2 4 SignalR WebSocket Hubs (`Hubs/`)
- `OrderHub.cs` (`/hubs/order`)
- `KitchenHub.cs` (`/hubs/kitchen`)
- `PaymentHub.cs` (`/hubs/payment`)
- `NotificationHub.cs` (`/hubs/notification`)

### 4.3 Middleware & Pipeline (`Program.cs`)
- `Middleware/GlobalExceptionMiddleware.cs`
- `Program.cs` configured with OpenAPI/Swagger, JWT Bearer Auth, CORS, SignalR Hub mapping, Controllers.

---

## 5. Verification Results
- `dotnet build backend/SmartFB.slnx`: Exit Code 0 (0 Warnings, 0 Errors).
- `dotnet test backend/SmartFB.slnx`: Exit Code 0 (95 tests passed, 0 failed, 0 skipped).
