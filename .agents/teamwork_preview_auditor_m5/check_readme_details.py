import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\README.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE README.md ===")

# Check Section headings
headings = re.findall(r"^#\s+(\d+\.\s+[^\n]+)", content, re.MULTILINE)
print(f"Top-level sections ({len(headings)}):")
for h in headings:
    print("  -", h)

# Check all 62 features in table
c_count = len(re.findall(r"\*\*C-\d+\*\*", content))
s_count = len(re.findall(r"\*\*S-\d+\*\*", content))
m_count = len(re.findall(r"\*\*M-\d+\*\*", content))
a_count = len(re.findall(r"\*\*A-\d+\*\*", content))
print(f"\nTraceability Matrix Feature Rows:")
print(f"  Customer features (C-01 ~ C-20): {c_count}/20")
print(f"  Staff features (S-01 ~ S-13): {s_count}/13")
print(f"  Manager features (M-01 ~ M-12): {m_count}/12")
print(f"  Admin features (A-01 ~ A-17): {a_count}/17")
print(f"  TOTAL: {c_count + s_count + m_count + a_count}/62")
