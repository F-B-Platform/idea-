import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

sql_path = r"d:\Idea_DoAn\.agents\victory_auditor_1\extracted_schema_and_seed.sql"
with open(sql_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines[:120]):
    print(f"{i+1:3d}: {l.rstrip()}")
