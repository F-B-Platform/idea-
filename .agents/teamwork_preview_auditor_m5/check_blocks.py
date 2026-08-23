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

def check_mermaid_and_code():
    print("=== INSPECTING CODE BLOCKS & MERMAID DIAGRAMS ===")
    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Find all code blocks
        blocks = re.findall(r"```([a-zA-Z0-9_-]*)\n([\s\S]*?)```", content)
        mermaid_blocks = [b[1] for b in blocks if b[0] == "mermaid"]
        other_blocks = [b for b in blocks if b[0] != "mermaid"]

        print(f"File {fname:30} -> Total Code Blocks: {len(blocks):3} | Mermaid: {len(mermaid_blocks):2} | Other: {len(other_blocks):2}")

        # Check mermaid diagrams for common syntax errors
        for idx, m in enumerate(mermaid_blocks, 1):
            m_clean = m.strip()
            first_line = m_clean.split("\n")[0].strip()
            valid_starts = ["graph", "flowchart", "sequenceDiagram", "erDiagram", "classDiagram", "stateDiagram", "stateDiagram-v2", "gantt", "pie", "journey"]
            is_valid_start = any(first_line.startswith(vs) for vs in valid_starts)
            if not is_valid_start:
                print(f"  [WARNING] File {fname} Mermaid block #{idx} invalid start: '{first_line}'")

check_mermaid_and_code()
