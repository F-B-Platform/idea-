# ☕ NỀN TẢNG QUẢN LÝ F&B THÔNG MINH (AI-Powered F&B Operating System)

## Đề Tài Đồ Án Tốt Nghiệp — Ngành Kỹ Thuật Phần Mềm

> **Tiếng Việt:** "Nền Tảng Quản Lý Chuỗi F&B Thông Minh Ứng Dụng Trí Tuệ Nhân Tạo và IoT"
>
> **Tiếng Anh:** "AI-Powered Smart F&B Chain Operating System with IoT Integration"

---
---

# 🔴 PHẦN 0: BẤT CẬP THỰC TẾ TRONG QUẢN LÝ QUÁN CÀ PHÊ TẠI VIỆT NAM

> **Ghi chú riêng:** Phần này tổng hợp các vấn đề "nhức nhối" mà hầu hết quán cà phê tại VN đang gặp phải — từ quán nhỏ lẻ đến chuỗi 10-50 chi nhánh. Đây là nền tảng để xây dựng giải pháp.

---

## 0.1 🕐 Bất Cập Về CHẤM CÔNG Nhân Viên

### Hiện trạng:
- **Chấm công bằng sổ tay:** Nhân viên tự ghi giờ vào/ra — **dễ gian lận** (nhờ đồng nghiệp ký hộ, ghi sai giờ).
- **Chấm công bằng vân tay nhưng không liên kết POS:** Có máy chấm công vân tay nhưng data nằm riêng, không kết nối với hệ thống tính lương → vẫn phải **export Excel rồi tính thủ công**.
- **Quản lý không giám sát được từ xa:** Chủ chuỗi có 5-10 quán, không biết nhân viên quán nào đến muộn, về sớm. Phải gọi điện từng quán hỏi.
- **Không có chế tài rõ ràng:** Nhân viên đến muộn 15 phút nhưng vẫn ghi "đúng giờ" → **mất công bằng**, nhân viên chăm chỉ thấy bất mãn.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Nhân viên đến muộn 15-30 phút mỗi ca | Giờ cao điểm sáng thiếu người → khách chờ lâu → mất khách |
| Gian lận chấm công (ký hộ) | Trả lương sai, tổn thất 5-10% quỹ lương/tháng |
| Không biết ai đang trực ca nào | Khi có sự cố (khách phàn nàn, mất đồ) → không quy trách nhiệm được |
| Tính lương thủ công cuối tháng | Kế toán mất 2-3 ngày tính lương cho 20-30 nhân viên, dễ sai sót |

---

## 0.2 📋 Bất Cập Về QUẢN LÝ CA LÀM VIỆC

### Hiện trạng:
- **Xếp ca bằng giấy / nhóm Zalo:** Quản lý post bảng ca lên Zalo mỗi tuần → nhân viên xin đổi ca qua tin nhắn → **hỗn loạn, quên, nhầm**.
- **Không dựa trên dữ liệu:** Xếp ca theo cảm tính — "thứ 7 đông nên cho thêm 1 người". Nhưng **thứ 7 tuần này mưa → vắng**, thừa người. Ngược lại, thứ 3 có sự kiện gần đó → **đông bất ngờ**, thiếu người.
- **Không công bằng:** Một số nhân viên bị xếp ca "xấu" liên tục (tối khuya, cuối tuần) → bất mãn, nghỉ việc. Turnover rate quán cà phê VN: **40-60%/năm**.
- **Nhân viên nghỉ đột xuất:** Không có hệ thống backup tự động → quản lý phải gọi điện từng người tìm người thay.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Giờ cao điểm thiếu người | Khách chờ >10 phút → 30% bỏ đi, mất doanh thu 500K-2M/ngày |
| Giờ vắng thừa người | Trả lương cho 4 người trong khi chỉ cần 2 → lãng phí 50% nhân công |
| Nhân viên bất mãn vì ca không công bằng | Turnover cao → chi phí tuyển + đào tạo: 5-8 triệu/người |
| Quản lý mất 3-5 tiếng/tuần xếp ca | Thời gian đáng lẽ dùng để quản lý chất lượng, chăm sóc khách |

---

## 0.3 📦 Bất Cập Về KIỂM KÊ HÀNG HÓA & NGUYÊN LIỆU

### Hiện trạng:
- **Không kiểm soát được nguyên liệu xuất từ kho lên quầy:** Khi lấy 2kg cà phê hạt, 5 hộp sữa tươi hay 2 chai syrup từ kho tổng lên quầy pha chế, nhân viên thường **không ghi chép sổ sách** → không biết Kho tổng còn bao nhiêu kg, Quầy đã nhận bao nhiêu.
- **Kiểm kê thủ công & phức tạp:** Cuối tháng/cuối tuần nhân viên phải đếm tay từng túi/hộp → mất 3-5 tiếng, dễ sai lệch giữa sổ sách và thực tế.
- **Không thể trừ kho chi tiết theo từng gram/ml:** Pha chế thực tế luôn có độ hao hụt (dial-in máy xay lãng phí 50-100g/ngày, trót tay đổ sữa...), nếu bắt hệ thống trừ từng gram theo từng ly sẽ **xa rời thực tế** và tạo ra chênh lệch ảo khổng lồ.
- **Hết nguyên liệu giữa ca:** Đang giờ cao điểm, nhân viên phát hiện hết sữa/cà phê trên quầy mà kho tổng cũng hết → phải chạy ra ngoài mua lẻ → **mất 30 phút**, khách chờ.
- **Thất thoát nguyên liệu 5-15%:** Xuất nguyên liệu lên quầy không ai kiểm soát → mất mát, dùng lãng phí hoặc thất thoát không rõ nguyên nhân.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Thất thoát nguyên liệu 5-15% | Quán doanh thu 200 triệu/tháng → mất 10-30 triệu/tháng không rõ lý do |
| Hết nguyên liệu giữa ca | Mất 20-50 đơn hàng/lần → thiệt hại 1-3 triệu VNĐ + mất uy tín |
| Kiểm kê thủ công sai lệch | Nhập thêm hàng không cần (tồn kho ảo) hoặc thiếu hàng cần |
| Không kiểm soát được nhà cung cấp | Mua giá cao hơn thị trường 10-20% vì không so sánh được |

