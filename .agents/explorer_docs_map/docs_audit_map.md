# 🗺️ BẢN ĐỒ KIỂM TOÁN TÀI LIỆU & BÁO CÁO LỆCH NGHIỆP VỤ (DOCS AUDIT MAP)
## HỆ THỐNG SMART F&B OPERATING SYSTEM (SMART F&B OS)

> **Mã Tài Liệu:** `DOCS_AUDIT_MAP_v2.0`  
> **Người Thực Hiện:** Explorer 2 — Documentation Mapper & Divergence Auditor  
> **Thư Mục Làm Việc:** `d:\Idea_DoAn\.agents\explorer_docs_map\`  
> **Nguồn Sự Thật (Source of Truth):** `Smart_FB_OS_Revised_4members.docx` (Trích xuất: `temp_revised_content.txt`)  
> **Mục Tiêu:** Rà soát toàn bộ 31+ tệp Markdown và các tài liệu phái sinh trong `d:\Idea_DoAn\`, lập bản đồ mâu thuẫn nghiệp vụ chi tiết so với 5 Thay Đổi Nghiệp Vụ Cốt Lõi, xác định rõ các phần cần viết lại, các phần cần chuyển sang "Scale Up / Future Work", và thiết lập mạng lưới phụ thuộc chéo (Cross-file Dependencies).

---

## 📌 PHẦN 1: TỔNG QUAN 5 THAY ĐỔI NGHIỆP VỤ CỐT LÕI (5 CORE BUSINESS CHANGES)

Toàn bộ hệ thống tài liệu bắt buộc phải đồng bộ 100% theo 5 thay đổi nghiệp vụ nền tảng dưới đây:

| STT | Thay Đổi Nghiệp Vụ | Luồng CŨ (Lỗi Thời / Cần Xóa Bỏ) | Luồng MỚI (Chuẩn Nghiệp Vụ Chính Thức) | Tác Động Hệ Thống & Dữ Liệu |
|:---:|---|---|---|---|
| **1** | **Dine-in: Thanh toán TRƯỚC khi bếp nhận đơn** | Khách quét QR → Chọn món → Bếp nhận đơn pha chế → Khách dùng món → Bấm "Yêu cầu bill" → NV mang bill/thu tiền sau. | Khách quét QR bàn → Nhập SĐT (tùy chọn) → Duyệt menu & chọn món → Giỏ hàng → **Thanh toán VietQR** → Xác nhận thành công → **BẾP MỚI NHẬN ĐƠN QUA SIGNALR**. | • Order status flow: `PendingPayment` → `Paid` → `Confirmed` → `Preparing` → `Ready` → `Served/Completed`.<br>• Xóa bỏ hoàn toàn chức năng "Yêu cầu bill" / thanh toán sau cho Dine-in. |
| **2** | **QR Delivery (MỚI HOÀN TOÀN): Đặt hàng tại nhà** | Không có luồng Delivery độc lập; khách chỉ đặt món tại quán hoặc mang đi. | Quét **QR Delivery** (trên poster, fanpage, standee) → Mở PWA → Nhập SĐT + **Địa chỉ giao hàng (Bắt buộc)** → Chọn món → **Thanh toán VietQR trước + Phí ship cố định 20.000 VNĐ** → Đơn vào hệ thống bếp & điều phối. | • Thêm `OrderType` enum: `DineIn`, `TakeAway`, `Delivery`.<br>• Thêm cột DB: `delivery_address` (string), `delivery_fee` (decimal 20k).<br>• Chỉ chấp nhận VietQR (Không COD). |
| **3** | **Takeaway: Giao diện NV thao tác (KHÔNG dùng QR)** | Khách tự quét mã QR Takeaway dán tại quầy/cửa để đặt món trên điện thoại cá nhân. | **Bỏ QR Takeaway cũ** → NV quầy mở **giao diện Takeaway Web POS trên hệ thống** → Tra cứu SĐT khách (nếu mới: nhập tên tạo CRM, nếu cũ: hiện loyalty) → NV chọn món → Tạo đơn → Khách **thanh toán SAU khi nhận món** (Tiền mặt hoặc VietQR). | • Loyalty mới: **Mỗi 10 ly = tặng 1 ly miễn phí** (đơn giản hóa thay cho hệ thống điểm phức tạp).<br>• Thêm trường `CupCount`, `FreeCupCount` trong CRM. |
| **4** | **Chấm công WiFi-locked (Thay GPS 50m & QR động 30s)** | Nhân viên dùng app quét mã QR động đổi mỗi 30 giây trên POS và kích hoạt GPS trong bán kính 50m. | **Bỏ GPS 50m và QR động 30s** → NV kết nối **WiFi của quán** → Vào web hệ thống → Chọn Chấm công → Quét QR chấm công cố định + Nhập Mã NV → Hệ thống kiểm tra: (a) WiFi network (SSID/BSSID/MAC/IP) đúng quán, (b) Mã NV hợp lệ → Ghi nhận vào ca. | • Thêm cấu hình WiFi chi nhánh (`wifi_ssid`, `wifi_bssid`/`mac_address`, `subnet_ip`).<br>• Xóa bỏ các trường kinh độ/vĩ độ GPS trong bảng `Attendances`. |
| **5** | **Xóa bỏ hoàn toàn Staff Mobile App** | Có ứng dụng di động riêng (Flutter/React Native) cho nhân viên phục vụ nhận alert, rung chuông, xuất VietQR. | **Bỏ hoàn toàn Staff Mobile App** → Toàn bộ tính năng (xem sơ đồ bàn, KDS, báo hết món, tạo đơn Takeaway, chấm công) tích hợp trực tiếp vào **giao diện Web Responsive / KDS** trên trình duyệt. | • Loại bỏ Actor/Container/Route Group `(staff)` di động độc lập.<br>• Thống nhất 100% Web Stack: Next.js 14 Responsive. |
| **+** | **Phân Định Phạm Vi AI Modules** | Đưa cả 5 module AI vào cam kết triển khai ngay trong đồ án. | **2 Module triển khai chính thức:**<br>• **AI-1:** Recommendation Chatbot (RAG, nghiên cứu chính kèm bảng đánh giá baselines).<br>• **AI-2:** Combo Suggestion (Apriori / FP-Growth).<br>**3 Module chuyển sang "Scale Up / Future Work":**<br>• **AI-3:** Natural Language Business Analytics (NLQ).<br>• **AI-4:** Churn Prediction (XGBoost/Random Forest).<br>• **AI-5:** Menu Intelligence (Demand Forecasting). | • Giữ vững kiến trúc mở rộng nhưng phân định rõ ràng ranh giới nghiên cứu Capstone 16 tuần. |

---

## 🗂️ PHẦN 2: BẢNG KIỂM KÊ VÀ PHÂN LOẠI TOÀN BỘ 31 TỆP MARKDOWN

| STT | Đường Dẫn Tệp | Phân Nhóm | Hiện Trạng & Mức Độ Lệch Nghiệp Vụ | Hành Động Yêu Cầu |
|:---:|---|---|---|:---:|
| 1 | `01_Tai_Lieu_Dac_Ta_Goc/Actor_KhachHang_Xem.md` | Đặc Tả Gốc | 🔴 Chứa Staff Mobile App, GPS 50m, Dine-in thanh toán sau, thiếu Delivery, 5 AI lẫn lộn. | **Viết lại toàn bộ** |
| 2 | `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS.md` | Đặc Tả Gốc | 🔴 Chứa Staff Mobile App, GPS 50m, Dine-in thanh toán sau, gộp chung Waiter/Barista, thiếu Delivery. | **Viết lại toàn bộ** |
| 3 | `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS_Revised.md` | Đặc Tả Gốc | 🟡 Đã cập nhật 2 AI module nhưng vẫn còn Staff App, GPS 50m, QR động 30s, Dine-in trả sau. | **Viết lại / Chuẩn hóa** |
| 4 | `01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md` | Đặc Tả Gốc | 🔴 Tài liệu 882 dòng chứa luồng Dine-in cũ, QR Takeaway cũ, GPS 50m, Tech Stack cũ, thiếu Delivery. | **Viết lại toàn bộ** |
| 5 | `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Smart_FB_OS.md` | Đặc Tả Gốc | 🔴 16 Workflow chứa WF-01 trả sau, WF-07 GPS, thiếu WF Delivery, thiếu WF Takeaway NV, 5 AI. | **Viết lại toàn bộ** |
| 6 | `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.md` | Báo Giá | 🟡 Chứa bảng QR Takeaway tại quầy (cũ), thiếu QR Delivery poster, cam kết vượt phạm vi 15tr. | **Cập nhật nội dung** |
| 7 | `03_Quy_Trinh_Trien_Khai/01_QUY_TRINH_PHAN_TICH_YEU_CAU.md` | Quy Trình | 🟡 MVP 12 tính năng chứa yêu cầu bill, thiếu Delivery, thiếu Takeaway NV, thiếu WiFi attendance. | **Cập nhật MVP & Rules** |
| 8 | `03_Quy_Trinh_Trien_Khai/02_QUY_TRINH_THIET_KE_DATABASE.md` | Quy Trình | 🔴 ERD 28 bảng thiếu `delivery_address`, `delivery_fee`, `OrderType`, WiFi config, thừa GPS. | **Cập nhật Schema & Rules** |
| 9 | `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT.md` | Quy Trình | 🟡 Chứa endpoint `request-bill`, `BillRequested`, thiếu Delivery/Takeaway endpoints, thiếu WiFi check-in. | **Cập nhật API Contract** |
| 10 | `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md` | Quy Trình | 🟡 2,500 dòng; có enum Delivery nhưng thiếu endpoint chi tiết, thiếu WiFi check-in, còn endpoint GPS. | **Cập nhật API Chi Tiết** |
| 11 | `03_Quy_Trinh_Trien_Khai/04_QUY_TRINH_THIET_KE_UI_UX.md` | Quy Trình | 🟡 Chứa phân hệ Staff App, thiếu Delivery UI, thiếu Takeaway Staff UI. | **Cập nhật Wireframe Flow** |
| 12 | `03_Quy_Trinh_Trien_Khai/04_THIET_KE_UI_UX_DESIGN_SYSTEM.md` | Quy Trình | 🔴 1,294 dòng; Chương 4 thiết kế hoàn toàn cho Staff Mobile & Sunmi POS + GPS 50m/QR 30s. | **Đại phẫu Chương 4 & 2** |
| 13 | `03_Quy_Trinh_Trien_Khai/05_QUY_TRINH_PHAT_TRIEN_BACKEND.md` | Quy Trình | 🟡 Luồng order engine và payment cần cập nhật theo Dine-in pre-pay, Delivery fee, WiFi attendance. | **Cập nhật BE Process** |
| 14 | `03_Quy_Trinh_Trien_Khai/06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md` | Quy Trình | 🟡 Route Groups chứa `(staff)` di động; cần đổi thành Staff Web / Takeaway POS, thêm Delivery PWA. | **Cập nhật FE Routes** |
| 15 | `03_Quy_Trinh_Trien_Khai/07_QUY_TRINH_TESTING_DEPLOYMENT.md` | Quy Trình | 🟡 E2E test flows và AI integration (AI-1 vs AI-5) cần chuẩn hóa theo scope mới. | **Cập nhật Test & Scope** |
| 16 | `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md` | Sơ Đồ Kiến Trúc | 🟡 Tầng 1 chứa Staff Mobile App, C4 Context thiếu Delivery & Takeaway NV flows. | **Cập nhật Sơ đồ Mermaid** |
| 17 | `04_Thiet_Ke_Kien_Truc_Diagrams/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md` | Sơ Đồ Kiến Trúc | 🔴 Sequence 1 & 3 mô tả Dine-in trả sau & gửi KDS trước thanh toán; thiếu Sequence Delivery/Takeaway/WiFi. | **Viết lại 5 Sequence** |
| 18 | `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` | Sơ Đồ Kiến Trúc | 🔴 ERD Mermaid thiếu trường Delivery, WiFi branch, thừa GPS attendance, thiếu loyalty 10-cup. | **Cập nhật Mermaid ERD** |
| 19 | `04_Thiet_Ke_Kien_Truc_Diagrams/04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md` | Sơ Đồ Kiến Trúc | 🟢 Hạ tầng 4 containers chuẩn; cần chỉnh Client devices loại bỏ Staff Mobile App riêng biệt. | **Chỉnh sửa nhỏ** |
| 20 | `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md` | Quy Chuẩn | 🟡 File stub 12 dòng chuyển hướng. Đề xuất hoàn thiện thành tài liệu Coding Guidelines chuẩn hoặc tích hợp. | **Cập nhật / Hợp nhất** |
| 21 | `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md` | Quy Chuẩn | 🟢 Quy chuẩn GitFlow, Commit, PR, .env rất tốt. Chỉ cần cập nhật các biến WiFi & Delivery nếu có. | **Giữ nguyên / Thêm biến** |
| 22 | `05_Quy_Chuan_&_Test_Cases/02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md` | Test Cases | 🔴 Demo 5 phút và 15 test cases chạy theo Dine-in trả sau; thiếu Delivery, Takeaway NV, WiFi check-in. | **Viết lại Demo & UAT** |
| 23 | `05_Quy_Chuan_&_Test_Cases/03_MOCHI_DATA_SEED_DEFINITION.md` | Seed Data | 🔴 Thiếu dữ liệu mẫu WiFi branch, thiếu Delivery QR & Fee, thiếu Takeaway Loyalty 10 ly, lệch tên Mochi/SmartFB. | **Bổ sung Seed Data** |
| 24 | `05_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md` | Duplicate Folder | 🔴 Bản sao trùng lặp 100% với thư mục `04_`. | **Xóa toàn bộ folder 05_** |
| 25 | `06_Danh_Sach_Skills/DANH_SACH_SKILLS_TONG_QUAT.md` | Agent Skills | 🟢 Bảng chỉ mục 9 Leader Skills. Cần chuẩn hóa đường dẫn và bảo đảm không có staff app mobile. | **Cập nhật đường dẫn** |
| 26 | `06_Danh_Sach_Skills/SKILLS_BACKEND_VA_KIEN_TRUC.md` | Agent Skills | 🟢 Registry prompt backend. Giữ nguyên, chuẩn hóa tham chiếu. | **Giữ nguyên** |
| 27 | `06_Danh_Sach_Skills/SKILLS_DEVOPS_GIT_VA_RELEASE.md` | Agent Skills | 🟡 Sửa lỗi gõ nhầm đường dẫn thư mục kiến trúc (`05_` → `04_`). | **Sửa lỗi đường dẫn** |
| 28 | `06_Danh_Sach_Skills/SKILLS_FRONTEND_VA_UIUX.md` | Agent Skills | 🟢 Đã loại bỏ Staff Mobile App, đúng chuẩn 4 Route Groups. | **Giữ nguyên** |
| 29 | `06_Danh_Sach_Skills/SKILLS_TESTING_QA_VA_SECURITY.md` | Agent Skills | 🟢 Registry prompt QA. Giữ nguyên. | **Giữ nguyên** |
| 30 | `DOC_AUDIT_REPORT.md` | Báo Cáo Kiểm Toán | 🔴 Báo cáo kiểm toán lập ngày 14/08/2026 dựa trên docs cũ. Cần viết lại phản ánh đúng hiện trạng sau overhaul. | **Viết lại theo docs mới** |
| 31 | `ROADMAP.md` | Lộ Trình Triển Khai | 🔴 8 Sprints (16 tuần) chứa các task Staff Mobile App, Yêu cầu bill, GPS attendance; cần tái cấu trúc. | **Cập nhật 8 Sprints** |

---

## 🔍 PHẦN 3: PHÂN TÍCH CHI TIẾT TỪNG TỆP (FILE-BY-FILE AUDIT & DIVERGENCE ANALYSIS)

---

### THƯ MỤC 01: TÀI LIỆU ĐẶC TẢ GỐC (`01_Tai_Lieu_Dac_Ta_Goc/`)

#### 1. `01_Tai_Lieu_Dac_Ta_Goc/Actor_KhachHang_Xem.md`
- **Mục đích:** Tài liệu trình bày góc nhìn người dùng, pitch cho khách hàng và chủ đầu tư về 4 nhóm người dùng, trải nghiệm vận hành và bảng tính năng.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *Dòng 13, 149, 283:* Nhắc đến `TV/Màn hình quầy (KDS) + Mobile App nội bộ nhân viên`, `App nhân viên nhận alert "Bàn X cần bill" -> In bill -> Thu tiền -> Xác nhận`, tính năng `Mobile App nội bộ`.
  - *Dòng 30, 148:* Nhắc đến `Chấm công QR + GPS`, `Chấm công GPS & QR` bằng mã QR động và bán kính GPS.
  - *Dòng 68, 85, 86:* Khách trải nghiệm `Yêu cầu thanh toán -> Nhân viên mang bill ra bàn hoặc thanh toán tại quầy`, tính năng `Yêu cầu in bill`, `Thanh toán tại bàn`.
  - *Thiếu hoàn toàn:* Luồng QR Delivery (đặt tại nhà, nhập địa chỉ, phí ship 20.000 VNĐ, thanh toán VietQR trước); luồng Takeaway nhân viên tạo đơn kèm loyalty 10 ly = 1 ly; cơ chế chấm công WiFi-locked.
  - *AI Scope:* Liệt kê toàn bộ 5 Module AI hoạt động song song mà không phân tách 2 AI chính vs 3 AI Future Work.
- **Phần cần viết lại:**
  - Mục 1 (Khách hàng): Cập nhật luồng Dine-in thanh toán VietQR trước khi bếp nhận đơn; thêm phân nhóm Đặt hàng Delivery tại nhà; cập nhật tính năng Takeaway.
  - Mục 2 (Nhân viên): Xóa bỏ hoàn toàn Staff Mobile App; chuyển sang giao diện Web KDS và Web Staff POS; thay chấm công GPS bằng chấm công WiFi-locked; thêm giao diện tạo đơn Takeaway.
  - Bảng phân bổ AI: Ghi rõ AI-1 (Chatbot RAG) và AI-2 (Gợi ý Combo) là triển khai chính thức; AI-3, AI-4, AI-5 đưa vào mục "Scale Up / Định hướng tương lai".
- **Phụ thuộc chéo:** Liên kết với `Actor_Smart_FB_OS_Revised.md`, `Workflow_Smart_FB_OS.md`, và `04_THIET_KE_UI_UX_DESIGN_SYSTEM.md`.

#### 2. `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS.md`
- **Mục đích:** Đặc tả chi tiết 4 Actor kỹ thuật, phân bổ mã tính năng (`C-xx`, `S-xx`, `M-xx`, `A-xx`), giao diện và quyền hạn.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *Dòng 12, 126, 130:* Định nghĩa Actor 2 sử dụng `KDS (TV/Tablet) + Staff App (Mobile)`, "nhận alert từ App Nội Bộ Nhân Viên (Staff Mobile App)".
  - *Dòng 38, 175, 436:* Luồng thao tác có `Yêu cầu bill → NV | In bill, thu tiền`, tính năng `S-10: Nhận thông báo Gọi NV + Yêu cầu bill`, `F-30: Alert gọi nhân viên & yêu cầu bill`.
  - *Dòng 160, 438:* Tính năng `S-11: Chấm công đa phương thức (App: QR động + GPS Lock)`.
  - *Thiếu sót:* Không có mã tính năng cho Đặt hàng Delivery (`C-xx: Đặt giao hàng tận nơi`, `C-xx: Nhập địa chỉ nhận hàng & tính phí ship 20k`), thiếu tính năng Staff Takeaway Counter (`S-xx: Tạo đơn mang về tại quầy & tra cứu SĐT loyalty`).
- **Phần cần viết lại:**
  - Tái định nghĩa Actor 2: "Barista / Nhân viên vận hành quầy" sử dụng KDS Web & Staff Web POS (bỏ Staff App).
  - Tái cấu trúc mã tính năng: Xóa `S-12 (Staff Mobile App)`, sửa `S-10` (bỏ yêu cầu bill, chỉ giữ gọi hỗ trợ), sửa `S-11` (thành Chấm công xác thực WiFi-locked), bổ sung mã tính năng cho Delivery và Takeaway Counter.
  - Chuyển các tính năng AI-3 (NLQ Analytics), AI-4 (Churn Prediction), AI-5 (Menu Intelligence) vào mục "Scale Up / Future Work".
- **Phụ thuộc chéo:** Liên kết trực tiếp với RBAC Matrix trong `01_QUY_TRINH_PHAN_TICH_YEU_CAU.md` và API Endpoints trong `03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md`.

#### 3. `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS_Revised.md`
- **Mục đích:** Phiên bản đặc tả Actor đã điều chỉnh cho nhóm 4 thành viên (đã khoanh vùng 2 AI modules).
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - Mặc dù đã khoanh vùng AI (66 tính năng), tệp này **vẫn giữ nguyên 4 lỗi nghiệp vụ lớn**:
    1. Vẫn ghi Actor 2 dùng `Staff App (Mobile)` (Dòng 18, 142, 146, 437 - `F-31: Staff Mobile App`).
    2. Vẫn giữ cơ chế chấm công `QR Code động (đổi 30s) + GPS Lock (bán kính 50m)` (Dòng 176, 438 - `F-32`).
    3. Vẫn giữ luồng Dine-in `Yêu cầu bill → NV | In bill, thu tiền` (Dòng 44, 98, 175, 436).
    4. Vẫn thiếu hoàn toàn nghiệp vụ Delivery (QR Delivery, địa chỉ, phí 20k) và Takeaway NV (giao diện POS, loyalty 10 ly).
- **Phần cần viết lại:**
  - Cập nhật triệt để theo 5 Core Changes: Bỏ Staff App, bỏ GPS/QR 30s, đưa VietQR Pre-pay vào Dine-in, bổ sung Delivery và Takeaway Counter.
  - Cập nhật lại tổng số tính năng cho khớp với bảng tổng hợp mới.
- **Phụ thuộc chéo:** Đây là tài liệu cầu nối giữa Đặc Tả Gốc và Phân Tích Yêu Cầu MVP.

#### 4. `01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md`
- **Mục đích:** Báo cáo đặc tả tổng quan quy mô lớn (882 dòng), phân tích 8 nỗi đau ngành F&B, giải pháp đề xuất, kiến trúc kỹ thuật và so sánh đối thủ.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *Mục 3 (Dòng 215-237):* Mô tả "BƯỚC 3: YÊU CẦU THANH TOÁN -> Khách bấm Yêu cầu bill -> NV nhận alert -> In bill -> Mang ra bàn..." (Luồng trả sau cũ).
  - *Mục 3.3 (Dòng 273):* "Khách takeaway: Scan QR tại quầy/cửa -> Chọn Mang đi -> Thanh toán -> Nhận đồ" (QR Takeaway cũ).
  - *Mục 4 (Dòng 280-288, 765, 869):* "Chấm công QR Code động (đổi 30s) + GPS Lock (bán kính 50m quán)".
  - *Mục 7 & Bảng tính năng:* Đề cập `Staff Mobile App` chạy trên điện thoại nhân viên phục vụ; tích hợp 5 AI features hoạt động đồng thời.
  - *Tech Stack cũ (Mục 17):* Còn sót lại các tham chiếu Node.js/Python/Flutter từ các bản thảo đầu tiên.
- **Phần cần viết lại:**
  - Viết lại Mục 3 thành Luồng QR Self-Order Chuẩn: Quét QR → Chọn món → Thanh toán VietQR → Bếp nhận đơn qua KDS.
  - Thêm mục giải pháp mới cho **QR Delivery** (Đặt hàng tại nhà với phí ship 20.000 VNĐ) và **Takeaway Counter Web POS** (NV thao tác, loyalty 10 ly = 1 ly).
  - Viết lại Mục 4 thành Chấm Công Thông Minh WiFi-locked (xác thực mạng WiFi quán + Mã NV).
  - Khóa cứng Tech Stack: .NET 8 Clean Architecture + Next.js 14 + PostgreSQL 16 + Redis 7 + SignalR.
  - Chuyển AI-3, AI-4, AI-5 vào phần "Scale Up / Kiến trúc tương lai".
- **Phụ thuộc chéo:** Tài liệu mẹ của toàn bộ dự án, định hình các quy trình triển khai tại `03_` và kiến trúc tại `04_`.

#### 5. `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Smart_FB_OS.md`
- **Mục đích:** Đặc tả 16 quy trình luồng nghiệp vụ chi tiết (Workflows) dưới dạng ASCII Flowcharts và bảng dữ liệu.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *WF-01 (Đặt món):* Mô tả khách gửi đơn không thanh toán → KDS hiện đơn → Pha xong → Bấm yêu cầu bill → Thu tiền sau.
  - *WF-07 (Chấm công):* Mô tả quét QR động 30s kết hợp kiểm tra Geolocation GPS bán kính 50m.
  - *Thiếu Workflows:* Thiếu hẳn Workflow Đặt Hàng Giao Tận Nơi (QR Delivery) và Workflow Đặt Món Mang Đi Tại Quầy (Takeaway Staff POS).
  - *WF-04, WF-11, WF-13, WF-14:* Trình bày AI Churn Prediction và AI Thống kê tự động như các luồng core đang chạy.
  - *Staff App references:* Xuất hiện trong WF-01, WF-02, WF-03, WF-07.
- **Phần cần viết lại:**
  - *Sửa WF-01:* Khách chọn món → Thanh toán VietQR → Backend nhận Webhook/Xác nhận → SignalR đẩy đơn vào KDS.
  - *Bổ sung WF-01B (hoặc WF mới):* **Quy Trình Đặt Hàng QR Delivery** (Scan QR ở poster/fanpage → Nhập SĐT & Địa chỉ nhận hàng → Chọn món → Thanh toán VietQR [Tiền món + 20k ship] → Đơn bay vào KDS & Hàng đợi giao hàng).
  - *Bổ sung WF-01C (hoặc WF mới):* **Quy Trình Khách Mua Mang Về Takeaway Tại Quầy** (NV mở Web POS → Nhập/Tìm SĐT khách → Hiển thị số ly tích lũy [x/10] → Chọn món → In tạm tính/Làm đồ → Khách nhận món → Thu tiền mặt/VietQR → Hoàn tất tích ly).
  - *Sửa WF-07:* **Quy Trình Chấm Công WiFi-locked** (NV kết nối WiFi quán → Mở trang Chấm công → Quét QR check-in & Nhập mã NV → Kiểm tra SSID/BSSID & Mã NV → Ghi nhận vào ca).
  - *Đóng dấu Scale Up:* Ghi rõ WF-11 (AI Thống kê NLQ), WF-14 (AI Churn Prediction) thuộc phạm vi "Scale Up / Future Work".
- **Phụ thuộc chéo:** Trực tiếp làm cơ sở cho Sequence Diagrams trong `04_02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md` và Test Cases trong `05_02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md`.

---

### THƯ MỤC 02: BÁO GIÁ & CHI PHÍ (`02_Bao_Gia_Chi_Phi/`)

#### 6. `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.md`
- **Mục đích:** Bảng báo giá thương mại triển khai giải pháp Smart F&B OS cho khách hàng chuỗi 3 chi nhánh.
- **Nội dung lỗi thời / Cần cập nhật:**
  - *Phần B (Thiết bị phần cứng) - Dòng 44:* Liệt kê `Bảng QR Takeaway tại quầy (30.000 VNĐ x 3 = 90.000 VNĐ)`. Trong nghiệp vụ mới, Takeaway chuyển sang NV thao tác trên máy quầy, không dùng QR Takeaway riêng.
  - *Thiếu thiết bị:* Cần bổ sung hạng mục in ấn **Bảng/Standee QR Delivery (Giao tận nơi)** để đặt tại cửa hoặc phân phối trên fanpage/poster.
  - *Phần A & C (Phần mềm & AI):* Cần làm rõ phạm vi AI đóng gói trong gói MVP thương mại: Chatbot tư vấn khẩu vị (AI-1) và Gợi ý combo tăng doanh số (AI-2). Các module thống kê tự nhiên nâng cao và dự báo churn được ghi chú là gói nâng cấp mở rộng.
- **Phụ thuộc chéo:** Đồng bộ với danh mục QR Code trong `04_03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` và Seed Data trong `05_03_MOCHI_DATA_SEED_DEFINITION.md`.

---

### THƯ MỤC 03: QUY TRÌNH TRIỂN KHAI (`03_Quy_Trinh_Trien_Khai/`)

#### 7. `03_Quy_Trinh_Trien_Khai/01_QUY_TRINH_PHAN_TICH_YEU_CAU.md`
- **Mục đích:** Chốt phạm vi MVP Tier 1 (12 nhóm tính năng), các ràng buộc nghiệp vụ (Business Rules) và Ma trận phân quyền (RBAC Matrix).
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *Mục 1.1 (Dòng 14):* Tính năng 4 ghi `Yêu Cầu Bill & Gọi NV: Phát tín hiệu Alert tức thì tới Staff App và KDS`.
  - *Mục 1.2 (Business Rules):* Quy tắc thanh toán VietQR và hủy đơn chưa phản ánh luồng Dine-in trả trước; thiếu quy tắc cho đơn Delivery (địa chỉ bắt buộc, phí ship cố định 20.000 VNĐ, không COD) và đơn Takeaway (NV tạo đơn, thanh toán sau, loyalty 10 ly = 1 ly).
  - *Thiếu nghiệp vụ chấm công:* Chưa có Business Rule cho Chấm công WiFi-locked.
  - *RBAC Matrix:* Còn hiển thị role Staff với quyền nhận Alert trên Staff App di động.
- **Phần cần viết lại:**
  - Cập nhật 12 nhóm MVP: Thay "Yêu cầu bill" bằng "Thanh toán VietQR Pre-pay & KDS Dispatch"; bổ sung "QR Delivery Hub" và "Takeaway Counter POS".
  - Cập nhật Business Rules:
    1. *Dine-in:* Khách bắt buộc thanh toán VietQR thành công mới chuyển đơn sang KDS.
    2. *Delivery:* Bắt buộc SĐT + Địa chỉ; tự động cộng 20.000 VNĐ phí ship; chỉ thanh toán online VietQR.
    3. *Takeaway:* NV tạo đơn; thanh toán tiền mặt/VietQR sau khi nhận đồ; tích lũy 10 ly tặng 1 ly.
    4. *Chấm công:* Bắt buộc kết nối đúng WiFi chi nhánh (SSID/BSSID hợp lệ) + Mã nhân viên đúng.
  - Cập nhật RBAC Matrix: Bỏ Staff App, gộp thao tác của nhân viên vào Web POS/KDS.
- **Phụ thuộc chéo:** Quyết định trực tiếp cấu trúc của `02_QUY_TRINH_THIET_KE_DATABASE.md` và `03_QUY_TRINH_THIET_KE_API_CONTRACT.md`.

#### 8. `03_Quy_Trinh_Trien_Khai/02_QUY_TRINH_THIET_KE_DATABASE.md`
- **Mục đích:** Hướng dẫn quy chuẩn thiết kế Database ERD 28 bảng, Indexing Strategy và quy trình Code-First Migration.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - Chỉ liệt kê tên 28 bảng mà không mô tả các trường phục vụ 5 thay đổi nghiệp vụ:
    - Bảng `Orders`: Cần có `OrderType` (Enum: `DineIn`, `TakeAway`, `Delivery`), `DeliveryAddress` (string nullable), `DeliveryFee` (decimal, default 20000 cho Delivery, 0 cho loại khác), `TableId` (nullable cho TakeAway/Delivery).
    - Bảng `Branches`: Cần có `WifiSsid`, `WifiBssid` (hoặc `WifiMacAddress`), `WifiSubnetIP` để cấu hình WiFi-locked attendance.
    - Bảng `Attendances`: Cần xóa các trường kinh độ/vĩ độ/bán kính GPS, thay bằng `ConnectedWifiSsid`, `ConnectedWifiBssid`, `EmployeeCode`.
    - Bảng `Customers`: Cần thêm trường quản lý chương trình tích ly `CupCount` (int, 0-9), `FreeCupCount` (int) thay cho điểm point trừu tượng.
    - Bảng `QrCodes`: `QrType` enum gồm `Table` và `Delivery` (bỏ `Takeaway` QR).
- **Phần cần viết lại:**
  - Bổ sung định nghĩa trường dữ liệu chi tiết cho 28 bảng, đặc biệt là các bảng bị ảnh hưởng bởi 5 Core Changes.
  - Cập nhật lại Indexing Strategy: Thêm index cho `OrderType`, `Customers(Phone)`, `Branches(WifiSsid)`.
- **Phụ thuộc chéo:** Phải khớp 100% với `04_03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` và `05_03_MOCHI_DATA_SEED_DEFINITION.md`.

#### 9. `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT.md`
- **Mục đích:** Tổng quan chuẩn Envelope JSON, danh mục nhóm 45+ endpoints và hợp đồng sự kiện SignalR.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *Endpoints (Dòng 64):* Vẫn còn `POST /orders/{id}/request-bill`.
  - *SignalR Events (Dòng 84-85):* Vẫn còn sự kiện `BillRequested` phát tới `Staff App`.
  - *Thiếu Endpoints:* Thiếu `POST /api/v1/orders/delivery`, `POST /api/v1/orders/takeaway`, `GET /api/v1/customers/lookup`, `POST /api/v1/attendance/wifi-checkin`.
- **Phần cần viết lại:**
  - Xóa bỏ các endpoint và sự kiện liên quan đến "yêu cầu bill" và Staff App.
  - Bổ sung nhóm endpoint Delivery, Takeaway POS và Chấm công WiFi.
  - Cập nhật SignalR Contract: Thêm sự kiện `OrderPaid` (kích hoạt KDS), bỏ `BillRequested`.
- **Phụ thuộc chéo:** Khung hướng dẫn cho `03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md`.

#### 10. `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md`
- **Mục đích:** Đặc tả chi tiết 64+ RESTful endpoints và 4 SignalR Hubs (2,505 dòng) với đầy đủ Request/Response JSON Schema và RFC 7807 ProblemDetails.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *Dòng 1005:* Đã có enum `orderType: ["DineIn", "TakeAway", "Delivery"]` nhưng schema `OrderResponse` và `CreateOrderRequest` chưa có trường `deliveryAddress` và `deliveryFee`.
  - *Mục Chấm công (Dòng 2131):* Mô tả `POST /api/v1/hrm/attendance/check-in` bằng tọa độ GPS Geofence (bán kính < 50m) kết hợp quét mã QR xoay 30 giây.
  - *Mục Staff Alerts:* Còn chứa các endpoint nhận thông báo gọi bill và xuất VietQR di động trên Staff App.
- **Phần cần viết lại:**
  - Cập nhật Schema `CreateOrderRequest`: Nếu `orderType == "Delivery"`, `deliveryAddress` là bắt buộc, `deliveryFee` tự động set 20000; nếu `orderType == "DineIn"`, `tableId` là bắt buộc.
  - Viết lại endpoint Chấm công: `POST /api/v1/hrm/attendance/wifi-checkin` nhận `{ branchId, employeeCode, wifiSsid, wifiBssid }`.
  - Bổ sung endpoint Takeaway POS: `POST /api/v1/orders/takeaway` (NV tạo đơn, hỗ trợ áp dụng ly miễn phí từ loyalty 10 ly) và `PATCH /api/v1/orders/{id}/pay-takeaway` (xác nhận thanh toán sau).
  - Tinh gọn SignalR Hubs: Loại bỏ các event gửi tới Staff App cũ.
- **Phụ thuộc chéo:** Hợp đồng giao tiếp sống giữa Backend (.NET 8) và Frontend (Next.js 14).

#### 11. `03_Quy_Trinh_Trien_Khai/04_QUY_TRINH_THIET_KE_UI_UX.md`
- **Mục đích:** Quy trình thiết kế Wireframe, cấu trúc Design Tokens và phân bổ 4 phân hệ giao diện.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - *Mục 1.1 (Dòng 21):* Phân hệ 3 là `STAFF APP (Phục vụ): Alert Bar (Gọi bàn / Yêu cầu Bill), Sơ đồ bàn trực quan, Báo hết món nhanh`.
  - *Mục 2 (Dòng 81):* Setup Next.js Route Groups có `/(staff)`.
  - *Thiếu giao diện:* Thiếu phân hệ cho Delivery Order Flow và Takeaway Counter Web POS.
- **Phần cần viết lại:**
  - Thay đổi 4 phân hệ giao diện:
    1. `QR ORDER & DELIVERY PWA (Khách hàng)`: Mobile-first, hỗ trợ cả Dine-in (chọn bàn + VietQR pre-pay) và Delivery (nhập địa chỉ + 20k ship).
    2. `KDS BẾP (Barista)`: Full-screen TV/Tablet, nhận đơn sau thanh toán.
    3. `STAFF & MANAGER WEB PORTAL (Nhân viên & Quản lý)`: Web POS Takeaway (tìm SĐT, tích 10 ly, thanh toán sau), Sơ đồ bàn, Chấm công WiFi, Mở/Kết ca, Quản lý kho.
    4. `ADMIN DASHBOARD (Chủ chuỗi)`: Quản trị menu, giá, combo AI, báo cáo toàn chuỗi.
  - Sửa lại Route Groups Next.js: `(customer)`, `(kds)`, `(portal)` hoặc `(manager)`, `(admin)`. Xóa bỏ `(staff)` mobile app riêng biệt.
- **Phụ thuộc chéo:** Khung hướng dẫn cho `04_THIET_KE_UI_UX_DESIGN_SYSTEM.md`.

#### 12. `03_Quy_Trinh_Trien_Khai/04_THIET_KE_UI_UX_DESIGN_SYSTEM.md`
- **Mục đích:** Tài liệu thiết kế Design System & Wireframe chi tiết nhất dự án (1,294 dòng, 29 màn hình Wireframe ASCII, Design Tokens HSL/Hex, Animations).
- **Nội dung lỗi thời / Lệch nghiệp vụ nghiêm trọng:**
  - *Chương 2 (Giao diện Khách hàng):* Màn hình `SCR-PWA-04` (Giỏ hàng) và `SCR-PWA-07` (Gọi phục vụ & Yêu cầu Bill) vẫn theo luồng trả sau (gửi đơn không thanh toán). Thiếu màn hình Đặt hàng Delivery (nhập địa chỉ, cộng phí ship 20.000 VNĐ, sinh VietQR thanh toán trước).
  - *Chương 4 (Chương STAFF MOBILE & SUNMI POS DUAL-SCREEN):* Toàn bộ Chương 4 (5 màn hình: `SCR-STAFF-01` đến `SCR-STAFF-05`) được thiết kế cho Handheld Mobile POS / Smartphone 360x800 của nhân viên phục vụ, bao gồm:
    - `SCR-STAFF-03`: Mobile VietQR Dynamic Payment Generator (Thu tiền tại bàn).
    - `SCR-STAFF-05`: 30s Dynamic QR Code & 50m GPS Attendance Clock-in.
  - *Chương 6 (Admin Dashboard):* Màn hình `SCR-ADM-05` (AI Customer Churn Risk Prediction) chưa được đánh dấu là "Scale Up / Future Work".
- **Phần cần viết lại (Đại phẫu):**
  - *Chương 2:* Sửa `SCR-PWA-04` thành Checkout thanh toán VietQR ngay; cập nhật `SCR-PWA-06` (Tracking đơn) bắt đầu từ trạng thái Đã thanh toán; bổ sung Wireframe `SCR-PWA-DELIVERY` (Màn hình đặt hàng giao tận nơi với Form Địa chỉ, Phí ship 20k và VietQR Pay).
  - *Chương 4:* **Viết lại toàn bộ Chương 4 thành "GIAO DIỆN WEB QUẦY & VẬN HÀNH NHÂN VIÊN (STAFF WEB POS & COUNTER)":**
    - `SCR-STAFF-01`: Giao diện Tạo Đơn Mang Về Tại Quầy (Takeaway Web POS) với thanh tìm kiếm SĐT khách, hiển thị vòng tròn tích lũy 10 ly, chọn món và nút thanh toán sau.
    - `SCR-STAFF-02`: Sơ đồ bàn & Trạng thái phục vụ trên Web.
    - `SCR-STAFF-03`: Giao diện Báo hết món (86 Toggle) nhanh tại quầy.
    - `SCR-STAFF-04`: Màn hình Chấm Công WiFi-locked (hiển thị trạng thái kết nối WiFi quán, nút Quét QR và ô nhập Mã số NV).
    - Xóa bỏ hoàn toàn wireframe Sunmi 2 màn hình và GPS 50m.
  - *Chương 6:* Đánh dấu `SCR-ADM-05` (AI Churn) và `SCR-ADM-04` (AI Business NLQ nếu có) là Scale Up.
- **Phụ thuộc chéo:** Định hình toàn bộ giao diện Frontend Next.js 14 trong `06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md`.

#### 13. `03_Quy_Trinh_Trien_Khai/05_QUY_TRINH_PHAT_TRIEN_BACKEND.md`
- **Mục đích:** Hướng dẫn luồng dữ liệu 4 tầng Clean Architecture, thứ tự code từng module và phân công BE1 vs BE2.
- **Nội dung lỗi thời / Cần cập nhật:**
  - *Bước 5.3 & 5.4:* Cần điều chỉnh Order Engine để nhận diện `OrderType`, tính toán `DeliveryFee` tự động, và chỉ kích hoạt SignalR broadcast sang KDS sau khi Payment đã `Confirmed`.
  - *Bước 5.6:* HRM Module cần cập nhật logic xác thực WiFi chi nhánh thay cho GPS.
  - *Phân công AI:* BE1 phụ trách AI-1 (Chatbot RAG qua Gemini API), BE2 phụ trách AI-2 (Gợi ý Combo qua thuật toán Apriori/FP-Growth trong C#).
- **Phụ thuộc chéo:** Khung thực thi kỹ thuật cho Backend.

#### 14. `03_Quy_Trinh_Trien_Khai/06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md`
- **Mục đích:** Chiến lược Mock-First, cấu trúc Route Groups Next.js 14 và hook kết nối SignalR Client.
- **Nội dung lỗi thời / Cần cập nhật:**
  - *Route Groups (Dòng 25-40):* Xóa bỏ `src/app/(staff)/alerts/page.tsx`.
  - Bổ sung cấu trúc Route Groups mới:
    - `src/app/(customer)/delivery/page.tsx`: Giao diện đặt hàng Delivery.
    - `src/app/(portal)/takeaway/page.tsx` hoặc `(staff)/takeaway/page.tsx`: Web POS cho nhân viên quầy.
    - `src/app/(portal)/attendance/page.tsx`: Giao diện chấm công WiFi.
  - Cập nhật hook SignalR để lắng nghe sự kiện thanh toán thành công và chuyển trang tự động.
- **Phụ thuộc chéo:** Khung thực thi kỹ thuật cho Frontend.

#### 15. `03_Quy_Trinh_Trien_Khai/07_QUY_TRINH_TESTING_DEPLOYMENT.md`
- **Mục đích:** Chiến lược kiểm thử 3 cấp độ, tích hợp AI Engine và cấu hình Docker Deploy.
- **Nội dung lỗi thời / Cần cập nhật:**
  - *Mục 1.2 (Tích hợp AI):* Hiện tại ghi nhầm `AI-5: Chatbot Gợi Ý Món Ăn` và `AI-1: Thống Kê Hỏi Đáp Tiếng Việt`. Cần sửa lại theo Source of Truth: **AI-1 là Recommendation Chatbot (RAG)** và **AI-2 là Combo Suggestion (Apriori)**.
  - *E2E Test Flows:* Cập nhật kịch bản E2E kiểm thử luồng Dine-in trả trước, Delivery giao tận nơi, Takeaway nhân viên quầy và Chấm công WiFi.
- **Phụ thuộc chéo:** Liên kết với `05_02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md` và `04_04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md`.

---

### THƯ MỤC 04: THIẾT KẾ KIẾN TRÚC & DIAGRAMS (`04_Thiet_Ke_Kien_Truc_Diagrams/`)

#### 16. `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md`
- **Mục đích:** Sơ đồ kiến trúc tổng quan 4 tầng (Mermaid Graph) và Sơ đồ ngữ cảnh C4 Context Level 1.
- **Nội dung lỗi thời / Cần cập nhật:**
  - *Sơ đồ 4 tầng (Dòng 16):* Xuất hiện `STAFF["📱 Staff Mobile App\n(Phục vụ PWA)"]`. Cần đổi thành `STAFF["💻 Staff Web POS & Counter\n(Nhân viên quầy Web)"]`.
  - *C4 Context Diagram:* Bỏ actor "Nhân viên phục vụ chạy bàn nhận alert gọi bill trên app di động"; thay bằng "Nhân viên vận hành quầy (Tạo đơn Takeaway, KDS, Chấm công WiFi)". Bổ sung luồng tương tác đặt hàng Delivery từ khách hàng.
  - *Tầng AI Engine:* Thể hiện rõ AI-1 (Chatbot RAG) và AI-2 (Combo Apriori) là core; AI-3, 4, 5 là extension points.
- **Phụ thuộc chéo:** Kiến trúc tổng thể chi phối tất cả các sơ đồ phân rã còn lại.

#### 17. `04_Thiet_Ke_Kien_Truc_Diagrams/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md`
- **Mục đích:** Tập hợp các sơ đồ tuần tự (Sequence Diagrams) mô tả tương tác thời gian thực giữa các Actor và Services.
- **Nội dung lỗi thời / Lệch nghiệp vụ nghiêm trọng:**
  - *Sequence 1 (Khách đặt món QR):* Bước 29-39 gửi đơn `POST /orders` tạo status `Confirmed` và broadcast ngay tới KDS Bếp mà **chưa hề thanh toán**.
  - *Sequence 3 (Khách yêu cầu bill & thanh toán VietQR):* Bước 99-119 mô tả khách ăn xong bấm "Yêu cầu thanh toán VietQR" → phát event `BillRequested` đến Staff App → Staff đến kiểm tra và confirm thủ công.
  - *Thiếu các Sequence cốt lõi:* Thiếu Sequence Đặt hàng QR Delivery (với phí ship 20k), thiếu Sequence Takeaway Counter POS (NV tra SĐT, tích 10 ly, thanh toán sau), thiếu Sequence Chấm công WiFi-locked.
- **Phần cần viết lại:**
  - *Viết lại Sequence 1:* **Luồng Dine-in Chuẩn (Thanh Toán Trước → Bếp Nhận Đơn)**: Khách chọn món → Bấm Thanh toán → Sinh mã VietQR → Khách chuyển khoản → Webhook/Confirm → SignalR Event `OrderPaid` → KDS rung chuông nhận đơn.
  - *Viết lại Sequence 2:* Barista hoàn thành món (giữ nguyên logic chuyển trạng thái KDS).
  - *Thay Sequence 3 bằng Sequence Đặt Hàng QR Delivery:* Khách scan QR Delivery → Nhập SĐT & Địa chỉ → Chọn món → Thanh toán VietQR (Tổng = Món + 20k) → Xác nhận → Đơn vào KDS & Dispatch.
  - *Thêm Sequence 4: Luồng Đặt Hàng Takeaway Tại Quầy:* NV tra SĐT CRM → Hiển thị số ly tích lũy → Chọn món → Tạo đơn → Pha chế → Khách nhận món → NV thu tiền (Tiền mặt/VietQR) → Cập nhật tích ly (+N ly, nếu đủ 10 ly tặng 1).
  - *Thêm Sequence 5: Luồng Chấm Công WiFi-locked:* NV mở trang Chấm công → Hệ thống lấy BSSID/SSID WiFi hiện tại + Mã NV → Gửi `POST /attendance/wifi-checkin` → Backend kiểm tra với cấu hình Branch → Trả về kết quả Check-in thành công.
  - *Chuyển Sequence AI Chatbot:* Thành Sequence 6 (tư vấn menu khẩu vị RAG).
- **Phụ thuộc chéo:** Cơ sở lập trình trực tiếp cho SignalR Hubs và Controllers.

#### 18. `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md`
- **Mục đích:** Sơ đồ thực thể liên kết (Mermaid ERD) chuẩn 28 bảng và bảng ma trận thực thể.
- **Nội dung lỗi thời / Lệch nghiệp vụ:**
  - Thực thể `Order` thiếu `OrderType` (Enum: `DineIn`, `TakeAway`, `Delivery`), `DeliveryAddress`, `DeliveryFee`; `TableId` chưa để nullable.
  - Thực thể `Branch` thiếu `WifiSsid`, `WifiBssid`, `WifiSubnetIP`.
  - Thực thể `Attendance` còn ghi chú "Check-in, Check-out + GPS" (Dòng 267); thiếu các trường ghi nhận WiFi.
  - Thực thể `Customer` cần bổ sung `CupCount` và `FreeCupCount`.
  - Thực thể `QrCode` cần quy định `QrType` enum (`Table`, `Delivery`).
- **Phần cần viết lại:**
  - Cập nhật sơ đồ Mermaid ERD và định nghĩa chi tiết từng Entity khớp 100% với các yêu cầu trên.
- **Phụ thuộc chéo:** Đồng bộ với `03_02_QUY_TRINH_THIET_KE_DATABASE.md` và `05_03_MOCHI_DATA_SEED_DEFINITION.md`.

#### 19. `04_Thiet_Ke_Kien_Truc_Diagrams/04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md`
- **Mục đích:** Sơ đồ mạng hạ tầng Docker Compose, Nginx Reverse Proxy và cấu hình `docker-compose.yml` production.
- **Hiện trạng:**
  - Cấu hình 4 containers (`postgres`, `redis`, `smartfb-backend`, `smartfb-frontend`) và mạng `smartfb-net` rất chuẩn xác.
  - Cần chỉnh sửa nhỏ: Phần Client Devices trong sơ đồ mạng, sửa "Smartphone Phục vụ App" thành "Thiết bị Web Quầy / Tablet KDS / Mobile PWA Khách".
- **Phụ thuộc chéo:** Đồng bộ với `docker-compose.yml` tại root.

---

### THƯ MỤC 05: QUY CHUẨN & TEST CASES (`05_Quy_Chuan_&_Test_Cases/`)

#### 20. `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md`
- **Hiện trạng:** Tệp stub 12 dòng chuyển hướng sang `01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md`.
- **Hành động:** Giữ nguyên làm redirect stub hoặc hoàn thiện thành tài liệu Coding Guidelines chuẩn để tránh nhầm lẫn.

#### 21. `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md`
- **Hiện trạng:** Tài liệu rất hoàn chỉnh về GitFlow, Conventional Commits, PR Checklist và `.env.example`.
- **Hành động:** Bổ sung thêm các biến môi trường cấu hình WiFi chi nhánh và phí ship mặc định (`DEFAULT_DELIVERY_FEE=20000`) vào phần mẫu `.env`.

#### 22. `05_Quy_Chuan_&_Test_Cases/02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md`
- **Mục đích:** Kịch bản Demo 5 phút trước Hội đồng bảo vệ đồ án và bộ 15 Test Cases UAT cốt lõi.
- **Nội dung lỗi thời / Lệch nghiệp vụ nghiêm trọng:**
  - *Kịch bản Demo (Dòng 18-34):* Bước 2 khách gửi đơn không thanh toán → Bước 3 Bếp nhận đơn pha chế → Bước 4 khách mới bấm "Yêu cầu thanh toán VietQR" và Staff App nhận alert. Đây là luồng cũ đã bị cấm!
  - *Bảng Test Cases UAT:*
    - `TC-05`: Khách đặt món không nhập SĐT → Đơn tạo trạng thái `Confirmed` ngay (Sai!).
    - `TC-10`, `TC-11`: Test case cho "Yêu cầu bill VietQR" và NV xác nhận sau khi dùng món (Sai!).
    - Thiếu hoàn toàn test cases cho: Đặt hàng Delivery (tính phí 20k, validate địa chỉ), Takeaway POS (tra SĐT, tích ly 10/10 nhận free), Chấm công WiFi (sai WiFi bị từ chối, đúng WiFi thành công).
- **Phần cần viết lại:**
  - *Viết lại Kịch bản Demo 5 phút chuẩn:*
    - Bước 1: Admin tạo menu/giá và xem Dashboard.
    - Bước 2: Khách quét QR Bàn 5 → Chọn món → Thanh toán VietQR ngay trên PWA.
    - Bước 3: Hệ thống xác nhận thanh toán → KDS Bếp lập tức nhận đơn qua SignalR → Barista bấm pha chế & hoàn thành.
    - Bước 4: NV quầy mở Web POS Takeaway → Nhập SĐT khách quen → Hiển thị tích 9/10 ly → Đặt thêm 1 ly → Kích hoạt tặng 1 ly miễn phí → Khách thanh toán sau.
    - Bước 5: NV thực hiện Chấm công WiFi thành công.
    - Bước 6: Admin Dashboard cập nhật doanh thu và số lượng đơn tức thì.
  - *Cập nhật bảng Test Cases (20+ UAT Cases):* Bổ sung đầy đủ các kịch bản kiểm thử cho 5 Core Changes.
- **Phụ thuộc chéo:** Quyết định tiêu chí nghiệm thu phần mềm của toàn bộ dự án.

#### 23. `05_Quy_Chuan_&_Test_Cases/03_MOCHI_DATA_SEED_DEFINITION.md`
- **Mục đích:** Định nghĩa dữ liệu mẫu (Seed Data) cho 3 chi nhánh, 20 bàn, menu đồ uống và tài khoản người dùng.
- **Nội dung lỗi thời / Cần bổ sung:**
  - *Chi nhánh (Mục 2.1):* Thiếu dữ liệu cấu hình WiFi (`WifiSsid: "SmartCoffee_Q1"`, `WifiBssid: "00:14:22:01:23:45"`, `WifiSubnetIP: "192.168.1.0/24"`).
  - *QR Code:* Thiếu Seed Data cho mã QR Delivery chung và mã QR Chấm công của chi nhánh.
  - *Dữ liệu Đơn Hàng Mẫu:* Cần cung cấp dữ liệu mẫu cho cả 3 loại đơn:
    1. Đơn Dine-in Bàn 5 (Đã thanh toán VietQR, Status='Completed').
    2. Đơn Takeaway tại quầy (Khách 0901234567, đã tích ly, thanh toán tiền mặt).
    3. Đơn Delivery (Địa chỉ "72 Lê Thánh Tôn, Q1", phí ship 20.000 VNĐ, thanh toán VietQR).
  - *Khách Hàng & Loyalty Mẫu:* Seed khách hàng có `CupCount = 9` để test tính năng ly thứ 10 miễn phí.
  - *Tên thương hiệu:* Đổi tiêu đề/nội dung đồng nhất thành `SMART F&B OS SEED DATA` (loại bỏ tên cũ Mochi).
- **Phụ thuộc chéo:** Nguồn dữ liệu khởi tạo cho EF Core Database Migration.

---

### THƯ MỤC 05 TRÙNG LẶP: `05_Thiet_Ke_Kien_Truc_Diagrams/`

#### 24. `05_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md`
- **Hiện trạng:** Thư mục này bị tạo trùng lặp do lỗi đặt tên thư mục trước đây. Nội dung bên trong là bản sao của `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md`.
- **Hành động bắt buộc:** **Xóa bỏ hoàn toàn thư mục `05_Thiet_Ke_Kien_Truc_Diagrams/`** để dọn sạch cấu trúc dự án và tránh xung đột đường dẫn tài liệu.

---

### THƯ MỤC 06: DANH SÁCH SKILLS (`06_Danh_Sach_Skills/`)

#### 25–29. Các Tệp Skills Registry (`DANH_SACH_SKILLS_TONG_QUAT.md`, `SKILLS_*.md`)
- **Hiện trạng:**
  - `DANH_SACH_SKILLS_TONG_QUAT.md`: Bảng điều phối 9 Skill Leaders.
  - `SKILLS_FRONTEND_VA_UIUX.md`: Đã cập nhật đúng 4 Route Groups (không còn staff app di động).
  - `SKILLS_DEVOPS_GIT_VA_RELEASE.md`: Có lỗi gõ nhầm đường dẫn thư mục `05_Thiet_Ke_Kien_Truc_Diagrams` thay vì `04_`.
- **Hành động:** Sửa lỗi đường dẫn trong `SKILLS_DEVOPS_GIT_VA_RELEASE.md`, bảo đảm tính nhất quán của toàn bộ chỉ mục skills.

---

### CÁC TỆP GỐC: `ROADMAP.md` VÀ `DOC_AUDIT_REPORT.md`

#### 30. `ROADMAP.md`
- **Mục đích:** Kế hoạch phân bổ 8 Sprints (16 tuần) cho 4 thành viên (2 BE + 2 FE).
- **Nội dung lỗi thời / Cần cập nhật:**
  - *Sprint 1 (Tuần 1-2):* ERD và API Spec cần bao hàm các trường Delivery, Takeaway, WiFi config.
  - *Sprint 3 (Tuần 5-6):* Sửa Order Flow & KDS thành luồng Dine-in thanh toán trước rồi mới phát SignalR sang KDS.
  - *Sprint 4 (Tuần 7-8):* Xóa task API yêu cầu bill (`POST /orders/{id}/request-bill`); thay bằng Task API Delivery Order & Takeaway Order; FE dựng trang Delivery PWA và Staff Takeaway Web POS; cập nhật Chấm công thành WiFi check-in.
  - *Sprint 5 (Tuần 9-10):* Xóa bỏ task dựng Staff Mobile App (`/staff/alerts`); thay bằng hoàn thiện giao diện Quầy Vận Hành (Takeaway POS, Table Map Web, Loyalty 10 ly).
  - *Sprint 6 (Tuần 11-12):* Phân định rõ scope AI: Tích hợp AI-1 Recommendation Chatbot (RAG) và AI-2 Combo Suggestion (Apriori); các AI còn lại chuyển vào tài liệu Scale Up.
- **Phụ thuộc chéo:** Kim chỉ nam điều phối tiến độ toàn bộ dự án.

#### 31. `DOC_AUDIT_REPORT.md`
- **Mục đích:** Báo cáo kiểm toán toàn diện tính toàn vẹn và mâu thuẫn của bộ tài liệu dự án.
- **Hiện trạng & Yêu cầu:** Báo cáo cũ (ngày 14/08/2026) được viết dựa trên hiện trạng ban đầu. Sau khi toàn bộ các tài liệu được viết lại và cập nhật theo 5 Thay Đổi Nghiệp Vụ Cốt Lõi, tệp `DOC_AUDIT_REPORT.md` phải được viết lại hoàn chỉnh để:
  1. Xác nhận 100% các mâu thuẫn cũ (7 Critical Blockers) đã được giải quyết triệt để.
  2. Đánh giá tính nhất quán tuyệt đối của 5 Core Changes trên toàn bộ 30+ tệp.
  3. Đưa ra kết luận thẩm định chính thức: **HỆ THỐNG ĐÃ ĐỦ ĐIỀU KIỆN 100% ĐỂ BƯỚC VÀO GIAI ĐOẠN VIẾT CODE (READY FOR DIRECT CODING)**.

---

## 🔗 PHẦN 4: MA TRẬN PHỤ THUỘC CHÉO LIÊN TỆP (CROSS-FILE DEPENDENCY MATRIX)

Mọi thay đổi trong một thành phần kỹ thuật bắt buộc phải được đồng bộ chính xác trên tất cả các tệp phụ thuộc:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             MA TRẬN PHỤ THUỘC CHÉO LIÊN TỆP                                      │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘

 [1. ĐẶC TẢ NGHIỆP VỤ & ACTORS]
    ├── 01/Smart_FB_Operating_System.md
    ├── 01/Actor_Smart_FB_OS_Revised.md
    └── 01/Workflow_Smart_FB_OS.md
               │
               ▼ (Định nghĩa Scope, Rules & Flow)
 [2. QUY TRÌNH PHÂN TÍCH & DB SCHEMA]
    ├── 03/01_QUY_TRINH_PHAN_TICH_YEU_CAU.md  ──────► Chốt 12 MVP Tier 1 & RBAC
    ├── 03/02_QUY_TRINH_THIET_KE_DATABASE.md  ──────► 28 Bảng C# Entities & EF Mapping
    └── 04/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md ► Mermaid ERD Schema
               │
               ▼ (Định nghĩa Data Contract & Events)
 [3. HỢP ĐỒNG API & SƠ ĐỒ TUẦN TỰ]
    ├── 03/03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md ──► 64+ Endpoints & 4 Hubs
    └── 04/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md     ──► 5 Sequence Diagrams
               │
               ▼ (Định nghĩa Giao diện & Layout)
 [4. THIẾT KẾ UI/UX & ROUTE GROUPS]
    ├── 03/04_THIET_KE_UI_UX_DESIGN_SYSTEM.md ──► 29 Wireframes & Tokens
    └── 03/06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md ──► Next.js 14 Route Groups
               │
               ▼ (Kiểm thử & Khởi tạo dữ liệu)
 [5. KIỂM THỬ UAT, SEED DATA & ROADMAP]
    ├── 05/02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md ──► Demo 5p & 20+ Test Cases
    ├── 05/03_MOCHI_DATA_SEED_DEFINITION.md      ──► Seed Data Mẫu (WiFi, Orders, CRM)
    ├── ROADMAP.md                               ──► Kế hoạch 8 Sprints (16 tuần)
    └── DOC_AUDIT_REPORT.md                      ──► Báo cáo Thẩm định Nghiệm thu
```

