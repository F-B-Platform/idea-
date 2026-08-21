# BÁO CÁO KIỂM TOÁN TÀI LIỆU & PHÂN TÍCH LỖ HỔNG TOÀN DIỆN
## DỰ ÁN: SMART F&B OPERATING SYSTEM (SMART F&B OS)

> **Paper / Project**: Smart F&B Operating System (Smart F&B OS) — Comprehensive Documentation Audit & Engineering Gap Analysis  
> **Category**: Software Architecture, Enterprise Specifications & Quality Assurance Audit  
> **Segments Reviewed**: 6 Segments (29 Markdown files, 8 PDF/HTML/DOCX artifacts, Root Infrastructure & Environment files)  
> **Date**: 2026-08-14  
> **Target Audience**: 4 Developers (2 .NET 8 Backend, 2 Next.js 14 Frontend), System Architects & Project Stakeholders  
> **Synthesizer**: Lead Synthesizer (Teamwork Multi-Agent Documentation Review Track)  

---

# 1. TỔNG QUAN ĐÁNH GIÁ & KẾT LUẬN THẨM ĐỊNH (EXECUTIVE SUMMARY & FINAL VERDICT)

### 🔴 KẾT LUẬN THẨM ĐỊNH CHÍNH THỨC: **CHƯA ĐỦ ĐIỀU KIỆN VIẾT CODE NGAY (NOT READY FOR DIRECT CODING)**
**Cần giải quyết dứt điểm 7 điểm nghẽn kỹ thuật cốt tử (7 Critical Blockers) trước khi 4 lập trình viên bắt đầu Sprint 1.**

Hệ thống tài liệu dự án **Smart F&B Operating System** là một công trình đặc tả quy mô lớn, bao gồm **29 tệp Markdown**, 8 tài liệu phái sinh (PDF, HTML, DOCX), cùng hệ thống cấu hình Docker/Environment. Tài liệu thể hiện tầm nhìn nghiệp vụ sâu sắc, đón đầu xu hướng chuyển đổi số ngành F&B (loại bỏ máy POS truyền thống, tự phục vụ qua QR Menu PWA, điều phối bếp/bar bằng KDS thời gian thực, đối soát két tiền ca tự động, tích hợp thanh toán VietQR và ứng dụng AI Gemini).

Tuy nhiên, qua quá trình rà soát kiểm toán đa chiều của 6 chuyên viên phân tích độc lập, hệ thống tài liệu hiện tại tồn tại **nhiều mâu thuẫn kỹ thuật liên tầng (cross-layer inconsistencies), xung đột danh pháp mô hình dữ liệu (domain model drift), lỗ hổng bảo mật và những khoảng trống thực thi nghiêm trọng**. Nếu cho phép đội ngũ 4 kỹ sư (2 .NET 8 BE + 2 Next.js 14 FE) tiến hành viết code ngay lập tức, dự án chắc chắn sẽ rơi vào tình trạng phân mảnh kiến trúc, vỡ hợp đồng tích hợp API-Frontend, lỗi rò rỉ kết nối WebSocket SignalR và đứt gãy luồng thanh toán tự động.

---

### 🚨 7 ĐIỂM NGHẼN KỸ THUẬT CỐT TỬ (7 CRITICAL BLOCKERS) CẦN KHẮC PHỤC NGAY

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          7 ĐIỂM NGHẼN KỸ THUẬT CỐT TỬ (BLOCKERS TO CODE)                         │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. LƯỢC ĐỒ DATABASE RỖNG TRONG TÀI LIỆU QUY TRÌNH 02:                                            │
│    Tài liệu 02 chỉ liệt kê 28 tên bảng mà không có trường, kiểu dữ liệu, quan hệ FK hay Enum.   │
│ 2. XUNG ĐỘT CẤU TRÚC ENVELOPE API (CUSTOM ENVELOPE VS RFC 7807 PROBLEMDETAILS):                  │
│    Doc 03 bắt buộc {success, data} trong khi Doc 03_CHI_TIET dùng RFC 7807 & Direct DTOs.       │
│ 3. LỆCH PHA VÀ RÒ RỈ KẾT NỐI SIGNALR HUBS:                                                      │
│    Doc 04/05/02 vẽ 1 OrderHub chung, Doc 03_CHI_TIET định nghĩa 4 Hubs; code hook mẫu bị leak. │
│ 4. ĐỨT GÃY LUỒNG THANH TOÁN VIETQR WEBHOOK TỰ ĐỘNG:                                              │
│    Sơ đồ Sequence mô tả nhân viên duyệt tay; thiếu webhook callback HMAC-SHA256 & Idempotency.  │
│ 5. BẤT ĐỒNG BỘ DANH PHÁP MÔ HÌNH DỮ LIỆU (DOMAIN MODEL DRIFT):                                   │
│    Tài liệu dùng Branch/Product/Topping nhưng code C# dùng Restaurant/MenuItem/ModifierItem.     │
│ 6. NGHỊCH LÝ "KHÔNG MÁY POS" VS "OFFLINE MODE CẦN MÁY POS":                                      │
│    Slogan bỏ 100% POS nhưng kiến trúc ngoại tuyến lại đòi hỏi máy POS Sunmi SQLite độc quyền.    │
│ 7. THIẾU 75% DỮ LIỆU SEED DATA & MÃ C# INITIALIZER:                                              │
│    Seed Data chỉ có 6/28 bảng dạng text Markdown; thiếu DbInitializer.cs với GUIDs & mock JSON. │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# 2. TÓM TẮT HỆ THỐNG & ĐẶC TẢ BÀI TOÁN (PAPER & SYSTEM SUMMARY)

- **Tên Dự Án:** Smart F&B Operating System (Smart F&B OS).
- **Mục Tiêu Nghiệp Vụ:** Cung cấp nền tảng vận hành toàn diện cho các chuỗi Cà phê, Trà sữa và Nhà hàng vừa/nhỏ (1-10 chi nhánh). Giải quyết 8 nỗi đau lớn của ngành F&B Việt Nam: chi phí thiết bị POS đắt đỏ, sai sót ghi order thủ công, thất thoát doanh thu/nguyên liệu, quản lý ca làm và két tiền rời rạc, thiếu vắng báo cáo P&L tự động thời gian thực.
- **Kiến Trúc Kỹ Thuật Chuẩn Hóa:**
  - **Backend API:** .NET 8 C# Clean Architecture (4 dự án: `SmartFB.Domain`, `SmartFB.Application`, `SmartFB.Infrastructure`, `SmartFB.API`), ASP.NET Core SignalR, Entity Framework Core 8, MediatR CQRS, FluentValidation.
  - **Frontend Monorepo:** Next.js 14 App Router phân tách 5 Route Groups: `(customer)` cho QR Menu PWA, `(kds)` cho màn hình bếp/bar KDS, `(staff)` cho ứng dụng phục vụ di động, `(manager)` cho quản lý ca/kho, `(admin)` cho bảng điều khiển chuỗi.
  - **Cơ Sở Dữ Liệu & Caching:** PostgreSQL 16 (28 bảng thực thể, UUID PKs, Soft Delete, Auditing) + Redis 7 (Cache-aside, Distributed Lock, SignalR Redis Backplane).
  - **Hạ Tầng Triển Khai:** Docker Compose cô lập mạng `smartfb-net`, Nginx Reverse Proxy hỗ trợ SSL Certbot và WebSocket Upgrade headers.
  - **Tích Hợp Bên Thứ Ba:** Cổng thanh toán VietQR / PayOS động, Google Gemini 1.5 Flash API cho Module AI Analytics & Chatbot tư vấn món.

---

# 3. BẢN ĐỒ VẤN ĐỀ TRỌNG YẾU THEO PHÂN ĐOẠN (KEY ISSUES ROADMAP)

* **[Segment 1: Gốc & Roadmap]**: Tồn tại xung đột Tech Stack lịch sử (Node.js/Python vs .NET 8), nghịch lý "Không POS" vs yêu cầu máy POS Sunmi khi mất mạng, lỗ hổng Eat-and-Run do thiếu ràng buộc thanh toán trước/sau, rủi ro khách đăng ảnh phản cảm trực tiếp lên QR Menu do thiếu kiểm duyệt Feedback, và lỗi trùng lặp mã tính năng `C-21`.
* **[Segment 2: Báo giá & Skills]**: Mức báo giá 15 triệu VNĐ/4 tháng/4 devs là phi thực tế thương mại; báo giá cam kết nhiều dịch vụ ngoại vi (Zalo OA ZNS, SendGrid, Firebase, Offline Sync, Màn hình phụ POS) nhưng hoàn toàn không có thiết kế kỹ thuật trong API spec; thư mục `06_Danh_Sach_Skills` chỉ là bảng chỉ mục prompt AI Antigravity với đường dẫn máy cá nhân `C:\Users\nqtha\...` chứ không phải tài liệu quy chuẩn code.
* **[Segment 3: Quy trình Yêu cầu, DB & API]**: Xung đột nghiêm trọng giữa Custom Envelope `{success, data}` (Doc 03) và RFC 7807 ProblemDetails / Direct DTOs (Doc 03_CHI_TIET); tài liệu 02 để trống toàn bộ trường dữ liệu của 28 bảng; thiếu hoàn toàn User Stories, Acceptance Criteria (Given/When/Then) và chỉ số phi chức năng NFRs; thiếu các API CRUD Voucher, Upload Media và tra cứu Loyalty.
* **[Segment 4: Quy trình UI/UX, BE, FE, Test]**: Tài liệu Design System (1.294 dòng) rất xuất sắc nhưng 4 tài liệu quy trình còn lại quá sơ sài (<95 dòng); mã hook `useSignalR` bị lỗi kiến trúc nghiêm trọng gây rò rỉ WebSocket connections; thiếu ranh giới Server/Client Components, thiếu cấu hình Nginx WebSocket proxy headers và phương pháp AI Text-to-SQL tiềm ẩn lỗ hổng bảo mật SQL Injection nếu không có Read-only sandbox.
* **[Segment 5: Kiến trúc & Diagrams]**: Sơ đồ Clean Architecture vẽ mũi tên Application phụ thuộc Infrastructure (vi phạm DIP); sơ đồ Sequence VietQR mô tả duyệt tiền bằng mắt thay vì Webhook tự động; xung đột danh mục 28 bảng giữa ERD và Quy trình 03; biến môi trường trong tài liệu kiến trúc lệch với `.env.example` gốc; thiếu cấu hình `nginx.conf` cho SignalR trên môi trường Production.
* **[Segment 6: Quy chuẩn, Test cases & Seed data]**: Tồn tại xung đột danh pháp mô hình dữ liệu giữa tài liệu (`Branch/Product/Topping`) và mã nguồn C# thực tế (`Restaurant/MenuItem/ModifierItem`); Seed data mới có 6/28 bảng dạng text và mang tên Mochi nhưng nội dung là chuỗi Smart Coffee; bộ 15 test cases UAT quá đơn giản, thiếu 100% các kịch bản biên chí mạng (Concurrency, Kitchen Void, Split Bill, POS Offline, SignalR Reconnect, Webhook Replay); file `01_QUY_CHUAN_CODING...md` chỉ là redirect stub 12 dòng.

---

# 4. BẢNG KIỂM KÊ TOÀN BỘ TÀI LIỆU DỰ ÁN (COMPREHENSIVE FILE INVENTORY TABLE)

Bảng dưới đây thống kê và đánh giá toàn diện **tất cả 29 tệp Markdown, 8 tệp phái sinh/nhị phân và các tệp cấu hình hệ thống** trong thư mục `d:\Idea_DoAn`:

| STT | Đường Dẫn Tập Tin | Danh Mục Phân Loại | Định Dạng / Quy Mô | Trạng Thái Đánh Giá | Tóm Tắt Hiện Trạng & Vấn Đề Cốt Lõi |
|:---:|---|---|---|:---:|---|
| 1 | `ORIGINAL_REQUEST.md` | Baseline Specs | Markdown (4.3 KB / 85 dòng) | 🟢 **Complete** | Xác lập yêu cầu kiến trúc .NET 8, Next.js 14 Monorepo (5 Route Groups), Docker Compose, và quy chuẩn Pre-code. |
| 2 | `ROADMAP.md` | Roadmap & Planning | Markdown (19.9 KB / 485 dòng) | 🟢 **Complete** | Phân rã 8 Sprints (16 tuần) cho 4 devs rất khoa học. Cần chuẩn hóa AI dùng C# SDK gọi Gemini API thay vì Python microservice. |
| 3 | `01_Tai_Lieu_Dac_Ta_Goc/Actor_KhachHang_Xem.md` | Root Business Specs | Markdown (20.3 KB / 380 dòng) | 🟡 **Needs Improvement** | Tài liệu pitching khách hàng; thiếu cơ chế xác thực bảo vệ CRM/SĐT, thiếu kiểm duyệt ảnh feedback công khai. |
| 4 | `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS.md` | Root Business Specs | Markdown (19.2 KB / 395 dòng) | 🟡 **Needs Improvement** | Ma trận 4 Actor; gộp chung Barista và Phục vụ vào 1 Actor gây xung đột thao tác KDS; lệch đếm 24 vs 25 tính năng. |
| 5 | `01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md` | Root Business Specs | Markdown (66.5 KB / 882 dòng) | 🟡 **Needs Improvement** | Phân tích thị trường sâu sắc; tồn tại Tech Stack cũ (Node/Python), nghịch lý máy POS Sunmi ngoại tuyến, trùng mã tính năng `C-21`. |
| 6 | `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Smart_FB_OS.md` | Root Business Specs | Markdown (24.0 KB / 520 dòng) | 🟡 **Needs Improvement** | 16 sơ đồ luồng ASCII trực quan; thiếu luồng ngoại lệ (Error Flows), thiếu cơ chế Rollback đơn hủy và cảnh báo Eat-and-Run. |
| 7 | `01_Tai_Lieu_Dac_Ta_Goc/Actor_KhachHang_Xem.html` | Derived Artifact | HTML (29.4 KB) | 🟢 **Derived (Valid)** | Bản HTML xuất in ấn A4 từ `Actor_KhachHang_Xem.md`. CSS Inter chuyên nghiệp, nội dung khớp bản Markdown. |
| 8 | `01_Tai_Lieu_Dac_Ta_Goc/Actor_KhachHang_Xem.pdf` | Derived Artifact | PDF (287 KB) | 🟢 **Derived (Valid)** | Bản PDF đóng gói tài liệu Actor dành cho chủ đầu tư. |
| 9 | `01_Tai_Lieu_Dac_Ta_Goc/TomTat_HeThong_Smart_FB_OS.pdf` | Derived Artifact | PDF (88.8 KB) | 🟢 **Derived (Valid)** | Bản tóm tắt đồ họa sơ đồ vận hành hệ thống. |
| 10 | `01_Tai_Lieu_Dac_Ta_Goc/Tóm Tắt F&B.pdf` | Derived Artifact | PDF (88.8 KB) | 🔴 **Duplicate** | File trùng lặp 100% nội dung và kích thước với `TomTat_HeThong_Smart_FB_OS.pdf`. Đề xuất xóa để dọn rác repo. |
| 11 | `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.md` | Commercial Quotation | Markdown (18.6 KB / 350 dòng) | 🟡 **Needs Improvement** | Định giá 15tr quá thấp; cam kết vượt thiết kế kỹ thuật (Zalo OA, SendGrid, Firebase, Offline Sync, 2 màn hình POS); mâu thuẫn 4 vs 5 module AI. |
| 12 | `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.html` | Derived Artifact | HTML (32.1 KB) | 🟢 **Derived (Valid)** | Bản HTML báo giá in ấn A4. Thừa hưởng các bất cập phạm vi từ file Markdown gốc. |
| 13 | `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.docx` | Derived Artifact | MS Word (24.8 KB) | 🟢 **Derived (Valid)** | Tệp nhị phân Word xuất từ báo giá. Cần dọn lock file rác `~$oGia_KhachHang.docx`. |
| 14 | `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.pdf` | Derived Artifact | PDF (142 KB) | 🟢 **Derived (Valid)** | Bản PDF báo giá gửi khách hàng. |
| 15 | `02_Bao_Gia_Chi_Phi/BẢNG BÁO GIÁ TRIỂN KHAI HỆ THỐNG SMART F&B OS.pdf` | Derived Artifact | PDF (142 KB) | 🔴 **Duplicate** | Bản sao trùng khớp `BaoGia_KhachHang.pdf` nhưng có dấu tiếng Việt trong tên file, dễ lỗi CI/CD. Đề xuất xóa. |
| 16 | `03_Quy_Trinh_Trien_Khai/01_QUY_TRINH_PHAN_TICH_YEU_CAU.md` | Development Process | Markdown (3.8 KB / 88 dòng) | 🟡 **Needs Improvement** | Khoanh vùng 12 tính năng MVP tốt; thiếu 100% User Stories, Acceptance Criteria (Given/When/Then) và NFRs. |
| 17 | `03_Quy_Trinh_Trien_Khai/02_QUY_TRINH_THIET_KE_DATABASE.md` | Database Specs | Markdown (3.6 KB / 92 dòng) | 🔴 **Needs Improvement** | Chỉ liệt kê 28 tên bảng; thiếu 100% định nghĩa cột, kiểu dữ liệu, quan hệ FK, Enums, Soft Delete và Audit Trail. |
| 18 | `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT.md` | API Contract Overview | Markdown (4.1 KB / 98 dòng) | 🟡 **Needs Improvement** | Xung đột Envelope `{success, data}` với RFC 7807 trong file chi tiết; chỉ có 17 endpoints sơ lược và 2 hubs. |
| 19 | `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md` | Detailed API Specs | Markdown (124 KB / 2,505 dòng) | 🟢 **Complete (Exceptional)** | 64 REST endpoints, 4 SignalR Hubs, RFC 7807, JSON Schemas rất chuẩn mực. Chỉ thiếu CRUD Voucher, Upload Media & Loyalty endpoint. |
| 20 | `03_Quy_Trinh_Trien_Khai/04_QUY_TRINH_THIET_KE_UI_UX.md` | UI/UX Process | Markdown (4.8 KB / 95 dòng) | 🟡 **Needs Improvement** | Mô tả quy trình chung; Store Zustand sơ sài; lệch số lượng phân hệ (4 vs 5) so với Design System. |
| 21 | `03_Quy_Trinh_Trien_Khai/04_THIET_KE_UI_UX_DESIGN_SYSTEM.md` | Design System | Markdown (112 KB / 1,294 dòng) | 🟢 **Complete (Exceptional)** | 29 Wireframe ASCII, Design Tokens HSL/Hex, Typography, KDS Dark theme rất hoàn hảo. Cần bổ sung `tailwind.config.ts`. |
| 22 | `03_Quy_Trinh_Trien_Khai/05_QUY_TRINH_PHAT_TRIEN_BACKEND.md` | Backend Process | Markdown (3.4 KB / 88 dòng) | 🔴 **Needs Improvement** | Quá sơ lược; thiếu CQRS/MediatR pipeline, Result Pattern, Unit of Work, Optimistic Concurrency và Redis lock. |
| 23 | `03_Quy_Trinh_Trien_Khai/06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md` | Frontend Process | Markdown (3.1 KB / 82 dòng) | 🔴 **Needs Improvement** | Hook mẫu `useSignalR` bị lỗi gây memory leak và sập WebSocket; thiếu RSC vs Client boundary, thiếu TanStack Query v5 guide. |
| 24 | `03_Quy_Trinh_Trien_Khai/07_QUY_TRINH_TESTING_DEPLOYMENT.md` | QA & Deployment | Markdown (2.4 KB / 67 dòng) | 🔴 **Needs Improvement** | Thiếu mã test xUnit/Vitest; AI Text-to-SQL tiềm ẩn SQL Injection; thiếu multi-stage Dockerfile, Nginx WebSocket headers & CI/CD. |
| 25 | `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md` | Architecture Diagrams | Markdown (14.2 KB / 240 dòng) | 🟡 **Needs Improvement** | Sơ đồ Clean Architecture vẽ sai chiều phụ thuộc DIP; thiếu SignalR cho Manager; xuất hiện FCM nhưng không có cấu hình. |
| 26 | `04_Thiet_Ke_Kien_Truc_Diagrams/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md` | Sequence Diagrams | Markdown (16.8 KB / 280 dòng) | 🟡 **Needs Improvement** | Luồng VietQR thiếu Webhook tự động; Order gán ngay `Confirmed`; lệch tên Event SignalR so với API Contract 64 endpoints. |
| 27 | `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` | Database ERD | Markdown (18.5 KB / 320 dòng) | 🔴 **Needs Improvement** | Chỉ đặc tả trường cho 17/28 bảng (thiếu 11 bảng); xung đột danh mục 28 bảng với Folder 03; xung đột danh pháp với code C#. |
| 28 | `04_Thiet_Ke_Kien_Truc_Diagrams/04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md` | Infrastructure & Deploy | Markdown (12.3 KB / 210 dòng) | 🟡 **Needs Improvement** | Docker Compose mẫu dùng sai tên biến môi trường so với `.env.example`; thiếu Volume mount uploads; thiếu file `nginx.conf` mẫu. |
| 29 | `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md` | Coding Standards | Markdown (824 B / 12 dòng) | 🟡 **Needs Improvement** | File chuyển hướng tạm thời (12 dòng). Gây phân mảnh danh mục; cần tái cấu trúc thành tài liệu Linter/.editorconfig hoặc xóa. |
| 30 | `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md` | Git & PR Standards | Markdown (18.2 KB / 365 dòng) | 🟢 **Complete (Khá tốt)** | GitFlow, Commit, PR checklist, .env mẫu rất chi tiết. Cần sửa đường dẫn repo thực tế và hạ quy định 2 approvals xuống 1 cho feature PR. |
| 31 | `05_Quy_Chuan_&_Test_Cases/02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md` | UAT & Demo Cases | Markdown (11.5 KB / 240 dòng) | 🔴 **Needs Improvement** | Kịch bản demo 5 phút tốt nhưng 15 UAT cases quá sơ sài; thiếu 100% test cases biên (concurrency, offline, void, webhook replay, reconnect). |
| 32 | `05_Quy_Chuan_&_Test_Cases/03_MOCHI_DATA_SEED_DEFINITION.md` | Seed Data Specs | Markdown (14.6 KB / 290 dòng) | 🔴 **Needs Improvement** | Mới có 6/28 bảng dữ liệu dạng text; thiếu DbInitializer.cs với GUIDs; thiếu mock JSON; dữ liệu chuỗi Smart Coffee lệch tên file Mochi. |
| 33 | `06_Danh_Sach_Skills/DANH_SACH_SKILLS_TONG_QUAT.md` | Agent Skills Index | Markdown (4.9 KB / 115 dòng) | 🟡 **Needs Improvement** | Bảng chỉ mục kích hoạt Prompt AI Antigravity; không chứa quy chuẩn code thực tế; hardcode đường dẫn cá nhân `C:\Users\nqtha\...`. |
| 34 | `06_Danh_Sach_Skills/SKILLS_BACKEND_VA_KIEN_TRUC.md` | Agent Skills Index | Markdown (2.1 KB / 43 dòng) | 🟡 **Needs Improvement** | Chỉ mục AI prompt backend; thiếu code mẫu Clean Architecture/MediatR; hardcode đường dẫn cục bộ. |
| 35 | `06_Danh_Sach_Skills/SKILLS_DEVOPS_GIT_VA_RELEASE.md` | Agent Skills Index | Markdown (1.7 KB / 34 dòng) | 🟡 **Needs Improvement** | Chỉ mục AI prompt devops; sai đường dẫn thư mục kiến trúc (`05_` thay vì `04_Thiet_Ke_Kien_Truc_Diagrams`). |
| 36 | `06_Danh_Sach_Skills/SKILLS_FRONTEND_VA_UIUX.md` | Agent Skills Index | Markdown (1.8 KB / 35 dòng) | 🟡 **Needs Improvement** | Chỉ mục AI prompt frontend; thiếu hướng dẫn cấu hình Zustand Persist, SignalR Provider và React Query. |
| 37 | `06_Danh_Sach_Skills/SKILLS_TESTING_QA_VA_SECURITY.md` | Agent Skills Index | Markdown (1.9 KB / 35 dòng) | 🟡 **Needs Improvement** | Chỉ mục AI prompt QA; thiếu chỉ tiêu độ phủ Coverage định lượng và kịch bản tải k6 cụ thể. |
| 38 | `docker-compose.yml` (Root) | Infrastructure Config | YAML (1.2 KB / 38 dòng) | 🟡 **Needs Improvement** | Chỉ chứa Postgres & Redis cho local dev; thiếu cấu hình backend và frontend production containers. |
| 39 | `.env.example` (Root) | Environment Config | Text (1.8 KB / 48 dòng) | 🟢 **Complete** | Khai báo đầy đủ các biến môi trường cho Database, Redis, JWT, VietQR, PayOS, Gemini AI. |

