# ❄️ HỆ THỐNG GIÁM SÁT THÔNG MINH KHO ĐÔNG LẠNH & CHUỖI VẬN CHUYỂN LẠNH

## 1. 📌 TÊN ĐỀ TÀI

> **Tiếng Việt:** "Hệ Thống Giám Sát Thông Minh Kho Đông Lạnh và Chuỗi Vận Chuyển Lạnh Sử Dụng IoT và Trí Tuệ Nhân Tạo"
>
> **Tiếng Anh:** "AI-Powered Smart Frozen Warehouse & Cold Chain Transport Monitoring System with IoT"

---

## 2. 🎯 BÀI TOÁN THỰC TẾ

### Hiện trạng tại VN — Vòng lặp nguy hiểm:
```
[Máy nén kho lạnh hỏng đột ngột]
       ↓
[Nhiệt độ kho tăng, không ai hay biết ngay]
       ↓
[Phát hiện khi nhân viên đi tuần hoặc khi hàng đã hỏng]
       ↓
[Thiệt hại lô hàng: hàng trăm triệu → hàng tỷ VNĐ]
       ↓
[Tranh chấp: Kho đổ lỗi xe tải, xe tải đổ lỗi kho nhận]
       ↓
[Không có bằng chứng số → kiện tụng kéo dài]
```

### NHÓM A — Vấn đề bên trong Kho Đông Lạnh:

| # | Vấn Đề | Hậu Quả |
|---|---|---|
| A1 | Máy nén hỏng đột ngột, không có cảnh báo sớm | Thiệt hại toàn bộ lô hàng (hàng chục tỷ VNĐ) |
| A2 | Không cân bằng nhiệt khi 1 máy lạnh bị lỗi | Zone nóng không đều, hàng hỏng cục bộ |
| A3 | Điện chạy 100% lúc vắng hàng, không tối ưu | Lãng phí 15–25% chi phí điện/tháng |
| A4 | Báo cáo thiết bị thủ công, không kịp thời | Kỹ thuật không biết đúng lúc, phản ứng chậm |
| A5 | Không rõ ai chịu trách nhiệm khi hàng hỏng trong kho | Tranh chấp với chủ hàng, mất uy tín |

### NHÓM B — Vấn đề chuỗi Vận Chuyển Container Lạnh:

| # | Vấn Đề | Hậu Quả |
|---|---|---|
| B1 | Không theo dõi nhiệt độ trong container khi di chuyển | Phát hiện hỏng khi giao hàng — quá trễ |
| B2 | Không có GPS tracking container đông lạnh | Không biết xe ở đâu, dừng bao lâu, đường nào |
| B3 | Bàn giao hàng không có bằng chứng số | Khi hàng hỏng: ai cũng đổ lỗi cho người khác |
| B4 | Tài xế tắt máy lạnh container khi tắc đường | Hàng hỏng, không ai biết |
| B5 | Không có lịch sử vận chuyển pháp lý | Không đáp ứng audit HACCP xuất khẩu |

---

## 3. 🏗️ KIẾN TRÚC HỆ THỐNG

```
┌──────────────────────────────────────────────────────────────┐
│         SMART COLD CHAIN MONITORING SYSTEM (SCCMS)          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  MODULE A: KHO ĐÔNG LẠNH       MODULE B: VẬN CHUYỂN         │
│  ┌───────────────────────┐     ┌─────────────────────────┐   │
│  │ ESP32 Nodes mỗi Zone: │     │ ESP32 + GPS trong cont: │   │
│  │ • DS18B20 Nhiệt độ    │     │ • NEO-6M GPS            │   │
│  │ • DHT22 Độ ẩm         │     │ • DS18B20 Temp          │   │
│  │ • PZEM-004T Điện      │     │ • 4G SIM card           │   │
│  │ • MPU-6050 Rung động  │     │ • LoRa backup           │   │
│  │ • Reed Switch cửa kho │     │ • MicroSD buffer log    │   │
│  │ • Relay điều khiển    │     │ • Pin LiPo + Solar      │   │
│  └─────────┬─────────────┘     └──────────┬──────────────┘   │
│            │ MQTT / WiFi                   │ 4G/LTE           │
│            ▼                              ▼                  │
│  ┌──────────────────────────────────────────────────────┐    │
│  │          EDGE LAYER (Raspberry Pi 5 tại kho)         │    │
│  │  • Local MQTT Broker (Mosquitto)                     │    │
│  │  • Anomaly Detection offline (AI)                    │    │
│  │  • Emergency SMS Alert (không cần internet)          │    │
│  │  • Buffer data khi mất kết nối cloud                 │    │
│  └──────────────────────┬───────────────────────────────┘    │
│                         │ HTTPS / MQTT                       │
│                         ▼                                    │
│  ┌──────────────────────────────────────────────────────┐    │
│  │                   CLOUD LAYER                        │    │
│  │  MQTT Broker (EMQX)  │  AI Engine (Python FastAPI)  │    │
│  │  InfluxDB (sensor TS)│  PostgreSQL (business data)  │    │
│  │  Redis (real-time)   │  Alert Engine (SMS/Zalo)     │    │
│  └──────────────────────┬───────────────────────────────┘    │
│                         │ REST API / WebSocket               │
│                         ▼                                    │
│  ┌──────────────────────────────────────────────────────┐    │
│  │              APPLICATION LAYER                       │    │
│  │  Web Dashboard  │  Mobile App  │  GPS Tracking Map  │    │
│  │  AI Reports     │  Alert Panel │  Compliance PDF    │    │
│  └──────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

---

## 4. 👥 CÁC ACTOR

| Actor | Chức Năng Chính |
|---|---|
| 🏭 **Quản Lý Kho** | Xem dashboard toàn kho, nhận alert khẩn, phê duyệt bảo trì |
| 🔧 **Kỹ Thuật Viên** | Nhận ticket bảo trì tự động, ghi nhận kết quả sửa chữa |
| 🚚 **Tài Xế / Giao Hàng** | Scan QR bàn giao hàng, xem nhiệt độ container trên app |
| 🏪 **Chủ Hàng / Khách Hàng** | Theo dõi lô hàng của mình, tra lịch sử nhiệt độ |
| 👨‍💼 **Giám Đốc / CEO** | Xem báo cáo tổng hợp, chi phí, hiệu suất toàn hệ thống |

---

## 5. 🤖 6 TÍNH NĂNG AI — CHI TIẾT

### AI #1: Phát Hiện Bất Thường Nhiệt Độ (Real-time Anomaly Detection)

**Kỹ thuật:** LSTM Autoencoder train trên 90 ngày dữ liệu lịch sử

**Phân biệt:**
- **Bình thường:** Mở cửa nhập hàng → tăng 2-3°C trong 10 phút → tự hồi phục
- **Nguy hiểm:** Máy nén hỏng → tăng liên tục, không dừng

**Kết quả mẫu:**
```
[23:47] ⚠️ CẢNH BÁO KHẨN — Kho Zone B
Nhiệt độ: -18.5°C → -14.2°C (trong 18 phút)
AI phân tích: Máy nén #2 ngừng hoạt động
Lô hàng bị ảnh hưởng: TH-0804-001 (Cá hồi, 2.5 tấn)
Thời gian an toàn còn lại: ~4.5 giờ
→ SMS đã gửi: KTV Minh (0901234567)
→ Zalo đã gửi: Quản lý Hùng
```

---

### AI #2: Dự Báo Lỗi Máy Lạnh (Predictive Failure Detection)

**Dữ liệu đầu vào:**

| Sensor | Tín Hiệu Cảnh Báo |
|---|---|
| PZEM-004T (Điện năng) | Tiêu thụ tăng 15–20% bất thường |
| MPU-6050 (Rung động) | Rung tần số cao → bearing mòn |
| DS18B20 (Nhiệt bề mặt máy) | Vỏ máy nóng bất thường |
| Pressure transducer (Áp suất) | Áp suất sụt → rò gas lạnh |

**Kỹ thuật:** Random Forest + rolling statistics 7 ngày

**Kết quả mẫu:**
```
📊 BÁO CÁO SỨC KHỎE THIẾT BỊ — 04/08/2025

