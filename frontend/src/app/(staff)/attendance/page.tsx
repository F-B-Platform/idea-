"use client";

import React, { useState } from "react";
import { useAttendanceWifi } from "@/hooks/useAttendanceWifi";
import { formatDateTime } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { AttendanceRecordDto } from "@/types";
import {
  Wifi,
  WifiOff,
  Clock,
  CheckCircle2,
  AlertTriangle,
  UserCheck,
  Calendar,
  LogOut,
} from "lucide-react";

const initialHistory: AttendanceRecordDto[] = [
  {
    id: "att-01",
    employeeCode: "NV001",
    employeeName: "Nguyễn Văn Thu Ngân",
    branchId: "branch-q1",
    branchName: "Chi nhánh Quận 1",
    clockInUtc: "2026-08-25T07:00:00Z",
    clockInBssid: "AA:BB:CC:DD:EE:01",
    clockInIp: "192.168.1.105",
    isClockInValid: true,
    status: "Working",
  },
  {
    id: "att-02",
    employeeCode: "NV001",
    employeeName: "Nguyễn Văn Thu Ngân",
    branchId: "branch-q1",
    branchName: "Chi nhánh Quận 1",
    clockInUtc: "2026-08-24T07:02:00Z",
    clockOutUtc: "2026-08-24T15:30:00Z",
    clockInBssid: "AA:BB:CC:DD:EE:01",
    clockInIp: "192.168.1.105",
    isClockInValid: true,
    isClockOutValid: true,
    workHours: 8.5,
    status: "Completed",
  },
];

