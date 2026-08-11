# BẢNG BÁO GIÁ TRIỂN KHAI HỆ THỐNG SMART F&B OS

> **Khách hàng:** Chuỗi Quán Cà phê / Đồ uống — 3 chi nhánh  
> **Giải pháp:** Hệ thống đặt món QR thông minh thay thế cây POS truyền thống  
> **Ngày lập:** 11/08/2026  
> **Hiệu lực báo giá:** 30 ngày kể từ ngày lập

---

## A. CHI PHÍ THIẾT BỊ (Thanh toán 1 lần)

### Thiết bị chính: Máy POS cảm ứng 2 màn hình

Mỗi chi nhánh trang bị 1 máy POS cảm ứng chuyên dụng đặt tại quầy:
- Mặt trong (Nhân viên): Màn hình cảm ứng 15.6 inch — thao tác nhận đơn, hoàn thành pha chế, báo hết món.
- Mặt ngoài (Khách hàng): Màn hình phụ 10 inch — hiển thị chi tiết đơn hàng, giá tiền, tổng cộng và mã VietQR thanh toán.

Thiết bị chạy liên tục cả ngày (16-18 tiếng), thiết kế chuyên dụng cho ngành F&B, có quạt tản nhiệt và pin dự phòng khi mất điện.

| STT | Hạng mục | Đơn giá | SL | Thành tiền | Ghi chú |
|---|---|---|---|---|---|
| 1 | Máy POS 2 màn hình cảm ứng (Sunmi T2s / D2s) | 9.000.000 | 3 | 27.000.000 | 15.6" NV cảm ứng + 10" Khách xem đơn & QR |
| 2 | Máy in hóa đơn nhiệt 80mm | 2.000.000 | 3 | 6.000.000 | Dùng lại máy in cũ nếu có: 0 đ |
| 3 | Bảng QR Code Acrylic để bàn | 30.000 | 60 | 1.800.000 | 20 bàn mỗi chi nhánh |
| 4 | Bảng QR Takeaway tại quầy | 30.000 | 3 | 90.000 | Khách mang đi quét QR đặt món tại quầy |
| 5 | Router WiFi + 4G Backup | 1.200.000 | 3 | 3.600.000 | Tự chuyển sang 4G khi WiFi chết, không gián đoạn |
| 6 | Lắp đặt, cấu hình & chạy thử | 1.000.000 | 3 | 3.000.000 | Trọn gói 3 chi nhánh |
| | | | | | |
| | **TỔNG THIẾT BỊ** | | | **41.490.000** | |
| | *Nếu dùng lại máy in cũ* | | | *35.490.000* | *Tiết kiệm 6 triệu* |

### Máy POS 2 màn hình hoạt động như thế nào?

Mặt nhân viên (15.6 inch cảm ứng):
- Hiển thị đơn hàng real-time từ QR Order của khách.
- Nhân viên bấm cảm ứng: hoàn thành đơn, báo hết món, xem sơ đồ bàn.
- Hiển thị công thức pha chi tiết kèm mỗi đơn.
- Tạo đơn thủ công cho khách order tại quầy (Takeaway).

Mặt khách hàng (10 inch hiển thị):
- Hiển thị danh sách món đang order, số lượng, đơn giá và tổng tiền.
- Hiển thị mã VietQR để khách quét thanh toán chuyển khoản.
- Khách kiểm tra đơn hàng minh bạch trước khi thanh toán.

---

## B. CHI PHÍ VẬN HÀNH HÀNG THÁNG (Cho cả 3 chi nhánh)

| STT | Hạng mục | Chi phí/tháng | Ghi chú |
|---|---|---|---|
| 1 | Máy chủ Cloud (Server) | 800.000 | VPS 4 vCPU, 8GB RAM — chạy toàn bộ hệ thống |
| 2 | Tên miền (.com) | 30.000 | 360.000/năm, chia ra 30.000/tháng |
| 3 | AI Engine (Chatbot + Thống kê) | 400.000 | Google Gemini Flash API |
| 4 | SIM 4G Data backup (3 quán) | 450.000 | 3 quán x 150.000/tháng, chỉ dùng khi WiFi chết |
| 5 | Giấy in nhiệt (tiêu hao) | 180.000 | 3 quán x 3 cuộn/tháng x 20.000/cuộn |
| | | | |
| | **TỔNG HÀNG THÁNG** | **1.860.000** | **~620.000/chi nhánh** |

---

## C. DỊCH VỤ MIỄN PHÍ ĐI KÈM (0 đ)

| STT | Dịch vụ | Nhà cung cấp | Mục đích |
|---|---|---|---|
| 1 | Thanh toán chuyển khoản VietQR | NAPAS | Khách quét mã thanh toán, miễn phí 100% |
| 2 | Bảo mật SSL & tăng tốc CDN | Cloudflare | Chứng chỉ bảo mật & tăng tốc tải trang |
| 3 | Thông báo đẩy (Push Notification) | Firebase (Google) | Báo trạng thái đơn, gọi nhân viên |
| 4 | Gửi báo cáo Email cuối ca | SendGrid | Tự động gửi báo cáo kết ca cho Quản lý |
| 5 | Gửi voucher tri ân qua Zalo | Zalo OA | Voucher sinh nhật, khách lâu chưa ghé |
| 6 | Lưu trữ ảnh menu & feedback | Self-hosted (trên Server) | Ảnh món, ảnh feedback khách chụp |
| 7 | Sao lưu dữ liệu tự động | Script tự động hàng ngày | Backup database lên Cloud miễn phí |
| 8 | Dữ liệu thời tiết (cho AI) | OpenWeatherMap | AI Chatbot tham khảo thời tiết gợi ý đồ uống |

