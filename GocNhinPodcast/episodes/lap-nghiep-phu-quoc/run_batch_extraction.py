import asyncio
import json
import os
from pathlib import Path
from notebooklm import NotebookLMClient

NOTEBOOK_ID = "b14b9d2f-6f32-491a-b7dd-c5638817dc71"
STORAGE_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home/profiles/default/storage_state.json"
BASE_DIR = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc")
VAULT_DIR = BASE_DIR / "research_vault"

QUERIES = [
    {
        "file": "01_living_costs_and_island_tax.md",
        "title": "Báo Cáo 01: Chi Phí Sinh Hoạt, Giá Thuê Trọ & Chỉ Số 'Thuế Hải Đảo' (Island Tax) Tại Phú Quốc 2025–2026",
        "prompt": """
        Phân tích chi tiết, định lượng và toàn diện về chi phí sinh hoạt tại Đặc khu Phú Quốc giai đoạn 2025 - 2026:
        1. Khảo sát giá thuê phòng trọ bình dân và phòng tiện nghi tại các khu vực Dương Đông, An Thới, Dương Tơ, Cửa Cạn.
        2. Chi phí sinh hoạt hàng ngày: giá thực phẩm (rau củ, thịt cá, hải sản), chi phí điện nước, cước viễn thông, đi lại so với TP.HCM và Hà Nội.
        3. Phân tích bản chất và quy mô của "Thuế hải đảo" (Island Tax): Chi phí vận chuyển đường biển/hàng không đẩy giá vốn hàng bán (COGS) lên bao nhiêu %?
        4. Tổng ngân sách sinh hoạt tối thiểu hàng tháng của một người độc thân và một gia đình nhỏ để tồn tại ổn định trên đảo.
        Trình bày bằng số liệu cụ thể, bảng biểu so sánh và trích dẫn thực tế.
        """
    },
    {
        "file": "02_commercial_rental_market.md",
        "title": "Báo Cáo 02: Thị Trường Thuê Mặt Bằng Kinh Doanh, Kiot & Shophouse Tại Phú Quốc 2025–2026",
        "prompt": """
        Mổ xẻ thực trạng thị trường cho thuê mặt bằng thương mại tại Phú Quốc hiện nay:
        1. Mặt bằng kinh doanh nhỏ, kiot chợ, quán ăn ven đường: giá thuê trung bình, biến động giá qua các năm.
        2. Shophouse tại các khu đô thị lớn và mặt tiền các trục đường huyết mạch (ĐT.975, Trần Hưng Đạo, 30/4): giá thuê thực tế, tỷ lệ lấp đầy, các căn bỏ hoang.
        3. Rào cản vốn ban đầu: Quy định về tiền đặt cọc (1-6 tháng), chu kỳ thanh toán (3-6 tháng/lần), chi phí cải tạo hoàn thiện thô.
        4. Rủi ro pháp lý hợp đồng thuê: thời hạn cam kết, điều khoản tăng giá thuê hàng năm, rủi ro thu hồi đất hoặc tranh chấp pháp lý mặt bằng.
        """
    },
    {
        "file": "03_labor_market_wages_and_benefits.md",
        "title": "Báo Cáo 03: Cơ Cấu Thị Trường Lao Động, Thang Lương & Chế Độ Đãi Ngộ Tại Các Resort 4-5 Sao Phú Quốc",
        "prompt": """
        Phân tích chuyên sâu về thị trường tuyển dụng và việc làm tại các tập đoàn lớn và resort 4-5 sao ở Phú Quốc:
        1. Thang lương chi tiết: Lao động phổ thông (buồng phòng, phục vụ, bảo vệ, cây xanh); Nhân viên chuyên môn (lễ tân, kỹ thuật cơ điện, đầu bếp, pha chế); Quản lý cấp trung và cấp cao.
        2. Cơ cấu thu nhập thực tế: Lương cứng + Phí phục vụ (Service charge) + Tiền tip. Mức độ biến động của service charge giữa mùa cao điểm và mùa thấp điểm.
        3. Chính sách đãi ngộ sống còn: Tỷ lệ các resort bao ăn ở (ký túc xá nhân viên, xe đưa đón); giá trị của gói phúc lợi này đối với người lao động ngoại tỉnh.
        4. Lợi thế cạnh tranh của lao động đa ngôn ngữ: Nhu cầu và mức chênh lệch lương đối với nhân sự thông thạo tiếng Hàn, tiếng Trung, tiếng Nga, tiếng Anh.
        5. Tỷ lệ nhảy việc (turnover rate) và lý do người lao động rời đảo sau 1-2 năm làm việc.
        """
    },
    {
        "file": "04_seasonal_monsoon_impact.md",
        "title": "Báo Cáo 04: Cơn Ác Mộng Mùa Mưa (Gió Mùa Tây Nam) & Rủi Ro Đứt Gãy Dòng Tiền F&B / Homestay",
        "prompt": """
        Phân tích quy luật khắc nghiệt của chu kỳ thời tiết và mùa vụ kinh doanh tại Phú Quốc:
        1. Đặc điểm mùa mưa (từ tháng 5 đến tháng 10): Tần suất mưa, sóng biển, gió mùa Tây Nam, số ngày tàu cao tốc và tour đảo buộc phải ngừng hoạt động.
        2. Mức độ sụt giảm lượng khách du lịch và doanh thu của các hộ kinh doanh cá thể ngoài trời (nhà hàng, quán cafe ngắm hoàng hôn, homestay, tour ca nô).
        3. Bài toán "6 tháng cày bù 6 tháng nhịn": Áp lực chi phí mặt bằng cố định trong mùa mưa khi doanh thu chạm đáy.
        4. Tỷ lệ các cơ sở khởi nghiệp nhỏ lẻ phải đóng cửa, sang nhượng hoặc phá sản sau 1 mùa mưa; nguyên nhân đứt gãy dòng tiền dự phòng.
        """
    },
    {
        "file": "05_all_inclusive_resorts_vs_local_smbs.md",
        "title": "Báo Cáo 05: Sự Thống Trị Của Integrated Resorts (Hệ Sinh Thái Khép Kín) & Bẫy Hoa Hồng Taxi",
        "prompt": """
        Bóc tách xung đột thị phần giữa các đại tập đoàn và hộ kinh doanh dịch vụ độc lập:
        1. Khái niệm và thực tế mô hình "Integrated Resorts" (Khu nghỉ dưỡng tích hợp khép kín) tại Bắc đảo và Nam đảo (Grand World, Sun World, Corona Casino...): Khách quốc tế đi tour trọn gói (all-inclusive), ăn ngủ chơi nội khu, tiền không chảy ra ngoài cộng đồng dân sinh.
        2. Bẫy hoa hồng và chi phí trung gian (Kickback Trap): Thực trạng các quán ăn, cửa hàng ngoài phố phải chiết khấu từ 20% đến 40% cho tài xế taxi, hướng dẫn viên du lịch để dẫn khách đến.
        3. Hậu quả đối với người kinh doanh: Đội giá bán khiến khách chê đắt, hoặc giảm chất lượng dịch vụ dẫn tới mất uy tín lâu dài; biên lợi nhuận ròng thực tế còn lại bao nhiêu?
        """
    },
    {
        "file": "06_b2b_and_supply_chain_opportunities.md",
        "title": "Báo Cáo 06: Cơ Hội Lập Nghiệp Chuỗi Cung Ứng B2B & Dịch Vụ Phụ Trợ Cho Các Tổ Hợp Nghỉ Dưỡng 5 Sao",
        "prompt": """
        Nghiên cứu các ngách kinh doanh B2B (Business-to-Business) bền vững và giàu tiềm năng tại Phú Quốc:
        1. Cung ứng nông sản sạch, thực phẩm tươi sống, hải sản đạt chuẩn an toàn vệ sinh cho bếp ăn các resort lớn.
        2. Dịch vụ giặt ủi công nghiệp, vệ sinh công nghiệp, bảo dưỡng hệ thống điều hòa, điện lạnh và chống ăn mòn muối biển cho các khách sạn.
        3. Cung ứng vật liệu xây dựng, cây xanh cảnh quan và dịch vụ logistics kho bãi phục vụ các dự án lớn hướng tới APEC 2027.
        4. Điều kiện, tiêu chuẩn và rào cản gia nhập mạng lưới nhà cung ứng của các tập đoàn (Sun Group, Vingroup, BIM, IHG, Marriott).
        """
    },
    {
        "file": "07_permanent_resident_services_2040.md",
        "title": "Báo Cáo 07: Đón Đầu Quy Hoạch 700.000 Dân Thường Trú 2040 — Cơ Hội Dịch Vụ Đô Thị & An Cư",
        "prompt": """
        Phân tích cơ hội kinh doanh và nghề nghiệp đón đầu sự chuyển dịch dân cư theo Quyết định 150/QĐ-TTg (Quy hoạch Phú Quốc 2040):
        1. Mục tiêu tăng trưởng dân số từ 150.000 dân hiện tại lên 700.000 dân thường trú vào năm 2040: Nhu cầu về hạ tầng xã hội đô thị.
        2. Các ngành dịch vụ thiết yếu cho cư dân: Giáo dục mầm non, trường liên cấp, trung tâm ngoại ngữ, chăm sóc sức khỏe ban đầu, phòng khám gia đình.
        3. Dịch vụ bán lẻ, siêu thị tiện lợi, sửa chữa kỹ thuật và đời sống hàng ngày tại các khu đô thị mới (Meyhomes Capital, khu tái định cư An Thới, Dương Đông mở rộng).
        4. Tiềm năng và độ ổn định doanh thu của nhóm dịch vụ phục vụ cư dân thường trú so với nhóm dịch vụ phụ thuộc du khách vãng lai.
        """
    },
    {
        "file": "08_institutional_legal_framework.md",
        "title": "Báo Cáo 08: Khung Pháp Lý Đặc Khu Phú Quốc, Nghị Quyết 41/2026/QH16, FTZ & Bảng Giá Đất Mới 2026",
        "prompt": """
        Phân tích tác động của các thay đổi thể chế và chính sách mới nhất lên môi trường kinh doanh Phú Quốc:
        1. Vị thế mới: Phú Quốc trở thành Đặc khu kinh tế trực thuộc tỉnh An Giang mới (theo Nghị quyết 202/2025/QH15 và 1654/NQ-UBTVQH15).
        2. Nghị quyết số 41/2026/QH16 của Quốc hội: Các cơ chế đặc thù tháo gỡ cho dự án APEC 2027 và việc phân cấp thủ tục hành chính.
        3. Đề án thí điểm Khu thương mại tự do (FTZ) 10 năm: Chính sách thuế, quản lý hộ kinh doanh cá thể, hoàn thuế VAT.
        4. Tác động của việc áp dụng Bảng giá đất mới 2026 sát giá thị trường: Chi phí thuê đất, tiền sử dụng đất tăng lên ảnh hưởng ra sao đến chi phí đầu vào của doanh nghiệp và giá thuê mặt bằng?
        5. Quy định siết chặt kiểm tra nguồn gốc đất, ngắt tiện ích công trình sai phạm của chính quyền địa phương.
        """
    },
    {
        "file": "09_international_island_benchmarks.md",
        "title": "Báo Cáo 09: Bài Học Quốc Tế Về Lập Nghiệp Hải Đảo — Jeju, Bali, Okinawa & Phuket",
        "prompt": """
        Nghiên cứu đối sánh quốc tế về hiện tượng di cư lập nghiệp từ đất liền ra các đảo du lịch - đặc khu:
        1. Đảo Jeju (Hàn Quốc): Làn sóng người trẻ Seoul ra Jeju mở cafe/homestay và tỷ lệ vỡ mộng sau 3 năm; sự xung đột văn hóa giữa người bản địa và người mới đến (mainlander vs islander).
        2. Bali (Indonesia): Sự bùng nổ của Digital Nomads và doanh nghiệp ngoại kiều; bài toán cạnh tranh không gian sống, hạ tầng quá tải và chính sách siết visa/thuế của chính phủ.
        3. Okinawa (Nhật Bản) & Phuket (Thái Lan): Cách thức chính quyền hỗ trợ cư dân định cư, đào tạo nghề và bảo vệ chuỗi cung ứng địa phương.
        4. Những bài học kinh nghiệm sâu sắc nhất có thể áp dụng cho người chuẩn bị vào Phú Quốc lập nghiệp.
        """
    },
    {
        "file": "10_steelman_audit_and_survival_playbook.md",
        "title": "Báo Cáo 10: Phản Biện Đối Lập Mạnh Nhất (Steelman Audit) & Cẩm Nang Kỷ Luật Sinh Tồn Tại Phú Quốc",
        "prompt": """
        Tổng hợp phản biện đối lập sắc bén và xây dựng cẩm nang sinh tồn cho người lập nghiệp:
        1. Bảng 5 ngộ nhận chết người nhất của người mang vốn và hy vọng ra Phú Quốc:
           - Ngộ nhận 1: "Cứ đông khách du lịch là kinh doanh gì cũng thắng."
           - Ngộ nhận 2: "Phú Quốc đang sốt đất và hạ tầng APEC nên giá thuê sẽ tăng mãi."
           - Ngộ nhận 3: "Chỉ cần quán đẹp, view hoàng hôn là có khách tự tìm đến."
           - Ngộ nhận 4: "Không cần vốn dự phòng vì dòng tiền sẽ xoay vòng ngay tháng đầu."
           - Ngộ nhận 5: "Làm việc ở đảo thì ngày nào cũng được nghỉ dưỡng như đi du lịch."
        2. Bản quy tắc kỷ luật tài chính và vận hành (Survival Playbook):
           - Kỷ luật vốn dự phòng: Bắt buộc chuẩn bị dòng tiền đủ bù lỗ tối thiểu 6-9 tháng (bao gồm trọn vẹn 1 mùa mưa).
           - Chiến lược lựa chọn địa điểm: Phân biệt bãi biển mùa khô (Tây) và mùa mưa (Đông).
           - Tối ưu hóa mô hình: Tự động hóa, cắt giảm chi phí trung gian, tập trung vào chất lượng dịch vụ lõi.
        3. Kết luận đanh thép: Ai nên vào Phú Quốc và Ai tuyệt đối KHÔNG NÊN vào Phú Quốc lập nghiệp lúc này?
        """
    }
]

async def main():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    print("=== BẮT ĐẦU TRÍCH XUẤT 10 BÁO CÁO NGHIÊN CỨU SÂU: LẬP NGHIỆP PHÚ QUỐC 2026 ===")
    
    async with NotebookLMClient.from_storage(STORAGE_PATH) as client:
        email = await client.get_account_email()
        print(f"Đã kết nối NotebookLM thành công: {email}")
        print(f"Master Notebook ID: {NOTEBOOK_ID}\n")
        
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
                md_content += f"> **Mã chủ đề:** `VAULT_PQ_CAREER_{idx:02d}`  \n"
                md_content += f"> **Nguồn trích xuất:** Google NotebookLM Master Notebook (`{NOTEBOOK_ID}`)  \n"
                md_content += f"> **Phương pháp:** Direct RPC Ingestion & Batch Extraction (`notebooklm-py`)  \n"
                md_content += f"> **Thời điểm trích xuất:** Tháng 09/2026  \n\n"
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
            
    print("\n=== HOÀN TẤT TRÍCH XUẤT 10 BÁO CÁO CHUYÊN SÂU LẬP NGHIỆP PHÚ QUỐC ===")

if __name__ == "__main__":
    asyncio.run(main())