---

## 0.4 💰 Bất Cập Về QUẢN LÝ TÀI CHÍNH & DOANH THU

### Hiện trạng:
- **Thu tiền mặt không kiểm soát:** Nhân viên thu tiền khách nhưng **không nhập đơn vào POS** → tiền vào túi riêng. Chủ quán không biết.
- **Không biết lợi nhuận thật:** Doanh thu 200 triệu/tháng, nhưng lợi nhuận bao nhiêu? Chi phí nguyên liệu? Chi phí nhân sự? Chi phí điện nước? → **Không ai tổng hợp được** vì dữ liệu nằm rải rác (POS 1 nơi, kho 1 nơi, lương 1 nơi).
- **Hóa đơn điện tử chưa phổ biến:** Nhiều quán vẫn xuất bill giấy, chưa tích hợp HĐĐT theo NĐ 123/2020 → **rủi ro thuế**.
- **So sánh chi nhánh bằng cảm tính:** Chủ chuỗi 5 quán không biết quán nào lãi nhất, quán nào đang "chảy máu" → quyết định dựa trên **cảm giác thay vì dữ liệu**.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Nhân viên bán không nhập POS | Thất thoát 3-8% doanh thu/tháng (= 6-16 triệu cho quán 200 triệu) |
| Không biết quán nào lỗ | Nuôi quán lỗ 6-12 tháng mới phát hiện → thiệt hại hàng trăm triệu |
| Không có báo cáo tài chính real-time | Ra quyết định chậm, bỏ lỡ cơ hội hoặc không cắt lỗ kịp |

---

## 0.5 🍵 Bất Cập Về CHẤT LƯỢNG SẢN PHẨM Không Đồng Nhất & Thiếu Data Feedback

### Hiện trạng:
- **Phụ thuộc tay nghề barista:** Cùng 1 công thức Latte, barista A pha ngon, barista B pha nhạt — vì **không có hệ thống kiểm soát thông số** (lượng cà phê, nhiệt độ sữa, thời gian chiết xuất).
- **Quán Q1 khác quán Q9:** Khách quen uống ở quán trung tâm, đến quán ngoại thành thấy "khác vị" → **mất niềm tin vào thương hiệu**.
- **Đào tạo barista mới mất 2-4 tuần:** Người mới phải học thuộc 30-50 công thức → **dễ sai**, phải có người kèm liên tục.
- **Khách không có kênh phản hồi kín đáo:** Khi món dở, khách thường im lặng bỏ đi hoặc bóc phốt lên MXH → chủ quán không biết ca nào, barista nào pha hỏng để khắc phục.
- **Không có data thực tế để cải tiến menu:** Không biết chính xác ly nào khách khen/chê → cải tiến menu bằng cảm tính thay vì dữ liệu thật từ khách.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Chất lượng không đồng nhất giữa chi nhánh | Mất 10-20% khách trung thành do "không đúng vị quen" |
| Barista mới pha sai | 5-10 ly bỏ/ngày × 40K/ly = 200-400K lãng phí/ngày |
| Khách bỏ đi do trải nghiệm kém mà quán không biết | Mất khách âm thầm, giảm doanh thu 15-25% |
| Cải tiến menu bằng cảm tính | Giữ món bán chậm/vị kém trên menu → lãng phí nguyên liệu & nguyên cớ mất khách |

---

## 0.6 📱 Bất Cập Về QUẢN LÝ KHÁCH HÀNG & Loyalty

### Hiện trạng:
- **Thẻ tích điểm giấy:** Nhiều quán vẫn dùng thẻ giấy đóng dấu → khách **mất thẻ, quên mang**, hoặc giả mạo dấu.
- **Không biết khách hàng là ai:** Khách đến 20 lần nhưng quán không biết tên, sở thích, hay **tổng chi tiêu** → không có cách chăm sóc VIP.
- **Không nhắn tin/thông báo được:** Muốn gửi khuyến mãi cho khách cũ nhưng **không có thông tin liên hệ** (chỉ có thẻ giấy, không có số điện thoại).
- **Khách "churn" (bỏ đi) không biết:** Khách trung thành mua mỗi ngày, đột nhiên biến mất 2 tuần → **không ai phát hiện**, không có cơ chế giữ chân.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Mất khách trung thành không biết | Chi phí tìm khách mới đắt gấp 5-7 lần giữ khách cũ |
| Không có chương trình loyalty hiệu quả | Khách dễ chuyển sang đối thủ khi có khuyến mãi |
| Không biết sở thích khách | Không upsell/cross-sell được → doanh thu/khách thấp |

---

## 0.7 📋 Bất Cập Về BÁO CÁO CUỐI NGÀY (EOD Report) Thủ Công

### Hiện trạng:
- **Tổng hợp doanh thu cuối ca bằng tay:** Cuối mỗi ca (hoặc cuối ngày), quản lý phải tự đếm tiền mặt trong két, đối chiếu với sổ bán hàng, cộng thêm tiền chuyển khoản/MoMo → **mất 30-60 phút mỗi tối**.
- **Gửi báo cáo qua Zalo cho chủ quán:** Quản lý chụp sổ hoặc gõ tay số liệu gửi tin nhắn Zalo → **dễ gõ sai số**, chủ quán nhận 5-10 tin Zalo mỗi tối từ 5 chi nhánh khác nhau, **không tổng hợp được**.
- **Không phát hiện chênh lệch tiền mặt kịp thời:** Tiền trong két thiếu so với số đơn trong POS nhưng phải đến cuối tháng kiểm toán mới biết → **mất dấu vết, không quy được trách nhiệm**.
- **Chủ chuỗi không có bức tranh tổng quan:** Muốn biết "hôm nay toàn chuỗi doanh thu bao nhiêu?" phải đợi quản lý từng quán gửi số → **biết vào sáng hôm sau**, không real-time.

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Tổng hợp báo cáo thủ công mỗi tối | Quản lý mất 30-60 phút/ngày = ~15-30 giờ/tháng lãng phí |
| Số liệu gõ tay sai sót | Chênh lệch 2-5% doanh thu báo cáo vs thực tế |
| Chủ chuỗi không có dashboard real-time | Ra quyết định chậm 12-24 tiếng, không cắt lỗ kịp |

