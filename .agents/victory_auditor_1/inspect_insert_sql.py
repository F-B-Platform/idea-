import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

sql_path = r"d:\Idea_DoAn\.agents\victory_auditor_1\extracted_schema_and_seed.sql"
with open(sql_path, "r", encoding="utf-8") as f:
    sql_text = f.read()

# Search for INSERT INTO tables
m = re.search(r"INSERT\s+INTO\s+tables.*?;", sql_text, re.DOTALL | re.IGNORECASE)
if m:
    print("=== INSERT INTO tables ===")
    print(m.group(0))

m2 = re.search(r"INSERT\s+INTO\s+user_roles.*?;", sql_text, re.DOTALL | re.IGNORECASE)
if m2:
    print("\n=== INSERT INTO user_roles ===")
    print(m2.group(0))
