# 🎨 ĐẶC TẢ HỆ THỐNG THIẾT KẾ UI/UX DESIGN SYSTEM & WIREFRAME SPECS
## SMART F&B OPERATING SYSTEM — ENTERPRISE MULTI-BRANCH PLATFORM

---

> **Mã Tài Liệu:** `04_THIET_KE_UI_UX_DESIGN_SYSTEM.md`  
> **Phiên Bản:** `2.0.0-PROD` (Production Specs)  
> **Ngày Phát Hành:** 2026-08-13  
> **Trạng Thái:** Complete / Approved for Engineering Implementation  
> **Phạm Vi Ứng Dụng:** QR Order PWA (Mobile), KDS Kitchen Display (Tablet/TV), Staff App & Sunmi POS Dual-Screen, Manager App (Mobile), Admin Web Dashboard (Desktop).

---

## 📑 MỤC LỤC CHÍNH

1. [CHƯƠNG 1: THƯ VIỆN DESIGN SYSTEM TOKENS & PHẦN CỨNG BẢNG MỤC TIÊU](#chuong-1-thu-vien-design-system-tokens--phan-cung-bang-muc-tieu)
   - 1.1 Color Palette System & Theme Tokens (HSL & Hex)
   - 1.2 KDS Dark Mode High-Contrast Theme Specs
   - 1.3 Typography Scale & Font System (Outfit & Inter)
   - 1.4 Spatial Grid Scale, Padding & Elevation System
   - 1.5 Micro-Interactions, CSS Keyframe Animations & SignalR Pulse Rules
   - 1.6 Hardware Profile & Target Resolution Matrix
2. [CHƯƠNG 2: NHÓM 1 — GIAO DIỆN QR MENU (CUSTOMER PWA - 9 MÀN HÌNH)](#chuong-2-nhom-1--giao-dien-qr-menu-customer-pwa---9-man-hinh)
   - 2.1 SCR-PWA-01: Phone Check-in & Table Verification Screen
   - 2.2 SCR-PWA-02: Interactive Menu Grid & Category Navigator
   - 2.3 SCR-PWA-03: Dish Item Customization Modal / Drawer
   - 2.4 SCR-PWA-04: Shopping Cart & Checkout Order Summary
   - 2.5 SCR-PWA-05: AI Sommelier / Food Chatbot Assistant Drawer
   - 2.6 SCR-PWA-06: Real-time Order Status Tracker (SignalR Pulse)
   - 2.7 SCR-PWA-07: Call Staff & Service / Bill Request Overlay
   - 2.8 SCR-PWA-08: Photo Feedback & Staff Tip Rating Modal
   - 2.9 SCR-PWA-09: Customer Loyalty Wallet & Rewards History
3. [CHƯƠNG 3: NHÓM 2 — KITCHEN DISPLAY SYSTEM (KDS BẾP - 4 MÀN HÌNH)](#chuong-3-nhom-2--kitchen-display-system-kds-bep---4-man-hinh)
   - 3.1 SCR-KDS-01: Kitchen Ticket Grid with Dynamic Timer Cards
   - 3.2 SCR-KDS-02: Consolidated Dish & Table-Aggregated Summary View
   - 3.3 SCR-KDS-03: Recipe Specification & Plating Guide Modal
   - 3.4 SCR-KDS-04: Barista / Kitchen Out-of-Stock (86 Dish) Toggle
4. [CHƯƠNG 4: NHÓM 3 — STAFF MOBILE & SUNMI POS DUAL-SCREEN (5 MÀN HÌNH)](#chuong-4-nhom-3--staff-mobile--sunmi-pos-dual-screen---5-man-hinh)
   - 4.1 SCR-STAFF-01: Waiter Service Notification Center
   - 4.2 SCR-STAFF-02: Interactive Floor Map & Real-time Table Matrix
   - 4.3 SCR-STAFF-03: Mobile VietQR Dynamic Payment Generator
   - 4.4 SCR-POS-04: Sunmi 10.1" Customer Display Secondary Screen View
   - 4.5 SCR-STAFF-05: 30s Dynamic QR Code & 50m GPS Attendance Clock-in
5. [CHƯƠNG 5: NHÓM 4 — MANAGER MOBILE APP (5 MÀN HÌNH)](#chuong-5-nhom-4--manager-mobile-app---5-man-hinh)
   - 5.1 SCR-MGR-01: Shift Opening & Closing Management Screen
   - 5.2 SCR-MGR-02: Cash Drawer Reconciliation & >50k Variance Alert
   - 5.3 SCR-MGR-03: Warehouse-to-Counter Stock Transfer Request
   - 5.4 SCR-MGR-04: Branch Revenue Analytics & AI Natural Language Query
   - 5.5 SCR-MGR-05: Emergency Incident & Low-Rating Feedback Action Center
6. [CHƯƠNG 6: NHÓM 5 — ADMIN WEB DASHBOARD (6 MÀN HÌNH)](#chuong-6-nhom-5--admin-web-dashboard---6-man-hinh)
   - 6.1 SCR-ADM-01: Multi-Branch Executive Command Overview Dashboard
   - 6.2 SCR-ADM-02: Automated Real-time P&L Statement & Expense Matrix
   - 6.3 SCR-ADM-03: Centralized Menu Editor & Branch Multi-Price Matrix
   - 6.4 SCR-ADM-04: AI Combo Generator & Promotional Campaign Engine
   - 6.5 SCR-ADM-05: AI Customer Churn Risk Prediction & Retargeting Hub
   - 6.6 SCR-ADM-06: RBAC Permission Matrix & Immutable Audit Trail Logs
7. [CHƯƠNG 7: BẢNG HƯỚNG DẪN COMPONENT LÍP-RÀN DÙNG CHUNG & QUY TRÌNH KIỂM THỬ UI](#chuong-7-bang-huong-dan-component-lip-ran-dung-chung--quy-trinh-kiem-thu-ui)

---

## 🛠️ CHƯƠNG 1: THƯ VIỆN DESIGN SYSTEM TOKENS & PHẦN CỨNG BẢNG MỤC TIÊU

### 1.1 Color Palette System & Theme Tokens (HSL & Hex)

Hệ thống màu sắc của Smart F&B OS được xây dựng trên chuẩn **HSL (Hue, Saturation, Lightness)** kết hợp Hex mã hóa cứng để đảm bảo tính nhất quán trên toàn bộ thiết bị (Mobile PWA, POS, KDS Tablet, Admin Web).

```css
:root {
  /* --- Primary Brand Color: Warm Amber / Emerald Fusion --- */
  --brand-primary-50: hsl(28, 100%, 96%);     /* #FFF7ED - Soft Tint */
  --brand-primary-100: hsl(28, 100%, 89%);    /* #FFEDD5 - Hover Light */
  --brand-primary-500: hsl(28, 100%, 50%);    /* #FF6B00 - Brand Main Accent */
  --brand-primary-600: hsl(24, 95%, 46%);     /* #EA580C - Active Press */
  --brand-primary-700: hsl(21, 90%, 38%);     /* #C2410C - Focus Outline */

  /* --- Secondary Brand Color: Deep Emerald Teal --- */
  --brand-secondary-50: hsl(166, 76%, 97%);   /* #F0FDF4 */
  --brand-secondary-500: hsl(160, 84%, 39%);  /* #10B981 - Success & Eco Badge */
  --brand-secondary-700: hsl(163, 88%, 20%);  /* #064E3B - Dark Accent */

  /* --- Semantic Status Colors --- */
  --semantic-success: hsl(142, 71%, 45%);    /* #22C55E - Delivered / Normal Timer */
  --semantic-warning: hsl(38, 92%, 50%);     /* #F59E0B - Pending 5-10m / Alert */
  --semantic-danger: hsl(354, 84%, 57%);    /* #EF4444 - Overdue >10m / Critical */
  --semantic-info: hsl(217, 91%, 60%);      /* #3B82F6 - System Info / SignalR */
  --semantic-neutral-50: hsl(210, 40%, 98%);/* #F8FAFC - App Background Light */
  --semantic-neutral-100: hsl(214, 32%, 91%);/* #E2E8F0 - Divider Border */
  --semantic-neutral-500: hsl(215, 16%, 47%);/* #64748B - Subtext Caption */
  --semantic-neutral-900: hsl(222, 47%, 11%);/* #0F172A - Body Text Dark */

  /* --- Surface Tokens --- */
  --surface-base: #FFFFFF;
  --surface-card: #FFFFFF;
  --surface-overlay: rgba(15, 23, 42, 0.65);
  --surface-glass: rgba(255, 255, 255, 0.85);
}
```

---

### 1.2 KDS Dark Mode High-Contrast Theme Specs

Dành riêng cho màn hình Bếp & Pha chế (KDS Terminal), môi trường ánh sáng thay đổi và khoảng cách quan sát 1.5m - 3m đòi hỏi theme **High Contrast Dark Slate** chống mỏi mắt và tăng nhận diện thị giác khẩn cấp.

```css
.theme-kds-dark {
  /* KDS Background & Surface */
  --kds-bg-main: #0F172A;                     /* Dark Slate 900 */
  --kds-card-bg: #1E293B;                   /* Dark Slate 800 */
  --kds-card-border: #334155;               /* Dark Slate 700 */
  --kds-text-primary: #F8FAFC;              /* Pure Crisp White */
  --kds-text-muted: #94A3B8;                /* Light Slate 400 */

  /* Dynamic Ticket Status Color Coding */
  --kds-status-fresh-bg: #064E3B;           /* Green 950 Base */
  --kds-status-fresh-border: #22C55E;       /* Green 500 Glow Border (< 5m) */
  --kds-status-fresh-text: #86EFAC;         /* Green 300 Text */

  --kds-status-warning-bg: #451A03;         /* Amber 950 Base */
  --kds-status-warning-border: #F59E0B;     /* Amber 500 Glow Border (5 - 10m) */
  --kds-status-warning-text: #FDE047;       /* Amber 300 Text */

  --kds-status-overdue-bg: #450A0A;         /* Red 950 Base */
  --kds-status-overdue-border: #EF4444;     /* Red 500 Flashing Glow Border (> 10m) */
  --kds-status-overdue-text: #FCA5A5;       /* Red 300 Text */
  
  --kds-action-bump: #2563EB;               /* Vibrant Blue Action Button */
  --kds-action-recall: #475569;             /* Slate Muted Action Button */
}
```

---

### 1.3 Typography Scale & Font System (Outfit & Inter)

Quy định chuẩn 2 bộ phông chữ Google Fonts:
1. **Outfit**: Sử dụng cho Tiêu đề (Headings), Giá tiền (Price Numbers), Banner KPI và Điểm Loyalty. Font dạng Sans-serif hình học hiện đại, góc nét mềm mại tạo cảm giác cao cấp.
2. **Inter**: Sử dụng cho Nội dung văn bản (Body Text), Bảng dữ liệu (Data Tables), Form Input, Mã đơn hàng, Badge trạng thái.

| Scale Token | Font Family | Size (px/rem) | Line Height | Weight | Application |
|---|---|---|---|---|---|
| `font-display-xl` | Outfit | 36px (2.25rem) | 44px (1.22) | 700 (Bold) | Dashboard KPI Totals, Large VietQR Amount |
| `font-display-lg` | Outfit | 30px (1.875rem)| 38px (1.26) | 700 (Bold) | Header Sales Summary, KDS Timer Banner |
| `font-heading-h1` | Outfit | 24px (1.5rem)  | 32px (1.33) | 600 (SemiBold)| Modal Title, Screen Main Title |
| `font-heading-h2` | Outfit | 20px (1.25rem) | 28px (1.40) | 600 (SemiBold)| Card Section Title, Dish Group Header |
| `font-heading-h3` | Outfit | 18px (1.125rem)| 24px (1.33) | 500 (Medium)  | Dish Item Name, Table Badge Number |
| `font-body-lg`    | Inter  | 16px (1.0rem)  | 24px (1.50) | 400 (Regular) | Primary Content, Form Controls |
| `font-body-md`    | Inter  | 14px (0.875rem)| 20px (1.42) | 400 (Regular) | Default Subtitle, Table Row Data |
| `font-caption`    | Inter  | 12px (0.75rem) | 16px (1.33) | 500 (Medium)  | Timestamp, Helper Text, Form Labels |
| `font-micro-badge`| Inter  | 10px (0.625rem)| 14px (1.40) | 700 (Bold)    | Status Badge, Order Quantity Tag |

---

### 1.4 Spatial Grid Scale, Padding & Elevation System

Hệ thống lưới khoảng cách dựa trên cơ sở **8px Grid System** (có hỗ trợ sub-grid 4px cho micro-spacing):

```css
:root {
  /* Spacing Scale */
  --space-0-5: 4px;    /* Micro gap, badge padding */
  --space-1:   8px;    /* Compact element gap, icon-text space */
  --space-2:   16px;   /* Standard card internal padding, list item gap */
  --space-3:   24px;   /* Section padding, modal margin */
  --space-4:   32px;   /* Container outer padding */
  --space-6:   48px;   /* Header height offset */
  --space-8:   64px;   /* Large component separation */

  /* Border Radius Tokens */
  --radius-xs: 4px;    /* Micro tags, input borders */
  --radius-sm: 8px;    /* Standard buttons, dropdown menus */
  --radius-md: 12px;   /* Food cards, table cells */
  --radius-lg: 16px;   /* Modals, bottom sheet drawers */
  --radius-xl: 24px;   /* Hero action cards */
  --radius-full: 9999px; /* Avatar, pill badges, floating action buttons */

  /* Box Shadow & Elevation Scale */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  --shadow-glow-active: 0 0 15px rgba(255, 107, 0, 0.35);
  --shadow-glow-kds-alert: 0 0 20px rgba(239, 68, 68, 0.6);
}
```

---

### 1.5 Micro-Interactions, CSS Keyframe Animations & SignalR Pulse Rules

#### A. Micro-interaction Specifications:
- **Button Touch Feedback:** Khi người dùng click/tap vào nút bấm, kích hoạt hiệu ứng `transform: scale(0.97)` trong `80ms` với `transition: transform 80ms ease-out`.
- **Drawer Bottom-Sheet Slide Up:** Modals tùy chỉnh món và giỏ hàng xuất hiện từ dưới lên với hiệu ứng `cubic-bezier(0.16, 1, 0.3, 1)` thời gian `250ms`.
- **SignalR Real-time Badge Pulse:** Khi có tin nhắn/đơn hàng mới từ SignalR, badge cập nhật hiệu ứng vòng tròn nhấp nháy tỏa rộng (Ripple Effect).

#### B. CSS Keyframe Code Specifications:

```css
/* 1. KDS Overdue Card Flashing Alert (> 10 mins) */
@keyframes kds-overdue-flash {
  0%, 100% {
    border-color: #EF4444;
    box-shadow: 0 0 20px rgba(239, 68, 68, 0.8);
    background-color: #450A0A;
  }
  50% {
    border-color: #7F1D1D;
    box-shadow: 0 0 5px rgba(239, 68, 68, 0.2);
    background-color: #1E293B;
  }
}

.kds-card-overdue {
  animation: kds-overdue-flash 1.2s infinite ease-in-out;
}

/* 2. SignalR Live Status Indicator Pulse Ring */
@keyframes signalr-pulse-ring {
  0% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
  }
  70% {
    transform: scale(1);
    box-shadow: 0 0 0 10px rgba(34, 197, 94, 0);
  }
  100% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(34, 197, 94, 0);
  }
}

.signalr-online-dot {
  width: 10px;
  height: 10px;
  background-color: #22C55E;
  border-radius: 50%;
  animation: signalr-pulse-ring 1.8s infinite ease-in-out;
}

/* 3. Skeleton Loading Shimmer Animation */
@keyframes shimmer-sweep {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton-loader {
  background: linear-gradient(90deg, #E2E8F0 25%, #F1F5F9 50%, #E2E8F0 75%);
  background-size: 200% 100%;
  animation: shimmer-sweep 1.5s infinite;
}
```

---

### 1.6 Hardware Profile & Target Resolution Matrix

| Profile ID | Target Hardware | Resolution / Aspect Ratio | Orientation | Target Touch Target | User Role & Context |
|---|---|---|---|---|---|
| `HW-MOB-PWA` | iPhone / Android Phones | 375x812px đến 430x932px | Portrait (Dọc) | ≥ 44x44px | Khách hàng quét QR gọi món tại bàn |
| `HW-MOB-STAFF`| Handheld POS / Android Phone | 360x800px | Portrait (Dọc) | ≥ 48x48px | Phục vụ di động, nhận tin báo, thu tiền |
| `HW-KDS-TAB` | KDS Android Tablet / Industrial TV | 1280x800px / 1920x1080px | Landscape (Ngang) | ≥ 56x56px (Găng tay bếp)| Bếp & Barista nhận đơn và bump món |
| `HW-POS-SUNMI`| Sunmi T2 / D2 Desktop POS | 15.6" Main (1920x1080) + 10.1" Secondary (1024x600) | Landscape | ≥ 52x52px | Thu ngân POS + Màn hình phụ hướng Khách |
| `HW-DESK-WEB` | PC / Mac / iPad Pro Desktop | 1280x800px đến 1920x1080px+ | Landscape | Mouse / Touch | Quản lý chi nhánh & Admin quản trị toàn chuỗi |

---

## 📱 CHƯƠNG 2: NHÓM 1 — GIAO DIỆN QR MENU (CUSTOMER PWA - 9 MÀN HÌNH)

---

### 2.1 SCR-PWA-01: Phone Check-in & Table Verification Screen

- **Mã màn hình:** `SCR-PWA-01`
- **Tên màn hình:** Xác thực Số điện thoại Khách hàng & Bàn ăn (Check-in PWA)
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Viewport 375px - 430px, Responsive Mobile Portrait)
- **Mục đích:** Khi khách quét mã QR tại bàn, màn hình xác nhận thông tin Bàn (Branch & Table ID), cho phép nhập SĐT để tích điểm thành viên CRM và kích hoạt phiên đặt món.

```
┌─────────────────────────────────────────────────────────┐
│ [10:42]                                        📶 🔋 100%│
├─────────────────────────────────────────────────────────┤
│                       SMART F&B OS                      │
│                  HIGH-LAND COFFEE CHUỖI                 │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │ 📍 CHI NHÁNH QUẬN 1 - TPHCM                     │   │
│   │ 🪑 BÀN SỐ: T-04 (Khu Vực Tầng Trệt)             │   │
│   └─────────────────────────────────────────────────┘   │
│                                                         │
│         [ ICON CAFE ARTWORK - VECTOR BRAND 120x120 ]    │
│                                                         │
│   Chào mừng Quý khách đến với High-Land Coffee!         │
│   Vui lòng nhập SĐT để tích điểm & nhận ưu đãi 15%:     │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │ 📱 Số Điện Thoại: [ 0908 123 456             ]  │   │
│   └─────────────────────────────────────────────────┘   │
│   [!] SĐT này giúp bạn nhận quà sinh nhật & theo dõi đơn │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │  [X] Tôi đồng ý với Điều khoản & Thể lệ Loyalty │   │
│   └─────────────────────────────────────────────────┘   │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │ [  BẮT ĐẦU ĐẶT MÓN NGAY (START ORDERING)  ]     │   │
│   └─────────────────────────────────────────────────┘   │
│                                                         │
│              -- HOẶC TIẾP TỤC VỚI TƯ CÁCH --             │
│   [ Bỏ qua tích điểm, Đặt món Ẩn danh (Guest Order) ]    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Header Banner:** Logo Quán (Outfit 20px Bold), Tên Chi nhánh (`branch_name`), Tên Bàn (`table_code` = "T-04").
2. **Form Check-in Input:**
   - Input Field `phone_number`: Type Tel, Placeholder `09xx xxx xxx`, Validate Regex Việt Nam (`^(03|05|07|08|09)+[0-9]{8}$`).
   - Terms Checkbox: State Checked mặc định.
3. **Primary CTA Button:** Text "BẮT ĐẦU ĐẶT MÓN NGAY", Gradient Amber `#FF6B00`, Active Scale 0.97.
4. **Secondary Link Button:** Text "Đặt món Ẩn danh", Style Ghost Text `#64748B`.
5. **Interactive Behavior & SignalR Triggers:**
   - Khi bấm CTA -> Kiểm tra SĐT trong DB -> Nếu tồn tại -> Load thông tin thành viên (Tên + Điểm tích lũy).
   - Gọi API `POST /api/v1/pwa/sessions/checkin` -> Tạo `SessionToken` lưu trong `localStorage`.

---

### 2.2 SCR-PWA-02: Interactive Menu Grid & Category Navigator

- **Mã màn hình:** `SCR-PWA-02`
- **Tên màn hình:** Danh mục & Lưới Món ăn Tương tác (Menu PWA Grid)
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Viewport 375px - 430px)
- **Mục đích:** Hiển thị danh mục món ăn dạng Sticky Bar, Lưới sản phẩm với hình ảnh trực quan, giá tiền, badge Best Seller, và nút thêm nhanh vào giỏ.

```
┌─────────────────────────────────────────────────────────┐
│ 📍 High-Land Q1 | Bàn T-04           [ 🔍 ] [ 👤 150p ] │
├─────────────────────────────────────────────────────────┤
│ 📢 ƯU ĐÃI: Giảm 20k cho combo Cà Phê + Bánh Mì T8!      │
├─────────────────────────────────────────────────────────┤
│ [ TẤT CẢ ] [ CÀ PHÊ ] [ TRÀ TRÁI CÂY ] [ BÁNH ] [ KHÁC]│ <-- Sticky Tabs
├─────────────────────────────────────────────────────────┤
│ ⚡ MÓN HOT BÁN CHẠY (BEST SELLERS)                       │
│ ┌───────────────────────────┐ ┌──────────────────────────┐│
│ │ [ HÌNH ẢNH MÓN 160x120 ]  │ │ [ HÌNH ẢNH MÓN 160x120 ] ││
│ │ 🔥 Best Seller            │ │ 🌿 Organic Tea           ││
│ │ Phin Sữa Đá Premium       │ │ Trà Đào Cam Sả Rơm       ││
│ │ 39.000đ  <s>45.000đ</s>   │ │ 49.000đ                  ││
│ │ [ + THÊM MÓN ]            │ │ [ + THÊM MÓN ]           ││
│ └───────────────────────────┘ └──────────────────────────┘│
│ ┌───────────────────────────┐ ┌──────────────────────────┐│
│ │ Bánh Mì Bò Nướng Phô Mai  │ │ Bạc Xỉu Sương Sáo Lạnh   ││
│ │ 35.000đ                   │ │ 42.000đ                  ││
│ │ [ + THÊM MÓN ]            │ │ [ + THÊM MÓN ]           ││
│ └───────────────────────────┘ └──────────────────────────┘│
├─────────────────────────────────────────────────────────┤
│ 🤖 [ BẠN CẦN AI GỢI Ý MÓN TRÁI CÂY / CÀ PHÊ? (CHATBOT) ]│
├─────────────────────────────────────────────────────────┤
│ 🛒 GIỎ HÀNG (3 món) - 123.000đ         [ XEM GIỎ HÀNG >]│ <-- Floating Bar
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Sticky Category Bar:** Scroll ngang overflow, Active state đổi màu Tab thành Background Orange `#FF6B00` + Text White.
2. **Food Item Cards:**
   - Card Thumbnail: `160x120px` Object-fit cover, Lazy-loading image.
   - Badge Tag: "🔥 Best Seller" (Background Red `#EF4444`), "🌿 Organic" (Background Green `#22C55E`).
   - Price Display: Current Price (Outfit 16px Bold `#FF6B00`), Original Price (Strike-through `#94A3B8`).
   - Add Button: Touch target `44x44px`, icon `+`, bấm vào mở Drawer tùy chỉnh (`SCR-PWA-03`).
3. **Floating Cart Bar (Footer Sticky):** Mới thêm món sẽ có animation nảy nảy (Bounce 300ms), hiển thị Tổng số lượng + Tổng tiền.

---

### 2.3 SCR-PWA-03: Dish Item Customization Modal / Drawer

- **Mã màn hình:** `SCR-PWA-03`
- **Tên màn hình:** Modal Tùy chỉnh Món (Size, Topping, Ghi chú Bếp)
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Bottom-sheet Drawer Slide-up Animation)
- **Mục đích:** Cho phép chọn Kích thước (Size S/M/L), Mức đường/đá, Topping đi kèm, và nhập Ghi chú riêng cho Bartender/Bếp.

```
┌─────────────────────────────────────────────────────────┐
│                       [ ═══ DRAWER HANDLE ═══ ]          │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ HÌNH ẢNH CHI TIẾT MÓN MẮT 375x200PX ]             │ │
│ └─────────────────────────────────────────────────────┘ │
│ ✕ CLOSE                                                 │
│ Phin Sữa Đá Premium                                     │
│ 39.000đ — Cà phê đậm đà pha phin truyền thống          │
├─────────────────────────────────────────────────────────┤
│ 1. CHỌN KÍCH THƯỚC (SIZE) * Bắt buộc                     │
│ (•) Size M (Tiêu chuẩn)                     +0đ         │
│ ( ) Size L (Khổng lồ)                       +10.000đ    │
├─────────────────────────────────────────────────────────┤
│ 2. MỨC ĐƯỜNG & ĐÁ                                       │
│ Đường: [ 0% ] [ 30% ] [ (•) 70% ] [ 100% ]              │
│ Đá:    [ Ít đá ] [ (•) Vừa đá ] [ Nhiều đá ]            │
├─────────────────────────────────────────────────────────┤
│ 3. THÊM TOPPING TÙY CHỌN                                │
│ [X] Thạch Cà Phê                            +8.000đ     │
│ [ ] Sương Sáo Đen                           +6.000đ     │
│ [X] Shot Espresso Thêm                      +12.000đ    │
├─────────────────────────────────────────────────────────┤
│ 📝 GHI CHÚ CHO BẾP/PHA CHẾ                              │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Ít sữa đặc, cho đá riêng vào ly nhựa...             │ │
│ └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ Số lượng:  [ - ]   1   [ + ]     TỔNG: 59.000đ          │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [   + THÊM VÀO GIỎ HÀNG — 59.000đ (ADD TO CART)   ] │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Radio Group (Size):** Single selection, validate bắt chọn 1 option.
2. **Pill Segmented Control (Đường/Đá):** Multi-button horizontal group, Active item highlight Border `#FF6B00`.
3. **Checkbox List (Topping):** Multi-selection, cập nhật thời gian thực vào biến `DynamicTotalPrice`.
4. **Textarea Note:** Max length 150 ký tự, placeholder "Ít đường, không đá...".
5. **Dynamic Price Calculator Formula:**
   `TotalPrice = (BasePrice + SizeExtra + Sum(ToppingPrice)) * Quantity`.

---

### 2.4 SCR-PWA-04: Shopping Cart & Checkout Order Summary

- **Mã màn hình:** `SCR-PWA-04`
- **Tên màn hình:** Xem Giỏ Hàng & Tóm Tắt Đơn Hàng (Cart & Checkout PWA)
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Viewport 375px - 430px)
- **Mục đích:** Khách kiểm tra danh sách món, chỉnh sửa số lượng, áp mã giảm giá AI Voucher, chọn hình thức gửi bếp và xác nhận Đặt Món.

```
┌─────────────────────────────────────────────────────────┐
│ ← Tiếp tục chọn món | GIỎ HÀNG (BÀN T-04)    [ XÓA TẤT ]│
├─────────────────────────────────────────────────────────┤
│ DANH SÁCH MÓN ĐÃ CHỌN (3 MÓN)                           │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 1x Phin Sữa Đá Premium                      59.000đ │ │
│ │    • Size L, 70% Đường, Thạch Cà Phê                 │ │
│ │    • Note: Ít sữa đặc                               │ │
│ │    [ - ]  1  [ + ]                     [ 🗑️ Xóa ]   │ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ 2x Trà Đào Cam Sả Rơm                       98.000đ │ │
│ │    • Size M, 100% Đá                                │ │
│ │    [ - ]  2  [ + ]                     [ 🗑️ Xóa ]   │ │
│ └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ 🎟️ MÃ GIẢM GIÁ / VOUCHER AI                             │
│ ┌───────────────────────────┬─────────────────────────┐ │
│ │ [ Nhập mã: SUMMERCAMP20 ] │ [ ÁP DỤNG ]             │ │
│ └───────────────────────────┴─────────────────────────┘ │
│ 🟢 Voucher "SUMMERCAMP20": Giảm 20.000đ đã được áp dụng!│
├─────────────────────────────────────────────────────────┤
│ CHI TIẾT THANH TOÁN                                     │
│ Tạm tính:                                    157.000đ   │
│ Giảm giá Voucher:                            -20.000đ   │
│ Phí dịch vụ (0%):                                 0đ   │
│ ─────────────────────────────────────────────────────── │
│ TỔNG CỘNG:                                   137.000đ   │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ ⚡ GỬI ĐƠN XUỐNG BẾP NGAY (CONFIRM & ORDER) ]     │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Order Item List:** Render mảng `items`, có nút bấm `+`, `-` tăng giảm số lượng. Khi `quantity = 0` sẽ mở Confirm Dialog xóa món.
2. **Voucher Validation:** Input Code + Button Áp dụng. Khi thành công hiển thị Text Green `#22C55E` kèm số tiền giảm.
3. **Primary Action Button:** Text "GỬI ĐƠN XUỐNG BẾP NGAY", bấm vào trigger SignalR Event `SendOrderToKitchen` và chuyển khách sang màn hình Tracking `SCR-PWA-06`.

---

### 2.5 SCR-PWA-05: AI Sommelier / Food Chatbot Assistant Drawer

- **Mã màn hình:** `SCR-PWA-05`
- **Tên màn hình:** Trợ lý AI Tư Vấn Món Ăn (AI Food Chatbot Drawer)
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Slide-in Right / Overlay Drawer)
- **Mục đích:** Chatbot AI hỗ trợ tư vấn đồ uống/món ăn theo khẩu vị, thời tiết, hoặc ngân sách của khách. Khách có thể nhấn "Thêm vào giỏ" trực tiếp từ câu trả lời của AI.

```
┌─────────────────────────────────────────────────────────┐
│ 🤖 TRỢ LÝ AI GỢI Ý MÓN (AI SOMMELIER)         [ ✕ ĐÓNG ]│
├─────────────────────────────────────────────────────────┤
│ [AI] 👋 Chào bạn! Hôm nay trời nắng 34°C, bạn muốn chọn │
│      món nước giải nhiệt thanh mát hay cà phê tỉnh táo? │
│                                                         │
│                      [ 🍊 Trà trái cây giải nhiệt ]     │
│                      [ ☕ Cà phê đắng nhẹ tỉnh táo ]    │
│                      [ 🍰 Bánh ngọt dùng kèm trà ]      │
├─────────────────────────────────────────────────────────┤
│ [ Khách ] Tôi muốn uống món gì ít ngọt, mát lạnh có đào │
├─────────────────────────────────────────────────────────┤
│ [AI] 💡 Dựa trên sở thích của bạn, mình gợi ý 2 món:   │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 🍹 Trà Đào Cam Sả Rơm (Ít ngọt 50%)                │ │
│ │ Giá: 49.000đ | ⭐ 4.9 (240 đánh giá)                │ │
│ │ 🎯 Giảm 50% đường, vị sả thơm nức.                   │ │
│ │ [ + THÊM NHANH VÀO GIỎ ]                            │ │
│ └─────────────────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 🍧 Trà Lục Trà Ép Đào Tươi Lạnh                     │ │
│ │ Giá: 45.000đ | ⭐ 4.8 (110 đánh giá)                │ │
│ │ [ + THÊM NHANH VÀO GIỎ ]                            │ │
│ └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┬───────────┐ │
│ │ [ Nhập câu hỏi cho AI...               ]│ [ GỬI ➔ ] │ │
│ └─────────────────────────────────────────┴───────────┘ │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Chat Bubble History:** Phân biệt User Bubble (Background Amber Light `#FFEDD5`, Align Right) và AI Bubble (Background Slate Light `#F1F5F9`, Align Left).
2. **Quick Prompt Chips:** Nút nhấn nhanh câu hỏi gợi ý dạng Pill Buttons.
3. **Embedded Recommendation Card:** Card sản phẩm tích hợp trực tiếp nút "THÊM NHANH VÀO GIỎ", tự động cập nhật Zustand Store Cart.

---

### 2.6 SCR-PWA-06: Real-time Order Status Tracker (SignalR Pulse)

- **Mã màn hình:** `SCR-PWA-06`
- **Tên màn hình:** Theo Dõi Trạng Thái Đơn Hàng Real-time (SignalR Progress Tracker)
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Viewport 375px - 430px)
- **Mục đích:** Khách hàng xem tiến độ chế biến đơn hàng theo thời gian thực (Đã nhận đơn -> Bếp đang làm -> Đã xong/Đang giao -> Đã phục vụ tại bàn).

```
┌─────────────────────────────────────────────────────────┐
│ 📍 High-Land Q1 | ĐƠN HÀNG #ORD-8892 (BÀN T-04)        │
├─────────────────────────────────────────────────────────┤
│ TRẠNG THÁI ĐƠN HÀNG REAL-TIME                           │
│                                                         │
│  (✓) ĐÃ NHẬN  ─── (🟢) BẾP ĐANG LÀM ─── ( ) ĐANG GIAO  │
│  10:45 AM          10:47 AM (Pulse)     Dự kiến 10:52   │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ⏳ BẾP ĐÃ NHẬN ĐƠN VÀ ĐANG THỰC HIỆN!                │ │
│ │ Thời gian chờ dự kiến: 5 - 7 phút.                  │ │
│ │ (Tự động cập nhật qua WebSocket SignalR...)         │ │
│ └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ CHI TIẾT MÓN TRONG ĐƠN #ORD-8892                        │
│ • 1x Phin Sữa Đá Premium         [ 🟢 Đang pha chế ]    │
│ • 2x Trà Đào Cam Sả Rơm          [ ⏳ Đợi xếp hàng ]    │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ 🔔 GỌI PHỤC VỤ (CALL WAITER) ]                     │ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ [ 🧾 YÊU CẦU TÍNH TIỀN / BILL (REQUEST BILL) ]       │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **SignalR Progress Step Bar:** 4 Bước với Node Icon. Bước hiện tại có hiệu ứng `signalr-pulse-ring` xanh lá nhấp nháy.
2. **Item Status List:** Hiển thị chi tiết từng món với Badge trạng thái (`Chờ làm`, `Đang pha chế`, `Đã xong`).
3. **Service Trigger Buttons:** Nút "Gọi phục vụ" và "Yêu cầu tính tiền" kích hoạt Overlay `SCR-PWA-07`.

---

### 2.7 SCR-PWA-07: Call Staff & Service / Bill Request Overlay

- **Mã màn hình:** `SCR-PWA-07`
- **Tên màn hình:** Overlay Yêu Cầu Phục Vụ & Gọi Bill Tại Bàn
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Modal Overlay Center/Bottom)
- **Mục đích:** Khách gửi yêu cầu hỗ trợ (lấy thêm đá, thêm ly, lấy ớt) hoặc yêu cầu thanh toán (Tiền mặt, VietQR, Thẻ).

```
┌─────────────────────────────────────────────────────────┐
│ 🔔 YÊU CẦU HỖ TRỢ TẠI BÀN T-04                [ ✕ ĐÓNG ]│
├─────────────────────────────────────────────────────────┤
│ CHỌN LOẠI YÊU CẦU:                                      │
│                                                         │
│ ┌───────────────────────────┐ ┌──────────────────────────┐│
│ │ 🧊 LẤY THÊM ĐÁ / LY TRỐNG │ │ 🧾 YÊU CẦU THANH TOÁN    ││
│ │ [ BẤM GỬI YÊU CẦU ]       │ │ [ BẤM GỬI YÊU CẦU ]     ││
│ └───────────────────────────┘ └──────────────────────────┘│
│ ┌───────────────────────────┐ ┌──────────────────────────┐│
│ │ 🥢 LẤY KHĂN LẠNH / ỚT TƯƠI│ │ 👨‍🍳 GẶP QUẢN LÝ BÀN     ││
│ │ [ BẤM GỬI YÊU CẦU ]       │ │ [ BẤM GỬI YÊU CẦU ]     ││
│ └───────────────────────────┘ └──────────────────────────┘│
├─────────────────────────────────────────────────────────┤
│ NẾU THANH TOÁN, CHỌN PHƯƠNG THỨC:                       │
│ (•) Quét mã VietQR (Tự động xác nhận)                   │
│ ( ) Tiền mặt tại bàn (Nhân viên mang tiền thừa)         │
│ ( ) Quẹt thẻ POS (Visa/Mastercard/ATM)                  │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [   🔔 GỬI THÔNG BÁO TỚI NHÂN VIÊN PHỤC VỤ   ]      │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Grid Quick Options:** 4 Thẻ yêu cầu dịch vụ dạng Icon + Label.
2. **Payment Method Selector:** Radio List cho phép nhân viên chuẩn bị đúng thiết bị khi tới bàn.
3. **SignalR Broadcast Trigger:** Khi bấm nút -> Bắn Event SignalR `NewServiceRequest` tới ứng dụng Staff App (`SCR-STAFF-01`).

---

### 2.8 SCR-PWA-08: Photo Feedback & Staff Tip Rating Modal

- **Mã màn hình:** `SCR-PWA-08`
- **Tên màn hình:** Modal Đánh Giá 5 Sao, Tải Ảnh Feedback & Tip Nhân Viên
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Viewport 375px - 430px)
- **Mục đích:** Cho phép khách hàng trải nghiệm đánh giá dịch vụ sau khi hoàn thành bữa ăn, tải ảnh chụp món ăn và tặng tiền Tip cho đội ngũ phục vụ.

