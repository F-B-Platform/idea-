const fs = require('fs');

const fDb = fs.readFileSync('d:\\Idea_DoAn\\03_Quy_Trinh_Trien_Khai\\02_Thiet_Ke_Database.md', 'utf8');
const lines02 = fDb.split('\n');

console.log('Lines 380-450 in 02_Thiet_Ke_Database.md:');
for (let i = 379; i < 450; i++) {
  console.log(`${i+1}: ${lines02[i]}`);
}