## 2026-08-22T15:08:12Z
You are spec_miner_workflows_actors (TypeName: teamwork_preview_spec_miner).
Your working directory is: d:\Idea_DoAn\.agents\spec_miner_workflows_actors\

Your mission:
Synthesize and formulate the comprehensive, unambiguous technical specifications for all Workflows and Actors across the Smart F&B Operating System.

Read:
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (specifically latest follow-up)
- `d:\Idea_DoAn\temp_revised_content.txt`
- Current `01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- Current `01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`

Produce exact technical blueprints for:
1. Actor definitions and RBAC Matrix (Customer, Staff/Barista, Manager, Admin) — Web Responsive only, no Staff Mobile App, C-23 and C-24 removed completely.
2. Complete step-by-step workflow definitions and Mermaid sequence diagrams for all business flows:
   - WF-01A: Dine-In VietQR Pre-Payment (`Pending Payment` -> `Paid` -> `Confirmed` -> `Preparing` -> `Ready` -> `Served`)
   - WF-01B: Dine-In Cash Post-Payment (`Confirmed` -> `Preparing` -> `Ready` -> `Served` -> `Pending Payment` -> `Paid`, Bill printed with VietQR)
   - WF-02: Delivery Order (QR Delivery -> PWA -> Phone + Address -> VietQR Pre-Payment + 20,000 VND fee -> Kitchen)
   - WF-03: Takeaway Staff-Operated Flow (Staff Web UI -> CRM Phone lookup -> Order entry -> Kitchen -> Customer pickup -> Post-payment -> Loyalty 10 cups = 1 cup free)
   - WF-04: WiFi-Locked Attendance (Store WiFi connection verification + Staff ID validation)
   - Admin Workflows: Full product CRUD, Combo creation, image upload, branch pricing, 86 toggle, menu categories, seasonal menu scheduling
   - Other operational workflows (KDS real-time SignalR, calling staff alert, shift handover, inventory threshold alerts, etc.)

Ensure zero placeholders, complete edge cases, and 100% valid Mermaid diagram syntax.
Write your report to:
`d:\Idea_DoAn\.agents\spec_miner_workflows_actors\report.md`
and handoff to:
`d:\Idea_DoAn\.agents\spec_miner_workflows_actors\handoff.md`.
Communicate when done via send_message to parent.
