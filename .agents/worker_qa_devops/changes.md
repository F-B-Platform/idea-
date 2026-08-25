# Implementation Changes Log — QA & DevOps Engineering

## Overview
Built the complete, production-grade Unit Tests, Integration Tests scaffolding (7 UAT Flows), and GitHub Actions CI/CD pipeline for the Smart F&B Operating System.

---

## 1. Unit Tests (`backend/tests/SmartFB.UnitTests/`)
- **Total Test Cases**: 94 Tests (100% Pass Rate).
- **Core Coverage**:
  - **Domain Business Logic**:
    - `CustomerLoyaltyTests`: 10-cup takeaway loyalty accumulation, redemption rule (10 cups = 1 free cup), reset calculation (`Balance - 10 + NewPurchased`), channel restriction.
    - `OrderEntityTests`: Fixed 20,000 VND shipping fee on delivery orders, 0 VND for Dine-In/Takeaway, status transitions (`PendingPayment` -> `Paid` -> `Confirmed` -> `Preparing` -> `Ready` -> `Completed`), TTL expiration cancellation.
    - `ProductBomTests`: Multi-item recipe ingredient aggregation (Matcha Latte, Trà Đào), stock deduction, negative stock alerting.
    - `BranchWifiConfigTests`: Dual WiFi verification (BSSID MAC normalization + CIDR subnet `192.168.1.0/24`), 4G cellular rejection.
    - `CashShiftEntityTests`: Shift float + cash sales balance, variance calculation (`Actual - Expected`), threshold check (`|variance| > 50,000 VND`).
  - **CQRS Application Feature Handlers**:
    - `Auth`: `LoginUserCommandHandlerTests`, `RefreshTokenCommandHandlerTests`.
    - `Orders`: `CreateDineInPrepaidOrderCommandHandlerTests`, `CreateDineInPostpaidOrderCommandHandlerTests`, `CreateDeliveryOrderCommandHandlerTests`, `CreateTakeawayOrderCommandHandlerTests`.
    - `Payments`: `ProcessPayOSWebhookCommandHandlerTests` (HMAC-SHA256 verification & Redis idempotency lock), `ConfirmCashPaymentCommandHandlerTests`.
    - `Attendances`: `WifiClockInCommandHandlerTests`, `WifiClockOutCommandHandlerTests`.
    - `KitchenKDS`: `UpdateKdsOrderStatusCommandHandlerTests` (BOM deduction on Ready), `ToggleProductAvailabilityCommandHandlerTests` (86-toggle & cache invalidation).
    - `ShiftsAndCash`: `OpenCashShiftCommandHandlerTests`, `CloseCashShiftCommandHandlerTests`.
  - **FluentValidation DTO Validators**:
    - `CreateDeliveryOrderValidatorTests`: Vietnamese phone regex `^(03|05|07|08|09)\d{8}$`, delivery address min 10 chars, items count >= 1.
    - `WifiClockInValidatorTests`: BSSID MAC regex, IP regex, branchId & employeeCode requirements.
    - `CloseCashShiftValidatorTests`: Actual cash non-negative, variance justification rule.
    - `LoginUserCommandValidatorTests`: Username & Password required.
    - `CreateTakeawayOrderValidatorTests`: Phone & items validation.
    - `PayOSWebhookValidatorTests`: OrderCode & Amount validation.

---

## 2. Integration Tests (`backend/tests/SmartFB.IntegrationTests/`)
- **Total Test Cases**: 14 Tests (100% Pass Rate).
- **Test Infrastructure**:
  - `CustomWebApplicationFactory`: In-memory EF Core database with `TestApplicationDbContext`, mock `TestPayOSService`, in-memory Redis cache with distributed lock support (`InMemoryTestRedisCacheService`), mock `TestSignalRHubService`, and `TestWifiAttendanceValidator`.
  - `TestAuthHandler`: Simulates authentication headers for `CashierStaff`, `BaristaStaff`, `BranchManager`, `ChainAdmin`, `Customer`.
  - `SeedDataConstants`: Clean deterministic GUIDs for branches, tables, products, product sizes, users, and WiFi configs.
- **7 UAT Flow Suites**:
  1. `DineInOrdersFlowTests`: Prepaid VietQR vs Postpaid Cash flow, live tracking, order cancellation on TTL.
  2. `DeliveryOrdersFlowTests`: Fixed 20,000 VND shipping fee, validation for phone/address/items, COD payment rejection.
  3. `TakeawayPosLoyaltyFlowTests`: 10-cup loyalty stamp redemption, 1 free cup 100% discount, remaining cup calculation, new customer auto-registration.
  4. `WifiAttendanceFlowTests`: Dual network validation (BSSID + Subnet IP), 4G public cellular IP rejection (400), unknown employee code rejection (400).
  5. `KitchenKdsFlowTests`: Active kitchen tickets retrieval, emergency 86-toggle out-of-stock and menu update.
  6. `ShiftAndZReportFlowTests`: Cash shift opening, variance threshold check (> 50k VND requires justification), Z-Report generation.
  7. `PayOSWebhookFlowTests`: PayOS Webhook HMAC signature verification and Redis lock idempotency.

---

## 3. DevOps CI/CD Pipeline (`.github/workflows/ci.yml`)
- **Backend CI Job**:
  - Setup .NET 8 SDK.
  - PostgreSQL 16 & Redis 7 services with health checks.
  - Restore NuGet packages (`dotnet restore backend/SmartFB.slnx`).
  - Strict build with zero warnings (`dotnet build backend/SmartFB.slnx /p:TreatWarningsAsErrors=true`).
  - Unit & Integration test execution with XPlat code coverage (`dotnet test backend/SmartFB.slnx --collect:"XPlat Code Coverage"`).
  - Test results and coverage artifact upload (`actions/upload-artifact@v4`).
- **Frontend CI Job**:
  - Setup Node.js 20 LTS with NPM cache.
  - Dependency install (`npm ci`).
  - ESLint verification (`npm run lint`).
  - TypeScript strict type-checking (`npm run typecheck`).
  - Production build (`npm run build`).
- **Security Audit Job**:
  - NuGet vulnerability audit (`dotnet list package --vulnerable`).
  - NPM production security audit (`npm audit --production`).
