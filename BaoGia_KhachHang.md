# BẢNG BÁO GIÁ TRIỂN KHAI HỆ THỐNG SMART F&B OS

> **Khách hàng:** Chuỗi Quán Cà phê / Đồ uống — 3 chi nhánh  
> **Giải pháp:** Hệ thống đặt món QR thông minh thay thế cây POS truyền thống  
> **Ngày lập:** 11/08/2026  
> **Hiệu lực báo giá:** 30 ngày kể từ ngày lập

---

## A. CHI PHÍ PHÁT TRIỂN PHẦN MỀM (Thanh toán 1 lần)

Hệ thống gồm 5 module phần mềm, 5 AI module, 71 tính năng, phát triển trong 4-5 tháng.

### Bảng chi phí phát triển theo module

| STT | Module phần mềm | Mô tả | Thời gian | Chi phí |
|---|---|---|---|---|
| 1 | QR Order Web (PWA) cho Khách hàng | Menu trực quan, đặt món, thanh toán VietQR, AI Chatbot gợi ý, CRM, Loyalty, Feedback | 5 tuần | 30.000.000 |
| 2 | KDS & Màn hình Khách (POS 2 màn hình) | Nhận đơn real-time, công thức pha chế, hoàn thành đơn, báo hết món, chế độ Offline, hiển thị đơn + QR cho khách | 4 tuần | 25.000.000 |
| 3 | App Quản lý Chi nhánh (Manager) | Mở/kết ca, nhập xuất kho, kiểm kê, báo cáo, chấm công, AI thống kê | 4 tuần | 22.000.000 |
| 4 | Web Dashboard Admin (Chủ chuỗi) | Dashboard doanh thu toàn chuỗi, P&L, quản lý menu/giá, RBAC phân quyền, Audit Log, Export | 5 tuần | 28.000.000 |
| 5 | Backend API & Hạ tầng | REST API, WebSocket real-time, Auth/RBAC, VietQR, Database, Redis, Docker, Deploy, Backup, Offline Sync | 6 tuần | 35.000.000 |
| 6 | AI Engine (5 module) | AI-1: Thống kê doanh thu, AI-2: Gợi ý combo, AI-3: Churn Prediction, AI-4: Menu Intelligence, AI-5: Chatbot RAG | 4 tuần | 25.000.000 |
| 7 | Kiểm thử & Triển khai | Testing toàn bộ hệ thống, sửa lỗi, tối ưu hiệu năng, deploy production, hướng dẫn sử dụng | 2 tuần | 10.000.000 |
| | | | | |
| | **TỔNG PHÁT TRIỂN PHẦN MỀM** | **71 tính năng, 5 AI module** | **~4-5 tháng** | **175.000.000** |

### Lịch trình phát triển & thanh toán theo giai đoạn

| Giai đoạn | Nội dung bàn giao | Thời gian | Thanh toán |
|---|---|---|---|
| GĐ 1: Nền tảng (Tháng 1-2) | Backend API + Database + QR Order cơ bản + KDS cơ bản, chạy thử được luồng đặt-pha-xong | 8 tuần | 70.000.000 (40%) |
| GĐ 2: Hoàn thiện (Tháng 3-4) | Manager App + Admin Dashboard + thanh toán VietQR + CRM + Loyalty + Offline Mode | 8 tuần | 60.000.000 (34%) |
| GĐ 3: AI & Golive (Tháng 4-5) | 5 AI module + Chatbot + Testing + Deploy production + Đào tạo + Nghiệm thu | 4 tuần | 45.000.000 (26%) |

---

## B. CHI PHÍ THIẾT BỊ PHẦN CỨNG (Thanh toán 1 lần)

### Thiết bị chính: Máy POS cảm ứng 2 màn hình

Mỗi chi nhánh trang bị 1 máy POS cảm ứng chuyên dụng đặt tại quầy:
- Mặt trong (Nhân viên): Màn hình cảm ứng 15.6 inch — thao tác nhận đơn, hoàn thành pha chế, báo hết món.
- Mặt ngoài (Khách hàng): Màn hình phụ 10 inch — hiển thị chi tiết đơn hàng, giá tiền, tổng cộng và mã VietQR thanh toán.

