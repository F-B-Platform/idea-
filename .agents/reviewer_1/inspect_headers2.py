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
    for h in headers[:10]:
        print(" ", h)
    if len(headers) > 10:
        print(f"  ... and {len(headers) - 10} more headers")

inspect_file("02_Bao_Gia_Chi_Phi/Bang_Bao_Gia_Smart_FB_OS.md")
inspect_file("02_Bao_Gia_Chi_Phi/Chi_Phi_Duy_Tri_Hang_Thang.md")
inspect_file("03_Quy_Trinh_Trien_Khai/01_Phan_Tich_Yeu_Cau.md")
inspect_file("03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md")
inspect_file("03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md")
inspect_file("03_Quy_Trinh_Trien_Khai/04_Thiet_Ke_UI_UX.md")
inspect_file("03_Quy_Trinh_Trien_Khai/05_Quy_Trinh_Backend.md")
inspect_file("03_Quy_Trinh_Trien_Khai/06_Quy_Trinh_Frontend.md")
inspect_file("03_Quy_Trinh_Trien_Khai/07_Ke_Hoach_Kiem_Thu.md")
inspect_file("03_Quy_Trinh_Trien_Khai/08_Trien_Khai_He_Thong.md")
inspect_file("03_Quy_Trinh_Trien_Khai/README.md")
inspect_file("04_Thiet_Ke_Kien_Truc_Diagrams/01_Kien_Truc_Tong_Quan.md")
inspect_file("04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md")
inspect_file("04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md")
inspect_file("04_Thiet_Ke_Kien_Truc_Diagrams/04_Deployment_Diagram.md")
inspect_file("05_Quy_Chuan_&_Test_Cases/Git_Workflow_&_Branching_Strategy.md")
inspect_file("05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md")
inspect_file("05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md")
inspect_file("06_Danh_Sach_Skills/README.md")
inspect_file("ROADMAP.md")
inspect_file("DOC_AUDIT_REPORT.md")
