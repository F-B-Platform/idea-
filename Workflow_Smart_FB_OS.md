# 🔄 CÁC WORKFLOW CHÍNH TRONG HỆ THỐNG SMART F&B OS

> Tài liệu mô tả chi tiết các luồng nghiệp vụ (Workflow) trong hệ thống và cách từng Actor tương tác.

---

## 📋 MỤC LỤC WORKFLOW

| # | Workflow | Actor chính | Actor liên quan |
|---|---|---|---|
| WF-01 | Đặt món & Thanh toán (QR Self-Order) | 👤 Khách hàng | 🧋 Barista |
| WF-02 | Pha chế & Phục vụ đơn hàng (KDS) | 🧋 Barista | 👤 Khách hàng |
| WF-03 | Gọi thêm món / Gọi nhân viên | 👤 Khách hàng | 🧋 Barista |
| WF-04 | Chatbot AI Gợi ý món | 👤 Khách hàng | ⚙️ AI-5 |
| WF-05 | Đánh giá & Feedback | 👤 Khách hàng | 🏪 Quản lý |
| WF-06 | Báo hết món (Out of Stock) | 🧋 Barista | 👤 Khách hàng (tự ẩn trên menu) |
| WF-07 | Chấm công đầu/cuối ca | 🧋 Barista | 🏪 Quản lý |
| WF-08 | Mở ca / Kết ca | 🏪 Quản lý | 👑 Admin |
| WF-09 | Xuất kho quầy & Kiểm kê | 🏪 Quản lý | — |
| WF-10 | Nhập kho từ Nhà cung cấp | 🏪 Quản lý | — |
| WF-11 | Xem báo cáo & AI Thống kê | 🏪 Quản lý + 👑 Admin | ⚙️ AI-1 |
| WF-12 | Quản lý Menu & Giá | 👑 Admin | 👤 Khách (menu cập nhật) |
| WF-13 | Tạo Combo & Khuyến mãi | 👑 Admin | ⚙️ AI-2, AI-4 |
| WF-14 | AI Churn Prediction & Giữ chân khách | ⚙️ AI-3 (Tự động) | 👤 Khách hàng |
| WF-15 | Quản lý Loyalty & Voucher | 👑 Admin | 👤 Khách hàng |

---

## WF-01: 🛒 ĐẶT MÓN & THANH TOÁN (QR SELF-ORDER)

> **Actor chính:** 👤 Khách hàng  
> **Actor liên quan:** 🧋 Barista (nhận đơn + bill), 🏪 Quản lý / 👑 Admin (cập nhật doanh thu real-time)

```
👤 Khách hàng                     🧋 Barista (KDS Bếp)        📊 Admin/Manager
     │                                  │                          │
     │  1. Scan QR tại bàn               │                          │
     │  → Mở menu PWA trên trình duyệt  │                          │
     │                                   │                          │
     │  2. Chọn món, chỉnh Size/Đường/Đá │                          │
     │     Thêm Topping, ghi chú đặc biệt│                          │
     │                                   │                          │
     │  3. Thêm vào giỏ hàng             │                          │
     │     Chọn "Tại bàn" hoặc "Mang đi" │                          │
     │                                   │                          │
     │  4. Gửi đơn (không thanh toán)    │                          │
     │  → Đơn bay qua WebSocket ─────────→ 5. KDS hiện đơn         │
     │                                   │    + CÔNG THỨC PHA       │
     │                                   │                          │
     │  7. Nhận thông báo 🔔             │  6. Pha xong             │
     │     "Món đã sẵn sàng!"            │  → Bấm "Hoàn thành"     │
     │                                   │                          │
     │  8. Nhận món (NV mang ra bàn)     │                          │
     │                                   │                          │
     │  9. Yêu cầu thanh toán            │                          │
     │  → Bấm "💳 Yêu cầu bill"         │  Alert: "Bàn 5 cần bill" │
     │                                   │  → In bill → Ra bàn      │
     │                                   │                          │
     │  10. Thanh toán (2 lựa chọn)      │                          │
     │  ├── Tại bàn: NV thu tiền mặt     │                          │
     │  │           hoặc quét VietQR     │                          │
     │  └── Tại quầy: Khách tự ra trả   │                          │
     │                                   │                          │
     │                                   │  11. NV xác nhận ─────────→ Dashboard cập nhật
     │                                   │      thanh toán           │  doanh thu tức thì
     ▼                                   ▼                          ▼
  [ Kết thúc phiên order ]      [ Đơn hoàn tất ]       [ Doanh thu +XX.XK 📈 ]
```

