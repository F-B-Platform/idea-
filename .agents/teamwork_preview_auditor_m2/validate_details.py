# -*- coding: utf-8 -*-
import sys
import os
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

api_file = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md'
ui_file = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md'

with open(api_file, 'r', encoding='utf-8') as f:
    api_text = f.read()

with open(ui_file, 'r', encoding='utf-8') as f:
    ui_text = f.read()

print("=" * 80)
print("IN-DEPTH FORENSIC VALIDATION: JSON & MERMAID & FEATURE MAPPING")
print("=" * 80)

# Check JSON code blocks
print("\n--- CHECKING JSON CODE BLOCKS IN 03_API ---")
json_blocks = re.findall(r'```json\n([\s\S]*?)```', api_text)
print(f"Found {len(json_blocks)} JSON blocks in 03_API.")
valid_json_count = 0
for idx, b in enumerate(json_blocks):
    # Some json blocks might have trailing comments or pseudo-json if any, let's test parse
    # Strip comments if any
    clean_b = re.sub(r'//.*', '', b)
    try:
        json.loads(clean_b)
        valid_json_count += 1
    except json.JSONDecodeError as e:
        print(f"  JSON Block #{idx+1} decode note: {e}")
        # print snippet
        lines = b.splitlines()[:4]
        print(f"    Snippet: {' '.join(lines)}")

print(f"Valid strict JSON blocks: {valid_json_count} / {len(json_blocks)}")

# Check Mermaid blocks
print("\n--- CHECKING MERMAID BLOCKS ---")
for fname, content in [("03_API", api_text), ("04_UIUX", ui_text)]:
    mermaid_blocks = re.findall(r'```mermaid\n([\s\S]*?)```', content)
    print(f"Found {len(mermaid_blocks)} Mermaid blocks in {fname}.")
    for idx, mb in enumerate(mermaid_blocks):
        mb_type = mb.strip().splitlines()[0] if mb.strip() else "EMPTY"
        print(f"  [{fname}] Mermaid #{idx+1} diagram type: {mb_type}")

# Check 62 feature IDs mapping
print("\n--- CHECKING 62 FEATURE IDS COVERAGE ---")
expected_c = [f"C-{i:02d}" for i in range(1, 21)]
expected_s = [f"S-{i:02d}" for i in range(1, 14)]
expected_m = [f"M-{i:02d}" for i in range(1, 13)]
expected_a = [f"A-{i:02d}" for i in range(1, 18)]

all_expected = expected_c + expected_s + expected_m + expected_a
print(f"Total expected feature IDs: {len(all_expected)}")

combined_text = api_text + "\n" + ui_text

found_features = {}
for feat in all_expected:
    m = re.findall(rf'\b{feat}\b', combined_text)
    found_features[feat] = len(m)

missing_features = [f for f, count in found_features.items() if count == 0]
if missing_features:
    print(f"FAILED: Missing feature references: {missing_features}")
else:
    print(f"PASSED: All 62 core feature IDs referenced in M2 artifacts! Counts summary:")
    print(f"  Customer (C-01~C-20): {sum(found_features[f] for f in expected_c)} total occurrences")
    print(f"  Staff (S-01~S-13):    {sum(found_features[f] for f in expected_s)} total occurrences")
    print(f"  Manager (M-01~M-12):  {sum(found_features[f] for f in expected_m)} total occurrences")
    print(f"  Admin (A-01~A-17):    {sum(found_features[f] for f in expected_a)} total occurrences")

# Check C-23 and C-24
for bad in ["C-23", "C-24"]:
    bad_count = len(re.findall(rf'\b{bad}\b', combined_text))
    if bad_count > 0:
        print(f"VIOLATION: Found {bad_count} references to deleted feature {bad}!")
    else:
        print(f"PASSED: Confirmed 0 references to deleted feature {bad}.")

