"use client";

import React, { useState } from "react";
import { SeasonalMenuDto, ProductDto } from "@/types";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";
import { Calendar, Plus, Check, Clock } from "lucide-react";
import { formatDateTime } from "@/lib/utils";

export interface SeasonalSchedulerProps {
  campaigns: SeasonalMenuDto[];
  availableProducts: ProductDto[];
  onCreateCampaign: (campaign: Omit<SeasonalMenuDto, "id">) => void;
}

export const SeasonalScheduler: React.FC<SeasonalSchedulerProps> = ({
  campaigns,
  availableProducts,
  onCreateCampaign,
}) => {
  const [name, setName] = useState("");
  const [startDate, setStartDate] = useState("2026-06-01T00:00");
  const [endDate, setEndDate] = useState("2026-08-31T23:59");
  const [selectedProductIds, setSelectedProductIds] = useState<string[]>([]);

  const handleToggleProduct = (id: string) => {
    setSelectedProductIds((prev) =>
      prev.includes(id) ? prev.filter((p) => p !== id) : [...prev, id]
    );
  };

  const handleCreate = () => {
    if (!name.trim()) return;
    onCreateCampaign({
      name: name.trim(),
      startDateUtc: new Date(startDate).toISOString(),
      endDateUtc: new Date(endDate).toISOString(),
      isActive: true,
      productIds: selectedProductIds,
    });
    setName("");
    setSelectedProductIds([]);
  };

  return (
    <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-6">
      <div className="flex items-center gap-2 border-b border-slate-100 pb-4">
        <Calendar className="h-5 w-5 text-amber-700" />
        <h3 className="font-bold text-base text-slate-900">
          Lên Lịch Thực Đơn Mùa Vụ (Seasonal Menu Scheduler)
        </h3>
      </div>

      {/* Create New Campaign Form */}
      <div className="p-4 rounded-2xl bg-amber-50/60 border border-amber-200/80 space-y-4">
        <h4 className="font-bold text-xs uppercase tracking-wider text-amber-900">
          Tạo Chiến Dịch Thực Đơn Mùa Mới
        </h4>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <Input
            label="Tên Thực Đơn Mùa"
            placeholder="Ví dụ: Trà Trái Cây Mùa Hè 2026"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <Input
            label="Ngày Bắt Đầu"
            type="datetime-local"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
          />
          <Input
            label="Ngày Kết Thúc"
            type="datetime-local"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
          />
        </div>

        {/* Multi-product checkbox selection */}
        <div className="space-y-2">
          <label className="block text-xs font-semibold text-slate-700">
            Chọn các món áp dụng trong thực đơn mùa này ({selectedProductIds.length} món đã chọn):
          </label>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 max-h-36 overflow-y-auto p-1 bg-white rounded-xl border border-slate-200">
            {availableProducts.map((p) => {
              const isSelected = selectedProductIds.includes(p.id);
              return (
                <button
                  type="button"
                  key={p.id}
                  onClick={() => handleToggleProduct(p.id)}
                  className={`flex items-center justify-between p-2 rounded-lg text-xs font-medium border transition-colors ${
                    isSelected
                      ? "border-amber-600 bg-amber-50 text-amber-900"
                      : "border-slate-200 hover:bg-slate-50 text-slate-700"
                  }`}
                >
                  <span className="truncate pr-1">{p.name}</span>
                  {isSelected && <Check className="h-3.5 w-3.5 text-amber-700 shrink-0" />}
                </button>
              );
            })}
          </div>
        </div>

        <div className="flex justify-end">
          <Button
            type="button"
            onClick={handleCreate}
            size="sm"
            variant="primary"
            leftIcon={<Plus className="h-4 w-4" />}
          >
            Lên Lịch Chiến Dịch Mùa
          </Button>
        </div>
      </div>

      {/* Scheduled Campaigns List */}
      <div className="space-y-3">
        <h4 className="font-bold text-xs uppercase tracking-wider text-slate-500">
          Các Chiến Dịch Thực Đơn Mùa Vụ ({campaigns.length})
        </h4>

        <div className="space-y-2">
          {campaigns.map((c) => (
            <div
              key={c.id}
              className="p-4 rounded-xl border border-slate-200 bg-white flex items-center justify-between shadow-sm"
            >
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <span className="font-bold text-sm text-slate-900">{c.name}</span>
                  <span className="text-[10px] bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full font-bold">
                    Đang Hoạt Động
                  </span>
                </div>
                <div className="flex items-center gap-2 text-xs text-slate-500">
                  <Clock className="h-3.5 w-3.5" />
                  <span>
                    {formatDateTime(c.startDateUtc)} ➔ {formatDateTime(c.endDateUtc)}
                  </span>
                </div>
              </div>

              <span className="text-xs font-bold text-amber-800 bg-amber-50 px-2.5 py-1 rounded-lg border border-amber-200">
                {c.productIds.length} Món Áp Dụng
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
