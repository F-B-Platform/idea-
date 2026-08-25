"use client";

import React, { useState, useEffect } from "react";
import { useParams, useRouter } from "next/navigation";
import { ProductDto, CategoryDto } from "@/types";
import { useCartStore } from "@/stores/useCartStore";
import { formatCurrencyVND } from "@/lib/utils";
import { CustomizationDrawer } from "@/components/order/CustomizationDrawer";
import { SearchInput } from "@/components/ui/SearchInput";
import { Button } from "@/components/ui/Button";
import {
  Sparkles,
  Plus,
  ShoppingBag,
  Flame,
  ArrowRight,
  Coffee,
  Check,
} from "lucide-react";

const initialCategories: CategoryDto[] = [
  { id: "cat-all", name: "Tất Cả", displayOrder: 0, isActive: true },
  { id: "cat-01", name: "Cà Phê Đặc Sản", displayOrder: 1, isActive: true },
  { id: "cat-02", name: "Trà Trái Cây", displayOrder: 2, isActive: true },
  { id: "cat-03", name: "Trà Sữa Oolong", displayOrder: 3, isActive: true },
  { id: "cat-04", name: "Đá Xay & Sinh Tố", displayOrder: 4, isActive: true },
  { id: "cat-05", name: "Bánh Ngọt & Pastry", displayOrder: 5, isActive: true },
];

