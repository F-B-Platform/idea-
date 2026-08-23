import sys, base64
b64_str = sys.argv[1]
with open(r'd:\Idea_DoAn\.agents\worker_actor_rbac\generator.py', 'a', encoding='utf-8') as f:
    f.write(f'base64_chunk = {repr(b64_str)}\nout.append(base64.b64decode(base64_chunk).decode("utf-8"))\n\n')
print('Added chunk len:', len(b64_str))
