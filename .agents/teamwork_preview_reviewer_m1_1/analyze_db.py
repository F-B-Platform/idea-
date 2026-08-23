import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

f2_path = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"

with open(f2_path, "r", encoding="utf-8") as f:
    f2 = f.read()

# 1. Check all CREATE TABLE blocks
tables = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)\s*\((.*?)\);", f2, re.DOTALL | re.IGNORECASE)
print(f"Found {len(tables)} CREATE TABLE statements via regex")

for tname, tbody in tables:
    cols = [line.strip() for line in tbody.strip().splitlines() if line.strip() and not line.strip().startswith("--")]
    print(f"Table: {tname:<28} Columns/Constraints: {len(cols)}")

# 2. Check for Triggers
triggers = re.findall(r"CREATE\s+TRIGGER\s+([a-zA-Z0-9_]+)", f2, re.IGNORECASE)
print(f"\nTriggers found ({len(triggers)}): {triggers}")

# 3. Check for Indexes
indexes = re.findall(r"CREATE\s+(?:UNIQUE\s+)?INDEX\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)", f2, re.IGNORECASE)
print(f"\nIndexes found ({len(indexes)}):")
for idx in indexes:
    print(f"  - {idx}")

# 4. Check for EF Core Configurations
ef_configs = re.findall(r"public\s+class\s+([a-zA-Z0-9_]+)\s*:\s*IEntityTypeConfiguration<([a-zA-Z0-9_]+)>", f2)
print(f"\nEF Core Configurations found ({len(ef_configs)}):")
for cname, etype in ef_configs:
    print(f"  - {cname} -> Entity: {etype}")

# 5. Check Mermaid Diagram
mermaid_blocks = re.findall(r"```mermaid(.*?)```", f2, re.DOTALL)
print(f"\nMermaid blocks in 02_: {len(mermaid_blocks)}")

