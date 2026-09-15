import fs from 'fs';
export function debugLog(...args: any[]) {
  const logFile = '/Users/pro16/Documents/VideoProject/X-Economics/scratch/gemini_gems_mcp.log';
  try {
    const msg = args.map(a => typeof a === 'object' ? JSON.stringify(a) : a).join(' ');
    fs.appendFileSync(logFile, `[${new Date().toISOString()}] ${msg}\n`, 'utf8');
  } catch (e) {}
}
