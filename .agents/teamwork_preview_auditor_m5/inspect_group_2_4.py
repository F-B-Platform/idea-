import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for endpoint blocks: e.g. `POST /api/v1/...`
endpoints = re.findall(r"(?:`?(?:POST|GET|PUT|DELETE|PATCH)\s+[^`\n]+`?)", content)
print(f"Total API HTTP method mentions: {len(endpoints)}")
for ep in endpoints[:20]:
    print("  ", ep.strip())

# Print sample from Group 2.4 (Orders)
m = re.search(r"##\s+2\.4\s+Nhóm\s+4:", content)
if m:
    print("\n--- SAMPLE FROM GROUP 2.4 (ORDERS) ---")
    print(content[m.start():m.start()+2000])
