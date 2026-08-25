import Link from "next/link";
import { Coffee, Home, ShoppingBag, Clock } from "lucide-react";

export default function CustomerLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col justify-between">
      <div className="flex-1">{children}</div>

      {/* Bottom Navigation for Customer PWA */}
      <nav className="fixed bottom-0 left-0 right-0 z-30 bg-white/95 backdrop-blur border-t border-slate-200 py-2 px-6 flex justify-around items-center shadow-lg md:hidden">
        <Link href="/menu" className="flex flex-col items-center gap-1 text-slate-600 hover:text-orange-600">
          <Coffee className="w-5 h-5" />
          <span className="text-[10px] font-semibold">Thực Đơn</span>
        </Link>
        <Link href="/cart" className="flex flex-col items-center gap-1 text-slate-600 hover:text-orange-600">
          <ShoppingBag className="w-5 h-5" />
          <span className="text-[10px] font-semibold">Giỏ Hàng</span>
        </Link>
        <Link href="/history" className="flex flex-col items-center gap-1 text-slate-600 hover:text-orange-600">
          <Clock className="w-5 h-5" />
          <span className="text-[10px] font-semibold">Lịch Sử</span>
        </Link>
        <Link href="/" className="flex flex-col items-center gap-1 text-slate-600 hover:text-orange-600">
          <Home className="w-5 h-5" />
          <span className="text-[10px] font-semibold">Cổng Portal</span>
        </Link>
      </nav>
    </div>
  );
}