```
┌─────────────────────────────────────────────────────────┐
│ ⭐ ĐÁNH GIÁ TRẢI NGHIỆM TẠI HIGH-LAND         [ ✕ ĐÓNG ]│
├─────────────────────────────────────────────────────────┤
│ BẠN THẤY MÓN ĂN & DỊCH VỤ THẾ NÀO?                      │
│                                                         │
│               ⭐  ⭐  ⭐  ⭐  ⭐                        │
│             [ Tuyệt vời! (5/5 Stars) ]                  │
│                                                         │
│ CHỤP VÀ TẢI ẢNH FEEDBACK (NHẬN 50 ĐIỂM REWARD):         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 📸 [ + Tải ảnh món ăn của bạn lên (Max 3 ảnh) ]     │ │
│ │ (File đính kèm: ly_cafe_phin.jpg - 1.2MB ✓)          │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ LỜI NHẮN CHI TIẾT:                                      │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Cà phê rất ngon, bạn nhân viên Nam phục vụ rất chu  │ │
│ │ đáo và nhiệt tình!                                  │ │
│ └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ 💡 TẶNG TIỀN TIP TÙY CHỌN CHO PHỤC VỤ (STAFF TIP):       │
│ [ 10.000đ ]   [ (•) 20.000đ ]   [ 50.000đ ]   [ Khác ]  │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ 🚀 GỬI ĐÁNH GIÁ & HOÀN TẤT BỮA ĂN (SUBMIT) ]     │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Interactive Star Rating:** 5 Ngôi sao lớn touch target `40x40px`, hiệu ứng hover/tap đổi màu Vàng `#F59E0B`.
2. **Photo Dropzone Uploader:** HTML File Input accept `image/*`, xem trước Thumbnail 60x60px.
3. **Staff Tip Segmented Buttons:** Danh sách các mức Tip nhanh.
4. **Emergency Rule:** Nếu số sao ≤ 2 -> Tự động kích hoạt luồng cảnh báo tới Manager App (`SCR-MGR-05`).

