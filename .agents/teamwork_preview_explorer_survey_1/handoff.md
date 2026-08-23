# 📋 HANDOFF REPORT: EXPLORER 1 — SPEC, RBAC, REQUIREMENTS & DB ARCHITECTURE SPECIALIST

**Task:** Survey and Gap Analysis of Source of Truth vs Implementation Guides (`01_Phan_Tich_Yeu_Cau.md` & `02_Thiet_Ke_Database.md`)  
**Working Directory:** `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_1\`  
**Target Output Artifact:** `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_1\survey_requirements_db.md`  
**Handoff Type:** Hard Handoff (Investigation & Survey Complete)  

---

## 1. OBSERVATION

1. **Source of Truth Files (`d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc/`):**
   - `Actor_Phan_Quyen_Chuc_Nang.md` (lines 132-705): Fully defines **62 core features across 4 Actors**:
     - Customer Actor: 20 features (`C-01` ~ `C-20`, lines 132-303).
     - Staff / Barista Actor: 13 features (`S-01` ~ `S-13`, lines 320-428).
     - Branch Manager Actor: 12 features (`M-01` ~ `M-12`, lines 445-544).
     - Chain Admin Actor: 17 features (`A-01` ~ `A-17`, lines 561-705).
     - Total: $20 + 13 + 12 + 17 = 62$ features.
   - `Tong_Quan_Kien_Truc_He_Thong.md` (lines 400-692): Defines the standardized **25 database entities in 3NF (PostgreSQL 16)**:
     `branches`, `branch_wifi_configs`, `users`, `roles`, `user_roles`, `audit_logs`, `categories`, `products`, `product_sizes`, `product_branch_prices`, `modifiers`, `product_modifiers`, `ingredients`, `recipes_bom`, `tables`, `orders`, `order_items`, `order_item_modifiers`, `payments`, `customers`, `loyalty_cup_transactions`, `vouchers`, `customer_reviews`, `shifts`, `attendances`.
   - `Workflow_Quy_Trinh_Nghiep_Vu.md` (lines 1-93, 198-250) & `Smart_FB_Operating_System.md` (lines 106-200): Establish the 5 inviolable business rules:
     - Dine-In 2 branches: Branch A (VietQR pre-payment, kitchen receives only when `Paid`) vs Branch B (Cash post-payment, kitchen receives immediately `Confirmed`, staff serves with printed Bill having dynamic VietQR).
     - Delivery QR: Fixed fee 20,000 VNĐ, 100% VietQR pre-payment, No COD, mandatory recipient phone + delivery address.
     - Takeaway Web POS: Cashier operates on `(staff)/pos` without QR, phone CRM lookup, 10-cup loyalty (+1 cup per item, 10 cups = 1 free cup, **ONLY for Takeaway**), post-payment.
     - WiFi Attendance: Dual-check verification (BSSID / IP Subnet in `branch_wifi_configs` + Staff Code), strictly blocking 4G/5G and foreign WiFi.
     - Zero Staff Mobile App: 100% web responsive across 5 route groups `(customer)`, `(kds)`, `(staff)`, `(manager)`, `(admin)`.

2. **Current Deployment Documentation Files (`d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai/`):**
   - `01_Phan_Tich_Yeu_Cau.md`:
     - Line 57: Groups functional requirements into "44 FRs" (`FR-01` to `FR-44`) instead of the standardized 62 features categorized by 4 Actors.
     - Lacks detailed Input/Output data contracts and Edge Cases for each specific Actor feature.
   - `02_Thiet_Ke_Database.md`:
     - Inconsistency: The matrix in Section 2 declares 30 tables, the main DDL declares 28 tables, and Section 3.8 appends 2 more tables (`seasonal_menus`, `seasonal_menu_products`).
     - Needs alignment with the canonical 25-table 3NF schema specified in `Tong_Quan_Kien_Truc_He_Thong.md`.

---

## 2. LOGIC CHAIN

1. **Premise 1:** The authoritative master specification is defined in `01_Tai_Lieu_Dac_Ta_Goc/` and codified in `ORIGINAL_REQUEST.md`.
2. **Premise 2:** `Actor_Phan_Quyen_Chuc_Nang.md` explicitly structures the functional requirements into exactly 62 features across 4 distinct Actors (20 Customer + 13 Staff + 12 Manager + 17 Admin).
3. **Premise 3:** `01_Phan_Tich_Yeu_Cau.md` currently employs an obsolete numbering scheme of 44 FRs (`FR-01` ~ `FR-44`), which obscures the Actor boundaries and omits detailed contracts for each feature.
4. **Premise 4:** `Tong_Quan_Kien_Truc_He_Thong.md` defines the canonical 25-entity 3NF relational data model for PostgreSQL 16, whereas `02_Thiet_Ke_Database.md` presents a fragmented 28/30 table layout.
5. **Deduction:** To achieve 100% architectural consistency and compliance with v2.5.0, `01_Phan_Tich_Yeu_Cau.md` must be rewritten to adopt the 62-feature Actor-based catalog with exhaustive contracts, and `02_Thiet_Ke_Database.md` must be standardized onto the canonical 25-entity 3NF PostgreSQL 16 schema.

---

## 3. CAVEATS

- **No code modification performed outside `.agents/`:** As an Explorer (read-only investigation specialist), no files in `03_Quy_Trinh_Trien_Khai/` were modified directly during this turn. All findings and mapping specifications are captured in `survey_requirements_db.md`.
- **Database table count scoping:** While `seasonal_menus` can exist as an extension, the core relational database is standardized at 25 entities in 3NF to ensure clear ownership and clean architecture boundaries for EF Core 8 mappings.

---

## 4. CONCLUSION

- The comprehensive survey and gap analysis is complete and documented in `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_1\survey_requirements_db.md`.
- All 62 core features across 4 Actors (`C-01` ~ `C-20`, `S-01` ~ `S-13`, `M-01` ~ `M-12`, `A-01` ~ `A-17`), the 6 removed legacy concepts, the 4 core business engines, and the 25 3NF database entities have been mapped in exhaustive detail with zero placeholders.
- The downstream authoring agents have a complete, verified baseline to rewrite `01_Phan_Tich_Yeu_Cau.md` and `02_Thiet_Ke_Database.md`.

---

## 5. VERIFICATION METHOD

1. **Verify Feature Count:**
   - Inspect `d:\Idea_DoAn\.agents\teamwork_preview_explorer_survey_1\survey_requirements_db.md` (Section 2).
   - Count items: Customer ($C=20$), Staff ($S=13$), Manager ($M=12$), Admin ($A=17$). Sum $= 62$.
2. **Verify Removed Concepts:**
   - Inspect Section 3 of `survey_requirements_db.md` to confirm the removal of Staff Mobile App, GPS 50m, QR 30s, C-23, C-24, separate voucher wallet, and separate calorie lookup.
3. **Verify Database 3NF Schema:**
   - Inspect Section 5 of `survey_requirements_db.md` to confirm the 25 normalized entities matching `Tong_Quan_Kien_Truc_He_Thong.md`.
4. **Invalidation Conditions:**
   - Any reference to Flutter/React Native for staff, GPS coordinates in attendance, or deviation from the 62-feature count will invalidate this baseline.
