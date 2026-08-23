const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const files = [
  'd:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/01_Kien_Truc_Tong_Quan.md',
  'd:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md',
  'd:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md',
  'd:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/04_Deployment_Diagram.md'
];

const tempDir = 'd:/Idea_DoAn/.agents/reviewer_2/temp_mermaid';
if (!fs.existsSync(tempDir)) {
  fs.mkdirSync(tempDir, { recursive: true });
}

// Puppeteer config for Windows Chrome
const puppeteerConfigPath = path.join(tempDir, 'puppeteer-config.json');
fs.writeFileSync(puppeteerConfigPath, JSON.stringify({
  executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  args: ["--no-sandbox", "--disable-setuid-sandbox", "--headless=new"]
}), 'utf8');

let totalDiagrams = 0;
let passedDiagrams = 0;
let failedDiagrams = [];

files.forEach((filePath) => {
  const fileName = path.basename(filePath);
  console.log(`\n========================================`);
  console.log(`Checking file: ${fileName}`);
  console.log(`========================================`);

  const content = fs.readFileSync(filePath, 'utf8');
  const regex = /```mermaid\r?\n([\s\S]*?)```/g;
  let match;
  let index = 1;

  while ((match = regex.exec(content)) !== null) {
    totalDiagrams++;
    const diagramCode = match[1].trim();
    const tempMmdPath = path.join(tempDir, `${fileName}_diag_${index}.mmd`);
    const tempSvgPath = path.join(tempDir, `${fileName}_diag_${index}.svg`);

    fs.writeFileSync(tempMmdPath, diagramCode, 'utf8');

    try {
      // Run mmdc with puppeteer config
      execSync(`npx -y @mermaid-js/mermaid-cli -p "${puppeteerConfigPath}" -i "${tempMmdPath}" -o "${tempSvgPath}"`, {
        stdio: 'pipe',
        timeout: 30000
      });
      console.log(`  [PASS] Diagram #${index} in ${fileName} rendered successfully.`);
      passedDiagrams++;
    } catch (err) {
      console.error(`  [FAIL] Diagram #${index} in ${fileName} failed compilation!`);
      const errorMsg = err.stderr ? err.stderr.toString() : err.message;
      console.error(`         Error details: ${errorMsg}`);
      failedDiagrams.push({
        file: fileName,
        index: index,
        codePreview: diagramCode.slice(0, 100),
        error: errorMsg
      });
    }

    index++;
  }
});

console.log(`\n========================================`);
console.log(`VERIFICATION SUMMARY:`);
console.log(`Total Diagrams Tested: ${totalDiagrams}`);
console.log(`Passed: ${passedDiagrams}`);
console.log(`Failed: ${failedDiagrams.length}`);
console.log(`========================================\n`);

if (failedDiagrams.length > 0) {
  console.error('Failed diagrams details:', JSON.stringify(failedDiagrams, null, 2));
  process.exit(1);
} else {
  console.log('ALL MERMAID DIAGRAMS COMPILED WITH 0 ERRORS!');
  process.exit(0);
}
