const fs = require('fs');
const path = require('path');

const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const files = [
  '01_Phan_Tich_Yeu_Cau.md',
  '02_Thiet_Ke_Database.md',
  '03_Thiet_Ke_API_Contract.md',
  '04_Thiet_Ke_UI_UX.md',
  '05_Quy_Trinh_Backend.md',
  '06_Quy_Trinh_Frontend.md',
  '07_Ke_Hoach_Kiem_Thu.md',
  '08_Trien_Khai_He_Thong.md',
  'README.md'
];

files.forEach(f => {
  const content = fs.readFileSync(path.join(dir, f), 'utf8');
  console.log(`\n================================================================`);
  console.log(`FILE: ${f}`);
  console.log(`================================================================`);
  const lines = content.split('\n');
  const headers = lines.filter(l => /^#{1,3}\s+/.test(l));
  console.log(`Total Headers (${headers.length}):`);
  headers.slice(0, 20).forEach(h => console.log(`  ${h}`));
  if (headers.length > 20) {
    console.log(`  ... and ${headers.length - 20} more headers`);
  }
});
