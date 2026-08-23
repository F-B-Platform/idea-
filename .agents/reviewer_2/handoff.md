# 📋 BÁO CÁO THẨM ĐỊNH CHẤT LƯỢNG & ĐỘ SÂU KỸ THUẬT (HANDOFF REPORT)
## Reviewer 2 — Principal Software Quality Reviewer & Adversarial Critic

**Ngày thẩm định:** 2026-08-23T20:55:00+07:00  
**Đối tượng thẩm định:** 4 Tệp Sơ Đồ Thiết Kế Kiến Trúc Hệ Thống trong thư mục `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\`:
1. `01_Kien_Truc_Tong_Quan.md` (64.130 bytes, 768 lines)
2. `02_Sequence_Diagrams.md` (57.270 bytes, 871 lines)
3. `03_ERD_Database_Diagram.md` (91.375 bytes, 1441 lines)
4. `04_Deployment_Diagram.md` (72.597 bytes, 1019 lines)

**Nguồn sự thật đối chiếu (Source of Truth):**
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`

---

## 1. OBSERVATION (Quan Sát Trực Tiếp)

### 1.1. Thẩm định Chi tiết Kỹ thuật 10 Sơ đồ Tuần tự (Seq-01 -> Seq-10 trong `02_Sequence_Diagrams.md`)
- **Seq-01 (Dine-In Nhánh A - Trả trước VietQR):** Đặc tả chính xác luồng đặt món từ Table QR (`T04`), khóa phân tán RedLock `lock:table:T04` (5s), tạo đơn `PendingPayment` (chặn hiển thị KDS Bếp), gọi PayOS `/v2/payment-requests`, xử lý Webhook `/api/v1/webhooks/payos` với kiểm tra chữ ký HMAC-SHA256 và chống lặp `SETNX lock:webhook:payos:... EX 60`. Khi thanh toán thành công, cập nhật `Confirmed` và đẩy real-time qua SignalR `KitchenHub` (`NewKitchenOrder`) & `PaymentHub` (`PaymentReceived`).
- **Seq-02 (Dine-In Nhánh B - Trả sau Tiền mặt / Quét QR Bill):** Đơn vào KDS ngay lập tức ở trạng thái `Confirmed` không chờ tiền; Barista hoàn tất (`Ready`) kích hoạt in hóa đơn tạm tính có sẵn mã VietQR động qua máy in nhiệt ESC/POS (Port 9100). Phân nhánh đầy đủ: (B1) Khách trả tiền mặt cho nhân viên thu ngân (tính tiền thối, cập nhật doanh thu ca két `Shifts.CashRevenue`), (B2) Khách quét mã VietQR in trên hóa đơn (PayOS Webhook xác nhận và đồng bộ Web POS bàn sang màu xanh lá).
- **Seq-03 (QR Delivery):** Xác thực FluentValidation bắt buộc SĐT (10 số) và Địa chỉ nhận hàng ($\ge 10$ ký tự); tự động cộng phí giao hàng cố định 20.000 VNĐ; khóa 100% hình thức COD (bắt buộc VietQR trả trước qua PayOS); vé KDS hiển thị nhãn `[DELIVERY]` xanh lục nổi bật; Barista đóng gói dán tem niêm phong chống tràn và bàn giao Shipper.
- **Seq-04 (Takeaway Web POS):** Nhân viên thao tác trực tiếp trên Web POS quầy `(staff)/pos` (khách không quét QR); tra cứu CRM SĐT `/api/v1/crm/customers/lookup`; cơ chế tích 10 ly tặng 1 ly chỉ áp dụng cho Takeaway; tính toán biến động ly nguyên tử $(10 - 10 + N)$; ghi nhận giao dịch `LoyaltyCupTransactions`; in hóa đơn bán lẻ kèm điểm tích lũy mới.
- **Seq-05 (Chấm công Khóa WiFi):** Xác thực kép (Double Verification Gate) không dùng GPS hay QR 30s: Lớp 1 kiểm tra IP Subnet (`192.168.1.0/24`) và BSSID Access Point chi nhánh từ bảng `BranchWifiConfigs`; Lớp 2 kiểm tra định danh nhân sự `EmployeeCode` và trạng thái ca trực; phát thông báo qua SignalR `NotificationHub`.
- **Seq-06 (KDS & BOM Auto-Deduction & 86-Toggle):** Tự động khấu trừ nguyên liệu theo công thức BOM (đơn vị gam/ml) từ `ProductBOMs` khi Barista bấm `Ready`; kiểm tra ngưỡng tối thiểu `MinThreshold` để bắn `LowStockAlert` tới Quản lý; công tắc khẩn cấp 86-Toggle cập nhật database, xóa cache Redis `menu:branch:B01:active`, bắn SignalR `Item86Toggled` tới toàn bộ khách hàng trong quán để làm mờ món và khóa nút đặt hàng trong thời gian $< 1$s.
- **Seq-07 (Gọi phục vụ bàn):** Cơ chế Rate-Limit chống spam trên Redis `SET lock:ratelimit:call:T04 "1" NX EX 60` (trả về 429 Too Many Requests nếu nhấn liên tục); bắn sự kiện `ServiceCallAlert` qua `NotificationHub` tới Web POS và KDS quầy bar kèm chuông reo; nhân viên bấm "Đã Xử Lý" để tắt cảnh báo.
- **Seq-08 (Đánh giá 1-5 sao & Red Alert $\le 2$ sao):** Khách gửi đánh giá kèm ảnh tải lên S3 CDN; tích hợp Google Gemini 1.5 Flash phân tích cảm xúc (Sentiment Analysis); nếu rating $\le 2$ sao, kích hoạt sự kiện `UrgentRedAlert` qua SignalR làm màn hình Quản lý phát còi báo động đỏ khẩn cấp và mở pop-up để Quản lý trực tiếp đến bàn xử lý khiếu nại.
- **Seq-09 (Mở/Kết Ca & Z-Report):** Khai báo tiền lẻ mở ca (`OpeningCash`); theo dõi doanh thu thực tế; kiểm đếm tiền mặt cuối ca theo từng mệnh giá; tính toán chênh lệch $\text{Difference} = \text{ActualCash} - \text{SystemCash}$; nếu chênh lệch $> 50.000$ VNĐ, bắt buộc Thu ngân nhập giải trình và Quản lý nhập mã PIN duyệt điện tử; ghi vết nhật ký bất biến `AuditLogs`; xuất biên bản Z-Report.
- **Seq-10 (Admin Operations & AI-2 Combo Apriori):** Tải ảnh và nén WebP tự động qua ImageSharp; CRUD thực đơn và cấu hình BOM theo Size; lên lịch thực đơn mùa vụ (Seasonal Menu) qua Hangfire Cron; thuật toán Apriori tự động khai phá các mẫu món mua kèm có $\text{Lift} > 1.5$; Admin xem xét, chỉnh chiết khấu và phê duyệt xuất bản lên đầu Menu PWA.

