"use client";

import Link from "next/link";
import { ArrowLeft, Layers } from "lucide-react";

export default function KdsBatchViewPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 space-y-6">
      <header className="flex items-center gap-3 pb-4 border-b border-slate-800">
        <Link href="/kitchen" className="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="text-lg font-bold text-white flex items-center gap-2">
            <Layers className="w-5 h-5 text-blue-400" />
            Chế Độ Gom Đơn Theo Mẻ (Batch Production View)
          </h1>
          <p className="text-xs text-slate-400">Tự động tổng hợp số lượng từng loại đồ uống đang chờ pha chế để barista pha chế hàng loạt.</p>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {[
          { name: "Cà Phê Muối Hoàng Gia", totalQty: 4, orders: ["#ORD-8821", "#ORD-8824"] },
          { name: "Trà Đào Cam Sả Tươi", totalQty: 3, orders: ["#ORD-8821", "#ORD-8822"] },
          { name: "Trà Sữa Oolong Nướng", totalQty: 2, orders: ["#ORD-8823"] },
        ].map((batch, idx) => (
          <div key={idx} className="p-4 bg-slate-900 border border-slate-800 rounded-xl space-y-2">
            <div className="flex justify-between items-start">
              <h2 className="text-sm font-bold">{batch.name}</h2>
              <span className="px-2.5 py-1 rounded-lg bg-blue-600/30 text-blue-400 font-extrabold text-sm border border-blue-500/30">
                x{batch.totalQty} ly
              </span>
            </div>
            <p className="text-xs text-slate-500">Bao gồm trong đơn: {batch.orders.join(", ")}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
