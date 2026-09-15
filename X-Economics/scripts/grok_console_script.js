
/**
 * GOCNHINPODCAST GROK AUTO-GENERATOR
 * Copy toàn bộ đoạn code này paste vào Console (F12) của tab https://grok.com/imagine
 */
(async function() {
    console.log("%c🚀 KHỞI ĐỘNG GOCNHINPODCAST GROK AUTOMATION", "color: #00ff00; font-size: 20px; font-weight: bold;");
    
    const promptsData = [
    {
        "tag": "[c1:01]",
        "prompt": "[c1:01] A satirical editorial political cartoon of a massive, heavily overloaded, rickety bus shaped like the Earth speeding dangerously down a multilane highway, with tiny people looking out the windows in panic. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_01.png"
    },
    {
        "tag": "[c1:02]",
        "prompt": "[c1:02] A satirical editorial political cartoon of Donald Trump as a bus driver, manic and reckless, aggressively steering the wheel of a bus with one hand while casually laughing at his smartphone in the other hand, completely ignoring the road ahead. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_02.png"
    },
    {
        "tag": "[c1:03]",
        "prompt": "[c1:03] A satirical editorial political cartoon of a giant red Wall Street stock market line graph violently snapping in half like a broken steering column, with shattered glass and sparks flying. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_03.png"
    },
    {
        "tag": "[c1:04]",
        "prompt": "[c1:04] A satirical editorial political cartoon of massive stacks of hundred-dollar bills sprouting little legs and frantically running in circles around a glowing, chaotic glowing smartphone screen displaying a single social media post. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_04.png"
    },
    {
        "tag": "[c1:05]",
        "prompt": "[c1:05] A satirical editorial political cartoon of a gigantic black crude oil barrel being smashed to pieces by an oversized glowing yellow mallet that has the word 'TWEET' plastered on it, with dark oil spilling everywhere. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_05.png"
    },
    {
        "tag": "[c1:06]",
        "prompt": "[c1:06] A satirical editorial political cartoon of Donald Trump dressed as a flamboyant stage magician, standing under a spotlight and pulling exploding missiles and plunging currency symbols out of a magic hat, while the audience of world leaders cowers in terror. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_06.png"
    },
    {
        "tag": "[c1:07]",
        "prompt": "[c1:07] A satirical editorial political cartoon of a gas station pump nozzle morphed into a vicious metallic snake violently biting into a thin, worn-out leather wallet belonging to an everyday worker, draining the cash out of it. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_07.png"
    },
    {
        "tag": "[c1:08]",
        "prompt": "[c1:08] A satirical editorial political cartoon of a gigantic, aggressive hand in a tailored suit reaching down with giant chopsticks to grab tiny gold coins out of a tiny, cracked rice bowl held by a struggling worker. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_08.png"
    },
    {
        "tag": "[c1:09]",
        "prompt": "[c1:09] A satirical editorial political cartoon of a tough, glowing survival handbook wrapped in chains sitting on a tiny raft, navigating through a treacherous stormy sea made entirely of plunging red stock market arrows. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_09.png"
    },
    {
        "tag": "[c1:10]",
        "prompt": "[c1:10] A satirical editorial political cartoon of a massive, razor-sharp letter 'X' slicing cleanly through a chaotic, tangled mess of wires attached to a ticking time bomb shaped like the US dollar sign. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_10.png"
    },
    {
        "tag": "[c1:11]",
        "prompt": "[c1:11] A satirical editorial political cartoon of a smart investor using a shining shield branded with a YouTube 'Subscribe' button to block a torrential downpour of heavy, spiked tax bills and debt envelopes from falling onto a crowd of struggling people. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_11.png"
    },
    {
        "tag": "[c1:12]",
        "prompt": "[c1:12] A satirical editorial political cartoon of a serious professor pointing at a chalkboard with financial equations, while firmly pushing away a flashy, sleazy casino slot machine that has a massive red 'NO' symbol drawn over it. Exaggerated caricature style, dramatic ink lines, watercolor shading, The Economist magazine style, newspaper political satire, highly detailed.",
        "filename": "c1_12.png"
    }
];
    
    const delay = ms => new Promise(r => setTimeout(r, ms));
    
    // Auto-download helper
    async function downloadImage(imgSrc, filename) {
        try {
            const response = await fetch(imgSrc);
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            console.log("%c✅ Đã tải thành công: " + filename, "color: #00ff00;");
        } catch (e) {
            console.error("❌ Lỗi tải ảnh: " + filename, e);
        }
    }

    async function getLatestImageCount() {
        return document.querySelectorAll('img[src^="blob:"], img[src*="assets.grok.com"]').length;
    }

    for (let i = 0; i < promptsData.length; i++) {
        const item = promptsData[i];
        console.log(`⏳ Bắt đầu xử lý: ${item.tag} (${i+1}/${promptsData.length})`);
        
        // 1. Tìm Textarea
        const textarea = document.querySelector('textarea');
        if (!textarea) {
            console.error("❌ Không tìm thấy ô nhập liệu (Textarea)!");
            return;
        }

        // 2. Nhập Prompt
        textarea.value = item.prompt;
        textarea.dispatchEvent(new Event('input', { bubbles: true }));
        await delay(1000);
        
        let initialImageCount = await getLatestImageCount();

        // 3. Click nút Submit / Enter
        const submitBtn = document.querySelector('button[aria-label="Grok something"], button[type="submit"]') || textarea.nextElementSibling;
        if (submitBtn && submitBtn.tagName === 'BUTTON') {
            submitBtn.click();
        } else {
            // Cố gắng giả lập phím Enter nếu không có nút rõ ràng
            textarea.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
        }

        console.log(`🤖 Đã gửi lệnh Grok. Chờ ảnh (thường tốn 10-20s)...`);
        
        // 4. Polling chờ UI cập nhật trả về dòng ảnh mới
        let isDone = false;
        let waitLoops = 0;
        let newImageSrc = null;
        
        while (!isDone && waitLoops < 60) { // Chờ tối đa 60s
            await delay(1000);
            waitLoops++;
            
            // Cách tốt nhất là đếm số lượng <img src="blob..."> tăng lên
            const currentImages = Array.from(document.querySelectorAll('img[src^="blob:"], img[src*="assets.grok.com"]'));
            if (currentImages.length >= initialImageCount + 4) { // Grok thường xuất 4 ảnh
                isDone = true;
                // Lấy ảnh ĐẦU TIÊN trong nhóm 4 ảnh mới sinh ra
                const targetImg = currentImages[currentImages.length - 4];
                newImageSrc = targetImg.src;
            }
        }
        
        if (newImageSrc) {
            console.log(`📦 Đã thấy ảnh mới: ${newImageSrc}. Tiến hành tải về...`);
            await downloadImage(newImageSrc, item.filename);
        } else {
            console.error(`⏱ Quá thời gian chờ (Timeout) cho lệnh ${item.tag}`);
        }
        
        // 5. Nghỉ 5 giây trước khi bắn câu tiếp theo để tránh bị Grok block rate-limit
        console.log(`⏳ Nghỉ 5 giây trước câu tiếp theo...`);
        await delay(5000);
    }
    
    console.log("%c🎉 HOÀN TẤT TOÀN BỘ QUY TRÌNH!", "color: yellow; font-size: 20px; font-weight: bold;");
})();
