import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# Let's find all test case headings (#### `TC-...` or ### TC-...)
tc_headings = re.findall(r"(#{3,4}\s*[`\*]*(TC-[A-Z0-9_\-]+)[`\*]*\s*:\s*(.+))", text)
print(f"Total Detailed Test Case Sections found: {len(tc_headings)}")

for idx, (full, code, title) in enumerate(tc_headings, 1):
    print(f"{idx:2d}. [{code}] {title.strip()}")

# Check test case structure inside each section
print("\n--- Inspecting each Test Case Section structure ---")
sections = re.split(r"(?=#{3,4}\s*[`\*]*TC-[A-Z0-9_\-]+)", text)
# The first section is preamble
preamble = sections[0]
test_sections = sections[1:]

print(f"Total parsed test sections: {len(test_sections)}")

missing_structure = []
for sec in test_sections:
    lines = sec.strip().splitlines()
    header = lines[0]
    m = re.search(r"TC-[A-Z0-9_\-]+", header)
    tc_code = m.group(0) if m else "UNKNOWN"
    
    # Check fields
    has_purpose = bool(re.search(r"Mục đích|Mục tiêu", sec, re.IGNORECASE))
    has_precond = bool(re.search(r"Tiền điều kiện|Điều kiện tiên quyết", sec, re.IGNORECASE))
    has_steps = bool(re.search(r"Các bước thực hiện|Quy trình thực hiện|Các bước", sec, re.IGNORECASE))
    has_input = bool(re.search(r"Dữ liệu đầu vào|Dữ liệu mẫu|Request|Payload", sec, re.IGNORECASE))
    has_expected = bool(re.search(r"Kết quả kỳ vọng|Expected Result", sec, re.IGNORECASE))
    has_status = bool(re.search(r"Trạng thái|Kết luận|PASS", sec, re.IGNORECASE))
    
    missing = []
    if not has_purpose: missing.append("Mục đích")
    if not has_precond: missing.append("Tiền điều kiện")
    if not has_steps: missing.append("Các bước")
    if not has_input: missing.append("Dữ liệu đầu vào")
    if not has_expected: missing.append("Kết quả kỳ vọng")
    if not has_status: missing.append("Trạng thái")
    
    if missing:
        missing_structure.append((tc_code, missing))

print(f"Test cases with missing fields: {len(missing_structure)}")
if missing_structure:
    for tc, miss in missing_structure:
        print(f"  {tc}: Missing {miss}")
else:
    print("  [PASS] ALL test cases have 100% complete fields (Purpose, Preconditions, Steps, Input Data, Expected Results, Status)!")
