# PROMPT VÁ LỖI TREO LUỒNG & BẢO VỆ CONCURRENCY CHO GOOGLE FLOW BATCH STUDIO
# Phiên bản: v1.6.1 (Anti-Freeze & Veo Smart Concurrency Guard)

Hãy cập nhật `App.tsx` theo các yêu cầu nâng cấp sau đây. 

⚠️ **QUY TẮC BẤT BIẾN (STRICT INVARIANTS - BẮT BUỘC TUÂN THỦ 100%):**
1. Giữ nguyên 100% giao diện ngoài: `h-screen w-screen bg-[#0a0b10]`, Sidebar `w-[340px]`, Header KPI, Grid 10-Slot Worker, Bảng Table, Lightbox Preview Modal, Chapter Control Deck.
2. Model: Giữ nguyên tuyệt đối `'Veo 3.1 - Lite [Lower Priority]'` (0 credit) và `'🍌 Nano Banana 2'`.
3. CHỈ thay thế chính xác các khối logic nội bộ sau trong `App.tsx`:

---

### VỊ TRÍ 1: BỔ SUNG CẤU HÌNH & KHÓA CONCURRENCY CHO VIDEO (Đặt ngay sau import, trước component `App`)
Thay thế hoặc khai báo object `CONFIG`:

```typescript
const CONFIG = {
  ...SYSTEM_CONFIG,
  MAX_CONCURRENT_VIDEOS: 2, // ⚠️ QUAN TRỌNG: Chỉ cho phép tối đa 2 video Veo chạy đồng thời để chống quá tải/treo luồng
  RETRY_BACKOFF_STEPS: [5, 10, 20, 30, 45],
  HARD_TIMEOUT_S: 300 // Nâng timeout lên 5 phút cho video 8s
};
```

---

### VỊ TRÍ 2: CẬP NHẬT `processQueue` (Điều phối luồng thông minh chống nghẽn Veo)
Thay thế logic chọn `nextTask` trong hàm `processQueue`:

```typescript
      // Đếm số lượng video đang thực sự được render trên các slot
      const activeVideoCount = workersRef.current.filter(w => {
        if (w.status !== 'generating' && w.status !== 'waiting') return false;
        const t = batchRef.current.tasks.find(task => task.id === w.activeTaskId);
        return t?.type === 'video';
      }).length;

      // SELECT NEXT TASK với cơ chế chống nghẽn Veo
      const nextTask = batchRef.current.tasks.find(t => {
        if (t.status !== 'idle' && t.status !== 'pending') return false;
        if (activeTaskIdsRef.current.has(t.id)) return false; 
        if (t.retryCount >= SYSTEM_CONFIG.MAX_RETRIES) return false;
        
        // BỘ LỌC CHƯƠNG: Chỉ bốc task thuộc các chương đang được tick chọn
        const match = t.sceneId.match(/^([A-Za-z0-9]+)[_-]/);
        const ch = match ? match[1].toUpperCase() : 'OTHER';
        if (enabledChaptersRef.current.size > 0 && !enabledChaptersRef.current.has(ch)) {
          return false;
        }

        // BẢO VỆ VEO: Nếu đang có 2 video chạy rồi, tạm thời không bốc thêm video, nhường slot cho sinh Ảnh
        if (t.type === 'video' && activeVideoCount >= CONFIG.MAX_CONCURRENT_VIDEOS) {
          return false;
        }

        if (mode === 'chained' && t.type === 'video') {
          const imgTask = batchRef.current.tasks.find(it => it.sceneId === t.sceneId && it.type === 'image');
          return imgTask?.status === 'completed';
        }
        return true;
      });
```

---

### VỊ TRÍ 3: THAY THẾ TOÀN BỘ `executeTaskOnWorker` (Làm sạch Base64 & Vá triệt để lỗi TypeError crash)
Thay thế toàn bộ hàm `executeTaskOnWorker` bằng code bất tử chống treo luồng sau:

