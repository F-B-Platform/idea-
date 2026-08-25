"use client";

import React from "react";
import { useRouter } from "next/navigation";
import { useKdsStore } from "@/stores/useKdsStore";
import { Layers, ArrowLeft, CheckCircle2, Coffee } from "lucide-react";
import { Button } from "@/components/ui/Button";

export default function KdsBatchingPage() {
  const router = useRouter();
  const { getBatchSummaries, updateTicketStatus } = useKdsStore();
  const summaries = getBatchSummaries();

  const handleCompleteAll = (orderIds: string[]) => {
    orderIds.forEach((id) => {
      updateTicketStatus(id, "Ready");
    });
  };

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div className="flex items-center gap-3">
          <button
            onClick={() => router.push("/kitchen")}
            className="p-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700"
          >
            <ArrowLeft className="h-5 w-5" />
          </button>
          <div>
            <h1 className="text-xl font-extrabold text-white flex items-center gap-2">
              <Layers className="h-6 w-6 text-sky-400" />
              <span>Chế Độ Gom Món Pha Chế Đồng Loạt (KDS Batch Mode)</span>
            </h1>
            <p className="text-xs text-slate-400">
              Tổng hợp định lượng tất cả món cùng loại trên nhiều đơn để Barista pha chế 1 mẻ nhanh chóng.
            </p>
          </div>
        </div>
      </div>

      {summaries.length === 0 ? (
        <div className="py-20 text-center text-slate-500 space-y-3">
          <Coffee className="h-16 w-16 mx-auto text-slate-700" />
          <h3 className="text-lg font-bold text-slate-400">Không có món nào cần gom mẻ</h3>
          <p className="text-xs">Tất cả các món đã được pha chế hoặc đang rảnh tay.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {summaries.map((batch, idx) => (
            <div
              key={idx}
              className="p-5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-4 shadow-md"
            >
              <div className="flex items-start justify-between">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-extrabold text-2xl text-amber-400">
                      {batch.totalQuantity}x
                    </span>
                    <span className="font-bold text-lg text-white">{batch.productName}</span>
                  </div>
                  <span className="text-xs font-bold text-slate-400 mt-1 block">
                    Size {batch.sizeName} • Từ {batch.orderCount} đơn hàng ({batch.orderIds.join(", ")})
                  </span>
                </div>
              </div>

              {/* Sugar / Ice Breakdown */}
              <div className="grid grid-cols-2 gap-2 text-xs bg-slate-900/70 p-3 rounded-xl text-slate-300">
                <div>
                  <span className="text-[10px] text-slate-400 font-bold uppercase block mb-1">
                    Đường:
                  </span>
                  {Object.entries(batch.sugarLevels).map(([sugar, qty]) => (
                    <span key={sugar} className="block">
                      {sugar}: <strong className="text-white">{qty} ly</strong>
                    </span>
                  ))}
                </div>

                <div>
                  <span className="text-[10px] text-slate-400 font-bold uppercase block mb-1">
                    Đá:
                  </span>
                  {Object.entries(batch.iceLevels).map(([ice, qty]) => (
                    <span key={ice} className="block">
                      {ice}: <strong className="text-white">{qty} ly</strong>
                    </span>
                  ))}
                </div>
              </div>

              {/* Complete Batch CTA */}
              <button
                type="button"
                onClick={() => handleCompleteAll(batch.orderIds)}
                className="w-full py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs rounded-xl shadow-lg flex items-center justify-center gap-2 active:scale-95 transition-all min-h-[44px]"
              >
                <CheckCircle2 className="h-4 w-4" />
                <span>HOÀN TẤT CẢ MẺ ({batch.totalQuantity} LY)</span>
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
