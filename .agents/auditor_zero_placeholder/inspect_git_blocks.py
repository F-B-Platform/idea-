import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

GIT_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"
with open(GIT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Extract code blocks
blocks = re.findall(r"```([a-zA-Z0-9_\-#+]*)\n(.*?)```", content, re.DOTALL)

print(f"Total Code Blocks in Git_Workflow_&_Branching_Strategy.md: {len(blocks)}")

for idx, (lang, code) in enumerate(blocks, 1):
    lines = code.strip().splitlines()
    print(f"\n--- Block {idx:02d} [{lang}] ({len(lines)} lines) ---")
    if lines:
        print(f"  Start: {lines[0][:80]}")
        if len(lines) > 2:
            print(f"  Mid:   {lines[len(lines)//2][:80]}")
        print(f"  End:   {lines[-1][:80]}")
    # check for any placeholder or stub
    stub_match = re.findall(r"TODO|FIXME|throw new NotImplementedException|return null;|pass\b", code)
    if stub_match:
        print(f"  WARNING: Found possible stub keywords: {stub_match}")
