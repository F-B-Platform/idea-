import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SEED_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
with open(SEED_PATH, "r", encoding="utf-8") as f:
    content = f.read()

order_items_match = re.search(r"INSERT\s+INTO\s+order_items\s*\((.*?)\)\s*VALUES\s*(.*?)(?:ON CONFLICT|;)", content, re.DOTALL | re.IGNORECASE)
if order_items_match:
    print("=== FULL INSERT INTO order_items ===")
    print(order_items_match.group(0))
