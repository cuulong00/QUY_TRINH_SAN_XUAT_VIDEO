/**
 * chunk_splitter.js — Smart Chapter-Based Voiceover Splitter
 * Splits final_voiceover.md into chunks based on chapter boundaries.
 */
const fs = require('fs');
const path = require('path');

/**
 * Gather voiceover text by scanning chapter files in the episode directory.
 * Recognizes: chapter_01.md, chapter_02.md...
 *
 * @param {string} episodeDir - Path to the episode directory
 * @returns {Array<{index: number, title: string, text: string, wordCount: number}>}
 */
function splitByChapters(episodeDir) {
  if (!fs.existsSync(episodeDir)) {
    throw new Error(`Directory not found: ${episodeDir}`);
  }

  const files = fs.readdirSync(episodeDir);
  const chapterFiles = files
    .filter(file => file.match(/^chapter_\d+\.md$/i) || file.match(/^intro\.md$/i) || file.match(/^outro\.md$/i))
    .sort((a, b) => {
      // Custom sort: intro first, then chapters numerically, then outro
      if (a === 'intro.md') return -1;
      if (b === 'intro.md') return 1;
      if (a === 'outro.md') return 1;
      if (b === 'outro.md') return -1;
      return a.localeCompare(b);
    });

  if (chapterFiles.length === 0) {
    return [];
  }

  const chunks = [];
  let index = 1;

  for (const file of chapterFiles) {
    const filePath = path.join(episodeDir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const cleanText = cleanForTTS(content);

    if (cleanText.trim().length > 0) {
      let title = file.replace('.md', '');
      // Make title human readable
      if (title.startsWith('chapter_')) {
        title = `Chương ${parseInt(title.split('_')[1], 10)}`;
      } else if (title === 'intro') {
        title = 'Mở đầu';
      } else if (title === 'outro') {
        title = 'Kết thúc';
      }

      chunks.push({
        index: index++,
        title: title,
        text: cleanText,
        wordCount: countWords(cleanText),
      });
    }
  }

  return chunks;
}

/**
 * Clean markdown text for TTS input.
 * Removes formatting while preserving readable text.
 */
function cleanForTTS(text) {
  let cleaned = text;

  // Strip metadata-style preamble at the top of final_voiceover files
  const lines = cleaned.split('\n');
  let bodyStart = 0;
  while (bodyStart < lines.length) {
    const line = lines[bodyStart].trim();
    if (!line) {
      bodyStart += 1;
      continue;
    }
    if (/^[a-zA-Z_][a-zA-Z0-9_]*:\s*/.test(line) || /^-\s+[a-zA-Z_][a-zA-Z0-9_]*$/.test(line)) {
      bodyStart += 1;
      continue;
    }
    break;
  }
  cleaned = lines.slice(bodyStart).join('\n');

  return cleaned
    // Remove markdown headings (keep the text)
    .replace(/^#{1,6}\s+/gm, '')
    // Remove bold/italic markers
    .replace(/\*{1,3}([^*]+)\*{1,3}/g, '$1')
    .replace(/_{1,3}([^_]+)_{1,3}/g, '$1')
    // Remove markdown links [text](url) → text
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    // Remove images
    .replace(/!\[.*?\]\(.*?\)/g, '')
    // Remove horizontal rules
    .replace(/^---+$/gm, '')
    // Remove blockquote markers
    .replace(/^>\s?/gm, '')
    // Remove code blocks
    .replace(/```[\s\S]*?```/g, '')
    .replace(/`([^`]+)`/g, '$1')
    // Remove HTML tags
    .replace(/<[^>]*>/g, '')
    // Clean up multiple newlines → max 2
    .replace(/\n{3,}/g, '\n\n')
    // Trim
    .trim();
}

/**
 * Count Vietnamese words (approximate)
 */
function countWords(text) {
  return text.split(/\s+/).filter((w) => w.length > 0).length;
}

/**
 * Split long text into paragraph-based chunks sized for TTS.
 */
function splitLongText(text, maxWords = 1100) {
  const paragraphs = text
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter(Boolean);

  const chunks = [];
  let current = [];
  let currentWords = 0;

  for (const paragraph of paragraphs) {
    const paragraphWords = countWords(paragraph);

    if (current.length > 0 && currentWords + paragraphWords > maxWords) {
      const chunkText = current.join('\n\n').trim();
      chunks.push({
        index: chunks.length + 1,
        title: `Phần ${chunks.length + 1}`,
        text: chunkText,
        wordCount: countWords(chunkText),
      });
      current = [];
      currentWords = 0;
    }

    current.push(paragraph);
    currentWords += paragraphWords;
  }

  if (current.length > 0) {
    const chunkText = current.join('\n\n').trim();
    chunks.push({
      index: chunks.length + 1,
      title: `Phần ${chunks.length + 1}`,
      text: chunkText,
      wordCount: countWords(chunkText),
    });
  }

  return chunks;
}

/**
 * Print chunk summary
 */
function printSummary(chunks) {
  console.log('\n📑 Kết quả tách chương:');
  console.log('─'.repeat(60));
  
  let totalWords = 0;
  for (const chunk of chunks) {
    const bar = '█'.repeat(Math.min(Math.round(chunk.wordCount / 50), 30));
    console.log(`  ${String(chunk.index).padStart(2, '0')}. ${chunk.title.substring(0, 30).padEnd(30)} ${String(chunk.wordCount).padStart(5)} từ ${bar}`);
    totalWords += chunk.wordCount;
  }
  
  console.log('─'.repeat(60));
  console.log(`  Tổng: ${chunks.length} chunks, ${totalWords} từ`);
  console.log(`  Thời lượng ước tính: ${Math.round(totalWords / 150)}–${Math.round(totalWords / 120)} phút\n`);
}

// CLI mode
if (require.main === module) {
  const episodeDir = process.argv[2];
  if (!episodeDir) {
    console.log('Sử dụng: node chunk_splitter.js <path/to/episodes/slug>');
    process.exit(1);
  }

  if (!fs.existsSync(episodeDir)) {
    console.error(`❌ Thư mục không tồn tại: ${episodeDir}`);
    process.exit(1);
  }

  const chunks = splitByChapters(episodeDir);
  printSummary(chunks);
  
  // Optionally save chunks to individual files
  if (process.argv.includes('--save')) {
    const dir = path.join(path.dirname(filePath), 'tts_chunks');
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    
    for (const chunk of chunks) {
      const fileName = `chunk_${String(chunk.index).padStart(2, '0')}.txt`;
      fs.writeFileSync(path.join(dir, fileName), chunk.text, 'utf-8');
    }
    console.log(`💾 Đã lưu ${chunks.length} chunks vào ${dir}/`);
  }
}

module.exports = { splitByChapters, cleanForTTS, countWords, printSummary };
