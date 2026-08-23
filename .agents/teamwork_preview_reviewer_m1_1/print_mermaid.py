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

print("=== MERMAID BLOCK 1 (File 1) ===")
print(m1_blocks[0].strip())

print("\n=== MERMAID BLOCK 2 (File 2) ===")
print(m2_blocks[0].strip())

