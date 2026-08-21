# TÀI LIỆU ĐẶC TẢ CHI TIẾT API CONTRACT & SIGNALR REAL-TIME HUBS

**Hệ thống**: Smart F&B Operating System  
**Phiên bản**: v1.0.0 (Production Grade)  
**Mã tài liệu**: `03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET`  
**Đường dẫn đích**: `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_QUY_TRINH_THIET_KE_API_CONTRACT_CHI_TIET.md`  
**Trạng thái**: Đã phê duyệt & Sẵn sàng triển khai Backend (.NET 8 Web API & SignalR Hubs)

---

## 1. TỔNG QUAN HỆ THỐNG & NGUYÊN TẮC THIẾT KẾ API CONTRACT

### 1.1 Nguyên tắc kiến trúc & Chuẩn giao tiếp
1. **Chuẩn RESTful API**: Định dạng dữ liệu trao đổi duy nhất là JSON UTF-8. Tất cả tên thuộc tính (properties) tuân thủ quy tắc `camelCase`. Tất cả tài nguyên URL tuân thủ `kebab-case`.
2. **Kiến trúc Real-time SignalR Hubs**: Hệ thống tích hợp 4 SignalR Hubs chính trên nền WebSocket để cập nhật trạng thái đơn hàng, gọi món tại bàn, chế biến KDS và thanh toán VietQR thời gian thực.
3. **Chuẩn báo lỗi RFC 7807 (ProblemDetails)**: Tất cả mã phản hồi lỗi HTTP 4xx và 5xx bắt buộc tuân thủ cấu trúc chuẩn RFC 7807.
4. **Cơ chế xác thực & Phân quyền (RBAC)**:
   - Sử dụng JWT Access Token (hạn 8 giờ) và Refresh Token (hạn 30 ngày).
   - Truyền token qua HTTP Header: `Authorization: Bearer <JWT_TOKEN>`.
   - Kết nối SignalR WebSocket truyền token qua query string: `?access_token=<JWT_TOKEN>`.

### 1.2 Schema Lỗi Chuẩn RFC 7807 (ProblemDetails)
Dữ liệu phản hồi cho tất cả các mã lỗi (400, 401, 403, 404, 409, 422, 500) có cấu trúc chuẩn như sau:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ProblemDetails",
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "format": "uri",
      "description": "Đường dẫn URI tham chiếu đến tài liệu chi tiết của mã lỗi",
      "example": "https://api.smartfb.vn/errors/invalid-order-state"
    },
    "title": {
      "type": "string",
      "description": "Tiêu đề lỗi ngắn gọn",
      "example": "Trạng thái đơn hàng không hợp lệ"
    },
    "status": {
      "type": "integer",
      "description": "Mã trạng thái HTTP",
      "example": 400
    },
    "detail": {
      "type": "string",
      "description": "Mô tả chi tiết nguyên nhân phát sinh lỗi",
      "example": "Không thể thêm món vào đơn hàng đã hoàn tất thanh toán hoặc đã hủy."
    },
    "instance": {
      "type": "string",
      "description": "Đường dẫn endpoint phát sinh lỗi",
      "example": "/api/v1/orders/ord-88321/items"
    },
    "invalidParams": {
      "type": "array",
      "description": "Danh sách các tham số không hợp lệ (nếu có)",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string", "example": "orderStatus" },
          "reason": { "type": "string", "example": "Trạng thái hiện tại là Completed" }
        },
        "required": ["name", "reason"]
      }
    }
  },
  "required": ["type", "title", "status", "detail", "instance"]
}
```

---

## 2. CHUYÊN MỤC DỊCH VỤ RESTFUL API (64 ENDPOINTS)

### Module 1: Auth & Identity Management (6 Endpoints)

### POST /api/v1/auth/login
- **Mô tả**: Đăng nhập hệ thống dành cho Nhân viên (Thu ngân, Phục vụ, Bếp) và Quản lý cửa hàng bằng Username và Password. Trả về cặp JWT Access Token và Refresh Token.
- **Quyền truy cập**: Public (Anonymous)
- **Path Parameters**: Không có
- **Query Parameters**: Không có
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "username": { "type": "string", "minLength": 3, "maxLength": 50, "example": "cashier_quan1" },
    "password": { "type": "string", "format": "password", "minLength": 6, "example": "SecurePass123!" },
    "storeId": { "type": "string", "format": "uuid", "example": "str-8832-491a-9012" }
  },
  "required": ["username", "password", "storeId"]
}
```
*Payload ví dụ*:
```json
{
  "username": "cashier_quan1",
  "password": "SecurePass123!",
  "storeId": "str-8832-491a-9012"
}
```
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "accessToken": { "type": "string", "example": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3ItMTAwMiIsIm5hbWUiOiJOZ3V5ZW4gVmFuIEEiLCJyb2xlIjoiQ2FzaGllciIsImlhdCI6MTcxODkwMDAwMH0.signature" },
    "refreshToken": { "type": "string", "example": "ref-994821-abcf-4821-9901" },
    "expiresIn": { "type": "integer", "example": 28800 },
    "user": {
      "type": "object",
      "properties": {
        "userId": { "type": "string", "example": "usr-1002" },
        "username": { "type": "string", "example": "cashier_quan1" },
        "fullName": { "type": "string", "example": "Nguyễn Văn A" },
        "role": { "type": "string", "example": "Cashier" },
        "storeId": { "type": "string", "example": "str-8832-491a-9012" },
        "storeName": { "type": "string", "example": "Smart F&B Chi nhánh Quận 1" }
      },
      "required": ["userId", "username", "fullName", "role", "storeId", "storeName"]
    }
  },
  "required": ["accessToken", "refreshToken", "expiresIn", "user"]
}
```
- **Phản hồi lỗi (ProblemDetails)**:
  - 400 Bad Request: Sai thông tin đăng nhập hoặc thiếu thông tin bắt buộc.
  - 401 Unauthorized: Username/Password không chính xác hoặc tài khoản bị khóa.
  - 403 Forbidden: Tài khoản không có quyền truy cập vào cửa hàng `storeId` được chỉ định.

### POST /api/v1/auth/customer-checkin
- **Mô tả**: Khách hàng quét mã QR tại bàn gọi món PWA. Xác thực Token trên QR bàn và thông tin số điện thoại khách hàng (tùy chọn) để tạo phiên gọi món.
- **Quyền truy cập**: Public (Anonymous Guest)
- **Path Parameters**: Không có
- **Query Parameters**: Không có
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "qrToken": { "type": "string", "example": "qrtk-table12-sec99812" },
    "tableId": { "type": "string", "format": "uuid", "example": "tbl-0012-4821" },
    "customerPhone": { "type": "string", "pattern": "^0[0-9]{9}$", "example": "0908123456" },
    "customerName": { "type": "string", "example": "Anh Minh" }
  },
  "required": ["qrToken", "tableId"]
}
```
*Payload ví dụ*:
```json
{
  "qrToken": "qrtk-table12-sec99812",
  "tableId": "tbl-0012-4821",
  "customerPhone": "0908123456",
  "customerName": "Anh Minh"
}
```
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "guestToken": { "type": "string", "example": "guest-token-session-88219" },
    "sessionId": { "type": "string", "example": "ses-9981-1209" },
    "tableId": { "type": "string", "example": "tbl-0012-4821" },
    "tableName": { "type": "string", "example": "Bàn 12" },
    "areaName": { "type": "string", "example": "Tầng 1 - Sân Thượng" },
    "activeOrderId": { "type": "string", "nullable": true, "example": "ord-88321" }
  },
  "required": ["guestToken", "sessionId", "tableId", "tableName", "areaName"]
}
```
- **Phản hồi lỗi**:
  - 400 Bad Request: Mã QR hết hạn hoặc bàn đang ở trạng thái ngừng phục vụ.
  - 404 Not Found: Bàn ăn không tồn tại trong hệ thống.

### POST /api/v1/auth/refresh-token
- **Mô tả**: Cấp lại JWT Access Token mới khi token cũ hết hạn bằng cách sử dụng Refresh Token hợp lệ.
- **Quyền truy cập**: Public (Anonymous)
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "refreshToken": { "type": "string", "example": "ref-994821-abcf-4821-9901" }
  },
  "required": ["refreshToken"]
}
```
*Payload ví dụ*:
```json
{
  "refreshToken": "ref-994821-abcf-4821-9901"
}
```
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "accessToken": { "type": "string", "example": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.newtoken.signature" },
    "refreshToken": { "type": "string", "example": "ref-100293-xyz-9912" },
    "expiresIn": { "type": "integer", "example": 28800 }
  },
  "required": ["accessToken", "refreshToken", "expiresIn"]
}
```
- **Phản hồi lỗi**:
  - 401 Unauthorized: Refresh Token hết hạn hoặc không hợp lệ.

### POST /api/v1/auth/logout
- **Mô tả**: Đăng xuất tài khoản, thu hồi (revoke) Refresh Token và hủy phiên làm việc.
- **Quyền truy cập**: Authenticated (Bearer Token)
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "refreshToken": { "type": "string", "example": "ref-994821-abcf-4821-9901" }
  },
  "required": ["refreshToken"]
}
```
*Payload ví dụ*:
```json
{
  "refreshToken": "ref-994821-abcf-4821-9901"
}
```
- **Response 200 OK**:
```json
{
  "message": "Đăng xuất thành công và đã thu hồi phiên đăng nhập."
}
```
- **Phản hồi lỗi**:
  - 401 Unauthorized: Token không hợp lệ.

