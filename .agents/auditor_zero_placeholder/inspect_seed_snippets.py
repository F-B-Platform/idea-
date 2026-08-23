import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SEED_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
with open(SEED_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect the INSERT into order_items
order_items_match = re.search(r"INSERT\s+INTO\s+order_items\s*\((.*?)\)\s*VALUES\s*(.*?);", content, re.DOTALL | re.IGNORECASE)
if order_items_match:
    print("=== INSERT INTO order_items ===")
    print("Columns:", order_items_match.group(1))
    print("Values snippet:", order_items_match.group(2)[:500])

# Let's inspect how users are seeded
users_match = re.search(r"INSERT\s+INTO\s+users\s*\((.*?)\)\s*VALUES\s*(.*?);", content, re.DOTALL | re.IGNORECASE)
if users_match:
    print("\n=== INSERT INTO users ===")
    print("Columns:", users_match.group(1))
    print("Values snippet:", users_match.group(2))

# Let's inspect orders
orders_match = re.search(r"INSERT\s+INTO\s+orders\s*\((.*?)\)\s*VALUES\s*(.*?);", content, re.DOTALL | re.IGNORECASE)
if orders_match:
    print("\n=== INSERT INTO orders ===")
    print("Columns:", orders_match.group(1))
    print("Values snippet:", orders_match.group(2))

# Let's inspect shifts
shifts_match = re.search(r"INSERT\s+INTO\s+shifts\s*\((.*?)\)\s*VALUES\s*(.*?);", content, re.DOTALL | re.IGNORECASE)
if shifts_match:
    print("\n=== INSERT INTO shifts ===")
    print("Columns:", shifts_match.group(1))
    print("Values snippet:", shifts_match.group(2))

# Let's inspect product_sizes
psizes_match = re.search(r"INSERT\s+INTO\s+product_sizes\s*\((.*?)\)\s*VALUES\s*(.*?);", content, re.DOTALL | re.IGNORECASE)
if psizes_match:
    print("\n=== INSERT INTO product_sizes ===")
    print("Columns:", psizes_match.group(1))
    print("Values snippet:", psizes_match.group(2)[:500])
