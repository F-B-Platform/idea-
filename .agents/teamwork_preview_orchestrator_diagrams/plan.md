# Master Plan: Architecture Diagrams Modernization (v2.5.0)

## Objective
Upgrade and standardize all 4 architectural documentation files under `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\` to be 100% compliant with v2.5.0 specifications, zero placeholders, complete Mermaid diagrams, and professional Markdown styling.

## Milestones & Work Breakdown
1. **Milestone R1: System Architecture Overview (`01_Kien_Truc_Tong_Quan.md`)**
   - C4 Context (L1), C4 Container (L2), C4 Component (L3 - Clean Architecture .NET 8).
   - 5 Next.js 14 Route Groups (`(customer)`, `(pos)`, `(kitchen)`, `(admin)`, `(auth)`).
   - 4 SignalR Realtime Hubs (`/hubs/order`, `/hubs/kitchen`, `/hubs/service`, `/hubs/notification`).
   - Redis 7 Caching & Distributed Locks (`RedLock` for inventory & seat state).
   - AI Engine integration (Gemini 1.5 Flash + Apriori Market Basket Analysis).
   - Complete purging of obsolete legacy terms: Staff App, GPS 50m, QR 30s, C-23/C-24.

2. **Milestone R2: Sequence Diagrams Suite (`02_Sequence_Diagrams.md`)**
   - Minimum 10 detailed Mermaid Sequence Diagrams (Seq-01 -> Seq-10) with exact participants, message payloads, error flows, and alternative branches:
     - Seq-01: Dine-In Branch A (Prepaid VietQR via PayOS)
     - Seq-02: Dine-In Branch B (Postpaid Cash / Bill QR at Counter)
     - Seq-03: QR Delivery (20,000 VND flat fee, 100% Prepaid VietQR, address validation)
     - Seq-04: Takeaway Web POS (Counter POS, 10 cups earn 1 free cup loyalty)
     - Seq-05: WiFi Attendance Check-in (Branch BSSID + IP subnet verification)
     - Seq-06: KDS & Realtime Inventory Depletion (BOM gam/ml deduction + 86-Toggle Sold-out)
     - Seq-07: Call Service & Staff Realtime Response (Table assistance SignalR push)
     - Seq-08: Customer Feedback & Rating (1-5 stars with Red Alert on rating <= 2 stars)
     - Seq-09: Shift Open/Close & Z-Report Reconcilation (>50,000 VND variance mandatory explanation)
     - Seq-10: Admin Operations (Menu CRUD, BOM Recipe, Seasonal Product, AI-2 Demand Forecasting)

3. **Milestone R3: Database ERD Diagram (`03_ERD_Database_Diagram.md`)**
   - Standardized 25-table 3NF schema rendered via Mermaid `erDiagram`.
   - Explicit data types, primary keys (PK), foreign keys (FK), column descriptions, and relational cardinalities.
   - Comprehensive inclusion of v2.5.0 tables: `delivery_address`, `delivery_fee`, `BranchWifiConfigs`, `LoyaltyCupTransactions`, `ShiftHandoverDiscrepancies`, `InventoryLogs`, `BomRecipes`, etc.

4. **Milestone R4: Infrastructure & Deployment Diagram (`04_Deployment_Diagram.md`)**
   - Mermaid Deployment Topology diagram covering Client Edge, NGINX SSL Reverse Proxy Ingress, .NET 8 Clean Architecture App Container, PostgreSQL 16 & Redis 7 cluster, External Integrations (PayOS, Gemini AI, Weather API, AWS S3 / Cloudflare R2).
   - Production-grade deployment matrix & Comprehensive Trade-off Comparison: Cloud VPS Linux (Docker Compose) vs. Azure Singapore Cloud Native (AKS/App Service).

5. **Milestone Review & Verification Gate**
   - Reviewer check for Mermaid syntax correctness and rendering.
   - Challenger check for edge cases, payload completeness, and consistency across diagrams.
   - Forensic Auditor check for zero placeholder, zero cheating/simplification, and 100% v2.5.0 alignment.
