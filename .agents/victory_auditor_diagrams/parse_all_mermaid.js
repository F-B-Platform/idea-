const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

// Setup minimal DOM environment for mermaid
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="mermaid-container"></div></body></html>', {
  pretendToBeVisual: true
});
global.window = dom.window;
global.document = dom.window.document;
global.navigator = dom.window.navigator;
global.Element = dom.window.Element;
global.SVGElement = dom.window.SVGElement;

const mermaid = require('mermaid');

mermaid.initialize({
  startOnLoad: false,
  suppressErrorRendering: true,
  securityLevel: 'loose'
});

const mmdDir = path.join(__dirname, 'mermaid_test');
const files = fs.readdirSync(mmdDir).filter(f => f.endsWith('.mmd'));

console.log(`=== PARSING ${files.length} MERMAID DIAGRAMS USING OFFICIAL MERMAID PARSER API ===\n`);

let passed = 0;
let failed = 0;
const errors = [];

async function run() {
  for (const file of files) {
    const filePath = path.join(mmdDir, file);
    const content = fs.readFileSync(filePath, 'utf-8').trim();
    
    try {
      const valid = await mermaid.parse(content);
      console.log(`[PASS] ${file} (parsed successfully, type: ${content.split('\n')[0].trim()})`);
      passed++;
    } catch (err) {
      console.error(`[FAIL] ${file}`);
      console.error(`       Error: ${err.message || err}`);
      failed++;
      errors.push({ file, error: err.message || err });
    }
  }

  console.log(`\n======================================================`);
  console.log(`MERMAID PARSING RESULTS: ${passed}/${files.length} PASSED (${failed} FAILED)`);
  console.log(`======================================================`);

  if (failed === 0) {
    console.log(`VERDICT: ALL 22 MERMAID DIAGRAMS ARE 100% SYNTACTICALLY VALID!`);
  } else {
    console.error(`VERDICT: FAILED - ${failed} DIAGRAMS CONTAIN SYNTAX ERRORS!`);
    process.exit(1);
  }
}

run();
