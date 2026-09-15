#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const CANONICAL_PHASES = [
  'Topic Qualification',
  'Data Mining & Verification',
  'Strategy Brief',
  'Hook Lab',
  'Thesis Map',
  'Retention Map',
  'Outline',
  'Chapter Briefs',
  'Chapter Writing',
  'Financial QA',
  'Oral QA',
  'Visual Map',
  'Audio Landscape',
  'Slideshow Render',
  'Production Handoff',
  'Postmortem',
  'Performance Review',
];

const NEW_REQUIRED_ARTIFACTS = [
  '01_topic_qualification.md',
  '02_research_map.md',
  '03_brief.md',
  '04_hook_pack.md',
  '05_thesis_map.md',
  '06_retention_map.md',
  '07_outline.md',
  '08_chapter_briefs.md',
  '09_continuity_packet.md',
  '10_claim_ledger.md',
  'financial_qa.md',
  'oral_qa.md',
  'visual_map.csv',
  'production_notes.md',
  'postmortem.md',
];

const LEGACY_REQUIRED_ARTIFACTS = [
  '00_topic_qualification.md',
  '01_brief.md',
  '02_research_map.md',
  '02_hook_pack.md',
  '03_thesis_map.md',
  '04_retention_map.md',
  '04_outline.md',
  '05_continuity_packet.md',
  '06_claim_ledger.md',
  'final_voiceover.md',
  'financial_qa.md',
  'oral_qa.md',
  'visual_map.csv',
  'production_notes.md',
  'postmortem.md',
];

const REQUIRED_ARTIFACTS = NEW_REQUIRED_ARTIFACTS;

const OPTIONAL_ARTIFACTS = [
  '07_golden_lines.md',
];

const REQUIRED_COMMANDS = [
  'init_episode.md',
  'qualify_topic.md',
  'build_brief.md',
  'build_research_map.md',
  'hook_lab.md',
  'build_thesis.md',
  'build_retention_map.md',
  'build_outline.md',
  'build_chapter_briefs.md',
  'write_chapter.md',
  'merge_voiceover.md',
  'financial_qa.md',
  'oral_qa.md',
  'build_visual_map.md',
  'render_slideshow.md',
  'production_handoff.md',
  'postmortem.md',
];

const PHASE_STATUS_COLUMNS = [
  'qualification_status',
  'brief_status',
  'research_status',
  'hook_status',
  'thesis_status',
  'retention_status',
  'outline_status',
  'chapter_briefs_status',
  'chapters_status',
  'merge_status',
  'financial_qa_status',
  'oral_qa_status',
  'visual_map_status',
  'slideshow_status',
  'production_status',
  'postmortem_status',
];

const VALID_CURRENT_PHASES = new Set([
  'topic_qualification',
  'brief',
  'research_map',
  'hook_lab',
  'thesis_map',
  'retention_map',
  'outline',
  'chapter_briefs',
  'chapter_writing',
  'final_merge',
  'financial_qa',
  'oral_qa',
  'visual_map',
  'scene_timing_map',
  'visual_prompt_generation',
  'slideshow_render',
  'production_handoff',
  'postmortem',
]);

const OPERATOR_VISIBILITY_COLUMNS = [
  'active_specialist',
  'canonical_skill',
  'current_input_files',
  'current_output_file',
  'gate_status',
];

const VALID_CLASSIFICATIONS = new Set(['verified_data', 'market_analysis', 'opinion_commentary']);
const VALID_CONFIDENCE = new Set(['high', 'medium', 'low']);
const VALID_SOURCE_TYPES = new Set(['official_data', 'research_report', 'company_filing', 'market_observation', 'commentary']);
const VALID_VERIFICATION = new Set(['pending', 'verified', 'revise', 'cut']);

const SHORT_DISCLAIMER = 'Đây là nội dung giáo dục, không phải lời khuyên đầu tư';
const LONG_DISCLAIMER_SNIPPET = 'Nội dung trong video này chỉ mang tính giáo dục và tham khảo';