---

# 5. PHÂN TÍCH LỖ HỔNG CHI TIẾT TỪNG TÀI LIỆU VÀ CHỈ DẪN LẬP TRÌNH VIÊN

---

## 5.1 Nhóm Tài Liệu 01 — Đặc Tả Gốc, Actor, Workflow & Roadmap

### `01_Tai_Lieu_Dac_Ta_Goc/Actor_KhachHang_Xem.md`
- **Điểm mạnh:** Văn phong truyền thông chuyên nghiệp, làm nổi bật giá trị tự động hóa F&B và cơ chế cảnh báo khẩn cấp khi đánh giá $\le 2$ sao.
- **Lỗ hổng trọng yếu:**
  - Định danh khách hàng chỉ qua số điện thoại thuần (Soft Identification) mà không có OTP. Nguy cơ người ngồi cùng bàn mạo danh số điện thoại để tiêu điểm Loyalty hoặc sử dụng voucher cá nhân của người khác.
  - Cho phép tải ảnh trực tiếp từ camera và công khai ngay lên trang chủ QR Menu mà không qua kiểm duyệt tự động (AI NSFW) hoặc duyệt tay của Quản lý, tạo nguy cơ phá hoại thương hiệu.
- **Chỉ dẫn cho Lập trình viên:**
  - **BE1 & BE2:** Cấu hình chính sách Soft Identification: Nhập SĐT chỉ cho phép xem menu cá nhân hóa và **Tích điểm (Accrue Points)**. Khi **Tiêu điểm (Redeem)** hoặc **Dùng Voucher**, bắt buộc nhân viên quầy quét xác nhận hoặc gửi OTP Zalo/SMS.
  - **FE1:** Bổ sung cờ `isApproved` khi hiển thị Review. Nếu review có ảnh hoặc $\le 3$ sao, đưa vào hàng đợi `Pending_Review` trên Manager App.

### `01_Tai_Lieu_Dac_Ta_Goc/Actor_Smart_FB_OS.md`
- **Điểm mạnh:** Phân chia mã định danh tính năng khoa học theo tiền tố (`C-xx`, `S-xx`, `M-xx`, `A-xx`) và phân bổ chính xác 5 module AI cho các nhóm người dùng.
- **Lỗ hổng trọng yếu:** Gộp chung Barista (Bếp) và Waiter (Phục vụ chạy bàn) vào 1 Actor duy nhất (`Staff`), gây xung đột thao tác trên KDS: Barista đổi trạng thái sang "Đang pha / Đã xong", trong khi Waiter chịu trách nhiệm bưng bê ra bàn và in bill.
- **Chỉ dẫn cho Lập trình viên:**
  - **BE1:** Tách Claim Role trong JWT Token thành 2 vai trò riêng: `Role = "Barista"` và `Role = "Waiter"`.
  - **FE1 & FE2:** Phân tách 2 màn hình: `/kds` (Dành cho màn hình cảm ứng bếp quầy pha chế) và `/staff/orders` (Giao diện mobile gọn nhẹ cho nhân viên chạy bàn).

### `01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md`
- **Điểm mạnh:** Tài liệu phân tích kinh doanh đồ sộ (882 dòng), chỉ ra chính xác thiệt hại tài chính từ 8 bất cập thực tế của F&B truyền thống.
- **Lỗ hổng trọng yếu:**
  - Xung đột Tech Stack lịch sử: Vẫn còn lưu thông tin dùng Node.js/NestJS, Python FastAPI, Flutter trong Mục 17, trái ngược với chuẩn .NET 8 / Next.js 14.
  - Nghịch lý không POS: Tuyên bố loại bỏ 100% chi phí máy POS, nhưng Mục 18 lại yêu cầu máy POS Sunmi 2 màn hình chạy SQLite khi mất mạng.
  - Trùng lặp mã tính năng `C-21` (Voucher Zalo vs Gọi thêm món).
- **Chỉ dẫn cho Lập trình viên:**
  - **Toàn đội:** Khóa cứng 100% Tech Stack: **.NET 8 Clean Architecture + Next.js 14 App Router + SignalR + PostgreSQL 16**.
  - **BE1 & FE2:** Triển khai cơ chế Offline POS chạy trên Web App (IndexedDB / LocalStorage trên Laptop hoặc Tablet của Quản lý) thay vì phụ thuộc phần cứng máy POS Sunmi độc quyền.
  - **BE2:** Đánh số lại tính năng thành `C-22 (Allergen)`, `C-23 (Quick Reorder)`, `C-24 (Gọi thêm món)`.

### `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Smart_FB_OS.md`
- **Điểm mạnh:** 16 sơ đồ ASCII Sequence trực quan từ `WF-00` đến `WF-15`.
- **Lỗ hổng trọng yếu:** Thiếu hoàn toàn luồng Rollback khi Barista từ chối đơn do hết nguyên liệu đột xuất; thiếu cơ chế xử lý khách gọi thêm món đợt 2 (Round 2) và cảnh báo Eat-and-Run cho mô hình trả sau.
- **Chỉ dẫn cho Lập trình viên:**
  - **BE1:** Thiết kế tách biệt 2 State Machine: `OrderStatus` (`Pending` -> `InPreparation` -> `Ready` -> `Completed` / `Cancelled`) và `PaymentStatus` (`Unpaid` -> `PendingConfirmation` -> `Paid` / `Refunded`).
  - **FE1 & FE2:** Thêm cảnh báo màu đỏ trên Sơ đồ bàn cho những bàn đã phục vụ xong món nhưng chưa thanh toán quá 15 phút.