| STT | Hạng mục | Đơn giá | SL | Thành tiền | Ghi chú |
|---|---|---|---|---|---|
| 1 | Máy POS 2 màn hình cảm ứng (Sunmi T2s / D2s) | 9.000.000 | 3 | 27.000.000 | 15.6" NV cảm ứng + 10" Khách xem đơn & QR |
| 2 | Máy in hóa đơn nhiệt 80mm | 2.000.000 | 3 | 6.000.000 | Dùng lại máy in cũ nếu có: 0 đ |
| 3 | Bảng QR Code Acrylic để bàn | 30.000 | 60 | 1.800.000 | 20 bàn mỗi chi nhánh |
| 4 | Bảng QR Takeaway tại quầy | 30.000 | 3 | 90.000 | Khách mang đi quét QR đặt món tại quầy |
| 5 | Router WiFi + 4G Backup | 1.200.000 | 3 | 3.600.000 | Tự chuyển sang 4G khi WiFi chết |
| 6 | Lắp đặt, cấu hình & chạy thử | 1.000.000 | 3 | 3.000.000 | Trọn gói 3 chi nhánh |
| | | | | | |
| | **TỔNG THIẾT BỊ** | | | **41.490.000** | |
| | *Nếu dùng lại máy in cũ* | | | *35.490.000* | *Tiết kiệm 6 triệu* |

---

## C. CHI PHÍ VẬN HÀNH HÀNG THÁNG (Cho cả 3 chi nhánh)

| STT | Hạng mục | Chi phí/tháng | Ghi chú |
|---|---|---|---|
| 1 | Máy chủ Cloud (Server) | 800.000 | VPS 4 vCPU, 8GB RAM — chạy toàn bộ hệ thống |
| 2 | Tên miền (.com) | 30.000 | 360.000/năm, chia ra 30.000/tháng |
| 3 | AI Engine (Chatbot + Thống kê) | 400.000 | Google Gemini Flash API |
| 4 | SIM 4G Data backup (3 quán) | 450.000 | 3 quán x 150.000/tháng |
| 5 | Giấy in nhiệt (tiêu hao) | 180.000 | 3 quán x 3 cuộn/tháng x 20.000/cuộn |
| | | | |
| | **TỔNG HÀNG THÁNG** | **1.860.000** | **~620.000/chi nhánh** |

---

## D. CHI PHÍ BẢO TRÌ PHẦN MỀM

### Gói bảo trì cơ bản (Đề xuất)

| Hạng mục | Nội dung | Chi phí/tháng |
|---|---|---|
| Sửa lỗi phần mềm (Bug fix) | Xử lý lỗi phát sinh trong quá trình vận hành, thời gian phản hồi trong 24 giờ làm việc | Bao gồm |
| Cập nhật bảo mật | Vá lỗ hổng bảo mật, cập nhật thư viện, chống tấn công | Bao gồm |
| Giám sát server | Theo dõi uptime, cảnh báo khi server quá tải hoặc sập | Bao gồm |
| Backup & phục hồi | Sao lưu hàng ngày, hỗ trợ phục hồi khi có sự cố | Bao gồm |
| Hỗ trợ kỹ thuật | Hotline/Zalo hỗ trợ Quản lý & NV trong giờ hành chính (T2-T7) | Bao gồm |
| | | |
| | **TỔNG BẢO TRÌ CƠ BẢN** | **3.000.000/tháng** |

### Gói bảo trì nâng cao (Tùy chọn)

