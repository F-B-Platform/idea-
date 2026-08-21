# 👥 CÁC ACTOR TRONG HỆ THỐNG SMART F&B OS

> Tài liệu mô tả chi tiết 4 nhóm người dùng (Actor) trong hệ thống, vai trò, quyền hạn, giao diện sử dụng và các tính năng tương ứng.

---

## 📋 TỔNG QUAN ACTOR

| # | Actor | Vai Trò | Giao Diện | Số Tính Năng |
|---|---|---|---|---|
| 1 | 👤 **Khách hàng** | Người đặt món, thanh toán, feedback | QR Order Web (PWA) trên trình duyệt | 24 |
| 2 | 🧋 **Barista / Phục vụ** | Nhận đơn, pha chế, phục vụ, chấm công | KDS (TV/Tablet) + Staff App (Mobile) | 12 |
| 3 | 🏪 **Quản lý chi nhánh** | Quản lý ca, kho, báo cáo chi nhánh | App Manager (Mobile) + Web (giới hạn quyền) | 13 |
| 4 | 👑 **Chủ chuỗi / Admin** | Quản trị toàn bộ chuỗi, AI phân tích | Web Dashboard (Desktop/Laptop) — toàn quyền | 22 |

> **Tổng cộng:** 4 Actor | 71 tính năng | 5 AI Module

---

## 📐 SƠ ĐỒ QUAN HỆ GIỮA CÁC ACTOR

```
                    ┌───────────────────────────┐
                    │      SMART F&B OS         │
                    │   (Backend + AI Engine)   │
                    └─────────────┬─────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
   ┌────▼────┐            ┌───────▼───────┐          ┌──────▼──────┐
   │ 👤 KHÁCH │            │ 🧋 BARISTA     │          │ 🏪 QUẢN LÝ  │
   │ HÀNG    │            │ / PHA CHẾ     │          │ CHI NHÁNH   │
   └────┬────┘            └───────┬───────┘          └──────┬──────┘
        │                         │                         │
        │   Scan QR → Đặt món    │   Nhận đơn real-time    │   Mở/kết ca
        │   Nhập SĐT → CRM      │   Xem công thức pha     │   Nhập/Xuất kho
        │   AI Chatbot gợi ý     │   Báo hết món           │   Kiểm kê
        │   Yêu cầu bill → NV   │   In bill, thu tiền     │   Xem báo cáo
        │   Feedback / Loyalty   │   Chấm công             │   AI Thống kê
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                          ┌───────▼───────┐
                          │ 👑 ADMIN       │
                          │ (Chủ chuỗi)  │
                          └───────┬───────┘
                                  │
                     • Dashboard toàn chuỗi real-time
                     • P&L (Lãi/Lỗ) tự động
                     • Quản lý Menu/Giá/Combo
                     • CRM & Loyalty
                     • RBAC phân quyền
                     • AI Thống kê (AI-1)
                     • AI Combo Suggest (AI-2)
                     • AI Churn Prediction (AI-3)
                     • AI Menu Intelligence (AI-4)
```

---

## 1. 👤 ACTOR 1: KHÁCH HÀNG (Customer)

### Mô tả vai trò
Khách hàng là người sử dụng cuối cùng — đến quán, quét QR tại bàn, tự đặt món trên trình duyệt điện thoại. **Không cần tải app**, hệ thống là PWA mở trên trình duyệt.

### Giao diện
- **QR Order Web (PWA)** — mở bằng trình duyệt điện thoại

### Luồng tương tác chính
```
Scan QR tại bàn
      │
      ▼
Nhập SĐT (nhận diện khách)
  ├── Lần đầu → Nhập thêm Tên → Tạo hồ sơ CRM
  └── Khách quen → Hiện tên, điểm loyalty, món hay gọi
      │
      ▼
Xem Menu → Chọn món → Tùy chỉnh (Size/Đường/Đá/Topping) → Gửi đơn
      │
      ▼
Theo dõi trạng thái đơn real-time ("Đang pha chế..." → "Sẵn sàng! 🔔")
      │
      ▼
Nhận món → Yêu cầu thanh toán (NV mang bill hoặc ra quầy)
      │
      ▼
Feedback đánh giá từng món → Tích điểm Loyalty tự động
```

### Danh sách tính năng (24 tính năng)

