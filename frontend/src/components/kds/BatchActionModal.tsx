"use client";

import React from "react";
import { Modal } from "@/components/ui/Modal";
import { BatchItemSummary } from "@/types";
import { Layers, CheckCircle2, Coffee } from "lucide-react";

export interface BatchActionModalProps {
  isOpen: boolean;
  onClose: () => void;
  batchSummaries: BatchItemSummary[];
  onCompleteBatch: (orderIds: string[]) => void;
}

export const BatchActionModal: React.FC<BatchActionModalProps> = ({
  isOpen,
  onClose,
  batchSummaries,
  onCompleteBatch,
}) => {
  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      dark
      maxWidth="2xl"
      title={
        <div className="flex items-center gap-2 text-sky-400">
          <Layers className="h-6 w-6" />
          <span>Gom Món Pha Chế Đồng Loạt (KDS Batch Mode)</span>
        </div>
      }
      description="Tổng hợp tất cả đồ uống cùng loại từ các đơn hàng đang chờ để pha chế 1 mẻ trong giờ cao điểm."
      footer={
        <button
          onClick={onClose}
          className="px-5 py-2.5 bg-slate-700 hover:bg-slate-600 text-white text-xs font-bold rounded-xl"
        >
          Đóng Cửa Sổ
        </button>
      }
    >
      <div className="space-y-4">
        {batchSummaries.length === 0 ? (
          <div className="py-12 text-center text-slate-400 space-y-2">
            <Coffee className="h-10 w-10 mx-auto text-slate-600" />
            <p className="text-sm">Hiện không có món nào đang chờ pha chế để gom mẻ.</p>
          </div>
        ) : (
          <div className="space-y-3 max-h-[420px] overflow-y-auto pr-1">
            {batchSummaries.map((batch, idx) => (
              <div
                key={idx}
                className="p-4 rounded-xl bg-slate-800/80 border border-slate-700 space-y-3"
              >
                <div className="flex items-start justify-between">
                  <div className="space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="font-extrabold text-lg text-amber-400">
                        {batch.totalQuantity}x
                      </span>
                      <span className="font-bold text-base text-white">{batch.productName}</span>
                      <span className="text-xs font-bold text-slate-300 bg-slate-700 px-2 py-0.5 rounded">
                        Size {batch.sizeName}
                      </span>
                    </div>
                    <p className="text-xs text-slate-400">
                      Gom từ {batch.orderCount} đơn hàng ({batch.orderIds.join(", ")})
                    </p>
                  </div>

                  <button
                    type="button"
                    onClick={() => {
                      onCompleteBatch(batch.orderIds);
                    }}
                    className="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs rounded-xl flex items-center gap-1.5 shadow-md active:scale-95 transition-all"
                  >
                    <CheckCircle2 className="h-4 w-4" />
                    <span>Xong Cả Mẻ ({batch.totalQuantity})</span>
                  </button>
                </div>

                {/* Breakdown by sugar & ice */}
                <div className="grid grid-cols-2 gap-2 text-xs bg-slate-900/60 p-2.5 rounded-lg text-slate-300">
                  <div>
                    <span className="text-[11px] text-slate-400 font-semibold uppercase block mb-1">
                      Chi tiết Đường:
                    </span>
                    {Object.entries(batch.sugarLevels).map(([sugar, qty]) => (
                      <span key={sugar} className="mr-2 inline-block">
                        {sugar}: <strong className="text-white">{qty} ly</strong>
                      </span>
                    ))}
                  </div>

                  <div>
                    <span className="text-[11px] text-slate-400 font-semibold uppercase block mb-1">
                      Chi tiết Đá:
                    </span>
                    {Object.entries(batch.iceLevels).map(([ice, qty]) => (
                      <span key={ice} className="mr-2 inline-block">
                        {ice}: <strong className="text-white">{qty} ly</strong>
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </Modal>
  );
};
