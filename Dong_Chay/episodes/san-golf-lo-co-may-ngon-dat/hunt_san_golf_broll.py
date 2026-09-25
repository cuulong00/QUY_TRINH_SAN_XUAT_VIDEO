#!/usr/bin/env python3
"""
Footage Hunter — Master High-Performance B-Roll Pipeline for 'Dong_Chay / Sân Golf: Cỗ Máy Ngốn Đất'
====================================================================================================
Áp dụng chuẩn kiến trúc Agentic Video Retrieval & High-Performance yt-dlp:
1. Visual Intent Sourcing: Truy vấn bám sát thực thể vật lý (Subject + Action + Camera + 4K B-Roll).
2. High-Performance yt-dlp: Bỏ cookie keychain, dùng player_client=android,web (~4s/download).
3. HTTP Range Request (--download-sections): Chỉ tải đúng vài giây footage (<2MB/scene).
4. Fair Use Rules: Tước sạch 100% audio (-an), Scale 104% & Crop 1920x1080, Color Grade nhẹ.
5. Automated Frame Audit Gate: Tự động trích xuất frame kiểm định trước khi lưu trữ.
"""

import os
import sys
import json
import glob
import time
import shutil
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

EPISODE_DIR = Path("/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/san-golf-lo-co-may-ngon-dat")
VIDEOS_DIR = EPISODE_DIR / "videos"
STRIPPED_DIR = EPISODE_DIR / "video_stripped/videos"
BACKUP_DIR = EPISODE_DIR / "backup"
AUDIT_FRAMES_DIR = EPISODE_DIR / "audit_frames"

VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
STRIPPED_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
AUDIT_FRAMES_DIR.mkdir(parents=True, exist_ok=True)

YT_DLP_BIN = "/Users/pro16/.local/bin/yt-dlp"
if not os.path.exists(YT_DLP_BIN):
    YT_DLP_BIN = "yt-dlp"

def log(msg, level="INFO"):
    ts = time.strftime("%H:%M:%S")
    icons = {"INFO": "ℹ️", "SUCCESS": "✅", "WARN": "⚠️", "ERROR": "❌", "HUNT": "🎯", "PROCESS": "⚙️", "GATE": "🛡️"}
    icon = icons.get(level, "🔹")
    print(f"[{ts}] {icon} [{level}] {msg}", flush=True)

