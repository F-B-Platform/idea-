import os
import re
import sys
import json

# Ensure UTF-8
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Idea_DoAn"
UAT_PATH = os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "UAT_Test_Cases.md")
SEED_PATH = os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "Seed_Data_&_Database_Script.md")
GIT_PATH = os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "Git_Workflow_&_Branching_Strategy.md")

def deep_audit_uat():
    with open(UAT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all test case sections
    # Typical pattern: ### **TC-XXX-YY: Title** or ### TC-XXX-YY
    tc_blocks = re.findall(r"(###\s+\*?\*?(TC-[A-Za-z0-9_\-]+)(?:\*?\*?)?:?\s*(.*?))\n(?=(?:###\s+\*?\*?TC-|\Z))", content, re.DOTALL)
    
    # Also find table test cases if any
    table_tcs = re.findall(r"\|\s*(TC-[A-Za-z0-9_\-]+)\s*\|", content)
    
    all_unique_tcs = sorted(list(set([m[1] for m in tc_blocks] + table_tcs)))
    
    # Analyze each block for required fields
    required_fields = ["Mục đích", "Tiền điều kiện", "Các bước", "Dữ liệu", "Kỳ vọng", "Trạng thái"]
    tc_details = []
    
    for header, tc_id, body in tc_blocks:
        missing_fields = []
        for field in required_fields:
            if field.lower() not in body.lower() and field.lower() not in header.lower():
                missing_fields.append(field)
        
        tc_details.append({
            "tc_id": tc_id,
            "title": header.split("\n")[0],
            "body_length": len(body),
            "missing_fields": missing_fields,
            "has_placeholders": bool(re.search(r"\bTODO\b|\bFIXME\b|/\* rest of|// rest of", body))
        })
        
    return {
        "total_tc_blocks": len(tc_blocks),
        "total_unique_tcs": len(all_unique_tcs),
        "all_tc_ids": all_unique_tcs,
        "tc_details": tc_details
    }

def deep_audit_seed():
    with open(SEED_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract SQL code blocks
    sql_blocks = re.findall(r"```sql\n(.*?)```", content, re.DOTALL)
    full_sql = "\n\n".join(sql_blocks)
    
    # Extract CREATE TABLE statements
    # Match CREATE TABLE [IF NOT EXISTS] tablename ( ... );
    create_table_regex = re.compile(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_\.\"]+)\s*\((.*?)\);", re.DOTALL | re.IGNORECASE)
    created_tables = []
    for match in create_table_regex.finditer(full_sql):
        tname = match.group(1).replace('"', '').split('.')[-1]
        tbody = match.group(2)
        cols = [c.strip() for c in tbody.split(",") if c.strip() and not c.strip().startswith("CONSTRAINT") and not c.strip().startswith("PRIMARY KEY") and not c.strip().startswith("FOREIGN KEY")]
        created_tables.append({
            "table_name": tname,
            "column_count": len(cols),
            "raw_length": len(tbody),
            "has_pk": "PRIMARY KEY" in tbody.upper() or "UUID" in tbody.upper(),
            "has_fk": "REFERENCES" in tbody.upper() or "FOREIGN KEY" in tbody.upper()
        })
        
    # Extract INSERT INTO statements
    insert_regex = re.compile(r"INSERT\s+INTO\s+([a-zA-Z0-9_\.\"]+)\s*\((.*?)\)\s*VALUES\s*(.*?);", re.DOTALL | re.IGNORECASE)
    inserted_tables = []
    for match in insert_regex.finditer(full_sql):
        tname = match.group(1).replace('"', '').split('.')[-1]
        cols = match.group(2).strip()
        vals_block = match.group(3).strip()
        # Count rows inserted (approximate by counting tuples `(` at start of lines or after comma)
        tuples = re.findall(r"\([^\)]+\)", vals_block)
        inserted_tables.append({
            "table_name": tname,
            "columns": cols,
            "row_count": len(tuples),
            "raw_length": len(vals_block)
        })
        
    return {
        "sql_blocks_count": len(sql_blocks),
        "total_sql_length": len(full_sql),
        "created_tables": created_tables,
        "inserted_tables": inserted_tables
    }

def deep_audit_git():
    with open(GIT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract code blocks by language
    code_blocks = re.findall(r"```([a-zA-Z0-9_\-#+]*)\n(.*?)```", content, re.DOTALL)
    
    csharp_blocks = [code for lang, code in code_blocks if lang.lower() in ["csharp", "c#", "cs"]]
    ts_blocks = [code for lang, code in code_blocks if lang.lower() in ["typescript", "ts", "tsx"]]
    yaml_blocks = [code for lang, code in code_blocks if lang.lower() in ["yaml", "yml"]]
    
    # Check C# block quality
    cs_analysis = []
    for idx, cs in enumerate(csharp_blocks, 1):
        has_todo = bool(re.search(r"\bTODO\b|\bFIXME\b|/\* rest of|// rest of|throw new NotImplementedException", cs))
        has_empty_catch = bool(re.search(r"catch\s*\([^\)]*\)\s*\{\s*\}", cs))
        lines = cs.strip().splitlines()
        cs_analysis.append({
            "block_idx": idx,
            "lines_count": len(lines),
            "has_todo": has_todo,
            "has_empty_catch": has_empty_catch,
            "first_line": lines[0] if lines else "",
            "last_line": lines[-1] if lines else ""
        })
        
    # Check TS block quality
    ts_analysis = []
    for idx, ts in enumerate(ts_blocks, 1):
        has_todo = bool(re.search(r"\bTODO\b|\bFIXME\b|/\* rest of|// rest of", ts))
        has_empty_catch = bool(re.search(r"catch\s*\([^\)]*\)\s*\{\s*\}", ts))
        lines = ts.strip().splitlines()
        ts_analysis.append({
            "block_idx": idx,
            "lines_count": len(lines),
            "has_todo": has_todo,
            "has_empty_catch": has_empty_catch,
            "first_line": lines[0] if lines else "",
            "last_line": lines[-1] if lines else ""
        })

    return {
        "total_code_blocks": len(code_blocks),
        "csharp_blocks_count": len(csharp_blocks),
        "csharp_analysis": cs_analysis,
        "ts_blocks_count": len(ts_blocks),
        "ts_analysis": ts_analysis,
        "yaml_blocks_count": len(yaml_blocks)
    }

def main():
    uat_res = deep_audit_uat()
    seed_res = deep_audit_seed()
    git_res = deep_audit_git()
    
    deep_report = {
        "uat": uat_res,
        "seed": seed_res,
        "git": git_res
    }
    
    with open(r"d:\Idea_DoAn\.agents\auditor_zero_placeholder\deep_audit_results.json", "w", encoding="utf-8") as f:
        json.dump(deep_report, f, indent=2, ensure_ascii=False)
        
    print(f"UAT: {uat_res['total_tc_blocks']} TC blocks found, {uat_res['total_unique_tcs']} unique TC IDs.")
    print(f"Seed: {len(seed_res['created_tables'])} tables created, {len(seed_res['inserted_tables'])} insert statements.")
    print(f"Git: {git_res['csharp_blocks_count']} C# blocks, {git_res['ts_blocks_count']} TS blocks, {git_res['yaml_blocks_count']} YAML blocks.")
    print("Zero-placeholder verification completed.")

if __name__ == "__main__":
    main()
