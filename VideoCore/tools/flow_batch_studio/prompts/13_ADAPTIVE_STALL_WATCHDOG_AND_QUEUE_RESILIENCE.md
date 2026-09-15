# BẢN VÁ KIẾN TRÚC SỐ 13: CHỐNG TREO TỰ ĐỘNG - BẢO LƯU ẢNH - ĐẨY VIDEO XUỐNG CUỐI QUEUE - FALLBACK MODEL ẢNH
# Phiên bản: v1.6.5 (Adaptive Stall Watchdog & Queue Resilience)

⚠️ **BẢNG KHÓA TÍNH NĂNG BẤT BIẾN (STRICT INVARIANTS - BẢO VỆ 100% TÍNH NĂNG CỐT LÕI):**
1. **GIỮ NGUYÊN 100%** Tính năng Ảnh tham chiếu (Asset Bin & tag `@tên_ảnh`): Không xóa, không sửa cấu trúc.
2. **GIỮ NGUYÊN 100%** Bàn điều khiển Quản lý theo Chương (Chapter Control Deck & các nút chọn `[✓]` từng chương).
3. **GIỮ NGUYÊN 100%** Giao diện JSX (Sidebar, Table, Modal xem trước Lightbox, Nạp nhiều file .txt, Xuất ZIP).
4. **CỐ ĐỊNH MODEL VIDEO:** Luôn luôn giữ model video mặc định miễn phí `'Veo 3.1 - Lite [Lower Priority]'`. Tuyệt đối không tự ý nhảy sang model trả phí.
5. **BẢO TỒN TÀI NGUYÊN 100%:** Khi video bị treo, **TUYỆT ĐỐI KHÔNG XÓA ẢNH**. Ảnh đã tạo xong ở Bước 1 phải được giữ nguyên 100% để tái sử dụng làm khung hình đầu (`firstFrameImageMediaId`) cho video khi chạy lại!

---

### PHÉP SỬA 1: CẬP NHẬT HẰNG SỐ CẤU HÌNH `CONFIG`
* **Mục đích:** Khai báo ngưỡng an toàn cho Video (10 phút = 600s), Ảnh (90s), danh sách Model tạo ảnh dự phòng và số lần tối đa đẩy video xuống cuối hàng đợi.

**TÌM ĐOẠN:**
```typescript
// ======================================================================
// CONFIGURATION & CONCURRENCY GUARD
// ======================================================================
const CONFIG = {
  ...SYSTEM_CONFIG,
  MAX_CONCURRENT_VIDEOS: 2, // Only allow 2 concurrent video tasks to prevent freezing
  RETRY_BACKOFF_STEPS: [5, 10, 20, 30, 45],
  HARD_TIMEOUT_S: 300 // Used only for error logging, logic removed per patch
};
```

**THAY BẰNG:**
```typescript
// ======================================================================
// CONFIGURATION & CONCURRENCY GUARD
// ======================================================================
const CONFIG = {
  ...SYSTEM_CONFIG,
  MAX_CONCURRENT_VIDEOS: 2, // Giữ 2 video đồng thời để không bị Google phạt rate-limit
  RETRY_BACKOFF_STEPS: [5, 10, 20, 30, 45],
  VIDEO_WATCHDOG_S: 600, // 10 phút an toàn: Nếu Veo 3.1 kẹt quá 10m -> Tự động hủy và đẩy xuống cuối queue
  IMAGE_WATCHDOG_S: 90,   // 90s an toàn: Nếu tạo ảnh kẹt -> Tự động fallback sang model ảnh khác
  IMAGE_FALLBACK_MODELS: ['🍌 Nano Banana 2', 'Nano Banana Pro', 'Imagen 3'], // Chuỗi model ảnh dự phòng
  MAX_VEO_DEMOTE_RETRIES: 3 // Tối đa 3 lần dồn video xuống cuối hàng đợi
};
```

---

