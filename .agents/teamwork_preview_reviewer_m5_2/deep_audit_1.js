const fs = require('fs');
const path = require('path');

const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';

// 1. Check 01_Phan_Tich_Yeu_Cau.md
console.log('================================================================');
console.log('1. DEEP AUDIT: 01_Phan_Tich_Yeu_Cau.md');
console.log('================================================================');
const f01 = fs.readFileSync(path.join(dir, '01_Phan_Tich_Yeu_Cau.md'), 'utf8');

// Count FR definitions
const frRegex = /###\s+(?:FR-)?([CSMA]-\d{2}):\s*([^\n]+)/g;
let match;
const foundFRs = [];
while ((match = frRegex.exec(f01)) !== null) {
  foundFRs.push({ code: match[1], title: match[2].trim() });
}

console.log('Total Feature Definitions Found:', foundFRs.length);
const cFRs = foundFRs.filter(f => f.code.startsWith('C-'));
const sFRs = foundFRs.filter(f => f.code.startsWith('S-'));
const mFRs = foundFRs.filter(f => f.code.startsWith('M-'));
const aFRs = foundFRs.filter(f => f.code.startsWith('A-'));

console.log(`Customer FRs (${cFRs.length}):`, cFRs.map(f => f.code).join(', '));
console.log(`Staff FRs (${sFRs.length}):`, sFRs.map(f => f.code).join(', '));
console.log(`Manager FRs (${mFRs.length}):`, mFRs.map(f => f.code).join(', '));
console.log(`Admin FRs (${aFRs.length}):`, aFRs.map(f => f.code).join(', '));

// Check where C-23 / C-24 appear in f01
console.log('\nOccurrences of C-23 / C-24 in 01:');
f01.split('\n').forEach((line, i) => {
  if (/C-2[34]/.test(line)) {
    console.log(`  Line ${i+1}: ${line}`);
  }
});

// 2. Check 02_Thiet_Ke_Database.md
console.log('\n================================================================');
console.log('2. DEEP AUDIT: 02_Thiet_Ke_Database.md');
console.log('================================================================');
const f02 = fs.readFileSync(path.join(dir, '02_Thiet_Ke_Database.md'), 'utf8');

// Check 25 tables
const tableNames = [
  'branches', 'branch_wifi_configs', 'tables', 'users', 'roles', 'user_roles',
  'audit_logs', 'categories', 'products', 'product_sizes', 'product_branch_prices',
  'modifiers', 'product_modifiers', 'ingredients', 'recipes_bom', 'customers',
  'orders', 'order_items', 'order_item_modifiers', 'payments', 'loyalty_cup_transactions',
  'vouchers', 'customer_reviews', 'shifts', 'attendances'
];

console.log('Checking all 25 expected tables:');
tableNames.forEach((t, i) => {
  const hasCreate = new RegExp(`CREATE TABLE (?:IF NOT EXISTS )?${t}\\b`, 'i').test(f02);
  const hasDesc = new RegExp(`### 2\\.\\d+\\s+Bảng\\s+\`${t}\`|###.*\`${t}\``, 'i').test(f02);
  console.log(`  ${(i+1).toString().padStart(2)}. ${t.padEnd(26)}: CREATE TABLE: ${hasCreate ? '✓' : '✗'}, Section: ${hasDesc ? '✓' : '✗'}`);
});

// Check key fields in orders table
const ordersTableMatch = f02.match(/CREATE TABLE (?:IF NOT EXISTS )?orders\s*\(([\s\S]*?)\);/i);
if (ordersTableMatch) {
  console.log('\nOrders table fields check:');
  const ordersDef = ordersTableMatch[1];
  ['delivery_address', 'delivery_fee', 'order_type'].forEach(field => {
    const hasField = new RegExp(`\\b${field}\\b`, 'i').test(ordersDef);
    console.log(`  - ${field}: ${hasField ? '✓' : '✗'}`);
  });
}

// Check branch_wifi_configs table
const wifiTableMatch = f02.match(/CREATE TABLE (?:IF NOT EXISTS )?branch_wifi_configs\s*\(([\s\S]*?)\);/i);
if (wifiTableMatch) {
  console.log('\nbranch_wifi_configs fields check:');
  const wifiDef = wifiTableMatch[1];
  ['bssid', 'ip_subnet', 'branch_id'].forEach(field => {
    const hasField = new RegExp(`\\b${field}\\b`, 'i').test(wifiDef);
    console.log(`  - ${field}: ${hasField ? '✓' : '✗'}`);
  });
}

// Check loyalty_cup_transactions table
const loyaltyTableMatch = f02.match(/CREATE TABLE (?:IF NOT EXISTS )?loyalty_cup_transactions\s*\(([\s\S]*?)\);/i);
if (loyaltyTableMatch) {
  console.log('\nloyalty_cup_transactions fields check:');
  const loyaltyDef = loyaltyTableMatch[1];
  ['customer_id', 'order_id', 'cups_added', 'cups_redeemed', 'cups_balance_after'].forEach(field => {
    const hasField = new RegExp(`\\b${field}\\b`, 'i').test(loyaltyDef);
    console.log(`  - ${field}: ${hasField ? '✓' : '✗'}`);
  });
}

// 3. Check 03_Thiet_Ke_API_Contract.md
console.log('\n================================================================');
console.log('3. DEEP AUDIT: 03_Thiet_Ke_API_Contract.md');
console.log('================================================================');
const f03 = fs.readFileSync(path.join(dir, '03_Thiet_Ke_API_Contract.md'), 'utf8');

// Check 10 API Groups
const apiGroups = [
  'Auth', 'Branch', 'Table', 'Product', 'Order', 'Payment',
  'Attendance', 'KDS', 'Manager', 'Admin'
];
console.log('Checking API Groups in 03:');
apiGroups.forEach(g => {
  const has = new RegExp(g, 'i').test(f03);
  console.log(`  - Group ${g}: ${has ? '✓' : '✗'}`);
});

// Check endpoints in 03
const endpoints = f03.match(/`?(?:POST|GET|PUT|DELETE|PATCH)\s+\/api\/v1\/[^\s`]+/gi) || [];
console.log(`Total Endpoints defined: ${endpoints.length}`);
console.log('Sample endpoints:');
endpoints.slice(0, 10).forEach(e => console.log(`  ${e}`));

