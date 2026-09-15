# BẢN VÁ TOÀN DIỆN SỐ 15: CƠ CHẾ TỰ CỨU TẬN GỐC - TRIỆT TIÊU KẸT VIDEO CUỐI CÙNG & AUTO-REAPER
# Phiên bản: v1.6.7 (Definitive Auto-Recovery & Zero-Stall Engine)

⚠️ **BẢNG KHÓA TÍNH NĂNG BẤT BIẾN (STRICT INVARIANTS):**
- **GIỮ NGUYÊN 100%** Asset Bin, tag `@tên_ảnh`, Chapter Controller, STT `#`, Preview Lightbox, Nạp nhiều file .txt, Xuất ZIP.
- **CỐ ĐỊNH MODEL VIDEO:** Luôn luôn là `'Veo 3.1 - Lite [Lower Priority]'` miễn phí.
- **BẢO LƯU ẢNH 100%:** Khi video bị lỗi/treo, tuyệt đối không tạo lại ảnh, lấy luôn ảnh cũ làm khung hình đầu!

---

### PHÉP SỬA 1: CẬP NHẬT `CONFIG` (RÚT NGẮN WATCHDOG XUỐNG 7 PHÚT ĐỂ PHẢN ỨNG NHANH)
* **Vấn đề:** Để 10 phút (600s) là quá dài khiến người dùng chờ sốt ruột. Thực tế nếu Veo 3.1 quá 7 phút (420s) không xong thì 99% socket đã bị ngắt.

**TÌM ĐOẠN:**
```typescript
// ======================================================================
// CONFIGURATION & CONCURRENCY GUARD - PATCH v1.6.6
// ======================================================================
const CONFIG = {
  ...SYSTEM_CONFIG,
  MAX_CONCURRENT_VIDEOS: 2, // Giữ 2 video đồng thời để không bị Google phạt rate-limit
  RETRY_BACKOFF_STEPS: [5, 10, 20, 30, 45],
  VIDEO_WATCHDOG_S: 600, // 10 phút an toàn: Nếu Veo 3.1 kẹt quá 10m -> Tự động hủy và đẩy xuống cuối queue
  IMAGE_WATCHDOG_S: 90,   // 90s an toàn: Nếu tạo ảnh kẹt -> Tự động fallback sang model ảnh khác
  IMAGE_FALLBACK_MODELS: ['🍌 Nano Banana 2', '🍌 Nano Banana Pro', '🍌 Nano Banana 2 Lite'], // Danh sách model dự phòng khả dụng
  MAX_VEO_DEMOTE_RETRIES: 3 // Tối đa 3 lần dồn video xuống cuối hàng đợi
};
```

**THAY BẰNG:**
```typescript
// ======================================================================
// CONFIGURATION & CONCURRENCY GUARD - PATCH v1.6.7
// ======================================================================
const CONFIG = {
  ...SYSTEM_CONFIG,
  MAX_CONCURRENT_VIDEOS: 2, // Giữ 2 video đồng thời chống nghẽn
  RETRY_BACKOFF_STEPS: [5, 10, 20, 30, 45],
  VIDEO_WATCHDOG_S: 420, // 7 phút chuẩn xác: Quá 7m là Veo đã đứt socket -> Ngắt và dồn cuối queue ngay
  IMAGE_WATCHDOG_S: 90,   // 90s cho tạo ảnh
  IMAGE_FALLBACK_MODELS: ['🍌 Nano Banana 2', '🍌 Nano Banana Pro', '🍌 Nano Banana 2 Lite'],
  MAX_VEO_DEMOTE_RETRIES: 3 // Tối đa 3 vòng dồn video về cuối queue
};
```

---

### PHÉP SỬA 2: BỔ SUNG AUTO-REAPER (TỰ CỨU TÁC VỤ MỒ CÔI) & KHÓA CHỐNG TRÙNG TASK TRONG `processQueue`
* **Vấn đề cốt lõi:** Các cảnh bị kẹt cờ `PROCESSING / STANDBY` là do worker đã nhả nhưng task vẫn mang status `processing`, khiến vòng lặp bỏ qua vĩnh viễn!
* **Cách khắc phục:** 
  1. Thêm bộ quét **Auto-Reaper** ở đầu mỗi vòng lặp: Task nào `processing` mà không có worker nào ôm $\to$ lập tức trả về `idle` để worker bốc lại ngay!
  2. Khóa ngay `activeTaskIdsRef.add(nextTask.id)` TRƯỚC độ trễ 1500ms để triệt tiêu 100% việc 2 Slot cùng bốc trùng 1 task.

