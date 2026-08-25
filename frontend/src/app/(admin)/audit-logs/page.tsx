"use client";

import { FileText } from "lucide-react";

export default function AdminAuditLogsPage() {
  const logs = [
    { time: "10:20:15", user: "Admin (admin_hq)", action: "CẬP NHẬT GIÁ", detail: "Thay đổi giá Cà phê muối tại CN Quận 1 lên 35.000đ" },
    { time: "09:45:00", user: "Manager (mgr_q1)", action: "MỞ CA KÉT", detail: "Ghi nhận két tiền đầu ca 2.000.000đ" },
    { time: "08:30:12", user: "Staff (nv_002)", action: "CHẤM CÔNG WIFI", detail: "Vào ca thành công tại BSSID AA:BB:CC:DD:EE:01" },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <FileText className="w-5 h-5 text-rose-600" /> Nhật Ký Hệ Thống (Audit Logs)
        </h1>
        <p className="text-xs text-slate-500">Ghi lại toàn bộ hành động bảo mật, điều chỉnh giá, xuất kho và đối soát két tiền.</p>
      </header>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        <table className="w-full text-left text-xs">
          <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-semibold">
            <tr>
              <th className="p-3">Thời Gian</th>
              <th className="p-3">Người Thực Hiện</th>
              <th className="p-3">Hành Động</th>
              <th className="p-3">Chi Tiết Thay Đổi</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 font-mono">
            {logs.map((log, idx) => (
              <tr key={idx} className="hover:bg-slate-50/50">
                <td className="p-3 text-slate-500">{log.time}</td>
                <td className="p-3 font-sans font-bold text-slate-900">{log.user}</td>
                <td className="p-3">
                  <span className="px-2 py-0.5 rounded-full bg-slate-100 text-slate-700 font-sans font-semibold text-[11px]">
                    {log.action}
                  </span>
                </td>
                <td className="p-3 font-sans text-slate-700">{log.detail}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
