# ☕ TÓM TẮT ĐỀ TÀI: PAIN POINTS & SOLUTIONS
> **Đề tài:** Nền Tảng Quản Lý Chuỗi F&B Thông Minh (AI-Powered Smart F&B Chain OS)  
> **Giai đoạn:** Đề xuất Ý tưởng & Định hướng Giải pháp (Proposal)

---

## 🔴 PHẦN 1: BẤT CẬP THỰC TẾ (PAIN POINTS)

| # | Vấn Đề Vận Hành | Hiện Trạng Tại Quán | Tác Động & Hậu Quả Thực Tế |
|---|---|---|---|
| **V1** | **Chấm công gian lận & Thiếu giám sát** | Dùng sổ tay hoặc máy vân tay độc lập; Nhân viên đi muộn, về sớm, nhờ ký hộ; Quản lý không nắm được nhân sự từ xa. | • Thất thoát quỹ lương hàng tháng.<br>• Mất thời gian tổng hợp và tính lương thủ công.<br>• Tạo tâm lý bất mãn giữa các nhân viên. |
| **V2** | **Xếp ca làm việc cảm tính** | Xếp ca dựa trên cảm nhận cá nhân; Phân bổ ca làm không công bằng; Khó xoay sở khi nhân viên xin nghỉ đột xuất. | • Thừa nhân công giờ vắng, gây lãng phí chi phí.<br>• Thiếu người giờ cao điểm, giảm chất lượng phục vụ.<br>• Nhân viên bất mãn, tỷ lệ nghỉ việc cao. |
| **V3** | **Kiểm kê thủ công & Thất thoát kho** | Đếm tay từng món cuối tháng; Không có định mức công thức (BOM) trừ tự động; Đong đếm sai lệch; Hết hàng giữa ca. | • Thất thoát nguyên liệu không rõ lý do.<br>• Bị động, gián đoạn bán hàng vì hết nguyên liệu.<br>• Sai lệch giữa tồn kho thực tế và sổ sách. |
| **V4** | **Tài chính rời rạc & Nguy cơ thất thoát** | POS, kho, nhân sự nằm rải rác; Bán hàng không nhập hệ thống để trục lợi; Không tổng hợp được chi phí thực tế. | • Rò rỉ doanh thu tiền mặt.<br>• Không xác định được điểm hòa vốn và lợi nhuận thực.<br>• Chậm phát hiện các chi nhánh đang hoạt động kém. |
| **V5** | **Chất lượng sản phẩm không đồng nhất** | Phụ thuộc hoàn toàn vào tay nghề cá nhân của Barista; Lệch vị giữa các chi nhánh; Tốn thời gian đào tạo nhân sự mới. | • Mất khách hàng trung thành do chất lượng thất thường.<br>• Lãng phí nguyên liệu do pha chế sai phải bỏ.<br>• Khó nhân rộng và chuẩn hóa quy mô chuỗi. |
| **V6** | **Chăm sóc khách hàng kém hiệu quả** | Sử dụng thẻ tích điểm giấy dễ thất lạc; Thiếu dữ liệu về thói quen khách; Khách bỏ đi không được phát hiện. | • Tốn chi phí thu hút khách mới thay vì giữ khách cũ.<br>• Bỏ lỡ cơ hội gợi ý bán thêm (upsell/cross-sell).<br>• Không có kênh chăm sóc cá nhân hóa. |
| **V7** | **Sự cố thiết bị xảy ra bất ngờ** | Thiết bị chính (máy pha, máy xay) hỏng đột ngột; Tủ lạnh hỏng ban đêm làm hỏng nguyên liệu đắt tiền. | • Tê liệt vận hành trong giờ cao điểm.<br>• Hư hỏng toàn bộ nguyên liệu lưu trữ tươi sống.<br>• Chi phí sửa chữa cấp bách đắt đỏ. |
| **V8** | **Lãng phí chi phí năng lượng** | Thiết bị điện bật liên tục bất kể lượng khách; Không theo dõi được điện năng tiêu thụ của từng thiết bị. | • Tăng chi phí vận hành cố định hàng tháng.<br>• Lãng phí năng lượng không cần thiết. |

---

## 🟢 PHẦN 2: GIẢI PHÁP TƯƠNG ỨNG (SOLUTIONS)

