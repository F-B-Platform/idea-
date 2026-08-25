import { create } from "zustand";

export const VALID_DENOMINATIONS = [500000, 200000, 100000, 50000, 20000, 10000] as const;

export type DenominationValue = (typeof VALID_DENOMINATIONS)[number];

interface ShiftState {
  currentShiftId: string | null;
  shiftCode: string;
  branchId: string;
  openingCash: number;
  cashSales: number;
  vietQrSales: number;
  theoreticalCash: number;
  denominations: Record<number, number>;
  physicalCashTotal: number;
  variance: number;
  justificationReason: string;
  isClosed: boolean;

  // Actions
  openShift: (shiftId: string, shiftCode: string, branchId: string, openingCash: number) => void;
  setTheoreticalCash: (amount: number) => void;
  setSalesAmounts: (cashSales: number, vietQrSales: number) => void;
  setDenominationCount: (denomination: number, count: number) => void;
  setJustificationReason: (reason: string) => void;
  calculatePhysicalTotalAndVariance: () => void;
  closeShift: () => void;
  resetShift: () => void;
}

const initialDenominations: Record<number, number> = {
  500000: 0,
  200000: 0,
  100000: 0,
  50000: 0,
  20000: 0,
  10000: 0,
};

export const useShiftStore = create<ShiftState>((set, get) => ({
  currentShiftId: null,
  shiftCode: "",
  branchId: "",
  openingCash: 0,
  cashSales: 0,
  vietQrSales: 0,
  theoreticalCash: 0,
  denominations: { ...initialDenominations },
  physicalCashTotal: 0,
  variance: 0,
  justificationReason: "",
  isClosed: true,

  openShift: (shiftId, shiftCode, branchId, openingCash) =>
    set({
      currentShiftId: shiftId,
      shiftCode,
      branchId,
      openingCash,
      cashSales: 0,
      vietQrSales: 0,
      theoreticalCash: openingCash,
      denominations: { ...initialDenominations },
      physicalCashTotal: 0,
      variance: -openingCash,
      justificationReason: "",
      isClosed: false,
    }),

  setTheoreticalCash: (amount) => {
    set((state) => ({
      theoreticalCash: amount,
      variance: state.physicalCashTotal - amount,
    }));
  },

  setSalesAmounts: (cashSales, vietQrSales) => {
    set((state) => {
      const theoretical = state.openingCash + cashSales;
      return {
        cashSales,
        vietQrSales,
        theoreticalCash: theoretical,
        variance: state.physicalCashTotal - theoretical,
      };
    });
  },

  setDenominationCount: (denomination, count) => {
    set((state) => {
      const updated = {
        ...state.denominations,
        [denomination]: Math.max(0, count),
      };

      const physicalTotal = Object.entries(updated).reduce((sum, [denomStr, qty]) => {
        return sum + Number(denomStr) * qty;
      }, 0);

      const variance = physicalTotal - state.theoreticalCash;

      return {
        denominations: updated,
        physicalCashTotal: physicalTotal,
        variance: variance,
      };
    });
  },

  setJustificationReason: (reason) => set({ justificationReason: reason }),

  calculatePhysicalTotalAndVariance: () => {
    const denoms = get().denominations;
    const physicalTotal = Object.entries(denoms).reduce((sum, [denomStr, qty]) => {
      return sum + Number(denomStr) * qty;
    }, 0);
    const variance = physicalTotal - get().theoreticalCash;
    set({
      physicalCashTotal: physicalTotal,
      variance,
    });
  },

  closeShift: () => set({ isClosed: true }),

  resetShift: () =>
    set({
      currentShiftId: null,
      shiftCode: "",
      branchId: "",
      openingCash: 0,
      cashSales: 0,
      vietQrSales: 0,
      theoreticalCash: 0,
      denominations: { ...initialDenominations },
      physicalCashTotal: 0,
      variance: 0,
      justificationReason: "",
      isClosed: true,
    }),
}));
