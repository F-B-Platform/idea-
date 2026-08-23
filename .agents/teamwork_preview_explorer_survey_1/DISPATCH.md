## 2026-08-23T13:06:23Z
You are Explorer 1 (Spec, RBAC, Requirements & DB Architecture Specialist).
Your working directory is: d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_1\
Read the authoritative user request at: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md

Your mission:
1. Thoroughly investigate the Source of Truth files in `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:
   - `Smart_FB_Operating_System.md`
   - `Actor_Phan_Quyen_Chuc_Nang.md`
   - `Tong_Quan_Kien_Truc_He_Thong.md`
   - `Workflow_Quy_Trinh_Nghiep_Vu.md`
2. Compare them with the existing files in `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\`:
   - `01_Phan_Tich_Yeu_Cau.md`
   - `02_Thiet_Ke_Database.md`
3. Map out:
   - Full list of 62 core features across 4 Actors: Customer (C-01 ~ C-20, exactly 20), Staff (S-01 ~ S-13, exactly 13), Manager (M-01 ~ M-12, exactly 12), Admin (A-01 ~ A-17, exactly 17).
   - Removed legacy concepts that MUST NOT appear: Staff Mobile App (Flutter/React Native), GPS 50m, QR động 30s, C-23 (chia sẻ MXH), C-24 (Push PWA), ví voucher riêng, tra cứu calo riêng lẻ.
   - Core business rules: Dine-In 2 branches (VietQR prepay vs Cash postpay + Bill QR), Delivery (20k ship, 100% VietQR prepay, no COD, phone + address), Takeaway POS (no QR, phone CRM, 10 cups get 1 free loyalty, postpay), WiFi Attendance (BSSID / IP Subnet + Staff PIN).
   - 25 database entities 3NF (PostgreSQL 16) with all fields, relations, indexing, and audit columns.
   - Gaps, outdated sections, placeholders, and discrepancies in current 01_ and 02_ files.
4. Output your detailed analysis to `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_1\survey_requirements_db.md` and write a soft handoff to `handoff.md`.
5. Send a message to parent when complete.