---

### 2.9 SCR-PWA-09: Customer Loyalty Wallet & History

- **Mã màn hình:** `SCR-PWA-09`
- **Tên màn hình:** Ví Thành Viên Loyalty & Lịch Sử Tích Điểm
- **Thiết bị mục tiêu:** `HW-MOB-PWA` (Viewport 375px - 430px)
- **Mục đích:** Hiển thị thẻ thành viên điện tử (Member Tier Card), số điểm hiện có, danh sách voucher đổi thưởng và lịch sử giao dịch đơn hàng.

```
┌─────────────────────────────────────────────────────────┐
│ ← Menu | VÍ THÀNH VIÊN LOYALTY                [ ⚙️ ]   │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 💳 HỘI VIÊN VÀNG (GOLD MEMBER)                       │ │
│ │ Khách hàng: NGUYỄN VĂN A | SĐT: 0908***456          │ │
│ │                                                     │ │
│ │ 🌟 ĐIỂM TÍCH LŨY: 1,250 PTS                         │ │
│ │ [ Progress Bar: 1,250 / 2,000 PTS nâng hạng PLATINUM]│ │
│ └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ 🎁 VOUCHER ĐỔI THƯỞNG CỦA BẠN (3 VOUCHER)               │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ☕ Đổi 500pt -> 01 Phin Sữa Đá Free     [ ĐỔI NGAY ]│ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ 🍰 Đổi 300pt -> Giảm 15% Bánh Ngọt      [ ĐỔI NGAY ]│ │
│ └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ 📜 LỊCH SỬ ĐƠN HÀNG GẦN ĐÂY                             │
│ • #ORD-8892 | 13/08/2026 | 137.000đ (+13 pts)         │
│ • #ORD-7710 | 10/08/2026 | 210.000đ (+21 pts)         │
└─────────────────────────────────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Digital Loyalty Card Component:** Gradient Gold background (`linear-gradient(135deg, #F59E0B, #B45309)`), Text White.
2. **Progress Bar Component:** Width % tương ứng số điểm tích lũy.
3. **Reward Redeem Action:** Bấm "ĐỔI NGAY" gọi API `POST /api/v1/loyalty/redeem`.

---

## 🍳 CHƯƠNG 3: NHÓM 2 — KITCHEN DISPLAY SYSTEM (KDS BẾP - 4 MÀN HÌNH)

---

### 3.1 SCR-KDS-01: Kitchen Ticket Grid with Dynamic Timer Cards

- **Mã màn hình:** `SCR-KDS-01`
- **Tên màn hình:** Màn Hình Thẻ Đơn Hàng Bếp & Barista (KDS Kanban Ticket Grid)
- **Thiết bị mục tiêu:** `HW-KDS-TAB` (1920x1080 Full HD Landscape KDS Terminal)
- **Mục đích:** Màn hình chính của KDS Bếp, hiển thị danh sách thẻ đơn hàng dạng cột Kanban, tự động đếm thời gian chế biến với 3 cấp độ màu sắc cảnh báo.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🧋 KDS BẾP - CHI NHÁNH QUẬN 1 | Tổng đơn chờ: 4 | Đơn trễ: 1                   [ Mode: Kanban ] [ 🔔 ]  │
├────────────────────────────────────┬────────────────────────────────────┬───────────────────────────────┤
│ 📌 THẺ #ORD-8891 | BÀN T-02        │ 📌 THẺ #ORD-8892 | BÀN T-04        │ 📌 THẺ #ORD-8889 | BÀN T-08   │
│ ⏱️ 03:45 (🟢 BÌNH THƯỜNG < 5m)     │ ⏱️ 08:12 (🟡 CẢNH BÁO 5-10m)      │ ⏱️ 14:30 (🔴 OVERDUE > 10m)   │
├────────────────────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ • 1x Bạc Xỉu Lạnh (Ít đá)          │ • 1x Phin Sữa Đá (Size L)          │ • 2x Phở Bò Tái Nạm (Không hành)│
│ • 1x Trà Vải Lài                   │   - Note: Ít sữa đặc               │ • 1x Quẩy Giòn (2 cái)        │
│                                    │ • 2x Trà Đào Cam Sả Rơm            │                               │
├────────────────────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ [ 👨‍🍳 BẮT ĐẦU CHẾ BIẾN ]           │ [ 👨‍🍳 BẮT ĐẦU CHẾ BIẾN ]           │ [ ⚠️ BÁO ƯU TIÊN RA MÓN ]     │
│ [ 🚀 HOÀN THÀNH (BUMP TICKET) ]    │ [ 🚀 HOÀN THÀNH (BUMP TICKET) ]    │ [ 🚀 HOÀN THÀNH (BUMP TICKET) ]│
└────────────────────────────────────┴────────────────────────────────────┴───────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Dynamic Timer Banner:**
   - `< 5 phút`: Background Green `#064E3B`, Border `#22C55E`.
   - `5 - 10 phút`: Background Amber `#451A03`, Border `#F59E0B`.
   - `> 10 phút`: Background Red `#450A0A`, Border `#EF4444` kèm animation nhấp nháy `kds-overdue-flash`.
2. **Bump Action Button:** Touch target lớn `56x56px` màu Xanh Dương `#2563EB`. Bấm vào sẽ ẩn thẻ khỏi KDS và phát tín hiệu SignalR `KdsTicketStatusChanged` báo cho Phục vụ.

---

### 3.2 SCR-KDS-02: Consolidated Dish & Table-Aggregated Summary View

- **Mã màn hình:** `SCR-KDS-02`
- **Tên màn hình:** Màn Hình Gộp Món Ăn Bếp (Aggregated Batch View)
- **Thiết bị mục tiêu:** `HW-KDS-TAB` (1920x1080 Landscape)
- **Mục đích:** Giúp đầu bếp/barista xem tổng số lượng từng món cần chế biến trên tất cả các bàn hiện tại để nấu/pha chế theo mẻ (Batch Processing).

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 📊 TỔNG HỢP MÓN CẦN CHẾ BIẾN TOÀN BẾP (BATCH COOKING VIEW)                    [ Xem theo Thẻ Đơn ]     │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TÊN MÓN ĂN / ĐỒ UỐNG                  │ TỔNG SL CHỜ │ CHI TIẾT THEO BÀN                │ HÀNH ĐỘNG    │
├───────────────────────────────────────┼─────────────┼──────────────────────────────────┼──────────────┤
│ 🍵 Trà Đào Cam Sả Rơm                 │  8 Ly       │ Bàn T-04 (2), Bàn T-07 (4), T-09 (2)│ [ 🚀 XONG MẺ]│
│ ☕ Phin Sữa Đá Premium                 │  5 Ly       │ Bàn T-02 (1), Bàn T-04 (1), T-12 (3)│ [ 🚀 XONG MẺ]│
│ 🍜 Phở Bò Tái Nạm                     │  4 Bát      │ Bàn T-08 (2), Bàn T-15 (2)       │ [ 🚀 XONG MẺ]│
│ 🥖 Bánh Mì Bò Nướng Phô Mai           │  3 Ổ        │ Bàn T-03 (1), Bàn T-07 (2)       │ [ 🚀 XONG MẺ]│
└───────────────────────────────────────┴─────────────┴──────────────────────────────────┴──────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Aggregated Quantities Matrix:** Tự động gom nhóm theo `dish_id`, tính tổng `SUM(quantity)`.
2. **Batch Bump Button:** Nút "XONG MẺ" cho phép bump hàng loạt món đó trên tất cả các đơn hàng liên quan.

---

### 3.3 SCR-KDS-03: Recipe Specification & Plating Guide Modal

- **Mã màn hình:** `SCR-KDS-03`
- **Tên màn hình:** Modal Hướng Dẫn Định Lượng & Quy Chuẩn Decor Món
- **Thiết bị mục tiêu:** `HW-KDS-TAB` (Modal Dialog Center KDS)
- **Mục đích:** Hiển thị công thức pha chế/nấu ăn, định lượng nguyên vật liệu và hình ảnh decor chuẩn để nhân viên mới làm đúng SOP.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 📖 QUY CHUẨN PHA CHẾ: TRÀ ĐÀO CAM SẢ RƠM                          [ ✕ ĐÓNG ]     │
├─────────────────────────────────────────┬────────────────────────────────────────┤
│ [ HÌNH ẢNH MÓN DECOR CHUẨN 400x300PX ]  │ 🧪 ĐỊNH LƯỢNG NGUYÊN LIỆU (SIZE L):    │
│                                         │ • Cốt Trà Lục Trà: 120ml               │
│                                         │ • Siro Đào Monin:  30ml                │
│                                         │ • Nước Cốt Cam Tươi: 15ml              │
│                                         │ • Cây Sả Tươi Dập Mập: 1 Cây           │
│                                         │ • Đào Miếng Ngâm: 3 Miếng              │
│                                         ├────────────────────────────────────────┤
│                                         │ 👨‍🍳 BƯỚC THỰC HIỆN:                   │
│                                         │ 1. Lấy 120ml cốt trà lắc đều với đá.   │
│                                         │ 2. Rót ra ly, decor 3 miếng đào trên   │
│                                         │    mặt ly kèm cây sả đập dập.          │
└─────────────────────────────────────────┴────────────────────────────────────────┘
```

---

### 3.4 SCR-KDS-04: Barista / Kitchen Out-of-Stock (86 Dish) Toggle

- **Mã màn hình:** `SCR-KDS-04`
- **Tên màn hình:** Bảng Cảnh Báo Báo Hết Món Nhanh (86 Out-of-Stock Toggle)
- **Thiết bị mục tiêu:** `HW-KDS-TAB` (Full Screen Matrix)
- **Mục đích:** Barista hoặc Bếp trưởng bật/tắt nhanh trạng thái Còn hàng / Tạm hết hàng của từng món. Trạng thái lập tức đồng bộ real-time sang QR PWA và POS Thu ngân.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🚫 BẢNG BÁO HẾT MÓN NHANH (OUT OF STOCK - 86 TOGGLE MATRIX)                   [ 🔄 ĐỒNG BỘ REAL-TIME ] │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SEARCH: [ 🔍 Nhập tên món cần báo hết...                             ]                          │
├───────────────────────────────────────┬───────────────────────────────────┬─────────────────────────────┤
│ 🍵 Trà Đào Cam Sả Rơm                 │ ☕ Phin Sữa Đá Premium             │ 🍞 Bánh Mì Bơ Tỏi           │
│ Trạng thái: 🟢 CÒN HÀNG               │ Trạng thái: 🟢 CÒN HÀNG           │ Trạng thái: 🔴 BÁO HẾT MÓN  │
│ [ TOGGLE:  ON (CÒN HÀNG) ]            │ [ TOGGLE:  ON (CÒN HÀNG) ]        │ [ TOGGLE:  OFF (HẾT HÀNG) ] │
├───────────────────────────────────────┼───────────────────────────────────┼─────────────────────────────┤
│ 🍹 Trà Lục Trà Ép Đào                 │ 🍰 Bánh Mousse Dâu Tây            │ 🧋 Bạc Xỉu Sương Sáo        │
│ Trạng thái: 🔴 BÁO HẾT MÓN            │ Trạng thái: 🟢 CÒN HÀNG           │ Trạng thái: 🟢 CÒN HÀNG     │
│ [ TOGGLE:  OFF (HẾT HÀNG) ]           │ [ TOGGLE:  ON (CÒN HÀNG) ]        │ [ TOGGLE:  ON (CÒN HÀNG) ]  │
└───────────────────────────────────────┴───────────────────────────────────┴─────────────────────────────┘
```

#### Chi tiết Thành phần Layout & Data Fields:
1. **Switch Toggle Component:** Large Toggle Switch (Width 60px, Height 32px). State ON (Green `#22C55E`), State OFF (Red `#EF4444`).
2. **SignalR Broadcast:** Khi đổi Toggle -> Gửi SignalR Event `DishStockStatusChanged` cập nhật PWA của khách ngay tức thì.

---

## 💁 CHƯƠNG 4: NHÓM 3 — STAFF MOBILE & SUNMI POS DUAL-SCREEN (5 MÀN HÌNH)

---

### 4.1 SCR-STAFF-01: Waiter Service Notification Center

- **Mã màn hình:** `SCR-STAFF-01`
- **Tên màn hình:** Trung Tâm Thông Báo Yêu Cầu Phục Vụ (Staff Notification Alert)
- **Thiết bị mục tiêu:** `HW-MOB-STAFF` (Handheld Mobile POS / Smartphone 360x800)
- **Mục đích:** Nhân viên chạy bàn nhận thông báo tức thì từ khách (Gọi nước, lấy đá, yêu cầu bill) và từ KDS Bếp (Món đã làm xong sẵn sàng ra đồ).

```
┌─────────────────────────────────────────────────────────┐
│ 🔔 THÔNG BÁO CHẠY BÀN (STAFF ALERTS)          [🟢 Online]│
├─────────────────────────────────────────────────────────┤
│ YÊU CẦU MỚI NHẤT (REAL-TIME ALERTS)                     │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 🔴 BÀN T-04 | YÊU CẦU THANH TOÁN VIETQR              │ │
│ │ ⏱️ 30 giây trước | Khách yêu cầu mang mã VietQR     │ │
│ │ [ 🛠️ ĐÃ XỬ LÝ ]                  [ 📱 MỞ VIETQR ]   │ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ 🟢 BẾP BÁO RA MÓN | BÀN T-02                         │ │
│ │ ⏱️ 1 phút trước | 2x Trà Đào Cam Sả đã hoàn thành   │ │
│ │ [ 🛠️ XÁC NHẬN ĐÃ MANG RA BÀN ]                      │ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ 🟡 BÀN T-08 | GỌI THÊM ĐÁ & KHĂN LẠNH               │ │
│ │ ⏱️ 3 phút trước                                      │ │
│ │ [ 🛠️ ĐÃ XỬ LÝ ]                                     │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

### 4.2 SCR-STAFF-02: Interactive Floor Map & Real-time Table Matrix

- **Mã màn hình:** `SCR-STAFF-02`
- **Tên màn hình:** Sơ Đồ Bàn Trực Quan & Quản Lý Trạng Thái Bàn (Floor Map)
- **Thiết bị mục tiêu:** `HW-MOB-STAFF` / POS Tablet
- **Mục đích:** Hiển thị toàn bộ sơ đồ không gian quán theo Tầng/Khu vực. Mã màu phản ánh chính xác trạng thái thực tế của từng bàn.

```
┌─────────────────────────────────────────────────────────┐
│ 🗺️ SƠ ĐỒ BÀN - KHU VỰC: TẦNG TRỆT             [ CHỌN KHU]│
├─────────────────────────────────────────────────────────┤
│ [🟢 Bàn Trống (8)] [🔵 Đang Ăn (12)] [🟡 Gọi Bill (2)]   │
├─────────────────────────────────────────────────────────┤
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐   │
│ │ BÀN T-01     │ │ BÀN T-02     │ │ BÀN T-03     │   │
│ │ 🟢 BÀN TRỐNG  │ │ 🔵 ĐANG ĂN    │ │ 🟡 GỌI BILL   │   │
│ │ 4 Ghế         │ │ 145.000đ (25m)│ │ 320.000đ (40m)│   │
│ └───────────────┘ └───────────────┘ └───────────────┘   │
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐   │
│ │ BÀN T-04     │ │ BÀN T-05     │ │ BÀN T-06     │   │
│ │ 🔵 ĐANG ĂN    │ │ 🟢 BÀN TRỐNG  │ │ 🔴 CẢNH BÁO   │   │
│ │ 59.000đ (10m) │ │ 2 Ghế         │ │ Đơn trễ 15m!  │   │
│ └───────────────┘ └───────────────┘ └───────────────┘   │
└─────────────────────────────────────────────────────────┘
```

#### Mã Màu Trạng Thái Bàn Spec:
- `🟢 Green (#22C55E)`: Bàn trống sẵn sàng đón khách.
- `🔵 Blue (#3B82F6)`: Bàn đang có khách ăn uống.
- `🟡 Amber (#F59E0B)`: Khách đã bấm yêu cầu tính tiền.
- `🔴 Red (#EF4444)`: Bàn có sự cố / món trễ quá 15 phút.

---

### 4.3 SCR-STAFF-03: Mobile VietQR Payment Generator

- **Mã màn hình:** `SCR-STAFF-03`
- **Tên màn hình:** Tạo Mã VietQR Động Thu Tiền Tại Bàn (Mobile VietQR)
- **Thiết bị mục tiêu:** `HW-MOB-STAFF` (Smartphone Phục vụ)
- **Mục đích:** Nhân viên mở đơn hàng của bàn, hệ thống tạo mã VietQR động bao gồm chính xác Số tiền + Mã đơn hàng. Khi khách quét chuyển khoản, màn hình tự động đổi trạng thái "Thanh Toán Thành Công" qua Webhook Banking.

```
┌─────────────────────────────────────────────────────────┐
│ ← Bàn T-04 | THANH TOÁN VIETQR #ORD-8892                │
├─────────────────────────────────────────────────────────┤
│ TỔNG TIỀN CẦN THU: 137.000 VNĐ                          │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ┌─────────────────────────────────────────────────┐ │ │
│ │ │ [ 🖼️ HÌNH ẢNH MÃ VIETQR ĐỘNG NGÂN HÀNG MBBANK ] │ │ │
│ │ │ [ NỘI DUNG CK: SMARTFB ORD8892                ] │ │ │
│ │ └─────────────────────────────────────────────────┘ │ │
│ │ ⏳ Tự động làm mới mã sau: 25 giây...               │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ 🔄 TRẠNG THÁI: ⏳ Đang chờ ngân hàng báo Có (SignalR)... │
│ [ 🖨️ IN PHIẾU TẠM TÍNH ]       [ 💵 THU TIỀN MẶT ]      │
└─────────────────────────────────────────────────────────┘
```

---

### 4.4 SCR-POS-04: Sunmi 10.1" Customer Display Secondary Screen View

- **Mã màn hình:** `SCR-POS-04`
- **Tên màn hình:** Màn Hình Phụ Hướng Khách Sunmi POS (Secondary 10.1" Customer Screen)
- **Thiết bị mục tiêu:** `HW-POS-SUNMI` (Màn hình phụ 10.1 inch resolution 1024x600)
- **Mục đích:** Màn hình phụ hướng về phía khách tại quầy thu ngân Sunmi, hiển thị danh sách món đang order, tổng tiền, mã VietQR 30s tự động và banner quảng cáo combo.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ HIGH-LAND COFFEE Q1 | XIN CHÀO QUÝ KHÁCH!                                           [ 10:45 AM ] │
├────────────────────────────────────────┬─────────────────────────────────────────────────────────┤
│ CHI TIẾT ĐƠN HÀNG CỦA BẠN              │ QUÉT MÃ VIETQR ĐỂ THANH TOÁN TOÀN BỘ ĐƠN HÀNG            │
│ • 1x Phin Sữa Đá Premium      59.000đ  │ ┌─────────────────────────────────────────────────────┐ │
│ • 2x Trà Đào Cam Sả Rơm       98.000đ  │ │ [ 🖼️ MÃ VIETQR ĐỘNG 250x250PX - AUTOMATIC CHECK ]   │ │
│ ────────────────────────────────────── │ └─────────────────────────────────────────────────────┘ │
│ Tạm tính:                    157.000đ  │ STK: 9999888899 | Ngân hàng MBBank                     │
│ Voucher Giảm:                -20.000đ  │ TÊN TK: CONG TY SMART FB OS                             │
│ ────────────────────────────────────── │ ⏳ Mã QR hết hạn trong: 28 giây                         │
│ TỔNG CỘNG:                   137.000đ  │ 🎁 Tích được +13 Điểm Loyalty thành viên Gold           │
└────────────────────────────────────────┴─────────────────────────────────────────────────────────┘
```

---

### 4.5 SCR-STAFF-05: 30s Dynamic QR + 50m GPS Attendance Check-in

- **Mã màn hình:** `SCR-STAFF-05`
- **Tên màn hình:** Chấm Công Nhân Viên Bằng QR Động 30s & Tọa Độ GPS 50m
- **Thiết bị mục tiêu:** `HW-MOB-STAFF` (Mobile App Nhân viên)
- **Mục đích:** Ngăn chặn gian lận chấm công hộ. Nhân viên phải đứng trong bán kính GPS 50m của chi nhánh và quét mã QR biến đổi liên tục mỗi 30 giây trên màn hình POS quầy.

```
┌─────────────────────────────────────────────────────────┐
│ 📍 CHẤM CÔNG VÀO CA (STAFF CLOCK-IN)                     │
├─────────────────────────────────────────────────────────┤
│ VỊ TRÍ GPS HẠN ĐỊNH Chi Nhánh Q1:                        │
│ 🟢 Tọa độ hiện tại: 10.7769° N, 106.7009° E (Hợp lệ)   │
│ 🟢 Khoảng cách tới quán: 12 mét (Trong phạm vi 50m ✓)   │
├─────────────────────────────────────────────────────────┤
│ QUÉT MÃ QR ĐỘNG TẠI QUẦY THU NGÂN:                      │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ┌─────────────────────────────────────────────────┐ │ │
│ │ │ [ 📷 MỞ CAMERA QUÉT MÃ QR ĐỘNG TẠI QUẦY POS ]  │ │ │
│ │ └─────────────────────────────────────────────────┘ │ │
│ │ ⏱️ Mã QR quầy đổi mới sau: 14 giây                   │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ 🚀 THỰC HIỆN CHẤM CÔNG VÀO CA (CLOCK IN NOW) ]    │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

## 🏪 CHƯƠNG 5: NHÓM 4 — MANAGER MOBILE APP (5 MÀN HÌNH)

---

### 5.1 SCR-MGR-01: Shift Opening & Closing Management Screen

- **Mã màn hình:** `SCR-MGR-01`
- **Tên màn hình:** Quản Lý Mở Ca & Kết Ca Chi Nhánh (Shift Open / Close)
- **Thiết bị mục tiêu:** `HW-DESK-WEB` / Manager Mobile App
- **Mục đích:** Quản lý cửa hàng nhập số tiền két đầu ca (Float Money), phân công nhân viên vào ca và chốt doanh thu kiểm kê khi kết thúc ca làm việc.

```
┌─────────────────────────────────────────────────────────┐
│ 🏪 QUẢN LÝ CA LÀM VIỆC - CHI NHÁNH QUẬN 1               │
├─────────────────────────────────────────────────────────┤
│ CA HIỆN TẠI: CA SÁNG (06:00 - 14:00) | NV MỞ CA: VĂN A │
├─────────────────────────────────────────────────────────┤
│ 1. KHAI BÁO TIỀN KÉT ĐẦU CA (CASH FLOAT):               │
│ Tiền mặt ban đầu: [ 2.000.000 VNĐ                   ]   │
│ (Mệnh giá: 500k: 2 tờ | 200k: 3 tờ | 100k: 4 tờ...)      │
├─────────────────────────────────────────────────────────┤
│ 2. DANH SÁCH NHÂN VIÊN TRONG CA (4 NHÂN VIÊN):          │
│ • Nguyễn Văn A (Thu ngân POS)       [ 🟢 Đã chấm công]│
│ • Trần Thị B (Barista Pha chế)      [ 🟢 Đã chấm công]│
│ • Lê Văn C (Phục vụ bàn)            [ 🔴 Vắng mặt    ]│
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ 🚀 CHỐT CA & MỞ KÉT KIỂM KÊ (CLOSE SHIFT NOW) ]     │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

### 5.2 SCR-MGR-02: Cash Drawer Reconciliation & >50k Variance Alert

- **Mã màn hình:** `SCR-MGR-02`
- **Tên màn hình:** Bảng Đối SOÁT Két Tiền & Cảnh Báo Lệch Tiền >50k
- **Thiết bị mục tiêu:** `HW-DESK-WEB` / Manager Mobile App
- **Mục đích:** So sánh doanh thu tiền mặt trên hệ thống phần mềm với số tiền thực tế đếm được trong két. Nếu chênh lệch quá 50.000đ sẽ kích hoạt Form bắt buộc giải trình.

```
┌─────────────────────────────────────────────────────────┐
│ ⚠️ BẢNG ĐỐI SOÁT KÉT TIỀN KẾT CA               [ CA SÁNG]│
├─────────────────────────────────────────────────────────┤
│ BÁO CÁO DOANH THU HỆ THỐNG:                             │
│ • Doanh thu Tiền mặt hệ thống ghi nhận:  4.550.000 VNĐ  │
│ • Tiền két ban đầu (Float):             +2.000.000 VNĐ  │
│ ➔ TỔNG TIỀN MẶT LÝ THUYẾT PHẢI CÓ:       6.550.000 VNĐ  │
├─────────────────────────────────────────────────────────┤
│ THỰC TẾ ĐẾM TIỀN KÉT (PHYSICAL COUNT):                  │
│ Số tiền Quản lý đếm thực tế: [ 6.420.000 VNĐ        ]   │
├─────────────────────────────────────────────────────────┤
│ 🔴 KẾT QUẢ CHÊNH LỆCH: -130.000 VNĐ (THIẾU TIỀN!)       │
│                                                         │
│ ⚠️ CẢNH BÁO: CHÊNH LỆCH VƯỢT QUÁ HẠN MỨC 50.000 VNĐ!    │
│ VUI LÒNG NHẬP LÝ DO GIẢI TRÌNH (BẮT BỘC):              │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Thối lầm tiền cho khách đơn #ORD-8850 (Tờ 200k...   │ │
│ └─────────────────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ 🚨 XÁC NHẬN KẾT CA & GỬI BÁO CÁO CHO CHỦ CHUỖI ]  │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

### 5.3 SCR-MGR-03: Warehouse-to-Counter Stock Transfer Request

- **Mã màn hình:** `SCR-MGR-03`
- **Tên màn hình:** Phiếu Điều Chuyển Nguyên Liệu Từ Kho Tổng Về Quầy
- **Thiết bị mục tiêu:** Manager Mobile App / Web
- **Mục đích:** Quản lý lập phiếu xuất kho nguyên liệu (Hạt cà phê, Sữa tươi, Siro) chuyển từ Kho tổng chi nhánh ra Quầy Pha chế.

```
┌─────────────────────────────────────────────────────────┐
│ 📦 PHIẾU XUẤT KHO VỀ QUẦY PHA CHẾ #TRF-9910             │
├─────────────────────────────────────────────────────────┤
│ Kho xuất: KHO TỔNG Q1  ➔  Kho nhận: QUẦY BARISTA Q1     │
├─────────────────────────────────────────────────────────┤
│ DANH SÁCH NGUYÊN LIỆU ĐIỀU CHUYỂN:                      │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 1. Hạt Cà Phê Arabica Cầu Đất (Bao 1kg)             │ │
│ │    Số lượng: [ - ]  5  [ + ] Bao | HSD: 12/2026       │ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ 2. Sữa Tươi Thanh Trùng Dalatmilk (Hộp 1L)          │ │
│ │    Số lượng: [ - ]  12 [ + ] Hộp | Batch #BT-889     │ │
│ └─────────────────────────────────────────────────────┘ │
│ [ + THÊM NGUYÊN LIỆU VÀO PHIẾU ]                        │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ 🚀 DUYỆT XUẤT KHO & CẬP NHẬT TỒN THỰC TẾ ]        │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

### 5.4 SCR-MGR-04: Branch Revenue Analytics & AI Natural Language Query

- **Mã màn hình:** `SCR-MGR-04`
- **Tên màn hình:** Phân Tích Doanh Thu Chi Nhánh & Truy Vấn AI Bằng Giọng Nói / Văn Bản
- **Thiết bị mục tiêu:** Manager Mobile App / Web
- **Mục đích:** Hiển thị biểu đồ doanh thu theo giờ, món bán chạy và ô nhập câu hỏi tự nhiên cho AI (ví dụ: "So sánh doanh thu cà phê sáng nay với sáng qua").

```
┌─────────────────────────────────────────────────────────┐
│ 📊 BÁO CÁO DOANH THU Q1 & TRUY VẤN AI INTELLIGENCE     │
├─────────────────────────────────────────────────────────┤
│ 📈 DOANH THU HÔM NAY: 24.850.000 VNĐ (+18% vs Hôm qua)  │
│ [ Biểu đồ cột Doanh thu theo khung giờ 06h - 22h ]      │
├─────────────────────────────────────────────────────────┤
│ 🤖 HỎI AI TRUY VẤN DỮ LIỆU THÔNG MINH (AI QUERY):      │
│ ┌─────────────────────────────────────────┬───────────┐ │
│ │ "So sánh doanh thu trà đào ca sáng & tối"│ [ 🔍 HỎI ]│ │
│ └─────────────────────────────────────────┴───────────┘ │
│ 💡 AI Phân tích: "Trà Đào ca sáng bán 45 ly (2.2 triệu),│
│    ca tối bán 82 ly (4.0 triệu) -> Cao hơn 82%!"       │
└─────────────────────────────────────────────────────────┘
```

---

### 5.5 SCR-MGR-05: Emergency Incident & Low-Rating Feedback Action Center

- **Mã màn hình:** `SCR-MGR-05`
- **Tên màn hình:** Trung Tâm Xử Lý Cảnh Báo Khẩn Cấp & Đánh Giá Thấp (≤2 Star Alerts)
- **Thiết bị mục tiêu:** Manager Mobile App
- **Mục đích:** Khi khách hàng đánh giá ≤ 2 sao tại bàn (`SCR-PWA-08`), màn hình này lập tức báo động rung để Quản lý ra tận bàn xin lỗi và tặng Voucher đền bù.

```
┌─────────────────────────────────────────────────────────┐
│ 🚨 TRUNG TÂM XỬ LÝ SỰ CỐ KHÁCH HÀNG (ALERT CENTER)     │
├─────────────────────────────────────────────────────────┤
│ 🔴 CẢNH BÁO MỚI: ĐÁNH GIÁ 1 SAO TẠI BÀN T-06!          │
│ ⏱️ 45 giây trước | Khách: Anh Hoàng (0912***888)        │
│ 📝 Nội dung: "Bánh mì nguội ngắt, trà đào quá ngọt!"   │
├─────────────────────────────────────────────────────────┤
│ HÀNH ĐỘNG XỬ LÝ KHẨN CẤP DÀNH CHO QUẢN LÝ:              │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 1. [ 🚶 RA TẬN BÀN T-06 XIN LỖI TRỰC TIẾP ]         │ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ 2. [ 🎟️ TẶNG VOUCHER GIẢM 50% CHO LẦN SAU ]        │ │
│ ├─────────────────────────────────────────────────────┤ │
│ │ 3. [ 🔄 ĐỔI MỚI MÓN BÁNH MÌ NÓNG CHO KHÁCH ]        │ │
│ └─────────────────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ ✓ ĐÃ XỬ LÝ XONG — LƯU NHẬT KÝ SỰ CỐ (RESOLVED) ]   │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

