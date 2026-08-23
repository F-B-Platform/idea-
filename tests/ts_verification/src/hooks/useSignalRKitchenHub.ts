// ============================================================================
// File: src/hooks/useSignalRKitchenHub.ts
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Hook quản lý kết nối SignalR WebSocket thời gian thực cho Bếp KDS.
// Hỗ trợ tự động kết nối lại (Exponential Backoff), gia nhập nhóm chi nhánh và đồng bộ trạng thái.
// ============================================================================

import { useEffect, useRef, useState, useCallback } from "react";
import * as signalR from "@microsoft/signalr";

export interface KdsTicketItem {
  itemId: string;
  itemName: string;
  sizeName: string;
  quantity: number;
  sweetness?: string;
  ice?: string;
  toppings: string[];
  note?: string;
}

export interface KdsTicket {
  orderId: string;
  orderCode: string;
  tableCode?: string;
  channel: "DineIn" | "Delivery" | "TakeAway";
  status: "PendingPayment" | "Confirmed" | "Preparing" | "Ready";
  createdAtUtc: string;
  elapsedMinutes: number;
  urgencyLevel: "Normal" | "Warning" | "Critical";
  items: KdsTicketItem[];
}

interface UseSignalRKitchenHubOptions {
  branchId: string;
  accessToken: string;
  onNewTicket?: (ticket: KdsTicket) => void;
  onTicketStatusChanged?: (orderId: string, newStatus: string) => void;
  onItem86Toggled?: (menuItemId: string, isAvailable: boolean) => void;
}

interface UseSignalRKitchenHubReturn {
  isConnected: boolean;
  connectionError: string | null;
  reconnectAttempt: number;
  updateTicketStatus: (orderId: string, status: string) => Promise<boolean>;
}

export function useSignalRKitchenHub({
  branchId,
  accessToken,
  onNewTicket,
  onTicketStatusChanged,
  onItem86Toggled
}: UseSignalRKitchenHubOptions): UseSignalRKitchenHubReturn {
  const [isConnected, setIsConnected] = useState<boolean>(false);
  const [connectionError, setConnectionError] = useState<string | null>(null);
  const [reconnectAttempt, setReconnectAttempt] = useState<number>(0);
  const hubConnectionRef = useRef<signalR.HubConnection | null>(null);

  const connect = useCallback(async () => {
    if (hubConnectionRef.current) {
      return;
    }

    const hubUrl = process.env.NEXT_PUBLIC_SIGNALR_KITCHEN_HUB_URL || "https://api.smartfb.vn/hubs/kitchen";

    const connection = new signalR.HubConnectionBuilder()
      .withUrl(hubUrl, {
        accessTokenFactory: () => accessToken,
        transport: signalR.HttpTransportType.WebSockets,
        skipNegotiation: true
      })
      .withAutomaticReconnect({
        nextRetryDelayInMilliseconds: (retryContext) => {
          // Thử lại theo Exponential Backoff: 0s, 2s, 5s, 10s, 30s
          const delays = [0, 2000, 5000, 10000, 30000];
          const delay = delays[retryContext.previousAttempts] ?? 30000;
          setReconnectAttempt(retryContext.previousAttempts + 1);
          return delay;
        }
      })
      .configureLogging(signalR.LogLevel.Warning)
      .build();

    // Đăng ký các sự kiện thời gian thực
    connection.on("ReceiveNewKitchenTicket", (ticket: KdsTicket) => {
      onNewTicket?.(ticket);
    });

    connection.on("ReceiveTicketStatusUpdate", (orderId: string, newStatus: string) => {
      onTicketStatusChanged?.(orderId, newStatus);
    });

    connection.on("ReceiveItem86Toggle", (menuItemId: string, isAvailable: boolean) => {
      onItem86Toggled?.(menuItemId, isAvailable);
    });

    connection.onreconnecting((error) => {
      setIsConnected(false);
      setConnectionError(`Mất kết nối tới KDS Hub: ${error?.message || "Đang kết nối lại..."}`);
    });

    connection.onreconnected(async () => {
      setIsConnected(true);
      setConnectionError(null);
      setReconnectAttempt(0);
      await connection.invoke("JoinBranchKitchenGroup", branchId);
    });

    connection.onclose((error) => {
      setIsConnected(false);
      if (error) {
        setConnectionError(`Kết nối KDS Hub đã đóng do lỗi: ${error.message}`);
      }
    });

    try {
      await connection.start();
      await connection.invoke("JoinBranchKitchenGroup", branchId);
      hubConnectionRef.current = connection;
      setIsConnected(true);
      setConnectionError(null);
      setReconnectAttempt(0);
    } catch (err: unknown) {
      const errorMsg = err instanceof Error ? err.message : "Không thể thiết lập kết nối WebSocket tới Bếp KDS.";
      setIsConnected(false);
      setConnectionError(errorMsg);
    }
  }, [branchId, accessToken, onNewTicket, onTicketStatusChanged, onItem86Toggled]);

  useEffect(() => {
    connect();

    return () => {
      if (hubConnectionRef.current) {
        hubConnectionRef.current.stop();
        hubConnectionRef.current = null;
      }
    };
  }, [connect]);

  const updateTicketStatus = useCallback(async (orderId: string, status: string): Promise<boolean> => {
    if (!hubConnectionRef.current || !isConnected) {
      setConnectionError("Không thể cập nhật: Mất kết nối tới KDS Hub.");
      return false;
    }

    try {
      await hubConnectionRef.current.invoke("UpdateTicketStatus", branchId, orderId, status);
      return true;
    } catch (error: unknown) {
      console.error("Lỗi khi cập nhật trạng thái vé qua SignalR:", error);
      return false;
    }
  }, [branchId, isConnected]);

  return {
    isConnected,
    connectionError,
    reconnectAttempt,
    updateTicketStatus
  };
}
