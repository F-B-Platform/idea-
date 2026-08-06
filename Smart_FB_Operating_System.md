# ☕ SMART F&B OPERATING SYSTEM
## Nền Tảng Quản Lý & Vận Hành Quán Cà Phê Thông Minh — Thay Thế Hoàn Toàn Hệ Thống POS Truyền Thống

> **Tên dự án:** Smart F&B OS — AI-Powered QR Order & Management Platform
>
> **Slogan:** *"Không cần máy POS, không cần thu ngân gõ đơn — Khách scan QR, tự chọn món, tự thanh toán."*
>
> **Công nghệ lõi:** QR Self-Ordering + Web/Mobile App + AI Analytics + Cloud

---
---

# 📚 MỤC LỤC

| Phần | Nội Dung |
|---|---|
| **PHẦN 0** | 8 Bất Cập Thực Tế Của Quán Cà Phê Hiện Nay |
| **PHẦN I** | Tổng Quan Dự Án & Bài Toán |
| **PHẦN II** | Hướng Giải Quyết — Hệ Thống Đề Xuất |
| **PHẦN III** | AI Ứng Dụng — Chi Tiết Kỹ Thuật |
| **PHẦN IV** | Dự Án Giải Quyết Được Gì Cho Thị Trường? |
| **PHẦN V** | Điểm Độc Đáo & So Sánh Đối Thủ |
| **PHẦN VI** | Kiến Trúc Hệ Thống & Công Nghệ |
| **PHẦN VII** | Tính Năng Hệ Thống Chi Tiết Theo Từng Actor |

---
---

# 📝 PHẦN 0: 8 BẤT CẬP THỰC TẾ CỦA QUÁN CÀ PHÊ HIỆN NAY

## 0.1 🔴 Bất Cập Về HỆ THỐNG POS LỖI THỜI & QUY TRÌNH ĐẶT MÓN THỦ CÔNG

### Hiện trạng:
- **Khách phải xếp hàng tại quầy để gọi món:** Giờ cao điểm (8-9h sáng, 14-16h chiều) hàng dài 5-10 người → **khách bỏ đi** vì không muốn chờ.
- **Thu ngân phải gõ tay từng đơn vào máy POS:** Mỗi đơn mất 30-60 giây → tốc độ phục vụ bị giới hạn bởi **tốc độ gõ của 1 người thu ngân**. Muốn nhanh hơn → phải thuê thêm thu ngân → **tăng chi phí nhân sự**.
- **Sai đơn do giao tiếp:** Khách nói "ít đường", thu ngân ghi "không đường" hoặc quên ghi → **pha sai, phải pha lại, lãng phí nguyên liệu + mất uy tín**.
- **Máy POS đắt tiền:** Máy POS chuyên dụng giá 8-25 triệu VNĐ/bộ, chưa kể phí phần mềm hàng tháng (iPOS: 500K-2 triệu/tháng, KiotViet: 250K-1.5 triệu/tháng).
- **POS chỉ ghi nhận, không tối ưu:** POS truyền thống chỉ là "máy tính tiền" — ghi lại đơn hàng, in bill. **Không có AI**, không dự báo, không gợi ý, không chăm sóc khách hàng.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Khách bỏ đi vì xếp hàng lâu (giờ cao điểm) | Mất 10-20 đơn/ngày × 50K = 500K-1 triệu/ngày |
| Sai đơn do giao tiếp | 3-5 ly pha lại/ngày × 40K = 120-200K/ngày |
| Chi phí máy POS + phần mềm | 8-25 triệu/máy + 500K-2 triệu/tháng phí phần mềm |
| Thuê 2 thu ngân thay vì 1 | Thêm 6-8 triệu lương/tháng |

---

## 0.2 📋 Bất Cập Về CHẤM CÔNG & QUẢN LÝ NHÂN SỰ

### Hiện trạng:
- **Chấm công bằng sổ tay hoặc vân tay:** Nhân viên nhờ đồng nghiệp chấm hộ, đi muộn 15-30 phút nhưng sổ ghi đúng giờ → **gian lận 5-10% quỹ lương/tháng**.
- **Xếp ca theo cảm tính:** Quản lý xếp ca giống nhau mọi ngày (4 NV sáng, 4 NV tối) mà không biết Thứ 2 vắng khách (chỉ cần 2 NV), Thứ 7 đông gấp đôi (cần 6 NV) → **lãng phí 20-30% chi phí nhân công**.
- **Tính lương cuối tháng mất 2-3 ngày:** Quản lý phải lật sổ chấm công, tính tay từng ca, cộng phụ cấp, trừ nghỉ → **sai sót thường xuyên, nhân viên khiếu nại**.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Gian lận chấm công | 5-10% quỹ lương/tháng (~3-8 triệu/quán) |
| Xếp ca không theo data | Lãng phí 20-30% nhân công giờ vắng |
| Tính lương thủ công | Mất 2-3 ngày/tháng + sai sót |

---

## 0.3 📦 Bất Cập Về KIỂM KÊ HÀNG HÓA & NGUYÊN LIỆU

### Hiện trạng:
- **Không biết nguyên liệu đi đâu:** Cà phê hạt, sữa tươi, syrup — mua về kho nhưng cuối tuần đếm lại thì **thiếu 5-15%** mà không biết mất ở đâu (barista lấy dư? Nhân viên mang về? Hết hạn đổ bỏ không ghi?).
- **Kiểm kê bằng sổ tay hoặc Excel:** Quản lý phải đếm tay từng loại nguyên liệu, ghi vào sổ → **mất 1-2 tiếng mỗi lần kiểm kê**, dễ sai, không real-time.
- **Hết hàng giữa ca:** Đang giờ cao điểm mà hết sữa/hết cà phê → **không bán được sản phẩm chính**, mất doanh thu.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Thất thoát 5-15% nguyên liệu | 10-30 triệu VNĐ/tháng (tùy quy mô) |
| Hết hàng giữa ca | Mất 20-50 đơn × 50K = 1-2.5 triệu/lần |

---

## 0.4 💰 Bất Cập Về QUẢN LÝ TÀI CHÍNH

### Hiện trạng:
- **Doanh thu, chi phí nằm rải rác:** Tiền mặt trong két, tiền chuyển khoản trong app ngân hàng, tiền MoMo trong ví MoMo → **không ai biết tổng doanh thu thật là bao nhiêu** cho đến cuối ngày đếm lại.
- **Không biết lợi nhuận thật:** Doanh thu 300 triệu/tháng nhưng trừ hết chi phí (nguyên liệu, lương, thuê mặt bằng, điện nước) → **lãi hay lỗ?** Nhiều chủ quán không biết chính xác.
- **Quản lý chuỗi mù mờ:** Chủ có 3 quán nhưng không biết quán nào lãi, quán nào đang "nuôi" → **giữ quán lỗ quá lâu**, không cắt lỗ kịp thời.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Không biết P&L (Profit & Loss) từng ngày | Ra quyết định sai, nuôi quán lỗ hàng tháng |
| Tiền mặt chênh lệch không truy vết được | Mất 200K-1 triệu/tháng do thất thoát két tiền |

---

## 0.5 🍵 Bất Cập Về CHẤT LƯỢNG SẢN PHẨM & THIẾU PHẢN HỒI KHÁCH HÀNG

