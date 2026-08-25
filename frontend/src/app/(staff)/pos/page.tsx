"use client";

import Link from "next/link";
import { ArrowLeft, Search, Award, CreditCard, Banknote } from "lucide-react";
import { useState } from "react";
import { usePosStore } from "@/stores/usePosStore";
import { formatCurrencyVND } from "@/lib/utils";

export default function StaffPosPage() {
  const { currentCustomer, setCustomer, cartItems, addItem, resetPos, getNetTotal } = usePosStore();
  const [phoneInput, setPhoneInput] = useState("");

  const handleLookup = () => {
    if (!phoneInput.trim()) return;
    setCustomer({
      customerId: "cust-01",
      phone: phoneInput,
      fullName: "Khách Thân Thiết",
      cupBalance: 9,
      eligibleForFreeCup: false,
    });
  };

  const handleAddProduct = (prod: { id: string; name: string; price: number }) => {
    addItem({
      cartItemId: `${prod.id}-m-100-100`,
      productId: prod.id,
      productName: prod.name,
      sizeId: "size-m",
      sizeName: "M",
      unitPrice: prod.price,
      quantity: 1,
      sugarLevel: "100%",
      iceLevel: "100%",
      toppings: [],
      totalItemPrice: prod.price,
    });
  };

  return (
    <div className="min-h-screen bg-slate-100 text-slate-800 flex flex-col">
      <header className="bg-white border-b border-slate-200 px-6 py-3 flex items-center justify-between shadow-sm">
        <div className="flex items-center gap-3">
          <Link href="/" className="p-2 rounded-lg hover:bg-slate-100 text-slate-600">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-base font-bold text-slate-900">Web POS Quầy — Bán Hàng Mang Về (Takeaway)</h1>
            <p className="text-xs text-slate-500">Chi nhánh 01 • Thu ngân: Lê Văn B (NV-002)</p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <input
            type="tel"
            value={phoneInput}
            onChange={(e) => setPhoneInput(e.target.value)}
            placeholder="Nhập SĐT khách hàng CRM..."
            className="pl-3 pr-3 py-1.5 text-xs rounded-lg border border-slate-300 w-56 focus:outline-none focus:ring-2 focus:ring-orange-500 font-mono"
          />
          <button
            onClick={handleLookup}
            className="px-3 py-1.5 rounded-lg bg-orange-500 text-white text-xs font-semibold hover:bg-orange-600"
          >
            Tra cứu
          </button>
        </div>
      </header>

      <div className="flex-1 grid grid-cols-1 md:grid-cols-3 gap-4 p-4">
        {/* Menu Grid */}
        <div className="md:col-span-2 bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-4">
          <h2 className="text-sm font-bold text-slate-900">Danh Mục Món Quầy</h2>
          <div className="grid grid-cols-3 gap-3">
            {[
              { id: "1", name: "Cà Phê Sữa Đá", price: 29000 },
              { id: "2", name: "Bạc Xỉu Sữa Tươi", price: 32000 },
              { id: "3", name: "Trà Vải Hoa Hồng", price: 45000 },
              { id: "4", name: "Cà Phê Muối", price: 35000 },
              { id: "5", name: "Trà Đào Cam Sả", price: 42000 },
              { id: "6", name: "Trà Sữa Oolong", price: 39000 },
            ].map((m) => (
              <button
                key={m.id}
                onClick={() => handleAddProduct(m)}
                className="p-3 text-left rounded-xl border border-slate-200 hover:border-orange-500 hover:bg-orange-50/30 transition-all shadow-sm space-y-1"
              >
                <div className="text-xs font-bold text-slate-900">{m.name}</div>
                <div className="text-xs font-extrabold text-orange-600">{m.price.toLocaleString("vi-VN")}đ</div>
              </button>
            ))}
          </div>
        </div>

        {/* Current Order & Loyalty Panel */}
        <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm flex flex-col justify-between space-y-4">
          <div className="space-y-3">
            <h2 className="text-sm font-bold text-slate-900 pb-2 border-b border-slate-200">
              Đơn Hiện Tại (Takeaway)
            </h2>

            {currentCustomer && (
              <div className="p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-xs space-y-1">
                <div className="font-bold flex items-center gap-1.5 text-amber-800">
                  <Award className="w-4 h-4 text-amber-600" />
                  Khách: {currentCustomer.fullName} ({currentCustomer.phone})
                </div>
                <p className="text-[11px] text-amber-700">
                  Đã tích lũy: <strong className="font-bold text-amber-900">{currentCustomer.cupBalance} / 10 ly</strong> (Chỉ áp dụng Takeaway).
                </p>
              </div>
            )}

            <div className="space-y-1 max-h-48 overflow-y-auto">
              {cartItems.map((item, idx) => (
                <div key={idx} className="flex justify-between text-xs py-1 border-b border-slate-100">
                  <span>{item.quantity}x {item.productName}</span>
                  <span className="font-bold">{formatCurrencyVND(item.totalItemPrice)}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="pt-4 border-t border-slate-200 space-y-2">
            <div className="flex justify-between items-center text-sm font-bold">
              <span>Tổng Tiền:</span>
              <span className="text-lg text-orange-600">{formatCurrencyVND(getNetTotal())}</span>
            </div>

            <div className="grid grid-cols-2 gap-2">
              <button
                onClick={resetPos}
                className="py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs flex items-center justify-center gap-1"
              >
                <Banknote className="w-4 h-4" /> Tiền Mặt
              </button>
              <button
                onClick={resetPos}
                className="py-2.5 rounded-xl bg-orange-500 hover:bg-orange-600 text-white font-bold text-xs flex items-center justify-center gap-1"
              >
                <CreditCard className="w-4 h-4" /> VietQR Quầy
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
