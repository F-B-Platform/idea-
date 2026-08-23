import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE 07_Ke_Hoach_Kiem_Thu.md ===")

# Check 10 Critical Edge Cases
edge_cases = re.findall(r"###\s+3\.(\d+)\s+Kịch bản\s+\d+:\s+([^\n]+)", content)
print(f"Critical Edge Cases defined ({len(edge_cases)}):")
for num, ec in edge_cases:
    print(f"  Edge Case 3.{num}: {ec}")

# Check 3 Sales channels testing
channels = ["Dine-In", "Delivery", "Takeaway"]
print("\nSales Channels Testing:")
for ch in channels:
    found = ch.lower() in content.lower()
    print(f"  Channel '{ch}': {'PASS' if found else 'FAIL'}")

# Check Testcontainers & WebApplicationFactory
tc_waf = bool(re.search(r"Testcontainers", content)) and bool(re.search(r"WebApplicationFactory", content))
print(f"Testcontainers & WebApplicationFactory present: {tc_waf}")

# Check Load testing tools (k6, SignalR stress)
load_test = bool(re.search(r"k6|NBomber|SignalR|WebSocket", content))
print(f"Load/Stress testing specs present: {load_test}")

# Check RBAC Security Testing
rbac_test = bool(re.search(r"RBAC|4\s+Actor", content))
print(f"RBAC Security testing present: {rbac_test}")
