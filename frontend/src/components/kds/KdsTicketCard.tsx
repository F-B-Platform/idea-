import React from "react";
import { KdsTicketDto } from "@/types";
import { calculateSlaStatus } from "@/lib/utils";
import { Clock, Beaker, Check, Play, MapPin, AlertCircle } from "lucide-react";
import { cn } from "@/lib/utils";

export interface KdsTicketCardProps {
  ticket: KdsTicketDto;
  onUpdateStatus: (orderId: string, status: "Preparing" | "Ready") => void;
  onViewBom: (ticket: KdsTicketDto) => void;
}

export const KdsTicketCard: React.FC<KdsTicketCardProps> = ({
  ticket,
  onUpdateStatus,
  onViewBom,
}) => {
  const sla = calculateSlaStatus(ticket.elapsedSeconds);

  const getOrderTypeBadge = () => {
    switch (ticket.orderType) {
      case "DineIn":
        return (
          <span className="bg-amber-500/20 text-amber-300 border border-amber-500/40 text-[11px] px-2 py-0.5 rounded font-bold">
            BÀN {ticket.tableNumber || "01"}
          </span>
        );
      case "TakeAway":
        return (
          <span className="bg-sky-500/20 text-sky-300 border border-sky-500/40 text-[11px] px-2 py-0.5 rounded font-bold">
            MANG VỀ
          </span>
        );
      case "Delivery":
        return (
          <span className="bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 text-[11px] px-2 py-0.5 rounded font-bold">
            GIAO HÀNG
          </span>
        );
    }
  };

  const getPaymentBadge = () => {
    if (ticket.paymentStatus === "Paid" || ticket.paymentStatus === "Success") {
      return (
        <span className="text-[10px] text-emerald-400 font-semibold bg-emerald-950/60 px-1.5 py-0.5 rounded border border-emerald-800">
          ĐÃ TT
        </span>
      );
    }
    return (
      <span className="text-[10px] text-amber-400 font-semibold bg-amber-950/60 px-1.5 py-0.5 rounded border border-amber-800">
        TRẢ SAU
      </span>
    );
  };

  return (
    <div
      className={cn(
        "bg-slate-800/90 text-slate-100 rounded-2xl p-4 border-2 transition-all flex flex-col justify-between shadow-xl min-w-[290px] max-w-[340px] select-none",
        sla.cardBorderClass
      )}
    >
      {/* Header */}
      <div className="space-y-2 border-b border-slate-700/80 pb-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="font-extrabold text-lg tracking-wide text-white">
              #{ticket.orderNumber || ticket.orderCode}
            </span>
            {getOrderTypeBadge()}
          </div>
          {getPaymentBadge()}
        </div>

        {/* SLA Timer Bar */}
        <div className="flex items-center justify-between">
          <div className={cn("inline-flex items-center gap-1.5 text-xs px-2.5 py-1 rounded-lg font-bold", sla.badgeClass)}>
            <Clock className="h-3.5 w-3.5" />
            <span>{sla.label}</span>
          </div>

          <button
            type="button"
            onClick={() => onViewBom(ticket)}
            className="inline-flex items-center gap-1 text-[11px] font-medium text-slate-400 hover:text-amber-300 bg-slate-700/50 hover:bg-slate-700 px-2 py-1 rounded-lg transition-colors border border-slate-600/50"
          >
            <Beaker className="h-3.5 w-3.5" />
            <span>Xem BOM</span>
          </button>
        </div>
      </div>

      {/* Items List */}
      <div className="py-3 space-y-3 flex-1 overflow-y-auto max-h-[300px] divide-y divide-slate-700/40">
        {ticket.items.map((item, idx) => (
          <div key={idx} className="pt-2 first:pt-0 space-y-1">
            <div className="flex items-start justify-between gap-2">
              <div className="flex items-baseline gap-1.5">
                <span className="font-extrabold text-base text-amber-400 bg-amber-950/60 border border-amber-800/60 px-1.5 py-0.5 rounded">
                  {item.quantity}x
                </span>
                <span className="font-bold text-sm text-white">{item.productName}</span>
              </div>
              <span className="text-xs font-semibold text-slate-300 bg-slate-700 px-1.5 py-0.5 rounded">
                Size {item.sizeName}
              </span>
            </div>

            {/* Modifiers / Specs */}
            <div className="pl-6 text-[11px] text-slate-300 space-y-0.5">
              {(item.sugarLevel || item.iceLevel) && (
                <div className="flex gap-2 text-slate-400 font-medium">
                  <span>Đường: <strong className="text-slate-200">{item.sugarLevel}</strong></span>
                  <span>•</span>
                  <span>Đá: <strong className="text-slate-200">{item.iceLevel}</strong></span>
                </div>
              )}
              {item.toppings && item.toppings.length > 0 && (
                <div className="text-amber-300/90 font-medium">
                  + {item.toppings.join(", ")}
                </div>
              )}
              {item.notes && (
                <div className="text-rose-300 font-medium italic bg-rose-950/30 p-1 rounded border border-rose-900/40 flex items-center gap-1">
                  <AlertCircle className="h-3 w-3 shrink-0" />
                  <span>{item.notes}</span>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Footer Action Buttons */}
      <div className="pt-3 border-t border-slate-700/80 grid grid-cols-2 gap-2">
        {ticket.status === "Pending" ? (
          <button
            type="button"
            onClick={() => onUpdateStatus(ticket.orderId, "Preparing")}
            className="col-span-2 py-3 bg-amber-600 hover:bg-amber-500 text-white font-bold text-sm rounded-xl shadow-lg flex items-center justify-center gap-2 active:scale-95 transition-all min-h-[48px]"
          >
            <Play className="h-4 w-4 fill-current" />
            <span>BẮT ĐẦU PHA CHẾ</span>
          </button>
        ) : (
          <>
            <button
              type="button"
              disabled
              className="py-2.5 bg-slate-700/50 text-amber-400 border border-amber-500/30 font-bold text-xs rounded-xl flex items-center justify-center gap-1.5"
            >
              <span className="w-2 h-2 rounded-full bg-amber-400 animate-ping" />
              <span>Đang Làm</span>
            </button>
            <button
              type="button"
              onClick={() => onUpdateStatus(ticket.orderId, "Ready")}
              className="py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs rounded-xl shadow-lg flex items-center justify-center gap-1.5 active:scale-95 transition-all min-h-[48px]"
            >
              <Check className="h-4 w-4" />
              <span>HOÀN TẤT</span>
            </button>
          </>
        )}
      </div>
    </div>
  );
};
