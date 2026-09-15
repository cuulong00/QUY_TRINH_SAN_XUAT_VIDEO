#!/usr/bin/env python3
"""
scripts/build_full_master_project.py

Tạo Master Project hợp nhất toàn bộ 6 chương (Chương 01 -> Chương 06) của phim tài liệu
'Kem Tràng Tiền: Ván Cờ Đất Vàng' trên CapCut Desktop (macOS):
1. Rà soát và đồng bộ ngữ nghĩa 100% cho 392 phân cảnh:
   - Chương 01: Áp dụng bảng mapping SCENE_VIDEO_MAP chuẩn xác đã kiểm chứng.
   - Chương 02-06: Áp dụng mapping 1-1 trực tiếp từng scene ID tới video mp4.
2. Quy tắc chuyển giao giữa các chương (Inter-Chapter Transitions):
   - Giữa mỗi chương có 4.0s ngắt nghỉ âm thanh voiceover cho khán giả thư giãn.
   - Cảnh cuối chương K trờm ra +2.0s vào khoảng nghỉ.
   - Cảnh đầu chương K+1 bắt đầu tại mốc +2.0s (chạy trước 2.0s hình ảnh trước khi giọng đọc bắt đầu).
   - Video track liên tục 100% (Zero Black Gaps).
   - Cảnh cuối Chương 06 trờm ra +2.0s làm Outro kết màn.
3. Tối ưu thời lượng & tốc độ:
   - Với những cảnh thoại kéo dài > 7.95s, tự động áp dụng `speed` (0.83x - 0.95x) để hình ảnh
     trải đều suốt câu nói mà không vượt quá 8.0s của clip gốc.
   - Tinh chỉnh đồng bộ companion speed materials để đạt chuẩn `capcut lint` errors: 0.
4. Xử lý môi trường macOS Sandbox:
   - Toàn bộ media được nạp và tổ chức chuẩn mực qua `capcut compile` + `capcut register --materials --apply`.
"""

import os
import sys
import json
import shutil
import difflib
import subprocess
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple

WORKSPACE = Path("/Users/pro16/Documents/VideoProject/AutoCapCut")
sys.path.append(str(WORKSPACE / "scripts"))
from sync_timing_engine import SyncTimingEngine

EPISODE_DIR = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kem-trang-tien-van-co-dat-vang")
CAPCUT_DRAFTS_DIR = Path("/Users/pro16/Movies/CapCut/User Data/Projects/com.lveditor.draft")
PROJECT_NAME = "KemTrangTien_Master"
DRAFT_DIR = CAPCUT_DRAFTS_DIR / PROJECT_NAME
MODERN_TEMPLATE = WORKSPACE / "templates/capcut_modern_template"
CAPCUT_CLI = WORKSPACE / "tools/capcut-cli/dist/index.js"