**Điểm đặc biệt:**
- Khách **không tự thanh toán online** — nhân viên xác nhận dòng tiền.
- Hỗ trợ **2 hình thức:** Nhân viên mang bill ra bàn **hoặc** khách ra quầy.
- Mỗi đơn xác nhận → **doanh thu cập nhật real-time** lên Dashboard Admin + Manager ngay lập tức.


---

## WF-02: 🧋 PHA CHẾ & PHỤC VỤ ĐƠN HÀNG (KDS)

> **Actor chính:** 🧋 Barista
> **Giao diện:** Màn hình KDS Full-screen (Tablet/Smart TV tại bếp)

```
Đơn mới vào KDS
      │
      ▼
┌─────────────────────────────────────┐
│  ĐƠN #127 — BÀN 5 — Tại quán      │
│                                     │
│  🥤 Latte L (25% đường, ít đá)      │
│     → Espresso 2 shot               │
│     → Sữa tươi 200ml               │
│     → Đá 100g                       │
│     → Đường: 25%                    │
│     Ghi chú: "Thêm shot espresso"   │
│                                     │
│  🍞 Croissant x1                    │
│                                     │
│  ⏱️ Chờ: 2 phút  [  HOÀN THÀNH  ]  │
└─────────────────────────────────────┘
      │
      │  Barista pha theo công thức chuẩn
      │
      ▼
  Bấm "Hoàn thành"
      │
      ├── Đơn biến mất khỏi KDS
      ├── Khách nhận thông báo 🔔
      └── Thời gian phục vụ được ghi nhận
```

**Cảnh báo chờ lâu:**
- **Xanh** = Đơn mới (< 3 phút)
- **Vàng** = Chờ hơi lâu (3-5 phút) → ưu tiên
- **Đỏ** = Chờ quá lâu (> 5 phút) → pha ngay!

---

## WF-03: ➕ GỌI THÊM MÓN / 🔔 GỌI NHÂN VIÊN

> **Actor chính:** 👤 Khách hàng

**Gọi thêm món:**
```
👤 Khách (đã đặt đơn trước đó)
     │
     │  Bấm "Gọi thêm món" trên QR Menu
     │  → Chọn thêm 1 ly Trà Đào
     │  → Thanh toán bổ sung
     │
     ▼
  Món mới được GỘP vào đơn đang chạy (không tạo đơn mới)
  → Hiện trên KDS cho Barista
```

**Gọi nhân viên:**
```
👤 Khách
     │
     │  Bấm nút "Gọi nhân viên 🔔"
     │
     ▼
🧋 Barista nhận thông báo:
   "Bàn 5 cần hỗ trợ"
   → Đến bàn hỗ trợ khách
```

---

## WF-05: 🤖 CHATBOT AI GỢI Ý MÓN (AI-5)

> **Actor chính:** 👤 Khách hàng
> **AI Module:** AI-5 (Recommendation Engine)

```
👤 Khách mở QR Menu
     │
     │  Bấm nút "🤖 Gợi ý cho tôi"
     │
     ▼
┌──────────────────────────────────────┐
│  CHATBOT AI                          │
│                                      │
│  👤 "Tôi thích vị đắng, ít ngọt"    │
│  🤖 "Gợi ý: Americano (0% đường)    │
│      hoặc Cappuccino đường 25%"      │
│                                      │
│  👤 "Tôi bị dị ứng sữa"             │
│  🤖 AI lọc menu → chỉ hiện:         │
│     Americano, Trà Đào, Nước ép      │
│     (ẩn tất cả món có sữa)           │
│                                      │
│  👤 "Hôm nay nóng quá"               │
│  🤖 "Trà Đào Cam Sả đá ❄️            │
│      — bán chạy nhất hôm nay!"       │
└──────────────────────────────────────┘
     │
     ▼
  Khách chọn món gợi ý → Thêm vào giỏ → Thanh toán
```

