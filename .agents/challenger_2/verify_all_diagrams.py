import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TARGET_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"
OUTPUT_DIR = r"d:\Idea_DoAn\.agents\challenger_2\temp_mmd"
CONFIG_PATH = r"d:\Idea_DoAn\.agents\challenger_2\puppeteer-config.json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

files = [
    "01_Kien_Truc_Tong_Quan.md",
    "02_Sequence_Diagrams.md",
    "03_ERD_Database_Diagram.md",
    "04_Deployment_Diagram.md"
]

results = []

for filename in files:
    filepath = os.path.join(TARGET_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    in_block = False
    block_lines = []
    start_line = 0
    current_heading = "Top of file"
    diagram_idx = 0
    
    for i, line in enumerate(lines, 1):
        if line.startswith("#"):
            current_heading = line.strip()
        
        if line.strip().startswith("```mermaid"):
            in_block = True
            start_line = i
            block_lines = []
            diagram_idx += 1
            continue
        
        if in_block and line.strip().startswith("```"):
            in_block = False
            end_line = i
            mermaid_code = "".join(block_lines)
            
            diagram_id = f"{filename[:-3]}_diag_{diagram_idx}"
            mmd_path = os.path.join(OUTPUT_DIR, f"{diagram_id}.mmd")
            svg_path = os.path.join(OUTPUT_DIR, f"{diagram_id}.svg")
            
            with open(mmd_path, "w", encoding="utf-8") as mmd_f:
                mmd_f.write(mermaid_code)
            
            # Run mmdc
            cmd = [
                "npx", "--yes", "@mermaid-js/mermaid-cli",
                "-p", CONFIG_PATH,
                "-i", mmd_path,
                "-o", svg_path
            ]
            
            try:
                proc = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=60)
                success = proc.returncode == 0
                error_msg = proc.stderr.strip() if proc.stderr else proc.stdout.strip()
            except subprocess.TimeoutExpired:
                success = False
                error_msg = "Timeout rendering diagram (60s)"
            except Exception as e:
                success = False
                error_msg = str(e)
            
            # Detect diagram type
            first_non_empty = ""
            for bline in block_lines:
                if bline.strip() and not bline.strip().startswith("%%"):
                    first_non_empty = bline.strip().split()[0]
                    break
            
            res = {
                "file": filename,
                "index": diagram_idx,
                "id": diagram_id,
                "heading": current_heading,
                "lines": f"L{start_line}-L{end_line}",
                "type": first_non_empty,
                "code_len": len(mermaid_code),
                "success": success,
                "error": error_msg
            }
            results.append(res)
            status_str = "PASS" if success else "FAIL"
            print(f"[{status_str}] {filename} #{diagram_idx} ({first_non_empty}) {current_heading} ({res['lines']})")
            if not success:
                print(f"    ERROR: {error_msg}")
            
            continue
        
        if in_block:
            block_lines.append(line)

print("\n" + "="*80)
print(f"TOTAL DIAGRAMS TESTED: {len(results)}")
passed = sum(1 for r in results if r['success'])
failed = sum(1 for r in results if not r['success'])
print(f"PASSED: {passed}, FAILED: {failed}")
print("="*80)

for r in results:
    if not r['success']:
        print(f"FAILED DIAGRAM: {r['file']} #{r['index']} [{r['lines']}] - {r['heading']}")
        print(f"Error details: {r['error']}\n")

import json
with open(os.path.join(OUTPUT_DIR, "results.json"), "w", encoding="utf-8") as jf:
    json.dump(results, jf, indent=2, ensure_ascii=False)
