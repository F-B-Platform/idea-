import base64, os, sys
if len(sys.argv) >= 3:
    target = sys.argv[1]
    b64_data = sys.argv[2]
    os.makedirs(os.path.dirname(target), exist_ok=True)
    raw = base64.b64decode(b64_data)
    with open(target, 'ab') as f:
        f.write(raw)
    print(f'Appended {len(raw)} bytes to {target}, total: {os.path.getsize(target)}')
