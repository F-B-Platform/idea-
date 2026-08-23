## 2026-08-23T14:43:37Z
You are a Challenger subagent for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\challenger_schema_standards\
Create your working directory if needed.

Read:
1. `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`
2. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md`
3. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md`

Your task:
Adversarially challenge the technical soundness, schema consistency, and coding standards:
1. Database Schema & Seed Data Challenge:
   - Verify table creation order vs Foreign Key dependencies (no circular dependencies or missing referenced tables).
   - Check data type matching between Foreign Keys and Primary Keys (UUIDs).
   - Check all INSERT statements for syntax validity and matching column counts.
   - Verify that sample orders reference existing branches, tables, users, menu items, sizes, and customers.
2. Coding Standards & Code Samples Challenge:
   - Challenge .NET 8 C# samples: `Money.cs`, `Order.cs`, `CreateDineInOrderCommand.cs`, `CreateDineInOrderCommandHandler.cs`, `CreateDineInOrderCommandValidator.cs`, `GlobalExceptionHandler.cs`. Are they complete, compilable, and free of placeholders?
   - Challenge Next.js 14 TS samples: `TableOrderPage.tsx`, `ModifierDrawer.tsx`, `useSignalRKitchenHub.ts`, `useCartStore.ts`. Are they strict TypeScript, complete, and free of placeholders?
   - Challenge CI/CD YAML and Mermaid diagrams.

Provide your findings in `d:\Idea_DoAn\.agents\challenger_schema_standards\challenge_report.md` and write `d:\Idea_DoAn\.agents\challenger_schema_standards\handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`. Send a message to parent when completed.
