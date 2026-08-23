## 2026-08-22T15:11:21Z

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

You are worker_spec_master (TypeName: teamwork_preview_worker).
Your working directory is: d:\Idea_DoAn\.agents\worker_spec_master\
Your exclusive write target is: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`

Input References to Read First:
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (specifically latest follow-up)
- `d:\Idea_DoAn\temp_revised_content.txt`
- `d:\Idea_DoAn\.agents\spec_miner_doc_truth\report.md`
- `d:\Idea_DoAn\.agents\explorer_5docs_diff\report.md`
- `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\report.md`

Your Mission:
Completely rewrite `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md` with 100% full, comprehensive, professional Markdown content reflecting all authoritative business rules:
1. Executive Context & Problem Statement (Digital transformation for F&B coffee chains, eliminating expensive legacy POS hardware, 60% hardware cost savings, 40% service speed increase).
2. 3 Types of QR codes:
   - Table QR (Dine-in menu & ordering)
   - Delivery QR (Home ordering with mandatory address & 20k fee)
   - Attendance QR (Store WiFi-locked check-in)
3. 3 Types of Orders (`OrderType`: `DineIn`, `TakeAway`, `Delivery`).
4. Dine-In 2 distinct Payment Paths:
   - Path A (VietQR Pre-Pay): Scan QR -> select items -> VietQR pay -> system receives Webhook -> `Paid` -> `Confirmed` -> Kitchen receives order via SignalR -> `Preparing` -> `Ready` -> `Served`.
   - Path B (Cash Post-Pay): Scan QR -> select Cash -> Order sent immediately to kitchen (`Confirmed`) -> `Preparing` -> `Ready` -> Staff serves food WITH printed bill having dynamic VietQR -> Customer pays cash OR scans bill QR -> Staff confirms `Paid`.
5. Delivery Order: Separate QR, mandatory Phone + Delivery Address, fixed 20,000 VND shipping fee, 100% VietQR prepayment only (no COD, no cash).
6. Takeaway Order: Staff-operated Web POS UI at counter (NO QR for customer), CRM phone lookup, post-payment (Cash/Transfer/VietQR), Loyalty: 10 cups purchased = 1 cup free (STRICTLY applies to Takeaway only).
7. Attendance: WiFi-Locked check-in (Store WiFi SSID/BSSID/IP Subnet verification + Staff ID on Web, GPS 50m and 30s dynamic QR eliminated).
8. Admin Full CRUD: Product create/edit/delete/replace, BOM recipes, AI-2 Apriori Combo creation & approval, WebP image upload, Branch pricing, 86-toggle, Menu category display order, Seasonal menus & scheduling.
9. Scope Partitioning: 64 Core MVP Features (22 Customer [C-01 to C-22], 13 Staff [S-01 to S-13], 12 Manager [M-01 to M-12], 17 Admin [A-01 to A-17]). 2 Core AI Modules (AI-1 Gemini RAG Chatbot, AI-2 Apriori Combo). All non-docx features clearly organized in "Scale Up / Future Work" section.
10. Strict Removals:
   - C-23 (Social food sharing) & C-24 (PWA Push promo notifications) -> DELETED COMPLETELY (0 mentions anywhere).
   - Staff Mobile App -> Completely eliminated (100% Web Responsive on Web POS / Web KDS).
11. Quality: 100% Zero Placeholders (no TODO, TBD, /* rest of code */), full tables and details, valid Mermaid diagrams if present, clean Vietnamese prose with technical terms in English.