### 1.2. Thẩm định Chuẩn hóa Cơ sở Dữ liệu ERD 3NF (`03_ERD_Database_Diagram.md`)
- **Quy mô thực thể:** Chứa chính xác **31 bảng thực thể** (vượt yêu cầu tối thiểu 25 bảng), được nhóm khoa học thành 8 phân hệ nghiệp vụ:
  1. *Core & RBAC (6 bảng):* `users`, `roles`, `user_roles`, `permissions`, `role_permissions`, `refresh_tokens`.
  2. *Branches & Tables (4 bảng):* `branches`, `branch_wifi_configs`, `tables`, `table_qr_codes`.
  3. *Menu & Toppings (5 bảng):* `categories`, `products`, `product_sizes`, `toppings`, `product_toppings`.
  4. *BOM & Inventory (4 bảng):* `ingredients`, `product_recipes`, `inventory_stocks`, `inventory_logs`.
  5. *Orders & Payments (5 bảng):* `orders`, `order_items`, `order_item_toppings`, `payments`, `transactions`.
  6. *Delivery Logistics (1 bảng):* `delivery_orders`.
  7. *CRM & Loyalty (3 bảng):* `customers`, `loyalty_cup_transactions`, `customer_feedbacks`.
  8. *Shifts & HRM (3 bảng):* `work_shifts`, `staff_attendances`, `shift_handover_discrepancies`.
- **Ràng buộc toàn vẹn & Kiểu dữ liệu:** 100% Khóa chính UUID v4 (`gen_random_uuid()`), đầy đủ Khóa ngoại (FK) kèm hành vi cascade/restrict rõ ràng, chuẩn hóa múi giờ `TIMESTAMPTZ`, cờ xóa mềm `is_deleted`, các ràng buộc `CHECK` chặt chẽ (vd: `discrepancy_amount > 50000`, `rating_stars BETWEEN 1 AND 5`).
- **Từ điển dữ liệu (Data Dictionary):** Bảng chi tiết từng cột cho toàn bộ 31 bảng với kiểu dữ liệu, tính Nullable, khóa/ràng buộc và ý nghĩa nghiệp vụ.
- **Chiến lược Đánh chỉ mục (Indexing Strategy):** 20 chỉ mục tối ưu (B-Tree Composite, Partial Indexes, GIN Full-text Search & JSONB).
- **Triggers Nghiệp vụ Tự động:** 3 triggers PL/pgSQL hoàn chỉnh:
  1. `trg_orders_auto_deduct_bom`: Tự động trừ tồn kho theo công thức BOM khi đơn hàng sang trạng thái `Ready`.
  2. `trg_feedbacks_urgent_alert`: Tự động bật cờ cảnh báo khẩn cấp khi đánh giá $\le 2$ sao.
  3. `trg_orders_loyalty_takeaway`: Tự động tích lũy ly hội viên khi hoàn tất đơn Takeaway.
