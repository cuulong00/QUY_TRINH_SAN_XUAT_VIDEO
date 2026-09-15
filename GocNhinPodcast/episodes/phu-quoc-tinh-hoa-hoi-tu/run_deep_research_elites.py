import asyncio
import json
import os
from pathlib import Path
from notebooklm import NotebookLMClient

NOTEBOOK_ID = "82a612e7-c2d6-4cb7-b38e-2fcd8d223489"
STORAGE_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home/profiles/default/storage_state.json"
BASE_DIR = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/phu-quoc-tinh-hoa-hoi-tu")
VAULT_DIR = BASE_DIR / "research_vault"

QUERIES = [
    {
        "file": "11_global_elite_attraction_framework_and_prerequisites.md",
        "title": "Báo Cáo Chuyên Sâu: Khung Tiêu Chuẩn & 5 Điều Kiện Tiên Quyết Để Thu Hút Giới Tinh Hoa Toàn Cầu (Global Elites & Talent Attraction Prerequisites)",
        "prompt": """
        Phân tích chuyên sâu và toàn diện: Muốn thu hút và giữ chân giới tinh hoa toàn cầu (UHNWI, tỷ phú, nhà khoa học, giáo sư, tổng công trình sư, các nhà quản lý quỹ và Family Offices), một quốc gia/đặc khu bắt buộc phải đáp ứng những tiêu chuẩn và điều kiện tiên quyết nào?
        Bóc tách 5 trụ cột cốt lõi:
        1. Thể chế & Quyền tài sản: Hệ thống pháp luật dự đoán được (Common Law / Civil Law linh hoạt), bảo vệ tài sản tư nhân, tòa án/trọng tài quốc tế độc lập (như SIAC).
        2. Đòn bẩy tài khóa & Dòng vốn: Thuế thu nhập cá nhân cạnh tranh (0% - 15%), miễn thuế thặng dư vốn/cổ tức, tự do luân chuyển tài khoản vốn, khung pháp lý cho Family Offices.
        3. Hạ tầng mềm sống còn (Giáo dục & Y tế): Hệ thống trường liên cấp quốc tế K-12 chuẩn IB/Cambridge (để con cái giới tinh hoa theo học) và Bệnh viện quốc tế đạt chuẩn JCI (Joint Commission International).
        4. Môi trường sống & Phong cách sống thượng lưu: Sinh thái nguyên bản, an ninh cá nhân tối cao, hạ tầng hàng không tư nhân (VIP/FBO terminal), bến du thuyền (Marina), câu lạc bộ thể thao cao cấp (Golf, Yacht club).
        5. Đột phá thị thực (Visa): Golden Visa, Digital Nomad Visa, Thẻ cư trú dài hạn 10-15 năm không rào cản hành chính.
        Trình bày chuyên sâu với số liệu, bảng biểu và dẫn chứng cụ thể.
        """
    },
    {
        "file": "12_international_benchmarks_deep_dive_dubai_singapore_monaco.md",
        "title": "Đối Sánh Toàn Cầu: Phân Tích Chuyên Sâu 3 Thánh Địa Thu Hút Tinh Hoa (Dubai DIFC, Singapore GIP/ONE Pass, Monaco)",
        "prompt": """
        Bóc tách chi tiết chiến lược và cơ chế vận hành của 3 mô hình thành công nhất thế giới trong việc thu hút giới tinh hoa, dòng tiền và chất xám toàn cầu:
        1. Dubai (UAE):
           - Khung pháp lý riêng biệt tại Trung tâm Tài chính Quốc tế Dubai (DIFC) với Tòa án độc lập áp dụng Thông luật Anh (DIFC Courts).
           - Chính sách Golden Visa 10 năm (không cần nhà bảo lãnh), 0% thuế TNCN và thuế thặng dư vốn.
           - Sự bùng nổ của các văn phòng gia đình (Family Offices) và đô thị sang trọng.
        2. Singapore:
           - Chương trình Nhà đầu tư Toàn cầu (Global Investor Programme - GIP) cấp thẻ thường trú nhân (PR) khi đầu tư 10-25 triệu SGD vào quỹ/family office.
           - Thị thực nhân tài hàng đầu (ONE Pass - Overseas Networks & Expertise Pass) và Tech.Pass.
           - Hệ thống quản lý tài sản Wealth Management (>1.500 Family Offices), uy tín của Trọng tài SIAC, các trường quốc tế UWCSEA/SAS và y tế Mount Elizabeth/Johns Hopkins.
        3. Monaco:
           - Thiên đường thuế 0%, tỷ lệ an ninh cảnh sát trên đầu người cao nhất thế giới, bến du thuyền Port Hercules và câu lạc bộ Yacht Club de Monaco, dịch vụ ngân hàng tư nhân (Private Banking) bảo mật.
        So sánh các ưu thế và bài học cốt lõi cho một đặc khu mới nổi.
        """
    },
    {
        "file": "13_education_healthcare_pilots_jeju_and_hainan_boao.md",
        "title": "Đối Sánh Hải Đảo Chuyên Biệt: Mô Hình Đô Thị Giáo Dục Jeju JDC & Khu Thí Điểm Y Tế Boao Lecheng Hải Nam",
        "prompt": """
        Phân tích chuyên sâu 2 mô hình đặc thù hải đảo châu Á thành công trong việc tạo ra 'Hạ tầng mềm' hút gia đình tinh hoa và chuyên gia quốc tế:
        1. Thành phố Quốc tế Tự do Jeju (Hàn Quốc - Jeju JDC):
           - Dự án Đô thị Giáo dục Quốc tế Jeju (Jeju Global Education City): Thu hút 4 trường tư thục danh tiếng hàng đầu thế giới (North London Collegiate School - NLCS, Branksome Hall Asia - BHA, Korea International School - KIS, St. Johnsbury Academy - SJA). Cơ chế cho phép trường nước ngoài hoạt động và chuyển lợi nhuận về nước.
           - Cơ chế bất động sản gắn liền visa cư trú F-2 và định cư vĩnh viễn F-5 cho nhà đầu tư nước ngoài.
           - Dự án Đô thị Y tế Quốc tế Jeju (Jeju Healthcare Town).
        2. Cảng Thương mại Tự do Hải Nam (Trung Quốc):
           - Khu Thí điểm Du lịch Y tế Quốc tế Bác Ngao Lạc Thành (Boao Lecheng International Medical Tourism Pilot Zone): Cơ chế 'Cửa sổ đặc biệt' cho phép nhập khẩu thuốc và thiết bị y tế tiên tiến của Mỹ/châu Âu trước khi FDA Trung Quốc cấp phép.
           - Chính sách thuế TNCN trần 15% cho nhân tài cao cấp và thu hút các viện nghiên cứu, chuyên gia y khoa hàng đầu thế giới.
        Rút ra các bài học thực tiễn cho Phú Quốc.
        """
    },
    {
        "file": "14_vietnam_phu_quoc_strategic_gap_analysis_and_action_roadmap.md",
        "title": "Chiến Lược Hành Động: Khoảng Trống Tử Huyệt Của Phú Quốc & Lộ Trình 5 Trụ Cột Để Việt Nam Đạt Tiêu Chuẩn Giới Tinh Hoa",
        "prompt": """
        Phân tích thực trạng, định hướng phát triển và lộ trình chính sách của Phú Quốc nhằm thu hút giới tinh hoa và chất xám toàn cầu:
        1. Phú Quốc ĐANG CÓ GÌ:
           - Vị thế địa chính trị ngã tư hàng hải Vịnh Thái Lan.
           - Môi trường sinh thái độc bản (63% rừng quốc gia, biển đảo nguyên sơ).
           - Hạ tầng vật lý 137.000 tỷ APEC 2027 (Sân bay T2 đón Boeing 787/A350, đường sắt nhẹ TOD LRT 9.000 tỷ, MICE 21.860 tỷ, Khu phi thuế quan IPPG 6.830 tỷ).
           - Bước đột phá đầu tiên: Nghị định 221/2025/NĐ-CP (Golden Visa 15 năm, miễn 100% thuế TNCN 5 năm đầu, giảm 50% 5 năm sau).
        2. KHOẢNG TRỐNG TỬ HUYỆT (The Missing Links):
           - Thiếu cụm trường liên cấp quốc tế K-12 chuẩn IB/Cambridge cho con cái chuyên gia.
           - Thiếu bệnh viện quốc tế tư nhân đạt chuẩn JCI.
           - Thiếu khung pháp lý cho Family Offices, kiểm soát ngoại hối còn chặt chẽ.
           - Thiếu tòa án trọng tài thương mại quốc tế độc lập (SIAC).
           - Nguy cơ ô nhiễm môi trường (rác thải sinh hoạt bãi Đồng Cây Sao, thiếu nước ngọt mùa khô).
        3. LỘ TRÌNH HÀNH ĐỘNG 5 TRỤ CỘT CHO VIỆT NAM / PHÚ QUỐC:
           - Trụ cột 1: Mở Sandbox thể chế cho phép mở trường học và bệnh viện 100% vốn nước ngoài vì lợi nhuận (học Jeju + Boao Lecheng).
           - Trụ cột 2: Thiết lập Khu Tài chính Đặc thù cho Family Offices & Quản lý tài sản (học Dubai DIFC / Singapore).
           - Trụ cột 3: Luật hóa Trọng tài Thương mại Quốc tế và cơ chế giải quyết tranh chấp Thông luật.
           - Trụ cột 4: Giữ vững lằn ranh sinh thái Đô thị Nén TOD (bảo tồn 63% rừng, điện rác Bãi Bổn, hồ Dương Đông 2).
           - Trụ cột 5: Chính sách chuyển đổi sinh kế và an sinh bản địa (nhà ở xã hội HDB, đào tạo nghề 5 sao cho ngư dân).
        Trình bày đanh thép, số liệu rõ ràng, văn phong chuyên gia chính sách.
        """
    }
]

