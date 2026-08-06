# 📌 TỔNG HỢP TÀI LIỆU F&B — PHÂN TÍCH, THIẾT KẾ & NGHIÊN CỨU

> **Tài liệu gộp từ:** F&B_TLBS.md + F&B_TLBS2.md + F&B_TLBS3.md
>
> **Mục đích:** Tổng hợp toàn bộ nghiên cứu, phân tích, thiết kế 3 đề tài nền tảng (F&B, B2B, Clinic) + Deep Research AI+IoT cho F&B.

---

# 📚 MỤC LỤC

| Chương | Nội Dung | Nguồn Gốc |
|---|---|---|
| **CHƯƠNG 1** | Tổng Quan & So Sánh 2 Đề Tài (F&B vs B2B) — Báo cáo chi tiết | F&B_TLBS.md |
| **CHƯƠNG 2** | Deep Research: F&B + AI + IoT — Có gì mới lạ? | F&B_TLBS2.md |
| **CHƯƠNG 3** | 3 Đề Tài Full-Scale (F&B, B2B, Clinic) — So sánh & Khuyến nghị | F&B_TLBS3.md |

---
---

# ═══════════════════════════════════════════════════════
# CHƯƠNG 1: BÁO CÁO CHI TIẾT — THÁO GỠ VÀ THIẾT KẾ 2 ĐỀ TÀI NỀN TẢNG
# ═══════════════════════════════════════════════════════

> *Nguồn gốc: F&B_TLBS.md*

---

## 1.1 TỔNG QUAN VÀ SO SÁNH 2 ĐỀ TÀI

| Tiêu Chí So Sánh | IDEA 1: Nền Tảng F&B Thông Minh | IDEA 2: Sàn B2B Wholesale Thông Minh |
|---|---|---|
| **Lĩnh vực** | Quản lý nhà hàng, cà phê, chuỗi F&B | Phân phối sỉ, B2B e-Commerce |
| **Quy mô hệ thống** | 8 Module chính, 5 Actors | 7 Module chính, 4 Actors |
| **Đối tượng người dùng** | Chủ chuỗi, Quản lý cửa hàng, Thu ngân, Bếp, Khách hàng | Nhà sản xuất/Phân phối, Đại lý/Cửa hàng, Đơn vị vận chuyển, Sàn |
| **Số lượng AI features** | 6 tính năng AI cốt lõi | 6 tính năng AI cốt lõi |
| **Giao diện & Trải nghiệm** | Web Dashboard + POS Tablet + App Mobile + KDS Bếp | Web Portal B2B + Mobile App B2B |
| **Tích hợp bên thứ 3** | VietQR/MoMo, Zalo OA, Hóa đơn điện tử (VNPT/Viettel) | GHN/GHTK/ViettelPost, Cổng thanh toán B2B, OCR Engine |
| **Tính ứng dụng thị trường** | Rất cao (Thị trường F&B Việt Nam bùng nổ, các POS cũ thiếu AI) | Cực cao (Xu hướng chuyển đổi số chuỗi cung ứng B2B) |
| **Độ ấn tượng khi Demo** | ⭐⭐⭐⭐⭐ (Demo trực quan với POS, KDS, Chatbot Zalo) | ⭐⭐⭐⭐ (Nghiệp vụ sâu, logic công nợ & định giá AI) |

---

## 1.2 IDEA 1: NỀN TẢNG QUẢN LÝ F&B THÔNG MINH (AI-POWERED F&B OPERATING SYSTEM)

### 1.2.1 Tổng Quan & Bài Toán Thực Tế
- **Bài toán:** Các phần mềm POS hiện nay tại Việt Nam (iPOS, KiotViet, CukCuk) chủ yếu đóng vai trò ghi nhận giao dịch tĩnh. Doanh nghiệp F&B gặp 3 vấn đề lớn:
  1. **Thất thoát nguyên liệu:** Không dự báo được chính xác lượng nguyên liệu cần dùng → hao hụt do hết hạn hoặc thiếu hàng giờ cao điểm.
  2. **Tối ưu ca làm việc kém:** Xếp ca dư thừa vào giờ vắng, thiếu nhân sự vào giờ cao điểm.
  3. **Chăm sóc khách hàng thụ động:** Không dự đoán được hành vi khách rời đi (churn), gửi chương trình khuyến mãi đại trà không hiệu quả.
- **Giải pháp:** Xây dựng hệ thống vận hành F&B toàn diện kết hợp **Trí Tuệ Nhân Tạo (AI)** đóng vai trò như một "Trợ lý vận hành thông minh".

### 1.2.2 Các Vai Trò Trong Hệ Thống (Actors)
1. **Admin (Chủ chuỗi F&B):**
   - Quản lý danh sách chi nhánh, phân quyền nhân sự.
   - Xem báo cáo tổng quan tài chính, doanh thu, lợi nhuận thực tế theo thời gian thực.
   - Cấu hình các tham số AI và phê duyệt các chương trình khuyến mãi tự động.
2. **Manager (Quản lý cửa hàng / chi nhánh):**
   - Quản lý hoạt động hàng ngày của 1 chi nhánh cụ thể.
   - Kiểm duyệt đơn nhập hàng do AI đề xuất.
   - Duyệt ca làm việc, điều chỉnh định lượng nguyên liệu (BOM).
3. **Staff (Nhân viên thu ngân / Phục vụ):**
   - Sử dụng màn hình POS trên Tablet/PC để order món, gộp/tách bàn, tính tiền.
   - Nhận thông báo trực tiếp khi món ăn hoàn thành từ Bếp.
4. **Kitchen (Bộ phận Bếp / Pha chế):**
   - Sử dụng màn hình KDS (Kitchen Display System) để tiếp nhận đơn order.
   - Cập nhật trạng thái chế biến: *Đang chế biến* → *Hoàn thành* → *Đã phục vụ*.
5. **Customer (Khách hàng cuối):**
   - Tương tác qua Zalo Mini App / Web App: Xem menu, đặt bàn trước, tích điểm loyalty, xem lịch sử order và đánh giá chất lượng.

---

### 1.2.3 Chi Tiết 8 Module Chức Năng

#### Module 1: 🛒 POS — Quản Lý Bán Hàng & Order
- **Sơ đồ bàn trực quan:** Hiển thị trạng thái theo thời gian thực (Trống, Đang phục vụ, Đặt trước, Cần dọn dẹp).
- **Tạo order linh hoạt:** Hỗ trợ chọn topping, ghi chú đặc biệt (không đá, ít ngọt, dị ứng).
- **Gộp/Tách bàn & Đổi bàn:** Tự động tính toán lại hóa đơn và đồng bộ tức thì sang bộ phận Bếp.
- **Thanh toán đa phương thức:** Tích hợp mã VietQR động, Ví MoMo, ZaloPay, Tiền mặt.
- **Màn hình KDS (Kitchen Display System):** Thay thế in phiếu bếp thủ công bằng màn hình cảm ứng điện tử.

#### Module 2: 📦 Kho — Quản Lý Nguyên Liệu & Xuất Kho Quầy
- **Quản lý xuất kho quầy (Requisition):** Ghi nhận chính xác lượng nguyên liệu xuất từ Kho tổng lên Quầy pha chế (Ví dụ: xuất 2 túi Cà phê hạt 1kg, 5 hộp Sữa tươi 1L, 1 chai Syrup Caramel).
- **Theo dõi tồn kho 2 tầng (Kho tổng & Quầy):** Quản lý tồn kho theo đơn vị thực tế (Kg, Lít, Hộp, Chai, Bao), phù hợp thực tế vận hành quán.
- **Quản lý nhập / xuất / chuyển kho:** Ghi nhận lịch sử nhập kho từ nhà cung cấp, chuyển nguyên liệu giữa các chi nhánh hoặc từ Kho tổng ra Quầy.
- **Kiểm kê định kỳ & Đối soát:** Nhập số lượng thực tế kiểm đếm (Kg/Hộp/Chai) tại quầy & kho → hệ thống tự động tính toán chênh lệch và cảnh báo thất thoát.

#### Module 3: 📋 Menu — Quản Lý Thực Đơn & Giá
- **Phân loại danh mục:** Món chính, Món phụ, Đồ uống, Topping, Combo.
- **Cấu hình giá đa chi nhánh:** Cho phép thiết lập giá bán khác nhau giữa các khu vực (Ví dụ: Giá tại Quận 1 cao hơn Giá tại Quận 9).
- **Quản lý trạng thái món:** Bật/Tắt món tức thì khi hết nguyên liệu cấu thành.

