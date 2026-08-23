import os
import sys
from part1 import get_part1
from part2 import get_part2
from part3 import get_part3
from part4 import get_part4

full_content = get_part1() + get_part2() + get_part3() + get_part4()
target_file = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md"

with open(target_file, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Successfully generated {target_file} with {len(full_content)} chars.")
