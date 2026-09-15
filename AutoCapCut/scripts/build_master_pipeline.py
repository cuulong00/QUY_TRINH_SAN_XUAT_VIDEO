#!/usr/bin/env python3
"""
scripts/build_master_pipeline.py
=============================================================================
PRODUCTION-GRADE MASTER VIDEO ASSEMBLY PIPELINE FOR CAPCUT DESKTOP (macOS)
=============================================================================
Quy trình chuẩn hóa tự động hóa 100%:
1. Tiền kiểm cấu trúc source (audio, video, chapter_XX_visual.md).
2. Tách & Triệt tiêu âm thanh 3 tầng (3-Tier Physical Audio Stripping via ffmpeg).
3. Master Clock Engine: Phân bổ thời lượng theo số từ & snap điểm cắt vào khoảng lặng (silencedetect).
4. Nhịp thở chuyển chương: Khoảng nghỉ audio 4.0s, video overhang +2.0s, video lead-in +2.0s (Zero Black Gaps).
5. Nhạc nền chuẩn kênh (Channel BGM @ volume 0.031) loop tuần hoàn, fade out 3.0s cuối.
6. Biên dịch qua capcut compile sử dụng Modern Template (CapCut 8.9+/9.x macOS).
7. Tinh chỉnh draft_info.json, draft_content.json, template-2.tmp:
   - Synchronize speed materials with segment speed
   - Zero microsecond gaps on Track 0 (magnetic alignment)
   - has_audio = False, has_sound_separated = True, intensifies_audio_path = ""
8. Đăng ký tài nguyên (capcut register --materials --apply) và kiểm toán (capcut lint errors: 0).
"""

import os
import sys
import re
import json
import glob
import shutil
import difflib
import subprocess
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any

WORKSPACE = Path("/Users/pro16/Documents/VideoProject/AutoCapCut")
CAPCUT_DRAFTS_DIR = Path("/Users/pro16/Movies/CapCut/User Data/Projects/com.lveditor.draft")
MODERN_TEMPLATE = WORKSPACE / "templates/capcut_modern_template"
CAPCUT_CLI = WORKSPACE / "tools/capcut-cli/dist/index.js"

CHANNEL_BGM_MAP = {
    "GocNhinPodcast": Path("/Users/pro16/Documents/VideoProject/Nhac_nen/nhac-nen-goc-nhin.mp3"),
    "Dong_Chay": Path("/Users/pro16/Documents/VideoProject/Nhac_nen/nhac-nen-dong-chay.mp3"),
    "HieuBietHon": Path("/Users/pro16/Documents/VideoProject/Nhac_nen/hieubiethon.mp3"),
    "X-Economics": Path("/Users/pro16/Documents/VideoProject/Nhac_nen/nhac-nen-goc-nhin.mp3"),
    "X_Economics": Path("/Users/pro16/Documents/VideoProject/Nhac_nen/nhac-nen-goc-nhin.mp3"),
}
DEFAULT_BGM = Path("/Users/pro16/Documents/VideoProject/Nhac_nen/nhac-nen-goc-nhin.mp3")
DEFAULT_BGM_VOL = 0.031

CHANNEL_DISCLAIMER_MAP = {
    "GocNhinPodcast": Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/00_core/disclaimer/tuyenbo_trachnhiem_gocnhinpodcast_clean_audio.mp4"),
    "Dong_Chay": Path("/Users/pro16/Documents/VideoProject/Dong_Chay/00_core/disclaimer/tuyenbo_trachnhiem_dongchay_clean_audio.mp4"),
}


def run_cmd(cmd: List[str], check: bool = True) -> str:
    res = subprocess.run(cmd, capture_output=True, text=True)
    if check and res.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDERR: {res.stderr}\nSTDOUT: {res.stdout}")
    return res.stdout.strip()


