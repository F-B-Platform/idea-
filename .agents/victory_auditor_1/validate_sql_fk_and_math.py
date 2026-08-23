import re
import sys
import uuid

sys.stdout.reconfigure(encoding='utf-8')

sql_path = r"d:\Idea_DoAn\.agents\victory_auditor_1\extracted_schema_and_seed.sql"

with open(sql_path, "r", encoding="utf-8") as f:
    sql_text = f.read()

print("=== DEEP SQL INTEGRITY & FOREIGN KEY AUDIT ===")

# Parse table schemas and column names
# Match CREATE TABLE <name> (...)
create_tables = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_\.]+)\s*\((.*?)\);", sql_text, re.DOTALL | re.IGNORECASE)

print(f"Total CREATE TABLE statements parsed: {len(create_tables)}")
table_defs = {}
for tbl_name, body in create_tables:
    t_clean = tbl_name.replace('"', '').split('.')[-1].strip().lower()
    cols = []
    fks = []
    lines = body.splitlines()
    for l in lines:
        l = l.strip().rstrip(',')
        if not l or l.startswith('--'):
            continue
        if re.match(r"CONSTRAINT\s+", l, re.IGNORECASE) or re.match(r"FOREIGN\s+KEY", l, re.IGNORECASE):
            # parse foreign key
            fk_m = re.search(r"FOREIGN\s+KEY\s*\(([a-zA-Z0-9_\,\s]+)\)\s*REFERENCES\s+([a-zA-Z0-9_\.]+)\s*\(([a-zA-Z0-9_\,\s]+)\)", l, re.IGNORECASE)
            if fk_m:
                col_name = fk_m.group(1).strip().lower()
                target_table = fk_m.group(2).replace('"', '').split('.')[-1].strip().lower()
                target_col = fk_m.group(3).strip().lower()
                fks.append((col_name, target_table, target_col))
        elif re.match(r"PRIMARY\s+KEY", l, re.IGNORECASE) or re.match(r"UNIQUE", l, re.IGNORECASE):
            continue
        else:
            # Column definition
            col_parts = l.split()
            if col_parts:
                col_name = col_parts[0].replace('"', '').strip().lower()
                cols.append(col_name)
                # Check inline REFERENCES
                ref_m = re.search(r"REFERENCES\s+([a-zA-Z0-9_\.]+)\s*\(([a-zA-Z0-9_\,\s]+)\)", l, re.IGNORECASE)
                if ref_m:
                    target_table = ref_m.group(1).replace('"', '').split('.')[-1].strip().lower()
                    target_col = ref_m.group(2).strip().lower()
                    fks.append((col_name, target_table, target_col))
    table_defs[t_clean] = {'cols': cols, 'fks': fks}

print(f"Parsed {len(table_defs)} table definitions.")

# Parse INSERT statements and collect all inserted rows as dicts
# e.g. INSERT INTO <table> (col1, col2, ...) VALUES (v1, v2, ...), (v1, v2, ...);
insert_stmts = re.findall(r"INSERT\s+INTO\s+([a-zA-Z0-9_\.]+)\s*\((.*?)\)\s*VALUES\s*(.*?);", sql_text, re.DOTALL | re.IGNORECASE)
print(f"Total INSERT INTO statements parsed: {len(insert_stmts)}")

inserted_data = {}

def parse_sql_value(val_str):
    val_str = val_str.strip()
    if val_str.upper() == 'NULL':
        return None
    if val_str.upper() in ('TRUE', 'FALSE'):
        return val_str.upper() == 'TRUE'
    if val_str.startswith("'") and val_str.endswith("'"):
        # unescape SQL quotes
        return val_str[1:-1].replace("''", "'")
    # try int or float
    try:
        if '.' in val_str:
            return float(val_str)
        return int(val_str)
    except ValueError:
        return val_str

for tbl_name, col_str, values_str in insert_stmts:
    t_clean = tbl_name.replace('"', '').split('.')[-1].strip().lower()
    cols = [c.replace('"', '').strip().lower() for c in col_str.split(',')]
    
    # parse tuples in values_str: (val1, val2, ...), (val1, val2, ...)
    # simple SQL tuple parser handling string literals
    rows = []
    in_str = False
    cur_tuple = []
    cur_val = []
    in_tuple = False
    
    i = 0
    while i < len(values_str):
        ch = values_str[i]
        if ch == "'" and not in_str:
            in_str = True
            cur_val.append(ch)
        elif ch == "'" and in_str:
            if i + 1 < len(values_str) and values_str[i+1] == "'":
                cur_val.append("''")
                i += 1
            else:
                in_str = False
                cur_val.append(ch)
        elif not in_str:
            if ch == '(':
                in_tuple = True
                cur_tuple = []
                cur_val = []
            elif ch == ')':
                if in_tuple:
                    cur_tuple.append(parse_sql_value("".join(cur_val)))
                    rows.append(cur_tuple)
                    in_tuple = False
                    cur_tuple = []
                    cur_val = []
            elif ch == ',':
                if in_tuple:
                    cur_tuple.append(parse_sql_value("".join(cur_val)))
                    cur_val = []
            elif ch in ('\n', '\r', '\t'):
                pass
            else:
                cur_val.append(ch)
        else:
            cur_val.append(ch)
        i += 1
    
    if t_clean not in inserted_data:
        inserted_data[t_clean] = []
    for r in rows:
        row_dict = {}
        for c_idx, c_name in enumerate(cols):
            if c_idx < len(r):
                row_dict[c_name] = r[c_idx]
        inserted_data[t_clean].append(row_dict)