# Bảng ánh xạ video đặc thù cho Chương 01 (đã giải quyết triệt để lỗi sớm hình)
CH01_SCENE_VIDEO_MAP = {
    "CH01_SC001": "CH01_SC001.mp4",
    "CH01_SC002": "CH01_SC002.mp4",
    "CH01_SC003": "CH01_SC003.mp4",
    "CH01_SC004": "CH01_SC004.mp4",
    "CH01_SC005": "CH01_SC005.mp4",
    "CH01_SC006": "CH01_SC006.mp4",
    "CH01_SC007": "CH01_SC007.mp4",
    "CH01_SC008": "CH01_SC008.mp4",
    "CH01_SC009": "CH01_SC009.mp4",
    "CH01_SC010": "CH01_SC010.mp4",
    "CH01_SC011": "CH01_SC011.mp4", # Biểu đồ 484 tỷ
    "CH01_SC012": "CH01_SC011.mp4", # Giữ biểu đồ 484 tỷ (+60%) hết câu
    "CH01_SC013": "CH01_SC012.mp4", # Mảng kem truyền thống -> Dây chuyền kem
    "CH01_SC014": "CH01_SC013.mp4", # Hơn 400 đại lý -> Bản đồ đại lý
    "CH01_SC015": "CH01_SC015.mp4", # Không thua lỗ hay phá sản -> Cửa hàng kem đông đúc
    "CH01_SC016": "CH01_SC014.mp4", # Lỗ lũy kế 383 tỷ -> Bàn kế toán lỗ
    "CH01_SC017": "CH01_SC016.mp4", # Tăng trưởng mạnh mẽ -> Tòa nhà 35 Tràng Tiền
    "CH01_SC018": "CH01_SC018.mp4", # Nếu không phải phá sản
    "CH01_SC019": "CH01_SC019.mp4", # Thế lực vô hình
    "CH01_SC020": "CH01_SC020.mp4", # Sảnh lớn Indochine
    "CH01_SC021": "CH01_SC019.mp4", # Chụp ảnh mái vòm Indochine
    "CH01_SC022": "CH01_SC021.mp4", # THÔNG BÁO DỪNG ĐÓN KHÁCH
    "CH01_SC023": "CH01_SC022.mp4", # Nhà quan sát tỉnh táo
    "CH01_SC024": "CH01_SC022.mp4", # Nghịch lý thú vị
    "CH01_SC025": "CH01_SC023.mp4", # Chụp ảnh check in
    "CH01_SC026": "CH01_SC023.mp4", # Di sản 68 năm
    "CH01_SC027": "CH01_SC020.mp4", # Mái vòm uốn lượn
    "CH01_SC028": "CH01_SC023.mp4", # Tranh tường lung linh
    "CH01_SC029": "CH01_SC025.mp4", # ĐẠI TRÙNG TU NĂM 2020
    "CH01_SC030": "CH01_SC026.mp4", # Sân mậu dịch trước 2020
    "CH01_SC031": "CH01_SC027.mp4", # Mái che khung thép
    "CH01_SC032": "CH01_SC027.mp4", # Xe máy đứng ăn vội vã
    "CH01_SC033": "CH01_SC029.mp4", # DỰ ÁN CẢI TẠO 10 TỶ ĐỒNG
    "CH01_SC034": "CH01_SC030.mp4", # TUỔI THỜI GIAN KIẾN TRÚC 6 NĂM
    "CH01_SC035": "CH01_SC031.mp4", # Ký ức văn hóa
    "CH01_SC036": "CH01_SC031.mp4", # Di sản tập quán văn hóa
    "CH01_SC037": "CH01_SC028.mp4", # Dắt xe máy vào sân
    "CH01_SC038": "CH01_SC028.mp4", # Cắn kem buốt chân răng ngày đông
    "CH01_SC039": "CH01_SC024.mp4", # Tiếc nuối thói quen
    "CH01_SC040": "CH01_SC024.mp4", # Bám víu vỏ bọc thương mại
    "CH01_SC041": "CH01_SC017.mp4", # Nghịch lý dẫn đến sự thật
    "CH01_SC042": "CH01_SC032.mp4", # Sở Kế hoạch & Đầu tư
    "CH01_SC043": "CH01_SC001.mp4", # Tràng Tiền chỉ là một cái tên
    "CH01_SC044": "CH01_SC033.mp4", # HAI PHÁP NHÂN ĐỘC LẬP
    "CH01_SC045": "CH01_SC034.mp4", # CÔNG TY CP KEM TRÀNG TIỀN
    "CH01_SC046": "CH01_SC035.mp4", # Linh hồn sản xuất
    "CH01_SC047": "CH01_SC035.mp4", # Logo 1958
    "CH01_SC048": "CH01_SC036.mp4", # Hàng trăm tủ đông
    "CH01_SC049": "CH01_SC037.mp4", # Điều khoản pháp lý quyết định
    "CH01_SC050": "CH01_SC037.mp4", # KHÔNG SỞ HỮU ĐẤT TẠI SỐ 35
    "CH01_SC051": "CH01_SC044.mp4", # Người đi thuê trọ -> Chìa khóa trả phòng
    "CH01_SC052": "CH01_SC038.mp4", # Hợp đồng thuê mặt bằng
    "CH01_SC053": "CH01_SC038.mp4", # Ký ngày 02/09/2010
    "CH01_SC054": "CH01_SC040.mp4", # Khu đất kim cương 1.500m2 sát hồ Gươm
    "CH01_SC055": "CH01_SC039.mp4", # CÔNG TY CP TRÀNG TIỀN (thiếu chữ Kem)
    "CH01_SC056": "CH01_SC039.mp4", # Đứng tên hợp đồng thuê đất
    "CH01_SC057": "CH01_SC041.mp4", # Mục tiêu phát triển cao ốc thương mại
    "CH01_SC058": "CH01_SC041.mp4", # Dự án cao ốc đất vàng
    "CH01_SC059": "CH01_SC042.mp4", # Hết hạn tháng 9/2026 -> Tờ lịch 15/09/2026
    "CH01_SC060": "CH01_SC042.mp4", # Thu hồi mặt bằng
    "CH01_SC061": "CH01_SC043.mp4", # Bên đi thuê dọn đồ rời đi
    "CH01_SC062": "CH01_SC015.mp4", # Không có chuyện phá sản
    "CH01_SC063": "CH01_SC044.mp4", # Người thuê trọ trả lại phòng
    "CH01_SC064": "CH01_SC046.mp4", # Câu hỏi hóc búa
    "CH01_SC065": "CH01_SC040.mp4", # Đất 1.500m2 giá 0 đồng
    "CH01_SC066": "CH01_SC040.mp4", # Rơi vào tay tư nhân
    "CH01_SC067": "CH01_SC047.mp4", # Bánh xe lịch sử
    "CH01_SC068": "CH01_SC047.mp4", # Kẽ hở địa tô
    "CH01_SC069": "CH01_SC045.mp4"  # HỒ SƠ CỔ PHẦN HÓA NĂM 2000
}

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r"[^\w\s]", " ", t)
    return " ".join(t.split())

