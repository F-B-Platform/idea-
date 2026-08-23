import fs from 'fs';
import { JSDOM } from 'jsdom';

const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
globalThis.HTMLElement = dom.window.HTMLElement;
globalThis.SVGElement = dom.window.SVGElement;
globalThis.XMLSerializer = dom.window.XMLSerializer;

const mermaid = (await import('mermaid')).default;

mermaid.initialize({
  startOnLoad: false,
  securityLevel: 'loose',
  suppressErrorRendering: true
});

async function main() {
  const inputFile = process.argv[2];
  const data = JSON.parse(fs.readFileSync(inputFile, 'utf8'));
  const results = [];

  for (const item of data) {
    try {
      const parsed = await mermaid.parse(item.code);
      results.push({
        id: item.id,
        file: item.file,
        startLine: item.startLine,
        endLine: item.endLine,
        diagramType: parsed.diagramType || item.code.trim().split(/\r?\n/)[0],
        success: true
      });
    } catch (err) {
      results.push({
        id: item.id,
        file: item.file,
        startLine: item.startLine,
        endLine: item.endLine,
        diagramType: item.code.trim().split(/\r?\n/)[0],
        success: false,
        error: err.message || String(err),
        snippet: item.code.slice(0, 300)
      });
    }
  }

  const outputFile = process.argv[3];
  fs.writeFileSync(outputFile, JSON.stringify(results, null, 2), 'utf8');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