**Input AI sử dụng:** Khẩu vị khách, dị ứng, thời tiết (Weather API), data bán hàng real-time, lịch sử đơn hàng (CRM).

---

## WF-06: ⭐ ĐÁNH GIÁ & FEEDBACK

> **Actor chính:** 👤 Khách hàng
> **Actor liên quan:** 🏪 Quản lý (nhận alert)

```
👤 Khách (sau khi nhận món)
     │
     │  Scan QR tại bàn hoặc bấm trên QR Order
     │
     ▼
  Đánh giá TỪNG MÓN (1-5 sao)
     │  + Ghi chú: "Latte hơi nhạt"
     │
     ├── ≥ 4 sao → Lưu CRM + hiện "Cảm ơn bạn!"
     │
     └── ≤ 2 sao → 🚨 Alert ngay cho 🏪 Quản lý
         → QL đến bàn xin lỗi / xử lý trong 5 phút
```

---

## WF-07: 🚫 BÁO HẾT MÓN (OUT OF STOCK)

> **Actor chính:** 🧋 Barista
> **Ảnh hưởng:** 👤 Khách hàng (tự ẩn trên menu)

```
🧋 Barista phát hiện hết nguyên liệu (VD: hết sữa tươi)
     │
     │  Bấm "Hết" trên KDS cho món "Latte"
     │
     ▼
  Hệ thống TỰ ĐỘNG:
     ├── Ẩn "Latte" trên QR Menu của tất cả khách (tức thì)
     ├── Ẩn tất cả món khác dùng sữa tươi (nếu cấu hình)
     └── Gửi cảnh báo cho 🏪 Quản lý: "Latte đã hết — NL: sữa tươi"
```

---

## WF-08: ⏰ CHẤM CÔNG ĐẦU / CUỐI CA

> **Actor chính:** 🧋 Barista (Nhân viên)
> **Actor liên quan:** 🏪 Quản lý (xem báo cáo chấm công)

```
🧋 Nhân viên đến quán
     │
     ├── OPTION 1 (App):
     │   Mở App → Scan QR Code động (đổi mỗi 30s)
     │   + GPS xác nhận đang ở quán (bán kính 50m)
     │   → Hệ thống ghi: "NV Trung — Vào ca 7:58"
     │
     └── OPTION 2 (Máy chấm công):
         Chấm vân tay / Face ID trên máy chấm công
         → Máy đồng bộ API về hệ thống tự động
         → Ghi: "NV Trung — Vào ca 7:58"
              │
              ▼
       Cuối ca: Lặp lại → Ghi giờ ra
              │
              ▼
       Hệ thống tự tính: Số giờ làm × Lương/giờ + Phụ cấp
       → Cuối tháng xuất bảng lương tự động
```

**Cảnh báo:** Đi muộn > 15 phút → Thông báo cho Quản lý. Không chấm công → Ghi nhận vắng mặt.

---

## WF-09: 📋 MỞ CA / KẾT CA

> **Actor chính:** 🏪 Quản lý chi nhánh

```
ĐẦU NGÀY:
🏪 Quản lý
     │
     │  Bấm "Mở Ca" trên App
     │  → Nhập tiền mặt đầu két: 500K
     │  → Hệ thống bắt đầu ghi nhận doanh thu ca này
     │
     ▼

CUỐI NGÀY:
🏪 Quản lý
     │
     │  Bấm "Kết Ca"
     │  → Nhập tiền mặt thực đếm trong két: 2.850K
     │
     ▼
  Hệ thống đối soát:
     │  Tiền mặt hệ thống ghi = 2.900K
     │  Thực đếm = 2.850K
     │  Chênh lệch = 50K → ⚠️ Cảnh báo!
     │
     ▼
  Báo cáo EOD tự động gửi qua Zalo/Email cho 👑 Admin
```

---

## WF-10: 📦 XUẤT KHO QUẦY & KIỂM KÊ

> **Actor chính:** 🏪 Quản lý chi nhánh

