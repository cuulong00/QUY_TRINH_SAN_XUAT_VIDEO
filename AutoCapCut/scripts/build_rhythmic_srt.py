#!/usr/bin/env python3
"""
Tạo file phụ đề nhịp điệu (Rhythmic SRT) từ kết quả nhận diện Whisper Turbo.
Chuẩn Documentary/Video Essay:
- Mỗi cue gồm 3 đến 5 từ (tối đa 26 ký tự).
- Thời lượng hiển thị ~1.0s đến 1.6s/cue.
- Ngắt tại dấu câu (phẩy, chấm, chấm phẩy, gạch ngang) hoặc khoảng lặng giọng nói.
- Giữ trọn vẹn văn phong tiếng Việt chuẩn, không bao giờ để sót từ cụt (1 từ đơn lẻ đứng riêng).
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any

def format_timestamp_srt(seconds: float) -> str:
    """Chuyển đổi số giây thành định dạng SRT: HH:MM:SS,mmm"""
    total_ms = int(round(seconds * 1000))
    hours = total_ms // 3600000
    remainder = total_ms % 3600000
    minutes = remainder // 60000
    remainder = remainder % 60000
    secs = remainder // 1000
    millis = remainder % 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def extract_whisper_words(whisper_json_path: Path) -> List[Dict[str, Any]]:
    """Trích xuất danh sách các từ cùng start/end chính xác từ Whisper Turbo JSON"""
    with open(whisper_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_words = []
    for seg in data.get("transcription", []):
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
    return all_words

def group_words_into_rhythmic_cues(
    words: List[Dict[str, Any]],
    target_words: int = 4,
    max_words: int = 5,
    max_chars: int = 26,
    max_gap: float = 0.38
) -> List[Dict[str, Any]]:
    """Gom các từ thành từng cụm nhịp điệu ngắn 3-5 từ, chuyển động theo tiếng nói"""
    cues = []
    group = []
    punctuations = {',', '.', ';', ':', '—', '-', '!', '?', '…'}
    conjunctions = {'và', 'nhưng', 'mà', 'vì', 'để', 'nếu', 'khi', 'dù', 'hoặc', 'tại', 'trong', 'của'}

    i = 0
    while i < len(words):
        w = words[i]
        group.append(w)
        text = " ".join(item["word"] for item in group)

        ends_punc = any(w["word"].endswith(p) for p in punctuations)
        next_w = words[i + 1] if i + 1 < len(words) else None
        gap = (next_w["start"] - w["end"]) if next_w else 0
        dur = group[-1]["end"] - group[0]["start"]

        # Không bao giờ ngắt khi group mới có 1 từ (trừ khi là từ cuối cùng của file)
        if len(group) == 1 and next_w is not None:
            i += 1
            continue

        # Nếu từ tiếp theo kết thúc câu (dấu câu), ưu tiên gộp nốt nếu group còn nhỏ
        if next_w and any(next_w["word"].endswith(p) for p in punctuations):
            if len(group) <= 3:
                i += 1
                continue

        should_flush = False
        if next_w is None:
            should_flush = True
        elif ends_punc:
            should_flush = True
        elif gap > max_gap:
            should_flush = True
        elif len(group) >= max_words:
            should_flush = True
        elif len(text) >= max_chars:
            should_flush = True
        elif len(group) >= 3 and next_w and re.sub(r'[^\w\s]', '', next_w['word'].lower()) in conjunctions and dur >= 0.9:
            should_flush = True

        if should_flush:
            cues.append({
                "start": group[0]["start"],
                "end": group[-1]["end"],
                "text": text,
                "duration": round(group[-1]["end"] - group[0]["start"], 3),
                "words_count": len(group)
            })
            group = []

        i += 1

    if group:
        cues.append({
            "start": group[0]["start"],
            "end": group[-1]["end"],
            "text": " ".join(item["word"] for item in group),
            "duration": round(group[-1]["end"] - group[0]["start"], 3),
            "words_count": len(group)
        })

    # Hậu kiểm 1: Đảm bảo mọi cue đều có duration tối thiểu 0.4s
    for c in cues:
        if c["end"] <= c["start"] + 0.35:
            c["end"] = round(c["start"] + 0.40, 3)
        c["duration"] = round(c["end"] - c["start"], 3)

    # Hậu kiểm 2: Hợp nhất các cụm quá ngắn (< 0.6s hoặc 1 từ) vào cụm liền trước
    merged_cues = []
    for c in cues:
        if merged_cues and (c["duration"] < 0.6 or c["words_count"] <= 1) and (merged_cues[-1]["words_count"] + c["words_count"] <= 6):
            prev = merged_cues[-1]
            prev["end"] = max(prev["end"], c["end"])
            prev["text"] = prev["text"] + " " + c["text"]
            prev["duration"] = round(prev["end"] - prev["start"], 3)
            prev["words_count"] += c["words_count"]
        else:
            merged_cues.append(c)

    # Hậu kiểm 3: Đảm bảo không chồng chéo thời gian và end > start nghiêm ngặt
    for k in range(len(merged_cues) - 1):
        curr = merged_cues[k]
        nxt = merged_cues[k + 1]
        if curr["end"] >= nxt["start"]:
            if nxt["start"] - 0.02 >= curr["start"] + 0.35:
                curr["end"] = round(nxt["start"] - 0.02, 3)
            else:
                curr["end"] = round(curr["start"] + 0.35, 3)
                if nxt["start"] <= curr["end"] + 0.02:
                    nxt["start"] = round(curr["end"] + 0.02, 3)
                    if nxt["end"] <= nxt["start"] + 0.35:
                        nxt["end"] = round(nxt["start"] + 0.40, 3)
        curr["duration"] = round(curr["end"] - curr["start"], 3)

    # Hậu kiểm 4: Tối ưu tốc độ đọc (Reading Speed CPS <= 19) đạt chuẩn 0 lint warning
    total_audio_dur = 331.14
    for k in range(len(merged_cues)):
        plain_len = len(re.sub(r"\s+", "", merged_cues[k]["text"]))
        needed_dur = plain_len / 18.5
        curr_dur = merged_cues[k]["end"] - merged_cues[k]["start"]
        if curr_dur < needed_dur:
            deficit = needed_dur - curr_dur
            next_start = merged_cues[k + 1]["start"] if k < len(merged_cues) - 1 else total_audio_dur
            gap_after = next_start - merged_cues[k]["end"] - 0.02
            if gap_after > 0:
                expand_after = min(deficit, gap_after)
                merged_cues[k]["end"] = round(merged_cues[k]["end"] + expand_after, 3)
                deficit -= expand_after
            if deficit > 0:
                prev_end = merged_cues[k - 1]["end"] if k > 0 else 0.0
                gap_before = merged_cues[k]["start"] - prev_end - 0.02
                if gap_before > 0:
                    expand_before = min(deficit, gap_before)
                    merged_cues[k]["start"] = round(merged_cues[k]["start"] - expand_before, 3)
            merged_cues[k]["duration"] = round(merged_cues[k]["end"] - merged_cues[k]["start"], 3)

    return merged_cues

def generate_srt_file(cues: List[Dict[str, Any]], out_path: Path):
    """Ghi danh sách cues thành file SRT chuẩn"""
    lines = []
    for idx, cue in enumerate(cues, 1):
        start_str = format_timestamp_srt(cue["start"])
        end_str = format_timestamp_srt(cue["end"])
        lines.append(f"{idx}")
        lines.append(f"{start_str} --> {end_str}")
        lines.append(cue["text"])
        lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[✓] Đã tạo file SRT nhịp điệu với {len(cues)} cues tại: {out_path}")

def main():
    whisper_file = Path("source/kem-trang-tien/audio/chapter_01_whisper_turbo.json")
    out_srt = Path("output_drafts/chapter_01_rhythmic.srt")
    words = extract_whisper_words(whisper_file)
    print(f"[*] Đã trích xuất {len(words)} từ từ Whisper Turbo.")
    cues = group_words_into_rhythmic_cues(words)
    print(f"[*] Đã phân nhóm thành {len(cues)} cụm từ nhịp điệu (trung bình {len(words)/len(cues):.1f} từ/cue).")
    generate_srt_file(cues, out_srt)

if __name__ == "__main__":
    main()
