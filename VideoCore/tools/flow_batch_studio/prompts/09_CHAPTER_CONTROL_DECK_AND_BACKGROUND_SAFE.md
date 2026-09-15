# PROMPT NÂNG CẤP DÀNH CHO TRỢ LÝ AI TRONG GOOGLE FLOW TOOL BUILDER
# Phiên bản: v1.6.0 (Chapter Control Deck & Background Safe Engine)

Hãy cập nhật `App.tsx` theo các yêu cầu nâng cấp sau đây. 

⚠️ **QUY TẮC BẤT BIẾN (STRICT INVARIANTS - BẮT BUỘC TUÂN THỦ 100%):**
1. **TUYỆT ĐỐI KHÔNG VIẾT LẠI TOÀN BỘ FILE HAY LÀM THAY ĐỔI CẤU TRÚC GIAO DIỆN NGOÀI:**
   - Giữ nguyên 100% container gốc `h-screen w-screen bg-[#0a0b10] text-white overflow-hidden font-sans select-none`.
   - Giữ nguyên Sidebar `w-[340px]` và tất cả các component bên trong (Multi-Chapter Ingest, Shared Asset Bin, Pipeline Specs, Compute Matrix slider, Zip Archive button).
   - Giữ nguyên Header KPI (`QUEUE`, `READY`, `FAILED`, các nút `RETRY ALL FAILED`, `LAUNCH/HALT`).
   - Giữ nguyên Lưới 10-Slot Compute Matrix `h-[190px] grid grid-cols-5`.
   - Giữ nguyên Bảng Table hiển thị kết quả, Lightbox Preview Modal, System Telemetry Console.
2. **MODEL STRINGS:**
   - Video Model: Giữ nguyên tuyệt đối `'Veo 3.1 - Lite [Lower Priority]'` (0 credit).
   - Image Model: Giữ nguyên `'🍌 Nano Banana 2'`.
3. **CÁC CƠ CHẾ BẢO VỆ CỐT LÕI:**
   - Idempotent Auto-Download Guard (`downloadedTaskIdsRef.current`) giữ nguyên 100%.
   - Auto-retry 5 lần kèm Exponential Backoff giữ nguyên.
   - Fail-fast khi thiếu reference image giữ nguyên.

---

### VỊ TRÍ 1: KHAI BÁO STATE, REF & ENGINE CHẠY NGẦM (Bổ sung vào phần đầu component `App`)
Thêm các State, Ref và Hàm sau ngay trên dòng `// --- Helpers ---`:

```typescript
  // --- Chapter Execution Management ---
  const [enabledChapters, setEnabledChapters] = useState<Set<string>>(new Set());
  const enabledChaptersRef = useRef<Set<string>>(new Set());
  
  // --- Silent Audio Heartbeat Ref (Bypass Chrome Throttling & macOS App Nap) ---
  const audioContextRef = useRef<AudioContext | null>(null);

  useEffect(() => {
    enabledChaptersRef.current = enabledChapters;
  }, [enabledChapters]);

  // Tự động kích hoạt toàn bộ chương khi nạp file mới
  useEffect(() => {
    if (chapterList.length > 0) {
      setEnabledChapters(prev => {
        if (prev.size === 0) return new Set(chapterList);
        const next = new Set(prev);
        chapterList.forEach(ch => {
          if (!prev.has(ch) && !prev.has(`DISABLED_${ch}`)) next.add(ch);
        });
        return next;
      });
    }
  }, [chapterList]);

  // Bộ phát âm câm (Inaudible Audio) đánh lừa macOS và Chrome không được ngắt tiến trình khi thu nhỏ
  const startSilentAudio = () => {
    try {
      if (!audioContextRef.current) {
        const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
        if (AudioCtx) {
          const ctx = new AudioCtx();
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          gain.gain.value = 0.00001; // Silent heartbeat
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          audioContextRef.current = ctx;
        }
      }
      if (audioContextRef.current && audioContextRef.current.state === 'suspended') {
        audioContextRef.current.resume();
      }
    } catch (e) {
      console.warn('Silent audio init failed', e);
    }
  };

  const stopSilentAudio = () => {
    try {
      if (audioContextRef.current) {
        audioContextRef.current.close();
        audioContextRef.current = null;
      }
    } catch (e) {
      console.warn('Silent audio stop failed', e);
    }
  };

  // Cập nhật Worker State đồng bộ lập tức vào Ref (Dual-write) để không bị kẹt khi React hoãn render
  const updateWorkerSync = (workerIdx: number, updates: Partial<WorkerState>) => {
    workersRef.current[workerIdx] = { ...workersRef.current[workerIdx], ...updates };
    setWorkers([...workersRef.current]);
  };
```

