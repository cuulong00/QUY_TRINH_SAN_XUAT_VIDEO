#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tải 15 video phát biểu nguyên thủ quốc gia năm 2026 từ kênh BNC Now (@BNCNow).
Lưu trữ thô tại: 01_management/research_raw/bnc_leaders_speeches_2026/
"""

import os
import sys
import json
import subprocess

TARGET_DIR = "/Users/pro16/Documents/VideoProject/X-Economic/01_management/research_raw/bnc_leaders_speeches_2026"
os.makedirs(TARGET_DIR, exist_ok=True)

# Danh sách 15 video chọn lọc theo tiêu chí tranh biện sắc bén / đối đầu / phê phán trực diện
VIDEOS = [
    {
        "id": "XFeA3ynfh9U",
        "leader": "Benjamin Netanyahu (Thủ tướng Israel)",
        "slug": "netanyahu_israel",
        "argument": "Bác bỏ kịch liệt các cáo buộc diệt chủng, chỉ trích LHQ là 'nhà hát của sự phi lý' và đạo đức giả, thề tiếp tục cuộc chiến đến khi xóa sổ hoàn toàn Hamas và đập tan mạng lưới của Iran."
    },
    {
        "id": "l_FAdPAcobA",
        "leader": "Volodymyr Zelensky (Tổng thống Ukraine)",
        "slug": "zelensky_ukraine",
        "argument": "Chỉ trích gay gắt Vladimir Putin và vạch trần sự bất lực của Hội đồng Bảo an LHQ; cảnh báo chiến tranh sẽ lan rộng vượt khỏi châu Âu nếu thế giới tiếp tục nhượng bộ kẻ xâm lược."
    },
    {
        "id": "rTTsv_jmiHM",
        "leader": "Recep Tayyip Erdogan (Tổng thống Thổ Nhĩ Kỳ)",
        "slug": "erdogan_turkey",
        "argument": "Chỉ trích dữ dội hệ thống LHQ đã bị tê liệt và tha hóa đạo đức trước thảm kịch nhân đạo tại Gaza; kêu gọi các quốc gia liên minh ngăn chặn Israel như thế giới từng ngăn chặn Hitler."
    },
    {
        "id": "0lCKVquIBe0",
        "leader": "Masoud Pezeshkian (Tổng thống Iran)",
        "slug": "pezeshkian_iran",
        "argument": "Đáp trả gay gắt đe dọa quân sự từ phía Mỹ và phương Tây; lên án chính sách cấm vận đơn phương là 'khủng bố kinh tế' và khẳng định Tehran sẽ không bao giờ đầu hàng trước áp lực trừng phạt."
    },
    {
        "id": "R2TBpusKGIY",
        "leader": "Luiz Inácio Lula da Silva (Tổng thống Brazil)",
        "slug": "lula_brazil",
        "argument": "Lên án trực diện sự thất bại thảm hại của các thể chế đa phương; chỉ trích việc chi hàng trăm tỷ USD cho chiến tranh vũ trang trong khi hàng trăm triệu người nghèo đói bị phớt lờ."
    },
    {
        "id": "7I6w9BVllN0",
        "leader": "Donald Trump (Tổng thống Mỹ)",
        "slug": "trump_usa",
        "argument": "Tuyên bố cứng rắn về việc thiết lập trật tự sức mạnh mới; đe dọa xóa sổ năng lực hạt nhân của Iran, phê phán các định chế toàn cầu ăn bám vào ngân sách Mỹ và cảnh báo nguy cơ AI siêu trí tuệ."
    },
    {
        "id": "XAsZCozhuVA",
        "leader": "Emmanuel Macron (Tổng thống Pháp)",
        "slug": "macron_france",
        "argument": "Chỉ trích việc 'công nghiệp hóa tội ác chiến tranh' là sự sỉ nhục đối với công lý quốc tế; cảnh báo trật tự dựa trên luật lệ đang tan rã và đòi tước quyền phủ quyết của các nước thường trực HĐBA trong các vụ thảm sát."
    },
    {
        "id": "P8zRp-qte-w",
        "leader": "Mahmoud Abbas (Tổng thống Palestine)",
        "slug": "abbas_palestine",
        "argument": "Phát biểu đanh thép gióng lên hồi chuông báo động trước việc nhà nước Palestine đang bị xóa sổ trên thực địa; chất vấn trách nhiệm đạo đức của LHQ khi để người dân Palestine bị lưu đày và tước đoạt quyền tự quyết."
    },
    {
        "id": "_kBy_ODjJFA",
        "leader": "Abdullah II (Quốc vương Jordan)",
        "slug": "abdullah_jordan",
        "argument": "Cảnh báo toàn cầu đang làm ngơ trước sự sụp đổ hoàn toàn của luật pháp quốc tế; vạch trần tiêu chuẩn kép trắng trợn của các cường quốc phương Tây khiến uy tín của LHQ bị kéo lùi nhiều thập kỷ."
    },
    {
        "id": "rEKZRMLRnfM",
        "leader": "Shigeru Ishiba (Thủ tướng Nhật Bản)",
        "slug": "ishiba_japan",
        "argument": "Lên án quyết liệt liên minh quân sự Nga - Triều Tiên đe dọa trực tiếp an ninh Đông Bắc Á; phản đối việc sử dụng răn đe hạt nhân để uy hiếp các nước láng giềng và đòi trừng phạt nghiêm khắc hơn."
    },
    {
        "id": "BaHm5S1eoTE",
        "leader": "Lãnh đạo phe đối lập / Quyền TT Venezuela",
        "slug": "venezuela_opposition",
        "argument": "Bất ngờ tuyên bố lộ trình chuyển đổi dân chủ, công khai thách thức và tố cáo chế độ Maduro tại diễn đàn LHQ; kêu gọi cộng đồng quốc tế công nhận chính phủ hợp hiến mới."
    },
    {
        "id": "XXE8Xo3p6hY",
        "leader": "Sok Chenda Sophea (Ngoại trưởng Campuchia)",
        "slug": "cambodia_fm",
        "argument": "Phản pháo gay gắt Thái Lan về tranh chấp biên giới và chủ quyền lãnh thổ; tuyên ngôn đanh thép 'Campuchia không bao giờ lùi bước' trước bất kỳ sức ép ngoại giao hay quân sự nào từ nước láng giềng."
    },
    {
        "id": "epMVaFNWACA",
        "leader": "Donald Trump & Tập Cận Bình (Hội đàm Thượng đỉnh Mỹ - Trung)",
        "slug": "trump_xi_summit",
        "argument": "Màn đấu trí trực diện xác lập lằn ranh đỏ giữa hai siêu cường về Đài Loan, chuỗi cung ứng bán dẫn và hàng rào thuế quan; cả hai bên đều phát đi thông điệp sẵn sàng đối đầu kinh tế toàn diện nếu ranh giới bị vượt qua."
    },
    {
        "id": "M8Rw67NmZxU",
        "leader": "Justin Trudeau & Jonas Gahr Støre (Thủ tướng Canada & Na Uy)",
        "slug": "canada_norway_pm",
        "argument": "Ký kết thỏa thuận chiến lược đồng thời công khai chất vấn các hành động thương mại và địa chính trị mang tính thù địch đơn phương của Mỹ; tuyên bố Bắc Cực và châu Âu không thể là sân sau của chủ nghĩa biệt lập."
    },
    {
        "id": "78fpv1ir5S8",
        "leader": "Yanis Varoufakis (Cựu Bộ trưởng Tài chính Hy Lạp)",
        "slug": "varoufakis_greece",
        "argument": "Đưa ra bản cáo trạng dữ dội tuyên bố Liên minh châu Âu 'đã tàn đời' và trật tự đa phương phương Tây đã sụp đổ hoàn toàn về mặt đạo đức do tự biến mình thành chư hầu địa chính trị và suy thoái kinh tế công nghiệp sâu sắc."
    }
]

def main():
    print(f"Bắt đầu tải {len(VIDEOS)} video về: {TARGET_DIR}")
    download_results = []
    
    for idx, item in enumerate(VIDEOS, 1):
        vid = item["id"]
        slug = item["slug"]
        url = f"https://www.youtube.com/watch?v={vid}"
        out_template = os.path.join(TARGET_DIR, f"{idx:02d}_{vid}_{slug}.%(ext)s")
        expected_file = os.path.join(TARGET_DIR, f"{idx:02d}_{vid}_{slug}.mp4")
        
        print(f"\n[{idx}/15] Đang xử lý: {item['leader']} ({vid})...")
        
        # Lấy metadata trước
        meta_cmd = ["yt-dlp", "--dump-json", url]
        res = subprocess.run(meta_cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Lỗi lấy metadata cho {vid}: {res.stderr[:200]}")
            continue
            
        meta = json.loads(res.stdout)
        title = meta.get("title", "")
        upload_date = meta.get("upload_date", "")
        duration = meta.get("duration_string", "")
        
        # Định dạng ngày dd/mm/yyyy
        if upload_date and len(upload_date) == 8:
            formatted_date = f"{upload_date[6:8]}/{upload_date[4:6]}/{upload_date[0:4]}"
        else:
            formatted_date = upload_date
            
        # Kiểm tra nếu file đã tải xong
        if os.path.exists(expected_file) and os.path.getsize(expected_file) > 1000000:
            file_size_mb = os.path.getsize(expected_file) / (1024 * 1024)
            print(f"-> File đã tồn tại: {expected_file} ({file_size_mb:.1f} MB)")
            download_results.append({
                "idx": idx,
                "id": vid,
                "leader": item["leader"],
                "title": title,
                "date": formatted_date,
                "url": url,
                "duration": duration,
                "file_path": expected_file,
                "size_mb": f"{file_size_mb:.1f} MB",
                "argument": item["argument"],
                "status": "Đã tải thành công"
            })
            continue
            
        # Tải video chất lượng 720p tối ưu (đủ nét cho tư liệu, tải nhanh, không nặng ổ)
        dl_cmd = [
            "yt-dlp",
            "-f", "bestvideo[height<=720]+bestaudio/best[height<=720]/best",
            "--merge-output-format", "mp4",
            "-o", out_template,
            url
        ]
        
        print(f"-> Đang tải video...")
        dl_res = subprocess.run(dl_cmd, capture_output=True, text=True)
        
        # Tìm file thực tế được tạo ra
        actual_file = expected_file
        if not os.path.exists(actual_file):
            # Tìm file có tiền tố tương ứng
            import glob
            matches = glob.glob(os.path.join(TARGET_DIR, f"{idx:02d}_{vid}_{slug}.*"))
            if matches:
                actual_file = matches[0]
                
        if os.path.exists(actual_file):
            size_mb = os.path.getsize(actual_file) / (1024 * 1024)
            print(f"-> Tải thành công: {actual_file} ({size_mb:.1f} MB)")
            download_results.append({
                "idx": idx,
                "id": vid,
                "leader": item["leader"],
                "title": title,
                "date": formatted_date,
                "url": url,
                "duration": duration,
                "file_path": actual_file,
                "size_mb": f"{size_mb:.1f} MB",
                "argument": item["argument"],
                "status": "Đã tải thành công"
            })
        else:
            print(f"-> TẢI THẤT BẠI {vid}: {dl_res.stderr[:200]}")
            download_results.append({
                "idx": idx,
                "id": vid,
                "leader": item["leader"],
                "title": title,
                "date": formatted_date,
                "url": url,
                "duration": duration,
                "file_path": "N/A",
                "size_mb": "0 MB",
                "argument": item["argument"],
                "status": f"Lỗi tải: {dl_res.stderr[:100]}"
            })
            
    # Lưu kết quả tổng hợp ra JSON trung gian
    summary_path = os.path.join(TARGET_DIR, "download_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(download_results, f, ensure_ascii=False, indent=2)
    print(f"\nĐã hoàn thành tải toàn bộ video! Kết quả lưu tại: {summary_path}")

if __name__ == "__main__":
    main()
