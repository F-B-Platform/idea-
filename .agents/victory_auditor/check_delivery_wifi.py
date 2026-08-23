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

# Check Delivery in files
delivery_files = set()
for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if 'delivery_address' in content.lower() or '20.000' in content or '20,000' in content or ('delivery' in content.lower() and 'phí ship' in content.lower()):
        delivery_files.add(rel_path)

print(f'=== Delivery Keywords found in {len(delivery_files)} files (Requirement: >= 5 files) ===')
for f in sorted(delivery_files):
    print(f'  - {f}')

# Check WiFi in files
wifi_files = set()
for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if 'wifi' in content.lower() and ('ssid' in content.lower() or 'bssid' in content.lower()) and 'chấm công' in content.lower():
        wifi_files.add(rel_path)

print(f'\n=== WiFi Keywords found in {len(wifi_files)} files (Requirement: >= 3 files) ===')
for f in sorted(wifi_files):
    print(f'  - {f}')
