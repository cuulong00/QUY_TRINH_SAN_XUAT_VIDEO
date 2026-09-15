import subprocess
import os
import json

NOTEBOOK_ID = "592b802f-1f62-4720-bb03-c296066dce97"
HOME_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
CLI_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
VAULT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/sieu-du-an-ky-luc-the-gioi-viet-nam/research_vault"

QUERIES = [
    {
        "filename": "01_tong_quan_sieu_du_an_ky_luc.md",
        "title": "Tổng quan siêu dự án kỷ lục tại Việt Nam",
        "prompt": """Phân tích chi tiết quy mô, thiết kế kiến trúc, vốn đầu tư, vị trí và tiến độ của 2 siêu dự án đang gây chú ý tại Việt Nam:
1. Sân vận động VinFast - Trống Đồng (135.000 chỗ ngồi tại Khu đô thị Thể thao Quốc tế Hùng Vương, Thượng Phúc, Hà Nội). So sánh chi tiết sức chứa, diện tích, hệ thống mái che với SVĐ Narendra Modi (Ấn Độ - 132.000 chỗ), SVĐ Rungrado 1/5 (Triều Tiên - 114.000 chỗ) và SVĐ Quốc gia Mỹ Đình (40.000 chỗ).
2. Dự án Hanoi Twin Towers 99 (568m, 99 tầng tại 5-7 Đào Duy Anh, Đống Đa, Hà Nội - Khách sạn Kim Liên cũ, liên danh Thaiholdings - Du lịch Kim Liên - Thái Sơn Vingroup). So sánh chiều cao và số tầng với Petronas Twin Towers (Malaysia - 452m), Landmark 81 (461m) và Tháp Tài chính Phương Trạch (108 tầng, 639m).
Yêu cầu: Liệt kê số liệu định lượng, mốc thời gian cụ thể và các nguồn tham chiếu."""
    },
    {
        "filename": "02_chien_luoc_trophy_asset_land_value.md",
        "title": "Chiến lược Trophy Asset và Land Value Capture",
        "prompt": """Phân tích cơ chế kinh tế và bất động sản: Tại sao các tập đoàn bất động sản lớn (như Vingroup, Emaar, các tập đoàn quốc tế) sẵn sàng chi hàng tỷ USD để xây dựng các công trình 'cao nhất', 'lớn nhất' thế giới?
1. Giải thích khái niệm 'Trophy Asset' (Tài sản biểu tượng) và 'Land Value Capture' (Thâu tóm giá trị đất).
2. Cơ chế lan tỏa (Halo Effect / Real Estate Anchoring): Công trình biểu tượng tác động thế nào đến việc nâng trần định giá, tốc độ bán hàng, tính thanh khoản và biên lợi nhuận của toàn bộ quần thể đại đô thị hàng trăm hecta xung quanh?
3. Trích dẫn ví dụ thực chứng từ Landmark 81 với Vinhomes Central Park, Burj Khalifa với Downtown Dubai, và SVĐ VinFast Trống Đồng với Khu đô thị Thể thao Quốc tế Hùng Vương."""
    },
    {
        "filename": "03_kinh_te_su_kien_stadium_economics.md",
        "title": "Kinh tế Sân vận động và Nền kinh tế Sự kiện",
        "prompt": """Phân tích bài toán kinh tế học sân vận động (Stadium Economics) và Nền kinh tế Sự kiện (Mega-Event Economy):
1. Các dòng doanh thu chính của một siêu sân vận động hiện đại trên thế giới: Naming Rights (quyền đặt tên), VIP Box / Hospitality Suites, Bán vé thể thao & Mega Concert (Taylor Swift Eras Tour, Coldplay, K-Pop), Quảng cáo, Bản quyền truyền hình, Dịch vụ F&B, Du lịch MICE.
2. Sân vận động Mỹ Đình (40.000 chỗ) đang gặp những điểm nghẽn gì về hạ tầng, mặt sân, dịch vụ và khả năng đón các sự kiện quốc tế tỷ USD?
3. Việt Nam cần hệ sinh thái bổ trợ nào (giao thông kết nối, khách sạn, thủ tục visa, năng lực tổ chức sự kiện quốc tế) để SVĐ 135.000 chỗ đạt điểm hòa vốn và sinh lời?"""
    },
    {
        "filename": "04_rui_ro_voi_trang_chi_phi_van_hanh.md",
        "title": "Rủi ro Voi trắng và Gánh nặng Chi phí Vận hành",
        "prompt": """Phân tích góc nhìn phản biện về rủi ro 'Voi trắng' (White Elephant) và chi phí vận hành (O&M - Operation & Maintenance):
1. Chi phí vận hành, bảo trì, chăm sóc mặt cỏ, hệ thống điện chiếu sáng, điều hòa và mái che tự động của một sân vận động quy mô 100.000 - 135.000 chỗ ngồi ước tính là bao nhiêu mỗi năm?
2. Bài học cảnh báo từ các công trình biểu tượng quốc tế bị bỏ hoang hoặc thua lỗ nặng nề sau các kỳ Thế vận hội / World Cup (như SVĐ Tổ Chim Bắc Kinh, các sân vận động tại Hy Lạp, Brazil, Nam Phi).
3. Nếu tần suất tổ chức sự kiện thấp (chỉ vài trận bóng đá/năm), hậu quả tài chính đối với chủ đầu tư và ngân sách sẽ ra sao?"""
    },
    {
        "filename": "05_loi_nguyen_skyscraper_index_chu_ky_von.md",
        "title": "Lời nguyền Skyscraper Index và Chu kỳ Tín dụng",
        "prompt": """Phân tích lý thuyết 'Chỉ số Tòa nhà chọc trời' (Skyscraper Index của nhà kinh tế Andrew Lawrence - 1999):
1. Nội dung cốt lõi của Skyscraper Index: Mối tương quan lịch sử giữa việc khởi công/xây dựng các tòa nhà cao nhất thế giới với đỉnh điểm của chu kỳ tín dụng rẻ, đầu cơ tài sản và theo sau bởi suy thoái kinh tế.
2. Các ví dụ lịch sử kinh điển: Empire State Building & Chrysler Building (Đại khủng hoảng 1929), Petronas Twin Towers (Khủng hoảng tài chính châu Á 1997), Burj Khalifa (Khủng hoảng nợ Dubai & Toàn cầu 2008-2010).
3. Đánh giá rủi ro tài chính khi triển khai siêu dự án tháp đôi 99 tầng (vốn 3 - 3,5 tỷ USD) tại Hà Nội trong bối cảnh chu kỳ bất động sản và chi phí vốn hiện nay."""
    },
    {
        "filename": "06_quy_hoach_ha_tang_loi_noi_do.md",
        "title": "Quy hoạch Đô thị và Áp lực Hạ tầng Lõi Nội Đô",
        "prompt": """Phân tích các rào cản quy hoạch và tác động hạ tầng của dự án Hanoi Twin Towers 99 tầng tại số 5-7 Đào Duy Anh:
1. Quy chế quản lý quy hoạch, kiến trúc công trình cao tầng trong khu vực nội đô lịch sử Hà Nội (khu vực hạn chế chiều cao và mật độ xây dựng theo Quy hoạch chung Thủ đô).
2. Động lực chính sách: Tại sao chủ đầu tư đề xuất công trình 99 tầng kèm nhiều kỷ lục thế giới? Vai trò của yếu tố 'biểu tượng kiến trúc' trong việc xin cơ chế đặc thù, tăng hệ số sử dụng đất (FAR) và chỉnh trang đô thị.
3. Thách thức giao thông hạ tầng: Đánh giá áp lực gia tăng dân số, lưu lượng phương tiện lên nút giao Đào Duy Anh - Kim Liên - Giải Phóng nếu không có hệ thống đường sắt đô thị (Metro) ngầm đồng bộ."""
    },
    {
        "filename": "07_bai_hoc_quoc_te_petronas_burj_evergrande.md",
        "title": "Bài học Quốc tế: Thành công vs Đổ vỡ",
        "prompt": """So sánh đối chiếu 4 bài học quốc tế về việc xây dựng công trình biểu tượng kỷ lục:
1. Petronas Twin Towers (Malaysia): Thành công trong việc đưa thương hiệu quốc gia Malaysia và Kuala Lumpur lên bản đồ tài chính toàn cầu, dù trải qua khủng hoảng 1997.
2. Burj Khalifa & Dubai: Chiến lược 'Xây dựng biểu tượng để tái định vị nền kinh tế' từ dầu mỏ sang du lịch, tài chính và bất động sản toàn cầu.
3. Narendra Modi Stadium (Ấn Độ): Công cụ khẳng định vị thế cường quốc mới nổi và ngoại giao thể thao.
4. Dự án Evergrande Stadium (Quảng Châu, Trung Quốc - 100.000 chỗ, thiết kế hoa sen, vốn 1,7 tỷ USD): Dự án từng tham vọng lớn nhất thế giới nhưng bị đình trệ và sụp đổ cùng cuộc khủng hoảng nợ của Tập đoàn Evergrande.
Bài học rút ra cho các tập đoàn và nhà hoạch định chính sách Việt Nam là gì?"""
    },
    {
        "filename": "08_dinh_vi_quoc_gia_vs_hu_danh.md",
        "title": "Định vị Quốc gia vs Hư danh: Lằn ranh Thực chất",
        "prompt": """Tổng hợp và kết luận đa chiều: Các siêu dự án 'lớn nhất thế giới', 'cao nhất thế giới' tại Việt Nam là Hư danh hay Đòn bẩy Marketing & Kinh tế thực chất?
1. Lập luận của phe ủng hộ (Thesis): Khát vọng vươn tầm, tạo biểu tượng thế kỷ, kích cầu kinh tế đô thị, thu hút ngoại tệ và dòng vốn quốc tế, tạo đòn bẩy cho công nghiệp văn hóa và thể thao.
2. Lập luận của phe phản biện (Counter-thesis): Nguy cơ lãng phí nguồn lực xã hội, bẫy nợ tài chính, rủi ro voi trắng, áp lực quá tải hạ tầng đô thị và căn bệnh thành tích/hư danh.
3. Đề xuất nguyên tắc quản trị: Điều kiện tiên quyết để một siêu công trình kỷ lục trở thành động lực phát triển bền vững thay vì trở thành gánh nặng di sản."""
    }
]

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = HOME_DIR

for item in QUERIES:
    filepath = os.path.join(VAULT_DIR, item["filename"])
    print(f"[*] Extracting: {item['title']} -> {item['filename']}...")
    cmd = [
        CLI_PATH,
        "ask",
        item["prompt"],
        "-n", NOTEBOOK_ID,
        "--save-as-note",
        "-t", item["title"],
        "--json"
    ]
    try:
        res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=180)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            content = data.get("answer", "")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {item['title']}\n\n{content}\n")
            print(f"[✓] Saved {item['filename']} ({len(content)} chars)")
        else:
            print(f"[✗] Error extracting {item['filename']}: {res.stderr}")
    except Exception as e:
        print(f"[!] Exception for {item['filename']}: {e}")

print("\n[✓] Batch Extraction Complete!")
