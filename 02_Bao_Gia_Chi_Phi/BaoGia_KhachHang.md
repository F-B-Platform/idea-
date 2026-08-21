# BẢNG BÁO GIÁ TRIỂN KHAI HỆ THỐNG SMART F&B OS

> **Khách hàng:** Chuỗi Quán Cà phê / Đồ uống — 3 chi nhánh  
> **Giải pháp:** Hệ thống đặt món QR thông minh thay thế cây POS truyền thống  
> **Ngày lập:** 11/08/2026  
> **Hiệu lực báo giá:** 30 ngày kể từ ngày lập

---

## A. CHI PHÍ PHÁT TRIỂN PHẦN MỀM (Thanh toán 1 lần)

Toàn bộ hệ thống phát triển trên nền tảng Web, truy cập qua trình duyệt, không cần cài app.

| Hạng mục | Nội dung |
|---|---|
| Giao diện Khách hàng | QR Order Web: menu, đặt món, thanh toán VietQR, Chatbot AI gợi ý, tích điểm, feedback |
| Giao diện Nhân viên | KDS cảm ứng: nhận đơn real-time, công thức pha, hoàn thành đơn, báo hết món, Offline Mode |
| Màn hình Khách tại quầy | Hiển thị đơn hàng, giá, tổng tiền, mã VietQR cho khách xem khi thanh toán tại quầy |
| Giao diện Quản lý | Web quản lý chi nhánh: mở/kết ca, kho, kiểm kê, chấm công, báo cáo |
| Giao diện Admin | Web dashboard chủ chuỗi: doanh thu, quản lý menu/giá, phân quyền |
| Backend & Hạ tầng | API, WebSocket real-time, Database, Docker, Deploy, Backup, Offline Sync |
| AI Engine | Chatbot gợi ý món, thống kê doanh thu, gợi ý combo, dự đoán khách rời |
| | |
| **Thời gian phát triển** | **3 - 4 tháng** |
| **Chi phí trọn gói** | **15.000.000** |

### Thanh toán theo giai đoạn

| Giai đoạn | Bàn giao | Thanh toán |
|---|---|---|
| GĐ 1 (Tháng 1-2) | Backend + QR Order + KDS chạy thử được | 7.000.000 |
| GĐ 2 (Tháng 2-3) | Quản lý + Admin + VietQR + Offline Mode | 5.000.000 |
| GĐ 3 (Tháng 3-4) | AI + Testing + Deploy + Đào tạo + Nghiệm thu | 3.000.000 |

---

## B. CHI PHÍ THIẾT BỊ PHẦN CỨNG (Thanh toán 1 lần)

| STT | Hạng mục | Đơn giá | SL | Thành tiền | Ghi chú |
|---|---|---|---|---|---|
| 1 | Máy POS 2 màn hình cảm ứng (Sunmi T2s / D2s) | 9.000.000 | 3 | 27.000.000 | 15.6" NV cảm ứng + 10" Khách xem đơn & QR |
| 2 | Máy in hóa đơn nhiệt 80mm | 2.000.000 | 3 | 6.000.000 | Dùng lại máy in cũ nếu có: 0 đ |
| 3 | Bảng QR Code Acrylic để bàn | 30.000 | 60 | 1.800.000 | 20 bàn mỗi chi nhánh |
| 4 | Bảng QR Takeaway tại quầy | 30.000 | 3 | 90.000 | Khách mang đi quét QR đặt món |
| 5 | Lắp đặt, cấu hình & chạy thử | 1.000.000 | 3 | 3.000.000 | Trọn gói 3 chi nhánh |
| | | | | | |
| | **TỔNG THIẾT BỊ** | | | **37.890.000** | |
| | *Dùng lại máy POS cũ* | | | *10.890.000* | *Tiết kiệm 27 triệu* |
| | *Dùng lại cả máy in cũ* | | | *4.890.000* | *Tiết kiệm thêm 6 triệu* |

### Thiết bị tùy chọn (Thương lượng — có thể cắt giảm)

| STT | Hạng mục | Đơn giá | SL | Thành tiền | Ghi chú |
|---|---|---|---|---|---|
| 1 | Router WiFi + 4G Backup | 1.200.000 | 3 | 3.600.000 | Dự phòng mất WiFi. Nếu WiFi quán ổn định, có thể bỏ |
| | SIM 4G Data hàng tháng | 150.000 | 3 | 450.000/tháng | Chỉ phát sinh nếu lắp Router 4G |

---

## C. CHI PHÍ VẬN HÀNH HÀNG THÁNG (Cho cả 3 chi nhánh)

