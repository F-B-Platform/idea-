# 💰 CHI PHÍ HỆ THỐNG SMART F&B OS

> **Chuỗi 3 chi nhánh** | 71 tính năng | 5 AI Module  
> **Ngày lập:** 2026-08-10  
> **Nguyên tắc:** Chỉ tính chi phí BẮT BUỘC — cái nào miễn phí hoặc con người tự làm được thì loại bỏ.

---

## 🔍 PHÂN LOẠI: BẮT BUỘC vs MIỄN PHÍ / TỰ LÀM

| Hạng mục | Bắt buộc trả tiền? | Lý do |
|---|---|---|
| VPS / Cloud hosting | ✅ Bắt buộc | Cần server chạy Backend + AI + DB |
| Domain + SSL | ✅ Bắt buộc | Cần tên miền cho PWA, Dashboard |
| LLM API (GPT/Gemini) | ✅ Bắt buộc | Chatbot AI-5 + AI Thống kê AI-1 |
| TV/Màn hình KDS | ✅ Bắt buộc | Hiển thị đơn hàng cho Barista |
| Máy in nhiệt | ✅ Bắt buộc | In bill/receipt cho khách |
| VietQR API | ❌ Miễn phí | API mở, không mất phí |
| Zalo OA (free tier) | ❌ Miễn phí | Free ~500 msg/tháng (đủ dùng) |
| SendGrid Email | ❌ Miễn phí | Free 100 email/ngày |
| Firebase Push (FCM) | ❌ Miễn phí | Push notification miễn phí |
| Weather API | ❌ Miễn phí | OpenWeatherMap free 1000 calls/day |
| Google Fonts | ❌ Miễn phí | Hoàn toàn miễn phí |
| Cloudflare CDN | ❌ Miễn phí | Free tier đủ dùng |
| Let's Encrypt SSL | ❌ Miễn phí | SSL certificate miễn phí |
| Đào tạo nhân viên | ❌ Tự làm | Chủ quán / QL tự đào tạo NV |
| Tài liệu hướng dẫn | ❌ Tự làm | Team dev viết khi bàn giao |
| Design QR Code | ❌ Tự làm | Canva / tự thiết kế + in |
| Máy chấm công sinh trắc | ❌ Không cần | Dùng App QR + GPS thay thế |
| Tablet dự phòng | ❌ Không cần | Dùng điện thoại NV thay thế |

---

## 📊 2 BẢNG SO SÁNH: TỐI ƯU vs BÌNH THƯỜNG

---

### BẢNG 1: 🟢 CHI PHÍ TỐI ƯU (Tiết kiệm tối đa)

> Dùng VPS Việt Nam giá rẻ, tận dụng free tier, phần cứng tối thiểu, team nhỏ gọn.

#### A. Chi phí ban đầu (One-time)

| # | Hạng mục | Chi tiết | Chi phí (VNĐ) |
|---|---|---|---|
| 1 | **Phần mềm** | | |
| | Frontend: QR PWA + KDS + Staff App | React/Next.js + React Native | 180.000.000 |
| | Frontend: Manager App + Admin Dashboard | Flutter + Next.js | 140.000.000 |
| | Backend API + WebSocket + DB | NestJS + Socket.IO + PostgreSQL | 150.000.000 |
| | AI Engine (5 module) | Python + LangChain + scikit-learn | 140.000.000 |
| | DevOps + Testing + Bug fix | CI/CD + QA | 60.000.000 |
| | **Subtotal Phần mềm** | | **670.000.000** |
| 2 | **Phần cứng (3 quán)** | | |
| | TV 32" cơ bản × 3 | Màn hình KDS | 12.000.000 |
| | Android Box × 3 | Chạy KDS trên TV | 4.500.000 |
| | Máy in nhiệt × 3 | In bill | 6.000.000 |
| | QR acrylic × 60 bàn | 20 bàn/quán × 30K | 1.800.000 |
| | **Subtotal Phần cứng** | | **24.300.000** |
| 3 | **Triển khai** | | |
| | Lắp đặt + cấu hình 3 quán | Đi quán setup | 3.000.000 |
| | Hỗ trợ go-live 1 tuần | On-site hỗ trợ | 5.000.000 |
| | **Subtotal Triển khai** | | **8.000.000** |
| | | | |
| | **TỔNG BAN ĐẦU (TỐI ƯU)** | | **702.300.000** |

