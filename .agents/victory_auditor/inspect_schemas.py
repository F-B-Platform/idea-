import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
with open(os.path.join(DOCS_DIR, "02_Thiet_Ke_Database.md"), "r", encoding="utf-8") as f:
    doc2 = f.read()

m = re.search(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?orders\s*\((.*?)\);', doc2, re.DOTALL | re.I)
if m:
    print("ORDERS TABLE:")
    print(m.group(0))
    
m2 = re.search(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?branch_wifi_configs\s*\((.*?)\);', doc2, re.DOTALL | re.I)
if m2:
    print("\nBRANCH_WIFI_CONFIGS TABLE:")
    print(m2.group(0))

m3 = re.search(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?attendances\s*\((.*?)\);', doc2, re.DOTALL | re.I)
if m3:
    print("\nATTENDANCES TABLE:")
    print(m3.group(0))

m4 = re.search(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?loyalty_cup_transactions\s*\((.*?)\);', doc2, re.DOTALL | re.I)
if m4:
    print("\nLOYALTY_CUP_TRANSACTIONS TABLE:")
    print(m4.group(0))
