import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_db_schema():
    with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md", "r", encoding="utf-8") as f:
        content = f.read()

    print("=== INSPECTING DATABASE SCHEMA ===")
    tables = re.findall(r"###\s+\d+\.\s+Bảng\s+`?([a-zA-Z0-9_]+)`?", content)
    print(f"Tables listed in headings ({len(tables)}):")
    for idx, t in enumerate(tables, 1):
        print(f"  {idx}. {t}")

    # Check relationships, indexes, constraints
    foreign_keys = re.findall(r"REFERENCES\s+`?([a-zA-Z0-9_]+)`?", content, re.IGNORECASE)
    indexes = re.findall(r"CREATE\s+(?:UNIQUE\s+)?INDEX\s+([a-zA-Z0-9_]+)", content, re.IGNORECASE)
    print(f"\nTotal Foreign Key references: {len(foreign_keys)}")
    print(f"Total Indexes explicitly defined: {len(indexes)}")

def inspect_api_groups():
    with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md", "r", encoding="utf-8") as f:
        content = f.read()

    print("\n=== INSPECTING API GROUPS ===")
    groups = re.findall(r"##\s+(?:Nhóm|Phần)\s+\d+[:\.]\s+(.+)", content)
    for g in groups:
        print(f"  - {g.strip()}")

    # Find endpoints
    endpoints = re.findall(r"(GET|POST|PUT|DELETE|PATCH)\s+`(/api/v1/[^`]+)`", content)
    print(f"\nTotal Endpoints defined: {len(endpoints)}")
    for m, ep in endpoints[:15]:
        print(f"  [{m}] {ep}")
    if len(endpoints) > 15:
        print(f"  ... and {len(endpoints) - 15} more endpoints.")

def inspect_test_suite():
    with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md", "r", encoding="utf-8") as f:
        content = f.read()

    print("\n=== INSPECTING TESTING PLAN (07_) ===")
    sections = re.findall(r"##\s+\d+[\.:]\s+(.+)", content)
    for s in sections:
        print(f"  - {s.strip()}")

    # Search for UAT, E2E, Integration, Unit
    print("Test types found:")
    for term in ["Unit", "Integration", "E2E", "UAT", "Acceptance", "Pyramid", "Chấp nhận"]:
        matches = re.findall(rf"\b{term}\b", content, re.IGNORECASE)
        print(f"  Term '{term}': {len(matches)} occurrences")

def inspect_devops():
    with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md", "r", encoding="utf-8") as f:
        content = f.read()

    print("\n=== INSPECTING DEVOPS (08_) ===")
    sections = re.findall(r"##\s+\d+[\.:]\s+(.+)", content)
    for s in sections:
        print(f"  - {s.strip()}")

inspect_db_schema()
inspect_api_groups()
inspect_test_suite()
inspect_devops()
