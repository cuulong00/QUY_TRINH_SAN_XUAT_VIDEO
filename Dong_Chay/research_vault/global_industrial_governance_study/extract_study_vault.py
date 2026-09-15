import os
import sys
import json
import subprocess
from pathlib import Path

NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
NOTEBOOK_ID = "c586d12e-218f-4032-8944-80fe253afd1c"
VAULT_DIR = Path("/Users/pro16/Documents/VideoProject/Dong_Chay/research_vault/global_industrial_governance_study/vault")

QUERIES = [
    {
        "filename": "01_state_led_failures.md",
        "title": "Giải Phẫu Các Thảm Họa Đại Dự Án Do Nhà Nước Dẫn Dắt",
        "prompt": """Phân tích chuyên sâu và toàn diện về cơ chế sụp đổ của các đại dự án công nghiệp/công nghệ do nhà nước dẫn dắt:
1. British Leyland (Anh Quốc): Quá trình quốc hữu hóa 1975, quy mô vốn cứu trợ (£11 tỷ+), cơ chế quản trị ủy ban, ảnh hưởng của nghiệp đoàn đình công, các mẫu xe lỗi (Austin Allegro, Morris Marina) và sự xóa sổ quyền tự chủ ngành ô tô Anh.
2. Máy bay siêu thanh Concorde (Anh - Pháp): Chi phí phát triển ngân sách, nguyên nhân thương mại thất bại, nguồn gốc kinh tế học của 'Concorde Fallacy' (Bẫy chi phí chìm).
3. Plan Calcul & Máy tính Bull (Pháp): Giấc mơ của De Gaulle, chính sách mua sắm công ép buộc, tại sao thua IBM và Thung lũng Silicon.
4. Xe Trabant & Wartburg (Đông Đức): Cơ chế kinh tế kế hoạch hóa, 30 năm không đổi mẫu, sự sụp đổ khi mở cửa bức tường Berlin.
5. Proton (Malaysia) & Dự án máy tính thế hệ 5 FGCS (Nhật Bản MITI): Bẫy bảo hộ thuế quan, sự thất bại trong việc bắt kịp thị trường mở.
Nêu rõ các số liệu định lượng cụ thể, cơ chế kinh tế thể chế (Soft Budget Constraint, OPM) và trích dẫn nguồn."""
    },
    {
        "filename": "02_state_led_successes.md",
        "title": "Giải Mã Các Kỳ Tích Công Nghiệp Do Nhà Nước Kiến Tạo",
        "prompt": """Phân tích chi tiết và sâu sắc các đại dự án công nghiệp/công nghệ do nhà nước khởi xướng hoặc dẫn dắt nhưng ĐẠT THÀNH CÔNG RỰC RỠ:
1. TSMC & Viện ITRI (Đài Loan): Vai trò 48% vốn nhà nước ban đầu, K.T. Li, Sun Yun-suan, việc chiêu mộ Morris Chang (Trương Trung Mưu), mô hình Pure-play Foundry, tại sao TSMC không cần bảo hộ thuế quan mà cạnh tranh toàn cầu ngay từ đầu.
2. Airbus (Châu Âu): Liên minh 4 chính phủ (Pháp, Đức, Anh, TBN) năm 1970, cơ chế launch aid, giải bài toán quy mô tối thiểu (MES) để phá vỡ thế độc quyền của Boeing/McDonnell Douglas.
3. POSCO (Hàn Quốc): Quyết định của Park Chung-hee, Tướng Park Tae-joon và kỷ luật thép, cách POSCO cung cấp thép giá rẻ chất lượng cao làm bệ đỡ cho Hyundai, đóng tàu và công nghiệp Hàn Quốc.
4. Embraer (Brazil): Từ dự án không quân nhà nước 1969 đến top 3 nhà sản xuất máy bay dân dụng thế giới (E-Jets), bước ngoặt tư nhân hóa 1994 giữ cổ phần vàng.
5. DARPA & Mô hình 'The Entrepreneurial State' (Mỹ): Nguồn gốc nhà nước tài trợ R&D cơ bản cho Internet (ARPANET), GPS, Màn hình cảm ứng, Siri, Pin Lithium-ion trước khi tư nhân thương mại hóa.
6. Hệ sinh thái Xe điện & Pin Trung Quốc: Chính sách kép (Dual-credit), trợ cấp gắn với mật độ năng lượng pin, hạ tầng sạc, và 'Hiệu ứng cá da trơn' khi mời Tesla về Thượng Hải ép BYD/CATL vươn lên.
Cung cấp đầy đủ số liệu định lượng, cơ chế vận hành thể chế và trích dẫn nguồn."""
    },
    {
        "filename": "03_private_led_successes_failures.md",
        "title": "Canh Bạc Tư Nhân: Đột Phá Khởi Nghiệp vs. Bẫy Thổi Phồng Ảo Tưởng",
        "prompt": """Phân tích đối chiếu các đại dự án công nghiệp/công nghệ do KHỐI TƯ NHÂN dẫn dắt (Cả đột phá vĩ đại lẫn thảm kịch sụp đổ):
1. Đột phá tư nhân với Skin-in-the-game:
   - Soichiro Honda: Bất chấp đạo luật kiểm soát công nghiệp Tokushinho của MITI Nhật Bản năm 1963, tự dồn vốn làm xe S500/T360.
   - Chung Ju-yung (Hyundai): Cắt đứt với Ford năm 1973, thế chấp toàn bộ công ty xây dựng Hyundai E&C làm chiếc Hyundai Pony 1975.
   - Elon Musk (Tesla & SpaceX): Đặt cược toàn bộ tài sản từ PayPal, đối mặt bờ vực phá sản 2008, cách mạng hóa xe điện và tên lửa tái sử dụng.
2. Thảm kịch tư nhân & Bẫy ảo tưởng công nghệ:
   - Better Place (Shai Agassi): Dự án đổi pin xe điện đốt 850 triệu USD của các quỹ đầu tư mạo hiểm mượn vốn tư nhân nhưng thất bại vì không đồng bộ tiêu chuẩn và thiếu quy mô.
   - Fisker Automotive (Henrik Fisker): Thất bại 2 lần (Karma và Ocean) vì ảo tưởng thiết kế, quản trị chuỗi cung ứng yếu kém và phụ thuộc gia công ngoài.
   - DeLorean Motor Company (John DeLorean): Canh bạc xe thể thao tư nhân sụp đổ vì chi phí vượt kiểm soát và khủng hoảng tài chính.
   - Theranos (Elizabeth Holmes): Bẫy thổi phồng công nghệ (Hype bubble) và quản trị thiếu minh bạch.
Rút ra sự khác biệt giữa doanh nhân chân chính (Real Builder) vs kẻ bán ảo tưởng (Hype Merchant)."""
    },
    {
        "filename": "04_comparative_governance_frameworks.md",
        "title": "Ma Trận Thể Chế Quản Trị: Khi Nào Nhà Nước Thắng, Khi Nào Tư Nhân Vượt Trội",
        "prompt": """Tổng hợp và xây dựng Bộ Khung Quản Trị So Sánh Toàn Diện (Comprehensive Industrial Governance Framework) giữa 3 mô hình:
1. Ma trận 4 Biến Số Sinh Tử:
   - Nguồn vốn & Động lực rủi ro (OPM - Other People's Money vs. Skin-in-the-game).
   - Cơ chế Tuyển chọn & Bổ nhiệm Lãnh đạo (Quan chức nhiệm kỳ vs. Tướng lĩnh/Nhà sáng lập kiệt xuất).
   - Môi trường Cạnh tranh & Kỷ luật Thị trường (Bảo hộ chiếc lồng kính vs. Sân đấu toàn cầu).
   - Định nghĩa Vai trò Nhà nước (Nhà nước Kiến tạo Bệ phóng/R&D Cơ bản vs. Nhà nước Làm thay Thị trường/Bảo hộ tiêu cực).
2. Khi nào một quốc gia NÊN và KHÔNG NÊN dùng nguồn lực nhà nước can thiệp vào công nghiệp?
3. Bài học đắt giá cho các nước đang phát triển (Việt Nam, Đông Nam Á) khi xây dựng các ngành công nghiệp chiến lược (Bán dẫn, Xe điện, AI, Năng lượng tái tạo)."""
    }
]

def run_extraction():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME

    print(f"=== Bắt đầu trích xuất chuyên đề từ Notebook: {NOTEBOOK_ID} ===")

    for idx, item in enumerate(QUERIES, start=1):
        filename = item["filename"]
        title = item["title"]
        prompt_text = item["prompt"]
        target_path = VAULT_DIR / filename

        print(f"\n[{idx}/{len(QUERIES)}] Đang trích xuất: {title} -> {filename}...")
        
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

                md_content = f"# {title}\n\n"
                md_content += f"> **Extraction Query ID:** {filename}\n"
                md_content += f"> **Master Notebook ID:** `{NOTEBOOK_ID}`\n\n"
                md_content += f"---\n\n"
                md_content += content + "\n"

                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(md_content)
                print(f"  -> THÀNH CÔNG: Đã ghi {len(md_content)} ký tự vào {target_path}")
            else:
                print(f"  -> LỖI (code {result.returncode}): {result.stderr}")
        except Exception as e:
            print(f"  -> EXCEPTION: {e}")

if __name__ == "__main__":
    run_extraction()