| Hạng mục | Nội dung | Chi phí/tháng |
|---|---|---|
| Toàn bộ gói Cơ bản | Như trên | Bao gồm |
| Phát triển tính năng mới | Tối đa 2 tính năng nhỏ hoặc 1 tính năng vừa mỗi tháng | Bao gồm |
| Tối ưu hiệu năng | Cải thiện tốc độ tải, tối ưu database khi dữ liệu lớn | Bao gồm |
| Nâng cấp AI model | Cập nhật model AI mới, cải thiện độ chính xác chatbot | Bao gồm |
| Hỗ trợ 24/7 | Hỗ trợ ngoài giờ hành chính, xử lý sự cố khẩn cấp | Bao gồm |
| | | |
| | **TỔNG BẢO TRÌ NÂNG CAO** | **6.000.000/tháng** |

### Chính sách bảo hành phần mềm

- Bảo hành miễn phí 3 tháng sau khi nghiệm thu (sửa lỗi + hỗ trợ kỹ thuật, không tốn phí).
- Sau 3 tháng bảo hành, khách hàng chọn 1 trong 2 gói bảo trì hoặc tự vận hành.
- Nếu không ký bảo trì: Hỗ trợ sửa lỗi theo vụ việc, tính phí 500.000 - 2.000.000/lần tùy mức độ.

---

## E. DỊCH VỤ MIỄN PHÍ ĐI KÈM (0 đ)

| STT | Dịch vụ | Nhà cung cấp | Mục đích |
|---|---|---|---|
| 1 | Thanh toán chuyển khoản VietQR | NAPAS | Khách quét mã thanh toán, miễn phí 100% |
| 2 | Bảo mật SSL & tăng tốc CDN | Cloudflare | Chứng chỉ bảo mật & tăng tốc tải trang |
| 3 | Thông báo đẩy (Push Notification) | Firebase (Google) | Báo trạng thái đơn, gọi nhân viên |
| 4 | Gửi báo cáo Email cuối ca | SendGrid | Tự động gửi báo cáo kết ca cho Quản lý |
| 5 | Gửi voucher tri ân qua Zalo | Zalo OA | Voucher sinh nhật, khách lâu chưa ghé |
| 6 | Lưu trữ ảnh menu & feedback | Self-hosted (trên Server) | Ảnh món, ảnh feedback khách chụp |
| 7 | Sao lưu dữ liệu tự động | Script tự động hàng ngày | Backup database lên Cloud miễn phí |

---

## F. CHI PHÍ PHÁT SINH CÓ THỂ XẢY RA

| STT | Hạng mục | Khi nào phát sinh | Chi phí ước tính |
|---|---|---|---|
| 1 | Thay bảng QR Acrylic hư/mất | Khách làm hư hoặc mất | 30.000/bảng |
| 2 | Nâng cấp Zalo OA trả phí | Gửi voucher > 500 tin/tháng | 200.000 - 500.000/tháng |
| 3 | Nâng cấp cấu hình Server | Mở rộng > 5 chi nhánh | +400.000 - 800.000/tháng |
| 4 | Sửa chữa/thay thế máy POS | Sau 3-5 năm hoặc hư hỏng | 5.000.000 - 9.000.000/máy |
| 5 | Phát triển tính năng lớn mới | Ngoài phạm vi 71 tính năng ban đầu | Báo giá riêng theo yêu cầu |

---

## G. TỔNG HỢP CHI PHÍ ĐẦU TƯ

### Tổng chi phí ban đầu (Thanh toán 1 lần)

| Hạng mục | Chi phí |
|---|---|
| Phát triển phần mềm (71 tính năng + 5 AI) | 175.000.000 |
| Thiết bị phần cứng (3 chi nhánh) | 41.490.000 |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **216.490.000** |
| *Nếu dùng lại máy in cũ* | *210.490.000* |

### Chi phí vận hành hàng tháng

| Hạng mục | Chi phí/tháng |
|---|---|
| Vận hành hạ tầng (Server + AI + 4G + tiêu hao) | 1.860.000 |
| Bảo trì phần mềm (Gói cơ bản) | 3.000.000 |
| **TỔNG HÀNG THÁNG** | **4.860.000** |
| *Nếu chọn gói bảo trì nâng cao* | *7.860.000* |

### Tổng theo thời gian

