#!/usr/bin/env python3
"""
scripts/generate_capcut_spec.py
Chuyển đổi dữ liệu đồng bộ thời gian thành file spec.json declarative
phù hợp với chuẩn `capcut compile` của capcut-cli.
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from sync_timing_engine import SyncTimingEngine

def format_subtitle_text(text: str, max_chars: int = 42) -> str:
    """Ngắt dòng tự nhiên nếu câu dài hơn 42 ký tự chuẩn phóng sự/tài liệu"""
    if len(text) <= max_chars or "\n" in text:
        return text
    words = text.split()
    lines = []
    curr = []
    curr_len = 0
    for w in words:
        if curr_len + len(w) + (1 if curr else 0) > max_chars and curr:
            lines.append(" ".join(curr))
            curr = [w]
            curr_len = len(w)
        else:
            curr.append(w)
            curr_len += len(w) + (1 if len(curr) > 1 else 0)
    if curr:
        lines.append(" ".join(curr))
    return "\n".join(lines)

def load_subtitle_template(template_name_or_path: str = "johnny_harris_minimal") -> Dict[str, Any]:
    """Tải cấu hình template từ thư mục templates/subtitle_styles/"""
    p = Path(template_name_or_path)
    if not p.exists():
        p = Path("templates/subtitle_styles") / f"{template_name_or_path}.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def build_chapter_spec(
    timeline_data: Dict[str, Any],
    project_name: Optional[str] = None,
    width: int = 1920,
    height: int = 1080,
    fps: int = 30,
    ratio: str = "16:9",
    template_style: str = "johnny_harris_minimal",
    transition_slug: str = "black-fade",
    transition_duration: float = 0.40
) -> Dict[str, Any]:
    """Tạo đối tượng CompileSpec cho 1 chương áp dụng template chuẩn hóa và chuyển cảnh"""
    ch_num = timeline_data["chapter"]
    name = project_name or f"GocNhin_Ch{ch_num}"
    
    # Tải thông số template chuẩn
    tmpl = load_subtitle_template(template_style)
    typography = tmpl.get("typography", {})
    styling = tmpl.get("styling", {})
    
    text_color = typography.get("color", "#FFD700")
    text_font_size = int(typography.get("font_size", 12))
    text_y_offset = float(typography.get("y", -0.68))
    
    # 1. Track Video (Có ref cho từng clip để gắn transition)
    video_items = []
    for i, item in enumerate(timeline_data["video_items"]):
        v_ref = f"v_{i:03d}"
        video_items.append({
            "ref": v_ref,
            "path": item["path"],
            "start": item["start"],
            "duration": item["duration"],
            "sourceStart": item.get("sourceStart", 0.0),
            "speed": item.get("speed", 1.0),
            "volume": 0.0
        })
    
    video_track = {
        "type": "video",
        "name": "Main_Video",
        "items": video_items
    }
    
    # 2. Track Audio
    audio_track = {
        "type": "audio",
        "name": "Voiceover",
        "items": [
            {
                "path": timeline_data["audio_path"],
                "start": 0.0,
                "duration": timeline_data["total_duration"],
                "volume": 1.0
            }
        ]
    }
    
    # 3. Track Subtitle (Text)
    text_items = []
    text_style_operations = []
    for j, sub in enumerate(timeline_data["subtitle_items"]):
        t_ref = f"t_{j:03d}"
        text_items.append({
            "ref": t_ref,
            "text": sub["text"],
            "start": sub["start"],
            "duration": sub["duration"],
            "fontSize": text_font_size,
            "color": text_color,
            "y": text_y_offset
        })
        
        # Tạo operation text-style từ template
        op_style: Dict[str, Any] = {}
        if styling.get("has_border"):
            op_style["borderWidth"] = styling.get("border_width", 0.12)
            op_style["borderColor"] = styling.get("border_color", "#000000")
            op_style["borderAlpha"] = styling.get("border_alpha", 1.0)
        if styling.get("has_shadow"):
            op_style["shadow"] = True
            op_style["shadowAlpha"] = styling.get("shadow_alpha", 0.8)
            op_style["shadowAngle"] = styling.get("shadow_angle", -45.0)
            op_style["shadowColor"] = styling.get("shadow_color", "#000000")
            op_style["shadowDistance"] = styling.get("shadow_distance", 5.0)
            op_style["shadowSmoothing"] = styling.get("shadow_smoothing", 0.5)
        if styling.get("has_background"):
            op_style["bgColor"] = styling.get("bg_color", "#000000")
            op_style["bgAlpha"] = styling.get("bg_alpha", 0.65)
            op_style["bgStyle"] = styling.get("bg_style", 1)
            op_style["bgRoundRadius"] = styling.get("bg_round_radius", 0.25)
            op_style["bgWidth"] = styling.get("bg_width", 0.16)
            op_style["bgHeight"] = styling.get("bg_height", 0.14)
            
        if op_style:
            text_style_operations.append({
                "op": "text-style",
                "target": t_ref,
                "style": op_style
            })
    
    text_track = {
        "type": "text",
        "name": "Subtitles",
        "items": text_items
    }
    
    # 4. Operations: Chuyển cảnh giữa các video clips + Text Styling
    operations = []
    # Gắn transition cho các clip (trừ clip cuối cùng)
    for i in range(len(video_items) - 1):
        operations.append({
            "op": "transition",
            "target": f"v_{i:03d}",
            "slug": transition_slug,
            "duration": transition_duration
        })
    # Gắn text style operations
    operations.extend(text_style_operations)
    
    spec = {
        "name": name,
        "width": width,
        "height": height,
        "fps": fps,
        "ratio": ratio,
        "tracks": [video_track, audio_track, text_track],
        "operations": operations
    }
    
    return spec

if __name__ == "__main__":
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "source/philipin"
    ch = sys.argv[2] if len(sys.argv) > 2 else "01"
    out_file = sys.argv[3] if len(sys.argv) > 3 else f"output_drafts/spec_ch{ch}.json"
    
    engine = SyncTimingEngine(src)
    timeline = engine.compute_chapter_timeline(ch)
    spec = build_chapter_spec(timeline)
    
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)
        
    print(f"Đã xuất file cấu hình: {out_file}")
    print(f"Số lượng Tracks: {len(spec['tracks'])}")
    print(f"Video items: {len(spec['tracks'][0]['items'])}, Text items: {len(spec['tracks'][2]['items'])}")