#### Module 4: 👥 CRM & Loyalty — Quản Lý & Chăm Sóc Khách Hàng
- **Hồ sơ định danh khách hàng:** Lưu trữ SĐT, tên, ngày sinh, lịch sử giao dịch, tổng chi tiêu.
- **Hệ thống tích điểm tự động:** Tự động quy đổi doanh số thành điểm thưởng (Ví dụ: 100,000 VNĐ = 10 điểm).
- **Hạng thành viên (Tiering):** Đồng, Bạc, Vàng, Kim Cương với các đặc quyền giảm giá riêng.

#### Module 5: 📊 Analytics & AI Forecast — Phân Tích & Dự Báo Kinh Doanh
- **Dashboard quản trị:** Biểu đồ doanh thu, số lượng đơn hàng, món bán chạy nhất (Top Sellers), khung giờ vàng.
- **Phân tích chi phí & Lợi nhuận:** Tự động tính toán Cost of Goods Sold (COGS) dựa trên giá nhập nguyên liệu và lịch sử xuất kho quầy.

#### Module 6: 🤖 AI Chatbot — Đặt Bàn & Đặt Món Trực Tuyến
- **Tích hợp đa kênh:** Hoạt động trên Zalo OA và Facebook Messenger.
- **Đặt bàn thông minh:** Tự động kiểm tra bàn trống theo thời gian khách yêu cầu và ghi nhận vào hệ thống POS.
- **Hỏi đáp thực đơn:** Trả lời tự động các câu hỏi về thực đơn (món ăn chay, món không chứa gluten, món bán chạy).

#### Module 7: 👨‍💼 HRM — Quản Lý Nhân Sự & Ca Làm Việc
- **Phân ca làm việc:** Khai báo ca làm (Ca sáng, Ca chiều, Ca tối) và xếp lịch cho nhân viên.
- **Chấm công thông minh:** Check-in / Check-out qua QR code hoặc GPS tại cửa hàng.
- **Bảng lương tự động:** Tính lương dựa trên tổng số giờ làm việc thực tế, phụ cấp ca và tiền thưởng.

#### Module 8: 🧾 Tài Chính & Hóa Đơn Điện Tử (E-Invoice)
- **Quản lý sổ quỹ:** Ghi nhận thu chi tiền mặt, chuyển khoản ngân hàng.
- **Phát hành Hóa đơn điện tử:** Tích hợp API xuất hóa đơn GTGT tự động gửi về Email/Zalo của khách hàng theo quy định của Tổng cục Thuế.

---

### 1.2.4 Các Tính Năng AI & Mô Hình Sử Dụng

1. **AI Dự Báo Nhu Cầu Nguyên Liệu (Inventory Demand Forecasting):**
   - *Thuật toán/Mô hình:* **Prophet** hoặc **XGBoost / LightGBM** (Time-Series ML).
   - *Đầu vào:* Lịch sử bán hàng 6-12 tháng, dữ liệu ngày lễ, thời tiết, sự kiện địa phương.
   - *Kết quả:* Dự báo chính xác lượng nguyên liệu (kg trà, lít sữa, bao đường) cần tiêu thụ trong 7 ngày tới → Tự động tạo đơn đề xuất nhập hàng gửi Manager.

2. **AI Gợi Ý Combo & Món Đi Kèm (Cross-selling Recommendation Engine):**
   - *Thuật toán/Mô hình:* **Apriori Algorithm (Association Rule Mining)** hoặc **Collaborative Filtering**.
   - *Kết quả:* Khám phá các mẫu mua hàng ẩn (Ví dụ: 80% khách mua Bánh mì Thịt sẽ mua thêm Cà phê Sữa) → Gợi ý cho thu ngân tư vấn combo tại POS hoặc hiển thị trên Zalo Mini App.

3. **AI Dự Đoán Khách Hàng Rời Bỏ (Customer Churn Prediction):**
   - *Thuật toán/Mô hình:* **Random Forest / XGBoost Classifier**.
   - *Đầu vào:* Tần suất ghé thăm, khoảng cách giữa các lần mua, tổng chi tiêu, đánh giá feedback.
   - *Kết quả:* Gắn nhãn nguy cơ rời bỏ (High Churn Risk) → Hệ thống tự động gửi Voucher giảm giá 20% qua Zalo để kéo khách quay lại.

4. **AI Xếp Lịch Nhân Sự Tự Động (Smart Staff Scheduling):**
   - *Thuật toán/Mô hình:* **Constraint Satisfaction Problem (CSP) / Linear Programming** kết hợp dữ liệu dự báo lượng khách.
   - *Kết quả:* Tự động phân bổ số lượng nhân viên thu ngân và phục vụ tối ưu theo từng khung giờ trong ngày, tránh lãng phí chi phí nhân công.

5. **AI Chatbot Đặt Bàn NLP Tiếng Việt (Conversational AI Agent):**
   - *Thuật toán/Mô hình:* **RAG (Retrieval-Augmented Generation)** sử dụng **Gemini 1.5 Flash / GPT-4o-mini** + Vector Database (**pgvector**).
   - *Kết quả:* Hiểu ngữ cảnh tiếng Việt tự nhiên, trích xuất đúng Thời gian, Số lượng khách, Yêu cầu đặc biệt để tạo order đặt bàn tự động.

---

### 1.2.5 Kiến Trúc Kỹ Thuật & Luồng Dữ Liệu

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARCHITECTURAL SYSTEM OVERVIEW (F&B OS)                   │
│                                                                             │
│  [ Web Dashboard (React/Next.js) ]    [ Tablet POS (React/Vue) ]           │
│  [ Mobile Staff App (Flutter) ]       [ Customer Zalo Mini App ]            │
│                                  │                                          │
│                                  ▼                                          │
│                         ┌──────────────────┐                                │
│                         │   API Gateway    │ (REST / WebSocket / Auth JWT)  │
│                         └────────┬─────────┘                                │
│                                  │                                          │
│       ┌──────────────────────────┼──────────────────────────┐               │
│       ▼                          ▼                          ▼               │
│  ┌──────────────┐         ┌──────────────┐         ┌──────────────┐         │
│  │ Order & POS  │         │  Inventory   │         │ Customer &   │         │
│  │ Service      │         │  Service     │         │ CRM Service  │         │
│  └──────┬───────┘         └──────┬───────┘         └──────┬───────┘         │
│         │                        │                        │                 │
│         ▼                        ▼                        ▼                 │
│  ┌──────────────┐         ┌──────────────┐         ┌──────────────┐         │
│  │ HRM & Staff  │         │ AI & ML Engine│        │ Chatbot RAG  │         │
│  │ Service      │         │ (Python/FastAPI)       │ Service      │         │
│  └──────┬───────┘         └──────┬───────┘         └──────┬───────┘         │
│         │                        │                        │                 │
│         └────────────────────────┼────────────────────────┘                 │
│                                  ▼                                          │
│                    ┌────────────────────────────┐                           │
│                    │ PostgreSQL + pgvector      │                           │
│                    │ Redis Cache (Realtime DB)  │                           │
│                    └────────────────────────────┘                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 1.2.6 Phân Công Nhiệm Vụ Team 4 Người

| Vai Trò | Thành Viên | Trách Nhiệm Chi Tiết |
|---|---|---|
| **Backend & Architecture Lead** | **Sinh viên 1** | Thiết kế Database schema (PostgreSQL), API Gateway, JWT Auth. Xây dựng Core Microservices: Order Service, POS Engine, Payment Integration (VietQR/MoMo API). Triển khai Server, Docker containerization, WebSocket cho giao tiếp real-time giữa POS và KDS. |
| **Frontend & Mobile Lead** | **Sinh viên 2** | Phát triển Web Admin Dashboard (React.js / Next.js) cho Chủ chuỗi & Manager. Phát triển giao diện POS Tablet tối ưu trải nghiệm thao tác nhanh cho thu ngân. Xây dựng màn hình Bếp KDS (Kitchen Display System). |
| **AI & Data Engineer** | **Sinh viên 3** | Xây dựng mô hình AI dự báo nhu cầu nguyên liệu (Time-series forecast). Phát triển mô hình Churn Prediction và Recommendation Engine (Gợi ý combo). Xây dựng Chatbot RAG đặt bàn tiếng Việt tích hợp Zalo OA API. |
| **Full-Stack & Business Logic** | **Sinh viên 4** | Phát triển Module Inventory (Quản lý kho tổng & Xuất kho quầy theo Kg/Hộp/Chai). Phát triển Module HRM (Xếp ca, chấm công QR, tính lương). Xây dựng Zalo Mini App / Mobile App cho Khách hàng cuối (Tích điểm, đặt món). |

---

