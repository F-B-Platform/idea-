import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\temp_revised_content.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== ALL PARAGRAPHS IN TEMP_REVISED_CONTENT.TXT ===")
for idx, line in enumerate(text.splitlines(), 1):
    if line.strip():
        print(f"[{idx:3d}] {line.strip()}")
