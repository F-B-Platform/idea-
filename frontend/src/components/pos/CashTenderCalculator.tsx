import React from "react";
import { formatCurrencyVND } from "@/lib/utils";
import { DollarSign, ArrowRight, AlertTriangle } from "lucide-react";

export interface CashTenderCalculatorProps {
  netTotal: number;
  tenderAmount: number;
  onTenderChange: (amount: number) => void;
}

export const CashTenderCalculator: React.FC<CashTenderCalculatorProps> = ({
  netTotal,
  tenderAmount,
  onTenderChange,
}) => {
  const quickAmounts = [
    { label: "Vừa Đủ", value: netTotal },
    { label: "50k", value: 50000 },
    { label: "100k", value: 100000 },
    { label: "200k", value: 200000 },
    { label: "500k", value: 500000 },
  ];

  const changeAmount = Math.max(0, tenderAmount - netTotal);
  const isShort = tenderAmount > 0 && tenderAmount < netTotal;

  return (
    <div className="bg-white rounded-2xl p-4 border border-slate-200 shadow-sm space-y-4">
      <div className="flex items-center justify-between">
        <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
          Tính Tiền Mặt Khách Đưa & Tiền Thừa
        </span>
        <span className="text-xs font-bold text-amber-800">
          Cần Thu: {formatCurrencyVND(netTotal)}
        </span>
      </div>

      {/* Quick Amount Buttons */}
      <div className="grid grid-cols-5 gap-1.5">
        {quickAmounts.map((qa, idx) => (
          <button
            key={idx}
            type="button"
            onClick={() => onTenderChange(qa.value)}
            className="py-2 px-1 rounded-lg border border-slate-200 hover:border-amber-600 hover:bg-amber-50 text-xs font-semibold text-slate-800 transition-all active:scale-95"
          >
            {qa.label}
          </button>
        ))}
      </div>

      {/* Tender Input */}
      <div className="space-y-1">
        <label className="block text-xs font-medium text-slate-600">Số tiền khách đưa (₫):</label>
        <div className="relative">
          <input
            type="number"
            value={tenderAmount || ""}
            onChange={(e) => onTenderChange(Number(e.target.value))}
            placeholder="Ví dụ: 100000"
            className="w-full pl-3.5 pr-4 py-2.5 rounded-xl border border-slate-300 font-extrabold text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-600 min-h-[44px]"
          />
        </div>
      </div>

      {/* Change Display Box */}
      <div
        className={`p-3.5 rounded-xl border flex items-center justify-between transition-colors ${
          isShort
            ? "bg-rose-50 border-rose-300 text-rose-900"
            : tenderAmount >= netTotal
            ? "bg-emerald-50 border-emerald-300 text-emerald-950"
            : "bg-slate-50 border-slate-200 text-slate-800"
        }`}
      >
        <div className="flex items-center gap-2">
          {isShort ? (
            <AlertTriangle className="h-5 w-5 text-rose-500 shrink-0" />
          ) : (
            <DollarSign className="h-5 w-5 text-emerald-600 shrink-0" />
          )}
          <div>
            <span className="text-xs font-medium block">
              {isShort ? "Khách đưa thiếu:" : "Tiền thối lại khách:"}
            </span>
            <span className="text-lg font-black">
              {isShort
                ? formatCurrencyVND(netTotal - tenderAmount)
                : formatCurrencyVND(changeAmount)}
            </span>
          </div>
        </div>

        {tenderAmount >= netTotal && tenderAmount > 0 && (
          <span className="text-xs font-bold text-emerald-700 bg-emerald-100 px-2 py-1 rounded-lg">
            Hợp Lệ
          </span>
        )}
      </div>
    </div>
  );
};
