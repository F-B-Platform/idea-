import re
import sys

def parse_sql_seed_data():
    filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the SQL seed data block in Chapter 3
    ch3_match = re.search(r"# CHƯƠNG 3:.*?(```sql.*?)```", content, re.DOTALL)
    if not ch3_match:
        print("Could not find Chapter 3 SQL block")
        return
    
    sql_text = ch3_match.group(1)
    print(f"Chapter 3 SQL block length: {len(sql_text)}")

    # Split by INSERT INTO
    inserts = re.split(r"INSERT\s+INTO\s+", sql_text, flags=re.IGNORECASE)[1:]
    print(f"Total INSERT blocks: {len(inserts)}")

    parsed_data = {}

    for ins in inserts:
        tbl_match = re.match(r"(\w+)\s*\((.*?)\)\s*VALUES\s*(.*)", ins, re.DOTALL | re.IGNORECASE)
        if not tbl_match:
            print("Failed to match insert:", ins[:100])
            continue
        
        table_name = tbl_match.group(1).lower()
        cols = [c.strip() for c in tbl_match.group(2).split(",")]
        val_block = tbl_match.group(3)
        
        # Strip ON CONFLICT or ;
        val_block_clean = re.split(r"ON\s+CONFLICT|;", val_block, flags=re.IGNORECASE)[0].strip()
        
        # Split rows by finding top-level parentheses
        rows = []
        curr = ""
        depth = 0
        in_str = False
        str_char = None
        for ch in val_block_clean:
            if ch in ("'", '"') and (len(curr) == 0 or curr[-1] != '\\'):
                if not in_str:
                    in_str = True
                    str_char = ch
                elif str_char == ch:
                    in_str = False
                    str_char = None
            if not in_str:
                if ch == '(':
                    depth += 1
                    if depth == 1:
                        curr = ""
                        continue
                elif ch == ')':
                    depth -= 1
                    if depth == 0:
                        rows.append(curr.strip())
                        curr = ""
                        continue
            if depth >= 1:
                curr += ch
        
        parsed_rows = []
        for r in rows:
            # parse values inside row
            vals = []
            val_curr = ""
            val_in_str = False
            val_str_char = None
            for ch in r:
                if ch in ("'", '"') and (len(val_curr) == 0 or val_curr[-1] != '\\'):
                    if not val_in_str:
                        val_in_str = True
                        val_str_char = ch
                    elif val_str_char == ch:
                        val_in_str = False
                        val_str_char = None
                if not val_in_str and ch == ',':
                    vals.append(val_curr.strip())
                    val_curr = ""
                else:
                    val_curr += ch
            if val_curr:
                vals.append(val_curr.strip())
            
            # clean values
            clean_vals = []
            for v in vals:
                v = v.strip()
                if v.startswith("'") and v.endswith("'"):
                    clean_vals.append(v[1:-1])
                elif v.startswith("'") and "::jsonb" in v:
                    clean_vals.append(v.split("::jsonb")[0].strip()[1:-1])
                elif v.upper() == "NULL":
                    clean_vals.append(None)
                elif v.upper() == "TRUE":
                    clean_vals.append(True)
                elif v.upper() == "FALSE":
                    clean_vals.append(False)
                else:
                    try:
                        if "." in v:
                            clean_vals.append(float(v))
                        else:
                            clean_vals.append(int(v))
                    except:
                        clean_vals.append(v)
            parsed_rows.append(dict(zip(cols, clean_vals)))

        parsed_data[table_name] = parsed_rows
        print(f"Table `{table_name}`: successfully parsed {len(parsed_rows)} rows. (Cols: {len(cols)})")

    return parsed_data

if __name__ == "__main__":
    data = parse_sql_seed_data()
