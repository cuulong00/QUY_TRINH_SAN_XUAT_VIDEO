#!/usr/bin/env python3
"""
Dedicated Deep Research & Extraction Pipeline for Episode: Tesla Motors Việt Nam.
Workspace: /Users/pro16/Documents/VideoProject/GocNhinPodcast
Account: duongtt84@gmail.com
Enforces `--mode deep --import-all` and extracts verified data anchors into research_vault.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

WORKSPACE_ROOT = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast")
NOTEBOOKLM_HOME = WORKSPACE_ROOT / ".notebooklm_home"
CLI_PATH = WORKSPACE_ROOT / ".venv_notebooklm" / "bin" / "notebooklm"

EPISODE_SLUG = "tesla-vao-viet-nam"
EPISODE_DIR = WORKSPACE_ROOT / "episodes" / EPISODE_SLUG
VAULT_DIR = EPISODE_DIR / "research_vault"
SOURCES_DIR = EPISODE_DIR / "sources"
SCRATCH_DIR = WORKSPACE_ROOT / "scratch"

os.environ["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
os.environ["PYTHONUNBUFFERED"] = "1"

EPISODE_DIR.mkdir(parents=True, exist_ok=True)
VAULT_DIR.mkdir(parents=True, exist_ok=True)
SOURCES_DIR.mkdir(parents=True, exist_ok=True)
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)


def run_cmd(args, capture=True):
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
    cmd = [str(CLI_PATH)] + args
    res = subprocess.run(cmd, env=env, capture_output=capture, text=True)
    if res.returncode != 0:
        err_msg = res.stderr or res.stdout
        raise RuntimeError(f"CLI error (code {res.returncode}): {err_msg}")
    return res.stdout


def get_or_create_master_notebook(title: str) -> str:
    id_file = EPISODE_DIR / ".notebook_id"
    if id_file.exists():
        nb_id = id_file.read_text().strip()
        if nb_id:
            print(f"📖 Sử dụng Master Notebook đã lưu: {nb_id}")
            return nb_id

    print(f"🆕 Đang tạo Master Notebook mới: '{title}'...")
    out = run_cmd(["create", title, "--json"])
    data = json.loads(out)
    nb_id = data["notebook"]["id"]

    id_file.write_text(nb_id)
    url_file = EPISODE_DIR / ".notebook_url"
    url_file.write_text(f"https://notebooklm.google.com/notebook/{nb_id}")
    print(f"✓ Đã tạo và lưu Master Notebook ID: {nb_id}")
    return nb_id


def add_text_source(nb_id: str, title: str, text_content: str):
    print(f"📄 Đang nạp tài liệu văn bản mỏ neo: '{title}'...")
    temp_file = SCRATCH_DIR / "temp_source.txt"
    temp_file.write_text(text_content, encoding="utf-8")
    try:
        out = run_cmd(["source", "add-file", str(temp_file), "-n", nb_id, "-t", title, "--json"])
        print(f"✓ Đã nạp thành công nguồn: {title}")
    except Exception as e:
        print(f"⚠️ Cảnh báo khi nạp nguồn '{title}': {e}")


def execute_deep_research(nb_id: str, prompt_text: str, query_label: str, timeout: int = 1800):
    print(f"\n🔍 [DEEP RESEARCH] Kích hoạt chế độ nghiên cứu sâu: '{query_label}' (--mode deep)...")
    temp_prompt = SCRATCH_DIR / "deep_research_prompt.txt"
    temp_prompt.write_text(prompt_text, encoding="utf-8")

    start_time = time.time()
    try:
        out = run_cmd([
            "source", "add-research",
            "--prompt-file", str(temp_prompt),
            "-n", nb_id,
            "--mode", "deep",
            "--import-all",
            "--timeout", str(timeout),
            "--json"
        ])
        elapsed = time.time() - start_time
        data = json.loads(out)
        imported = data.get("imported", 0)
        print(f"✓ Đã hoàn tất Deep Research '{query_label}' trong {elapsed:.1f}s. Nạp thêm {imported} nguồn.")
    except Exception as e:
        print(f"⚠️ Lỗi trong quá trình Deep Research '{query_label}': {e}")


def batch_extract_rag(nb_id: str, queries: list):
    print(f"\n📦 BẮT ĐẦU BATCH EXTRACTION ({len(queries)} chuyên đề) RA VAULT...")
    for idx, item in enumerate(queries, 1):
        filename = item["filename"]
        title = item["title"]
        question = item["question"]
        target_file = VAULT_DIR / filename

        print(f"\n[{idx}/{len(queries)}] Đang trích xuất RAG: {title} -> {filename}...")
        temp_q = SCRATCH_DIR / f"q_{idx}.txt"
        temp_q.write_text(question, encoding="utf-8")

        try:
            out = run_cmd([
                "ask",
                "--prompt-file", str(temp_q),
                "-n", nb_id,
                "--save-as-note",
                "-t", title,
                "--json"
            ])
            data = json.loads(out)
            answer = data.get("answer", "")
            references = data.get("references", [])

            md_content = f"# {title}\n\n"
            md_content += f"> **Chuyên đề nghiên cứu:** {title}\n"
            md_content += f"> **Câu hỏi trích xuất chuyên sâu:** {question}\n\n"
            md_content += f"## 1. Nội dung Phân tích & Dữ liệu Thực chứng (Synthesized Analysis & Data Anchors)\n\n{answer}\n\n"

            if references:
                md_content += "## 2. Mỏ neo Trích dẫn Nguồn gốc (Citations & Direct Quotes)\n\n"
                for ref in references:
                    cit_no = ref.get("citation_number")
                    cited_text = ref.get("cited_text", "").strip()
                    md_content += f"- **Mỏ neo [{cit_no}]**: *\"{cited_text}\"*\n"

            target_file.write_text(md_content, encoding="utf-8")
            print(f"✓ Đã trích xuất và lưu thành công {len(md_content.splitlines())} dòng vào {filename}")

        except Exception as e:
            print(f"✗ Lỗi khi trích xuất câu {idx}: {e}")


def main():
    topic_title = "[GÓC NHÌN PODCAST] Tesla Motors Việt Nam - Giải Phẫu Thể Chế, Thuế Quan & Trận Địa Xe Điện"
    print(f"=== BẮT ĐẦU QUY TRÌNH DEEP RESEARCH NOTEBOOKLM ===")
    nb_id = get_or_create_master_notebook(topic_title)

    # 1. Nạp tài liệu mỏ neo nền tảng (Foundational Ground-truth Source)
    foundational_doc = """
