import { create } from "zustand";
import { OrderItemDto, OrderType } from "@/types";

interface CartState {
  orderType: OrderType;
  tableId: string | null;
  customerPhone: string | null;
  deliveryAddress: string | null;
  items: OrderItemDto[];
  addItem: (item: OrderItemDto) => void;
  removeItem: (productId: string, size: string) => void;
  clearCart: () => void;
  setOrderType: (type: OrderType) => void;
  setTableId: (tableId: string | null) => void;
  setDeliveryInfo: (phone: string, address: string) => void;
  getTotalAmount: () => number;
}

export const useCartStore = create<CartState>((set, get) => ({
  orderType: "DineIn",
  tableId: null,
  customerPhone: null,
  deliveryAddress: null,
  items: [],
  addItem: (item) =>
    set((state) => {
      const existingIdx = state.items.findIndex(
        (i) => i.productId === item.productId && i.size === item.size
      );
      if (existingIdx > -1) {
        const updated = [...state.items];
        updated[existingIdx].quantity += item.quantity;
        updated[existingIdx].totalPrice = updated[existingIdx].quantity * updated[existingIdx].unitPrice;
        return { items: updated };
      }
      return { items: [...state.items, item] };
    }),
  removeItem: (productId, size) =>
    set((state) => ({
      items: state.items.filter(
        (i) => !(i.productId === productId && i.size === size)
      ),
    })),
  clearCart: () => set({ items: [] }),
  setOrderType: (type) => set({ orderType: type }),
  setTableId: (tableId) => set({ tableId }),
  setDeliveryInfo: (phone, address) =>
    set({ customerPhone: phone, deliveryAddress: address }),
  getTotalAmount: () => {
    const subTotal = get().items.reduce((sum, i) => sum + i.totalPrice, 0);
    const deliveryFee = get().orderType === "Delivery" ? 20000 : 0;
    return subTotal + deliveryFee;
  },
}));
