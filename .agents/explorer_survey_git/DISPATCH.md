## 2026-08-23T14:36:04Z
You are an Explorer subagent for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\explorer_survey_git\
Create your working directory if needed.
Read the following files carefully:
1. `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`
2. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md`
3. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
4. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`

Your task:
Analyze and outline the required comprehensive upgrade for `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md`.
1. GitFlow branching strategy: main (production-ready), develop (integration), feature/* (features), release/* (release preparation), hotfix/* (emergency fixes). Provide ASCII/Mermaid flow and branching lifecycle rules.
2. Conventional Commits v1.0.0 specification: types (feat, fix, refactor, docs, test, chore, perf), scopes (backend, frontend, db, kds, pos, auth), descriptions, breaking changes.
3. Pull Request lifecycle: PR template with checkboxes, code review checklist (Clean Code, Security, Performance, Zero Placeholder), CI/CD quality gates (SonarQube quality gate 80% coverage, 0 bugs, 0 vulnerabilities; Build verification; Unit test runner).
4. Coding Standards with complete, zero-placeholder code examples:
   - Backend .NET 8: Clean Architecture (Domain, Application, Infrastructure, WebAPI), CQRS with MediatR, FluentValidation, Global Exception Handler with ProblemDetails, Repository & UnitOfWork, EF Core best practices.
   - Frontend Next.js 14: TypeScript Strict mode, App Router, Server Components vs Client Components, Custom Hooks, Zustand/React Query state management, Tailwind CSS design system, Error Boundary, Accessibility & Responsive.
5. GitHub Alert Callouts (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`).

Write your detailed findings to `d:\Idea_DoAn\.agents\explorer_survey_git\analysis.md` and `d:\Idea_DoAn\.agents\explorer_survey_git\handoff.md`.
Then send a message to parent with the summary and report path.
