import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

path = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find all workflows: format "## 🔄 WF-..."
wfs = re.findall(r'(##\s*🔄?\s*(WF-[0-9A-Za-z]+)\s*:\s*([^\n]+))', text)
print(f"Total Workflows found: {len(wfs)}")
for full_header, wf_code, wf_title in wfs:
    print(f"\n[{wf_code}] {wf_title.strip()}")
    # find workflow section
    start_pos = text.find(full_header)
    # find next workflow or end
    next_match = re.search(r'\n##\s*🔄?\s*WF-', text[start_pos+len(full_header):])
    if next_match:
        wf_body = text[start_pos : start_pos + len(full_header) + next_match.start()]
    else:
        wf_body = text[start_pos:]
    
    # check sub-sections: Mục đích, Tác nhân, Điều kiện, Hợp đồng dữ liệu, Các bước, Sơ đồ, Ngoại lệ
    sub_sections = ['Mục đích', 'Tác nhân', 'Điều kiện tiên quyết', 'Hợp đồng dữ liệu', 'Các bước thực hiện', 'Sơ đồ tuần tự', 'Xử lý ngoại lệ']
    sub_status = [f"{s}: {'OK' if s.lower() in wf_body.lower() else 'MISSING'}" for s in sub_sections]
    print(f"  Sections: {', '.join(sub_status)}")
    print(f"  Length: {len(wf_body.splitlines())} lines")