### GET /api/v1/auth/me
- **Mô tả**: Lấy thông tin tài khoản đang đăng nhập, danh sách quyền RBAC và cửa hàng phụ trách.
- **Quyền truy cập**: Authenticated
- **Path Parameters**: Không có
- **Query Parameters**: Không có
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "userId": { "type": "string", "example": "usr-1002" },
    "username": { "type": "string", "example": "cashier_quan1" },
    "fullName": { "type": "string", "example": "Nguyễn Văn A" },
    "email": { "type": "string", "example": "nguyenvana@smartfb.vn" },
    "role": { "type": "string", "example": "Cashier" },
    "permissions": {
      "type": "array",
      "items": { "type": "string" },
      "example": ["Order.Create", "Order.Read", "Payment.Process", "Table.Read"]
    },
    "storeId": { "type": "string", "example": "str-8832-491a-9012" }
  },
  "required": ["userId", "username", "fullName", "role", "permissions", "storeId"]
}
```
- **Phản hồi lỗi**:
  - 401 Unauthorized: Thiếu hoặc hết hạn JWT Bearer Token.

### POST /api/v1/auth/change-password
- **Mô tả**: Đổi mật khẩu tài khoản người dùng/nhân viên.
- **Quyền truy cập**: Authenticated
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "currentPassword": { "type": "string", "example": "SecurePass123!" },
    "newPassword": { "type": "string", "minLength": 6, "example": "NewStrongPass456!" }
  },
  "required": ["currentPassword", "newPassword"]
}
```
*Payload ví dụ*:
```json
{
  "currentPassword": "SecurePass123!",
  "newPassword": "NewStrongPass456!"
}
```
- **Response 200 OK**:
```json
{
  "message": "Đổi mật khẩu thành công."
}
```
- **Phản hồi lỗi**:
  - 400 Bad Request: Mật khẩu cũ không chính xác hoặc mật khẩu mới không đáp ứng chính sách an toàn.

---

### Module 2: Tenant & Store Branch Management (6 Endpoints)

### GET /api/v1/stores
- **Mô tả**: Lấy danh sách các cửa hàng/chi nhánh thuộc hệ thống theo Tenant.
- **Quyền truy cập**: SystemAdmin, StoreManager
- **Query Parameters**:
  - `status` (optional, string): Lọc theo trạng thái (`Active`, `Inactive`, `Busy`).
  - `page` (optional, integer): Số trang (mặc định 1).
  - `pageSize` (optional, integer): Số lượng/trang (mặc định 20).
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "totalCount": { "type": "integer", "example": 2 },
    "page": { "type": "integer", "example": 1 },
    "pageSize": { "type": "integer", "example": 20 },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "storeId": { "type": "string", "example": "str-8832-491a-9012" },
          "storeCode": { "type": "string", "example": "ST-Q1" },
          "name": { "type": "string", "example": "Smart F&B Chi nhánh Quận 1" },
          "address": { "type": "string", "example": "123 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP.HCM" },
          "phone": { "type": "string", "example": "02838229999" },
          "status": { "type": "string", "example": "Active" },
          "openedAt": { "type": "string", "example": "07:00" },
          "closedAt": { "type": "string", "example": "23:00" }
        },
        "required": ["storeId", "storeCode", "name", "address", "phone", "status"]
      }
    }
  },
  "required": ["totalCount", "page", "pageSize", "items"]
}
```
- **Phản hồi lỗi**:
  - 401 Unauthorized: Chưa xác thực.
  - 403 Forbidden: Không có quyền quản trị chi nhánh.

### POST /api/v1/stores
- **Mô tả**: Khởi tạo một cửa hàng/chi nhánh mới trong hệ thống.
- **Quyền truy cập**: SystemAdmin
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeCode": { "type": "string", "example": "ST-Q3" },
    "name": { "type": "string", "example": "Smart F&B Chi nhánh Quận 3" },
    "address": { "type": "string", "example": "456 Võ Văn Tần, Phường 5, Quận 3, TP.HCM" },
    "phone": { "type": "string", "example": "02839301111" },
    "taxCode": { "type": "string", "example": "0312345678" },
    "serviceChargePercent": { "type": "number", "example": 5.0 },
    "vatPercent": { "type": "number", "example": 8.0 }
  },
  "required": ["storeCode", "name", "address", "phone", "taxCode"]
}
```
*Payload ví dụ*:
```json
{
  "storeCode": "ST-Q3",
  "name": "Smart F&B Chi nhánh Quận 3",
  "address": "456 Võ Văn Tần, Phường 5, Quận 3, TP.HCM",
  "phone": "02839301111",
  "taxCode": "0312345678",
  "serviceChargePercent": 5.0,
  "vatPercent": 8.0
}
```
- **Response 201 Created (JSON Schema)**:
```json
{
  "storeId": "str-9921-771a-3301",
  "storeCode": "ST-Q3",
  "name": "Smart F&B Chi nhánh Quận 3",
  "status": "Active",
  "createdAt": "2026-08-13T16:00:00Z"
}
```
- **Phản hồi lỗi**:
  - 400 Bad Request: Dữ liệu không hợp lệ.
  - 409 Conflict: Mã cửa hàng `storeCode` đã tồn tại.

### GET /api/v1/stores/{storeId}
- **Mô tả**: Lấy thông tin chi tiết cấu hình và hồ sơ của một cửa hàng cụ thể.
- **Quyền truy cập**: SystemAdmin, StoreManager, ShiftLeader
- **Path Parameters**:
  - `storeId` (string, required): Mã GUID duy nhất của cửa hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "storeCode": { "type": "string", "example": "ST-Q1" },
    "name": { "type": "string", "example": "Smart F&B Chi nhánh Quận 1" },
    "address": { "type": "string", "example": "123 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP.HCM" },
    "phone": { "type": "string", "example": "02838229999" },
    "taxCode": { "type": "string", "example": "0312345678" },
    "serviceChargePercent": { "type": "number", "example": 5.0 },
    "vatPercent": { "type": "number", "example": 8.0 },
    "status": { "type": "string", "example": "Active" },
    "receiptFooterText": { "type": "string", "example": "Cảm ơn quý khách và hẹn gặp lại!" }
  },
  "required": ["storeId", "storeCode", "name", "address", "phone", "taxCode", "status"]
}
```
- **Phản hồi lỗi**:
  - 404 Not Found: Không tìm thấy cửa hàng.

### PUT /api/v1/stores/{storeId}
- **Mô tả**: Cập nhật thông tin kinh doanh, địa chỉ và thuế suất của cửa hàng.
- **Quyền truy cập**: SystemAdmin, StoreManager
- **Path Parameters**:
  - `storeId` (string, required): Mã GUID duy nhất của cửa hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string", "example": "Smart F&B Chi nhánh Nguyễn Huệ Quận 1" },
    "address": { "type": "string", "example": "123 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP.HCM" },
    "phone": { "type": "string", "example": "02838229999" },
    "serviceChargePercent": { "type": "number", "example": 5.0 },
    "vatPercent": { "type": "number", "example": 8.0 },
    "receiptFooterText": { "type": "string", "example": "Hân hạnh được phục vụ quý khách!" }
  },
  "required": ["name", "address", "phone", "serviceChargePercent", "vatPercent"]
}
```
*Payload ví dụ*:
```json
{
  "name": "Smart F&B Chi nhánh Nguyễn Huệ Quận 1",
  "address": "123 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP.HCM",
  "phone": "02838229999",
  "serviceChargePercent": 5.0,
  "vatPercent": 8.0,
  "receiptFooterText": "Hân hạnh được phục vụ quý khách!"
}
```
- **Response 200 OK**:
```json
{
  "storeId": "str-8832-491a-9012",
  "name": "Smart F&B Chi nhánh Nguyễn Huệ Quận 1",
  "updatedAt": "2026-08-13T16:05:00Z"
}
```
- **Phản hồi lỗi**:
  - 400 Bad Request: Dữ liệu không hợp lệ.
  - 404 Not Found: Không tìm thấy cửa hàng.

### PATCH /api/v1/stores/{storeId}/status
- **Mô tả**: Thao tác đóng/mở cửa hoặc chuyển trạng thái hoạt động của cửa hàng.
- **Quyền truy cập**: StoreManager
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "status": { "type": "string", "enum": ["Active", "Inactive", "Busy"], "example": "Busy" },
    "reason": { "type": "string", "example": "Quá tải giờ cao điểm, tạm ngưng nhận đơn PWA" }
  },
  "required": ["status"]
}
```
*Payload ví dụ*:
```json
{
  "status": "Busy",
  "reason": "Quá tải giờ cao điểm, tạm ngưng nhận đơn PWA"
}
```
- **Response 200 OK**:
```json
{
  "storeId": "str-8832-491a-9012",
  "status": "Busy",
  "updatedAt": "2026-08-13T16:06:00Z"
}
```
- **Phản hồi lỗi**:
  - 400 Bad Request: Trạng thái không thuộc enum quy định.

### GET /api/v1/stores/{storeId}/settings
- **Mô tả**: Lấy chi tiết cài đặt phần cứng và tích hợp (Sunmi POS IP, VietQR credentials, KDS printer routes).
- **Quyền truy cập**: StoreManager, ShiftLeader
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "sunmiPosIp": { "type": "string", "example": "192.168.1.150" },
    "vietQrBankId": { "type": "string", "example": "970436" },
    "vietQrAccountNo": { "type": "string", "example": "0001882199201" },
    "vietQrAccountName": { "type": "string", "example": "CONG TY SMART FB VIET NAM" },
    "kdsHotKitchenPrinterIp": { "type": "string", "example": "192.168.1.201" },
    "kdsBarPrinterIp": { "type": "string", "example": "192.168.1.202" },
    "autoAcceptOrder": { "type": "boolean", "example": false }
  },
  "required": ["storeId", "vietQrBankId", "vietQrAccountNo", "vietQrAccountName"]
}
```
- **Phản hồi lỗi**:
  - 404 Not Found: Không tìm thấy cài đặt cho cửa hàng.

---

### Module 3: Dining Area & Table Management (6 Endpoints)

### GET /api/v1/stores/{storeId}/areas
- **Mô tả**: Lấy danh sách các khu vực/tầng ăn uống trong cửa hàng.
- **Quyền truy cập**: Authenticated Staff, Customer Guest
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "areaId": { "type": "string", "example": "area-floor1-001" },
      "storeId": { "type": "string", "example": "str-8832-491a-9012" },
      "name": { "type": "string", "example": "Tầng 1 - Trong Nhà" },
      "displayOrder": { "type": "integer", "example": 1 },
      "tableCount": { "type": "integer", "example": 15 }
    },
    "required": ["areaId", "storeId", "name", "displayOrder", "tableCount"]
  }
}
```

### POST /api/v1/stores/{storeId}/areas
- **Mô tả**: Thêm mới khu vực ăn uống vào chi nhánh cửa hàng.
- **Quyền truy cập**: StoreManager
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string", "example": "Tầng 2 - Phòng VIP" },
    "displayOrder": { "type": "integer", "example": 2 }
  },
  "required": ["name", "displayOrder"]
}
```
*Payload ví dụ*:
```json
{
  "name": "Tầng 2 - Phòng VIP",
  "displayOrder": 2
}
```
- **Response 201 Created**:
```json
{
  "areaId": "area-floor2-vip",
  "storeId": "str-8832-491a-9012",
  "name": "Tầng 2 - Phòng VIP",
  "displayOrder": 2,
  "tableCount": 0
}
```

