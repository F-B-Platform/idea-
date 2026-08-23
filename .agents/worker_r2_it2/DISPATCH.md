## 2026-08-23T13:58:30Z
Bạn là Senior Solution Architect (Worker R2 - Iteration 2). Nhiệm vụ của bạn là hoàn thiện và nâng cấp sâu tệp:
`d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md`

Thư mục làm việc của bạn: `d:\Idea_DoAn\.agents\worker_r2_it2\`
Tạo file `progress.md` và `handoff.md`.

Nguồn sự thật đối chiếu:
- `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md` (Đối chiếu danh pháp bảng và cột chuẩn 100%)
- `d:\Idea_DoAn\.agents\challenger_1\handoff.md` (Đọc kỹ các phát hiện của Challenger 1)
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`

Nhiệm vụ chỉnh sửa bắt buộc trên `02_Sequence_Diagrams.md`:
1. **Đồng bộ hóa 100% Danh pháp Bảng Cơ sở Dữ liệu với `03_ERD_Database_Diagram.md`**:
   - Sử dụng chính xác các tên bảng chuẩn 3NF:
     - `product_recipes` (thay vì `ProductBOMs`)
     - `inventory_stocks` (thay vì `Ingredients.CurrentStock`)
     - `inventory_logs` (thay vì `InventoryTransactions`)
     - `users`, `roles`, `user_roles` (thay vì `BranchUsers`)
     - `staff_attendances` (thay vì `Attendances`)
     - `customer_feedbacks` (thay vì `CustomerReviews`)
     - `work_shifts` (thay vì `Shifts`)
     - `shift_handover_discrepancies` (thay vì `ShiftDiscrepancies`)
     - `delivery_orders` (thay vì `Deliveries`)
     - `loyalty_cup_transactions` (thay vì `LoyaltyTransactions`)
   - Đồng bộ tên cột: `current_stock`, `reserved_stock`, `min_threshold`, `bssid_list`, `allowed_ip_subnets`, `cups_count`, `rating`, `sentiment_score`, `discrepancy_amount`, `is_approved`.

2. **Bổ sung Cơ chế Giữ tồn kho tạm thời (Soft Inventory Reservation) trong Seq-01 và Seq-03**:
   - Khi tạo đơn hàng trả trước VietQR (trạng thái `PendingPayment`, hạn quét QR 10 phút):
   - Hệ thống dùng RedLock kiểm tra tồn kho khả dụng (`available_stock = physical_stock - reserved_stock >= required_bom_qty`).
   - Tạm giữ số lượng nguyên liệu trong Redis (`HINCRBY inventory:reserved:{branch_id} {ingredient_id} {qty}` với TTL 600s).
   - Đổi trạng thái bàn thành `PendingPayment` trong DB/Redis để chặn đơn trùng.
   - Khi Webhook PayOS báo thanh toán thành công: Chuyển sang `Paid` -> Trừ trực tiếp `inventory_stocks` (vĩnh viễn) và giải phóng `inventory:reserved`, ghi `inventory_logs`.
   - Nếu hết hạn 10 phút hoặc hủy đơn: Release reservation trong Redis (`HINCRBY -qty`) và mở khóa bàn.

3. **Bảo đảm 100% cú pháp Mermaid hợp lệ** và không làm mất bất kỳ chi tiết payload hay participant nào của 10 sơ đồ tuần tự.