### Bảng Chi Tiết Điểm Chạm Cần Đồng Bộ Giữa Các Tệp:

| Thành Phần Nghiệp Vụ / Kỹ Thuật | Điểm Chạm Cần Đồng Bộ Trên Các Tệp |
|---|---|
| **Dine-in Pre-Payment Flow** | • `01/Workflow`: WF-01 đổi sang trả trước.<br>• `03/01_QUY_TRINH_PHAN_TICH`: Business Rule không duyệt đơn khi chưa Paid.<br>• `03/03_API_CHI_TIET`: Endpoint `POST /orders` + VietQR webhook confirm.<br>• `04/02_SEQUENCE`: Sequence 1 thanh toán VietQR trước khi đẩy sang KDS.<br>• `03/04_DESIGN_SYSTEM`: SCR-PWA-04 thanh toán VietQR tại giỏ hàng.<br>• `05/02_UAT`: Test Case thanh toán VietQR thành công mới hiện đơn trên KDS. |
| **QR Delivery Flow** | • `01/Workflow`: Bổ sung WF Đặt hàng Delivery.<br>• `03/02_DATABASE` & `04/03_ERD`: Cột `OrderType`, `DeliveryAddress`, `DeliveryFee`.<br>• `03/03_API_CHI_TIET`: Endpoint `POST /api/v1/orders/delivery`.<br>• `04/02_SEQUENCE`: Sequence đặt hàng Delivery (+20k phí ship).<br>• `03/04_DESIGN_SYSTEM`: Wireframe SCR-PWA-DELIVERY.<br>• `05/03_SEED_DATA`: Dữ liệu mẫu đơn Delivery có địa chỉ và phí ship 20k. |
| **Takeaway Counter Web POS** | • `01/Actor` & `01/Workflow`: Luồng Takeaway nhân viên tạo đơn, loyalty 10 ly.<br>• `03/02_DATABASE` & `04/03_ERD`: Cột `CupCount`, `FreeCupCount` trong bảng Customer.<br>• `03/03_API_CHI_TIET`: Endpoint `POST /orders/takeaway` & `GET /customers/lookup`.<br>• `04/02_SEQUENCE`: Sequence tạo đơn mang về & thanh toán sau.<br>• `03/04_DESIGN_SYSTEM`: Wireframe SCR-STAFF-01 (Web POS Takeaway).<br>• `05/03_SEED_DATA`: Khách mẫu tích lũy 9 ly để test ly thứ 10 miễn phí. |
| **WiFi-locked Attendance** | • `01/Smart_FB_OS` & `01/Workflow`: Luồng chấm công WiFi quán.<br>• `03/02_DATABASE` & `04/03_ERD`: Cột `WifiSsid`, `WifiBssid` trong Branch; xóa GPS trong Attendance.<br>• `03/03_API_CHI_TIET`: Endpoint `POST /api/v1/hrm/attendance/wifi-checkin`.<br>• `04/02_SEQUENCE`: Sequence kiểm tra WiFi và Mã NV.<br>• `03/04_DESIGN_SYSTEM`: Wireframe SCR-STAFF-04 (Chấm công WiFi).<br>• `05/03_SEED_DATA`: Dữ liệu cấu hình WiFi cho 3 chi nhánh. |
| **Xóa Staff Mobile App** | • `01/Actor` & `01/Smart_FB_OS`: Xóa Actor Staff App di động, chuyển sang Web KDS / Staff Web.<br>• `03/04_DESIGN_SYSTEM`: Viết lại toàn bộ Chương 4 thành Web POS & Quầy vận hành.<br>• `03/06_FRONTEND`: Xóa Route Group `(staff)` mobile app.<br>• `04/01_KIEN_TRUC`: Xóa client container di động trong sơ đồ kiến trúc.<br>• `ROADMAP.md`: Xóa toàn bộ task lập trình Flutter/React Native/Staff App. |
| **Phân Định 2 AI Core vs 3 Scale Up** | • `01/Actor` & `01/Smart_FB_OS`: Đánh dấu AI-1 (Chatbot RAG) & AI-2 (Combo Apriori) là triển khai; AI-3, 4, 5 là Future Work.<br>• `03/07_TESTING`: Chỉ định hướng test AI-1 và AI-2.<br>• `ROADMAP.md`: Sắp xếp task Sprint 6 tập trung hoàn thành AI-1 và AI-2. |

