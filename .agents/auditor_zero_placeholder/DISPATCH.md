## 2026-08-23T14:43:37Z
You are a Forensic Auditor subagent for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\auditor_zero_placeholder\
Create your working directory if needed.

Read:
1. `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`
2. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`
3. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md`
4. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md`

Your task:
Perform a strict, uncompromising Forensic Integrity Audit across all 3 target files:
1. Zero Placeholders Forensics:
   - Perform comprehensive pattern matching across all 3 files for: `TODO`, `FIXME`, `TBD`, `/* rest of`, `// rest of`, `// tương tự`, `// giữ nguyên`, `...` (in SQL, C#, TS, YAML, or Markdown tables).
   - Verify that all code blocks and SQL statements are 100% complete and exhaustive.
2. Purge Verification Forensics:
   - Search for obsolete terms: `Staff Mobile App`, `Mobile App`, `GPS 50m`, `30s QR`, `QR xoay 30s`, `C-23`, `C-24`. Confirm they are completely purged.
3. Authenticity & Completeness Forensics:
   - Check file sizes and line counts: `UAT_Test_Cases.md` (1,400+ lines), `Seed_Data_&_Database_Script.md` (1,700+ lines), `Git_Workflow_&_Branching_Strategy.md` (2,300+ lines).
   - Confirm all 47 test cases in `UAT_Test_Cases.md` exist with complete fields.
   - Confirm all 25+ tables in `Seed_Data_&_Database_Script.md` have full DDL and complete INSERTs.
   - Confirm all C# and TypeScript code samples in `Git_Workflow_&_Branching_Strategy.md` are genuine, complete, production-grade implementations.
4. Formatting Forensics:
   - Confirm GitHub Alert Callouts (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`).

Provide your forensic audit report in `d:\Idea_DoAn\.agents\auditor_zero_placeholder\audit_report.md` and write `d:\Idea_DoAn\.agents\auditor_zero_placeholder\handoff.md` with binary verdict: `CLEAN` or `INTEGRITY VIOLATION`. Send a message to parent when completed.
