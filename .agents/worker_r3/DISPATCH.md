# DISPATCH - 2026-08-23T13:49:19Z

## Nhiệm vụ:
Senior Database Architect chịu trách nhiệm viết lại hoàn chỉnh tệp:
`d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md` (v2.5.0)

## Nguồn sự thật:
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`

## Yêu cầu cốt lõi:
1. Sơ đồ Mermaid `erDiagram` chuẩn hóa toàn bộ 25 bảng (3NF) chia theo các module nghiệp vụ:
   - Core / Auth & RBAC (Users, Roles, UserRoles, Permissions, RolePermissions, RefreshTokens)
   - Chi nhánh & Bàn (Branches, BranchWifiConfigs, Tables, TableQrCodes)
   - Thực đơn & Sản phẩm (Categories, Products, ProductSizes, Toppings, ProductToppings)
   - Định lượng & Kho hàng BOM (Ingredients, ProductRecipes, InventoryStocks, InventoryLogs)
   - Đơn hàng & Thanh toán (Orders, OrderItems, OrderItemToppings, Payments, Transactions)
   - Giao hàng & Vận chuyển (DeliveryOrders)
   - Khách hàng thân thiết & Đánh giá (Customers, LoyaltyCupTransactions, CustomerFeedbacks)
   - Ca làm việc & Chấm công (WorkShifts, StaffAttendances, ShiftHandoverDiscrepancies)
2. Cú pháp Mermaid `erDiagram` chuẩn, đầy đủ kiểu dữ liệu, PK, FK, UK, quan hệ chính xác.
3. Data Dictionary chi tiết từng bảng.
4. Chiến lược Indexing & Tối ưu hiệu năng.
5. Zero Placeholders 100%.
