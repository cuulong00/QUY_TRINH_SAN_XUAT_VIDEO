import os
import subprocess
import json
import time

NOTEBOOK_ID = "8a0efeb8-9576-4aa6-ad4e-eafe5a60da34"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
CLI_PATH = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
VAULT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/van-cuoc-seu-dau-dan/research_vault"

QUESTIONS = [
    {
        "file": "01_nghi_quyet_79_the_che_kinh_te_nha_nuoc.md",
        "title": "Nghị Quyết 79 & Đột Phá Thể Chế Kinh Tế Nhà Nước",
        "query": """Tóm tắt có cấu trúc về Nghị quyết số 79-NQ/TW ngày 06/01/2026 của Bộ Chính trị về kinh tế nhà nước:
1. 9 thành tố cấu thành kinh tế nhà nước và vai trò chủ đạo.
2. Mục tiêu 2030 (1-3 tập đoàn vào Top 500 thế giới, 100% chuẩn OECD) và tầm nhìn 2045.
3. Cơ chế tháo gỡ điểm nghẽn 'bảo toàn vốn', phân định rủi ro kinh doanh và bảo vệ cán bộ đổi mới sáng tạo.
4. Nguyên tắc thị trường: không bảo hộ, không độc quyền, giữ lại nguồn thu thoái vốn để tái đầu tư."""
    },
    {
        "file": "02_tuyen_phong_thu_7_tap_doan_nha_nuoc_va_tro_cap_ngam.md",
        "title": "Tuyến Phòng Thủ: 7 Tập Đoàn Nhà Nước Trụ Cột & Cơ Chế Trợ Cấp Ngầm",
        "query": """Phân tích vai trò của 7 Tập đoàn Doanh nghiệp Nhà nước (SOE) trụ cột (EVN, PVN, Viettel, VNPT, MobiFone, Tân Cảng Sài Gòn, Vietcombank):
1. Tiêu chí lựa chọn 7 tập đoàn (tổng tài sản tỷ USD, thị phần >30%, nắm huyết mạch).
2. Cơ chế 'trợ cấp ngầm' vĩ mô của EVN và doanh nghiệp năng lượng: Mua giá thế giới cao, neo giá bán thấp để ghìm CPI và hỗ trợ sản xuất cho FDI/tư nhân.
3. Nghịch lý đa mục tiêu: Tại sao không thể dùng ROE/Lợi nhuận thương mại thuần túy để đánh giá đơn vị gánh nhiệm vụ an sinh vĩ mô?
4. Thách thức quản trị 'bảo toàn vốn' và rủi ro quan liêu."""
    }
]

def run():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    for q in QUESTIONS:
        target_path = os.path.join(VAULT_DIR, q["file"])
        print(f"Đang trích xuất: {q['title']}...")
        cmd = [CLI_PATH, "ask", q["query"], "-n", NOTEBOOK_ID, "--json"]
        res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=180)
        if res.returncode == 0:
            try:
                data = json.loads(res.stdout)
                content = data.get("answer", res.stdout)
            except Exception:
                content = res.stdout
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(f"# {q['title']}\n\n")
                f.write(f"> **Tệp nguồn trích xuất từ Master Notebook:** `{NOTEBOOK_ID}`\n")
                f.write(f"> **Thời gian trích xuất:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n")
                f.write(content)
                f.write("\n")
            print(f" -> Đã lưu: {target_path}")
        else:
            print(f" -> Lỗi: {res.stderr}")
        time.sleep(2)

if __name__ == "__main__":
    run()
