const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const tempMmdDir = 'd:\\Idea_DoAn\\.agents\\auditor_1\\temp_mmd';
const configFile = 'd:\\Idea_DoAn\\.agents\\auditor_1\\puppeteerConfig.json';

const mmdFiles = fs.readdirSync(tempMmdDir).filter(f => f.endsWith('.mmd')).sort();

let results = [];

console.log(`Starting render of ${mmdFiles.length} Mermaid diagrams...\n`);

mmdFiles.forEach((file, index) => {
  const mmdPath = path.join(tempMmdDir, file);
  const svgPath = path.join(tempMmdDir, file.replace('.mmd', '.svg'));
  
  const startTime = Date.now();
  try {
    execSync(`npx -y @mermaid-js/mermaid-cli -p "${configFile}" -i "${mmdPath}" -o "${svgPath}"`, {
      stdio: 'pipe',
      timeout: 30000
    });
    const elapsed = Date.now() - startTime;
    const stat = fs.statSync(svgPath);
    console.log(`[${index + 1}/${mmdFiles.length}] PASS: ${file} -> SVG (${stat.size} bytes, ${elapsed}ms)`);
    results.push({ file, status: 'PASS', size: stat.size, timeMs: elapsed });
  } catch (err) {
    const elapsed = Date.now() - startTime;
    console.error(`[${index + 1}/${mmdFiles.length}] FAIL: ${file} (${elapsed}ms)`);
    if (err.stderr) console.error(err.stderr.toString());
    results.push({ file, status: 'FAIL', error: err.message, timeMs: elapsed });
  }
});

const summary = {
  total: results.length,
  passed: results.filter(r => r.status === 'PASS').length,
  failed: results.filter(r => r.status === 'FAIL').length,
  details: results
};

fs.writeFileSync('d:\\Idea_DoAn\\.agents\\auditor_1\\render_report.json', JSON.stringify(summary, null, 2), 'utf8');

console.log(`\n========================================`);
console.log(`RENDER SUMMARY: Total=${summary.total}, Passed=${summary.passed}, Failed=${summary.failed}`);
console.log(`========================================`);