---

## 0.8 🧠 Bất Cập Về THIẾU DATA ĐỂ RA QUYẾT ĐỊNH MENU & THỊ TRƯỜNG

### Hiện trạng:
- **Thêm/bỏ món theo cảm tính:** Chủ quán thấy quán bạn bán Matcha chạy → bắt chước thêm vào menu mà **không biết khách của mình có thích không**.
- **Không biết món nào đang lên/xuống:** Có 40 món trên menu nhưng không biết top 5 bán chạy nhất đang tăng hay giảm doanh thu theo tuần → **giữ món kém, bỏ lỡ trend**.
- **Giá bán chưa tối ưu:** Không biết tăng giá 5K/ly khách có bỏ không, giảm giá 10K có kéo thêm khách không → **quyết định giá bằng linh cảm**.
- **Không biết thời điểm tốt nhất để khuyến mãi:** Push khuyến mãi lúc quán đã đông (lãng phí margin) thay vì lúc vắng (kéo khách).

### Hậu quả thực tế:
| Vấn đề | Thiệt hại |
|---|---|
| Thêm món không phù hợp khách hàng | Tốn chi phí nguyên liệu mới + đào tạo pha chế, bán được 2-3 ly/ngày rồi bỏ |
| Giữ 10-15 món bán chậm trên menu | Chiếm chỗ, gây khó khăn kiểm kê, lãng phí nguyên liệu |
| Khuyến mãi sai thời điểm | Giảm margin khi không cần, không kéo khách khi cần |

---
---

# 📝 PHẦN I: TỔNG QUAN VÀ BÀI TOÁN

## 1. 📌 MÔ TẢ HỆ THỐNG

**Hệ thống "all-in-one"** cho chuỗi nhà hàng / quán cà phê / trà sữa, tích hợp:
- Quản lý bán hàng (POS) — order, thanh toán đa phương thức
- Quản lý kho nguyên liệu (BOM) — tự động trừ kho, đề xuất nhập hàng
- Quản lý khách hàng (CRM + Loyalty) — tích điểm, churn prediction
- AI dự báo doanh thu & lượng khách — forecast 7-30 ngày
- Chatbot đặt bàn/đặt món qua Zalo/Facebook — NLP tiếng Việt
- Quản lý nhân sự & ca làm việc (HRM) — chấm công, xếp ca AI
- Dashboard phân tích kinh doanh — real-time, so sánh chi nhánh
- Hóa đơn điện tử & báo cáo thuế — tích hợp API HĐĐT

**Đối thủ thực tế tại VN:** iPOS.vn, CukCuk (MISA), PosApp, KiotViet

**Lợi thế cạnh tranh:** Tất cả đối thủ trên **CHƯA CÓ AI thực sự** — chỉ có báo cáo thống kê cơ bản. Không có: dự báo doanh thu, gợi ý combo, churn prediction, chatbot NLP tiếng Việt, AI xếp ca, IoT giám sát thiết bị.

---

## 2. 🔴 CÁC VẤN ĐỀ NGHIÊM TRỌNG CẦN GIẢI QUYẾT (Tóm Tắt 8 Bất Cập)

| # | Vấn Đề | Phạm Vi | Thiệt Hại Ước Tính |
|---|---|---|---|
| **V1** | Chấm công gian lận, không giám sát từ xa | HRM | 5-10% quỹ lương/tháng |
| **V2** | Xếp ca theo cảm tính, không dựa trên data | HRM | Lãng phí 50% nhân công giờ vắng, thiếu giờ đông |
| **V3** | Kiểm kê thủ công, thất thoát nguyên liệu | Kho | 5-15% nguyên liệu thất thoát (10-30 triệu/tháng) |
| **V4** | Không biết lợi nhuận thật, quản lý tài chính rời rạc | Tài chính | Ra quyết định sai, nuôi quán lỗ hàng tháng |
| **V5** | Chất lượng sản phẩm không đồng nhất giữa chi nhánh | Sản phẩm | Mất 10-20% khách trung thành |
| **V6** | Không quản lý được khách hàng, không giữ chân được | CRM | Chi phí tìm khách mới đắt gấp 5-7 lần |
| **V7** | Báo cáo cuối ngày (EOD) thủ công, chủ chuỗi không có dashboard | Báo cáo | Mất 30-60 phút/tối, sai sót 2-5% số liệu |
| **V8** | Thiếu data phân tích xu hướng menu & thị trường | Menu/KD | Thêm/bỏ món theo cảm tính, khuyến mãi sai thời điểm |

---
---

# 📝 PHẦN II: HƯỚNG GIẢI QUYẾT — HỆ THỐNG ĐỀ XUẤT

## 3. ✅ Giải Quyết V1 (Chấm Công) → QR Check-in + GPS Lock + AI Giám Sát

| Trước (Thủ công) | Sau (Hệ thống F&B OS) |
|---|---|
| Sổ tay / vân tay không liên kết | **QR code + GPS lock**: Check-in phải ở đúng quán (bán kính 50m) |
| Ký hộ dễ dàng | **Selfie check-in**: Chụp ảnh xác nhận → AI face recognition (tùy chọn) |
| Chủ chuỗi không biết ai đến muộn | **Dashboard real-time**: Xem tất cả chi nhánh — ai đang trực, ai đến muộn |
| Tính lương thủ công 2-3 ngày | **Tự động tính lương**: Giờ làm × đơn giá + phụ cấp + thưởng → 1 click |

**Kết quả:** Giảm gian lận chấm công về 0%. Tiết kiệm 2-3 ngày tính lương/tháng.

---

## 4. ✅ Giải Quyết V2 (Xếp Ca) → AI Demand Forecast + Smart Scheduling

