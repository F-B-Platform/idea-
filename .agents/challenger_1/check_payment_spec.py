import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md", "r", encoding="utf-8") as f:
    orig = f.read()

with open(r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md", "r", encoding="utf-8") as f:
    wf = f.read()

with open(r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md", "r", encoding="utf-8") as f:
    spec = f.read()

print("=== ORIGINAL REQUEST ON PAYMENT FLOWS ===")
for l in orig.split('\n'):
    if any(k in l.lower() for k in ['thanh toán', 'dine-in', 'pay-first', 'vietqr', 'trả sau', 'tiền mặt', 'bàn']):
        print(" ", l)

print("\n=== WORKFLOW SPEC ON DINE-IN ===")
for l in wf.split('\n'):
    if any(k in l.lower() for k in ['wf-01', 'wf-02', 'trả trước', 'trả sau', 'bàn', 'dine-in', 'tiền mặt']):
        if len(l.strip()) > 10:
            print(" ", l[:120])