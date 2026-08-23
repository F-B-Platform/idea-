import re
import sys

sql_path = r'd:\Idea_DoAn\.agents\challenger_2\extracted_schema.sql'
with open(sql_path, 'r', encoding='utf-8') as f:
    sql_text = f.read()

print(f"=== SQL STATS ===")
print(f"Total lines: {len(sql_text.splitlines())}")

# 1. Extract CREATE TYPE enums
enums = {}
enum_matches = re.finditer(r'CREATE\s+TYPE\s+([a-zA-Z0-9_]+)\s+AS\s+ENUM\s*\((.*?)\);', sql_text, re.DOTALL | re.IGNORECASE)
for m in enum_matches:
    ename = m.group(1).lower()
    raw_vals = m.group(2)
    vals = [v.strip().strip("'\"") for v in raw_vals.split(',') if v.strip()]
    enums[ename] = vals

print(f"\n--- ENUMS DEFINED ({len(enums)}) ---")
for k, v in enums.items():
    print(f"  {k}: {v}")

# 2. Extract CREATE TABLE
tables = {}
# simple parser for CREATE TABLE
table_matches = re.finditer(r'CREATE\s+TABLE(?:\s+IF\s+NOT\s+EXISTS)?\s+([a-zA-Z0-9_]+)\s*\((.*?)\n\);', sql_text, re.DOTALL | re.IGNORECASE)
for m in table_matches:
    tname = m.group(1).lower()
    body = m.group(2)
    tables[tname] = body

print(f"\n--- TABLES DEFINED ({len(tables)}) ---")
for tname in tables:
    print(f"  - {tname}")

# Check critical columns and tables
print(f"\n--- CRITICAL CHECKS ---")
# Check orders table
if 'orders' in tables:
    body = tables['orders']
    print("orders table found.")
    has_order_type = bool(re.search(r'order_type', body, re.IGNORECASE))
    has_delivery_address = bool(re.search(r'delivery_address', body, re.IGNORECASE))
    has_delivery_fee = bool(re.search(r'delivery_fee', body, re.IGNORECASE))
    print(f"  - order_type: {has_order_type}")
    print(f"  - delivery_address: {has_delivery_address}")
    print(f"  - delivery_fee: {has_delivery_fee}")
else:
    print("CRITICAL ERROR: 'orders' table NOT found!")

# Check attendance table
has_att = False
for t in tables:
    if 'attend' in t:
        has_att = True
        body = tables[t]
        print(f"Attendance table found: {t}")
        has_wifi = bool(re.search(r'wifi|bssid|ssid|ip', body, re.IGNORECASE))
        has_gps = bool(re.search(r'gps|lat|long|geofence', body, re.IGNORECASE))
        print(f"  - wifi/bssid/ssid/ip fields: {has_wifi}")
        print(f"  - gps/lat/long fields (should be False): {has_gps}")

# Check wifi config table or branch columns
has_wifi_config = False
for t in tables:
    if 'wifi' in t or 'branch' in t:
        body = tables[t]
        if re.search(r'bssid|ssid|allowed_ip', body, re.IGNORECASE):
            has_wifi_config = True
            print(f"WiFi config found in table '{t}'")

print(f"  - WiFi config present: {has_wifi_config}")

# Check Seed Data INSERTS
print(f"\n--- SEED DATA INSERTS ---")
insert_matches = re.finditer(r'INSERT\s+INTO\s+([a-zA-Z0-9_]+)\s*(?:\((.*?)\))?\s*VALUES\s*(.*?);', sql_text, re.DOTALL | re.IGNORECASE)
inserts_by_table = {}
for m in insert_matches:
    tname = m.group(1).lower()
    cols = m.group(2)
    vals = m.group(3)
    if tname not in inserts_by_table:
        inserts_by_table[tname] = []
    inserts_by_table[tname].append({'cols': cols, 'vals': vals})

for tname, ins in inserts_by_table.items():
    print(f"  Table {tname}: {len(ins)} insert statement(s)")

# Check order types in orders inserts
if 'orders' in inserts_by_table:
    orders_text = "\n".join([i['vals'] for i in inserts_by_table['orders']])
    has_dinein_seed = 'DINE_IN' in orders_text.upper() or 'DINEIN' in orders_text.upper()
    has_takeaway_seed = 'TAKE_AWAY' in orders_text.upper() or 'TAKEAWAY' in orders_text.upper()
    has_delivery_seed = 'DELIVERY' in orders_text.upper()
    print(f"\nOrders Seed Coverage:")
    print(f"  - DineIn seed: {has_dinein_seed}")
    print(f"  - TakeAway seed: {has_takeaway_seed}")
    print(f"  - Delivery seed: {has_delivery_seed}")
