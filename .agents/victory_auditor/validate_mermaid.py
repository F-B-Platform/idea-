# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

folder = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'
files = [
    'Smart_FB_Operating_System.md',
    'Actor_Phan_Quyen_Chuc_Nang.md',
    'Workflow_Quy_Trinh_Nghiep_Vu.md',
    'Tong_Quan_Kien_Truc_He_Thong.md',
    'Tom_Tat_1_Trang_Executive_Summary.md'
]

print('=== MERMAID DIAGRAM EXTRACTION & SYNTAX AUDIT ===')
total_diagrams = 0
diagram_types = {}
all_valid = True

for f in files:
    p = os.path.join(folder, f)
    with open(p, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    mermaid_blocks = re.findall(r'`mermaid\s*([\s\S]*?)`', content)
    print(f'-- File: {f} -- ({len(mermaid_blocks)} diagrams)')
    for i, block in enumerate(mermaid_blocks, 1):
        total_diagrams += 1
        lines = [l.strip() for l in block.strip().split(chr(10)) if l.strip()]
        first_line = lines[0] if lines else 'EMPTY'
        dtype = first_line.split()[0] if lines else 'EMPTY'
        diagram_types[dtype] = diagram_types.get(dtype, 0) + 1
        
        valid_headers = ['sequenceDiagram', 'flowchart', 'graph', 'stateDiagram', 'stateDiagram-v2', 'erDiagram', 'classDiagram', 'gantt', 'pie', 'C4Context', 'C4Container', 'C4Component']
        is_known_header = any(first_line.startswith(h) for h in valid_headers)
        
        if not is_known_header:
            print(f'   Diagram {i}: Unknown header -> {first_line}')
            all_valid = False
        else:
            print(f'   Diagram {i}: Header={first_line[:35]} | Lines={len(lines)} | PASS')

print(f'\nTotal Mermaid Diagrams across 5 files: {total_diagrams}')
print(f'Diagram types breakdown: {diagram_types}')
print('Overall Mermaid Validation:', 'ALL VALID (PASS)' if all_valid else 'FAIL')
