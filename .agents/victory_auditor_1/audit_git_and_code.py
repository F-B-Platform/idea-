import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print("=== AUDIT Git_Workflow_&_Branching_Strategy.md ===")
print(f"Total characters: {len(content):,}")
print(f"Total lines: {len(content.splitlines()):,}")

# Check Section Headers
headers = [
    ("GitFlow Branching Strategy", r"GitFlow|Chiến lược phân nhánh"),
    ("Conventional Commits", r"Conventional Commits|Quy chuẩn Commit"),
    ("Pull Request Lifecycle & Gates", r"Pull Request|Quy trình PR|Review Checklist"),
    ("CI/CD Gates (SonarQube, Tests)", r"SonarQube|CI/CD|Quality Gate"),
    (".NET 8 Backend Coding Standards", r"\.NET 8|C#|Clean Architecture|CQRS|MediatR"),
    ("Next.js 14 Frontend Coding Standards", r"Next\.js|TypeScript|App Router|Tailwind")
]

print("\n--- 1. Section Coverage Check ---")
for name, pat in headers:
    m = re.search(pat, content, re.IGNORECASE)
    print(f"  [{'PASS' if m else 'FAIL'}] {name}: {'Found' if m else 'NOT FOUND'}")

# Extract Code Blocks
csharp_blocks = re.findall(r"```csharp\s*(.*?)\s*```", content, re.DOTALL)
ts_blocks = re.findall(r"```(?:typescript|tsx|ts)\s*(.*?)\s*```", content, re.DOTALL)
yaml_blocks = re.findall(r"```(?:yaml|yml)\s*(.*?)\s*```", content, re.DOTALL)
bash_blocks = re.findall(r"```(?:bash|sh)\s*(.*?)\s*```", content, re.DOTALL)

print(f"\n--- 2. Code Blocks Extracted ---")
print(f"  C# blocks: {len(csharp_blocks)}")
print(f"  TypeScript / TSX blocks: {len(ts_blocks)}")
print(f"  YAML / CI/CD blocks: {len(yaml_blocks)}")
print(f"  Bash / Git script blocks: {len(bash_blocks)}")

# Save C# and TS blocks to test compilation / syntax
csharp_dir = r"d:\Idea_DoAn\.agents\victory_auditor_1\test_csharp"
os.makedirs(csharp_dir, exist_ok=True)
for idx, cb in enumerate(csharp_blocks, 1):
    with open(os.path.join(csharp_dir, f"Sample_{idx}.cs"), "w", encoding="utf-8") as f:
        f.write(cb)

ts_dir = r"d:\Idea_DoAn\.agents\victory_auditor_1\test_ts"
os.makedirs(ts_dir, exist_ok=True)
for idx, tb in enumerate(ts_blocks, 1):
    with open(os.path.join(ts_dir, f"Sample_{idx}.tsx"), "w", encoding="utf-8") as f:
        f.write(tb)

print(f"Saved {len(csharp_blocks)} C# samples to {csharp_dir}")
print(f"Saved {len(ts_blocks)} TS/TSX samples to {ts_dir}")
