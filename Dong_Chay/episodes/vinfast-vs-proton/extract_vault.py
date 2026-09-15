import os
import sys
import json
import subprocess
from pathlib import Path

NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
NOTEBOOK_ID = "375a51fe-e26a-41e2-bc2b-72b9d694269d"
VAULT_DIR = Path("/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/vinfast-vs-proton/research_vault")

QUERIES = [
    {
        "filename": "01_proton_birth_protectionism.md",
        "title": "Proton: Nguồn Gốc, Tầm Nhìn Mahathir Và Hàng Rào Bảo Hộ",
        "prompt": """Phân tích chuyên sâu và toàn diện về lịch sử thành lập Proton (1983) tại Malaysia:
1. Tầm nhìn của Thủ tướng Mahathir Mohamad và vai trò của HICOM (Heavy Industries Corporation of Malaysia) trong chiến lược 'Look East' và công nghiệp hóa nặng.
2. Bản chất liên doanh ban đầu với Mitsubishi Motors (nền tảng Mitsubishi Lancer Fiore của Proton Saga 1985).
3. Hệ thống chính sách bảo hộ: Biểu thuế nhập khẩu ô tô nguyên chiếc (CBU) lên tới 100%-300%, ưu đãi thuế tiêu thụ đặc biệt, hệ thống giấy phép AP (Approved Permits), và chính sách độc quyền mua sắm công của chính phủ.
4. Đỉnh cao thị phần nội địa: Con số 74% năm 1993, sản lượng sản xuất và tác động đến ngành công nghiệp phụ trợ Malaysia.
Yêu cầu: Nêu rõ các mốc thời gian, số liệu định lượng, chính sách và cơ chế kinh tế. Trích dẫn nguồn tài liệu."""
    },
    {
        "filename": "02_proton_lotus_tech_trap.md",
        "title": "Proton & Cái Bẫy Mua Lại Lotus: Khi Công Nghệ Không Giải Quyết Được Quy Mô",
        "prompt": """Phân tích chi tiết thương vụ Proton mua lại hãng siêu xe thể thao Lotus Cars (Anh Quốc) năm 1996 với giá 51 triệu bảng Anh:
1. Động cơ chiến lược của Proton khi thâu tóm Lotus (kỳ vọng về R&D, công nghệ khung gầm, hệ thống treo 'Handling by Lotus').
2. Quá trình phát triển động cơ tự chủ Campro và các mẫu xe như Proton Gen-2, Satria GTi, Waja.
3. Tại sao thương vụ Lotus lại trở thành một 'cái bẫy công nghệ'? Phân tích sự khác biệt giữa công nghệ chế tạo thủ công quy mô nhỏ của siêu xe và nền tảng (Platform) sản xuất ô tô đại trà thương mại.
4. Chi phí chìm và gánh nặng tài chính của Lotus đối với Proton.
Yêu cầu: Cung cấp số liệu tài chính, phân tích kỹ thuật cơ khí/nền tảng và cơ chế kinh tế đằng sau sự thất bại này."""
    },
    {
        "filename": "03_proton_collapse_afta_geely.md",
        "title": "Sự Sụp Đổ Của Proton, Hiệp Định AFTA Và Gói Cứu Trợ 15 Tỷ Ringgit",
        "prompt": """Phân tích chi tiết giai đoạn sụp đổ của Proton từ sau năm 2000 đến 2017:
1. Tác động của Hiệp định Thương mại Tự do ASEAN (AFTA/ATIGA) khi Malaysia buộc phải dỡ bỏ dần hàng rào thuế quan ô tô về 0-5%.
2. Sự trỗi dậy của Perodua (liên minh Daihatsu/Toyota) và các hãng xe Nhật Bản, khiến thị phần Proton rơi tự do từ 74% xuống 12.5% năm 2016.
3. Thống kê toàn diện các khoản cứu trợ, trợ cấp, tài trợ R&D và cho vay ưu đãi của Chính phủ Malaysia cho Proton (tổng cộng hơn 13.9 tỷ đến 15.15 tỷ Ringgit / ~3.5 - 4 tỷ USD).
4. Cuộc tranh cãi chính trị và quyết định tư nhân hóa (bán cho DRB-HICOM năm 2012) rồi buộc phải tìm đối tác ngoại năm 2016-2017.
Yêu cầu: Số liệu định lượng chi tiết, trích dẫn các báo cáo kiểm toán, chính phủ và diễn biến tài chính."""
    },
    {
        "filename": "04_geely_turnaround_proton.md",
        "title": "Geely Thâu Tóm 49.9% Proton: Cú Hồi Sinh Và Đánh Đổi Tự Chủ Công Nghệ",
        "prompt": """Phân tích chi tiết thương vụ Geely mua 49.9% cổ phần Proton năm 2017:
1. Cấu trúc thương vụ: Định giá, điều kiện chuyển giao công nghệ và bán Lotus cho Geely.
2. Chiến lược hồi sinh của Geely: Đưa nền tảng Geely Boyue vào lắp ráp thành Proton X70, X50, X90; tái cấu trúc chuỗi cung ứng, cải thiện chất lượng và văn hóa quản trị.
3. Kết quả tài chính và thị phần: Sự phục hồi từ đáy 12.5% lên trên 18.7% - 26% thị phần (2018-2026), có lãi trở lại.
4. Kế hoạch chuyển dịch xe điện: Thương hiệu con e.MAS (Proton e.MAS 7 trên nền tảng Geely GEA).
5. Đánh giá bản chất: Proton hồi sinh nhưng đã mất quyền tự chủ công nghệ quốc gia, trở thành cánh tay nối dài của Geely tại Đông Nam Á.
Yêu cầu: Cung cấp đầy đủ số liệu thị phần, dòng xe, nền tảng công nghệ và phân tích chiến lược."""
    },
    {
        "filename": "05_vinfast_genesis_ice_pivot.md",
        "title": "VinFast: Khởi Đầu Thần Tốc Xe Xăng Và Quyết Định Khai Tử 2022",
        "prompt": """Phân tích giai đoạn khởi đầu của VinFast từ năm 2017 đến bước ngoặt khai tử xe xăng 2022:
1. Quá trình thành lập của Vingroup / Phạm Nhật Vượng: Xây dựng tổ hợp nhà máy Hải Phòng trị giá 3.5 tỷ USD trong 21 tháng.
2. Giai đoạn xe xăng (2018-2021): Mua bản quyền nền tảng BMW 5-Series/X5, động cơ N20 (Lux A2.0, Lux SA2.0) và GM Spark (Fadil). Thành công chiếm số 1 phân khúc trong nước.
3. Rào cản kinh tế của xe xăng: Chi phí bản quyền (royalty) cao, không làm chủ được công nghệ cốt lõi động cơ đốt trong (ICE), tiêu chuẩn khí thải Euro 5/6 khắt khe, và quy mô sản xuất nhỏ (~30.000 - 40.000 xe/năm) không thể bù đắp chi phí.
4. Quyết định lịch sử đầu năm 2022: Khai tử 100% xe xăng để trở thành hãng xe thuần điện (Pure-play EV). Phân tích rủi ro tài sản chìm (stranded assets) và sự dũng cảm chiến lược.
Yêu cầu: Phân tích sâu về cấu trúc chi phí, bản quyền, cơ chế kinh tế và tầm nhìn chiến lược."""
    },
    {
        "filename": "06_vinfast_ev_mechanics_scale.md",
        "title": "Cơ Chế Xe Điện Của VinFast: Đi Tắt Đón Đầu Và Tăng Tốc Sản Lượng",
        "prompt": """Phân tích cơ chế kỹ thuật và kinh tế của chiến lược xe điện thuần túy của VinFast:
1. Tại sao chuyển sang EV là cơ hội 'san phẳng sân chơi' (Level Playing Field)? Khung gầm Skateboard, cấu trúc Cell-to-Pack, bỏ qua 100 năm tích lũy cơ khí động cơ đốt trong.
2. Dải sản phẩm xe điện hoàn chỉnh: VF 3, VF 5, VF 6, VF 7, VF 8, VF 9 và xe máy điện.
3. Thống kê tăng trưởng bàn giao xe thực tế qua các năm: 2023 (~35.000 xe), 2024 (~97.399 xe), 2025 (~196.919 xe), và mục tiêu 2026 (300.000 xe). Thị phần tại Việt Nam vươn lên top 1 (~36% năm 2025).
4. Phân tích chi phí pin (LFP, NMC), hợp tác CATL, Gotion High-Tech và nhà máy pin VinES Hà Tĩnh.
Yêu cầu: Cung cấp đầy đủ số liệu định lượng về sản lượng, thị phần, công nghệ pin và cấu trúc sản phẩm."""
    },
    {
        "filename": "07_gsm_vgreen_domestic_engine.md",
        "title": "Động Cơ Kép Nội Địa: GSM Taxi Xanh Và Hào Môn Hạ Tầng V-GREEN",
        "prompt": """Phân tích chuyên sâu về hệ sinh thái 'Động cơ kép nội địa' hỗ trợ cho VinFast:
1. Taxi Xanh GSM (Green & Smart Mobility): Cơ chế thành lập, vai trò hấp thụ sản lượng ban đầu (hàng chục nghìn xe VF e34, VF 5, VF 8), tạo dòng tiền, chứng minh độ bền sản phẩm và quảng bá trải nghiệm thực tế cho người dân. Thỏa thuận cung ứng 1 triệu ô tô và 4 triệu xe máy điện (2026-2030).
2. Mạng lưới trạm sạc V-GREEN: Chiến lược xây dựng trạm sạc phủ khắp 63 tỉnh thành, tạo thành hào môn kinh tế (Economic Moat) độc quyền mà các đối thủ như BYD, Toyota khó vượt qua tại Việt Nam.
3. Chính sách bán hàng & thuê pin: Giảm giá thành lăn bánh ban đầu, dịch chuyển rủi ro chai pin về phía nhà sản xuất.
Yêu cầu: Phân tích cơ chế kinh tế mạng lưới, hiệu ứng quy mô nội địa và các số liệu liên quan."""
    },
    {
        "filename": "08_vinfast_global_expansion_imperative.md",
        "title": "Mệnh Lệnh Vươn Ra Toàn Cầu: Bài Toán Toán Học Về Quy Mô Tối Thiểu (MES)",
        "prompt": """Phân tích mệnh lệnh sinh tồn vươn ra thị trường quốc tế của VinFast:
1. Quy luật Quy mô Tối thiểu (Minimum Efficient Scale - MES) trong ngành công nghiệp ô tô: Tại sao một hãng xe cần đạt sản lượng từ 200.000 đến 500.000 xe/năm trên mỗi nền tảng để hòa vốn khấu hao khuôn đúc, dây chuyền dập và phần mềm?
2. Giới hạn dung lượng thị trường Việt Nam (tổng thị trường chỉ ~400.000 - 500.000 xe/năm cả xe xăng và điện): Tại sao chỉ dựa vào sân nhà là bản án tử như bài học Proton?
3. Chiến lược mở rộng toàn cầu của VinFast: Niêm yết Nasdaq (VFS), xây dựng nhà máy và mạng lưới tại Mỹ, Ấn Độ (Tamil Nadu), Indonesia (Subang), Philippines.
4. Chứng minh mở rộng toàn cầu là một 'đòi hỏi toán học bắt buộc' để sống sót chứ không phải chiêu trò đánh bóng thương hiệu.
Yêu cầu: Lập luận chặt chẽ bằng kinh tế học quy mô, chi phí cố định (Fixed Cost) vs Chi phí biến đổi (Variable Cost), và số liệu thực tế."""
    },
    {
        "filename": "09_macro_economic_mechanisms_comparison.md",
        "title": "So Sánh Đối Đầu Toàn Diện: 7 Trụ Cột Vĩ Mô Giữa Proton Và VinFast",
        "prompt": """Thiết lập bảng so sánh đối đầu toàn diện giữa Proton (Malaysia) và VinFast (Việt Nam) trên 7 trụ cột chiến lược:
1. Nguồn vốn & Bản chất sở hữu: Vốn ngân sách/Quốc doanh vs Tư bản tư nhân Vingroup.
2. Cơ chế bảo hộ thị trường: Hàng rào thuế quan 300% kiểu cũ (ISI) vs Cạnh tranh mở trong kỷ nguyên WTO/EVFTA/ATIGA (thuế 0%).
3. Chiến lược công nghệ: Rebadging phụ thuộc Mitsubishi/Geely vs Tự chủ nền tảng phần mềm xe điện thuần túy.
4. Dung lượng thị trường nội địa: Malaysia (~600k-800k xe) vs Việt Nam (~400k-500k xe).
5. Động lực mở rộng toàn cầu: Ỷ lại thị trường nội địa vs Bắt buộc xuất khẩu để đạt quy mô MES.
6. Mối quan hệ với chính quyền: Doanh nghiệp con cưng bao cấp vs Doanh nghiệp tư nhân tiên phong tự chịu trách nhiệm tài chính.
7. Kết cục & Viễn cảnh dài hạn: Bán mình cho Geely vs Hành trình tự chủ đầy thách thức.
Yêu cầu: Trình bày bảng so sánh chi tiết, sắc bén, làm rõ các cơ chế kinh tế học vĩ mô."""
    },
    {
        "filename": "10_counter_thesis_systemic_risks.md",
        "title": "Phản Biện Sắc Lạnh: Rủi Ro Hệ Thống, Áp Lực Nợ Vay Và Cuộc Chiến Giá Rẻ",
        "prompt": """Phân tích toàn diện các rủi ro hệ thống, điểm yếu và luận điểm phản biện (Counter-Thesis) đối với VinFast và bài học từ Proton:
1. Áp lực nợ vay và chi phí vốn: Tổng chi phí đầu tư khổng lồ (>13 tỷ USD) của Vingroup, mức độ đòn bẩy tài chính, áp lực trả nợ trái phiếu và lỗ ròng trong giai đoạn đầu tư mở rộng.
2. Sự phụ thuộc vào hệ sinh thái nội bộ: Tỷ lệ xe VinFast bán cho GSM chiếm bao nhiêu phần trăm? Thách thức khi thị trường dịch vụ taxi bão hòa và phải bán trực tiếp cho người tiêu dùng cá nhân (B2C).
3. Cuộc chiến giá rẻ tàn khốc từ Trung Quốc: Áp lực từ BYD, Geely, Wuling với chuỗi cung ứng pin khổng lồ và giá xe siêu rẻ tại Đông Nam Á.
4. Rủi ro địa chính trị và bảo hộ mới: Thuế chống trợ cấp của Mỹ và châu Âu đối với xe điện, rào cản tiêu chuẩn kỹ thuật.
5. Bài học thực tế cho người xem và nền kinh tế: Rủi ro 'Too big to fail' và tác động lan tỏa đến hệ sinh thái Vingroup.
Yêu cầu: Phân tích khách quan, khoa học, dựa trên báo cáo tài chính SEC, không suy diễn cảm tính, cung cấp ít nhất 4 data points rủi ro định lượng."""
    }
]

