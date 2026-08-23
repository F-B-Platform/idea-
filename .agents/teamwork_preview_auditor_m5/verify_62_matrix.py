import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

TARGET_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"

customer_feats = [f"C-{i:02d}" for i in range(1, 21)]
staff_feats = [f"S-{i:02d}" for i in range(1, 14)]
manager_feats = [f"M-{i:02d}" for i in range(1, 12+1)]
admin_feats = [f"A-{i:02d}" for i in range(1, 17+1)]
all_feats = customer_feats + staff_feats + manager_feats + admin_feats

files_to_check = [
    "01_Phan_Tich_Yeu_Cau.md",
    "04_Thiet_Ke_UI_UX.md",
    "05_Quy_Trinh_Backend.md",
    "06_Quy_Trinh_Frontend.md",
    "07_Ke_Hoach_Kiem_Thu.md",
    "README.md"
]

print(f"Checking {len(all_feats)} features across {len(files_to_check)} files:")

for fname in files_to_check:
    fpath = os.path.join(TARGET_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    missing = [f for f in all_feats if f not in content]
    print(f"File {fname:30} -> Present: {len(all_feats) - len(missing)}/62 | Missing: {len(missing)}")
    if missing:
        print(f"   Missing IDs in {fname}: {missing}")
