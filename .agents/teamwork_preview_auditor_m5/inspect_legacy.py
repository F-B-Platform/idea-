import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\.agents\teamwork_preview_auditor_m5\scan_raw.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"=== DETAILED LEGACY ALERTS ({len(data['prohibited_legacy'])}) ===")
for item in data["prohibited_legacy"]:
    print(f"[{item['file']}:{item['line']}] [{item['issue']}]\n  -> {item['content']}\n")
