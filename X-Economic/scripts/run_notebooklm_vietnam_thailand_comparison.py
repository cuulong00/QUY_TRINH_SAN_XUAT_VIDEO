#!/usr/bin/env python3
"""
Deep Research & Extraction Pipeline for Comprehensive Economic Comparison:
Vietnam vs Thailand (Holistic Macroeconomic Power, Growth Trajectory, and Structural Strengths).
Enforces `--mode deep` and outputs to research_vault.
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
SCRATCH_DIR = WORKSPACE_ROOT / "scratch"

os.environ["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
os.environ["PYTHONUNBUFFERED"] = "1"


def run_cmd(args, capture=True):
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
    cmd = [str(CLI_PATH)] + args
    res = subprocess.run(cmd, env=env, capture_output=capture, text=True)
    if res.returncode != 0:
        err_msg = res.stderr or res.stdout
        raise RuntimeError(f"CLI error (code {res.returncode}): {err_msg}")
    return res.stdout


def execute_deep_research(nb_id: str, prompt_text: str, label: str, timeout: int = 1800):
    print(f"\n🔍 [DEEP RESEARCH] Bắt đầu nghiên cứu sâu: '{label}' (--mode deep)...")
    temp_prompt = SCRATCH_DIR / "deep_research_prompt_vn_th.txt"
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
        print(f"✓ Hoàn tất Deep Research '{label}' trong {elapsed:.1f}s. Nạp thêm {imported} nguồn uy tín.")
    except Exception as e:
        print(f"⚠️ Lỗi trong quá trình Deep Research '{label}': {e}")


def batch_extract_rag(nb_id: str, queries: list):
    print(f"\n📦 BẮT ĐẦU BATCH EXTRACTION ({len(queries)} chuyên đề so sánh) RA VAULT...")
    for idx, item in enumerate(queries, 1):
        filename = item["filename"]
        title = item["title"]
        question = item["question"]
        target_file = VAULT_DIR / filename

        print(f"\n[{idx}/{len(queries)}] Đang trích xuất RAG: {title} -> {filename}...")
        temp_q = SCRATCH_DIR / f"q_vn_th_{idx}.txt"
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
            md_content += f"> **Chuyên đề so sánh:** {title}\n"
            md_content += f"> **Câu hỏi trích xuất chuyên sâu:** {question}\n\n"
            md_content += f"## 1. Nội dung Phân tích & Dữ liệu Đối sánh Thực chứng\n\n{answer}\n\n"

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
    id_file = EPISODE_DIR / ".notebook_id"
    if not id_file.exists():
        print("❌ Không tìm thấy .notebook_id!")
        sys.exit(1)
    nb_id = id_file.read_text().strip()
    print(f"📖 Sử dụng Master Notebook ID: {nb_id}")

    # 1. Deep Research query tập trung so sánh toàn diện kinh tế Việt Nam vs Thái Lan
    prompt_comparison = """
Comprehensive comparison of economic power between Vietnam and Thailand current year 2025 2026:
- Nominal GDP, GDP PPP, GDP per capita, GDP growth rate trajectory (World Bank, IMF, ADB projections)
- Trade volume, export structure (electronics, semiconductors, high-tech vs automotive, agriculture), trade balance
- Foreign Direct Investment (FDI inflows, high-tech supply chain relocation China+1, Apple, Samsung, Foxconn, BYD)
- Demographics: Population size, Golden Demographic window vs Super-Aged society, total fertility rate (TFR), labor force quality
- Financial health: Household debt to GDP ratio (86% Thailand vs Vietnam), public debt to GDP ratio, fiscal space, monetary policy flexibility
- National champions, domestic technology independence (EV, telecom, AI vs retail conglomerates), infrastructure development (highways, ports, renewable energy)
- Predictions on when Vietnam's economy will surpass Thailand (CEBR, Nikkei Asia, Standard Chartered forecasts)
"""
    execute_deep_research(nb_id, prompt_comparison, "So sánh Tổng thể Sức mạnh Kinh tế Việt Nam vs Thái Lan")

    # 2. Batch extraction RAG queries
    queries = [
        {
            "filename": "07_so_sanh_tong_the_kinh_te_viet_nam_thai_lan.md",
            "title": "Chuyên đề 07: So sánh Tổng thể Sức mạnh Vĩ mô Kinh tế Việt Nam và Thái Lan",
            "question": "Lập bảng và phân tích so sánh tổng thể sức mạnh kinh tế của Việt Nam và Thái Lan trên các chỉ số vĩ mô cốt lõi: Quy mô GDP danh nghĩa (Nominal GDP), GDP theo sức mua tương đương (GDP PPP), GDP bình quân đầu người, tốc độ tăng trưởng kinh tế trung bình 5-10 năm qua, tổng kim ngạch xuất nhập khẩu, cán cân thương mại và dự trữ ngoại hối. Nêu rõ các dự báo từ IMF, World Bank, Nikkei Asia về thời điểm quy mô kinh tế Việt Nam vượt Thái Lan."
        },
        {
            "filename": "08_doi_sanh_fdi_cong_nghiep_va_chuoi_cung_ung.md",
            "title": "Chuyên đề 08: Đối sánh Năng lực Công nghiệp, Thu hút FDI và Chuỗi Cung ứng Toàn cầu",
            "question": "So sánh cơ cấu sản xuất công nghiệp và chuỗi cung ứng giữa Việt Nam và Thái Lan: (1) Khả năng thu hút dòng vốn FDI công nghệ cao (bán dẫn, điện tử, AI) trong làn sóng China+1; (2) Cơ cấu xuất khẩu (hàng công nghệ cao của Việt Nam vs linh kiện xe xăng truyền thống và nông sản của Thái Lan); (3) Năng lực tự chủ công nghệ của các tập đoàn nội địa (National Champions: Viettel, VinFast, FPT, Hòa Phát vs CP Group, ThaiBev, SCG)."
        },
        {
            "filename": "09_doi_sanh_nhan_khau_hoc_tai_chinh_va_du_dia.md",
            "title": "Chuyên đề 09: Đối sánh Nhân khẩu học, Sức khỏe Tài chính và Dư địa Phát triển",
            "question": "Phân tích sự đối lập về nhân khẩu học và sức khỏe tài chính giữa Việt Nam và Thái Lan: (1) Dân số 101 triệu (Cửa sổ dân số vàng đến 2036) của Việt Nam vs Dân số 67 triệu (Siêu già hóa, TFR 0.76-1.16, dân số thu hẹp) của Thái Lan; (2) Gánh nặng nợ hộ gia đình (86-90% GDP của Thái Lan vs mức kiểm soát an toàn của Việt Nam); (3) Dư địa tài khóa và nợ công (Nợ công Việt Nam ~37% GDP vs Thái Lan 66% sát trần); (4) Đánh giá tổng thể lợi thế cạnh tranh dài hạn của Việt Nam."
        }
    ]

    batch_extract_rag(nb_id, queries)
    print("\n=== HOÀN TẤT BATCH EXTRACTION SO SÁNH VIỆT NAM - THÁI LAN ===")


if __name__ == "__main__":
    main()
