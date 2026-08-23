import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"d:\Idea_DoAn"

canonical_files = [
    r"01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md",
    r"01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md",
    r"01_Tai_Lieu_Dac_Ta_Goc\Tom_Tat_1_Trang_Executive_Summary.md",
    r"01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md",
    r"01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md",
    r"02_Bao_Gia_Chi_Phi\Bang_Bao_Gia_Smart_FB_OS.md",
    r"02_Bao_Gia_Chi_Phi\Chi_Phi_Duy_Tri_Hang_Thang.md",
    r"03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md",
    r"03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md",
    r"03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md",
    r"03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md",
    r"03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md",
    r"03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md",
    r"03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md",
    r"03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md",
    r"03_Quy_Trinh_Trien_Khai\README.md",
    r"04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md",
    r"04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md",
    r"04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md",
    r"04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md",
    r"05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md",
    r"05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md",
    r"05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md",
    r"06_Danh_Sach_Skills\README.md",
    r"DOC_AUDIT_REPORT.md",
    r"PROJECT.md",
    r"ROADMAP.md"
]

print("=== 1. VERIFYING CANONICAL FILES INVENTORY ===")
missing_files = []
for rel_path in canonical_files:
    full_path = os.path.join(root_dir, rel_path)
    if not os.path.exists(full_path):
        missing_files.append(rel_path)
        print(f"[MISSING] {rel_path}")
    else:
        size = os.path.getsize(full_path)
        print(f"[OK] {rel_path} ({size:,} bytes)")

if missing_files:
    print(f"FAILED: {len(missing_files)} missing canonical files.")
else:
    print(f"PASSED: All {len(canonical_files)} canonical files present.")

print("\n=== 2. VERIFYING NO UNWANTED / LEGACY MARKDOWN FILES ===")
all_md_files = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath or ".agents" in dirpath:
        continue
    for f in filenames:
        if f.endswith(".md"):
            rel = os.path.relpath(os.path.join(dirpath, f), root_dir)
            all_md_files.append(rel)

unexpected = [f for f in all_md_files if f not in canonical_files]
if unexpected:
    print(f"FAILED: Found unexpected markdown files: {unexpected}")
else:
    print(f"PASSED: Exactly {len(all_md_files)} markdown files in repository (0 unexpected).")

print("\n=== 3. ZERO PLACEHOLDER AUDIT ===")
placeholder_patterns = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\[TBD\]",
    r"/\*\s*rest of code\s*\*/",
    r"//\s*tương tự",
    r"//\s*\.\.\.",
    r"Chưa xác định,\s*sẽ bổ sung"
]
placeholder_violations = 0
for rel in canonical_files:
    full_path = os.path.join(root_dir, rel)
    with open(full_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        for pat in placeholder_patterns:
            if re.search(pat, line, re.IGNORECASE):
                # Check if it's describing the rule "Zero Placeholder" or "TODO" rule
                if "Zero Placeholder" in line or "TODO" in line and ("CẤM" in line or "cấm" in line or "rule" in line or "Convention" in line or "mẫu" in line or "Quy tắc" in line):
                    continue
                print(f"[PLACEHOLDER] {rel}:{idx} -> {line.strip()}")
                placeholder_violations += 1

if placeholder_violations == 0:
    print("PASSED: 0 placeholder violations found across all canonical files.")
else:
    print(f"WARNING/FAILED: Found {placeholder_violations} placeholder occurrences.")

print("\n=== 4. MANDATORY KEYWORDS THRESHOLD AUDIT ===")
mandatory_keywords = [
    ("Delivery", 5),
    ("delivery_address", 5),
    ("phí ship", 5),
    ("20.000", 5),
    ("WiFi", 3),
    ("SSID", 3),
    ("BSSID", 3),
    ("chấm công", 3),
    ("PendingPayment", 3),
    ("10 ly", 3),
    ("loyalty", 3)
]

for kw, threshold in mandatory_keywords:
    matched_files = 0
    total_hits = 0
    for rel in canonical_files:
        full_path = os.path.join(root_dir, rel)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        hits = len(re.findall(re.escape(kw), content, re.IGNORECASE))
        if hits > 0:
            matched_files += 1
            total_hits += hits
    status = "PASS" if matched_files >= threshold else "FAIL"
    print(f"[{status}] Keyword '{kw}': found in {matched_files} files (threshold >= {threshold}), total hits: {total_hits}")

print("\n=== VERIFICATION COMPLETE ===")
