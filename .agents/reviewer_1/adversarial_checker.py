import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def run_adversarial_checks():
    print("================================================================================")
    print("                        ADVERSARIAL STRESS TEST CHECKS                          ")
    print("================================================================================")

    # 1. Order Status Consistency
    print("\n--- Check 1: Order Status Enum Consistency ---")
    files_with_status = [
        "01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md",
        "01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md",
        "03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md",
        "03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md",
        "03_Quy_Trinh_Trien_Khai/05_Quy_Trinh_Backend.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md",
        "05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md",
        "05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md"
    ]
    for rel in files_with_status:
        path = os.path.join(DOCS_DIR, rel.replace("/", os.sep))
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            c = fp.read()
        statuses = re.findall(r"(?:PendingPayment|Pending_Payment|Paid|Confirmed|Preparing|Ready|Completed|Cancelled|Served)", c)
        unique_statuses = sorted(list(set(statuses)))
        print(f"  {rel:55} -> {unique_statuses}")

    # 2. Endpoints Check
    print("\n--- Check 2: API Endpoints Contract Coverage ---")
    p_api = os.path.join(DOCS_DIR, "03_Quy_Trinh_Trien_Khai", "03_Thiet_Ke_API_Contract.md")
    with open(p_api, "r", encoding="utf-8", errors="ignore") as fp:
        c_api = fp.read()
    endpoints = re.findall(r"(?:GET|POST|PUT|DELETE|PATCH)\s+`?(/api/v1/[a-zA-Z0-9_\-\/{}\?&=]+)`?", c_api)
    print(f"Total API Endpoints documented in 03_Thiet_Ke_API_Contract.md: {len(endpoints)}")
    for ep in endpoints:
        print(f"  - {ep}")

    # 3. Database Tables Count & Schema Check
    print("\n--- Check 3: Database Tables Count in Schema ---")
    p_erd = os.path.join(DOCS_DIR, "03_Quy_Trinh_Trien_Khai", "02_Thiet_Ke_Database.md")
    with open(p_erd, "r", encoding="utf-8", errors="ignore") as fp:
        c_erd = fp.read()
    tables = re.findall(r"CREATE TABLE (?:IF NOT EXISTS )?([a-zA-Z0-9_]+)", c_erd, re.IGNORECASE)
    print(f"Total tables created in 02_Thiet_Ke_Database.md: {len(tables)} -> {tables}")

    p_seed = os.path.join(DOCS_DIR, "05_Quy_Chuan_&_Test_Cases", "Seed_Data_&_Database_Script.md")
    with open(p_seed, "r", encoding="utf-8", errors="ignore") as fp:
        c_seed = fp.read()
    tables_seed = re.findall(r"CREATE TABLE (?:IF NOT EXISTS )?([a-zA-Z0-9_]+)", c_seed, re.IGNORECASE)
    print(f"Total tables created in Seed_Data_&_Database_Script.md: {len(tables_seed)} -> {tables_seed}")

    # 4. Check Workflows count
    print("\n--- Check 4: Workflows in 01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md ---")
    p_wf = os.path.join(DOCS_DIR, "01_Tai_Lieu_Dac_Ta_Goc", "Workflow_Quy_Trinh_Nghiep_Vu.md")
    with open(p_wf, "r", encoding="utf-8", errors="ignore") as fp:
        c_wf = fp.read()
    wfs = re.findall(r"##\s*🔄\s*(WF-\d+:\s*[^\n]+)", c_wf)
    print(f"Total Workflows documented: {len(wfs)}")
    for wf in wfs:
        print(f"  - {wf}")

    # 5. Check AI Modules division
    print("\n--- Check 5: AI Modules Division Check ---")
    ai_checks = {}
    for rel in CANONICAL_FILES:
        path = os.path.join(DOCS_DIR, rel.replace("/", os.sep))
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
        ai1 = "AI-1" in content
        ai2 = "AI-2" in content
        ai3 = "AI-3" in content
        ai4 = "AI-4" in content
        ai5 = "AI-5" in content
        ai_checks[rel] = (ai1, ai2, ai3, ai4, ai5)
    print("Files mentioning AI modules:")
    for f, (a1, a2, a3, a4, a5) in ai_checks.items():
        if any([a1, a2, a3, a4, a5]):
            print(f"  {f:50} -> AI-1:{a1}, AI-2:{a2}, AI-3:{a3}, AI-4:{a4}, AI-5:{a5}")

if __name__ == "__main__":
    from deep_audit import CANONICAL_FILES
    run_adversarial_checks()
