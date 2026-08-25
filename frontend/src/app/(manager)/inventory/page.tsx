"use client";

import { Package, AlertCircle } from "lucide-react";

export default function ManagerInventoryPage() {
  const stock = [
    { name: "Hạt Cà Phê Robusta Đắk Lắk", stock: "12.5 kg", min: "5.0 kg", status: "Đủ định mức" },
    { name: "Sữa Tươi Thanh Trùng DalatMilk", stock: "3.0 lít", min: "10.0 lít", status: "Cảnh báo thiếu" },
    { name: "Đào Miếng Ngâm Kronos", stock: "6 hộp", min: "4 hộp", status: "Đủ định mức" },
    { name: "Kem Muối Tươi (Bột Pha Chế)", stock: "1.2 kg", min: "2.0 kg", status: "Cảnh báo thiếu" },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <Package className="w-5 h-5 text-purple-600" /> Quản Lý Tồn Kho Nguyên Liệu & Định Mức BOM
        </h1>
        <p className="text-xs text-slate-500">Tồn kho được tự động trừ theo gam/ml khi đơn hàng hoàn tất pha chế tại KDS.</p>
      </header>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        <table className="w-full text-left text-xs">
          <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-semibold">
            <tr>
              <th className="p-3">Tên Nguyên Liệu</th>
              <th className="p-3">Tồn Kho Hiện Tại</th>
              <th className="p-3">Ngưỡng Tối Thiểu</th>
              <th className="p-3">Trạng Thái</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {stock.map((item, idx) => (
              <tr key={idx} className="hover:bg-slate-50/50">
                <td className="p-3 font-bold text-slate-900">{item.name}</td>
                <td className="p-3 font-mono font-semibold">{item.stock}</td>
                <td className="p-3 font-mono text-slate-500">{item.min}</td>
                <td className="p-3">
                  <span
                    className={`px-2 py-0.5 rounded-full font-semibold ${
                      item.status === "Đủ định mức"
                        ? "bg-emerald-50 text-emerald-700 border border-emerald-200"
                        : "bg-rose-50 text-rose-700 border border-rose-200 flex items-center gap-1 w-fit"
                    }`}
                  >
                    {item.status === "Cảnh báo thiếu" && <AlertCircle className="w-3 h-3" />}
                    {item.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