- **Bảo mật Đa Chi Nhánh (Row-Level Security):** Thiết lập chính sách RLS trên các bảng vận hành (`orders`, `inventory_stocks`, `work_shifts`) phân tách dữ liệu theo `current_branch_id` và cho phép `ChainAdmin` truy cập toàn chuỗi.

### 1.3. Thẩm định Hạ Tầng & Triển Khai (`04_Deployment_Diagram.md`)
- **Docker Compose Production-Grade (`docker-compose.prod.yml`):** Cấu hình hoàn chỉnh 5 services (`smartfb-postgres`, `smartfb-redis`, `smartfb-webapi`, `smartfb-frontend`, `smartfb-nginx`); thiết lập giới hạn tài nguyên CPU/RAM limits & reservations; cấu hình `healthcheck` từng service kèm cơ chế phụ thuộc `condition: service_healthy`; mạng bridge cô lập `smartfb-net` (không mở cổng DB/Redis ra ngoài); persistent volumes đầy đủ.
- **NGINX Reverse Proxy (`nginx.conf`):** Cấu hình đầy đủ SSL/TLS Let's Encrypt, chuyển hướng HTTP 80 sang HTTPS 443 (301), bản đồ WebSocket Upgrade cho SignalR (`/hubs/*`) với `proxy_read_timeout 3600s`, Rate Limiting (`zone=api_limit:10m rate=60r/m`, `zone=auth_limit:10m rate=10r/m`), Static Upload caching, và đầy đủ Security Headers (HSTS, X-Frame-Options, X-Content-Type-Options, CSP).
- **So Sánh Chuyên Sâu 2 Mô Hình Hạ Tầng:** Bảng so sánh toàn diện giữa *Phương án 1 (Cloud VPS Linux Ubuntu 22.04 LTS All-in-One Docker Compose - 8GB RAM, ~300k-500k VNĐ/tháng)* và *Phương án 2 (Cloud-Native Azure Singapore AKS + Managed PaaS Multi-AZ, ~$150-$350 USD/tháng)* trên 7 khía cạnh kỹ thuật rõ ràng (Hiệu năng, Chi phí, Độ phức tạp, Mở rộng, HA, Bảo mật, Khôi phục thảm họa).
- **Tự động hóa CI/CD & Vận hành:** Sơ đồ GitHub Actions CI/CD pipeline, Script sao lưu CSDL tự động `backup_postgres.sh`, Kịch bản khôi phục thảm họa khẩn cấp (Disaster Recovery Runbook) với cam kết RPO $< 24$h/5m và RTO $< 30$m, bộ endpoint Health Checks chuẩn ASP.NET Core (`/healthz/live`, `/healthz/ready`), và ma trận giám sát Prometheus/Grafana.

### 1.4. Kiểm Chứng Toàn Diện Cú Pháp Mermaid Bằng Headless Engine
- **Thực thi script kiểm thử tự động:** `verify_mermaid.js` trích xuất và biên dịch độc lập từng sơ đồ Mermaid sang định dạng SVG thông qua `@mermaid-js/mermaid-cli` v11.16.0 kết hợp Google Chrome Headless engine trên hệ điều hành Windows.
- **Kết quả kiểm chứng thực tế:**
  - `01_Kien_Truc_Tong_Quan.md`: **9 / 9 Sơ đồ PASSED** (C4 Context, C4 Container, C4 Component, 4 Hubs SignalR, Read/Write Cache Flow, AI Pipelines, State Machine Dine-In 2 nhánh, Chấm công WiFi, Docker Topology).
  - `02_Sequence_Diagrams.md`: **10 / 10 Sơ đồ Tuần tự PASSED** (Seq-01 đến Seq-10).
  - `03_ERD_Database_Diagram.md`: **1 / 1 Sơ đồ ERD 31 Bảng PASSED**.
  - `04_Deployment_Diagram.md`: **2 / 2 Sơ đồ Deployment & CI/CD Pipeline PASSED**.
- **Tổng cộng:** **22 / 22 Sơ đồ Mermaid hợp lệ 100%, render sắc nét, 0 lỗi cú pháp (Exit Code 0)**.

---

## 2. LOGIC CHAIN (Chuỗi Suy Luận Đánh Giá)