## 👑 CHƯƠNG 6: NHÓM 5 — ADMIN WEB DASHBOARD (6 MÀN HÌNH)

---

### 6.1 SCR-ADM-01: Multi-Branch Executive Command Overview Dashboard

- **Mã màn hình:** `SCR-ADM-01`
- **Tên màn hình:** Bảng Điều Hành Tổng Quan Phân Hệ Chuỗi Chi Nhánh (Executive Dashboard)
- **Thiết bị mục tiêu:** `HW-DESK-WEB` (Desktop Web 1280px - 1920px+)
- **Mục đích:** Dành cho Chủ chuỗi / Tổng Giám đốc xem toàn bộ chỉ số KPI real-time của 12 chi nhánh trên 1 màn hình duy nhất.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 👑 SMART F&B OS — ADMIN SYSTEM MANAGEMENT                     [ Chi nhánh: Tất cả (12) ] [ User: Admin ]│
├──────────────┬──────────────────────────────────────────────────────────────────────────────────────────┤
│ 📊 Overview  │ 📈 TỔNG DOANH THU TOÀN CHUỖI: 485.200.000 VNĐ | ĐƠN HÀNG: 3,420 | KHÁCH HÀNG: 4,150           │
│ 🏪 Chi Nhánh ├──────────────────────────┬──────────────────────────┬──────────────────────────┬─────────────┤
│ 📋 Menu Master│ 🟢 CN Quận 1 (TPHCM)   │ 🟢 CN Cầu Giấy (Hà Nội)  │ 🟡 CN Sơn Trà (Đà Nẵng)  │ 🔴 CN Q.3   │
│ 🤖 AI Engine │ Doanh thu: 85.2tr VNĐ   │ Doanh thu: 72.4tr VNĐ   │ Doanh thu: 34.1tr VNĐ   │ Cảnh báo:   │
│ 💰 P&L Lãi Lỗ│ 450 Đơn | KDS: 🟢 Normal │ 380 Đơn | KDS: 🟢 Normal │ 190 Đơn | KDS: 🟡 Peak   │ Báo hết 5 món│
│ 👥 RBAC Quyền├──────────────────────────┴──────────────────────────┴──────────────────────────┴─────────────┤
│ ⚙️ Cấu Hình  │ 📊 BIỂU ĐỒ SO SÁNH DOANH THU 12 CHI NHÁNH THEO KHUNG GIỜ REAL-TIME                      │
│              │ [ Biểu đồ đường Multi-line Chart.js hiển thị doanh thu theo thực tế ]                    │
└──────────────┴──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 6.2 SCR-ADM-02: Automated Real-time P&L Statement & Expense Matrix