### `ROADMAP.md`
- **Điểm mạnh:** Lộ trình 8 Sprints (16 tuần) cho 4 developers rất chi tiết và cân đối.
- **Lỗ hổng trọng yếu:** Sprint 6 ghi BE1 gọi Google Gemini API trực tiếp trong .NET 8, nhưng tài liệu gốc lại liệt kê các thư viện máy học Python phức tạp (Prophet, XGBoost).
- **Chỉ dẫn cho Lập trình viên:** Thống nhất tích hợp AI thông qua **Google Gemini 1.5 Flash API (C# SDK / REST Client với Structured Outputs)** trực tiếp trong `SmartFB.Application`, không dựng Python microservice riêng biệt.

---

## 5.2 Nhóm Tài Liệu 02 — Báo Giá Chi Phí & Danh Sách Skills

### `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.md`
- **Điểm mạnh:** Cung cấp phương án tài chính linh hoạt, phân tích bài toán hoàn vốn ROI và phân kỳ thanh toán 3 giai đoạn rõ ràng.
- **Lỗ hổng trọng yếu:**
  - Mức báo giá trọn gói 15.000.000 VNĐ cho 4 lập trình viên trong 4 tháng là bất khả thi về mặt kinh tế (tương đương ~937.500 VNĐ/người/tháng).
  - Cam kết nhiều tính năng "Phantom" (Zalo OA ZNS miễn phí, SendGrid Email, Firebase Push, Offline Sync tự động, POS 2 màn hình) mà không có thiết kế DTO/API Contract cụ thể trong hệ thống.
- **Chỉ dẫn cho Lập trình viên & PM:**
  - **PM / Hợp đồng:** Định vị bản báo giá 15tr là phiên bản MVP Đồ án Sinh viên / Khảo sát Thị trường. Với hợp đồng thương mại thực tế, cần tách các module Zalo ZNS, Chấm công sinh trắc học và AI Churn thành Phase 2 mở rộng; chi phí tin nhắn ZNS/SMS do khách hàng tự thanh toán cho nhà mạng.
  - **FE2:** Xây dựng tính năng POS 2 màn hình bằng **HTML5 `BroadcastChannel API`** giữa tab thu ngân và tab khách hàng trên trình duyệt.

### Thư mục `06_Danh_Sach_Skills/` (`DANH_SACH_SKILLS_TONG_QUAT.md` và 4 file con)
- **Điểm mạnh:** Danh mục tra cứu đầy đủ 8 nhóm năng lực AI Agent trong môi trường Antigravity.
- **Lỗ hổng trọng yếu:**
  - Toàn bộ các file chỉ là danh bạ Meta-Prompt gọi AI Agent, chứa các đường dẫn tuyệt đối máy cá nhân `C:\Users\nqtha\.gemini\config\skills\...`, hoàn toàn không chứa quy chuẩn lập trình thực tế cho con người.
  - Sai lệch liên kết thư mục kiến trúc (`05_Thiet_Ke_Kien_Truc_Diagrams/` thay vì `04_`).
- **Chỉ dẫn cho Lập trình viên:**
  - Thêm cảnh báo ở đầu file: Thư mục này là **Tài liệu Điều phối AI Prompt Registry**. Mọi quy chuẩn kỹ thuật thực tế cho 4 developers bắt buộc tham chiếu duy nhất tại thư mục `03_Quy_Trinh_Trien_Khai/` và `05_Quy_Chuan_&_Test_Cases/`.

---

## 5.3 Nhóm Tài Liệu 03 — Quy Trình Yêu Cầu, Thiết Kế Database & API Contract

### `03_Quy_Trinh_Trien_Khai/01_QUY_TRINH_PHAN_TICH_YEU_CAU.md`
- **Điểm mạnh:** Khoanh vùng chính xác 12 nhóm tính năng Tier 1 cốt lõi cho giai đoạn MVP.
- **Lỗ hổng trọng yếu:** Thiếu 100% User Stories, Acceptance Criteria (Given/When/Then) và các chỉ số phi chức năng NFRs (SLA, Latency, Concurrency, Idempotency).
- **Chỉ dẫn cho Lập trình viên:** Bổ sung 12 User Stories chuẩn kèm Acceptance Criteria và NFR Specifications (API p95 < 200ms cho Menu, < 500ms cho Đơn hàng, SignalR latency < 1.000ms, Concurrency 100 requests/giây).

### `03_Quy_Trinh_Trien_Khai/02_QUY_TRINH_THIET_KE_DATABASE.md`
- **Điểm mạnh:** Xác định 4 nguyên tắc nền tảng đúng đắn: UUID PK, Tiền tệ Decimal(12,0), Restrict FK, UTC DateTime.
- **Lỗ hổng trọng yếu:** File bị "rỗng ruột" hoàn toàn về mặt chi tiết: chỉ liệt kê 28 tên bảng mà không có bất kỳ định nghĩa cột, kiểu dữ liệu, quan hệ FK, Enums, hay cơ chế Soft Delete / Audit Trail nào.
- **Chỉ dẫn cho Lập trình viên:**
  - **BE2:** Sao chép và tích hợp toàn bộ bảng kê 28 thực thể chi tiết từ sơ đồ ERD sang tài liệu này.
  - **BE2:** Cấu hình Base Entity chuẩn cho 28 thực thể:
    ```csharp
    public abstract class BaseEntity {
        public Guid Id { get; set; } = Guid.NewGuid();
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public Guid? CreatedBy { get; set; }
        public DateTime? UpdatedAt { get; set; }
        public Guid? UpdatedBy { get; set; }
        public bool IsDeleted { get; set; } = false;
        public DateTime? DeletedAt { get; set; }
        public Guid? DeletedBy { get; set; }
    }
    ```
  - **BE2:** Khai báo trọn bộ C# Enums: `OrderStatus`, `PrepStatus`, `PaymentMethod`, `PaymentStatus`, `TableStatus`, `AppRoles`, `StockTransactionType`.

### `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT.md` (Tóm tắt)
- **Điểm mạnh:** Sơ đồ hóa quy trình phối hợp BE-FE nhanh gọn.
- **Lỗ hổng trọng yếu:** Xung đột trực tiếp với file chi tiết về cấu trúc Envelope phản hồi (`{ success, data }` vs RFC 7807 ProblemDetails / Direct DTOs) và số lượng SignalR Hubs (2 vs 4).
- **Chỉ dẫn cho Lập trình viên:** Đánh dấu file này là "Process Overview" và ghi chú rõ: **Mọi chuẩn Request/Response, Error RFC 7807 và Hubs bắt buộc tham chiếu duy nhất tại `03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md`**.

### `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md` (Chi tiết)
- **Điểm mạnh:** Tài liệu xuất sắc nhất dự án (2.505 dòng, 64 REST Endpoints, 4 SignalR Hubs, RFC 7807 ProblemDetails, JSON Schemas đầy đủ).
- **Lỗ hổng trọng yếu:** Thiếu Module CRUD Voucher (`/api/v1/vouchers`), Endpoint Upload ảnh Media (`/api/v1/media/upload`), Endpoint Khách xem điểm Loyalty (`/api/v1/customers/loyalty-profile`), và cơ chế xoay vòng Refresh Token.
- **Chỉ dẫn cho Lập trình viên:**
  - **BE1:** Bổ sung ngay 3 endpoints phụ trợ trên vào solution.
  - **BE1 & FE1/FE2:** Dùng trực tiếp JSON Schemas trong tài liệu này làm Single Source of Truth để sinh C# Record DTOs và TypeScript Interfaces.

---

## 5.4 Nhóm Tài Liệu 04 — Thiết Kế UI/UX, Backend, Frontend & Testing/Deployment

### `03_Quy_Trinh_Trien_Khai/04_THIET_KE_UI_UX_DESIGN_SYSTEM.md` & `04_QUY_TRINH_THIET_KE_UI_UX.md`
- **Điểm mạnh:** Design System đỉnh cao (1.294 dòng, 29 Wireframe ASCII, Design Tokens HSL/Hex, KDS High-contrast theme).
- **Lỗ hổng trọng yếu:** Thiếu file cấu hình `tailwind.config.ts` để sinh utility classes; thiếu TypeScript Props Interface cho 12 component UI dùng chung; chưa xử lý Autoplay Audio Policy trên trình duyệt khi KDS phát chuông báo.
- **Chỉ dẫn cho Lập trình viên:**
  - **FE1:** Cung cấp file `tailwind.config.ts` tích hợp toàn bộ biến CSS `:root`.
  - **FE1:** Định nghĩa chuẩn Props Interface cho 12 Shared Components (`Button`, `Modal`, `VietQRBox`, `TimerBanner`...).
  - **FE1:** Xây dựng nút "Bắt đầu ca làm (Bật âm thanh)" trên KDS để mở khóa AudioContext trình duyệt.

### `03_Quy_Trinh_Trien_Khai/05_QUY_TRINH_PHAT_TRIEN_BACKEND.md`
- **Điểm mạnh:** Xác định cấu trúc 4 tầng Clean Architecture cho .NET 8.
- **Lỗ hổng trọng yếu:** Quá ngắn (88 dòng); thiếu hướng dẫn triển khai MediatR Pipeline Behaviors, thiếu Result Pattern Monad (ném Exception tràn lan), thiếu Unit of Work và thiếu giải pháp Optimistic Concurrency (`xmin` / `RowVersion`).
- **Chỉ dẫn cho Lập trình viên:**
  - **BE1:** Cấu hình `MediatR` với `ValidationBehavior` và `LoggingBehavior`.
  - **BE1:** Triển khai lớp `Result<T>` và `Error` monad, loại bỏ việc ném Exception cho các lỗi nghiệp vụ thông thường.
  - **BE2:** Cấu hình Concurrency Token `builder.Property(o => o.Version).IsRowVersion()` hoặc `xmin` trên các bảng `Orders`, `CashShifts`, `InventoryStocks`.

### `03_Quy_Trinh_Trien_Khai/06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md`
- **Điểm mạnh:** Chiến lược Mock-First và cấu trúc Route Groups Next.js 14 rõ ràng.
- **Lỗ hổng trọng yếu:** Đoạn mã custom hook `useSignalR` bị lỗi thiết kế nghiêm trọng (tạo mới kết nối WebSocket trên mỗi component gây cạn kiệt tài nguyên); thiếu ranh giới RSC vs Client Components; thiếu Next.js Middleware RBAC Guard.
- **Chỉ dẫn cho Lập trình viên:**
  - **FE1 & FE2:** Xóa bỏ hoàn toàn hook `useSignalR` lỗi. Thay thế bằng **`SignalRProvider` Singleton** bao bọc toàn ứng dụng và hook `useSignalREvent`.
  - **FE2:** Viết file `middleware.ts` kiểm tra JWT Cookie/Bearer token để chặn truy cập trái phép vào route nhóm `(admin)` và `(staff)`.

### `03_Quy_Trinh_Trien_Khai/07_QUY_TRINH_TESTING_DEPLOYMENT.md`
- **Điểm mạnh:** Phác thảo chiến lược test 3 cấp độ và kiến trúc Docker 4 containers.
- **Lỗ hổng trọng yếu:** Tính năng AI Text-to-SQL thực thi trực tiếp trên database chính tiềm ẩn nguy cơ **SQL Injection / Rò rỉ dữ liệu**; thiếu cấu hình Nginx WebSocket upgrade headers; thiếu Dockerfile multi-stage và CI/CD workflow.
- **Chỉ dẫn cho Lập trình viên:**
  - **BE2:** Tạo User Database riêng biệt `smartfb_ai_readonly` chỉ có quyền `SELECT` trên các Views doanh thu đã được ẩn thông tin cá nhân.
  - **BE1:** Cung cấp file cấu hình `nginx.conf` chuẩn có đầy đủ `proxy_set_header Upgrade $http_upgrade` và `proxy_set_header Connection "upgrade"`.

---

## 5.5 Nhóm Tài Liệu 05 — Sơ Đồ Kiến Trúc, Workflow Sequence, ERD & Deploy

### `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md`
- **Điểm mạnh:** Sơ đồ 4 tầng và C4 Model trực quan.
- **Lỗ hổng trọng yếu:** Sơ đồ Clean Architecture vẽ sai chiều phụ thuộc (`Application -> Infrastructure`); thiếu kênh SignalR cho Manager Dashboard.
- **Chỉ dẫn cho Lập trình viên:** Đảo ngược mũi tên quan hệ: `Infrastructure -> Application` và `Infrastructure -> Domain`. Mở kết nối `NotificationHub` cho Manager Dashboard để nhận cảnh báo két tiền và bàn gọi phục vụ.

### `04_Thiet_Ke_Kien_Truc_Diagrams/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md`
- **Điểm mạnh:** 5 Sequence Diagrams Mermaid chi tiết về luồng nghiệp vụ chính.
- **Lỗ hổng trọng yếu:** Luồng VietQR mô tả nhân viên nhìn app ngân hàng rồi bấm duyệt tay (thiếu Webhook tự động); tên sự kiện SignalR bị lệch so với API Contract chi tiết (`NewOrder` vs `OrderCreated`).
- **Chỉ dẫn cho Lập trình viên:** Cập nhật Sequence Diagram 3 theo đúng luồng: Bank Server gửi Webhook `POST /api/v1/payments/webhook/vietqr` -> Backend verify chữ ký HMAC-SHA256 -> Tự động đổi trạng thái -> Broadcast SignalR `PaymentConfirmed`.

### `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md`
- **Điểm mạnh:** Sơ đồ ERD kết nối 28 bảng theo 5 phân hệ logic.
- **Lỗ hổng trọng yếu:** Thiếu định nghĩa trường thuộc tính cho 11/28 bảng; xung đột danh pháp (`Branch/Product/Topping` vs `Restaurant/MenuItem/ModifierItem`).
- **Chỉ dẫn cho Lập trình viên:** Bổ sung trường chi tiết cho 11 bảng còn thiếu và thống nhất 100% danh pháp **F&B Hiện đại (`Branch`, `Product`, `Topping`, `CashShift`)**.

### `04_Thiet_Ke_Kien_Truc_Diagrams/04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md` & Docker Root
- **Điểm mạnh:** Thiết kế mạng Docker cô lập và volume mount bền vững.
- **Lỗ hổng trọng yếu:** Tên biến môi trường lệch chuẩn so với `.env.example` gốc (`${DATABASE_NAME}` vs `${POSTGRES_DB}`); thiếu volume mount ảnh upload `/var/smartfb/uploads`.
- **Chỉ dẫn cho Lập trình viên:** Đồng bộ 100% tên biến môi trường trong file `docker-compose.production.yml` theo đúng `.env.example`. Khai báo volume `uploads_data:/var/smartfb/uploads`.

---

## 5.6 Nhóm Tài Liệu 06 — Quy Chuẩn Code, Git, UAT Test Cases & Seed Data

### `05_Quy_Chuan_&_Test_Cases/01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md` & `01_QUY_CHUAN_CODING...md`
- **Điểm mạnh:** Hướng dẫn GitFlow, Conventional Commits, và `.env.example` hơn 40 biến rất hoàn chỉnh.
- **Lỗ hổng trọng yếu:** Sai đường dẫn thư mục code thực tế (`src/Backend/SmartFnB.Api` vs `backend/src/SmartFB.API`); quy định 2 approvals quá nặng cho team 4 người; thiếu file `.editorconfig` chuẩn hóa.
- **Chỉ dẫn cho Lập trình viên:**
  - Sửa đường dẫn thành `backend/src/SmartFB.API` và `frontend/`.
  - Điều chỉnh chính sách PR: Feature PR vào `develop` chỉ cần **1 Approval** từ peer dev; Release PR vào `main` cần **2 Approvals** (Lead BE + Lead FE).
  - Tích hợp file `.editorconfig` vào root repository.

### `05_Quy_Chuan_&_Test_Cases/02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md`
- **Điểm mạnh:** Kịch bản Demo 5 phút liền mạch, bám sát nghiệp vụ bảo vệ đồ án.
- **Lỗ hổng trọng yếu:** 15 test cases UAT quá sơ sài; thiếu 100% các ca kiểm thử biên (concurrency tại 1 bàn, bếp hủy món hoàn tiền, tách/gộp bill, POS mất mạng, SignalR reconnect, webhook replay).
- **Chỉ dẫn cho Lập trình viên:** Mở rộng bộ test UAT lên tối thiểu **35 test cases chi tiết** có đầy đủ Pre-conditions, Request Payload JSON, Expected Database State và Expected SignalR Event Assertions.

### `05_Quy_Chuan_&_Test_Cases/03_MOCHI_DATA_SEED_DEFINITION.md`
- **Điểm mạnh:** Dữ liệu món ăn chi tiết, có định lượng pha chế và cảnh báo dị ứng.
- **Lỗ hổng trọng yếu:** Mới có 6/28 bảng; thiếu mã C# `DbInitializer.cs` với Static GUIDs; thiếu file `seed-data.json`; tên file Mochi nhưng dữ liệu là chuỗi Smart Coffee.
- **Chỉ dẫn cho Lập trình viên:**
  - Đổi tên file thành `03_SEED_DATA_SPECIFICATION_SMART_COFFEE.md`.
  - Viết toàn văn mã nguồn `DbInitializer.cs` nạp đủ 28 bảng dữ liệu với Static Deterministic GUIDs.
  - Tạo file `seed-data.json` cho Frontend làm Mock Server.

---

# 6. TỔNG HỢP CÁC LỖ HỔNG XUYÊN SUỐT VÀ GIẢI PHÁP KIẾN TRÚC ĐỒNG BỘ (SYNTHESIZED CROSS-CUTTING GAPS)

---

## 6.1 Chuẩn Hóa Envelope Phản Hồi API (Single Source of Truth: RFC 7807)

- **Xung đột:** Tài liệu 03 yêu cầu bọc wrapper `{ success, data, error }`, trong khi tài liệu 03_CHI_TIET trả về trực tiếp DTO và dùng RFC 7807 cho lỗi.
- **Giải pháp thống nhất:**
  - **Phản hồi thành công (HTTP 200/201):** Trả về trực tiếp DTO Model. Danh sách phân trang trả về:
    ```json
    {
      "totalCount": 150,
      "page": 1,
      "pageSize": 20,
      "totalPages": 8,
      "items": [ { "id": "...", "name": "..." } ]
    }
    ```
  - **Phản hồi lỗi (HTTP 4xx / 5xx):** 100% sử dụng chuẩn **RFC 7807 ProblemDetails** của ASP.NET Core:
    ```json
    {
      "type": "https://smartfb.vn/errors/out-of-stock",
      "title": "Item Out of Stock",
      "status": 400,
      "detail": "Nguyên liệu pha chế Bạc Xỉu tại chi nhánh Q1 đã hết.",
      "instance": "/api/v1/orders",
      "invalidParams": [
        { "name": "items[0].productId", "reason": "Insufficient inventory stock" }
      ]
    }
    ```

---

## 6.2 Giải Quyết Nghịch Lý "Không POS" vs "Offline Mode"

- **Mâu thuẫn:** Tuyên bố không cần máy POS nhưng chế độ ngoại tuyến lại yêu cầu máy POS Sunmi.
- **Giải pháp thống nhất:**
  - **Triển khai PWA Offline:** Chế độ bán hàng ngoại tuyến được tích hợp trực tiếp vào Web App POS chạy trên Laptop hoặc Tablet của Quản lý thông qua **HTML5 IndexedDB + Service Worker Cache-First**.
  - **Luồng hoạt động khi mất mạng:**
    1. Quản lý tạo đơn offline trên Tablet -> Dữ liệu lưu vào hàng đợi IndexedDB với `ClientOrderUuid`.
    2. In hóa đơn tạm qua máy in nhiệt LAN/Bluetooth nội bộ.
    3. Khi có mạng trở lại -> Service Worker tự động gọi `POST /api/v1/orders/sync-offline` đẩy hàng loạt đơn lên Cloud kèm cơ chế Idempotency chống trùng lặp.

---

## 6.3 Kiến Trúc SignalR Hubs: Tách 4 Hubs Chuyên Biệt & Singleton Provider Chống Rò Rỉ

- **Vấn đề:** Sơ đồ vẽ 1 Hub chung; mã hook frontend cũ tạo mới kết nối trên từng component gây sập server.
- **Giải pháp thống nhất:**
  - **Phía Backend (.NET 8):** Phân tách 4 Hubs độc lập kế thừa Strongly-Typed Interfaces:
    - `/hubs/order` (`IOrderHubClient`): Giao tiếp giữa Khách hàng PWA, Thu ngân và Nhân viên phục vụ.
    - `/hubs/kitchen` (`IKitchenHubClient`): Dành riêng cho màn hình Bếp/Bar KDS (`NewTicketReceived`, `ItemBumped`, `Item86Alert`).
    - `/hubs/table` (`ITableHubClient`): Cập nhật trạng thái đổi màu sơ đồ bàn ăn (`TableStatusChanged`).
    - `/hubs/payment` (`IPaymentHubClient`): Bắn thông báo khớp lệnh thanh toán (`PaymentConfirmed`).
  - **Phía Frontend (Next.js 14):** Sử dụng **`SignalRProvider` Singleton Context** khởi tạo duy nhất 1 kết nối WebSocket cho toàn bộ phiên làm việc, hỗ trợ tự động kết nối lại (`withAutomaticReconnect`) và lắng nghe sự kiện qua hook an toàn `useSignalREvent`.

---

## 6.4 Tự Động Hóa Luồng Thanh Toán VietQR Webhook & Bảo Mật HMAC-SHA256

- **Vấn đề:** Tài liệu Sequence cũ thiếu luồng webhook tự động, yêu cầu nhân viên nhìn app ngân hàng rồi bấm duyệt tay.
- **Giải pháp thống nhất:**
  - Backend cung cấp endpoint công khai `POST /api/v1/payments/webhook/vietqr`.
  - Khi ngân hàng khớp lệnh chuyển tiền -> Cổng thanh toán gửi Webhook Payload kèm chữ ký `X-Webhook-Signature`.
  - Backend xác thực chữ ký HMAC-SHA256 bằng `WebhookSecretKey`, kiểm tra Idempotency Key chống cộng trùng tiền, cập nhật `PaymentStatus = Paid`, `OrderStatus = InPreparation`, và broadcast tức thì sự kiện `PaymentConfirmed` qua `PaymentHub` xuống PWA khách và POS thu ngân.

---

## 6.5 Thống Nhất Danh Pháp Mô Hình Dữ Liệu (Ubiquitous Language Dictionary)

- **Xung đột:** Xung đột danh pháp giữa Tài liệu/ERD (`Branch`, `Product`, `Topping`, `CashShift`) và Mã nguồn C# (`Restaurant`, `MenuItem`, `ModifierItem`, `CashDrawer`).
- **Giải pháp thống nhất:** Toàn bộ 4 lập trình viên cam kết tuân thủ 100% bộ từ vựng chuẩn **F&B Hiện đại** trên toàn bộ tầng Database, DTOs, API URLs và Frontend Types:

| Khái Niệm Nghiệp Vụ | C# Entity (.NET 8) | API REST Route | TypeScript Interface (Next.js 14) |
|---|---|---|---|
| Chi nhánh cửa hàng | `Branch` | `/api/v1/branches` | `Branch` |
| Danh mục thực đơn | `Category` | `/api/v1/categories` | `Category` |
| Sản phẩm / Món ăn | `Product` | `/api/v1/products` | `Product` |
| Biến thể kích cỡ (Size) | `ProductVariant` | `/api/v1/products/{id}/variants` | `ProductVariant` |
| Topping thêm | `Topping` | `/api/v1/toppings` | `Topping` |
| Định lượng nguyên liệu | `ProductIngredient` | `/api/v1/products/{id}/ingredients` | `ProductIngredient` |
| Bàn ăn | `Table` | `/api/v1/tables` | `Table` |
| Đơn hàng | `Order` | `/api/v1/orders` | `Order` |
| Món trong đơn | `OrderItem` | `/api/v1/orders/{id}/items` | `OrderItem` |
| Giao dịch thanh toán | `Payment` | `/api/v1/payments` | `Payment` |
| Ca làm & Két tiền | `CashShift` | `/api/v1/cash-shifts` | `CashShift` |
| Tồn kho nguyên liệu | `InventoryStock` | `/api/v1/inventory/stocks` | `InventoryStock` |
| Phiếu xuất nhập kho | `StockTransaction` | `/api/v1/inventory/transactions` | `StockTransaction` |

---

## 6.6 Định Vị Rõ Ràng Bản Chất Thư Mục `06_Danh_Sach_Skills`

- Thư mục `06_Danh_Sach_Skills` được định vị chính thức là **Trạm Chỉ Mục Điều Phối Prompt AI Agent (Antigravity Meta-Prompt Index)**.
- Mọi tài liệu kỹ thuật có tính chất bắt buộc thi hành cho lập trình viên con người (Coding Conventions, PR Checklist, Database Schema, API Contracts, Wireframes) nằm độc quyền tại **Thư mục 03, 04 và 05**.

---

## 6.7 An Toàn Dữ Liệu & Phân Vùng AI Text-to-SQL Analytics

- **Rủi ro:** Module AI tự sinh câu lệnh SQL truy vấn báo cáo có nguy cơ bị tấn công Prompt Injection hoặc vô tình thực thi lệnh sửa đổi dữ liệu (`DROP`, `DELETE`, `UPDATE`).
- **Giải pháp bảo mật:**
  1. Tạo tài khoản Database riêng biệt `smartfb_ai_readonly` chỉ được cấp quyền `GRANT SELECT` trên các Views phân tích dữ liệu tổng hợp.
  2. Áp dụng Regex Filter tại Backend: Chặn đứng mọi câu truy vấn chứa các từ khóa nguy hiểm (`INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`, `TRUNCATE`, `EXEC`, `GRANT`).
  3. Mọi dữ liệu trả về cho LLM đều được ẩn danh hóa (Masking PII: số điện thoại, mật khẩu, thông tin thanh toán).

---

# 7. KẾ HOẠCH HÀNH ĐỘNG PHÂN VAI CHO 4 LẬP TRÌNH VIÊN (ROLE-SPECIFIC ACTION PLANS)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               MA TRẬN PHÂN VAI VÀ NHIỆM VỤ 4 DEVELOPERS                         │
├───────────────────────────────┬─────────────────────────────────────────────────────────────────┤
│ [BE1] BACKEND LEAD ARCHITECT  │ • Solution Clean Architecture .NET 8 + MediatR + Result Pattern │
│ (Core, Auth, SignalR, PayOS)  │ • Triển khai 4 SignalR Hubs (Order, Kitchen, Table, Payment)    │
│                               │ • Tích hợp Webhook VietQR tự động & Verify HMAC-SHA256          │
│                               │ • Xây dựng Global Exception Handler trả về RFC 7807             │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────┤
│ [BE2] BACKEND DATA & SERVICES │ • Tạo 28 Entity classes kế thừa BaseEntity (UUID, Soft Delete)  │
│ (DB, EF Core, Inventory, AI)  │ • Viết DbInitializer.cs với Static GUIDs nạp dữ liệu mẫu        │
│                               │ • Logic trừ kho tự động theo công thức ProductIngredient        │
│                               │ • Xử lý đối soát két tiền ca làm CashShift & AI Analytics       │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────┤
│ [FE1] FRONTEND PWA & KDS LEAD │ • Dựng UI QR Menu PWA chạm vuốt mobile-first & giỏ hàng         │
│ (Customer PWA, KDS, UI Kit)   │ • Cấu hình tailwind.config.ts & 12 Shared UI Components         │
│                               │ • Xây dựng SignalRProvider Singleton chống rò rỉ WebSocket      │
│                               │ • Màn hình KDS Bếp Kanban đổi màu real-time & âm báo chuông     │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────┤
│ [FE2] FRONTEND POS & ADMIN    │ • Màn hình Sơ đồ bàn ăn POS Thu ngân đổi màu real-time          │
│ (POS, Staff, Manager, Admin)  │ • Tích hợp BroadcastChannel API cho màn hình phụ POS 2 màn hình │
│                               │ • Form Mở/Kết ca đối soát két tiền lệch & Báo cáo P&L           │
│                               │ • Cấu hình Next.js 14 Middleware.ts bảo vệ Route Groups         │
└───────────────────────────────┴─────────────────────────────────────────────────────────────────┘
```

---

# 8. TOÀN VĂN BÁO CÁO CHI TIẾT TỪ 6 CHUYÊN VIÊN PHÂN TÍCH (DETAILED SEGMENT REPORTS)

Dưới đây là bản sao nguyên văn toàn bộ 6 báo cáo đánh giá chuyên sâu từ các chuyên viên phân tích theo đúng thứ tự xuất hiện của các phân đoạn tài liệu:

---

## 8.1 Báo Cáo Chi Tiết Phân Đoạn 1: `segment_01_goc_va_roadmap`

*(Nguồn: `d:\Idea_DoAn\.agents\teamwork_preview_worker_seg1\unit_report_segment_01_goc_va_roadmap.md`)*

```markdown
# BÁO CÁO RÀ SOÁT & ĐÁNH GIÁ KỸ THUẬT TOÀN DIỆN (UNIT AUDIT REPORT)
## PHÂN ĐOẠN 1: TÀI LIỆU ĐẶC TẢ GỐC, ACTOR, WORKFLOW & ROADMAP TRIỂN KHAI
**Dự án:** Smart F&B Operating System (Smart F&B OS)  
**Đối tượng bàn giao:** Đội ngũ phát triển (2 Backend .NET 8, 2 Frontend Next.js 14)  
**Mã phân đoạn:** `segment_01_goc_va_roadmap`  
**Ngày đánh giá:** 14/08/2026  
**Chuyên gia thẩm định:** Document Review Analyst & Forensic Software Architect  

---

# 1. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

Tài liệu Phân đoạn 1 là khối nền tảng thiết lập bối cảnh nghiệp vụ, định vị bài toán thị trường, phân định 4 nhóm Actor người dùng, thiết lập 16 luồng vận hành cốt lõi (Workflow WF-00 đến WF-15) và xây dựng Kế hoạch hành động 16 tuần (8 Sprints) cho đội ngũ 4 kỹ sư.

### Kết quả đánh giá tổng quát:
1. **Giá trị cốt lõi & Điểm mạnh:**
   - Xác định bài toán kinh doanh rõ ràng: Chuyển đổi mô hình gọi món truyền thống (xếp hàng, gõ POS, sai sót order) sang mô hình **QR Self-Ordering tại bàn kết hợp KDS thời gian thực và quản trị chuỗi thông minh**.
   - Định hình hoàn chỉnh 4 nhóm Actor: Khách hàng (PWA), Barista/Phục vụ (KDS + Mobile App), Quản lý chi nhánh (Manager Web/App), Chủ chuỗi (Admin Web Dashboard) với 71 tính năng vận hành và 5 phân hệ AI.
   - Lộ trình phát triển trong `ROADMAP.md` được phân rã khoa học theo mô hình Scrum/Sprint (8 Sprints, 16 tuần), phân định ranh giới công việc chi tiết giữa 2 Backend devs (.NET 8) và 2 Frontend devs (Next.js 14).

2. **Các rủi ro kỹ thuật & Lỗ hổng nghiệp vụ trọng yếu (Critical Gaps):**
   - **Xung đột Tech Stack lịch sử:** `Smart_FB_Operating_System.md` còn lưu dấu vết công nghệ cũ (Node.js/NestJS, Python FastAPI, Flutter), trong khi `ROADMAP.md` và `ORIGINAL_REQUEST.md` đã chuẩn hóa sang **.NET 8 Clean Architecture + Next.js 14 Monorepo (5 Route Groups)**.
   - **Nghịch lý "Không POS" vs "Offline Mode cần máy POS":** Slogan hệ thống khẳng định loại bỏ 100% phần cứng POS đắt tiền, nhưng tài liệu kiến trúc ngoại tuyến (Lớp 2) lại yêu cầu máy POS Sunmi chạy SQLite cục bộ.
   - **Rủi ro Eat-and-Run (Dine & Dash) trong luồng Post-pay:** Luồng đặt món `WF-01` vận hành theo cơ chế "Đặt món -> Pha chế -> Uống -> Yêu cầu bill -> Thu tiền". Không có cơ chế ràng buộc thanh toán trước (Pre-pay) hoặc định danh tín nhiệm khách hàng, tạo lỗ hổng thất thoát doanh thu nghiêm trọng cho quán tự phục vụ.
   - **Thiếu máy trạng thái đơn hàng (Order State Machine) & Luồng hủy/hoàn tiền:** Chưa đặc tả trạng thái chi tiết khi Barista từ chối đơn do hết nguyên liệu, khách hủy đơn giữa chừng, hoặc thanh toán VietQR thất bại/treo giao dịch.
   - **Rủi ro kiểm duyệt đánh giá công khai (Unmoderated Public Reviews):** `WF-05` công khai ngay lập tức đánh giá ẩn danh và ảnh chụp của khách lên QR Menu mà không qua hàng đợi duyệt (Moderation Queue) hay bộ lọc ngôn từ/hình ảnh phản cảm.
   - **Lỗi trùng lặp mã tính năng (ID Collision):** Trong `Smart_FB_Operating_System.md`, nhóm tính năng nâng cao bị trùng mã `C-21` (Nhận voucher Zalo vs Gọi thêm món), dẫn đến lệch tổng số lượng tính năng thực tế (25 tính năng thay vì 24).

---

# 2. BẢNG KIỂM KÊ TÀI LIỆU & TRẠNG THÁI (FILE INVENTORY & STATUS TABLE)

| STT | Đường Dẫn File | Định Dạng / Dung Lượng | Trạng Thái Đánh Giá | Tóm Tắt Vấn Đề Trọng Yếu |
|---|---|---|---|---|
| 1 | `d:\Idea_DoAn\ORIGINAL_REQUEST.md` | Markdown (4.3 KB) | **Hoàn thiện (Complete)** | Xác lập đầy đủ phạm vi bài toán ban đầu, quy chuẩn đầu ra Pre-Code và yêu cầu khởi tạo bộ khung Docker, .NET 8, Next.js 14. |
| 2 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Xem.md` | Markdown (20.3 KB) | **Cần cải thiện (Needs Improvement)** | Bản tài liệu pitching cho khách hàng/nhà đầu tư. Thiếu đặc tả kỹ thuật về xử lý bảo mật SĐT (OTP/Session) và cơ chế chống spam đánh giá. |
| 3 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Smart_FB_OS.md` | Markdown (19.2 KB) | **Cần cải thiện (Needs Improvement)** | Phân định 4 Actor chi tiết nhưng gộp chung Barista và Nhân viên chạy bàn vào 1 Actor duy nhất; thiếu ranh giới phân quyền khi nhiều NV cùng thao tác 1 ca. |
| 4 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md` | Markdown (66.5 KB) | **Cần cải thiện (Needs Improvement)** | Tài liệu tổng thể chi tiết nhất (882 dòng), nhưng tồn tại xung đột Tech Stack (Node/Python vs .NET 8), trùng mã tính năng `C-21`, mâu thuẫn phần cứng Offline POS. |
| 5 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Smart_FB_OS.md` | Markdown (24.0 KB) | **Cần cải thiện (Needs Improvement)** | 16 Workflow mô tả trực quan dạng ASCII, nhưng thiếu luồng ngoại lệ (Error Flows), thiếu Rollback khi giao dịch thất bại, và thiếu State Transition Diagram. |
| 6 | `d:\Idea_DoAn\ROADMAP.md` | Markdown (19.9 KB) | **Hoàn thiện (Complete - Rất tốt)** | Phân rã 8 Sprints cho 4 Devs rất chặt chẽ. Cần đồng bộ hóa cách triển khai AI (Gemini API trong .NET 8 thay vì Python microservice riêng biệt). |
| 7 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Xem.html` | HTML (29.4 KB) | **Tài liệu phái sinh (Derived)** | Bản xuất HTML định dạng in ấn/A4 từ `Actor_KhachHang_Xem.md`. CSS Inter chuyên nghiệp, nội dung khớp 100% với bản Markdown. |
| 8 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Xem.pdf` | PDF (287 KB) | **Tài liệu phái sinh (Derived)** | Bản in PDF đóng gói tài liệu Actor dành cho khách hàng/chủ đầu tư. |
| 9 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\TomTat_HeThong_Smart_FB_OS.pdf` | PDF (88.8 KB) | **Tài liệu phái sinh (Derived)** | Tóm tắt trực quan sơ đồ vận hành hệ thống. |
| 10 | `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tóm Tắt F&B.pdf` | PDF (88.8 KB) | **File trùng lặp (Duplicate)** | Bản sao trùng khớp nội dung với `TomTat_HeThong_Smart_FB_OS.pdf` (cùng kích thước 88,848 bytes). Đề xuất dọn dẹp để tránh rác workspace. |

---

# 3. PHÂN TÍCH LỖ HỔNG CHI TIẾT TỪNG TÀI LIỆU (FILE-BY-FILE GAP ANALYSIS)

## 3.1 Đánh giá: `d:\Idea_DoAn\ORIGINAL_REQUEST.md`
### A. Điểm mạnh (Strengths)
- Xác lập mục tiêu rất rõ ràng: Không code khi chưa hoàn thiện 100% tài liệu đặc tả, JSON Schemas cho 45+ endpoints, UI/UX tokens và Git workflow.
- Bản cập nhật Follow-up xác định chuẩn xác cấu trúc kỹ thuật: Docker Compose (PostgreSQL 16 + Redis 7), Solution .NET 8 Clean Architecture (4 projects: Domain, Infrastructure, Application, API) và Next.js 14 Monorepo (5 Route Groups: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`).
### B. Lỗ hổng & Điểm thiếu sót (Deficiencies / Gaps)
- Chưa đề cập cơ chế xác thực giữa các Route Groups trong Monorepo Next.js 14 (ví dụ: Session của Khách hàng là Anonymous/PWA Token, trong khi Staff/Manager/Admin yêu cầu JWT Cookie/Bearer).
- Chưa làm rõ cơ chế quản trị đa chi nhánh (Tenant Isolation): Dữ liệu phân tách theo `BranchId` ở tầng Application hay phân vùng schema Database.
### C. Điểm mơ hồ (Ambiguities)
- Khái niệm "28 Entity classes" được giao cho Backend: Chưa liệt kê danh mục cứng 28 entities này trong yêu cầu gốc mà phải đối chiếu chéo sang `ROADMAP.md`.
### D. Tác động đến Lập trình viên (Developer Impact)
- **Backend (.NET 8):** Phải chủ động đọc `ROADMAP.md` và `02_QUY_TRINH_THIET_KE_DATABASE.md` để lấy danh sách thực thể chính xác, tránh tạo thiếu bảng.
- **Frontend (Next.js 14):** Cần quy định rõ cấu hình chia sẻ UI Component giữa 5 Route Groups (Shared UI kit trong `@/components/ui`).
### E. Biện pháp xử lý chuẩn xác (Exact Remediation Required)
- Bổ sung bảng đối chiếu nhanh 28 Entities và 5 Route Groups vào tài liệu cấu trúc thư mục chuẩn.

