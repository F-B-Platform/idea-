"use client";

import { DollarSign } from "lucide-react";

export default function AdminPricingPage() {
  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-rose-600" /> Bảng Giá Theo Vùng & Chi Nhánh
        </h1>
        <p className="text-xs text-slate-500">Cấu hình giá bán linh hoạt cho từng chi nhánh khác nhau theo khu vực (Quận 1, Cầu Giấy, Hải Châu).</p>
      </header>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-4">
        <p className="text-xs text-slate-600">Sẵn sàng để kết nối API quản lý giá vùng `ProductBranchPrices`.</p>
      </div>
    </div>
  );
}