- **Mã màn hình:** `SCR-ADM-02`
- **Tên màn hình:** Báo Cáo Lãi / Lỗ Tự Động (Automated P&L Statement Generator)
- **Thiết bị mục tiêu:** `HW-DESK-WEB` (Desktop Web)
- **Mục đích:** Tự động tổng hợp Doanh thu, Chi phí Nguyên vật liệu (COGS), Chi phí Nhân công, Chi phí Mặt bằng và xuất ra Bảng P&L chuẩn kế toán.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 💰 BÁO CÁO LÃI / LỖ TỰ ĐỘNG (AUTOMATED P&L STATEMENT)          [ Từ: 01/08/2026 To: 13/08/2026 ] [ 📥 EXCEL]│
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ CHỈ SỐ TÀI CHÍNH KẾ TOÁN                │ SỐ TIỀN (VNĐ)        │ % DOANH THU  │ SO VỚI THÁNG TRƯỚC       │
├─────────────────────────────────────────┼──────────────────────┼──────────────┼──────────────────────────┤
│ I. TỔNG DOANH THU THUẦN (REVENUE)       │  1.250.000.000 VNĐ   │   100.0%     │ 📈 +12.4%                │
│ II. Giá vốn hàng bán (COGS - Nguyên liệu)│   -412.500.000 VNĐ   │    33.0%     │ 📉 -1.5% (Tốt)           │
│ ➔ LỢI NHUẬN GỘP (GROSS PROFIT)          │   +837.500.000 VNĐ   │    67.0%     │ 📈 +14.2%                │
│ III. Chi phí Nhân công (Labor Cost)     │   -210.000.000 VNĐ   │    16.8%     │ Ổn định                  │
│ IV. Chi phí Mặt bằng & Điện nước        │   -125.000.000 VNĐ   │    10.0%     │ Cố định                  │
│ ─────────────────────────────────────── │ ──────────────────── │ ──────────── │ ──────────────────────── │
│ ➔ LỢI NHUẬN RÒNG EBITDA (NET PROFIT)    │   +502.500.000 VNĐ   │    40.2%     │ 🚀 VƯỢT KẾ HOẠCH +8.2%   │
└─────────────────────────────────────────┴──────────────────────┴──────────────┴──────────────────────────┘
```

---

### 6.3 SCR-ADM-03: Centralized Menu Editor & Branch Multi-Price Matrix

- **Mã màn hình:** `SCR-ADM-03`
- **Tên màn hình:** Quản Lý Menu Trung Tâm & Ma Trận Giá Theo Chi Nhánh
- **Thiết bị mục tiêu:** `HW-DESK-WEB` (Desktop Web)
- **Mục đích:** Thiết lập danh mục món ăn dùng chung toàn chuỗi, nhưng cho phép điều chỉnh giá bán khác nhau giữa các chi nhánh (Ví dụ: Chi nhánh Sân bay giá cao hơn Chi nhánh Tỉnh 20%).

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 📋 MA TRẬN GIÁ MENU TOÀN CHUỖI (MULTI-BRANCH PRICE MATRIX BUILDER)             [ + THÊM MÓN MỚI ]       │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TÊN MÓN ĂN          │ DANH MỤC   │ GIÁ CHUẨN (BASE)│ GIÁ CN QUẬN 1  │ GIÁ CN CẦU GIẤY│ GIÁ CN SÂN BAY │
├─────────────────────┼────────────┼─────────────────┼────────────────┼────────────────┼────────────────┤
│ Phin Sữa Đá Premium │ Cà Phê     │ 35.000 VNĐ      │ 39.000 VNĐ     │ 39.000 VNĐ     │ 55.000 VNĐ     │
│ Trà Đào Cam Sả Rơm  │ Trà Trái Cây│ 45.000 VNĐ     │ 49.000 VNĐ     │ 49.000 VNĐ     │ 65.000 VNĐ     │
│ Phở Bò Tái Nạm      │ Món Ăn Sáng│ 65.000 VNĐ      │ 75.000 VNĐ     │ 75.000 VNĐ     │ 99.000 VNĐ     │
└─────────────────────┴────────────┴─────────────────┴────────────────┴────────────────┴────────────────┘
```

