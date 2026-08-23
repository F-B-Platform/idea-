const fs = require('fs');
const path = require('path');

const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const files = [
  '01_Phan_Tich_Yeu_Cau.md',
  '02_Thiet_Ke_Database.md',
  '03_Thiet_Ke_API_Contract.md',
  '04_Thiet_Ke_UI_UX.md',
  '05_Quy_Trinh_Backend.md',
  '06_Quy_Trinh_Frontend.md',
  '07_Ke_Hoach_Kiem_Thu.md',
  '08_Trien_Khai_He_Thong.md',
  'README.md'
];

console.log('================================================================');
console.log('AUDIT OF ALL 9 FILES IN 03_Quy_Trinh_Trien_Khai/');
console.log('================================================================\n');

// 1. Audit File Size & Line Counts
console.log('--- 1. File Statistics ---');
files.forEach(f => {
  const p = path.join(dir, f);
  if (!fs.existsSync(p)) {
    console.log(`[MISSING] ${f}`);
    return;
  }
  const content = fs.readFileSync(p, 'utf8');
  const lines = content.split('\n');
  console.log(`- ${f.padEnd(28)}: ${content.length.toString().padStart(6)} chars | ${lines.length.toString().padStart(5)} lines`);
});

// 2. Audit 62 Feature Traceability Across All Files
console.log('\n--- 2. Feature Mentions Traceability Across Files ---');
const allFeatures = [];
for (let i = 1; i <= 20; i++) allFeatures.push(`C-${i.toString().padStart(2, '0')}`);
for (let i = 1; i <= 13; i++) allFeatures.push(`S-${i.toString().padStart(2, '0')}`);
for (let i = 1; i <= 12; i++) allFeatures.push(`M-${i.toString().padStart(2, '0')}`);
for (let i = 1; i <= 17; i++) allFeatures.push(`A-${i.toString().padStart(2, '0')}`);

console.log(`Total expected feature codes: ${allFeatures.length} (20 C, 13 S, 12 M, 17 A)`);

files.forEach(f => {
  const content = fs.readFileSync(path.join(dir, f), 'utf8');
  const found = allFeatures.filter(code => new RegExp(`\\b${code}\\b`).test(content));
  console.log(`- ${f.padEnd(28)}: mentions ${found.length.toString().padStart(2)} / 62 feature codes`);
});

// 3. Check 04_Thiet_Ke_UI_UX.md Wireframes & Route Groups
console.log('\n--- 3. UI/UX Route Groups & Wireframes (04) ---');
const f04 = fs.readFileSync(path.join(dir, '04_Thiet_Ke_UI_UX.md'), 'utf8');
const routeGroups = ['(customer)', '(staff)', '(manager)', '(admin)', '(kds)'];
routeGroups.forEach(rg => {
  const has = f04.includes(rg);
  console.log(`- Route Group ${rg.padEnd(12)}: ${has ? '✓ Present' : '✗ Missing'}`);
});
const wireframes = f04.match(/Khung Giao Diện|ASCII Wireframe|Wireframe/gi) || [];
console.log(`- Wireframe sections / mentions count: ${wireframes.length}`);

// 4. Check 05_Quy_Trinh_Backend.md Clean Architecture & Core Engines
console.log('\n--- 4. Backend Components (05) ---');
const f05 = fs.readFileSync(path.join(dir, '05_Quy_Trinh_Backend.md'), 'utf8');
const backendChecks = [
  'Clean Architecture 4 lớp',
  'MediatR',
  'FluentValidation',
  'OrderHub',
  'KitchenHub',
  'PaymentHub',
  'NotificationHub',
  'Redis Distributed Lock',
  'Gemini 1.5 Flash',
  'Apriori',
  'PayOS Webhook',
  'Branch A Prepay vs Branch B Postpay',
  'Delivery 20,000 VND VietQR',
  'Takeaway 10 Cups Loyalty',
  'WiFi Attendance BSSID'
];
backendChecks.forEach(bc => {
  const has = new RegExp(bc.replace(/[\(\)]/g, '\\$&').replace(/\s+/g, '[\\s_]+'), 'i').test(f05);
  console.log(`- ${bc.padEnd(36)}: ${has ? '✓ Present' : '✗ Missing'}`);
});

