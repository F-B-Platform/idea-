# BẢNG BÁO GIÁ TRIỂN KHAI HỆ THỐNG SMART F&B OS

> **Khách hàng:** Chuỗi Quán Cà phê / Đồ uống — 3 chi nhánh  
> **Giải pháp:** Hệ thống đặt món QR thông minh thay thế cây POS truyền thống  
> **Ngày lập:** 11/08/2026  
> **Hiệu lực báo giá:** 30 ngày kể từ ngày lập

---

## A. CHI PHÍ PHÁT TRIỂN PHẦN MỀM (Thanh toán 1 lần)

Toàn bộ hệ thống phát triển trên nền tảng Web, không cần cài đặt app riêng. Quản lý và Admin truy cập qua trình duyệt trên điện thoại hoặc máy tính.

| STT | Module | Mô tả | Chi phí |
|---|---|---|---|
| 1 | QR Order Web (Khách hàng) | Menu, đặt món, thanh toán VietQR, Chatbot AI gợi ý, CRM, Loyalty, Feedback | 12.000.000 |
| 2 | KDS & Màn hình Khách (POS 2 màn hình) | Nhận đơn real-time, công thức pha chế, hoàn thành đơn, báo hết món, Offline Mode, hiển thị đơn + QR cho khách | 10.000.000 |
| 3 | Web Quản lý Chi nhánh (Manager) | Mở/kết ca, nhập xuất kho, kiểm kê, chấm công, báo cáo chi nhánh | 8.000.000 |
| 4 | Web Dashboard Admin (Chủ chuỗi) | Dashboard doanh thu, quản lý menu/giá, phân quyền, Audit Log | 10.000.000 |
| 5 | Backend API & Hạ tầng | API, WebSocket real-time, Database, thanh toán VietQR, Docker, Deploy, Backup, Offline Sync | 12.000.000 |
| 6 | AI Engine | Thống kê doanh thu, Gợi ý combo, Chatbot gợi ý món, Dự đoán khách rời | 8.000.000 |
| | | | |
| | **TỔNG PHÁT TRIỂN** | **Thời gian: ~3-4 tháng** | **60.000.000** |

### Thanh toán theo giai đoạn

| Giai đoạn | Bàn giao | Thanh toán |
|---|---|---|
| GĐ 1 (Tháng 1-2) | Backend + QR Order + KDS chạy thử được | 25.000.000 (42%) |
| GĐ 2 (Tháng 2-3) | Manager Web + Admin Web + VietQR + Offline Mode | 20.000.000 (33%) |
| GĐ 3 (Tháng 3-4) | AI Engine + Testing + Deploy + Đào tạo + Nghiệm thu | 15.000.000 (25%) |

---

## B. CHI PHÍ THIẾT BỊ PHẦN CỨNG (Thanh toán 1 lần)

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
| 1 | Máy chủ Cloud (Server) | 800.000 | VPS chạy toàn bộ hệ thống |
| 2 | Tên miền (.com) | 30.000 | 360.000/năm |
| 3 | AI Engine (Chatbot + Thống kê) | 400.000 | Google Gemini Flash API |
| 4 | SIM 4G Data backup (3 quán) | 450.000 | 3 quán x 150.000/tháng |
| 5 | Giấy in nhiệt (tiêu hao) | 180.000 | 3 quán x 3 cuộn/tháng x 20.000/cuộn |
| | | | |
| | **TỔNG HÀNG THÁNG** | **1.860.000** | **~620.000/chi nhánh** |

---

## D. BẢO TRÌ PHẦN MỀM

- Bảo hành miễn phí 3 tháng đầu sau nghiệm thu (sửa lỗi + hỗ trợ kỹ thuật).
- Sau bảo hành, hỗ trợ bảo trì theo gói tùy chọn:

| Gói | Chi phí/tháng | Nội dung |
|---|---|---|
| Cơ bản | 2.000.000 | Sửa lỗi, cập nhật bảo mật, giám sát server, hỗ trợ qua Zalo giờ hành chính |
| Nâng cao | 4.000.000 | Gói cơ bản + phát triển tính năng mới nhỏ, tối ưu hiệu năng, hỗ trợ ngoài giờ |
| Không ký bảo trì | Tính theo lần | Sửa lỗi/hỗ trợ: 300.000 - 1.000.000/lần tùy mức độ |

---

## E. DỊCH VỤ MIỄN PHÍ ĐI KÈM (0 đ)

