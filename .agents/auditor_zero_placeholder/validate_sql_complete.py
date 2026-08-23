import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SEED_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
with open(SEED_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Extract SQL blocks
sql_blocks = re.findall(r"```sql\n(.*?)```", content, re.DOTALL)
combined_sql = "\n".join(sql_blocks)

# Remove single line comments -- ...
def clean_sql(sql_str):
    lines = []
    for line in sql_str.splitlines():
        # remove -- comment if not in quotes
        clean_line = re.sub(r"--.*$", "", line)
        if clean_line.strip():
            lines.append(clean_line)
    return "\n".join(lines)

clean = clean_sql(combined_sql)

# Split statements by ;
# but respect string literals and DO $$ ... $$
statements = []
current_stmt = []
in_string = False
in_dollar = False

for line in clean.splitlines():
    current_stmt.append(line)
    if ";" in line:
        # check if line ends with ;
        if line.strip().endswith(";"):
            statements.append("\n".join(current_stmt))
            current_stmt = []

if current_stmt and "\n".join(current_stmt).strip():
    statements.append("\n".join(current_stmt))

print(f"Total SQL Statements: {len(statements)}")

create_table_stmts = [s for s in statements if s.strip().upper().startswith("CREATE TABLE")]
insert_stmts = [s for s in statements if s.strip().upper().startswith("INSERT INTO")]
create_index_stmts = [s for s in statements if s.strip().upper().startswith("CREATE INDEX") or s.strip().upper().startswith("CREATE UNIQUE INDEX")]
create_extension_stmts = [s for s in statements if "CREATE EXTENSION" in s.upper()]

print(f"  CREATE EXTENSION: {len(create_extension_stmts)}")
print(f"  CREATE TABLE: {len(create_table_stmts)}")
print(f"  CREATE INDEX: {len(create_index_stmts)}")
print(f"  INSERT INTO: {len(insert_stmts)}")

print("\n--- Detailed INSERT INTO Row Counts ---")
total_rows = 0
for idx, s in enumerate(insert_stmts, 1):
    m = re.match(r"INSERT\s+INTO\s+([a-zA-Z0-9_\.\"]+)", s, re.IGNORECASE)
    tname = m.group(1) if m else "unknown"
    # count tuples
    # Values block
    val_idx = s.upper().find("VALUES")
    if val_idx != -1:
        val_block = s[val_idx:]
        tuples = re.findall(r"\([^\)]+\)", val_block)
        count = len(tuples)
    else:
        count = 0
    total_rows += count
    print(f"{idx:02d}. {tname:<30} -> {count:>3} rows")

print(f"\nTOTAL SEED ROWS INSERTED: {total_rows}")
