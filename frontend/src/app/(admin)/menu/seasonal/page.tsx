"use client";

import { Calendar, Plus } from "lucide-react";

export default function AdminSeasonalPage() {
  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Calendar className="w-5 h-5 text-rose-600" /> Lên Lịch Thực Đơn Theo Mùa (Seasonal Menu)
          </h1>
          <p className="text-xs text-slate-500">Tự động bật/tắt món đồ uống đặc biệt theo khung ngày giờ đã cấu hình.</p>
        </div>
        <button className="px-3 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs flex items-center gap-1.5 shadow">
          <Plus className="w-4 h-4" /> Tạo Lịch Mùa Mới
        </button>
      </header>

      <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
        <h2 className="text-sm font-bold text-slate-900">Chiến Dịch Mùa Thu 2026: 'Hương Cốm Mùa Vàng'</h2>
        <div className="text-xs text-slate-600 space-y-1">
          <p>Thời gian áp dụng: <strong>01/09/2026 - 31/10/2026</strong></p>
          <p>Món áp dụng: <strong>Cà Phê Cốm Sữa Dừa, Trà Sen Vàng Kem Cốm</strong></p>
          <p>Chi nhánh: <strong>Áp dụng toàn bộ 3 chi nhánh</strong></p>
        </div>
      </div>
    </div>
  );
}
