import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_files = [
    r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md",
    r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md",
    r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"
]

print("=== 1. FILE EXISTENCE & LINE COUNTS ===")
for f in target_files:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
            size = os.path.getsize(f)
            print(f"[EXISTS] {os.path.basename(f)}: {len(lines)} lines, {size:,} bytes")
    else:
        print(f"[MISSING] {f}")

print("\n=== 2. ZERO PLACEHOLDER SCAN ===")
placeholder_patterns = [
    r"\bTODO\b",
    r"\bFIXME\b",
    r"\bTBD\b",
    r"\bXXX\b",
    r"/\*\s*rest of code\s*\*/",
    r"//\s*rest of code",
    r"#\s*rest of code",
    r"//\s*tương tự",
    r"//\s*giữ nguyên",
    r"/\*\s*implement later\s*\*/",
    r"\.\.\.\s*giữ nguyên",
    r"\bNotImplementedException\b",
]

for f in target_files:
    print(f"\nScanning {os.path.basename(f)}:")
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
        lines = content.splitlines()
        found = False
        for idx, line in enumerate(lines, 1):
            for pat in placeholder_patterns:
                matches = re.findall(pat, line, re.IGNORECASE)
                if matches:
                    print(f"  Line {idx}: matched '{pat}' -> {line.strip()[:100]}")
                    found = True
        if not found:
            print("  -> 0 placeholders detected (CLEAN)")

print("\n=== 3. OBSOLETE TERMS SCAN ===")
obsolete_terms = [
    (r"\bStaff\s+Mobile\s+App\b", "Staff Mobile App"),
    (r"\bApp\s+nhân\s+viên\b", "App nhân viên"),
    (r"\bGPS\s+50m\b", "GPS 50m"),
    (r"\bbán\s+kính\s+50m\b", "bán kính 50m"),
    (r"\b30s\s+QR\b", "30s QR"),
    (r"\bQR\s+30s\b", "QR 30s"),
    (r"\bC-23\b", "C-23"),
    (r"\bC-24\b", "C-24"),
]

for f in target_files:
    print(f"\nScanning obsolete terms in {os.path.basename(f)}:")
    with open(f, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
        found = False
        for idx, line in enumerate(lines, 1):
            for pat, name in obsolete_terms:
                if re.search(pat, line, re.IGNORECASE):
                    print(f"  Line {idx}: matched '{name}' -> {line.strip()[:100]}")
                    found = True
        if not found:
            print("  -> 0 obsolete terms detected (CLEAN)")