## 1.3 IDEA 2: SÀN THƯƠNG MẠI ĐIỆN TỬ B2B THÔNG MINH (AI-POWERED B2B WHOLESALE MARKETPLACE)

### 1.3.1 Tổng Quan & Bài Toán Thực Tế
- **Bài toán:** Giao dịch bán sỉ (B2B) giữa **Nhà sản xuất / Nhà phân phối (Suppliers)** và **Đại lý / Cửa hàng bán lẻ (Buyers/Retailers)** hiện nay vẫn phụ thuộc nặng nề vào sổ sách, tin nhắn Zalo và bảng tính Excel. Các điểm nghẽn lớn gồm:
  1. **Công nợ phức tạp:** Khó kiểm soát rủi ro nợ xấu khi đại lý mua trước trả sau.
  2. **Định giá thủ công:** Bảng giá sỉ thay đổi liên tục theo số lượng mua, cấp độ đại lý và thời điểm thị trường.
  3. **Khó dự báo hàng hóa:** Nhà phân phối không biết khi nào đại lý sắp hết hàng để chủ động chào đơn mới.
- **Giải pháp:** Xây dựng **Sàn thương mại điện tử B2B chuyên biệt**, tích hợp AI để tự động hóa định giá động, chấm điểm tín dụng đại lý, dự báo nhu cầu mua sỉ và xử lý chứng từ hóa đơn bằng OCR.

### 1.3.2 Các Vai Trò Trong Hệ Thống (Actors)
1. **Platform Admin (Quản trị sàn B2B):**
   - Phê duyệt hồ sơ pháp lý của Nhà cung cấp (Supplier) và Đại lý (Buyer).
   - Giám sát toàn bộ dòng tiền, phí giao dịch sàn và cấu hình quy tắc hạn mức tín dụng chung.
2. **Supplier (Nhà cung cấp / Nhà phân phối):**
   - Đăng tải danh mục sản phẩm sỉ với cấu trúc giá theo bậc (Tiered Pricing).
   - Quản lý đơn đặt hàng sỉ, xác nhận xuất kho, quản lý danh sách đại lý được cấp hạn mức công nợ.
3. **Buyer (Đại lý / Cửa hàng tạp hóa / Retailer):**
   - Tìm kiếm sản phẩm sỉ bằng hình ảnh hoặc mô tả tiếng Việt.
   - Đặt đơn hàng sỉ (với số lượng lớn), quản lý hạn mức công nợ được cấp, thực hiện tái đặt hàng nhanh (Re-order).
4. **Logistics Partner (Đơn vị vận chuyển B2B):**
   - Tiếp nhận thông báo gom đơn hàng sỉ, cập nhật trạng thái vận chuyển theo thời gian thực (Tracking).

---

### 1.3.3 Chi Tiết 7 Module Chức Năng

#### Module 1: 🏪 B2B Marketplace — Sàn Giao Dịch & Tìm Kiếm
- **Catalog sản phẩm B2B:** Hỗ trợ cấu hình giá bán sỉ theo số lượng (Ví dụ: Mua 10-49 thùng = 200k/thùng; Mua 50-100 thùng = 180k/thùng).
- **Tìm kiếm ngữ nghĩa (Semantic Search):** Cho phép đại lý gõ từ khóa tự nhiên (Ví dụ: *"bột giặt loại nhỏ đóng gói 100g"*) → Hệ thống trả về đúng sản phẩm dù tên chuẩn là *"OMO Sachet 100g"*.
- **So sánh giá nhà cung cấp:** Cho phép đại lý so sánh chiết khấu, chính sách giao hàng giữa các NCC cùng bán 1 mặt hàng.

#### Module 2: 📋 Order Management — Quản Lý Đơn Hàng Sỉ
- **Giỏ hàng B2B:** Xử lý đơn hàng phức tạp với hàng trăm SKU và khối lượng/thể tích lớn.
- **Quy trình phê duyệt đơn sỉ (Approval Workflow):** Tự động chuyển trạng thái đơn: *Đã đặt hàng* → *NCC xác nhận* → *Kiểm tra công nợ* → *Xuất kho* → *Giao hàng* → *Đã đối soát*.
- **Tính năng Re-Order 1-Click:** Cho phép đại lý đặt lại toàn bộ đơn hàng của tháng trước chỉ với 1 thao tác.

#### Module 3: 💰 Dynamic Pricing & Credit — Giá Động & Quản Lý Công Nợ
- **Quản lý hạn mức công nợ (Credit Limit):** Thiết lập số tiền tối đa đại lý được nợ và thời hạn thanh toán (Ví dụ: Hạn mức 100 triệu, gối đầu 30 ngày).
- **Báo cáo tuổi nợ (Aging Report):** Phân loại nợ theo các mốc: *Trong hạn*, *Quá hạn 1-15 ngày*, *Quá hạn 16-30 ngày*, *Nợ xấu (>60 ngày)*.
- **Tự động chặn đơn:** Tự động khóa tính năng đặt hàng mới nếu đại lý có nợ quá hạn chưa thanh toán.

#### Module 4: 🚚 Logistics & Fulfillment — Vận Chuyển Sỉ
- **Tích hợp hãng vận chuyển B2B:** Kết nối API với GHN, Viettel Post hoặc đội xe riêng của NCC.
- **Tính toán chi phí cồng kềnh:** Tự động tính phí vận chuyển dựa trên tổng trọng lượng (kg) và thể tích của đơn sỉ.

#### Module 5: 📄 AI Document OCR — Xử Lý Chứng Từ & Hóa Đơn
- **Tự động quét và nhập liệu hóa đơn (Invoice OCR):** Cho phép NCC upload ảnh chụp/file PDF hóa đơn VAT đầu vào → AI tự trích xuất dữ liệu đưa vào kho.
- **Đối soát 3 bên (3-Way Matching):** Tự động đối chiếu dữ liệu giữa: *Đơn đặt hàng (PO)* ↔ *Phát hành hóa đơn (Invoice)* ↔ *Biên bản giao hàng (Receipt)*.

#### Module 6: 📊 Analytics & Market Intelligence — Phân Tích Thị Trường
- **Dashboard Supplier:** Thống kê doanh số bán sỉ, sản phẩm sắp hết hàng, tỷ lệ thu hồi công nợ đúng hạn.
- **Dashboard Buyer:** Thống kê tổng chi tiêu, xu hướng biến động giá của các mặt hàng chủ lực.

#### Module 7: 💬 AI B2B Sales Assistant — Trợ Lý Mua Hàng Thông Minh
- **Trợ lý ảo giao tiếp ngôn ngữ tự nhiên:** Giúp đại lý hỏi nhanh thông tin: *"Sản phẩm Mì Hảo Hảo bên nào đang có chiết khấu cao nhất?"* hoặc *"Công nợ tháng này của tôi còn bao nhiêu?"*.

---

### 1.3.4 Các Tính Năng AI & Mô Hình Sử Dụng

1. **AI Chấm Điểm Tín Dụng Đại Lý (B2B Credit Scoring):**
   - *Thuật toán/Mô hình:* **XGBoost / Logistic Regression / Decision Trees**.
   - *Đầu vào:* Lịch sử thanh toán đúng hạn, thời gian hoạt động trên sàn, giá trị đơn hàng trung bình, tỷ lệ hủy đơn.
   - *Kết quả:* Tính toán Điểm tín dụng (Credit Score từ 300 - 850) và tự động đề xuất Hạn mức công nợ phù hợp cho từng Đại lý.

2. **AI Định Giá Động (Dynamic Pricing Engine):**
   - *Thuật toán/Mô hình:* **Regression Trees / Reinforcement Learning**.
   - *Đầu vào:* Tồn kho hiện tại của NCC, mức độ cầu của thị trường, giá của đối thủ cạnh tranh trên sàn.
   - *Kết quả:* Tự động gợi ý mức giá chiết khấu tối ưu cho từng lô hàng sỉ nhằm giải phóng tồn kho nhanh nhất mà vẫn đảm bảo biên lợi nhuận.

3. **AI Dự Báo Tái Đặt Hàng (Buyer Re-order Prediction):**
   - *Thuật toán/Mô hình:* **Time-Series / Survival Analysis**.
   - *Kết quả:* Phân tích chu kỳ tiêu thụ hàng của đại lý → Gửi thông báo chủ động: *"Cửa hàng của bạn có thể sắp hết Nước rửa chén Sunlight. Đặt hàng ngay để nhận chiết khấu 5%."*

