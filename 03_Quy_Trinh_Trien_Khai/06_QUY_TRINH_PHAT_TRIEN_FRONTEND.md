# 🖥️ QUY TRÌNH 6: PHÁT TRIỂN FRONTEND (NEXT.JS 14 APP ROUTER)

> **Mục tiêu:** Xây dựng 4 phân hệ giao diện PWA/Responsive, áp dụng chiến lược Mock-First và ghép nối API/SignalR mượt mà.

---

## 1. NHỮNG ĐIỂM BẮT BUỘC PHẢI LÀM RÕ TRONG BƯỚC NÀY

### 1.1 Chiến Lược "Mock-First" (Không Phụ Thuộc Backend)
Để Frontend **KHÔNG NGHẼN** khi chờ Backend code API:

```
[ Giai đoạn 1: Mock UI ]
   Next.js Pages ──► Local JSON Mock Data ──► Dựng hoàn chỉnh 100% UI/UX
                                                       │
[ Giai đoạn 2: Ghép API ]                              ▼
   Next.js Pages ──► Axios/Fetch Wrapper ──► Backend API Thật (Chỉ thay URL!)
```

---

### 1.2 Cấu Trúc Route Groups & Màn Hình

```
src/app/
  ├── (customer)/             ← Route Group QR Order Khách
  │   ├── menu/page.tsx       (Lưới món + Category Tabs)
  │   ├── cart/page.tsx       (Giỏ hàng)
  │   ├── order-status/page.tsx (Tiến trình đơn hàng)
  │   └── bill/page.tsx       (Mã VietQR thanh toán)
  ├── (kds)/                  ← Route Group KDS Bếp
  │   └── kitchen/page.tsx    (Full-screen Kanban Bếp)
  ├── (staff)/                ← Route Group Staff App
  │   └── alerts/page.tsx     (Alert gọi bàn/bill)
  ├── (manager)/              ← Route Group Manager
  │   └── shift/page.tsx      (Mở/Kết ca)
  └── (admin)/                ← Route Group Admin Dashboard
      ├── dashboard/page.tsx  (Biểu đồ Doanh thu)
      └── menu-mgmt/page.tsx  (CRUD Sản phẩm)
```

---

### 1.3 Quản Lý Kết Nối SignalR Client (Custom Hook `useSignalR`)

```typescript
// Custom hook kết nối SignalR tự động reconnect
export const useSignalR = (hubUrl: string, eventName: string, callback: (data: any) => void) => {
  useEffect(() => {
    const connection = new HubConnectionBuilder()
      .withUrl(hubUrl)
      .withAutomaticReconnect()
      .build();

    connection.start().then(() => {
      connection.on(eventName, callback);
    });

    return () => { connection.stop(); };
  }, [hubUrl, eventName]);
};
```

---

## 2. PHÂN CÔNG THỰC THI (FE1 vs FE2)

| Phân hệ | FE1 (Frontend Lead) | FE2 (Frontend Dev) |
|---|---|---|
| **Khách hàng** | Trang Menu QR, Detail Modal, Cart Drawer | Trang Bill VietQR & Feedback |
| **Pha chế & Phục vụ** | KDS Bếp (Kanban + SignalR), Staff Alerts | Sơ đồ bàn trực quan |
| **Quản trị** | Design Tokens & Shared UI Components | Admin Dashboard Charts, Menu CRUD |
| **Vận hành** | SignalR Client Wrapper | Manager Mở/Kết ca & Kho UI |

---

## 📥 INPUT & 📤 OUTPUT CỦA QUY TRÌNH 6

* **Input:** Wireframe UI, Design System, Shared Components & API Specification từ Quy trình 3 & 4.
* **Output:** Frontend Next.js 14 chạy mượt trên `http://localhost:3000`, kết nối 100% API & SignalR thật.
* **Bước tiếp theo:** Chuyển sang **Quy trình 7: Testing, AI Integration & Deployment**.
