import os
import subprocess
import json
import time

NOTEBOOK_ID = "8a0efeb8-9576-4aa6-ad4e-eafe5a60da34"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
CLI_PATH = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
VAULT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/van-cuoc-seu-dau-dan/research_vault"

os.makedirs(VAULT_DIR, exist_ok=True)

QUESTIONS = [
    {
        "file": "01_nghi_quyet_79_the_che_kinh_te_nha_nuoc.md",
        "title": "Nghị Quyết 79 & Đột Phá Thể Chế Kinh Tế Nhà Nước",
        "query": """Trích xuất toàn bộ thông tin chi tiết, chính xác về Nghị quyết số 79-NQ/TW ngày 06/01/2026 của Bộ Chính trị về phát triển kinh tế nhà nước và chiến lược Sếu Đầu Đàn:
1. Hoàn cảnh ra đời, vai trò chủ đạo và 9 thành tố cấu thành kinh tế nhà nước.
2. Mục tiêu định lượng cụ thể đến năm 2030 (số lượng doanh nghiệp vào Fortune Global 500, Top 500 Đông Nam Á, chuẩn mực quản trị OECD, top ngân hàng châu Á) và tầm nhìn 2045.
3. Cơ chế tháo gỡ điểm nghẽn thể chế: Phân định rủi ro kinh doanh và vi phạm pháp luật, bảo vệ cán bộ dám nghĩ dám làm, giải quyết nút thắt 'bảo toàn vốn'.
4. Nguyên tắc hạch toán thị trường, không bảo hộ, không độc quyền, và cơ chế giữ lại nguồn thu cổ phần hóa để tái đầu tư.
Trình bày chi tiết, có số liệu, văn bản và trích dẫn nguồn."""
    },
    {
        "file": "02_tuyen_phong_thu_7_tap_doan_nha_nuoc_va_tro_cap_ngam.md",
        "title": "Tuyến Phòng Thủ: 7 Tập Đoàn Nhà Nước Trụ Cột & Cơ Chế Trợ Cấp Ngầm",
        "query": """Giải phẫu chi tiết vai trò của 7 Tập đoàn Doanh nghiệp Nhà nước (SOE) trụ cột được định hướng làm nòng cốt hạ tầng (EVN, PVN, Viettel, VNPT, MobiFone, Tân Cảng Sài Gòn, Vietcombank):
1. Tiêu chí sàng lọc 7 tập đoàn (quy mô tài sản tỷ USD, thị phần chi phối >30%, an ninh năng lượng, viễn thông, thanh khoản).
2. Cơ chế 'trợ cấp ngầm' vĩ mô của EVN và doanh nghiệp xăng dầu: Tại sao phải mua nguyên liệu giá cao trên thị trường thế giới nhưng neo giá bán thấp trong nước? Tác động giảm xóc lạm phát (CPI) và hỗ trợ chi phí sản xuất cho FDI và doanh nghiệp tư nhân.
3. Nghịch lý đa mục tiêu và gánh nặng tài chính: Tại sao không thể dùng ROE/Lợi nhuận thương mại thuần túy để đánh giá tổ chức gánh trách nhiệm an sinh vĩ mô?
4. Điểm nghẽn quản trị 'Bảo toàn vốn' và rủi ro quan liêu/trì trệ.
Trình bày đầy đủ dữ liệu định lượng, phân tích cơ chế và trích dẫn nguồn."""
    },
    {
        "file": "03_viettel_nha_may_chip_32nm_hoa_lac.md",
        "title": "Viettel & Nhà Máy Chế Tạo Chip Bán Dẫn 27ha Hòa Lạc",
        "query": """Báo cáo chi tiết và toàn diện về dự án nhà máy chế tạo chip bán dẫn đầu tiên của Việt Nam do Viettel khởi công tại Khu Công nghệ cao Hòa Lạc (ngày 16/01/2026):
1. Quy mô diện tích (27 ha), phân kỳ đầu tư (2026-2027 xây dựng & nhận chuyển giao, 2028-2030 tối ưu hóa dây chuyền).
2. Tiến trình công nghệ (32nm / tiến trình công nghiệp): Tại sao 32nm là bước đi thực tế và chiến lược (phục vụ chip viễn thông, IoT, radar quân sự, ô tô điện, thiết bị y tế)?
3. Mảnh ghép khép kín chuỗi giá trị bán dẫn: Việt Nam đã làm chủ 5/6 công đoạn, khâu chế tạo (fabrication) mang ý nghĩa tự chủ an ninh công nghệ thế nào?
4. Vai trò như một hạ tầng công nghệ quốc gia cho các doanh nghiệp Việt Nam đặt gia công chip.
Trình bày chi tiết, có số liệu và trích dẫn nguồn."""
    },
    {
        "file": "04_sieu_du_an_duong_sat_67b_hoa_phat_thaco.md",
        "title": "Đường Sắt 67 Tỷ USD: Thép Ray Hòa Phát & Toa Xe Thaco",
        "query": """Giải mã sự tham gia của các tập đoàn tư nhân vào Siêu dự án đường sắt tốc độ cao Bắc - Nam 67 tỷ USD (tốc độ 350km/h, khởi công cuối 2026):
1. Hòa Phát: Nhà máy thép ray tại Dung Quất 2 (vốn 14.000 tỷ VNĐ), công nghệ luyện thép ray cao tốc tiêu chuẩn EN 13674 của SMS group (Đức), công suất và lộ trình ra mắt 2027. Ý nghĩa giữ lại dòng ngoại tệ và tự chủ vật liệu công nghiệp nặng.
2. Thaco: Chuyển giao công nghệ chế tạo đầu máy và toa xe (rolling stock) từ Hyundai Rotem (Hàn Quốc), xây dựng tổ hợp công nghiệp đường sắt tại TP.HCM, hệ sinh thái 1.200 ha Chu Lai với 35 nhà máy vệ tinh.
3. Cơ chế kích cầu vĩ mô của Nhà nước: Mồi dẫn vốn (crowding-in) để tư nhân dấn thân vào ngành công nghiệp chế tạo có rào cản vốn lớn.
Trình bày đầy đủ dữ liệu, thông số kỹ thuật và trích dẫn nguồn."""
    },
    {
        "file": "05_vingroup_fpt_chien_luoc_tien_cong_toan_cau.md",
        "title": "Vingroup & FPT: Mũi Nhọn Tiến Công Toàn Cầu & Công Nghệ Lõi",
        "query": """Bức tranh toàn cảnh về chiến lược công nghiệp toàn cầu của Vingroup và FPT:
1. Vingroup: Chiến lược mở rộng xe điện VinFast sang Đông Nam Á (Indonesia, Philippines, Thái Lan) và Ấn Độ; hạ tầng mạng lưới trạm sạc V-Green; các siêu dự án hạ tầng như VinSpeed (đường sắt 5,6 tỷ USD Hà Nội - Quảng Ninh), Trung tâm Hội chợ Triển lãm Quốc gia Cổ Loa.
2. FPT: Chuyển dịch từ xuất khẩu phần mềm sang làm chủ công nghệ lõi AI và vi mạch bán dẫn; kế hoạch đào tạo 50.000 kỹ sư bán dẫn cho chuỗi cung ứng toàn cầu.
3. Động lực dòng tiền và tham vọng đưa thương hiệu công nghiệp Việt Nam ra thế giới thay vì chỉ dừng ở gia công.
Trình bày chi tiết số liệu, cơ chế và trích dẫn nguồn."""
    },
    {
        "file": "06_rui_ro_don_bay_no_va_too_big_to_fail.md",
        "title": "Cơ Học Đòn Bẩy, Áp Lực Đáo Hạn Nợ & Bẫy 'Quá Lớn Để Sụp Đổ'",
        "query": """Phân tích sâu sắc, khách quan về rủi ro tài chính của các đại tập đoàn sử dụng đòn bẩy cao:
1. Quy mô nợ phải trả và bức tường đáo hạn trái phiếu doanh nghiệp của các tập đoàn lớn. Chi phí lãi vay hàng chục nghìn tỷ đồng mỗi năm và áp lực thanh khoản.
2. Khái niệm 'Too Big To Fail' (Quá lớn để sụp đổ): Khi một tập đoàn phình to bằng nợ, sự cố thanh khoản có thể tạo ra hiệu ứng domino lên hệ thống ngân hàng thương mại, thị trường trái phiếu và hàng trăm doanh nghiệp vệ tinh như thế nào?
3. Bài học từ khủng hoảng 2008 của Mỹ (bơm 443 tỷ USD giải cứu) và sự khác biệt về bộ đệm tài chính của Việt Nam (GDP bình quân nhỏ, không đủ nguồn lực để cấp cứu rủi ro hệ thống).
4. Hiện tượng Policy Capture (Lũng đoạn chính sách): Sức mạnh mặc cả của các đại tập đoàn khi sử dụng hàng vạn lao động khiến nhà hoạch định chính sách bị ràng buộc.
Trình bày khách quan, có số liệu và trích dẫn nguồn."""
    },
    {
        "file": "07_hieu_ung_chen_lan_tin_dung_sme.md",
        "title": "Hiệu Ứng Chèn Lấn Tín Dụng & Số Phận 930.000 Doanh Nghiệp Nhỏ",
        "query": """Phân tích đa chiều về tác động của chiến lược Sếu Đầu Đàn đối với 930.000 doanh nghiệp vừa và nhỏ (SME) và người dân:
1. Hiệu ứng chèn lấn tín dụng (Crowding-out effect): Cơ chế dòng vốn ngân hàng chảy về nơi có tài sản thế chấp lớn nhất (các đại tập đoàn và siêu dự án), khiến room tín dụng cho SME bị thu hẹp và lãi suất cho vay khó hạ sâu.
2. Rủi ro 'Nền kinh tế kép' (Dual Economy): Tầng trên là số ít tập đoàn tinh hoa với dự án tỷ đô, tầng dưới là hàng trăm nghìn SME vật lộn với chi phí vốn cao và thiếu bảo đảm.
3. Tác động tới cá nhân người xem: Lãi suất vay mua nhà, cơ hội việc làm, sự phụ thuộc sinh kế vào chuỗi cung ứng của các tập đoàn lớn.
Trình bày khách quan, đa chiều và có trích dẫn nguồn."""
    },
    {
        "file": "08_bay_ky_sinh_dia_to_vs_san_xuat_cong_nghiep.md",
        "title": "Bẫy Ký Sinh Địa Tô vs Canh Bạc Công Nghiệp Hóa",
        "query": """Phân tích mâu thuẫn giữa lợi nhuận đầu cơ bất động sản và sự phát triển công nghiệp công nghệ cao:
1. Sự chênh lệch biên lợi nhuận và chu kỳ hoàn vốn: Bất động sản mang lại siêu lợi nhuận ngắn hạn nhờ chênh lệch địa tô, trong khi công nghệ và chế tạo đòi hỏi đốt vốn 5-10 năm ròng rã.
2. Rủi ro của mô hình 'Lấy bất động sản nuôi công nghiệp': Khi thị trường bất động sản đóng băng, dòng tiền nuôi dưỡng các nhà máy sản xuất và R&D bị ngắt đột ngột.
3. Rào cản hành chính thể chế: Thủ tục đất đai, phê duyệt dự án kéo dài làm chôn vốn của doanh nghiệp sản xuất thực thụ.
Trình bày sắc bén, có số liệu và trích dẫn nguồn."""
    },
    {
        "file": "09_doi_sanh_quoc_te_chaebol_sasac_temasek.md",
        "title": "Bài Học Quốc Tế: Chaebol Hàn Quốc, SASAC Trung Quốc & Temasek Singapore",
        "query": """So sánh đối chiếu chi tiết 3 mô hình đại tập đoàn quốc tế để rút ra bài học cho Việt Nam:
1. Hàn Quốc: Kỳ tích Sông Hàn dưới thời Park Chung-hee bằng chính sách tín dụng chỉ định xuất khẩu; Mặt tối: Sở hữu chéo, nợ khổng lồ, lũng đoạn chính trị và sự sụp đổ dây chuyền trong khủng hoảng tài chính châu Á 1997.
2. Trung Quốc: Cải cách 'Nắm lớn buông nhỏ' của Chu Dung Cơ (1998), cho hàng vạn SOE yếu kém phá sản để dồn lực nuôi các siêu tập đoàn trung ương (SASAC quản lý 97 tập đoàn), áp dụng sở hữu hỗn hợp.
3. Singapore: Mô hình Temasek Holdings - phân tách tuyệt đối giữa quyền sở hữu của Nhà nước và quyền điều hành của chuyên gia thị trường, duy trì kỷ luật tỷ suất sinh lời thương mại 14-15%/năm.
4. Bài học thể chế cho Việt Nam: Không thể sao chép máy móc mà cần kết hợp kỷ luật thị trường và bảo vệ an ninh kinh tế.
Trình bày sâu sắc, có số liệu lịch sử và trích dẫn nguồn."""
    },
    {
        "file": "10_co_che_cong_sinh_va_ban_hop_dong_2045.md",
        "title": "Cơ Chế Cộng Sinh Lan Tỏa & Bản Hợp Đồng Thể Chế 2026–2045",
        "query": """Phân tích cơ chế cộng sinh (Spillover Effect) và bản hợp đồng phát triển mới giữa Nhà nước - Doanh nghiệp - Xã hội đến năm 2045:
1. Mỏ neo đơn hàng và chuyển giao công nghệ thực tế: Case study VinFast hợp tác 700 nhà cung cấp nội địa (mục tiêu 84% nội địa hóa); Thaco Chu Lai chia sẻ 150 bộ linh kiện toa xe; PTSC kéo gần 100 thầu phụ chân đế điện gió ngoài khơi xuất khẩu.
2. Bản hợp đồng thể chế Nghị quyết 79: Nguyên tắc 'Không bảo hộ, không độc quyền', Nhà nước lùi lại làm bệ phóng hạ tầng và dọn rào cản hành chính, để doanh nghiệp tự bơi bằng năng lực cạnh tranh quốc tế.
3. Framework đánh giá cho người dân và doanh nghiệp SME: Làm sao để định vị bản thân và tham gia vào chuỗi giá trị trong kỷ nguyên đại tập đoàn?
Trình bày tổng hợp, thực tế và trích dẫn nguồn."""
    }
]

