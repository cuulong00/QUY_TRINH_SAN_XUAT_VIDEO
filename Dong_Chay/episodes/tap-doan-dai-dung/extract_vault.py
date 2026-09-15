import os
import sys
import json
import subprocess
import time

NOTEBOOK_ID = "93df2e1c-62e3-4bd7-8cb9-7408f6159db9"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/tap-doan-dai-dung/research_vault"

os.makedirs(OUTPUT_DIR, exist_ok=True)

EXTRACTION_QUESTIONS = [
    {
        "file": "01_ho_so_nang_luc_va_lich_su_phat_trien_dai_dung.md",
        "title": "Hồ Sơ Năng Lực, Lịch Sử 30 Năm Phát Triển & Chân Dung Nhà Sáng Lập Trịnh Tiến Dũng",
        "prompt": """Phân tích chuyên sâu về hành trình 30 năm phát triển và hồ sơ năng lực của Tập đoàn Cơ khí Xây dựng Thương mại Đại Dũng (DaiDung Corporation / DDC):
1. Hành trình lịch sử: Từ xưởng cơ khí tư nhân năm 1995 đến vị thế tập đoàn công nghiệp nặng hàng đầu Việt Nam. Các mốc chuyển mình quan trọng (nhà xưởng công nghiệp -> siêu dự án sân vận động -> điện gió ngoài khơi -> EPC hạ tầng).
2. Chân dung và tầm nhìn của nhà sáng lập Trịnh Tiến Dũng (Chủ tịch HĐQT kiêm TGĐ): Triết lý quản trị, uy tín trong ngành cơ khí, vai trò tại HUBA và HĐQT PC1 Group.
3. Cấu trúc tập đoàn: Mô hình công ty mẹ - con, các đơn vị thành viên, cơ cấu nhân sự (>6.000 người), giá trị cốt lõi và văn hóa doanh nghiệp. Trích dẫn đầy đủ số liệu định lượng, mốc năm và nguồn."""
    },
    {
        "file": "02_he_thong_6_cum_nha_may_120ha_va_cong_suat_san_xuat.md",
        "title": "Hệ Thống 6 Cụm Nhà Máy 120 Hecta & Quy Mô Năng Lực Sản Xuất Cơ Khí Nặng",
        "prompt": """Phân tích chi tiết quy mô vật lý và hệ thống sản xuất của Tập đoàn Đại Dũng:
1. Chi tiết 6 cụm nhà máy với tổng diện tích 120 ha:
   - Nhà máy An Hạ / Bình Chánh (TP.HCM): Diện tích, công suất, sản phẩm chủ lực.
   - Cụm nhà máy Long An (Đức Hòa): Diện tích, chức năng.
   - Cụm nhà máy Quảng Ngãi (gần Dung Quất): Phục vụ tổ hợp luyện kim, lọc hóa dầu miền Trung.
   - Nhà máy Cơ khí Công nghệ cao Đông Xuyên (Vũng Tàu): Quy mô giai đoạn I (10 ha, công suất 87.000 tấn/năm), năng lực cầu cảng nước sâu xuất khẩu cấu kiện điện gió biển (Jacket, Monopile) và module dầu khí.
   - Tổ hợp Cơ khí Công nghệ cao Nghi Sơn (Thanh Hóa): Quy mô (45 ha, công suất giai đoạn I 73.000 tấn/năm), tổng vốn đầu tư, chức năng phục vụ năng lượng tái tạo, LNG, công nghiệp nặng.
2. Công suất thiết kế tổng thể: 500.000 tấn kết cấu thép/năm hiện tại và lộ trình nâng lên 800.000 tấn/năm vào năm 2030. Năng lực cẩu trục, bãi lắp thử (trial assembly) và năng lực gia công siêu trường siêu trọng. Trích dẫn số liệu cụ thể và nguồn."""
    },
    {
        "file": "03_he_thong_33_chung_chi_quoc_te_aisc_asme_en1090.md",
        "title": "Con Hào Kỹ Thuật: Hệ Thống 33+ Chứng Chỉ Quốc Tế Cao Cấp Nhất Toàn Cầu",
        "prompt": """Mổ xẻ chi tiết hệ thống hơn 33 chứng chỉ quốc tế uy tín của Tập đoàn Đại Dũng – con hào bảo hộ kỹ thuật giúp DDC bước vào chuỗi cung ứng toàn cầu:
1. AISC (Viện Kết cấu Thép Hoa Kỳ) & SPE (Sophisticated Paint Endorsement): Ý nghĩa kỹ thuật của chứng nhận chế tạo và chứng nhận sơn phủ chống ăn mòn môi trường biển khắc nghiệt.
2. ASME (Hoa Kỳ): Các dấu U, S, R Stamp cho thiết bị áp lực, bồn bể lò hơi, hóa dầu và nhiệt điện.
3. EN 1090-1 EXC4 (Tiêu chuẩn Châu Âu): Cấp độ kiểm soát Execution Class 4 (cấp cao nhất) cho kết cấu thép chịu lực đặc biệt, công trình cầu đường và sân vận động nhịp lớn.
4. Các chứng chỉ quốc tế khác: H-Grade (Nhật Bản - tiêu chuẩn kháng chấn), CWB (Canada - hàn thép nóng chảy), AS/NZS 5131 (Úc & New Zealand), ISO 3834-2 (quản lý chất lượng hàn).
5. Bộ chứng nhận Xanh: Tiêu chuẩn công trình xanh LEED Gold v4, kiểm kê khí nhà kính ISO 14064, ISO 14067, EPD và tuân thủ cơ chế điều chỉnh biên giới carbon CBAM của EU. Trích dẫn đầy đủ thông số kỹ thuật và nguồn."""
    },
    {
        "file": "04_cong_nghe_che_tao_bim_robotics_va_kiem_dinh_ndt.md",
        "title": "Công Nghệ Số Hóa BIM, Tự Động Hóa Robotics & Kiểm Định Chất Lượng Không Phá Hủy NDT",
        "prompt": """Phân tích năng lực công nghệ, chuyển đổi số và quy trình chế tạo cơ khí chính xác tại Đại Dũng:
1. Ứng dụng Mô hình thông tin công trình BIM (Tekla Structures, Revit): Mô phỏng số 3D, bóc tách cấu kiện, phân tích tải trọng động, tối ưu hóa vật liệu và quản lý vòng đời dự án.
2. Tự động hóa dây chuyền sản xuất: Máy cắt CNC Plasma/Laser Fiber công suất cao cắt thép tấm siêu dày, hệ thống hàn tự động dưới lớp thuốc (SAW), robot hàn gantry cho dầm hộp (box girder) và ống thép khẩu độ lớn.
3. Quy trình kiểm tra chất lượng không phá hủy (NDT): Các phương pháp kiểm định siêu âm (UT), chụp phim phóng xạ (RT), hạt từ tính (MPI), thẩm thấu chất lỏng (DPI) để đảm bảo 100% mối hàn chịu lực siêu trọng không có khuyết tật. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "05_sieu_du_an_world_cup_qatar_lusail_va_974.md",
        "title": "Hồ Sơ Gói Thầu 80 Triệu USD Tại FIFA World Cup 2022 (Sân Vận Động Lusail & 974)",
        "prompt": """Phân tích toàn diện dấu ấn lịch sử của Đại Dũng tại FIFA World Cup 2022 tại Qatar:
1. Bối cảnh và quy mô gói thầu: Đại Dũng là doanh nghiệp Việt Nam đầu tiên và duy nhất trúng gói thầu 80 triệu USD cung cấp hơn 34.000 tấn kết cấu thép cho 2 sân vận động:
   - Sân vận động Lusail Iconic (80.000 chỗ, nơi diễn ra trận Chung kết): Khối lượng ~6.000 tấn cấu kiện vòm phức tạp.
   - Sân vận động Ras Abu Aboud (Sân vận động 974): Khối lượng ~28.000 tấn kết cấu thép tháo lắp bằng container.
2. Thách thức kỹ thuật và quy trình đàm phán: Vượt qua các đối thủ quốc tế từ Trung Quốc, Thổ Nhĩ Kỳ, châu Âu; vượt qua hàng trăm tiêu chí kiểm định nghiêm ngặt của FIFA, tổng thầu và đơn vị tư vấn giám sát quốc tế.
3. Tác động của dự án đến vị thế thương hiệu quốc tế của Đại Dũng và ngành cơ khí Việt Nam. Trích dẫn số liệu chi tiết và nguồn."""
    },
    {
        "file": "06_ha_tang_quoc_gia_san_bay_long_thanh_t3_trien_lam_co_loa.md",
        "title": "Dấu Ấn Tại Các Siêu Hạ Tầng Trọng Điểm Quốc Gia & Trung Tâm Triển Lãm Cổ Loa",
        "prompt": """Phân tích vai trò và khối lượng thi công của Đại Dũng tại các công trình hạ tầng trọng điểm quốc gia:
1. Dự án Cảng hàng không Quốc tế Long Thành: Hạng mục kết cấu thép mái nhà ga hành khách, tiêu chuẩn kỹ thuật hàng không, yêu cầu dung sai và tiến độ.
2. Nhà ga T3 Cảng hàng không Quốc tế Tân Sơn Nhất, Sân bay Quảng Trị.
3. Trung tâm Hội chợ Triển lãm Quốc gia (Cổ Loa, Đông Anh, Hà Nội - Nhà triển lãm Kim Quy): Khối lượng 24.000 tấn thép mái vòm siêu khẩu độ, giải pháp kỹ thuật và sự phối hợp giữa Đại Dũng, ATAD, QH Plus cùng chủ đầu tư Vingroup.
4. Các dự án công nghiệp nặng: Khu liên hợp gang thép Hòa Phát Dung Quất 1 & 2, các nhà máy nhiệt điện, hóa dầu, các sân vận động mới (Hưng Yên 15.000 tấn, Trống Đồng 40.000 tấn). Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "07_nang_luong_tai_tao_dien_gio_ngoai_khoi_changhua_va_cip.md",
        "title": "Chinh Phục Đại Dương: Năng Lực Điện Gió Ngoài Khơi, Dự Án Greater Changhua & Đối Tác CIP",
        "prompt": """Phân tích chiến lược mở rộng sang lĩnh vực năng lượng tái tạo và điện gió ngoài khơi (Offshore Wind) của Đại Dũng:
1. Dự án điện gió ngoài khơi Greater Changhua (Đài Loan): Chế tạo thùng hút chân không (Suction Buckets) đường kính 14m, cao 16m, trọng lượng 350 tấn/cấu kiện. Yêu cầu kỹ thuật hàn và chống ăn mòn nước mặn cực hạn.
2. Năng lực chế tạo cấu kiện biển: Transition Pieces, Chân đế Jacket, Cột đơn Monopile, Tháp turbine gió.
3. Hợp tác chiến lược với Copenhagen Infrastructure Partners (CIP - Đan Mạch): Mục tiêu tham gia chuỗi cung ứng điện gió ngoài khơi toàn cầu và đón đầu các dự án điện gió ngoài khơi tại Việt Nam theo Quy hoạch Điện VIII. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "08_cac_du_an_quoc_te_saudi_uc_chau_au_fehmarnbelt.md",
        "title": "Hồ Sơ Các Dự Án Biểu Tượng Quốc Tế: Saudi Arabia, Úc, Châu Âu & Bắc Mỹ",
        "prompt": """Tổng hợp hồ sơ các dự án xuất khẩu quốc tế tiêu biểu của Đại Dũng sang hơn 50-60 quốc gia:
1. Bảo tàng Khoa học và Công nghệ Misk Ilmi (Ả Rập Saudi): Gói thầu 52 triệu USD với kiến trúc uốn cong 3D phức tạp.
2. Bảo tàng Powerhouse Parramatta (Úc): Cung cấp gần 9.000 tấn kết cấu thép tiêu chuẩn AS/NZS.
3. Siêu dự án đường hầm xuyên biển Fehmarnbelt (Đan Mạch - Đức): Cung cấp các cấu kiện thép chịu lực cho đường hầm dìm kết hợp đường sắt/đường bộ dài nhất thế giới.
4. Các dự án nhà máy công nghiệp, trung tâm dữ liệu (Data Center), nhà xưởng công nghệ cao tại Mỹ, Nhật Bản, Indonesia. Trích dẫn số liệu giá trị hợp đồng, khối lượng tấn và nguồn."""
    },
    {
        "file": "09_thuong_vu_dau_tu_38m_usd_ifc_va_co_cau_tai_chinh.md",
        "title": "Thương Vụ Đầu Tư 38 Triệu USD Của IFC (World Bank) & Cấu Trúc Tài Chính Đại Dũng",
        "prompt": """Mổ xẻ chi tiết thương vụ đầu tư của Tổ chức Tài chính Quốc tế (IFC) vào Đại Dũng và cấu trúc tài chính tập đoàn:
1. Chi tiết thương vụ: Tháng 10/2025, IFC rót 38 triệu USD (~1.000 tỷ VND) dưới hình thức vốn lai (quasi-equity). Bản chất công cụ vốn lai, lợi ích so với vay nợ thông thường và cơ chế phân chia lợi nhuận.
2. Mục đích sử dụng vốn: Tài trợ cho kế hoạch mở rộng 152 triệu USD bao gồm Nhà máy Nghi Sơn (Thanh Hóa - 45 ha) và Nhà máy Đông Xuyên (Vũng Tàu - 10 ha) theo chuẩn công trình xanh LEED Gold.
3. Cơ cấu vốn và cổ đông: Vốn điều lệ đạt ~1.999 tỷ VND (100% tư nhân), sức khỏe tài chính và sự chuẩn mực hóa quản trị doanh nghiệp theo chuẩn mực ESG của World Bank. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "10_ke_hoach_ipo_2026_va_chien_luoc_doanh_thu_ty_do_2030.md",
        "title": "Kế Hoạch IPO 2026, Tăng Trưởng Doanh Thu & Mục Tiêu Tập Đoàn Tỷ Đô 2030",
        "prompt": """Phân tích kế hoạch kinh doanh, lộ trình IPO và chiến lược dài hạn của Đại Dũng:
1. Kết quả kinh doanh và Backlog hợp đồng: Doanh thu tăng trưởng 28%, sản lượng tăng 26%, giá trị hợp đồng ký mới tăng 65%. Riêng đầu năm 2026 ghi nhận 34 hợp đồng mới trị giá hơn 6.650 tỷ đồng.
2. Kế hoạch tài chính: Mục tiêu doanh thu 12.000 tỷ đồng trong năm 2026, kế hoạch IPO (chào bán cổ phiếu lần đầu ra công chúng) năm 2026.
3. Tầm nhìn chiến lược 2030: Hướng tới doanh thu trên 1 tỷ USD trước năm 2030, nâng công suất lên 800.000 tấn/năm, định vị là tập đoàn giải pháp kết cấu thép và EPC công nghiệp nặng hàng đầu thế giới. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "11_phan_tich_doi_thu_va_vi_the_thi_truong_atad_zamil_ptsc.md",
        "title": "Ma Trận Cạnh Tranh: Đại Dũng vs. ATAD, Zamil Steel, PTSC & Các Nhà Thầu Quốc Tế",
        "prompt": """Phân tích ma trận cạnh tranh và tương quan vị thế của Đại Dũng với các đối thủ trong ngành kết cấu thép và công nghiệp nặng:
1. So sánh với ATAD Steel: Quy mô nhà máy (120 ha vs 36 ha), công suất (500k tấn vs 216k tấn), định vị phân khúc (Đại Dũng mạnh về công nghiệp nặng, cảng biển, hạ tầng siêu trọng; ATAD mạnh về nhà thép tiền chế PEB, thương mại, thị trường Đông Nam Á). Các dự án phối hợp (Triển lãm Cổ Loa, Sân bay Long Thành).
2. So sánh với Zamil Steel, BMB Steel, QH Plus.
3. So sánh với các doanh nghiệp cơ khí dầu khí truyền thống (PTSC M&C, Lilama) trong mảng năng lượng ngoài khơi và chế tạo kết cấu biển.
4. Lợi thế cạnh tranh con hào (Moats) của Đại Dũng: Chi phí sản xuất tối ưu tại Việt Nam kết hợp tiêu chuẩn kỹ thuật G7 và vị trí cảng biển nước sâu. Trích dẫn số liệu so sánh và nguồn."""
    },
    {
        "file": "12_rui_ro_gia_thep_bien_loi_nhuan_va_rao_can_cbam_green_steel.md",
        "title": "Phản Biện Kinh Tế: Rủi Ro Biến Động Giá Thép, Biên Lợi Nhuận & Rào Cản Carbon CBAM",
        "prompt": """Phân tích các góc nhìn phản biện khách quan về rủi ro hoạt động, tài chính và rào cản thương mại mà Đại Dũng phải đối mặt:
1. Rủi ro biến động giá nguyên liệu thép: Phụ thuộc vào giá thép cuộn cán nóng HRC, phôi thép nhập khẩu và biến động thị trường thép Trung Quốc/thế giới. Tác động của rủi ro trượt giá vật liệu lên các hợp đồng EPC cố định (Lump-sum contracts).
2. Biên lợi nhuận ngành: Bản chất ngành gia công cơ khí kết cấu thép có biên lợi nhuận ròng tương đối mỏng (khoảng 3-6%), đòi hỏi quản trị chi phí cực kỳ khắt khe và vòng quay vốn lưu động nhanh.
3. Rào cản thương mại xanh: Cơ chế điều chỉnh biên giới carbon (CBAM) của EU, yêu cầu kiểm kê phát thải khí nhà kính (Scope 1, 2, 3), bài toán chuyển đổi sang Thép Xanh (Green Steel) và chi phí chứng nhận ESG.
4. Rủi ro quản trị khi mở rộng quy mô thần tốc lên 800.000 tấn/năm và gánh nặng chi phí lãi vay đầu tư tài sản cố định (Capex). Trích dẫn số liệu và phân tích tài chính."""
    }
]

def run_extraction():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    print(f"Bắt đầu trích xuất chuyên sâu {len(EXTRACTION_QUESTIONS)} chuyên đề từ Master Notebook: {NOTEBOOK_ID}")
    
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
                f.write("\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC Deep Research Engine*\n")
            
            print(f"✅ Hoàn thành: {item['file']} ({len(answer)} ký tự)")
            time.sleep(1)
        except Exception as e:
            print(f"❌ Lỗi trích xuất {item['file']}: {e}")
            if hasattr(e, 'stderr') and e.stderr:
                print(f"Stderr: {e.stderr}")

if __name__ == "__main__":
    run_extraction()
