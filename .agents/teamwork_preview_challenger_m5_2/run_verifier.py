import os
import sys
import json
import re
import subprocess
import yaml

DOCS_DIR = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai'
AGENT_DIR = 'd:/Idea_DoAn/.agents/teamwork_preview_challenger_m5_2'

FILES = [
    '01_Phan_Tich_Yeu_Cau.md',
    '02_Thiet_Ke_Database.md',
    '03_Thiet_Ke_API_Contract.md',
    '04_Thiet_Ke_UI_UX.md',
    '05_Quy_Trinh_Backend.md',
    '06_Quy_Trinh_Frontend.md',
    '07_Ke_Hoach_Kiem_Thu.md',
    '08_Trien_Khai_He_Thong.md',
    'README.md'
]

print('Files to check:', len(FILES))
