#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time

NOTEBOOK_ID = "b90c33cf-e11f-4c0d-9439-923424b79877"
NOTEBOOKLM_HOME = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
CLI_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/khong-vung-thi-dung-noi-den-manh/research_vault"

os.makedirs(OUTPUT_DIR, exist_ok=True)

QUERIES = [
    {
        "filename": "01_macro_theoretical_framework.md",
        "title": "Khung Lý Thuyết Vĩ Mô: Solow, TFP, Antifragility & Đệm Kinh Tế Phi Chính Thức",
        "question": """Trích xuất chi tiết cơ sở lý thuyết kinh tế học về:
1. Mô hình Solow-Swan và quy luật lợi suất giảm dần của vốn (K) khi thiếu vắng năng suất nhân tố tổng hợp (A/TFP). Phương trình tích lũy vốn Solow, trạng thái dừng (steady-state) và tác động của TFP đến hàm sản xuất.
2. Thuyết 'Chống mong manh' (Antifragility) của Nassim Nicholas Taleb: Ứng dụng vào cấu trúc kinh tế vĩ mô; sự khác biệt giữa hệ thống cồng kềnh dễ vỡ (Fragile) và hệ thống hấp thụ cú sốc để tiến hóa (Resilient/Antifragile).
3. Vai trò đệm giảm chấn của khu vực kinh tế phi chính thức (Informal Sector) và dòng kiều hối (Remittances) theo các nghiên cứu của World Bank và ILO.
4. Khung phân tích Năng lực nhà nước (State Capacity vs Scope of State) của Francis Fukuyama và Thể chế bao trùm (Inclusive Institutions) của Daron Acemoglu & James Robinson.
Lập bảng so sánh giữa tăng trưởng theo chiều rộng (Scale/Mạnh) vs chiều sâu (Resilience/Vững) kèm công thức toán học và số liệu thực chứng."""
    },
    {
        "filename": "02_argentina_case_study.md",
        "title": "Giải Phẫu Ca Vỡ Nợ Thế Kỷ Của Argentina: Dân Túy, Thâm Hụt Và Bài Học Bỏ Rơi Sản Xuất",
        "question": """Trích xuất chi tiết dòng thời gian và cơ chế sụp đổ kinh tế của Argentina từ đầu thế kỷ 20 đến nay:
1. Số liệu GDP bình quân đầu người giai đoạn 1900-1920 so với châu Âu (dựa trên dữ liệu lịch sử Maddison Database); câu ngạn ngữ 'Giàu như một người Argentina'.
2. Cơ chế bẫy dân túy Peronism, sự phình to của chi tiêu công, thâm hụt tài khóa triền miên và chính sách in tiền bù ngân sách.
3. Lịch sử 9 lần vỡ nợ quốc tế, số liệu lạm phát phi mã và diễn biến phá giá đồng Peso.
4. Bản chất của việc phụ thuộc vào nông sản xuất khẩu mà bỏ rơi nền sản xuất công nghiệp chế tạo tự chủ."""
    },
    {
        "filename": "03_thailand_1997_crisis.md",
        "title": "Khủng Hoảng Tài Chính Thái Lan 1997: Cơn Say Vốn Nóng BIBF, Bong Bóng BĐS Và Sự Thức Tỉnh Tàn Nhẫn",
        "question": """Phân tích giải phẫu chi tiết cuộc khủng hoảng tài chính Thái Lan 1997:
1. Cơ chế hoạt động của BIBF (Bangkok International Banking Facility) trong việc hút vốn vay USD ngắn hạn với lãi suất rẻ.
2. Tỷ trọng dòng vốn đổ vào bất động sản và bong bóng tài sản tại Bangkok giai đoạn 1990-1996; sự tắc nghẽn của hệ thống ngân hàng thương mại.
3. Cán cân thanh toán và số liệu cạn kiệt dự trữ ngoại hối của Ngân hàng Trung ương Thái Lan trước các đợt tấn công tỷ giá của quỹ đầu cơ quốc tế.
4. Diễn biến ngày định mệnh 02/07/1997 thả nổi đồng Baht, sự phá sản của hàng loạt công ty tài chính và hiệu ứng domino lan sang châu Á."""
    },
    {
        "filename": "04_greece_debt_crisis.md",
        "title": "Hy Lạp & Khủng Hoảng Nợ Công Eurozone: Ảo Tưởng Tiêu Dùng Vượt Năng Suất Và Gian Lận Thể Chế",
        "question": """Trích xuất dữ liệu và cơ chế khủng hoảng nợ công Hy Lạp:
1. Số liệu chi tiêu công, phúc lợi, lương hưu và thâm hụt tài khóa thực tế giai đoạn 2000-2009 so với trần Maastricht; tiêu dùng vượt quá năng suất lao động.
2. Vai trò của các hợp đồng phái sinh hoán đổi tiền tệ (cross-currency swaps) với Goldman Sachs trong việc che giấu nợ công quốc gia.
3. Diễn biến khi sự thật bị phơi bày năm 2009, lợi suất trái phiếu chính phủ Hy Lạp tăng vọt và mất khả năng tiếp cận thị trường vốn.
4. Hậu quả kinh tế - xã hội của 3 gói cứu trợ đi kèm điều kiện thắt lưng buộc bụng tàn khốc từ Troika (IMF, EC, ECB)."""
    },
    {
        "filename": "05_east_asia_resilience_benchmarks.md",
        "title": "Mô Hình Tự Cường Đông Á: Hàn Quốc Đại Phẫu Chaebol, Cụm SMEs Đài Loan & Thể Chế Singapore",
        "question": """Trích xuất chi tiết về các con đường tự cường kinh tế của các nền kinh tế Đông Á:
1. Cuộc đại phẫu của Hàn Quốc hậu 1997: xóa bỏ các Chaebol zombie (Daewoo), tái cơ cấu nợ xấu ngân hàng qua KAMCO, xử lý sở hữu chéo, và chính sách đẩy chi tiêu R&D lên trên 4% GDP để làm chủ công nghệ bán dẫn (Samsung, SK Hynix), ô tô.
2. Mô hình mạng lưới SMEs bán dẫn linh hoạt của Đài Loan: Tự cường bằng cụm công nghiệp hỗ trợ ngách và vai trò của TSMC.
3. Mô hình Singapore: Tự cường bằng thể chế pháp quyền liêm chính, năng lực quản trị dòng vốn và trung tâm logistics hàng hải số 1.
Lập bảng so sánh ưu nhược điểm của 3 mô hình này và bài học tương thích với Việt Nam."""
    },
    {
        "filename": "06_vietnam_fdi_trade_audit.md",
        "title": "Kiểm Toán Ngoại Thương & Khối FDI Việt Nam: Gia Công Thô Hay Đòn Bẩy Tích Lũy Ngoại Hối?",
        "question": """Kiểm toán kinh tế thực chứng đa chiều về vị thế và tác động của khối FDI đối với Việt Nam:
1. Mặt trái và Lỗ hổng Cấu trúc: Tỷ trọng kim ngạch xuất khẩu của khối FDI (~72-74%), tỷ lệ DVA nội địa trong ngành điện tử/dệt may, tỷ lệ doanh nghiệp Việt làm Tier-1/Tier-2 cho Samsung/Apple, hiện tượng kinh tế đảo ngoại vi (Enclave Economy).
2. Vai trò Trụ Cột và Lợi ích Thực Chứng: Đóng góp của thặng dư thương mại FDI vào kho dự trữ ngoại hối (~100 tỷ USD) giúp giữ vững tỷ giá; tạo việc làm cho hơn 5 triệu lao động; đào tạo kỹ sư công nghiệp và chuyển giao kỹ năng quản trị chuỗi cung ứng.
3. Bài toán Chiến lược: Rủi ro dịch chuyển chuỗi cung ứng trước thuế tối thiểu toàn cầu, cơ chế Quỹ Hỗ trợ đầu tư (Nghị định 182/2024/NĐ-CP) và lộ trình nội địa hóa khả thi."""
    },
    {
        "filename": "07_vietnam_banking_realestate_audit.md",
        "title": "Mạch Máu Tài Chính & Bất Động Sản Việt Nam: Giải Mã Động Lực Gốc Và Luật Các TCTD 2024",
        "question": """Kiểm toán hệ thống tài chính - ngân hàng và bất động sản Việt Nam:
1. Rủi ro Hệ thống: Tỷ lệ tài sản bảo đảm là BĐS trong hệ thống ngân hàng thương mại (60-70%), cơ cấu tín dụng BĐS, áp lực đáo hạn trái phiếu doanh nghiệp BĐS giai đoạn 2024-2026, đại án Vạn Thịnh Phát/SCB và sở hữu chéo.
2. Góc nhìn Động lực Xã hội: Tại sao đất đai là kênh tích lũy tài sản chủ đạo của người dân khi lãi suất thực âm, vàng bị siết và thiếu kênh đầu tư an toàn? Đóng góp của tiền sử dụng đất (12-15% ngân sách) trong việc đối ứng phát triển hạ tầng giao thông đô thị 25 năm qua.
3. Giải pháp Tháo gỡ: Các điều khoản mang tính bước ngoặt của Luật Các tổ chức tín dụng 2024 (siết sở hữu cổ phần, giảm giới hạn cấp tín dụng, cấm bán bảo hiểm kèm khoản vay) và bài toán phát triển quỹ hưu trí tự nguyện làm kênh dẫn vốn dài hạn."""
    },
    {
        "filename": "08_vietnam_institutional_reform.md",
        "title": "Đột Phá Thể Chế, Tinh Gọn Bộ Máy & Giải Mã Căn Bệnh Sợ Sai Trong Đầu Tư Công",
        "question": """Tổng hợp phân tích về thể chế và bộ máy nhà nước tại Việt Nam:
1. Chỉ đạo lịch sử của Tổng Bí thư Tô Lâm: Xác định 'Thể chế là điểm nghẽn của điểm nghẽn', đưa 'chống lãng phí' ngang hàng với chống tham nhũng; cuộc cách mạng tinh gọn tổ chức bộ máy, sáp nhập bộ ngành, dẹp bỏ cấp trung gian.
2. Bản chất bệnh 'Sợ sai, Né tránh trách nhiệm': Xung đột, chồng chéo giữa Luật Đất đai, Đầu tư, Xây dựng, Đấu thầu khiến cán bộ rơi vào bẫy 'làm đúng luật này thì vi phạm luật khác'; số liệu vốn đầu tư công tồn đọng trong Kho bạc Nhà nước (hàng trăm ngàn tỷ đồng).
3. Cơ chế Khơi thông: Bảo vệ cán bộ '6 dám' theo Kết luận số 14-KL/TW và Nghị định 73/2023/NĐ-CP; giải phóng chi thường xuyên để dồn lực cho chi đầu tư phát triển."""
    },
    {
        "filename": "09_vietnam_demographics_productivity.md",
        "title": "Bẫy Nhân Khẩu Học, Năng Suất Lao Động & Bài Toán An Sinh Xã Hội",
        "question": """Trích xuất dữ liệu nhân khẩu học, năng suất lao động và an sinh xã hội của Việt Nam:
1. Tốc độ già hóa dân số của Việt Nam, dự báo thời điểm kết thúc thời kỳ 'dân số vàng' và nguy cơ rơi vào bẫy 'chưa giàu đã già'.
2. Năng suất lao động theo PPP của Việt Nam so với Singapore, Malaysia, Thái Lan, Indonesia; nguyên nhân năng suất tăng chậm.
3. Tỷ số giữa giá nhà ở bình quân so với thu nhập của người lao động trẻ tại các đô thị lớn; áp lực chi phí sinh hoạt khiến thanh niên ngại kết hôn, ngại sinh con.
4. Lưới an sinh xã hội, độ bao phủ bảo hiểm xã hội và tính cấp bách của Đề án 1 triệu căn nhà ở xã hội."""
    },
    {
        "filename": "10_vietnam_industrial_strategy_2045.md",
        "title": "Chiến Lược Tự Cường 2045: Nghị Quyết 29-NQ/TW, National Champions & Hạ Tầng Chiến Lược",
        "question": """Trích xuất các định hướng chiến lược lớn của Đảng và Chính phủ hướng tới năm 2030, tầm nhìn 2045:
1. Nghị quyết số 29-NQ/TW về tiếp tục đẩy mạnh công nghiệp hóa, hiện đại hóa: Xây dựng các doanh nghiệp dân tộc đầu đàn (National Champions), tự chủ công nghệ cơ khí chế tạo, bán dẫn, và đại dự án đường sắt tốc độ cao Bắc - Nam.
2. Mục tiêu nâng tỷ trọng đóng góp của TFP (Năng suất nhân tố tổng hợp) lên trên 45-50% vào tăng trưởng GDP giai đoạn 2025-2030.
3. Các chỉ số an toàn vĩ mô: Tỷ lệ nợ công/GDP hiện tại (~37-39% so với trần 60%), dự trữ ngoại hối ròng và kỷ luật ngân sách quốc gia.
4. Thông điệp cốt lõi: 'Không vững thì đừng nói đến mạnh' — Nền tảng tự chủ công nghiệp và thể chế vững chãi là điều kiện tiên quyết để bước vào kỷ nguyên vươn mình."""
    }
]

