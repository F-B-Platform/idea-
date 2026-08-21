# 🎨 QUY TRÌNH 4: THIẾT KẾ GIAO DIỆN UI/UX & WIREFRAME

> **Mục tiêu:** Thống nhất Layout, luồng thao tác người dùng (User Flow) và dựng sẵn thư viện Component trước khi ghép API.

---

## 1. NHỮNG ĐIỂM BẮT BUỘC PHẢI LÀM RÕ TRONG BƯỚC NÀY

### 1.1 Phác Thảo Wireframe Cho 4 Giao Diện

```
┌────────────────────────────────────────────────────────────────────────┐
│                      4 PHÂN HỆ GIAO DIỆN CHÍNH                         │
│                                                                        │
│  1. QR ORDER PWA (Khách hàng)           2. KDS BẾP (Barista)           │
│  • Mobile-first (375px - 430px)         • Full-screen TV/Tablet (1080p) │
│  • Menu List + Category Tabs            • Kanban Card Đơn Hàng          │
│  • Modal Tùy chỉnh (Size/Topping)       • Timer Cảnh báo (Xanh/Vàng/Đỏ) │
│  • Cart Drawer & VietQR Payment         • Modal Công thức pha chế       │
│                                                                        │
│  3. STAFF APP (Phục vụ)                 4. ADMIN DASHBOARD (Chủ/QL)     │
│  • Alert Bar (Gọi bàn / Yêu cầu Bill)   • Desktop Web (Sidebar + Header)│
│  • Sơ đồ bàn trực quan (Floor Map)      • Thẻ KPI Doanh thu            │
│  • Báo hết món nhanh                    • Biểu đồ Doanh thu (Chart.js) │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 1.2 Hierarchy Component & Design Tokens

* **Design Tokens:**
  * **Color Palette:** Primary Brand Orange (`#FF6B00`), Dark Neutral (`#18181B`), Background Off-White (`#FAFAFA`), Success Green (`#22C55E`), Warning Yellow (`#F59E0B`), Danger Red (`#EF4444`).
  * **Typography:** Inter / Plus Jakarta Sans (Google Fonts).
* **Shared UI Component Library:**
  * `Button` (Primary, Secondary, Ghost, Danger)
  * `Card` (ProductCard, OrderCard, KdsCard)
  * `Modal` / `Drawer` (DetailModal, CartDrawer)
  * `Badge` (StatusBadge, TagBadge)
  * `Toast` (NotificationToast)

---

### 1.3 Quản Lý State Client-side (Zustand Stores)

```typescript
// 1. Cart Store (QR Order Khách)
interface CartState {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  removeItem: (itemId: string) => void;
  updateQuantity: (itemId: string, qty: number) => void;
  clearCart: () => void;
  getTotalAmount: () => number;
}

// 2. Auth Store (Admin / Manager / Staff)
interface AuthState {
  user: User | null;
  token: string | null;
  setAuth: (user: User, token: string) => void;
  logout: () => void;
}
```

---

## 2. QUY TRÌNH THỰC THI THEO VAI TRÒ

```
┌────────────────────────────────────────────────────────────────────────┐
│                        QUY TRÌNH THIẾT KẾ UI                           │
│                                                                        │
│  [FE1] Vẽ Wireframe QR Order & KDS Bếp (Figma / Excalidraw)            │
│     │                                                                  │
│     ▼                                                                  │
│  [FE2] Vẽ Wireframe Admin Dashboard & Manager App                      │
│     │                                                                  │
│     ▼                                                                  │
│  [FE1 & FE2] Setup Next.js 14 Route Groups:                            │
│              /(customer), /(kds), /(staff), /(manager), /(admin)       │
│     │                                                                  │
│     ▼                                                                  │
│  [FE1 & FE2] Xây dựng bộ Component UI dùng chung trong `components/ui/` │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📥 INPUT & 📤 OUTPUT CỦA QUY TRÌNH 4

* **Input:** Scope MVP Tier 1 & API Specification từ Quy trình 1 & 3.
* **Output:**Bộ Wireframe 15+ màn hình & Dự án Next.js 14 khởi tạo có sẵn Shared UI Components.
* **Bước tiếp theo:** Bắt đầu bước lập trình — **Quy trình 5: Phát triển Backend API**.