Máy nén #1 (Zone A): ✅ BÌNH THƯỜNG (95% sức khỏe)
Máy nén #2 (Zone B): 🟡 CẦN THEO DÕI (67%)
  - Điện năng tăng 18% so với baseline
  - Rung động 45Hz tăng 30% trong 3 ngày
  - Xác suất hỏng trong 7 ngày: 62%
  - Khuyến nghị: Kiểm tra bearing, thêm dầu bôi trơn

Máy nén #3 (Zone C): 🔴 BẢO TRÌ KHẨN CẤP (34%)
  - Áp suất đầu đẩy giảm 22% — nguy cơ rò gas
  - Xác suất hỏng trong 3 ngày: 87%
  - Ticket #MT-2025-089 đã tạo tự động
```

---

### AI #3: Tự Động Cân Bằng Tải Lạnh (Thermal Load Balancing) ⭐

**Đây là tính năng kỹ thuật nhất — ít đồ án SE nào dám làm.**

**Kịch bản:** Kho 3 zone (A, B, C), mỗi zone 2 máy nén. Máy #2B đột ngột hỏng.

```
Trước sự cố:
Zone A: #1A (60%) + #1B (65%) → -20°C ✅
Zone B: #2A (60%) + #2B (60%) → -18°C ✅  ← #2B vừa hỏng!
Zone C: #3A (70%) + #3B (65%) → -22°C ✅

AI Load Balancing quyết định:
1. Tăng #2A: 60% → 85% (bù đắp trực tiếp)
2. Tăng #1B: 65% → 75% (hỗ trợ Zone B qua tường chia)
3. Điều chỉnh setpoint Zone B: -18°C → -17°C (biên rộng hơn)
4. Ước tính: "Duy trì ổn định Zone B ≥ 4.5 tiếng ở -17±1°C"
5. Sau 4 tiếng chưa sửa: Alert di chuyển hàng khỏi Zone B

Điều khiển phần cứng:
ESP32 → Relay Module → PWM → Biến tần máy nén
(Demo: ESP32 relay + DC fan mô phỏng, không cần phần cứng thật)
```

**Kỹ thuật:**
- PID Controller (software) điều chỉnh tốc độ motor
- Constraint Optimization (SciPy) phân bổ tải tối ưu

---

### AI #4: Báo Cáo Khẩn Cấp + Ticket Bảo Trì Tự Động

**Escalation flow:**
```
Phát hiện sự cố
  │
  ├─► Alert cấp 1 (ngay): SMS + Zalo → KTV trực ca
  │       Chờ 5 phút không phản hồi →
  │
  ├─► Alert cấp 2: SMS + Zalo → Trưởng phòng kỹ thuật
  │       Chờ 10 phút không phản hồi →
  │
  ├─► Alert cấp 3: SMS → Giám đốc + gọi điện tự động
  │
  ├─► Tạo Maintenance Ticket tự động:
  │     - Mã sự cố, thời gian, zone bị ảnh hưởng
  │     - Lịch sử thông số thiết bị 7 ngày qua
  │     - Đề xuất nguyên nhân từ AI
  │     - Danh sách lô hàng bị ảnh hưởng
  │
  └─► Thông báo chủ hàng tự động (Zalo/Email):
        "Lô hàng của quý công ty đang được bảo vệ.
         Sự cố phát hiện 23:47. Đội kỹ thuật đã được
         thông báo. Nhiệt độ: -16.8°C (an toàn đến -15°C).
         Cập nhật tiếp theo sau 30 phút."
```

---

### AI #5: Tối Ưu Điện Năng (Smart Energy Optimization)

**Chiến lược dựa trên giá điện EVN:**
```
Giờ thấp điểm (22h-06h): ~1,500 VNĐ/kWh
Giờ bình thường:          ~2,200 VNĐ/kWh
Giờ cao điểm (09h-11h, 17h-20h): ~2,900 VNĐ/kWh

AI Strategy:
• 22h-06h: Chạy full → kho lạnh xuống -23°C (dự trữ lạnh)
• 09h-11h: Giảm công suất → dùng "lạnh dự trữ"
• Ngưỡng: Chỉ chạy full khi nhiệt độ > -17°C

