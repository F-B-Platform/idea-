# 📋 BẢNG BÁO GIÁ THƯƠNG MẠI & DỰ TOÁN CHI PHÍ TRIỂN KHAI
## DỰ ÁN NỀN TẢNG QUẢN LÝ VÀ VẬN HÀNH QUÁN CÀ PHÊ THÔNG MINH (SMART F&B OS)

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   THÔNG TIN HỒ SƠ BÁO GIÁ THƯƠNG MẠI                                   │
├──────────────────────────────────────┬─────────────────────────────────────────────────────────────────┤
│ 📄 **Mã Báo Giá (Quote No.):**       │ **BG-2026/08-SFB01**                                            │
│ 🏢 **Đơn Vị Cung Cấp Giải Pháp:**    │ **Đội Ngũ Kỹ Sư Phát Triển Hệ Thống Smart F&B OS**              │
│ 👤 **Khách Hàng / Đối Tác:**         │ **Chủ Quán / Ban Giám Đốc Chuỗi Cà Phê (03 Chi Nhánh)**        │
│ 📅 **Ngày Lập Báo Giá:**             │ **23/08/2026** (Hiệu lực: 60 ngày kể từ ngày ban hành)          │
│ 🎯 **Phạm Vi Triển Khai:**           │ **Trọn gói 03 Chi nhánh** (Sẵn sàng mở rộng lên 5 – 10 quán)    │
│ 💻 **Kiến Trúc Kỹ Thuật:**           │ **100% Web-First (Next.js 14 + .NET 8 + Docker + PayOS)**       │
│ 💵 **Đơn Vị Tiền Tệ:**               │ **VNĐ (Việt Nam Đồng)**                                         │
└──────────────────────────────────────┴─────────────────────────────────────────────────────────────────┘
```

---

## 📌 TÓM TẮT ĐIỀU HÀNH 3 KHỐI CHI PHÍ (EXECUTIVE COST SUMMARY)

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              TỔNG HỢP 3 KHỐI NGÂN SÁCH CHỦ ĐẠO DỰ ÁN                                   │
├──────────────────────────────────────┬────────────────────────────────┬────────────────────────────────┤
│ 1. CHI PHÍ PHÁT TRIỂN (CAPEX)        │ 2. CHI PHÍ VẬN HÀNH (OPEX)     │ 3. BẢO TRÌ & TÍNH NĂNG MỚI     │
│ • Phát triển trọn gói toàn bộ hệ thống│ • Máy chủ VPS, Tên miền, AI,   │ • 03 Tháng đầu: MIỄN PHÍ 100%  │
│ • Bàn giao 100% mã nguồn bản quyền   │   Vật tư giấy in nhiệt 3 quán  │ • Hỗ trợ theo lần:             │
│ • 0 VNĐ phí bản quyền phần mềm       │ • Kịch bản VPS tối ưu chi phí  │   👉 300.000 – 500.000 đ/lần   │
│                                      │                                │ • Thêm tính năng mới:          │
│ 💰 **15.000.000 VNĐ (TRẢ 1 LẦN)**    │ 💰 **940.000 VNĐ / THÁNG**     │   👉 THƯƠNG LƯỢNG THEO YÊU CẦU │
│    *(Sở hữu hệ thống vĩnh viễn)*     │    *(Chỉ ~313.000 đ/quán/tháng)*│    *(Tùy chỉnh linh hoạt)*     │
└──────────────────────────────────────┴────────────────────────────────┴────────────────────────────────┘
```

---

# PHẦN 1. BÁO GIÁ PHÁT TRIỂN PHẦN MỀM TRỌN GÓI (CAPEX)

> [!IMPORTANT]
> **Quy Chế Bản Quyền & Sở Hữu Vĩnh Viễn:** Khách hàng thanh toán **01 lần duy nhất**, được bàn giao **100% mã nguồn và tài liệu kỹ thuật**. Khách hàng sở hữu vĩnh viễn hệ thống, **hoàn toàn KHÔNG phải trả phí duy trì bản quyền phần mềm hàng tháng (0 VNĐ Software License Fee)**.

### 💰 TỔNG CHI PHÍ PHÁT TRIỂN PHẦN MỀM TRỌN GÓI: **15.000.000 VNĐ**
*(Bằng chữ: Mười lăm triệu đồng chẵn — Trả một lần duy nhất, sở hữu vĩnh viễn mã nguồn).*