| Nhóm | # | Tính Năng | Mô Tả |
|---|---|---|---|
| **Nhận diện** | C-00 | Nhận diện SĐT | Scan QR → nhập SĐT → lần đầu thêm Tên, quen thì nạp hồ sơ CRM |
| **Đặt món** | C-01 | Scan QR xem menu | Quét QR tại bàn → mở menu trên trình duyệt, tự nhận diện bàn + chi nhánh |
| | C-02 | Menu trực quan | Phân loại (Cà phê / Trà / Đá xay / Bánh) kèm ảnh, giá, mô tả |
| | C-03 | Tùy chỉnh món | Size (S/M/L), Đường (0-100%), Đá, Topping |
| | C-04 | Ghi chú đặc biệt | Ghi chú tự do: "Ít đá, thêm shot espresso" |
| | C-05 | Giỏ hàng | Thêm nhiều món, chỉnh số lượng, xóa trước khi gửi |
| | C-06 | Chọn Mang đi / Tại quán | "Tại bàn" (gắn số bàn) hoặc "Mang đi" (Takeaway) |
| **Thanh toán** | C-07 | Yêu cầu in bill | Bấm "💳 Yêu cầu thanh toán" → NV nhận alert → mang bill ra bàn |
| | C-08 | Thanh toán tại bàn | NV đưa bill → Tiền mặt hoặc VietQR → NV xác nhận |
| | C-09 | Thanh toán tại quầy | Khách tự ra quầy trả → NV xác nhận |
| | C-10 | Áp mã giảm giá | Khách báo mã voucher → NV nhập → giảm tự động |
| | C-11 | Cập nhật doanh thu real-time | Xác nhận thanh toán → dashboard Admin/Manager cập nhật tức thì |
| **Trải nghiệm** | C-12 | 🤖 Chatbot AI gợi ý | Chat với AI: khẩu vị, thời tiết, dị ứng → gợi ý món phù hợp |
| | C-13 | Xem món bán chạy | Tag "Best Seller", "Mới", "Hot" trên menu |
| | C-14 | Theo dõi trạng thái đơn | Thanh tiến trình real-time: "Đã xác nhận → Đang pha chế → Sẵn sàng 🔔" |
| | C-15 | Thời gian chờ ước tính | "Dự kiến xong sau ~8 phút" |
| | C-16 | Thông báo khi món xong | Push notification trên trình duyệt |
| | C-17 | Gọi nhân viên | Nút "Gọi nhân viên 🔔" → NV nhận alert "Bàn 5 cần hỗ trợ" |
| | C-18 | QR Feedback & Review công khai | Scan QR/uống xong → đánh giá 1-5 sao + **tải ảnh thực tế** + tùy chọn **Ẩn danh** + **Publish công khai** lên QR menu |
| **CRM & Loyalty** | C-19 | Tích điểm Loyalty | Tự động cộng điểm vào SĐT khi hoàn tất đơn |
| | C-20 | Lưu lịch sử uống & CRM | Ghi lại: món đã gọi, số lần ghé, ngày cuối, tổng chi tiêu |
| | C-21 | Nhận voucher qua Zalo | Voucher sinh nhật, loyalty, "lâu ngày chưa ghé" → gửi tự động |
| **Nâng cao** | C-22 | Gọi thêm món | Thêm vào đơn đang chạy, không tạo đơn mới |
| | C-23 | Allergen & Calories | Hiện thành phần dị ứng + calories từng món |
| | C-24 | Món yêu thích / Quick Reorder | Dựa CRM hiện "Món của bạn" → order 1 click |

---

## 2. 🧋 ACTOR 2: BARISTA / PHỤC VỤ (Staff)

### Mô tả vai trò
Barista và nhân viên phục vụ là lực lượng vận hành tại quán. Nhận đơn real-time qua màn hình KDS tại quầy, pha chế theo công thức chuẩn, phục vụ khách tại bàn và nhận alert từ **App Nội Bộ Nhân Viên (Staff Mobile App)**.

### Giao diện
- **KDS (Kitchen Display System)** — TV hoặc Tablet full-screen tại quầy pha chế
- **Staff Mobile App (App Nội Bộ Nhân Viên)** — Ứng dụng di động cho nhân viên phục vụ & pha chế

### Luồng tương tác chính
```
Đơn mới hiện trên KDS (real-time qua WebSocket)
      │
      ▼
Xem chi tiết đơn + CÔNG THỨC PHA (tự động kèm mỗi đơn)
      │
      ▼
Pha chế theo công thức chuẩn → Bấm "Hoàn thành" → Khách nhận 🔔
      │
      ▼
Nhận alert "Bàn X cần bill" → In bill → Mang ra bàn → Thu tiền → Xác nhận
```

### Danh sách tính năng (12 tính năng)