```
XUẤT KHO:
🏪 Quản lý
     │
     │  Tạo phiếu xuất: "Xuất 2kg CF hạt + 5 hộp sữa từ Kho → Quầy"
     │  → Hệ thống trừ tồn kho tổng
     │
     ▼

KIỂM KÊ:
🏪 Quản lý
     │
     │  Mở App → Kiểm kê
     │  Nhập số thực đếm từng loại nguyên liệu
     │
     ▼
  Hệ thống tính chênh lệch:
     │  CF hạt: Hệ thống = 5.2kg, Thực đếm = 4.8kg
     │  Chênh lệch: -0.4kg (7.7%) → ⚠️ Cảnh báo thất thoát
     │
     ▼
  Cảnh báo: "CF hạt còn 4.8kg — dự kiến hết trong 2 ngày"
  → Quản lý đặt hàng NCC kịp thời
```

---

## WF-11: 📥 NHẬP KHO TỪ NHÀ CUNG CẤP

> **Actor chính:** 🏪 Quản lý chi nhánh

```
NCC giao hàng đến quán
     │
     ▼
🏪 Quản lý
     │
     │  Tạo phiếu nhập kho:
     │  "Nhận 10kg CF hạt + 50 hộp sữa tươi"
     │
     │  Đối chiếu với đơn đặt hàng trước đó
     │  → Đúng: Xác nhận → Kho tổng cộng thêm
     │  → Thiếu: Ghi chú → Thông báo Admin
     │
     ▼
  Tồn kho cập nhật real-time
```

---

## WF-12: 📊 XEM BÁO CÁO & AI THỐNG KÊ (AI-1)

> **Actor chính:** 🏪 Quản lý + 👑 Admin
> **AI Module:** AI-1 (Prophet / LLM RAG)

```
🏪 Quản lý (chỉ xem quán mình):
     │
     │  Hỏi AI: "Hôm nay doanh thu bao nhiêu?"
     │  → AI: "18.5 triệu, tăng 8% so với hôm qua.
     │         Top 3: Bạc Xỉu (42 ly), Latte (38), Trà Đào (29)"
     │
     │  Xem biểu đồ doanh thu theo giờ
     │  → Biết giờ nào đông để xếp ca phù hợp
     │
     ▼

👑 Admin (xem toàn chuỗi):
     │
     │  Hỏi AI: "So sánh doanh thu Q1 vs Q3 tuần này"
     │  → AI trả lời kèm biểu đồ so sánh trực quan
     │
     │  Xem Dashboard: P&L, doanh thu, chi phí 3 quán
     │  → Biết quán nào lãi, quán nào đang lỗ
     │
     ▼
  Xuất báo cáo Excel/PDF gửi kế toán
```

---

## WF-13: 🍽️ QUẢN LÝ MENU & GIÁ

> **Actor chính:** 👑 Admin

```
👑 Admin
     │
     │  Tạo món mới: "Matcha Latte"
     │  → Ảnh, giá, mô tả, công thức pha, allergen, calories
     │
     │  Cài giá theo chi nhánh:
     │  → Q1 (trung tâm): 55K
     │  → Thủ Đức: 45K
     │
     │  Bấm "Đồng bộ"
     │
     ▼
  Món mới hiện trên QR Menu tất cả quán tức thì
     │
     │  Bật/Tắt món (VD: hết sữa → tắt tất cả món có sữa)
     │  Menu mùa (VD: "Menu hè 2026" tự bật 1/6, tự tắt 31/8)
     │
     ▼
  👤 Khách scan QR → Thấy menu đã cập nhật
```

---

## WF-14: 🎯 TẠO COMBO & KHUYẾN MÃI (AI-2 + AI-4)

> **Actor chính:** 👑 Admin
> **AI Module:** AI-2 (Combo Suggest), AI-4 (Menu Intelligence)

```
⚙️ AI-2 phân tích data:
     │
     │  "68% khách mua Latte cũng mua Croissant"
     │  → Đề xuất: Tạo Combo Latte + Croissant = 75K (tiết kiệm 15K)
     │
     ▼
👑 Admin duyệt & tạo Combo
     │
     ▼
  Combo hiện trên QR Menu: "Combo tiết kiệm 15K 🔥"

⚙️ AI-4 phân tích thêm:
     │
     │  "Khung 14h-16h vắng nhất (chỉ 12 đơn/giờ)"
     │  → Đề xuất: Push giảm 20% khung giờ này qua Zalo OA
     │
     ▼
👑 Admin tạo chiến dịch Smart Promotion
     → Zalo OA tự gửi "☕ Giảm 20% từ 14h-16h hôm nay!"
```

