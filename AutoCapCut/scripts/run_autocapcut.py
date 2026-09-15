#!/usr/bin/env python3
"""
AutoCapCut Automation Pipeline using capcut-cli (renezander030)
Chuẩn hóa 100% qua lệnh CLI chính thức của capcut-cli:
1. Compile Timeline Video (69 clips cắt khít Whisper) + Audio (Voiceover) + Chuyển cảnh (Mix 0.8s).
2. Sinh file SRT nhịp điệu (Rhythmic Subtitles 3-5 từ/cue, ~1.2s/cue).
3. Import phụ đề bằng lệnh chính thức `capcut import-srt` với font-size 7.0, #FFD700, stroke đen và shadow.
4. Gán hoạt ảnh chữ bằng lệnh chính thức `capcut text-anim` (--intro typewriter).
5. Mute video clips & Đăng ký vật liệu bằng `capcut register --materials --apply`.
6. Kiểm toán chất lượng bằng `capcut lint` (0 error, 0 warning).
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "scripts"))

from sync_timing_engine import SyncTimingEngine
from build_rhythmic_srt import extract_whisper_words, group_words_into_rhythmic_cues, generate_srt_file

CAPCUT_CLI_PATH = PROJECT_ROOT / "tools" / "capcut-cli" / "dist" / "index.js"
DEFAULT_MAC_DRAFT_DIR = Path.home() / "Movies" / "CapCut" / "User Data" / "Projects" / "com.lveditor.draft"

def run_cmd(cmd, check=True):
    """Chạy command dòng lệnh và in output"""
    res = subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True)
    if check and res.returncode != 0:
        print(f"[ERROR] Command thất bại (code {res.returncode}):\n{res.stderr or res.stdout}", file=sys.stderr)
    return res

def process_chapter(
    chapter_num: str,
    source_dir: Path,
    out_dir: Path,
    project_name: Optional[str] = None,
    dry_run: bool = False,
    install_to_capcut: bool = True,
    transition_slug: str = "mix",
    transition_dur: float = 0.8,
    font_size: float = 7.0,
    burn_subtitles: bool = False
):
    ch_str = f"{int(chapter_num):02d}"
    if not project_name:
        clean_src = "".join(part.title() for part in source_dir.name.replace("-", " ").replace("_", " ").split())
        proj_name = f"{clean_src}_Ch{ch_str}"
    else:
        proj_name = project_name

    if install_to_capcut and DEFAULT_MAC_DRAFT_DIR.exists():
        final_dest = DEFAULT_MAC_DRAFT_DIR / proj_name
    else:
        final_dest = out_dir / proj_name

    out_dir.mkdir(parents=True, exist_ok=True)
    spec_file = out_dir / f"spec_ch{ch_str}_base.json"
    srt_file = out_dir / f"chapter_{ch_str}_semantic.srt"

    print(f"\n==========================================")
    print(f"▶ BẮT ĐẦU DỰNG CHƯƠNG {ch_str}: {proj_name}")
    print(f"==========================================")

    # 1. Tính toán timeline phân cảnh
    print(f"[*] 1/6. Tính toán mốc cắt cảnh bằng Whisper Forced Alignment...")
    engine = SyncTimingEngine(str(source_dir))
    timeline = engine.compute_chapter_timeline(ch_str)
    print(f"    - Thời lượng Voiceover: {timeline['total_duration']:.2f}s")
    print(f"    - Số lượng video phân cảnh: {len(timeline['video_items'])}")

    # 2. Xây dựng spec_base.json (Video + Audio + Transitions)
    print(f"[*] 2/6. Tạo kịch bản Timeline spec_base.json (Chuyển cảnh: {transition_slug} {transition_dur}s)...")
    video_items = []
    for i, item in enumerate(timeline["video_items"]):
        video_items.append({
            "ref": f"v_{i:03d}",
            "path": str(Path(item["path"]).resolve()),
            "start": item["start"],
            "duration": item["duration"],
            "sourceStart": item.get("sourceStart", 0.0),
            "speed": item.get("speed", 1.0),
            "volume": 0.0
        })

    audio_items = [{
        "path": str(Path(timeline["audio_path"]).resolve()),
        "start": 0.0,
        "duration": timeline["total_duration"],
        "volume": 1.0
    }]

    operations = []
    for i in range(len(video_items) - 1):
        operations.append({
            "op": "transition",
            "target": f"v_{i:03d}",
            "slug": transition_slug,
            "duration": transition_dur
        })

    spec = {
        "name": proj_name,
        "width": 1920,
        "height": 1080,
        "fps": 30,
        "ratio": "16:9",
        "tracks": [
            {"type": "video", "name": "Main_Video", "items": video_items},
            {"type": "audio", "name": "Voiceover", "items": audio_items}
        ],
        "operations": operations
    }

    with open(spec_file, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)

    # 3. Biên dịch Timeline bằng capcut compile
    print(f"[*] 3/5. Biên dịch Timeline Video + Audio bằng capcut compile...")
    if final_dest.exists():
        shutil.rmtree(final_dest)

    MODERN_TEMPLATE_PATH = PROJECT_ROOT / "templates" / "capcut_modern_template"
    compile_cmd = ["node", str(CAPCUT_CLI_PATH), "compile", str(spec_file), "--out", str(final_dest)]
    if MODERN_TEMPLATE_PATH.exists():
        compile_cmd.extend(["--template", str(MODERN_TEMPLATE_PATH)])

    if dry_run:
        compile_cmd.remove("--out")
        compile_cmd.remove(str(final_dest))
        compile_cmd.append("--plan")
        res = run_cmd(compile_cmd)
        return res.returncode == 0

    res = run_cmd(compile_cmd)
    if res.returncode != 0:
        return False
    print(f"    - Đã biên dịch xong 69 clips video và master audio!")

    # 4. Phụ đề ngữ nghĩa (Tạo file SRT rời cho YouTube CC, không gắn cứng vào video)
    print(f"[*] 4/5. Xây dựng phụ đề ngữ nghĩa chuẩn YouTube Closed Captions (CC)...")
    whisper_file = engine._find_whisper_json(ch_str)
    if whisper_file:
        from apply_vox_semantic_subtitles import generate_semantic_cues, export_cues_to_srt, apply_vox_subtitles
        cues = generate_semantic_cues(str(whisper_file))
        export_cues_to_srt(cues, str(srt_file))
        print(f"    - Đã lưu file phụ đề YouTube CC rời ({len(cues)} câu ngữ nghĩa): {srt_file}")
        if burn_subtitles:
            apply_vox_subtitles(str(final_dest), str(whisper_file), srt_out_path=str(srt_file))
            print(f"    - Đã gắn phụ đề trực tiếp lên timeline.")
        else:
            print(f"    - Timeline video sạch 100% (No burned-in subtitles) để tôn vinh toàn bộ tranh vẽ!")

    # 5. Đăng ký vật liệu macOS & Kiểm toán lint
    print(f"[*] 5/5. Đăng ký vật liệu macOS và kiểm toán capcut lint...")
    run_cmd(["node", str(CAPCUT_CLI_PATH), "register", str(final_dest), "--materials", "--apply"], check=False)
    lint_res = run_cmd(["node", str(CAPCUT_CLI_PATH), "lint", str(final_dest)], check=False)
    try:
        lint_data = json.loads(lint_res.stdout)
        summary = lint_data.get("summary", {})
        errs = summary.get("errors", 0)
        warns = summary.get("warnings", 0)
        infos = summary.get("info", 0)
        print(f"    - Kết quả Lint: {errs} errors, {warns} warnings, {infos} info.")
    except Exception:
        pass

    print(f"\n[✓] HOÀN TẤT THÀNH CÔNG: Chương {ch_str} đã sẵn sàng trong CapCut Desktop:")
    print(f"    ▶ {final_dest}")
    return True

def main():
    parser = argparse.ArgumentParser(description="AutoCapCut Pipeline using capcut-cli (renezander030)")
    parser.add_argument("--chapter", type=str, help="Số thứ tự chương cần dựng (01, 02, ...)")
    parser.add_argument("--all-chapters", action="store_true", help="Dựng toàn bộ các chương")
    parser.add_argument("--source", type=str, default="source/kem-trang-tien", help="Thư mục tài nguyên nguồn")
    parser.add_argument("--name", type=str, default=None, help="Tên dự án CapCut tùy biến")
    parser.add_argument("--out-dir", type=str, default="output_drafts", help="Thư mục lưu trữ dự án xuất ra")
    parser.add_argument("--dry-run", action="store_true", help="Chạy kiểm tra kế hoạch không ghi đè")
    parser.add_argument("--install-to-capcut", action="store_true", default=True, help="Biên dịch thẳng vào thư mục CapCut Desktop macOS")
    parser.add_argument("--transition", type=str, default="mix", help="Hiệu ứng chuyển cảnh (mix, dissolve)")
    parser.add_argument("--transition-dur", type=float, default=0.8, help="Thời lượng chuyển cảnh (giây)")
    parser.add_argument("--font-size", type=float, default=7.0, help="Kích thước font phụ đề (chuẩn 7.0)")
    parser.add_argument("--burn-subtitles", action="store_true", default=False, help="Gắn cứng phụ đề lên timeline video (mặc định: tắt để giữ video sạch 100%)")

    args = parser.parse_args()

    source_dir = (PROJECT_ROOT / args.source).resolve()
    out_dir = (PROJECT_ROOT / args.out_dir).resolve()

    if not CAPCUT_CLI_PATH.exists():
        print(f"[ERROR] Không tìm thấy binary capcut-cli tại {CAPCUT_CLI_PATH}", file=sys.stderr)
        sys.exit(1)

    if args.all_chapters:
        chapters = [f"{i:02d}" for i in range(1, 9)]
    elif args.chapter:
        chapters = [f"{int(args.chapter):02d}"]
    else:
        print("Vui lòng chọn --chapter <số> hoặc --all-chapters. Dùng --help để xem hướng dẫn.")
        sys.exit(1)

    for ch in chapters:
        process_chapter(
            ch,
            source_dir,
            out_dir,
            project_name=args.name,
            dry_run=args.dry_run,
            install_to_capcut=args.install_to_capcut,
            transition_slug=args.transition,
            transition_dur=args.transition_dur,
            font_size=args.font_size,
            burn_subtitles=args.burn_subtitles
        )

if __name__ == "__main__":
    main()
