"use client";

import Link from "next/link";
import { Sparkles, TrendingUp, Layers, Sliders, ArrowLeft } from "lucide-react";

export default function AdminDashboardPage() {
  return (
    <div className="p-6 max-w-6xl mx-auto space-y-6">
      <header className="flex justify-between items-center pb-4 border-b border-slate-200">
        <div>
          <h1 className="text-xl font-bold text-slate-900">Báo Cáo Tổng Hợp Doanh Thu P&L (Chuỗi 3 Quán)</h1>
          <p className="text-xs text-slate-500">Trụ sở điều hành HQ • Phân hệ Quản trị Viên</p>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
          <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
            <TrendingUp className="w-4 h-4 text-emerald-600" /> Doanh Thu Toàn Chuỗi
          </div>
          <div className="text-xl font-bold text-slate-900">45.280.000đ</div>
        </div>
        <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
          <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
            <Layers className="w-4 h-4 text-blue-600" /> Món Đang Kinh Doanh
          </div>
          <div className="text-xl font-bold text-slate-900">24 Món (3 Size)</div>
        </div>
        <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
          <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
            <Sliders className="w-4 h-4 text-orange-600" /> Bảng Giá Vùng
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
    </div>
  );
}