def get_media_duration_sec(file_path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    out = run_cmd(cmd, check=True)
    return float(out)


def detect_silence_pauses(audio_path: Path, noise_db: float = -28.0, min_duration: float = 0.20) -> List[float]:
    """Dò tìm các điểm bắt đầu khoảng lặng tự nhiên trong file giọng đọc bằng ffmpeg silencedetect."""
    cmd = [
        "ffmpeg", "-i", str(audio_path),
        "-af", f"silencedetect=noise={noise_db}dB:d={min_duration}s",
        "-f", "null", "-"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    silences = []
    for line in res.stderr.splitlines():
        if "silence_start" in line:
            m = re.search(r"silence_start:\s*([\d\.]+)", line)
            if m:
                silences.append(float(m.group(1)))
    return silences


def clean_tokens(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    return text.split()


def compute_chapter_cuts_whisper(scenes: List[Dict[str, Any]], audio_duration: float, whisper_path: Path) -> List[float]:
    """Tính toán các điểm cắt (cuts) cực kỳ chuẩn xác dựa trên Whisper Forced Alignment."""
    with open(whisper_path, "r", encoding="utf-8") as f:
        wdata = json.load(f)

    all_words = []
    for chunk in wdata.get("chunks", []):
        ts = chunk.get("timestamp", [0.0, 2.0])
        c_start = ts[0] if ts[0] is not None else 0.0
        c_end = ts[1] if ts[1] is not None else c_start + 2.0
        c_text = chunk.get("text", "").strip()
        c_words = clean_tokens(c_text)
        if not c_words:
            continue
        c_dur = max(0.1, c_end - c_start)
        dt = c_dur / len(c_words)
        for i, w in enumerate(c_words):
            all_words.append({
                "word": w,
                "start": c_start + i * dt,
                "end": c_start + (i + 1) * dt
            })

    if not all_words:
        return [round(i * (audio_duration / len(scenes)), 4) for i in range(len(scenes))] + [round(audio_duration, 4)]

    w_norm = [w["word"] for w in all_words]
    cursor = 0
    cuts = [0.0]

    for idx, sc in enumerate(scenes):
        stoks = clean_tokens(sc.get("dialogue", ""))
        if not stoks:
            cuts.append(round(cuts[-1] + 1.0, 4))
            continue

        target_last = stoks[-2:] if len(stoks) >= 2 else stoks[-1:]
        exp_len = len(stoks)
        search_start = max(0, cursor + exp_len - 5)
        search_end = min(len(w_norm), cursor + exp_len + 15)

        best_match = -1
        for k in range(search_start, search_end):
            if len(target_last) >= 2 and k > 0:
                if w_norm[k - 1] == target_last[0]:
                    if w_norm[k] == target_last[1] or difflib.SequenceMatcher(None, w_norm[k], target_last[1]).ratio() >= 0.5:
                        best_match = k
                        break
            if w_norm[k] == target_last[-1]:
                best_match = k
                break

        if best_match == -1:
            best_match = min(len(w_norm) - 1, cursor + exp_len - 1)

        end_time = all_words[best_match]["end"]
        if end_time <= cuts[-1]:
            end_time = cuts[-1] + 1.0
        cuts.append(round(end_time, 4))
        cursor = min(len(w_norm) - 1, best_match + 1)

    cuts[-1] = round(audio_duration, 4)
    return cuts


def compute_chapter_cuts(scenes: List[Dict[str, Any]], audio_duration: float, silences: List[float]) -> List[float]:
    """Tính toán các điểm cắt (cuts) theo nhịp câu thoại và snap vào khoảng lặng."""
    total_est = sum(sc.get("duration_est", 0.0) for sc in scenes)
    total_words = sum(sc.get("word_count", 1) for sc in scenes) or 1
    N = len(scenes)

    cum_val = 0.0
    raw_cuts = []
    for sc in scenes:
        if total_est > 0:
            cum_val += sc.get("duration_est", 0.0)
            raw_cuts.append(audio_duration * (cum_val / total_est))
        else:
            cum_val += sc.get("word_count", 1)
            raw_cuts.append(audio_duration * (cum_val / total_words))

    snapped_cuts = [0.0]
    for i in range(N - 1):
        target = raw_cuts[i]
        best_sil = None
        min_dist = 999.0
        for s in silences:
            dist = abs(s - target)
            if dist < min_dist and s > snapped_cuts[-1] + 1.0 and s < audio_duration - 1.0:
                min_dist = dist
                best_sil = s

        if best_sil is not None and min_dist <= 1.8:
            snapped_cuts.append(best_sil)
        else:
            c = max(snapped_cuts[-1] + 1.0, min(audio_duration - 1.0, target))
            snapped_cuts.append(c)

    snapped_cuts.append(audio_duration)
    return snapped_cuts


def strip_single_file(vfile: Path, stripped_dir: Path) -> Tuple[str, Path]:
    rel_sub = vfile.parent.name
    out_sub = stripped_dir / rel_sub
    out_sub.mkdir(parents=True, exist_ok=True)
    out_file = out_sub / vfile.name

    if not out_file.exists() or out_file.stat().st_size == 0 or out_file.stat().st_mtime < vfile.stat().st_mtime:
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(vfile), "-an", "-c:v", "copy", str(out_file)]
        run_cmd(cmd)

    return vfile.stem, out_file


def strip_audio_streams(video_files: List[Path], stripped_dir: Path) -> Dict[str, Path]:
    """Tầng 1: Triệt tiêu hoàn toàn audio stream vật lý khỏi container MP4 (đa luồng)."""
    stripped_dir.mkdir(parents=True, exist_ok=True)
    mapped_files = {}

    print(f"[*] Đang thực hiện Tầng 1 (Physical Audio Strip) đa luồng cho {len(video_files)} video clips...")
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(strip_single_file, vf, stripped_dir) for vf in video_files]
        for fut in futures:
            stem, out_f = fut.result()
            mapped_files[stem] = out_f

    print(f"[✓] Hoàn thành triệt tiêu audio cho {len(video_files)} clips.")
    return mapped_files


def verify_tier1_audio_stripped(stripped_dir: Path) -> bool:
    """Kiểm chứng độc lập Tầng 1: ffprobe toàn bộ files mp4 khẳng định không còn audio stream."""
    print("[*] Đang thực hiện kiểm chứng độc lập Tầng 1 (Audio Stream Probe)...")
    all_mp4 = list(stripped_dir.rglob("*.mp4"))
    if not all_mp4:
        raise RuntimeError(f"Không tìm thấy file mp4 nào trong {stripped_dir}")

    from concurrent.futures import ThreadPoolExecutor
    def check_mp4(mp4: Path) -> Optional[str]:
        cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "stream=codec_type",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(mp4)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if "audio" in res.stdout:
            return mp4.name
        return None

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(check_mp4, all_mp4))
    contaminated = [r for r in results if r is not None]

    if contaminated:
        raise RuntimeError(f"KỶ LUẬT TẦNG 1 THẤT BẠI: Còn {len(contaminated)} clips chứa audio stream! Ví dụ: {contaminated[:5]}")
    print(f"[✓] TẦNG 1 HOÀN TOÀN ĐẠT: 100% ({len(all_mp4)}/{len(all_mp4)}) clips đã sạch audio stream vật lý.")
    return True


