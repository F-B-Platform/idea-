import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md", "r", encoding="utf-8") as f:
    content = f.read()

matches = re.findall(r"(?:Dine-?In|tại\s+bàn|VietQR|tiền\s+mặt|Cash)", content, re.IGNORECASE)
print(f"Total Dine-In/Payment related mentions in 06_: {len(matches)} -> {set(matches)}")

# Let's search for how Dine-In checkout is implemented in 06_
cart_store = re.search(r"useCartStore", content)
if cart_store:
    print("\n--- SAMPLE useCartStore in 06_ ---")
    print(content[cart_store.start():cart_store.start()+1500])
