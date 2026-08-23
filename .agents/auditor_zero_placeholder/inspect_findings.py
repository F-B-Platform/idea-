import json
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\.agents\auditor_zero_placeholder\audit_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open(r"d:\Idea_DoAn\.agents\auditor_zero_placeholder\findings_detailed.txt", "w", encoding="utf-8") as out:
    out.write("="*80 + "\n")
    out.write("PURGED TERMS FINDINGS:\n")
    out.write("="*80 + "\n")
    for file_key, items in data["patterns_findings"]["purged"].items():
        out.write(f"\n--- File: {file_key} ({len(items)} hits) ---\n")
        for item in items:
            out.write(f"Line {item['line_num']}: [{item['term']}] -> {item['line_content']}\n")

    out.write("\n" + "="*80 + "\n")
    out.write("PLACEHOLDER FINDINGS:\n")
    out.write("="*80 + "\n")
    for file_key, items in data["patterns_findings"]["placeholders"].items():
        out.write(f"\n--- File: {file_key} ({len(items)} hits) ---\n")
        for item in items:
            out.write(f"Line {item['line_num']}: [{item['pattern']}] -> {item['line_content']}\n")

print("Wrote detailed findings to findings_detailed.txt")
