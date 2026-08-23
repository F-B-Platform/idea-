import fs from 'fs';
import path from 'path';
import mermaid from './node_modules/mermaid/dist/mermaid.esm.mjs';

// Mermaid in browser requires DOM, let's test if mermaid.parse works or if we need minimal DOM mocking
try {
    mermaid.initialize({ startOnLoad: false });
    console.log("Mermaid initialized successfully!");
} catch (e) {
    console.log("Initialization note:", e.message);
}
