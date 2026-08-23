# DISPATCH LOG

## 2026-08-22T14:14:40Z
Initial dispatch for full repository overhaul.

## 2026-08-22T15:07:22Z
You are the Project Orchestrator for the Smart F&B Operating System documentation project.

Mission:
Lead the full rewrite of ONLY the 5 Markdown specification files in `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:
1. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
2. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`
3. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
4. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md`
5. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tom_Tat_1_Trang_Executive_Summary.md`

Authoritative User Request: `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (specifically latest follow-up).
Source of Truth: `d:\Idea_DoAn\temp_revised_content.txt` (extracted from `Smart_FB_OS_Revised_4members.docx`).
Working Directory: `d:\Idea_DoAn\.agents\orchestrator\`

Strict Business Rules:
1. DINE-IN (2 Payment Paths):
   - Path A: VietQR (Pre-pay): Customer scans table QR -> selects items -> pays VietQR -> payment confirmed -> Kitchen receives order via SignalR -> prepare -> serve.
     Status flow: `Pending Payment` -> `Paid` -> `Confirmed` -> `Preparing` -> `Ready` -> `Served`
   - Path B: Cash (Post-pay): Customer selects Cash -> Order sent to kitchen IMMEDIATELY -> prepare -> Staff serves food WITH printed bill having VietQR on it -> Customer pays cash OR scans QR on bill to transfer -> Staff confirms payment.
     Status flow: `Confirmed` -> `Preparing` -> `Ready` -> `Served` -> `Pending Payment` -> `Paid`
2. DELIVERY: Separate QR code, mandatory Phone + Delivery Address, fixed 20,000 VND shipping fee, VietQR prepayment ONLY (no COD, no cash). `order_type` enum (`DineIn`, `TakeAway`, `Delivery`), `delivery_address`, `delivery_fee`.
3. TAKEAWAY: Staff-operated UI on system (NO QR code for customer). Staff searches customer phone (auto-create CRM or view loyalty) -> staff enters items -> kitchen prepares -> customer receives items -> Paid AFTER receipt (Cash/Transfer/VietQR selected by staff). Loyalty: 10 cups purchased = 1 cup free (STRICTLY applies to Takeaway only, not Dine-In, not Delivery).
4. ATTENDANCE: WiFi-Locked check-in (Staff connects to store WiFi -> enters system -> Attendance section -> scans attendance QR -> enters Staff ID -> system verifies WiFi network matches store WiFi + valid staff ID -> Success; if wrong WiFi -> Reject). Replaces GPS/30s dynamic QR.
5. ADMIN FULL CRUD: Product create/edit/delete/replace, Combos creation, Image uploads (product & category), Branch pricing, 86 Toggle (out of stock), Menu category & display order, Seasonal menus.
6. REMOVALS:
   - Staff Mobile App -> Completely removed. All staff features (KDS, table map, call alerts, payment confirmation, takeaway) run on Web Responsive.
   - C-23 (Chia sẻ món ăn MXH) & C-24 (Push notification khuyến mãi PWA) -> DELETED COMPLETELY (zero mentions in all 5 files, NOT even in Future Work).
   - Any feature present in original docs but NOT in docx source of truth -> moved to "Scale Up / Future Work" section.
