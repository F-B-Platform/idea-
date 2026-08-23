# -*- coding: utf-8 -*-
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\.agents\challenger_5docs_keywords\empirical_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fname, res in data.items():
    staff_app_matches = res['check3_staff_app']
    print('=' * 75)
    print('STAFF MOBILE APP IN ' + fname + ' (Count: ' + str(len(staff_app_matches)) + ')')
    print('=' * 75)
    for m in staff_app_matches:
        print('Line ' + str(m['line']) + ': ' + m['content'])
