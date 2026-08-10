# 👥 HỆ THỐNG SMART F&B OS — AI LÀM GÌ, CON NGƯỜI LÀM GÌ?

> **Tài liệu giới thiệu cho Khách hàng**  
> Mô tả 4 nhóm người dùng trong hệ thống, mỗi người sẽ **thấy gì, làm gì, và được hỗ trợ gì** từ hệ thống thông minh.

---

## 📋 TỔNG QUAN: 4 NHÓM NGƯỜI DÙNG

| # | Ai? | Làm gì? | Dùng thiết bị gì? | Số tính năng |
|---|---|---|---|---|
| 1 | 👤 **Khách hàng** | Quét QR đặt món, thanh toán, đánh giá | **Điện thoại cá nhân** (trình duyệt, không cần tải app) | 24 |
| 2 | 🧋 **Nhân viên pha chế / Phục vụ** | Nhận đơn, pha chế, mang bill, chấm công | **TV/Màn hình tại quầy** + **App trên điện thoại NV** | 12 |
| 3 | 🏪 **Quản lý chi nhánh** | Mở/kết ca, quản lý kho, xem doanh thu | **App trên điện thoại** + Web | 13 |
| 4 | 👑 **Chủ chuỗi (Admin)** | Quản lý toàn bộ chuỗi, phân tích AI | **Máy tính / Laptop** (Website Dashboard) | 22 |

> **Tổng cộng:** 71 tính năng + 5 Module AI thông minh

---

## 📐 MỐI QUAN HỆ GIỮA CÁC NHÓM NGƯỜI DÙNG

```
     👤 KHÁCH HÀNG                🧋 NHÂN VIÊN                🏪 QUẢN LÝ
     (Điện thoại)                (TV quầy + ĐT)              (ĐT + Web)
          │                           │                          │
  Quét QR → Đặt món           Nhận đơn tức thì           Mở ca / Kết ca
  Nhập SĐT → Tích điểm       Pha chế theo công thức     Nhập/Xuất kho
  Chat AI → Gợi ý món         Mang bill / Thu tiền       Xem doanh thu
  Đánh giá → Feedback         Chấm công bằng App        Hỏi AI thống kê
          │                           │                          │
          └───────────────────────────┼──────────────────────────┘
                                      │
                              👑 CHỦ CHUỖI (ADMIN)
                              (Website trên máy tính)
                                      │
                         • Xem doanh thu 3 quán cùng lúc
                         • Quản lý menu, giá, combo cả chuỗi
                         • AI dự đoán khách sắp bỏ quán
                         • AI gợi ý combo bán chạy
                         • AI phân tích menu nên giữ/loại
                         • Xuất báo cáo gửi kế toán
```

---

## 1. 👤 KHÁCH HÀNG — Tự đặt món trên điện thoại

> **Không cần tải app** — chỉ cần quét QR bằng camera điện thoại, menu hiện trên trình duyệt.

### Khách đến quán sẽ trải qua các bước sau:

```
📱 Quét QR tại bàn
      │
      ▼
📞 Nhập số điện thoại
   ├── Lần đầu → Nhập thêm Tên → Hệ thống tạo hồ sơ khách hàng
   └── Lần sau → Hệ thống nhận diện → Hiện tên, điểm tích lũy, món hay gọi
      │
      ▼
📋 Xem menu → Chọn món → Tùy chỉnh (Size / Đường / Đá / Topping)
      │
      ▼
⏳ Theo dõi trạng thái đơn ("Đang pha chế..." → "Sẵn sàng! 🔔")
      │
      ▼
💳 Yêu cầu thanh toán → NV mang bill ra bàn hoặc khách ra quầy
      │
      ▼
⭐ Đánh giá trải nghiệm → Tự động tích điểm Loyalty
```

### 24 tính năng cho Khách hàng

