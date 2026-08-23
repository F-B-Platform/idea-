import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# Parse section 4 (Chi tiết các Test Cases)
sec4_match = re.search(r"## 4\. DANH SÁCH CHI TIẾT CÁC TEST CASES UAT(.*)", text, re.DOTALL)
if not sec4_match:
    print("Section 4 not found!")
    sys.exit(1)

sec4_text = sec4_match.group(1)

# Find all test case subsections in Section 4: starts with #### `TC-...`
tc_blocks = re.split(r"(?=####\s+[`\*]*(?:TC-[A-Z0-9_\-]+))", sec4_text)
# the first chunk is before the first ####
tc_cases = tc_blocks[1:]
print(f"Total Detailed Test Case Sections in Section 4: {len(tc_cases)}")

fields = [
    ("Mã Test / Tiêu đề", r"####\s+[`\*]*(TC-[A-Z0-9_\-]+)"),
    ("Mục đích", r"\*\*Mục đích\*\*|\*\*Mục tiêu\*\*"),
    ("Tiền điều kiện", r"\*\*Tiền điều kiện\*\*"),
    ("Các bước thực hiện", r"\*\*Các bước thực hiện\*\*"),
    ("Dữ liệu đầu vào", r"\*\*Dữ liệu đầu vào\*\*|\*\*Payload mẫu\*\*|\*\*Request Body\*\*"),
    ("Kết quả kỳ vọng", r"\*\*Kết quả kỳ vọng\*\*"),
    ("Trạng thái", r"\*\*Trạng thái kiểm thử\*\*|\*\*Trạng thái\*\*|\*\*Kết luận\*\*")
]

valid_count = 0
for idx, case in enumerate(tc_cases, 1):
    header = case.splitlines()[0]
    tc_code_match = re.search(r"TC-[A-Z0-9_\-]+", header)
    tc_code = tc_code_match.group(0) if tc_code_match else f"CASE-{idx}"
    
    missing = []
    for fname, fpat in fields:
        if not re.search(fpat, case, re.IGNORECASE):
            missing.append(fname)
            
    if missing:
        print(f"  [WARN] {tc_code}: missing {missing}")
    else:
        valid_count += 1

print(f"\nResult: {valid_count} / {len(tc_cases)} Test Cases have 100% complete fields!")
