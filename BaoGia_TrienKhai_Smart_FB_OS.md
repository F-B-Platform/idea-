# BÁO GIÁ & ĐỀ XUẤT TRIỂN KHAI HỆ THỐNG SMART F&B OS

> **Đơn vị nhận đề xuất:** Chuỗi Quán Cà phê / Đồ uống (Quy mô 3 chi nhánh)  
> **Mục tiêu:** Chuyển đổi mô hình từ Cây POS truyền thống sang Hệ thống Tự động hóa Smart F&B OS  
> **Ngày lập:** 11/08/2026

---

## 1. THƯ ĐỀ XUẤT CHUYỂN ĐỔI MÔ HÌNH

Hệ thống **Smart F&B OS** được thiết kế để **thay thế hoàn toàn cây POS truyền thống**, chuyển đổi mô hình phục vụ từ thụ động (khách xếp hàng/gọi phục vụ -> thu ngân gõ POS) sang mô hình **QR Self-Order kết hợp Màn hình pha chế KDS**.

### So sánh mô hình Cây POS cũ vs Smart F&B OS

| Tiêu chí | Mô hình Cây POS cũ | Mô hình Smart F&B OS |
|---|---|---|
| **Hình thức đặt món** | Khách xếp hàng tại cây POS hoặc NV dùng thiết bị order | Khách quét mã QR tại bàn bằng điện thoại cá nhân (PWA) |
| **Nhân sự thu ngân** | Bắt buộc 1 thu ngân đứng cây POS tại mỗi chi nhánh | Không cần thu ngân — Hệ thống tự nhận đơn & VietQR |
| **Tốc độ xử lý đơn** | Nghẽn đơn giờ cao điểm do phụ thuộc tốc độ gõ POS | Xử lý song song 100% số bàn cùng lúc, không chờ đợi |
| **Pha chế & Định lượng** | Barista tự nhớ công thức, dễ sai sót định lượng | KDS hiển thị công thức chuẩn kèm định lượng tự động |
| **Bản quyền phần mềm** | Thu phí bản quyền theo từng cây POS / thiết bị | Không thu phí bản quyền theo thiết bị |
| **Phản hồi khách hàng** | Không thu thập được phản hồi hoặc thu thủ công | Thu thập 100% Feedback (Hình ảnh, Ẩn danh, Alert khẩn) |

---

## 2. DỰ TOÁN CHI PHÍ THIẾT BỊ BAN ĐẦU (MUA 1 LẦN)

> Tận dụng tối đa hạ tầng sẵn có: Máy in nhiệt cũ (nếu hỗ trợ chuẩn ESC/POS) và mạng WiFi hiện tại của quán có thể tiếp tục sử dụng, giúp tối ưu chi phí đầu tư.

### Bảng chi phí thiết bị cho chuỗi 3 chi nhánh

| STT | Thiết bị & Hạng mục | Đơn giá (VNĐ) | Số lượng | Thành tiền (VNĐ) | Ghi chú & Khả năng tái sử dụng |
|---|---|---|---|---|---|
| 1 | **Màn hình KDS tại quầy** (TV 32 inch) | 4.000.000 | 3 cái | 12.000.000 | Thay thế vị trí cây POS cũ, hiển thị đơn cho Barista |
| 2 | **Android Box kết nối KDS** | 1.500.000 | 3 cái | 4.500.000 | Kết nối TV để chạy phần mềm pha chế KDS |
| 3 | **Máy in nhiệt khổ 80mm** | 2.000.000 | 3 cái | 6.000.000 | *Có thể dùng lại máy in cũ của cây POS nếu có* |
| 4 | **Bảng QR Code Acrylic tại bàn** | 30.000 | 60 bảng | 1.800.000 | 20 bàn/chi nhánh (Mã QR cố định hoặc NFC) |
| 5 | **Chi phí lắp đặt & Cấu hình hệ thống** | 1.000.000 | 3 chi nhánh | 3.000.000 | Setup thiết bị, cấu hình KDS, dán QR & chạy thử |
| | **TỔNG CHI PHÍ ĐẦU TƯ BAN ĐẦU** | | | **27.300.000** | *(Nếu tái sử dụng máy in cũ: 21.300.000 VNĐ)* |

---

## 3. CHI PHÍ HẠ TẦNG VẬN HÀNH HÀNG THÁNG

> Hệ thống vận hành trên hạ tầng Cloud tối ưu, áp dụng công nghệ máy chủ gộp và tận dụng các gói dịch vụ mở (Open API / Free tier), loại bỏ hoàn toàn phí duy trì đắt đỏ.

### Bảng chi phí hạ tầng vận hành (Dùng cho cả 3 chi nhánh)

