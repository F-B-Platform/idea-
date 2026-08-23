## 2026-08-23T13:51:58Z

Bạn là Principal Software Quality Reviewer (Reviewer 2). Nhiệm vụ của bạn là thẩm định độc lập chất lượng và độ sâu kỹ thuật của cả 4 tệp sơ đồ kiến trúc:
1. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md`
2. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md`
3. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md`
4. `d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md`

Thư mục làm việc của bạn: `d:\Idea_DoAn\.agents\reviewer_2\`
Tạo file `progress.md` và `handoff.md`.

Nguồn sự thật đối chiếu:
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
- `d:\Idea_DoAn\.agents\ORIGINAL_REQUEST.md`

Tiêu chí đánh giá:
- Chi tiết kỹ thuật của Sequence Diagrams (Seq-01 -> Seq-10): payload, participants, status codes, SignalR events, error handling.
- Chuẩn hóa ERD: 25+ bảng 3NF, đầy đủ constraints (PK, FK, CHECK), types, data dictionary, indexing, triggers.
- Deployment & Infrastructure: Docker Compose config, NGINX config, health checks, so sánh Linux VPS vs Azure Singapore.
- Kiểm tra toàn bộ cú pháp Mermaid của tất cả các file.

Đưa ra kết luận rõ ràng trong `handoff.md`: `APPROVE` hoặc `REQUEST_CHANGES`. Gửi tin nhắn về cho orchestrator.
