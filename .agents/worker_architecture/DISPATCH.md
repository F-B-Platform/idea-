## 2026-08-22T15:11:22Z
You are worker_architecture (TypeName: teamwork_preview_worker).
Your working directory is: d:\Idea_DoAn\.agents\worker_architecture\
Your exclusive write target is: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md`

Input References to Read First:
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md` (specifically latest follow-up)
- `d:\Idea_DoAn\temp_revised_content.txt`
- `d:\Idea_DoAn\.agents\spec_miner_doc_truth\report.md`
- `d:\Idea_DoAn\.agents\explorer_5docs_diff\report.md`
- `d:\Idea_DoAn\.agents\spec_miner_workflows_actors\report.md`

Your Mission:
Completely rewrite `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md` with 100% full, comprehensive, professional Markdown content:
1. Web-First Monorepo Architecture Overview:
   - Frontend: Next.js 14 App Router Monorepo (Customer PWA, Staff Web POS & KDS, Manager Web Portal, Admin Executive Portal).
   - Backend: .NET 8 Web API, Clean Architecture (Domain, Application, Infrastructure, WebAPI), MediatR CQRS, FluentValidation.
   - Database: PostgreSQL 16 (25 normalized entities in 3NF).
   - Caching & Locking: Redis 7 (Cache-aside, Distributed Locks, SignalR backplane).
   - Real-time: SignalR WebSockets (OrderHub, KitchenHub, PaymentHub, NotificationHub).
   - AI Services: Google Gemini 1.5 Flash SDK (RAG Chatbot AI-1) + Apriori/FP-Growth (Combo Mining AI-2).
   - Payment Gateway: PayOS / VietQR Webhook.
2. Complete elimination of Staff Mobile App container/component from all diagrams and descriptions (all staff operations run on Web Responsive).
3. 3 Types of QR Architecture & Data Flow:
   - Table QR (Dine-In)
   - Delivery QR (Delivery with 20k fee & mandatory address)
   - Attendance QR (WiFi-locked check-in)
4. Dine-In 2 Payment Paths data flows (VietQR pre-pay vs Cash post-pay with bill QR).
5. Takeaway Web POS architecture (CRM phone lookup, 10 cups loyalty, post-payment).
6. 100% Valid Mermaid diagrams:
   - C4 Context Diagram
   - C4 Container Diagram
   - Layered Clean Architecture Diagram
   - SignalR Real-Time Event Architecture Diagram
   - Database ERD Diagram (25 entities, `OrderType` enum `DineIn`/`TakeAway`/`Delivery`, `delivery_address`, `delivery_fee`, `WiFiConfig`, `BOM`, `Loyalty`, etc.)
   - Deployment & Security Topology Diagram
7. Non-Functional Requirements (Performance, Security, Reliability, Scalability).
8. Core MVP vs Scale Up / Future Work boundary. Total deletion of C-23 & C-24. Zero Placeholders.
