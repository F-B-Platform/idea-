"use client";

import Link from "next/link";
import { ArrowLeft, QrCode, ShieldCheck, CheckCircle } from "lucide-react";

export default function VietQrCheckoutPage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 max-w-md mx-auto space-y-4">
      <header className="flex items-center gap-2 py-2 border-b border-slate-200">
        <Link href="/cart" className="p-2 rounded-full hover:bg-slate-200 text-slate-600">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <h1 className="text-base font-bold text-slate-900">Thanh Toán VietQR PayOS</h1>
      </header>

      <div className="p-6 bg-white rounded-2xl border border-slate-200 shadow-sm text-center space-y-4">
        <div className="inline-flex p-3 rounded-2xl bg-orange-50 text-orange-600">
          <QrCode className="w-12 h-12" />
        </div>
        <div>
          <h2 className="text-lg font-bold text-slate-900">Quét Mã VietQR</h2>
          <p className="text-xs text-slate-500">Mở ứng dụng ngân hàng hoặc ví điện tử để thanh toán</p>
        </div>

        <div className="w-48 h-48 bg-slate-100 border-2 border-dashed border-slate-300 rounded-xl mx-auto flex items-center justify-center text-xs text-slate-400 font-mono">
          [VietQR Image Placeholder]
        </div>

        <div className="p-3 rounded-xl bg-emerald-50 text-emerald-800 text-xs flex items-center gap-2 border border-emerald-100">
          <ShieldCheck className="w-4 h-4 flex-shrink-0 text-emerald-600" />
          <span>Webhook PayOS tự động xác nhận sau 1-2 giây khi chuyển khoản thành công.</span>
        </div>

        <Link
          href="/tracking/sample-order-id"
          className="block w-full py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow"
        >
          Giả lập thanh toán thành công &rarr;
        </Link>
      </div>
    </div>
  );
}
