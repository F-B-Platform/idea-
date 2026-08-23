# Project: Smart F&B Operating System — 05_Quy_Chuan_&_Test_Cases Upgrade

## Architecture
- **Domain**: F&B Enterprise Multi-Branch Management & Real-time POS/KDS System (v2.5.0)
- **Tech Stack**: Backend .NET 8 (Clean Architecture, CQRS, MediatR, EF Core), Frontend Next.js 14 (TypeScript Strict, App Router, Tailwind CSS), Database PostgreSQL 16 (29 Tables 3NF).
- **Core Channels**: Dine-In (Branch A Prepaid VietQR vs Branch B Postpaid Cash/VietQR), QR Delivery (20k ship, 100% Prepaid VietQR, No COD), Takeaway (POS counter, Loyalty 10-cup stamp).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---|---|---|---|
| 1 | UAT Test Cases & 5-Min Linked Demo | 47 full UAT cases, 5-min demo, 10 edge cases | M1 | Workflow_Quy_Trinh_Nghiep_Vu.md, 07_Ke_Hoach_Kiem_Thu.md |
| 2 | PostgreSQL 16 DDL & Seed Data Script | Full 29 tables 3NF, audit triggers, realistic seed data | M2 | 02_Thiet_Ke_Database.md, 03_ERD_Database_Diagram.md |
| 3 | GitFlow, PR, CI/CD & Coding Standards | Branching, Conventional Commits, PR Lifecycle, .NET 8 & Next.js 14 rules | M3 | Master Spec v2.5.0, Clean Architecture |
| 4 | Global Quality Gate & Integrity Forensics | Review, Challenger tests, Zero Placeholder Forensic Audit | M4 | Rule Zero Placeholder, Forensic Integrity |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M0 | Survey Phase | 3 Parallel Explorers investigating truth sources | none | DONE |
| M1 | Upgrade UAT_Test_Cases.md | Kịch bản Demo 5p liên hoàn + 47 Test cases UAT + 10 Edge cases | M0 | DONE |
| M2 | Upgrade Seed_Data_&_Database_Script.md | PostgreSQL 16 Script (29 tables 3NF) + Full Seed Data | M0 | DONE |
| M3 | Upgrade Git_Workflow_&_Branching_Strategy.md | GitFlow + Commits + PR + .NET 8/Next.js 14 Standards | M0 | DONE |
| M4 | Verification & Audit | Multi-Reviewer, Challenger, Forensic Auditor Gate | M1, M2, M3 | DONE |

## Code Layout
- Target Files Upgraded:
  - `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md` (1,449 lines, 99.5 KB)
  - `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md` (1,733 lines, 125.2 KB)
  - `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md` (2,371 lines, 111.7 KB)
- Total Documentation: 5,553 lines / 336.4 KB across all 3 upgraded specification files.