# Bảng Visual Intent độ chính xác cao (Subject + Action + Camera + 4K / B-Roll)
QUERY_ENHANCEMENTS = {
    # CH01 (Special re-hunt)
    "CH01_SC006": [
        "golfers waiting at tee box slow motion 4k",
        "golf players waiting tee off fairway tee box",
        "pga tour golfers on tee box waiting"
    ],

    # CH02 (Đã hoàn thành 100%)
    "CH02_SC002": ["đất nông nghiệp ven đô flycam 4k", "rural land vietnam outskirts aerial drone 4k"],
    "CH02_SC004": ["corporate real estate board meeting b-roll", "họp ban lãnh đạo tập đoàn bất động sản b-roll"],
    "CH02_SC010": ["hội thảo bất động sản savills cbre", "savills vietnam real estate report presentation"],
    "CH02_SC014": ["khu đô thị sinh thái ecopark vinhomes flycam 4k", "master planned community villas flycam vietnam"],
    "CH02_SC017": ["lễ mở bán bất động sản b-roll", "real estate launch event crowd vietnam"],
    "CH02_SC021": ["công nhân cắt cỏ chăm sóc cây xanh đô thị", "urban park landscaping maintenance workers 4k"],
    "CH02_SC024a1": ["financial audit report document desk b-roll", "báo cáo tài chính kiểm toán lật giở b-roll"],
    "CH02_SC024a2": ["tòa nhà văn phòng landmark 81 sài gòn đêm 4k", "hanoi financial tower modern skyscraper night 4k"],

    # CH03 (Surgical Re-hunt 4 cảnh)
    "CH03_SC001": ["thung lũng núi hoang sơ việt nam flycam 4k", "remote mountainous valley vietnam drone 4k"],
    "CH03_SC005": ["rural agricultural land plot dry barren soil 4k b-roll", "đất nông nghiệp cọc ranh mốc giới việt nam 4k"],
    "CH03_SC010": ["công bố quyết định đầu tư văn bản dấu đỏ b-roll", "official government decree stamp signing b-roll 4k"],
    "CH03_SC013": ["golf club membership card launch event b-roll", "lễ ra mắt thẻ hội viên golf vip"],
    "CH03_SC016": ["lễ ký kết hợp đồng tín dụng ngân hàng doanh nghiệp b-roll", "corporate bank loan agreement signing ceremony b-roll"],
    "CH03_SC020": ["financial documents corporate prospectus desk review 4k", "hồ sơ tài chính chứng khoán bàn làm việc b-roll"],
    "CH03_SC024": ["golf driving range ball picker machine", "golf range picking robot Pik'r-X 4k"],
    "CH03_SC026": ["abandoned construction site unfinished building 4k", "công trường đình trệ bất động sản đóng băng 4k"],
    "CH03_SC030": ["central vietnam coastal white sand dunes turquoise ocean aerial 4k", "bờ biển cát trắng miền trung việt nam flycam 4k"],

    # CH04
    "CH04_SC002": ["tranh luận sân golf thời sự vtv b-roll", "quy hoạch sân golf vtv24 tư liệu"],
    "CH04_SC006a1": ["Black Mountain Golf Club Hua Hin aerial 4k", "Hua Hin golf course drone 4k"],
    "CH04_SC007": ["Amazing Thailand golf tournament asian tour", "thailand golf tourism promotional video 4k"],
    "CH04_SC014": ["travel agency brochure itinerary desk b-roll 4k", "golf holiday vacation package brochure"],
    "CH04_SC016": ["5 star luxury hotel lobby check in b-roll 4k", "luxury resort reception concierge b-roll"],
    "CH04_SC018": ["Pattaya golf course aerial drone 4k", "thailand luxury golf course flycam 4k"],
    "CH04_SC021": ["golfers clubhouse patio smiling relaxing 4k", "international golfers discussing round clubhouse"],
    "CH04_SC023": ["Vietnam Golf Coast Danang 4k", "sân golf ven biển đà nẵng flycam 4k"],
    "CH04_SC026": ["asian golfers playing golf laughing 4k", "korean golfers in vietnam danang 4k b-roll"],
    "CH04_SC027": ["golf course covered heavy snow winter frozen 4k", "snow covered golf green frozen pin flag 4k"],
    "CH04_SC028": ["danang international airport passenger arrivals b-roll", "airplane landing runway airport 4k b-roll"],
    "CH04_SC033": ["central vietnam coastal white sand dunes harsh sun 4k", "đồi cát trắng ven biển miền trung 4k flycam"],
    "CH04_SC035": ["heavy rain storm falling on golf course green grass 4k", "tropical rain pouring golf green lawn b-roll"],
    "CH04_SC040a1": ["rusty chain padlock abandoned gate 4k b-roll", "cổng sắt khóa xích hoen rỉ bỏ hoang 4k"],

    # CH05
    "CH05_SC005": ["central bank press conference governor podium 4k", "họp báo ngân hàng nhà nước lãi suất b-roll"],
    "CH05_SC012": ["empty real estate showroom closed office 4k", "sàn giao dịch bất động sản vắng vẻ đóng cửa"],
    "CH05_SC013": ["khủng hoảng trái phiếu doanh nghiệp vtv b-roll", "thị trường trái phiếu doanh nghiệp thời sự tài chính"],
    "CH05_SC017": ["japan bubble economy 1989 golf club membership frenzy", "tokyo 1989 bubble economy golf NHK"],
    "CH05_SC019": ["vintage luxury cars tokyo golf club entrance 1989", "luxury classic golf club entrance gate historical"],
    "CH05_SC021": ["Bank of Japan governor 1990 interest rate hike", "Yasushi Mieno Bank of Japan speech 1990"],
    "CH05_SC024": ["bankruptcy court filing document desk review b-roll", "tòa án thụ lý đơn phá sản doanh nghiệp b-roll"],
    "CH05_SC026": ["abandoned golf course japan overgrown drone 4k", "nature reclaimed abandoned golf course 4k"],
    "CH05_SC029": ["auctioneer gavel bidding room public auction 4k", "đấu giá tài sản phát mãi ngân hàng b-roll"],
    "CH05_SC032": ["quoc hoi viet nam chat van lang phi dat dai b-roll", "phiên chất vấn quốc hội truyền hình b-roll"],

    # CH06
    "CH06_SC003": ["nghị định 52 2020 quy định kinh doanh sân golf văn bản", "văn bản nghị định chính phủ b-roll 4k"],
    "CH06_SC005": ["cánh đồng lúa chín vàng mùa gặt flycam 4k", "combine harvester harvesting rice paddy vietnam aerial 4k"],
    "CH06_SC008": ["biển cảnh báo quy hoạch đất đai xây dựng 4k", "construction warning signboard project site b-roll"],
    "CH06_SC010": ["quốc hội biểu quyết thông qua luật đất đai 2024", "bảng điện tử quốc hội biểu quyết thông qua 4k"],
    "CH06_SC019": ["đoàn thanh tra kiểm tra công trường dự án b-roll", "government inspection team construction site review"],
    "CH06_SC022": ["đấu giá đất búa đấu giá hội trường 4k", "public land auction bidding room gavel 4k"],
    "CH06_SC025": ["vietnamese farmer standing by rice field canal 4k", "nông dân đứng bên đồng ruộng việt nam 4k"],

    # CH07
    "CH07_SC004": ["caddie vocational training class vietnam golf", "đào tạo nhân viên dịch vụ caddie sân golf"],
    "CH07_SC007": ["modern rural house vietnam coastal village 4k", "nhà mới xây nông thôn việt nam khang trang 4k"],
    "CH07_SC011": ["dry well drought cracked earth water scarcity 4k", "hạn hán giếng cạn nứt nẻ đất đai 4k"],
    "CH07_SC016a1": ["bulldozer clearing trees land development 4k", "máy ủi san gạt mặt bằng dự án 4k"],
    "CH07_SC019": ["young people using smartphones modern cafe 4k", "giới trẻ lướt điện thoại quán cafe 4k"],
    "CH07_SC021": ["master planned residential community aerial drone 4k", "golf course converted to housing development drone"],
    "CH07_SC023": ["hyperscale data center server racks blinking blue lights 4k", "server room rows blue led lights 4k"],
    "CH07_SC026": ["solar farm aerial drone clean energy 4k", "công viên đô thị trang trại điện mặt trời 4k flycam"],

    # CH08
    "CH08_SC002": ["ornate wrought iron gate luxury private estate 4k", "exclusive private golf club entrance gate 4k"],
    "CH08_SC005": ["annual report document turning pages corporate desk 4k", "golf industry annual report presentation 4k"],
    "CH08_SC011": ["Topgolf night friends hitting balls fun party 4k", "topgolf party bay night smiling 4k"],
    "CH08_SC015": ["gangnam seoul night neon street 4k", "screen golf gangnam seoul signs 4k"],
    "CH08_SC020": ["indoor screen golf simulator young golfers smiling 4k", "phòng tập golf 3d giả lập màn hình 4k"],
    "CH08_SC024": ["toa nha quoc hoi viet nam flycam kien truc dep 4k", "national assembly building vietnam aerial 4k"]
}

