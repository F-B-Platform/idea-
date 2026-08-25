import React from "react";
import { cn } from "@/lib/utils";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "danger" | "outline" | "ghost" | "amber" | "dark";
  size?: "sm" | "md" | "lg" | "xl" | "icon";
  isLoading?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      className,
      variant = "primary",
      size = "md",
      isLoading = false,
      leftIcon,
      rightIcon,
      children,
      disabled,
      ...props
    },
    ref
  ) => {
    const baseStyles =
      "inline-flex items-center justify-center font-medium transition-all duration-150 rounded-lg focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed select-none active:scale-[0.98]";

    const variantStyles = {
      primary: "bg-amber-700 text-white hover:bg-amber-800 focus:ring-amber-600 shadow-sm",
      amber: "bg-amber-600 text-white hover:bg-amber-700 focus:ring-amber-500 shadow-sm",
      secondary: "bg-slate-100 text-slate-900 hover:bg-slate-200 focus:ring-slate-400 border border-slate-200",
      danger: "bg-rose-600 text-white hover:bg-rose-700 focus:ring-rose-500 shadow-sm",
      outline: "border border-amber-700 text-amber-700 hover:bg-amber-50 focus:ring-amber-600",
      ghost: "text-slate-700 hover:bg-slate-100 focus:ring-slate-300",
      dark: "bg-slate-800 text-slate-100 hover:bg-slate-700 border border-slate-700 focus:ring-slate-500",
    };

    const sizeStyles = {
      sm: "text-xs px-2.5 py-1.5 min-h-[36px] gap-1.5",
      md: "text-sm px-4 py-2 min-h-[44px] gap-2", // 44px for WCAG 2.1 AA touch target
      lg: "text-base px-5 py-2.5 min-h-[48px] gap-2.5 font-semibold",
      xl: "text-lg px-6 py-3.5 min-h-[54px] gap-3 font-bold",
      icon: "p-2 min-h-[44px] min-w-[44px] justify-center",
    };

    return (
      <button
        ref={ref}
        className={cn(baseStyles, variantStyles[variant], sizeStyles[size], className)}
        disabled={disabled || isLoading}
        {...props}
      >
        {isLoading ? (
          <span className="flex items-center gap-2">
            <svg
              className="animate-spin h-4 w-4 text-current"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            <span>{children}</span>
          </span>
        ) : (
          <>
            {leftIcon && <span className="inline-flex shrink-0">{leftIcon}</span>}
            {children}
            {rightIcon && <span className="inline-flex shrink-0">{rightIcon}</span>}
          </>
        )}
      </button>
    );
  }
);

Button.displayName = "Button";