| Mốc thời gian | Chi phí | Ghi chú |
|---|---|---|
| **Ban đầu** | **216.490.000** | Phần mềm + thiết bị, thanh toán theo giai đoạn |
| **Mỗi tháng** | **4.860.000** | Vận hành + Bảo trì cơ bản |
| **Năm đầu tiên** | **~274.800.000** | Ban đầu + 12 tháng vận hành (gồm 3 tháng BH miễn phí + 9 tháng bảo trì) |
| **Từ năm thứ 2** | **~58.300.000/năm** | Chỉ vận hành + bảo trì hàng tháng |

---

## H. SO SÁNH CHI PHÍ: CÂY POS CŨ vs SMART F&B OS

| Hạng mục | Cây POS cũ (tháng) | Smart F&B OS (tháng) | Tiết kiệm |
|---|---|---|---|
| Lương thu ngân (3 quán x 1 NV) | 21.000.000 | 0 | -21.000.000 |
| Phí phần mềm/bản quyền POS | 3.000.000 - 6.000.000 | 0 | -3.000.000 ~ -6.000.000 |
| Hao hụt nguyên liệu (ước tính) | 10 - 15% doanh thu | < 2% doanh thu | Giảm 8 - 13% |
| Chi phí vận hành + bảo trì | 1.000.000 - 1.500.000 | 4.860.000 | +3.360.000 |
| | | | |
| **Tổng ước tính/tháng** | **~35.000.000 - 42.000.000** | **~7.860.000** | **Tiết kiệm ~27 - 34 triệu** |

> Tiết kiệm ròng hàng tháng khoảng **27 - 34 triệu VNĐ**.  
> **Thời gian hoàn vốn toàn bộ** (phần mềm + thiết bị): Khoảng **7 - 8 tháng** vận hành.  
> Từ tháng thứ 9 trở đi, toàn bộ khoản tiết kiệm là lợi nhuận ròng.

---

## I. ĐIỀU KHOẢN THANH TOÁN

| Đợt | Nội dung | Số tiền | Thời điểm |
|---|---|---|---|
| Đợt 1 | Ký hợp đồng + Khởi động phát triển (GĐ 1) | 70.000.000 | Ngày ký hợp đồng |
| Đợt 2 | Bàn giao GĐ 1 (Backend + QR + KDS chạy thử) | 41.490.000 (thiết bị) | Sau 2 tháng |
| Đợt 3 | Bàn giao GĐ 2 (Manager + Admin + Offline) | 60.000.000 | Sau 4 tháng |
| Đợt 4 | Nghiệm thu toàn bộ + Golive (GĐ 3) | 45.000.000 | Sau 5 tháng |
| Hàng tháng | Vận hành + Bảo trì (sau 3 tháng BH miễn phí) | 4.860.000 | Từ tháng thứ 8 |

---

## J. GHI CHÚ QUAN TRỌNG

1. Báo giá trên chưa bao gồm thuế VAT (nếu có).
2. Giá thiết bị có thể thay đổi tùy thời điểm mua & nhà cung cấp.
3. Phần mềm thuộc sở hữu 100% của khách hàng sau khi thanh toán đầy đủ, bao gồm toàn bộ mã nguồn.
4. Bảo hành phần mềm miễn phí 3 tháng sau nghiệm thu. Sau đó khách hàng chọn gói bảo trì hoặc tự vận hành.
5. Hệ thống có cơ chế dự phòng mất mạng 3 lớp: Router 4G tự chuyển, chế độ Offline trên POS, và PWA cache menu.
6. Máy in hóa đơn cũ của cây POS (chuẩn ESC/POS, khổ 80mm) có thể tái sử dụng, giảm 6.000.000 trong tổng chi phí.
7. Dữ liệu hệ thống được sao lưu tự động hàng ngày, cam kết không mất data.
8. Máy POS cảm ứng Sunmi T2s/D2s bảo hành chính hãng 12 tháng, tuổi thọ 3-5 năm sử dụng liên tục.
9. Khi mất mạng hoàn toàn, quán vẫn hoạt động: NV tạo đơn trên POS, thu tiền mặt. Có mạng lại, dữ liệu tự đồng bộ.
