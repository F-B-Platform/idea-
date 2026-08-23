# BÁO CÁO ĐÁNH GIÁ KỸ THUẬT & KIỂM CHỨNG TÍNH NHẤT QUÁN 5 TÀI LIỆU ĐẶC TẢ
## Smart F&B Operating System — Technical & Architectural Review Report

- **Reviewer**: `reviewer_5docs_technical` (Teamwork Technical Reviewer & Adversarial Critic)
- **Working Directory**: `d:\Idea_DoAn\.agents\reviewer_5docs_technical\`
- **Target Directory**: `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\`
- **Timestamp**: 2026-08-22T15:30:00Z
- **Verdict**: **REQUEST_CHANGES** (Yêu cầu đồng bộ hóa 3 điểm lệch kiến trúc & hợp đồng giữa 5 tài liệu)

---

## 1. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY OF VERDICT)

Qua quá trình rà soát toàn diện, đối chiếu từng dòng mã đặc tả, ma trận phân quyền, lược đồ cơ sở dữ liệu, máy trạng thái đơn hàng và kiến trúc thời gian thực trên toàn bộ **5 tài liệu đặc tả gốc**:
1. `Smart_FB_Operating_System.md` (66 KB)
2. `Actor_Phan_Quyen_Chuc_Nang.md` (116 KB)
3. `Workflow_Quy_Trinh_Nghiep_Vu.md` (122 KB)
4. `Tong_Quan_Kien_Truc_He_Thong.md` (57 KB)
5. `Tom_Tat_1_Trang_Executive_Summary.md` (12 KB)

### Đánh Giá Chung:
- **Chất lượng kỹ thuật tổng thể:** **RẤT CAO (9.2/10)**. Tài liệu được biên soạn cực kỳ chi tiết, công phu, chuẩn hóa mô hình .NET 8 Clean Architecture + Next.js 14 App Router, không có mã giữ chỗ (`Zero Placeholders`), giải quyết triệt để 4 kênh bán hàng (`DineIn_PrePay`, `DineIn_PostPay`, `TakeAway`, `Delivery`), khóa mạng WiFi chấm công, KDS SignalR, 2 module AI thực thi (Gemini 1.5 Flash RAG và Apriori Combo Mining).
- **Lý do đưa ra phán quyết `REQUEST_CHANGES`:** Phát hiện **02 lỗi lệch chuẩn Major** và **01 lỗi lệch chuẩn Minor** giữa các tài liệu liên quan đến: (1) Phân bổ số lượng tính năng trong bản Tóm tắt 1 trang, (2) Danh mục 4 Hubs SignalR trong tài liệu Workflow so với Kiến trúc hệ thống, và (3) Số lượng thực thể database trong tài liệu Tổng quan OS. Cần hiệu chỉnh đồng bộ để bảo đảm **100% Single Source of Truth**.

---

## 2. MA TRẬN ĐỐI CHIẾU 7 TIÊU CHÍ KỸ THUẬT CỐT LÕI

| Tiêu Chí Đánh Giá | Yêu Cầu Kỹ Thuật Chuẩn | Hiện Trạng Đối Chiếu Trên 5 File | Đánh Giá Tính Nhất Quán |
|---|---|---|:---:|
| **1. Feature Inventory (64 Features)** | Đúng 64 Core MVP:<br>• 22 Customer (`C-01`..`C-22`)<br>• 13 Staff (`S-01`..`S-13`)<br>• 12 Manager (`M-01`..`M-12`)<br>• 17 Admin (`A-01`..`A-17`) | • `Actor_Phan_Quyen_Chuc_Nang.md`: 22 / 13 / 12 / 17 = 64 (Chuẩn).<br>• `Smart_FB_Operating_System.md`: 22 / 13 / 12 / 17 = 64 (Chuẩn).<br>• `Workflow_Quy_Trinh_Nghiep_Vu.md`: 17 Workflows ánh xạ 64 features (Chuẩn).<br>• `Tom_Tat_1_Trang_Executive_Summary.md` (Dòng 95): Ghi `22 CUS`, `12 STF`, `12 MGR`, `18 ADM`. | 🔴 **LỆCH PHÂN BỔ**<br>(Dòng 95 File Tóm Tắt) |
| **2. RBAC Permissions Matrix** | Ma trận 10 nhóm tài nguyên API trên 6 vai trò định danh (Guest, Auth, Staff, Manager, Admin, System). | • `Actor_Phan_Quyen_Chuc_Nang.md` (Phần 7): Đặc tả đầy đủ 10 nhóm tài nguyên và 6 roles, phân định rõ CRUDX.<br>• `Tong_Quan_Kien_Truc_He_Thong.md`: Thiết kế JWT Claims-based RBAC .NET 8 hoàn toàn tương thích. | 🟢 **PASSED (100%)** |
| **3. PostgreSQL Schema (25 Entities)** | 25 Thực thể 3NF chứa:<br>• `OrderType` (`DineIn`/`TakeAway`/`Delivery`)<br>• `delivery_address`, `delivery_fee`<br>• `BranchWifiConfigs`<br>• `BOM` (Recipes, Ingredients)<br>• `Loyalty` (10 ly Takeaway) | • `Tong_Quan_Kien_Truc_He_Thong.md` (Phần 6): Chuẩn hóa đúng 25 bảng 3NF trong Mermaid ERD.<br>• `Smart_FB_Operating_System.md` (Mục 7.2): Tiêu đề ghi "25 Thực Thể" nhưng danh sách số thứ tự liệt kê đến 26 mục (bao gồm `Combos`, `ComboItems`, tách riêng `InventoryStocks`, `InventoryTransactions`). | 🟡 **LỆCH ĐẾM & TÊN BẢNG**<br>(Mục 7.2 Smart FB OS) |
| **4. SignalR Real-Time Architecture** | 4 Hubs cốt lõi:<br>• `OrderHub` (`/hubs/orders`)<br>• `KitchenHub` (`/hubs/kitchen`)<br>• `PaymentHub` (`/hubs/payments`)<br>• `NotificationHub` (`/hubs/notifications`) | • `Tong_Quan_Kien_Truc_He_Thong.md` (Mục 5.2): Chuẩn hóa 4 Hubs trên.<br>• `Smart_FB_Operating_System.md` (Mục 7): Sơ đồ kiến trúc chứa đúng 4 Hubs trên.<br>• `Tom_Tat_1_Trang_Executive_Summary.md`: Ghi nhận đúng 4 Hubs trên.<br>• `Workflow_Quy_Trinh_Nghiep_Vu.md` (Mục 6.3, dòng 1593-1603): Sơ đồ và Bảng lại đổi thành: `KitchenHub`, `NotificationHub` (`/hubs/notify`), `MenuHub` (`/hubs/menu`), `ManagerHub` (`/hubs/manager`).<br>• `Actor_Phan_Quyen_Chuc_Nang.md` (Dòng 421): Đề cập `TableHub`. | 🔴 **LỆCH KIẾN TRÚC HUBS**<br>(Workflow Mục 6.3 & Actor Dòng 421) |
| **5. Order State Machine (4 Channels)** | Máy trạng thái riêng biệt cho 4 kênh:<br>• `DineIn_PrePay`<br>• `DineIn_PostPay`<br>• `TakeAway`<br>• `Delivery` | • `Workflow_Quy_Trinh_Nghiep_Vu.md` (Chương 1-5): Đặc tả cực kỳ chi tiết, mạch lạc, sơ đồ Sequence rõ ràng, 10 Edge cases xử lý toàn diện.<br>• Timeout 10 phút hủy đơn VietQR, In bill VietQR động tại bàn cho đơn Cash, Khóa 100% VietQR cho Delivery, Tích 10 ly Takeaway quầy. | 🟢 **PASSED (100%)** |
| **6. Monorepo Structure** | .NET 8 Clean Architecture (Domain, Application, Infrastructure, WebApi) + Next.js 14 App Router (5 route groups). | • Phân bổ 5 route groups `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)` đồng nhất.<br>• Bỏ hoàn toàn Staff Mobile App, chuyển 100% Web Responsive.<br>• Clean Architecture CQRS MediatR, FluentValidation, EF Core 8, Redis 7 Cache-aside. | 🟢 **PASSED (100%)** |
| **7. Zero Placeholders & Hygiene** | 100% nội dung hoàn chỉnh, không có `TODO`, `TBD`, mã giả hay chú thích giữ chỗ. | • Quét toàn diện regex: 0 code placeholders.<br>• Mọi trường dữ liệu, tham số, endpoint, mã lỗi HTTP đều khai báo tường minh. | 🟢 **PASSED (100%)** |

---

## 3. CHI TIẾT CÁC ĐIỂM CẦN KHẮC PHỤC (DEFECT DETAILS & CHANGE REQUESTS)

### 🔴 Finding 1 (Major) — Lệch Phân Bổ Feature Inventory trong Tóm Tắt Dự Án
- **Vị trí:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tom_Tat_1_Trang_Executive_Summary.md`, Dòng 95.
- **Hiện trạng:**
  ```markdown
  95: - **Quy mô bàn giao:** **64 Tính năng cốt lõi** phân bổ cho 4 nhóm Actor (22 Khách hàng `C-01`–`C-22`, 12 Nhân viên `S-01`–`S-12`, 12 Quản lý `M-01`–`M-12`, 18 Chủ chuỗi `A-01`–`A-18`).
  ```