| Trước (Cảm tính) | Sau (AI-powered) |
|---|---|
| Xếp ca dựa trên "tuần trước đông thì tuần này cũng đông" | AI phân tích **thời tiết + sự kiện + lịch sử** → dự báo lượng khách từng giờ |
| Nhân viên xin đổi ca qua Zalo → hỗn loạn | **App đổi ca**: Nhấn nút xin đổi → hệ thống tìm người thay → phê duyệt tự động |
| Quản lý mất 3-5 tiếng/tuần xếp ca | AI **tự đề xuất bảng ca tối ưu** → quản lý chỉ cần review + duyệt |
| Ca "xấu" phân bổ không công bằng | AI phân bổ ca **công bằng** — rotate ca tối, ca cuối tuần đều giữa các nhân viên |

**AI cụ thể:**
- **Input:** Doanh thu lịch sử theo giờ + thời tiết + ngày lễ + sự kiện khu vực
- **Model:** XGBoost time-series → dự báo lượng khách từng khung giờ
- **Output:** "Thứ 7 tuần này: dự báo 180 khách (tăng 20% do sự kiện gần quán) → cần 5 nhân viên thay vì 4"

**Kết quả:** Giảm 30% chi phí nhân sự lãng phí. Giảm 50% thời gian xếp ca.

---

## 5. ✅ Giải Quyết V3 (Kiểm Kê) → Quản Lý Xuất Kho Quầy + AI Đề Xuất Nhập Hàng (Theo Kg/Hộp/Chai)

| Trước (Thủ công / Sai lệch) | Sau (Hệ thống F&B OS Thực Tế) |
|---|---|
| Xuất hàng từ kho lên quầy không ghi chép | **Quản lý xuất kho quầy**: Ghi nhận chính xác mỗi lần chuyển nguyên liệu từ Kho tổng lên Quầy (VD: xuất 2kg cà phê, 5L sữa, 1 chai syrup) |
| Cố trừ kho từng gram theo ly (sai số lớn) | **Theo dõi tồn kho theo đơn vị thực tế (Kg/Hộp/Chai)**: Quản lý lượng nguyên liệu xuất lên quầy & tồn kho tổng, phù hợp thực tế vận hành |
| Kiểm kê cuối tháng 3-5 tiếng | **Kiểm kê kho & quầy nhanh**: Nhập số lượng thực tế kiểm đếm (Kg/Hộp/Chai) → Hệ thống tự động tính toán chênh lệch |
| Hết nguyên liệu giữa ca | **Alert cảnh báo ngưỡng tồn kho**: Cảnh báo khi tồn kho tổng hoặc tồn quầy < mức tối thiểu (VD: "Cà phê kho tổng còn 2kg — cần nhập thêm") |
| Nhập hàng theo cảm tính | **AI đề xuất nhập hàng**: Dự báo tốc độ tiêu thụ nguyên liệu (Kg/Lít/Chai) trong 7-30 ngày tới → tạo đơn nhập hàng tối ưu |

**AI cụ thể:**
- **Input:** Lịch sử xuất kho quầy (Kg/Hộp/Chai) + Lịch sử doanh số đơn hàng + Tồn kho thực tế + Lead time NCC
- **Model:** XGBoost + time-series decomposition
- **Output:** Đề xuất số lượng nguyên liệu (Kg cà phê, Hộp sữa, Chai syrup) cần nhập từ Nhà cung cấp cho tuần/tháng tới.

**Kết quả:** Giảm thất thoát xuống <2%. Thực tế hóa quản lý kho. Giảm 80% thời gian kiểm kê. Không bao giờ hết hàng giữa ca.

---

## 6. ✅ Giải Quyết V4 (Tài Chính) → Dashboard Real-time + Hóa Đơn Điện Tử

| Trước (Rời rạc) | Sau (Tích hợp) |
|---|---|
| POS 1 nơi, kho 1 nơi, lương 1 nơi | **1 dashboard duy nhất**: Doanh thu - Chi phí nguyên liệu - Nhân sự - Điện = Lợi nhuận |
| Không biết quán nào lãi/lỗ | **Ranking chi nhánh real-time**: Quán A lãi 25%, Quán B lỗ 5% → ra quyết định nhanh |
| Bill giấy, không có HĐĐT | **Tích hợp API HĐĐT** (VNPT/Viettel) → xuất hóa đơn điện tử 1 click |
| Nhân viên bán không nhập POS | **Mọi đơn phải qua POS** → hệ thống kiểm soát → giảm thất thoát tiền mặt |

**Kết quả:** Biết lợi nhuận thật mỗi ngày. Phát hiện quán lỗ ngay lập tức thay vì sau 6-12 tháng.

---

## 7. ✅ Giải Quyết V5 (Chất Lượng & Feedback) → Công Thức Chuẩn Hóa + IoT + QR Customer Feedback

| Trước (Phụ thuộc & Không data) | Sau (Chuẩn hóa + QR Feedback + IoT) |
|---|---|
| Barista pha theo cảm tính | **Công thức pha chế chuẩn hóa**: Quy định chuẩn 1 Latte (18g cà phê, 200ml sữa 65°C, chiết xuất 25s) hiển thị trên App pha chế |
| Quán Q1 khác quán Q9 | **Cùng 1 quy chuẩn công thức trên hệ thống** — barista nào cũng tuân thủ đúng tỷ lệ |
| Khách bị phục vụ dở im lặng bỏ đi | **QR Code Feedback tại bàn / trên Bill**: Khách scan QR qua Zalo Mini App chấm 1-5 sao + chọn lý do (VD: "nhạt", "ngọt quá", "phục vụ chậm") |
| Không biết ca nào/món nào dở | **Alert Real-time & Auto-Voucher đền bù**: Feedback ≤ 2 sao → alert quản lý ngay + tự động gửi voucher đền bù giữ chân khách |
| Cải tiến menu bằng cảm tính | **AI Data Analytics Feedback**: Gom dữ liệu đánh giá theo chi nhánh/ca làm/từng món → cải tiến menu & đào tạo nhân sự dựa trên data thực tế |

**Quy trình QR Feedback thực tế:**
1. In mã QR cá nhân hóa ở chân hóa đơn / dán sticker QR tại bàn.
2. Khách scan QR bằng Zalo Mini App → Chấm sao + chọn đánh giá chất lượng món & thái độ phục vụ.
3. Nếu đánh giá 1-2 sao → Hệ thống gửi thông báo khẩn tới Zalo Manager + gửi tặng tự động Voucher đền bù cho khách.
4. Dashboard phân tích điểm Rating trung bình từng món & từng ca làm việc của từng chi nhánh.

