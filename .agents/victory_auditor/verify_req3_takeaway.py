import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\Idea_DoAn'
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.agents' in dirpath or '.git' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.md'):
            docs.append(os.path.join(dirpath, f))

print("=== VERIFYING REQUIREMENT 3: TAKEAWAY STAFF UI & 10 CUPS LOYALTY ===")

takeaway_staff_ui = []
loyalty_10_cups = []
takeaway_postpay = []

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check staff UI for takeaway (no customer QR for takeaway)
    if 'takeaway' in content.lower() and ('giao diện nv' in content.lower() or 'web pos' in content.lower() or 'nhân viên thao tác' in content.lower() or 'thu ngân' in content.lower() or 'không dùng qr' in content.lower() or 'bỏ qr takeaway' in content.lower()):
        takeaway_staff_ui.append(rel_path)
    
    # Check 10 cups = 1 cup loyalty rule
    if '10 ly' in content.lower() or '10 ly tặng 1' in content.lower() or 'tặng 1 ly' in content.lower() or '10_cups' in content.lower() or '10 cups' in content.lower():
        loyalty_10_cups.append(rel_path)
        
    # Check takeaway postpay (cash / vietqr)
    if 'takeaway' in content.lower() and ('thanh toán sau' in content.lower() or 'tiền mặt' in content.lower() or 'tiền thừa' in content.lower() or 'tiền thối' in content.lower()):
        takeaway_postpay.append(rel_path)

print(f"1. Takeaway Staff-Operated UI (No customer QR): {len(takeaway_staff_ui)} files")
for f in takeaway_staff_ui:
    print(f"  - {f}")

print(f"\n2. Loyalty Rule '10 ly = tặng 1 ly miễn phí': {len(loyalty_10_cups)} files")
for f in loyalty_10_cups:
    print(f"  - {f}")

print(f"\n3. Takeaway Post-Payment (Cash/VietQR): {len(takeaway_postpay)} files")
for f in takeaway_postpay:
    print(f"  - {f}")
