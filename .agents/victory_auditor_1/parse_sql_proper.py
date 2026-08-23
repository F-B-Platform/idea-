import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

sql_path = r"d:\Idea_DoAn\.agents\victory_auditor_1\extracted_schema_and_seed.sql"

with open(sql_path, "r", encoding="utf-8") as f:
    raw_sql = f.read()

# Strip multi-line comments /* ... */
clean_sql = re.sub(r"/\*.*?\*/", "", raw_sql, flags=re.DOTALL)

# Strip single-line comments -- ...
lines = []
for l in clean_sql.splitlines():
    in_quote = False
    cut_idx = len(l)
    for i in range(len(l)):
        if l[i] == "'" and (i == 0 or l[i-1] != '\\'):
            in_quote = not in_quote
        elif not in_quote and l[i:i+2] == '--':
            cut_idx = i
            break
    lines.append(l[:cut_idx])

clean_sql = "\n".join(lines)

# Split statements by semicolon outside DO $$ blocks and functions
statements = []
cur_stmt = []
in_do_block = False
in_quote = False

i = 0
while i < len(clean_sql):
    if clean_sql[i:i+2] == "$$":
        in_do_block = not in_do_block
        cur_stmt.append("$$")
        i += 2
        continue
    elif clean_sql[i] == "'" and not in_do_block:
        in_quote = not in_quote
        cur_stmt.append("'")
        i += 1
        continue
    elif clean_sql[i] == ';' and not in_do_block and not in_quote:
        cur_stmt_str = "".join(cur_stmt).strip()
        if cur_stmt_str:
            statements.append(cur_stmt_str)
        cur_stmt = []
        i += 1
        continue
    else:
        cur_stmt.append(clean_sql[i])
        i += 1

if "".join(cur_stmt).strip():
    statements.append("".join(cur_stmt).strip())

create_table_stmts = [s for s in statements if re.match(r"CREATE\s+TABLE", s, re.IGNORECASE)]
insert_stmts = [s for s in statements if re.match(r"INSERT\s+INTO", s, re.IGNORECASE)]

# Parse Tables, Columns, PKs, FKs
table_defs = {}
for stmt in create_table_stmts:
    m = re.match(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_\.\"]+)\s*\((.*)\)", stmt, re.DOTALL | re.IGNORECASE)
    if not m:
        continue
    t_name = m.group(1).replace('"', '').split('.')[-1].strip().lower()
    body = m.group(2)
    cols = []
    fks = []
    pk = None
    
    col_defs = []
    p_depth = 0
    cur_cd = []
    for ch in body:
        if ch == '(':
            p_depth += 1
            cur_cd.append(ch)
        elif ch == ')':
            p_depth -= 1
            cur_cd.append(ch)
        elif ch == ',' and p_depth == 0:
            col_defs.append("".join(cur_cd).strip())
            cur_cd = []
        else:
            cur_cd.append(ch)
    if "".join(cur_cd).strip():
        col_defs.append("".join(cur_cd).strip())
        
    for cd in col_defs:
        cd_clean = " ".join(cd.split())
        if re.match(r"CONSTRAINT\s+", cd_clean, re.IGNORECASE) or re.match(r"FOREIGN\s+KEY", cd_clean, re.IGNORECASE):
            fk_m = re.search(r"FOREIGN\s+KEY\s*\(([a-zA-Z0-9_\,\s]+)\)\s*REFERENCES\s+([a-zA-Z0-9_\.]+)\s*\(([a-zA-Z0-9_\,\s]+)\)", cd_clean, re.IGNORECASE)
            if fk_m:
                col_name = fk_m.group(1).strip().lower()
                tgt_tbl = fk_m.group(2).replace('"', '').split('.')[-1].strip().lower()
                tgt_col = fk_m.group(3).strip().lower()
                fks.append((col_name, tgt_tbl, tgt_col))
        elif re.match(r"PRIMARY\s+KEY", cd_clean, re.IGNORECASE):
            pk_m = re.search(r"PRIMARY\s+KEY\s*\(([a-zA-Z0-9_\,\s]+)\)", cd_clean, re.IGNORECASE)
            if pk_m:
                pk = [c.strip().lower() for c in pk_m.group(1).split(',')]
        elif re.match(r"CHECK\s*\(", cd_clean, re.IGNORECASE) or re.match(r"UNIQUE\s*\(", cd_clean, re.IGNORECASE):
            continue
        else:
            parts = cd_clean.split()
            if parts:
                c_name = parts[0].replace('"', '').strip().lower()
                cols.append(c_name)
                if "PRIMARY KEY" in cd_clean.upper():
                    pk = [c_name]
                ref_m = re.search(r"REFERENCES\s+([a-zA-Z0-9_\.]+)\s*\(([a-zA-Z0-9_\,\s]+)\)", cd_clean, re.IGNORECASE)
                if ref_m:
                    tgt_tbl = ref_m.group(1).replace('"', '').split('.')[-1].strip().lower()
                    tgt_col = ref_m.group(2).strip().lower()
                    fks.append((c_name, tgt_tbl, tgt_col))
    table_defs[t_name] = {'cols': cols, 'fks': fks, 'pk': pk}