---

## 3.2 Đánh giá: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Xem.md` & `Actor_KhachHang_Xem.html`
### A. Điểm mạnh (Strengths)
- Ngôn từ diễn đạt mang tính thương mại cao, làm nổi bật giá trị nghiệp vụ cho Chủ đầu tư F&B.
- Phân loại rõ 4 nhóm người dùng, bảng thống kê 71 tính năng và ma trận phân quyền cơ bản (RBAC Matrix).
- Quy trình Feedback có cơ chế bắn Alert khẩn cấp khi đánh giá $\le 2$ sao.
### B. Lỗ hổng & Điểm thiếu sót (Deficiencies / Gaps)
1. **Lỗ hổng bảo mật định danh SĐT (CRM Identity Spoofing):** Khách chỉ cần nhập SĐT là nạp hồ sơ CRM, lịch sử món và điểm Loyalty. Nếu không có mã xác thực OTP (Zalo/SMS), bất kỳ ai ngồi tại bàn cũng có thể nhập SĐT của người khác để xem lịch sử uống hoặc tiêu điểm Loyalty/áp voucher cá nhân.
2. **Thiếu cơ chế ràng buộc bàn (Table Session Locking):** Không chỉ rõ điều gì xảy ra nếu 2 khách tại 2 bàn khác nhau cùng quét mã QR hoặc một khách cố tình quét mã QR của bàn bên cạnh.
3. **Lỗ hổng kiểm duyệt ảnh Feedback:** Cho phép tải ảnh trực tiếp từ camera và "Publish công khai ngay lên QR Menu". Không có quy trình phê duyệt tự động bằng AI NSFW/Computer Vision hoặc quản lý duyệt tay, tiềm ẩn rủi ro phá hoại thương hiệu (Brand Defamation).
### C. Điểm mơ hồ (Ambiguities)
- Thuật ngữ "Không cần cài đặt ứng dụng" vs "Bắn thông báo lên trình duyệt điện thoại khi món nước đã pha xong": Push Notification trên trình duyệt Web (Web Push API) trên hệ điều hành iOS Safari có những ràng buộc rất ngặt nghèo (bắt buộc người dùng thêm vào Home Screen - Add to Home Screen mới bật được Web Push). Tài liệu chưa làm rõ giải pháp dự phòng (Polling / SignalR Websocket giữ kết nối màn hình).
### D. Tác động đến Lập trình viên (Developer Impact)
- **FE1 (Customer PWA):** Lúng túng khi lập trình thông báo món xong trên iPhone nếu khách không cài đặt PWA hoặc tắt màn hình điện thoại.
- **BE1 (Auth & CRM):** Phải tự quyết định việc có gửi OTP hay dùng "Soft Identification" (nhận diện mềm chỉ cho tích điểm, muốn trừ điểm/dùng voucher phải có xác nhận của nhân viên).
### E. Biện pháp xử lý chuẩn xác (Exact Remediation Required)
1. **Quy tắc bảo mật CRM Soft-ID:** Định danh qua SĐT chỉ cho phép xem Menu gợi ý và **Tích điểm tự động (Accrue Points)**. Khi khách muốn **Đổi điểm (Redeem Points)** hoặc **Sử dụng Voucher cá nhân**, hệ thống bắt buộc nhân viên quầy quét xác nhận hoặc gửi OTP Zalo.
2. **Chế độ kiểm duyệt Feedback:** Bổ sung trường `IsApproved` (mặc định `true` cho 4-5 sao kèm text thuần, nhưng nếu có ảnh hoặc $\le 3$ sao thì chuyển `IsApproved = false` chờ Quản lý duyệt trước khi hiện lên trang chủ QR Menu).

---

## 3.3 Đánh giá: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Smart_FB_OS.md`
### A. Điểm mạnh (Strengths)
- Cấu trúc tài liệu kỹ thuật chuẩn mực, phân định mã tính năng theo tiền tố rõ ràng: Khách hàng (`C-00` đến `C-24`), Nhân viên (`S-01` đến `S-12`), Quản lý (`M-01` đến `M-13`), Admin (`A-01` đến `A-22`).
- Phân định rõ 5 Module AI gán đúng đối tượng sử dụng (Khách hàng dùng AI-5 Chatbot, Admin dùng AI-1/2/3/4, Quản lý dùng AI-1; Barista không dùng AI mà nhìn công thức trực tiếp trên KDS).
### B. Lỗ hổng & Điểm thiếu sót (Deficiencies / Gaps)
1. **Xung đột trách nhiệm trong Actor 2 (Staff: Barista vs Chạy bàn):** Gom chung Barista và Waiter làm 1 Actor dẫn đến xung đột thao tác trên KDS: Barista chịu trách nhiệm đổi trạng thái món sang "Đang pha" / "Hoàn thành", trong khi Waiter chịu trách nhiệm "Bưng bê ra bàn" / "In bill" / "Thu tiền tại bàn".
2. **Thiếu cơ chế xử lý ca làm việc đồng thời (Concurrent Shift Workers):** Trong 1 ca làm việc tại quán thường có 1 Quản lý, 2 Barista, 2 Phục vụ. Tài liệu chưa làm rõ khi Barista A bấm "Hoàn thành", KDS của Barista B và điện thoại của Waiter C có đồng bộ ngay lập tức không và ai là người chịu trách nhiệm giao món.
3. **Lệch tổng số lượng tính năng:** Bảng tổng hợp ghi 24 tính năng Khách hàng, nhưng danh sách liệt kê từ `C-00` đến `C-24` là 25 tính năng thực tế (vì có thêm `C-00 Nhận diện SĐT`).
### C. Điểm mơ hồ (Ambiguities)
- Tính năng `A-06: Giá theo chi nhánh`: Chưa đặc tả cấu trúc bảng giá (Price List theo Branch hay bảng trung gian `ProductBranchPrice`). Nếu Admin sửa giá gốc toàn chuỗi, giá chi nhánh có bị ghi đè không?
### D. Tác động đến Lập trình viên (Developer Impact)
- **BE2 (Database & Admin):** Cần thiết kế bảng `BranchProduct` chứa `CustomPrice` và `IsAvailable` để ghi đè bảng giá chuỗi `Product.BasePrice`.
- **FE1 (KDS & Staff App):** Cần phân tách 2 chế độ hiển thị: KDS Bếp (cho màn hình TV quầy pha chế) và Staff Alerts (dành cho điện thoại nhân viên phục vụ chạy bàn).
### E. Biện pháp xử lý chuẩn xác (Exact Remediation Required)
- Cập nhật số liệu tính năng: 25 tính năng Khách hàng (hoặc đánh số lại `C-01` đến `C-24`), làm rõ mô hình phân quyền chi nhánh trong Database.

