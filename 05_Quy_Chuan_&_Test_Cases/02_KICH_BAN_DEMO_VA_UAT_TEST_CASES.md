# 🧪 KỊCH BẢN DEMO HỘI ĐỒNG & BỘ TEST CASES UAT (TIER 1 MVP)

> **Dự án:** Smart F&B Operating System  
> **Mục tiêu:** Kịch bản kiểm thử nghiệm thu (UAT) và Kịch bản Demo mượt mà trước Hội đồng bảo vệ đồ án.

---

## 🎬 1. KỊCH BẢN DEMO CHÍNH THỨC TRƯỚC HỘI ĐỒNG (LUỒNG NỐI LIỀN 5 PHÚT)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   KỊCH BẢN DEMO CHẠY THỰC TẾ (END-TO-END)              │
│                                                                        │
│  [Bước 1] ADMIN THIẾT LẬP MENU (1 phút)                                 │
│  • Admin mở Dashboard → Tạo món "Bạc Xỉu Sài Gòn" (Giá 35K) + Upload ảnh │
│  • Tạo biến thể Size M (+5K), Topping Trân châu (+10K).                │
│                                                                        │
│  [Bước 2] KHÁCH ĐẶT MÓN TẠI BÀN (1.5 phút)                             │
│  • Khách lấy điện thoại scan mã QR Bàn 5 → Menu PWA bật lên            │
│  • Chọn "Bạc Xỉu Sài Gòn" Size M, 50% đường, 100% đá, thêm Trân châu   │
│  • Nhập SĐT "0901234567" để tích điểm → Nhấn "Gửi Đơn Hàng"            │
│                                                                        │
│  [Bước 3] BẾP NHẬN ĐƠN & PHA CHẾ REAL-TIME (1 phút)                    │
│  • Màn hình KDS TV phát chuông 🔔 & hiện Card đơn #001 (Bàn 5)          │
│  • Barista xem công thức định lượng → Bấm "Bắt đầu pha chế"            │
│  • Điện thoại Khách nhảy thanh tiến trình "Đang pha chế ☕"             │
│  • Barista pha xong → Bấm "Hoàn thành món"                             │
│  • Điện thoại Khách nhảy tiến trình "Món đã sẵn sàng! 🥳"               │
│                                                                        │
│  [Bước 4] THANH TOÁN VIETQR & XÁC NHẬN (1 phút)                        │
│  • Khách nhấn nút "Yêu cầu thanh toán VietQR" trên điện thoại          │
│  • Mã VietQR động hiện lên màn hình khách + Alert nhảy trên Staff App  │
│  • Nhân viên bấm "Xác nhận đã nhận tiền"                               │
│                                                                        │
│  [Bước 5] ADMIN KẾT NỐI DASHBOARD BÁO CÁO (0.5 phút)                    │
│  • Mở Admin Dashboard → Thẻ Doanh thu nhảy tự động 50.000 VNĐ          │
│  • Biểu đồ cập nhật đơn hàng thành công real-time                      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 2. BẢNG TEST CASES UAT TIÊU CHUẨN (TOP 15 CRITICAL TEST CASES)

| ID | Module | Kịch bản Test (Test Case Description) | Thao tác (Steps) | Kết quả kỳ vọng (Expected Output) |
|---|---|---|---|---|
| TC-01 | Auth | Đăng nhập tài khoản Admin | Nhập `admin@smartfb.vn` / `Admin@123` | Đăng nhập thành công, trả về JWT Token & chuyển vào `/admin/dashboard`. |
| TC-02 | Auth | Đăng nhập sai mật khẩu | Nhập sai mật khẩu | Trả về 401 Unauthorized kèm message "Email hoặc mật khẩu sai". |
| TC-03 | Menu | Khách quét QR mở Menu | Mở đường dẫn chứa QR bàn | Hiển thị đầy đủ danh sách món còn bán, giao diện mobile-first mượt mà. |
| TC-04 | Menu | Khách tùy chỉnh Size & Topping | Chọn Bạc Xỉu + Size M (+5k) + Topping (+10k) | Tổng đơn giá món tự động nhảy từ 35k ➔ 50k. |
| TC-05 | Order | Khách đặt món không nhập SĐT | Bỏ qua SĐT, bấm Gửi đơn | Đơn hàng tạo thành công với trạng thái `Confirmed`, trả về OrderNumber `#001`. |
| TC-06 | Order | Khách nhập SĐT để tích điểm | Nhập SĐT `0901234567` khi gửi đơn | Đơn hàng tạo thành công, hệ thống tự cộng điểm Loyalty cho SĐT đó. |
| TC-07 | KDS | Real-time phát đơn mới sang KDS | Khách vừa nhấn Gửi đơn trên điện thoại | Màn hình KDS lập tức phát chuông 🔔 và hiện Card đơn hàng không cần reload. |
| TC-08 | KDS | Barista bấm Hoàn thành món | Barista click nút "Hoàn thành" trên KDS | Đơn đổi màu xanh trên KDS, điện thoại khách nhảy thông báo "Món đã sẵn sàng". |
| TC-09 | KDS | Cảnh báo đơn chờ quá lâu | Để đơn chờ quá 5 phút trên KDS | Card đơn đổi sang màu Đỏ nhấp nháy phát chuông cảnh báo. |
| TC-10 | Payment | Sinh mã VietQR tự động | Khách bấm "Yêu cầu bill VietQR" | Mã VietQR sinh ra đúng số tiền đơn hàng và nội dung chuyển khoản `DH...`. |
| TC-11 | Payment | NV xác nhận đã thu tiền | NV bấm "Xác nhận thanh toán" | Trạng thái đơn đổi sang `Paid`, điện thoại khách hiện thông báo "Cảm ơn quý khách". |
| TC-12 | Shift | Quản lý Mở ca két tiền | Nhập 2.000.000 VNĐ tiền đầu ca | Tạo CashShift thành công với trạng thái `Open`. |
| TC-13 | Shift | Quản lý Kết ca đối soát | Nhập tiền thực đếm 5.450.000 VNĐ | Hệ thống tự tính chênh lệch `Difference = -50.000 VNĐ` và tạo báo cáo ca. |
| TC-14 | Admin | Báo hết món tức thì | Barista hoặc Admin toggle "Hết món" Bạc Xỉu | Món Bạc Xỉu lập tức ẩn/disabled trên Menu QR của Khách hàng. |
| TC-15 | Report | Dashboard cập nhật doanh thu | Sau khi thanh toán đơn 50k thành công | Thẻ KPI Doanh thu hôm nay trên Admin Dashboard tăng đúng 50.000 VNĐ. |
