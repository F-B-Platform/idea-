import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE 03_Thiet_Ke_API_Contract.md ===")

# Check 10 API Groups headings
groups = re.findall(r"##\s+2\.(\d+)\s+Nhóm\s+\d+:\s+([^\n]+)", content)
print(f"Total API Groups defined: {len(groups)}")
for num, gname in groups:
    print(f"  Group 2.{num}: {gname}")

# Check Endpoints defined in markdown
endpoints = re.findall(r"###\s+2\.\d+\.\d+\s+(?:API\s+)?([^\n]+)", content)
print(f"\nTotal Specific Endpoints Headings: {len(endpoints)}")
for ep in endpoints:
    print(f"  - {ep}")

# Check PayOS Webhook
payos_webhook = bool(re.search(r"payos", content, re.IGNORECASE))
hmac_sha256 = bool(re.search(r"HMAC.*SHA256|SHA256.*HMAC|signature", content, re.IGNORECASE))
print(f"\nPayOS Webhook covered: {payos_webhook}")
print(f"HMAC-SHA256 signature verification covered: {hmac_sha256}")

# Check SignalR Hubs
signalr_hubs = re.findall(r"OrderHub|KitchenHub|PaymentHub|NotificationHub", content)
print(f"SignalR Hubs mentions count: {len(signalr_hubs)} ({set(signalr_hubs)})")
