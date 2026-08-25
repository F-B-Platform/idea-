"use client";

import React, { useState } from "react";
import { WifiConfigDto } from "@/types";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";
import { Wifi, Plus, Trash2, ShieldCheck, CheckCircle2 } from "lucide-react";

const initialBranchWifi: WifiConfigDto[] = [
  {
    id: "wifi-01",
    branchId: "branch-q1",
    branchName: "Chi nhánh Quận 1 (Trụ Sở)",
    ssid: "SMART_FB_BRANCH_OFFICIAL",
    bssid: "AA:BB:CC:DD:EE:01",
    subnetIpRange: "192.168.1.0/24",
    isActive: true,
  },
  {
    id: "wifi-02",
    branchId: "branch-q1",
    branchName: "Chi nhánh Quận 1 (Trụ Sở)",
    ssid: "SMART_FB_STAFF_5G",
    bssid: "AA:BB:CC:DD:EE:02",
    subnetIpRange: "192.168.1.0/24",
    isActive: true,
  },
];

export default function ManagerWifiConfigPage() {
  const [configs, setConfigs] = useState<WifiConfigDto[]>(initialBranchWifi);
  const [ssid, setSsid] = useState("");
  const [bssid, setBssid] = useState("");
  const [subnet, setSubnet] = useState("192.168.1.0/24");
  const [error, setError] = useState<string | null>(null);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const macRegex = /^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/;

  const handleAddConfig = () => {
    setError(null);
    if (!ssid.trim()) {
      setError("Tên SSID mạng không được để trống");
      return;
    }
    if (!macRegex.test(bssid.trim())) {
      setError("Địa chỉ MAC / BSSID không đúng định dạng (Ví dụ: AA:BB:CC:DD:EE:03)");
      return;
    }
    if (!subnet.includes("/")) {
      setError("Dải Subnet IP phải đúng định dạng CIDR (Ví dụ: 192.168.1.0/24)");
      return;
    }

    const newConf: WifiConfigDto = {
      id: `wifi-${Date.now()}`,
      branchId: "branch-q1",
      branchName: "Chi nhánh Quận 1",
      ssid: ssid.trim(),
      bssid: bssid.trim().toUpperCase(),
      subnetIpRange: subnet.trim(),
      isActive: true,
    };

    setConfigs((prev) => [...prev, newConf]);
    setSsid("");
    setBssid("");
    setToastMessage("Đã đăng ký thêm Router WiFi chấm công thành công!");
    setTimeout(() => setToastMessage(null), 3000);
  };

  const handleDelete = (id: string) => {
    setConfigs((prev) => prev.filter((c) => c.id !== id));
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Wifi className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Cấu Hình Router BSSID & Dải IP Chấm Công
            </h1>
            <span className="text-xs text-slate-500">
              Quản lý danh sách địa chỉ MAC của các cục phát WiFi chính thức tại quán
            </span>
          </div>
        </div>
      </div>

      {toastMessage && (
        <div className="p-4 bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
          <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Add New Router Form */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-800 border-b border-slate-100 pb-3">
          Đăng Ký Thêm Router WiFi Chi Nhánh
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <Input
            label="Tên Mạng WiFi (SSID)"
            required
            placeholder="SMART_FB_Q1_5G"
            value={ssid}
            onChange={(e) => setSsid(e.target.value)}
          />
          <Input
            label="Địa chỉ BSSID (MAC Router)"
            required
            placeholder="AA:BB:CC:DD:EE:03"
            value={bssid}
            onChange={(e) => setBssid(e.target.value)}
          />
          <Input
            label="Dải Subnet IP (CIDR)"
            required
            placeholder="192.168.1.0/24"
            value={subnet}
            onChange={(e) => setSubnet(e.target.value)}
          />
        </div>

        {error && <p className="text-xs text-rose-600 font-semibold">{error}</p>}

        <div className="flex justify-end pt-2">
          <Button
            type="button"
            onClick={handleAddConfig}
            variant="primary"
            leftIcon={<Plus className="h-4 w-4" />}
          >
            Lưu Điểm WiFi Mới
          </Button>
        </div>
      </div>

      {/* Registered WiFi Routers List */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-500">
          Danh Sách Điểm Phát WiFi Đang Hoạt Động ({configs.length})
        </h3>

        <div className="space-y-3">
          {configs.map((c) => (
            <div
              key={c.id}
              className="p-4 rounded-2xl border border-slate-200 bg-slate-50/60 flex items-center justify-between shadow-2xs"
            >
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center border border-emerald-300">
                  <Wifi className="h-5 w-5" />
                </div>
                <div>
                  <span className="font-bold text-sm text-slate-900 block">{c.ssid}</span>
                  <div className="flex items-center gap-3 text-xs text-slate-500 font-mono mt-0.5">
                    <span>BSSID: {c.bssid}</span>
                    <span>•</span>
                    <span>Subnet: {c.subnetIpRange}</span>
                  </div>
                </div>
              </div>

              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold bg-emerald-100 text-emerald-800 px-2.5 py-1 rounded-full">
                  Hợp Lệ
                </span>
                <button
                  type="button"
                  onClick={() => handleDelete(c.id)}
                  className="p-2 text-slate-400 hover:text-rose-600 rounded-lg hover:bg-rose-50 transition-colors"
                >
                  <Trash2 className="h-4 w-4" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
