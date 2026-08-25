"use client";

import React, { useState } from "react";
import { Modal } from "@/components/ui/Modal";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";
import { WifiConfigDto } from "@/types";
import { Wifi, Plus, Trash2, CheckCircle2 } from "lucide-react";

export interface WifiConfigModalProps {
  isOpen: boolean;
  onClose: () => void;
  branchName?: string;
  configs: WifiConfigDto[];
  onSaveConfig: (config: Omit<WifiConfigDto, "id">) => void;
  onDeleteConfig: (id: string) => void;
}

export const WifiConfigModal: React.FC<WifiConfigModalProps> = ({
  isOpen,
  onClose,
  branchName = "Chi nhánh Quận 1",
  configs,
  onSaveConfig,
  onDeleteConfig,
}) => {
  const [ssid, setSsid] = useState("");
  const [bssid, setBssid] = useState("");
  const [subnet, setSubnet] = useState("192.168.1.0/24");
  const [error, setError] = useState<string | null>(null);

  const macRegex = /^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/;

  const handleAdd = () => {
    setError(null);
    if (!ssid.trim()) {
      setError("Tên SSID mạng không được để trống");
      return;
    }
    if (!macRegex.test(bssid.trim())) {
      setError("Địa chỉ MAC / BSSID không đúng định dạng (Ví dụ: AA:BB:CC:DD:EE:01)");
      return;
    }
    if (!subnet.includes("/")) {
      setError("Dải Subnet IP phải đúng định dạng CIDR (Ví dụ: 192.168.1.0/24)");
      return;
    }

    onSaveConfig({
      branchId: "branch-q1",
      branchName,
      ssid: ssid.trim(),
      bssid: bssid.trim().toUpperCase(),
      subnetIpRange: subnet.trim(),
      isActive: true,
    });

    setSsid("");
    setBssid("");
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      maxWidth="2xl"
      title={
        <div className="flex items-center gap-2 text-amber-900">
          <Wifi className="h-5 w-5 text-amber-700" />
          <span>Cấu Hình Router WiFi Chấm Công — {branchName}</span>
        </div>
      }
      description="Khai báo địa chỉ BSSID (MAC Router) và Subnet IP để hệ thống khóa mạng chấm công chính xác."
      footer={
        <Button variant="secondary" onClick={onClose}>
          Đóng Cửa Sổ
        </Button>
      }
    >
      <div className="space-y-6">
        {/* Form add new wifi config */}
        <div className="p-4 rounded-2xl bg-amber-50/60 border border-amber-200/80 space-y-4">
          <h4 className="font-bold text-xs uppercase tracking-wider text-amber-900">
            Thêm Điểm Phát WiFi Mới
          </h4>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <Input
              label="Tên WiFi (SSID)"
              placeholder="SMART_FB_Q1"
              value={ssid}
              onChange={(e) => setSsid(e.target.value)}
            />
            <Input
              label="Địa chỉ BSSID (MAC)"
              placeholder="AA:BB:CC:DD:EE:01"
              value={bssid}
              onChange={(e) => setBssid(e.target.value)}
            />
            <Input
              label="Dải Subnet CIDR"
              placeholder="192.168.1.0/24"
              value={subnet}
              onChange={(e) => setSubnet(e.target.value)}
            />
          </div>

          {error && <p className="text-xs text-rose-600 font-medium">{error}</p>}

          <div className="flex justify-end">
            <Button
              type="button"
              onClick={handleAdd}
              size="sm"
              variant="amber"
              leftIcon={<Plus className="h-4 w-4" />}
            >
              Lưu Điểm WiFi Mới
            </Button>
          </div>
        </div>

        {/* Existing Wifi Configs List */}
        <div className="space-y-2">
          <h4 className="font-bold text-xs uppercase tracking-wider text-slate-500">
            Danh Sách Router Đã Đăng Ký ({configs.length})
          </h4>

          <div className="space-y-2 max-h-[220px] overflow-y-auto">
            {configs.length === 0 ? (
              <p className="text-xs text-slate-400 py-4 text-center">Chưa có router nào được cấu hình.</p>
            ) : (
              configs.map((c) => (
                <div
                  key={c.id}
                  className="flex items-center justify-between p-3 rounded-xl bg-white border border-slate-200 shadow-sm"
                >
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 border border-emerald-200 flex items-center justify-center">
                      <Wifi className="h-4 w-4" />
                    </div>
                    <div>
                      <span className="font-bold text-xs text-slate-900 block">{c.ssid}</span>
                      <div className="flex items-center gap-2 text-[11px] text-slate-500 font-mono">
                        <span>BSSID: {c.bssid}</span>
                        <span>•</span>
                        <span>Subnet: {c.subnetIpRange}</span>
                      </div>
                    </div>
                  </div>

                  <button
                    type="button"
                    onClick={() => onDeleteConfig(c.id)}
                    className="p-1.5 rounded-lg text-slate-400 hover:text-rose-600 hover:bg-rose-50 transition-colors"
                  >
                    <Trash2 className="h-4 w-4" />
                  </button>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </Modal>
  );
};