print("\n--- Summary of Seed Data Records per Table ---")
for t, rows in inserted_data.items():
    print(f"  {t}: {len(rows)} records")

# 4. Check Foreign Key Consistency
print("\n--- 4. Checking Foreign Key Referencing Consistency ---")
fk_errors = []
total_fk_checks = 0

for t_clean, t_info in table_defs.items():
    fks = t_info['fks']
    rows = inserted_data.get(t_clean, [])
    for col_name, target_table, target_col in fks:
        target_rows = inserted_data.get(target_table, [])
        target_values = set(r.get(target_col) for r in target_rows if target_col in r)
        for r_idx, r in enumerate(rows):
            val = r.get(col_name)
            if val is not None:
                total_fk_checks += 1
                if val not in target_values:
                    fk_errors.append(f"Table '{t_clean}' row {r_idx+1} col '{col_name}'={val} NOT FOUND in target table '{target_table}'.'{target_col}'")

print(f"Total FK references checked: {total_fk_checks}")
if fk_errors:
    print(f"FK ERRORS FOUND: {len(fk_errors)}")
    for err in fk_errors[:20]:
        print(f"  [FAIL] {err}")
else:
    print("  [PASS] 100% Foreign Key and UUID References are completely VALID and RESOLVED!")

# 5. Check Math Arithmetic in Orders, Payments, Shifts, Z-Reports
print("\n--- 5. Mathematical Arithmetic Verification ---")

# 5.1 Order item subtotals and Order total
order_items = inserted_data.get('order_items', [])
orders = inserted_data.get('orders', [])
order_map = {o['id']: o for o in orders if 'id' in o}

order_calc = {}
for item in order_items:
    oid = item.get('order_id')
    qty = item.get('quantity', 1)
    price = item.get('unit_price', 0)
    subtotal = item.get('subtotal', qty * price)
    if oid not in order_calc:
        order_calc[oid] = 0
    order_calc[oid] += subtotal

print("\nValidating Orders Subtotal & Total Amounts:")
math_errors = []
for oid, o in order_map.items():
    calc_sub = order_calc.get(oid, 0)
    subtotal_db = o.get('subtotal', o.get('total_amount', 0))
    shipping_fee = o.get('shipping_fee', 0)
    discount = o.get('discount_amount', 0)
    total_db = o.get('final_amount', o.get('total_amount', 0))
    
    # Calculate expected total = subtotal + shipping_fee - discount
    expected_total = subtotal_db + (shipping_fee or 0) - (discount or 0)
    print(f"  Order {oid[:8]} ({o.get('order_type')}): Subtotal={subtotal_db}, Ship={shipping_fee}, Disc={discount}, TotalDB={total_db}, ExpectedTotal={expected_total}")
    if total_db != expected_total:
        math_errors.append(f"Order {oid} total mismatch: DB={total_db} vs Expected={expected_total}")

if not math_errors:
    print("  [PASS] All Order total calculations match subtotal + shipping - discount exactly!")
else:
    for e in math_errors:
        print(f"  [FAIL] {e}")

# 5.2 Payments match Order total
payments = inserted_data.get('payments', [])
print(f"\nValidating {len(payments)} Payments against Orders:")
for p in payments:
    oid = p.get('order_id')
    p_amount = p.get('amount')
    if oid in order_map:
        o = order_map[oid]
        o_total = o.get('final_amount', o.get('total_amount'))
        print(f"  Payment {p.get('id', '')[:8]}: Amount={p_amount}, OrderTotal={o_total}, Status={p.get('status')}")
        if p_amount != o_total:
            print(f"    [WARN/FAIL] Payment amount {p_amount} != Order total {o_total}")
            math_errors.append(f"Payment amount mismatch for order {oid}")

# 5.3 Shifts & Cash Drawer Reconciliation
shifts = inserted_data.get('shifts', [])
print(f"\nValidating {len(shifts)} Shifts / Cash Drawer Reconciliation:")
for s in shifts:
    open_cash = s.get('opening_cash', s.get('initial_cash', 0)) or 0
    cash_sales = s.get('cash_sales', s.get('total_cash_sales', 0)) or 0
    cash_refunds = s.get('cash_refunds', 0) or 0
    expected_cash = s.get('expected_cash', open_cash + cash_sales - cash_refunds)
    actual_cash = s.get('actual_cash', s.get('closing_cash', 0))
    diff = s.get('difference', (actual_cash or 0) - (expected_cash or 0)) if actual_cash is not None else 0
    note = s.get('notes', s.get('discrepancy_reason', ''))
    print(f"  Shift {s.get('id', '')[:8]}: Open={open_cash:,}, CashSales={cash_sales:,}, Expected={expected_cash:,}, Actual={actual_cash}, Diff={diff}, Note='{note}'")
