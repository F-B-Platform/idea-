"use client";

import React from "react";
import { formatCurrencyVND } from "@/lib/utils";
import {
  TrendingUp,
  DollarSign,
  QrCode,
  Banknote,
  Clock,
  AlertTriangle,
  ShoppingBag,
  Users,
  Store,
} from "lucide-react";

export default function BranchDashboardPage() {
  const kpiData = {
    todayRevenue: 14850000,
    ordersCount: 186,
    vietQrRatio: 68.5, // 68.5% VietQR vs 31.5% Cash
    kdsSlaCompliance: 96.2, // 96.2% orders completed under 5 mins
    lowStockIngredients: [
      { name: "Cốt Cà Phê Robusta Đắk Lắk", current: "1.2 kg", threshold: "3.0 kg" },
      { name: "Sữa Tươi Thanh Trùng Barista", current: "4 Hộp", threshold: "12 Hộp" },
      { name: "Trân Châu Hoàng Kim 3Q", current: "0.8 kg", threshold: "2.0 kg" },
    ],
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Top Title Bar */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Store className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Dashboard Vận Hành Chi Nhánh
            </h1>
            <span className="text-xs text-slate-500">
              Chi nhánh Quận 1 (Trụ sở) • Theo dõi doanh thu & KPI trực tiếp
            </span>
          </div>
        </div>
      </div>

      {/* 4 Core KPI Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500 text-xs font-bold uppercase">
            <span>Doanh Thu Hôm Nay</span>
            <DollarSign className="h-4 w-4 text-amber-700" />
          </div>
          <div className="text-2xl font-black text-slate-950">
            {formatCurrencyVND(kpiData.todayRevenue)}
          </div>
          <span className="text-xs text-emerald-600 font-semibold">+18.5% so với hôm qua</span>
        </div>

        <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500 text-xs font-bold uppercase">
            <span>Số Đơn Đã Phục Vụ</span>
            <ShoppingBag className="h-4 w-4 text-sky-600" />
          </div>
          <div className="text-2xl font-black text-slate-950">{kpiData.ordersCount} đơn</div>
          <span className="text-xs text-slate-400 font-medium">Trung bình: 79.800₫ / đơn</span>
        </div>

        <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500 text-xs font-bold uppercase">
            <span>Tỷ Lệ VietQR / Tiền Mặt</span>
            <QrCode className="h-4 w-4 text-emerald-600" />
          </div>
          <div className="text-2xl font-black text-emerald-700">{kpiData.vietQrRatio}% VietQR</div>
          <span className="text-xs text-slate-500 font-medium">
            Tiền mặt chiếm: {(100 - kpiData.vietQrRatio).toFixed(1)}%
          </span>
        </div>

        <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500 text-xs font-bold uppercase">
            <span>Tuân Thủ SLA Bếp KDS</span>
            <Clock className="h-4 w-4 text-amber-700" />
          </div>
          <div className="text-2xl font-black text-amber-900">{kpiData.kdsSlaCompliance}%</div>
          <span className="text-xs text-emerald-600 font-semibold">&lt; 5 phút hoàn tất món</span>
        </div>
      </div>

      {/* 2-Column Operational Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Payment Channels Breakdown */}
        <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
          <h3 className="font-bold text-sm text-slate-900 border-b border-slate-100 pb-3">
            Cơ Cấu Doanh Thu Theo Kênh Thanh Toán
          </h3>

          <div className="space-y-3">
            <div className="space-y-1.5">
              <div className="flex justify-between text-xs font-bold">
                <span className="flex items-center gap-1.5 text-emerald-800">
                  <QrCode className="h-4 w-4" /> VietQR Chuyển Khoản Trả Trước (68.5%)
                </span>
                <span>{formatCurrencyVND((kpiData.todayRevenue * 68.5) / 100)}</span>
              </div>
              <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden">
                <div className="h-full bg-emerald-600 rounded-full" style={{ width: "68.5%" }} />
              </div>
            </div>

            <div className="space-y-1.5">
              <div className="flex justify-between text-xs font-bold">
                <span className="flex items-center gap-1.5 text-slate-700">
                  <Banknote className="h-4 w-4" /> Tiền Mặt Quầy / Trả Sau (31.5%)
                </span>
                <span>{formatCurrencyVND((kpiData.todayRevenue * 31.5) / 100)}</span>
              </div>
              <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden">
                <div className="h-full bg-amber-600 rounded-full" style={{ width: "31.5%" }} />
              </div>
            </div>
          </div>
        </div>

        {/* Low Stock BOM Ingredients Alert */}
        <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
          <div className="flex items-center justify-between border-b border-slate-100 pb-3">
            <div className="flex items-center gap-2 text-rose-700 font-bold text-sm">
              <AlertTriangle className="h-4 w-4" />
              <span>Cảnh Báo Nguyên Liệu Sắp Hết</span>
            </div>
            <span className="text-xs bg-rose-100 text-rose-800 font-bold px-2.5 py-0.5 rounded-full">
              {kpiData.lowStockIngredients.length} Mục
            </span>
          </div>

          <div className="space-y-2.5">
            {kpiData.lowStockIngredients.map((item, idx) => (
              <div
                key={idx}
                className="p-3 rounded-2xl bg-rose-50/60 border border-rose-200 flex items-center justify-between text-xs"
              >
                <div>
                  <span className="font-bold text-slate-900 block">{item.name}</span>
                  <span className="text-slate-500">Ngưỡng an toàn: {item.threshold}</span>
                </div>
                <span className="font-black text-rose-700 bg-rose-200/80 px-2.5 py-1 rounded-lg">
                  Còn: {item.current}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