Kết quả tính toán (kho 150kW):
• Cũ: 150kW x 24h x 30 ngày x 2,200 VNĐ ≈ 238 triệu/tháng
• Mới: Shift sang giờ thấp điểm → ~185 triệu/tháng
• Tiết kiệm: ~53 triệu VNĐ/tháng
```

---

### AI #6: Chain of Custody — Phân Định Trách Nhiệm ⭐

**Luồng bàn giao hàng có bằng chứng số:**

```
ĐIỂM 1: Nhà sản xuất → Kho đông lạnh
• Thời gian: 08:00 ngày 04/08/2025
• Người bàn giao: Nguyễn Văn A (Cty Thủy sản ABC)
• Người nhận: Trần Thị B (Kho lạnh XYZ)
• Nhiệt độ tại bàn giao: -19.8°C ✅
• Xác nhận: Scan QR + OTP + Ký số
→ Từ đây, KHO LẠNH XYZ chịu trách nhiệm

ĐIỂM 2: Kho → Container vận chuyển
• Thời gian: 14:30 ngày 06/08/2025
• Bàn giao: Kho XYZ → Lái xe Lê Văn C (Cty LogiVN)
• Nhiệt độ: -20.1°C ✅ | Container: CONT-2025-00892
→ Từ đây, CÔNG TY LOGIVN chịu trách nhiệm

TRONG VẬN CHUYỂN (GPS + IoT tự động):
14:30 - Bình Dương:  -20.0°C ✅
17:00 - Long An:     -19.5°C ✅ (dừng tắc 45 phút)
20:30 - Tiền Giang:  -19.8°C ✅
02:15 - Cần Thơ:     ⚠️ -16.2°C — Alert tự động!
         → Gọi tài xế → "Máy lạnh container bị lỗi"
         → Alert Quản lý LogiVN + Chủ hàng ABC
03:00 - Dừng sửa: Reset máy lạnh container
04:30 - Tiếp tục:   -19.2°C ✅ Đã ổn định

