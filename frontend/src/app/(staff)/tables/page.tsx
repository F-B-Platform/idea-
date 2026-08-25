"use client";

import { LayoutGrid, CheckCircle2, User, Clock } from "lucide-react";

export default function StaffTablesPage() {
  const tables = [
    { number: "01", status: "Trống", color: "bg-emerald-50 border-emerald-200 text-emerald-800" },
    { number: "02", status: "Có Khách", color: "bg-amber-50 border-amber-200 text-amber-800" },
    { number: "03", status: "Có Khách", color: "bg-amber-50 border-amber-200 text-amber-800" },
    { number: "04", status: "Trống", color: "bg-emerald-50 border-emerald-200 text-emerald-800" },
    { number: "05", status: "Chờ Dọn", color: "bg-slate-100 border-slate-300 text-slate-700" },
    { number: "06", status: "Trống", color: "bg-emerald-50 border-emerald-200 text-emerald-800" },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <LayoutGrid className="w-5 h-5 text-orange-600" /> Sơ Đồ Bàn Thời Gian Thực
          </h1>
          <p className="text-xs text-slate-500">Chi nhánh 01 (Quận 1) • Cập nhật qua SignalR</p>
        </div>
      </header>

      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        {tables.map((t, idx) => (
          <div
            key={idx}
            className={`p-4 rounded-2xl border ${t.color} text-center space-y-2 shadow-sm`}
          >
            <div className="text-2xl font-extrabold font-mono">Bàn {t.number}</div>
            <div className="text-xs font-semibold">{t.status}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
