const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const targetDir = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams';
const tempMmdDir = 'd:\\Idea_DoAn\\.agents\\auditor_1\\temp_mmd';
const configFile = 'd:\\Idea_DoAn\\.agents\\auditor_1\\puppeteerConfig.json';

if (!fs.existsSync(tempMmdDir)) {
  fs.mkdirSync(tempMmdDir, { recursive: true });
}

const files = [
  '01_Kien_Truc_Tong_Quan.md',
  '02_Sequence_Diagrams.md',
  '03_ERD_Database_Diagram.md',
  '04_Deployment_Diagram.md'
];

let items = [];

files.forEach(filename => {
  const filePath = path.join(targetDir, filename);
  const content = fs.readFileSync(filePath, 'utf8');
  
  const mermaidRegex = /```mermaid\r?\n([\s\S]*?)```/g;
  let mMatch;
  let bIdx = 0;
  while ((mMatch = mermaidRegex.exec(content)) !== null) {
    bIdx++;
    const code = mMatch[1].trim();
    const prefix = filename.replace('.md', '');
    const mmdName = `${prefix}_b${bIdx < 10 ? '0' + bIdx : bIdx}.mmd`;
    const svgName = `${prefix}_b${bIdx < 10 ? '0' + bIdx : bIdx}.svg`;
    const mmdPath = path.join(tempMmdDir, mmdName);
    const svgPath = path.join(tempMmdDir, svgName);
    
    fs.writeFileSync(mmdPath, code, 'utf8');
    items.push({ filename, blockIndex: bIdx, mmdName, svgName, mmdPath, svgPath });
  }
});

console.log(`Extracted ${items.length} total Mermaid diagram files.\n`);

let results = [];
items.forEach((item, index) => {
  const startTime = Date.now();
  try {
    execSync(`npx -y @mermaid-js/mermaid-cli -p "${configFile}" -i "${item.mmdPath}" -o "${item.svgPath}"`, {
      stdio: 'pipe',
      timeout: 35000
    });
    const elapsed = Date.now() - startTime;
    const stat = fs.statSync(item.svgPath);
    console.log(`[${index + 1}/${items.length}] PASS: ${item.mmdName} (${stat.size} bytes, ${elapsed}ms)`);
    results.push({ ...item, status: 'PASS', size: stat.size, timeMs: elapsed });
  } catch (err) {
    const elapsed = Date.now() - startTime;
    console.error(`[${index + 1}/${items.length}] FAIL: ${item.mmdName} (${elapsed}ms)`);
    if (err.stderr) console.error(err.stderr.toString());
    results.push({ ...item, status: 'FAIL', error: err.message, timeMs: elapsed });
  }
});

const summary = {
  total: results.length,
  passed: results.filter(r => r.status === 'PASS').length,
  failed: results.filter(r => r.status === 'FAIL').length,
  details: results
};

fs.writeFileSync('d:\\Idea_DoAn\\.agents\\auditor_1\\all_render_results.json', JSON.stringify(summary, null, 2), 'utf8');

console.log(`\n==============================================`);
console.log(`FULL MERMAID TEST SUITE: Total=${summary.total}, Passed=${summary.passed}, Failed=${summary.failed}`);
console.log(`==============================================`);