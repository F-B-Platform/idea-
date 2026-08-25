"use client";

import { useState, useCallback, useEffect } from "react";
import { apiClient } from "@/lib/api-client";
import { AttendanceRecordDto, WifiConfigDto } from "@/types";

interface WifiStatus {
  ssid: string;
  bssid: string;
  clientIp: string;
  isValidBranchWifi: boolean;
  branchName?: string;
}

export function useAttendanceWifi(branchId?: string) {
  const [wifiStatus, setWifiStatus] = useState<WifiStatus>({
    ssid: "SMART_FB_BRANCH_OFFICIAL",
    bssid: "AA:BB:CC:DD:EE:01",
    clientIp: "192.168.1.105",
    isValidBranchWifi: true,
    branchName: "Chi nhánh Quận 1 (Trụ Sở)",
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lastAttendance, setLastAttendance] = useState<AttendanceRecordDto | null>(null);

  // In production browser, Web APIs cannot directly read raw MAC/BSSID without local agent,
  // so this hook simulates network probe and communicates with backend WifiValidator.
  const refreshWifiContext = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    try {
      // Probe WiFi configs from branch if branchId provided
      if (branchId) {
        const response = await apiClient.get<WifiConfigDto[]>(`/api/v1/branches/${branchId}/wifi-configs`);
        if (response.success && response.data && response.data.length > 0) {
          const config = response.data[0];
          setWifiStatus({
            ssid: config.ssid,
            bssid: config.bssid,
            clientIp: "192.168.1.105",
            isValidBranchWifi: true,
            branchName: config.branchName,
          });
        }
      }
    } catch (err: any) {
      console.warn("Could not query branch wifi configs directly:", err);
    } finally {
      setIsLoading(false);
    }
  }, [branchId]);

  useEffect(() => {
    refreshWifiContext();
  }, [refreshWifiContext]);

  const clockIn = useCallback(
    async (employeeCode: string): Promise<AttendanceRecordDto | null> => {
      setIsLoading(true);
      setError(null);
      try {
        const response = await apiClient.post<AttendanceRecordDto>("/api/v1/attendances/wifi-checkin", {
          employeeCode,
          bssid: wifiStatus.bssid,
          clientIp: wifiStatus.clientIp,
        });

        if (response.success && response.data) {
          setLastAttendance(response.data);
          return response.data;
        } else {
          setError(response.message || "Chấm công thất bại: Mạng WiFi không hợp lệ");
          return null;
        }
      } catch (err: any) {
        const msg = err?.problemDetails?.detail || err?.message || "Lỗi chấm công";
        setError(msg);
        return null;
      } finally {
        setIsLoading(false);
      }
    },
    [wifiStatus]
  );

  const clockOut = useCallback(
    async (employeeCode: string): Promise<AttendanceRecordDto | null> => {
      setIsLoading(true);
      setError(null);
      try {
        const response = await apiClient.post<AttendanceRecordDto>("/api/v1/attendances/wifi-checkout", {
          employeeCode,
          bssid: wifiStatus.bssid,
          clientIp: wifiStatus.clientIp,
        });

        if (response.success && response.data) {
          setLastAttendance(response.data);
          return response.data;
        } else {
          setError(response.message || "Chấm công ra ca thất bại: Mạng WiFi không hợp lệ");
          return null;
        }
      } catch (err: any) {
        const msg = err?.problemDetails?.detail || err?.message || "Lỗi chấm công";
        setError(msg);
        return null;
      } finally {
        setIsLoading(false);
      }
    },
    [wifiStatus]
  );

  return {
    wifiStatus,
    setWifiStatus,
    isLoading,
    error,
    lastAttendance,
    clockIn,
    clockOut,
    refreshWifiContext,
  };
}
