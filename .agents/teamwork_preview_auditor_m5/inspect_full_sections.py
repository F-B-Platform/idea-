import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def print_section_full(filepath, heading):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(heading, content)
    if match:
        start = match.start()
        print(f"=== {filepath} ===")
        print(content[start:start+3000])

print_section_full(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md", r"# 8\.\s+PHÂN BỔ TRÁCH NHIỆM")
print_section_full(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md", r"# 6\.\s+PHÂN BỔ TRÁCH NHIỆM")
