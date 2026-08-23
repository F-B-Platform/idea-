# -*- coding: utf-8 -*-
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\.agents\challenger_5docs_keywords\empirical_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fname in ['Actor_Phan_Quyen_Chuc_Nang.md', 'Workflow_Quy_Trinh_Nghiep_Vu.md']:
    res = data[fname]
    ellipses = res['check2_placeholders']['ellipsis']
    print('=' * 75)
    print('ELLIPSES IN ' + fname + ' (Count: ' + str(len(ellipses)) + ')')
    print('=' * 75)
    for m in ellipses:
        print('Line ' + str(m['line']) + ': ' + m['content'])
