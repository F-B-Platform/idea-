import sys
from parse_sql_proper import table_defs, inserted_rows

sys.stdout.reconfigure(encoding='utf-8')

print("Loyalty Cup Transactions columns:", table_defs['loyalty_cup_transactions']['cols'])
for tx in inserted_rows['loyalty_cup_transactions']:
    print(tx)
