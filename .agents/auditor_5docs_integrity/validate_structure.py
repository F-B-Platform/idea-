import os
import sys
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

docs_dir = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'
files = [
    'Smart_FB_Operating_System.md',
    'Actor_Phan_Quyen_Chuc_Nang.md',
    'Workflow_Quy_Trinh_Nghiep_Vu.md',
    'Tong_Quan_Kien_Truc_He_Thong.md',
    'Tom_Tat_1_Trang_Executive_Summary.md'
]

print("=== CHECKING MERMAID SYNTAX ===")
for fname in files:
    path = os.path.join(docs_dir, fname)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    mermaid_blocks = re.findall(r'```mermaid([\s\S]*?)```', content)
    print(f"File {fname}: {len(mermaid_blocks)} diagrams found")
    for idx, block in enumerate(mermaid_blocks):
        lines = [l for l in block.strip().splitlines() if l.strip()]
        if not lines:
            print(f"  [ERROR] Diagram {idx+1} is empty!")
            continue
        diag_type = lines[0].strip().split()[0]
        # Basic balance check for brackets
        opens = block.count('{') + block.count('[') + block.count('(')
        closes = block.count('}') + block.count(']') + block.count(')')
        # In Mermaid ERD, { and } wrap attributes
        print(f"  Diagram {idx+1}: Type '{lines[0].strip()}', {len(lines)} lines")

print("\n=== CROSS-REFERENCING ACTORS AND MODULES ===")
# Check Actors in Actor_Phan_Quyen_Chuc_Nang.md
actor_file = os.path.join(docs_dir, 'Actor_Phan_Quyen_Chuc_Nang.md')
with open(actor_file, 'r', encoding='utf-8') as fp:
    actor_content = fp.read()

actors = re.findall(r'###\s*([A-Z0-9_\-]+)\s*:\s*(.*?)\n', actor_content)
print(f"Found {len(actors)} sub-actors / feature groups in Actor doc:")
for a in actors[:10]:
    print(f"  - {a[0]}: {a[1]}")

# Check Workflows in Workflow_Quy_Trinh_Nghiep_Vu.md
wf_file = os.path.join(docs_dir, 'Workflow_Quy_Trinh_Nghiep_Vu.md')
with open(wf_file, 'r', encoding='utf-8') as fp:
    wf_content = fp.read()

wfs = re.findall(r'##\s*(WF-[0-9A-Za-z]+)\s*:\s*(.*?)\n', wf_content)
print(f"\nFound {len(wfs)} Workflows in Workflow doc:")
for wf in wfs:
    print(f"  - {wf[0]}: {wf[1]}")

# Check Database tables in Tong_Quan_Kien_Truc_He_Thong.md
arch_file = os.path.join(docs_dir, 'Tong_Quan_Kien_Truc_He_Thong.md')
with open(arch_file, 'r', encoding='utf-8') as fp:
    arch_content = fp.read()

erd_tables = re.findall(r'([A-Z0-9_]+)\s*\{([^}]+)\}', arch_content)
print(f"\nFound {len(erd_tables)} Entities in ERD:")
for tbl, attrs in erd_tables:
    attr_count = len([l for l in attrs.strip().splitlines() if l.strip()])
    print(f"  - {tbl}: {attr_count} attributes")

