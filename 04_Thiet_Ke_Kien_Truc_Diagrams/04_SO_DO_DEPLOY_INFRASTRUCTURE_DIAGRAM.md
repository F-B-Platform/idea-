# 🌐 SƠ ĐỒ TRIỂN KHAI & HẠ TẦNG (DEPLOYMENT & INFRASTRUCTURE DIAGRAM)

> **Dự án:** Smart F&B Operating System  
> **Môi trường:** Production VPS Server (Ubuntu 22.04 LTS + Docker Compose + Nginx Reverse Proxy)

---

## 1. SƠ ĐỒ MẠNG & CONTAINER DOCKER (NETWORK & CONTAINER TOPOLOGY)

```mermaid
graph TB
    subgraph CLIENTS["📱 CLIENT DEVICES (INTERNET)"]
        MOBILE["📱 Smartphone Khách hàng\n(PWA trên Safari/Chrome)"]
        TV["📺 TV / Tablet KDS Bếp\n(Màn hình full-screen)"]
        DESKTOP["💻 Laptop/Desktop\n(Admin & Manager)"]
    end

    subgraph CLOUD_EDGE["🌐 PUBLIC INTERNET & EDGE SECURITY"]
        DNS["🌐 Domain DNS\n(https://smartfb.vn)"]
        CLOUDFLARE["🛡️ Cloudflare / Firewall\n(DDoS Protection & SSL)"]
    end

    subgraph VPS_HOST["🐧 PRODUCTION VPS SERVER (UBUNTU 22.04 LTS)"]
        NGINX["🌐 Nginx Reverse Proxy\n(Port 80/443 SSL Certbot)"]
        
        subgraph DOCKER_NET["🐳 DOCKER INTERNAL NETWORK (smartfb-net)"]
            FE_CONTAINER["📦 Container: smartfb-frontend\n(Next.js 14 Standalone - Port 3000)"]
            BE_CONTAINER["📦 Container: smartfb-backend\n(ASP.NET Core 8 API - Port 5000)"]
            PG_CONTAINER["🐘 Container: smartfb-postgres\n(PostgreSQL 16 - Port 5432)"]
            REDIS_CONTAINER["🔴 Container: smartfb-redis\n(Redis 7 Alpine - Port 6379)"]
        end

        subgraph VOLUMES["💾 PERSISTENT DOCKER VOLUMES"]
            PG_DATA["/var/lib/postgresql/data\n(PostgreSQL Data Volume)"]
            REDIS_DATA["/data\n(Redis AOF Persistence Volume)"]
            UPLOADS["/var/smartfb/uploads\n(Product & Review Images)"]
        end
    end

    MOBILE & TV & DESKTOP --> DNS
    DNS --> CLOUDFLARE
    CLOUDFLARE -->|Port 443 HTTPS| NGINX

    NGINX -->|/ -> Port 3000| FE_CONTAINER
    NGINX -->|/api & /hubs -> Port 5000| BE_CONTAINER

    BE_CONTAINER -->|EF Core Connection| PG_CONTAINER
    BE_CONTAINER -->|Cache & SignalR Backplane| REDIS_CONTAINER
    BE_CONTAINER -->|Save Uploads| UPLOADS

    PG_CONTAINER --- PG_DATA
    REDIS_CONTAINER --- REDIS_DATA
```

---

## 2. CẤU HÌNH PRODUCTION DOCKER COMPOSE SPEC

```yaml
version: '3.8'

services:
  smartfb-postgres:
    image: postgres:16-alpine
    container_name: smartfb-postgres
    restart: always
    environment:
      POSTGRES_DB: ${DATABASE_NAME}
      POSTGRES_USER: ${DATABASE_USER}
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
    ports:
      - "127.0.0.1:5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - smartfb-net

  smartfb-redis:
    image: redis:7-alpine
    container_name: smartfb-redis
    restart: always
    command: redis-server --appendonly yes
    ports:
      - "127.0.0.1:6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - smartfb-net

  smartfb-backend:
    image: smartfb-backend:latest
    container_name: smartfb-backend
    restart: always
    environment:
      - ASPNETCORE_ENVIRONMENT=Production
      - ConnectionStrings__DefaultConnection=Host=smartfb-postgres;Port=5432;Database=${DATABASE_NAME};Username=${DATABASE_USER};Password=${DATABASE_PASSWORD}
      - Redis__ConnectionString=smartfb-redis:6379
    depends_on:
      - smartfb-postgres
      - smartfb-redis
    ports:
      - "127.0.0.1:5000:5000"
    networks:
      - smartfb-net

  smartfb-frontend:
    image: smartfb-frontend:latest
    container_name: smartfb-frontend
    restart: always
    environment:
      - NEXT_PUBLIC_API_URL=https://smartfb.vn/api/v1
      - NEXT_PUBLIC_SIGNALR_URL=https://smartfb.vn/hubs
    depends_on:
      - smartfb-backend
    ports:
      - "127.0.0.1:3000:3000"
    networks:
      - smartfb-net

volumes:
  postgres_data:
  redis_data:

networks:
  smartfb-net:
    driver: bridge
```

---

## 3. CHIẾN LƯỢC BACKUP DỮ LIỆU & PHỤC HỒI (DISASTER RECOVERY)

1. **Auto DB Backup:** Cronjob chạy 2:00 AM hàng ngày thực hiện `pg_dump` nén file SQL lưu sang Cloud Storage (S3 / Google Drive).
2. **Redis Persistence:** Cấu hình Redis `--appendonly yes` (AOF) lưu trữ từng lệnh write xuống ổ đĩa, đảm bảo không mất dữ liệu SignalR session khi khởi động lại server.
3. **Rolling Updates:** Khởi chạy Container bằng Docker Compose không gây downtime cho người dùng.
