const fs = require('fs');
const path = require('path');
const ts = require('typescript');

const tsDir = path.join('d:', 'Idea_DoAn', '.agents', 'victory_auditor_1', 'test_ts');
const files = fs.readdirSync(tsDir).filter(f => f.endsWith('.tsx') || f.endsWith('.ts'));

console.log(`Parsing ${files.length} TypeScript / TSX files for syntactic validity...`);

let hasSyntaxErrors = false;

for (const file of files) {
  const filePath = path.join(tsDir, file);
  const sourceCode = fs.readFileSync(filePath, 'utf-8');
  
  const sourceFile = ts.createSourceFile(
    file,
    sourceCode,
    ts.ScriptTarget.Latest,
    true,
    file.endsWith('.tsx') ? ts.ScriptKind.TSX : ts.ScriptKind.TS
  );
  
  // Check syntactic diagnostics
  const program = ts.createProgram([filePath], {
    target: ts.ScriptTarget.ESNext,
    jsx: ts.JsxEmit.Preserve,
    module: ts.ModuleKind.ESNext,
    noEmit: true
  });
  
  const syntaxDiagnostics = program.getSyntacticDiagnostics(sourceFile);
  
  if (syntaxDiagnostics.length > 0) {
    console.log(`❌ ${file} has syntactic errors:`);
    for (const diag of syntaxDiagnostics) {
      const { line, character } = sourceFile.getLineAndCharacterOfPosition(diag.start);
      console.log(`   Line ${line + 1}:${character + 1} - ${diag.messageText}`);
    }
    hasSyntaxErrors = true;
  } else {
    console.log(`✅ ${file}: 100% Syntactically Valid TS/TSX AST (${sourceFile.statements.length} top-level AST nodes)`);
  }
}

if (!hasSyntaxErrors) {
  console.log("\n>>> [PASS] ALL TYPESCRIPT AND TSX CODE SAMPLES ARE 100% SYNTACTICALLY VALID! <<<");
}
