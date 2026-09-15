#!/usr/bin/env python3
"""
Dedicated Deep Research & Extraction Pipeline for Episode: Khủng hoảng Kinh tế Thái Lan - Vết xe đổ của Nhật Bản.
Enforces `--mode deep` and extracts verified data anchors into research_vault.
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

EPISODE_SLUG = "thai-lan-no-ngap-dau-vet-xe-do-nhat-ban"
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
    print(f"📄 Đang nạp tài liệu văn bản: '{title}'...")
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
    topic_title = "[GÓC NHÌN PODCAST] Khủng hoảng Kinh tế Thái Lan - Vết xe đổ của Nhật Bản"
    print(f"=== BẮT ĐẦU QUY TRÌNH DEEP RESEARCH NOTEBOOKLM ===")
    nb_id = get_or_create_master_notebook(topic_title)

    # 1. Nạp nội dung 2 bài báo nền tảng
    article_1_text = """
Nguồn: NguoiQuanSat.vn (Tác giả: Thiên Kim, 30/08/2026)
Tiêu đề: 'Con hổ châu Á' nợ ngập đầu, đứng trước nguy cơ đi vào vết xe đổ của Nhật Bản
Tóm tắt & Số liệu cốt lõi:
- Lãi suất chính sách Thái Lan: 1%, thuộc nhóm thấp nhất thế giới, chỉ cao hơn Thụy Sĩ. Ngân hàng Trung ương Thái Lan (BoT) giữ nguyên lãi suất 3 cuộc họp liên tiếp.
- Dự báo Thái Lan sớm có lãi suất thấp hơn Nhật Bản (BoJ đã nâng lãi suất lên 1% vào tháng 6 và dự kiến tiếp tục tăng).
- Nguy cơ 'Nhật Bản hóa' (Japanification): Tăng trưởng thấp kéo dài quanh 2% và lạm phát suy yếu (từng trải qua 12 tháng liên tiếp giảm phát, tháng 7 lạm phát về 1,95%).
- Oxford Economics (Louise Loo): "Châu Á nói chung đối mặt với nguy cơ Nhật Bản hóa cao hơn phần còn lại của thế giới vì dân số đang già đi. Thái Lan chịu ảnh hưởng nặng nề hơn bởi mức nợ đã rất cao".
- Don Nakornthab (Phó Thống đốc BoT): Chính sách tiền tệ 'gần như đã chạm giới hạn' trong khả năng thúc đẩy tăng trưởng. Cần kết hợp biện pháp tài chính mục tiêu và kích thích tài khóa.
- Nhân khẩu học: Tổng tỷ suất sinh TFR chỉ 1,2 con/phụ nữ (thấp hơn mức 2,1 thay thế). Tỷ lệ trên 65 tuổi tăng gấp đôi (2000-2020) và đạt 26% vào năm 2040. Dân số dự báo giảm từ 67 triệu xuống 30 triệu người trong 50 năm tới.
- Burin Adulwattana: "Chúng ta sẽ già đi nhưng không giàu lên. Thái Lan đang đi theo quỹ đạo của một nền kinh tế phát triển nhưng chưa đạt được mức thu nhập thường đi kèm với quá trình đó".
- Nợ hộ gia đình: Đạt 86% - 90% GDP (theo HSBC, cao nhất nhóm nước thu nhập trung bình cao). Nợ công tiến gần mức trần 70% GDP.
"""

    article_2_text = """
