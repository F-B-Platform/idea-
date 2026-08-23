## 2026-08-23T14:36:04Z
You are an Explorer subagent for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\explorer_survey_db\
Create your working directory if needed.
Read the following files carefully:
1. `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`
2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
3. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md`
4. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md`
5. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`

Your task:
Analyze and map out the complete PostgreSQL 16 schema and seed data to rewrite `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md`.
1. Verify the 25 tables 3NF: branches, users, roles, categories, menu_items, item_sizes, ingredients, recipes/BOM, tables, orders, order_items, payments, shifts, timekeepings, inventory_checks, z_reports, combo_suggestions, branch_menu_items, promotions, etc.
2. Ensure complete DDL definition with PostgreSQL types (UUID, VARCHAR, NUMERIC, TIMESTAMPTZ, JSONB, ENUM), Foreign Keys with ON DELETE constraints, Indexes (BTREE, GIN for JSONB/Search), and updated_at trigger functions.
3. Design 100% complete, realistic Seed Data DML:
   - 3 branches (Chi nhánh Quận 1, Cầu Giấy, Hải Châu) with exact BSSID, Subnet CIDR IP, Address, Phone.
   - 20+ realistic menu items across categories (Cà phê, Trà sữa, Trà trái cây, Bánh ngọt, Đồ ăn vặt), with item sizes (S/M/L, price deltas).
   - Ingredients in grams/ml/units with unit costs and safety thresholds.
   - Recipes (BOM) linking menu_items/sizes to ingredients with exact gram/ml amounts.
   - 10+ Users & Accounts: 1 Admin, 3 Branch Managers, 6 Staff (Barista, Cashier), 10 CRM Customers with points and loyalty tier.
   - Sample Orders across all 3 channels (Dine-In A/B, Delivery with 20k ship fee, Takeaway).
   - Shifts, WiFi Attendance records, Inventory count checks, Z-Reports, AI-2 Combo suggestions.
4. Ensure ZERO placeholders (No TODO, no ellipses, no partial scripts).

Write your detailed findings to `d:\Idea_DoAn\.agents\explorer_survey_db\analysis.md` and `d:\Idea_DoAn\.agents\explorer_survey_db\handoff.md`.
Then send a message to parent with the summary and report path.
