# Master Plan — Upgrade 05_Quy_Chuan_&_Test_Cases

## Objective
Rewrite, upgrade, and standardize all 3 documentation files in `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\` according to Master Spec v2.5.0, 4 Actors / 62 Features RBAC, 16 Workflows, 25 Database Tables 3NF, Test Plan, and Sequence/ERD diagrams.

## Phase Breakdown

### Phase 0: Survey & Architecture Alignment (3 Parallel Explorers)
- **Explorer 1 (Domain: UAT & Workflows)**: Analyzes `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md`, `Smart_FB_Operating_System.md`, `Actor_Phan_Quyen_Chuc_Nang.md`, `03_Quy_Trinh_Trien_Khai/07_Ke_Hoach_Kiem_Thu.md`, and current `05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md`. Extracts all 35+ test cases, 5-min continuous demo flow, and 10 edge scenarios.
- **Explorer 2 (Domain: Database Schema & Seed Data)**: Analyzes `03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md`, `04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md`, and current `05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md`. Maps all 25 3NF tables, foreign keys, triggers, enum types, and realistic seed data (3 branches, 20+ items, recipes BOM in g/ml, 10 CRM users, orders, shifts, inventory checks, z-reports).
- **Explorer 3 (Domain: Git Flow & Standards)**: Analyzes tech stack (.NET 8 Clean Architecture, Next.js 14 App Router), `05_Quy_Chuan_&_Test_Cases/Git_Workflow_&_Branching_Strategy.md`, SonarQube rules, CI/CD gates, PR templates, and coding conventions.

### Phase 1: Implementation / Document Production (3 Parallel Dedicated Workers)
- **Worker 1 (Target: `UAT_Test_Cases.md`)**: Fully rewrites `UAT_Test_Cases.md` with:
  1. Kịch bản Demo 5 phút kết nối liên hoàn (7 vai diễn / phân cảnh kết nối liên tục từ Khách Dine-In A/B, Delivery, Takeaway, Chấm công WiFi, KDS Barista BOM & 86-Toggle, Quản lý Z-Report, Admin AI-2 Combo).
  2. 35+ chi tiết Test Cases UAT chuẩn bảng (TC-DINE-01A, TC-DINE-01B, TC-DEL-01, TC-TAKE-01, TC-ATT-01, TC-KDS-01, TC-MGR-01, TC-ADM-01, TC-EDGE-01~10, và các test cases bổ sung).
  3. GitHub Callouts, 100% Zero Placeholders, Không chứa thuật ngữ lỗi thời.
- **Worker 2 (Target: `Seed_Data_&_Database_Script.md`)**: Fully rewrites `Seed_Data_&_Database_Script.md` with:
  1. 100% Complete PostgreSQL 16 SQL Script (DDL for 25 tables 3NF, indexes, constraints, audit triggers).
  2. Complete realistic DML Seed Data: 3 branches (Q1, Cầu Giấy, Hải Châu) with BSSID/IP; 20+ menu items with S/M/L sizes; BOM recipes with g/ml; Users (1 Admin, 3 Managers, 6 Staff, 10 CRM Customers); Orders for Dine-In A/B, Delivery, Takeaway; Shifts, WiFi attendance, Inventory checks, Z-reports, AI combo suggestions.
  3. Zero placeholders, zero ellipses, valid PostgreSQL syntax.
- **Worker 3 (Target: `Git_Workflow_&_Branching_Strategy.md`)**: Fully rewrites `Git_Workflow_&_Branching_Strategy.md` with:
  1. GitFlow branching model (main, develop, feature/*, release/*, hotfix/*).
  2. Conventional Commits standards with scopes and examples.
  3. Pull Request lifecycle, PR template, Code review checklist, CI/CD quality gates.
  4. .NET 8 & Next.js 14 coding standards with real, comprehensive code examples.

### Phase 2: Verification, Adversarial Challenge & Forensic Audit
- **Reviewer 1**: Reviews `UAT_Test_Cases.md` and `Git_Workflow_&_Branching_Strategy.md` against Master Spec v2.5.0.
- **Reviewer 2**: Reviews `Seed_Data_&_Database_Script.md` for SQL syntax correctness, 25 tables 3NF compliance, foreign key integrity, and seed data completeness.
- **Challenger / Critic**: Adversarially checks for missing test cases, broken logic, obsolete terms (Staff Mobile App, GPS 50m, 30s QR, C-23/C-24), and placeholder patterns.
- **Auditor**: Performs zero-placeholder and forensic integrity verification across all 3 files.

### Phase 3: Gate Evaluation & Final Synthesis
- Verify all gate criteria.
- Summarize changes and produce handoff report.
