"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { useCartStore } from "@/stores/useCartStore";
import { formatCurrencyVND } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import {
  Trash2,
  Plus,
  Minus,
  ArrowLeft,
  QrCode,
  Banknote,
  Tag,
  CheckCircle2,
  ShoppingBag,
} from "lucide-react";

export default function CartPage() {
  const router = useRouter();
  const {
    items,
    updateItemQuantity,
    removeItem,
    orderType,
    tableNumber,
    paymentMethod,
    setPaymentMethod,
    voucherCode,
    discountAmount,
    applyVoucher,
    removeVoucher,
    getSubtotal,
    getTotalAmount,
    deliveryFee,
    clearCart,
  } = useCartStore();

  const [inputVoucher, setInputVoucher] = useState("");
  const [voucherError, setVoucherError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const subtotal = getSubtotal();
  const total = getTotalAmount();

  const handleApplyVoucher = () => {
    setVoucherError(null);
    const code = inputVoucher.trim().toUpperCase();
    if (!code) return;

    if (code === "DISCOUNT10" || code === "SMARTFB10") {
      applyVoucher(code, 15000);
      setInputVoucher("");
    } else if (code === "VIP20") {
      applyVoucher(code, 25000);
      setInputVoucher("");
    } else {
      setVoucherError("Mã giảm giá không tồn tại hoặc đã hết hạn");
    }
  };

  const handleCheckout = () => {
    if (items.length === 0) return;
    setIsSubmitting(true);

    const generatedOrderId = `ORD-${Math.floor(1000 + Math.random() * 9000)}`;

    setTimeout(() => {
      setIsSubmitting(false);
      if (paymentMethod === "VIETQR") {
        router.push(`/checkout/vietqr?orderId=${generatedOrderId}&amount=${total}`);
      } else {
        // Cash Postpaid: goes straight to tracking & sends to KDS
        router.push(`/tracking/${generatedOrderId}?type=postpaid`);
      }
    }, 600);
  };

  if (items.length === 0) {
    return (
      <div className="px-4 py-16 text-center space-y-4">
        <div className="w-20 h-20 bg-amber-100 text-amber-700 rounded-full flex items-center justify-center mx-auto">
          <ShoppingBag className="h-10 w-10" />
        </div>
        <h3 className="text-lg font-bold text-slate-900">Giỏ hàng đang trống</h3>
        <p className="text-xs text-slate-500 max-w-xs mx-auto">
          Quý khách chưa thêm món nào vào giỏ hàng. Vui lòng quay lại thực đơn để chọn món.
        </p>
        <Button
          onClick={() => router.push(tableNumber ? `/table/${tableNumber}` : "/menu")}
          variant="primary"
          className="mt-2"
        >
          Xem Thực Đơn
        </Button>
      </div>
    );
  }

  return (
    <div className="space-y-6 px-4 pt-4 pb-12">
      {/* Top Header */}
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={() => router.back()}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Tiếp tục chọn món</span>
        </button>
        <span className="text-xs font-bold text-amber-800 bg-amber-100 px-3 py-1 rounded-full">
          {tableNumber ? `Bàn #${tableNumber}` : "Giao hàng"}
        </span>
      </div>

      <h2 className="text-xl font-black text-slate-950">Giỏ Hàng Của Bạn</h2>

      {/* Cart Items List */}
      <div className="space-y-3">
        {items.map((item) => (
          <div
            key={item.cartItemId}
            className="p-4 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-3"
          >
            <div className="flex items-start justify-between gap-3">
              <div>
                <h4 className="font-bold text-sm text-slate-900">{item.productName}</h4>
                <div className="text-xs text-slate-500 space-y-0.5 mt-0.5">
                  <span className="font-semibold text-amber-800">Size {item.sizeName}</span>
                  {(item.sugarLevel || item.iceLevel) && (
                    <span> • Đ: {item.sugarLevel} • Đá: {item.iceLevel}</span>
                  )}
                  {item.toppings.length > 0 && (
                    <p className="text-[11px] text-slate-600">
                      + Topping: {item.toppings.map((t) => t.name).join(", ")}
                    </p>
                  )}
                  {item.notes && (
                    <p className="text-[11px] text-amber-800 italic">Ghi chú: {item.notes}</p>
                  )}
                </div>
              </div>

              <span className="font-extrabold text-sm text-amber-900 shrink-0">
                {formatCurrencyVND(item.totalItemPrice)}
              </span>
            </div>

            {/* Quantity controls & Delete */}
            <div className="flex items-center justify-between pt-2 border-t border-slate-100">
              <button
                type="button"
                onClick={() => removeItem(item.cartItemId)}
                className="text-xs text-rose-600 hover:text-rose-700 flex items-center gap-1 font-medium p-1"
              >
                <Trash2 className="h-3.5 w-3.5" />
                <span>Xóa</span>
              </button>

              <div className="flex items-center gap-2 bg-slate-100 p-1 rounded-xl">
                <button
                  type="button"
                  onClick={() => updateItemQuantity(item.cartItemId, -1)}
                  className="w-7 h-7 bg-white rounded-lg flex items-center justify-center text-slate-700 shadow-2xs"
                >
                  <Minus className="h-3 w-3" />
                </button>
                <span className="font-bold text-xs w-5 text-center text-slate-900">
                  {item.quantity}
                </span>
                <button
                  type="button"
                  onClick={() => updateItemQuantity(item.cartItemId, 1)}
                  className="w-7 h-7 bg-white rounded-lg flex items-center justify-center text-slate-700 shadow-2xs"
                >
                  <Plus className="h-3 w-3" />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Voucher Code Box */}
      <div className="p-4 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-2">
        <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
          Mã Khuyến Mãi / Voucher
        </label>
        {voucherCode ? (
          <div className="flex items-center justify-between bg-emerald-50 border border-emerald-200 p-3 rounded-xl">
            <div className="flex items-center gap-2 text-emerald-900 text-xs font-bold">
              <CheckCircle2 className="h-4 w-4 text-emerald-600" />
              <span>
                Áp dụng mã <strong>{voucherCode}</strong> (-{formatCurrencyVND(discountAmount)})
              </span>
            </div>
            <button
              type="button"
              onClick={removeVoucher}
              className="text-xs text-rose-600 font-bold hover:underline"
            >
              Hủy
            </button>
          </div>
        ) : (
          <div className="flex gap-2">
            <input
              type="text"
              value={inputVoucher}
              onChange={(e) => setInputVoucher(e.target.value)}
              placeholder="Nhập mã (DISCOUNT10, VIP20)..."
              className="flex-1 px-3 py-2 text-xs rounded-xl border border-slate-300 uppercase font-semibold focus:outline-none focus:ring-2 focus:ring-amber-600"
            />
            <Button type="button" size="sm" variant="secondary" onClick={handleApplyVoucher}>
              Áp Dụng
            </Button>
          </div>
        )}
        {voucherError && <p className="text-xs text-rose-600">{voucherError}</p>}
      </div>

      {/* 2-Branch Dine-In Payment Method Selection */}
      <div className="p-4 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-3">
        <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
          Chọn Hình Thức Thanh Toán
        </label>

        <div className="space-y-2">
          {/* Branch A: VietQR Prepaid */}
          <div
            onClick={() => setPaymentMethod("VIETQR")}
            className={`p-3.5 rounded-xl border-2 flex items-center justify-between cursor-pointer transition-all ${
              paymentMethod === "VIETQR"
                ? "border-amber-700 bg-amber-50/60 shadow-sm"
                : "border-slate-200 hover:border-slate-300"
            }`}
          >
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-xl bg-amber-700 text-white flex items-center justify-center">
                <QrCode className="h-5 w-5" />
              </div>
              <div>
                <span className="font-bold text-xs text-slate-900 block">
                  Nhánh A: VIETQR TRẢ TRƯỚC (Prepaid)
                </span>
                <span className="text-[11px] text-slate-500">
                  Quét mã QR PayOS thanh toán xong ➔ Bếp KDS nhận đơn ngay
                </span>
              </div>
            </div>
            <input
              type="radio"
              checked={paymentMethod === "VIETQR"}
              onChange={() => setPaymentMethod("VIETQR")}
              className="text-amber-700 accent-amber-700"
            />
          </div>

          {/* Branch B: Cash Postpaid (Disabled if Delivery) */}
          {orderType !== "Delivery" && (
            <div
              onClick={() => setPaymentMethod("CASH")}
              className={`p-3.5 rounded-xl border-2 flex items-center justify-between cursor-pointer transition-all ${
                paymentMethod === "CASH"
                  ? "border-amber-700 bg-amber-50/60 shadow-sm"
                  : "border-slate-200 hover:border-slate-300"
              }`}
            >
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 rounded-xl bg-slate-700 text-white flex items-center justify-center">
                  <Banknote className="h-5 w-5" />
                </div>
                <div>
                  <span className="font-bold text-xs text-slate-900 block">
                    Nhánh B: TIỀN MẶT TRẢ SAU (Postpaid)
                  </span>
                  <span className="text-[11px] text-slate-500">
                    Đơn gửi thẳng xuống Bếp ngay ➔ Nhân viên mang đồ & in bill thu sau
                  </span>
                </div>
              </div>
              <input
                type="radio"
                checked={paymentMethod === "CASH"}
                onChange={() => setPaymentMethod("CASH")}
                className="text-amber-700 accent-amber-700"
              />
            </div>
          )}
        </div>
      </div>

      {/* Cost Summary Box */}
      <div className="p-4 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-2 text-xs">
        <div className="flex justify-between text-slate-600">
          <span>Tạm tính ({items.length} món):</span>
          <span className="font-semibold text-slate-900">{formatCurrencyVND(subtotal)}</span>
        </div>
        {discountAmount > 0 && (
          <div className="flex justify-between text-rose-600 font-semibold">
            <span>Giảm giá voucher:</span>
            <span>-{formatCurrencyVND(discountAmount)}</span>
          </div>
        )}
        {deliveryFee > 0 && (
          <div className="flex justify-between text-slate-600">
            <span>Phí giao hàng cố định:</span>
            <span className="font-semibold text-slate-900">{formatCurrencyVND(deliveryFee)}</span>
          </div>
        )}
        <div className="flex justify-between font-black text-base pt-2 border-t border-slate-100 text-slate-900">
          <span>Tổng thanh toán:</span>
          <span className="text-amber-900">{formatCurrencyVND(total)}</span>
        </div>
      </div>

      {/* Submit Order Button */}
      <Button
        type="button"
        onClick={handleCheckout}
        isLoading={isSubmitting}
        size="lg"
        variant="primary"
        className="w-full font-bold shadow-md text-base"
      >
        {paymentMethod === "VIETQR" ? "Tiếp Tục Thanh Toán VietQR" : "Xác Nhận Đặt Đơn (Trả Sau)"}
      </Button>
    </div>
  );
}
