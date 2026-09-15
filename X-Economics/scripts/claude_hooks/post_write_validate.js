const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const STATE_FILE = '/tmp/gocnhinpodcast-claude-hook-state.json';
const DISCLAIMER = 'Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng';

function readStdin() {
  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', chunk => (data += chunk));
    process.stdin.on('end', () => {
      try {
        resolve(data.trim() ? JSON.parse(data) : {});
      } catch (err) {
        reject(err);
      }
    });
  });
}

function rel(filePath) {
  return path.relative(ROOT, filePath).replace(/\\/g, '/');
}

function readJsonSafe(file) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch {
    return { touchedEpisodeFiles: [], registryTouched: false };
  }
}

function writeJsonSafe(file, data) {
  fs.writeFileSync(file, JSON.stringify(data, null, 2));
}

(async () => {
  const input = await readStdin();
  const filePath = input.tool_input?.file_path || input.tool_response?.filePath;
  if (!filePath || !fs.existsSync(filePath)) return;

  const relative = rel(filePath);
  const state = readJsonSafe(STATE_FILE);

  if (/^episodes\/.+/.test(relative)) {
    if (!state.touchedEpisodeFiles.includes(relative)) {
      state.touchedEpisodeFiles.push(relative);
    }
  }
  if (relative === '01_management/episode_registry.csv') {
    state.registryTouched = true;
  }
  writeJsonSafe(STATE_FILE, state);

  const basename = path.basename(filePath);
  const content = fs.readFileSync(filePath, 'utf8');

  if (basename === 'final_voiceover.md' && !content.includes(DISCLAIMER)) {
    process.stdout.write(JSON.stringify({
      decision: 'block',
      reason: 'final_voiceover.md must contain the mandatory compliance note.',
      systemMessage: 'Workflow guard: final_voiceover.md is missing the mandatory compliance note.',
      suppressOutput: true
    }));
    return;
  }

  if (basename === '10_claim_ledger.md' || basename === '06_claim_ledger.md') {
    const required = ['verified_data', 'market_analysis', 'opinion_commentary'];
    const missing = required.filter(tag => !content.includes(tag));
    if (missing.length) {
      process.stdout.write(JSON.stringify({
        decision: 'block',
        reason: `${basename} must preserve taxonomy tags: ${missing.join(', ')}`,
        systemMessage: 'Workflow guard: claim ledger taxonomy is incomplete.',
        suppressOutput: true
      }));
      return;
    }
  }

  if (/^chapter_\d+\.md$/.test(basename)) {
    const hasNumber = /\d/.test(content);
    if (!hasNumber) {
      process.stdout.write(JSON.stringify({
        systemMessage: 'Workflow reminder: mỗi chapter nên có ít nhất 1 case study hoặc số liệu thực tế, và nhớ cập nhật continuity packet + claim ledger + episode registry.',
        suppressOutput: true
      }));
      return;
    }
  }

  if (/^episodes\/.+/.test(relative) && relative !== '01_management/episode_registry.csv') {
    process.stdout.write(JSON.stringify({
      systemMessage: 'Workflow reminder: nếu vừa hoàn tất một pha, hãy cập nhật 01_management/episode_registry.csv trước khi kết thúc.',
      suppressOutput: true
    }));
  }
})().catch(err => {
  process.stdout.write(JSON.stringify({
    systemMessage: `post_write_validate error: ${err.message}`,
    suppressOutput: true
  }));
});