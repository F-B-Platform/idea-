import fs from "fs";
import path from "path";

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

const APP_DIR = path.resolve(__dirname, "../src/app");

const expectedRoutes = [
  // (admin) - 8 pages
  "(admin)/admin-dashboard/page.tsx",
  "(admin)/ai/combos/page.tsx",
  "(admin)/audit-logs/page.tsx",
  "(admin)/crm/page.tsx",
  "(admin)/menu/categories/page.tsx",
  "(admin)/menu/products/page.tsx",
  "(admin)/menu/seasonal/page.tsx",
  "(admin)/pricing/page.tsx",

  // (customer) - 9 pages
  "(customer)/ai-chat/page.tsx",
  "(customer)/cart/page.tsx",
  "(customer)/checkout/vietqr/page.tsx",
  "(customer)/delivery/page.tsx",
  "(customer)/history/page.tsx",
  "(customer)/menu/page.tsx",
  "(customer)/review/[orderId]/page.tsx",
  "(customer)/table/[tableId]/page.tsx",
  "(customer)/tracking/[orderId]/page.tsx",

  // (kds) - 3 pages
  "(kds)/86-toggle/page.tsx",
  "(kds)/batch/page.tsx",
  "(kds)/kitchen/page.tsx",

  // (manager) - 5 pages
  "(manager)/branch-dashboard/page.tsx",
  "(manager)/inventory/page.tsx",
  "(manager)/reviews/page.tsx",
  "(manager)/shifts/page.tsx",
  "(manager)/wifi-configs/page.tsx",

  // (staff) - 4 pages
  "(staff)/attendance/page.tsx",
  "(staff)/pos/page.tsx",
  "(staff)/shift-report/page.tsx",
  "(staff)/tables/page.tsx",

  // Root - 1 page
  "page.tsx",
];

const expectedLayouts = [
  "layout.tsx",
  "(admin)/layout.tsx",
  "(customer)/layout.tsx",
  "(kds)/layout.tsx",
  "(manager)/layout.tsx",
  "(staff)/layout.tsx",
];

async function runRouteTests() {
  console.log("==========================================");
  console.log("TEST SUITE: Route Component Exports & Integrity");
  console.log("==========================================");

  console.log(`Verifying ${expectedRoutes.length} Page Routes across 5 Route Groups...`);

  for (const routeRelPath of expectedRoutes) {
    const fullPath = path.join(APP_DIR, routeRelPath);
    assert(fs.existsSync(fullPath), `Route file exists: ${routeRelPath}`);

    const fileContent = fs.readFileSync(fullPath, "utf-8");
    assert(
      fileContent.includes("export default function") ||
      fileContent.includes("export default"),
      `Route ${routeRelPath} has default export`
    );

    // Ensure no placeholder or lazy comments in page
    assert(!fileContent.includes("// TODO"), `Route ${routeRelPath} has zero TODO placeholders`);
    assert(!fileContent.includes("/* rest of code */"), `Route ${routeRelPath} has zero /* rest of code */ placeholders`);
  }

  console.log(`\nVerifying ${expectedLayouts.length} Route Group & Root Layouts...`);

  for (const layoutRelPath of expectedLayouts) {
    const fullPath = path.join(APP_DIR, layoutRelPath);
    assert(fs.existsSync(fullPath), `Layout file exists: ${layoutRelPath}`);

    const fileContent = fs.readFileSync(fullPath, "utf-8");
    assert(
      fileContent.includes("export default function") ||
      fileContent.includes("export default"),
      `Layout ${layoutRelPath} has default export`
    );
  }

  console.log("\n==========================================");
  console.log(`SUMMARY: ${passed} PASSED, ${failed} FAILED`);
  console.log("==========================================");

  if (failed > 0) {
    process.exit(1);
  }
}

runRouteTests().catch((err) => {
  console.error("FATAL ERROR in route test runner:", err);
  process.exit(1);
});
