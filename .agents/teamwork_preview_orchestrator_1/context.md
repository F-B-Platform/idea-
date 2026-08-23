# Context & References

## Authoritative Specifications (Source of Truth)
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md`
- `d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_KhachHang_Luong_Chay.md`

## Target Deliverables (to be standardized 100%)
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md`
- `d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\README.md`

## Key Business & Technical Rules (v2.5.0)
1. 62 Features: 20 Customer (C-01~C-20), 13 Staff (S-01~S-13), 12 Manager (M-01~M-12), 17 Admin (A-01~A-17).
2. Removed: Staff Mobile App (Flutter/React Native), GPS 50m, QR 30s, C-23, C-24, separate calorie lookup, voucher wallet.
3. Dine-In 2 branches: VietQR prepay vs Cash postpay + Bill QR.
4. Delivery: Fixed 20,000 VND shipping fee, 100% VietQR prepay, no COD, phone + address required.
5. Takeaway: Counter staff POS, no QR, phone CRM, 10 cups get 1 free loyalty, postpay cash/QR.
6. Attendance: WiFi Router BSSID / IP Subnet check + Staff PIN.
7. Database: 25 entities 3NF in PostgreSQL 16.
8. Backend: Clean Architecture 4 layers (.NET 8 C#), MediatR CQRS, FluentValidation, EF Core 8, Redis, SignalR 4 Hubs, Gemini 1.5 Flash + Apriori.
9. Frontend: Next.js 14 App Router (5 route groups: `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`), Tailwind CSS, Shadcn UI, Zustand, TanStack Query.
10. Quality: Zero Placeholders, 100% valid Mermaid diagrams, GitHub Alert Callouts.
