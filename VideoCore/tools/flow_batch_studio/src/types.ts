export type GenerationMode = 'chained' | 'image-only' | 'video-only';

export type SceneStatus = 'idle' | 'pending' | 'processing' | 'completed' | 'failed' | 'blocked' | 'retrying';

export interface SceneTask {
  id: string;
  sceneId: string;
  type: 'image' | 'video';
  prompt: string;
  referenceFile?: string;
  status: SceneStatus;
  progress: number;
  retryCount: number;
  error?: string;
  resultMediaId?: string;
  resultBase64?: string;
  resultMimeType?: string;
  startedAt?: number;
  completedAt?: number;
  downloaded?: boolean;
}

export interface SceneGroup {
  sceneId: string;
  status: SceneStatus;
  imageTask?: SceneTask;
  videoTask?: SceneTask;
}

export interface WorkerState {
  id: number;
  activeTaskId: string | null;
  status: 'idle' | 'waiting' | 'generating';
  message: string;
  progress: number;
  countdown: number;
}

export interface BatchState {
  groups: SceneGroup[];
  tasks: SceneTask[];
  isProcessing: boolean;
  isPaused: boolean;
  circuitBreakerActive: boolean;
  cooldownRemaining: number;
  destinationSet: boolean;
}