ĐIỂM 3: Container → Kho nhận (Cần Thơ)
• Nhiệt độ bàn giao: -18.7°C
• ⚠️ Ghi chú: Sự cố 45 phút từ 02:15-03:00
• AI đánh giá: 96.3% hàng an toàn (tính theo MKT)
• Trách nhiệm sự cố: CÔNG TY LOGIVN
• PDF bằng chứng + chữ ký số: Tạo tự động
```

---

## 6. 📱 7 MODULE PHẦN MỀM

| Module | Tên | Chức Năng Chính |
|---|---|---|
| M1 | 🌡️ **Giám Sát Kho Real-time** | Dashboard đa zone, heatmap floor plan, time-series 5 năm |
| M2 | 🔧 **Quản Lý Thiết Bị & Bảo Trì** | Health dashboard, ticket tự động, lịch sử bảo trì |
| M3 | ⚡ **Điều Khiển & Tối Ưu Điện** | Setpoint từng zone, smart energy schedule, điều khiển từ xa |
| M4 | 📦 **Quản Lý Lô Hàng Trong Kho** | Nhập/xuất kho, gán zone, cảnh báo HSD |
| M5 | 🚚 **Theo Dõi Vận Chuyển** | GPS map real-time, temp log hành trình, alert container |
| M6 | 🔗 **Chain of Custody** | QR bàn giao, timeline phân định trách nhiệm, PDF bằng chứng |
| M7 | 📊 **Báo Cáo & Tuân Thủ** | HACCP auto-report, MKT calculator, audit trail 5 năm |

---

## 7. 🔩 PHẦN CỨNG IoT

### A — Tại Kho Đông Lạnh:

| Thiết Bị | Vai Trò | Giá Ước Tính |
|---|---|---|
| ESP32 WROOM-32 | MCU chính, thu sensor, gửi MQTT | ~150k VNĐ |
| DS18B20 (chống nước) | Đo nhiệt độ zone (-55 đến +125°C) | ~30k VNĐ |
| DHT22 | Nhiệt độ + độ ẩm backup | ~50k VNĐ |
| PZEM-004T | Đo điện năng máy nén (V, A, W, kWh) | ~150k VNĐ |
| MPU-6050 | Đo rung động motor bất thường | ~40k VNĐ |
| Magnetic Reed Switch | Cảm biến cửa kho mở/đóng | ~20k VNĐ |
| Relay 4 kênh | Điều khiển thiết bị (simulate) | ~60k VNĐ |
| LoRaWAN Gateway | Thu data nodes, gửi cloud (xuyên tường kho) | ~3M VNĐ |
| Raspberry Pi 5 | Edge server: offline AI + local MQTT | ~2M VNĐ |

### B — Trên Container Vận Chuyển:

| Thiết Bị | Vai Trò | Giá Ước Tính |
|---|---|---|
| ESP32 + SIM800L | MCU + kết nối 4G cellular | ~250k VNĐ |
| DS18B20 | Nhiệt độ trong container | ~30k VNĐ |
| NEO-6M GPS | Theo dõi vị trí real-time | ~120k VNĐ |
| LoRa SX1276 | Backup khi mất 4G | ~80k VNĐ |
| MicroSD + Reader | Buffer log offline | ~30k VNĐ |
| Pin LiPo 3.7V + Module solar | Nguồn điện độc lập | ~200k VNĐ |

---

## 8. 🛠️ TECH STACK

| Tầng | Công Nghệ |
|---|---|
| IoT Firmware | C/C++ (ESP-IDF framework) |
| Edge Computing | Python + Mosquitto MQTT (Raspberry Pi 5) |
| Backend API | Python FastAPI (async, high performance) |
| MQTT Cloud Broker | EMQX Cloud |
| Time-series Database | InfluxDB v2 |
| Business Database | PostgreSQL |
| Cache / Real-time | Redis + WebSocket |
| AI / ML | scikit-learn, XGBoost, PyTorch (LSTM) |
| Frontend Web | React.js + Recharts + Leaflet.js (map) |
| Mobile App | Flutter (iOS + Android) |
| Alert | Zalo OA API + Twilio SMS |
| Maps & GPS | Google Maps Platform |
| Deploy | Docker + AWS/GCP |

---

## 9. 📐 PHÂN CÔNG TEAM 4 NGƯỜI

| Sinh Viên | Vai Trò | Phụ Trách |
|---|---|---|
| **SV 1 — IoT & Backend Lead** | Phần cứng + hạ tầng | Lập trình ESP32 (sensor+relay+GPS), MQTT Broker, InfluxDB, API Gateway, WebSocket |
| **SV 2 — Frontend Lead** | Giao diện người dùng | Web Dashboard (chart+heatmap+map), Mobile App Flutter, Alert Panel |
| **SV 3 — AI Engineer** | Toàn bộ tính năng AI | Anomaly Detection, Predictive Maintenance, Load Balancing, Energy Optimizer |
| **SV 4 — Full-stack & DevOps** | Business logic | Chain of Custody, HACCP PDF, User/Multi-tenant, Docker deploy |

---

## 10. 📊 ROI ĐO LƯỜNG ĐƯỢC

| Chỉ Số | Trước | Sau | Cải Thiện |
|---|---|---|---|
| Phát hiện sự cố máy lạnh | 2-8 tiếng (khi tuần tra) | 30 giây | -99% |
| Dự báo máy hỏng | Không có | Trước 5-14 ngày | Hoàn toàn mới |
| Chi phí điện kho | 100% | 75-80% | Tiết kiệm 20-25% |
| Làm báo cáo HACCP | 4-8 tiếng/lô | 30 giây tự động | -99% |
| Tranh chấp bồi thường | Không bằng chứng | PDF chữ ký số đầy đủ | Giải quyết ngay |
| Thiệt hại hàng do hỏng máy | Toàn bộ lô (không biết kịp) | Giảm 70-80% (cảnh báo sớm) | -70-80% |

---

## 11. ✅ KẾT LUẬN

**6 lý do đề tài này đủ tốt cho đồ án KTPM:**

1. **Bài toán thật** — Kho đông lạnh + container lạnh đang là nhu cầu cấp thiết tại VN 2025
2. **Kỹ thuật đa dạng** — Có phần cứng IoT + AI + full-stack software (đủ cho 4 SV làm sâu)
3. **Demo ấn tượng** — Mô hình mini (tủ lạnh + ESP32 sensor) + GPS tracking thật trên bản đồ
4. **Tính năng độc đáo** — Tự động cân bằng tải lạnh + Chain of Custody chưa đồ án nào làm
5. **Giá trị kinh tế đo được** — Tiết kiệm điện 20-25%, tránh thiệt hại hàng trăm triệu VNĐ
6. **Mở rộng được** — Áp dụng cho dược phẩm, thủy sản xuất khẩu, chuỗi siêu thị

---
---

# 📝 PHÂN TÍCH CHI TIẾT — VẤN ĐỀ, HƯỚNG GIẢI QUYẾT, GIÁ TRỊ THỊ TRƯỜNG & ĐIỂM ĐỘC ĐÁO

---

## 12. 🔴 MÔ TẢ CÁC VẤN ĐỀ THỰC TẾ ĐANG TỒN TẠI

### Vấn đề 1: Giám sát nhiệt độ kho đông lạnh vẫn đang THỦ CÔNG

**Hiện trạng:** Phần lớn kho đông lạnh tại Việt Nam (đặc biệt kho vừa và nhỏ) vẫn sử dụng **data logger truyền thống** — thiết bị ghi nhiệt độ lên thẻ nhớ hoặc giấy, nhân viên phải đi tuần kiểm tra định kỳ mỗi 2-4 tiếng.

**Hậu quả cụ thể:**
- Nếu máy nén hỏng lúc **2 giờ sáng** (không có ai trực), đến 6 giờ sáng mới phát hiện → nhiệt độ đã tăng từ -20°C lên -5°C trong 4 tiếng → **toàn bộ lô hàng hỏng**.
- Một kho đông lạnh 500 tấn chứa thủy sản xuất khẩu, mỗi tấn ~50 triệu VNĐ → thiệt hại tiềm năng: **25 tỷ VNĐ** chỉ vì phát hiện chậm 4 tiếng.
- Data logger chỉ ghi log — **không gửi cảnh báo tự động**, không có ai nhận alert khi sự cố xảy ra ngoài giờ làm việc.

**Con số thực tế:** Theo Bộ NN&PTNT, 14% nông sản đông lạnh bị thất thoát mỗi năm do chuỗi lạnh đứt gãy. Thiệt hại ước tính hàng chục nghìn tỷ VNĐ/năm trên toàn quốc.

---

### Vấn đề 2: Thiết bị lạnh hỏng đột ngột — Không có dự báo

**Hiện trạng:** Máy nén lạnh (compressor), motor quạt dàn lạnh, van điện từ... đều được bảo trì theo **lịch cố định** (3 tháng/lần hoặc 6 tháng/lần) — bất kể thiết bị đang khỏe hay sắp hỏng.

**Hậu quả cụ thể:**
- Máy nén chạy bình thường hôm trước, hôm sau **hỏng đột ngột** không báo trước → dừng làm lạnh → nhiệt độ kho tăng nhanh.
- Bearing motor mòn dần nhưng **không ai biết** vì không có sensor rung động → đến khi motor kẹt cứng mới phát hiện.
- Chi phí sửa chữa khẩn cấp (reactive maintenance) **cao gấp 3-5 lần** so với bảo trì phòng ngừa có kế hoạch.
- Thời gian chờ phụ tùng thay thế: 1-3 ngày → trong thời gian đó kho không có lạnh hoặc lạnh không đủ.

**Thiệt hại kép:** Vừa mất tiền sửa máy (hàng chục triệu VNĐ), vừa mất hàng hóa (hàng trăm triệu đến hàng tỷ VNĐ).

---

### Vấn đề 3: Không cân bằng được nhiệt độ khi có sự cố

**Hiện trạng:** Khi 1 trong nhiều máy nén trong kho bị lỗi, các máy còn lại **vẫn chạy theo cài đặt cũ** — không tự động tăng công suất để bù đắp. Kết quả: zone bị mất máy nóng lên dần, các zone khác vẫn lạnh bình thường.

**Hậu quả cụ thể:**
- Kho có 3 zone nhưng zone B mất máy → zone B tăng nhiệt, hàng trong zone B hỏng dần, trong khi zone A và C vẫn dư lạnh.
- Nhân viên không biết cách điều chỉnh thủ công các máy khác để bù → phải chờ kỹ thuật viên đến (có thể 2-6 tiếng).
- Trong khoảng thời gian chờ đó, **hàng hóa trong zone bị ảnh hưởng đã hỏng một phần hoặc toàn bộ**.

---

### Vấn đề 4: Chi phí điện năng kho lạnh CỰC KỲ CAO — chạy không tối ưu

**Hiện trạng:** Kho đông lạnh là một trong những cơ sở tiêu thụ điện lớn nhất trong ngành logistics. Máy nén chạy **cùng công suất 24/7** bất kể:
- Giờ cao điểm hay thấp điểm (giá điện chênh gần 2 lần)
- Kho đang đầy hàng hay gần trống
- Trời nắng nóng 40°C hay mát mẻ 25°C

**Con số thực tế:**
- Kho đông lạnh 500 tấn tiêu thụ **50-150 triệu VNĐ tiền điện/tháng**.
- Nếu tối ưu theo giờ thấp điểm + load factor, có thể tiết kiệm **15-25% = 7.5 đến 37 triệu VNĐ/tháng**.
- Hầu hết kho tại VN **chưa có hệ thống tối ưu năng lượng tự động** — vẫn cài đặt cố định.

---

### Vấn đề 5: Mất kiểm soát hoàn toàn trong quá trình vận chuyển

**Hiện trạng:** Khi hàng đông lạnh được chuyển từ kho lên container/xe tải lạnh, nhà sản xuất và chủ kho **hoàn toàn mất kiểm soát**. Không biết:
- Container hiện đang ở đâu (không có GPS tracking)
- Nhiệt độ bên trong container là bao nhiêu (không có sensor gắn)
- Tài xế có tắt máy lạnh khi dừng nghỉ hay không

**Hậu quả cụ thể:**
- Hàng giao đến kho nhận, mở container ra → **hàng đã tan đá một phần**, chất lượng giảm.
- Không biết sự cố xảy ra ở đoạn nào: kho xuất? Trên xe? Kho nhận?
- Chỉ phát hiện khi đã giao hàng → **không thể can thiệp sớm**.

---

### Vấn đề 6: Tranh chấp trách nhiệm — Không có bằng chứng pháp lý

**Hiện trạng:** Đây là **vấn đề nhức nhối nhất** trong ngành cold chain tại VN. Khi hàng hỏng:
- **Kho xuất** nói: "Tôi giao hàng -20°C, đúng chuẩn."
- **Nhà vận chuyển** nói: "Tôi chở đúng nhiệt độ, hàng hỏng trước khi tôi nhận."
- **Kho nhận** nói: "Tôi nhận hàng đã tan đá, không phải lỗi tôi."

**Hậu quả:**
- Không ai có bằng chứng → **tranh chấp bồi thường kéo dài hàng tháng**.
- Mất uy tín với đối tác, khách hàng.
- Xuất khẩu sang EU/Nhật/Mỹ: **không đáp ứng yêu cầu audit HACCP** vì không có hồ sơ nhiệt độ đầy đủ → bị từ chối lô hàng tại cảng.

---

## 13. ✅ HƯỚNG GIẢI QUYẾT — HỆ THỐNG ĐỀ XUẤT

### Giải quyết Vấn đề 1 → Bằng IoT Real-time + AI Anomaly Detection

| Trước (Thủ công) | Sau (Hệ thống SCCMS) |
|---|---|
| Data logger ghi thẻ nhớ, check 2-4 tiếng/lần | ESP32 + DS18B20 đo nhiệt độ **mỗi 30 giây**, gửi MQTT lên cloud |
| Phát hiện sự cố khi đi tuần (2-8 tiếng sau) | AI Anomaly Detection phát hiện **trong 30 giây** → alert SMS/Zalo |
| Không phân biệt được mở cửa vs máy hỏng | LSTM Autoencoder **phân biệt pattern** bình thường vs nguy hiểm |
| Mất internet = mất giám sát | Raspberry Pi Edge chạy AI **offline** — vẫn alert qua SMS không cần internet |

**Kết quả:** Từ "phát hiện sau 2-8 tiếng" → "phát hiện trong 30 giây". Giảm thiệt hại từ 100% lô hàng → gần 0%.

---

### Giải quyết Vấn đề 2 → Bằng IoT Sensor Đa Kênh + AI Predictive Maintenance

| Trước (Reactive) | Sau (Predictive) |
|---|---|
| Bảo trì theo lịch cố định 3-6 tháng | AI phân tích dữ liệu sensor liên tục → dự báo trước **5-14 ngày** |
| Không biết máy nào sắp hỏng | Dashboard sức khỏe: % sức khỏe từng máy, xếp hạng rủi ro |
| Chi phí sửa chữa khẩn cấp cao gấp 3-5x | Bảo trì **đúng thời điểm** — tiết kiệm chi phí, không gián đoạn |
| Phụ tùng chờ 1-3 ngày | Dự báo sớm → **đặt phụ tùng trước**, sẵn sàng khi cần |

**IoT sensor cụ thể:**
- **PZEM-004T** đo điện năng → máy nén tiêu thụ tăng bất thường = dấu hiệu hiệu suất giảm
- **MPU-6050** đo rung động → tần số rung cao = bearing mòn, trục lệch
- **DS18B20** đo nhiệt bề mặt → vỏ máy nóng bất thường = quá tải hoặc thiếu gas lạnh

**Kết quả:** Giảm 70-80% sự cố hỏng đột ngột. Kéo dài tuổi thọ thiết bị 20-30%.

---

### Giải quyết Vấn đề 3 → Bằng AI Thermal Load Balancing + Điều Khiển Relay

| Trước (Không có) | Sau (Tự động cân bằng) |
|---|---|
| Máy hỏng → zone đó mất lạnh hoàn toàn | AI **tự động tăng công suất** các máy còn lại để bù |
| Chờ kỹ thuật viên 2-6 tiếng | Hệ thống **ổn định tức thì** trong vòng phút, mua thời gian chờ sửa |
| Hàng trong zone hỏng bị thiệt hại | Duy trì nhiệt độ an toàn **thêm 4-6 tiếng** — đủ thời gian sửa chữa |
| Không biết khi nào cần di chuyển hàng | AI ước tính chính xác: "Còn giữ được X tiếng" → quyết định kịp thời |

**Cách implement:**
- ESP32 giao tiếp với relay module → điều khiển tốc độ quạt/biến tần máy nén
- PID Controller (phần mềm) tính toán công suất tối ưu cho từng máy
- Constraint Optimization (SciPy) đảm bảo không quá tải máy nào quá mức an toàn

**Kết quả:** Tránh thiệt hại hàng hóa trong 80-90% trường hợp sự cố 1 máy — feature mà **chưa đồ án nào tại VN từng làm**.

---

### Giải quyết Vấn đề 4 → Bằng AI Smart Energy Optimization

| Trước (Cố định 24/7) | Sau (AI tối ưu) |
|---|---|
| Máy nén chạy cùng công suất mọi lúc | AI **shift tải sang giờ thấp điểm** (22h-06h) — giá điện rẻ hơn gần 2x |
| Không biết kho đang dư lạnh hay thiếu lạnh | Sensor nhiệt độ + AI phân tích → chỉ chạy khi CẦN |
| Tiền điện 100% (baseline) | Tiết kiệm **15-25%** mỗi tháng |

**Chiến lược cụ thể:**
- **Pre-cooling:** Giờ thấp điểm (22h-06h, giá ~1,500 VNĐ/kWh) → chạy full power, kho lạnh xuống -23°C
- **Coast period:** Giờ cao điểm (09h-11h, 17h-20h, giá ~2,900 VNĐ/kWh) → giảm công suất, dùng "lạnh dự trữ"
- **Smart threshold:** Chỉ chạy lại khi nhiệt độ vượt -17°C (đảm bảo hàng vẫn an toàn)

**Kết quả:** Kho 150kW tiết kiệm ~40-53 triệu VNĐ/tháng. ROI phần cứng IoT thu hồi trong 2-4 tháng.

---

### Giải quyết Vấn đề 5 → Bằng IoT GPS + 4G Logger Trên Container

| Trước (Mù hoàn toàn) | Sau (Real-time tracking) |
|---|---|
| Không biết xe ở đâu | GPS **real-time trên bản đồ**, cập nhật mỗi 30 giây |
| Không biết nhiệt độ trong container | DS18B20 đo **nhiệt độ liên tục**, log lên cloud qua 4G |
| Tài xế tắt máy lạnh khi dừng → không ai biết | Alert **tự động ngay lập tức** khi nhiệt độ container tăng bất thường |
| Phát hiện khi giao hàng → quá muộn | Phát hiện **trong lúc di chuyển** → có thể can thiệp (gọi tài xế, điều xe khác) |

**Điểm đặc biệt:**
- Khi mất sóng 4G (đường hầm, vùng sâu): **LoRa backup** gửi data nếu gần gateway, hoặc **MicroSD buffer** lưu offline → sync khi có sóng lại
- Nguồn điện độc lập: **Pin LiPo + Solar** → không phụ thuộc vào điện xe, vẫn hoạt động khi xe tắt máy

---

### Giải quyết Vấn đề 6 → Bằng Chain of Custody + Digital Proof

| Trước (Đổ lỗi vòng tròn) | Sau (Bằng chứng số minh bạch) |
|---|---|
| Không ai có bằng chứng | Mỗi điểm bàn giao: **QR scan + GPS + Nhiệt độ + Chữ ký số** |
| Tranh chấp kéo dài hàng tháng | Timeline tự động: "Đoạn X do ABC chịu trách nhiệm" → **giải quyết ngay** |
| Không đáp ứng audit HACCP | **PDF bằng chứng tự động** với log nhiệt độ từng phút → audit ready |
| Xuất khẩu bị từ chối | Đủ hồ sơ GDP/HACCP → **vượt qua kiểm toán EU/Nhật/Mỹ** |

**Cách hoạt động:**
- Tại mỗi điểm bàn giao (kho → xe, xe → kho nhận): người nhận **scan QR lô hàng** → hệ thống tự động ghi nhận: ai, lúc nào, ở đâu (GPS), nhiệt độ bao nhiêu
- Từ thời điểm scan: **người nhận chính thức chịu trách nhiệm**
- Toàn bộ data được hash → blockchain-anchored → **không thể sửa đổi hoặc giả mạo**
- Khi có tranh chấp: xuất **PDF 1 click** với toàn bộ timeline + bằng chứng → kết thúc tranh cãi

---

## 14. 🏪 DỰ ÁN GIẢI QUYẾT ĐƯỢC NHỮNG VẤN ĐỀ GÌ CHO THỊ TRƯỜNG?

### 14.1 Đối với Doanh nghiệp Kho đông lạnh (Cold Storage Operators)

| Giá trị mang lại | Đo lường được |
|---|---|
| Giảm thiệt hại hàng hóa do sự cố thiết bị | Từ "mất 100% lô khi hỏng máy" → "giảm 70-80% nhờ cảnh báo sớm" |
| Tiết kiệm chi phí điện năng | 15-25% mỗi tháng (= 7.5 - 37 triệu VNĐ/tháng cho kho 500 tấn) |
| Giảm chi phí bảo trì thiết bị | Bảo trì đúng lúc rẻ hơn 3-5 lần so với sửa chữa khẩn cấp |
| Tăng uptime (thời gian hoạt động) | Giảm 70% downtime ngoài kế hoạch |
| Chứng minh chất lượng với khách hàng B2B | Dashboard + PDF nhiệt độ real-time → tăng uy tín, dễ ký hợp đồng mới |

### 14.2 Đối với Doanh nghiệp Vận chuyển lạnh (Cold Chain Logistics)

| Giá trị mang lại | Đo lường được |
|---|---|
| Giám sát đội xe container lạnh | GPS + Temp real-time → biết chính xác xe ở đâu, nhiệt độ bao nhiêu |
| Giảm rủi ro pháp lý | Chain of Custody → có bằng chứng rõ ràng ai chịu trách nhiệm |
| Phản ứng nhanh khi có sự cố | Alert 30 giây → gọi tài xế xử lý ngay, không chờ giao hàng |
| Tối ưu lộ trình giao hàng | AI route optimization → giảm 20% thời gian giao hàng |

### 14.3 Đối với Nhà sản xuất / Xuất khẩu thực phẩm

| Giá trị mang lại | Đo lường được |
|---|---|
| Theo dõi lô hàng từ kho đến nơi nhận | Timeline nhiệt độ toàn hành trình — minh bạch 100% |
| Đáp ứng yêu cầu xuất khẩu HACCP/GDP | Báo cáo tự động 30 giây thay vì 4-8 tiếng thủ công |
| Bảo vệ thương hiệu | Không để hàng kém chất lượng ra thị trường |
| Giảm tranh chấp với nhà vận chuyển | Bằng chứng số → giải quyết trong 1 ngày thay vì 1 tháng |

### 14.4 Thị trường tiềm năng tại Việt Nam (2025)

| Phân khúc | Quy mô ước tính | Nhu cầu |
|---|---|---|
| Thủy sản xuất khẩu (cá, tôm) | $8.9 tỷ USD kim ngạch XK | Bắt buộc có HACCP audit trail cho EU/Nhật |
| Dược phẩm (vaccine, sinh phẩm) | $1.2 tỷ USD | GDP/GSP bắt buộc, yêu cầu log nhiệt 2-8°C |
| Sữa & sản phẩm sữa | 6.4 tỷ lít/năm | Chuỗi lạnh 2-6°C liên tục, nhiều điểm bàn giao |
| Thịt chế biến, thực phẩm đông lạnh | Tăng trưởng 15%/năm | Nhu cầu cold chain logistics tăng mạnh |
| Chuỗi siêu thị (WinMart, BigC, Bách Hóa Xanh) | Hàng nghìn điểm bán | Cần giám sát tủ đông/tủ mát tại mỗi cửa hàng |

---

## 15. 🤖 AI ỨNG DỤNG NHƯ THẾ NÀO — CHI TIẾT KỸ THUẬT

### 15.1 Bảng Tổng Hợp 6 Tính Năng AI

| # | Tên AI Feature | Bài Toán Giải Quyết | Model/Thuật Toán | Dữ Liệu Đầu Vào (từ IoT) | Kết Quả Đầu Ra |
|---|---|---|---|---|---|
| AI-1 | Anomaly Detection | Phát hiện nhiệt độ tăng bất thường | LSTM Autoencoder + Isolation Forest | DS18B20 (nhiệt độ mỗi 30 giây) | Alert trong 30 giây + phân loại nguyên nhân |
| AI-2 | Predictive Maintenance | Dự báo máy nén sắp hỏng | Random Forest + Rolling Feature Engineering | PZEM-004T (điện) + MPU-6050 (rung) + DS18B20 (nhiệt bề mặt) | % xác suất hỏng trong 3/7/14 ngày + khuyến nghị |
| AI-3 | Thermal Load Balancing | Cân bằng nhiệt khi 1 máy lỗi | PID Controller + Constraint Optimization | Nhiệt độ từng zone + công suất từng máy | Lệnh điều khiển: máy X tăng Y%, ước tính thời gian ổn định |
| AI-4 | Smart Energy | Tối ưu chi phí điện | Reinforcement Learning (Q-Learning) | Nhiệt độ kho + giá điện EVN + lượng hàng | Lịch chạy máy tối ưu → tiết kiệm 15-25%/tháng |
| AI-5 | Compliance Report AI | Tự động tạo báo cáo HACCP/GDP | LLM (Gemini Flash) + Structured Templates | Toàn bộ log nhiệt độ + thông tin lô hàng | PDF report 30 giây thay vì 4-8 tiếng |
| AI-6 | Route Optimization | Tối ưu lộ trình giao container | Graph Neural Network + CSP | GPS position + Time-to-Spoilage + traffic data | Thứ tự giao tối ưu → giảm 20% thời gian |

### 15.2 AI Chạy Ở Đâu? — Edge vs Cloud

```
┌──────────────────────────────────────────────────────────────┐
│           AI DEPLOYMENT STRATEGY                              │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  🏠 TẠI EDGE (Raspberry Pi 5 — tại kho)                       │
│  ├── AI-1: Anomaly Detection (lightweight LSTM)               │
│  │   → Vì: CẦN phản ứng trong 30 giây, kể cả mất internet  │
│  ├── AI-3: Load Balancing (PID Controller)                    │
│  │   → Vì: CẦN điều khiển relay tức thì, không chờ cloud    │
│  └── Alert Engine: SMS qua GSM module, không cần internet    │
│                                                                │
│  ☁️ TẠI CLOUD (AWS/GCP — Server)                              │
│  ├── AI-2: Predictive Maintenance (model nặng hơn, batch)    │
│  │   → Vì: Phân tích 7 ngày data, chạy 1 lần/ngày          │
│  ├── AI-4: Smart Energy (RL training cần GPU)                │
│  │   → Vì: Training model cần tài nguyên lớn                │
│  ├── AI-5: Compliance Report (LLM API call)                  │
│  │   → Vì: Gọi Gemini Flash API, cần internet               │
│  └── AI-6: Route Optimization (GNN + Maps API)               │
│      → Vì: Cần data GPS toàn đội xe + Google Maps           │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

