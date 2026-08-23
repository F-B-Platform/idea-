import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md", "r", encoding="utf-8") as f:
    content = f.read()

# Search for wireframe headings in section 4
m = re.findall(r"###\s+4\.\d+\.\d+\s+([^\n]+)", content)
print(f"Wireframe subheadings found with ### 4.x.x ({len(m)}):")
for item in m:
    print("  -", item)
