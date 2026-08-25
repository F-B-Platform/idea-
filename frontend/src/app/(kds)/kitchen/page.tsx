"use client";

import Link from "next/link";
import { ArrowLeft, Clock, CheckCircle2, RotateCcw, AlertTriangle } from "lucide-react";

export default function KitchenKDSPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      {/* KDS Header Bar */}
      <header className="bg-slate-900 border-b border-slate-800 px-6 py-3 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <Link href="/" className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-lg font-bold text-white flex items-center gap-2">
              <span className="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></span>
              Web KDS Bếp — Realtime Barista Display
            </h1>
            <p className="text-xs text-slate-400">SignalR Connection: Connected (KitchenHub)</p>
          </div>
        </div>

        <div className="flex items-center gap-4 text-xs font-semibold">
          <div className="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-amber-400">
            Chờ Pha Chế: 2 Đơn
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-blue-400">
            Đang Làm: 1 Đơn
          </div>
        </div>
      </header>

      {/* KDS Kanban Order Grid */}
      <main className="flex-1 p-6 grid grid-cols-1 md:grid-cols-3 gap-4 overflow-y-auto">
        {/* Sample KDS Card 1 */}
        <div className="bg-slate-900 border border-amber-500/40 rounded-xl p-4 flex flex-col justify-between shadow-lg">
          <div className="space-y-3">
            <div className="flex items-center justify-between pb-2 border-b border-slate-800">
              <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 border border-amber-500/30">
                Bàn 03 • Dine-In
              </span>
              <span className="text-xs text-slate-400 flex items-center gap-1 font-mono">
                <Clock className="w-3.5 h-3.5 text-amber-400" />
                03:45
              </span>
            </div>

            <div className="text-sm font-bold text-white">Đơn hàng #ORD-8821</div>

            <ul className="space-y-2 text-sm text-slate-200">
              <li className="flex justify-between items-start">
                <span>1x Cà Phê Muối (Size L, 50% Đường, 70% Đá)</span>
              </li>
              <li className="flex justify-between items-start">
                <span>2x Trà Đào Cam Sả (Size M, Ít Đá)</span>
              </li>
            </ul>
          </div>

          <div className="pt-4 flex gap-2">
            <button className="flex-1 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center justify-center gap-1 shadow">
              <CheckCircle2 className="w-4 h-4" /> Hoàn Tất
            </button>
            <button className="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs">
              <RotateCcw className="w-4 h-4" />
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
