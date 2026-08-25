# 📋 HANDOFF REPORT — FRONTEND SPECIFICATION MINER

**Dự án:** Smart F&B Operating System (Smart F&B OS)  
**Agent:** Frontend Specification Miner (`spec_miner_frontend`)  
**Mục tiêu bàn giao:** Báo cáo đặc tả toàn diện kiến trúc Frontend Next.js 14 App Router, 5 Route Groups, Shared UI Components, Zustand Stores, Custom Hooks, TypeScript DTOs, SignalR Contracts, Bảng 62 Tính năng cốt lõi và Ma trận Kịch bản Biên.  
**Ngày thực hiện:** 2026-08-25  

---

## 1. OBSERVATION (QUAN SÁT TRỰC TIẾP)

1. **Nguồn sự thật tài liệu đặc tả hệ thống:**
   - Đã khảo sát và đọc chi tiết các tài liệu đặc tả chuẩn hóa trong workspace:
     * `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md` (Lines 1-555): Xác định rõ 8 điểm nghẽn F&B, 5 trụ cột đột phá nghiệp vụ, 3 loại mã QR (Table QR, Delivery QR, Attendance QR), 3 loại đơn hàng (`DineIn`, `TakeAway`, `Delivery`), 2 module AI cốt lõi (AI-1 Gemini RAG & AI-2 Apriori Combo) và danh mục 62 tính năng.
     * `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md` (Lines 1-940): Xác lập Design Tokens (bảng màu kép Amber/Dark Slate, typography, spacing lưới 4px, touch targets >= 44px), hệ thống Web Audio API (880Hz-1174Hz, 440Hz 3-pulse, 587Hz), 5 Route Groups Next.js 14, 20 Wireframes ASCII chi tiết và UI RTM.
     * `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md` (Lines 1-1564): Đóng băng 10 nhóm RESTful API, 4 SignalR Hubs (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`), cấu trúc Envelope `ApiResponse<T>` / `PagedResponse<T>`, và chuẩn lỗi RFC 7807 ProblemDetails.
     * `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md` (Lines 1-1010): Xác thực chi tiết 10 sơ đồ tuần tự kiến trúc, cơ chế RedLock phân tán, Soft Inventory Reservation TTL 600s, Webhook PayOS HMAC-SHA256, và cơ chế Rollback/Compensation.
     * `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md` (Lines 1-1449): Kiểm tra 47 kịch bản UAT Test Cases, phân tích 10 kịch bản biên quan trọng và các quy tắc nghiệp vụ khóa cứng (ví dụ: Loyalty 10 ly chỉ áp dụng cho Takeaway; Delivery phí 20k và 100% VietQR).

2. **Cấu trúc mã nguồn Frontend hiện hữu:**
   - Đã khảo sát `d:\Idea_DoAn\frontend\`:
     * Thư mục `frontend/src/app/` đã có sẵn 5 Route Groups: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.
     * Thư mục `frontend/src/stores/` có các tệp store cơ bản: `useAuthStore.ts`, `useCartStore.ts`, `usePosStore.ts`.
     * Thư mục `frontend/src/types/` có tệp `index.ts`.

---

## 2. LOGIC CHAIN (CHUỖI SUY LUẬN LOGIC)

1. **Từ Quan sát 1 & 2 (5 Trụ Cột Nghiệp Vụ v2.5.0):**
   - Tài liệu `01_Smart_FB_Operating_System.md` và `05_UAT_Test_Cases.md` khẳng định sự thay đổi triệt để so với các mô hình POS truyền thống:
     * Dine-In chia làm 2 nhánh rõ ràng: Nhánh A (VietQR trả trước, Bếp nhận khi Paid) và Nhánh B (Tiền mặt trả sau, Bếp nhận ngay Confirmed, nhân viên mang đồ kèm hóa đơn có mã VietQR động).
     * QR Delivery bắt buộc nhập SĐT + Địa chỉ, tự động cộng 20.000đ phí giao hàng, và khóa 100% hình thức COD (chỉ chấp nhận VietQR trả trước).
     * Takeaway chuyển 100% thao tác về Web POS của thu ngân, áp dụng chính sách Loyalty 10 ly đổi 1 ly miễn phí (chỉ áp dụng duy nhất cho Takeaway).
     * Chấm công loại bỏ hoàn toàn GPS và QR động, thay bằng kiểm tra kép Router BSSID và IP Subnet chi nhánh.
     * Hợp nhất 100% nền tảng Web Responsive Monorepo Next.js 14, loại bỏ Mobile Native App.
   - Do đó, toàn bộ kiến trúc Route Groups, Components, Stores và TypeScript DTOs phải bám sát tuyệt đối 5 trụ cột này.

2. **Từ Quan sát 1 & 2 (Đặc Tả UI/UX & Real-time WebSockets):**
   - Giao diện KDS Bếp cần chế độ Nền Tối Chống Lóa chuyên dụng (`#0F172A`), bộ đếm SLA đổi màu Xanh/Cam/Đỏ nhấp nháy, Web Audio API 3 tần số âm thanh tổng hợp và công tắc 86-Toggle khẩn cấp.
   - Toàn bộ kết nối Real-time được phân bổ trên 4 SignalR Hubs chuyên biệt (`OrderHub`, `KitchenHub`, `PaymentHub`, `NotificationHub`) với cơ chế Auto-Reconnect backoff lũy thừa.
   - Quản lý trạng thái client cần 6 Zustand Stores (`useAuthStore`, `useCartStore`, `usePosStore`, `useShiftStore`, `useKdsStore`, `useTableStore`) đảm bảo luồng dữ liệu độc lập và phản hồi tức thời.

3. **Từ Quan sát 1 (Đặc Tả API Contract & DTOs):**
   - Đã ánh xạ chính xác các Interfaces & DTOs từ C# .NET 8 sang TypeScript, bao gồm Enums (`OrderType`, `OrderStatus`, `PaymentMethod`, `UserRole`, `TableStatus`), Payload gửi/nhận, Envelope `ApiResponse<T>` / `PagedResponse<T>` và `ProblemDetails`.

4. **Kết quả xây dựng `analysis.md`:**
   - Toàn bộ các phát hiện và đặc tả đã được tổng hợp hoàn chỉnh, chi tiết 100% Zero Placeholder vào tệp `d:\Idea_DoAn\.agents\spec_miner_frontend\analysis.md`.

---

## 3. CAVEATS (CÁC ĐIỂM LƯU Ý & GIẢ ĐỊNH)

1. **Phạm vi Agent:** Spec Miner chỉ thực hiện khảo sát, khai phá và tài liệu hóa đặc tả, không trực tiếp sửa đổi hay phát sinh mã nguồn ứng dụng ngoài thư mục phân quyền `.agents/spec_miner_frontend/`.
2. **Quyền riêng tư BSSID trên Web Browser:** Trên một số trình duyệt bảo mật cao, Web Browser API có thể không đọc trực tiếp được BSSID WiFi nếu không có extension hỗ trợ; hệ thống dự phòng cơ chế xác thực IP Subnet và Gateway IP tại tầng Ingress/Backend API.
3. **Web Audio Autoplay Policy:** Trình duyệt có thể chặn âm thanh phát tự động nếu người dùng chưa tương tác lần đầu (First Click); giao diện KDS cần có nút "Bật âm thanh chuông báo" để kích hoạt AudioContext ban đầu.

---

## 4. CONCLUSION (KẾT LUẬN)

1. **Hoàn thành 100% nhiệm vụ khai phá đặc tả Frontend:**
   - Đã trích xuất và tài liệu hóa toàn diện 5 Route Groups: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.
   - Đã đặc tả chi tiết danh mục Shared UI Components, 6 Zustand Stores, các Custom Hooks (`useSignalR`, `useWebAudio`, `useAttendanceWifi`, `useApiQuery`) và hệ thống TypeScript Interfaces/DTOs.
   - Đã lập Bảng Ma trận 62 Tính năng cốt lõi (Features Discovered Table) và Ma trận 12 Kịch bản biên (Edge Cases Table).
2. **Báo cáo chi tiết đã lưu:** `d:\Idea_DoAn\.agents\spec_miner_frontend\analysis.md`.

---

## 5. VERIFICATION METHOD (PHƯƠNG PHÁP KIỂM CHỨNG ĐỘC LẬP)

1. **Kiểm tra tệp báo cáo đặc tả:**
   - Xem nội dung tệp `d:\Idea_DoAn\.agents\spec_miner_frontend\analysis.md` bằng công cụ `view_file`.
   - Xác nhận có đầy đủ các mục: 5 Route Groups, UI Components, 6 Zustand Stores, Hooks, TypeScript DTOs, Bảng Features Discovered và Bảng Edge Cases.
2. **Kiểm tra tính nhất quán với Nguồn sự thật:**
   - Đối chiếu các mã tính năng C-01 ~ C-20, S-01 ~ S-13, M-01 ~ M-12, A-01 ~ A-17 với `01_Smart_FB_Operating_System.md` và `04_Thiet_Ke_UI_UX.md`.
   - Đối chiếu DTOs và SignalR Hubs với `03_Thiet_Ke_API_Contract.md`.
