import os
import re
import subprocess
import json
import tempfile
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"
FILES = [
    "01_Kien_Truc_Tong_Quan.md",
    "02_Sequence_Diagrams.md",
    "03_ERD_Database_Diagram.md",
    "04_Deployment_Diagram.md"
]
PUPPETEER_CFG = r"d:\Idea_DoAn\.agents\challenger_1\puppeteer-config.json"

print("=================================================================")
print("  STEP 1: EMPIRICAL MERMAID SYNTAX VALIDATION VIA MMDC & CHROME  ")
print("=================================================================")

mermaid_results = {}

for fname in FILES:
    fpath = os.path.join(DIAG_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Normalize CRLF to LF
    content_lf = content.replace('\r\n', '\n')
    
    # Find all mermaid blocks with start and end line numbers
    pattern = re.compile(r'`mermaid\n(.*?)\n`', re.DOTALL)
    matches = list(pattern.finditer(content_lf))
    
    print(f"\nScanning {fname}: Found {len(matches)} Mermaid code blocks")
    mermaid_results[fname] = []
    
    for idx, match in enumerate(matches):
        block = match.group(1)
        start_char = match.start()
        start_line = content_lf[:start_char].count('\n') + 1
        end_line = start_line + block.count('\n') + 1
        
        # Create temp file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".mmd", delete=False, encoding="utf-8") as tmp_in:
            tmp_in.write(block)
            tmp_in_path = tmp_in.name
            
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tmp_out:
            tmp_out_path = tmp_out.name
            
        try:
            cmd = f'npx.cmd -p @mermaid-js/mermaid-cli mmdc -p "{PUPPETEER_CFG}" -i "{tmp_in_path}" -o "{tmp_out_path}"'
            proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=45)
            
            first_line = block.strip().split('\n')[0] if block.strip() else "EMPTY"
            diag_type = first_line.split()[0] if first_line else "UNKNOWN"
            
            if proc.returncode == 0:
                status = "PASS"
                err = ""
            else:
                status = "FAIL"
                err = (proc.stderr or proc.stdout).strip()
                
            mermaid_results[fname].append({
                "block_number": idx + 1,
                "lines": f"{start_line}-{end_line}",
                "diagram_type": diag_type,
                "header_preview": first_line[:60],
                "status": status,
                "error": err,
                "block_length": len(block)
            })
            print(f"  [{status}] Block #{idx+1} (L{start_line}-L{end_line}) [{diag_type}]: {first_line[:40]}...")
            if status == "FAIL":
                print(f"      >>> ERROR DETAILS:\n{err}\n")
        except Exception as e:
            mermaid_results[fname].append({
                "block_number": idx + 1,
                "lines": f"{start_line}-{end_line}",
                "diagram_type": "ERROR",
                "header_preview": "EXCEPTION",
                "status": "ERROR",
                "error": str(e),
                "block_length": len(block)
            })
            print(f"  [ERROR] Block #{idx+1}: {str(e)}")
        finally:
            if os.path.exists(tmp_in_path):
                os.remove(tmp_in_path)
            if os.path.exists(tmp_out_path):
                os.remove(tmp_out_path)

with open(r"d:\Idea_DoAn\.agents\challenger_1\mermaid_audit_results.json", "w", encoding="utf-8") as f:
    json.dump(mermaid_results, f, indent=2, ensure_ascii=False)

total_blocks = sum(len(v) for v in mermaid_results.values())
passed_blocks = sum(sum(1 for b in v if b['status'] == 'PASS') for v in mermaid_results.values())
failed_blocks = total_blocks - passed_blocks
print(f"\n=================================================================")
print(f">>> MERMAID VERIFICATION SUMMARY: Total={total_blocks}, Passed={passed_blocks}, Failed={failed_blocks}")
print("=================================================================")