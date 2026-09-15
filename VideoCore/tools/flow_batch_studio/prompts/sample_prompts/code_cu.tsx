import React, { useState, useEffect, useCallback, useRef } from 'react';
import { Flow } from 'flow-sdk';
import { Sidebar } from './components/Sidebar';
import { MonitorGrid } from './components/MonitorGrid';
import { PromptTable } from './components/PromptTable';
import { ControlBar } from './components/ControlBar';
import { LogConsole } from './components/LogConsole';
export type MediaType = 'Image' | 'Video' | 'I2V';
export interface Prompt {
  id: string;
  pos: string;
  text: string;
  imagePrompt?: string;
  videoPrompt?: string;
  type: MediaType;
  status: 'Pending' | 'Queueing' | 'Active' | 'Completed' | 'Error';
  progress: number;
  retryCount: number; 
  outputUrl?: string; 
  imagePreviewUrl?: string; 
  videoPreviewUrl?: string; 
  mediaId?: string;   
  error?: string;
  currentStep?: string;
  subStatus?: {
    image: 'idle' | 'processing' | 'done' | 'error';
    video: 'idle' | 'processing' | 'done' | 'error';
  };
}
export interface Track {
  id: string;
  status: 'Idle' | 'Processing';
  currentPromptId: string | null;
  lastPromptId?: string | null;
}
export interface SystemLog {
  id: string;
  timestamp: string;
  type: 'info' | 'error' | 'success' | 'warn' | 'sdk';
  message: string;
  details?: string;
}
function sanitizeFilename(pos: string, index: number, mimeType: string): string {
  const ext = mimeType.split('/')[1]?.replace('jpeg', 'jpg') || 'png';
  const cleanPos = pos.replace(/[^a-zA-Z0-9_\-]/g, '_').slice(0, 20);
  return `${cleanPos || 'render'}_${index + 1}_${Date.now().toString().slice(-4)}.${ext}`;
}
const MAX_RETRIES = 5; // Tăng số lần thử lại cho các tiến trình dài
export default function App() {
  const [projectName, setProjectName] = useState('Director Pro Project');
  const [parallelTracks, setParallelTracks] = useState(3);
  const [staggerDelay, setStaggerDelay] = useState(5); 
  const [isRunning, setIsRunning] = useState(false);
  const [isAutoDownload, setIsAutoDownload] = useState(true);
  
  const [videoModel, setVideoModel] = useState('Veo 3.1 - Lite [Lower Priority]');
  const [imageModel, setImageModel] = useState('🍌 Nano Banana 2');
  
  const [mediaType, setMediaType] = useState<MediaType>('I2V');
  const [aspectRatio, setAspectRatio] = useState('16:9');
  const [clipDuration, setClipDuration] = useState('8s');
  const [prompts, setPrompts] = useState<Prompt[]>([]);
  const [tracks, setTracks] = useState<Track[]>([]);
  const [logs, setLogs] = useState<SystemLog[]>([]);
  const [isLogOpen, setIsLogOpen] = useState(false);
  
  const promptsRef = useRef(prompts);
  const tracksRef = useRef(tracks);
  const lastTrackStartTimeRef = useRef<number>(0);
  const processingIdsRef = useRef<Set<string>>(new Set());
  useEffect(() => { promptsRef.current = prompts; }, [prompts]);
  useEffect(() => { tracksRef.current = tracks; }, [tracks]);
  const addLog = useCallback((type: SystemLog['type'], message: string, details?: string) => {
    setLogs(prev => [{ 
      id: Math.random().toString(36).substr(2, 9), 
      timestamp: new Date().toLocaleTimeString(), 
      type, 
      message, 
      details 
    }, ...prev].slice(0, 300));
  }, []);
  useEffect(() => {
    setTracks(prev => {
      if (prev.length === parallelTracks) return prev;
      if (prev.length < parallelTracks) {
        const diff = parallelTracks - prev.length;
        const newOnes: Track[] = Array.from({ length: diff }).map((_, i) => ({
          id: `TRACK-${prev.length + i + 1}`,
          status: 'Idle',
          currentPromptId: null,
          lastPromptId: null
        }));
        return [...prev, ...newOnes];
      } else {
        return prev.slice(0, parallelTracks);
      }
    });
  }, [parallelTracks]);
  const processPrompt = async (promptId: string, trackId: string, attempt = 1) => {
    try {
      const prompt = promptsRef.current.find(p => p.id === promptId);
      if (!prompt) return;
      setPrompts(prev => prev.map(p => p.id === promptId ? { 
        ...p, 
        status: 'Active', 
        progress: Math.min(95, (prompt.progress || 5) + 2), 
        retryCount: attempt - 1,
        currentStep: attempt > 1 ? `Đang thử lại (Lần ${attempt})...` : 'Khởi tạo...',
      } : p));
      
      setTracks(prev => prev.map(t => t.id === trackId ? { ...t, status: 'Processing', currentPromptId: promptId, lastPromptId: promptId } : t));
      const ratio = (aspectRatio === '9:16' ? '9:16' : '16:9') as '16:9' | '9:16';
      const durationSec = parseInt(clipDuration) || 8;
      let finalResult;
      if (prompt.type === 'I2V') {
        let currentMediaId = prompt.mediaId;
        // Giai đoạn 1: Image (Chỉ chạy nếu chưa có mediaId lưu đệm)
        if (!currentMediaId) {
          setPrompts(prev => prev.map(p => p.id === promptId ? { 
            ...p, 
            currentStep: 'Đang tạo ảnh gốc...', 
            subStatus: { image: 'processing', video: 'idle' } 
          } : p));
          
          const imgRes = await Flow.generate.image({
            prompt: prompt.imagePrompt || prompt.text,
            modelDisplayName: imageModel,
            aspectRatio: ratio
          });
          currentMediaId = imgRes.mediaId;
          
          // Lưu mediaId ngay lập tức để nếu bước Video lỗi, lần thử lại sau sẽ bỏ qua bước này
          setPrompts(prev => prev.map(p => p.id === promptId ? { 
            ...p, 
            progress: 40, 
            mediaId: currentMediaId,
            imagePreviewUrl: `data:${imgRes.mimeType};base64,${imgRes.base64}`,
            subStatus: { image: 'done', video: 'idle' }
          } : p));
          
          addLog('info', `[${prompt.pos}] Đã tạo xong ảnh gốc, chuyển sang video.`);
        }
        // Giai đoạn 2: Video
        setPrompts(prev => prev.map(p => p.id === promptId ? { 
          ...p, 
          currentStep: 'Đang tạo Video (có thể mất vài phút)...', 
          subStatus: { image: 'done', video: 'processing' } 
        } : p));
        finalResult = await Flow.generate.video({
          prompt: prompt.videoPrompt || prompt.text,
          modelDisplayName: videoModel,
          aspectRatio: ratio,
          durationSeconds: durationSec,
          firstFrameImageMediaId: currentMediaId
        });
      } else if (prompt.type === 'Image') {
        setPrompts(prev => prev.map(p => p.id === promptId ? { ...p, subStatus: { image: 'processing', video: 'idle' } } : p));
        finalResult = await Flow.generate.image({
          prompt: prompt.imagePrompt || prompt.text,
          modelDisplayName: imageModel,
          aspectRatio: ratio
        });
      } else {
        setPrompts(prev => prev.map(p => p.id === promptId ? { ...p, subStatus: { image: 'idle', video: 'processing' } } : p));
        finalResult = await Flow.generate.video({
          prompt: prompt.videoPrompt || prompt.text,
          modelDisplayName: videoModel,
          aspectRatio: ratio,
          durationSeconds: durationSec
        });
      }
      const finalUrl = `data:${finalResult.mimeType};base64,${finalResult.base64}`;
      setPrompts(prev => prev.map(p => p.id === promptId ? { 
        ...p, 
        status: 'Completed', 
        progress: 100, 
        outputUrl: finalUrl,
        videoPreviewUrl: p.type !== 'Image' ? finalUrl : undefined,
        imagePreviewUrl: p.type === 'Image' ? finalUrl : p.imagePreviewUrl,
        currentStep: 'Hoàn thành',
        subStatus: { 
          image: p.type === 'Video' ? 'idle' : 'done', 
          video: p.type === 'Image' ? 'idle' : 'done' 
        }
      } : p));
      if (isAutoDownload) {
        await Flow.download({
          base64: finalResult.base64,
          mimeType: finalResult.mimeType,
          filename: sanitizeFilename(prompt.pos, 0, finalResult.mimeType)
        });
      }
      addLog('success', `Đã xong Scene: [${prompt.pos}]`);
      processingIdsRef.current.delete(promptId);
      setTracks(prev => prev.map(t => t.id === trackId ? { ...t, status: 'Idle', currentPromptId: null } : t));
    } catch (err: any) {
      const msg = err.message || 'Unknown error';
      // Nếu là lỗi timeout hoặc "something went wrong", ta thử lại và giữ nguyên mediaId đã có
      if (attempt < MAX_RETRIES) {
        const isTimeout = msg.toLowerCase().includes('timeout') || msg.toLowerCase().includes('wrong');
        addLog('warn', `Lỗi [${promptId}] ${isTimeout ? '(Có thể do thời gian tạo lâu)' : ''}, đang thử lại (${attempt}/${MAX_RETRIES})`, msg);
        
        // Đợi một chút trước khi thử lại để tránh nghẽn
        await new Promise(r => setTimeout(r, 5000 + (attempt * 2000))); 
        return processPrompt(promptId, trackId, attempt + 1);
      } else {
        addLog('error', `Thất bại vĩnh viễn [${promptId}] sau ${MAX_RETRIES} lần thử`, msg);
        setPrompts(prev => prev.map(p => p.id === promptId ? { ...p, status: 'Error', error: msg, currentStep: 'Thất bại' } : p));
        processingIdsRef.current.delete(promptId);
        setTracks(prev => prev.map(t => t.id === trackId ? { ...t, status: 'Idle', currentPromptId: null } : t));
      }
    }
  };
  useEffect(() => {
    if (!isRunning) return;
    const interval = setInterval(() => {
      const now = Date.now();
      if (now - lastTrackStartTimeRef.current < staggerDelay * 1000) return;
      const idleTracks = tracksRef.current.filter(t => t.status === 'Idle');
      const pendingPrompts = promptsRef.current.filter(p => p.status === 'Pending' && !processingIdsRef.current.has(p.id));
      if (idleTracks.length > 0 && pendingPrompts.length > 0) {
        const trackToUse = idleTracks[0];
        const promptToUse = pendingPrompts[0];
        processingIdsRef.current.add(promptToUse.id);
        lastTrackStartTimeRef.current = Date.now();
        processPrompt(promptToUse.id, trackToUse.id);
      }
    }, 1000);
    return () => clearInterval(interval);
  }, [isRunning, staggerDelay, imageModel, videoModel, aspectRatio, clipDuration, isAutoDownload]);
  const handleImport = (text: string) => {
    const lines = text.split('\n').map(l => l.trim()).filter(l => l);
    const sceneMap = new Map<string, Prompt>();
    lines.forEach(line => {
      const match = line.match(/^\[?(.*?)\]?(?:\s+\[(IMAGE|VIDEO)\])?[:\-\s]+(.*)$/i);
      
      if (match) {
        let pos = match[1].trim();
        const tag = match[2]?.toUpperCase();
        let promptText = match[3].trim();
        
        if (tag === 'VIDEO' && promptText.includes('->')) {
          promptText = promptText.split('->')[1].trim();
        }
        if (!sceneMap.has(pos)) {
          sceneMap.set(pos, {
            id: Math.random().toString(36).substr(2, 9),
            pos: pos,
            text: promptText,
            imagePrompt: tag === 'IMAGE' ? promptText : undefined,
            videoPrompt: tag === 'VIDEO' ? promptText : undefined,
            status: 'Pending',
            progress: 0,
            retryCount: 0,
            type: mediaType,
            subStatus: { image: 'idle', video: 'idle' }
          });
        } else {
          const existing = sceneMap.get(pos)!;
          if (tag === 'IMAGE') {
            existing.imagePrompt = promptText;
            if (!existing.videoPrompt) existing.text = promptText;
          } else if (tag === 'VIDEO') {
            existing.videoPrompt = promptText;
            existing.text = promptText;
          }
        }
      } else {
        const id = Math.random().toString(36).substr(2, 9);
        sceneMap.set(id, {
          id,
          pos: 'Scene',
          text: line,
          status: 'Pending',
          progress: 0,
          retryCount: 0,
          type: mediaType,
          subStatus: { image: 'idle', video: 'idle' }
        });
      }
    });
    setPrompts(prev => [...prev, ...Array.from(sceneMap.values())]);
    addLog('info', `Đã nạp thêm ${sceneMap.size} kịch bản.`);
  };
  const updatePrompt = (id: string, updates: Partial<Prompt>) => {
    setPrompts(prev => prev.map(p => {
      if (p.id === id) {
        // Nếu thay đổi nội dung chữ, xóa mediaId cũ để force render lại từ đầu
        const shouldClearCache = updates.text !== undefined || updates.imagePrompt !== undefined || updates.videoPrompt !== undefined;
        return { 
          ...p, 
          ...updates, 
          mediaId: shouldClearCache ? undefined : (updates.mediaId || p.mediaId),
          imagePreviewUrl: shouldClearCache ? undefined : (updates.imagePreviewUrl || p.imagePreviewUrl),
          progress: shouldClearCache ? 0 : (updates.progress ?? p.progress)
        };
      }
      return p;
    }));
  };
  const handleExportLogs = async () => {
    const content = logs.map(l => `[${l.timestamp}] [${l.type.toUpperCase()}] ${l.message} ${l.details ? `\nDetails: ${l.details}` : ''}`).join('\n');
    const base64 = btoa(unescape(encodeURIComponent(content)));
    await Flow.download({
      base64,
      mimeType: 'text/plain',
      filename: `render_logs_${Date.now()}.txt`
    });
    addLog('info', 'Đã xuất tệp tin nhật ký hệ thống.');
  };
  const handleRetryAll = () => {
    setPrompts(prev => prev.map(p => p.status === 'Error' ? { ...p, status: 'Pending', error: undefined, progress: p.mediaId ? 40 : 0, retryCount: 0 } : p));
    setIsRunning(true);
    addLog('warn', 'Đang kích hoạt thử lại toàn bộ lỗi.');
  };
  const handleRetryOne = (id: string) => {
    setPrompts(prev => prev.map(p => p.id === id ? { ...p, status: 'Pending', error: undefined, progress: p.mediaId ? 40 : 0, retryCount: 0 } : p));
    setIsRunning(true);
  };
  return (
    <div className="flex h-screen w-screen overflow-hidden bg-[#0e0e0e] text-white selection:bg-emerald-500/30">
      <Sidebar 
        parallelTracks={parallelTracks} setParallelTracks={setParallelTracks}
        staggerDelay={staggerDelay} setStaggerDelay={setStaggerDelay}
        videoModel={videoModel} setVideoModel={setVideoModel}
        imageModel={imageModel} setImageModel={setImageModel}
        mediaType={mediaType} setMediaType={setMediaType}
        aspectRatio={aspectRatio} setAspectRatio={setAspectRatio}
        clipDuration={clipDuration} setClipDuration={setClipDuration}
        isAutoDownload={isAutoDownload} setIsAutoDownload={setIsAutoDownload}
        onToggleLog={() => setIsLogOpen(!isLogOpen)}
        errorCount={prompts.filter(p => p.status === 'Error').length}
      />
      <main className="flex-1 flex flex-col h-full border-l border-white/5 relative">
        <header className="h-[80px] px-8 flex items-center justify-between bg-black/40 border-b border-white/5 backdrop-blur-md">
          <ControlBar 
            projectName={projectName} setProjectName={setProjectName}
            isRunning={isRunning} setIsRunning={setIsRunning}
            onImport={handleImport}
            onReset={() => { setPrompts([]); setLogs([]); setIsRunning(false); processingIdsRef.current.clear(); }}
            onRetryAllErrors={handleRetryAll}
            completedCount={prompts.filter(p => p.status === 'Completed').length}
            totalCount={prompts.length}
            errorCount={prompts.filter(p => p.status === 'Error').length}
          />
        </header>
        <div className="flex-1 overflow-y-auto p-8 flex flex-col gap-8 bg-[#0e0e0e] dark-scrollbar">
          <MonitorGrid tracks={tracks.map(t => {
            const promptId = t.currentPromptId || t.lastPromptId;
            const p = prompts.find(p => p.id === promptId);
            return {
              ...t,
              currentScene: p?.pos || 'Idle',
              progress: p?.progress || 0,
              imagePreviewUrl: p?.imagePreviewUrl,
              videoPreviewUrl: p?.videoPreviewUrl,
              outputUrl: p?.outputUrl,
              type: p?.type,
              currentStep: p?.currentStep,
              promptStatus: p?.status,
              subStatus: p?.subStatus
            };
          })} />
          <section className="flex-1 bg-white/[0.01] border border-white/5 rounded-3xl overflow-hidden min-h-[400px]">
            <PromptTable 
              prompts={prompts} 
              onRetry={handleRetryOne} 
              onUpdate={updatePrompt}
              onCopyError={() => {
                const errors = prompts.filter(p => p.status === 'Error').map(p => `[${p.pos}] ${p.text}`).join('\n');
                navigator.clipboard.writeText(errors);
                addLog('info', 'Đã sao chép kịch bản lỗi.');
              }}
              onDelete={(id) => setPrompts(prev => prev.filter(p => p.id !== id))}
            />
          </section>
        </div>
        <LogConsole 
          isOpen={isLogOpen} 
          onClose={() => setIsLogOpen(false)} 
          logs={logs} 
          onClear={() => setLogs([])}
          onExport={handleExportLogs}
        />
      </main>
    </div>
  );
}