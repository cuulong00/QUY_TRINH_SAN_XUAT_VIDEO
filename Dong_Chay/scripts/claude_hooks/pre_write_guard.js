const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');

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

function exists(p) {
  try {
    return fs.existsSync(p);
  } catch {
    return false;
  }
}

function rel(filePath) {
  return path.relative(ROOT, filePath).replace(/\\/g, '/');
}

function episodeInfo(filePath) {
  const relative = rel(filePath);
  const m = relative.match(/^episodes\/([^/]+)\/(.+)$/);
  if (!m) return null;
  return { slug: m[1], relative };
}

function missingFiles(base, required) {
  return required.filter(name => !exists(path.join(base, name)));
}

(async () => {
  const input = await readStdin();
  const filePath = input.tool_input?.file_path;
  if (!filePath) return;

  const info = episodeInfo(filePath);
  if (!info) return;

  const episodeDir = path.join(ROOT, 'episodes', info.slug);
  const basename = path.basename(filePath);
  const episodeDirExists = exists(episodeDir);

  const emitBlock = (reason, missing = []) => {
    process.stdout.write(JSON.stringify({
      continue: false,
      stopReason: missing.length ? `${reason} Missing: ${missing.join(', ')}` : reason,
      suppressOutput: true
    }));
  };

  if (/^chapter_\d+\.md$/.test(basename)) {
    const required = [
      '01_brief.md',
      '02_research_map.md',
      '02_hook_pack.md',
      '03_thesis_map.md',
      '04_retention_map.md',
      '04_outline.md',
      '05_continuity_packet.md',
      '06_claim_ledger.md'
    ];
    const missing = missingFiles(episodeDir, required);
    if (missing.length) {
      emitBlock(`Cannot write ${basename} before upstream workflow files exist.`, missing);
      return;
    }
  }

  if (basename === 'final_voiceover.md') {
    const required = [
      '00_topic_qualification.md',
      '01_brief.md',
      '02_research_map.md',
      '02_hook_pack.md',
      '03_thesis_map.md',
      '04_retention_map.md',
      '04_outline.md',
      '06_claim_ledger.md'
    ];
    const missing = episodeDirExists ? missingFiles(episodeDir, required) : required;
    const chapterFiles = episodeDirExists ? fs.readdirSync(episodeDir).filter(f => /^chapter_\d+\.md$/.test(f)) : [];
    if (missing.length || chapterFiles.length === 0) {
      const extra = chapterFiles.length === 0 ? ['chapter_XX.md (at least one chapter required)'] : [];
      emitBlock('Cannot create or update final_voiceover.md before chapter-writing workflow is complete.', [...missing, ...extra]);
      return;
    }
  }

  if (basename === 'visual_map.csv') {
    const required = ['final_voiceover.md', '04_retention_map.md', 'production_notes.md'];
    const missing = missingFiles(episodeDir, required);
    if (missing.length) {
      emitBlock('Cannot build visual_map.csv before merge and retention are complete.', missing);
      return;
    }
  }

  if (basename === 'production_notes.md' && !exists(path.join(episodeDir, 'final_voiceover.md'))) {
    emitBlock('Cannot update production_notes.md for handoff before final_voiceover.md exists.');
  }
})().catch(err => {
  process.stdout.write(JSON.stringify({
    continue: false,
    stopReason: `pre_write_guard failed: ${err.message}`,
    suppressOutput: true
  }));
});