### Hiện trạng:
- **Phụ thuộc tay nghề barista:** Cùng 1 công thức Latte, barista A pha ngon, barista B pha nhạt — vì không có hệ thống hiển thị công thức chuẩn.
- **Quán Q1 khác quán Q3:** Khách quen uống ở quán trung tâm, đến quán ngoại thành thấy "khác vị" → mất niềm tin vào thương hiệu.
- **Không thu thập được feedback khách hàng:** Không biết ly nào khách khen, ly nào bị trả lại → **cải tiến menu bằng cảm tính**.

### Giải pháp trong hệ thống:
- **Màn hình KDS hiện công thức chuẩn** cho từng ly (bao nhiêu ml sữa, bao nhiêu shot espresso, nhiệt độ bao nhiêu).
- **QR Code Feedback tại bàn:** Khách scan → đánh giá 1-5 sao + ghi chú. Đánh giá ≤ 2 sao → quản lý nhận thông báo tức thì xử lý ngay.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Chất lượng không đồng nhất giữa chi nhánh | Mất 10-20% khách trung thành |
| Không có data feedback | Cải tiến menu bằng cảm tính, bỏ lỡ vấn đề |

---

## 0.6 👤 Bất Cập Về QUẢN LÝ KHÁCH HÀNG & LOYALTY

### Hiện trạng:
- **Không biết khách hàng là ai:** 80% khách mua xong ra về → quán **không có SĐT, không có lịch sử mua**, không thể chăm sóc.
- **Thẻ tích điểm giấy:** Dễ mất, dễ giả mạo, khách không mang theo → **tỷ lệ sử dụng < 10%**.
- **Không biết khách nào sắp bỏ đi:** Khách quen đột ngột biến mất 2-3 tháng, quán không biết → **mất khách vĩnh viễn** mà tìm khách mới tốn gấp 5-7 lần.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Không có data khách hàng | Không target được marketing → chi phí quảng cáo lãng phí |
| Khách bỏ đi không quay lại | Chi phí tìm khách mới đắt gấp 5-7 lần giữ khách cũ |

---

## 0.7 📋 Bất Cập Về BÁO CÁO CUỐI NGÀY (EOD Report) Thủ Công

### Hiện trạng:
- **Tổng hợp doanh thu cuối ca bằng tay:** Quản lý phải đếm tiền mặt, đối chiếu sổ, cộng chuyển khoản → **mất 30-60 phút mỗi tối**.
- **Gửi báo cáo qua Zalo:** Chụp sổ hoặc gõ tay số liệu → **dễ sai số**, chủ chuỗi nhận 5-10 tin Zalo mỗi tối, **không tổng hợp được**.
- **Chủ chuỗi không có dashboard real-time:** Muốn biết "hôm nay doanh thu bao nhiêu?" → phải đợi sáng hôm sau.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Tổng hợp báo cáo thủ công mỗi tối | Quản lý mất 30-60 phút/ngày = ~15-30 giờ/tháng |
| Số liệu sai sót | Chênh lệch 2-5% doanh thu báo cáo vs thực tế |
| Không có dashboard real-time | Ra quyết định chậm 12-24 tiếng |

---

## 0.8 🧠 Bất Cập Về THIẾU DATA ĐỂ RA QUYẾT ĐỊNH MENU & THỊ TRƯỜNG

### Hiện trạng:
- **Thêm/bỏ món theo cảm tính:** Thấy quán bạn bán Matcha chạy → bắt chước mà **không biết khách mình có thích không**.
- **Không biết món nào đang lên/xuống:** 40 món trên menu nhưng không biết top 5 bán chạy đang tăng hay giảm.
- **Khuyến mãi sai thời điểm:** Push khuyến mãi lúc quán đã đông (lãng phí margin) thay vì lúc vắng (kéo khách).

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Thêm món không phù hợp | Tốn chi phí nguyên liệu + đào tạo, bán 2-3 ly/ngày rồi bỏ |
| Giữ 10-15 món bán chậm trên menu | Chiếm chỗ, lãng phí nguyên liệu |
| Khuyến mãi sai thời điểm | Giảm margin khi không cần, không kéo khách khi cần |

---
---

# 📝 PHẦN I: TỔNG QUAN VÀ BÀI TOÁN

## 1. 🎯 Mô Tả Dự Án

### Tên dự án: Smart F&B Operating System

**Bài toán cốt lõi:** Các quán cà phê tại Việt Nam đang vận hành bằng **hệ thống POS lỗi thời** (iPOS, KiotViet, CukCuk) — chỉ đóng vai trò "máy tính tiền", không có AI, không tự đặt món, không phân tích dữ liệu. Trong khi đó, khách hàng ngày càng quen với việc **tự đặt món bằng điện thoại** (GrabFood, ShopeeFood) nhưng khi vào quán vẫn phải **xếp hàng gọi bằng miệng**.

**Giải pháp:** Xây dựng hệ thống vận hành F&B toàn diện với **QR Self-Ordering** làm trung tâm — khách scan QR tại bàn → tự chọn món → tự thanh toán → đơn bay thẳng vào bếp. **Thay thế hoàn toàn máy POS truyền thống**, tích hợp quản lý kho, nhân sự, tài chính, khách hàng và AI phân tích.

## 2. 🔴 CÁC VẤN ĐỀ NGHIÊM TRỌNG CẦN GIẢI QUYẾT (Tóm Tắt 8 Bất Cập)

| # | Vấn Đề | Phạm Vi | Thiệt Hại Ước Tính |
|---|---|---|---|
| **V1** | POS lỗi thời, khách xếp hàng, sai đơn, máy đắt tiền | Đặt món | Mất 500K-1 triệu/ngày + 8-25 triệu/máy POS |
| **V2** | Chấm công gian lận, xếp ca cảm tính | HRM | 5-10% quỹ lương + 20-30% nhân công lãng phí |
| **V3** | Kiểm kê thủ công, thất thoát nguyên liệu | Kho | 5-15% nguyên liệu thất thoát (10-30 triệu/tháng) |
| **V4** | Không biết lợi nhuận thật, quản lý tài chính rời rạc | Tài chính | Ra quyết định sai, nuôi quán lỗ |
| **V5** | Chất lượng không đồng nhất, thiếu feedback | Sản phẩm | Mất 10-20% khách trung thành |
| **V6** | Không quản lý được khách hàng, không giữ chân | CRM | Chi phí tìm khách mới đắt gấp 5-7 lần |
| **V7** | Báo cáo cuối ngày thủ công 30-60 phút | Báo cáo | Sai sót 2-5% số liệu, chậm ra quyết định |
| **V8** | Thiếu data phân tích menu & thị trường | Menu/KD | Thêm/bỏ món theo cảm tính |

---
---

# 📝 PHẦN II: HƯỚNG GIẢI QUYẾT — HỆ THỐNG ĐỀ XUẤT

## 3. ✅ GIẢI PHÁP TRUNG TÂM: QR SELF-ORDER — THAY THẾ HOÀN TOÀN MÁY POS

### 3.1 Luồng Đặt Món Mới (QR Order)

