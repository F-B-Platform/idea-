# 👥 CÁC ACTOR TRONG HỆ THỐNG SMART F&B OS (REVISED — 4 MEMBERS)

> Tài liệu mô tả chi tiết 4 nhóm người dùng (Actor) trong hệ thống, vai trò, quyền hạn, giao diện sử dụng và các tính năng tương ứng.
>
> **Phiên bản:** Revised — Cập nhật theo `Smart_FB_OS_Revised_4members.docx`
>
> **Thay đổi chính so với bản gốc:**
> - AI Modules: Chỉ triển khai **2 modules** (AI-1 Recommendation Chatbot + AI-2 Combo Suggestion). Ba modules còn lại (Business Analytics, Churn Prediction, Menu Intelligence) được ghi nhận là **future extensions**, không triển khai trong phạm vi Capstone này.
> - Tổng tính năng giảm từ 71 → **66** (cắt 5 tính năng liên quan 3 AI modules future work).

---

## 📋 TỔNG QUAN ACTOR

| # | Actor | Vai Trò | Giao Diện | Số Tính Năng |
|---|---|---|---|---|
| 1 | 👤 **Khách hàng** | Người đặt món, thanh toán, feedback, nhận gợi ý AI | QR Order Web (PWA) trên trình duyệt | 24 |
| 2 | 🧋 **Barista / Phục vụ** | Nhận đơn, pha chế, phục vụ, chấm công | KDS (TV/Tablet) + Staff App (Mobile) | 12 |
| 3 | 🏪 **Quản lý chi nhánh** | Quản lý ca, kho, báo cáo chi nhánh | App Manager (Mobile) + Web (giới hạn quyền) | 12 |
| 4 | 👑 **Chủ chuỗi / Admin** | Quản trị toàn bộ chuỗi, duyệt combo AI | Web Dashboard (Desktop/Laptop) — toàn quyền | 18 |

> **Tổng cộng:** 4 Actor | 66 tính năng | 2 AI Module triển khai + 3 AI Module future work

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
        │   Feedback / Loyalty   │   Chấm công             │   EOD Report
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
                     • ✅ AI Combo Suggest (AI-2)
                     • ✅ AI Chatbot cho Khách (AI-1)
                     •
                     • ── FUTURE WORK ──
                     • 🔮 AI Thống kê (AI-3)
                     • 🔮 AI Churn Prediction (AI-4)
                     • 🔮 AI Menu Intelligence (AI-5)
```

---

## 1. 👤 ACTOR 1: KHÁCH HÀNG (Customer)

### Mô tả vai trò
Khách hàng là người sử dụng cuối cùng — đến quán, quét QR tại bàn, tự đặt món trên trình duyệt điện thoại. **Không cần tải app**, hệ thống là PWA mở trên trình duyệt. Khách có thể trò chuyện với **AI Chatbot gợi ý món** (AI-1) — module nghiên cứu chính của dự án.

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
      │                              │
      │                    [AI Chatbot gợi ý]
      │                    "Hôm nay nóng quá, gợi ý đi!"
      │                    → "Trà Đào Cam Sả đá ❄️"
      │
      ▼
Theo dõi trạng thái đơn real-time ("Đang pha chế..." → "Sẵn sàng! 🔔")
      │
      ▼
Nhận món → Yêu cầu thanh toán (NV mang bill hoặc ra quầy)
      │
      ▼
Feedback đánh giá từng món (1-5 sao + ảnh + ẩn danh tùy chọn)
      │
      ▼
Tích điểm Loyalty tự động
```

### Danh sách tính năng (24 tính năng)