| Nhóm | Tính Năng | Khách hàng được gì? |
|---|---|---|
| **Nhận diện** | Nhận diện SĐT | Nhập SĐT → hệ thống nhớ tên, điểm tích lũy, món hay gọi |
| **Đặt món** | Scan QR xem menu | Quét QR tại bàn → mở menu ngay trên trình duyệt |
| | Menu trực quan | Ảnh đẹp, phân loại rõ ràng (Cà phê / Trà / Bánh) |
| | Tùy chỉnh món | Chọn Size, Đường, Đá, Topping theo ý muốn |
| | Ghi chú đặc biệt | "Ít đá", "Thêm shot espresso", "Không đường" |
| | Giỏ hàng | Thêm nhiều món, chỉnh số lượng trước khi gửi |
| | Mang đi / Tại quán | Chọn "Tại bàn" hoặc "Mang đi" |
| **Thanh toán** | Yêu cầu in bill | Bấm nút → nhân viên tự mang bill ra bàn |
| | Thanh toán tại bàn | Tiền mặt hoặc chuyển khoản (VietQR) → NV xác nhận |
| | Thanh toán tại quầy | Tự ra quầy trả tiền |
| | Áp mã giảm giá | Báo mã voucher cho NV → giảm giá tự động |
| | Doanh thu cập nhật tức thì | Thanh toán xong → chủ quán thấy doanh thu ngay trên Dashboard |
| **Trải nghiệm** | 🤖 Chat AI gợi ý | Chat với AI: "Tôi muốn uống gì ngọt mát?" → AI gợi ý món phù hợp |
| | Món bán chạy | Tag "Best Seller", "Mới", "Hot" giúp chọn nhanh |
| | Theo dõi trạng thái đơn | Thanh tiến trình: "Đã xác nhận → Đang pha → Sẵn sàng 🔔" |
| | Thời gian chờ | "Dự kiến xong sau ~8 phút" |
| | Thông báo khi xong | Điện thoại báo: "Món của bạn đã sẵn sàng!" |
| | Gọi nhân viên | Bấm nút 🔔 → NV nhận thông báo: "Bàn 5 cần hỗ trợ" |
| | Đánh giá & Review | Đánh giá 1-5 sao từng món + chụp ảnh + tùy chọn ẩn danh. Review hiển thị công khai cho khách sau tham khảo |
| **Tích điểm** | Loyalty tự động | Mỗi đơn hoàn tất → tự động cộng điểm vào SĐT |
| | Lưu lịch sử | Hệ thống nhớ: món đã gọi, số lần ghé, tổng chi tiêu |
| | Nhận voucher Zalo | Voucher sinh nhật, "lâu ngày chưa ghé" → gửi tự động qua Zalo |
| **Nâng cao** | Gọi thêm món | Thêm vào đơn đang chạy, không cần tạo đơn mới |
| | Dị ứng & Calories | Hiện thành phần dị ứng + calories từng món |
| | Món yêu thích | Hiện "Món của bạn" dựa lịch sử → đặt lại 1 click |

---

## 2. 🧋 NHÂN VIÊN PHA CHẾ / PHỤC VỤ — Nhận đơn tự động, không cần nhớ

> **2 màn hình làm việc:** TV tại quầy (hiện đơn hàng) + App trên điện thoại NV (nhận chuông, mang bill)

### Quy trình làm việc:

```
📺 Đơn mới hiện trên TV tại quầy (tức thì, không cần ai báo)
      │
      ▼
📝 Xem chi tiết: tên món + CÔNG THỨC PHA kèm sẵn
      │
      ▼
☕ Pha chế theo công thức → Bấm "Hoàn thành" → Khách nhận 🔔
      │
      ▼
📱 ĐT rung: "Bàn 5 cần bill" → In bill → Mang ra bàn → Thu tiền → Xác nhận
```

### 12 tính năng cho Nhân viên

| Nhóm | Tính Năng | NV được hỗ trợ gì? |
|---|---|---|
| **Đơn hàng** | Đơn hiện tức thì trên TV | Khách đặt xong → đơn hiện ngay trên TV quầy, không cần ai nhận |
| | Công thức pha kèm sẵn | Mỗi đơn kèm công thức: "Espresso 2 shot + Sữa 200ml + Đá 150g + Đường 25%" |
| | Ưu tiên đơn chờ lâu | Xanh (< 3 phút) → Vàng (3-5p) → Đỏ (> 5p) — biết đơn nào cần pha gấp |
| | Bấm "Hoàn thành" | Pha xong → bấm → khách nhận thông báo trên ĐT |
| | Ghi chú khách | Hiện rõ: "Ít đá", "Không đường", "Thêm shot" |
| | Gom đơn theo bàn | Xem tất cả món của 1 bàn → mang 1 chuyến đủ hết |
| **Vận hành** | Báo hết món | Bấm "Hết" → món tự ẩn ngay trên menu của khách |
| | In bill | Kết nối máy in → in hóa đơn khi khách yêu cầu |
| | Sơ đồ bàn | Xem bàn nào có khách (đỏ), bàn nào trống (xanh) |
| | Chuông gọi nhân viên | Khách bấm "Gọi NV" → ĐT rung + chuông: "Bàn 5 cần hỗ trợ" |
| | Chấm công | Mở app → Quét QR + GPS xác nhận vị trí → Check-in/out |
| | App NV trên điện thoại | App nội bộ: nhận chuông 🔔, mang bill 💳, báo hết món, xem sơ đồ bàn |

> **Lưu ý:** NV **không cần nhớ công thức** — công thức pha hiện tự động kèm mỗi đơn trên TV.

---

## 3. 🏪 QUẢN LÝ CHI NHÁNH — Quản lý quán từ điện thoại

> **Chỉ xem được data của quán mình**, không thấy quán khác hay lương toàn chuỗi.