```
╔══════════════════════════════════════════════════════════════════════╗
║                    LUỒNG ĐẶT MÓN QR SELF-ORDER                     ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  BƯỚC 1: KHÁCH VÀO QUÁN                                            ║
║  ┌──────────────────────────────────────────────────────────┐       ║
║  │  📱 Khách ngồi bàn → Quét mã QR trên bàn bằng điện thoại │       ║
║  │  (Không cần tải app — mở bằng trình duyệt)               │       ║
║  └──────────────────────────┬───────────────────────────────┘       ║
║                              │                                       ║
║  BƯỚC 2: XEM MENU & CHỌN MÓN                                       ║
║  ┌──────────────────────────▼───────────────────────────────┐       ║
║  │  📋 Menu hiện trên điện thoại khách:                      │       ║
║  │  ├─ Phân loại: Cà phê | Trà | Đá xay | Bánh | Topping   │       ║
║  │  ├─ Ảnh món + Giá + Mô tả                                │       ║
║  │  ├─ Tùy chỉnh: Size (S/M/L), Đường (0-100%), Đá, Topping│       ║
║  │  └─ Ghi chú đặc biệt: "Ít đá, thêm shot espresso"       │       ║
║  └──────────────────────────┬───────────────────────────────┘       ║
║                              │                                       ║
║  BƯỚC 3: THANH TOÁN                                                 ║
║  ┌──────────────────────────▼───────────────────────────────┐       ║
║  │  💳 Chọn hình thức thanh toán:                            │       ║
║  │  ├─ 📲 VietQR (Mã QR động — đúng số tiền, tự xác nhận)  │       ║
║  │  ├─ 📲 MoMo / ZaloPay                                    │       ║
║  │  └─ 💵 Tiền mặt (thanh toán tại quầy sau khi nhận món)   │       ║
║  └──────────────────────────┬───────────────────────────────┘       ║
║                              │                                       ║
║  BƯỚC 4: ĐƠN HÀNG BAY VÀO BẾP                                     ║
║  ┌──────────────────────────▼───────────────────────────────┐       ║
║  │  📺 Đơn hàng TỰ ĐỘNG hiện trên MÀN HÌNH KDS (Bếp/Pha chế)│     ║
║  │  ├─ Hiện: Món + Size + Đường + Đá + Ghi chú + Số bàn     │       ║
║  │  ├─ Hiện: CÔNG THỨC PHA CHẾ CHUẨN cho từng ly            │       ║
║  │  └─ Barista pha xong → Bấm "HOÀN THÀNH"                  │       ║
║  └──────────────────────────┬───────────────────────────────┘       ║
║                              │                                       ║
║  BƯỚC 5: KHÁCH NHẬN MÓN                                            ║
║  ┌──────────────────────────▼───────────────────────────────┐       ║
║  │  🔔 Điện thoại khách nhận thông báo: "Món đã sẵn sàng!"  │       ║
║  │  Hoặc: Nhân viên mang ra bàn theo số bàn                 │       ║
║  └──────────────────────────────────────────────────────────┘       ║
╚══════════════════════════════════════════════════════════════════════╝
```

### 3.2 So Sánh: Cách Cũ vs. QR Self-Order

| Tiêu Chí | ❌ POS Truyền Thống (Cách cũ) | ✅ QR Self-Order (F&B OS) |
|---|---|---|
| **Đặt món** | Khách xếp hàng → nói cho thu ngân → thu ngân gõ vào POS | Khách scan QR → **tự chọn trên điện thoại** → gửi |
| **Tốc độ** | 30-60 giây/đơn (phụ thuộc thu ngân) | **10-15 giây/đơn** (khách tự chọn, không phụ thuộc ai) |
| **Sai đơn** | Thường xuyên (nói "ít đường" ghi "không đường") | **Gần 0%** (khách tự chọn chính xác trên màn hình) |
| **Giờ cao điểm** | Xếp hàng 5-10 người, khách bỏ đi | **Không xếp hàng** — 50 khách đặt cùng lúc được |
| **Nhân sự thu ngân** | Cần 1-2 thu ngân mỗi ca | **Không cần thu ngân** (hoặc giảm xuống 1 người hỗ trợ) |
| **Chi phí máy POS** | 8-25 triệu/máy + phí hàng tháng | **0 đồng** — chỉ cần in QR Code dán bàn |
| **Thanh toán** | Thu ngân nhận tiền mặt, quét mã thủ công | **Tự động:** VietQR động tự tạo theo số tiền |
| **Data khách hàng** | Không thu thập được | **Tự động:** SĐT khi thanh toán → CRM Loyalty |

### 3.3 Mã QR Tại Quán — Hoạt Động Thế Nào?

```
┌───────────────────────────────────────────────────────┐
│                                                       │
│   Mỗi BÀN trong quán có 1 mã QR duy nhất:            │
│                                                       │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐              │
│   │ QR BÀN 1│  │ QR BÀN 2│  │ QR BÀN 3│  ...         │
│   │ ██████  │  │ ██████  │  │ ██████  │              │
│   │ ██  ██  │  │ ██  ██  │  │ ██  ██  │              │
│   │ ██████  │  │ ██████  │  │ ██████  │              │
│   └─────────┘  └─────────┘  └─────────┘              │
│                                                       │
│   Khách scan → Hệ thống TỰ BIẾT khách ngồi bàn nào   │
│   → Đơn hàng gắn với số bàn → Nhân viên mang đúng bàn │
│                                                       │
│   ⚡ KHÔNG cần tải app — Mở bằng trình duyệt Safari    │
│      hoặc Chrome trên bất kỳ điện thoại nào            │
│                                                       │
│   ⚡ Khách takeaway (mang đi): Scan QR tại quầy/cửa    │
│      → Chọn "Mang đi" → Thanh toán → Nhận đồ          │
└───────────────────────────────────────────────────────┘
```

---

## 4. ✅ Giải Quyết V2 (Chấm Công) → QR Check-in + GPS Lock

| Trước (Thủ công) | Sau (Hệ thống F&B OS) |
|---|---|
| Chấm công sổ tay / vân tay — dễ gian lận | **QR Code động** đổi mỗi 30 giây + **GPS Lock** (bán kính 50m quán) |
| Không biết ai đi muộn | Ghi nhận chính xác giờ vào/ra **từng phút**, selfie tùy chọn |
| Cuối tháng tính lương 2-3 ngày | Hệ thống **tự tính lương** theo giờ thực tế + phụ cấp |

**Kết quả:** Gian lận → 0%. Tiết kiệm 2-3 ngày tính lương/tháng.

---

## 5. ✅ Giải Quyết V3 (Kho) → Quản Lý Xuất Kho Quầy + AI Đề Xuất Nhập

| Trước (Đếm tay) | Sau (F&B OS) |
|---|---|
| Không biết nguyên liệu đi đâu | **Xuất kho quầy (Requisition):** Ghi nhận chính xác lấy bao nhiêu kg/lít từ Kho lên Quầy |
| Kiểm kê bằng sổ, sai số liệu | **Kiểm kê trên App:** Nhập số thực đếm → hệ thống tự tính chênh lệch |
| Hết hàng giữa ca | **AI đề xuất nhập hàng:** "CF hạt còn 2kg, dự kiến hết trong 2 ngày — đặt NCC trước Thứ 4" |