**Điểm quan trọng:** AI-1 (Anomaly Detection) và AI-3 (Load Balancing) **BẮT BUỘC chạy tại Edge** — vì kho lạnh ở vùng công nghiệp có thể **mất internet**, nhưng vẫn phải phát hiện sự cố và điều khiển thiết bị tự động. Đây là điểm khác biệt so với các giải pháp cloud-only.

---

## 16. 📡 IoT ỨNG DỤNG NHƯ THẾ NÀO — LUỒNG DỮ LIỆU

### 16.1 Tại Kho Đông Lạnh — Luồng IoT Data

```
[DS18B20] Nhiệt độ zone ────┐
[DHT22]   Độ ẩm zone ───────┤
[PZEM-004T] Điện năng máy nén┤
[MPU-6050]  Rung động motor ──┼──► [ESP32 Node] ──MQTT──► [Raspberry Pi 5]
[Reed Switch] Cửa kho mở/đóng┤                            │ (Edge Server)
[Relay Module] Điều khiển ────┘                            │
                                                            ├──► Local MQTT Broker
                                                            ├──► AI Anomaly Detection
                                                            ├──► PID Load Balancing
                                                            ├──► Emergency SMS (GSM)
                                                            │
                                                            └──HTTPS──► [Cloud]
                                                                         ├── EMQX MQTT
                                                                         ├── InfluxDB
                                                                         ├── AI Engine
                                                                         └── Web/App
```

