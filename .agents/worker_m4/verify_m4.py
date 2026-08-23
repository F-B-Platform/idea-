# -*- coding: utf-8 -*-
"""
Verification Script for Worker M4 Deliverables
"""
import os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files_to_check = [
    r'd:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md',
    r'd:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md',
    r'd:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md',
    r'd:\Idea_DoAn\06_Danh_Sach_Skills\README.md',
    r'd:\Idea_DoAn\02_Bao_Gia_Chi_Phi\Bang_Bao_Gia_Smart_FB_OS.md',
    r'd:\Idea_DoAn\02_Bao_Gia_Chi_Phi\Chi_Phi_Duy_Tri_Hang_Thang.md'
]

placeholders = ['TODO', 'TBD', '/* rest of code */', '// tương tự như trên', '// giữ nguyên logic cũ']

all_passed = True
print("=== VERIFYING WORKER M4 DELIVERABLES ===")

for fp in files_to_check:
    if not os.path.exists(fp):
        print(f"[FAIL] Missing file: {fp}")
        all_passed = False
        continue
    
    size = os.path.getsize(fp)
    if size == 0:
        print(f"[FAIL] Empty file: {fp}")
        all_passed = False
        continue
        
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()
        
    found_placeholders = []
    for p in placeholders:
        if p in content:
            found_placeholders.append(p)
            
    if found_placeholders:
        print(f"[WARN] Found placeholders {found_placeholders} in {fp}")
        all_passed = False
    else:
        print(f"[PASS] {os.path.basename(fp)} -> {size:,} bytes | {len(lines):,} lines | 0 placeholders")

if all_passed:
    print("\nALL 6 WORKER M4 DELIVERABLES VERIFIED 100% SUCCESSFUL!")
else:
    print("\nVerification found issues that need fixing.")
    sys.exit(1)
