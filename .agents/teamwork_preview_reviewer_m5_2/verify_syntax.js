const fs = require('fs');
const path = require('path');
const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.md'));

console.log('=== CODE BLOCK & MERMAID SYNTAX VERIFICATION ===\n');

let totalJsonBlocks = 0;
let validJsonBlocks = 0;
let jsonErrors = [];

let totalMermaidBlocks = 0;
let totalSqlBlocks = 0;
let totalCSharpBlocks = 0;
let totalTsBlocks = 0;
let totalYamlBlocks = 0;

files.forEach(f => {
  const content = fs.readFileSync(path.join(dir, f), 'utf8');
  
  // Extract JSON blocks
  const jsonMatches = content.matchAll(/```json\s*\n([\s\S]*?)\n```/g);
  for (const m of jsonMatches) {
    totalJsonBlocks++;
    const jsonStr = m[1].trim();
    try {
      JSON.parse(jsonStr);
      validJsonBlocks++;
    } catch (e) {
      // Sometimes JSON contains comments like // or ellipsis - check
      jsonErrors.push({ file: f, error: e.message, snippet: jsonStr.slice(0, 80) });
    }
  }
  
  // Count other language blocks
  const mermaidMatches = content.match(/```mermaid/g) || [];
  totalMermaidBlocks += mermaidMatches.length;

  const sqlMatches = content.match(/```sql/g) || [];
  totalSqlBlocks += sqlMatches.length;

  const csMatches = content.match(/```csharp/g) || [];
  totalCSharpBlocks += csMatches.length;

  const tsMatches = content.match(/```(?:typescript|tsx|ts)/g) || [];
  totalTsBlocks += tsMatches.length;

  const yamlMatches = content.match(/```(?:yaml|yml)/g) || [];
  totalYamlBlocks += yamlMatches.length;
});

console.log('Summary of Code Blocks in 9 Files:');
console.log(`- Mermaid Diagrams: ${totalMermaidBlocks}`);
console.log(`- SQL Blocks:       ${totalSqlBlocks}`);
console.log(`- C# (.NET 8):      ${totalCSharpBlocks}`);
console.log(`- TypeScript/TSX:   ${totalTsBlocks}`);
console.log(`- YAML / Compose:   ${totalYamlBlocks}`);
console.log(`- JSON Blocks:      ${totalJsonBlocks} (Strictly valid JSON: ${validJsonBlocks})`);

if (jsonErrors.length > 0) {
  console.log(`\nNote on non-strict JSON blocks (${jsonErrors.length}):`);
  jsonErrors.slice(0, 5).forEach((err, idx) => {
    console.log(`  ${idx+1}. [${err.file}] ${err.error} -> "${err.snippet}..."`);
  });
}
