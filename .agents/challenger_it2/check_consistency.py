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

# 1. Extract all ERD table definitions and column names
erd_tables = {}

table_headers = re.findall(r'###\s+Bảng\s+\d+:\s+`([^`]+)`', erd_content)
print(f"Found {len(table_headers)} tables in ERD Data Dictionary:")
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
    print(f"  - {t} ({len(cols)} columns): {', '.join(cols[:5])}...")

# Check for forbidden legacy patterns in 02_Sequence_Diagrams.md
# Note: GPS/50m mentions might appear in context descriptions as "Loại bỏ GPS 50m".
# We want to make sure they are NOT used as an active mechanism.
legacy_forbidden_patterns = [
    (r'\bProductBOMs\b', 'Legacy table ProductBOMs'),
    (r'\bIngredients\.CurrentStock\b', 'Legacy column Ingredients.CurrentStock'),
    (r'\bInventoryTransactions\b', 'Legacy table InventoryTransactions'),
    (r'\bIngredients\.current_stock\b', 'Legacy column Ingredients.current_stock'),
    (r'\bstock_transactions\b', 'Legacy table stock_transactions'),
    (r'\bbom_recipes\b', 'Legacy table bom_recipes'),
    (r'\bproduct_boms\b', 'Legacy table product_boms')
]

print("\n========================================")
print("CHECKING FOR FORBIDDEN LEGACY PATTERNS IN 02_Sequence_Diagrams.md:")
forbidden_matches = []
for pat, desc in legacy_forbidden_patterns:
    matches = re.findall(pat, seq_content, re.IGNORECASE)
    if matches:
        print(f"[FAIL] FOUND FORBIDDEN PATTERN: {desc} ({pat}) -> matches: {matches}")
        forbidden_matches.append((pat, matches))
    else:
        print(f"[PASS] NOT FOUND: {desc}")

# 2. Extract and check all SQL queries and schema references
print("\n========================================")
print("CHECKING SQL STATEMENTS AGAINST ERD TABLES & COLUMNS:")
sql_lines = []
for line_no, line in enumerate(seq_content.split('\n'), 1):
    if any(k in line for k in ['SELECT', 'INSERT INTO', 'UPDATE', 'DELETE FROM']):
        sql_lines.append((line_no, line.strip()))

print(f"Found {len(sql_lines)} SQL interaction lines.")

valid_table_names = set(erd_tables.keys())
inconsistencies = []

# List of all extracted table occurrences
referenced_tables = set()

for lno, s in sql_lines:
    # Find table names after FROM, JOIN, INSERT INTO, UPDATE
    # e.g., INSERT INTO orders (...)
    # e.g., UPDATE tables SET ...
    # e.g., SELECT ... FROM product_recipes r WHERE ...
    # e.g., SELECT ... FROM inventory_stocks s JOIN ingredients i ON ...
    tables_in_line = re.findall(r'(?:FROM|JOIN|INSERT INTO|UPDATE)\s+([a-zA-Z0-9_]+)', s, re.IGNORECASE)
    for tbl in tables_in_line:
        tbl_lower = tbl.lower()
        if tbl_lower in ['coalesce', 'sum', 'count', 'avg', 'min', 'max', 'now', 'interval']:
            continue
        referenced_tables.add(tbl_lower)
        if tbl_lower not in valid_table_names:
            print(f"Line {lno:4d} [INVALID TABLE]: '{tbl}' not in ERD! -> {s}")
            inconsistencies.append((lno, f"Table '{tbl}' invalid", s))
        else:
            # Check columns in INSERT INTO table (col1, col2, ...)
            insert_match = re.search(r'INSERT INTO\s+([a-zA-Z0-9_]+)\s*\(([^)]+)\)', s, re.IGNORECASE)
            if insert_match:
                ins_table = insert_match.group(1).lower()
                ins_cols = [c.split('=')[0].strip().lower() for c in insert_match.group(2).split(',') if c.strip()]
                for col in ins_cols:
                    if col and col not in erd_tables.get(ins_table, []):
                        print(f"Line {lno:4d} [INVALID COL in {ins_table}]: '{col}' not in {ins_table}! -> {s}")
                        inconsistencies.append((lno, f"Column '{col}' not in table '{ins_table}'", s))

            # Check columns in UPDATE table SET col1 = ..., col2 = ... WHERE col3 = ...
            update_match = re.search(r'UPDATE\s+([a-zA-Z0-9_]+)\s+SET\s+([^W]+)(?:WHERE\s+(.+))?', s, re.IGNORECASE)
            if update_match:
                upd_table = update_match.group(1).lower()
                set_part = update_match.group(2)
                # parse set columns
                set_cols = [c.split('=')[0].strip().lower() for c in set_part.split(',') if c.strip()]
                for col in set_cols:
                    # sometimes "col = col - 80"
                    col_clean = col.split()[0].strip().lower()
                    if col_clean and col_clean not in erd_tables.get(upd_table, []):
                        print(f"Line {lno:4d} [INVALID COL in UPDATE {upd_table}]: '{col_clean}' not in {upd_table}! -> {s}")
                        inconsistencies.append((lno, f"Column '{col_clean}' not in table '{upd_table}'", s))

print(f"\nTotal Referenced Tables in Sequence SQLs: {len(referenced_tables)}")
print(f"Referenced: {sorted(list(referenced_tables))}")
print(f"Total Schema Inconsistencies: {len(inconsistencies)}")

with open(r"d:\Idea_DoAn\.agents\challenger_it2\consistency_report.json", "w", encoding="utf-8") as f:
    json.dump({
        "forbidden_matches": forbidden_matches,
        "referenced_tables": list(referenced_tables),
        "inconsistencies": inconsistencies,
        "total_sql_lines": len(sql_lines)
    }, f, indent=2, ensure_ascii=False)
