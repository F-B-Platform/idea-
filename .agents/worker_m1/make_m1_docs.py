# Master M1 Documentation Overhaul Generator
import os

BASE_DIR = r'd:\Idea_DoAn_Tai_Lieu_Dac_Ta_Goc'
os.makedirs(BASE_DIR, exist_ok=True)

def write_doc(filename, content):
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'Done: {filename} -> {len(content)} chars')
