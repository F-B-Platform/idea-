import sys, base64
target = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md'
mode = sys.argv[1]
b64_str = sys.argv[2]
data = base64.b64decode(b64_str).decode('utf-8')
with open(target, mode, encoding='utf-8') as f:
    f.write(data)
print(f'Done {mode}: {len(data)} chars')
