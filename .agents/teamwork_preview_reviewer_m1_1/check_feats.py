import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

f1_path = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md"
proj_path = r"d:\Idea_DoAn\.agents\teamwork_preview_orchestrator_1\PROJECT.md"

with open(f1_path, "r", encoding="utf-8") as f:
    f1 = f.read()

with open(proj_path, "r", encoding="utf-8") as f:
    proj = f.read()

# Extract from PROJECT.md
proj_feats = re.findall(r"\|\s*\d+\s*\|\s*([A-Z]-\d{2})\s*\|\s*([^|]+)\s*\|\s*([A-Za-z]+)\s*\|", proj)
print(f"Features in PROJECT.md: {len(proj_feats)}")

# Extract from 01_
f1_feats = re.findall(r"###\s+([A-Z]-\d{2})[:\s\-]+([^\n]+)", f1)
print(f"Features in 01_Phan_Tich_Yeu_Cau.md: {len(f1_feats)}")

for code, title in f1_feats:
    print(f"  {code}: {title.strip()}")

# Check RTM table in 01_
rtm_matches = re.findall(r"\|\s*([A-Z]-\d{2})\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|", f1)
print(f"\nRTM Rows in 01_: {len(rtm_matches)}")

