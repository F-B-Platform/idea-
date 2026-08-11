# BẢNG BÁO GIÁ TRIỂN KHAI HỆ THỐNG SMART F&B OS

> **Khách hàng:** Chuỗi Quán Cà phê / Đồ uống — 3 chi nhánh  
> **Giải pháp:** Hệ thống đặt món QR thông minh thay thế cây POS truyền thống  
> **Ngày lập:** 11/08/2026  
> **Hiệu lực báo giá:** 30 ngày kể từ ngày lập

---

## A. CHI PHÍ THIẾT BỊ (Thanh toán 1 lần)

### Lựa chọn 1: Màn hình TV + Android Box (Không cảm ứng)

Nhân viên xem đơn trên TV, thao tác hoàn thành đơn qua điện thoại (Staff App).

| STT | Hạng mục | Đơn giá | SL | Thành tiền | Ghi chú |
|---|---|---|---|---|---|
| 1 | TV 32 inch hiển thị đơn tại quầy | 4.000.000 | 3 | 12.000.000 | Đặt tại vị trí cây POS cũ |
| 2 | Android Box kết nối TV | 1.500.000 | 3 | 4.500.000 | Chạy phần mềm KDS trên TV |
| 3 | Máy in hóa đơn nhiệt 80mm | 2.000.000 | 3 | 6.000.000 | Dùng lại máy in cũ nếu có: 0 đ |
| 4 | Bảng QR Code Acrylic để bàn | 30.000 | 60 | 1.800.000 | 20 bàn mỗi chi nhánh |
| 5 | Lắp đặt, cấu hình & chạy thử | 1.000.000 | 3 | 3.000.000 | Trọn gói 3 chi nhánh |
| | | | | | |
| | **TỔNG LỰA CHỌN 1** | | | **27.300.000** | |
| | *Nếu dùng lại máy in cũ* | | | *21.300.000* | *Tiết kiệm 6 triệu* |

### Lựa chọn 2: Tablet cảm ứng (Đề xuất)

Nhân viên bấm trực tiếp trên màn hình cảm ứng để hoàn thành đơn, báo hết món, xem chi tiết.

| STT | Hạng mục | Đơn giá | SL | Thành tiền | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tablet Android 10-11 inch | 5.000.000 | 3 | 15.000.000 | Thay thế TV + Box, NV thao tác cảm ứng |
| 2 | Giá đỡ Tablet cố định tại quầy | 200.000 | 3 | 600.000 | Gắn cố định hoặc đặt đứng |
| 3 | Máy in hóa đơn nhiệt 80mm | 2.000.000 | 3 | 6.000.000 | Dùng lại máy in cũ nếu có: 0 đ |
| 4 | Bảng QR Code Acrylic để bàn | 30.000 | 60 | 1.800.000 | 20 bàn mỗi chi nhánh |
| 5 | Lắp đặt, cấu hình & chạy thử | 1.000.000 | 3 | 3.000.000 | Trọn gói 3 chi nhánh |
| | | | | | |
| | **TỔNG LỰA CHỌN 2** | | | **26.400.000** | |
| | *Nếu dùng lại máy in cũ* | | | *20.400.000* | *Tiết kiệm 6 triệu* |

### So sánh 2 lựa chọn thiết bị

| Tiêu chí | TV + Android Box | Tablet cảm ứng |
|---|---|---|
| Chi phí thiết bị (3 quán) | 27.300.000 | 26.400.000 |
| Cảm ứng trực tiếp | Không — NV dùng ĐT thao tác | Có — bấm trực tiếp trên màn hình |
| Kích thước hiển thị | 32 inch (lớn, nhìn xa rõ) | 10-11 inch (vừa tầm tay) |
| Di động | Không (gắn cố định) | Có thể cầm theo khi cần |
| Số thiết bị cần quản lý | 2 (TV + Box) | 1 (Tablet) |

---

## B. CHI PHÍ VẬN HÀNH HÀNG THÁNG (Cho cả 3 chi nhánh)

| STT | Hạng mục | Chi phí/tháng | Ghi chú |
|---|---|---|---|
| 1 | Máy chủ Cloud (Server) | 800.000 | VPS 4 vCPU, 8GB RAM — chạy toàn bộ hệ thống |
| 2 | Tên miền (.com) | 30.000 | 360.000/năm, chia ra 30.000/tháng |
| 3 | AI Engine (Chatbot + Thống kê) | 400.000 | Google Gemini Flash API |
| 4 | Giấy in nhiệt (tiêu hao) | 180.000 | 3 quán x 3 cuộn/tháng x 20.000/cuộn |
| | | | |
| | **TỔNG HÀNG THÁNG** | **1.410.000** | **~470.000/chi nhánh** |

---

## C. DỊCH VỤ MIỄN PHÍ ĐI KÈM (0 đ — Không phát sinh chi phí)

| STT | Dịch vụ | Nhà cung cấp | Mục đích |
|---|---|---|---|
| 1 | Thanh toán chuyển khoản VietQR | NAPAS | Khách quét mã thanh toán, miễn phí 100% |
| 2 | Bảo mật SSL & tăng tốc CDN | Cloudflare | Chứng chỉ bảo mật & tăng tốc tải trang |
| 3 | Thông báo đẩy (Push Notification) | Firebase (Google) | Báo trạng thái đơn, gọi nhân viên |
| 4 | Gửi báo cáo Email cuối ca | SendGrid | Tự động gửi báo cáo kết ca cho Quản lý |
| 5 | Gửi voucher tri ân qua Zalo | Zalo OA | Voucher sinh nhật, khách lâu chưa ghé |
| 6 | Lưu trữ ảnh menu & feedback | Self-hosted (trên Server) | Ảnh món, ảnh feedback khách chụp |
| 7 | Sao lưu dữ liệu tự động | Script tự động hàng ngày | Backup database, ảnh lên Cloud miễn phí |
| 8 | Dữ liệu thời tiết (cho AI) | OpenWeatherMap | AI Chatbot tham khảo thời tiết gợi ý đồ uống |

