const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const targetDir = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams';
const tempMmdDir = 'd:\\Idea_DoAn\\.agents\\auditor_it2\\temp_mmd';
const resultsFile = 'd:\\Idea_DoAn\\.agents\\auditor_it2\\audit_results.json';

if (!fs.existsSync(tempMmdDir)) {
  fs.mkdirSync(tempMmdDir, { recursive: true });
}

const files = [
  '01_Kien_Truc_Tong_Quan.md',
  '02_Sequence_Diagrams.md',
  '03_ERD_Database_Diagram.md',
  '04_Deployment_Diagram.md'
];

const auditResults = {
  timestamp: new Date().toISOString(),
  files: {},
  placeholderViolations: [],
  legacyRemnantsViolations: [],
  mermaidDiagrams: [],
  technicalValidation: {},
  verdict: 'PENDING'
};

console.log('=== STEP 1: SCANNING FILES FOR PLACEHOLDERS & LEGACY REMNANTS ===');

// Check patterns
const placeholderRegexes = [
  { name: 'TODO', regex: /\bTODO\b/gi },
  { name: 'TBD', regex: /\bTBD\b/gi },
  { name: 'Lazy code comments', regex: /(\/\*|\/\/)\s*(rest of|tương tự|giữ nguyên|dummy|code here|chèn thêm)/gi },
  { name: 'Generic placeholder', regex: /\b(placeholder|dummy_data|dummy_logic)\b/gi },
  { name: 'Ellipsis line', regex: /^\s*\.\.\.\s*$/gm }
];

const legacyRegexes = [
  { name: 'Staff Mobile App (Flutter/RN active)', regex: /\b(Staff\s+Mobile\s+App|Flutter|React\s+Native)\b/gi },
  { name: 'GPS 50m / GPS chấm công', regex: /\b(GPS\s*50\s*m|chấm\s*công\s*(bằng|qua)?\s*GPS|GPS\s*chấm\s*công)\b/gi },
  { name: 'QR 30s / QR động 30s', regex: /\b(QR\s*(động\s*)?30\s*s|30\s*giây)\b/gi },
  { name: 'C-23 / C-24 feature codes', regex: /\b(C-23|C-24)\b/gi },
  { name: 'Ví voucher riêng lẻ', regex: /\b(ví\s+voucher)\b/gi },
  { name: 'Tra cứu calo độc lập', regex: /\b(tra\s+cứu\s+calo\s+độc\s+lập|tính\s+calo\s+riêng)\b/gi }
];

files.forEach(fileName => {
  const filePath = path.join(targetDir, fileName);
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');

  auditResults.files[fileName] = {
    sizeBytes: Buffer.byteLength(content, 'utf8'),
    lineCount: lines.length,
    mermaidCount: 0
  };

  // Scan Placeholders
  placeholderRegexes.forEach(({ name, regex }) => {
    let match;
    while ((match = regex.exec(content)) !== null) {
      // Find line number
      const lineNum = content.substring(0, match.index).split('\n').length;
      const lineContent = lines[lineNum - 1].trim();
      auditResults.placeholderViolations.push({
        file: fileName,
        type: name,
        line: lineNum,
        matched: match[0],
        snippet: lineContent
      });
    }
  });

  // Scan Legacy Remnants
  legacyRegexes.forEach(({ name, regex }) => {
    let match;
    while ((match = regex.exec(content)) !== null) {
      const lineNum = content.substring(0, match.index).split('\n').length;
      const lineContent = lines[lineNum - 1].trim();
      
      // Check if it is an explicit deprecation note (e.g. "Loại bỏ hoàn toàn Staff Mobile App", "Thay thế GPS bằng WiFi")
      const isDeprecationExplanation = 
        lineContent.includes('Loại bỏ') || 
        lineContent.includes('loại bỏ') || 
        lineContent.includes('Bãi bỏ') || 
        lineContent.includes('bãi bỏ') || 
        lineContent.includes('không sử dụng') ||
        lineContent.includes('thay thế') ||
        lineContent.includes('Bỏ hoàn toàn') ||
        lineContent.includes('Xóa bỏ') ||
        lineContent.includes('được thay thế bằng');

      auditResults.legacyRemnantsViolations.push({
        file: fileName,
        type: name,
        line: lineNum,
        matched: match[0],
        snippet: lineContent,
        isDeprecationExplanation
      });
    }
  });

  // Extract Mermaid Blocks
  const mermaidBlockRegex = /```mermaid\r?\n([\s\S]*?)```/g;
  let mMatch;
  let index = 0;
  while ((mMatch = mermaidBlockRegex.exec(content)) !== null) {
    index++;
    const mmdContent = mMatch[1].trim();
    const baseName = fileName.replace('.md', '');
    const mmdFileName = `${baseName}_b${String(index).padStart(2, '0')}.mmd`;
    const mmdFilePath = path.join(tempMmdDir, mmdFileName);
    fs.writeFileSync(mmdFilePath, mmdContent, 'utf8');

    // Detect diagram type and title/description
    const firstLine = mmdContent.split('\n')[0].trim();
    auditResults.mermaidDiagrams.push({
      file: fileName,
      blockIndex: index,
      mmdFileName,
      mmdFilePath,
      diagramType: firstLine,
      lineCount: mmdContent.split('\n').length,
      byteLength: Buffer.byteLength(mmdContent, 'utf8'),
      renderStatus: 'PENDING'
    });
  }
  auditResults.files[fileName].mermaidCount = index;
});

console.log(`Files Analyzed: ${files.length}`);
console.log(`Total Mermaid Diagrams Found: ${auditResults.mermaidDiagrams.length}`);
console.log(`Placeholder Violations: ${auditResults.placeholderViolations.length}`);
console.log(`Legacy Violations (total hits): ${auditResults.legacyRemnantsViolations.length}`);

// Write intermediate results
fs.writeFileSync(resultsFile, JSON.stringify(auditResults, null, 2), 'utf8');
console.log('Scan complete. Results written to', resultsFile);
