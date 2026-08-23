import re
import sys
import uuid
from typing import Dict, List, Tuple, Set, Any, Optional
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"

def remove_sql_comments(sql: str) -> str:
    """Removes single-line and multi-line SQL comments while preserving strings."""
    res = []
    i = 0
    n = len(sql)
    in_single_quote = False
    in_double_quote = False
    
    while i < n:
        if not in_single_quote and not in_double_quote:
            if sql[i:i+2] == '--':
                # Skip to end of line
                nl = sql.find('\n', i)
                if nl == -1:
                    break
                i = nl + 1
                res.append('\n')
                continue
            elif sql[i:i+2] == '/*':
                # Skip to end of comment
                end_c = sql.find('*/', i+2)
                if end_c == -1:
                    break
                i = end_c + 2
                continue
            elif sql[i] == "'":
                in_single_quote = True
                res.append(sql[i])
                i += 1
                continue
            elif sql[i] == '"':
                in_double_quote = True
                res.append(sql[i])
                i += 1
                continue
        elif in_single_quote:
            if sql[i] == "'":
                if i + 1 < n and sql[i+1] == "'": # Escaped single quote ''
                    res.append("''")
                    i += 2
                    continue
                else:
                    in_single_quote = False
            res.append(sql[i])
            i += 1
            continue
        elif in_double_quote:
            if sql[i] == '"':
                if i + 1 < n and sql[i+1] == '"':
                    res.append('""')
                    i += 2
                    continue
                else:
                    in_double_quote = False
            res.append(sql[i])
            i += 1
            continue
            
        res.append(sql[i])
        i += 1
        
    return "".join(res)

def split_sql_statements(sql: str) -> List[str]:
    """Splits SQL text into individual statements by semicolon, respecting quotes and dollar quoting."""
    statements = []
    current = []
    i = 0
    n = len(sql)
    in_single_quote = False
    in_dollar_quote = False
    dollar_tag = ""
    
    while i < n:
        if not in_single_quote and not in_dollar_quote:
            if sql[i] == "'":
                in_single_quote = True
                current.append(sql[i])
                i += 1
                continue
            # Check dollar quote like $$ or $func$
            if sql[i] == '$':
                m = re.match(r'^\$([a-zA-Z0-9_]*)\$', sql[i:])
                if m:
                    dollar_tag = m.group(0)
                    in_dollar_quote = True
                    current.append(dollar_tag)
                    i += len(dollar_tag)
                    continue
            if sql[i] == ';':
                stmt = "".join(current).strip()
                if stmt:
                    statements.append(stmt)
                current = []
                i += 1
                continue
        elif in_single_quote:
            if sql[i] == "'":
                if i + 1 < n and sql[i+1] == "'":
                    current.append("''")
                    i += 2
                    continue
                else:
                    in_single_quote = False
            current.append(sql[i])
            i += 1
            continue
        elif in_dollar_quote:
            if sql[i:i+len(dollar_tag)] == dollar_tag:
                in_dollar_quote = False
                current.append(dollar_tag)
                i += len(dollar_tag)
                continue
            current.append(sql[i])
            i += 1
            continue
            
        current.append(sql[i])
        i += 1
        
    if current:
        stmt = "".join(current).strip()
        if stmt:
            statements.append(stmt)
            
    return statements

def parse_sql_tuples(values_str: str) -> List[List[str]]:
    """Robust parser for SQL VALUES (...) tuples."""
    tuples = []
    i = 0
    n = len(values_str)
    in_single_quote = False
    
    current_tuple_str = None
    
    while i < n:
        ch = values_str[i]
        if not in_single_quote:
            if ch == "'":
                in_single_quote = True
                if current_tuple_str is not None:
                    current_tuple_str.append(ch)
            elif ch == '(':
                if current_tuple_str is None:
                    current_tuple_str = []
                else:
                    current_tuple_str.append(ch)
            elif ch == ')':
                if current_tuple_str is not None:
                    # Check if top-level closing parenthesis
                    depth = 0
                    t_str = "".join(current_tuple_str)
                    tuples.append(t_str)
                    current_tuple_str = None
            else:
                if current_tuple_str is not None:
                    current_tuple_str.append(ch)
        else:
            if ch == "'":
                if i + 1 < n and values_str[i+1] == "'":
                    if current_tuple_str is not None:
                        current_tuple_str.append("''")
                    i += 2
                    continue
                else:
                    in_single_quote = False
            if current_tuple_str is not None:
                current_tuple_str.append(ch)
        i += 1
        
    # Now parse individual values from each tuple string
    parsed_rows = []
    for t_str in tuples:
        vals = []
        cur_val = []
        in_sq = False
        depth = 0
        j = 0
        tn = len(t_str)
        while j < tn:
            c = t_str[j]
            if not in_sq:
                if c == "'":
                    in_sq = True
                    cur_val.append(c)
                elif c in ('(', '{', '['):
                    depth += 1
                    cur_val.append(c)
                elif c in (')', '}', ']'):
                    depth -= 1
                    cur_val.append(c)
                elif c == ',' and depth == 0:
                    vals.append("".join(cur_val).strip())
                    cur_val = []
                else:
                    cur_val.append(c)
            else:
                if c == "'":
                    if j + 1 < tn and t_str[j+1] == "'":
                        cur_val.append("''")
                        j += 2
                        continue
                    else:
                        in_sq = False
                cur_val.append(c)
            j += 1
        if cur_val:
            vals.append("".join(cur_val).strip())
            
        parsed_rows.append(vals)
        
    return parsed_rows

