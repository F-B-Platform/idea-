import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

uat_file = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md"
wf_file = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md"
actor_file = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md"

with open(uat_file, "r", encoding="utf-8") as f:
    uat_content = f.read()

with open(wf_file, "r", encoding="utf-8") as f:
    wf_content = f.read()

with open(actor_file, "r", encoding="utf-8") as f:
    actor_content = f.read()

# Extract workflows from wf_file
# Workflows typically marked as WF-01 to WF-16 or Quy trình 1..16
wf_list = re.findall(r"(WF-\d+|Quy trình \d+:[^\n]+|### \d+\.\d+\s+[^\n]+)", wf_content)
print(f"Sample workflow patterns extracted from {wf_file}: {len(wf_list)}")

# Extract Actors from actor_file
actors = ["Khách hàng", "Nhân viên", "Quản lý", "Admin", "Customer", "Staff", "Manager", "Barista", "Cashier"]
for act in actors:
    count = len(re.findall(r"\b" + act + r"\b", uat_content, re.IGNORECASE))
    print(f"Actor mention in UAT: '{act}' -> {count} occurrences")

# Key business concepts check in UAT
key_concepts = [
    ("Dine-In Branch A (VietQR Prepay)", "TC-DINE-01A"),
    ("Dine-In Branch B (Cash Postpay)", "TC-DINE-01B"),
    ("Delivery 20k Fee", "20.000"),
    ("Takeaway Loyalty 10 Cups", "10 ly"),
    ("WiFi Attendance", "BSSID"),
    ("KDS BOM Deduction (g/ml)", "gam"),
    ("86-Toggle & Undo 10s", "86-Toggle"),
    ("Cash Drawer & Z-Report Reconcile > 50k", "50.000"),
    ("AI-2 Combo Apriori Approval", "Apriori"),
    ("Regional Price Book", "bảng giá"),
    ("Seasonal Menu", "theo mùa"),
    ("RedLock Concurrency", "RedLock"),
    ("PayOS Idempotency Key", "Idempotency"),
    ("Circuit Breaker Fallback", "Circuit Breaker")
]

print("\n--- Key Business & Architectural Concepts Check in UAT ---")
for name, kw in key_concepts:
    found = kw.lower() in uat_content.lower()
    print(f"  [{'PASS' if found else 'FAIL'}] {name}: keyword '{kw}'")
