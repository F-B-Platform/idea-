# UAT Builder
import os

parts = []
def add(text):
    parts.append(text)

def build():
    content = '\n'.join(parts)
    target = r'd:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md'
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully built {target}, size: {len(content)} bytes')
