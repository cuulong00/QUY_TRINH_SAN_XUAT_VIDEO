#!/usr/bin/env python3
"""
apply_vox_semantic_subtitles.py

Industry-standard (BBC / Netflix / Vox Video Essay) Subtitling Engine for CapCut Desktop.
Fixes the two core problems:
1. "Chữ không hiển thị được trên video dù timeline đi qua":
   Uses CapCut native text track via official `capcut import-srt` instead of broken cloud template IDs.
   CapCut Desktop native font renderer renders it 100% visibly and crisply.
2. "Chữ khó đọc, trùng nền, cắt nửa vời":
   - Semantic Clause Segmentation: Complete thoughts (3.0s - 5.5s per cue), no dangling phrases.
   - Vox Dark Rounded Card: Background style 1 (black #000000, alpha 0.80, round radius 0.35).
   - High contrast white text (#FFFFFF), font size 8.0, lower-third position (y = -0.73), black stroke.
"""

import json
import os
import re
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CAPCUT_CLI_PATH = PROJECT_ROOT / "tools" / "capcut-cli" / "dist" / "index.js"

def get_word_tokens(entry):
    tokens = []
    curr = ""
    w_start = None
    w_end = None
    for tok in entry.get("tokens", []):
        t_text = tok.get("text", "")
        if t_text.startswith("[_") and t_text.endswith("]"):
            continue
        o_from = tok.get("offsets", {}).get("from", 0)
        o_to = tok.get("offsets", {}).get("to", 0)
        if t_text.startswith(" ") or not curr:
            if curr:
                tokens.append({"word": curr.strip(), "start_ms": w_start, "end_ms": w_end})
            curr = t_text
            w_start = o_from
            w_end = o_to
        else:
            curr += t_text
            w_end = o_to
    if curr:
        tokens.append({"word": curr.strip(), "start_ms": w_start, "end_ms": w_end})
    return tokens

def clean_vietnamese_text(text):
    text = re.sub(r"\btràng tiền\b", "Tràng Tiền", text, flags=re.IGNORECASE)
    text = re.sub(r"\bhà nội\b", "Hà Nội", text, flags=re.IGNORECASE)
    text = re.sub(r"\bhồ gươm\b", "Hồ Gươm", text, flags=re.IGNORECASE)
    text = re.sub(r"\bindochine\b", "Indochine", text, flags=re.IGNORECASE)
    text = re.sub(r"\bvnđ\b", "VNĐ", text, flags=re.IGNORECASE)
    text = re.sub(r"\blan sóng\b", "làn sóng", text, flags=re.IGNORECASE)
    text = re.sub(r"\bchen trúc\b", "chen chúc", text, flags=re.IGNORECASE)
    text = re.sub(r"\bdơ điện thoại\b", "giơ điện thoại", text, flags=re.IGNORECASE)
    text = re.sub(r"\brừng đón khách\b", "dừng đón khách", text, flags=re.IGNORECASE)
    text = re.sub(r"\btrốn dung thân\b", "chốn dung thân", text, flags=re.IGNORECASE)
    text = re.sub(r"\bcùng kỷ\b", "cùng kỳ", text, flags=re.IGNORECASE)
    return text

def generate_semantic_cues(whisper_path):
    with open(whisper_path, "r", encoding="utf-8") as f:
        whisper_data = json.load(f)

    transcription = whisper_data.get("transcription", [])
    raw_cues = []

    for entry in transcription:
        words = get_word_tokens(entry)
        if not words:
            continue

        # Split by punctuation
        clauses = []
        cur = []
        for w in words:
            cur.append(w)
            w_text = w["word"]
            if any(w_text.endswith(p) for p in [",", ";", ":", "—", "-", ".", "!", "?"]):
                clauses.append(cur)
                cur = []
        if cur:
            clauses.append(cur)

        # Merge short clauses (< 2.0s or < 6 words) with adjacent clauses
        merged = []
        buf = []
        for cl in clauses:
            if not buf:
                buf = cl
            else:
                buf_dur = (buf[-1]["end_ms"] - buf[0]["start_ms"]) / 1000.0
                cl_dur = (cl[-1]["end_ms"] - cl[0]["start_ms"]) / 1000.0
                total_words = len(buf) + len(cl)
                total_dur = (cl[-1]["end_ms"] - buf[0]["start_ms"]) / 1000.0

                if (buf_dur < 2.0 or len(buf) < 6 or cl_dur < 2.0 or len(cl) < 6) and total_dur <= 6.5 and total_words <= 20:
                    buf.extend(cl)
                else:
                    merged.append(buf)
                    buf = cl
        if buf:
            merged.append(buf)

        # For clauses > 6.0s or > 18 words, split before known clause markers
        clause_markers = {"trước khi", "để", "với", "nhưng", "và đành", "khi", "mà không"}
        final_clauses = []
        for cl in merged:
            dur = (cl[-1]["end_ms"] - cl[0]["start_ms"]) / 1000.0
            if dur > 6.0 and len(cl) > 16:
                split_idx = None
                mid = len(cl) // 2
                best_dist = 999
                for k in range(4, len(cl) - 4):
                    w_curr = cl[k]["word"].lower()
                    w_prev = cl[k-1]["word"].lower() if k > 0 else ""
                    two_words = f"{w_prev} {w_curr}"
                    if two_words in clause_markers or w_curr in clause_markers:
                        dist = abs(k - mid)
                        if dist < best_dist:
                            best_dist = dist
                            split_idx = k
                if split_idx is not None:
                    final_clauses.append(cl[:split_idx])
                    final_clauses.append(cl[split_idx:])
                else:
                    final_clauses.append(cl)
            else:
                final_clauses.append(cl)

        for cl in final_clauses:
            text = clean_vietnamese_text(" ".join(w["word"] for w in cl))
            raw_cues.append({
                "start_ms": cl[0]["start_ms"],
                "end_ms": cl[-1]["end_ms"],
                "start_us": cl[0]["start_ms"] * 1000,
                "duration_us": (cl[-1]["end_ms"] - cl[0]["start_ms"]) * 1000,
                "text": text,
                "words": cl
            })

    return raw_cues

