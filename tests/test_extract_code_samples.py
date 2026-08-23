import os
import re
import sys
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"

def extract_code_blocks():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
    print(f"Total code blocks in Git Workflow: {len(code_blocks)}")
    
    categorized = defaultdict(list)
    for lang, code in code_blocks:
        categorized[lang.lower()].append(code)
        
    for lang, list_codes in categorized.items():
        print(f"  - Lang '{lang}': {len(list_codes)} blocks")
        
    return categorized

from collections import defaultdict

if __name__ == "__main__":
    extract_code_blocks()
