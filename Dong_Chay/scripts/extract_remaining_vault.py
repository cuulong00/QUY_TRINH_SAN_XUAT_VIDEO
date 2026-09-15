import asyncio
import os
import subprocess
from notebooklm.client import NotebookLMClient

NOTEBOOK_ID = "477ee042-ce17-4ef1-9f53-9cbd97316e78"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/philipines-bi-kich-gia-toc/research_vault"

REMAINING = [
    {
        "filename": "05_rice_crisis_and_agricultural_abandonment.md",
        "title": "Khủng Hoảng Lúa Gạo & Nghịch Lý Cái Nôi IRRI Đói Ăn",
        "prompt": """Phân tích chuyên sâu từ các tài liệu nguồn trong notebook về:
1. Nghịch lý Viện Nghiên cứu Lúa Quốc tế (IRRI) tại Los Baños (Laguna): Nơi khai sinh giống lúa thần kỳ IR8 trong Cách mạng Xanh nhưng quốc gia sở tại lại là nước nhập khẩu gạo lớn nhất hành tinh.
2. Số liệu nhập khẩu gạo kỷ lục: Dự báo của USDA năm 2026 (5.0 - 5.7 triệu tấn), năm 2024 (3.39 triệu tấn); vai trò của Việt Nam cung cấp 74% - 77% tổng lượng gạo nhập khẩu.
3. Nguyên nhân cấu trúc hủy diệt nông nghiệp: Sự thất bại của Đạo luật Cải cách Điền địa Toàn diện (CARP), đất đai manh mún, địa chủ Hacienda chuyển đổi đất thành bất động sản, thiếu hụt đầu tư thủy lợi và kho lạnh.
4. Chi phí sản xuất: Tại sao trồng lúa ở Philippines đắt hơn 40% - 50% so với Đồng bằng Sông Cửu Long Việt Nam?
5. Tác động lạm phát: Gạo chiếm tỷ trọng lớn trong giỏ hàng tiêu dùng của người nghèo, biến an ninh lương thực thành ngòi nổ bất ổn xã hội.
Trích dẫn số liệu từ USDA, Cục Trồng trọt Philippines (BPI), DA, IRRI."""
    },
    {
        "filename": "06_bpo_under_ai_siege_and_ofw_remittance_loop.md",
        "title": "Bão AI Đe Dọa BPO & Vòng Lặp Kiều Hối Tiêu Dùng",
        "prompt": """Phân tích chuyên sâu từ các tài liệu nguồn trong notebook về:
1. Hai trụ cột kinh tế dịch vụ: Kiều hối OFW (đạt kỷ lục 39.62 tỷ USD năm 2025, ~7.3% - 9% GDP) và Doanh thu ngành IT-BPM/BPO (40 tỷ USD, sử dụng 1.9 triệu lao động).
2. 'Căn bệnh Hà Lan' phiên bản dịch vụ: Dòng ngoại tệ kiều hối làm định giá cao đồng Peso, bóp nghẹt hàng xuất khẩu nội địa; tiền kiều hối chảy thẳng vào các chuỗi đại siêu thị SM/Ayala để tiêu dùng hàng nhập khẩu thay vì đầu tư nhà xưởng.
3. Cơn địa chấn Generative AI và Voice AI Agents (2025-2026): Tác động hủy diệt lên các vị trí tổng đài viên cấp 1 và cấp 2 (L1/L2) xử lý chăm sóc khách hàng và nhập liệu.
4. Phản ứng của IBPAP (Roadmap Refresh 2026): Việc hạ thấp mục tiêu tăng trưởng việc làm 2028, nỗ lực chuyển đổi sang KPO (Knowledge Process Outsourcing), và khoảng cách giữa tốc độ sa thải của AI và tốc độ tái đào tạo kỹ năng.
Trích dẫn báo cáo của IBPAP, BSP, World Bank, ILO."""
    },
    {
        "filename": "07_sovereign_debt_cliff_and_maharlika_fund.md",
        "title": "Quả Bom Nợ Công 19.39 Nghìn Tỷ Peso & Quỹ Maharlika",
        "prompt": """Phân tích chuyên sâu từ các tài liệu nguồn trong notebook về:
1. Tình trạng nợ công quốc gia: Chạm mốc kỷ lục 19.39 nghìn tỷ Peso (~340 tỷ USD) vào tháng 7/2026; dự báo tăng lên 21.48 nghìn tỷ Peso vào năm 2027.
2. Tỷ lệ Nợ công/GDP: Đạt 66% trong Quý 2/2026 — mức đỉnh cao nhất trong 22 năm qua; áp lực trả nợ đè nặng lên ngân sách phát triển hạ tầng.
3. Tranh cãi Quỹ Đầu tư Quốc gia Maharlika (MIF - Đạo luật RA 11954): Cấu trúc góp vốn từ ngân hàng nhà nước (LandBank 50 tỷ Peso, DBP 25 tỷ Peso), lo ngại rút cạn dự trữ thanh khoản an toàn của hệ thống ngân hàng phục vụ nông nghiệp/phát triển.
4. Rủi ro quản trị và xung đột lợi ích: Mối lo ngại về việc Quỹ Maharlika biến thành công cụ tài trợ cho các dự án thân hữu của phe cánh chính trị miền Bắc.
Trích dẫn số liệu của Bureau of the Treasury (BTr), Department of Finance (DOF), báo cáo thẩm định kinh tế."""
    },
    {
        "filename": "08_dynastic_civil_war_marcos_vs_duterte.md",
        "title": "Nội Chiến Vương Triều: Marcos Jr. vs Phe Duterte (Luận Tội & ICC)",
        "prompt": """Phân tích chuyên sâu từ các tài liệu nguồn trong notebook về:
1. Sự sụp đổ của liên minh 'UniTeam 2022': Từ sự bắt tay vụ lợi giữa Marcos Jr. (miền Bắc) và Sara Duterte (Mindanao miền Nam) đến cuộc đối đầu sinh tử trước thềm bầu cử Tổng thống 2028.
2. Phiên tòa luận tội Phó Tổng thống Sara Duterte: Hạ viện thông qua ngày 11/5/2026, Thượng viện mở phiên tòa ngày 6/7/2026; các cáo buộc về quỹ bảo mật (612.5 triệu Peso tại DepEd/OVP), tham nhũng, đe dọa ám sát Tổng thống; lệnh bắt giữ ngày 4/9/2026 và việc nộp bảo lãnh 360.000 Peso ngày 5/9/2026.
3. Số phận pháp lý của cựu Tổng thống Rodrigo Duterte: Lệnh bắt giữ của Tòa án Hình sự Quốc tế (ICC) ngày 7/3/2025, chiến dịch bắt giữ Oplan Tugis tại sân bay NAIA ngày 11/3/2025 và di lý sang The Hague; phiên xét xử chính thức ngày 30/11/2026 về tội ác chống lại loài người trong chiến tranh ma túy.
4. Tác động làm tê liệt thể chế và bộ máy công quyền: Sự phân rã sâu sắc giữa phe thân Mỹ ở Manila và phe bình dân miền Nam thân Bắc Kinh.
Trích dẫn hồ sơ Thượng viện Philippines, Tòa Tối cao, Tòa Sơ thẩm Quezon City, tài liệu ICC The Hague."""
    },
    {
        "filename": "10_systemic_synthesis_and_vietnam_comparison.md",
        "title": "Bản Tổng Hợp Toàn Cảnh & Ma Trận Đối Soát Sống Còn Với Việt Nam",
        "prompt": """Tổng hợp vĩ mô toàn diện từ toàn bộ các nguồn tài liệu trong notebook:
1. Bức tranh toàn cảnh về 'Đứa trẻ dân số vàng còi cọc': Mối quan hệ nhân quả hữu cơ giữa Căn bệnh nhảy cóc công nghiệp -> Độc quyền địa tô 100 gia tộc -> Giá điện Meralco cao nhất ASEAN -> Khủng hoảng nhập khẩu gạo IRRI -> Bão AI đe dọa BPO & kiều hối -> Nợ công 19.39T Peso -> Nội chiến Marcos vs Duterte -> Con chốt tiền đồn EDCA Biển Đông.
2. Ma trận đối soát 6 chiều với Việt Nam (2024-2026):
   - Công nghiệp chế tạo: Chế tạo VN ~25% GDP vs Philippines <18% GDP.
   - Giá điện sản xuất: VN 0.07-0.09 USD/kWh vs Philippines 0.25 USD/kWh.
   - An ninh lương thực: VN xuất khẩu gạo hàng đầu vs Philippines nhập khẩu số 1 thế giới (VN nuôi 75% thị phần gạo Phi).
   - Nợ công: VN ~37% GDP vs Philippines 66% GDP.
   - Dân số: Cùng dân số vàng nhưng VN tận dụng thành công xưởng sản xuất, Philippines xuất khẩu lao động.
   - Ngoại giao: Cây tre độc lập tự chủ vs Đặt cược một phía vào đồng minh quân sự.
3. 3 Bài học chiến lược sống còn cho các quốc gia đang phát triển: Giá trị của công nghiệp chế tạo, kiểm soát hạ tầng thiết yếu và độc lập tự chủ địa chính trị.
Tổng hợp bảng số liệu so sánh đanh thép, khách quan, giàu sức thuyết phục."""
    }
]

