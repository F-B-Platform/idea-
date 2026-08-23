const fs = require('fs');

const fDb = fs.readFileSync('d:\\Idea_DoAn\\03_Quy_Trinh_Trien_Khai\\02_Thiet_Ke_Database.md', 'utf8');
const fErd = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md', 'utf8');

// Match table names in 02_Thiet_Ke_Database.md
const tablesIn02 = [];
const lines02 = fDb.split('\n');
lines02.forEach(l => {
  const m = l.match(/### Bảng \d+: `([a-z_]+)`/i) || l.match(/### Bảng [0-9A-Za-z_]+: `([a-z_]+)`/i);
  if (m) tablesIn02.push(m[1]);
});

// Match table names in 03_ERD_Database_Diagram.md
const tablesIn03 = [];
const lines03 = fErd.split('\n');
lines03.forEach(l => {
  const m = l.match(/### Bảng \d+: `([a-z_]+)`/i) || l.match(/### Bảng [0-9A-Za-z_]+: `([a-z_]+)`/i);
  if (m) tablesIn03.push(m[1]);
});

console.log('Tables in 02_Thiet_Ke_Database.md (' + tablesIn02.length + '):', tablesIn02);
console.log('Tables in 03_ERD_Database_Diagram.md (' + tablesIn03.length + '):', tablesIn03);