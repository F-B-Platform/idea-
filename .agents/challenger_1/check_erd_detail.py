import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"

with open(os.path.join(DIAG_DIR, "03_ERD_Database_Diagram.md"), "r", encoding="utf-8") as f:
    erd_text = f.read()

# Check table INGREDIENTS and INVENTORY_STOCKS
m_ing = re.search(r'INGREDIENTS\s*\{([^}]+)\}', erd_text)
if m_ing:
    print("=== ERD INGREDIENTS ===")
    print(m_ing.group(1).strip())

m_stk = re.search(r'INVENTORY_STOCKS\s*\{([^}]+)\}', erd_text)
if m_stk:
    print("\n=== ERD INVENTORY_STOCKS ===")
    print(m_stk.group(1).strip())

m_rec = re.search(r'PRODUCT_RECIPES\s*\{([^}]+)\}', erd_text)
if m_rec:
    print("\n=== ERD PRODUCT_RECIPES ===")
    print(m_rec.group(1).strip())

m_logs = re.search(r'INVENTORY_LOGS\s*\{([^}]+)\}', erd_text)
if m_logs:
    print("\n=== ERD INVENTORY_LOGS ===")
    print(m_logs.group(1).strip())