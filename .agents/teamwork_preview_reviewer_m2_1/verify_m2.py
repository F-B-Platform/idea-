import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

api_file = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md'
uiux_file = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md'

with open(api_file, 'r', encoding='utf-8') as f:
    api_text = f.read()

with open(uiux_file, 'r', encoding='utf-8') as f:
    uiux_text = f.read()

print("==================================================")
print("1. CHECKING 62 CORE FEATURES COVERAGE (RTM)")
print("==================================================")

expected_features = []
for i in range(1, 21):
    expected_features.append(f"C-{i:02d}")
for i in range(1, 14):
    expected_features.append(f"S-{i:02d}")
for i in range(1, 13):
    expected_features.append(f"M-{i:02d}")
for i in range(1, 18):
    expected_features.append(f"A-{i:02d}")

print(f"Total expected features: {len(expected_features)} (20 C, 13 S, 12 M, 17 A)")

missing_api = [f for f in expected_features if f not in api_text]
missing_uiux = [f for f in expected_features if f not in uiux_text]

print(f"Missing in API Contract ({len(missing_api)}): {missing_api}")
print(f"Missing in UI/UX Design ({len(missing_uiux)}): {missing_uiux}")

print("\n==================================================")
print("2. CHECKING 10 RESTful API GROUPS")
print("==================================================")
api_groups = [
    "Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4", "Nhóm 5",
    "Nhóm 6", "Nhóm 7", "Nhóm 8", "Nhóm 9", "Nhóm 10"
]
for g in api_groups:
    found = g in api_text
    print(f"  {g}: {'FOUND' if found else 'MISSING'}")

print("\n==================================================")
print("3. CHECKING 4 SIGNALR HUBS & REDIS BACKPLANE")
print("==================================================")
hubs = [
    "/hubs/orders", "OrderHub",
    "/hubs/kitchen", "KitchenHub",
    "/hubs/payments", "PaymentHub",
    "/hubs/notifications", "NotificationHub",
    "Redis Backplane"
]
for h in hubs:
    found = h in api_text
    print(f"  {h}: {'FOUND' if found else 'MISSING'}")

print("\n==================================================")
print("4. CHECKING PAYOS WEBHOOK HMAC-SHA256 & REDIS LOCK")
print("==================================================")
security_items = [
    "HMAC-SHA256", "X-Webhook-Signature", "FixedTimeEquals",
    "lock:webhook:payos:", "Idempotency", "webhook"
]
for s in security_items:
    found = s.lower() in api_text.lower()
    print(f"  {s}: {'FOUND' if found else 'MISSING'}")

print("\n==================================================")
print("5. CHECKING 5 ROUTE GROUPS IN UI/UX")
print("==================================================")
route_groups = [
    "(customer)", "(kds)", "(staff)", "(manager)", "(admin)"
]
for r in route_groups:
    found = r in uiux_text
    print(f"  {r}: {'FOUND' if found else 'MISSING'}")

print("\n==================================================")
print("6. CHECKING MERMAID SYNTAX BLOCKS")
print("==================================================")
def test_mermaid_blocks(filename, text):
    pattern = r'```mermaid\s*\n(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    print(f"File {filename}: found {len(matches)} diagrams")
    for idx, code in enumerate(matches, 1):
        lines = code.strip().splitlines()
        dtype = lines[0].strip()
        print(f"  Diagram #{idx}: Type={dtype}, Lines={len(lines)}")
        # Check matching quotes and syntax keywords
        for l_num, line in enumerate(lines, 1):
            if line.count('"') % 2 != 0:
                print(f"    [SYNTAX WARN] Line {l_num}: unmatched double quotes -> {line}")

test_mermaid_blocks("03_Thiet_Ke_API_Contract.md", api_text)
test_mermaid_blocks("04_Thiet_Ke_UI_UX.md", uiux_text)