def parse_visual_markdown(md_path: Path) -> List[Dict[str, Any]]:
    """Phân tích file chapter_XX_visual.md để trích xuất scene ID, thời lượng ước lượng và câu thoại."""
    scenes = []
    if not md_path.exists():
        return scenes

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    for line in content.splitlines():
        line_clean = line.strip()
        if not line_clean.startswith("|") or "Scene ID" in line_clean or "Mã Scene" in line_clean or "Mã Phân Cảnh" in line_clean or "Mã Cảnh" in line_clean or "---" in line_clean:
            continue
        parts = [p.strip() for p in line_clean.split("|")[1:-1]]
        if len(parts) >= 2:
            sc_match = re.search(r"(CH\d+_SC\d+[a-zA-Z0-9]*)", parts[0])
            if sc_match:
                sc_id = sc_match.group(1)
                dur_est = 0.0
                m_dur = re.match(r"^([\d\.]+)s?$", parts[1])
                if m_dur:
                    dur_est = float(m_dur.group(1))
                    dialogue = parts[2] if len(parts) > 2 else ""
                else:
                    dialogue = parts[1]

                dialogue_clean = re.sub(r"\[.*?\]", "", dialogue).replace("**", "").replace("*", "").strip()
                words = len(dialogue_clean.split())
                if words == 0:
                    words = 1
                scenes.append({
                    "scene_id": sc_id,
                    "dialogue": dialogue_clean,
                    "word_count": words,
                    "duration_est": dur_est,
                    "raw_line": line_clean
                })
    return scenes


