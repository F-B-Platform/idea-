import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"

with open(os.path.join(DIAG_DIR, "02_Sequence_Diagrams.md"), "r", encoding="utf-8") as f:
    seq_text = f.read()

with open(os.path.join(DIAG_DIR, "03_ERD_Database_Diagram.md"), "r", encoding="utf-8") as f:
    erd_text = f.read()

# ERD tables
erd_tables = sorted(list(set(re.findall(r'(\w+)\s*\{', erd_text))))
erd_tables_lower = [t.lower() for t in erd_tables]

print("ERD Tables (Normalized):")
print(erd_tables_lower)

# Extract SQL table names in 02_Sequence_Diagrams.md
sql_patterns = [
    r'FROM\s+([a-zA-Z0-9_]+)',
    r'INTO\s+([a-zA-Z0-9_]+)',
    r'UPDATE\s+([a-zA-Z0-9_]+)',
    r'JOIN\s+([a-zA-Z0-9_]+)'
]

seq_sql_tables = set()
for p in sql_patterns:
    found = re.findall(p, seq_text, re.I)
    for t in found:
        # filter out SQL keywords or false positives
        if t.upper() not in ['SELECT', 'SET', 'WHERE', 'VALUES', 'NOW', 'RETURNING', 'GROUP']:
            seq_sql_tables.add(t)

print(f"\nSQL Table names referenced in 02_Sequence_Diagrams.md ({len(seq_sql_tables)}):")
for t in sorted(list(seq_sql_tables)):
    t_low = t.lower()
    match = "EXACT" if t_low in erd_tables_lower else "NO_EXACT_MATCH"
    # Find close match
    close_matches = [e for e in erd_tables_lower if t_low in e or e in t_low]
    print(f"  - {t:30} -> {match:15} (ERD candidate: {close_matches})")
