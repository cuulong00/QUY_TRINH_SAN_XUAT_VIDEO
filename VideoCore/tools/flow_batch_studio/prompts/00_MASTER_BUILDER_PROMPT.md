# ==============================================================================
# 🎬 GOOGLE FLOW BATCH PRODUCTION ENGINE — MASTER PROMPT (OPTIMIZED & LEAN)
# ==============================================================================
# Role: Principal AI Systems & Full-Stack Architect
# Environment: Google Flow Tool Builder (React, TypeScript, Tailwind CSS, Flow SDK)
# Target Models: 
#   - Video Engine: 'Veo 3.1 - Lite [Lower Priority]' (DEFAULT - DO NOT SHORTEN)
#   - Image Engine: '🍌 Nano Banana 2' (DEFAULT)
# Objective: Build an industrial-grade batch generation engine for Google Flow 
# that executes multi-threaded chained image-to-video pipelines with maximum 
# stability, anti-spam jitter, robust 5-time retry, and strict target-only downloads.
# ==============================================================================

### 1. IMMUTABLE SYSTEM DEFAULTS & STATE INITIALIZATION
Declare these constants at the very top of `App.tsx` before any component logic:
```typescript
export const SYSTEM_CONFIG = {
  DEFAULT_VIDEO_MODEL: 'Veo 3.1 - Lite [Lower Priority]',
  DEFAULT_IMAGE_MODEL: '🍌 Nano Banana 2',
  VIDEO_MODELS: ['Veo 3.1 - Lite [Lower Priority]', 'Veo 3.1', 'Veo 3.0'],
  IMAGE_MODELS: ['🍌 Nano Banana 2', 'Nano Banana Pro', 'Imagen 3'],
  DEFAULT_ASPECT_RATIO: '16:9',
  DEFAULT_DURATION: 8,
  DEFAULT_WORKERS: 4,
  MAX_WORKERS: 6,
  MIN_WORKERS: 1,
  DEFAULT_MIN_JITTER_S: 3,
  DEFAULT_MAX_JITTER_S: 8,
  MAX_RETRIES: 5,
  RETRY_BACKOFF_S: [4, 10, 20, 40, 60],
  HARD_TIMEOUT_S: 240, // 4-minute timeout for Veo Lower Priority
  CIRCUIT_BREAKER_COOLDOWN_S: 60
} as const;
```

---

