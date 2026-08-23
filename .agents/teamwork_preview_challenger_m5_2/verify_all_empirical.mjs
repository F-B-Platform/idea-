
import fs from 'fs';
import path from 'path';
import mermaid from 'mermaid';
import jsYaml from 'js-yaml';

mermaid.initialize({
  startOnLoad: false,
  securityLevel: 'loose',
  suppressErrorRendering: true
});

const DOCS_DIR = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const FILES = [
  '01_Phan_Tich_Yeu_Cau.md',
  '02_Thiet_Ke_Database.md',
  '03_Thiet_Ke_API_Contract.md',
  '04_Thiet_Ke_UI_UX.md',
  '05_Quy_Trinh_Backend.md',
  '06_Quy_Trinh_Frontend.md',
  '07_Ke_Hoach_Kiem_Thu.md',
  '08_Trien_Khai_He_Thong.md',
  'README.md'
];

const results = {
  totalFiles: FILES.length,
  filesSummary: {},
  mermaid: { total: 0, passed: 0, failed: 0, details: [] },
  json: { total: 0, passed: 0, failed: 0, details: [] },
  yaml: { total: 0, passed: 0, failed: 0, details: [] },
  tables: { total: 0, passed: 0, failed: 0, details: [] },
  headings: { total: 0, issues: 0, details: [] },
  callouts: { total: 0, valid: 0, invalid: 0, details: [] },
  placeholders: { found: 0, details: [] }
};

function extractCodeBlocks(content) {
  const blocks = [];
  const lines = content.split(/\r?\n/);
  let inBlock = false;
  let currentLang = '';
  let currentCode = [];
  let startLine = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const match = line.match(/^`([a-zA-Z0-9_-]*)/);
    if (match && !inBlock) {
      inBlock = true;
      currentLang = match[1].toLowerCase().trim();
      currentCode = [];
      startLine = i + 1;
    } else if (line.startsWith('`') && inBlock) {
      inBlock = false;
      blocks.push({
        lang: currentLang,
        code: currentCode.join('\n'),
        startLine: startLine,
        endLine: i + 1
      });
      currentLang = '';
      currentCode = [];
    } else if (inBlock) {
      currentCode.push(line);
    }
  }
  return blocks;
}

function checkHeadings(content, fileName) {
  const lines = content.split(/\r?\n/);
  let prevLevel = 0;
  let issues = [];
  let count = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const match = line.match(/^(#{1,6})\s+(.+)$/);
    if (match) {
      count++;
      const level = match[1].length;
      const title = match[2];
      if (prevLevel > 0 && level > prevLevel + 1) {
        issues.push({
          fileName,
          line: i + 1,
          msg: Heading level skip: from h to h ()
        });
      }
      prevLevel = level;
    }
  }
  return { count, issues };
}

function checkTables(content, fileName) {
  const lines = content.split(/\r?\n/);
  const tables = [];
  let inTable = false;
  let currentTable = [];
  let startLine = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith('|') && line.endsWith('|')) {
      if (!inTable) {
        inTable = true;
        currentTable = [];
        startLine = i + 1;
      }
      currentTable.push({ lineNum: i + 1, text: line });
    } else {
      if (inTable) {
        if (currentTable.length >= 2) {
          tables.push({ startLine, rows: currentTable });
        }
        inTable = false;
        currentTable = [];
      }
    }
  }
  if (inTable && currentTable.length >= 2) {
    tables.push({ startLine, rows: currentTable });
  }

  const tableResults = [];
  for (const t of tables) {
    let isValid = true;
    let errorMsg = '';
    
    const headerCols = t.rows[0].text.split('|').slice(1, -1).map(c => c.trim());
    const sepCols = t.rows[1].text.split('|').slice(1, -1).map(c => c.trim());
    
    const isSep = sepCols.every(c => /^:?-+:?$/.test(c));
    if (!isSep) {
      isValid = false;
      errorMsg = Row 2 is not a valid markdown table separator row: ;
    } else {
      const colCount = headerCols.length;
      for (let r = 0; r < t.rows.length; r++) {
        const rowCols = t.rows[r].text.split('|').slice(1, -1);
        if (rowCols.length !== colCount) {
          isValid = false;
          errorMsg = Row  column count mismatch: expected , got ;
          break;
        }
      }
    }
    tableResults.push({
      fileName,
      startLine: t.startLine,
      rowCount: t.rows.length,
      colCount: headerCols.length,
      isValid,
      errorMsg
    });
  }
  return tableResults;
}