// 5. Check 06_Quy_Trinh_Frontend.md Next.js & Stores
console.log('\n--- 5. Frontend Components (06) ---');
const f06 = fs.readFileSync(path.join(dir, '06_Quy_Trinh_Frontend.md'), 'utf8');
const feChecks = [
  'Next.js 14 App Router',
  'Zustand Stores',
  'CartStore',
  'PosStore',
  'ShiftStore',
  'SignalR Hooks',
  'Service Worker Offline Menu',
  'Tailwind CSS',
  'Shadcn UI',
  'TanStack Query'
];
feChecks.forEach(fc => {
  const has = new RegExp(fc.replace(/[\(\)]/g, '\\$&').replace(/\s+/g, '[\\s_]+'), 'i').test(f06);
  console.log(`- ${fc.padEnd(36)}: ${has ? '✓ Present' : '✗ Missing'}`);
});

// 6. Check 07_Ke_Hoach_Kiem_Thu.md Test Suites
console.log('\n--- 6. Test Suites (07) ---');
const f07 = fs.readFileSync(path.join(dir, '07_Ke_Hoach_Kiem_Thu.md'), 'utf8');
const testChecks = [
  'Unit Test',
  'Integration Test',
  'UAT Test Cases',
  'Dine-In 2 nhánh',
  'Delivery 20k',
  'Takeaway 10 ly',
  'SignalR Load Test',
  'RBAC Security Test',
  '10 Edge Cases'
];
testChecks.forEach(tc => {
  const has = new RegExp(tc.replace(/[\(\)]/g, '\\$&').replace(/\s+/g, '[\\s_]+'), 'i').test(f07);
  console.log(`- ${tc.padEnd(36)}: ${has ? '✓ Present' : '✗ Missing'}`);
});

// 7. Check 08_Trien_Khai_He_Thong.md Deployment
console.log('\n--- 7. Deployment Components (08) ---');
const f08 = fs.readFileSync(path.join(dir, '08_Trien_Khai_He_Thong.md'), 'utf8');
const deployChecks = [
  'Docker Compose',
  'NGINX Reverse Proxy',
  'SSL Let\'s Encrypt',
  'GitHub Actions CI/CD',
  'PostgreSQL Container',
  'Redis Container',
  'Backend .NET 8 Container',
  'Frontend Next.js Container'
];
deployChecks.forEach(dc => {
  const has = new RegExp(dc.replace(/[\(\)\']/g, '\\$&').replace(/\s+/g, '[\\s_]+'), 'i').test(f08);
  console.log(`- ${dc.padEnd(36)}: ${has ? '✓ Present' : '✗ Missing'}`);
});

// 8. Check README.md
console.log('\n--- 8. README Overview & Navigation Table ---');
const readme = fs.readFileSync(path.join(dir, 'README.md'), 'utf8');
const readmeChecks = [
  '01_Phan_Tich_Yeu_Cau.md',
  '02_Thiet_Ke_Database.md',
  '03_Thiet_Ke_API_Contract.md',
  '04_Thiet_Ke_UI_UX.md',
  '05_Quy_Trinh_Backend.md',
  '06_Quy_Trinh_Frontend.md',
  '07_Ke_Hoach_Kiem_Thu.md',
  '08_Trien_Khai_He_Thong.md',
  '62 tính năng',
  '25 bảng',
  '4 Actor'
];
readmeChecks.forEach(rc => {
  const has = new RegExp(rc.replace(/[\(\)\.]/g, '\\$&').replace(/\s+/g, '[\\s_]+'), 'i').test(readme);
  console.log(`- ${rc.padEnd(36)}: ${has ? '✓ Present' : '✗ Missing'}`);
});
