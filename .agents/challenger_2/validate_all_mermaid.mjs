import fs from 'fs';
import path from 'path';
import { JSDOM } from 'jsdom';
import createDOMPurify from 'dompurify';

const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
const purify = createDOMPurify(dom.window);
globalThis.DOMPurify = purify;
globalThis.purify = purify;
dom.window.DOMPurify = purify;
dom.window.purify = purify;

const mermaidModule = await import('./node_modules/mermaid/dist/mermaid.esm.mjs');
const mermaid = mermaidModule.default;

mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'loose',
    theme: 'default'
});

const rootDir = path.resolve('d:/Idea_DoAn');

function getMarkdownFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    for (const file of list) {
        if (file === '.git' || file === '.agents') continue;
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory()) {
            results = results.concat(getMarkdownFiles(fullPath));
        } else if (file.endsWith('.md')) {
            results.push(fullPath);
        }
    }
    return results;
}

const mdFiles = getMarkdownFiles(rootDir);
console.log(`Found ${mdFiles.length} markdown files. Extracting and validating all Mermaid blocks...`);

let totalDiagrams = 0;
let passedDiagrams = 0;
let failedDiagrams = [];

async function run() {
    for (const filePath of mdFiles) {
        const relPath = path.relative(rootDir, filePath);
        const content = fs.readFileSync(filePath, 'utf-8');
        const regex = /```mermaid\s*\n([\s\S]*?)\n```/g;
        let match;
        let blockIndex = 0;

        while ((match = regex.exec(content)) !== null) {
            blockIndex++;
            totalDiagrams++;
            const rawCode = match[1].trim();
            
            try {
                const parseResult = await mermaid.parse(rawCode);
                passedDiagrams++;
                console.log(`[PASS] ${relPath} - Block #${blockIndex}`);
            } catch (err) {
                console.error(`[FAIL] ${relPath} - Block #${blockIndex}: ${err.message || err}`);
                failedDiagrams.push({
                    file: relPath,
                    blockIndex,
                    error: err.message || String(err),
                    code: rawCode
                });
            }
        }
    }

    console.log('\n==========================================');
    console.log(`MERMAID VALIDATION SUMMARY`);
    console.log(`Total Diagrams Tested: ${totalDiagrams}`);
    console.log(`Passed: ${passedDiagrams}`);
    console.log(`Failed: ${failedDiagrams.length}`);
    console.log('==========================================');

    if (failedDiagrams.length > 0) {
        console.log('\nFailed Diagram Details:');
        for (const fail of failedDiagrams) {
            console.log(`\n--- File: ${fail.file} | Block #${fail.blockIndex} ---`);
            console.log(`Error: ${fail.error}`);
            console.log(`Code snippet (first 10 lines):`);
            console.log(fail.code.split('\n').slice(0, 10).join('\n'));
        }
    }
}

run().catch(console.error);
