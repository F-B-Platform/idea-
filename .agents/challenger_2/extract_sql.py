import os
import re

sql_file = r'd:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md'

with open(sql_file, 'r', encoding='utf-8', errors='ignore') as fp:
    content = fp.read()

sql_blocks = re.findall(r'```sql\s*\n(.*?)\n```', content, re.DOTALL)
print(f"Found {len(sql_blocks)} SQL blocks in {sql_file}")

all_sql = "\n\n".join(sql_blocks)
out_sql = r'd:\Idea_DoAn\.agents\challenger_2\extracted_schema.sql'
with open(out_sql, 'w', encoding='utf-8') as fp:
    fp.write(all_sql)

print(f"Extracted SQL size: {len(all_sql)} chars ({len(all_sql.splitlines())} lines)")
