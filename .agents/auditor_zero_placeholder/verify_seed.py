import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Idea_DoAn"
SEED_PATH = os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "Seed_Data_&_Database_Script.md")

with open(SEED_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Extract SQL code blocks
sql_blocks = re.findall(r"```sql\n(.*?)```", content, re.DOTALL)
print(f"Total SQL code blocks: {len(sql_blocks)}")

full_sql = "\n\n".join(sql_blocks)

# Check all CREATE TABLE statements
create_tables = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_\.\"]+)\s*\((.*?)\);", full_sql, re.DOTALL | re.IGNORECASE)

print(f"\nTotal CREATE TABLE statements: {len(create_tables)}")
for idx, (tname, body) in enumerate(create_tables, 1):
    clean_name = tname.replace('"', '').split('.')[-1]
    # Count columns (lines with types)
    lines = [l.strip() for l in body.splitlines() if l.strip()]
    print(f"{idx:02d}. {clean_name:<30} ({len(lines)} def lines)")

# Check all INSERT INTO statements
insert_statements = re.findall(r"INSERT\s+INTO\s+([a-zA-Z0-9_\.\"]+)\s*\((.*?)\)\s*VALUES\s*(.*?);", full_sql, re.DOTALL | re.IGNORECASE)

print(f"\nTotal INSERT INTO statements: {len(insert_statements)}")
for idx, (tname, cols, vals) in enumerate(insert_statements, 1):
    clean_name = tname.replace('"', '').split('.')[-1]
    rows = re.findall(r"\([^\)]+\)", vals)
    print(f"{idx:02d}. {clean_name:<30} -> {len(rows)} rows inserted")

# Check for any unclosed parentheses or syntax red flags in SQL blocks
open_parens = full_sql.count("(")
close_parens = full_sql.count(")")
print(f"\nSQL Parentheses Check: '(' = {open_parens}, ')' = {close_parens} (Diff = {open_parens - close_parens})")

# Check for specific seed data required by user
checks = {
    "3 Branches (Q1, Cau Giay, Hai Chau)": ("Chi nhánh Quận 1" in full_sql and "Chi nhánh Cầu Giấy" in full_sql and "Chi nhánh Hải Châu" in full_sql),
    "WiFi BSSID / Subnet IP": ("00:1A:2B:3C:4D:5E" in full_sql or "bssid" in full_sql.lower()),
    "Menu items with sizes S/M/L": ("item_sizes" in full_sql and "'M'" in full_sql and "'L'" in full_sql),
    "BOM recipes in grams/ml": ("recipes" in full_sql and "gam" in content.lower() or "gram" in content.lower() or "ml" in content.lower()),
    "Accounts (Admin, Branch Managers, Staff, CRM Customers)": ("admin@smartcoffee.vn" in full_sql and "manager_q1@smartcoffee.vn" in full_sql and "barista_q1@smartcoffee.vn" in full_sql),
    "Orders for 3 channels (DineIn A/B, Delivery 20k ship fee, Takeaway)": ("DINE_IN" in full_sql and "DELIVERY" in full_sql and "TAKEAWAY" in full_sql and "20000" in full_sql),
    "Timekeepings with WiFi": ("timekeepings" in full_sql),
    "Z-Reports & Shifts": ("z_reports" in full_sql and "shifts" in full_sql),
    "Inventory Checks": ("inventory_checks" in full_sql)
}

print("\nSpecific Seed Data Verification:")
for k, v in checks.items():
    print(f"  {k}: {'PASS' if v else 'FAIL'}")
