import { create } from "zustand";
import { OrderType, PaymentMethod, SugarLevel, IceLevel, ProductSizeName } from "@/types";

export interface CartItemModifier {
  modifierId: string;
  name: string;
  price: number;
}

export interface CartItem {
  cartItemId: string;
  productId: string;
  productName: string;
  imageUrl?: string;
  sizeId: string;
  sizeName: ProductSizeName | string;
  unitPrice: number;
  quantity: number;
  sugarLevel: SugarLevel | string;
  iceLevel: IceLevel | string;
  toppings: CartItemModifier[];
  notes?: string;
  totalItemPrice: number;
}

interface CartState {
  tableId: string | null;
  tableNumber: string | null;
  branchId: string | null;
  orderType: OrderType;
  items: CartItem[];
  voucherCode: string | null;
  discountAmount: number;
  deliveryFee: number;
  paymentMethod: PaymentMethod;
  recipientName: string;
  recipientPhone: string;
  deliveryAddress: string;
  shipperNotes: string;

  // Actions
  setTableAndBranch: (tableId: string | null, tableNumber: string | null, branchId: string) => void;
  setOrderType: (type: OrderType) => void;
  addItem: (item: Omit<CartItem, "cartItemId" | "totalItemPrice">) => void;
  updateItemQuantity: (cartItemId: string, delta: number) => void;
  removeItem: (cartItemId: string) => void;
  applyVoucher: (code: string, discount: number) => void;
  removeVoucher: () => void;
  setPaymentMethod: (method: PaymentMethod) => void;
  setDeliveryInfo: (info: {
    recipientName: string;
    recipientPhone: string;
    deliveryAddress: string;
    shipperNotes?: string;
  }) => void;
  clearCart: () => void;

  // Computed / Selectors
  getSubtotal: () => number;
  getTotalAmount: () => number;
  getTotalItemsCount: () => number;
}

const DEFAULT_DELIVERY_FEE = 20000;

export const useCartStore = create<CartState>((set, get) => ({
  tableId: null,
  tableNumber: null,
  branchId: "default-branch",
  orderType: "DineIn",
  items: [],
  voucherCode: null,
  discountAmount: 0,
  deliveryFee: 0,
  paymentMethod: "VIETQR",
  recipientName: "",
  recipientPhone: "",
  deliveryAddress: "",
  shipperNotes: "",

  setTableAndBranch: (tableId, tableNumber, branchId) =>
    set({
      tableId,
      tableNumber,
      branchId,
      orderType: tableId ? "DineIn" : "Delivery",
      deliveryFee: tableId ? 0 : DEFAULT_DELIVERY_FEE,
    }),

  setOrderType: (type) =>
    set((state) => ({
      orderType: type,
      deliveryFee: type === "Delivery" ? DEFAULT_DELIVERY_FEE : 0,
      paymentMethod: type === "Delivery" ? "VIETQR" : state.paymentMethod, // Delivery is 100% VietQR prepaid
    })),

  addItem: (itemData) => {
    const toppingsTotal = itemData.toppings.reduce((sum, t) => sum + t.price, 0);
    const itemSinglePrice = itemData.unitPrice + toppingsTotal;
    const totalItemPrice = itemSinglePrice * itemData.quantity;

    const cartItemId = `${itemData.productId}-${itemData.sizeId}-${itemData.sugarLevel}-${itemData.iceLevel}-${itemData.toppings
      .map((t) => t.modifierId)
      .sort()
      .join("_")}-${itemData.notes || ""}`;

    set((state) => {
      const existingIndex = state.items.findIndex((i) => i.cartItemId === cartItemId);
      if (existingIndex > -1) {
        const updated = [...state.items];
        const newQty = updated[existingIndex].quantity + itemData.quantity;
        updated[existingIndex] = {
          ...updated[existingIndex],
          quantity: newQty,
          totalItemPrice: itemSinglePrice * newQty,
        };
        return { items: updated };
      }

      return {
        items: [
          ...state.items,
          {
            ...itemData,
            cartItemId,
            totalItemPrice,
          },
        ],
      };
    });
  },

  updateItemQuantity: (cartItemId, delta) => {
    set((state) => {
      const updated = state.items
        .map((item) => {
          if (item.cartItemId === cartItemId) {
            const newQty = item.quantity + delta;
            if (newQty <= 0) return null;
            const singlePrice = item.unitPrice + item.toppings.reduce((sum, t) => sum + t.price, 0);
            return {
              ...item,
              quantity: newQty,
              totalItemPrice: singlePrice * newQty,
            };
          }
          return item;
        })
        .filter((item): item is CartItem => item !== null);

      return { items: updated };
    });
  },

  removeItem: (cartItemId) =>
    set((state) => ({
      items: state.items.filter((i) => i.cartItemId !== cartItemId),
    })),

  applyVoucher: (code, discount) =>
    set({
      voucherCode: code,
      discountAmount: discount,
    }),

  removeVoucher: () =>
    set({
      voucherCode: null,
      discountAmount: 0,
    }),

  setPaymentMethod: (method) => set({ paymentMethod: method }),

  setDeliveryInfo: (info) =>
    set({
      recipientName: info.recipientName,
      recipientPhone: info.recipientPhone,
      deliveryAddress: info.deliveryAddress,
      shipperNotes: info.shipperNotes || "",
      orderType: "Delivery",
      deliveryFee: DEFAULT_DELIVERY_FEE,
      paymentMethod: "VIETQR", // Locked 100% VietQR for delivery
    }),

  clearCart: () =>
    set({
      items: [],
      voucherCode: null,
      discountAmount: 0,
    }),

  getSubtotal: () => {
    return get().items.reduce((sum, item) => sum + item.totalItemPrice, 0);
  },

  getTotalAmount: () => {
    const subtotal = get().getSubtotal();
    const discount = get().discountAmount;
    const fee = get().deliveryFee;
    return Math.max(0, subtotal - discount + fee);
  },

  getTotalItemsCount: () => {
    return get().items.reduce((sum, item) => sum + item.quantity, 0);
  },
}));
