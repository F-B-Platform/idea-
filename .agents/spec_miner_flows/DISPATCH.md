## 2026-08-22T14:15:29Z
You are Spec Miner 3 for the Smart F&B OS documentation overhaul.
Your working directory is: `d:\Idea_DoAn\.agents\spec_miner_flows\`

MANDATORY FIRST STEP: Read `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` and `d:\Idea_DoAn\temp_revised_content.txt`.
Your task:
1. Deep-dive into the 5 Core Business Changes and extract precise technical contracts:
   - Change 1 (Dine-in pre-pay): Order lifecycle status enum (`PendingPayment`, `Paid`, `Confirmed`, `Preparing`, `Ready`, `Completed`), SignalR events, VietQR generation & payment webhook/polling, Kitchen KDS flow.
   - Change 2 (QR Delivery): OrderType (`Delivery`), fields (`delivery_address`, `delivery_fee` fixed 20.000 VNĐ, `phone_number`), customer PWA flow, payment must be VietQR upfront, driver/dispatch integration if any or scale-up status.
   - Change 3 (Takeaway Staff UI): OrderType (`TakeAway`), POS/Staff Web screen, customer phone search, CRM profile creation, simplified Loyalty (10 cups = 1 free cup voucher/redemption), post-payment option (Cash or VietQR).
   - Change 4 (WiFi-locked Attendance): Branch network config (`wifi_ssid`, `wifi_bssid`/MAC address, IP subnet), Attendance verification logic (Staff WiFi network check + Employee ID check), removal of GPS coordinates & 30s dynamic QR.
   - Change 5 (Staff App removal): Consolidation of staff responsibilities into Web KDS / Manager Web Portal / Cashier POS. Removal of Flutter/React Native mobile app references across architecture, deployment, route groups, and actors.
2. Outline exact API endpoints, Database schema changes, UI wireframe screens, and Mermaid sequence diagrams needed for these 5 changes.
3. Write your report to `d:\Idea_DoAn\.agents\spec_miner_flows\technical_contracts.md` and deliver `handoff.md`.
4. When finished, send a completion message back to your caller (parent).
