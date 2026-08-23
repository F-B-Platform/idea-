import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE 04_Thiet_Ke_UI_UX.md ===")

# Check 5 Route Groups
routes = re.findall(r"##\s+4\.\d+\s+Route Group\s+\d+:\s+`([^`]+)`", content)
print(f"Route Groups defined: {routes}")

# Check 7 Core Business Flows
flows = re.findall(r"###\s+3\.\d+\s+Luồng\s+\d+:\s+([^\n]+)", content)
print(f"\nCore Business Flows ({len(flows)}):")
for f in flows:
    print(f"  - {f}")

# Check 20 ASCII Wireframes
wireframes = re.findall(r"####\s+Khung\s+\d+:\s+([^\n]+)", content)
print(f"\nASCII Wireframes ({len(wireframes)}):")
for wf in wireframes:
    print(f"  - {wf}")

# Check WCAG and Traceability Matrix
print("\nWCAG 2.1 AA section present:", bool(re.search(r"WCAG\s+2\.1", content)))
print("Ma trận 62 tính năng UI present:", bool(re.search(r"MA TRẬN TRUY VẾT 62 TÍNH NĂNG", content)))
