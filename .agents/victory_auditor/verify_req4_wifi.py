import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\Idea_DoAn'
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.agents' in dirpath or '.git' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.md'):
            docs.append(os.path.join(dirpath, f))

print("=== VERIFYING REQUIREMENT 4: WIFI-LOCKED ATTENDANCE ===")

wifi_attendance = []
bssid_ssid_subnet = []
no_gps_fields = []

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if 'chấm công' in content.lower() and ('wifi' in content.lower() or 'wifi-locked' in content.lower()):
        wifi_attendance.append(rel_path)
        
    if 'bssid' in content.lower() or 'ssid' in content.lower() or 'subnet' in content.lower():
        bssid_ssid_subnet.append(rel_path)

print(f"1. WiFi-locked Attendance: {len(wifi_attendance)} files")
for f in wifi_attendance:
    print(f"  - {f}")

print(f"\n2. BSSID / SSID / Subnet configuration: {len(bssid_ssid_subnet)} files")
for f in bssid_ssid_subnet:
    print(f"  - {f}")

# Check DDL in 02_Thiet_Ke_Database.md
db_spec = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md'
with open(db_spec, 'r', encoding='utf-8') as f:
    db_content = f.read()

has_wifi_ddl = 'client_bssid' in db_content.lower() or 'wifi_bssid' in db_content.lower() or 'client_ssid' in db_content.lower()
has_no_gps = 'latitude' not in db_content.lower() or 'gps' not in db_content.lower()

print(f"\nDatabase DDL Check for Attendances / Branches:")
print(f"  - Has WiFi BSSID/SSID columns: {has_wifi_ddl}")
print(f"  - GPS fields eliminated: {has_no_gps}")
