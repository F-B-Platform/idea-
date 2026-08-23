import base64
with open(r'd:\Idea_DoAn\.agents\teamwork_preview_reviewer_m5_1\handoff.md', 'wb') as f:
    f.write(base64.b64decode(sys.argv[1]))
