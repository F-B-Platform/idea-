"use client";

import Link from "next/link";
import { Coffee, ShoppingBag, ArrowLeft } from "lucide-react";

export default function CustomerMenuPage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 pb-20">
      {/* Top Header */}
      <header className="sticky top-0 z-20 bg-white/90 backdrop-blur border-b border-slate-200 px-4 py-3 flex items-center justify-between shadow-sm">
        <div className="flex items-center gap-2">
          <Link href="/" className="p-2 rounded-full hover:bg-slate-100 text-slate-600">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-base font-bold text-slate-900">Smart Coffee - Bàn 05</h1>
            <p className="text-xs text-slate-500">Chi nhánh Quận 1 • Dine-in QR</p>
          </div>
        </div>
        <div className="relative p-2 rounded-full bg-orange-50 text-orange-600">
          <ShoppingBag className="w-5 h-5" />
          <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-orange-500 text-white text-[10px] font-bold flex items-center justify-center">
            0
          </span>
        </div>
      </header>

      {/* Main Container */}
      <main className="max-w-md mx-auto p-4 space-y-4">
        <div className="p-4 rounded-2xl bg-gradient-to-br from-orange-500 to-amber-600 text-white shadow-lg space-y-1">
          <span className="text-xs uppercase tracking-wider font-semibold opacity-90">Gọi Món Tại Bàn</span>
          <h2 className="text-xl font-bold">Thực Đơn Đồ Uống</h2>
          <p className="text-xs text-orange-100">
            Hỗ trợ VietQR trả trước (Bếp nhận khi thanh toán) và Tiền mặt trả sau (In bill kèm VietQR).
          </p>
        </div>

        {/* Skeleton Category List */}
        <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-none">
          {["Cà Phê", "Trà Trái Cây", "Trà Sữa", "Đá Xay", "Bánh Ngọt"].map((cat, idx) => (
            <button
              key={idx}
              className={`px-3 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap transition-colors ${
                idx === 0 ? "bg-orange-600 text-white shadow-sm" : "bg-white text-slate-600 border border-slate-200"
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Placeholder Items for Frontend Developers to connect API */}
        <div className="space-y-3">
          {[
            { name: "Cà Phê Muối Hoàng Gia", price: "35.000đ", desc: "Cà phê Robusta pha phin kết hợp lớp kem muối béo ngậy." },
            { name: "Trà Đào Cam Sả Tươi", price: "42.000đ", desc: "Trà đen ủ lạnh với đào miếng giòn ngọt và sả thơm ngát." },
            { name: "Trà Sữa Oolong Nướng", price: "39.000đ", desc: "Trà Oolong nướng đậm vị, sữa tươi thanh trùng ngọt dịu." },
          ].map((item, idx) => (
            <div key={idx} className="p-3 bg-white rounded-xl border border-slate-200 shadow-sm flex items-center justify-between gap-3">
              <div className="space-y-1 flex-1">
                <h3 className="text-sm font-bold text-slate-900">{item.name}</h3>
                <p className="text-xs text-slate-500 line-clamp-1">{item.desc}</p>
                <div className="text-sm font-extrabold text-orange-600">{item.price}</div>
              </div>
              <button className="px-3 py-1.5 rounded-lg bg-orange-500 hover:bg-orange-600 text-white text-xs font-semibold shadow-sm">
                + Thêm
              </button>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