**IoT cụ thể (cho quán premium/chuỗi lớn):**
- **Sensor nhiệt độ** trên group head máy espresso: đảm bảo nước 90-96°C
- **Flow meter** đo lưu lượng nước: đảm bảo 25-30ml espresso shot
- **Smart scale** (cân điện tử Bluetooth): hỗ trợ cân cà phê định lượng tại quầy khi xay

**Kết quả:** Chất lượng đồng nhất 95%+. Xử lý 100% sự cố khách phàn nàn ngay tại chỗ. Tối ưu menu 100% dựa trên data thật.

---

## 8. ✅ Giải Quyết V6 (Khách Hàng) → CRM + Loyalty Digital + AI Churn Prediction

| Trước (Thẻ giấy) | Sau (CRM + AI) |
|---|---|
| Thẻ tích điểm giấy, dễ mất | **Loyalty digital**: Tích điểm qua SĐT hoặc QR trên app |
| Không biết khách là ai | **Hồ sơ khách hàng**: Tên, SĐT, lịch sử mua, món ưa thích, tổng chi tiêu |
| Khách bỏ đi không biết | **AI Churn Prediction**: "Khách Nguyễn Văn A — mua mỗi ngày, nay 10 ngày không mua → gửi voucher giữ chân" |
| Khuyến mãi rải đều không hiệu quả | **AI phân nhóm khách**: VIP gửi voucher 50K, Regular gửi thông báo món mới, Churned gửi "Nhớ bạn" 30% off |

**AI cụ thể:**
- **Input:** Lịch sử mua hàng (tần suất, giá trị, món) + khoảng cách giữa các lần mua
- **Model:** Random Forest / XGBoost classification
- **Output:** Danh sách khách có xác suất churn > 60% → trigger auto-voucher qua Zalo OA

**Kết quả:** Giữ chân thêm 15-25% khách sắp "bỏ đi". Tăng 20% doanh thu từ khách quay lại.

---

## 9. ✅ Giải Quyết V7 (Báo Cáo Cuối Ngày) → Auto EOD Report + Dashboard Real-time Chuỗi

| Trước (Thủ công + Zalo) | Sau (Tự động hóa hoàn toàn) |
|---|---|
| Quản lý đếm két tiền, gõ số liệu gửi Zalo | **Auto EOD Report**: Hệ thống tự tổng hợp doanh thu (tiền mặt + chuyển khoản + ví điện tử) cuối ca → gửi báo cáo tự động qua Zalo/Email |
| Chủ chuỗi nhận 5-10 tin Zalo mỗi tối | **Dashboard chuỗi real-time**: 1 màn hình duy nhất xem doanh thu, số đơn, so sánh chi nhánh — mọi lúc, mọi nơi |
| Chênh lệch tiền mặt phát hiện trễ | **Đối soát két tiền cuối ca**: Nhập số tiền mặt thực đếm → hệ thống so sánh vs doanh thu tiền mặt trên POS → cảnh báo ngay nếu chênh lệch > 50K |
| Sáng hôm sau mới biết doanh thu hôm qua | **Push notification**: Kết ca → chủ quán nhận ngay thông báo: "Chi nhánh Nguyễn Huệ — Ca tối: 8.5 triệu, 127 đơn, tiền mặt khớp 100%" |

**Kết quả:** Quản lý tiết kiệm 30-60 phút mỗi tối. Chủ chuỗi biết doanh thu real-time 24/7. Phát hiện chênh lệch tiền ngay trong ca.

---

## 10. ✅ Giải Quyết V8 (Menu Intelligence) → AI Phân Tích Xu Hướng & Gợi Ý Chiến Lược Menu

| Trước (Cảm tính) | Sau (AI-powered Menu Intelligence) |
|---|---|
| Thêm/bỏ món theo trend bên ngoài | **AI Menu Analytics**: Phân tích doanh số từng món theo tuần/tháng/mùa → "Matcha Latte tăng 35% trong 4 tuần → đề xuất tạo thêm biến thể Matcha" |
| Giữ 10-15 món bán chậm trên menu | **AI gợi ý loại bỏ/điều chỉnh**: "Smoothie Dâu: chỉ bán 2 ly/ngày, rating feedback 2.8/5 → đề xuất loại bỏ hoặc thay đổi công thức" |
| Giá bán theo linh cảm | **AI Price Sensitivity**: Phân tích sự thay đổi doanh số khi điều chỉnh giá → "Tăng giá Latte từ 45K→50K: dự báo giảm 8% đơn nhưng tăng 12% doanh thu" |
| Khuyến mãi sai thời điểm | **AI Smart Promotion**: Kết hợp dữ liệu giờ vắng + tồn kho + thời tiết → "14h-16h thứ 3-5 vắng nhất → push combo giảm 20% qua Zalo cho khách lân cận" |

**AI cụ thể:**
- **Input:** Doanh số từng món theo giờ/ngày/tuần + QR feedback rating + tồn kho + thời tiết + ngày lễ
- **Model:** Time-series decomposition + Clustering (nhóm món) + Elasticity regression (price sensitivity)
- **Output:** Báo cáo Menu Intelligence hàng tuần — top món tăng trưởng, món cần loại, thời điểm khuyến mãi tối ưu, gợi ý giá

**Kết quả:** Loại bỏ 10-15 món kém → giảm phức tạp kho & menu. Tăng 10-15% doanh thu nhờ push đúng món, đúng giờ, đúng giá.

---
---

# 📝 PHẦN III: AI VÀ IoT ỨNG DỤNG NHƯ THẾ NÀO — CHI TIẾT KỸ THUẬT

## 11. 🤖 Tổng Hợp 7 Tính Năng AI

