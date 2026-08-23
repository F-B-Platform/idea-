## 2026-08-22T14:20:38Z
You are Worker M4 for the Smart F&B OS documentation overhaul.
Your working directory is: d:\Idea_DoAn\.agents\worker_m4\

MANDATORY FIRST STEP: Read d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md and d:\Idea_DoAn\PROJECT.md.
Also consult reference specifications:
- d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md
- d:\Idea_DoAn\.agents\spec_miner_docx\spec_extraction.md
- d:\Idea_DoAn\.agents\explorer_docs_map\docs_audit_map.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

YOUR EXCLUSIVE WRITE SCOPE:
1. d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md
2. d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md
3. d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md
4. d:\Idea_DoAn\06_Danh_Sach_Skills\README.md
5. d:\Idea_DoAn\02_Bao_Gia_Chi_Phi\Bang_Bao_Gia_Smart_FB_OS.md
6. d:\Idea_DoAn\02_Bao_Gia_Chi_Phi\Chi_Phi_Duy_Tri_Hang_Thang.md

TASK REQUIREMENTS:
- Rewrite all 6 files completely with 100% full content (Zero Placeholders, NO TODO/TBD).
- UAT_Test_Cases.md: Exhaustive test cases for Dine-in Pre-pay, QR Delivery (20k fee, mandatory address, VietQR), Takeaway Staff POS (phone search, 10 cups loyalty, cash/VietQR), WiFi-locked attendance (valid WiFi vs wrong WiFi vs wrong Employee code), Staff Web KDS, Edge cases (payment timeout, concurrent orders, out-of-stock).
- Seed_Data_&_Database_Script.md: PostgreSQL 16 DDL scripts & realistic DML seed data containing sample orders for all 3 OrderTypes (DineIn, TakeAway, Delivery), sample branches with wifi_ssid/wifi_bssid/allowed_ip_subnet, sample loyalty records (cup_count = 9 and cup_count = 10), menu items, modifiers.
- Git_Workflow_&_Branching_Strategy.md: Clean git workflow for 4-member team (2 BE + 2 FE).
- 06_Danh_Sach_Skills/README.md: Standard skill registry.
- 02_Bao_Gia_Chi_Phi/*.md: Update quotation and maintenance docs to reflect web-based solution (remove mobile app store licensing/maintenance costs, reflect unified web portal architecture).
- Write your completion report in d:\Idea_DoAn\.agents\worker_m4\handoff.md and send a message back when done.
