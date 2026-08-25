"use client";

import React from "react";
import { CheckCircle2, AlertCircle, AlertTriangle, Info, X } from "lucide-react";
import { cn } from "@/lib/utils";

export interface ToastProps {
  type?: "success" | "error" | "warning" | "info";
  title?: string;
  message: string;
  onClose?: () => void;
  className?: string;
}

export const Toast: React.FC<ToastProps> = ({
  type = "info",
  title,
  message,
  onClose,
  className,
}) => {
  const icons = {
    success: <CheckCircle2 className="h-5 w-5 text-emerald-500 shrink-0" />,
    error: <AlertCircle className="h-5 w-5 text-rose-500 shrink-0" />,
    warning: <AlertTriangle className="h-5 w-5 text-amber-500 shrink-0" />,
    info: <Info className="h-5 w-5 text-sky-500 shrink-0" />,
  };

  const borderClasses = {
    success: "border-emerald-200 bg-emerald-50/90 text-emerald-950",
    error: "border-rose-200 bg-rose-50/90 text-rose-950",
    warning: "border-amber-200 bg-amber-50/90 text-amber-950",
    info: "border-sky-200 bg-sky-50/90 text-sky-950",
  };

  return (
    <div
      className={cn(
        "flex items-start gap-3 p-4 rounded-xl border shadow-lg backdrop-blur-md transition-all duration-200 animate-in slide-in-from-top-2",
        borderClasses[type],
        className
      )}
    >
      {icons[type]}
      <div className="flex-1 text-sm">
        {title && <h4 className="font-semibold leading-5">{title}</h4>}
        <p className={cn("text-xs leading-relaxed", title && "mt-0.5 opacity-90")}>{message}</p>
      </div>
      {onClose && (
        <button
          onClick={onClose}
          className="p-1 rounded-md text-slate-400 hover:text-slate-700 hover:bg-black/5"
        >
          <X className="h-4 w-4" />
        </button>
      )}
    </div>
  );
};
