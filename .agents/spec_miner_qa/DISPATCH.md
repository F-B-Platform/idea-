## 2026-08-25T02:33:36Z
You are the QA & Verification Spec Miner for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\spec_miner_qa\
Original Request path: d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md

TASK:
1. Read d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md.
2. Investigate authoritative documents in d:\Idea_DoAn\:
   - d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md
   - d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md
   - d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md
3. Extract and document complete specifications for:
   - 47 UAT Test Cases categorized by functional area, test ID, precondition, test steps, input data, expected results.
   - Scaffolding architecture for Unit Tests (`SmartFB.UnitTests`): Feature handler tests, Domain entity logic tests, Validator tests.
   - Scaffolding architecture for Integration Tests (`SmartFB.IntegrationTests`): WebApplicationFactory setup, SQLite / InMemory / Test db fixture, API endpoint tests mapped to key UAT flows (e.g. Takeaway 10-cup loyalty, Dine-in prepay vs postpay, 86-toggle, Wifi attendance, Z-Report).
   - CI/CD Pipeline specification (`.github/workflows/ci.yml`): steps for dotnet restore, build, test, npm install, typecheck, lint.
4. Write your comprehensive specification findings to `d:\Idea_DoAn\.agents\spec_miner_qa\analysis.md`.
5. Write your handoff to `d:\Idea_DoAn\.agents\spec_miner_qa\handoff.md`.
6. Update `d:\Idea_DoAn\.agents\spec_miner_qa\progress.md` with your progress and timestamps.
7. Send a message to caller when done.
