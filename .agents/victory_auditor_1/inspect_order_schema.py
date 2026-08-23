import sys
from parse_sql_proper import table_defs, inserted_rows

sys.stdout.reconfigure(encoding='utf-8')

print("Orders Columns in Table Def:", table_defs['orders']['cols'])
print("\nFirst Order record in Seed Data:")
for k, v in inserted_rows['orders'][0].items():
    print(f"  {k}: {v}")

print("\nOrder Items Columns in Table Def:", table_defs['order_items']['cols'])
print("\nFirst Order Item record in Seed Data:")
for k, v in inserted_rows['order_items'][0].items():
    print(f"  {k}: {v}")

print("\nShifts Columns in Table Def:", table_defs['shifts']['cols'])
print("\nAll Shifts records in Seed Data:")
for s in inserted_rows['shifts']:
    print(s)