| Nhóm | # | Tính Năng | Mô Tả |
|---|---|---|---|
| **Đơn hàng** | S-01 | Xem đơn hàng real-time | Đơn từ QR Order hiện TỨC THÌ trên KDS |
| | S-02 | Hiện công thức chuẩn | Mỗi đơn kèm công thức pha: "Espresso 2 shot + Sữa tươi 200ml + Đá 150g + Đường 25%" |
| | S-03 | Ưu tiên đơn chờ lâu | Xanh (< 3p) → Vàng (3-5p) → Đỏ (> 5p) |
| | S-04 | Bấm "Hoàn thành" | Đơn biến mất khỏi KDS → Khách nhận thông báo |
| | S-05 | Xem ghi chú khách | Hiện rõ: "Ít đá", "Không đường", "Thêm shot" |
| | S-06 | Xem đơn gom theo bàn | "Bàn View" → mang 1 chuyến đủ cả bàn |
| **Vận hành** | S-07 | Báo Hết Món | Bấm "Hết" trên KDS → món tự ẩn ngay trên QR Order khách |
| | S-08 | In Bill / Receipt | Kết nối máy in nhiệt → in hóa đơn khi khách yêu cầu |
| | S-09 | Sơ đồ bàn (Floor Map) | Xem trực quan bàn nào có khách (xanh/đỏ), bàn nào trống |
| | S-10 | Nhận thông báo "Gọi NV" | Khách bấm "Gọi nhân viên" → chuông alert trên KDS & Staff App: "Bàn 5 cần hỗ trợ" |
| | S-11 | Chấm công đa phương thức | App: QR động + GPS Lock. Mở rộng: Máy vân tay / Face ID |
| | S-12 | App Nội Bộ Nhân Viên (Staff App) | App di động nội bộ: Rung/phát chuông alert gọi bàn 🔔/báo bill 💳, xuất mã VietQR di động, báo hết món, sơ đồ bàn |

> **Lưu ý quan trọng:** Barista **KHÔNG CẦN chatbot hỏi công thức** — vì công thức pha chi tiết đã hiển thị tự động kèm mỗi đơn hàng trên KDS (S-02).

---

## 3. 🏪 ACTOR 3: QUẢN LÝ CHI NHÁNH (Branch Manager)

### Mô tả vai trò
Quản lý chịu trách nhiệm vận hành 1 chi nhánh: mở/kết ca, đối soát két, nhập/xuất kho, kiểm kê nguyên liệu, xem báo cáo doanh thu. **Chỉ xem data của quán mình**, không thấy quán khác hay lương toàn chuỗi.

### Giao diện
- **App Manager (Mobile)** + **Web** (giới hạn quyền — chỉ xem quán mình)

### Luồng tương tác chính
```
Mở ca đầu ngày → Nhập tiền mặt đầu két
      │
      ▼
Quản lý trong ngày:
  • Duyệt/đổi ca nhân viên
  • Xuất kho quầy (lấy nguyên liệu từ Kho lớn → Quầy pha)
  • Nhận hàng từ NCC (Nhập kho)
  • Kiểm kê nguyên liệu
  • Xem báo cáo doanh thu
  • Hỏi AI thống kê ("Hôm nay bán bao nhiêu?")
      │
      ▼
Kết ca cuối ngày → Đếm tiền két → Hệ thống đối soát chênh lệch
```

### Danh sách tính năng (13 tính năng)

| Nhóm | # | Tính Năng | Mô Tả |
|---|---|---|---|
| **Ca làm** | M-01 | Mở ca / Kết ca | Nhập tiền đầu két (mở ca), đếm tiền thực (kết ca) |
| | M-02 | Đối soát két tiền | So sánh: tiền hệ thống ghi vs thực đếm → cảnh báo chênh > 50K |
| | M-03 | Duyệt lịch ca | Xem bảng ca tuần → duyệt / đổi ca / thêm NV thay thế |
| | M-04 | Xem chấm công NV | Danh sách NV check-in/check-out → ai đi muộn, ai overtime |
| **Kho hàng** | M-05 | Xuất kho quầy | Tạo phiếu xuất: "Xuất 2kg CF hạt + 5 hộp sữa từ Kho → Quầy" |
| | M-06 | Kiểm kê | Nhập số thực đếm → hệ thống tính chênh lệch tự động |
| | M-07 | Nhận cảnh báo kho | "CF hạt còn 1.2kg — dự kiến hết trong 1 ngày" |
| | M-12 | Nhập kho từ NCC | Khi NCC giao hàng → nhập phiếu → đối chiếu với đơn đặt hàng |
| **Báo cáo** | M-08 | Xem doanh thu ca/ngày | Doanh thu, số đơn, trung bình/đơn, top món — chỉ quán mình |
| | M-09 | Biểu đồ doanh thu theo giờ | Giờ nào đông / vắng → xếp ca đúng người đúng lúc |
| | M-10 | Nhận báo cáo EOD tự động | Cuối ca → hệ thống gửi báo cáo qua Zalo/Email |
| | M-11 | 🤖 AI Thống kê (AI-1) | Hỏi AI: "Hôm nay doanh thu?" "Hao hụt tháng này?" → AI trả lời tức thì |
| **Khác** | M-13 | Quản lý Sơ đồ bàn | Cấu hình bàn quán (Trong/Ngoài/VIP) → dùng cho KDS và QR Order |