---

### 6.4 SCR-ADM-04: AI Combo Generator & Promotional Campaign Engine

- **Mã màn hình:** `SCR-ADM-04`
- **Tên màn hình:** Trợ Lý AI Gợi Ý Combo & Quản Lý Chiến Dịch Khuyến Mãi
- **Thiết bị mục tiêu:** `HW-DESK-WEB` (Desktop Web)
- **Mục đích:** Thuật toán AI phân tích lịch sử hóa đơn để phát hiện các món thường được mua cùng nhau, từ đó đề xuất tạo Combo có tỷ lệ chốt đơn cao nhất.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🤖 AI COMBO INTELLIGENCE & KHUYẾN MÃI (AI-2 MODULE ENGINE)                     [ 🔄 CHẠY THUẬT TOÁN ]   │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 💡 AI ĐỀ XUẤT COMBO MỚI DỰA TRÊN 50,000 ĐƠN HÀNG GẦN NHẤT:                                             │
│ ┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐ │
│ │ 🔥 COMBO "SÁNG TỈNH TÁO": Phin Sữa Đá + Bánh Mì Bò Nướng Phô Mai                                      │ │
│ │ • Tần suất khách mua cùng nhau: 68% đơn hàng buổi sáng (07h - 09h).                                  │ │
│ │ • Giá tách lẻ: 39k + 35k = 74.000đ  ➔  AI Đề xuất giá Combo: 59.000đ (Tiết kiệm 15k).                │ │
│ │ • Dự báo tăng trưởng doanh thu: +22% đơn hàng ca sáng.                                              │ │
│ │ [ 🚀 KÍCH HOẠT TẠO COMBO NÀY NGAY ]                           [ ❌ BỎ QUA ]                         │ │
│ └─────────────────────────────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 6.5 SCR-ADM-05: AI Customer Churn Risk Prediction & Retargeting Hub

