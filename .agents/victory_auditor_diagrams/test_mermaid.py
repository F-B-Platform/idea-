import os
import re
import sys

files = [
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md'
]

def check_mermaid_block(diag_type, lines, file_name, block_idx):
    issues = []
    subgraphs = 0
    alts = 0
    opts = 0
    loops = 0
    pars = 0
    criticals = 0
    breaks = 0
    rects = 0
    
    for line_no, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        if not line or line.startswith('%%'):
            continue
            
        if line.startswith('subgraph'):
            subgraphs += 1
        elif line == 'end':
            if subgraphs > 0:
                subgraphs -= 1
            elif alts > 0:
                alts -= 1
            elif opts > 0:
                opts -= 1
            elif loops > 0:
                loops -= 1
            elif pars > 0:
                pars -= 1
            elif criticals > 0:
                criticals -= 1
            elif breaks > 0:
                breaks -= 1
            elif rects > 0:
                rects -= 1
            else:
                issues.append(f"Line {line_no}: 'end' without matching block opening")
        elif line.startswith('alt ') or line == 'alt':
            alts += 1
        elif line.startswith('opt ') or line == 'opt':
            opts += 1
        elif line.startswith('loop ') or line == 'loop':
            loops += 1
        elif line.startswith('par ') or line == 'par':
            pars += 1
        elif line.startswith('critical ') or line == 'critical':
            criticals += 1
        elif line.startswith('break ') or line == 'break':
            breaks += 1
        elif line.startswith('rect '):
            rects += 1

    if subgraphs != 0:
        issues.append(f"Unclosed subgraph: {subgraphs} remaining")
    if alts != 0:
        issues.append(f"Unclosed alt: {alts} remaining")
    if opts != 0:
        issues.append(f"Unclosed opt: {opts} remaining")
    if loops != 0:
        issues.append(f"Unclosed loop: {loops} remaining")
    if pars != 0:
        issues.append(f"Unclosed par: {pars} remaining")

    return issues

print("=== MERMAID BLOCK STRUCTURE & NESTING VALIDATION ===")
all_pass = True
for f in files:
    content = open(f, encoding='utf-8').read()
    mermaid_blocks = re.findall(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL)
    print(f"\n--- {os.path.basename(f)} ({len(mermaid_blocks)} blocks) ---")
    for i, mb in enumerate(mermaid_blocks):
        lines = mb.strip().splitlines()
        diag_type = lines[0].strip() if lines else 'UNKNOWN'
        issues = check_mermaid_block(diag_type, lines, f, i+1)
        if issues:
            all_pass = False
            print(f"  [FAIL] Block {i+1} ({diag_type}): {issues}")
        else:
            print(f"  [PASS] Block {i+1} ({diag_type}, {len(lines)} lines)")

if all_pass:
    print("\nALL MERMAID BLOCKS PASSED STRUCTURE VALIDATION!")
else:
    print("\nSOME MERMAID BLOCKS FAILED STRUCTURE VALIDATION!")