| # | Tên AI Feature | Bài Toán Giải Quyết | Model / Thuật Toán | Dữ Liệu Đầu Vào | Kết Quả Đầu Ra |
|---|---|---|---|---|---|
| AI-1 | **Thống Kê doanh thu bằng AI** | Thông kê so sánh doanh thu các tuần các tháng, quán, quý | Prophet / LSTM time-series | Doanh thu lịch sửn | "Tháng này so với tháng trước bao nhiêu " |
| AI-2 | **Gợi ý combo bán chạy** | Tăng doanh thu trung bình/đơn | Association Rules (Apriori) + Collaborative Filtering | Lịch sử đơn hàng (món nào hay đi kèm nhau) | "Combo Latte + Croissant: 68% khách mua Latte cũng mua Croissant" |
| AI-3 | **Churn Prediction khách hàng** | Giữ chân khách sắp bỏ đi | Random Forest / XGBoost classification | Tần suất mua, giá trị mua, khoảng cách giữa lần mua | "Khách Nguyễn A: 78% churn risk → gửi voucher 30% off" |
| AI-4 | **Chatbot NLP tiếng Việt** |cho nhân viên hỏi nguyên liệu , cách vận hành quán , Cho admin AL-1  | RAG (LLM + Vector DB) + PhoBERT intent | Tin nhắn khách: "trình bày cho Admin và staff" | Parse: {item: "trà sữa", qty: 2, time: "15:00"} → tạo order |
| AI-5 | **Menu Intelligence & Smart Promotion** | Tối ưu menu + khuyến mãi đúng thời điểm | Time-series decomposition + Clustering + Elasticity regression | Doanh số từng món/giờ + QR feedback + tồn kho + thời tiết | "Matcha +35% 4 tuần, Smoothie Dâu 2 ly/ngày → loại. Giờ vắng 14-16h → push combo" |

---

### Luồng IoT Data:

```
[DS18B20] Nhiệt độ tủ lạnh ────┐
[Smart Scale] Cân nguyên liệu ──┼──► [ESP32 Hub] ──WiFi/MQTT──► [Cloud]
[QR/NFC] Chấm công & Loyalty ──┘                                 │
                                                                    ├── InfluxDB
                                                                    ├── Alert (SMS/Zalo)
                                                                    └── Web Dashboard
```

**Lưu ý quan trọng:** IoT là **phần mở rộng tùy chọn** — hệ thống F&B OS hoạt động hoàn chỉnh **không cần IoT** (chỉ cần POS + Web + App). IoT bổ sung thêm khả năng giám sát kho lạnh và hỗ trợ kiểm kê cho các chuỗi lớn muốn "nâng cấp".

---
---

# 📝 PHẦN IV: DỰ ÁN GIẢI QUYẾT ĐƯỢC GÌ CHO THỊ TRƯỜNG?

## 13. 🏪 Đối Với Chủ Quán Cà Phê / Chuỗi F&B

| Giá Trị | Đo Lường Được |
|---|---|
| Kiểm soát thất thoát nguyên liệu | Từ 5-15% → dưới 2% (tiết kiệm 10-30 triệu/tháng) |
| Giảm chi phí nhân sự lãng phí | Xếp ca tối ưu → tiết kiệm 30% nhân công giờ vắng |
| Giữ chân khách hàng | AI churn prediction → giữ thêm 15-25% khách sắp bỏ đi |
| Tăng doanh thu/đơn | Gợi ý combo → tăng giá trị trung bình mỗi đơn 15-20% |
| Biết lợi nhuận thật mỗi ngày | Dashboard real-time → quyết định nhanh, cắt lỗ kịp |
| Không mất hàng vì tủ lạnh hỏng | IoT alert → phát hiện trong 5 phút thay vì 8 tiếng |

## 14. 📊 Thị Trường Mục Tiêu Tại Việt Nam (2025)

| Phân Khúc | Quy Mô | Nhu Cầu |
|---|---|---|
| Chuỗi cà phê (Highlands, TCH, Phúc Long...) | ~3,000 cửa hàng | Cần POS + AI analytics + quản lý chuỗi |
| Quán cà phê độc lập | ~300,000 quán | Cần POS đơn giản + kho + lương |
| Chuỗi trà sữa (ToCoToCo, Tiger Sugar...) | ~2,000 cửa hàng | Tương tự cà phê + kiểm soát nguyên liệu |
| Nhà hàng (lẩu, nướng, cơm) | ~150,000 nhà hàng | Cần KDS + quản lý bàn + kho + HĐĐT |
| Cloud kitchen / Delivery only | Tăng trưởng 30%/năm | Cần quản lý đơn online + kho + tối ưu menu |

**Tổng thị trường tiềm năng:** ~455,000 cơ sở F&B tại VN → thị trường SaaS F&B ước tính **500-800 triệu USD**.

---
---

# 📝 PHẦN V: ĐIỂM ĐỘC ĐÁO — TẠI SAO KHÁC BIỆT?

## 15. So Sánh Với Đối Thủ Hiện Tại Tại VN

| Tiêu Chí | iPOS / CukCuk / KiotViet | F&B Operating System (Đề Tài) |
|---|---|---|
| POS cơ bản | ✅ Có | ✅ Có |
| Quản lý kho | ✅ Có (cơ bản) | ✅ Có + **BOM tự động trừ** + AI đề xuất nhập |
| Dự báo doanh thu | ❌ Chỉ có thống kê quá khứ | ✅ **AI forecast 7-30 ngày** (Prophet/LSTM) |
| Gợi ý combo tăng doanh thu | ❌ Không | ✅ **AI Association Rules** — combo bán chạy |
| Dự đoán khách sắp bỏ đi | ❌ Không | ✅ **AI Churn Prediction** — giữ chân tự động |
| Chatbot đặt bàn/đặt món | ❌ Không | ✅ **NLP tiếng Việt** — qua Zalo/Facebook |
| AI xếp ca nhân viên | ❌ Không | ✅ **Demand forecast → auto-scheduling** |
| IoT giám sát thiết bị | ❌ Không | ✅ **ESP32 + sensor** — tủ lạnh, máy pha, điện |
| Chấm công GPS + selfie | ❌ Cơ bản | ✅ **QR + GPS lock + selfie** — chống gian lận |
| Hóa đơn điện tử | ✅ Có (1 số) | ✅ Có — tích hợp VNPT/Viettel API |

## 16. 5 Điểm Độc Đáo Chưa Đồ Án Nào Tại VN Làm

