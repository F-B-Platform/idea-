const fs = require('fs');

const f3 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md', 'utf8');
const lines = f3.split('\n');

console.log('Lines 540-580 of 03_ERD_Database_Diagram.md:');
for (let i = 535; i < Math.min(580, lines.length); i++) {
  console.log(`${i+1}: ${lines[i]}`);
}