#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { fetchTranscriptWithFallback } = require('./youtube_transcript_service.cjs');

function ensureDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

function writeJson(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

function writeStatusMarkdown(filePath, result) {
  const lines = [
    '# Transcript Extraction Status',
    '',
    `- status: ${result.status}`,
    `- source_backend: ${result.sourceBackend || 'unknown'}`,
    `- video_id: ${result.videoId || 'unknown'}`,
    `- url: ${result.url || 'unknown'}`,
    `- fetched_at: ${result.fetchedAt || new Date().toISOString()}`,
    `- error_code: ${result.error?.code || 'none'}`,
    `- error_message: ${result.error?.message || 'none'}`,
    `- retryable: ${result.error?.retryable === true ? 'yes' : 'no'}`,
    '',
    '## Attempts',
    '',
  ];

  for (const attempt of result.attempts || []) {
    lines.push(`- variant: ${attempt.variant}`);
    lines.push(`  status: ${attempt.status}`);
    if (attempt.error) {
      lines.push(`  error_code: ${attempt.error.code}`);
      lines.push(`  error_message: ${attempt.error.message}`);
    }
  }

  if (result.warnings?.length) {
    lines.push('', '## Warnings', '');
    for (const warning of result.warnings) {
      lines.push(`- ${warning}`);
    }
  }

  lines.push(
    '',
    '## Next Step',
    '',
    '- Nếu transcript không khả dụng, không được suy đoán nội dung video từ URL.',
    '- Hãy dùng metadata/status artifact này để quyết định: đổi video, thử lại sau, hoặc yêu cầu transcript thủ công từ user.'
  );

  fs.writeFileSync(filePath, lines.join('\n'), 'utf8');
}

async function extractTranscript(url, outputDir) {
  console.log(`⏳ Đang bóc transcript cho URL: ${url}`);
  ensureDir(outputDir);

  const result = await fetchTranscriptWithFallback(url);

  const metaPath = path.join(outputDir, '00_transcript_meta.json');
  const segmentsPath = path.join(outputDir, '00_transcript_segments.json');
  const rawPath = path.join(outputDir, '00_raw_transcript.txt');
  const errorPath = path.join(outputDir, '00_transcript_error.json');
  const statusPath = path.join(outputDir, '00_transcript_status.md');

  const meta = {
    status: result.status,
    sourceBackend: result.sourceBackend,
    fetchedAt: result.fetchedAt,
    url: result.url,
    videoId: result.videoId,
    language: result.language || null,
    wordCount: result.wordCount || 0,
    charCount: result.charCount || 0,
    segmentCount: result.segmentCount || 0,
    warnings: result.warnings || [],
    attempts: result.attempts || [],
    error: result.error || null,
  };

  writeJson(metaPath, meta);

  if (result.ok) {
    fs.writeFileSync(rawPath, result.fullText, 'utf8');
    writeJson(segmentsPath, {
      status: result.status,
      sourceBackend: result.sourceBackend,
      videoId: result.videoId,
      url: result.url,
      language: result.language || null,
      fetchedAt: result.fetchedAt,
      segments: result.segments,
    });

    if (fs.existsSync(errorPath)) fs.unlinkSync(errorPath);
    if (fs.existsSync(statusPath)) fs.unlinkSync(statusPath);

    console.log(`✅ THÀNH CÔNG: ${result.wordCount} từ, ${result.segmentCount} segments.`);
    console.log(`📂 Raw transcript: ${rawPath}`);
    console.log(`📂 Meta: ${metaPath}`);
    console.log(`📂 Segments: ${segmentsPath}`);
    return 0;
  }

  writeJson(errorPath, {
    status: result.status,
    sourceBackend: result.sourceBackend,
    fetchedAt: result.fetchedAt,
    url: result.url,
    videoId: result.videoId,
    warnings: result.warnings || [],
    attempts: result.attempts || [],
    error: result.error || null,
  });
  writeStatusMarkdown(statusPath, result);

  if (fs.existsSync(rawPath)) fs.unlinkSync(rawPath);
  if (fs.existsSync(segmentsPath)) fs.unlinkSync(segmentsPath);

  console.error(`❌ Không lấy được transcript: ${result.error?.message || 'Unknown error'}`);
  console.error(`📂 Meta: ${metaPath}`);
  console.error(`📂 Status: ${statusPath}`);
  console.error(`📂 Error: ${errorPath}`);

  if (result.status === 'invalid_input') return 1;
  if (result.status === 'no_transcript') return 2;
  return 3;
}

const url = process.argv[2];
const outputDir = process.argv[3];

if (!url || !outputDir) {
  console.error('⚠️ Hướng dẫn: node extract_transcript.cjs <youtube_url_or_video_id> <thu_muc_luu_tru>');
  process.exit(1);
}

extractTranscript(url, outputDir)
  .then((code) => process.exit(code))
  .catch((error) => {
    console.error(`💥 Lỗi nghiêm trọng: ${error.message}`);
    process.exit(4);
  });