### Một ngày làm việc của Quản lý:

```
☀️ Sáng: Mở ca → Nhập tiền đầu két
      │
      ▼
🏪 Trong ngày:
   • Duyệt lịch ca / đổi ca nhân viên
   • Xuất nguyên liệu từ kho → quầy pha chế
   • Nhận hàng từ nhà cung cấp → nhập kho
   • Kiểm kê nguyên liệu
   • Hỏi AI: "Hôm nay bán bao nhiêu?" → AI trả lời tức thì
      │
      ▼
🌙 Tối: Kết ca → Đếm tiền két → Hệ thống tự so sánh chênh lệch
```

### 13 tính năng cho Quản lý

| Nhóm | Tính Năng | Quản lý được gì? |
|---|---|---|
| **Ca làm** | Mở ca / Kết ca | Nhập tiền đầu két (mở ca), đếm tiền thực (kết ca) |
| | Đối soát két tiền | Hệ thống so sánh: tiền máy tính vs tiền thực đếm → cảnh báo nếu chênh > 50K |
| | Duyệt lịch ca | Xem bảng ca tuần → duyệt / đổi ca / thêm NV thay thế |
| | Xem chấm công NV | Ai đi đúng giờ, ai trễ, ai overtime — tất cả trên ĐT |
| **Kho hàng** | Xuất kho quầy | "Xuất 2kg cà phê hạt + 5 hộp sữa từ Kho → Quầy pha" |
| | Kiểm kê | Nhập số thực đếm → hệ thống tự tính chênh lệch |
| | Cảnh báo kho | "Cà phê hạt còn 1.2kg — dự kiến hết trong 1 ngày" |
| | Nhận hàng từ NCC | NCC giao hàng → nhập phiếu → đối chiếu với đơn đặt |
| **Báo cáo** | Doanh thu ca/ngày | Doanh thu, số đơn, trung bình/đơn, top món — chỉ quán mình |
| | Biểu đồ theo giờ | Giờ nào đông / vắng → xếp ca đúng người đúng lúc |
| | Báo cáo tự động | Cuối ca → hệ thống gửi báo cáo qua Zalo/Email cho QL |
| | 🤖 Hỏi AI thống kê | "Doanh thu hôm nay?" "Hao hụt tháng này?" → AI trả lời ngay |
| **Khác** | Sơ đồ bàn | Cấu hình bàn quán: Trong / Ngoài / VIP |

---

## 4. 👑 CHỦ CHUỖI (ADMIN) — Quản lý tất cả từ 1 màn hình

> **Quyền cao nhất:** xem tất cả quán real-time, quản lý menu/giá/combo toàn chuỗi, sử dụng 5 AI Module.

### Chủ chuỗi dùng hệ thống để:

```
💻 Mở Dashboard trên máy tính
      │
      ▼
📊 Xem tổng quan 3 quán cùng lúc (doanh thu, đơn, cảnh báo)
      │
      ├── So sánh chi nhánh: Quán nào lãi nhất? Chi phí bất thường?
      ├── Quản lý Menu / Giá / Combo → thay đổi đồng bộ cả 3 quán
      ├── Quản lý nhân sự / Loyalty / Khuyến mãi
      ├── Hỏi AI: "Quán nào lãi nhất tháng này?" → AI trả lời kèm biểu đồ
      ├── AI gợi ý: tạo combo mới, loại món kém, giữ khách sắp bỏ
      └── Xuất báo cáo Excel/PDF → gửi kế toán
```

### 22 tính năng cho Chủ chuỗi

