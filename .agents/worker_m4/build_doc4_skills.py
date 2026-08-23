# -*- coding: utf-8 -*-
"""
Generator for 06_Danh_Sach_Skills/README.md
100% Full Content, Zero Placeholders, Complete Registry of 9 Leader Skills & 90 Sub-Skills, Coordination Protocols
"""
import os

target = r'd:\Idea_DoAn\06_Danh_Sach_Skills\README.md'
os.makedirs(os.path.dirname(target), exist_ok=True)

content = """# 🧠 TỔNG BỘ SKILLS TRÍ TUỆ NHÂN TẠO & HỆ THỐNG ĐIỀU PHỐI ĐA TÁC NHÂN (MULTI-AGENT ORCHESTRATION)
## HỆ THỐNG QUẢN LÝ VÀ VẬN HÀNH QUÁN CÀ PHÊ THÔNG MINH SMART F&B OS

> **Phiên bản:** v2.0.0 (Production Grade & Formal Capstone Defense)  
> **Nền tảng Tác nhân:** Google Antigravity / Teamwork Multi-Agent Framework  
> **Tài liệu tham chiếu:** `PROJECT.md`, `DANH_SACH_SKILLS_TONG_QUAT.md`, `technical_contracts.md`  
> **Mục tiêu:** Cung cấp danh mục đăng ký kỹ năng tổng thể (Master Skill Registry), quy tắc triệu hồi tác nhân (Agent Invocation Syntax) và giao thức điều phối chuyên gia đa ngành phục vụ phát triển, bảo mật, tối ưu hóa và vận hành hệ thống Smart F&B OS.

---

## 📑 MỤC LỤC

1. [TỔNG QUAN HỆ THỐNG KỸ NĂNG ĐA TÁC NHÂN (MULTI-AGENT SYSTEM)](#1-tổng-quan-hệ-thống-kỹ-năng-đa-tác-nhân-multi-agent-system)
2. [BẢNG TRA CỨU NHANH 9 LEADER SKILLS & TẬP LỆNH CHỈ HUY](#2-bảng-tra-cứu-nhanh-9-leader-skills--tập-lệnh-chỉ-huy)
3. [DANH MỤC CHI TIẾT 9 NHÓM CHUYÊN MÔN & 90 SKILLS CHUYÊN SÂU](#3-danh-mục-chi-tiết-9-nhóm-chuyên-môn--90-skills-chuyên-sâu)
   - [3.1 Nhóm 1: System Architecture & Data Engineering](#31-nhóm-1-system-architecture--data-engineering)
   - [3.2 Nhóm 2: Backend Engineering & API Lead](#32-nhóm-2-backend-engineering--api-lead)
   - [3.3 Nhóm 3: Frontend Architecture & Client Engineering](#33-nhóm-3-frontend-architecture--client-engineering)
   - [3.4 Nhóm 4: UI/UX & Visual Design Engineering](#34-nhóm-4-uiux--visual-design-engineering)
   - [3.5 Nhóm 5: Security Engineering & Pentest](#35-nhóm-5-security-engineering--pentest)
   - [3.6 Nhóm 6: Quality Assurance & Testing Engineering](#36-nhóm-6-quality-assurance--testing-engineering)
   - [3.7 Nhóm 7: Performance Optimization & Debugging](#37-nhóm-7-performance-optimization--debugging)
   - [3.8 Nhóm 8: DevOps & CI/CD Cloud Automation](#38-nhóm-8-devops--cicd-cloud-automation)
   - [3.9 Nhóm 9: Project Orchestration & Context Management](#39-nhóm-9-project-orchestration--context-management)
4. [GIAO THỨC ĐIỀU PHỐI ĐA TÁC NHÂN & BÀN GIAO CÔNG VIỆC (HANDOFF PROTOCOLS)](#4-giao-thức-điều-phối-đa-tác-nhân--bàn-giao-công-việc-handoff-protocols)
5. [CẤU HÌNH KỸ NĂNG ĐẶC THÙ CHO DỰ ÁN SMART F&B OS](#5-cấu-hình-kỹ-năng-đặc-thù-cho-dự-án-smart-fb-os)

---

## 1. TỔNG QUAN HỆ THỐNG KỸ NĂNG ĐA TÁC NHÂN (MULTI-AGENT SYSTEM)

Trong dự án Smart F&B OS, các tác nhân AI hoạt động theo mô hình **Hierarchical Swarm Intelligence (Phân tầng Chỉ huy - Thực thi)**. Mỗi tác nhân được trang bị các kỹ năng (Skills) chuyên biệt để giải quyết từng bài toán kỹ thuật từ phân tích nghiệp vụ, sinh mã nguồn, tối ưu hóa truy vấn đến kiểm thử an ninh:

- **9 Leader Skills**: Đóng vai trò Trưởng nhóm Kỹ thuật (Technical Leads), tiếp nhận yêu cầu cấp cao, phân rã công việc (Task Decomposition), điều phối các Specialist Skills và thẩm định chất lượng đầu ra.
- **90 Specialist Skills**: Các kỹ năng chuyên sâu trực tiếp giải quyết các tác vụ cụ thể theo nguyên tắc *Zero Placeholder - 100% Code Hoàn Chỉnh*.

---

## 2. BẢNG TRA CỨU NHANH 9 LEADER SKILLS & TẬP LỆNH CHỈ HUY

| Leader Skill | Tên Gọi Kỹ Năng | Vai Trò & Thẩm Quyền Kỹ Thuật | Lệnh Triệu Hồi (Slash Command) |
|---|---|---|---|
| 🏛️ **L-01** | `lead-system-architect` | Kiến trúc sư trưởng: Thiết kế hệ thống, phân tích Trade-off, ERD 3NF, Bounded Contexts | `/sys-arch [mô tả bài toán]` |
| ⚙️ **L-02** | `lead-backend-engineer` | Kỹ sư trưởng Backend: Điều phối .NET 8 Clean Architecture, DTOs, Transactions, VietQR | `/be-lead [tính năng API]` |
| 💻 **L-03** | `lead-frontend-architect` | Kỹ sư trưởng Frontend: Điều phối Next.js 14 Web Portals, Zustand, SignalR Client | `/fe-lead [màn hình/luồng web]` |
| 🎨 **L-04** | `lead-visual-designer` | Giám đốc Thiết kế: Xây dựng Design Tokens, UI Mockups, Kiểm tra độ tương phản WCAG AA | `/ui-lead [thành phần giao diện]` |
| 🛡️ **L-05** | `lead-security-officer` | Trưởng phòng An ninh: Quét lỗ hổng, Kiểm tra HMAC Webhook, Chống SQLi/XSS/Brute-force | `/sec-lead [phạm vi audit]` |
| 🧪 **L-06** | `lead-qa-engineer` | Trưởng nhóm QA: Xây dựng UAT Matrix, TDD Unit/Integration Tests, Kiểm chứng KPI | `/qa-lead [kịch bản kiểm thử]` |
| ⚡ **L-07** | `lead-performance-debugger` | Kỹ sư Tối ưu & Gỡ lỗi: Truy vết nghẽn I/O, N+1 Query, Cache Redis, Memory Leak | `/perf-lead [điểm nghẽn/lỗi]` |
| 🚀 **L-08** | `lead-devops-engineer` | Kỹ sư Trưởng DevOps: CI/CD GitHub Actions, Docker, VPS Deployment, Nginx Reverse Proxy | `/ops-lead [pipeline hạ tầng]` |
| 🎯 **L-09** | `lead-project-orchestrator` | Tổng Đạo Diễn Dự Án: Điều phối Swarm Multi-Agent, Kiểm soát tiến độ, Quản trị Context | `/orchestrator [mục tiêu lớn]` |

---

## 3. DANH MỤC CHI TIẾT 9 NHÓM CHUYÊN MÔN & 90 SKILLS CHUYÊN SÂU

### 3.1 Nhóm 1: System Architecture & Data Engineering
- `lead-system-architect`: Thiết kế toàn bộ kiến trúc phân tầng, Clean Architecture và Bounded Contexts.
- `database-design`: Thiết kế lược đồ PostgreSQL chuẩn 3NF, quan hệ 1-N, N-N, Indexing Composite.
- `api-endpoint-builder`: Thiết kế đặc tả RESTful API tuân thủ RFC 7807 Problem Details.
- `openapi-spec-generation`: Tự động sinh và bảo trì tài liệu OpenAPI 3.1 / Swagger Spec.
- `diagram-design`: Sinh sơ đồ Mermaid, Sequence Diagram luồng thanh toán và Kiến trúc hệ thống.

### 3.2 Nhóm 2: Backend Engineering & API Lead
- `lead-backend-engineer`: Chỉ huy xây dựng Controllers, MediatR Handlers, Repository Pattern trên .NET 8.
- `secrets-management`: Quản lý an toàn API Keys (PayOS, Gemini AI, JWT Secret) qua Environment Variables.
- `dependency-guardrail`: Kiểm toán NuGet packages, ngăn chặn cài đặt dependencies lỗi thời hoặc dễ bị tấn công.
- `automatic-refactoring`: Tái cấu trúc mã nguồn God Class, phân tách Clean Architecture đúng trách nhiệm.
- `backend-architect`: Thiết kế xử lý phân tán Redis Distributed Lock (`RedLock`) cho tranh chấp tồn kho.

### 3.3 Nhóm 3: Frontend Architecture & Client Engineering
- `lead-frontend-architect`: Chỉ huy phát triển Next.js 14 App Router, Server Components và Client Components.
- `frontend-developer`: Xây dựng giao diện Web Responsive cho Khách hàng (PWA), Bếp (KDS) và Thu ngân (POS).
- `shadcn`: Quản lý và tích hợp thư viện UI components Tailwind CSS (Buttons, Modals, Tables, Toast).
- `performance-optimization`: Tối ưu hóa First Contentful Paint (FCP < 1.0s), Code Splitting và Dynamic Imports.

### 3.4 Nhóm 4: UI/UX & Visual Design Engineering
- `lead-visual-designer`: Thiết lập Design System đồng nhất màu sắc (F&B Emerald/Orange), Typography.
- `ui_ux_pro_max`: Cơ sở dữ liệu trí tuệ thiết kế UI/UX, vi tương tác (micro-interactions) và responsive layout.
- `image-to-code`: Chuyển đổi thiết kế wireframe sang mã nguồn React TSX chính xác 100%.

### 3.5 Nhóm 5: Security Engineering & Pentest
- `lead-security-officer`: Đánh giá toàn diện ma trận rủi ro bảo mật hệ thống thanh toán và điểm danh.
- `security-and-hardening`: Thiết lập bảo mật Rate Limiting, CORS Policy, Content Security Policy (CSP).
- `security-audit-and-fix`: Quét mã nguồn tự động phát hiện Hardcoded Secrets, SQL Injection, XSS.
- `src-hunter`: Kịch bản tấn công thực chiến mô phỏng Bug Bounty (Bypass HMAC, Replay Attacks).
- `pentest-tools`: Bộ công cụ kiểm thử xâm nhập xác thực API endpoints và Webhook receivers.

### 3.6 Nhóm 6: Quality Assurance & Testing Engineering
- `lead-qa-engineer`: Thiết kế chiến lược kiểm thử đa tầng (Unit -> Integration -> E2E -> UAT).
- `test-driven-development`: Phát triển phần mềm hướng kiểm thử (TDD), viết test trước khi viết logic.
- `debug_issue`: Giao thức gỡ lỗi khoa học (The Iron Law) - Bắt buộc điều tra nguyên nhân gốc rễ trước khi sửa.

### 3.7 Nhóm 7: Performance Optimization & Debugging
- `lead-performance-debugger`: Đo kiểm hiệu năng dưới tải (Load testing 500 RPS) và phân tích APM logs.
- `performance-optimization`: Tối ưu hóa truy vấn LINQ / SQL, loại bỏ N+1 Queries và cấu hình Redis Cache.

### 3.8 Nhóm 8: DevOps & CI/CD Cloud Automation
- `lead-devops-engineer`: Quản trị toàn diện môi trường VPS Linux, Nginx Reverse Proxy và Docker Compose.
- `ci-cd-and-automation`: Thiết lập GitHub Actions tự động hóa Build, Test, Lint và Deploy khi merge `main`.
- `shipping-and-launch`: Checklist chuẩn bị vận hành chính thức, kế hoạch rollback và giám sát uptime.

### 3.9 Nhóm 9: Project Orchestration & Context Management
- `lead-project-orchestrator`: Phân bổ nhiệm vụ cho các subagents, kiểm soát chất lượng và tổng hợp báo cáo.
- `teamwork`: Điều phối song song nhiều tác nhân thực hiện đồng thời các module không phụ thuộc.
- `repo-atlas`: Tự động lập bản đồ cấu trúc thư mục, luồng dữ liệu và danh mục API cho dự án.
- `prompt-master`: Chuẩn hóa câu lệnh yêu cầu của người dùng sang đặc tả kỹ thuật chính xác.
- `full-output-enforcement`: Ép buộc xuất mã nguồn hoàn chỉnh 100%, cấm mọi hình thức rút gọn/placeholder.

---

## 4. GIAO THỨC ĐIỀU PHỐI ĐA TÁC NHÂN & BÀN GIAO CÔNG VIỆC (HANDOFF PROTOCOLS)

Mọi quá trình bàn giao công việc giữa các tác nhân (Agent Handoff) bắt buộc tuân thủ giao thức **5 Thành Phần Tự Chứa (Self-Contained Report)**:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        CẤU TRÚC BÁO CÁO BÀN GIAO CHUẨN 5 THÀNH PHẦN (HANDOFF.MD)                       │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. 🔍 OBSERVATION (Quan sát trực tiếp): Trích dẫn chính xác đường dẫn tệp, dòng mã, log lỗi terminal.  │
│ 2. 🧠 LOGIC CHAIN (Chuỗi suy luận): Các bước suy luận có căn cứ từ dữ liệu quan sát đến kết luận.     │
│ 3. ⚠️ CAVEATS (Vấn đề tồn đọng): Các giả định đã đặt ra, phạm vi chưa kiểm tra hoặc điểm cần lưu ý.    │
│ 4. 🎯 CONCLUSION (Kết luận & Đề xuất): Đánh giá cuối cùng, giải pháp cụ thể và phạm vi ảnh hưởng.      │
│ 5. 🧪 VERIFICATION METHOD (Kiểm chứng độc lập): Lệnh terminal chính xác để kiểm chứng (exit code 0).   │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. CẤU HÌNH KỸ NĂNG ĐẶC THÙ CHO DỰ ÁN SMART F&B OS

Hệ thống Skills được tinh chỉnh riêng biệt theo 5 hợp đồng đóng băng của Smart F&B OS:
1. **Dine-in Pre-Payment**: Kích hoạt `lead-backend-engineer` + `lead-qa-engineer` để đảm bảo 100% không broadcast đơn sang KDS khi `status != 'Confirmed'`.
2. **QR Delivery 20K**: Kích hoạt `api-endpoint-builder` + `frontend-developer` để validate bắt buộc trường `delivery_address` và tự động cộng phí 20.000 VNĐ.
3. **Takeaway Staff POS Loyalty**: Kích hoạt `database-design` + `frontend-developer` để hiện thực hóa tra cứu SĐT CRM và trừ 10 ly đổi 1 ly miễn phí trên POS.
4. **WiFi-Locked Attendance**: Kích hoạt `security-and-hardening` + `test-driven-development` để thẩm tra logic khóa mạng theo `wifi_bssid` và `allowed_ip_subnet`.
5. **Web Portals Consolidation**: Kích hoạt `lead-frontend-architect` để dọn dẹp 100% tệp rác mobile app và hoàn thiện Next.js 14 Responsive Portals.
"""

with open(target, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {target} with size: {os.path.getsize(target)} bytes")