```typescript
  const executeTaskOnWorker = async (workerIdx: number, task: SceneTask) => {
    const waitTime = Math.floor(Math.random() * (jitter.max - jitter.min + 1) + jitter.min);
    const targetLaunchTime = Date.now() + (waitTime * 1000);
    updateWorkerSync(workerIdx, { 
      status: 'waiting', activeTaskId: task.id, message: `Stagger: ${waitTime}s`, countdown: waitTime 
    });
    
    // Vòng lặp đếm lùi an toàn thời gian thực
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

    updateTask(task.id, { status: 'processing', startedAt: Date.now() });
    updateWorkerSync(workerIdx, { 
      status: 'generating', message: `Generating ${task.type}...`, progress: 15, countdown: 0 
    });

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
              const cleanBase64 = asset.base64.includes(',') ? asset.base64.split(',')[1] : asset.base64;
              const uploaded = await Flow.upload({ 
                base64: cleanBase64, 
                mimeType: asset.mimeType as any, 
                name: cleanRef 
              });
              referenceImageMediaIds = [uploaded.mediaId];
            }
            return Flow.generate.image({
              prompt: cleanPrompt,
              modelDisplayName: imageModel,
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
                // ⚠️ BẮT BUỘC: Làm sạch tiền tố data:... trước khi upload
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

      const timeoutPromise = new Promise((_, reject) => 
        setTimeout(() => reject(new Error('TIMEOUT_LIMIT_REACHED')), (CONFIG.HARD_TIMEOUT_S || 300) * 1000)
      );

      const result = await Promise.race([generationPromise, timeoutPromise]) as { base64: string, mimeType: string, mediaId?: string };
      
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
      updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Done', countdown: 0 });
      addLog('WORKER', `Slot ${workerIdx + 1} completed ${task.sceneId} (${task.type.toUpperCase()})`, 'success');
    } catch (err: any) {
      const errMsg = err?.message || 'Unknown error';
      console.error(`Task ${task.id} failed:`, errMsg);

      // Giải phóng khóa tác vụ ngay lập tức
      activeTaskIdsRef.current.delete(task.id);

      // Xử lý lỗi thiếu file tham chiếu
      if (errMsg.includes('MISSING_REF_ASSET')) {
        updateTask(task.id, { status: 'failed', error: 'Missing Asset' });
        addLog('ASSET', `Halted ${task.sceneId}: Missing @${task.referenceFile}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Missing Asset', countdown: 0 });
        return;
      } 
      
      // Xử lý kiểm duyệt Safety Block
      if (errMsg.includes('SAFETY') || errMsg.includes('BLOCK')) {
        updateTask(task.id, { status: 'blocked', error: 'Safety Block' });
        addLog('WORKER', `Safety block on ${task.sceneId}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Safety Block', countdown: 0 });
        return;
      }

      // Xử lý lỗi Quota / Rate Limit 429: Tự động kích hoạt Cầu Dao Nghỉ 60s
      if (errMsg.includes('429') || errMsg.includes('QUOTA') || errMsg.includes('EXHAUSTED')) {
        addLog('CIRCUIT', `Rate limit hit on ${task.sceneId}. Cooling down for 60s...`, 'warning');
        setBatch(prev => ({ ...prev, circuitBreakerActive: true, cooldownRemaining: 60 }));
        setTimeout(() => {
          setBatch(prev => ({ ...prev, circuitBreakerActive: false }));
        }, 60000);
      }

      // Tự động Retry an toàn 100% (Có fallback backoff, không bao giờ bị TypeError crash)
      const nextRetry = (task.retryCount || 0) + 1;
      const backoffList = CONFIG.RETRY_BACKOFF_STEPS || [5, 10, 20, 30, 60];
      const backoff = backoffList[nextRetry - 1] || 15;

      if (nextRetry <= SYSTEM_CONFIG.MAX_RETRIES) {
        updateTask(task.id, { status: 'retrying', retryCount: nextRetry, error: errMsg });
        addLog('WORKER', `Retrying ${task.sceneId} (${nextRetry}/${SYSTEM_CONFIG.MAX_RETRIES}) in ${backoff}s`, 'warning');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 });
        
        setTimeout(() => {
          updateTask(task.id, { status: 'idle' });
          if (batchRef.current.isProcessing && !batchRef.current.isPaused) {
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
```