**TÌM TOÀN BỘ HÀM `processQueue`:**
```typescript
  const processQueue = async () => {
    if (processingRef.current) return;
    processingRef.current = true;
    
    while (batchRef.current.isProcessing && !batchRef.current.isPaused) {
      if (batchRef.current.circuitBreakerActive) {
        await new Promise(r => setTimeout(r, 1000));
        continue;
      }
      const availableWorkerIndex = workersRef.current.findIndex((w, i) => i < workersCount && w.status === 'idle');
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
        const now = Date.now();
        const diff = now - lastDispatchRef.current;
        if (diff < 1500) await new Promise(r => setTimeout(r, 1500 - diff));
        lastDispatchRef.current = Date.now();
        activeTaskIdsRef.current.add(nextTask.id);
        addLog('WORKER', `Slot ${availableWorkerIndex + 1} claimed ${nextTask.sceneId} (${nextTask.type.toUpperCase()})`, 'info');
        updateWorkerSync(availableWorkerIndex, { status: 'waiting', activeTaskId: nextTask.id });
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
```

**THAY BẰNG TOÀN BỘ HÀM `processQueue` MỚI:**
```typescript
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

      const availableWorkerIndex = workersRef.current.findIndex((w, i) => i < workersCount && w.status === 'idle');
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
```

---

### PHÉP SỬA 3: DỒN QUEUE TOÀN DIỆN KHI VIDEO GẶP BẤT KỲ LỖI NÀO (Trong `executeTaskOnWorker`)
* **Vấn đề:** Trước đây chỉ dồn queue khi gặp đúng chuỗi `VEO_WATCHDOG_TIMEOUT`. Nếu Veo bị lỗi mạng, lỗi máy chủ, hoặc lỗi API của Google $\to$ nó bị kẹt lại không dồn.
* **Cách sửa:** **Bất kể Video gặp lỗi gì**: Bảo lưu ảnh 100%, đồng bộ cả `tasks` lẫn `groups`, và dồn video về đuôi queue để các cảnh sau chạy trước!

**TÌM KHỐI `catch` TRONG `executeTaskOnWorker`:**
```typescript
    } catch (err: any) {
      clearTimeout(watchdogTimer);
      const errMsg = err?.message || 'Unknown error';
      console.error(`Task ${task.id} failed:`, errMsg);
      activeTaskIdsRef.current.delete(task.id);
      // --- FALLBACK MODEL ẢNH ---
      if (task.type === 'image') {
        const currentAssigned = (task as any).assignedModel || imageModel;
        const currentIdx = CONFIG.IMAGE_FALLBACK_MODELS.indexOf(currentAssigned);
        const nextModel = (currentIdx !== -1 && currentIdx < CONFIG.IMAGE_FALLBACK_MODELS.length - 1)
          ? CONFIG.IMAGE_FALLBACK_MODELS[currentIdx + 1]
          : null;
        if (nextModel) {
          (task as any).assignedModel = nextModel;
          addLog('FALLBACK', `Ảnh ${task.sceneId} lỗi/treo -> Thử lại với [${nextModel}]`, 'warning');
          updateTask(task.id, { status: 'idle', error: `Fallback: ${nextModel}` });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Model Fallback', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        }
      }
      // --- DỒN QUEUE VIDEO NẾU TREO ---
      if (task.type === 'video' && errMsg.includes('VEO_WATCHDOG_TIMEOUT')) {
        const currentRetries = (task.retryCount || 0) + 1;
        if (currentRetries <= CONFIG.MAX_VEO_DEMOTE_RETRIES) {
          addLog('WATCHDOG', `Cảnh ${task.sceneId} treo >10m -> Đã bảo lưu ảnh, dồn video về cuối queue (${currentRetries}/${CONFIG.MAX_VEO_DEMOTE_RETRIES})`, 'warning');
          const allTasks = [...batchRef.current.tasks];
          const taskIdx = allTasks.findIndex(t => t.id === task.id);
          if (taskIdx !== -1) {
            const [demotedTask] = allTasks.splice(taskIdx, 1);
            demotedTask.status = 'idle';
            demotedTask.retryCount = currentRetries;
            demotedTask.error = 'Stalled (Moved to tail)';
            allTasks.push(demotedTask);
            batchRef.current = { ...batchRef.current, tasks: allTasks };
            setBatch(batchRef.current);
          }
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Standby', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        } else {
          addLog('WORKER', `Cảnh ${task.sceneId} thất bại vĩnh viễn do treo máy chủ liên tục`, 'error');
          updateTask(task.id, { status: 'failed', error: 'Veo Backend Hung (3x)' });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Task Failed', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        }
      }
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
```

