import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\Idea_DoAn'
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.agents' in dirpath or '.git' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.md'):
            docs.append(os.path.join(dirpath, f))

total_mermaid = 0
mermaid_blocks = []

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    matches = re.finditer(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL)
    for m in matches:
        total_mermaid += 1
        block = m.group(1).strip()
        lines = block.split('\n')
        first_line = lines[0].strip() if lines else 'empty'
        mermaid_blocks.append((rel_path, first_line, len(lines), block))

print(f'Total Mermaid blocks found: {total_mermaid}')
for rel, fst, lc, blk in mermaid_blocks:
    print(f'  [{rel}] -> Type: {fst[:40]} ({lc} lines)')

# Syntax check patterns
errors = []
for rel, fst, lc, blk in mermaid_blocks:
    if lc < 2:
        errors.append((rel, 'Too short / empty block'))
    # Check braces matching
    if blk.count('{') != blk.count('}'):
        # In flowchart or erDiagram, check why
        errors.append((rel, f'Mismatched curly braces: {blk.count("{")} open vs {blk.count("}")} close'))
    if blk.count('[') != blk.count(']'):
        errors.append((rel, f'Mismatched square brackets: {blk.count("[")} open vs {blk.count("]")} close'))
    if blk.count('(') != blk.count(')'):
        errors.append((rel, f'Mismatched parentheses: {blk.count("(")} open vs {blk.count(")")} close'))

print(f'\nSyntax Error Count: {len(errors)}')
for e in errors:
    print(f'  ERROR in {e[0]}: {e[1]}')