### 📌 Ánh Xạ Giải Pháp Tương Ứng

> [!TIP]
> **Mô hình chuyển đổi:** Từ **Ghi nhận thủ công** $\rightarrow$ **Tự động hóa & Giám sát thông minh**

- **[V1: Chấm công gian lận]** $\longrightarrow$ **S1:** QR Check-in + Định vị GPS + Xác thực hình ảnh
- **[V2: Xếp ca cảm tính]** $\longrightarrow$ **S2:** AI Dự báo nhu cầu khách + Tự động xếp ca tối ưu
- **[V3: Thất thoát kho]** $\longrightarrow$ **S3:** Khấu trừ kho tự động theo BOM + AI Đề xuất nhập hàng
- **[V4: Tài chính rời rạc]** $\longrightarrow$ **S4:** Dashboard quản trị tập trung + Tích hợp Hóa đơn điện tử
- **[V5: Lệch chất lượng]** $\longrightarrow$ **S5:** Công thức chuẩn hóa KDS + Hướng dẫn kỹ thuật + Cảm biến giám sát
- **[V6: Mất khách hàng]** $\longrightarrow$ **S6:** Loyalty Digital + AI Nhận diện khách rời bỏ + Auto-Voucher
- **[V7: Thiết bị hỏng]** $\longrightarrow$ **S7:** Cảm biến IoT giám sát tủ lạnh + Cảnh báo sự cố tức thì
- **[V8: Lãng phí điện]** $\longrightarrow$ **S8:** Cảm biến đo điện năng + Đề xuất tối ưu năng lượng

---

### 💡 Chi Tiết 6 Tính Năng AI & IoT Cốt Lõi

#### 1. 🤖 AI Dự Báo Nhu Cầu & Nhập Hàng (`XGBoost` / `Prophet`)
* **Định hướng:** Phân tích lịch sử bán hàng kết hợp yếu tố thời tiết, ngày lễ $\rightarrow$ Dự báo lượng khách từng khung giờ và đề xuất lượng nguyên liệu cần nhập.

#### 2. 📋 AI Smart Scheduling - Đề Xuất Ca Làm
* **Định hướng:** Tự động đối soát biểu đồ lượng khách dự báo với lịch rảnh của nhân viên $\rightarrow$ Đề xuất bảng ca làm việc cân bằng, tránh thừa/thiếu người.

#### 3. 🧑‍🤝‍🧑 AI Churn Prediction - Giữ Chân Khách Hàng
* **Định hướng:** Phân tích tần suất mua hàng để nhận diện khách quen có dấu hiệu ngừng quay lại $\rightarrow$ Kích hoạt gửi ưu đãi riêng qua Zalo OA.

#### 4. 🧋 AI Chatbot NLP Tiếng Việt (`RAG` + `LLM`)
* **Định hướng:** Nhận diện tin nhắn đặt hàng/đặt bàn dạng văn bản tự nhiên của người dùng $\rightarrow$ Bóc tách thông tin và tự động tạo đơn hàng cấu trúc.

#### 5. 🧊 IoT Cảnh Báo Thiết Bị Ban Đêm (`ESP32` + `Sensor`)
* **Định hướng:** Giám sát nhiệt độ tủ lưu trữ nguyên liệu liên tục $\rightarrow$ Tự động gửi cảnh báo khẩn cấp đến Quản lý nếu nhiệt độ tăng bất thường.

#### 6. ⚡ IoT Giám Sát Điện Năng Tiêu Thụ (`Smart Meter`)
* **Định hướng:** Theo dõi điện năng thực tế của từng thiết bị công suất lớn $\rightarrow$ Nhận diện thiết bị hoạt động bất thường để bảo trì kịp thời.

---

## 🌟 ĐIỂM KHÁC BIỆT CỐT LÕI (USP)

* 🔴 **Hệ thống truyền thống:** Tập trung vào **Ghi nhận quá khứ** (chỉ xuất báo cáo thống kê đơn thuần sau khi sự việc đã diễn ra).
* 🟢 **F&B Operating System:** Hướng tới **Dự báo & Tự động hành động** (Chủ động cảnh báo rủi ro, đề xuất phương án và hỗ trợ ra quyết định trước).