const fs = require('fs');
const path = require('path');

const doc03Path = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md';
const content = fs.readFileSync(doc03Path, 'utf8');

// 1. Extract erDiagram block
const erdBlockMatch = content.match(/```mermaid\r?\nerDiagram([\s\S]*?)```/);
if (!erdBlockMatch) {
  console.error('No erDiagram block found in 03_ERD_Database_Diagram.md');
  process.exit(1);
}

const erdContent = erdBlockMatch[1];

// Find all entity definitions in erDiagram (e.g. USERS {, BRANCHES {, etc.)
const entityRegex = /^\s*([A-Za-z0-9_]+)\s*\{/gm;
const entitiesInDiagram = [];
let match;
while ((match = entityRegex.exec(erdContent)) !== null) {
  entitiesInDiagram.push(match[1]);
}

console.log(`Found ${entitiesInDiagram.length} entities in Mermaid erDiagram:`);
console.log(entitiesInDiagram.join(', '));

// 2. Check required 25 core entities / tables from R3 in ORIGINAL_REQUEST.md:
// Khách hàng & CRM: Users, Customers, LoyaltyCupTransactions, Reviews, ReviewImages
// Chi nhánh & Bàn: Branches, BranchWifiConfigs, Tables, PriceGroups
// Thực đơn & BOM: Categories, Products, ProductModifiers, ProductBOMs, Ingredients, InventoryTransactions
// Đơn hàng & Thanh toán: Orders, OrderItems, Payments, PayOSTransactions, Vouchers
// Vận hành & Nhân sự: Attendances, StaffShifts, CashShifts, ZReports, AuditLogs

const required25 = [
  { group: 'Khách hàng & CRM', tables: ['Users', 'Customers', 'LoyaltyCupTransactions', 'Reviews', 'ReviewImages'] },
  { group: 'Chi nhánh & Bàn', tables: ['Branches', 'BranchWifiConfigs', 'Tables', 'PriceGroups'] },
  { group: 'Thực đơn & BOM', tables: ['Categories', 'Products', 'ProductModifiers', 'ProductBOMs', 'Ingredients', 'InventoryTransactions'] },
  { group: 'Đơn hàng & Thanh toán', tables: ['Orders', 'OrderItems', 'Payments', 'PayOSTransactions', 'Vouchers'] },
  { group: 'Vận hành & Nhân sự', tables: ['Attendances', 'StaffShifts', 'CashShifts', 'ZReports', 'AuditLogs'] }
];

console.log('\n--- Checking 25 Required Tables Against ERD & Dictionary ---');
let allFound = true;
const detailedChecks = [];

required25.forEach(g => {
  console.log(`\nGroup: ${g.group}`);
  g.tables.forEach(t => {
    // Check if table or singular/plural equivalent exists in diagram or markdown text
    const inDiagram = entitiesInDiagram.some(e => 
      e.toLowerCase() === t.toLowerCase() || 
      e.toLowerCase() === t.toLowerCase().replace(/s$/, '') ||
      e.toLowerCase() === t.toLowerCase() + 's' ||
      e.toLowerCase().replace(/_/g, '') === t.toLowerCase().replace(/_/g, '')
    );
    
    // Check in text dictionary
    const inText = new RegExp(`### \\d+\\.\\d+\\s+Bảng\\s+\`?([a-z0-9_]+)\`?`, 'gi');
    let textMatch = false;
    let tm;
    while ((tm = inText.exec(content)) !== null) {
      const foundName = tm[1].toLowerCase().replace(/_/g, '');
      const reqName = t.toLowerCase().replace(/_/g, '');
      if (foundName === reqName || foundName === reqName.replace(/s$/, '') || foundName + 's' === reqName) {
        textMatch = true;
        break;
      }
    }

    const passed = inDiagram || textMatch;
    if (!passed) allFound = false;
    console.log(` - ${t}: Diagram=${inDiagram ? 'YES' : 'NO'}, Dict=${textMatch ? 'YES' : 'NO'} => ${passed ? 'OK' : 'MISSING'}`);
    detailedChecks.push({ table: t, group: g.group, inDiagram, inText: textMatch, passed });
  });
});

// Specific constraints verification
const checks = {
  hasDeliveryAddress: /delivery_address/i.test(content),
  hasDeliveryFee: /delivery_fee/i.test(content),
  hasOrderType: /order_type/i.test(content),
  hasWifiBSSID: /bssid/i.test(content),
  hasWifiSubnet: /ip_subnet/i.test(content) || /subnet/i.test(content),
  has10CupsLoyalty: /cups_earned/i.test(content) || /loyalty/i.test(content),
  hasZReportDiscrepancy: /discrepancy/i.test(content) || /chenh_lech/i.test(content),
  hasNoGPSAttendance: !/attendance.*gps/i.test(content),
  hasNoQR30s: !/qr_code_30s|qr_dynamic_30s/i.test(content)
};

console.log('\n--- Specific Field & Integrity Constraint Checks ---');
console.log(JSON.stringify(checks, null, 2));

const report = {
  totalEntitiesInDiagram: entitiesInDiagram.length,
  entitiesInDiagram,
  all25Found: allFound,
  detailedChecks,
  constraintsChecks: checks
};

fs.writeFileSync('d:\\Idea_DoAn\\.agents\\auditor_it2\\erd_audit_report.json', JSON.stringify(report, null, 2), 'utf8');
console.log('\nERD audit report saved to erd_audit_report.json');
