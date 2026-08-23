# -*- coding: utf-8 -*-
import os

part1 = '''# 👥 BẢN ĐẶC TẢ ACTORS, MA TRẬN PHÂN QUYỀN RBAC & DANH MỤC TÍNH NĂNG TOÀN DIỆN
## Smart F&B Operating System — Nền Tảng Quản Trị & Vận Hành F&B Đa Chi Nhánh Tích Hợp Đặt Món QR & Trí Tuệ Nhân Tạo

> **Tài liệu:** Bản đặc tả kỹ thuật chi tiết về 4 Nhóm Tác Nhân (Actor Profiles), Ma trận kiểm soát truy cập phân quyền theo vai trò (Role-Based Access Control - RBAC) trên 10 nhóm tài nguyên API, và Danh mục 64 Tính năng cốt lõi (Core MVP Feature Catalog).  
> **Phiên bản:** v2.5.0-Production-Ready  
> **Nguồn sự thật chuẩn hóa:** Smart_FB_OS_Revised_4members.docx (Kết hợp chỉ đạo kỹ thuật tại ORIGINAL_REQUEST.md)  
> **Quy mô dự án:** Đồ án Capstone 16 tuần (08 Sprints) — Nhóm 4 Kỹ sư Phần mềm (2 Backend + 2 Frontend).  
> **Nền tảng công nghệ:** .NET 8 Clean Architecture (Backend) + Next.js 14 App Router Monorepo (Frontend) + PostgreSQL 16 + Redis 7 + SignalR Hubs + Google Gemini 1.5 Flash.  
> **Cam kết chất lượng:** Hoàn chỉnh 100%, tuyệt đối không sử dụng mã giữ chỗ (TODO, TBD, /* rest of code */), không ngụy tạo dữ liệu.

---

# 📚 MỤC LỤC ĐẶC TẢ

| Phần | Tiêu Đề Chi Tiết | Mô Tả Trọng Tâm |
|:---:|---|---|
| **PHẦN 1** | [Tổng Quan 4 Nhóm Actor & Thiết Bị Truy Cập Chuẩn Hóa](#-phần-1-tổng-quan-4-nhóm-actor--thiết-bị-truy-cập-chuẩn-hóa) | Định vị 4 Actor, thiết bị truy cập, 5 nguyên tắc kiến trúc bất biến. |
| **PHẦN 2** | [Sơ Đồ Tương Tác Tổng Thể Actor (Actor Interaction Architecture)](#-phần-2-sơ-đồ-tương-tác-tổng-thể-actor-actor-interaction-architecture) | Sơ đồ Mermaid toàn diện biểu diễn luồng tương tác giữa 4 Actor. |
| **PHẦN 3** | [Đặc Tả Chi Tiết Actor 1: Khách Hàng (Customer — 22 Features)](#-phần-3-đặc-tả-chi-tiết-actor-1-khách-hàng-customer--22-features) | Danh mục C-01 đến C-22, 2 nhánh Dine-in, Delivery 20k, AI-1, Review. |
| **PHẦN 4** | [Đặc Tả Chi Tiết Actor 2: Nhân Viên Vận Hành Quầy (Staff / Barista — 13 Features)](#-phần-4-đặc-tả-chi-tiết-actor-2-nhân-viên-vận-hành-quầy-staff--barista--13-features) | Danh mục S-01 đến S-13, KDS SignalR, Web POS Takeaway, CRM 10 ly, WiFi. |
| **PHẦN 5** | [Đặc Tả Chi Tiết Actor 3: Quản Lý Chi Nhánh (Branch Manager — 12 Features)](#-phần-5-đặc-tả-chi-tiết-actor-3-quản-lý-chi-nhánh-branch-manager--12-features) | Danh mục M-01 đến M-12, Mở/kết ca két tiền, Kho BOM, WiFi config, Review alert. |
| **PHẦN 6** | [Đặc Tả Chi Tiết Actor 4: Chủ Chuỗi / Quản Trị Viên (Chain Admin — 17 Features)](#-phần-6-đặc-tả-chi-tiết-actor-4-chủ-chuỗi--quản-trị-viên-chain-admin--17-features) | Danh mục A-01 đến A-17, Full CRUD Món/Combo/Ảnh, Giá vùng, AI-2 Apriori, P&L. |
| **PHẦN 7** | [Ma Trận Phân Quyền Bảo Mật Chi Tiết (RBAC Security Matrix)](#-phần-7-ma-trận-phân-quyền-bảo-mật-chi-tiết-rbac-security-matrix) | Ma trận quyền hạn 6 vai trò trên 10 nhóm Endpoint API tài nguyên. |
| **PHẦN 8** | [Định Hướng Mở Rộng Actor & Tính Năng Tương Lai (Scale Up / Future Work)](#-phần-8-định-hướng-mở-rộng-actor--tính-năng-tương-lai-scale-up--future-work) | Các Actor và tính năng nâng cao chuyển sang giai đoạn phát triển tiếp theo. |
| **PHẦN 9** | [Tổng Hợp Kiểm Chứng & Ma Trận Truy Vết Yêu Cầu (Traceability Matrix)](#-phần-9-tổng-hợp-kiểm-chứng--ma-trận-truy-vết-yêu-cầu-traceability-matrix) | Đối soát tính toàn vẹn giữa nghiệp vụ thực tế và tài liệu đặc tả. |

---

# 👥 PHẦN 1: TỔNG QUAN 4 NHÓM ACTOR & THIẾT BỊ TRUY CẬP CHUẨN HÓA

Hệ thống **Smart F&B OS** được thiết kế theo mô hình phân quyền chặt chẽ dựa trên vai trò (Role-Based Access Control - RBAC), phân định ranh giới rõ ràng giữa **4 nhóm tác nhân (Actors)**. Kiến trúc bảo đảm tính tách biệt tuyệt đối giữa giao diện khách hàng không cần cài đặt (PWA), giao diện vận hành quầy phản ứng nhanh (Web POS & KDS), giao diện quản trị chi nhánh (Manager Portal) và giao diện điều hành chuỗi tập trung (Admin Executive Portal).

`
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               4 NHÓM ACTOR CHÍNH TRONG SMART F&B OS                              │
├───────────────────────┬──────────────────────────────────┬───────────────────────────────────────┤
│ Actor Profile         │ Thiết Bị & Giao Diện Sử Dụng     │ Trách Nhiệm Vận Hành Chính            │
├───────────────────────┼──────────────────────────────────┼───────────────────────────────────────┤
│ 👤 1. Khách Hàng      │ Trình duyệt di động (PWA Web)    │ Quét QR đặt món tại bàn (Dine-in),    │
│    (Customer)         │ Safari, Chrome trên iOS/Android  │ quét QR Delivery đặt tận nhà, trả     │
│                       │ (Route: (customer))            │ trước VietQR / trả tiền mặt, chat AI. │
├───────────────────────┼──────────────────────────────────┼───────────────────────────────────────┤
│ 🧋 2. Nhân Viên Quầy   │ Smart TV / Tablet Bếp (KDS),     │ Nhận đơn KDS thời gian thực, pha chế  │
│    (Staff / Barista)  │ PC / Tablet Cảm ứng Quầy Thu ngân│ theo BOM, thao tác POS Takeaway, tra  │
│                       │ (Routes: (kds), (staff))     │ CRM 10 ly tặng 1, thu tiền, chấm công.│
├───────────────────────┼──────────────────────────────────┼───────────────────────────────────────┤
│ 🏪 3. Quản Lý CN      │ Laptop, Máy tính bảng (Tablet),  │ Mở/kết ca đếm két tiền, đối soát Z-   │
│    (Branch Manager)   │ Desktop tại phòng quản lý        │ Report, lập lịch phân ca, quản lý kho │
│                       │ (Route: (manager))             │ BOM, cấu hình WiFi, duyệt review ảnh. │
├───────────────────────┼──────────────────────────────────┼───────────────────────────────────────┤
│ 👑 4. Chủ Chuỗi       │ Máy tính để bàn (Desktop),       │ Toàn quyền CRUD Menu, BOM, Nhóm giá,  │
│    (Chain Admin)      │ Laptop điều hành cấp cao         │ duyệt AI-2 Combo Apriori, xem P&L hợp │
│                       │ (Route: (admin))               │ nhất, phân quyền RBAC & audit log.    │
└───────────────────────┴──────────────────────────────────┴───────────────────────────────────────┘
`

### 1.1 Bảng Phân Định Actor Profiles & Môi Trường Thực Thi

| Thuộc Tính | Customer (Khách Hàng) | Staff / Barista (Nhân Viên) | Branch Manager (Quản Lý CN) | Chain Admin (Chủ Chuỗi) |
|---|---|---|---|---|
| **Mã Định Danh Role** | GuestCustomer, AuthCustomer | BaristaStaff, CashierStaff, ServiceStaff | BranchManager | ChainAdmin |
| **Phương Thức Xác Thực** | Anonymous Token / Phone OTP / JWT 30 ngày | JWT Token (Mã NV + Mật khẩu ca) | JWT Token (Email + Password + 2FA) | JWT Token (Root Admin Credentials) |
| **Phạm Vi Dữ Liệu (Scope)** | Cá nhân (Own Data) | Chi nhánh công tác (Branch Data) | Chi nhánh quản lý (Branch Data) | Toàn hệ thống chuỗi (All System Data) |
| **Giao Thức Thời Gian Thực** | SignalR OrderHub | SignalR KitchenHub, OrderHub | SignalR NotificationHub, KitchenHub | SignalR NotificationHub |
| **Công Nghệ Giao Diện** | Next.js 14 PWA Mobile-First | Next.js 14 Web KDS & Staff POS | Next.js 14 Manager Dashboard | Next.js 14 High-Density Admin Grid |

### 1.2 Năm Nguyên Tắc Kiến Trúc & Vận Hành Bất Biến

1. **Loại bỏ hoàn toàn Staff Mobile App (100% Web Responsive):** Không duy trì bất kỳ ứng dụng di động native/hybrid nào cho nhân viên phục vụ. Toàn bộ thao tác nghiệp vụ của nhân viên (xem KDS, tạo đơn Takeaway, kiểm tra sơ đồ bàn, nhận chuông gọi phục vụ, xác nhận thanh toán) được vận hành mượt mà trên nền tảng Web Responsive ((kds), (staff)).
2. **Chấm công Khóa Mạng WiFi (WiFi-Locked Attendance):** Xóa bỏ hoàn toàn định vị vệ tinh GPS 50m và mã QR động 30 giây. Nhân viên chỉ có thể chấm công vào ca/ra ca thành công khi: (a) Đang kết nối trực tiếp vào mạng WiFi chi nhánh (kiểm tra BSSID Access Point / IP Gateway Subnet), và (b) Nhập đúng Mã số nhân viên hợp lệ.
3. **Dine-In hỗ trợ 2 Nhánh thanh toán độc lập:** 
   - *Nhánh A (VietQR trả trước):* Khách chọn VietQR ➔ Quét mã chuyển khoản ➔ PayOS Webhook xác nhận Paid ➔ Bếp KDS mới nhận đơn.
   - *Nhánh B (Tiền mặt trả sau):* Khách chọn Tiền mặt ➔ Đơn vào bếp ngay với trạng thái Confirmed ➔ Barista pha chế ➔ Nhân viên bưng món ra bàn kèm Hóa đơn có in sẵn mã VietQR ➔ Khách trả tiền mặt HOẶC quét VietQR trên hóa đơn ➔ Nhân viên bấm xác nhận thanh toán trên Web Staff.
4. **Takeaway POS qua Nhân viên & Tích 10 Ly chỉ áp dụng Mang Về:** Khách mua mang đi không quét QR. Nhân viên thu ngân thao tác trên Web POS Quầy, tra cứu SĐT CRM. Chương trình ưu đãi ** Tích lũy 10 ly = Tặng 1 ly miễn phí CHỈ ÁP DỤNG DUY NHẤT CHO ĐƠN TAKEAWAY** (Không áp dụng cho Dine-in, không áp dụng cho Delivery). Khách thanh toán sau khi nhận đồ uống.
5. **Admin Full CRUD & Toàn quyền kiểm soát hệ thống:** Chủ chuỗi sở hữu toàn quyền Tạo mới, Sửa, Xóa mềm, Thay thế món ăn (Product Full CRUD), định nghĩa BOM chi tiết, quản lý danh mục & thứ tự hiển thị, lên lịch thực đơn theo mùa vụ, phê duyệt Combo AI-2, và giám sát báo cáo P&L hợp nhất.
'''

with open('d:/Idea_DoAn/.agents/worker_actor_rbac/generate_actor_doc.py', 'w', encoding='utf-8') as f:
    f.write(part1)
print('Part 1 written')
