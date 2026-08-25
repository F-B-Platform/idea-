import React from "react";
import Link from "next/link";
import {
  Coffee,
  Tv,
  Store,
  ShieldAlert,
  Crown,
  QrCode,
  Truck,
  Sparkles,
  Layers,
  ArrowRight,
  Wifi,
  Receipt,
  FileCheck,
} from "lucide-react";

export default function RootHomePage() {
  const workspaces = [
    {
      title: "1. Khách Hàng (Customer PWA)",
      role: "Khách Dùng Bàn & Đặt Giao Tận Nơi",
      color: "border-amber-600 bg-amber-50/50 text-amber-900",
      icon: Coffee,
      links: [
        { label: "Gọi Món Tại Bàn (Table #05)", href: "/table/05" },
        { label: "Thực Đơn Số Chung", href: "/menu" },
        { label: "Giỏ Hàng & Chọn 2 Nhánh Dine-In", href: "/cart" },
        { label: "Đặt Giao Hàng QR Delivery (Ship 20k, 100% VietQR)", href: "/delivery" },
        { label: "Thanh Toán VietQR Động (10p Timer)", href: "/checkout/vietqr" },
        { label: "Theo Dõi Đơn Hàng & Chuông Gọi Bàn Live", href: "/tracking/ORD-0042" },
        { label: "Đánh Giá 1-5 Sao & Tải Ảnh (Red Alert <= 2 Sao)", href: "/review/ORD-0042" },
        { label: "Lịch Sử Đơn Hàng & Đặt Lại 1 Chạm", href: "/history" },
        { label: "Chatbot AI-1 Gemini Tư Vấn Khẩu Vị", href: "/ai-chat" },
      ],
    },
    {
      title: "2. Màn Hình Bếp / Bar (KDS High-Contrast TV)",
      role: "Barista & Đầu Bếp",
      color: "border-slate-700 bg-slate-900 text-slate-100",
      icon: Tv,
      links: [
        { label: "Ticket Board Pha Chế Real-Time (SLA Timers & Audio)", href: "/kitchen" },
        { label: "Modal Khóa Món Khẩn Cấp (86-Toggle)", href: "/86-toggle" },
        { label: "Chế Độ Gom Món Pha Chế Đồng Loạt (KDS Batching)", href: "/batch" },
      ],
    },
    {
      title: "3. Nhân Viên Vận Hành (Staff Operations & POS)",
      role: "Thu Ngân & Phục Vụ Bàn",
      color: "border-sky-600 bg-sky-50/50 text-sky-950",
      icon: Store,
      links: [
        { label: "Web POS Takeaway & Tra Cứu CRM 10 Ly Đổi 1", href: "/pos" },
        { label: "Sơ Đồ Bàn Mặt Bằng & Tiếp Nhận Chuông Gọi Bàn (587Hz)", href: "/tables" },
        { label: "Chấm Công Khóa Mạng WiFi (BSSID + Subnet IP)", href: "/attendance" },
        { label: "Báo Cáo Bàn Giao Ca Nhân Viên", href: "/shift-report" },
      ],
    },
    {
      title: "4. Quản Lý Chi Nhánh (Manager Portal)",
      role: "Quản Lý Vận Hành Cửa Hàng",
      color: "border-emerald-600 bg-emerald-50/50 text-emerald-950",
      icon: ShieldAlert,
      links: [
        { label: "Dashboard Vận Hành Chi Nhánh", href: "/dashboard" },
        { label: "Mở/Kết Ca Két Tiền & Đối Soát Z-Report (6 Mệnh Giá)", href: "/shifts" },
        { label: "Quản Lý Kho BOM & Kiểm Kê Hao Hụt (>3% Warning)", href: "/inventory" },
        { label: "Cấu Hình BSSID & Dải IP Router WiFi Chi Nhánh", href: "/wifi-configs" },
        { label: "Hộp Thư Cảnh Báo Đánh Giá <= 2 Sao & Duyệt Ảnh", href: "/reviews" },
      ],
    },
    {
      title: "5. Chủ Chuỗi Trung Tâm (Chain Admin Portal)",
      role: "Giám Đốc Chuỗi & Điều Hành Hệ Thống",
      color: "border-purple-600 bg-purple-50/50 text-purple-950",
      icon: Crown,
      links: [
        { label: "Dashboard P&L Hợp Nhất Đa Chi Nhánh (BOM COGS)", href: "/admin-dashboard" },
        { label: "Full CRUD Món Ăn & Công Thức BOM Từng Size", href: "/menu/products" },
        { label: "Sắp Xếp Danh Mục Món Kéo Thả", href: "/menu/categories" },
        { label: "Lên Lịch Thực Đơn Mùa Vụ (Seasonal Menu)", href: "/menu/seasonal" },
        { label: "Quản Lý Bảng Giá Vùng Chi Nhánh", href: "/pricing" },
        { label: "AI-2 Khai Phá & Phê Duyệt Combo Apriori", href: "/ai/combos" },
        { label: "CRM Danh Bạ & Phân Khúc Hội Viên RFM", href: "/crm" },
        { label: "Nhật Ký Kiểm Toán Bất Biến (Audit Logs)", href: "/audit-logs" },
      ],
    },
  ];

  return (
    <main className="min-h-screen bg-slate-100 text-slate-900 p-6 md:p-12">
      <div className="max-w-6xl mx-auto space-y-10">
        {/* Hero Section */}
        <div className="text-center space-y-3">
          <div className="inline-flex items-center gap-2 bg-amber-700 text-white px-4 py-1.5 rounded-full text-xs font-bold shadow-sm">
            <Coffee className="h-4 w-4" />
            <span>SMART F&B OPERATING SYSTEM (v2.5.0)</span>
          </div>
          <h1 className="text-3xl md:text-5xl font-black tracking-tight text-slate-950">
            Cổng Điều Hướng 5 Phân Hệ Trực Tuyến
          </h1>
          <p className="text-slate-600 text-sm md:text-base max-w-2xl mx-auto">
            Hệ thống quản trị và vận hành chuỗi F&B thông minh đồng bộ thời gian thực: Next.js 14 App Router,
            Zustand Store, SignalR WebSockets, Web Audio Synthesizer, 100% Zero-Placeholder.
          </p>
        </div>

        {/* 5 Workspaces Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {workspaces.map((ws, idx) => {
            const Icon = ws.icon;
            return (
              <div
                key={idx}
                className={`rounded-3xl p-6 border-2 shadow-sm flex flex-col justify-between space-y-5 transition-all hover:shadow-lg ${ws.color}`}
              >
                <div className="space-y-4">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 rounded-2xl bg-white/80 backdrop-blur border border-current/20 flex items-center justify-center shadow-sm">
                      <Icon className="h-6 w-6" />
                    </div>
                    <div>
                      <h3 className="font-extrabold text-base leading-snug">{ws.title}</h3>
                      <span className="text-xs opacity-75 font-medium">{ws.role}</span>
                    </div>
                  </div>

                  <div className="space-y-1.5 pt-2">
                    {ws.links.map((link, lIdx) => (
                      <Link
                        key={lIdx}
                        href={link.href}
                        className="flex items-center justify-between p-2.5 rounded-xl bg-white/70 hover:bg-white text-xs font-semibold shadow-2xs hover:shadow-xs transition-all text-slate-800"
                      >
                        <span className="line-clamp-1">{link.label}</span>
                        <ArrowRight className="h-3.5 w-3.5 opacity-40 shrink-0 ml-1" />
                      </Link>
                    ))}
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Footer info banner */}
        <div className="text-center text-xs text-slate-500 pt-6 border-t border-slate-200">
          <p className="font-semibold">Smart F&B OS • .NET 8 Clean Architecture Backend + Next.js 14 Frontend</p>
          <p className="mt-1 text-slate-400">Thiết kế chuẩn UI/UX WCAG 2.1 AA • Zero Placeholder • Sẵn sàng Production</p>
        </div>
      </div>
    </main>
  );
}
