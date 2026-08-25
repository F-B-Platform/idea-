"use client";

import Link from "next/link";
import { ArrowLeft, Sparkles, TrendingUp, Layers, Sliders } from "lucide-react";

export default function AdminDashboardPage() {
  return (
    <div className="min-h-screen bg-slate-100 text-slate-800">
      <header className="bg-slate-900 text-white px-6 py-4 flex items-center justify-between shadow-sm">
        <div className="flex items-center gap-3">
          <Link href="/" className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-lg font-bold text-white">Portal Chủ Chuỗi & Admin Toàn Quyền</h1>
            <p className="text-xs text-slate-400">Điều hành toàn chuỗi 3 chi nhánh • Full CRUD Menu, BOM & AI-2</p>
          </div>
        </div>
      </header>

      <main className="p-6 max-w-6xl mx-auto space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <TrendingUp className="w-4 h-4 text-emerald-600" /> Doanh Thu Hợp Nhất (P&L)
            </div>
            <div className="text-xl font-bold text-slate-900">45.280.000đ</div>
          </div>
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <Layers className="w-4 h-4 text-blue-600" /> Quản Lý Menu & BOM
            </div>
            <div className="text-xl font-bold text-slate-900">24 Món (3 Size)</div>
          </div>
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <Sliders className="w-4 h-4 text-orange-600" /> Bảng Giá Theo Vùng
            </div>
            <div className="text-xl font-bold text-slate-900">3 Chi Nhánh</div>
          </div>
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <Sparkles className="w-4 h-4 text-purple-600" /> Đề Xuất Combo AI-2
            </div>
            <div className="text-xl font-bold text-purple-600">3 Cần Phê Duyệt</div>
          </div>
        </div>
      </main>
    </div>
  );
}
