import subprocess
import os
import json

NOTEBOOK_ID = "592b802f-1f62-4720-bb03-c296066dce97"
HOME_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
CLI_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
VAULT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/sieu-du-an-ky-luc-the-gioi-viet-nam/research_vault"

tasks = [
    {
        "filename": "09_so_sanh_chi_phi_thap_50_vs_100_tang.md",
        "title": "So sánh chi phí kỹ thuật: 2 tòa 50 tầng vs 1 tòa 100 tầng",
        "prompt": "Dựa trên các nghiên cứu của CTBUH (Council on Tall Buildings and Urban Habitat), GS. Jason Barr và dữ liệu xây dựng quốc tế: So sánh chi tiết suất vốn đầu tư xây dựng ($/m2 sàn) giữa tòa nhà 50 tầng và tòa nhà 100 tầng (Supertall). Giải thích tại sao chi phí không tăng tuyến tính mà tăng theo hàm số mũ / hàm lồi (Convex Cost Function). Phân tích các yếu tố kỹ thuật then chốt: Lực gió và mô-men lật (M proportional to H^3), quả cầu dập dao động TMD, hình phạt diện tích lõi (Core Penalty - tỷ lệ diện tích sàn bán được), và chi phí lãi vay trong thời gian xây dựng (IDC) giữa 3 năm vs 6-7 năm. Trích dẫn đầy đủ số liệu định lượng, tên nghiên cứu và các mốc tham chiếu thực tế."
    },
    {
        "filename": "10_so_sanh_chi_phi_va_loi_ich_svd_40k_vs_135k.md",
        "title": "So sánh kỹ thuật và kinh tế: Sân vận động 40.000 chỗ vs 135.000 chỗ",
        "prompt": "Dựa trên tài liệu FIFA Stadium Guidelines (6th Edition), dữ liệu Pollstar, Billboard Boxscore và các hợp đồng Naming Rights thực tế (SoFi Stadium, Mercedes-Benz Stadium): 1. So sánh kỹ thuật và chi phí xây dựng: Khẩu độ nhô ra của mái che (Cantilever Span), hệ thống mái che trượt tự động (Retractable Roof), độ dốc khán đài (Raking) và tải trọng dao động cộng hưởng (Harmonic Resonance) giữa sân 40.000 chỗ và sân 135.000 chỗ. 2. Chi phí vận hành và bảo trì (O&M): Tỷ lệ % O&M hàng năm trên tổng vốn đầu tư của sân vận động hiện đại, nguy cơ Voi trắng nếu tần suất sự kiện thấp. 3. Lợi ích kinh tế đột phá mà chỉ sân 135.000 chỗ đạt được (sân 40.000 chỗ bị loại): Quy định của FIFA về sức chứa tối thiểu cho trận Chung kết World Cup (80.000 chỗ); Bài toán hòa vốn sản xuất cố định (Fixed Production Costs $4M-$6M) của các siêu concert (Taylor Swift Eras Tour, Coldplay) tại sân 40k chỗ (lỗ/hòa vốn) vs sân 135k chỗ (lãi ròng $10M+/đêm); Giá trị thương quyền Naming Rights thực tế (dẫn chứng SoFi $625M/20 năm); Hiệu ứng kinh tế lan tỏa (The Multiplier Effect) dẫn chứng từ Singapore GDP và du lịch. Nêu rõ các số liệu định lượng và trích dẫn nguồn."
    }
]

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = HOME_DIR

for t in tasks:
    filepath = os.path.join(VAULT_DIR, t["filename"])
    print(f"[*] Extracting {t['filename']}...")
    cmd = [CLI_PATH, "ask", t["prompt"], "-n", NOTEBOOK_ID, "--save-as-note", "-t", t["title"], "--json"]
    res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=180)
    if res.returncode == 0:
        data = json.loads(res.stdout)
        content = data.get("answer", "")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {t['title']}\n\n{content}\n")
        print(f"[✓] Saved {t['filename']} ({len(content)} chars)")
    else:
        print(f"[✗] Error: {res.stderr}")

print("[✓] Done extracting grounded comparisons!")
