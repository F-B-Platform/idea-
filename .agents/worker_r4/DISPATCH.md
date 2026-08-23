## 2026-08-23T13:49:19Z

Bạn là Senior DevOps & Infrastructure Architect chịu trách nhiệm viết lại hoàn chỉnh tệp:
`d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md`

1. Thư mục làm việc của bạn: `d:\Idea_DoAn\.agents\worker_r4\`
Tạo file `d:\Idea_DoAn\.agents\worker_r4\progress.md` và `d:\Idea_DoAn\.agents\worker_r4\handoff.md`.

2. Bắt buộc đọc kỹ Nguồn sự thật (Source of Truth):
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`

3. Yêu cầu chi tiết cho `04_Deployment_Diagram.md` (v2.5.0):
- **Sơ đồ Triển khai Mermaid (Mermaid Deployment Diagram / Architecture Graph)**:
  - Chi tiết các tầng: Client Edge (PWA Next.js 14 on Vercel / NGINX Server), Ingress & Load Balancing (NGINX Reverse Proxy, SSL/TLS Let's Encrypt, Rate Limiting, CORS, WAF), Application Tier (.NET 8 Web API Docker Container, SignalR WebSockets, Background Worker Jobs), Data Tier (PostgreSQL 16 Primary Database, Redis 7 Cluster / Standalone with Persistence AOF/RDB), Storage & AI Tier (AWS S3 / Cloudflare R2 for Assets, Google Gemini 1.5 Flash API, PayOS Webhook Integration, OpenWeatherMap API).
- **Mô hình triển khai chi tiết 2 phương án & Bảng so sánh chuyên sâu**:
  - **Phương án 1 (Khuyến nghị cho Đồ án & Pilot): Cloud VPS Linux (Ubuntu Server 22.04 LTS / Docker Compose / NGINX / CI-CD GitHub Actions)**: Cấu hình phần cứng (4 vCPU, 8GB RAM, 80GB NVMe SSD), phân bổ tài nguyên Docker Containers, chi phí ước tính (~300.000 - 500.000 VNĐ/tháng).
  - **Phương án 2 (Mở rộng Doanh nghiệp Enterprise): Cloud Native Azure Singapore (AKS / Azure App Service / Azure Database for PostgreSQL / Azure Cache for Redis / Azure Blob Storage)**: Kiến trúc High Availability (HA), Multi-zone Redundancy, Auto-scaling, chi phí ước tính ($150 - $350/tháng).
  - **Bảng so sánh Trade-off toàn diện**: Hiệu năng, Chi phí, Độ phức tạp vận hành, Khả năng mở rộng (Scalability), Bảo mật, Phục hồi thảm họa (Disaster Recovery RPO/RTO).
- **Chiến lược Sao lưu & Khôi phục (Backup & Disaster Recovery)**: PostgreSQL `pg_dump` cronjob hàng ngày, Redis snapshot, S3 bucket replication.
- **Giám sát & Cảnh báo (Observability & Monitoring)**: Health Check endpoints (`/health`, `/health/ready`, `/health/live`), Prometheus + Grafana metrics, Structured Logging (Serilog + Seq/Loki), Uptime Robot alert.

4. Tiêu chuẩn:
- Zero Placeholders: Không có TODO hay bảng biểu dang dở.
- 100% cú pháp Mermaid hợp lệ, render rõ ràng và chuyên nghiệp.
