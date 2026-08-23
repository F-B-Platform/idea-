const fs = require('fs');

const f1 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\01_Kien_Truc_Tong_Quan.md', 'utf8');
const f2 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\02_Sequence_Diagrams.md', 'utf8');
const f3 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\03_ERD_Database_Diagram.md', 'utf8');
const f4 = fs.readFileSync('d:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\04_Deployment_Diagram.md', 'utf8');

console.log('--- 01_Kien_Truc_Tong_Quan.md Headers ---');
f1.split('\n').filter(l => l.startsWith('#')).forEach(l => console.log(l));

console.log('\n--- 02_Sequence_Diagrams.md Headers ---');
f2.split('\n').filter(l => l.startsWith('#')).forEach(l => console.log(l));

console.log('\n--- 04_Deployment_Diagram.md Headers ---');
f4.split('\n').filter(l => l.startsWith('#')).forEach(l => console.log(l));