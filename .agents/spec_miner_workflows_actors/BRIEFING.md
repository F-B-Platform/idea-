# BRIEFING — 2026-08-22T22:10:35+07:00

## Mission
Synthesize and formulate comprehensive, unambiguous technical specifications for all Workflows and Actors across the Smart F&B Operating System.

## 🔒 My Identity
- Archetype: teamwork_preview_spec_miner
- Roles: Specification Miner, Workflows & Actors Lead
- Working directory: d:\Idea_DoAn\.agents\spec_miner_workflows_actors\
- Original parent: 2f276ad2-ad97-4bca-96be-6ea74949ded0
- Milestone: Full Specifications for Workflows and Actors (Phase 1 Deep Dive)

## 🔒 Key Constraints
- Web Responsive only, NO Staff Mobile App (Native App eliminated).
- C-23 (POS - In hóa đơn KiotViet) and C-24 (Kế toán MISA) removed completely.
- Zero placeholders (100% full detail, no TODOs, no summaries).
- 100% valid Mermaid diagram syntax for all sequence diagrams.
- Include all mandatory business workflows: WF-01A, WF-01B, WF-02, WF-03, WF-04, Admin Workflows (Product CRUD, Combo, Image Upload, Branch Pricing, 86 Toggle, Menu Categories, Seasonal Menu Scheduling), Operational Workflows (KDS SignalR, Calling Staff, Shift Handover, Inventory Threshold Alerts).
- Full RBAC Matrix for 4 core roles: Customer, Staff/Barista, Manager, Admin.

## Current Parent
- Conversation ID: 2f276ad2-ad97-4bca-96be-6ea74949ded0
- Updated: 2026-08-22T22:10:35+07:00

## Task Summary
- **What to build**: Comprehensive technical specifications document `report.md` detailing Actors, RBAC, Business Workflows (WF-01A, WF-01B, WF-02, WF-03, WF-04), Admin Workflows, Operational Workflows, Edge Cases, SignalR events, DTOs/Payloads, and validation rules.
- **Success criteria**: Zero placeholders, 100% Mermaid syntax accuracy, exhaustive edge-case handling, comprehensive RBAC matrix.
- **Interface contracts**: System specs in `01_Tai_Lieu_Dac_Ta_Goc/` and `temp_revised_content.txt`.

## Key Decisions Made
- Fully formulated 2 distinct Dine-In payment paths: WF-01A (VietQR Pre-Payment, kitchen waits for Paid) vs WF-01B (Cash Post-Payment, kitchen receives immediately, bill printed with VietQR).
- Standardized Delivery WF-02: QR Delivery, mandatory Phone + Address, fixed 20,000 VND fee, 100% VietQR pre-payment (No COD).
- Standardized Takeaway WF-03: Staff Web POS operated, CRM lookup, 10 cups = 1 free cup loyalty (Takeaway only), post-payment.
- Standardized Attendance WF-04: WiFi-locked (Public IP / Gateway subnet + BSSID + Staff ID validation).
- Fully validated 19 Mermaid diagrams with 0 errors and zero placeholders.

## Artifact Index
- `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\report.md` — Complete Workflow & Actor Specifications
- `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\handoff.md` — 5-component handoff report
- `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\progress.md` — Progress tracker
- `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\DISPATCH.md` — Dispatch record