**Tần suất gửi data:**
- Nhiệt độ: mỗi **30 giây** (real-time critical)
- Điện năng: mỗi **1 phút** (trend monitoring)
- Rung động: mỗi **5 phút** (predictive analysis)
- Cửa kho: **event-driven** (chỉ gửi khi thay đổi trạng thái)

### 16.2 Trên Container Vận Chuyển — Luồng IoT Data

```
[DS18B20] Nhiệt độ ──────┐
[NEO-6M GPS] Vị trí ──────┼──► [ESP32 + SIM800L] ──4G──► [Cloud MQTT]
[MicroSD] Buffer offline ──┘        │                         │
                                     │                         ├── InfluxDB
                                     └── LoRa backup ──► Gateway  ├── GPS Map
                                                                   └── Alert Engine
```

**Chế độ gửi data:**
- Bình thường: mỗi **5 phút** (tiết kiệm pin + data SIM)
- Khi nhiệt độ vượt ngưỡng: chuyển sang **mỗi 30 giây** (chế độ khẩn cấp)
- Mất 4G: log vào MicroSD → sync khi có sóng lại (không mất data)

---

## 17. 🏆 ĐIỂM ĐỘC ĐÁO — TẠI SAO ĐỀ TÀI NÀY KHÁC BIỆT?