#### B. Chi phí hàng tháng (Recurring)

| # | Hạng mục | Chi tiết | Chi phí/tháng (VNĐ) |
|---|---|---|---|
| 1 | VPS Việt Nam (1 máy all-in-one) | 4 vCPU, 8GB RAM, 100GB SSD (VNPT/Viettel IDC) | 800.000 |
| 2 | Domain | .vn hoặc .com | 30.000 |
| 3 | LLM API (Gemini Flash / GPT-4o-mini) | ~300 query/ngày × 30 ngày | 400.000 |
| 4 | Object Storage (ảnh feedback) | MinIO self-hosted trên VPS | 0 |
| 5 | SSL | Let's Encrypt (miễn phí) | 0 |
| 6 | CDN | Cloudflare free | 0 |
| 7 | Push Notification | Firebase FCM (miễn phí) | 0 |
| 8 | Zalo OA | Free tier | 0 |
| 9 | VietQR | Miễn phí | 0 |
| 10 | Backup | Script tự backup hàng ngày | 0 |
| 11 | Bảo trì phần mềm | Bug fix cơ bản, team nội bộ | 5.000.000 |
| | | | |
| | **TỔNG HÀNG THÁNG (TỐI ƯU)** | | **6.230.000** |

#### C. Tổng năm đầu (Tối ưu)

| | Tính toán | Tổng (VNĐ) |
|---|---|---|
| Ban đầu + 12 tháng vận hành | 702 triệu + (6,2 triệu × 12) | **~777 triệu VNĐ** |

---

### BẢNG 2: 🔵 CHI PHÍ BÌNH THƯỜNG (Đầy đủ, chuyên nghiệp)

> Dùng Cloud chuyên dụng, server tách riêng, bảo trì SLA, phần cứng chất lượng cao.

#### A. Chi phí ban đầu (One-time)

| # | Hạng mục | Chi tiết | Chi phí (VNĐ) |
|---|---|---|---|
| 1 | **Phần mềm** | | |
| | Frontend: QR PWA + KDS + Staff App | React/Next.js + React Native | 275.000.000 |
| | Frontend: Manager App + Admin Dashboard | Flutter + Next.js | 212.500.000 |
| | Backend API + WebSocket + DB | NestJS + Socket.IO + PostgreSQL | 243.000.000 |
| | AI Engine (5 module) | Python + LangChain + scikit-learn | 234.500.000 |
| | DevOps + Testing + Bug fix | CI/CD + QA + UAT | 122.500.000 |
| | **Subtotal Phần mềm** | | **1.087.500.000** |
| 2 | **Phần cứng (3 quán)** | | |
| | TV 43" chất lượng cao × 3 | Màn hình KDS | 24.000.000 |
| | Mini PC × 3 | Chạy KDS trên TV | 9.000.000 |
| | Máy in nhiệt chuyên dụng × 3 | In bill nhanh | 12.000.000 |
| | QR acrylic cao cấp × 60 bàn | 20 bàn/quán × 50K | 3.000.000 |
| | Router WiFi chuyên dụng × 3 | Kết nối ổn định | 9.000.000 |
| | Tablet backup × 3 | Dự phòng KDS | 15.000.000 |
| | **Subtotal Phần cứng** | | **72.000.000** |
| 3 | **Triển khai** | | |
| | Lắp đặt + cấu hình 3 quán | Kỹ thuật viên chuyên nghiệp | 9.000.000 |
| | Hỗ trợ go-live 2 tuần | On-site + remote | 15.000.000 |
| | Đào tạo nhân viên 3 quán | 2 buổi/quán | 6.000.000 |
| | Tài liệu + Video hướng dẫn | PDF + Video cho 4 Actor | 5.000.000 |
| | **Subtotal Triển khai** | | **35.000.000** |
| | | | |
| | **TỔNG BAN ĐẦU (BÌNH THƯỜNG)** | | **1.194.500.000** |

#### B. Chi phí hàng tháng (Recurring)

