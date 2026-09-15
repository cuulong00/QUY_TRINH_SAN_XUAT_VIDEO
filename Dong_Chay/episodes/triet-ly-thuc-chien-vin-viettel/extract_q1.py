import os
import json
import subprocess

NOTEBOOK_ID = "88e50fa8-b2db-43b5-990b-82543c6fd2d0"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
TARGET_FILE = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/triet-ly-thuc-chien-vin-viettel/research_vault/01_triet_ly_thuc_tien_vs_kiem_loi.md"

prompt = """Phân tích cô đọng và chuyên sâu về triết lý nhận thức và hành động của Viettel và Vingroup:
1. Hoàn cảnh, nguồn gốc và ý nghĩa thực tế của câu nói của Chủ tịch Phạm Nhật Vượng: "Tôi là người kiệm lời, chỉ thích làm". Vì sao Vingroup chọn cách im lặng trước truyền thông và để kết quả/sản phẩm tự lên tiếng?
2. Nguồn gốc và vai trò của giá trị cốt lõi số 1 tại Viettel: "Thực tiễn là tiêu chuẩn kiểm nghiệm chân lý" và tư tưởng của ông Nguyễn Mạnh Hùng: "Làm trước, học sau. Làm sẽ sinh ra nghĩ".
3. So sánh điểm tương đồng và khác biệt giữa 2 triết lý này, kèm các dẫn chứng thực tế."""

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME

cmd = [
    NOTEBOOKLM_BIN,
    "ask",
    prompt,
    "-n", NOTEBOOK_ID,
    "--json"
]

result = subprocess.run(cmd, capture_output=True, text=True, env=env, check=True)
data = json.loads(result.stdout)
answer = data.get("answer", "")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write("# Triết lý Thực tiễn vs Kiệm lời\n\n")
    f.write(answer)
    f.write("\n\n---\n*Trích xuất tự động qua NotebookLM Direct RPC Engine*\n")

print(f"✅ Hoàn thành 01_triet_ly_thuc_tien_vs_kiem_loi.md ({len(answer)} ký tự)")
