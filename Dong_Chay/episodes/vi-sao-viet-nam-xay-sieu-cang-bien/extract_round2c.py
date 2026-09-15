import os
import json
import subprocess
import time

NOTEBOOK_ID = "b0e0cc8f-84b4-4d4f-b3d1-1c7e86ea0aa9"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
NOTEBOOKLM_BIN = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/vi-sao-viet-nam-xay-sieu-cang-bien/research_vault"

os.makedirs(OUTPUT_DIR, exist_ok=True)

QUESTIONS = [
    {
        "file": "17_phan_tich_tai_chinh_va_do_nhay_sieu_cang_can_gio.md",
        "title": "Phân Tích Tài Chính Dự Án & Độ Nhạy Kinh Tế Siêu Cảng Cần Giờ",
        "prompt": """Phân tích tài chính chi tiết và các kịch bản độ nhạy của siêu dự án Cảng trung chuyển quốc tế Cần Giờ:
1. Cơ cấu vốn và lộ trình giải ngân: Tổng vốn ~128.870 tỷ VND (~4.95 - 5 tỷ USD), tỷ lệ vốn chủ sở hữu (15%) vs vốn vay thương mại (85%), tiến độ phân kỳ 7 giai đoạn trong 20 năm, yêu cầu giải ngân tối thiểu 50.000 tỷ VND trong 10 năm đầu.
2. Dự phóng doanh thu và dòng tiền: Doanh thu ước tính 34.000 - 40.000 tỷ VND/năm (1,14 - 1,52 tỷ USD/năm) khi đạt tối đa công suất 16.9 triệu TEU; các nguồn thu (phí bốc xếp THC, phí hoa tiêu, lưu bãi, cấp nhiên liệu, dịch vụ đại lý).
3. Phân tích độ nhạy (Sensitivity Analysis): Thời gian hoàn vốn (Payback Period), tỷ suất hoàn vốn nội bộ (IRR) ước tính theo 3 kịch bản (Bull Case: MSC đưa đủ 80% hàng trung chuyển; Base Case: đạt 60-70%; Bear Case: chỉ đạt 40-50% do chu kỳ vận tải biển suy thoái). Trích dẫn số liệu và nguồn."""
    },
    {
        "file": "18_bang_so_lieu_dinh_luong_cung_va_cuoc_thc.md",
        "title": "Bảng Số Liệu Định Lượng Cứng: Cước THC, Năng Suất Cẩu Bến & So Sánh Quốc Tế",
        "prompt": """Tổng hợp bảng số liệu định lượng so sánh cứng và chi tiết giữa hệ thống cảng biển Việt Nam và các đối thủ lớn tại Đông Nam Á:
1. Bảng so sánh cước xếp dỡ container (THC - Terminal Handling Charge) tại cầu cảng: So sánh mức giá THC cho container 20ft và 40ft (hàng nhập/xuất/trung chuyển) giữa Cái Mép, Cần Giờ, Lạch Huyện với Singapore (Tuas/PSA), Malaysia (Tanjung Pelepas, Port Klang), Thái Lan (Laem Chabang).
2. Bảng so sánh năng suất vận hành: Tốc độ bốc dỡ cẩu bờ (Crane moves per hour), thời gian giải phóng tàu mẹ (Berth turnaround time), chiều dài cầu bến, mớn nước luồng tàu (Draft depth), kích cỡ tàu tối đa (TEU & DWT), sản lượng thực tế 2024-2025.
3. Bảng điểm chi tiết Chỉ số Hiệu quả Logistics (LPI) của World Bank: So sánh điểm số 6 tiêu chí (Hải quan, Hạ tầng, Vận tải quốc tế, Năng lực logistics, Theo dõi hàng, Đúng hạn) của Việt Nam vs Singapore, Malaysia, Thái Lan. Trích dẫn đầy đủ số liệu chính xác và nguồn."""
    }
]

def run():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    print(f"Bắt đầu trích xuất Round 2c: {len(QUESTIONS)} chuyên đề...")
    for idx, item in enumerate(QUESTIONS, 1):
        target_file = os.path.join(OUTPUT_DIR, item["file"])
        print(f"[{idx}/{len(QUESTIONS)}] Đang trích xuất: {item['title']} -> {item['file']}")
        
        cmd = [
            NOTEBOOKLM_BIN,
            "ask",
            item["prompt"],
            "-n", NOTEBOOK_ID,
            "--json"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, env=env, check=True)
            data = json.loads(result.stdout)
            answer = data.get("answer", "")
            
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(f"# {item['title']}\n\n")
                f.write(answer)
                f.write("\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC Deep Research Engine*\n")
            
            print(f"✅ Hoàn thành: {item['file']} ({len(answer)} ký tự)")
            time.sleep(2)
        except Exception as e:
            print(f"❌ Lỗi {item['file']}: {e}")

if __name__ == "__main__":
    run()
