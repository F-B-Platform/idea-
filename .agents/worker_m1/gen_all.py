# Master Generator for 01_Tai_Lieu_Dac_Ta_Goc
import os

OUT_DIR = r'd:\Idea_DoAn_Tai_Lieu_Dac_Ta_Goc'
os.makedirs(OUT_DIR, exist_ok=True)

def save(name, content):
    p = os.path.join(OUT_DIR, name)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'[OK] {name}: {len(content)} chars, {os.path.getsize(p)} bytes')