| Nhóm | # | Tính Năng | Mô Tả |
|---|---|---|---|
| **Nhận diện** | C-00 | Nhận diện SĐT | Scan QR → nhập SĐT → lần đầu thêm Tên, quen thì nạp hồ sơ CRM |
| **Đặt món** | C-01 | Scan QR xem menu | Quét QR tại bàn → mở menu trên trình duyệt, tự nhận diện bàn + chi nhánh |
| | C-02 | Menu trực quan | Phân loại (Cà phê / Trà / Đá xay / Bánh) kèm ảnh, giá theo chi nhánh, mô tả, best-seller tag |
| | C-03 | Tùy chỉnh món | Size (S/M/L), Đường (0-100%), Đá, Topping |
| | C-04 | Ghi chú đặc biệt | Ghi chú tự do: "Ít đá, thêm shot espresso" |
| | C-05 | Giỏ hàng | Thêm nhiều món, chỉnh số lượng, xóa trước khi gửi |
| | C-06 | Chọn Mang đi / Tại quán | "Tại bàn" (gắn số bàn) hoặc "Mang đi" (Takeaway) |
| **Thanh toán** | C-07 | Yêu cầu in bill | Bấm "💳 Yêu cầu thanh toán" → NV nhận alert → mang bill ra bàn |
| | C-08 | Thanh toán tại bàn | NV đưa bill → Tiền mặt hoặc VietQR → NV xác nhận |
| | C-09 | Thanh toán tại quầy | Khách tự ra quầy trả → NV xác nhận |
| | C-10 | Áp mã giảm giá / Voucher | Khách chọn voucher khả dụng hoặc nhập mã → giảm tự động |
| | C-11 | Cập nhật doanh thu real-time | Xác nhận thanh toán → dashboard Admin/Manager cập nhật tức thì |
| **Trải nghiệm** | C-12 | 🤖 **AI Chatbot gợi ý (AI-1)** | Chat với AI: khẩu vị, thời tiết, dị ứng, lịch sử CRM → gợi ý món phù hợp qua RAG + content-based/hybrid recommendation. **Đây là module nghiên cứu chính.** |
| | C-13 | Xem món bán chạy | Tag "Best Seller", "Mới", "Hot" trên menu |
| | C-14 | Theo dõi trạng thái đơn | Thanh tiến trình real-time: "Đã xác nhận → Đang pha chế → Sẵn sàng 🔔" |
| | C-15 | Thời gian chờ ước tính | "Dự kiến xong sau ~8 phút" |
| | C-16 | Thông báo khi món xong | Push notification trên trình duyệt |
| | C-17 | Gọi nhân viên | Nút "Gọi nhân viên 🔔" → NV nhận alert "Bàn 5 cần hỗ trợ" |
| | C-18 | QR Feedback & Review công khai | Đánh giá 1-5 sao từng món + **tải ảnh thực tế** + tùy chọn **Ẩn danh** + **Publish công khai** lên QR menu. ≤ 2 sao → alert Manager ngay. |
| **CRM & Loyalty** | C-19 | Tích điểm Loyalty | Tự động cộng điểm vào SĐT khi hoàn tất đơn |
| | C-20 | Lưu lịch sử uống & CRM | Ghi lại: món đã gọi, số lần ghé, ngày cuối, tổng chi tiêu, sở thích |
| | C-21 | Nhận voucher qua Zalo | Voucher sinh nhật, loyalty, "lâu ngày chưa ghé" → gửi tự động qua Zalo OA |
| **Nâng cao** | C-22 | Gọi thêm món | Thêm vào đơn đang chạy trên bàn, không tạo đơn mới |
| | C-23 | Allergen & Calories | Hiện thành phần dị ứng + calories ước tính từng món |
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
| **Đơn hàng** | S-01 | Xem đơn hàng real-time | Đơn từ QR Order hiện TỨC THÌ trên KDS qua WebSocket |
| | S-02 | Hiện công thức chuẩn | Mỗi đơn kèm công thức pha: "Espresso 2 shot + Sữa tươi 200ml + Đá 150g + Đường 25%" |
| | S-03 | Ưu tiên đơn chờ lâu | Xanh (< 3p) → Vàng (3-5p) → Đỏ (> 5p) — visual priority levels |
| | S-04 | Bấm "Hoàn thành" | Cập nhật trạng thái đơn → thông báo khách hoặc nhân viên phục vụ |
| | S-05 | Xem ghi chú khách | Hiện rõ: "Ít đá", "Không đường", "Thêm shot" |
| | S-06 | Xem đơn gom theo bàn | "Bàn View" → gom nhiều order cùng bàn, mang 1 chuyến đủ cả bàn |
| **Vận hành** | S-07 | Báo Hết Món | Bấm "Hết" trên KDS → món tự ẩn ngay trên QR Order menu khách |
| | S-08 | In Bill / Receipt | Kết nối máy in nhiệt → in hóa đơn khi khách yêu cầu |
| | S-09 | Sơ đồ bàn (Floor Map) | Xem trực quan bàn nào có khách (xanh/đỏ), bàn nào trống |
| | S-10 | Nhận thông báo "Gọi NV" + "Yêu cầu bill" | Khách bấm gọi → chuông alert trên KDS & Staff App: "Bàn 5 cần hỗ trợ" / "Bàn 3 yêu cầu bill 💳" |
| | S-11 | Chấm công đa phương thức | QR Code động (đổi 30s) + GPS Lock (bán kính 50m). Mở rộng: Máy vân tay / Face ID |
| | S-12 | App Nội Bộ Nhân Viên (Staff App) | App di động: alert gọi bàn 🔔/báo bill 💳, xuất mã VietQR di động, báo hết món, sơ đồ bàn, xác nhận thanh toán |

> **Lưu ý quan trọng:** Barista **KHÔNG CẦN chatbot hỏi công thức** — vì công thức pha chi tiết đã hiển thị tự động kèm mỗi đơn hàng trên KDS (S-02). Barista **KHÔNG sử dụng bất kỳ AI Module nào**.

---

## 3. 🏪 ACTOR 3: QUẢN LÝ CHI NHÁNH (Branch Manager)

### Mô tả vai trò
Quản lý chịu trách nhiệm vận hành 1 chi nhánh: mở/kết ca, đối soát két, nhập/xuất kho, kiểm kê nguyên liệu, xem báo cáo doanh thu. **Chỉ xem data của quán mình**, không thấy quán khác hay lương toàn chuỗi.

> **Thay đổi so với bản gốc:** Tính năng AI-1 Thống kê NLP (M-11 cũ) đã được chuyển sang **future work**. Manager dùng các báo cáo và dashboard có sẵn thay cho truy vấn ngôn ngữ tự nhiên.

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
  • Xem báo cáo doanh thu chi nhánh
  • Xem feedback / cảnh báo đánh giá thấp
      │
      ▼
Kết ca cuối ngày → Đếm tiền két → Hệ thống đối soát chênh lệch
      │
      ▼
