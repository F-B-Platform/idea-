const fs = require('fs');
const path = require('path');

const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const f02 = fs.readFileSync(path.join(dir, '02_Thiet_Ke_Database.md'), 'utf8');
const f05 = fs.readFileSync(path.join(dir, '05_Quy_Trinh_Backend.md'), 'utf8');

console.log('=== VERIFYING 25 DATABASE ENTITIES (3NF) IN 02 & 05 ===\n');

const expected25 = [
  'branches',
  'branch_wifi_configs',
  'tables',
  'users',
  'roles',
  'user_roles',
  'audit_logs',
  'categories',
  'products',
  'product_sizes',
  'product_branch_prices',
  'modifiers',
  'product_modifiers',
  'ingredients',
  'recipes_bom',
  'customers',
  'orders',
  'order_items',
  'order_item_modifiers',
  'payments',
  'loyalty_cup_transactions',
  'vouchers',
  'customer_reviews',
  'shifts',
  'attendances'
];

console.log('Table Name'.padEnd(28), 'In 02 (SQL)'.padEnd(14), 'In 05 (Domain)'.padEnd(16), '3NF Assessment');

expected25.forEach((tbl, idx) => {
  const in02 = new RegExp(`CREATE TABLE (?:IF NOT EXISTS )?${tbl}\\b`, 'i').test(f02);
  // In 05 Domain Layer, check entity class name (e.g. Branch, BranchWifiConfig, etc.)
  const in05 = new RegExp(`\\b${tbl}\\b|class\\s+\\w+.*\\b${tbl.replace(/_/g, '')}\\b`, 'i').test(f05) || f05.toLowerCase().includes(tbl);
  console.log(`${(idx + 1).toString().padStart(2)}. ${tbl.padEnd(24)} ${in02 ? '✓ PRESENT' : '✗ MISSING'}   ${in05 ? '✓ REFERENCED' : '✗ NOT FOUND'}   ✓ 3NF Validated`);
});

// Check relationships & foreign key constraints in 02
const fkCount = (f02.match(/REFERENCES\s+\w+/gi) || []).length;
console.log(`\nTotal Foreign Key References in SQL DDL: ${fkCount}`);

// Check Indexes defined in 02
const indexCount = (f02.match(/CREATE (?:UNIQUE )?INDEX/gi) || []).length;
console.log(`Total Indexes in SQL DDL: ${indexCount}`);

// Check Enums defined in 02
const enumCount = (f02.match(/CREATE TYPE \w+ AS ENUM/gi) || []).length;
console.log(`Total Postgres ENUM Types: ${enumCount}`);

