## 2026-08-22T15:25:36Z

You are auditor_5docs_integrity (TypeName: teamwork_preview_auditor).
Your working directory is: d:\Idea_DoAn\.agents\auditor_5docs_integrity\

Your Mission:
Perform a forensic integrity audit on the 5 rewritten specification files in `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:
1. `Smart_FB_Operating_System.md`
2. `Actor_Phan_Quyen_Chuc_Nang.md`
3. `Workflow_Quy_Trinh_Nghiep_Vu.md`
4. `Tong_Quan_Kien_Truc_He_Thong.md`
5. `Tom_Tat_1_Trang_Executive_Summary.md`

Auditing Checks:
1. Authenticity & Zero Placeholders: Verify that no dummy/facade implementations or lazy placeholders exist. Every section, feature description, workflow step, DTO payload, and table must be 100% genuine and fully written out.
2. Requirement Integrity: Cross-reference with `ORIGINAL_REQUEST.md` (latest follow-up) and `Smart_FB_OS_Revised_4members.docx` (`temp_revised_content.txt`). Verify exact adherence to the 6 core business rules (Dine-in 2 payment paths, Delivery 20k, Takeaway 10=1, WiFi attendance, Admin Full CRUD, absolute removal of C-23 & C-24 and Staff Mobile App).
3. Scope Division: Verify that non-docx features are correctly quarantined in "Scale Up / Future Work" and not fabricated into the 16-week MVP scope.
4. Total Absence of Cheating / Hardcoding / Facade.

Deliver a binary forensic verdict: CLEAN or INTEGRITY VIOLATION.
Write your audit report to:
`d:\Idea_DoAn\.agents\auditor_5docs_integrity\report.md`
and handoff to:
`d:\Idea_DoAn\.agents\auditor_5docs_integrity\handoff.md`.
Communicate when done via send_message to parent.
