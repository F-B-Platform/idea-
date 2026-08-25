## 2026-08-25T02:36:33Z

<USER_REQUEST>
You are the Lead QA & DevOps Engineer for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\worker_qa_devops\
Original Request path: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md
Project specification: d:\Idea_DoAn\PROJECT.md
QA Spec Analysis: d:\Idea_DoAn\.agents\spec_miner_qa\analysis.md

WRITE OWNERSHIP:
You exclusively own and can create/modify files under: `backend/tests/` and `.github/`. Do NOT modify `backend/src/` or `frontend/src/`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

TASK OBJECTIVE:
Implement the complete, production-ready Unit & Integration test scaffolding and CI/CD pipelines:
1. `backend/tests/SmartFB.UnitTests/`:
   - Domain logic tests: `CustomerLoyaltyTests` (10-cup takeaway rule, reset to 0), `OrderEntityTests` (20k delivery shipping fee, status transitions), `ProductBomTests` (ingredient calculation).
   - Application feature handler tests with Moq (`Auth`, `Orders`, `Payments`, `Attendances`, `KitchenKDS`, `ShiftsAndCash`).
   - FluentValidation validator tests for key request DTOs.
2. `backend/tests/SmartFB.IntegrationTests/`:
   - `CustomWebApplicationFactory<Program>` test infrastructure.
   - Test database fixture & `TestAuthHandler` (simulating CashierStaff, BaristaStaff, BranchManager, ChainAdmin, Customer).
   - 7 UAT flow test suites:
     * Dine-In prepaid VietQR vs postpaid Cash flow
     * QR Delivery with 20k fee & VietQR payment
     * Takeaway POS 10-cup loyalty stamp & free drink redemption
     * Dual WiFi attendance verification (BSSID + Subnet IP)
     * KDS 86-Toggle out-of-stock & BOM auto-deduction on Ready
     * Cash Shift Z-Report with >50k variance justification
     * PayOS Webhook HMAC-SHA256 signature verification & idempotency
3. `.github/workflows/ci.yml`:
   - Complete GitHub Actions pipeline for backend (.NET 8 restore, build, test with coverage) and frontend (Node.js 20, npm install, typecheck, lint).
4. VERIFICATION:
   - Run `dotnet test backend/SmartFB.slnx` and verify 100% test success.
   - Document execution commands and output in your handoff.

OUTPUT REQUIREMENTS:
- Write detailed implementation log to `d:\Idea_DoAn\.agents\worker_qa_devops\changes.md`.
- Write handoff report to `d:\Idea_DoAn\.agents\worker_qa_devops\handoff.md`.
- Update `d:\Idea_DoAn\.agents\worker_qa_devops\progress.md`.
- Send message to caller when done.
</USER_REQUEST>