- **Mã màn hình:** `SCR-ADM-05`
- **Tên màn hình:** Bảng Dự Báo Khách Hàng Có Nguy Cơ Rời Bỏ & Tiếp Thị AI (AI-3 Churn Prediction)
- **Thiết bị mục tiêu:** `HW-DESK-WEB` (Desktop Web)
- **Mục đích:** Mô hình Machine Learning phân tích tần suất quay lại của khách hàng RFM. Khi phát hiện khách VIP không quay lại quán > 30 ngày, hệ thống tự động gửi Zalo ZNS / SMS tự động tặng Voucher kéo khách trở lại.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🎯 BẢNG DỰ BÁO KHÁCH HÀNG RỜI BỎ (AI CHURN PREDICTION HUB)                     [ 📲 KÍCH HOẠT CAMPAIGN ]│
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ THỐNG KÊ RỦI RỎ: 142 Khách VIP nguy cơ rời bỏ (>30 ngày chưa quay lại)                                  │
├──────────────────────┬──────────────┬──────────────┬────────────────────────┬───────────────────────────┤
│ KHÁCH HÀNG           │ HẠNG THẺ     │ LẦN CUỐI ĂN  │ XÁC SUẤT CHURN (AI)    │ HÀNH ĐỘNG AI TỰ ĐỘNG     │
├──────────────────────┼──────────────┼──────────────┼────────────────────────┼───────────────────────────┤
│ Nguyễn Văn X (0903*) │ Platinum     │ 35 ngày trước│ 🔴 89% (Rủi ro rất cao)│ Send Zalo ZNS - Voucher 30%│
│ Lê Thị Y (0918*)     │ Gold         │ 28 ngày trước│ 🟡 65% (Rủi ro vừa)   │ Send SMS Reminder + 100pt │
└──────────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────────┘
```

---

### 6.6 SCR-ADM-06: RBAC Permission Matrix & Immutable Audit Trail Logs

- **Mã màn hình:** `SCR-ADM-06`
- **Tên màn hình:** Bảng Phân Quyền RBAC & Nhật Ký Bảo Mật Audit Logs
- **Thiết bị mục tiêu:** `HW-DESK-WEB` (Desktop Web)
- **Mục đích:** Quản lý phân quyền chi tiết tới từng Action Permission (View, Create, Edit, Delete, Void Order, Export P&L) cho 4 nhóm vai trò (Admin, Manager, Barista, Staff) và xem nhật ký thao tác chống gian lận.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🛡️ NGUYÊN TẮC BẢO MẬT & PHÂN QUYỀN RBAC (AUDIT LOGS)                          [ 🔒 KHÓA NHẬT KÝ AUDIT ] │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ BẢNG PHÂN QUYỀN VAI TRÒ (RBAC MATRIX):                                                                  │
│ VAI TRÒ (ROLE)       │ XEM DOANH THU│ HỦY ĐƠN HÀNG │ SỬA GIÁ MÓN  │ XUẤT KHO MAT │ XEM BÁO CÁO P&L │
├──────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┼─────────────────┤
│ 👑 Super Admin       │ [X] Yes      │ [X] Yes      │ [X] Yes      │ [X] Yes      │ [X] Yes         │
│ 🏪 Branch Manager    │ [X] Yes (CN) │ [X] Yes (CN) │ [ ] No       │ [X] Yes      │ [ ] No          │
│ 🧋 Barista / Kitchen │ [ ] No       │ [ ] No       │ [ ] No       │ [ ] No       │ [ ] No          │
│ 👨‍🍳 Waiter Staff      │ [ ] No       │ [ ] No       │ [ ] No       │ [ ] No       │ [ ] No          │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NHẬT KÝ BẢO MẬT THAO TÁC (IMMUTABLE AUDIT LOGS):                                                         │
│ THỜI GIAN       │ USER           │ HÀNH ĐỘNG THỰC HIỆN            │ ĐỊA CHỈ IP      │ KẾT QUẢ        │
├─────────────────┼────────────────┼────────────────────────────────┼─────────────────┼────────────────┤
│ 13/08 10:45:12  │ mgr_quan1      │ Hủy đơn hàng #ORD-8850 (150k)  │ 118.69.12.4     │ 🟢 Thành công  │
│ 13/08 09:12:00  │ admin_master   │ Thay đổi giá Phin Sữa Đá thành 39k│ 14.161.20.88   │ 🟢 Thành công  │
└─────────────────┴────────────────┴────────────────────────────────┴─────────────────┴────────────────┘
```

