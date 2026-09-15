#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { resolveVoiceCode, processSingleChunk } = require('./tts_client');

async function recordFile(filePath) {
  if (!fs.existsSync(filePath)) {
    console.error(`❌ Lỗi: Không tìm thấy file ${filePath}`);
    process.exit(1);
  }

  const absolutePath = path.resolve(filePath);
  console.log(`🎙️  Đang chuẩn bị thu âm file: ${absolutePath}`);

  // Đọc nội dung
  const content = fs.readFileSync(absolutePath, 'utf-8').trim();
  if (content.length === 0) {
    console.error(`❌ Lỗi: File rỗng!`);
    process.exit(1);
  }

  // Determine output path (change extension to .mp3)
  const dir = path.dirname(absolutePath);
  const ext = path.extname(absolutePath);
  const baseName = path.basename(absolutePath, ext);
  const outputPath = path.join(dir, `${baseName}.mp3`);

  console.log(`Số ký tự sẽ gửi: ${content.length}`);

  try {
    const voiceCode = await resolveVoiceCode();
    await processSingleChunk(content, voiceCode, outputPath);
    console.log(`\n✅ THÀNH CÔNG! Đã ghép và lưu audio tại: ${outputPath}`);
  } catch (error) {
    console.error(`\n❌ THẤT BẠI: ${error.message}`);
    process.exit(1);
  }
}

const targetFile = process.argv[2];
if (!targetFile) {
  console.log('Sử dụng: node record_file.js <đường_dẫn_đến_file.md>');
  process.exit(1);
}

recordFile(targetFile);
