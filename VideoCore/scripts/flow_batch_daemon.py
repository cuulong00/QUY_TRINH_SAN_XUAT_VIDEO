#!/usr/bin/env python3
"""
Flow Batch Daemon — Zero-Token High-Velocity Master Orchestrator
----------------------------------------------------------------
Key Features:
  1. Single Master Batch Execution (Runs all remaining prompts in one unified queue)
  2. Aggressive External Watchdog (Cancels any video stuck > 160s or image > 50s)
  3. Zero Stall / Deadlock Recovery (Auto-clicks 'Run Incomplete Only' if workers go idle)
  4. Auto-moving finished .mp4 files directly to destination folder
  5. Mass-Block Defense (detects 10 consecutive errors and pauses safely)
"""

import os
import sys
import time
import glob
import json
import base64
import shutil
import asyncio
import urllib.request
import websockets

# TIMEOUT CONSTRAINTS
MAX_VIDEO_TIME_S = 300  # 5 minutes: Veo 3.1 Lite Lower Priority watchdog timeout per user instruction
MAX_IMAGE_TIME_S = 90   # 90 seconds: Nano Banana 2 watchdog timeout

def log(msg, level="INFO"):
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {msg}", flush=True)

async def cdp_call(ws, method, params=None, req_id=1):
    payload = {"id": req_id, "method": method, "params": params or {}}
    await ws.send(json.dumps(payload))
    res = json.loads(await ws.recv())
    return res

async def cdp_eval(ws, expression, req_id=1):
    res = await cdp_call(ws, "Runtime.evaluate", {
        "expression": expression,
        "returnByValue": True,
        "awaitPromise": True
    }, req_id=req_id)
    if "result" in res and "result" in res["result"]:
        return res["result"]["result"].get("value")
    return None

async def find_runner_ws_url(port=9222, max_retries=15, retry_delay=2):
    hosts = ["[::1]", "127.0.0.1", "localhost"]
    for attempt in range(max_retries):
        for host in hosts:
            try:
                req = urllib.request.urlopen(f"http://{host}:{port}/json", timeout=5)
                tabs = json.loads(req.read().decode("utf-8"))
                for t in tabs:
                    url = t.get("url", "")
                    if "scf.usercontent.goog" in url:
                        ws_url = t.get("webSocketDebuggerUrl")
                        if ws_url:
                            try:
                                val = await check_is_batch_runner(ws_url)
                                if val:
                                    return ws_url
                            except Exception:
                                pass
            except Exception as e:
                pass
        if attempt < max_retries - 1:
            await asyncio.sleep(retry_delay)
    return None

async def check_is_batch_runner(ws_url):
    try:
        async with websockets.connect(ws_url) as ws:
            val = await cdp_eval(ws, "Boolean(document.body && document.body.innerText.includes('BATCH PRODUCTION'))")
            return bool(val)
    except Exception:
        return False

async def clear_existing_queue(ws):
    log("Resetting and clearing batch queue...", "SETUP")
    await cdp_eval(ws, """(() => {
        const haltBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('HALT PRODUCTION'));
        if (haltBtn) haltBtn.click();
        const clearBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Clear'));
        if (clearBtn) clearBtn.click();
        return true;
    })()""")
    await asyncio.sleep(1.5)

async def set_browser_download_behavior(port, download_path):
    hosts = ["[::1]", "127.0.0.1", "localhost"]
    for host in hosts:
        try:
            req = urllib.request.urlopen(f"http://{host}:{port}/json/version", timeout=3)
            info = json.loads(req.read().decode("utf-8"))
            browser_ws = info.get("webSocketDebuggerUrl")
            if browser_ws:
                async with websockets.connect(browser_ws) as ws:
                    payload = {
                        "id": 1,
                        "method": "Browser.setDownloadBehavior",
                        "params": {
                            "behavior": "allow",
                            "downloadPath": download_path,
                            "eventsEnabled": True
                        }
                    }
                    await ws.send(json.dumps(payload))
                    await ws.recv()
                    log(f"Configured Browser.setDownloadBehavior -> {download_path}", "SETUP")
                    return
        except Exception:
            pass

