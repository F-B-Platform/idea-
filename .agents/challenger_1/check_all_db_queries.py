import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"

with open(os.path.join(DIAG_DIR, "02_Sequence_Diagrams.md"), "r", encoding="utf-8") as f:
    seq_text = f.read()

# Find all DB interactions in all sequences
db_queries = re.findall(r'(API->>DB|DB->>API|CRON->>DB|POS->>DB|ST->>DB):\s*([^\n]+)', seq_text)
print(f"Total DB Interactions in Sequence Diagrams: {len(db_queries)}")
for who, q in db_queries:
    print(f"{who:12}: {q}")