import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
ts_blocks = [(lang, code) for lang, code in code_blocks if lang.lower() in ('tsx', 'typescript')]

print(f"Total TS/TSX blocks: {len(ts_blocks)}")
for i, (lang, code) in enumerate(ts_blocks):
    lines = code.strip().splitlines()
    print(f"\n--- Block {i+1} [{lang}] ({len(lines)} lines) ---")
    print("\n".join(lines[:15]))
    print("...")
    print("\n".join(lines[-5:]))
