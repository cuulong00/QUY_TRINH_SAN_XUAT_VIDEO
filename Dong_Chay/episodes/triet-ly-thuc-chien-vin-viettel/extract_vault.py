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
        "file": "01_triet_ly_thuc_tien_vs_kiem_loi.md",
        "title": "Triết lý Thực tiễn vs Kiệm lời",
        "prompt": """Phân tích chuyên sâu về triết lý nhận thức và hành động của Viettel và Vingroup:
1. Nguồn gốc, hoàn cảnh và ý nghĩa thực tế của câu nói của Chủ tịch Phạm Nhật Vượng: "Tôi là người kiệm lời, chỉ thích làm". Cơ chế tại sao Vingroup chọn cách im lặng trước truyền thông và để kết quả/sản phẩm tự lên tiếng.
2. Nguồn gốc và vai trò của giá trị cốt lõi số 1 tại Viettel: "Thực tiễn là tiêu chuẩn kiểm nghiệm chân lý" và câu nói của ông Nguyễn Mạnh Hùng "Làm trước, học sau. Làm sẽ sinh ra nghĩ".
3. So sánh điểm tương đồng và khác biệt giữa 2 triết lý này. Trích dẫn đầy đủ nguồn tài liệu, các ví dụ thực tế và số liệu minh chứng."""
    },
    {
        "file": "02_nghe_thuat_xam_chiem_nong_thon_vs_tong_luc.md",
        "title": "Nghệ thuật Thâm nhập Thị trường",
        "prompt": """Phân tích chiến lược thâm nhập và chiếm lĩnh thị trường của Viettel và Vingroup:
1. Chiến lược của Viettel: Phương châm "Dò đá qua sông" và chiến thuật "Lấy nông thôn vây thành thị". Viettel đã triển khai hạ tầng trạm BTS ở vùng sâu vùng xa, biên giới hải đảo như thế nào để đánh bại các đối thủ lớn? Case study mở rộng sang Campuchia (Metfone), Lào, châu Phi, Peru (Bitel).
2. Chiến lược của Vingroup: Chiến lược "Quy hoạch hệ sinh thái tổng lực All-in-one" và đòn đánh thần tốc. Từ Vinpearl Nha Trang, Vinhomes Central Park/Landmark 81, Ocean Park đến xây dựng nhà máy VinFast Hải Phòng chỉ trong 21 tháng.
3. So sánh 2 trường phái phân bổ nguồn lực: Đánh ngách bền bỉ tích lũy vs Đánh tổng lực quy mô lớn. Trích dẫn đầy đủ mốc thời gian, số liệu và nguồn."""
    },
    {
        "file": "03_ban_linh_nghien_viec_kho_va_tu_chu.md",
        "title": "Bản lĩnh Nghiện việc khó và Tự chủ",
        "prompt": """Phân tích bản lĩnh dấn thân vào các bài toán khó nhất của Viettel và Vingroup:
1. Viettel: Giá trị "Trưởng thành qua những thách thức và thất bại". Quá trình Viettel High Tech (VHT) nghiên cứu và làm chủ toàn trình công nghệ thiết bị 5G Make-in-Vietnam (lọt Magic Quadrant Gartner), radar và khí tài quân sự.
2. Vingroup: Tinh thần "Mãi mãi tinh thần khởi nghiệp". Canh bạc xe điện toàn cầu VinFast: tại sao dám dấn thân vào ngành công nghiệp khó nhất thế giới, tự xây dựng hạ tầng trạm sạc V-GREEN và mạng lưới Xanh SM?
3. Tại sao cả hai đều chọn "bài toán khó" thay vì những mảng kinh doanh an toàn, dễ kiếm tiền? Trích dẫn số liệu R&D, đối tác quốc tế và nguồn."""
    },
    {
        "file": "04_nghe_thuat_cat_bo_va_tai_cau_truc.md",
        "title": "Nghệ thuật Cắt bỏ và Tái cấu trúc",
        "prompt": """Phân tích các quyết định tái cấu trúc sinh tử và nghệ thuật cắt bỏ để dồn lực của Viettel và Vingroup:
1. Vingroup: Triết lý "Cắt bỏ để tập trung mũi nhọn" của Phạm Nhật Vượng. Chi tiết các thương vụ: Chuyển giao VinMart/VinMart+/VinEco cho Masan (2019), Dừng sản xuất điện thoại/TV Vsmart (2021), Dừng sản xuất xe xăng để thuần xe điện VinFast (2022), và tái cấu trúc asset-light (2026).
2. Viettel: Các bài học từ thị trường quốc tế khó khăn, các dự án công nghệ từng gặp trục trặc và cách Viettel thích ứng, chuyển mình linh hoạt.
3. Phân tích bài học vượt qua bẫy chi phí chìm (Sunk Cost Fallacy) từ 2 tập đoàn. Trích dẫn số liệu tài chính và nguồn trích dẫn."""
    },
    {
        "file": "05_co_may_ky_luat_nguoi_linh_vs_startup.md",
        "title": "Cỗ máy Kỷ luật Bộ máy",
        "prompt": """Phân tích văn hóa kỷ luật và cơ chế vận hành nội bộ của Viettel và Vingroup:
1. Kỷ luật Người lính của Viettel: Giá trị "Truyền thống và cách làm người lính". Tinh thần không bàn lùi, mệnh lệnh dứt khoát, văn hóa chấp nhận hy sinh và xung phong vào việc khó.
2. Kỷ luật Khởi nghiệp của Vingroup: Văn hóa hiệu suất cao, nguyên tắc báo cáo tối đa 1 trang A4, tốc độ ra quyết định tính bằng ngày, chế độ đãi ngộ cao đi kèm đào thải và luân chuyển khắc nghiệt.
3. So sánh 2 mô hình quản trị con người: Đâu là động lực giữ lửa cho hàng chục ngàn nhân sự? Trích dẫn dẫn chứng thực tế và nguồn tài liệu."""
    },
    {
        "file": "06_so_lieu_tai_chinh_va_quy_mo_dong_gop.md",
        "title": "Số liệu Tài chính và Quy mô Đóng góp",
        "prompt": """Tổng hợp bảng số liệu định lượng chi tiết về quy mô tài chính, đóng góp kinh tế của Vingroup và Viettel (giai đoạn từ 2018 đến 2024-2026):
1. Doanh thu hợp nhất, lợi nhuận trước/sau thuế hàng năm.
2. Tổng tài sản, quy mô vốn chủ sở hữu và cơ cấu nợ.
3. Số tiền nộp ngân sách nhà nước qua từng năm.
4. Thị phần trong các mảng cốt lõi: Viễn thông di động, hạ tầng số (Viettel); Bất động sản dân cư, xe điện, du lịch (Vingroup).
5. Trích dẫn nguồn số liệu cụ thể (Báo cáo tài chính kiểm toán, Tổng cục Thống kê, Báo cáo thường niên)."""
    },
    {
        "file": "07_su_menh_ngon_co_dau_national_champions.md",
        "title": "Sứ mệnh Ngọn cờ đầu Quốc gia",
        "prompt": """Phân tích vai trò và sứ mệnh 'National Champions' của Viettel và Vingroup đối với quốc gia:
1. Vingroup: Khát vọng "Làm đẹp cho đời", nâng tầm vị thế thương hiệu Việt Nam trên bản đồ công nghiệp và công nghệ toàn cầu.
2. Viettel: Trách nhiệm "Bảo vệ chủ quyền số, giữ vững an ninh quốc phòng và phụng sự Tổ quốc".
3. Mối quan hệ tương hỗ giữa Doanh nghiệp Nhà nước và Doanh nghiệp Tư nhân trong chiến lược vươn mình của kỷ nguyên mới. Trích dẫn các phát biểu của lãnh đạo Đảng, Nhà nước và lãnh đạo 2 tập đoàn."""
    },
    {
        "file": "08_cac_goc_nhin_phan_bien_va_rui_ro_tiem_an.md",
        "title": "Phản biện và Rủi ro Tiềm ẩn",
        "prompt": """Phân tích các góc nhìn phản biện khách quan, rủi ro và thách thức tiềm ẩn đối với mô hình của Viettel và Vingroup:
1. Rủi ro của Vingroup: Áp lực đòn bẩy tài chính, chi phí lãi vay và thâm dụng vốn khổng lồ của mảng xe điện VinFast; rủi ro cạnh tranh gay gắt từ các hãng xe điện Trung Quốc (BYD) và toàn cầu; áp lực duy trì tốc độ tăng trưởng.
2. Thách thức của Viettel: Rủi ro địa chính trị và biến động tỷ giá tại các thị trường Viettel Global (Myanmar, Haiti, châu Phi); thách thức thương mại hóa thiết bị 5G quy mô lớn trên thị trường quốc tế; cơ chế quản trị doanh nghiệp nhà nước.
3. Mặt trái của văn hóa kỷ luật thép đối với đời sống nhân viên và sự kiệt sức (burnout). Trích dẫn các báo cáo phân tích tài chính độc lập."""
    },
    {
        "file": "09_bai_hoc_thuc_chien_cho_ca_nhan_va_su_nghiep.md",
        "title": "Bài học Thực chiến cho Cá nhân",
        "prompt": """Từ triết lý và sự thành công của Viettel và Vingroup, hãy đúc rút hệ thống bài học và framework tư duy thực chiến dành cho cá nhân:
1. Doer's Mindset (Tư duy người thực thi): Vượt qua bẫy "nói trước", triệt tiêu dopamine giả tạo, tập trung hành động và để kết quả lên tiếng.
2. Career Moat (Hào kinh tế sự nghiệp): Tại sao phải dấn thân vào giải quyết việc khó để tạo sự khác biệt không thể thay thế.
3. Anti-Procrastination & Execution: Áp dụng quy tắc "Làm trước, học sau" và nguyên tắc cô đọng thông tin 1 trang giấy để nâng cao hiệu suất làm việc.
4. Quản trị cá nhân: Kỷ luật tự thân, vượt qua thất bại và xây dựng tư duy 'Trò chơi vô cực' (The Infinite Game)."""
    },
    {
        "file": "10_bai_hoc_quan_tri_cho_doanh_nghiep_nho_sme.md",
        "title": "Bài học Quản trị cho Doanh nghiệp SME",
        "prompt": """Đúc rút các bài học quản trị kinh doanh thực chiến cho các chủ doanh nghiệp vừa và nhỏ (SME), nhà khởi nghiệp từ kinh nghiệm của Viettel và Vingroup:
1. Chiến lược thâm nhập thị trường: Khi ít vốn thì "Lấy nông thôn vây thành thị", đánh ngách; khi có đòn bẩy thì tạo hệ sinh thái khác biệt.
2. Quản trị dòng tiền và nguồn lực: Nghệ thuật "cắt bỏ chi phí chìm", từ bỏ mảng không hiệu quả để bảo toàn dòng tiền cho mũi nhọn.
3. Văn hóa tổ chức: Cách thiết lập kỷ luật không bàn lùi, tối giản hóa thủ tục họp hành và tạo động lực từ những mục tiêu lớn."""
    }
]

def run_extraction():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    print(f"Bắt đầu trích xuất {len(EXTRACTION_QUESTIONS)} chủ đề từ Notebook: {NOTEBOOK_ID}")
    
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
                f.write("\n\n---\n*Trích xuất tự động qua NotebookLM Direct RPC Engine*\n")
            
            print(f"✅ Hoàn thành: {item['file']} ({len(answer)} ký tự)")
            time.sleep(2) # tránh rate limit
        except Exception as e:
            print(f"❌ Lỗi trích xuất {item['file']}: {e}")
            if hasattr(e, 'stderr') and e.stderr:
                print(f"Stderr: {e.stderr}")

if __name__ == "__main__":
    run_extraction()