#### 📦 Gói phát triển bao gồm đầy đủ toàn bộ các phân hệ và hạng mục kỹ thuật:
1. **Hệ thống Backend Lõi:** Kiến trúc .NET 8 Clean Architecture, CQRS MediatR, SignalR Real-time Hubs, Distributed Locks, phân quyền JWT/RBAC, 10 nhóm Resource RESTful APIs, State Machine 4 kênh bán (Dine-in A/B, Takeaway, Delivery).
2. **Hệ thống Frontend Toàn Diện:** Next.js 14 Monorepo gồm 5 Route Groups: Khách hàng gọi món PWA `(customer)`, Màn hình Bếp Dark Mode `(kds)`, POS Thu ngân `(staff)`, Cổng Quản lý `(manager)`, Bảng điều khiển Chuỗi `(admin)`.
3. **Cơ Sở Dữ Liệu:** PostgreSQL 16 với 30 bảng thực thể chuẩn hóa 3NF, hỗ trợ Thực đơn theo mùa (`seasonal_menus`), Quản lý ca & chốt sổ Z-Report (`cash_shifts`), tự động trừ tồn kho theo định mức BOM.
4. **Tích Hợp Cổng VietQR:** Tích hợp cổng PayOS tạo mã VietQR động theo đơn, xác thực thanh toán tức thì qua Webhook HMAC-SHA256, tiền chuyển thẳng 100% vào tài khoản quán (0% phí hoa hồng).
5. **Bộ Đôi Trí Tuệ Nhân Tạo (AI Modules):**
   * **AI-1 Chatbot Gemini 1.5 Flash:** Tư vấn đồ uống cá nhân hóa theo khẩu vị, dị ứng, thực đơn thời gian thực và thời tiết.
   * **AI-2 Gợi ý Combo Tự Động (Apriori):** Khai phá dữ liệu giỏ hàng để đề xuất các combo tăng doanh thu kèm giao diện duyệt cho quản lý.
6. **Chấm Công Khóa Mạng WiFi (WiFi-Locked HRM):** Xác thực 2 lớp BSSID/IP Subnet nội bộ chi nhánh + Mã số nhân viên, chống chấm công hộ và xuất báo cáo công Excel.
7. **Thiết Kế UI/UX & Bộ Kiểm Thử QA:** Bộ Design Tokens F&B, chuẩn tương phản WCAG AA, bộ kịch bản kiểm thử UAT 38+ Test Cases và kiểm tra chịu tải k6 (500 VUs).
8. **Đóng Gói Docker & CI/CD:** Docker Compose 4 containers, cấu hình Nginx Reverse Proxy, chứng chỉ SSL Let's Encrypt tự động, sẵn sàng triển khai ngay.

---

# PHẦN 2. DỰ TOÁN CHI PHÍ VẬN HÀNH ĐỊNH KỲ (OPEX HÀNG THÁNG)

Dự toán vận hành hàng tháng cung cấp **02 Kịch bản hạ tầng** để quán linh hoạt lựa chọn tùy theo định hướng:

### 🌟 KỊCH BẢN A: HẠ TẦNG CLOUD VPS VIỆT NAM (KHUYÊN DÙNG — TỐI ƯU CHI PHÍ)
*Mô hình tự triển khai Docker Compose trên VPS Việt Nam, chi phí tối thiểu, hiệu năng cao và đường truyền nội địa ổn định cho chuỗi 03 quán.*