export default function WifiAttendancePage() {
  const { wifiStatus, isLoading, error, clockIn, clockOut } = useAttendanceWifi("branch-q1");
  const [employeeCode, setEmployeeCode] = useState("NV001");
  const [history, setHistory] = useState<AttendanceRecordDto[]>(initialHistory);
  const [message, setMessage] = useState<string | null>(null);

  const handleClockIn = async () => {
    if (!employeeCode.trim()) return;
    const result = await clockIn(employeeCode.trim());
    if (result) {
      setHistory((prev) => [result, ...prev]);
      setMessage("Chấm công vào ca thành công! Chúc bạn một ngày làm việc hiệu quả.");
    }
  };

  const handleClockOut = async () => {
    if (!employeeCode.trim()) return;
    const result = await clockOut(employeeCode.trim());
    if (result) {
      setHistory((prev) =>
        prev.map((h) => (h.id === result.id ? result : h))
      );
      setMessage("Chấm công ra ca thành công! Cảm ơn bạn đã nỗ lực trong ca.");
    }
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Top Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Wifi className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Chấm Công Khóa Mạng WiFi Chi Nhánh
            </h1>
            <span className="text-xs text-slate-500">
              Xác thực kép địa chỉ BSSID (MAC Router) & IP Subnet nội bộ
            </span>
          </div>
        </div>
      </div>

      {/* Network Verification Context Card */}
      <div
        className={`p-6 rounded-3xl border-2 shadow-sm space-y-4 ${
          wifiStatus.isValidBranchWifi
            ? "bg-emerald-50/80 border-emerald-300 text-emerald-950"
            : "bg-rose-50 border-rose-300 text-rose-950"
        }`}
      >
        <div className="flex items-start justify-between">
          <div className="flex items-center gap-3">
            <div
              className={`w-12 h-12 rounded-2xl flex items-center justify-center ${
                wifiStatus.isValidBranchWifi
                  ? "bg-emerald-600 text-white"
                  : "bg-rose-600 text-white"
              }`}
            >
              {wifiStatus.isValidBranchWifi ? (
                <Wifi className="h-6 w-6" />
              ) : (
                <WifiOff className="h-6 w-6" />
              )}
            </div>
            <div>
              <span className="text-xs font-bold uppercase tracking-wider opacity-75">
                Trạng Thái Kết Nối Mạng Quán
              </span>
              <h3 className="text-lg font-black">{wifiStatus.ssid}</h3>
            </div>
          </div>

          <span
            className={`text-xs font-bold px-3 py-1 rounded-full border ${
              wifiStatus.isValidBranchWifi
                ? "bg-emerald-100 text-emerald-800 border-emerald-300"
                : "bg-rose-100 text-rose-800 border-rose-300"
            }`}
          >
            {wifiStatus.isValidBranchWifi ? "Đúng WiFi Chi Nhánh" : "Sai WiFi / 4G (Bị Khóa)"}
          </span>
        </div>

        {/* Technical Network Details (Dual Lock) */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs bg-white/70 backdrop-blur p-4 rounded-2xl border border-current/20">
          <div>
            <span className="text-slate-500 block text-[11px]">BSSID (MAC Router):</span>
            <strong className="font-mono">{wifiStatus.bssid}</strong>
          </div>
          <div>
            <span className="text-slate-500 block text-[11px]">IP Thiết Bị:</span>
            <strong className="font-mono">{wifiStatus.clientIp}</strong>
          </div>
          <div>
            <span className="text-slate-500 block text-[11px]">Chi Nhánh Xác Thực:</span>
            <strong>{wifiStatus.branchName || "Chi nhánh Q1"}</strong>
          </div>
        </div>
      </div>

      {/* Clock-in / Out Form Card */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-5">
        <h3 className="font-bold text-sm uppercase tracking-wider text-slate-800 border-b border-slate-100 pb-3">
          Thực Hiện Chấm Công Vào / Ra Ca
        </h3>

        {message && (
          <div className="p-4 bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
            <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0" />
            <span>{message}</span>
          </div>
        )}

        {error && (
          <div className="p-4 bg-rose-50 border border-rose-300 text-rose-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
            <AlertTriangle className="h-5 w-5 text-rose-600 shrink-0" />
            <span>{error}</span>
          </div>
        )}

        <div className="max-w-md space-y-4">
          <Input
            label="Mã Số Nhân Viên (Employee Code)"
            required
            placeholder="Ví dụ: NV001"
            value={employeeCode}
            onChange={(e) => setEmployeeCode(e.target.value)}
          />

          {/* 2 Big Action Buttons */}
          <div className="grid grid-cols-2 gap-4 pt-2">
            <Button
              type="button"
              onClick={handleClockIn}
              disabled={isLoading || !wifiStatus.isValidBranchWifi}
              isLoading={isLoading}
              size="lg"
              className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs shadow-md min-h-[50px]"
              leftIcon={<Clock className="h-4 w-4" />}
            >
              VÀO CA (CLOCK-IN)
            </Button>

            <Button
              type="button"
              onClick={handleClockOut}
              disabled={isLoading || !wifiStatus.isValidBranchWifi}
              isLoading={isLoading}
              size="lg"
              variant="danger"
              className="font-extrabold text-xs shadow-md min-h-[50px]"
              leftIcon={<LogOut className="h-4 w-4" />}
            >
              RA CA (CLOCK-OUT)
            </Button>
          </div>
        </div>
      </div>

      {/* Attendance History Table */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-500">
          Lịch Sử Chấm Công Gần Nhất
        </h3>

        <div className="space-y-2">
          {history.map((record) => (
            <div
              key={record.id}
              className="p-4 rounded-2xl border border-slate-200 bg-slate-50/50 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs"
            >
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-bold text-sm text-slate-900">{record.employeeName}</span>
                  <span className="font-mono text-slate-500 font-semibold">({record.employeeCode})</span>
                </div>
                <div className="flex items-center gap-2 text-slate-500 mt-1">
                  <Calendar className="h-3.5 w-3.5" />
                  <span>Vào: {formatDateTime(record.clockInUtc)}</span>
                  {record.clockOutUtc && (
                    <span>• Ra: {formatDateTime(record.clockOutUtc)}</span>
                  )}
                </div>
              </div>

              <div className="flex items-center gap-3">
                {record.workHours && (
                  <span className="font-bold text-slate-700 bg-slate-200 px-2.5 py-1 rounded-lg">
                    {record.workHours} Giờ Làm
                  </span>
                )}
                <span
                  className={`px-3 py-1 rounded-full font-bold ${
                    record.status === "Completed"
                      ? "bg-emerald-100 text-emerald-800"
                      : "bg-amber-100 text-amber-800"
                  }`}
                >
                  {record.status === "Completed" ? "Đã Ra Ca" : "Đang Làm Việc"}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
