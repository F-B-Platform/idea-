"use client";

import Link from "next/link";
import { ArrowLeft, AlertTriangle, CheckCircle2 } from "lucide-react";
import { useState } from "react";

export default function Emergency86TogglePage() {
  const [items, setItems] = useState([
    { id: "1", name: "Cà Phê Muối", available: true },
    { id: "2", name: "Trà Đào Cam Sả", available: true },
    { id: "3", name: "Sữa Tươi Trân Châu", available: false },
  ]);

  const toggle = (id: string) => {
    setItems((prev) =>
      prev.map((i) => (i.id === id ? { ...i, available: !i.available } : i))
    );
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 max-w-2xl mx-auto space-y-6">
      <header className="flex items-center gap-3 pb-4 border-b border-slate-800">
        <Link href="/kitchen" className="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="text-lg font-bold text-white flex items-center gap-2">
            <AlertTriangle className="w-5 h-5 text-amber-400" />
            Công Tắc Khẩn Cấp 86-Toggle (Báo Hết Món)
          </h1>
          <p className="text-xs text-slate-400">Khi bật 'Hết món', thực đơn khách hàng sẽ tự động khóa món tức thì.</p>
        </div>
      </header>

      <div className="space-y-3">
        {items.map((item) => (
          <div
            key={item.id}
            className="p-4 bg-slate-900 border border-slate-800 rounded-xl flex items-center justify-between"
          >
            <span className="text-sm font-semibold">{item.name}</span>
            <button
              onClick={() => toggle(item.id)}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-colors ${
                item.available
                  ? "bg-emerald-600/20 text-emerald-400 border border-emerald-500/30"
                  : "bg-rose-600/20 text-rose-400 border border-rose-500/30"
              }`}
            >
              {item.available ? "Đang Bán (Available)" : "Đã Hết Món (86ed)"}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
