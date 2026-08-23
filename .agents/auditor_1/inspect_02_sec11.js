const fs = require('fs');

const f2 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\02_Sequence_Diagrams.md', 'utf8');
const lines2 = f2.split('\n');

console.log('--- Lines 840 to 920 of 02_Sequence_Diagrams.md: ---');
for (let i = 840; i < Math.min(920, lines2.length); i++) {
  console.log(`${i+1}: ${lines2[i]}`);
}