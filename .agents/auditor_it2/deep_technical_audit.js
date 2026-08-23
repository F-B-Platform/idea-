const fs = require('fs');
const path = require('path');

const targetDir = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams';
const doc01 = fs.readFileSync(path.join(targetDir, '01_Kien_Truc_Tong_Quan.md'), 'utf8');
const doc02 = fs.readFileSync(path.join(targetDir, '02_Sequence_Diagrams.md'), 'utf8');
const doc03 = fs.readFileSync(path.join(targetDir, '03_ERD_Database_Diagram.md'), 'utf8');
const doc04 = fs.readFileSync(path.join(targetDir, '04_Deployment_Diagram.md'), 'utf8');

const techAudit = {
  timestamp: new Date().toISOString(),
  routeGroups: {},
  signalRHubs: {},
  cleanArchitecture: {},
  databaseSchema: {},
  deploymentConfigs: {},
  allPassed: false
};

console.log('=== RUNNING REFINED DEEP TECHNICAL ARCHITECTURE AUDIT ===');

// 1. Route Groups: (customer), (pos), (kitchen), (admin), (auth)
const routeGroups = [
  { group: '(customer)', role: 'Customer PWA' },
  { group: '(pos)', role: 'Staff POS' },
  { group: '(kitchen)', role: 'Kitchen KDS' },
  { group: '(admin)', role: 'Admin & Manager' },
  { group: '(auth)', role: 'Central Auth' }
];

techAudit.routeGroups = {
  items: routeGroups.map(rg => ({
    ...rg,
    presentIn01: doc01.includes(rg.group),
    count: (doc01.match(new RegExp(rg.group.replace('(', '\\(').replace(')', '\\)'), 'g')) || []).length
  })),
  allPresent: routeGroups.every(rg => doc01.includes(rg.group))
};

// 2. 4 SignalR Hubs: OrderHub, KitchenHub, PaymentHub, NotificationHub
const signalRHubs = ['OrderHub', 'KitchenHub', 'PaymentHub', 'NotificationHub'];
techAudit.signalRHubs = {
  items: signalRHubs.map(h => ({
    hub: h,
    inDoc01: doc01.includes(h),
    inDoc02: doc02.includes(h),
    inDoc04: doc04.includes(h) || doc04.includes('/hubs/')
  })),
  allPresentIn01And02: signalRHubs.every(h => doc01.includes(h) && doc02.includes(h)),
  wsLocationIn04: doc04.includes('location /hubs/') || doc04.includes('WebSocket')
};

// 3. .NET 8 Clean Architecture
const cleanArchKeywords = [
  'Clean Architecture',
  'Domain Layer',
  'Application Layer',
  'Infrastructure Layer',
  'API',
  'MediatR',
  'FluentValidation',
  'Entity Framework Core',
  'Redis',
  'RedLock'
];
techAudit.cleanArchitecture = {
  items: cleanArchKeywords.map(k => ({ keyword: k, present: doc01.includes(k) })),
  allPresent: cleanArchKeywords.every(k => doc01.includes(k))
};

// 4. 31 Database Tables in 03_ERD_Database_Diagram.md
const tables31 = [
  'users', 'roles', 'user_roles', 'permissions', 'role_permissions', 'refresh_tokens',
  'branches', 'branch_wifi_configs', 'tables', 'table_qr_codes',
  'categories', 'products', 'product_sizes', 'toppings', 'product_toppings',
  'ingredients', 'product_recipes', 'inventory_stocks', 'inventory_logs',
  'orders', 'order_items', 'order_item_toppings', 'payments', 'transactions', 'delivery_orders',
  'customers', 'loyalty_cup_transactions', 'customer_feedbacks',
  'work_shifts', 'staff_attendances', 'shift_handover_discrepancies'
];

techAudit.databaseSchema = {
  totalEntitiesRequired: tables31.length,
  items: tables31.map(t => {
    const inDict = doc03.includes(`\`${t}\``) || doc03.includes(`Bảng `) && doc03.toLowerCase().includes(t);
    return { table: t, presentInDoc03: inDict };
  }),
  all31Found: tables31.every(t => doc03.includes(`\`${t}\``)),
  hasDeliveryAddress: /delivery_address/i.test(doc03),
  hasDeliveryFee: /delivery_fee/i.test(doc03),
  hasBranchWifiConfigs: /branch_wifi_configs/i.test(doc03),
  hasLoyaltyCups: /loyalty_cup_transactions/i.test(doc03),
  hasDiscrepancy50k: /50\.000/i.test(doc03) || /50000/i.test(doc03)
};

// 5. Deployment configs in 04_Deployment_Diagram.md
techAudit.deploymentConfigs = {
  hasPostgresService: doc04.includes('smartfb-postgres') && doc04.includes('postgres:16-alpine'),
  hasRedisService: doc04.includes('smartfb-redis') && doc04.includes('redis:7-alpine'),
  hasBackendService: doc04.includes('smartfb-backend') && doc04.includes('mcr.microsoft.com/dotnet/aspnet:8.0'),
  hasFrontendService: doc04.includes('smartfb-frontend') && doc04.includes('node:20-alpine'),
  hasNginxService: doc04.includes('smartfb-nginx') && doc04.includes('nginx:1.25-alpine'),
  hasNginxConf: doc04.includes('proxy_pass http://backend_upstream') && doc04.includes('proxy_pass http://frontend_upstream'),
  hasWebSocketUpgrade: doc04.includes('proxy_set_header Upgrade $http_upgrade') && doc04.includes('proxy_set_header Connection "upgrade"'),
  hasSSLConfig: doc04.includes('ssl_protocols TLSv1.2 TLSv1.3') && doc04.includes('ssl_certificate'),
  hasRateLimiting: doc04.includes('limit_req_zone') && doc04.includes('limit_req zone='),
  hasCI_CD: doc04.includes('.github/workflows/deploy.yml') && doc04.includes('dotnet test'),
  hasBackupScript: doc04.includes('backup_postgres.sh') && doc04.includes('pg_dump')
};

techAudit.allPassed = 
  techAudit.routeGroups.allPresent &&
  techAudit.signalRHubs.allPresentIn01And02 &&
  techAudit.cleanArchitecture.allPresent &&
  techAudit.databaseSchema.all31Found &&
  techAudit.deploymentConfigs.hasPostgresService &&
  techAudit.deploymentConfigs.hasRedisService &&
  techAudit.deploymentConfigs.hasBackendService &&
  techAudit.deploymentConfigs.hasFrontendService &&
  techAudit.deploymentConfigs.hasNginxService &&
  techAudit.deploymentConfigs.hasNginxConf &&
  techAudit.deploymentConfigs.hasWebSocketUpgrade &&
  techAudit.deploymentConfigs.hasSSLConfig &&
  techAudit.deploymentConfigs.hasRateLimiting &&
  techAudit.deploymentConfigs.hasCI_CD &&
  techAudit.deploymentConfigs.hasBackupScript;

fs.writeFileSync('d:\\Idea_DoAn\\.agents\\auditor_it2\\technical_audit_results.json', JSON.stringify(techAudit, null, 2), 'utf8');

console.log('Technical Audit All Passed:', techAudit.allPassed);
