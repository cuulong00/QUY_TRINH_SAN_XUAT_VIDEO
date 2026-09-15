#!/usr/bin/env node
/**
 * record_episode.js — Main Orchestrator
 * Automates the full TTS pipeline:
 *   final_voiceover.md → split → TTS → download → merge → full_voiceover.mp3
 * 
 * Usage:
 *   node scripts/tts/record_episode.js <episode-slug>
 *   node scripts/tts/record_episode.js buong-bo-nguoi-cu
 */
const fs = require('fs');
const path = require('path');

const { resolveVoiceCode, processSingleChunk, loadConfig, sleep } = require('./tts_client');
const { splitByChapters, printSummary } = require('./chunk_splitter');
const { mergeAudioFiles, printAudioSummary, checkFfmpeg } = require('./audio_merger');

const PROJECT_ROOT = path.resolve(__dirname, '..', '..');

async function recordEpisode(slug) {
  const startTime = Date.now();
  
  console.log('╔══════════════════════════════════════════════════════╗');
  console.log('║         🎙️  VBEE TTS — Thu âm tự động              ║');
  console.log('╚══════════════════════════════════════════════════════╝');
  console.log(`\n📂 Episode: ${slug}\n`);

  // ─── 1. Verify prerequisites ───
  const episodeDir = path.join(PROJECT_ROOT, 'episodes', slug);
  const checkChapterPath = path.join(episodeDir, 'chapter_01.md');
  
  if (!fs.existsSync(episodeDir)) {
    throw new Error(`❌ Thư mục episode không tồn tại: episodes/${slug}/`);
  }
  
  if (!fs.existsSync(checkChapterPath)) {
    throw new Error(`❌ File kịch bản chưa có: episodes/${slug}/chapter_01.md`);
  }

  if (!checkFfmpeg()) {
    console.warn('⚠️  ffmpeg chưa cài đặt. Sẽ bỏ qua bước ghép audio.');
    console.warn('   Cài bằng: brew install ffmpeg\n');
  }

  // ─── 2. Resolve voice code ───
  console.log('━'.repeat(55));
  console.log('BƯỚC 1: Xác định giọng đọc');
  console.log('━'.repeat(55));
  const voiceCode = await resolveVoiceCode();
  console.log(`🎤 Giọng đọc: ${voiceCode}\n`);

  // ─── 3. Split voiceover into chunks ───
  console.log('━'.repeat(55));
  console.log('BƯỚC 2: Tách kịch bản theo chương');
  console.log('━'.repeat(55));
  const chunks = splitByChapters(episodeDir);
  printSummary(chunks);

  if (chunks.length === 0) {
    throw new Error('❌ Không tìm thấy file chapter_*.md nào trong thư mục.');
  }

  // ─── 4. Create audio output directory ───
  const audioDir = path.join(episodeDir, 'audio');
  if (!fs.existsSync(audioDir)) {
    fs.mkdirSync(audioDir, { recursive: true });
  }

  // ─── 5. Process each chunk ───
  console.log('━'.repeat(55));
  console.log('BƯỚC 3: Thu âm từng chương');
  console.log('━'.repeat(55));
  
  const audioFiles = [];
  const results = [];

  for (const chunk of chunks) {
    // Descriptive filename from chapter title
    const titleSlug = chunk.title
      .toLowerCase()
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
      .replace(/đ/g, 'd').replace(/Đ/g, 'D')
      .replace(/[^a-z0-9]+/g, '_')
      .replace(/^_|_$/g, '')
      .substring(0, 40);
    const chunkFileName = `${String(chunk.index).padStart(2, '0')}_${titleSlug}.mp3`;
    const outputPath = path.join(audioDir, chunkFileName);
    
    console.log(`\n📖 [${chunk.index}/${chunks.length}] ${chunk.title} (${chunk.wordCount} từ)`);
    
    // Check if already processed (for resume capability)
    if (fs.existsSync(outputPath) && fs.statSync(outputPath).size > 1000) {
      console.log(`⏭️  Đã có file, bỏ qua. (Xóa file để thu lại)`);
      audioFiles.push(outputPath);
      results.push({ chunk: chunk.index, title: chunk.title, status: 'skipped', file: chunkFileName });
      continue;
    }

    try {
      await processSingleChunk(chunk.text, voiceCode, outputPath);
      audioFiles.push(outputPath);
      results.push({ chunk: chunk.index, title: chunk.title, status: 'success', file: chunkFileName });
      
      // Small delay between chunks to be nice to the API
      if (chunk.index < chunks.length) {
        console.log('⏳ Chờ 2 giây trước chunk tiếp...');
        await sleep(2000);
      }
    } catch (err) {
      console.error(`\n❌ Lỗi chunk ${chunk.index}: ${err.message}`);
      results.push({ chunk: chunk.index, title: chunk.title, status: 'failed', error: err.message });
    }
  }

  // ─── 6. Audio files kept separate for post-production ───
  const successFiles = audioFiles.filter(f => fs.existsSync(f));
  
  if (successFiles.length > 0) {
    console.log('\n' + '━'.repeat(55));
    console.log('BƯỚC 4: Tổng hợp file audio (giữ riêng từng chương)');
    console.log('━'.repeat(55));
    console.log(`📁 ${successFiles.length} file MP3 riêng lẻ trong: episodes/${slug}/audio/`);
    console.log('💡 Các file được đặt tên theo thứ tự chương để dễ xử lý hậu kỳ.');
  }

  // ─── 7. Print final report ───
  const elapsed = ((Date.now() - startTime) / 1000 / 60).toFixed(1);
  const successCount = results.filter(r => r.status === 'success' || r.status === 'skipped').length;
  const failCount = results.filter(r => r.status === 'failed').length;

  console.log('\n' + '═'.repeat(55));
  console.log('📊 BÁO CÁO THU ÂM');
  console.log('═'.repeat(55));
  console.log(`  Episode:      ${slug}`);
  console.log(`  Tổng chunks:  ${chunks.length}`);
  console.log(`  Thành công:   ${successCount} ✅`);
  console.log(`  Thất bại:     ${failCount} ❌`);
  console.log(`  Thời gian:    ${elapsed} phút`);
  console.log(`  Thư mục:      episodes/${slug}/audio/`);
  
  if (failCount > 0) {
    console.log(`\n⚠️  Chunks thất bại:`);
    for (const r of results.filter(r => r.status === 'failed')) {
      console.log(`    ${r.chunk}. ${r.title}: ${r.error}`);
    }
    console.log(`\n💡 Chạy lại lệnh để retry các chunks thất bại (file đã có sẽ được bỏ qua).`);
  }
  
  console.log('═'.repeat(55) + '\n');

  // Save report file
  const reportPath = path.join(audioDir, 'recording_report.json');
  fs.writeFileSync(reportPath, JSON.stringify({
    slug,
    timestamp: new Date().toISOString(),
    voiceCode,
    chunks: results,
    elapsedMinutes: parseFloat(elapsed),
  }, null, 2), 'utf-8');

  return results;
}

// ─── CLI Entry Point ───
const slug = process.argv[2];

if (!slug) {
  console.log('🎙️  VBEE TTS Recorder');
  console.log('━'.repeat(40));
  console.log('Sử dụng:');
  console.log('  node scripts/tts/record_episode.js <episode-slug>');
  console.log('');
  console.log('Ví dụ:');
  console.log('  node scripts/tts/record_episode.js buong-bo-nguoi-cu');
  console.log('');
  console.log('Yêu cầu:');
  console.log('  - File episodes/<slug>/chapter_01.md phải tồn tại');
  console.log('  - ffmpeg đã cài (brew install ffmpeg)');
  console.log('  - API key đã cấu hình trong scripts/tts/config.json');
  process.exit(1);
}

recordEpisode(slug)
  .then(() => process.exit(0))
  .catch((err) => {
    console.error(`\n💥 Lỗi nghiêm trọng: ${err.message}`);
    process.exit(1);
  });
