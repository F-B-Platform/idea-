"use client";

import React from "react";
import { SugarLevel, IceLevel, ProductModifierDto, ProductSizeDto } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { cn } from "@/lib/utils";

interface ModifierSelectorProps {
  sizes?: ProductSizeDto[];
  selectedSizeId: string;
  onSelectSize: (size: ProductSizeDto) => void;

  sugarLevel: SugarLevel | string;
  onSelectSugar: (sugar: SugarLevel) => void;

  iceLevel: IceLevel | string;
  onSelectIce: (ice: IceLevel) => void;

  availableModifiers?: ProductModifierDto[];
  selectedModifierIds: string[];
  onToggleModifier: (modifier: ProductModifierDto) => void;
}

export const ModifierSelector: React.FC<ModifierSelectorProps> = ({
  sizes = [],
  selectedSizeId,
  onSelectSize,
  sugarLevel,
  onSelectSugar,
  iceLevel,
  onSelectIce,
  availableModifiers = [],
  selectedModifierIds,
  onToggleModifier,
}) => {
  const sugarOptions: SugarLevel[] = ["0%", "30%", "50%", "70%", "100%"];
  const iceOptions: IceLevel[] = ["0%", "30%", "50%", "70%", "100%"];

  return (
    <div className="space-y-6">
      {/* Size Selector */}
      {sizes.length > 0 && (
        <div className="space-y-2.5">
          <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
            1. Chọn Kích Cỡ (Size) <span className="text-rose-500">*</span>
          </label>
          <div className="grid grid-cols-3 gap-2.5">
            {sizes.map((size) => {
              const isSelected = size.id === selectedSizeId;
              return (
                <button
                  type="button"
                  key={size.id}
                  onClick={() => onSelectSize(size)}
                  className={cn(
                    "flex flex-col items-center justify-center p-3 rounded-xl border-2 transition-all min-h-[58px]",
                    isSelected
                      ? "border-amber-700 bg-amber-50/50 text-amber-900 shadow-sm"
                      : "border-slate-200 hover:border-slate-300 text-slate-700 bg-white"
                  )}
                >
                  <span className="font-bold text-sm">Size {size.sizeName}</span>
                  <span className="text-xs text-amber-700 font-semibold mt-0.5">
                    {formatCurrencyVND(size.price)}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* Sugar Level Selector */}
      <div className="space-y-2.5">
        <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
          2. Chọn Mức Đường
        </label>
        <div className="grid grid-cols-5 gap-1.5">
          {sugarOptions.map((sugar) => {
            const isSelected = sugarLevel === sugar;
            return (
              <button
                type="button"
                key={sugar}
                onClick={() => onSelectSugar(sugar)}
                className={cn(
                  "py-2 px-1 rounded-lg border text-xs font-semibold transition-all min-h-[44px]",
                  isSelected
                    ? "border-amber-700 bg-amber-700 text-white shadow-sm"
                    : "border-slate-200 text-slate-700 bg-white hover:bg-slate-50"
                )}
              >
                {sugar}
              </button>
            );
          })}
        </div>
      </div>

      {/* Ice Level Selector */}
      <div className="space-y-2.5">
        <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
          3. Chọn Mức Đá
        </label>
        <div className="grid grid-cols-5 gap-1.5">
          {iceOptions.map((ice) => {
            const isSelected = iceLevel === ice;
            return (
              <button
                type="button"
                key={ice}
                onClick={() => onSelectIce(ice)}
                className={cn(
                  "py-2 px-1 rounded-lg border text-xs font-semibold transition-all min-h-[44px]",
                  isSelected
                    ? "border-amber-700 bg-amber-700 text-white shadow-sm"
                    : "border-slate-200 text-slate-700 bg-white hover:bg-slate-50"
                )}
              >
                {ice === "0%" ? "K.Đá" : ice}
              </button>
            );
          })}
        </div>
      </div>

      {/* Toppings / Modifiers Selector */}
      {availableModifiers.length > 0 && (
        <div className="space-y-2.5">
          <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
            4. Topping Thêm
          </label>
          <div className="grid grid-cols-2 gap-2">
            {availableModifiers.map((mod) => {
              const isSelected = selectedModifierIds.includes(mod.id);
              return (
                <button
                  type="button"
                  key={mod.id}
                  onClick={() => onToggleModifier(mod)}
                  className={cn(
                    "flex items-center justify-between p-3 rounded-xl border-2 text-left transition-all min-h-[48px]",
                    isSelected
                      ? "border-amber-700 bg-amber-50/60 text-amber-950"
                      : "border-slate-200 text-slate-700 bg-white hover:border-slate-300"
                  )}
                >
                  <span className="text-xs font-medium">{mod.name}</span>
                  <span className="text-xs font-bold text-amber-800">
                    +{formatCurrencyVND(mod.priceAdjustment)}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};
