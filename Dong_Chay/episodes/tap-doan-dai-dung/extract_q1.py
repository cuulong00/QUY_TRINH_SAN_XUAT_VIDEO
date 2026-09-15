import os
import json
import subprocess

NOTEBOOK_ID = "93df2e1c-62e3-4bd7-8cb9-7408f6159db9"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/tap-doan-dai-dung/research_vault"

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME

prompt = """Tóm lược và phân tích chuyên sâu về hành trình 30 năm phát triển và hồ sơ năng lực của Tập đoàn Đại Dũng (DDC):
1. Hành trình lịch sử từ năm 1995: Xưởng cơ khí nhỏ ban đầu -> Nhà máy An Hạ -> Chinh phục các công trình công nghiệp nặng, sân vận động World Cup, điện gió ngoài khơi và siêu hạ tầng.
2. Chân dung nhà sáng lập Trịnh Tiến Dũng: Triết lý lãnh đạo, tầm nhìn kỹ nghệ, vai trò tại HUBA và HĐQT PC1 Group.
3. Cấu trúc tổ chức, quy mô nhân sự (>6.000 người), giá trị cốt lõi và các đơn vị thành viên.
Trích dẫn số liệu định lượng, mốc thời gian và nguồn chi tiết."""

target_file = os.path.join(OUTPUT_DIR, "01_ho_so_nang_luc_va_lich_su_phat_trien_dai_dung.md")

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
    f.write("# Hồ Sơ Năng Lực, Lịch Sử 30 Năm Phát Triển & Chân Dung Nhà Sáng Lập Trịnh Tiến Dũng\n\n")
    f.write(answer)
    f.write("\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC Deep Research Engine*\n")

print(f"✅ Hoàn thành trích xuất chuyên đề 01: {len(answer)} ký tự")
