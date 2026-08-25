"use client";

import Link from "next/link";
import { ArrowLeft, DollarSign, Package, Wifi, FileText } from "lucide-react";

export default function ManagerDashboardPage() {
  return (
    <div className="min-h-screen bg-slate-100 text-slate-800">
      <header className="bg-white border-b border-slate-200 px-6 py-4 flex items-center justify-between shadow-sm">
        <div className="flex items-center gap-3">
          <Link href="/" className="p-2 rounded-lg hover:bg-slate-100 text-slate-600">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-lg font-bold text-slate-900">Portal Quản Lý Chi Nhánh</h1>
            <p className="text-xs text-slate-500">Chi nhánh 01 (Quận 1) • Quản lý: Trần Văn C</p>
          </div>
        </div>
      </header>

      <main className="p-6 max-w-6xl mx-auto space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <DollarSign className="w-4 h-4 text-emerald-600" /> Két Tiền Đầu Ca
            </div>
            <div className="text-xl font-bold text-slate-900">2.000.000đ</div>
          </div>
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <Package className="w-4 h-4 text-orange-600" /> Cảnh Báo Tồn Kho BOM
            </div>
            <div className="text-xl font-bold text-orange-600">2 Nguyên Liệu</div>
          </div>
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <Wifi className="w-4 h-4 text-indigo-600" /> Access Point WiFi
            </div>
            <div className="text-xl font-bold text-slate-900">2 BSSID Active</div>
          </div>
          <div className="p-4 rounded-xl bg-white border border-slate-200 shadow-sm space-y-1">
            <div className="text-xs font-semibold text-slate-500 flex items-center gap-1.5">
              <FileText className="w-4 h-4 text-purple-600" /> Báo Cáo Z-Report
            </div>
            <div className="text-xl font-bold text-purple-600">Sẵn Sàng Kết Ca</div>
          </div>
        </div>
      </main>
    </div>
  );
}