def extract_query(q_idx, item):
    filename = item["filename"]
    title = item["title"]
    question = item["question"]
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    print(f"\n==========================================")
    print(f"[{q_idx+1}/10] EXTRACTING: {filename}")
    print(f"Title: {title}")
    print(f"==========================================")
    
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = NOTEBOOKLM_HOME
    
    cmd = [
        CLI_PATH,
        "ask",
        question,
        "-n", NOTEBOOK_ID,
        "--json"
    ]
    
    try:
        res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=300)
        if res.returncode != 0:
            print(f"ERROR extracting {filename}: {res.stderr}")
            return False
            
        data = json.loads(res.stdout)
        answer = data.get("answer", "")
        citations = data.get("citations", [])
        
        # Format markdown document
        md_content = f"""<!--
DOCUMENT PROVENANCE & EXTRACTION LINEAGE:
- Source Notebook ID: {NOTEBOOK_ID}
- Target Vault File: episodes/khong-vung-thi-dung-noi-den-manh/research_vault/{filename}
- Extraction Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
- Query Title: {title}
-->

# {title}

---

## 1. NỘI DUNG TỔNG HỢP THỰC CHỨNG & CƠ CHẾ VĨ MÔ

{answer}

---

## 2. BẢNG DANH MỤC NGUỒN KIỂM CHỨNG (CITED REFERENCES)

| Citation ID | Source Title | Cited Fragment Summary |
| :--- | :--- | :--- |
"""
        seen_citations = set()
        for c in citations:
            c_num = c.get("citation_number", "?")
            c_title = c.get("source_id", "Source") # Will be updated with snippet
            c_text = c.get("cited_text", "").replace("\n", " ").strip()
            if len(c_text) > 120:
                c_text = c_text[:117] + "..."
            
            if c_num not in seen_citations:
                seen_citations.add(c_num)
                md_content += f"| [{c_num}] | Source Ref #{c.get('source_id', '')[:8]} | {c_text} |\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print(f"SUCCESS: Saved {len(answer)} chars to {filepath} with {len(seen_citations)} citations.")
        return True
    except Exception as e:
        print(f"Exception during extraction of {filename}: {e}")
        return False

def main():
    print(f"Starting batch extraction of 10 queries for Episode 72...")
    for idx, item in enumerate(QUERIES):
        success = extract_query(idx, item)
        if not success:
            print(f"Retrying query {idx+1} once after 5s...")
            time.sleep(5)
            extract_query(idx, item)
        time.sleep(3) # Small pacing between queries
        
    print("\nALL 10 QUERIES PROCESSED!")

if __name__ == "__main__":
    main()