| STT | Hạng Mục Vận Hành | Cấu Hình Kỹ Thuật & Nhà Cung Cấp | ĐVT | Đơn Giá / Tháng (VNĐ) | Thành Tiền / Tháng (VNĐ) | Ghi Chú & Mục Đích Sử Dụng |
|:---:|---|---|:---:|:---:|:---:|---|
| 1 | **Cloud VPS Linux (Chính)** | 4 vCPU, 8GB RAM, 80GB NVMe SSD *(Vietnix / Viettel IDC)* | Tháng | 450.000 | **450.000** | Chạy Docker: Backend, Frontend, PostgreSQL, Redis (Đủ tải 3-5 quán) |
| 2 | **Tên Miền Thương Hiệu `.vn`** | Domain riêng (VD: `smartcoffee.vn`) *(Mắt Bão / PA VN)* | Tháng | 40.000 | **40.000** | ~480.000 VNĐ/năm chia đều cho 12 tháng duy trì |
| 3 | **Cloudflare CDN & SSL** | Cloudflare Free Tier (Edge CDN, SSL 1.3, Anti-DDoS) | Tháng | 0 | **0** | Tăng tốc tải Menu PWA, bảo mật chống tấn công DDoS |
| 4 | **Lưu Trữ Ảnh (Object Storage)** | Cloudflare R2 / AWS S3 (Miễn phí 10GB đầu tiên) | Tháng | 0 | **0** | Lưu ảnh món ăn WebP và ảnh đánh giá của khách hàng |
| 5 | **Cổng Thanh Toán VietQR** | PayOS Gateway (Mô hình Account-to-Account) | Tháng | 0 | **0** | Miễn phí 100% giao dịch, tiền chuyển thẳng vào tài khoản quán |
| 6 | **AI Chatbot Gemini 1.5 Flash** | Google Gemini API (~2.000 lượt hỏi đáp món/quán/tháng) | Tháng | 150.000 | **150.000** | Tư vấn đồ uống cá nhân hóa (Áp dụng Redis cache 75%) |
| 7 | **Email & Dữ Liệu Thời Tiết** | Resend (3.000 mail/tháng) + OpenWeatherMap Free | Tháng | 0 | **0** | Báo cáo doanh thu cuối ngày & dữ liệu nhiệt độ cho AI |
| 8 | **Vật Tư Giấy In Nhiệt K80** | 50 cuộn/tháng cho 3 quán (10 cuộn POS + 7 cuộn KDS/quán) | Tháng | 300.000 | **300.000** | In hóa đơn thanh toán kèm VietQR & phiếu nhận đồ (6.000đ/cuộn) |
| | | | | | | |
| 🏆 | **TỔNG OPEX KỊCH BẢN A** | **Áp dụng trọn gói cho toàn bộ chuỗi 03 Chi nhánh** | | | **940.000 VNĐ / tháng** | **Bình quân chỉ ~313.000 VNĐ / quán / tháng** |

---

### 🚀 KỊCH BẢN B: HẠ TẦNG MANAGED CLOUD / SERVERLESS (MỞ RỘNG LINH HOẠT)
*Mô hình sử dụng các dịch vụ Cloud quốc tế có sẵn tính năng Auto-scaling và Managed Database.*

| STT | Hạng Mục Dịch Vụ | Nhà Cung Cấp & Cấu Hình | ĐVT | Chi Phí / Tháng (VNĐ) | Ghi Chú & Đặc Điểm |
|:---:|---|---|:---:|:---:|---|
| 1 | **Backend & Frontend App Hosting** | Render.com / Railway Team Tier | Tháng | 750.000 | Tự động cân bằng tải và triển khai không gián đoạn |
| 2 | **Managed PostgreSQL Database** | Supabase Pro Tier / Neon DB | Tháng | 600.000 | Tự động sao lưu Point-in-Time, mở rộng dung lượng linh hoạt |
| 3 | **Tên Miền & Dịch Vụ Mạng** | Domain `.vn` + Cloudflare Pro CDN | Tháng | 50.000 | Tên miền thương hiệu + tăng tốc tải hình ảnh toàn cầu |
| 4 | **Dịch Vụ AI Gemini Flash** | Google Cloud Gemini API Pay-as-you-go | Tháng | 150.000 | Tư vấn món cá nhân hóa theo lưu lượng thực tế |
| 5 | **Vật Tư Giấy In Nhiệt K80** | 50 cuộn/tháng cho chuỗi 3 quán | Tháng | 300.000 | In hóa đơn thanh toán và phiếu dán ly pha chế |
| | | | | | |
| 🏆 | **TỔNG OPEX KỊCH BẢN B** | **Áp dụng cho chuỗi 03 Chi nhánh** | | **1.850.000 VNĐ / tháng** | **Bình quân ~616.000 VNĐ / quán / tháng** |

---

# PHẦN 3. DỊCH VỤ BẢO TRÌ, HỖ TRỢ KỸ THUẬT & PHÁT TRIỂN TÍNH NĂNG