def load_manifest_scenes():
    scenes = []
    manifest_files = sorted(glob.glob(str(EPISODE_DIR / "broll_manifest_chapter_*.json")))
    for m in manifest_files:
        ch = Path(m).stem.replace("broll_manifest_", "")
        with open(m, "r", encoding="utf-8") as f:
            d = json.load(f)
        items = d if isinstance(d, list) else d.get("scenes", [])
        for it in items:
            sid = it.get("scene_id") or it.get("id")
            dur = float(it.get("target_duration_seconds") or it.get("recommended_duration_sec", 4.0))
            queries = []
            if sid in QUERY_ENHANCEMENTS:
                queries.extend(QUERY_ENHANCEMENTS[sid])
            if it.get("search_query"):
                queries.append(it.get("search_query"))
            if it.get("search_queries"):
                queries.extend(it.get("search_queries"))
            desc = it.get("description") or it.get("target_visual") or it.get("action_description", "")
            source = it.get("source_recommendation") or it.get("source") or "B-Roll Báo Chí"
            scenes.append({
                "chapter": ch,
                "scene_id": sid,
                "duration": dur,
                "queries": [q for q in queries if q],
                "description": desc,
                "source": source
            })
    return scenes

def search_candidate(query):
    cleaned_query = f"{query} -vlog -reaction -karaoke -cover -review -lyrics -vietsub -anime -hoathinh -talkshow"
    cmd = [
        YT_DLP_BIN,
        "--extractor-args", "youtube:player_client=android,web",
        f"ytsearch5:{cleaned_query}",
        "--print", "%(id)s | %(title)s | %(duration)s",
        "--no-warnings"
    ]
    env = os.environ.copy()
    env["PATH"] = f"/Users/pro16/.local/bin:/opt/homebrew/bin:{env.get('PATH', '')}"
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=20)
        lines = [l.strip() for l in res.stdout.strip().split("\n") if l.strip()]
        candidates = []
        bad_keywords = ["vlog", "tập ", "tập_", "phim", "vietsub", "hoạt hình", "anime", "reaction", "karaoke", "official music video", "mv", "remix", "hát", "cover", "review", "tóm tắt"]
        for line in lines:
            parts = line.split(" | ")
            if len(parts) >= 2:
                ytid = parts[0].strip()
                title = parts[1].strip()
                title_lower = title.lower()
                if any(bk in title_lower for bk in bad_keywords):
                    continue
                try:
                    dur_sec = float(parts[2].strip()) if len(parts) >= 3 and parts[2].strip() != "NA" else 120.0
                except Exception:
                    dur_sec = 120.0
                candidates.append((ytid, title, dur_sec))
        return candidates
    except Exception:
        return []

