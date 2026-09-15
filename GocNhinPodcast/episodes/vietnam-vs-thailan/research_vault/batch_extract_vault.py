import os
import json
import subprocess
import time

NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
NOTEBOOKLM_CLI = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
NOTEBOOK_ID = "ddb6a362-5217-460b-b7c3-3fc2bc88314d"
VAULT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/bay-thu-nhap-trung-binh-1975-2045/research_vault"

QUESTIONS = [
    {
        "filename": "01_geopolitical_constraints_1975_1994.md",
        "title": "Ràng Buộc Địa Chính Trị & Chi Phí Thời Chiến (1975–1994)",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy phân tích toàn diện các ràng buộc địa chính trị và thời chiến mà Việt Nam phải đối mặt từ 1975 đến 1994: Chi phí kinh tế và tỷ trọng ngân sách quốc phòng của 10 năm chiến tranh biên giới Tây Nam & phía Bắc (1978-1989), lệnh cấm vận thương mại của Mỹ (Trading with the Enemy Act kéo dài đến 03/02/1994) cô lập khỏi WB/IMF, và cú sốc sụp đổ khối XHCN Đông Âu & Liên Xô (1989-1991) làm mất hơn 80% thị trường. So sánh với điều kiện ban đầu của Hàn Quốc được Mỹ viện trợ và bảo trợ trong Chiến tranh Lạnh. Trình bày chi tiết với số liệu và nguồn trích dẫn."
    },
    {
        "filename": "02_subsidized_economy_hyperinflation_1986.md",
        "title": "Khủng Hoảng Thể Chế Bao Cấp & Siêu Lạm Phát 1986",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy mổ xẻ cơ chế kinh tế kế hoạch hóa tập trung quan liêu bao cấp, ngăn sông cấm chợ và cuộc cải cách Giá - Lương - Tiền tháng 9/1985. Cung cấp số liệu thực chứng về đỉnh điểm lạm phát 774.7% năm 1986, tình trạng khan hiếm lương thực phải ăn độn bo bo khoai sắn, sự suy kiệt sức mua của đồng tiền, và bài học đắt giá về quy luật thị trường. Trình bày chi tiết với số liệu và nguồn trích dẫn."
    },
    {
        "filename": "03_doi_moi_grassroots_reforms.md",
        "title": "Quá Trình Tự Sửa Sai & Đột Phá Đổi Mới Từ Cơ Sở",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy giải mã quá trình tự sửa sai và chuyển dịch thể chế từ dưới lên: Các hiện tượng 'xé rào' tại địa phương, Khoán 100 (1981), Khoán 10 (1988), và bước ngoặt Đại hội VI (1986) dưới sự lãnh đạo của Tổng Bí thư Nguyễn Văn Linh. Bản chất của việc chuyển đổi sang kinh tế thị trường định hướng XHCN mà không gây sụp đổ thể chế hay hỗn loạn xã hội như Đông Âu. Trình bày chi tiết với số liệu và nguồn trích dẫn."
    },
    {
        "filename": "04_world_bank_poverty_reduction_miracle.md",
        "title": "Đánh Giá Của World Bank & UNDP: Kỳ Tích Giảm Nghèo Bao Trùm",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy tổng hợp đánh giá của Ngân hàng Thế giới (World Bank) và UNDP về thành tựu xóa đói giảm nghèo của Việt Nam: Tỷ lệ nghèo cùng cực giảm từ hơn 70% (sau 1975) và 58% (1993) xuống dưới 3% hiện nay. Đánh giá về tính bao trùm (Inclusive Growth), Chỉ số Vốn con người (Human Capital Index - HCI) và Chỉ số Phát triển Con người (HDI). Trình bày chi tiết với số liệu và nguồn trích dẫn."
    },
    {
        "filename": "05_thailand_middle_income_trap_lessons.md",
        "title": "Bài Học Chiếc Bẫy Thu Nhập Trung Bình Của Thái Lan & ASEAN",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy phân tích bài học về 'Bẫy thu nhập trung bình' (Middle-Income Trap) từ trường hợp của Thái Lan và Malaysia: Tại sao Thái Lan không có chiến tranh sau 1975, đón sóng FDI sớm nhưng đã bị 'chôn chân' ở mức 7.000 - 7.500 USD suốt hơn 13 năm qua? Bản chất giới hạn của mô hình tăng trưởng dựa trên vốn và gia công lắp ráp giá rẻ. Trình bày chi tiết với số liệu và nguồn trích dẫn."
    },
    {
        "filename": "06_dual_economy_fdi_vs_domestic_tech.md",
        "title": "Nghiên Cứu Harvard Kennedy School: Nền Kinh Tế Nhị Nguyên",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy tổng hợp các nghiên cứu của Harvard Kennedy School (Chương trình Việt Nam - GS. Dwight Perkins, TS. Vũ Thành Tự Anh) và World Bank về 'Nền kinh tế nhị nguyên' (Dual Economy) của Việt Nam: Khối FDI chiếm hơn 70% xuất khẩu nhưng liên kết lan tỏa công nghệ (FDI spillovers) yếu, tỷ lệ giá trị gia tăng nội địa (Domestic Value Added) chỉ đạt 20-30%, và nguy cơ kẹt lại ở mắt xích gia công giá rẻ. Trình bày chi tiết với số liệu và nguồn trích dẫn."
    },
    {
        "filename": "07_demographic_clock_aging_population_2036.md",
        "title": "Đồng Hồ Nhân Khẩu Học & Thách Thức 'Chưa Giàu Đã Già'",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy phân tích cảnh báo của UNFPA, IMF và Tổng cục Thống kê về tốc độ già hóa dân số của Việt Nam: Thời gian chuyển từ 'già hóa' (2011) sang 'dân số già' (2036) chỉ mất 25 năm (nhanh kỷ lục so với phương Tây). Cửa sổ dân số vàng khép lại sau năm 2035 và áp lực lên năng suất lao động, quỹ an sinh, gánh nặng y tế. Trình bày chi tiết với số liệu và nguồn trích dẫn."
    },
    {
        "filename": "08_structural_reforms_tfp_target_2045.md",
        "title": "Báo Cáo World Bank 'Việt Nam 2035' & Cửa Hẹp 2045",
        "prompt": "Dựa trên các tài liệu đã nạp, hãy phân tích các khuyến nghị chính sách trong báo cáo 'Việt Nam 2035' của World Bank và mục tiêu trở thành quốc gia phát triển thu nhập cao (>14.000 USD) vào năm 2045: Đòi hỏi chuyển đổi mô hình tăng trưởng dựa trên Năng suất tổng nhân tố (TFP), phát triển công nghệ lõi (bán dẫn, AI, kinh tế số), cải cách thể chế và xây dựng doanh nghiệp dân tộc tự chủ. Trình bày chi tiết với số liệu và nguồn trích dẫn."
    }
]

