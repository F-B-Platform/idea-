const fs = require('fs');
const path = require('path');
const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.md'));

console.log('=== FORENSIC PROHIBITION AUDIT ===\n');

const prohibitedAudit = [
  { term: 'Flutter', pattern: /flutter/i },
  { term: 'React Native', pattern: /react\s*native/i },
  { term: 'GPS', pattern: /\bgps\b/i },
  { term: 'Geofencing', pattern: /geofenc/i },
  { term: 'QR 30s', pattern: /30\s*gi[aâ]y|qr\s*30s|xoay\s*v[oò]ng\s*30/i },
  { term: 'C-23', pattern: /\bC-23\b/i },
  { term: 'C-24', pattern: /\bC-24\b/i },
  { term: 'Standalone Calorie', pattern: /tra\s*c[uứ]u\s*calo\s*ri[eê]ng|m[aà]n\s*h[iì]nh\s*calo/i },
  { term: 'Standalone Voucher Wallet', pattern: /v[ií]\s*voucher\s*ri[eê]ng/i }
];

files.forEach(f => {
  const content = fs.readFileSync(path.join(dir, f), 'utf8');
  const lines = content.split('\n');
  lines.forEach((line, idx) => {
    prohibitedAudit.forEach(p => {
      if (p.pattern.test(line)) {
        console.log(`[${f}:${idx+1}] [${p.term}] => ${line.trim()}`);
      }
    });
  });
});
