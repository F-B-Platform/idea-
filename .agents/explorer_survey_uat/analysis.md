# 📊 BẢN PHÂN TÍCH KHẢO SÁT & BẢN THIẾT KẾ NÂNG CẤP UAT TEST CASES (v2.5.0)
## Hệ Thống Smart F&B Operating System (AI-Powered QR Order & Management Platform)

> **Mã tài liệu:** `ANALYSIS-UAT-V250`  
> **Người thực hiện:** Explorer Subagent (Survey & Analysis)  
> **Dự án:** Smart F&B Operating System  
> **Mục tiêu:** Phân tích, tổng hợp toàn diện các nguồn sự thật kỹ thuật (Master Spec v2.5.0, 4 Actors 62 Features, 16 Workflows, Database Schema, Sequence Diagrams, Test Plan) để cung cấp bản thiết kế chuẩn mực 100% phục vụ việc viết lại tệp `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`.

---

## 📑 MỤC LỤC BẢN PHÂN TÍCH

1. [TỔNG HỢP NGUỒN SỰ THẬT & ĐẶC TẢ KỸ THUẬT V2.5.0](#1-tổng-hợp-nguồn-sự-thật--đặc-tả-kỹ-thuật-v250)
2. [DANH MỤC CÁC THÀNH PHẦN LỖI THỜI CẦN LOẠI BỎ (PURGE LIST)](#2-danh-mục-các-thành-phần-lỗi-thời-cần-loại-bỏ-purge-list)
3. [THIẾT KẾ KỊCH BẢN DEMO 5 PHÚT KẾT NỐI LIÊN HOÀN (7 SCENES / ACTORS)](#3-thiết-kế-kịch-bản-demo-5-phút-kết-nối-liên-hoàn-7-scenes--actors)
4. [CẤU TRÚC MA TRẬN 35+ TEST CASES UAT TOÀN DIỆN V2.5.0](#4-cấu-trúc-ma-trận-35-test-cases-uat-toàn-diện-v250)
5. [ĐẶC TẢ CHI TIẾT TỪNG PHÂN HỆ VÀ CÁC TEST CASES TRỌNG TÂM](#5-đặc-tả-chi-tiết-từng-phân-hệ-và-các-test-cases-trọng-tâm)
6. [ĐẶC TẢ MA TRẬN 10 KỊCH BẢN BIÊN (TC-EDGE-01 ~ TC-EDGE-10)](#6-đặc-tả-ma-trận-10-kịch-bản-biên-tc-edge-01--tc-edge-10)
7. [QUY CHUẨN ĐỊNH DẠNG GITHUB ALERT CALLOUTS](#7-quy-chuẩn-định-dạng-github-alert-callouts)
8. [KẾT LUẬN & HƯỚNG DẪN TRIỂN KHAI WRITER SUBAGENT](#8-kết-luận--hướng-dẫn-triển-khai-writer-subagent)

---

## 1. TỔNG HỢP NGUỒN SỰ THẬT & ĐẶC TẢ KỸ THUẬT V2.5.0

Qua quá trình rà soát đối chiếu 7 tài liệu kỹ thuật cốt lõi của dự án:
- `01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md` (Master Spec v2.5.0)
- `01_Tai_Lieu_Dac_Ta_Goc/Actor_Phan_Quyen_Chuc_Nang.md` (4 Actors, 62 Core Features RBAC)
- `01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md` (16 Business Workflows)
- `03_Quy_Trinh_Trien_Khai/07_Ke_Hoach_Kiem_Thu.md` (Comprehensive Test Plan & Testing Pyramid)
- `04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md` (10 Architectural Sequence Diagrams)
- `05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md` (Tệp hiện hữu cần nâng cấp)

Hệ thống xác lập **5 Trụ cột nghiệp vụ nền tảng v2.5.0**:
1. **Dine-In 2 Nhánh Thanh Toán Linh Hoạt:**
   - *Nhánh A (VietQR Trả trước):* Khách quét QR -> Chọn món -> Thanh toán VietQR qua PayOS -> Webhook xác nhận -> KDS Bếp **MỚI NHẬN ĐƠN** qua SignalR (`PendingPayment` -> `Paid` -> `Confirmed` -> `Preparing` -> `Ready` -> `Served`).
   - *Nhánh B (Tiền mặt Trả sau):* Khách quét QR -> Chọn tiền mặt -> Đơn vào KDS Bếp **NGAY LẬP TỨC** (`Confirmed` -> `Preparing` -> `Ready` -> In bill nhiệt có mã VietQR động -> Bưng nước + Bill ra bàn -> Thu tiền mặt hoặc quét VietQR trên bill -> `Paid`).
2. **QR Delivery (Giao Hàng Tận Nơi):**
   - Quét mã QR Delivery riêng biệt (poster/fanpage/standee).
   - Bắt buộc nhập Tên, SĐT (10 số VN) và Địa chỉ giao hàng chi tiết.
   - Tự động cộng **Phí ship cố định 20.000 VNĐ** vào giỏ hàng.
   - **100% Thanh toán trước qua VietQR** (Khóa hoàn toàn tùy chọn COD).
   - KDS hiển thị vé tím `[GIAO HÀNG #DEL-XXXX]` kèm SĐT và địa chỉ giao.
3. **Takeaway Staff Web POS (Bán Mang Về Tại Quầy) & Loyalty 10 Ly:**
   - Nhân viên thu ngân thao tác trên Web POS `(staff)/pos` (Không dùng mã QR).
   - Tra cứu CRM bằng SĐT khách hàng: hiển thị số ly tích lũy (`CupBalance`).
   - Chính sách Loyalty: **Tích 10 ly = Tặng 1 ly miễn phí (CHỈ ÁP DỤNG DUY NHẤT CHO ĐƠN TAKEAWAY)**.
   - Khách nhận nước và thanh toán sau (Tiền mặt tự tính tiền thối hoặc VietQR quầy).
4. **Chấm Công Khóa Mạng WiFi (WiFi-Locked Attendance):**
   - Xác thực kép 2 lớp: (a) Địa chỉ BSSID Access Point và dải Subnet IP của mạng WiFi chi nhánh (bảng `branch_wifi_configs`), (b) Mã số nhân viên (`EmployeeCode`).
   - Bật 4G hoặc kết nối WiFi ngoài -> Lập tức từ chối HTTP 403 Forbidden.
5. **Hợp Nhất 100% Nền Tảng Web Responsive (Loại bỏ Staff Mobile App):**
   - 100% vận hành trên Next.js 14 App Router Monorepo: `(customer)` PWA, `(kds)` Web KDS Full-screen, `(staff)` Web POS Quầy & Sơ đồ bàn, `(manager)` Quản lý ca & Kho, `(admin)` Điều hành trung tâm.

---

## 2. DANH MỤC CÁC THÀNH PHẦN LỖI THỜI CẦN LOẠI BỎ (PURGE LIST)

Bản nâng cấp UAT Test Cases v2.5.0 phải loại bỏ triệt để và không để sót bất kỳ dấu vết nào của các thành phần sau:

| Thành phần lỗi thời (Obsolete) | Lý do loại bỏ | Giải pháp chuẩn hóa thay thế v2.5.0 |
|---|---|---|
| ❌ **Staff Mobile App** (Flutter/React Native) | Tốn chi phí phát hành App Store / Google Play và bảo trì đa nền tảng | **100% Web Responsive** trên Next.js 14 (`(staff)` và `(kds)`) |
| ❌ **Định vị GPS 50m** khi chấm công | Sai số lớn khi nhân viên đứng trong nhà/tầng hầm (20-50m) | **WiFi-Locked Attendance** (Xác thực BSSID Router + Subnet IP chi nhánh) |
| ❌ **Mã QR động 30 giây** chấm công | Gây nghẽn thiết bị và phiền hà cho nhân viên | **Xác thực mạng WiFi chi nhánh + Mã NV** trực tiếp trên Web Staff |
| ❌ **Tính năng C-23 & C-24 cũ** (Share mạng xã hội, Push notification) | Không nằm trong phạm vi nghiệp vụ cốt lõi F&B | Đã loại bỏ hoàn toàn, hệ thống chỉ giữ 62 tính năng chuẩn |
| ❌ **Mã QR Takeaway cho khách quét** | Trùng lặp quy trình và khó kiểm soát thanh toán | **Nhân viên thu ngân thao tác 100% trên Web POS Quầy** |
| ❌ **Chỉ có 1 luồng Dine-In Pre-Payment** | Cứng nhắc, không phục vụ được khách lớn tuổi/tiền mặt | **Tách biệt 2 nhánh:** Nhánh A VietQR trước & Nhánh B Tiền mặt trả sau |
| ❌ **Đổi ly 10 ly áp dụng cho mọi kênh** | Gây thâm hụt biên lợi nhuận kênh Dine-In/Delivery | **Chương trình 10 ly tặng 1 ly CHỈ áp dụng riêng cho đơn Takeaway** |

---

## 3. THIẾT KẾ KỊCH BẢN DEMO 5 PHÚT KẾT NỐI LIÊN HOÀN (7 SCENES / ACTORS)

Kịch bản Demo trước Hội đồng Capstone được thiết kế kéo dài đúng 5 phút, liên kết liên hoàn 7 cảnh quay (scenes) chứng minh tính nhất quán dữ liệu thời gian thực giữa 4 nhóm Actor:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        KỊCH BẢN DEMO THỰC THẾ TRƯỚC HỘI ĐỒNG CAPSTONE (5 PHÚT LIÊN HOÀN)               │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                        │
│  ⏱️ [0:00 - 0:45] SCENE 1: QUẢN LÝ MỞ CA KÉT TIỀN & NHÂN VIÊN CHẤM CÔNG WIFI                          │
│  • Quản lý đăng nhập Web Manager (/manager/shifts), khai báo tiền mặt đầu ca: 1.500.000 VNĐ -> Mở ca. │
│  • Barista kết nối WiFi 'SmartCoffee_Q1' (BSSID 00:14:22:01:23:45, IP 192.168.1.45), mở Web Staff     │
│    (/staff/attendance), nhập mã 'NV-Q1-008' -> Thẻ xanh: 'Chấm công thành công qua WiFi chi nhánh'.   │
│  • [ĐỐI CHỨNG AN NINH]: Tắt WiFi, bật 4G thử chấm công lại -> Hệ thống từ chối HTTP 403 Forbidden.   │
│                                                                                                        │
│  ⏱️ [0:45 - 2:00] SCENE 2: KHÁCH ĐẶT DINE-IN 2 NHÁNH (NHÁNH A VIETQR & NHÁNH B TIỀN MẶT)             │
│  • [Nhánh A - Bàn 04 VietQR Trước]: Khách quét QR Bàn 04 -> Chatbot AI-1 (Gemini Flash RAG):          │
│    'Trời 34 độ, tư vấn món mát ít ngọt' -> AI gợi ý Trà Đào Cam Sả (53k) -> Khách chọn VietQR         │
│    -> Đơn tạo 'PendingPayment' -> KDS BẾP CHƯA NHẬN ĐƠN -> Khách quét PayOS 53k -> Webhook xác nhận   │
│    -> Đơn chuyển 'Paid' -> KDS Bếp rung chuông 🔔 nhận đơn tức thì.                                   │
│  • [Nhánh B - Bàn 05 Tiền Mặt Sau]: Khách Bàn 05 chọn Bạc Xỉu (35k), chọn Tiền Mặt                    │
│    -> Đơn vào KDS Bếp NGAY LẬP TỨC ('Confirmed') -> Barista bấm Ready -> Máy in nhiệt tự động in bill │
│    có mã VietQR động -> Phục vụ bưng nước kèm bill ra bàn -> Khách quét QR trên bill hoặc trả tiền.  │
│                                                                                                        │
│  ⏱️ [2:00 - 2:45] SCENE 3: KHÁCH ĐẶT GIAO TẬN NƠI (QR DELIVERY 20K SHIP, 100% VIETQR)                 │
│  • Khách quét QR Delivery -> Bắt buộc nhập Tên 'Mai Hương', SĐT '0987654321', Địa chỉ 'Bitexco Q1'   │
│    -> Chọn 2 Trà Đào (70k) -> Hệ thống tự cộng Phí ship cố định 20.000đ -> Tổng: 90.000đ.             │
│  • Khóa COD, thanh toán 100% VietQR -> KDS Bếp nhận Ticket màu tím `[GIAO HÀNG #DEL-0015]`.           │
│                                                                                                        │
│  ⏱️ [2:45 - 3:30] SCENE 4: THU NGÂN TẠO ĐƠN TAKEAWAY TẠI QUẦY & ĐỔI THƯỞNG 10 LY                     │
│  • Khách đến quầy đọc SĐT: 0909123456 -> Thu ngân mở Web POS (/staff/pos) tra cứu:                   │
│    'Nguyễn Hoàng Nam | Tích lũy: 10/10 Ly 🎁 ĐỦ ĐIỀU KIỆN TẶNG 1 LY'.                                 │
│  • Chọn 2 Cà Phê Muối (78k) -> Bấm [ÁP DỤNG ĐỔI 1 LY FREE (-35k)] -> Khách chỉ trả 43.000đ.          │
│  • Khách đưa 100k tiền mặt -> POS tính thối 57.000đ -> In bill -> CRM reset quỹ ly: 10 - 10 + 2 = 2 ly│
│                                                                                                        │
│  ⏱️ [3:30 - 4:15] SCENE 5: KDS BARISTA BOM TRỪ KHO GAM/ML, CÔNG TẮC 86-TOGGLE & UNDO 10S              │
│  • Barista bấm Hoàn tất -> BOM Engine tự trừ kho: Cà phê (-80g), Sữa (-120ml) -> Log inventory_logs. │
│  • Barista phát hiện hết Đào ngâm -> Bật 86-Toggle món 'Trà Đào Cam Sả' -> Trong < 1s, menu PWA của   │
│    toàn bộ khách trong quán mờ món và khóa nút đặt hàng.                                              │
│  • Barista bấm nhầm hoàn tất món -> Nút Undo 10s xuất hiện cho phép khôi phục trạng thái tức thì.     │
│                                                                                                        │
│  ⏱️ [4:15 - 4:45] SCENE 6: QUẢN LÝ KẾT CA & ĐỐI SOÁT Z-REPORT (GIẢI TRÌNH LỆCH > 50K)                 │
│  • Quản lý vào Kết ca: Tiền lý thuyết: 1.500.000đ (đầu ca) + 43.000đ (tiền mặt) = 1.543.000đ.        │
│  • Thu ngân đếm két thực tế: 1.613.000đ (Lệch +70.000đ > 50k threshold).                             │
│  • Hệ thống khóa kết ca -> Thu ngân nhập giải trình 'Khách tip vào két 70k' + Quản lý nhập PIN 9988   │
│    -> Đóng ca thành công & In biên bản Z-Report.                                                      │
│                                                                                                        │
│  ⏱️ [4:45 - 5:00] SCENE 7: ADMIN DASHBOARD P&L, BẢNG GIÁ VÙNG & PHÊ DUYỆT AI-2 COMBO                 │
│  • Admin mở /admin/dashboard: Doanh thu nhảy tức thì, báo cáo P&L tự động tính Net Revenue, COGS, Lãi.│
│  • Admin duyệt gợi ý AI-2 Apriori: Combo {Cà phê muối + Croissant} (Lift 2.45) -> Giảm 15% -> Public.│
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. CẤU TRÚC MA TRẬN 35+ TEST CASES UAT TOÀN DIỆN V2.5.0

Bộ kiểm thử nghiệm thu UAT được cấu trúc thành **12 Phân hệ** với hơn **35 Test Cases** chi tiết, bao phủ 100% các luồng nghiệp vụ và 10 trường hợp biên quan trọng:

| Phân hệ (Module) | Danh sách Mã Test Cases | Số lượng | Mức độ ưu tiên |
|---|---|:---:|:---:|
| **1. Xác thực & Phân quyền (Auth & RBAC)** | `TC-AUTH-01`, `TC-AUTH-02`, `TC-AUTH-03`, `TC-AUTH-04` | 4 | High |
| **2. Thực đơn & Tùy biến món (Menu & Modifiers)** | `TC-MENU-01`, `TC-MENU-02`, `TC-MENU-03`, `TC-MENU-04` | 4 | High |
| **3. Đặt món Tại bàn (Dine-In 2 Flows)** | `TC-DINE-01A`, `TC-DINE-01B`, `TC-DINE-02`, `TC-DINE-03`, `TC-DINE-04` | 5 | Critical |
| **4. Đặt hàng Giao tận nơi (QR Delivery)** | `TC-DEL-01`, `TC-DEL-02`, `TC-DEL-03`, `TC-DEL-04` | 4 | Critical |
| **5. Bán hàng Quầy & Tích Ly (Takeaway POS & Loyalty)** | `TC-TAKE-01`, `TC-TAKE-02`, `TC-TAKE-03`, `TC-TAKE-04` | 4 | Critical |
| **6. Chấm công Khóa WiFi (WiFi-Locked Attendance)** | `TC-ATT-01`, `TC-ATT-02`, `TC-ATT-03`, `TC-ATT-04` | 4 | Critical |
| **7. Điều phối Bếp & BOM Kho (Web KDS & Inventory)** | `TC-KDS-01`, `TC-KDS-02`, `TC-KDS-03`, `TC-KDS-04` | 4 | High |
| **8. Quản lý Ca & Đối soát Két (Shift & Z-Report)** | `TC-SHIFT-01`, `TC-SHIFT-02`, `TC-SHIFT-03` | 3 | High |
| **9. Đánh giá & Phản hồi (Reviews & Red Alert)** | `TC-REV-01`, `TC-REV-02`, `TC-REV-03` | 3 | Medium |
| **10. Trí tuệ Nhân tạo (AI-1 Chatbot & AI-2 Combo)** | `TC-AI-01`, `TC-AI-02`, `TC-AI-03` | 3 | High |
| **11. Quản trị Trung tâm (Admin Central Operations)** | `TC-ADM-01`, `TC-ADM-02`, `TC-ADM-03` | 3 | High |
| **12. Ma trận Kịch bản Biên & Ngoại lệ (Edge Cases)** | `TC-EDGE-01` ~ `TC-EDGE-10` | 10 | Critical |
| **TỔNG CỘNG** | **47 Test Cases chi tiết** | **47** | **100% PASS** |

---

## 5. ĐẶC TẢ CHI TIẾT TỪNG PHÂN HỆ VÀ CÁC TEST CASES TRỌNG TÂM

Mỗi Test Case trong tài liệu UAT bắt buộc phải tuân thủ nghiêm ngặt định dạng 7 trường tiêu chuẩn:
1. **Mã test (Test ID)**
2. **Mục đích (Objective)**
3. **Tiền điều kiện (Preconditions)**
4. **Các bước thực hiện (Execution Steps)**
5. **Dữ liệu đầu vào (Test Data / Payloads)**
6. **Kết quả kỳ vọng (Expected Results)**
7. **Tiêu chí nghiệm thu & Trạng thái (Acceptance Criteria & Status)**

### 5.1 Phân hệ Đặt món Tại bàn Dine-In (Dine-In 2 Flows)
- **`TC-DINE-01A` (Nhánh A VietQR Trả trước):** Khách chọn VietQR -> Tạo đơn `PendingPayment` -> Sinh mã PayOS 53k -> KDS Bếp CHƯA hiển thị đơn -> Khách quét chuyển khoản -> Webhook PayOS xác nhận -> Đơn chuyển `Paid`/`Confirmed` -> KDS Bếp rung chuông 🔔 nhận đơn trong < 500ms.
- **`TC-DINE-01B` (Nhánh B Tiền mặt Trả sau):** Khách chọn Tiền mặt -> Đơn tạo `Confirmed` ngay lập tức -> KDS Bếp NHẬN ĐƠN NGAY -> Barista pha chế bấm `Ready` -> Lệnh in nhiệt tự động in Hóa đơn tạm tính có sẵn Mã VietQR động -> Nhân viên bưng nước + Bill ra bàn -> Khách trả tiền mặt hoặc quét VietQR trên bill -> Nhân viên bấm xác nhận -> Đơn hoàn tất `Paid`.
- **`TC-DINE-02` (Gọi phục vụ tại bàn & Rate-limit):** Khách bấm chuông trên PWA chọn lý do "Lấy thêm đá" -> SignalR phát chuông & banner cam trên Web POS -> Khách bấm gọi liên tục trong 60s bị chặn HTTP 429.
- **`TC-DINE-03` (Hết hạn thanh toán VietQR 10 phút):** Đơn `PendingPayment` sau 10 phút không thanh toán -> Hangfire Cron Job tự động hủy đơn (`Cancelled`), giải phóng bàn và hoàn trả tồn kho tạm giữ.

### 5.2 Phân hệ Đặt hàng Giao tận nơi (QR Delivery)
- **`TC-DEL-01` (Đặt hàng QR Delivery đầy đủ):** Khách quét QR Delivery -> Bắt buộc nhập Tên, SĐT, Địa chỉ chi tiết -> Hệ thống tự cộng Phí ship cố định 20.000 VNĐ -> Thanh toán 100% VietQR -> KDS Bếp nhận vé tím `[GIAO HÀNG]`.
- **`TC-DEL-02` (Validation chặn thiếu địa chỉ/SĐT):** Khách để trống địa chỉ hoặc nhập dưới 10 ký tự -> Frontend validate chặn submit, Backend trả về HTTP 400 `DELIVERY_ADDRESS_REQ`.
- **`TC-DEL-03` (Chặn chọn Tiền mặt COD):** Giao diện Delivery không có tùy chọn COD; nếu cố tình gửi payload `PaymentMethod: "CASH"` -> Backend từ chối HTTP 400 `COD_NOT_ALLOWED`.

### 5.3 Phân hệ Bán hàng Mang về tại Quầy (Takeaway Web POS) & Loyalty 10 Ly
- **`TC-TAKE-01` (Tra cứu CRM & Đổi 1 ly miễn phí khi đủ 10 ly):** Thu ngân nhập SĐT `0909123456` có `CupBalance = 10` -> POS hiển thị huy hiệu đủ điều kiện đổi thưởng -> Thu ngân chọn 2 ly Cà Phê Muối (78k) và bấm [Đổi 1 Ly Free] -> Giảm 100% giá 1 ly tiêu chuẩn (-35k), khách chỉ trả 43k -> Hoàn tất đơn -> CRM cập nhật `10 - 10 + 2 = 2 ly`.
- **`TC-TAKE-02` (Thanh toán tiền mặt & Tự tính tiền thối):** Thu ngân nhập tiền khách đưa 100k -> Hệ thống tự tính tiền thừa 57k và kích hoạt mở két tiền.
- **`TC-TAKE-03` (Tạo mới hồ sơ CRM cho khách vãng lai):** Nhập SĐT mới -> Nhập tên khách -> Hệ thống tự động tạo bản ghi CRM mới với `CupBalance = 0`.
- **`TC-TAKE-04` (Chặn đổi ly cho đơn Dine-In / Delivery):** Cố tình áp dụng giảm trừ 10 ly cho đơn Dine-In hoặc Delivery -> Backend chặn ném lỗi HTTP 400 `LOYALTY_TAKEAWAY_ONLY`.

### 5.4 Phân hệ Chấm công Khóa mạng WiFi (WiFi-Locked Attendance)
- **`TC-ATT-01` (Chấm công thành công đúng WiFi quán):** Thiết bị kết nối WiFi quán (Subnet `192.168.1.0/24`, BSSID `00:14:22:01:23:45`), nhập mã `NV-Q1-008` -> Chấm công thành công, hiển thị thẻ xanh `is_wifi_verified = true`.
- **`TC-ATT-02` (Từ chối khi dùng 4G / WiFi ngoài):** Tắt WiFi, bật 4G (IP ngoài mạng `14.169.12.88`) -> Hệ thống từ chối HTTP 403 Forbidden: "Vui lòng kết nối đúng mạng WiFi chi nhánh".
- **`TC-ATT-03` (Từ chối khi sai Mã nhân viên):** Nhập mã `NV-UNKNOWN-999` -> Hệ thống báo lỗi HTTP 404 Not Found.

### 5.5 Phân hệ Điều phối Bếp & BOM Kho (Web KDS & Inventory)
- **`TC-KDS-01` (Nhận đơn SignalR & Chuyển trạng thái):** KDS nhận đơn thời gian thực < 300ms -> Barista bấm Bắt đầu (`Preparing`) -> Bấm Hoàn thành (`Ready`) -> PWA khách cập nhật mượt mà.
- **`TC-KDS-02` (Khấu trừ BOM theo gam/ml khi Ready):** Bấm `Ready` cho 2 ly Matcha Latte Size L -> BOM Engine tự trừ kho: 30g Bột Matcha, 360ml Sữa tươi -> Ghi nhận `inventory_logs`. Nếu chạm ngưỡng tối thiểu -> Bắn `LowStockAlert` tới Quản lý.
- **`TC-KDS-03` (Khóa món khẩn cấp 86-Toggle):** Barista gạt công tắc 86-Toggle món "Trà Đào" trên KDS -> SignalR đồng bộ tới toàn bộ PWA khách trong quán trong < 1s làm mờ món và khóa nút giỏ hàng.
- **`TC-KDS-04` (Tính năng Undo 10s trên KDS):** Barista lỡ bấm nhầm `Ready` -> Nút Undo đếm ngược 10s cho phép phục hồi trạng thái về `Preparing` và hoàn lại tồn kho BOM.

### 5.6 Phân hệ Quản lý Ca & Đối soát Két tiền (Shift & Z-Report)
- **`TC-SHIFT-01` (Mở ca đầu ngày):** Khai báo tiền mặt đầu ca: 1.500.000 VNĐ -> Tạo bản ghi `WorkShifts` trạng thái `Open`.
- **`TC-SHIFT-02` (Kết ca & Bắt buộc giải trình khi chênh lệch > 50k):** Tiền lý thuyết: 1.543.000đ; Thực đếm: 1.613.000đ (Chênh lệch +70.000đ > 50k) -> Hệ thống khóa kết ca, bắt buộc nhập lý do giải trình + Quản lý nhập mã PIN 9988 -> Đóng ca và in biên bản Z-Report.

### 5.7 Phân hệ Trí tuệ Nhân tạo (AI-1 Chatbot & AI-2 Combo)
- **`TC-AI-01` (Chatbot AI-1 Gemini RAG):** Khách hỏi "Trưa nóng 35 độ có món gì mát ít calo" -> Gemini kết hợp thời tiết 35°C + catalog món -> Tư vấn Trà Đào Cam Sả kèm nút "Thêm vào giỏ hàng ngay" 1 chạm.
- **`TC-AI-02` (AI-2 Khai phá Apriori & Admin duyệt Combo):** Thuật toán Apriori quét giỏ hàng lịch sử phát hiện `{Cà phê muối + Croissant}` (Lift 2.45) -> Admin xem xét, chỉnh giảm giá 15% và bấm [Phê duyệt & Phát hành] -> Combo xuất hiện ngay đầu Menu PWA.
- **`TC-AI-03` (Fallback Rule-based khi AI Timeout):** Gemini API timeout > 3s -> Kích hoạt Fallback trả về Top 3 Best-Seller thống kê mà không gây crash UI.

### 5.8 Phân hệ Quản trị Trung tâm (Admin Operations)
- **`TC-ADM-01` (Admin Full CRUD Món & Định mức BOM):** Tải ảnh nén WebP lên CDN S3, tạo món mới kèm kích cỡ S/M/L và định lượng BOM gam/ml chi tiết -> Xóa cache Redis menu -> Đồng bộ toàn chuỗi.
- **`TC-ADM-02` (Quản trị Bảng giá vùng chi nhánh):** Cấu hình bảng giá Sân Bay (+20%) -> Khách quét QR tại chi nhánh Sân Bay tự động nạp bảng giá điều chỉnh chính xác.
- **`TC-ADM-03` (Lên lịch Thực đơn theo mùa Seasonal Menu):** Lên lịch Menu Giáng Sinh (01/12 - 31/12) qua Hangfire Cron Job -> Tự động kích hoạt và tự động ẩn khi hết hạn.

---

## 6. ĐẶC TẢ MA TRẬN 10 KỊCH BẢN BIÊN (TC-EDGE-01 ~ TC-EDGE-10)

| Mã Test Case | Tên Kịch Bản Biên | Điều Kiện Kích Hoạt | Cơ Chế Xử Lý & Bất Biến Bảo Vệ | Kết Quả Kỳ Vọng |
|:---:|---|---|---|---|
| **`TC-EDGE-01`** | **Race Condition Đặt Món Cùng Bàn** | 2 khách cùng quét 1 mã bàn và bấm đặt hàng đồng thời tại cùng mili-giây | Phân tán RedLock `lock:table:{tableId}` thời hạn 15s | 1 đơn tạo thành công 201, đơn thứ 2 nhận 409 Conflict |
| **`TC-EDGE-02`** | **PayOS Webhook Gửi Trùng Lặp** | Cổng PayOS gửi lại cùng 1 webhook nhiều lần do mạng chập chờn | Redis Idempotency Key `webhook:vietqr:{transId}` | Lần 1 kích hoạt đơn `Paid` & KDS. Lần 2 trả 200 OK ngay mà không gửi vé lần 2 |
| **`TC-EDGE-03`** | **Khóa Món 86 Đúng Lúc Đang Checkout** | Barista bấm 86-Toggle hết món đúng tích tắc khách bấm thanh toán | Concurrency check `product_branch_prices.is_available` | Trả về HTTP 409 Conflict: "Món vừa tạm hết, vui lòng chọn món khác" |
| **`TC-EDGE-04`** | **Hết Hạn Thanh Toán VietQR (TTL 10m)** | Khách tạo đơn VietQR nhưng không chuyển khoản sau 10 phút | Hangfire Worker tự động quét và chuyển trạng thái `Cancelled` | Hủy đơn, giải phóng bàn và hoàn trả nguyên liệu tạm giữ |
| **`TC-EDGE-05`** | **Gian Lận Chấm Công Bằng 4G / Fake IP** | Nhân viên dùng 4G hoặc Fake IP chấm công từ xa | Xác thực 2 lớp: Subnet IP (`192.168.1.0/24`) và BSSID Access Point | Chặn 100% từ chối HTTP 403 và ghi log an ninh |
| **`TC-EDGE-06`** | **Lệch Két Tiền Cuối Ca Vượt Ngưỡng** | Kiểm đếm két tiền lệch `\|variance\| > 50.000đ` | Bắt buộc nhập giải trình + Quản lý nhập mã PIN duyệt | Khóa kết ca cho đến khi có giải trình hợp lệ, lưu vào `shift_handover_discrepancies` |
| **`TC-EDGE-07`** | **Âm Kho Khi Trừ Định Lượng BOM** | Kho quầy bar không đủ số lượng do quên lập phiếu xuất | Vẫn cho phép hoàn tất đơn hàng, trừ tồn âm màu đỏ | Không gián đoạn phục vụ khách, phát `LowStockAlert` khẩn cấp cho Quản lý |
| **`TC-EDGE-08`** | **Lạm Dụng Đổi 10 Ly Sai Kênh Bán** | Cố tình gửi request đổi 10 ly cho đơn Dine-In hoặc Delivery | Domain rule kiểm tra `OrderType == TakeAway` | Ném lỗi HTTP 400 Bad Request: `LOYALTY_TAKEAWAY_ONLY` |
| **`TC-EDGE-09`** | **Gemini AI API Gặp Sự Cố / Quá Tải** | Google Gemini API timeout > 3s hoặc mã lỗi 500 | Circuit Breaker kích hoạt Rule-based Fallback Engine | Chatbot phản hồi mượt mà Top 3 Best-Seller, không crash UI |
| **`TC-EDGE-10`** | **Mất Kết Nối SignalR WebSockets** | Rớt mạng WiFi quán tạm thời trong 15 giây | Client kích hoạt Auto-Reconnect (Exponential Backoff) | Tự động kết nối lại và đồng bộ toàn bộ đơn phát sinh qua API |

---

## 7. QUY CHUẨN ĐỊNH DẠNG GITHUB ALERT CALLOUTS

Toàn bộ tài liệu UAT phải sử dụng chuẩn Markdown GitHub Alert Callouts:

```markdown
> [!NOTE]
> Thông tin lưu ý quan trọng về kiến trúc và phạm vi nghiệm thu.

> [!IMPORTANT]
> Quy tắc nghiệp vụ bắt buộc không được phép vi phạm.

> [!TIP]
> Gợi ý tối ưu thao tác demo và cấu hình hệ thống.

> [!WARNING]
> Cảnh báo về an ninh, gian lận hoặc sai lệch tài chính.
```

---

## 8. KẾT LUẬN & HƯỚNG DẪN TRIỂN KHAI WRITER SUBAGENT

Bản phân tích này cung cấp đầy đủ 100% dữ liệu kỹ thuật và cấu trúc chuẩn mực để tiến hành viết lại toàn diện tệp `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`.

Các cam kết chất lượng khi xuất bản file đích:
1. **Zero Placeholders:** Không sử dụng `// TODO`, `/* rest of code */`, `...`. Mọi Test Case đều viết đầy đủ 7 trường thông tin với Payload JSON thực tế.
2. **Loại bỏ 100% Obsolete References:** Không có Staff Mobile App, không có GPS 50m, không có QR 30s, không có C-23/C-24.
3. **Độ phủ kiểm thử:** Đạt 47 Test Cases (37 Module Cases + 10 Critical Edge Cases).
4. **Kịch bản Demo 5 phút:** 7 Scenes liên hoàn rõ ràng theo mốc thời gian thực tế.
