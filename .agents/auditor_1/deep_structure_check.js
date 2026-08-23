const fs = require('fs');

const f1 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\01_Kien_Truc_Tong_Quan.md', 'utf8');
const f2 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\02_Sequence_Diagrams.md', 'utf8');
const f3 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md', 'utf8');
const f4 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\04_Deployment_Diagram.md', 'utf8');

console.log('=== AUDIT DEEP-DIVE CHECKS ===\n');

// 1. FILE 01: KIEN TRUC TONG QUAN
console.log('--- 01_Kien_Truc_Tong_Quan.md ---');
console.log('Total characters:', f1.length);
console.log('Has C4 Context (Level 1):', f1.includes('MÔ HÌNH C4 CẤP 1: SYSTEM CONTEXT DIAGRAM'));
console.log('Has C4 Containers (Level 2):', f1.includes('MÔ HÌNH C4 CẤP 2: CONTAINER DIAGRAM'));
console.log('Has C4 Components (Level 3):', f1.includes('MÔ HÌNH C4 CẤP 3: COMPONENT DIAGRAM'));
console.log('Has 5 Route Groups Table:', f1.includes('5 Route Groups') && f1.includes('(customer)') && f1.includes('(kds)') && f1.includes('(staff)') && f1.includes('(manager)') && f1.includes('(admin)'));
console.log('Has 4 SignalR Hubs Table:', f1.includes('4 SignalR Hubs') && f1.includes('OrderHub') && f1.includes('KitchenHub') && f1.includes('PaymentHub') && f1.includes('NotificationHub'));
console.log('Has Redis Invalidation & RedLock Tables:', f1.includes('Redis 7') && f1.includes('Distributed RedLock'));
console.log('Has AI Pipelines (Gemini + Apriori):', f1.includes('Gemini 1.5 Flash') && f1.includes('Apriori'));
console.log('Has RBAC Matrix (4 roles):', f1.includes('Customer') && f1.includes('Staff') && f1.includes('Manager') && f1.includes('ChainAdmin'));
console.log('Has NFRs & SLAs:', f1.includes('Non-Functional SLAs'));

// 2. FILE 02: SEQUENCE DIAGRAMS
console.log('\n--- 02_Sequence_Diagrams.md ---');
console.log('Total characters:', f2.length);
for (let i = 1; i <= 10; i++) {
  const numStr = i < 10 ? `0${i}` : `${i}`;
  const seqHeader = `SEQ-${numStr}`;
  const hasSeq = f2.includes(seqHeader);
  console.log(`Has ${seqHeader}:`, hasSeq);
}
console.log('Has Alignment Table with 62 features & 16 workflows:', f2.includes('BẢNG ĐỐI CHIẾU 10 SEQUENCE VỚI MA TRẬN 62 TÍNH NĂNG VÀ 16 WORKFLOWS'));
console.log('Has Verification & Integration Guide:', f2.includes('HƯỚNG DẪN KIỂM CHỨNG & TÍCH HỢP HỆ THỐNG'));

// 3. FILE 03: ERD DATABASE DIAGRAM
console.log('\n--- 03_ERD_Database_Diagram.md ---');
console.log('Total characters:', f3.length);
console.log('Has erDiagram block:', f3.includes('```mermaid\nerDiagram') || f3.includes('```mermaid\r\nerDiagram'));
console.log('Number of data dictionary tables:', (f3.match(/### Bảng \d+:/g) || []).length);
console.log('Has 8 Functional Modules Matrix:', f3.includes('MA TRẬN PHÂN RÃ 8 PHÂN HỆ NGHIỆP VỤ'));
console.log('Has Enums Specification (Chapter 4):', f3.includes('CHƯƠNG 4: ĐẶC TẢ KIỂU DỮ LIỆU LIỆT KÊ (ENUMS)'));
console.log('Has Indexing Strategy (Chapter 5):', f3.includes('CHƯƠNG 5: CHIẾN LƯỢC ĐÁNH CHỈ MỤC'));
console.log('Has 3 Business Triggers (Chapter 6):', f3.includes('Trigger 1: Tự Động Trừ Tồn Kho') && f3.includes('Trigger 2: Tự Động Kích Hoạt Alert') && f3.includes('Trigger 3: Tự Động Tích Ly'));
console.log('Has Multi-branch RLS (Chapter 7):', f3.includes('CHƯƠNG 7: MÔ HÌNH PHÂN VÙNG DỮ LIỆU & BẢO MẬT ROW-LEVEL SECURITY'));

// 4. FILE 04: DEPLOYMENT DIAGRAM
console.log('\n--- 04_Deployment_Diagram.md ---');
console.log('Total characters:', f4.length);
console.log('Has Deployment Topology Graph:', f4.includes('```mermaid\ngraph TB') || f4.includes('```mermaid\r\ngraph TB'));
console.log('Has VPS vs Azure Comparison & Trade-offs:', f4.includes('BẢNG SO SÁNH TOÀN DIỆN & PHÂN TÍCH TRADE-OFF'));
console.log('Has Complete docker-compose.prod.yml:', f4.includes('docker-compose.prod.yml') && f4.includes('backend:') && f4.includes('frontend:') && f4.includes('postgres:'));
console.log('Has Complete nginx.conf:', f4.includes('nginx.conf') && f4.includes('proxy_pass http://backend_api;') && f4.includes('proxy_pass http://frontend_app;'));
console.log('Has GitHub Actions CI/CD Pipeline:', f4.includes('TỰ ĐỘNG HÓA CI/CD PIPELINE VỚI GITHUB ACTIONS'));
console.log('Has Backup & DR Scripts:', f4.includes('backup_postgres.sh') && f4.includes('Disaster Recovery Runbook'));
console.log('Has Health Checks, Observability & Firewall Matrix:', f4.includes('Bộ Endpoint Health Checks') && f4.includes('MA TRẬN CỔNG MẠNG, TƯỜNG LỬA'));