# -*- coding: utf-8 -*-
import json, sys, re, os

sys.stdout.reconfigure(encoding='utf-8')

target_dir = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'
files = [
    'Smart_FB_Operating_System.md',
    'Actor_Phan_Quyen_Chuc_Nang.md',
    'Workflow_Quy_Trinh_Nghiep_Vu.md',
    'Tong_Quan_Kien_Truc_He_Thong.md',
    'Tom_Tat_1_Trang_Executive_Summary.md'
]

for fname in files:
    p = os.path.join(target_dir, fname)
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
        
    print('=' * 75)
    print('DINE-IN PAYMENT ANALYSIS IN ' + fname)
    print('=' * 75)
    
    # Check mentions of Dine-In payment models
    lines = text.splitlines()
    for idx, line in enumerate(lines, 1):
        if any(w in line.lower() for w in ['trả trước', 'trả sau', 'tùy chọn thanh toán', 'phương thức thanh toán', 'tiền mặt', 'vietqr']) and any(w in line.lower() for w in ['dine-in', 'tại bàn', 'bàn', 'dine_in']):
            print('Line ' + str(idx) + ': ' + line.strip()[:140])