async def ingest_reference_images(ws, ref_dir):
    if not ref_dir or not os.path.isdir(ref_dir):
        return

    image_files = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
        image_files.extend(glob.glob(os.path.join(ref_dir, ext)))

    if not image_files:
        return

    log(f"Ingesting {len(image_files)} reference assets from {ref_dir}...", "SETUP")
    
    assets_data = []
    for fpath in sorted(image_files):
        fname = os.path.basename(fpath)
        mime = "image/png" if fname.endswith(".png") else "image/jpeg"
        with open(fpath, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        assets_data.append({"name": fname, "mime": mime, "b64": b64})

    js_inject = f"""(async () => {{
        const assets = {json.dumps(assets_data)};
        const input = document.querySelector('input[type="file"][accept*="image"]');
        if (!input) return {{ success: false, error: 'Asset file input not found' }};
        
        const dt = new DataTransfer();
        for (const a of assets) {{
            const res = await fetch("data:" + a.mime + ";base64," + a.b64);
            const blob = await res.blob();
            const file = new File([blob], a.name, {{ type: a.mime }});
            dt.items.add(file);
        }}
        input.files = dt.files;
        input.dispatchEvent(new Event('change', {{ bubbles: true }}));
        return {{ success: true, count: assets.length }};
    }})()"""

    await cdp_eval(ws, js_inject)
    await asyncio.sleep(2)
    
    badges = await cdp_eval(ws, """(() => {
        return Array.from(document.querySelectorAll('.border-violet-500\\\\/30, .text-violet-300'))
            .map(e => e.innerText.trim())
            .filter(Boolean);
    })()""")
    log(f"Asset Bin active references: {badges}", "SUCCESS")

async def ingest_prompts(ws, prompts_path):
    if not os.path.isfile(prompts_path):
        raise FileNotFoundError(f"Prompts file not found: {prompts_path}")

    with open(prompts_path, "r", encoding="utf-8") as f:
        content = f.read()

    fname = os.path.basename(prompts_path)
    log(f"Ingesting prompts from {fname} ({len(content.splitlines())} lines)...", "SETUP")

    js_inject = f"""(async () => {{
        const input = document.querySelector('input[type="file"][accept*=".txt"]');
        if (!input) return {{ success: false, error: 'Text file input not found' }};
        
        const content = {json.dumps(content)};
        const file = new File([content], {json.dumps(fname)}, {{ type: 'text/plain' }});
        const dt = new DataTransfer();
        dt.items.add(file);
        input.files = dt.files;
        input.dispatchEvent(new Event('change', {{ bubbles: true }}));
        return {{ success: true }};
    }})()"""

    await cdp_eval(ws, js_inject)
    await asyncio.sleep(2.5)

    scene_info = await cdp_eval(ws, """(() => {
        const rows = document.querySelectorAll('tr').length;
        const text = document.querySelector('header')?.innerText || '';
        const sm = text.match(/SCENES\\s+(\\d+)/);
        return { rows, scenes: sm ? parseInt(sm[1]) : 0 };
    })()""")
    log(f"Prompts loaded: {scene_info.get('scenes', 0)} scenes parsed ({scene_info.get('rows', 0)} rows)", "SUCCESS")

async def set_workers_count(ws, count=5):
    log(f"Setting concurrent workers count to {count}...", "SETUP")
    res = await cdp_eval(ws, f"""(() => {{
        const slider = document.querySelector('input[type="range"]');
        if (!slider) return false;
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        nativeInputValueSetter.call(slider, {count});
        slider.dispatchEvent(new Event("input", {{ bubbles: true }}));
        slider.dispatchEvent(new Event("change", {{ bubbles: true }}));
        return true;
    }})()""")
    log(f"Workers slider set to {count} (success={res})", "SUCCESS")
    await asyncio.sleep(1)

async def launch_matrix(ws):
    log("Kicking off generation pipeline via LAUNCH MATRIX...", "LAUNCH")
    res = await cdp_eval(ws, """(() => {
        const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('LAUNCH MATRIX'));
        if (btn) {
            btn.click();
            return true;
        }
        return false;
    })()""")
    if not res:
        log("LAUNCH MATRIX button not found or already running", "WARN")
    else:
        log("LAUNCH MATRIX clicked successfully!", "SUCCESS")
    await asyncio.sleep(2)

def move_completed_downloads(downloads_dir, dest_dir):
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    moved = []
    for fpath in glob.glob(os.path.join(downloads_dir, "*.mp4")):
        fname = os.path.basename(fpath)
        crdownload = fpath + ".crdownload"
        if os.path.exists(crdownload):
            continue

        try:
            size_mb = os.path.getsize(fpath) / (1024 * 1024)
            if size_mb < 0.5:
                continue

            target_path = os.path.join(dest_dir, fname)
            shutil.move(fpath, target_path)
            log(f"Moved video: {fname} ({size_mb:.2f} MB) -> {dest_dir}", "DOWNLOAD")
            moved.append(fname)
        except Exception as e:
            log(f"Error moving {fname}: {e}", "WARN")
    return moved

async def monitor_master_batch(ws, downloads_dir, dest_dir, check_interval=10):
    log("==================================================================", "MONITOR")
    log(f"Active Watchdog Enabled: Max Video={MAX_VIDEO_TIME_S}s | Max Image={MAX_IMAGE_TIME_S}s", "MONITOR")
    log("==================================================================", "MONITOR")

    last_progress_time = time.time()
    last_ready_count = 0
    total_moved = 0
    slot_tracking = {}  # slot_idx -> {"task": str, "start": float}

    while True:
        await asyncio.sleep(check_interval)

        # 1. Move any completed downloads
        new_moved = move_completed_downloads(downloads_dir, dest_dir)
        if new_moved:
            total_moved += len(new_moved)
            last_progress_time = time.time()

        # 2. Query App State & Slot Contents
        state = await cdp_eval(ws, """(() => {
            const headerText = document.querySelector('header')?.innerText || '';
            const sm = headerText.match(/SCENES\\s+(\\d+)/);
            const rm = headerText.match(/READY\\s+(\\d+)/);
            const fm = headerText.match(/FAILED\\s+(\\d+)/);

            const scenes = sm ? parseInt(sm[1]) : 0;
            const ready = rm ? parseInt(rm[1]) : 0;
            const failed = fm ? parseInt(fm[1]) : 0;

            const isProcessing = Array.from(document.querySelectorAll('button')).some(b => b.innerText.includes('HALT PRODUCTION'));
            const circuitAlert = document.querySelector('[class*="bg-rose-950"], [class*="SHIELD"], [class*="bg-amber-950"]')?.innerText || '';
            const hasShield = Array.from(document.querySelectorAll('*')).some(e => 
                e.innerText && (e.innerText.includes('ANTI-SPAM SHIELD') || e.innerText.includes('HẠ NHIỆT') || e.innerText.includes('RATE-LIMIT BLOCK'))
            );

            // Query active worker slots
            const slotSpans = Array.from(document.querySelectorAll('span')).filter(s => s.innerText && s.innerText.startsWith('SLOT-'));
            const slots = slotSpans.map((span, idx) => {
                const card = span.parentElement?.parentElement || span.closest('div');
                const text = card ? card.innerText.replace(/\\s+/g, ' ').trim() : span.innerText;
                const isGenerating = text.includes('GENERATING');
                const isVideo = text.includes('VIDEO') || text.includes('Veo');
                const isImage = text.includes('IMAGE') || text.includes('Banana');
                // Extract task ID (e.g. CH08_SC001 or CH01_SC001a1)
                const m = text.match(/(CH\\d+_SC[A-Za-z0-9_]+)/i);
                const sceneId = m ? m[1] : '';
                return { idx, text, isGenerating, isVideo, isImage, sceneId };
            });

            const logs = Array.from(document.querySelectorAll('.font-mono'))
                .map(e => e.innerText.trim())
                .filter(t => t.startsWith('['));

            return {
                scenes,
                ready,
                failed,
                isProcessing,
                hasShield,
                circuitAlert: circuitAlert.replace(/\\s+/g, ' ').slice(0, 120),
                slots,
                recentLog: logs.length ? logs[logs.length - 1].replace(/\\s+/g, ' ') : ''
            };
        })()""")

        if not state:
            log("Lost connection to runner iframe or frame refreshed", "WARN")
            continue

        scenes = state.get("scenes", 0)
        ready = state.get("ready", 0)
        failed = state.get("failed", 0)
        is_proc = state.get("isProcessing", False)
        circuit = state.get("circuitAlert", "")
        slots = state.get("slots", [])
        recent_log = state.get("recentLog", "")

        # 3. Active Slot Watchdog (Cancel if stuck too long!)
        now = time.time()
        for s in slots:
            idx = s["idx"]
            scene_id = s.get("sceneId", "")
            is_gen = s.get("isGenerating", False)
            is_vid = s.get("isVideo", False)
            is_img = s.get("isImage", False)

            if is_gen and scene_id:
                task_key = f"{scene_id}_{'VID' if is_vid else 'IMG'}"
                if idx not in slot_tracking or slot_tracking[idx]["task"] != task_key:
                    slot_tracking[idx] = {"task": task_key, "start": now, "sceneId": scene_id, "isVid": is_vid}
                else:
                    elapsed = now - slot_tracking[idx]["start"]
                    limit = MAX_VIDEO_TIME_S if is_vid else MAX_IMAGE_TIME_S
                    if elapsed > limit:
                        log(f"🚨 [WATCHDOG CANCELLATION] Slot {idx+1} stuck on {task_key} for {int(elapsed)}s (> {limit}s)! Force-cancelling request...", "WATCHDOG")
                        # Click close button on worker card or refresh on that scene
                        await cdp_eval(ws, f"""(() => {{
                            const spans = Array.from(document.querySelectorAll('span')).filter(s => s.innerText && s.innerText.includes('SLOT-{idx+1}'));
                            if (spans.length > 0) {{
                                const card = spans[0].parentElement?.parentElement || spans[0].closest('div');
                                if (card) {{
                                    const closeBtn = Array.from(card.querySelectorAll('button')).find(b => b.innerText.includes('close') || (b.title && b.title.includes('giải phóng')));
                                    if (closeBtn) {{
                                        closeBtn.click();
                                        return 'Clicked force skip button on Slot {idx+1}';
                                    }}
                                }}
                            }}
                            const tr = Array.from(document.querySelectorAll('tr')).find(r => r.innerText.includes('{scene_id}'));
                            if (tr) {{
                                const btn = tr.querySelector('button.material-symbols-outlined');
                                if (btn) {{
                                    btn.click();
                                    return 'Clicked refresh on {scene_id}';
                                }}
                            }}
                            return 'Row/Worker not found';
                        }})()""")
                        # Reset tracking for this slot
                        slot_tracking.pop(idx, None)
                        last_progress_time = now
            else:
                slot_tracking.pop(idx, None)

        log(f"Status: READY={ready}/{scenes} | FAILED={failed} | Processing={is_proc} | Last Log: {recent_log}")

        # Check Circuit Breaker / Cooldown
        has_shield = state.get("hasShield", False)
        is_cooling_down = has_shield or ("SHIELD" in circuit) or ("10 lỗi liên tiếp" in circuit) or ("HẠ NHIỆT" in circuit)
        if is_cooling_down:
            log(f"MASS BLOCK SHIELD ACTIVE: {circuit or 'Cooling down'}", "MASS_BLOCK")
            last_progress_time = now  # Reset progress timer so recovery NEVER fires during cooldown

        # Update Progress
        if ready > last_ready_count:
            last_ready_count = ready
            last_progress_time = now

        # Check Completion
        if scenes > 0 and (ready + failed) >= scenes and not is_proc:
            log(f"ALL PROMPTS RESOLVED: {ready} ready, {failed} failed out of {scenes} scenes.", "SUCCESS")
            await asyncio.sleep(4)
            move_completed_downloads(downloads_dir, dest_dir)
            break

        if scenes > 0 and ready >= scenes:
            log(f"100% COMPLETE! All {ready}/{scenes} scenes generated successfully!", "SUCCESS")
            await asyncio.sleep(4)
            move_completed_downloads(downloads_dir, dest_dir)
            break

        # Auto-recover if workers stalled for > 90s (STRICTLY ONLY WHEN NOT COOLING DOWN)
        if not is_proc and not is_cooling_down and scenes > 0 and (ready + failed) < scenes:
            if now - last_progress_time > 90:
                log("Workers idle with pending tasks. Auto-clicking '⚡ Run Incomplete Only'...", "RECOVERY")
                await cdp_eval(ws, """(() => {
                    const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Run Incomplete Only'));
                    if (btn) btn.click();
                })()""")
                last_progress_time = now

    log(f"Master Batch finished. Total video files moved: {total_moved}", "SUCCESS")

async def run_daemon(prompts_file, ref_dir, dest_dir, port=9222, monitor_only=False, workers=2):
    log("==================================================================", "INIT")
    log("Starting Unified Master Batch Flow Daemon" + (" [ATTACH / MONITOR ONLY]" if monitor_only else ""), "INIT")
    log(f"Configured concurrency: {workers} workers", "INIT")
    log("==================================================================", "INIT")

    ws_url = await find_runner_ws_url(port)
    if not ws_url:
        log("Failed to find Google Flow Batch Studio runner iframe on port 9222", "FATAL")
        sys.exit(1)

    log(f"Connected to Flow Runner via CDP: {ws_url}", "CONNECTED")
    downloads_dir = os.path.expanduser("~/Downloads")
    await set_browser_download_behavior(port, dest_dir)

    async with websockets.connect(ws_url, max_size=50 * 1024 * 1024) as ws:
        if not monitor_only:
            # 1. Clear previous queue
            await clear_existing_queue(ws)

            # 2. Ingest Reference Assets
            if ref_dir:
                await ingest_reference_images(ws, ref_dir)

            # 3. Ingest All Remaining Prompts
            await ingest_prompts(ws, prompts_file)

            # 4. Set Concurrent Workers
            await set_workers_count(ws, workers)

            # 5. Launch Matrix
            await launch_matrix(ws)

        # 6. Monitor and Watchdog
        await monitor_master_batch(ws, downloads_dir, dest_dir, check_interval=10)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Flow Batch Master Daemon")
    parser.add_argument("--prompts", default="", help="Path to prompts missing .txt file")
    parser.add_argument("--ref-dir", default="", help="Path to reference images directory")
    parser.add_argument("--dest-dir", required=True, help="Destination directory for completed videos")
    parser.add_argument("--port", type=int, default=9222, help="Chrome DevTools port")
    parser.add_argument("--workers", "-w", type=int, default=4, help="Number of concurrent workers (default: 4)")
    parser.add_argument("--monitor-only", action="store_true", help="Attach to running batch without clearing queue")
    args = parser.parse_args()

    asyncio.run(run_daemon(
        prompts_file=os.path.abspath(args.prompts) if args.prompts else "",
        ref_dir=os.path.abspath(args.ref_dir) if args.ref_dir else "",
        dest_dir=os.path.abspath(args.dest_dir),
        port=args.port,
        monitor_only=args.monitor_only,
        workers=args.workers
    ))
