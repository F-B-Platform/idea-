import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE 02_Thiet_Ke_Database.md ===")
# Find all CREATE TABLE statements
create_tables = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)\s*\(([\s\S]*?)\);", content, re.IGNORECASE)
print(f"Total CREATE TABLE blocks: {len(create_tables)}")
for idx, (tname, body) in enumerate(create_tables, 1):
    cols = [line.strip() for line in body.strip().split("\n") if line.strip() and not line.strip().startswith("--") and not line.strip().startswith("CONSTRAINT") and not line.strip().startswith("PRIMARY") and not line.strip().startswith("FOREIGN")]
    print(f"{idx:2d}. Table: {tname:28} | Defined columns/constraints: {len(cols)}")

# Check key business columns in specific tables
print("\n--- Business Column Verifications ---")
orders_block = [body for name, body in create_tables if name.lower() == "orders"]
if orders_block:
    print("orders table columns:")
    for l in orders_block[0].split("\n"):
        if any(k in l.lower() for k in ["delivery_fee", "delivery_address", "order_type", "payment_status", "status"]):
            print("  ", l.strip())

wifi_block = [body for name, body in create_tables if "wifi" in name.lower()]
if wifi_block:
    print("branch_wifi_configs table columns:")
    for l in wifi_block[0].split("\n"):
        print("  ", l.strip())

loyalty_block = [body for name, body in create_tables if "loyalty" in name.lower()]
if loyalty_block:
    print("loyalty_cup_transactions table columns:")
    for l in loyalty_block[0].split("\n"):
        print("  ", l.strip())