| STT | Hạng mục | Chi phí/tháng | Ghi chú |
|---|---|---|---|
| 1 | Máy chủ Cloud (Server) | 800.000 | VPS chạy toàn bộ hệ thống |
| 2 | Tên miền (.com) | 30.000 | 360.000/năm |
| 3 | AI Engine (Chatbot + Thống kê) | 400.000 | Google Gemini Flash API |
| 4 | Giấy in nhiệt (tiêu hao) | 180.000 | 3 quán x 3 cuộn/tháng x 20.000/cuộn |
| | | | |
| | **TỔNG HÀNG THÁNG** | **1.410.000** | **~470.000/chi nhánh** |
| | *Nếu có Router 4G (tùy chọn)* | *+450.000* | *Thêm SIM 4G 3 quán* |

---

## D. BẢO TRÌ PHẦN MỀM

- Bảo hành miễn phí 3 tháng đầu sau nghiệm thu (sửa lỗi + hỗ trợ kỹ thuật).
- Sau bảo hành, hỗ trợ bảo trì theo gói tùy chọn:

| Gói | Chi phí/tháng | Nội dung |
|---|---|---|
| Cơ bản | 1.000.000 | Sửa lỗi, cập nhật bảo mật, giám sát server, hỗ trợ qua Zalo giờ hành chính |
| Nâng cao | Thương lượng | Gói cơ bản + phát triển tính năng mới, tối ưu hiệu năng, hỗ trợ ngoài giờ |
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

## F. CHI PHÍ PHÁT SINH CÓ THỂ XẢY RA

| STT | Hạng mục | Khi nào phát sinh | Chi phí ước tính |
|---|---|---|---|
| 1 | Thay bảng QR Acrylic hư/mất | Khách làm hư hoặc mất | 30.000/bảng |
| 2 | Nâng cấp Zalo OA trả phí | Gửi voucher > 500 tin/tháng | 200.000 - 500.000/tháng |
| 3 | Nâng cấp cấu hình Server | Mở rộng > 5 chi nhánh | +400.000 - 800.000/tháng |
| 4 | Sửa chữa/thay thế máy POS | Sau 3-5 năm hoặc hư hỏng | 5.000.000 - 9.000.000/máy |
| 5 | Phát triển tính năng lớn mới | Yêu cầu ngoài phạm vi ban đầu | Báo giá riêng |
| 6 | Đào tạo nhân viên mới | Tuyển NV mới cần hướng dẫn | Miễn phí (đào tạo nội bộ) |

---

## G. TỔNG HỢP CHI PHÍ ĐẦU TƯ

### Phương án 1: Triển khai thí điểm 1 chi nhánh (Khuyến nghị)

| Hạng mục | Mua mới | Dùng lại POS cũ |
|---|---|---|
| Phát triển phần mềm | 15.000.000 | 15.000.000 |
| Thiết bị 1 chi nhánh | 12.630.000 | 1.630.000 |
| **TỔNG BAN ĐẦU** | **27.630.000** | **16.630.000** |

| Hạng mục | Chi phí/tháng |
|---|---|
| Vận hành (Server + Domain + AI + Giấy in) | 1.270.000 |
| Bảo trì phần mềm (gói cơ bản) | 1.000.000 |
| **TỔNG HÀNG THÁNG** | **2.270.000** |

Chi phí mở rộng thêm mỗi chi nhánh sau thí điểm:

| Hạng mục | Mua mới | Dùng lại POS cũ |
|---|---|---|
| Thiết bị (POS + Máy in + QR + Lắp đặt) | 12.630.000 | 1.630.000 |
| Vận hành thêm hàng tháng (Giấy in) | 60.000 | 60.000 |
| Phần mềm | 0 (dùng chung) | 0 (dùng chung) |

---

### Phương án 2: Triển khai đồng loạt 3 chi nhánh

| Hạng mục | Mua mới | Dùng lại POS cũ |
|---|---|---|
| Phát triển phần mềm | 15.000.000 | 15.000.000 |
| Thiết bị 3 chi nhánh | 37.890.000 | 4.890.000 |
| **TỔNG BAN ĐẦU** | **52.890.000** | **19.890.000** |

| Hạng mục | Chi phí/tháng |
|---|---|
| Vận hành hạ tầng | 1.410.000 |
| Bảo trì phần mềm (gói cơ bản) | 1.000.000 |
| **TỔNG HÀNG THÁNG** | **2.410.000** |

---

### So sánh các phương án

| Tiêu chí | 1 chi nhánh (mua mới) | 1 chi nhánh (POS cũ) | 3 chi nhánh (mua mới) | 3 chi nhánh (POS cũ) |
|---|---|---|---|---|
| **Đầu tư ban đầu** | **27.630.000** | **16.630.000** | **52.890.000** | **19.890.000** |
| Hàng tháng | 2.270.000 | 2.270.000 | 2.410.000 | 2.410.000 |
| Hoàn vốn | < 1 tháng | < 1 tháng | ~2 tháng | < 1 tháng |

