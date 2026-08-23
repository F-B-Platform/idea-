import re
import sys
import uuid

def test_seed_data_file():
    filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Total file size: {len(content)} characters, {len(content.splitlines())} lines.")

    # 1. Check for forbidden placeholders
    placeholders = [
        "TODO", "FIXME", "/* rest of", "// rest of", "... rest", "TBD", "PLACEHOLDER", "etc."
    ]
    found_placeholders = []
    for line_no, line in enumerate(content.splitlines(), start=1):
        for p in placeholders:
            if p.lower() in line.lower() and not ("zero placeholder" in line.lower() or "no todo" in line.lower()):
                # ignore markdown text discussing the rule itself
                if not ("zero" in line.lower() or "quy ước" in line.lower() or "tiêu chuẩn" in line.lower() or "banned" in line.lower() or "báo cáo" in line.lower() or "checklist" in line.lower()):
                    found_placeholders.append((line_no, p, line.strip()))
    
    print(f"Placeholders found: {len(found_placeholders)}")
    for p in found_placeholders[:10]:
        print(f"  Line {p[0]}: [{p[1]}] -> {p[2]}")

    # Check for ellipses `...` inside code blocks
    code_blocks = re.findall(r"```(?:sql|csharp|bash|mermaid)?\s*\n(.*?)\n```", content, re.DOTALL)
    print(f"Total code blocks found: {len(code_blocks)}")
    
    ellipsis_in_code = []
    for idx, cb in enumerate(code_blocks):
        for l_idx, line in enumerate(cb.splitlines()):
            if "..." in line:
                ellipsis_in_code.append((idx, l_idx+1, line.strip()))
    
    print(f"Ellipses in code blocks: {len(ellipsis_in_code)}")
    for ec in ellipsis_in_code:
        print(f"  CodeBlock {ec[0]}, line {ec[1]}: {ec[2]}")

    # 2. Extract and count CREATE TABLE statements
    create_tables = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)\s*\((.*?)\);", content, re.DOTALL | re.IGNORECASE)
    print(f"\nTotal CREATE TABLE statements: {len(create_tables)}")
    table_names = [t[0] for t in create_tables]
    for idx, name in enumerate(table_names, 1):
        print(f"  {idx:02d}. {name}")

    # 3. Extract and analyze INSERT statements
    insert_matches = re.findall(r"INSERT\s+INTO\s+(\w+)\s*\((.*?)\)\s*VALUES\s*(.*?)(?:ON\s+CONFLICT|;)", content, re.DOTALL | re.IGNORECASE)
    print(f"\nTotal INSERT INTO statements matched: {len(insert_matches)}")
    inserted_tables = {}
    for table, cols, val_block in insert_matches:
        cols_list = [c.strip() for c in cols.split(",")]
        # Count rows in val_block
        # Each row is typically (...)
        rows = re.findall(r"\((.*?)\)(?:\s*,|\s*$)", val_block.strip(), re.DOTALL)
        inserted_tables[table] = {
            "cols": cols_list,
            "row_count": len(rows),
            "rows_raw": rows
        }
        print(f"  Table `{table}`: {len(rows)} rows inserted with {len(cols_list)} columns.")

    # 4. Check ENUM types created
    enum_matches = re.findall(r"CREATE\s+TYPE\s+(\w+)\s+AS\s+ENUM\s*\((.*?)\);", content, re.DOTALL | re.IGNORECASE)
    print(f"\nTotal ENUM types: {len(enum_matches)}")
    for e_name, e_vals in enum_matches:
        vals = [v.strip().strip("'") for v in e_vals.split(",")]
        print(f"  ENUM `{e_name}`: {vals}")

    # 5. Check Triggers created
    trigger_matches = re.findall(r"CREATE\s+TRIGGER\s+(\w+)\s+(.*?);", content, re.DOTALL | re.IGNORECASE)
    print(f"\nTotal Triggers: {len(trigger_matches)}")
    for trg_name, trg_body in trigger_matches:
        print(f"  Trigger `{trg_name}`")

    # 6. Check Indexes created
    index_matches = re.findall(r"CREATE\s+(?:UNIQUE\s+)?INDEX\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)\s+ON\s+(\w+)(.*?);", content, re.DOTALL | re.IGNORECASE)
    print(f"\nTotal Indexes: {len(index_matches)}")
    for idx_name, tbl_name, idx_spec in index_matches:
        print(f"  Index `{idx_name}` ON `{tbl_name}`: {idx_spec.strip()}")

if __name__ == "__main__":
    test_seed_data_file()
