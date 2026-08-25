"use client";

import Link from "next/link";
import { ArrowLeft, MapPin, ShieldCheck, Truck } from "lucide-react";
import { useState } from "react";
import { useCartStore } from "@/stores/useCartStore";

export default function CustomerDeliveryPage() {
  const { setDeliveryInfo } = useCartStore();
  const [phone, setPhone] = useState("");
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");

  const handleSave = () => {
    if (!phone || !address) return;
    setDeliveryInfo({
      recipientName: name || "Khách Hàng",
      recipientPhone: phone,
      deliveryAddress: address,
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 pb-20">
      <header className="sticky top-0 z-20 bg-white/90 backdrop-blur border-b border-slate-200 px-4 py-3 flex items-center gap-2 shadow-sm">
        <Link href="/" className="p-2 rounded-full hover:bg-slate-100 text-slate-600">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="text-base font-bold text-slate-900">QR Delivery — Giao Tận Nơi</h1>
          <p className="text-xs text-slate-500">Phí ship cố định: 20.000 VNĐ • 100% VietQR Trả Trước</p>
        </div>
      </header>

      <main className="max-w-md mx-auto p-4 space-y-4">
        <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
          <h2 className="text-sm font-bold text-slate-900 flex items-center gap-2">
            <MapPin className="w-4 h-4 text-emerald-600" />
            Thông Tin Giao Hàng Bắt Buộc
          </h2>

          <div className="space-y-3">
            <div>
              <label className="text-xs font-semibold text-slate-600">Họ và Tên</label>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Ví dụ: Nguyễn Văn A"
                className="w-full mt-1 px-3 py-2 text-xs rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500"
              />
            </div>
            <div>
              <label className="text-xs font-semibold text-slate-600">Số Điện Thoại Nhận Hàng (*)</label>
              <input
                type="tel"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                placeholder="Ví dụ: 0901234567"
                className="w-full mt-1 px-3 py-2 text-xs rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500 font-mono"
              />
            </div>
            <div>
              <label className="text-xs font-semibold text-slate-600">Địa Chỉ Giao Hàng Chi Tiết (*)</label>
              <textarea
                rows={2}
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                placeholder="Số nhà, tên đường, toà nhà, phòng..."
                className="w-full mt-1 px-3 py-2 text-xs rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500"
              />
            </div>
          </div>

          <div className="p-2.5 rounded-lg bg-emerald-50 text-emerald-800 text-xs flex items-center gap-2 border border-emerald-100">
            <ShieldCheck className="w-4 h-4 flex-shrink-0 text-emerald-600" />
            <span>Khóa hoàn toàn COD: Đơn chỉ được xác nhận sau khi quét mã VietQR thành công.</span>
          </div>

          <Link
            href="/menu"
            onClick={handleSave}
            className="block w-full py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs text-center shadow"
          >
            Lưu Thông Tin & Chọn Món &rarr;
          </Link>
        </div>
      </main>
    </div>
  );
}
