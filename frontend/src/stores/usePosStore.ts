import { create } from "zustand";
import { CustomerDto, OrderItemDto } from "@/types";

interface PosState {
  currentCustomer: CustomerDto | null;
  items: OrderItemDto[];
  setCurrentCustomer: (customer: CustomerDto | null) => void;
  addItem: (item: OrderItemDto) => void;
  removeItem: (productId: string, size: string) => void;
  clearPos: () => void;
  getSubTotal: () => number;
}

export const usePosStore = create<PosState>((set, get) => ({
  currentCustomer: null,
  items: [],
  setCurrentCustomer: (customer) => set({ currentCustomer: customer }),
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
  clearPos: () => set({ currentCustomer: null, items: [] }),
  getSubTotal: () => get().items.reduce((sum, i) => sum + i.totalPrice, 0),
}));
