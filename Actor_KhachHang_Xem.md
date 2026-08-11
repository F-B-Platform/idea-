# HỆ THỐNG SMART F&B OS — ĐẶC TẢ VAI TRÒ & NĂNG LỰC HỆ THỐNG

> **Tài liệu đặc tả cho Khách hàng & Chủ đầu tư**  
> Mô tả 4 nhóm người dùng trong hệ thống, phạm vi thao tác, giao diện và các tính năng hỗ trợ vận hành.

---

## TỔNG QUAN: 4 NHÓM NGƯỜI DÙNG

| STT | Nhóm người dùng | Vai trò & Thao tác chính | Thiết bị & Giao diện | Số tính năng |
|---|---|---|---|---|
| 1 | **Khách hàng** | Quét QR đặt món, thanh toán tại bàn/quầy, đánh giá món | Điện thoại cá nhân (Trình duyệt PWA, không cần cài app) | 24 |
| 2 | **Nhân viên pha chế / Phục vụ** | Nhận đơn real-time, xem công thức pha, báo hết món, chấm công | TV/Màn hình quầy (KDS) + Mobile App nội bộ nhân viên | 12 |
| 3 | **Quản lý chi nhánh** | Mở/kết ca, kiểm kê kho, xuất kho quầy, xem báo cáo chi nhánh | App Mobile Quản lý + Web Dashboard | 13 |
| 4 | **Chủ chuỗi (Admin)** | Quản trị toàn bộ chuỗi, cấu hình menu/giá, phân tích AI | Web Dashboard (Máy tính/Laptop) — Toàn quyền | 22 |

> **Tổng cộng hệ thống:** 71 tính năng + 5 Module AI phân tích thông minh

---

## MỐI QUAN HỆ VÀ LUỒNG VẬN HÀNH GIỮA CÁC ACTOR

```
      KHÁCH HÀNG                   NHÂN VIÊN                   QUẢN LÝ
     (Điện thoại PWA)           (TV quầy + App NV)           (App ĐT + Web)
          │                           │                          │
  Quét QR -> Đặt món           Nhận đơn tức thì           Mở ca / Kết ca
  Nhập SĐT -> Tích điểm       Pha chế theo công thức     Nhập/Xuất kho quầy
  Chat AI -> Gợi ý món         In bill / Mang bill        Kiểm kê nguyên liệu
  Đánh giá -> Feedback         Chấm công QR + GPS         Xem doanh thu chi nhánh
          │                           │                          │
          └───────────────────────────┼──────────────────────────┘
                                      │
                              CHỦ CHUỖI (ADMIN)
                           (Website trên máy tính)
                                      │
                         • Thống kê doanh thu toàn chuỗi real-time
                         • Quản lý menu, giá, combo đồng bộ cả chuỗi
                         • AI dự đoán nguy cơ rời đi của khách hàng
                         • AI gợi ý tạo combo bán chạy
                         • AI phân tích hiệu quả menu
                         • Xuất báo cáo quản trị & kế toán
```

---

## 1. KHÁCH HÀNG — Tự đặt món trên điện thoại

> **Không cần cài đặt ứng dụng** — Khách hàng quét mã QR tại bàn bằng camera điện thoại, giao diện PWA mở trực tiếp trên trình duyệt.

### Trải nghiệm khách hàng tại quán:

```
[1] Quét mã QR tại bàn
      │
      ▼
[2] Nhập số điện thoại nhận diện
   ├── Lần đầu: Nhập thêm Tên -> Hệ thống tự động tạo hồ sơ CRM
   └── Khách quen: Hệ thống nhận diện -> Hiển thị tên, điểm tích lũy & món hay gọi
      │
      ▼
[3] Xem Menu -> Chọn món -> Tùy chỉnh (Size / Đường / Đá / Topping)
      │
      ▼
[4] Theo dõi trạng thái đơn hàng (Xác nhận -> Đang pha chế -> Sẵn sàng)
      │
      ▼
[5] Yêu cầu thanh toán -> Nhân viên mang bill ra bàn hoặc thanh toán tại quầy
      │
      ▼
[6] Đánh giá chất lượng -> Tự động tích điểm Loyalty
```

