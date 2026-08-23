## 2026-08-23T14:36:04Z
You are an Explorer subagent for the Smart F&B Operating System project.
Working directory: d:\Idea_DoAn\.agents\explorer_survey_uat\
Create your working directory if needed.
Read the following files carefully:
1. `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`
2. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
3. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`
4. `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
5. `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md`
6. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md`
7. `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md`

Your task:
Analyze and extract all information required to fully rewrite `d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md` according to Master Spec v2.5.0.
1. Outline the 5-Minute Continuous Linked Demo Flow connecting 7 actors/scenes: Khách đặt Dine-In 2 nhánh (A: PayOS VietQR trước -> KDS, B: Tiền mặt sau -> KDS Confirmed ngay -> In bill VietQR), QR Delivery (SĐT + Đ/c bắt buộc, 20k ship, 100% VietQR trước, khóa COD), Takeaway quầy POS (Tra cứu CRM SĐT, Tích 10 ly tặng 1 ly, Thu sau), Chấm công WiFi (BSSID/IP vs 4G từ chối), KDS Barista BOM trừ kho g/ml & 86-Toggle & Undo 10s, Quản lý Z-Report giải trình > 50k, Admin Seasonal/Bảng giá vùng/AI-2 Combo Apriori.
2. Structure the 35+ full UAT test cases with complete fields: Mã test, Mục đích, Tiền điều kiện, Các bước thực hiện, Dữ liệu đầu vào, Kết quả kỳ vọng, Trạng thái (TC-DINE-01A, TC-DINE-01B, TC-DEL-01, TC-TAKE-01, TC-ATT-01, TC-KDS-01, TC-MGR-01, TC-ADM-01, TC-EDGE-01~10, plus all module cases).
3. Identify all obsolete references to purge: Staff Mobile App, GPS 50m, 30s QR, C-23/C-24.
4. Verify GitHub Alert Callout formatting (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`).

Write your detailed findings to `d:\Idea_DoAn\.agents\explorer_survey_uat\analysis.md` and `d:\Idea_DoAn\.agents\explorer_survey_uat\handoff.md`.
Then send a message to parent with the summary and report path.