HỒ SƠ MỎ NEO THỰC CHỨNG ĐỀ TÀI: TESLA MOTORS VIỆT NAM (11/09/2026)
1. Pháp nhân:
- Tên công ty: Công ty TNHH Tesla Motors Việt Nam (Tesla Motors Vietnam Limited Liability Company).
- Ngày thành lập: 11/09/2026.
- Vốn điều lệ: 77,667 tỷ đồng (~3,05 triệu USD).
- Trụ sở: Tầng 6, Mê Linh Point Tower, số 2 Ngô Đức Kế, Quận 1, TP. Hồ Chí Minh.
- Người đại diện theo pháp luật:
  * David Jon Feinstein (Sinh 1978, Mỹ) - Chủ tịch, Senior Director of Global Trade & New Markets tại Tesla.
  * Isabel Ching Fan (Sinh 1965, Mỹ) - Tổng Giám đốc, Regional Director phụ trách Đông Nam Á, HK, Macau tại Tesla (cựu Apple 19 năm).
  * Nguyễn Mạnh Hùng (Sinh 1983, Việt Nam) - Trợ lý Tổng Giám đốc.
- Ngành nghề: Bán buôn, bán lẻ ô tô, phụ tùng ô tô, xuất nhập khẩu và phân phối hàng hóa.

