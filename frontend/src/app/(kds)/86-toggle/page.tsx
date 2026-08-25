"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { Switch } from "@/components/ui/Switch";
import { SearchInput } from "@/components/ui/SearchInput";
import { Button } from "@/components/ui/Button";
import { AlertOctagon, ArrowLeft, CheckCircle2 } from "lucide-react";
import { Product86ToggleDto } from "@/types";

const initial86List: Product86ToggleDto[] = [
  { productId: "prod-01", productName: "Cà Phê Muối Hoàng Gia", categoryName: "Cà Phê Đặc Sản", isAvailable: true },
  { productId: "prod-02", productName: "Trà Đào Cam Sả Tươi", categoryName: "Trà Trái Cây", isAvailable: true },
  { productId: "prod-03", productName: "Matcha Latte Kem Trứng", categoryName: "Đá Xay & Matcha", isAvailable: false },
  { productId: "prod-04", productName: "Trà Sữa Oolong Nướng", categoryName: "Trà Sữa", isAvailable: true },
  { productId: "prod-05", productName: "Bạc Xỉu Sữa Hạnh Nhân", categoryName: "Cà Phê Đặc Sản", isAvailable: true },
  { productId: "prod-06", productName: "Cà Phê Đen Đá Phin", categoryName: "Cà Phê Truyền Thống", isAvailable: true },
  { productId: "prod-07", productName: "Sinh Tố Bơ Sáp Dừa", categoryName: "Đá Xay & Sinh Tố", isAvailable: true },
  { productId: "prod-08", productName: "Bánh Croissant Bơ Tỏi Phô Mai", categoryName: "Bánh Ngọt & Pastry", isAvailable: false },
];

export default function Emergency86Page() {
  const router = useRouter();
  const [items, setItems] = useState<Product86ToggleDto[]>(initial86List);
  const [search, setSearch] = useState("");
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const filteredItems = items.filter(
    (i) =>
      i.productName.toLowerCase().includes(search.toLowerCase()) ||
      i.categoryName.toLowerCase().includes(search.toLowerCase())
  );

  const handleToggle = (productId: string, isAvailable: boolean) => {
    setItems((prev) =>
      prev.map((i) => (i.productId === productId ? { ...i, isAvailable } : i))
    );

    const product = items.find((i) => i.productId === productId);
    setToastMessage(
      isAvailable
        ? `Đã mở bán lại món: ${product?.productName}`
        : `ĐÃ KHÓA HẾT HÀNG (86'd): ${product?.productName}`
    );
    setTimeout(() => setToastMessage(null), 3000);
  };

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      {/* Top Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div className="flex items-center gap-3">
          <button
            onClick={() => router.push("/kitchen")}
            className="p-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700"
          >
            <ArrowLeft className="h-5 w-5" />
          </button>
          <div>
            <h1 className="text-xl font-extrabold text-white flex items-center gap-2">
              <AlertOctagon className="h-6 w-6 text-rose-500" />
              <span>Quản Lý Khóa Món Khẩn Cấp (86-Toggle)</span>
            </h1>
            <p className="text-xs text-slate-400">
              Khóa món sẽ lập tức gỡ món khỏi Menu Khách Hàng và Web POS Quầy Thu Ngân.
            </p>
          </div>
        </div>
      </div>

      {toastMessage && (
        <div className="p-3.5 bg-emerald-950/80 border border-emerald-500 text-emerald-300 text-xs font-bold rounded-xl flex items-center gap-2 animate-in fade-in">
          <CheckCircle2 className="h-4 w-4" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Search Input */}
      <SearchInput
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        onClear={() => setSearch("")}
        placeholder="Tìm kiếm món ăn, đồ uống cần khóa..."
        className="bg-slate-800 border-slate-700 text-white placeholder:text-slate-400"
      />

      {/* Grid of Items */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {filteredItems.map((item) => (
          <div
            key={item.productId}
            className="p-4 rounded-2xl bg-slate-800/80 border border-slate-700 hover:border-slate-600 flex items-center justify-between transition-colors shadow-sm"
          >
            <div>
              <span className="font-bold text-sm text-white block">{item.productName}</span>
              <span className="text-xs text-slate-400">{item.categoryName}</span>
            </div>

            <div className="flex items-center gap-3">
              <span
                className={`text-xs font-bold ${
                  item.isAvailable ? "text-emerald-400" : "text-rose-400 font-extrabold"
                }`}
              >
                {item.isAvailable ? "ĐANG BÁN" : "HẾT HÀNG (86)"}
              </span>
              <Switch
                checked={item.isAvailable}
                onCheckedChange={(checked) => handleToggle(item.productId, checked)}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
