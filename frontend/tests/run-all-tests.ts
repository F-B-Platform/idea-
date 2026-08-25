import { execSync } from "child_process";

const testFiles = [
  "tests/test-stores.ts",
  "tests/test-utils-audio-escpos.ts",
  "tests/test-routes-exports.ts",
  "tests/test-api-client.ts",
];

console.log("================================================================================");
console.log("SMART F&B OS — FRONTEND EMPIRICAL CHALLENGE MASTER TEST RUNNER");
console.log("================================================================================\n");

let allPassed = true;

for (const testFile of testFiles) {
  console.log(`>>> Executing: ${testFile}...`);
  try {
    const output = execSync(`npx tsx ${testFile}`, { encoding: "utf-8" });
    console.log(output);
  } catch (err: any) {
    console.error(`❌ Suite failed: ${testFile}`);
    console.error(err.stdout || err.message);
    allPassed = false;
  }
}

if (!allPassed) {
  console.error("❌ Master verification FAILED.");
  process.exit(1);
} else {
  console.log("================================================================================");
  console.log("✅ ALL FRONTEND ADVERSARIAL TEST SUITES PASSED EMPIRICALLY (100% SUCCESS)");
  console.log("================================================================================");
}