**THAY BẰNG KHỐI `catch` MỚI (TỰ PHỤC HỒI TOÀN DIỆN):**
```typescript
    } catch (err: any) {
      clearTimeout(watchdogTimer);
      const errMsg = err?.message || 'Unknown error';
      console.error(`Task ${task.id} failed:`, errMsg);
      activeTaskIdsRef.current.delete(task.id);

      // --- TRƯỜNG HỢP 1: TẠO ẢNH LỖI HOẶC TREO -> FALLBACK MODEL ---
      if (task.type === 'image') {
        const currentAssigned = (task as any).assignedModel || imageModel;
        const currentIdx = CONFIG.IMAGE_FALLBACK_MODELS.indexOf(currentAssigned);
        const nextModel = (currentIdx !== -1 && currentIdx < CONFIG.IMAGE_FALLBACK_MODELS.length - 1)
          ? CONFIG.IMAGE_FALLBACK_MODELS[currentIdx + 1]
          : null;
        if (nextModel) {
          (task as any).assignedModel = nextModel;
          addLog('FALLBACK', `Ảnh ${task.sceneId} lỗi [${errMsg.substring(0, 25)}] -> Thử lại với [${nextModel}]`, 'warning');
          updateTask(task.id, { status: 'idle', error: `Fallback: ${nextModel}` });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Model Fallback', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        }
      }

      // --- TRƯỜNG HỢP 2: TẠO VIDEO GẶP BẤT KỲ LỖI NÀO (TREO >7M HOẶC LỖI SERVER) ---
      if (task.type === 'video') {
        const currentRetries = (task.retryCount || 0) + 1;
        if (currentRetries <= CONFIG.MAX_VEO_DEMOTE_RETRIES) {
          addLog('WATCHDOG', `Cảnh ${task.sceneId} gặp lỗi/treo -> Bảo lưu ảnh, dồn video về cuối queue (${currentRetries}/${CONFIG.MAX_VEO_DEMOTE_RETRIES})`, 'warning');
          
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
          setTimeout(processQueue, 200);
          return;
        } else {
          addLog('WORKER', `Cảnh ${task.sceneId} thất bại vĩnh viễn sau ${CONFIG.MAX_VEO_DEMOTE_RETRIES} lần dồn queue`, 'error');
          updateTask(task.id, { status: 'failed', error: errMsg });
          updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Task Failed', countdown: 0 });
          setTimeout(processQueue, 200);
          return;
        }
      }

      // Xử lý lỗi thiếu ảnh gốc
      if (errMsg.includes('MISSING_REF_ASSET')) {
        updateTask(task.id, { status: 'failed', error: 'Missing Asset' });
        addLog('ASSET', `Halted ${task.sceneId}: Missing @${task.referenceFile}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Missing Asset', countdown: 0 });
        return;
      } 
      
      // Xử lý Rate Limit 429
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

      // Mặc định cho các task ảnh hết lượt fallback
      updateTask(task.id, { status: 'failed', error: errMsg });
      updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Task Failed', countdown: 0 });
      setTimeout(processQueue, 200);
    }
```

---

### PHÉP SỬA 4: NÂNG CẤP HÀM `retryAllFailed` (QUÉT SẠCH MỌI TASK KẸT)
* **Vấn đề:** Hàm cũ chỉ reset `failed` và `blocked`, bỏ qua các task bị kẹt `processing`.
* **Cách sửa:** Quét và đưa toàn bộ task chưa hoàn thành (kể cả kẹt `processing` hay `retrying`) về `idle`, reset worker và khởi động lại ngay!

**TÌM TOÀN BỘ HÀM `retryAllFailed`:**
```typescript
  const retryAllFailed = () => {
    setBatch(prev => {
      const newTasks = prev.tasks.map(t => 
        (t.status === 'failed' || t.status === 'blocked') ? { ...t, status: 'idle' as const, progress: 0, retryCount: 0 } : t
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
      return { ...prev, tasks: newTasks, groups: newGroups, isProcessing: true, isPaused: false };
    });
    setWorkers(prev => prev.map(w => 
      w.message === 'Task Error' || w.message === 'Missing Asset' || w.message === 'Safety Block' ? { ...w, status: 'idle', message: 'Standby', activeTaskId: null } : w
    ));
    addLog('QUEUE', 'Production auto-resumed: Failed/Blocked tasks reset', 'warning');
    setTimeout(processQueue, 150);
  };
```

**THAY BẰNG:**
```typescript
  const retryAllFailed = () => {
    activeTaskIdsRef.current.clear();
    setBatch(prev => {
      const newTasks = prev.tasks.map(t => 
        (t.status !== 'completed') ? { ...t, status: 'idle' as const, progress: 0, retryCount: 0 } : t
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
      return { ...prev, tasks: newTasks, groups: newGroups, isProcessing: true, isPaused: false };
    });
    setWorkers(prev => prev.map(w => ({ ...w, status: 'idle', message: 'Standby', activeTaskId: null, countdown: 0 })));
    addLog('QUEUE', 'Toàn bộ các tác vụ chưa hoàn thành đã được reset về IDLE và kích hoạt lại!', 'warning');
    setTimeout(processQueue, 150);
  };
```
