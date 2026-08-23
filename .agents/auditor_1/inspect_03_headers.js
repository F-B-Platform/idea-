const fs = require('fs');

const fErd = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md', 'utf8');
const lines03 = fErd.split('\n');

console.log('Headers in 03_ERD_Database_Diagram.md:');
lines03.forEach((l, idx) => {
  if (l.startsWith('# ') || l.startsWith('## ') || l.startsWith('### ')) {
    console.log(`${idx+1}: ${l}`);
  }
});