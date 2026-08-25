"use client";

import React, { useEffect } from "react";
import { X } from "lucide-react";
import { cn } from "@/lib/utils";

export interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: React.ReactNode;
  description?: React.ReactNode;
  children: React.ReactNode;
  footer?: React.ReactNode;
  maxWidth?: "sm" | "md" | "lg" | "xl" | "2xl" | "3xl" | "full";
  className?: string;
  dark?: boolean;
}

export const Modal: React.FC<ModalProps> = ({
  isOpen,
  onClose,
  title,
  description,
  children,
  footer,
  maxWidth = "lg",
  className,
  dark = false,
}) => {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "unset";
    }
    return () => {
      document.body.style.overflow = "unset";
    };
  }, [isOpen]);

  if (!isOpen) return null;

  const maxWidthClasses = {
    sm: "max-w-sm",
    md: "max-w-md",
    lg: "max-w-lg",
    xl: "max-w-xl",
    "2xl": "max-w-2xl",
    "3xl": "max-w-3xl",
    full: "max-w-5xl",
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 overflow-y-auto">
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black/60 backdrop-blur-sm transition-opacity"
        onClick={onClose}
      />

      {/* Modal Dialog */}
      <div
        className={cn(
          "relative w-full rounded-2xl shadow-2xl transition-all transform z-10 flex flex-col max-h-[90vh] overflow-hidden",
          dark ? "bg-slate-900 text-slate-100 border border-slate-800" : "bg-white text-slate-900 border border-slate-100",
          maxWidthClasses[maxWidth],
          className
        )}
      >
        {/* Header */}
        {(title || description) && (
          <div
            className={cn(
              "px-6 py-4 border-b flex items-start justify-between gap-4 shrink-0",
              dark ? "border-slate-800" : "border-slate-100"
            )}
          >
            <div>
              {title && <h3 className="text-lg font-bold leading-6">{title}</h3>}
              {description && (
                <p className={cn("text-xs mt-1", dark ? "text-slate-400" : "text-slate-500")}>
                  {description}
                </p>
              )}
            </div>
            <button
              onClick={onClose}
              className={cn(
                "p-1.5 rounded-lg transition-colors -mr-1",
                dark ? "text-slate-400 hover:text-white hover:bg-slate-800" : "text-slate-400 hover:text-slate-600 hover:bg-slate-100"
              )}
            >
              <X className="h-5 w-5" />
            </button>
          </div>
        )}

        {/* Content Body */}
        <div className="px-6 py-5 overflow-y-auto flex-1">{children}</div>

        {/* Footer */}
        {footer && (
          <div
            className={cn(
              "px-6 py-4 border-t flex items-center justify-end gap-3 shrink-0",
              dark ? "border-slate-800 bg-slate-950/40" : "border-slate-100 bg-slate-50/50"
            )}
          >
            {footer}
          </div>
        )}
      </div>
    </div>
  );
};
