const fs = require('fs');
const path = require('path');

const episodeDir = '/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/kim-cuong-gia';

const LAB_DIRECTOR_DESC = 'a Vietnamese man in his late 40s with Asian features, thin face, short neat graying hair, wearing a white laboratory lab coat, wire-rimmed glasses, intense focused expression';
const WEALTHY_BUYER_DESC = 'a Vietnamese woman in her late 30s with Asian features, elegant features, long black hair tied up in a bun, wearing a loose flowing silk dark blouse, worried expression';

function rewriteImagePrompt(rawPrompt) {
    // Determine the theme suffixes in the original prompt
    const hasVN = rawPrompt.includes('culturally authentic Vietnamese elements') || rawPrompt.includes('warm organic tones');
    const hasTech = rawPrompt.includes('cyber-minimalism') || rawPrompt.includes('glowing data streams');
    const hasGlobal = rawPrompt.includes('geopolitics') || rawPrompt.includes('international');
    
    // Clean style suffixes out of the raw prompt
    let subject = rawPrompt;
    const suffixes = [
        ', culturally authentic Vietnamese elements',
        ', warm organic tones',
        ', futuristic cyber-minimalism',
        ', high-tech engineering background',
        ', glowing data streams',
        ', cinematic editorial illustration style',
        ', minimalist graphic novel aesthetic',
        ', clean ink outlines',
        ', dramatic chiaroscuro lighting',
        ', deep noir shadows',
        ', modern international geopolitics theme',
        ', highly detailed atmospheric background'
    ];
    
    for (const suffix of suffixes) {
        subject = subject.split(suffix).join('');
    }
    
    // Trim and clean extra punctuation
    subject = subject.trim();
    if (subject.endsWith('.')) subject = subject.slice(0, -1);
    
    // Normalize leading articles
    subject = subject.replace(/^(A\s+|An\s+|The\s+)/i, '');
    
    // Apply visual cast sheet replacements
    // Case 1: Lab Director
    if (/Lab Director/i.test(subject) || /gemologist/i.test(subject) || /lab expert/i.test(subject)) {
        const actionMatch = subject.match(/(?:The\s+)?(?:Lab Director|gemologist|lab expert)(?:\s+in\s+a\s+white\s+coat)?\s*(looking|examining|working|shaking|sitting|bench|signing)(.*)$/i);
        if (actionMatch) {
            const verb = actionMatch[1].trim();
            let actionText = actionMatch[2].trim();
            // clean up redundant phrases
            actionText = actionText.replace(/with a stressed expression/i, '').replace(/stressed expression/i, '');
            if (actionText.startsWith(',')) actionText = actionText.substring(1).trim();
            
            subject = `${LAB_DIRECTOR_DESC}, ${verb} ${actionText}`;
        } else {
            subject = subject.replace(/(?:The\s+)?(?:Lab Director|gemologist|lab expert)(?:\s+in\s+a\s+white\s+coat)?/i, LAB_DIRECTOR_DESC);
        }
    }
    
    // Case 2: Wealthy Buyer / Vietnamese woman
    if (/Vietnamese woman/i.test(subject) || /Wealthy Buyer/i.test(subject) || /anxious buyer/i.test(subject)) {
        const actionMatch = subject.match(/(?:beautiful\s+)?(?:Vietnamese woman|Wealthy Buyer|anxious buyer)(?:\s+in\s+her\s+late\s+30s)?\s*(wearing|looking|holding|standing|sitting|touching)(.*)$/i);
        if (actionMatch) {
            const verb = actionMatch[1].trim();
            let actionText = actionMatch[2].trim();
            // Clean up redundant "worried expression" or similar since it's already in WEALTHY_BUYER_DESC
            actionText = actionText.replace(/with a worried expression/i, '').replace(/worried expression/i, '');
            if (actionText.startsWith(',')) actionText = actionText.substring(1).trim();
            
            subject = `${WEALTHY_BUYER_DESC}, ${verb} ${actionText}`;
        } else {
            subject = subject.replace(/(?:beautiful\s+)?(?:Vietnamese woman|Wealthy Buyer|anxious buyer)(?:\s+in\s+her\s+late\s+30s)?/i, WEALTHY_BUYER_DESC);
        }
    }
    
    // General text cleanup
    subject = subject.replace(/\b(a|an)\s+(a|an)\b/ig, 'a');
    subject = subject.replace(/\s+/g, ' ').trim();
    
    // Lowercase first letter of subject
    subject = subject.charAt(0).toLowerCase() + subject.slice(1);
    
    // Clean up trailing commas or double punctuation
    subject = subject.replace(/,\s*,/g, ',');
    subject = subject.replace(/,\s*$/g, '');
    
    // Build style suffix (2D flat vector, clean bold outlines, flat colors, noir aesthetic)
    let themePart = '';
    if (hasTech) {
        themePart = ', futuristic cyber-minimalism, high-tech engineering background, glowing data streams';
    } else if (hasGlobal) {
        themePart = ', modern international geopolitics theme';
    } else if (hasVN) {
        themePart = ', culturally authentic Vietnamese elements, warm organic tones';
    }
    
    const styleSuffix = `, clean bold outlines, flat colors, in a minimalist graphic novel aesthetic, dramatic chiaroscuro lighting, deep noir shadows${themePart}`;
    
    return `A flat 2D vector illustration of ${subject}${styleSuffix}`;
}

