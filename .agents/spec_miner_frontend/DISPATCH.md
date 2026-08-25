## 2026-08-25T09:33:36+07:00
You are the Frontend Spec Miner for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\spec_miner_frontend\
Original Request path: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md

TASK:
1. Read d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md.
2. Investigate authoritative documents in d:\Idea_DoAn\:
   - d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md
   - d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md
   - d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md
3. Extract and document complete specifications for:
   - Next.js 14 App Router layout & 5 Route Groups:
     * (customer): Dine-in ordering, cart, order tracking, QR Delivery form (phone + address + 20k shipping fee), VietQR payment & confirmation.
     * (kds): Kitchen Display System TV real-time, Kanban board (Pending, Preparing, Ready, Delivered), 86-Toggle emergency out-of-stock modal.
     * (staff): Takeaway POS (Customer phone search, 10-cup loyalty free redemption), Table map status & service bell alerts, WiFi attendance check-in/out.
     * (manager): Cash drawer shift open/close, Z-Report viewing, BOM recipe inventory management, Branch WiFi BSSID/IP config.
     * (admin): Menu & BOM full CRUD by size, regional price groups, seasonal menu scheduling, Apriori AI-2 combo approval, consolidated P&L dashboard.
   - Shared UI Components (Buttons, Inputs, Badges, Modals, ReceiptPrint, OrderCard, StatusBadge, Navbar, Sidebar).
   - Zustand Stores (useAuthStore, useCartStore, usePosStore, useShiftStore, useKdsStore, useTableStore) with complete state & actions signatures.
   - Custom Hooks (useSignalR, useAttendanceWifi, useApiQuery) and TypeScript types matching backend DTOs.
4. Write your comprehensive specification findings to `d:\Idea_DoAn\.agents\spec_miner_frontend\analysis.md`.
5. Write your handoff to `d:\Idea_DoAn\.agents\spec_miner_frontend\handoff.md`.
6. Update `d:\Idea_DoAn\.agents\spec_miner_frontend\progress.md` with your progress and timestamps.
7. Send a message to caller when done.
