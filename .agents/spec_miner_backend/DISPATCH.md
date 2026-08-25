## 2026-08-25T02:33:36Z
You are the Backend Spec Miner for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\spec_miner_backend\
Original Request path: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md

TASK:
1. Read d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md.
2. Investigate authoritative documents in d:\Idea_DoAn\:
   - d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md
   - d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md
   - d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md
   - d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md
   - d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md
3. Extract and document complete specifications for:
   - 25 Entity classes (3NF), exact property names, types, primary keys, foreign keys, navigation properties, enums, soft delete columns, audit properties.
   - 10 CQRS feature modules in Application layer (Auth, Branches, Tables, Products, Orders, Payments, Attendances, KitchenKDS, ShiftsAndCash, AdminAndAnalytics), enumerating all Commands, Queries, DTOs, Validators, and business rules (e.g. 10 cups loyalty, dine-in prepay vs postpay, 20k delivery, 86-toggle, wifi BSSID attendance).
   - 25 EF Core Configurations in Infrastructure layer (Table names, column types, relationships, indexes, global query filters).
   - 10 API Controllers, route paths, HTTP methods, request/response models, status codes.
   - 4 SignalR Hubs (OrderHub, KitchenHub, PaymentHub, NotificationHub) with all server methods and client event contracts.
   - Core interfaces (IAppDbContext, IPayOSService, ISignalRHubService, ICurrentUserService, IDateTimeService) and DI registration plan.
4. Write your comprehensive specification findings to `d:\Idea_DoAn\.agents\spec_miner_backend\analysis.md`.
5. Write your handoff to `d:\Idea_DoAn\.agents\spec_miner_backend\handoff.md`.
6. Update `d:\Idea_DoAn\.agents\spec_miner_backend\progress.md` with your progress and timestamps.
7. Send a message to caller when done.
