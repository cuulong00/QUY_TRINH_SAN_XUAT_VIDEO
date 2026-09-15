export type PipelineMode = 'Image + Video (Chained)' | 'Image Only' | 'Video Only';

export type SceneStatus = 
  | 'Pending'
  | 'Waiting'
  | 'Generating_Image'
  | 'Image_Done'
  | 'Generating_Video'
  | 'Saving'
  | 'Completed'
  | 'Retrying'
  | 'Failed'
  | 'Skipped';

export interface ParsedScene {
  id: string;                    // e.g. CH01_SC001
  index: number;
  imagePrompt?: string;
  videoPrompt?: string;
  userRefImageTag?: string;      // e.g. engineer.png
  chainedImageTag?: string;      // e.g. @CH01_SC001.png
  aspectRatio: string;           // '16:9'
  duration: number;              // 8
  
  // Runtime State
  status: SceneStatus;
  retryCount: number;
  lastError?: string;
  progress: number;              // 0 - 100
  generatedImageUrl?: string;    // Temporary Blob URL
  generatedVideoUrl?: string;    // Video Blob URL
}

export interface WorkerSlot {
  slotId: number;                // 1 to 6
  sceneId: string | null;
  status: 'Idle' | 'Busy' | 'CoolingDown';
  currentStep: string;
  countdown: number;
}
