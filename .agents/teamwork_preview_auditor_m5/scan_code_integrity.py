import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

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

def scan_code_blocks():
    print("=== DEEP CODE BLOCK SYNTAX & INTEGRITY SCAN ===")
    total_blocks = 0
    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        blocks = re.findall(r"```([a-zA-Z0-9_-]*)\n([\s\S]*?)```", content)
        total_blocks += len(blocks)
        for idx, (lang, code) in enumerate(blocks, 1):
            code_trimmed = code.strip()
            # Check for JSON syntax validity if lang == 'json'
            if lang.lower() == "json":
                # Try to parse if it's pure JSON (not pseudo or containing comments)
                # Some JSON blocks might contain comments like // which standard json parser rejects
                pass
            # Check for SQL unclosed quotes or semicolons
            # Check for unclosed curly braces in C# or TypeScript
            if lang.lower() in ["csharp", "cs", "typescript", "ts", "tsx"]:
                open_braces = code.count("{")
                close_braces = code.count("}")
                if open_braces != close_braces:
                    # Some snippets might be just a single method or class interface, let's report
                    print(f"  [Notice] File {fname} block #{idx} ({lang}): {{={open_braces}, }}={close_braces}")

    print(f"\nScanned {total_blocks} total code blocks across all 9 files.")

scan_code_blocks()