### 1. 🤖 AI Chatbot Đặt Bàn/Đặt Món Tiếng Việt Qua Zalo
- Hiểu tiếng lóng, viết tắt, emoji: **"Cho e 2 ly matcha đá lúc 3h nha 🧋"**
- Tự động parse: {item: "matcha đá", qty: 2, time: "15:00"} → tạo order trong POS
- Hỏi đáp menu: **"Có món gì cho người ăn chay không?"** → AI trả lời dựa trên menu thực
- Chưa quán cà phê nào tại VN có chatbot đặt món **thông minh thực sự** (chỉ có chatbot FAQ cơ bản)

### 2. 📊 AI Dự Báo Doanh Thu + Nhu Cầu Nguyên Liệu
- Không chỉ "nhìn lại quá khứ" như các POS hiện tại → **nhìn trước 7-30 ngày**
- Kết hợp dữ liệu thời tiết (mưa → doanh thu giảm 30%), sự kiện, ngày lễ
- Tự động chuyển thành **đề xuất nhập hàng** → chủ quán không bao giờ hết nguyên liệu

### 3. 🧊 IoT Giám Sát Tủ Lạnh + Máy Pha Espresso
- ESP32 + DS18B20 giám sát nhiệt độ tủ lạnh → **alert khi hỏng ban đêm**
- Smart plug đo điện năng máy pha → phát hiện **máy hoạt động bất thường**
- Vibration sensor trên bơm máy espresso → dự báo **bơm sắp hỏng trước 3-7 ngày**
- Đây là tính năng **chưa POS nào tại VN có** — tạo lợi thế cạnh tranh rõ ràng

### 4. 🧑‍🤝‍🧑 AI Churn Prediction + Auto-Voucher
- Phát hiện khách trung thành "biến mất" → tự động gửi voucher qua Zalo OA
- Phân nhóm khách: VIP / Regular / New / Churned → chiến lược khuyến mãi riêng
- **Tăng retention rate 15-25%** — giảm chi phí marketing 30-40%

### 5. 📋 Smart Scheduling — AI Tự Xếp Ca
- AI dự báo lượng khách → tính số nhân viên cần → đề xuất bảng ca tối ưu
- Tích hợp: availability nhân viên + quy tắc công bằng + ngày nghỉ phép
- Quản lý **tiết kiệm 3-5 tiếng/tuần** — dành thời gian cho quản lý chất lượng

---
---

# 📝 PHẦN VI: TỔNG HỢP KIẾN TRÚC & PHÂN CÔNG

## 17. 🏗️ Kiến Trúc Hệ Thống

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     F&B OPERATING SYSTEM                                │
│                                                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │ Web App  │ │ Mobile   │ │ KDS      │ │ Zalo OA  │ │ Facebook │     │
│  │ (Admin/  │ │ App      │ │ (Kitchen │ │ Chatbot  │ │ Chatbot  │     │
│  │ Manager) │ │ (Staff)  │ │ Display) │ │          │ │          │     │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘     │
│       └─────────────┴────────────┴─────────────┴─────────────┘           │
│                                  │                                       │
│                           ┌──────▼──────┐                               │
│                           │  API Gateway │ (Auth, Rate Limit)           │
│                           └──────┬──────┘                               │
│       ┌──────────────────────────┼──────────────────────────┐           │
│       │                          │                          │           │
│  ┌────▼────┐  ┌─────────▼────────┐  ┌──────▼──────┐                   │
│  │ Order   │  │ Inventory        │  │ Customer    │                    │
│  │ Service │  │ Service          │  │ Service     │                    │
│  │ POS,    │  │ (BOM, Forecast)  │  │ (CRM,      │                    │
│  │ Payment │  │                  │  │  Loyalty)   │                    │
│  └────┬────┘  └────────┬────────┘  └──────┬──────┘                    │
│       │                │                   │                            │
│  ┌────▼────┐  ┌────────▼────────┐  ┌──────▼──────┐                    │
│  │ HRM     │  │ Analytics       │  │ Chatbot     │                    │
│  │ Service │  │ Service         │  │ Service     │                    │
│  │ (Staff, │  │ (Dashboard,     │  │ (NLP,       │                    │
│  │  Shift) │  │  AI Forecast)   │  │  RAG)       │                    │
│  └────┬────┘  └────────┬────────┘  └──────┬──────┘                    │
│       └────────────────┼───────────────────┘                            │
│                        │                                                │
│              ┌─────────▼─────────┐                                     │
│              │    PostgreSQL     │                                      │
│              │    + pgvector     │  (RAG cho Chatbot)                   │
│              │    + Redis Cache  │  (Real-time data)                    │
│              │    + InfluxDB     │  (IoT time-series)                   │
│              └───────────────────┘                                      │
│                                                                         │
│  External:                                                              │
│  ├── VietQR / MoMo / ZaloPay (Payment)                                │
│  ├── Zalo OA API (Chatbot + Notification)                              │
│  ├── VNPT / Viettel E-Invoice API (HĐĐT)                               │
│  ├── OpenWeatherMap API (Dự báo thời tiết cho AI)                      │
│  └── Gemini / GPT API (Chatbot NLP)                                    │
│                                                                         │
│  IoT Layer (Tùy chọn):                                                 │
│  ├── ESP32 + DS18B20 (Tủ lạnh)                                        │
│  ├── Smart Plug Sonoff S31 (Điện năng)                                 │
│  └── ESP32 + MPU-6050 (Rung động máy pha)                              │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 18. 👥 5 Actors (Vai Trò)

| Actor | Mô Tả | Chức Năng Chính |
|---|---|---|
| 🔴 **Admin (Chủ chuỗi)** | Quản lý toàn bộ hệ thống, xem tổng | Dashboard tổng, quản lý chi nhánh, phân quyền, tài chính, HĐĐT |
| 🟠 **Manager (Quản lý chi nhánh)** | Quản lý 1 cửa hàng | POS, kho, ca làm, doanh thu chi nhánh, phê duyệt nhập hàng |
| 🟢 **Staff (Nhân viên)** | Thu ngân, phục vụ | Tạo order, thanh toán, gọi món, chấm công, xin đổi ca |
| 🔵 **Kitchen (Bếp/Bar)** | Pha chế, nấu bếp | KDS hiển thị order, cập nhật "đang làm"/"xong", xem công thức pha chế |
| 🟣 **Customer (Khách hàng)** | Đặt bàn, mua hàng | App/Zalo: đặt bàn, xem menu, tích điểm, feedback, chatbot |