### Danh sách 24 tính năng dành cho Khách hàng

| Nhóm chức năng | Tên tính năng | Mô tả giá trị mang lại |
|---|---|---|
| **Nhận diện** | Nhận diện SĐT | Quét QR nhập SĐT -> Hệ thống nạp hồ sơ CRM, lịch sử món uống và điểm tích lũy |
| **Đặt món** | Scan QR xem menu | Quét QR tại bàn -> Trình duyệt mở menu tự động gắn đúng số bàn và chi nhánh |
| | Menu trực quan | Hiển thị menu phân loại rõ ràng (Cà phê, Trà, Bánh) kèm hình ảnh và giá |
| | Tùy chỉnh món | Cho phép chọn Size (S/M/L), mức Đường, mức Đá và Topping đi kèm |
| | Ghi chú đặc biệt | Ghi chú yêu cầu riêng: "Ít đá", "Không đường", "Thêm shot espresso" |
| | Giỏ hàng | Thêm nhiều món, điều chỉnh số lượng và kiểm tra tổng tiền trước khi gửi đơn |
| | Mang đi / Tại quán | Lựa chọn hình thức "Phục vụ tại bàn" hoặc "Mang đi (Takeaway)" |
| **Thanh toán** | Yêu cầu in bill | Bấm nút yêu cầu -> Hệ thống thông báo nhân viên in bill và mang ra bàn |
| | Thanh toán tại bàn | Thanh toán tiền mặt hoặc quét mã VietQR -> Nhân viên xác nhận hoàn tất |
| | Thanh toán tại quầy | Khách hàng chủ động ra quầy thanh toán trực tiếp với nhân viên |
| | Áp mã giảm giá | Khách hàng báo mã voucher -> Nhân viên áp dụng trực tiếp trên đơn hàng |
| | Cập nhật doanh thu | Đơn hàng hoàn tất -> Doanh thu tự động cập nhật tức thì lên Dashboard |
| **Trải nghiệm** | Chatbot AI gợi ý | Chat tương tác với AI: "Gợi ý đồ uống mát nhẹ" -> AI phân tích đưa ra lựa chọn |
| | Món bán chạy | Hiển thị nhãn "Best Seller", "Hot Trend" dựa trên dữ liệu bán hàng thực tế |
| | Trạng thái đơn hàng | Thanh tiến trình cập nhật real-time: "Đã nhận -> Đang pha -> Sẵn sàng" |
| | Thời gian chờ ước tính | Hiển thị thời gian dự kiến hoàn thành dựa trên số lượng đơn hàng trong hàng chờ |
| | Thông báo hoàn thành | Bắn thông báo lên trình duyệt điện thoại khi món nước đã pha xong |
| | Gọi nhân viên | Bấm nút hỗ trợ -> Gửi thông báo đến ứng dụng của nhân viên: "Bàn X cần hỗ trợ" |
| **Feedback & Review** | Đánh giá từng món | Cho phép đánh giá 1-5 sao chi tiết từng món trong đơn hàng |
| | Chụp ảnh thực tế | Chụp và tải ảnh trực tiếp từ camera điện thoại lên hệ thống |
| | Tùy chọn ẩn danh | Tùy chọn ẩn danh tính khi gửi nhận xét để khách hàng thoải mái đóng góp ý kiến |
| | Hiển thị công khai | Đánh giá hiển thị trực tiếp trên trang QR Menu cho các khách hàng sau tham khảo |
| | Cảnh báo đánh giá kém | Đánh giá từ 1-2 sao tự động gửi alert khẩn cấp đến Quản lý để xử lý kịp thời |
| **Tích điểm CRM** | Tích điểm tự động | Đơn hàng hoàn thành tự động cộng điểm loyalty vào tài khoản SĐT khách hàng |
| | Lưu lịch sử gọi món | Ghi nhận tần suất ghé quán, tổng chi tiêu và các món uống ưa thích |
| | Gửi voucher qua Zalo | Voucher sinh nhật, ưu đãi tri ân tự động gửi qua Zalo OA |
| **Nâng cao** | Gọi thêm món | Cho phép chọn thêm món bổ sung vào đơn đang xử lý mà không cần tạo đơn mới |
| | Dị ứng & Calories | Hiển thị cảnh báo thành phần gây dị ứng và hàm lượng calories từng món |
| | Món yêu thích | Tự động đề xuất danh mục "Món hay gọi" giúp đặt hàng nhanh trong 1 lần chạm |