### So với Data Logger truyền thống (giải pháp phổ biến hiện tại tại VN)

| Tiêu chí | Data Logger truyền thống | Hệ thống SCCMS đề xuất |
|---|---|---|
| Giám sát | Ghi log, xem sau | **Real-time 24/7**, alert trong 30 giây |
| AI/Dự báo | ❌ Không có | ✅ 6 tính năng AI: anomaly, predict, balance, energy, report, route |
| Vận chuyển | ❌ Không theo dõi | ✅ GPS + Temp tracking container toàn hành trình |
| Tự động xử lý | ❌ Phụ thuộc con người | ✅ Tự cân bằng tải lạnh + tự tạo ticket bảo trì |
| Bằng chứng pháp lý | ❌ File Excel, dễ sửa | ✅ Blockchain-anchored, chữ ký số, không giả mạo được |
| Chi phí vận hành | Cao (điện lãng phí) | **Tiết kiệm 15-25% điện** nhờ AI |

### So với các giải pháp IoT cold chain quốc tế (Controlant, Sensitech, Emerson)

| Tiêu chí | Giải pháp quốc tế | SCCMS (đề tài) |
|---|---|---|
| Giá triển khai | **$50,000 - $200,000+** | Demo với ESP32 + Raspberry Pi < **10 triệu VNĐ** |
| Ngôn ngữ / UX | Tiếng Anh, giao diện phức tạp | **Tiếng Việt**, UX đơn giản cho thị trường VN |
| Tích hợp Zalo/MoMo | ❌ Không có | ✅ Alert qua **Zalo OA**, thanh toán VietQR |
| Tự động cân bằng tải | ❌ Hầu hết chỉ monitor | ✅ **Tự động cân bằng** + điều khiển relay |
| Tuân thủ VN | Không hỗ trợ luật VN | ✅ Hóa đơn điện tử VN, báo cáo tiếng Việt |