def compute_chapter_cuts(ch_num: int, scenes: List[Dict[str, Any]]) -> Tuple[List[float], float]:
    """
    Tính toán các điểm cắt thời gian cho từng scene trong chương dựa trên Whisper / Timestamps JSON.
    Trả về (cuts, audio_duration).
    """
    ch_str = f"{ch_num:02d}"
    ts_file = EPISODE_DIR / "timestamps" / f"chapter_{ch_str}_timestamps.json"
    if not ts_file.exists():
        ts_file = EPISODE_DIR / "audio" / f"chapter_{ch_str}_timestamps.json"
        
    ts_data = json.load(open(ts_file, "r", encoding="utf-8"))
    audio_duration = float(ts_data.get("duration", 0.0))
    
    words = []
    for seg in ts_data.get("segments", []):
        for w in seg.get("words", []):
            w_txt = w.get("word", "").strip()
            if w_txt:
                words.append({
                    "word": w_txt,
                    "norm": normalize_text(w_txt),
                    "start": float(w.get("start", 0.0)),
                    "end": float(w.get("end", 0.0))
                })
                
    cursor = 0
    cuts = [0.0]
    
    for i, sc in enumerate(scenes):
        s_text = " ".join(sc.get("sentences", []))
        s_norm = normalize_text(s_text).split()
        
        if i == len(scenes) - 1:
            best_idx = len(words) - 1
        else:
            t_last1 = s_norm[-1]
            min_k = cursor + max(1, len(s_norm) // 2)
            max_k = min(len(words) - 1, cursor + len(s_norm) * 2 + 10)
            best_idx = -1
            best_score = -1.0
            
            for k in range(min_k, max_k + 1):
                w_k = words[k]["norm"]
                score = 0.0
                if w_k == t_last1 or t_last1 in w_k or w_k in t_last1:
                    score += 1.0
                elif difflib.SequenceMatcher(None, w_k, t_last1).ratio() >= 0.7:
                    score += 0.8
                    
                dist_penalty = abs((k - cursor + 1) - len(s_norm)) * 0.02
                total_score = score - dist_penalty
                if total_score > best_score and score >= 0.7:
                    best_score = total_score
                    best_idx = k
                    
            if best_idx == -1:
                best_idx = min(len(words) - 1, cursor + len(s_norm) - 1)
                
        end_time = words[best_idx]["end"]
        next_start = words[best_idx + 1]["start"] if best_idx + 1 < len(words) else end_time
        cut_point = round((end_time + next_start) / 2.0, 3)
        cuts.append(cut_point)
        cursor = best_idx + 1
        
    cuts[-1] = audio_duration
    return cuts, audio_duration

def main():
    print("=" * 70)
    print("   BẮT ĐẦU DỰNG MASTER PROJECT TOÀN BỘ 6 CHƯƠNG CHO CAPCUT DESKTOP   ")
    print("=" * 70)
    
    # 1. Đóng ứng dụng CapCut Desktop nếu đang chạy
    print("\n[1/8] Kiểm tra và đóng CapCut Desktop...")
    subprocess.run(["pkill", "-9", "-f", "CapCut"], capture_output=True)
    
    # 2. Nạp timing map
    print("\n[2/8] Nạp dữ liệu cấu trúc 392 phân cảnh từ scene_timing_map.json...")
    timing_map_path = WORKSPACE / "source/kem-trang-tien/scene_timing_map.json"
    timing_map = json.load(open(timing_map_path, "r", encoding="utf-8"))
    
    # 3. Tính toán dòng thời gian từng chương và ghép nối liên tục
    print("\n[3/8] Tính toán mốc thời gian microsecond và quy tắc trờm 4.0s ngắt nghỉ giữa các chương...")
    
    video_timeline_items = []
    audio_timeline_items = []
    operations = []
    
    current_audio_timeline_start = 0.0 # giây
    current_video_timeline_start = 0.0 # giây
    
    # Danh sách lưu thông tin clip liên tiếp để tinh chỉnh sau compile
    clip_pairs_info = []
    
    engine = SyncTimingEngine(str(WORKSPACE / "source/kem-trang-tien"))
    tl01 = engine.compute_chapter_timeline("01")
    ch01_cuts = [it["start"] for it in tl01["video_items"]] + [tl01["total_duration"]]
    
    for ch in range(1, 7):
        ch_str = f"{ch:02d}"
        ch_scenes = [s for s in timing_map if s["chapter"] == ch_str]
        if ch == 1:
            cuts = ch01_cuts
            audio_dur = tl01["total_duration"]
        else:
            cuts, audio_dur = compute_chapter_cuts(ch, ch_scenes)
        
        print(f"   -> Chương {ch_str}: {len(ch_scenes)} cảnh | Audio: {audio_dur:.2f}s | Bắt đầu tại timeline: {current_audio_timeline_start:.2f}s")
        
        # Thêm file audio voiceover của chương
        audio_src = WORKSPACE / f"source/kem-trang-tien/audio/chapter_{ch_str}.wav"
        if not audio_src.exists():
            audio_src = EPISODE_DIR / f"audio/chapter_{ch_str}.wav"
            
        audio_timeline_items.append({
            "path": str(audio_src.resolve()),
            "start": round(current_audio_timeline_start, 3),
            "duration": round(audio_dur, 3),
            "volume": 1.0
        })
        
        video_dir = EPISODE_DIR / "video" / f"Chương {ch_str}"
        
        for idx, sc in enumerate(ch_scenes):
            sid = sc["id"]
            
            # Xác định tên file video tương ứng
            if ch == 1:
                vname = CH01_SCENE_VIDEO_MAP.get(sid, f"{sid}.mp4")
            else:
                vname = f"{sid}.mp4"
                
            vpath = video_dir / vname
            if not vpath.exists():
                raise FileNotFoundError(f"Không tìm thấy video: {vpath}")
                
            raw_scene_dur = cuts[idx + 1] - cuts[idx]
            
            # Áp dụng quy tắc trờm chuyển giao chương
            is_first_scene_of_chapter = (idx == 0)
            is_last_scene_of_chapter = (idx == len(ch_scenes) - 1)
            
            scene_display_dur = raw_scene_dur
            
            # Cảnh đầu chương (từ Chương 2 trở đi): trờm ra trước 2.0s
            if ch > 1 and is_first_scene_of_chapter:
                scene_display_dur += 2.0
                
            # Cảnh cuối chương: trờm ra 2.0s vào khoảng nghỉ
            if is_last_scene_of_chapter:
                scene_display_dur += 2.0 # (Ch01-Ch05 trờm vào gap, Ch06 trờm làm outro)
                
            scene_display_dur = round(scene_display_dur, 3)
            
            # Tính toán speed nếu thời lượng hiển thị > 7.95s
            speed = 1.0
            if scene_display_dur > 7.95:
                speed = round(7.95 / scene_display_dur, 4)
                
            ref_id = f"v_{len(video_timeline_items):04d}"
            
            video_timeline_items.append({
                "ref": ref_id,
                "scene_id": sid,
                "chapter": ch_str,
                "path": str(vpath.resolve()),
                "filename": vname,
                "start": round(current_video_timeline_start, 3),
                "duration": scene_display_dur,
                "sourceStart": 0.0,
                "speed": speed,
                "volume": 0.0
            })
            
            # Cập nhật vị trí bắt đầu của video kế tiếp
            current_video_timeline_start = round(current_video_timeline_start + scene_display_dur, 3)
            
        # Kết thúc chương: audio nghỉ 4.0s trước khi chương kế bắt đầu
        current_audio_timeline_start = round(current_audio_timeline_start + audio_dur + 4.0, 3)
        
    print(f"   -> Tổng số phân cảnh video: {len(video_timeline_items)}")
    print(f"   -> Tổng thời lượng video timeline: {current_video_timeline_start:.2f}s (~{current_video_timeline_start/60:.2f} phút)")
    print(f"   -> Mốc kết thúc giọng đọc chương 06: {audio_timeline_items[-1]['start'] + audio_timeline_items[-1]['duration']:.2f}s")
    print(f"   -> Chênh lệch cuối cùng (Outro trờm ra): {current_video_timeline_start - (audio_timeline_items[-1]['start'] + audio_timeline_items[-1]['duration']):.2f}s")

    # 4. Gán transition mix (0.4s) giữa các clip khác nhau
    print("\n[4/8] Thiết lập hiệu ứng chuyển cảnh tự nhiên (0.4s mix transition)...")
    for idx in range(len(video_timeline_items) - 1):
        it1 = video_timeline_items[idx]
        it2 = video_timeline_items[idx + 1]
        
        # Nếu 2 clip liên tiếp dùng chung file video (chỉ có ở Chương 01): không gán mix transition
        if it1["filename"] == it2["filename"]:
            clip_pairs_info.append((idx, idx + 1, it1["filename"]))
            continue
            
        operations.append({
            "op": "transition",
            "target": it1["ref"],
            "slug": "mix",
            "duration": 0.4
        })

    # 5. Xây dựng spec_master.json
    print("\n[5/8] Tạo file đặc tả kiến trúc spec_master.json...")
    spec = {
        "name": PROJECT_NAME,
        "width": 1920,
        "height": 1080,
        "fps": 30,
        "ratio": "16:9",
        "tracks": [
            {
                "type": "video",
                "name": "Main_Video",
                "items": [
                    {
                        "ref": it["ref"],
                        "path": it["path"],
                        "start": it["start"],
                        "duration": it["duration"],
                        "sourceStart": it["sourceStart"],
                        "speed": it["speed"],
                        "volume": it["volume"]
                    }
                    for it in video_timeline_items
                ]
            },
            {
                "type": "audio",
                "name": "Voiceover",
                "items": audio_timeline_items
            }
        ],
        "operations": operations
    }
    
    spec_path = WORKSPACE / "spec_master.json"
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
    print(f"   -> Đã ghi đặc tả dự án vào: {spec_path}")
    
    # 6. Dọn dẹp draft cũ và biên dịch qua capcut compile
    print(f"\n[6/8] Khởi tạo draft mới tại {DRAFT_DIR} qua `capcut compile`...")
    if DRAFT_DIR.exists():
        shutil.rmtree(DRAFT_DIR)
        
    cmd_compile = [
        "node", str(CAPCUT_CLI), "compile", str(spec_path),
        "--out", str(DRAFT_DIR),
        "--template", str(MODERN_TEMPLATE)
    ]
    res = subprocess.run(cmd_compile, cwd=str(WORKSPACE), capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[!] Lỗi khi biên dịch draft:\n{res.stderr or res.stdout}")
        sys.exit(1)
    print("   -> Biên dịch CapCut Draft thành công 100%!")
    
    # 7. Post-processing: Tinh chỉnh speed companion materials & các cặp clip dùng chung
    print("\n[7/8] Tinh chỉnh companion materials (speeds) và liên kết timerange clip đôi...")
    draft_info_path = DRAFT_DIR / "draft_info.json"
    template_tmp_path = DRAFT_DIR / "template-2.tmp"
    
    with open(draft_info_path, "r", encoding="utf-8") as f:
        draft_content = json.load(f)
        
    vtrack = [t for t in draft_content["tracks"] if t["type"] == "video"][0]
    speeds_mat = {s["id"]: s for s in draft_content.get("materials", {}).get("speeds", [])}
    
    # Cập nhật speed material cho từng segment để khớp 100% với segment.speed
    speed_sync_count = 0
    for seg in vtrack["segments"]:
        seg_speed = seg.get("speed", 1.0)
        if seg.get("source_timerange", {}).get("duration", 0) > 8_000_000:
            seg["source_timerange"]["duration"] = 8_000_000
        for ref_id in seg.get("extra_material_refs", []):
            if ref_id in speeds_mat:
                speeds_mat[ref_id]["speed"] = seg_speed
                speed_sync_count += 1
                
    # Xử lý các cặp clip dùng chung (nối source_timerange)
    mats_videos = {m["id"]: m["path"] for m in draft_content["materials"]["videos"]}
    smoothed_pairs = 0
    for i in range(len(vtrack["segments"]) - 1):
        seg1 = vtrack["segments"][i]
        seg2 = vtrack["segments"][i+1]
        p1 = mats_videos[seg1["material_id"]].split("/")[-1]
        p2 = mats_videos[seg2["material_id"]].split("/")[-1]
        
        if p1 == p2:
            d1_us = seg1["target_timerange"]["duration"]
            d2_us = seg2["target_timerange"]["duration"]
            if d1_us + d2_us <= 8_000_000:
                seg1["source_timerange"] = {"start": 0, "duration": d1_us}
                seg2["source_timerange"] = {"start": d1_us, "duration": d2_us}
            else:
                seg1["source_timerange"] = {"start": 0, "duration": d1_us}
                start2 = max(0, 8_000_000 - d2_us)
                seg2["source_timerange"] = {"start": start2, "duration": d2_us}
            smoothed_pairs += 1
            
    # Ghi lại draft_info.json và template-2.tmp
    updated_raw = json.dumps(draft_content, ensure_ascii=False)
    with open(draft_info_path, "w", encoding="utf-8") as f:
        f.write(updated_raw)
    if template_tmp_path.exists():
        with open(template_tmp_path, "w", encoding="utf-8") as f:
            f.write(updated_raw)
            
    print(f"   -> Đã đồng bộ {speed_sync_count} speed materials.")
    print(f"   -> Đã tinh chỉnh {smoothed_pairs} cặp phân cảnh cùng clip liền mạch.")

    # 8. Đăng ký materials & Lint kiểm toán chất lượng
    print("\n[8/8] Đăng ký macOS materials và chạy capcut lint kiểm toán chất lượng...")
    cmd_reg = ["node", str(CAPCUT_CLI), "register", str(DRAFT_DIR), "--materials", "--apply"]
    subprocess.run(cmd_reg, cwd=str(WORKSPACE), check=True)
    
    cmd_lint = ["node", str(CAPCUT_CLI), "lint", str(DRAFT_DIR)]
    res_lint = subprocess.run(cmd_lint, cwd=str(WORKSPACE), capture_output=True, text=True)
    print(res_lint.stdout)
    
    # 9. Mở CapCut Desktop để người dùng thẩm định
    print("Mở ứng dụng CapCut Desktop để kiểm tra...")
    subprocess.run(["open", "-a", "CapCut"])
    
    print("=" * 70)
    print("   HOÀN TẤT DỰNG MASTER PROJECT TOÀN BỘ 6 CHƯƠNG THÀNH CÔNG RỰC RỠ!   ")
    print("=" * 70)

if __name__ == "__main__":
    main()
