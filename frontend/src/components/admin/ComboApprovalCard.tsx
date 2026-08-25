"use client";

import React, { useState } from "react";
import { ComboCandidateDto } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { Slider } from "@/components/ui/Slider";
import { Button } from "@/components/ui/Button";
import { Sparkles, Check, X, TrendingUp, AlertTriangle } from "lucide-react";

export interface ComboApprovalCardProps {
  combo: ComboCandidateDto;
  onApprove: (comboId: string, comboName: string, discountPercent: number, finalPrice: number) => void;
  onReject: (comboId: string) => void;
}

export const ComboApprovalCard: React.FC<ComboApprovalCardProps> = ({
  combo,
  onApprove,
  onReject,
}) => {
  const [discountPercent, setDiscountPercent] = useState(combo.suggestedDiscountPercent || 15);
  const [comboName, setComboName] = useState(
    `Combo ${combo.productNames.join(" + ")}`
  );

  const discountAmount = Math.round((combo.originalPrice * discountPercent) / 100);
  const proposedPrice = combo.originalPrice - discountAmount;
  const projectedProfit = proposedPrice - combo.bomCost;
  const grossMarginPercent = Math.round((projectedProfit / proposedPrice) * 100);
  const isLoss = projectedProfit <= 0;

  return (
    <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-5 hover:shadow-md transition-all">
      {/* Header with AI Badge */}
      <div className="flex items-start justify-between gap-3">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <span className="inline-flex items-center gap-1 text-[11px] font-bold bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-0.5 rounded-full">
              <Sparkles className="h-3 w-3 text-amber-700" />
              <span>AI-2 Apriori (Lift: {combo.lift.toFixed(2)})</span>
            </span>
            <span className="text-xs text-slate-500">
              Support: {(combo.support * 100).toFixed(1)}% • Conf: {(combo.confidence * 100).toFixed(1)}%
            </span>
          </div>

          <input
            type="text"
            value={comboName}
            onChange={(e) => setComboName(e.target.value)}
            className="text-base font-bold text-slate-900 w-full border-b border-transparent hover:border-slate-300 focus:border-amber-600 focus:outline-none bg-transparent py-0.5"
          />
        </div>

        <div className="text-right shrink-0">
          <span className="text-xs text-slate-400 line-through block">
            {formatCurrencyVND(combo.originalPrice)}
          </span>
          <span className="text-lg font-black text-amber-800">
            {formatCurrencyVND(proposedPrice)}
          </span>
        </div>
      </div>

      {/* BOM Cost & Profit Breakdown Matrix */}
      <div className="grid grid-cols-3 gap-3 p-3.5 rounded-xl bg-slate-50 border border-slate-200 text-xs">
        <div>
          <span className="text-slate-500 block">Giá Vốn BOM:</span>
          <span className="font-bold text-slate-800">{formatCurrencyVND(combo.bomCost)}</span>
        </div>
        <div>
          <span className="text-slate-500 block">Lợi Nhuận Gộp:</span>
          <span className={`font-bold ${isLoss ? "text-rose-600" : "text-emerald-700"}`}>
            {formatCurrencyVND(projectedProfit)}
          </span>
        </div>
        <div>
          <span className="text-slate-500 block">Biên Lợi Nhuận:</span>
          <span className={`font-bold ${isLoss ? "text-rose-600" : "text-emerald-700"}`}>
            {grossMarginPercent}%
          </span>
        </div>
      </div>

      {/* Discount Slider */}
      <div className="space-y-2">
        <Slider
          label="Điều chỉnh mức chiết khấu combo"
          min={5}
          max={35}
          step={1}
          value={discountPercent}
          valueSuffix="%"
          onChange={setDiscountPercent}
        />
      </div>

      {/* Warning if loss */}
      {isLoss && (
        <div className="p-3 bg-rose-50 border border-rose-300 rounded-xl text-xs text-rose-900 flex items-center gap-2">
          <AlertTriangle className="h-4 w-4 text-rose-600 shrink-0" />
          <span>CẢNH BÁO: Mức chiết khấu khiến combo bị lỗ vốn so với định mức BOM!</span>
        </div>
      )}

      {/* Action Buttons */}
      <div className="flex items-center gap-3 pt-2">
        <Button
          type="button"
          onClick={() => onReject(combo.id)}
          variant="secondary"
          className="flex-1"
          leftIcon={<X className="h-4 w-4" />}
        >
          Từ Chối
        </Button>
        <Button
          type="button"
          onClick={() => onApprove(combo.id, comboName, discountPercent, proposedPrice)}
          variant="primary"
          disabled={isLoss}
          className="flex-1"
          leftIcon={<Check className="h-4 w-4" />}
        >
          Phê Duyệt & Phát Hành
        </Button>
      </div>
    </div>
  );
};
