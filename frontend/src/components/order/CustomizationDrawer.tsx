"use client";

import React, { useState, useEffect } from "react";
import { ProductDto, ProductSizeDto, ProductModifierDto, SugarLevel, IceLevel } from "@/types";
import { Drawer } from "@/components/ui/Drawer";
import { Button } from "@/components/ui/Button";
import { ModifierSelector } from "./ModifierSelector";
import { formatCurrencyVND } from "@/lib/utils";
import { Plus, Minus, ShoppingBag } from "lucide-react";
import { CartItemModifier } from "@/stores/useCartStore";

export interface CustomizationDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  product: ProductDto | null;
  onAddToCart: (customizedItem: {
    productId: string;
    productName: string;
    imageUrl?: string;
    sizeId: string;
    sizeName: string;
    unitPrice: number;
    quantity: number;
    sugarLevel: SugarLevel | string;
    iceLevel: IceLevel | string;
    toppings: CartItemModifier[];
    notes?: string;
  }) => void;
}

export const CustomizationDrawer: React.FC<CustomizationDrawerProps> = ({
  isOpen,
  onClose,
  product,
  onAddToCart,
}) => {
  const [selectedSize, setSelectedSize] = useState<ProductSizeDto | null>(null);
  const [sugarLevel, setSugarLevel] = useState<SugarLevel>("100%");
  const [iceLevel, setIceLevel] = useState<IceLevel>("100%");
  const [selectedModifiers, setSelectedModifiers] = useState<ProductModifierDto[]>([]);
  const [quantity, setQuantity] = useState(1);
  const [notes, setNotes] = useState("");

  useEffect(() => {
    if (product) {
      const defaultSize = product.sizes.find((s) => s.isDefault) || product.sizes[0] || {
        id: "default-size",
        sizeName: "M",
        price: product.basePrice,
        isDefault: true,
      };
      setSelectedSize(defaultSize);
      setSugarLevel("100%");
      setIceLevel("100%");
      setSelectedModifiers([]);
      setQuantity(1);
      setNotes("");
    }
  }, [product, isOpen]);

  if (!product) return null;

  const currentBasePrice = selectedSize ? selectedSize.price : product.basePrice;
  const toppingsPrice = selectedModifiers.reduce((sum, mod) => sum + mod.priceAdjustment, 0);
  const singleItemPrice = currentBasePrice + toppingsPrice;
  const totalPrice = singleItemPrice * quantity;

  const handleToggleModifier = (mod: ProductModifierDto) => {
    setSelectedModifiers((prev) => {
      const exists = prev.some((m) => m.id === mod.id);
      if (exists) {
        return prev.filter((m) => m.id !== mod.id);
      } else {
        return [...prev, mod];
      }
    });
  };

  const handleConfirm = () => {
    if (!selectedSize) return;

    onAddToCart({
      productId: product.id,
      productName: product.name,
      imageUrl: product.imageUrl,
      sizeId: selectedSize.id,
      sizeName: selectedSize.sizeName,
      unitPrice: currentBasePrice,
      quantity,
      sugarLevel,
      iceLevel,
      toppings: selectedModifiers.map((m) => ({
        modifierId: m.id,
        name: m.name,
        price: m.priceAdjustment,
      })),
      notes: notes.trim() || undefined,
    });

    onClose();
  };

  return (
    <Drawer
      isOpen={isOpen}
      onClose={onClose}
      title={
        <div className="flex items-center gap-3">
          {product.imageUrl && (
            <img
              src={product.imageUrl}
              alt={product.name}
              className="w-10 h-10 rounded-lg object-cover border border-slate-200"
            />
          )}
          <div>
            <span className="font-bold text-slate-900 line-clamp-1">{product.name}</span>
            <span className="text-xs text-slate-500 font-normal">Tùy biến đồ uống</span>
          </div>
        </div>
      }
      footer={
        <div className="space-y-3">
          {/* Quantity Controls & Price Summary */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3 bg-slate-100 p-1 rounded-xl">
              <button
                type="button"
                onClick={() => setQuantity((q) => Math.max(1, q - 1))}
                className="w-8 h-8 rounded-lg bg-white flex items-center justify-center text-slate-700 shadow-sm disabled:opacity-50"
                disabled={quantity <= 1}
              >
                <Minus className="h-4 w-4" />
              </button>
              <span className="font-bold text-sm text-slate-900 w-6 text-center">{quantity}</span>
              <button
                type="button"
                onClick={() => setQuantity((q) => q + 1)}
                className="w-8 h-8 rounded-lg bg-white flex items-center justify-center text-slate-700 shadow-sm"
              >
                <Plus className="h-4 w-4" />
              </button>
            </div>

            <div className="text-right">
              <span className="text-xs text-slate-400 block">Thành tiền</span>
              <span className="text-lg font-extrabold text-amber-800">
                {formatCurrencyVND(totalPrice)}
              </span>
            </div>
          </div>

          {/* Add to Cart CTA */}
          <Button
            type="button"
            onClick={handleConfirm}
            size="lg"
            variant="primary"
            className="w-full font-bold shadow-md"
            leftIcon={<ShoppingBag className="h-5 w-5" />}
          >
            Thêm Vào Giỏ • {formatCurrencyVND(totalPrice)}
          </Button>
        </div>
      }
    >
      <div className="space-y-6">
        <ModifierSelector
          sizes={product.sizes}
          selectedSizeId={selectedSize?.id || ""}
          onSelectSize={setSelectedSize}
          sugarLevel={sugarLevel}
          onSelectSugar={setSugarLevel}
          iceLevel={iceLevel}
          onSelectIce={setIceLevel}
          availableModifiers={product.modifiers}
          selectedModifierIds={selectedModifiers.map((m) => m.id)}
          onToggleModifier={handleToggleModifier}
        />

        {/* Special Instructions / Notes */}
        <div className="space-y-1.5 pt-2">
          <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
            5. Ghi Chú Đặc Biệt Cho Barista
          </label>
          <input
            type="text"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder="Ví dụ: Ít ngọt, mang ly giữ nhiệt..."
            className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-amber-600"
          />
        </div>
      </div>
    </Drawer>
  );
};
