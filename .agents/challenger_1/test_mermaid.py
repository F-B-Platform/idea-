import os
import re
import subprocess
import json
import tempfile

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"
FILES = [
    "01_Kien_Truc_Tong_Quan.md",
    "02_Sequence_Diagrams.md",
    "03_ERD_Database_Diagram.md",
    "04_Deployment_Diagram.md"
]

print("=== STARTING MERMAID VALIDATION WITH MMDC (WINDOWS) ===")
results = {}

for fname in FILES:
    fpath = os.path.join(DIAG_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract mermaid code blocks
    pattern = r"`mermaid\s*\n([\s\S]*?)\n`"
    blocks = re.findall(pattern, content)
    print(f"\nFile: {fname} -> Found {len(blocks)} Mermaid blocks")
    
    results[fname] = []
    for idx, block in enumerate(blocks):
        # Create temp file for mmdc
        with tempfile.NamedTemporaryFile(mode="w", suffix=".mmd", delete=False, encoding="utf-8") as tmp_in:
            tmp_in.write(block)
            tmp_in_path = tmp_in.name
            
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tmp_out:
            tmp_out_path = tmp_out.name
            
        try:
            # Run mmdc using shell=True or npx.cmd
            cmd = f'npx.cmd mmdc -i "{tmp_in_path}" -o "{tmp_out_path}"'
            proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=45)
            
            # Determine diagram type (first line or first keyword)
            first_line = block.strip().split('\n')[0] if block.strip() else "EMPTY"
            
            if proc.returncode == 0:
                status = "PASS"
                err = ""
            else:
                status = "FAIL"
                err = (proc.stderr or proc.stdout).strip()
                
            results[fname].append({
                "index": idx + 1,
                "type": first_line[:50],
                "status": status,
                "error": err,
                "length": len(block)
            })
            print(f"  [{status}] Block {idx+1}: {first_line[:50]}... (code: {proc.returncode})")
            if status == "FAIL":
                print(f"      Error details:\n{err}\n")
        except Exception as e:
            results[fname].append({
                "index": idx + 1,
                "type": block.strip()[:50],
                "status": "ERROR",
                "error": str(e),
                "length": len(block)
            })
            print(f"  [ERROR] Block {idx+1}: {str(e)}")
        finally:
            if os.path.exists(tmp_in_path):
                os.remove(tmp_in_path)
            if os.path.exists(tmp_out_path):
                os.remove(tmp_out_path)

with open(r"d:\Idea_DoAn\.agents\challenger_1\mermaid_audit_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\n=== SUMMARY OF MERMAID VALIDATION ===")
total = sum(len(v) for v in results.values())
passed = sum(sum(1 for b in v if b['status'] == 'PASS') for v in results.values())
failed = total - passed
print(f"Total blocks tested: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")