### GET /api/v1/stores/{storeId}/tables
- **Mô tả**: Lấy danh sách sơ đồ bàn ăn cùng trạng thái thời gian thực (`Available`, `Occupied`, `Reserved`, `Cleaning`, `BillRequested`).
- **Quyền truy cập**: Authenticated Staff, Customer Guest
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
- **Query Parameters**:
  - `areaId` (optional, string): Lọc theo khu vực.
  - `status` (optional, string): Lọc theo trạng thái bàn.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "tableId": { "type": "string", "example": "tbl-0012-4821" },
      "tableName": { "type": "string", "example": "Bàn 12" },
      "areaId": { "type": "string", "example": "area-floor1-001" },
      "areaName": { "type": "string", "example": "Tầng 1 - Trong Nhà" },
      "capacity": { "type": "integer", "example": 4 },
      "status": { "type": "string", "example": "Occupied" },
      "activeOrderId": { "type": "string", "nullable": true, "example": "ord-88321" },
      "occupiedAt": { "type": "string", "nullable": true, "example": "2026-08-13T15:30:00Z" }
    },
    "required": ["tableId", "tableName", "areaId", "areaName", "capacity", "status"]
  }
}
```

### POST /api/v1/stores/{storeId}/tables
- **Mô tả**: Tạo bàn ăn mới trong một khu vực đã chọn.
- **Quyền truy cập**: StoreManager
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "tableName": { "type": "string", "example": "Bàn 16" },
    "areaId": { "type": "string", "example": "area-floor1-001" },
    "capacity": { "type": "integer", "minimum": 1, "example": 6 }
  },
  "required": ["tableName", "areaId", "capacity"]
}
```
*Payload ví dụ*:
```json
{
  "tableName": "Bàn 16",
  "areaId": "area-floor1-001",
  "capacity": 6
}
```
- **Response 201 Created**:
```json
{
  "tableId": "tbl-0016-9901",
  "tableName": "Bàn 16",
  "areaId": "area-floor1-001",
  "capacity": 6,
  "status": "Available"
}
```

### PATCH /api/v1/stores/{storeId}/tables/{tableId}/status
- **Mô tả**: Cập nhật trạng thái bàn ăn (vd: dọn dẹp xong -> `Available`, khóa bàn -> `Reserved`).
- **Quyền truy cập**: Authenticated Staff (Cashier, Waiter, Manager)
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
  - `tableId` (string, required): Mã bàn ăn.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "status": { "type": "string", "enum": ["Available", "Occupied", "Reserved", "Cleaning", "BillRequested"], "example": "Available" }
  },
  "required": ["status"]
}
```
*Payload ví dụ*:
```json
{
  "status": "Available"
}
```
- **Response 200 OK**:
```json
{
  "tableId": "tbl-0012-4821",
  "status": "Available",
  "updatedAt": "2026-08-13T16:08:00Z"
}
```

### GET /api/v1/stores/{storeId}/tables/{tableId}/qr
- **Mô tả**: Tạo chuỗi dữ liệu mã QR động và URL token gọi món tại bàn cho khách hàng.
- **Quyền truy cập**: StoreManager, Cashier
- **Path Parameters**:
  - `storeId` (string, required): Mã cửa hàng.
  - `tableId` (string, required): Mã bàn ăn.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "tableId": { "type": "string", "example": "tbl-0012-4821" },
    "tableName": { "type": "string", "example": "Bàn 12" },
    "qrToken": { "type": "string", "example": "qrtk-table12-sec99812" },
    "qrUrl": { "type": "string", "example": "https://menu.smartfb.vn/checkin?token=qrtk-table12-sec99812&table=tbl-0012-4821" },
    "expiresAt": { "type": "string", "example": "2026-12-31T23:59:59Z" }
  },
  "required": ["tableId", "tableName", "qrToken", "qrUrl"]
}
```

---

### Module 4: Menu & Category Management (8 Endpoints)

### GET /api/v1/categories
- **Mô tả**: Lấy cây danh mục thực đơn (Cà phê, Trà sữa, Món chính, Tráng miệng).
- **Quyền truy cập**: Public (Anonymous Guest), Staff
- **Query Parameters**:
  - `storeId` (optional, string): Mã cửa hàng để lọc danh mục khả dụng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "categoryId": { "type": "string", "example": "cat-coffee-01" },
      "name": { "type": "string", "example": "Cà Phê Truyền Thống" },
      "displayOrder": { "type": "integer", "example": 1 },
      "iconUrl": { "type": "string", "example": "https://cdn.smartfb.vn/icons/coffee.png" },
      "isActive": { "type": "boolean", "example": true }
    },
    "required": ["categoryId", "name", "displayOrder", "isActive"]
  }
}
```

### POST /api/v1/categories
- **Mô tả**: Tạo mới một danh mục món ăn trong thực đơn.
- **Quyền truy cập**: StoreManager
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string", "example": "Trà Trái Cây & Soda" },
    "displayOrder": { "type": "integer", "example": 3 },
    "iconUrl": { "type": "string", "example": "https://cdn.smartfb.vn/icons/fruit-tea.png" }
  },
  "required": ["name", "displayOrder"]
}
```
*Payload ví dụ*:
```json
{
  "name": "Trà Trái Cây & Soda",
  "displayOrder": 3,
  "iconUrl": "https://cdn.smartfb.vn/icons/fruit-tea.png"
}
```
- **Response 201 Created**:
```json
{
  "categoryId": "cat-tea-03",
  "name": "Trà Trái Cây & Soda",
  "displayOrder": 3,
  "isActive": true
}
```

### PUT /api/v1/categories/{categoryId}
- **Mô tả**: Cập nhật thông tin danh mục thực đơn.
- **Quyền truy cập**: StoreManager
- **Path Parameters**:
  - `categoryId` (string, required): Mã danh mục.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string", "example": "Trà Trái Cây Tươi & Soda" },
    "displayOrder": { "type": "integer", "example": 3 },
    "iconUrl": { "type": "string", "example": "https://cdn.smartfb.vn/icons/fruit-tea-new.png" },
    "isActive": { "type": "boolean", "example": true }
  },
  "required": ["name", "displayOrder", "isActive"]
}
```
*Payload ví dụ*:
```json
{
  "name": "Trà Trái Cây Tươi & Soda",
  "displayOrder": 3,
  "iconUrl": "https://cdn.smartfb.vn/icons/fruit-tea-new.png",
  "isActive": true
}
```
- **Response 200 OK**:
```json
{
  "categoryId": "cat-tea-03",
  "name": "Trà Trái Cây Tươi & Soda",
  "updatedAt": "2026-08-13T16:10:00Z"
}
```

### DELETE /api/v1/categories/{categoryId}
- **Mô tả**: Xóa mềm (soft-delete) một danh mục thực đơn.
- **Quyền truy cập**: StoreManager
- **Path Parameters**:
  - `categoryId` (string, required): Mã danh mục.
- **Response 204 No Content**
- **Phản hồi lỗi**:
  - 409 Conflict: Danh mục còn chứa món ăn active, không thể xóa.

### GET /api/v1/menu/items
- **Mô tả**: Truy vấn danh sách món ăn/đồ uống theo danh mục, từ khóa tìm kiếm và cờ tạm hết hàng (86).
- **Quyền truy cập**: Public (Anonymous Guest), Staff
- **Query Parameters**:
  - `categoryId` (optional, string): Lọc theo danh mục.
  - `search` (optional, string): Từ khóa tìm kiếm tên món.
  - `isAvailable` (optional, boolean): Lọc theo trạng thái có sẵn.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "itemId": { "type": "string", "example": "item-cf-001" },
      "categoryId": { "type": "string", "example": "cat-coffee-01" },
      "name": { "type": "string", "example": "Cà Phê Sữa Đá Sài Gòn" },
      "description": { "type": "string", "example": "Cà phê đậm đà kết hợp sữa đặc Ngôi Sao Phương Nam" },
      "basePrice": { "type": "number", "example": 35000 },
      "imageUrl": { "type": "string", "example": "https://cdn.smartfb.vn/dishes/cf-sua-da.jpg" },
      "isAvailable": { "type": "boolean", "example": true },
      "modifiers": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "modifierId": { "type": "string", "example": "mod-sugar-01" },
            "name": { "type": "string", "example": "Mức đường" },
            "options": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "optionId": { "type": "string", "example": "opt-s100" },
                  "name": { "type": "string", "example": "100% Đường" },
                  "extraPrice": { "type": "number", "example": 0 }
                },
                "required": ["optionId", "name", "extraPrice"]
              }
            }
          },
          "required": ["modifierId", "name", "options"]
        }
      }
    },
    "required": ["itemId", "categoryId", "name", "basePrice", "isAvailable"]
  }
}
```

