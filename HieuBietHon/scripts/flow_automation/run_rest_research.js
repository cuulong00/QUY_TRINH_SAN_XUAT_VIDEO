const fs = require('fs');
const { Agent, setGlobalDispatcher } = require('undici');

const agent = new Agent({
    bodyTimeout: 1800000,
    headersTimeout: 1800000
});
setGlobalDispatcher(agent);

async function sendResearchRequest(query) {
    console.log(`\n--- Sending Deep Research Request for: "${query}" ---`);
    const payload = {
        notebook_url: 'https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800',
        query: query,
        show_browser: false,
        timeout_ms: 600000 // 10 minutes timeout per query
    };

    const startTime = Date.now();
    try {
        const response = await fetch('http://localhost:3000/deep-research', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload),
            signal: AbortSignal.timeout(1800000) // 30 minutes timeout
        });

        const data = await response.json();
        const durationSec = Math.round((Date.now() - startTime) / 1000);
        console.log(`Duration: ${durationSec}s`);
        console.log('Response:', JSON.stringify(data, null, 2));
        return data;
    } catch (err) {
        console.error('Fetch Error:', err.message);
        return { success: false, error: err.message };
    }
}

async function main() {
    const queries = [
        "Vingroup transferring 182,000 billion VND in factory debt to Công ty Tương Lai in May 2026, leaseback OEM model of VinFast",
        "Indonesian police VF 3 EV deployment: Korlantas Polri modified VF 3s as mobile bases for ETLE drone patrols"
    ];

    for (let i = 0; i < queries.length; i++) {
        console.log(`\n========================================`);
        console.log(`Executing Query ${i + 1}/${queries.length}`);
        console.log(`========================================`);
        
        const result = await sendResearchRequest(queries[i]);
        if (!result.success) {
            console.error(`Query ${i + 1} failed. Stopping batch to prevent errors.`);
            break;
        }
        
        console.log('Query completed successfully. Waiting 5 seconds before next query...');
        await new Promise(r => setTimeout(r, 5000));
    }
}

main();
