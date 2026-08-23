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

// Test C4 Container with Container_Boundary vs Boundary vs ContainerBoundary
const c4Test = `
C4Container
    title Container Diagram - Smart F&B Operating System

    Person(user_client, "Người dùng hệ thống", "Khách hàng, Nhân viên, Barista, Quản lý, Admin")

    Container_Boundary(frontend_boundary, "Frontend Next.js 14 Monorepo (Port 3000)") {
        Container(customer_pwa, "Customer PWA Portal", "Next.js 14 / React 19 / Tailwind", "Màn hình đặt món tại bàn Dine-in, đặt giao hàng Delivery, thanh toán VietQR và Chatbot tư vấn.")
    }
`;

try {
    const res = await mermaid.parse(c4Test);
    console.log("C4 Container with Container_Boundary: PASSED!");
} catch (e) {
    console.log("C4 Container with Container_Boundary: FAILED:", e.message);
}

// Test ERD with single FK
const erdTest = `
erDiagram
    PAYMENT {
        uuid id PK
        uuid order_id FK
        string payment_method
    }
`;

try {
    const res2 = await mermaid.parse(erdTest);
    console.log("ERD with single FK: PASSED!");
} catch (e) {
    console.log("ERD with single FK: FAILED:", e.message);
}