### POST /api/v1/menu/items
- **Mô tả**: Tạo món ăn/đồ uống mới trong hệ thống thực đơn.
- **Quyền truy cập**: StoreManager
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "categoryId": { "type": "string", "example": "cat-coffee-01" },
    "name": { "type": "string", "example": "Bac Xiu Da Macchiato" },
    "description": { "type": "string", "example": "Bạc xỉu 3 tầng kết hợp lớp kem béo macchiato" },
    "basePrice": { "type": "number", "minimum": 0, "example": 45000 },
    "imageUrl": { "type": "string", "example": "https://cdn.smartfb.vn/dishes/bac-xiu-macchiato.jpg" }
  },
  "required": ["categoryId", "name", "basePrice"]
}
```
*Payload ví dụ*:
```json
{
  "categoryId": "cat-coffee-01",
  "name": "Bac Xiu Da Macchiato",
"description": "Bạc xỉu 3 tầng kết hợp lớp kem béo macchiato",
  "basePrice": 45000,
  "imageUrl": "https://cdn.smartfb.vn/dishes/bac-xiu-macchiato.jpg"
}
```
- **Response 201 Created**:
```json
{
  "itemId": "item-cf-009",
  "name": "Bac Xiu Da Macchiato",
  "basePrice": 45000,
  "isAvailable": true
}
```

### PUT /api/v1/menu/items/{itemId}
- **Mô tả**: Cập nhật thông tin chi tiết, giá bán và tùy chọn modifier của món ăn.
- **Quyền truy cập**: StoreManager
- **Path Parameters**:
  - `itemId` (string, required): Mã món ăn.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "categoryId": { "type": "string", "example": "cat-coffee-01" },
    "name": { "type": "string", "example": "Bạc Xỉu Đá Macchiato" },
    "description": { "type": "string", "example": "Bạc xỉu 3 tầng kết hợp lớp kem béo macchiato hảo hạng" },
    "basePrice": { "type": "number", "example": 49000 },
    "imageUrl": { "type": "string", "example": "https://cdn.smartfb.vn/dishes/bac-xiu-macchiato-v2.jpg" },
    "isAvailable": { "type": "boolean", "example": true }
  },
  "required": ["categoryId", "name", "basePrice", "isAvailable"]
}
```
*Payload ví dụ*:
```json
{
  "categoryId": "cat-coffee-01",
  "name": "Bạc Xỉu Đá Macchiato",
  "description": "Bạc xỉu 3 tầng kết hợp lớp kem béo macchiato hảo hạng",
  "basePrice": 49000,
  "imageUrl": "https://cdn.smartfb.vn/dishes/bac-xiu-macchiato-v2.jpg",
  "isAvailable": true
}
```
- **Response 200 OK**:
```json
{
  "itemId": "item-cf-009",
  "name": "Bạc Xỉu Đá Macchiato",
  "basePrice": 49000,
  "updatedAt": "2026-08-13T16:12:00Z"
}
```

### PATCH /api/v1/menu/items/{itemId}/86-toggle
- **Mô tả**: Bật/tắt tức thì trạng thái tạm hết hàng (86 dish) cho bếp/barista trên giao diện KDS và PWA khách hàng.
- **Quyền truy cập**: StoreManager, KitchenChef, Barista
- **Path Parameters**:
  - `itemId` (string, required): Mã món ăn.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "isOut": { "type": "boolean", "example": true },
    "reason": { "type": "string", "example": "Hết nguyên liệu sữa tươi Dalat Milk" }
  },
  "required": ["isOut"]
}
```
*Payload ví dụ*:
```json
{
  "isOut": true,
  "reason": "Hết nguyên liệu sữa tươi Dalat Milk"
}
```
- **Response 200 OK**:
```json
{
  "itemId": "item-cf-009",
  "isAvailable": false,
  "toggledBy": "Chef_Nguyen",
  "toggledAt": "2026-08-13T16:13:00Z"
}
```

---

### Module 5: Order & Basket Lifecycle Management (12 Endpoints)

### POST /api/v1/orders
- **Mô tả**: Khởi tạo đơn hàng mới (hỗ trợ Khách hàng quét PWA, Nhân viên tạo qua App di động, hoặc Thu ngân ghi trực tiếp tại POS).
- **Quyền truy cập**: Authenticated Staff, Customer Guest (Session Token)
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "tableId": { "type": "string", "example": "tbl-0012-4821" },
    "orderType": { "type": "string", "enum": ["DineIn", "TakeAway", "Delivery"], "example": "DineIn" },
    "customerNotes": { "type": "string", "example": "Cho 1 ly ít đá" },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "itemId": { "type": "string", "example": "item-cf-001" },
          "quantity": { "type": "integer", "minimum": 1, "example": 2 },
          "selectedOptions": {
            "type": "array",
            "items": { "type": "string" },
            "example": ["opt-s50", "opt-i70"]
          },
          "note": { "type": "string", "example": "Mang ra trước" }
        },
        "required": ["itemId", "quantity"]
      }
    }
  },
  "required": ["storeId", "tableId", "orderType", "items"]
}
```
*Payload ví dụ*:
```json
{
  "storeId": "str-8832-491a-9012",
  "tableId": "tbl-0012-4821",
  "orderType": "DineIn",
  "customerNotes": "Cho 1 ly ít đá",
  "items": [
    {
      "itemId": "item-cf-001",
      "quantity": 2,
      "selectedOptions": ["opt-s50", "opt-i70"],
      "note": "Mang ra trước"
    }
  ]
}
```
- **Response 201 Created (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "orderId": { "type": "string", "example": "ord-88321" },
    "orderCode": { "type": "string", "example": "ORD-20260813-0042" },
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "tableId": { "type": "string", "example": "tbl-0012-4821" },
    "tableName": { "type": "string", "example": "Bàn 12" },
    "status": { "type": "string", "example": "Submitted" },
    "subTotal": { "type": "number", "example": 70000 },
    "taxAmount": { "type": "number", "example": 5600 },
    "totalAmount": { "type": "number", "example": 75600 },
    "createdAt": { "type": "string", "example": "2026-08-13T16:15:00Z" }
  },
  "required": ["orderId", "orderCode", "storeId", "tableId", "status", "totalAmount"]
}
```

### GET /api/v1/orders
- **Mô tả**: Lấy danh sách đơn hàng active hoặc lịch sử đơn hàng với phân trang và bộ lọc.
- **Quyền truy cập**: Authenticated Staff
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `status` (optional, string): Lọc trạng thái (`Submitted`, `Confirmed`, `InPreparation`, `Ready`, `Served`, `Completed`, `Cancelled`).
  - `tableId` (optional, string): Lọc theo bàn.
  - `page` (optional, integer): Mặc định 1.
  - `pageSize` (optional, integer): Mặc định 20.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "totalCount": { "type": "integer", "example": 1 },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "orderId": { "type": "string", "example": "ord-88321" },
          "orderCode": { "type": "string", "example": "ORD-20260813-0042" },
          "tableName": { "type": "string", "example": "Bàn 12" },
          "status": { "type": "string", "example": "InPreparation" },
          "totalAmount": { "type": "number", "example": 75600 },
          "createdAt": { "type": "string", "example": "2026-08-13T16:15:00Z" }
        },
        "required": ["orderId", "orderCode", "tableName", "status", "totalAmount"]
      }
    }
  },
  "required": ["totalCount", "items"]
}
```

### GET /api/v1/orders/{orderId}
- **Mô tả**: Lấy toàn bộ chi tiết đơn hàng gồm chi tiết từng dòng món ăn, trạng thái chế biến KDS và tổng số tiền thanh toán.
- **Quyền truy cập**: Authenticated Staff, Customer Guest (Session Owner)
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "orderId": { "type": "string", "example": "ord-88321" },
    "orderCode": { "type": "string", "example": "ORD-20260813-0042" },
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "tableName": { "type": "string", "example": "Bàn 12" },
    "status": { "type": "string", "example": "InPreparation" },
    "orderItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "orderItemId": { "type": "string", "example": "ori-99120" },
          "itemId": { "type": "string", "example": "item-cf-001" },
          "itemName": { "type": "string", "example": "Cà Phê Sữa Đá Sài Gòn" },
          "quantity": { "type": "integer", "example": 2 },
          "unitPrice": { "type": "number", "example": 35000 },
          "totalPrice": { "type": "number", "example": 70000 },
          "prepStatus": { "type": "string", "example": "Cooking" }
        },
        "required": ["orderItemId", "itemId", "itemName", "quantity", "unitPrice", "totalPrice", "prepStatus"]
      }
    },
    "subTotal": { "type": "number", "example": 70000 },
    "discountAmount": { "type": "number", "example": 0 },
    "taxAmount": { "type": "number", "example": 5600 },
    "totalAmount": { "type": "number", "example": 75600 }
  },
  "required": ["orderId", "orderCode", "tableName", "status", "orderItems", "totalAmount"]
}
```

### POST /api/v1/orders/{orderId}/items
- **Mô tả**: Gọi thêm món (top-up) vào đơn hàng đang mở của bàn ăn.
- **Quyền truy cập**: Authenticated Staff, Customer Guest (Session Owner)
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "itemId": { "type": "string", "example": "item-cake-005" },
          "quantity": { "type": "integer", "minimum": 1, "example": 1 },
          "note": { "type": "string", "example": "Ăn tại bàn" }
        },
        "required": ["itemId", "quantity"]
      }
    }
  },
  "required": ["items"]
}
```
*Payload ví dụ*:
```json
{
  "items": [
    {
      "itemId": "item-cake-005",
      "quantity": 1,
      "note": "Ăn tại bàn"
    }
  ]
}
```
- **Response 200 OK**:
```json
{
  "orderId": "ord-88321",
  "addedItemsCount": 1,
  "newTotalAmount": 115600,
  "updatedAt": "2026-08-13T16:18:00Z"
}
```

### PATCH /api/v1/orders/{orderId}/items/{itemId}/quantity
- **Mô tả**: Cập nhật số lượng của một món ăn trong đơn hàng chưa gửi bếp.
- **Quyền truy cập**: Authenticated Staff, Customer Guest (Session Owner)
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
  - `itemId` (string, required): Mã món ăn.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "quantity": { "type": "integer", "minimum": 1, "example": 3 }
  },
  "required": ["quantity"]
}
```
*Payload ví dụ*:
```json
{
  "quantity": 3
}
```
- **Response 200 OK**:
```json
{
  "orderId": "ord-88321",
  "itemId": "item-cf-001",
  "newQuantity": 3,
  "newTotalAmount": 150600
}
```

### DELETE /api/v1/orders/{orderId}/items/{itemId}
- **Mô tả**: Hủy món ăn khỏi đơn hàng (cần mã lý do hủy đơn của Quản lý nếu món đã gửi bếp).
- **Quyền truy cập**: StoreManager, ShiftLeader, Waiter (với món chưa gửi bếp)
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
  - `itemId` (string, required): Mã món ăn.
- **Query Parameters**:
  - `reasonCode` (optional, string): Mã lý do hủy (`CustomerCancel`, `KitchenOutOfStock`, `WrongItem`).
- **Response 200 OK**:
```json
{
  "orderId": "ord-88321",
  "removedItemId": "item-cf-001",
  "newTotalAmount": 45000,
  "message": "Đã hủy món khỏi đơn hàng."
}
```

### PATCH /api/v1/orders/{orderId}/status
- **Mô tả**: Chuyển trạng thái tiến trình đơn hàng (`Submitted` -> `Confirmed` -> `InPreparation` -> `Ready` -> `Served` -> `Completed` / `Cancelled`).
- **Quyền truy cập**: Authenticated Staff
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "status": { "type": "string", "enum": ["Submitted", "Confirmed", "InPreparation", "Ready", "Served", "Completed", "Cancelled"], "example": "Ready" },
    "note": { "type": "string", "example": "Đã hoàn thành chuẩn bị, chờ nhân viên trả món" }
  },
  "required": ["status"]
}
```
*Payload ví dụ*:
```json
{
  "status": "Ready",
  "note": "Đã hoàn thành chuẩn bị, chờ nhân viên trả món"
}
```
- **Response 200 OK**:
```json
{
  "orderId": "ord-88321",
  "previousStatus": "InPreparation",
  "newStatus": "Ready",
  "updatedAt": "2026-08-13T16:22:00Z"
}
```