def run_extraction():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    print(f"Bắt đầu trích xuất 10 chủ đề từ Master Notebook {NOTEBOOK_ID}...")
    
    for idx, q in enumerate(QUESTIONS, 1):
        target_path = os.path.join(VAULT_DIR, q["file"])
        print(f"\n[{idx}/10] Đang trích xuất: {q['title']}...")
        
        cmd = [
            CLI_PATH,
            "ask",
            q["query"],
            "-n", NOTEBOOK_ID,
            "--json"
        ]
        
        try:
            res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=300)
            if res.returncode == 0:
                try:
                    data = json.loads(res.stdout)
                    content = data.get("answer", res.stdout)
                except Exception:
                    content = res.stdout
                
                # Ghi vào file vault
                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(f"# {q['title']}\n\n")
                    f.write(f"> **Tệp nguồn trích xuất từ Master Notebook:** `{NOTEBOOK_ID}`\n")
                    f.write(f"> **Thời gian trích xuất:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n")
                    f.write(content)
                    f.write("\n")
                print(f" -> Đã lưu: {target_path}")
            else:
                print(f" -> Lỗi khi chạy query {idx}: {res.stderr}")
        except Exception as e:
            print(f" -> Ngoại lệ: {e}")
        
        time.sleep(2)

if __name__ == "__main__":
    run_extraction()
