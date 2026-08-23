# 🏛️ SƠ ĐỒ THIẾT KẾ KIẾN TRÚC HỆ THỐNG TỔNG QUAN (SYSTEM ARCHITECTURE SPECIFICATION)
## Smart F&B Operating System — AI-Powered QR Order & Multi-Channel Management Platform

> [!NOTE]
> **Tài liệu:** Bản Đặc Tả Thiết Kế Kiến Trúc Hệ Thống Tổng Thể (System Architecture Specification)  
> **Mã tài liệu:** `SPEC-ARCH-V2.5.0` | **Phiên bản:** `v2.5.0-Enterprise-Production-Ready`  
> **Nguồn sự thật tối thượng (Source of Truth):** `Smart_FB_OS_Revised_4members.docx`, `Tong_Quan_Kien_Truc_He_Thong.md`, `Actor_Phan_Quyen_Chuc_Nang.md`, `Workflow_Quy_Trinh_Nghiep_Vu.md`  
> **Quy mô thực thi:** Đồ án Capstone 16 tuần (08 Sprints) — Đội ngũ 4 Kỹ sư Phần mềm (2 Backend + 2 Frontend)  
> **Tech Stack Chuẩn Hóa:**  
> • **Backend:** .NET 8 Web API (C# 12), Clean Architecture 4 Lớp, MediatR 12 (CQRS), FluentValidation 11, Entity Framework Core 8, ASP.NET Core SignalR.  
> • **Frontend:** Next.js 14.2 (App Router Monorepo), React 19, TypeScript 5, TanStack Query v5, Zustand 4, Tailwind CSS, Shadcn UI.  
> • **Data & Caching:** PostgreSQL 16 Enterprise (25 Thực thể 3NF), Redis 7.2 Alpine (L2 Cache, RedLock Distributed Locks, SignalR Backplane).  
> • **AI & Integration:** Google Gemini 1.5 Flash SDK (RAG Chatbot), Apriori / FP-Growth Engine (Combo Mining), PayOS VietQR Webhook, OpenWeatherMap API, AWS S3 / Cloudflare R2 Storage, SMTP / Telegram Alert.

> [!IMPORTANT]
> **NĂM NGUYÊN TẮC KIẾN TRÚC BẤT BIẾN (V2.5.0 INVARIANTS):**
> 1. **Web-First Monorepo (Zero Mobile App):** Hợp nhất 100% cổng vận hành (Customer PWA, Staff Web POS, Kitchen KDS TV, Manager Portal, Admin Portal) vào một dự án Next.js 14 duy nhất phân tách qua 5 Route Groups. **LOẠI BỎ TRIỆT ĐỂ** ứng dụng di động riêng cho nhân viên (Flutter/React Native) và thiết bị POS chuyên dụng đắt đỏ.
> 2. **Chấm Công Khóa Mạng WiFi (WiFi-Locked):** Xóa bỏ hoàn toàn định vị vệ tinh GPS 50m và mã QR động 30s. Chấm công an toàn qua cơ chế Dual-Check: Mạng WiFi chi nhánh (BSSID Access Point / IP Subnet) + Mã số nhân viên.
> 3. **Phân Định Rõ Ràng 3 Kênh Bán:**  
>    - *Dine-In (Tại bàn):* Hỗ trợ 2 nhánh thanh toán độc lập: Nhánh A (VietQR trả trước -> PayOS Webhook xác nhận -> KDS nhận đơn) và Nhánh B (Tiền mặt trả sau -> Đơn vào KDS ngay `Confirmed` -> In hóa đơn kèm VietQR -> Khách trả tiền mặt hoặc quét VietQR trên bill).  
>    - *Delivery (Giao tận nhà):* Quét QR Delivery -> Bắt buộc SĐT + Địa chỉ -> Phí ship cố định 20.000đ -> Bắt buộc 100% VietQR trả trước (Khóa COD).  
>    - *TakeAway (Mang về):* Thu ngân thao tác trên Web POS quầy -> Tra cứu CRM SĐT -> **Chương trình tích 10 ly tặng 1 ly CHỈ ÁP DỤNG DUY NHẤT CHO TAKEAWAY** -> Thu tiền sau bằng Tiền mặt / VietQR quầy.
> 4. **Loại Bỏ Hoàn Toàn Out-of-Scope Features:** Xóa bỏ triệt để tính năng chia sẻ món mạng xã hội (C-23), Push notification khuyến mãi PWA (C-24), ví voucher riêng lẻ và tra cứu calo tách biệt.
> 5. **Zero Placeholders & Chuẩn Hóa C4 Model:** 100% sơ đồ Mermaid (C4 Context, C4 Container, C4 Component), bảng dữ liệu, luồng tương tác và giao tiếp thời gian thực được mô tả chi tiết, hoàn chỉnh và kiểm chứng cú pháp nghiêm ngặt.

---

# 📚 MỤC LỤC KIẾN TRÚC

| STT | Phân Mục Kỹ Thuật | Trọng Tâm Kiến Trúc |
|:---:|---|---|
| **1** | [Tổng Quan Kiến Trúc & Phong Cách Thiết Kế Hệ Thống](#1-tổng-quan-kiến-trúc--phong-cách-thiết-kế-hệ-thống) | Clean Architecture, CQRS MediatR, Web-First, Event-Driven |
| **2** | [Mô Hình C4 Cấp 1: System Context Diagram](#2-mô-hình-c4-cấp-1-system-context-diagram) | Toàn cảnh Hệ thống, 6 Nhóm Tác Nhân & 5 Hệ Thống Tích Hợp Ngoài |
| **3** | [Mô Hình C4 Cấp 2: Container Diagram](#3-mô-hình-c4-cấp-2-container-diagram) | 5 Route Groups Frontend, NGINX WAF, .NET 8 Web API, PostgreSQL 16, Redis 7, AI |
| **4** | [Mô Hình C4 Cấp 3: Component Diagram (.NET 8 Clean Architecture)](#4-mô-hình-c4-cấp-3-component-diagram-net-8-clean-architecture) | Phân rã 4 Lớp: WebApi, Application (CQRS), Domain, Infrastructure |
| **5** | [Thiết Kế Tầng Client: Next.js 14 App Router (5 Route Groups)](#5-thiết-kế-tầng-client-nextjs-14-app-router-5-route-groups) | Đặc tả chi tiết `(customer)`, `(pos)`, `(kitchen)`, `(admin)`, `(auth)` |
| **6** | [Hạ Tầng Giao Tiếp Thời Gian Thực: 4 SignalR Hubs & Redis Backplane](#6-hạ-tầng-giao-tiếp-thời-gian-thực-4-signalr-hubs--redis-backplane) | Endpoints, Connection Groups, Events Emitted/Listened, Auto-Reconnect |
| **7** | [Chiến Lược Caching, Distributed Lock & Data Store (Redis 7 & PostgreSQL 16)](#7-chiến-lược-caching-distributed-lock--data-store-redis-7--postgresql-16) | L1/L2 Caching, RedLock chống Race Condition, 25 Bảng 3NF |
| **8** | [Kiến Trúc Module Trí Tuệ Nhân Tạo (AI Pipelines)](#8-kiến-trúc-module-trí-tuệ-nhân-tạo-ai-pipelines) | AI-1 Gemini 1.5 Flash RAG Chatbot & AI-2 Apriori Market Basket Analysis |
| **9** | [Kiến Trúc 3 Kênh Bán & Luồng Nghiệp Vụ Đặc Thù v2.5.0](#9-kiến-trúc-3-kênh-bán--luồng-nghiệp-vụ-đặc-thù-v250) | State Machines Dine-In 2 nhánh, Delivery 20k, Takeaway 10 ly, WiFi Lock |
| **10** | [Bảo Mật Đa Lớp, Ma Trận Phân Quyền RBAC & Audit Trails](#10-bảo-mật-đa-lớp-ma-trận-phân-quyền-rbac--audit-trails) | Defense-in-Depth, JWT Refresh Token, HMAC Webhook, Audit Log Bất Biến |
| **11** | [Tô-Pô Triển Khai, Hạ Tầng & Non-Functional Requirements (NFRs)](#11-tô-pô-triển-khai-hạ-tầng--non-functional-requirements-nfrs) | Docker Compose Topology, SLAs Hiệu Năng, Scale-Up Extension Points |

---

# 1. TỔNG QUAN KIẾN TRÚC & PHONG CÁCH THIẾT KẾ HỆ THỐNG

Hệ thống **Smart F&B OS** được xây dựng theo phong cách kiến trúc **Clean Architecture (Onion / Hexagonal Architecture)** kết hợp với mô hình xử lý phân tách trách nhiệm **CQRS (Command Query Responsibility Segregation)** và giao tiếp hướng sự kiện thời gian thực **Event-Driven Architecture qua WebSockets**:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              6 TRỤ CỘT THIẾT KẾ KIẾN TRÚC (ARCHITECTURAL PILLARS)                      │
├──────────────────────────┬─────────────────────────────────────────────────────────────────────────────┤
│ 1. Web-First Monorepo    │ Hợp nhất 100% ứng dụng vào một Next.js 14 Monorepo (5 Route Groups).        │
│    Zero Hardware Lock-in │ Chạy mượt trên Smartphone, Tablet, PC, Smart TV; không phụ thuộc máy POS cũ.│
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 2. Clean Architecture    │ Cô lập 100% nghiệp vụ lõi (Domain) khỏi Database, Frameworks và bên thứ 3.  │
│    & Domain Invariants   │ Phụ thuộc một chiều hướng tâm (Dependency Inversion Principle - DIP).       │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 3. CQRS & Pipeline Bus   │ Phân tách tuyệt đối luồng Ghi (Command + Transaction) và luồng Đọc (Query). │
│                          │ MediatR Pipeline tích hợp tự động Validation, Logging, Performance, Audit.  │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 4. Event-Driven Real-Time│ Đồng bộ trạng thái tức thời (< 500ms) qua 4 SignalR Hubs.                   │
│    Redis Backplane       │ Redis Pub/Sub Backplane sẵn sàng Scale-out đa instance không nghẽn kết nối. │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 5. Concurrency Control   │ Sử dụng Redis RedLock Distributed Locks ngăn chặn triệt để Race Conditions  │
│    & Data Integrity      │ (trùng phiên bàn, tranh chấp nguyên liệu BOM, thanh toán lặp, lệch ca két). │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 6. Hybrid AI Engine      │ Tích hợp kép: Gemini 1.5 Flash (RAG Tư vấn thực đơn theo thời tiết & CRM)   │
│                          │ và Thuật toán Apriori/FP-Growth (Khai phá Combo tối ưu hóa doanh thu AOV).  │
└──────────────────────────┴─────────────────────────────────────────────────────────────────────────────┘
```

---

# 2. MÔ HÌNH C4 CẤP 1: SYSTEM CONTEXT DIAGRAM

Sơ đồ ngữ cảnh C4 (Level 1) định vị hệ thống Smart F&B OS trong mối tương quan với **6 nhóm người dùng hệ thống** và **5 hệ sinh thái dịch vụ bên ngoài**:

```mermaid
flowchart TD
    subgraph ACTORS["👥 NGƯỜI DÙNG HỆ THỐNG (ACTORS)"]
        direction TB
        CUST_DINE["👤 Khách Hàng Ăn Tại Bàn (Dine-in Customer)<br>[Thiết bị: Trình duyệt Smartphone cá nhân]<br>Quét QR bàn, gọi món, chọn VietQR/Tiền mặt, Chat AI"]
        CUST_DELI["🛵 Khách Hàng Đặt Tận Nhà (Delivery Customer)<br>[Thiết bị: Trình duyệt Smartphone cá nhân]<br>Quét QR Delivery, nhập SĐT/Địa chỉ, trả trước VietQR (+20k)"]
        STAFF_POS["👨‍💼 Thu Ngân / Phục Vụ (Staff / Cashier)<br>[Thiết bị: PC / Laptop / Tablet Quầy]<br>Tạo đơn Takeaway, tra cứu CRM 10 ly, sơ đồ bàn, chấm công WiFi"]
        STAFF_BAR["👨‍🍳 Pha Chế / Bếp (Barista / Chef)<br>[Thiết bị: Smart TV / Tablet Bếp cảm ứng]<br>Xem đơn KDS thời gian thực, xem định mức BOM, 86-Toggle hết hàng"]
        MGR["👔 Quản Lý Chi Nhánh (Branch Manager)<br>[Thiết bị: Laptop / Desktop Quản lý]<br>Mở/kết ca két tiền, đối soát Z-Report, quản lý kho, cấu hình WiFi"]
        ADM["👑 Chủ Chuỗi / Quản Trị Viên (System Admin)<br>[Thiết bị: Desktop / Laptop điều hành]<br>Full CRUD Menu/BOM, giá vùng, duyệt AI Combo, xem P&L, phân quyền"]
    end

    subgraph SYSTEM["🏛️ SMART F&B OPERATING SYSTEM PLATFORM"]
        SFBOS["☕ Nền Tảng Quản Trị & Vận Hành Smart F&B OS<br>[Next.js 14 Monorepo + .NET 8 Clean Arch + PostgreSQL 16 + Redis 7 + SignalR]<br>Cung cấp dịch vụ đặt món thông minh, điều phối KDS, quản lý kho quỹ và phân tích AI"]
    end

    subgraph EXTERNAL["🌐 HỆ THỐNG DỊCH VỤ BÊN NGOÀI (EXTERNAL SERVICES)"]
        direction TB
        PAYOS["💳 Cổng Thanh Toán VietQR / PayOS<br>[OpenAPI / Webhook HMAC-SHA256]<br>Sinh mã QR thanh toán động & xác nhận giao dịch ngân hàng"]
        GEMINI["🤖 Google Gemini 1.5 Flash Cloud<br>[Google AI SDK REST API]<br>Mô hình ngôn ngữ lớn RAG tư vấn khẩu vị & phân tích đánh giá"]
        WEATHER["⛅ OpenWeatherMap API<br>[REST API JSON]<br>Cung cấp dữ liệu nhiệt độ, thời tiết thời gian thực tại chi nhánh"]
        STORAGE["📁 AWS S3 / Cloudflare R2 Storage<br>[S3-Compatible Object Storage]<br>Lưu trữ hình ảnh món ăn, ảnh đánh giá thực tế và hóa đơn điện tử"]
        NOTIFY["📨 Dịch Vụ Thông Báo (SMTP & Telegram Bot)<br>[SMTP Protocol / Telegram Bot API]<br>Gửi OTP xác thực, báo cáo Z-Report và phát cảnh báo đỏ khẩn cấp"]
    end

    %% Tương tác Actors -> System
    CUST_DINE -->|"1. Quét QR bàn, xem menu, đặt món, thanh toán VietQR/Tiền mặt, đánh giá"| SFBOS
    CUST_DELI -->|"2. Quét QR poster, nhập địa chỉ nhận hàng, thanh toán VietQR (Ship 20k)"| SFBOS
    STAFF_POS -->|"3. Bán POS Takeaway, tích 10 ly CRM, thu tiền sau, chấm công WiFi"| SFBOS
    STAFF_BAR -->|"4. Nhận vé đơn KDS real-time, đổi trạng thái chế biến, bật/tắt 86-out"| SFBOS
    MGR -->|"5. Khai báo ca két, kiểm kê hao hụt kho, cấu hình WiFi BSSID, xử lý review xấu"| SFBOS
    ADM -->|"6. Toàn quyền CRUD thực đơn/BOM, duyệt AI-2 Combo, xem P&L hợp nhất toàn chuỗi"| SFBOS

    %% Tương tác System -> External Services
    SFBOS -->|"Khởi tạo link thanh toán & nhận Webhook biến động số dư"| PAYOS
    PAYOS -->|"Webhook xác nhận thanh toán kèm chữ ký số HMAC"| SFBOS
    SFBOS -->|"Gửi Prompt ngữ cảnh RAG (Menu, Calo, Thời tiết, CRM)"| GEMINI
    GEMINI -->|"Phản hồi gợi ý món ăn có cấu trúc JSON"| SFBOS
    SFBOS -->|"Truy vấn thông tin thời tiết định kỳ theo tọa độ chi nhánh"| WEATHER
    SFBOS -->|"Lưu trữ & truy xuất media tài nguyên số qua Pre-signed URL"| STORAGE
    SFBOS -->|"Bắn tin nhắn cảnh báo lệch két >50k, review <=2 sao & email báo cáo"| NOTIFY

    %% Styling
    classDef actorStyle fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
    classDef systemStyle fill:#065f46,stroke:#10b981,stroke-width:3px,color:#ffffff;
    classDef extStyle fill:#374151,stroke:#6b7280,stroke-width:2px,color:#ffffff;

    class CUST_DINE,CUST_DELI,STAFF_POS,STAFF_BAR,MGR,ADM actorStyle;
    class SFBOS systemStyle;
    class PAYOS,GEMINI,WEATHER,STORAGE,NOTIFY extStyle;
```

---

# 3. MÔ HÌNH C4 CẤP 2: CONTAINER DIAGRAM

Sơ đồ C4 Container (Level 2) phân rã toàn bộ các thành phần phần mềm, công nghệ giao tiếp, cổng mạng và ranh giới bảo mật trong hệ thống:

```mermaid
flowchart TB
    subgraph CLIENT_TIER["🖥️ CLIENT LAYER (Next.js 14 App Router Monorepo - Port 3000)"]
        direction TB
        FE_AUTH["🔐 Auth Route Group: (auth)<br>[React 19 / Tailwind]<br>Đăng nhập tập trung JWT RBAC, OTP SĐT"]
        FE_CUST["📱 Customer Route Group: (customer)<br>[PWA Mobile-First / Zustand]<br>Dine-in Menu, Delivery Form 20k, VietQR, AI Chat, Review"]
        FE_POS["💻 Staff Route Group: (pos)<br>[Web Responsive / TanStack Query]<br>Takeaway POS, CRM 10 Ly, Sơ đồ bàn, Thu tiền, Chấm công WiFi"]
        FE_KDS["📺 Kitchen Route Group: (kitchen)<br>[Fullscreen TV / SignalR Hook]<br>Hàng đợi KDS Barista, Định mức BOM, Nút bấm 86-Toggle"]
        FE_ADM["🏢 Admin & Manager Route Group: (admin)<br>[Shadcn UI / Data Grid / Recharts]<br>Ca két Z-Report, Kho BOM, WiFi Config, CRUD Menu, AI Combo, P&L"]
    end

    subgraph EDGE_TIER["🛡️ API GATEWAY & REVERSE PROXY LAYER (Port 80/443)"]
        NGINX["🛡️ NGINX Reverse Proxy & WAF (Alpine Linux)<br>• SSL/TLS Termination (Let's Encrypt)<br>• Rate Limiting (60 req/min/IP cho Khách, 300 req/min cho POS)<br>• Gzip/Brotli Compression & Static CDN Proxy"]
    end

    subgraph BACKEND_TIER["⚙️ APPLICATION BACKEND CONTAINER (.NET 8 Web API - Port 5000)"]
        direction TB
        API_GATE["🌐 API Controllers & Middlewares<br>[JWT Auth, Exception Middleware, Request Audit Logger]"]
        CQRS_BUS["🔀 MediatR Pipeline & CQRS Engine<br>[ValidationBehavior, LoggingBehavior, TransactionScope]"]
        
        subgraph BUSINESS_MODULES["Core Business Handlers"]
            MOD_ORDER["📦 Order Engine (DineIn 2 nhánh, Delivery 20k, Takeaway)"]
            MOD_PAY["💳 Payment & PayOS Webhook HMAC Handler"]
            MOD_KDS["🍳 KDS & Inventory BOM Auto-Deduction Engine"]
            MOD_CRM["🎁 CRM & Loyalty 10-Cup Rule Engine (Takeaway Only)"]
            MOD_ATT["📶 WiFi-Locked Attendance Validator (BSSID/IP)"]
            MOD_SHIFT["💵 Cash Shift & Z-Report Reconciliation Handler"]
        end

        SIG_ENGINE["⚡ SignalR Real-Time Hubs Server<br>[/hubs/orders, /hubs/kitchen, /hubs/payments, /hubs/notifications]"]
    end

    subgraph AI_CONTAINER["🧠 AI MICRO-ENGINE & ANALYTICS CONTAINER"]
        AI_RAG["🤖 AI-1: RAG Chatbot Service (Gemini 1.5 Flash SDK)<br>Context Builder + Semantic Prompt + Fallback Top Best-Sellers"]
        AI_APRIORI["📊 AI-2: Market Basket Association Miner<br>Apriori / FP-Growth (Support >= 0.02, Lift > 1.2)"]
    end

    subgraph DATA_TIER["🗄️ PERSISTENCE & IN-MEMORY DATA LAYER (Docker Bridge Network)"]
        PG_DB[("🐘 PostgreSQL 16 Enterprise Database (Port 5432)<br>25 Tables 3NF, B-Tree & GIN Indexes, Foreign Keys, ACID Isolation")]
        REDIS_CACHE[("⚡ Redis 7.2 Alpine In-Memory Cache (Port 6379)<br>• L2 Distributed Cache (Menu, Categories, Stores)<br>• RedLock Distributed Locks (lock:tbl, lock:inv, lock:pay)<br>• SignalR Redis Backplane Pub/Sub (smartfb:signalr:*)")]
    end

    subgraph EXT_INTEGRATIONS["🌐 EXTERNAL INTEGRATION ENDPOINTS"]
        EXT_PAYOS["💳 PayOS VietQR API"]
        EXT_GEMINI["🤖 Google Gemini API Cloud"]
        EXT_OPENWEATHER["⛅ OpenWeatherMap API"]
        EXT_STORAGE["📁 S3 / Cloudflare R2"]
        EXT_PRINTER["🖨️ Máy In Nhiệt LAN/USB (ESC/POS)"]
    end

    %% Client to NGINX
    FE_AUTH & FE_CUST & FE_POS & FE_KDS & FE_ADM -->|"HTTPS (Port 443) / WSS"| NGINX

    %% NGINX to Backend
    NGINX -->|"HTTP REST Requests (/api/v1/*)"| API_GATE
    NGINX -->|"WebSocket Upgrades (/hubs/*)"| SIG_ENGINE

    %% Inside Backend
    API_GATE --> CQRS_BUS
    CQRS_BUS --> BUSINESS_MODULES
    BUSINESS_MODULES -->|"State Events & Broadcasts"| SIG_ENGINE
    BUSINESS_MODULES <-->|"In-process / Internal Call"| AI_CONTAINER

    %% Backend to Data Layer
    BUSINESS_MODULES -->|"EF Core 8 Npgsql (ACID Transactions)"| PG_DB
    BUSINESS_MODULES <-->|"Cache-Aside & RedLock Acquirements"| REDIS_CACHE
    SIG_ENGINE <-->|"Pub/Sub Message Bus Backplane"| REDIS_CACHE

    %% Backend to External
    MOD_PAY <-->|"REST API & HMAC Webhook"| EXT_PAYOS
    AI_RAG -->|"Prompt Context / GenerateContent"| EXT_GEMINI
    AI_RAG -->|"Query Current Weather"| EXT_OPENWEATHER
    API_GATE -->|"Pre-signed Upload / Media Fetch"| EXT_STORAGE
    MOD_ORDER & MOD_KDS -->|"RAW Byte TCP/IP Socket (Port 9100)"| EXT_PRINTER

    %% Styling
    classDef clientStyle fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
    classDef edgeStyle fill:#b91c1c,stroke:#ef4444,stroke-width:2px,color:#ffffff;
    classDef beStyle fill:#14532d,stroke:#22c55e,stroke-width:2px,color:#ffffff;
    classDef aiStyle fill:#581c87,stroke:#a855f7,stroke-width:2px,color:#ffffff;
    classDef dataStyle fill:#701a75,stroke:#ec4899,stroke-width:2px,color:#ffffff;
    classDef extStyle fill:#374151,stroke:#9ca3af,stroke-width:2px,color:#ffffff;

    class FE_AUTH,FE_CUST,FE_POS,FE_KDS,FE_ADM clientStyle;
    class NGINX edgeStyle;
    class API_GATE,CQRS_BUS,BUSINESS_MODULES,SIG_ENGINE beStyle;
    class AI_RAG,AI_APRIORI aiStyle;
    class PG_DB,REDIS_CACHE dataStyle;
    class EXT_PAYOS,EXT_GEMINI,EXT_OPENWEATHER,EXT_STORAGE,EXT_PRINTER extStyle;
```

---

# 4. MÔ HÌNH C4 CẤP 3: COMPONENT DIAGRAM (.NET 8 CLEAN ARCHITECTURE)

Tầng Backend được tổ chức nghiêm ngặt theo **Clean Architecture (4 Lớp)**. Quy tắc bất biến: Các lớp bên ngoài phụ thuộc vào các lớp bên trong, tầng Domain nằm ở lõi trung tâm và tuyệt đối không phụ thuộc vào bất kỳ framework bên ngoài nào:

```mermaid
flowchart TD
    subgraph L1["1. PRESENTATION / WEBAPI LAYER (SmartFB.API)"]
        direction TB
        CTRL["REST API Controllers<br>• AuthController, OrdersController, PaymentsController<br>• ProductsController, CategoriesController, TablesController<br>• AttendanceController, ShiftsController, InventoryController<br>• ReviewsController, AnalyticsController, AiController"]
        HUBS["SignalR Real-Time Hubs<br>• OrderHub (/hubs/orders)<br>• KitchenHub (/hubs/kitchen)<br>• PaymentHub (/hubs/payments)<br>• NotificationHub (/hubs/notifications)"]
        MW["Middlewares & Action Filters<br>• JwtAuthenticationMiddleware & ClaimsPrincipalTransformer<br>• GlobalExceptionHandlingMiddleware (RFC 7807 ProblemDetails)<br>• RateLimitingFilter (Fixed Window / Sliding Window)<br>• SerilogRequestLoggingMiddleware & AuditActionFilter"]
    end

    subgraph L2["2. APPLICATION LAYER (SmartFB.Application - CQRS MediatR)"]
        direction TB
        CMD["Commands & Handlers (Write Side - ACID)<br>• CreateDineInOrderCommand / CreateDeliveryOrderCommand / CreateTakeawayOrderCommand<br>• ProcessPayOSWebhookCommand / ConfirmCashPaymentCommand<br>• UpdateKdsItemStatusCommand / ToggleProduct86StatusCommand<br>• VerifyWifiAttendanceCommand / OpenCashShiftCommand / CloseCashShiftCommand<br>• ApproveAiComboCommand / CreateProductWithBOMCommand"]
        QRY["Queries & Handlers (Read Side - Optimized Cache)<br>• GetBranchMenuQuery / GetCustomerLoyaltyQuery / GetActiveKdsQueueQuery<br>• GetCashShiftReconciliationQuery / GetPnLConsolidatedReportQuery / GetAiRecommendationsQuery"]
        PIPE["MediatR Pipeline Behaviors<br>• ValidationBehavior (Tự động kích hoạt FluentValidation trước Handler)<br>• LoggingBehavior (Ghi log tham số đầu vào và kết quả có cấu trúc)<br>• PerformanceBehavior (Cảnh báo khi thời gian thực thi > 500ms)<br>• TransactionBehavior (Quản lý DbTransaction Unit of Work tự động)"]
        VAL["FluentValidation Validators<br>• CreateOrderValidator, CheckInWifiValidator, CashShiftValidator..."]
        DTOS["DTOs, ViewModels & AutoMapper Profiles"]
        PORTS["Application Interfaces (Ports)<br>• IAppDbContext, IRedisCacheService, IRedLockManager<br>• IPayOSGateway, IGeminiAiClient, IWeatherClient, IEmailService, ITelegramBotService"]
    end

    subgraph L3["3. DOMAIN LAYER (SmartFB.Domain - Core Enterprise Rules)"]
        direction TB
        ENT["Domain Entities (25 Real Entities)<br>• Branch, BranchWifiConfig, Table, User, Role, UserRole, AuditLog<br>• Category, Product, ProductSize, ProductBranchPrice, Modifier, ProductModifier<br>• Ingredient, RecipeBOM, Order, OrderItem, OrderItemModifier, Payment<br>• Customer, LoyaltyCupTransaction, Voucher, CustomerReview, Shift, Attendance"]
        VO["Value Objects<br>• Money, Address, PhoneNumber, WifiSubnet, GeoLocation"]
        ENUMS["Domain Enums<br>• OrderType (DineIn, TakeAway, Delivery)<br>• OrderStatus (PendingPayment, Paid, Confirmed, Preparing, Ready, Served, Cancelled)<br>• PaymentMethod (VietQR, Cash)<br>• ShiftStatus (Open, Closed, Reconciled)"]
        EVENTS["Domain Events<br>• OrderPaidDomainEvent, OrderConfirmedDomainEvent<br>• OrderReadyDomainEvent, LowRatingAlertDomainEvent, StockShortageDomainEvent"]
        EXCEPTIONS["Domain Exceptions (Business Rule Invariants)"]
    end

    subgraph L4["4. INFRASTRUCTURE LAYER (SmartFB.Infrastructure - Adapters)"]
        direction TB
        EF["Entity Framework Core 8 DbContext<br>• AppDbContext (25 DbSets, Fluent API Mapping, Shadow Properties)<br>• SoftDeleteGlobalFilter, AuditableEntityInterceptor, MigrationManager"]
        REPOS["Repositories & Unit of Work Implementation<br>• OrderRepository, ProductRepository, ShiftRepository, AttendanceRepository"]
        REDIS_IMPL["Redis 7 Services<br>• RedisCacheService (Cache-Aside Engine)<br>• RedLockDistributedLockManager (RedLock.net Implementation)<br>• SignalR Redis Backplane Bus"]
        EXT_ADAPTERS["External Gateway Adapters<br>• PayOSPaymentGateway (PayOS .NET SDK + HMAC-SHA256 Validator)<br>• GoogleGeminiClient (Semantic Prompt Builder + RestClient)<br>• OpenWeatherClient (HttpClientFactory)<br>• SmtpEmailService & TelegramBotService (Cảnh báo đỏ khẩn cấp)"]
    end

    %% Dependencies
    L1 --> L2
    L2 --> L3
    L4 --> L3
    L4 --> L2
    L1 --> L4

    CTRL --> MW
    MW --> PIPE
    PIPE --> VAL
    PIPE --> CMD & QRY
    CMD & QRY --> PORTS
    PORTS -.-> L4
    CMD & QRY --> ENT & VO & ENUMS
    CMD --> EVENTS

    REPOS --> EF
    REDIS_IMPL -.-> PORTS
    EXT_ADAPTERS -.-> PORTS
    EF --> ENT

    %% Styling
    classDef preStyle fill:#1e293b,stroke:#475569,stroke-width:2px,color:#ffffff;
    classDef appStyle fill:#1e40af,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
    classDef domStyle fill:#991b1b,stroke:#ef4444,stroke-width:2px,color:#ffffff;
    classDef infStyle fill:#14532d,stroke:#22c55e,stroke-width:2px,color:#ffffff;

    class CTRL,HUBS,MW preStyle;
    class CMD,QRY,PIPE,VAL,DTOS,PORTS appStyle;
    class ENT,VO,ENUMS,EVENTS,EXCEPTIONS domStyle;
    class EF,REPOS,REDIS_IMPL,EXT_ADAPTERS infStyle;
```

---

# 5. THIẾT KẾ TẦNG CLIENT: NEXT.JS 14 APP ROUTER (5 ROUTE GROUPS)

Tầng giao diện người dùng được tổ chức theo kiến trúc **Next.js 14 App Router Monorepo** với 5 Route Groups phân định ranh giới chức năng và trải nghiệm người dùng:

```
frontend/
├── src/
│   ├── app/
│   │   ├── (auth)/                           # [CỔNG ĐĂNG NHẬP TẬP TRUNG]
│   │   │   ├── login/                        # Đăng nhập Nhân viên, Quản lý, Admin (JWT + Role Dispatch)
│   │   │   └── forgot-password/              # Khôi phục mật khẩu qua Email OTP
│   │   │
│   │   ├── (customer)/                       # [ACTOR 1: KHÁCH HÀNG - PWA Mobile-First]
│   │   │   ├── menu/                         # Duyệt thực đơn QR Bàn, chọn Size/Đường/Đá/Topping
│   │   │   ├── cart/                         # Giỏ hàng: Áp voucher, chọn VietQR trả trước / Tiền mặt trả sau
│   │   │   ├── delivery/                     # Form đặt hàng giao tận nơi (SĐT + Địa chỉ + Phí ship cố định 20k)
│   │   │   ├── tracking/[orderId]/           # Theo dõi tiến độ đơn hàng thời gian thực qua SignalR
│   │   │   ├── ai-consultant/                # Chatbot RAG Gemini 1.5 Flash tư vấn khẩu vị & năng lượng món
│   │   │   └── review/[orderId]/             # Đánh giá 1-5 sao, viết nhận xét & tải ảnh chụp thực tế
│   │   │
│   │   ├── (pos)/                            # [ACTOR 2: NHÂN VIÊN QUẦY - Web Responsive POS]
│   │   │   ├── pos/                          # Web POS Quầy: Bán mang về (Takeaway), tra cứu CRM SĐT tích 10 ly
│   │   │   ├── tables/                       # Sơ đồ mặt bằng bàn trực quan, tiếp nhận chuông gọi phục vụ bàn
│   │   │   ├── cash-payment/                 # Xác nhận thu tiền mặt đơn Dine-in Nhánh B & Takeaway
│   │   │   └── attendance/                   # Chấm công khóa mạng WiFi (Xác thực IP/BSSID + Mã NV)
│   │   │
│   │   ├── (kitchen)/                        # [ACTOR 2: BARISTA / ĐẦU BẾP - Web KDS TV Fullscreen]
│   │   │   ├── queue/                        # Hàng đợi đơn hàng thời gian thực (Gom nhóm món, xem công thức BOM)
│   │   │   └── 86-toggle/                    # Nút gạt bật/tắt trạng thái hết hàng tức thì của món tại quầy bar
│   │   │
│   │   └── (admin)/                          # [ACTOR 3 & 4: QUẢN LÝ CHI NHÁNH & CHỦ CHUỖI]
│   │       ├── shifts/                       # Mở ca đầu ngày, kết ca kiểm đếm két tiền mặt & ký Z-Report
│   │       ├── inventory/                    # Lập phiếu xuất quầy bar, nhập kho NCC, kiểm kê hao hụt BOM
│   │       ├── wifi-config/                  # Khai báo danh sách BSSID Access Point & IP Subnet chấm công
│   │       ├── reviews/                      # Tiếp nhận Alert review <= 2 sao khẩn cấp & duyệt ảnh review
│   │       ├── menu-management/              # Full CRUD Món ăn, Danh mục, Định lượng BOM từng Size
│   │       ├── dynamic-pricing/              # Thiết lập bảng giá theo nhóm chi nhánh (Sân bay, Phố, Tỉnh)
│   │       ├── ai-combo-mining/              # Phê duyệt các gợi ý Combo khai phá bởi thuật toán Apriori
│   │       ├── reports-pnl/                  # Dashboard P&L hợp nhất toàn chuỗi (Doanh thu, COGS, Lãi gộp)
│   │       └── branches-rbac/                # Quản lý danh mục chi nhánh, tài khoản & phân quyền RBAC
│   │
│   ├── components/                           # Shadcn UI, Data Grid, Recharts, POS Keypad, Dialogs
│   ├── hooks/                                # useSignalR, useCart, usePosCart, useWifiAttendance, useKdsQueue
│   ├── stores/                               # Zustand: cartStore, posStore, shiftStore, authStore
│   └── lib/                                  # Axios API Client, SignalR Factory, Crypto Utils, Formatters
```

### Bảng Chi Tiết Công Nghệ & Vai Trò 5 Route Groups:

| Route Group | Actor Mục Tiêu | Thiết Bị Tối Ưu | Tech Stack Thành Phần | Trách Nhiệm Kỹ Thuật Chính |
|---|---|---|---|---|
| **`(customer)`** | Khách Hàng Ăn Tại Bàn & Đặt Về | Smartphone (iOS/Android Safari/Chrome) | React 19, Zustand (`cartStore`), Tailwind CSS, `@microsoft/signalr` | Trải nghiệm PWA không cần cài đặt; Quét QR Bàn / QR Delivery; Thanh toán VietQR; Chat RAG AI; Nhận push cập nhật trạng thái đơn hàng. |
| **`(pos)`** | Thu Ngân & Phục Vụ Quầy | Tablet / PC Cảm ứng Quầy Thu ngân | TanStack Query v5, Zustand (`posStore`), Shadcn UI, Lucide Icons | Nhập đơn Takeaway siêu tốc; Tra cứu CRM SĐT và áp dụng cơ chế 10 ly tặng 1; Theo dõi sơ đồ bàn; Chấm công WiFi. |
| **`(kitchen)`** | Barista & Đầu Bếp | Smart TV / Tablet Bếp Màn hình lớn | SignalR Real-time, Web Audio API, Fullscreen API, CSS Grid | Hiển thị vé đơn hàng KDS tự động cuộn; Báo âm thanh chuông khi có đơn mới; Hiển thị định lượng BOM; Bật/tắt 86-out. |
| **`(admin)`** | Quản Lý Chi Nhánh & Chủ Chuỗi | Desktop / Laptop / Máy tính bảng | Shadcn UI Data Table, TanStack Table, Recharts, React Hook Form, Zod | Mở/kết ca két tiền Z-Report; Quản lý kho nguyên liệu BOM; Cấu hình WiFi chấm công; Full CRUD Menu/BOM; Phê duyệt AI Combo; Báo cáo P&L. |
| **`(auth)`** | Toàn Bộ Nhân Sự & Quản Trị | Mọi Thiết Bị Trình Duyệt | Next.js Server Actions, JWT Decoder, Cookies Manager | Xác thực thông tin đăng nhập; Kiểm tra phân quyền RBAC; Tự động điều hướng đúng Route Group theo vai trò sau khi đăng nhập. |

---

# 6. HẠ TẦNG GIAO TIẾP THỜI GIAN THỰC: 4 SIGNALR HUBS & REDIS BACKPLANE

Hệ thống thiết lập **4 SignalR Hubs chuyên biệt** chạy trên nền tảng **Redis 7 Pub/Sub Backplane**, đảm bảo độ trễ truyền thông `< 500ms` và hỗ trợ mở rộng không giới hạn số lượng instances Web API:

```mermaid
flowchart TD
    subgraph HUBS["⚡ 4 ASP.NET CORE SIGNALR HUBS"]
        H1["1. OrderHub<br>Endpoint: /hubs/orders<br>Mục đích: Cập nhật tiến trình đơn cho Khách & POS"]
        H2["2. KitchenHub<br>Endpoint: /hubs/kitchen<br>Mục đích: Đẩy vé đơn vào Bếp KDS & đồng bộ 86-Toggle"]
        H3["3. PaymentHub<br>Endpoint: /hubs/payments<br>Mục đích: Bắn tín hiệu thanh toán VietQR từ PayOS Webhook"]
        H4["4. NotificationHub<br>Endpoint: /hubs/notifications<br>Mục đích: Chuông gọi bàn, Alert Review đỏ <= 2 sao, Lệch két tiền"]
    end

    subgraph REDIS_BACKPLANE["⚡ REDIS 7 PUB/SUB MESSAGE BUS BACKPLANE"]
        R_PUB["Kênh Pub/Sub phân tán: smartfb:signalr:*<br>Đồng bộ tức thì mọi sự kiện giữa các cụm Server Web API"]
    end

    subgraph CLIENT_GROUPS["📱 CLIENT CONNECTION GROUPS"]
        G_CUST["Customer PWA<br>Groups: Order_{orderId}, Customer_{phone}"]
        G_KDS["Kitchen KDS TV<br>Group: Branch_{branchId}_Kitchen"]
        G_STAFF["Staff Web POS<br>Group: Branch_{branchId}_Staff"]
        G_MGR["Manager Portal<br>Group: Branch_{branchId}_Manager"]
        G_ADM["Admin Portal<br>Group: Chain_Admin"]
    end

    H1 & H2 & H3 & H4 <--> R_PUB

    H1 -->|OrderStatusUpdated, OrderReady, EstimatedTimeAdjusted| G_CUST & G_STAFF
    H2 -->|NewPaidOrder, OrderConfirmedCash, Item86Toggled| G_KDS
    H3 -->|PaymentSucceeded, PaymentFailed, PaymentExpired| G_CUST & G_STAFF
    H4 -->|ServiceRequested, LowRatingAlert, CashVarianceAlert, InventoryShortageAlert| G_STAFF & G_MGR & G_ADM
```

### Bảng Đặc Tả Chi Tiết 4 SignalR Hubs:

| Tên Hub & URL | Connection Groups | Events Bắn Từ Server (Server-to-Client) | Events Lắng Nghe Từ Client (Client-to-Server) | Payload Dữ Liệu Chi Tiết |
|---|---|---|---|---|
| **`OrderHub`**<br>`/hubs/orders` | `Order_{orderId}`<br>`Customer_{phone}` | • `OrderStatusUpdated`<br>• `OrderReady`<br>• `EstimatedTimeAdjusted` | • `JoinOrderGroup(orderId)`<br>• `LeaveOrderGroup(orderId)` | `{ orderId, orderCode, status, estimatedMinutes, queuePosition, updatedAtUtc }` |
| **`KitchenHub`**<br>`/hubs/kitchen` | `Branch_{branchId}_Kitchen`<br>`Station_{stationId}` | • `NewPaidOrder`<br>• `OrderConfirmedCash`<br>• `Item86Toggled`<br>• `ItemBatchUpdated` | • `JoinKitchenGroup(branchId)`<br>• `UpdateItemStatus(orderItemId, status)`<br>• `Toggle86Product(productId, isAvailable)` | `{ ticketId, orderCode, orderType, tableNumber, items: [{ name, size, notes, bom }], createdAt }` |
| **`PaymentHub`**<br>`/hubs/payments` | `Payment_{orderId}` | • `PaymentSucceeded`<br>• `PaymentFailed`<br>• `PaymentExpired` | • `JoinPaymentGroup(orderId)`<br>• `LeavePaymentGroup(orderId)` | `{ orderId, orderCode, amount, transactionCode, paymentMethod, paidAtUtc }` |
| **`NotificationHub`**<br>`/hubs/notifications` | `Branch_{branchId}_Staff`<br>`Branch_{branchId}_Manager`<br>`Chain_Admin` | • `ServiceRequested`<br>• `ServiceCallResolved`<br>• `LowRatingAlert`<br>• `CashVarianceAlert`<br>• `InventoryShortageAlert` | • `JoinBranchNotifications(branchId)`<br>• `CallWaiter(tableId, message)`<br>• `ResolveServiceCall(callId)` | `{ branchId, tableNumber, reason, ratingStars, comment, varianceAmount, ingredientName, timestamp }` |

---

# 7. CHIẾN LƯỢC CACHING, DISTRIBUTED LOCK & DATA STORE (REDIS 7 & POSTGRESQL 16)

```mermaid
flowchart TD
    subgraph READ_FLOW["LUỒNG ĐỌC DỮ LIỆU TỐI ƯU (CACHE-ASIDE & 2-TIER CACHING)"]
        REQ_R["Client Read Request (VD: GetBranchMenu)"] --> L1_CHECK{"Kiểm tra L1 In-Memory Cache (.NET MemoryCache)"}
        L1_CHECK -->|Hit| RESP_L1["Trả về DTO ngay (< 5ms)"]
        L1_CHECK -->|Miss| L2_CHECK{"Kiểm tra L2 Distributed Cache (Redis 7)"}
        L2_CHECK -->|Hit| POP_L1["Ghi bù vào L1 Cache"] --> RESP_L2["Trả về DTO (< 20ms)"]
        L2_CHECK -->|Miss| DB_QUERY["Truy vấn PostgreSQL 16 (EF Core Compiled Query)"]
        DB_QUERY --> POP_L2["Ghi vào Redis 7 (TTL 24h)"] --> POP_L1 --> RESP_DB["Trả về Client DTO"]
    end

    subgraph WRITE_FLOW["LUỒNG GHI DỮ LIỆU AN TOÀN (DISTRIBUTED REDLOCK & ACID)"]
        REQ_W["Client Write Request (VD: Đặt đơn / Trừ kho / Đổi giá)"] --> ACQ_LOCK{"Lấy Khóa Phân Tán RedLock (Redis 7)"}
        ACQ_LOCK -->|Không lấy được| ERR_LOCK["Báo lỗi 409 Conflict: Thao tác đang được xử lý"]
        ACQ_LOCK -->|Lấy khóa thành công| TX_BEGIN["Mở Giao Dịch ACID (PostgreSQL 16 Transaction)"]
        TX_BEGIN --> EXEC_BIZ["Thực thi Business Logic & Cập nhật DbContext"]
        EXEC_BIZ --> COMMIT_DB["Commit Giao Dịch Database Thành Công"]
        COMMIT_DB --> INVAL_CACHE["Xóa Cache Liên Quan (Redis Invalidation)"]
        INVAL_CACHE --> PUB_EVENT["Publish Domain Events & Bắn SignalR Hubs"]
        PUB_EVENT --> REL_LOCK["Giải phóng Khóa RedLock"]
    end

    classDef reqStyle fill:#1e40af,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
    classDef checkStyle fill:#b45309,stroke:#f59e0b,stroke-width:2px,color:#ffffff;
    classDef successStyle fill:#15803d,stroke:#22c55e,stroke-width:2px,color:#ffffff;
    classDef errStyle fill:#b91c1c,stroke:#ef4444,stroke-width:2px,color:#ffffff;

    class REQ_R,REQ_W reqStyle;
    class L1_CHECK,L2_CHECK,ACQ_LOCK checkStyle;
    class RESP_L1,RESP_L2,RESP_DB,TX_BEGIN,EXEC_BIZ,COMMIT_DB,INVAL_CACHE,PUB_EVENT,REL_LOCK successStyle;
    class ERR_LOCK errStyle;
```

### 7.1. Bảng Cấu Trúc Khóa Caching & Chiến Lược Invalidation Redis 7

| Loại Dữ Liệu Caching | Key Pattern Trong Redis | TTL Mặc Định | Chiến Lược Cập Nhật / Invalidation (Cache Invalidation Policy) |
|---|---|---|---|
| **Thực Đơn Chi Nhánh** | `menu:branch:{branchId}` | 24 Giờ | Invalidate ngay khi Admin đổi giá, sửa món, hoặc Barista bấm nút **86-Toggle** hết hàng. |
| **Danh Mục Thực Đơn** | `categories:active` | 24 Giờ | Invalidate khi Admin thêm, sửa, đổi thứ tự hiển thị (`display_order`) danh mục. |
| **Bảng Giá Theo Vùng** | `pricing:group:{priceGroupId}` | 24 Giờ | Invalidate khi Admin điều chỉnh hệ số giá vùng chi nhánh. |
| **Hồ Sơ Loyalty CRM** | `crm:customer:{phoneNumber}` | 1 Giờ | Invalidate ngay khi có giao dịch Takeaway tích lũy ly mới hoặc đổi ly thành công. |
| **Cấu Hình WiFi Chi Nhánh** | `wifi:branch:{branchId}` | 12 Giờ | Invalidate khi Quản lý chi nhánh cập nhật BSSID Router hoặc IP Subnet chấm công. |

### 7.2. Bảng Phân Bổ Distributed RedLock Chống Race Conditions

| Tên Khóa Phân Tán | Cấu Trúc Khóa (Key Pattern) | Thời Gian Khóa (Expiry) | Mục Đích Ngăn Chặn Race Condition |
|---|---|---|---|
| **Table Session Lock** | `lock:table:{tableId}` | 15 Giây | Chặn xung đột khi 2 khách hàng cùng quét QR tại cùng một bàn và tạo đơn đồng thời. |
| **Inventory BOM Lock** | `lock:inventory:{ingredientId}` | 10 Giây | Ngăn chặn trừ âm kho nguyên liệu khi nhiều đơn hàng có cùng công thức được xác nhận cùng lúc. |
| **Payment Process Lock** | `lock:payment:order:{orderId}` | 30 Giây | Chặn xử lý trùng lặp giao dịch khi PayOS Webhook bắn lại hoặc nhân viên xác nhận tiền mặt trùng. |
| **Shift Management Lock** | `lock:shift:cashier:{cashierId}` | 15 Giây | Chặn nhân viên mở hoặc kết ca két đồng thời trên nhiều thiết bị trình duyệt khác nhau. |

---

# 8. KIẾN TRÚC MODULE TRÍ TUỆ NHÂN TẠO (AI PIPELINES)

```mermaid
flowchart TD
    subgraph DATA_SOURCES["DỮ LIỆU ĐẦU VÀO CHO AI (DATA PERSISTENCE)"]
        D_MENU["Danh Mục Thực Đơn & Công Thức BOM (PostgreSQL 16)"]
        D_CRM["Lịch Sử Tiêu Dùng & Khẩu Vị Khách Hàng (PostgreSQL 16)"]
        D_ORDERS["Lịch Sử 10,000+ Giao Dịch Đơn Hàng Đã Bán (PostgreSQL 16)"]
        D_WEATHER["Dữ Liệu Thời Tiết & Nhiệt Độ Chi Nhánh (OpenWeatherMap API)"]
    end

    subgraph ACTIVE_AI["🤖 2 MODULES AI TRIỂN KHAI CHÍNH THỨC TRONG 16 TUẦN (ACTIVE MVP)"]
        direction TB
        
        subgraph AI1_PIPELINE["AI-1: RAG Recommendation Chatbot Pipeline (Google Gemini 1.5 Flash)"]
            P1_INPUT["Tin nhắn yêu cầu của Khách hàng (VD: 'Trời nóng muốn uống món thanh mát ít ngọt')"]
            P1_BUILDER["Context Builder: Lọc món còn bán (Active & !86-out) + Tag Calo + Dữ liệu thời tiết"]
            P1_PROMPT["System Prompt Structurer & Temperature 0.3 (Định dạng JSON Schema)"]
            P1_GEMINI["Google Gemini 1.5 Flash Cloud LLM"]
            P1_FALLBACK["Fallback Engine: Tự động trả về Top 3 Best-Seller nếu Timeout > 1.5s hoặc lỗi mạng"]
            P1_OUTPUT["Giao diện PWA: Thẻ món ăn trực quan kèm nút 'Thêm Ngay Vào Giỏ'"]

            P1_INPUT --> P1_BUILDER
            P1_BUILDER --> P1_PROMPT
            P1_PROMPT --> P1_GEMINI
            P1_GEMINI -->|Thành công| P1_OUTPUT
            P1_GEMINI -.->|Timeout / Error| P1_FALLBACK
            P1_FALLBACK --> P1_OUTPUT
        end

        subgraph AI2_PIPELINE["AI-2: Market Basket Analysis & Combo Mining (Apriori Engine)"]
            P2_EXTRACT["Trích xuất tập giao dịch (Transaction Dataset) từ bảng OrderItems"]
            P2_MINE["Thuật toán Apriori / FP-Growth: Min Support >= 0.02, Min Confidence >= 0.3, Lift > 1.2"]
            P2_FILTER["Bộ lọc quy tắc kết hợp (Association Rules): Món chính + Đồ ăn kèm / Topping"]
            P2_ADMIN_UI["Giao diện Admin Portal: Chủ Chuỗi xem xét, chỉnh mức chiết khấu và phê duyệt"]
            P2_PUBLISH["Phát hành Combo lên Menu PWA Khách hàng ➔ Tăng giá trị trung bình đơn hàng (AOV)"]

            P2_EXTRACT --> P2_MINE
            P2_MINE --> P2_FILTER
            P2_FILTER --> P2_ADMIN_UI
            P2_ADMIN_UI -->|Admin Phê Duyệt| P2_PUBLISH
        end
    end

    subgraph SCALEUP_AI["🔮 3 MODULES AI MỞ RỘNG TƯƠNG LAI (SCALE-UP EXTENSIONS)"]
        direction LR
        AI3_EXT["AI-3: Text-to-SQL Analytics<br>[Hỏi đáp số liệu kinh doanh tự nhiên]"]
        AI4_EXT["AI-4: Churn Prediction<br>[Mô hình XGBoost RFM dự báo khách rời bỏ]"]
        AI5_EXT["AI-5: Demand Forecasting<br>[Dự báo nhu cầu nguyên liệu theo ngày]"]
    end

    D_MENU & D_CRM & D_WEATHER --> P1_BUILDER
    D_ORDERS --> P2_EXTRACT
    D_ORDERS -.-> AI3_EXT & AI4_EXT & AI5_EXT

    classDef srcStyle fill:#1e293b,stroke:#475569,stroke-width:2px,color:#ffffff;
    classDef aiStyle fill:#581c87,stroke:#a855f7,stroke-width:2px,color:#ffffff;
    classDef futStyle fill:#374151,stroke:#6b7280,stroke-dasharray: 5 5,stroke-width:2px,color:#ffffff;

    class D_MENU,D_CRM,D_ORDERS,D_WEATHER srcStyle;
    class P1_INPUT,P1_BUILDER,P1_PROMPT,P1_GEMINI,P1_FALLBACK,P1_OUTPUT,P2_EXTRACT,P2_MINE,P2_FILTER,P2_ADMIN_UI,P2_PUBLISH aiStyle;
    class AI3_EXT,AI4_EXT,AI5_EXT futStyle;
```

---

# 9. KIẾN TRÚC 3 KÊNH BÁN & LUỒNG NGHIỆP VỤ ĐẶC THÙ V2.5.0

### 9.1. State Machine Dine-In 2 Nhánh Độc Lập

```mermaid
flowchart TD
    START([Khách Quét QR Bàn & Đưa Món Vào Giỏ]) --> CHOOSE_PAY{Khách Chọn Phương Thức Thanh Toán}

    %% NHANH A: VIETQR TRẢ TRƯỚC
    CHOOSE_PAY -->|Nhánh A: VietQR Trả Trước| A1[Khởi tạo đơn: Status = PendingPayment]
    A1 --> A2[Hiển thị Mã VietQR Động từ PayOS]
    A2 --> A3[Khách quét mã chuyển khoản ngân hàng]
    A3 --> A4[PayOS gửi Webhook xác nhận chữ ký HMAC]
    A4 --> A5[Cập nhật trạng thái: Status = Paid]
    A5 --> A6[SignalR KitchenHub bắn vé đơn vào Bếp]
    A6 --> A7[BẾP KDS MỚI NHẬN ĐƠN ĐỂ PHA CHẾ]
    A7 --> A8[Barista bấm: Status = Preparing]
    A8 --> A9[Barista bấm: Status = Ready]
    A9 --> A10[Phục vụ bưng món ra bàn: Status = Served / Completed]

    %% NHANH B: TIỀN MẶT TRẢ SAU
    CHOOSE_PAY -->|Nhánh B: Tiền Mặt Trả Sau| B1[Tạo đơn: Status = Confirmed]
    B1 --> B2[SignalR KitchenHub bắn vé đơn vào Bếp NGAY LẬP TỨC]
    B2 --> B3[ĐƠN VÀO BẾP PHA CHẾ NGAY KHÔNG CẦN CHỜ TIỀN]
    B3 --> B4[Barista bấm: Status = Preparing]
    B4 --> B5[Barista bấm: Status = Ready]
    B5 --> B6[Máy in quầy tự động in Hóa đơn CÓ IN MÃ VIETQR]
    B6 --> B7[Nhân viên bưng món ra bàn KÈM HÓA ĐƠN ĐÃ IN]
    B7 --> B8[Cập nhật trạng thái: Status = Served -> Chờ Thu Tiền]
    B8 --> B9{Khách Chọn Cách Trả Tiền Tại Bàn}
    B9 -->|Đưa Tiền Mặt Cho NV| B10[NV thu tiền & bấm Xác Nhận Tiền Mặt trên Web POS]
    B9 -->|Quét Mã QR Trên Bill| B11[Khách quét VietQR trên Bill & PayOS báo Webhook Paid]
    B10 & B11 --> B12[Đơn hàng hoàn tất: Status = Paid / Completed]

    classDef initStyle fill:#7c2d12,stroke:#ea580c,stroke-width:2px,color:#ffffff;
    classDef aStyle fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
    classDef bStyle fill:#14532d,stroke:#22c55e,stroke-width:2px,color:#ffffff;

    class START,CHOOSE_PAY initStyle;
    class A1,A2,A3,A4,A5,A6,A7,A8,A9,A10 aStyle;
    class B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12 bStyle;
```

### 9.2. Ma Trận So Sánh Kỹ Thuật 3 Kênh Bán Hàng

| Tiêu Chí Kỹ Thuật | Kênh 1: Ăn Tại Bàn (Dine-In) | Kênh 2: Giao Hàng (QR Delivery) | Kênh 3: Mang Về (TakeAway POS) |
|---|---|---|---|
| **Hình Thức Khởi Tạo** | Khách quét mã QR dán tại bàn (`table_id`) | Khách quét mã QR Poster / Banner quảng cáo | Nhân viên thao tác trực tiếp trên Web POS Quầy |
| **Dữ Liệu Bắt Buộc** | `branch_id`, `table_id`, danh sách món | `branch_id`, `recipient_phone`, `delivery_address` | `branch_id`, `customer_phone` (để tra cứu CRM) |
| **Phí Vận Chuyển** | 0 VNĐ | **Cố định 20.000 VNĐ** (cộng tự động vào đơn) | 0 VNĐ |
| **Chính Sách Thanh Toán** | • Nhánh A: 100% VietQR trước<br>• Nhánh B: Tiền mặt / VietQR sau | **Bắt buộc 100% VietQR trả trước** (Khóa COD hoàn toàn) | Thu tiền sau khi pha chế xong (Tiền mặt / VietQR) |
| **Chương Trình 10 Ly Tặng 1** | ❌ **KHÔNG ÁP DỤNG** (Không tích lũy / đổi ly) | ❌ **KHÔNG ÁP DỤNG** (Không tích lũy / đổi ly) | ✅ **ÁP DỤNG DUY NHẤT** (Tích ly & Đổi ly miễn phí) |
| **Thời Điểm Vào KDS Bếp** | • Nhánh A: Sau khi PayOS báo Paid<br>• Nhánh B: Vào bếp ngay khi bấm đặt món | Vào bếp sau khi PayOS báo Paid | Vào bếp ngay khi thu ngân bấm xác nhận đơn |

### 9.3. Kiến Trúc Chấm Công Khóa Mạng WiFi (WiFi-Locked Attendance)

```mermaid
sequenceDiagram
    autonumber
    actor NV as Nhân Viên (Staff Browser)
    participant POS as Web POS / Attendance Route
    participant BE as .NET 8 Backend API
    participant DB as PostgreSQL 16
    participant HUB as SignalR NotificationHub

    NV->>POS: Truy cập (pos)/attendance & Nhập Mã Nhân Viên (VD: NV-088)
    POS->>BE: POST /api/v1/attendance/check-in { employeeCode: "NV-088", clientIp: "192.168.1.45", bssid: "00:14:22:01:23:45" }
    
    Note over BE,DB: BƯỚC 1: DUAL-CHECK KIỂM TRA MẠNG WIFI
    BE->>DB: Query bảng BranchWifiConfigs theo branch_id
    DB-->>BE: Trả về danh sách BSSID & Allowed IP Subnets hợp lệ
    
    alt IP hoặc BSSID KHÔNG khớp với cấu hình chi nhánh
        BE-->>POS: HTTP 403 Forbidden: "Bạn không kết nối đúng mạng WiFi của quán!"
        POS-->>NV: Hiển thị thông báo đỏ: Chấm công thất bại!
    else Mạng WiFi hợp lệ
        Note over BE,DB: BƯỚC 2: KIỂM TRA ĐỊNH DANH NHÂN VIÊN & CA LÀM
        BE->>DB: Query User & ShiftSchedule theo employeeCode
        alt Mã NV không tồn tại hoặc không có ca hôm nay
            BE-->>POS: HTTP 400 Bad Request: "Mã NV không hợp lệ hoặc chưa được phân ca!"
        else Thông tin hợp lệ
            BE->>DB: INSERT INTO Attendances (check_in_time, verified_ip, verified_bssid, status='OnTime')
            DB-->>BE: Confirm Inserted
            BE->>HUB: Broadcast 'StaffCheckedInEvent' tới Group "Branch_{branchId}_Manager"
            BE-->>POS: HTTP 200 OK: "Chấm công thành công lúc 07:55 AM (Đúng giờ)"
            POS-->>NV: Hiển thị màn hình xanh thành công & mở quyền POS
        end
    end
```

---

# 10. BẢO MẬT ĐA LỚP, MA TRẬN PHÂN QUYỀN RBAC & AUDIT TRAILS

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              MÔ HÌNH BẢO MẬT PHÒNG THỦ CHIỀU SÂU (6 LỚP)                                │
├──────────────────────────┬─────────────────────────────────────────────────────────────────────────────┤
│ 1. Edge & WAF Layer      │ Cloudflare WAF, NGINX SSL Termination (TLS 1.3), Chống DDoS Lớp 7,          │
│                          │ Rate Limiting phân tầng (60 req/min Khách hàng, 300 req/min POS quầy).      │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 2. Network Isolation     │ Mạng nội bộ Docker Bridge Network: PostgreSQL (5432) và Redis (6379)        │
│                          │ bị khóa cổng từ Internet, chỉ cho phép Container Backend API kết nối.       │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 3. Identity & JWT RBAC   │ Access Token (RS256/HS256, TTL 60 phút) + Refresh Token Rotation lưu Redis. │
│                          │ Phân quyền Claims-based trên 5 vai trò chính thức.                          │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 4. Webhook Integrity     │ Xác thực chữ ký số HMAC-SHA256 bí mật cho mọi callback từ PayOS VietQR.     │
│                          │ Chống tấn công giả mạo biến động số dư hoặc lặp gói tin (Replay Attack).   │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 5. Data Sanitation       │ 100% truy vấn DB tham số hóa qua EF Core 8 (Chống SQL Injection).           │
│                          │ FluentValidation lọc sạch XSS payload trong dữ liệu đầu vào.                │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 6. Immutable Audit Trail │ Ghi nhật ký bất biến vào bảng AuditLogs cho mọi hành vi nhạy cảm: đổi giá, │
│                          │ sửa định mức BOM, kết ca két tiền, xóa món ăn, cấu hình lại mạng WiFi.      │
└──────────────────────────┴─────────────────────────────────────────────────────────────────────────────┘
```

### Bảng Ma Trận Phân Quyền Chi Tiết (RBAC Matrix):

| Nhóm Tài Nguyên API | Khách Hàng (`Customer`) | Thu Ngân / Phục Vụ (`Staff`) | Barista / Bếp (`Barista`) | Quản Lý Chi Nhánh (`Manager`) | Chủ Chuỗi (`Admin`) |
|---|:---:|:---:|:---:|:---:|:---:|
| **Auth & Profile** | Đăng nhập SĐT / OTP | Đăng nhập Mã NV | Đăng nhập Mã NV | Đăng nhập Email/2FA | Toàn quyền Quản trị |
| **Dine-in / Delivery Menu** | Xem / Đặt món | Xem / Đặt món | Xem đơn KDS | Xem / Khóa món | Toàn quyền CRUD |
| **Takeaway POS & 10 Ly** | ❌ Không có quyền | Toàn quyền Bán POS | ❌ Không có quyền | Xem báo cáo POS | Toàn quyền Quản trị |
| **KDS Queue & 86-Toggle** | ❌ Không có quyền | Xem trạng thái món | Toàn quyền KDS / 86 | Toàn quyền Giám sát | Toàn quyền Quản trị |
| **Ca Két Tiền & Z-Report** | ❌ Không có quyền | Khai báo tiền ca | ❌ Không có quyền | Mở/Kết ca & Ký duyệt | Xem P&L hợp nhất |
| **Kho Nguyên Liệu & BOM** | ❌ Không có quyền | Xem tồn quầy bar | Xem công thức BOM | Xuất/Nhập/Kiểm kê | CRUD Công thức BOM |
| **Chấm Công Khóa WiFi** | ❌ Không có quyền | Check-in / Check-out | Check-in / Check-out | Cấu hình BSSID/IP | Xem toàn chuỗi |
| **AI Combo & Dynamic Price** | Xem gợi ý RAG | ❌ Không có quyền | ❌ Không có quyền | Xem bảng giá vùng | Duyệt AI-2 / Đổi giá |
| **Báo Cáo P&L & Doanh Thu** | ❌ Không có quyền | Xem doanh thu ca | ❌ Không có quyền | Báo cáo chi nhánh | Báo cáo chuỗi hợp nhất |

---

# 11. TÔ-PÔ TRIỂN KHAI, HẠ TẦNG & NON-FUNCTIONAL REQUIREMENTS (NFRS)

### 11.1. Sơ Đồ Tô-Pô Triển Khai Thực Tế (Docker Compose Topology)

```mermaid
flowchart TD
    subgraph PUBLIC_INTERNET["🌐 MẠNG INTERNET CÔNG CỘNG"]
        CLIENT_BROWSER["📱 Safari / Chrome (Khách Hàng PWA)"]
        STAFF_BROWSER["💻 Tablet / PC Quầy POS & KDS Bếp"]
        MGR_BROWSER["🏢 Laptop / Desktop Quản Lý & Admin"]
        EXT_PAYOS_SRV["💳 PayOS Webhook Delivery Server"]
    end

    subgraph HOST_SERVER["🖥️ PRODUCTION LINUX VPS / CLOUD HOST (UBUNTU 22.04 LTS)"]
        direction TB
        
        subgraph DMZ["🛡️ DMZ INGRESS (Public Ports: 80, 443)"]
            NGINX_CTR["NGINX Container (Alpine Linux)<br>• Let's Encrypt SSL/TLS Auto-Renewal<br>• Reverse Proxy Router<br>• Rate Limiting & Gzip Engine"]
        end

        subgraph DOCKER_NET["🔒 ISOLATED DOCKER BRIDGE NETWORK (smartfb_net)"]
            FE_CTR["Frontend Container (Node.js 20 Alpine)<br>Next.js 14 Standalone SSR Server<br>Internal Port: 3000"]
            BE_CTR["Backend Container (.NET 8 SDK / ASP.NET Core)<br>Kestrel Web API & SignalR Engine<br>Internal Port: 5000"]
            REDIS_CTR["Cache Container (Redis 7.2 Alpine)<br>In-Memory Storage & RedLock Engine<br>Internal Port: 6379 (No Host Binding)"]
            PG_CTR["Database Container (PostgreSQL 16 Alpine)<br>Persistent Relational Storage<br>Internal Port: 5432 (No Host Binding)"]
        end

        subgraph STORAGE_VOLUMES["💾 PERSISTENT DOCKER VOLUMES"]
            VOL_DB[("pg_data Volume<br>[PostgreSQL Tables & WAL Files]")]
            VOL_REDIS[("redis_data Volume<br>[AOF & RDB Snapshots]")]
            VOL_MEDIA[("media_uploads Volume<br>[Local Cached Assets / Logs]")]
        end
    end

    %% Routing
    CLIENT_BROWSER & STAFF_BROWSER & MGR_BROWSER & EXT_PAYOS_SRV -->|"HTTPS (443) / WSS"| NGINX_CTR

    NGINX_CTR -->|"Proxy Pass / (SSR Pages & Static CDN)"| FE_CTR
    NGINX_CTR -->|"Proxy Pass /api/v1/* (REST APIs)"| BE_CTR
    NGINX_CTR -->|"Proxy Pass /hubs/* (Upgrade: WebSocket)"| BE_CTR

    BE_CTR <-->|"Cache-Aside, Locks & Pub/Sub"| REDIS_CTR
    BE_CTR <-->|"Npgsql Connection Pool (Max=100)"| PG_CTR

    PG_CTR --- VOL_DB
    REDIS_CTR --- VOL_REDIS
    BE_CTR --- VOL_MEDIA

    classDef pubStyle fill:#1e293b,stroke:#475569,stroke-width:2px,color:#ffffff;
    classDef dmzStyle fill:#991b1b,stroke:#ef4444,stroke-width:2px,color:#ffffff;
    classDef netStyle fill:#14532d,stroke:#22c55e,stroke-width:2px,color:#ffffff;
    classDef volStyle fill:#701a75,stroke:#ec4899,stroke-width:2px,color:#ffffff;

    class CLIENT_BROWSER,STAFF_BROWSER,MGR_BROWSER,EXT_PAYOS_SRV pubStyle;
    class NGINX_CTR dmzStyle;
    class FE_CTR,BE_CTR,REDIS_CTR,PG_CTR netStyle;
    class VOL_DB,VOL_REDIS,VOL_MEDIA volStyle;
```

### 11.2. Tiêu Chuẩn Đặc Tả Phi Chức Năng (Non-Functional SLAs)

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        MA TRẬN TIÊU CHUẨN PHI CHỨC NĂNG (NON-FUNCTIONAL SLAs)                          │
├────────────────────┬───────────────────────────────────────────────────────────────────────────────────┤
│ 1. Hiệu Năng       │ • P95 API Response Time < 200ms đối với các tác vụ Đọc/Ghi dữ liệu thông thường.  │
│    (Performance)   │ • SignalR WebSocket Event Latency < 500ms từ PayOS Webhook tới Màn hình Bếp KDS.  │
│                    │ • AI Chatbot RAG Response Latency < 1.5 giây cho toàn bộ câu trả lời tư vấn món. │
│                    │ • Khả năng chịu tải đồng thời: Tối thiểu 500 CCU / Chi nhánh mà không suy giảm.   │
├────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ 2. Tính Sẵn Sàng   │ • Cam kết Uptime hệ thống >= 99.9% trong khung giờ hoạt động của quán (06:00-23:00│
│    (Availability)  │ • Graceful Fallback: Nếu AI Gemini lỗi/timeout, hệ thống tự động trả Best-Sellers│
│                    │ • SignalR Auto-Reconnect với cơ chế thử lại theo hàm mũ (Exponential Backoff).    │
├────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ 3. Tính Toàn Vẹn   │ • 100% giao dịch tạo đơn, trừ kho BOM và ca két được bảo vệ bởi ACID Transaction. │
│    & Nhất Quán     │ • RedLock ngăn chặn 100% tình trạng đặt trùng bàn hoặc trừ âm kho nguyên liệu.    │
├────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ 4. Khả Năng Mở     │ • Kiến trúc Stateless Web API cho phép nhân bản (Scale Out) thêm container dễ dàng│
│    Rộng (Scale)    │ • Redis Pub/Sub Backplane đảm bảo broadcast đồng bộ trên nhiều API servers.       │
│                    │ • Sẵn sàng phân tách Read/Write Database Replicas khi mở rộng trên 50 chi nhánh.  │
└────────────────────┴───────────────────────────────────────────────────────────────────────────────────┘
```

### 11.3. Ma Trận Ranh Giới Phạm Vi & Điểm Nối Tương Lai (Scale-Up Matrix)

| Phân Hệ / Tính Năng | 16-Tuần 4-Thành Viên MVP (Active v2.5.0) | Scale Up / Future Work | C# Interface Điểm Nối Mở Rộng |
|---|:---:|:---:|---|
| **Đặt Món Tại Bàn (Dine-In)** | ✅ 2 Nhánh (VietQR trước / Tiền mặt sau) | — | Nghiệp vụ cốt lõi tại chỗ. |
| **Giao Hàng Tận Nơi (Delivery)** | ✅ SĐT + Địa chỉ, Phí 20k, 100% VietQR | 🔮 Tích hợp AhaMove / GrabExpress | `IDeliveryDispatchPartner` |
| **Bán Mang Về (Takeaway)** | ✅ Web POS, Tích 10 ly, Thu tiền sau | — | Nghiệp vụ thu ngân quầy. |
| **Chấm Công Nhân Viên** | ✅ Khóa Mạng WiFi (BSSID/IP + Mã NV) | 🔮 Sinh trắc học FaceID | `IBiometricAttendanceProvider` |
| **Ứng Dụng Nhân Viên** | ✅ 100% Web Responsive (KDS & POS) | ❌ XÓA Staff Mobile App | Loại bỏ hoàn toàn App di động. |
| **AI-1: Tư Vấn Khẩu Vị RAG** | ✅ Gemini 1.5 Flash + Context Menu | — | `IGeminiAiClient` |
| **AI-2: Khai Phá Combo Món** | ✅ Apriori / FP-Growth + Admin duyệt | — | `IAssociationRuleMiner` |
| **AI-3: Hỏi Đáp Số Liệu Kinh Doanh** | — | 🔮 Text-to-SQL Analytics | `ITextToSqlAnalyticsEngine` |
| **AI-4: Dự Báo Rời Bỏ (Churn)** | — | 🔮 XGBoost / Random Forest RFM | `IChurnPredictionEngine` |
| **AI-5: Dự Báo Nhu Cầu Món** | — | 🔮 Demand Forecasting & Auto PO | `IDemandForecastingEngine` |
| **Đồng Bộ Offline Mesh P2P** | — | 🔮 IndexedDB ServiceWorker Sync | Hoạt động qua Internet ổn định. |

---

> [!TIP]
> **Kết Luận Kiến Trúc:** Bản đặc tả kiến trúc tổng quan v2.5.0 đã hoàn chỉnh 100%, bảo đảm tính nhất quán tuyệt đối với các bản đặc tả gốc, sẵn sàng làm kim chỉ nam kỹ thuật cho toàn bộ giai đoạn triển khai mã nguồn Backend (.NET 8), Frontend (Next.js 14 Monorepo), Hạ tầng (Docker & NGINX) và Tích hợp Trí tuệ Nhân tạo.