Nguồn: VietnamBiz (Theo Financial Times / Bloomberg, 28/08/2026)
Tiêu đề: Cú trượt dài của 'con hổ châu Á': Lãi suất thấp gần nhất thế giới vẫn không cứu nổi kinh tế Thái Lan
Tóm tắt & Số liệu cốt lõi:
- NHTW Thái Lan (BoT) giữ nguyên lãi suất 1% tại 3 cuộc họp liên tiếp (gần nhất 26/8).
- Nond Prueksiri (Siam Commercial Bank EIC): "Lãi suất thấp của Thái Lan là rắc rối mang tính cấu trúc hơn là chu kỳ. Chúng tôi không có lực đẩy đáng kể từ phía cầu. Với tình trạng xã hội đang già hóa và mức nợ cao, khó có khả năng người tiêu dùng sẽ gia tăng chi tiêu".
- Trước xung đột Trung Đông, Thái Lan giảm phát 12 tháng liên tiếp. Lạm phát tháng 7 hạ xuống 1,95%.
- Tăng trưởng quanh 2% trong nhiều năm, World Bank & IMF dự báo còn thấp hơn. Mục tiêu thu nhập cao năm 2037 xa vời.
- Miguel Chanco (Pantheon Macroeconomics): "Từ trước COVID-19, Thái Lan đã chứng kiến quy mô dân số trong độ tuổi lao động sụt giảm. Điều này báo hiệu triển vọng tăng trưởng kinh tế cơ cấu ở mức thấp từ nay về sau. Hệ quả thường thấy là lạm phát thấp và kéo theo đó là lãi suất thấp".
- Khủng hoảng sản xuất: Cạnh tranh khốc liệt từ hàng hóa giá rẻ Trung Quốc và sự vươn lên của các trung tâm sản xuất mới như Việt Nam, Indonesia. Nguy cơ thuế quan Mỹ và lực lượng lao động thu hẹp.
- Aris Dacanay (HSBC): Nợ hộ gia đình 86% GDP khiến người tiêu dùng phải vay mượn trang trải chi phí sinh hoạt khi lương và tăng trưởng chậm. Doanh nghiệp trì hoãn mở rộng đầu tư vì sức cầu nội địa yếu và không thể chuyển chi phí tăng cho người tiêu dùng.
- Oxford Economics (Louise Loo): Cơ chế truyền dẫn chính sách tiền tệ tại Thái Lan về cơ bản đã bị vô hiệu hóa. Tuy nhiên dư địa tài khóa không còn nhiều khi nợ công/GDP tiến gần mức trần 70%.
"""

    add_text_source(nb_id, "NguoiQuanSat: Con ho Chau A no ngap dau vet xe do Nhat Ban", article_1_text)
    add_text_source(nb_id, "VietnamBiz Financial Times: Cu truot dai con ho Chau A", article_2_text)

    # 2. Thực thi Deep Research (--mode deep) cho 3 trục vĩ mô
    research_prompts = [
        (
            "Thailand economy Japanification household debt liquidity trap Bank of Thailand interest rate Balance Sheet Recession Richard Koo monetary policy transmission failure GDP growth slowdown",
            "Trục 1: Bẫy thanh khoản, nợ hộ gia đình & Suy thoái bảng cân đối kế toán"
        ),
        (
            "Thailand automotive industry crisis Chinese EV BYD Great Wall Changan supply chain bankruptcy factory closures manufacturing deindustrialization aging population demographic crisis TFR birth rate",
            "Trục 2: Cú sụp đổ Detroit Đông Nam Á & Khủng hoảng nhân khẩu học"
        ),
        (
            "Thailand public debt ceiling fiscal space digital wallet 500 billion baht stimulus tourism structural decline Middle Income Trap comparison with Japan lost decades and lessons for Vietnam",
            "Trục 3: Giới hạn tài khóa, du lịch, bẫy thu nhập trung bình & Đối sánh quốc tế"
        )
    ]

    for p_text, label in research_prompts:
        execute_deep_research(nb_id, p_text, label)

    # 3. Batch extraction vào research_vault
    queries = [
        {
            "filename": "01_no_ho_gia_dinh_va_bay_thanh_khoan.md",
            "title": "Chuyên đề 01: Nợ hộ gia đình kỷ lục, Lãi suất sàn 1% và Bẫy thanh khoản tại Thái Lan",
            "question": "Phân tích chi tiết thực trạng nợ hộ gia đình tại Thái Lan (tỷ lệ % GDP, cơ cấu nợ tiêu dùng, mua nhà, mua xe, vay nợ phi chính thức). Tại sao mức lãi suất 1% của Bank of Thailand (BoT) không kích thích được vay mượn và tiêu dùng? Cơ chế truyền dẫn chính sách tiền tệ bị vô hiệu hóa ra sao? Cung cấp các số liệu và nhận định từ BoT, HSBC, Oxford Economics, SCB EIC."
        },
        {
            "filename": "02_nhat_ban_hoa_va_suy_thoai_bctc.md",
            "title": "Chuyên đề 02: Hiện tượng 'Nhật Bản hóa' (Japanification) và Lý thuyết Suy thoái Bảng cân đối Kế toán",
            "question": "So sánh hiện tượng 'Nhật Bản hóa' (Japanification) và Thập niên mất mát của Nhật Bản (1990s) với tình trạng hiện tại của Thái Lan theo khung lý thuyết Balance Sheet Recession của Richard Koo. Sự khác biệt chí mạng giữa Nhật Bản khi rơi vào khủng hoảng (nước giàu, GDP/người cao, thặng dư tài sản ròng quốc tế lớn) và Thái Lan (nước thu nhập trung bình, chưa giàu đã già, nợ công cao) là gì?"
        },
        {
            "filename": "03_nhan_khau_hoc_chua_giau_da_gia.md",
            "title": "Chuyên đề 03: Khủng hoảng Nhân khẩu học — Bẫy 'Chưa giàu đã già' (Aging Before Getting Rich)",
            "question": "Phân tích toàn diện cuộc khủng hoảng nhân khẩu học của Thái Lan: Tổng tỷ suất sinh TFR (1.16 - 1.20), tốc độ già hóa dân số (tỷ lệ >65 tuổi 2000-2040), dự báo suy giảm quy mô dân số (từ 67 triệu xuống 30 triệu). Tác động của việc thu hẹp lực lượng lao động đến tiềm năng tăng trưởng GDP (potential GDP), năng suất lao động và quỹ bảo trợ xã hội/y tế."
        },
        {
            "filename": "04_khung_hoang_detroit_dong_nam_a_va_xe_dien.md",
            "title": "Chuyên đề 04: Cú sụp đổ của 'Detroit Đông Nam Á' và Cuộc xâm lấn của Xe điện Trung Quốc",
            "question": "Phân tích nguyên nhân suy thoái của ngành sản xuất ô tô Thái Lan - từng được mệnh danh là 'Detroit Đông Nam Á'. Sự phụ thuộc vào các hãng xe Nhật Bản (Toyota, Isuzu, Honda), sự tràn ngập của xe điện Trung Quốc (BYD, Great Wall, Changan) và làn sóng phá sản/đóng cửa của các nhà sản xuất linh kiện phụ trợ nội địa Thái Lan cấp Tier-2, Tier-3. Hiện tượng phi công nghiệp hóa (deindustrialization) tại Thái Lan."
        },
        {
            "filename": "05_be_tac_tai_khoa_va_dong_luc_du_lich.md",
            "title": "Chuyên đề 05: Bế tắc Tài khóa, Tranh cãi Digital Wallet và Động lực Du lịch suy yếu",
            "question": "Phân tích thực trạng nợ công Thái Lan tiến sát trần 70% GDP, những tranh cãi xung quanh gói kích thích phát tiền số Digital Wallet (500 tỷ baht). Tại sao ngành du lịch (chiếm 12-18% GDP) không còn đủ sức gánh vác toàn bộ nền kinh tế? Cạnh tranh thương mại với hàng giá rẻ Trung Quốc và các đối thủ khu vực như Việt Nam, Indonesia."
        },
        {
            "filename": "06_bai_hoc_canh_tinh_cho_viet_nam.md",
            "title": "Chuyên đề 06: Bài học Cảnh tỉnh Chiến lược Phát triển cho Việt Nam và Đông Nam Á",
            "question": "Tổng hợp các bài học chiến lược từ khủng hoảng Thái Lan đối với Việt Nam: (1) Quản trị rủi ro nợ hộ gia đình và bong bóng bất động sản; (2) Tận dụng cơ hội dân số vàng trước khi bước vào giai đoạn già hóa (2036); (3) Chiến lược tự chủ công nghệ và nâng cấp chuỗi cung ứng công nghiệp thay vì chỉ gia công lắp ráp FDI; (4) Tránh bẫy thu nhập trung bình."
        }
    ]

    batch_extract_rag(nb_id, queries)
    print("\n=== HOÀN TẤT TOÀN BỘ QUY TRÌNH DEEP RESEARCH NOTEBOOKLM ===")


if __name__ == "__main__":
    main()