---

## 📋 PHẦN 5: BẢNG CHỈ DẪN VÀ THỨ TỰ THỰC THI CHO ĐỘI NGŨ WRITERS

Để việc viết lại bộ tài liệu diễn ra trơn tru, không bị xung đột hay thiếu sót, đội ngũ Writers nên thực hiện tuần tự theo 4 giai đoạn:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          LỘ TRÌNH THỰC THI 4 GIAI ĐOẠN ĐẠI PHẪU DOCS                             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 1: Chuẩn Hóa Đặc Tả Gốc & Nghiệp Vụ Nền Tảng (Thư mục 01_ & 02_)                        │
│ • Viết lại Actor_KhachHang_Xem.md, Actor_Smart_FB_OS_Revised.md, Smart_FB_Operating_System.md    │
│ • Viết lại Workflow_Smart_FB_OS.md (thêm WF Delivery, Takeaway POS, WiFi attendance)             │
│ • Cập nhật BaoGia_KhachHang.md                                                                   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 2: Chuẩn Hóa Kiến Trúc & Sơ Đồ Mermaid (Thư mục 04_)                                   │
│ • Cập nhật Kiến trúc tổng quan (04_01)                                                           │
│ • Viết lại 5 Sơ đồ tuần tự Sequence Diagrams (04_02)                                             │
│ • Cập nhật Mermaid Database ERD 28 bảng (04_03)                                                  │
│ • Xóa bỏ hoàn toàn thư mục trùng lặp 05_Thiet_Ke_Kien_Truc_Diagrams/                             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 3: Chuẩn Hóa 9 Quy Trình Triển Khai Kỹ Thuật (Thư mục 03_)                             │
│ • Cập nhật 01_QUY_TRINH_PHAN_TICH_YEU_CAU (Scope MVP & Rules)                                    │
│ • Cập nhật 02_QUY_TRINH_THIET_KE_DATABASE (Schema 28 bảng chi tiết)                              │
│ • Cập nhật 03_QUY_TRINH_THIET_KE_API_CONTRACT & API_CONTRACT_CHI_TIET                            │
│ • Đại phẫu 04_THIET_KE_UI_UX_DESIGN_SYSTEM (Đặc biệt Chương 4 Staff Web POS & Chương 2 Delivery)│
│ • Cập nhật 05_BACKEND, 06_FRONTEND, 07_TESTING                                                   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 4: Chuẩn Hóa Test Cases, Seed Data, Roadmap & Audit Bàn Giao                           │
│ • Viết lại 05/02_KICH_BAN_DEMO_VA_UAT_TEST_CASES (Demo 5p chuẩn & 20+ UAT cases)                │
│ • Cập nhật 05/03_MOCHI_DATA_SEED_DEFINITION (Dữ liệu WiFi, Delivery, Takeaway, Loyalty)         │
│ • Cập nhật ROADMAP.md (8 Sprints 16 tuần chuẩn)                                                  │
│ • Viết lại DOC_AUDIT_REPORT.md (Báo cáo thẩm định toàn diện kết luận READY FOR CODING)           │
│ • Dọn dẹp các file rác tạm thời (temp_*.txt, ~$*.docx)                                           │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 KẾT LUẬN & BÀN GIAO

Bản đồ kiểm toán tài liệu `docs_audit_map.md` này đã hoàn thành việc rà soát và định vị chính xác:
1. **100% các điểm lệch nghiệp vụ** trên toàn bộ 31 tệp Markdown so với 5 Thay Đổi Nghiệp Vụ Cốt Lõi.
2. **Danh mục chi tiết từng tệp**: file title, purpose, outdated contents, required rewrites, sections to move to Scale Up, và cross-file dependencies.
3. **Mạng lưới phụ thuộc chéo (Dependency Matrix)** bảo đảm không bỏ sót bất kỳ điểm chạm nào trong quá trình sửa đổi.
4. **Lộ trình thực thi 4 giai đoạn** rõ ràng cho các tác vụ viết tài liệu tiếp theo.
