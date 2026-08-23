const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const tempMmdDir = 'd:\\Idea_DoAn\\.agents\\auditor_it2\\temp_mmd';
const puppeteerConfig = 'd:\\Idea_DoAn\\.agents\\auditor_it2\\puppeteerConfig.json';
const renderReportPath = 'd:\\Idea_DoAn\\.agents\\auditor_it2\\render_report.json';

const mmdFiles = fs.readdirSync(tempMmdDir).filter(f => f.endsWith('.mmd')).sort();

console.log(`Starting render tests for ${mmdFiles.length} Mermaid diagrams...`);

const results = [];
let passCount = 0;
let failCount = 0;

for (const mmdFile of mmdFiles) {
  const mmdPath = path.join(tempMmdDir, mmdFile);
  const svgPath = path.join(tempMmdDir, mmdFile.replace('.mmd', '.svg'));
  
  const mmdContent = fs.readFileSync(mmdPath, 'utf8');
  const firstLine = mmdContent.split('\n')[0].trim();
  const lineCount = mmdContent.split('\n').length;
  
  const startTime = Date.now();
  let status = 'PASS';
  let errorMsg = null;
  let svgSize = 0;

  try {
    const cmd = `npx @mermaid-js/mermaid-cli -i "${mmdPath}" -o "${svgPath}" -p "${puppeteerConfig}" --quiet`;
    execSync(cmd, { stdio: 'pipe', timeout: 30000 });
    
    if (fs.existsSync(svgPath)) {
      const svgStat = fs.statSync(svgPath);
      svgSize = svgStat.size;
      if (svgSize === 0) {
        status = 'FAIL';
        errorMsg = 'Generated SVG file is 0 bytes';
      }
    } else {
      status = 'FAIL';
      errorMsg = 'SVG file was not generated';
    }
  } catch (err) {
    status = 'FAIL';
    errorMsg = err.stderr ? err.stderr.toString() : err.message;
  }

  const durationMs = Date.now() - startTime;
  
  if (status === 'PASS') {
    passCount++;
    console.log(`[PASS] ${mmdFile} | SVG: ${svgSize.toLocaleString()} bytes | ${durationMs}ms | ${firstLine}`);
  } else {
    failCount++;
    console.error(`[FAIL] ${mmdFile} | Error: ${errorMsg}`);
  }

  results.push({
    file: mmdFile,
    firstLine,
    lineCount,
    status,
    svgSize,
    durationMs,
    errorMsg
  });
}

console.log('\n==============================================');
console.log(`RENDER SUMMARY: Total=${mmdFiles.length}, Passed=${passCount}, Failed=${failCount}`);
console.log('==============================================\n');

fs.writeFileSync(renderReportPath, JSON.stringify({
  total: mmdFiles.length,
  passed: passCount,
  failed: failCount,
  results
}, null, 2), 'utf8');

if (failCount > 0) {
  process.exit(1);
} else {
  process.exit(0);
}