Nhận báo cáo EOD tự động qua Zalo/Email
```

### Danh sách tính năng (12 tính năng)

| Nhóm | # | Tính Năng | Mô Tả |
|---|---|---|---|
| **Ca làm** | M-01 | Mở ca / Kết ca | Nhập tiền đầu két (mở ca), đếm tiền thực (kết ca), hệ thống ghi nhận thời gian mở/đóng |
| | M-02 | Đối soát két tiền | So sánh: tiền hệ thống ghi vs thực đếm → cảnh báo chênh > 50K |
| | M-03 | Duyệt lịch ca | Xem bảng ca tuần → duyệt / đổi ca / thêm NV thay thế |
| | M-04 | Xem chấm công NV | Danh sách NV check-in/check-out → ai đi muộn, ai overtime, payroll-supporting data |
| **Kho hàng** | M-05 | Xuất kho quầy (Requisition) | Tạo phiếu xuất: "Xuất 2kg CF hạt + 5 hộp sữa từ Kho → Quầy" — traceable stock movement |
| | M-06 | Kiểm kê (Stocktaking) | Nhập số thực đếm → hệ thống tính chênh lệch actual vs system → ghi nhận wastage |
| | M-07 | Nhận cảnh báo kho | "CF hạt còn 1.2kg — dự kiến hết trong 1 ngày" / Cảnh báo abnormal loss |
| | M-08 | Nhập kho từ NCC (Goods Receipt) | NCC giao hàng → nhập phiếu → đối chiếu received vs purchase order → cập nhật inventory |
| **Báo cáo** | M-09 | Xem doanh thu ca/ngày | Doanh thu, số đơn, trung bình/đơn, top món, hourly demand — chỉ quán mình |
| | M-10 | Nhận báo cáo EOD tự động | Cuối ca → hệ thống tự tổng hợp → gửi báo cáo qua Zalo/Email cho Manager |
| | M-11 | Xem feedback & cảnh báo | Review ≤ 2 sao → alert ngay lập tức để xử lý kịp thời |
| **Khác** | M-12 | Quản lý Sơ đồ bàn & cấu hình chi nhánh | Cấu hình bàn quán (Trong/Ngoài/VIP), giờ hoạt động, giá riêng chi nhánh, quyền chi nhánh |

> **🔮 Future Work:** Tính năng hỏi AI bằng ngôn ngữ tự nhiên (AI-3 Business Analytics) sẽ được bổ sung trong các giai đoạn mở rộng sau Capstone.

---

## 4. 👑 ACTOR 4: CHỦ CHUỖI / ADMIN (Owner)

### Mô tả vai trò
Admin là chủ sở hữu toàn bộ chuỗi quán. Có **quyền cao nhất**: xem dashboard tất cả quán real-time, quản lý menu/giá/combo toàn chuỗi, cấu hình nhân sự + Loyalty + Promotion. Trong phiên bản Revised, Admin sử dụng **AI-2 Combo Suggestion** để nhận gợi ý combo từ dữ liệu bán hàng. Các AI modules khác (Business Analytics, Churn Prediction, Menu Intelligence) được thiết kế kiến trúc sẵn nhưng **chưa triển khai**.

### Giao diện
- **Web Dashboard (Desktop/Laptop)** — toàn quyền xem và quản lý cả chuỗi

### Luồng tương tác chính
```
Đăng nhập Dashboard
      │
      ▼
Xem tổng quan các quán real-time (doanh thu, đơn, cảnh báo)
      │
      ├── So sánh chi nhánh → P&L tự động
      ├── Quản lý Menu / Giá / Combo → đồng bộ cả chuỗi
      ├── Quản lý Nhân sự / Loyalty / Promotion
      ├── ✅ AI Combo Suggest: "68% khách mua Latte cũng mua Croissant → tạo combo?"
      ├── Xem feedback & review kèm ảnh → xử lý
      └── Export Excel/PDF → gửi kế toán
