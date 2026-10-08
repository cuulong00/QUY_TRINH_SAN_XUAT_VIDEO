const fs = require('fs');

const STATE_FILE = '/tmp/gocnhinpodcast-claude-hook-state.json';

function readStdin() {
  return new Promise(resolve => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', chunk => (data += chunk));
    process.stdin.on('end', () => resolve(data));
  });
}

function clearState() {
  try {
    fs.unlinkSync(STATE_FILE);
  } catch {}
}

(async () => {
  await readStdin();
  if (!fs.existsSync(STATE_FILE)) return;

  let state;
  try {
    state = JSON.parse(fs.readFileSync(STATE_FILE, 'utf8'));
  } catch {
    clearState();
    return;
  }

  const touchedEpisodeFiles = Array.isArray(state.touchedEpisodeFiles) ? state.touchedEpisodeFiles : [];
  const registryTouched = Boolean(state.registryTouched);

  if (touchedEpisodeFiles.length > 0 && !registryTouched) {
    process.stdout.write(JSON.stringify({
      decision: 'block',
      reason: 'Episode files changed but 01_management/episode_registry.csv was not updated in this session.',
      systemMessage: 'Workflow guard: bạn đã sửa file episode nhưng chưa cập nhật 01_management/episode_registry.csv.',
      suppressOutput: true
    }));
    return;
  }

  clearState();
})().catch(err => {
  process.stdout.write(JSON.stringify({
    decision: 'block',
    reason: `stop_guard failed: ${err.message}`,
    suppressOutput: true
  }));
});