### POST /api/v1/orders/{orderId}/call-staff
- **Mô tả**: Khách gửi yêu cầu trợ giúp/hỗ trợ từ bàn (vd: xin thêm đá, khăn giấy, cần nhân viên tư vấn).
- **Quyền truy cập**: Customer Guest (Session Owner)
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "tableId": { "type": "string", "example": "tbl-0012-4821" },
    "callType": { "type": "string", "enum": ["WaterRefill", "Napkins", "ServiceAdvice", "Other"], "example": "WaterRefill" },
    "note": { "type": "string", "example": "Cho thêm 2 ly nước lọc" }
  },
  "required": ["tableId", "callType"]
}
```
*Payload ví dụ*:
```json
{
  "tableId": "tbl-0012-4821",
  "callType": "WaterRefill",
  "note": "Cho thêm 2 ly nước lọc"
}
```
- **Response 200 OK**:
```json
{
  "callId": "call-99182-1201",
  "tableId": "tbl-0012-4821",
  "status": "Sent",
  "message": "Đã gửi thông báo đến nhân viên phục vụ."
}
```

### POST /api/v1/orders/{orderId}/request-bill
- **Mô tả**: Khách hàng bấm yêu cầu tính tiền tại bàn. Hệ thống chốt hóa đơn và khởi tạo mã VietQR.
- **Quyền truy cập**: Customer Guest (Session Owner), Waiter
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "orderId": { "type": "string", "example": "ord-88321" },
    "tableName": { "type": "string", "example": "Bàn 12" },
    "totalAmount": { "type": "number", "example": 75600 },
    "vietQrUrl": { "type": "string", "example": "https://img.vietqr.io/image/970436-0001882199201-compact2.png?amount=75600&addInfo=ORD88321" },
    "billStatus": { "type": "string", "example": "BillRequested" }
  },
  "required": ["orderId", "tableName", "totalAmount", "vietQrUrl", "billStatus"]
}
```

### POST /api/v1/orders/{orderId}/split
- **Mô tả**: Tách hóa đơn bàn ăn cho nhóm khách (tách đều tiền hoặc tách theo danh sách món đã chọn).
- **Quyền truy cập**: Cashier, StoreManager
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng gốc.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "splitType": { "type": "string", "enum": ["Equal", "Itemized"], "example": "Itemized" },
    "splitCount": { "type": "integer", "example": 2 },
    "splitItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "orderItemId": { "type": "string", "example": "ori-99120" },
          "quantity": { "type": "integer", "example": 1 }
        },
        "required": ["orderItemId", "quantity"]
      }
    }
  },
  "required": ["splitType"]
}
```
*Payload ví dụ*:
```json
{
  "splitType": "Itemized",
  "splitCount": 2,
  "splitItems": [
    { "orderItemId": "ori-99120", "quantity": 1 }
  ]
}
```
- **Response 201 Created**:
```json
{
  "originalOrderId": "ord-88321",
  "newChildOrderId": "ord-88321-SPLIT1",
  "newOrderAmount": 37800,
  "remainingOrderAmount": 37800
}
```

### POST /api/v1/orders/{orderId}/merge
- **Mô tả**: Gộp hai đơn hàng của hai bàn ăn kề nhau thành một hóa đơn duy nhất.
- **Quyền truy cập**: Cashier, StoreManager
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng đích (target order).
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "sourceOrderId": { "type": "string", "example": "ord-88322" },
    "reason": { "type": "string", "example": "Khách chuyển ghép bàn 12 và 13" }
  },
  "required": ["sourceOrderId"]
}
```
*Payload ví dụ*:
```json
{
  "sourceOrderId": "ord-88322",
  "reason": "Khách chuyển ghép bàn 12 và 13"
}
```
- **Response 200 OK**:
```json
{
  "mergedOrderId": "ord-88321",
  "closedSourceOrderId": "ord-88322",
  "totalMergedAmount": 151200,
  "message": "Đã gộp thành công 2 đơn hàng."
}
```

### POST /api/v1/orders/{orderId}/discount
- **Mô tả**: Áp dụng mã giảm giá, đổi điểm tích lũy thành viên hoặc giảm giá thủ công do quản lý duyệt.
- **Quyền truy cập**: Cashier, StoreManager
- **Path Parameters**:
  - `orderId` (string, required): Mã đơn hàng.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "discountType": { "type": "string", "enum": ["CouponCode", "LoyaltyPoints", "ManualPercent", "ManualAmount"], "example": "CouponCode" },
    "couponCode": { "type": "string", "example": "SUMMER2026" },
    "discountAmount": { "type": "number", "example": 15000 },
    "managerReason": { "type": "string", "example": "Vip member discount" }
  },
  "required": ["discountType"]
}
```
*Payload ví dụ*:
```json
{
  "discountType": "CouponCode",
  "couponCode": "SUMMER2026",
  "discountAmount": 15000
}
```
- **Response 200 OK**:
```json
{
  "orderId": "ord-88321",
  "subTotal": 70000,
  "discountAmount": 15000,
  "taxAmount": 4400,
  "finalTotalAmount": 59400
}
```

---

### Module 6: Kitchen Display System (KDS) Management (6 Endpoints)

### GET /api/v1/kds/tickets
- **Mô tả**: Lấy danh sách phiếu chế biến active trên màn hình KDS theo trạm (Bếp nóng, Bếp lạnh, Bar).
- **Quyền truy cập**: Authenticated Staff (KitchenChef, Barista, Manager)
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `station` (optional, string): Lọc trạm chế biến (`HotKitchen`, `ColdKitchen`, `Bar`).
  - `status` (optional, string): Lọc trạng thái (`Pending`, `Cooking`, `Ready`, `Bumped`).
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "ticketId": { "type": "string", "example": "kds-tkt-99012" },
      "orderId": { "type": "string", "example": "ord-88321" },
      "orderCode": { "type": "string", "example": "ORD-20260813-0042" },
      "tableName": { "type": "string", "example": "Bàn 12" },
      "station": { "type": "string", "example": "HotKitchen" },
      "status": { "type": "string", "example": "Cooking" },
      "ticketItems": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ticketItemId": { "type": "string", "example": "kds-item-1102" },
            "itemName": { "type": "string", "example": "Cơm Chiên Hải Sản" },
            "quantity": { "type": "integer", "example": 2 },
            "note": { "type": "string", "example": "Không cay" },
            "itemStatus": { "type": "string", "example": "Cooking" }
          },
          "required": ["ticketItemId", "itemName", "quantity", "itemStatus"]
        }
      },
      "elapsedMinutes": { "type": "integer", "example": 8 },
      "createdAt": { "type": "string", "example": "2026-08-13T16:15:00Z" }
    },
    "required": ["ticketId", "orderId", "orderCode", "tableName", "station", "status", "ticketItems", "elapsedMinutes"]
  }
}
```

### PATCH /api/v1/kds/tickets/{ticketId}/status
- **Mô tả**: Chuyển trạng thái phiếu chế biến (`Pending` -> `Cooking` -> `Ready` -> `Bumped`).
- **Quyền truy cập**: KitchenChef, Barista
- **Path Parameters**:
  - `ticketId` (string, required): Mã phiếu chế biến KDS.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "status": { "type": "string", "enum": ["Pending", "Cooking", "Ready", "Bumped"], "example": "Ready" }
  },
  "required": ["status"]
}
```
*Payload ví dụ*:
```json
{
  "status": "Ready"
}
```
- **Response 200 OK**:
```json
{
  "ticketId": "kds-tkt-99012",
  "status": "Ready",
  "bumpedAt": "2026-08-13T16:24:00Z"
}
```

### PATCH /api/v1/kds/tickets/{ticketId}/items/{itemId}/status
- **Mô tả**: Cập nhật tiến độ chế biến cho từng món ăn đơn lẻ trong phiếu KDS.
- **Quyền truy cập**: KitchenChef, Barista
- **Path Parameters**:
  - `ticketId` (string, required): Mã phiếu KDS.
  - `itemId` (string, required): Mã món ăn trong phiếu.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "itemStatus": { "type": "string", "enum": ["Pending", "Cooking", "Ready"], "example": "Ready" }
  },
  "required": ["itemStatus"]
}
```
*Payload ví dụ*:
```json
{
  "itemStatus": "Ready"
}
```
- **Response 200 OK**:
```json
{
  "ticketId": "kds-tkt-99012",
  "ticketItemId": "kds-item-1102",
  "itemStatus": "Ready"
}
```

### POST /api/v1/kds/tickets/{ticketId}/recall
- **Mô tả**: Triệu hồi (recall) phiếu vừa lỡ tay bump nhầm trở lại màn hình KDS đang chế biến.
- **Quyền truy cập**: KitchenChef, Barista, StoreManager
- **Path Parameters**:
  - `ticketId` (string, required): Mã phiếu KDS.
- **Response 200 OK**:
```json
{
  "ticketId": "kds-tkt-99012",
  "recalledStatus": "Cooking",
  "recalledAt": "2026-08-13T16:25:00Z",
  "message": "Đã triệu hồi phiếu KDS trở lại màn hình chế biến."
}
```