2. Căn cứ Pháp lý & Thuế quan:
- Thuế Tiêu thụ đặc biệt (TTĐB): Luật số 03/2022/QH15 quy định thuế suất TTĐB cho xe điện chạy pin (dưới 9 chỗ) là 3% từ 01/03/2022 đến 28/02/2027. Từ 01/03/2027 tăng lên 11%.
- Lệ phí trước bạ: Nghị định 10/2022/NĐ-CP: Từ 01/03/2025 đến 28/02/2027 áp dụng mức thu 50% so với xe xăng thông thường.
- Thuế nhập khẩu CBU: Nghị định 26/2023/NĐ-CP: Xe ô tô điện nguyên chiếc (HS 8703.80) từ Trung Quốc/Mỹ không nằm trong danh mục ưu đãi giảm về 0% của ACFTA/RCEP, chịu thuế suất tối huệ quốc MFN 45% - 70%.

3. Bàn cờ Cạnh tranh & Hạ tầng:
- VinFast & V-GREEN: Sở hữu hơn 150.000 cổng sạc trên 63 tỉnh thành, kiên quyết đóng kín trạm sạc không chia sẻ với bên thứ ba.
- Trạm Supercharger của Tesla: Chi phí xây dựng chuẩn V3/V4 (4-8 cọc sạc 250kW) tốn từ 150.000 - 250.000 USD (chưa tính trạm biến áp và mặt bằng).
- Trạm sạc độc lập bên thứ ba (EV ONE, Charge+, EverCharge): Quy mô nhỏ lẻ, công suất thấp.
- Chuỗi cung ứng tại Việt Nam: Foxconn (Quảng Ninh sản xuất sạc/linh kiện), Pegatron (Hải Phòng), Compal...
- SpaceX Starlink: Đề xuất dự án 1,5 tỷ USD Internet vệ tinh tại Việt Nam.
"""
    add_text_source(nb_id, "Ho So Mo Neo Thuc Chung: Tesla Motors Viet Nam 2026", foundational_doc)

    # 2. Thực thi 5 Truy vấn Nạp nguồn Deep Research (--mode deep)
    ingestion_queries = [
        {
            "label": "Trụ Cột 1: Pháp nhân & Dàn Lãnh đạo Feinstein - Fan",
            "prompt": '"Tesla Motors Vietnam Limited Liability Company" OR "Công ty TNHH Tesla Motors Việt Nam" "David Jon Feinstein" "Isabel Ching Fan" "Nguyễn Mạnh Hùng" "Mê Linh Point" registration date September 2026 charter capital 77.667 billion VND "Senior Director of Global Trade and New Markets" Tesla expansion Thailand Malaysia India'
        },
        {
            "label": "Trụ Cột 2: Thuế Nhập Khẩu CBU, TTĐB 3% & Bóc Tách Giá",
            "prompt": '"thuế nhập khẩu ô tô điện" CBU "8703.80" Nghị định 26/2023/NĐ-CP ACFTA RCEP biểu thuế ô tô nguyên chiếc từ Trung Quốc về Việt Nam Luật số 03/2022/QH15 thuế tiêu thụ đặc biệt xe điện 3% Nghị định 10/2022/NĐ-CP lệ phí trước bạ xe điện 2025 2026 2027 Tesla Model 3 Giga Shanghai price Malaysia BEV Global Leaders tax exemption Thailand EV incentive bilateral agreement'
        },
        {
            "label": "Trụ Cột 3: Chiến Địa Trạm Sạc: V-GREEN vs. Supercharger",
            "prompt": 'VinFast V-GREEN 150000 trạm sạc chính sách chia sẻ trạm sạc bên thứ ba trạm sạc độc quyền Vingroup chi phí xây dựng trạm Tesla Supercharger V3 V4 250kW cost per station grid interconnection transformer trạm sạc xe điện độc lập Việt Nam EV ONE Charge+ EverCharge Porsche charging network Vietnam'
        },
        {
            "label": "Trụ Cột 4: Tesla Vision FSD V12 & Thể Chế Xe Tự Hành",
            "prompt": 'Tesla Full Self Driving FSD V12 neural network vision-only autonomous driving performance in heavy traffic motorcycles phantom braking Luật Trật tự an toàn giao thông đường bộ 2024 quy định xe tự lái cấp độ 3 trách nhiệm pháp lý tai nạn xe tự hành Việt Nam thị phần xe điện Việt Nam 2025 2026 BYD Geely VinFast VF8 VF9 BMW i4 Mercedes EQE'
        },
        {
            "label": "Trụ Cột 5: Chuỗi Cung Ứng Linh Kiện VN & Đòn Bẩy Starlink 1.5 tỷ USD",
            "prompt": 'Tesla suppliers Vietnam Foxconn Quang Ninh EV charger Pegatron Hai Phong electronics Compal Vinh Phuc SpaceX Starlink investment 1.5 billion USD Vietnam Prime Minister Pham Minh Chinh meetings Elon Musk US Vietnam Comprehensive Strategic Partnership semiconductor supply chain'
        }
    ]

    for q in ingestion_queries:
        execute_deep_research(nb_id, q["prompt"], q["label"])

    # 3. Thực thi 5 Truy vấn Bóc tách RAG Chuyên sâu vào research_vault
    extraction_queries = [
        {
            "filename": "001_phap_nhan_tesla_va_lanh_dao.md",
            "title": "Hồ Sơ Pháp Lý Tesla Motors Việt Nam, Nhân Sự Chủ Chốt Và Tiền Lệ ASEAN",
            "question": """Dựa trên toàn bộ các tài liệu đã nạp, hãy bóc tách và kiểm toán chi tiết các nội dung sau:
