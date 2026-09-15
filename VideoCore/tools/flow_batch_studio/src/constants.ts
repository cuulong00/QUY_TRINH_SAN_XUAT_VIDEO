export const SYSTEM_CONFIG = {
  DEFAULT_VIDEO_MODEL: 'Veo 3.1 - Lite [Lower Priority]',
  DEFAULT_IMAGE_MODEL: '🍌 Nano Banana 2',
  VIDEO_MODELS: [
    'Veo 3.1 - Lite [Lower Priority]',
    'Veo 3.1',
    'Veo 3.0'
  ],
  IMAGE_MODELS: [
    '🍌 Nano Banana 2',
    'Nano Banana Pro',
    'Imagen 3'
  ],
  DEFAULT_ASPECT_RATIO: '16:9',
  ASPECT_RATIOS: ['16:9', '9:16', '1:1'],
  DEFAULT_DURATION: '8',
  DURATIONS: ['4', '6', '8'],
  DEFAULT_WORKERS: 4,
  MIN_WORKERS: 1,
  MAX_WORKERS: 10,
  DEFAULT_MIN_JITTER_S: 3,
  DEFAULT_MAX_JITTER_S: 8,
  JITTER_MIN_RANGE: { min: 1, max: 15 },
  JITTER_MAX_RANGE: { min: 3, max: 25 },
  MAX_RETRIES: 5,
  HARD_TIMEOUT_S: 240,
  CIRCUIT_BREAKER_COOLDOWN_S: 60
} as const;