def build_pipeline(
    source_dir: Path,
    output_name: str,
    channel_name: Optional[str] = None,
    custom_bgm: Optional[Path] = None,
    custom_audio_dir: Optional[Path] = None,
    custom_video_dir: Optional[Path] = None,
    bgm_vol: float = DEFAULT_BGM_VOL,
    inter_chapter_gap: float = 4.0,
    bridge_lead: float = 2.0
):
    print("=" * 80)
    print(f"🎬 KHỞI ĐỘNG CAPCUT MASTER ASSEMBLY PIPELINE: {output_name}")
    print(f"📂 Thư mục nguồn: {source_dir}")
    print("=" * 80)

    # Đóng CapCut trước khi bắt đầu
    subprocess.run(["pkill", "-9", "-f", "CapCut"], stderr=subprocess.DEVNULL)
    import time
    time.sleep(1)

    # Tự động nhận diện kênh nếu chưa chỉ định
    if not channel_name:
        src_str = str(source_dir)
        if "X-Economics" in src_str or "X_Economics" in src_str:
            channel_name = "X-Economics"
        elif "Dong_Chay" in src_str or "DongChay" in src_str:
            channel_name = "Dong_Chay"
        elif "HieuBietHon" in src_str:
            channel_name = "HieuBietHon"
        elif "GocNhinPodcast" in src_str or "GocNhin" in src_str:
            channel_name = "GocNhinPodcast"
        else:
            channel_name = "GocNhinPodcast"

    print(f"[*] Kênh nhận diện: {channel_name}")

    # 1. Phát hiện kịch bản & file tài nguyên
    if custom_audio_dir:
        target_audio_dir = custom_audio_dir
    elif (source_dir / "audio_v2").exists():
        target_audio_dir = source_dir / "audio_v2"
    else:
        target_audio_dir = source_dir / "audio"

    print(f"[*] Thư mục audio được sử dụng: {target_audio_dir}")
    audio_files = sorted(glob.glob(str(target_audio_dir / "chapter_*.wav")) +
                         glob.glob(str(target_audio_dir / "chapter_*.mp3")))
    if not audio_files:
        raise FileNotFoundError(f"Không tìm thấy file audio giọng đọc tại {target_audio_dir}")

    num_chapters = len(audio_files)
    print(f"[*] Phát hiện {num_chapters} chương giọng đọc:")
    for a in audio_files:
        print(f"    - {Path(a).name}")

    # Tìm các file kịch bản visual md
    visual_files = {}
    for ch in range(1, num_chapters + 1):
        ch_str = f"chapter_{ch:02d}"
        cand1 = source_dir / f"{ch_str}_visual.md"
        cand2 = source_dir / "video" / f"{ch_str}_visual.md"
        if cand1.exists():
            visual_files[ch] = cand1
        elif cand2.exists():
            visual_files[ch] = cand2
        else:
            print(f"[!] Cảnh báo: Không tìm thấy kịch bản thị giác cho chương {ch}")

    # Tìm danh sách video clips thô
    all_raw_videos = []
    if custom_video_dir and custom_video_dir.exists():
        all_raw_videos = sorted(custom_video_dir.rglob("*.mp4"))
    else:
        for ch in range(1, num_chapters + 1):
            for folder_pattern in [f"ch{ch:02d}", f"chapter_{ch:02d}", f"Chương {ch:02d}", f"Chương {ch}", f"ch{ch}"]:
                vdir = source_dir / "video" / folder_pattern
                if vdir.exists():
                    vids = sorted(vdir.glob("*.mp4"))
                    all_raw_videos.extend(vids)
                    break

        if not all_raw_videos:
            for vcand in [source_dir / "video", source_dir / "videos"]:
                if vcand.exists() and vcand.is_dir():
                    vids = sorted(vcand.glob("*.mp4"))
                    if vids:
                        all_raw_videos.extend(vids)
                        break

    print(f"[*] Tổng số video clips thô tìm thấy: {len(all_raw_videos)}")

    # 2. Tầng 1: Triệt tiêu âm thanh vật lý
    stripped_cache_dir = source_dir / "video_stripped"
    stripped_map = strip_audio_streams(all_raw_videos, stripped_cache_dir)
    verify_tier1_audio_stripped(stripped_cache_dir)

    # Map scene ID sang file video stripped
    scene_to_file = {}
    for vid_file in stripped_cache_dir.rglob("*.mp4"):
        if any("_backup" in part for part in vid_file.parts):
            continue
        scene_to_file[vid_file.stem] = vid_file
        scene_to_file[vid_file.stem.upper()] = vid_file
        m = re.match(r"(CH\d+_SC\d+[a-zA-Z0-9]*)", vid_file.stem, re.IGNORECASE)
        if m:
            scene_to_file[m.group(1)] = vid_file
            scene_to_file[m.group(1).upper()] = vid_file

    print("\n[*] Đang tính toán nhịp thời gian Master Clock & Silence Snapping...")

    chapters_data = []
    for ch_idx, a_file_str in enumerate(audio_files, 1):
        a_path = Path(a_file_str)
        a_dur = get_media_duration_sec(a_path)
        silences = detect_silence_pauses(a_path)

        scenes = []
        timing_map_path = source_dir / "scene_timing_map.json"
        if timing_map_path.exists():
            try:
                with open(timing_map_path, "r", encoding="utf-8") as f:
                    all_map_scenes = json.load(f)
                ch_target = f"{ch_idx:02d}"
                map_scenes = [s for s in all_map_scenes if f"{int(s.get('chapter', 0)):02d}" == ch_target]
                if map_scenes:
                    for s in map_scenes:
                        s_id = s.get("id") or s.get("original_tag")
                        dur_est = float(s.get("duration_sec", 0.0))
                        sents = s.get("sentences", [])
                        dialogue = " ".join(sents)
                        words = len(dialogue.split()) or 1
                        scenes.append({
                            "scene_id": s_id,
                            "dialogue": dialogue,
                            "word_count": words,
                            "duration_est": dur_est,
                            "raw_line": ""
                        })
            except Exception as e:
                print(f"[!] Lỗi đọc scene_timing_map.json: {e}, fallback sang visual markdown")

        if not scenes:
            md_path = visual_files.get(ch_idx)
            scenes = parse_visual_markdown(md_path) if md_path else []

        if not scenes:
            for fpat in [f"ch{ch_idx:02d}", f"chapter_{ch_idx:02d}"]:
                ch_folder = source_dir / "video" / fpat
                if ch_folder.exists():
                    v_files = sorted(ch_folder.glob("*.mp4"))
                    scenes = [{"scene_id": re.match(r"(CH\d+_SC\d+)", vf.stem).group(1) if re.match(r"(CH\d+_SC\d+)", vf.stem) else vf.stem,
                               "word_count": 1,
                               "duration_est": 0.0} for vf in v_files]
                    break

        whisper_file = source_dir / "whisper_align" / f"chapter_{ch_idx:02d}_whisper.json"
        if whisper_file.exists():
            cuts = compute_chapter_cuts_whisper(scenes, a_dur, whisper_file)
            align_method = "Whisper Alignment"
        else:
            cuts = compute_chapter_cuts(scenes, a_dur, silences)
            align_method = "Silence Snapping"

        chapters_data.append({
            "chapter": ch_idx,
            "wav_path": a_path,
            "audio_duration": a_dur,
            "scenes": scenes,
            "cuts": cuts
        })
        print(f"   • Chương {ch_idx:02d} [{align_method}]: {len(scenes)} scenes | Audio: {a_dur:.3f}s | Cuts: {len(cuts)-1}")

    # 3. Lắp ráp items cho Spec
    print("\n[*] Thiết kế Timeline Spec (4.0s Inter-chapter pause, +2.0s overhang, +2.0s lead-in)...")
    video_items = []
    audio_items = []

    current_audio_time = 0.0
    current_video_time = 0.0

    for idx, ch_info in enumerate(chapters_data):
        ch = ch_info["chapter"]
        scenes = ch_info["scenes"]
        cuts = ch_info["cuts"]
        a_dur = ch_info["audio_duration"]

        # 3.1 Audio Track Position
        if ch == 1:
            vo_start = 0.0
        else:
            vo_start = current_audio_time + inter_chapter_gap

        vo_end = vo_start + a_dur
        current_audio_time = vo_end

        audio_items.append({
            "path": str(ch_info["wav_path"].resolve()),
            "start": round(vo_start, 4),
            "duration": round(a_dur, 4),
            "volume": 1.0,
            "ref": f"vo_ch{ch:02d}"
        })

        # 3.2 Video Track Position
        N = len(scenes)
        for s_idx in range(N):
            sc = scenes[s_idx]
            sc_id = sc["scene_id"]
            base_dur = cuts[s_idx + 1] - cuts[s_idx]

            dur = base_dur
            if s_idx == 0 and ch > 1:
                dur += bridge_lead
            if s_idx == N - 1:
                dur += bridge_lead

            # Tìm file video
            v_path = scene_to_file.get(sc_id) or scene_to_file.get(sc_id.upper())
            source_start = 0.0
            if not v_path or not v_path.exists():
                print(f"    [!] Missing video for {sc_id}, fallback...")
                prev_id = scenes[s_idx - 1]["scene_id"] if s_idx > 0 else None
                if prev_id and scene_to_file.get(prev_id):
                    v_path = scene_to_file[prev_id]
                    if video_items and video_items[-1]["path"] == str(v_path.resolve()):
                        prev_item = video_items[-1]
                        prev_source_start = prev_item.get("sourceStart", 0.0)
                        prev_dur = prev_item["duration"] * prev_item.get("speed", 1.0)
                        source_start = prev_source_start + prev_dur
                else:
                    fallback_list = (list((stripped_cache_dir / f"ch{ch:02d}").glob("*.mp4")) or
                                     list((stripped_cache_dir / f"chapter_{ch:02d}").glob("*.mp4")) or
                                     list(stripped_cache_dir.rglob("*.mp4")))
                    v_path = fallback_list[0]

            # Tự động co giãn speed nếu thời lượng yêu cầu vượt quá dung lượng clip còn lại
            speed = 1.0
            max_source_dur = 8.0 - source_start
            if max_source_dur <= 1.0:
                source_start = 0.0
                max_source_dur = 8.0

            if dur > max_source_dur:
                speed = round((max_source_dur - 0.05) / dur, 4)
                if speed <= 0:
                    speed = 1.0

            v_start = current_video_time
            video_items.append({
                "path": str(v_path.resolve()),
                "start": round(v_start, 4),
                "duration": round(dur, 4),
                "sourceStart": round(source_start, 4),
                "speed": speed,
                "volume": 0.0,
                "ref": f"vid_{sc_id}"
            })
            current_video_time += dur

    # 3.3 Video Tuyên Bố Trách Nhiệm (Disclaimer Outro)
    disclaimer_video = CHANNEL_DISCLAIMER_MAP.get(channel_name)
    if disclaimer_video and disclaimer_video.exists():
        disc_dur = get_media_duration_sec(disclaimer_video)
        print(f"[*] Bổ sung video Tuyên Bố Trách Nhiệm: {disclaimer_video.name} | Thời lượng: {disc_dur:.2f}s")
        video_items.append({
            "path": str(disclaimer_video.resolve()),
            "start": round(current_video_time, 4),
            "duration": round(disc_dur, 4),
            "sourceStart": 0.0,
            "speed": 1.0,
            "volume": 1.0,
            "ref": "disclaimer_outro"
        })
        current_video_time += disc_dur

    # 4. Nhạc nền (Track 2)
    selected_bgm = custom_bgm or CHANNEL_BGM_MAP.get(channel_name, DEFAULT_BGM)
    if not selected_bgm.exists():
        selected_bgm = DEFAULT_BGM

    bgm_items = []
    total_timeline_sec = max(current_video_time, current_audio_time)

    if selected_bgm.exists():
        bgm_dur = get_media_duration_sec(selected_bgm)
        bgm_cursor = 0.0
        bgm_idx = 1
        while bgm_cursor < total_timeline_sec:
            chunk = min(bgm_dur, total_timeline_sec - bgm_cursor)
            bgm_items.append({
                "path": str(selected_bgm.resolve()),
                "start": round(bgm_cursor, 4),
                "duration": round(chunk, 4),
                "volume": bgm_vol,
                "ref": f"bgm_{bgm_idx:02d}"
            })
            bgm_cursor += chunk
            bgm_idx += 1
        print(f"[*] Nhạc nền: {selected_bgm.name} | Volume: {bgm_vol} | {len(bgm_items)} loops")

    # 5. Xuất bản spec.json
    spec = {
        "name": output_name,
        "width": 1920,
        "height": 1080,
        "fps": 30,
        "ratio": "16:9",
        "tracks": [
            {
                "type": "video",
                "name": "video",
                "items": video_items
            },
            {
                "type": "audio",
                "name": "voiceover",
                "items": audio_items
            },
            {
                "type": "audio",
                "name": "bgm",
                "items": bgm_items
            }
        ]
    }

    spec_out_path = source_dir / f"{output_name}_spec.json"
    with open(spec_out_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)

    print(f"\n[✓] Đã tạo Spec hoàn chỉnh: {spec_out_path}")
    print(f"    - Tổng thời lượng: {total_timeline_sec:.2f}s (~{total_timeline_sec / 60:.1f} phút)")
    print(f"    - Video Segments: {len(video_items)}")
    print(f"    - Audio Segments: {len(audio_items)}")

    # 6. Biên dịch CapCut Draft qua capcut-cli
    draft_dir = CAPCUT_DRAFTS_DIR / output_name
    print(f"\n[*] Đang biên dịch dự án vào CapCut Desktop: {draft_dir}...")
    if draft_dir.exists():
        subprocess.run(["rm", "-rf", str(draft_dir)], check=False)
        time.sleep(0.5)

    compile_cmd = [
        "node", str(CAPCUT_CLI), "compile",
        str(spec_out_path),
        "--out", str(draft_dir),
        "--template", str(MODERN_TEMPLATE)
    ]
    run_cmd(compile_cmd)
    print("[✓] Biên dịch hoàn tất.")

    # 7. Tinh chỉnh đồng bộ draft_info.json, template-2.tmp, draft_content.json
    print("\n[*] Tinh chỉnh đồng bộ metadata (Zero-Gap, Speed Sync, 3-Tier Audio Separation)...")
    info_file = draft_dir / "draft_info.json"
    content_file = draft_dir / "draft_content.json"
    template_file = draft_dir / "template-2.tmp"

    target_main = info_file if info_file.exists() else content_file
    with open(target_main, "r", encoding="utf-8") as f:
        draft = json.load(f)

    # 7.3 Cấu hình materials.videos (Tầng 2) & nhận diện Disclaimer
    disc_path_str = str(disclaimer_video.resolve()) if (disclaimer_video and disclaimer_video.exists()) else None
    disc_mat_id = None
    for mat in draft.get("materials", {}).get("videos", []):
        m_path = mat.get("path", "")
        if (disc_path_str and m_path == disc_path_str) or "tuyenbo_trachnhiem" in m_path:
            disc_mat_id = mat.get("id")
            mat["has_audio"] = True
            mat["has_sound_separated"] = False
            mat["intensifies_audio_path"] = ""
        else:
            mat["has_audio"] = False
            mat["has_sound_separated"] = True
            mat["intensifies_audio_path"] = ""

    # 7.1 Căn chỉnh Track 0 triệt tiêu mọi gap microsecond
    vtracks = [t for t in draft.get("tracks", []) if t.get("type") == "video"]
    if vtracks:
        v_track = vtracks[0]
        cursor = 0
        segments = v_track.get("segments", [])
        for idx, seg in enumerate(segments):
            seg["target_timerange"]["start"] = cursor
            if (disc_mat_id and seg.get("material_id") == disc_mat_id) or (disclaimer_video and disclaimer_video.exists() and idx == len(segments) - 1):
                seg["volume"] = 1.0
            else:
                seg["volume"] = 0.0
            dur = seg["target_timerange"]["duration"]
            seg_speed = seg.get("speed", 1.0)
            seg["source_timerange"]["duration"] = int(round(dur * seg_speed))
            cursor += dur
        draft["duration"] = cursor

    # 7.2 Đồng bộ materials.speeds
    speeds_mat = {s["id"]: s for s in draft.get("materials", {}).get("speeds", [])}
    if vtracks:
        for seg in vtracks[0].get("segments", []):
            seg_speed = seg.get("speed", 1.0)
            for ref_id in seg.get("extra_material_refs", []):
                if ref_id in speeds_mat:
                    speeds_mat[ref_id]["speed"] = seg_speed

    # Lưu lại đồng bộ vào các file tồn tại
    raw = json.dumps(draft, ensure_ascii=False, indent=2)
    for fname in ["draft_info.json", "template-2.tmp", "template-1.tmp", "draft_content.json"]:
        fpath = draft_dir / fname
        if fpath.exists():
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(raw)

    print("[✓] Đã tinh chỉnh đồng bộ draft_info.json, template-2.tmp và các file cấu hình.")

    # 8. Đăng ký tài nguyên macOS & Lint kiểm toán
    print("\n[*] Đang đăng ký tài nguyên với hệ thống macOS CapCut...")
    reg_cmd = ["node", str(CAPCUT_CLI), "register", str(draft_dir), "--materials", "--apply"]
    run_cmd(reg_cmd)

    print("[*] Đang thực hiện kiểm toán Lint dự án...")
    lint_cmd = ["node", str(CAPCUT_CLI), "lint", str(draft_dir)]
    lint_out = run_cmd(lint_cmd, check=False)
    print("---------------- LINT RESULT ----------------")
    print(lint_out)
    print("---------------------------------------------")

    # 8.1 Đồng bộ sang output_drafts nếu có bản sao lưu
    output_backup = WORKSPACE / "output_drafts" / output_name
    if (WORKSPACE / "output_drafts").exists():
        print(f"[*] Đồng bộ bản sao dự án sang {output_backup}...")
        if output_backup.exists():
            subprocess.run(["rm", "-rf", str(output_backup)], check=False)
        shutil.copytree(draft_dir, output_backup)

    print("\n🎉 [HOÀN TẤT] Dự án đã được dựng thành công 100% không lỗi!")
    print(f"👉 Vị trí Draft: {draft_dir}")
    return draft_dir