---

## 19. 📦 8 Module Hệ Thống

| # | Module | Chức Năng Chính |
|---|---|---|
| M1 | 🛒 **POS — Bán Hàng** | Order, chia/gộp bill, thanh toán VietQR/MoMo/tiền mặt, KDS, quản lý bàn |
| M2 | 📦 **Kho — Nguyên Liệu** | Quản lý xuất kho quầy (Kg/Hộp/Chai), kiểm kê kho & quầy, alert hết hàng, AI đề xuất nhập hàng |
| M3 | 📋 **Menu — Thực Đơn** | CRUD món, giá theo chi nhánh, combo, AI gợi ý combo, ảnh + mô tả |
| M4 | 👥 **CRM & Loyalty** | Hồ sơ khách, tích điểm, phân nhóm, QR Customer Feedback (đánh giá món/ca), AI churn prediction, auto-voucher |
| M5 | 📊 **Analytics & AI** | Dashboard real-time, forecast doanh thu, so sánh chi nhánh, heatmap giờ |
| M6 | 🤖 **Chatbot AI** | Đặt bàn/đặt món qua Zalo/FB, hỏi đáp menu, xử lý feedback, NLP tiếng Việt |
| M7 | 👨‍💼 **HRM — Nhân Sự** | Chấm công QR/GPS, xếp ca AI, đổi ca app, tính lương tự động |
| M8 | 🧾 **Tài Chính & HĐĐT** | Thu chi, lợi nhuận, ranking chi nhánh, hóa đơn điện tử, báo cáo thuế |

---

## 20. 🛠️ Tech Stack

| Tầng | Công Nghệ |
|---|---|
| Backend API | Python FastAPI hoặc Node.js (NestJS) |
| Frontend Web | React.js + Recharts (chart/dashboard) |
| Mobile App (Staff) | Flutter (iOS + Android) |
| Database | PostgreSQL + pgvector (RAG) |
| Cache / Real-time | Redis + WebSocket |
| IoT Time-series | InfluxDB v2 |
| AI / ML | scikit-learn, XGBoost, Prophet, PyTorch |
| Chatbot NLP | RAG (LLM + pgvector) + PhoBERT intent |
| IoT Firmware | C/C++ (ESP-IDF) cho ESP32 |
| Payment | VietQR, MoMo API, ZaloPay API |
| Alert / Notification | Zalo OA API, Firebase Push |
| E-Invoice | VNPT / Viettel HĐĐT API |
| Deploy | Docker + AWS/GCP |

---

## 21. 👨‍💻 Phân Công Team 4 Người

| Sinh Viên | Vai Trò | Phụ Trách |
|---|---|---|
| **SV 1 — Backend Lead** | API, Database, Auth, Payment | Order Service, Payment (VietQR/MoMo), E-Invoice API, WebSocket |
| **SV 2 — Frontend Lead** | Web App (Admin/Manager), KDS | Dashboard, POS UI, Menu Management, KDS Kitchen Display |
| **SV 3 — AI Engineer** | ML models, Chatbot, Analytics | AI Forecast (Prophet), Chatbot NLP (RAG), Churn Prediction, Combo AI |
| **SV 4 — Full-stack + IoT** | Mobile App, Inventory, HRM, IoT | Flutter App, Quản lý kho & Xuất kho quầy, HRM + Chấm công, ESP32 sensor |

---

## 22. 📊 BẢNG TỔNG HỢP: VẤN ĐỀ → GIẢI PHÁP → CÔNG NGHỆ → KẾT QUẢ

| Vấn Đề | Giải Pháp | AI / IoT | Kết Quả |
|---|---|---|---|
| Chấm công gian lận | QR + GPS lock + selfie | Face recognition (tùy chọn) | Gian lận → 0%, tiết kiệm 2-3 ngày tính lương |
| Xếp ca cảm tính | AI demand forecast + auto-scheduling | XGBoost time-series + Optimization | Tiết kiệm 30% nhân công lãng phí |
| Thất thoát nguyên liệu 5-15% | Quản lý xuất kho quầy + AI đề xuất nhập | XGBoost demand forecast | Thất thoát < 2%, không hết hàng giữa ca |
| Không biết lợi nhuận thật | Dashboard tích hợp real-time | Analytics engine | Biết lãi/lỗ từng quán mỗi ngày |
| Chất lượng không đồng nhất & Thiếu Data | Công thức chuẩn + QR Code Feedback | Feedback Analytics | Đồng nhất 95%+, xử lý phàn nàn 100% tại chỗ, tối ưu menu theo data |
| Khách bỏ đi không biết | CRM + AI Churn Prediction | Random Forest / XGBoost | Giữ thêm 15-25% khách, tăng 20% doanh thu |
| Báo cáo cuối ngày thủ công 30-60 phút | Auto EOD Report + Dashboard chuỗi real-time | Auto aggregation + Push notification | Tiết kiệm 30-60 phút/tối, phát hiện chênh lệch ngay |
| Thêm/bỏ món theo cảm tính, KM sai thời điểm | AI Menu Intelligence + Smart Promotion | Time-series + Clustering + Price Elasticity | Tăng 10-15% doanh thu, loại món kém, push đúng giờ vắng |

---

> **Tóm lại:** Nền tảng F&B Operating System giải quyết **8 bất cập thực tế** mà hầu hết quán cà phê tại VN đang gặp — từ chấm công, xếp ca, kiểm kê, tài chính, chất lượng, khách hàng, báo cáo cuối ngày đến chiến lược menu. Tích hợp **7 AI features** (forecast doanh thu, forecast nguyên liệu, combo AI, churn prediction, chatbot NLP, smart scheduling, menu intelligence) + **IoT tùy chọn** (giám sát tủ lạnh, cân nguyên liệu). Đối thủ hiện tại (iPOS, CukCuk) **chưa có AI thực sự** → đây là lợi thế cạnh tranh rõ ràng.
