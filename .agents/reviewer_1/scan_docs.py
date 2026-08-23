import os
import sys
import re
import glob

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn"

def scan_markdown_files():
    md_files = []
    for root, dirs, files in os.walk(DOCS_DIR):
        if ".agents" in root or ".git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))
    return md_files

def check_placeholders(files):
    placeholder_patterns = [
        (r'\bTODO\b', "TODO"),
        (r'\bTBD\b', "TBD"),
        (r'\bTBA\b', "TBA"),
        (r'\/\*\s*rest of code\s*\*\/', "rest of code"),
        (r'\/\/\s*rest of', "rest of code"),
        (r'\[chưa có\]', "chua co"),
        (r'\[đang cập nhật\]', "dang cap nhat"),
        (r'\[placeholder\]', "placeholder")
    ]
    results = {}
    for f in files:
        rel = os.path.relpath(f, DOCS_DIR)
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            lines = fp.readlines()
        findings = []
        for idx, line in enumerate(lines, 1):
            for pat, label in placeholder_patterns:
                if re.search(pat, line, re.IGNORECASE):
                    # check if it's an explanation like "không có TODO" or "Zero TODO"
                    clean_line = line.strip()
                    findings.append((idx, label, clean_line))
        if findings:
            results[rel] = findings
    return results

if __name__ == "__main__":
    files = scan_markdown_files()
    print(f"Total markdown files scanned (excluding .agents): {len(files)}")
    placeholders = check_placeholders(files)
    if not placeholders:
        print("NO PLACEHOLDERS FOUND!")
    else:
        for f, items in placeholders.items():
            print(f"\nFile: {f}")
            for line_no, label, content in items:
                print(f"  Line {line_no} [{label}]: {content[:100]}")
