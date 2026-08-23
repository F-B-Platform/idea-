import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"

def read_file(name):
    with open(os.path.join(DIAG_DIR, name), "r", encoding="utf-8") as f:
        return f.read()

f01 = read_file("01_Kien_Truc_Tong_Quan.md")
f02 = read_file("02_Sequence_Diagrams.md")
f03 = read_file("03_ERD_Database_Diagram.md")
f04 = read_file("04_Deployment_Diagram.md")

print("=== DEEP ERD ANALYSIS ===")
# Extract all relationships in 03_ERD_Database_Diagram.md
rel_pattern = r'([A-Z0-9_]+)\s+([|o\}\{]+--[|o\}\{]+)\s+([A-Z0-9_]+)\s*:\s*\"([^\"]*)\"'
rels = re.findall(rel_pattern, f03)
print(f"Found {len(rels)} entity relationships in ERD:")
for r in rels:
    print(f"  {r[0]} {r[1]} {r[2]} : \"{r[3]}\"")

# Extract table attributes in ERD
table_attr_pattern = r'([A-Z0-9_]+)\s*\{([^}]+)\}'
table_blocks = re.findall(table_attr_pattern, f03)
print(f"\nFound {len(table_blocks)} entity attribute blocks in ERD:")
erd_schema = {}
for tname, body in table_blocks:
    lines = [l.strip() for l in body.strip().split('\n') if l.strip()]
    fields = []
    for l in lines:
        parts = l.split()
        if len(parts) >= 2:
            fields.append((parts[0], parts[1], ' '.join(parts[2:]) if len(parts) > 2 else ''))
    erd_schema[tname] = fields
    print(f"  Entity {tname:30} has {len(fields):2} attributes")

print("\n=== DEEP SEQUENCE CONCURRENCY ANALYSIS ===")
for seq_id in range(1, 11):
    seq_name = f"SEQ-{seq_id:02d}"
    # Find section
    pattern = rf"#\s+\d+\.\s+{seq_name}:([^\n]+)"
    m = re.search(pattern, f02, re.I)
    title = m.group(1).strip() if m else "Not found"
    print(f"\n[{seq_name}] {title}")
    
    # Extract content of this sequence section
    sec_pattern = rf"#\s+\d+\.\s+{seq_name}:.*?(?=#\s+\d+\.\s+SEQ|\Z)"
    sec_m = re.search(sec_pattern, f02, re.DOTALL | re.I)
    if sec_m:
        sec_text = sec_m.group(0)
        # Check concurrency mentions
        has_redlock = bool(re.search(r"redlock|lock|mutex", sec_text, re.I))
        has_idempotency = bool(re.search(r"idempotent|idempotency|x-idempotency", sec_text, re.I))
        has_rollback = bool(re.search(r"rollback|release|unlock|compensat", sec_text, re.I))
        has_signalr = bool(re.search(r"signalr|hub|websocket|broadcast", sec_text, re.I))
        has_db_tx = bool(re.search(r"transaction|begin|commit|acid", sec_text, re.I))
        print(f"   - RedLock/Locking: {'YES' if has_redlock else 'NO'}")
        print(f"   - Idempotency:     {'YES' if has_idempotency else 'NO'}")
        print(f"   - Rollback/Unlock: {'YES' if has_rollback else 'NO'}")
        print(f"   - SignalR/Realtime:{'YES' if has_signalr else 'NO'}")
        print(f"   - DB Transaction:  {'YES' if has_db_tx else 'NO'}")
