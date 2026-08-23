import os
BASE_DIR = 'd:/Idea_DoAn/01_Tai_Lieu_Dac_Ta_Goc'
def append_hex(filename, hex_str):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'ab') as f:
        f.write(bytes.fromhex(hex_str))
def clear_doc(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'wb') as f:
        pass
