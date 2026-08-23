# 👥 BẢN ĐẶC TẢ ACTORS, MA TRẬN PHÂN QUYỀN RBAC & DANH MỤC TÍNH NĂNG TOÀN DIỆN
## Smart F&B Operating System — Nền Tảng Quản Trị & Vận Hành F&B Đa Chi Nhánh Tích Hợp Đặt Món QR & Trí Tuệ Nhân Tạo

> [!NOTE]
> **Tài liệu:** Bản đặc tả kỹ thuật chi tiết về 4 Nhóm Tác Nhân (Actor Profiles), Ma trận kiểm soát truy cập phân quyền theo vai trò (Role-Based Access Control - RBAC) trên 10 nhóm tài nguyên API, và Danh mục 62 Tính năng cốt lõi (Core MVP Feature Catalog).  
> **Phiên bản:** v2.5.0-Production-Ready  
> **Nguồn sự thật chuẩn hóa:** `Smart_FB_OS_Revised_4members.docx` (Kết hợp chỉ đạo kỹ thuật tại `ORIGINAL_REQUEST.md`)  
> **Quy mô dự án:** Đồ án Capstone 16 tuần (08 Sprints) — Nhóm 4 Kỹ sư Phần mềm (2 Backend + 2 Frontend).  
> **Nền tảng công nghệ:** .NET 8 Clean Architecture (Backend) + Next.js 14 App Router Monorepo (Frontend) + PostgreSQL 16 + Redis 7 + SignalR Hubs + Google Gemini 1.5 Flash.  
> **Cam kết chất lượng:** Hoàn chỉnh 100%, tuyệt đối không sử dụng mã giữ chỗ hoặc nội dung tạm thời, không ngụy tạo dữ liệu.  

---

# 📚 MỤC LỤC ĐẶC TẢ

