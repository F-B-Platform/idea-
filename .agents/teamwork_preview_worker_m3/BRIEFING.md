# BRIEFING — 2026-08-23T20:30:00+07:00

## Mission
Standardize and completely rewrite 05_Quy_Trinh_Backend.md (.NET 8 Clean Architecture) and 06_Quy_Trinh_Frontend.md (Next.js 14 App Router) according to v2.5.0 specification with zero placeholders.

## 🔒 My Identity
- Archetype: implementer, qa, specialist
- Roles: implementer, qa, specialist
- Working directory: d:\Idea_DoAn\.agents\teamwork_preview_worker_m3\
- Original parent: 56614ba6-9550-4aba-ae35-c6047e7bcd93
- Milestone: M3 (Backend & Frontend Processes)

## 🔒 Key Constraints
- 62 Core Features (20 Customer C-01..C-20, 13 Staff S-01..S-13, 12 Manager M-01..M-12, 17 Admin A-01..A-17)
- 25 3NF Database Tables (PostgreSQL 16)
- Clean Architecture 4 Layers in .NET 8 C# (.Domain, .Application, .Infrastructure, .WebAPI)
- Next.js 14 App Router (5 route groups: (customer), (kds), (staff), (manager), (admin))
- Zero placeholders (no TODO, no TBD, no ... or ellipses in code)
- 100% elimination of Staff Mobile App, GPS 50m, QR 30s, C-23, C-24, separate voucher wallet
- All code, Mermaid diagrams, and markdown blocks must be valid and production-grade

## Current Parent
- Conversation ID: 56614ba6-9550-4aba-ae35-c6047e7bcd93
- Updated: 2026-08-23T20:30:00+07:00

## Task Summary
- **What to build**: Full standard production manuals for Backend (`05_Quy_Trinh_Backend.md`) and Frontend (`06_Quy_Trinh_Frontend.md`)
- **Success criteria**: 100% sync with 01..04 deliverables, full C# and TypeScript code, zero placeholder, valid Mermaid diagrams, full real-time and business rules.
- **Interface contracts**: `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`, `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md`
- **Code layout**: `d:\Idea_DoAn\.agents\teamwork_preview_orchestrator_1\PROJECT.md`

## Key Decisions Made
- `05_Quy_Trinh_Backend.md`: Implemented .NET 8 Clean Architecture with MediatR CQRS, 4 Pipeline Behaviors, EF Core 8 with 25 tables, Redis Cache-Aside & RedLock distributed locking, SignalR 4 Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) with Redis Backplane, PayOS HMAC SHA256 Webhook processor, Gemini 1.5 Flash RAG Client, Apriori Algorithm Market Basket Engine, RFC 7807 Global Exception Middleware, Rate Limiting, JWT & RBAC.
- `06_Quy_Trinh_Frontend.md`: Implemented Next.js 14 App Router with 5 Route Groups, 5 full TypeScript Zustand Stores (`useCartStore`, `usePosStore`, `useShiftStore`, `useKdsStore`, `useAuthStore`), TanStack Query v5, SignalR client hook (`useSignalRHub`), Web Audio API chime sound synthesizer (`useAudioAlert`), and Workbox Service Worker PWA offline caching.

## Change Tracker
- **Files modified**:
  * `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md` — 81.8 KB, completely standardized.
  * `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md` — 50.3 KB, completely standardized.
- **Build status**: All verification checks passed (zero placeholders, syntax valid).
- **Pending issues**: None.

## Quality Status
- **Build/test result**: Passed
- **Lint status**: 0 violations
- **Tests added/modified**: Unit test sample & verification procedures included.

## Loaded Skills
- **Source**: `C:\Users\nqtha\.gemini\config\skills\lead-backend-engineer\SKILL.md`
  - **Local copy**: `d:\Idea_DoAn\.agents\teamwork_preview_worker_m3\skills\lead-backend-engineer.md`
  - **Core methodology**: .NET 8 Clean Architecture, MediatR CQRS, EF Core, Redis, SignalR, PayOS Webhook, API specs.
- **Source**: `C:\Users\nqtha\.gemini\config\skills\frontend-developer\SKILL.md`
  - **Local copy**: `d:\Idea_DoAn\.agents\teamwork_preview_worker_m3\skills\frontend-developer.md`
  - **Core methodology**: Next.js 14 App Router, Zustand, React 19 / TanStack Query, Tailwind, PWA.
- **Source**: `C:\Users\nqtha\.gemini\config\skills\output-skill\SKILL.md`
  - **Local copy**: `d:\Idea_DoAn\.agents\teamwork_preview_worker_m3\skills\output-skill.md`
  - **Core methodology**: Full output enforcement, zero placeholder, unabridged production code.

## Artifact Index
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md` — Backend Implementation & Architecture Guide
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md` — Frontend Implementation & Architecture Guide
- `d:\Idea_DoAn\.agents\teamwork_preview_worker_m3\handoff.md` — Handoff Report
