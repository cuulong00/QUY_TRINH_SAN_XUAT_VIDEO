/**
 * IMMUTABLE SYSTEM CONFIGURATION
 * Dán khối này vào đầu file App.tsx trong tab "Mã" của Google Flow
 * để khóa chết các thiết lập mặc định, chống bị AI tự ý thay đổi.
 */
export const SYSTEM_CONFIG = {
  // Model mặc định bất biến
  DEFAULT_VIDEO_MODEL: 'Veo 3.1 - Lite [Lower Priority]',
  DEFAULT_IMAGE_MODEL: '🍌 Nano Banana 2',

  // Tùy chọn Model
  VIDEO_MODEL_OPTIONS: [
    'Veo 3.1 - Lite [Lower Priority]',
    'Veo 3.1',
    'Veo 3.0'
  ],
  IMAGE_MODEL_OPTIONS: [
    '🍌 Nano Banana 2',
    'Nano Banana Pro',
    'Imagen 3'
  ],

  // Cấu hình Queue & Concurrency
  DEFAULT_CONCURRENT_TRACKS: 4,
  MAX_CONCURRENT_TRACKS: 6,
  MIN_CONCURRENT_TRACKS: 1,

  // Cấu hình Jitter (Anti-Spam Delay ngẫu nhiên giữa các luồng)
  DEFAULT_MIN_JITTER_SECONDS: 3,
  DEFAULT_MAX_JITTER_SECONDS: 8,

  // Cơ chế Retry & Fault-Tolerance
  MAX_RETRIES: 5,
  RETRY_BACKOFF_STEPS_SECONDS: [4, 10, 20, 40, 60],
  HARD_TIMEOUT_SECONDS: 240, // 4 phút cho Veo Lower Priority

  // Quy tắc File Đích (Target Deliverable Only)
  DEFAULT_ASPECT_RATIO: '16:9',
  DEFAULT_DURATION_SECONDS: 8,
  
  // Pipeline Modes
  MODES: {
    CHAINED: 'Image + Video (Chained)',
    IMAGE_ONLY: 'Image Only',
    VIDEO_ONLY: 'Video Only'
  }
} as const;
