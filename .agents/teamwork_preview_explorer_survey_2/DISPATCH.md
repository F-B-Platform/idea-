## 2026-08-23T13:06:23Z
You are Explorer 2 (API Contracts, UI/UX Design System & Flows Specialist).
Your working directory is: d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_2\
Read the authoritative user request at: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md

Your mission:
1. Thoroughly investigate the Source of Truth files in `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:
   - `Smart_FB_Operating_System.md`
   - `Actor_KhachHang_Luong_Chay.md`
   - `Workflow_Quy_Trinh_Nghiep_Vu.md`
   - `Tong_Quan_Kien_Truc_He_Thong.md`
2. Compare them with existing files in `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\`:
   - `03_Thiet_Ke_API_Contract.md`
   - `04_Thiet_Ke_UI_UX.md`
3. Map out:
   - 10 RESTful API Groups (.NET 8 Clean Architecture / MediatR CQRS) + SignalR 4 Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) + PayOS Webhook HMAC SHA256.
   - UI/UX Design System across 5 Route Groups in Next.js 14 App Router: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.
   - UI screens mapping: Mobile Web PWA for Customer (Dine-In Bill QR, Delivery QR), Web POS for Counter Staff (Takeaway 10 cups, Cash collection, WiFi attendance), Web KDS for Kitchen/Bar TV, Web Management for Manager & Admin.
   - Total elimination of Staff Mobile App (Flutter/React Native), GPS 50m, QR 30s.
   - Gaps, outdated endpoints, missing DTOs/parameters, syntax issues in Mermaid diagrams, placeholders in current 03_ and 04_ files.
4. Output your detailed analysis to `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_2\survey_api_uiux.md` and write a soft handoff to `handoff.md`.
5. Send a message to parent when complete.
