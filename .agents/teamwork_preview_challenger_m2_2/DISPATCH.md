## 2026-08-23T13:24:00Z
You are Challenger 2 for Milestone M2 (API Contracts & UI/UX Design System).
Your working directory is: d:\Idea_DoAn\.agents\teamwork_preview_challenger_m2_2\
Read the authoritative user request at: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md
Read the project scope at: d:\Idea_DoAn\.agents\teamwork_preview_orchestrator_1\PROJECT.md

Your task:
Empirically test contracts, security protocols and UI interactions in:
1. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md`

Test scenarios:
- PayOS webhook HMAC SHA256 signature verification & Redis lock idempotency logic.
- WiFi Attendance API (BSSID + IP Subnet check + Staff PIN payload).
- Takeaway POS order creation API & 10 cups loyalty logic.
- Delivery order creation API (mandatory 20,000 VND shipping fee + phone + address).
- Dine-In Branch A vs Branch B order & payment flow API contracts.

Write your verdict (APPROVE or REJECT) with test results in `d:\Idea_DoAn\.agents\teamwork_preview_challenger_m2_2\handoff.md` and send a message back to parent.
