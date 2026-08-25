import { create } from "zustand";
import { TableDto, TableStatus } from "@/types";

interface TableState {
  tables: TableDto[];
  selectedFloor: number;
  floors: number[];

  // Actions
  setTables: (tables: TableDto[]) => void;
  updateTableStatus: (tableId: string, status: TableStatus, extra?: Partial<TableDto>) => void;
  setSelectedFloor: (floor: number) => void;
  resolveServiceCall: (tableId: string) => void;
  getTablesForSelectedFloor: () => TableDto[];
  getServiceAlertsCount: () => number;
}

export const useTableStore = create<TableState>((set, get) => ({
  tables: [],
  selectedFloor: 1,
  floors: [1, 2, 3],

  setTables: (tables) => {
    const floorsSet = new Set<number>(tables.map((t) => t.floor || 1));
    const sortedFloors = Array.from(floorsSet).sort((a, b) => a - b);
    set({
      tables,
      floors: sortedFloors.length > 0 ? sortedFloors : [1],
      selectedFloor: sortedFloors.length > 0 ? sortedFloors[0] : 1,
    });
  },

  updateTableStatus: (tableId, status, extra) =>
    set((state) => ({
      tables: state.tables.map((t) =>
        t.id === tableId
          ? {
              ...t,
              status,
              ...extra,
            }
          : t
      ),
    })),

  setSelectedFloor: (floor) => set({ selectedFloor: floor }),

  resolveServiceCall: (tableId) =>
    set((state) => ({
      tables: state.tables.map((t) =>
        t.id === tableId
          ? {
              ...t,
              status: t.activeOrderId ? "Occupied_Paid" : "Available",
              serviceRequestedAt: undefined,
            }
          : t
      ),
    })),

  getTablesForSelectedFloor: () => {
    const { tables, selectedFloor } = get();
    return tables.filter((t) => (t.floor || 1) === selectedFloor);
  },

  getServiceAlertsCount: () => {
    return get().tables.filter((t) => t.status === "ServiceRequested").length;
  },
}));
