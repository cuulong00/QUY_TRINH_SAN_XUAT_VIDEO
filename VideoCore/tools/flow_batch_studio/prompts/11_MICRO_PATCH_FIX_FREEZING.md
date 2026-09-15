# LỆNH PHẪU THUẬT CHÍNH XÁC: VÁ LỖI TREO LUỒNG - KHÓA BẢO VỆ 100% TÍNH NĂNG
# Phiên bản: v1.6.3 (Strict Search & Replace Anchor)

🛑 **BẢNG KHÓA BẤT BIẾN NGHIÊM NGẶT (STRICT INVARIANTS - CẤM CHẠM VÀO):**
1. **CẤM SỬA BẤT KỲ DÒNG NÀO TRONG PHẦN JSX RENDER (toàn bộ khối `return (...)`):** Giữ nguyên 100% Chapter Control Deck, Grid 10 Worker, Sidebar `w-[340px]`, Header, Table, Modal.
2. **CẤM SỬA CÁC MODEL STRING:** Giữ nguyên tuyệt đối `'Veo 3.1 - Lite [Lower Priority]'` và `'🍌 Nano Banana 2'`.
3. **CẤM SỬA HAY XÓA CÁC HÀM:** Giữ nguyên 100% `startSilentAudio`, `stopSilentAudio`, `updateWorkerSync`, `handleTxtUpload`, `downloadAllAsZip`, `clearQueue`, `retryAllFailed`, `refreshScene`.
4. **CẤM THAY ĐỔI CƠ CHẾ:** Giữ nguyên `downloadedTaskIdsRef`, `enabledChaptersRef`, `lastDispatchRef`, và vòng lặp thời gian thực `Date.now() < targetLaunchTime`.

👉 **HÃY ÁP DỤNG ĐÚNG 3 PHÉP THAY THẾ CỤC BỘ (SEARCH & REPLACE) SAU TRONG `App.tsx`:**

---

### PHÉP THAY THẾ 1 (Trong hàm `processQueue` - Khóa tối đa 2 video Veo cùng lúc để chống quá tải):
**TÌM ĐOẠN:**
```typescript
        // BỘ LỌC CHƯƠNG: Chỉ bốc task thuộc các chương đang được tick chọn
        const match = t.sceneId.match(/^([A-Za-z0-9]+)[_-]/);
        const ch = match ? match[1].toUpperCase() : 'OTHER';
        if (enabledChaptersRef.current.size > 0 && !enabledChaptersRef.current.has(ch)) {
          return false;
        }
        if (mode === 'chained' && t.type === 'video') {
```

**THAY BẰNG:**
```typescript
        // BỘ LỌC CHƯƠNG: Chỉ bốc task thuộc các chương đang được tick chọn
        const match = t.sceneId.match(/^([A-Za-z0-9]+)[_-]/);
        const ch = match ? match[1].toUpperCase() : 'OTHER';
        if (enabledChaptersRef.current.size > 0 && !enabledChaptersRef.current.has(ch)) {
          return false;
        }

        // KHÓA VEO CONCURRENCY: Tối đa 2 video Veo chạy đồng thời để chống nghẽn server
        if (t.type === 'video') {
          const activeVideos = workersRef.current.filter(w => (w.status === 'generating' || w.status === 'waiting') && batchRef.current.tasks.find(tk => tk.id === w.activeTaskId)?.type === 'video').length;
          if (activeVideos >= 2) return false;
        }

        if (mode === 'chained' && t.type === 'video') {
```

---

### PHÉP THAY THẾ 2 (Trong `executeTaskOnWorker` - Làm sạch Base64 trước khi upload):
**TÌM ĐOẠN:**
```typescript
              } else if (imgTask?.resultBase64) {
                const uploaded = await Flow.upload({
                  base64: imgTask.resultBase64,
                  mimeType: (imgTask.resultMimeType || 'image/png') as any,
                  name: `${task.sceneId}_first_frame.png`
                });
```

**THAY BẰNG:**
```typescript
              } else if (imgTask?.resultBase64) {
                const cleanBase64 = imgTask.resultBase64.replace(/^data:[^;]+;base64,/, '');
                const uploaded = await Flow.upload({
                  base64: cleanBase64,
                  mimeType: (imgTask.resultMimeType || 'image/png') as any,
                  name: `${task.sceneId}_first_frame.png`
                });
```

---

### PHÉP THAY THẾ 3 (Trong `executeTaskOnWorker` - Sửa lỗi TypeError crash khi retry):
**TÌM TOÀN BỘ KHỐI CATCH:**
```typescript
    } catch (err: any) {
      const errMsg = err?.message || 'Unknown error';
      console.error(`Task ${task.id} failed:`, errMsg);
      if (errMsg.includes('MISSING_REF_ASSET')) {
        updateTask(task.id, { status: 'failed', error: `Missing Asset` });
        activeTaskIdsRef.current.delete(task.id);
        addLog('ASSET', `Halted ${task.sceneId}: Missing @${task.referenceFile}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Missing Asset', countdown: 0 });
        return;
      } 
      
      if (errMsg.includes('SAFETY') || errMsg.includes('BLOCK')) {
        updateTask(task.id, { status: 'blocked', error: 'Safety Block' });
        activeTaskIdsRef.current.delete(task.id);
        addLog('WORKER', `Safety block on ${task.sceneId}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Safety Block', countdown: 0 });
        return;
      }
      const nextRetry = task.retryCount + 1;
      if (nextRetry <= SYSTEM_CONFIG.MAX_RETRIES) {
        const backoff = SYSTEM_CONFIG.RETRY_BACKOFF_S[nextRetry - 1] || 10;
        updateTask(task.id, { status: 'retrying', retryCount: nextRetry, error: errMsg });
        activeTaskIdsRef.current.delete(task.id); 
        
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
        activeTaskIdsRef.current.delete(task.id);
        addLog('WORKER', `Permanent Failure: ${task.sceneId}`, 'error');
        updateWorkerSync(workerIdx, { status: 'idle', activeTaskId: null, message: 'Task Failed', countdown: 0 });
      }
    }
```

**THAY THẾ BẰNG KHỐI CATCH AN TOÀN TUYỆT ĐỐI:**
```typescript
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

      const nextRetry = (task.retryCount || 0) + 1;
      const backoff = [5, 10, 20, 30, 45][nextRetry - 1] || 15;

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
