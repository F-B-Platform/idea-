"use client";

import Link from "next/link";
import { ArrowLeft, Wifi, UserCheck, ShieldAlert } from "lucide-react";

export default function StaffAttendancePage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-white rounded-2xl border border-slate-200 shadow-xl p-6 space-y-6">
        <div className="flex items-center gap-2">
          <Link href="/" className="p-2 rounded-lg hover:bg-slate-100 text-slate-600">
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <h1 className="text-base font-bold text-slate-900">Chấm Công Khóa Mạng WiFi</h1>
            <p className="text-xs text-slate-500">Xác thực BSSID Router & Mã Nhân Viên</p>
          </div>
        </div>

        {/* WiFi Status Card */}
        <div className="p-4 rounded-xl bg-indigo-50 border border-indigo-200 text-indigo-900 text-xs space-y-2">
          <div className="flex items-center gap-2 font-bold text-indigo-800">
            <Wifi className="w-4 h-4 text-indigo-600 animate-pulse" />
            Trạng Thái Kết Nối WiFi Chi Nhánh
          </div>
          <p className="text-indigo-700">
            Đang kết nối: <strong>SmartCoffee_Branch01</strong> (BSSID: <span className="font-mono">AA:BB:CC:DD:EE:FF</span>)
          </p>
        </div>

        {/* Input Form */}
        <div className="space-y-4">
          <div>
            <label className="text-xs font-semibold text-slate-600">Mã Số Nhân Viên (*)</label>
            <input
              type="text"
              placeholder="Ví dụ: NV-002"
              className="w-full mt-1 px-3 py-2 text-sm rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 font-mono"
            />
          </div>

          <div className="grid grid-cols-2 gap-3">
            <button className="py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs flex items-center justify-center gap-1 shadow-sm">
              <UserCheck className="w-4 h-4" /> Vào Ca (Check-In)
            </button>
            <button className="py-2.5 rounded-xl bg-slate-800 hover:bg-slate-900 text-white font-bold text-xs flex items-center justify-center gap-1 shadow-sm">
              Ra Ca (Check-Out)
            </button>
          </div>
        </div>

        <div className="text-[11px] text-slate-400 text-center flex items-center justify-center gap-1">
          <ShieldAlert className="w-3.5 h-3.5" />
          Không sử dụng GPS và QR động xoay. Chống gian lận 100%.
        </div>
      </div>
    </div>
  );
}
