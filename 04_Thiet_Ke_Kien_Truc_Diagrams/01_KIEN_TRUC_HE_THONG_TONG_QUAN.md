# 🏗️ SƠ ĐỒ KIẾN TRÚC HỆ THỐNG TỔNG QUAN (SYSTEM ARCHITECTURE)

> **Dự án:** Smart F&B Operating System  
> **Kiến trúc:** 4-Tier Clean Architecture Monolith + Real-time SignalR + AI Engine Integration

---

## 1. SƠ ĐỒ KIẾN TRÚC 4 TẦNG (HIGH-LEVEL ARCHITECTURE DIAGRAM)

```mermaid
graph TB
    subgraph TANG1["🖥️ TẦNG 1: PRESENTATION LAYER (FRONTEND NEXT.JS 14)"]
        direction LR
        PWA["📱 QR Order PWA\n(Khách hàng Mobile)"]
        KDS["📺 KDS Kitchen App\n(Barista TV/Tablet)"]
        STAFF["📱 Staff Mobile App\n(Phục vụ PWA)"]
        MGR["💻 Manager Web App\n(Quản lý chi nhánh)"]
        ADMIN["💻 Admin Dashboard\n(Chủ chuỗi Desktop)"]
    end

    subgraph PROTOCOL["⚡ GIAO THỨC TRUYỀN THÔNG"]
        HTTP["HTTP/REST API\n(JSON Payload)"]
        WS["WebSocket / SignalR\n(Real-time 2-way)"]
    end

    subgraph TANG2["⚙️ TẦNG 2: APPLICATION & API LAYER (ASP.NET CORE 8)"]
        direction TB
        GATEWAY["Middleware: Auth (JWT), Rate Limit, CORS, Exception Handler"]
        
        subgraph CLEAN_ARCH[".NET Clean Architecture Solution"]
            API_CTRL["SmartFB.API\n(Controllers & SignalR Hubs)"]
            APP_SRV["SmartFB.Application\n(Services, DTOs, FluentValidation)"]
            DOMAIN_CORE["SmartFB.Domain\n(Entities, Value Objects, Domain Rules)"]
            INFRA_REPO["SmartFB.Infrastructure\n(EF Core, Repositories, Redis Cache)"]
        end
    end

    subgraph TANG3["🤖 TẦNG 3: AI ENGINE & INTEGRATION"]
        GEMINI["Google Gemini API\n(Chatbot RAG & SQL Analytics)"]
        RULE_AI["Logic C# Rule-based Engine\n(Combo & Churn Prediction)"]
    end

    subgraph TANG4["🗄️ TẦNG 4: DATA & INFRASTRUCTURE LAYER"]
        PG["🐘 PostgreSQL 16\n(Primary Relational DB)"]
        REDIS["🔴 Redis 7\n(Distributed Cache & SignalR Backplane)"]
        STORAGE["📁 Local File System / S3\n(Product Images & Assets)"]
    end

    PWA --> HTTP & WS
    KDS --> HTTP & WS
    STAFF --> HTTP & WS
    MGR --> HTTP
    ADMIN --> HTTP

    HTTP & WS --> GATEWAY
    GATEWAY --> API_CTRL
    API_CTRL --> APP_SRV
    APP_SRV --> DOMAIN_CORE
    APP_SRV --> GEMINI & RULE_AI
    INFRA_REPO --> DOMAIN_CORE
    APP_SRV --> INFRA_REPO

    INFRA_REPO --> PG
    INFRA_REPO --> REDIS
    INFRA_REPO --> STORAGE
```

---

## 2. SƠ ĐỒ C4 LEVEL 1: SYSTEM CONTEXT DIAGRAM

```mermaid
C4Context
    title System Context Diagram - Smart F&B Operating System

    Person(customer, "Khách hàng", "Quét mã QR tại bàn, xem menu, đặt món, gọi phục vụ và thanh toán VietQR.")
    Person(barista, "Pha chế / Barista", "Xem đơn hàng real-time trên KDS, xem công thức pha chế, bấm hoàn thành món.")
    Person(staff, "Nhân viên Phục vụ", "Nhận cảnh báo gọi bàn/bill, hỗ trợ khách, xác nhận thanh toán tiền mặt/VietQR.")
    Person(manager, "Quản lý Chi nhánh", "Mở/Kết ca két tiền, quản lý tồn kho, xuất nhập kho, xem báo cáo ca.")
    Person(admin, "Chủ chuỗi (Admin)", "Quản lý Menu toàn chuỗi, phân quyền nhân sự, xem Dashboard báo cáo doanh thu.")

    System(smartfb, "Smart F&B OS", "Hệ thống điều hành quầy F&B thông minh thay thế POS truyền thống.")

    System_Ext(vietqr, "Hệ thống VietQR / NAPAS", "Tạo mã QR thanh toán ngân hàng tự động.")
    System_Ext(gemini, "Google Gemini AI", "Tư vấn món ăn theo khẩu vị và chuyển câu hỏi tiếng Việt thành SQL.")
    System_Ext(fcm, "Firebase Cloud Messaging", "Gửi thông báo đẩy Push Notification.")

    Rel(customer, smartfb, "Quét QR đặt món & thanh toán", "HTTPS / WebSocket")
    Rel(barista, smartfb, "Xem KDS & bấm hoàn thành món", "HTTPS / WebSocket")
    Rel(staff, smartfb, "Nhận Alert & xác nhận thu tiền", "HTTPS / WebSocket")
    Rel(manager, smartfb, "Quản lý ca & xuất nhập kho", "HTTPS")
    Rel(admin, smartfb, "Quản trị toàn chuỗi & cấu hình", "HTTPS")

    Rel(smartfb, vietqr, "Sinh VietQR Code", "HTTPS API")
    Rel(smartfb, gemini, "Gửi Prompt tư vấn & Analytics", "HTTPS API")
    Rel(smartfb, fcm, "Gửi Push Notification", "HTTPS API")
```

