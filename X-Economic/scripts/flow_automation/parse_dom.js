const fs = require('fs');
const path = require('path');

const html = fs.readFileSync('/tmp/nblm_dom.html', 'utf8');

// Search using a regex for text around "bước"
const regex = /[^<>]{0,100}bước[^<>]{0,100}/gi;
let match;
console.log('--- Matches for "bước" ---');
while ((match = regex.exec(html)) !== null) {
    console.log(`Matched text: "${match[0].trim()}"`);
    // Find the surrounding HTML tag
    const idx = match.index;
    const start = Math.max(0, idx - 200);
    const end = Math.min(html.length, idx + 200);
    console.log(`Surrounding HTML: ${html.substring(start, end).replace(/\s+/g, ' ')}\n`);
}

// Search for progress bar classes or spinners
const regexSpinner = /class="[^"]*(spinner|progress|loading|shimmer)[^"]*"/gi;
console.log('\n--- Progress/Spinner elements ---');
let count = 0;
while ((match = regexSpinner.exec(html)) !== null && count < 10) {
    const idx = match.index;
    const start = Math.max(0, idx - 100);
    const end = Math.min(html.length, idx + 100);
    console.log(`Tag: ${html.substring(start, end).replace(/\s+/g, ' ')}`);
    count++;
}
