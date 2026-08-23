const fs = require('fs');

const f1 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\01_Kien_Truc_Tong_Quan.md', 'utf8');
const f2 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\02_Sequence_Diagrams.md', 'utf8');
const f3 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md', 'utf8');
const f4 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\04_Deployment_Diagram.md', 'utf8');

const report = {
  f1_TongQuan: {
    c4Level1: /Level 1.*System Context/i.test(f1),
    c4Level2: /Level 2.*Container/i.test(f1),
    c4Level3: /Level 3.*Component/i.test(f1),
    routeGroups: ['(customer)', '(kds)', '(staff)', '(manager)', '(admin)'].every(g => f1.includes(g)),
    signalrHubs: ['OrderHub', 'KitchenHub', 'PaymentHub', 'NotificationHub'].every(h => f1.includes(h)),
    redisCaching: /Redis/i.test(f1) && /Cache-aside/i.test(f1) && /(Distributed Lock|RedLock)/i.test(f1),
    aiEngine: /Gemini 1.5 Flash/i.test(f1) && /Apriori/i.test(f1),
    tradeOffs: /Trade-off/i.test(f1) && /ADR/i.test(f1)
  },
  f2_Sequence: {
    seq01_DineInA: /Seq-01.*Dine-In.*Nhánh A/i.test(f2) && /PayOS/i.test(f2),
    seq02_DineInB: /Seq-02.*Dine-In.*Nhánh B/i.test(f2) && /Tiền mặt trả sau/i.test(f2),
    seq03_Delivery: /Seq-03.*Delivery/i.test(f2) && /20\.000/i.test(f2),
    seq04_Takeaway: /Seq-04.*Takeaway.*POS/i.test(f2) && /10 ly/i.test(f2),
    seq05_Attendance: /Seq-05.*Chấm công.*WiFi/i.test(f2) && /BSSID/i.test(f2),
    seq06_KDS_BOM: /Seq-06.*KDS.*BOM/i.test(f2) && /86-Toggle/i.test(f2),
    seq07_CallStaff: /Seq-07.*Gọi phục vụ/i.test(f2) && /chuông/i.test(f2),
    seq08_Review: /Seq-08.*Đánh giá/i.test(f2) && /Alert đỏ/i.test(f2),
    seq09_Shift_ZReport: /Seq-09.*Ca két.*Z-Report/i.test(f2) && /50\.000/i.test(f2),
    seq10_Admin_Menu_AI: /Seq-10.*Admin.*Menu/i.test(f2) && /Apriori/i.test(f2)
  },
  f3_ERD: {
    erDiagramBlock: /```mermaid\r?\nerDiagram/i.test(f3),
    tablesCount: (f3.match(/### Bảng \d+:/g) || []).length,
    deliveryFee20k: /20000/i.test(f3) && /delivery_fee/i.test(f3),
    wifiAttendance: /branch_wifi_configs/i.test(f3) && /bssid/i.test(f3) && /ip_subnet/i.test(f3),
    loyalty10Cups: /loyalty_cup_transactions/i.test(f3) && /cups_earned/i.test(f3),
    recipeBOM: /product_recipes/i.test(f3) && /quantity_required/i.test(f3),
    feedbackRating: /customer_feedbacks/i.test(f3) && /rating/i.test(f3),
    discrepancy50k: /shift_handover_discrepancies/i.test(f3) && /discrepancy_amount/i.test(f3)
  },
  f4_Deployment: {
    deploymentGraph: /```mermaid\r?\ngraph TB/i.test(f4),
    dockerComposeYaml: /```yaml[\s\S]*?services:[\s\S]*?backend:[\s\S]*?frontend:[\s\S]*?postgres:[\s\S]*?redis:[\s\S]*?nginx:/i.test(f4),
    nginxConfig: /```nginx[\s\S]*?upstream backend_api[\s\S]*?upstream frontend_app[\s\S]*?\/hubs\/[\s\S]*?proxy_set_header Upgrade/i.test(f4),
    githubActionsCiCd: /```yaml[\s\S]*?name:\s*CI\/CD Pipeline[\s\S]*?jobs:[\s\S]*?build-test:[\s\S]*?docker-build-push:[\s\S]*?deploy-vps:/i.test(f4),
    comparisonVpsVsAzure: /So Sánh.*VPS Linux.*Azure/i.test(f4)
  }
};

console.log(JSON.stringify(report, null, 2));