import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def extract_and_validate_mermaid():
    print("=== EXTRACTING AND VALIDATING MERMAID DIAGRAMS ===")
    mermaid_count = 0
    errors = []
    
    for root, dirs, files in os.walk(DOCS_DIR):
        if ".agents" in root or ".git" in root:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DOCS_DIR)
            with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
            
            # Find all ```mermaid ... ```
            matches = re.findall(r"```mermaid(.*?)```", content, re.DOTALL)
            for i, block in enumerate(matches, 1):
                mermaid_count += 1
                lines = [l.strip() for l in block.strip().splitlines() if l.strip() and not l.strip().startswith("%%")]
                if not lines:
                    errors.append((rel, i, "Empty mermaid block"))
                    continue
                header = lines[0]
                valid_headers = [
                    "graph", "flowchart", "sequenceDiagram", "erDiagram", "classDiagram",
                    "stateDiagram", "stateDiagram-v2", "gantt", "pie", "gitGraph", "C4Context", "mindmap"
                ]
                if not any(header.startswith(vh) for vh in valid_headers):
                    errors.append((rel, i, f"Unknown diagram type header: '{header}'"))
                
                # Check for common syntax traps like unclosed quotes, broken brackets, etc.
                # In sequenceDiagram: participant syntax, ->> or -->>
                # In erDiagram: entity { type field }
                # In flowchart/graph: balanced brackets
                text = "\n".join(lines)
                open_b = text.count("[") - text.count("]")
                open_p = text.count("(") - text.count(")")
                open_c = text.count("{") - text.count("}")
                
                # Report if large imbalance
                if abs(open_b) > 2 or abs(open_p) > 2 or abs(open_c) > 2:
                    errors.append((rel, i, f"Bracket imbalance: [] diff={open_b}, () diff={open_p}, {{}} diff={open_c}"))

    print(f"Total Mermaid diagrams found: {mermaid_count}")
    if errors:
        print(f"❌ Found {len(errors)} potential Mermaid syntax issues:")
        for rel, num, err in errors:
            print(f"  - {rel} [Diagram #{num}]: {err}")
    else:
        print("✅ All Mermaid diagrams passed header and structural checks!")

if __name__ == "__main__":
    extract_and_validate_mermaid()