# Parse Insert Data
inserted_rows = {}

def parse_sql_value(val_str):
    val_str = val_str.strip()
    if val_str.upper() == 'NULL':
        return None
    if val_str.upper() == 'TRUE':
        return True
    if val_str.upper() == 'FALSE':
        return False
    if val_str.startswith("'") and val_str.endswith("'"):
        return val_str[1:-1].replace("''", "'")
    try:
        if '.' in val_str:
            return float(val_str)
        return int(val_str)
    except ValueError:
        return val_str

for stmt in insert_stmts:
    m = re.match(r"INSERT\s+INTO\s+([a-zA-Z0-9_\.]+)\s*\((.*?)\)\s*VALUES\s*(.*)", stmt, re.DOTALL | re.IGNORECASE)
    if not m:
        continue
    t_name = m.group(1).replace('"', '').split('.')[-1].strip().lower()
    col_names = [c.replace('"', '').strip().lower() for c in m.group(2).split(',')]
    values_part = m.group(3).strip()
    
    # Strip ON CONFLICT ...
    values_part = re.sub(r"ON\s+CONFLICT\s+.*$", "", values_part, flags=re.DOTALL | re.IGNORECASE).strip()
    
    # Parse tuples
    tuples = []
    in_s = False
    in_t = False
    cur_t = []
    cur_v = []
    idx = 0
    while idx < len(values_part):
        ch = values_part[idx]
        if ch == "'" and not in_s:
            in_s = True
            cur_v.append(ch)
        elif ch == "'" and in_s:
            if idx + 1 < len(values_part) and values_part[idx+1] == "'":
                cur_v.append("''")
                idx += 1
            else:
                in_s = False
                cur_v.append(ch)
        elif not in_s:
            if ch == '(':
                in_t = True
                cur_t = []
                cur_v = []
            elif ch == ')':
                if in_t:
                    cur_t.append(parse_sql_value("".join(cur_v)))
                    tuples.append(cur_t)
                    in_t = False
                    cur_t = []
                    cur_v = []
            elif ch == ',':
                if in_t:
                    cur_t.append(parse_sql_value("".join(cur_v)))
                    cur_v = []
            elif ch in ('\n', '\r', '\t', ' '):
                pass
            else:
                cur_v.append(ch)
        else:
            cur_v.append(ch)
        idx += 1
        
    if t_name not in inserted_rows:
        inserted_rows[t_name] = []
    for tup in tuples:
        row_dict = {}
        for c_idx, c_name in enumerate(col_names):
            if c_idx < len(tup):
                row_dict[c_name] = tup[c_idx]
        inserted_rows[t_name].append(row_dict)

print("\n--- Summary of Parsed Seed Data (Accurate) ---")
total_records = sum(len(r) for r in inserted_rows.values())
print(f"Total inserted records across all tables: {total_records}")
for t_name, rows in inserted_rows.items():
    print(f"  {t_name:25s}: {len(rows):3d} rows")

# Validate Foreign Keys
print("\n--- Validating Foreign Key Relationships ---")
fk_errors = []
fk_checks = 0

for t_name, t_info in table_defs.items():
    fks = t_info['fks']
    rows = inserted_rows.get(t_name, [])
    for col_name, tgt_tbl, tgt_col in fks:
        tgt_rows = inserted_rows.get(tgt_tbl, [])
        valid_tgt_vals = set(r.get(tgt_col) for r in tgt_rows if tgt_col in r)
        for r_idx, r in enumerate(rows):
            val = r.get(col_name)
            if val is not None:
                fk_checks += 1
                if val not in valid_tgt_vals:
                    fk_errors.append(f"Table '{t_name}' [row {r_idx+1}]: FK '{col_name}' = '{val}' does NOT exist in target '{tgt_tbl}'.'{tgt_col}'")

print(f"Total Foreign Key references verified: {fk_checks}")
if fk_errors:
    print(f"FAILED FK CHECKS: {len(fk_errors)}")
    for err in fk_errors:
        print(f"  [FAIL] {err}")
else:
    print("  [PASS] ZERO FK ERRORS! 100% of foreign keys and UUIDs are properly resolved and valid!")