| STT | Dịch vụ hạ tầng | Đơn vị cung cấp | Chi phí/tháng (VNĐ) | Mục đích sử dụng |
|---|---|---|---|---|
| 1 | **Máy chủ VPS Server** | Viettel IDC / VNPT / Cloud | 800.000 | Gộp Backend API, WebSocket real-time, Database & Redis |
| 2 | **Tên miền Domain (.com)** | Nhà đăng ký Tên miền | 30.000 | Tên miền truy cập QR Menu & Web Dashboard (360K/năm) |
| 3 | **AI LLM API Engine** | Google Gemini Flash API | 400.000 | Phục vụ Chatbot tư vấn đồ uống & AI Thống kê tự nhiên |
| 4 | **Thanh toán VietQR API** | NAPAS VietQR | 0 | Chuyển khoản VietQR tự động, miễn phí 100% |
| 5 | **Bảo mật & CDN** | Cloudflare Free Tier | 0 | Chứng chỉ SSL, tăng tốc tải trang & chống tấn công |
| 6 | **Thông báo đẩy (Push)** | Firebase FCM (Google) | 0 | Bắn thông báo gọi món/báo xong tới thiết bị nhân viên |
| 7 | **Gửi báo cáo EOD & Email** | SendGrid Free Tier | 0 | Gửi báo cáo kết ca tự động qua Email cho Quản lý |
| 8 | **Gửi voucher & Tri ân** | Zalo OA Free Tier | 0 | Gửi voucher tri ân tự động tới Zalo khách hàng |
| | **TỔNG CHI PHÍ VẬN HÀNH HÀNG THÁNG** | | **1.230.000** | *(Chia trung bình chỉ ~410.000 VNĐ/tháng/chi nhánh)* |

---

## 4. PHÂN TÍCH HIỆU QUẢ KINH TẾ (ROI & TỔNG TIẾT KIỆM)

### Bảng so sánh chi phí vận hành hàng tháng (Cho chuỗi 3 chi nhánh)

| Hạng mục chi phí | Vận hành với Cây POS cũ | Vận hành với Smart F&B OS | Tiết kiệm/tháng (VNĐ) |
|---|---|---|---|
| **Lương nhân sự Thu ngân** | 3 NV thu ngân × 7.000.000 VNĐ = **21.000.000 VNĐ** | 0 VNĐ *(Khách tự đặt & VietQR)* | **21.000.000** |
| **Phí bản quyền POS cũ** | 3 chi nhánh × 1.500.000 VNĐ = **4.500.000 VNĐ** | 0 VNĐ *(Không thu phí theo đầu máy)* | **4.500.000** |
| **Thất thoát nguyên liệu** | ~10-15% doanh thu (~**15.000.000 VNĐ**) | < 2% doanh thu (~**3.000.000 VNĐ**) | **12.000.000** |
| **Chi phí duy trì hạ tầng** | Phí bảo trì phần mềm POS: ~**1.500.000 VNĐ** | VPS Server + AI API: **1.230.000 VNĐ** | **270.000** |
| **TỔNG TIẾT KIỆM HÀNG THÁNG** | | | **37.770.000 VNĐ/tháng** |

### Bài toán thời gian hoàn vốn đầu tư (Payback Period)

- **Tổng chi phí đầu tư ban đầu:** 27.300.000 VNĐ
- **Số tiền tiết kiệm ròng hàng tháng:** 37.770.000 VNĐ − 1.230.000 VNĐ = **36.540.000 VNĐ/tháng**
- **Thời gian hoàn vốn:** **Dưới 1 tháng (Khoảng 22 - 25 ngày hoạt động)**

---

## 5. TỔNG HỢP CÁC LỰA CHỌN TRIỂN KHAI

### Phương án 1: Triển khai Tối ưu (Đề xuất)
- **Chi phí thiết bị (mua 1 lần):** 27.300.000 VNĐ *(hoặc 21.300.000 VNĐ nếu dùng lại máy in cũ)*
- **Chi phí duy trì:** 1.230.000 VNĐ/tháng cho cả 3 chi nhánh.
- **Đặc điểm:** Tận dụng 1 máy chủ VPS gộp cấu hình cao, sử dụng Gemini Flash API tối ưu chi phí, tận dụng mạng WiFi & thiết bị sẵn có tại quán.
- **Tổng chi phí năm đầu tiên:** **~42.000.000 VNĐ** (Đã bao gồm toàn bộ thiết bị và 12 tháng vận hành).

### Phương án 2: Triển khai Mở rộng Nâng cao
- **Chi phí thiết bị (mua 1 lần):** 87.000.000 VNĐ *(Trang bị thêm TV 43 inch, Mini PC riêng, Router WiFi chuyên dụng & Tablet dự phòng)*.
- **Chi phí duy trì:** 8.100.000 VNĐ/tháng *(Tách riêng 4 máy chủ Backend, AI Engine, Database & Redis)*.
- **Đặc điểm:** Phù hợp khi mở rộng quy mô trên 10 chi nhánh với lưu lượng hàng trăm nghìn lượt khách/ngày.

---

## 6. KẾT LUẬN & CAM KẾT VẬN HÀNH

1. **Thay thế hoàn toàn cây POS cũ:** Hệ thống loại bỏ sự phụ thuộc vào máy POS đắt tiền và nhân sự thu ngân cố định, giúp dòng công việc vận hành trôi chảy.
2. **Chi phí duy trì cực thấp:** Chỉ với **1.230.000 VNĐ/tháng** cho toàn bộ chuỗi 3 chi nhánh (chưa tới 14.000 VNĐ/ngày/chi nhánh).
3. **Thời gian hoàn vốn cực nhanh:** Tiết kiệm hơn 36 triệu VNĐ mỗi tháng, thu hồi 100% vốn đầu tư thiết bị ngay trong tháng đầu tiên.
