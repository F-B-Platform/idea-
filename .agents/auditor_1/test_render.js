const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const targetDir = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams';
const tempMmdDir = 'd:\\Idea_DoAn\\.agents\\auditor_1\\temp_mmd';

if (!fs.existsSync(tempMmdDir)) {
  fs.mkdirSync(tempMmdDir, { recursive: true });
}

const files = [
  '01_Kien_Truc_Tong_Quan.md',
  '02_Sequence_Diagrams.md',
  '03_ERD_Database_Diagram.md',
  '04_Deployment_Diagram.md'
];

let index = 0;
let renderResults = [];

files.forEach(filename => {
  const filePath = path.join(targetDir, filename);
  const content = fs.readFileSync(filePath, 'utf8');
  
  const mermaidRegex = /```mermaid\r?\n([\s\S]*?)```/g;
  let mMatch;
  let bIdx = 0;
  while ((mMatch = mermaidRegex.exec(content)) !== null) {
    bIdx++;
    index++;
    const code = mMatch[1].trim();
    const mmdName = `${filename.replace('.md','')}_b${bIdx}.mmd`;
    const svgName = `${filename.replace('.md','')}_b${bIdx}.svg`;
    const mmdPath = path.join(tempMmdDir, mmdName);
    const svgPath = path.join(tempMmdDir, svgName);
    
    fs.writeFileSync(mmdPath, code, 'utf8');
    
    try {
      // Execute mmdc compile
      execSync(`npx -y @mermaid-js/mermaid-cli -i "${mmdPath}" -o "${svgPath}"`, {
        stdio: 'pipe',
        timeout: 30000
      });
      const svgSize = fs.statSync(svgPath).size;
      console.log(`[PASS] ${mmdName} -> SVG generated (${svgSize} bytes)`);
      renderResults.push({ file: mmdName, status: 'PASS', size: svgSize });
    } catch (err) {
      console.error(`[FAIL] ${mmdName} -> Error: ${err.message}`);
      if (err.stderr) console.error(err.stderr.toString());
      renderResults.push({ file: mmdName, status: 'FAIL', error: err.message });
    }
  }
});

console.log('\n--- SUMMARY ---');
console.log(`Total Diagrams: ${renderResults.length}`);
console.log(`Passed: ${renderResults.filter(r => r.status === 'PASS').length}`);
console.log(`Failed: ${renderResults.filter(r => r.status === 'FAIL').length}`);