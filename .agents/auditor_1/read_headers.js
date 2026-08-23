const fs = require('fs');

const fDb = fs.readFileSync('d:\\Idea_DoAn\\03_Quy_Trinh_Trien_Khai\\02_Thiet_Ke_Database.md', 'utf8');
const lines02 = fDb.split('\n');

console.log('Headers with ### in 02_Thiet_Ke_Database.md:');
lines02.forEach((l, idx) => {
  if (l.startsWith('### ') || l.startsWith('## ') || l.startsWith('# ')) {
    console.log(`${idx+1}: ${l}`);
  }
});