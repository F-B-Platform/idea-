"use client";

import React, { useState } from "react";
import { SeasonalMenuDto, ProductDto } from "@/types";
import { SeasonalScheduler } from "@/components/admin/SeasonalScheduler";

const mockAdminProducts: ProductDto[] = [
  {
    id: "prod-01",
    sku: "CF-SALT-01",
    name: "Cà Phê Muối Hoàng Gia",
    basePrice: 35000,
    categoryId: "cat-01",
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
    isAvailable: true,
    sizes: [{ id: "s-03", sizeName: "M", price: 42000, isDefault: true }],
    modifiers: [],
  },
];

const initialCampaigns: SeasonalMenuDto[] = [
  {
    id: "camp-01",
    name: "Thực Đơn Mùa Hè Rực Rỡ 2026",
    description: "Bộ sưu tập trà trái cây và sinh tố nhiệt đới thanh mát.",
    startDateUtc: "2026-06-01T00:00:00Z",
    endDateUtc: "2026-08-31T23:59:59Z",
    isActive: true,
    productIds: ["prod-02", "prod-03"],
  },
];

export default function SeasonalMenuPage() {
  const [campaigns, setCampaigns] = useState<SeasonalMenuDto[]>(initialCampaigns);

  const handleCreateCampaign = (camp: Omit<SeasonalMenuDto, "id">) => {
    const newCamp: SeasonalMenuDto = {
      ...camp,
      id: `camp-${Date.now()}`,
    };
    setCampaigns((prev) => [newCamp, ...prev]);
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      <SeasonalScheduler
        campaigns={campaigns}
        availableProducts={mockAdminProducts}
        onCreateCampaign={handleCreateCampaign}
      />
    </div>
  );
}
