"use client";

import { DollarSign, FileCheck } from "lucide-react";

export default function ManagerShiftsPage() {
  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-purple-600" /> Quản Lý Ca Két & Đối Soát Z-Report
        </h1>
        <p className="text-xs text-slate-500">Mở ca kiểm tiền đầu ca, kết ca kiểm đếm và in biên bản Z-Report.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
          <h2 className="text-sm font-bold text-slate-900">Ca Hiện Tại: Ca Sáng (06:30 - 14:30)</h2>
          <div className="text-xs space-y-1 text-slate-600">
            <p>Thu ngân trực ca: <strong>Lê Văn B (NV-002)</strong></p>
            <p>Tiền mặt đầu ca: <strong>2.000.000đ</strong></p>
            <p>Doanh thu tiền mặt ghi nhận: <strong>3.450.000đ</strong></p>
            <p>Doanh thu VietQR: <strong>8.230.000đ</strong></p>
          </div>
          <button className="w-full py-2.5 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs flex items-center justify-center gap-2 shadow">
            <FileCheck className="w-4 h-4" /> Kết Ca & Tạo Biên Bản Z-Report
          </button>
        </div>
      </div>
    </div>
  );
}
