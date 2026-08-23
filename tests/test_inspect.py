import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_file(filepath):
    print(f"=== Inspecting {filepath} ===")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.splitlines()
    print(f"Total lines: {len(lines)}")
    print(f"Total bytes: {len(content.encode('utf-8'))}")
    
    # Check placeholders
    placeholders = []
    placeholder_patterns = [
        r'\bTODO\b',
        r'\bTBD\b',
        r'\bFIXME\b',
        r'/\*\s*rest of code\s*\*/',
        r'//\s*tương tự',
        r'//\s*giữ nguyên',
        r'\.\.\.',
    ]
    for idx, line in enumerate(lines):
        for pat in placeholder_patterns:
            if re.search(pat, line, re.IGNORECASE):
                placeholders.append((idx + 1, pat, line.strip()))
    
    print(f"Potential placeholder matches: {len(placeholders)}")
    for line_no, pat, text in placeholders[:30]:
        print(f"  Line {line_no} [{pat}]: {text[:100]}")
        
    code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
    print(f"Total code blocks: {len(code_blocks)}")
    for i, (lang, code) in enumerate(code_blocks):
        first_line = code.strip().splitlines()[0] if code.strip() else ""
        print(f"  Block {i+1}: lang='{lang}', lines={len(code.splitlines())}, first_line='{first_line[:60]}'")

if __name__ == "__main__":
    inspect_file(r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md")
    print("\n" + "="*50 + "\n")
    inspect_file(r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md")