---

## 3.4 Đánh giá: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
### A. Điểm mạnh (Strengths)
- Tài liệu quy mô và toàn diện nhất dự án (882 dòng code/text), phân tích sâu sắc 8 bất cập thực tế của ngành F&B Việt Nam kèm số liệu thiệt hại kinh tế cụ thể.
- Đưa ra giải pháp kỹ thuật cụ thể cho từng bài toán: KDS công thức định lượng chuẩn, P&L đa chi nhánh tự động, Chấm công kết hợp GPS & QR động chống gian lận, AI Churn Prediction kéo khách quay lại.
- Thiết kế cơ chế chịu lỗi ngoại tuyến (Offline Resilience) 3 lớp bài bản.
### B. Lỗ hổng & Điểm thiếu sót (Deficiencies / Gaps)
1. **Xung đột Tech Stack không nhất quán (Legacy Technology Residue):** Tại mục 17 (Tech Stack), tài liệu ghi: Node.js / Python FastAPI, Flutter / React Native, Socket.IO. Trong khi dự án đã chốt .NET 8 Clean Architecture + Next.js 14 App Router + SignalR.
2. **Nghịch lý "Không POS" vs "POS Ngoại tuyến":** Mục 3.2 khẳng định chi phí máy POS = 0 đ, nhưng Mục 18.2 lại ghi màn hình POS Sunmi cảm ứng lưu SQLite local. Cần điều chỉnh sang Web PWA Offline (IndexedDB trên Tablet/Laptop của Quản lý).
3. **Lỗi trùng lặp ID tính năng:** Dòng 734 ghi `C-21 Gọi thêm món` (trong khi dòng 728 đã dùng `C-21 Nhận voucher qua Zalo`).
### C. Điểm mơ hồ (Ambiguities)
- **Định lượng nguyên liệu tự động (BOM - Bill of Materials):** Mục 5 nêu khi pha chế sẽ trừ kho quầy, nhưng chưa mô tả rõ việc trừ kho diễn ra khi Khách bấm đặt đơn, khi Barista bấm "Hoàn thành", hay khi Đóng ca kết kiểm kê.
### D. Tác động đến Lập trình viên (Developer Impact)
- Bắt buộc phải khóa cứng: **.NET 8 + Next.js 14 + SignalR + PostgreSQL 16**.
- **BE2:** Làm rõ logic trừ kho: Bán 1 ly Latte -> Trừ tự động `ProductIngredient` tương ứng ở kho quầy của chi nhánh (`BranchInventory`).
### E. Biện pháp xử lý chuẩn xác (Exact Remediation Required)
- Hiệu chỉnh bảng Tech Stack sang .NET 8 / Next.js 14 / SignalR.
- Đổi định danh tính năng mục 18.4 thành `C-22`, `C-23`, `C-24`.
- Sửa mô tả Lớp 2 Ngoại tuyến: Áp dụng Web PWA Offline (IndexedDB trên Tablet/PC thu ngân của Quản lý).

---

## 3.5 Đánh giá: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Smart_FB_OS.md`
### A. Điểm mạnh (Strengths)
- Minh họa luồng đi dữ liệu trực quan bằng sơ đồ ASCII Sequence Diagrams từ `WF-00` đến `WF-15`.
- Làm rõ tính liên kết giữa Khách hàng, Bếp (KDS), Quản lý ca và Chủ chuỗi.
### B. Lỗ hổng & Điểm thiếu sót (Deficiencies / Gaps)
1. **Thiếu hoàn toàn luồng Rollback & Hủy đơn (Order Cancellation & Rollback Flow):** Không có kịch bản xử lý khi khách đặt nhầm muốn hủy trong 30s đầu; không có kịch bản khi Barista hết nguyên liệu bấm từ chối pha món.
2. **Kẽ hở "Dine and Dash" trong luồng Thanh toán (WF-01):** Khách quét QR đặt món -> Bếp pha -> Uống xong bỏ về không trả tiền. Hệ thống chưa có cơ chế cảnh báo bàn chưa thanh toán trên Sơ đồ bàn.
3. **Luồng gộp đơn (`WF-03 Gọi thêm món`):** Khi đơn cũ đã thanh toán tiền mặt mà khách gọi thêm món thứ 2, hệ thống gộp hay sinh Round 2?
### C. Điểm mơ hồ (Ambiguities)
- Cơ chế đối soát két tiền `WF-08`: Chênh lệch 50K chưa có quy định ai bù tiền và ghi vết sổ kế toán (Audit Ledger).
### D. Tác động đến Lập trình viên (Developer Impact)
- **BE1:** Bắt buộc phải thiết kế `OrderStatus` và `PaymentStatus` là 2 State Machine độc lập.
- **FE1:** Xử lý logic hiển thị các món gọi thêm theo từng đợt (Round 1, Round 2) trên KDS.
### E. Biện pháp xử lý chuẩn xác (Exact Remediation Required)
- Bổ sung quy tắc: Mỗi lần khách gửi thêm món, tạo một `OrderGroup` hoặc đợt `OrderItem` mới gắn timestamp.
- Thêm cảnh báo màu đỏ trên Sơ đồ bàn cho những bàn "Đã phục vụ xong món nhưng chưa thanh toán > 15 phút".

---

## 3.6 Đánh giá: `d:\Idea_DoAn\ROADMAP.md`
### A. Điểm mạnh (Strengths)
- Phân bổ công việc chi tiết theo mô hình 4 Developers (BE1, BE2, FE1, FE2) qua 8 Sprints (16 tuần).
- Thiết lập 4 mốc Milestone cốt lõi (M0: Spec/Docker, M1: Auth/Menu, M2: QR Order/KDS Realtime, M3: VietQR/CRM/Admin).
- Có nguyên tắc "Mock First" cho Frontend rất tiến bộ.
### B. Lỗ hổng & Điểm thiếu sót (Deficiencies & Gaps)
1. **Độ lệch công nghệ AI trong Sprint 6:** Khẳng định 100% việc tích hợp AI sẽ sử dụng **Google Gemini 1.5 Flash API thông qua C# SDK** trong `SmartFB.Application`, không dựng Python server riêng.
2. **Khối lượng công việc FE1 trong Sprint 3 rất nặng:** Cần FE2 hỗ trợ dựng trước UI components hoặc modal.
### C. Tác động đến Lập trình viên (Developer Impact)
- Giúp 4 lập trình viên bắt tay làm việc song song ngay lập tức mà không bị chồng chéo quyền hạn.
### E. Biện pháp xử lý chuẩn xác (Exact Remediation Required)
- Chuẩn hóa AI dùng Gemini API C# SDK.
- Thiết lập chỉ tiêu Unit Test: Tối thiểu 80% coverage cho tầng `SmartFB.Application`.

---

# 4. CÁC KHOẢNG TRỐNG KỸ THUẬT XUYÊN SUỐT (CRITICAL CROSS-CUTTING GAPS)

### 4.1 Ma Trận Phân Quyền Chi Tiết (RBAC Enforcement Matrix)
| Phân hệ / API Resource | Endpoint Pattern | Khách hàng (`Customer`) | Nhân viên (`Staff`) | Quản lý (`Manager`) | Chủ chuỗi (`Admin`) | Ghi chú kiểm soát dữ liệu |
|---|---|:---:|:---:|:---:|:---:|---|
| **Xem Menu & Món ăn** | `GET /api/v1/products` | ✅ Cho phép | ✅ Cho phép | ✅ Cho phép | ✅ Cho phép | Public / Cache Redis |
| **Tạo đơn hàng QR** | `POST /api/v1/orders` | ✅ Cho phép | ✅ Tạo hộ | ❌ Chặn | ❌ Chặn | Gắn `TableId` & `BranchId` |
| **KDS Nhận & Đổi trạng thái** | `PATCH /api/v1/orders/{id}/items/{itemId}` | ❌ Chặn | ✅ Chi nhánh mình | ✅ Chi nhánh mình | ✅ Toàn quyền | Kiểm tra `User.BranchId == Order.BranchId` |
| **Báo hết món tạm thời** | `PATCH /api/v1/products/{id}/out-of-stock` | ❌ Chặn | ✅ Chi nhánh mình | ✅ Chi nhánh mình | ✅ Toàn quyền | Cập nhật Redis Key `OutOfStock:{BranchId}:{ProductId}` |
| **Mở ca / Kết ca két tiền** | `POST /api/v1/cash-shifts/*` | ❌ Chặn | ❌ Chặn | ✅ Chi nhánh mình | 🔍 Chỉ xem | Yêu cầu quyền `Cashier.Manage` |
| **Nhập / Xuất kho quầy** | `POST /api/v1/inventory/transactions` | ❌ Chặn | ❌ Chặn | ✅ Chi nhánh mình | ✅ Toàn chuỗi | Ghi log `CreatedByUserId` |
| **Xem Báo cáo Doanh thu** | `GET /api/v1/reports/*` | ❌ Chặn | ❌ Chặn | ✅ Chi nhánh mình | ✅ Toàn chuỗi | Filter bắt buộc theo `BranchId` của Manager |
| **CRUD Món, Giá, Danh mục** | `POST/PUT/DELETE /api/v1/admin/menu/*` | ❌ Chặn | ❌ Chặn | ❌ Chặn | ✅ Toàn quyền | Ghi vết `AuditLog` |
| **Quản lý Tài khoản & Phân quyền** | `POST/PUT/DELETE /api/v1/admin/users/*` | ❌ Chặn | ❌ Chặn | ❌ Chặn | ✅ Toàn quyền | Chỉ Admin tối cao |
| **Truy vấn AI Thống kê** | `POST /api/v1/ai/analytics` | ❌ Chặn | ❌ Chặn | ✅ Dữ liệu quán | ✅ Dữ liệu chuỗi | Prompt Injection Guard & Tenant Filter |

### 4.2 Máy Trạng Thái Đơn Hàng & Kịch Bản Ngoại Lệ
```
[OrderStatus State Machine]
 (Khách gửi đơn)           (KDS tiếp nhận)             (Barista pha xong)           (Phục vụ đưa ra bàn)
   [Pending]   ───────►   [InPreparation]   ───────►       [Ready]        ───────►       [Completed]
       │                         │                            │
       ├─────────────────────────┼────────────────────────────┤ (Hết nguyên liệu / Khách hủy)
       ▼                         ▼                            ▼
   [Cancelled] ◄─────────────────┴────────────────────────────┘

[PaymentStatus State Machine]
   [Unpaid]    ───────►   [PendingConfirmation]  ───────►   [Paid]
       │                         │
       ▼                         ▼
   [Refunded]  ◄───────────  [Failed]
```

### 4.3 Giải Quyết Nghịch Lý "Không Máy POS" vs "Offline Mode"
1. Thiết bị tại quán: 01 Smart TV (KDS) + 01 Tablet/Laptop Quản lý.
2. Mất mạng Internet: Tablet Quản lý mở Web App chạy Service Worker & IndexedDB local, tạo đơn, thu tiền mặt, in bill qua LAN.
3. Có mạng trở lại: Service Worker tự động Background Sync đơn lên Cloud.

### 4.4 Kiểm Soát Nội Dung Đánh Giá Khách Hàng
Đánh giá 4-5 sao text thuần -> Hiện công khai ngay. Đánh giá 1-3 sao HOẶC có Ảnh -> Chuyển vào hàng đợi `Pending_Review`, bắn alert cho Quản lý đến chăm sóc khách và bấm duyệt trên Web.

---

# 5. KHUYẾN NGHỊ HÀNH ĐỘNG CHO ĐỘI NGŨ LẬP TRÌNH
1. **Backend Lead (BE1) & Dev (BE2):** Khóa cứng .NET 8 Web API, EF Core 8, MediatR, SignalR, Redis 7, PostgreSQL 16. Gọi trực tiếp Gemini API trong .NET. Tổ chức SignalR Hub phân chia nhóm theo `branchId` và `tableId`.
2. **Frontend Lead (FE1) & Dev (FE2):** Monorepo 5 Route Groups trong Next.js 14 (`customer`, `kds`, `staff`, `manager`, `admin`). Quản lý state bằng Zustand và TanStack Query.

---

# 6. KẾT LUẬN THẨM ĐỊNH (AUDIT VERDICT)
Phân đoạn tài liệu 1 cung cấp bức tranh nghiệp vụ rất sâu sắc và thực tế. Sau khi áp dụng các khuyến nghị hiệu chỉnh về Tech Stack (.NET 8/Next.js 14), bổ sung State Machine cho Order/Payment, thiết lập cơ chế bảo mật Soft-CRM và quy trình kiểm duyệt Feedback công khai, **toàn bộ tài liệu Phân đoạn 1 đạt chuẩn 100% độ sẵn sàng kỹ thuật để bàn giao cho đội ngũ 4 lập trình viên.**
```

---

## 8.2 Báo Cáo Chi Tiết Phân Đoạn 2: `segment_02_baogia_va_skills`

*(Nguồn: `d:\Idea_DoAn\.agents\teamwork_preview_worker_seg2\unit_report_segment_02_baogia_va_skills.md`)*

```markdown
# 📊 BÁO CÁO RÀ SOÁT & ĐÁNH GIÁ KỸ THUẬT: PHÂN ĐOẠN 2 (BÁO GIÁ CHI PHÍ & DANH SÁCH SKILLS)

> **Dự án:** Hệ thống Điều hành Quán Cà phê / F&B Thông minh (Smart F&B OS)  
> **Phân đoạn rà soát:** Segment 2 — `segment_02_baogia_va_skills`  
> **Thư mục làm việc:** `d:\Idea_DoAn\.agents\teamwork_preview_worker_seg2`  
> **Tài liệu phân vùng:** `d:\Idea_DoAn\.agents\teamwork_preview_document_1\ANALYSIS_PARTITION.md`  
> **Đối tượng áp dụng:** Đội ngũ phát triển 4 thành viên (2 Backend .NET 8, 2 Frontend Next.js 14)  
> **Thời điểm thực hiện:** 2026-08-14

---

# 1. TỔNG QUAN ĐÁNH GIÁ (SUMMARY)

Phân đoạn 2 tập trung vào hai nhóm tài liệu có tính quyết định đến tính khả thi thương mại và phương pháp luận kỹ thuật của dự án:
1. **Nhóm Báo giá & Chi phí triển khai (`02_Bao_Gia_Chi_Phi`):** Tài liệu thương mại cam kết phạm vi tính năng, chi phí phần mềm, thiết bị phần cứng, chi phí vận hành hàng tháng và điều khoản thanh toán đối với khách hàng (chuỗi F&B 3 chi nhánh).
2. **Nhóm Danh mục Kỹ năng Kỹ thuật (`06_Danh_Sach_Skills`):** Các tài liệu hướng dẫn kỹ năng chuyên môn từ Backend, Frontend, DevOps, QA Testing đến Bảo mật và Kiến trúc hệ thống.

