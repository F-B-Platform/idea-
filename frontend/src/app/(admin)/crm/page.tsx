"use client";

import { Users, Award } from "lucide-react";

export default function AdminCrmPage() {
  const customers = [
    { phone: "0901234567", name: "Nguyễn Thị Mai", takeawayCups: 9, totalPoints: 120 },
    { phone: "0987654321", name: "Trần Quốc Toản", takeawayCups: 4, totalPoints: 65 },
    { phone: "0912345678", name: "Lê Hoàng Nam", takeawayCups: 10, totalPoints: 210 },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <Users className="w-5 h-5 text-rose-600" /> Quản Lý Khách Hàng CRM & Tích Lũy 10 Ly Takeaway
        </h1>
        <p className="text-xs text-slate-500">Chính sách Loyalty: Tích 10 ly tặng 1 ly miễn phí chỉ áp dụng duy nhất cho đơn hàng mang về (Takeaway).</p>
      </header>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        <table className="w-full text-left text-xs">
          <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-semibold">
            <tr>
              <th className="p-3">Số Điện Thoại</th>
              <th className="p-3">Họ Tên Khách Hàng</th>
              <th className="p-3">Số Ly Takeaway Tích Lũy</th>
              <th className="p-3">Tổng Điểm</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 font-mono">
            {customers.map((c, idx) => (
              <tr key={idx} className="hover:bg-slate-50/50">
                <td className="p-3 font-bold text-slate-900">{c.phone}</td>
                <td className="p-3 font-sans font-semibold text-slate-800">{c.name}</td>
                <td className="p-3">
                  <span className="px-2.5 py-1 rounded-full bg-amber-50 text-amber-900 font-bold border border-amber-200 inline-flex items-center gap-1">
                    <Award className="w-3.5 h-3.5 text-amber-600" /> {c.takeawayCups} / 10 ly
                  </span>
                </td>
                <td className="p-3 font-semibold text-purple-700">{c.totalPoints} pts</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