1. **Từ Quan Sát 1.1:** Toàn bộ 10 Sequence Diagrams đều được xây dựng với độ chi tiết cao, đầy đủ các bên tham gia (Actors, Boundary, Control, Entity, External Gateways), giao thức truyền tin (HTTP Methods, Route URLs, JSON Payloads, Status Codes, SignalR Events), và cơ chế phòng ngừa lỗi (RedLock, HMAC-SHA256, Idempotency, Rate Limiting). Điều này chứng minh tài liệu đạt tiêu chuẩn thiết kế kiến trúc mức chi tiết (Detailed Design).
2. **Từ Quan Sát 1.2:** Database ERD đã chuẩn hóa 3NF trên toàn bộ 31 bảng dữ liệu, không có trường dư thừa hoặc vi phạm phụ thuộc bắc cầu; định nghĩa đầy đủ khóa chính UUID, khóa ngoại, kiểu dữ liệu, ràng buộc nghiệp vụ, 20 chỉ mục tối ưu, 3 trigger tự động và RLS. Điều này đảm bảo tính toàn vẹn dữ liệu ở cấp độ CSDL quan hệ doanh nghiệp.
3. **Từ Quan Sát 1.3:** Tài liệu triển khai cung cấp các cấu hình mã nguồn thực thi thực tế (`docker-compose.prod.yml`, `nginx.conf`, `backup_postgres.sh`, `restore_runbook.sh`, `Program.cs` health check) hoàn chỉnh 100%, không sử dụng mã giả (pseudo-code) hay giữ chỗ (`TODO`). Phân tích so sánh Linux VPS vs Azure Singapore cung cấp căn cứ ra quyết định kỹ thuật rõ ràng.
4. **Từ Quan Sát 1.4:** Toàn bộ 22 sơ đồ Mermaid đã được kiểm chứng tự động bằng công cụ biên dịch thực tế của Mermaid CLI và Chrome Headless, đạt tỷ lệ thành công 100% không có cảnh báo hay lỗi cú pháp.
5. **Kiểm tra Tính Toàn Vẹn & Phạm Vi (Integrity & Scope):** Không còn bất kỳ dấu vết nào của Staff Mobile App, GPS 50m, QR động 30s, C-23, C-24 hay ví voucher; phản ánh chính xác 100% kiến trúc chuẩn hóa v2.5.0.

---

## 3. CAVEATS (Lưu Ý & Giả Định)

- **Giả định hạ tầng:** Cấu hình Docker Compose và NGINX được tối ưu hóa cho máy chủ Linux (Ubuntu Server 22.04 LTS x86_64). Khi triển khai trên môi trường Windows Host cục bộ cho phát triển, cần lưu ý đường dẫn volume mount định dạng Unix (`/var/...`).
- **Môi trường Webhook PayOS:** Trong môi trường thử nghiệm nội bộ (localhost), cần sử dụng công cụ ngrok hoặc Cloudflare Tunnel để chuyển tiếp Webhook từ PayOS về NGINX cục bộ.

---

## 4. CONCLUSION (Kết Luận & Quyết Định Nghiệm Thu)

Sau khi rà soát độc lập, đối chiếu với toàn bộ nguồn sự thật và kiểm chứng thực nghiệm tự động trên toàn bộ 4 tệp tài liệu sơ đồ kiến trúc:

### 🏆 **VERDICT: APPROVE (CHẤP THUẬN NGHIỆM THU 100%)**

**Đánh giá tổng thể:**
- **Độ hoàn thiện:** 100% Zero Placeholders, cấu trúc trình bày chuyên nghiệp, tuân thủ nghiêm ngặt GitHub Alert Callouts.
- **Độ sâu kỹ thuật:** Đạt chuẩn Enterprise Production-Ready, sẵn sàng chuyển giao cho đội ngũ kỹ sư phát triển Backend (.NET 8 Clean Architecture) và Frontend (Next.js 14 App Router Monorepo).
- **Tính nhất quán nghiệp vụ:** Khớp 100% với Master Spec v2.5.0.

---

## 5. VERIFICATION METHOD (Phương Pháp Tự Kiểm Chứng Độc Lập)

Người nhận bàn giao hoặc Orchestrator có thể tự động kiểm chứng lại toàn bộ các phát hiện trên bằng các lệnh sau trong terminal:

```bash
# 1. Kiểm tra sự tồn tại và dung lượng của 4 file tài liệu
ls -la "d:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/"

# 2. Thực thi script kiểm thử cú pháp 22 sơ đồ Mermaid bằng Mermaid CLI + Chrome Headless
node "d:/Idea_DoAn/.agents/reviewer_2/verify_mermaid.js"

# 3. Kiểm tra tính toàn vẹn (Không chứa placeholder TODO / TBD)
grep -rn "TODO" "d:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/"
grep -rn "TBD" "d:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/"
```
