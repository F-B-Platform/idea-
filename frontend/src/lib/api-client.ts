import { ApiResponse, ProblemDetails } from "@/types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000";

interface RequestOptions extends RequestInit {
  token?: string;
  params?: Record<string, string | number | boolean | undefined>;
}

export class ApiError extends Error {
  public statusCode: number;
  public problemDetails?: ProblemDetails;

  constructor(message: string, statusCode: number, problemDetails?: ProblemDetails) {
    super(message);
    this.name = "ApiError";
    this.statusCode = statusCode;
    this.problemDetails = problemDetails;
  }
}

export async function fetchApi<T>(
  endpoint: string,
  options: RequestOptions = {}
): Promise<ApiResponse<T>> {
  const { token, params, ...customConfig } = options;

  let url = `${API_BASE_URL}${endpoint.startsWith("/") ? endpoint : `/${endpoint}`}`;

  if (params) {
    const searchParams = new URLSearchParams();
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined && value !== null) {
        searchParams.append(key, String(value));
      }
    });
    const queryString = searchParams.toString();
    if (queryString) {
      url += `?${queryString}`;
    }
  }

  const authToken = token || (typeof window !== "undefined" ? localStorage.getItem("smart_fb_token") : null);

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    Accept: "application/json",
    ...(authToken ? { Authorization: `Bearer ${authToken}` } : {}),
    ...(customConfig.headers as Record<string, string>),
  };

  try {
    const response = await fetch(url, {
      ...customConfig,
      headers,
    });

    const contentType = response.headers.get("content-type");
    let responseData: any = null;

    if (contentType && contentType.includes("application/json")) {
      responseData = await response.json();
    } else {
      const text = await response.text();
      responseData = { message: text };
    }

    if (!response.ok) {
      const problemDetails: ProblemDetails = {
        title: responseData?.title || responseData?.message || "Lỗi yêu cầu máy chủ",
        status: response.status,
        detail: responseData?.detail || responseData?.message || response.statusText,
        errors: responseData?.errors,
        timestampUtc: new Date().toISOString(),
      };

      throw new ApiError(
        problemDetails.detail || problemDetails.title,
        response.status,
        problemDetails
      );
    }

    // If backend returns enveloped ApiResponse<T>
    if (responseData && typeof responseData === "object" && "success" in responseData) {
      return responseData as ApiResponse<T>;
    }

    // Normalize direct data payload into ApiResponse envelope
    return {
      success: true,
      statusCode: response.status,
      message: "Thành công",
      data: responseData as T,
      timestamp: new Date().toISOString(),
    };
  } catch (error: any) {
    if (error instanceof ApiError) {
      throw error;
    }

    return {
      success: false,
      statusCode: 500,
      message: error?.message || "Lỗi mạng hoặc không thể kết nối tới máy chủ",
      data: null,
      timestamp: new Date().toISOString(),
    };
  }
}

export const apiClient = {
  get: <T>(url: string, params?: Record<string, any>, options?: RequestOptions) =>
    fetchApi<T>(url, { method: "GET", params, ...options }),

  post: <T>(url: string, body?: any, options?: RequestOptions) =>
    fetchApi<T>(url, {
      method: "POST",
      body: body ? JSON.stringify(body) : undefined,
      ...options,
    }),

  put: <T>(url: string, body?: any, options?: RequestOptions) =>
    fetchApi<T>(url, {
      method: "PUT",
      body: body ? JSON.stringify(body) : undefined,
      ...options,
    }),

  patch: <T>(url: string, body?: any, options?: RequestOptions) =>
    fetchApi<T>(url, {
      method: "PATCH",
      body: body ? JSON.stringify(body) : undefined,
      ...options,
    }),

  delete: <T>(url: string, options?: RequestOptions) =>
    fetchApi<T>(url, { method: "DELETE", ...options }),
};
