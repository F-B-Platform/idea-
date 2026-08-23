import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE 05_Quy_Trinh_Backend.md ===")

# Check C# files / classes defined
cs_classes = re.findall(r"(?:public\s+(?:class|record|interface|enum)\s+([a-zA-Z0-9_]+))", content)
print(f"Total C# Types (classes, records, interfaces, enums) defined: {len(cs_classes)}")
print("Sample C# Types:")
for c in cs_classes[:25]:
    print("  -", c)

# Check specific key classes
key_classes = [
    "CreateOrderCommandHandler",
    "PayOsWebhookCommandHandler",
    "WifiAttendanceCommandHandler",
    "CloseCashShiftCommandHandler",
    "GeminiAdvisorService",
    "AprioriEngine",
    "OrderHub",
    "KitchenHub",
    "PaymentHub",
    "NotificationHub",
    "MonthlyAprioriWorker",
    "OrderTimeoutWorker"
]
print("\nKey Classes Presence:")
for kc in key_classes:
    print(f"  {kc}: {'PASS' if kc in content else 'FAIL'}")
