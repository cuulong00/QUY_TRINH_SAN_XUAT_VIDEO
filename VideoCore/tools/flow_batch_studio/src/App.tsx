import React, { useState, useEffect, useRef, useCallback, useMemo } from 'react';
import { Flow } from 'flow-sdk';
import JSZip from 'jszip';
import { SYSTEM_CONFIG } from './constants';
import { SceneGroup, SceneTask, WorkerState, BatchState, GenerationMode, SceneStatus } from './types';
import { parseStorytrack, sanitizePrompt, sanitizeFilename } from './services/parser';
import { SectionLabel, GlassPanel, KPI, ActionButton } from './components/Shared';

// ======================================================================
// CONFIGURATION & CONCURRENCY GUARD - PATCH v1.6.8 (SMART CIRCUIT BREAKER)
// ======================================================================
const CONFIG = {
  ...SYSTEM_CONFIG,
  MAX_CONCURRENT_VIDEOS: 2, // Khóa chặt 2 luồng video đồng thời (4 luồng bị Google chặn rate-limit ngay)
  RETRY_BACKOFF_STEPS: [10, 20, 35, 50, 70], // Giãn cách an toàn để nhả áp lực máy chủ
  VIDEO_WATCHDOG_S: 300, // 5 phút chuẩn xác: Quá 5m là Veo đã đứt socket -> Ngắt và dồn cuối queue ngay
  IMAGE_WATCHDOG_S: 90,   // 90s cho tạo ảnh
  IMAGE_FALLBACK_MODELS: ['🍌 Nano Banana 2', 'Nano Banana Pro', 'Imagen 3'],
  MAX_VEO_DEMOTE_RETRIES: 3, // Tối đa 3 vòng dồn video về cuối queue
  
  // --- HÀNG RÀO NHẬN DẠNG CHẶN ĐỒNG LOẠT (MASS BLOCK DEFENSE) ---
  MASS_BLOCK_THRESHOLD: 10,    // Khi có đúng 10 phân cảnh lỗi liên tiếp -> Xác định Flow chặn đồng loạt
  MASS_BLOCK_COOLDOWN_S: 3600, // Đóng băng hệ thống 3600 giây (60 phút) để Google Flow nhả rate-limit
  RATE_LIMIT_COOLDOWN_S: 3600  // Hạ nhiệt 3600s (60 phút) khi máy chủ trả mã lỗi rate limit
};

