const fs = require('fs');
const path = require('path');
const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.md'));

console.log('=== FORENSIC ZERO PLACEHOLDER AUDIT ===\n');

const placeholderPatterns = [
  { name: 'TODO', regex: /\btodo\b/i },
  { name: 'TBD', regex: /\btbd\b/i },
  { name: 'FIXME', regex: /\bfixme\b/i },
  { name: 'XXX', regex: /\bxxx\b/i },
  { name: 'Rest of code', regex: /\brest of\b/i },
  { name: 'Tuong tu', regex: /t[uư][oơ]ng\s*t[uư]\s*nh[uư]/i },
  { name: 'Giu nguyen', regex: /gi[uữ]\s*nguy[eê]n\s*logic/i },
  { name: 'Three Dots in Code', regex: /^(\s*(\/\/|\/\*|#|--)?\s*\.\.\.\s*(\*\/)?)$/ }
];

let totalIssues = 0;

files.forEach(f => {
  const content = fs.readFileSync(path.join(dir, f), 'utf8');
  const lines = content.split('\n');
  let fileIssues = 0;
  
  lines.forEach((line, idx) => {
    placeholderPatterns.forEach(p => {
      if (p.regex.test(line)) {
        console.log(`[ISSUE] ${f}:${idx+1} [${p.name}] => ${line.trim()}`);
        fileIssues++;
        totalIssues++;
      }
    });
  });
  
  console.log(`File ${f.padEnd(30)}: ${fileIssues === 0 ? '✓ ZERO PLACEHOLDERS (100% Complete)' : `✗ ${fileIssues} issues found`}`);
});

console.log(`\nTotal Placeholder Findings: ${totalIssues}`);