- **Vấn đề:** Phân bổ ghi `12 Nhân viên (S-01–S-12)` và `18 Chủ chuỗi (A-01–A-18)`. Trong khi Source of Truth và 2 tài liệu lớn (`Actor_Phan_Quyen_Chuc_Nang.md` và `Smart_FB_Operating_System.md`) đều định nghĩa chuẩn là **13 Nhân viên (`S-01`–`S-13`)** và **17 Chủ chuỗi (`A-01`–`A-17`)**.
- **Yêu cầu sửa đổi (Fix Suggestion):**
  Sửa lại Dòng 95 thành:
  ```markdown
  - **Quy mô bàn giao:** **64 Tính năng cốt lõi** phân bổ cho 4 nhóm Actor (22 Khách hàng `C-01`–`C-22`, 13 Nhân viên `S-01`–`S-13`, 12 Quản lý `M-01`–`M-12`, 17 Chủ chuỗi `A-01`–`A-17`).
  ```

---

### 🔴 Finding 2 (Major) — Lệch Danh Mục & Route Endpoint 4 SignalR Hubs
- **Vị trí 1:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`, Chương 6, Mục 6.3 (Dòng 1585-1604).
- **Vị trí 2:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`, Dòng 421 (`TableHub`).
- **Hiện trạng:**
  - Trong `Tong_Quan_Kien_Truc_He_Thong.md` (Mục 5.2), `Smart_FB_Operating_System.md` (Mục 7), và `Tom_Tat_1_Trang_Executive_Summary.md`, 4 SignalR Hubs chuẩn hóa là:
    1. `OrderHub` (`/hubs/orders`)
    2. `KitchenHub` (`/hubs/kitchen`)
    3. `PaymentHub` (`/hubs/payments`)
    4. `NotificationHub` (`/hubs/notifications`)
  - Nhưng trong `Workflow_Quy_Trinh_Nghiep_Vu.md` (Mục 6.3), sơ đồ và bảng lại liệt kê:
    - `KitchenHub` (`/hubs/kitchen`)
    - `NotificationHub` (`/hubs/notify`)
    - `MenuHub` (`/hubs/menu`)
    - `ManagerHub` (`/hubs/manager`)
  - Trong `Actor_Phan_Quyen_Chuc_Nang.md` (Dòng 421) xuất hiện tên `TableHub`.
