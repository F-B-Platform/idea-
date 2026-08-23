## 2026-08-22T14:38:18Z
You are Worker M5 for the Smart F&B OS documentation overhaul.
Your working directory is: `d:\Idea_DoAn\.agents\worker_m5\`

MANDATORY FIRST STEP: Read `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` and `d:\Idea_DoAn\PROJECT.md`.
Also consult reference specifications:
- `d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md`
- `d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md`
- `d:\Idea_DoAn\.agents\explorer_docs_map\docs_audit_map.md`
- All newly rewritten files in `01_Tai_Lieu_Dac_Ta_Goc/`, `02_Bao_Gia_Chi_Phi/`, `03_Quy_Trinh_Trien_Khai/`, `04_Thiet_Ke_Kien_Truc_Diagrams/`, `05_Quy_Chuan_&_Test_Cases/`, `06_Danh_Sach_Skills/`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

YOUR EXCLUSIVE WRITE AND CLEANUP SCOPE:
1. `d:\Idea_DoAn\ROADMAP.md`
2. `d:\Idea_DoAn\DOC_AUDIT_REPORT.md`
3. Directory cleanup per R6:
   - Check if `d:\Idea_DoAn\05_Thiet_Ke_Kien_Truc_Diagrams/` exists. If it exists, verify all diagram content is in `04_Thiet_Ke_Kien_Truc_Diagrams/` and remove/clean up the duplicate directory.
   - Clean up temporary text files at root (`d:\Idea_DoAn\temp_docx_content.txt`, `d:\Idea_DoAn\temp_revised_content.txt`, temporary script files, `~$*` temporary files if any). Keep the original `Smart_FB_OS_Revised_4members.docx`.

TASK REQUIREMENTS:
- Rewrite `ROADMAP.md` completely:
  - 16 weeks duration, 8 Sprints (Sprint 1 to Sprint 8, 2 weeks/sprint) for 4 Capstone members (2 Backend, 2 Frontend).
  - Explicitly align every sprint with the revised MVP scope:
    * Sprint 1-2: Core Architecture (.NET 8 Clean Architecture, Next.js 14 App Router monorepo, PostgreSQL 16 schema, Redis 7, Branch WiFi config).
    * Sprint 3: Dine-in pre-payment flow (VietQR gateway, Order lifecycle `PendingPayment` -> `Paid` -> `Confirmed`, Web KDS real-time via SignalR).
    * Sprint 4: Takeaway Staff Web POS (phone CRM inline search, simplified loyalty 10 cups = 1 free cup, cash & VietQR counter payment).
    * Sprint 5: QR Delivery flow (Delivery PWA, mandatory address, fixed 20k shipping fee, 100% VietQR upfront, real-time status tracking).
    * Sprint 6: WiFi-locked Attendance (Branch IP/BSSID subnet + Employee ID validation, manager shift scheduling) & Staff Web portal consolidation (table map, call alerts).
    * Sprint 7: AI Modules integration (AI-1 RAG Chatbot advisor + AI-2 Apriori combo recommender at cart). Mark AI-3, AI-4, AI-5 as Scale Up / Future Work.
    * Sprint 8: UAT Testing, E2E validation, Docker Compose deployment & Final Capstone defense preparation.
  - Detailed task breakdown per sprint with assigned roles (BE 1, BE 2, FE 1, FE 2) and verifiable deliverables.
  - Zero Placeholders.
- Rewrite `DOC_AUDIT_REPORT.md` completely:
  - Comprehensive documentation audit evaluating all 30+ files across the repository.
  - Detailed audit against the 5 Core Business Changes, requirements R1-R6, Zero Placeholders rule, Mermaid syntax validity, cross-document consistency.
  - Verification checklist and statistics.
- Execute the cleanup and verify repository cleanliness.
- Write your completion report in `d:\Idea_DoAn\.agents\worker_m5\handoff.md` and send a message back when done.