| # | Hạng mục | Chi tiết | Chi phí/tháng (VNĐ) |
|---|---|---|---|
| 1 | VPS Backend + WebSocket | 4 vCPU, 8GB RAM (DigitalOcean/AWS) | 1.500.000 |
| 2 | VPS AI Engine (tách riêng) | 4 vCPU, 8GB RAM | 1.200.000 |
| 3 | Managed PostgreSQL | 2 vCPU, 4GB RAM | 1.000.000 |
| 4 | Redis managed | 1GB RAM | 500.000 |
| 5 | Object Storage (S3) | 50GB/tháng | 300.000 |
| 6 | Domain | .com | 50.000 |
| 7 | LLM API (GPT-4o / Gemini Pro) | ~500 query/ngày × 30 ngày | 2.000.000 |
| 8 | Zalo OA (gói trả phí) | Gửi voucher/thông báo không giới hạn | 500.000 |
| 9 | SendGrid (gói trả phí) | Email báo cáo EOD | 250.000 |
| 10 | Backup tự động | Daily snapshot | 300.000 |
| 11 | Monitoring (Grafana/UptimeRobot Pro) | Uptime + alert | 500.000 |
| 12 | Bảo trì phần mềm (SLA) | Bug fix + cập nhật + support 8/5 | 15.000.000 |
| | | | |
| | **TỔNG HÀNG THÁNG (BÌNH THƯỜNG)** | | **23.100.000** |

#### C. Tổng năm đầu (Bình thường)

| | Tính toán | Tổng (VNĐ) |
|---|---|---|
| Ban đầu + 12 tháng vận hành | 1,19 tỷ + (23,1 triệu × 12) | **~1,47 tỷ VNĐ** |

---

## 📊 SO SÁNH 2 PHƯƠNG ÁN

| Chỉ tiêu | 🟢 Tối ưu | 🔵 Bình thường | Chênh lệch |
|---|---|---|---|
| **Chi phí ban đầu** | **702 triệu** | **1,19 tỷ** | -492 triệu (-41%) |
| **Chi phí hàng tháng** | **6,2 triệu** | **23,1 triệu** | -16,9 triệu (-73%) |
| **Tổng năm đầu** | **~777 triệu** | **~1,47 tỷ** | -693 triệu (-47%) |
| | | | |
| Phần mềm | 670 triệu | 1,09 tỷ | Team nhỏ vs Team lớn |
| Phần cứng | 24,3 triệu | 72 triệu | Cơ bản vs Cao cấp |
| Server | 1 VPS all-in-one | 4 server tách riêng | Gộp vs Tách |
| LLM API | Gemini Flash (rẻ) | GPT-4o (mạnh hơn) | $0.075 vs $2.5/1M token |
| Bảo trì | Team nội bộ | SLA chuyên nghiệp | Tự fix vs Có support |
| Backup | Script tự viết | Managed backup | Thủ công vs Tự động |
| Monitoring | Free tools | Grafana Pro | Cơ bản vs Đầy đủ |

---

## 💡 PHÂN TÍCH CHI TIẾT: TIẾT KIỆM Ở ĐÂU?

### 1. Phần mềm: Tiết kiệm 420 triệu (-39%)

| Cách tối ưu | Tiết kiệm |
|---|---|
| **Team 3-4 người** thay vì 6-7 người (dev full-stack kiêm nhiệm) | ~200 triệu |
| **Bỏ UAT chuyên nghiệp** — chủ quán test trực tiếp | ~35 triệu |
| **Dùng open-source UI kit** — giảm thời gian design | ~50 triệu |
| **AI dùng model nhẹ** (scikit-learn, Prophet) — không cần GPU | ~95 triệu |
| **Bỏ tài liệu formal** — README + inline comment đủ | ~14 triệu |

### 2. Phần cứng: Tiết kiệm 47,7 triệu (-66%)

| Cách tối ưu | Tiết kiệm |
|---|---|
| **TV 32" cơ bản** thay vì 43" cao cấp | 12 triệu |
| **Android Box 1,5 triệu** thay vì Mini PC 3 triệu | 4,5 triệu |
| **Máy in nhiệt 2 triệu** thay vì 4 triệu | 6 triệu |
| **Bỏ Router chuyên dụng** — dùng WiFi quán có sẵn | 9 triệu |
| **Bỏ Tablet dự phòng** — dùng ĐT nhân viên | 15 triệu |
| **QR acrylic 30K** thay vì 50K | 1,2 triệu |

