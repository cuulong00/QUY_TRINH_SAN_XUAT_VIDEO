import { SceneGroup, SceneTask, GenerationMode } from '../types';

export function parseStorytrack(content: string, mode: GenerationMode = 'chained'): SceneGroup[] {
  const lines = content.split('\n');
  const groupMap = new Map<string, { imageTask?: SceneTask; videoTask?: SceneTask }>();

  lines.forEach((line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return;

    // Pattern: SCENE_ID [TYPE]: @ref -> prompt...
    const match = trimmed.match(/^([A-Za-z0-9_-]+)\s*\[(IMAGE|VIDEO)\]\s*:\s*(?:@([^\s->]+)\s*->)?\s*(.+)$/i);
    if (!match) return;

    const [, sceneId, typeStr, refFile, rawPrompt] = match;
    const type = typeStr.toLowerCase() as 'image' | 'video';

    if (!groupMap.has(sceneId)) {
      groupMap.set(sceneId, {});
    }

    const group = groupMap.get(sceneId)!;
    const taskId = `${sceneId}_${type}`;

    const task: SceneTask = {
      id: taskId,
      sceneId,
      type,
      prompt: rawPrompt.trim(),
      referenceFile: refFile ? refFile.trim() : undefined,
      status: 'idle',
      progress: 0,
      retryCount: 0
    };

    if (type === 'image') {
      group.imageTask = task;
    } else {
      group.videoTask = task;
    }
  });

  const result: SceneGroup[] = [];
  groupMap.forEach((tasks, sceneId) => {
    result.push({
      sceneId,
      status: 'idle',
      imageTask: (mode === 'video-only') ? undefined : tasks.imageTask,
      videoTask: (mode === 'image-only') ? undefined : tasks.videoTask
    });
  });

  return result;
}

export function sanitizePrompt(prompt: string): string {
  // Strip out any remaining @ref -> tags, embedded @image.ext mentions, and trailing parameters like --ar 16:9 --dur 8s
  return prompt
    .replace(/^@[^\s->]+\s*->\s*/, '')
    .replace(/@[A-Za-z0-9_.-]+\.(?:jpg|png|jpeg|webp)/gi, '')
    .replace(/--ar\s+[0-9:]+/gi, '')
    .replace(/--dur\s+[0-9]+s?/gi, '')
    .replace(/\s+/g, ' ')
    .trim();
}

export function sanitizeFilename(sceneId: string, type: 'image' | 'video', mimeType: string): string {
  const ext = type === 'video' 
    ? 'mp4' 
    : mimeType.includes('jpeg') || mimeType.includes('jpg') 
      ? 'jpg' 
      : 'png';
  return `${sceneId}.${ext}`;
}
