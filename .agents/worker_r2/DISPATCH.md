## 2026-08-23T13:49:19Z
Bạn là Senior Solution Architect chịu trách nhiệm viết lại hoàn chỉnh tệp:
`d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md`

1. Thư mục làm việc của bạn: `d:\Idea_DoAn\.agents\worker_r2\`
Tạo file `d:\Idea_DoAn\.agents\worker_r2\progress.md` và `d:\Idea_DoAn\.agents\worker_r2\handoff.md`.

2. Bắt buộc đọc kỹ Nguồn sự thật (Source of Truth):
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`

3. Yêu cầu chi tiết cho `02_Sequence_Diagrams.md` (v2.5.0):
Tạo đầy đủ TỐI THIỂU 10 SƠ ĐỒ TUẦN TỰ MERMAID CHI TIẾT (Seq-01 đến Seq-10), có đầy đủ participants (Customer, Next.js Web App, NGINX, .NET 8 API Controller/MediatR, Redis 7 RedLock/Cache, PostgreSQL EF Core, SignalR Hub, PayOS Gateway, Gemini AI, v.v.), message payload, alt/loop/opt blocks, xử lý lỗi và transaction:
- **Seq-01**: Quy trình Gọi món Tại bàn - Nhánh A: Trả trước qua VietQR (PayOS webhook, SignalR KDS push, RedLock giữ bàn & trừ kho).
- **Seq-02**: Quy trình Gọi món Tại bàn - Nhánh B: Trả sau (Tiền mặt / Quét QR in trên Bill tại quầy POS thu ngân).
- **Seq-03**: Quy trình Đặt món Giao hàng (QR Delivery) - Phí ship cố định 20.000 VNĐ, 100% trả trước qua VietQR, validation địa chỉ nhận hàng & số điện thoại.
- **Seq-04**: Quy trình Bán hàng Mang đi (Takeaway Web POS) - Tích điểm khách hàng (Loyalty 10 ly tặng 1 ly), in hóa đơn, trừ kho tự động.
- **Seq-05**: Quy trình Chấm công Nhân viên qua WiFi - Xác thực kép BSSID & IP Subnet của chi nhánh (Không dùng GPS), lưu lịch sử ca làm việc.
- **Seq-06**: Quy trình Xử lý Đơn Bếp (KDS) & Khấu trừ Định lượng BOM - Trừ kho chi tiết theo gam/ml, chuyển trạng thái chế biến -> hoàn thành, chức năng 86-Toggle tạm ngưng món khi hết nguyên liệu.
- **Seq-07**: Quy trình Gọi Phục vụ & Hỗ trợ Khách hàng - Khách bấm gọi nước đá/khăn lạnh/thanh toán -> SignalR Realtime Hub push tới màn hình nhân viên -> Xác nhận đã xử lý.
- **Seq-08**: Quy trình Đánh giá & Phản hồi Khách hàng - Đánh giá 1-5 sao, phân tích cảm xúc (Sentiment Analysis) qua Gemini AI, kích hoạt Red Alert gửi thông báo khẩn cấp tới Quản lý khi rating <= 2 sao.
- **Seq-09**: Quy trình Mở ca & Kết ca (Z-Report) Thu ngân - Khai báo tiền đầu ca, kết ca đếm tiền mặt, đối soát doanh thu POS vs thực tế, yêu cầu giải trình bắt buộc nếu chênh lệch > 50.000 VNĐ.
- **Seq-10**: Quy trình Nghiệp vụ Quản trị viên (Admin Operations) - Quản lý thực đơn (CRUD món/BOM công thức), kích hoạt món theo mùa (Seasonal items), phân tích gợi ý tồn kho & doanh thu dự báo AI-2 (Gemini + Apriori).

4. Tiêu chuẩn:
- Zero Placeholders: Tuyệt đối không viết tóm tắt hay dùng `...` trong Mermaid. Mọi sơ đồ phải đầy đủ từng bước từ Request -> Validation -> Database -> Gateway -> Response -> Realtime Push.
- 100% cú pháp Mermaid hợp lệ (`sequenceDiagram`), phân biệt rõ actor, boundary, control, database, external gateway.
