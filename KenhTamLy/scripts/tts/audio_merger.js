/**
 * audio_merger.js — Merge MP3 chunks into one final audio file using ffmpeg.
 * Inserts configurable silence between chapters.
 */
const { execSync, exec } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * Check if ffmpeg is installed
 */
function checkFfmpeg() {
  try {
    execSync('which ffmpeg', { stdio: 'pipe' });
    return true;
  } catch {
    return false;
  }
}

/**
 * Generate a silence audio file
 * @param {number} durationMs - Duration in milliseconds
 * @param {string} outputPath - Output file path
 */
function generateSilence(durationMs, outputPath) {
  const durationSec = durationMs / 1000;
  execSync(
    `ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t ${durationSec} -q:a 9 "${outputPath}"`,
    { stdio: 'pipe' }
  );
}

/**
 * Merge multiple MP3 files with silence between them
 * @param {string[]} inputFiles - Array of MP3 file paths (in order)
 * @param {string} outputPath - Output merged MP3 path
 * @param {number} silenceMs - Silence duration between files (default: 2000ms)
 */
function mergeAudioFiles(inputFiles, outputPath, silenceMs = 2000) {
  if (!checkFfmpeg()) {
    throw new Error(
      'ffmpeg chưa được cài đặt. Hãy cài bằng: brew install ffmpeg'
    );
  }

  if (inputFiles.length === 0) {
    throw new Error('Không có file audio nào để ghép.');
  }

  if (inputFiles.length === 1) {
    // Just copy the single file
    fs.copyFileSync(inputFiles[0], outputPath);
    console.log(`📋 Chỉ có 1 file, copy trực tiếp → ${path.basename(outputPath)}`);
    return outputPath;
  }

  const tempDir = path.join(path.dirname(outputPath), '.temp_merge');
  if (!fs.existsSync(tempDir)) fs.mkdirSync(tempDir, { recursive: true });

  try {
    // Generate silence file
    const silenceFile = path.join(tempDir, 'silence.mp3');
    if (silenceMs > 0) {
      generateSilence(silenceMs, silenceFile);
    }

    // Build concat list: file1 + silence + file2 + silence + ... + fileN
    const concatListPath = path.join(tempDir, 'concat_list.txt');
    const lines = [];
    
    for (let i = 0; i < inputFiles.length; i++) {
      lines.push(`file '${path.resolve(inputFiles[i])}'`);
      if (i < inputFiles.length - 1 && silenceMs > 0) {
        lines.push(`file '${path.resolve(silenceFile)}'`);
      }
    }
    
    fs.writeFileSync(concatListPath, lines.join('\n'), 'utf-8');

    // Run ffmpeg concat
    console.log(`🔧 Đang ghép ${inputFiles.length} file audio...`);
    execSync(
      `ffmpeg -y -f concat -safe 0 -i "${concatListPath}" -c copy "${outputPath}"`,
      { stdio: 'pipe' }
    );

    const sizeMB = (fs.statSync(outputPath).size / 1024 / 1024).toFixed(2);
    console.log(`✅ Đã ghép thành: ${path.basename(outputPath)} (${sizeMB} MB)`);
    
    return outputPath;
  } finally {
    // Cleanup temp files
    if (fs.existsSync(tempDir)) {
      fs.rmSync(tempDir, { recursive: true, force: true });
    }
  }
}

/**
 * Get audio duration using ffprobe
 */
function getAudioDuration(filePath) {
  try {
    const result = execSync(
      `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${filePath}"`,
      { stdio: 'pipe' }
    ).toString().trim();
    return parseFloat(result);
  } catch {
    return 0;
  }
}

/**
 * Print audio summary
 */
function printAudioSummary(files) {
  console.log('\n🎵 Audio Summary:');
  console.log('─'.repeat(50));
  
  let totalDuration = 0;
  for (const file of files) {
    const duration = getAudioDuration(file);
    totalDuration += duration;
    const mins = Math.floor(duration / 60);
    const secs = Math.round(duration % 60);
    console.log(`  ${path.basename(file).padEnd(30)} ${mins}:${String(secs).padStart(2, '0')}`);
  }
  
  const totalMins = Math.floor(totalDuration / 60);
  const totalSecs = Math.round(totalDuration % 60);
  console.log('─'.repeat(50));
  console.log(`  Tổng thời lượng: ${totalMins}:${String(totalSecs).padStart(2, '0')}\n`);
}

// CLI mode
if (require.main === module) {
  const args = process.argv.slice(2);
  
  if (args.length < 2) {
    console.log('Sử dụng: node audio_merger.js <output.mp3> <input1.mp3> <input2.mp3> ...');
    process.exit(1);
  }

  const outputFile = args[0];
  const inputFiles = args.slice(1);
  
  // Verify all input files exist
  for (const f of inputFiles) {
    if (!fs.existsSync(f)) {
      console.error(`❌ File không tồn tại: ${f}`);
      process.exit(1);
    }
  }

  mergeAudioFiles(inputFiles, outputFile);
  printAudioSummary([...inputFiles, outputFile]);
}

module.exports = { mergeAudioFiles, getAudioDuration, printAudioSummary, checkFfmpeg };
