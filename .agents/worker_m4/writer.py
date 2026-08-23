import sys, os, base64

def append_to_buffer(b64_str):
    with open(r'd:\Idea_DoAn\.agents\worker_m4\buffer_b64.txt', 'a', encoding='ascii') as f:
        f.write(b64_str + '\n')

def flush_buffer_to_file(dest_path):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(r'd:\Idea_DoAn\.agents\worker_m4\buffer_b64.txt', 'r', encoding='ascii') as f:
        lines = [line.strip() for line in f if line.strip()]
    full_data = bytearray()
    for line in lines:
        full_data.extend(base64.b64decode(line))
    text = full_data.decode('utf-8')
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Wrote {dest_path}, {len(text)} characters, {len(full_data)} bytes.')
    open(r'd:\Idea_DoAn\.agents\worker_m4\buffer_b64.txt', 'w').close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        flush_buffer_to_file(sys.argv[1])
