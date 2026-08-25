import React from "react";
import { OrderStatus, OrderType } from "@/types";
import { Check, Clock, Coffee, Truck, CheckCircle2, XCircle } from "lucide-react";
import { cn } from "@/lib/utils";

export interface LiveStepperProps {
  status: OrderStatus;
  orderType: OrderType;
  estimatedMinutes?: number;
  queuePosition?: number;
}

export const LiveStepper: React.FC<LiveStepperProps> = ({
  status,
  orderType,
  estimatedMinutes = 5,
  queuePosition = 1,
}) => {
  const isDelivery = orderType === "Delivery";

  const steps = isDelivery
    ? [
        { key: "Confirmed", label: "Tiếp Nhận", icon: CheckCircle2 },
        { key: "Preparing", label: "Pha Chế", icon: Coffee },
        { key: "Delivering", label: "Đang Giao", icon: Truck },
        { key: "Completed", label: "Giao Xong", icon: Check },
      ]
    : [
        { key: "Confirmed", label: "Tiếp Nhận", icon: CheckCircle2 },
        { key: "Preparing", label: "Pha Chế", icon: Coffee },
        { key: "Ready", label: "Sẵn Sàng", icon: CheckCircle2 },
        { key: "Served", label: "Đã Phục Vụ", icon: Check },
      ];

  const getStepIndex = (currentStatus: OrderStatus): number => {
    switch (currentStatus) {
      case "PendingPayment":
        return -1;
      case "Paid":
      case "Confirmed":
        return 0;
      case "Preparing":
        return 1;
      case "Ready":
      case "Delivering":
        return 2;
      case "Served":
      case "Completed":
        return 3;
      case "Cancelled":
        return -2;
      default:
        return 0;
    }
  };

  const currentIndex = getStepIndex(status);

  if (status === "Cancelled") {
    return (
      <div className="bg-rose-50 border border-rose-200 rounded-2xl p-4 text-center space-y-2">
        <XCircle className="h-8 w-8 text-rose-500 mx-auto" />
        <h4 className="font-bold text-rose-900">Đơn Hàng Đã Hủy</h4>
        <p className="text-xs text-rose-700">Đơn hàng này đã bị hủy hoặc hoàn trả do quá hạn.</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm space-y-5">
      {/* Top status info banner */}
      <div className="flex items-center justify-between text-xs bg-amber-50/70 border border-amber-200/60 p-3 rounded-xl">
        <div className="flex items-center gap-1.5 text-amber-900 font-medium">
          <Clock className="h-4 w-4 text-amber-700 shrink-0" />
          <span>Dự kiến xong: ~{estimatedMinutes} phút</span>
        </div>
        {queuePosition > 0 && (
          <span className="font-bold text-amber-800 bg-amber-200/60 px-2 py-0.5 rounded-full">
            #{queuePosition} trong hàng đợi
          </span>
        )}
      </div>

      {/* Stepper progress nodes */}
      <div className="relative flex items-center justify-between">
        {/* Background connector line */}
        <div className="absolute left-6 right-6 top-1/2 -translate-y-1/2 h-1 bg-slate-200 -z-0" />

        {/* Active progress connector line */}
        <div
          className="absolute left-6 top-1/2 -translate-y-1/2 h-1 bg-amber-700 transition-all duration-500 -z-0"
          style={{
            width: `${Math.max(0, Math.min(100, (currentIndex / (steps.length - 1)) * 100))}%`,
          }}
        />

        {steps.map((step, idx) => {
          const isPassed = idx < currentIndex;
          const isCurrent = idx === currentIndex;
          const StepIcon = step.icon;

          return (
            <div key={step.key} className="relative z-10 flex flex-col items-center gap-1.5">
              <div
                className={cn(
                  "w-10 h-10 rounded-full flex items-center justify-center transition-all duration-300 font-bold shadow-sm",
                  isPassed
                    ? "bg-amber-700 text-white"
                    : isCurrent
                    ? "bg-amber-600 text-white ring-4 ring-amber-200 animate-pulse scale-110"
                    : "bg-white border-2 border-slate-300 text-slate-400"
                )}
              >
                {isPassed ? <Check className="h-5 w-5" /> : <StepIcon className="h-5 w-5" />}
              </div>
              <span
                className={cn(
                  "text-[11px] font-medium text-center",
                  isCurrent ? "font-bold text-amber-900" : isPassed ? "text-slate-700" : "text-slate-400"
                )}
              >
                {step.label}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
