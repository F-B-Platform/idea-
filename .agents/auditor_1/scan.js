const fs = require('fs');
const path = require('path');

const targetDir = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams';
const files = [
  '01_Kien_Truc_Tong_Quan.md',
  '02_Sequence_Diagrams.md',
  '03_ERD_Database_Diagram.md',
  '04_Deployment_Diagram.md'
];

const results = {
  fileStats: {},
  placeholderChecks: {},
  deprecatedChecks: {},
  mermaidBlocks: {},
  specificChecks: {}
};

// 1. Check placeholders
const placeholderRegexes = [
  { name: 'TODO', regex: /\bTODO\b/gi },
  { name: 'TBD', regex: /\bTBD\b/gi },
  { name: 'REST_OF_CODE', regex: /(\/\*|\/\/)\s*(rest of|tương tự|giữ nguyên)/gi },
  { name: 'PLACEHOLDER_WORD', regex: /\b(placeholder|dummy_data|dummy_logic)\b/gi },
  { name: 'ELLIPSIS_LAZY', regex: /^\s*\.\.\.\s*$/gm }
];

// 2. Check deprecated terms
const deprecatedRegexes = [
  { name: 'STAFF_MOBILE_APP', regex: /(Staff\s+Mobile\s+App|App\s+di\s+động\s+nhân\s+viên|Flutter|React\s+Native)/gi },
  { name: 'GPS_LOCK', regex: /(GPS|bán\s+kính\s+50m|khoảng\s+cách\s+50m)/gi },
  { name: 'DYNAMIC_QR_30S', regex: /(QR\s+động\s+30|30\s*giây\s+đổi|hết\s+hạn\s+30s)/gi },
  { name: 'C23_C24', regex: /\b(C-23|C-24|C23|C24)\b/gi },
  { name: 'VOUCHER_WALLET', regex: /(ví\s+voucher|voucher\s+wallet)/gi }
];

files.forEach(filename => {
  const filePath = path.join(targetDir, filename);
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  
  results.fileStats[filename] = {
    bytes: Buffer.byteLength(content, 'utf8'),
    lines: lines.length
  };

  // Placeholders
  results.placeholderChecks[filename] = [];
  placeholderRegexes.forEach(p => {
    let match;
    const re = new RegExp(p.regex);
    while ((match = re.exec(content)) !== null) {
      // Find line number
      const lineNum = content.substring(0, match.index).split('\n').length;
      results.placeholderChecks[filename].push({
        type: p.name,
        match: match[0],
        line: lineNum,
        snippet: lines[lineNum - 1].trim()
      });
    }
  });

  // Deprecated terms check
  results.deprecatedChecks[filename] = [];
  deprecatedRegexes.forEach(d => {
    let match;
    const re = new RegExp(d.regex);
    while ((match = re.exec(content)) !== null) {
      const lineNum = content.substring(0, match.index).split('\n').length;
      const snippet = lines[lineNum - 1].trim();
      // Check if it's explicitly discussing elimination / deprecation
      const isEliminationContext = /(loại\s+bỏ|bỏ\s+hoàn\s+toàn|xóa\s+bỏ|thay\s+thế|không\s+sử\s+dụng|bãi\s+bỏ|chấm\s+dứt|tuyệt\s+đối\s+không)/i.test(snippet);
      results.deprecatedChecks[filename].push({
        type: d.name,
        match: match[0],
        line: lineNum,
        snippet: snippet,
        isEliminationContext: isEliminationContext
      });
    }
  });

  // Extract Mermaid Blocks
  results.mermaidBlocks[filename] = [];
  const mermaidRegex = /```mermaid\r?\n([\s\S]*?)```/g;
  let mMatch;
  let blockIndex = 1;
  while ((mMatch = mermaidRegex.exec(content)) !== null) {
    const startLine = content.substring(0, mMatch.index).split('\n').length;
    const diagramCode = mMatch[1];
    const diagramType = diagramCode.trim().split('\n')[0].trim();
    results.mermaidBlocks[filename].push({
      index: blockIndex++,
      startLine: startLine,
      type: diagramType,
      lineCount: diagramCode.split('\n').length,
      codeSnippet: diagramCode.trim().substring(0, 100) + '...'
    });
  }
});

console.log(JSON.stringify(results, null, 2));