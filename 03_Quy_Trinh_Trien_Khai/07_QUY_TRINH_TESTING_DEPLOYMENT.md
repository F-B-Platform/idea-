# 🧪 QUY TRÌNH 7: TESTING, TÍCH HỢP AI ENGINE & DEPLOYMENT

> **Mục tiêu:** Kiểm thử toàn diện hệ thống, tích hợp các tính năng AI thông minh và triển khai (Deploy) sản phẩm lên VPS Production.

---

## 1. NHỮNG ĐIỂM BẮT BUỘC PHẢI LÀM RÕ TRONG BƯỚC NÀY

### 1.1 Quy Trình Kiểm Thử 3 Cấp Độ (Testing Strategy)

```
Level 1: Unit & Integration Testing
  ├── BE: Test các Business Logic trong Application Layer bằng xUnit
  └── FE: Test các Component UI và Zustand Stores

Level 2: Cross-Testing (Kiểm thử chéo nội bộ team)
  ├── FE1 & FE2 test toàn bộ 45+ API Endpoints của Backend
  └── BE1 & BE2 test trải nghiệm trên thiết bị di động thật (iOS / Android)

Level 3: End-to-End (E2E Workflow Testing)
  └── Chạy kịch bản thực tế 12 Workflows: Đặt món ➔ KDS ➔ Thanh toán ➔ Doanh thu
```

---

### 1.2 Tích Hợp AI Engine (Google Gemini API)

* **AI-5: Chatbot Gợi Ý Món Ăn:**
  * Endpoint: `POST /api/v1/ai/chat`
  * System Prompt: Truyền danh sách Menu hiện tại + Yêu cầu/Dị ứng của khách → Gemini trả về đoạn chat tư vấn + ID món gợi ý.
* **AI-1: Thống Kê Hỏi Đáp Tiếng Việt:**
  * Endpoint: `POST /api/v1/ai/analytics`
  * Chuyển câu hỏi tiếng Việt ("Doanh thu hôm nay bao nhiêu?") → Query SQL Dữ liệu → Gemini tổng hợp báo cáo.

---

### 1.3 Quy Trình Deploy Lên Server (VPS & Docker)

```
[ Git Repository (main branch) ]
       │
       ▼
[ VPS Linux Server (Ubuntu 22.04) ]
       │
       ├── docker compose up -d
       │      ├── Container 1: postgres:16-alpine (Port 5432)
       │      ├── Container 2: redis:7-alpine (Port 6379)
       │      ├── Container 3: smartfb-backend (.NET 8 Web API - Port 5000)
       │      └── Container 4: smartfb-frontend (Next.js 14 - Port 3000)
       │
       ▼
[ Nginx Reverse Proxy + SSL Certbot (HTTPS) ]
       │
       ▼
[ Domain Public: https://smartfb.vn ]
```

---

## 📥 INPUT & 📤 OUTPUT CỦA QUY TRÌNH 7

* **Input:** Codebase Backend & Frontend hoàn chỉnh từ Quy trình 5 & 6.
* **Output:**
  * Hệ thống hoàn chỉnh 0 bug nghiêm trọng.
  * Server VPS hoặt động 24/7 với đường dẫn HTTPS công khai.
  * Báo cáo đồ án, Slide thuyết trình & Video demo hoạt động.
