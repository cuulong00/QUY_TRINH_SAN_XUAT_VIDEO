#!/usr/bin/env python3
"""
scripts/realign_ch01_timeline.py
Realigns Chapter 01 video timeline to match spoken sentences semantically.
Ensures zero drift, zero unsupported media, and 100% visual-audio synchronization.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

# Paths
WORKSPACE = Path("/Users/pro16/Documents/VideoProject/AutoCapCut")
VIDEO_SOURCE = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kem-trang-tien-van-co-dat-vang/video/Chương 01")
AUDIO_FILE = WORKSPACE / "source/kem-trang-tien/audio/chapter_01.wav"
WHISPER_FILE = WORKSPACE / "source/kem-trang-tien/audio/chapter_01_whisper_turbo.json"
DRAFT_DIR = Path("/Users/pro16/Movies/CapCut/User Data/Projects/com.lveditor.draft/KemTrangTien_Ch01")
DRAFT_ASSETS = DRAFT_DIR / "assets"

sys.path.append(str(WORKSPACE / "scripts"))
from sync_timing_engine import SyncTimingEngine

def get_semantic_segments():
    """
    Returns the list of semantic video segments with exact start, end, and assigned video file.
    """
    engine = SyncTimingEngine(str(WORKSPACE / "source/kem-trang-tien"))
    tl = engine.compute_chapter_timeline("01")
    cut_map = {it["scene_id"]: it for it in tl["video_items"]}
    
    # Helper to get start of first scene and end of last scene
    def get_range(first_sc, last_sc):
        start = cut_map[first_sc]["start"]
        end = cut_map[last_sc]["start"] + cut_map[last_sc]["duration"]
        return round(start, 6), round(end, 6)

    # Define semantic mapping: (start_scene, end_scene, video_clip_filename, description)
    mapping = [
        ("CH01_SC001", "CH01_SC001", "CH01_SC001.mp4", "Phố Tràng Tiền mùa thu"),
        ("CH01_SC002", "CH01_SC002", "CH01_SC002.mp4", "Dòng người xếp hàng"),
        ("CH01_SC003", "CH01_SC003", "CH01_SC003.mp4", "Que kem 15.000 VNĐ"),
        ("CH01_SC004", "CH01_SC004", "CH01_SC004.mp4", "Ông cháu chào từ biệt"),
        ("CH01_SC005", "CH01_SC005", "CH01_SC005.mp4", "Cổng vòm đóng cửa 15/09/2026"),
        ("CH01_SC006", "CH01_SC006", "CH01_SC006.mp4", "Mạng xã hội đồn đoán hoang mang"),
        ("CH01_SC007", "CH01_SC007", "CH01_SC007.mp4", "Biểu tượng mậu dịch bao cấp"),
        ("CH01_SC008", "CH01_SC008", "CH01_SC008.mp4", "Bảng PHÁ SẢN? trên sổ sách"),
        ("CH01_SC009", "CH01_SC009", "CH01_SC009.mp4", "Sổ sách tài chính thực tế"),
        ("CH01_SC010", "CH01_SC010", "CH01_SC010.mp4", "Trụ sở tập đoàn mẹ OCH"),
        # SC011 + SC012: Hold chart until end of 60%
        ("CH01_SC011", "CH01_SC012", "CH01_SC011.mp4", "Biểu đồ 484 tỷ (+60%) chạy hết câu"),
        ("CH01_SC013", "CH01_SC013", "CH01_SC012.mp4", "Mảng kem truyền thống -> Dây chuyền sản xuất kem"),
        ("CH01_SC014", "CH01_SC014", "CH01_SC013.mp4", "Mở rộng 400 đại lý -> Bản đồ 400+ ĐẠI LÝ"),
        ("CH01_SC015", "CH01_SC015", "CH01_SC015.mp4", "Doanh nghiệp không phá sản -> Cửa hàng đông đúc"),
        ("CH01_SC016", "CH01_SC016", "CH01_SC014.mp4", "Lỗ lũy kế 383 tỷ -> Bàn kế toán LỖ LŨY KẾ 383 TỶ"),
        ("CH01_SC017", "CH01_SC017", "CH01_SC016.mp4", "Mảng kem tăng trưởng mạnh mẽ -> Tòa nhà 35 Tràng Tiền"),
        ("CH01_SC018", "CH01_SC018", "CH01_SC018.mp4", "Vậy nếu không phải phá sản"),
        ("CH01_SC019", "CH01_SC019", "CH01_SC019.mp4", "Thế lực vô hình nào -> Thanh niên cầm điện thoại"),
        ("CH01_SC020", "CH01_SC020", "CH01_SC020.mp4", "Sảnh lớn 35 Tràng Tiền mái vòm"),
        ("CH01_SC021", "CH01_SC021", "CH01_SC019.mp4", "Chụp ảnh mái vòm xanh Indochine"),
        ("CH01_SC022", "CH01_SC022", "CH01_SC021.mp4", "THÔNG BÁO DỪNG ĐÓN KHÁCH"),
        ("CH01_SC023", "CH01_SC024", "CH01_SC022.mp4", "Nhà quan sát tỉnh táo"),
        ("CH01_SC025", "CH01_SC026", "CH01_SC023.mp4", "Check in không gian di sản 68 năm"),
        ("CH01_SC027", "CH01_SC028", "CH01_SC020.mp4", "Kiến trúc mái vòm tranh tường"),
        ("CH01_SC029", "CH01_SC029", "CH01_SC025.mp4", "ĐẠI TRÙNG TU NĂM 2020"),
        ("CH01_SC030", "CH01_SC030", "CH01_SC026.mp4", "Sân mậu dịch trước 2020"),
        ("CH01_SC031", "CH01_SC032", "CH01_SC027.mp4", "Mái che khung thép dựng xe ăn kem"),
        ("CH01_SC033", "CH01_SC033", "CH01_SC029.mp4", "DỰ ÁN CẢI TẠO 10 TỶ ĐỒNG"),
        ("CH01_SC034", "CH01_SC034", "CH01_SC030.mp4", "TUỔI THỜI GIAN KIẾN TRÚC 6 NĂM"),
        ("CH01_SC035", "CH01_SC036", "CH01_SC031.mp4", "Di sản đích thực là tập quán văn hóa"),
        ("CH01_SC037", "CH01_SC038", "CH01_SC028.mp4", "Dắt xe máy đứng ăn kem buốt răng ngày đông"),
        ("CH01_SC039", "CH01_SC040", "CH01_SC024.mp4", "Tiếc nuối thói quen bám víu vỏ bọc"),
        ("CH01_SC041", "CH01_SC041", "CH01_SC017.mp4", "Nghịch lý dẫn đến sự thật sửng sốt"),
        ("CH01_SC042", "CH01_SC042", "CH01_SC032.mp4", "Hai bộ hồ sơ tại Sở KH&ĐT"),
        ("CH01_SC043", "CH01_SC043", "CH01_SC001.mp4", "Tràng Tiền chỉ là một cái tên duy nhất"),
        ("CH01_SC044", "CH01_SC044", "CH01_SC033.mp4", "HAI PHÁP NHÂN ĐỘC LẬP"),
        ("CH01_SC045", "CH01_SC045", "CH01_SC034.mp4", "CÔNG TY CỔ PHẦN KEM TRÀNG TIỀN"),
        ("CH01_SC046", "CH01_SC047", "CH01_SC035.mp4", "Nắm giữ linh hồn sản xuất, logo 1958"),
        ("CH01_SC048", "CH01_SC048", "CH01_SC036.mp4", "Hàng trăm tủ đông phủ khắp tỉnh thành"),
        ("CH01_SC049", "CH01_SC050", "CH01_SC037.mp4", "KHÔNG SỞ HỮU ĐẤT TẠI SỐ 35"),
        ("CH01_SC051", "CH01_SC051", "CH01_SC044.mp4", "Vị thế chỉ là một người đi thuê trọ"),
        ("CH01_SC052", "CH01_SC053", "CH01_SC038.mp4", "HỢP ĐỒNG THUÊ MẶT BẰNG 02/09/2010"),
        ("CH01_SC054", "CH01_SC054", "CH01_SC040.mp4", "Khu đất kim cương 1.500m2 sát hồ Gươm"),
        ("CH01_SC055", "CH01_SC056", "CH01_SC039.mp4", "CÔNG TY CỔ PHẦN TRÀNG TIỀN (thiếu chữ Kem)"),
        ("CH01_SC057", "CH01_SC058", "CH01_SC041.mp4", "Dự án cao ốc thương mại trên đất vàng"),
        ("CH01_SC059", "CH01_SC060", "CH01_SC042.mp4", "Hết hạn hợp đồng tháng 9/2026 thu hồi đất"),
        ("CH01_SC061", "CH01_SC061", "CH01_SC043.mp4", "Dọn đồ rời đi"),
        ("CH01_SC062", "CH01_SC062", "CH01_SC015.mp4", "Không hề có chuyện phá sản"),
        ("CH01_SC063", "CH01_SC063", "CH01_SC044.mp4", "Người thuê trọ trả lại phòng"),
        ("CH01_SC064", "CH01_SC064", "CH01_SC046.mp4", "Câu hỏi hóc búa hơn"),
        ("CH01_SC065", "CH01_SC066", "CH01_SC040.mp4", "Làm thế nào rơi vào tay tư nhân giá 0 đồng"),
        ("CH01_SC067", "CH01_SC068", "CH01_SC047.mp4", "Bánh xe lịch sử & kẽ hở địa tô chấn động"),
        ("CH01_SC069", "CH01_SC069", "CH01_SC045.mp4", "HỒ SƠ CỔ PHẦN HÓA NĂM 2000")
    ]

    segments = []
    prev_end = 0.0
    for start_sc, end_sc, vid_name, desc in mapping:
        s_time, e_time = get_range(start_sc, end_sc)
        if prev_end > 0.0 and abs(s_time - prev_end) > 0.0001:
            s_time = prev_end
        
        dur = round(e_time - s_time, 6)
        vid_path = VIDEO_SOURCE / vid_name
        if not vid_path.exists():
            raise FileNotFoundError(f"Video file not found: {vid_path}")
            
        speed = 1.0
        if dur > 8.0:
            speed = round(8.0 / dur, 4)

        segments.append({
            "start_scene": start_sc,
            "end_scene": end_sc,
            "video_file": str(vid_path),
            "video_name": vid_name,
            "start": s_time,
            "duration": dur,
            "end": e_time,
            "speed": speed,
            "desc": desc
        })
        prev_end = e_time

    audio_dur = tl["total_duration"]
    if segments:
        segments[-1]["end"] = audio_dur
        segments[-1]["duration"] = round(audio_dur - segments[-1]["start"], 6)

    return segments, audio_dur

if __name__ == "__main__":
    segs, total_dur = get_semantic_segments()
    print(f"Total semantic segments: {len(segs)}")
    print(f"Total timeline duration: {total_dur}s")
    for idx, s in enumerate(segs, 1):
        print(f"{idx:02d}. [{s['start']:6.2f}s - {s['end']:6.2f}s | {s['duration']:5.2f}s] {s['video_name']:<16} ({s['desc']})")
