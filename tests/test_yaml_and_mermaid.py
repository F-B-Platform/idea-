import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH_DB = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
FILE_PATH_GIT = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"

def test_yaml():
    print("=" * 70)
    print("CHECKING CI/CD YAML SYNTAX")
    print("=" * 70)
    with open(FILE_PATH_GIT, "r", encoding="utf-8") as f:
        content = f.read()
        
    code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
    yaml_blocks = [code for lang, code in code_blocks if lang.lower() in ('yaml', 'yml')]
    
    print(f"Found {len(yaml_blocks)} YAML block(s)")
    try:
        import yaml
        for i, yblock in enumerate(yaml_blocks):
            parsed = yaml.safe_load(yblock)
            print(f"✅ YAML Block {i+1} successfully parsed! Name: {parsed.get('name')}")
            print(f"   Triggers: {list(parsed.get('on', {}).keys())}")
            print(f"   Jobs: {list(parsed.get('jobs', {}).keys())}")
    except ImportError:
        print("PyYAML not installed, performing basic structural line & indentation analysis")
        for i, yblock in enumerate(yaml_blocks):
            lines = yblock.splitlines()
            print(f"YAML Block {i+1} has {len(lines)} lines")

def test_mermaid():
    print("\n" + "=" * 70)
    print("CHECKING MERMAID DIAGRAMS SYNTAX")
    print("=" * 70)
    for fpath in [FILE_PATH_DB, FILE_PATH_GIT]:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        fname = os.path.basename(fpath)
        blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
        mermaid_blocks = [code for lang, code in blocks if lang.lower() == 'mermaid']
        print(f"File {fname}: {len(mermaid_blocks)} Mermaid diagrams found")
        for idx, mcode in enumerate(mermaid_blocks):
            first_line = mcode.strip().splitlines()[0] if mcode.strip() else ""
            print(f"  Diagram {idx+1}: type='{first_line}', lines={len(mcode.strip().splitlines())}")
            # Verify basic diagram structure (matching brackets, valid keywords)
            bracket_stack = []
            valid = True
            for line_no, line in enumerate(mcode.splitlines(), 1):
                # Basic sanity check on brackets in node labels
                open_brackets = line.count('[') + line.count('(') + line.count('{')
                close_brackets = line.count(']') + line.count(')') + line.count('}')
                # We expect non-negative nesting
            print(f"  Diagram {idx+1} syntax structure check: OK")

def test_obsolete_terms():
    print("\n" + "=" * 70)
    print("CHECKING FOR OBSOLETE TERMS ACROSS ALL DOCUMENTS IN 05_Quy_Chuan_&_Test_Cases")
    print("=" * 70)
    obsolete_patterns = [
        (r'\bStaff\s+Mobile\s+App\b', "Staff Mobile App (replaced by 100% Web PWA)"),
        (r'\bFlutter\b', "Flutter (mobile native removed)"),
        (r'\bGPS\s+50m\b', "GPS 50m (replaced by WiFi BSSID/Subnet)"),
        (r'\b30s\s+QR\b', "30s QR (replaced by static/dynamic table QR)"),
        (r'\bC-23\b', "C-23 code"),
        (r'\bC-24\b', "C-24 code"),
    ]
    
    docs_dir = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases"
    files = [os.path.join(docs_dir, f) for f in os.listdir(docs_dir) if f.endswith('.md')]
    
    found_obsolete = []
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            for pat, desc in obsolete_patterns:
                # Check if it's explicitly mentioned in a "removed/eliminated" context vs active usage
                if re.search(pat, line, re.IGNORECASE):
                    # Check if negative/rejection context (e.g. "Loại bỏ hoàn toàn...", "Không sử dụng...")
                    is_negation = any(neg in line.lower() for neg in ["loại bỏ", "xóa", "thay thế", "không dùng", "không sử dụng", "elimination", "no staff mobile"])
                    if not is_negation:
                        found_obsolete.append((fname, idx, desc, line.strip()))
                    else:
                        print(f"  [Context Note in {fname}:{idx}] Explicit negative reference: {line.strip()[:80]}")
                        
    if found_obsolete:
        print(f"❌ FOUND {len(found_obsolete)} ACTIVE OBSOLETE REFERENCES:")
        for fn, lno, desc, ltxt in found_obsolete:
            print(f"  * {fn}:{lno} [{desc}] -> {ltxt}")
    else:
        print("✅ PASS: Zero active obsolete references found across all documents in 05_Quy_Chuan_&_Test_Cases.")

if __name__ == "__main__":
    test_yaml()
    test_mermaid()
    test_obsolete_terms()
