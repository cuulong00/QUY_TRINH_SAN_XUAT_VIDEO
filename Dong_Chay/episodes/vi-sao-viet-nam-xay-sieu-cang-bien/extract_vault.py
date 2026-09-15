import os
import sys
import json
import subprocess
import time

NOTEBOOK_ID = "b0e0cc8f-84b4-4d4f-b3d1-1c7e86ea0aa9"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/vi-sao-viet-nam-xay-sieu-cang-bien/research_vault"

os.makedirs(OUTPUT_DIR, exist_ok=True)

EXTRACTION_QUESTIONS = [
    {
        "file": "01_dong_luc_vi_mo_va_quy_hoach_1579.md",
        "title": "Động Lực Kinh Tế Vĩ Mô & Quy Hoạch Cảng Biển Quốc Gia 1579/QĐ-TTg",
        "prompt": """Phân tích chuyên sâu về động lực kinh tế vĩ mô và Quy hoạch tổng thể phát triển hệ thống cảng biển Việt Nam thời kỳ 2021-2030, tầm nhìn đến năm 2050 (Quyết định 1579/QĐ-TTg):
1. Động lực vĩ mô: Tốc độ tăng trưởng kim ngạch xuất nhập khẩu của Việt Nam (vượt 730-800 tỷ USD), tỷ lệ XNK/GDP vượt 160-180% (độ mở kinh tế hàng đầu thế giới), áp lực từ làn sóng dịch chuyển sản xuất FDI toàn cầu.
2. Mục tiêu quy hoạch 1579: Khối lượng hàng hóa thông qua dự kiến (1,14 - 1,42 tỷ tấn hàng hóa, 38 - 47 triệu TEU container vào năm 2030). Phân loại các cảng đặc biệt (Cái Mép, Lạch Huyện, Cần Giờ) và chiến lược đưa Việt Nam trở thành trung tâm hàng hải khu vực.
3. Trích dẫn đầy đủ số liệu định lượng, mốc năm, căn cứ pháp lý và nguồn tài liệu."""
    },
    {
        "file": "02_bai_toan_chi_phi_logistics_gdp.md",
        "title": "Bóc Trần Gánh Nặng Chi Phí Logistics & Lợi Thế Tuyến Tàu Mẹ Trực Tiếp",
        "prompt": """Phân tích chuyên sâu về gánh nặng chi phí logistics của Việt Nam và cơ chế kinh tế của tuyến tàu mẹ trực tiếp (Direct Calls):
1. Thực trạng chi phí logistics Việt Nam: Chiếm 16.8% - 18% GDP (so với mức trung bình thế giới 10.7%, Singapore ~8%, Trung Quốc ~14%). Tác động bào mòn biên lợi nhuận của doanh nghiệp sản xuất và xuất khẩu trong nước.
2. Cơ chế kinh tế của Tuyến tàu mẹ trực tiếp (Direct mother vessel calls) từ cảng nước sâu Việt Nam đi Mỹ (Bờ Tây, Bờ Đông) và Châu Âu: Tiết kiệm $150 - $300/TEU chi phí trung chuyển feeder, rút ngắn 3-5 ngày thời gian hải trình so với việc phải chuyển tải qua Singapore hay Hong Kong.
3. Nhu cầu cấp thiết phải nâng cấp cảng để đón các siêu tàu container thế hệ mới 18.000 - 24.000 TEU (250.000 DWT). Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "03_cuoc_chien_cang_trung_chuyen_quoc_te_singapore_malaysia.md",
        "title": "Cuộc Chiến Giành Thị Phần Cảng Trung Chuyển Quốc Tế Đông Nam Á",
        "prompt": """Phân tích bản đồ chiến trường hàng hải Đông Nam Á và cuộc cạnh tranh giành vị thế Cảng trung chuyển quốc tế (International Transshipment Hub):
1. So sánh tương quan vị thế, công suất và công nghệ của Việt Nam với các đối thủ lớn: Siêu cảng Tuas của Singapore (20 tỷ USD, công suất 65 triệu TEU, tự động hóa toàn diện), Cảng Tanjung Pelepas (PTP) và Port Klang của Malaysia, Cảng Laem Chabang của Thái Lan.
2. Tiêu chí quyết định một cảng có thể trở thành Hub trung chuyển quốc tế: Độ lệch luồng hàng hải (deviation time), giá cước bốc dỡ THC, năng suất cẩu bến, và cam kết nguồn hàng của các liên minh hãng tàu.
3. Tác động của các biến số địa kinh tế khu vực: Kênh đào Funan Techo (Campuchia), đề xuất Landbridge eo biển Kra (Thái Lan). Trích dẫn số liệu so sánh chi tiết và nguồn."""
    },
    {
        "file": "04_lien_minh_hang_tau_va_van_co_msc_can_gio.md",
        "title": "Giải Mã Ván Cược Gần 5 Tỷ USD Của MSC Tại Cần Giờ",
        "prompt": """Phân tích chi tiết về dự án Cảng trung chuyển quốc tế Cần Giờ và chiến lược của Tập đoàn Hàng hải MSC (Mediterranean Shipping Company):
1. Thông số dự án: Tổng mức đầu tư gần 5 tỷ USD (~129.000 tỷ VNĐ), diện tích 571 ha, chiều dài cầu bến chính 7.2 - 7.5 km, công suất tối đa dự kiến 16.9 triệu TEU vào năm 2047. Cơ cấu liên danh: MSC/TIL nắm 49%, VIMC nắm 36%, Cảng Sài Gòn nắm 15%.
2. Chiến lược của MSC: Vì sao hãng tàu số 1 thế giới (gần 20% thị phần đội tàu toàn cầu) chọn Cần Giờ làm căn cứ trung chuyển sau khi liên minh 2M giải thể? Chiến lược mạng lưới độc lập (Standalone network) của MSC.
3. Cơ cấu nguồn hàng: Tỷ lệ hàng trung chuyển quốc tế ngoại khối (chiếm 75-80%) vs hàng nội địa (20-25%). Lợi ích kinh tế và đóng góp ngân sách nhà nước dự kiến. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "05_cai_mep_thi_vai_va_nghich_ly_ao_tu_nuoc_sau.md",
        "title": "Cụm Cảng Cái Mép - Thị Vải & Nghịch Lý Phân Bổ Nguồn Hàng Phía Nam",
        "prompt": """Phân tích thực trạng cụm cảng nước sâu Cái Mép - Thị Vải và bài toán phân định vai trò với Cảng Cần Giờ:
1. Hiện trạng và năng lực của Cái Mép - Thị Vải: Các bến cảng quốc tế (TCIT, CMIT, TCTT, SSIT, Gemalink), sản lượng thông qua hàng năm, xếp hạng Top 10-12 thế giới về hiệu quả hoạt động cảng container (theo World Bank & S&P Global CPPI).
2. Phân tích tranh cãi: Liệu Cần Giờ và Cái Mép có giẫm chân, triệt tiêu thị phần của nhau hay không? Mô hình 'Hai bờ một cửa ngõ' (twin-hub) và phân công chức năng (Cái Mép là cảng cửa ngõ xuất nhập khẩu quốc gia, Cần Giờ là cảng trung chuyển quốc tế của hãng tàu MSC).
3. Nghịch lý Cát Lái quá tải, kẹt xe nội đô TP.HCM trong khi Cái Mép từng thừa công suất vì hạ tầng kết nối yếu. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "06_lach_huyen_hai_phong_va_cuc_tang_truong_mien_bac.md",
        "title": "Cảng Nước Sâu Lạch Huyện & Cực Tăng Trưởng Công Nghiệp Miền Bắc",
        "prompt": """Phân tích vai trò chiến lược của Cụm cảng nước sâu Lạch Huyện (Hải Phòng) đối với tam giác kinh tế phía Bắc:
1. Năng lực tiếp nhận tàu mẹ trọng tải lớn (12.000 - 18.000 TEU, 132.000 - 160.000 DWT) kết nối thẳng đi Bờ Tây nước Mỹ và Châu Âu.
2. Tiến độ triển khai các bến cảng: Bến 1-2 (TC-HICT), Bến 3-4 (Cảng Hải Phòng/VIMC), Bến 5-6 (Hateco), Bến 7-8.
3. Vai trò bệ phóng cho các chuỗi sản xuất công nghệ cao miền Bắc (Samsung, LG, Foxconn, Luxshare, Amkor, Pegatron, VinFast Hải Phòng) và định hướng Khu thương mại tự do Hải Phòng, cụm cảng Nam Đồ Sơn. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "07_lan_song_dich_chuyen_fdi_china_plus_one.md",
        "title": "Làn Sóng Dịch Chuyển Chuỗi Cung Ứng Toàn Cầu (China+1) & Áp Lực Cảng Biển",
        "prompt": """Phân tích mối quan hệ giữa làn sóng dịch chuyển chuỗi cung ứng sản xuất toàn cầu (China+1 / Friendshoring) và chiến lược siêu cảng biển của Việt Nam:
1. Dòng vốn FDI và sự chuyển dịch của các đại bàng công nghệ (Apple, Foxconn, Samsung, Pegatron, Lego, BYD) vào Việt Nam, thúc đẩy nhu cầu logistics quy mô lớn.
2. Xu hướng chuyển từ cảng sông nước nông (Cảng Sài Gòn, Bến Nghé, Cát Lái, sông Cấm Hải Phòng) sang cảng nước sâu ven biển để thích ứng với kỷ nguyên siêu tàu container (Megaship era từ 4.000 TEU lên 24.000 TEU).
3. Hạ tầng cảng biển nước sâu như điều kiện cốt tử để Việt Nam giữ vững vị thế 'công xưởng mới của thế giới'. Trích dẫn số liệu FDI, xuất nhập khẩu và nguồn."""
    },
    {
        "file": "08_ket_noi_ha_tang_sau_cang_duong_sat_va_thuy_noi_dia.md",
        "title": "Điểm Nghẽn Hạ Tầng Sau Cảng (Hinterland) & Bài Toán Kết Nối Đa Phương Thức",
        "prompt": """Mổ xẻ điểm nghẽn lớn nhất trong chuỗi logistics cảng biển Việt Nam - Hạ tầng kết nối sau cảng (Hinterland Connectivity):
1. Thực trạng phụ thuộc: Hơn 80% hàng hóa đến cụm cảng Cái Mép phải trung chuyển bằng sà lan đường thủy nội địa hoặc xe container đường bộ qua Quốc lộ 51 đang quá tải nghiêm trọng.
2. Sự thiếu vắng mạng lưới đường sắt kết nối trực tiếp vào cảng biển: Tình trạng chưa có đường sắt kết nối Cái Mép (tuyến Biên Hòa - Vũng Tàu) và Lạch Huyện (tuyến Lào Cai - Hà Nội - Hải Phòng).
3. Các dự án hạ tầng đột phá đang triển khai để tháo gỡ điểm nghẽn: Cầu Phước An, Cao tốc Biên Hòa - Vũng Tàu, Vành đai 3, Vành đai 4 TP.HCM, Cầu Cần Giờ. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "09_bai_toan_moi_truong_va_rung_ngap_man_can_gio.md",
        "title": "Tranh Cãi Môi Trường & Khu Dự Trữ Sinh Quyển Rừng Ngập Mặn Cần Giờ",
        "prompt": """Phân tích các đánh giá tác động môi trường (ĐTM) và tranh cãi bảo tồn sinh thái xung quanh dự án Cảng Cần Giờ:
1. Vị trí địa lý tại Cù lao Phú Lợi: Nằm trong vùng đệm/vùng chuyển tiếp (transition zone) của Khu dự trữ sinh quyển Rừng ngập mặn Cần Giờ (UNESCO), không nằm trong vùng lõi (core zone).
2. Tác động môi trường cụ thể: Khoảng 89.7 ha rừng ngập mặn bị ảnh hưởng; phương án trồng rừng thay thế gấp 3 lần (~270 ha); tác động của hoạt động nạo vét luồng hàng hải (25-30 triệu m3 bùn cát), nguy cơ bồi lắng và xói lở bờ sông Soài Rạp/Lòng Tàu.
3. Các giải pháp công nghệ cảng sinh thái, giảm thiểu tác động sinh thái và cam kết bảo tồn của chính quyền và chủ đầu tư. Trích dẫn tài liệu ĐTM và nguồn khoa học."""
    },
    {
        "file": "10_rui_ro_du_thua_cong_suat_va_phan_manh_thi_phan.md",
        "title": "Phản Biện Kinh Tế: Rủi Ro Dư Thừa Công Suất & Cạnh Tranh Hạ Cước",
        "prompt": """Phân tích các góc nhìn phản biện khách quan về rủi ro đầu tư và vận hành hệ thống siêu cảng biển Việt Nam:
1. Nguy cơ dư thừa công suất (Overcapacity): Bài học giai đoạn 2011-2015 khi Cái Mép chỉ đạt 20-30% công suất, các liên doanh cảng cạnh tranh hạ giá cước xả hàng (price dumping), thua lỗ kéo dài.
2. Rủi ro phân mảnh thị phần: Sự chậm trễ trong di dời cảng nội đô (Cát Lái) khiến hàng hóa không chịu đổ về cảng nước sâu do thói quen của chủ hàng và chi phí đường bộ ngắn hơn.
3. Rủi ro biến động chu kỳ vận tải biển toàn cầu, sự chia tách và tái cơ cấu các liên minh hãng tàu (2M, Gemini Cooperation, Ocean Alliance, Premier Alliance). Trích dẫn số liệu và phân tích tài chính."""
    },
    {
        "file": "11_chuyen_doi_cang_xanh_va_tu_dong_hoa_smart_port.md",
        "title": "Xu Hướng Chuyển Đổi Cảng Xanh & Cảng Thông Minh (Smart Port)",
        "prompt": """Phân tích xu hướng Chuyển đổi Cảng Xanh (Green Port) và Tự động hóa Cảng thông minh (Smart Port) tại Việt Nam:
1. Áp lực từ quy chuẩn quốc tế: Quy định giảm phát thải của IMO (Net Zero 2050, chỉ số CII, EEXI) và Cơ chế điều chỉnh biên giới carbon EU (CBAM).
2. Công nghệ cấp điện bờ (Cold Ironing / Onshore Power Supply - OPS) cho tàu mẹ khi cập cảng, điện hóa thiết bị cẩu bãi (e-RTG, e-STS), hệ thống điều hành cảng thông minh TOS (Terminal Operating System), cổng nhận diện tự động AI/OCR.
3. Thực tiễn áp dụng tại Cảng Gemalink, TCIT, Cái Mép và định hướng thiết kế Cần Giờ, Lạch Huyện. Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "12_tong_hop_so_lieu_dinh_luong_va_so_sanh_quoc_te.md",
        "title": "Bảng Số Liệu Định Lượng Tổng Hợp & So Sánh Quốc Tế Toàn Diện",
        "prompt": """Tổng hợp bảng số liệu định lượng chi tiết so sánh hệ thống cảng biển Việt Nam với các cảng biển lớn trong khu vực và trên thế giới:
1. Bảng so sánh các cảng biển: Cần Giờ, Cái Mép - Thị Vải, Lạch Huyện, Tuas (Singapore), Tanjung Pelepas (Malaysia), Port Klang (Malaysia), Laem Chabang (Thái Lan), Thượng Hải (Trung Quốc). Các thông số: Vốn đầu tư, diện tích, chiều dài cầu bến, mớn nước (draft), kích cỡ tàu tối đa tiếp nhận (DWT & TEU), công suất thiết kế, sản lượng thực tế, cước bốc dỡ THC.
2. Chỉ số Hiệu quả Logistics (Logistics Performance Index - LPI) của World Bank: Thứ hạng và điểm số của Việt Nam qua các năm so với ASEAN và thế giới.
3. Ma trận các hãng tàu container lớn nhất thế giới và liên minh hàng hải tại Việt Nam (MSC, Maersk, CMA CGM, COSCO, Hapag-Lloyd, ONE, Evergreen). Trích dẫn đầy đủ số liệu chính thống và nguồn."""
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
            time.sleep(2)
        except Exception as e:
            print(f"❌ Lỗi trích xuất {item['file']}: {e}")
            if hasattr(e, 'stderr') and e.stderr:
                print(f"Stderr: {e.stderr}")

if __name__ == "__main__":
    run_extraction()