- **Vấn đề:** Thiếu vắng `OrderHub` và `PaymentHub` trong chương SignalR của tài liệu Workflow; phát sinh các Hub không nằm trong thiết kế Backend (`MenuHub`, `ManagerHub`, `TableHub`).
- **Yêu cầu sửa đổi (Fix Suggestion):**
  - Cập nhật Chương 6 trong `Workflow_Quy_Trinh_Nghiep_Vu.md` để đồng bộ đúng 4 Hubs chuẩn: `OrderHub` (`/hubs/orders`), `KitchenHub` (`/hubs/kitchen`), `PaymentHub` (`/hubs/payments`), `NotificationHub` (`/hubs/notifications`).
  - Gộp các sự kiện thông báo của Manager và Menu vào `NotificationHub` và `KitchenHub`/`OrderHub` theo đúng kiến trúc.
  - Sửa `TableHub` ở Dòng 421 trong `Actor_Phan_Quyen_Chuc_Nang.md` thành `NotificationHub` (nhóm `branch_{branchId}_tables`).

---

### 🟡 Finding 3 (Minor) — Số Lượng & Định Danh Bảng Cơ Sở Dữ Liệu Chưa Hoàn Toàn Khớp
- **Vị trí:** `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`, Mục 7.2 (Dòng 372-400).
- **Hiện trạng:**
  - Tiêu đề ghi: `7.2 Danh Mục 25 Thực Thể Cơ Sở Dữ Liệu Chuẩn Hóa (PostgreSQL 16)`.
  - Danh sách bên dưới đánh số từ 1 đến 26: bao gồm `Combos`, `ComboItems`, `InventoryStocks`, `InventoryTransactions`, `OrderItemToppings`, `BranchProductPrices`, `ProductSizes`.
  - Trong khi `Tong_Quan_Kien_Truc_He_Thong.md` (Mục 6.1) chuẩn hóa chính xác **25 thực thể 3NF**: sử dụng mô hình Modifier tổng quát (`MODIFIERS`, `PRODUCT_MODIFIERS`, `ORDER_ITEM_MODIFIERS`), quản lý kho qua `INGREDIENTS`, `RECIPES_BOM`, và tích lũy qua `LOYALTY_CUP_TRANSACTIONS`.
- **Yêu cầu sửa đổi (Fix Suggestion):**
  - Đồng bộ hóa danh mục 25 thực thể trong `Smart_FB_Operating_System.md` để khớp 1:1 với 25 bảng thực thể trong Mermaid ERD của `Tong_Quan_Kien_Truc_He_Thong.md`.

---

## 4. KẾT LUẬN & HƯỚNG DẪN HÀNH ĐỘNG (NEXT STEPS)

- **Đánh giá tổng quát:** 5 tài liệu đặc tả đã đạt độ hoàn thiện rất xuất sắc về mặt tư duy kiến trúc, logic nghiệp vụ, giao tiếp thời gian thực, thiết kế database và ma trận xử lý trường hợp biên.
- **Hành động khắc phục:** Sau khi nhóm biên soạn cập nhật 3 điểm lệch dòng ở trên, toàn bộ bộ tài liệu sẽ đạt trạng thái **100% Contractual & Technical Consistency**, sẵn sàng tuyệt đối để bước vào giai đoạn cài đặt mã nguồn (Implementation Phase).
