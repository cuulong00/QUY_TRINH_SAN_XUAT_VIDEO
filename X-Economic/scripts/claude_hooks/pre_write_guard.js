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

  // Canonical required-artifact list — kept in sync with CLAUDE.md's 16-Pha pipeline.
  // Pha 1: 01_global_vision_synthesis.md | Pha 2: 02_research_map.md/02_research_synthesis.md
  // Pha 3: 03_brief.md | Pha 4: 07_outline.md | Pha 5: 04_hook_pack.md
  // Pha 6: 08_chapter_briefs.md + 09_narrative_state_tracker.md | Pha 7: chapter_XX.md
  // Pha 8: voiceover.md | Pha 9: retention_bridge_audit.md | Pha 10&11: 10_compliance_report.md
  if (/^chapter_\d+\.md$/.test(basename)) {
    const required = [
      '01_global_vision_synthesis.md',
      '02_research_synthesis.md',
      '03_brief.md',
      '04_hook_pack.md',
      '07_outline.md',
      '08_chapter_briefs.md',
      '09_narrative_state_tracker.md'
    ];
    const missing = missingFiles(episodeDir, required);
    if (missing.length) {
      emitBlock(`Cannot write ${basename} before upstream workflow files exist.`, missing);
      return;
    }
  }

  if (basename === 'voiceover.md') {
    const required = [
      '01_global_vision_synthesis.md',
      '02_research_synthesis.md',
      '03_brief.md',
      '04_hook_pack.md',
      '07_outline.md',
      '08_chapter_briefs.md',
      '09_narrative_state_tracker.md'
    ];
    const missing = episodeDirExists ? missingFiles(episodeDir, required) : required;
    const chapterFiles = episodeDirExists ? fs.readdirSync(episodeDir).filter(f => /^chapter_\d+\.md$/.test(f)) : [];
    if (missing.length || chapterFiles.length === 0) {
      const extra = chapterFiles.length === 0 ? ['chapter_XX.md (at least one chapter required)'] : [];
      emitBlock('Cannot create or update voiceover.md before chapter-writing workflow is complete.', [...missing, ...extra]);
      return;
    }
  }

  if (basename === 'visual_storyboard_blueprint.md') {
    const required = ['voiceover.md', '07_outline.md'];
    const missing = missingFiles(episodeDir, required);
    if (missing.length) {
      emitBlock('Cannot build visual_storyboard_blueprint.md before voiceover and outline are complete.', missing);
      return;
    }
  }

  if (basename === 'production_notes.md') {
    const required = ['10_compliance_report.md', 'voiceover.md'];
    const missing = missingFiles(episodeDir, required);
    if (missing.length) {
      emitBlock('Cannot update production_notes.md for handoff before compliance report and voiceover exist.', missing);
      return;
    }
  }
})().catch(err => {
  process.stdout.write(JSON.stringify({
    continue: false,
    stopReason: `pre_write_guard failed: ${err.message}`,
    suppressOutput: true
  }));
});