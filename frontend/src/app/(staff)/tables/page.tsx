"use client";

import React, { useState, useEffect } from "react";
import { useTableStore } from "@/stores/useTableStore";
import { TableDto, TableStatus } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { useWebAudio } from "@/hooks/useWebAudio";
import { useSignalR } from "@/hooks/useSignalR";
import { Button } from "@/components/ui/Button";
import { Modal } from "@/components/ui/Modal";
import {
  LayoutGrid,
  Bell,
  CheckCircle2,
  Users,
  Coffee,
  Check,
  Plus,
  RefreshCw,
} from "lucide-react";

const initialFloorTables: TableDto[] = [
  { id: "tbl-01", tableNumber: "01", branchId: "branch-q1", floor: 1, capacity: 4, status: "Available" },
  { id: "tbl-02", tableNumber: "02", branchId: "branch-q1", floor: 1, capacity: 2, status: "Occupied_Paid", activeOrderId: "ORD-0038", activeAmount: 74000 },
  { id: "tbl-03", tableNumber: "03", branchId: "branch-q1", floor: 1, capacity: 4, status: "Occupied_PendingPayment", activeOrderId: "ORD-0040", activeAmount: 112000 },
  { id: "tbl-04", tableNumber: "04", branchId: "branch-q1", floor: 1, capacity: 6, status: "ServiceRequested", activeOrderId: "ORD-0042", activeAmount: 85000, serviceRequestedAt: new Date().toISOString() },
  { id: "tbl-05", tableNumber: "05", branchId: "branch-q1", floor: 1, capacity: 4, status: "Available" },
  { id: "tbl-06", tableNumber: "06", branchId: "branch-q1", floor: 1, capacity: 2, status: "Available" },
  { id: "tbl-07", tableNumber: "07", branchId: "branch-q1", floor: 2, capacity: 4, status: "Available" },
  { id: "tbl-08", tableNumber: "08", branchId: "branch-q1", floor: 2, capacity: 6, status: "Occupied_Paid", activeOrderId: "ORD-0035", activeAmount: 145000 },
  { id: "tbl-09", tableNumber: "09", branchId: "branch-q1", floor: 2, capacity: 4, status: "Available" },
];