> **Giá trị cốt lõi của tính năng Feedback:**
> - Hình ảnh thực tế từ khách hàng giúp tăng tính minh bạch và uy tín cho thương hiệu.
> - Tùy chọn ẩn danh khuyến khích phản hồi trung thực, giúp bộ phận vận hành cải thiện dịch vụ.
> - Cơ chế cảnh báo phản hồi kém giúp Quản lý can thiệp xử lý ngay tại quán, tránh suy giảm trải nghiệm khách hàng.

---

## 2. NHÂN VIÊN PHA CHẾ / PHỤC VỤ — Nhận đơn tự động, tối ưu pha chế

> **Môi trường làm việc song song:** Màn hình KDS tại quầy pha chế + App di động nội bộ dành cho nhân viên.

### Luồng vận hành của Nhân viên:

```
[1] Đơn hàng mới hiển thị tức thì trên màn hình KDS tại quầy
      │
      ▼
[2] KDS hiển thị chi tiết tên món + Công thức định lượng chuẩn
      │
      ▼
[3] Pha chế theo định lượng -> Bấm "Hoàn thành" -> Bắn thông báo tới khách hàng
      │
      ▼
[4] App nhân viên nhận alert "Bàn X cần bill" -> In bill -> Thu tiền -> Xác nhận
```

### Danh sách 12 tính năng dành cho Nhân viên

| Nhóm chức năng | Tên tính năng | Giá trị hỗ trợ vận hành |
|---|---|---|
| **Đơn hàng** | Đơn hàng real-time | Đơn từ QR Order tự động chuyển đến màn hình KDS mà không qua khâu trung gian |
| | Hiển thị công thức | Tự động đính kèm công thức định lượng chi tiết cho từng món trên màn hình KDS |
| | Cảnh báo thời gian | Tự động chuyển màu cảnh báo đơn hàng chờ lâu (Xanh -> Vàng -> Đỏ) để ưu tiên |
| | Xác nhận hoàn thành | Thao tác 1 chạm báo hoàn thành -> Đơn biến mất khỏi KDS và gửi thông báo tới khách |
| | Hiển thị ghi chú | Hiển thị nổi bật các yêu cầu đặc biệt của khách trên giao diện pha chế |
| | Gom đơn theo bàn | Chế độ hiển thị tổng hợp toàn bộ món theo từng bàn để nhân viên trả món 1 lần |
| **Vận hành** | Báo hết món | Thao tác báo hết món trực tiếp trên KDS -> Món nước tự động ẩn trên QR Menu |
| | In hóa đơn | Kết nối máy in nhiệt tại quầy để xuất hóa đơn thanh toán cho khách hàng |
| | Sơ đồ bàn trực quan | Cập nhật trạng thái bàn đang có khách hoặc bàn trống theo thời gian thực |
| | Nhận alert gọi hỗ trợ | Nhận thông báo kèm âm thanh trên KDS và App khi khách hàng bấm nút gọi hỗ trợ |
| | Chấm công GPS & QR | Thực hiện check-in/check-out ca làm việc bằng mã QR động và bán kính GPS |
| | Mobile App nội bộ | Ứng dụng di động giúp nhân viên nhận chuông báo bill, xuất VietQR và kiểm tra sơ đồ bàn |