### 📌 Các phát hiện cốt lõi:
- **Nguy cơ tài chính & Bất khả thi thương mại:** Mức báo giá phần mềm trọn gói **15.000.000 VNĐ** cho 3-4 tháng phát triển với quy mô team 4 người (2 .NET 8 BE + 2 Next.js 14 FE) tương đương mức thù lao **~937.500 – 1.250.000 VNĐ / lập trình viên / tháng**. Mức định giá này chỉ mang tính tượng trưng/đồ án sinh viên, không phản ánh chi phí công sức thực tế cho một hệ thống phân tán đa chi nhánh gồm 28 bảng CSDL, 45+ REST endpoints, 4 kênh SignalR thời gian thực, 5 module AI và cơ chế Offline PWA Sync.
- **Hiện tượng Phình phạm vi (Scope Creep) & Cam kết vượt quá thiết kế:** Báo giá cam kết nhiều tính năng và dịch vụ bên thứ ba (Zalo OA ZNS, SendGrid Email, Firebase FCM, Chế độ Offline Sync tự động, Màn hình phụ 10" cho khách tại POS, Chấm công GPS/Sinh trắc học), nhưng trong tài liệu đặc tả kỹ thuật và API Contracts không hề có đặc tả giao thức đồng bộ (Conflict Resolution Protocol), không có webhook Zalo/SendGrid, và không có kiến trúc điều khiển màn hình phụ (Presentation/Dual-screen API).
- **Sự nhầm lẫn bản chất tài liệu Skills:** Toàn bộ thư mục `06_Danh_Sach_Skills` thực chất là **bộ chỉ mục lệnh điều phối AI Agent (Antigravity Meta-Prompt Index)** trỏ tới đường dẫn tuyệt đối cục bộ trên máy cá nhân (`C:\Users\nqtha\.gemini\config\skills\...`), chứ **HOÀN TOÀN KHÔNG PHẢI** là tài liệu hướng dẫn chuẩn code (Coding Standards) hay kiến trúc kỹ thuật nội bộ dành cho lập trình viên con người. Nếu không có AI Agent hỗ trợ, lập trình viên không thể trích xuất được quy tắc kỹ thuật nào từ thư mục này.
- **Lỗi liên kết & Không nhất quán đường dẫn:** Xuất hiện sai lệch nghiêm trọng về tên thư mục trong tài liệu (`05_Thiet_Ke_Kien_Truc_Diagrams/` thay vì `04_Thiet_Ke_Kien_Truc_Diagrams/`), sai lệch số lượng module AI (4 module trong Báo giá vs 5 module trong Đặc tả gốc).

---

# 2. BẢNG TỔNG HỢP DANH MỤC TÀI LIỆU & TRẠNG THÁI (FILE INVENTORY & STATUS TABLE)

| Đường dẫn tệp | Định dạng | Trạng thái kỹ thuật | Tóm tắt các vấn đề trọng yếu |
|---|---|---|---|
| `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.md` | Markdown | **Cần cải thiện** *(Needs Improvement)* | Báo giá quá thấp so với khối lượng công việc (15tr/4 người/4 tháng); Cam kết tính năng vượt đặc tả kỹ thuật (Zalo OA, SendGrid, Firebase, Offline Sync, Màn hình phụ POS 2 màn hình); Thiếu SLA bảo trì; Mâu thuẫn 4 vs 5 Module AI. |
| `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.html` | HTML | **Cần cải thiện** *(Needs Improvement)* | Bản HTML đồng bộ nội dung với bản `.md`. CSS in ấn A4 chuẩn, nhưng mang toàn bộ các sai lệch phạm vi và bất cập thương mại của file markdown gốc. |
| `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.docx` | MS Word | **Cần cải thiện** *(Needs Improvement)* | Tệp nhị phân xuất từ markdown/HTML. Đi kèm lock file rác `~$oGia_KhachHang.docx` ở thư mục gốc cần dọn dẹp. |
| `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.pdf` | PDF | **Cần cải thiện** *(Needs Improvement)* | Bản PDF xuất khẩu dùng để gửi khách hàng; lưu vết các cam kết pháp lý/phạm vi chưa có giải pháp kỹ thuật cụ thể. |
| `02_Bao_Gia_Chi_Phi/BẢNG BÁO GIÁ TRIỂN KHAI HỆ THỐNG SMART F&B OS.pdf` | PDF | **Cần cải thiện** *(Needs Improvement)* | File trùng lặp nội dung với `BaoGia_KhachHang.pdf` nhưng có dấu tiếng Việt trong tên file, dễ gây lỗi trên các môi trường CI/CD Linux. |
| `06_Danh_Sach_Skills/DANH_SACH_SKILLS_TONG_QUAT.md` | Markdown | **Cần cải thiện** *(Needs Improvement)* | Chỉ là danh mục từ khóa gọi AI prompt; Không chứa kiến thức kỹ thuật trực tiếp; Hardcode đường dẫn máy Windows cá nhân; Thiếu hướng dẫn áp dụng cho dev người. |
| `06_Danh_Sach_Skills/SKILLS_BACKEND_VA_KIEN_TRUC.md` | Markdown | **Cần cải thiện** *(Needs Improvement)* | 43 dòng văn bản thuần mô tả tên skill; Không có code mẫu Clean Architecture, MediatR CQRS, EF Core Fluent API, Redis Caching; Đường dẫn file tuyệt đối không khả chuyển (non-portable). |
| `06_Danh_Sach_Skills/SKILLS_DEVOPS_GIT_VA_RELEASE.md` | Markdown | **Cần cải thiện** *(Needs Improvement)* | 34 dòng mô tả; Thiếu file cấu hình Docker/CI-CD thực tế; Sai đường dẫn thư mục kiến trúc (`05_` thay vì `04_Thiet_Ke_Kien_Truc_Diagrams`). |
| `06_Danh_Sach_Skills/SKILLS_FRONTEND_VA_UIUX.md` | Markdown | **Cần cải thiện** *(Needs Improvement)* | 35 dòng mô tả; Không có cấu trúc Zustand store mẫu, quy ước Server/Client Component, Design Tokens Tailwind; Chỉ dẫn hướng tới AI prompt. |
| `06_Danh_Sach_Skills/SKILLS_TESTING_QA_VA_SECURITY.md` | Markdown | **Cần cải thiện** *(Needs Improvement)* | 35 dòng mô tả; Không có code mẫu xUnit, tiêu chí độ phủ Coverage (target %), quy tắc OWASP Header, Auth Middleware; Thiếu khả năng thực thi độc lập. |

---

# 3. PHÂN TÍCH KHE HỞ CHI TIẾT TỪNG TỆP (DETAILED FILE-BY-FILE GAP ANALYSIS)

### 3.1 `02_Bao_Gia_Chi_Phi/BaoGia_KhachHang.md` (và các định dạng `.html`, `.docx`, `.pdf`)
#### A. Điểm mạnh (Strengths)
1. Cấu trúc thương mại hoàn chỉnh (Phần A đến J), bao quát chi phí phần mềm, phần cứng, vận hành đám mây, bảo trì, phân tích ROI so với POS truyền thống.
2. Cung cấp phương án tái sử dụng máy POS Android cũ (tiết kiệm 27tr) và máy in nhiệt cũ (tiết kiệm 6tr).
3. Phân kỳ thanh toán 3 giai đoạn (7tr - 5tr - 3tr) bám sát mốc nghiệm thu.
#### B. Khiếm khuyết & Khe hở kỹ thuật/thương mại (Deficiencies & Gaps)
1. **Nghịch lý chi phí phát triển:** Báo giá 15.000.000 VNĐ cho hệ thống 28 bảng, 45+ endpoints, 5 route groups, SignalR, 5 module AI, Offline Sync. Tương đương ~937.500 VNĐ/người/tháng, phi thực tế với phát triển thương mại.
2. **Cam kết tính năng ngoại vi nhưng không có thiết kế kỹ thuật:** Zalo OA ZNS (cần tài khoản OA Doanh nghiệp, nạp tiền trước), SendGrid Email (thiếu SMTP/worker), Firebase FCM (PWA trên iOS cần Web Push VAPID và A2HS). Toàn bộ API Contract không có webhook nhận callback từ Zalo.
3. **Ảo tưởng về cơ chế Offline Mode:** Khẳng định khi mất mạng quán vẫn tạo đơn, thu tiền, tự đồng bộ khi có mạng. Thiếu cơ chế Conflict Resolution khi nguyên liệu bị bàn khác đặt hết; thiếu endpoint `BatchSyncOfflineOrdersRequest`.
4. **Màn hình phụ tại quầy POS:** Cam kết Sunmi 2 màn hình nhưng không có đặc tả kỹ thuật cách Web App POS đẩy dữ liệu sang màn hình thứ 2 (BroadcastChannel vs Presentation API).
5. **Mâu thuẫn số lượng Module AI:** Báo giá ghi 4 module AI; Đặc tả gốc ghi 5 module.
#### C. Điểm mơ hồ (Ambiguities)
- Chuyển giao 100% mã nguồn với giá 15tr mà không có điều khoản bảo vệ bản quyền.
- Gói bảo trì 1.000.000 VNĐ/tháng không nêu rõ cam kết SLA.
#### D. Tác động tới lập trình viên (Developer Impact)
- Team 4 devs sẽ bị quá tải nếu khách hàng đòi nghiệm thu đầy đủ Zalo OA, SendGrid, Offline Mode và POS 2 màn hình như đã hứa trong báo giá.
#### E. Biện pháp xử lý & Khắc phục chính xác (Exact Remediation Required)
1. Ghi rõ MVP v1.0 chỉ hỗ trợ Web-based POS online qua 4G/WiFi; dời Offline Storage Sync nâng cao sang Phase 2.
2. Chuyển tính năng Zalo OA và SendGrid sang "Tính năng tùy chọn tích hợp (Khách tự trả phí tin nhắn)".
3. Soạn thảo quy chuẩn POS 2 màn hình dùng `BroadcastChannel API`.
4. Thống nhất 5 Module AI xuyên suốt.

---

### 3.2 `06_Danh_Sach_Skills/DANH_SACH_SKILLS_TONG_QUAT.md` & 4 File Con
#### A. Điểm mạnh (Strengths)
- Tổng hợp 8 nhóm nghiệp vụ bao phủ toàn bộ vòng đời phát triển phần mềm; cú pháp kích hoạt AI rõ ràng.
#### B. Khiếm khuyết & Khe hở kỹ thuật (Deficiencies & Gaps)
1. **Sai lệch bản chất tài liệu:** Tệp này chỉ là danh bạ Meta-Prompt của công cụ AI Antigravity, hoàn toàn không cung cấp quy chuẩn lập trình hay best practice kỹ thuật nào cho lập trình viên con người.
2. **Đường dẫn cục bộ không khả chuyển:** Mọi mục đều hardcode `C:\Users\nqtha\.gemini\config\skills\...`.
3. **Lỗi sai đường dẫn thư mục:** Ghi `05_Thiet_Ke_Kien_Truc_Diagrams/` thay vì `04_Thiet_Ke_Kien_Truc_Diagrams/`.
4. **Thiếu vắng nội dung kỹ thuật thực tế:** Không có code mẫu Clean Architecture/MediatR, không có cấu hình Tailwind/Zustand, không có chỉ tiêu độ phủ Unit Test hay kịch bản k6 tải cụ thể.
#### E. Biện pháp xử lý & Khắc phục chính xác (Exact Remediation Required)
- Bổ sung cảnh báo ở đầu file: Thư mục này là danh bạ kỹ năng AI. Quy chuẩn code tham chiếu tại thư mục 03 và 05.
- Sửa lỗi đường dẫn `05_` thành `04_Thiet_Ke_Kien_Truc_Diagrams/`.

---

# 4. CÁC KHE HỞ PHỦ RỘNG TRỌNG YẾU (CRITICAL CROSS-CUTTING GAPS)
1. **Khoảng cách giữa Cam kết Báo giá và Hiện thực Kỹ thuật:** Báo giá hứa hẹn Zalo OA, SendGrid, FCM, POS Offline Sync, 2 màn hình POS với giá 15tr, nhưng các file thiết kế chi tiết chưa mô hình hóa thành DTO hay API cụ thể.
2. **Sự chuyển đổi bất khả thi từ Agent Skills sang Quy chuẩn Lập trình:** Cần chuyển hóa các hướng dẫn này thành tài liệu quy chuẩn kỹ thuật tại thư mục 03 và 05.
3. **Vấn đề Cold-Start của Module AI:** AI Churn Prediction và Combo Recommendation cần dữ liệu lịch sử lớn. Đối với quán mới mở (ngày 1-30), hệ thống sẽ bị Cold-Start và cần fallback sang quy tắc thống kê tĩnh (Rule-based).
4. **Chi phí ẩn của Dịch vụ bên thứ ba:** Phí viễn thông Zalo ZNS và xác thực DNS SendGrid cần được làm rõ với khách hàng.

---

# 5. KHUYẾN NGHỊ DÀNH CHO ĐỘI NGŨ LẬP TRÌNH VIÊN
- **Backend (BE1 & BE2):** Tạo `INotificationService` với `LoggingNotificationService` làm default implementation; bổ sung endpoint `POST /api/v1/orders/sync-offline` có kiểm tra `IdempotencyKey`.
- **Frontend (FE1 & FE2):** Zustand `persist` middleware lưu giỏ hàng vào `localStorage`; dùng `BroadcastChannel` cho màn hình phụ POS 2 màn hình; xây dựng hook `useSoundNotification` có kiểm tra User Gesture.
- **DevOps & QA:** Sửa đường dẫn `04_Thiet_Ke_Kien_Truc_Diagrams/`; thiết lập CI workflow `.github/workflows/ci.yml`; xóa lock file rác `~$oGia_KhachHang.docx`.
- **PM / Hợp đồng:** Tách bạch phụ lục hợp đồng MVP (12 tính năng cốt lõi) vs Phase 2 mở rộng; minh bạch chi phí dịch vụ bên thứ ba.
```

---

## 8.3 Báo Cáo Chi Tiết Phân Đoạn 3: `segment_03_quytrinh_yeucau_db_api`

*(Nguồn: `d:\Idea_DoAn\.agents\teamwork_preview_worker_seg3\unit_report_segment_03_quytrinh_yeucau_db_api.md`)*

```markdown
# BÁO CÁO ĐÁNH GIÁ KIỂM TOÁN TÀI LIỆU — PHÂN ĐOẠN 3 (SEGMENT 3)
## QUY TRÌNH PHÂN TÍCH YÊU CẦU, THIẾT KẾ DATABASE & HỢP ĐỒNG API CONTRACT

- **Dự án**: Smart F&B Operating System
- **Phân đoạn kiểm toán**: `segment_03_quytrinh_yeucau_db_api`
- **Mã phân bổ**: `teamwork_preview_worker_seg3`
- **Thời gian thực hiện**: 2026-08-14
- **Đối tượng thụ hưởng**: Đội ngũ phát triển 4 thành viên (2 .NET 8 Backend, 2 Next.js 14 Frontend)
- **Tài liệu kiểm toán**:
  1. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_QUY_TRINH_PHAN_TICH_YEU_CAU.md`
  2. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_QUY_TRINH_THIET_KE_DATABASE.md`
  3. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_QUY_TRINH_THIET_KE_API_CONTRACT.md`
  4. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md`

---

# 1. SUMMARY (TỔNG QUAN ĐÁNH GIÁ)

Phân đoạn 3 chứa các tài liệu cốt lõi định hình toàn bộ logic nghiệp vụ, lược đồ cơ sở dữ liệu và giao thức tích hợp client-server của hệ thống Smart F&B OS.

1. **Điểm sáng nổi bật (Strengths)**:
   - Tài liệu `03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md` (2.505 dòng) là một tài liệu đặc tả API xuất sắc, chi tiết bậc nhất với **64 RESTful Endpoints**, **4 SignalR Hubs** (kèm đầy đủ broadcast events và JSON Schema), áp dụng chuẩn **RFC 7807 ProblemDetails** và kịch bản kiểm thử tích hợp thực tế.
   - Tài liệu `01_QUY_TRINH_PHAN_TICH_YEU_CAU.md` xác định rất rõ tư duy tinh gọn (Lean Scope) bằng cách khoanh vùng 12 nhóm tính năng MVP Tier 1 thay vì dàn trải 71 tính năng.
   - Định hướng công nghệ nhất quán: PostgreSQL 16, EF Core 8 Code-First, UUID PK, SignalR WebSocket real-time, Next.js 14 App Router.

2. **Rủi ro và Lỗ hổng nghiêm trọng (Critical Vulnerabilities & Gaps)**:
   - **Xung đột cấu trúc Envelope phản hồi API (Envelope Inconsistency)**: Tài liệu tóm tắt `03` bắt buộc bọc toàn bộ phản hồi theo cấu trúc `{ success, data, pagination, error }`, trong khi tài liệu chi tiết `03_CHI_TIET` trả về trực tiếp DTO payload và áp dụng RFC 7807 cho mã lỗi. Gây vỡ giao thức kết nối giữa BE và FE nếu không thống nhất.
   - **Lược đồ cơ sở dữ liệu bị "rỗng ruột" trong tài liệu 02**: `02_QUY_TRINH_THIET_KE_DATABASE.md` chỉ liệt kê tên 28 bảng mà **hoàn toàn không có định nghĩa trường (fields), kiểu dữ liệu (data types), ràng buộc khóa ngoại (foreign keys), nullability, default values, hay Enum domain**.
   - **Thiếu hụt User Stories, Acceptance Criteria và NFRs trong tài liệu 01**: Hoàn toàn thiếu cấu trúc User Story chuẩn, tiêu chí chấp thuận kiểm thử được (Acceptance Criteria dạng Given/When/Then), và các chỉ số phi chức năng (NFR: SLA, Latency, Concurrency, Security, Idempotency).
   - **Lệch pha định nghĩa Vai trò (Role Discrepancy)**: Tài liệu 01 và 02 chỉ đề cập 4 vai trò, trong khi tài liệu 03_CHI_TIET mở rộng thành 6-7 vai trò.
   - **Thiếu các API phụ trợ vận hành**: Chưa có endpoints quản lý CRUD Voucher/Khuyến mãi, API upload media/ảnh, API quản lý điểm thành viên phía khách, và Health check endpoints.

3. **Chỉ số sẵn sàng triển khai (Readiness Index)**:
   - **Requirements Analysis (01)**: `60%`
   - **Database Design (02)**: `40%`
   - **High-level API Contract (03)**: `50%`
   - **Detailed API Contract (03_CHI_TIET)**: `95%`

---

# 2. FILE INVENTORY & STATUS TABLE

| Đường dẫn file | Trạng thái | Đánh giá tổng quát & Các vấn đề then chốt |
|---|:---:|---|
| `03_Quy_Trinh_Trien_Khai/01_QUY_TRINH_PHAN_TICH_YEU_CAU.md` | **Needs Improvement** | Phạm vi MVP 12 tính năng tốt, nhưng thiếu hoàn toàn User Stories, Acceptance Criteria (Given/When/Then), Non-Functional Requirements (NFRs), và các kịch bản biên (Edge cases). |
| `03_Quy_Trinh_Trien_Khai/02_QUY_TRINH_THIET_KE_DATABASE.md` | **Needs Improvement** | Thiếu 100% định nghĩa trường (columns), kiểu dữ liệu, quan hệ FK, Enums, cơ chế Soft Delete (`IsDeleted`) và Audit Trail (`CreatedBy`/`UpdatedBy`). Chỉ có 5 câu lệnh index sơ sài. |
| `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT.md` | **Needs Improvement** | Xung đột trực tiếp với file `03_CHI_TIET` về chuẩn đóng gói Response Envelope (`{success, data}` vs `ProblemDetails`), số lượng endpoints (17 vs 64), và số SignalR Hubs (2 vs 4). |
| `03_Quy_Trinh_Trien_Khai/03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md` | **Complete (High Quality)** | Cực kỳ xuất sắc và chi tiết (64 endpoints, 4 hubs, ProblemDetails RFC 7807, JSON Schemas). Thiếu sót nhỏ: Endpoint CRUD Vouchers, Upload file CDN, và Token refresh revocation policy. |

---

# 3. DETAILED FILE-BY-FILE GAP ANALYSIS

## 3.1. Phân tích File: `01_QUY_TRINH_PHAN_TICH_YEU_CAU.md`
- **Strengths:** Khoanh vùng 12 tính năng Tier 1, 6 nguyên tắc nghiệp vụ cốt lõi.
- **Deficiencies:** Thiếu User Stories, Acceptance Criteria, NFRs (Performance SLA, Real-time Latency, Concurrency, Availability, Rate Limiting).
- **Ambiguities:** Chưa làm rõ định danh phiên khách tại bàn (Guest Session Tracking) khi nhiều người cùng quét QR; phạm vi Báo hết món (86 Scope) theo chuỗi hay theo chi nhánh.
- **Remediation:** Bổ sung 12 User Stories dạng Given-When-Then, bảng NFRs định lượng, và giải pháp `GuestSessionId` gắn với `TableId`.

## 3.2. Phân tích File: `02_QUY_TRINH_THIET_KE_DATABASE.md`
- **Strengths:** Quy chuẩn UUID PK, Decimal(12,0), Restrict FK, UTC DateTime.
- **Deficiencies:** Thiếu 100% cấu trúc cột, thiếu Enum Domain (`OrderStatus`, `PrepStatus`, `PaymentMethod`, `PaymentStatus`, `TableStatus`, `AppRoles`, `StockTransactionType`), thiếu BaseEntity Soft Delete và Audit Trail. Danh mục 28 bảng lệch với ERD.
- **Remediation:** Tích hợp 28 bảng chi tiết từ ERD sang, chuẩn hóa BaseEntity có Soft Delete Filter `builder.HasQueryFilter(e => !e.IsDeleted)`, định nghĩa `ProductVariantIngredient` để trừ kho đúng theo Size biến thể.

## 3.3. Phân tích File: `03_QUY_TRINH_THIET_KE_API_CONTRACT.md` (Tóm tắt)
- **Deficiencies:** Xung đột Envelope với file chi tiết (`{success, data}` vs RFC 7807); chỉ có 17 endpoints sơ lược và 2 Hubs.
- **Remediation:** Đánh dấu file này là tổng quan quy trình; Single Source of Truth là file `03_CHI_TIET`.

## 3.4. Phân tích File: `03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md` (Chi tiết)
- **Strengths:** 2.505 dòng, 64 REST Endpoints, 4 SignalR Hubs (`OrderHub`, `KitchenHub`, `TableHub`, `PaymentHub`), RFC 7807, JSON Schemas, Webhook VietQR bảo mật `X-Webhook-Secret`.
- **Deficiencies:** Thiếu CRUD Vouchers (`/api/v1/vouchers`), Media Upload (`/api/v1/media/upload`), Khách xem điểm Loyalty (`/api/v1/customers/loyalty-profile`), Health check endpoints.
- **Remediation:** Bổ sung các module thiếu vào API Contract; áp dụng Refresh Token Rotation và Idempotency Key header `X-Idempotency-Key`.

---

# 4. CRITICAL CROSS-CUTTING GAPS
1. **Xung đột Envelope phản hồi:** Chuẩn hóa theo `03_CHI_TIET`: Thành công trả DTO trực tiếp; Lỗi trả về RFC 7807 ProblemDetails.
2. **Cơ sở Dữ liệu 28 bảng:** Chốt danh mục 28 bảng chuẩn hóa duy nhất (Branches, Tables, QrCodes, Categories, Products, ProductVariants, Toppings, ProductIngredients, Combos, ComboItems, Orders, OrderItems, OrderItemToppings, Payments, Users, BranchUsers, Customers, Ingredients, InventoryStocks, StockTransactions, Attendances, CashShifts, Shifts, LoyaltyTransactions, Vouchers, VoucherUsages, Reviews, ReviewImages).
3. **Ma trận Phân quyền RBAC:** Chuẩn hóa 7 vai trò trong JWT Claims: `SystemAdmin`, `StoreManager`, `ShiftLeader`, `Cashier`, `Waiter`, `KitchenChef`, `Barista`, `Customer`.
4. **Cơ chế Quản lý Phiên bàn:** Sinh `GuestToken` JWT nhẹ 4 giờ khi khách quét QR; đồng bộ giỏ hàng qua SignalR `OrderHub` nhóm `TableGroup_{TableId}`.
5. **Khóa Lạc quan & Idempotency:** Áp dụng Row-level Lock / Concurrency Token khi trừ kho; dùng Idempotency Key trên `Payments` theo transactionId ngân hàng.

---

# 5. RECOMMENDATIONS FOR DEVELOPERS
- **BE1:** Lấy `03_CHI_TIET` làm bất biến; cấu hình RFC 7807 trong `Program.cs`; xây dựng 4 SignalR Hubs có strongly-typed interfaces; viết middleware verify webhook VietQR; bổ sung CRUD Voucher & Media Upload.
- **BE2:** Tạo 28 Entity classes kế thừa `BaseEntity`; cấu hình Fluent API Restrict FK; tạo Migration InitialCreate_28Tables; viết `DatabaseSeeder.cs` nạp dữ liệu mẫu; viết Service trừ tồn kho tự động.
- **FE1:** Xây dựng luồng QR Check-in PWA lưu guestToken; kết nối `OrderHub` lắng nghe `OrderStatusUpdated`; kết nối `PaymentHub` nhận `PaymentConfirmed` từ VietQR.
- **FE2:** Xây dựng KDS Bếp `/kds` nhận `NewTicketReceived` từ `KitchenHub` với màu sắc và âm thanh; xây dựng Sơ đồ bàn `/pos/tables` nhận `TableStatusChanged` từ `TableHub`; Dashboard và Báo cáo P&L.

---

# 6. KẾT LUẬN & BÀN GIAO (VERDICT)
Segment 3 là phân đoạn tài liệu có giá trị kỹ thuật cao nhất. Sau khi khắc phục các thiếu sót đã nêu, **đội ngũ 4 lập trình viên hoàn toàn có thể bắt tay vào giai đoạn Implementation (Sprint 1) mà không gặp phải bất kỳ rào cản kỹ thuật nào.**
```

---

## 8.4 Báo Cáo Chi Tiết Phân Đoạn 4: `segment_04_quytrinh_uiux_be_fe_test`

*(Nguồn: `d:\Idea_DoAn\.agents\teamwork_preview_worker_seg4\unit_report_segment_04_quytrinh_uiux_be_fe_test.md`)*

```markdown
# 📋 BÁO CÁO KIỂM ĐỊNH TÀI LIỆU CHUYÊN SÂU: PHÂN ĐOẠN 4 (SEGMENT 4)
## QUY TRÌNH THIẾT KẾ UI/UX, PHÁT TRIỂN BACKEND (.NET 8), FRONTEND (NEXT.JS 14), TESTING & DEPLOYMENT

> **Mã Tài Liệu Báo Cáo:** `UNIT-REPORT-SEG-04-20260814`  
> **Phạm Vi Đánh Giá:** Phân đoạn 4 theo `ANALYSIS_PARTITION.md` (Segment: `segment_04_quytrinh_uiux_be_fe_test`)  
> **Nhóm Đối Tượng Đích:** Đội ngũ Kỹ sư gồm 4 Lập trình viên (2 Backend .NET 8 + 2 Frontend Next.js 14)  
> **Ngày Đánh Giá:** 14/08/2026  
> **Người Thực Hiện:** Chuyên viên Kiểm định Tài liệu & Kiến trúc Hệ thống Cấp cao (Specialist Document Review Analyst & Forensic QA)

---

# 1. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

Phân đoạn 4 là mắt xích thực thi trọng tâm của toàn bộ dự án **Smart F&B OS**, chuyển hóa các yêu cầu nghiệp vụ và hợp đồng dữ liệu thành phần mềm vận hành thực tế trên 5 thiết bị mục tiêu.

### Kết Luận Chung:
- **Điểm sáng vượt trội:** Tài liệu `04_THIET_KE_UI_UX_DESIGN_SYSTEM.md` đạt mức độ hoàn thiện xuất sắc và chi tiết hiếm thấy (1,294 dòng). Chuẩn hóa toàn bộ Design Tokens (HSL/Hex), bảng phông chữ Outfit/Inter, lưới 8px, theme KDS tương phản cao, các hiệu ứng hoạt họa CSS Keyframe và 29 màn hình Wireframe ASCII trực quan.
- **Lỗ hổng nghiêm trọng:** 4 tài liệu quy trình còn lại quá sơ lược (67 - 95 dòng mỗi file).
- **Rủi ro kỹ thuật đối với 4 Lập trình viên:**
  1. *Backend (.NET 8):* Thiếu CQRS/MediatR, Result Pattern monad, interface Repository/UnitOfWork, chi tiết RBAC Policy và chiến lược Optimistic Concurrency trên bảng đơn hàng và ca làm việc.
  2. *Frontend (Next.js 14):* Custom hook `useSignalR` trong quy trình 6 có lỗ hổng thiết kế nghiêm trọng (tạo mới kết nối trên từng component gây rò rỉ bộ nhớ và vượt ngưỡng kết nối WebSocket); thiếu ranh giới RSC/Client Components, TanStack Query v5 và Offline PWA.
  3. *Testing & Deployment:* Chưa cung cấp Dockerfile multi-stage, thiếu cấu hình Nginx WebSocket upgrade headers, thiếu mã test tự động (xUnit/Vitest), và AI Text-to-SQL tiềm ẩn lỗ hổng SQL Injection nếu không có Read-only sandbox.

---

# 2. BẢNG KIỂM KÊ TÀI LIỆU & TRẠNG THÁI (FILE INVENTORY & STATUS TABLE)

| Đường dẫn tập tin | Dung lượng / Dòng | Trạng thái kỹ thuật | Đánh giá mức độ sẵn sàng cho Dev | Tóm tắt các vấn đề cốt lõi |
|---|---|---|---|---|
| `03_Quy_Trinh_Trien_Khai/04_QUY_TRINH_THIET_KE_UI_UX.md` | 4.8 KB / 95 dòng | 🟡 **Needs Improvement** | 60% Ready | Quá ngắn; định nghĩa Zustand Store sơ sài; không có Breakpoint CSS; lệch số lượng phân hệ so với Design System. |
| `03_Quy_Trinh_Trien_Khai/04_THIET_KE_UI_UX_DESIGN_SYSTEM.md` | 112 KB / 1,294 dòng | 🟢 **Complete / Production-Grade** | 95% Ready | Đặc tả 29 Wireframe và Design Tokens rất chi tiết; chỉ thiếu file mapping `tailwind.config.ts` và TypeScript Props Interface cho 12 UI Components. |
| `03_Quy_Trinh_Trien_Khai/05_QUY_TRINH_PHAT_TRIEN_BACKEND.md` | 3.4 KB / 88 dòng | 🔴 **Needs Improvement (Major Gaps)** | 40% Ready | Thiếu CQRS/MediatR, Result Pattern, Unit of Work, JWT Refresh Token, strongly-typed SignalR Hubs và Optimistic Concurrency. |
| `03_Quy_Trinh_Trien_Khai/06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md` | 3.1 KB / 82 dòng | 🔴 **Needs Improvement (Critical Flaw)** | 35% Ready | Đoạn code `useSignalR` bị lỗi thiết kế gây rò rỉ WebSocket; thiếu RSC/Client boundary, TanStack Query v5 Optimistic Updates, Middleware RBAC và PWA Offline. |
| `03_Quy_Trinh_Trien_Khai/07_QUY_TRINH_TESTING_DEPLOYMENT.md` | 2.4 KB / 67 dòng | 🔴 **Needs Improvement (Major Gaps)** | 30% Ready | Không có setup xUnit/Vitest; AI Text-to-SQL có rủi ro SQL Injection; thiếu Dockerfile multi-stage, Nginx WebSocket proxy headers và CI/CD workflow. |

---

# 3. PHÂN TÍCH CHI TIẾT KHE HỞNG TỪNG TẬP TIN

## 3.1 `04_QUY_TRINH_THIET_KE_UI_UX.md`
- Thiếu các Store quan trọng: `TableSessionState`, `KdsFilterState`, `NotificationState`, `OfflineSyncQueueState`. Lệch số phân hệ (4 vs 5).
- Khắc phục: Bổ sung TypeScript Interface đầy đủ cho các Store Zustand.

## 3.2 `04_THIET_KE_UI_UX_DESIGN_SYSTEM.md`
- Đạt 95% chất lượng. Thiếu `tailwind.config.ts`, thiếu Interface Props cho 12 component dùng chung, chưa xử lý Autoplay Audio Policy của trình duyệt cho chuông báo KDS.
- Khắc phục: Cung cấp `tailwind.config.ts` tích hợp Design Tokens; định nghĩa Interface Props cho `TimerBanner`, `VietQRBox`, `Button`, `Modal`...

## 3.3 `05_QUY_TRINH_PHAT_TRIEN_BACKEND.md`
- Thiếu MediatR Pipeline Behaviors, thiếu Result Pattern Monad (`Result<T>`, `Error`), thiếu Unit of Work, thiếu strongly-typed Hubs, thiếu Concurrency token `xmin` cho PostgreSQL.
- Khắc phục: Cung cấp bộ khung Clean Architecture, Result Pattern Monad và Strongly Typed Hubs.

## 3.4 `06_QUY_TRINH_PHAT_TRIEN_FRONTEND.md`
- **LỖ HỔNG NGHIÊM TRỌNG TRONG HOOK `useSignalR`:** Tạo mới connection WebSocket trên từng component dẫn đến mở hàng chục kết nối thừa, gây rò rỉ bộ nhớ và sập máy chủ.
- Thiếu quy tắc RSC vs Client Components, thiếu TanStack Query v5, thiếu `middleware.ts` RBAC guard.
- Khắc phục: Thay thế bằng **SignalR Singleton Provider Pattern (`SignalRProvider.tsx`)** và hook `useSignalREvent`.

## 3.5 `07_QUY_TRINH_TESTING_DEPLOYMENT.md`
- **RỦI RO BẢO MẬT AI TEXT-TO-SQL:** LLM tự sinh SQL và chạy trực tiếp trên database chính có thể gây SQL Injection hoặc xóa dữ liệu do hallucination.
- Thiếu Dockerfile multi-stage, thiếu Nginx WebSocket upgrade headers, thiếu xUnit Integration test sample.
- Khắc phục: Tạo User DB Read-only riêng cho AI (`smartfb_ai_readonly`); cung cấp file `nginx.conf` chuẩn có WebSocket upgrade headers; cung cấp xUnit `WebApplicationFactory` test sample.

---

# 4. CÁC LỖ HỔNG XUYÊN SUỐT HỆ THỐNG
1. **Đồng bộ SignalR Contract & State:** Dùng SignalREventRegistry tập trung, Strongly-Typed Hubs ở BE và Singleton Provider ở FE.
2. **Khả năng chống chịu mất mạng (Offline):** Bổ sung Idempotency-Key Header, IndexedDB queue và Service Worker Cache-First cho Menu PWA.
3. **Luồng Xác thực & Phân quyền (RBAC):** HttpOnly Cookie cho Refresh Token, Next.js Middleware Guard và ClaimsPrincipal Policy.
4. **Chiến lược Caching Redis:** Cấu trúc key chuẩn hóa (`menu:branch:{id}`) và tự động xóa cache khi Admin đổi giá món.
5. **An toàn AI Engine:** Read-Only DB User riêng, whitelist bảng và tham số hóa query.
6. **Hạ tầng Nginx WebSocket:** Cung cấp Nginx conf chuẩn có WebSocket upgrade headers và multi-stage Dockerfiles.

---

# 5. KHUYẾN NGHỊ HÀNH ĐỘNG CHO ĐỘI NGŨ 4 LẬP TRÌNH VIÊN
- **BE1:** Solution Clean Architecture chuẩn, Result Pattern, Strongly-Typed Hubs, Optimistic Concurrency `xmin`.
- **BE2:** EF Core Fluent API 28 bảng, Seed Data Mochi Sweets, Database User Read-only cho AI Analytics.
- **FE1:** Config `tailwind.config.ts`, 12 Shared UI Components, `SignalRProvider` Singleton, Audio Context unlock cho KDS.
- **FE2:** Route Guards `middleware.ts`, TanStack Query v5 Optimistic Updates, Touch targets $\ge 48\times 48\text{px}$ cho POS.
```

---

## 8.5 Báo Cáo Chi Tiết Phân Đoạn 5: `segment_05_kientruc_diagrams`

*(Nguồn: `d:\Idea_DoAn\.agents\teamwork_preview_worker_seg5\unit_report_segment_05_kientruc_diagrams.md`)*

```markdown
# BÁO CÁO ĐÁNH GIÁ CHI TIẾT KIẾN TRÚC VÀ SƠ ĐỒ HỆ THỐNG (SEGMENT 5)
## DỰ ÁN: SMART F&B OPERATING SYSTEM
**Người thực hiện:** Senior Architecture & Document Review Analyst (Teamwork Specialist)  
**Phạm vi kiểm tra (Segment 5):** `04_Thiet_Ke_Kien_Truc_Diagrams/` & Hạ tầng triển khai (Docker/Env)  
**Tập tin mục tiêu:**
1. `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md`
2. `04_Thiet_Ke_Kien_Truc_Diagrams/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md`
3. `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md`
4. `04_Thiet_Ke_Kien_Truc_Diagrams/04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md`
5. Root files liên kết: `docker-compose.yml`, `.env.example`, `frontend/.env.example`

---

# 1. SUMMARY (TỔNG QUAN ĐÁNH GIÁ)

Phân hệ **Segment 5 (Kiến trúc, Sơ đồ luồng, ERD & Hạ tầng triển khai)** đóng vai trò là "Bản vẽ kỹ thuật thi công" quyết định sự thành bại trong việc phối hợp của đội ngũ 4 lập trình viên.

### Kết quả tổng quan:
* **Mức độ hoàn thiện hình ảnh & sơ đồ:** **Khá (78/100)**
* **Mức độ nhất quán kỹ thuật & khớp nối thực thi:** **Trung bình yếu (62/100)**
* **Điểm đánh giá sẵn sàng thi công (Production Readiness Score):** **68 / 100**

### 5 Vấn đề cốt tử được phát hiện:
1. **Bất đồng bộ mô hình thực thể (Domain Entity Duality):** ERD dùng `Branch`, `Product`, `ProductVariant`, `Topping`, `CashShift` trong khi C# code lại dùng `Restaurant`, `MenuItem`, `ModifierGroup`, `ModifierItem`, `CashDrawer`.
2. **Lệch pha kiến trúc SignalR Hub:** Sơ đồ chỉ vẽ 1 `OrderHub` chung, trong khi API Contract chi tiết định nghĩa 4 Hubs (`OrderHub`, `KitchenHub`, `TableHub`, `PaymentHub`).
3. **Đứt gãy luồng thanh toán VietQR Webhook:** Sequence Diagram 3 mô tả nhân viên xác nhận tiền bằng mắt trên app ngân hàng rồi bấm duyệt tay, thiếu luồng Webhook tự động.
4. **Vi phạm nguyên lý Clean Architecture trong sơ đồ Component:** Sơ đồ vẽ `Application -> Infrastructure`, vi phạm Dependency Inversion Principle.
5. **Độ lệch cấu hình Docker Compose & Môi trường:** Sai tên biến môi trường (`${DATABASE_NAME}` vs `${POSTGRES_DB}`), thiếu Volume mount uploads `/var/smartfb/uploads`, thiếu file `nginx.conf` mẫu hỗ trợ WebSocket.

---

# 2. FILE INVENTORY & STATUS TABLE

| STT | Đường dẫn tập tin | Trạng thái | Tóm tắt các vấn đề cốt lõi |
|:---:|---|:---:|---|
| 1 | `04_Thiet_Ke_Kien_Truc_Diagrams/01_KIEN_TRUC_HE_THONG_TONG_QUAN.md` | 🟡 Needs Improvement | Sơ đồ Clean Architecture sai DIP; thiếu SignalR cho Manager; xuất hiện FCM nhưng không có cấu hình; ranh giới AI Container chưa rõ. |
| 2 | `04_Thiet_Ke_Kien_Truc_Diagrams/02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md` | 🟡 Needs Improvement | QR Order gán ngay `Confirmed`; VietQR thiếu Banking Webhook tự động; lệch tên Event SignalR; thiếu Sequence Diagram cho Text-to-SQL và Offline Sync. |
| 3 | `04_Thiet_Ke_Kien_Truc_Diagrams/03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md` | 🔴 Needs Improvement | Chỉ đặc tả trường cho 17/28 bảng (thiếu 11 bảng); xung đột danh mục 28 bảng với Folder 03; xung đột tên bảng với C# code. |
| 4 | `04_Thiet_Ke_Kien_Truc_Diagrams/04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md` | 🟡 Needs Improvement | Docker Compose mẫu sai biến môi trường so với `.env.example`; thiếu Volume mount uploads; thiếu file `nginx.conf` mẫu hỗ trợ WebSocket; thiếu healthcheck. |
| 5 | `docker-compose.yml` (Root) & `.env.example` | 🟡 Needs Improvement | Root compose chỉ có Postgres + Redis cho local dev; Redis password không nhất quán; FE `.env.example` chỉ có 1 Hub URL chung. |

---

# 3. PHÂN TÍCH CHI TIẾT TỪNG TẬP TIN & GIẢI PHÁP KHẮC PHỤC

## 3.1 `01_KIEN_TRUC_HE_THONG_TONG_QUAN.md`
- Đảo ngược quan hệ Clean Architecture: `Infrastructure -> Application` và `Infrastructure -> Domain`. `Application` chỉ chứa Interfaces, `Infrastructure` thực thi chúng.
- Bổ sung kết nối `NotificationHub` cho Manager Dashboard.
- Xác nhận Frontend là Single Next.js 14 Monolith (App Router 5 Route Groups) chạy trên port 3000.

## 3.2 `02_SO_DO_LUONG_DULIEU_WORKFLOW_SEQUENCE.md`
- Chuẩn hóa lại Sequence Diagram 3: Luồng thanh toán VietQR Webhook tự động (Bank Server gửi webhook -> PayAPI verify signature HMAC-SHA256 -> Update DB -> Broadcast SignalR `PaymentConfirmed` tới PWA và POS).
- Cập nhật tên event SignalR khớp 100% với file 03_CHI_TIET.

## 3.3 `03_SO_DO_DATABSE_ERD_DATABASE_DIAGRAM.md`
- Chốt danh mục 28 bảng chuẩn hóa duy nhất.
- Bổ sung chi tiết trường thuộc tính cho 11 bảng còn thiếu (`BranchUser`, `Combo`, `ComboItem`, `ProductIngredient`, `Attendance`, `Shifts`, `LoyaltyTransaction`, `Voucher`, `VoucherUsage`, `ReviewImage`, `BusinessHours`).
- Thống nhất 100% danh pháp F&B Hiện đại: `Branch`, `Product`, `ProductVariant`, `Topping`, `CashShift`.

## 3.4 `04_SO_DO_DEPLOY_INFRASTRUCTURE_DIAGRAM.md`
- Cung cấp file cấu hình `nginx.conf` hoàn chỉnh có WebSocket upgrade headers cho `/hubs/` và location `/uploads/`.
- Chuẩn hóa file `docker-compose.production.yml` đồng bộ 100% biến môi trường với `.env.example` và bổ sung volume mount `uploads_data:/var/smartfb/uploads`.

---

# 4. CRITICAL CROSS-CUTTING GAPS
1. **Xung đột Ngôn ngữ mô hình (Ubiquitous Language Gap):** Thống nhất dùng `Branch`, `Product`, `Topping`, `CashShift`.
2. **Độ lệch kiến trúc SignalR Hubs:** Tách 4 Hubs độc lập (`/hubs/order`, `/hubs/kitchen`, `/hubs/table`, `/hubs/payment`) để phân tách tải.
3. **Cơ chế Background Processing:** Cài đặt .NET `BackgroundService` định kỳ quét đơn hết hạn thanh toán và đối soát kết ca tự động.

---

# 5. RECOMMENDATIONS FOR DEVELOPERS
- **BE1:** Refactor Entity Models trong `SmartFB.Domain` theo bảng từ vựng chuẩn; cấu hình Fluent API & Indexing; xây dựng 4 SignalR Hubs độc lập.
- **BE2:** Triển khai Webhook VietQR tự động với HMAC-SHA256 checksum; viết `CashShiftService` đối soát két tiền; tích hợp Gemini AI với Read-only DB user.
- **FE1:** Xây dựng luồng QR Order PWA gửi kèm `Idempotency-Key`; kết nối SignalR `OrderHub` & `PaymentHub` đếm ngược 15 phút.
- **FE2:** Màn hình KDS Bếp kết nối `KitchenHub` nhận `NewTicketReceived`; màn hình Sơ đồ bàn POS kết nối `TableHub`; Form Mở/Kết ca đối soát két tiền.
```

---

## 8.6 Báo Cáo Chi Tiết Phân Đoạn 6: `segment_06_quychuan_testcases_mochi`

*(Nguồn: `d:\Idea_DoAn\.agents\teamwork_preview_worker_seg6\unit_report_segment_06_quychuan_testcases_mochi.md`)*

```markdown
# BÁO CÁO ĐÁNH GIÁ VÀ KIỂM ĐỊNH KỸ THUẬT (UNIT AUDIT REPORT)
## PHÂN ĐOẠN 6: QUY CHUẨN LẬP TRÌNH, GIT CONVENTIONS, KỊCH BẢN DEMO/UAT VÀ SEED DATA (SEGMENT 6)
**Dự án:** Smart F&B Operating System  
**Phạm vi kiểm định:** Thư mục `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\`  
**Chuyên viên đánh giá:** Document Review Specialist (Teamwork Agent)  
**Ngày thực hiện:** 2026-08-14  
**Đối tượng thụ hưởng:** Đội ngũ phát triển 4 thành viên (2 .NET 8 Backend, 2 Next.js 14 Frontend) & Hội đồng nghiệm thu  

---

# 1. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

Phân đoạn 6 bao gồm 4 tài liệu cốt lõi quy định tiêu chuẩn kỹ thuật phát triển, quy trình cộng tác Git, kịch bản kiểm thử nghiệm thu (UAT/Demo), và định nghĩa dữ liệu mẫu (Seed Data) cho toàn bộ hệ thống Smart F&B OS.

### Kết quả đánh giá tổng thể:
1. **Điểm sáng (Strengths):**
   - Tài liệu `01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md` có chất lượng rất tốt: Phân chia ma trận trách nhiệm rõ ràng cho 4 devs, hướng dẫn Git Rebase chi tiết, 10 Conventional Commit types với 15 ví dụ thực tế, và mẫu `.env.example` hơn 40 biến môi trường không dùng placeholder.
   - Kịch bản Demo 5 phút nối liền trong `02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md` bám sát luồng nghiệp vụ cốt lõi, phù hợp bảo vệ trước Hội đồng.
   - Dữ liệu món ăn mẫu trong `03_MOCHI_DATA_SEED_DEFINITION.md` có định lượng pha chế (Recipe Instructions), cảnh báo dị ứng (Allergens) và tag nghiệp vụ thực tế.

2. **Tồn tại và Lỗ hổng nghiêm trọng (Critical Deficiencies & Technical Gaps):**
   - **Xung đột danh pháp mô hình dữ liệu (Domain Model Drift):** Bất đồng bộ giữa Seed Data / ERD (`Branch`, `Product`, `Topping`) và Mã nguồn C# `AppDbContext.cs` (`Restaurant`, `MenuItem`, `ModifierGroup`, `ModifierItem`, `Zone`, `Invoice`).
   - **Tài liệu Seed Data chưa đủ độ phủ (Seed Incompleteness):** Mới chỉ định nghĩa dạng text cho 6/28 thực thể. Thiếu toàn bộ Kho & Định lượng (`Ingredients`, `InventoryStocks`, `ProductIngredients`), `Vouchers`, `Customers`, `CashShifts`, `QrCodes`. Thiếu hoàn toàn mã C# `DbInitializer.cs` với Static GUIDs và file mock JSON cho Frontend.
   - **Xung đột tên gọi & Nhận diện thương hiệu:** Tên file là `MOCHI` nhưng nội dung là chuỗi cà phê "Smart Coffee" (Bạc xỉu, Cà phê muối, Trà đào).
   - **Bộ kịch bản Test UAT quá sơ sài và thiếu Edge Cases:** 15 test cases happy path; thiếu 100% các ca kiểm thử biên (Concurrent Table Ordering, Kitchen Void & Stock Reversal, Split Bill, POS Offline Sync, SignalR Reconnect, Webhook Idempotency).
   - **Trùng lặp & Phân mảnh tài liệu:** `01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md` chỉ là file redirect 12 dòng.

---

# 2. BẢNG DANH MỤC TÀI LIỆU VÀ TRẠNG THÁI (FILE INVENTORY & STATUS TABLE)

| Đường Dẫn File | Trạng Thái | Mức Độ Hoàn Thiện | Tóm Tắt Vấn Đề Trọng Tâm |
| :--- | :---: | :---: | :--- |
| `05_Quy_Chuan_&_Test_Cases\01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md` | 🟡 **Needs Improvement** (Redirect Stub) | 15% | File 12 dòng chuyển hướng. Gây phân mảnh danh mục; cần tái cấu trúc thành file Linter/Formatter hoặc xóa. |
| `05_Quy_Chuan_&_Test_Cases\01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md` | 🟢 **Needs Improvement** (Khá Tốt) | 85% | Nội dung rất đầy đủ về GitFlow, Commit, PR, .env. Tuy nhiên sai đường dẫn thư mục code thực tế (`src/Backend/...` vs `backend/src/...`), quy định 2 approvals quá nặng cho team 4 người. |
| `05_Quy_Chuan_&_Test_Cases\02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md` | 🔴 **Needs Improvement** (Thiếu Trầm Trọng) | 40% | Kịch bản demo 5 phút tốt nhưng chỉ có 15 test cases UAT cơ bản. Thiếu 100% các ca kiểm thử biên (concurrency, offline, void món, hoàn tiền, split bill, webhook idempotency). |
| `05_Quy_Chuan_&_Test_Cases\03_MOCHI_DATA_SEED_DEFINITION.md` | 🔴 **Needs Improvement** (Thiếu Trầm Trọng) | 35% | Mới định nghĩa 6/28 bảng dữ liệu. Thiếu Script C# `DbInitializer.cs` với GUIDs, thiếu JSON mock data, thiếu seed kho nguyên liệu, voucher, loyalty, két tiền ca. Tên file `MOCHI` bất nhất với dữ liệu "Smart Coffee". |

---

# 3. PHÂN TÍCH CHI TIẾT TỪNG FILE VÀ LỖ HỔNG

## 3.1 `01_QUY_CHUAN_CODING_VA_GIT_CONVENTION.md`
- File redirect stub 12 dòng. Đề xuất: Tái cấu trúc thành tài liệu chứa toàn văn cấu hình `.editorconfig`, `.eslintrc.json`, `.prettierrc` hoặc xóa bỏ.

## 3.2 `01_QUY_CHUAN_GIT_WORKFLOW_VA_PR_CHECKLIST.md`
- Sửa đường dẫn thành `backend/src/SmartFB.API` và `frontend/`.
- Điều chỉnh PR Approval: Nhánh `feature/*` -> `develop` cần **1 Approval** từ peer dev; Nhánh `release/*` / `hotfix/*` -> `main` cần **2 Approvals**.
- Bổ sung cấu hình `.editorconfig` vào root repository.

## 3.3 `02_KICH_BAN_DEMO_VA_UAT_TEST_CASES.md`
- Mở rộng từ 15 lên tối thiểu **35 test cases chi tiết**, chia 4 nhóm:
  1. *Core Functional Tests (P0):* Auth, Menu, QR Order, KDS State, Payment.
  2. *Concurrency & Race Conditions (P1):* Concurrent Table Ordering, Out-of-Stock Lock, Double Webhook Callback.
  3. *Failure Recovery & Hardware (P1/P2):* SignalR Reconnect Sync, POS Offline Queue, Sunmi Printer Jam.
  4. *Accounting, Void & Shift Reconciliation (P1):* Kitchen Void Item, Cash Drawer Discrepancy, Split Bill.

## 3.4 `03_MOCHI_DATA_SEED_DEFINITION.md`
- Đổi tên thành `03_SEED_DATA_SPECIFICATION_SMART_COFFEE.md`.
- Cung cấp toàn văn mã nguồn C# `DbInitializer.cs` với Static Deterministic GUIDs cho toàn bộ 28 bảng (Branches, Categories, Products, ProductVariants, Toppings, Ingredients, ProductIngredients, InventoryStocks, Tables, QrCodes, Users, Customers, LoyaltyTiers, Vouchers, CashShifts, Printers).
- Tạo file `seed-data.json` đi kèm cho Frontend.

---

# 4. CÁC LỖ HỔNG XUYÊN SUỐT HỆ THỐNG
1. **Entity Naming Drift:** Xung đột danh pháp giữa tài liệu (`Branch/Product/Topping`) và `AppDbContext.cs`.
2. **Real-time Failure & Resilience:** UAT thiếu test SignalR Reconnect & POS Offline sync queue.
3. **Automated Webhook & Idempotency:** Thiếu test replay webhook thanh toán.
4. **Seed Data Execution Gap:** Thiếu mã C# DbInitializer và JSON fixtures.

---

# 5. KHUYẾN NGHỊ CHO 4 DEVELOPERS
- **BE-Dev-1:** Thống nhất danh pháp Entity; Xây dựng `DbInitializer.cs` với Static GUIDs; Cấu hình Docker PostgreSQL & Seed tự động.
- **BE-Dev-2:** Reconnect & Backoff cho SignalR Hubs; Idempotency Key cho Webhook PayOS/VietQR; 10 Integration Tests (xUnit) cho Concurrency & Kitchen Void.
- **FE-Dev-1:** Mock `seed-data.json` cho QR Menu & KDS; UI KDS cảnh báo vàng khi mất WebSocket; Playwright E2E cho Demo 5 phút.
- **FE-Dev-2:** IndexedDB Offline Cache cho POS; Màn hình Đối soát Két tiền Ca làm; Cấu hình kết nối máy in Sunmi POS.

---

# 6. ĐỀ XUẤT CÁC ĐOẠN MÃ VÀ TÀI LIỆU CHUẨN CẦN BỔ SUNG

### 6.1 File Cấu Hình `.editorconfig` Chuẩn Hóa (.NET 8 & Next.js 14)
```ini
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.cs]
indent_size = 4
csharp_new_line_before_open_brace = all
csharp_new_line_before_else = true
csharp_new_line_before_catch = true
csharp_new_line_before_finally = true
csharp_prefer_braces = true:silent
csharp_style_var_for_built_in_types = false:suggestion
dotnet_style_qualification_for_field = false:suggestion
dotnet_naming_rule.private_fields_with_underscore.symbols = private_fields
dotnet_naming_rule.private_fields_with_underscore.style = prefix_underscore

[*.{ts,tsx,js,jsx,json}]
indent_size = 2
quote_type = single

[*.md]
trim_trailing_whitespace = false
```

### 6.2 Đoạn Mã C# Khởi Tạo Dữ Liệu Mẫu (`DbInitializer.cs`)
```csharp
using Microsoft.EntityFrameworkCore;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Data;

public static class DbInitializer
{
    public static readonly Guid BranchQ1Id = Guid.Parse("11111111-1111-1111-1111-111111111111");
    public static readonly Guid BranchThuDucId = Guid.Parse("22222222-2222-2222-2222-222222222222");
    public static readonly Guid BranchQ7Id = Guid.Parse("33333333-3333-3333-3333-333333333333");

    public static readonly Guid CatCoffeeId = Guid.Parse("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa");
    public static readonly Guid CatTeaId = Guid.Parse("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb");
    public static readonly Guid CatPastryId = Guid.Parse("cccccccc-cccc-cccc-cccc-cccccccccccc");

    public static readonly Guid ProdBacXiuId = Guid.Parse("d1111111-1111-1111-1111-111111111111");
    public static readonly Guid ProdCafeMuoiId = Guid.Parse("d2222222-2222-2222-2222-222222222222");

    public static async Task SeedAsync(AppDbContext context)
    {
        if (await context.Categories.AnyAsync()) return;

        var categories = new List<Category>
        {
            new() { Id = CatCoffeeId, Name = "Cà Phê Truyền Thống", Icon = "coffee", DisplayOrder = 1, IsActive = true },
            new() { Id = CatTeaId, Name = "Trà & Trà Sữa", Icon = "cup", DisplayOrder = 2, IsActive = true },
            new() { Id = CatPastryId, Name = "Bánh Ngọt & Croissant", Icon = "croissant", DisplayOrder = 3, IsActive = true }
        };
        await context.Categories.AddRangeAsync(categories);

        var products = new List<Product>
        {
            new()
            {
                Id = ProdBacXiuId,
                CategoryId = CatCoffeeId,
                Name = "Bạc Xỉu Sài Gòn",
                Description = "Espresso đậm đà kết hợp sữa đặc béo ngậy và sữa tươi thanh trùng.",
                BasePrice = 35000m,
                Allergens = "Sữa",
                IsAvailable = true,
                IsBestSeller = true,
                RecipeInstructions = "Espresso 1 shot (18ml) + Sữa đặc 30ml + Sữa tươi 40ml + Đá 150g",
                DisplayOrder = 1
            }
        };
        await context.Products.AddRangeAsync(products);

        await context.SaveChangesAsync();
    }
}
```

---

# 7. KẾT LUẬN VÀ BƯỚC TIẾP THEO (CONCLUSION & NEXT STEPS)
Tài liệu Phân đoạn 6 có nền tảng cấu trúc tốt. Sau khi dọn dẹp file redirect stub, bổ sung `.editorconfig`, mở rộng 35 UAT test cases và hoàn thiện `DbInitializer.cs` cùng file `seed-data.json`, **phân đoạn 6 sẽ sẵn sàng 100% để phục vụ công tác phát triển và nghiệm thu của dự án.**
```

---

# 9. KẾT LUẬN TỔNG THỂ & KHUYẾN NGHỊ BÀN GIAO (SYNTHESIS CONCLUSION)

Báo cáo kiểm toán này là sản phẩm tổng hợp chuyên sâu của toàn bộ quy trình Document Review 6 phân đoạn thuộc dự án **Smart F&B Operating System**. 

Bằng việc xác lập rõ **7 Điểm Nghẽn Kỹ Thuật Cốt Tử (7 Critical Blockers)**, xây dựng **Bảng kiểm kê toàn diện 39 tệp tin**, chuẩn hóa **7 Giải pháp Kiến trúc Xuyên suốt**, và phân công **Kế hoạch hành động chi tiết cho 4 Developers**, bản báo cáo này cung cấp kim chỉ nam kỹ thuật chuẩn xác, bảo đảm hệ thống Smart F&B OS sẽ được triển khai đúng tiến độ, đạt độ tin cậy cấp doanh nghiệp (Enterprise Grade) và bảo vệ thành công xuất sắc trước Hội đồng thẩm định.

---
*Báo cáo được biên soạn và phê duyệt bởi Lead Synthesizer — Teamwork Documentation Review System.*
