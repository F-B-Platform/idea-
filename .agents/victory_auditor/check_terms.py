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

terms = [
    'Staff App',
    'Staff Mobile App',
    'GPS lock',
    'GPS 50m',
    'QR động 30 giây',
    'QR xoay 30',
    'thanh toán sau',
    'yêu cầu bill',
]

results = {t: [] for t in terms}

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        for t in terms:
            if t.lower() in line.lower():
                results[t].append((rel_path, idx, line.strip()))

for t, matches in results.items():
    print(f'=== Keyword: "{t}" (Total matches: {len(matches)}) ===')
    for m in matches:
        print(f'  {m[0]}:{m[1]} -> {m[2]}')
