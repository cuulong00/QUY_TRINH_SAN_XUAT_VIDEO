import os
import sys
import json
import subprocess
import time

NOTEBOOK_ID = "88e50fa8-b2db-43b5-990b-82543c6fd2d0"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/triet-ly-thuc-chien-vin-viettel/research_vault"

os.makedirs(OUTPUT_DIR, exist_ok=True)

EXTRACTION_QUESTIONS = [
    {
        "file": "01_hien_tuong_nen_thoi_gian_va_toc_do_truong_thanh.md",
        "title": "Hiện Tượng Nén Thời Gian & Tốc Độ Trưởng Thành Phi Mã",
        "prompt": """Phân tích chuyên sâu về hiện tượng 'Nén thời gian' (Time-compression phenomenon) trong sự phát triển của Viettel và Vingroup:
1. Cơ chế và các cột mốc chứng minh tốc độ trưởng thành thần tốc: Viettel mất đúng 4 năm (2004-2008) từ 4,3% lên vị trí Top 1 mạng di động Việt Nam; 15 năm (2009-2024) chuyển dịch thành tập đoàn công nghệ làm chủ 5G Open RAN. Vingroup mất 21 tháng xây nhà máy ô tô Cát Hải; mất 5 năm (2019-2024) đưa VinFast lên Top 1 toàn thị trường ô tô Việt Nam (>87.000 xe); chỉ mất chưa đầy 3 năm (2022-2024) đưa xe thuần điện đánh bại toàn bộ các hãng xe xăng truyền thống.
2. So sánh cơ chế nén thời gian này với chu kỳ phát triển 30-50 năm của các tập đoàn phương Tây và Chaebol Hàn Quốc. Trích dẫn đầy đủ mốc thời gian, số liệu và nguồn."""
    },
    {
        "file": "02_cau_truc_banh_da_he_sinh_thai_da_nganh.md",
        "title": "Cấu Trúc Bánh Đà Hệ Sinh Thái Đa Ngành & Trợ Lực Chéo",
        "prompt": """Phân tích mô hình Tập đoàn Đa ngành Hệ sinh thái (Conglomerate Ecosystem Flywheel) của Viettel và Vingroup:
1. Cơ chế trợ lực chéo dòng vốn (Cross-Financing): Cách các mảng 'bò sữa' tạo tiền mặt mạnh (Viễn thông truyền thống của Viettel; Bất động sản Vinhomes của Vingroup) đóng vai trò bệ phóng tài chính nuôi dưỡng các ngành công nghệ - công nghiệp rủi ro cao (5G VHT, Chip; Ô tô điện VinFast, Pin, AI).
2. Cơ chế tự tạo thị trường đầu ra nội bộ và khép kín vòng đời khách hàng: Viettel Post, Viettel Money (Viettel) và V-GREEN, Taxi Xanh SM, Vinmec, Vinschool (Vingroup). Trích dẫn số liệu dòng tiền và nguồn tài liệu."""
    },
    {
        "file": "03_triet_ly_ha_tang_hang_nang_di_truoc.md",
        "title": "Triết Lý Hạ Tầng Hạng Nặng Đi Trước",
        "prompt": """Phân tích chiến lược 'Hạ tầng vật lý hạng nặng đi trước' của Viettel và Vingroup:
1. Tại sao cả hai đều từ chối con đường thương mại trung gian ngắn hạn mà chấp nhận chôn vốn khổng lồ vào hạ tầng vật lý trước: Viettel cắm hàng chục nghìn trạm BTS và kéo cáp quang về nông thôn; Vingroup xây dựng mạng lưới hơn 150.000 cổng sạc V-GREEN toàn quốc.
2. Vai trò của hạ tầng như một 'con hào kinh tế' (economic moat) tuyệt đối ngăn chặn đối thủ ngoại cạnh tranh. Trích dẫn dẫn chứng thực tế và nguồn."""
    },
    {
        "file": "04_co_may_ky_luat_thuc_thi_triet_de.md",
        "title": "Cỗ Máy Kỷ Luật Thực Thi Triệt Để",
        "prompt": """Phân tích văn hóa kỷ luật và cơ chế vận hành không thỏa hiệp của Viettel và Vingroup:
1. Cách triệt tiêu sự trì hoãn và chủ nghĩa bàn giấy: Kỷ luật báo cáo tối đa 1 trang A4, họp 15-30 phút của Vingroup; Kỷ luật quân đội, không bàn lùi, nhận nhiệm vụ là làm đến cùng của Viettel.
2. Tốc độ đo bằng ngày và cơ chế phản ứng thần tốc với thị trường. Trích dẫn các ví dụ nội bộ và nguồn tài liệu."""
    },
    {
        "file": "05_nghe_thuat_quan_tri_chi_phi_co_hoi_va_cat_bo.md",
        "title": "Nghệ Thuật Quản Trị Chi Phí Cơ Hội & Dũng Cảm Cắt Bỏ",
        "prompt": """Phân tích cách Viettel và Vingroup bẻ gãy 'Bẫy chi phí chìm' (Sunk Cost Fallacy):
1. Vingroup: Các quyết sách cắt bỏ mang tính lịch sử để dồn lực cho mũi nhọn: Bán VinMart, đóng Vsmart (khi đang giữ 12.7% thị phần), dừng xe xăng, và tái cấu trúc Asset-light (2026) chuyển giao 182.000 tỷ đồng nợ sản xuất.
2. Viettel: Phương châm 'Dò đá qua sông' và triết lý 'Sẵn sàng trả học phí cho thất bại dấn thân' — dũng cảm dừng ngay các thử nghiệm sai ở cấp xã/huyện. Trích dẫn số liệu tài chính và nguồn."""
    },
    {
        "file": "06_so_sanh_voi_mo_hinh_chaebol_va_toan_cau.md",
        "title": "So Sánh Với Mô Hình Chaebol Hàn Quốc & Toàn Cầu",
        "prompt": """So sánh mô hình siêu tập đoàn đa ngành Việt Nam (Viettel, Vingroup) với các mô hình quốc tế:
1. So sánh với Chaebol Hàn Quốc (Samsung, Hyundai) và Keiretsu Nhật Bản: Điểm tương đồng về vai trò 'ngọn cờ đầu quốc gia' (National Champions), khả năng huy động nguồn lực và tinh thần tự lực công nghệ.
2. Điểm khác biệt về môi trường thể chế, mức độ mở cửa thị trường và thời đại chuyển đổi số/chuyển đổi xanh. Trích dẫn nghiên cứu so sánh thể chế và nguồn."""
    },
    {
        "file": "07_su_hop_luc_he_sinh_thai_viettel_vingroup.md",
        "title": "Sự Hợp Lực Giữa Hai Hệ Sinh Thái Viettel & Vingroup",
        "prompt": """Phân tích các thỏa thuận và tiềm năng hợp tác chiến lược giữa Viettel và Vingroup (2024-2026):
1. Sự kết hợp giữa hạ tầng số (Viettel Cloud, siêu máy tính AI GPU NVIDIA, 5G, an ninh mạng) với hạ tầng công nghiệp - phương tiện xanh (VinFast, trạm sạc V-GREEN, Xanh SM).
2. Tác động của sự hợp lực này đối với công cuộc chuyển đổi số và chuyển đổi xanh quốc gia. Trích dẫn các thông cáo hợp tác chính thức và nguồn."""
    },
    {
        "file": "08_so_lieu_tai_chinh_dinh_luong_toan_dien.md",
        "title": "Bảng Số Liệu Định Lượng Toàn Diện 2004-2026",
        "prompt": """Tổng hợp bảng số liệu định lượng chi tiết về tài chính, đóng góp và thị phần của Viettel và Vingroup:
1. Doanh thu, lợi nhuận, tổng tài sản qua các giai đoạn phát triển chính.
2. Số tiền nộp ngân sách nhà nước hàng năm.
3. Thị phần di động/hạ tầng số (Viettel) và thị phần ô tô/BĐS (Vingroup). Trích dẫn báo cáo tài chính kiểm toán và số liệu chính thống."""
    },
    {
        "file": "09_cac_goc_nhin_phan_bien_va_rui_ro_mo_hinh.md",
        "title": "Phản Biện Khách Quan & Rủi Ro Hệ Thống",
        "prompt": """Phân tích các góc nhìn phản biện khách quan về rủi ro của mô hình tập đoàn đa ngành siêu tốc độ:
1. Rủi ro thâm dụng vốn, chi phí tài chính và gánh nặng nợ khi đầu tư dàn trải quy mô lớn (case VinFast).
2. Rủi ro địa chính trị và biến động tỷ giá khi mở rộng toàn cầu (case Viettel Global).
3. Áp lực văn hóa kỷ luật thép lên đời sống nhân viên và nguy cơ kiệt sức (Burnout). Trích dẫn các phân tích độc lập."""
    },
    {
        "file": "10_bai_hoc_nen_thoi_gian_cho_ca_nhan.md",
        "title": "Framework Nén Thời Gian & Bánh Đà Cho Cá Nhân",
        "prompt": """Từ hiện tượng nén thời gian và bánh đà hệ sinh thái của 2 tập đoàn, hãy đúc rút các framework tư duy ứng dụng cụ thể cho cá nhân:
1. Tư duy 'Nén thời gian cá nhân': Cách tăng tốc độ thử-sai để rút ngắn chu kỳ học tập và đạt thành tựu trong sự nghiệp.
2. Mô hình 'Bánh đà kỹ năng đa nhiệm': Lấy kỹ năng tạo tiền ngắn hạn nuôi kỹ năng khó mang tính đột phá lâu dài.
3. Xây dựng 'Hạ tầng cá nhân' vững chắc và triệt tiêu bệnh trì hoãn bằng quy tắc cô đọng thông tin 1 trang giấy."""
    },
    {
        "file": "11_bai_hoc_quan_tri_ha_tang_va_dong_tien_sme.md",
        "title": "Bài Học Quản Trị Hạ Tầng & Dòng Tiền Cho Doanh Nghiệp SME",
        "prompt": """Đúc rút các bài học kinh doanh thực chiến cho doanh nghiệp nhỏ (SME), startup từ mô hình của Viettel và Vingroup:
1. Cách xây dựng con hào kinh tế dựa trên hạ tầng/năng lực cốt lõi thay vì chiêu trò marketing ngắn hạn.
2. Quản trị dòng tiền trợ lực chéo giữa các mảng kinh doanh và dũng cảm cắt bỏ các chi phí chìm không hiệu quả."""
    },
    {
        "file": "12_triet_ly_tro_choi_vo_cuc_va_di_san.md",
        "title": "Triết Lý Trò Chơi Vô Cực & Tầm Nhìn Di Sản Quốc Gia",
        "prompt": """Phân tích triết lý 'Trò chơi vô cực' (The Infinite Game) và khát vọng tự lực tự cường dân tộc của Viettel và Vingroup:
1. Vượt qua mục tiêu lợi nhuận tài chính ngắn hạn để phụng sự xã hội và nâng tầm thương hiệu quốc gia ('Make in Vietnam', 'Làm đẹp cho đời', 'Bảo vệ chủ quyền số').
2. Bài học về việc xây dựng động lực dài hạn và sức bền vượt qua khủng hoảng cho cá nhân và tổ chức."""
    }
]

def run_extraction():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    print(f"Bắt đầu trích xuất mở rộng {len(EXTRACTION_QUESTIONS)} chuyên đề từ Notebook: {NOTEBOOK_ID}")
    
    for idx, item in enumerate(EXTRACTION_QUESTIONS, 1):
        target_file = os.path.join(OUTPUT_DIR, item["file"])
        print(f"\n[{idx}/{len(EXTRACTION_QUESTIONS)}] Đang trích xuất: {item['title']} -> {item['file']}")
        
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
                f.write("\n\n---\n*Trích xuất tự động qua NotebookLM Direct RPC Deep Research Engine*\n")
            
            print(f"✅ Hoàn thành: {item['file']} ({len(answer)} ký tự)")
            time.sleep(2)
        except Exception as e:
            print(f"❌ Lỗi trích xuất {item['file']}: {e}")
            if hasattr(e, 'stderr') and e.stderr:
                print(f"Stderr: {e.stderr}")

if __name__ == "__main__":
    run_extraction()
