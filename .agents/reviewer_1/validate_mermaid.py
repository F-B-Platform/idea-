import os
import re

files = [
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md'
]

def check_sequence(code, filename, block_idx):
    lines = code.strip().split('\n')
    stack = []
    activations = {}
    errors = []
    
    for line_no, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        if not line or line.startswith('%%'):
            continue
            
        first_word = line.split()[0] if line.split() else ''
        if first_word in ['alt', 'opt', 'par', 'loop', 'rect', 'critical', 'break']:
            stack.append((first_word, line_no))
        elif first_word == 'else':
            if not stack or stack[-1][0] not in ['alt', 'critical']:
                errors.append(f'Line {line_no}: "else" without matching alt/critical')
        elif first_word == 'and':
            if not stack or stack[-1][0] != 'par':
                errors.append(f'Line {line_no}: "and" without matching par')
        elif first_word == 'end':
            if not stack:
                errors.append(f'Line {line_no}: "end" without matching block start')
            else:
                stack.pop()
                
        if line.startswith('activate '):
            part = line.split()[1]
            activations[part] = activations.get(part, 0) + 1
        elif line.startswith('deactivate '):
            part = line.split()[1]
            activations[part] = activations.get(part, 0) - 1
            if activations[part] < 0:
                errors.append(f'Line {line_no}: deactivate {part} without corresponding activate')

    if stack:
        for s, lno in stack:
            errors.append(f'Unclosed block "{s}" started at line {lno}')
    for part, count in activations.items():
        if count > 0:
            errors.append(f'Participant "{part}" activated {count} more times than deactivated')
            
    return errors

def check_flowchart(code, filename, block_idx):
    lines = code.strip().split('\n')
    stack = []
    errors = []
    for line_no, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        if not line or line.startswith('%%'):
            continue
        if line.startswith('subgraph '):
            stack.append(('subgraph', line_no))
        elif line == 'end':
            if not stack:
                errors.append(f'Line {line_no}: "end" without matching subgraph')
            else:
                stack.pop()
    if stack:
        for s, lno in stack:
            errors.append(f'Unclosed subgraph started at line {lno}')
    return errors

def check_er(code, filename, block_idx):
    lines = code.strip().split('\n')
    errors = []
    in_entity = False
    entity_start = 0
    entity_name = ''
    for line_no, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        if not line or line.startswith('%%'):
            continue
        if '{' in line and not in_entity:
            in_entity = True
            entity_start = line_no
            entity_name = line.split('{')[0].strip()
        elif line == '}' and in_entity:
            in_entity = False
        elif '}' in line and not in_entity:
            errors.append(f'Line {line_no}: closing brace without opening entity')
    if in_entity:
        errors.append(f'Unclosed entity {entity_name} started at line {entity_start}')
    return errors

all_errors = []
for filepath in files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = re.findall(r'```mermaid(.*?)```', content, re.DOTALL)
    for i, b in enumerate(blocks):
        first_line = b.strip().split('\n')[0].strip()
        diagram_type = first_line.split()[0]
        if diagram_type in ['flowchart', 'graph']:
            errs = check_flowchart(b, fname, i+1)
        elif diagram_type == 'sequenceDiagram':
            errs = check_sequence(b, fname, i+1)
        elif diagram_type == 'erDiagram':
            errs = check_er(b, fname, i+1)
        else:
            errs = [f'Unknown diagram type: {diagram_type}']
        
        if errs:
            for e in errs:
                all_errors.append(f'[{fname} Block {i+1} ({diagram_type})]: {e}')
        else:
            print(f'OK: [{fname} Block {i+1} ({diagram_type})]')

if all_errors:
    print('\nFound structural issues:')
    for e in all_errors:
        print('  - ' + e)
else:
    print('\nAll 22 mermaid blocks passed structural syntax analysis!')
