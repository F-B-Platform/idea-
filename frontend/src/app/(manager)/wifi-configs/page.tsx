"use client";

import { Wifi, Plus, ShieldCheck } from "lucide-react";

export default function ManagerWifiConfigsPage() {
  const wifis = [
    { ssid: "SmartCoffee_Branch01_5G", bssid: "AA:BB:CC:DD:EE:01", subnet: "192.168.1.0/24", status: "Active" },
    { ssid: "SmartCoffee_Branch01_2.4G", bssid: "AA:BB:CC:DD:EE:02", subnet: "192.168.1.0/24", status: "Active" },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Wifi className="w-5 h-5 text-purple-600" /> Cấu Hình Access Point WiFi Chấm Công
          </h1>
          <p className="text-xs text-slate-500">Khóa mạng WiFi chi nhánh dựa trên BSSID Router & Subnet IP.</p>
        </div>
        <button className="px-3 py-2 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs flex items-center gap-1.5 shadow">
          <Plus className="w-4 h-4" /> Thêm Router AP
        </button>
      </header>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        <table className="w-full text-left text-xs">
          <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-semibold">
            <tr>
              <th className="p-3">Tên WiFi (SSID)</th>
              <th className="p-3">Địa Chỉ MAC (BSSID)</th>
              <th className="p-3">Dải Mạng (IP Subnet)</th>
              <th className="p-3">Trạng Thái</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 font-mono">
            {wifis.map((w, idx) => (
              <tr key={idx} className="hover:bg-slate-50/50">
                <td className="p-3 font-sans font-bold text-slate-900">{w.ssid}</td>
                <td className="p-3 text-purple-700 font-semibold">{w.bssid}</td>
                <td className="p-3 text-slate-600">{w.subnet}</td>
                <td className="p-3">
                  <span className="px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-sans font-semibold border border-emerald-200">
                    {w.status}
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