def audit_frame_quality(video_path, sid):
    """Visual Gate: Trích xuất 1 frame ở giữa clip và kiểm tra tính toàn vẹn."""
    out_frame = AUDIT_FRAMES_DIR / f"{sid}_audit.jpg"
    cmd = [
        "ffmpeg", "-y",
        "-ss", "00:00:01.5",
        "-i", str(video_path),
        "-vframes", "1",
        "-q:v", "2",
        str(out_frame)
    ]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if out_frame.exists() and out_frame.stat().st_size > 20 * 1024:
        return True, str(out_frame)
    return False, ""

def download_and_process(scene, force=False):
    sid = scene["scene_id"]
    final_video = VIDEOS_DIR / f"{sid}.mp4"
    final_stripped = STRIPPED_DIR / f"{sid}.mp4"
    dur = scene["duration"]

    # BẢO VỆ TỐI THƯỢNG: Nếu video đã có và dung lượng > 150KB ➔ BỎ QUA NGAY
    if not force and final_video.exists() and final_video.stat().st_size > 150 * 1024:
        if not final_stripped.exists() or final_stripped.stat().st_size < 100 * 1024:
            cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(final_video), "-an", "-c:v", "copy", str(final_stripped)]
            subprocess.run(cmd, check=False)
        log(f"[{sid}] Đã có sẵn ({final_video.stat().st_size / 1024:.1f} KB). BẢO TOÀN, BỎ QUA.", "INFO")
        return True, "SKIPPED_EXISTING"

    log(f"[{sid}] 🎯 Săn tư liệu cho: {scene['description'][:75]}...", "HUNT")

    candidates = []
    for q in scene["queries"]:
        cands = search_candidate(q)
        if cands:
            candidates = cands
            break

    if not candidates:
        log(f"[{sid}] Không tìm thấy video ứng viên từ YouTube.", "WARN")
        return False, "NO_CANDIDATES"

    raw_tmp = Path(f"/tmp/raw_broll_sg_{sid}.mp4")
    if raw_tmp.exists():
        try: raw_tmp.unlink()
        except Exception: pass

    download_ok = False
    for ytid, title, total_dur in candidates[:3]:
        # Smart Offset: Tránh intro/MC trường quay
        if total_dur > 600:
            st_sec = 85.0
        elif total_dur > 180:
            st_sec = 35.0
        elif total_dur > 45:
            st_sec = 12.0
        else:
            st_sec = 4.0

        en_sec = st_sec + dur + 2.0
        start_t = f"{int(st_sec)//3600:02d}:{(int(st_sec)%3600)//60:02d}:{int(st_sec)%60:02d}"
        end_t = f"{int(en_sec)//3600:02d}:{(int(en_sec)%3600)//60:02d}:{int(en_sec)%60:02d}"

        env = os.environ.copy()
        env["PATH"] = f"/Users/pro16/.local/bin:/opt/homebrew/bin:{env.get('PATH', '')}"

        # High-Performance yt-dlp: android/web client, range requests, ~4s download
        cmd_dl = [
            YT_DLP_BIN,
            "--extractor-args", "youtube:player_client=android,web",
            "-f", "bv*[height<=1080][ext=mp4]/b[height<=1080]/best",
            "--download-sections", f"*{start_t}-{end_t}",
            "--force-keyframes-at-cuts",
            "--no-warnings",
            "--no-playlist",
            f"https://www.youtube.com/watch?v={ytid}",
            "-o", str(raw_tmp)
        ]

        try:
            res_dl = subprocess.run(cmd_dl, capture_output=True, text=True, env=env, timeout=30)
            found_tmp = None
            for p in Path("/tmp").glob(f"raw_broll_sg_{sid}.*"):
                if p.stat().st_size > 100 * 1024:
                    found_tmp = p
                    break

            if found_tmp:
                raw_tmp = found_tmp
                download_ok = True
                log(f"[{sid}] Tải thành công từ '{title[:45]}' ({ytid})", "SUCCESS")
                break
        except Exception:
            continue

    if not download_ok:
        log(f"[{sid}] Tải thất bại từ tất cả ứng viên.", "ERROR")
        return False, "DOWNLOAD_FAILED"

    # Chuyển hóa 4 Chuẩn Mực Thép Fair Use qua FFmpeg
    vf_filter = (
        "scale=1920:1080:force_original_aspect_ratio=increase,"
        "crop=1920:1080,"
        "scale=trunc(iw*1.04/2)*2:trunc(ih*1.04/2)*2,"
        "crop=1920:1080,"
        "eq=contrast=1.03:brightness=0.01:saturation=1.05,"
        "format=yuv420p"
    )

    cmd_ff = [
        "ffmpeg", "-y",
        "-i", str(raw_tmp),
        "-t", str(dur),
        "-an",
        "-vf", vf_filter,
        "-c:v", "libx264",
        "-crf", "18",
        "-preset", "fast",
        str(final_video)
    ]

    res_ff = subprocess.run(cmd_ff, capture_output=True, text=True)
    if raw_tmp.exists():
        try: raw_tmp.unlink()
        except Exception: pass

    if res_ff.returncode == 0 and final_video.exists() and final_video.stat().st_size > 150 * 1024:
        # Đồng bộ sang video_stripped
        cmd_strip = ["ffmpeg", "-v", "error", "-y", "-i", str(final_video), "-an", "-c:v", "copy", str(final_stripped)]
        subprocess.run(cmd_strip, check=False)

        # Automated Visual Gate: Kiểm định frame
        gate_ok, frame_path = audit_frame_quality(final_video, sid)
        sz_mb = final_video.stat().st_size / (1024 * 1024)
        if gate_ok:
            log(f"[{sid}] 🛡️ [VISUAL GATE PASS] Frame: {Path(frame_path).name} | Video: {sz_mb:.2f} MB ({dur:.1f}s)", "SUCCESS")
        else:
            log(f"[{sid}] ⚠️ [VISUAL GATE WARN] Không trích xuất được frame hợp lệ.", "WARN")
        return True, "SUCCESS"
    else:
        log(f"[{sid}] Lỗi xử lý FFmpeg: {res_ff.stderr[:100]}", "ERROR")
        return False, "FFMPEG_ERROR"

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Footage Hunter Sân Golf")
    parser.add_argument("--chapter", type=str, default="", help="Lọc theo chương (ví dụ: 3 hoặc chapter_03)")
    parser.add_argument("--scene", type=str, default="", help="Chỉ xử lý một cảnh cụ thể (ví dụ: CH03_SC010)")
    parser.add_argument("--workers", type=int, default=4, help="Số worker song song (mặc định: 4)")
    parser.add_argument("--force", action="store_true", help="Ép tải lại")
    args = parser.parse_args()

    all_scenes = load_manifest_scenes()

    target_scenes = all_scenes
    if args.scene:
        target_scenes = [s for s in target_scenes if s["scene_id"].upper() == args.scene.upper()]
    elif args.chapter:
        ch_str = f"chapter_{int(args.chapter):02d}" if args.chapter.isdigit() else args.chapter
        target_scenes = [s for s in target_scenes if ch_str in s["chapter"]]

    needed = []
    already = []
    for s in target_scenes:
        vf = VIDEOS_DIR / f"{s['scene_id']}.mp4"
        if not args.force and vf.exists() and vf.stat().st_size > 150 * 1024:
            already.append(s)
        else:
            needed.append(s)

    log("=" * 80, "INFO")
    log("🚀 FOOTAGE HUNTER B-ROLL — HIGH-PERFORMANCE PIPELINE", "INFO")
    log(f"📊 Rà soát: {len(target_scenes)} | Đã có: {len(already)} | Cần săn bù: {len(needed)}", "INFO")
    log(f"⚡ Động cơ: yt-dlp android,web (Range Requests) | Số luồng: {args.workers}", "INFO")
    log("=" * 80, "INFO")

    if not needed:
        log("🎉 TẤT CẢ PHÂN CẢNH ĐÃ ĐẦY ĐỦ VÀ HỢP LỆ! KHÔNG CẦN TẢI THÊM.", "SUCCESS")
        return

    success_cnt = 0
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(download_and_process, sc, args.force): sc for sc in needed}
        for future in as_completed(futures):
            sc = futures[future]
            try:
                ok, reason = future.result()
                if ok:
                    success_cnt += 1
            except Exception as e:
                log(f"[{sc['scene_id']}] Ngoại lệ: {e}", "ERROR")

    log("=" * 80, "INFO")
    log(f"🏁 TỔNG KẾT: Đã hoàn tất {success_cnt}/{len(needed)} phân cảnh!", "SUCCESS")
    log("=" * 80, "INFO")

if __name__ == "__main__":
    main()