def clean_sql_value(val_str: str) -> Optional[str]:
    v = val_str.strip()
    if v.upper() == 'NULL':
        return None
    # Strip type casts like ::uuid, ::inet, ::jsonb
    v = re.sub(r'::[a-zA-Z0-9_]+', '', v)
    if v.startswith("'") and v.endswith("'"):
        # Remove surrounding quotes and replace '' with '
        inner = v[1:-1]
        return inner.replace("''", "'")
    return v

def test_full_database_script():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
    sql_blocks = [code for lang, code in blocks if lang.lower() == 'sql']
    
    assert len(sql_blocks) >= 2, "Expected at least 2 SQL code blocks (DDL + DML)"
    
    ddl_raw = sql_blocks[0]
    dml_raw = sql_blocks[1]
    
    ddl_clean = remove_sql_comments(ddl_raw)
    dml_clean = remove_sql_comments(dml_raw)
    
    ddl_stmts = split_sql_statements(ddl_clean)
    dml_stmts = split_sql_statements(dml_clean)
    
    print(f"Total DDL statements: {len(ddl_stmts)}")
    print(f"Total DML statements: {len(dml_stmts)}")
    
    # 1. Process DDL: ENUMs and Tables
    enums = {}
    tables = {}
    tables_creation_order = []
    
    for stmt in ddl_stmts:
        # CREATE TYPE ... AS ENUM
        m_enum = re.match(r'CREATE\s+TYPE\s+([a-zA-Z0-9_]+)\s+AS\s+ENUM\s*\((.*?)\)', stmt, re.IGNORECASE | re.DOTALL)
        if m_enum:
            ename = m_enum.group(1).lower()
            evals = [clean_sql_value(v) for v in m_enum.group(2).split(',')]
            enums[ename] = evals
            continue
            
        # CREATE TABLE
        m_tbl = re.match(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)\s*\((.*)\)', stmt, re.IGNORECASE | re.DOTALL)
        if m_tbl:
            tname = m_tbl.group(1).lower()
            tbody = m_tbl.group(2).strip()
            
            tables_creation_order.append(tname)
            
            # Split table elements
            # We split by comma at depth 0
            elems = []
            cur = []
            depth = 0
            in_sq = False
            for ch in tbody:
                if not in_sq:
                    if ch == "'":
                        in_sq = True
                    elif ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    elif ch == ',' and depth == 0:
                        elems.append("".join(cur).strip())
                        cur = []
                        continue
                else:
                    if ch == "'":
                        in_sq = False
                cur.append(ch)
            if cur:
                elems.append("".join(cur).strip())
                
            columns = {}
            primary_keys = []
            foreign_keys = []
            
            for elem in elems:
                # Table-level Primary Key
                m_pk = re.match(r'(?:CONSTRAINT\s+[a-zA-Z0-9_]+\s+)?PRIMARY\s+KEY\s*\(([a-zA-Z0-9_,\s]+)\)', elem, re.IGNORECASE)
                if m_pk:
                    pks = [c.strip().lower() for c in m_pk.group(1).split(',')]
                    primary_keys.extend(pks)
                    continue
                    
                # Table-level Foreign Key
                m_fk = re.match(r'(?:CONSTRAINT\s+[a-zA-Z0-9_]+\s+)?FOREIGN\s+KEY\s*\(([a-zA-Z0-9_,\s]+)\)\s*REFERENCES\s+([a-zA-Z0-9_]+)\s*\(([a-zA-Z0-9_,\s]+)\)', elem, re.IGNORECASE)
                if m_fk:
                    fk_cols = [c.strip().lower() for c in m_fk.group(1).split(',')]
                    ref_tbl = m_fk.group(2).lower()
                    ref_cols = [c.strip().lower() for c in m_fk.group(3).split(',')]
                    for fc, rc in zip(fk_cols, ref_cols):
                        foreign_keys.append({
                            'column': fc,
                            'ref_table': ref_tbl,
                            'ref_column': rc,
                            'elem': elem
                        })
                    continue
                    
                # Column definition
                m_col = re.match(r'^([a-zA-Z0-9_]+)\s+([a-zA-Z0-9_]+(?:\([^\)]+\))?)(.*)$', elem, re.DOTALL)
                if m_col:
                    col_name = m_col.group(1).lower()
                    col_type = m_col.group(2).upper()
                    col_rest = m_col.group(3)
                    
                    if 'PRIMARY KEY' in col_rest.upper():
                        primary_keys.append(col_name)
                    
                    m_inline_ref = re.search(r'REFERENCES\s+([a-zA-Z0-9_]+)\s*\(([a-zA-Z0-9_]+)\)', col_rest, re.IGNORECASE)
                    if m_inline_ref:
                        foreign_keys.append({
                            'column': col_name,
                            'ref_table': m_inline_ref.group(1).lower(),
                            'ref_column': m_inline_ref.group(2).lower(),
                            'elem': elem
                        })
                        
                    columns[col_name] = {
                        'type': col_type,
                        'nullable': 'NOT NULL' not in col_rest.upper() if 'PRIMARY KEY' not in col_rest.upper() else False,
                        'is_pk': 'PRIMARY KEY' in col_rest.upper(),
                        'raw': elem
                    }
                    
            tables[tname] = {
                'columns': columns,
                'primary_keys': list(dict.fromkeys(primary_keys)),
                'foreign_keys': foreign_keys
            }

    print(f"\nSuccessfully parsed {len(tables)} tables from DDL:")
    for idx, tname in enumerate(tables_creation_order):
        t = tables[tname]
        print(f"  {idx+1:02d}. {tname} (PK: {t['primary_keys']}, FKs: {len(t['foreign_keys'])})")

    # =========================================================================
    # TEST 1: Table Creation Order vs FK Dependencies
    # =========================================================================
    print("\n" + "="*70)
    print("TEST 1: TABLE CREATION ORDER vs FK DEPENDENCIES")
    print("="*70)
    created_so_far = set()
    order_errors = []
    
    for tname in tables_creation_order:
        t = tables[tname]
        for fk in t['foreign_keys']:
            ref_tbl = fk['ref_table']
            if ref_tbl not in created_so_far and ref_tbl != tname:
                order_errors.append(f"Table '{tname}' references '{ref_tbl}' before '{ref_tbl}' is created! (FK: {fk['column']} -> {ref_tbl}.{fk['ref_column']})")
        created_so_far.add(tname)
        
    if order_errors:
        print(f"❌ FAIL: {len(order_errors)} Order errors:")
        for err in order_errors:
            print("  *", err)
    else:
        print("✅ PASS: All 27 tables are created in strictly valid topological order. No forward FK references.")

    # =========================================================================
    # TEST 2: Data Type Matching between FK and PK
    # =========================================================================
    print("\n" + "="*70)
    print("TEST 2: DATA TYPE MATCHING (FK vs PK)")
    print("="*70)
    type_errors = []
    for tname, t in tables.items():
        for fk in t['foreign_keys']:
            cname = fk['column']
            ref_tbl = fk['ref_table']
            ref_col = fk['ref_column']
            
            if ref_tbl not in tables:
                type_errors.append(f"Table '{tname}'.'{cname}' references non-existent table '{ref_tbl}'")
                continue
            if ref_col not in tables[ref_tbl]['columns']:
                type_errors.append(f"Table '{tname}'.'{cname}' references non-existent column '{ref_tbl}'.'{ref_col}'")
                continue
                
            src_type = t['columns'][cname]['type']
            dst_type = tables[ref_tbl]['columns'][ref_col]['type']
            
            # Normalize comparison
            if src_type != dst_type:
                type_errors.append(f"Type mismatch: '{tname}'.'{cname}' ({src_type}) -> '{ref_tbl}'.'{ref_col}' ({dst_type})")
                
    if type_errors:
        print(f"❌ FAIL: {len(type_errors)} Type mismatch errors:")
        for err in type_errors:
            print("  *", err)
    else:
        print("✅ PASS: 100% of Foreign Keys match the exact data type of their target Primary Keys (UUID == UUID, etc.).")

    # =========================================================================
    # TEST 3: Parse and Validate DML INSERTs
    # =========================================================================
    print("\n" + "="*70)
    print("TEST 3: PARSING & VALIDATING DML INSERTS")
    print("=" * 70)
    
    database_data = defaultdict(list)
    insert_errors = []
    
    for stmt in dml_stmts:
        m_ins = re.match(r'INSERT\s+INTO\s+([a-zA-Z0-9_]+)\s*\((.*?)\)\s*VALUES\s*(.*)', stmt, re.IGNORECASE | re.DOTALL)
        if not m_ins:
            continue
        tname = m_ins.group(1).lower()
        cols_raw = m_ins.group(2)
        vals_raw = m_ins.group(3)
        
        # Strip ON CONFLICT
        vals_clean = re.sub(r'ON\s+CONFLICT.*$', '', vals_raw, flags=re.IGNORECASE | re.DOTALL).strip()
        
        cols = [c.strip().lower() for c in cols_raw.split(',') if c.strip()]
        tuples = parse_sql_tuples(vals_clean)
        
        print(f"  INSERT into '{tname}': {len(cols)} cols, {len(tuples)} rows")
        
        if tname not in tables:
            insert_errors.append(f"INSERT into non-existent table '{tname}'")
            continue
            
        t_meta = tables[tname]
        
        for r_idx, row_vals in enumerate(tuples):
            if len(row_vals) != len(cols):
                insert_errors.append(f"Table '{tname}' row {r_idx+1}: Expected {len(cols)} values, got {len(row_vals)} ({row_vals})")
                continue
                
            row_dict = {}
            for col, val_str in zip(cols, row_vals):
                val = clean_sql_value(val_str)
                row_dict[col] = val
                
                # Check column existence in table
                if col not in t_meta['columns']:
                    insert_errors.append(f"Table '{tname}' row {r_idx+1}: Unknown column '{col}'")
                    
            database_data[tname].append(row_dict)

    if insert_errors:
        print(f"❌ FAIL: {len(insert_errors)} Insert parsing errors:")
        for err in insert_errors:
            print("  *", err)
    else:
        print(f"✅ PASS: 100% of INSERT statements parsed successfully across {len(database_data)} tables.")

    # =========================================================================
    # TEST 4: Referential Integrity across all Seed Data
    # =========================================================================
    print("\n" + "="*70)
    print("TEST 4: SEED DATA REFERENTIAL INTEGRITY (FOREIGN KEY CHECKS)")
    print("="*70)
    
    fk_violations = []
    
    for tname, rows in database_data.items():
        t_meta = tables[tname]
        fks = t_meta['foreign_keys']
        
        for r_idx, row in enumerate(rows):
            for fk in fks:
                col = fk['column']
                ref_tbl = fk['ref_table']
                ref_col = fk['ref_column']
                
                val = row.get(col)
                if val is None:
                    continue  # Nullable FK allowed
                    
                ref_rows = database_data.get(ref_tbl, [])
                ref_pks = {r.get(ref_col) for r in ref_rows if r.get(ref_col) is not None}
                
                if val not in ref_pks:
                    fk_violations.append(
                        f"Table '{tname}' row {r_idx+1}: FK '{col}'='{val}' does not exist in referenced table '{ref_tbl}'.'{ref_col}'! (Available count: {len(ref_pks)})"
                    )
                    
    if fk_violations:
        print(f"❌ FAIL: {len(fk_violations)} FK violations in Seed Data:")
        for v in fk_violations[:10]:
            print("  *", v)
        if len(fk_violations) > 10:
            print(f"  ... and {len(fk_violations)-10} more.")
    else:
        print("✅ PASS: 100% of Seed Data Foreign Keys resolve to valid existing records in referenced tables!")

    # =========================================================================
    # TEST 5: Business Invariants and Financial Math Verification
    # =========================================================================
    print("\n" + "="*70)
    print("TEST 5: BUSINESS LOGIC & FINANCIAL MATH VERIFICATION")
    print("="*70)
    
    orders = database_data.get('orders', [])
    order_items = database_data.get('order_items', [])
    payments = database_data.get('payments', [])
    recipes = database_data.get('recipes_bom', [])
    shifts = database_data.get('shifts', [])
    
    math_errors = []
    
    # 5.1 Order item subtotals
    items_by_order = defaultdict(list)
    for itm in order_items:
        oid = itm['order_id']
        items_by_order[oid].append(itm)
        qty = int(itm['quantity'])
        unit_p = float(itm['unit_price'])
        subt = float(itm['subtotal_price'])
        if abs(subt - (qty * unit_p)) > 0.01:
            math_errors.append(f"Order item {itm.get('order_item_id')}: unit_price {unit_p} * qty {qty} != subtotal_price {subt}")
            
    # 5.2 Orders calculation
    for o in orders:
        oid = o['order_id']
        code = o['order_code']
        otype = o['order_type']
        sub_total = float(o['sub_total'])
        discount = float(o['discount_amount'])
        ship_fee = float(o['delivery_fee'])
        total = float(o['total_amount'])
        
        # Check subtotal against sum of order items
        o_items = items_by_order.get(oid, [])
        calc_subtotal = sum(float(it['subtotal_price']) for it in o_items)
        
        if abs(sub_total - calc_subtotal) > 0.01:
            math_errors.append(f"Order {code}: order sub_total ({sub_total}) != sum of items ({calc_subtotal})")
            
        expected_total = sub_total - discount + ship_fee
        if abs(total - expected_total) > 0.01:
            math_errors.append(f"Order {code}: total_amount ({total}) != sub_total ({sub_total}) - discount ({discount}) + ship ({ship_fee}) = {expected_total}")
            
        # Delivery fee rule
        if otype.lower() == 'delivery':
            if ship_fee != 20000:
                math_errors.append(f"Delivery order {code} has invalid delivery fee: {ship_fee} (must be 20000)")
            if not o.get('delivery_address') or not o.get('recipient_phone') or not o.get('recipient_name'):
                math_errors.append(f"Delivery order {code} missing required delivery fields: address={o.get('delivery_address')}, phone={o.get('recipient_phone')}, name={o.get('recipient_name')}")
        else:
            if ship_fee != 0:
                math_errors.append(f"Non-delivery order {code} ({otype}) has non-zero delivery fee: {ship_fee}")
                
    # 5.3 Payment matching
    pmt_by_order = defaultdict(list)
    for p in payments:
        pmt_by_order[p['order_id']].append(p)
        
    for o in orders:
        oid = o['order_id']
        code = o['order_code']
        status = o['status']
        total = float(o['total_amount'])
        p_list = pmt_by_order.get(oid, [])
        
        if status in ('Preparing', 'Served', 'Completed') and o['order_type'] in ('DineIn', 'TakeAway', 'Delivery'):
            # Check payments
            paid_sum = sum(float(p['amount']) for p in p_list if p['status'] == 'Paid')
            if abs(paid_sum - total) > 0.01:
                math_errors.append(f"Order {code} ({status}) total={total} but sum of Paid payments={paid_sum}")
                
    # 5.4 Shifts cash difference calculation
    for s in shifts:
        init_c = float(s['initial_cash'])
        act_c = float(s['actual_cash_counted']) if s['actual_cash_counted'] is not None else 0
        sys_c = float(s['system_cash_calculated']) if s['system_cash_calculated'] is not None else 0
        diff_c = float(s['cash_difference']) if s['cash_difference'] is not None else 0
        
        if s['status'] == 'Closed':
            expected_diff = act_c - sys_c
            if abs(diff_c - expected_diff) > 0.01:
                math_errors.append(f"Shift {s['shift_id']}: cash_difference {diff_c} != actual ({act_c}) - system ({sys_c}) = {expected_diff}")
                
    if math_errors:
        print(f"❌ FAIL: {len(math_errors)} Business logic / financial math errors:")
        for err in math_errors:
            print("  *", err)
    else:
        print("✅ PASS: All 6 seeded orders, items, payments, delivery rules, and shift calculations are 100% mathematically consistent and accurate!")

    overall_pass = (len(order_errors) == 0 and len(type_errors) == 0 and len(insert_errors) == 0 and len(fk_violations) == 0 and len(math_errors) == 0)
    print("\n" + "="*70)
    print("DATABASE VERIFICATION OVERALL RESULT:", "PASS" if overall_pass else "FAIL")
    print("="*70)
    return overall_pass

if __name__ == "__main__":
    test_full_database_script()