def ask_question(prompt, title):
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    cmd = [
        NOTEBOOKLM_CLI,
        "ask",
        prompt,
        "-n", NOTEBOOK_ID,
        "--json"
    ]
    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if result.returncode == 0:
        try:
            data = json.loads(result.stdout)
            answer = data.get("answer", "")
            references = data.get("references", [])
            return answer, references
        except Exception as e:
            return result.stdout, []
    else:
        print(f"Error for {title}: {result.stderr}")
        return None, []

def main():
    os.makedirs(VAULT_DIR, exist_ok=True)
    print(f"Bắt đầu Batch Extraction 8 câu hỏi chuyên sâu từ NotebookLM (ID: {NOTEBOOK_ID})...")
    
    for i, q in enumerate(QUESTIONS, 1):
        filename = os.path.join(VAULT_DIR, q["filename"])
        print(f"[{i}/8] Đang trích xuất: {q['title']}...")
        answer, refs = ask_question(q["prompt"], q["title"])
        if answer:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# {q['title']}\n\n")
                f.write(f"> **Nguồn trích xuất:** Master Notebook `{NOTEBOOK_ID}`  \n")
                f.write(f"> **Mục đích:** Cung cấp mỏ neo dữ liệu thực chứng cho kịch bản episode `bay-thu-nhap-trung-binh-1975-2045`  \n\n---\n\n")
                f.write(answer)
                f.write("\n\n---\n### Danh mục Trích dẫn & Tham chiếu (Citations)\n")
                if refs:
                    for ref in refs:
                        f.write(f"- [{ref.get('citation_number', '')}] {ref.get('cited_text', '')}\n")
                else:
                    f.write("- Trích xuất trực tiếp từ các nguồn tổng hợp trong Master Notebook.\n")
            print(f"  ✓ Đã lưu: {q['filename']}")
        else:
            print(f"  ✗ Thất bại khi trích xuất {q['title']}")
        time.sleep(2)
    print("Hoàn tất Batch Extraction vào research_vault!")

if __name__ == "__main__":
    main()
