# Project: Standardizing Architecture Diagrams v2.5.0

## Architecture
This project standardizes all technical architecture and design artifacts for the Smart F&B Operating System (v2.5.0) in folder `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\`.

### System Overview
- **Frontend**: Single responsive Next.js 14 Web Application divided into 5 Route Groups:
  - `(customer)`: PWA QR Order, Dine-in, Delivery, Loyalty & Feedback
  - `(pos)`: Counter Cashier, Takeaway Order, Table Management, Shift Z-Report
  - `(kitchen)`: KDS (Kitchen Display System) with realtime ticket status & 86-toggle
  - `(admin)`: Management Portal (Menu, BOM, Warehouse, Staff, AI insights)
  - `(auth)`: JWT authentication, Role-based access control (RBAC), WiFi Check-in
- **Backend**: .NET 8 Clean Architecture:
  - `Domain`: Enterprise entities, value objects, domain events, business invariants
  - `Application`: Use cases, CQRS commands/queries, MediatR, FluentValidation, DTOs
  - `Infrastructure`: EF Core PostgreSQL 16, Redis 7 (Caching + RedLock), External Adapters (PayOS, Gemini 1.5 Flash, Weather API, AWS S3 / Cloudflare R2)
  - `WebApi`: REST API endpoints, SignalR Hubs (`/hubs/orders`, `/hubs/kitchen`, `/hubs/payments`, `/hubs/notifications`), JWT Auth Middleware, Global Exception Handling
- **Database**: PostgreSQL 16 relational store with 31 normalized 3NF tables + Redis 7 caching and distributed locking.

## Feature Inventory
| # | Feature / Artifact | Description | Target File | Source |
|---|--------------------|-------------|-------------|--------|
| 1 | C4 Architecture Model (L1, L2, L3) | Context, Container, Component diagrams + Next.js Route Groups + SignalR Hubs + Redis | `01_Kien_Truc_Tong_Quan.md` | SoT Docs |
| 2 | Sequence Diagrams (Seq-01 to Seq-10) | 10 end-to-end operational workflows with full payloads & participants | `02_Sequence_Diagrams.md` | SoT Docs |
| 3 | Database ERD (31 Tables 3NF) | Complete Mermaid ERD diagram with types, PK, FK, relations | `03_ERD_Database_Diagram.md` | 02_Thiet_Ke_Database.md |
| 4 | Deployment Topology & Cloud Comparison | Mermaid deployment architecture + Linux VPS vs Azure comparison table | `04_Deployment_Diagram.md` | 04_Deployment_Diagram.md |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | R1: Architecture Overview | `01_Kien_Truc_Tong_Quan.md` | SoT Docs | DONE |
| M2 | R2: Sequence Diagrams | `02_Sequence_Diagrams.md` | SoT Docs | DONE |
| M3 | R3: Database ERD Diagram | `03_ERD_Database_Diagram.md` | 02_Thiet_Ke_Database.md | DONE |
| M4 | R4: Deployment Diagram | `04_Deployment_Diagram.md` | SoT Docs | DONE |
| M5 | Quality Gate & Verification | 2 Reviewers, 2 Challengers, 2 Auditors | M1-M4 | DONE (100% UNANIMOUS PASS) |

## Code Layout
- Target Directory: `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\`
  - `01_Kien_Truc_Tong_Quan.md` (768 lines, 64 KB)
  - `02_Sequence_Diagrams.md` (920 lines, 69 KB)
  - `03_ERD_Database_Diagram.md` (1441 lines, 91 KB)
  - `04_Deployment_Diagram.md` (1019 lines, 62 KB)
- Working Directory: `d:\Idea_DoAn\.agents\teamwork_preview_orchestrator_diagrams\`
