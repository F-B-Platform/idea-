"use client";

import Link from "next/link";
import { ArrowLeft, Search, Plus, Award, CreditCard, Banknote } from "lucide-react";

export default function StaffPosPage() {
  return (
    <div className="min-h-screen bg-slate-100 text-slate-800 flex flex-col">
      {/* POS Topbar */}
      <header className="bg-white border-b border-slate-200 px-6 py-3 flex items-center justify-between shadow-sm">
        <div className="flex items-center gap-3">
          <Link href="/" className="p-2 rounded-lg hover:bg-slate-100 text-slate-600">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-base font-bold text-slate-900">Web POS Quầy — Bán Hàng Mang Về (Takeaway)</h1>
            <p className="text-xs text-slate-500">Chi nhánh Quận 1 • Thu ngân: Lê Văn B (NV-002)</p>
          </div>
        </div>

        {/* CRM Lookup Bar */}
        <div className="flex items-center gap-2">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="tel"
              placeholder="Nhập SĐT khách hàng CRM..."
              className="pl-9 pr-3 py-1.5 text-xs rounded-lg border border-slate-300 w-64 focus:outline-none focus:ring-2 focus:ring-orange-500"
            />
          </div>
          <button className="px-3 py-1.5 rounded-lg bg-orange-500 text-white text-xs font-semibold hover:bg-orange-600">
            Tra cứu
          </button>
        </div>
      </header>

      {/* POS Body Grid */}
      <div className="flex-1 grid grid-cols-1 md:grid-cols-3 gap-4 p-4">
        {/* Menu Grid (2 cols) */}
        <div className="md:col-span-2 bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-4">
          <h2 className="text-sm font-bold text-slate-900">Danh Mục Món Quầy</h2>
          <div className="grid grid-cols-3 gap-3">
            {[
              { name: "Cà Phê Sữa Đá", price: "29.000đ" },
              { name: "Bạc Xỉu Sữa Tươi", price: "32.000đ" },
              { name: "Trà Vải Hoa Hồng", price: "45.000đ" },
            ].map((m, idx) => (
              <button
                key={idx}
                className="p-3 text-left rounded-xl border border-slate-200 hover:border-orange-500 hover:bg-orange-50/30 transition-all shadow-sm space-y-1"
              >
                <div className="text-xs font-bold text-slate-900">{m.name}</div>
                <div className="text-xs font-extrabold text-orange-600">{m.price}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Current Order & Loyalty Panel (1 col) */}
        <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm flex flex-col justify-between space-y-4">
          <div className="space-y-3">
            <h2 className="text-sm font-bold text-slate-900 pb-2 border-b border-slate-200">
              Đơn Hiện Tại (Takeaway)
            </h2>

            {/* Loyalty Status Badge */}
            <div className="p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-xs space-y-1">
              <div className="font-bold flex items-center gap-1.5 text-amber-800">
                <Award className="w-4 h-4 text-amber-600" />
                Loyalty CRM (Chỉ Áp Dụng Takeaway)
              </div>
              <p className="text-[11px] text-amber-700">
                Đã tích lũy: <strong className="font-bold text-amber-900">9 / 10 ly</strong> (Mua thêm 1 ly để được tặng 1 ly miễn phí!).
              </p>
            </div>
          </div>

          {/* Payment Actions */}
          <div className="pt-4 border-t border-slate-200 space-y-2">
            <div className="flex justify-between items-center text-sm font-bold">
              <span>Tổng Tiền:</span>
              <span className="text-lg text-orange-600">0đ</span>
            </div>

            <div className="grid grid-cols-2 gap-2">
              <button className="py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs flex items-center justify-center gap-1">
                <Banknote className="w-4 h-4" /> Tiền Mặt
              </button>
              <button className="py-2.5 rounded-xl bg-orange-500 hover:bg-orange-600 text-white font-bold text-xs flex items-center justify-center gap-1">
                <CreditCard className="w-4 h-4" /> VietQR Quầy
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
