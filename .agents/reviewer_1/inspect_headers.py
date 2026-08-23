import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def inspect_file(rel_path):
    path = os.path.join(DOCS_DIR, rel_path.replace("/", os.sep))
    print(f"\n=======================================================")
    print(f"FILE: {rel_path}")
    print(f"=======================================================")
    if not os.path.exists(path):
        print("FILE NOT FOUND!")
        return
    with open(path, "r", encoding="utf-8", errors="ignore") as fp:
        lines = fp.readlines()
    print(f"Total lines: {len(lines)}")
    # Print headers
    headers = [line.strip() for line in lines if line.startswith("#")]
    print(f"Headers count: {len(headers)}")
    for h in headers[:15]:
        print(" ", h)
    if len(headers) > 15:
        print(f"  ... and {len(headers) - 15} more headers")

inspect_file("01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md")
inspect_file("01_Tai_Lieu_Dac_Ta_Goc/Actor_Phan_Quyen_Chuc_Nang.md")
inspect_file("01_Tai_Lieu_Dac_Ta_Goc/Tom_Tat_1_Trang_Executive_Summary.md")
inspect_file("01_Tai_Lieu_Dac_Ta_Goc/Tong_Quan_Kien_Truc_He_Thong.md")
inspect_file("01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md")
