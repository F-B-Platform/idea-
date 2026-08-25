import { create } from "zustand";
import { PaymentMethod } from "@/types";
import { CartItem } from "./useCartStore";

export interface PosCustomer {
  customerId: string;
  phone: string;
  fullName: string;
  cupBalance: number;
  eligibleForFreeCup: boolean;
  totalOrdersCount?: number;
}

interface PosState {
  currentCustomer: PosCustomer | null;
  cartItems: CartItem[];
  freeCupRedeemed: boolean;
  tenderAmount: number;
  paymentMethod: PaymentMethod;
  selectedCategoryId: string | null;

  // Actions
  setCustomer: (customer: PosCustomer | null) => void;
  addItem: (item: CartItem) => void;
  updateQuantity: (cartItemId: string, qty: number) => void;
  removeItem: (cartItemId: string) => void;
  redeemFreeCup: () => void;
  cancelFreeCup: () => void;
  setTenderAmount: (amount: number) => void;
  setPaymentMethod: (method: PaymentMethod) => void;
  setSelectedCategoryId: (catId: string | null) => void;
  resetPos: () => void;

  // Computed / Selectors
  getGrossTotal: () => number;
  getDiscountTotal: () => number;
  getNetTotal: () => number;
  getChangeAmount: () => number;
}

export const usePosStore = create<PosState>((set, get) => ({
  currentCustomer: null,
  cartItems: [],
  freeCupRedeemed: false,
  tenderAmount: 0,
  paymentMethod: "CASH",
  selectedCategoryId: null,

  setCustomer: (customer) => {
    set({
      currentCustomer: customer,
      // If customer has >= 10 cups, they are eligible
      freeCupRedeemed: false,
    });
  },

  addItem: (item) => {
    set((state) => {
      const existingIndex = state.cartItems.findIndex((i) => i.cartItemId === item.cartItemId);
      if (existingIndex > -1) {
        const updated = [...state.cartItems];
        const newQty = updated[existingIndex].quantity + item.quantity;
        const singlePrice = item.unitPrice + item.toppings.reduce((s, t) => s + t.price, 0);
        updated[existingIndex] = {
          ...updated[existingIndex],
          quantity: newQty,
          totalItemPrice: singlePrice * newQty,
        };
        return { cartItems: updated };
      }
      return { cartItems: [...state.cartItems, item] };
    });
  },

  updateQuantity: (cartItemId, qty) => {
    set((state) => {
      if (qty <= 0) {
        return { cartItems: state.cartItems.filter((i) => i.cartItemId !== cartItemId) };
      }
      const updated = state.cartItems.map((item) => {
        if (item.cartItemId === cartItemId) {
          const singlePrice = item.unitPrice + item.toppings.reduce((s, t) => s + t.price, 0);
          return {
            ...item,
            quantity: qty,
            totalItemPrice: singlePrice * qty,
          };
        }
        return item;
      });
      return { cartItems: updated };
    });
  },

  removeItem: (cartItemId) => {
    set((state) => ({
      cartItems: state.cartItems.filter((i) => i.cartItemId !== cartItemId),
    }));
  },

  redeemFreeCup: () => {
    const customer = get().currentCustomer;
    if (customer && customer.cupBalance >= 10) {
      set({ freeCupRedeemed: true });
    }
  },

  cancelFreeCup: () => {
    set({ freeCupRedeemed: false });
  },

  setTenderAmount: (amount) => set({ tenderAmount: amount }),

  setPaymentMethod: (method) => set({ paymentMethod: method }),

  setSelectedCategoryId: (catId) => set({ selectedCategoryId: catId }),

  resetPos: () =>
    set({
      currentCustomer: null,
      cartItems: [],
      freeCupRedeemed: false,
      tenderAmount: 0,
      paymentMethod: "CASH",
    }),

  getGrossTotal: () => {
    return get().cartItems.reduce((sum, item) => sum + item.totalItemPrice, 0);
  },

  getDiscountTotal: () => {
    if (!get().freeCupRedeemed) return 0;
    // Free drink discount: 100% discount on 1 most expensive eligible base cup (or lowest/first) up to 35,000 VND or exact price
    const items = get().cartItems;
    if (items.length === 0) return 0;
    // Find the item with highest single price
    const highestItem = [...items].sort((a, b) => b.unitPrice - a.unitPrice)[0];
    return highestItem ? highestItem.unitPrice : 35000;
  },

  getNetTotal: () => {
    const gross = get().getGrossTotal();
    const discount = get().getDiscountTotal();
    return Math.max(0, gross - discount);
  },

  getChangeAmount: () => {
    const net = get().getNetTotal();
    const tender = get().tenderAmount;
    if (get().paymentMethod === "VIETQR") return 0;
    return Math.max(0, tender - net);
  },
}));