```

### Danh sách tính năng (18 tính năng)

| Nhóm | # | Tính Năng | Mô Tả |
|---|---|---|---|
| **Dashboard** | A-01 | Dashboard đa chi nhánh | Doanh thu, đơn, NV, cảnh báo — tất cả trên 1 màn hình real-time |
| | A-02 | So sánh chi nhánh | Biểu đồ: quán nào doanh thu cao nhất? Chi phí bất thường? |
| | A-03 | P&L (Lãi/Lỗ) tự động | Doanh thu − Chi phí = Lợi nhuận ròng từng quán, từng kỳ |
| | A-04 | Cảnh báo real-time | NV vắng, két chênh, kho hết, feedback ≤ 2 sao → alert tức thì |
| **Menu & Giá** | A-05 | Tạo/Sửa/Xóa menu | Tạo món mới kèm ảnh, giá, mô tả, công thức, nguyên liệu → đồng bộ chuỗi |
| | A-06 | Giá theo chi nhánh | Latte Q1: 55K. Thủ Đức: 45K — tùy chỉnh riêng từng chi nhánh |
| | A-07 | Bật/Tắt món & Availability | Hết sữa → tắt tất cả món có sữa ngay lập tức, hoặc lên lịch menu mùa tự bật/tắt |
| | A-08 | Quản lý Combo | Tạo combo: Latte + Croissant = 75K (tiết kiệm 15K). Duyệt gợi ý từ AI-2. |
| **Nhân sự & CRM** | A-09 | Quản lý NV & Tài khoản | Thêm/sửa/xóa NV, quản lý tài khoản, phân quyền, xem chấm công toàn chuỗi |
| | A-10 | Quản lý Loyalty | Cấu hình tích điểm, tạo voucher, thiết lập hạng thành viên (membership tiers) |
| | A-11 | Quản lý Promotion | Giảm 20% khung 14-16h, Buy 1 Get 1, voucher sinh nhật, chain-wide announcements |
| | A-12 | Xem CRM & Customer History | Lịch sử khách hàng, chi tiêu, tần suất, voucher đã dùng, sở thích |
| **AI** | A-13 | 🤖 **AI Combo Suggestion (AI-2)** | Phân tích dữ liệu bán hàng bằng Apriori/FP-Growth → "68% khách mua Latte cũng mua Croissant → tạo combo 75K". Admin duyệt trước khi publish. Đánh giá bằng support, confidence, lift. |
| **Quản trị** | A-14 | Xem Feedback & Review | Review tất cả chi nhánh kèm ảnh, trạng thái xử lý, lịch sử response |
| | A-15 | Export Báo Cáo | Xuất doanh thu, kho, chấm công, CRM, tài chính → file Excel/PDF |
| | A-16 | Audit Log | Ghi lại mọi thao tác: ai sửa giá, ai hủy đơn, ai chỉnh kho, lúc nào |
| | A-17 | RBAC phân quyền | QL chỉ xem kho + doanh thu quán mình, không thấy lương chuỗi. Branch-level data isolation. |
| | A-18 | Quản lý Chi nhánh | Thêm/sửa chi nhánh, giờ hoạt động, cấu hình riêng |

> **🔮 Future Work (Không triển khai trong Capstone):**
>
> | # | AI Module | Mô tả | Lý do chưa triển khai |
> |---|---|---|---|
> | A-FW1 | AI-3 Business Analytics | Hỏi AI bằng NLP: "Doanh thu tuần này?" → AI trả lời kèm biểu đồ | Cần NL query engine + RAG pipeline phức tạp |
> | A-FW2 | AI-4 Churn Prediction | Dự đoán khách sắp bỏ đi → tự gửi voucher giữ chân | Cần train RF/XGBoost + đủ data CRM |
> | A-FW3 | AI-5 Menu Intelligence | Phân tích trend món → gợi ý thêm/loại/thay đổi menu | Cần time-series + clustering + elasticity analysis |
>
> Ba modules này được **thiết kế sẵn trong kiến trúc** (API contracts, database schema, extension points) nhưng chưa implement code trong phạm vi Capstone.

---

## 🔐 BẢNG PHÂN QUYỀN (RBAC MATRIX)

| Chức năng | 👤 Khách | 🧋 Barista | 🏪 Quản lý | 👑 Admin |
|---|---|---|---|---|
| **Xem menu & đặt món** | ✅ | ❌ | ❌ | ❌ |
| **AI Chatbot gợi ý món (AI-1)** | ✅ | ❌ | ❌ | ❌ |
| **Feedback & Review** | ✅ | ❌ | 🔍 Xem & xử lý | 🔍 Xem toàn chuỗi |
| **Nhận đơn trên KDS** | ❌ | ✅ | ❌ | ❌ |
| **Báo hết món** | ❌ | ✅ | ✅ | ✅ |
| **Chấm công** | ❌ | ✅ | 🔍 Xem | 🔍 Xem |
| **Mở/Kết ca** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Xuất kho quầy (Requisition)** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Nhập kho NCC (Goods Receipt)** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Kiểm kê (Stocktaking)** | ❌ | ❌ | ✅ | 🔍 Xem |
| **Xem báo cáo doanh thu** | ❌ | ❌ | ✅ Quán mình | ✅ Toàn chuỗi |
| **Quản lý Menu/Giá** | ❌ | ❌ | ❌ | ✅ |
| **Tạo Combo / Khuyến mãi** | ❌ | ❌ | ❌ | ✅ |
| **AI Combo Suggest (AI-2)** | ❌ | ❌ | ❌ | ✅ Duyệt & Publish |
| **Quản lý Loyalty/Voucher** | ❌ | ❌ | ❌ | ✅ |
| **Quản lý NV toàn chuỗi** | ❌ | ❌ | ❌ | ✅ |
| **RBAC phân quyền** | ❌ | ❌ | ❌ | ✅ |
| **Audit Log** | ❌ | ❌ | ❌ | ✅ |
| **Export Excel/PDF** | ❌ | ❌ | ❌ | ✅ |

> 🔑 **Nguyên tắc phân quyền:** Mỗi Actor chỉ thấy và thao tác được những gì thuộc phạm vi vai trò. Quản lý chỉ xem data quán mình. Admin xem toàn chuỗi. Barista chỉ tương tác với KDS. Khách chỉ dùng QR Order PWA.

---

## 🤖 AI MODULE — ACTOR NÀO DÙNG AI NÀO?

### ✅ Triển khai trong Capstone (2 Modules)

| AI Module | Mô Tả | Actor Sử Dụng | Phương pháp đánh giá |
|---|---|---|---|
| **AI-1** — Recommendation Chatbot | Gợi ý món theo khẩu vị, dị ứng, thời tiết, lịch sử CRM qua RAG + content-based/hybrid | 👤 Khách hàng | Precision@K, Recall@K, NDCG, coverage, response time. **Module nghiên cứu chính.** |
| **AI-2** — Combo Suggestion | Phân tích data bán hàng bằng Apriori/FP-Growth → gợi ý combo | 👑 Admin (duyệt trước khi publish) | Support, confidence, lift. **Đánh giá nhẹ hơn AI-1.** |

### 🔮 Future Work (3 Modules — Chỉ thiết kế kiến trúc, KHÔNG implement)

| AI Module | Mô Tả | Actor dự kiến | Lý do chưa triển khai |
|---|---|---|---|
| **AI-3** — Business Analytics | Hỏi AI bằng NLP, trả lời kèm biểu đồ doanh thu/vận hành | 🏪 Manager (quán mình) + 👑 Admin (toàn chuỗi) | Scope quá rộng cho team 4 người |
| **AI-4** — Churn Prediction | Dự đoán khách sắp bỏ đi → tự gửi voucher kéo lại | 👑 Admin (cấu hình) → ⚙️ Tự động | Cần train classification model + đủ CRM data |
| **AI-5** — Menu Intelligence | Phân tích trend món → gợi ý thêm/loại/khuyến mãi | 👑 Admin | Cần time-series + demand analysis phức tạp |

> **Barista KHÔNG dùng AI.** Công thức pha đã hiển thị tự động kèm mỗi đơn trên KDS.

---

## 📊 THỐNG KÊ SỐ LIỆU

| Chỉ Tiêu | Bản Gốc | Bản Revised |
|---|---|---|
| Tổng số Actor | **4** | **4** (không đổi) |
| Tổng số tính năng | 71 (24+12+13+22) | **66** (24+12+12+18) |
| AI Module triển khai | 5 | **2** (Chatbot + Combo) |
| AI Module future work | 0 | **3** (Analytics, Churn, Menu Intel) |
| Actor dùng AI nhiều nhất | 👑 Admin (4 AI) | 👑 Admin (**1 AI**: Combo) |
| Actor có nhiều tính năng nhất | 👤 Khách hàng (24) | 👤 Khách hàng (**24** — không đổi) |
| Actor có quyền cao nhất | 👑 Admin | 👑 Admin (không đổi) |
| Module nghiên cứu chính | AI-1 Business Analytics | **AI-1 Recommendation Chatbot** |

---

## 📝 MAPPING: DOCX SECTION → ACTOR FEATURES

Bảng tra ngược từ nội dung file `Smart_FB_OS_Revised_4members.docx` sang mã tính năng Actor:

| Nội dung trong Docx (Section c) | Actor | Feature IDs |
|---|---|---|
| Customer Identification & QR Ordering | 👤 Customer | C-00 → C-06 |
| Order tracking, estimated time, notification | 👤 Customer | C-14, C-15, C-16 |
| Bill request, payment, voucher | 👤 Customer | C-07 → C-11 |
| Customer Feedback, CRM & Loyalty | 👤 Customer | C-18 → C-21, C-24 |
| AI-1 Recommendation Chatbot | 👤 Customer | C-12 |
| Kitchen Display & Staff Operations | 🧋 Barista | S-01 → S-12 |
| Branch Management | 🏪 Manager | M-01 → M-12 |
| Owner, Administration & Multi-Branch | 👑 Admin | A-01 → A-18 |
| AI-2 Combo Suggestion | 👑 Admin | A-13 |

---
---

# 📋 CATALOGUE TÍNH NĂNG TOÀN HỆ THỐNG — SMART F&B OS

> **Dành cho:** Khách hàng / Stakeholder review
>
> Tài liệu liệt kê toàn bộ tính năng của hệ thống Smart F&B OS, phân theo **7 nhóm chức năng** (Module). Mỗi tính năng được đánh mã, mô tả ngắn gọn và gắn với Actor sử dụng.

---

## MODULE 1: 📱 ĐẶT MÓN QR & TRẢI NGHIỆM KHÁCH HÀNG

> Khách hàng scan QR tại bàn → mở menu trên trình duyệt → chọn & tùy chỉnh món → gửi đơn → theo dõi → thanh toán. Không cần cài app.

| # | Tính năng | Mô tả | Actor |
|---|---|---|---|
| F-01 | 🔲 QR Code theo bàn & chi nhánh | Mỗi bàn có mã QR riêng, hệ thống tự nhận diện bàn + chi nhánh khi khách scan | 👤 Khách |
| F-02 | 📲 PWA không cần cài app | Mở menu trực tiếp trên trình duyệt điện thoại, responsive mobile-first | 👤 Khách |
| F-03 | 📞 Nhận diện khách bằng SĐT | Nhập SĐT tùy chọn → khách mới tạo hồ sơ CRM, khách quen nạp loyalty + lịch sử | 👤 Khách |
| F-04 | 🍽️ Menu trực quan theo chi nhánh | Phân loại danh mục, ảnh, giá riêng chi nhánh, mô tả, tag Best Seller / Mới | 👤 Khách |
| F-05 | ⚙️ Tùy chỉnh món chi tiết | Chọn Size (S/M/L), Đường (0-100%), Đá, Topping, số lượng | 👤 Khách |
| F-06 | 📝 Ghi chú tự do | Khách ghi yêu cầu đặc biệt: "Ít đá, thêm shot espresso, không kem" | 👤 Khách |
| F-07 | 🛒 Quản lý giỏ hàng | Thêm/bớt/xóa nhiều món, chỉnh số lượng trước khi gửi đơn | 👤 Khách |
| F-08 | 🏠 Chọn Tại quán / Mang đi | "Tại bàn" (gắn số bàn) hoặc "Mang đi" (Takeaway entry point riêng) | 👤 Khách |
| F-09 | ➕ Gọi thêm món vào đơn đang chạy | Thêm món vào đơn hiện tại trên bàn, không tạo đơn mới | 👤 Khách |
| F-10 | ⏱️ Theo dõi trạng thái đơn | Thanh tiến trình real-time: Đã xác nhận → Đang pha chế → Sẵn sàng 🔔 | 👤 Khách |
| F-11 | ⏳ Thời gian chờ ước tính | Hiện "Dự kiến xong sau ~8 phút" dựa trên hàng đợi KDS | 👤 Khách |
| F-12 | 🔔 Thông báo khi món xong | Push notification trên trình duyệt khi barista bấm hoàn thành | 👤 Khách |
| F-13 | 🙋 Gọi nhân viên phục vụ | Nút "Gọi nhân viên 🔔" → Staff nhận alert: "Bàn 5 cần hỗ trợ" | 👤 Khách |
| F-14 | 🥜 Thông tin dị ứng & Calories | Hiện thành phần nguyên liệu, cảnh báo dị ứng, calories ước tính từng món | 👤 Khách |
| F-15 | ⭐ Món yêu thích / Quick Reorder | Dựa lịch sử CRM hiện "Món của bạn" → đặt lại 1 click | 👤 Khách |

---

## MODULE 2: 💳 THANH TOÁN & HÓA ĐƠN

> Thanh toán tại bàn hoặc quầy bằng tiền mặt / VietQR. Nhân viên xác nhận thanh toán — chỉ khi đó doanh thu, loyalty và báo cáo mới được cập nhật.

| # | Tính năng | Mô tả | Actor |
|---|---|---|---|
| F-16 | 💳 Yêu cầu thanh toán | Khách bấm "Yêu cầu thanh toán" → Staff nhận alert → mang bill ra bàn | 👤 Khách → 🧋 Staff |
| F-17 | 💵 Thanh toán tiền mặt | Khách trả tiền mặt tại bàn hoặc quầy → Staff xác nhận trên hệ thống | 👤 Khách → 🧋 Staff |
| F-18 | 📱 Thanh toán VietQR | Staff xuất mã VietQR → khách chuyển khoản → Staff xác nhận nhận tiền | 👤 Khách → 🧋 Staff |
| F-19 | 🎫 Áp mã voucher / giảm giá | Khách chọn voucher khả dụng hoặc nhập mã → hệ thống tự tính giảm giá | 👤 Khách |
| F-20 | 🧾 In hóa đơn (Receipt) | Kết nối máy in nhiệt → in bill khi khách yêu cầu | 🧋 Staff |
| F-21 | 📊 Cập nhật doanh thu real-time | Xác nhận thanh toán xong → Dashboard Manager/Admin cập nhật tức thì | ⚙️ Hệ thống |

---

## MODULE 3: 👨‍🍳 BẾP & VẬN HÀNH NHÂN VIÊN (KDS & Staff App)

> Đơn hàng từ QR Order được đẩy real-time qua WebSocket đến màn hình KDS tại quầy pha chế. Barista xem đơn, công thức chuẩn, pha chế và cập nhật trạng thái.

| # | Tính năng | Mô tả | Actor |
|---|---|---|---|
| F-22 | 📺 KDS nhận đơn real-time | Đơn hàng từ QR Order hiện TỨC THÌ trên màn hình KDS qua WebSocket | 🧋 Barista |
| F-23 | 📖 Hiện công thức pha chuẩn | Mỗi đơn kèm công thức chi tiết: "Espresso 2 shot + Sữa 200ml + Đá 150g + Đường 25%" | 🧋 Barista |
| F-24 | 📋 Hiện ghi chú & tùy chỉnh khách | Hiện rõ tất cả ghi chú: "Ít đá, không đường, thêm shot, dị ứng sữa" | 🧋 Barista |
| F-25 | 🚦 Ưu tiên theo thời gian chờ | Xanh (< 3 phút) → Vàng (3-5 phút) → Đỏ (> 5 phút) — visual priority | 🧋 Barista |
| F-26 | ✅ Cập nhật trạng thái đơn | Bấm "Đang pha" / "Hoàn thành" / "Phục vụ" → khách nhận thông báo | 🧋 Barista |
| F-27 | 🪑 Gom đơn theo bàn | "Bàn View" — gom tất cả order cùng bàn để mang 1 chuyến đủ | 🧋 Barista |
| F-28 | 🚫 Báo hết món | Bấm "Hết" → món tự ẩn ngay trên QR menu khách, ingredient liên quan cũng cập nhật | 🧋 Barista |
| F-29 | 🗺️ Sơ đồ bàn (Floor Map) | Xem trực quan bàn nào có khách (xanh/đỏ), bàn nào trống | 🧋 Staff |
| F-30 | 🔔 Alert gọi nhân viên & yêu cầu bill | Nhận thông báo "Bàn 5 cần hỗ trợ" / "Bàn 3 yêu cầu bill 💳" trên KDS & Staff App | 🧋 Staff |
| F-31 | 📱 Staff Mobile App | App di động nội bộ: alert, VietQR mobile, báo hết món, sơ đồ bàn, xác nhận thanh toán | 🧋 Staff |
| F-32 | ⏰ Chấm công QR + GPS | QR Code động (đổi 30s) + GPS Lock (bán kính 50m quán). Extension: máy vân tay/Face ID | 🧋 Staff |

---

## MODULE 4: ⭐ ĐÁNH GIÁ, CRM & LOYALTY

> Khách đánh giá từng món sau phục vụ, tải ảnh thực tế, chọn ẩn danh hoặc công khai. Hệ thống tự tích điểm, gửi voucher qua Zalo OA, quản lý hồ sơ khách hàng toàn bộ vòng đời.

| # | Tính năng | Mô tả | Actor |
|---|---|---|---|
| F-33 | ⭐ Đánh giá 1-5 sao từng món | Khách rate từng món đã uống/ăn, viết review chi tiết sau phục vụ | 👤 Khách |
| F-34 | 📸 Tải ảnh thực tế kèm review | Upload ảnh chụp món thực, file validation & content moderation | 👤 Khách |
| F-35 | 🕶️ Review ẩn danh hoặc công khai | Chọn hiện tên CRM hoặc ẩn danh; SĐT KHÔNG BAO GIỜ hiện công khai | 👤 Khách |
| F-36 | 🌟 Review công khai trên QR menu | Review được duyệt → hiện trên menu QR như social proof cho khách sau | 👤 Khách → ⚙️ Hệ thống |
| F-37 | 🚨 Alert đánh giá thấp (≤ 2 sao) | Rating ≤ 2 sao → cảnh báo tức thì cho Manager chi nhánh để xử lý | ⚙️ Hệ thống → 🏪 Manager |
| F-38 | 🏆 Tích điểm Loyalty tự động | Hoàn tất đơn → tự động cộng điểm vào SĐT khách | ⚙️ Hệ thống |
| F-39 | 📊 Hồ sơ CRM đầy đủ | Lịch sử: món đã gọi, số lần ghé, ngày cuối, tổng chi tiêu, sở thích, hạng thành viên | 👤 Khách → 👑 Admin |
| F-40 | 📨 Voucher tự động qua Zalo OA | Voucher sinh nhật, loyalty tier, "lâu ngày chưa ghé" → gửi qua Zalo OA tự động | ⚙️ Hệ thống |
| F-41 | 🎖️ Hạng thành viên (Membership Tiers) | Cấu hình tier: Silver / Gold / Platinum → ưu đãi riêng theo hạng | 👑 Admin |
| F-42 | 🎁 Quản lý Voucher & Promotion | Tạo voucher, giảm giá khung giờ, Buy 1 Get 1, chain-wide announcements | 👑 Admin |

---

## MODULE 5: 🏪 QUẢN LÝ CHI NHÁNH & VẬN HÀNH

> Quản lý chi nhánh thực hiện mở/kết ca, đối soát két tiền, quản lý nhân sự ca làm, nhập/xuất kho nguyên liệu, kiểm kê, và xem báo cáo vận hành hàng ngày.

| # | Tính năng | Mô tả | Actor |
|---|---|---|---|
| F-43 | 🔓 Mở ca làm việc | Nhập tiền mặt đầu két, hệ thống ghi nhận thời gian mở ca | 🏪 Manager |
| F-44 | 🔒 Kết ca làm việc | Đếm tiền thực tế cuối ca, nhập vào hệ thống | 🏪 Manager |
| F-45 | 💰 Đối soát két tiền | So sánh tiền hệ thống vs thực đếm → cảnh báo tự động nếu chênh > 50K | 🏪 Manager |
| F-46 | 📅 Quản lý lịch ca & xếp ca | Bảng ca tuần, duyệt đổi ca, thêm NV thay thế, xem overtime | 🏪 Manager |
| F-47 | 👥 Xem chấm công nhân viên | Danh sách check-in/check-out, đi muộn, overtime, payroll-supporting data | 🏪 Manager |
| F-48 | 📦 Xuất kho quầy (Requisition) | Phiếu xuất: "Xuất 2kg CF hạt + 5 hộp sữa từ Kho → Quầy" — traceable | 🏪 Manager |
| F-49 | 🚚 Nhập kho từ NCC (Goods Receipt) | NCC giao hàng → nhập phiếu → đối chiếu received vs purchase order | 🏪 Manager |
| F-50 | 📋 Kiểm kê (Stocktaking) | Nhập số thực đếm → hệ thống tính chênh lệch → ghi nhận wastage/abnormal loss | 🏪 Manager |
| F-51 | ⚠️ Cảnh báo kho thấp & hao hụt | "CF hạt còn 1.2kg — dự kiến hết trong 1 ngày" / cảnh báo hao hụt bất thường | ⚙️ Hệ thống |
| F-52 | 📊 Báo cáo doanh thu ca/ngày | Doanh thu, số đơn, AOV, top món, hourly demand — chỉ quán mình | 🏪 Manager |
| F-53 | 📧 Báo cáo EOD tự động | Cuối ca → hệ thống tổng hợp → gửi qua Zalo/Email cho Manager tự động | ⚙️ Hệ thống |
| F-54 | 🗺️ Quản lý sơ đồ bàn & cấu hình | Cấu hình bàn (Trong/Ngoài/VIP), giờ hoạt động, giá riêng chi nhánh | 🏪 Manager |

---

## MODULE 6: 👑 QUẢN TRỊ CHUỖI & ADMIN DASHBOARD

> Chủ chuỗi xem toàn bộ chi nhánh trên 1 dashboard real-time, quản lý menu/giá/combo tập trung, phân quyền RBAC, audit log, và xuất báo cáo tài chính.

| # | Tính năng | Mô tả | Actor |
|---|---|---|---|
| F-55 | 📊 Dashboard đa chi nhánh real-time | Doanh thu, số đơn, NV, cảnh báo — tất cả chi nhánh trên 1 màn hình | 👑 Admin |
| F-56 | 📈 So sánh chi nhánh | Biểu đồ so sánh: quán nào doanh thu cao nhất? Chi phí bất thường? | 👑 Admin |
| F-57 | 💹 P&L tự động (Lãi/Lỗ) | Doanh thu − Chi phí = Lợi nhuận ròng từng quán, từng kỳ, tự động tính | 👑 Admin |
| F-58 | 🚨 Cảnh báo vận hành real-time | NV vắng, két chênh, kho hết, feedback ≤ 2 sao → alert tức thì | 👑 Admin |
| F-59 | 🍽️ Quản lý Menu tập trung | Tạo/sửa/xóa món kèm ảnh, giá, mô tả, công thức, nguyên liệu → đồng bộ chuỗi | 👑 Admin |
| F-60 | 💲 Giá riêng theo chi nhánh | Latte Q1: 55K, Thủ Đức: 45K — tùy chỉnh riêng, đồng bộ tự động | 👑 Admin |
| F-61 | 🔄 Bật/Tắt món & Menu mùa | Tắt tất cả món chứa sữa khi hết sữa; lên lịch menu mùa tự bật/tắt theo ngày | 👑 Admin |
| F-62 | 🎯 Quản lý Combo | Tạo combo: Latte + Croissant = 75K (tiết kiệm 15K). Duyệt gợi ý từ AI. | 👑 Admin |
| F-63 | 👥 Quản lý NV & Tài khoản toàn chuỗi | Thêm/sửa/xóa NV, quản lý tài khoản, xem chấm công tất cả chi nhánh | 👑 Admin |
| F-64 | 🔐 RBAC phân quyền | Cấu hình quyền theo vai trò, data isolation theo chi nhánh | 👑 Admin |
| F-65 | 📝 Audit Log | Ghi lại mọi thao tác: ai sửa giá, ai hủy đơn, ai chỉnh kho, lúc nào, IP nào | 👑 Admin |
| F-66 | 📤 Export báo cáo Excel/PDF | Xuất doanh thu, kho, chấm công, CRM, tài chính → file Excel hoặc PDF | 👑 Admin |

---

## MODULE 7: 🤖 AI & PHÂN TÍCH THÔNG MINH

> Hệ thống tích hợp 2 module AI triển khai trong Capstone và 3 module thiết kế kiến trúc sẵn cho giai đoạn mở rộng.

### ✅ Triển khai trong phiên bản Capstone

| # | Tính năng | Mô tả | Actor | Đánh giá |
|---|---|---|---|---|
| F-AI-1 | 🤖 **Chatbot Gợi Ý Món** | Khách chat với AI: khẩu vị, dị ứng, thời tiết, lịch sử CRM → AI gợi ý món phù hợp. Dùng RAG + content-based/hybrid recommendation. **Module nghiên cứu chính.** | 👤 Khách | Precision@K, Recall@K, NDCG, coverage, response time |
| F-AI-2 | 🔗 **Gợi Ý Combo Bán Chạy** | Phân tích data đơn hàng bằng Apriori/FP-Growth → "68% khách mua Latte cũng mua Croissant → tạo combo 75K?". Admin duyệt trước khi publish. | 👑 Admin | Support, confidence, lift |

#### Ví dụ AI-1 Chatbot trong thực tế:

| Khách hỏi | AI trả lời | Logic |
|---|---|---|
| "Tôi thích vị đắng nhẹ, ít ngọt" | "Gợi ý: Americano (0% đường) hoặc Cappuccino (đường 25%)" | Content-based: tag vị đắng → filter menu |
| "Hôm nay nóng quá, gợi ý đi" | "Trà Đào Cam Sả đá ❄️ — bán chạy nhất hôm nay!" | Weather API + data bán hàng real-time |
| "Món bán chạy nhất ở đây là gì?" | "Top 3 hôm nay: 1. Bạc Xỉu (42 ly) 2. Latte (38 ly) 3. Trà Đào (29 ly)" | Query data đơn hàng trong ngày |
| "Tôi bị dị ứng sữa" | Lọc menu → chỉ hiện: Americano, Trà Đào, Nước ép... (ẩn món có sữa) | Allergen filter + menu data |
| "Lần trước tôi uống gì?" | "Lần trước (12/07) bạn đặt Latte L + Croissant. Đặt lại nhé?" | Lịch sử CRM (nếu đã có SĐT) |
| "Combo nào tiết kiệm nhất?" | "Combo Latte + Bánh Flan: 75K (tiết kiệm 15K so với mua lẻ)" | Combo engine + AI-2 data |

#### Ví dụ AI-2 Combo trong thực tế:

| Phát hiện | Gợi ý cho Admin | Dữ liệu |
|---|---|---|
| 68% khách mua Latte cũng mua Croissant | "Tạo Combo Latte + Croissant = 75K (tiết kiệm 15K)" | Support: 0.15, Confidence: 0.68, Lift: 2.3 |
| 55% khách mua Trà Đào cũng mua Bánh Flan | "Tạo Combo Trà Đào + Bánh Flan = 65K (tiết kiệm 10K)" | Support: 0.12, Confidence: 0.55, Lift: 1.9 |
| Combo sáng: Americano + Bánh Mì phổ biến 7-9h | "Combo Early Bird 7-9h: 45K (giảm 20%)" | Time-based association |

### 🔮 Thiết kế kiến trúc sẵn — Triển khai giai đoạn mở rộng

| # | Tính năng | Mô tả | Actor dự kiến | Ghi chú |
|---|---|---|---|---|
| F-AI-3 | 📊 **Thống kê doanh thu bằng AI** | Hỏi bằng ngôn ngữ tự nhiên: "So sánh doanh thu Q1 vs Q3 tháng 8?" → AI trả lời kèm biểu đồ | 🏪 Manager + 👑 Admin | Cần NL query engine + analytical pipeline |
| F-AI-4 | 🔮 **Dự đoán khách rời bỏ (Churn)** | Phát hiện khách sắp bỏ đi → tự gửi voucher giữ chân: "Khách A: 78% churn risk → voucher 30%" | 👑 Admin → ⚙️ Auto | Cần train RF/XGBoost + đủ CRM data |
| F-AI-5 | 📈 **Menu Intelligence & Smart Promotion** | Phân tích trend: "Matcha +35% → thêm biến thể", "14-16h vắng → push combo giảm 20%" | 👑 Admin | Cần time-series + demand analysis |

---

## 📊 TỔNG HỢP NHANH

| Chỉ tiêu | Giá trị |
|---|---|
| **Tổng Module chức năng** | 7 |
| **Tổng tính năng vận hành** | 66 |
| **Tính năng AI triển khai** | 2 (Chatbot + Combo) |
| **Tính năng AI future work** | 3 (Analytics + Churn + Menu Intel) |
| **Số Actor** | 4 (Khách, Barista, Manager, Admin) |
| **Số giao diện** | 5 (QR PWA, KDS TV/Tablet, Staff App, Manager App/Web, Admin Dashboard) |
| **Công nghệ thanh toán** | Tiền mặt + VietQR (staff xác nhận) |
| **Real-time** | WebSocket (đơn hàng, trạng thái, cảnh báo) |
| **Không cần** | Máy POS chuyên dụng, App cài đặt, Online payment gateway |
