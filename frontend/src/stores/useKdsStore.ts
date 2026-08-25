import { create } from "zustand";
import { KdsTicketDto, BatchItemSummary } from "@/types";

interface KdsState {
  tickets: KdsTicketDto[];
  stationFilter: "ALL" | "BAR" | "KITCHEN";
  batchMode: boolean;
  soundEnabled: boolean;
  selectedTicket: KdsTicketDto | null;

  // Actions
  setTickets: (tickets: KdsTicketDto[]) => void;
  addTicket: (ticket: KdsTicketDto) => void;
  updateTicketStatus: (orderId: string, status: "Pending" | "Preparing" | "Ready") => void;
  removeTicket: (orderId: string) => void;
  setStationFilter: (filter: "ALL" | "BAR" | "KITCHEN") => void;
  toggleBatchMode: () => void;
  toggleSound: () => void;
  setSelectedTicket: (ticket: KdsTicketDto | null) => void;
  incrementTimers: () => void;

  // Selectors
  getFilteredTickets: () => KdsTicketDto[];
  getBatchSummaries: () => BatchItemSummary[];
}

export const useKdsStore = create<KdsState>((set, get) => ({
  tickets: [],
  stationFilter: "ALL",
  batchMode: false,
  soundEnabled: true,
  selectedTicket: null,

  setTickets: (tickets) => set({ tickets }),

  addTicket: (ticket) =>
    set((state) => {
      const exists = state.tickets.some((t) => t.orderId === ticket.orderId);
      if (exists) return state;
      return { tickets: [ticket, ...state.tickets] };
    }),

  updateTicketStatus: (orderId, status) =>
    set((state) => ({
      tickets: state.tickets.map((t) => (t.orderId === orderId ? { ...t, status } : t)),
    })),

  removeTicket: (orderId) =>
    set((state) => ({
      tickets: state.tickets.filter((t) => t.orderId !== orderId),
      selectedTicket: state.selectedTicket?.orderId === orderId ? null : state.selectedTicket,
    })),

  setStationFilter: (filter) => set({ stationFilter: filter }),

  toggleBatchMode: () => set((state) => ({ batchMode: !state.batchMode })),

  toggleSound: () => set((state) => ({ soundEnabled: !state.soundEnabled })),

  setSelectedTicket: (ticket) => set({ selectedTicket: ticket }),

  incrementTimers: () =>
    set((state) => ({
      tickets: state.tickets.map((t) => ({
        ...t,
        elapsedSeconds: t.elapsedSeconds + 1,
      })),
    })),

  getFilteredTickets: () => {
    const { tickets, stationFilter } = get();
    if (stationFilter === "ALL") return tickets;
    return tickets.filter((t) => t.station === stationFilter || t.station === "ALL");
  },

  getBatchSummaries: () => {
    const { tickets } = get();
    // Only group Pending and Preparing tickets
    const activeTickets = tickets.filter((t) => t.status === "Pending" || t.status === "Preparing");
    const summaryMap = new Map<string, BatchItemSummary>();

    activeTickets.forEach((ticket) => {
      ticket.items.forEach((item) => {
        const key = `${item.productId}-${item.sizeName}`;
        if (!summaryMap.has(key)) {
          summaryMap.set(key, {
            productId: item.productId,
            productName: item.productName,
            sizeName: item.sizeName,
            totalQuantity: 0,
            orderCount: 0,
            orderIds: [],
            sugarLevels: {},
            iceLevels: {},
          });
        }

        const summary = summaryMap.get(key)!;
        summary.totalQuantity += item.quantity;
        if (!summary.orderIds.includes(ticket.orderId)) {
          summary.orderIds.push(ticket.orderId);
          summary.orderCount += 1;
        }

        // Tally sugar & ice levels
        const sugar = item.sugarLevel || "100%";
        summary.sugarLevels[sugar] = (summary.sugarLevels[sugar] || 0) + item.quantity;

        const ice = item.iceLevel || "100%";
        summary.iceLevels[ice] = (summary.iceLevels[ice] || 0) + item.quantity;
      });
    });

    return Array.from(summaryMap.values()).sort((a, b) => b.totalQuantity - a.totalQuantity);
  },
}));