| STT | Dịch vụ | Mục đích |
|---|---|---|
| 1 | Thanh toán VietQR (NAPAS) | Khách quét mã thanh toán, miễn phí 100% |
| 2 | Bảo mật SSL & CDN (Cloudflare) | Chứng chỉ bảo mật & tăng tốc tải trang |
| 3 | Thông báo đẩy (Firebase) | Báo trạng thái đơn, gọi nhân viên |
| 4 | Gửi báo cáo Email (SendGrid) | Báo cáo kết ca tự động |
| 5 | Gửi voucher qua Zalo (Zalo OA) | Voucher sinh nhật, tri ân khách |
| 6 | Lưu trữ ảnh & Backup | Ảnh menu, backup dữ liệu tự động |

---

## F. TỔNG HỢP CHI PHÍ ĐẦU TƯ

### Chi phí ban đầu

| Hạng mục | Chi phí |
|---|---|
| Phát triển phần mềm | 60.000.000 |
| Thiết bị phần cứng (3 chi nhánh) | 41.490.000 |
| **TỔNG BAN ĐẦU** | **101.490.000** |
| *Dùng lại máy in cũ* | *95.490.000* |

### Chi phí hàng tháng

| Hạng mục | Chi phí/tháng |
|---|---|
| Vận hành hạ tầng | 1.860.000 |
| Bảo trì phần mềm (gói cơ bản) | 2.000.000 |
| **TỔNG HÀNG THÁNG** | **3.860.000** |

### Tổng theo thời gian

| Mốc thời gian | Chi phí | Ghi chú |
|---|---|---|
| **Ban đầu** | **101.490.000** | Phần mềm + thiết bị |
| **Mỗi tháng** | **3.860.000** | Vận hành + bảo trì cơ bản |
| **Năm đầu tiên** | **~136.200.000** | Ban đầu + 9 tháng vận hành (3 tháng BH miễn phí) |
| **Từ năm thứ 2** | **~46.300.000/năm** | Vận hành + bảo trì |

---

## G. SO SÁNH CHI PHÍ: CÂY POS CŨ vs SMART F&B OS

| Hạng mục | Cây POS cũ (tháng) | Smart F&B OS (tháng) | Tiết kiệm |
|---|---|---|---|
| Lương thu ngân (3 quán x 1 NV) | 21.000.000 | 0 | -21.000.000 |
| Phí phần mềm/bản quyền POS | 3.000.000 - 6.000.000 | 0 | -3.000.000 ~ -6.000.000 |
| Hao hụt nguyên liệu (ước tính) | 10 - 15% doanh thu | < 2% doanh thu | Giảm 8 - 13% |
| Chi phí vận hành + bảo trì | 1.000.000 - 1.500.000 | 3.860.000 | +2.360.000 |
| | | | |
| **Tổng ước tính/tháng** | **~35.000.000 - 42.000.000** | **~6.860.000** | **Tiết kiệm ~28 - 35 triệu** |

> Tiết kiệm ròng: Khoảng **28 - 35 triệu/tháng**.  
> **Thời gian hoàn vốn toàn bộ:** Khoảng **3 - 4 tháng** vận hành.  
> Từ tháng thứ 5 trở đi, toàn bộ khoản tiết kiệm là lợi nhuận ròng.

---

## H. ĐIỀU KHOẢN THANH TOÁN

| Đợt | Nội dung | Số tiền | Thời điểm |
|---|---|---|---|
| Đợt 1 | Ký hợp đồng + Khởi động phát triển | 25.000.000 | Ngày ký |
| Đợt 2 | Bàn giao GĐ 1 + Mua thiết bị | 20.000.000 + 41.490.000 | Sau 2 tháng |
| Đợt 3 | Nghiệm thu + Golive | 15.000.000 | Sau 3-4 tháng |
| Hàng tháng | Vận hành + Bảo trì (sau 3 tháng BH miễn phí) | 3.860.000 | Từ tháng thứ 7 |

---

## I. GHI CHÚ QUAN TRỌNG

1. Báo giá chưa bao gồm thuế VAT (nếu có).
2. Phần mềm thuộc sở hữu 100% của khách hàng sau khi thanh toán đầy đủ, bao gồm toàn bộ mã nguồn.
3. Toàn bộ giao diện Quản lý và Admin là Web, truy cập trên điện thoại hoặc máy tính qua trình duyệt, không cần cài đặt app.
4. Bảo hành phần mềm miễn phí 3 tháng sau nghiệm thu.
5. Hệ thống có cơ chế dự phòng mất mạng 3 lớp: Router 4G, Offline Mode trên POS, và PWA cache menu.
6. Máy in cũ của cây POS (chuẩn ESC/POS, khổ 80mm) có thể tái sử dụng, giảm 6 triệu chi phí thiết bị.
7. Dữ liệu hệ thống được sao lưu tự động hàng ngày.
8. Khi mất mạng hoàn toàn, quán vẫn hoạt động: NV tạo đơn trên POS, thu tiền mặt, dữ liệu tự đồng bộ khi có mạng.
