# 📋 QUY TRÌNH 1: PHÂN TÍCH & LÀM RÕ YÊU CẦU NGHIỆP VỤ

> **Mục tiêu:** Xóa bỏ 100% điểm mơ hồ về nghiệp vụ trước khi thiết kế Database và API.

---

## 1. NHỮNG ĐIỂM BẮT BUỘC PHẢI LÀM RÕ TRONG BƯỚC NÀY

### 1.1 Xác Định Phạm Vi MVP Tier 1 (12 Nhóm Tính Năng Cốt Lõi)
Không dàn trải 71 tính năng. Phải chốt 12 nhóm tính năng chạy mượt 100% để demo luồng chính:
1. **QR Self-Order:** Khách quét QR → Mở PWA → Xem menu → Chọn món/tùy chỉnh → Đặt món.
2. **KDS Bếp:** Nhận đơn tức thì → Xem công thức pha chế → Cảnh báo chờ quá 5 phút → Bấm hoàn thành.
3. **Tracking Đơn Hàng:** Khách theo dõi tiến trình (Chờ xác nhận → Đang pha → Đã xong).
4. **Yêu Cầu Bill & Gọi NV:** Phát tín hiệu Alert tức thì tới Staff App và KDS.
5. **Thanh Toán:** Sinh mã VietQR động / Thu tiền mặt → NV xác nhận thành công.
6. **Mở/Kết Ca:** Quản lý mở ca với tiền đầu két, kết ca đối soát chênh lệch tiền thực đếm.
7. **Admin Menu CRUD:** Quản lý Danh mục, Sản phẩm, Biến thể Size, Toppings, Trạng thái hết hàng.
8. **Admin Dashboard:** Biểu đồ doanh thu real-time, số lượng đơn trong ngày, top món bán chạy.
9. **Xác Thực & RBAC:** Đăng nhập JWT cho 4 vai trò (`Admin`, `Manager`, `Staff`, `Customer`).
10. **Quản Lý Bàn & QR:** Sơ đồ bàn theo vùng (Zone), phát hành mã QR theo bàn.
11. **CRM SĐT Cơ Bản:** Khách nhập SĐT → Tích điểm Loyalty tự động.
12. **SignalR Real-time:** Truyền dữ liệu 2 chiều tức thì giữa Khách ↔ Bếp ↔ Nhân viên ↔ Quản lý.

---

### 1.2 Ràng Buộc Nghiệp Vụ Cần Chốt (Business Rules)

| STT | Nghiệp Vụ | Quy Tắc Chốt |
|---|---|---|
| 1 | **Tài khoản Khách hàng** | Khách **KHÔNG** cần đăng ký/đăng nhập. Quét QR là vào thẳng Menu. Nhập SĐT là tùy chọn để tích điểm. |
| 2 | **Hủy đơn hàng** | Khách chỉ được hủy đơn khi trạng thái là `Pending` (Chờ bếp nhận). Khi Bếp đã chuyển sang `Preparing` thì **KHÔNG** được hủy. |
| 3 | **Thanh toán VietQR** | Nhân viên quầy/phục vụ sẽ nhìn thấy màn hình báo chuyển khoản và bấm "Xác nhận đã nhận tiền" thủ công. |
| 4 | **Báo hết món** | Khi Barista/Manager bấm "Hết món" trên KDS hoặc Manager App, món đó lập tức ẩn/disabled trên Menu QR của Khách. |
| 5 | **Cảnh báo chờ lâu (KDS)** | Đơn chờ < 3 phút (Xanh) → 3-5 phút (Vàng) → > 5 phút (Đỏ + nhấp nháy phát chuông). |
| 6 | **Đối soát Két tiền** | Cuối ca, Quản lý nhập số tiền mặt thực đếm. Hệ thống tự tính: `Chênh lệch = Tiền thực đếm - (Tiền đầu ca + Doanh thu tiền mặt)`. |

---

### 1.3 Ma Trận Phân Quyền (RBAC Matrix)

| Chức năng | 👤 Customer | 🧋 Staff | 🏪 Manager | 👑 Admin |
|---|:---:|:---:|:---:|:---:|
| Quét QR xem Menu & Đặt món | ✅ | ✅ | ✅ | ✅ |
| Xem KDS & Bấm hoàn thành món | ❌ | ✅ | ✅ | ✅ |
| Xác nhận thanh toán & In bill | ❌ | ✅ | ✅ | ✅ |
| Mở ca / Kết ca két tiền | ❌ | ❌ | ✅ | ✅ |
| Quản lý Kho & Nhập/Xuất kho | ❌ | ❌ | ✅ | ✅ |
| Thêm/Sửa/Xóa Menu & Giá | ❌ | ❌ | ❌ | ✅ |
| Xem Dashboard Doanh thu toàn chuỗi | ❌ | ❌ | ❌ | ✅ |
| Phân quyền & Quản lý Nhân sự | ❌ | ❌ | ❌ | ✅ |

---

## 📥 INPUT & 📤 OUTPUT CỦA QUY TRÌNH 1

* **Input:** 5 file tài liệu đặc tả dự án (`Smart_FB_Operating_System.md`, `Workflow_Smart_FB_OS.md`, `Actor_Smart_FB_OS.md`,...).
* **Output:** Tài liệu chốt Scope MVP Tier 1, Business Rules & RBAC Matrix (đã thống nhất cả team).
* **Bước tiếp theo:** Chuyển sang **Quy trình 2: Thiết kế Database Schema (ERD)**.
