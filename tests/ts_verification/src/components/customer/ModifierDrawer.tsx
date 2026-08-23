"use client";

// ============================================================================
// File: src/components/customer/ModifierDrawer.tsx
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Drawer tùy biến chọn size, đường, đá, topping và ghi chú món.
// Đạt chuẩn tiếp cận WCAG 2.1 AA với touch target >= 44px.
// ============================================================================

import React, { useState } from "react";
import {
  Drawer,
  DrawerContent,
  DrawerHeader,
  DrawerTitle,
  DrawerFooter,
  DrawerDescription
} from "@/components/ui/drawer";
import { Button } from "@/components/ui/button";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Checkbox } from "@/components/ui/checkbox";
import { Textarea } from "@/components/ui/textarea";
import { useCartStore } from "@/stores/useCartStore";
import { formatVndCurrency } from "@/lib/utils/formatters";

export interface ItemSize {
  id: string;
  name: string;
  price: number;
}

export interface ItemTopping {
  id: string;
  name: string;
  price: number;
}

export interface MenuItemDetail {
  id: string;
  name: string;
  description: string;
  imageUrl: string;
  sizes: ItemSize[];
  toppings: ItemTopping[];
}

interface ModifierDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  item: MenuItemDetail;
}

export const ModifierDrawer: React.FC<ModifierDrawerProps> = ({ isOpen, onClose, item }) => {
  const [selectedSize, setSelectedSize] = useState<ItemSize>(item.sizes[0]);
  const [selectedSweetness, setSelectedSweetness] = useState<string>("100%");
  const [selectedIce, setSelectedIce] = useState<string>("100%");
  const [selectedToppings, setSelectedToppings] = useState<ItemTopping[]>([]);
  const [quantity, setQuantity] = useState<number>(1);
  const [specialNote, setSpecialNote] = useState<string>("");

  const addItem = useCartStore((state) => state.addItem);

  const calculateItemTotal = (): number => {
    const toppingTotal = selectedToppings.reduce((sum, t) => sum + t.price, 0);
    return (selectedSize.price + toppingTotal) * quantity;
  };

  const handleToggleTopping = (topping: ItemTopping) => {
    setSelectedToppings((prev) =>
      prev.some((t) => t.id === topping.id)
        ? prev.filter((t) => t.id !== topping.id)
        : [...prev, topping]
    );
  };

  const handleAddToCart = () => {
    const toppingTotal = selectedToppings.reduce((sum, t) => sum + t.price, 0);
    addItem({
      menuItemId: item.id,
      name: item.name,
      size: selectedSize,
      sweetness: selectedSweetness,
      ice: selectedIce,
      toppings: selectedToppings,
      quantity,
      note: specialNote.trim() || undefined,
      unitPrice: selectedSize.price + toppingTotal
    });
    onClose();
  };

  return (
    <Drawer open={isOpen} onOpenChange={(open) => !open && onClose()}>
      <DrawerContent className="bg-neutral-900 border-t border-neutral-800 text-neutral-100 max-h-[90vh]">
        <DrawerHeader className="border-b border-neutral-800 pb-3 text-left">
          <DrawerTitle className="text-xl font-bold text-emerald-400">{item.name}</DrawerTitle>
          <DrawerDescription className="text-sm text-neutral-400">{item.description}</DrawerDescription>
        </DrawerHeader>

        <div className="overflow-y-auto px-4 py-4 space-y-6">
          {/* Lựa chọn Kích cỡ (Size) */}
          <section aria-labelledby="size-heading">
            <h4 id="size-heading" className="text-xs font-bold uppercase tracking-wider text-neutral-400 mb-3">
              1. Chọn Kích Cỡ (Bắt buộc)
            </h4>
            <RadioGroup
              value={selectedSize.id}
              onValueChange={(id) => {
                const size = item.sizes.find((s) => s.id === id);
                if (size) setSelectedSize(size);
              }}
              className="space-y-2"
            >
              {item.sizes.map((size) => (
                <label
                  key={size.id}
                  htmlFor={`size-${size.id}`}
                  className="flex items-center justify-between p-3.5 rounded-xl border border-neutral-800 bg-neutral-950 cursor-pointer min-h-[48px] hover:border-emerald-500/50 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <RadioGroupItem value={size.id} id={`size-${size.id}`} />
                    <span className="font-medium text-sm">{size.name}</span>
                  </div>
                  <span className="text-sm text-emerald-400 font-semibold">{formatVndCurrency(size.price)}</span>
                </label>
              ))}
            </RadioGroup>
          </section>

          {/* Lựa chọn Mức đường */}
          <section aria-labelledby="sweetness-heading">
            <h4 id="sweetness-heading" className="text-xs font-bold uppercase tracking-wider text-neutral-400 mb-3">
              2. Mức Đường
            </h4>
            <div className="grid grid-cols-4 gap-2">
              {["0%", "30%", "70%", "100%"].map((level) => (
                <Button
                  key={level}
                  type="button"
                  variant={selectedSweetness === level ? "default" : "outline"}
                  className={`min-h-[44px] font-medium text-sm ${
                    selectedSweetness === level
                      ? "bg-emerald-600 hover:bg-emerald-500 text-white"
                      : "border-neutral-800 bg-neutral-950 text-neutral-300"
                  }`}
                  onClick={() => setSelectedSweetness(level)}
                >
                  {level}
                </Button>
              ))}
            </div>
          </section>

          {/* Lựa chọn Mức đá */}
          <section aria-labelledby="ice-heading">
            <h4 id="ice-heading" className="text-xs font-bold uppercase tracking-wider text-neutral-400 mb-3">
              3. Mức Đá
            </h4>
            <div className="grid grid-cols-4 gap-2">
              {["0%", "30%", "70%", "100%"].map((level) => (
                <Button
                  key={level}
                  type="button"
                  variant={selectedIce === level ? "default" : "outline"}
                  className={`min-h-[44px] font-medium text-sm ${
                    selectedIce === level
                      ? "bg-emerald-600 hover:bg-emerald-500 text-white"
                      : "border-neutral-800 bg-neutral-950 text-neutral-300"
                  }`}
                  onClick={() => setSelectedIce(level)}
                >
                  {level}
                </Button>
              ))}
            </div>
          </section>

          {/* Danh sách Toppings */}
          {item.toppings.length > 0 && (
            <section aria-labelledby="topping-heading">
              <h4 id="topping-heading" className="text-xs font-bold uppercase tracking-wider text-neutral-400 mb-3">
                4. Thêm Topping
              </h4>
              <div className="space-y-2">
                {item.toppings.map((topping) => {
                  const isChecked = selectedToppings.some((t) => t.id === topping.id);
                  return (
                    <label
                      key={topping.id}
                      htmlFor={`topping-${topping.id}`}
                      className="flex items-center justify-between p-3.5 rounded-xl border border-neutral-800 bg-neutral-950 cursor-pointer min-h-[48px] hover:border-emerald-500/50 transition-colors"
                    >
                      <div className="flex items-center gap-3">
                        <Checkbox
                          id={`topping-${topping.id}`}
                          checked={isChecked}
                          onCheckedChange={() => handleToggleTopping(topping)}
                        />
                        <span className="text-sm font-medium">{topping.name}</span>
                      </div>
                      <span className="text-sm text-neutral-300">+{formatVndCurrency(topping.price)}</span>
                    </label>
                  );
                })}
              </div>
            </section>
          )}

          {/* Ghi chú đặc biệt */}
          <section aria-labelledby="note-heading">
            <h4 id="note-heading" className="text-xs font-bold uppercase tracking-wider text-neutral-400 mb-2">
              5. Ghi Chú Riêng Cho Món
            </h4>
            <Textarea
              placeholder="Vd: Ít sữa đặc, uống nóng, tách đá riêng..."
              value={specialNote}
              onChange={(e) => setSpecialNote(e.target.value)}
              maxLength={200}
              className="bg-neutral-950 border-neutral-800 text-neutral-100 text-sm min-h-[70px]"
            />
          </section>

          {/* Số lượng */}
          <section className="flex items-center justify-between pt-2 border-t border-neutral-800">
            <span className="font-semibold text-sm text-neutral-200">Số lượng:</span>
            <div className="flex items-center gap-3">
              <Button
                type="button"
                size="icon"
                variant="outline"
                className="h-11 w-11 rounded-full border-neutral-700 bg-neutral-900 text-xl font-bold"
                onClick={() => setQuantity((q) => Math.max(1, q - 1))}
                disabled={quantity <= 1}
                aria-label="Giảm số lượng"
              >
                -
              </Button>
              <span className="w-8 text-center font-bold text-lg">{quantity}</span>
              <Button
                type="button"
                size="icon"
                variant="outline"
                className="h-11 w-11 rounded-full border-neutral-700 bg-neutral-900 text-xl font-bold"
                onClick={() => setQuantity((q) => Math.min(20, q + 1))}
                disabled={quantity >= 20}
                aria-label="Tăng số lượng"
              >
                +
              </Button>
            </div>
          </section>
        </div>

        <DrawerFooter className="border-t border-neutral-800 pt-3">
          <Button
            type="button"
            className="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-bold h-12 text-base shadow-lg shadow-emerald-950/50"
            onClick={handleAddToCart}
          >
            Thêm Vào Giỏ Hàng • {formatVndCurrency(calculateItemTotal())}
          </Button>
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  );
};
