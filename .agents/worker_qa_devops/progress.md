# Progress Tracking — QA & DevOps Engineering

Last visited: 2026-08-25T09:50:25+07:00

## Completed Milestones
- [x] **Investigation & Setup**: Checked solution, dependencies, UAT cases, API contracts, and established test projects.
- [x] **Unit Tests Implementation (`backend/tests/SmartFB.UnitTests/`)**:
  - [x] Domain business logic tests: `CustomerLoyaltyTests` (10-cup takeaway rule, reset to 0), `OrderEntityTests` (20k delivery shipping fee, status transitions), `ProductBomTests` (ingredient calculation), `BranchWifiConfigTests` (dual WiFi validation), `CashShiftEntityTests` (cash shift variance calculations).
  - [x] Feature handlers tests with Moq (`Auth`, `Orders`, `Payments`, `Attendances`, `KitchenKDS`, `ShiftsAndCash`).
  - [x] FluentValidation validator tests for all key request DTOs (`CreateDeliveryOrderValidator`, `WifiClockInValidator`, `CloseCashShiftValidator`, `LoginUserCommandValidator`, `CreateTakeawayOrderValidator`, `PayOSWebhookValidator`).
  - [x] Result: 94 tests passing 100%.
- [x] **Integration Tests Implementation (`backend/tests/SmartFB.IntegrationTests/`)**:
  - [x] `CustomWebApplicationFactory`, `TestAuthHandler`, `SeedDataConstants`, and in-memory test doubles (`TestPayOSService`, `InMemoryTestRedisCacheService`, `TestWifiAttendanceValidator`, `TestSignalRHubService`).
  - [x] 7 UAT Flow Test Suites (`DineInOrdersFlowTests`, `DeliveryOrdersFlowTests`, `TakeawayPosLoyaltyFlowTests`, `WifiAttendanceFlowTests`, `KitchenKdsFlowTests`, `ShiftAndZReportFlowTests`, `PayOSWebhookFlowTests`).
  - [x] Result: 14 tests passing 100%.
- [x] **DevOps CI/CD Pipeline (`.github/workflows/ci.yml`)**:
  - [x] Configured backend .NET 8 restore, build (`/p:TreatWarningsAsErrors=true`), test with coverage, artifact upload.
  - [x] Configured frontend Node.js 20, npm ci, lint, typecheck, build.
  - [x] Configured security package audit.
- [x] **Verification & Documentation**:
  - [x] Verified solution test run (`dotnet test backend/SmartFB.slnx` -> 108/108 tests passing).
  - [x] Created `changes.md` and `handoff.md`.