4. **AI Trích Xuất Dữ Liệu Hóa Đơn (Smart Invoice OCR):**
   - *Thuật toán/Mô hình:* **PaddleOCR / Donut Transformer** kết hợp **LLM Structuring (Pydantic)**.
   - *Kết quả:* Đọc chính xác 98% thông tin từ hóa đơn VAT scanned/PDF (Mã số thuế, Danh sách hàng hóa, Tiền thuế VAT, Tổng tiền) đưa vào cơ sở dữ liệu.

5. **AI Tìm Kiếm Ngữ Nghĩa (Semantic Vector Search):**
   - *Thuật toán/Mô hình:* **BGE-M3 Embedding** + Vector Database (**pgvector**).
   - *Kết quả:* Tìm kiếm chính xác sản phẩm theo ý định mua hàng dù đại lý gõ từ khóa không chuẩn hoặc dùng ngôn ngữ địa phương.

6. **AI Assistant Tra Cứu Dữ Liệu Doanh Nghiệp (Enterprise RAG Agent):**
   - *Thuật toán/Mô hình:* **Agentic RAG Engine** với khả năng tự sinh câu truy vấn SQL (Text-to-SQL) an toàn để trả lời về báo cáo tài chính/công nợ cho quản lý.

---

### 1.3.5 Kiến Trúc Kỹ Thuật & Luồng Dữ Liệu

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 ARCHITECTURAL SYSTEM OVERVIEW (B2B MARKETPLACE)            │
│                                                                             │
│  [ Supplier Web Portal (Next.js) ]    [ Buyer Mobile App (Flutter) ]        │
│  [ Admin Dashboard (React) ]          [ Logistics Web (React) ]             │
│                                  │                                          │
│                                  ▼                                          │
│                         ┌──────────────────┐                                │
│                         │   API Gateway    │ (Authentication & Rate Limits) │
│                         └────────┬─────────┘                                │
│                                  │                                          │
│       ┌──────────────────────────┼──────────────────────────┐               │
│       ▼                          ▼                          ▼               │
│  ┌──────────────┐         ┌──────────────┐         ┌──────────────┐         │
│  │ Catalog &    │         │ Order &      │         │ Credit &     │         │
│  │ Search Micro │         │ Fulfillment  │         │ Pricing Engine│        │
│  └──────┬───────┘         └──────┬───────┘         └──────┬───────┘         │
│         │                        │                        │                 │
│         ▼                        ▼                        ▼                 │
│  ┌──────────────┐         ┌──────────────┐         ┌──────────────┐         │
│  │ OCR Document │         │ AI Predictive│         │ RAG Assistant│         │
│  │ Service      │         │ ML Service   │         │ Engine       │         │
│  └──────┬───────┘         └──────┬───────┘         └──────┬───────┘         │
│         │                        │                        │                 │
│         └────────────────────────┼────────────────────────┘                 │
│                                  ▼                                          │
│                    ┌────────────────────────────┐                           │
│                    │ PostgreSQL + pgvector      │                           │
│                    │ MinIO (Document Storage)   │                           │
│                    └────────────────────────────┘                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 1.3.6 Phân Công Nhiệm Vụ Team 4 Người

| Vai Trò | Thành Viên | Trách Nhiệm Chi Tiết |
|---|---|---|
| **Backend & System Lead** | **Sinh viên 1** | Xây dựng Kiến trúc Microservices, Database Schema cho B2B Marketplace. Xây dựng Order Engine, Credit Limit Management, Workflow đối soát thanh toán. Triển khai Docker, CI/CD pipeline, bảo mật hệ thống (RBAC, SQL Injection protection). |
| **Frontend & UI/UX Lead** | **Sinh viên 2** | Thiết kế và lập trình Web Portal cho Supplier (Quản lý catalog, cấu hình giá sỉ, duyệt đơn). Phát triển Admin Dashboard cho Sàn (Duyệt hồ sơ, xem báo cáo GMV toàn sàn). Xây dựng giao diện hiển thị biểu đồ phân tích và Báo cáo tuổi nợ. |
| **AI & Data Scientist** | **Sinh viên 3** | Huấn luyện mô hình AI Credit Scoring (Chấm điểm tín dụng đại lý). Xây dựng mô hình Dynamic Pricing và Demand Forecasting. Xây dựng OCR Pipeline đọc hóa đơn tài chính và RAG Assistant Text-to-SQL. |
| **Full-Stack & Mobile Lead** | **Sinh viên 4** | Lập trình Mobile App dành cho Buyer/Đại lý (Tìm kiếm sản phẩm, đặt đơn sỉ, Re-order 1-click). Tích hợp Semantic Search (Vector Search) vào ô tìm kiếm sản phẩm. Xây dựng Module Tracking vận chuyển và kết nối API đơn vị giao hàng. |

---

## 1.4 TỔNG KẾT VÀ ĐỀ XUẤT LỰA CHỌN

> 💡 **LỜI KHUYÊN CHO TEAM:**
> 
> 1. **Nếu team muốn chọn giải pháp AN TOÀN, DỄ DEMO VÀ TRỰC QUAN NHẤT:** 
>    👉 Chọn **IDEA 1 (Nền Tảng F&B Thông Minh)**. Hội đồng sẽ bị thuyết phục ngay khi xem Demo luồng tương tác thực tế giữa Tablet POS, Màn hình Bếp KDS, Chatbot Zalo đặt bàn và AI dự báo nguyên liệu.
> 
> 2. **Nếu team muốn chọn giải pháp CHUYÊN SÂU DOANH NGHIỆP (ENTERPRISE SCORE):**
>    👉 Chọn **IDEA 2 (Sàn B2B Wholesale Marketplace)**. Đề tài này thể hiện tư duy kiến trúc hệ thống cực kỳ vững chắc với các bài toán khó về Công nợ, Credit Scoring AI, Dynamic Pricing và OCR hóa đơn.

---
---

# ═══════════════════════════════════════════════════════
# CHƯƠNG 2: DEEP RESEARCH — F&B / CHUỖI CÀ PHÊ + AI + IoT — CÓ GÌ MỚI LẠ?
# ═══════════════════════════════════════════════════════

> *Nguồn gốc: F&B_TLBS2.md*
>
> **Mục tiêu:** Đào sâu vào lĩnh vực quản lý chuỗi cà phê / F&B, tìm ra các công nghệ AI + IoT **mới lạ, ít ai làm** có thể áp dụng vào đồ án, tạo lợi thế vượt trội so với các phần mềm POS hiện có tại Việt Nam.

---

## 2.1 🇻🇳 BỐI CẢNH THỊ TRƯỜNG CHUỖI CÀ PHÊ VN 2025

### Cuộc chiến hiện tại:
| Thương hiệu | Số cửa hàng (2025) | Chiến lược | Điểm yếu công nghệ |
|---|---|---|---|
| **Highlands Coffee** | ~1,000 | Giữ vị trí dẫn đầu, đầu tư nhà máy rang xay 500 tỷ | POS cơ bản, chưa có AI dự báo |
| **Phúc Long** | Tăng 50% (nhờ WinMart) | Mô hình kiosk + takeaway trong siêu thị | Chưa có IoT giám sát chất lượng pha chế |
| **The Coffee House** | Thu hẹp, tái cấu trúc | Tối ưu hiệu quả từng cửa hàng | App mạnh nhưng thiếu AI analytics |

### 5 thách thức "chí mạng" mà CHƯA AI nào giải quyết triệt để:

| # | Thách Thức | Mô Tả | Giải Pháp Tiềm Năng |
|---|---|---|---|
| 1 | **Chất lượng không đồng nhất** | Ly cà phê ở Q1 khác ly ở Q9 — phụ thuộc tay nghề barista | 🤖 IoT giám sát máy pha + AI kiểm soát thông số pha chế |
| 2 | **Thất thoát nguyên liệu 5-15%** | Không biết chính xác bao nhiêu cà phê/sữa/syrup được dùng vs lãng phí | 🤖 IoT cân điện tử tự động + AI so sánh BOM vs thực tế |
| 3 | **Xếp ca không tối ưu** | Đông khách nhưng thiếu người, vắng khách nhưng thừa người | 🤖 CV đếm khách + AI dự báo lưu lượng theo giờ |
| 4 | **Thiết bị hỏng bất ngờ** | Máy pha cà phê, tủ lạnh hỏng vào giờ cao điểm → mất doanh thu | 🤖 IoT giám sát thiết bị + AI predictive maintenance |
| 5 | **Chi phí điện năng cao** | Chuỗi 50 cửa hàng, mỗi cửa hàng 15-20 triệu/tháng tiền điện | 🤖 IoT smart meter + AI tối ưu năng lượng |

---

## 2.2 🆕 6 ĐIỂM MỚI LẠ — AI + IoT CÓ THỂ ÁP DỤNG