### 3. Hạ tầng hàng tháng: Tiết kiệm 16,9 triệu/tháng (-73%)

| Cách tối ưu | Tiết kiệm/tháng |
|---|---|
| **1 VPS gộp** tất cả (Backend + AI + DB + Redis) thay vì 4 server tách | 2,4 triệu |
| **Gemini Flash** (rẻ hơn 30x so với GPT-4o) | 1,6 triệu |
| **MinIO self-hosted** thay vì S3 trả phí | 300K |
| **Free tier** (Zalo OA, SendGrid, FCM, Cloudflare) | 1,25 triệu |
| **Monitoring miễn phí** (UptimeRobot free + logs) | 500K |
| **Bảo trì team nội bộ** thay vì SLA outsource | 10 triệu |

---

## 📈 ROI — HOÀN VỐN

### Tiết kiệm hàng tháng khi dùng Smart F&B OS (cả 3 quán)

| Tiết kiệm từ đâu | Số tiền/tháng (VNĐ) |
|---|---|
| Bỏ thu ngân (3 quán × 1 NV × 7 triệu) | 21.000.000 |
| Giảm thất thoát nguyên liệu (15% → 2%) | 12.000.000 - 30.000.000 |
| Bỏ POS License (3 quán) | 6.000.000 - 12.000.000 |
| Giảm chiết khấu Grab/ShopeeFood (20-30%) | 15.000.000 - 40.000.000 |
| **TỔNG TIẾT KIỆM** | **54.000.000 - 103.000.000** |

### Thời gian hoàn vốn

| Phương án | Chi phí ban đầu | Tiết kiệm ròng/tháng | Hoàn vốn |
|---|---|---|---|
| 🟢 **Tối ưu** | 702 triệu | 54 triệu - 6,2 triệu = **47,8 triệu** | **~15 tháng** |
| 🟢 **Tối ưu** (lạc quan) | 702 triệu | 103 triệu - 6,2 triệu = **96,8 triệu** | **~7 tháng** |
| 🔵 **Bình thường** | 1,19 tỷ | 80 triệu - 23,1 triệu = **56,9 triệu** | **~21 tháng** |
| 🔵 **Bình thường** (lạc quan) | 1,19 tỷ | 103 triệu - 23,1 triệu = **79,9 triệu** | **~15 tháng** |

---

## ✅ KHUYẾN NGHỊ

| Đối tượng | Nên chọn | Lý do |
|---|---|---|
| **Startup / Quán mới mở** | 🟢 Tối ưu (~700 triệu) | Tiết kiệm vốn, hoàn vốn nhanh 7-15 tháng |
| **Chuỗi đã ổn định, DT > 500 triệu/tháng** | 🔵 Bình thường (~1,2 tỷ) | Server ổn định, SLA bảo trì, scale tốt |
| **Muốn test trước** | 🟢 Tối ưu (MVP 1 quán trước) | Triển khai 1 quán ~300 triệu, validate rồi mở rộng |

---

## 📌 CÁC DỊCH VỤ MIỄN PHÍ ĐÃ TẬN DỤNG

| Dịch vụ | Free tier | Đủ dùng cho 3 quán? |
|---|---|---|
| **VietQR API** | Hoàn toàn miễn phí | ✅ Không giới hạn |
| **Cloudflare CDN** | Free plan | ✅ Đủ bandwidth |
| **Let's Encrypt SSL** | Miễn phí, tự động renew | ✅ |
| **Firebase Cloud Messaging** | Miễn phí | ✅ Push không giới hạn |
| **Zalo OA** (free tier) | 500 msg/tháng | ✅ Đủ cho 3 quán nhỏ |
| **SendGrid** | 100 email/ngày | ✅ Đủ gửi EOD report |
| **OpenWeatherMap** | 1000 calls/ngày | ✅ Đủ cho AI Chatbot |
| **Google Fonts** | Miễn phí | ✅ |
| **GitHub Actions** (CI/CD) | 2000 min/tháng free | ✅ Đủ cho deploy |
| **UptimeRobot** | 50 monitors free | ✅ Monitoring cơ bản |
