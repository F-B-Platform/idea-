// ============================================================================
// File: src/stores/useCartStore.ts
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Zustand Store Slice quản lý trạng thái giỏ hàng khách hàng.
// Tích hợp middleware persist lưu trữ LocalStorage và tự động tính toán phí ship 20.000 VND.
// ============================================================================

import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

export interface CartItem {
  id: string; // Khóa định danh duy nhất của dòng món trong giỏ (UUID)
  menuItemId: string;
  name: string;
  size: { id: string; name: string; price: number };
  sweetness: string;
  ice: string;
  toppings: Array<{ id: string; name: string; price: number }>;
  quantity: number;
  note?: string;
  unitPrice: number;
}

interface CartState {
  items: CartItem[];
  branchId: string | null;
  tableId: string | null;
  tableCode: string | null;
  deliveryAddress: string | null;
  customerPhone: string | null;
  shippingFee: number;
  orderChannel: "DineIn" | "Delivery" | "TakeAway";

  // Actions
  setDineInContext: (branchId: string, tableId: string, tableCode: string) => void;
  setDeliveryContext: (branchId: string, phone: string, address: string) => void;
  setTakeAwayContext: (branchId: string, phone?: string) => void;
  addItem: (item: Omit<CartItem, "id">) => void;
  removeItem: (id: string) => void;
  updateQuantity: (id: string, delta: number) => void;
  clearCart: () => void;

  // Selectors
  getSubTotal: () => number;
  getTotalAmount: () => number;
  getItemCount: () => number;
}

export const useCartStore = create<CartState>()(
  persist(
    (set, get) => ({
      items: [],
      branchId: null,
      tableId: null,
      tableCode: null,
      deliveryAddress: null,
      customerPhone: null,
      shippingFee: 0,
      orderChannel: "DineIn",

      setDineInContext: (branchId, tableId, tableCode) =>
        set({
          branchId,
          tableId,
          tableCode,
          orderChannel: "DineIn",
          shippingFee: 0,
          deliveryAddress: null
        }),

      setDeliveryContext: (branchId, phone, address) =>
        set({
          branchId,
          tableId: null,
          tableCode: null,
          customerPhone: phone,
          deliveryAddress: address,
          orderChannel: "Delivery",
          shippingFee: 20000 // Cố định 20.000 VNĐ theo spec v2.5.0
        }),

      setTakeAwayContext: (branchId, phone) =>
        set({
          branchId,
          tableId: null,
          tableCode: null,
          customerPhone: phone ?? null,
          deliveryAddress: null,
          orderChannel: "TakeAway",
          shippingFee: 0
        }),

      addItem: (itemData) => {
        const state = get();
        // Kiểm tra xem món có cùng Size, Đường, Đá, Topping và Ghi chú đã có trong giỏ chưa
        const existingIndex = state.items.findIndex(
          (item) =>
            item.menuItemId === itemData.menuItemId &&
            item.size.id === itemData.size.id &&
            item.sweetness === itemData.sweetness &&
            item.ice === itemData.ice &&
            item.note === itemData.note &&
            JSON.stringify(item.toppings.map((t) => t.id).sort()) ===
              JSON.stringify(itemData.toppings.map((t) => t.id).sort())
        );

        if (existingIndex > -1) {
          const updatedItems = [...state.items];
          const newQty = Math.min(20, updatedItems[existingIndex].quantity + itemData.quantity);
          updatedItems[existingIndex] = {
            ...updatedItems[existingIndex],
            quantity: newQty
          };
          set({ items: updatedItems });
        } else {
          const newItem: CartItem = {
            ...itemData,
            id: crypto.randomUUID()
          };
          set({ items: [...state.items, newItem] });
        }
      },

      removeItem: (id) =>
        set((state) => ({
          items: state.items.filter((item) => item.id !== id)
        })),

      updateQuantity: (id, delta) =>
        set((state) => ({
          items: state.items
            .map((item) => {
              if (item.id === id) {
                const newQty = item.quantity + delta;
                return newQty > 0 && newQty <= 20 ? { ...item, quantity: newQty } : null;
              }
              return item;
            })
            .filter((item): item is CartItem => item !== null)
        })),

      clearCart: () => set({ items: [] }),

      getSubTotal: () => {
        return get().items.reduce((sum, item) => sum + item.unitPrice * item.quantity, 0);
      },

      getTotalAmount: () => {
        return get().getSubTotal() + get().shippingFee;
      },

      getItemCount: () => {
        return get().items.reduce((count, item) => count + item.quantity, 0);
      }
    }),
    {
      name: "smartfb-cart-storage-v250",
      storage: createJSONStorage(() => localStorage)
    }
  )
);