def refresh_cookies():
    subprocess.run([
        ".venv/bin/notebooklm", "login",
        "--browser-cookies", "chrome",
        "--account", "duongtt84@gmail.com"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

async def extract_remaining():
    print("=== TIẾP TỤC TRÍCH XUẤT 5 CHUYÊN ĐỀ CÒN LẠI VÀO RESEARCH_VAULT ===")
    
    for idx, item in enumerate(REMAINING, 1):
        fname = item["filename"]
        ftitle = item["title"]
        fprompt = item["prompt"]
        outpath = os.path.join(OUTPUT_DIR, fname)
        
        print(f"\n[{idx}/5] 📝 Đang trích xuất: {ftitle} -> {fname}...")
        refresh_cookies()
        
        try:
            async with NotebookLMClient.from_storage() as client:
                res = await client.chat.ask(NOTEBOOK_ID, fprompt)
                answer = res.answer
                
                with open(outpath, "w", encoding="utf-8") as f:
                    f.write(f"# {ftitle}\n\n")
                    f.write(f"<!--\nTRÍCH XUẤT NGUỒN GỐC RAG:\n- Master Notebook ID: {NOTEBOOK_ID}\n- Nguồn dữ liệu: 657 tài liệu Deep Research Google NotebookLM\n- Tài khoản: duongtt84@gmail.com\n-->\n\n")
                    f.write(answer)
                    f.write(f"\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC API từ 657 nguồn Deep Research*\n")
                
                print(f"    ✅ Hoàn tất trích xuất {fname} ({len(answer)} ký tự)!")
        except Exception as e:
            print(f"    ❌ Lỗi trích xuất {fname}: {e}")
            
        await asyncio.sleep(2)
        
    print("\n🎉 HOÀN TẤT TRÍCH XUẤT TOÀN BỘ 10/10 CHUYÊN ĐỀ VÀO RESEARCH_VAULT!")

if __name__ == "__main__":
    asyncio.run(extract_remaining())
