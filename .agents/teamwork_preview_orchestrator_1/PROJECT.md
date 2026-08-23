# Project: Standardize 9 Technical Process Documentation Files (v2.5.0)

## Architecture
Standardizing 9 comprehensive engineering process manuals in `03_Quy_Trinh_Trien_Khai/` based on the authoritative v2.5.0 specification in `01_Tai_Lieu_Dac_Ta_Goc/`.

## Feature Inventory (62 Core Features Across 4 Actors)
| # | Feature Code | Feature Name | Actor | Assigned Milestone | Status |
|---|-------------|--------------|-------|--------------------|--------|
| 1-20 | C-01 ~ C-20 | Customer Features (20 features) | Customer | M1, M2, M3, M4, M5 | 100% DONE |
| 21-33 | S-01 ~ S-13 | Staff Features (13 features) | Staff | M1, M2, M3, M4, M5 | 100% DONE |
| 34-45 | M-01 ~ M-12 | Manager Features (12 features) | Manager | M1, M2, M3, M4, M5 | 100% DONE |
| 46-62 | A-01 ~ A-17 | Admin Features (17 features) | Admin | M1, M2, M3, M4, M5 | 100% DONE |

## Milestones & Status
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M0 | Survey & Mapping | Deep analysis of 01_ specs vs 03_ existing docs | none | DONE |
| M1 | Requirements & Database | `01_Phan_Tich_Yeu_Cau.md`, `02_Thiet_Ke_Database.md` | M0 | DONE |
| M2 | API Contracts & UI/UX | `03_Thiet_Ke_API_Contract.md`, `04_Thiet_Ke_UI_UX.md` | M1 | DONE |
| M3 | Backend & Frontend Processes | `05_Quy_Trinh_Backend.md`, `06_Quy_Trinh_Frontend.md` | M2 | DONE |
| M4 | Testing, DevOps & README | `07_Ke_Hoach_Kiem_Thu.md`, `08_Trien_Khai_He_Thong.md`, `README.md` | M3 | DONE |
| M5 | Final Comprehensive Verification | Global cross-file review, challenging & forensic audit | M4 | DONE (Gate PASS) |

## Standardized Deliverables in `03_Quy_Trinh_Trien_Khai/`
1. `01_Phan_Tich_Yeu_Cau.md`: 62 Core Features, NFRs, 4 Core Workflows, Traceability Matrix (DONE)
2. `02_Thiet_Ke_Database.md`: 25 3NF PostgreSQL 16 Tables, UUID PKs, DDL, Indexes, Triggers, EF Core 8 (DONE)
3. `03_Thiet_Ke_API_Contract.md`: 10 RESTful API Groups, 4 SignalR Hubs, PayOS HMAC-SHA256 & Redis Lock (DONE)
4. `04_Thiet_Ke_UI_UX.md`: 5 Route Groups Next.js 14 App Router, Design Tokens, 20 Wireframes (DONE)
5. `05_Quy_Trinh_Backend.md`: Clean Architecture .NET 8, MediatR CQRS, Redis RedLock, SignalR, Gemini + Apriori (DONE)
6. `06_Quy_Trinh_Frontend.md`: Next.js 14, TypeScript, Tailwind, Shadcn UI, 5 Zustand Stores, SignalR Client Hooks, PWA (DONE)
7. `07_Ke_Hoach_Kiem_Thu.md`: Testing Pyramid, 3 Sales Channels, 10 Critical Edge Cases, k6, SignalR Stress, RBAC (DONE)
8. `08_Trien_Khai_He_Thong.md`: Docker Compose 5 Containers, NGINX SSL WebSocket, GitHub Actions CI/CD, Backup/Restore (DONE)
9. `README.md`: Master Index, End-to-End Master Traceability Matrix, Quick Start, Deprecation Table (DONE)