function rewriteVideoPrompt(rawPrompt, isI2V) {
    if (isI2V) {
        return rawPrompt;
    }
    
    const hasVN = rawPrompt.includes('culturally authentic Vietnamese elements') || rawPrompt.includes('warm organic tones');
    const hasTech = rawPrompt.includes('cyber-minimalism') || rawPrompt.includes('glowing data streams');
    const hasGlobal = rawPrompt.includes('geopolitics') || rawPrompt.includes('international');
    
    let cleanPrompt = rawPrompt;
    const suffixes = [
        ', culturally authentic Vietnamese elements',
        ', warm organic tones',
        ', futuristic cyber-minimalism',
        ', high-tech engineering background',
        ', glowing data streams',
        ', cinematic editorial illustration style',
        ', minimalist graphic novel aesthetic',
        ', clean ink outlines',
        ', dramatic chiaroscuro lighting',
        ', deep noir shadows',
        ', modern international geopolitics theme',
        ', highly detailed atmospheric background',
        ', 8-second continuous documentary video --ar 16:9'
    ];
    
    for (const suffix of suffixes) {
        cleanPrompt = cleanPrompt.split(suffix).join('');
    }
    
    cleanPrompt = cleanPrompt.trim();
    if (cleanPrompt.endsWith('.')) cleanPrompt = cleanPrompt.slice(0, -1);
    
    let themePart = '';
    if (hasTech) {
        themePart = ', futuristic cyber-minimalism, high-tech engineering background, glowing data streams';
    } else if (hasGlobal) {
        themePart = ', modern international geopolitics theme';
    } else if (hasVN) {
        themePart = ', culturally authentic Vietnamese elements, warm organic tones';
    }
    
    const styleSuffix = `, clean bold outlines, flat colors, in a minimalist graphic novel aesthetic, dramatic chiaroscuro lighting, deep noir shadows${themePart}, 8-second continuous documentary video --ar 16:9`;
    
    return `A flat 2D vector video showing ${cleanPrompt}${styleSuffix}`;
}

function processFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n');
    let outputLines = [];
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) {
            outputLines.push('');
            continue;
        }
        
        const imageMatch = line.match(/^(CH\d+_SC\d+)\s+\[IMAGE\]:\s*(.*)$/);
        const videoMatch = line.match(/^(CH\d+_SC\d+)\s+\[VIDEO\]:\s*(.*)$/);
        
        if (imageMatch) {
            const sceneId = imageMatch[1];
            const rawPrompt = imageMatch[2];
            const rewritten = rewriteImagePrompt(rawPrompt);
            outputLines.push(`${sceneId} [IMAGE]: ${rewritten}`);
        } else if (videoMatch) {
            const sceneId = videoMatch[1];
            const rawPrompt = videoMatch[2];
            const isI2V = rawPrompt.includes('->');
            
            if (isI2V) {
                outputLines.push(`${sceneId} [VIDEO]: ${rawPrompt}`);
            } else {
                const rewritten = rewriteVideoPrompt(rawPrompt, false);
                outputLines.push(`${sceneId} [VIDEO]: ${rewritten}`);
            }
        } else {
            outputLines.push(line);
        }
    }
    
    fs.writeFileSync(filePath, outputLines.join('\n'), 'utf-8');
    console.log(`Rewrote: ${filePath}`);
}

function main() {
    console.log('Starting visual style coherence rewriting (strictly 2D flat vector)...');
    
    for (let ch = 1; ch <= 8; ch++) {
        const chStr = String(ch).padStart(2, '0');
        const chFile = path.join(episodeDir, `ch${chStr}_prompts.txt`);
        if (fs.existsSync(chFile)) {
            processFile(chFile);
        }
    }
    
    const globalFile = path.join(episodeDir, 'prompts.txt');
    if (fs.existsSync(globalFile)) {
        processFile(globalFile);
    }
    
    console.log('Splitting prompts.txt into image_prompts.txt and video_prompts.txt...');
    const globalContent = fs.readFileSync(globalFile, 'utf-8');
    const lines = globalContent.split('\n');
    let imageLines = [];
    let videoLines = [];
    
    for (const line of lines) {
        const trimmed = line.trim();
        if (!trimmed) continue;
        
        const imageMatch = trimmed.match(/^(CH\d+_SC\d+)\s+\[IMAGE\]:\s*(.*)$/);
        const videoMatch = trimmed.match(/^(CH\d+_SC\d+)\s+\[VIDEO\]:\s*(.*)$/);
        
        if (imageMatch) {
            imageLines.push(`${imageMatch[1]}: ${imageMatch[2]}`);
        } else if (videoMatch) {
            videoLines.push(`${videoMatch[1]}: ${videoMatch[2]}`);
        }
    }
    
    fs.writeFileSync(path.join(episodeDir, 'image_prompts.txt'), imageLines.join('\n\n'), 'utf-8');
    fs.writeFileSync(path.join(episodeDir, 'video_prompts.txt'), videoLines.join('\n\n'), 'utf-8');
    console.log('Successfully wrote image_prompts.txt and video_prompts.txt!');
    console.log('Coherence rewriting completed successfully!');
}

main();
