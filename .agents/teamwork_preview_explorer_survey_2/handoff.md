# 🤝 HANDOFF REPORT — EXPLORER 2 (API CONTRACTS & UI/UX SPECIALIST)

> **Agent:** Explorer 2 (API Contracts, UI/UX Design System & Real-Time Flows Specialist)  
> **Working Directory:** `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_2\`  
> **Target Files Audited:** `03_Thiet_Ke_API_Contract.md`, `04_Thiet_Ke_UI_UX.md`  
> **Source of Truth Reference:** `01_Tai_Lieu_Dac_Ta_Goc/` (`Smart_FB_Operating_System.md`, `Actor_Phan_Quyen_Chuc_Nang.md`, `Workflow_Quy_Trinh_Nghiep_Vu.md`, `Tong_Quan_Kien_Truc_He_Thong.md`, `Actor_KhachHang_Luong_Chay.md`)  
> **Handoff Type:** Soft Handoff (Investigation & Specification Audit Complete)  
> **Timestamp:** 2026-08-23T20:08:50+07:00  

---

## 1. Observation

1. **Về Số Lượng Nhóm API RESTful trong `03_Thiet_Ke_API_Contract.md`:**
   - Tại dòng 63-72 của `03_Thiet_Ke_API_Contract.md`, tài liệu hiện chỉ liệt kê **8 phân hệ**: `Auth/User`, `Orders Dine-in`, `Orders Delivery`, `Takeaway POS`, `Payments VietQR`, `KDS`, `Attendance WiFi`, `Manager/Admin`.
   - Các endpoint quan trọng theo chuẩn v2.5.0 gồm: Dine-in Nhánh B (Tiền mặt trả sau + Bill in VietQR), Z-Report đối soát két tiền, Tra cứu BOM định lượng, Seasonal Menu và KDS Batching lại bị xếp rời rạc ở mục 6 (dòng 583-674) dưới dạng "nhóm endpoint bổ sung".
   - Trong khi đó, `Actor_Phan_Quyen_Chuc_Nang.md` (dòng 738-750) và `Tong_Quan_Kien_Truc_He_Thong.md` (dòng 27, 155-168) yêu cầu phân rã thành **10 nhóm RESTful API chuẩn Clean Architecture .NET 8 / MediatR CQRS**.

2. **Về Hạ Tầng SignalR Hubs trong `03_Thiet_Ke_API_Contract.md`:**
   - Tại dòng 506-523 của `03_Thiet_Ke_API_Contract.md`, tài liệu chỉ mô tả **3 Hubs**: `OrderHub` (`/hubs/order`), `KitchenHub` (`/hubs/kitchen`), `NotifHub` (`/hubs/notif`).
   - Trong khi đó, `Workflow_Quy_Trinh_Nghiep_Vu.md` (dòng 1581-1606) và `Tong_Quan_Kien_Truc_He_Thong.md` (dòng 338-343) xác nhận hệ thống gồm **4 Hubs chuyên biệt**:
     - `OrderHub` (`/hubs/orders`)
     - `KitchenHub` (`/hubs/kitchen`)
     - `PaymentHub` (`/hubs/payments`)
     - `NotificationHub` (`/hubs/notifications`)

3. **Về Cấu Trúc UI/UX 5 Route Groups trong `04_Thiet_Ke_UI_UX.md`:**
   - Tại dòng 48-66 của `04_Thiet_Ke_UI_UX.md`, tài liệu chia thành 4 phân hệ với 3 khối giao diện (`CUSTOMER PWA`, `STAFF POS`, `WEB KDS`), không thể hiện rõ ràng 5 Route Groups độc lập của Next.js 14 App Router Monorepo.
   - Các wireframes mới (Nhánh B, BOM popup, Z-Report modal, Seasonal Menu, Bill VietQR) bị xếp riêng ở mục 5 (dòng 355-472) thay vì tích hợp theo luồng 5 Route Groups.
   - Trong khi đó, `Tong_Quan_Kien_Truc_He_Thong.md` (dòng 143-149, 329-335) và `Actor_KhachHang_Luong_Chay.md` (dòng 28-43) phân định rõ **5 Route Groups**: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.

4. **Về Việc Loại Bỏ Hoàn Toàn 100% Khái Niệm Lỗi Thời:**
   - Kiểm tra `grep_search` trên cả 2 tệp `03_` và `04_`: Đã hoàn toàn loại bỏ Staff Mobile App, Flutter/React Native, GPS 50m, QR 30s, C-23, C-24, ví voucher, tra cứu calo riêng lẻ.

---

## 2. Logic Chain

1. **Từ Quan Sát 1:** Sự phân mảnh giữa 8 phân hệ chính và mục 6 "bổ sung" trong `03_Thiet_Ke_API_Contract.md` khiến tài liệu thiếu tính hệ thống và khó ánh xạ trực tiếp sang các CQRS Handlers của .NET 8 Clean Architecture. Do đó, cần tái cấu trúc đồng bộ thành **10 nhóm RESTful API chuẩn hóa** với đầy đủ MediatR Commands/Queries, Request/Response DTOs và Business Rules.
2. **Từ Quan Sát 2:** Việc thiếu `PaymentHub` và sai quy ước đặt tên số nhiều (`/hubs/order` thay vì `/hubs/orders`, `/hubs/notif` thay vì `/hubs/notifications`) tạo nguy cơ không đồng nhất giữa Backend SignalR Hub configuration và Frontend client hooks (SignalR client listeners). Do đó, cần chuẩn hóa toàn bộ 4 Hubs theo đúng `Workflow_Quy_Trinh_Nghiep_Vu.md`.
3. **Từ Quan Sát 3:** Việc tổ chức UI/UX không theo cấu trúc thư mục Next.js 14 App Router làm giảm tính trực quan cho Frontend Developers khi xây dựng các `layout.tsx`, `page.tsx` và middleware phân quyền. Do đó, cần cấu trúc lại toàn bộ `04_Thiet_Ke_UI_UX.md` xoay quanh **5 Route Groups** (`(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`), tích hợp toàn bộ 18 Wireframes chuẩn hóa vào đúng từng Route Group.
4. **Từ Quan Sát 4:** Codebase tài liệu đã sạch các khái niệm lỗi thời (Staff App, GPS 50m, QR 30s, C-23, C-24), là nền tảng thuận lợi để triển khai viết lại tài liệu hoàn chỉnh 100% không phát sinh mâu thuẫn.

---

## 3. Caveats

- **Phạm vi thẩm định:** Explorer 2 chỉ tập trung chuyên sâu vào Hợp đồng API (RESTful OpenAPI 3.1, SignalR Hubs, PayOS Webhook) và Thiết kế UI/UX (Design Tokens, 5 Route Groups, Wireframes, Screen Flows). Các phần về Database Schema (25 bảng) do Explorer 1 khảo sát, phần Backend/Frontend Implementation do Lead Developers phụ trách.
- **Giả định kỹ thuật:** Giả định kiến trúc Next.js 14 App Router Monorepo và .NET 8 Web API Clean Architecture đã được thống nhất đóng băng theo Source of Truth.
- **Không có caveats nào khác.**

---

## 4. Conclusion

1. Tài liệu `03_Thiet_Ke_API_Contract.md` cần được viết lại toàn diện theo cấu trúc **10 nhóm RESTful API** (.NET 8 Clean Architecture / MediatR CQRS) + **4 SignalR Hubs** (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) + **Đặc tả PayOS Webhook HMAC SHA256** chi tiết.
2. Tài liệu `04_Thiet_Ke_UI_UX.md` cần được tái cấu trúc toàn diện theo **5 Route Groups Next.js 14 App Router Monorepo** (`(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`), tích hợp đầy đủ **18 ASCII Wireframes** cho cả 3 kênh bán (`DineIn` 2 nhánh, `Delivery` 20k, `TakeAway` 10 ly), KDS Dark Mode, Web POS Quầy, Chấm công WiFi, Z-Report đếm két tiền và AI-2 Combo Approval.
3. Báo cáo khảo sát chi tiết đã được xuất bản đầy đủ tại: `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_2\survey_api_uiux.md`.

---

## 5. Verification Method

1. **Kiểm tra Báo cáo Khảo sát:**
   - Mở và đọc tệp `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_2\survey_api_uiux.md`.
   - Xác nhận có đủ 10 nhóm API, 4 SignalR Hubs, PayOS Webhook HMAC SHA256, Design System Tokens, cây thư mục 5 Route Groups và các wireframes chi tiết.
2. **Kiểm tra tính nhất quán với Source of Truth:**
   - Đối chiếu các endpoint trong `survey_api_uiux.md` với `Actor_Phan_Quyen_Chuc_Nang.md` (Phần 7) và `Workflow_Quy_Trinh_Nghiep_Vu.md` (Chương 2, 6).
   - Xác nhận không còn chứa bất kỳ từ khóa lỗi thời nào (`Flutter`, `GPS 50m`, `QR 30s`, `C-23`, `C-24`).
3. **Điều kiện vô hiệu hóa (Invalidation Conditions):**
   - Báo cáo bị coi là không hợp lệ nếu thiếu bất kỳ nhóm nào trong 10 nhóm API hoặc thiếu bất kỳ Hub nào trong 4 SignalR Hubs.
