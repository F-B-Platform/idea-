import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\README.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== README.md SECTION 3 & 4 ===")
match3 = re.search(r"# 3\.\s+BẢN ĐỒ PHÂN PHỐI", content)
match4 = re.search(r"# 4\.\s+MA TRẬN TRUY VẾT", content)
match5 = re.search(r"# 5\.\s+HƯỚNG DẪN KHỞI CHẠY", content)

if match3 and match4:
    print(content[match3.start():match4.start()])
if match4 and match5:
    print(content[match4.start():match4.start()+2500])
