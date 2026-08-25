import * as signalR from "@microsoft/signalr";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000";

export type HubPath =
  | "/hubs/orders"
  | "/hubs/kitchen"
  | "/hubs/payments"
  | "/hubs/notifications";

/**
 * Creates a configured SignalR HubConnection with exponential backoff auto-reconnect.
 */
export function createSignalRConnection(hubPath: HubPath | string) {
  const url = `${API_BASE_URL}${hubPath.startsWith("/") ? hubPath : `/${hubPath}`}`;

  const token = typeof window !== "undefined" ? localStorage.getItem("smart_fb_token") : null;

  return new signalR.HubConnectionBuilder()
    .withUrl(url, {
      skipNegotiation: false,
      transport: signalR.HttpTransportType.WebSockets | signalR.HttpTransportType.LongPolling,
      accessTokenFactory: token ? () => token : undefined,
    })
    .withAutomaticReconnect([0, 2000, 5000, 10000, 30000])
    .configureLogging(process.env.NODE_ENV === "development" ? signalR.LogLevel.Information : signalR.LogLevel.Error)
    .build();
}

export const signalRHubs = {
  orders: () => createSignalRConnection("/hubs/orders"),
  kitchen: () => createSignalRConnection("/hubs/kitchen"),
  payments: () => createSignalRConnection("/hubs/payments"),
  notifications: () => createSignalRConnection("/hubs/notifications"),
};
