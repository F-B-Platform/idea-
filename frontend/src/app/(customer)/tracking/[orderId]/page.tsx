"use client";

import Link from "next/link";
import { ArrowLeft, Clock, CheckCircle2, Coffee, Star } from "lucide-react";

export default function OrderTrackingPage({ params }: { params: { orderId: string } }) {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 max-w-md mx-auto space-y-4">
      <header className="flex items-center gap-2 py-2 border-b border-slate-200">
        <Link href="/menu" className="p-2 rounded-full hover:bg-slate-200 text-slate-600">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="text-base font-bold text-slate-900">Theo Dõi Đơn Hàng</h1>
          <p className="text-xs text-slate-500 font-mono">Mã Đơn: #{params.orderId}</p>
        </div>
      </header>

      <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-4">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-orange-100 text-orange-600 flex items-center justify-center">
            <Coffee className="w-5 h-5" />
          </div>
          <div>
            <div className="text-sm font-bold text-slate-900">Đang Pha Chế (Preparing)</div>
            <p className="text-xs text-slate-500">Barista đang chuẩn bị đồ uống cho bạn</p>
          </div>
        </div>

        {/* Live Stepper */}
        <div className="space-y-3 pt-2 text-xs">
          <div className="flex items-center gap-2 text-emerald-600 font-semibold">
            <CheckCircle2 className="w-4 h-4" /> 1. Tiếp nhận đơn hàng (Đã thanh toán)
          </div>
          <div className="flex items-center gap-2 text-orange-600 font-bold">
            <Clock className="w-4 h-4 animate-spin" /> 2. Barista đang pha chế món
          </div>
          <div className="flex items-center gap-2 text-slate-400">
            <div className="w-4 h-4 rounded-full border border-slate-300"></div> 3. Đã sẵn sàng phục vụ
          </div>
        </div>

        <div className="pt-4 border-t border-slate-100">
          <Link
            href={`/review/${params.orderId}`}
            className="flex items-center justify-center gap-1.5 py-2.5 rounded-xl bg-amber-50 text-amber-800 text-xs font-bold border border-amber-200 hover:bg-amber-100"
          >
            <Star className="w-4 h-4 text-amber-500 fill-amber-500" /> Đánh Giá Trải Nghiệm Món
          </Link>
        </div>
      </div>
    </div>
  );
}
