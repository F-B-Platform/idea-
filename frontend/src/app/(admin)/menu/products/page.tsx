"use client";

import { Coffee, Plus, Edit2, Trash2 } from "lucide-react";

export default function AdminProductsPage() {
  const products = [
    { code: "CF-01", name: "Cà Phê Muối Hoàng Gia", category: "Cà Phê", basePrice: "35.000đ", sizes: "S, M, L", hasBom: true },
    { code: "TEA-01", name: "Trà Đào Cam Sả Tươi", category: "Trà Trái Cây", basePrice: "42.000đ", sizes: "M, L", hasBom: true },
    { code: "MLK-01", name: "Trà Sữa Oolong Nướng", category: "Trà Sữa", basePrice: "39.000đ", sizes: "S, M, L", hasBom: true },
  ];

  return (
    <div className="p-6 max-w-6xl mx-auto space-y-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Coffee className="w-5 h-5 text-rose-600" /> Quản Lý Danh Mục Món & Định Mức BOM
          </h1>
          <p className="text-xs text-slate-500">Cấu hình chi tiết món, giá chuẩn và định mức BOM cho từng Size (S/M/L).</p>
        </div>
        <button className="px-3.5 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs flex items-center gap-1.5 shadow">
          <Plus className="w-4 h-4" /> Thêm Món Mới
        </button>
      </header>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        <table className="w-full text-left text-xs">
          <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-semibold">
            <tr>
              <th className="p-3">Mã Món</th>
              <th className="p-3">Tên Món</th>
              <th className="p-3">Danh Mục</th>
              <th className="p-3">Giá Gốc</th>
              <th className="p-3">Sizes</th>
              <th className="p-3">Định Mức BOM</th>
              <th className="p-3 text-right">Thao Tác</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {products.map((p, idx) => (
              <tr key={idx} className="hover:bg-slate-50/50">
                <td className="p-3 font-mono font-bold text-slate-900">{p.code}</td>
                <td className="p-3 font-semibold text-slate-800">{p.name}</td>
                <td className="p-3 text-slate-600">{p.category}</td>
                <td className="p-3 font-bold text-rose-600">{p.basePrice}</td>
                <td className="p-3 font-mono text-slate-600">{p.sizes}</td>
                <td className="p-3">
                  <span className="px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-semibold border border-emerald-200">
                    Đã cấu hình
                  </span>
                </td>
                <td className="p-3 text-right space-x-2">
                  <button className="p-1 hover:text-rose-600 text-slate-400"><Edit2 className="w-4 h-4" /></button>
                  <button className="p-1 hover:text-rose-600 text-slate-400"><Trash2 className="w-4 h-4" /></button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