### 🔥 Điểm mới 1: Computer Vision Đếm Khách & Heatmap Cửa Hàng

**Mô tả:** Dùng camera AI (Raspberry Pi + Camera Module) tại lối vào để **đếm số khách ra/vào theo thời gian thực**, tạo **heatmap lưu lượng** theo giờ trong ngày. Dữ liệu này feed vào model AI để dự báo lượng khách cho ngày mai / tuần sau.

**Tại sao mới lạ?**
- iPOS, CukCuk **KHÔNG có** tính năng này.
- Kết hợp **CV (Computer Vision) + Time-series AI** → chưa có đồ án nào ở VN làm cho F&B.

**Phần cứng IoT cần:**
| Thiết bị | Giá ước tính | Vai trò |
|---|---|---|
| Raspberry Pi 5 | ~2,000,000 VNĐ | Edge computing — chạy model YOLOv8-Nano |
| Camera Module v3 | ~500,000 VNĐ | Ghi hình lối vào |
| ESP32 | ~150,000 VNĐ | Truyền data đếm khách về server qua MQTT |

**AI kỹ thuật:**
- **YOLOv8-Nano** (quantized INT8) chạy trên Raspberry Pi → detect & count người.
- **Prophet / LSTM** dự báo lưu lượng khách 7 ngày tới dựa trên pattern lịch sử, thời tiết, ngày lễ.
- Kết quả: "**Thứ 7 tuần này dự kiến 350 lượt khách (tăng 25% so với thứ 7 tuần trước). Đề xuất: bổ sung 2 nhân viên ca chiều.**"

---

### 🔥 Điểm mới 2: IoT Giám Sát Máy Pha Cà Phê — "Digital Twin" Thiết Bị

**Mô tả:** Gắn sensor vào máy pha espresso để **giám sát real-time** các thông số pha chế: nhiệt độ nước, áp suất bơm, thời gian chiết xuất (shot time), số lượng shot/ngày. Dữ liệu được gửi lên cloud → AI phát hiện bất thường → cảnh báo trước khi máy hỏng.

**Tại sao mới lạ?**
- Đây là concept **"Digital Twin"** cho thiết bị F&B — cực kỳ hot trong Industry 4.0 nhưng **chưa ai áp dụng cho chuỗi cà phê tại VN**.
- Giải quyết bài toán #1 (chất lượng đồng nhất) + #4 (hỏng bất ngờ).

**Phần cứng IoT cần:**
| Thiết bị | Giá ước tính | Vai trò |
|---|---|---|
| DS18B20 (Waterproof Temp Sensor) | ~30,000 VNĐ | Đo nhiệt độ nước pha |
| Pressure Transducer (0-12 Bar) | ~200,000 VNĐ | Đo áp suất bơm |
| Hall-Effect Flow Sensor | ~80,000 VNĐ | Đo lưu lượng nước (ml/shot) |
| ESP32 | ~150,000 VNĐ | Thu thập data sensor, gửi qua MQTT |
| MAX31855 (Thermocouple Amp) | ~50,000 VNĐ | Khuếch đại tín hiệu nhiệt độ chính xác |

**AI kỹ thuật:**
- **Anomaly Detection (Isolation Forest / Autoencoder):** Phát hiện khi thông số pha chế lệch khỏi baseline (VD: áp suất giảm dần → pump sắp hỏng).
- **Predictive Maintenance (XGBoost):** Dự đoán thời điểm cần bảo trì dựa trên pattern sử dụng + tuổi thiết bị.
- **Quality Scoring:** Mỗi shot espresso được chấm điểm chất lượng dựa trên combo (nhiệt độ + áp suất + thời gian + lưu lượng). Nếu score < threshold → alert barista.
- Kết quả: "**Máy pha #3 tại chi nhánh Nguyễn Huệ: áp suất giảm 15% trong 3 ngày qua. Dự báo: cần thay seal bơm trong 5 ngày tới. ⚠️**"

---

### 🔥 Điểm mới 3: Digital Menu Động — Thay Đổi Theo Ngữ Cảnh

**Mô tả:** Thay bảng menu giấy bằng **màn hình digital** hiển thị menu thay đổi theo:
- **Thời gian trong ngày:** Sáng = Combo breakfast + cà phê, Chiều = Trà sữa + bánh ngọt, Tối = Mocktail.
- **Thời tiết:** Nắng nóng → đẩy đồ uống đá lên đầu. Mưa lạnh → đẩy cappuccino nóng.
- **Tồn kho real-time:** Hết syrup caramel → tự ẩn tất cả món có caramel.
- **Khách hàng (nếu có loyalty):** KH VIP scan QR → menu hiện "Món yêu thích của bạn".

**Tại sao mới lạ?**
- Concept **"Context-Aware Dynamic Menu"** kết hợp IoT (sensor thời tiết, tồn kho) + AI (recommendation) → **chưa có chuỗi CF VN nào có**.
- Demo trước hội đồng sẽ cực ấn tượng.

**Phần cứng IoT:**
| Thiết bị | Giá ước tính | Vai trò |
|---|---|---|
| Màn hình LED/LCD 32-43 inch | ~3,000,000 VNĐ | Hiển thị menu |
| Raspberry Pi 5 | ~2,000,000 VNĐ | Chạy ứng dụng menu + kết nối cloud |
| BME280 Sensor | ~50,000 VNĐ | Đo nhiệt độ, độ ẩm, áp suất không khí |

**AI kỹ thuật:**
- **Context Engine (Rule-based + ML):** Kết hợp thời gian + thời tiết + tồn kho + profile KH → quyết định menu items nào hiển thị.
- **Upsell Recommendation (Collaborative Filtering):** Gợi ý topping/combo dựa trên món KH vừa chọn.

---

### 🔥 Điểm mới 4: IoT Giám Sát Chuỗi Lạnh & Kho Nguyên Liệu

**Mô tả:** Gắn sensor nhiệt độ + độ ẩm vào **tủ lạnh, kho nguyên liệu** tại mỗi cửa hàng. Hệ thống giám sát 24/7, cảnh báo khi:
- Tủ lạnh nhiệt độ vượt ngưỡng an toàn (nguy cơ hỏng sữa, kem).
- Cửa tủ mở quá lâu (nhân viên quên đóng).
- Dự báo nguyên liệu sắp hết dựa trên tốc độ tiêu thụ + tồn kho hiện tại.

**Tại sao mới lạ?**
- Giải quyết **Food Safety** (HACCP compliance) — rất quan trọng cho chuỗi F&B.
- Kết hợp IoT monitoring + AI prediction cho kho.

**Phần cứng IoT:**
| Thiết bị | Giá ước tính | Vai trò |
|---|---|---|
| DHT22 / SHT31 | ~50,000 VNĐ | Đo nhiệt độ + độ ẩm kho/tủ lạnh |
| Cảm biến cửa (Magnetic Reed Switch) | ~20,000 VNĐ | Phát hiện cửa tủ mở/đóng |
| Load Cell + HX711 | ~100,000 VNĐ | Cân tự động nguyên liệu (kg sữa, cà phê) |
| ESP32 | ~150,000 VNĐ | Gom data sensor, gửi MQTT |

**AI kỹ thuật:**
- **Anomaly Alert:** Nhiệt độ > 8°C trong 15 phút liên tục → SMS/Zalo alert cho Manager.
- **AI Inventory Prediction:** Kết hợp data cân tự động (Load Cell) + doanh số bán → dự báo khi nào hết nguyên liệu X.

---

### 🔥 Điểm mới 5: Smart Energy Management — Tiết Kiệm Điện AI

**Mô tả:** Giám sát và tối ưu hóa **tiêu thụ điện năng** của từng cửa hàng trong chuỗi. IoT đo điện năng từng thiết bị (máy pha, tủ lạnh, điều hòa, đèn). AI phân tích pattern → đề xuất tiết kiệm.

**Tại sao mới lạ?**
- Chi phí điện chiếm **15-25% chi phí vận hành** quán CF → tiết kiệm 15-20% = ROI cực rõ.
- Kết hợp với CV đếm khách: "**Không có khách từ 14h-15h → tự giảm công suất điều hòa 30%.**"

**Phần cứng IoT:**
| Thiết bị | Giá ước tính | Vai trò |
|---|---|---|
| PZEM-004T (Energy Meter) | ~150,000 VNĐ | Đo điện năng tiêu thụ (Voltage, Current, Power, kWh) |
| CT Clamp (SCT-013) | ~50,000 VNĐ | Đo dòng điện không xâm lấn |
| Smart Relay (Sonoff/Tuya) | ~200,000 VNĐ | Bật/tắt thiết bị từ xa |
| ESP32 | ~150,000 VNĐ | Gom data điện, gửi MQTT |

