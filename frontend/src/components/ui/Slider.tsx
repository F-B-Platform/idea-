import React from "react";
import { cn } from "@/lib/utils";

export interface SliderProps {
  min: number;
  max: number;
  step?: number;
  value: number;
  onChange: (value: number) => void;
  label?: string;
  valuePrefix?: string;
  valueSuffix?: string;
  className?: string;
  disabled?: boolean;
}

export const Slider: React.FC<SliderProps> = ({
  min,
  max,
  step = 1,
  value,
  onChange,
  label,
  valuePrefix = "",
  valueSuffix = "",
  className,
  disabled = false,
}) => {
  return (
    <div className={cn("w-full space-y-2", className)}>
      <div className="flex justify-between items-center text-sm font-medium text-slate-700">
        {label && <span>{label}</span>}
        <span className="font-semibold text-amber-700">
          {valuePrefix}
          {value}
          {valueSuffix}
        </span>
      </div>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        disabled={disabled}
        onChange={(e) => onChange(Number(e.target.value))}
        className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-amber-700 focus:outline-none focus:ring-2 focus:ring-amber-500 disabled:opacity-50"
      />
      <div className="flex justify-between text-[11px] text-slate-400">
        <span>
          {valuePrefix}
          {min}
          {valueSuffix}
        </span>
        <span>
          {valuePrefix}
          {max}
          {valueSuffix}
        </span>
      </div>
    </div>
  );
};
