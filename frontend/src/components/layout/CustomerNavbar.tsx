"use client";

import React from "react";
import Link from "next/link";
import { useCartStore } from "@/stores/useCartStore";
import { ShoppingBag, Coffee, Sparkles, History, MapPin } from "lucide-react";
import { formatCurrencyVND } from "@/lib/utils";

export interface CustomerNavbarProps {
  tableNumber?: string;
  branchName?: string;
}

export const CustomerNavbar: React.FC<CustomerNavbarProps> = ({
  tableNumber,
  branchName = "Smart F&B Coffee & Tea",
}) => {
  const itemsCount = useCartStore((state) => state.getTotalItemsCount());
  const totalAmount = useCartStore((state) => state.getTotalAmount());
  const currentTableNumber = useCartStore((state) => state.tableNumber) || tableNumber;

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-xs">
      <div className="max-w-md mx-auto px-4 h-16 flex items-center justify-between">
        {/* Brand Logo & Table Identification */}
        <Link href="/menu" className="flex items-center gap-2.5">
          <div className="w-10 h-10 rounded-xl bg-amber-700 text-white flex items-center justify-center shadow-sm">
            <Coffee className="h-5 w-5" />
          </div>
          <div>
            <span className="font-black text-sm text-slate-900 tracking-tight block leading-tight">
              SMART F&B
            </span>
            <div className="flex items-center gap-1 text-[11px] text-amber-800 font-semibold">
              <MapPin className="h-3 w-3 shrink-0" />
              <span>{currentTableNumber ? `Bàn #${currentTableNumber}` : "Đặt Giao Tận Nơi"}</span>
            </div>
          </div>
        </Link>

        {/* Quick Links & Cart Badge Button */}
        <div className="flex items-center gap-2">
          <Link
            href="/ai-chat"
            className="p-2 rounded-xl text-amber-800 bg-amber-50 hover:bg-amber-100 transition-colors"
            title="Chatbot AI-1 Gợi Ý Món"
          >
            <Sparkles className="h-5 w-5" />
          </Link>

          <Link
            href="/history"
            className="p-2 rounded-xl text-slate-600 hover:bg-slate-100 transition-colors"
            title="Lịch Sử Đơn Hàng"
          >
            <History className="h-5 w-5" />
          </Link>

          <Link
            href="/cart"
            className="relative flex items-center gap-2 pl-3 pr-4 py-2 rounded-xl bg-amber-700 text-white font-bold text-xs shadow-sm hover:bg-amber-800 transition-colors active:scale-95"
          >
            <ShoppingBag className="h-4 w-4" />
            <span>{itemsCount > 0 ? formatCurrencyVND(totalAmount) : "Giỏ Hàng"}</span>
            {itemsCount > 0 && (
              <span className="absolute -top-1.5 -right-1.5 w-5 h-5 bg-rose-500 text-white rounded-full flex items-center justify-center text-[10px] font-black border-2 border-white shadow-sm animate-bounce">
                {itemsCount}
              </span>
            )}
          </Link>
        </div>
      </div>
    </header>
  );
};
