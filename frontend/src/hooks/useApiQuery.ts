"use client";

import { useState, useEffect, useCallback } from "react";
import { fetchApi, ApiError } from "@/lib/api-client";
import { ApiResponse, ProblemDetails } from "@/types";

interface UseApiQueryOptions {
  enabled?: boolean;
  params?: Record<string, any>;
  onSuccess?: (data: any) => void;
  onError?: (error: ApiError | Error) => void;
}

export function useApiQuery<T>(
  endpoint: string,
  options: UseApiQueryOptions = {}
) {
  const { enabled = true, params, onSuccess, onError } = options;

  const [data, setData] = useState<T | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(enabled);
  const [error, setError] = useState<ProblemDetails | Error | null>(null);
  const [statusCode, setStatusCode] = useState<number | null>(null);

  const refetch = useCallback(async () => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetchApi<T>(endpoint, { method: "GET", params });
      if (response.success && response.data !== null) {
        setData(response.data);
        setStatusCode(response.statusCode || 200);
        if (onSuccess) onSuccess(response.data);
      } else {
        const err = new Error(response.message || "Yêu cầu không thành công");
        setError(err);
        if (onError) onError(err);
      }
    } catch (err: any) {
      if (err instanceof ApiError && err.problemDetails) {
        setError(err.problemDetails);
        setStatusCode(err.statusCode);
      } else {
        setError(err);
      }
      if (onError) onError(err);
    } finally {
      setIsLoading(false);
    }
  }, [endpoint, JSON.stringify(params), onSuccess, onError]);

  useEffect(() => {
    if (enabled) {
      refetch();
    }
  }, [enabled, refetch]);

  return {
    data,
    isLoading,
    error,
    statusCode,
    refetch,
    setData,
  };
}

export function useApiMutation<TData = any, TVariables = any>(
  endpoint: string,
  method: "POST" | "PUT" | "PATCH" | "DELETE" = "POST"
) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<ProblemDetails | Error | null>(null);
  const [data, setData] = useState<TData | null>(null);

  const mutate = async (variables?: TVariables): Promise<ApiResponse<TData>> => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetchApi<TData>(endpoint, {
        method,
        body: variables ? JSON.stringify(variables) : undefined,
      });

      if (response.success) {
        setData(response.data);
        return response;
      } else {
        throw new Error(response.message || "Thao tác thất bại");
      }
    } catch (err: any) {
      if (err instanceof ApiError && err.problemDetails) {
        setError(err.problemDetails);
      } else {
        setError(err);
      }
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  return {
    mutate,
    isLoading,
    error,
    data,
    reset: () => {
      setError(null);
      setData(null);
      setIsLoading(false);
    },
  };
}