const LEGACY_WORKFLOW_ALLOWLIST = new Set([
  'qa_review.md',
  'generate_episode.md',
  'build_outline.md',
  'init_episode.md',
]);

function exists(targetPath) {
  return fs.existsSync(targetPath);
}

function read(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

function safeRead(filePath) {
  return exists(filePath) ? read(filePath) : '';
}

function listFiles(dir, predicate = () => true) {
  if (!exists(dir)) return [];
  return fs.readdirSync(dir).filter((name) => predicate(path.join(dir, name))).sort();
}

function parseArgs(argv) {
  const options = { json: false, allowLegacy: true, strict: false };
  const positional = [];

  for (const arg of argv) {
    if (arg === '--json') {
      options.json = true;
    } else if (arg === '--strict') {
      options.strict = true;
    } else if (arg === '--no-legacy') {
      options.allowLegacy = false;
    } else if (arg === '--allow-legacy') {
      options.allowLegacy = true;
    } else {
      positional.push(arg);
    }
  }

  const mode = positional[0] || 'all';
  const slug = positional[1];
  return { mode, slug, options };
}

function createReporter(options) {
  const state = {
    ok: true,
    errors: [],
    warnings: [],
    legacyWarnings: [],
    checkedEpisodes: [],
  };

  function push(level, target, message) {
    const entry = { level, target, message };
    if (level === 'error') {
      state.ok = false;
      state.errors.push(entry);
    } else if (level === 'warning') {
      state.warnings.push(entry);
    } else if (level === 'legacy-warning') {
      state.legacyWarnings.push(entry);
    }
  }

  return {
    state,
    error(target, message) { push('error', target, message); },
    warn(target, message) { push('warning', target, message); },
    legacy(target, message) { push('legacy-warning', target, message); },
    checkedEpisode(slug) {
      if (!state.checkedEpisodes.includes(slug)) state.checkedEpisodes.push(slug);
    },
    finish() {
      const summary = {
        ok: state.ok,
        errors: state.errors.length,
        warnings: state.warnings.length,
        legacyWarnings: state.legacyWarnings.length,
        checkedEpisodes: state.checkedEpisodes.length,
      };

      if (options.json) {
        process.stdout.write(`${JSON.stringify({ ...state, summary }, null, 2)}\n`);
      } else {
        printEntries('ERRORS', state.errors);
        printEntries('WARNINGS', state.warnings);
        printEntries('LEGACY WARNINGS', state.legacyWarnings);
        process.stdout.write(`Checked episodes: ${state.checkedEpisodes.length ? state.checkedEpisodes.join(', ') : 'none'}\n`);
        process.stdout.write(`Summary: ${summary.errors} error(s), ${summary.warnings} warning(s), ${summary.legacyWarnings} legacy warning(s).\n`);
      }

      process.exit(state.ok ? 0 : 1);
    },
  };
}

function printEntries(label, entries) {
  if (!entries.length) {
    process.stdout.write(`${label}: none\n`);
    return;
  }
  process.stdout.write(`${label}:\n`);
  for (const entry of entries) {
    process.stdout.write(`- [${entry.target}] ${entry.message}\n`);
  }
}

function extractBulletItems(content) {
  return content
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => line.startsWith('- `') && line.endsWith('`'))
    .map((line) => line.slice(3, -1));
}

function extractNumberedPhaseList(content) {
  const phases = [];
  for (const line of content.split('\n')) {
    const match = line.trim().match(/^\d+\.\s+(.+)$/);
    if (match) phases.push(match[1].trim());
  }
  return phases;
}

function ensureRootStructure(reporter) {
  const requiredPaths = [
    'CLAUDE.md',
    'README.md',
    path.join('03_playbooks', 'episode_workflow.md'),
    path.join('02_templates', 'episode_template'),
    path.join('.claude', 'commands'),
    path.join('01_management', 'episode_registry.csv'),
    'episodes',
  ];

  for (const relativePath of requiredPaths) {
    if (!exists(path.join(ROOT, relativePath))) {
      reporter.error('repo', `Missing required path: ${relativePath}`);
    }
  }
}

