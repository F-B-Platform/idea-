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

print("=== VERIFYING REQUIREMENT 1: DINE-IN PRE-PAYMENT ===")
dine_in_checks = []

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check for Dine-in keywords
    has_dinein = 'dine-in' in content.lower() or 'dinein' in content.lower() or 'tại bàn' in content.lower() or 'qr bàn' in content.lower()
    has_prepay = 'trả trước' in content.lower() or 'pre-payment' in content.lower() or 'prepayment' in content.lower() or 'thanh toán trước' in content.lower() or 'pendingpayment' in content.lower()
    
    # Check order status sequence
    has_status_flow = 'pendingpayment' in content.lower() and 'preparing' in content.lower() and ('ready' in content.lower() or 'served' in content.lower())
    
    if has_dinein and has_prepay:
        dine_in_checks.append((rel_path, True, has_status_flow))

print(f"Dine-in pre-payment documented across {len(dine_in_checks)} files:")
for f, prepay, flow in dine_in_checks:
    print(f"  - {f} (Status flow included: {flow})")

# Verify NO Dine-in workflow contains post-payment or bill request
bad_dinein_patterns = [
    r'dine[- ]in.*?thanh toán sau',
    r'tại bàn.*?thanh toán sau',
    r'quét qr bàn.*?thanh toán sau',
    r'dine[- ]in.*?yêu cầu bill',
    r'tại bàn.*?yêu cầu bill',
]

violations = []
for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for p in bad_dinein_patterns:
        matches = re.finditer(p, content, re.IGNORECASE)
        for m in matches:
            # Check context to see if it's describing the eliminated legacy flow
            snippet = content[max(0, m.start()-50):min(len(content), m.end()+50)]
            if 'loại bỏ' in snippet.lower() or 'xóa' in snippet.lower() or 'cũ' in snippet.lower() or 'thay vì' in snippet.lower():
                continue
            violations.append((rel_path, m.group(0), snippet))

print(f"\nDine-in post-pay violations: {len(violations)}")
for v in violations:
    print(f"  VIOLATION in {v[0]}: {v[1]}")
    print(f"    Context: {v[2]}")
