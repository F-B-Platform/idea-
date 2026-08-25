import { ApiError, fetchApi, apiClient } from "../src/lib/api-client";
import { ApiResponse, ProblemDetails } from "../src/types";

let passed = 0;
let failed = 0;

function assert(condition: boolean, msg: string) {
  if (!condition) {
    console.error(`❌ FAIL: ${msg}`);
    failed++;
    throw new Error(`Assertion failed: ${msg}`);
  } else {
    console.log(`✅ PASS: ${msg}`);
    passed++;
  }
}

async function runApiClientTests() {
  console.log("==========================================");
  console.log("TEST SUITE: API Client & RFC 7807 Parsing");
  console.log("==========================================");

  // 1. ApiError instantiation
  const problem: ProblemDetails = {
    title: "Validation Error",
    status: 400,
    detail: "Dữ liệu gửi lên không hợp lệ.",
    errors: {
      Phone: ["Số điện thoại không đúng định dạng."],
    },
    timestampUtc: new Date().toISOString(),
  };

  const error = new ApiError(problem.detail, 400, problem);
  assert(error.name === "ApiError", "Error name is ApiError");
  assert(error.statusCode === 400, "Status code is 400");
  assert(error.problemDetails?.errors?.Phone[0] === "Số điện thoại không đúng định dạng.", "RFC 7807 errors dictionary parsed");

  // 2. Mock fetch test for RFC 7807 response
  const originalFetch = global.fetch;

  // Mock 400 Bad Request with ProblemDetails
  global.fetch = async () => {
    return {
      ok: false,
      status: 400,
      statusText: "Bad Request",
      headers: {
        get: (header: string) => (header === "content-type" ? "application/json" : null),
      },
      json: async () => ({
        title: "One or more validation errors occurred.",
        status: 400,
        detail: "Validation failed on BranchId.",
        errors: {
          BranchId: ["BranchId is required."],
        },
      }),
      text: async () => "",
    } as any;
  };

  try {
    await apiClient.post("/api/v1/orders/dine-in/prepaid", { items: [] });
    assert(false, "Should have thrown ApiError on 400");
  } catch (err: any) {
    assert(err instanceof ApiError, "Caught ApiError instance");
    assert(err.statusCode === 400, "Caught 400 status");
    assert(err.problemDetails?.detail === "Validation failed on BranchId.", "Problem details detail parsed");
    assert(err.problemDetails?.errors?.BranchId[0] === "BranchId is required.", "Validation errors dictionary extracted");
  }

  // Mock 200 OK with ApiResponse envelope
  global.fetch = async () => {
    return {
      ok: true,
      status: 200,
      statusText: "OK",
      headers: {
        get: (header: string) => (header === "content-type" ? "application/json" : null),
      },
      json: async () => ({
        success: true,
        statusCode: 200,
        message: "Thành công",
        data: { id: "order-123", totalAmount: 50000 },
        timestamp: new Date().toISOString(),
      }),
      text: async () => "",
    } as any;
  };

  const successRes = await apiClient.get<any>("/api/v1/orders/order-123");
  assert(successRes.success === true, "ApiResponse success is true");
  assert(successRes.data?.id === "order-123", "ApiResponse data extracted");
  assert(successRes.data?.totalAmount === 50000, "ApiResponse totalAmount extracted");

  // Restore fetch
  global.fetch = originalFetch;

  console.log("\n==========================================");
  console.log(`SUMMARY: ${passed} PASSED, ${failed} FAILED`);
  console.log("==========================================");

  if (failed > 0) {
    process.exit(1);
  }
}

runApiClientTests().catch((err) => {
  console.error("FATAL ERROR in api client test runner:", err);
  process.exit(1);
});
