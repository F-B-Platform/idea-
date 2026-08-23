import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"

for fname in ["01_Kien_Truc_Tong_Quan.md", "02_Sequence_Diagrams.md", "03_ERD_Database_Diagram.md", "04_Deployment_Diagram.md"]:
    fpath = os.path.join(DIAG_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = re.findall(r'.{0,50}(?:hết món|out of stock|tồn kho|shortage|âm kho|negative stock|bù trừ|compensation|refund|hoàn tiền|86-toggle).{0,50}', content, re.I)
    print(f"File {fname}: Found {len(matches)} mentions of stock/refund/shortage/86-toggle")
    for m in matches[:5]:
        print(f"  ...{m.strip()}...")