---

## 3. SƠ ĐỒ C4 LEVEL 2: CONTAINER DIAGRAM

```mermaid
C4Container
    title Container Diagram - Smart F&B Operating System

    Person(user, "Người dùng hệ thống", "Khách, Barista, Staff, Manager, Admin")

    ContainerBoundary(frontend_b, "Frontend Applications (Next.js 14)") {
        Container(customer_app, "Customer QR PWA", "Next.js 14 / React", "Giao diện PWA mobile-first cho khách hàng đặt món")
        Container(kds_app, "KDS Kitchen App", "Next.js 14 / React", "Màn hình TV/Tablet full-screen hiển thị đơn hàng Bếp")
        Container(admin_app, "Admin & Manager Dashboard", "Next.js 14 / React", "Giao diện Web Desktop/Responsive quản trị hệ thống")
    }

    ContainerBoundary(backend_b, "Backend System (.NET 8)") {
        Container(web_api, "ASP.NET Core Web API", "C# / .NET 8", "Cung cấp 45+ RESTful APIs xác thực, đơn hàng, kho, báo cáo")
        Container(signalr_hub, "SignalR Real-time Hubs", "C# / SignalR", "Quản lý kết nối WebSocket 2 chiều phát đơn hàng tức thì")
    }

    ContainerBoundary(ai_b, "AI Engine") {
        Container(ai_service, "Gemini Integration Service", "C# / Google AI SDK", "Xử lý RAG Chatbot gợi ý món & Text-to-SQL Analytics")
    }

    ContainerBoundary(data_b, "Data Layer (Docker Containers)") {
        ContainerDb(database, "PostgreSQL Database", "PostgreSQL 16", "Lưu trữ toàn bộ dữ liệu 28 bảng relational")
        ContainerDb(cache, "Redis Cache", "Redis 7", "Lưu Session, Distributed Cache & SignalR Backplane")
    }

    Rel(user, customer_app, "Sử dụng trình duyệt Mobile", "HTTPS")
    Rel(user, kds_app, "Sử dụng màn hình TV/Tablet", "HTTPS")
    Rel(user, admin_app, "Sử dụng Laptop/Desktop", "HTTPS")

    Rel(customer_app, web_api, "Gọi REST API", "HTTPS/JSON")
    Rel(customer_app, signalr_hub, "Lắng nghe tiến trình đơn", "WebSocket")

    Rel(kds_app, web_api, "Gọi REST API", "HTTPS/JSON")
    Rel(kds_app, signalr_hub, "Nhận đơn mới tức thì", "WebSocket")

    Rel(admin_app, web_api, "Gọi REST API", "HTTPS/JSON")

    Rel(web_api, ai_service, "Gửi Prompt & Context", "Internal Call")
    Rel(web_api, database, "Đọc/Ghi dữ liệu (EF Core)", "TCP/IP")
    Rel(web_api, cache, "Cache & Session Store", "TCP/IP")
    Rel(signalr_hub, cache, "Pub/Sub Backplane", "TCP/IP")
```

---

## 4. SƠ ĐỒ COMPONENT CLEAN ARCHITECTURE (.NET 8)

```mermaid
graph TD
    subgraph API_LAYER["1. SmartFB.API (Presentation Project)"]
        CTRL["Controllers\n(Auth, Products, Orders, Payments...)"]
        HUBS["SignalR Hubs\n(OrderHub, KitchenHub, NotificationHub)"]
        MIDDLEWARE["Middleware\n(ExceptionHandling, JwtAuth, RateLimiter)"]
    end

    subgraph APP_LAYER["2. SmartFB.Application (Business Logic Project)"]
        SRV_IMPL["Services Implementation\n(OrderService, ProductService, AuthService...)"]
        DTOS["DTOs & ViewModels\n(CreateOrderDto, OrderResponseDto...)"]
        VALIDATORS["FluentValidation Rules\n(OrderValidator, ProductValidator...)"]
        MAPPER["AutoMapper Profiles"]
    end

    subgraph DOMAIN_LAYER["3. SmartFB.Domain (Core Enterprise Logic Project)"]
        ENTITIES["Domain Entities (28 classes)\n(Order, Product, Branch, User...)"]
        VALUE_OBJ["Value Objects & Enums\n(OrderStatus, UserRole, Money...)"]
        REPO_INT["Repository Interfaces\n(IOrderRepository, IProductRepository...)"]
    end

    subgraph INFRA_LAYER["4. SmartFB.Infrastructure (Data & External Project)"]
        DBCONTEXT["AppDbContext (EF Core)"]
        CONFIGS["EF Fluent API Configurations (28 files)"]
        REPO_IMPL["Repositories Implementation\n(OrderRepository, ProductRepository...)"]
        EXT_SERVICES["External Services\n(VietQrService, GeminiAiService, FirebaseService)"]
    end

    CTRL --> APP_LAYER
    HUBS --> APP_LAYER
    MIDDLEWARE --> APP_LAYER

    SRV_IMPL --> DOMAIN_LAYER
    SRV_IMPL --> INFRA_LAYER
    DTOS --> DOMAIN_LAYER

    REPO_IMPL --> DOMAIN_LAYER
    DBCONTEXT --> CONFIGS
    CONFIGS --> DOMAIN_LAYER
```
