# ☕ HỆ THỐNG QUẢN LÝ VẬN HÀNH CHUỖI 3 QUÁN CÀ PHÊ
## F&B Operating System — Tài Liệu Tổng Quan Hệ Thống Dành Cho Khách Hàng

> **Phiên bản:** 1.0 — Tháng 08/2026
>
> **Đối tượng đọc:** Chủ chuỗi cà phê, Quản lý chi nhánh, Nhà đầu tư
>
> **Mục đích:** Mô tả toàn bộ hệ thống quản lý vận hành cho chuỗi 3 quán cà phê — bao gồm cách hoạt động, ai sử dụng, luồng công việc hàng ngày, và thiết bị cần thiết.

---

# 📚 MỤC LỤC

| # | Nội Dung |
|---|---|
| **I** | Tổng Quan Hệ Thống — Nhìn Toàn Cảnh |
| **II** | Sơ Đồ Kiến Trúc Hệ Thống |
| **III** | Phân Quyền Người Dùng — Ai Dùng Gì? |
| **IV** | 8 Module Chức Năng Chi Tiết |
| **V** | Luồng Vận Hành Hàng Ngày (Quy Trình Thực Tế) |
| **VI** | Thiết Bị & Trang Bị Cho Mỗi Quán |
| **VII** | Dashboard Chủ Chuỗi — Quản Lý 3 Quán Từ 1 Màn Hình |
| **VIII** | Lộ Trình Triển Khai (Timeline) |

---
---

# I. TỔNG QUAN HỆ THỐNG — NHÌN TOÀN CẢNH

## 1.1 Hệ Thống Này Là Gì?

F&B Operating System (F&B OS) là **nền tảng quản lý vận hành toàn diện** cho chuỗi quán cà phê, bao gồm:

- **Bán hàng & Thanh toán** (POS — Point of Sale)
- **Quản lý nhân sự & Chấm công** (HRM)
- **Quản lý nguyên liệu & Kho** (Inventory)
- **Quản lý khách hàng & Tích điểm** (CRM & Loyalty)
- **Quản lý tài chính & Báo cáo tự động** (Finance & EOD Report)
- **Quản lý thực đơn & Giá** (Menu Management)
- **Màn hình pha chế / Bếp** (KDS — Kitchen Display System)
- **AI phân tích & Đề xuất tối ưu** (AI Engine)

## 1.2 Quy Mô Triển Khai

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CHỦ CHUỖI (OWNER / CEO)                        │
│              Dashboard tổng — Quản lý 3 quán từ 1 nơi             │
│                    📱 App + 💻 Web Dashboard                       │
└──────────────────────┬──────────────────────────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
    ┌────▼────┐   ┌────▼────┐   ┌────▼────┐
    │  QUÁN 1  │   │  QUÁN 2  │   │  QUÁN 3  │
    │ (Quận 1) │   │ (Quận 3) │   │ (Thủ Đức)│
    │          │   │          │   │          │
    │ 1 QL     │   │ 1 QL     │   │ 1 QL     │
    │ 2 TN     │   │ 2 TN     │   │ 2 TN     │
    │ 3 Barista│   │ 3 Barista│   │ 3 Barista│
    └──────────┘   └──────────┘   └──────────┘