### GET /api/v1/kds/summary
- **Mô tả**: Tổng hợp danh sách món cần làm trên toàn bộ các đơn active (VD: 15 ly Cà phê sữa, 8 đĩa Cơm chiên).
- **Quyền truy cập**: KitchenChef, Barista, ShiftLeader
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `station` (optional, string): Lọc trạm chế biến.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "itemId": { "type": "string", "example": "item-cf-001" },
      "itemName": { "type": "string", "example": "Cà Phê Sữa Đá Sài Gòn" },
      "totalPendingQuantity": { "type": "integer", "example": 15 },
      "totalCookingQuantity": { "type": "integer", "example": 5 },
      "oldestTicketTime": { "type": "string", "example": "2026-08-13T16:10:00Z" }
    },
    "required": ["itemId", "itemName", "totalPendingQuantity", "totalCookingQuantity"]
  }
}
```

### GET /api/v1/kds/metrics
- **Mô tả**: Đo lường hiệu suất chế biến của bếp (thời gian chế biến trung bình/món, số đơn bị quá hạn 15 phút).
- **Quyền truy cập**: StoreManager
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `date` (optional, string): Ngày truy vấn (YYYY-MM-DD).
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "avgPrepTimeMinutes": { "type": "number", "example": 6.4 },
    "totalTicketsProcessed": { "type": "integer", "example": 142 },
    "overdueTicketsCount": { "type": "integer", "example": 3 },
    "busiestHour": { "type": "string", "example": "12:00 - 13:00" }
  },
  "required": ["storeId", "avgPrepTimeMinutes", "totalTicketsProcessed", "overdueTicketsCount"]
}
```

---

### Module 7: Payments & VietQR Integration (6 Endpoints)

### POST /api/v1/payments/generate-vietqr
- **Mô tả**: Khởi tạo payload mã VietQR động chứa Ngân hàng, Số tài khoản, Số tiền và Nội dung chuyển khoản chuẩn.
- **Quyền truy cập**: Authenticated Staff, Customer Guest
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "orderId": { "type": "string", "example": "ord-88321" },
    "amount": { "type": "number", "minimum": 1000, "example": 75600 }
  },
  "required": ["orderId", "amount"]
}
```
*Payload ví dụ*:
```json
{
  "orderId": "ord-88321",
  "amount": 75600
}
```
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "paymentId": { "type": "string", "example": "pay-99120-7712" },
    "orderId": { "type": "string", "example": "ord-88321" },
    "bankId": { "type": "string", "example": "970436" },
    "accountNo": { "type": "string", "example": "0001882199201" },
    "accountName": { "type": "string", "example": "CONG TY SMART FB VIET NAM" },
    "amount": { "type": "number", "example": 75600 },
    "transferContent": { "type": "string", "example": "ORD88321" },
    "qrDataUrl": { "type": "string", "example": "https://img.vietqr.io/image/970436-0001882199201-compact2.png?amount=75600&addInfo=ORD88321" }
  },
  "required": ["paymentId", "orderId", "bankId", "accountNo", "amount", "transferContent", "qrDataUrl"]
}
```

### POST /api/v1/payments/cash
- **Mô tả**: Thực hiện thanh toán bằng tiền mặt tại POS/Thu ngân với tính toán tiền thừa trả khách.
- **Quyền truy cập**: Cashier, StoreManager
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "orderId": { "type": "string", "example": "ord-88321" },
    "amountPaid": { "type": "number", "example": 100000 }
  },
  "required": ["orderId", "amountPaid"]
}
```
*Payload ví dụ*:
```json
{
  "orderId": "ord-88321",
  "amountPaid": 100000
}
```
- **Response 200 OK**:
```json
{
  "paymentId": "pay-cash-88129",
  "orderId": "ord-88321",
  "totalAmount": 75600,
  "amountPaid": 100000,
  "changeAmount": 24400,
  "status": "Paid",
  "paidAt": "2026-08-13T16:28:00Z"
}
```

### POST /api/v1/payments/webhook/vietqr
- **Mô tả**: Endpoint nhận Webhook tự động từ cổng thanh toán Ngân hàng khi biến động số dư VietQR khớp lệnh.
- **Quyền truy cập**: Public (Secured by Secret API Key Header `X-Webhook-Secret`)
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "transactionId": { "type": "string", "example": "TXN-BANK-9982109" },
    "transferContent": { "type": "string", "example": "ORD88321" },
    "amount": { "type": "number", "example": 75600 },
    "bankCode": { "type": "string", "example": "VCB" },
    "transactionTime": { "type": "string", "example": "2026-08-13T16:29:10Z" }
  },
  "required": ["transactionId", "transferContent", "amount", "bankCode"]
}
```
*Payload ví dụ*:
```json
{
  "transactionId": "TXN-BANK-9982109",
  "transferContent": "ORD88321",
  "amount": 75600,
  "bankCode": "VCB",
  "transactionTime": "2026-08-13T16:29:10Z"
}
```
- **Response 200 OK**:
```json
{
  "status": "Success",
  "matchedOrderId": "ord-88321",
  "message": "Giao dịch VietQR được xác thực thành công."
}
```

### GET /api/v1/payments/{paymentId}
- **Mô tả**: Kiểm tra trạng thái chi tiết của giao dịch thanh toán.
- **Quyền truy cập**: Authenticated Staff, Customer Guest
- **Path Parameters**:
  - `paymentId` (string, required): Mã thanh toán.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "paymentId": { "type": "string", "example": "pay-99120-7712" },
    "orderId": { "type": "string", "example": "ord-88321" },
    "paymentMethod": { "type": "string", "example": "VietQR" },
    "status": { "type": "string", "example": "Paid" },
    "amount": { "type": "number", "example": 75600 },
    "gatewayRef": { "type": "string", "example": "TXN-BANK-9982109" },
    "paidAt": { "type": "string", "example": "2026-08-13T16:29:10Z" }
  },
  "required": ["paymentId", "orderId", "paymentMethod", "status", "amount"]
}
```

### POST /api/v1/payments/{paymentId}/refund
- **Mô tả**: Thực hiện hoàn tiền một phần hoặc toàn bộ cho giao dịch (Cần quyền duyệt của Quản lý).
- **Quyền truy cập**: StoreManager
- **Path Parameters**:
  - `paymentId` (string, required): Mã thanh toán.
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "refundAmount": { "type": "number", "minimum": 1000, "example": 75600 },
    "refundReason": { "type": "string", "example": "Khách tính nhầm món, trả lại tiền mặt" }
  },
  "required": ["refundAmount", "refundReason"]
}
```
*Payload ví dụ*:
```json
{
  "refundAmount": 75600,
  "refundReason": "Khách tính nhầm món, trả lại tiền mặt"
}
```
- **Response 200 OK**:
```json
{
  "refundId": "ref-pay-11029",
  "paymentId": "pay-99120-7712",
  "refundAmount": 75600,
  "status": "Refunded",
  "refundedAt": "2026-08-13T16:31:00Z"
}
```

### GET /api/v1/payments/history
- **Mô tả**: Truy vấn nhật ký giao dịch thanh toán kèm phân loại theo phương thức (Tiền mặt, VietQR, Thẻ).
- **Quyền truy cập**: StoreManager, Cashier
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `fromDate` (optional, string): Ngày bắt đầu.
  - `toDate` (optional, string): Ngày kết thúc.
  - `method` (optional, string): `Cash`, `VietQR`, `CreditCard`.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "totalRevenue": { "type": "number", "example": 15400000 },
    "transactions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "paymentId": { "type": "string", "example": "pay-99120-7712" },
          "orderCode": { "type": "string", "example": "ORD-20260813-0042" },
          "paymentMethod": { "type": "string", "example": "VietQR" },
          "amount": { "type": "number", "example": 75600 },
          "paidAt": { "type": "string", "example": "2026-08-13T16:29:10Z" }
        },
        "required": ["paymentId", "orderCode", "paymentMethod", "amount", "paidAt"]
      }
    }
  },
  "required": ["totalRevenue", "transactions"]
}
```

---

### Module 8: Inventory & Stock Management (6 Endpoints)

### GET /api/v1/inventory/items
- **Mô tả**: Danh sách nguyên vật liệu trong kho kèm định mức tồn tối thiểu.
- **Quyền truy cập**: StoreManager, KitchenChef
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `category` (optional, string): Loại nguyên liệu (`CoffeeBeans`, `Milk`, `Syrup`, `Meat`, `Vegetables`).
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "ingredientId": { "type": "string", "example": "ing-cf-arabica" },
      "name": { "type": "string", "example": "Hạt Cà Phê Arabica Cầu Đất" },
      "unit": { "type": "string", "example": "kg" },
      "currentStock": { "type": "number", "example": 14.5 },
      "minReorderPoint": { "type": "number", "example": 5.0 },
      "costPricePerUnit": { "type": "number", "example": 220000 }
    },
    "required": ["ingredientId", "name", "unit", "currentStock", "minReorderPoint"]
  }
}
```

### POST /api/v1/inventory/items
- **Mô tả**: Đăng ký nguyên vật liệu mới vào danh mục kho.
- **Quyền truy cập**: StoreManager
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string", "example": "Sữa Tươi Dalat Milk Thanh Trùng" },
    "unit": { "type": "string", "example": "hộp 1L" },
    "minReorderPoint": { "type": "number", "example": 10.0 },
    "costPricePerUnit": { "type": "number", "example": 38000 }
  },
  "required": ["name", "unit", "minReorderPoint", "costPricePerUnit"]
}
```
*Payload ví dụ*:
```json
{
  "name": "Sữa Tươi Dalat Milk Thanh Trùng",
  "unit": "hộp 1L",
  "minReorderPoint": 10.0,
  "costPricePerUnit": 38000
}
```
- **Response 201 Created**:
```json
{
  "ingredientId": "ing-milk-dalat",
  "name": "Sữa Tươi Dalat Milk Thanh Trùng",
  "unit": "hộp 1L",
  "currentStock": 0.0
}
```

### POST /api/v1/inventory/receipts
- **Mô tả**: Tạo phiếu nhập kho nguyên vật liệu từ nhà cung cấp.
- **Quyền truy cập**: StoreManager, ShiftLeader
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "supplierName": { "type": "string", "example": "Nha Cung Cap Dalat Milk" },
    "receiptItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ingredientId": { "type": "string", "example": "ing-milk-dalat" },
          "quantity": { "type": "number", "example": 20.0 },
          "unitPrice": { "type": "number", "example": 38000 }
        },
        "required": ["ingredientId", "quantity", "unitPrice"]
      }
    }
  },
  "required": ["storeId", "supplierName", "receiptItems"]
}
```
*Payload ví dụ*:
```json
{
  "storeId": "str-8832-491a-9012",
  "supplierName": "Nha Cung Cap Dalat Milk",
  "receiptItems": [
    { "ingredientId": "ing-milk-dalat", "quantity": 20.0, "unitPrice": 38000 }
  ]
}
```
- **Response 201 Created**:
```json
{
  "receiptId": "rec-20260813-0012",
  "totalCost": 760000,
  "createdAt": "2026-08-13T16:33:00Z"
}
```