def run_extraction():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME

    for idx, item in enumerate(QUERIES, start=1):
        filename = item["filename"]
        title = item["title"]
        prompt_text = item["prompt"]
        target_path = VAULT_DIR / filename

        print(f"[{idx}/{len(QUERIES)}] Extracting: {title} -> {filename}...")
        
        cmd = [
            NOTEBOOKLM_BIN,
            "ask",
            prompt_text,
            "-n", NOTEBOOK_ID,
            "--save-as-note",
            "-t", title,
            "--json"
        ]

        try:
            result = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                try:
                    data = json.loads(result.stdout)
                    content = data.get("answer", "") or data.get("content", "") or result.stdout
                except Exception:
                    content = result.stdout

                # Write markdown file
                md_content = f"# {title}\n\n"
                md_content += f"> **Extraction Query ID:** {filename}\n"
                md_content += f"> **Master Notebook ID:** `{NOTEBOOK_ID}`\n\n"
                md_content += f"---\n\n"
                md_content += content + "\n"

                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(md_content)
                print(f"  -> SUCCESS: Wrote {len(md_content)} chars to {target_path}")
            else:
                print(f"  -> ERROR (code {result.returncode}): {result.stderr}")
        except Exception as e:
            print(f"  -> EXCEPTION: {e}")

if __name__ == "__main__":
    run_extraction()