function checkCallouts(content, fileName) {
  const lines = content.split(/\r?\n/);
  const callouts = [];
  const validTypes = ['NOTE', 'TIP', 'IMPORTANT', 'WARNING', 'CAUTION'];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    const match = line.match(/^>\s*\[!([A-Z]+)\](.*)$/);
    if (match) {
      const type = match[1];
      const rest = match[2];
      const isValid = validTypes.includes(type);
      callouts.push({
        fileName,
        line: i + 1,
        type,
        isValid,
        msg: isValid ? 'OK' : Invalid alert type: [!]. Allowed: 
      });
    }
  }
  return callouts;
}

function checkPlaceholders(content, fileName) {
  const lines = content.split(/\r?\n/);
  const findings = [];
  const banned = [
    /\bTODO\b/i,
    /\bTBD\b/i,
    /\/\*\s*rest of code\s*\*\//i,
    /\/\/\s*rest of code/i,
    /\/\/\s*tương tự như trên/i,
    /\/\/\s*giữ nguyên logic cũ/i,
    /\[Chưa hoàn thiện\]/i,
    /\/\*\s*còn tiếp\s*\*\//i
  ];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    for (const pattern of banned) {
      if (pattern.test(line)) {
        findings.push({
          fileName,
          line: i + 1,
          matched: line.trim(),
          pattern: pattern.toString()
        });
      }
    }
  }
  return findings;
}