1. Thông tin pháp lý chính xác của Công ty TNHH Tesla Motors Việt Nam: Ngày cấp phép, mã số doanh nghiệp, vốn điều lệ (bằng VNĐ và quy đổi USD), địa chỉ trụ sở, danh mục các ngành nghề kinh doanh đăng ký.
2. Hồ sơ nhân sự của 3 người đại diện pháp luật:
   - David Jon Feinstein: Chức danh hiện tại tại Tesla toàn cầu, năm gia nhập, kinh nghiệm thực chiến trong việc mở rộng thị trường tại Canada, Ấn Độ, Thái Lan và Malaysia.
   - Isabel Ching Fan: Chức vụ, phạm vi quản lý khu vực, kinh nghiệm trước đó tại Apple.
   - Nguyễn Mạnh Hùng: Vai trò đại diện sở tại.
3. So sánh tiền lệ: Khảo sát lộ trình của Tesla tại Thái Lan (cuối 2022) và Malaysia (2023) từ thời điểm thành lập pháp nhân đến lúc mở cổng nhận đặt hàng trực tuyến, khai trương Showroom đầu tiên và bàn giao xe. Khung thời gian trung bình là bao nhiêu tháng?
4. Đánh giá tính chất mô hình: Tại sao mức vốn ~3 triệu USD khẳng định đây là mô hình Asset-Light thuần túy thương mại, không phải cam kết đầu tư sản xuất?"""
        },
        {
            "filename": "002_thue_quan_va_phuong_trinh_gia_cbu.md",
            "title": "Hàng Rào Thuế Quan CBU, Luật Thuế TTĐB 3% Và Phương Trình Định Giá Lăn Bánh",
            "question": """Dựa trên các văn bản quy phạm pháp luật và biểu thuế quan đã nạp, hãy tính toán và phân tích:
1. Xác định chính xác mã HS và mức thuế nhập khẩu nguyên chiếc (CBU) áp dụng cho xe điện chở người dưới 9 chỗ (nhóm 8703.80) nhập khẩu từ:
   - Trung Quốc (nhà máy Giga Shanghai): Kiểm tra rõ xe CBU có nằm trong danh mục loại trừ của ACFTA/RCEP không? Mức thuế MFN áp dụng là bao nhiêu %?
   - Mỹ (nhà máy Fremont/Texas): Mức thuế MFN áp dụng là bao nhiêu %?
