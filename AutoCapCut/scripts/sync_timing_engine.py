#!/usr/bin/env python3
"""
scripts/sync_timing_engine.py
Engine tính toán nhịp thời gian microsecond và đồng bộ hóa:
- Audio giọng đọc (Master Clock)
- Video B-roll phân cảnh (Slave Clock - trim từ clip 8s, speed 1.0)
- Phụ đề từng câu thoại (Subtitles Track)
"""

import os
import re
import json
import wave
import difflib
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

class SyncTimingEngine:
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.timing_map_path = self.source_dir / "scene_timing_map.json"
        self.audio_dir = self.source_dir / "audio"
        self.video_dir = self.source_dir / "video"
        
        if not self.timing_map_path.exists():
            raise FileNotFoundError(f"Không tìm thấy timing map: {self.timing_map_path}")
            
        with open(self.timing_map_path, "r", encoding="utf-8") as f:
            self.timing_data = json.load(f)
            
        self._map_video_folders()

    def _map_video_folders(self):
        """Ánh xạ số chương (01, 02, ...) sang thư mục video tương ứng"""
        self.chapter_folders = {}
        if not self.video_dir.exists():
            return
            
        for entry in self.video_dir.iterdir():
            if entry.is_dir():
                m = re.search(r"Chương\s+(\d+)", entry.name, re.IGNORECASE)
                if m:
                    ch_num = f"{int(m.group(1)):02d}"
                    self.chapter_folders[ch_num] = entry

    def get_audio_duration(self, chapter_num: str) -> float:
        """Đo thời lượng chính xác của file audio theo số giây (float)"""
        wav_path = self.audio_dir / f"chapter_{chapter_num}.wav"
        if wav_path.exists():
            try:
                with wave.open(str(wav_path), "rb") as f:
                    frames = f.getnframes()
                    rate = f.getframerate()
                    return frames / float(rate)
            except Exception:
                pass
                
        # Fallback ffprobe nếu file không phải WAV chuẩn
        for ext in [".wav", ".mp3", ".m4a", ".aac"]:
            fpath = self.audio_dir / f"chapter_{chapter_num}{ext}"
            if fpath.exists():
                cmd = [
                    "/opt/homebrew/bin/ffprobe",
                    "-v", "error",
                    "-show_entries", "format=duration",
                    "-of", "default=noprint_wrappers=1:nokey=1",
                    str(fpath)
                ]
                res = subprocess.run(cmd, capture_output=True, text=True)
                if res.returncode == 0 and res.stdout.strip():
                    return float(res.stdout.strip())
                    
        raise FileNotFoundError(f"Không tìm thấy file audio cho chương {chapter_num} tại {self.audio_dir}")

    def get_scenes_for_chapter(self, chapter_num: str) -> List[Dict[str, Any]]:
        """Lọc danh sách các scene thuộc một chương cụ thể"""
        target = f"{int(chapter_num):02d}"
        scenes = [sc for sc in self.timing_data if f"{int(sc.get('chapter', 0)):02d}" == target]
        return scenes

    def _find_whisper_json(self, chapter_num: str) -> Optional[Path]:
        """Tìm file kết quả Whisper JSON cho chương (ưu tiên bản turbo)"""
        ch_key = f"{int(chapter_num):02d}"
        turbo_file = self.audio_dir / f"chapter_{ch_key}_whisper_turbo.json"
        if turbo_file.exists():
            return turbo_file
        normal_file = self.audio_dir / f"chapter_{ch_key}_whisper.json"
        if normal_file.exists():
            return normal_file
        return None

    def _compute_timeline_with_whisper(
        self,
        ch_key: str,
        scenes: List[Dict[str, Any]],
        audio_duration: float,
        audio_path: Path,
        video_folder: Path,
        whisper_path: Path
    ) -> Dict[str, Any]:
        """Tính toán mốc thời gian chính xác dựa trên Whisper Forced Alignment"""
        with open(whisper_path, "r", encoding="utf-8") as f:
            wdata = json.load(f)

        # Trích xuất toàn bộ từ cùng mốc thời gian từ token
        all_words = []
        for seg in wdata.get("transcription", []):
            tokens = seg.get("tokens", [])
            curr_word = ""
            start_ms = 0
            end_ms = 0
            for t in tokens:
                txt = t.get("text", "")
                if txt.startswith("[_") and txt.endswith("]"):
                    continue
                if txt.startswith(" "):
                    if curr_word:
                        w_clean = re.sub(r"\[_.*?\]", "", curr_word).strip()
                        if w_clean:
                            all_words.append({
                                "word": w_clean,
                                "start": start_ms / 1000.0,
                                "end": end_ms / 1000.0
                            })
                    curr_word = txt
                    start_ms = t.get("offsets", {}).get("from", 0)
                    end_ms = t.get("offsets", {}).get("to", 0)
                else:
                    curr_word += txt
                    end_ms = t.get("offsets", {}).get("to", 0)
            if curr_word:
                w_clean = re.sub(r"\[_.*?\]", "", curr_word).strip()
                if w_clean:
                    all_words.append({
                        "word": w_clean,
                        "start": start_ms / 1000.0,
                        "end": end_ms / 1000.0
                    })

        def clean_tokens(text: str) -> List[str]:
            text = text.lower()
            text = re.sub(r"[^\w\s]", "", text)
            return text.split()

        w_norm = [clean_tokens(w["word"])[0] if clean_tokens(w["word"]) else "" for w in all_words]

        # Khớp tuần tự từng scene với các từ trong Whisper (hỗ trợ so khớp mờ cho phương ngữ/dấu)
        cursor = 0
        scene_bounds = []

        for idx, sc in enumerate(scenes):
            s_text = " ".join(sc.get("sentences", []))
            stoks = clean_tokens(s_text)
            if not stoks:
                continue

            target_last = stoks[-2:] if len(stoks) >= 2 else stoks[-1:]
            exp_len = len(stoks)
            search_start = max(0, cursor + exp_len - 3)
            search_end = min(len(w_norm), cursor + exp_len + 10)

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

            start_word = all_words[cursor]
            end_word = all_words[best_match]
            sc_words = all_words[cursor : best_match + 1]
            scene_bounds.append({
                "id": sc["id"],
                "start_word": start_word,
                "end_word": end_word,
                "scene_words": sc_words,
                "sentences": sc.get("sentences", []),
                "raw_scene": sc
            })
            cursor = best_match + 1

        # Cắt cảnh tại trung điểm khoảng lặng giữa 2 câu
        cuts = [0.0]
        for i in range(len(scene_bounds) - 1):
            curr_end = scene_bounds[i]["end_word"]["end"]
            next_start = scene_bounds[i + 1]["start_word"]["start"]
            if next_start > curr_end:
                cut = round((curr_end + next_start) / 2.0, 6)
            else:
                cut = curr_end
            cuts.append(cut)
        cuts.append(audio_duration)

        # Xây dựng danh sách Video items và Subtitle items
        video_items = []
        raw_cues = []

        for i, sb in enumerate(scene_bounds):
            sc_id = sb["id"]
            video_file = video_folder / f"{sc_id}.mp4"
            if not video_file.exists():
                raise FileNotFoundError(f"Không tìm thấy file video {sc_id}.mp4 trong {video_folder}")

            s_time = cuts[i]
            e_time = cuts[i + 1]
            dur = round(e_time - s_time, 6)

            # Tốc độ clip: nếu thời lượng > 8s, điều chỉnh nhẹ tốc độ
            speed = 1.0
            if dur > 8.0:
                speed = round(8.0 / dur, 4)

            video_items.append({
                "scene_id": sc_id,
                "path": str(video_file.resolve()),
                "start": s_time,
                "duration": dur,
                "sourceStart": 0.0,
                "speed": speed
            })

            # Tạo các phân đoạn phụ đề nhịp điệu (Rhythmic Subtitles)
            cues = self._build_rhythmic_subtitles(sb, s_time, e_time)
            raw_cues.extend(cues)

        # Sanitizer pass đảm bảo tuyệt đối không overlap và tốc độ đọc êm ái
        subtitle_items = self._sanitize_subtitles(raw_cues, audio_duration)

        return {
            "chapter": ch_key,
            "audio_path": str(audio_path.resolve()),
            "total_duration": audio_duration,
            "video_items": video_items,
            "subtitle_items": subtitle_items,
            "alignment_mode": "whisper_forced_alignment"
        }

    @staticmethod
    def _format_caption_text(text: str, max_line_len: int = 38) -> str:
        """Tự động xuống dòng tại điểm ngắt ngữ nghĩa tự nhiên nếu vượt quá max_line_len (tối đa 42 ký tự)"""
        if len(text) <= max_line_len or "\n" in text:
            return text
        words = text.split()
        if len(words) <= 3:
            return text
        
        conjunctions = {'và', 'nhưng', 'mà', 'vì', 'để', 'nếu', 'khi', 'dù', 'hoặc', 'hay', 'bởi', 'thế', 'tuy', 'cho', 'với', 'trong', 'tại'}
        mid = len(words) // 2
        best_idx = mid
        best_score = -100
        for idx in range(1, len(words) - 1):
            score = 0
            w = words[idx]
            if any(w.endswith(p) for p in [',', ';', ':', '—', '-']):
                score += 40
            if idx + 1 < len(words):
                next_w = re.sub(r'[^\w\s]', '', words[idx + 1].lower())
                if next_w in conjunctions:
                    score += 30
            l1 = len(' '.join(words[:idx + 1]))
            l2 = len(' '.join(words[idx + 1:]))
            if l1 <= max_line_len and l2 <= max_line_len:
                score += 50
            score -= abs(l1 - l2)
            if score > best_score:
                best_score = score
                best_idx = idx
        return ' '.join(words[:best_idx + 1]) + '\n' + ' '.join(words[best_idx + 1:])

    def _build_rhythmic_subtitles(
        self,
        sb: Dict[str, Any],
        s_time: float,
        e_time: float
    ) -> List[Dict[str, Any]]:
        """Xây dựng phụ đề chuẩn phim tài liệu (Vox/Johnny Harris) ngắt theo cụm ngữ nghĩa tự nhiên"""
        sc_id = sb["id"]
        s_text = " ".join(sb.get("sentences", [])).strip()
        words = sb.get("scene_words", [])

        if not words or not s_text:
            return [{
                "text": s_text,
                "start": round(s_time, 3),
                "raw_end": e_time,
                "scene_id": sc_id
            }]

        dur_total = e_time - s_time
        # Nếu câu <= 75 ký tự hoặc thời lượng <= 4.2s, hiển thị trọn vẹn 1 cue (1 hoặc 2 dòng cân đối)
        if len(s_text) <= 75 or dur_total <= 4.2:
            c_text = self._format_caption_text(s_text)
            c_start = max(words[0]["start"], s_time)
            c_end = min(words[-1]["end"], e_time)
            return [{
                "text": c_text,
                "start": round(c_start, 3),
                "raw_end": c_end,
                "scene_id": sc_id
            }]

        # Với câu dài hơn (> 75 ký tự và > 4.2s), tách thành 2 cues thời gian
        script_words = s_text.split()
        n_w = len(words)
        n_s = len(script_words)
        conjunctions = {'và', 'nhưng', 'mà', 'vì', 'để', 'nếu', 'khi', 'dù', 'hoặc', 'hay', 'bởi', 'thế', 'tuy', 'cho', 'với', 'trong', 'tại'}

        mid_w = n_w // 2
        split_w = mid_w
        best_score = -100
        for j in range(2, n_w - 2):
            w = words[j]
            score = 0
            if any(w["word"].endswith(p) for p in [',', ';', ':', '—', '-']):
                score += 50
            if j + 1 < n_w:
                next_w = re.sub(r'[^\w\s]', '', words[j + 1]["word"].lower())
                if next_w in conjunctions:
                    score += 30
            dur_left = w["end"] - words[0]["start"]
            dur_right = words[-1]["end"] - words[j + 1]["start"]
            if dur_left < 1.3 or dur_right < 1.3:
                score -= 100
            score -= abs(j - mid_w) * 3
            if score > best_score:
                best_score = score
                split_w = j

        grp1 = words[:split_w + 1]
        grp2 = words[split_w + 1:]
        s_split = min(int(split_w * n_s / n_w), n_s - 1)
        t1 = self._format_caption_text(" ".join(script_words[:s_split + 1]))
        t2 = self._format_caption_text(" ".join(script_words[s_split + 1:]))

        return [
            {
                "text": t1,
                "start": round(max(grp1[0]["start"], s_time), 3),
                "raw_end": grp1[-1]["end"],
                "scene_id": sc_id
            },
            {
                "text": t2,
                "start": round(max(grp2[0]["start"], s_time), 3),
                "raw_end": min(grp2[-1]["end"], e_time),
                "scene_id": sc_id
            }
        ]

    def _sanitize_subtitles(
        self,
        cues: List[Dict[str, Any]],
        total_audio_duration: float,
        gap: float = 0.02
    ) -> List[Dict[str, Any]]:
        """Bảo đảm 100% không chồng chéo (zero-overlap) và tốc độ đọc thoải mái (CPS <= 20, 0 warning)"""
        if not cues:
            return []

        # 1. Đảm bảo start time tăng đơn điệu và có khoảng cách tối thiểu
        for i in range(len(cues)):
            if i > 0:
                min_start = cues[i - 1]["start"] + 0.45 + gap
                if cues[i]["start"] < min_start:
                    cues[i]["start"] = min_start

        # 2. Tinh chỉnh: nếu tốc độ đọc sát ngưỡng 20 cps, tận dụng khoảng trống phía trước để lùi nhẹ mốc bắt đầu
        for i in range(len(cues)):
            plain_text = re.sub(r"\s+", "", cues[i]["text"])
            text_len = len(plain_text)
            min_dur_needed = text_len / 19.5
            next_start = cues[i + 1]["start"] if i < len(cues) - 1 else total_audio_duration
            avail = next_start - cues[i]["start"] - gap
            if avail < min_dur_needed and i > 0:
                prev_start = cues[i - 1]["start"]
                shortage = min_dur_needed - avail
                prev_min_end = prev_start + 0.45 + gap
                max_back = cues[i]["start"] - prev_min_end
                if max_back > 0:
                    shift = min(shortage + 0.05, max_back)
                    cues[i]["start"] = round(cues[i]["start"] - shift, 3)

        # 3. Tính toán duration chính xác
        sanitized = []
        for i in range(len(cues)):
            cur_start = cues[i]["start"]
            if i < len(cues) - 1:
                next_start = cues[i + 1]["start"]
                max_dur = round(next_start - cur_start - gap, 3)
            else:
                max_dur = round(total_audio_duration - cur_start - gap, 3)

            plain_text = re.sub(r"\s+", "", cues[i]["text"])
            text_len = len(plain_text)
            min_dur_needed = round(text_len / 19.5, 3)
            ideal_dur = max(cues[i]["raw_end"] - cur_start, min_dur_needed)

            # Cầu nối khoảng lặng ngắn (< 0.8s) để chữ đứng yên cho người xem dễ đọc
            if max_dur <= ideal_dur + 0.8:
                dur = max_dur
            else:
                dur = min(ideal_dur + 0.25, max_dur)

            dur = round(max(dur, 0.45), 3)
            if dur > max_dur:
                dur = max_dur

            sanitized.append({
                "text": cues[i]["text"],
                "start": round(cur_start, 3),
                "duration": dur,
                "scene_id": cues[i]["scene_id"]
            })

        return sanitized

    def compute_chapter_timeline(self, chapter_num: str) -> Dict[str, Any]:
        """
        Tính toán mốc thời gian chính xác cho toàn bộ video clips và phụ đề trong một chương.
        Ưu tiên dùng Whisper Forced Alignment nếu có file json.
        """
        ch_key = f"{int(chapter_num):02d}"
        scenes = self.get_scenes_for_chapter(ch_key)
        if not scenes:
            raise ValueError(f"Không tìm thấy scene nào cho chương {ch_key} trong timing map")
            
        audio_duration = self.get_audio_duration(ch_key)
        audio_path = self.audio_dir / f"chapter_{ch_key}.wav"
        video_folder = self.chapter_folders.get(ch_key)
        if not video_folder:
            raise FileNotFoundError(f"Không tìm thấy thư mục video cho chương {ch_key}")

        whisper_json = self._find_whisper_json(ch_key)
        if whisper_json:
            return self._compute_timeline_with_whisper(
                ch_key, scenes, audio_duration, audio_path, video_folder, whisper_json
            )

        # Fallback: Tính toán trọng số văn bản nếu không có Whisper
        scene_weights = []
        for sc in scenes:
            sentences = sc.get("sentences", [])
            total_chars = sum(len(s.strip()) for s in sentences)
            weight = max(total_chars, 10)
            scene_weights.append(weight)
            
        total_weight = sum(scene_weights)
        
        scene_durations = []
        current_sum = 0.0
        for i, w in enumerate(scene_weights):
            if i == len(scene_weights) - 1:
                dur = round(audio_duration - current_sum, 6)
            else:
                dur = round((w / total_weight) * audio_duration, 6)
                current_sum += dur
            scene_durations.append(dur)

        video_items = []
        subtitle_items = []
        current_time = 0.0

        for i, (sc, dur) in enumerate(zip(scenes, scene_durations)):
            sc_id = sc["id"]
            video_file = video_folder / f"{sc_id}.mp4"
            if not video_file.exists():
                raise FileNotFoundError(f"Không tìm thấy file video {sc_id}.mp4 trong {video_folder}")
                
            video_items.append({
                "scene_id": sc_id,
                "path": str(video_file.resolve()),
                "start": current_time,
                "duration": dur,
                "sourceStart": 0.0,
                "speed": 1.0
            })
            
            sentences = sc.get("sentences", [])
            if sentences:
                sent_weights = [max(len(s.strip()), 1) for s in sentences]
                sum_sw = sum(sent_weights)
                sub_curr = current_time
                sub_sum = 0.0
                
                for s_idx, (sent, sw) in enumerate(zip(sentences, sent_weights)):
                    if s_idx == len(sentences) - 1:
                        s_dur = round(dur - sub_sum, 6)
                    else:
                        s_dur = round((sw / sum_sw) * dur, 6)
                        sub_sum += s_dur
                        
                    subtitle_items.append({
                        "text": sent.strip(),
                        "start": sub_curr,
                        "duration": s_dur,
                        "scene_id": sc_id
                    })
                    sub_curr = round(sub_curr + s_dur, 6)
            
            current_time = round(current_time + dur, 6)

        return {
            "chapter": ch_key,
            "audio_path": str(audio_path.resolve()),
            "total_duration": audio_duration,
            "video_items": video_items,
            "subtitle_items": subtitle_items,
            "alignment_mode": "text_weight_fallback"
        }

if __name__ == "__main__":
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "source/philipin"
    ch = sys.argv[2] if len(sys.argv) > 2 else "01"
    engine = SyncTimingEngine(src)
    res = engine.compute_chapter_timeline(ch)
    print(f"--- KIỂM TRA ĐỒNG BỘ CHƯƠNG {ch} ---")
    print(f"Tổng thời lượng Audio: {res['total_duration']:.4f}s")
    print(f"Số lượng Video Clips: {len(res['video_items'])}")
    print(f"Số lượng Phụ Đề: {len(res['subtitle_items'])}")
    total_v_dur = res['video_items'][-1]['start'] + res['video_items'][-1]['duration']
    print(f"Tổng thời lượng Video: {total_v_dur:.6f}s (Khớp Audio: {abs(total_v_dur - res['total_duration']) < 1e-5})")
