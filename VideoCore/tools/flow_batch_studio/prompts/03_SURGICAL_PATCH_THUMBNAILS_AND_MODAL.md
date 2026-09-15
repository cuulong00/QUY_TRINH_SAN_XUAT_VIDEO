# 🖼️ SURGICAL PATCH: FIX THUMBNAIL DISPLAY & SYNC (BẢN VÁ TRIỆT ĐỂ)

Tệp tin này chứa prompt bản vá chính xác (surgical patch) để gửi cho **Tool Builder** trên Google Flow, khắc phục triệt để lỗi **không hiển thị thumbnail** do `group.imageTask` và `group.videoTask` bị kẹt dữ liệu cũ (stale pointer) trong `batch.groups`.

---

## 📋 NỘI DUNG PROMPT DÁN VÀO CHAT CỦA TOOL BUILDER

```markdown
[CRITICAL REGRESSION LOCK - SURGICAL PATCH: FIX THUMBNAIL RENDERING]

⚠️ STRICT INVARIANTS: You MUST PRESERVE 100% of the following existing configurations:
1. MODEL PRESERVATION: `videoModel` MUST remain EXACTLY `'Veo 3.1 - Lite [Lower Priority]'`. DO NOT strip or alter this string (zero-credit tier).
2. IMAGE MODEL: MUST remain `'🍌 Nano Banana 2'`.
3. WORKERS COUNT (Active Compute Slots): Default initial `workersCount` MUST be 4 (`useState(4)`).
4. RETRY & AUTO-RESUME: Keep `retryAllFailed` and `refreshScene` auto-resume logic exactly as implemented.
5. ASSET BIN & DOWNLOAD: Keep `assetBin`, `Reference Asset Bin`, and the chained download logic intact.
6. 1 SCENE = 1 ROW: Keep the Production Ledger table layout strictly intact.

[BUG EXPLANATION]:
In the current code, `updateTask` updates `newTasks` (array in batch.tasks), but in `newGroups` it only returns `{ ...g, status: groupStatus }`. It NEVER updates `g.imageTask` or `g.videoTask` with the newly completed tasks containing `resultBase64`!
Because of this, `group.imageTask?.resultBase64` is ALWAYS undefined, so thumbnails never appear in the table!

[MANDATORY SURGICAL FIXES]:

1. Set Active Compute Slots initial state to 4:
```tsx
const [workersCount, setWorkersCount] = useState(4);
```

2. Add a safe helper function right before the return in App:
```tsx
const getMediaSrc = (base64?: string, mimeType?: string) => {
  if (!base64) return '';
  return base64.startsWith('data:') ? base64 : `data:${mimeType || 'image/png'};base64,${base64}`;
};
```

3. Fix `updateTask` to synchronize `imageTask` and `videoTask` inside `newGroups`:
Inside `updateTask`, update the `newGroups` mapping:
```tsx
const newGroups = prev.groups.map(g => {
  if (g.sceneId === task.sceneId) {
    const groupTasks = newTasks.filter(t => t.sceneId === task.sceneId);
    const allCompleted = groupTasks.every(t => t.status === 'completed');
    const anyFailed = groupTasks.some(t => t.status === 'failed');
    const anyBlocked = groupTasks.some(t => t.status === 'blocked');
    
    let groupStatus: SceneStatus = 'idle';
    if (anyFailed) groupStatus = 'failed';
    else if (anyBlocked) groupStatus = 'blocked';
    else if (allCompleted) groupStatus = 'completed';
    else if (groupTasks.some(t => t.status === 'processing')) groupStatus = 'processing';
    
    return { 
      ...g, 
      status: groupStatus,
      imageTask: groupTasks.find(t => t.type === 'image'),
      videoTask: groupTasks.find(t => t.type === 'video')
    };
  }
  return g;
});
```

4. In the table render (`batch.groups.map(group => ...)`), look up tasks directly from `batch.tasks` for 100% reactive rendering:
At the start of `batch.groups.map(group => {`:
```tsx
const imgTask = batch.tasks.find(t => t.sceneId === group.sceneId && t.type === 'image') || group.imageTask;
const vidTask = batch.tasks.find(t => t.sceneId === group.sceneId && t.type === 'video') || group.videoTask;
const worker = workers.find(w => 
  w.activeTaskId && (w.activeTaskId === imgTask?.id || w.activeTaskId === vidTask?.id)
);
const groupTasks = [imgTask, vidTask].filter(Boolean) as SceneTask[];
```

And update the table cells:
- Step 1 [IMAGE] cell:
```tsx
<td className="p-4 text-center">
  {imgTask?.status === 'completed' && imgTask?.resultBase64 ? (
    <div className="flex items-center justify-center gap-1.5">
      <img 
        src={getMediaSrc(imgTask.resultBase64, imgTask.resultMimeType)} 
        alt={group.sceneId} 
        className="w-14 h-8 object-cover rounded border border-white/20 hover:border-violet-400 cursor-pointer shadow-sm hover:scale-110 transition-transform"
        onClick={() => setPreviewModal({ 
          type: 'image', 
          url: getMediaSrc(imgTask.resultBase64, imgTask.resultMimeType), 
          title: `${group.sceneId} - Image Output` 
        })}
        title="Click to preview full image"
      />
      <span className="text-emerald-400 text-[9px] font-bold">✓</span>
    </div>
  ) : imgTask ? (
    getStatusBadge(imgTask.status, 'image')
  ) : (
    <span className="text-white/5">--</span>
  )}
</td>
```

- Step 2 [VIDEO] cell:
```tsx
<td className="p-4 text-center">
  {vidTask?.status === 'completed' && vidTask?.resultBase64 ? (
    <div className="flex items-center justify-center gap-1.5">
      <div 
        className="relative w-14 h-8 rounded border border-white/20 hover:border-violet-400 overflow-hidden cursor-pointer shadow-sm group hover:scale-110 transition-transform bg-black"
        onClick={() => setPreviewModal({ 
          type: 'video', 
          url: getMediaSrc(vidTask.resultBase64, vidTask.resultMimeType), 
          title: `${group.sceneId} - Video Output` 
        })}
        title="Click to play full video"
      >
        <video 
          src={getMediaSrc(vidTask.resultBase64, vidTask.resultMimeType)} 
          className="w-full h-full object-cover pointer-events-none"
          muted 
          loop 
          playsInline
        />
        <div className="absolute inset-0 bg-black/30 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
          <span className="material-symbols-outlined text-[12px] text-white">play_arrow</span>
        </div>
      </div>
      <span className="text-emerald-400 text-[9px] font-bold">✓</span>
    </div>
  ) : vidTask ? (
    getStatusBadge(vidTask.status, 'video')
  ) : (
    <span className="text-white/5">--</span>
  )}
</td>
```
```