export default function TablesManagementPage() {
  const {
    tables,
    setTables,
    selectedFloor,
    setSelectedFloor,
    updateTableStatus,
    resolveServiceCall,
    getTablesForSelectedFloor,
    getServiceAlertsCount,
  } = useTableStore();

  const { playServiceCallSound } = useWebAudio();
  const [selectedTable, setSelectedTable] = useState<TableDto | null>(null);

  useEffect(() => {
    if (tables.length === 0) {
      setTables(initialFloorTables);
    }
  }, [tables.length, setTables]);

  // SignalR NotificationHub for ServiceRequested events
  const { registerHandler } = useSignalR({
    hubPath: "/hubs/notifications",
    groupName: "branch-q1",
    joinGroupMethod: "JoinBranchNotifications",
  });

  useEffect(() => {
    registerHandler("ServiceRequested", (data: { tableId: string; tableNumber: string }) => {
      updateTableStatus(data.tableId, "ServiceRequested", {
        serviceRequestedAt: new Date().toISOString(),
      });
      playServiceCallSound();
    });
  }, [registerHandler, updateTableStatus, playServiceCallSound]);

  const currentFloorTables = getTablesForSelectedFloor();
  const alertsCount = getServiceAlertsCount();

  const getTableStatusCard = (table: TableDto) => {
    switch (table.status) {
      case "Available":
        return {
          borderClass: "border-emerald-300 bg-emerald-50/50 hover:bg-emerald-50 text-emerald-950",
          statusText: "Bàn Trống",
          badgeClass: "bg-emerald-600 text-white",
          dotColor: "bg-emerald-500",
        };
      case "Occupied_Paid":
        return {
          borderClass: "border-sky-300 bg-sky-50/50 hover:bg-sky-50 text-sky-950",
          statusText: "Đã Trả Trước (VietQR)",
          badgeClass: "bg-sky-600 text-white",
          dotColor: "bg-sky-500",
        };
      case "Occupied_PendingPayment":
        return {
          borderClass: "border-amber-300 bg-amber-50/50 hover:bg-amber-50 text-amber-950",
          statusText: "Chờ Thu Tiền Mặt",
          badgeClass: "bg-amber-600 text-white",
          dotColor: "bg-amber-500",
        };
      case "ServiceRequested":
        return {
          borderClass: "border-rose-500 bg-rose-50 text-rose-950 shadow-lg shadow-rose-200 animate-pulse ring-2 ring-rose-400",
          statusText: "KHÁCH BẤM CHUÔNG GỌI",
          badgeClass: "bg-rose-600 text-white font-black",
          dotColor: "bg-rose-600 animate-ping",
        };
    }
  };

  const handleResolveAlert = (tableId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    resolveServiceCall(tableId);
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Top Title Bar */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <LayoutGrid className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Sơ Đồ Quản Lý Bàn & Tiếp Nhận Chuông Gọi
            </h1>
            <span className="text-xs text-slate-500">
              Giám sát trạng thái bàn theo thời gian thực và xử lý yêu cầu phục vụ của khách
            </span>
          </div>
        </div>

        {/* Active Service Bell Alert Counter */}
        {alertsCount > 0 && (
          <div className="bg-rose-600 text-white px-4 py-2 rounded-2xl text-xs font-black flex items-center gap-2 shadow-md animate-bounce">
            <Bell className="h-4 w-4 fill-current" />
            <span>{alertsCount} BÀN ĐANG GỌI PHỤC VỤ!</span>
          </div>
        )}
      </div>

      {/* Floor Selection Tabs */}
      <div className="flex items-center gap-2 bg-white p-2 rounded-2xl border border-slate-200 shadow-2xs w-max">
        {[1, 2, 3].map((fl) => (
          <button
            key={fl}
            onClick={() => setSelectedFloor(fl)}
            className={`px-5 py-2.5 rounded-xl text-xs font-bold transition-all ${
              selectedFloor === fl
                ? "bg-amber-700 text-white shadow-sm"
                : "text-slate-600 hover:bg-slate-100"
            }`}
          >
            Tầng {fl} {fl === 3 ? "(Sân Thượng)" : ""}
          </button>
        ))}
      </div>

      {/* Tables Grid Layout */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {currentFloorTables.map((table) => {
          const style = getTableStatusCard(table);

          return (
            <div
              key={table.id}
              onClick={() => setSelectedTable(table)}
              className={`p-5 rounded-3xl border-2 transition-all cursor-pointer flex flex-col justify-between space-y-4 shadow-sm hover:shadow-md ${style.borderClass}`}
            >
              {/* Table Number & Capacity */}
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="font-black text-2xl tracking-tight">
                    BÀN #{table.tableNumber}
                  </h3>
                  <div className="flex items-center gap-1.5 text-xs opacity-75 font-medium mt-0.5">
                    <Users className="h-3.5 w-3.5" />
                    <span>Sức chứa: {table.capacity} khách</span>
                  </div>
                </div>

                <div className="flex items-center gap-1.5">
                  <span className={`w-2.5 h-2.5 rounded-full ${style.dotColor}`} />
                  <span className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${style.badgeClass}`}>
                    {table.status === "Available"
                      ? "Trống"
                      : table.status === "Occupied_Paid"
                      ? "Đã TT"
                      : table.status === "Occupied_PendingPayment"
                      ? "Trả Sau"
                      : "GỌI BÀN"}
                  </span>
                </div>
              </div>

              {/* Active Order Info or Call Bell Action */}
              {table.status === "ServiceRequested" ? (
                <div className="space-y-2 pt-2">
                  <span className="text-xs font-bold text-rose-800 block">
                    🔔 Khách yêu cầu nhân viên đến bàn!
                  </span>
                  <button
                    type="button"
                    onClick={(e) => handleResolveAlert(table.id, e)}
                    className="w-full py-2.5 bg-rose-600 hover:bg-rose-700 text-white font-extrabold text-xs rounded-xl shadow-md flex items-center justify-center gap-1.5 active:scale-95 transition-all"
                  >
                    <Check className="h-4 w-4" />
                    <span>TIẾP NHẬN & TẮT CHUÔNG</span>
                  </button>
                </div>
              ) : table.activeOrderId ? (
                <div className="bg-white/80 backdrop-blur p-2.5 rounded-xl border border-current/20 text-xs space-y-1">
                  <div className="flex justify-between font-semibold">
                    <span>Mã Đơn: #{table.activeOrderId}</span>
                    <span>{table.activeAmount ? formatCurrencyVND(table.activeAmount) : ""}</span>
                  </div>
                  <span className="text-[11px] opacity-75 block">{style.statusText}</span>
                </div>
              ) : (
                <div className="py-2 text-center text-xs opacity-60 font-medium">
                  Sẵn sàng đón khách mới
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Table Detail Modal */}
      <Modal
        isOpen={!!selectedTable}
        onClose={() => setSelectedTable(null)}
        maxWidth="md"
        title={selectedTable ? `Chi Tiết Bàn #${selectedTable.tableNumber}` : ""}
        footer={
          <Button variant="secondary" onClick={() => setSelectedTable(null)}>
            Đóng
          </Button>
        }
      >
        {selectedTable && (
          <div className="space-y-4 text-xs">
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <div className="flex justify-between">
                <span className="text-slate-500">Vị trí:</span>
                <strong className="text-slate-900">Tầng {selectedTable.floor}</strong>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Sức chứa:</span>
                <strong className="text-slate-900">{selectedTable.capacity} người</strong>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Trạng thái:</span>
                <span className="font-bold text-amber-800">{selectedTable.status}</span>
              </div>
            </div>

            {selectedTable.activeOrderId && (
              <div className="p-4 rounded-xl bg-amber-50 border border-amber-200 space-y-2">
                <h4 className="font-bold text-amber-950">Đơn hàng đang phục vụ</h4>
                <div className="flex justify-between">
                  <span>Mã đơn:</span>
                  <strong>#{selectedTable.activeOrderId}</strong>
                </div>
                <div className="flex justify-between">
                  <span>Tổng tiền:</span>
                  <strong className="text-amber-900">
                    {selectedTable.activeAmount ? formatCurrencyVND(selectedTable.activeAmount) : "--"}
                  </strong>
                </div>
              </div>
            )}
          </div>
        )}
      </Modal>
    </div>
  );
}
