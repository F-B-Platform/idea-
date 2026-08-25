import * as signalR from "@microsoft/signalr";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000";

export function createSignalRConnection(hubPath: string) {
  const url = `${API_BASE_URL}${hubPath.startsWith("/") ? hubPath : `/${hubPath}`}`;

  return new signalR.HubConnectionBuilder()
    .withUrl(url, {
      skipNegotiation: false,
      transport: signalR.HttpTransportType.WebSockets | signalR.HttpTransportType.LongPolling,
    })
    .withAutomaticReconnect([0, 2000, 5000, 10000, 30000])
    .configureLogging(signalR.LogLevel.Information)
    .build();
}