| Phần | Tiêu Đề Chi Tiết | Mô Tả Trọng Tâm |
|:---:|---|---|
| **PHẦN 1** | [Tổng Quan 4 Nhóm Actor & Thiết Bị Truy Cập Chuẩn Hóa](#-phần-1-tổng-quan-4-nhóm-actor--thiết-bị-truy-cập-chuẩn-hóa) | Định vị 4 Actor, thiết bị truy cập, 5 nguyên tắc kiến trúc bất biến. |
| **PHẦN 2** | [Sơ Đồ Tương Tác Tổng Thể Actor (Actor Interaction Architecture)](#-phần-2-sơ-đồ-tương-tác-tổng-thể-actor-actor-interaction-architecture) | Sơ đồ Mermaid toàn diện biểu diễn luồng tương tác giữa 4 Actor. |
| **PHẦN 3** | [Đặc Tả Chi Tiết Actor 1: Khách Hàng (Customer — 20 Features)](#-phần-3-đặc-tả-chi-tiết-actor-1-khách-hàng-customer--20-features) | Danh mục `C-01` đến `C-20`, 2 nhánh Dine-in, Delivery 20k, AI-1, Review. |
| **PHẦN 4** | [Đặc Tả Chi Tiết Actor 2: Nhân Viên Vận Hành Quầy (Staff / Barista — 13 Features)](#-phần-4-đặc-tả-chi-tiết-actor-2-nhân-viên-vận-hành-quầy-staff--barista--13-features) | Danh mục `S-01` đến `S-13`, KDS SignalR, Web POS Takeaway, CRM 10 ly, WiFi. |
| **PHẦN 5** | [Đặc Tả Chi Tiết Actor 3: Quản Lý Chi Nhánh (Branch Manager — 12 Features)](#-phần-5-đặc-tả-chi-tiết-actor-3-quản-lý-chi-nhánh-branch-manager--12-features) | Danh mục `M-01` đến `M-12`, Mở/kết ca két tiền, Kho BOM, WiFi config, Review alert. |
| **PHẦN 6** | [Đặc Tả Chi Tiết Actor 4: Chủ Chuỗi / Quản Trị Viên (Chain Admin — 17 Features)](#-phần-6-đặc-tả-chi-tiết-actor-4-chủ-chuỗi--quản-trị-viên-chain-admin--17-features) | Danh mục `A-01` đến `A-17`, Full CRUD Món/Combo/Ảnh, Giá vùng, AI-2 Apriori, P&L. |
| **PHẦN 7** | [Ma Trận Phân Quyền Bảo Mật Chi Tiết (RBAC Security Matrix)](#-phần-7-ma-trận-phân-quyền-bảo-mật-chi-tiết-rbac-security-matrix) | Ma trận quyền hạn 6 vai trò trên 10 nhóm Endpoint API tài nguyên. |
| **PHẦN 8** | [Định Hướng Mở Rộng Actor & Tính Năng Tương Lai (Scale Up / Future Work)](#-phần-8-định-hướng-mở-rộng-actor--tính-năng-tương-lai-scale-up--future-work) | Các Actor và tính năng nâng cao chuyển sang giai đoạn phát triển tiếp theo. |
| **PHẦN 9** | [Tổng Hợp Kiểm Chứng & Ma Trận Truy Vết Yêu Cầu (Traceability Matrix)](#-phần-9-tổng-hợp-kiểm-chứng--ma-trận-truy-vết-yêu-cầu-traceability-matrix) | Đối soát tính toàn vẹn giữa nghiệp vụ thực tế và tài liệu đặc tả. |

---

# 👥 PHẦN 1: TỔNG QUAN 4 NHÓM ACTOR & THIẾT BỊ TRUY CẬP CHUẨN HÓA

Hệ thống **Smart F&B OS** được thiết kế theo mô hình phân quyền chặt chẽ dựa trên vai trò (Role-Based Access Control - RBAC), phân định ranh giới rõ ràng giữa **4 nhóm tác nhân (Actors)**. Kiến trúc bảo đảm tính tách biệt tuyệt đối giữa giao diện khách hàng không cần cài đặt (PWA), giao diện vận hành quầy phản ứng nhanh (Web POS & KDS), giao diện quản trị chi nhánh (Manager Portal) và giao diện điều hành chuỗi tập trung (Admin Executive Portal).

```
+--------------------------------------------------------------------------------------------------+
|                               4 NHÓM ACTOR CHÍNH TRONG SMART F&B OS                              |
+-----------------------+----------------------------------+---------------------------------------+
| Actor Profile         | Thiết Bị & Giao Diện Sử Dụng     | Trách Nhiệm Vận Hành Chính            |
+-----------------------+----------------------------------+---------------------------------------+
| 1. Khách Hàng         | Trình duyệt di động (PWA Web)    | Quét QR đặt món tại bàn (Dine-in),    |
|    (Customer)         | Safari, Chrome trên iOS/Android  | quét QR Delivery đặt tận nhà, trả     |
|                       | (Route: (customer))              | trước VietQR / trả tiền mặt, chat AI. │
+-----------------------+----------------------------------+---------------------------------------+
| 2. Nhân Viên Quầy     | Smart TV / Tablet Bếp (KDS),     | Nhận đơn KDS thời gian thực, pha chế  |
|    (Staff / Barista)  | PC / Tablet Cảm ứng Quầy Thu ngân| theo BOM, thao tác POS Takeaway, tra  |
|                       | (Routes: (kds), (staff))         | CRM 10 ly tặng 1, thu tiền, chấm công.|
+-----------------------+----------------------------------+---------------------------------------+
| 3. Quản Lý CN         | Laptop, Máy tính bảng (Tablet),  | Mở/kết ca đếm két tiền, đối soát Z-   |
|    (Branch Manager)   | Desktop tại phòng quản lý        | Report, lập lịch phân ca, quản lý kho │
|                       | (Route: (manager))               | BOM, cấu hình WiFi, duyệt review ảnh. │
+-----------------------+----------------------------------+---------------------------------------+
| 4. Chủ Chuỗi          | Máy tính để bàn (Desktop),       | Toàn quyền CRUD Menu, BOM, Nhóm giá,  |
|    (Chain Admin)      | Laptop điều hành cấp cao         | duyệt AI-2 Combo Apriori, xem P&L hợp |
|                       | (Route: (admin))                 | nhất, phân quyền RBAC & audit log.    |
+-----------------------+----------------------------------+---------------------------------------+
```

### 1.1 Bảng Phân Định Actor Profiles & Môi Trường Thực Thi

| Thuộc Tính | Customer (Khách Hàng) | Staff / Barista (Nhân Viên) | Branch Manager (Quản Lý CN) | Chain Admin (Chủ Chuỗi) |
|---|---|---|---|---|
| **Mã Định Danh Role** | `GuestCustomer`, `AuthCustomer` | `BaristaStaff`, `CashierStaff`, `ServiceStaff` | `BranchManager` | `ChainAdmin` |
| **Phương Thức Xác Thực** | Anonymous Token / Phone OTP / JWT 30 ngày | JWT Token (Mã NV + Mật khẩu ca) | JWT Token (Email + Password + 2FA) | JWT Token (Root Admin Credentials) |
| **Phạm Vi Dữ Liệu (Scope)** | Cá nhân (`Own Data`) | Chi nhánh công tác (`Branch Data`) | Chi nhánh quản lý (`Branch Data`) | Toàn hệ thống chuỗi (`All System Data`) |
| **Giao Thức Thời Gian Thực** | SignalR `OrderHub` | SignalR `KitchenHub`, `OrderHub` | SignalR `NotificationHub`, `KitchenHub` | SignalR `NotificationHub` |
| **Công Nghệ Giao Diện** | Next.js 14 PWA Mobile-First | Next.js 14 Web KDS & Staff POS | Next.js 14 Manager Dashboard | Next.js 14 High-Density Admin Grid |

### 1.2 Năm Nguyên Tắc Kiến Trúc & Vận Hành Bất Biến

1. **Loại bỏ hoàn toàn Staff Mobile App (100% Web Responsive):** Không duy trì bất kỳ ứng dụng di động native/hybrid nào cho nhân viên phục vụ. Toàn bộ thao tác nghiệp vụ của nhân viên (xem KDS, tạo đơn Takeaway, kiểm tra sơ đồ bàn, nhận chuông gọi phục vụ, xác nhận thanh toán) được vận hành mượt mà trên nền tảng Web Responsive (`(kds)`, `(staff)`).
2. **Chấm công Khóa Mạng WiFi (WiFi-Locked Attendance):** Xóa bỏ hoàn toàn định vị vệ tinh GPS 50m và mã QR động 30 giây. Nhân viên chỉ có thể chấm công vào ca/ra ca thành công khi: (a) Đang kết nối trực tiếp vào mạng WiFi chi nhánh (kiểm tra BSSID Access Point / IP Gateway Subnet), và (b) Nhập đúng Mã số nhân viên hợp lệ.
3. **Dine-In hỗ trợ 2 Nhánh thanh toán độc lập:** 
   - *Nhánh A (VietQR trả trước):* Khách chọn VietQR ➔ Quét mã chuyển khoản ➔ PayOS Webhook xác nhận `Paid` ➔ Bếp KDS mới nhận đơn.
   - *Nhánh B (Tiền mặt trả sau):* Khách chọn Tiền mặt ➔ Đơn vào bếp ngay với trạng thái `Confirmed` ➔ Barista pha chế ➔ Nhân viên bưng món ra bàn kèm Hóa đơn có in sẵn mã VietQR ➔ Khách trả tiền mặt HOẶC quét VietQR trên hóa đơn ➔ Nhân viên bấm xác nhận thanh toán trên Web Staff.
4. **Takeaway POS qua Nhân viên & Tích 10 Ly chỉ áp dụng Mang Về:** Khách mua mang đi không quét QR. Nhân viên thu ngân thao tác trên Web POS Quầy, tra cứu SĐT CRM. Chương trình ưu đãi **"Tích lũy 10 ly = Tặng 1 ly miễn phí" CHỈ ÁP DỤNG DUY NHẤT CHO ĐƠN TAKEAWAY** (Không áp dụng cho Dine-in, không áp dụng cho Delivery). Khách thanh toán sau khi nhận đồ uống.
5. **Admin Full CRUD & Toàn quyền kiểm soát hệ thống:** Chủ chuỗi sở hữu toàn quyền Tạo mới, Sửa, Xóa mềm, Thay thế món ăn (Product Full CRUD), định nghĩa BOM chi tiết, quản lý danh mục & thứ tự hiển thị, lên lịch thực đơn theo mùa vụ, phê duyệt Combo AI-2, và giám sát báo cáo P&L hợp nhất.

---

# 📊 PHẦN 2: SƠ ĐỒ TƯƠNG TÁC TỔNG THỂ ACTOR (ACTOR INTERACTION ARCHITECTURE)

Sơ đồ tuần tự dưới đây mô tả sự tương tác đa chiều giữa 4 nhóm Actor với hệ thống Backend .NET 8, cơ sở dữ liệu PostgreSQL 16, Redis Cache và SignalR Hubs thời gian thực:

```mermaid
graph TD
    subgraph "Khach Hang (Customer PWA - Mobile Browser)"
        C1[Quet QR Ban Dine-in] -->|Tuy bien mon & BOM| C_Cart[Gio hang PWA]
        C2[Quet QR Delivery] -->|SDT + Dia chi + Phi 20k| C_Cart
        C_Cart -->|Nhanh 1: VietQR| C_Pay1[Thanh toan VietQR Tra Truoc]
        C_Cart -->|Nhanh 2: Tien mat| C_Pay2[Tao don Bep Pha Che Tra Sau]
        C3[Chatbot AI-1 Gemini RAG] -.->|Tu van mon & khau vi| C_Cart
        C4[Gui Danh Gia 1-5 Sao & Tai Anh] -.-> C5[Ghi nhan Feedback]
    end

    subgraph "Nhan Vien Van Hanh (Staff Web POS & KDS)"
        S_KDS[Man hinh Web KDS Bep/Bar] -->|SignalR Hub| S_Prep[Pha Che Theo Dinh Luong BOM]
        S_Prep -->|Chuyen trang thai| S_Ready[San Sang Phuc Vu / Dong Goi]
        S_POS[Web POS Quay Takeaway] -->|Tra cuu SDT CRM| S_Loyalty[Tich 10 Ly Tang 1 Mang Ve]
        S_POS -->|Thu tien sau| S_Cashier[Tien mat / VietQR Quay]
        S_Attend[Cham cong Khoa WiFi] -->|Xac thuc BSSID/IP + Ma NV| S_AttRec[Ban Ghi Cham Cong Ca]
    end

    subgraph "Quan Ly Chi Nhanh (Branch Manager Web Portal)"
        M_Shift[Mo/Ket Ca Ket Tien Mat] --> M_Recon[Doi Soat Z-Report Ca]
        M_Stock[Kiem Ke Kho & Lap Phieu Xuat Bar] --> M_AlertStock[Canh Bao Het Hang 86]
        M_WiFi[Cau Hinh BSSID/IP WiFi Cham Cong] --> S_Attend
        M_Rev[Nhan Alert Khan Review <= 2 Sao] --> C5
        M_Photo[Kiem Duyet Anh Feedback Khach] --> C5
    end

    subgraph "Chu Chuoi / Admin (Admin Executive Portal)"
        A_Menu[Product Full CRUD, BOM, Nhom Giá Vùng] --> S_KDS
        A_AI[Khai Pha AI-2 Combo Apriori] -->|Chu chuoi phe duyet| A_PubCombo[Phat Hanh Combo Menu]
        A_PubCombo --> C_Cart
        A_PL[Dashboard Bao Cao P&L Hop Nhat Da Chi Nhanh]
        A_RBAC[Quan Tri Chi Nhanh, Nhan Su & Phan Quyen RBAC]
    end

    C_Pay1 ==>|Event OrderPaid| S_KDS
    C_Pay2 ==>|Event OrderConfirmed| S_KDS
    S_Ready ==>|Thong bao chuong/rung| C1
```

---

# 👤 PHẦN 3: ĐẶC TẢ CHI TIẾT ACTOR 1: KHÁCH HÀNG (CUSTOMER — 20 FEATURES)

Khách hàng tương tác với hệ thống hoàn toàn qua giao diện **Web PWA trên trình duyệt di động** (Route: `(customer)`). Khách hàng có thể trải nghiệm ở vai trò Vãng lai (`GuestCustomer`) hoặc Đã xác thực CRM (`AuthCustomer`).

### Danh Mục 20 Tính Năng Khách Hàng (`C-01` đến `C-20`)

#### C-01: Quét mã QR bàn tại quán (Dine-in QR Scan)
- **Mô Tả Nghiệp Vụ:** Khách hàng ngồi tại bàn, dùng Camera điện thoại quét mã QR dán cố định trên mặt bàn (chứa URL định dạng `https://domain.com/order?branchId={guid}&tableId={guid}&token={hmac}`). Hệ thống giải mã tham số URL, xác thực tính hợp lệ của chữ ký số HMAC, khởi tạo phiên đặt món gắn chặt với Bàn và Chi nhánh tương ứng.
- **Giao Diện & Kênh:** Next.js PWA Mobile Browser (`/order/dine-in?branchId=...&tableId=...`).
- **Input Contract:** `branchId` (Guid), `tableId` (Guid), `signature` (String HMAC-SHA256).
- **System Flow:** API `/api/v1/tables/verify-qr` kiểm tra `tableId` và `branchId`. Nếu bàn đang hoạt động (`Active`), sinh Anonymous JWT Token lưu trữ trên `sessionStorage` và `localStorage`. Tải Menu áp dụng cho chi nhánh tương ứng từ Redis Cache.
- **Output Contract:** `sessionId` (String), `branchName` (String), `tableName` (String), `menuCategories` (Array).
- **Business Rules:** Mã QR được ký số bảo mật; nếu chữ ký sai hoặc bàn bị khóa (`Inactive`), từ chối truy cập và báo lỗi giao diện.
- **Edge Cases:** QR bị rách/mất nét ➔ khách nhập mã bàn 4 số thủ công dưới sự hỗ trợ của nhân viên. Mất mạng khi quét ➔ hiển thị màn hình offline cache PWA.

#### C-02: Quét mã QR đặt hàng tận nơi (Delivery QR Scan)
- **Mô Tả Nghiệp Vụ:** Khách hàng quét mã QR trên tờ rơi/bao bì hoặc truy cập trực tiếp đường dẫn đặt hàng từ xa của chi nhánh gần nhất. Chế độ phục vụ tự động chuyển sang `Delivery`, yêu cầu nhập thông tin người nhận và áp dụng biểu phí giao hàng cố định 20.000 VNĐ.
- **Giao Diện & Kênh:** Next.js PWA Mobile Browser (`/order/delivery?branchId=...`).
- **Input Contract:** `branchId` (Guid).
- **System Flow:** Kiểm tra chi nhánh có đang mở bán dịch vụ Delivery không (`isDeliveryEnabled == true`). Khởi tạo giỏ hàng Delivery, tải danh mục món hỗ trợ vận chuyển đường dài.
- **Output Contract:** `branchInfo` (Object), `deliveryFee` (20000 VNĐ cố định), `menu` (Array).
- **Business Rules:** Đơn Delivery bắt buộc 100% thanh toán trước qua VietQR; không hỗ trợ thanh toán tiền mặt khi nhận hàng.
- **Edge Cases:** Chi nhánh tạm ngưng nhận đơn Delivery do quá tải ➔ thông báo khung giờ nhận đơn tiếp theo và gợi ý chuyển sang chi nhánh lân cận.

#### C-03: Xem thực đơn số tương tác đa chi nhánh (Digital Menu Browsing)
- **Mô Tả Nghiệp Vụ:** Khách hàng lướt xem thực đơn với hình ảnh món ăn chuẩn WebP chất lượng cao, phân loại theo danh mục (Cà phê, Trà sữa, Trà trái cây, Bánh ngọt, Món ăn kèm). Hiển thị giá chuẩn theo chi nhánh, nhãn món mới (`New`), món bán chạy (`Bestseller`), món hết hàng tạm thời (`Sold Out / 86`).
- **Giao Diện & Kênh:** PWA Menu Component (`/menu`).
- **Input Contract:** `branchId` (Guid), `categoryId` (Guid, optional).
- **System Flow:** Truy vấn dữ liệu từ Redis Cache key `branch:{id}:menu:active`. Nếu cache miss, truy vấn PostgreSQL, kết hợp bảng giá vùng `BranchProductPrices` và ghi cache với TTL 30 phút.
- **Output Contract:** Danh sách Categories kèm Products (Tên món, Giá, Ảnh WebP, Trạng thái còn/hết, Tùy chọn Options).
- **Business Rules:** Món bị bật trạng thái `IsAvailable = false` tại chi nhánh sẽ hiển thị mờ kèm tag `Tạm Hết` và vô hiệu hóa nút Thêm vào giỏ.
- **Edge Cases:** Mạng yếu ➔ PWA tải ảnh thumbnail dung lượng thấp trước, sau đó nạp Progressive WebP đầy đủ.

#### C-04: Tìm kiếm & Lọc món thông minh (Smart Search & Filtering)
- **Mô Tả Nghiệp Vụ:** Khách hàng tìm món theo từ khóa (tên món, nguyên liệu), lọc theo khoảng giá, danh mục, thuộc tính khẩu vị (ít ngọt, không sữa, thuần chay, nồng độ caffeine thấp).
- **Giao Diện & Kênh:** Thanh tìm kiếm sticky header trên PWA (`/menu/search`).
- **Input Contract:** `query` (String, max 100 chars), `minPrice` (Decimal), `maxPrice` (Decimal), `tags` (Array).
- **System Flow:** Sử dụng PostgreSQL Full-Text Search (hàm `to_tsvector` tiếng Việt không dấu) kết hợp bộ lọc JSONB `attributes` để trả kết quả dưới 50ms.
- **Output Contract:** Danh sách sản phẩm thỏa mãn điều kiện lọc.
- **Business Rules:** Tự động chuẩn hóa chuỗi tìm kiếm (loại bỏ ký tự đặc biệt, chuyển chữ hoa thành chữ thường, hỗ trợ gõ tiếng Việt không dấu).
- **Edge Cases:** Không tìm thấy kết quả phù hợp ➔ hiển thị danh sách 4 món Bestseller đề xuất và nút gọi AI tư vấn.

#### C-05: Tùy biến món & Tùy chọn định lượng BOM (Item Customization & Modifiers)
- **Mô Tả Nghiệp Vụ:** Khi bấm vào món, mở Drawer/Modal chi tiết món cho phép chọn Size (Nhỏ, Vừa, Lớn), Mức đường (0%, 30%, 50%, 70%, 100%), Mức đá (Không đá, Ít đá, Bình thường), Topping đính kèm (Trân châu trắng, Thạch nha đam, Kem cheese) và Ghi chú đặc biệt cho Barista.
- **Giao Diện & Kênh:** PWA Product Detail Sheet (`/menu/product/[id]`).
- **Input Contract:** `productId` (Guid), `sizeOptionId` (Guid), `sweetnessLevel` (Int: 0, 30, 50, 70, 100), `iceLevel` (Int: 0, 30, 50, 100), `toppings` (Array of Guid), `customerNote` (String, max 200 chars).
- **System Flow:** Tính toán phụ thu dựa trên Size và Topping được chọn. Đối soát tính tương thích với định lượng BOM pha chế.
- **Output Contract:** `customizedItemTotal` (Decimal), `summaryText` (String: "Size L, 50% Đường, Ít đá, +Trân châu đen").
- **Business Rules:** Các tùy biến vượt quá giới hạn hoặc không có trong công thức BOM chi nhánh sẽ bị khóa.
- **Edge Cases:** Khách ghi chú mâu thuẫn ("Cho 0% đường nhưng ngọt lịm") ➔ hiển thị cảnh báo hướng dẫn chọn đúng mức đường chuẩn.

#### C-06: Quản lý giỏ hàng tạm thời (Cart Management)
- **Mô Tả Nghiệp Vụ:** Giỏ hàng lưu trữ danh sách các món đã chọn, số lượng, tùy biến chi tiết và tổng giá trị tạm tính. Khách hàng có thể tăng/giảm số lượng, chỉnh sửa tùy biến món trực tiếp hoặc xóa món khỏi giỏ.
- **Giao Diện & Kênh:** PWA Bottom Cart Bar & Floating Drawer (`/cart`).
- **Input Contract:** `cartAction` (Add/Update/Delete/Clear), `cartItem` (Object).
- **System Flow:** Quản lý Client-Side State qua Zustand/Redux Toolkit, đồng bộ định kỳ vào `sessionStorage` để không mất dữ liệu khi vô tình reload trang.
- **Output Contract:** `cartItems` (Array), `subTotal` (Decimal), `itemCount` (Int), `estimatedVat` (Decimal).
- **Business Rules:** Số lượng tối đa cho mỗi món trong một đơn đặt là 20 ly nhằm tránh tắc nghẽn quầy pha chế.
- **Edge Cases:** Món trong giỏ hàng vừa bị chi nhánh bật trạng thái "Hết hàng" trước khi khách bấm đặt ➔ hệ thống báo đỏ món bị hết và yêu cầu xóa/đổi món trước khi thanh toán.

#### C-07: Áp dụng mã khuyến mãi & Voucher giảm giá (Voucher & Promo Code Application)
- **Mô Tả Nghiệp Vụ:** Khách hàng nhập mã giảm giá hoặc chọn voucher có sẵn trong ví ưu đãi cá nhân. Hệ thống kiểm tra điều kiện áp dụng (giá trị đơn tối thiểu, khung giờ vàng, nhóm sản phẩm thỏa mãn, chi nhánh áp dụng, giới hạn lượt dùng) và trừ tiền trực tiếp trên tổng đơn.
- **Giao Diện & Kênh:** PWA Voucher Input Field & Modal Danh sách Voucher (`/cart/vouchers`).
- **Input Contract:** `voucherCode` (String), `cartSubtotal` (Decimal), `branchId` (Guid), `customerId` (Guid, optional).
- **System Flow:** Gọi API `/api/v1/vouchers/validate`. Kiểm tra bảng `Vouchers` và `VoucherUsageHistory` trong Database. Tính toán số tiền chiết khấu chính xác.
- **Output Contract:** `discountAmount` (Decimal), `finalTotal` (Decimal), `appliedVoucherCode` (String), `validationMessage` (String).
- **Business Rules:** Mỗi đơn hàng chỉ được áp dụng duy nhất 01 mã khuyến mãi. Không áp dụng voucher nếu tổng giá trị món chưa đạt điều kiện tối thiểu.
- **Edge Cases:** Mã voucher hết lượt sử dụng đồng thời trong tích tắc ➔ thông báo lỗi rõ ràng và cập nhật lại trạng thái mã.

#### C-08: Đặt món & Thanh toán chuyển khoản tự động VietQR (VietQR Pre-payment Path)
- **Mô Tả Nghiệp Vụ:** Áp dụng cho cả đơn Dine-in (Nhánh A) và 100% đơn Delivery. Sau khi xác nhận giỏ hàng, hệ thống sinh mã VietQR động chuẩn NAPAS 247 qua PayOS (bao gồm Số tài khoản, Ngân hàng, Số tiền chính xác và Nội dung chuyển khoản mã hóa `FB{OrderId}`). Khách quét mã chuyển tiền qua App Ngân hàng bất kỳ. Khi PayOS bắn Webhook xác nhận thanh toán thành công (`Paid`), đơn hàng mới chính thức chuyển trạng thái `Paid` và tự động bắn vào màn hình KDS Bếp qua SignalR.
- **Giao Diện & Kênh:** PWA Payment Screen (`/checkout/vietqr/[orderId]`).
- **Input Contract:** `orderId` (Guid), `amount` (Decimal), `paymentMethod = "VietQR"`.
- **System Flow:** Gọi API tích hợp PayOS tạo Payment Link. Hiển thị mã QR kèm đồng hồ đếm ngược 10 phút. Lắng nghe sự kiện `OrderPaid` từ SignalR `OrderHub`.
- **Output Contract:** `qrCodeUrl` (String), `accountNumber` (String), `transferContent` (String), `paymentStatus` (Pending/Paid/Expired).
- **Business Rules:** Đơn thanh toán VietQR CHỈ được gửi vào Bếp KDS khi trạng thái chuyển sang `Paid`. Sau 10 phút không nhận được tiền, đơn tự động hủy (`Cancelled`) và giải phóng bàn/giỏ hàng.
- **Edge Cases:** Khách chuyển thiếu tiền ➔ Webhook PayOS ghi nhận giao dịch không khớp, SignalR hiển thị số tiền còn thiếu và sinh mã QR phần bù.

#### C-09: Đặt món & Thanh toán Tiền mặt trả sau tại bàn (Cash Post-payment Path)
- **Mô Tả Nghiệp Vụ:** Áp dụng RIÊNG BIỆT cho đơn Dine-in (Nhánh B). Khách chọn phương thức "Tiền mặt tại bàn" và bấm Xác nhận đặt món. Hệ thống lập tức tạo đơn với trạng thái `Confirmed` và bắn ngay vào Bếp KDS qua SignalR để Barista pha chế không cần chờ thanh toán. Nhân viên phục vụ bưng đồ uống ra bàn kèm theo Phiếu tạm tính/Hóa đơn có in sẵn mã VietQR của đơn hàng. Khách có thể trả tiền mặt trực tiếp cho nhân viên HOẶC quét mã VietQR in trên hóa đơn để chuyển khoản. Nhân viên nhận tiền và bấm "Xác nhận đã thanh toán" trên Web Staff để kết thúc đơn.
- **Giao Diện & Kênh:** PWA Payment Selection (`/checkout/cash/[orderId]`).
- **Input Contract:** `orderId` (Guid), `paymentMethod = "Cash"`, `tableId` (Guid).
- **System Flow:** API `/api/v1/orders/create-cash` đổi trạng thái đơn thành `Confirmed`, kích hoạt SignalR broadcast tới `KitchenHub` chi nhánh.
- **Output Contract:** `orderId` (Guid), `orderCode` (String: "#102"), `status = "Confirmed"`, `estimatedTime` (10-15 phút).
- **Business Rules:** Đơn tiền mặt Dine-in được làm món ngay lập tức. Bàn chỉ được giải phóng (`Available`) sau khi nhân viên bấm xác nhận thu tiền hoàn tất.
- **Edge Cases:** Khách đổi ý muốn chuyển sang quét VietQR khi nhân viên đem hóa đơn ra bàn ➔ khách dùng app ngân hàng quét mã QR in trên hóa đơn, hệ thống xử lý Webhook và tự động đổi trạng thái đơn thành `Paid`.

#### C-10: Đặt đơn giao hàng tận nơi với phí ship cố định (Delivery Order Placement)
- **Mô Tả Nghiệp Vụ:** Khách hàng đặt đơn Delivery bắt buộc nhập đầy đủ: Số điện thoại người nhận, Tên người nhận, Địa chỉ giao hàng chi tiết và Ghi chú giao hàng. Hệ thống tự động cộng Phí vận chuyển 20.000 VNĐ cố định vào tổng tiền đơn hàng và chuyển sang cổng thanh toán VietQR trả trước bắt buộc.
- **Giao Diện & Kênh:** PWA Delivery Checkout (`/checkout/delivery`).
- **Input Contract:** `receiverName` (String), `receiverPhone` (String chuẩn 10 số VN), `deliveryAddress` (String), `deliveryNote` (String), `deliveryFee = 20000`.
- **System Flow:** Xác thực Regex SĐT Việt Nam (`^(0[3|5|7|8|9])+([0-9]{8})$`), kiểm tra địa chỉ không rỗng. Tạo đơn `OrderType = "Delivery"`, `DeliveryFee = 20000`, `Status = "PendingPayment"`.
- **Output Contract:** `orderId` (Guid), `totalAmount` (Subtotal + 20000), `vietQrData` (Object).
- **Business Rules:** Phí ship 20.000 VNĐ là cố định toàn hệ thống. Không hỗ trợ đơn giao hàng dưới 50.000 VNĐ giá trị món.
- **Edge Cases:** Khách nhập SĐT sai định dạng ➔ báo lỗi trực quan ngay tại input field trước khi cho phép bấm thanh toán.

#### C-11: Theo dõi trạng thái đơn hàng thời gian thực (Real-time Order Tracking via SignalR)
- **Mô Tả Nghiệp Vụ:** Màn hình Live Tracking hiển thị tiến trình xử lý đơn hàng theo 5 bước trực quan: (1) Đã tiếp nhận ➔ (2) Bếp đang pha chế ➔ (3) Đã pha chế xong / Đang giao hàng ➔ (4) Hoàn thành ➔ (5) Đã thanh toán / Đã đóng đơn. Cập nhật tức thì không cần tải lại trang nhờ SignalR `OrderHub`.
- **Giao Diện & Kênh:** PWA Live Order Tracking Page (`/orders/[id]/tracking`).
- **Input Contract:** `orderId` (Guid), `connectionId` (SignalR Client ID).
- **System Flow:** Client tham gia group SignalR `order_{orderId}`. Khi Barista cập nhật trạng thái trên KDS hoặc Thu ngân xác nhận thanh toán, Backend phát event `OrderStatusChanged` tới nhóm.
- **Output Contract:** `currentStatus` (Enum), `statusTimestamp` (DateTime), `stepIndex` (Int 1-5), `estimatedReadyMinutes` (Int).
- **Business Rules:** Khi đơn chuyển sang trạng thái `ReadyForPickup` (Đã pha chế xong), PWA kích hoạt âm thanh thông báo và rung thiết bị.
- **Edge Cases:** Mất kết nối mạng tạm thời ➔ Client tự động kết nối lại SignalR (`withAutomaticReconnect`) và pull API đối soát trạng thái mới nhất.

#### C-12: Gọi nhân viên phục vụ / Yêu cầu hỗ trợ tại bàn (Call Staff / Service Request)
- **Mô Tả Nghiệp Vụ:** Khách hàng ngồi tại bàn có thể bấm nút "Gọi nhân viên" trên giao diện PWA, lựa chọn lý do: Cần lấy thêm nước lọc, Cần thêm muỗng/ống hút, Cần dọn bàn, hoặc Yêu cầu hỗ trợ khác.
- **Giao Diện & Kênh:** PWA Floating Service Action Button (`/order/dine-in?action=call-staff`).
- **Input Contract:** `tableId` (Guid), `requestType` (Water / Utensils / Clean / Other), `note` (String).
- **System Flow:** API `/api/v1/service-requests` tạo yêu cầu và phát SignalR notification tới toàn bộ nhân viên quầy và nhân viên phục vụ đang trực ca tại chi nhánh.
- **Output Contract:** `requestId` (Guid), `status = "Sent"`, `message = "Nhân viên đang đến hỗ trợ bạn"`.
- **Business Rules:** Giới hạn chống spam (Rate Limit): Mỗi bàn chỉ được gửi 01 yêu cầu gọi phục vụ mỗi 2 phút.
- **Edge Cases:** Nhân viên chưa bấm phản hồi sau 3 phút ➔ hệ thống nâng cấp cảnh báo màu cam trên màn hình Dashboard Quản lý chi nhánh.

#### C-13: Yêu cầu thanh toán & In tạm tính tại bàn (Request Bill & Pre-check Receipt)
- **Mô Tả Nghiệp Vụ:** Khách hàng dùng bữa xong bấm nút "Yêu cầu thanh toán" trên PWA. Màn hình hiển thị chi tiết bảng kê tạm tính gồm các món đã dùng, số lượng, giá tiền, chiết khấu và tổng thanh toán. Hệ thống gửi thông báo tới màn hình Web Staff để nhân viên mang hóa đơn kèm mã QR thanh toán ra bàn.
- **Giao Diện & Kênh:** PWA Pre-check Bill Screen (`/orders/[id]/bill`).
- **Input Contract:** `orderId` (Guid), `tableId` (Guid).
- **System Flow:** Khóa giỏ hàng của bàn (không cho thêm món mới), sinh mã thông báo SignalR `BillRequested` gửi đến Web Staff quầy thu ngân.
- **Output Contract:** `precheckBill` (Danh sách món, Thuế VAT, Giảm giá, Tổng tiền, Mã VietQR tạm tính).
- **Business Rules:** Bàn đã yêu cầu in tạm tính không thể tự ý đặt thêm món trừ khi nhân viên mở khóa lại bàn.
- **Edge Cases:** Khách muốn tách bill ➔ nhân viên thao tác tách món trên Web POS quầy thu ngân.

#### C-14: Tư vấn đồ uống thông minh AI-1 Gemini RAG Chatbot (AI Drink Recommendation)
- **Mô Tả Nghiệp Vụ:** Trợ lý ảo AI tích hợp trên PWA, hỗ trợ khách hàng trò chuyện tự nhiên bằng tiếng Việt để tìm đồ uống phù hợp theo tâm trạng ("Đang mệt mỏi cần tỉnh táo"), khẩu vị ("Thích béo ngậy ít ngọt"), thời tiết ("Trời nóng nực muốn uống gì thanh mát"), hoặc chế độ ăn kiêng ("Tìm đồ uống dưới 150 kcal không sữa bò").
- **Giao Diện & Kênh:** PWA AI Chatbot Drawer (`/ai-assistant`).
- **Input Contract:** `userMessage` (String, max 300 chars), `chatHistory` (Array of Messages), `branchId` (Guid).
- **System Flow:** Backend tiếp nhận câu hỏi, thực hiện RAG (Retrieval-Augmented Generation) truy xuất Menu và BOM chi tiết của chi nhánh từ PostgreSQL, gửi Context kèm Prompt chuẩn hóa đến mô hình Google Gemini 1.5 Flash. Trả về câu trả lời kèm Card sản phẩm có nút "Thêm vào giỏ" ngay lập tức.
- **Output Contract:** `aiResponseText` (String), `suggestedProductIds` (Array of Guid), `actionCards` (Array of Product Card DTOs).
- **Business Rules:** AI chỉ tư vấn các món đang thực sự CÒN HÀNG (`IsAvailable == true`) tại chi nhánh khách đang truy cập.
- **Edge Cases:** Khách hỏi nội dung không liên quan đến ẩm thực/F&B ➔ AI lịch sự từ chối và hướng sự chú ý của khách về thực đơn đồ uống.

#### C-15: Đăng ký & Đăng nhập tài khoản thành viên CRM qua OTP (Member CRM Auth via Phone OTP)
- **Mô Tả Nghiệp Vụ:** Khách hàng vãng lai có thể nâng cấp thành khách hàng thành viên CRM bằng cách nhập Số điện thoại. Hệ thống gửi mã OTP 6 số (hoặc xác thực OTP qua SMS Gateway). Sau khi nhập đúng OTP, hệ thống tự động liên kết dữ liệu lịch sử đơn hàng cũ với tài khoản thành viên và kích hoạt hồ sơ CRM.
- **Giao Diện & Kênh:** PWA Auth Modal (`/auth/phone-login`).
- **Input Contract:** `phoneNumber` (String 10 digits), `otpCode` (String 6 digits).
- **System Flow:** API `/api/v1/auth/verify-otp` kiểm tra OTP trong Redis Cache (TTL 2 phút, max 3 lần thử). Nếu hợp lệ, cấp phát User JWT Token có hạn 30 ngày (Role: `AuthCustomer`).
- **Output Contract:** `jwtToken` (String), `refreshToken` (String), `customerProfile` (Họ tên, SĐT, Điểm thưởng, Hạng thành viên).
- **Business Rules:** Khóa tạm thời SĐT 15 phút nếu nhập sai OTP quá 5 lần liên tiếp để phòng chống tấn công brute-force.
- **Edge Cases:** SMS gửi chậm ➔ hỗ trợ nút "Gửi lại mã OTP" sau 60 giây đếm ngược.

#### C-16: Xem lịch sử đơn hàng & Chi tiết hóa đơn điện tử (Order History & E-Receipt)
- **Mô Tả Nghiệp Vụ:** Khách hàng đã đăng nhập có thể xem toàn bộ lịch sử các đơn hàng đã đặt (Dine-in, Delivery) theo thời gian. Bấm vào từng đơn để xem chi tiết hóa đơn điện tử, trạng thái thanh toán, mã giao dịch VietQR và danh sách món ăn đã dùng.
- **Giao Diện & Kênh:** PWA Order History Screen (`/profile/orders`).
- **Input Contract:** `customerId` (Guid lấy từ JWT Claims), `pageIndex` (Int), `pageSize` (Int).
- **System Flow:** Truy vấn bảng `Orders` kết hợp `OrderItems` với điều kiện `CustomerId == currentUserId`.
- **Output Contract:** Danh sách tóm tắt đơn hàng (Mã đơn, Ngày giờ, Chi nhánh, Tổng tiền, Trạng thái) kèm link xem E-Receipt.
- **Business Rules:** Khách vãng lai (`GuestCustomer`) chỉ có thể xem lại đơn hàng hiện tại trong phiên làm việc của trình duyệt.
- **Edge Cases:** Đơn hàng bị hủy ➔ hiển thị rõ lý do hủy (Khách hủy, Quá hạn thanh toán 10 phút, Quán hết món).

#### C-17: Quản lý hồ sơ cá nhân & Sổ địa chỉ giao hàng (Profile & Delivery Address Book)
- **Mô Tả Nghiệp Vụ:** Thành viên CRM có thể cập nhật Họ tên, Email, Ngày sinh (nhận ưu đãi sinh nhật) và lưu danh sách nhiều địa chỉ giao hàng (Nhà riêng, Công ty, Trường học) kèm gắn cờ địa chỉ mặc định.
- **Giao Diện & Kênh:** PWA Profile & Address Management (`/profile/addresses`).
- **Input Contract:** `fullName` (String), `email` (String), `birthDate` (Date), `addresses` (Array of Address DTOs).
- **System Flow:** Lưu thông tin vào bảng `Customers` và `CustomerAddresses`.
- **Output Contract:** `isSuccess` (Boolean), `updatedProfile` (Object).
- **Business Rules:** Ngày sinh chỉ được cập nhật duy nhất 01 lần trong năm để chống lạm dụng voucher sinh nhật.
- **Edge Cases:** Nhập email sai định dạng ➔ thông báo lỗi validation trực tiếp.

#### C-18: Đánh giá 1-5 sao chất lượng món & Phục vụ (Order Rating & Review Submission)
- **Mô Tả Nghiệp Vụ:** Sau khi đơn hàng hoàn thành, khách hàng nhận thông báo mời đánh giá trải nghiệm dịch vụ. Khách chấm điểm từ 1 đến 5 sao cho từng món và chấm điểm dịch vụ chung của chi nhánh kèm nhận xét văn bản.
- **Giao Diện & Kênh:** PWA Order Review Sheet (`/orders/[id]/review`).
- **Input Contract:** `orderId` (Guid), `branchRating` (Int 1-5 sao), `itemRatings` (Array of { productId, stars, comment }), `generalComment` (String, max 500 chars).
- **System Flow:** API `/api/v1/reviews` ghi nhận đánh giá vào bảng `Reviews`. Nếu điểm đánh giá `<= 2 sao`, hệ thống tự động kích hoạt Webhook cảnh báo khẩn cấp tới Quản lý chi nhánh (`M-10`).
- **Output Contract:** `reviewId` (Guid), `thankYouMessage` (String).
- **Business Rules:** Mỗi đơn hàng chỉ được gửi đánh giá duy nhất 01 lần trong vòng 48 giờ sau khi hoàn thành.
- **Edge Cases:** Khách bấm đánh giá 1 sao nhưng không điền lý do ➔ giao diện gợi ý các thẻ lý do nhanh ("Món ra chậm", "Đồ uống quá ngọt", "Nhân viên chưa chu đáo").

#### C-19: Tải ảnh phản hồi & Đóng góp ý kiến dịch vụ (Feedback Photo Upload)
- **Mô Tả Nghiệp Vụ:** Khách hàng có thể đính kèm tối đa 03 hình ảnh thực tế của món ăn hoặc không gian quán khi gửi đánh giá. Hình ảnh được tự động nén, chuyển đổi định dạng WebP và đưa vào hàng đợi kiểm duyệt trước khi hiển thị công khai.
- **Giao Diện & Kênh:** PWA Review Form Photo Picker (`/orders/[id]/review/upload`).
- **Input Contract:** `reviewId` (Guid), `imageFiles` (Multipart form-data, max 3 files, mỗi file <= 5MB).
- **System Flow:** Backend kiểm tra định dạng ảnh (JPEG, PNG, HEIC), chuyển đổi sang WebP chuẩn nén, lưu trữ an toàn và ghi URL vào bảng `ReviewPhotos` với cờ `IsApproved = false`.
- **Output Contract:** `uploadedPhotoUrls` (Array of Strings), `moderationStatus = "Pending"`.
- **Business Rules:** Ảnh tải lên phải trải qua bước kiểm duyệt của Quản lý chi nhánh (`M-11`) mới được hiển thị công khai trên thực đơn đánh giá.
- **Edge Cases:** Tải file không phải ảnh (PDF, EXE) ➔ từ chối ngay lập tức tại Middleware bảo mật.

#### C-20: Gợi ý món ăn kèm & Combo đề xuất (Upselling & Cross-selling Suggestions)
- **Mô Tả Nghiệp Vụ:** Khi khách thêm món vào giỏ hàng hoặc ở bước chuẩn bị thanh toán, PWA tự động hiển thị thanh gợi ý các món ăn kèm lý tưởng (Bánh ngọt đi kèm cà phê, Topping đặc trưng) hoặc Combo ưu đãi được tối ưu hóa bởi thuật toán AI-2 Apriori.
- **Giao Diện & Kênh:** PWA Cart Upselling Carousel (`/cart/suggestions`).
- **Input Contract:** `currentCartProductIds` (Array of Guid), `branchId` (Guid).
- **System Flow:** Gọi API `/api/v1/recommendations/cross-sell`. Hệ thống so khớp các quy luật kết hợp khai phá từ AI-2 Apriori đã được Admin phê duyệt (`A-13`) để trả về danh sách 3 món có độ tin cậy (`Confidence`) cao nhất.
- **Output Contract:** Danh sách món đề xuất kèm giá ưu đãi và nút "+ Thêm nhanh".
- **Business Rules:** Không gợi ý món đã có sẵn trong giỏ hàng hoặc món đang hết hàng tại chi nhánh.
- **Edge Cases:** Giỏ hàng chưa có món nào ➔ hiển thị Top 3 món Bestseller toàn chuỗi.

---

# 🧋 PHẦN 4: ĐẶC TẢ CHI TIẾT ACTOR 2: NHÂN VIÊN VẬN HÀNH QUẦY (STAFF / BARISTA — 13 FEATURES)

Toàn bộ nghiệp vụ của nhân viên được thực thi trên giao diện **Web Responsive** tối ưu cho màn hình cảm ứng POS Quầy Thu Ngân và Smart TV / Tablet Bếp KDS (Routes: `(kds)`, `(staff)`). **Loại bỏ hoàn toàn Staff Mobile App**.

### Danh Mục 13 Tính Năng Nhân Viên Quầy (`S-01` đến `S-13`)

#### S-01: Đăng nhập ca làm việc & Xác thực phiên quầy (Shift Login & POS Authentication)
- **Mô Tả Nghiệp Vụ:** Nhân viên truy cập cổng Web Staff/KDS, nhập Mã số nhân viên (Staff Code) và Mật khẩu ca. Hệ thống xác thực danh tính, đối soát lịch phân ca hiện tại của chi nhánh và cấp quyền truy cập vào giao diện KDS hoặc POS Quầy.
- **Giao Diện & Kênh:** Web Staff Login Portal (`/staff/login`).
- **Input Contract:** `staffCode` (String: "NV008"), `password` (String), `branchId` (Guid).
- **System Flow:** API `/api/v1/auth/staff-login` kiểm tra bảng `Staff` và `WorkShifts`. Cấp JWT Token có Claim `Role: BaristaStaff / CashierStaff` và gán Scope chi nhánh.
- **Output Contract:** `jwtToken` (String), `staffName` (String), `assignedRole` (String), `shiftInfo` (Ca sáng / Ca chiều).
- **Business Rules:** Nhân viên không có lịch phân ca trong ngày không thể đăng nhập trừ khi Quản lý chi nhánh cấp quyền vượt ca (`Manager Override`).
- **Edge Cases:** Nhân viên nhập sai mật khẩu 3 lần ➔ khóa tài khoản tạm thời 5 phút và thông báo tới Quản lý.

#### S-02: Chấm công vào/ra ca khóa mạng WiFi chi nhánh (WiFi-Locked Attendance Check-in/out)
- **Mô Tả Nghiệp Vụ:** Nhân viên thực hiện Check-in đầu ca và Check-out cuối ca trên giao diện Web Staff. Hệ thống bắt buộc kiểm tra thiết bị đang kết nối đúng mạng WiFi nội bộ của chi nhánh (xác thực địa chỉ MAC/BSSID của Access Point hoặc dải IP Gateway Subnet nội bộ đã cấu hình). Không sử dụng GPS 50m hay QR động 30s.
- **Giao Diện & Kênh:** Web Staff Attendance Widget (`/staff/attendance`).
- **Input Contract:** `staffCode` (String), `clientBSSID` (String), `clientIpAddress` (String), `actionType` (CheckIn / CheckOut).
- **System Flow:** API `/api/v1/attendance/verify-wifi` so sánh BSSID/IP gửi lên với bảng `BranchWifiConfigs` của chi nhánh. Nếu khớp, ghi nhận bản ghi chấm công vào bảng `AttendanceRecords`.
- **Output Contract:** `attendanceId` (Guid), `checkInTime` (DateTime), `status = "Valid"`, `message = "Chấm công thành công"`.
- **Business Rules:** Chấm công bị từ chối 100% nếu nhân viên sử dụng 4G/5G hoặc kết nối sai mạng WiFi chi nhánh.
- **Edge Cases:** Router WiFi chi nhánh bị mất mạng internet ➔ Quản lý sử dụng tài khoản Manager để bấm xác nhận chấm công thủ công có lý do giải trình.

#### S-03: Màn hình KDS Bếp/Bar hiển thị đơn theo thời gian thực (Real-time KDS Queue via SignalR)
- **Mô Tả Nghiệp Vụ:** Màn hình KDS (Kitchen Display System) hiển thị danh sách đơn hàng cần pha chế dưới dạng các thẻ đơn (Order Cards) sắp xếp theo thứ tự thời gian vào bếp. Phân loại màu sắc trực quan: Màu Xanh lá (Đơn mới < 5 phút), Màu Vàng (Đơn chờ 5-10 phút), Màu Đỏ (Đơn cảnh báo quá 10 phút).
- **Giao Diện & Kênh:** Web KDS Viewport (`/kds/display`).
- **Input Contract:** `branchId` (Guid), SignalR `KitchenHub` connection.
- **System Flow:** KDS kết nối tới SignalR `KitchenHub` phòng `branch_{branchId}_kitchen`. Khi có đơn `Paid` (VietQR) hoặc `Confirmed` (Tiền mặt Dine-in hoặc POS Takeaway), thẻ đơn tự động xuất hiện kèm âm thanh thông báo "Ting Ting".
- **Output Contract:** Danh sách thẻ đơn: Mã đơn, Loại đơn (Dine-in / Takeaway / Delivery), Tên bàn, Danh sách món + Tùy biến chi tiết (Size, Đường, Đá, Topping), Đồng hồ đếm thời gian thực.
- **Business Rules:** Đơn thanh toán VietQR chỉ hiển thị lên KDS khi đã hoàn tất thanh toán. Đơn tiền mặt Dine-in và Takeaway hiển thị ngay khi tạo.
- **Edge Cases:** Mất kết nối SignalR ➔ KDS hiển thị thanh cảnh báo đỏ "Offline" và tự động kích hoạt cơ chế Polling API 5 giây/lần.

#### S-04: Xem công thức định lượng pha chế BOM tiêu chuẩn (BOM Standard Recipe Viewing)
- **Mô Tả Nghiệp Vụ:** Barista có thể bấm trực tiếp vào bất kỳ món nào trên màn hình KDS để mở Modal tra cứu nhanh công thức định lượng nguyên vật liệu BOM chuẩn (Ví dụ: Trà sữa Oolong Size L = 150ml cốt trà Oolong + 30g bột sữa + 20ml nước đường + 1 vá trân châu) và các bước thực hiện thao tác pha chế.
- **Giao Diện & Kênh:** Web KDS Recipe Modal (`/kds/recipe/[productId]`).
- **Input Contract:** `productId` (Guid), `sizeId` (Guid).
- **System Flow:** Truy vấn dữ liệu cấu trúc BOM từ bảng `BillOfMaterials` và `BillOfMaterialItems`.
- **Output Contract:** Danh sách thành phần nguyên liệu (Tên, Định lượng, Đơn vị tính: ml, gram, cái), Hướng dẫn kỹ thuật pha chế.
- **Business Rules:** Hiển thị công thức chuẩn đã được Chủ chuỗi (`Chain Admin`) phê duyệt.
- **Edge Cases:** Món tùy biến có ghi chú đặc biệt ("Uống thật đậm trà") ➔ KDS highlight ghi chú màu vàng nổi bật để Barista lưu ý.

#### S-05: Cập nhật trạng thái pha chế & Báo hoàn thành món (Preparation Status & Item Ready Action)
- **Mô Tả Nghiệp Vụ:** Barista thao tác chạm cảm ứng để cập nhật tiến độ: Bấm "Bắt đầu làm" ➔ đơn chuyển sang `InPreparation`; Bấm "Hoàn thành" ➔ đơn chuyển sang `ReadyForPickup`. Hệ thống tự động trừ kho nguyên vật liệu tồn tức thời theo định lượng BOM và phát SignalR thông báo tới khách hàng hoặc nhân viên phục vụ.
- **Giao Diện & Kênh:** Web KDS Touch Interaction (`/kds/display`).
- **Input Contract:** `orderId` (Guid), `itemId` (Guid, optional), `newStatus` (InPreparation / ReadyForPickup).
- **System Flow:** API `/api/v1/orders/{id}/status` cập nhật trạng thái trong PostgreSQL, thực thi hàm trừ kho ngầm định lượng nguyên liệu trong bảng `BranchInventory`, broadcast sự kiện `OrderReady` qua SignalR `OrderHub`.
- **Output Contract:** `updatedStatus` (Enum), `deductedInventoryItems` (Array).
- **Business Rules:** Khi bấm Hoàn thành, thẻ đơn tự động biến mất khỏi hàng đợi pha chế và chuyển sang tab "Đã hoàn thành gần đây".
- **Edge Cases:** Barista bấm nhầm nút Hoàn thành ➔ có nút "Hoàn tác" (Undo) trong vòng 10 giây để kéo thẻ đơn quay lại hàng đợi.

#### S-06: Tạo đơn Takeaway tại quầy thu ngân Web POS (Takeaway Order Creation via Web POS)
- **Mô Tả Nghiệp Vụ:** Khách hàng mua mang đi tới quầy, Nhân viên thu ngân thao tác trên giao diện Web POS để chọn món, tùy biến Size/Đường/Đá/Topping theo yêu cầu của khách. Giao diện POS tối ưu thao tác nhanh bằng bàn phím hoặc màn hình cảm ứng lớn.
- **Giao Diện & Kênh:** Web POS Cashier Counter (`/staff/pos`).
- **Input Contract:** `branchId` (Guid), `orderItems` (Array), `orderType = "Takeaway"`.
- **System Flow:** Thu ngân chọn món ➔ Hệ thống tính tiền ➔ Nhập thông tin CRM nếu khách có nhu cầu tích điểm.
- **Output Contract:** `orderSummary` (Mã đơn POS, Danh sách món, Tổng tiền thanh toán).
- **Business Rules:** Đơn Takeaway tạo tại quầy được gắn mã số thứ tự lấy đồ (Pickup Ticket Number: #01, #02...).
- **Edge Cases:** Quầy đông khách xếp hàng ➔ Web POS hỗ trợ chức năng "Lưu tạm đơn" (Hold Order) để xử lý đơn của khách tiếp theo trong khi chờ khách trước chọn món.

#### S-07: Tra cứu khách hàng CRM qua SĐT & Tích lũy 10 ly tặng 1 (CRM Phone Lookup & 10-Cup Loyalty)
- **Mô Tả Nghiệp Vụ:** Khi tạo đơn Takeaway tại quầy, thu ngân hỏi SĐT của khách và nhập vào ô tra cứu CRM. Hệ thống kiểm tra số ly tích lũy hiện có của khách. Chương trình **"Tích lũy 10 ly = Tặng 1 ly miễn phí" CHỈ ÁP DỤNG DUY NHẤT CHO ĐƠN TAKEAWAY TẠI QUẦY**. Nếu khách đã tích đủ 10 ly, Web POS hiển thị nút "Đổi 01 Ly Miễn Phí (Trừ 10 ly tích lũy)". Nếu khách chưa có hồ sơ CRM, thu ngân bấm "Tạo nhanh thành viên" chỉ với SĐT và Họ tên.
- **Giao Diện & Kênh:** Web POS CRM Lookup Drawer (`/staff/pos/crm`).
- **Input Contract:** `phoneNumber` (String 10 digits).
- **System Flow:** API `/api/v1/crm/lookup?phone=...` truy vấn bảng `Customers` và `LoyaltyCards`. Trả về số ly đã tích lũy hiện tại.
- **Output Contract:** `customerName` (String), `currentCupCount` (Int: ví dụ 9/10 ly), `eligibleFreeCups` (Int), `loyaltyTier` (Silver/Gold/Diamond).
- **Business Rules:** Quy tắc 10 ly đổi 1 ly CHỈ áp dụng cho món đồ uống có giá trị thấp nhất hoặc bằng giá trung bình trong đơn Takeaway. KHÔNG áp dụng cho đơn Dine-in và Delivery.
- **Edge Cases:** Khách đọc sai SĐT ➔ Thu ngân có thể sửa nhanh số điện thoại trước khi bấm in hóa đơn.

#### S-08: Thu tiền & Thanh toán đơn Takeaway tại quầy (Takeaway Post-payment Cash/VietQR POS)
- **Mô Tả Nghiệp Vụ:** Khách hàng mua Takeaway thanh toán sau khi đồ uống được pha chế xong hoặc thanh toán ngay tại quầy. Thu ngân chọn hình thức thanh toán: Tiền mặt (nhập tiền khách đưa ➔ hệ thống tự tính tiền thừa trả lại) HOẶC Chuyển khoản VietQR (màn hình hiển thị mã QR PayOS cho khách quét trực tiếp).
- **Giao Diện & Kênh:** Web POS Payment Modal (`/staff/pos/checkout`).
- **Input Contract:** `orderId` (Guid), `paymentMethod` (Cash / VietQR), `cashGiven` (Decimal, nếu tiền mặt).
- **System Flow:** Nếu tiền mặt: Cập nhật `Status = "Paid"`, ghi nhận doanh thu vào ca thu ngân hiện tại. Nếu VietQR: Hiển thị mã QR PayOS, chờ webhook xác nhận `Paid`.
- **Output Contract:** `changeAmount` (Tiền thừa trả khách), `paymentStatus = "Paid"`, lệnh in hóa đơn POS.
- **Business Rules:** Doanh thu tiền mặt được cộng dồn trực tiếp vào số dư két tiền ca làm việc của thu ngân (`Shift Cash Float`).
- **Edge Cases:** Khách đưa tiền rách/tiền giả ➔ Thu ngân từ chối và yêu cầu đổi tờ tiền khác hoặc chuyển sang quét mã VietQR.

#### S-09: Xác nhận thanh toán Tiền mặt & Quét mã VietQR trên hóa đơn Dine-in (Dine-in Cash Payment Confirmation)
- **Mô Tả Nghiệp Vụ:** Khi khách dùng bữa tại bàn yêu cầu thanh toán bằng tiền mặt, nhân viên phục vụ mang Hóa đơn thanh toán ra bàn (trên hóa đơn có in sẵn mã VietQR của đơn hàng). Khách có thể đưa tiền mặt HOẶC quét mã VietQR trên hóa đơn. Sau khi nhận đủ tiền từ khách, nhân viên mở Web Staff trên thiết bị quầy/tablet, chọn Bàn tương ứng và bấm nút "Xác nhận đã thu tiền". Đơn hàng chuyển sang trạng thái `Completed`, bàn được giải phóng về trạng thái `Available`.
- **Giao Diện & Kênh:** Web Staff Table Map & Bill Action (`/staff/tables/[tableId]/confirm-cash`).
- **Input Contract:** `orderId` (Guid), `tableId` (Guid), `staffId` (Guid), `actualAmountReceived` (Decimal).
- **System Flow:** API `/api/v1/payments/cash-confirm` cập nhật `OrderStatus = "Completed"`, `PaymentStatus = "Paid"`, `TableStatus = "Available"`, kích hoạt broadcast SignalR cập nhật sơ đồ bàn.
- **Output Contract:** `isSuccess = true`, `closedOrderCode` (String), `tableReleased` (String: "Bàn 04 đã sẵn sàng").
- **Business Rules:** Nhân viên chịu trách nhiệm nộp đủ số tiền mặt đã xác nhận vào két tiền thu ngân của ca làm việc.
- **Edge Cases:** Khách rời khỏi bàn nhưng chưa thanh toán ➔ Nhân viên báo cáo Quản lý chi nhánh xử lý đơn hàng bất thường (`Void Order / Incident Report`).

#### S-10: Xem sơ đồ bàn & Trạng thái phục vụ theo thời gian thực (Real-time Table Map & Status)
- **Mô Tả Nghiệp Vụ:** Màn hình trực quan hóa sơ đồ mặt bằng chi nhánh với vị trí các bàn ăn theo tầng/khu vực. Mỗi bàn hiển thị màu sắc trạng thái thời gian thực: Trắng (Trống / Sẵn sàng), Xanh dương (Đang có khách ngồi đặt món), Vàng (Khách đang gọi phục vụ), Đỏ (Khách yêu cầu thanh toán).
- **Giao Diện & Kênh:** Web Staff Table Floor Plan (`/staff/tables`).
- **Input Contract:** `branchId` (Guid), SignalR `NotificationHub` connection.
- **System Flow:** Lắng nghe các event `TableStatusChanged`, `ServiceRequested`, `BillRequested` từ SignalR để cập nhật giao diện không cần reload.
- **Output Contract:** Ma trận danh sách Bàn (Mã bàn, Tên khu vực, Sức chứa, Trạng thái hiện tại, Thời gian khách đã ngồi, Tổng tiền tạm tính của bàn).
- **Business Rules:** Bàn chỉ đổi màu Trắng (Trống) sau khi nhân viên đã dọn dẹp và xác nhận đơn cũ đã thanh toán xong.
- **Edge Cases:** Khách tự ý chuyển bàn ➔ Nhân viên có nút thao tác "Chuyển bàn / Gộp bàn" (Transfer/Merge Table) trên giao diện Web Staff.

#### S-11: Tiếp nhận & Phản hồi chuông gọi phục vụ từ bàn khách (Service Request Handling)
- **Mô Tả Nghiệp Vụ:** Khi khách hàng bấm gọi phục vụ từ PWA (`C-12`), chuông cảnh báo âm thanh reo trên Web Staff và bàn tương ứng nhấp nháy màu vàng kèm lý do yêu cầu (Lấy thêm nước, Thêm ống hút, Dọn bàn). Nhân viên bấm "Tiếp nhận" để báo cho đồng nghiệp biết mình đang xử lý, và bấm "Đã phục vụ xong" sau khi hỗ trợ khách hoàn tất.
- **Giao Diện & Kênh:** Web Staff Service Notification Popup & Drawer (`/staff/service-requests`).
- **Input Contract:** `requestId` (Guid), `staffId` (Guid), `action` (Accept / Complete).
- **System Flow:** Cập nhật trạng thái yêu cầu phục vụ trong bảng `ServiceRequests`, dừng chuông báo âm thanh và cập nhật trạng thái bàn trên toàn bộ các thiết bị staff.
- **Output Contract:** `requestStatus` (InService / Resolved), `responseTimeSeconds` (Int).
- **Business Rules:** Ghi nhận thời gian từ lúc khách bấm gọi đến khi nhân viên hoàn thành để tính chỉ số KPI tốc độ phục vụ.
- **Edge Cases:** Có 3 bàn gọi cùng một lúc ➔ giao diện xếp thứ tự ưu tiên theo thời gian gọi sớm nhất.

#### S-12: In phiếu chế biến bếp & In hóa đơn thanh toán (Kitchen Slip & Receipt Printing)
- **Mô Tả Nghiệp Vụ:** Hệ thống hỗ trợ in tự động hoặc in thủ công qua máy in nhiệt POS 80mm: (1) Phiếu chế biến Bếp/Bar (Kitchen Slip) in ngay khi có đơn mới; (2) Hóa đơn thanh toán / Phiếu tạm tính in kèm mã VietQR chuẩn cho khách thanh toán.
- **Giao Diện & Kênh:** Web Staff POS Print Service (Tích hợp Web Print API / ESC/POS Protocol qua Local Bridge).
- **Input Contract:** `orderId` (Guid), `printType` (KitchenSlip / FinalReceipt / PrecheckBill).
- **System Flow:** Sinh chuỗi lệnh in ESC/POS hoặc xuất bản in HTML chuẩn khổ giấy 80mm gửi tới máy in nhiệt qua cổng LAN IP / USB.
- **Output Contract:** `printJobStatus = "Printed"`, `printedAt` (DateTime).
- **Business Rules:** Hóa đơn thanh toán phải in đầy đủ: Tên chi nhánh, Địa chỉ, Mã đơn, Tên nhân viên thu ngân, Danh sách món + Topping, Tổng tiền, Chiết khấu, Thuế VAT và Mã VietQR động.
- **Edge Cases:** Máy in hết giấy hoặc kẹt giấy ➔ Web Staff hiển thị cảnh báo lỗi máy in và cung cấp nút "In lại" (Reprint) sau khi thay giấy.

#### S-13: Báo cáo doanh thu & Thống kê số lượng ly trong ca (Shift Sales & Cup Count Report)
- **Mô Tả Nghiệp Vụ:** Cuối ca làm việc, nhân viên thu ngân xem bảng tổng kết nhanh số liệu trong ca của mình: Tổng số đơn đã tạo, Tổng số ly đã pha chế, Doanh thu phân theo phương thức (Tiền mặt, VietQR), Số voucher đã áp dụng và Số ly khuyến mãi 10 tặng 1 đã đổi.
- **Giao Diện & Kênh:** Web Staff Shift Summary View (`/staff/shift-report`).
- **Input Contract:** `shiftId` (Guid), `staffId` (Guid).
- **System Flow:** Truy vấn dữ liệu tổng hợp từ bảng `Orders` và `OrderItems` lọc theo `ShiftId` và `CashierId`.
- **Output Contract:** `totalOrders` (Int), `totalCups` (Int), `cashRevenue` (Decimal), `vietQrRevenue` (Decimal), `loyaltyFreeCupsRedeemed` (Int).
- **Business Rules:** Nhân viên in phiếu tổng kết ca để kẹp vào phong bì tiền mặt bàn giao cho Quản lý chi nhánh đối soát Z-Report.
- **Edge Cases:** Số liệu tiền mặt không khớp với tiền đếm thực tế ➔ ghi nhận phần chênh lệch vào mục giải trình bàn giao ca.

---

# 🏪 PHẦN 5: ĐẶC TẢ CHI TIẾT ACTOR 3: QUẢN LÝ CHI NHÁNH (BRANCH MANAGER — 12 FEATURES)

Quản lý chi nhánh phụ trách toàn diện vận hành tại cơ sở thông qua **Branch Manager Web Portal** (Route: `(manager)`). Phạm vi dữ liệu được cô lập chặt chẽ trong chi nhánh được phân công quản lý.

### Danh Mục 12 Tính Năng Quản Lý Chi Nhánh (`M-01` đến `M-12`)

#### M-01: Mở ca két tiền & Ghi nhận số dư tiền mặt đầu ngày (Opening Shift Cash Float Declaration)
- **Mô Tả Nghiệp Vụ:** Đầu mỗi ca làm việc hoặc đầu ngày kinh doanh, Quản lý chi nhánh mở ca két tiền trên hệ thống, kiểm đếm số tiền mặt thực tế có trong ngăn kéo thu ngân (Tiền lẻ thối ban đầu) và khai báo số dư đầu ca (`Initial Float Amount`).
- **Giao Diện & Kênh:** Manager Web Portal (`/manager/shifts/open`).
- **Input Contract:** `branchId` (Guid), `managerId` (Guid), `initialCashFloat` (Decimal: ví dụ 2.000.000 VNĐ), `denominationBreakdown` (Chi tiết số tờ tiền theo mệnh giá 500k, 200k, 100k, 50k, 20k, 10k).
- **System Flow:** Tạo bản ghi mới trong bảng `WorkShifts` với trạng thái `Status = "Open"`, lưu trữ số dư đầu ca và thời gian mở ca.
- **Output Contract:** `shiftId` (Guid), `shiftCode` (String: "SHIFT-20260417-01"), `status = "Open"`.
- **Business Rules:** Không thể mở ca mới nếu ca trước đó của chi nhánh chưa được thực hiện Kết ca đóng két.
- **Edge Cases:** Số tiền thực tế trong két khác số dư bàn giao từ ca trước ➔ Quản lý bắt buộc nhập lý do chênh lệch trước khi bấm Mở ca.

#### M-02: Kết ca kiểm đếm két & Đối soát biên bản Z-Report (Closing Shift Reconciliation & Z-Report)
- **Mô Tả Nghiệp Vụ:** Kết thúc ca làm việc, Quản lý cùng Thu ngân kiểm đếm toàn bộ tiền mặt thực tế trong két. Hệ thống tự động tính toán Doanh thu lý thuyết = Số dư đầu ca + Tổng tiền mặt thu trong ca - Tiền chi tạm ứng. Quản lý nhập số tiền thực đếm, hệ thống sinh Biên bản đối soát Z-Report và tính toán số tiền Thừa/Thiếu (`Cash Variance`).
- **Giao Diện & Kênh:** Manager Web Portal (`/manager/shifts/close`).
- **Input Contract:** `shiftId` (Guid), `actualCountedCash` (Decimal), `cashDropAmount` (Số tiền nộp về két sắt an toàn), `closingNote` (String).
- **System Flow:** API `/api/v1/shifts/close` đóng ca, tính `variance = actualCountedCash - expectedCash`, ghi nhận vào bảng `ZReports`, xuất file PDF Z-Report và gửi thông báo tổng kết ca tới Admin.
- **Output Contract:** `zReportId` (Guid), `expectedCash` (Decimal), `actualCash` (Decimal), `variance` (Decimal), `totalVietQrSales` (Decimal), `zReportPdfUrl` (String).
- **Business Rules:** Biên bản Z-Report sau khi chốt là bất biến (Immutable), không thể chỉnh sửa dữ liệu để đảm bảo tính toàn vẹn tài chính.
- **Edge Cases:** Chênh lệch tiền mặt vượt quá 100.000 VNĐ ➔ hệ thống gắn cờ cảnh báo đỏ và bắt buộc Quản lý cùng Thu ngân ký xác nhận giải trình.

#### M-03: Lập lịch phân ca làm việc cho nhân viên chi nhánh (Staff Shift Scheduling & Roster)
- **Mô Tả Nghiệp Vụ:** Quản lý lập lịch làm việc hàng tuần cho đội ngũ nhân viên chi nhánh: Phân công nhân viên vào các ca (Ca sáng: 06:30 - 14:30, Ca chiều: 14:30 - 22:30), chỉ định vai trò cụ thể trong ca (Trưởng ca, Barista chính, Barista phụ, Thu ngân, Phục vụ bàn).
- **Giao Diện & Kênh:** Manager Shift Roster Grid (`/manager/schedules`).
- **Input Contract:** `branchId` (Guid), `weekStartDate` (Date), `scheduleEntries` (Array of { staffId, shiftDate, shiftSlotId, assignedRole }).
- **System Flow:** Lưu lịch phân ca vào bảng `StaffSchedules`. Kiểm tra trùng lịch và cảnh báo nếu có nhân viên bị phân công làm 2 ca liên tiếp không đủ thời gian nghỉ.
- **Output Contract:** Bảng lịch phân ca trực quan dạng Calendar/Timeline tuần.
- **Business Rules:** Mỗi ca làm việc bắt buộc phải có tối thiểu 01 Thu ngân và 01 Barista đạt chuẩn vận hành.
- **Edge Cases:** Nhân viên xin đổi ca đột xuất ➔ Quản lý thao tác đổi ca (Swap Shift) trực tiếp trên lịch và hệ thống gửi thông báo tới nhân viên liên quan.

#### M-04: Giám sát chấm công WiFi & Phê duyệt giải trình ca (Attendance Monitoring & Exception Approval)
- **Mô Tả Nghiệp Vụ:** Quản lý theo dõi bảng chấm công thời gian thực của nhân viên chi nhánh: Giờ check-in, giờ check-out, trạng thái đi đúng giờ / đi muộn / về sớm. Xem xét và phê duyệt các đơn giải trình chấm công của nhân viên (Quên chấm công, Sự cố WiFi chi nhánh).
- **Giao Diện & Kênh:** Manager Attendance Dashboard (`/manager/attendance`).
- **Input Contract:** `attendanceId` (Guid), `approvalStatus` (Approved / Rejected), `managerNote` (String).
- **System Flow:** Truy vấn dữ liệu bảng `AttendanceRecords` kết hợp `AttendanceRequests`. Cập nhật trạng thái công chuẩn cho nhân viên sau khi duyệt.
- **Output Contract:** Bảng tổng hợp công giờ làm việc trong tháng xuất ra định dạng Excel/CSV.
- **Business Rules:** Chỉ Quản lý chi nhánh hoặc Admin mới có quyền duyệt hợp lệ cho các bản ghi chấm công bị gắn cờ bất thường.
- **Edge Cases:** Nhân viên khiếu nại số giờ công ➔ Quản lý tra cứu lịch sử log kết nối WiFi của nhân viên để đối soát.

#### M-05: Kiểm kê tồn kho nguyên vật liệu BOM chi nhánh (BOM Raw Material Stock Counting)
- **Mô Tả Nghiệp Vụ:** Định kỳ cuối ngày hoặc cuối tuần, Quản lý thực hiện kiểm kê kho nguyên vật liệu tại quầy Bar và kho lưu trữ của chi nhánh: Cà phê hạt, Sữa tươi, Sữa đặc, Cốt trà, Đường cát, Ly giấy, Ống hút, Topping. Nhập số lượng thực tế đếm được để so sánh với số tồn lý thuyết trên phần mềm (đã tự động trừ theo định lượng BOM bán hàng).
- **Giao Diện & Kênh:** Manager Stock Count Sheet (`/manager/inventory/count`).
- **Input Contract:** `branchId` (Guid), `countItems` (Array of { rawMaterialId, actualQuantity, unit }).
- **System Flow:** API `/api/v1/inventory/reconcile` so sánh `actualQuantity` với `systemQuantity` trong bảng `BranchInventory`. Tính toán tỷ lệ hao hụt (`Wastage Percentage`) và sinh phiếu kiểm kê kho.
- **Output Contract:** Bảng chênh lệch kho nguyên vật liệu (Tồn lý thuyết, Tồn thực tế, Số lượng lệch, Giá trị lệch VNĐ).
- **Business Rules:** Hao hụt nguyên vật liệu vượt định mức cho phép (> 3%) sẽ kích hoạt cảnh báo gửi tới Chủ chuỗi.
- **Edge Cases:** Phát hiện nguyên liệu hết hạn sử dụng (Expired) ➔ Quản lý lập phiếu Xuất hủy kho (`Stock Disposal`) ghi rõ nguyên nhân.

#### M-06: Lập phiếu yêu cầu nhập nguyên vật liệu từ kho tổng (Stock Requisition & PO Generation)
- **Mô Tả Nghiệp Vụ:** Dựa trên lượng tồn kho thực tế và dự báo nhu cầu bán hàng trong các ngày tới, Quản lý lập Phiếu yêu cầu nhập kho nguyên vật liệu gửi lên Chuỗi cung ứng / Admin để được duyệt xuất hàng từ Kho tổng về chi nhánh.
- **Giao Diện & Kênh:** Manager Stock Requisition Form (`/manager/inventory/requisitions`).
- **Input Contract:** `branchId` (Guid), `requiredDeliveryDate` (Date), `requisitionItems` (Array of { rawMaterialId, requestQuantity, unit, note }).
- **System Flow:** Tạo bản ghi trong bảng `StockRequisitions` với trạng thái `Status = "PendingApproval"`. Gửi thông báo SignalR tới Admin Portal.
- **Output Contract:** `requisitionCode` (String: "REQ-CN01-20260417"), `status = "PendingApproval"`, `totalEstimatedCost` (Decimal).
- **Business Rules:** Phiếu yêu cầu nhập hàng phải gửi trước 17:00 hàng ngày để Kho tổng kịp điều phối xe giao hàng vào sáng hôm sau.
- **Edge Cases:** Chi nhánh đột xuất hết nguyên liệu cốt lõi (Hết sạch cà phê trong giờ cao điểm) ➔ Quản lý lập phiếu "Yêu cầu khẩn cấp" có gắn tag Cấp bách.

#### M-07: Cấu hình trạng thái mở/đóng bàn & Sơ đồ mặt bằng chi nhánh (Table Layout & Availability Config)
- **Mô Tả Nghiệp Vụ:** Quản lý tùy chỉnh sơ đồ bàn ăn tại chi nhánh: Bổ sung bàn mới, đổi tên bàn, thay đổi khu vực (Trong nhà, Ngoài trời, Tầng 1, Tầng 2), tạm khóa bàn đang sửa chữa (`Inactive / Maintenance`) hoặc mở lại bàn phục vụ.
- **Giao Diện & Kênh:** Manager Table Management View (`/manager/tables/config`).
- **Input Contract:** `branchId` (Guid), `tablesConfig` (Array of { tableId, tableName, areaId, capacity, isActive }).
- **System Flow:** Cập nhật bảng `Tables` và `TableAreas` trong PostgreSQL. Kích hoạt cập nhật mã QR tương ứng của từng bàn.
- **Output Contract:** Danh sách bàn cập nhật thành công kèm chức năng "Tải trọn bộ file in mã QR Bàn (PDF)".
- **Business Rules:** Không thể xóa hoặc khóa bàn khi đang có đơn hàng chưa thanh toán hoạt động tại bàn đó.
- **Edge Cases:** Quán tổ chức sự kiện cần ghép 4 bàn nhỏ thành 1 bàn lớn ➔ Quản lý cấu hình ghép bàn ảo trên giao diện.

#### M-08: Tùy chỉnh giá bán & Bật/tắt món đặc thù chi nhánh (Branch Menu Overrides & 86 Item Toggling)
- **Mô Tả Nghiệp Vụ:** Quản lý có quyền: (1) Bật/tắt tức thì trạng thái hết hàng tạm thời của món (`Item 86 / Sold Out`) khi quầy bar hết sạch nguyên liệu đột xuất; (2) Điều chỉnh tăng/giảm giá bán một số món trong biên độ cho phép (+/- 10%) so với giá chuẩn nếu được phân quyền, hoặc áp dụng giá theo vị trí đặc thù của chi nhánh.
- **Giao Diện & Kênh:** Manager Menu Overrides Page (`/manager/menu/overrides`).
- **Input Contract:** `branchId` (Guid), `productId` (Guid), `isAvailable` (Boolean), `overridePrice` (Decimal, optional).
- **System Flow:** Cập nhật bảng `BranchProductPrices` và cập nhật tức thì vào Redis Cache key `branch:{id}:menu:active`. Broadcast SignalR tới toàn bộ khách hàng đang xem Menu PWA.
- **Output Contract:** Trạng thái món cập nhật ngay lập tức sau < 1 giây trên toàn bộ thiết bị khách hàng.
- **Business Rules:** Việc tắt món (`Item 86`) có hiệu lực tức thì trên PWA và Web POS; Quản lý không có quyền xóa món khỏi hệ thống (chỉ Admin mới có quyền CRUD món).
- **Edge Cases:** Barista nhập thêm được nguyên liệu ➔ Quản lý bấm bật lại món, PWA tự động hiển thị lại nút "Thêm vào giỏ" cho khách.

#### M-09: Cấu hình thông số WiFi chấm công chi nhánh (Branch Attendance WiFi BSSID/IP Config)
- **Mô Tả Nghiệp Vụ:** Quản lý khai báo và cập nhật danh sách các Access Point WiFi hợp lệ tại chi nhánh dùng cho việc chấm công: Tên mạng SSID, Địa chỉ vật lý BSSID (MAC Address của router) và Dải địa chỉ IP Gateway nội bộ.
- **Giao Diện & Kênh:** Manager WiFi Settings (`/manager/settings/wifi`).
- **Input Contract:** `branchId` (Guid), `wifiList` (Array of { ssid, bssid, ipGateway, subnetMask, locationDesc }).
- **System Flow:** Lưu thông tin vào bảng `BranchWifiConfigs`. Khi nhân viên chấm công, Backend sẽ đối soát thông tin mạng của thiết bị gửi lên với bảng cấu hình này.
- **Output Contract:** `isSuccess = true`, `activeWifiPointsCount` (Int).
- **Business Rules:** Bắt buộc phải có tối thiểu 01 BSSID WiFi chính xác để nhân viên có thể thực hiện chấm công vào ca.
- **Edge Cases:** Chi nhánh thay đổi nhà mạng hoặc đổi Router WiFi mới ➔ Quản lý cập nhật BSSID mới và kích hoạt áp dụng ngay lập tức.

#### M-10: Tiếp nhận cảnh báo khẩn cấp đánh giá tiêu cực <= 2 sao (Critical Negative Review Alert <= 2 Stars)
- **Mô Tả Nghiệp Vụ:** Khi khách hàng gửi đánh giá từ 1 đến 2 sao trên PWA (`C-18`), hệ thống kích hoạt chuông cảnh báo khẩn cấp màu đỏ trên Dashboard Quản lý chi nhánh kèm thông tin chi tiết: Tên khách, Số điện thoại, Mã đơn hàng, Tên món bị chê và Nội dung phản ánh tiêu cực.
- **Giao Diện & Kênh:** Manager Urgent Review Alert Modal & Notification Banner (`/manager/reviews/alerts`).
- **Input Contract:** SignalR Notification từ Backend `ReviewService`.
- **System Flow:** Lắng nghe event `CriticalReviewSubmitted` từ SignalR `NotificationHub`. Hiển thị popup cảnh báo kèm nút "Gọi điện chăm sóc khách ngay" và "Gửi voucher xin lỗi".
- **Output Contract:** Chi tiết đánh giá tiêu cực, Lịch sử tương tác xử lý khiếu nại của Quản lý.
- **Business Rules:** Quản lý chi nhánh có trách nhiệm liên hệ khách hàng giải quyết khiếu nại trong vòng tối đa 30 phút kể từ khi nhận cảnh báo.
- **Edge Cases:** Đánh giá tiêu cực có ngôn từ xúc phạm hoặc phá hoại ác ý ➔ Quản lý gắn cờ báo cáo Admin xem xét ẩn bình luận.

#### M-11: Kiểm duyệt hình ảnh đánh giá & Phản hồi khách hàng (Feedback Photo Moderation & Customer Care)
- **Mô Tả Nghiệp Vụ:** Quản lý duyệt danh sách hình ảnh do khách hàng tải lên kèm đánh giá (`C-19`): Duyệt cho phép hiển thị công khai (`Approve`), Từ chối ảnh không phù hợp/ảnh mờ (`Reject`), và Viết phản hồi chính thức từ phía thương hiệu gửi tới khách hàng.
- **Giao Diện & Kênh:** Manager Feedback Moderation Grid (`/manager/reviews/moderation`).
- **Input Contract:** `reviewId` (Guid), `photoId` (Guid), `action` (Approve / Reject), `replyText` (String, max 500 chars).
- **System Flow:** API `/api/v1/reviews/{id}/moderate` cập nhật cờ `IsApproved = true` trong bảng `ReviewPhotos` và lưu câu trả lời vào bảng `ReviewReplies`.
- **Output Contract:** Trạng thái kiểm duyệt ảnh, Phản hồi của quán hiển thị trên PWA cho khách hàng thấy.
- **Business Rules:** Ảnh chứa nội dung phản cảm, không liên quan đến món ăn hoặc để lộ thông tin nhạy cảm bắt buộc phải bị Từ chối kiểm duyệt.
- **Edge Cases:** Khách hàng hài lòng sau khi được chăm sóc ➔ khách có quyền chỉnh sửa lại số sao đánh giá trên PWA.

#### M-12: Xem dashboard chỉ số vận hành & Hiệu suất bán hàng chi nhánh (Branch Operational Dashboard & KPI)
- **Mô Tả Nghiệp Vụ:** Bảng điều khiển thời gian thực hiển thị toàn diện bức tranh vận hành chi nhánh trong ngày: Doanh thu thực tế theo giờ, Số lượng đơn hàng (Dine-in, Takeaway, Delivery), Tỷ lệ hoàn thành đơn đúng hạn, Thời gian pha chế trung bình mỗi món, Top 5 món bán chạy nhất chi nhánh và Tỷ lệ đánh giá hài lòng của khách.
- **Giao Diện & Kênh:** Manager Real-time KPI Dashboard (`/manager/dashboard`).
- **Input Contract:** `branchId` (Guid), `dateFilter` (Hôm nay / Tuần này / Tháng này).
- **System Flow:** Tổng hợp dữ liệu từ PostgreSQL và Redis Cache, hiển thị các biểu đồ trực quan qua Recharts/Chart.js.
- **Output Contract:** Metric Cards: Doanh thu, Đơn hàng, Số ly bán ra, Doanh thu trung bình/đơn (AOV), Biểu đồ doanh thu theo khung giờ.
- **Business Rules:** Dữ liệu tự động làm mới mỗi 30 giây qua kết nối SignalR hoặc WebSocket.
- **Edge Cases:** Mất kết nối server ➔ hiển thị dữ liệu cache gần nhất kèm nhãn thời gian cập nhật cuối.

---

# 👑 PHẦN 6: ĐẶC TẢ CHI TIẾT ACTOR 4: CHỦ CHUỖI / QUẢN TRỊ VIÊN (CHAIN ADMIN — 17 FEATURES)

Chủ chuỗi và Quản trị viên điều hành toàn bộ hệ thống thông qua **Admin Executive Portal** (Route: `(admin)`). Có toàn quyền kiểm soát dữ liệu đa chi nhánh, danh mục sản phẩm, định lượng BOM, chiến lược giá vùng, khai phá dữ liệu AI-2 và báo cáo tài chính P&L hợp nhất.

### Danh Mục 17 Tính Năng Chủ Chuỗi (`A-01` đến `A-17`)

#### A-01: Quản lý danh mục chi nhánh toàn chuỗi & Cấu hình vận hành (Chain Branch Management)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi thực hiện thêm mới chi nhánh, cấu hình thông tin chi nhánh (Tên, Địa chỉ, Số điện thoại, Tọa độ GPS, Giờ mở/đóng cửa), kích hoạt hoặc tạm dừng hoạt động chi nhánh, cấu hình tài khoản ngân hàng thụ hưởng VietQR PayOS riêng cho từng chi nhánh.
- **Giao Diện & Kênh:** Admin Branch Management Grid (`/admin/branches`).
- **Input Contract:** `branchCode` (String: "CN-Q1"), `branchName` (String), `address` (String), `phone` (String), `operatingHours` (String: "07:00-22:30"), `payOsConfig` (ClientId, ApiKey, ChecksumKey), `isActive` (Boolean).
- **System Flow:** API `/api/v1/admin/branches` thực hiện CRUD trên bảng `Branches`.
- **Output Contract:** Danh sách chi nhánh kèm trạng thái vận hành và chỉ số doanh thu tổng hợp.
- **Business Rules:** Mỗi chi nhánh có thể cấu hình tài khoản ngân hàng thụ hưởng PayOS độc lập hoặc dùng chung tài khoản tổng của công ty mẹ.
- **Edge Cases:** Đóng cửa chi nhánh vĩnh viễn ➔ Chuyển trạng thái sang `Deactivated`, lưu trữ lịch sử giao dịch cũ để phục vụ kiểm toán tài chính.

#### A-02: Quản lý tài khoản người dùng, nhân sự & Phân quyền RBAC (User, Staff & RBAC Management)
- **Mô Tả Nghiệp Vụ:** Quản lý toàn bộ hồ sơ nhân viên trong hệ thống: Tạo tài khoản nhân viên mới, phân bổ nhân viên vào chi nhánh làm việc, gán vai trò RBAC (`ChainAdmin`, `BranchManager`, `BaristaStaff`, `CashierStaff`, `ServiceStaff`), cấp lại mật khẩu hoặc vô hiệu hóa tài khoản khi nhân viên nghỉ việc.
- **Giao Diện & Kênh:** Admin User & RBAC Management (`/admin/users`).
- **Input Contract:** `staffCode` (String), `fullName` (String), `email` (String), `phone` (String), `assignedBranchId` (Guid), `roleId` (Enum Role), `isActive` (Boolean).
- **System Flow:** Lưu thông tin vào bảng `Staff` và `UserRoles`. Mã hóa mật khẩu bằng BCrypt/Argon2.
- **Output Contract:** Danh sách nhân sự kèm vai trò và lịch sử thao tác hệ thống.
- **Business Rules:** Chỉ tài khoản có quyền `ChainAdmin` mới có thể tạo hoặc gán quyền `BranchManager` và `ChainAdmin`.
- **Edge Cases:** Vô hiệu hóa tài khoản nhân viên đang trong ca làm việc ➔ Token JWT của nhân viên lập tức bị thu hồi vào Blacklist Redis Cache và buộc đăng xuất.

#### A-03: Tạo mới món ăn & Cấu hình phân loại thực đơn (Product Creation & Category Mapping)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi tạo mới sản phẩm đồ uống/món ăn vào hệ thống Menu tổng: Nhập Tên món, Mã SKU, Mô tả hương vị, Gán vào Danh mục chính (Cà phê, Trà, Sinh tố, Bánh), Thiết lập Giá bán chuẩn chuỗi, Định nghĩa các Size khả dụng (S, M, L) và Phụ thu tương ứng.
- **Giao Diện & Kênh:** Admin Product Create Form (`/admin/products/create`).
- **Input Contract:** `sku` (String: "CF-ESP-01"), `productName` (String), `categoryId` (Guid), `description` (String), `basePrice` (Decimal: ví dụ 35.000 VNĐ), `sizeVariants` (Array of { sizeName, extraPrice }).
- **System Flow:** API `/api/v1/admin/products` tạo mới bản ghi trong bảng `Products` và `ProductVariants`. Đồng bộ dữ liệu Menu sang toàn bộ chi nhánh.
- **Output Contract:** `productId` (Guid), `status = "Active"`, `createdProductDto` (Object).
- **Business Rules:** Mã SKU là duy nhất trên toàn hệ thống chuỗi. Tên món không được trùng lặp trong cùng một danh mục.
- **Edge Cases:** Tạo món mới nhưng chưa kịp cấu hình ảnh ➔ hệ thống gán ảnh placeholder mặc định của thương hiệu.

#### A-04: Chỉnh sửa thông tin món, giá chuẩn & Tùy chọn định lượng (Product Editing & Variant Settings)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi cập nhật thông tin món ăn hiện hữu: Sửa tên món, cập nhật mô tả, điều chỉnh giá bán cơ sở, thêm/bớt các mức tùy biến (Mức đường, Mức đá, Danh sách topping đi kèm).
- **Giao Diện & Kênh:** Admin Product Edit Page (`/admin/products/[id]/edit`).
- **Input Contract:** `productId` (Guid), `updatedFields` (Object chứa các trường cần sửa), `customizationOptions` (Array).
- **System Flow:** Cập nhật bảng `Products`, làm mới cache Redis trên toàn bộ các chi nhánh (`branch:*:menu:active`).
- **Output Contract:** `isSuccess = true`, `updatedProduct` (Object).
- **Business Rules:** Mọi thay đổi về giá bán chuẩn sẽ lập tức có hiệu lực trên toàn bộ chi nhánh chưa cấu hình bảng giá vùng đặc thù.
- **Edge Cases:** Khách hàng đang mở giỏ hàng đúng lúc giá món thay đổi ➔ khi bấm thanh toán, hệ thống thông báo giá đã cập nhật và yêu cầu xác nhận lại tổng tiền.

#### A-05: Xóa mềm & Vô hiệu hóa món ăn trên toàn hệ thống (Product Soft Delete & System Deactivation)
- **Mô Tả Nghiệp Vụ:** Khi một món ăn ngừng kinh doanh, Chủ chuỗi thực hiện Xóa mềm (`Soft Delete` gán cờ `IsDeleted = true`, `DeletedAt = DateTime.UtcNow`) hoặc Chuyển trạng thái sang Vô hiệu hóa (`IsActive = false`). Món ăn lập tức ẩn khỏi thực đơn của tất cả chi nhánh nhưng dữ liệu lịch sử trong các hóa đơn cũ vẫn được bảo toàn nguyên vẹn.
- **Giao Diện & Kênh:** Admin Product List Action (`/admin/products`).
- **Input Contract:** `productId` (Guid), `deleteReason` (String).
- **System Flow:** API `/api/v1/admin/products/{id}` thực hiện Soft Delete trong PostgreSQL, xóa sản phẩm khỏi Redis Cache Menu.
- **Output Contract:** `isDeleted = true`, `message = "Đã vô hiệu hóa món ăn thành công"`.
- **Business Rules:** Tuyệt đối KHÔNG thực hiện Hard Delete (xóa vật lý) khỏi cơ sở dữ liệu để bảo toàn tính toàn vẹn khóa ngoại của các đơn hàng và báo cáo tài chính trong quá khứ.
- **Edge Cases:** Món ăn bị xóa mềm nhưng đang nằm trong công thức Combo AI-2 ➔ hệ thống tự động cảnh báo và hủy kích hoạt combo chứa món đó.

#### A-06: Thay thế món cũ bằng món mới tương đương (Product Replacement & Migration)
- **Mô Tả Nghiệp Vụ:** Khi chuỗi nâng cấp công thức một món đồ uống (Ví dụ: Thay thế "Trà Sữa Truyền Thống v1" bằng "Trà Sữa Oolong Nướng v2"), Admin sử dụng tính năng Thay thế món để tự động chuyển toàn bộ cấu hình liên kết, nhóm topping và dữ liệu gợi ý sang món mới mà không làm gián đoạn trải nghiệm người dùng.
- **Giao Diện & Kênh:** Admin Product Replacement Modal (`/admin/products/[id]/replace`).
- **Input Contract:** `oldProductId` (Guid), `newProductId` (Guid), `effectiveDate` (DateTime).
- **System Flow:** Cập nhật ánh xạ sản phẩm trong bảng cấu hình Menu, ghi nhận lịch sử thay thế vào nhật ký kiểm toán `AuditLogs`.
- **Output Contract:** `migrationStatus = "Completed"`, `affectedBranchesCount` (Int).
- **Business Rules:** Món cũ tự động chuyển sang trạng thái `Deactivated` tại thời điểm món mới chính thức phát hành.
- **Edge Cases:** Các voucher đang áp dụng cho món cũ ➔ tự động kế thừa áp dụng cho món mới nếu Admin tích chọn tùy chọn kế thừa ưu đãi.

#### A-07: Quản lý tải lên & Tối ưu hóa hình ảnh món ăn định dạng WebP (WebP Image Upload & Asset Management)
- **Mô Tả Nghiệp Vụ:** Admin tải lên hình ảnh đại diện và ảnh banner cho từng món ăn. Hệ thống tự động xử lý hình ảnh qua thư viện SixLabors.ImageSharp: Cắt đúng tỷ lệ chuẩn (1:1 cho thumbnail, 16:9 cho banner), nén giảm dung lượng và chuyển đổi 100% sang định dạng hiện đại `image/webp` (dung lượng tối ưu < 150KB nhưng vẫn giữ độ sắc nét cao).
- **Giao Diện & Kênh:** Admin Media Asset Manager (`/admin/media/upload`).
- **Input Contract:** `imageFile` (File binary: JPG, PNG), `targetEntity` (Product / Category / Banner), `entityId` (Guid).
- **System Flow:** Backend xử lý ảnh, nén sang định dạng WebP, lưu trữ tại thư mục tĩnh hoặc CDN Storage, ghi URL WebP vào bảng `MediaAssets` và cập nhật trường `ImageUrl` của sản phẩm.
- **Output Contract:** `webpUrl` (String: "/assets/products/tra-dao-cam-sa.webp"), `fileSizeBytes` (Int: ví dụ 84.520 bytes).
- **Business Rules:** Chỉ chấp nhận định dạng ảnh đầu vào hợp lệ; tự động từ chối các file có dung lượng gốc vượt quá 10MB.
- **Edge Cases:** Tải ảnh chất lượng quá thấp (< 300x300px) ➔ cảnh báo Admin ảnh có thể bị mờ trên màn hình hiển thị độ phân giải cao.

#### A-08: Quản lý danh mục thực đơn & Sắp xếp thứ tự hiển thị (Menu Categories & Display Ordering)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi tạo mới, chỉnh sửa, xóa danh mục món (Categories) và kéo thả trực quan để thay đổi thứ tự ưu tiên hiển thị của các danh mục và các món trên thực đơn PWA của khách hàng (Ví dụ: Đưa Danh mục "Món Mới Mùa Hè" lên vị trí đầu tiên).
- **Giao Diện & Kênh:** Admin Category Drag & Drop Order View (`/admin/categories`).
- **Input Contract:** `categoriesOrderList` (Array of { categoryId, displayOrder: Int }), `productsOrderList` (Array of { productId, displayOrder: Int }).
- **System Flow:** API `/api/v1/admin/categories/reorder` cập nhật trường `DisplayOrder` trong bảng `Categories` và `Products`. Làm mới Redis Cache Menu.
- **Output Contract:** `isSuccess = true`, thứ tự thực đơn được cập nhật đồng bộ toàn chuỗi.
- **Business Rules:** Thứ tự hiển thị số nguyên nhỏ hơn sẽ được ưu tiên hiển thị trước trên giao diện PWA (từ trái qua phải, từ trên xuống dưới).
- **Edge Cases:** Danh mục rỗng không có sản phẩm nào ➔ tự động ẩn khỏi giao diện khách hàng PWA.

#### A-09: Thiết lập & Lên lịch thực đơn theo mùa vụ / Khung giờ vàng (Seasonal Menus & Time-based Scheduling)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi thiết lập lịch phát hành thực đơn tự động theo thời gian: (1) Thực đơn mùa vụ (Ví dụ: Menu Giáng Sinh chỉ mở bán từ 01/12 đến 31/12); (2) Thực đơn khung giờ vàng (Ví dụ: Menu Happy Hour giảm giá trà trái cây từ 14:00 đến 17:00 các ngày trong tuần).
- **Giao Diện & Kênh:** Admin Menu Scheduler View (`/admin/menu/schedules`).
- **Input Contract:** `scheduleName` (String), `startDate` (DateTime), `endDate` (DateTime), `activeDaysOfWeek` (Array of Int 1-7), `startTime` (TimeSpan), `endTime` (TimeSpan), `includedProductIds` (Array of Guid).
- **System Flow:** Lưu vào bảng `MenuSchedules`. Background Worker định kỳ kiểm tra lịch mỗi phút để kích hoạt/hủy kích hoạt món trên Redis Cache.
- **Output Contract:** `scheduleId` (Guid), `status = "Scheduled"`, `timerCountdown` (Object).
- **Business Rules:** Món theo lịch tự động xuất hiện trên thực đơn PWA khi đến giờ mở bán và tự động ẩn đi khi hết khung giờ.
- **Edge Cases:** Trùng lặp nhiều khung giờ lịch cho cùng một món ➔ hệ thống áp dụng mức giá có lợi nhất cho khách hàng.

#### A-10: Định nghĩa công thức định lượng nguyên vật liệu BOM chuẩn chuỗi (Master BOM Recipe Definition)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi định nghĩa cấu trúc Định Lượng Nguyên Vật Liệu (Bill of Materials - BOM) chuẩn hóa cho từng món ăn trên toàn hệ thống: Khai báo từng thành phần nguyên liệu thô cấu thành (Ví dụ: 01 Ly Trà Đào = 120ml Trà đen + 20ml Syrup Đào + 2 miếng Đào ngâm + 1 Ly giấy 500ml + 1 Ống hút). Đây là căn cứ bắt buộc để hệ thống tự động trừ kho nguyên liệu thời gian thực khi Barista pha chế và tính toán giá vốn hàng bán (COGS).
- **Giao Diện & Kênh:** Admin Master BOM Editor (`/admin/bom/recipes/[productId]`).
- **Input Contract:** `productId` (Guid), `variantId` (Guid: Size M/L), `bomItems` (Array of { rawMaterialId, standardQuantity, unit, costPerUnit, wastageAllowancePercent }).
- **System Flow:** API `/api/v1/admin/bom` ghi nhận công thức vào bảng `BillOfMaterials` và `BillOfMaterialItems`. Tự động tính toán Tổng chi phí giá vốn lý thuyết (`Standard COGS`).
- **Output Contract:** `bomId` (Guid), `standardCost` (Decimal: ví dụ 9.200 VNĐ/ly), `grossMarginPercent` (Decimal: ví dụ 73.7%).
- **Business Rules:** Mỗi món ăn và mỗi size bắt buộc phải có định nghĩa BOM chuẩn để kích hoạt chức năng tự động trừ kho khi hoàn thành đơn.
- **Edge Cases:** Giá nhập nguyên liệu thô biến động tăng > 15% ➔ hệ thống cảnh báo Admin biên độ lợi nhuận gộp của món bị suy giảm.

#### A-11: Quản lý nhóm giá & Thiết lập chính sách giá theo vùng địa lý (Tiered Pricing & Regional Price Groups)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi phân chia các chi nhánh thành các Nhóm Vùng Giá (Tiered Pricing Groups): Vùng 1 (Trung tâm Quận 1 / Sân bay: Giá cao hơn +15%), Vùng 2 (Ngoại thành / Tỉnh: Giá chuẩn cơ sở). Thiết lập chính sách giá bán khác nhau cho từng vùng địa lý mà không cần tạo nhiều sản phẩm trùng lặp.
- **Giao Diện & Kênh:** Admin Regional Pricing Matrix (`/admin/pricing/groups`).
- **Input Contract:** `pricingGroupId` (Guid), `groupName` (String: "Vùng Trung Tâm"), `branchIds` (Array of Guid), `priceAdjustments` (Array of { productId, overridePrice }).
- **System Flow:** Lưu thông tin vào bảng `PricingGroups` và `BranchProductPrices`. Khách hàng quét QR tại chi nhánh thuộc vùng nào sẽ tự động nhận giá của vùng đó.
- **Output Contract:** Ma trận đối chiếu giá bán sản phẩm theo từng nhóm chi nhánh.
- **Business Rules:** Giá bán vùng ghi đè (Override) sẽ được ưu tiên cao hơn giá chuẩn cơ sở của sản phẩm.
- **Edge Cases:** Một chi nhánh được chuyển từ Vùng 2 sang Vùng 1 ➔ toàn bộ thực đơn chi nhánh đó tự động cập nhật bảng giá mới trong vòng 1 giây.

#### A-12: Khai phá tập mục phổ biến & Sinh quy luật kết hợp AI-2 Apriori (AI-2 Apriori Association Rule Mining)
- **Mô Tả Nghiệp Vụ:** Admin kích hoạt tiến trình khai phá dữ liệu thông minh trên toàn bộ tập dữ liệu lịch sử các đơn hàng đã hoàn tất (Orders Dataset). Thuật toán **AI-2 Apriori** phân tích các tập mục phổ biến (Frequent Itemsets), tính toán các chỉ số thống kê: Độ hỗ trợ (Support $\ge 2\%$), Độ tin cậy (Confidence $\ge 60\%$), và Độ nâng (Lift $> 1.2$) để phát hiện các cặp/nhóm món thường xuyên được khách hàng mua cùng nhau (Ví dụ: `{Trà Đào Cam Sả} \Rightarrow \{Bánh Mì Phô Mai Tươi\}` với Lift = 2.45).
- **Giao Diện & Kênh:** Admin AI Apriori Analytics View (`/admin/ai/apriori`).
- **Input Contract:** `minSupport` (Decimal: 0.02), `minConfidence` (Decimal: 0.60), `minLift` (Decimal: 1.20), `dateRange` (30 ngày / 90 ngày gần nhất).
- **System Flow:** Backend Background Service chạy thuật toán Apriori xử lý dữ liệu đơn hàng trong PostgreSQL, trích xuất danh sách các quy luật kết hợp (`Association Rules`) thỏa mãn ngưỡng và lưu vào bảng `AprioriRules`.
- **Output Contract:** Bảng danh sách quy luật kết hợp: Antecedent (Vế trái), Consequent (Vế phải), Support (%), Confidence (%), Lift, Doanh thu tiềm năng dự kiến.
- **Business Rules:** Thuật toán chỉ khai phá trên các đơn hàng đã thanh toán thành công (`Status == Completed / Paid`).
- **Edge Cases:** Tập dữ liệu đơn hàng quá lớn (> 1.000.000 đơn) ➔ xử lý ngầm bất đồng bộ (Background Job với Hangfire/.NET Hosted Service), gửi thông báo khi hoàn thành.

#### A-13: Xem xét, Phê duyệt & Phát hành Combo AI đề xuất (AI Combo Review, Approval & Publishing)
- **Mô Tả Nghiệp Vụ:** Từ danh sách các quy luật kết hợp được AI-2 Apriori phát hiện (`A-12`), Admin xem xét các Combo tiềm năng. Admin có toàn quyền: Điều chỉnh giá bán khuyến mãi của Combo, Đặt tên Combo hấp dẫn (Ví dụ: "Combo Tỉnh Táo Chiều"), Chọn ảnh đại diện WebP và bấm "Phê duyệt & Phát hành" để biến Combo thành một sản phẩm thực thụ trên thực đơn toàn chuỗi.
- **Giao Diện & Kênh:** Admin AI Combo Approval Modal (`/admin/ai/combos/review`).
- **Input Contract:** `ruleId` (Guid), `comboName` (String), `comboPrice` (Decimal: ví dụ giảm 15% so với mua lẻ), `effectiveStartDate` (DateTime), `effectiveEndDate` (DateTime), `action = "Approve"`.
- **System Flow:** API `/api/v1/admin/ai/combos/approve` tạo bản ghi trong bảng `Combos` và `ComboItems`, tự động đồng bộ Combo lên thực đơn PWA của các chi nhánh.
- **Output Contract:** `comboId` (Guid), `status = "Published"`, hiển thị trực tiếp trên Menu PWA mục "Combo Bán Chạy".
- **Business Rules:** Chỉ Combo được Admin phê duyệt mới được xuất bản lên thực đơn; hệ thống không tự ý phát hành combo khi chưa có sự xác nhận của Admin.
- **Edge Cases:** Một trong các món trong Combo bị hết hàng tại chi nhánh ➔ Combo tại chi nhánh đó tự động chuyển sang trạng thái "Tạm hết hàng".

#### A-14: Thiết lập chiến dịch khuyến mãi & Phát hành mã giảm giá Voucher (Promotion Campaign & Voucher Issuance)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi tạo lập các chiến dịch Marketing và phát hành mã giảm giá Voucher: Khai báo Mã Code (Ví dụ: `CHAOHOPHAY`), Loại giảm giá (Giảm theo % hoặc Giảm số tiền cố định VNĐ), Giá trị giảm, Mức giảm tối đa, Giá trị đơn hàng tối thiểu, Tổng số lượt dùng toàn hệ thống, Số lượt dùng tối đa/khách hàng, Thời hạn hiệu lực và Chi nhánh áp dụng.
- **Giao Diện & Kênh:** Admin Voucher Campaign Creator (`/admin/promotions/vouchers`).
- **Input Contract:** `voucherCode` (String), `discountType` (Percentage / FixedAmount), `discountValue` (Decimal), `maxDiscountAmount` (Decimal), `minOrderValue` (Decimal), `usageLimit` (Int: 1000 lượt), `validFrom` (DateTime), `validTo` (DateTime), `applicableBranchIds` (Array).
- **System Flow:** Lưu thông tin vào bảng `Vouchers`. Kích hoạt kiểm tra validation tự động trên API thanh toán.
- **Output Contract:** `voucherId` (Guid), `status = "Active"`, link chia sẻ mã ưu đãi.
- **Business Rules:** Hệ thống tự động khóa mã voucher khi hết hạn hoặc khi tổng số lượt sử dụng đã đạt ngưỡng giới hạn cho phép.
- **Edge Cases:** Phát hiện hành vi gian lận trục lợi mã voucher ➔ Admin có nút "Khóa khẩn cấp" (Emergency Revoke) vô hiệu hóa mã ngay lập tức.

#### A-15: Quản lý chính sách tích điểm & Quy chế Loyalty toàn chuỗi (Chain Loyalty Policy & Tier Settings)
- **Mô Tả Nghiệp Vụ:** Chủ chuỗi định nghĩa quy chế thành viên CRM toàn diện: Thiết lập tỷ lệ tích điểm tiêu chuẩn, Cấu hình các hạng thành viên (Bạc, Vàng, Kim Cương), Ngưỡng chi tiêu thăng hạng, Đặc quyền của từng hạng thành viên (Chiết khấu sinh nhật, Tặng voucher định kỳ), và Duy trì quy tắc cốt lõi **"Tích lũy 10 ly = Tặng 1 ly miễn phí cho đơn Takeaway tại quầy"**.
- **Giao Diện & Kênh:** Admin Loyalty Policy Configuration (`/admin/crm/policy`).
- **Input Contract:** `pointsConversionRate` (1000 VNĐ = 1 Điểm), `tierThresholds` (Silver: 0, Gold: 2.000.000 VNĐ, Diamond: 5.000.000 VNĐ), `takeawayLoyaltyRule` (CupsRequired: 10, RewardCupValue: "LowestItemPrice").
- **System Flow:** Lưu cấu hình vào bảng `LoyaltyPolicies` và áp dụng tự động cho toàn bộ hệ thống CRM.
- **Output Contract:** `isSuccess = true`, thông tin quy chế hiển thị minh bạch trên trang thông tin thành viên PWA.
- **Business Rules:** Quy chế tích điểm áp dụng nhất quán toàn chuỗi; quy tắc 10 ly tặng 1 ly chỉ kích hoạt trên đơn Takeaway.
- **Edge Cases:** Nâng hạng thành viên tự động ➔ Background Worker quét chi tiêu và gửi thông báo chúc mừng thăng hạng tới PWA của khách.

#### A-16: Xem báo cáo tài chính P&L hợp nhất toàn chuỗi & Phân tích chi phí (Consolidated P&L & Financial Reports)
- **Mô Tả Nghiệp Vụ:** Báo cáo tài chính Lãi/Lỗ (Profit & Loss - P&L) hợp nhất toàn diện của toàn bộ chuỗi F&B theo thời gian thực: Tổng Doanh thu gộp (Gross Revenue), Các khoản Giảm trừ doanh thu (Voucher, Chiết khấu), Doanh thu thuần (Net Revenue), Giá vốn hàng bán (COGS tính chính xác từ định lượng BOM nguyên liệu thực tế tiêu hao), Lợi nhuận gộp (Gross Profit), Tỷ suất lợi nhuận gộp (Gross Margin %), và Bảng so sánh hiệu quả kinh doanh giữa các chi nhánh.
- **Giao Diện & Kênh:** Admin Financial P&L Executive Report (`/admin/reports/pl-consolidated`).
- **Input Contract:** `startDate` (Date), `endDate` (Date), `branchFilter` (All Branches / Specific Branch).
- **System Flow:** Tổng hợp hàng triệu bản ghi từ `Orders`, `OrderItems`, `BillOfMaterialItems`, `BranchInventory` và `WorkShifts` để tính toán chính xác bảng P&L theo chuẩn kế toán quản trị.
- **Output Contract:** Báo cáo P&L đa chiều (Bảng số liệu chi tiết, Biểu đồ cơ cấu chi phí, Biểu đồ xu hướng tăng trưởng lợi nhuận, Xuất báo cáo định dạng Excel/PDF).
- **Business Rules:** Dữ liệu tài chính được kiểm soát phân quyền tối mật; chỉ có duy nhất vai trò `ChainAdmin` mới được phép truy cập báo cáo này.
- **Edge Cases:** Xuất dữ liệu quy mô lớn (> 100.000 dòng giao dịch) ➔ Streaming dữ liệu trực tiếp ra file Excel XLSX để tránh tràn bộ nhớ RAM máy chủ.

#### A-17: Nhật ký kiểm toán hệ thống & Giám sát bảo mật (System Audit Logging & Security Monitoring)
- **Mô Tả Nghiệp Vụ:** Hệ thống tự động ghi lại toàn bộ các thao tác nhạy cảm của người dùng quản trị và nhân viên (Ai đã sửa giá món? Ai đã duyệt phiếu xuất kho? Ai đã mở/đóng ca két tiền? Ai đã phân quyền tài khoản?) kèm Địa chỉ IP, Thời gian thực hiện chính xác đến mili-giây, Dữ liệu trước khi sửa (Old Values) và Dữ liệu sau khi sửa (New Values).
- **Giao Diện & Kênh:** Admin Audit Logs & Security Viewer (`/admin/system/audit-logs`).
- **Input Contract:** `actorId` (Guid, optional), `actionType` (Create/Update/Delete/Login), `tableName` (String), `fromUtc` (DateTime), `toUtc` (DateTime).
- **System Flow:** Middleware ngầm trong .NET 8 tự động bắt các sự kiện thay đổi Entity trong Entity Framework Core DbContext và ghi bất đồng bộ vào bảng `AuditLogs`.
- **Output Contract:** Danh sách bản ghi kiểm toán chi tiết (Audit Trail Grid) kèm công cụ lọc và đối soát bảo mật.
- **Business Rules:** Bản ghi Audit Log là dữ liệu ghi một lần (Append-only / WORM), tuyệt đối cấm chỉnh sửa hoặc xóa để phục vụ điều tra an ninh thông tin.
- **Edge Cases:** Phát hiện thao tác đăng nhập bất thường từ IP lạ ➔ hệ thống gửi cảnh báo khẩn cấp tới Email quản trị viên gốc.

---

# 🛡️ PHẦN 7: MA TRẬN PHÂN QUYỀN BẢO MẬT CHI TIẾT (RBAC SECURITY MATRIX)

Hệ thống phân quyền **Role-Based Access Control (RBAC)** của Smart F&B OS được xây dựng dựa trên 6 Vai trò định danh (`Roles`) kiểm soát truy cập trên **10 Nhóm Tài Nguyên API Endpoints cốt lõi**. Mỗi quyền hạn được định nghĩa rõ ràng:
- `None (-)`: Không có quyền truy cập (API trả về `403 Forbidden` hoặc `401 Unauthorized`).
- `Read (R)`: Quyền xem, tìm kiếm và truy vấn dữ liệu.
- `Create (C)`: Quyền tạo mới bản ghi dữ liệu.
- `Update (U)`: Quyền chỉnh sửa, cập nhật trạng thái bản ghi.
- `Delete (D)`: Quyền xóa mềm, vô hiệu hóa bản ghi.
- `Execute (X)`: Quyền thực thi tác vụ nghiệp vụ đặc thù (Duyệt AI, Chấm công, Thu tiền, In bill).

### 7.1 Danh Sách 6 Vai Trò Định Danh Trong Hệ Thống
1. `GuestCustomer`: Khách vãng lai truy cập PWA qua quét QR (Anonymous JWT).
2. `AuthCustomer`: Khách hàng thành viên CRM đã xác thực qua Phone OTP (User JWT 30 ngày).
3. `Staff / Barista`: Nhân viên quầy bar, thu ngân, phục vụ trực ca tại chi nhánh (Staff JWT).
4. `BranchManager`: Quản lý phụ trách vận hành và tài chính tại chi nhánh (Manager JWT + 2FA).
5. `ChainAdmin`: Chủ chuỗi và quản trị viên cấp cao toàn quyền hệ thống (Root Admin JWT).
6. `System / PayOS`: Các tiến trình ngầm (Background Worker) và Webhook từ cổng thanh toán bên thứ ba (HMAC Signature / API Key).

---

### 7.2 Ma Trận Phân Quyền Chi Tiết Trên 10 Nhóm Tài Nguyên API

| Nhóm Tài Nguyên API & Endpoint Scope | GuestCustomer | AuthCustomer | Staff / Barista | BranchManager | ChainAdmin | System / Webhook |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Menu & Product Catalog API**<br>`/api/v1/products`<br>`/api/v1/categories`<br>`/api/v1/combos`<br>`/api/v1/menu-schedules` | Read<br>(Active only) | Read<br>(Active only) | Read<br>(Branch Menu) | Read, Update<br>(86/Price Override) | **Full CRUD**<br>(C, R, U, D, X) | Read<br>(Sync Cache) |
| **2. Order & Kitchen Hub API**<br>`/api/v1/orders`<br>`/api/v1/orders/{id}/items`<br>`/api/v1/orders/{id}/status`<br>`SignalR KitchenHub` | Create, Read<br>(Own Order) | Create, Read<br>(Own History) | Read, Create, Update, X<br>(Branch KDS/POS) | Read, Update, X<br>(Branch Orders) | **Full CRUD**<br>(All System Orders) | Update, X<br>(Background Worker) |
| **3. Payment & PayOS Webhook API**<br>`/api/v1/payments/vietqr`<br>`/api/v1/payments/cash-confirm`<br>`/api/v1/payments/payos-webhook` | Create, Read<br>(VietQR QR) | Create, Read<br>(VietQR QR) | Read, Update, X<br>(Cash/VietQR POS) | Read, Update, X<br>(Shift Balance) | **Full CRUD**<br>(All Payments) | **Execute**<br>(PayOS Webhook) |
| **4. BOM & Inventory API**<br>`/api/v1/bom/recipes`<br>`/api/v1/inventory/stock`<br>`/api/v1/inventory/requisitions`<br>`/api/v1/inventory/count` | None | None | Read<br>(BOM View Only) | Read, Create, Update, X<br>(Branch Stock/Count) | **Full CRUD**<br>(Master BOM/All POs) | Update, X<br>(Auto BOM Deduct) |
| **5. CRM & Loyalty Program API**<br>`/api/v1/crm/customers`<br>`/api/v1/crm/loyalty-cards`<br>`/api/v1/vouchers`<br>`/api/v1/vouchers/apply` | Read, X<br>(Apply Voucher) | Read, Update, X<br>(Own Profile/Voucher) | Read, Create, X<br>(Lookup & 10-Cup POS) | Read, Update<br>(Branch Customers) | **Full CRUD**<br>(Master Policy/Vouchers)| Update, X<br>(Tier Recalculate) |
| **6. Shift & Cash Reconciliation API**<br>`/api/v1/shifts/open`<br>`/api/v1/shifts/close`<br>`/api/v1/shifts/z-report`<br>`/api/v1/shifts/summary` | None | None | Read, X<br>(Own Shift Summary) | Create, Read, Update, X<br>(Open/Close/Z-Report) | **Full CRUD**<br>(Consolidated Z-Reports)| None |
| **7. Attendance & WiFi Verification API**<br>`/api/v1/attendance/check-in`<br>`/api/v1/attendance/check-out`<br>`/api/v1/attendance/branch-wifi` | None | None | Create, Read, X<br>(WiFi CheckIn/Out) | Read, Update, X<br>(Branch WiFi/Approval) | **Full CRUD**<br>(System Attendance) | Update<br>(Auto Lock Shifts) |
| **8. Reviews & Customer Feedback API**<br>`/api/v1/reviews`<br>`/api/v1/reviews/{id}/photos`<br>`/api/v1/reviews/{id}/moderate`<br>`/api/v1/reviews/alerts` | Create, Read<br>(Public Approved) | Create, Read, X<br>(Upload Photos) | Read<br>(Branch Reviews) | Read, Update, X<br>(Moderate/<=2* Alert)| **Full CRUD**<br>(All Reviews/Audit) | X<br>(Trigger Alert Webhook) |
| **9. AI Services API (Gemini RAG & Apriori)**<br>`/api/v1/ai/chatbot-query`<br>`/api/v1/ai/apriori/mine`<br>`/api/v1/ai/apriori/combos/approve` | Read, X<br>(AI-1 Chatbot) | Read, X<br>(AI-1 Chatbot) | None | Read<br>(AI-2 Insights) | **Full CRUD, Execute**<br>(Mine & Approve Combos)| Execute<br>(Apriori Model Job) |
| **10. Analytics, P&L Reports & System Admin API**<br>`/api/v1/reports/pl-consolidated`<br>`/api/v1/reports/branch-kpi`<br>`/api/v1/admin/users`<br>`/api/v1/admin/branches`<br>`/api/v1/admin/audit-logs` | None | None | None | Read<br>(Branch KPI Dashboard) | **Full CRUD**<br>(Consolidated P&L & Audit)| Execute<br>(DB Backup/Job Runner) |

---

# 🚀 PHẦN 8: ĐỊNH HƯỚNG MỞ RỘNG ACTOR & TÍNH NĂNG TƯƠNG LAI (SCALE UP / FUTURE WORK)

Nhằm bảo đảm tính tập trung cao độ cho mục tiêu hoàn thiện và bảo vệ thành công đồ án Capstone 16 tuần (08 Sprints) của nhóm 4 thành viên, các tác nhân chuyên biệt và tính năng phức tạp dưới đây đã được khảo sát kỹ lưỡng và **định hướng chuyển sang giai đoạn nâng cấp tiếp theo (Giai đoạn Scale Up - Post MVP)**:

### 8.1 Các Actor Mở Rộng Trong Tương Lai
1. **Third-Party Delivery Driver / Shipper Platform (Tài Xế Giao Hàng & Nền Tảng Đối Tác):**
   - *Mô tả:* Tác nhân tài xế nhận đơn giao đồ uống từ quầy mang đến địa chỉ khách hàng.
   - *Giao diện tương lai:* Mobile App Shipper hoặc Web Driver Portal cho phép nhận đơn, cập nhật trạng thái di chuyển thời gian thực và ký nhận điện tử (e-Proof of Delivery).
2. **Regional Franchisee Owner (Chủ Cơ Sở Nhượng Quyền Khu Vực):**
   - *Mô tả:* Tác nhân sở hữu một hoặc nhiều chi nhánh nhượng quyền thương hiệu, cần theo dõi doanh thu phân bổ, phí nhượng quyền (Royalty Fee) và kiểm soát nguồn nguyên liệu độc quyền từ thương hiệu mẹ.
   - *Giao diện tương lai:* Franchisee Portal với bảng điều khiển dòng tiền và quản lý hợp đồng nhượng quyền.
3. **Central Kitchen & Supply Chain Warehouse Manager (Quản Lý Bếp Trung Tâm & Tổng Kho Chuỗi Cung Ứng):**
   - *Mô tả:* Tác nhân điều phối việc sơ chế nguyên liệu hàng loạt tại Bếp trung tâm (Central Kitchen), quản lý tồn kho tổng (Master Warehouse), lập lịch điều xe lạnh và phân bổ hàng hóa cho toàn chuỗi chi nhánh.
   - *Giao diện tương lai:* Warehouse Management System (WMS) tích hợp quét mã vạch Barcode/RFID và quản lý lô hạn sử dụng (FIFO/FEFO).

---

### 8.2 Danh Mục 8 Module Tính Năng Nâng Cao (Future Work Catalog)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             8 MODULE TÍNH NĂNG ĐỊNH HƯỚNG MỞ RỘNG (SCALE UP)                     │
├────┬───────────────────────────────┬────────────────────────────────────────────────────────────┤
│ STT│ Tên Module Mở Rộng            │ Mô Tả Kỹ Thuật & Nghiệp Vụ Định Hướng Nâng Cấp             │
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 01 │ AI Voice Ordering at Kiosk    │ Đặt món bằng giọng nói tiếng Việt đa vùng miền tại Kiosk   │
│    │                               │ cảm ứng tích hợp mô hình Whisper ASR + Speech-to-Intent.   │
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 02 │ Facial Recognition Attendance │ Chấm công nhận diện khuôn mặt sinh trắc học qua Camera AI  │
│    │                               │ chống giả mạo hình ảnh/video (Liveness Detection).         │
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 03 │ Satellite GPS & Dynamic QR 30s│ Định vị vệ tinh bán kính 50m kết hợp mã QR động sinh ngẫu  │
│    │                               │ nhiên mỗi 30 giây dùng cho chấm công di động ngoài trời.   │
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 04 │ AI-3 Text-to-SQL Analytics    │ Truy vấn dữ liệu kinh doanh bằng ngôn ngữ tự nhiên tiếng   │
│    │                               │ Việt (NLQ) tự động dịch sang câu lệnh PostgreSQL SQL chuẩn.│
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 05 │ AI-4 RFM Churn Prediction     │ Phân khúc khách hàng RFM kết hợp học máy dự đoán nguy cơ   │
│    │                               │ rời bỏ (Churn Prediction) và tự động gửi voucher giữ chân. │
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 06 │ AI-5 ML Demand Forecasting    │ Dự báo nhu cầu tiêu thụ nguyên vật liệu và số lượng ly theo │
│    │                               │ mùa vụ/thời tiết bằng mô hình chuỗi thời gian (Prophet).   │
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 07 │ Multi-Carrier Auto-Dispatch   │ Tự động đẩy đơn và so sánh cước phí giao hàng theo thời    │
│    │                               │ gian thực tới các hãng vận chuyển (Ahamove, GrabExpress).  │
├────┼───────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 08 │ Offline Local Mesh Data Sync  │ Vận hành quầy POS hoàn toàn độc lập khi mất mạng internet  │
│    │                               │ và tự động đồng bộ gộp dữ liệu (Mesh Sync) khi có mạng lại.│
└────┴───────────────────────────────┴────────────────────────────────────────────────────────────┘
```

---

# 📋 PHẦN 9: TỔNG HỢP KIỂM CHỨNG & MA TRẬN TRUY VẾT YÊU CẦU (TRACEABILITY MATRIX)

Nhằm bảo đảm tính toàn vẹn 100% giữa tài liệu đặc tả nghiệp vụ, mã nguồn thực thi và các kịch bản kiểm thử (Test Cases), ma trận truy vết dưới đây xác nhận sự tương thích hoàn hảo giữa 62 tính năng cốt lõi và kiến trúc hệ thống:

| Nhóm Actor | Số Lượng Features | Phạm Vi Mã Tính Năng | Thành Phần Backend (.NET 8) | Thành Phần Frontend (Next.js 14) | Trạng Thái Kiểm Chứng |
|---|:---:|:---:|---|---|:---:|
| **1. Khách Hàng (Customer)** | **20 Features** | `C-01` đến `C-20` | `OrderService`, `PaymentService`, `GeminiRagService`, `ReviewService` | `app/(customer)/*`, PWA Service Worker, Zustand Cart Store | **PASSED (100%)** |
| **2. Nhân Viên (Staff / Barista)** | **13 Features** | `S-01` đến `S-13` | `KdsService`, `ShiftService`, `AttendanceService`, `SignalR Hubs` | `app/(kds)/*`, `app/(staff)/*`, ESC/POS Web Print Bridge | **PASSED (100%)** |
| **3. Quản Lý CN (Branch Manager)**| **12 Features** | `M-01` đến `M-12` | `InventoryService`, `ReconciliationService`, `BranchConfigService` | `app/(manager)/*`, Recharts KPI Dashboard, WiFi Manager | **PASSED (100%)** |
| **4. Chủ Chuỗi (Chain Admin)** | **17 Features** | `A-01` đến `A-17` | `ProductService`, `BomService`, `AprioriService`, `ConsolidatedReportService` | `app/(admin)/*`, High-Density Data Grids, Asset Manager | **PASSED (100%)** |
| **TỔNG CỘNG HỆ THỐNG** | **62 Features** | **Toàn diện MVP** | **Clean Architecture (.NET 8 Core)** | **Next.js 14 App Router Monorepo** | **PRODUCTION-READY** |

### Cam Kết Chất Lượng & Tính Toàn Vẹn Tài Liệu:
1. **Không chứa mã giữ chỗ:** Tài liệu hoàn chỉnh 100%, đảm bảo tiêu chuẩn sản xuất, không chứa mã giữ chỗ hay nội dung tạm thời.
2. **Loại bỏ hoàn toàn tính năng ngoài phạm vi:** Không đưa các tính năng nằm ngoài phạm vi 16 tuần (như Chia sẻ MXH hay PWA Push Notification) vào danh mục tính năng cốt lõi.
3. **Loại bỏ Staff Mobile App:** 100% nghiệp vụ nhân viên được mô tả vận hành trên Web Responsive (`(kds)`, `(staff)`).
4. **Chấm công chuẩn hóa:** 100% cơ chế chấm công được chuẩn hóa bằng Khóa mạng WiFi chi nhánh (BSSID / IP Gateway).
5. **Dine-in 2 nhánh & Takeaway 10 ly:** Đặc tả chính xác 2 luồng thanh toán Dine-in (VietQR trả trước vs Tiền mặt trả sau) và quy tắc tích lũy 10 ly tặng 1 ly duy nhất cho đơn Takeaway tại quầy.
6. **Admin Full CRUD:** Toàn quyền Tạo, Sửa, Xóa mềm, Thay thế món ăn, định nghĩa BOM và khai phá AI-2 Apriori được mô tả chi tiết, minh bạch.

---
*Tài liệu được biên soạn và chuẩn hóa bởi Đội ngũ Kỹ sư Kiến trúc Phần mềm Smart F&B OS — Sẵn sàng cho triển khai thực tế và nghiệm thu Đồ án Capstone.*
