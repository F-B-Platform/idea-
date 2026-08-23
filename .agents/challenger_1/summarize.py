
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\.agents\challenger_1\scan_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('=== 1. OBSOLETE KEYWORDS SUMMARY ===')
for pat, matches in data['obsolete'].items():
    print(f'\nPattern: {pat} -> Total matches: {len(matches)}')
    by_file = {}
    for m in matches:
        by_file.setdefault(m['file'], []).append(m)
    for fn, flist in by_file.items():
        print(f'  File: {fn} ({len(flist)} matches)')
        for item in flist[:5]:
            ln = item['line']
            cnt = item['content'][:110]
            print(f'    Line {ln}: {cnt}')
        if len(flist) > 5:
            print(f'    ... and {len(flist) - 5} more')

print('\n=== 2. MANDATORY KEYWORDS SUMMARY ===')
for pat, info in data['mandatory'].items():
    t_m = info['total_matches']
    t_f = info['total_files']
    flist = info['files']
    print(f'Pattern: {pat:18} -> Total matches: {t_m:4}, in {t_f:2} files')
    if t_f < 10:
        print(f'   Files: {flist}')

print('\n=== 3. PLACEHOLDER SUMMARY ===')
for pat, matches in data['placeholders'].items():
    print(f'\nPattern: {pat} -> Total matches: {len(matches)}')
    by_file = {}
    for m in matches:
        by_file.setdefault(m['file'], []).append(m)
    for fn, flist in by_file.items():
        print(f'  File: {fn} ({len(flist)} matches)')
        for item in flist[:5]:
            ln = item['line']
            cnt = item['content'][:110]
            print(f'    Line {ln}: {cnt}')
        if len(flist) > 5:
            print(f'    ... and {len(flist) - 5} more')
