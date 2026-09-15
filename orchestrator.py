#!/usr/bin/env python3
"""Video Production Operating System (VPOS) — Master Orchestrator CLI.
Central command tool to audit, coordinate, and monitor production across all stations.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent

CHANNELS = {
    "gocnhin": {
        "name": "Góc Nhìn Podcast",
        "path": BASE_DIR / "GocNhinPodcast",
        "episodes_dir": BASE_DIR / "GocNhinPodcast" / "episodes",
    },
    "dongchay": {
        "name": "Dòng Chảy",
        "path": BASE_DIR / "Dong_Chay",
        "episodes_dir": BASE_DIR / "Dong_Chay" / "episodes",
    },
    "xeconomics": {
        "name": "X-Economics",
        "path": BASE_DIR / "X-Economics",
        "episodes_dir": BASE_DIR / "X-Economics" / "episodes",
    },
}

CORE_STATIONS = {
    "TroLyCaNhan": {"name": "Trợ Lý Cá Nhân (Research & Agents)", "path": BASE_DIR / "TroLyCaNhan"},
    "VideoCore": {"name": "VideoCore (Footage Engine Veo 3.1)", "path": BASE_DIR / "VideoCore"},
    "AutoCapCut": {"name": "AutoCapCut (Assembly Plant)", "path": BASE_DIR / "AutoCapCut"},
    "FacebookChannel": {"name": "FacebookChannel (Distribution Hub)", "path": BASE_DIR / "FacebookChannel"},
}


def cmd_status():
    """Hiển thị bảng kiểm toán tổng thể sức khỏe toàn bộ hệ sinh thái."""
    print("================================================================================")
    print(" 🎬 VPOS: BẢNG ĐIỀU PHỐI HỆ THỐNG SẢN XUẤT VIDEO (CHIEF ORCHESTRATOR)")
    print("================================================================================")
    print(f"Thời gian kiểm toán: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Thư mục gốc: {BASE_DIR}")
    print("--------------------------------------------------------------------------------")

    print("\n🏛️ [CÁC TRẠM SẢN XUẤT CỐT LÕI]:")
    for key, info in CORE_STATIONS.items():
        exists = info["path"].exists()
        status_str = "✅ HOẠT ĐỘNG" if exists else "❌ THIẾU"
        print(f"  • {info['name']:<42} : {status_str} ({info['path'].name})")

    print("\n📺 [TIẾN ĐỘ CÁC KÊNH NỘI DUNG]:")
    for key, cinfo in CHANNELS.items():
        ep_dir = cinfo["episodes_dir"]
        count = 0
        if ep_dir.exists():
            count = len([d for d in ep_dir.iterdir() if d.is_dir() and not d.name.startswith(".")])
        print(f"  • Kênh {cinfo['name']:<25} : {count:>2} tập đã đăng ký trong pipeline")

    print("\n================================================================================")
    print("💡 Gợi ý lệnh:")
    print("  • Khởi tạo tập mới   : python3 orchestrator.py new-episode --channel <kênh> --slug <tên-tập>")
    print("  • Quét tiến độ kênh  : python3 orchestrator.py scan --channel <kênh>")
    print("================================================================================\n")


def cmd_new_episode(channel: str, slug: str, title: str):
    """Khởi tạo một tập video mới chuẩn hợp đồng dữ liệu."""
    ch = CHANNELS.get(channel.lower())
    if not ch:
        print(f"❌ Kênh không hợp lệ. Chọn một trong: {list(CHANNELS.keys())}")
        sys.exit(1)

    slug_clean = slug.strip().lower().replace(" ", "-")
    target_dir = ch["episodes_dir"] / slug_clean

    if target_dir.exists():
        print(f"⚠️ Thư mục tập đã tồn tại: {target_dir}")
        sys.exit(1)

    # Tạo cấu trúc thư mục chuẩn
    for sub in ["prompts", "ref_images", "videos", "audio"]:
        (target_dir / sub).mkdir(parents=True, exist_ok=True)

    # Tạo buc_tranh_toan_canh.md
    with open(target_dir / "buc_tranh_toan_canh.md", "w", encoding="utf-8") as f:
        f.write(f"# Bức Tranh Toàn Cảnh: {title}\n\n")
        f.write(f"**Ngày khởi tạo:** {datetime.now().strftime('%d/%m/%Y')}\n")
        f.write(f"**Kênh:** {ch['name']}\n")
        f.write(f"**Slug:** `{slug_clean}`\n\n---\n\n")
        f.write("## 1. Móc câu dẫn nhập (Hook 60s đầu)\n\n## 2. Bối cảnh & Dữ liệu định lượng thực chứng\n\n## 3. Bản chất thể chế & Cơ chế dòng tiền\n\n## 4. Các luận điểm phản biện & Góc nhìn đối nghịch\n\n## 5. Kết luận có điều kiện & Actionable Insights\n")

    # Tạo README.md
    with open(target_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(f"# Episode: {title}\n\n")
        f.write(f"- **Kênh:** {ch['name']}\n")
        f.write("- **Trạng thái:** `[ ] Đang nghiên cứu kịch bản`\n\n")
        f.write("### Checklist Quy Trình Sản Xuất:\n")
        f.write("- [ ] Bức tranh toàn cảnh & Nghiên cứu dữ liệu\n")
        f.write("- [ ] Bẻ kịch bản phân cảnh (`prompts/`)\n")
        f.write("- [ ] Chạy VideoCore render footage độc bản\n")
        f.write("- [ ] Sinh giọng đọc AI TTS\n")
        f.write("- [ ] AutoCapCut ráp timeline & subtitle\n")
        f.write("- [ ] Chuyển hóa kịch bản Facebook & Upload\n")

    print(f"✅ ĐÃ KHỞI TẠO TẬP MỚI THÀNH CÔNG TẠI:")
    print(f"📁 {target_dir}")


def cmd_scan(channel: str):
    """Quét và phân loại tiến độ các tập của một kênh."""
    ch = CHANNELS.get(channel.lower())
    if not ch or not ch["episodes_dir"].exists():
        print(f"❌ Không tìm thấy kênh: {channel}")
        sys.exit(1)

    print(f"\n🔍 QUÉT TIẾN ĐỘ KÊNH: {ch['name']}")
    print("--------------------------------------------------------------------------------")
    episodes = [d for d in ch["episodes_dir"].iterdir() if d.is_dir() and not d.name.startswith(".")]
    for ep in sorted(episodes, key=lambda x: x.name):
        has_blueprint = (ep / "buc_tranh_toan_canh.md").exists()
        has_prompts = (ep / "prompts").exists() or len(list(ep.glob("prompts*.txt"))) > 0
        has_videos = (ep / "videos").exists() and len(list((ep / "videos").glob("*.mp4"))) > 0
        
        status_icons = []
        status_icons.append("📝 Kịch bản" if has_blueprint else "⚪ Kịch bản")
        status_icons.append("🎬 Prompts" if has_prompts else "⚪ Prompts")
        status_icons.append("📹 Footage" if has_videos else "⚪ Footage")

        print(f"  • {ep.name:<40} : {' | '.join(status_icons)}")
    print("--------------------------------------------------------------------------------\n")


def main():
    parser = argparse.ArgumentParser(description="VPOS Master Orchestrator CLI")
    subparsers = parser.add_subparsers(dest="command", help="Lệnh thực thi")

    # Status
    subparsers.add_parser("status", help="Kiểm toán trạng thái toàn bộ hệ sinh thái")

    # New Episode
    p_new = subparsers.add_parser("new-episode", help="Khởi tạo tập video mới")
    p_new.add_argument("--channel", required=True, choices=list(CHANNELS.keys()), help="Kênh phát hành")
    p_new.add_argument("--slug", required=True, help="Tên mã thư mục (slug không dấu)")
    p_new.add_argument("--title", default="", help="Tiêu đề chính thức của tập")

    # Scan
    p_scan = subparsers.add_parser("scan", help="Quét tiến độ chi tiết các tập")
    p_scan.add_argument("--channel", required=True, choices=list(CHANNELS.keys()), help="Kênh cần quét")

    args = parser.parse_args()

    if args.command == "status" or not args.command:
        cmd_status()
    elif args.command == "new-episode":
        title = args.title or args.slug.replace("-", " ").title()
        cmd_new_episode(args.channel, args.slug, title)
    elif args.command == "scan":
        cmd_scan(args.channel)


if __name__ == "__main__":
    main()