### 5 Điểm Độc Đáo Mà Chưa Đồ Án KTPM Nào Tại VN Từng Làm

1. **🧊 Tự động cân bằng tải lạnh (Thermal Load Balancing)**
   - Khi 1 máy hỏng → AI tự động điều phối các máy còn lại để giữ ổn định toàn kho
   - Kết hợp PID Controller + Constraint Optimization — kỹ thuật của hệ thống công nghiệp thực
   - **Demo thật được:** ESP32 relay + DC fan mô phỏng máy nén trên mô hình kho mini

2. **🔗 Chain of Custody — Phân định trách nhiệm bằng bằng chứng số**
   - Scan QR + GPS + Nhiệt độ + Chữ ký số tại mỗi điểm bàn giao
   - Timeline tự động: "Từ 14:30 đến 08:00 hôm sau: Công ty LogiVN chịu trách nhiệm"
   - PDF bằng chứng pháp lý xuất 1 click — **giải quyết vấn đề nhức nhối nhất** của ngành

3. **🧠 AI chạy tại Edge (Offline) — Không phụ thuộc internet**
   - Raspberry Pi 5 tại kho chạy AI anomaly detection + PID load balancing offline
   - Khi mất internet: vẫn phát hiện sự cố, vẫn cân bằng tải lạnh, vẫn gửi SMS qua GSM module
   - Hầu hết đồ án khác **hoàn toàn phụ thuộc cloud** → mất mạng = mất giám sát

4. **⚡ AI tối ưu điện năng dựa trên giá điện EVN thực tế**
   - Không chỉ "giám sát điện" — mà **AI tự động shift tải** sang giờ thấp điểm để tiết kiệm
   - Sử dụng Reinforcement Learning học pattern tối ưu theo mùa, thời tiết, lượng hàng
   - **Kết quả đo lường được:** Tiết kiệm 15-25% chi phí điện/tháng — ROI rõ ràng

5. **🚚 IoT GPS Logger container với chế độ failover 3 lớp**
   - Lớp 1: 4G LTE (bình thường) → Lớp 2: LoRa (mất 4G) → Lớp 3: MicroSD offline (mất tất cả)
   - Đảm bảo **không bao giờ mất data** — dù container đi qua vùng không có sóng
   - Pin LiPo + Solar → hoạt động độc lập, không phụ thuộc điện xe

---

## 18. 📊 BẢNG TỔNG HỢP: VẤN ĐỀ → GIẢI PHÁP → CÔNG NGHỆ

| Vấn Đề | Giải Pháp | IoT | AI | Kết Quả |
|---|---|---|---|---|
| Giám sát thủ công, chậm | Real-time monitoring | ESP32 + DS18B20 + MQTT | LSTM Anomaly Detection | Phát hiện 30 giây thay vì 2-8 tiếng |
| Máy lạnh hỏng đột ngột | Predictive Maintenance | PZEM-004T + MPU-6050 | Random Forest | Dự báo trước 5-14 ngày |
| Không cân bằng khi sự cố | Auto Load Balancing | ESP32 Relay + PWM | PID + Constraint Optimization | Giữ ổn định kho 4-6 tiếng chờ sửa |
| Điện cao, không tối ưu | Smart Energy | PZEM-004T đo kWh | Reinforcement Learning | Tiết kiệm 15-25% điện/tháng |
| Mất kiểm soát vận chuyển | GPS + Temp Tracking | ESP32 + GPS + 4G + LoRa | Route Optimization (GNN) | Theo dõi real-time toàn hành trình |
| Không có bằng chứng | Chain of Custody | QR Scan + GPS lock | LLM Report Generation | PDF bằng chứng pháp lý 1 click |

---

> **Tóm lại:** Đề tài này không phải "1 app đơn lẻ" — mà là **hệ thống hoàn chỉnh** kết hợp phần cứng IoT thật (ESP32, sensor, relay, GPS) + 6 tính năng AI đa dạng (từ anomaly detection đến LLM report) + phần mềm full-stack (web dashboard, mobile app, alert engine). Giải quyết **6 vấn đề thực tế, đo lường được** của ngành kho đông lạnh và vận chuyển lạnh tại Việt Nam — với ROI rõ ràng cho doanh nghiệp.
