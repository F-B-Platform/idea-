## 2026-08-22T15:37:00Z
MANDATORY INTEGRITY AUDIT:
You are victory_5docs_auditor (TypeName: teamwork_preview_auditor).
Your working directory is: d:\Idea_DoAn\.agents\victory_5docs_auditor\

Your Mission:
Perform the final, exhaustive Victory Forensic Integrity Audit on all 5 specification files in `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:
1. `Smart_FB_Operating_System.md`
2. `Actor_Phan_Quyen_Chuc_Nang.md`
3. `Workflow_Quy_Trinh_Nghiep_Vu.md`
4. `Tong_Quan_Kien_Truc_He_Thong.md`
5. `Tom_Tat_1_Trang_Executive_Summary.md`

Run rigorous empirical validation:
1. Grep search across `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:
   - `C-23` -> must be exactly 0 matches
   - `C-24` -> must be exactly 0 matches
   - `TODO` -> must be exactly 0 matches
   - `TBD` -> must be exactly 0 matches
   - `/* rest of code */` -> must be exactly 0 matches
   - `// tương tự` -> must be exactly 0 matches
   - `TableHub` -> must be 0 matches
   - `Actor_KhachHang_Xem.html` -> must not exist
2. Check feature breakdown consistency:
   - Summary line 95: exactly 22 Customer C-01..C-22, 13 Staff S-01..S-13, 12 Manager M-01..M-12, 17 Admin A-01..A-17.
   - Total = 64 features.
3. Check 6 strict business rules:
   - Dine-In 2 payment paths (VietQR pre-pay vs Cash post-pay with bill QR)
   - Delivery (QR Delivery, 20k flat shipping fee, mandatory address, 100% VietQR)
   - Takeaway (Staff Web POS UI, CRM phone lookup, 10 cups loyalty strictly Takeaway-only, post-pay)
   - Attendance (WiFi-locked check-in, store WiFi + Staff ID, GPS 50m & 30s QR eliminated)
   - Admin Full CRUD (Product create/edit/delete/replace, BOM, combo, upload, branch price, 86 toggle, categories, seasonal menus)
   - Staff Mobile App completely eliminated (Web Responsive only)
4. Check SignalR Hubs consistency (OrderHub, KitchenHub, PaymentHub, NotificationHub).
5. Check Database entities (exactly 25 entities 3NF).

Deliver your final binary verdict: CLEAN or INTEGRITY VIOLATION.
Write your report to:
`d:\Idea_DoAn\.agents\victory_5docs_auditor\report.md`
and handoff to:
`d:\Idea_DoAn\.agents\victory_5docs_auditor\handoff.md`.
Communicate when done via send_message to parent.
