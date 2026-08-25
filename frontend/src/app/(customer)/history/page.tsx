"use client";

import Link from "next/link";
import { ArrowLeft, Clock, CheckCircle2 } from "lucide-react";

export default function OrderHistoryPage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 max-w-md mx-auto space-y-4">
      <header className="flex items-center gap-2 py-2 border-b border-slate-200">
        <Link href="/menu" className="p-2 rounded-full hover:bg-slate-200 text-slate-600">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <h1 className="text-base font-bold text-slate-900">Lịch Sử Đơn Hàng</h1>
      </header>

      <div className="space-y-3">
        {[
          { id: "ORD-8821", date: "Hôm nay, 10:15", items: "1x Cà Phê Muối, 1x Trà Đào", total: "77.000đ", status: "Hoàn tất" },
          { id: "ORD-7742", date: "Hôm qua, 15:30", items: "2x Trà Sữa Oolong", total: "78.000đ", status: "Hoàn tất" },
        ].map((order, idx) => (
          <div key={idx} className="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
            <div className="flex justify-between items-center text-xs">
              <span className="font-mono font-bold text-slate-900">#{order.id}</span>
              <span className="text-slate-400 flex items-center gap-1"><Clock className="w-3 h-3" /> {order.date}</span>
            </div>
            <p className="text-xs text-slate-600">{order.items}</p>
            <div className="flex justify-between items-center pt-2 border-t border-slate-100 text-xs">
              <span className="font-bold text-orange-600">{order.total}</span>
              <span className="px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-semibold flex items-center gap-1 border border-emerald-200">
                <CheckCircle2 className="w-3 h-3" /> {order.status}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
