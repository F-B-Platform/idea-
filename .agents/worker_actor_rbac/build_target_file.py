# -*- coding: utf-8 -*-
import os

target = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md'
chunks = []

def add(text):
    chunks.append(text)

def finish():
    with open(target, 'w', encoding='utf-8') as f:
        f.write(''.join(chunks))
    print(f'Successfully written {len(chunks)} chunks to {target}')
