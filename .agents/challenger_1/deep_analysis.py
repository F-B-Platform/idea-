
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Idea_DoAn\.agents\challenger_1\scan_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('===============================================================')
print('DETAILED ANALYSIS OF OBSOLETE KEYWORDS ACROSS REPOSITORY')
print('===============================================================')

# Active canonical files according to PROJECT.md
canonical_files = {
    r'01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Tom_Tat_1_Trang_Executive_Summary.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md',
    r'02_Bao_Gia_Chi_Phi\Bang_Bao_Gia_Smart_FB_OS.md',
    r'02_Bao_Gia_Chi_Phi\Chi_Phi_Duy_Tri_Hang_Thang.md',
    r'03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md',
    r'03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md',
    r'03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md',
    r'03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md',
    r'03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md',
    r'03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md',
    r'03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md',
    r'03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md',
    r'03_Quy_Trinh_Trien_Khai\README.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md',
    r'05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md',
    r'05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md',
    r'05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md',
    r'06_Danh_Sach_Skills\README.md',
    r'ROADMAP.md',
    r'DOC_AUDIT_REPORT.md',
    r'PROJECT.md'
}

elim_words = [
    'bỏ', 'xóa', 'loại bỏ', 'thay thế', 'elimination', 'deprecated', 
    'khác biệt', 'removed', 'chuyển sang', 'thay vì', 'trước đây', 
    'không còn', 'loại trừ', 'quy tắc bất biến', 'triệt để', 'không có', 
    'tiết kiệm', 'scale-up', 'scale up', 'khóa wifi', 'wifi-locked',
    'eliminate', 'eliminated', 'deprecation', 'bãi bỏ', 'chấm dứt'
]

potential_violations = []
canonical_matches = []
legacy_matches = []

for pat_name, matches in data['obsolete'].items():
    print(f'\n>>> Pattern: {pat_name} ({len(matches)} matches)')
    for m in matches:
        fn = m['file']
        ln = m['line']
        cnt = m['content']
        is_canonical = fn in canonical_files
        is_elim = any(w in cnt.lower() for w in elim_words)
        
        if not is_canonical:
            status = 'LEGACY_FILE'
            legacy_matches.append((pat_name, fn, ln, cnt))
        elif is_elim:
            status = 'ELIMINATION_OR_MIGRATION_NOTE'
            canonical_matches.append((pat_name, fn, ln, cnt, status))
        else:
            status = 'POTENTIAL_ACTIVE_VIOLATION'
            potential_violations.append((pat_name, fn, ln, cnt))
            canonical_matches.append((pat_name, fn, ln, cnt, status))
            
        print(f'  [{status}] {fn}:{ln} -> {cnt[:100]}')

print('\n===============================================================')
print(f'SUMMARY: {len(potential_violations)} POTENTIAL VIOLATIONS IN CANONICAL FILES')
print('===============================================================')
for pat, fn, ln, cnt in potential_violations:
    print(f'FAIL: [{pat}] {fn}:{ln} -> {cnt}')

print('\n===============================================================')
print(f'LEGACY / NON-CANONICAL FILES WITH OBSOLETE TERMS: {len(legacy_matches)}')
print('===============================================================')
by_leg_file = {}
for pat, fn, ln, cnt in legacy_matches:
    by_leg_file.setdefault(fn, []).append((pat, ln, cnt))
for fn, items in by_leg_file.items():
    print(f'Legacy File: {fn} ({len(items)} obsolete matches)')
