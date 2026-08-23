import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def check_section(filepath, start_pattern):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(start_pattern, content)
    if match:
        start_pos = match.start()
        print(f"=== {filepath} ({start_pattern}) ===")
        print(content[start_pos:start_pos+1500])
    else:
        print(f"Pattern {start_pattern} NOT FOUND in {filepath}")

check_section(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md", r"# 8\.\s+PHÂN BỔ TRÁCH NHIỆM")
check_section(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md", r"# 6\.\s+PHÂN BỔ TRÁCH NHIỆM")