2. Chi tiết chính sách thuế nội địa:
   - Thuế Tiêu thụ đặc biệt (TTĐB): Tỷ lệ 3% theo Luật số 03/2022/QH15 áp dụng đến mốc thời gian nào? Sau đó tăng lên bao nhiêu %?
   - Thuế Giá trị gia tăng (VAT): 10% tính lũy kế trên những cấu phần nào?
   - Lệ phí trước bạ: Mức thu hiện hành cho xe điện chạy pin (áp dụng từ 01/03/2025 đến 28/02/2027) là bao nhiêu %?
3. Thiết lập bảng tính giá lăn bánh chi tiết cho 2 dòng xe chủ lực:
   - Tesla Model 3 RWD (giá CIF xuất xưởng Giga Shanghai ước tính 28.000 - 30.000 USD).
   - Tesla Model Y RWD (giá CIF xuất xưởng Giga Shanghai ước tính 34.000 - 36.000 USD).
   - Tính toán đầy đủ: Thuế NK + Thuế TTĐB + VAT + Chi phí vận chuyển/showroom/lợi nhuận đại lý (ước tính 15-20%) + Lệ phí trước bạ + Biển số.
4. Đối sánh chính sách: Chỉ rõ tại sao giá xe Tesla tại Thái Lan và Malaysia lại rẻ hơn đáng kể so với phương trình tại Việt Nam (phân tích hiệp định song phương Thái - Trung và gói ưu đãi BEV Global Leaders của Malaysia)."""
        },
        {
            "filename": "003_ha_tang_sac_vgreen_vs_supercharger.md",
            "title": "Chiến Địa Bất Đối Xứng Hạ Tầng: V-GREEN Độc Quyền vs. Capex Supercharger",
            "question": """Trích xuất và phân tích toàn diện cuộc chiến hạ tầng trạm sạc tại Việt Nam:
1. Dữ liệu thực chứng về mạng lưới trạm sạc V-GREEN (VinFast):
   - Số lượng cổng sạc quy hoạch và thực tế vận hành trên toàn quốc.
   - Độ phủ trên 63 tỉnh thành, hệ thống quốc lộ, cao tốc, khu đô thị Vinhomes và trung tâm thương mại Vincom.
   - Tuyên bố chiến lược và lập trường chính thức của V-GREEN/Vingroup về việc chia sẻ cổng sạc cho các hãng xe đối thủ.
2. Bài toán Unit Economics của một trạm Tesla Supercharger chuẩn V3/V4 (4 đến 8 cọc sạc công suất 250kW):
   - Chi phí phần cứng cọc sạc và tủ điều khiển (Cabinet).
   - Chi phí trạm biến áp chuyên dùng, đường dây trung thế và đấu nối điện lực.
   - Chi phí thuê mặt bằng thương mại tại các vị trí đắc địa ở Hà Nội và TP.HCM.
   - Với số vốn điều lệ 77,667 tỷ VNĐ (~3 triệu USD), Tesla có thể tự xây dựng tối đa bao nhiêu trạm sạc?
3. Khảo sát hiện trạng mạng lưới sạc độc lập bên thứ ba (Third-party CPO):
   - Quy mô, độ phủ và công suất của EV ONE, Charge+, EverCharge...
   - Những hạn chế kỹ thuật (chuẩn giao tiếp CCS2, công suất chia tải, thanh toán qua app).
4. Phân tích hành vi và rủi ro của người dùng: Trải nghiệm thực tế của chủ xe Tesla tại Việt Nam nếu chỉ sạc tại nhà (Wall Connector) và không có Supercharger đường dài."""
        },
        {
            "filename": "004_cong_nghe_fsd_va_phap_ly_giao_thong.md",
            "title": "Thách Thức Công Nghệ FSD V12 Trước Giao Thông Bản Địa & Rào Cản Thể Chế",
            "question": """Bóc tách các giới hạn kỹ thuật và rào cản pháp lý của công nghệ tự lái Tesla:
