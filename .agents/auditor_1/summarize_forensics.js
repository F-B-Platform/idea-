const fs = require('fs');

const renderReport = JSON.parse(fs.readFileSync('d:\\Idea_DoAn\\.agents\\auditor_1\\all_render_results.json', 'utf8'));

console.log('=== AUDIT FORENSICS DATA SUMMARY ===');
console.log('Total Diagrams Tested:', renderReport.total);
console.log('Total Diagrams Passed:', renderReport.passed);
console.log('Total Diagrams Failed:', renderReport.failed);

renderReport.details.forEach(d => {
  console.log(`- ${d.filename} | Block #${d.blockIndex} (${d.mmdName}): Status=${d.status}, SVG Size=${d.size.toLocaleString()} bytes, Render Time=${d.timeMs}ms`);
});