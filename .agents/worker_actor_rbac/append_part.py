import sys, base64
target = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md'
mode = sys.argv[1]
b64_data = sys.argv[2]
bytes_data = base64.b64decode(b64_data)
with open(target, mode, encoding='utf-8') as f:
    f.write(bytes_data.decode('utf-8'))
print('Appended bytes:', len(bytes_data))