> **Lưu ý:** Nhân viên pha chế không cần tra cứu thủ công — Công thức định lượng chuẩn đã được tích hợp tự động trên giao diện KDS.

---

## 3. QUẢN LÝ CHI NHÁNH — Quản lý vận hành & Kho hàng chi nhánh

> **Phạm vi quyền hạn:** Quản lý toàn bộ hoạt động trong ca, két tiền, nguyên vật liệu và báo cáo thuộc chi nhánh phụ trách.

### Quy trình quản lý trong ngày:

```
ĐẦU CA: Mở ca làm việc -> Kiểm đếm và khai báo tiền mặt đầu két
  │
TRONG CA:
  • Duyệt lịch làm việc & phân công ca nhân viên
  • Xuất kho nguyên liệu từ Kho tổng sang Quầy pha chế
  • Nhập kho hàng hóa từ Nhà cung cấp
  • Kiểm kê định kỳ & đối soát hao hụt
  • Truy vấn dữ liệu qua AI Thống kê
  │
CUỐI CA: Kết ca -> Kiểm đếm tiền két thực tế -> Hệ thống đối soát tự động
```

### Danh sách 13 tính năng dành cho Quản lý chi nhánh

| Nhóm chức năng | Tên tính năng | Mô tả chức năng quản lý |
|---|---|---|
| **Quản lý ca** | Mở ca / Kết ca | Khai báo tiền mặt đầu ca và đối soát tiền thực đếm khi đóng ca làm việc |
| | Đối soát két tiền | Tự động so sánh doanh thu máy ghi nhận với tiền thực đếm -> Cảnh báo khi lệch chênh |
| | Duyệt lịch làm việc | Xem bảng phân công tuần, duyệt yêu cầu đổi ca và điều phối nhân sự thay thế |
| | Quản lý chấm công | Ghi nhận thời gian ra/vào ca, phát hiện các trường hợp đi muộn hoặc tăng ca |
| **Quản lý kho** | Xuất kho quầy | Tạo phiếu điều chuyển nguyên vật liệu từ Kho tổng sang Quầy pha chế |
| | Kiểm kê nguyên liệu | Nhập số lượng tồn thực tế -> Hệ thống tự động tính toán chênh lệch hao hụt |
| | Cảnh báo tồn kho | Tự động phát cảnh báo khi nguyên liệu xuống dưới định mức tối thiểu |
| | Nhập kho nhà cung cấp | Ghi nhận phiếu nhập hàng từ nhà cung cấp và tự động tăng tăng tồn kho tổng |
| **Báo cáo & AI** | Doanh thu ca/ngày | Theo dõi tổng doanh thu, số lượng đơn, giá trị trung bình đơn của chi nhánh |
| | Phân tích khung giờ | Biểu đồ mật độ đơn hàng theo khung giờ giúp tối ưu hóa số lượng nhân sự trong ca |
| | Báo cáo EOD tự động | Tự động tổng hợp và gửi báo cáo kết ca qua Email/Zalo cho cấp quản lý |
| | AI Thống kê chi nhánh | Truy vấn dữ liệu doanh thu, hao hụt bằng câu hỏi tự nhiên -> AI trích xuất kết quả tức thì |
| **Cấu hình** | Sơ đồ bàn chi nhánh | Thiếp lập sơ đồ bàn, khu vực (Trong nhà, Sân thượng, VIP) phục vụ hiển thị trên KDS & QR |

---

## 4. CHỦ CHUỖI (ADMIN) — Quản trị chiến lược toàn hệ thống

> **Phạm vi quyền hạn:** Toàn quyền quản trị đa chi nhánh, cấu hình thực đơn toàn chuỗi, quản lý nhân sự và sử dụng 5 Module AI.

### Thao tác quản trị chính của Chủ chuỗi:

```
[1] Truy cập Web Dashboard trung tâm trên máy tính
      │
      ▼
[2] Theo dõi Dashboard tổng quan 3 chi nhánh theo thời gian thực
      │
      ├── So sánh hiệu quả kinh doanh giữa các chi nhánh -> Báo cáo P&L tự động
      ├── Quản lý Thực đơn / Bảng giá / Gói Combo -> Đồng bộ toàn bộ hệ thống
      ├── Cấu hình chương trình Khuyến mãi / Tích điểm / Phân quyền tài khoản
      ├── AI Thống kê: Truy vấn so sánh chỉ số kinh doanh toàn chuỗi
      ├── AI Phân tích: Đề xuất gói Combo, dự báo rủi ro rời đi của khách hàng
      └── Xuất dữ liệu báo cáo dạng Excel/PDF cho bộ phận Kế toán
```

### Danh sách 22 tính năng dành cho Chủ chuỗi (Admin)

| Nhóm chức năng | Tên tính năng | Giá trị quản trị chiến lược |
|---|---|---|
| **Dashboard** | Tổng quan đa chi nhánh | Hiển thị doanh thu, lượng đơn hàng và cảnh báo của tất cả chi nhánh trên 1 màn hình |
| | So sánh chi nhánh | Biểu đồ trực quan so sánh chỉ số doanh thu, chi phí giữa các cơ sở kinh doanh |
| | Báo cáo P&L tự động | Tự động tổng hợp Doanh thu - Chi phí (Nguyên liệu, Lương, Điện nước) = Lợi nhuận ròng |
| | Cảnh báo trung tâm | Bắn cảnh báo tức thì khi có sự cố lệch két, hết kho hoặc phản hồi chất lượng kém |
| **Menu & Giá** | Quản lý thực đơn | Tạo mới, chỉnh sửa món ăn, công thức pha và tải hình ảnh đồng bộ cả chuỗi |
| | Cấu hình giá linh hoạt | Cho phép thiết lập chính sách giá riêng biệt theo từng khu vực/chi nhánh |
| | Khóa món tức thì | Thao tác tắt hiển thị món nước trên toàn bộ QR Menu khi thiếu nguyên liệu |
| | Menu theo thời điểm | Thiết lập lịch tự động kích hoạt thực đơn theo mùa hoặc theo khung giờ cố định |
| | Quản lý gói Combo | Tạo các gói kết hợp món nước + bánh ngọt giúp nâng cao giá trị trung bình đơn |
| **Nhân sự & CRM** | Quản lý nhân sự chuỗi | Tạo tài khoản, phân quyền truy cập và giám sát bảng chấm công nhân viên toàn hệ thống |
| | Cấu hình CRM & Loyalty | Thiết lập quy tắc tích điểm, hạng thành viên và các chính sách đổi quà |
| | Quản lý Khuyến mãi | Cài đặt các chương trình giảm giá theo khung giờ vàng, mã quà tặng sinh nhật |
| **Phân tích AI** | AI Thống kê toàn chuỗi | Truy vấn so sánh dữ liệu kinh doanh phức tạp bằng ngôn ngữ tự nhiên |
| | AI Phân tích thực đơn | AI tự động đưa ra khuyến nghị bổ sung món trend hoặc loại bỏ món bán chậm |
| | AI Dự báo khách rời đi | Phân tích tần suất gọi món để phát hiện khách hàng sắp ngừng quay lại và tự gửi voucher |
| | AI Đề xuất Combo | Phân tích lịch sử đơn hàng để gợi ý kết hợp các món thường được mua cùng nhau |
| **Quản trị hệ thống** | Xuất dữ liệu báo cáo | Trích xuất báo cáo doanh thu, kho hàng, chi phí ra file Excel/PDF chuẩn kế toán |
| | Nhật ký thao tác (Audit Log) | Ghi vết toàn bộ lịch sử chỉnh sửa giá, xóa đơn, đổi menu để phòng ngừa gian lận |
| | Cấu hình giờ hoạt động | Đặt khung giờ mở/đóng cửa -> Hệ thống tự động chặn đặt hàng ngoài giờ |
| | Phân quyền RBAC | Phân quyền chi tiết theo từng cấp bậc (Quản lý chỉ xem chi nhánh phụ trách) |
| | Gửi thông báo hệ thống | Phát thông báo khẩn cấp tới toàn bộ App nhân viên và Quản lý trên toàn chuỗi |

