"use client";

import React from "react";
import { VALID_DENOMINATIONS } from "@/stores/useShiftStore";
import { formatCurrencyVND } from "@/lib/utils";
import { Textarea } from "@/components/ui/Textarea";
import { AlertTriangle, CheckCircle2, DollarSign, Calculator } from "lucide-react";

export interface DenominationCounterProps {
  denominations: Record<number, number>;
  onCountChange: (denomination: number, count: number) => void;
  theoreticalCash: number;
  physicalCashTotal: number;
  variance: number;
  justificationReason: string;
  onJustificationChange: (reason: string) => void;
}

export const DenominationCounter: React.FC<DenominationCounterProps> = ({
  denominations,
  onCountChange,
  theoreticalCash,
  physicalCashTotal,
  variance,
  justificationReason,
  onJustificationChange,
}) => {
  const hasVariance = variance !== 0;
  const isSevereVariance = Math.abs(variance) > 50000;

  return (
    <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-6">
      {/* Title */}
      <div className="flex items-center justify-between border-b border-slate-100 pb-4">
        <div className="flex items-center gap-2">
          <Calculator className="h-5 w-5 text-amber-700" />
          <h3 className="font-bold text-base text-slate-900">
            Bảng Đếm Tiền Mặt 6 Mệnh Giá Đối Soát Z-Report
          </h3>
        </div>
        <span className="text-xs text-slate-500 font-medium">Bắt buộc kiểm đếm cuối ca</span>
      </div>

      {/* 6 Denominations Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {VALID_DENOMINATIONS.map((denom) => {
          const count = denominations[denom] || 0;
          const subtotal = denom * count;

          return (
            <div
              key={denom}
              className="p-4 rounded-xl border border-slate-200 bg-slate-50/50 hover:bg-slate-50 transition-colors space-y-2"
            >
              <div className="flex items-center justify-between">
                <span className="font-bold text-sm text-slate-800">
                  {formatCurrencyVND(denom)}
                </span>
                <span className="text-xs font-semibold text-amber-800 bg-amber-100 px-2 py-0.5 rounded">
                  {formatCurrencyVND(subtotal)}
                </span>
              </div>

              <div className="flex items-center gap-2">
                <input
                  type="number"
                  min="0"
                  value={count === 0 ? "" : count}
                  onChange={(e) => onCountChange(denom, Number(e.target.value) || 0)}
                  placeholder="Số tờ..."
                  className="w-full px-3 py-2 text-sm font-semibold rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-amber-600 min-h-[40px]"
                />
                <span className="text-xs text-slate-500 shrink-0">tờ</span>
              </div>
            </div>
          );
        })}
      </div>

      {/* Summary Box */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 p-4 rounded-xl bg-slate-100/70 border border-slate-200">
        <div>
          <span className="text-xs font-semibold text-slate-500 block">Lý thuyết hệ thống:</span>
          <span className="text-lg font-bold text-slate-800">
            {formatCurrencyVND(theoreticalCash)}
          </span>
        </div>

        <div>
          <span className="text-xs font-semibold text-slate-500 block">Thực đếm trong két:</span>
          <span className="text-lg font-bold text-amber-900">
            {formatCurrencyVND(physicalCashTotal)}
          </span>
        </div>

        <div>
          <span className="text-xs font-semibold text-slate-500 block">Chênh lệch (Variance):</span>
          <span
            className={`text-lg font-black ${
              variance === 0
                ? "text-emerald-600"
                : variance > 0
                ? "text-sky-600"
                : "text-rose-600"
            }`}
          >
            {variance > 0 ? "+" : ""}
            {formatCurrencyVND(variance)}
          </span>
        </div>
      </div>

      {/* Variance Alert & Justification Textarea */}
      {hasVariance && (
        <div className="space-y-3 pt-2">
          <div
            className={`p-4 rounded-xl border flex items-start gap-3 ${
              isSevereVariance
                ? "bg-rose-50 border-rose-300 text-rose-950"
                : "bg-amber-50 border-amber-300 text-amber-950"
            }`}
          >
            <AlertTriangle className="h-5 w-5 text-rose-600 shrink-0 mt-0.5" />
            <div className="text-xs space-y-1">
              <h5 className="font-bold text-sm">
                Phát hiện chênh lệch tiền két ({formatCurrencyVND(variance)})
              </h5>
              <p>
                {isSevereVariance
                  ? "CẢNH BÁO: Chênh lệch vượt ngưỡng 50.000₫! Hệ thống sẽ tự động kích hoạt cảnh báo Red Alert tới Chủ chuỗi."
                  : "Vui lòng nhập lý do giải trình chi tiết về khoản chênh lệch tiền mặt này trước khi chốt ca."}
              </p>
            </div>
          </div>

          <Textarea
            label="Lý Do Giải Trình Chênh Lệch Tiền Mặt (Bắt buộc)"
            required
            value={justificationReason}
            onChange={(e) => onJustificationChange(e.target.value)}
            placeholder="Ví dụ: Thối nhầm tiền khách bàn 04 20k, bù tiền lẻ đầu ca..."
            rows={2}
          />
        </div>
      )}
    </div>
  );
};