1. Nguyên lý công nghệ Tesla Vision (FSD V12):
   - Cơ chế xử lý End-to-End Neural Networks dựa thuần túy vào camera quang học, loại bỏ hoàn toàn radar và LiDAR.
   - Những điểm mù vật lý và giới hạn xử lý khi gặp thời tiết mưa bão nhiệt đới, bụi mịn, ánh sáng đèn pha ngược chiều.
2. Va chạm thực tế với mô hình giao thông "Dòng chảy hỗn loạn có tổ chức" tại Hà Nội và TP.HCM:
   - Mật độ xe máy dày đặc (khoảng cách tạt đầu dưới 0,5m).
   - Hiện tượng lấn làn, đi ngược chiều, vượt đèn vàng, biển báo bị che khuất.
   - Nguy cơ xảy ra hiện tượng phanh giật ảo (Phantom Braking) và ngắt kết nối hệ thống khi mạng nơ-ron bị quá tải điểm ảnh.
3. Rà soát khung pháp lý Việt Nam:
   - Luật Trật tự, an toàn giao thông đường bộ 2024 và các quy chuẩn đăng kiểm hiện hành: Có công nhận xe tự lái cấp độ 3 (Level 3 - Conditional Automation) trở lên hay không?
   - Khoảng trống pháp lý: Trong trường hợp xe bật chế độ tự lái gây tai nạn giao thông, trách nhiệm hình sự và bồi thường dân sự thuộc về ai?
4. Định vị cạnh tranh: Khi tính năng FSD bị hạn chế/vô hiệu hóa, giá trị cốt lõi của Tesla bị suy giảm ra sao trước các đối thủ xe sang Đức và xe điện Trung Quốc trang bị LiDAR?"""
        },
        {
            "filename": "005_chuoi_cung_ung_viet_nam_va_starlink.md",
            "title": "Bàn Cờ Đôi: Chuỗi Cung Ứng Phần Cứng Tại Việt Nam & Dự Án 1.5 Tỷ USD Starlink",
            "question": """Phân tích bức tranh liên hoàn giữa Tesla, chuỗi cung ứng phần cứng tại Việt Nam và đại dự án SpaceX Starlink:
1. Mạng lưới cung ứng của Tesla tại Việt Nam:
   - Danh sách các nhà máy Tier-1/Tier-2 đang sản xuất linh kiện cho Tesla: Pegatron (KCN Deep C Hải Phòng), Foxconn (Quảng Ninh), Compal (Vĩnh Phúc)...
   - Các dòng linh kiện cụ thể: Bo mạch điều khiển, bộ sạc xe điện, linh kiện cơ khí chính xác, dây dẫn điện.
   - Tỷ trọng và vai trò của các nhà máy này trong chuỗi cung ứng toàn cầu của Tesla.
2. Đại dự án Internet vệ tinh Starlink của SpaceX:
   - Tiến trình tiếp xúc cấp cao giữa Lãnh đạo Chính phủ Việt Nam và lãnh đạo SpaceX trong các năm 2023 - 2026.
   - Quy mô vốn đề xuất 1,5 tỷ USD và các vướng mắc về an ninh mạng, tỷ lệ sở hữu nước ngoài trong lĩnh vực viễn thông và việc đặt trạm Gateway mặt đất.
3. Mối liên kết địa chính trị & Chiến lược thương hiệu:
   - Việc Tesla thành lập pháp nhân bán lẻ đóng vai trò gì trong việc xây dựng uy tín pháp lý của hệ sinh thái Musk tại Việt Nam?
   - Tác động qua lại giữa cam kết đầu tư công nghệ cao và đàm phán chính sách trong khuôn khổ quan hệ Đối tác Chiến lược Toàn diện Việt - Mỹ."""
        }
    ]

    batch_extract_rag(nb_id, extraction_queries)
    print("\n🎉 HOÀN TẤT TOÀN BỘ QUY TRÌNH DEEP RESEARCH & BATCH EXTRACTION!")


if __name__ == "__main__":
    main()
