const fs = require('fs');

const f1 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\01_Kien_Truc_Tong_Quan.md', 'utf8');
const f4 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\04_Deployment_Diagram.md', 'utf8');

console.log('--- 01 Route groups check ---');
['(customer)', '(kds)', '(staff)', '(manager)', '(admin)'].forEach(g => {
  console.log(`Contains "${g}":`, f1.includes(g));
});

console.log('\n--- 01 RBAC check ---');
['Customer', 'Staff', 'Manager', 'ChainAdmin', 'Admin'].forEach(r => {
  console.log(`Contains role "${r}":`, f1.includes(r));
});

console.log('\n--- 04 Docker Compose & Nginx check ---');
console.log('Contains docker-compose.prod.yml:', f4.includes('docker-compose.prod.yml'));
console.log('Contains backend service in compose:', f4.includes('smartfb-backend') || f4.includes('backend:'));
console.log('Contains nginx.conf:', f4.includes('nginx.conf'));