**AI kỹ thuật:**
- **Energy Profiling:** Phân tích pattern tiêu thụ điện từng thiết bị → tìm "energy vampire" (thiết bị ngốn điện bất thường).
- **Occupancy-Based Optimization:** Kết hợp data đếm khách (CV) + điện → tự động điều chỉnh điều hòa, đèn theo lượng khách thực tế.

---

### 🔥 Điểm mới 6: AI Chatbot "Barista Ảo" — Order Bằng Giọng Nói

**Mô tả:** Nâng cấp chatbot từ text-only thành **voice-enabled AI barista** trên Zalo/App. Khách hàng nói: *"Cho tôi một ly Americano đá, ít đường, thêm shot espresso"* → AI hiểu → tạo order → gửi vào hệ thống POS.

**AI kỹ thuật:**
- **Speech-to-Text:** Whisper (OpenAI) hoặc Google STT cho tiếng Việt.
- **NLU (Natural Language Understanding):** LLM (Gemini/GPT) extract entities: Tên món = Americano, Nhiệt độ = Đá, Đường = Ít, Extra = Thêm 1 shot.
- **RAG:** Tra cứu menu hiện tại để validate món có tồn tại không, giá bao nhiêu.

---

## 2.3 📊 BẢNG TỔNG HỢP: TRƯỚC vs SAU KHI THÊM AI + IoT

| Khía cạnh | Idea 1 GỐC (chỉ phần mềm) | Idea 1 NÂNG CẤP (AI + IoT) | Điểm khác biệt |
|---|---|---|---|
| **Đếm khách** | ❌ Không có | ✅ Camera CV + heatmap + forecast | Hoàn toàn mới |
| **Kiểm soát chất lượng pha chế** | ❌ Phụ thuộc barista | ✅ IoT sensor trên máy pha + Quality Score mỗi shot | Hoàn toàn mới |
| **Giám sát kho lạnh** | ❌ Kiểm tra thủ công | ✅ IoT 24/7 + alert tự động | Hoàn toàn mới |
| **Tiết kiệm điện** | ❌ Không có | ✅ Smart meter + AI optimization | Hoàn toàn mới |
| **Menu** | Tĩnh (CRUD cơ bản) | ✅ Dynamic menu theo ngữ cảnh (thời tiết, tồn kho, KH) | Nâng cấp lớn |
| **Dự báo nguyên liệu** | ✅ Có (từ data bán hàng) | ✅ Có + bổ sung data từ Load Cell IoT (chính xác hơn) | Bổ sung IoT |
| **Chatbot** | ✅ Text-based | ✅ Voice + Text + context-aware | Nâng cấp |
| **Bảo trì thiết bị** | ❌ Sửa khi hỏng | ✅ Predictive maintenance từ IoT sensor | Hoàn toàn mới |
| **Xếp ca** | ✅ Từ data bán hàng | ✅ Từ data CV đếm khách (chính xác hơn) | Bổ sung IoT |

---

## 2.4 🏗️ ĐỀ XUẤT MODULE MỚI CHO IDEA 1 (PHIÊN BẢN AI + IoT)

### Danh sách 10 Module (nâng cấp từ 8 lên 10):

| # | Module | Loại | Mô tả ngắn |
|---|---|---|---|
| 1 | 🛒 POS & Order | Phần mềm | Quản lý bán hàng, thanh toán, KDS |
| 2 | 📦 Kho & BOM | Phần mềm + IoT | Tự động trừ kho + Load Cell IoT cân nguyên liệu |
| 3 | 📋 Menu | Phần mềm + IoT | Dynamic Menu theo ngữ cảnh (thời tiết sensor, tồn kho, KH) |
| 4 | 👥 CRM & Loyalty | Phần mềm | Tích điểm, phân nhóm KH, churn prediction |
| 5 | 📊 Analytics & Forecast | Phần mềm + AI | Dashboard + AI dự báo doanh thu, nguyên liệu, lượng khách |
| 6 | 🤖 AI Chatbot | Phần mềm + AI | Đặt bàn, đặt món qua Zalo (text + voice) |
| 7 | 👨‍💼 HRM & Ca | Phần mềm + AI | Xếp ca tự động dựa trên AI dự báo lượng khách |
| 8 | 🧾 Tài Chính | Phần mềm | Hóa đơn điện tử, báo cáo thu chi |
| 9 | **📷 IoT Footfall & Heatmap** | **IoT + AI (MỚI)** | **Camera đếm khách + heatmap + dự báo lưu lượng** |
| 10 | **☕ IoT Equipment Monitor** | **IoT + AI (MỚI)** | **Giám sát máy pha CF, tủ lạnh, điện năng + predictive maintenance** |

---

## 2.5 📐 KIẾN TRÚC TỔNG THỂ SAU NÂNG CẤP

