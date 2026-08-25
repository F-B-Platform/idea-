"use client";

import React, { useState, useEffect } from "react";
import { useKdsStore } from "@/stores/useKdsStore";
import { KdsTicketDto } from "@/types";
import { KdsTicketCard } from "@/components/kds/KdsTicketCard";
import { BomRecipeModal } from "@/components/kds/BomRecipeModal";
import { Emergency86Modal } from "@/components/kds/Emergency86Modal";
import { BatchActionModal } from "@/components/kds/BatchActionModal";
import { useWebAudio } from "@/hooks/useWebAudio";
import { useSignalR } from "@/hooks/useSignalR";
import {
  Tv,
  Volume2,
  VolumeX,
  AlertOctagon,
  Layers,
  Clock,
  Filter,
  CheckCircle2,
  Coffee,
} from "lucide-react";

const initialTickets: KdsTicketDto[] = [
  {
    orderId: "ord-01",
    orderNumber: "ORD-0042",
    orderCode: "ORD-0042",
    orderType: "DineIn",
    tableNumber: "05",
    createdAtUtc: new Date().toISOString(),
    elapsedSeconds: 95, // 1m35s (< 3m: green)
    status: "Pending",
    paymentStatus: "Paid",
    paymentMethod: "VIETQR",
    station: "BAR",
    items: [
      {
        orderItemId: "item-01",
        productId: "prod-01",
        productName: "Cà Phê Muối Hoàng Gia",
        sizeName: "M",
        quantity: 2,
        sugarLevel: "50%",
        iceLevel: "100%",
        toppings: ["Kem Muối Béo"],
      },
      {
        orderItemId: "item-02",
        productId: "prod-02",
        productName: "Trà Đào Cam Sả Tươi",
        sizeName: "L",
        quantity: 1,
        sugarLevel: "70%",
        iceLevel: "100%",
        toppings: ["Đào Miếng Giòn"],
      },
    ],
  },
  {
    orderId: "ord-02",
    orderNumber: "TK-0089",
    orderCode: "TK-0089",
    orderType: "TakeAway",
    createdAtUtc: new Date().toISOString(),
    elapsedSeconds: 220, // 3m40s (3-5m: amber)
    status: "Preparing",
    paymentStatus: "Paid",
    paymentMethod: "CASH",
    station: "BAR",
    items: [
      {
        orderItemId: "item-03",
        productId: "prod-01",
        productName: "Cà Phê Muối Hoàng Gia",
        sizeName: "M",
        quantity: 1,
        sugarLevel: "100%",
        iceLevel: "100%",
        toppings: [],
      },
    ],
  },
  {
    orderId: "ord-03",
    orderNumber: "DEL-0015",
    orderCode: "DEL-0015",
    orderType: "Delivery",
    createdAtUtc: new Date().toISOString(),
    elapsedSeconds: 340, // 5m40s (> 5m: red pulsing)
    status: "Preparing",
    paymentStatus: "Paid",
    paymentMethod: "VIETQR",
    station: "BAR",
    items: [
      {
        orderItemId: "item-04",
        productId: "prod-03",
        productName: "Trà Sữa Oolong Nướng",
        sizeName: "L",
        quantity: 3,
        sugarLevel: "70%",
        iceLevel: "50%",
        toppings: ["Trân Châu Hoàng Kim", "Pudding Trứng"],
        notes: "Giao gấp trước 12h trưa",
      },
    ],
  },
];

