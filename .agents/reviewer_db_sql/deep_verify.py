import re
import sys
import ipaddress

def strip_sql_comments(sql):
    # Remove single line comments
    lines = []
    for line in sql.splitlines():
        # Keep quotes intact
        in_str = False
        str_char = None
        cleaned = []
        i = 0
        while i < len(line):
            ch = line[i]
            if ch in ("'", '"'):
                if not in_str:
                    in_str = True
                    str_char = ch
                elif str_char == ch:
                    in_str = False
                    str_char = None
                cleaned.append(ch)
            elif not in_str and ch == '-' and i + 1 < len(line) and line[i+1] == '-':
                break
            else:
                cleaned.append(ch)
            i += 1
        lines.append("".join(cleaned))
    return "\n".join(lines)

def parse_full_database_script():
    filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract SQL blocks
    sql_blocks = re.findall(r"```sql\s*\n(.*?)\n```", content, re.DOTALL)
    full_sql = "\n".join(sql_blocks)
    clean_sql = strip_sql_comments(full_sql)

    # 1. Parse Tables DDL
    create_tables = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)\s*\((.*?)\);", clean_sql, re.DOTALL | re.IGNORECASE)
    tables_ddl = {}
    for tbl_name, col_defs in create_tables:
        tables_ddl[tbl_name.lower()] = col_defs.strip()

    print(f"=== [DDL Verification] Found {len(tables_ddl)} tables ===")
    for idx, (t, defs) in enumerate(tables_ddl.items(), 1):
        pk_match = re.search(r"(\w+)\s+UUID\s+PRIMARY\s+KEY", defs, re.IGNORECASE)
        composite_pk = re.search(r"PRIMARY\s+KEY\s*\((.*?)\)", defs, re.IGNORECASE)
        pk_info = pk_match.group(1) if pk_match else (f"Composite: {composite_pk.group(1)}" if composite_pk else "NO PK!")
        print(f"  {idx:02d}. {t} (PK: {pk_info})")

    # 2. Parse DML Inserts
    insert_pattern = re.compile(r"INSERT\s+INTO\s+(\w+)\s*\((.*?)\)\s*VALUES\s*(.*?)(?:ON\s+CONFLICT|;\s*(?:INSERT|CREATE|SELECT|DO|\Z))", re.DOTALL | re.IGNORECASE)
    
    parsed_tables = {}
    
    for match in insert_pattern.finditer(clean_sql):
        table_name = match.group(1).lower()
        cols = [c.strip() for c in match.group(2).split(",")]
        val_block = match.group(3).strip()
        
        # Parse value tuples
        rows = []
        depth = 0
        curr = ""
        in_str = False
        str_char = None
        for ch in val_block:
            if ch in ("'", '"') and (len(curr) == 0 or curr[-1] != '\\'):
                if not in_str:
                    in_str = True
                    str_char = ch
                elif str_char == ch:
                    in_str = False
                    str_char = None
            if not in_str:
                if ch == '(':
                    depth += 1
                    if depth == 1:
                        curr = ""
                        continue
                elif ch == ')':
                    depth -= 1
                    if depth == 0:
                        rows.append(curr.strip())
                        curr = ""
                        continue
            if depth >= 1:
                curr += ch
        
        parsed_rows = []
        for r in rows:
            vals = []
            val_curr = ""
            val_in_str = False
            val_str_char = None
            for ch in r:
                if ch in ("'", '"') and (len(val_curr) == 0 or val_curr[-1] != '\\'):
                    if not val_in_str:
                        val_in_str = True
                        val_str_char = ch
                    elif val_str_char == ch:
                        val_in_str = False
                        val_str_char = None
                if not val_in_str and ch == ',':
                    vals.append(val_curr.strip())
                    val_curr = ""
                else:
                    val_curr += ch
            if val_curr:
                vals.append(val_curr.strip())
            
            clean_vals = []
            for v in vals:
                v = v.strip()
                if v.startswith("'") and v.endswith("'"):
                    clean_vals.append(v[1:-1])
                elif v.startswith("'") and "::jsonb" in v:
                    clean_vals.append(v.split("::jsonb")[0].strip()[1:-1])
                elif v.upper() == "NULL":
                    clean_vals.append(None)
                elif v.upper() == "TRUE":
                    clean_vals.append(True)
                elif v.upper() == "FALSE":
                    clean_vals.append(False)
                else:
                    try:
                        if "." in v:
                            clean_vals.append(float(v))
                        else:
                            clean_vals.append(int(v))
                    except:
                        clean_vals.append(v)
            parsed_rows.append(dict(zip(cols, clean_vals)))

        if table_name not in parsed_tables:
            parsed_tables[table_name] = []
        parsed_tables[table_name].extend(parsed_rows)

    print(f"\n=== [DML Seed Data Row Counts] ===")
    for t_name, t_rows in parsed_tables.items():
        print(f"  Table `{t_name}`: {len(t_rows)} rows")

    # 3. Validation & Adversarial Checks
    print(f"\n=== [Integrity & Referential Validation] ===")
    errors = []
    warnings = []

    # Map PKs for all tables
    pk_map = {}
    for t_name, rows in parsed_tables.items():
        pk_map[t_name] = set()
        for r in rows:
            # find PK column (usually <tbl_singular>_id or id)
            for k, v in r.items():
                if k.endswith("_id") and (k == f"{t_name[:-1]}_id" or k == f"{t_name}_id" or k in ("branch_id", "user_id", "role_id", "category_id", "product_id", "size_id", "modifier_id", "ingredient_id", "table_id", "order_id", "order_item_id", "payment_id", "customer_id", "trans_id", "voucher_id", "review_id", "combo_id", "shift_id", "attendance_id", "check_id", "detail_id", "audit_id", "wifi_config_id", "branch_price_id", "item_mod_id", "combo_item_id")):
                    if v:
                        pk_map[t_name].add(str(v).lower())

    # Check Foreign Keys
    # orders -> branches, tables, customers
    for ord_row in parsed_tables.get("orders", []):
        o_id = ord_row.get("order_id")
        b_id = str(ord_row.get("branch_id")).lower() if ord_row.get("branch_id") else None
        t_id = str(ord_row.get("table_id")).lower() if ord_row.get("table_id") else None
        c_id = str(ord_row.get("customer_id")).lower() if ord_row.get("customer_id") else None
        
        if b_id and b_id not in pk_map.get("branches", set()):
            errors.append(f"Order {o_id} references non-existent branch {b_id}")
        if t_id and t_id not in pk_map.get("tables", set()):
            errors.append(f"Order {o_id} references non-existent table {t_id}")
        if c_id and c_id not in pk_map.get("customers", set()):
            errors.append(f"Order {o_id} references non-existent customer {c_id}")

    # order_items -> orders, products, product_sizes
    for item in parsed_tables.get("order_items", []):
        it_id = item.get("order_item_id")
        o_id = str(item.get("order_id")).lower() if item.get("order_id") else None
        p_id = str(item.get("product_id")).lower() if item.get("product_id") else None
        s_id = str(item.get("size_id")).lower() if item.get("size_id") else None
        
        if o_id and o_id not in pk_map.get("orders", set()):
            errors.append(f"OrderItem {it_id} references non-existent order {o_id}")
        if p_id and p_id not in pk_map.get("products", set()):
            errors.append(f"OrderItem {it_id} references non-existent product {p_id}")
        if s_id and s_id not in pk_map.get("product_sizes", set()):
            errors.append(f"OrderItem {it_id} references non-existent product_size {s_id}")

    # order_item_modifiers -> order_items, modifiers
    for im in parsed_tables.get("order_item_modifiers", []):
        im_id = im.get("item_mod_id")
        oi_id = str(im.get("order_item_id")).lower() if im.get("order_item_id") else None
        m_id = str(im.get("modifier_id")).lower() if im.get("modifier_id") else None
        if oi_id and oi_id not in pk_map.get("order_items", set()):
            errors.append(f"OrderItemModifier {im_id} references non-existent order_item {oi_id}")
        if m_id and m_id not in pk_map.get("modifiers", set()):
            errors.append(f"OrderItemModifier {im_id} references non-existent modifier {m_id}")

    # recipes_bom -> products, product_sizes, ingredients
    for rb in parsed_tables.get("recipes_bom", []):
        r_id = rb.get("recipe_id")
        p_id = str(rb.get("product_id")).lower() if rb.get("product_id") else None
        s_id = str(rb.get("size_id")).lower() if rb.get("size_id") else None
        i_id = str(rb.get("ingredient_id")).lower() if rb.get("ingredient_id") else None
        if p_id and p_id not in pk_map.get("products", set()):
            errors.append(f"Recipe {r_id} references non-existent product {p_id}")
        if s_id and s_id not in pk_map.get("product_sizes", set()):
            errors.append(f"Recipe {r_id} references non-existent product_size {s_id}")
        if i_id and i_id not in pk_map.get("ingredients", set()):
            errors.append(f"Recipe {r_id} references non-existent ingredient {i_id}")

    # 4. Check Order Math
    print(f"\n=== [Order Math Verification] ===")
    order_items_by_order = {}
    for oi in parsed_tables.get("order_items", []):
        oid = str(oi.get("order_id")).lower()
        if oid not in order_items_by_order:
            order_items_by_order[oid] = []
        order_items_by_order[oid].append(oi)

    for o in parsed_tables.get("orders", []):
        oid = str(o.get("order_id")).lower()
        code = o.get("order_code")
        sub_total = o.get("sub_total", 0)
        discount = o.get("discount_amount", 0)
        del_fee = o.get("delivery_fee", 0)
        total = o.get("total_amount", 0)
        
        expected_total = sub_total - discount + del_fee
        if total != expected_total:
            errors.append(f"Order {code}: total_amount ({total}) != sub_total ({sub_total}) - discount ({discount}) + fee ({del_fee}) [expected: {expected_total}]")
        
        # Check sub_total from items
        items = order_items_by_order.get(oid, [])
        calc_subtotal = sum(it.get("subtotal_price", 0) for it in items)
        if sub_total != calc_subtotal:
            errors.append(f"Order {code}: sub_total ({sub_total}) != sum of item subtotal_prices ({calc_subtotal})")
        
        print(f"  Order `{code}`: sub_total={sub_total}, discount={discount}, delivery_fee={del_fee}, total={total} [OK: {total == expected_total}]")

    # 5. Check Shift Math
    print(f"\n=== [Shift & Z-Report Math Verification] ===")
    for sh in parsed_tables.get("shifts", []):
        sh_id = sh.get("shift_id")
        init_c = sh.get("initial_cash", 0)
        act_c = sh.get("actual_cash_counted")
        sys_c = sh.get("system_cash_calculated", 0)
        diff = sh.get("cash_difference", 0)
        status = sh.get("status")
        notes = sh.get("shift_notes", "")
        
        if act_c is not None:
            expected_diff = act_c - sys_c
            if diff != expected_diff:
                errors.append(f"Shift {sh_id}: cash_difference ({diff}) != actual ({act_c}) - sys ({sys_c}) [expected: {expected_diff}]")
            print(f"  Shift `{sh_id}` ({status}): initial={init_c}, sys={sys_c}, actual={act_c}, diff={diff} [OK: {diff == expected_diff}]")
        else:
            print(f"  Shift `{sh_id}` ({status}): Open shift, cash not yet counted.")

    # 6. Check Reviews Trigger Alert
    print(f"\n=== [Review Alert Trigger Verification] ===")
    for rev in parsed_tables.get("customer_reviews", []):
        rev_id = rev.get("review_id")
        stars = rev.get("rating_stars")
        alert = rev.get("is_urgent_alert")
        expected_alert = (stars <= 2)
        if alert != expected_alert:
            errors.append(f"Review {rev_id}: rating_stars={stars}, is_urgent_alert={alert} [expected: {expected_alert}]")
        print(f"  Review `{rev_id}`: stars={stars}, alert={alert} [OK: {alert == expected_alert}]")

    # 7. Check WiFi Attendance CIDR / BSSID
    print(f"\n=== [WiFi Attendance Verification] ===")
    wifi_by_branch = {}
    for w in parsed_tables.get("branch_wifi_configs", []):
        b_id = str(w.get("branch_id")).lower()
        wifi_by_branch[b_id] = {
            "bssid_list": [b.strip().upper() for b in w.get("bssid_list", "").split(",")],
            "subnets": [ipaddress.ip_network(s.strip()) for s in w.get("allowed_ip_subnets", "").split(",")]
        }

    for att in parsed_tables.get("attendances", []):
        att_id = att.get("attendance_id")
        b_id = str(att.get("branch_id")).lower()
        bssid = str(att.get("verified_bssid", "")).strip().upper()
        ip_str = str(att.get("verified_ip", "")).strip()
        status = att.get("status")
        
        cfg = wifi_by_branch.get(b_id)
        if not cfg:
            errors.append(f"Attendance {att_id}: branch {b_id} has no WiFi config")
            continue
        
        bssid_ok = bssid in cfg["bssid_list"]
        ip_obj = ipaddress.ip_address(ip_str)
        ip_ok = any(ip_obj in subnet for subnet in cfg["subnets"])
        
        if not bssid_ok:
            errors.append(f"Attendance {att_id}: BSSID {bssid} not in branch allowed list {cfg['bssid_list']}")
        if not ip_ok:
            errors.append(f"Attendance {att_id}: IP {ip_str} not in branch subnets {cfg['subnets']}")
        
        print(f"  Attendance `{att_id}` ({status}): BSSID={bssid} (OK:{bssid_ok}), IP={ip_str} (OK:{ip_ok})")

    # 8. Check Inventory Checks
    print(f"\n=== [Inventory Checks Verification] ===")
    for icd in parsed_tables.get("inventory_check_details", []):
        d_id = icd.get("detail_id")
        sys_q = icd.get("system_quantity", 0)
        act_q = icd.get("actual_quantity", 0)
        diff_q = icd.get("difference_quantity", 0)
        expected_diff_q = round(act_q - sys_q, 3)
        if round(diff_q, 3) != expected_diff_q:
            errors.append(f"InventoryDetail {d_id}: diff_q ({diff_q}) != actual ({act_q}) - sys ({sys_q}) [expected: {expected_diff_q}]")
        print(f"  InventoryDetail `{d_id}`: sys={sys_q}, act={act_q}, diff={diff_q} [OK: {round(diff_q, 3) == expected_diff_q}]")

    print(f"\n=======================================================")
    print(f"TOTAL ERRORS FOUND: {len(errors)}")
    for e in errors:
        print(f"  [ERROR] {e}")
    print(f"TOTAL WARNINGS FOUND: {len(warnings)}")
    for w in warnings:
        print(f"  [WARNING] {w}")
    print(f"=======================================================")

if __name__ == "__main__":
    parse_full_database_script()
