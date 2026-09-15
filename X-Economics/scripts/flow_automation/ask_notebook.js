const { Agent, setGlobalDispatcher } = require('undici');

const agent = new Agent({
    bodyTimeout: 1800000,
    headersTimeout: 1800000
});
setGlobalDispatcher(agent);

async function askQuestion(question) {
    console.log(`\n--- Asking: "${question}" ---`);
    const payload = {
        notebook_url: 'https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800',
        question: question,
        source_format: 'footnotes',
        show_browser: true // Run headfully to match user-agent
    };

    const startTime = Date.now();
    try {
        const response = await fetch('http://localhost:3000/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload),
            signal: AbortSignal.timeout(1800000)
        });

        const data = await response.json();
        const durationSec = Math.round((Date.now() - startTime) / 1000);
        console.log(`Duration: ${durationSec}s`);
        if (data.success) {
            console.log('\nResponse:\n', data.data?.answer || data.answer || JSON.stringify(data, null, 2));
        } else {
            console.error('Error Response:', JSON.stringify(data, null, 2));
        }
        return data;
    } catch (err) {
        console.error('Fetch Error:', err.message);
        return { success: false, error: err.message };
    }
}

async function main() {
    const question1 = "Hãy trích lục chi tiết về thương vụ chuyển giao nợ nhà máy Hải Phòng trị giá 182.000 tỷ đồng của Vingroup sang Công ty Tương Lai (Công ty Cổ phần Nghiên cứu Đầu tư và Phát triển Tương Lai) trong tháng 5/2026. Vai trò của mô hình leaseback OEM trong thương vụ này là gì? Trích rõ các nguồn/văn bản cụ thể.";
    await askQuestion(question1);
}

main();
