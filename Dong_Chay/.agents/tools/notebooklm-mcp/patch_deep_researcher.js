const fs = require('fs');
const path = '/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/tools/notebooklm-mcp/src/content/deep-researcher.ts';
let code = fs.readFileSync(path, 'utf8');

const replacement = `
    const addSourceSelectors = [
      'button[aria-label="Add source"]',
      'button[aria-label*="Add source"]',
      'button[aria-label*="add source" i]',
      'button[aria-label*="Upload" i]',
      'button[aria-label*="Choose" i]',
      'button:has(mat-icon:has-text("add"))',
      'button:has(mat-icon:has-text("add_circle"))',
      'button:has-text("Thêm nguồn")',
      'button:has-text("Add source")',
      'button:has-text("Upload sources")',
      'button:has-text("Choose files")',
      'button.mat-fab',
      'button.mat-mini-fab',
      '.action-button:has-text("Thêm nguồn")',
      '.action-button:has-text("Add source")'
    ];
`;

code = code.replace(/const addSourceSelectors = \[\s*'button:has-text\("Thêm nguồn"\)',\s*'button:has-text\("Add source"\)',\s*\];/g, replacement.trim());

fs.writeFileSync(path, code);
console.log('Patched deep-researcher.ts');
