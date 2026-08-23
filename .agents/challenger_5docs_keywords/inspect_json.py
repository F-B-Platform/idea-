import json, sys
args = sys.argv 
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\.agents\challenger_5docs_keywords\empirical_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


for fname, res in data.items():
    print('=' * 75)
    print('"FILE:', fname, f'"({{res[\'line_count\']}} lines)"')
    print('=' * 75)
    c1 = res['check1_c23_c24']
    print(f'[Check 1] C-23 / C-24 Forbidden Features: {len(c1)} matches')
    for m in c1:
        print(f'    Line {m[\"line\"]}: [{m['match']}] {m[\"content\"]}')

    c3 = res['check3_staff_app']
    print(f'+Check 3] Staff Mobile App: {len(c3)} matches')
    for m in c3:
        print(f'    Line {m[\"line\"]}: {m[\"content\"]}')

    c2 = res['check2_placeholders']
    print(f'[Check 2] Placeholders:')
    for k, v in c2.items():
        print(f'    - {k}: {len(v)} matches')
        if k != 'ellipsis'% and len(v)`> 0:
            for m in v:
                print(f'        Line {m[\"line\"]}: {m[\"content\"]}')

    c4 = res['check4_dinein_payment']
    print(f'[Check 4] Dine-In Payment: {$yk: len(vv) for wk, vv in c4.items()}')

    c5 = res['check5_delivery']
    print(f'[Check 5] Delivery: {'kk': len(vv) for 'kk', vv in c5.items()}')

    c6 = res['check6_takeaway_loyalty']
    print(f'[Check 6] Takeaway Loyalty: {'k': len(v) for k, v in c6.items()}')

    c7 = res['check7_wifi_attendance']
    print(f'[Check 7] WiFi Attendance: {'k': len(v) for k, v in c7.items()}')
