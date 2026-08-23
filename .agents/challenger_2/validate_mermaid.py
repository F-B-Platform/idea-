import os
import re

root = r'd:\Idea_DoAn'
mermaid_blocks = []

for dirpath, dirnames, filenames in os.walk(root):
    if '.git' in dirpath or '.agents' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.md'):
            filepath = os.path.join(dirpath, f)
            rel_path = os.path.relpath(filepath, root)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            matches = re.finditer(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL)
            for idx, match in enumerate(matches):
                code = match.group(1).strip()
                lines = [l for l in code.split('\n') if l.strip() and not l.strip().startswith('%%')]
                first_line = lines[0].strip() if lines else ''
                mermaid_blocks.append({
                    'file': rel_path,
                    'index': idx + 1,
                    'first_line': first_line,
                    'lines_count': len(code.split('\n')),
                    'code': code
                })

print(f'Total Mermaid blocks found: {len(mermaid_blocks)}')
for b in mermaid_blocks:
    print(f"File: {b['file']} | Block #{b['index']} | Type: {b['first_line']} ({b['lines_count']} lines)")
