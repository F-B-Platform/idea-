const fs = require('fs');

const f4 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\04_Deployment_Diagram.md', 'utf8');
const lines4 = f4.split('\n');

console.log('--- Lines 260 to 350 of 04_Deployment_Diagram.md: ---');
for (let i = 260; i < Math.min(350, lines4.length); i++) {
  console.log(`${i+1}: ${lines4[i]}`);
}