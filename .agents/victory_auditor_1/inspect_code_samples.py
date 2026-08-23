import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

csharp_dir = r"d:\Idea_DoAn\.agents\victory_auditor_1\test_csharp"
ts_dir = r"d:\Idea_DoAn\.agents\victory_auditor_1\test_ts"

print("=== C# CODE SAMPLES ===")
for fname in sorted(os.listdir(csharp_dir)):
    fpath = os.path.join(csharp_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()
        print(f"\n[{fname}] - {len(lines)} lines")
        print("  First 3 lines:", lines[:3])
        print("  Last 3 lines:", lines[-3:])

print("\n=== TYPESCRIPT / TSX CODE SAMPLES ===")
for fname in sorted(os.listdir(ts_dir)):
    fpath = os.path.join(ts_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()
        print(f"\n[{fname}] - {len(lines)} lines")
        print("  First 3 lines:", lines[:3])
        print("  Last 3 lines:", lines[-3:])
