#!/usr/bin/env python3
import os
import json
import subprocess
from pathlib import Path

WORKSPACE_ROOT = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast")
NOTEBOOKLM_HOME = WORKSPACE_ROOT / ".notebooklm_home"
CLI_PATH = WORKSPACE_ROOT / ".venv_notebooklm" / "bin" / "notebooklm"
EPISODE_DIR = WORKSPACE_ROOT / "episodes" / "thai-lan-no-ngap-dau-vet-xe-do-nhat-ban"
VAULT_DIR = EPISODE_DIR / "research_vault"
SCRATCH_DIR = WORKSPACE_ROOT / "scratch"

os.environ["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
os.environ["PYTHONUNBUFFERED"] = "1"

id_file = EPISODE_DIR / ".notebook_id"
nb_id = id_file.read_text().strip()

question = """
Phân tích so sánh chuyên sâu và giải phẫu rủi ro Nợ hộ gia đình (Household Debt) giữa Thái Lan và Việt Nam:
1. So sánh tỷ lệ nợ hộ gia đình / GDP, quy mô nợ thực tế, tỷ lệ nợ trên thu nhập khả dụng (Debt-to-Income / DTI), tốc độ tăng trưởng nợ hộ gia đình trong 5-10 năm qua.
2. Cơ cấu nợ: Tỷ trọng nợ bất động sản/mua nhà (mortgage), nợ mua xe (auto loan), tín dụng tiêu dùng cá nhân (P-loans, thẻ tín dụng, BNPL) và nợ phi chính thức (tín dụng đen).
3. Cơ chế rủi ro và sự tàn phá: Tại sao nợ hộ gia đình 86-90% GDP biến thành 'cục máu đông' bóp nghẹt kinh tế Thái Lan (BSR, thắt chặt chi tiêu, tê liệt truyền dẫn tiền tệ)? 
4. Thực trạng và mầm mống rủi ro nợ hộ gia đình tại Việt Nam: Tỷ lệ nợ hộ gia đình Việt Nam đã tăng nhanh ra sao trong chu kỳ bùng nổ bất động sản và tín dụng tiêu dùng vừa qua? Những rủi ro tiềm ẩn đối với tầng lớp trẻ (Gen Z, Millennials) và người thu nhập thấp?
5. Các mốc cảnh báo đỏ (Early Warning Signals) và bài học phòng ngừa khẩn cấp để Việt Nam không giẫm phải vết xe đổ của Thái Lan.
"""

temp_q = SCRATCH_DIR / "q_household_debt.txt"
temp_q.write_text(question, encoding="utf-8")

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
cmd = [
    str(CLI_PATH), "ask",
    "--prompt-file", str(temp_q),
    "-n", nb_id,
    "--save-as-note",
    "-t", "Chuyên đề 10: Giải phẫu So sánh Rủi ro Nợ Hộ Gia Đình Thái Lan vs Việt Nam",
    "--json"
]
res = subprocess.run(cmd, env=env, capture_output=True, text=True)
if res.returncode == 0:
    data = json.loads(res.stdout)
    answer = data.get("answer", "")
    references = data.get("references", [])
    
    md_content = "# Chuyên đề 10: Giải phẫu So sánh Rủi ro Nợ Hộ Gia Đình Thái Lan vs Việt Nam\n\n"
    md_content += f"> **Câu hỏi:** {question}\n\n"
    md_content += f"## Nội dung Phân tích & Rủi ro Thực chứng\n\n{answer}\n\n"
    if references:
        md_content += "## Mỏ neo Trích dẫn Nguồn gốc\n\n"
        for ref in references:
            md_content += f"- **[{ref.get('citation_number')}]**: *\"{ref.get('cited_text','').strip()}\"*\n"
    
    target_file = VAULT_DIR / "10_giai_phau_rui_ro_no_ho_gia_dinh_vn_th.md"
    target_file.write_text(md_content, encoding="utf-8")
    print(f"✓ Đã lưu thành công vào {target_file.name}")
else:
    print(f"Error: {res.stderr or res.stdout}")
