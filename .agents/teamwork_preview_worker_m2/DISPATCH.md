## 2026-08-23T13:20:47Z

You are Worker M2 (Lead Technical Documentation Writer — API Contracts & UI/UX Design System Specialist).
Your working directory is: d:\Idea_DoAn\.agents\teamwork_preview_worker_m2\

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Authoritative Request: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md
Project Scope: d:\Idea_DoAn\.agents\teamwork_preview_orchestrator_1\PROJECT.md
Detailed Survey Findings: d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_2\survey_api_uiux.md
Prerequisite M1 Deliverables:
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
Source of Truth:
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Luong_Chay.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md`

Your Exclusive File Ownership:
1. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md`

Your Tasks:
1. Standardize and completely rewrite `03_Thiet_Ke_API_Contract.md` to:
   - Present 10 RESTful API Groups mapped 100% to the 62 Core Features:
     1. Authentication & RBAC (`/api/v1/auth/*`)
     2. Branch & Table Management (`/api/v1/branches/*`, `/api/v1/tables/*`)
     3. Category, Product & BOM Recipe (`/api/v1/categories/*`, `/api/v1/products/*`, `/api/v1/recipes/*`)
     4. Order Management (`/api/v1/orders/*` - Dine-In 2 branches, Delivery 20k fee, Takeaway POS)
     5. Payment & PayOS Webhook (`/api/v1/payments/*`, `/api/v1/webhooks/payos` HMAC SHA256)
     6. WiFi-Locked Attendance (`/api/v1/attendances/*` - BSSID + IP Subnet + Staff PIN)
     7. KDS & Real-time Kitchen Dispatch (`/api/v1/kds/*`)
     8. Shifts, Cash Management & Z-Report (`/api/v1/shifts/*`)
     9. Inventory & Warehouse Transactions (`/api/v1/inventory/*`)
     10. Admin Analytics, AI-1 Gemini & AI-2 Apriori Engine (`/api/v1/admin/*`, `/api/v1/ai/*`)
   - Detail full OpenAPI 3.1 contracts, complete C# DTOs, MediatR CQRS Commands/Queries, FluentValidation rules, headers, query parameters, request/response JSON bodies, and HTTP status codes.
   - Specify 4 SignalR Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) with event payloads, methods, and group management.
   - Detail PayOS Webhook idempotency handling with Redis distributed lock (`lock:webhook:payos:{paymentLinkId}`) and HMAC-SHA256 signature verification.
   - Zero placeholders, zero code cutoffs, valid Mermaid diagrams, GitHub Alert Callouts.

2. Standardize and completely rewrite `04_Thiet_Ke_UI_UX.md` to:
   - Define Next.js 14 App Router Monorepo Design System across 5 Route Groups:
     * `(customer)`: Mobile Web PWA (Menu, Dine-In Bill QR, Delivery QR 20k fee, AI suggestions, real-time tracking, feedback)
     * `(kds)`: Web KDS TV Dark Mode (Cooking queue, urgency colors, cook/ready action buttons, audio chime)
     * `(staff)`: Web POS (Counter Takeaway 10-cup loyalty, Dine-In table order, Cash collection, WiFi Attendance PIN screen, Shift handoff)
     * `(manager)`: Web Management (Menu/BOM management, Stock counts, WiFi config, Cash shifts, KDS SLA monitor)
     * `(admin)`: Enterprise Master Web (Branch chain, Master menu, Global pricing, AI-2 Apriori combo approvals, Financial reports, PayOS config, Audit logs)
   - Eliminate 100% of Staff Mobile App (Flutter/React Native), GPS 50m, QR 30s, C-23, C-24, separate voucher/calorie screens.
   - Include complete Design Tokens (Colors, Typography, Spacing, Shadows, Border Radii, Dark Mode).
   - Include comprehensive ASCII wireframes and user interaction flows for all 3 sales channels, WiFi attendance, KDS, Cash Shifts, and AI Combo Approval.
   - Zero placeholders, valid Mermaid diagrams, GitHub Alert Callouts.

3. Verify deliverables:
   - Check API groups coverage of all 62 features.
   - Check 5 route groups and UI screens.
   - Check no trace of removed legacy concepts.
   - Check Mermaid syntax.

4. Write a comprehensive handoff report to `d:\Idea_DoAn\.agents\teamwork_preview_worker_m2\handoff.md`.
5. Send a message to parent when done.
