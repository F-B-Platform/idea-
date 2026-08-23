## 2026-08-22T14:20:38Z
You are Worker M2 for the Smart F&B OS documentation overhaul.
Your working directory is: `d:\Idea_DoAn\.agents\worker_m2\`

MANDATORY FIRST STEP: Read `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` and `d:\Idea_DoAn\PROJECT.md`.
Also consult reference specifications:
- `d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md`
- `d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md`
- `d:\Idea_DoAn\.agents\explorer_docs_map\docs_audit_map.md`

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

YOUR EXCLUSIVE WRITE SCOPE (All 9 files in `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai/`):
1. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md`
2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
3. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
4. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md`
5. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md`
6. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md`
7. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md`
8. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md`
9. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\README.md`

TASK REQUIREMENTS:
- Rewrite all 9 files completely with 100% full content (Zero Placeholders, NO TODO/TBD).
- DB Design (02): ERD & DDL must include `order_type` enum (`DineIn`, `TakeAway`, `Delivery`), `delivery_address`, `delivery_fee`, `branch_wifi_configs` / `wifi_bssid`, `allowed_ip_subnet`; remove GPS latitude/longitude and rotating QR token fields.
- API Contract (03): Include OpenAPI 3.1 endpoints for Delivery (`/api/v1/orders/delivery`), Takeaway POS (`/api/v1/pos/takeaway/orders`), WiFi Attendance (`/api/v1/attendance/wifi-checkin`), VietQR Webhook; remove Staff Mobile App endpoints.
- UI/UX Design (04): Wireframes for Customer PWA Delivery, Staff Counter POS (phone search, loyalty 10 cups = 1 free), Web KDS, WiFi Attendance; remove Staff Mobile App screens.
- Backend/Frontend/Testing/Deployment (05, 06, 07, 08): Aligned with .NET 8 Clean Architecture, Next.js 14 App Router, SignalR hubs, Docker Compose (remove mobile builds/containers).
- Write your completion report in `d:\Idea_DoAn\.agents\worker_m2\handoff.md` and send a message back when done.
