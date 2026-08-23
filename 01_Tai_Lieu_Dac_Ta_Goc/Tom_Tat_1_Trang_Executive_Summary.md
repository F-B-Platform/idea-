# 📋 TÓM TẮT DỰ ÁN 1 TRANG (EXECUTIVE SUMMARY)
## Smart F&B Operating System — AI-Powered QR Order & Management Platform

> [!NOTE]
> **Đồ án Capstone Tốt nghiệp Kỹ sư Phần mềm (16 tuần — 4 thành viên: 2 Backend + 2 Frontend)**  
> **Slogan:** *"Không cần máy POS cồng kềnh, không cần thu ngân gõ đơn — Khách scan QR, tự chọn món, tự thanh toán; Nhân viên vận hành mượt mà trên Web-First."*  
> **Nguồn sự thật chuẩn hóa (Source of Truth):** `Smart_FB_OS_Revised_4members.docx` & `ORIGINAL_REQUEST.md`  

---

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       BỨC TRANH TỔNG THỂ DỰ ÁN TRÊN 1 TRANG                                          │
├────────────────────────────────┬───────────────────────────────────────┬──────────────────────────────────────────────┤
│ 8 BẤT CẬP QUÁN CÀ PHÊ HIỆN NAY │ 6 ĐỘT PHÁ NGHIỆP VỤ CỐT LÕI           │ TECH STACK CHUẨN HÓA                         │
│ 1. Máy POS đắt đỏ (8 - 25 triệu)│ 1. Dine-In 2 nhánh (VietQR / Tiền mặt)│ • Backend: .NET 8 Clean Architecture (CQRS)  │
│ 2. Xếp hàng nghẽn quầy cao điểm│ 2. QR Delivery (Phí 20k, 100% VietQR)│ • Frontend: Next.js 14 App Router Monorepo   │
│ 3. Gian lận chấm công 5 - 10%  │ 3. Takeaway POS (Tích 10 ly, Trả sau) │ • Database: PostgreSQL 16 (25 thực thể 3NF)  │
│ 4. Thất thoát nguyên liệu kho  │ 4. Chấm công Khóa WiFi (BSSID / IP)   │ • Cache & Lock: Redis 7 (Cache-aside, PubSub)│
│ 5. Mù mờ tài chính & P&L       │ 5. Nền tảng Web-First (Bỏ Staff App)  │ • Realtime: SignalR WebSockets (4 Hubs)      │
│ 6. Lệch vị pha chế & thiếu data│ 6. Admin Full CRUD & Menu mùa lên lịch│ • Payment: Cổng PayOS VietQR (HMAC-SHA256)   │
│ 7. 80% khách vãng lai mất dấu  ├───────────────────────────────────────┼──────────────────────────────────────────────┤
│ 8. Ra quyết định theo cảm tính │ 2 MODULE TRÍ TUỆ NHÂN TẠO (AI ACTIVE) │ HIỆU QUẢ KINH TẾ & THỰC THI (ROI)            │
│                                │ • AI-1: Chatbot RAG Gemini 1.5 Flash  │ 💰 Tiết kiệm: 15 - 22 triệu VNĐ/tháng/quán   │
│                                │ • AI-2: Khai phá Combo Apriori Mining │ ⏱️ Thực thi: 16 tuần (08 Sprints) / 4 Kỹ sư  │
│                                │ • (AI-3, 4, 5 cấu trúc ở Future Work) │ 📦 Quy mô: 62 tính năng core chuẩn production│
└────────────────────────────────┴───────────────────────────────────────┴──────────────────────────────────────────────┘
```

---

### 1. Bối Cảnh Thị Trường & Tuyên Bố Giá Trị (Value Proposition)

Ngành kinh doanh dịch vụ ăn uống (F&B) và chuỗi cà phê tại Việt Nam đang đối mặt với bài toán chi phí vận hành nặng nề: đầu tư thiết bị máy POS đắt đỏ (8 - 25 triệu VNĐ/máy), ùn tắc cục bộ tại quầy thu ngân trong khung giờ cao điểm, thất thoát 5 - 15% doanh thu do bùng đơn hoặc gian lận ca kíp.  

**Smart F&B OS** giải quyết triệt để các bất cập trên bằng nền tảng quản trị **Web-First tích hợp QR Code đa năng và Trí tuệ Nhân tạo (AI)**, mang lại 3 giá trị cam kết:
- **Giảm 60% - 100%** chi phí đầu tư phần cứng máy POS ban đầu nhờ tận dụng thiết bị cá nhân của khách và trình duyệt Web sẵn có.
- **Tăng 40%** công suất phục vụ trong khung giờ cao điểm nhờ quy trình tự phục vụ (Self-Ordering) và điều phối KDS tức thời.
- **Triệt tiêu 0%** rủi ro thất thoát doanh thu và bùng đơn thông qua cổng VietQR động khớp lệnh tự động.

---

### 2. 6 Đột Phá Nghiệp Vụ Cốt Lõi (Core Differentiators)

1. **Đặt Món Tại Bàn (Dine-In) — 2 Nhánh Thanh Toán Song Song:**
   - **Nhánh A (VietQR Trả trước):** Khách quét QR bàn ➔ Chọn món ➔ Thanh toán VietQR động ➔ Cổng PayOS xác nhận `Paid` ➔ **Bếp KDS mới nhận đơn** qua SignalR ➔ Pha chế ➔ Phục vụ. *(Triệt tiêu 100% rủi ro bùng đơn).*
   - **Nhánh B (Tiền mặt Trả sau):** Khách quét QR bàn ➔ Chọn Tiền mặt ➔ **Đơn vào bếp KDS ngay lập tức** (`Confirmed`) ➔ Pha chế ➔ Nhân viên mang món ra bàn **kèm Hóa đơn có in sẵn mã VietQR** ➔ Khách linh hoạt trả tiền mặt hoặc quét VietQR trên bill ➔ Nhân viên xác nhận hoàn tất. *(Phù hợp khách quen và người lớn tuổi).*
2. **Đặt Hàng Giao Tận Nơi (QR Delivery) — Phí Ship Cố Định 20.000 VNĐ:**
   - Khách quét mã QR Delivery (trên poster, fanpage, standee) ➔ Mở PWA ➔ Bắt buộc nhập Số điện thoại + **Địa chỉ giao hàng** (`delivery_address`) ➔ Hệ thống tự động cộng **Phí ship cố định 20.000 VNĐ** (`delivery_fee = 20000`) ➔ **100% Thanh toán VietQR trả trước** (Khóa hoàn toàn COD để chống bùng hàng) ➔ Bếp KDS nhận đơn điều phối giao tận nhà.
3. **Bán Mang Đi Tại Quầy (Takeaway Staff POS) — Tích 10 Ly Tặng 1 & Thu Sau:**
   - Khách mua mang đi **không dùng mã QR**; Nhân viên thu ngân thao tác trực tiếp trên giao diện **Web POS Quầy**.
   - Thu ngân tra cứu SĐT CRM: Khách mới ➔ Tạo nhanh hồ sơ; Khách cũ ➔ Hiển thị số ly tích lũy (`CupBalance`).
   - **Chính sách Loyalty 10 ly = 1 ly miễn phí:** **CHỈ ÁP DỤNG DUY NHẤT CHO ĐƠN TAKEAWAY** (Không áp dụng Dine-In và Delivery). Đủ 10 ly được tặng 1 ly miễn phí thứ 11.
   - Khách nhận món và **Thanh toán sau khi nhận**: Thu ngân chọn Tiền mặt (tính tiền thối tự động) hoặc xuất VietQR quầy.
4. **Chấm Công Khóa Mạng WiFi (WiFi-Locked Attendance):**
   - Loại bỏ hoàn toàn định vị vệ tinh GPS (sai số lớn) và mã QR 30 giây.
   - Nhân viên kết nối mạng WiFi của quán ➔ Mở Web chấm công ➔ Quét mã QR chấm công tĩnh + Nhập Mã NV ➔ Hệ thống xác thực kép: (a) Đúng địa chỉ BSSID Access Point / IP Subnet của chi nhánh?, (b) Đúng Mã số nhân viên hợp lệ? ➔ Hợp lệ ghi nhận vào ca/ra ca; Sai WiFi từ chối tức thì.
5. **Hợp Nhất 100% Nền Tảng Web-First (Loại Bỏ Hoàn Toàn Staff Mobile App):**
   - Không phát triển ứng dụng di động riêng cho nhân viên. Mọi nghiệp vụ phục vụ, KDS pha chế, sơ đồ bàn, chuông gọi phục vụ, xác nhận thanh toán chạy mượt mà trên **Web Responsive và Web KDS** chuẩn hóa (`(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`).
6. **Chủ Chuỗi Toàn Quyền Quản Trị (Admin Full CRUD):**
   - Toàn quyền Quản trị Sản phẩm (Tạo, Sửa, Xóa, Thay thế món), Định mức nguyên liệu BOM chi tiết cho từng size (S/M/L), Tạo Combo giảm giá, Tải ảnh món WebP lên CDN, Cấu hình giá bán theo từng chi nhánh, Bật/tắt khóa món khẩn cấp (86-Toggle), Sắp xếp thứ tự hiển thị thực đơn và **Lên lịch Thực đơn theo mùa (Seasonal Menu)** tự động xuất hiện/ẩn theo ngày.

---

### 3. Phân Rã 2 Module Trí Tuệ Nhân Tạo (Active AI Modules)

- **AI-1 (Personalized Recommendation Chatbot — Active MVP):** Ứng dụng mô hình **Google Gemini 1.5 Flash** kết hợp kỹ thuật RAG (Retrieval-Augmented Generation), ngữ cảnh thời tiết thực tế (OpenWeatherMap) và lịch sử tiêu dùng CRM để tư vấn đồ uống cá nhân hóa. Được đánh giá khoa học bằng Precision@K, Recall@K, NDCG@K và độ trễ phản hồi <= 1.5 giây.
- **AI-2 (Automated Combo Discovery Engine — Active MVP):** Khai phá dữ liệu giỏ hàng lịch sử bằng thuật toán **Apriori / FP-Growth** (Market Basket Analysis), tự động phát hiện các cặp sản phẩm có độ kết hợp cao (Support, Confidence, Lift > 1.2) và đề xuất combo tối ưu cho Chủ chuỗi phê duyệt (Human-in-the-loop) nhằm gia tăng giá trị đơn hàng trung bình (AOV).
- *(3 Module mở rộng tương lai được đóng gói sẵn Extension Points: AI-3 Text-to-SQL Analytics, AI-4 Customer Churn Prediction RFM, AI-5 Menu Demand Forecasting).*

---

### 4. Kiến Trúc Kỹ Thuật & Ngăn Xếp Công Nghệ Chuẩn Hóa

| Tầng Kiến Trúc | Công Nghệ Lựa Chọn | Vai Trò Kỹ Thuật & Đặc Điểm Vận Hành |
|---|---|---|
| **Backend API** | **.NET 8 (C#)** Clean Architecture | MediatR CQRS, FluentValidation, EF Core 8, 4 lớp phân tách chặt chẽ. |
| **Frontend Web** | **Next.js 14 App Router** Monorepo | TypeScript, Tailwind CSS, Shadcn UI, TanStack Query, PWA Mobile-First. |
| **Database** | **PostgreSQL 16** | 25 thực thể chuẩn hóa 3NF, quan hệ toàn vẹn ACID, lưu trữ cấu hình đa chi nhánh. |
| **Caching & Lock** | **Redis 7** | Cache-aside danh mục menu, Distributed Lock chống race condition, SignalR Backplane. |
| **Real-time Hubs** | **SignalR WebSockets** | 4 Hubs chuyên biệt: `OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`. |
| **Cổng Thanh Toán** | **PayOS / VietQR Gateway** | Sinh mã VietQR động, đối soát giao dịch thời gian thực qua Webhook HMAC-SHA256. |

---

### 5. Giá Trị Kinh Tế & Chỉ Số Hoàn Vốn (ROI & Financial Impact)

- **Cắt giảm chi phí đầu tư ban đầu:** Tiết kiệm 100% chi phí mua sắm máy POS và máy quét mã vạch (tiết kiệm 15 - 50 triệu VNĐ/chi nhánh khi mở quán).
- **Tối ưu hóa nhân sự quầy:** Giảm 50% áp lực nhân viên thu ngân trong ca cao điểm (tiết kiệm 7 - 14 triệu VNĐ tiền lương/tháng/quán).
- **Triệt tiêu thất thoát:** Giảm 80% thất thoát nguyên liệu nhờ định mức BOM tự động trừ kho trên KDS và 0% bùng đơn ở kênh Delivery & Dine-In VietQR.
- **Gia tăng doanh thu:** Tăng 15 - 25% doanh thu bán chéo nhờ AI-1 gợi ý topping và AI-2 phát hành combo tự động.
- **Tổng giá trị kinh tế mang lại:** Tạo ra thặng dư và tiết kiệm từ **15 đến 22 triệu VNĐ/tháng/chi nhánh** (~180 - 260 triệu VNĐ/năm).

---

### 6. Thông Số Thực Thi Dự Án & Cam Kết Bàn Giao (Project Execution)

- **Quy mô đội ngũ:** 4 Kỹ sư phần mềm Capstone (2 Backend + 2 Frontend).
- **Thời lượng phát triển:** 16 tuần (chia làm **08 Sprints**, 2 tuần/Sprint).
- **Quy mô bàn giao:** **62 Tính năng cốt lõi** phân bổ cho 4 nhóm Actor (20 Khách hàng C-01–C-20, 13 Nhân viên S-01–S-13, 12 Quản lý M-01–M-12, 17 Chủ chuỗi A-01–A-17).
- **Cam kết chất lượng:** 100% tuân thủ Clean Architecture, kiểm soát toàn diện trường hợp biên (Edge Cases), loại bỏ hoàn toàn tính năng thừa/cũ và sẵn sàng triển khai thực tế cho các chuỗi cà phê hiện đại.
