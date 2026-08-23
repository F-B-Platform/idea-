
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\.agents\challenger_1\scan_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for pat in ['Staff Mobile App', 'Staff App', 'GPS 50m', 'GPS lock', 'GPS general']:
    matches = data['obsolete'][pat]
    print(f'=== {pat} ({len(matches)} matches) ===')
    for m in matches:
        fn = m['file']
        ln = m['line']
        cnt = m['content']
        print(f'{fn}:{ln}: {cnt}')
