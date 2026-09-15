import os
import json
import subprocess
import time

NOTEBOOK_ID = "b0e0cc8f-84b4-4d4f-b3d1-1c7e86ea0aa9"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/vi-sao-viet-nam-xay-sieu-cang-bien/research_vault"

os.makedirs(OUTPUT_DIR, exist_ok=True)

QUESTIONS = [
    {
        "file": "16_lat_cat_vi_mo_con_nguoi_va_sinh_ke_thuc_dia.md",
        "title": "Lát Cắt Vi Mô Thực Địa: Đời Sống Con Người, Tài Xế QL51, Công Nhân Cảng & Ngư Dân Cần Giờ",
        "prompt": """Phân tích sâu sắc các lát cắt vi mô và câu chuyện con người thực tế đằng sau những con số vĩ mô của hệ thống cảng biển Việt Nam:
1. Hành trình và trải nghiệm thực tế của tài xế xe container trên Quốc lộ 51 và các cửa ngõ Cát Lái / Cái Mép: Tình trạng tắc nghẽn giao thông, thời gian chờ đợi tại cổng cảng, chi phí phát sinh (drayage fee, lưu bãi, nhiên liệu) và áp lực giao hàng đúng giờ cho các chuyến tàu mẹ.
2. Đời sống và ca kíp của công nhân vận hành cẩu bến (STS crane operators), kỹ sư logistics tại cụm cảng Cái Mép - Thị Vải: Áp lực duy trì năng suất bốc dỡ 30-40 moves/cẩu/giờ để giải phóng siêu tàu 24.000 TEU trong vòng 24-36 giờ.
3. Sinh kế của cộng đồng ngư dân và người giữ rừng ngập mặn tại Cần Giờ: Những tác động trực tiếp của siêu dự án 5 tỷ USD lên nghề đánh bắt ven bờ, nuôi trồng thủy sản và cơ chế chuyển đổi nghề nghiệp, đền bù sinh thái ('Blue Carbon') cho người dân địa phương.
4. Lịch sử hình thành Cái Mép: Câu chuyện về tầm nhìn của các nhà quy hoạch cảng biển Việt Nam (JICA, Portcoast) khi kiên định biến vùng đầm lầy sông Thị Vải thành cụm cảng nước sâu đón siêu tàu mẹ khi nhiều người còn hoài nghi. Trích dẫn chi tiết và nguồn."""
    }
]

def run():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    print(f"Bắt đầu trích xuất Round 2b: {len(QUESTIONS)} chuyên đề...")
    for idx, item in enumerate(QUESTIONS, 1):
        target_file = os.path.join(OUTPUT_DIR, item["file"])
        print(f"[{idx}/{len(QUESTIONS)}] Đang trích xuất: {item['title']} -> {item['file']}")
        
        cmd = [
            NOTEBOOKLM_BIN,
            "ask",
            item["prompt"],
            "-n", NOTEBOOK_ID,
            "--json"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, env=env, check=True)
            data = json.loads(result.stdout)
            answer = data.get("answer", "")
            
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(f"# {item['title']}\n\n")
                f.write(answer)
                f.write("\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC Deep Research Engine*\n")
            
            print(f"✅ Hoàn thành: {item['file']} ({len(answer)} ký tự)")
            time.sleep(2)
        except Exception as e:
            print(f"❌ Lỗi {item['file']}: {e}")

if __name__ == "__main__":
    run()
