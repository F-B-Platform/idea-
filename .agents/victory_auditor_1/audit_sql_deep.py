import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print("=== AUDIT Seed_Data_&_Database_Script.md ===")
print(f"Total characters: {len(content):,}")
print(f"Total lines: {len(content.splitlines()):,}")

# Extract SQL code blocks
sql_blocks = re.findall(r"```sql\s*(.*?)\s*```", content, re.DOTALL)
print(f"Total SQL code blocks found: {len(sql_blocks)}")

full_sql = "\n\n".join(sql_blocks)
print(f"Total concatenated SQL lines: {len(full_sql.splitlines()):,}")

# Save extracted SQL to a standalone file for testing
sql_out_path = r"d:\Idea_DoAn\.agents\victory_auditor_1\extracted_schema_and_seed.sql"
with open(sql_out_path, "w", encoding="utf-8") as f:
    f.write(full_sql)
print(f"Saved full SQL to {sql_out_path}")

# 1. Check Tables Created
tables_created = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_\.\"]+)", full_sql, re.IGNORECASE)
cleaned_tables = [t.replace('"', '').split('.')[-1] for t in tables_created]
print(f"\n--- 1. Tables Created ({len(cleaned_tables)} tables) ---")
for idx, tbl in enumerate(cleaned_tables, 1):
    print(f"  {idx:2d}. {tbl}")

# 2. Check Tables Inserted
tables_inserted = re.findall(r"INSERT\s+INTO\s+([a-zA-Z0-9_\.\"]+)", full_sql, re.IGNORECASE)
cleaned_inserted = sorted(list(dict.fromkeys([t.replace('"', '').split('.')[-1] for t in tables_inserted])))
print(f"\n--- 2. Tables Populated with Seed Data ({len(cleaned_inserted)} tables) ---")
for idx, tbl in enumerate(cleaned_inserted, 1):
    count = len(re.findall(r"INSERT\s+INTO\s+(?:public\.)?" + tbl + r"\b", full_sql, re.IGNORECASE))
    print(f"  {idx:2d}. {tbl} (Insert statements/batches: {count})")

# 3. Check Realistic Data Requirements
print("\n--- 3. Checking Specific Realistic Seed Data Requirements ---")

# 3.1 Branches
branches_check = re.findall(r"INSERT\s+INTO\s+(?:public\.)?branches.*?;", full_sql, re.DOTALL | re.IGNORECASE)
print(f"  Branches insert statements: {len(branches_check)}")
if branches_check:
    for b_kw in ["Quận 1", "Cầu Giấy", "Hải Châu", "BSSID", "192.168."]:
        found = b_kw.lower() in branches_check[0].lower()
        print(f"    [{'PASS' if found else 'FAIL'}] Branch data contains '{b_kw}'")

# 3.2 Users & Roles
users_check = re.findall(r"INSERT\s+INTO\s+(?:public\.)?users.*?;", full_sql, re.DOTALL | re.IGNORECASE)
print(f"  Users insert statements: {len(users_check)}")
if users_check:
    for u_kw in ["admin", "manager", "staff", "barista", "cashier"]:
        c = len(re.findall(r"\b" + u_kw, users_check[0], re.IGNORECASE))
        print(f"    User accounts with role/term '{u_kw}': {c} occurrences")

# 3.3 Menu Items & Recipes (BOM)
menu_check = re.findall(r"INSERT\s+INTO\s+(?:public\.)?menu_items.*?;", full_sql, re.DOTALL | re.IGNORECASE)
recipes_check = re.findall(r"INSERT\s+INTO\s+(?:public\.)?(?:recipes|recipe_items|product_recipes|item_recipes).*?;", full_sql, re.DOTALL | re.IGNORECASE)
print(f"  Menu items inserts: {len(menu_check)}, Recipe BOM inserts: {len(recipes_check)}")

# 3.4 Orders (Dine-In A/B, Delivery, Takeaway)
orders_check = re.findall(r"INSERT\s+INTO\s+(?:public\.)?orders.*?;", full_sql, re.DOTALL | re.IGNORECASE)
print(f"  Orders inserts: {len(orders_check)}")
if orders_check:
    for o_kw in ["DINE_IN", "DELIVERY", "TAKEAWAY", "20000", "VIETQR", "CASH"]:
        found = o_kw.lower() in orders_check[0].lower() or (len(orders_check) > 1 and any(o_kw.lower() in oc.lower() for oc in orders_check))
        print(f"    [{'PASS' if found else 'FAIL'}] Orders contain '{o_kw}'")
