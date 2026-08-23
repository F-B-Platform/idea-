import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

f2_path = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"
with open(f2_path, "r", encoding="utf-8") as f:
    f2 = f.read()

# Extract table DDLs
table_blocks = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)\s*\((.*?)\);", f2, re.DOTALL | re.IGNORECASE)

tables_dict = {}
for name, body in table_blocks:
    tables_dict[name.lower()] = body

print(f"Total DDL tables: {len(tables_dict)}")

# Extract FK references
fk_pattern = r"REFERENCES\s+([a-zA-Z0-9_]+)\s*\(([a-zA-Z0-9_]+)\)"
all_fks = []
for tname, body in tables_dict.items():
    fks = re.findall(fk_pattern, body, re.IGNORECASE)
    for ref_table, ref_col in fks:
        all_fks.append((tname, ref_table.lower(), ref_col.lower()))

print(f"Total FK references: {len(all_fks)}")
fk_errors = []
for src_t, ref_t, ref_c in all_fks:
    if ref_t not in tables_dict:
        fk_errors.append(f"Table '{src_t}' references non-existent table '{ref_t}'")
    else:
        # Check if ref_c is in ref_t body
        if not re.search(rf"\b{ref_c}\b", tables_dict[ref_t], re.IGNORECASE):
            fk_errors.append(f"Table '{src_t}' references non-existent column '{ref_c}' in table '{ref_t}'")

if fk_errors:
    print(f"❌ FK Errors found: {fk_errors}")
else:
    print("✅ All Foreign Key references are valid and link to existing tables/columns!")

# Check money types and decimals
money_cols = re.findall(r"([a-zA-Z0-9_]+)\s+DECIMAL\((\d+),\s*(\d+)\)", f2, re.IGNORECASE)
print(f"\nDecimal columns defined ({len(money_cols)}):")
for col, p, s in money_cols[:15]:
    print(f"  - {col}: DECIMAL({p},{s})")

