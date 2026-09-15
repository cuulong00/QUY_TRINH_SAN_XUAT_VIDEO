# BẢN VÁ SỐ 14: THÊM CỘT SỐ THỨ TỰ (STT / #) TRƯỚC CỘT ID PHÂN CẢNH & TỐI ƯU HIỂN THỊ ĐẾM CẢNH
# Phiên bản: v1.6.6

⚠️ **BẢNG KHÓA TÍNH NĂNG BẤT BIẾN:**
- **GIỮ NGUYÊN 100%** toàn bộ logic Watchdog 10 phút, tự động fallback model ảnh, dồn video về cuối queue vừa cập nhật ở v1.6.5.
- **GIỮ NGUYÊN 100%** Asset Bin, Chapter Controller, Lightbox preview, ZIP download.

---

### PHÉP SỬA 1: THÊM CỘT SỐ THỨ TỰ (STT / #) TRƯỚC CỘT ID PHÂN CẢNH

**1. TÌM ĐOẠN THEAD (Tiêu đề bảng):**
```tsx
                <thead className="sticky top-0 bg-[#0a0b10] z-10">
                  <tr className="border-b border-white/5">
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter">ID</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter text-center">Step 1 [IMG]</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter text-center">Step 2 [VID]</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter">Compute Slot</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter">Status</th>
                    <th className="p-4 font-bold text-white/20 uppercase tracking-tighter text-right">Reset</th>
                  </tr>
                </thead>
```

**THAY BẰNG:**
```tsx
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
```

---

**2. TÌM ĐOẠN TBODY (Dòng nội dung bảng):**
```tsx
                <tbody>
                  {filteredGroups.map(group => {
                    const imgTask = batch.tasks.find(t => t.sceneId === group.sceneId && t.type === 'image') || group.imageTask;
                    const vidTask = batch.tasks.find(t => t.sceneId === group.sceneId && t.type === 'video') || group.videoTask;
                    const worker = workers.find(w => w.activeTaskId && (w.activeTaskId === imgTask?.id || w.activeTaskId === vidTask?.id));
                    const groupTasks = [imgTask, vidTask].filter(Boolean) as SceneTask[];
                    const retryMax = Math.max(...groupTasks.map(t => t.retryCount), 0);
                    return (
                      <tr key={group.sceneId} className="border-b border-white/5 hover:bg-white/5 transition-colors">
                        <td className="p-4 font-bold text-white/70">{group.sceneId}</td>
```

**THAY BẰNG:**
```tsx
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
```

---

### PHÉP SỬA 2 (TÙY CHỌN NÂNG CẤP): TỐI ƯU HIỂN THỊ KPI ĐẾM THEO PHÂN CẢNH (TRÁNH HIỂU NHẦM 12 CẢNH THÀNH 24 QUEUE)
* **Mục đích:** Ở chế độ Chained, KPI hiển thị rõ số phân cảnh (12 Cảnh) và số Video thành phẩm đã xong (READY), thay vì cộng dồn cả task ảnh làm người dùng tưởng 24 cảnh.

**TÌM ĐOẠN:**
```tsx
            <div className="flex gap-2">
              <KPI label="QUEUE" value={batch.tasks.filter(t => t.status === 'idle' || t.status === 'pending').length} />
              <KPI label="READY" value={batch.tasks.filter(t => t.status === 'completed').length} color="text-emerald-400" />
              <KPI label="FAILED" value={batch.tasks.filter(t => t.status === 'failed' || t.status === 'blocked').length} color="text-rose-400" />
            </div>
```

**THAY BẰNG:**
```tsx
            <div className="flex gap-2">
              {/* Hiển thị số phân cảnh thực tế thay vì tổng số task kỹ thuật */}
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
```

---

### PHÉP SỬA 3 (TÙY CHỌN NÂNG CẤP): TỐI ƯU THẺ CHƯƠNG ĐẾM THEO SỐ CẢNH (VÍ DỤ `0/12` THAY VÌ `0/24`)

**TÌM ĐOẠN (Trong phần Chapter Controller thẻ từng chương):**
```tsx
                  const chTasks = batch.tasks.filter(t => (t.sceneId.match(/^([A-Za-z0-9]+)[_-]/)?.[1]?.toUpperCase() || 'OTHER') === ch);
                  const completedTasks = chTasks.filter(t => t.status === 'completed').length;
                  const totalTasks = chTasks.length;
                  const isCompleted = totalTasks > 0 && completedTasks === totalTasks;
                  const isRunning = chTasks.some(t => t.status === 'processing' || t.status === 'retrying');
                  const percent = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;
```

**THAY BẰNG:**
```tsx
                  const chTasks = batch.tasks.filter(t => (t.sceneId.match(/^([A-Za-z0-9]+)[_-]/)?.[1]?.toUpperCase() || 'OTHER') === ch);
                  // Ở chế độ Chained: chỉ tính video hoàn thành là đã xong phân cảnh
                  const completedTasks = mode === 'chained'
                    ? chTasks.filter(t => t.type === 'video' && t.status === 'completed').length
                    : chTasks.filter(t => t.status === 'completed').length;
                  const totalTasks = mode === 'chained' ? Math.ceil(chTasks.length / 2) : chTasks.length;
                  const isCompleted = totalTasks > 0 && completedTasks === totalTasks;
                  const isRunning = chTasks.some(t => t.status === 'processing' || t.status === 'retrying');
                  const percent = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;
```
