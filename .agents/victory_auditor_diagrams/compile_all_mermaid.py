import os
import re
import subprocess
import sys

files = {
    '01_Kien_Truc_Tong_Quan': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    '02_Sequence_Diagrams': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    '03_ERD_Database_Diagram': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    '04_Deployment_Diagram': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md'
}

out_dir = r'd:\Idea_DoAn\.agents\victory_auditor_diagrams\mermaid_test'
os.makedirs(out_dir, exist_ok=True)

mmd_files = []

for file_key, file_path in files.items():
    content = open(file_path, encoding='utf-8').read()
    mermaid_blocks = re.findall(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL)
    for idx, block in enumerate(mermaid_blocks, 1):
        mmd_name = f"{file_key}_block_{idx:02d}.mmd"
        mmd_path = os.path.join(out_dir, mmd_name)
        with open(mmd_path, 'w', encoding='utf-8') as f:
            f.write(block.strip())
        mmd_files.append((mmd_name, mmd_path, file_key, idx))

print(f"Extracted {len(mmd_files)} Mermaid diagram files into {out_dir}")
print("Starting independent compilation using @mermaid-js/mermaid-cli...\n")

results = []
for mmd_name, mmd_path, file_key, idx in mmd_files:
    svg_path = mmd_path.replace('.mmd', '.svg')
    cmd = f'npx -y @mermaid-js/mermaid-cli -i "{mmd_path}" -o "{svg_path}"'
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    success = (proc.returncode == 0 and os.path.exists(svg_path))
    svg_size = os.path.getsize(svg_path) if success else 0
    results.append({
        'name': mmd_name,
        'file': file_key,
        'idx': idx,
        'success': success,
        'returncode': proc.returncode,
        'stderr': proc.stderr.strip() if proc.stderr else '',
        'stdout': proc.stdout.strip() if proc.stdout else '',
        'svg_size': svg_size
    })
    status = "SUCCESS" if success else "FAILED"
    print(f"[{status}] {mmd_name} -> {svg_size} bytes (code: {proc.returncode})")
    if not success:
        print(f"  STDERR: {proc.stderr[:300]}")
        print(f"  STDOUT: {proc.stdout[:300]}")

total = len(results)
passed = sum(1 for r in results if r['success'])
print(f"\n==========================================")
print(f"MERMAID COMPILATION SUMMARY: {passed}/{total} PASSED")
print(f"==========================================")

if passed == total:
    print("ALL MERMAID DIAGRAMS COMPILED PERFECTLY TO SVG WITH ZERO SYNTAX ERRORS!")
else:
    print(f"ERROR: {total - passed} DIAGRAM(S) FAILED COMPILATION.")
