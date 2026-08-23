const fs = require('fs');

const fErd = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md', 'utf8');
const lines03 = fErd.split('\n');

for (let i = 899; i < 930; i++) {
  console.log(`${i+1}: ${lines03[i]}`);
}