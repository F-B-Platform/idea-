import os, sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\Idea_DoAn'
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.agents' in dirpath or '.git' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.md'):
            docs.append(os.path.join(dirpath, f))

print("=== VERIFYING ENCODING AND SIZES OF ALL 27 DOCS ===")
corrupted = []
tiny_files = []

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    try:
        with open(doc, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = len(content.splitlines())
        size = len(content.encode('utf-8'))
        if size < 500:
            tiny_files.append((rel_path, size, lines))
    except UnicodeDecodeError as e:
        corrupted.append((rel_path, str(e)))

print(f"Total markdown files checked: {len(docs)}")
print(f"UTF-8 Encoding errors: {len(corrupted)}")
if corrupted:
    for c in corrupted:
        print(f"  CORRUPTED: {c[0]} -> {c[1]}")

print(f"Tiny / Stub files (<500 bytes): {len(tiny_files)}")
if tiny_files:
    for t in tiny_files:
        print(f"  TINY: {t[0]} ({t[1]} bytes, {t[2]} lines)")
