import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn"

# Target canonical files listed in PROJECT.md
CANONICAL_FILES = [
    r"01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md",
    r"01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md",
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
    r"ROADMAP.md",
    r"DOC_AUDIT_REPORT.md",
    r"PROJECT.md"
]

def check_file_existence():
    print("=== 1. Checking Existence of Canonical Files ===")
    missing = []
    for f in CANONICAL_FILES:
        path = os.path.join(DOCS_DIR, f)
        if not os.path.exists(path):
            missing.append(f)
            print(f"❌ MISSING: {f}")
        else:
            size = os.path.getsize(path)
            print(f"✅ FOUND: {f} ({size} bytes)")
    return missing

def check_deprecated_patterns():
    print("\n=== 2. Checking for Deprecated / Forbidden Patterns ===")
    patterns = [
        (r'\bStaff Mobile App\b', "Staff Mobile App"),
        (r'\bStaff App\b', "Staff App"),
        (r'\bGPS 50m\b', "GPS 50m"),
        (r'\bGPS lock\b', "GPS lock"),
        (r'QR động 30', "QR dong 30s"),
        (r'30s rotating QR', "30s rotating QR"),
        (r'thanh toán sau khi dùng', "thanh toan sau khi dung (dine-in)"),
        (r'khách yêu cầu bill', "khach yeu cau bill (dine-in)")
    ]
    
    findings = []
    for root, dirs, files in os.walk(DOCS_DIR):
        if ".agents" in root or ".git" in root:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DOCS_DIR)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                lines = fp.readlines()
            for idx, line in enumerate(lines, 1):
                for pat, label in patterns:
                    if re.search(pat, line, re.IGNORECASE):
                        # Filter out if it's explicitly explaining deprecation / removal / comparison table
                        clean = line.strip()
                        findings.append((rel, idx, label, clean))
                        
    for rel, idx, label, clean in findings:
        print(f"[{label}] {rel}:{idx} -> {clean[:100]}")
    return findings

def check_five_core_rules():
    print("\n=== 3. Checking Coverage of 5 Core Business Changes ===")
    checks = {
        "1. Dine-in VietQR Pre-payment": [
            r"PendingPayment", r"VietQR", r"thanh toán trước", r"SignalR"
        ],
        "2. QR Delivery (20k fee + Address + Upfront VietQR)": [
            r"Delivery", r"20\.000", r"delivery_address", r"delivery_fee", r"không COD|No COD|không tiền mặt"
        ],
        "3. Takeaway Staff POS (No QR + Phone CRM + 10 cups loyalty + Post-pay)": [
            r"TakeAway|Takeaway", r"10 ly", r"CRM", r"tiền mặt|VietQR"
        ],
        "4. WiFi-locked Attendance (BSSID / Subnet + Employee ID)": [
            r"WiFi|Wifi", r"BSSID", r"Subnet", r"Mã NV|EmployeeCode"
        ],
        "5. Staff App Deprecation & Web Portal Consolidation": [
            r"Web KDS|KDS", r"Web Counter POS|Counter POS|Staff Portal", r"PWA"
        ]
    }
    
    for rule_name, pats in checks.items():
        print(f"\nRule: {rule_name}")
        matching_files = set()
        for f in CANONICAL_FILES:
            path = os.path.join(DOCS_DIR, f)
            if not os.path.exists(path):
                continue
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            # check how many patterns match
            matched = [p for p in pats if re.search(p, content, re.IGNORECASE)]
            if len(matched) >= len(pats) // 2 + 1:
                matching_files.add(f)
        print(f"  Matches in {len(matching_files)}/{len(CANONICAL_FILES)} canonical files:")
        for mf in sorted(matching_files):
            print(f"    - {mf}")

def check_scale_up():
    print("\n=== 4. Checking Scale Up / Future Work Preservation ===")
    scale_up_keywords = [
        "AI-3", "AI-4", "AI-5", "NLQ", "Churn", "Demand", "Ahamove", "GrabExpress"
    ]
    for kw in scale_up_keywords:
        found_in = []
        for f in CANONICAL_FILES:
            path = os.path.join(DOCS_DIR, f)
            if not os.path.exists(path):
                continue
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            if kw in content:
                found_in.append(f)
        print(f"Keyword '{kw}': found in {len(found_in)} files -> {found_in[:5]}")

if __name__ == "__main__":
    check_file_existence()
    check_deprecated_patterns()
    check_five_core_rules()
    check_scale_up()
