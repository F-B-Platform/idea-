## 2026-08-22T14:20:38Z
You are Worker M3 for the Smart F&B OS documentation overhaul.
Your working directory is: `d:\Idea_DoAn\.agents\worker_m3\`

MANDATORY FIRST STEP: Read `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` and `d:\Idea_DoAn\PROJECT.md`.
Also consult reference specifications:
- `d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md`
- `d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md`
- `d:\Idea_DoAn\.agents\explorer_docs_map\docs_audit_map.md`

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

YOUR EXCLUSIVE WRITE SCOPE (All 4 files in `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams/`):
1. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md`
2. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md`
3. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md`
4. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md`

TASK REQUIREMENTS:
- Rewrite all 4 files completely with valid, renderable, syntax-error-free Mermaid diagrams.
- 01_Kien_Truc_Tong_Quan.md: C4 Architecture diagrams, System Context, Container diagram (Next.js 14 web portals: Customer PWA, Staff POS, KDS, Manager Portal; .NET 8 Web API, PostgreSQL, Redis, SignalR; VietQR gateway; AI Service). Remove Staff Mobile App container.
- 02_Sequence_Diagrams.md: Mermaid sequence diagrams for:
  1. Dine-in Pre-payment flow (Customer -> QR Table -> VietQR -> Webhook -> Kitchen KDS receives order).
  2. QR Delivery flow (Customer -> QR Delivery -> Address & 20k fee -> VietQR upfront -> Order confirmed -> Delivery tracking).
  3. Takeaway Staff POS flow (Staff -> Web POS -> Phone CRM -> 10 cups loyalty check -> Create order -> Customer pays Cash/VietQR at counter).
  4. WiFi-locked Attendance flow (Staff -> WiFi network check -> Employee code validation -> Check-in recorded).
  5. AI-1 Chatbot Consultation & AI-2 Smart Combo recommendation flows.
- 03_ERD_Database_Diagram.md: Comprehensive Mermaid ERD with all updated entities, relations, `OrderType`, `delivery_address`, `delivery_fee`, WiFi fields, removing GPS fields.
- 04_Deployment_Diagram.md: Docker Compose & Production deployment diagram (VPS/Cloud Run, Nginx reverse proxy, .NET 8 container, Next.js container, PostgreSQL 16, Redis 7). Remove mobile app store pipelines.
- Write your completion report in `d:\Idea_DoAn\.agents\worker_m3\handoff.md` and send a message back when done.
