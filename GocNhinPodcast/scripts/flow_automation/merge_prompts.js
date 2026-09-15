const fs = require('fs');
const path = require('path');

const episodeDir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kim-cuong-gia';

function parsePrompts(filePath) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n');
    const promptMap = new Map();
    
    for (let line of lines) {
        line = line.trim();
        if (!line) continue;
        
        // Match "SCENE_ID: Content"
        const colonIndex = line.indexOf(':');
        if (colonIndex === -1) continue;
        
        const sceneId = line.substring(0, colonIndex).trim();
        let contentPart = line.substring(colonIndex + 1).trim();
        
        promptMap.set(sceneId, contentPart);
    }
    
    return promptMap;
}

function main() {
    let globalPrompts = [];
    
    for (let ch = 1; ch <= 8; ch++) {
        const chStr = String(ch).padStart(2, '0');
        const imgFile = path.join(episodeDir, `ch${chStr}_image_prompts.txt`);
        const vidFile = path.join(episodeDir, `ch${chStr}_video_prompts.txt`);
        const mergedFile = path.join(episodeDir, `ch${chStr}_prompts.txt`);
        
        if (!fs.existsSync(imgFile) || !fs.existsSync(vidFile)) {
            console.warn(`Missing file for chapter ${chStr}`);
            continue;
        }
        
        console.log(`Merging prompts for Chapter ${chStr}...`);
        const imgMap = parsePrompts(imgFile);
        const vidMap = parsePrompts(vidFile);
        
        // Get all scene IDs in order
        const sceneIds = Array.from(imgMap.keys());
        let chPrompts = [];
        
        for (const sceneId of sceneIds) {
            const imgPrompt = imgMap.get(sceneId);
            let vidPrompt = vidMap.get(sceneId) || '';
            
            // Clean up any "@sceneId.png -> " prefix in the raw video prompt if it exists,
            // to make sure we format it cleanly.
            const prefixRegex = new RegExp(`^@${sceneId}\\.png\\s*->\\s*`, 'i');
            vidPrompt = vidPrompt.replace(prefixRegex, '').trim();
            
            // Format to:
            // CH07_SC032 [IMAGE]: ...
            // CH07_SC032 [VIDEO]: @CH07_SC032.png -> ...
            const imgLine = `${sceneId} [IMAGE]: ${imgPrompt}`;
            const vidLine = `${sceneId} [VIDEO]: @${sceneId}.png -> ${vidPrompt}`;
            
            chPrompts.push(imgLine);
            chPrompts.push(vidLine);
            chPrompts.push(''); // Empty line separating scenes
            
            globalPrompts.push(imgLine);
            globalPrompts.push(vidLine);
            globalPrompts.push('');
        }
        
        fs.writeFileSync(mergedFile, chPrompts.join('\n'), 'utf-8');
        console.log(`Saved merged file to: ${mergedFile}`);
    }
    
    // Save global prompts.txt
    const globalFile = path.join(episodeDir, `prompts.txt`);
    fs.writeFileSync(globalFile, globalPrompts.join('\n'), 'utf-8');
    console.log(`Saved global merged file to: ${globalFile}`);
}

main();
