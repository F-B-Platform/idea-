# Execution Plan — Smart F&B OS Infrastructure Setup

## Objectives
Establish a 100% production-ready, zero-placeholder infrastructure scaffolding for Smart F&B OS across Backend (.NET 8 Clean Architecture), Frontend (Next.js 14 App Router), Testing Suites, and CI/CD pipelines based on specification documents v2.5.0.

## Workflow Phases

### Phase 0: Survey & Specification Inventory
- Dispatch 3 Explorers / Spec Miners:
  * Explorer 1 (Spec Miner - Backend & Database): Probe `01_` & `03_` (02_Thiet_Ke_Database.md, 03_Thiet_Ke_API_Contract.md, ERD) -> 25 entities, 10 API groups.
  * Explorer 2 (Spec Miner - Frontend & UX): Probe `01_` & `04_Thiet_Ke_UI_UX.md`, Sequences -> 5 Route groups, components, stores, hooks.
  * Explorer 3 (Spec Miner - Testing & QA): Probe `05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`, CI/CD -> 47 UAT tests, test runner requirements, pipeline.
- Synthesize into `PROJECT.md` with full Feature Inventory, Architecture, Code Layout, and Milestones.

### Phase 1: Backend .NET 8 Clean Architecture Implementation
- Worker (Backend Specialist):
  * Solution setup: `backend/SmartFB.slnx` or `.sln` with Domain, Application, Infrastructure, API projects.
  * Domain: 25 entities 3NF, BaseEntity, AuditableEntity, Enums, Exceptions.
  * Application: 10 CQRS Feature folders (Commands, Queries, DTOs, Validators), interfaces (`IAppDbContext`, `IPayOSService`, etc.).
  * Infrastructure: 25 EF Core Configurations (`IEntityTypeConfiguration<T>`), `AppDbContext`, External service skeletons (PayOS, WiFi, JWT).
  * API: 10 Controllers, 4 SignalR Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`), `Program.cs` with DI, Swagger, JWT, CORS, Exception Handling.

### Phase 2: Frontend Next.js 14 App Router Implementation
- Worker (Frontend Specialist):
  * Next.js 14 App Router project setup (`frontend/`).
  * 5 Route Groups: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.
  * Common UI Components & Layouts in `src/components/`.
  * Zustand stores (`useAuthStore`, `useCartStore`, `usePosStore`, `useShiftStore`, `useKdsStore`, `useTableStore`).
  * Custom hooks (`useSignalR`, `useAttendanceWifi`, `useApiQuery`) and Types in `src/types/`.

### Phase 3: Testing Scaffolding & CI/CD Pipeline
- Worker (Test & DevOps Specialist):
  * `backend/tests/SmartFB.UnitTests/` covering domain logic and feature handlers.
  * `backend/tests/SmartFB.IntegrationTests/` covering API endpoints and UAT flows.
  * `.github/workflows/ci.yml` for dotnet build, dotnet test, npm typecheck, lint.

### Phase 4: Multi-Agent Verification & Audit Gate
- 2 Reviewers independently reviewing correctness, completeness, zero-placeholder compliance.
- 2 Challengers testing builds, compilation, and unit/integration test executions.
- 1 Forensic Auditor (`teamwork_preview_auditor`) running integrity forensics.
- Orchestrator evaluation and final synthesis.
