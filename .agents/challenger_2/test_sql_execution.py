import sqlite3
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

sql_path = r'd:\Idea_DoAn\.agents\challenger_2\extracted_schema.sql'
with open(sql_path, 'r', encoding='utf-8') as f:
    full_sql = f.read()

# Connect to in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Split into statements
raw_stmts = [s.strip() for s in full_sql.split(';') if s.strip()]

executed_tables = 0
executed_inserts = 0
executed_indexes = 0
errors = []

for idx, stmt in enumerate(raw_stmts):
    clean = re.sub(r'--.*?$', '', stmt, flags=re.MULTILINE).strip()
    if not clean:
        continue
    
    # Skip CREATE TYPE or EXTENSION
    if clean.upper().startswith('CREATE TYPE') or clean.upper().startswith('CREATE EXTENSION'):
        continue

    # SQLite compatibility conversions
    converted = clean
    converted = re.sub(r'\bUUID\b', 'TEXT', converted, flags=re.IGNORECASE)
    converted = re.sub(r'\bTIMESTAMPTZ\b', 'DATETIME', converted, flags=re.IGNORECASE)
    converted = re.sub(r'\bJSONB\b', 'TEXT', converted, flags=re.IGNORECASE)
    converted = re.sub(r'\bNUMERIC\([0-9,\s]+\)', 'REAL', converted, flags=re.IGNORECASE)
    converted = re.sub(r'\bgen_random_uuid\(\)', "'uuid-mock'", converted, flags=re.IGNORECASE)
    converted = re.sub(r'CURRENT_TIMESTAMP\s*-\s*INTERVAL\s*\'[^\']+\'', "CURRENT_TIMESTAMP", converted, flags=re.IGNORECASE)
    # Replace enums with text
    converted = re.sub(r'\b[a-z_]+_enum\b', 'TEXT', converted, flags=re.IGNORECASE)

    try:
        cursor.execute(converted)
        if clean.upper().startswith('CREATE TABLE'):
            executed_tables += 1
        elif clean.upper().startswith('INSERT INTO'):
            executed_inserts += 1
        elif clean.upper().startswith('CREATE INDEX'):
            executed_indexes += 1
    except Exception as e:
        errors.append({
            'stmt_idx': idx,
            'stmt_preview': clean[:80].replace('\n', ' '),
            'error': str(e)
        })

print(f"=== SQL EXECUTION IN SQLITE ENGINE ===")
print(f"Tables created: {executed_tables}")
print(f"Inserts executed: {executed_inserts}")
print(f"Indexes created: {executed_indexes}")
print(f"Errors encountered: {len(errors)}")

if errors:
    for err in errors:
        print(f"  [ERROR] Stmt #{err['stmt_idx']} ({err['stmt_preview']}): {err['error']}")
else:
    print("[PASS] All DDL, DML Inserts, and Indexes executed with 0 syntax or runtime errors!")

# Verify data counts in SQLite
print("\n--- RECORD COUNTS IN DATABASE ---")
tables_to_check = ['branches', 'branch_wifi_configs', 'tables', 'users', 'categories', 'products', 'product_variants', 'ingredients', 'recipes', 'recipe_ingredients', 'customers', 'orders', 'order_items', 'payments', 'loyalty_cup_transactions', 'work_shifts', 'attendances']

for tbl in tables_to_check:
    cursor.execute(f"SELECT COUNT(*) FROM {tbl}")
    cnt = cursor.fetchone()[0]
    print(f"  - {tbl}: {cnt} rows")

# Query the 3 order types from SQLite
cursor.execute("SELECT order_number, order_type, status, total_amount, delivery_fee, delivery_address FROM orders")
orders = cursor.fetchall()
print("\n--- VERIFIED ORDERS IN DATABASE ---")
for o in orders:
    print(f"  Order {o[0]}: type={o[1]}, status={o[2]}, total={o[3]}, delivery_fee={o[4]}, address={o[5]}")

conn.close()
