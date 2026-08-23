const fs = require('fs');
const path = require('path');
const url = require('url');
const { JSDOM } = require('d:/Idea_DoAn/.agents/teamwork_preview_challenger_m5_2/node_modules/jsdom');

async function main() {
    const dom = new JSDOM('<!DOCTYPE html><html><body><div id="graph"></div></body></html>');
    global.window = dom.window;
    global.document = dom.window.document;
    global.navigator = dom.window.navigator;
    global.Element = dom.window.Element;
    global.SVGElement = dom.window.SVGElement;

    // Load mermaid
    const mermaidPath = path.resolve('d:/Idea_DoAn/.agents/teamwork_preview_challenger_m5_2/node_modules/mermaid/dist/mermaid.core.mjs');
    const mermaidUrl = url.pathToFileURL(mermaidPath).href;
    const mermaidModule = await import(mermaidUrl);
    const mermaid = mermaidModule.default;
    mermaid.initialize({ startOnLoad: false, suppressErrorRendering: true });

    const mdPath = 'd:/Idea_DoAn/04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md';
    const content = fs.readFileSync(mdPath, 'utf8');

    // Extract code blocks with mermaid
    const regex = /```mermaid([\s\S]*?)```/g;
    let match;
    let index = 0;
    const results = [];

    while ((match = regex.exec(content)) !== null) {
        index++;
        const diagramCode = match[1].trim();
        console.log(`\n========================================`);
        console.log(`Validating Diagram ${index}...`);
        const header = diagramCode.split('\n')[0];
        console.log(`Type: ${header}`);
        try {
            const parseResult = await mermaid.parse(diagramCode);
            console.log(`✅ Diagram ${index} PASS!`);
            results.push({ index, header, status: 'PASS', error: null });
        } catch (err) {
            console.error(`❌ Diagram ${index} FAILED:`, err.message || err);
            results.push({ index, header, status: 'FAIL', error: err.message || String(err) });
        }
    }

    console.log(`\n========================================`);
    console.log(`SUMMARY: Total diagrams: ${results.length}, Passed: ${results.filter(r => r.status === 'PASS').length}, Failed: ${results.filter(r => r.status === 'FAIL').length}`);

    fs.writeFileSync('d:/Idea_DoAn/.agents/challenger_it2/mermaid_validation_result.json', JSON.stringify(results, null, 2));
}

main().catch(err => {
    console.error('Fatal error in runner:', err);
    process.exit(1);
});