**Kết quả:** Thất thoát < 2%. Không hết hàng giữa ca.

---

## 6. ✅ Giải Quyết V4 (Tài Chính) → Dashboard Real-time + P&L Tự Động

| Trước (Rời rạc) | Sau (F&B OS) |
|---|---|
| Tiền mặt + chuyển khoản + MoMo nằm rải rác | **Tổng hợp real-time:** 1 dashboard duy nhất hiện tổng doanh thu từ mọi nguồn |
| Không biết lãi/lỗ | **P&L tự động:** Doanh thu − Chi phí (nguyên liệu + lương + thuê + điện) = Lợi nhuận ròng |
| Chủ chuỗi mù mờ | **So sánh chi nhánh:** Quán nào lãi nhiều? Quán nào đang "nuôi"? |

**Kết quả:** Biết chính xác lãi/lỗ từng quán mỗi ngày. Cắt lỗ kịp thời.

---

## 7. ✅ Giải Quyết V5 (Chất Lượng) → KDS Công Thức Chuẩn + QR Feedback

| Trước (Phụ thuộc barista) | Sau (F&B OS) |
|---|---|
| Barista tự nhớ công thức → pha khác nhau | **KDS hiện công thức chuẩn** cho từng ly: "Espresso 2 shot, Sữa 200ml, Đá 150g" |
| Quán Q1 khác vị quán Q3 | **Công thức đồng bộ** cả chuỗi → chuẩn vị 95%+ |
| Không biết khách nghĩ gì | **QR Feedback tại bàn:** Khách scan → đánh giá 1-5 sao → ≤ 2 sao: QL nhận alert xử lý ngay |

**Kết quả:** Đồng nhất 95%+ chất lượng. Thu thập 100% feedback khách hàng.

---

## 8. ✅ Giải Quyết V6 (Khách Hàng) → CRM Tự Động Từ QR Order + AI Churn

| Trước (Không biết khách là ai) | Sau (F&B OS) |
|---|---|
| 80% khách vô danh | **QR Order tự động thu thập:** SĐT khi thanh toán → tạo hồ sơ khách hàng |
| Thẻ tích điểm giấy (< 10% sử dụng) | **Loyalty số:** Tích điểm tự động mỗi lần đặt qua QR, nhận voucher qua Zalo |
| Không biết khách nào sắp bỏ đi | **AI Churn Prediction:** "Khách A: 45 ngày chưa quay lại → 78% risk → auto gửi voucher 30%" |

**Kết quả:** Giữ chân thêm 15-25% khách. Tăng 20% doanh thu từ khách quay lại.

---

## 9. ✅ Giải Quyết V7 (Báo Cáo) → Auto EOD Report + Dashboard Chuỗi

| Trước (Thủ công) | Sau (F&B OS) |
|---|---|
| QL đếm két, gõ tay gửi Zalo 30-60 phút | **Auto EOD Report:** Hệ thống tự tổng hợp → gửi Zalo/Email cho chủ |
| Chủ chuỗi nhận 5-10 tin Zalo mỗi tối | **1 Dashboard duy nhất:** Xem doanh thu, đơn hàng, so sánh chi nhánh real-time |
| Chênh lệch tiền mặt phát hiện trễ | **Đối soát két cuối ca:** Nhập thực đếm → cảnh báo ngay nếu chênh > 50K |

**Kết quả:** Tiết kiệm 30-60 phút/tối. Biết doanh thu real-time 24/7.

---

## 10. ✅ Giải Quyết V8 (Menu) → AI Menu Intelligence

| Trước (Cảm tính) | Sau (F&B OS) |
|---|---|
| Thêm/bỏ món theo trend bên ngoài | **AI phân tích doanh số từng món:** "Matcha +35% 4 tuần → tạo thêm biến thể" |
| Giữ món bán chậm | **AI gợi ý loại:** "Smoothie Dâu: 2 ly/ngày → đề xuất loại bỏ" |
| Khuyến mãi sai thời điểm | **AI Smart Promotion:** "14h-16h vắng nhất → push combo giảm 20% qua Zalo" |

**Kết quả:** Tăng 10-15% doanh thu. Loại bỏ món kém hiệu quả.

---
---

# 📝 PHẦN III: AI ỨNG DỤNG — CHI TIẾT KỸ THUẬT

## 11. 🤖 Tổng Hợp 5 Tính Năng AI

| # | Tên AI Feature | Bài Toán Giải Quyết | Ai Sử Dụng | Model / Thuật Toán | Ví Dụ Kết Quả |
|---|---|---|---|---|---|
| AI-1 | **Thống kê & So sánh doanh thu bằng AI** | So sánh doanh thu theo tuần/tháng/quý giữa các quán. Hỏi đáp bằng ngôn ngữ tự nhiên | 👑 Admin + 🏪 Manager | Prophet / LSTM time-series + RAG (LLM) | Admin: "So sánh Q1 vs Q3 tháng 8" → AI trả lời kèm biểu đồ. QL: "Hôm nay doanh thu bao nhiêu?" → "18.5 triệu, tăng 8% so với hôm qua" |
| AI-2 | **Gợi ý combo bán chạy** | Phân tích món nào hay mua cùng nhau → tạo combo tăng doanh thu | ⚙️ Hệ thống tự động | Association Rules (Apriori) + Collaborative Filtering | "68% khách mua Latte cũng mua Croissant → Combo 75K" |
| AI-3 | **Churn Prediction khách hàng** | Phát hiện khách sắp bỏ đi → tự động gửi voucher kéo lại | ⚙️ Tự động | Random Forest / XGBoost classification | "Khách Nguyễn A: 78% churn risk → auto gửi voucher 30% off" |
| AI-4 | **Menu Intelligence & Smart Promotion** | Phân tích món bán chạy/chậm, gợi ý giá, khuyến mãi đúng thời điểm | 👑 Admin | Time-series + Clustering + Elasticity regression | "Matcha +35% → thêm biến thể. Smoothie Dâu 2 ly/ngày → loại. 14-16h vắng → push combo" |
| AI-5 | **Chatbot Gợi Ý Món Cho Khách Hàng** | Khách hỏi chatbot trên QR Order → AI gợi ý món theo khẩu vị, thời tiết, dị ứng, trend | 👤 Khách hàng | RAG + Recommendation Engine + Content-based Filtering | Khách: "Tôi thích vị đắng, ít ngọt" → "Americano hoặc Cappuccino đường 25%". "Hôm nay nóng quá" → "Trà Đào Cam Sả đá" |

> **Lưu ý:** Nhân viên pha chế (Barista) **không cần chatbot hỏi công thức** — vì mỗi đơn hàng trên KDS đã hiển thị **công thức pha chi tiết** kèm theo (xem S-02). AI-1 (Thống kê) phục vụ cho Admin xem toàn chuỗi và Manager xem quán mình.

### Chi Tiết AI-5: Chatbot Gợi Ý Món Cho Khách Hàng

Khi khách scan QR xem menu, có nút **"🤖 Gợi ý cho tôi"** — khách bấm vào để chat với AI:

| Khách Hỏi | AI Trả Lời | Logic |
|---|---|---|
| "Tôi thích vị đắng nhẹ, ít ngọt" | "Gợi ý: Americano (0% đường) hoặc Cappuccino (đường 25%)" | Content-based filtering: tag vị đắng → filter menu |
| "Hôm nay nóng quá, gợi ý đi" | "Trà Đào Cam Sả đá ❄️ — bán chạy nhất hôm nay!" | Thời tiết API + data bán hàng real-time |
| "Món bán chạy nhất ở đây là gì?" | "Top 3 hôm nay: 1. Bạc Xỉu (42 ly) 2. Latte (38 ly) 3. Trà Đào (29 ly)" | Query trực tiếp từ data đơn hàng trong ngày |
| "Tôi bị dị ứng sữa" | Lọc menu → chỉ hiện: Americano, Trà Đào, Nước ép... (ẩn tất cả món có sữa) | Tag nguyên liệu trong menu + allergen filter |
| "Lần trước tôi uống gì?" | "Lần trước (12/07) bạn đặt Latte L + Croissant. Đặt lại nhé?" | Lịch sử đơn hàng CRM (nếu khách đã có SĐT) |
| "Combo nào tiết kiệm nhất?" | "Combo Latte + Bánh Flan: 75K (tiết kiệm 15K so với mua lẻ)" | Combo engine + price comparison |

---
---

# 📝 PHẦN IV: DỰ ÁN GIẢI QUYẾT ĐƯỢC GÌ CHO THỊ TRƯỜNG?

## 12. 🏪 Đối Với Chủ Quán Cà Phê / Chuỗi F&B

| Giá Trị | Chi Tiết |
|---|---|
| **Cắt giảm chi phí nhân sự** | Không cần thu ngân (hoặc giảm từ 2 → 0-1 người) → tiết kiệm 6-16 triệu/quán/tháng |
| **Cắt giảm chi phí POS** | Không cần mua máy POS 8-25 triệu → thay bằng QR Code (gần 0 đồng) |
| **Tăng tốc phục vụ** | Khách tự đặt 10-15 giây/đơn → phục vụ gấp 3-4 lần so với POS thủ công |
| **Giảm sai đơn về gần 0%** | Khách tự chọn trên điện thoại → không sai do giao tiếp |
| **Chống thất thoát** | Chấm công GPS + Kiểm kê cảnh báo → gian lận & thất thoát < 2% |
| **Ra quyết định bằng data** | Dashboard real-time + AI phân tích → không đoán mò |
| **Tăng doanh thu** | AI combo + Loyalty tự động + Churn prediction → +15-25% doanh thu |

## 13. 👤 Đối Với Khách Hàng

| Giá Trị | Chi Tiết |
|---|---|
| **Không xếp hàng** | Scan QR tại bàn → đặt món ngay → không cần đứng chờ |
| **Đặt đúng ý** | Tự chọn Size, Đường, Đá, Topping trên điện thoại → không sợ bị ghi sai |
| **Biết chờ bao lâu** | Hiển thị thời gian chờ ước tính (~8 phút) → không bất an, không phải hỏi nhân viên |
| **AI gợi ý món** | Hỏi chatbot "tôi thích vị đắng" → AI gợi ý ngay món phù hợp + allergen filter |
| **Gọi thêm dễ dàng** | Muốn order thêm → bấm "Gọi thêm" từ điện thoại — không cần lên quầy |
| **Thanh toán tiện lợi** | VietQR / MoMo / Tiền mặt / Split Bill chia nhóm — tùy chọn |
| **Tích điểm tự động** | Không cần thẻ giấy, không cần tải app → tích điểm ngay khi đặt qua QR |
| **Nhận ưu đãi** | Voucher sinh nhật, ưu đãi loyalty gửi qua Zalo tự động |

---
---

# 📝 PHẦN V: ĐIỂM ĐỘC ĐÁO & SO SÁNH ĐỐI THỦ

## 14. 🏆 So Sánh Với Các Giải Pháp Hiện Tại

| Tiêu Chí | iPOS / KiotViet / CukCuk | GrabFood / ShopeeFood | **F&B OS (Dự án này)** |
|---|---|---|---|
| **Đặt món** | Thu ngân gõ vào POS | Khách đặt online (giao tận nơi) | **Khách scan QR tại quán → tự đặt** |
| **Cần máy POS?** | ✅ Cần (8-25 triệu/máy) | ❌ Không | **❌ Không cần** |
| **Cần thu ngân?** | ✅ Cần (1-2 người/ca) | ❌ Không | **❌ Không cần** (hoặc 1 người hỗ trợ) |
| **Phí hàng tháng** | 250K-2 triệu/tháng | 20-30% chiết khấu/đơn | **Tự sở hữu — 0 đồng chiết khấu** |
| **AI phân tích** | ❌ Không có | ❌ Không có | **✅ 5 tính năng AI** |
| **AI gợi ý cho khách** | ❌ Không | ❌ Không | **✅ Chatbot gợi ý món theo khẩu vị** |
| **AI thống kê doanh thu** | ❌ Không | ❌ Không | **✅ AI hỏi đáp doanh thu cho Admin & Manager** |
| **CRM & Loyalty** | Cơ bản (thẻ giấy) | Không (data thuộc Grab) | **✅ CRM đầy đủ + AI Churn Prediction** |
| **Quản lý kho** | Cơ bản | ❌ Không | **✅ Xuất kho quầy + AI đề xuất nhập** |
| **KDS Bếp** | Có (một số) | ❌ Không | **✅ Có + Công thức chuẩn từng ly (kèm mỗi đơn)** |
| **Data thuộc ai?** | Thuộc nền tảng | Thuộc Grab/Shopee | **Thuộc 100% chủ quán** |

## 15. 🎯 Điểm Khác Biệt Cốt Lõi (Unique Selling Points)

| # | Điểm Độc Đáo | Tại Sao Quan Trọng |
|---|---|---|
| 1 | **QR Self-Order thay thế hoàn toàn POS** | Cắt giảm chi phí máy POS (8-25 triệu) + lương thu ngân (6-16 triệu/tháng) |
| 2 | **AI Chatbot gợi ý món cho khách** | Khách hỏi "tôi thích vị đắng" → AI gợi ý Americano. Tăng trải nghiệm + tăng giá trị đơn hàng |
| 3 | **AI Thống Kê & Hỏi Đáp Doanh Thu** | Admin/Manager hỏi AI: "So sánh Q1 vs Q3 tháng này" → có câu trả lời trong 5 giây |
| 4 | **QR Feedback + AI Menu Intelligence** | Thu thập data thật từ khách → AI phân tích → đề xuất menu tối ưu (không cảm tính) |
| 5 | **0 đồng chiết khấu** (khác Grab 20-30%) | Đơn hàng tại quán 100% doanh thu về chủ quán, không chia cho nền tảng |

---
---

# 📝 PHẦN VI: KIẾN TRÚC HỆ THỐNG & CÔNG NGHỆ

## 16. 🏗️ Kiến Trúc Tổng Thể