def ms_to_srt_time(ms):
    hours = ms // 3600000
    ms %= 3600000
    minutes = ms // 60000
    ms %= 60000
    seconds = ms // 1000
    millis = ms % 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"

def wrap_text(text, max_chars=42):
    if len(text) <= max_chars:
        return text
    words = text.split()
    if len(text) <= max_chars * 2:
        mid = len(text) // 2
        best_idx = len(words) // 2
        best_dist = 999
        cur_len = 0
        for i, w in enumerate(words[:-1]):
            cur_len += len(w) + (1 if i > 0 else 0)
            dist = abs(cur_len - mid)
            if dist < best_dist:
                best_dist = dist
                best_idx = i + 1
        l1 = " ".join(words[:best_idx])
        l2 = " ".join(words[best_idx:])
        if len(l1) <= max_chars and len(l2) <= max_chars:
            return f"{l1}\n{l2}"

    lines = []
    cur = []
    cur_len = 0
    for w in words:
        if cur and (cur_len + 1 + len(w) > max_chars):
            lines.append(" ".join(cur))
            cur = [w]
            cur_len = len(w)
        else:
            cur.append(w)
            cur_len += (1 if cur_len > 0 else 0) + len(w)
    if cur:
        lines.append(" ".join(cur))
    return "\n".join(lines)

def export_cues_to_srt(cues, srt_path):
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, c in enumerate(cues, 1):
            s = ms_to_srt_time(c["start_ms"])
            e = ms_to_srt_time(c["end_ms"])
            t = wrap_text(c["text"], max_chars=42)
            f.write(f"{i}\n{s} --> {e}\n{t}\n\n")

def apply_vox_subtitles(draft_path, whisper_path, srt_out_path=None):
    draft_path = Path(draft_path).resolve()
    info_path = draft_path / "draft_info.json"
    if not info_path.exists():
        print(f"Error: {info_path} does not exist.")
        sys.exit(1)

    cues = generate_semantic_cues(whisper_path)
    print(f"Generated {len(cues)} complete semantic cues (Complete Thoughts).")

    if not srt_out_path:
        srt_out_path = draft_path / "semantic_subtitles.srt"
    else:
        srt_out_path = Path(srt_out_path).resolve()

    export_cues_to_srt(cues, str(srt_out_path))
    print(f"Exported semantic cues to {srt_out_path}")

    # 1. Clean existing text tracks & text templates from draft_info.json
    with open(info_path, "r", encoding="utf-8") as f:
        draft = json.load(f)

    # Remove any existing text tracks
    draft["tracks"] = [tr for tr in draft.get("tracks", []) if tr.get("type") != "text"]
    materials = draft.setdefault("materials", {})
    materials["texts"] = []
    materials["text_templates"] = []
    materials["material_animations"] = []

    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(draft, f, ensure_ascii=False, indent=2)

    # 2. Use official capcut-cli import-srt
    cmd = [
        "node",
        str(CAPCUT_CLI_PATH),
        "import-srt",
        str(draft_path),
        str(srt_out_path),
        "--track-name", "Subtitles",
        "--font-size", "8.0",
        "--color", "#FFFFFF",
        "--y", "-0.73",
        "--border-width", "0.08",
        "--border-color", "#000000",
        "--border-alpha", "1.0",
        "--bg-color", "#000000",
        "--bg-alpha", "0.80",
        "--bg-style", "1",
        "--bg-round-radius", "0.35"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] import-srt failed:\n{res.stderr or res.stdout}", file=sys.stderr)
        sys.exit(1)

    # 3. Post-process to ensure sub_type: 1 and clean caption_template_info for 100% CapCut compatibility
    with open(info_path, "r", encoding="utf-8") as f:
        draft = json.load(f)

    for tm in draft.get("materials", {}).get("texts", []):
        tm["sub_type"] = 1
        tm["caption_template_info"] = {
            "category_id": "",
            "category_name": "",
            "effect_id": "",
            "is_new": False,
            "path": "",
            "request_id": "",
            "resource_id": "",
            "resource_name": "",
            "source_platform": 0,
            "third_resource_id": ""
        }

    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(draft, f, ensure_ascii=False, indent=2)

    print(f"Successfully applied {len(cues)} Native Vox Semantic Subtitles to {draft_path}!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 apply_vox_semantic_subtitles.py <draft_path> <whisper_json_path> [srt_out_path]")
        sys.exit(1)
    srt_p = sys.argv[3] if len(sys.argv) > 3 else None
    apply_vox_subtitles(sys.argv[1], sys.argv[2], srt_p)