---

## 4. 👑 ACTOR 4: CHỦ CHUỖI / ADMIN (Owner)

### Mô tả vai trò
Admin là chủ sở hữu toàn bộ chuỗi quán (3 chi nhánh). Có **quyền cao nhất**: xem dashboard tất cả quán real-time, quản lý menu/giá/combo toàn chuỗi, cấu hình nhân sự + Loyalty + Promotion, và sử dụng **đầy đủ 5 AI Module** để phân tích kinh doanh.

### Giao diện
- **Web Dashboard (Desktop/Laptop)** — toàn quyền xem và quản lý cả chuỗi

### Luồng tương tác chính
```
Đăng nhập Dashboard
      │
      ▼
Xem tổng quan 3 quán real-time (doanh thu, đơn, cảnh báo)
      │
      ├── So sánh chi nhánh → P&L tự động
      ├── Quản lý Menu / Giá / Combo → đồng bộ cả chuỗi
      ├── Quản lý Nhân sự / Loyalty / Promotion
      ├── Hỏi AI Thống kê: "Quán nào lãi nhất?" → AI trả lời kèm biểu đồ
      ├── AI gợi ý: tạo Combo, loại món kém, giữ khách sắp bỏ
      └── Export Excel/PDF → gửi kế toán
```

### Danh sách tính năng (22 tính năng)

| Nhóm | # | Tính Năng | Mô Tả |
|---|---|---|---|
| **Dashboard** | A-01 | Dashboard 3 quán | Doanh thu, đơn, NV, cảnh báo — tất cả trên 1 màn hình |
| | A-02 | So sánh chi nhánh | Biểu đồ: quán nào doanh thu cao nhất? Chi phí bất thường? |
| | A-03 | P&L (Lãi/Lỗ) tự động | Doanh thu − Chi phí = Lợi nhuận ròng từng quán |
| | A-04 | Cảnh báo real-time | NV vắng, két chênh, kho hết, feedback ≤ 2 sao → alert tức thì |
| **Menu & Giá** | A-05 | Tạo/Sửa/Xóa menu | Tạo món mới kèm ảnh, giá, mô tả, công thức → đồng bộ chuỗi |
| | A-06 | Giá theo chi nhánh | Latte Q1: 55K. Thủ Đức: 45K — tùy chỉnh riêng |
| | A-07 | Bật/Tắt món tức thì | Hết sữa → tắt tất cả món có sữa ngay lập tức |
| | A-08 | Menu mùa / Giới hạn | Tạo menu mùa tự bật/tắt theo ngày đã đặt |
| | A-09 | Quản lý Combo | Tạo combo: Latte + Croissant = 75K (tiết kiệm 15K) |
| **Nhân sự & CRM** | A-10 | Quản lý NV toàn chuỗi | Thêm/sửa/xóa NV, phân quyền, xem chấm công 3 quán |
| | A-11 | Quản lý Loyalty | Cấu hình tích điểm, tạo voucher, thiết lập hạng thành viên |
| | A-12 | Quản lý Promotion | Giảm 20% khung 14-16h, Buy 1 Get 1, voucher sinh nhật |
| **AI & Phân tích** | A-13 | 🤖 AI Thống kê toàn chuỗi (AI-1) | Hỏi AI: "So sánh Q1 vs Q3 tháng 8?" → AI trả lời kèm biểu đồ |
| | A-14 | 🤖 AI Menu Intelligence (AI-4) | "Matcha tăng 35% → thêm biến thể", "Smoothie Dâu 2 ly/ngày → loại" |
| | A-15 | 🤖 AI Churn Prediction (AI-3) | Danh sách khách nguy cơ bỏ đi + tự gửi voucher kéo lại |
| | A-16 | 🤖 AI Combo Suggest (AI-2) | "68% khách mua Latte cũng mua Croissant → tạo combo 75K" |
| **Quản trị** | A-18 | Export Báo Cáo | Xuất doanh thu, lương, kho → file Excel/PDF gửi kế toán |
| | A-19 | Audit Log | Ghi lại mọi thao tác: ai sửa giá, ai xóa đơn, lúc nào, IP nào |
| | A-20 | Giờ Hoạt Động | Cài giờ mở/đóng cửa → QR Order tự hiện "Quán đã đóng cửa" |
| | A-21 | RBAC phân quyền | QL chỉ xem kho + doanh thu quán mình, không thấy lương chuỗi |
| | A-22 | Broadcast Notification | Gửi thông báo tất cả NV/QL: "Hôm nay đóng cửa sớm 8h" |