| Nhóm | Tính Năng | Chủ chuỗi được gì? |
|---|---|---|
| **Dashboard** | Dashboard 3 quán | Doanh thu, đơn, NV, cảnh báo — tất cả trên 1 màn hình |
| | So sánh chi nhánh | Biểu đồ: quán nào doanh thu cao nhất? Chi phí bất thường? |
| | Lãi/Lỗ tự động | Doanh thu − Chi phí = Lợi nhuận ròng từng quán, tự tính |
| | Cảnh báo real-time | NV vắng, két chênh, kho hết, feedback kém → báo tức thì |
| **Menu & Giá** | Tạo/Sửa/Xóa menu | Tạo món mới kèm ảnh, giá, công thức → đồng bộ cả chuỗi |
| | Giá theo chi nhánh | Latte Q1: 55K, Thủ Đức: 45K — tùy chỉnh riêng từng quán |
| | Bật/Tắt món tức thì | Hết sữa → tắt tất cả món có sữa ngay lập tức |
| | Menu mùa / Giới hạn | Tạo menu mùa tự bật/tắt theo ngày đã hẹn |
| | Quản lý Combo | Latte + Croissant = 75K (tiết kiệm 15K) — tạo trong 1 phút |
| **Nhân sự & CRM** | Quản lý NV toàn chuỗi | Thêm/sửa/xóa NV, phân quyền, xem chấm công 3 quán |
| | Quản lý Loyalty | Cấu hình tích điểm, tạo voucher, hạng thành viên |
| | Quản lý Khuyến mãi | Giảm 20% khung 14-16h, Buy 1 Get 1, voucher sinh nhật |
| **🤖 AI thông minh** | AI Thống kê toàn chuỗi | Hỏi: "So sánh Q1 vs Q3 tháng 8?" → AI trả lời kèm biểu đồ |
| | AI Phân tích menu | "Matcha tăng 35% → thêm biến thể", "Smoothie Dâu 2 ly/ngày → nên loại" |
| | AI Dự đoán khách bỏ | Danh sách khách sắp bỏ quán + tự gửi voucher kéo lại |
| | AI Gợi ý Combo | "68% khách mua Latte cũng mua Croissant → tạo combo 75K" |
| **Quản trị** | Xuất báo cáo | Doanh thu, lương, kho → Excel/PDF gửi kế toán |
| | Nhật ký thao tác | Ai sửa giá, ai xóa đơn, lúc nào, từ đâu → ghi hết |
| | Giờ hoạt động | Cài giờ mở/đóng → QR Order tự hiện "Quán đã đóng cửa" |
| | Phân quyền | QL chỉ xem quán mình, không thấy lương toàn chuỗi |
| | Gửi thông báo | "Hôm nay đóng cửa sớm 20h" → gửi tất cả NV/QL |

---

## 🔐 AI LÀM GÌ CHO AI?

| 🤖 AI Module | Làm gì? | Ai dùng? |
|---|---|---|
| **AI Thống kê** | Hỏi bằng tiếng Việt: "Doanh thu tuần này?" → AI trả lời kèm biểu đồ | 🏪 Quản lý (quán mình) + 👑 Admin (cả chuỗi) |
| **AI Gợi ý Combo** | Phân tích data → "68% khách mua Latte cũng mua Croissant" → gợi ý tạo combo | 👑 Admin |
| **AI Giữ chân khách** | Dự đoán khách sắp bỏ quán → tự gửi voucher kéo lại | 👑 Admin (cấu hình) → Tự động chạy |
| **AI Phân tích menu** | "Matcha tăng 35% → thêm biến thể", "Smoothie Dâu chỉ 2 ly/ngày → loại" | 👑 Admin |
| **AI Chatbot gợi ý** | Khách chat: "Tôi muốn uống gì mát?" → AI gợi ý dựa khẩu vị, thời tiết | 👤 Khách hàng |

> **Nhân viên pha chế KHÔNG cần AI** — vì công thức pha đã hiện tự động kèm mỗi đơn trên TV.

---

## 🔐 PHÂN QUYỀN: AI THẤY GÌ, LÀM GÌ?

| Chức năng | 👤 Khách | 🧋 NV | 🏪 Quản lý | 👑 Admin |
|---|---|---|---|---|
| Đặt món qua QR | ✅ | — | — | — |
| Nhận đơn trên TV | — | ✅ | — | — |
| Báo hết món | — | ✅ | ✅ | ✅ |
| Chấm công | — | ✅ | 👁️ Xem | 👁️ Xem |
| Mở/Kết ca | — | — | ✅ | 👁️ Xem |
| Quản lý kho | — | — | ✅ | 👁️ Xem |
| Xem doanh thu | — | — | ✅ Quán mình | ✅ Toàn chuỗi |
| Hỏi AI Thống kê | — | — | ✅ Quán mình | ✅ Toàn chuỗi |
| Quản lý Menu/Giá | — | — | — | ✅ |
| Tạo Combo / Khuyến mãi | — | — | — | ✅ |
| AI Dự đoán / Gợi ý | — | — | — | ✅ |
| Quản lý Nhân sự | — | — | — | ✅ |
| Phân quyền / Audit Log | — | — | — | ✅ |

> 🔑 **Nguyên tắc:** Mỗi người chỉ thấy và làm được những gì thuộc phạm vi vai trò của mình. Quản lý chỉ thấy quán mình. Admin thấy tất cả.

---

## 📊 TÓM TẮT

| Chỉ tiêu | Giá trị |
|---|---|
| Tổng nhóm người dùng | **4** (Khách, NV, Quản lý, Admin) |
| Tổng tính năng | **71** (24 + 12 + 13 + 22) |
| Tổng AI Module | **5** (Thống kê, Combo, Giữ khách, Phân tích menu, Chatbot) |
| Người dùng AI nhiều nhất | 👑 Admin (4 AI) |
| Nhiều tính năng nhất | 👤 Khách hàng (24 tính năng) |
| Quyền cao nhất | 👑 Admin (toàn quyền chuỗi) |
