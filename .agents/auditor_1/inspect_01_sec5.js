const fs = require('fs');

const f1 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\01_Kien_Truc_Tong_Quan.md', 'utf8');
const lines1 = f1.split('\n');

console.log('--- Lines 290 to 365 of 01_Kien_Truc_Tong_Quan.md: ---');
for (let i = 290; i < Math.min(365, lines1.length); i++) {
  console.log(`${i+1}: ${lines1[i]}`);
}