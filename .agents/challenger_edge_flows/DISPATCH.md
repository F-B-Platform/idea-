## 2026-08-23T14:43:37Z
You are a Challenger subagent for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\challenger_edge_flows\
Create your working directory if needed.

Read:
1. `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`
2. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
3. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md`
4. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`
5. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md`
6. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md`

Your task:
Adversarially challenge the business logic, state machines, and operational edge scenarios across all 3 files:
1. Check Dine-In 2 distinct flows: Is Dine-In Branch A (Prepaid PayOS VietQR -> KDS receives only upon webhook payment) vs Dine-In Branch B (Postpaid Cash -> KDS receives Confirmed immediately -> Staff prints bill with dynamic VietQR -> Guest pays Cash or VietQR) 100% consistent across UAT, SQL Seed Data, and Coding Standards?
2. Check QR Delivery: Does it strictly mandate Phone + Address, fixed 20k shipping fee, 100% prepaid VietQR, and lock COD?
3. Check Takeaway POS: Does it strictly isolate the 10-stamp loyalty redeem 1 free cup to counter takeaway only?
4. Check WiFi Attendance: Does it strictly require BSSID and Subnet IP CIDR match and reject 4G?
5. Check KDS BOM & 86-Toggle: Does BOM deduct in grams/ml and does 86-Toggle isolate per branch with 10s undo?
6. Check Shift & Z-Report: Does Z-Report strictly enforce variance explanation when |variance| > 50k?
7. Check Edge Matrix: Are all 10 edge scenarios (TC-EDGE-01 to TC-EDGE-10) thoroughly covered?
8. Check for any trace of obsolete terms (Staff Mobile App, GPS 50m, 30s QR, C-23/C-24).

Provide your findings in `d:\Idea_DoAn\.agents\challenger_edge_flows\challenge_report.md` and write `d:\Idea_DoAn\.agents\challenger_edge_flows\handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`. Send a message to parent when completed.