---

## D. CHI PHÍ PHÁT SINH CÓ THỂ XẢY RA

| STT | Hạng mục | Khi nào phát sinh | Chi phí ước tính |
|---|---|---|---|
| 1 | Thay bảng QR Acrylic hư/mất | Khách làm hư hoặc mất | 30.000/bảng |
| 2 | Nâng cấp Zalo OA trả phí | Gửi voucher > 500 tin/tháng | 200.000 - 500.000/tháng |
| 3 | Nâng cấp cấu hình Server | Mở rộng > 5 chi nhánh | +400.000 - 800.000/tháng |
| 4 | Thay Tablet hoặc Android Box hỏng | Sau 2-3 năm sử dụng | 1.500.000 - 5.000.000/cái |
| 5 | Bảo trì & cập nhật phần mềm | Nếu ký hợp đồng bảo trì riêng | Thỏa thuận riêng |
| 6 | Đào tạo nhân viên mới | Tuyển NV mới cần hướng dẫn | Miễn phí (đào tạo nội bộ) |

---

## E. TỔNG HỢP CHI PHÍ THEO THỜI GIAN

### Với Lựa chọn 2 — Tablet cảm ứng (Đề xuất)

| Mốc thời gian | Chi phí | Ghi chú |
|---|---|---|
| **Ban đầu (thiết bị)** | **26.400.000** | Thanh toán 1 lần. Dùng lại máy in cũ: 20.400.000 |
| **Mỗi tháng (vận hành)** | **1.410.000** | Trung bình 470.000/chi nhánh/tháng |
| **Năm đầu tiên** | **~43.300.000** | Thiết bị + 12 tháng vận hành |
| **Từ năm thứ 2** | **~16.900.000/năm** | Chỉ còn chi phí vận hành hàng tháng |

### Với Lựa chọn 1 — TV + Android Box

| Mốc thời gian | Chi phí | Ghi chú |
|---|---|---|
| **Ban đầu (thiết bị)** | **27.300.000** | Thanh toán 1 lần. Dùng lại máy in cũ: 21.300.000 |
| **Mỗi tháng (vận hành)** | **1.410.000** | Trung bình 470.000/chi nhánh/tháng |
| **Năm đầu tiên** | **~44.200.000** | Thiết bị + 12 tháng vận hành |
| **Từ năm thứ 2** | **~16.900.000/năm** | Chỉ còn chi phí vận hành hàng tháng |

---

## F. SO SÁNH CHI PHÍ: CÂY POS CŨ vs SMART F&B OS

| Hạng mục | Cây POS cũ (tháng) | Smart F&B OS (tháng) | Tiết kiệm |
|---|---|---|---|
| Lương thu ngân (3 quán x 1 NV) | 21.000.000 | 0 | -21.000.000 |
| Phí phần mềm/bản quyền POS | 3.000.000 - 6.000.000 | 0 | -3.000.000 ~ -6.000.000 |
| Hao hụt nguyên liệu (ước tính) | 10 - 15% doanh thu | < 2% doanh thu | Giảm 8 - 13% |
| Chi phí duy trì hệ thống | 1.000.000 - 1.500.000 | 1.410.000 | Tương đương |
| | | | |
| **Tổng ước tính/tháng** | **~35.000.000 - 42.000.000** | **~4.410.000** | **Tiết kiệm ~30 - 37 triệu** |

> **Thời gian hoàn vốn thiết bị:** Trong vòng tháng đầu tiên vận hành.  
> Lương thu ngân: Tùy khu vực, ước tính 6 - 7 triệu/NV (gồm phụ cấp & BHXH).  
> Phí POS cũ: Tùy nhà cung cấp đang dùng (iPOS, KiotViet, CukCuk,...).

---

## G. ĐIỀU KHOẢN THANH TOÁN

| Đợt | Nội dung | Số tiền | Thời điểm |
|---|---|---|---|
| Đợt 1 | Thanh toán thiết bị & lắp đặt | 26.400.000 - 27.300.000 | Trước khi triển khai |
| Hàng tháng | Chi phí vận hành hạ tầng | 1.410.000 | Đầu mỗi tháng |

---

## H. GHI CHÚ QUAN TRỌNG

1. Báo giá trên chưa bao gồm thuế VAT (nếu có).
2. Giá thiết bị có thể thay đổi tùy thời điểm mua & nhà cung cấp.
3. Chi phí phát sinh (Mục D) chỉ phát sinh khi có nhu cầu thực tế, không bắt buộc.
4. Hệ thống yêu cầu kết nối Internet ổn định tại mỗi chi nhánh (sử dụng WiFi sẵn có của quán).
5. Máy in hóa đơn cũ của cây POS (chuẩn ESC/POS, khổ 80mm) có thể tái sử dụng, giảm 6.000.000 trong tổng chi phí thiết bị.
6. Dữ liệu hệ thống (khách hàng, doanh thu, kho) được sao lưu tự động hàng ngày, đảm bảo an toàn.