---

## BẢNG PHÂN BỔ CÁC MODULE AI TRONG HỆ THỐNG

| Module AI | Chức năng cốt lõi | Đối tượng sử dụng |
|---|---|---|
| **AI Thống kê dữ liệu** | Phân tích câu hỏi tự nhiên -> Trích xuất biểu đồ doanh thu & báo cáo | Quản lý chi nhánh & Chủ chuỗi |
| **AI Đề xuất Combo** | Phân tích hành vi mua sắm -> Đề xuất gói kết hợp tối ưu doanh số | Chủ chuỗi (Admin) |
| **AI Dự báo giữ chân khách** | Phát hiện khách hàng giảm tần suất ghé -> Tự động kích hoạt voucher | Chủ chuỗi (Tự động vận hành) |
| **AI Phân tích thực đơn** | Đánh giá hiệu suất bán của từng món -> Đề xuất tối ưu thực đơn | Chủ chuỗi (Admin) |
| **AI Chatbot tư vấn** | Tương tác giải đáp nhu cầu đồ uống dựa trên khẩu vị và thời tiết | Khách hàng (trên QR Menu) |

> **Lưu ý:** Bộ phận pha chế vận hành trực tiếp trên màn hình KDS đã có sẵn định lượng công thức, không cần sử dụng Chatbot tra cứu.

---

## MA TRẬN PHÂN QUYỀN TRUY CẬP (RBAC MATRIX)

| Chức năng hệ thống | Khách hàng | Nhân viên | Quản lý chi nhánh | Chủ chuỗi (Admin) |
|---|---|---|---|---|
| Đặt món qua QR Menu | Cho phép | — | — | — |
| Hiển thị đơn hàng KDS | — | Cho phép | — | — |
| Thao tác báo hết món | — | Cho phép | Cho phép | Cho phép |
| Chấm công ca làm | — | Cho phép | Xem dữ liệu | Xem dữ liệu |
| Thao tác Mở/Kết ca | — | — | Cho phép | Xem dữ liệu |
| Quản lý xuất/nhập kho | — | — | Cho phép | Xem dữ liệu |
| Báo cáo doanh thu | — | — | Xem chi nhánh | Xem toàn chuỗi |
| Truy vấn AI Thống kê | — | — | Xem chi nhánh | Xem toàn chuỗi |
| Quản lý Thực đơn & Giá | — | — | — | Cho phép |
| Cấu hình Khuyến mãi / Combo | — | — | — | Cho phép |
| Module AI Phân tích & Dự báo | — | — | — | Cho phép |
| Quản lý Nhân sự & Phân quyền | — | — | — | Cho phép |
| Nhật ký Audit Log | — | — | — | Cho phép |

---

## BẢNG TỔNG HỢP CHỈ TIÊU HỆ THỐNG

| Chỉ tiêu hệ thống | Dữ liệu quy chuẩn |
|---|---|
| Tổng số Nhóm người dùng (Actor) | **4** (Khách hàng, Nhân viên, Quản lý, Chủ chuỗi) |
| Tổng số Tính năng vận hành | **71 tính năng** (Khách hàng: 24, Nhân viên: 12, Quản lý: 13, Admin: 22) |
| Tổng số Module AI | **5 Module** (Thống kê, Combo, Giữ chân khách, Phân tích thực đơn, Chatbot) |
| Giao diện chính | QR PWA (Khách), KDS & Mobile App (NV), App & Web (Quản lý), Web Dashboard (Admin) |
