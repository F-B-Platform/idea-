# Original User Request

## Initial Request — 2026-08-23T21:35:18+07:00

You are the PROJECT ORCHESTRATOR for the Smart F&B Operating System project.

Working Directory: d:\Idea_DoAn\.agents\orchestrator_1\
Original Request File: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md
Workspace Root: d:\Idea_DoAn\

Your mission:
Fully rewrite, upgrade, and standardize all 3 files in `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\` to reflect 100% accurately the v2.5.0 system architecture and business logic.

## Reference Sources of Truth:
1. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md` (Master Spec v2.5.0)
2. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md` (4 Actors, 62 Core Features RBAC)
3. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md` (16 Business Workflows)
4. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md` (25 Tables 3NF PostgreSQL Schema)
5. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md` (Test Plan)
6. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md` (10 Sequence Diagrams)
7. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md` (ERD Diagram)

## Target Files to Upgrade:
1. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`
   - Kịch bản Demo 5 phút kết nối liên hoàn: Khách đặt Dine-In 2 nhánh, QR Delivery, Takeaway quầy POS tích 10 ly, Chấm công WiFi, KDS Barista BOM & 86-Toggle, Quản lý Z-Report, Admin AI-2 Combo.
   - 35+ Test Cases UAT chi tiết (Mã test, Mục đích, Tiền điều kiện, Các bước thực hiện, Dữ liệu đầu vào, Kết quả kỳ vọng, Trạng thái):
     * TC-DINE-01A: Dine-In Nhánh A VietQR trả trước (PayOS Webhook -> KDS nhận khi Paid).
     * TC-DINE-01B: Dine-In Nhánh B Tiền mặt trả sau (KDS nhận ngay `Confirmed` -> In bill kèm VietQR -> Khách trả tiền mặt hoặc quét VietQR trên bill -> NV xác nhận).
     * TC-DEL-01: QR Delivery (SĐT + Địa chỉ bắt buộc, Phí ship 20k, 100% VietQR trước, Khóa COD).
     * TC-TAKE-01: Takeaway Web POS (Tra cứu CRM SĐT, Tích 10 ly tặng 1 ly, Thu tiền sau).
     * TC-ATT-01: Chấm công Khóa mạng WiFi (Đúng BSSID/IP -> Pass; Sai WiFi/4G -> Từ chối).
     * TC-KDS-01: KDS Bếp, Công thức BOM trừ kho theo gam/ml, Công tắc 86-Toggle & Undo 10s.
     * TC-MGR-01: Mở/kết ca két tiền & Đối soát Z-Report (giải trình khi chênh lệch > 50k).
     * TC-ADM-01: Admin Full CRUD món, Seasonal Menu, Bảng giá vùng & Phê duyệt AI-2 Combo Apriori.
     * TC-EDGE-01~10: Ma trận 10 kịch bản biên và ngoại lệ vận hành.
     * Plus additional comprehensive test cases across all modules to exceed 35+ cases.

2. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md`
   - 100% Complete PostgreSQL 16 SQL Script (Zero TODOs, Zero placeholders, syntax-checked and executable).
   - Full 25 tables 3NF: branches, users, roles, categories, menu_items, item_sizes, ingredients, recipes/BOM, tables, orders, order_items, payments, shifts, timekeepings, inventory_checks, z_reports, combo_suggestions, etc.
   - Realistic seed data: 3 branches (Q1, Cau Giay, Hai Chau) with WiFi BSSID/Subnet IP; 20+ realistic menu items with sizes (S/M/L) and BOM recipes in grams/ml; Accounts (1 Admin, 3 Branch Managers, 6 Staff, 10 CRM Customers with points/loyalty); Orders for all 3 channels (DineIn A/B, Delivery with 20k ship fee, Takeaway); Shifts, WiFi Attendance records, Inventory checks, and Z-Reports.

3. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md`
   - GitFlow branching strategy (main, develop, feature/*, release/*, hotfix/*).
   - Conventional Commits specifications (feat:, fix:, refactor:, docs:, test:, chore:).
   - Pull Request lifecycle (PR Template, Code Review Checklist, CI/CD Gates: SonarQube, Unit Tests, Build verification).
   - Coding Standards for .NET 8 (C# Clean Code, CQRS, MediatR, FluentValidation, Error handling) and Next.js 14 (TypeScript Strict, App Router, ESLint, Prettier, Tailwind CSS, Component architecture).

## Key Constraints:
- Zero Placeholders: Absolute 100% completeness. No `TODO`, no `/* rest of code */`.
- Elimination of outdated references: No Staff Mobile App, No GPS 50m, No 30s QR, No C-23/C-24.
- Beautiful Markdown with GitHub Alert Callouts (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`).
- Maintain `progress.md` and `plan.md` in `d:\Idea_DoAn\.agents\orchestrator_1\` continuously.
- When done, send a detailed completion message to parent.
