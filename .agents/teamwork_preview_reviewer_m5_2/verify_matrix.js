const fs = require('fs');
const path = require('path');

const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';

const features = {
  C: Array.from({ length: 20 }, (_, i) => `C-${(i + 1).toString().padStart(2, '0')}`),
  S: Array.from({ length: 13 }, (_, i) => `S-${(i + 1).toString().padStart(2, '0')}`),
  M: Array.from({ length: 12 }, (_, i) => `M-${(i + 1).toString().padStart(2, '0')}`),
  A: Array.from({ length: 17 }, (_, i) => `A-${(i + 1).toString().padStart(2, '0')}`)
};

const allFeatures = [...features.C, ...features.S, ...features.M, ...features.A];
console.log('Total Features to verify:', allFeatures.length);

const filesToCheck = [
  '01_Phan_Tich_Yeu_Cau.md',
  '03_Thiet_Ke_API_Contract.md',
  '04_Thiet_Ke_UI_UX.md',
  '07_Ke_Hoach_Kiem_Thu.md',
  'README.md'
];

const matrix = {};

allFeatures.forEach(feat => {
  matrix[feat] = {};
  filesToCheck.forEach(f => {
    const content = fs.readFileSync(path.join(dir, f), 'utf8');
    const regex = new RegExp(`\\b${feat}\\b`);
    matrix[feat][f] = regex.test(content);
  });
});

console.log('=== FEATURE TRACEABILITY MATRIX ACROSS 5 CORE FILES ===');
console.log('Feature'.padEnd(8), filesToCheck.map(f => f.slice(0, 10).padEnd(12)).join(' '));
let allPresent = true;
allFeatures.forEach(feat => {
  const row = filesToCheck.map(f => (matrix[feat][f] ? '✓ PASS' : '✗ FAIL').padEnd(12)).join(' ');
  console.log(feat.padEnd(8), row);
  filesToCheck.forEach(f => {
    if (!matrix[feat][f]) {
      console.log(`[ALERT] Missing ${feat} in ${f}`);
      allPresent = false;
    }
  });
});

console.log('\nResult of 62 Feature Traceability Matrix:', allPresent ? '100% PERFECT PASS' : 'FAILURES DETECTED');

