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

print("=== VERIFYING REQUIREMENT 5: STAFF MOBILE APP REMOVAL ===")

# Check if any file treats Staff Mobile App as an active deliverable or component
violations = []
for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check for active references (not in removal / scale-up contexts)
    matches = re.finditer(r'(staff\s+mobile\s+app|staff\s+app|ứng\s+dụng\s+nhân\s+viên)', content, re.IGNORECASE)
    for m in matches:
        snippet = content[max(0, m.start()-80):min(len(content), m.end()+80)].replace('\n', ' ')
        # If snippet contains removal explanation or scale-up, it's valid
        is_removal_note = any(w in snippet.lower() for w in ['loại bỏ', 'bỏ', 'xóa', 'thay thế', 'không dùng', 'hợp nhất', 'web portal', 'scale up', 'future work', 'chuyển sang'])
        if not is_removal_note:
            violations.append((rel_path, m.group(0), snippet))

print(f"Active Staff App violations found: {len(violations)}")
for v in violations:
    print(f"  VIOLATION in {v[0]}: {v[1]}")
    print(f"    Context: {v[2]}")

# Check that Web Staff / KDS exists
web_staff_files = []
for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if 'kds' in content.lower() or 'staff portal' in content.lower() or 'web pos' in content.lower() or 'giao diện nhân viên' in content.lower():
        web_staff_files.append(rel_path)

print(f"\nWeb Staff/KDS integration documented across {len(web_staff_files)} files.")
