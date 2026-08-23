import re

target = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md"
with open(target, "r", encoding="utf-8") as f:
  content = f.read()

lines = content.split("\n")
print(f"Total lines: {len(lines)}")
print(f"Total characters: {len(content)}")

c23 = len(re.findall(r"C-23", content))
c24 = len(re.findall(r"C-24", content))
todos = len(re.findall(r"TODO|TBD|/\* rest of code \*/", content))
print(f"Banned count check: C-23={c23}, C-24={c24}, TODO/TBD={todos}")

c_feats = len(re.findall(r"#### C-\d{2}:", content))
s_feats = len(re.findall(r"#### S-\d{2}:", content))
m_feats = len(re.findall(r"#### M-\d{2}:", content))
a_feats = len(re.findall(r"#### A-\d{2}:", content))

print(
    f"Feature counts: Customer={c_feats}/22, Staff={s_feats}/13,"
    f" Manager={m_feats}/12, Admin={a_feats}/17"
)
print(f"Total Core Features: {c_feats + s_feats + m_feats + a_feats}/64")

sections = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for sec in sections:
  pattern = f"PHẦN {sec}"
  found = pattern in content
  status = "FOUND" if found else "MISSING"
  print(f"Section {sec}: {status}")