```
┌─────────────────────────────────────────────────────────────────────────┐
│          SMART F&B CHAIN OPERATING SYSTEM (AI + IoT Edition)           │
│                                                                         │
│  ┌─────────────────────── CLOUD LAYER ───────────────────────────┐     │
│  │                                                                │     │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │     │
│  │  │ Web App  │  │ Tablet   │  │ Mobile   │  │ Zalo OA  │      │     │
│  │  │ Admin    │  │ POS      │  │ App KH   │  │ Chatbot  │      │     │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘      │     │
│  │       └──────────────┴────────────┴──────────────┘             │     │
│  │                          │                                     │     │
│  │                   ┌──────▼──────┐                              │     │
│  │                   │ API Gateway │                              │     │
│  │                   └──────┬──────┘                              │     │
│  │                          │                                     │     │
│  │   ┌──────────────────────┼─────────────────────────┐          │     │
│  │   │                      │                         │          │     │
│  │   ▼                      ▼                         ▼          │     │
│  │ ┌────────┐  ┌──────────────────┐  ┌──────────────────┐       │     │
│  │ │Business│  │   AI/ML Engine   │  │  IoT Data Engine │       │     │
│  │ │Services│  │                  │  │                  │       │     │
│  │ │        │  │ • Demand Forecast│  │ • MQTT Broker    │       │     │
│  │ │• Order │  │ • Churn Predict  │  │ • Sensor Data    │       │     │
│  │ │• Inv.  │  │ • Recommendation│  │   Aggregation    │       │     │
│  │ │• HRM   │  │ • Anomaly Detect│  │ • Alert Engine   │       │     │
│  │ │• CRM   │  │ • CV Processing │  │                  │       │     │
│  │ └────────┘  └──────────────────┘  └──────────────────┘       │     │
│  │                          │                                     │     │
│  │               ┌──────────▼──────────┐                         │     │
│  │               │ PostgreSQL+pgvector │                         │     │
│  │               │ InfluxDB (IoT TS)   │                         │     │
│  │               │ Redis (Realtime)    │                         │     │
│  │               └─────────────────────┘                         │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                                                                         │
│  ┌─────────────────── EDGE LAYER (Mỗi cửa hàng) ────────────────┐     │
│  │                                                                │     │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │     │
│  │  │ 📷 Raspberry Pi │  │ ☕ ESP32 Node 1 │  │ 🌡️ ESP32 Node 2│   │     │
│  │  │ + Camera       │  │ (Máy pha CF)   │  │ (Kho lạnh)     │   │     │
│  │  │                │  │                │  │                │   │     │
│  │  │ • YOLOv8-Nano  │  │ • Temp sensor  │  │ • DHT22 sensor │   │     │
│  │  │ • People Count │  │ • Pressure     │  │ • Door sensor  │   │     │
│  │  │ • Heatmap      │  │ • Flow sensor  │  │ • Load Cell    │   │     │
│  │  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘   │     │
│  │          │                   │                   │            │     │
│  │          └───────────────────┴───────────────────┘            │     │
│  │                              │                                │     │
│  │                       MQTT / Wi-Fi                            │     │
│  │                              │                                │     │
│  │                     ┌────────▼────────┐                       │     │
│  │                     │  Edge Gateway   │                       │     │
│  │                     │  (Local MQTT    │                       │     │
│  │                     │   Broker)       │                       │     │
│  │                     └────────┬────────┘                       │     │
│  │                              │                                │     │
│  └──────────────────────────────┼────────────────────────────────┘     │
│                                 │                                       │
│                          ☁️ Internet                                    │
│                                 │                                       │
│                          ┌──────▼──────┐                               │
│                          │ Cloud Server │                               │
│                          └─────────────┘                               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2.6 💡 TẠI SAO ĐỀ TÀI NÀY "KHÁC BIỆT" SO VỚI CÁC ĐỒ ÁN KHÁC?

| Điểm so sánh | Đồ án POS thông thường | Đồ án của bạn (AI + IoT) |
|---|---|---|
| **Phạm vi** | Chỉ phần mềm (web/mobile) | Phần mềm + Phần cứng IoT + AI |
| **Dữ liệu** | Chỉ từ input thủ công (nhập tay) | Tự động thu thập từ sensor 24/7 |
| **Dự báo** | Không có hoặc rất cơ bản | AI dự báo đa chiều (khách, nguyên liệu, thiết bị, điện) |
| **Demo** | Click trên web | Demo thật: camera đếm khách, sensor đo nhiệt độ máy pha, digital menu đổi theo thời tiết |
| **Tính mới** | Rất nhiều đồ án POS giống nhau | **Chưa có đồ án nào** kết hợp CV đếm khách + IoT máy pha CF + Dynamic Menu + Predictive Maintenance |
| **WOW factor** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Phù hợp ngành SE** | ✅ Phần mềm | ✅✅✅ Phần mềm + IoT + AI = Full-stack đúng nghĩa |

---

## 2.7 📌 PHÂN CÔNG GỢI Ý CHO TEAM 4 NGƯỜI (AI + IoT Edition)

| Vai Trò | Phụ Trách | Chi Tiết |
|---|---|---|
| **Backend & IoT Lead** | SV 1 | API Gateway, Microservices, **MQTT Broker**, **InfluxDB** cho IoT data, WebSocket realtime |
| **Frontend Lead** | SV 2 | Web Dashboard (React), POS Tablet, **Digital Menu UI động**, KDS Bếp |
| **AI & CV Engineer** | SV 3 | **YOLOv8 đếm khách trên Raspberry Pi**, AI Forecast, Churn, Recommendation, Chatbot RAG |
| **IoT & Full-stack** | SV 4 | **Lập trình ESP32** (sensor máy pha, kho lạnh, điện), Mobile App KH, Module Kho+BOM |

---

## 2.8 ⚡ TỔNG KẾT CHƯƠNG 2

> **Đề tài nâng cấp:** *"Nền Tảng Quản Lý Chuỗi Cà Phê / F&B Thông Minh Ứng Dụng Trí Tuệ Nhân Tạo và Internet Vạn Vật"*
>
> **Tên tiếng Anh:** *"AI & IoT-Powered Smart Coffee Chain Operating System"*

**10 Module** | **5 Actor** | **6 AI Feature** | **4 IoT Node** | **1 Edge Device (Raspberry Pi)**

Điểm vượt trội:
1. **IoT thật** — không phải giả lập, có sensor, có Raspberry Pi, có ESP32.
2. **AI thật** — Computer Vision chạy edge, ML dự báo, NLP chatbot.
3. **Full-scale platform** — 10 module, đủ quản lý toàn bộ chuỗi.
4. **Demo WOW** — Hội đồng nhìn thấy camera đếm khách live, sensor đo máy pha live, menu tự thay đổi.
5. **Thị trường thật** — Giải quyết pain-point CỤ THỂ của Highlands, Phúc Long, The Coffee House.

---
---

# ═══════════════════════════════════════════════════════
# CHƯƠNG 3: 3 ĐỀ TÀI FULL-SCALE — SO SÁNH & KHUYẾN NGHỊ
# ═══════════════════════════════════════════════════════

> *Nguồn gốc: F&B_TLBS3.md*
>
> **Yêu cầu:** Scope ở mức **1 sản phẩm thực sự** — nhiều module, nhiều vai trò (actor), đủ "nặng" cho 4 SE cả học kỳ.
> Không phải 1 feature nhỏ, mà là **1 hệ thống vận hành doanh nghiệp**.

---

## 3.1 📊 Tổng Quan 3 Đề Tài Full-Scale

| # | Tên Nền Tảng | Ngành | Số Module | Số Actor | AI Features |
|---|---|---|:---:|:---:|:---:|
| **A** | Nền Tảng Quản Lý F&B Thông Minh | Nhà hàng / Quán cà phê | **8** | **5** | **6** |
| **B** | Sàn Thương Mại B2B Thông Minh | Phân phối / Bán sỉ | **7** | **4** | **5** |
| **C** | Nền Tảng Quản Lý Phòng Khám Thông Minh | Y tế / Phòng khám tư | **7** | **5** | **6** |

---

## 3.2 🍜 IDEA A: Nền Tảng Quản Lý F&B Thông Minh

*(Chi tiết đã trình bày đầy đủ tại Chương 1 mục 1.2 — ở đây chỉ tóm tắt module + AI)*

### Actors: Admin, Manager, Staff, Kitchen, Customer (5 vai trò)

### 8 Module:
| # | Module | Highlight |
|---|---|---|
| 1 | 🛒 POS — Bán Hàng | Order, chia/gộp bill, thanh toán VietQR/MoMo, KDS |
| 2 | 📦 Kho — Nguyên Liệu | Xuất kho quầy theo Kg/Hộp/Chai, kiểm kê, 🤖 AI đề xuất nhập hàng |
| 3 | 📋 Menu — Thực Đơn | Giá đa chi nhánh, 🤖 AI gợi ý combo |
| 4 | 👥 CRM & Loyalty | Tích điểm, 🤖 AI Churn Prediction |
| 5 | 📊 Analytics & AI Forecast | Dashboard, 🤖 AI dự báo doanh thu + nguyên liệu |
| 6 | 🤖 AI Chatbot | Đặt bàn/đặt món Zalo, 🤖 NLP tiếng Việt |
| 7 | 👨‍💼 HRM | Xếp ca, chấm công, 🤖 AI đề xuất ca |
| 8 | 🧾 Tài Chính | HĐĐT, báo cáo thuế |

### 6 AI Features:
| # | AI Feature | Kỹ Thuật |
|---|---|---|
| 1 | Dự báo doanh thu | Prophet / LSTM time-series |
| 2 | Dự báo nhu cầu nguyên liệu | XGBoost + time-series |
| 3 | Gợi ý combo bán chạy | Association Rules (Apriori) / Collaborative Filtering |
| 4 | Dự đoán churn khách hàng | Random Forest / XGBoost classification |
| 5 | Chatbot NLP tiếng Việt | RAG (LLM + Vector DB) + PhoBERT intent detection |
| 6 | Đề xuất ca làm việc | Optimization (demand forecast → staff scheduling) |

---

## 3.3 🏭 IDEA B: Sàn Thương Mại B2B Thông Minh

*(Chi tiết đã trình bày đầy đủ tại Chương 1 mục 1.3 — ở đây chỉ tóm tắt module + AI)*

### Actors: Platform Admin, Supplier, Buyer, Logistics Partner (4 vai trò)

### 7 Module:
| # | Module | Highlight |
|---|---|---|
| 1 | 🏪 Marketplace | Catalog, semantic search, so sánh giá, 🤖 AI Recommendation |
| 2 | 📋 Order Management | Giỏ hàng B2B, workflow đơn sỉ, Re-order 1-click, 🤖 AI Demand Forecast |
| 3 | 💰 Pricing & Credit | Tiered pricing, 🤖 AI Dynamic Pricing, 🤖 AI Credit Scoring, aging report |
| 4 | 🚚 Logistics | GHN/GHTK integration, 🤖 AI Route Optimization |
| 5 | 📄 AI Document OCR | 🤖 OCR hóa đơn, đối soát 3 bên |
| 6 | 📊 Analytics | Dashboard Supplier/Buyer/Admin, 🤖 AI Insight |
| 7 | 💬 AI Assistant | 🤖 RAG + LLM tra cứu dữ liệu |

### 6 AI Features:
| # | AI Feature | Kỹ Thuật |
|---|---|---|
| 1 | Product Recommendation cho Buyer | Collaborative Filtering + Content-Based |
| 2 | Demand Forecasting | Prophet / XGBoost time-series |
| 3 | Dynamic Pricing | Reinforcement Learning / Rule-based + ML |
| 4 | Credit Scoring đại lý | XGBoost / Logistic Regression |
| 5 | OCR Invoice Processing | PaddleOCR + LLM extraction |
| 6 | NL Query Assistant | RAG (LLM + pgvector) |

---

## 3.4 🏥 IDEA C: Nền Tảng Quản Lý Phòng Khám Thông Minh (AI-Powered Clinic Management)

### Tổng Quan Sản Phẩm
**Hệ thống quản lý vận hành hoàn chỉnh** cho phòng khám tư nhân (đa khoa, nha khoa, da liễu, nhi...), tích hợp:
- Hồ sơ bệnh nhân điện tử (EMR)
- Đặt lịch khám online + AI tối ưu lịch
- Chatbot tư vấn triệu chứng sơ bộ
- AI hỗ trợ chẩn đoán (gợi ý ICD-10 code)
- Quản lý dược / vật tư
- Thanh toán + BHYT
- Dashboard phân tích hiệu quả phòng khám

**Thực tế VN:** Hàng nghìn phòng khám tư nhân vẫn dùng sổ tay + Excel. Nhu cầu số hóa **cực lớn**.

### Actors:

| Actor | Mô tả | Chức năng chính |
|---|---|---|
| 🔴 **Admin (Chủ phòng khám)** | Quản trị hệ thống | Quản lý BS/NV, tài chính, báo cáo, cấu hình |
| 🟠 **Doctor (Bác sĩ)** | Khám & chẩn đoán | Xem hồ sơ BN, ghi chẩn đoán, kê đơn, xem lịch sử |
| 🟢 **Receptionist (Lễ tân)** | Tiếp nhận & thanh toán | Đăng ký khám, xếp hàng, thu phí, BHYT |
| 🔵 **Pharmacist (Dược sĩ)** | Cấp thuốc | Nhận đơn, kiểm tra tồn kho, phát thuốc, cảnh báo tương tác |
| 🟣 **Patient (Bệnh nhân)** | Khám & theo dõi | App: đặt lịch, xem kết quả, hỏi chatbot, nhận đơn thuốc |

### 7 Module:

#### Module 1: 📋 EMR — Hồ Sơ Bệnh Nhân Điện Tử
- Hồ sơ bệnh nhân (thông tin cá nhân, tiền sử bệnh, dị ứng)
- Lịch sử khám (mỗi lần khám = 1 record: triệu chứng, chẩn đoán, đơn thuốc)
- Upload kết quả xét nghiệm / hình ảnh (X-ray, siêu âm)
- 🤖 **AI Auto-Summary:** Tóm tắt lịch sử khám dài thành 1 đoạn ngắn cho bác sĩ đọc nhanh
- Timeline view: xem toàn bộ hành trình sức khỏe bệnh nhân

#### Module 2: 📅 Appointment — Đặt Lịch Khám
- Bệnh nhân đặt lịch online (web/app)
- Chọn bác sĩ, chuyên khoa, khung giờ
- 🤖 **AI Smart Scheduling:** Tối ưu lịch khám dựa trên: thời gian khám TB của từng BS, dự đoán no-show, ưu tiên ca cấp cứu
- Gửi nhắc nhở SMS/Zalo trước 24h
- Quản lý hàng đợi (queue) real-time tại phòng khám
- 🤖 **AI No-Show Prediction:** Dự đoán BN nào có khả năng vắng → gửi reminder/đặt slot dự phòng

#### Module 3: 🤖 Patient Chatbot — Trợ Lý Sức Khỏe
- Chatbot trên app/Zalo: BN mô tả triệu chứng → AI gợi ý khoa nên khám
- "Tôi bị đau đầu, sốt, ho 3 ngày" → "Bạn nên khám Nội tổng quát. Đặt lịch ngay?"
- Hỏi đáp về dịch vụ phòng khám (giá, giờ làm, BHYT)
- Nhắc uống thuốc (theo đơn đã kê)
- 🤖 **NLP + Medical Knowledge Base (RAG):** Trả lời chính xác, KHÔNG bịa thông tin y tế
- ⚠️ **Disclaimer:** "Đây là gợi ý sơ bộ, không thay thế khám bác sĩ"

#### Module 4: 🩺 Clinical Decision Support — Hỗ Trợ Chẩn Đoán
- 🤖 **AI gợi ý ICD-10:** BS nhập triệu chứng → AI suggest mã bệnh ICD-10 phù hợp
- 🤖 **Drug Interaction Check:** Kiểm tra tương tác thuốc khi BS kê đơn (VD: thuốc A + thuốc B = nguy hiểm)
- Gợi ý xét nghiệm cần làm dựa trên triệu chứng
- Template đơn thuốc theo chuyên khoa
- 🤖 **AI Allergy Alert:** Cảnh báo nếu thuốc kê trùng với dị ứng trong hồ sơ BN

#### Module 5: 💊 Pharmacy — Quản Lý Dược / Vật Tư
- Quản lý tồn kho thuốc (lot, hạn sử dụng, số lô)
- Cảnh báo thuốc sắp hết hạn
- Nhận đơn từ BS → phát thuốc → trừ kho
- Quản lý nhập thuốc từ nhà cung cấp
- 🤖 **AI dự báo nhu cầu thuốc:** Dựa trên xu hướng khám → dự đoán thuốc nào cần nhập thêm

#### Module 6: 💰 Billing & Insurance — Thanh Toán & BHYT
- Tính phí khám (khám + xét nghiệm + thuốc + thủ thuật)
- Tra cứu BHYT (API cổng BHYT VN)
- Tính phần BHYT chi trả vs bệnh nhân tự trả
- In phiếu thu, xuất hóa đơn điện tử
- Quản lý doanh thu / công nợ

#### Module 7: 📊 Analytics — Phân Tích Hiệu Quả Phòng Khám
- Dashboard: số lượt khám/ngày, doanh thu, top chuyên khoa
- Thời gian chờ trung bình, thời gian khám TB
- 🤖 **AI Insight:** "Số lượt khám Nhi tăng 30% trong tháng 7 → có thể do mùa dịch tay chân miệng"
- Báo cáo tài chính: doanh thu - chi phí = lợi nhuận
- Phân tích BS: số BN khám, tỷ lệ hài lòng, thời gian khám TB

### 6 AI Features:

| # | AI Feature | Kỹ Thuật |
|---|---|---|
| 1 | Tóm tắt hồ sơ bệnh nhân | LLM (Gemini/GPT) summarization |
| 2 | Smart Scheduling + No-Show Prediction | XGBoost + Constraint Optimization |
| 3 | Chatbot tư vấn triệu chứng | RAG (LLM + Medical KB) + PhoBERT NER |
| 4 | Gợi ý ICD-10 code | Multi-label classification (BERT fine-tuned) |
| 5 | Drug Interaction + Allergy Check | Knowledge Graph + Rule Engine |
| 6 | Dự báo nhu cầu thuốc | Time-series forecasting (Prophet) |

---

## 3.5 📊 SO SÁNH TỔNG HỢP 3 NỀN TẢNG

| Tiêu chí | A: F&B Platform | B: B2B Marketplace | C: Clinic Management |
|---|:---:|:---:|:---:|
| **Số module** | 8 | 7 | 7 |
| **Số actor** | 5 | 4 | 5 |
| **Số AI feature** | 6 | 6 | 6 |
| **Thị trường VN** | 🔥🔥🔥🔥🔥 | 🔥🔥🔥🔥 | 🔥🔥🔥🔥🔥 |
| **Đối thủ hiện tại** | iPOS, CukCuk (nhưng ít AI) | Rất ít | Rất ít (cơ hội lớn) |
| **Độ khó kỹ thuật** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **WOW demo** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Phù hợp 4 SE** | ✅✅✅ | ✅✅ | ✅✅✅ |
| **Khả năng startup** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Dữ liệu demo** | Dễ tạo mock data | Trung bình | Cần cẩn thận (y tế) |
| **Tích hợp IoT?** | Có thể (sensor nhiệt kho) | Có thể (GPS tracking) | Có thể (IoT y tế) |

---

## 3.6 🏆 Khuyến Nghị

> [!TIP]
> **IDEA A (F&B Platform)** — Nếu muốn đề tài **"gần gũi nhất"** với cuộc sống. Dễ demo (mở quán cà phê giả, gọi món thật). Thị trường VN cực lớn. Đối thủ có nhưng CHƯA có AI. **Đây là lựa chọn an toàn nhất + ấn tượng nhất.**

> [!TIP]
> **IDEA B (B2B Marketplace)** — Nếu muốn đề tài **"enterprise nhất"**, scope lớn nhất, nhiều nghiệp vụ phức tạp (công nợ, credit scoring, logistics). Phù hợp nếu team mạnh backend.

> [!TIP]
> **IDEA C (Clinic Management)** — Nếu muốn đề tài **"có impact xã hội"** + AI sâu (medical NLP, ICD-10, drug interaction). Rất ít đối thủ tại VN. Nhưng cần cẩn thận về dữ liệu y tế giả (đừng dùng data thật).

---

*Tài liệu tổng hợp từ 3 file gốc (F&B_TLBS.md + F&B_TLBS2.md + F&B_TLBS3.md) — lưu trữ tại workspace dự án đồ án tốt nghiệp.*