### Tổng theo thời gian (1 chi nhánh, dùng lại POS cũ — chi phí thấp nhất)

| Mốc thời gian | Chi phí | Ghi chú |
|---|---|---|
| **Ban đầu** | **16.630.000** | Phần mềm + thiết bị phụ |
| **Mỗi tháng** | **2.270.000** | Vận hành + bảo trì |
| **Năm đầu tiên** | **~37.060.000** | Ban đầu + 9 tháng (3 tháng BH miễn phí) |
| **Mở rộng thêm 1 quán** | **+1.630.000** | Chỉ QR + lắp đặt, phần mềm dùng chung |

---

## H. SO SÁNH CHI PHÍ: CÂY POS CŨ vs SMART F&B OS

| Hạng mục | Cây POS cũ (tháng) | Smart F&B OS (tháng) | Tiết kiệm |
|---|---|---|---|
| Lương thu ngân (3 quán x 1 NV) | 21.000.000 | 0 | -21.000.000 |
| Phí phần mềm/bản quyền POS | 3.000.000 - 6.000.000 | 0 | -3.000.000 ~ -6.000.000 |
| Hao hụt nguyên liệu (ước tính) | 10 - 15% doanh thu | < 2% doanh thu | Giảm 8 - 13% |
| Chi phí vận hành + bảo trì | 1.000.000 - 1.500.000 | 2.410.000 | +910.000 |
| | | | |
| **Tổng ước tính/tháng** | **~35.000.000 - 42.000.000** | **~5.410.000** | **Tiết kiệm ~30 - 37 triệu** |

> Tiết kiệm ròng: Khoảng **30 - 37 triệu/tháng**.  
> **Thời gian hoàn vốn** (dùng POS cũ, 3 quán): **Chưa đến 1 tháng**.  
> Từ tháng thứ 2 trở đi, toàn bộ khoản tiết kiệm là lợi nhuận ròng.

---

## I. ĐIỀU KHOẢN THANH TOÁN

### Thanh toán Phương án 1 (1 chi nhánh thí điểm)

| Đợt | Nội dung | Số tiền | Thời điểm |
|---|---|---|---|
| Đợt 1 | Ký hợp đồng + Khởi động phát triển | 7.000.000 | Ngày ký |
| Đợt 2 | Bàn giao GĐ 1 + Mua thiết bị 1 quán | 5.000.000 + thiết bị | Sau 2 tháng |
| Đợt 3 | Nghiệm thu + Golive | 3.000.000 | Sau 3-4 tháng |
| Hàng tháng | Vận hành + Bảo trì (sau 3 tháng BH miễn phí) | 2.270.000 | Từ tháng thứ 7 |

### Thanh toán Phương án 2 (3 chi nhánh đồng loạt)

| Đợt | Nội dung | Số tiền | Thời điểm |
|---|---|---|---|
| Đợt 1 | Ký hợp đồng + Khởi động phát triển | 7.000.000 | Ngày ký |
| Đợt 2 | Bàn giao GĐ 1 + Mua thiết bị 3 quán | 5.000.000 + thiết bị | Sau 2 tháng |
| Đợt 3 | Nghiệm thu + Golive | 3.000.000 | Sau 3-4 tháng |
| Hàng tháng | Vận hành + Bảo trì (sau 3 tháng BH miễn phí) | 2.410.000 | Từ tháng thứ 7 |

---

## J. GHI CHÚ QUAN TRỌNG

1. Báo giá chưa bao gồm thuế VAT (nếu có).
2. Phần mềm thuộc sở hữu 100% của khách hàng sau khi thanh toán đầy đủ, bao gồm toàn bộ mã nguồn.
3. Toàn bộ giao diện Quản lý và Admin là Web, truy cập trên điện thoại hoặc máy tính, không cần cài app.
4. Bảo hành phần mềm miễn phí 3 tháng sau nghiệm thu.
5. Hệ thống có chế độ Offline Mode trên POS và PWA cache menu. Router 4G là tùy chọn thêm nếu cần.
6. Nếu quán đã có máy POS cũ (Android, cảm ứng), có thể tái sử dụng — tiết kiệm đến 27 triệu. Máy in cũ ESC/POS cũng tái sử dụng được.
7. Dữ liệu hệ thống được sao lưu tự động hàng ngày.
8. Khi mất mạng, quán vẫn hoạt động: NV tạo đơn trên POS, thu tiền mặt, dữ liệu tự đồng bộ khi có mạng.
9. Chi phí phát sinh (Mục F) chỉ phát sinh khi có nhu cầu thực tế, không bắt buộc.
