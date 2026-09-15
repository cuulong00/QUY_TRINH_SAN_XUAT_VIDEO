import os
import json
import subprocess

NOTEBOOK_ID = "b0e0cc8f-84b4-4d4f-b3d1-1c7e86ea0aa9"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
TARGET_FILE = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/vi-sao-viet-nam-xay-sieu-cang-bien/research_vault/03_cuoc_chien_cang_trung_chuyen_quoc_te_singapore_malaysia.md"

prompt = """So sánh tương quan vị thế cảng trung chuyển quốc tế giữa Việt Nam và các đối thủ Đông Nam Á:
1. Đối thủ cạnh tranh chính: Cảng Tuas Singapore (công suất 65 triệu TEU, 20 tỷ USD), Cảng Tanjung Pelepas và Port Klang (Malaysia), Laem Chabang (Thái Lan).
2. Tiêu chí quyết định hub trung chuyển: Tọa độ luồng hàng hải, độ lệch tuyến (deviation), cước bốc dỡ THC, cam kết nguồn hàng của liên minh hãng tàu.
3. Tác động của các dự án khu vực: Kênh Funan Techo (Campuchia), dự án Landbridge Kra (Thái Lan). Trích dẫn số liệu cụ thể và nguồn tài liệu."""

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
    f.write("# Cuộc Chiến Giành Thị Phần Cảng Trung Chuyển Quốc Tế Đông Nam Á\n\n")
    f.write(answer)
    f.write("\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC Deep Research Engine*\n")

print(f"✅ Hoàn thành Q3: {len(answer)} ký tự")
