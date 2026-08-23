## 2026-08-22T15:11:22Z
MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

You are worker_workflows (TypeName: teamwork_preview_worker).
Your working directory is: d:\Idea_DoAn\.agents\worker_workflows\
Your exclusive write target is: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`

Input References to Read First:
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (specifically latest follow-up)
- `d:\Idea_DoAn\temp_revised_content.txt`
- `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\report.md`
- `d:\Idea_DoAn\.agents\spec_miner_doc_truth\report.md`
- `d:\Idea_DoAn\.agents\explorer_5docs_diff\report.md`

Your Mission:
Completely rewrite `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md` with 100% full, comprehensive, professional Markdown content:
1. Architectural overview of business workflows and order state machine.
2. Complete step-by-step descriptions, participating actors, preconditions, postconditions, input/output data, exception handling, and 100% VALID Mermaid sequence diagrams for all 16 business workflows:
   - WF-00: Customer CRM Phone Identification & Session
   - WF-01A: Dine-In VietQR Pre-Payment (`PendingPayment` -> `Paid` -> `Confirmed` -> `Preparing` -> `Ready` -> `Served`)
   - WF-01B: Dine-In Cash Post-Payment (`Confirmed` -> `Preparing` -> `Ready` -> `Served` -> `PendingPayment` -> `Paid`, staff serves food WITH printed bill having dynamic VietQR, customer pays cash or scans bill QR, staff confirms payment)
   - WF-02: Delivery Order (QR Delivery, mandatory Phone + Delivery Address, fixed 20,000 VND shipping fee, 100% VietQR prepayment only, kitchen `[DELIVERY]` badge)
   - WF-03: Takeaway Counter Staff Flow (Staff Web POS UI, CRM phone lookup, order entry, kitchen preparation, customer pickup, post-payment, Loyalty: 10 cups purchased = 1 cup free strictly applies ONLY to Takeaway)
   - WF-04: WiFi-Locked Attendance (Store WiFi connection verification via Subnet/BSSID + Staff ID on Web, GPS 50m and 30s dynamic QR removed)
   - WF-05: Real-Time KDS SignalR WebSocket & Batching
   - WF-06: 86-Toggle Out-of-Stock Synchronization
   - WF-07: Table Service Calling Alert & Resolution
   - WF-08: Customer Feedback, Photo Upload & <= 2 Stars Escalation
   - WF-09: Shift Opening, Closing & Cash Reconciliation (Z-Report)
   - WF-10: Stock Requisition & BOM Auto-Deduction with Low-Stock Alerts
   - WF-11: Admin Full CRUD (Product create/edit/delete/replace, BOM recipes, WebP image upload)
   - WF-12: AI-2 Apriori/FP-Growth Combo Discovery & Approval
   - WF-13: Menu Category Reordering & Seasonal Menu Scheduling
   - WF-14: Branch Dynamic Pricing Management
   - WF-15: AI-1 Gemini RAG Chatbot Consultation
   - WF-16: Consolidated P&L Financial Reporting
3. Comprehensive Order State Transition Matrix for all 4 channels (`DineIn_PrePay`, `DineIn_PostPay`, `TakeAway`, `Delivery`).
4. Edge Cases Matrix covering 10 operational scenarios.
5. Strict deletion of C-23, C-24 and Staff Mobile App.
6. Quality: 100% Zero Placeholders, 100% valid Mermaid diagrams.

Write the rewritten file to `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md` using `write_to_file`.
Then write your handoff to `d:\Idea_DoAn\.agents\worker_workflows\handoff.md` and report back via send_message.