---

## 🔐 BẢNG PHÂN QUYỀN (RBAC MATRIX)

| Chức năng | 👤 Khách | 🧋 Barista | 🏪 Quản lý | 👑 Admin |
|---|---|---|---|---|
| **Xem menu & đặt món** | ✅ | ❌ | ❌ | ❌ |
| **Nhận đơn trên KDS** | ❌ | ✅ | ❌ | ❌ |
| **Báo hết món** | ❌ | ✅ | ✅ | ✅ |
| **Chấm công** | ❌ | ✅ | 🔍 Xem | 🔍 Xem |
| **Mở/Kết ca** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Xuất kho quầy** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Nhập kho NCC** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Kiểm kê** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Xem báo cáo doanh thu** | ❌ | ❌ | ✅ Quán mình | ✅ Toàn chuỗi |
| **AI Thống kê (AI-1)** | ❌ | ❌ | ✅ Quán mình | ✅ Toàn chuỗi |
| **Quản lý Menu/Giá** | ❌ | ❌ | ❌ | ✅ |
| **Tạo Combo / Khuyến mãi** | ❌ | ❌ | ❌ | ✅ |
| **AI Churn Prediction (AI-3)** | ❌ | ❌ | ❌ | ✅ |
| **AI Menu Intelligence (AI-4)** | ❌ | ❌ | ❌ | ✅ |
| **AI Combo Suggest (AI-2)** | ❌ | ❌ | ❌ | ✅ |
| **Quản lý Loyalty/Voucher** | ❌ | ❌ | ❌ | ✅ |
| **Quản lý NV toàn chuỗi** | ❌ | ❌ | ❌ | ✅ |
| **RBAC phân quyền** | ❌ | ❌ | ❌ | ✅ |
| **Audit Log** | ❌ | ❌ | ❌ | ✅ |
| **Export Excel/PDF** | ❌ | ❌ | ❌ | ✅ |

> 🔑 **Nguyên tắc phân quyền:** Mỗi Actor chỉ thấy và thao tác được những gì thuộc phạm vi vai trò. Quản lý chỉ xem data quán mình. Admin xem toàn chuỗi. Barista chỉ tương tác với KDS. Khách chỉ dùng QR Order PWA.

---

## 🤖 AI MODULE — ACTOR NÀO DÙNG AI NÀO?

| AI Module | Mô Tả | Actor Sử Dụng |
|---|---|---|
| **AI-1** — Thống kê doanh thu | Hỏi AI bằng ngôn ngữ tự nhiên, AI trả lời kèm biểu đồ | 🏪 Quản lý (quán mình) + 👑 Admin (toàn chuỗi) |
| **AI-2** — Combo Suggest | Phân tích data bán hàng → gợi ý combo có conversion cao | 👑 Admin |
| **AI-3** — Churn Prediction | Dự đoán khách sắp bỏ đi → tự gửi voucher giữ chân | 👑 Admin (cấu hình) → ⚙️ Tự động chạy |
| **AI-4** — Menu Intelligence | Phân tích trend món → gợi ý thêm/loại/thay đổi menu | 👑 Admin |
| **AI-5** — Chatbot gợi ý món | Chat với AI: khẩu vị, thời tiết, dị ứng → gợi ý món | 👤 Khách hàng |

> **Barista KHÔNG dùng AI.** Công thức pha đã hiển thị tự động kèm mỗi đơn trên KDS.

---

## 📊 THỐNG KÊ SỐ LIỆU

| Chỉ Tiêu | Giá Trị |
|---|---|
| Tổng số Actor | **4** (Khách, Barista, Quản lý, Admin) |
| Tổng số tính năng | **71** (24 + 12 + 13 + 22) |
| Tổng AI Module | **5** (Thống kê, Combo, Churn, Menu Intel, Chatbot) |
| Actor dùng AI nhiều nhất | 👑 Admin (4 AI: AI-1, AI-2, AI-3, AI-4) |
| Actor có nhiều tính năng nhất | 👤 Khách hàng (24 tính năng) |
| Actor có quyền cao nhất | 👑 Admin (toàn quyền chuỗi + RBAC) |
