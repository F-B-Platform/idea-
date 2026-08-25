import Link from "next/link";
import { Utensils, Monitor, Store, ShieldCheck, UserCheck, Coffee, QrCode } from "lucide-react";

export default function HomePage() {
  const routes = [
    {
      title: "PWA Gọi Món Tại Bàn (Dine-in)",
      desc: "Khách hàng quét QR bàn, chọn món, thanh toán VietQR trả trước hoặc Tiền mặt trả sau kèm Bill QR.",
      href: "/menu",
      icon: Coffee,
      badge: "(customer)",
      color: "bg-amber-500",
    },
    {
      title: "PWA Đặt Món Giao Tận Nhà (Delivery)",
      desc: "Khách quét QR Delivery riêng, nhập SĐT & địa chỉ, phí ship 20k cố định, 100% VietQR trước.",
      href: "/delivery",
      icon: QrCode,
      badge: "(customer)",
      color: "bg-emerald-500",
    },
    {
      title: "Màn Hình Điều Phối Bếp (Web KDS)",
      desc: "Màn hình TV/Tablet quầy bar, barista nhận đơn realtime qua SignalR, xem BOM và 86-Toggle.",
      href: "/kitchen",
      icon: Monitor,
      badge: "(kds)",
      color: "bg-blue-600",
    },
    {
      title: "Web POS Quầy & CRM 10 Ly (Takeaway)",
      desc: "Thu ngân tạo đơn mang về, tra cứu SĐT CRM, áp dụng tích 10 ly tặng 1, thu tiền sau.",
      href: "/pos",
      icon: Store,
      badge: "(staff)",
      color: "bg-orange-500",
    },
    {
      title: "Chấm Công Khóa Mạng WiFi",
      desc: "Nhân viên vào/ra ca trên Web Staff, tự động kiểm tra BSSID WiFi router quán và Mã NV.",
      href: "/attendance",
      icon: UserCheck,
      badge: "(staff)",
      color: "bg-indigo-500",
    },
    {
      title: "Portal Quản Lý Chi Nhánh",
      desc: "Quản lý mở/kết ca két tiền, đối soát Z-Report, kiểm kê kho BOM và cấu hình BSSID WiFi.",
      href: "/branch-dashboard",
      icon: Utensils,
      badge: "(manager)",
      color: "bg-purple-600",
    },
    {
      title: "Portal Chủ Chuỗi & Admin Toàn Quyền",
      desc: "CRUD thực đơn, BOM theo size, Seasonal Menu, giá vùng, duyệt Combo AI-2 và P&L.",
      href: "/admin-dashboard",
      icon: ShieldCheck,
      badge: "(admin)",
      color: "bg-rose-600",
    },
  ];

  return (
    <main className="min-h-screen bg-slate-900 text-slate-100 p-6 md:p-12">
      <div className="max-w-5xl mx-auto space-y-8">
        <div className="text-center space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-500/20 text-orange-400 text-sm font-semibold border border-orange-500/30">
            <span>☕ Smart F&B OS v2.5.0</span>
          </div>
          <h1 className="text-3xl md:text-5xl font-bold tracking-tight text-white">
            Khung Hạ Tầng Dự Án (Developer Portal)
          </h1>
          <p className="text-slate-400 max-w-2xl mx-auto text-sm md:text-base">
            Bộ khung mã nguồn đã được cấu hình sẵn sàng cho 4 thành viên (2 Backend + 2 Frontend). Chọn phân hệ để kiểm tra giao diện khởi tạo:
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4">
          {routes.map((route, idx) => {
            const Icon = route.icon;
            return (
              <Link
                key={idx}
                href={route.href}
                className="group relative flex flex-col p-6 rounded-2xl bg-slate-800/80 border border-slate-700/60 hover:border-orange-500/50 hover:bg-slate-800 transition-all duration-200 shadow-lg hover:shadow-orange-500/10"
              >
                <div className="flex items-start justify-between mb-4">
                  <div className={`p-3 rounded-xl ${route.color} text-white shadow-md`}>
                    <Icon className="w-6 h-6" />
                  </div>
                  <span className="text-xs font-mono font-medium px-2.5 py-1 rounded-md bg-slate-700/80 text-slate-300 border border-slate-600">
                    {route.badge}
                  </span>
                </div>
                <h2 className="text-lg font-semibold text-white group-hover:text-orange-400 transition-colors">
                  {route.title}
                </h2>
                <p className="text-sm text-slate-400 mt-1 flex-1">
                  {route.desc}
                </p>
                <div className="mt-4 flex items-center text-xs font-semibold text-orange-400 group-hover:translate-x-1 transition-transform">
                  Mở giao diện phân hệ &rarr;
                </div>
              </Link>
            );
          })}
        </div>

        <div className="p-4 rounded-xl bg-slate-800/40 border border-slate-700 text-center text-xs text-slate-400">
          Backend API: <span className="text-emerald-400 font-mono">http://localhost:5000</span> | Swagger: <span className="text-emerald-400 font-mono">http://localhost:5000/swagger</span> | Database: <span className="text-emerald-400 font-mono">PostgreSQL 16 (Port 5432)</span> | Cache: <span className="text-emerald-400 font-mono">Redis 7 (Port 6379)</span>
        </div>
      </div>
    </main>
  );
}