async def main():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"=== BẮT ĐẦU TRÍCH XUẤT 4 BÁO CÁO NGHIÊN CỨU SÂU VỀ GIỚI TINH HOA TOÀN CẦU ===")
    
    async with NotebookLMClient.from_storage(STORAGE_PATH) as client:
        email = await client.get_account_email()
        print(f"Đã kết nối NotebookLM thành công: {email}\n")
        
        for idx, item in enumerate(QUERIES, start=1):
            out_file = VAULT_DIR / item["file"]
            title = item["title"]
            prompt = item["prompt"].strip()
            
            print(f"[{idx}/{len(QUERIES)}] Đang truy vấn chuyên sâu: {title}...")
            
            try:
                res = await client.chat.ask(
                    notebook_id=NOTEBOOK_ID,
                    question=prompt
                )
                
                answer = res.answer if hasattr(res, "answer") else str(res)
                
                md_content = f"# {title}\n\n"
                md_content += f"> **Mã chủ đề:** `VAULT_ELITE_{idx:02d}`  \n"
                md_content += f"> **Nguồn trích xuất:** Google NotebookLM Master Notebook (`{NOTEBOOK_ID}`)  \n"
                md_content += f"> **Phương pháp:** Direct RPC Ingestion & Batch Extraction (`notebooklm-py`)  \n\n"
                md_content += f"## 1. Yêu Cầu Truy Vấn (Research Prompt)\n\n"
                md_content += f"```text\n{prompt}\n```\n\n"
                md_content += f"---\n\n"
                md_content += f"## 2. Báo Cáo Phân Tích & Dữ Liệu Thực Chứng (Grounded Insights)\n\n"
                md_content += f"{answer}\n\n"
                
                if hasattr(res, "references") and res.references:
                    md_content += f"---\n\n## 3. Danh Mục Nguồn Trích Dẫn Thực Chứng (Citations & Sources)\n\n"
                    for ref_idx, ref in enumerate(res.references, start=1):
                        source_id = getattr(ref, "source_id", "N/A")
                        quote = getattr(ref, "quote", "") or getattr(ref, "text", "")
                        title_src = getattr(ref, "source_title", "") or getattr(ref, "title", "Tài liệu NotebookLM")
                        md_content += f"- **[{ref_idx}] {title_src}** (Source ID: `{source_id}`)\n"
                        if quote:
                            md_content += f"  > *\"{quote.strip()}\"*\n"
                
                out_file.write_text(md_content, encoding="utf-8")
                print(f"  [+] Đã lưu thành công: {item['file']} ({len(md_content.encode('utf-8'))} bytes)")
                
            except Exception as e:
                print(f"  [!] Lỗi khi truy vấn {title}: {e}")
                
            await asyncio.sleep(2)
            
    print(f"\n=== HOÀN TẤT TRÍCH XUẤT 4 BÁO CÁO CHUYÊN SÂU TINH HOA TOÀN CẦU ===")

if __name__ == "__main__":
    asyncio.run(main())
