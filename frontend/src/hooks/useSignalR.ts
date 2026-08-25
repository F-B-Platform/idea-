"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import * as signalR from "@microsoft/signalr";
import { createSignalRConnection, HubPath } from "@/lib/signalr";

export type ConnectionStatus = "Connecting" | "Connected" | "Reconnecting" | "Disconnected";

interface UseSignalROptions {
  hubPath: HubPath | string;
  autoConnect?: boolean;
  groupName?: string;
  joinGroupMethod?: string;
  leaveGroupMethod?: string;
  onConnected?: (connection: signalR.HubConnection) => void;
  onReconnecting?: (error?: Error) => void;
  onReconnected?: (connectionId?: string) => void;
  onClose?: (error?: Error) => void;
}

export function useSignalR({
  hubPath,
  autoConnect = true,
  groupName,
  joinGroupMethod,
  leaveGroupMethod,
  onConnected,
  onReconnecting,
  onReconnected,
  onClose,
}: UseSignalROptions) {
  const connectionRef = useRef<signalR.HubConnection | null>(null);
  const [status, setStatus] = useState<ConnectionStatus>("Disconnected");
  const [error, setError] = useState<Error | null>(null);

  const registerHandler = useCallback((eventName: string, handler: (...args: any[]) => void) => {
    if (connectionRef.current) {
      connectionRef.current.off(eventName);
      connectionRef.current.on(eventName, handler);
    }
  }, []);

  const sendEvent = useCallback(async (methodName: string, ...args: any[]) => {
    if (connectionRef.current && connectionRef.current.state === signalR.HubConnectionState.Connected) {
      try {
        return await connectionRef.current.invoke(methodName, ...args);
      } catch (err: any) {
        console.error(`[SignalR] Invoke ${methodName} failed:`, err);
        throw err;
      }
    } else {
      console.warn(`[SignalR] Cannot invoke ${methodName}: connection is not in Connected state.`);
    }
  }, []);

  useEffect(() => {
    if (!autoConnect) return;

    let isMounted = true;
    const connection = createSignalRConnection(hubPath);
    connectionRef.current = connection;

    setStatus("Connecting");

    connection.onreconnecting((err) => {
      if (isMounted) {
        setStatus("Reconnecting");
        if (onReconnecting) onReconnecting(err);
      }
    });

    connection.onreconnected((connectionId) => {
      if (isMounted) {
        setStatus("Connected");
        if (groupName && joinGroupMethod) {
          connection.invoke(joinGroupMethod, groupName).catch(console.error);
        }
        if (onReconnected) onReconnected(connectionId);
      }
    });

    connection.onclose((err) => {
      if (isMounted) {
        setStatus("Disconnected");
        if (onClose) onClose(err);
      }
    });

    const startConnection = async () => {
      try {
        await connection.start();
        if (isMounted) {
          setStatus("Connected");
          if (groupName && joinGroupMethod) {
            await connection.invoke(joinGroupMethod, groupName);
          }
          if (onConnected) onConnected(connection);
        }
      } catch (err: any) {
        if (isMounted) {
          console.warn(`[SignalR] Connection to ${hubPath} failed (will fallback or retry):`, err?.message || err);
          setStatus("Disconnected");
          setError(err);
        }
      }
    };

    startConnection();

    return () => {
      isMounted = false;
      if (connection.state === signalR.HubConnectionState.Connected) {
        if (groupName && leaveGroupMethod) {
          connection.invoke(leaveGroupMethod, groupName).catch(() => {});
        }
        connection.stop().catch(() => {});
      }
    };
  }, [hubPath, autoConnect, groupName, joinGroupMethod, leaveGroupMethod]);

  return {
    connection: connectionRef.current,
    status,
    isConnected: status === "Connected",
    error,
    registerHandler,
    sendEvent,
  };
}