### 2. STRICT TARGET DELIVERABLE DOWNLOAD POLICY (MANDATORY)
The engine MUST download ONLY the final deliverable of the active mode using standard `Flow.download()` (or blob anchor download). Never clutter the user's computer with intermediate files:
- **Mode 1: `Image + Video (Chained - DEFAULT)`**: 
  * Step 1: Generate reference image via `🍌 Nano Banana 2`. The image Blob is held temporarily in RAM.
  * Step 2: Pass the image Blob as input reference ingredient to `Veo 3.1 - Lite [Lower Priority]`.
  * Step 3: Veo generates the 8s 16:9 video.
  * Step 4: **DOWNLOAD ONLY THE VIDEO (`<Scene_ID>.mp4`)`. NEVER download the intermediate image!**
  * Step 5: Immediately call `URL.revokeObjectURL()` on the image blob URL to prevent browser memory leaks.
- **Mode 2: `Image Only`**: 
  * Generates image only ➔ **DOWNLOAD ONLY THE IMAGE (`<Scene_ID>.png`)**.
- **Mode 3: `Video Only`**: 
  * Generates video directly ➔ **DOWNLOAD ONLY THE VIDEO (`<Scene_ID>.mp4`)**.

---

### 3. PROMPT PARSING & INTELLIGENT SANITIZATION
The parser accepts `.txt` files directly via a file input `<input type="file" accept=".txt">`:
```text
CH01_SC001 [IMAGE]: @optional_user_ref.png -> A flat 2D vector illustration of...
CH01_SC001 [VIDEO]: @CH01_SC001.png -> Slow downward crane lowering motion... --ar 16:9 --dur 8s
```
**Parsing & Sanitization Rules**:
1. **Direct File Import**: Provide a prominent button "📂 Upload Storyboard (.txt)" to parse files directly without copy-pasting.
2. **Scene Pairing**: Group `[IMAGE]` and `[VIDEO]` lines by common prefix `Scene ID` (e.g., `CH01_SC001`).
3. **Prompt Stripping (Crucial for AI Models)**:
   - When passing prompt text to `🍌 Nano Banana 2`: Strip out any `@filename ->` tag before sending to the model, sending only pure visual description.
   - When passing prompt text to `Veo 3.1`: Strip out the chained `@CH01_SCXXX.png ->` tag and trailing flags (`--ar 16:9`, `--dur 8s`). Send ONLY the clean camera motion instructions (e.g., *"Slow downward crane lowering motion..."*). Sending raw `@` tags or flags to Veo causes severe hallucinations!
4. **Reference Asset Bin**:
   - Provide a drag-and-drop staging bin in the sidebar where users can upload multiple source reference images.
   - If `[IMAGE]` contains `@my_ref.png`, auto-attach the uploaded file as the model input ingredient.

---

### 4. MULTI-THREADED WORKER QUEUE & ANTI-SPAM JITTER
- **Worker Pool Slider**: Configurable from 1 to 6 concurrent worker slots (Default: 4).
- **Staggered Launch Jitter (Anti-Bot Pattern)**:
  * Two separate sliders: `Min Jitter (s)` (default: 3) and `Max Jitter (s)` (default: 8).
  * When launching adjacent worker slots, introduce a randomized delay: `delay = Math.floor(Math.random() * (max - min + 1) + min) * 1000` to mimic natural human behavior.
- **Global Circuit Breaker (429 Rate Limit Shield)**:
  * If ANY worker encounters an HTTP 429 or Quota Exceeded error:
  * Immediately PAUSE all active workers and freeze the queue for 60 seconds.
  * Display a warning countdown badge: `⚠️ Rate Limit Detected. Cooling down: 45s...`.
  * After 60s, resume queue execution with staggered spacing.
- **Hard Timeout (240s)**:
  * For `Veo 3.1 - Lite [Lower Priority]`, enforce a strict 240-second timeout per task.
  * If a generation hangs over 240s, abort it, mark as a failed attempt, free the worker slot, and trigger retry.

---

### 5. INDUSTRIAL RETRY PROTOCOL & BULK RECOVERY
- **5-Stage Exponential Backoff Auto-Retry**:
  * On transient failure (network timeout, 500/503): automatically retry up to 5 times per scene.
  * Backoff delays: Attempt 1 ➔ 4s | Attempt 2 ➔ 10s | Attempt 3 ➔ 20s | Attempt 4 ➔ 40s | Attempt 5 ➔ 60s.
  * Show live status badge: `Retry 2/5 (Waiting 10s...)`.
  * If all 5 attempts fail, transition scene to `Failed` and record the error reason.
- **Safety Violation Bypass**:
  * If error contains `SAFETY_POLICY_BLOCK`, do NOT waste retries. Mark immediately as `Blocked by Safety Policy` and highlight the offending scene.
- **Bulk Action ("🔄 Retry All Failed")**:
  * Prominent button in the top header that collects all `Failed` scenes, resets their retry counters to 0, and injects them back into the active queue.
- **Per-row Actions**: `Re-run Scene`, `Re-roll Video Only` (uses existing generated image), `Edit Prompt`.

---

### 6. UI / UX LAYOUT (CYBER-NOIR GLASSMORPHISM)
- **Theme Palette**: Deep carbon slate (`#0a0b10`), frosted glass panels (`rgba(18, 20, 30, 0.7)`), electric violet accent (`#8b5cf6`), emerald green (`#10b981`), rose red (`#f43f5e`).
- **Layout Structure**:
  1. **Top Header**:
     - Title: "BATCH ENGINE v1.0.0 INDUSTRIAL DEPLOYMENT".
     - KPI Pills: TOTAL | DONE | IN FLIGHT | RETRYING | FAILED.
     - Master Buttons: `🚀 LAUNCH QUEUE`, `⏸ PAUSE`, `🔄 RETRY ALL FAILED`.
  2. **Left Sidebar (320px scrollable)**:
     - "PIPELINE CONFIGURATION": Processing Mode dropdown (`Chained: Image → Video`, `Image Only`, `Video Only`).
     - "MODEL STACK":
       * Video Engine: `Veo 3.1 - Lite [Lower Priority]` (Default - Exact string).
       * Image Engine: `🍌 Nano Banana 2` (Default).
     - "VIDEO SPECS": Aspect Ratio (`16:9`), Duration (`8s`).
     - "STORYTRACK IMPORT":
       * File input button: `📂 Upload .txt File` (Loads directly into queue).
       * Optional preview/edit textarea.
     - "REFERENCE ASSET BIN": Drag & drop box for user-uploaded images (`@ref.png`).
     - "WORKER PARAMETERS":
       * Active Slots Slider (1 to 6, default 4).
       * Min Jitter Slider (2s - 5s, default 3s).
       * Max Jitter Slider (6s - 15s, default 8s).
  3. **Active Workers Monitor (Top Center)**:
     - 1 to 6 slot cards showing: Worker Slot #, Scene ID, Step Indicator, Countdown Timer, Progress Bar, Retry status badge.
  4. **Live Storyboard Queue Table (Bottom Center)**:
     - Filters: `ALL`, `IN PROGRESS`, `DONE`, `FAILED`.
     - Columns: SCENE, TYPE, STATUS, RETRIES, ACTION.
- **Audio Feedback**: Built-in Web Audio API synthesizer chime (523Hz/1046Hz) on queue completion — zero external asset dependencies.
