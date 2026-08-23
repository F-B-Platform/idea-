import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE 08_Trien_Khai_He_Thong.md ===")

# Check Docker Compose services
services = re.findall(r"(?:services:\s*\n)((?:\s+[a-zA-Z0-9_-]+:\n)+)", content)
print("Docker Compose services found:")
dc_services = re.findall(r"^\s{2}([a-zA-Z0-9_-]+):\s*$", content, re.MULTILINE)
for s in dc_services:
    print(f"  - Service: {s}")

# Check NGINX SSL config
has_nginx_ssl = bool(re.search(r"ssl_certificate", content)) and bool(re.search(r"ssl_certificate_key", content))
print(f"NGINX SSL certificates configured: {has_nginx_ssl}")

# Check SignalR WebSocket proxy in NGINX
has_ws_proxy = bool(re.search(r"Upgrade\s+\$http_upgrade", content))
print(f"SignalR WebSocket upgrade proxy configured in NGINX: {has_ws_proxy}")

# Check GitHub Actions CI/CD
has_gha = bool(re.search(r"name:\s*CI/CD\s+Pipeline|actions/checkout", content))
print(f"GitHub Actions CI/CD pipeline defined: {has_gha}")

# Check Backup script
has_backup = bool(re.search(r"pg_dump", content))
print(f"PostgreSQL pg_dump automated backup script present: {has_backup}")
