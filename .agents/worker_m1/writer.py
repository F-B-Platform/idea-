# Master Writer for Worker M1
import os

BASE_DIR = r'd:\Idea_DoAn_Tai_Lieu_Dac_Ta_Goc'
os.makedirs(BASE_DIR, exist_ok=True)

def save_doc(filename, hex_content):
    data = bytes.fromhex(hex_content)
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'wb') as f:
        f.write(data)
    print(f'Successfully saved {filename} ({len(data)} bytes)')
