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

print("=== VERIFYING SCALE UP / FUTURE WORK & AI MODULES ===")

ai1_files = []
ai2_files = []
future_ai_files = []
scaleup_files = []

for doc in docs:
    rel_path = os.path.relpath(doc, root_dir)
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if 'ai-1' in content.lower() or 'rag' in content.lower() or 'chatbot' in content.lower() or 'gợi ý món' in content.lower():
        ai1_files.append(rel_path)
    if 'ai-2' in content.lower() or 'apriori' in content.lower() or 'combo' in content.lower():
        ai2_files.append(rel_path)
    if 'ai-3' in content.lower() or 'ai-4' in content.lower() or 'ai-5' in content.lower() or 'dự báo nhu cầu' in content.lower():
        future_ai_files.append(rel_path)
    if 'scale up' in content.lower() or 'future work' in content.lower() or 'mở rộng' in content.lower():
        scaleup_files.append(rel_path)

print(f"1. AI-1 (Chatbot / RAG / MVP): {len(ai1_files)} files")
print(f"2. AI-2 (Combo Recommender / Apriori / MVP): {len(ai2_files)} files")
print(f"3. AI-3 / AI-4 / AI-5 (Future Work): {len(future_ai_files)} files")
print(f"4. Scale Up / Future Work sections: {len(scaleup_files)} files")

print("\n=== VERIFYING ROADMAP 16 WEEKS ===")
with open(r'd:\Idea_DoAn\ROADMAP.md', 'r', encoding='utf-8') as f:
    roadmap_content = f.read()

has_16_weeks = '16 tuần' in roadmap_content or '16 weeks' in roadmap_content
sprints = re.findall(r'Sprint\s+\d+|Tuần\s+\d+', roadmap_content, re.IGNORECASE)
print(f"  - Mentions 16 weeks: {has_16_weeks}")
print(f"  - Sprints / Weeks found: {len(sprints)} occurrences")

print("\n=== VERIFYING SEED DATA ===")
with open(r'd:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md', 'r', encoding='utf-8') as f:
    seed_content = f.read()

has_dinein_seed = 'DINE_IN' in seed_content or 'DineIn' in seed_content
has_takeaway_seed = 'TAKE_AWAY' in seed_content or 'TakeAway' in seed_content
has_delivery_seed = 'DELIVERY' in seed_content or 'Delivery' in seed_content
has_wifi_seed = 'wifi' in seed_content.lower() or 'bssid' in seed_content.lower()

print(f"  - Seed DineIn orders: {has_dinein_seed}")
print(f"  - Seed TakeAway orders: {has_takeaway_seed}")
print(f"  - Seed Delivery orders: {has_delivery_seed}")
print(f"  - Seed WiFi configuration: {has_wifi_seed}")

print("\n=== VERIFYING DOC_AUDIT_REPORT.md ===")
with open(r'd:\Idea_DoAn\DOC_AUDIT_REPORT.md', 'r', encoding='utf-8') as f:
    audit_content = f.read()

print(f"  - Lines in DOC_AUDIT_REPORT.md: {len(audit_content.splitlines())}")
print(f"  - Has Comprehensive Audit Sections: {'BÁO CÁO' in audit_content}")