---

### VỊ TRÍ 2: CẬP NHẬT LOGIC HÀNG ĐỢI & XỬ LÝ TASK (Thay thế trong `updateTask`, `processQueue`, `executeTaskOnWorker`)

1. Cập nhật hàm `updateTask`: Ghi đè trực tiếp `batchRef.current` tức thì trước khi gọi `setBatch`:
```typescript
  const updateTask = (taskId: string, updates: Partial<SceneTask>) => {
    const prev = batchRef.current;
    let newTasks = prev.tasks.map(t => t.id === taskId ? { ...t, ...updates } : t);
    const task = newTasks.find(t => t.id === taskId);
    
    if (task) {
      if (mode === 'chained' && task.type === 'image' && (task.status === 'failed' || task.status === 'blocked')) {
        newTasks = newTasks.map(t => {
          if (t.sceneId === task.sceneId && t.type === 'video' && t.status === 'idle') {
            activeTaskIdsRef.current.delete(t.id);
            return { ...t, status: task.status, error: 'Chained Image Failed' };
          }
          return t;
        });
      }
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
          else if (groupTasks.some(t => t.status === 'processing' || t.status === 'retrying')) groupStatus = 'processing';
          
          return { 
            ...g, 
            status: groupStatus,
            imageTask: groupTasks.find(t => t.type === 'image'),
            videoTask: groupTasks.find(t => t.type === 'video')
          };
        }
        return g;
      });
      batchRef.current = { ...prev, tasks: newTasks, groups: newGroups };
    } else {
      batchRef.current = { ...prev, tasks: newTasks };
    }
    setBatch(batchRef.current);
  };
```

2. Trong `processQueue`: 
- Thêm điều kiện lọc chỉ bốc task thuộc các chương đang được tích chọn:
```typescript
      // Select next available task
      const nextTask = batchRef.current.tasks.find(t => {
        if (t.status !== 'idle' && t.status !== 'pending') return false;
        if (activeTaskIdsRef.current.has(t.id)) return false;
        if (t.retryCount >= CONFIG.MAX_RETRIES) return false;
        
        // BỘ LỌC CHƯƠNG: Chỉ bốc task thuộc các chương đang được tick chọn
        const match = t.sceneId.match(/^([A-Za-z0-9]+)[_-]/);
        const ch = match ? match[1].toUpperCase() : 'OTHER';
        if (enabledChaptersRef.current.size > 0 && !enabledChaptersRef.current.has(ch)) {
          return false;
        }

        if (mode === 'chained' && t.type === 'video') {
          const imgTask = batchRef.current.tasks.find(it => it.sceneId === t.sceneId && it.type === 'image');
          return imgTask?.status === 'completed';
        }
        return true;
      });
```
- Khi gán task cho worker trong `processQueue`: dùng `updateWorkerSync` thay cho `setWorkers`:
```typescript
      if (nextTask) {
        activeTaskIdsRef.current.add(nextTask.id);
        lastDispatchTimeRef.current = Date.now();
        
        addLog('WORKER', `Slot ${availableWorkerIndex + 1} claimed ${nextTask.sceneId} (${nextTask.type.toUpperCase()})`, 'info');
        updateWorkerSync(availableWorkerIndex, { status: 'waiting', activeTaskId: nextTask.id });
        
        executeTaskOnWorker(availableWorkerIndex, nextTask);
      }
```