const mockProducts: ProductDto[] = [
  {
    id: "prod-01",
    sku: "CF-SALT-01",
    name: "Cà Phê Muối Hoàng Gia",
    description: "Cà phê Robusta Đắk Lắk đậm đà hòa quyện lớp kem muối béo ngậy thủ công.",
    basePrice: 35000,
    imageUrl: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400&q=80",
    categoryId: "cat-01",
    categoryName: "Cà Phê Đặc Sản",
    isAvailable: true,
    isBestSeller: true,
    sizes: [
      { id: "s-01", sizeName: "S", price: 32000, isDefault: false },
      { id: "s-02", sizeName: "M", price: 35000, isDefault: true },
      { id: "s-03", sizeName: "L", price: 42000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-01", name: "Thêm Shot Espresso", priceAdjustment: 10000, isDefault: false },
      { id: "mod-02", name: "Thêm Kem Muối Béo", priceAdjustment: 8000, isDefault: false },
    ],
  },
  {
    id: "prod-02",
    sku: "TEA-PEACH-02",
    name: "Trà Đào Cam Sả Tươi",
    description: "Trà đen ủ lạnh cao cấp kết hợp miếng đào giòn ngọt và tinh dầu sả tươi.",
    basePrice: 39000,
    imageUrl: "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    categoryId: "cat-02",
    categoryName: "Trà Trái Cây",
    isAvailable: true,
    isBestSeller: true,
    sizes: [
      { id: "s-04", sizeName: "M", price: 39000, isDefault: true },
      { id: "s-05", sizeName: "L", price: 45000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-03", name: "Thêm Đào Miếng Giòn (2 miếng)", priceAdjustment: 10000, isDefault: false },
      { id: "mod-04", name: "Thêm Thạch Nha Đam", priceAdjustment: 6000, isDefault: false },
    ],
  },
  {
    id: "prod-03",
    sku: "MILKTEA-OOLONG-03",
    name: "Trà Sữa Oolong Nướng",
    description: "Trà Oolong nướng than đượm hương khói hòa quyện sữa tươi New Zealand.",
    basePrice: 42000,
    imageUrl: "https://images.unsplash.com/photo-1558857563-b37cf05d8a58?w=400&q=80",
    categoryId: "cat-03",
    categoryName: "Trà Sữa Oolong",
    isAvailable: true,
    sizes: [
      { id: "s-06", sizeName: "M", price: 42000, isDefault: true },
      { id: "s-07", sizeName: "L", price: 49000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-05", name: "Trân Châu Hoàng Kim", priceAdjustment: 8000, isDefault: false },
      { id: "mod-06", name: "Pudding Trứng", priceAdjustment: 8000, isDefault: false },
    ],
  },
  {
    id: "prod-04",
    sku: "CF-BACXIU-04",
    name: "Bạc Xỉu Sữa Hạnh Nhân",
    description: "Bạc xỉu 3 tầng thơm béo hạt hạnh nhân rang, ít ngọt thanh lịch.",
    basePrice: 38000,
    imageUrl: "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&q=80",
    categoryId: "cat-01",
    categoryName: "Cà Phê Đặc Sản",
    isAvailable: true,
    sizes: [
      { id: "s-08", sizeName: "M", price: 38000, isDefault: true },
      { id: "s-09", sizeName: "L", price: 45000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-07", name: "Đổi Sữa Yến Mạch Oatly", priceAdjustment: 12000, isDefault: false },
    ],
  },
  {
    id: "prod-05",
    sku: "PASTRY-CROISSANT-05",
    name: "Bánh Croissant Bơ Tỏi Phô Mai",
    description: "Bánh sừng bò nướng nóng giòn tan với bơ tỏi thơm lừng và phô mai kéo sợi.",
    basePrice: 32000,
    imageUrl: "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=400&q=80",
    categoryId: "cat-05",
    categoryName: "Bánh Ngọt & Pastry",
    isAvailable: true,
    sizes: [{ id: "s-10", sizeName: "Regular", price: 32000, isDefault: true }],
    modifiers: [],
  },
];

export default function TableMenuPage() {
  const params = useParams();
  const router = useRouter();
  const tableId = (params?.tableId as string) || "01";

  const setTableAndBranch = useCartStore((state) => state.setTableAndBranch);
  const addItem = useCartStore((state) => state.addItem);
  const totalAmount = useCartStore((state) => state.getTotalAmount());
  const itemsCount = useCartStore((state) => state.getTotalItemsCount());

  const [selectedCategory, setSelectedCategory] = useState("cat-all");
  const [search, setSearch] = useState("");
  const [customizingProduct, setCustomizingProduct] = useState<ProductDto | null>(null);

  useEffect(() => {
    setTableAndBranch(tableId, tableId, "branch-q1");
  }, [tableId, setTableAndBranch]);

  const filteredProducts = mockProducts.filter((p) => {
    const matchCategory = selectedCategory === "cat-all" || p.categoryId === selectedCategory;
    const matchSearch =
      p.name.toLowerCase().includes(search.toLowerCase()) ||
      (p.description && p.description.toLowerCase().includes(search.toLowerCase()));
    return matchCategory && matchSearch;
  });

  return (
    <div className="space-y-5 px-4 pt-4">
      {/* Header identification */}
      <div className="bg-gradient-to-r from-amber-700 to-amber-900 text-white rounded-3xl p-5 shadow-lg space-y-2 relative overflow-hidden">
        <div className="absolute right-[-20px] top-[-20px] opacity-10">
          <Coffee className="w-36 h-36" />
        </div>
        <div className="flex items-center justify-between">
          <span className="text-xs uppercase font-bold tracking-widest text-amber-200">
            Dine-In Menu • Quét QR Bàn
          </span>
          <span className="bg-white/20 backdrop-blur text-white text-xs font-black px-3 py-1 rounded-full border border-white/30">
            BÀN #{tableId}
          </span>
        </div>
        <h2 className="text-xl font-black">Smart F&B Coffee & Tea</h2>
        <p className="text-xs text-amber-100/90 leading-relaxed">
          Quý khách chọn món bên dưới, chọn thanh toán VietQR trả trước hoặc Tiền mặt trả sau tại bước giỏ hàng.
        </p>
      </div>

      {/* AI-1 Weather Recommender Banner */}
      <div
        onClick={() => router.push("/ai-chat")}
        className="bg-amber-50 border border-amber-200/80 rounded-2xl p-3.5 flex items-center justify-between cursor-pointer hover:bg-amber-100/70 transition-colors shadow-2xs"
      >
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-amber-600 text-white flex items-center justify-center shadow-xs">
            <Sparkles className="h-5 w-5" />
          </div>
          <div>
            <span className="text-xs font-bold text-amber-950 block">
              Gợi Ý Món AI-1 Hôm Nay (32°C Nắng)
            </span>
            <span className="text-[11px] text-amber-800">
              Đề xuất: <strong>Trà Đào Cam Sả</strong> & <strong>Cà Phê Muối</strong>
            </span>
          </div>
        </div>
        <ArrowRight className="h-4 w-4 text-amber-700 shrink-0" />
      </div>

      {/* Search Input */}
      <SearchInput
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        onClear={() => setSearch("")}
        placeholder="Tìm đồ uống, cà phê, trà trái cây..."
      />

      {/* Horizontal Category Scroll Tabs */}
      <div className="flex gap-2 overflow-x-auto pb-1 no-scrollbar">
        {initialCategories.map((cat) => {
          const isSelected = selectedCategory === cat.id;
          return (
            <button
              key={cat.id}
              onClick={() => setSelectedCategory(cat.id)}
              className={`px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap transition-all min-h-[40px] shrink-0 ${
                isSelected
                  ? "bg-amber-700 text-white shadow-sm"
                  : "bg-white border border-slate-200 text-slate-700 hover:bg-slate-50"
              }`}
            >
              {cat.name}
            </button>
          );
        })}
      </div>

      {/* Products Grid / Cards */}
      <div className="space-y-3.5">
        {filteredProducts.map((product) => (
          <div
            key={product.id}
            onClick={() => setCustomizingProduct(product)}
            className="bg-white rounded-2xl p-3.5 border border-slate-200 shadow-2xs hover:shadow-md transition-all flex gap-3.5 cursor-pointer"
          >
            {/* Product Image */}
            <div className="relative w-24 h-24 rounded-xl overflow-hidden bg-slate-100 shrink-0 border border-slate-100">
              <img
                src={product.imageUrl}
                alt={product.name}
                className="w-full h-full object-cover"
              />
              {product.isBestSeller && (
                <span className="absolute top-1 left-1 bg-amber-600 text-white text-[9px] font-black px-1.5 py-0.5 rounded shadow-xs flex items-center gap-0.5">
                  <Flame className="h-2.5 w-2.5 fill-current" />
                  HOT
                </span>
              )}
            </div>

            {/* Info */}
            <div className="flex-1 flex flex-col justify-between">
              <div>
                <h4 className="font-bold text-sm text-slate-900 line-clamp-1">{product.name}</h4>
                <p className="text-[11px] text-slate-500 line-clamp-2 mt-0.5 leading-tight">
                  {product.description}
                </p>
              </div>

              <div className="flex items-center justify-between pt-1">
                <span className="font-extrabold text-sm text-amber-800">
                  {formatCurrencyVND(product.basePrice)}
                </span>
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    setCustomizingProduct(product);
                  }}
                  className="w-8 h-8 rounded-lg bg-amber-700 text-white flex items-center justify-center hover:bg-amber-800 shadow-sm active:scale-95 transition-all"
                >
                  <Plus className="h-4 w-4" />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Floating Bottom Cart Bar */}
      {itemsCount > 0 && (
        <div className="fixed bottom-4 left-4 right-4 max-w-md mx-auto z-40">
          <button
            type="button"
            onClick={() => router.push("/cart")}
            className="w-full bg-amber-700 hover:bg-amber-800 text-white p-4 rounded-2xl shadow-xl flex items-center justify-between transition-all active:scale-[0.99]"
          >
            <div className="flex items-center gap-3">
              <div className="relative">
                <ShoppingBag className="h-6 w-6" />
                <span className="absolute -top-2 -right-2 w-5 h-5 bg-rose-500 text-white rounded-full flex items-center justify-center text-[10px] font-black border-2 border-amber-700">
                  {itemsCount}
                </span>
              </div>
              <div className="text-left">
                <span className="text-xs text-amber-200 block leading-tight">Bàn #{tableId}</span>
                <span className="font-extrabold text-base">{formatCurrencyVND(totalAmount)}</span>
              </div>
            </div>

            <div className="flex items-center gap-1.5 font-bold text-sm bg-amber-600/80 px-3.5 py-1.5 rounded-xl border border-amber-500/50">
              <span>Xem Giỏ Hàng</span>
              <ArrowRight className="h-4 w-4" />
            </div>
          </button>
        </div>
      )}

      {/* Customization Drawer Modal */}
      <CustomizationDrawer
        isOpen={!!customizingProduct}
        onClose={() => setCustomizingProduct(null)}
        product={customizingProduct}
        onAddToCart={(item) => {
          addItem(item);
        }}
      />
    </div>
  );
}
