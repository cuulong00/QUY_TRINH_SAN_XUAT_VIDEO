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
        "file": "13_dia_chinh_tri_bien_dong_va_chuoi_ngoc_trai.md",
        "title": "Địa Chính Trị Biển Đông, Tuyến Huyết Mạch Thương Mại & Đối Trọng Chiến Lược",
        "prompt": """Phân tích chuyên sâu về ý nghĩa địa chính trị và an ninh hàng hải của hệ thống siêu cảng biển Việt Nam trên Biển Đông:
1. Tầm quan trọng của tuyến hàng hải Biển Đông: Quy mô giá trị thương mại thông qua (khoảng 30% - hơn 5.300 tỷ USD thương mại toàn cầu mỗi năm, huyết mạch vận tải dầu mỏ từ Trung Đông sang Đông Á). Vị trí chiến lược của bờ biển Việt Nam dọc theo tuyến hàng hải huyết mạch này.
2. Chiến lược cảng biển 'Vành đai và Con đường' (BRI) / 'Chuỗi ngọc trai' của Trung Quốc: Sự hiện diện tại Căn cứ Hải quân Ream / Cảng Sihanoukville (Campuchia), Cảng Hambantota (Sri Lanka), Cảng Gwadar (Pakistan).
3. Vai trò của các vịnh nước sâu và cụm cảng chiến lược của Việt Nam (Cam Ranh, Vân Phong, Cái Mép, Lạch Huyện, Vũng Áng) trong việc bảo vệ chủ quyền biển đảo, an ninh năng lượng và cân bằng địa chính trị khu vực. Trích dẫn đầy đủ số liệu và nguồn."""
    },
    {
        "file": "14_kenh_dao_funan_techo_va_kra_landbridge.md",
        "title": "Tác Động Địa Kinh Tế Của Kênh Đào Funan Techo (Campuchia) & Đề Xuất Kra Landbridge (Thái Lan)",
        "prompt": """Phân tích chi tiết về tác động của các dự án đại công trình hàng hải khu vực lên hệ thống cảng biển Việt Nam:
1. Dự án Kênh đào Funan Techo của Campuchia: Quy mô, chiều dài (180 km), hướng tuyến từ sông Mekong ra vịnh Thái Lan. Động cơ tự chủ tuyến vận tải hàng hải của Campuchia để giảm phụ thuộc vào các cảng sông và cảng biển Việt Nam (Cái Mép, Cát Lái, Cần Thơ). Tác động thực tế đến lưu lượng hàng hóa quá cảnh và bài toán nguồn nước, sinh thái Đồng bằng sông Cửu Long.
2. Đề xuất Dự án Cầu cạn (Southern Landbridge) eo biển Kra của Thái Lan: Quy mô vốn đầu tư ~28-31 tỷ USD, tuyến đường bộ/đường sắt/ống dẫn dầu 90 km nối Vịnh Thái Lan và Biển Andaman nhằm 'né' eo biển Malacca. Phân tích tính khả thi kinh tế, chi phí bốc dỡ 2 đầu so với cước tàu đi qua Malacca và tác động tiềm tàng đến các cảng biển Việt Nam và Singapore. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "15_case_study_quoc_te_dubai_busan_hambantota.md",
        "title": "Bài Học Quốc Tế: Dubai Jebel Ali, Busan Hàn Quốc, Bẫy Nợ Hambantota & Rotterdam Net-Zero",
        "prompt": """Phân tích và đối chiếu 4 bài học lịch sử phát triển cảng biển quốc tế có giá trị tham chiếu sâu sắc cho Việt Nam:
1. Dubai (Jebel Ali & DP World): Từ một vùng đất cằn cỗi trở thành siêu cảng trung chuyển Top 10 thế giới nhờ mô hình kết hợp Cảng nước sâu + Khu thương mại tự do JAFZA (Jebel Ali Free Zone) + chính sách miễn thuế và logistics tích hợp.
2. Busan (Hàn Quốc): Quá trình chuyển đổi từ cảng cửa ngõ xuất khẩu công nghiệp thuần túy sang Siêu trung tâm trung chuyển quốc tế (Transshipment Hub) Đông Bắc Á, phục vụ hàng hóa trung chuyển từ Trung Quốc và Nhật Bản.
3. Cảnh báo từ Cảng Hambantota (Sri Lanka): Bài học về 'Bẫy nợ' (Debt-trap) và việc mất quyền kiểm soát cảng biển chiến lược khi vay nợ ồ ạt đầu tư vượt quá nhu cầu thực tế, dẫn đến việc phải cho thuê cảng 99 năm.
4. Port of Rotterdam (Hà Lan): Mô hình Cảng thông minh kỹ thuật số (Digital Twin), tự động hóa và lộ trình chuyển đổi Cảng Xanh / Net-Zero, năng lượng Hydro xanh — mô hình kiểu mẫu cho tương lai Cần Giờ và Cái Mép. Trích dẫn số liệu cụ thể và bài học đúc rút."""
    }
]

def run():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    print(f"Bắt đầu trích xuất Round 2a: {len(QUESTIONS)} chuyên đề...")
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