### POST /api/v1/inventory/transfers
- **Mô tả**: Phiếu điều chuyển nguyên vật liệu giữa tổng kho và chi nhánh cửa hàng.
- **Quyền truy cập**: StoreManager
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "fromStoreId": { "type": "string", "example": "str-warehouse-central" },
    "toStoreId": { "type": "string", "example": "str-8832-491a-9012" },
    "transferItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ingredientId": { "type": "string", "example": "ing-cf-arabica" },
          "quantity": { "type": "number", "example": 10.0 }
        },
        "required": ["ingredientId", "quantity"]
      }
    }
  },
  "required": ["fromStoreId", "toStoreId", "transferItems"]
}
```
*Payload ví dụ*:
```json
{
  "fromStoreId": "str-warehouse-central",
  "toStoreId": "str-8832-491a-9012",
  "transferItems": [
    { "ingredientId": "ing-cf-arabica", "quantity": 10.0 }
  ]
}
```
- **Response 201 Created**:
```json
{
  "transferId": "trf-99812-001",
  "status": "Transferred",
  "transferredAt": "2026-08-13T16:34:00Z"
}
```

### GET /api/v1/inventory/low-stock-alerts
- **Mô tả**: Danh sách các nguyên liệu chạm ngưỡng tồn tối thiểu cần nhập hàng gấp.
- **Quyền truy cập**: StoreManager, KitchenChef
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "ingredientId": { "type": "string", "example": "ing-milk-dalat" },
      "name": { "type": "string", "example": "Sữa Tươi Dalat Milk Thanh Trùng" },
      "currentStock": { "type": "number", "example": 2.0 },
      "minReorderPoint": { "type": "number", "example": 10.0 },
      "alertLevel": { "type": "string", "example": "Critical" }
    },
    "required": ["ingredientId", "name", "currentStock", "minReorderPoint", "alertLevel"]
  }
}
```

### POST /api/v1/inventory/audit
- **Mô tả**: Kiểm kê kho thực tế và ghi nhận chênh lệch kho (lý do hao hụt/hỏng hóc).
- **Quyền truy cập**: StoreManager
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "auditItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ingredientId": { "type": "string", "example": "ing-cf-arabica" },
          "actualStock": { "type": "number", "example": 13.0 },
          "varianceReason": { "type": "string", "example": "Hao hụt khi rang xay" }
        },
        "required": ["ingredientId", "actualStock"]
      }
    }
  },
  "required": ["storeId", "auditItems"]
}
```
*Payload ví dụ*:
```json
{
  "storeId": "str-8832-491a-9012",
  "auditItems": [
    { "ingredientId": "ing-cf-arabica", "actualStock": 13.0, "varianceReason": "Hao hụt khi rang xay" }
  ]
}
```
- **Response 200 OK**:
```json
{
  "auditId": "adt-20260813-99",
  "itemsAudited": 1,
  "totalVarianceCost": 330000,
  "auditedAt": "2026-08-13T16:35:00Z"
}
```

---

### Module 9: Staff & Attendance Management (4 Endpoints)

### GET /api/v1/staff
- **Mô tả**: Danh sách nhân viên cửa hàng, phân quyền vai trò và ca làm việc.
- **Quyền truy cập**: StoreManager, SystemAdmin
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `role` (optional, string): Lọc theo vai trò.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "staffId": { "type": "string", "example": "usr-1002" },
      "fullName": { "type": "string", "example": "Nguyễn Văn A" },
      "role": { "type": "string", "example": "Cashier" },
      "phone": { "type": "string", "example": "0912345678" },
      "isClockedIn": { "type": "boolean", "example": true }
    },
    "required": ["staffId", "fullName", "role", "phone", "isClockedIn"]
  }
}
```

### POST /api/v1/staff
- **Mô tả**: Đăng ký hồ sơ nhân viên mới và gán vai trò bảo mật.
- **Quyền truy cập**: StoreManager, SystemAdmin
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "storeId": { "type": "string", "example": "str-8832-491a-9012" },
    "username": { "type": "string", "example": "waiter_nam" },
    "password": { "type": "string", "example": "WaiterPass123!" },
    "fullName": { "type": "string", "example": "Trần Văn Nam" },
    "role": { "type": "string", "enum": ["StoreManager", "ShiftLeader", "Cashier", "Waiter", "KitchenChef", "Barista"], "example": "Waiter" },
    "phone": { "type": "string", "example": "0987654321" }
  },
  "required": ["storeId", "username", "password", "fullName", "role", "phone"]
}
```
*Payload ví dụ*:
```json
{
  "storeId": "str-8832-491a-9012",
  "username": "waiter_nam",
  "password": "WaiterPass123!",
  "fullName": "Trần Văn Nam",
  "role": "Waiter",
  "phone": "0987654321"
}
```
- **Response 201 Created**:
```json
{
  "staffId": "usr-1008",
  "username": "waiter_nam",
  "fullName": "Trần Văn Nam",
  "role": "Waiter"
}
```

### POST /api/v1/staff/clock-in
- **Mô tả**: Chấm công vào ca bằng tọa độ GPS Geofence (bán kính < 50m) kết hợp quét mã QR xoay 30 giây trên màn hình POS.
- **Quyền truy cập**: Authenticated Staff
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "latitude": { "type": "number", "example": 10.7769 },
    "longitude": { "type": "number", "example": 106.7009 },
    "posRotatingQrCode": { "type": "string", "example": "POS-QR-88219-SEC30" }
  },
  "required": ["latitude", "longitude", "posRotatingQrCode"]
}
```
*Payload ví dụ*:
```json
{
  "latitude": 10.7769,
  "longitude": 106.7009,
  "posRotatingQrCode": "POS-QR-88219-SEC30"
}
```
- **Response 200 OK**:
```json
{
  "shiftId": "sft-20260813-01",
  "staffId": "usr-1002",
  "clockInTime": "2026-08-13T07:00:15Z",
  "geofenceVerified": true,
  "message": "Chấm công vào ca thành công."
}
```

### POST /api/v1/staff/clock-out
- **Mô tả**: Chấm công ra ca & nộp báo cáo đối soát tiền mặt ngăn kéo POS.
- **Quyền truy cập**: Authenticated Staff
- **Request Body (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "shiftId": { "type": "string", "example": "sft-20260813-01" },
    "cashInDrawer": { "type": "number", "example": 3500000 },
    "notes": { "type": "string", "example": "Bàn giao ca sáng đủ tiền mặt" }
  },
  "required": ["shiftId", "cashInDrawer"]
}
```
*Payload ví dụ*:
```json
{
  "shiftId": "sft-20260813-01",
  "cashInDrawer": 3500000,
  "notes": "Bàn giao ca sáng đủ tiền mặt"
}
```
- **Response 200 OK**:
```json
{
  "shiftId": "sft-20260813-01",
  "clockOutTime": "2026-08-13T15:00:00Z",
  "totalSystemCash": 3500000,
  "cashVariance": 0,
  "message": "Chấm công ra ca thành công."
}
```

---

### Module 10: Analytics & AI Business Intelligence (4 Endpoints)

### GET /api/v1/analytics/dashboard
- **Mô tả**: Lấy chỉ số tổng quan điều hành (Doanh thu gộp, Doanh thu thuần, Số đơn hàng, AOV, Khung giờ cao điểm).
- **Quyền truy cập**: StoreManager, SystemAdmin
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `period` (optional, string): `Today`, `ThisWeek`, `ThisMonth`.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "grossRevenue": { "type": "number", "example": 45800000 },
    "netRevenue": { "type": "number", "example": 42136000 },
    "totalOrders": { "type": "integer", "example": 320 },
    "averageOrderValue": { "type": "number", "example": 131675 },
    "peakHour": { "type": "string", "example": "11:30 - 13:00" }
  },
  "required": ["grossRevenue", "netRevenue", "totalOrders", "averageOrderValue", "peakHour"]
}
```

### GET /api/v1/analytics/pnl
- **Mô tả**: Báo cáo Lãi/Lỗ (P&L) thời gian thực (COGS nguyên liệu, Chi phí nhân công, Chi phí vận hành, Lợi nhuận ròng).
- **Quyền truy cập**: StoreManager, SystemAdmin
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
  - `month` (optional, string): Tháng (YYYY-MM).
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "totalRevenue": { "type": "number", "example": 350000000 },
    "cogsAmount": { "type": "number", "example": 105000000 },
    "laborCost": { "type": "number", "example": 70000000 },
    "overheadCost": { "type": "number", "example": 35000000 },
    "netProfit": { "type": "number", "example": 140000000 },
    "netProfitMarginPercent": { "type": "number", "example": 40.0 }
  },
  "required": ["totalRevenue", "cogsAmount", "laborCost", "overheadCost", "netProfit", "netProfitMarginPercent"]
}
```

### GET /api/v1/analytics/ai-combo-recommendations
- **Mô tả**: Gợi ý gói Combo tối ưu dựa trên phân tích thuật toán đồng xuất hiện giỏ hàng (Basket Co-occurrence AI).
- **Quyền truy cập**: StoreManager
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "comboName": { "type": "string", "example": "Combo Buổi Sáng Năng Lượng" },
      "itemIds": {
        "type": "array",
        "items": { "type": "string" },
        "example": ["item-cf-001", "item-cake-005"]
      },
      "suggestedComboPrice": { "type": "number", "example": 65000 },
      "expectedRevenueLiftPercent": { "type": "number", "example": 18.5 }
    },
    "required": ["comboName", "itemIds", "suggestedComboPrice", "expectedRevenueLiftPercent"]
  }
}
```

### GET /api/v1/analytics/ai-churn-predictions
- **Mô tả**: AI dự báo chỉ số nguy cơ rời bỏ dịch vụ của khách hàng thân thiết và danh sách khuyến nghị chăm sóc.
- **Quyền truy cập**: StoreManager, SystemAdmin
- **Query Parameters**:
  - `storeId` (required, string): Mã cửa hàng.
