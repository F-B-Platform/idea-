## 2026-08-22T15:32:28Z

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

You are remediation_5docs_worker (TypeName: teamwork_preview_worker).
Your working directory is: d:\Idea_DoAn\.agents\remediation_5docs_worker\

Your Mission:
Execute the precise cross-document synchronizations and cleanup on the 5 specification files in `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`:

1. In `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`:
   - Line 11: Remove literal `C-23` and `C-24` string entirely. Replace `> 2. **Đã loại bỏ vĩnh viễn:** C-23 (Chia sẻ món ăn MXH) và C-24 (Push Notification khuyến mãi PWA).` with `> 2. **Đã loại bỏ vĩnh viễn:** Các tính năng chia sẻ món ăn lên mạng xã hội và Push Notification khuyến mãi trên PWA đã được loại bỏ hoàn toàn khỏi toàn bộ hệ thống.`
   - Section 6.3 (Lines ~1585-1604): Synchronize the SignalR hubs table to list the canonical 4 Hubs:
     - `OrderHub` (`/hubs/orders`): Theo dõi và cập nhật trạng thái đơn hàng thời gian thực cho PWA và POS
     - `KitchenHub` (`/hubs/kitchen`): Truyền tải đơn hàng mới, cập nhật trạng thái pha chế KDS, 86-toggle
     - `PaymentHub` (`/hubs/payments`): Bắn tín hiệu xác nhận thanh toán VietQR Webhook tới PWA và Staff POS
     - `NotificationHub` (`/hubs/notifications`): Chuông gọi phục vụ tại bàn, cảnh báo review <= 2 sao, alert quản lý

2. In `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tom_Tat_1_Trang_Executive_Summary.md`:
   - Line 95: Fix feature breakdown to exactly: `(22 Khách hàng C-01–C-22, 13 Nhân viên S-01–S-13, 12 Quản lý M-01–M-12, 17 Chủ chuỗi A-01–A-17)`.

3. In `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`:
   - Line 421: Change `TableHub` to `NotificationHub`.

4. In `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`:
   - Section 7.2: Ensure the numbered list of database entities contains exactly 25 entities matching 1:1 with `Tong_Quan_Kien_Truc_He_Thong.md` (`Branches`, `BranchWifiConfigs`, `Users`, `Roles`, `UserRoles`, `AuditLogs`, `Categories`, `Products`, `ProductSizes`, `ProductBranchPrices`, `Modifiers`, `ProductModifiers`, `Ingredients`, `RecipesBOM`, `Tables`, `Orders`, `OrderItems`, `OrderItemModifiers`, `Payments`, `Customers`, `LoyaltyCupTransactions`, `Vouchers`, `CustomerReviews`, `Shifts`, `Attendances`).

5. Delete the obsolete file `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Xem.html`.

6. Run empirical validation across all 5 files:
   - `grep "C-23"` -> 0 results
   - `grep "C-24"` -> 0 results
   - `grep "TODO"` -> 0 results
   - `grep "TBD"` -> 0 results
   - Verify table formatting and Mermaid syntax across all 5 files.

Write your report to `d:\Idea_DoAn\.agents\remediation_5docs_worker\report.md` and handoff to `d:\Idea_DoAn\.agents\remediation_5docs_worker\handoff.md`.
Communicate when done via send_message to parent.