```
╔══════════════════════════════════════════════════════════════════════╗
║  TẦNG 1: KHÁCH HÀNG & NHÂN VIÊN (Frontend)                         ║
║                                                                      ║
║  📱 QR Order Web     📺 KDS Bếp      📱 Manager App    💻 Admin Web ║
║  (Khách scan QR      (Barista xem     (QL quán:         (Chủ chuỗi: ║
║   → menu → đặt       đơn + công      mở/kết ca,        dashboard,  ║
║   → thanh toán)      thức pha)        kho, kiểm kê)    tài chính)  ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  TẦNG 2: API & BACKEND                                              ║
║                                                                      ║
║  ┌─────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐ ║
║  │ REST API    │  │ WebSocket│  │ Auth &   │  │ Payment Gateway │ ║
║  │ (CRUD)      │  │ (Real-   │  │ RBAC     │  │ (VietQR, MoMo)  │ ║
║  │             │  │  time)   │  │          │  │                  │ ║
║  └─────────────┘  └──────────┘  └──────────┘  └──────────────────┘ ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  TẦNG 3: AI ENGINE                                                   ║
║                                                                      ║
║  ┌──────────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          ║
║  │ AI-1         │ │ AI-2     │ │ AI-3     │ │ AI-4     │          ║
║  │ Thống kê     │ │ Combo    │ │ Churn    │ │ Menu     │          ║
║  │ Doanh thu    │ │ Suggest  │ │ Predict  │ │ Intel    │          ║
║  │ (Admin + QL) │ │          │ │          │ │          │          ║
║  └──────────────┘ └──────────┘ └──────────┘ └──────────┘          ║
║  ┌──────────────────────────────────────────────────┐              ║
║  │ AI-5: Chatbot Gợi Ý Món Cho Khách Hàng          │              ║
║  │ (Khẩu vị, thời tiết, dị ứng, trend)             │              ║
║  └──────────────────────────────────────────────────┘              ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  TẦNG 4: DATABASE & INFRASTRUCTURE                                   ║
║                                                                      ║
║  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              ║
║  │ PostgreSQL   │  │ Redis Cache  │  │ Cloud Storage│              ║
║  │ (Data chính) │  │ (Real-time)  │  │ (Ảnh menu)   │              ║
║  └──────────────┘  └──────────────┘  └──────────────┘              ║
║                                                                      ║
║  Deploy: Docker + Cloud (AWS / GCP / VPS Việt Nam)                   ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 17. 🛠️ Tech Stack

| Thành Phần | Công Nghệ |
|---|---|
| **QR Order (Khách)** | Progressive Web App (PWA) — React/Next.js — Responsive Mobile-first |
| **KDS Bếp** | Web App — React — Full-screen TV mode |
| **Manager App** | Flutter (iOS + Android) hoặc React Native |
| **Admin Dashboard** | Next.js — Web Dashboard |
| **Backend API** | Node.js (NestJS) hoặc Python (FastAPI) |
| **Database** | PostgreSQL + Redis (cache & real-time) |
| **Real-time** | WebSocket (Socket.IO) — đơn hàng hiện tức thì trên KDS |
| **Thanh toán** | VietQR API (VNPay/Vietcombank) + MoMo API |
| **AI Engine** | Python (scikit-learn, Prophet, LangChain) |
| **Chatbot (Khách hàng)** | RAG (LangChain + Vector DB + LLM API) |
| **Notification** | Zalo OA API + Email (SendGrid) |
| **Deploy** | Docker + Cloud (AWS/GCP/VPS) |

---
---

# 📝 PHẦN VII: TÍNH NĂNG HỆ THỐNG CHI TIẾT THEO TỪNG ACTOR

### Tổng Quan 4 Actor

| Actor | Giao Diện | Số Tính Năng | Highlight Chính |
|---|---|---|---|
| 👤 **Khách hàng** | QR Order Web (PWA) | 24 tính năng | Order, Thanh toán, AI gợi ý, Split Bill, Loyalty |
| 🧋 **Barista / Pha chế** | KDS (TV/Tablet) | 11 tính năng | Real-time order, Công thức chuẩn kèm đơn, Báo hết món, Sơ đồ bàn |
| 🏪 **Quản lý chi nhánh** | App Mobile + Web | 13 tính năng | Ca làm việc, Nhập/Xuất kho, Báo cáo, AI thống kê |
| 👑 **Chủ chuỗi / Admin** | Web Dashboard | 22 tính năng | Dashboard, P&L, Menu, RBAC, AI thống kê, Audit Log, Export |

---

## 18. 👤 ACTOR 1: KHÁCH HÀNG (Customer)

> **Giao diện:** QR Order Web (PWA) — mở bằng trình duyệt điện thoại, KHÔNG cần tải app

### 18.1 Tính Năng Đặt Món (QR Order)

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| C-01 | **Scan QR xem menu** | Quét mã QR tại bàn/quầy → mở trang menu trên trình duyệt. Hệ thống tự nhận diện số bàn + chi nhánh |
| C-02 | **Menu trực quan** | Hiển thị menu phân loại (Cà phê / Trà / Đá xay / Bánh / Topping) kèm ảnh, giá, mô tả từng món |
| C-03 | **Tùy chỉnh món** | Chọn Size (S/M/L), mức đường (0-25-50-75-100%), mức đá (không/ít/nhiều), thêm Topping |
| C-04 | **Ghi chú đặc biệt** | Ghi chú tự do: "Ít đá, thêm shot espresso, để riêng đường" |
| C-05 | **Giỏ hàng** | Thêm nhiều món vào giỏ, chỉnh số lượng, xóa món trước khi gửi đơn |
| C-06 | **Chọn Mang đi / Tại quán** | Khách chọn "Tại bàn" (gắn số bàn) hoặc "Mang đi" (Takeaway) |

### 18.2 Tính Năng Thanh Toán

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| C-07 | **Thanh toán VietQR động** | Hệ thống tự tạo mã VietQR chứa đúng số tiền + tài khoản quán → khách scan trả → hệ thống tự xác nhận |
| C-08 | **Thanh toán MoMo / ZaloPay** | Tích hợp ví điện tử phổ biến tại VN |
| C-09 | **Thanh toán tiền mặt** | Chọn "Trả tiền mặt tại quầy" → nhân viên thu tiền sau khi nhận món |
| C-10 | **Áp mã giảm giá / Voucher** | Nhập mã voucher hoặc áp tự động nếu đủ điều kiện (Loyalty, sinh nhật, combo) |

### 18.3 Tính Năng Trải Nghiệm & AI

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| C-11 | **🤖 Chatbot gợi ý món** | Bấm "Gợi ý cho tôi" → chat với AI: hỏi theo khẩu vị, thời tiết, dị ứng, trend → AI gợi ý món phù hợp |
| C-12 | **Xem món bán chạy** | Hiển thị tag "Best Seller", "Mới", "Hot" trên menu dựa trên data bán hàng thật |
| C-13 | **Theo dõi trạng thái đơn real-time** | Sau khi đặt → thanh tiến trình: "Đã xác nhận → Đang pha chế... → Sẵn sàng! 🔔" |
| C-14 | **Thời gian chờ ước tính** | Hiển thị: "Đơn của bạn dự kiến xong sau ~8 phút" — tính từ số đơn đang chờ trên KDS |
| C-15 | **Thông báo khi món xong** | Push notification trên trình duyệt hoặc hiện trên màn hình đặt món |
| C-16 | **Gọi nhân viên** | Nút "Gọi nhân viên 🔔" trên màn hình QR → nhân viên nhận thông báo trên App: "Bàn 5 cần hỗ trợ" |
| C-17 | **QR Feedback đánh giá** | Scan QR tại bàn → đánh giá 1-5 sao **từng món** + ghi chú → gửi feedback trực tiếp |
| C-18 | **Tích điểm Loyalty tự động** | Mỗi đơn hàng tự động tích điểm theo SĐT (không cần thẻ giấy, không cần app) |
| C-19 | **Xem lịch sử đặt hàng** | Khách có SĐT → xem lại các đơn trước + đặt lại nhanh 1 click |
| C-20 | **Nhận voucher qua Zalo** | Voucher sinh nhật, ưu đãi loyalty, voucher "lâu ngày chưa ghé" — gửi tự động qua Zalo OA |

### 18.4 Tính Năng Nâng Cao (UX+)

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| C-21 | **Gọi thêm món (Add to order)** | Sau khi đặt xong, khách muốn thêm 1 ly nữa → bấm "Gọi thêm" → thêm vào đơn đang chạy, không tạo đơn mới |
| C-22 | **Allergen & Calories** | Mỗi món hiển thị: thành phần dị ứng (sữa, gluten, đậu phộng) + calories ước tính → khách sức khỏe yên tâm |
| C-23 | **Món yêu thích / Quick Reorder** | Khách lưu món hay gọi → lần sau vào QR menu hiện ngay "Món của bạn" → order 1 click |
| C-24 | **Split Bill (Chia tiền nhóm)** | Nhóm 4 người → bấm "Chia tiền" → chọn chia đều hoặc chia theo món → mỗi người nhận QR thanh toán riêng |

---

## 19. 🧋 ACTOR 2: BARISTA / PHA CHẾ (Staff)

> **Giao diện:** Màn hình KDS (Kitchen Display System) — hiển thị trên TV/Tablet tại quầy pha chế

### 19.1 Quản Lý Đơn Hàng

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| S-01 | **Xem đơn hàng real-time** | Đơn từ QR Order hiện TỨC THÌ trên KDS — không cần chờ thu ngân gõ |
| S-02 | **Hiện công thức chuẩn** | Mỗi đơn kèm công thức pha chi tiết: "Espresso 2 shot + Sữa tươi 200ml + Đá 150g + Đường 25%" |
| S-03 | **Ưu tiên đơn chờ lâu** | Đơn chờ > 3 phút → đổi màu vàng. Chờ > 5 phút → đổi màu đỏ → pha trước |
| S-04 | **Bấm "Hoàn thành"** | Pha xong → bấm nút → đơn biến mất khỏi KDS → khách nhận thông báo "Món đã sẵn sàng" |
| S-05 | **Xem ghi chú khách** | Hiện rõ ghi chú: "Ít đá", "Không đường", "Thêm shot" → không cần hỏi lại |
| S-06 | **Xem đơn gom theo bàn** | Chế độ "Bàn View": xem tất cả món bàn 5 đã order (kể cả nhiều lần) → mang 1 chuyến đủ |

### 19.2 Hỗ Trợ Vận Hành

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| S-07 | **Báo Hết Món (Out of Stock)** | Barista bấm "Hết" trên KDS → món **tự ẩn ngay lập tức** trên QR Order của khách — không cần nhờ Admin |
| S-08 | **In Bill / Receipt** | Kết nối máy in nhiệt → in hóa đơn khi khách yêu cầu (tên món, giá, tổng tiền, mã đơn) |
| S-09 | **Sơ đồ bàn (Floor Map)** | Xem trực quan bàn nào đang có khách (xanh/đỏ), bàn nào trống → ưu tiên phục vụ đúng bàn |
| S-10 | **Nhận thông báo gọi nhân viên** | Khi khách bấm "Gọi nhân viên" từ QR → nhân viên nhận chuông thông báo: "Bàn 5 cần hỗ trợ" |
| S-11 | **Chấm công QR + GPS** | Đầu ca: Scan QR động (đổi 30 giây) + GPS lock (bán kính 50m) → hệ thống ghi giờ vào/ra |

> **Lưu ý:** Barista **không cần chatbot hỏi công thức** — vì công thức pha chi tiết đã hiển thị tự động kèm mỗi đơn hàng trên KDS (xem S-02).

---

## 20. 🏪 ACTOR 3: QUẢN LÝ CHI NHÁNH (Branch Manager)

> **Giao diện:** App Manager (Mobile) + Web (giới hạn quyền — chỉ xem quán mình)

### 20.1 Quản Lý Ca Làm Việc

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| M-01 | **Mở ca / Kết ca** | Bấm "Mở Ca" đầu ngày → nhập tiền mặt đầu két. "Kết Ca" cuối ngày → nhập tiền thực đếm |
| M-02 | **Đối soát két tiền** | Hệ thống so sánh: Tiền mặt hệ thống ghi vs Thực đếm → cảnh báo nếu chênh > 50K |
| M-03 | **Duyệt lịch ca** | Xem bảng ca tuần → duyệt / đổi ca / thêm NV thay thế |
| M-04 | **Xem chấm công NV** | Danh sách NV đã check-in/check-out → ai đi muộn, ai làm overtime |

### 20.2 Quản Lý Kho & Nguyên Liệu

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| M-05 | **Xuất kho quầy** | Tạo phiếu xuất: "Xuất 2kg CF hạt + 5 hộp sữa từ Kho → Quầy" → hệ thống trừ kho tổng |
| M-06 | **Kiểm kê** | Nhập số thực đếm từng loại nguyên liệu → hệ thống tính chênh lệch tự động |
| M-07 | **Nhận cảnh báo kho** | "CF hạt còn 1.2kg — dự kiến hết trong 1 ngày" → nhập hàng kịp thời |

### 20.3 Xem Báo Cáo & AI

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| M-08 | **Xem doanh thu ca/ngày** | Doanh thu, số đơn, trung bình/đơn, top món bán chạy — **chỉ của quán mình** |
| M-09 | **Biểu đồ doanh thu theo giờ** | Chart hiển thị giờ nào đông (đơn nhiều), giờ nào vắng → QL xếp ca đúng người đúng lúc |
| M-10 | **Nhận báo cáo EOD tự động** | Cuối ca → hệ thống tự gửi báo cáo qua Zalo/Email → không cần gõ tay |
| M-11 | **🤖 AI Thống kê doanh thu (AI-1)** | Hỏi AI bằng ngôn ngữ tự nhiên: "Hôm nay doanh thu bao nhiêu?" "Hao hụt tháng này?" → AI trả lời tức thì (chỉ xem data quán mình) |

### 20.4 Quản Lý Kho Nâng Cao

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| M-12 | **Nhập kho từ NCC (Goods Receipt)** | Khi NCC giao hàng: QL nhập phiếu "Nhận 10kg CF hạt + 50 hộp sữa" → kho tổng cộng số thêm. Đối chiếu với đơn đặt hàng |
| M-13 | **Quản lý Sơ Đồ Bàn** | Cấu hình bàn của quán (bàn 1-20, khu vực: Trong/Ngoài/VIP) → dùng cho KDS Floor Map và QR Order theo bàn |

---

## 21. 👑 ACTOR 4: CHỦ CHUỖI / ADMIN (Owner)

> **Giao diện:** Web Dashboard (Desktop/Laptop) — toàn quyền xem và quản lý cả chuỗi

### 21.1 Dashboard Tổng Quan (Real-time)

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| A-01 | **Dashboard 3 quán** | Xem doanh thu, số đơn, nhân viên, cảnh báo — tất cả 3 quán trên 1 màn hình |
| A-02 | **So sánh chi nhánh** | Biểu đồ so sánh: Quán nào doanh thu cao nhất? Quán nào chi phí cao bất thường? |
| A-03 | **P&L (Lãi/Lỗ) tự động** | Doanh thu − Chi phí (nguyên liệu + lương + thuê + điện) = Lợi nhuận ròng từng quán |
| A-04 | **Cảnh báo real-time** | NV vắng không báo, két chênh lệch, kho sắp hết, feedback ≤ 2 sao → thông báo tức thì |

### 21.2 Quản Lý Menu & Giá

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| A-05 | **Tạo / Sửa / Xóa menu** | Tạo món mới kèm ảnh, giá, mô tả, công thức pha → đồng bộ cả chuỗi |
| A-06 | **Giá theo chi nhánh** | Latte Quán Q1 (trung tâm): 55K. Quán Thủ Đức: 45K — tùy chỉnh riêng |
| A-07 | **Bật/Tắt món tức thì** | Hết sữa → tắt tất cả món có sữa ngay lập tức trên QR Order |
| A-08 | **Menu mùa / Giới hạn** | Tạo menu "Mùa hè 2026" → tự bật/tắt theo ngày đã đặt |
| A-09 | **Quản lý Combo** | Tạo combo: Latte + Croissant = 75K (tiết kiệm 15K) → hiện trên QR Order |

### 21.3 Quản Lý Nhân Sự & CRM

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| A-10 | **Quản lý NV toàn chuỗi** | Thêm/sửa/xóa nhân viên, phân quyền, xem chấm công 3 quán |
| A-11 | **Quản lý Loyalty** | Cấu hình chương trình tích điểm, tạo voucher, thiết lập hạng thành viên |
| A-12 | **Quản lý Promotion** | Tạo khuyến mãi: giảm 20% khung 14-16h, Buy 1 Get 1, voucher sinh nhật |

### 21.4 AI & Phân Tích

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| A-13 | **🤖 AI Thống kê doanh thu (AI-1)** | Hỏi AI bằng ngôn ngữ tự nhiên: "So sánh Q1 vs Q3 tháng 8" "Quán nào lãi nhất?" → AI trả lời kèm biểu đồ (xem toàn chuỗi) |
| A-14 | **🤖 AI Menu Intelligence (AI-4)** | AI gợi ý: "Matcha tăng 35% → thêm biến thể", "Smoothie Dâu 2 ly/ngày → loại" |
| A-15 | **🤖 AI Churn Prediction (AI-3)** | Danh sách khách có nguy cơ bỏ đi + hệ thống tự gửi voucher kéo lại |
| A-16 | **🤖 AI Combo Suggest (AI-2)** | AI phân tích: "68% khách mua Latte cũng mua Croissant → tạo combo 75K" |

### 21.5 Quản Trị & Bảo Mật Hệ Thống

| # | Tính Năng | Mô Tả Chi Tiết |
|---|---|---|
| A-18 | **Export Báo Cáo (Excel / PDF)** | Xuất báo cáo doanh thu, lương, kho theo tháng/quý → file Excel/PDF gửi kế toán |
| A-19 | **Audit Log (Nhật Ký Thao Tác)** | Ghi lại mọi thao tác: ai sửa giá, ai xóa đơn, ai đổi menu — lúc nào, IP nào → chống gian lận nội bộ |
| A-20 | **Giờ Hoạt Động (Business Hours)** | Cài giờ mở/đóng cửa từng quán → QR Order tự hiện thông báo "Quán đã đóng cửa" ngoài giờ hoạt động |
| A-21 | **RBAC — Phân Quyền Chi Tiết** | Cấu hình quyền theo chức năng: QL chỉ xem kho + doanh thu quán mình, không thấy lương toàn chuỗi |
| A-22 | **Broadcast Notification** | Gửi thông báo đến tất cả nhân viên/quản lý cùng lúc: "Hôm nay đóng cửa sớm 8h — Kiểm kê tháng" |

---

## 22. 📊 BẢNG TỔNG HỢP: VẤN ĐỀ → GIẢI PHÁP → CÔNG NGHỆ → KẾT QUẢ

| Vấn Đề | Giải Pháp | Công Nghệ | Kết Quả |
|---|---|---|---|
| POS lỗi thời, xếp hàng, sai đơn | **QR Self-Order** — khách scan QR tự đặt món | PWA + WebSocket + VietQR | Không cần máy POS, không cần thu ngân, sai đơn → 0% |
| Khách không biết chọn gì | **AI Chatbot gợi ý** theo khẩu vị, thời tiết, dị ứng | RAG + Recommendation Engine | Tăng trải nghiệm + tăng giá trị đơn hàng |
| Chấm công gian lận | QR động + GPS Lock | QR Code + Geolocation API | Gian lận → 0%, tiết kiệm 2-3 ngày tính lương |
| Thất thoát nguyên liệu 5-15% | Xuất kho quầy + Kiểm kê + AI cảnh báo | Inventory module | Thất thoát < 2%, không hết hàng giữa ca |
| Không biết lợi nhuận thật | Dashboard tài chính real-time + P&L | Analytics + Dashboard | Biết lãi/lỗ từng quán mỗi ngày |
| Chất lượng không đồng nhất | KDS công thức chuẩn + QR Feedback | KDS Web App + Feedback module | 95%+ chuẩn vị, thu thập 100% feedback |
| Khách bỏ đi không biết | CRM tự động từ QR Order + AI Churn | CRM + XGBoost | Giữ thêm 15-25% khách |
| Báo cáo cuối ngày thủ công | Auto EOD Report + Dashboard chuỗi | Auto aggregation + Push Zalo | Tiết kiệm 30-60 phút/tối |
| Thêm/bỏ món theo cảm tính | AI Menu Intelligence + Smart Promotion | Time-series + Clustering | Tăng 10-15% doanh thu, loại món kém |

---

> **Tóm lại:** Smart F&B Operating System **thay thế hoàn toàn hệ thống POS truyền thống** bằng **QR Self-Order** — khách tự đặt món trên điện thoại, tự thanh toán, đơn bay thẳng vào bếp. Tích hợp **5 AI features**: chatbot gợi ý món cho khách theo khẩu vị, AI thống kê doanh thu cho Admin & Manager, gợi ý combo, dự đoán khách sắp bỏ đi, và tối ưu menu tự động. Barista không cần chatbot — công thức pha chi tiết đã hiển thị tự động kèm mỗi đơn trên KDS. Hệ thống phục vụ **4 nhóm người dùng** với tổng cộng **69 tính năng** — Khách hàng (24), Barista (11), Quản lý (13), Chủ chuỗi (21). Không cần máy POS đắt tiền, không cần thu ngân, không chiết khấu 20-30% như Grab — **100% doanh thu về chủ quán**.

