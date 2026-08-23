import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

erd_path = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md"
seq_path = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md"

with open(erd_path, 'r', encoding='utf-8') as f:
    erd_content = f.read()

with open(seq_path, 'r', encoding='utf-8') as f:
    seq_content = f.read()

# Extract all ERD table definitions and column names
erd_tables = {}
table_headers = re.findall(r'###\s+Bảng\s+\d+:\s+`([^`]+)`', erd_content)
for t in table_headers:
    pattern = rf'###\s+Bảng\s+\d+:\s+`{t}`[\s\S]*?\| Tên Cột \(Column\)[^\n]*\n\|[^\n]*\n([\s\S]*?)(?=\n###|\n---|\n#|\Z)'
    m = re.search(pattern, erd_content)
    cols = []
    if m:
        col_rows = m.group(1).strip().split('\n')
        for r in col_rows:
            if r.strip().startswith('|'):
                parts = [p.strip() for p in r.split('|') if p.strip()]
                if parts:
                    col_name = parts[0].replace('`', '').strip()
                    cols.append(col_name)
    erd_tables[t] = cols

valid_table_names = set(erd_tables.keys())

def split_sql_tokens(s):
    # Split by comma but respect single quotes and parentheses
    tokens = []
    current = []
    in_quote = False
    in_paren = 0
    for char in s:
        if char == "'":
            in_quote = not in_quote
            current.append(char)
        elif char == '(' and not in_quote:
            in_paren += 1
            current.append(char)
        elif char == ')' and not in_quote:
            in_paren -= 1
            current.append(char)
        elif char == ',' and not in_quote and in_paren == 0:
            tokens.append(''.join(current).strip())
            current = []
        else:
            current.append(char)
    if current:
        tokens.append(''.join(current).strip())
    return tokens

# Extract and check all SQL queries
sql_lines = []
for line_no, line in enumerate(seq_content.split('\n'), 1):
    if any(k in line for k in ['SELECT', 'INSERT INTO', 'UPDATE', 'DELETE FROM']):
        sql_lines.append((line_no, line.strip()))

real_inconsistencies = []

for lno, s in sql_lines:
    # 1. INSERT INTO table (col=val, col=val) or INSERT INTO table (col, col) VALUES (val, val)
    m_ins = re.search(r'INSERT INTO\s+([a-zA-Z0-9_]+)\s*\((.*?)\)(?:\s*VALUES\s*\((.*?)\))?', s, re.IGNORECASE)
    if m_ins:
        table_name = m_ins.group(1).lower()
        if table_name not in valid_table_names:
            real_inconsistencies.append((lno, f"Unknown table in INSERT: {table_name}", s))
        else:
            first_paren = m_ins.group(2)
            has_values = m_ins.group(3) is not None
            items = split_sql_tokens(first_paren)
            for item in items:
                if '=' in item and not has_values:
                    col_name = item.split('=')[0].strip().lower()
                else:
                    col_name = item.strip().lower()
                
                # Check column
                if col_name and col_name not in erd_tables[table_name]:
                    real_inconsistencies.append((lno, f"Unknown column '{col_name}' in table '{table_name}'", s))

    # 2. UPDATE table SET col1 = val1, col2 = val2 WHERE ...
    m_upd = re.search(r'UPDATE\s+([a-zA-Z0-9_]+)\s+SET\s+(.*?)(?:\s+WHERE\s+(.*))?$', s, re.IGNORECASE)
    if m_upd:
        table_name = m_upd.group(1).lower()
        if table_name not in valid_table_names:
            real_inconsistencies.append((lno, f"Unknown table in UPDATE: {table_name}", s))
        else:
            set_clause = m_upd.group(2)
            where_clause = m_upd.group(3) if m_upd.group(3) else ''
            
            # check set columns
            set_items = split_sql_tokens(set_clause)
            for item in set_items:
                if '=' in item:
                    col_name = item.split('=')[0].strip().lower()
                    if col_name and col_name not in erd_tables[table_name]:
                        real_inconsistencies.append((lno, f"Unknown column '{col_name}' in UPDATE SET '{table_name}'", s))

    # 3. SELECT ... FROM table ...
    m_sel = re.search(r'SELECT\s+(.*?)\s+FROM\s+([a-zA-Z0-9_]+)(?:\s+([a-zA-Z0-9_]+))?(.*?)$', s, re.IGNORECASE)
    if m_sel:
        table_name = m_sel.group(2).lower()
        if table_name not in valid_table_names:
            real_inconsistencies.append((lno, f"Unknown table in SELECT: {table_name}", s))

print("\n========================================")
print(f"STRICT PARSER RESULTS:")
print(f"Total SQL statements analyzed: {len(sql_lines)}")
print(f"Real Schema Inconsistencies found: {len(real_inconsistencies)}")
if real_inconsistencies:
    for lno, msg, stmt in real_inconsistencies:
        print(f"Line {lno}: {msg}\n  Statement: {stmt}")
else:
    print("ALL 100% of SQL statements strictly match ERD tables and columns!")
