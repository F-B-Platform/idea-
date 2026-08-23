# generate_all.py - Assembles and outputs the complete Seed_Data_&_Database_Script.md
import os
import sys

# Add current directory to path
sys.path.append(r"d:\Idea_DoAn\.agents\worker_db_script")

from doc_sections_part1 import get_part1
from doc_sections_part2 import get_part2
from doc_sections_part3 import get_part3
from doc_sections_part4 import get_part4

def main():
    target_path = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
    
    print(f"Generating content for {target_path}...")
    part1 = get_part1()
    part2 = get_part2()
    part3 = get_part3()
    part4 = get_part4()
    
    full_content = "\n".join([part1, part2, part3, part4])
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_content)
        
    print(f"Successfully generated {target_path}!")
    print(f"Total characters: {len(full_content)}")
    print(f"Total lines: {len(full_content.splitlines())}")

if __name__ == "__main__":
    main()