3. Trong `executeTaskOnWorker`:
- Khi set status waiting ban đầu:
```typescript
    updateWorkerSync(workerIdx, { 
      status: 'waiting', activeTaskId: task.id, message: `Stagger: ${waitTime}s`, countdown: waitTime 
    });
```
- Trong vòng lặp đếm lùi `while (Date.now() < targetLaunchTime)`:
```typescript
    while (Date.now() < targetLaunchTime) {
      if (!batchRef.current.isProcessing || batchRef.current.isPaused) {
        updateTask(task.id, { status: 'idle' });
        activeTaskIdsRef.current.delete(task.id);
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 });
        return;
      }
      const remaining = Math.max(0, Math.ceil((targetLaunchTime - Date.now()) / 1000));
      updateWorkerSync(workerIdx, { countdown: remaining });
      await new Promise(r => setTimeout(r, 1000));
    }
```
- Khi bắt đầu sinh:
```typescript
    updateTask(task.id, { status: 'processing', startedAt: Date.now() });
    updateWorkerSync(workerIdx, { 
      status: 'generating', message: `Generating ${task.type}...`, progress: 10, countdown: 0 
    });
```
- Khi hoàn thành:
```typescript
    activeTaskIdsRef.current.delete(task.id);
    updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Done', countdown: 0 });
    addLog('WORKER', `Slot ${workerIdx + 1} completed ${task.sceneId}`, 'success');
```
- Khi gặp lỗi hoặc retry: Dùng `updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, ... })`.

4. Trong `toggleProcessing`: Kích hoạt / Tắt Silent Audio Heartbeat:
```typescript
  const toggleProcessing = () => {
    if (batch.isProcessing) {
      setBatch(prev => ({ ...prev, isProcessing: false, isPaused: false }));
      stopSilentAudio();
      addLog('PIPELINE', 'Production halted', 'warning');
    } else {
      setBatch(prev => ({ ...prev, isProcessing: true, isPaused: false }));
      startSilentAudio();
      addLog('PIPELINE', '10-Slot Matrix launched (Background Safe Active)', 'info');
      setTimeout(processQueue, 100);
    }
  };
```

---

### VỊ TRÍ 3: THAY THẾ GIAO DIỆN BÀN ĐIỀU KHIỂN CHƯƠNG (Chapter Control Deck)
Thay thế toàn bộ khối thẻ cũ:
`<div className="px-4 py-2.5 border-b border-white/5 flex justify-between items-center bg-white/5 shrink-0"> ... </div>`
bằng khối giao diện Chapter Control Deck mới sau:

```tsx
            {/* Chapter Production Control Deck */}
            <div className="px-4 py-2.5 border-b border-white/10 bg-white/[0.03] shrink-0 flex flex-col gap-2">
              <div className="flex justify-between items-center">
                <div className="flex items-center gap-2">
                  <span className="text-[10px] font-bold text-violet-300 font-mono tracking-wider uppercase flex items-center gap-1.5">
                    <span className="material-symbols-outlined text-[14px]">tune</span>
                    CHAPTER CONTROLLER
                  </span>
                  <span className="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white/5 text-white/50 border border-white/10">
                    {chapterList.filter(ch => enabledChapters.has(ch)).length} / {chapterList.length} Active
                  </span>
                </div>
                
                {/* Bulk Actions */}
                <div className="flex items-center gap-1.5">
                  <button 
                    onClick={() => setEnabledChapters(new Set(chapterList))}
                    className="px-2 py-0.5 rounded text-[8px] font-mono font-bold bg-white/5 hover:bg-white/10 text-white/70 hover:text-white transition-colors"
                  >
                    Select All
                  </button>
                  <button 
                    onClick={() => setEnabledChapters(new Set())}
                    className="px-2 py-0.5 rounded text-[8px] font-mono font-bold bg-white/5 hover:bg-white/10 text-white/40 hover:text-white transition-colors"
                  >
                    Deselect All
                  </button>
                  <button 
                    onClick={() => {
                      const incomplete = chapterList.filter(ch => {
                        const chTasks = batch.tasks.filter(t => (t.sceneId.match(/^([A-Za-z0-9]+)[_-]/)?.[1]?.toUpperCase() || 'OTHER') === ch);
                        return chTasks.some(t => t.status !== 'completed');
                      });
                      setEnabledChapters(new Set(incomplete));
                    }}
                    className="px-2 py-0.5 rounded text-[8px] font-mono font-bold bg-violet-500/10 hover:bg-violet-500/20 text-violet-300 border border-violet-500/20 transition-colors"
                  >
                    ⚡ Run Incomplete Only
                  </button>
                  <div className="h-3 w-[1px] bg-white/10 mx-1" />
                  <button 
                    onClick={() => setSelectedChapter('ALL')}
                    className={`px-2 py-0.5 rounded text-[8px] font-mono font-bold transition-all ${selectedChapter === 'ALL' ? 'bg-violet-600 text-white shadow-sm' : 'bg-white/5 text-white/40 hover:text-white'}`}
                  >
                    View All ({batch.groups.length})
                  </button>
                </div>
              </div>

              {/* Scrollable Chapter Cards Strip */}
              <div className="flex items-center gap-2 overflow-x-auto dark-scrollbar pb-1">
                {chapterList.map(ch => {
                  const isEnabled = enabledChapters.has(ch);
                  const isFiltered = selectedChapter === ch;
                  const chTasks = batch.tasks.filter(t => (t.sceneId.match(/^([A-Za-z0-9]+)[_-]/)?.[1]?.toUpperCase() || 'OTHER') === ch);
                  const completedTasks = chTasks.filter(t => t.status === 'completed').length;
                  const totalTasks = chTasks.length;
                  const isCompleted = totalTasks > 0 && completedTasks === totalTasks;
                  const isRunning = chTasks.some(t => t.status === 'processing' || t.status === 'retrying');
                  const percent = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

                  return (
                    <div 
                      key={ch}
                      className={`flex items-center gap-2 px-2.5 py-1.5 rounded-xl border transition-all shrink-0 cursor-pointer ${
                        !isEnabled ? 'opacity-35 border-white/5 bg-white/[0.01]' :
                        isFiltered ? 'border-violet-500 bg-violet-600/15 shadow-sm shadow-violet-500/20' :
                        isCompleted ? 'border-emerald-500/30 bg-emerald-950/10 hover:border-emerald-500/50' :
                        isRunning ? 'border-violet-500/40 bg-violet-950/20 animate-pulse' :
                        'border-white/10 bg-white/5 hover:border-white/20'
                      }`}
                      onClick={() => setSelectedChapter(prev => prev === ch ? 'ALL' : ch)}
                    >
                      {/* Checkbox Bật / Tắt chạy cho chương này */}
                      <input 
                        type="checkbox"
                        checked={isEnabled}
                        onChange={(e) => {
                          e.stopPropagation();
                          setEnabledChapters(prev => {
                            const next = new Set(prev);
                            if (e.target.checked) next.add(ch);
                            else next.delete(ch);
                            return next;
                          });
                        }}
                        className="accent-violet-500 w-3.5 h-3.5 rounded cursor-pointer"
                        title={isEnabled ? "Đang bật chạy (Click để bỏ qua)" : "Đang tắt (Click để bật chạy)"}
                      />
                      
                      <div className="flex flex-col min-w-[70px]">
                        <div className="flex items-center justify-between gap-1.5">
                          <span className="text-[10px] font-mono font-bold text-white/90">{ch}</span>
                          <span className={`text-[8px] font-mono font-bold ${isCompleted ? 'text-emerald-400' : isRunning ? 'text-violet-400' : isEnabled ? 'text-white/40' : 'text-white/20'}`}>
                            {completedTasks}/{totalTasks}
                          </span>
                        </div>
                        {/* Mini Progress Bar */}
                        <div className="w-full h-1 bg-white/10 rounded-full mt-1 overflow-hidden">
                          <div 
                            className={`h-full transition-all duration-300 ${isCompleted ? 'bg-emerald-400' : isRunning ? 'bg-violet-500' : 'bg-white/30'}`}
                            style={{ width: `${percent}%` }}
                          />
                        </div>
                      </div>

                      {/* Status Pill Badge */}
                      <span className={`text-[7px] font-mono font-bold px-1 py-0.5 rounded uppercase ${
                        !isEnabled ? 'bg-white/5 text-white/30' :
                        isCompleted ? 'bg-emerald-500/20 text-emerald-300' :
                        isRunning ? 'bg-violet-500/20 text-violet-300' :
                        'bg-white/10 text-white/50'
                      }`}>
                        {!isEnabled ? 'OFF' : isCompleted ? 'DONE' : isRunning ? 'RUN' : 'WAIT'}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
```
