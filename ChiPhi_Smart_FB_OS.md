# 💰 BẢNG TÍNH CHI PHÍ TRIỂN KHAI HỆ THỐNG SMART F&B OS

> **Đối tượng:** Khách hàng sở hữu chuỗi F&B (3 chi nhánh)  
> **Quy mô:** 71 tính năng | 4 Actor | 5 AI Module | 16 Workflow  
> **Ngày lập:** 2026-08-10

---

## 📋 MỤC LỤC

1. [Chi phí phát triển phần mềm (One-time)](#1-chi-phí-phát-triển-phần-mềm-one-time)
2. [Chi phí phần cứng tại quán (One-time)](#2-chi-phí-phần-cứng-tại-quán-one-time)
3. [Chi phí hạ tầng Cloud & API (Hàng tháng)](#3-chi-phí-hạ-tầng-cloud--api-hàng-tháng)
4. [Chi phí nhân sự phát triển](#4-chi-phí-nhân-sự-phát-triển)
5. [Chi phí khác](#5-chi-phí-khác)
6. [TỔNG HỢP CHI PHÍ](#6-tổng-hợp-chi-phí)
7. [Phân tích ROI](#7-phân-tích-roi)
8. [Phương án tối ưu chi phí](#8-phương-án-tối-ưu-chi-phí)

---

## 1. CHI PHÍ PHÁT TRIỂN PHẦN MỀM (One-time)

### 1.1 Frontend Applications

| Module | Công nghệ | Ước tính Man-day | Đơn giá/day (VNĐ) | Thành tiền (VNĐ) |
|---|---|---|---|---|
| **QR Order PWA** (Khách hàng) | React/Next.js — 24 features | 45-55 ngày | 2.500.000 | 112.500.000 - 137.500.000 |
| ├─ Menu browser responsive | | 8 ngày | | |
| ├─ Order flow + Giỏ hàng | | 10 ngày | | |
| ├─ Feedback + Photo Upload + Review | | 7 ngày | | |
| ├─ AI Chatbot UI | | 5 ngày | | |
| ├─ Theo dõi đơn real-time | | 5 ngày | | |
| ├─ CRM (SĐT nhận diện + Loyalty) | | 5 ngày | | |
| └─ Thanh toán + Gọi NV | | 5 ngày | | |
| **KDS Web App** (Barista) | React — Full-screen TV mode | 20-25 ngày | 2.500.000 | 50.000.000 - 62.500.000 |
| ├─ Danh sách đơn real-time | | 6 ngày | | |
| ├─ Công thức pha tự động | | 4 ngày | | |
| ├─ Sơ đồ bàn (Floor Map) | | 5 ngày | | |
| └─ Báo hết món + In bill | | 5 ngày | | |
| **Staff Mobile App** (NV nội bộ) | React Native / Flutter | 25-30 ngày | 2.500.000 | 62.500.000 - 75.000.000 |
| ├─ Alert gọi NV + Yêu cầu bill | | 6 ngày | | |
| ├─ Xác nhận thanh toán + VietQR | | 5 ngày | | |
| ├─ Báo hết món di động | | 3 ngày | | |
| ├─ Sơ đồ bàn di động | | 4 ngày | | |
| └─ Chấm công QR + GPS | | 7 ngày | | |
| **Manager App** (Quản lý) | Flutter / React Native | 30-35 ngày | 2.500.000 | 75.000.000 - 87.500.000 |
| ├─ Mở/Kết ca + Đối soát két | | 7 ngày | | |
| ├─ Nhập/Xuất kho + Kiểm kê | | 10 ngày | | |
| ├─ Báo cáo doanh thu + Biểu đồ | | 8 ngày | | |
| └─ AI Thống kê (chat) | | 5 ngày | | |
| **Admin Dashboard** (Chủ chuỗi) | Next.js — Web Dashboard | 40-50 ngày | 2.500.000 | 100.000.000 - 125.000.000 |
| ├─ Dashboard 3 quán real-time | | 8 ngày | | |
| ├─ P&L tự động + So sánh CN | | 7 ngày | | |
| ├─ Menu/Giá/Combo CRUD | | 8 ngày | | |
| ├─ Nhân sự + Loyalty + Promotion | | 8 ngày | | |
| ├─ AI Module UI (4 AI) | | 5 ngày | | |
| └─ RBAC + Audit Log + Export | | 4 ngày | | |

> **Subtotal Frontend:** 160-195 man-day → **400.000.000 - 487.500.000 VNĐ**

### 1.2 Backend API & Infrastructure

| Module | Công nghệ | Ước tính Man-day | Đơn giá/day (VNĐ) | Thành tiền (VNĐ) |
|---|---|---|---|---|
| **REST API Core** | NestJS / FastAPI | 35-40 ngày | 3.000.000 | 105.000.000 - 120.000.000 |
| ├─ Auth & RBAC (4 role) | | 7 ngày | | |
| ├─ Order Module | | 6 ngày | | |
| ├─ Menu Module | | 5 ngày | | |
| ├─ Inventory Module | | 7 ngày | | |
| ├─ CRM & Loyalty Module | | 5 ngày | | |
| └─ Reporting Module | | 5 ngày | | |
| **WebSocket Server** | Socket.IO | 8-10 ngày | 3.000.000 | 24.000.000 - 30.000.000 |
| **Database Design** | PostgreSQL + Redis | 8-10 ngày | 3.000.000 | 24.000.000 - 30.000.000 |
| **File Storage (Ảnh feedback)** | S3 / MinIO | 3-4 ngày | 3.000.000 | 9.000.000 - 12.000.000 |
| **VietQR Integration** | VietQR API | 5-6 ngày | 3.000.000 | 15.000.000 - 18.000.000 |
| **Notification Service** | Zalo OA + SendGrid | 5-6 ngày | 3.000.000 | 15.000.000 - 18.000.000 |
| **Máy in nhiệt (Receipt Printing)** | ESC/POS Protocol | 4-5 ngày | 3.000.000 | 12.000.000 - 15.000.000 |

> **Subtotal Backend:** 68-81 man-day → **204.000.000 - 243.000.000 VNĐ**

### 1.3 AI Engine (5 Module)

| AI Module | Mô tả | Ước tính Man-day | Đơn giá/day (VNĐ) | Thành tiền (VNĐ) |
|---|---|---|---|---|
| **AI-1** — Thống kê NLP | Query NLP → SQL → Biểu đồ | 15-20 ngày | 3.500.000 | 52.500.000 - 70.000.000 |
| **AI-2** — Combo Suggest | Association rule + Clustering | 8-10 ngày | 3.500.000 | 28.000.000 - 35.000.000 |
| **AI-3** — Churn Prediction | XGBoost / Random Forest | 10-12 ngày | 3.500.000 | 35.000.000 - 42.000.000 |
| **AI-4** — Menu Intelligence | Time-series (Prophet) + Trend | 8-10 ngày | 3.500.000 | 28.000.000 - 35.000.000 |
| **AI-5** — Chatbot RAG | LangChain + Vector DB + LLM | 12-15 ngày | 3.500.000 | 42.000.000 - 52.500.000 |

> **Subtotal AI:** 53-67 man-day → **185.500.000 - 234.500.000 VNĐ**

### 1.4 DevOps & QA

| Hạng mục | Ước tính Man-day | Đơn giá/day (VNĐ) | Thành tiền (VNĐ) |
|---|---|---|---|
| **CI/CD Pipeline** (Docker, GitHub Actions) | 5-7 ngày | 3.000.000 | 15.000.000 - 21.000.000 |
| **Testing (Unit + Integration + E2E)** | 20-25 ngày | 2.000.000 | 40.000.000 - 50.000.000 |
| **UAT & Bug fixing** | 10-15 ngày | 2.500.000 | 25.000.000 - 37.500.000 |
| **Documentation** | 5-7 ngày | 2.000.000 | 10.000.000 - 14.000.000 |

> **Subtotal DevOps & QA:** 40-54 man-day → **90.000.000 - 122.500.000 VNĐ**

---

### TỔNG CHI PHÍ PHÁT TRIỂN PHẦN MỀM

| Hạng mục | Thấp (VNĐ) | Cao (VNĐ) |
|---|---|---|
| Frontend (5 app) | 400.000.000 | 487.500.000 |
| Backend API | 204.000.000 | 243.000.000 |
| AI Engine (5 module) | 185.500.000 | 234.500.000 |
| DevOps & QA | 90.000.000 | 122.500.000 |
| **TỔNG PHẦN MỀM** | **879.500.000** | **1.087.500.000** |

> **~880 triệu — 1,09 tỷ VNĐ** (khoảng $35.000 - $43.500 USD)

---

## 2. CHI PHÍ PHẦN CỨNG TẠI QUÁN (One-time)

> Tính cho **3 chi nhánh**, mỗi quán có quầy pha chế + khu vực phục vụ

### 2.1 Phần cứng mỗi chi nhánh

| Thiết bị | SL | Đơn giá (VNĐ) | Thành tiền (VNĐ) | Ghi chú |
|---|---|---|---|---|
| **TV/Màn hình KDS** (32-43 inch) | 1 | 5.000.000 - 8.000.000 | 5.000.000 - 8.000.000 | Hiển thị đơn hàng real-time |
| **Android Box / Mini PC** (cho KDS) | 1 | 1.500.000 - 3.000.000 | 1.500.000 - 3.000.000 | Chạy KDS Web App trên TV |
| **Máy in nhiệt (Receipt Printer)** | 1 | 2.000.000 - 4.000.000 | 2.000.000 - 4.000.000 | In hóa đơn / bill |
| **QR Code acrylic tại bàn** | 20 | 30.000 - 50.000 | 600.000 - 1.000.000 | QR cố định hoặc NFC Tag |
| **Router WiFi chuyên dụng** | 1 | 1.500.000 - 3.000.000 | 1.500.000 - 3.000.000 | Đảm bảo kết nối ổn định |
| **Tablet dự phòng** (cho QL/Staff) | 1 | 3.000.000 - 5.000.000 | 3.000.000 - 5.000.000 | Backup nếu TV KDS gặp sự cố |
| **Máy chấm công** (tùy chọn mở rộng) | 1 | 3.000.000 - 8.000.000 | 3.000.000 - 8.000.000 | Vân tay / Face ID (không bắt buộc) |

| **Tổng mỗi quán** | | | **16.600.000 - 32.000.000** | |

### 2.2 Tổng 3 chi nhánh

| Hạng mục | Thấp (VNĐ) | Cao (VNĐ) |
|---|---|---|
| Phần cứng x 3 quán | 49.800.000 | 96.000.000 |
| Lắp đặt + Cấu hình (x3) | 6.000.000 | 15.000.000 |
| **TỔNG PHẦN CỨNG** | **55.800.000** | **111.000.000** |

> **~56 triệu — 111 triệu VNĐ** cho cả 3 quán

---

## 3. CHI PHÍ HẠ TẦNG CLOUD & API (Hàng tháng)

### 3.1 Server & Hosting

| Dịch vụ | Spec | Chi phí/tháng (VNĐ) | Ghi chú |
|---|---|---|---|
| **VPS chính** (Backend API + WebSocket) | 4 vCPU, 8GB RAM, 100GB SSD | 800.000 - 1.500.000 | VPS Việt Nam (VNPT/Viettel IDC) hoặc DigitalOcean |
| **VPS phụ** (AI Engine) | 4 vCPU, 8GB RAM, 50GB SSD | 600.000 - 1.200.000 | Chạy AI Model (scikit-learn, Prophet) |
| **Database** (PostgreSQL managed) | 2 vCPU, 4GB RAM | 500.000 - 1.000.000 | Hoặc self-hosted trên VPS chính |
| **Redis** (Cache + Real-time) | 1GB RAM | 200.000 - 500.000 | Hoặc self-hosted |
| **Object Storage** (Ảnh feedback) | 50GB/tháng | 100.000 - 300.000 | S3 / MinIO |
| **CDN** (Tĩnh assets PWA) | 10GB bandwidth | 0 - 200.000 | Cloudflare Free hoặc Bunny CDN |
| **Domain + SSL** | 1 domain | 30.000 - 50.000/tháng | (khoảng 360.000 - 600.000/năm) |
| **Backup tự động** | Daily | 100.000 - 300.000 | Snapshot VPS hàng ngày |

> **Subtotal Server:** **2.330.000 - 5.050.000 VNĐ/tháng**

### 3.2 API bên thứ 3

| API / Service | Pricing Model | Chi phí/tháng (VNĐ) | Ghi chú |
|---|---|---|---|
| **LLM API** (GPT-4o-mini / Gemini Flash) | Pay-per-token | 500.000 - 2.000.000 | Cho AI Chatbot (AI-5) + AI Thống kê (AI-1). Ước tính ~500 query/ngày |
| **Zalo OA API** | Freemium | 0 - 500.000 | Gửi voucher, thông báo cho khách. Free tier ~500 msg/tháng |
| **SendGrid Email** | Free tier 100/day | 0 - 250.000 | Gửi báo cáo EOD, voucher email |
| **VietQR API** | Miễn phí (open API) | 0 | VietQR là API mở, không tính phí |
| **Weather API** (cho AI Chatbot) | Free tier | 0 | OpenWeatherMap free 1000 calls/day |
| **Google Fonts** | Miễn phí | 0 | |
| **Firebase Cloud Messaging** (Push) | Miễn phí | 0 | Push notification cho Staff App |

> **Subtotal API:** **500.000 - 2.750.000 VNĐ/tháng**

### 3.3 Tổng chi phí hạ tầng hàng tháng

| Hạng mục | Thấp (VNĐ) | Cao (VNĐ) |
|---|---|---|
| Server & Hosting | 2.330.000 | 5.050.000 |
| API bên thứ 3 | 500.000 | 2.750.000 |
| **TỔNG HÀNG THÁNG** | **2.830.000** | **7.800.000** |

> **~2,8 triệu — 7,8 triệu VNĐ/tháng** (khoảng $113 - $312 USD/tháng)

---

## 4. CHI PHÍ NHÂN SỰ PHÁT TRIỂN

> Ước tính thời gian phát triển toàn bộ: **5-7 tháng** với team 4-6 người

### 4.1 Đội ngũ phát triển

| Vị trí | SL | Lương/tháng (VNĐ) | Thời gian | Tổng (VNĐ) |
|---|---|---|---|---|
| **Tech Lead / Architect** | 1 | 35.000.000 - 50.000.000 | 6 tháng | 210.000.000 - 300.000.000 |
| **Backend Developer** (Senior) | 1 | 25.000.000 - 40.000.000 | 6 tháng | 150.000.000 - 240.000.000 |
| **Frontend Developer** (Senior) | 1 | 25.000.000 - 35.000.000 | 6 tháng | 150.000.000 - 210.000.000 |
| **Mobile Developer** (Mid-Senior) | 1 | 20.000.000 - 35.000.000 | 5 tháng | 100.000.000 - 175.000.000 |
| **AI/ML Engineer** (Mid-Senior) | 1 | 25.000.000 - 40.000.000 | 4 tháng | 100.000.000 - 160.000.000 |
| **QA/Tester** | 1 | 15.000.000 - 25.000.000 | 4 tháng | 60.000.000 - 100.000.000 |
| **UI/UX Designer** | 1 | 15.000.000 - 25.000.000 | 2 tháng | 30.000.000 - 50.000.000 |
| **DevOps** (Part-time) | 0.5 | 25.000.000 - 35.000.000 | 2 tháng | 25.000.000 - 35.000.000 |

> **Subtotal Nhân sự:** **825.000.000 - 1.270.000.000 VNĐ**

> **LƯU Ý:** Chi phí nhân sự đã BAO GỒM trong chi phí phát triển phần mềm (mục 1). Nếu thuê outsource/công ty phần mềm thì dùng số ở mục 1. Nếu tự build team thì dùng số ở mục 4 này. **KHÔNG CỘNG CHỒNG 2 mục.**

---

## 5. CHI PHÍ KHÁC

### 5.1 Chi phí triển khai & đào tạo

| Hạng mục | Chi phí (VNĐ) | Ghi chú |
|---|---|---|
| **Đào tạo nhân viên** (3 quán x 2 buổi) | 5.000.000 - 10.000.000 | Hướng dẫn sử dụng KDS, Staff App, Manager App |
| **Hỗ trợ Go-live** (2 tuần on-site) | 10.000.000 - 20.000.000 | Kỹ thuật viên đi quán hỗ trợ tuần đầu |
| **Tài liệu hướng dẫn sử dụng** | 3.000.000 - 5.000.000 | Video + PDF cho từng Actor |
| **Design QR Code + In ấn** | 1.000.000 - 3.000.000 | Thiết kế QR đẹp + In bảng acrylic |

> **Subtotal Khác:** **19.000.000 - 38.000.000 VNĐ**

### 5.2 Chi phí bảo trì & hỗ trợ (Hàng tháng sau Go-live)

| Hạng mục | Chi phí/tháng (VNĐ) | Ghi chú |
|---|---|---|
| **Bảo trì phần mềm** (Bug fix, cập nhật) | 5.000.000 - 15.000.000 | Tùy SLA (8h/5 ngày hoặc 24/7) |
| **Monitoring & Alert** | 500.000 - 1.000.000 | Uptime monitoring (UptimeRobot, Grafana) |
| **Backup & Security** | 500.000 - 1.000.000 | |

> **Subtotal Bảo trì:** **6.000.000 - 17.000.000 VNĐ/tháng**

---

## 6. TỔNG HỢP CHI PHÍ

### 6.1 Chi phí ban đầu (One-time)

| Hạng mục | Thấp (VNĐ) | Cao (VNĐ) |
|---|---|---|
| Phát triển phần mềm (Outsource) | 879.500.000 | 1.087.500.000 |
| Phần cứng 3 quán | 55.800.000 | 111.000.000 |
| Triển khai & Đào tạo | 19.000.000 | 38.000.000 |
| **TỔNG BAN ĐẦU** | **954.300.000** | **1.236.500.000** |

> ### CHI PHÍ BAN ĐẦU: ~950 triệu — 1,24 tỷ VNĐ
> ### Khoảng $38.000 — $49.500 USD

### 6.2 Chi phí vận hành hàng tháng (Recurring)

| Hạng mục | Thấp (VNĐ) | Cao (VNĐ) |
|---|---|---|
| Hạ tầng Cloud & API | 2.830.000 | 7.800.000 |
| Bảo trì phần mềm | 6.000.000 | 17.000.000 |
| **TỔNG HÀNG THÁNG** | **8.830.000** | **24.800.000** |

> ### CHI PHÍ HÀNG THÁNG: ~8,8 triệu — 24,8 triệu VNĐ/tháng
> ### Khoảng $353 — $992 USD/tháng

### 6.3 Chi phí năm đầu tiên (Tổng)

| Kịch bản | Tính toán | Tổng (VNĐ) |
|---|---|---|
| **Tiết kiệm** | 954 triệu + (8,8 triệu x 12 tháng) | **~1,06 tỷ VNĐ** |
| **Trung bình** | 1,09 tỷ + (16 triệu x 12 tháng) | **~1,28 tỷ VNĐ** |
| **Cao cấp** | 1,24 tỷ + (24,8 triệu x 12 tháng) | **~1,54 tỷ VNĐ** |

---

## 7. PHÂN TÍCH ROI (Return On Investment)

### 7.1 Tiết kiệm chi phí hàng tháng (cho 3 quán)

| Hạng mục | Trước (Truyền thống) | Sau (Smart F&B OS) | Tiết kiệm/tháng |
|---|---|---|---|
| **Thu ngân** (3 quán x 1 NV x 7 triệu) | 21.000.000 | 0 (QR Self-Order) | **21.000.000** |
| **Thất thoát nguyên liệu** (5-15% giảm xuống dưới 2%) | 15.000.000 - 45.000.000 | 3.000.000 - 6.000.000 | **12.000.000 - 39.000.000** |
| **POS License** (3 quán x 2-5 triệu/tháng) | 6.000.000 - 15.000.000 | 0 | **6.000.000 - 15.000.000** |
| **Grab/ShopeeFood chiết khấu** (20-30%) | 20.000.000 - 50.000.000 | 0 (đặt trực tiếp) | **20.000.000 - 50.000.000** |
| **TỔNG TIẾT KIỆM** | | | **59.000.000 - 125.000.000** |

### 7.2 Tăng doanh thu (ước tính)

| Hạng mục | Ước tính tăng |
|---|---|
| AI gợi ý Combo + Upsell | +10-15% giá trị đơn hàng |
| CRM + Loyalty giữ khách | +15-25% khách quay lại |
| AI Churn Prediction + Voucher | Giữ thêm 10-20% khách sắp bỏ |
| Menu Intelligence tối ưu | +5-10% doanh thu từ tối ưu menu |

### 7.3 Thời gian hoàn vốn

| Kịch bản | Chi phí ban đầu | Tiết kiệm/tháng (ròng) | Hoàn vốn |
|---|---|---|---|
| **Lạc quan** | 950 triệu | 100 triệu (tiết kiệm) - 17 triệu (vận hành) = 83 triệu | **~11-12 tháng** |
| **Trung bình** | 1,1 tỷ | 80 triệu - 16 triệu = 64 triệu | **~17-18 tháng** |
| **Bi quan** | 1,24 tỷ | 59 triệu - 25 triệu = 34 triệu | **~36 tháng** |

> **Kết luận:** Hoàn vốn trong **12-18 tháng** với kịch bản trung bình. Sau đó mỗi tháng lợi nhuận ròng tăng thêm 50-80 triệu/tháng so với trước.

---

## 8. PHƯƠNG ÁN TỐI ƯU CHI PHÍ

### Phương án A: Triển khai FULL (Đề xuất)
- **Chi phí:** ~1,0 - 1,2 tỷ VNĐ
- **Thời gian:** 5-7 tháng
- **Ưu điểm:** Đầy đủ 71 tính năng, 5 AI Module
- **Phù hợp:** Chuỗi 3+ quán, doanh thu > 300 triệu/tháng

### Phương án B: Triển khai MVP (Giai đoạn 1 rồi 2)
- **Giai đoạn 1 (3 tháng):** QR Order + KDS + Staff App + Thanh toán + CRM
  - Chi phí: ~500 - 600 triệu VNĐ
  - Features: ~40 tính năng cốt lõi
- **Giai đoạn 2 (2-3 tháng):** AI Module + Dashboard + Kho + Loyalty
  - Chi phí: ~350 - 450 triệu VNĐ
  - Features: 31 tính năng nâng cao
- **Ưu điểm:** Giảm rủi ro, có sản phẩm dùng sớm hơn
- **Phù hợp:** Budget hạn chế, muốn validate trước

### Phương án C: SaaS / Thuê dịch vụ
- **Không tự build — Thuê platform có sẵn** (KiotViet, iPOS, Sapo FnB...)
- **Chi phí:** 2-8 triệu/tháng/quán = 6-24 triệu/tháng cho 3 quán
- **Hạn chế:** Không có AI, không custom, phụ thuộc bên thứ 3, không sở hữu data
- **Phù hợp:** Quán nhỏ lẻ, không cần AI, không cần custom

---

## GHI CHÚ QUAN TRỌNG

- Giá trên tính theo thị trường Việt Nam 2026, thuê team developer Việt Nam
- Nếu dùng Freelancer giá có thể giảm 30-40% nhưng rủi ro chất lượng cao hơn
- Chi phí LLM API (GPT/Gemini) có thể giảm nhanh theo thời gian (trend giá giảm 50-70%/năm)
- Phần cứng có thể dùng lại thiết bị đã có (TV, tablet, router) để giảm chi phí
- VietQR API hoàn toàn miễn phí, không mất phí thanh toán

> **Khuyến nghị cho khách hàng:** Chọn **Phương án B (MVP)** — đầu tư ~500 triệu giai đoạn 1, validate 2-3 tháng, sau đó mở rộng giai đoạn 2. Giảm rủi ro tài chính mà vẫn có sản phẩm chạy được ngay.