```

| Thông Số | Giá Trị |
|---|---|
| Số chi nhánh | **3 quán** |
| Tổng nhân viên dự kiến | **18-24 người** (6-8 người/quán) |
| Số tài khoản hệ thống | **~25 tài khoản** (1 Owner + 3 Manager + 6 Thu ngân + 9 Barista + dự phòng) |
| Quản lý tập trung | **1 Dashboard duy nhất** cho chủ chuỗi |
| Dữ liệu | **Đồng bộ real-time** giữa 3 quán qua Cloud |

---
---

# II. SƠ ĐỒ KIẾN TRÚC HỆ THỐNG

## 2.1 Kiến Trúc Tổng Thể (4 Tầng)

```
╔══════════════════════════════════════════════════════════════════════════╗
║  TẦNG 1: THIẾT BỊ TẠI QUÁN (Tại mỗi chi nhánh)                       ║
║  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     ║
║  │ Tablet   │ │ Màn hình │ │ Máy in   │ │ QR Code  │ │ Máy quét │     ║
║  │ POS      │ │ KDS Bếp  │ │ Bill     │ │ Feedback │ │ Barcode  │     ║
║  │ (bán hàng│ │ (pha chế)│ │ (hóa đơn)│ │ (tại bàn)│ │ (kho)    │     ║
║  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘     ║
║       └────────────┬┴───────────┬┴────────────┘            │           ║
╠════════════════════╪═══════════╪═══════════════════════════╪═══════════╣
║  TẦNG 2: MẠNG & KẾT NỐI       │                           │           ║
║  ┌─────────────────▼───────────▼───────────────────────────▼─────┐     ║
║  │              WiFi quán → Internet → HTTPS/API                 │     ║
║  └─────────────────────────────┬─────────────────────────────────┘     ║
╠═══════════════════════════════╪═══════════════════════════════════════╣
║  TẦNG 3: CLOUD SERVER (Trung tâm xử lý)                              ║
║  ┌─────────────┐ ┌──────────────┐ ┌───────────────┐ ┌────────────┐   ║
║  │ API Server  │ │ Database     │ │ AI Engine     │ │ Noti Server│   ║
║  │ (xử lý     │ │ (lưu toàn bộ│ │ (phân tích &  │ │ (gửi thông│   ║
║  │  nghiệp vụ)│ │  dữ liệu)   │ │  dự báo)      │ │  báo Zalo) │   ║
║  └─────────────┘ └──────────────┘ └───────────────┘ └────────────┘   ║
╠═══════════════════════════════════════════════════════════════════════╣
║  TẦNG 4: GIAO DIỆN NGƯỜI DÙNG                                        ║
║  ┌────────────┐ ┌──────────────┐ ┌──────────────────┐                 ║
║  │ 📱 App     │ │ 💻 Web       │ │ 🧾 Zalo OA       │                 ║
║  │ Manager    │ │ Dashboard    │ │ Thông báo tự động│                 ║
║  │ (QL + Chủ) │ │ (Chủ chuỗi) │ │ (Nhân viên + KH) │                 ║
║  └────────────┘ └──────────────┘ └──────────────────┘                 ║
╚═══════════════════════════════════════════════════════════════════════╝
```

## 2.2 Luồng Dữ Liệu Giữa 3 Quán

```
   QUÁN 1 (Quận 1)          QUÁN 2 (Quận 3)          QUÁN 3 (Thủ Đức)
   ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
   │ POS + KDS    │          │ POS + KDS    │          │ POS + KDS    │
   │ Kho riêng    │          │ Kho riêng    │          │ Kho riêng    │
   │ NV riêng     │          │ NV riêng     │          │ NV riêng     │
   └──────┬───────┘          └──────┬───────┘          └──────┬───────┘
          │ Real-time                │ Real-time                │ Real-time
          └──────────────────┬───────┴──────────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  ☁️ CLOUD SERVER │
                    │  Database chung  │
                    │  AI Engine chung │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ 📊 DASHBOARD    │
                    │ CHỦ CHUỖI       │
                    │ (Xem cả 3 quán) │
                    └─────────────────┘
```

**Nguyên tắc:**
- Mỗi quán có **kho riêng, nhân viên riêng, doanh thu riêng** — nhưng tất cả đều đổ về **1 cơ sở dữ liệu tập trung** trên Cloud.
- Chủ chuỗi ngồi bất kỳ đâu đều xem được **tất cả** — không cần chạy tới từng quán.
- Menu, giá bán, chương trình khuyến mãi có thể **đồng bộ cả chuỗi** hoặc **tùy chỉnh riêng từng quán**.

---
---

# III. PHÂN QUYỀN NGƯỜI DÙNG — AI DÙNG GÌ?

## 3.1 Bảng Phân Quyền Chi Tiết

| Vai Trò | Số Lượng | Thiết Bị Sử Dụng | Chức Năng Được Phép | Chức Năng BỊ KHÓA |
|---|---|---|---|---|
| **👑 Chủ Chuỗi (Owner)** | 1 người | 💻 Web Dashboard + 📱 App | ✅ XEM TẤT CẢ: Doanh thu 3 quán, tài chính, kho, nhân sự, AI báo cáo. ✅ DUYỆT: Nhập kho lớn, thay đổi giá, thêm/bớt menu, tuyển/sa thải. ✅ CẤU HÌNH: Phân quyền, thiết lập quy tắc. | Không bị khóa gì |
| **🏪 Quản Lý Chi Nhánh (Manager)** | 3 người (1/quán) | 📱 App Manager + 💻 Web (giới hạn) | ✅ XEM: Doanh thu, kho, nhân viên **của quán mình**. ✅ THAO TÁC: Xuất kho quầy, kiểm kê, duyệt ca, đối soát két tiền cuối ca. ✅ NHẬN: Báo cáo EOD tự động. | ❌ Không xem quán khác. ❌ Không đổi giá/menu. ❌ Không xem tài chính tổng chuỗi. |
| **💳 Thu Ngân (Cashier)** | 6 người (2/quán) | 🖥️ Tablet POS | ✅ THAO TÁC: Tạo đơn hàng, nhận thanh toán (tiền mặt / QR), in bill, áp voucher. ✅ XEM: Danh sách đơn hàng trong ca của mình. | ❌ Không xem doanh thu tổng. ❌ Không truy cập kho. ❌ Không sửa/xóa đơn đã thanh toán. |
| **🧋 Barista / Pha Chế** | 9 người (3/quán) | 📺 Màn hình KDS | ✅ XEM: Danh sách đơn cần pha, công thức chuẩn từng ly, thứ tự ưu tiên. ✅ THAO TÁC: Bấm "Hoàn thành" khi pha xong. | ❌ Không truy cập bất kỳ chức năng nào khác. |
| **👤 Khách Hàng** | Không giới hạn | 📱 Điện thoại cá nhân | ✅ Scan QR tích điểm Loyalty. ✅ Gửi Feedback đánh giá chất lượng. ✅ Nhận voucher qua Zalo. | ❌ Không cần tải app. Mọi thứ qua QR + Zalo. |

## 3.2 Sơ Đồ Phân Quyền Trực Quan

```
                          👑 CHỦ CHUỖI
                    ┌─────────┼─────────┐
              Toàn quyền  Toàn quyền  Toàn quyền
                    │         │         │
               🏪 QL Q1   🏪 QL Q3   🏪 QL TĐ
               ┌───┴───┐  ┌───┴───┐  ┌───┴───┐
              💳    🧋  💳    🧋  💳    🧋
             TN  Barista TN  Barista TN  Barista
              │         │         │
              └────┬────┘         │
                   │              │
              👤 KHÁCH HÀNG ──────┘
              (Scan QR + Zalo)
```

---
---

# IV. 8 MODULE CHỨC NĂNG CHI TIẾT

## Module 1: 💳 BÁN HÀNG & THANH TOÁN (POS)

### Màn hình Thu ngân tạo đơn:

| Bước | Thao Tác | Thời Gian |
|---|---|---|
| 1 | Chọn món trên màn hình cảm ứng (phân loại: Cà phê / Trà / Đá xay / Bánh / Topping) | 2-3 giây |
| 2 | Tùy chỉnh: Size (S/M/L), đường (0-25-50-75-100%), đá (ít/nhiều/không), thêm Topping | 1-2 giây |
| 3 | Chọn hình thức thanh toán: **Tiền mặt / VietQR / MoMo / Chuyển khoản** | 1 giây |
| 4 | Hệ thống **tự tạo mã VietQR động** (đúng số tiền, đúng tài khoản quán) — Khách scan trả | 3-5 giây |
| 5 | Đơn hàng tự động hiện trên **Màn hình KDS Pha chế** | Ngay lập tức |
| 6 | In bill (tùy chọn) hoặc gửi bill qua Zalo | 1 giây |

**Tổng thời gian 1 đơn: ~10-15 giây** (so với ghi sổ tay: 1-2 phút).

### Tính năng nổi bật:
- ✅ **Mã VietQR động tự tạo:** Không cần quét mã cố định → khách trả đúng số tiền, hệ thống tự ghi nhận, **không nhầm lẫn**.
- ✅ **Tách bill / Gộp bill:** Khách 1 bàn 5 người muốn chia tiền → tách bill từng người ngay trên POS.
- ✅ **Áp voucher tự động:** Nhập mã hoặc scan QR loyalty → giảm giá tự động.
- ✅ **Chế độ offline:** Mất WiFi vẫn bán được → dữ liệu đồng bộ khi có mạng lại.

---

## Module 2: 📺 MÀN HÌNH PHA CHẾ / BẾP (KDS)

### Barista nhìn thấy gì trên màn hình?

```
┌──────────────────────────────────────────────────────────────────┐
│  📺 KDS — Màn hình Pha Chế        Quán: Q1 - Nguyễn Huệ        │
├──────────────┬──────────────┬──────────────┬─────────────────────┤
│  ĐƠN #047   │  ĐƠN #048   │  ĐƠN #049   │  ĐƠN #050          │
│  ⏱️ 2:15     │  ⏱️ 1:30     │  ⏱️ 0:45     │  ⏱️ MỚI            │
│  ──────────  │  ──────────  │  ──────────  │  ──────────         │
│  Latte (L)   │  Cappuccino  │  Trà Đào     │  Bạc Xỉu (M)      │
│  Đường: 50%  │  Size: M     │  Cam Sả (L)  │  Đường: 75%        │
│  Đá: Nhiều   │  Đường: 25%  │  Đá: Ít      │  Thêm: Shot Esp   │
│  ──────────  │  ──────────  │  ──────────  │  ──────────         │
│  📋 CÔNG THỨC│  📋 CÔNG THỨC│  📋 CÔNG THỨC│  📋 CÔNG THỨC      │
│  • Esp 2 shot│  • Esp 2 shot│  • Trà đen   │  • Esp 1 shot      │
│  • Sữa 200ml│  • Sữa 150ml│    200ml     │  • Sữa đặc 40ml   │
│  • Đá 200g  │  • Foam sữa │  • Đào 3 lát │  • Sữa tươi 180ml │
│              │    5cm      │  • Cam 2 lát │  • Đá 150g          │
│              │              │  • Sả 2 lát  │  • + Shot Esp       │
│  ┌────────┐  │  ┌────────┐  │  ┌────────┐  │  ┌────────┐        │
│  │✅ XONG  │  │  │✅ XONG  │  │  │✅ XONG  │  │  │✅ XONG  │        │
│  └────────┘  │  └────────┘  │  └────────┘  │  └────────┘        │
└──────────────┴──────────────┴──────────────┴─────────────────────┘
```

**Lợi ích:**
- Barista **không cần nhớ công thức** → màn hình hiện sẵn nguyên liệu + lượng chính xác.
- Barista mới **đào tạo 1 ngày** là pha được (thay vì 2-4 tuần).
- Đảm bảo **chuẩn vị 100%** giữa 3 quán — Quán 1 và Quán 3 pha giống nhau.
- Đơn nào chờ lâu sẽ **đổi màu đỏ** → ưu tiên pha trước.

---

## Module 3: 👥 QUẢN LÝ NHÂN SỰ & CHẤM CÔNG (HRM)

### 3.1 Chấm Công Chống Gian Lận

| Cách cũ (Thủ công) | Cách mới (F&B OS) |
|---|---|
| Sổ tay / Vân tay dễ nhờ chấm hộ | **QR Code động** đổi mỗi 30 giây + **GPS Lock** (chỉ chấm được trong bán kính 50m quán) |
| Không biết nhân viên đi muộn hay sớm | Ghi nhận chính xác giờ vào/ra **từng phút** |
| Cuối tháng tính lương mất 2-3 ngày | Hệ thống **tự tính lương** theo giờ thực tế + phụ cấp ca đêm/cuối tuần |

### 3.2 Xếp Ca Thông Minh

```
TRƯỚC (Cảm tính):                        SAU (AI Đề xuất):
┌─────────────────────┐                  ┌──────────────────────────────────┐
│ Thứ 2: 4 NV sáng    │                  │ Thứ 2: 3 NV sáng (dự báo vắng) │
│ Thứ 7: 4 NV sáng    │   →→→→→→→→→     │ Thứ 7: 6 NV sáng (dự báo ĐÔNG) │
│ (Giống nhau mọi ngày│                  │ AI phân tích: Thứ 7 đông gấp 2 │
│  → Thứ 2 dư, T7 thiếu)                │  → Tự điều phối nhân lực        │
└─────────────────────┘                  └──────────────────────────────────┘
```

---

## Module 4: 📦 QUẢN LÝ KHO & NGUYÊN LIỆU

### 4.1 Mô Hình Kho 2 Tầng

```
┌──────────────────────────────────────────────────────────┐
│                    KHO TỔNG (Kho chính)                   │
│  Lưu trữ nguyên liệu nhập từ NCC (Nhà Cung Cấp)        │
│  Đơn vị: Bao 5kg, Thùng 12 hộp, Chai 1.5L...            │
│  Ví dụ: 10 bao CF hạt (5kg) + 50 hộp sữa (1L)...       │
└────────────┬────────────┬────────────┬───────────────────┘
             │ Xuất kho    │ Xuất kho    │ Xuất kho
             │ quầy Q1    │ quầy Q2    │ quầy Q3
        ┌────▼────┐  ┌────▼────┐  ┌────▼────┐
        │ QUẦY Q1 │  │ QUẦY Q2 │  │ QUẦY Q3 │
        │ CF 2kg  │  │ CF 3kg  │  │ CF 1.5kg│
        │ Sữa 10L│  │ Sữa 8L │  │ Sữa 12L│
        │ Syrup 2 │  │ Syrup 1 │  │ Syrup 3 │
        └─────────┘  └─────────┘  └─────────┘
```

### 4.2 Luồng Xuất Kho Quầy (Mỗi Ngày)

| Bước | Ai Làm | Thao Tác | Hệ Thống Ghi Nhận |
|---|---|---|---|
| 1 | **Quản lý** mở ca sáng | Kiểm tra quầy còn bao nhiêu nguyên liệu | Tồn quầy đầu ca |
| 2 | **Quản lý** lấy hàng từ kho | Ghi phiếu xuất kho: "Xuất 2kg CF hạt + 5 hộp sữa lên Quầy" | Trừ kho tổng, cộng kho quầy |
| 3 | **Barista** pha chế cả ca | Sử dụng nguyên liệu tại quầy bình thường | Hệ thống ước tính tiêu hao dựa trên số đơn đã bán |
| 4 | **Quản lý** cuối ca | Kiểm kê quầy: "CF còn 0.8kg, sữa còn 2 hộp" | So sánh: Xuất ra bao nhiêu − Còn lại bao nhiêu − Ước tính tiêu hao |
| 5 | **Hệ thống** | Tự động tính **chênh lệch** | ⚠️ Cảnh báo nếu chênh lệch > 5%: "Quán Q1: CF chênh 300g so với ước tính — kiểm tra thất thoát" |

### 4.3 AI Đề Xuất Nhập Hàng

```
┌─────────────────────────────────────────────────────────────┐
│  📦 ĐỀ XUẤT NHẬP HÀNG — Tuần 2 Tháng 8/2026               │
│                                                              │
│  Dựa trên: Doanh số 4 tuần gần nhất + Dự báo khách tuần tới│
│                                                              │
│  ┌────────────────────────┬─────────┬────────────┐          │
│  │ Nguyên liệu            │ Tồn kho │ Cần nhập   │          │
│  ├────────────────────────┼─────────┼────────────┤          │
│  │ Cà phê hạt Arabica     │ 4 kg    │ ⚠️ 12 kg    │          │
│  │ Sữa tươi TH True Milk  │ 15 hộp  │ 30 hộp     │          │
│  │ Syrup Caramel Monin     │ 3 chai  │ 5 chai     │          │
│  │ Đường nâu               │ 2 kg    │ 4 kg       │          │
│  │ Trà Oolong              │ 8 gói   │ ✅ Đủ dùng  │          │
│  └────────────────────────┴─────────┴────────────┘          │
│                                                              │
│  ⚠️ Cà phê hạt: Dự kiến hết trong 3 ngày                    │
│  💡 Đề xuất: Đặt hàng NCC trước Thứ 4                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Module 5: 💰 TÀI CHÍNH & BÁO CÁO TỰ ĐỘNG (EOD)

### 5.1 Báo Cáo Cuối Ca Tự Động (Auto EOD Report)

**Trước đây:** Quản lý ngồi đếm két tiền 30-60 phút, gõ tay gửi Zalo cho chủ.

**Bây giờ:** Hệ thống tự tổng hợp và gửi ngay khi kết ca:

```
┌─────────────────────────────────────────────────────┐
│  📊 BÁO CÁO CUỐI CA — Quán Q1 Nguyễn Huệ            │
│  Ca: Tối (14:00 - 22:00) — Ngày: 06/08/2026         │
│  Quản lý ca: Nguyễn Văn A                            │
│                                                      │
│  DOANH THU:                                          │
│  ├─ Tiền mặt:        2,850,000 VNĐ                  │
│  ├─ Chuyển khoản/QR: 4,200,000 VNĐ                  │
│  ├─ MoMo:              680,000 VNĐ                   │
│  └─ TỔNG:            7,730,000 VNĐ                   │
│                                                      │
│  SỐ ĐƠN:             127 đơn                         │
│  TRUNG BÌNH/ĐƠN:     60,866 VNĐ                     │
│                                                      │
│  ĐỐI SOÁT KÉT TIỀN:                                 │
│  ├─ Tiền mặt hệ thống ghi:  2,850,000 VNĐ           │
│  ├─ Tiền mặt thực đếm:      2,840,000 VNĐ           │
│  └─ Chênh lệch:             -10,000 VNĐ  ✅ OK       │
│                                                      │
│  TOP 5 MÓN BÁN CHẠY:                                │
│  1. Bạc Xỉu (M)     — 28 ly                         │
│  2. Latte (L)        — 22 ly                         │
│  3. Trà Đào Cam Sả   — 19 ly                         │
│  4. Cappuccino       — 15 ly                         │
│  5. Sinh tố Xoài    — 12 ly                          │
└─────────────────────────────────────────────────────┘
```

Báo cáo này được **tự động gửi qua Zalo/Email** cho Quản lý quán + Chủ chuỗi ngay khi kết ca. Chủ chuỗi nhận **3 báo cáo** (1 từ mỗi quán) mà **không cần hỏi ai**.

### 5.2 Dashboard Tài Chính Chủ Chuỗi

| Chỉ Số | Quán Q1 | Quán Q2 | Quán Q3 | TỔNG CHUỖI |
|---|---|---|---|---|
| Doanh thu hôm nay | 15.2 tr | 12.8 tr | 9.5 tr | **37.5 tr** |
| Doanh thu tháng này | 380 tr | 320 tr | 240 tr | **940 tr** |
| Chi phí nguyên liệu | 95 tr | 85 tr | 62 tr | **242 tr** |
| Chi phí nhân công | 72 tr | 68 tr | 55 tr | **195 tr** |
| Chi phí cố định (thuê, điện) | 45 tr | 38 tr | 30 tr | **113 tr** |
| **LỢI NHUẬN RÒNG** | **168 tr** | **129 tr** | **93 tr** | **390 tr** |

---

## Module 6: 👤 QUẢN LÝ KHÁCH HÀNG & LOYALTY (CRM)

### 6.1 Hành Trình Khách Hàng Trong Hệ Thống

```
KHÁCH MỚI          KHÁCH QUAY LẠI           KHÁCH TRUNG THÀNH         KHÁCH SẮP BỎ ĐI
   │                     │                        │                        │
   ▼                     ▼                        ▼                        ▼
Scan QR            Tích điểm mỗi           Đạt hạng Vàng/           AI phát hiện:
tại bàn            lần thanh toán          Kim Cương                 "45 ngày chưa
   │                     │                  │                        quay lại"
   ▼                     ▼                  ▼                            │
Tạo hồ sơ         Nhận voucher            Ưu đãi riêng:                ▼
tự động            sinh nhật              Size-up miễn phí        Auto gửi voucher
(SĐT + Tên)       qua Zalo               Combo VIP               30% off qua Zalo
```

### 6.2 QR Code Feedback Tại Bàn

- Mỗi bàn/ly nước dán **1 mã QR cố định**.
- Khách scan → hiện form đánh giá nhanh (1-5 sao + ghi chú).
- Nếu đánh giá ≤ 2 sao → **Quản lý nhận thông báo tức thì** trên App để xử lý ngay tại chỗ.
- Dữ liệu feedback → AI phân tích → đề xuất cải tiến menu.

---

## Module 7: 📋 QUẢN LÝ MENU & GIÁ

| Tính Năng | Chi Tiết |
|---|---|
| **Menu tập trung** | Chủ chuỗi tạo menu 1 lần → đồng bộ cả 3 quán |
| **Giá theo khu vực** | Quán Q1 (trung tâm): Latte 55K. Quán Thủ Đức: Latte 45K |
| **Bật/Tắt món tức thì** | Hết sữa → tắt tất cả món có sữa ngay lập tức trên POS |
| **Menu mùa / Giới hạn** | Tạo menu "Mùa hè 2026" → tự bật/tắt theo ngày đã đặt |
| **Combo & Upsell** | Gợi ý combo trên POS khi thu ngân chọn món: "Thêm Croissant chỉ +25K?" |

---

## Module 8: 🤖 AI ENGINE — 7 TÍNH NĂNG TRÍ TUỆ NHÂN TẠO

| # | Tính Năng AI | Hệ Thống Tự Động Làm Gì | Ví Dụ Cụ Thể |
|---|---|---|---|
| AI-1 | **Dự báo doanh thu** | Dự đoán doanh thu & lượng khách 7-30 ngày tới | "Thứ 7 tuần tới Q1: ~185 khách, doanh thu dự kiến 12.5 triệu" |
| AI-2 | **Dự báo nguyên liệu** | Tự tính lượng CF, sữa cần nhập cho tuần tới | "Cần nhập 9kg CF hạt + 100 hộp sữa trước Thứ 5" |
| AI-3 | **Gợi ý Combo** | Phân tích món nào hay mua cùng nhau → tạo combo | "68% khách mua Latte cũng mua Croissant → Combo 75K" |
| AI-4 | **Phát hiện khách sắp bỏ** | Tìm khách lâu không quay lại → tự gửi voucher | "Khách Nguyễn A: 78% khả năng bỏ → gửi voucher 30%" |
| AI-5 | **Chatbot Zalo** | Khách nhắn Zalo đặt món → AI tự hiểu và tạo đơn | Khách gõ: "2 ly trà sữa 3h chiều" → Tạo order tự động |
| AI-6 | **Xếp ca tối ưu** | Dựa trên dự báo khách → tự đề xuất bảng ca tuần | "T7 cần 6 NV, T2 chỉ cần 3 NV" |
| AI-7 | **Menu Intelligence** | Phân tích món bán chạy/chậm + gợi ý giá + khuyến mãi | "Smoothie Dâu: 2 ly/ngày → đề xuất loại. Giờ vắng 14-16h → push combo" |

---
---

# V. LUỒNG VẬN HÀNH HÀNG NGÀY (QUY TRÌNH THỰC TẾ)

## 5.1 Một Ngày Tại Quán — Từ Mở Cửa Đến Đóng Cửa

```
06:30  ┌─ MỞ CA SÁNG ──────────────────────────────────────────┐
       │  • Quản lý mở App → Bấm "Mở Ca"                       │
       │  • Nhập số tiền mặt đầu ca (két tiền)                  │
       │  • Kiểm tra quầy → Xuất kho nếu thiếu nguyên liệu     │
       │  • Barista bật màn hình KDS                             │
       └────────────────────────────────────────────────────────┘
              │
07:00  ┌─ BÁN HÀNG ────────────────────────────────────────────┐
       │  • Khách vào → Thu ngân chọn món trên Tablet POS        │
       │  • Khách thanh toán (Tiền mặt / Scan VietQR)           │
       │  • Đơn hàng tự động hiện trên KDS cho Barista           │
       │  • Barista pha theo công thức trên màn hình → Bấm XONG  │
       │  • Thu ngân gọi khách lấy đồ                            │
       └────────────────────────────────────────────────────────┘
              │
       (Lặp lại suốt ca — mỗi đơn 10-15 giây)
              │
14:00  ┌─ CHUYỂN CA ────────────────────────────────────────────┐
       │  • Quản lý ca sáng bấm "Kết Ca"                        │
       │  • Đếm tiền mặt trong két → Nhập số thực đếm            │
       │  • Hệ thống tự so sánh: Tiền mặt hệ thống vs Thực đếm  │
       │    ✅ Khớp: "Ca sáng OK — chênh lệch 0đ"                │
       │    ⚠️ Lệch: "Ca sáng chênh -50K — cần kiểm tra"         │
       │  • Quản lý ca tối mở ca mới, nhận bàn giao              │
       └────────────────────────────────────────────────────────┘
              │
22:00  ┌─ KẾT CA TỐI & BÁO CÁO ───────────────────────────────┐
       │  • Quản lý bấm "Kết Ca" → đếm tiền mặt                 │
       │  • Hệ thống TỰ ĐỘNG tạo báo cáo EOD:                   │
       │    ├─ Tổng doanh thu (tiền mặt + QR + MoMo)             │
       │    ├─ Số đơn, trung bình/đơn                             │
       │    ├─ Top 5 món bán chạy                                 │
       │    ├─ Đối soát két tiền                                  │
       │    └─ Cảnh báo bất thường (nếu có)                       │
       │  • Báo cáo TỰ ĐỘNG GỬI qua Zalo/Email cho:              │
       │    ├─ Quản lý quán                                       │
       │    └─ Chủ chuỗi                                          │
       └────────────────────────────────────────────────────────┘
              │
22:30  ┌─ CHỦ CHUỖI NHẬN BÁO CÁO ─────────────────────────────┐
       │  📱 Zalo nhận 3 thông báo:                               │
       │  ├─ "Q1 Nguyễn Huệ: 15.2 tr — 245 đơn — két khớp ✅"    │
       │  ├─ "Q2 Lý Tự Trọng: 12.8 tr — 198 đơn — két khớp ✅"   │
       │  └─ "Q3 Thủ Đức: 9.5 tr — 142 đơn — két lệch -30K ⚠️"  │
       │                                                           │
       │  💻 Dashboard Web: Biểu đồ tổng 3 quán, so sánh chi tiết │
       └────────────────────────────────────────────────────────┘
```

## 5.2 Quy Trình Kiểm Kê Kho (Mỗi Tuần / Cuối Tháng)

| Bước | Ai Làm | Mô Tả |
|---|---|---|
| 1 | Quản lý quán | Mở App → vào "Kiểm Kê" → Chọn kho cần kiểm |
| 2 | Quản lý quán | Đếm/cân từng loại nguyên liệu → Nhập số thực tế (VD: CF hạt 3.2kg, Sữa 8 hộp) |
| 3 | Hệ thống | So sánh: Số liệu hệ thống (tính toán) vs Số liệu thực đếm |
| 4 | Hệ thống | Nếu chênh lệch > 5%: ⚠️ Cảnh báo "Thất thoát bất thường" gửi cho Chủ chuỗi |
| 5 | Chủ chuỗi | Xem báo cáo kiểm kê trên Dashboard → quyết định điều tra hoặc điều chỉnh |

---
---

# VI. THIẾT BỊ & TRANG BỊ CHO MỖI QUÁN

## 6.1 Danh Sách Thiết Bị Tại Mỗi Chi Nhánh

| # | Thiết Bị | Số Lượng/Quán | Mục Đích | Giá Ước Tính |
|---|---|---|---|---|
| 1 | **Tablet Android 10"** (Samsung Tab A8 hoặc tương đương) | 1-2 cái | Chạy App POS bán hàng | 4-6 triệu/cái |
| 2 | **Màn hình LCD/TV 22-32"** | 1 cái | Hiển thị KDS cho Barista | 3-5 triệu |
| 3 | **Máy in hóa đơn nhiệt** (Xprinter 80mm) | 1 cái | In bill cho khách | 1-2 triệu |
| 4 | **Giá đỡ Tablet** | 1-2 cái | Cố định Tablet trên quầy thu ngân | 200-500K |
| 5 | **Sticker QR Feedback** | 10-20 tờ | Dán tại mỗi bàn → khách scan đánh giá | In ấn ~100K |
| 6 | **WiFi ổn định** | Có sẵn | Kết nối Internet cho hệ thống | Chi phí hàng tháng sẵn có |

## 6.2 Tổng Chi Phí Thiết Bị Cho Cả Chuỗi 3 Quán

| Hạng Mục | Đơn Giá | × 3 Quán | Tổng |
|---|---|---|---|
| Tablet POS (2 cái/quán) | 10 triệu | × 3 | 30 triệu |
| Màn hình KDS | 4 triệu | × 3 | 12 triệu |
| Máy in bill | 1.5 triệu | × 3 | 4.5 triệu |
| Giá đỡ + QR Code | 700K | × 3 | 2.1 triệu |
| **TỔNG THIẾT BỊ** | | | **~48.6 triệu** |

> 💡 **Ghi chú:** Nếu quán đã có Tablet/iPad sẵn có thể tận dụng → giảm đáng kể chi phí. Phần mềm chạy trên trình duyệt web nên **không yêu cầu thiết bị đặc biệt**.

---
---

# VII. DASHBOARD CHỦ CHUỖI — QUẢN LÝ 3 QUÁN TỪ 1 MÀN HÌNH

## 7.1 Màn Hình Tổng Quan (Overview)

```
╔══════════════════════════════════════════════════════════════════════╗
║  📊 F&B OS — DASHBOARD CHỦ CHUỖI        Xin chào, Anh/Chị [Tên]  ║
║  Ngày: 06/08/2026 (Thứ Tư)              Cập nhật: 5 phút trước    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     ║
║  │  🏪 QUÁN Q1      │  │  🏪 QUÁN Q2      │  │  🏪 QUÁN Q3      │     ║
║  │  Nguyễn Huệ, Q1  │  │  Lý Tự Trọng,Q3 │  │  Thủ Đức         │     ║
║  │                   │  │                   │  │                   │     ║
║  │  💰 15.2 tr       │  │  💰 12.8 tr       │  │  💰 9.5 tr        │     ║
║  │  📦 245 đơn       │  │  📦 198 đơn       │  │  📦 142 đơn       │     ║
║  │  👥 6/6 NV        │  │  👥 5/6 NV ⚠️    │  │  👥 6/6 NV        │     ║
║  │  🟢 Đang mở       │  │  🟢 Đang mở       │  │  🟢 Đang mở       │     ║
║  └─────────────────┘  └─────────────────┘  └─────────────────┘     ║
║                                                                      ║
║  ── TỔNG CHUỖI HÔM NAY ──────────────────────────────────────      ║
║  💰 Tổng doanh thu:  37,500,000 VNĐ    (↑12% so với Thứ 3)        ║
║  📦 Tổng đơn hàng:   585 đơn                                        ║
║  💵 Trung bình/đơn:   64,103 VNĐ                                    ║
║                                                                      ║
║  ── CẢNH BÁO ──────────────────────────────────────────────────      ║
║  ⚠️ Q2: Nhân viên Trần B vắng mặt không báo trước                   ║
║  ⚠️ Q3: Cà phê hạt còn 1.2kg — dự kiến hết trong 1 ngày            ║
║  ✅ Két tiền 3 quán ca sáng: Đều khớp 100%                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 7.2 Chủ Chuỗi Có Thể Làm Gì Từ Dashboard?

| Chức Năng | Mô Tả |
|---|---|
| 📊 **So sánh chi nhánh** | Quán nào doanh thu cao nhất? Quán nào chi phí cao bất thường? |
| 📋 **Xem menu & chỉnh giá** | Đổi giá Latte từ 45K → 50K → đồng bộ cả 3 quán (hoặc riêng từng quán) |
| 👥 **Xem nhân sự** | Ai đi muộn, ai nghỉ nhiều, ai làm overtime → quyết định thưởng/phạt |
| 📦 **Xem kho tổng** | Nguyên liệu nào sắp hết? Quán nào tiêu hao nhiều bất thường? |
| 🤖 **Xem báo cáo AI** | AI gợi ý: "Nên thêm Matcha vào menu Q1 — trend tăng 35%", "Bỏ Smoothie Dâu — chỉ 2 ly/ngày" |
| 💰 **Xem P&L (Lãi/Lỗ)** | Bảng Profit & Loss từng quán — biết chính xác quán nào lãi, quán nào đang "nuôi" |
| 📱 **Nhận thông báo tự động** | EOD Report cuối ca, cảnh báo thất thoát, cảnh báo nhân viên bất thường |

---
---

# VIII. LỘ TRÌNH TRIỂN KHAI (TIMELINE)

## 8.1 Kế Hoạch 4 Tuần

| Tuần | Hoạt Động | Chi Tiết |
|---|---|---|
| **Tuần 1** | **Khảo sát & Thiết lập** | Đội kỹ sư đến quán khảo sát quy trình hiện tại, nhập menu, cấu hình kho, tạo tài khoản nhân viên |
| **Tuần 2** | **Triển khai Quán 1 (Pilot)** | Cài đặt thiết bị, đào tạo nhân viên quán 1 (1 buổi 2h), chạy song song với cách cũ trong 1 tuần |
| **Tuần 3** | **Mở rộng Quán 2 + Quán 3** | Sau khi Quán 1 ổn định → triển khai 2 quán còn lại |
| **Tuần 4** | **Tối ưu & Bàn giao** | Điều chỉnh theo feedback thực tế, bật AI features, đào tạo chủ chuỗi dùng Dashboard |

## 8.2 Đào Tạo Nhân Viên

| Đối Tượng | Thời Gian Đào Tạo | Nội Dung |
|---|---|---|
| **Thu ngân** | 30 phút | Cách tạo đơn, nhận thanh toán, in bill trên POS |
| **Barista** | 15 phút | Cách đọc đơn trên KDS, bấm "Hoàn thành" |
| **Quản lý quán** | 1 tiếng | Mở/kết ca, xuất kho, kiểm kê, đối soát két tiền, duyệt ca |
| **Chủ chuỗi** | 1 tiếng | Dùng Dashboard, đọc báo cáo AI, quản lý menu & giá |

---
---

# 📌 TÓM TẮT

| Câu Hỏi | Trả Lời |
|---|---|
| Hệ thống này làm gì? | Quản lý toàn bộ vận hành 3 quán CF: bán hàng, kho, nhân sự, tài chính, khách hàng, menu — tất cả từ 1 nơi |
| Ai dùng? | Chủ chuỗi (Dashboard), Quản lý quán (App), Thu ngân (POS Tablet), Barista (KDS), Khách (QR) |
| Khác POS cũ chỗ nào? | Có AI tự dự báo, tự cảnh báo, tự đề xuất — không chỉ "ghi nhận" mà còn "tư vấn" |
| Triển khai mất bao lâu? | 4 tuần cho cả 3 quán |
| Nhân viên có khó dùng không? | Thu ngân học 30 phút, Barista học 15 phút — đơn giản hơn dùng điện thoại |
| Chi phí thiết bị? | ~48.6 triệu cho cả 3 quán (có thể tận dụng thiết bị sẵn có) |

---

> **F&B Operating System** — Giải pháp công nghệ nâng tầm vận hành cho chuỗi cà phê Việt Nam.
>
> 📞 Liên hệ: [Tên / SĐT / Email của bạn]
