"use client";

import React, { useState } from "react";
import { PriceGroupDto, ProductDto } from "@/types";
import { PricingMatrixTable } from "@/components/admin/PricingMatrixTable";
import { DollarSign } from "lucide-react";

const initialPriceGroups: PriceGroupDto[] = [
  {
    id: "grp-01",
    name: "Bảng Giá Chuẩn (Hồ Chí Minh)",
    regionCode: "HCM_STD",
    priceMultiplier: 1.0,
    assignedBranchCount: 2,
  },
  {
    id: "grp-02",
    name: "Bảng Giá Trung Tâm Quận 1 (+15%)",
    regionCode: "HCM_Q1_PREMIUM",
    priceMultiplier: 1.15,
    assignedBranchCount: 1,
  },
  {
    id: "grp-03",
    name: "Bảng Giá Làng Đại Học (-5%)",
    regionCode: "HCM_STUDENT",
    priceMultiplier: 0.95,
    assignedBranchCount: 1,
  },
];

const initialPricingProducts: ProductDto[] = [
  {
    id: "prod-01",
    sku: "CF-SALT-01",
    name: "Cà Phê Muối Hoàng Gia",
    basePrice: 35000,
    categoryId: "cat-01",
    categoryName: "Cà Phê Đặc Sản",
    isAvailable: true,
    sizes: [{ id: "s-01", sizeName: "M", price: 35000, isDefault: true }],
    modifiers: [],
  },
  {
    id: "prod-02",
    sku: "TEA-PEACH-02",
    name: "Trà Đào Cam Sả Tươi",
    basePrice: 39000,
    categoryId: "cat-02",
    categoryName: "Trà Trái Cây",
    isAvailable: true,
    sizes: [{ id: "s-02", sizeName: "M", price: 39000, isDefault: true }],
    modifiers: [],
  },
  {
    id: "prod-03",
    sku: "MILKTEA-OOLONG-03",
    name: "Trà Sữa Oolong Nướng",
    basePrice: 42000,
    categoryId: "cat-03",
    categoryName: "Trà Sữa Oolong",
    isAvailable: true,
    sizes: [{ id: "s-03", sizeName: "M", price: 42000, isDefault: true }],
    modifiers: [],
  },
  {
    id: "prod-04",
    sku: "CF-BACXIU-04",
    name: "Bạc Xỉu Sữa Hạnh Nhân",
    basePrice: 38000,
    categoryId: "cat-01",
    categoryName: "Cà Phê Đặc Sản",
    isAvailable: true,
    sizes: [{ id: "s-04", sizeName: "M", price: 38000, isDefault: true }],
    modifiers: [],
  },
];

export default function RegionalPricingPage() {
  const [priceGroups, setPriceGroups] = useState<PriceGroupDto[]>(initialPriceGroups);
  const [products] = useState<ProductDto[]>(initialPricingProducts);

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <DollarSign className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Quản Lý Bảng Giá Vùng Chi Nhánh (Regional Pricing Matrix)
            </h1>
            <span className="text-xs text-slate-500">
              Thiết lập hệ số nhân giá bán tự động áp dụng theo từng khu vực địa lý
            </span>
          </div>
        </div>
      </div>

      <PricingMatrixTable products={products} priceGroups={priceGroups} />
    </div>
  );
}