export default function KitchenKdsPage() {
  const {
    tickets,
    setTickets,
    addTicket,
    updateTicketStatus,
    stationFilter,
    setStationFilter,
    soundEnabled,
    toggleSound,
    incrementTimers,
    getFilteredTickets,
    getBatchSummaries,
  } = useKdsStore();

  const { playNewTicketSound, playOverdueAlertSound } = useWebAudio();

  const [selectedBomTicket, setSelectedBomTicket] = useState<KdsTicketDto | null>(null);
  const [show86Modal, setShow86Modal] = useState(false);
  const [showBatchModal, setShowBatchModal] = useState(false);

  // Initialize initial tickets on mount
  useEffect(() => {
    if (tickets.length === 0) {
      setTickets(initialTickets);
    }
  }, [tickets.length, setTickets]);

  // Live Timer Interval (1s) & Overdue Check
  useEffect(() => {
    const timer = setInterval(() => {
      incrementTimers();

      // Check if any ticket exceeds 5 minutes (300s) and sound is enabled
      const overdueExists = tickets.some(
        (t) => t.status !== "Ready" && t.elapsedSeconds === 301
      );
      if (overdueExists && soundEnabled) {
        playOverdueAlertSound();
      }
    }, 1000);

    return () => clearInterval(timer);
  }, [incrementTimers, tickets, soundEnabled, playOverdueAlertSound]);

  // SignalR KitchenHub integration
  const { registerHandler } = useSignalR({
    hubPath: "/hubs/kitchen",
    groupName: "branch-q1",
    joinGroupMethod: "JoinKitchenGroup",
  });

  useEffect(() => {
    registerHandler("ReceiveNewTicket", (ticket: KdsTicketDto) => {
      addTicket(ticket);
      if (soundEnabled) {
        playNewTicketSound();
      }
    });

    registerHandler("TicketStatusChanged", (payload: { orderId: string; status: any }) => {
      updateTicketStatus(payload.orderId, payload.status);
    });
  }, [registerHandler, addTicket, updateTicketStatus, soundEnabled, playNewTicketSound]);

  const filteredTickets = getFilteredTickets();
  const batchSummaries = getBatchSummaries();

  const pendingCount = filteredTickets.filter((t) => t.status === "Pending").length;
  const preparingCount = filteredTickets.filter((t) => t.status === "Preparing").length;
  const overdueCount = filteredTickets.filter(
    (t) => t.status !== "Ready" && t.elapsedSeconds > 300
  ).length;

  const handleUpdateStatus = (orderId: string, newStatus: "Preparing" | "Ready") => {
    updateTicketStatus(orderId, newStatus);
    // When marking Ready: simulates backend BOM deduction and bill print for postpaid
  };

  const handleCompleteBatch = (orderIds: string[]) => {
    orderIds.forEach((id) => {
      updateTicketStatus(id, "Ready");
    });
    setShowBatchModal(false);
  };

  return (
    <div className="flex flex-col h-screen overflow-hidden bg-[#0F172A] text-slate-100">
      {/* KDS Header Bar */}
      <header className="h-16 px-6 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2.5">
            <div className="w-10 h-10 rounded-xl bg-amber-600 text-white flex items-center justify-center font-black shadow-lg">
              <Tv className="h-5 w-5" />
            </div>
            <div>
              <h1 className="text-base font-extrabold tracking-tight text-white">
                KITCHEN DISPLAY TV (KDS)
              </h1>
              <span className="text-xs text-amber-400 font-semibold">Chi nhánh Quận 1</span>
            </div>
          </div>

          {/* Station Filters */}
          <div className="flex items-center gap-1 bg-slate-800 p-1 rounded-xl border border-slate-700">
            {(["ALL", "BAR", "KITCHEN"] as const).map((st) => (
              <button
                key={st}
                onClick={() => setStationFilter(st)}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                  stationFilter === st
                    ? "bg-amber-600 text-white shadow-sm"
                    : "text-slate-400 hover:text-white"
                }`}
              >
                {st === "ALL" ? "TẤT CẢ" : st === "BAR" ? "QUẦY BAR" : "BẾP NẤU"}
              </button>
            ))}
          </div>
        </div>

        {/* Live Counters & Action Modals */}
        <div className="flex items-center gap-3">
          {/* Overdue Warning Tag */}
          {overdueCount > 0 && (
            <div className="bg-rose-600/30 text-rose-300 border border-rose-500 px-3 py-1.5 rounded-xl text-xs font-extrabold flex items-center gap-1.5 animate-pulse">
              <Clock className="h-4 w-4" />
              <span>{overdueCount} ĐƠN QUÁ HẠN 5P</span>
            </div>
          )}

          {/* Batch Mode Modal Trigger */}
          <button
            type="button"
            onClick={() => setShowBatchModal(true)}
            className="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-sky-400 font-bold text-xs rounded-xl flex items-center gap-2 transition-colors"
          >
            <Layers className="h-4 w-4" />
            <span>Gom Món ({batchSummaries.length})</span>
          </button>

          {/* 86-Toggle Modal Trigger */}
          <button
            type="button"
            onClick={() => setShow86Modal(true)}
            className="px-3.5 py-2 bg-rose-600/20 hover:bg-rose-600/30 border border-rose-500/50 text-rose-300 font-bold text-xs rounded-xl flex items-center gap-2 transition-colors"
          >
            <AlertOctagon className="h-4 w-4" />
            <span>Khóa Món 86</span>
          </button>

          {/* Audio Synthesizer Toggle */}
          <button
            type="button"
            onClick={toggleSound}
            className={`p-2 rounded-xl border transition-colors ${
              soundEnabled
                ? "bg-emerald-950/60 border-emerald-600 text-emerald-400"
                : "bg-slate-800 border-slate-700 text-slate-500"
            }`}
            title={soundEnabled ? "Tắt âm thanh chuông" : "Bật âm thanh chuông"}
          >
            {soundEnabled ? <Volume2 className="h-5 w-5" /> : <VolumeX className="h-5 w-5" />}
          </button>
        </div>
      </header>

      {/* Ticket Board Stream */}
      <main className="flex-1 overflow-x-auto overflow-y-hidden p-6">
        {filteredTickets.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-slate-500 space-y-3">
            <Coffee className="h-16 w-16 text-slate-700" />
            <h3 className="text-xl font-bold text-slate-400">Hiện không có vé đơn hàng nào</h3>
            <p className="text-xs">Các đơn hàng mới sẽ tự động xuất hiện tại đây qua SignalR WebSocket.</p>
          </div>
        ) : (
          <div className="flex gap-5 h-full items-start">
            {filteredTickets.map((ticket) => (
              <KdsTicketCard
                key={ticket.orderId}
                ticket={ticket}
                onUpdateStatus={handleUpdateStatus}
                onViewBom={setSelectedBomTicket}
              />
            ))}
          </div>
        )}
      </main>

      {/* BOM Recipe Formula Modal */}
      <BomRecipeModal
        isOpen={!!selectedBomTicket}
        onClose={() => setSelectedBomTicket(null)}
        ticket={selectedBomTicket}
      />

      {/* Emergency 86-Toggle Modal */}
      <Emergency86Modal isOpen={show86Modal} onClose={() => setShow86Modal(false)} />

      {/* Batch Preparation Modal */}
      <BatchActionModal
        isOpen={showBatchModal}
        onClose={() => setShowBatchModal(false)}
        batchSummaries={batchSummaries}
        onCompleteBatch={handleCompleteBatch}
      />
    </div>
  );
}