---

## D. CHI PHÍ PHÁT SINH CÓ THỂ XẢY RA

| STT | Hạng mục | Khi nào phát sinh | Chi phí ước tính |
|---|---|---|---|
| 1 | Thay bảng QR Acrylic hư/mất | Khách làm hư hoặc mất | 30.000/bảng |
| 2 | Nâng cấp Zalo OA trả phí | Gửi voucher > 500 tin/tháng | 200.000 - 500.000/tháng |
| 3 | Nâng cấp cấu hình Server | Mở rộng > 5 chi nhánh | +400.000 - 800.000/tháng |
| 4 | Sửa chữa/thay thế máy POS | Sau 3-5 năm hoặc hư hỏng | 5.000.000 - 9.000.000/máy |
| 5 | Bảo trì & cập nhật phần mềm | Nếu ký hợp đồng bảo trì riêng | Thỏa thuận riêng |
| 6 | Đào tạo nhân viên mới | Tuyển NV mới cần hướng dẫn | Miễn phí (đào tạo nội bộ) |

---

## E. TỔNG HỢP CHI PHÍ THEO THỜI GIAN

| Mốc thời gian | Chi phí | Ghi chú |
|---|---|---|
| **Ban đầu (thiết bị)** | **41.490.000** | Thanh toán 1 lần. Dùng lại máy in cũ: 35.490.000 |
| **Mỗi tháng (vận hành)** | **1.860.000** | Trung bình 620.000/chi nhánh/tháng |
| **Năm đầu tiên** | **~63.800.000** | Thiết bị + 12 tháng vận hành |
| **Từ năm thứ 2** | **~22.300.000/năm** | Chỉ còn chi phí vận hành hàng tháng |

---

## F. SO SÁNH CHI PHÍ: CÂY POS CŨ vs SMART F&B OS

| Hạng mục | Cây POS cũ (tháng) | Smart F&B OS (tháng) | Tiết kiệm |
|---|---|---|---|
| Lương thu ngân (3 quán x 1 NV) | 21.000.000 | 0 | -21.000.000 |
| Phí phần mềm/bản quyền POS | 3.000.000 - 6.000.000 | 0 | -3.000.000 ~ -6.000.000 |
| Hao hụt nguyên liệu (ước tính) | 10 - 15% doanh thu | < 2% doanh thu | Giảm 8 - 13% |
| Chi phí duy trì hệ thống | 1.000.000 - 1.500.000 | 1.860.000 | Tương đương |
| | | | |
| **Tổng ước tính/tháng** | **~35.000.000 - 42.000.000** | **~4.860.000** | **Tiết kiệm ~30 - 37 triệu** |

> Lương thu ngân: Ước tính 6 - 7 triệu/NV (gồm phụ cấp & BHXH), tùy khu vực.  
> Phí POS cũ: Tùy nhà cung cấp đang dùng (iPOS, KiotViet, CukCuk,...).  
> **Thời gian hoàn vốn thiết bị:** Khoảng 1.5 - 2 tháng vận hành.

---

## G. ĐIỀU KHOẢN THANH TOÁN

| Đợt | Nội dung | Số tiền | Thời điểm |
|---|---|---|---|
| Đợt 1 | Thanh toán thiết bị & lắp đặt | 41.490.000 | Trước khi triển khai |
| Hàng tháng | Chi phí vận hành hạ tầng | 1.860.000 | Đầu mỗi tháng |

---

## H. GHI CHÚ QUAN TRỌNG

1. Báo giá trên chưa bao gồm thuế VAT (nếu có).
2. Giá thiết bị có thể thay đổi tùy thời điểm mua & nhà cung cấp.
3. Chi phí phát sinh (Mục D) chỉ phát sinh khi có nhu cầu thực tế, không bắt buộc.
4. Hệ thống có cơ chế dự phòng mất mạng 3 lớp: Router 4G tự chuyển, chế độ Offline trên POS, và PWA cache menu cho khách.
5. Máy in hóa đơn cũ của cây POS (chuẩn ESC/POS, khổ 80mm) có thể tái sử dụng, giảm 6.000.000 trong tổng chi phí.
6. Dữ liệu hệ thống (khách hàng, doanh thu, kho) được sao lưu tự động hàng ngày.
7. Máy POS cảm ứng Sunmi T2s/D2s là thiết bị chuyên dụng F&B, bảo hành chính hãng 12 tháng, tuổi thọ trung bình 3-5 năm sử dụng liên tục.
8. Khi mất mạng hoàn toàn, quán vẫn hoạt động bình thường: NV tạo đơn trên POS, thu tiền mặt. Khi có mạng lại, dữ liệu tự đồng bộ lên Cloud.
