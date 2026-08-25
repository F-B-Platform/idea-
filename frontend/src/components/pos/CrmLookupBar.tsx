"use client";

import React, { useState } from "react";
import { Search, UserCheck, UserX, Gift, UserPlus } from "lucide-react";
import { PosCustomer } from "@/stores/usePosStore";
import { validateVietnamesePhone } from "@/lib/utils";

export interface CrmLookupBarProps {
  currentCustomer: PosCustomer | null;
  onCustomerFound: (customer: PosCustomer) => void;
  onClearCustomer: () => void;
}

export const CrmLookupBar: React.FC<CrmLookupBarProps> = ({
  currentCustomer,
  onCustomerFound,
  onClearCustomer,
}) => {
  const [phone, setPhone] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isSearching, setIsSearching] = useState(false);

  const handleSearch = () => {
    setError(null);
    const validation = validateVietnamesePhone(phone);
    if (!validation.isValid) {
      setError(validation.message || "Số điện thoại không hợp lệ");
      return;
    }

    setIsSearching(true);
    // Simulate real CRM API lookup or creation
    setTimeout(() => {
      setIsSearching(false);
      // If phone ends with 88 or 99, give 10 cups for testing redemption
      const cups = phone.endsWith("88") || phone.endsWith("99") ? 10 : 7;
      onCustomerFound({
        customerId: `cust-${phone}`,
        phone: phone.trim(),
        fullName: phone.endsWith("88") ? "Nguyễn Văn VIP (10 Ly)" : "Khách Hàng Thân Thiết",
        cupBalance: cups,
        eligibleForFreeCup: cups >= 10,
        totalOrdersCount: 14,
      });
      setPhone("");
    }, 300);
  };

  return (
    <div className="bg-white rounded-2xl p-4 border border-slate-200 shadow-sm space-y-3">
      {currentCustomer ? (
        <div className="flex items-center justify-between bg-amber-50/80 border border-amber-200/80 p-3 rounded-xl">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-amber-700 text-white flex items-center justify-center font-bold">
              <UserCheck className="h-5 w-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-bold text-sm text-slate-900">{currentCustomer.fullName}</span>
                <span className="text-xs text-slate-500 font-medium">({currentCustomer.phone})</span>
              </div>
              <div className="flex items-center gap-2 mt-0.5">
                <span className="text-xs font-semibold text-amber-800">
                  Quỹ ly: {currentCustomer.cupBalance}/10 ly
                </span>
                {currentCustomer.cupBalance >= 10 && (
                  <span className="text-[10px] bg-emerald-600 text-white px-2 py-0.5 rounded-full font-bold animate-pulse">
                    Đủ 10 ly đổi quà!
                  </span>
                )}
              </div>
            </div>
          </div>

          <button
            type="button"
            onClick={onClearCustomer}
            className="p-2 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-amber-100 transition-colors"
            title="Đổi khách hàng khác"
          >
            <UserX className="h-5 w-5" />
          </button>
        </div>
      ) : (
        <div className="space-y-1.5">
          <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
            Tra Cứu Hội Viên / Tích Điểm 10 Ly (SĐT)
          </label>
          <div className="flex gap-2">
            <div className="relative flex-1">
              <input
                type="tel"
                value={phone}
                onChange={(e) => {
                  setPhone(e.target.value);
                  if (error) setError(null);
                }}
                onKeyDown={(e) => e.key === "Enter" && handleSearch()}
                placeholder="Nhập 10 số điện thoại (03x, 05x, 07x, 08x, 09x)..."
                className="w-full pl-3.5 pr-10 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-amber-600 min-h-[44px]"
              />
            </div>
            <button
              type="button"
              onClick={handleSearch}
              disabled={isSearching}
              className="px-4 py-2.5 bg-amber-700 hover:bg-amber-800 text-white font-bold text-xs rounded-xl flex items-center gap-1.5 shadow-sm min-h-[44px] shrink-0"
            >
              <Search className="h-4 w-4" />
              <span>{isSearching ? "Đang tìm..." : "Tra Cứu"}</span>
            </button>
          </div>
          {error && <p className="text-xs text-rose-600 font-medium">{error}</p>}
        </div>
      )}
    </div>
  );
};