---

## 🧼 CHƯƠNG 7: BẢNG HƯỚNG DẪN COMPONENT LÍP-RÀN DÙNG CHUNG & QUY TRÌNH KIỂM THỬ UI

### 7.1 Thư Viện React Component Dùng Chung (`components/ui/`)

Tất cả 29 màn hình trên được lắp ghép từ thư viện 12 Shared Core Components chuẩn hóa đặt trong thư mục `src/components/ui/`:

1. `Button.tsx`: Variants `primary`, `secondary`, `ghost`, `danger`, `kds-action`.
2. `Input.tsx`: Custom Text, Tel, Number input với Icon prefix & Error badge.
3. `Modal.tsx`: Accessible Dialog hỗ trợ backdrop blur, esc key handling, và slide-up / scale-in animation.
4. `Drawer.tsx`: Bottom Sheet dành cho PWA Mobile và Right Side Sheet dành cho AI Chatbot.
5. `Badge.tsx`: Pill Badges cho trạng thái đơn (`Fresh`, `Pending`, `Overdue`, `Served`).
6. `Card.tsx`: Dish Card, KDS Ticket Card, Floor Map Table Box.
7. `TimerBanner.tsx`: KDS Real-time Countdown Timer Banner kèm màu sắc động.
8. `VietQRBox.tsx`: Component render hình ảnh mã QR động kèm countdown timer 30s.
9. `FloorGrid.tsx`: Visual Floor Map Grid render các ô bàn tương tác.
10. `StatCard.tsx`: Dashboard KPI metric card cho Admin & Manager.
11. `Table.tsx`: Data Table hỗ trợ phân trang, sắp xếp và tìm kiếm.
12. `ToastNotification.tsx`: Toast popup cảnh báo sự cố SignalR và cuộc gọi phục vụ.

---

### 7.2 Quy Trình Kiểm Thử & Nghiệm Thu UI/UX (UI QA Checklist)

Trước khi chuyển giao mã nguồn Frontend cho đội ngũ QA, toàn bộ giao diện phải đạt 100% các tiêu chí nghiệm thu sau:

- [x] **Zero Placeholder Mandate:** Tất cả màn hình được định nghĩa đầy đủ 100%, không sử dụng `...` hay skeleton sơ sài.
- [x] **Responsive & Layout Integrity:** Không bị đè chữ, vỡ khung layout trên các breakpoint từ `375px` (Mobile PWA) tới `1920px` (Admin Desktop).
- [x] **Contrast Ratio Compliance:** Chữ và nền đạt chuẩn **WCAG 2.1 AA** (Tỷ lệ tương phản ≥ 4.5:1 đối với văn bản thường, ≥ 3.0:1 cho KDS Dark Mode).
- [x] **Touch Target Size:** Tất cả các phần tử tương tác bấm/chạm trên Mobile và KDS Tablet có kích thước vùng chạm tối thiểu từ `44x44px` trở lên.
- [x] **SignalR Integration Verification:** Kiểm tra thành công các hiệu ứng Pulse, Badge Update và Audio Beep khi có Event SignalR đẩy về Client.

---

> **BẢO TRÌ & CẬP NHẬT:**  
> Tài liệu thiết kế UI/UX Design System này là tài sản kỹ thuật chính thức của dự án **Smart F&B OS**. Mọi sự thay đổi về token màu sắc, phông chữ hoặc wireframe màn hình bắt buộc phải được cập nhật trực tiếp vào file này và thông qua sự phê duyệt của Trưởng nhóm Kiến trúc UI/UX.
