import os
import re
import json

TARGET_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
FILES = [
    "01_Phan_Tich_Yeu_Cau.md",
    "02_Thiet_Ke_Database.md",
    "03_Thiet_Ke_API_Contract.md",
    "04_Thiet_Ke_UI_UX.md",
    "05_Quy_Trinh_Backend.md",
    "06_Quy_Trinh_Frontend.md",
    "07_Ke_Hoach_Kiem_Thu.md",
    "08_Trien_Khai_He_Thong.md",
    "README.md"
]

def scan_file_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()

def run_all_checks():
    results = {
        "placeholders": [],
        "prohibited_legacy": [],
        "core_engines": {},
        "features_check": {},
        "db_tables": {},
        "api_groups": {},
        "ui_routes": {},
        "mermaid_blocks": [],
        "code_blocks": []
    }

    # 1. Scan for placeholders
    placeholder_patterns = [
        (r"\bTODO\b", "TODO detected"),
        (r"\bTBD\b", "TBD detected"),
        (r"/\*\s*\.\.\.\s*\*/", "Comment ellipsis /* ... */ detected"),
        (r"//\s*\.\.\.", "Comment ellipsis // ... detected"),
        (r"tương tự như trên", "Placeholder phrase 'tương tự như trên'"),
        (r"giữ nguyên logic", "Placeholder phrase 'giữ nguyên logic'"),
        (r"/\*\s*rest of\b", "Truncation phrase '/* rest of'"),
        (r"//\s*rest of\b", "Truncation phrase '// rest of'"),
        (r"NotImplementedException", "NotImplementedException detected"),
    ]

    # Standalone ellipsis on a single line in code block
    ellipsis_line_pattern = re.compile(r"^\s*(\.{3}|\u2026)\s*$")

    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        lines = scan_file_lines(fpath)
        in_code_block = False
        code_lang = ""

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                if in_code_block:
                    in_code_block = False
                else:
                    in_code_block = True
                    code_lang = stripped[3:].strip()

            # Check placeholders
            for pat, desc in placeholder_patterns:
                if re.search(pat, line, re.IGNORECASE):
                    # Check if it's an explicit anti-pattern example or explanation
                    results["placeholders"].append({
                        "file": fname,
                        "line": idx,
                        "content": stripped,
                        "issue": desc
                    })

            if in_code_block and ellipsis_line_pattern.match(stripped):
                results["placeholders"].append({
                    "file": fname,
                    "line": idx,
                    "content": stripped,
                    "issue": "Standalone ellipsis '...' in code block"
                })

    # 2. Prohibited legacy concepts
    legacy_patterns = [
        (r"Staff\s+Mobile\s+App", "Staff Mobile App reference"),
        (r"Staff\s+App\b", "Staff App reference"),
        (r"\bFlutter\b", "Flutter reference"),
        (r"React\s+Native", "React Native reference"),
        (r"GPS\s*50\s*m", "GPS 50m reference"),
        (r"\bGPS\b", "GPS reference"),
        (r"geofence", "Geofence reference"),
        (r"QR\s*30\s*s", "QR 30s reference"),
        (r"QR\s*động\s*30\s*giây", "QR dong 30s reference"),
        (r"\bC-23\b", "C-23 legacy feature reference"),
        (r"\bC-24\b", "C-24 legacy feature reference"),
        (r"ví\s+voucher", "Vi voucher reference"),
        (r"tra\s+cứu\s+calo\s+riêng", "Tra cuu calo rieng reference"),
    ]

    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        lines = scan_file_lines(fpath)
        for idx, line in enumerate(lines, 1):
            for pat, desc in legacy_patterns:
                if re.search(pat, line, re.IGNORECASE):
                    results["prohibited_legacy"].append({
                        "file": fname,
                        "line": idx,
                        "content": line.strip(),
                        "issue": desc
                    })

    # Write scan results to json for detailed analysis
    with open(r"d:\Idea_DoAn\.agents\teamwork_preview_auditor_m5\scan_raw.json", "w", encoding="utf-8") as out:
        json.dump(results, out, ensure_ascii=False, indent=2)

    print(f"Scanned {len(FILES)} files.")
    print(f"Total placeholder alerts: {len(results['placeholders'])}")
    print(f"Total legacy alerts: {len(results['prohibited_legacy'])}")

if __name__ == "__main__":
    run_all_checks()
