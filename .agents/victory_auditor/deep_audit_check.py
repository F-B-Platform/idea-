# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

folder = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'

print('=== 1. CHECK DINE-IN 2 DISTINCT FLOWS & STATUS PATHS ===')
wf_path = os.path.join(folder, 'Workflow_Quy_Trinh_Nghiep_Vu.md')
with open(wf_path, 'r', encoding='utf-8') as fh:
    wf_text = fh.read()

# Search for Dine in workflows
print('Checking Dine-In workflows in Workflow_Quy_Trinh_Nghiep_Vu.md:')
matches = re.findall(r'(###\s*WF-01[\s\S]*?)(?=###\s*WF-02|\Z)', wf_text)
if matches:
    print(matches[0][:1500])
else:
    print('WF-01 not found by regex, searching headers...')
    for line in wf_text.splitlines():
        if 'WF-' in line:
            print('  ', line)

print('\n' + '='*60)
print('=== 2. CHECK ADMIN CRUD CAPABILITIES ===')
actor_path = os.path.join(folder, 'Actor_Phan_Quyen_Chuc_Nang.md')
with open(actor_path, 'r', encoding='utf-8') as fh:
    actor_text = fh.read()

admin_keywords = ['CRUD', 'combo', 'upload', 'giá theo chi nhánh', '86', 'menu mùa']
for kw in admin_keywords:
    found = kw.lower() in actor_text.lower()
    print(f'Admin capability: {kw} -> Found in Actor doc: {found}')

print('\n' + '='*60)
print('=== 3. CHECK 16 WORKFLOWS IN WORKFLOW DOC ===')
for i in range(1, 17):
    wf_id = f'WF-{i:02d}'
    found = wf_id in wf_text
    print(f'Workflow {wf_id}: Found = {found}')

print('\n' + '='*60)
print('=== 4. CHECK SCALE UP / FUTURE WORK SECTIONS ===')
for f in ['Smart_FB_Operating_System.md', 'Actor_Phan_Quyen_Chuc_Nang.md', 'Workflow_Quy_Trinh_Nghiep_Vu.md', 'Tong_Quan_Kien_Truc_He_Thong.md', 'Tom_Tat_1_Trang_Executive_Summary.md']:
    p = os.path.join(folder, f)
    with open(p, 'r', encoding='utf-8') as fh:
        t = fh.read()
    has_scaleup = ('scale up' in t.lower() or 'future work' in t.lower() or 'lộ trình mở rộng' in t.lower())
    print(f'{f}: Scale Up / Future Work present = {has_scaleup}')
