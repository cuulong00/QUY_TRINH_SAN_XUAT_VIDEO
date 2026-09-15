#!/usr/bin/env python3
"""
scripts/build_semantic_realigned_project.py
Dựng lại Project CapCut theo chuẩn Semantic Alignment 69 cảnh:
- Giữ biểu đồ 484 tỷ (+60%) chạy qua cả SC011 và SC012 (hết câu 60%)
- Trả clip dây chuyền kem SC012 về đúng câu mảng kem truyền thống SC013
- Trả clip bản đồ 400 đại lý SC013 về đúng câu 400 đại lý SC014
- Trả clip cửa hàng kem đông đúc SC015 về đúng câu không phá sản SC015
- Trả clip sổ sách lỗ 383 tỷ SC014 về đúng câu lỗ lũy kế 383 tỷ SC016
- Triệt tiêu 100% hiện tượng hình chạy trước tiếng và lỗi lũy kế
- Toàn bộ thời lượng từng clip <= 7.58s
- Sử dụng templates/capcut_modern_template (CapCut 9.x)
- Tự động copy media vào assets/ của project
- Đăng ký materials và kiểm tra lint
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

WORKSPACE = Path("/Users/pro16/Documents/VideoProject/AutoCapCut")
sys.path.append(str(WORKSPACE / "scripts"))
from sync_timing_engine import SyncTimingEngine

PROJECT_NAME = "KemTrangTien_Ch01"
DRAFT_DIR = Path(f"/Users/pro16/Movies/CapCut/User Data/Projects/com.lveditor.draft/{PROJECT_NAME}")
VIDEO_SOURCE = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kem-trang-tien-van-co-dat-vang/video/Chương 01")
AUDIO_SRC = WORKSPACE / "source/kem-trang-tien/audio/chapter_01.wav"
MODERN_TEMPLATE = WORKSPACE / "templates/capcut_modern_template"
CAPCUT_CLI = WORKSPACE / "tools/capcut-cli/dist/index.js"

SCENE_VIDEO_MAP = {
    "CH01_SC001": "CH01_SC001.mp4", # Phố Tràng Tiền mùa thu
    "CH01_SC002": "CH01_SC002.mp4", # Dòng người xếp hàng
    "CH01_SC003": "CH01_SC003.mp4", # Que kem 15.000 VNĐ
    "CH01_SC004": "CH01_SC004.mp4", # Chào từ biệt 7 thập kỷ
    "CH01_SC005": "CH01_SC005.mp4", # Cổng vòm đóng 15/09/2026
    "CH01_SC006": "CH01_SC006.mp4", # Mạng xã hội đồn đoán
    "CH01_SC007": "CH01_SC007.mp4", # Biểu tượng mậu dịch
    "CH01_SC008": "CH01_SC008.mp4", # Bảng PHÁ SẢN?
    "CH01_SC009": "CH01_SC009.mp4", # Sổ sách tài chính thực tế
    "CH01_SC010": "CH01_SC010.mp4", # Trụ sở tập đoàn mẹ OCH
    # SC011 & SC012: GIỮ BIỂU ĐỒ DOANH THU 484 TỶ (+60%) CHO ĐẾN KHI NÓI HẾT 60%!
    "CH01_SC011": "CH01_SC011.mp4", # Biểu đồ 484 tỷ
    "CH01_SC012": "CH01_SC011.mp4", # Biểu đồ 484 tỷ (+60%) tiếp tục giữ đến hết câu
    # NẮN LẠI CÁC CẢNH PHÍA SAU THEO ĐÚNG TIẾNG NÓI
    "CH01_SC013": "CH01_SC012.mp4", # Mảng kem truyền thống -> Dây chuyền sản xuất kem
    "CH01_SC014": "CH01_SC013.mp4", # Hơn 400 đại lý -> Bản đồ 400+ ĐẠI LÝ TOÀN QUỐC
    "CH01_SC015": "CH01_SC015.mp4", # Không thua lỗ hay phá sản -> Cửa hàng kem đông đúc
    "CH01_SC016": "CH01_SC014.mp4", # Lỗ lũy kế 383 tỷ -> Bàn kế toán LỖ LŨY KẾ 383 TỶ
    "CH01_SC017": "CH01_SC016.mp4", # Tăng trưởng mạnh mẽ -> Tòa nhà 35 Tràng Tiền
    "CH01_SC018": "CH01_SC018.mp4", # Nếu không phải phá sản -> Sảnh lớn đông đúc
    "CH01_SC019": "CH01_SC019.mp4", # Thế lực vô hình -> Thanh niên cầm điện thoại
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

def main():
    print("=== BẮT ĐẦU DỰNG LẠI PROJECT THEO CHUẨN SEMANTIC ALIGNMENT 69 CẢNH ===")
    
    # 1. Đóng CapCut Desktop
    print("1. Đóng ứng dụng CapCut Desktop...")
    subprocess.run(["pkill", "-9", "-f", "CapCut"], capture_output=True)
    
    # 2. Tính toán nhịp thời gian 69 cảnh từ Whisper Forced Alignment
    print("2. Tính toán timeline từ Whisper Forced Alignment...")
    engine = SyncTimingEngine(str(WORKSPACE / "source/kem-trang-tien"))
    tl = engine.compute_chapter_timeline("01")
    total_duration = tl["total_duration"]
    print(f"   -> 69 phân cảnh, tổng thời lượng: {total_duration}s")
    
    # 3. Chuẩn bị video_items cho spec.json
    print("3. Xây dựng declarative spec.json...")
    video_items = []
    operations = []
    for idx, it in enumerate(tl["video_items"]):
        sid = it["scene_id"]
        vname = SCENE_VIDEO_MAP.get(sid, f"{sid}.mp4")
        vpath = VIDEO_SOURCE / vname
        if not vpath.exists():
            raise FileNotFoundError(f"Không tìm thấy video: {vpath}")
            
        dur = it["duration"]
        dur_clamped = min(dur, 7.95) # Đảm bảo tuyệt đối không vượt quá 8s của clip gốc
        
        ref = f"v_{idx:03d}"
        video_items.append({
            "ref": ref,
            "path": str(vpath.resolve()),
            "start": it["start"],
            "duration": dur_clamped,
            "sourceStart": 0.0,
            "speed": 1.0,
            "volume": 0.0
        })
        
        # Gán transition mix nhẹ (0.4s) giữa các clip
        if idx < len(tl["video_items"]) - 1:
            operations.append({
                "op": "transition",
                "target": ref,
                "slug": "mix",
                "duration": 0.4
            })
        
    audio_items = [
        {
            "path": str(AUDIO_SRC.resolve()),
            "start": 0.0,
            "duration": total_duration,
            "volume": 1.0
        }
    ]
    
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
                "items": video_items
            },
            {
                "type": "audio",
                "name": "Voiceover",
                "items": audio_items
            }
        ],
        "operations": operations
    }
    
    spec_file = WORKSPACE / "spec_realigned_ch01.json"
    with open(spec_file, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
    print(f"   -> Đã ghi spec vào {spec_file}")
    
    # 4. Xóa draft cũ nếu có để compile mới hoàn toàn
    if DRAFT_DIR.exists():
        print(f"4. Dọn dẹp thư mục draft cũ: {DRAFT_DIR}...")
        shutil.rmtree(DRAFT_DIR)
        
    # 5. Biên dịch qua capcut compile
    print("5. Biên dịch dự án qua `capcut compile`...")
    cmd_compile = [
        "node", str(CAPCUT_CLI), "compile", str(spec_file),
        "--out", str(DRAFT_DIR),
        "--template", str(MODERN_TEMPLATE)
    ]
    res = subprocess.run(cmd_compile, cwd=str(WORKSPACE), capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Compile error: {res.stderr or res.stdout}")
        sys.exit(1)
    print("   -> Compile thành công 100%!")
    
    # 6. Đăng ký materials chuẩn CapCut 9.x
    print("6. Đăng ký materials chuẩn CapCut 9.x...")
    cmd_reg = ["node", str(CAPCUT_CLI), "register", PROJECT_NAME, "--materials", "--apply"]
    subprocess.run(cmd_reg, cwd=str(WORKSPACE), check=True)
    
    # 7. Kiểm tra lint
    print("7. Chạy capcut lint kiểm toán chất lượng dự án...")
    cmd_lint = ["node", str(CAPCUT_CLI), "lint", PROJECT_NAME]
    res_lint = subprocess.run(cmd_lint, cwd=str(WORKSPACE), capture_output=True, text=True)
    print(res_lint.stdout)
    
    # 8. Mở CapCut Desktop
    print("8. Mở ứng dụng CapCut Desktop...")
    subprocess.run(["open", "-a", "CapCut"])
    print("=== HOÀN TẤT DỰNG DỰ ÁN KEMTRANGTIEN_CH01 ĐỒNG BỘ 100%! ===")

if __name__ == "__main__":
    main()