- **Response 200 OK (JSON Schema)**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "customerId": { "type": "string", "example": "cus-99120" },
      "customerName": { "type": "string", "example": "Chị Hoàng Anh" },
      "churnRiskScore": { "type": "number", "example": 0.85 },
      "daysSinceLastVisit": { "type": "integer", "example": 45 },
      "recommendedAction": { "type": "string", "example": "Gửi Voucher giảm 20% qua Zalo OA" }
    },
    "required": ["customerId", "customerName", "churnRiskScore", "daysSinceLastVisit", "recommendedAction"]
  }
}
```

---

## 3. ĐẶC TẢ CHI TIẾT 4 SIGNALR REAL-TIME HUBS

### Hub 1: OrderHub
- **Route URL**: `wss://api.smartfb.vn/hubs/order`
- **Giao thức xác thực**: Quản lý kết nối qua JWT Token truyền bằng query parameter `?access_token={JWT_TOKEN}`.
- **Quản lý nhóm (Groups)**:
  - `JoinStoreGroup(string storeId)` — Lắng nghe biến động tất cả đơn hàng thuộc chi nhánh cửa hàng.
  - `JoinTableGroup(string tableId)` — Lắng nghe riêng đơn hàng của một bàn ăn (dành cho PWA khách hàng).
- **Phương thức Client gọi Server (Client-to-Server Methods)**:
  - `SubscribeTable(string tableId)`
  - `UnsubscribeTable(string tableId)`
- **Sự kiện Server phát tín hiệu (Server-to-Client Broadcast Events & JSON Schemas)**:
  - **Sự kiện `OrderCreated`**: Phát tới nhóm `StoreGroup` khi có đơn mới.
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "orderId": { "type": "string", "example": "ord-88321" },
    "orderCode": { "type": "string", "example": "ORD-20260813-0042" },
    "tableName": { "type": "string", "example": "Bàn 12" },
    "totalAmount": { "type": "number", "example": 75600 },
    "createdAt": { "type": "string", "example": "2026-08-13T16:15:00Z" }
  },
  "required": ["orderId", "orderCode", "tableName", "totalAmount"]
}
```
  - **Sự kiện `OrderStatusUpdated`**: Cập nhật tiến trình đơn.
```json
{
  "orderId": "ord-88321",
  "oldStatus": "InPreparation",
  "newStatus": "Ready",
  "updatedBy": "KitchenStaff_Huan"
}
```
  - **Sự kiện `BillRequested`**: Phát cảnh báo yêu cầu thanh toán tới màn hình POS Thu ngân.
```json
{
  "orderId": "ord-88321",
  "tableId": "tbl-0012-4821",
  "tableName": "Bàn 12",
  "totalAmount": 75600
}
```
  - **Sự kiện `StaffCalled`**: Khách tại bàn bấm nút gọi nhân viên.
```json
{
  "tableId": "tbl-0012-4821",
  "tableName": "Bàn 12",
  "callType": "WaterRefill",
  "calledAt": "2026-08-13T16:20:00Z"
}
```

### Hub 2: KitchenHub
- **Route URL**: `wss://api.smartfb.vn/hubs/kitchen`
- **Giao thức xác thực**: JWT Token có chứa Role Claims `KitchenChef`, `Barista`, `StoreManager`.
- **Quản lý nhóm (Groups)**:
  - `JoinKitchenStation(string storeId, string stationId)` (`HotKitchen`, `ColdKitchen`, `Bar`).
- **Phương thức Client gọi Server**:
  - `UpdateItemPrepState(string ticketId, string itemId, string state)`
  - `BumpTicket(string ticketId)`
  - `ToggleItem86(string itemId, bool isOut)`
- **Sự kiện Server phát tín hiệu (Server-to-Client Broadcast Events & JSON Schemas)**:
  - **Sự kiện `NewTicketReceived`**: Đơn món mới gửi xuống bếp.
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "ticketId": { "type": "string", "example": "kds-tkt-99012" },
    "tableName": { "type": "string", "example": "Bàn 12" },
    "station": { "type": "string", "example": "HotKitchen" },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "itemName": { "type": "string", "example": "Cơm Chiên Hải Sản" },
          "quantity": { "type": "integer", "example": 2 },
          "note": { "type": "string", "example": "Không cay" }
        },
        "required": ["itemName", "quantity"]
      }
    }
  },
  "required": ["ticketId", "tableName", "station", "items"]
}
```
  - **Sự kiện `ItemBumped`**: Hoàn thành món.
```json
{
  "ticketId": "kds-tkt-99012",
  "itemId": "kds-item-1102",
  "bumpedBy": "Chef_Nguyen"
}
```
  - **Sự kiện `Dish86Toggled`**: Thông báo món tạm hết hàng trên toàn màn hình KDS.
```json
{
  "itemId": "item-cf-009",
  "isOut": true,
  "toggledBy": "Chef_Nguyen"
}
```

### Hub 3: TableHub
- **Route URL**: `wss://api.smartfb.vn/hubs/table`
- **Giao thức xác thực**: JWT Token có vai trò Nhân viên/Quản lý.
- **Quản lý nhóm (Groups)**:
  - `JoinStoreFloor(string storeId, string areaId)` — Theo dõi sơ đồ bàn theo từng tầng.
- **Phương thức Client gọi Server**:
  - `ChangeTableStatus(string tableId, string newStatus)`
- **Sự kiện Server phát tín hiệu**:
  - **Sự kiện `TableStatusChanged`**: Cập nhật màu sắc sơ đồ bàn thời gian thực (`Available`, `Occupied`, `Cleaning`, `BillRequested`).
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "tableId": { "type": "string", "example": "tbl-0012-4821" },
    "oldStatus": { "type": "string", "example": "Occupied" },
    "newStatus": { "type": "string", "example": "BillRequested" },
    "updatedAt": { "type": "string", "example": "2026-08-13T16:22:00Z" }
  },
  "required": ["tableId", "oldStatus", "newStatus"]
}
```
  - **Sự kiện `TableMerged`**: Gộp bàn trên màn hình sơ đồ.
```json
{
  "targetTableId": "tbl-0012-4821",
  "sourceTableId": "tbl-0013-4822",
  "message": "Đã gộp Bàn 13 vào Bàn 12"
}
```

### Hub 4: PaymentHub
- **Route URL**: `wss://api.smartfb.vn/hubs/payment`
- **Giao thức xác thực**: JWT Token (Customer Session hoặc Staff).
- **Quản lý nhóm (Groups)**:
  - `JoinOrderPaymentGroup(string orderId)`
- **Phương thức Client gọi Server**:
  - `WatchPaymentStatus(string orderId)`
- **Sự kiện Server phát tín hiệu**:
  - **Sự kiện `PaymentQRGenerated`**: Đẩy QR VietQR xuống thiết bị khách hàng.
```json
{
  "orderId": "ord-88321",
  "qrCodeUrl": "https://img.vietqr.io/image/970436-0001882199201-compact2.png?amount=75600&addInfo=ORD88321",
  "amount": 75600
}
```
  - **Sự kiện `PaymentConfirmed`**: Tự động nhảy màn hình "Thanh toán thành công" khi Webhook ngân hàng khớp lệnh.
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "orderId": { "type": "string", "example": "ord-88321" },
    "transactionId": { "type": "string", "example": "TXN-BANK-9982109" },
    "amountPaid": { "type": "number", "example": 75600 },
    "paidAt": { "type": "string", "example": "2026-08-13T16:29:10Z" }
  },
  "required": ["orderId", "transactionId", "amountPaid", "paidAt"]
}
```

---

## 4. MA TRẬN PHÂN QUYỀN VÀ XÁC THỰC (SECURITY & RBAC MATRIX)

| Module / Chức năng | Anonymous Guest | Waiter | Cashier | Kitchen / Bar | Store Manager | System Admin |
|---|---|---|---|---|---|---|
| Auth & Login | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Store Management | ❌ | ❌ | ❌ | ❌ | Read / Update | Full Access |
| Area & Table Map | Read | Read / Update | Read / Update | Read | Full Access | Full Access |
| Menu Categories | Read | Read | Read | Read | Full Access | Full Access |
| Menu Items & 86 Toggle | Read | Read | Read | 86-Toggle | Full Access | Full Access |
| Order Creation & Top-up | Create / Read | Create / Read | Create / Read | Read | Full Access | Full Access |
| Order Void & Discount | ❌ | ❌ | Discount | ❌ | Full Access | Full Access |
| KDS Ticket Management | ❌ | ❌ | ❌ | Full Access | Full Access | Full Access |
| Payment & VietQR Webhook | Guest QR | Process Cash | Full Process | ❌ | Full Access | Full Access |
| Inventory & Stock Audit | ❌ | ❌ | ❌ | Read | Full Access | Full Access |
| Staff Clock-in / Out | ❌ | Clock-in/out | Clock-in/out | Clock-in/out | Full Access | Full Access |
| Analytics & AI P&L | ❌ | ❌ | ❌ | ❌ | Full Access | Full Access |

---

## 5. HƯỚNG DẪN KIỂM THỬ THỦ CÔNG VÀ KỊCH BẢN TÍCH HỢP (INTEGRATION TESTS)

### Kịch bản 1: Luồng gọi món PWA -> KDS Bếp -> Thanh toán VietQR
1. **Bước 1**: Khách hàng quét mã QR bàn 12 -> Gọi `POST /api/v1/auth/customer-checkin` nhận `guestToken`.
2. **Bước 2**: Khách hàng chọn món và gọi `POST /api/v1/orders` -> Trạng thái đơn `Submitted`.
3. **Bước 3**: Server SignalR `OrderHub` phát tín hiệu `OrderCreated` tới thiết bị Thu ngân và `KitchenHub` phát `NewTicketReceived` tới trạm Bếp nóng `HotKitchen`.
4. **Bước 4**: Bếp chế biến xong bấm BUMP trên KDS -> Gọi `PATCH /api/v1/kds/tickets/{ticketId}/status` sang `Ready`.
5. **Bước 5**: Khách hàng bấm yêu cầu tính tiền -> Gọi `POST /api/v1/orders/{orderId}/request-bill`. `PaymentHub` phát sự kiện `PaymentQRGenerated`.
6. **Bước 6**: Khách chuyển khoản VietQR -> Ngân hàng gửi callback về `POST /api/v1/payments/webhook/vietqr`.
7. **Bước 7**: Webhook xác thực đúng `orderId` và số tiền -> `PaymentHub` phát `PaymentConfirmed`. Bàn 12 tự động đổi sang `Cleaning`.

---