async function run() {
  console.log('================================================================');
  console.log('STARTING EMPIRICAL SYNTAX, SCHEMA & DIAGRAM VERIFICATION');
  console.log('================================================================');

  for (const fileName of FILES) {
    const filePath = path.join(DOCS_DIR, fileName);
    if (!fs.existsSync(filePath)) {
      console.error(MISSING FILE: );
      continue;
    }
    const content = fs.readFileSync(filePath, 'utf8');
    const blocks = extractCodeBlocks(content);
    
    results.filesSummary[fileName] = {
      sizeBytes: Buffer.byteLength(content, 'utf8'),
      totalLines: content.split(/\r?\n/).length,
      codeBlocks: blocks.length,
      mermaidBlocks: 0,
      jsonBlocks: 0,
      yamlBlocks: 0,
      tablesCount: 0,
      headingsCount: 0,
      calloutsCount: 0
    };

    console.log(\n------------------------------------------------------------);
    console.log([FILE]  ( chars,  code blocks));
    console.log(------------------------------------------------------------);

    // Headings
    const headingCheck = checkHeadings(content, fileName);
    results.headings.total += headingCheck.count;
    results.filesSummary[fileName].headingsCount = headingCheck.count;
    if (headingCheck.issues.length > 0) {
      results.headings.issues += headingCheck.issues.length;
      results.headings.details.push(...headingCheck.issues);
      for (const issue of headingCheck.issues) {
        console.warn(  [HEADING ISSUE] Line : );
      }
    } else {
      console.log(  ✓ Headings:  headings, 0 hierarchy skips);
    }

    // Tables
    const tableChecks = checkTables(content, fileName);
    results.tables.total += tableChecks.length;
    results.filesSummary[fileName].tablesCount = tableChecks.length;
    let fileTablesFailed = 0;
    for (const t of tableChecks) {
      if (t.isValid) {
        results.tables.passed++;
      } else {
        fileTablesFailed++;
        results.tables.failed++;
        results.tables.details.push(t);
        console.error(  [TABLE ERROR] Line : );
      }
    }
    if (fileTablesFailed === 0) {
      console.log(  ✓ Tables:  tables verified, all valid);
    }

    // Callouts
    const calloutChecks = checkCallouts(content, fileName);
    results.callouts.total += calloutChecks.length;
    results.filesSummary[fileName].calloutsCount = calloutChecks.length;
    let fileCalloutsInvalid = 0;
    for (const c of calloutChecks) {
      if (c.isValid) {
        results.callouts.valid++;
      } else {
        fileCalloutsInvalid++;
        results.callouts.invalid++;
        results.callouts.details.push(c);
        console.error(  [CALLOUT ERROR] Line : );
      }
    }
    if (fileCalloutsInvalid === 0) {
      console.log(  ✓ Alert Callouts:  callouts verified, all valid);
    }

    // Placeholders
    const placeholderChecks = checkPlaceholders(content, fileName);
    if (placeholderChecks.length > 0) {
      results.placeholders.found += placeholderChecks.length;
      results.placeholders.details.push(...placeholderChecks);
      for (const p of placeholderChecks) {
        console.error(  [PLACEHOLDER FOUND] Line : );
      }
    } else {
      console.log(  ✓ Placeholders: 0 forbidden placeholder tokens found);
    }

    // Code Blocks
    for (const block of blocks) {
      if (block.lang === 'mermaid') {
        results.mermaid.total++;
        results.filesSummary[fileName].mermaidBlocks++;
        try {
          const parseResult = await mermaid.parse(block.code);
          results.mermaid.passed++;
          const firstLine = block.code.trim().split(/\r?\n/)[0];
          console.log(  ✓ Mermaid [Line -] ());
        } catch (err) {
          results.mermaid.failed++;
          const firstLine = block.code.trim().split(/\r?\n/)[0];
          const errDetail = {
            fileName,
            startLine: block.startLine,
            endLine: block.endLine,
            diagramType: firstLine,
            error: err.message || String(err),
            snippet: block.code.slice(0, 200)
          };
          results.mermaid.details.push(errDetail);
          console.error(  ❌ MERMAID ERROR [Line -] in : );
        }
      } else if (block.lang === 'json') {
        results.json.total++;
        results.filesSummary[fileName].jsonBlocks++;
        try {
          JSON.parse(block.code);
          results.json.passed++;
          console.log(  ✓ JSON [Line -] (Valid syntax));
        } catch (err) {
          results.json.failed++;
          const errDetail = {
            fileName,
            startLine: block.startLine,
            endLine: block.endLine,
            error: err.message,
            snippet: block.code.slice(0, 200)
          };
          results.json.details.push(errDetail);
          console.error(  ❌ JSON ERROR [Line -] in : );
        }
      } else if (block.lang === 'yaml' || block.lang === 'yml') {
        results.yaml.total++;
        results.filesSummary[fileName].yamlBlocks++;
        try {
          jsYaml.load(block.code);
          results.yaml.passed++;
          console.log(  ✓ YAML [Line -] (Valid syntax));
        } catch (err) {
          results.yaml.failed++;
          const errDetail = {
            fileName,
            startLine: block.startLine,
            endLine: block.endLine,
            error: err.message,
            snippet: block.code.slice(0, 200)
          };
          results.yaml.details.push(errDetail);
          console.error(  ❌ YAML ERROR [Line -] in : );
        }
      }
    }
  }

  console.log('\n================================================================');
  console.log('FINAL EMPIRICAL VERIFICATION SUMMARY');
  console.log('================================================================');
  console.log(Total Files Checked: );
  console.log(Mermaid Diagrams:  total |  passed |  failed);
  console.log(JSON Blocks:       total |  passed |  failed);
  console.log(YAML Blocks:       total |  passed |  failed);
  console.log(Tables:            total |  passed |  failed);
  console.log(Heading Skips:     issues across  headings);
  console.log(Alert Callouts:    total |  valid |  invalid);
  console.log(Placeholders:      forbidden tokens found);
  console.log('================================================================');

  fs.writeFileSync(
    'd:/Idea_DoAn/.agents/teamwork_preview_challenger_m5_2/results.json',
    JSON.stringify(results, null, 2),
    'utf8'
  );
}

run().catch(console.error);
