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

print("=== VERIFYING REQUIREMENT 2: QR DELIVERY ===")

checks = {
    'delivery_address': [],
    '20.000': [],
    'no_cod': [],
    'ordertype_enum': [],
}

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if 'delivery_address' in content.lower() or 'địa chỉ giao hàng' in content.lower():
        checks['delivery_address'].append(rel_path)
    if '20.000' in content or '20,000' in content or '20000' in content:
        checks['20.000'].append(rel_path)
    if 'không' in content.lower() and ('cod' in content.lower() or 'tiền mặt khi nhận' in content.lower()):
        checks['no_cod'].append(rel_path)
    if 'ordertype' in content or 'order_type' in content or ('dinein' in content and 'takeaway' in content and 'delivery' in content):
        checks['ordertype_enum'].append(rel_path)

print(f"1. delivery_address / Địa chỉ giao hàng: {len(checks['delivery_address'])} files")
print(f"2. 20.000 VNĐ flat shipping fee: {len(checks['20.000'])} files")
print(f"3. No COD (100% VietQR Prepayment): {len(checks['no_cod'])} files")
print(f"4. OrderType Enum (DineIn, TakeAway, Delivery): {len(checks['ordertype_enum'])} files")

# Verify ERD DDL in Database spec & ERD diagram
db_spec = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md'
with open(db_spec, 'r', encoding='utf-8') as f:
    db_content = f.read()

has_ddl_delivery_address = 'delivery_address' in db_content
has_ddl_delivery_fee = 'delivery_fee' in db_content
has_ddl_enum = 'order_type' in db_content or 'ordertype' in db_content

print(f"\nDatabase DDL Check (02_Thiet_Ke_Database.md):")
print(f"  - Has delivery_address: {has_ddl_delivery_address}")
print(f"  - Has delivery_fee: {has_ddl_delivery_fee}")
print(f"  - Has OrderType enum: {has_ddl_enum}")
