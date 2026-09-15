import os
import subprocess
import json

NOTEBOOK_ID = "b2b49222-8024-438f-9d67-db8951a5fdf5"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/thai-lan-vet-xe-do-nhat-ban/research_vault"

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME

prompt = """Phân tích chuyên sâu và toàn diện về tình trạng kinh tế vĩ mô của Thái Lan giai đoạn 2024-2026:
1. Tăng trưởng GDP đình trệ: Xu hướng sụt giảm từ vị thế 'Con hổ châu Á' (7-9% thập niên 80-90) xuống chỉ còn quanh 1.9% - 2.3% hiện nay. So sánh dự báo của NESDC, BoT, World Bank, IMF.
2. Nghịch lý lãi suất chính sách 1%: Quyết định giữ nguyên lãi suất 1% của BoT (cuộc họp tháng 8/2026), thuộc hàng thấp nhất thế giới (chỉ cao hơn Thụy Sĩ). Nguy cơ đảo ngược vị thế khi lãi suất Thái Lan có thể thấp hơn cả Nhật Bản (BOJ tăng lên 1% và có xu hướng tăng tiếp).
3. Chuỗi giảm phát kéo dài & Áp lực giá: Chuỗi 12 tháng giảm phát trước xung đột Trung Đông và lạm phát hạ nhiệt xuống 1.95% vào tháng 7/2026. Tác động của việc cầu nội địa suy kiệt.
4. Bẫy thanh khoản (Liquidity Trap) & Tê liệt chính sách tiền tệ: Lời thừa nhận của Don Nakornthab (Trợ lý Thống đốc BoT) về việc chính sách tiền tệ đã chạm giới hạn. Nhận định của Louise Loo (Oxford Economics), Nond Prueksiri (SCB EIC), Aris Dacanay (HSBC).
Trích dẫn số liệu định lượng, mốc thời gian, bảng biểu so sánh và nguồn chi tiết."""

target_file = os.path.join(OUTPUT_DIR, "01_macro_growth_and_interest_rate_trap.md")

cmd = [
    NOTEBOOKLM_BIN,
    "ask",
    prompt,
    "-n", NOTEBOOK_ID,
    "--json"
]

print("Đang trích xuất lại chuyên đề 01...")
result = subprocess.run(cmd, capture_output=True, text=True, env=env, check=True)
data = json.loads(result.stdout)
answer = data.get("answer", "")

with open(target_file, "w", encoding="utf-8") as f:
    f.write("# Tăng trưởng GDP Đình trệ, Lãi suất 1% và Bẫy Thanh khoản (Bản Bóc tách Chuyên sâu)\n\n")
    f.write(f"**Trích xuất từ Master Notebook ID:** `{NOTEBOOK_ID}`\n\n---\n\n")
    f.write(answer)
    f.write("\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC Deep Research Engine*\n")

print(f"✅ Hoàn thành trích xuất chuyên đề 01: {len(answer)} ký tự")