function validateDocs(reporter) {
  const claude = safeRead(path.join(ROOT, 'CLAUDE.md'));
  const readme = safeRead(path.join(ROOT, 'README.md'));
  const workflow = safeRead(path.join(ROOT, '03_playbooks', 'episode_workflow.md'));
  const templateReadme = safeRead(path.join(ROOT, '02_templates', 'episode_template', 'README.md'));

  const readmePhases = extractNumberedPhaseList(sectionBetween(readme, '## Pipeline chính thức', '## Required vs optional artifacts'));
  const claudePhases = extractNumberedPhaseList(sectionBetween(claude, '## Cấu trúc làm việc bắt buộc', '## File bắt buộc của mỗi episode'));
  const workflowPhaseLines = workflow
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => /^##\s+Pha\s+\d+\s+—\s+/.test(line))
    .map((line) => line.replace(/^##\s+Pha\s+\d+\s+—\s+/, '').trim());

  compareList(reporter, 'docs', 'Canonical phases in CLAUDE.md', claudePhases, CANONICAL_PHASES);
  compareList(reporter, 'docs', 'Canonical phases in README.md', readmePhases, CANONICAL_PHASES);
  compareList(reporter, 'docs', 'Canonical phases in episode_workflow.md', workflowPhaseLines, CANONICAL_PHASES);

  const claudeArtifacts = extractBulletItems(sectionBetween(claude, '## File bắt buộc của mỗi episode', '## File hỗ trợ tùy chọn'));
  const readmeRequired = extractBulletItems(sectionBetween(readme, '### Required artifacts', '### Optional-supported artifacts'));
  const readmeOptional = extractBulletItems(sectionBetween(readme, '### Optional-supported artifacts', '## Nên dùng IDE nào?'));
  const templateRequired = extractBulletItems(sectionBetween(templateReadme, '## Required artifacts', '## Optional-supported artifacts'));
  const templateOptional = extractBulletItems(sectionBetween(templateReadme, '## Optional-supported artifacts', '## Nguyên tắc'));

  compareSet(reporter, 'docs', 'Required artifacts in CLAUDE.md', claudeArtifacts, REQUIRED_ARTIFACTS.concat(['chapter_XX.md']));
  compareSet(reporter, 'docs', 'Required artifacts in README.md', readmeRequired, REQUIRED_ARTIFACTS.concat(['chapter_XX.md']));
  compareSet(reporter, 'docs', 'Required artifacts in template README', templateRequired, REQUIRED_ARTIFACTS.concat(['chapter_XX.md']));
  compareSet(reporter, 'docs', 'Optional artifacts in README.md', readmeOptional, OPTIONAL_ARTIFACTS.concat(['generated output như `video/slideshow_base.mp4`']));
  compareSet(reporter, 'docs', 'Optional artifacts in template README', templateOptional, OPTIONAL_ARTIFACTS.concat(['images_final/', 'video/slideshow_base.mp4']));
  const claudeOptional = extractBulletItems(sectionBetween(claude, '## File hỗ trợ tùy chọn', '## Cách làm việc đúng'));
  compareSet(reporter, 'docs', 'Optional artifacts in CLAUDE.md', claudeOptional, OPTIONAL_ARTIFACTS.concat(['thư mục ảnh final, ví dụ `images_final/`', 'file output render, ví dụ `video/slideshow_base.mp4`']));

  if (!claude.includes('verified_data') || !claude.includes('market_analysis') || !claude.includes('opinion_commentary')) {
    reporter.error('docs', 'CLAUDE.md does not state the canonical claim taxonomy.');
  }

  if (!claude.includes(SHORT_DISCLAIMER)) {
    reporter.error('docs', 'CLAUDE.md does not contain the canonical short disclaimer.');
  }

  if (!claude.includes('Mỗi lần chỉ làm đúng một pha')) {
    reporter.error('docs', 'CLAUDE.md is missing the one-phase-at-a-time rule.');
  }
}

function sectionBetween(content, startMarker, endMarker) {
  const start = content.indexOf(startMarker);
  if (start === -1) return '';
  const sliced = content.slice(start + startMarker.length);
  const end = endMarker ? sliced.indexOf(endMarker) : -1;
  return end === -1 ? sliced : sliced.slice(0, end);
}

function compareList(reporter, target, label, actual, expected) {
  const normalizedActual = actual.map((item) => normalizePhaseName(item));
  const normalizedExpected = expected.map((item) => normalizePhaseName(item));
  if (normalizedActual.length !== normalizedExpected.length || normalizedActual.some((item, index) => item !== normalizedExpected[index])) {
    reporter.warn(target, `${label} differ from canonical order.`);
  }
}

function normalizePhaseName(value) {
  return value
    .trim()
    .replace(/^Viết từng chapter.*$/i, 'Chapter Writing')
    .replace(/^Chapter Writing$/i, 'Chapter Writing');
}

function compareSet(reporter, target, label, actual, expected) {
  const a = [...new Set(actual)].sort();
  const e = [...new Set(expected)].sort();
  if (JSON.stringify(a) !== JSON.stringify(e)) {
    reporter.warn(target, `${label} differ from canonical artifact set.`);
  }
}

function validateCommands(reporter) {
  const commandsDir = path.join(ROOT, '.claude', 'commands');
  const present = new Set(listFiles(commandsDir, (entry) => fs.statSync(entry).isFile()));

  for (const file of REQUIRED_COMMANDS) {
    if (!present.has(file)) {
      reporter.error('commands', `Missing canonical command file: ${file}`);
    }
  }

  const checks = [
    ['write_chapter.md', ['continuity_packet.md', 'claim_ledger.md']],
    ['merge_voiceover.md', ['disclaimer']],
    ['financial_qa.md', ['disclaimer', 'buy/sell', 'fabricated']],
    ['oral_qa.md', ['spoken', 'pacing', 'breath']],
    ['render_slideshow.md', ['slideshow_video', 'images_final', 'slideshow_base.mp4']],
  ];

  for (const [file, keywords] of checks) {
    const filePath = path.join(commandsDir, file);
    if (!exists(filePath)) continue;
    const content = read(filePath).toLowerCase();
    for (const keyword of keywords) {
      if (!content.includes(keyword.toLowerCase())) {
        reporter.warn('commands', `${file} may be missing invariant keyword: ${keyword}`);
      }
    }
  }
}

function parseCsv(content) {
  const lines = content.trim().split('\n').filter(Boolean);
  if (!lines.length) return { header: [], rows: [] };
  const header = splitCsvLine(lines[0]);
  const rows = lines.slice(1).map((line) => {
    const values = splitCsvLine(line);
    const row = {};
    header.forEach((key, index) => {
      row[key] = (values[index] || '').trim();
    });
    return row;
  });
  return { header, rows };
}

function splitCsvLine(line) {
  const result = [];
  let current = '';
  let inQuotes = false;

  for (let i = 0; i < line.length; i += 1) {
    const char = line[i];
    if (char === '"') {
      if (inQuotes && line[i + 1] === '"') {
        current += '"';
        i += 1;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (char === ',' && !inQuotes) {
      result.push(current);
      current = '';
    } else {
      current += char;
    }
  }
  result.push(current);
  return result;
}

function loadRegistry(reporter) {
  const registryPath = path.join(ROOT, '01_management', 'episode_registry.csv');
  if (!exists(registryPath)) return { header: [], rows: [] };
  const parsed = parseCsv(read(registryPath));

  const expectedHeader = [
    'episode_slug', 'status', 'current_phase', ...PHASE_STATUS_COLUMNS,
    'hook_final', 'target_minutes', 'last_updated', 'notes',
    ...OPERATOR_VISIBILITY_COLUMNS,
  ];

  compareSet(reporter, 'registry', 'episode_registry.csv header', parsed.header, expectedHeader);
  return parsed;
}

function validateEpisodes(reporter, specificSlug) {
  const episodesDir = path.join(ROOT, 'episodes');
  const registry = loadRegistry(reporter);
  const registryBySlug = new Map(registry.rows.map((row) => [row.episode_slug, row]));
  const episodeNames = specificSlug
    ? [specificSlug]
    : listFiles(episodesDir, (entry) => fs.statSync(entry).isDirectory());

  const reqPhaseOrder = {
    'topic_qualification': 0,
    'brief': 1,
    'research_map': 2,
    'hook_lab': 3,
    'thesis_map': 4,
    'retention_map': 5,
    'outline': 6,
    'chapter_briefs': 7,
    'chapter_writing': 8,
    'final_merge': 9,
    'financial_qa': 10,
    'oral_qa': 11,
    'visual_map': 12,
    'scene_timing_map': 13,
    'visual_prompt_generation': 14,
    'slideshow_render': 15,
    'production_handoff': 16,
    'postmortem': 17
  };

  for (const slug of episodeNames) {
    const episodeDir = path.join(episodesDir, slug);
    if (!exists(episodeDir)) {
      reporter.error(`episode:${slug}`, 'Episode directory does not exist.');
      continue;
    }

    reporter.checkedEpisode(slug);
    const registryRow = registryBySlug.get(slug);

    if (!registryRow) {
      reporter.warn(`episode:${slug}`, 'Episode has no row in episode_registry.csv.');
      continue;
    }

    const files = new Set(listFiles(episodeDir, (entry) => fs.statSync(entry).isFile()));
    const isLegacy = files.has('00_topic_qualification.md') ||
                     files.has('01_brief.md') ||
                     files.has('05_continuity_packet.md') ||
                     files.has('06_claim_ledger.md');

    const currentPhase = registryRow.current_phase || '';
    const currentPhaseIndex = reqPhaseOrder[currentPhase] !== undefined ? reqPhaseOrder[currentPhase] : 17;
    const rowValues = Object.values(registryRow);
    const dateVal = rowValues.find((val) => /^\d{4}-\d{2}-\d{2}$/.test(val));
    const lastUpdated = dateVal || '';
    const isPreExisting = lastUpdated && lastUpdated < '2026-05-20';

    const requirements = [
      { name: 'Topic Qualification', phase: 'topic_qualification', files: ['01_topic_qualification.md', '00_topic_qualification.md'] },
      { name: 'Research Map', phase: 'research_map', files: ['02_research_map.md'] },
      { name: 'Brief', phase: 'brief', files: ['03_brief.md', '01_brief.md'] },
      { name: 'Hook Lab', phase: 'hook_lab', files: ['04_hook_pack.md', '02_hook_pack.md'] },
      { name: 'Thesis Map', phase: 'thesis_map', files: ['05_thesis_map.md', '03_thesis_map.md'] },
      { name: 'Retention Map', phase: 'retention_map', files: ['06_retention_map.md', '04_retention_map.md'] },
      { name: 'Outline', phase: 'outline', files: ['07_outline.md', '04_outline.md'] },
      { name: 'Continuity Packet', phase: 'chapter_writing', files: ['09_continuity_packet.md', '05_continuity_packet.md'] },
      { name: 'Claim Ledger', phase: 'chapter_writing', files: ['10_claim_ledger.md', '06_claim_ledger.md'] },
      { name: 'Financial QA', phase: 'financial_qa', files: ['financial_qa.md'] },
      { name: 'Oral QA', phase: 'oral_qa', files: ['oral_qa.md'] },
      { name: 'Visual Map', phase: 'visual_map', files: ['visual_map.csv'] },
      { name: 'Production Handoff', phase: 'production_handoff', files: ['production_notes.md'] },
      { name: 'Postmortem', phase: 'postmortem', files: ['postmortem.md'] }
    ];

    if (!isLegacy) {
      requirements.push({ name: 'Chapter Briefs', phase: 'chapter_briefs', files: ['08_chapter_briefs.md'] });
    } else {
      requirements.push({ name: 'Final Voiceover', phase: 'final_merge', files: ['final_voiceover.md'] });
    }

    for (const req of requirements) {
      const reqIndex = reqPhaseOrder[req.phase];
      if (reqIndex !== undefined && reqIndex <= currentPhaseIndex) {
        const hasAny = req.files.some((file) => files.has(file));
        if (!hasAny) {
          if (isPreExisting) {
            reporter.warn(`episode:${slug}`, `Missing required artifact: ${req.files.join(' or ')} (legacy warning)`);
          } else {
            reporter.error(`episode:${slug}`, `Missing required artifact: ${req.files.join(' or ')}`);
          }
        }
      }
    }

    if (files.has('chapter_template.md')) {
      reporter.warn(`episode:${slug}`, 'Template-only file chapter_template.md should not exist in an episode scaffold.');
    }

    for (const file of files) {
      if (file === 'chapter_template.md') continue;
      const fullPath = path.join(episodeDir, file);
      if (fs.statSync(fullPath).isFile() && read(fullPath).includes('__EPISODE_SLUG__')) {
        reporter.error(`episode:${slug}`, `Found unresolved __EPISODE_SLUG__ placeholder in ${file}`);
      }
    }

    const chapterFiles = [...files].filter((name) => /^chapter_\d+\.md$/.test(name)).sort();

    if (!VALID_CURRENT_PHASES.has(currentPhase)) {
      reporter.error(`episode:${slug}`, `Invalid current_phase in registry: ${currentPhase || '(blank)'}`);
    }
    for (const column of PHASE_STATUS_COLUMNS) {
      if (!(column in registryRow)) {
        reporter.error(`episode:${slug}`, `Registry row is missing column: ${column}`);
      }
    }

    const isEarlyPhase = !['final_merge', 'financial_qa', 'oral_qa', 'visual_map', 'slideshow_render', 'production_handoff', 'postmortem'].includes(currentPhase);
    if (!chapterFiles.length && !isEarlyPhase) {
      reporter.error(`episode:${slug}`, 'Later-phase episode has no chapter_XX.md files.');
    }

    validateClaimLedger(reporter, slug, episodeDir, currentPhase, isLegacy, isPreExisting);
    validateFinalVoiceover(reporter, slug, episodeDir);
    validateFinancialQa(reporter, slug, episodeDir);
  }
}

function validateClaimLedger(reporter, slug, episodeDir, currentPhase, isLegacy, isPreExisting) {
  const ledgerFile = isLegacy ? '06_claim_ledger.md' : '10_claim_ledger.md';
  const ledgerPath = path.join(episodeDir, ledgerFile);
  if (!exists(ledgerPath)) return;
  const content = read(ledgerPath);

  const reportError = (tag, msg) => {
    if (isPreExisting) {
      reporter.warn(tag, `${msg} (legacy warning)`);
    } else {
      reporter.error(tag, msg);
    }
  };

  const blocks = [];
  let currentBlock = [];
  for (const line of content.split('\n')) {
    const trimmed = line.trim();
    if (trimmed.startsWith('|')) {
      currentBlock.push(trimmed);
    } else {
      if (currentBlock.length > 0) {
        blocks.push(currentBlock);
        currentBlock = [];
      }
    }
  }
  if (currentBlock.length > 0) {
    blocks.push(currentBlock);
  }

  let claimsTable = null;
  for (const block of blocks) {
    if (block.length < 2) continue;
    const header = block[0].split('|').map((part) => part.trim()).filter(Boolean);
    const normalizedHeader = header.map(h => h.toLowerCase());
    if (normalizedHeader.includes('nhãn') || normalizedHeader.includes('nghĩa') || normalizedHeader.includes('cách viết')) {
      continue;
    }
    if (header.length >= 2) {
      claimsTable = block;
      break;
    }
  }

  if (!claimsTable) {
    if (['research_map', 'hook_lab', 'thesis_map', 'retention_map', 'outline', 'chapter_briefs', 'chapter_writing', 'final_merge', 'financial_qa', 'oral_qa', 'visual_map', 'slideshow_render', 'production_handoff', 'postmortem'].includes(currentPhase)) {
      reporter.warn(`episode:${slug}`, 'Research-or-later episode has an unexpectedly empty claim ledger.');
    }
    return;
  }

  const header = claimsTable[0].split('|').map((part) => part.trim()).filter(Boolean);
  const isNewSchema = header.length === 10;
  const expectedHeader = ['id', 'claim', 'classification', 'confidence', 'source_type', 'source_reference', 'source_note', 'chapter_used_in', 'safe_wording_note', 'verification_status'];

  if (isNewSchema) {
    const normalizedHeader = header.map(h => h.toLowerCase());
    const normalizedExpected = expectedHeader.map(h => h.toLowerCase());
    if (JSON.stringify(normalizedHeader) !== JSON.stringify(normalizedExpected)) {
      reportError(`episode:${slug}`, `Claim ledger header does not match the expected schema. Expected: [${expectedHeader.join(', ')}], Found: [${header.join(', ')}]`);
      return;
    }
  }

  const rows = claimsTable.slice(2)
    .map((line) => line.split('|').map((part) => part.trim()).filter(Boolean))
    .filter((parts) => parts.length === header.length);

  for (const row of rows) {
    if (isNewSchema) {
      const [id, claim, classification, confidence, sourceType, sourceReference, sourceNote, chapterUsedIn, safeWordingNote, verificationStatus] = row;
      if (classification.includes('/')) continue;
      if (!VALID_CLASSIFICATIONS.has(classification)) {
        reportError(`episode:${slug}`, `Claim ${id} has invalid classification: ${classification}`);
      }
      if (!VALID_CONFIDENCE.has(confidence)) {
        reportError(`episode:${slug}`, `Claim ${id} has invalid confidence: ${confidence}`);
      }
      if (!VALID_SOURCE_TYPES.has(sourceType)) {
        reportError(`episode:${slug}`, `Claim ${id} has invalid source_type: ${sourceType}`);
      }
      if (!VALID_VERIFICATION.has(verificationStatus)) {
        reportError(`episode:${slug}`, `Claim ${id} has invalid verification_status: ${verificationStatus}`);
      }
      if (classification === 'verified_data' && !sourceReference) {
        reportError(`episode:${slug}`, `Claim ${id} is verified_data but missing source_reference.`);
      }
      if (verificationStatus === 'verified' && !sourceReference) {
        reportError(`episode:${slug}`, `Claim ${id} is verified but missing source_reference.`);
      }
      if (classification === 'opinion_commentary' && claim && !safeWordingNote) {
        reporter.warn(`episode:${slug}`, `Claim ${id} is opinion_commentary but safe_wording_note is blank.`);
      }
    } else {
      const classIndex = header.findIndex(h => {
        const lh = h.toLowerCase();
        return lh === 'loại' || lh === 'classification' || lh === 'type';
      });
      const claimIndex = header.findIndex(h => h.toLowerCase() === 'claim' || h.toLowerCase() === 'nhận định');
      const idIndex = header.findIndex(h => h.toLowerCase() === '#' || h.toLowerCase() === 'id');

      const id = idIndex !== -1 ? row[idIndex] : '?';
      const classification = classIndex !== -1 ? row[classIndex] : '';

      if (classification && !classification.includes('/')) {
        if (!VALID_CLASSIFICATIONS.has(classification)) {
          reporter.warn(`episode:${slug}`, `Claim ${id} has invalid classification: ${classification}`);
        }
      }
    }
  }
}

function validateFinalVoiceover(reporter, slug, episodeDir) {
  const finalPath = path.join(episodeDir, 'final_voiceover.md');
  if (!exists(finalPath)) return;
  const content = read(finalPath);
  const hasScriptContent = !content.includes('[full voiceover script ở đây]');
  const hasDisclaimer = content.includes(SHORT_DISCLAIMER) || content.includes(LONG_DISCLAIMER_SNIPPET);
  const disclaimerLocation = matchMetadataField(content, 'disclaimer_location');

  if (hasScriptContent && !hasDisclaimer) {
    reporter.error(`episode:${slug}`, 'final_voiceover.md has script content but no valid disclaimer.');
  }

  if (hasDisclaimer && !disclaimerLocation) {
    reporter.warn(`episode:${slug}`, 'final_voiceover.md contains a disclaimer but disclaimer_location is blank.');
  }
}

function validateFinancialQa(reporter, slug, episodeDir) {
  const qaPath = path.join(episodeDir, 'financial_qa.md');
  const finalPath = path.join(episodeDir, 'final_voiceover.md');
  if (!exists(qaPath) || !exists(finalPath)) return;
  const qa = read(qaPath);
  const finalVoiceover = read(finalPath);
  const hasScriptContent = !finalVoiceover.includes('[full voiceover script ở đây]');
  if (!hasScriptContent) return;

  const hasDisclaimer = finalVoiceover.includes(SHORT_DISCLAIMER) || finalVoiceover.includes(LONG_DISCLAIMER_SNIPPET);
  const qaSaysPresent = /^disclaimer_present:\s*yes\s*$/m.test(qa);
  const qaSaysAbsent = /^disclaimer_present:\s*no\s*$/m.test(qa);

  if (hasDisclaimer && qaSaysAbsent) {
    reporter.warn(`episode:${slug}`, 'financial_qa.md says disclaimer_present: no but final_voiceover.md contains a disclaimer.');
  }
  if (!hasDisclaimer && qaSaysPresent) {
    reporter.warn(`episode:${slug}`, 'financial_qa.md says disclaimer_present: yes but final_voiceover.md does not contain a disclaimer.');
  }
}

function matchMetadataField(content, field) {
  const match = content.match(new RegExp(`^${field}:\\s*(.*)$`, 'm'));
  return match ? match[1].trim() : '';
}

function validateWorkflows(reporter, options) {
  const workflowsDir = path.join(ROOT, '.agent', 'workflows');
  if (!exists(workflowsDir)) return;
  const files = listFiles(workflowsDir, (entry) => fs.statSync(entry).isFile());

  for (const file of files) {
    const content = read(path.join(workflowsDir, file));
    const lower = content.toLowerCase();

    if (!options.allowLegacy && LEGACY_WORKFLOW_ALLOWLIST.has(file)) {
      reporter.error('workflows', `${file} is marked legacy-compatible but --no-legacy was used.`);
      continue;
    }

    if (LEGACY_WORKFLOW_ALLOWLIST.has(file)) {
      reporter.legacy(`workflow:${file}`, 'Legacy-compatible workflow diverges from canonical one-phase flow.');
    }

    if (file === 'generate_episode.md' && !lower.includes('disclaimer')) {
      reporter.warn(`workflow:${file}`, 'Finance-heavy autopilot workflow may be missing explicit disclaimer handling.');
    }

    if (file === 'write_chapter.md' && lower.includes('07_golden_lines.md') && !lower.includes('if it exists') && !lower.includes('nếu có') && !lower.includes('đã tồn tại') && !lower.includes('bỏ qua')) {
      reporter.warn(`workflow:${file}`, '07_golden_lines.md may be treated as required instead of optional.');
    }

    if (file === 'generate_visual_prompts.md' && !lower.includes('slideshow')) {
      reporter.warn(`workflow:${file}`, 'generate_visual_prompts.md may be missing slideshow handoff guidance.');
    }
  }
}

function main() {
  const { mode, slug, options } = parseArgs(process.argv.slice(2));
  const reporter = createReporter(options);

  ensureRootStructure(reporter);

  if (mode === 'all' || mode === 'docs') validateDocs(reporter);
  if (mode === 'all' || mode === 'commands') validateCommands(reporter);
  if (mode === 'all' || mode === 'episode') {
    if (mode === 'episode' && !slug) {
      reporter.error('cli', 'Usage: node scripts/validate_repo.js episode <slug>');
    } else {
      validateEpisodes(reporter, mode === 'episode' ? slug : undefined);
    }
  }
  if (mode === 'all' || mode === 'workflows') validateWorkflows(reporter, options);

  if (!['all', 'docs', 'commands', 'episode', 'workflows'].includes(mode)) {
    reporter.error('cli', `Unknown mode: ${mode}`);
  }

  reporter.finish();
}

main();
