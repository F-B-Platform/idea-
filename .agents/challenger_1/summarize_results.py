import os
import re
import json

# Generate structured test evidence summary for handoff.md
with open(r"d:\Idea_DoAn\.agents\challenger_1\mermaid_audit_results.json", "r", encoding="utf-8") as f:
    mermaid_data = json.load(f)

summary = {}
for fname, blocks in mermaid_data.items():
    summary[fname] = {
        "total": len(blocks),
        "passed": sum(1 for b in blocks if b["status"] == "PASS"),
        "failed": sum(1 for b in blocks if b["status"] != "PASS")
    }

print("Mermaid Verification Summary:")
print(json.dumps(summary, indent=2))