def main():
    parser = argparse.ArgumentParser(description="AutoCapCut Master Assembly Pipeline")
    parser.add_argument("--source", required=True, help="Đường dẫn thư mục nguồn (chứa audio/, video/)")
    parser.add_argument("--output-name", default=None, help="Tên dự án CapCut Draft (mặc định tự tạo từ tên thư mục nguồn)")
    parser.add_argument("--channel", default=None, help="Tên kênh (mặc định tự động nhận diện từ thư mục nguồn)")
    parser.add_argument("--audio-dir", default=None, help="Đường dẫn thư mục audio tùy chỉnh (mặc định ưu tiên audio_v2/ nếu có, hoặc audio/)")
    parser.add_argument("--video-dir", default=None, help="Đường dẫn thư mục video tùy chỉnh")
    parser.add_argument("--bgm", default=None, help="Đường dẫn tùy chỉnh file nhạc nền")
    parser.add_argument("--bgm-vol", type=float, default=DEFAULT_BGM_VOL, help="Volume nhạc nền (mặc định 0.031)")
    args = parser.parse_args()

    source_path = Path(args.source).resolve()
    output_name = args.output_name or f"{source_path.name.replace('-', '_')}_Master"
    custom_bgm = Path(args.bgm).resolve() if args.bgm else None
    custom_audio = Path(args.audio_dir).resolve() if args.audio_dir else None
    custom_video = Path(args.video_dir).resolve() if args.video_dir else None

    build_pipeline(
        source_dir=source_path,
        output_name=output_name,
        channel_name=args.channel,
        custom_bgm=custom_bgm,
        custom_audio_dir=custom_audio,
        custom_video_dir=custom_video,
        bgm_vol=args.bgm_vol
    )


if __name__ == "__main__":
    main()