---

## WF-15: 🔮 AI CHURN PREDICTION & GIỮ CHÂN KHÁCH (AI-3)

> **Actor chính:** ⚙️ AI-3 (Tự động)
> **Actor ảnh hưởng:** 👤 Khách hàng

```
⚙️ AI-3 chạy hàng ngày (tự động)
     │
     │  Quét toàn bộ CRM:
     │  "Khách Nguyễn A: 45 ngày chưa ghé quán
     │   Tần suất trước: 2 lần/tuần → Churn risk: 78%"
     │
     ▼
  Hệ thống tự động:
     │
     │  Gửi Voucher giảm 30% qua Zalo OA cho khách A
     │  "Chúng tôi nhớ bạn! ☕ Giảm 30% cho đơn tiếp theo"
     │
     ▼
  👤 Khách A nhận Zalo → Quay lại quán → Scan QR → Áp voucher
```

---

## WF-16: 🎁 QUẢN LÝ LOYALTY & VOUCHER

> **Actor chính:** 👑 Admin
> **Actor ảnh hưởng:** 👤 Khách hàng

```
👑 Admin cấu hình chương trình Loyalty:
     │
     │  Mỗi 10K chi tiêu = 1 điểm
     │  100 điểm = Voucher giảm 20K
     │  Sinh nhật = Voucher 50K (auto gửi qua Zalo)
     │
     ▼

👤 Khách đặt qua QR Order:
     │
     │  Thanh toán 55K → Tự động tích 5 điểm vào SĐT
     │  (Không cần thẻ giấy, không cần nhân viên ghi)
     │
     │  Đủ 100 điểm → Voucher tự động hiện trên QR Menu
     │  "Bạn có Voucher giảm 20K! Áp ngay?"
     │
     ▼
  Khách áp Voucher → Giá trừ tự động → Thanh toán phần còn lại
```

---

## 📐 SƠ ĐỒ TỔNG QUAN: 4 ACTOR TƯƠNG TÁC VỚI HỆ THỐNG

```
                        ┌───────────────────────┐
                        │   SMART F&B OS        │
                        │   (Backend + AI)       │
                        └───────────┬───────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
     ┌────▼────┐            ┌───────▼───────┐          ┌──────▼─────┐
     │ 👤 KHÁCH │            │ 🧋 BARISTA     │          │ 🏪 QUẢN LÝ │
     │ (PWA)   │            │ (KDS Bếp)     │          │ (App/Web)  │
     └────┬────┘            └───────┬───────┘          └──────┬─────┘
          │                         │                         │
     • Scan QR Order           • Nhận đơn real-time      • Mở/kết ca
     • Thanh toán VietQR       • Xem công thức chuẩn     • Đối soát két
     • Chatbot AI gợi ý        • Báo hết món             • Nhập/Xuất kho
     • Gọi thêm món            • Sơ đồ bàn               • Kiểm kê
     • Feedback                • In bill                 • Xếp ca NV
     • Loyalty/Voucher         • Chấm công               • Biểu đồ doanh thu
                               • Nhận "Gọi NV"           • AI Thống kê (AI-1)
          │                         │                         │
          └─────────────────────────┼─────────────────────────┘
                                    │
                            ┌───────▼───────┐
                            │ 👑 ADMIN       │
                            │ (Dashboard)   │
                            └───────┬───────┘
                                    │
                       • Dashboard 3 quán real-time
                       • P&L (Lãi/Lỗ) tự động
                       • Quản lý Menu/Giá/Combo
                       • CRM & Loyalty
                       • RBAC phân quyền
                       • Audit Log
                       • AI Thống kê toàn chuỗi (AI-1)
                       • AI Menu Intelligence (AI-4)
                       • AI Combo Suggest (AI-2)
                       • AI Churn Prediction (AI-3)
                       • Export Excel/PDF
```

---

> **Tổng cộng:** 15 Workflow chính | 4 Actor | 5 AI Module | 69 Tính năng
