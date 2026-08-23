# -*- coding: utf-8 -*-
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\.agents\challenger_5docs_keywords\empirical_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fname, res in data.items():
    print('=' * 75)
    print('FILE: ' + fname + ' (' + str(res['line_count']) + ' lines)')
    print('=' * 75)
    
    # Check 1
    print('[Check 1] C-23 / C-24 Forbidden Features: ' + str(len(res['check1_c23_c24'])) + ' matches')
    for m in res['check1_c23_c24']:
        print('    Line ' + str(m['line']) + ': [' + m['match'] + '] ' + m['content'])

    # Check 3
    print('[Check 3] Staff Mobile App: ' + str(len(res['check3_staff_app'])) + ' matches')
    for m in res['check3_staff_app']:
        print('    Line ' + str(m['line']) + ': ' + m['content'])

    # Check 2
    print('[Check 2] Placeholders:')
    for k, v in res['check2_placeholders'].items():
        print('    - ' + k + ': ' + str(len(v)) + ' matches')
        if k != 'ellipsis' and len(v) > 0:
            for m in v:
                print('        Line ' + str(m['line']) + ': ' + m['content'])
        if k == 'ellipsis' and len(v) > 0:
            print('        (Ellipsis count: ' + str(len(v)) + ')')

    # Check 4
    print('[Check 4] Dine-In Payment:')
    for k, v in res['check4_dinein_payment'].items():
        print('    - ' + k + ': ' + str(len(v)) + ' matches')

    # Check 5
    print('[Check 5] Delivery:')
    for k, v in res['check5_delivery'].items():
        print('    - ' + k + ': ' + str(len(v)) + ' matches')

    # Check 6
    print('[Check 6] Takeaway Loyalty:')
    for k, v in res['check6_takeaway_loyalty'].items():
        print('    - ' + k + ': ' + str(len(v)) + ' matches')

    # Check 7
    print('[Check 7] WiFi Attendance:')
    for k, v in res['check7_wifi_attendance'].items():
        print('    - ' + k + ': ' + str(len(v)) + ' matches')
