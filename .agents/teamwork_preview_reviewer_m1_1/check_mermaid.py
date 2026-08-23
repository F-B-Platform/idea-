import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

f1_path = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md"
f2_path = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"

with open(f1_path, "r", encoding="utf-8") as f:
    f1 = f.read()

with open(f2_path, "r", encoding="utf-8") as f:
    f2 = f.read()

m1_blocks = re.findall(r"```mermaid(.*?)```", f1, re.DOTALL)
m2_blocks = re.findall(r"```mermaid(.*?)```", f2, re.DOTALL)

print(f"File 1 has {len(m1_blocks)} mermaid blocks")
for i, b in enumerate(m1_blocks):
    print(f"\n--- File 1 Mermaid Block {i+1} ---")
    print(b.strip()[:300] + ("..." if len(b.strip()) > 300 else ""))

print(f"\nFile 2 has {len(m2_blocks)} mermaid blocks")
for i, b in enumerate(m2_blocks):
    print(f"\n--- File 2 Mermaid Block {i+1} ---")
    print(b.strip()[:500] + ("..." if len(b.strip()) > 500 else ""))

