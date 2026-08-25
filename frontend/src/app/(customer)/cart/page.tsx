"use client";

import Link from "next/link";
import { ShoppingBag, ArrowLeft, Trash2 } from "lucide-react";
import { useCartStore } from "@/stores/useCartStore";
import { formatCurrencyVND } from "@/lib/utils";

export default function CartPage() {
  const { items, clearCart, getTotalAmount } = useCartStore();

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 max-w-md mx-auto space-y-4">
      <header className="flex items-center justify-between py-2 border-b border-slate-200">
        <div className="flex items-center gap-2">
          <Link href="/menu" className="p-2 rounded-full hover:bg-slate-200 text-slate-600">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <h1 className="text-base font-bold text-slate-900">Giỏ Hàng Của Bạn</h1>
        </div>
        {items.length > 0 && (
          <button onClick={clearCart} className="text-xs text-rose-600 hover:underline flex items-center gap-1">
            <Trash2 className="w-3.5 h-3.5" /> Xóa hết
          </button>
        )}
      </header>

      {items.length === 0 ? (
        <div className="text-center py-16 space-y-3">
          <div className="w-16 h-16 rounded-full bg-orange-100 text-orange-600 flex items-center justify-center mx-auto">
            <ShoppingBag className="w-8 h-8" />
          </div>
          <p className="text-sm font-semibold text-slate-600">Giỏ hàng của bạn đang trống</p>
          <Link href="/menu" className="inline-block px-4 py-2 rounded-xl bg-orange-500 text-white text-xs font-bold shadow">
            Xem Thực Đơn Ngay
          </Link>
        </div>
      ) : (
        <div className="space-y-4">
          <div className="space-y-2">
            {items.map((item, idx) => (
              <div key={idx} className="p-3 bg-white rounded-xl border border-slate-200 shadow-sm flex justify-between">
                <div>
                  <h3 className="text-sm font-bold">{item.productName}</h3>
                  <p className="text-xs text-slate-500">Size {item.sizeName} • SL: {item.quantity}</p>
                </div>
                <div className="text-sm font-bold text-orange-600">{formatCurrencyVND(item.totalItemPrice)}</div>
              </div>
            ))}
          </div>

          <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-sm space-y-2">
            <div className="flex justify-between font-bold text-base">
              <span>Tổng thanh toán:</span>
              <span className="text-orange-600">{formatCurrencyVND(getTotalAmount())}</span>
            </div>
            <Link
              href="/checkout/vietqr"
              className="block w-full text-center py-3 rounded-xl bg-orange-500 hover:bg-orange-600 text-white font-bold text-sm shadow"
            >
              Tiến Hành Thanh Toán
            </Link>
          </div>
        </div>
      )}
    </div>
  );
}
