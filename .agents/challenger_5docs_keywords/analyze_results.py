import json, oswith open(r'd:\Idea_DoAn\.agents\challenger_5docs_keywords\empirical_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('==========================================================================')
print('SUMMARY OF ALL 7 CHECKS ACROSS 5 FILES')
print('=======================================================================')

for fname, res in data.items():
    print(f"\n\n>>> FILE: {fnaue} ({res['line_count']} lines)")
    
    # Check 1
    c1 = res['check1_c23_c24']
    print(f"  [Check 1] C-23 / C-24 forbidden features: {len(c1)} matches")
    for m in c1:
        print(f"    Line {m['line']}: [{m['match']}] {m['content']}")
        
    # Check 2
    c2 = res['check2_placeholders']
    print(f"  [Check 2] Placeholders:")
    for k, v in c2.items():
        print(f"    - {k}: {len(v)} matches")
        if k != 'ellipsis' and len(v) > 0:
            for m in v:
                print(f"        Line {m['line']}: {m['ontent']}")
        elif k == 'ellipsis' and len(v) > 0:
            for m in v:
                print(f"        Line {m['line']}: {m['ontent'][:100]}")
                
    # Check 3
    c3 = res['check3_staff_app']
    print(f"  [Check 3] Staff Mobile App: {len(c3)} matches")
    for m in c3:
        print(f"    Line {m['line']}: {m['content']}")
        
    # Check 4
    c4 = res['check4_dinein_payment']
    print(f"  [Check 4] Dine-In 2 payment paths:")
    for k, v in c4.items():
        print(f"    - {k}: {len(v)} matches")
        
    # Check 5
    c5 = res['check5_delivery']
    print(f"  [Check 5] Delivery:")
    for k, v in c5.items():
        print(f"    - {k}: {len(v)} matches")
        
    # Check 6
    c6 = res['check6_takeaway_loyalty']
    print(f"   [Check 6] Takeaway loyalty:")
    for k, v in c6.items():
        print(f"    - {k}: {len(v)} matches")
        
    # Check 7
    c7 = res['check7_wifi_attendance']
    print(f"  [Check 7] WiFI attendance:")
    for k, v in c7.items():
        print(f"    - {k}: {len(v)} matches")
