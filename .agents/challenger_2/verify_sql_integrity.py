import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

sql_path = r'd:\Idea_DoAn\.agents\challenger_2\extracted_schema.sql'
with open(sql_path, 'r', encoding='utf-8') as f:
    full_sql = f.read()

# Remove comments
clean_sql = re.sub(r'--.*?$', '', full_sql, flags=re.MULTILINE)

# Parse Enums
enums = {}
for m in re.finditer(r'CREATE\s+TYPE\s+([a-zA-Z0-9_]+)\s+AS\s+ENUM\s*\((.*?)\);', clean_sql, re.DOTALL | re.IGNORECASE):
    ename = m.group(1).strip().lower()
    vals = [v.strip().strip("'\"") for v in m.group(2).split(',') if v.strip()]
    enums[ename] = vals

# Parse Tables
tables = {}
table_fks = {}

tbl_blocks = re.findall(r'CREATE\s+TABLE(?:\s+IF\s+NOT\s+EXISTS)?\s+([a-zA-Z0-9_]+)\s*\((.*?)\n\);', clean_sql, re.DOTALL | re.IGNORECASE)

for tname, body in tbl_blocks:
    tname = tname.lower().strip()
    columns = {}
    fks = []
    
    lines = body.split('\n')
    for line in lines:
        line = line.strip().rstrip(',')
        if not line or line.startswith('--'):
            continue
        
        fk_match = re.search(r'FOREIGN\s+KEY\s*\(([a-zA-Z0-9_,\s]+)\)\s*REFERENCES\s+([a-zA-Z0-9_]+)\s*\(([a-zA-Z0-9_]+)\)', line, re.IGNORECASE)
        if fk_match:
            col = fk_match.group(1).strip().lower()
            ref_tbl = fk_match.group(2).strip().lower()
            ref_col = fk_match.group(3).strip().lower()
            fks.append({'col': col, 'ref_tbl': ref_tbl, 'ref_col': ref_col, 'line': line})
            continue

        inline_fk = re.search(r'^([a-zA-Z0-9_]+)\s+([a-zA-Z0-9_()]+).*?REFERENCES\s+([a-zA-Z0-9_]+)\s*\(([a-zA-Z0-9_]+)\)', line, re.IGNORECASE)
        if inline_fk:
            col = inline_fk.group(1).strip().lower()
            ctype = inline_fk.group(2).strip().lower()
            ref_tbl = inline_fk.group(3).strip().lower()
            ref_col = inline_fk.group(4).strip().lower()
            columns[col] = {'type': ctype, 'raw': line}
            fks.append({'col': col, 'ref_tbl': ref_tbl, 'ref_col': ref_col, 'line': line})
            continue

        col_match = re.match(r'^([a-zA-Z0-9_]+)\s+([a-zA-Z0-9_()]+)(.*)$', line)
        if col_match:
            cname = col_match.group(1).lower()
            if cname in ['constraint', 'primary', 'foreign', 'unique', 'check']:
                continue
            ctype = col_match.group(2).lower()
            crest = col_match.group(3)
            columns[cname] = {'type': ctype, 'raw': line}

    tables[tname] = columns
    table_fks[tname] = fks

def parse_sql_values(vals_str):
    """Accurately parse SQL VALUES (...), (...) accounting for nested parens, quotes, etc."""
    rows = []
    in_quote = False
    quote_char = None
    paren_depth = 0
    cur_row = []
    
    for ch in vals_str:
        if ch in ["'", '"']:
            if not in_quote:
                in_quote = True
                quote_char = ch
            elif quote_char == ch:
                in_quote = False
                quote_char = None
            if paren_depth > 0:
                cur_row.append(ch)
        elif in_quote:
            cur_row.append(ch)
        elif ch == '(':
            if paren_depth == 0:
                cur_row = []
            else:
                cur_row.append(ch)
            paren_depth += 1
        elif ch == ')':
            paren_depth -= 1
            if paren_depth == 0:
                # Row completed
                row_str = "".join(cur_row).strip()
                if row_str:
                    # split values in row
                    row_vals = []
                    v_cur = []
                    v_quote = False
                    v_qchar = None
                    v_pdepth = 0
                    for vch in row_str:
                        if vch in ["'", '"']:
                            if not v_quote:
                                v_quote = True
                                v_qchar = vch
                            elif v_qchar == vch:
                                v_quote = False
                                v_qchar = None
                            v_cur.append(vch)
                        elif v_quote:
                            v_cur.append(vch)
                        elif vch == '(':
                            v_pdepth += 1
                            v_cur.append(vch)
                        elif vch == ')':
                            v_pdepth -= 1
                            v_cur.append(vch)
                        elif vch == ',' and v_pdepth == 0:
                            row_vals.append("".join(v_cur).strip())
                            v_cur = []
                        else:
                            v_cur.append(vch)
                    if v_cur:
                        row_vals.append("".join(v_cur).strip())
                    rows.append(row_vals)
                cur_row = []
            else:
                cur_row.append(ch)
        elif paren_depth > 0:
            cur_row.append(ch)
            
    return rows

print(f"\n=== INSERT DATA & SEED INTEGRITY CHECK ===")
insert_blocks = re.finditer(r'INSERT\s+INTO\s+([a-zA-Z0-9_]+)\s*\((.*?)\)\s*VALUES\s*(.*?);', clean_sql, re.DOTALL | re.IGNORECASE)

inserted_pks = {}
seed_errors = []
total_rows = 0

for m in insert_blocks:
    tname = m.group(1).lower().strip()
    cols_str = m.group(2)
    vals_str = m.group(3)
    
    if tname not in tables:
        seed_errors.append(f"INSERT into non-existent table '{tname}'")
        continue
    
    cols = [c.strip().lower() for c in cols_str.split(',') if c.strip()]
    for c in cols:
        if c not in tables[tname]:
            seed_errors.append(f"Table '{tname}' INSERT references non-existent column '{c}'")

    rows = parse_sql_values(vals_str)
    for r_idx, row_vals in enumerate(rows):
        total_rows += 1
        if len(row_vals) != len(cols):
            seed_errors.append(f"Table '{tname}' row #{r_idx+1}: Column count ({len(cols)}) != Value count ({len(row_vals)}) -> cols={cols}, vals={row_vals}")
            continue

        if 'id' in cols:
            id_idx = cols.index('id')
            id_val = row_vals[id_idx].strip("'\" ")
            if tname not in inserted_pks:
                inserted_pks[tname] = set()
            inserted_pks[tname].add(id_val)

        for c_idx, c in enumerate(cols):
            ctype = tables[tname][c]['type']
            if ctype in enums:
                val = row_vals[c_idx].strip("'\" ")
                if val not in enums[ctype] and not val.upper().startswith('DEFAULT') and val != 'NULL':
                    seed_errors.append(f"Table '{tname}' row #{r_idx+1} col '{c}' value '{val}' not in enum '{ctype}' {enums[ctype]}")

if seed_errors:
    print(f"Found {len(seed_errors)} Seed errors:")
    for err in seed_errors:
        print(f"  [FAIL] {err}")
else:
    print(f"[PASS] All {total_rows} INSERT rows across tables match columns, counts, and ENUM definitions 100%!")

print(f"\nInserted PKs tracked across {len(inserted_pks)} tables:")
for t, pks in inserted_pks.items():
    print(f"  - {t}: {len(pks)} record(s)")
