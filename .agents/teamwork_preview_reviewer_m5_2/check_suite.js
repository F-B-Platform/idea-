const fs = require('fs');
const path = require('path');

const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.md'));

console.log('=== AUDITING 9 FILES FOR PROHIBITED TERMS & PLACEHOLDERS ===');
const prohibited = [
  { name: 'Flutter / React Native', regex: /flutter|react\s*native/i },
  { name: 'C-23 / C-24', regex: /\bC-2[3-9]\b|\bC-[3-9]\d\b/i },
  { name: 'GPS / Geofencing', regex: /\bGPS\b|geofenc/i },
  { name: 'Dynamic QR 30s', regex: /QR\s*30s|30\s*gi[aâ]y|xoay\s*v[oò]ng\s*30/i },
  { name: 'Separate Voucher / Calorie Screen', regex: /m[aà]n\s*h[iì]nh\s*(tra\s*c[uứ]u\s*)?calo\s*ri[eê]ng|v[ií]\s*voucher\s*ri[eê]ng/i },
  { name: 'Placeholder TODO', regex: /\bTODO\b/i },
  { name: 'Placeholder TBD', regex: /\bTBD\b/i },
  { name: 'Placeholder Code', regex: /\/\*\s*rest\s*of|\/\/\s*t[uư][oơ]ng\s*t[uư]|\/\/\s*gi[uữ]\s*nguy[eê]n/i }
];

files.forEach(f => {
  const filePath = path.join(dir, f);
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  
  lines.forEach((line, idx) => {
    prohibited.forEach(p => {
      if (p.regex.test(line)) {
        console.log(`[FOUND] ${f}:${idx+1} [${p.name}] => ${line.trim()}`);
      }
    });
  });
});

console.log('\n=== AUDITING FEATURE INVENTORY (C, S, M, A) IN 01_Phan_Tich_Yeu_Cau.md ===');
const f01 = fs.readFileSync(path.join(dir, '01_Phan_Tich_Yeu_Cau.md'), 'utf8');
const cMatches = f01.match(/\bC-\d{2}\b/g) || [];
const sMatches = f01.match(/\bS-\d{2}\b/g) || [];
const mMatches = f01.match(/\bM-\d{2}\b/g) || [];
const aMatches = f01.match(/\bA-\d{2}\b/g) || [];

const uniqueC = [...new Set(cMatches)].sort();
const uniqueS = [...new Set(sMatches)].sort();
const uniqueM = [...new Set(mMatches)].sort();
const uniqueA = [...new Set(aMatches)].sort();

console.log('Customer Features Count:', uniqueC.length, uniqueC.join(', '));
console.log('Staff Features Count:', uniqueS.length, uniqueS.join(', '));
console.log('Manager Features Count:', uniqueM.length, uniqueM.join(', '));
console.log('Admin Features Count:', uniqueA.length, uniqueA.join(', '));

console.log('\n=== AUDITING 25 DATABASE ENTITIES IN 02_Thiet_Ke_Database.md ===');
const f02 = fs.readFileSync(path.join(dir, '02_Thiet_Ke_Database.md'), 'utf8');
const tableMatches = f02.match(/CREATE TABLE\s+(?:IF NOT EXISTS\s+)?(\w+)/gi) || [];
const tables = tableMatches.map(t => t.replace(/CREATE TABLE\s+(?:IF NOT EXISTS\s+)?/i, '').trim());
console.log('Tables defined with CREATE TABLE count:', tables.length);
tables.forEach((t, i) => console.log(`  ${i+1}. ${t}`));

console.log('\n=== AUDITING 4 CORE BUSINESS ENGINES ACROSS ALL FILES ===');
const checks = [
  { name: 'Dine-In Prepay (Branch A)', regex: /nh[aá]nh\s*A.*tr[aả]\s*tr[uư][oớ]c|tr[aả]\s*tr[uư][oớ]c.*VietQR|DineIn.*Prepay/i },
  { name: 'Dine-In Postpay (Branch B + Bill QR)', regex: /nh[aá]nh\s*B.*tr[aả]\s*sau|tr[aả]\s*sau.*Bill\s*QR|DineIn.*Postpay/i },
  { name: 'Delivery (20k fee, 100% VietQR, no COD, phone+address)', regex: /20\.?000\s*(?:VND|đ).*VietQR|kh[oó]a\s*COD|delivery_fee/i },
  { name: 'Takeaway POS (no QR, phone CRM, 10 cups loyalty, postpay)', regex: /Takeaway.*qu[aầ]y|10\s*ly.*(?:t[aặ]ng|free)|LoyaltyCupTransactions/i },
  { name: 'WiFi Attendance (BSSID / IP Subnet + PIN)', regex: /BranchWifiConfigs|BSSID.*IP\s*Subnet|ch[aấ]m\s*c[oô]ng.*WiFi/i }
];

files.forEach(f => {
  const content = fs.readFileSync(path.join(dir, f), 'utf8');
  console.log(`\nChecking Business Engines in ${f}:`);
  checks.forEach(c => {
    const has = c.regex.test(content);
    console.log(`  ${has ? '✓' : '✗'} ${c.name}`);
  });
});