### PHÉP SỬA 2: NÂNG CẤP HÀM `executeTaskOnWorker` (CHỐNG TREO, BẢO LƯU ẢNH, DỒN QUEUE & FALLBACK MODEL)
* **Mục đích:**
  1. Thêm Watchdog an toàn (không bao giờ để Promise của Google treo vô tận làm tê liệt worker).
  2. Ở bước **TẠO ẢNH**: Nếu model hiện tại lỗi/treo, tự động chuyển sang model ảnh tiếp theo trong `IMAGE_FALLBACK_MODELS` để sinh lại ảnh ngay, cứu sống chuỗi `chained`.
  3. Ở bước **TẠO VIDEO**: Nếu bị treo >10 phút (`VEO_WATCHDOG_TIMEOUT`), ngắt luồng chờ ngay, **giữ nguyên 100% ảnh đã tạo**, đẩy riêng task video xuống cuối hàng đợi (`batch.tasks`), giải phóng Slot để chạy tiếp các cảnh sau!

**TÌM TOÀN BỘ HÀM `executeTaskOnWorker`:**
```typescript
  const executeTaskOnWorker = async (workerIdx: number, task: SceneTask) => {
    // PHÉP SỬA 2: KHỞI ĐỘNG TRỰC TIẾP - Bỏ vòng lặp đếm lùi jitter làm chậm tiến độ
    updateTask(task.id, { status: 'processing', startedAt: Date.now() });
    updateWorkerSync(workerIdx, { 
      status: 'generating', activeTaskId: task.id, message: `Generating ${task.type}...`, progress: 15, countdown: 0 
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
              
              // PHÉP SỬA 3: Tái sử dụng mediaId nếu đã upload trước đó trong session
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
      // PHÉP SỬA 1: CHỜ TỰ NHIÊN - Không áp đặt timeout giả tạo để tránh hỏng video render lâu
      const result = await generationPromise as { base64: string, mimeType: string, mediaId?: string };
      
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
      activeTaskIdsRef.current.delete(task.id);
      if (errMsg.includes('MISSING_REF_ASSET')) {
        updateTask(task.id, { status: 'failed', error: 'Missing Asset' });
        addLog('ASSET', `Halted ${task.sceneId}: Missing @${task.referenceFile}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Missing Asset', countdown: 0 });
        return;
      } 
      
      if (errMsg.includes('SAFETY') || errMsg.includes('BLOCK')) {
        updateTask(task.id, { status: 'blocked', error: 'Safety Block' });
        addLog('WORKER', `Safety block on ${task.sceneId}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Safety Block', countdown: 0 });
        return;
      }
      if (errMsg.includes('429') || errMsg.includes('QUOTA') || errMsg.includes('EXHAUSTED')) {
        addLog('CIRCUIT', `Rate limit hit on ${task.sceneId}. Cooling down for 60s...`, 'warning');
        setBatch(prev => ({ ...prev, circuitBreakerActive: true, cooldownRemaining: 60 }));
        const countdownInterval = setInterval(() => {
          setBatch(prev => {
            if (prev.cooldownRemaining <= 1) {
              clearInterval(countdownInterval);
              return { ...prev, circuitBreakerActive: false, cooldownRemaining: 0 };
            }
            return { ...prev, cooldownRemaining: prev.cooldownRemaining - 1 };
          });
        }, 1000);
      }
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

**THAY BẰNG TOÀN BỘ HÀM MỚI:**
```typescript
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

            // Tự động sử dụng model được fallback (nếu có), mặc định dùng imageModel
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
              // TẬN DỤNG LẠI ẢNH ĐÃ TẠO XONG: Đọc trực tiếp resultMediaId từ imageTask
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

            // LUÔN CỐ ĐỊNH MODEL VIDEO ĐÃ CHỌN (Veo 3.1 - Lite miễn phí)
            return Flow.generate.video({
              prompt: cleanPrompt,
              modelDisplayName: videoModel,
              aspectRatio: aspectRatio as any,
              firstFrameImageMediaId,
              durationSeconds: parseInt(duration) as any
            });
          })();

      // WATCHDOG THÔNG MINH: 10 phút cho Video Veo, 90s cho Ảnh
      const timeoutLimitS = task.type === 'video' ? (CONFIG.VIDEO_WATCHDOG_S || 600) : (CONFIG.IMAGE_WATCHDOG_S || 90);
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
      updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Done', countdown: 0 });
      addLog('WORKER', `Slot ${workerIdx + 1} completed ${task.sceneId} (${task.type.toUpperCase()})`, 'success');

    } catch (err: any) {
      clearTimeout(watchdogTimer);
      const errMsg = err?.message || 'Unknown error';
      console.error(`Task ${task.id} failed:`, errMsg);
      activeTaskIdsRef.current.delete(task.id);

      // --- TRƯỜNG HỢP 1: BƯỚC TẠO ẢNH BỊ LỖI HOẶC TREO -> TỰ ĐỘNG FALLBACK SANG MODEL KHÁC ---
      if (task.type === 'image') {
        const currentAssigned = (task as any).assignedModel || imageModel;
        const currentIdx = CONFIG.IMAGE_FALLBACK_MODELS.indexOf(currentAssigned);
        const nextModel = (currentIdx !== -1 && currentIdx < CONFIG.IMAGE_FALLBACK_MODELS.length - 1)
          ? CONFIG.IMAGE_FALLBACK_MODELS[currentIdx + 1]
          : null;

        if (nextModel) {
          (task as any).assignedModel = nextModel;
          addLog('FALLBACK', `Ảnh ${task.sceneId} lỗi với [${currentAssigned}] -> Tự động chuyển sang model [${nextModel}]`, 'warning');
          updateTask(task.id, { status: 'idle', error: `Fallback: ${nextModel}` });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Model Fallback', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        }
      }

      // --- TRƯỜNG HỢP 2: BƯỚC TẠO VIDEO BỊ TREO >10 PHÚT -> BẢO LƯU ẢNH & ĐẨY VIDEO XUỐNG CUỐI QUEUE ---
      if (task.type === 'video' && errMsg.includes('VEO_WATCHDOG_TIMEOUT')) {
        const currentRetries = (task.retryCount || 0) + 1;
        if (currentRetries <= (CONFIG.MAX_VEO_DEMOTE_RETRIES || 3)) {
          addLog('WATCHDOG', `Cảnh ${task.sceneId} bị Veo treo >10m -> Đã bảo lưu ảnh, đẩy video xuống cuối queue (Thử lại ${currentRetries}/${CONFIG.MAX_VEO_DEMOTE_RETRIES})`, 'warning');

          // Cắt task này khỏi vị trí hiện tại và nhét xuống cuối cùng của mảng tasks
          const allTasks = [...batchRef.current.tasks];
          const taskIdx = allTasks.findIndex(t => t.id === task.id);
          if (taskIdx !== -1) {
            const [demotedTask] = allTasks.splice(taskIdx, 1);
            demotedTask.status = 'idle';
            demotedTask.retryCount = currentRetries;
            demotedTask.error = 'Stalled (Moved to back)';
            allTasks.push(demotedTask);

            // Cập nhật state không làm mất ảnh của các group
            batchRef.current = { ...batchRef.current, tasks: allTasks };
            setBatch(batchRef.current);
          }

          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        } else {
          addLog('WORKER', `Cảnh ${task.sceneId} thất bại vĩnh viễn do máy chủ Veo liên tục treo`, 'error');
          updateTask(task.id, { status: 'failed', error: 'Veo Backend Hung (3x)' });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Task Failed', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        }
      }

      // --- CÁC TRƯỜNG HỢP LỖI CỤ THỂ KHÁC ---
      if (errMsg.includes('MISSING_REF_ASSET')) {
        updateTask(task.id, { status: 'failed', error: 'Missing Asset' });
        addLog('ASSET', `Halted ${task.sceneId}: Missing @${task.referenceFile}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Missing Asset', countdown: 0 });
        return;
      } 
      
      if (errMsg.includes('SAFETY') || errMsg.includes('BLOCK')) {
        updateTask(task.id, { status: 'blocked', error: 'Safety Block' });
        addLog('WORKER', `Safety block on ${task.sceneId}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Safety Block', countdown: 0 });
        return;
      }

      if (errMsg.includes('429') || errMsg.includes('QUOTA') || errMsg.includes('EXHAUSTED')) {
        addLog('CIRCUIT', `Rate limit hit on ${task.sceneId}. Cooling down for 60s...`, 'warning');
        setBatch(prev => ({ ...prev, circuitBreakerActive: true, cooldownRemaining: 60 }));
        const countdownInterval = setInterval(() => {
          setBatch(prev => {
            if (prev.cooldownRemaining <= 1) {
              clearInterval(countdownInterval);
              return { ...prev, circuitBreakerActive: false, cooldownRemaining: 0 };
            }
            return { ...prev, cooldownRemaining: prev.cooldownRemaining - 1 };
          });
        }, 1000);
      }

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

---

### PHÉP SỬA 3: BỔ SUNG HÀM CỨU NGUY KHẨN CẤP `handleForceSkipWorker` (SKIP BẰNG TAY 1-CLICK)
* **Mục đích:** Thêm hàm xử lý khi người dùng bấm nút ❌ trên thẻ Slot để giải phóng slot ngay lập tức nếu mắt thường nhìn thấy video đã bị treo quá lâu.

**CHÈN HÀM NÀY NGAY TRƯỚC HÀM `toggleProcessing`:**
```typescript
  // --- BỔ SUNG: NÚT CỨU NGUY KHẨN CẤP THỦ CÔNG TRÊN TỪNG SLOT ---
  const handleForceSkipWorker = (workerIdx: number) => {
    const worker = workersRef.current[workerIdx];
    if (!worker?.activeTaskId) return;
    const taskId = worker.activeTaskId;
    const task = batchRef.current.tasks.find(t => t.id === taskId);
    activeTaskIdsRef.current.delete(taskId);

    if (task) {
      if (task.type === 'video') {
        // Bảo lưu ảnh, đẩy video xuống cuối hàng đợi
        const allTasks = [...batchRef.current.tasks];
        const taskIdx = allTasks.findIndex(t => t.id === taskId);
        if (taskIdx !== -1) {
          const [demotedTask] = allTasks.splice(taskIdx, 1);
          demotedTask.status = 'idle';
          demotedTask.retryCount = (demotedTask.retryCount || 0) + 1;
          demotedTask.error = 'Manually Skipped to Tail';
          allTasks.push(demotedTask);
          batchRef.current = { ...batchRef.current, tasks: allTasks };
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
```

---

### PHÉP SỬA 4: THÊM NÚT "FORCE SKIP" TRỰC QUAN TRÊN THẺ SLOT WORKER
* **Mục đích:** Hiển thị một nút icon `close` (❌) nhỏ ngay cạnh nhãn trạng thái của Slot khi worker đang chạy, cho phép bấm ngắt bất cứ lúc nào.

**TÌM ĐOẠN (Trong phần `Compute Slots Matrix`):**
```tsx
              <div className="flex justify-between items-start">
                <span className="text-[8px] font-mono text-white/40 tracking-[1px]">SLOT-{worker.id}</span>
                <span className={`text-[7px] px-1.5 py-0.5 rounded font-bold ${
                  worker.status === 'generating' ? 'bg-violet-600 text-white animate-pulse' : 
                  worker.status === 'waiting' ? 'bg-amber-600 text-black' : 'bg-white/10 text-white/40'
                }`}>
                  {worker.status.toUpperCase()}
                </span>
              </div>
```

**THAY BẰNG:**
```tsx
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
```
