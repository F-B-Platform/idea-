"use client";

import Link from "next/link";
import { ShoppingBag, ArrowLeft } from "lucide-react";
import { useCartStore } from "@/stores/useCartStore";

export default function CustomerMenuPage() {
  const { items, addItem, orderType } = useCartStore();

  const handleQuickAdd = (product: { id: string; name: string; price: number }) => {
    addItem({
      productId: product.id,
      productName: product.name,
      sizeId: "size-m",
      sizeName: "M",
      unitPrice: product.price,
      quantity: 1,
      sugarLevel: "100%",
      iceLevel: "100%",
      toppings: [],
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 pb-20">
      <header className="sticky top-0 z-20 bg-white/90 backdrop-blur border-b border-slate-200 px-4 py-3 flex items-center justify-between shadow-sm">
        <div className="flex items-center gap-2">
          <Link href="/" className="p-2 rounded-full hover:bg-slate-100 text-slate-600">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-base font-bold text-slate-900">Smart Coffee</h1>
            <p className="text-xs text-slate-500">
              {orderType === "Delivery" ? "Kênh Giao Hàng (Ship 20k)" : "Kênh Gọi Món Tại Bàn (Dine-in)"}
            </p>
          </div>
        </div>
        <Link href="/cart" className="relative p-2 rounded-full bg-orange-50 text-orange-600">
          <ShoppingBag className="w-5 h-5" />
          {items.length > 0 && (
            <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-orange-500 text-white text-[10px] font-bold flex items-center justify-center">
              {items.reduce((s, i) => s + i.quantity, 0)}
            </span>
          )}
        </Link>
      </header>

      <main className="max-w-md mx-auto p-4 space-y-4">
        <div className="p-4 rounded-2xl bg-gradient-to-br from-orange-500 to-amber-600 text-white shadow-lg space-y-1">
          <span className="text-xs uppercase tracking-wider font-semibold opacity-90">Thực Đơn Đồ Uống</span>
          <h2 className="text-xl font-bold">Menu Quán Cà Phê</h2>
          <p className="text-xs text-orange-100">
            VietQR trả trước hoặc Tiền mặt trả sau kèm Bill QR.
          </p>
        </div>

        <div className="space-y-3">
          {[
            { id: "1", name: "Cà Phê Muối Hoàng Gia", price: 35000, desc: "Cà phê Robusta pha phin kết hợp lớp kem muối béo ngậy." },
            { id: "2", name: "Trà Đào Cam Sả Tươi", price: 42000, desc: "Trà đen ủ lạnh với đào miếng giòn ngọt và sả thơm ngát." },
            { id: "3", name: "Trà Sữa Oolong Nướng", price: 39000, desc: "Trà Oolong nướng đậm vị, sữa tươi thanh trùng ngọt dịu." },
          ].map((item) => (
            <div key={item.id} className="p-3 bg-white rounded-xl border border-slate-200 shadow-sm flex items-center justify-between gap-3">
              <div className="space-y-1 flex-1">
                <h3 className="text-sm font-bold text-slate-900">{item.name}</h3>
                <p className="text-xs text-slate-500 line-clamp-1">{item.desc}</p>
                <div className="text-sm font-extrabold text-orange-600">{item.price.toLocaleString("vi-VN")}đ</div>
              </div>
              <button
                onClick={() => handleQuickAdd(item)}
                className="px-3 py-1.5 rounded-lg bg-orange-500 hover:bg-orange-600 text-white text-xs font-semibold shadow-sm"
              >
                + Thêm
              </button>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
