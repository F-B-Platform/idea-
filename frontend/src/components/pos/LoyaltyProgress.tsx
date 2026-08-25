import React from "react";
import { Coffee, Gift, CheckCircle2, RotateCcw } from "lucide-react";
import { cn } from "@/lib/utils";

export interface LoyaltyProgressProps {
  cupBalance: number;
  freeCupRedeemed: boolean;
  onRedeem: () => void;
  onCancelRedeem: () => void;
  disabled?: boolean;
}

export const LoyaltyProgress: React.FC<LoyaltyProgressProps> = ({
  cupBalance,
  freeCupRedeemed,
  onRedeem,
  onCancelRedeem,
  disabled = false,
}) => {
  const maxCups = 10;
  const clampedBalance = Math.min(maxCups, Math.max(0, cupBalance));
  const isEligible = cupBalance >= 10;

  return (
    <div className="bg-gradient-to-br from-amber-50 to-orange-50/60 rounded-2xl p-4 border border-amber-200/80 shadow-sm space-y-3.5">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Gift className="h-5 w-5 text-amber-700" />
          <span className="font-bold text-sm text-amber-950">Chương Trình 10 Ly Tặng 1</span>
        </div>
        <span className="font-extrabold text-sm text-amber-900 bg-amber-200/60 px-2.5 py-0.5 rounded-full">
          {cupBalance}/{maxCups} Ly
        </span>
      </div>

      {/* 10 Stamps Visual Grid */}
      <div className="grid grid-cols-5 gap-2">
        {Array.from({ length: maxCups }).map((_, idx) => {
          const isStamped = idx < clampedBalance;
          const isTenth = idx === 9;

          return (
            <div
              key={idx}
              className={cn(
                "h-11 rounded-xl border-2 flex flex-col items-center justify-center transition-all",
                isStamped
                  ? isTenth
                    ? "bg-emerald-600 border-emerald-700 text-white shadow-md ring-2 ring-emerald-300"
                    : "bg-amber-600 border-amber-700 text-white shadow-sm"
                  : "bg-white border-dashed border-amber-300 text-amber-300"
              )}
            >
              {isTenth ? (
                <Gift className="h-5 w-5" />
              ) : (
                <Coffee className={cn("h-4 w-4", isStamped ? "fill-current" : "")} />
              )}
              <span className="text-[9px] font-bold mt-0.5 leading-none">
                {isTenth ? "FREE" : `#${idx + 1}`}
              </span>
            </div>
          );
        })}
      </div>

      {/* Redemption Action Bar */}
      {isEligible && (
        <div className="pt-1">
          {freeCupRedeemed ? (
            <div className="flex items-center justify-between bg-emerald-100 border border-emerald-300 p-2.5 rounded-xl">
              <div className="flex items-center gap-2 text-emerald-900 text-xs font-bold">
                <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
                <span>ĐÃ ÁP DỤNG ĐỔI 1 LY MIỄN PHÍ (-35.000₫)</span>
              </div>
              <button
                type="button"
                onClick={onCancelRedeem}
                className="text-xs font-semibold text-rose-700 hover:text-rose-900 flex items-center gap-1 p-1 hover:bg-rose-50 rounded"
              >
                <RotateCcw className="h-3 w-3" />
                <span>Hủy</span>
              </button>
            </div>
          ) : (
            <button
              type="button"
              onClick={onRedeem}
              disabled={disabled}
              className="w-full py-2.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-extrabold text-xs rounded-xl shadow-md flex items-center justify-center gap-2 active:scale-95 transition-all animate-bounce"
            >
              <Gift className="h-4 w-4" />
              <span>BẤM ĐỔI 1 LY MIỄN PHÍ NGAY (-35.000₫)</span>
            </button>
          )}
        </div>
      )}
    </div>
  );
};
