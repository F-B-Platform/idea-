const fs = require('fs');
const path = require('path');

const targetDir = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams';
const files = [
  '01_Kien_Truc_Tong_Quan.md',
  '02_Sequence_Diagrams.md',
  '03_ERD_Database_Diagram.md',
  '04_Deployment_Diagram.md'
];

let totalBlocks = 0;
let errors = [];

function validateSequenceDiagram(code, file, startLine) {
  const lines = code.split('\n');
  const stack = [];
  lines.forEach((line, idx) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('%%')) return;
    
    // Check block openings
    if (/^(alt|opt|loop|par|critical|rect)\b/i.test(trimmed)) {
      stack.push({ type: trimmed.split(' ')[0], line: startLine + idx });
    } else if (/^else\b/i.test(trimmed)) {
      if (stack.length === 0 || (stack[stack.length - 1].type !== 'alt' && stack[stack.length - 1].type !== 'critical')) {
        errors.push({ file, line: startLine + idx, msg: `Unmatched 'else' without preceding 'alt'` });
      }
    } else if (/^and\b/i.test(trimmed)) {
      if (stack.length === 0 || stack[stack.length - 1].type !== 'par') {
        errors.push({ file, line: startLine + idx, msg: `Unmatched 'and' without preceding 'par'` });
      }
    } else if (/^end\b/i.test(trimmed)) {
      if (stack.length === 0) {
        errors.push({ file, line: startLine + idx, msg: `Unmatched 'end' statement` });
      } else {
        stack.pop();
      }
    }
  });
  if (stack.length > 0) {
    stack.forEach(s => {
      errors.push({ file, line: s.line, msg: `Unclosed block '${s.type}'` });
    });
  }
}

function validateErDiagram(code, file, startLine) {
  const lines = code.split('\n');
  let inEntity = false;
  let currentEntity = '';
  lines.forEach((line, idx) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('%%') || trimmed === 'erDiagram') return;
    
    if (trimmed.endsWith('{')) {
      if (inEntity) {
        errors.push({ file, line: startLine + idx, msg: `Nested entity definition inside ${currentEntity}` });
      }
      inEntity = true;
      currentEntity = trimmed.replace('{', '').trim();
    } else if (trimmed === '}') {
      if (!inEntity) {
        errors.push({ file, line: startLine + idx, msg: `Unmatched closing brace '}' outside entity` });
      }
      inEntity = false;
      currentEntity = '';
    } else if (inEntity) {
      // Must be attribute line: type name [keys] ["comment"]
      const attrMatch = trimmed.match(/^([A-Za-z0-9_()]+)\s+([A-Za-z0-9_]+)(\s+[A-Za-z0-9_,]+)?(\s+"[^"]*")?$/);
      if (!attrMatch) {
        // Some types might have spaces or special characters
        const broadMatch = trimmed.match(/^(\S+)\s+(\S+)/);
        if (!broadMatch) {
          errors.push({ file, line: startLine + idx, msg: `Invalid attribute format in entity ${currentEntity}: ${trimmed}` });
        }
      }
    } else {
      // Must be relationship: ENTITY1 relation ENTITY2 : "comment"
      const relMatch = trimmed.match(/^([A-Za-z0-9_]+)\s+(\|\||\|o|o\||}\||\}|o|\{)(\-\-|\.\.)(\|\||\|o|o\||o\{|\{\||\{\{|\}\})(\s+[A-Za-z0-9_]+)\s*:\s*("[^"]*"|'[^']*'|[A-Za-z0-9_ \-\/()]+)$/);
      const simpleRelMatch = trimmed.match(/^([A-Za-z0-9_]+)\s+[\S]+\s+([A-Za-z0-9_]+)\s*:\s*.*$/);
      if (!relMatch && !simpleRelMatch && !trimmed.startsWith('%%')) {
        errors.push({ file, line: startLine + idx, msg: `Unrecognized erDiagram line: ${trimmed}` });
      }
    }
  });
  if (inEntity) {
    errors.push({ file, line: startLine, msg: `Unclosed entity '${currentEntity}' in erDiagram` });
  }
}

function validateFlowchart(code, file, startLine) {
  const lines = code.split('\n');
  let subgraphStack = [];
  lines.forEach((line, idx) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('%%')) return;
    
    if (/^subgraph\b/i.test(trimmed)) {
      subgraphStack.push({ line: startLine + idx, text: trimmed });
    } else if (/^end\b/i.test(trimmed)) {
      if (subgraphStack.length === 0) {
        errors.push({ file, line: startLine + idx, msg: `Unmatched 'end' in flowchart` });
      } else {
        subgraphStack.pop();
      }
    }
  });
  if (subgraphStack.length > 0) {
    subgraphStack.forEach(s => {
      errors.push({ file, line: s.line, msg: `Unclosed subgraph '${s.text}'` });
    });
  }
}

files.forEach(filename => {
  const filePath = path.join(targetDir, filename);
  const content = fs.readFileSync(filePath, 'utf8');
  
  const mermaidRegex = /```mermaid\r?\n([\s\S]*?)```/g;
  let mMatch;
  let bIdx = 0;
  while ((mMatch = mermaidRegex.exec(content)) !== null) {
    bIdx++;
    totalBlocks++;
    const startLine = content.substring(0, mMatch.index).split('\n').length;
    const diagramCode = mMatch[1].trim();
    const firstLine = diagramCode.split('\n')[0].trim();
    
    console.log(`[${filename}] Block #${bIdx} at Line ${startLine}: Type='${firstLine}' (${diagramCode.split('\n').length} lines)`);
    
    if (firstLine.startsWith('sequenceDiagram')) {
      validateSequenceDiagram(diagramCode, filename, startLine);
    } else if (firstLine.startsWith('erDiagram')) {
      validateErDiagram(diagramCode, filename, startLine);
    } else if (firstLine.startsWith('flowchart') || firstLine.startsWith('graph')) {
      validateFlowchart(diagramCode, filename, startLine);
    }
  }
});

console.log(`\nTotal Mermaid Blocks Checked: ${totalBlocks}`);
console.log(`Total Syntax / Structural Errors: ${errors.length}`);
if (errors.length > 0) {
  console.log('Errors:', JSON.stringify(errors, null, 2));
}