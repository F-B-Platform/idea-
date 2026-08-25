## 2026-08-25T02:32:54Z

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
1. Domain Layer: 25 Entity classes chuẩn 3NF, Base entities, Audit fields, Domain Enums, Domain Exceptions.
2. Application Layer: 10 Features (Auth, Branches, Tables, Products, Orders, Payments, Attendances, KitchenKDS, ShiftsAndCash, AdminAndAnalytics) với Commands, Queries, DTOs, Validators, Common interfaces.
3. Infrastructure Layer: 25 Entity Configuration classes, AppDbContext, External service skeletons.
4. API Layer: 10 REST Controllers, 4 SignalR Hubs, Program.cs với DI, Swagger, CORS, JWT, SignalR, Global Exception Handler.

### R2. Bộ Khung Frontend Next.js 14 App Router Toàn Diện
1. 5 Route Groups: (customer), (kds), (staff), (manager), (admin).
2. UI Components & Layout Skeletons.
3. Zustand Stores, Custom Hooks, Types.

### R3. Bộ Khung Kiểm Thử & CI/CD Pipelines
1. Unit & Integration Tests Scaffolding (.NET 8).
2. DevOps CI/CD (.github/workflows/ci.yml).
