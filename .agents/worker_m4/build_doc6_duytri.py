# -*- coding: utf-8 -*-
"""
Generator for Chi_Phi_Duy_Tri_Hang_Thang.md
100% Full Content, Zero Placeholders, Monthly Recurring Operational Costs, SaaS, SLA & 12-Month Forecast
"""
import os

target = r'd:\Idea_DoAn\02_Bao_Gia_Chi_Phi\Chi_Phi_Duy_Tri_Hang_Thang.md'
os.makedirs(os.path.dirname(target), exist_ok=True)

content = """# 📊 BẢNG KÊ CHI TIẾT CHI PHÍ DUY TRÌ & VẬN HÀNH HÀNG THÁNG
## HỆ THỐNG QUẢN LÝ VÀ VẬN HÀNH QUÁN CÀ PHÊ THÔNG MINH SMART F&B OS

> **Phiên bản:** v2.0.0 (Production Grade & Formal Capstone Defense)  
> **Áp dụng cho quy mô:** Chuỗi từ 1 đến 5 Chi nhánh Cà phê  
> **Kiến trúc vận hành:** Docker Containerized trên Cloud VPS Linux + Cloudflare Edge CDN  
> **Tài liệu tham chiếu:** `PROJECT.md`, `Bang_Bao_Gia_Smart_FB_OS.md`, `technical_contracts.md`  
> **Mục tiêu:** Cung cấp bức tranh tài chính minh bạch về toàn bộ các khoản chi phí định kỳ (Operational Expenditure - OPEX) cần thiết để hệ thống vận hành liên tục, ổn định và an toàn 24/7.

---

## 📑 MỤC LỤC

1. [TỔNG QUAN CƠ CẤU CHI PHÍ VẬN HÀNH ĐỊNH KỲ (OPEX)](#1-tổng-quan-cơ-cấu-chi-phí-vận-hành-định-kỳ-opex)
2. [CHI TIẾT CHI PHÍ HẠ TẦNG MÁY CHỦ & ĐÁM MÂY (CLOUD INFRASTRUCTURE)](#2-chi-tiết-chi-phí-hạ-tầng-máy-chủ--đám-mây-cloud-infrastructure)
3. [CHI TIẾT CHI PHÍ DỊCH VỤ SAAS & API BÊN THỨ BA](#3-chi-tiết-chi-phí-dịch-vụ-saas--api-bên-thứ-ba)
4. [CHI TIẾT VẬT TƯ TIÊU HAO TẠI CÁC ĐIỂM BÁN (CONSUMABLES)](#4-chi-tiết-vật-tư-tiêu-hao-tại-các-điểm-bán-consumables)
5. [CÁC GÓI DỊCH VỤ BẢO TRÌ & HỖ TRỢ KỸ THUẬT (SLA MAINTENANCE TIERS)](#5-các-gói-dịch-vụ-bảo-trì--hỗ-trợ-kỹ-thuật-sla-maintenance-tiers)
6. [BẢNG TỔNG HỢP CHI PHÍ THEO QUY MÔ CHI NHÁNH (1, 3 VÀ 5 QUÁN)](#6-bảng-tổng-hợp-chi-phí-theo-quy-mô-chi-nhánh-1-3-và-5-quán)
7. [DỰ TOÁN NGÂN SÁCH DÒNG TIỀN VẬN HÀNH 12 THÁNG (1-YEAR CASH FLOW FORECAST)](#7-dự-toán-ngân-sách-dòng-tiền-vận-hành-12-tháng-1-year-cash-flow-forecast)
8. [CHIẾN LƯỢC TỐI ƯU HÓA CHI PHÍ & TỰ CÂN ĐỐI DÒNG TIỀN](#8-chiến-lược-tối-ưu-hóa-chi-phí--tự-cân-đối-dòng-tiền)

---

## 1. TỔNG QUAN CƠ CẤU CHI PHÍ VẬN HÀNH ĐỊNH KỲ (OPEX)

Chi phí vận hành hàng tháng của Smart F&B OS được chia làm 4 nhóm chính:
1. **Hạ tầng Máy chủ (VPS & Cloud CDN)**: Chi phí cố định thuê máy chủ ảo Linux để chạy Docker containers (.NET 8 WebApi, Next.js 14 Web Portals, PostgreSQL 16, Redis 7).
2. **Dịch vụ Trí tuệ Nhân tạo & API (Gemini AI & Transactional Services)**: Chi phí biến đổi linh hoạt theo lượng truy vấn thực tế của khách hàng.
3. **Vật tư Tiêu hao (Giấy in nhiệt K80)**: Chi phí giấy in hóa đơn và phiếu nhận nước tại quầy bar.
4. **Bảo trì & Ứng cứu Kỹ thuật (Technical SLA)**: Chi phí hỗ trợ kỹ thuật, sao lưu dữ liệu và khắc phục sự cố hệ thống.

---

## 2. CHI TIẾT CHI PHÍ HẠ TẦNG MÁY CHỦ & ĐÁM MÂY (CLOUD INFRASTRUCTURE)

| Hạng mục Hạ tầng | Cấu hình & Nhà cung cấp | Chi phí Hàng tháng (VNĐ) | Vai trò & Mục đích sử dụng |
|---|---|:---:|---|
| **Cloud VPS Linux (Chính)** | • 4 vCPU Intel Xeon / AMD EPYC<br>• 8 GB RAM DDR4/DDR5<br>• 80 GB NVMe SSD High Speed<br>• Băng thông: 1 Gbps không giới hạn<br>*(Vietnix / AZDIGI / Vultr / DigitalOcean)* | **450.000** | Chạy toàn bộ hệ thống qua Docker Compose: Backend .NET 8, Frontend Next.js 14, PostgreSQL 16 và Redis 7. Đủ tải cho 3 - 5 quán (~1.500 đơn/ngày). |
| **Tên Miền (Domain Name)** | • Tên miền thương hiệu `.vn` hoặc `.com`<br>*(Mắt Bão / PA Việt Nam / Cloudflare)* | **40.000** | ~480.000 VNĐ/năm chia đều cho 12 tháng để duy trì địa chỉ truy cập `smartcoffee.vn`. |
| **Cloudflare Edge CDN & SSL** | • Cloudflare Free Tier (SSL/TLS 1.3, DDoS Protection, Global Caching) | **0 VNĐ** | Tăng tốc độ tải trang PWA menu cho khách hàng, bảo mật chống tấn công từ chối dịch vụ (DDoS). |
| **Dịch vụ Lưu trữ Tệp (Object Storage)** | • Cloudflare R2 / AWS S3 (Miễn phí 10GB đầu tiên) | **0 VNĐ** | Lưu trữ hình ảnh món ăn, ảnh đánh giá của khách hàng và file backup database hàng ngày. |
| **TỔNG CHI PHÍ HẠ TẦNG MÁY CHỦ** | | **490.000 VNĐ / tháng** | Cố định cho cả chuỗi (không tăng khi mở thêm quán thứ 2, thứ 3) |

---

## 3. CHI TIẾT CHI PHÍ DỊCH VỤ SAAS & API BÊN THỨ BA

| Dịch vụ SaaS / API | Bảng Giá & Định mức Sử dụng | Chi phí Ước tính (VNĐ/tháng) | Chính sách & Tối ưu hóa |
|---|---|:---:|---|
| **Cổng Thanh toán VietQR (PayOS / VietQR Open API)** | • Miễn phí 100% không giới hạn giao dịch<br>• 0% phí giao dịch trên mỗi đơn hàng | **0 VNĐ** | Tiền chuyển khoản từ khách hàng chuyển trực tiếp 100% vào tài khoản ngân hàng chính chủ của quán. |
| **Trí tuệ Nhân tạo Google Gemini 1.5 Flash API** | • Định giá: $0.075 / 1 triệu input tokens, $0.30 / 1 triệu output tokens<br>• Ước tính ~2.000 lượt hỏi đáp món/quán/tháng | **150.000** | Hệ thống áp dụng Redis Caching cho các câu hỏi phổ biến (vd: menu, địa chỉ, giờ mở cửa), giảm 75% chi phí API. |
| **Dịch vụ Email Giao dịch (Resend / SendGrid)** | • Gửi báo cáo doanh thu cuối ngày cho Chủ quán & Quản lý<br>• Gói Free: 3.000 emails/tháng | **0 VNĐ** | Nhu cầu thực tế chỉ dùng ~90 emails/tháng cho 3 chi nhánh (hoàn toàn nằm trong hạn mức miễn phí). |
| **TỔNG CHI PHÍ DỊCH VỤ API & SAAS** | | **150.000 VNĐ / tháng** | Linh hoạt theo lưu lượng khách hàng thực tế |

---

## 4. CHI TIẾT VẬT TƯ TIÊU HAO TẠI CÁC ĐIỂM BÁN (CONSUMABLES)

| Vật tư Tiêu hao | Quy cách & Định mức | Số lượng cho 3 Quán | Chi phí Hàng tháng (VNĐ) |
|---|---|:---:|:---:|
| **Giấy In Hóa Đơn Nhiệt K80 (Quầy POS)** | Cuộn K80 x 45mm bọc bạc chống ẩm, in bill thanh toán đơn mang về và biên bản kết ca | 30 Cuộn / tháng (10 cuộn/quán) | **180.000** (6.000đ/cuộn) |
| **Giấy In Phiếu Nhận Nước (Quầy Bếp)** | In ticket dán ly cho đơn giao hàng (Delivery) | 20 Cuộn / tháng | **120.000** |
| **TỔNG CHI PHÍ VẬT TƯ TIÊU HAO** | **Tổng cộng 50 cuộn giấy in nhiệt K80 cho 3 chi nhánh** | | **300.000 VNĐ / tháng** (Chỉ 100.000 VNĐ/quán/tháng) |

---

## 5. CÁC GÓI DỊCH VỤ BẢO TRÌ & HỖ TRỢ KỸ THUẬT (SLA MAINTENANCE TIERS)

Sau thời gian **03 Tháng Bảo Hành Miễn Phí**, khách hàng có thể lựa chọn 1 trong 2 gói dịch vụ hỗ trợ kỹ thuật định kỳ:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        SO SÁNH 2 GÓI DỊCH VỤ BẢO TRÌ & VẬN HÀNH KỸ THUẬT (SLA)                         │
├──────────────────────────────────────┬────────────────────────────────┬────────────────────────────────┤
│ TIÊU CHÍ SO SÁNH                     │ GÓI TIER 1: TIÊU CHUẨN (BASIC) │ GÓI TIER 2: NÂNG CAO (PRIORITY)│
├──────────────────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ 💵 **Phí Dịch vụ Hàng tháng**        │ **1.000.000 VNĐ / tháng**      │ **2.500.000 VNĐ / tháng**      │
│ 🏢 **Phạm vi Chi nhánh Áp dụng**     │ Trọn gói cho cả 3 Chi nhánh    │ Trọn gói cho cả 3 Chi nhánh    │
│ 🛡️ **Giám sát Uptime & Cảnh báo**    │ Giám sát tự động 24/7          │ Giám sát chủ động 24/7 + APM   │
│ 💾 **Sao lưu Dữ liệu (Backup DB)**   │ Tự động sao lưu 1 lần / ngày   │ Sao lưu 2 lần / ngày + Cold S3 │
│ ⏱️ **Thời gian Phản hồi Sự cố (SLA)**│ Trong vòng < 2 giờ làm việc    │ Trong vòng < 30 phút (24/7)    │
│ ☕ **Cập nhật Thực đơn Định kỳ**     │ Hỗ trợ đổi menu 1 lần / tháng  │ Không giới hạn số lần đổi menu │
│ 🧠 **Tối ưu Hóa Dữ liệu AI**         │ Tự động theo thuật toán        │ Tinh chỉnh Prompt & Rules AI   │
│ 🧑‍🏫 **Đào tạo Nhân viên Mới**       │ Cung cấp tài liệu & video      │ Đào tạo trực tiếp 1 buổi/quý   │
└──────────────────────────────────────┴────────────────────────────────┴────────────────────────────────┘
```

---

## 6. BẢNG TỔNG HỢP CHI PHÍ THEO QUY MÔ CHI NHÁNH (1, 3 VÀ 5 QUÁN)

| Khoản Mục Chi Phí (VNĐ / Tháng) | Mô Hình 1 Quán Thí Điểm | Mô Hình 3 Quán (Hiện Tại) | Mô Hình 5 Quán (Mở Rộng) |
|---|:---:|:---:|:---:|
| **1. Hạ tầng Máy chủ Cloud VPS & Domain** | 490.000 | 490.000 | 740.000 *(Nâng cấp 8 vCPU / 16GB)* |
| **2. Dịch vụ AI Gemini & API** | 50.000 | 150.000 | 250.000 |
| **3. Vật tư Tiêu hao (Giấy in nhiệt)** | 100.000 | 300.000 | 500.000 |
| **4. Gói Bảo trì Kỹ thuật Tiêu chuẩn (Tier 1)** | 600.000 | 1.000.000 | 1.500.000 |
| **TỔNG CHI PHÍ VẬN HÀNH / THÁNG** | **1.240.000 VNĐ** | **1.940.000 VNĐ** | **2.990.000 VNĐ** |
| **BÌNH QUÂN CHI PHÍ / QUÁN / THÁNG** | **1.240.000 VNĐ/quán** | **~646.000 VNĐ/quán** | **~598.000 VNĐ/quán** |

> **Nhận xét**: Càng mở rộng số lượng quán, chi phí vận hành bình quân trên từng quán càng giảm mạnh (từ 1.24 triệu xuống chỉ còn ~598 nghìn đồng/quán/tháng) nhờ tận dụng tối đa năng lực xử lý tập trung của máy chủ.

---

## 7. DỰ TOÁN NGÂN SÁCH DÒNG TIỀN VẬN HÀNH 12 THÁNG (1-YEAR CASH FLOW FORECAST)

Bảng tính dự toán dòng tiền vận hành cho **Chuỗi 3 Chi Nhánh** trong năm đầu tiên (Đã bao gồm ưu đãi 3 tháng bảo hành miễn phí):

| Tháng Vận Hành | Chi Phí Hạ Tầng & AI | Vật Tư Giấy In | Phí Bảo Trì Kỹ Thuật | Tổng Chi Phí Tháng (VNĐ) | Ghi Chú |
|:---:|:---:|:---:|:---:|:---:|---|
| **Tháng 1** | 640.000 | 300.000 | **0 VNĐ** | **940.000** | Tháng đầu tiên (Bảo hành miễn phí) |
| **Tháng 2** | 640.000 | 300.000 | **0 VNĐ** | **940.000** | Bảo hành miễn phí |
| **Tháng 3** | 640.000 | 300.000 | **0 VNĐ** | **940.000** | Bảo hành miễn phí |
| **Tháng 4** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Bắt đầu hợp đồng bảo trì Tier 1 |
| **Tháng 5** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Vận hành ổn định |
| **Tháng 6** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Vận hành ổn định |
| **Tháng 7** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Vận hành ổn định |
| **Tháng 8** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Vận hành ổn định |
| **Tháng 9** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Vận hành ổn định |
| **Tháng 10** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Vận hành ổn định |
| **Tháng 11** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Vận hành ổn định |
| **Tháng 12** | 640.000 | 300.000 | 1.000.000 | **1.940.000** | Tổng kết & Tối ưu hóa cuối năm |
| **TỔNG CỘNG 1 NĂM** | **7.680.000** | **3.600.000** | **9.000.000** | **20.280.000 VNĐ** | **Bình quân chỉ ~1.690.000 VNĐ / tháng cho cả 3 quán** |

---

## 8. CHIẾN LƯỢC TỐI ƯU HÓA CHI PHÍ & TỰ CÂN ĐỐI DÒNG TIỀN

Hệ thống Smart F&B OS được thiết kế để **Tự cân đối dòng tiền chi phí vận hành (Self-Funding)** thông qua nguồn doanh thu mới từ tính năng Đặt hàng Giao tận nơi (QR Delivery):

- **Bài toán Phí Giao Hàng Bù Đắp Chi Phí Vận Hành**:
  * Mỗi đơn hàng Delivery mang lại khoản phí ship cố định: **20.000 VNĐ / đơn**.
  * Chỉ cần toàn chuỗi phát sinh tối thiểu **97 đơn giao hàng / tháng** (tương đương chỉ **~1 đơn ship / ngày / quán**).
  * Doanh thu từ phí ship = `97 x 20.000 = 1.940.000 VNĐ / tháng` -> **Bù đắp 100% toàn bộ chi phí vận hành và bảo trì hàng tháng của cả 3 quán**.
- **Tiết kiệm Chi Phí Nhân Sự & Hao Hụt**:
  * Chuỗi tiết kiệm ròng từ **30.000.000 đến 37.000.000 VNĐ / tháng** nhờ cắt giảm lương thu ngân thừa và giảm hao hụt nguyên vật liệu.
  * Tỷ lệ chi phí vận hành phần mềm trên tổng số tiền tiết kiệm được chỉ chiếm **~5.2%**.
"""

with open(target, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {target} with size: {os.path.getsize(target)} bytes")