export default function App() {
  // --- Configuration State ---
  const [videoModel, setVideoModel] = useState<string>(SYSTEM_CONFIG.DEFAULT_VIDEO_MODEL);
  const [imageModel, setImageModel] = useState<string>(SYSTEM_CONFIG.DEFAULT_IMAGE_MODEL);
  const [aspectRatio, setAspectRatio] = useState<string>(SYSTEM_CONFIG.DEFAULT_ASPECT_RATIO);
  const [duration, setDuration] = useState<string>(SYSTEM_CONFIG.DEFAULT_DURATION);
  const [workersCount, setWorkersCount] = useState(2);
  const workersCountRef = useRef(workersCount);
  useEffect(() => { workersCountRef.current = workersCount; }, [workersCount]);
  const [jitter, setJitter] = useState({ min: SYSTEM_CONFIG.DEFAULT_MIN_JITTER_S, max: SYSTEM_CONFIG.DEFAULT_MAX_JITTER_S });
  
  // --- App State ---
  const [batch, setBatch] = useState<BatchState>({
    groups: [],
    tasks: [],
    isProcessing: false,
    isPaused: false,
    circuitBreakerActive: false,
    cooldownRemaining: 0,
    destinationSet: false
  });
  
  const [workers, setWorkers] = useState<WorkerState[]>(
    Array.from({ length: 10 }, (_, i) => ({
      id: i + 1,
      activeTaskId: null,
      status: 'idle',
      message: 'Standby',
      progress: 0,
      countdown: 0
    }))
  );
  const [logs, setLogs] = useState<{ id: string; timestamp: string; source: string; message: string; type: string }[]>([]);
  const [rawText, setRawText] = useState('');
  const [mode, setMode] = useState<GenerationMode>('chained');
  const [assetBin, setAssetBin] = useState<Map<string, { base64: string, mimeType: string }>>(new Map());
  const [isDragging, setIsDragging] = useState(false);
  const [isZipping, setIsZipping] = useState(false);
  
  // Lightbox State
  const [previewModal, setPreviewModal] = useState<{ type: 'image' | 'video'; url: string; title: string } | null>(null);
  
  // --- Chapter & Filter Management ---
  const [selectedChapter, setSelectedChapter] = useState<string>('ALL');
  const [enabledChapters, setEnabledChapters] = useState<Set<string>>(new Set());
  const enabledChaptersRef = useRef<Set<string>>(new Set());
  
  const chapterList = useMemo(() => {
    const chapters = new Set<string>();
    batch.tasks.forEach(t => {
      const match = t.sceneId.match(/^([A-Za-z0-9]+)[_-]/);
      chapters.add(match ? match[1].toUpperCase() : 'OTHER');
    });
    return Array.from(chapters).sort();
  }, [batch.tasks]);

  const batchRef = useRef(batch);
  const workersRef = useRef(workers);
  const processingRef = useRef(false);
  const imageInputRef = useRef<HTMLInputElement>(null);
  const lastDispatchRef = useRef<number>(0);
  const activeTaskIdsRef = useRef<Set<string>>(new Set());
  const downloadedTaskIdsRef = useRef<Set<string>>(new Set());
  const audioContextRef = useRef<AudioContext | null>(null);

  // --- REFS CHỐNG CHẶN ĐỒNG LOẠT ---
  const consecutiveFailuresRef = useRef<number>(0);
  const circuitCountdownTimerRef = useRef<any>(null);

  useEffect(() => {
    batchRef.current = batch;
    workersRef.current = workers;
  }, [batch, workers]);

  useEffect(() => {
    enabledChaptersRef.current = enabledChapters;
  }, [enabledChapters]);

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

  const startSilentAudio = () => {
    try {
      if (!audioContextRef.current) {
        const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
        if (AudioCtx) {
          const ctx = new AudioCtx();
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          gain.gain.value = 0.00001; 
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

  const updateWorkerSync = (workerIdx: number, updates: Partial<WorkerState>) => {
    workersRef.current[workerIdx] = { ...workersRef.current[workerIdx], ...updates };
    setWorkers([...workersRef.current]);
  };

  const addLog = useCallback((source: string, message: string, type: string = 'info') => {
    const timestamp = new Date().toLocaleTimeString([], { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
    setLogs(prev => [{ id: Math.random().toString(36).substr(2, 9), timestamp, source, message, type }, ...prev].slice(0, 50));
  }, []);

  const handleTxtUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = Array.from(e.target.files || []);
    if (files.length === 0) return;
    addLog('IMPORT', `Processing ${files.length} storyboard files...`, 'info');
    try {
      const contents = await Promise.all(files.map(file => {
        return new Promise<string>((resolve) => {
          const reader = new FileReader();
          reader.onload = (ev) => resolve(ev.target?.result as string);
          reader.readAsText(file);
        });
      }));
      const combinedContent = contents.join('\n');
      setRawText(combinedContent);
      const groups = parseStorytrack(combinedContent, mode);
      const tasks: SceneTask[] = [];
      groups.forEach(g => {
        if (g.imageTask) tasks.push(g.imageTask);
        if (g.videoTask) tasks.push(g.videoTask);
      });
      setBatch(prev => ({ ...prev, groups, tasks }));
      addLog('QUEUE', `Merged and imported ${groups.length} scenes (${tasks.length} tasks)`, 'success');
    } catch (err) {
      addLog('IMPORT', 'Failed to read multiple files', 'error');
    }
    e.target.value = '';
  };

  const processImageFile = (file: File) => {
    const reader = new FileReader();
    reader.onload = (ev) => {
      const base64 = (ev.target?.result as string).split(',')[1];
      setAssetBin(prev => {
        const next = new Map(prev);
        const cleanName = file.name.replace(/^@/, '');
        next.set(cleanName, { base64, mimeType: file.type });
        next.set('@' + cleanName, { base64, mimeType: file.type });
        next.set(cleanName.toLowerCase(), { base64, mimeType: file.type });
        next.set('@' + cleanName.toLowerCase(), { base64, mimeType: file.type });
        return next;
      });
    };
    reader.readAsDataURL(file);
  };

  const handleAssetSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = Array.from(e.target.files || []);
    files.forEach(processImageFile);
    e.target.value = '';
  };

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    const files = Array.from(e.dataTransfer.files);
    files.filter(f => f.type.startsWith('image/')).forEach(processImageFile);
  };

  const clearQueue = () => {
    setRawText('');
    activeTaskIdsRef.current.clear();
    downloadedTaskIdsRef.current.clear();
    consecutiveFailuresRef.current = 0;
    if (circuitCountdownTimerRef.current) clearInterval(circuitCountdownTimerRef.current);
    setBatch(prev => ({ ...prev, groups: [], tasks: [], isProcessing: false, circuitBreakerActive: false, cooldownRemaining: 0 }));
    setWorkers(prev => prev.map(w => ({ ...w, status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 })));
    addLog('QUEUE', 'Queue and workers cleared by operator', 'warning');
  };

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
          const anyRunning = groupTasks.some(t => t.status === 'processing' || t.status === 'retrying');
          let groupStatus: SceneStatus = 'idle';
          if (anyFailed) groupStatus = 'failed';
          else if (anyBlocked) groupStatus = 'blocked';
          else if (allCompleted) groupStatus = 'completed';
          else if (anyRunning) groupStatus = 'processing';
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

  const retryAllFailed = () => {
    activeTaskIdsRef.current.clear();
    consecutiveFailuresRef.current = 0;
    if (circuitCountdownTimerRef.current) clearInterval(circuitCountdownTimerRef.current);
    setBatch(prev => {
      const newTasks = prev.tasks.map(t => 
        (t.status !== 'completed') ? { ...t, status: 'idle' as const, progress: 0, retryCount: 0, error: undefined } : t
      );
      const newGroups = prev.groups.map(g => {
        const groupTasks = newTasks.filter(t => t.sceneId === g.sceneId);
        const allCompleted = groupTasks.every(t => t.status === 'completed');
        return { 
          ...g, 
          status: allCompleted ? 'completed' : 'idle' as SceneStatus,
          imageTask: groupTasks.find(t => t.type === 'image'),
          videoTask: groupTasks.find(t => t.type === 'video')
        };
      });
      return { ...prev, tasks: newTasks, groups: newGroups, isProcessing: true, isPaused: false, circuitBreakerActive: false, cooldownRemaining: 0 };
    });
    setWorkers(prev => prev.map(w => ({ ...w, status: 'idle', message: 'Standby', activeTaskId: null, countdown: 0 })));
    addLog('QUEUE', 'Toàn bộ các tác vụ chưa hoàn thành đã được reset về IDLE và kích hoạt lại!', 'warning');
    setTimeout(processQueue, 150);
  };

  const refreshScene = (sceneId: string) => {
    consecutiveFailuresRef.current = 0;
    setBatch(prev => {
      const newTasks = prev.tasks.map(t => 
        (t.sceneId === sceneId && t.status !== 'completed') 
          ? { ...t, status: 'idle' as const, progress: 0, retryCount: 0, error: undefined } 
          : t
      );
      const newGroups = prev.groups.map(g => {
        const groupTasks = newTasks.filter(t => t.sceneId === g.sceneId);
        return (g.sceneId === sceneId && g.status !== 'completed') ? { 
          ...g, 
          status: 'idle' as SceneStatus,
          imageTask: groupTasks.find(t => t.type === 'image'),
          videoTask: groupTasks.find(t => t.type === 'video')
        } : g;
      });
      return { ...prev, tasks: newTasks, groups: newGroups, isProcessing: true, isPaused: false };
    });
    setWorkers(prev => prev.map(w => {
      const task = batchRef.current.tasks.find(t => t.id === w.activeTaskId);
      if (task?.sceneId === sceneId && (w.status === 'idle' || w.message === 'Task Error' || w.message === 'Missing Asset' || w.message === 'Safety Block' || w.message === 'Rate-Limit Block')) {
        return { ...w, status: 'idle', message: 'Standby', activeTaskId: null };
      }
      return w;
    }));
    addLog('QUEUE', `Auto-resumed: Scene ${sceneId} reset`, 'info');
    setTimeout(processQueue, 150);
  };

  // Nút thủ công cho phép người dùng bỏ qua chờ hạ nhiệt và ép chạy tiếp
  const handleForceResumeCircuitBreaker = () => {
    if (circuitCountdownTimerRef.current) clearInterval(circuitCountdownTimerRef.current);
    consecutiveFailuresRef.current = 0;
    setBatch(prev => ({ ...prev, circuitBreakerActive: false, cooldownRemaining: 0, isProcessing: true, isPaused: false }));
    addLog('CIRCUIT', '⚡ Người dùng đã chủ động bỏ qua thời gian chờ hạ nhiệt.', 'info');
    setTimeout(processQueue, 200);
  };

  const processQueue = async () => {
    if (processingRef.current) return;
    processingRef.current = true;
    
    while (batchRef.current.isProcessing && !batchRef.current.isPaused) {
      if (batchRef.current.circuitBreakerActive) {
        await new Promise(r => setTimeout(r, 1000));
        continue;
      }
      // --- TỰ ĐỘNG GIẢI CỨU TÁC VỤ MỒ CÔI (ORPHAN TASK AUTO-REAPER) ---
      // Tìm các task mang cờ 'processing' hoặc 'waiting' nhưng KHÔNG có worker nào đang ôm thực tế
      const activeWorkerTaskIds = new Set(
        workersRef.current.filter(w => w.status !== 'idle' && w.activeTaskId).map(w => w.activeTaskId!)
      );
      
      let hasOrphans = false;
      const healedTasks = batchRef.current.tasks.map(t => {
        if ((t.status === 'processing' || t.status === 'waiting') && !activeWorkerTaskIds.has(t.id)) {
          hasOrphans = true;
          activeTaskIdsRef.current.delete(t.id);
          return { ...t, status: 'idle' as const };
        }
        return t;
      });
      if (hasOrphans) {
        const healedGroups = batchRef.current.groups.map(g => {
          const groupTasks = healedTasks.filter(t => t.sceneId === g.sceneId);
          const allCompleted = groupTasks.every(t => t.status === 'completed');
          const anyFailed = groupTasks.some(t => t.status === 'failed');
          const anyBlocked = groupTasks.some(t => t.status === 'blocked');
          const anyRunning = groupTasks.some(t => t.status === 'processing' || t.status === 'retrying');
          let groupStatus: SceneStatus = 'idle';
          if (anyFailed) groupStatus = 'failed';
          else if (anyBlocked) groupStatus = 'blocked';
          else if (allCompleted) groupStatus = 'completed';
          else if (anyRunning) groupStatus = 'processing';
          return {
            ...g,
            status: groupStatus,
            imageTask: groupTasks.find(t => t.type === 'image'),
            videoTask: groupTasks.find(t => t.type === 'video')
          };
        });
        batchRef.current = { ...batchRef.current, tasks: healedTasks, groups: healedGroups };
        setBatch(batchRef.current);
      }

      const availableWorkerIndex = workersRef.current.findIndex((w, i) => i < workersCountRef.current && w.status === 'idle');
      if (availableWorkerIndex === -1) {
        await new Promise(r => setTimeout(r, 1000));
        continue;
      }
      const activeVideoCount = workersRef.current.filter(w => {
        if (w.status !== 'generating' && w.status !== 'waiting') return false;
        const t = batchRef.current.tasks.find(task => task.id === w.activeTaskId);
        return t?.type === 'video';
      }).length;

      const nextTask = batchRef.current.tasks.find(t => {
        if (t.status !== 'idle' && t.status !== 'pending') return false;
        if (activeTaskIdsRef.current.has(t.id)) return false; 
        if (t.retryCount >= SYSTEM_CONFIG.MAX_RETRIES) return false;
        
        const match = t.sceneId.match(/^([A-Za-z0-9]+)[_-]/);
        const ch = match ? match[1].toUpperCase() : 'OTHER';
        if (enabledChaptersRef.current.size > 0 && !enabledChaptersRef.current.has(ch)) {
          return false;
        }
        if (t.type === 'video' && activeVideoCount >= CONFIG.MAX_CONCURRENT_VIDEOS) {
          return false;
        }
        if (mode === 'chained' && t.type === 'video') {
          const imgTask = batchRef.current.tasks.find(it => it.sceneId === t.sceneId && it.type === 'image');
          return imgTask?.status === 'completed';
        }
        return true;
      });

      if (nextTask) {
        // KHÓA TASK NGAY TỨC KHẮC để chống việc 2 Slot cùng bốc 1 task
        activeTaskIdsRef.current.add(nextTask.id);
        updateWorkerSync(availableWorkerIndex, { status: 'waiting', activeTaskId: nextTask.id });
        const now = Date.now();
        const diff = now - lastDispatchRef.current;
        if (diff < 1500) await new Promise(r => setTimeout(r, 1500 - diff));
        lastDispatchRef.current = Date.now();
        addLog('WORKER', `Slot ${availableWorkerIndex + 1} claimed ${nextTask.sceneId} (${nextTask.type.toUpperCase()})`, 'info');
        executeTaskOnWorker(availableWorkerIndex, nextTask);
      } else {
        const allDone = batchRef.current.tasks.every(t => {
          const match = t.sceneId.match(/^([A-Za-z0-9]+)[_-]/);
          const ch = match ? match[1].toUpperCase() : 'OTHER';
          const isIgnored = enabledChaptersRef.current.size > 0 && !enabledChaptersRef.current.has(ch);
          return isIgnored || t.status === 'completed' || t.status === 'failed' || t.status === 'blocked';
        });
        if (allDone && batchRef.current.tasks.length > 0) {
          setBatch(prev => ({ ...prev, isProcessing: false }));
          addLog('QUEUE', 'All active tasks completed!', 'success');
          break;
        }
        await new Promise(r => setTimeout(r, 1000));
      }
      await new Promise(r => setTimeout(r, 50));
    }
    processingRef.current = false;
  };

  const handleForceSkipWorker = (workerIdx: number) => {
    const worker = workersRef.current[workerIdx];
    if (!worker?.activeTaskId) return;
    const taskId = worker.activeTaskId;
    const task = batchRef.current.tasks.find(t => t.id === taskId);
    activeTaskIdsRef.current.delete(taskId);
    if (task) {
      if (task.type === 'video') {
        const allTasks = [...batchRef.current.tasks];
        const taskIdx = allTasks.findIndex(t => t.id === taskId);
        if (taskIdx !== -1) {
          const [demotedTask] = allTasks.splice(taskIdx, 1);
          demotedTask.status = 'idle';
          demotedTask.retryCount = (demotedTask.retryCount || 0) + 1;
          demotedTask.error = 'Manually Skipped to Tail';
          allTasks.push(demotedTask);
          
          const newGroups = batchRef.current.groups.map(g => {
            if (g.sceneId === task.sceneId) {
              const groupTasks = allTasks.filter(t => t.sceneId === task.sceneId);
              return {
                ...g,
                status: 'idle' as SceneStatus,
                imageTask: groupTasks.find(t => t.type === 'image'),
                videoTask: demotedTask
              };
            }
            return g;
          });
          batchRef.current = { ...batchRef.current, tasks: allTasks, groups: newGroups };
          setBatch(batchRef.current);
        }
        addLog('WORKER', `Operator chủ động Skip ${task.sceneId} -> Bảo lưu ảnh, đẩy video về cuối queue`, 'warning');
      } else {
        updateTask(taskId, { status: 'failed', error: 'Manually Skipped' });
        addLog('WORKER', `Operator chủ động Skip ${task.sceneId} (Image)`, 'warning');
      }
    }
    updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 });
    setTimeout(processQueue, 150);
  };

  const executeTaskOnWorker = async (workerIdx: number, task: SceneTask) => {
    updateTask(task.id, { status: 'processing', startedAt: Date.now() });
    updateWorkerSync(workerIdx, { 
      status: 'generating', activeTaskId: task.id, message: `Generating ${task.type}...`, progress: 15, countdown: 0 
    });
    let watchdogTimer: any;
    try {
      const cleanPrompt = sanitizePrompt(task.prompt);
      
      const generationPromise = task.type === 'image' 
        ? (async () => {
            let referenceImageMediaIds: string[] = [];
            if (task.referenceFile) {
              const cleanRef = task.referenceFile.replace(/^@/, '').trim();
              const asset = assetBin.get(cleanRef) || 
                            assetBin.get('@' + cleanRef) || 
                            assetBin.get(cleanRef.toLowerCase()) || 
                            assetBin.get('@' + cleanRef.toLowerCase());
              if (!asset) {
                throw new Error(`MISSING_REF_ASSET: Reference @${cleanRef} not found in Asset Bin`);
              }
              
              let refMediaId = (asset as any).uploadedMediaId;
              if (!refMediaId) {
                const cleanBase64 = asset.base64.includes(',') ? asset.base64.split(',')[1] : asset.base64;
                const uploaded = await Flow.upload({ 
                  base64: cleanBase64, 
                  mimeType: asset.mimeType as any, 
                  name: cleanRef 
                });
                refMediaId = uploaded.mediaId;
                (asset as any).uploadedMediaId = refMediaId;
              }
              referenceImageMediaIds = [refMediaId];
            }
            const targetImageModel = (task as any).assignedModel || imageModel;
            return Flow.generate.image({
              prompt: cleanPrompt,
              modelDisplayName: targetImageModel,
              aspectRatio: aspectRatio as any,
              referenceImageMediaIds
            });
          })()
        : (async () => {
            let firstFrameImageMediaId: string | undefined;
            if (mode === 'chained') {
              const imgTask = batchRef.current.tasks.find(t => t.sceneId === task.sceneId && t.type === 'image');
              if (imgTask?.resultMediaId) {
                firstFrameImageMediaId = imgTask.resultMediaId;
              } else if (imgTask?.resultBase64) {
                const cleanBase64 = imgTask.resultBase64.includes(',') 
                  ? imgTask.resultBase64.split(',')[1] 
                  : imgTask.resultBase64;
                const uploaded = await Flow.upload({
                  base64: cleanBase64,
                  mimeType: (imgTask.resultMimeType || 'image/png') as any,
                  name: `${task.sceneId}_first_frame.png`
                });
                firstFrameImageMediaId = uploaded.mediaId;
                updateTask(imgTask.id, { resultMediaId: uploaded.mediaId });
              } else {
                throw new Error(`CHAIN_ERROR: Generated image for ${task.sceneId} is missing!`);
              }
            }
            return Flow.generate.video({
              prompt: cleanPrompt,
              modelDisplayName: videoModel,
              aspectRatio: aspectRatio as any,
              firstFrameImageMediaId,
              durationSeconds: parseInt(duration) as any
            });
          })();

      const timeoutLimitS = task.type === 'video' ? CONFIG.VIDEO_WATCHDOG_S : CONFIG.IMAGE_WATCHDOG_S;
      const watchdogPromise = new Promise((_, reject) => {
        watchdogTimer = setTimeout(() => {
          reject(new Error(task.type === 'video' ? 'VEO_WATCHDOG_TIMEOUT' : 'IMAGE_WATCHDOG_TIMEOUT'));
        }, timeoutLimitS * 1000);
      });

      const result = await Promise.race([generationPromise, watchdogPromise]) as { base64: string, mimeType: string, mediaId?: string };
      clearTimeout(watchdogTimer);
      
      updateTask(task.id, { 
        status: 'completed', 
        resultMediaId: result.mediaId, 
        resultBase64: result.base64, 
        resultMimeType: result.mimeType,
        completedAt: Date.now() 
      });

      const shouldDownload = 
        (mode === 'chained' && task.type === 'video') || 
        (mode === 'image-only' && task.type === 'image') || 
        (mode === 'video-only' && task.type === 'video');
      
      if (shouldDownload && !downloadedTaskIdsRef.current.has(task.id)) {
        downloadedTaskIdsRef.current.add(task.id);
        await Flow.download({
          base64: result.base64,
          mimeType: result.mimeType,
          filename: sanitizeFilename(task.sceneId, task.type, result.mimeType)
        });
        updateTask(task.id, { downloaded: true });
      }

      activeTaskIdsRef.current.delete(task.id);

      // 🟢 QUAN TRỌNG: TASK NÀY THÀNH CÔNG -> RESET NGAY BỘ ĐẾM LỖI LIÊN TIẾP VỀ 0!
      consecutiveFailuresRef.current = 0;

      updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Done', countdown: 0 });
      addLog('WORKER', `Slot ${workerIdx + 1} completed ${task.sceneId} (${task.type.toUpperCase()})`, 'success');
    } catch (err: any) {
      clearTimeout(watchdogTimer);
      const errMsg = err?.message || 'Unknown error';
      console.error(`Task ${task.id} failed:`, errMsg);
      activeTaskIdsRef.current.delete(task.id);

      // TĂNG BỘ ĐẾM LỖI LIÊN TIẾP
      consecutiveFailuresRef.current += 1;
      const failCount = consecutiveFailuresRef.current;

      // ======================================================================
      // 🛑 KIỂM TRA ĐIỀU KIỆN CHẶN ĐỒNG LOẠT (MASS BLOCKING DEFENSE)
      // ======================================================================
      const isMassBlock = failCount >= CONFIG.MASS_BLOCK_THRESHOLD;
      const isExplicitRateLimit = errMsg.includes('429') || errMsg.includes('QUOTA') || errMsg.includes('EXHAUSTED') || errMsg.includes('RESOURCE_EXHAUSTED');

      if (isMassBlock || isExplicitRateLimit) {
        const cooldownTime = isMassBlock ? CONFIG.MASS_BLOCK_COOLDOWN_S : CONFIG.RATE_LIMIT_COOLDOWN_S;
        
        addLog('CIRCUIT', `🚨 PHÁT HIỆN FLOW CHẶN ĐỒNG LOẠT (${failCount} lỗi liên tiếp)! DỪNG RETRY ĐỂ TRÁNH BỊ KHÓA TÀI KHOẢN!`, 'error');
        addLog('CIRCUIT', `🛑 Tự động đóng băng hàng đợi và hạ nhiệt trong ${cooldownTime}s...`, 'warning');

        // Đưa task hiện tại về IDLE để sau khi hạ nhiệt sẽ chạy lại
        updateTask(task.id, { status: 'idle', error: isMassBlock ? `Tạm dừng: Flow chặn đồng loạt (${failCount} lỗi)` : 'Rate Limit 429' });
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Rate-Limit Block', countdown: 0 });

        // Kích hoạt Circuit Breaker toàn cục
        setBatch(prev => ({
          ...prev,
          circuitBreakerActive: true,
          cooldownRemaining: cooldownTime
        }));

        // Thiết lập đồng hồ đếm ngược hạ nhiệt
        if (circuitCountdownTimerRef.current) clearInterval(circuitCountdownTimerRef.current);
        circuitCountdownTimerRef.current = setInterval(() => {
          setBatch(prev => {
            if (prev.cooldownRemaining <= 1) {
              clearInterval(circuitCountdownTimerRef.current);
              consecutiveFailuresRef.current = 0; // Reset sau khi hạ nhiệt xong
              addLog('CIRCUIT', '✅ Đã hoàn tất thời gian hạ nhiệt. Hệ thống tự động tiếp tục an toàn.', 'success');
              
              setTimeout(() => {
                if (batchRef.current.isProcessing && !batchRef.current.isPaused) {
                  processQueue();
                }
              }, 500);

              return { ...prev, circuitBreakerActive: false, cooldownRemaining: 0 };
            }
            return { ...prev, cooldownRemaining: prev.cooldownRemaining - 1 };
          });
        }, 1000);

        return; // DỪNG NGAY! TUYỆT ĐỐI KHÔNG GỌI RETRY SPAM NỮA!
      }

      // ======================================================================
      // 🟢 XỬ LÝ LỖI ĐƠN LẺ (ISOLATED FAILURE: failCount < 10)
      // ======================================================================

      // 1. Missing Reference Asset
      if (errMsg.includes('MISSING_REF_ASSET')) {
        updateTask(task.id, { status: 'failed', error: 'Missing Asset' });
        addLog('ASSET', `Halted ${task.sceneId}: Missing @${task.referenceFile}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Missing Asset', countdown: 0 });
        return;
      } 
      
      // 2. Safety Block
      if (errMsg.includes('SAFETY') || errMsg.includes('BLOCK')) {
        updateTask(task.id, { status: 'blocked', error: 'Safety Block' });
        addLog('WORKER', `Safety block on ${task.sceneId}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Safety Block', countdown: 0 });
        return;
      }

      // 3. Ảnh lỗi hoặc treo -> Fallback Model chu kỳ thông minh
      if (task.type === 'image') {
        const normalize = (m: string) => m.replace(/🍌\s*/g, '').trim().toLowerCase();
        const currentAssigned = (task as any).assignedModel || imageModel;
        const currentNorm = normalize(currentAssigned);
        const currentIdx = CONFIG.IMAGE_FALLBACK_MODELS.findIndex(m => normalize(m) === currentNorm);
        const nextModel = (currentIdx !== -1 && currentIdx < CONFIG.IMAGE_FALLBACK_MODELS.length - 1)
          ? CONFIG.IMAGE_FALLBACK_MODELS[currentIdx + 1]
          : (currentIdx === -1 && CONFIG.IMAGE_FALLBACK_MODELS.length > 1 ? CONFIG.IMAGE_FALLBACK_MODELS[1] : null);

        if (nextModel) {
          (task as any).assignedModel = nextModel;
          addLog('FALLBACK', `Ảnh ${task.sceneId} lỗi [${errMsg.substring(0, 25)}] -> Chuyển sang model dự phòng [${nextModel}] (Chuỗi lỗi: ${failCount}/${CONFIG.MASS_BLOCK_THRESHOLD})`, 'warning');
          updateTask(task.id, { status: 'idle', error: `Fallback: ${nextModel}` });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Model Fallback', countdown: 0 });
          setTimeout(processQueue, 1000);
          return;
        } else {
          // Đã thử hết toàn bộ model ảnh mà vẫn lỗi -> Dồn cảnh này về cuối queue để không chặn các cảnh khác
          addLog('FALLBACK', `Ảnh ${task.sceneId} đã thử hết toàn bộ model (${CONFIG.IMAGE_FALLBACK_MODELS.join(' -> ')}) -> Dồn về cuối queue để ưu tiên cảnh khác!`, 'error');
          const allTasks = [...batchRef.current.tasks];
          const taskIdx = allTasks.findIndex(t => t.id === task.id);
          if (taskIdx !== -1) {
            const [demoted] = allTasks.splice(taskIdx, 1);
            demoted.status = 'idle';
            (demoted as any).assignedModel = CONFIG.IMAGE_FALLBACK_MODELS[0]; // Reset model chính cho vòng sau
            demoted.retryCount = (demoted.retryCount || 0) + 1;
            allTasks.push(demoted);
            batchRef.current = { ...batchRef.current, tasks: allTasks };
            setBatch(batchRef.current);
          }
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Demoted', countdown: 0 });
          setTimeout(processQueue, 1000);
          return;
        }
      }

      // 4. Video lỗi hoặc treo (>7m hoặc server error) -> BẢO LƯU ẢNH 100%, DỒN XUỐNG CUỐI QUEUE
      if (task.type === 'video') {
        const currentRetries = (task.retryCount || 0) + 1;
        if (currentRetries <= CONFIG.MAX_VEO_DEMOTE_RETRIES) {
          addLog('WATCHDOG', `Cảnh ${task.sceneId} lỗi đơn lẻ -> Bảo lưu ảnh, dồn video về cuối queue (${currentRetries}/${CONFIG.MAX_VEO_DEMOTE_RETRIES}) [Chuỗi lỗi: ${failCount}/${CONFIG.MASS_BLOCK_THRESHOLD}]`, 'warning');
          
          const allTasks = [...batchRef.current.tasks];
          const taskIdx = allTasks.findIndex(t => t.id === task.id);
          if (taskIdx !== -1) {
            const [demotedTask] = allTasks.splice(taskIdx, 1);
            demotedTask.status = 'idle';
            demotedTask.retryCount = currentRetries;
            demotedTask.error = `Error: ${errMsg.substring(0, 30)} (Requeued)`;
            allTasks.push(demotedTask);
            // Cập nhật đồng bộ cả tasks lẫn groups
            const newGroups = batchRef.current.groups.map(g => {
              if (g.sceneId === task.sceneId) {
                const groupTasks = allTasks.filter(t => t.sceneId === task.sceneId);
                const allCompleted = groupTasks.every(t => t.status === 'completed');
                return {
                  ...g,
                  status: allCompleted ? 'completed' : 'idle' as SceneStatus,
                  imageTask: groupTasks.find(t => t.type === 'image'),
                  videoTask: demotedTask
                };
              }
              return g;
            });
            batchRef.current = { ...batchRef.current, tasks: allTasks, groups: newGroups };
            setBatch(batchRef.current);
          }
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 });
          setTimeout(processQueue, 300);
          return;
        } else {
          addLog('WORKER', `Cảnh ${task.sceneId} thất bại vĩnh viễn sau ${CONFIG.MAX_VEO_DEMOTE_RETRIES} lần dồn queue`, 'error');
          updateTask(task.id, { status: 'failed', error: errMsg });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Task Failed', countdown: 0 });
          setTimeout(processQueue, 300);
          return;
        }
      }

      // 5. Retry thông thường với Exponential Backoff cho các lỗi đơn lẻ còn lại
      const nextRetry = (task.retryCount || 0) + 1;
      const backoffList = CONFIG.RETRY_BACKOFF_STEPS || [10, 20, 35, 50, 70];
      const backoff = backoffList[nextRetry - 1] || 20;
      if (nextRetry <= SYSTEM_CONFIG.MAX_RETRIES) {
        updateTask(task.id, { status: 'retrying', retryCount: nextRetry, error: errMsg });
        addLog('WORKER', `Lỗi đơn lẻ ${task.sceneId}: Thử lại (${nextRetry}/${SYSTEM_CONFIG.MAX_RETRIES}) sau ${backoff}s [Chuỗi lỗi: ${failCount}/${CONFIG.MASS_BLOCK_THRESHOLD}]`, 'warning');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 });
        
        setTimeout(() => {
          updateTask(task.id, { status: 'idle' });
          if (batchRef.current.isProcessing && !batchRef.current.isPaused && !batchRef.current.circuitBreakerActive) {
            processQueue();
          }
        }, backoff * 1000);
      } else {
        updateTask(task.id, { status: 'failed', error: errMsg });
        addLog('WORKER', `Permanent Failure: ${task.sceneId}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Task Failed', countdown: 0 });
      }
    }
  };

  const toggleProcessing = () => {
    if (batch.isProcessing) {
      setBatch(prev => ({ ...prev, isProcessing: false, isPaused: false }));
      stopSilentAudio();
      addLog('PIPELINE', 'Production halted', 'warning');
    } else {
      setBatch(prev => ({ ...prev, isProcessing: true, isPaused: false }));
      startSilentAudio();
      addLog('PIPELINE', 'Matrix launched (Auto-Optimize Active)', 'info');
      setTimeout(processQueue, 100);
    }
  };

  const downloadAllAsZip = async () => {
    const completedTasks = batch.tasks.filter(t => t.status === 'completed' && t.resultBase64);
    if (completedTasks.length === 0) return;
    setIsZipping(true);
    addLog('EXPORT', `Bundling ${completedTasks.length} assets...`, 'info');
    try {
      const zip = new JSZip();
      completedTasks.forEach(task => {
        const filename = sanitizeFilename(task.sceneId, task.type, task.resultMimeType || 'image/png');
        zip.file(filename, task.resultBase64!, { base64: true });
      });
      const blob = await zip.generateAsync({ type: 'blob' });
      const reader = new FileReader();
      reader.onload = async () => {
        const base64 = (reader.result as string).split(',')[1];
        await Flow.download({
          base64,
          mimeType: 'application/zip',
          filename: `Production_Batch_${new Date().getTime()}.zip`
        });
        addLog('EXPORT', 'Export successful', 'success');
        setIsZipping(false);
      };
      reader.readAsDataURL(blob);
    } catch (err) {
      addLog('EXPORT', 'Export failed', 'error');
      setIsZipping(false);
    }
  };

  const getStatusBadge = (status: SceneStatus, step: string, isImageReady: boolean = false) => {
    switch (status) {
      case 'completed': return <span className="bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2 py-0.5 rounded text-[8px] font-bold">COMPLETED ✓</span>;
      case 'processing': return <span className="bg-violet-500/10 text-violet-400 border border-violet-500/20 px-2 py-0.5 rounded text-[8px] font-bold animate-pulse">GENERATING...</span>;
      case 'retrying': return <span className="bg-amber-500/10 text-amber-400 border border-amber-500/20 px-2 py-0.5 rounded text-[8px] font-bold animate-pulse">RETRYING...</span>;
      case 'failed': return <span className="bg-rose-500/10 text-rose-400 border border-rose-500/20 px-2 py-0.5 rounded text-[8px] font-bold">FAILED</span>;
      case 'blocked': return <span className="bg-amber-500/10 text-amber-400 border border-amber-500/20 px-2 py-0.5 rounded text-[8px] font-bold">BLOCKED</span>;
      case 'idle': 
        if (step === 'video' && mode === 'chained') {
          if (isImageReady) return <span className="bg-violet-500/10 text-violet-300 border border-violet-500/20 px-2 py-0.5 rounded text-[8px] font-bold">READY</span>;
          return <span className="text-white/20 px-2 py-0.5 rounded text-[8px] font-bold">WAITING IMG</span>;
        }
        return <span className="text-white/20 px-2 py-0.5 rounded text-[8px] font-bold">PENDING</span>;
      default: return null;
    }
  };

  const getMediaSrc = (base64?: string, mimeType?: string) => {
    if (!base64) return '';
    return base64.startsWith('data:') ? base64 : `data:${mimeType || 'image/png'};base64,${base64}`;
  };

  const filteredGroups = useMemo(() => {
    if (selectedChapter === 'ALL') return batch.groups;
    return batch.groups.filter(g => (g.sceneId.match(/^([A-Za-z0-9]+)[_-]/)?.[1]?.toUpperCase() || 'OTHER') === selectedChapter);
  }, [batch.groups, selectedChapter]);

  return (
    <div className="flex h-screen w-screen bg-[#0a0b10] text-white overflow-hidden font-sans select-none">
      
      {/* Sidebar UI */}
      <aside className="w-[340px] border-r border-white/10 flex flex-col p-4 gap-6 bg-[#0a0b10]/95 overflow-y-auto dark-scrollbar shrink-0">
        <div>
          <h2 className="text-2xl font-black tracking-tighter mb-1 text-violet-400">BATCH PRODUCTION</h2>
          <p className="text-[10px] text-white/40 font-mono uppercase tracking-widest">Master Pipeline v1.6.8</p>
        </div>
        <section>
          <div className="flex justify-between items-center mb-1.5">
            <SectionLabel>Story Import</SectionLabel>
            <ActionButton onClick={clearQueue} variant="ghost" icon="delete" className="text-rose-400 hover:bg-rose-500/10 h-[24px] px-2 text-[10px]">Clear</ActionButton>
          </div>
          <div className="flex flex-col gap-2">
            <label className="relative flex items-center justify-center gap-2 h-[34px] w-full border border-white/10 rounded-xl bg-white/5 hover:bg-white/10 transition-all cursor-pointer text-[11px] font-bold">
              <span className="material-symbols-outlined text-[18px]">upload_file</span>
              📂 Load Storytrack (.txt)
              <input type="file" accept=".txt" multiple onChange={handleTxtUpload} className="hidden" />
            </label>
            <textarea 
              className="w-full h-24 bg-white/5 border border-white/10 rounded-xl p-3 text-[11px] font-mono resize-none outline-none focus:border-violet-500/50 transition-colors"
              placeholder="SCENE_01 [IMAGE]: @char -> Prompt..."
              value={rawText}
              onChange={(e) => setRawText(e.target.value)}
            />
          </div>
        </section>
        <section>
          <SectionLabel>Reference Asset Bin</SectionLabel>
          <div 
            className={`w-full min-h-[90px] border-2 border-dashed rounded-xl flex flex-col items-center justify-center p-3 transition-all cursor-pointer ${
              isDragging ? 'border-violet-500 bg-violet-500/10' : 'border-white/10 bg-white/5 hover:border-white/20'
            }`}
            onClick={() => imageInputRef.current?.click()}
            onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
            onDragLeave={() => setIsDragging(false)}
            onDrop={handleDrop}
          >
            <input type="file" multiple accept="image/*" ref={imageInputRef} className="hidden" onChange={handleAssetSelect} />
            <span className="material-symbols-outlined text-white/20 text-2xl mb-1">inventory_2</span>
            <span className="text-[10px] text-white/40 text-center font-mono uppercase">Reference Ingest Zone</span>
            
            {assetBin.size > 0 && (
              <div className="mt-2 w-full flex flex-wrap gap-1">
                {Array.from(new Set(Array.from(assetBin.keys()).map(k => k.replace(/^@/, '')))).map(name => (
                  <div key={name} className="px-1.5 py-0.5 bg-violet-600/20 border border-violet-500/30 rounded text-[9px] font-mono text-violet-300">
                    @{name}
                  </div>
                ))}
              </div>
            )}
          </div>
        </section>
        <section>
          <SectionLabel>Pipeline Specs</SectionLabel>
          <div className="flex flex-col gap-2">
            <div className="bg-white/5 p-2 rounded-xl border border-white/10">
              <span className="text-[9px] text-white/30 block mb-1 uppercase tracking-wider">Mode</span>
              <select value={mode} onChange={(e) => setMode(e.target.value as GenerationMode)} className="w-full bg-transparent border-none outline-none text-[11px] font-bold text-white">
                <option value="chained">Chained: Image → Video</option>
                <option value="image-only">Image Only</option>
                <option value="video-only">Video Only</option>
              </select>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div className="bg-white/5 p-2 rounded-xl border border-white/10">
                <span className="text-[9px] text-white/30 block mb-1 uppercase">AR</span>
                <select value={aspectRatio} onChange={(e) => setAspectRatio(e.target.value)} className="w-full bg-transparent border-none outline-none text-[11px] font-bold text-white">
                  {SYSTEM_CONFIG.ASPECT_RATIOS.map(r => <option key={r} value={r}>{r}</option>)}
                </select>
              </div>
              <div className="bg-white/5 p-2 rounded-xl border border-white/10">
                <span className="text-[9px] text-white/30 block mb-1 uppercase">DUR</span>
                <select value={duration} onChange={(e) => setDuration(e.target.value)} className="w-full bg-transparent border-none outline-none text-[11px] font-bold text-white">
                  {SYSTEM_CONFIG.DURATIONS.map(d => <option key={d} value={d}>{d}</option>)}
                </select>
              </div>
            </div>
            <div className="bg-white/5 p-2 rounded-xl border border-white/10">
              <span className="text-[9px] text-white/30 block mb-1 uppercase">Video Model</span>
              <select value={videoModel} onChange={(e) => setVideoModel(e.target.value)} className="w-full bg-transparent border-none outline-none text-[11px] font-bold text-white">
                {SYSTEM_CONFIG.VIDEO_MODELS.map(m => <option key={m} value={m}>{m}</option>)}
              </select>
            </div>
            <div className="bg-white/5 p-2 rounded-xl border border-white/10">
              <span className="text-[9px] text-white/30 block mb-1 uppercase">Image Model</span>
              <select value={imageModel} onChange={(e) => setImageModel(e.target.value)} className="w-full bg-transparent border-none outline-none text-[11px] font-bold text-white">
                {SYSTEM_CONFIG.IMAGE_MODELS.map(m => <option key={m} value={m}>{m}</option>)}
              </select>
            </div>
          </div>
        </section>
        <section>
          <SectionLabel>Compute Slots</SectionLabel>
          <div className="flex flex-col gap-4 px-1">
            <div>
              <div className="flex justify-between text-[11px] mb-1">
                <span className="text-white/40">Active Workers</span>
                <span className="font-mono text-violet-400">{workersCount}</span>
              </div>
              <input type="range" min={SYSTEM_CONFIG.MIN_WORKERS} max={SYSTEM_CONFIG.MAX_WORKERS} value={workersCount} onChange={(e) => setWorkersCount(parseInt(e.target.value))} className="w-full accent-violet-600 h-1.5 bg-white/10 rounded-full cursor-pointer" />
            </div>
            <div className="grid grid-cols-1 gap-3">
              <div>
                <div className="flex justify-between text-[10px] mb-1">
                  <span className="text-white/40">Min Jitter</span>
                  <span className="font-mono text-amber-500">{jitter.min}s</span>
                </div>
                <input type="range" min={SYSTEM_CONFIG.JITTER_MIN_RANGE.min} max={SYSTEM_CONFIG.JITTER_MIN_RANGE.max} value={jitter.min} onChange={(e) => setJitter(j => ({ ...j, min: parseInt(e.target.value) }))} className="w-full accent-amber-500 h-1 bg-white/10 rounded-full cursor-pointer" />
              </div>
              <div>
                <div className="flex justify-between text-[10px] mb-1">
                  <span className="text-white/40">Max Jitter</span>
                  <span className="font-mono text-amber-500">{jitter.max}s</span>
                </div>
                <input type="range" min={SYSTEM_CONFIG.JITTER_MAX_RANGE.min} max={SYSTEM_CONFIG.JITTER_MAX_RANGE.max} value={jitter.max} onChange={(e) => setJitter(j => ({ ...j, max: parseInt(e.target.value) }))} className="w-full accent-amber-500 h-1 bg-white/10 rounded-full cursor-pointer" />
              </div>
            </div>
          </div>
        </section>
        <section className="mt-auto">
          <SectionLabel>Batch Export</SectionLabel>
          <ActionButton 
            onClick={downloadAllAsZip} 
            variant="ghost" 
            icon={isZipping ? "sync" : "archive"} 
            className="w-full border-emerald-500/30 text-emerald-400 h-[38px]"
            disabled={isZipping || batch.tasks.filter(t => t.status === 'completed').length === 0}
          >
            {isZipping ? "PREPARING ZIP..." : "ZIP COMPLETED ASSETS"}
          </ActionButton>
        </section>
      </aside>

      {/* Main Floor */}
      <main className="flex-1 flex flex-col overflow-hidden bg-black/20">
        
        {/* Statistics Header */}
        <header className="p-6 border-b border-white/10 bg-[#0a0b10]/60 backdrop-blur-md z-10">
          <div className="flex justify-between items-center mb-6">
            <div className="flex gap-2">
              <KPI label="SCENES" value={batch.groups.length} />
              <KPI 
                label="READY" 
                value={
                  mode === 'chained' 
                    ? batch.tasks.filter(t => t.type === 'video' && t.status === 'completed').length 
                    : batch.tasks.filter(t => t.status === 'completed').length
                } 
                color="text-emerald-400" 
              />
              <KPI label="FAILED" value={batch.tasks.filter(t => t.status === 'failed' || t.status === 'blocked').length} color="text-rose-400" />
            </div>
            <div className="flex gap-2">
              <ActionButton onClick={retryAllFailed} variant="ghost" icon="restart_alt" className="border-rose-500/20 text-rose-400 h-[34px]">
                RETRY ALL FAILED
              </ActionButton>
              <ActionButton 
                onClick={toggleProcessing} 
                variant={batch.isProcessing ? "danger" : "primary"}
                icon={batch.isProcessing ? "pause" : "play_arrow"}
                className="h-[34px] min-w-[160px]"
              >
                {batch.isProcessing ? "HALT PRODUCTION" : "LAUNCH MATRIX"}
              </ActionButton>
            </div>
          </div>
          <div className="relative h-1.5 w-full bg-white/5 rounded-full overflow-hidden">
            <div 
              className="absolute top-0 left-0 h-full bg-gradient-to-r from-violet-600 to-emerald-400 transition-all duration-700"
              style={{ width: `${batch.tasks.length > 0 ? (batch.tasks.filter(t => t.status === 'completed').length / batch.tasks.length) * 100 : 0}%` }}
            />
          </div>
        </header>

        {/* Compute Slots Matrix */}
        <section className="p-6 grid grid-cols-5 gap-3 h-[190px] shrink-0 overflow-y-auto dark-scrollbar">
          {workers.slice(0, workersCount).map((worker) => (
            <GlassPanel key={worker.id} className={`p-3 flex flex-col justify-between transition-all duration-300 border-white/5 ${worker.status !== 'idle' ? 'border-violet-500/40 bg-violet-950/10 shadow-lg' : 'opacity-20'}`}>
              <div className="flex justify-between items-start">
                <span className="text-[8px] font-mono text-white/40 tracking-[1px]">SLOT-{worker.id}</span>
                <div className="flex items-center gap-1.5">
                  {worker.status !== 'idle' && worker.activeTaskId && (
                    <button 
                      title="Chủ động giải phóng Slot này (Đẩy video xuống cuối queue)"
                      onClick={() => handleForceSkipWorker(worker.id - 1)}
                      className="text-[11px] text-white/40 hover:text-rose-400 transition-colors cursor-pointer material-symbols-outlined leading-none"
                    >
                      close
                    </button>
                  )}
                  <span className={`text-[7px] px-1.5 py-0.5 rounded font-bold ${
                    worker.status === 'generating' ? 'bg-violet-600 text-white animate-pulse' : 
                    worker.status === 'waiting' ? 'bg-amber-600 text-black' : 'bg-white/10 text-white/40'
                  }`}>
                    {worker.status.toUpperCase()}
                  </span>
                </div>
              </div>
              <div className="my-1 truncate">
                <p className="text-[9px] font-mono truncate text-white/80">{worker.activeTaskId || 'STANDBY'}</p>
                <p className={`text-[8px] truncate font-mono uppercase ${worker.status === 'waiting' ? 'text-amber-500' : 'text-white/30'}`}>
                  {worker.message}
                </p>
              </div>
              <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
                <div 
                  className={`h-full transition-all duration-100 ${worker.status === 'waiting' ? 'bg-amber-500' : 'bg-violet-500'}`}
                  style={{ width: `${worker.status === 'generating' ? 65 : worker.status === 'waiting' ? (worker.countdown / jitter.max) * 100 : 0}%` }}
                />
              </div>
            </GlassPanel>
          ))}
        </section>

        {/* Queue Ledger */}
        <section className="flex-1 p-6 pt-0 overflow-hidden flex flex-col gap-4">
          <GlassPanel className="flex-1 flex flex-col overflow-hidden">
            
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
                <div className="flex items-center gap-1.5">
                  <button onClick={() => setEnabledChapters(new Set(chapterList))} className="px-2 py-0.5 rounded text-[8px] font-mono font-bold bg-white/5 hover:bg-white/10 text-white/70 hover:text-white transition-colors">Select All</button>
                  <button onClick={() => setEnabledChapters(new Set())} className="px-2 py-0.5 rounded text-[8px] font-mono font-bold bg-white/5 hover:bg-white/10 text-white/40 hover:text-white transition-colors">Deselect All</button>
                  <button onClick={() => {
                    const incomplete = chapterList.filter(ch => {
                      const chTasks = batch.tasks.filter(t => (t.sceneId.match(/^([A-Za-z0-9]+)[_-]/)?.[1]?.toUpperCase() || 'OTHER') === ch);
                      return chTasks.some(t => t.status !== 'completed');
                    });
                    setEnabledChapters(new Set(incomplete));
                  }} className="px-2 py-0.5 rounded text-[8px] font-mono font-bold bg-violet-500/10 hover:bg-violet-500/20 text-violet-300 border border-violet-500/20 transition-colors">⚡ Run Incomplete Only</button>
                  <div className="h-3 w-[1px] bg-white/10 mx-1" />
                  <button onClick={() => setSelectedChapter('ALL')} className={`px-2 py-0.5 rounded text-[8px] font-mono font-bold transition-all ${selectedChapter === 'ALL' ? 'bg-violet-600 text-white shadow-sm' : 'bg-white/5 text-white/40 hover:text-white'}`}>View All ({batch.groups.length})</button>
                </div>
              </div>
              <div className="flex items-center gap-2 overflow-x-auto dark-scrollbar pb-1">
                {chapterList.map(ch => {
                  const isEnabled = enabledChapters.has(ch);
                  const isFiltered = selectedChapter === ch;
                  const chTasks = batch.tasks.filter(t => (t.sceneId.match(/^([A-Za-z0-9]+)[_-]/)?.[1]?.toUpperCase() || 'OTHER') === ch);
                  
                  // Ở chế độ Chained: chỉ tính video hoàn thành là đã xong phân cảnh
                  const completedTasks = mode === 'chained'
                    ? chTasks.filter(t => t.type === 'video' && t.status === 'completed').length
                    : chTasks.filter(t => t.status === 'completed').length;
                  
                  const totalTasks = mode === 'chained' ? Math.ceil(chTasks.length / 2) : chTasks.length;
                  
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
                      />
                      <div className="flex flex-col min-w-[70px]">
                        <div className="flex items-center justify-between gap-1.5">
                          <span className="text-[10px] font-mono font-bold text-white/90">{ch}</span>
                          <span className={`text-[8px] font-mono font-bold ${isCompleted ? 'text-emerald-400' : isRunning ? 'text-violet-400' : isEnabled ? 'text-white/40' : 'text-white/20'}`}>{completedTasks}/{totalTasks}</span>
                        </div>
                        <div className="w-full h-1 bg-white/10 rounded-full mt-1 overflow-hidden">
                          <div className={`h-full transition-all duration-300 ${isCompleted ? 'bg-emerald-400' : isRunning ? 'bg-violet-500' : 'bg-white/30'}`} style={{ width: `${percent}%` }} />
                        </div>
                      </div>
                      <span className={`text-[7px] font-mono font-bold px-1 py-0.5 rounded uppercase ${!isEnabled ? 'bg-white/5 text-white/30' : isCompleted ? 'bg-emerald-500/20 text-emerald-300' : isRunning ? 'bg-violet-500/20 text-violet-300' : 'bg-white/10 text-white/50'}`}>{!isEnabled ? 'OFF' : isCompleted ? 'DONE' : isRunning ? 'RUN' : 'WAIT'}</span>
                    </div>
                  );
                })}
              </div>
            </div>
            
            <div className="flex-1 overflow-y-auto font-mono text-[10px] dark-scrollbar">
              <table className="w-full text-left border-collapse">
                <thead className="sticky top-0 bg-[#0a0b10] z-10">
                  <tr className="border-b border-white/5">
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter w-14 text-center">#</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter">ID</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter text-center">Step 1 [IMG]</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter text-center">Step 2 [VID]</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter">Compute Slot</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter">Status</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter text-right">Reset</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredGroups.map((group, idx) => {
                    const imgTask = batch.tasks.find(t => t.sceneId === group.sceneId && t.type === 'image') || group.imageTask;
                    const vidTask = batch.tasks.find(t => t.sceneId === group.sceneId && t.type === 'video') || group.videoTask;
                    const worker = workers.find(w => w.activeTaskId && (w.activeTaskId === imgTask?.id || w.activeTaskId === vidTask?.id));
                    const groupTasks = [imgTask, vidTask].filter(Boolean) as SceneTask[];
                    const retryMax = Math.max(...groupTasks.map(t => t.retryCount), 0);
                    return (
                      <tr key={group.sceneId} className="border-b border-white/5 hover:bg-white/5 transition-colors">
                        <td className="p-4 text-center font-mono font-bold text-violet-400/60 w-14">
                          {String(idx + 1).padStart(2, '0')}
                        </td>
                        <td className="p-4 font-bold text-white/70">{group.sceneId}</td>
                        <td className="p-4 text-center">
                          {imgTask?.status === 'completed' && imgTask?.resultBase64 ? (
                            <img 
                              src={getMediaSrc(imgTask.resultBase64, imgTask.resultMimeType)} 
                              className="w-14 h-8 object-cover rounded border border-white/20 mx-auto cursor-pointer hover:scale-110 transition-transform"
                              onClick={() => setPreviewModal({ type: 'image', url: getMediaSrc(imgTask!.resultBase64, imgTask!.resultMimeType), title: group.sceneId })}
                            />
                          ) : imgTask ? getStatusBadge(imgTask.status, 'image') : <span className="text-white/5">--</span>}
                        </td>
                        <td className="p-4 text-center">
                          {vidTask?.status === 'completed' && vidTask?.resultBase64 ? (
                            <div 
                              className="relative w-14 h-8 rounded border border-white/20 overflow-hidden mx-auto cursor-pointer group hover:scale-110 transition-transform"
                              onClick={() => setPreviewModal({ type: 'video', url: getMediaSrc(vidTask!.resultBase64, vidTask!.resultMimeType), title: group.sceneId })}
                            >
                              <video src={getMediaSrc(vidTask.resultBase64, vidTask.resultMimeType)} className="w-full h-full object-cover" muted loop playsInline />
                              <div className="absolute inset-0 bg-black/30 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                                <span className="material-symbols-outlined text-[12px] text-white">play_arrow</span>
                              </div>
                            </div>
                          ) : vidTask ? getStatusBadge(vidTask.status, 'video', imgTask?.status === 'completed') : <span className="text-white/5">--</span>}
                        </td>
                        <td className="p-4">
                          {worker ? <span className="text-violet-400 font-black">ACTIVE_SLOT_{worker.id}</span> : group.status === 'completed' ? <span className="text-emerald-500/40">FINISHED</span> : <span className="text-white/10 text-[9px] uppercase">Standby</span>}
                        </td>
                        <td className="p-4">
                          <div className="flex flex-col">
                            <span className={`uppercase text-[9px] font-bold ${group.status === 'completed' ? 'text-emerald-400' : group.status === 'failed' ? 'text-rose-400' : group.status === 'processing' ? 'text-violet-400' : 'text-white/40'}`}>{group.status}</span>
                            {retryMax > 0 && <span className="text-[8px] text-white/20">RETRY {retryMax}/{SYSTEM_CONFIG.MAX_RETRIES}</span>}
                          </div>
                        </td>
                        <td className="p-4 text-right">
                          <button onClick={() => refreshScene(group.sceneId)} className="material-symbols-outlined text-white/20 hover:text-white transition-colors cursor-pointer text-base">refresh</button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </GlassPanel>

          {/* Logs */}
          <GlassPanel className="h-[140px] flex flex-col overflow-hidden">
            <div className="px-4 py-2 border-b border-white/5 bg-white/5 flex justify-between items-center">
              <span className="text-[10px] font-bold text-white/40 tracking-widest uppercase">System Telemetry Console</span>
              <button onClick={() => setLogs([])} className="text-[10px] text-white/20 hover:text-white">Clear</button>
            </div>
            <div className="flex-1 overflow-y-auto p-4 font-mono text-[10px] space-y-1 dark-scrollbar">
              {logs.length === 0 && <div className="text-white/10 italic">Waiting for telemetry data...</div>}
              {logs.map(log => (
                <div key={log.id} className="flex gap-3">
                  <span className="text-white/20">[{log.timestamp}]</span>
                  <span className={`font-bold ${log.type === 'success' ? 'text-emerald-400' : log.type === 'error' ? 'text-rose-400' : 'text-violet-400'}`}>[{log.source}]</span>
                  <span className="text-white/70">{log.message}</span>
                </div>
              ))}
            </div>
          </GlassPanel>
        </section>
      </main>

      {/* Circuit Breaker UI — SHIELD BẢO VỆ KHI BỊ FLOW CHẶN ĐỒNG LOẠT */}
      {batch.circuitBreakerActive && (
        <div className="fixed bottom-6 right-6 z-50 animate-in fade-in slide-in-from-bottom">
          <div className="bg-red-950/95 backdrop-blur-xl border border-red-500/60 text-white px-5 py-4 rounded-2xl shadow-2xl flex flex-col gap-2 min-w-[320px] max-w-[400px]">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2 font-black text-[11px] text-red-300 uppercase tracking-wider">
                <span className="material-symbols-outlined text-base text-red-400 animate-pulse">gpp_maybe</span>
                FLOW ANTI-SPAM SHIELD
              </div>
              <span className="font-mono text-[11px] font-bold text-amber-400 bg-black/40 px-2 py-0.5 rounded border border-amber-500/30">
                {batch.cooldownRemaining}s
              </span>
            </div>
            <p className="text-[10px] text-red-200/80 font-sans leading-relaxed">
              Phát hiện Flow chặn đồng loạt (10 lỗi liên tiếp). Hệ thống tạm đóng băng hàng đợi để máy chủ nhả rate-limit chống bị khóa tài khoản.
            </p>
            <div className="flex justify-end pt-1">
              <button
                onClick={handleForceResumeCircuitBreaker}
                className="px-3 py-1.5 rounded-lg bg-red-800 hover:bg-red-700 text-white text-[10px] font-mono font-bold tracking-wider transition-all border border-red-400/40 cursor-pointer shadow-md flex items-center gap-1.5"
              >
                <span className="material-symbols-outlined text-[13px]">bolt</span>
                BỎ QUA CHỜ & TIẾP TỤC
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Lightbox Modal */}
      {previewModal && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-6" onClick={() => setPreviewModal(null)}>
          <div className="bg-[#12141e] border border-white/10 rounded-2xl overflow-hidden max-w-4xl w-full flex flex-col" onClick={(e) => e.stopPropagation()}>
            <div className="p-4 border-b border-white/10 flex justify-between items-center bg-white/5">
              <span className="text-xs font-mono font-bold text-violet-300 uppercase">{previewModal.title}</span>
              <button onClick={() => setPreviewModal(null)} className="material-symbols-outlined text-white/40 hover:text-white cursor-pointer">close</button>
            </div>
            <div className="p-4 flex items-center justify-center bg-black min-h-[400px]">
              {previewModal.type === 'image' ? <img src={previewModal.url} className="max-h-[70vh] object-contain rounded-lg" /> : <video src={previewModal.url} controls autoPlay loop className="max-h-[70vh] rounded-lg" />}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
