#!/usr/bin/env python3
import os
import sys
import json
import subprocess
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
CLI_PATH = WORKSPACE_ROOT / ".venv" / "bin" / "notebooklm"
SCRATCH_DIR = WORKSPACE_ROOT / "scratch"
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

NOTEBOOK_ID = "1e4df066-24e0-48fe-b67e-c1b12f7ff6ab"
VAULT_DIR = WORKSPACE_ROOT / "episodes" / "grab-vs-gsm-tai-xe-tat-app" / "research_vault"
VAULT_DIR.mkdir(parents=True, exist_ok=True)

QUESTIONS = [
    {
        "filename": "01_grab_take_rate_and_algorithmic_control.md",
        "title": "Bóc Tách Khấu Trừ Grab & Cơ Chế Bẻ Gãy Tắt App",
        "question": "Bóc tách chi tiết công thức trừ tiền 4 tầng của Grab sau Nghị định 126/2020/NĐ-CP (thuế VAT 10%, phí sử dụng ứng dụng, thuế TNCN, phí cuốc cố định). Giải thích cơ chế hoạt động của thuật toán ghép đơn (order batching) và cách Dynamic Pricing kích hoạt Surge Pricing để bẻ gãy các đợt tắt app của tài xế theo lý thuyết Nghịch lý tù nhân. Trích dẫn số liệu tài chính của Grab tại Việt Nam và toàn cầu."
    },
    {
        "filename": "02_gsm_financial_anatomy_and_vinfast_synergy.md",
        "title": "Giải Phẫu Tài Chính GSM & Mối Quan Hệ Với VinFast",
        "question": "Phân tích báo cáo xếp hạng tín nhiệm của Saigon Ratings đối với GSM Xanh SM (bậc vnBBB+, hồ sơ rủi ro tài chính 5/6, nợ vay, EBITDA). Số liệu doanh thu thuần năm 2025 đạt 16.000 - 17.400 tỷ đồng (+125%). Bản chất giao dịch các bên liên quan giữa GSM và VinFast: vai trò hấp thụ sản lượng xe, tiếp thị trải nghiệm thực tế, và kế hoạch IPO Hong Kong năm 2027 với định giá 20 tỷ USD."
    },
    {
        "filename": "03_market_share_triumvirate_and_regulatory_push.md",
        "title": "Bàn Cờ Thị Phần Tam Mã & Đòn Bẩy Thể Chế 876",
        "question": "Phân tích diễn biến thị phần gọi xe 4 bánh và 2 bánh tại Việt Nam giai đoạn 2023 - 2026 sau khi Gojek rút lui. Tác động từ Quyết định 876/QĐ-TTg của Thủ tướng Chính phủ quy định 100% taxi chuyển sang xe điện đến năm 2030 đối với Grab. Bức tường hạ tầng trạm sạc độc quyền V-GREEN bảo vệ GSM như thế nào? Sự chuyển dịch của các hãng taxi truyền thống vào liên minh Xanh SM Partner."
    },
    {
        "filename": "04_unit_economics_ice_vs_ev.md",
        "title": "Đối Soát Unit Economics 100km: Xe Điện vs Xe Xăng",
        "question": "Lập bảng đối chiếu chi phí đơn vị (Unit Economics) trên 100km giữa xe điện VinFast VF5 và xe xăng Toyota Vios/Hyundai Accent: Tiền nhiên liệu (điện vs xăng), chi phí bảo dưỡng định kỳ, khấu hao pin. Phân tích bẫy khấu hao tài sản (Depreciation Trap) và gánh nặng nợ vay ngân hàng mua xe trả góp của tài xế GrabCar."
    },
    {
        "filename": "05_driver_lived_experience_and_discipline.md",
        "title": "Hiện Thực Đời Sống: Kỷ Luật Quân Đội vs Tự Do Bấp Bênh",
        "question": "So sánh hiện thực đời sống và áp lực lao động giữa tài xế Xanh SM và tài xế Grab: Kỷ luật tác phong 5 sao, quy chế xử phạt và chính sách truy thu ví tài xế hụt KPI của Xanh SM. Cơn ác mộng trạm sạc: quy định phạt 10 phút đỗ quá giờ V-GREEN (1.000đ/phút từ 26/8/2025), việc mất ngủ canh giờ sạc đêm. So sánh với sự tự do bấp bênh của tài xế Grab."
    },
    {
        "filename": "06_the_convergence_trap_and_informal_labor.md",
        "title": "Bẫy Chuyển Dịch 'Grab Hóa' Của GSM & Tương Lai Lao Động",
        "question": "Phân tích xu hướng chuyển dịch của GSM từ tài xế cơ hữu (lương cứng, đóng BHXH) sang mô hình Xanh SM Platform (thuê xe, khoán doanh thu). Tại sao các nền tảng gọi xe luôn kết thúc bằng việc đẩy rủi ro tài chính cho người lao động? Đánh giá tương lai của tầng lớp lao động phi chính thức (precariat) khi bước qua tuổi 45-50."
    }
]

print(f"🚀 BẮT ĐẦU TRÍCH XUẤT 6 HỒ SƠ VAULT TỪ MASTER NOTEBOOK: {NOTEBOOK_ID}")

for idx, item in enumerate(QUESTIONS, 1):
    filename = item["filename"]
    title = item["title"]
    q = item["question"]
    target_file = VAULT_DIR / filename

    print(f"\n[{idx}/6] Đang xử lý: {title} -> {filename}...")

    q_file = SCRATCH_DIR / f"q_{idx}.txt"
    q_file.write_text(q, encoding="utf-8")

    cmd = [
        str(CLI_PATH), "ask",
        "--prompt-file", str(q_file),
        "-n", NOTEBOOK_ID,
        "--save-as-note",
        "-t", title,
        "--json"
    ]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(res.stdout)
        answer = data.get("answer", "")
        references = data.get("references", [])

        md = f"<!--\nPROVENANCE METADATA:\n- Target File: episodes/grab-vs-gsm-tai-xe-tat-app/research_vault/{filename}\n- Query: {q}\n- Source: Google NotebookLM Master Notebook ({NOTEBOOK_ID})\n-->\n\n"
        md += f"# {title}\n\n"
        md += f"> **Câu hỏi trích xuất:** {q}\n\n"
        md += f"## 1. Nội dung Phân tích & Dữ liệu Thực chứng\n\n{answer}\n\n"

        if references:
            md += "## 2. Mỏ neo Trích dẫn Nguồn (Citations / Footnotes)\n\n"
            for ref in references:
                c_no = ref.get("citation_number", "")
                c_text = ref.get("cited_text", "").strip()
                c_src = ref.get("source_id", "")
                md += f"- **[{c_no}]**: *\"{c_text}\"*\n"

        target_file.write_text(md, encoding="utf-8")
        print(f"✓ Thành công: {len(md.splitlines())} dòng đã ghi vào {filename}")
    except Exception as e:
        print(f"✗ Lỗi khi trích xuất câu {idx}: {e}")
        if hasattr(e, 'stderr') and e.stderr:
            print(f"   Stderr: {e.stderr}")

print("\n🎉 HOÀN TẤT TOÀN BỘ 6 HỒ SƠ TRÍCH XUẤT RA VAULT!")