> [!TIP]
> **Chính Sách Bảo Hành:** Hệ thống được **BẢO HÀNH MIỄN PHÍ 03 THÁNG ĐẦU TIÊN** kể từ ngày nghiệm thu (sửa toàn bộ lỗi phát sinh, giám sát hệ thống và hỗ trợ kỹ thuật qua Zalo/Hotline 24/7).

### 🛠️ Sau Thời Gian Bảo Hành (Lựa chọn linh hoạt theo nhu cầu thực tế):

1. **Hỗ Trợ Xử Lý Sự Cố & Bảo Trì Theo Từng Lần (On-Demand Support):**
   * **Chi phí:** **300.000 – 500.000 VNĐ / lần** (tùy theo mức độ phát sinh).
   * **Phạm vi hỗ trợ:** Kiểm tra và tối ưu máy chủ VPS, sửa lỗi phát sinh do môi trường vận hành, hỗ trợ phục hồi dữ liệu từ bản backup, cập nhật cấu hình cổng thanh toán hoặc mạng chi nhánh.
2. **Gói Hỗ Trợ Bảo Trì Định Kỳ Hàng Tháng (Tùy chọn nếu cần):**
   * **Chi phí:** **1.000.000 VNĐ / tháng** (trọn gói cho cả chuỗi 3 chi nhánh ~333.000 đ/quán).
   * **Phạm vi:** Giám sát Uptime 24/7, tự động backup dữ liệu hàng ngày lên Cloud riêng, hỗ trợ kỹ thuật ưu tiên < 30 phút, hỗ trợ đổi giá/menu định kỳ.
3. **Yêu Cầu Nâng Cấp & Phát Triển Tính Năng Mới (New Feature Requests):**
   * **Chi phí:** **Thương lượng theo từng yêu cầu thực tế** (Báo giá riêng).
   * **Quy trình:** Khi quán có nhu cầu bổ sung thêm tính năng mới (ví dụ: mở rộng kênh bán mới, tích hợp thiết bị mới, kết nối phần mềm kế toán bên ngoài...), đội ngũ kỹ sư sẽ khảo sát phạm vi, thống nhất giải pháp và báo giá cụ thể theo độ phức tạp.

---

# PHẦN 4. DANH MỤC THIẾT BỊ PHẦN CỨNG CẦN THIẾT TẠI QUÁN (THAM KHẢO)

> [!WARNING]
> Toàn bộ hệ thống chạy trên nền tảng **100% Web-First**, do đó quán hoàn toàn có thể **tận dụng thiết bị sẵn có** (Smart TV, Laptop cũ, Tablet, Điện thoại) mà **KHÔNG bắt buộc phải mua mới**. Chi phí thiết bị dưới đây mang tính chất tham khảo chuẩn bị và **0 VNĐ tính vào ngân sách phần mềm của dự án**.

### 📱 Danh Sách Thiết Bị Cần Có Tại Mỗi Chi Nhánh:
1. **Màn hình KDS Bếp (01 cái/quán):** Smart TV 32"–43" có trình duyệt web, hoặc Tablet Android/iPad 10"+ đặt tại quầy pha chế để Barista nhận đơn, xem định mức BOM và thao tác 86-toggle hết món.
2. **Thiết bị Web POS Quầy (01 cái/quán):** Laptop, máy tính PC để bàn hoặc máy tính bảng có trình duyệt Google Chrome để Thu ngân tạo đơn Takeaway, tra cứu tích điểm CRM 10 ly và quản lý ca thu chi.
3. **Máy in nhiệt khổ K80 (01 máy/quán):** Máy in bill nhiệt khổ K80 cổng LAN hoặc USB (các dòng phổ biến như Xprinter, Epson) dùng in hóa đơn thanh toán VietQR (Nhánh B) và tem dán ly.
4. **Bộ phát Router WiFi (01–02 bộ/quán):** Router phát sóng WiFi mạng nội bộ ổn định và có BSSID cố định để phục vụ tính năng chấm công nhân viên khóa theo mạng chi nhánh.
5. **Standee & Nhãn Decal Mã QR:**
   * **Standee QR Delivery (01–02 tấm/quán):** Đặt tại quầy hoặc cửa ra vào để khách quét đặt đồ giao tận nơi.
   * **Bộ nhãn QR dán mặt bàn (Theo số bàn):** Decal in mã QR từng bàn ép màng chống nước để khách quét tự gọi món (Self-Ordering).
