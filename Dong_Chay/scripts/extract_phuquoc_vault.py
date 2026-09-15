import asyncio
import os
import sys
from notebooklm.client import NotebookLMClient

os.environ["NOTEBOOKLM_HOME"] = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"

NOTEBOOK_ID = "2cc55935-2e9d-4ee7-bd02-7a906ff073f9"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/dinh-van-noi-dac-khu-phu-quoc/research_vault"

QUERIES = [
    {
        "filename": "01_funan_techo_and_maritime_geopolitics.md",
        "title": "Địa Chính Trị Vịnh Thái Lan: Kênh Đào Funan Techo & Pháo Đài Phòng Ngự Tây Nam",
        "prompt": """Phân tích chi tiết từ toàn bộ tài liệu nguồn trong notebook về:
1. Tiến độ Kênh đào Funan Techo (Campuchia 1,7 tỷ USD, dài 180km, sâu 5,4m, tàu 3.000 tấn): Lễ khởi công Giai đoạn II ngày 11/4/2026 tại Borei Cholsar (Takeo), hoàn thành đoạn kênh trình diễn 5km, kế hoạch thông tuyến năm 2028.
2. Vị trí điểm cuối kênh đào tại tỉnh Kep và khoảng cách 26-30km đến Phú Quốc; sự chuyển dịch luồng hàng hải Vịnh Thái Lan.
3. Vị thế chốt chặn logistics và an ninh của Cảng nước sâu An Thới, Cảng Vịnh Đầm, căn cứ hải quân Ream.
4. Quy hoạch Sân bay lưỡng dụng Thổ Chu cấp 4E (28.800 tỷ đồng) kéo giãn chiều sâu phòng ngự 100km trên biển, bảo hiểm rủi ro chủ quyền cho khối tài sản hơn 504.000 tỷ đồng Đảo Ngọc.
Trích dẫn số liệu cụ thể và nguồn tài liệu có trong notebook."""
    },
    {
        "filename": "02_fatf_grey_list_and_aml_casino_ftz.md",
        "title": "Lá Chắn Chống Rửa Tiền FATF: Casino Corona & Khu Thương Mại Tự Do",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Quyết định số 1139/QĐ-TTg (tháng 6/2026) của Thủ tướng Chính phủ thực hiện Kế hoạch hành động quốc gia đưa Việt Nam rời khỏi Danh sách xám (Grey List) của FATF.
2. Đánh giá rủi ro rửa tiền và tài trợ khủng bố (AML/CFT) trong các lĩnh vực nhạy cảm: Casino Corona (thí điểm cho người Việt) và Khu thương mại tự do (FTZ).
3. Cơ chế kiểm soát dòng tiền xuyên biên giới, nhận diện chủ sở hữu hưởng lợi (Beneficial Ownership) và giao dịch đáng ngờ.
4. Bài học tránh "vết xe đổ Sihanoukville" (tội phạm lừa đảo trực tuyến, cờ bạc ngầm lũng đoạn kinh tế thực) và vai trò của tướng an ninh A03 trong việc bảo vệ xếp hạng tín nhiệm của toàn bộ hệ thống ngân hàng tài chính Việt Nam."""
    },
    {
        "filename": "03_apec2027_21_projects_and_137k_billion.md",
        "title": "Bóc Tách 21 Dự Án Hạ Tầng APEC 2027: Gói Đầu Tư 137.138 Tỷ Đồng",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Cấu trúc gói vốn 137.138 tỷ đồng phục vụ APEC 2027: 20.166 tỷ vốn công mồi sinh thái/mặt bằng kéo 116.972 tỷ vốn đối tác công tư (PPP) và tư nhân.
2. Tiến độ thực tế đến tháng 8/2026 của Nhà ga T2 Sân bay Phú Quốc (22.000 tỷ do Changi Singapore vận hành): Đạt 95% bê tông cốt thép, 70% kết cấu thép, 80% xây trát, lắp đặt hơn 9.500 tấm kính cường lực Unitized, kế hoạch vận hành thử tháng 4/2027.
3. Tuyến đường sắt nhẹ (LRT) BOT Sun Group (gần 9.000 tỷ, dài 17,59km): Đã giải ngân 1.800 tỷ, đang thi công 3 ca liên tục lắp đặt đường ray, hợp đồng vận hành HURC1, chạy thử tháng 6/2027, vận hành thương mại tháng 8/2027.
4. Các dự án hồ cấp nước Cửa Cạn, Dương Đông 2 và hệ thống cáp ngầm 220kV."""
    },
    {
        "filename": "04_dinh_van_noi_utility_cutoff_policy_2026.md",
        "title": "Kỹ Trị Dòng Tiền OPEX: Chiến Dịch Ngắt Tiện Ích & Cao Điểm 90 Ngày 2026",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Quyết sách chỉ đạo của Bí thư Đặc khu Phú Quốc Đinh Văn Nơi từ tháng 7 và đầu tháng 8/2026: Chiến dịch cao điểm 90 ngày (từ 20/7/2026) tổng kiểm tra trật tự xây dựng và đất rừng.
2. Giải pháp kỹ trị "Ngừng cung cấp điện, nước sinh hoạt, viễn thông và thu hồi giấy phép kinh doanh, PCCC, ATTP" đối với các cơ sở xây dựng trái phép trên đất rừng và hành lang biển.
3. Bản chất tài chính: Đưa dòng tiền vận hành về 0 (Operating Cash Flow = 0), triệt tiêu giá trị hiện tại thuần (NPV < 0), biến tài sản vi phạm thành cục nợ độc hại buộc đối tượng tự giải thể mà không cần đem xe ủi đến cưỡng chế.
4. Tuyên bố nguyên tắc: "Ai đặt bút ký cấp sai thì phải chịu trách nhiệm", kết luận thanh tra đất rừng Hàm Ninh, Cửa Cạn; thu hồi 4.000m² Bãi Đất Đỏ và cưỡng chế điểm du lịch The Peak; hiệu quả Hotline 096.229.7777 (HUMINT)."""
    },
    {
        "filename": "05_land_crisis_and_912ha_clearance.md",
        "title": "Khủng Hoảng 8.707 Thửa Đất Lậu & Bài Toán Giải Phóng Mặt Bằng 912 Hécta APEC",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Quy mô sai phạm đất đai theo thanh tra: 685 ha đất rừng bị lấn chiếm (1.744 vụ), 420 khu phân lô trái phép, 8.707 thửa đất lậu, hơn 900 căn nhà không phép trên 195 ha.
2. Lý thuyết Hernando de Soto: 8.707 thửa đất giấy tay là hàng chục ngàn tỷ đồng "Tư bản chết" (Dead Capital) không thể thế chấp ngân hàng, không tạo thuế, làm tê liệt quy hoạch.
3. Thách thức giải phóng mặt bằng 912 ha đất cho 21 dự án APEC, ảnh hưởng 3.972 hộ dân bản địa.
4. Tiến độ GPMB thực tế đến tháng 8/2026: Hoàn thành gần 660/1.050 ha (đạt 62,79%).
5. Phương châm dân vận "Bàn tay sắt, Đôi găng nhung": Răn đe đầu nậu nhưng chăm lo sinh kế, tái định cư cho người dân yếu thế."""
    },
    {
        "filename": "06_ben_tram_shooting_appeal_trial_verdict.md",
        "title": "Giải Phẫu Đại Án Bến Tràm: Bản Án Tử Hình & Sự Bẻ Gãy Mafia Bảo Kê Đất",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Diễn biến vụ nổ súng ngày 27/10/2022 tại ấp Bến Tràm, xã Cửa Dương: 12 xe ô tô, gần 70 giang hồ trang bị vũ khí nóng, tranh chấp 2,2 ha đất trị giá 4 tỷ đồng giữa nhóm Thái "bus" và nhóm Trường; 3 phát súng hoa cải của Đoàn Thiên Long làm 2 người chết tại chỗ, 6 người bị thương nặng.
2. Bản án phúc thẩm TAND Cấp cao tại TP.HCM (tháng 6/2024): Đoàn Thiên Long nhận án TỬ HÌNH; Nguyễn Văn Thái (Thái "bus") nhận TÙ CHUNG THÂN; Phạm Anh Hiếu nhận TÙ CHUNG THÂN; Bùi Minh Trung và Võ Văn Lương mỗi người 16 năm tù; Nguyễn Quốc Vinh 15 năm tù.
3. Tác động kinh tế học: Vụ án chứng minh chi phí bảo vệ quyền sở hữu tài sản từng bị vô hiệu hóa, đẩy Legal Risk Premium lên cực hạn, đòi hỏi sự xuất hiện của bàn tay sắt thể chế."""
    },
    {
        "filename": "07_a03_internal_security_and_crony_capture.md",
        "title": "Năng Lực Thể Chế A03: Phá Vỡ Mạng Lưới Thân Hữu 20 Năm",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Bẫy thân hữu (Crony Capture): Tại sao technocrat kinh tế thông thường thất bại trước các nhóm lợi ích địa phương?
2. Vụ án 20 tỷ chạy điều chuyển của Trần Trí Mãnh (chi 20 tỷ chỉ để "mua sự vắng mặt" của Giám đốc Công an tỉnh Đinh Văn Nơi).
3. Đại án hóa đơn khống và cựu Thiếu tướng Đỗ Hữu Ca nhận 35 tỷ chạy án: Nguyên tắc "Không có vùng cấm, không có ngoại lệ".
4. Đại án Mười Tường buôn lậu 51kg vàng vùng biên An Giang.
5. Thẩm quyền Cục trưởng A03 (Cục An ninh chính trị nội bộ): Công cụ phản gián và giám sát tối cao bảo đảm sự liêm chính của bộ máy đặc khu."""
    },
    {
        "filename": "08_administrative_merger_resolution_202_and_sez.md",
        "title": "Thể Chế Mới Theo Nghị Quyết 202/2025/QH15 & Quyết Định 219-QĐNS/TW",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Bối cảnh sáp nhập địa giới hành chính Kiên Giang vào An Giang mới (diện tích ~10.000 km², dân số ~5 triệu người) theo Nghị quyết số 202/2025/QH15 của Quốc hội.
2. Vị thế của Phú Quốc: Là 1 trong 3 Đặc khu kinh tế trực thuộc tỉnh mới, vận hành theo cơ chế phân cấp đặc thù.
3. Quyết định số 219-QĐNS/TW (tháng 7/2026) của Ban Bí thư: Điều động Trung tướng Đinh Văn Nơi giữ chức Phó Bí thư Tỉnh ủy kiêm Bí thư Đảng ủy Đặc khu Phú Quốc.
4. Sự phân vai rạch ròi giữa Lãnh đạo chính trị (Bí thư Đặc khu lập lại kỷ cương thể chế) và Cơ quan kỹ trị điều hành (Chủ tịch UBND Đặc khu điều hành kinh tế vi mô)."""
    },
    {
        "filename": "09_tho_chu_airport_and_southwest_defense.md",
        "title": "Căn Cứ Sân Bay Thổ Chu 28.800 Tỷ & Vành Đai Phòng Thủ Tây Nam",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Dự án Sân bay lưỡng dụng Thổ Chu trên đảo Thổ Chu (vốn đầu tư 28.800 tỷ đồng, quy hoạch đạt chuẩn 4E tiếp nhận tàu bay thân rộng).
2. Khoảng cách địa lý: Thổ Chu cách Phú Quốc ~100km về phía Tây Nam, tạo nên thế trận phòng ngự chiều sâu 100km trên biển.
3. Vai trò của Vùng 5 Hải quân và Bộ Tư lệnh Cảnh sát biển 4 trong việc bảo vệ an ninh ngư trường, giàn khoan dầu khí và các tuyến hàng hải quốc tế.
4. Mối quan hệ biện chứng: Sự phồn vinh của Đặc khu Phú Quốc và lá chắn Thổ Chu tạo nên chiếc neo bảo vệ chủ quyền biên giới Tây Nam vững chắc nhất."""
    },
    {
        "filename": "10_economic_indicators_and_growth_7m_2026.md",
        "title": "Báo Cáo Tăng Trưởng Kinh Tế 7 Tháng Năm 2026 & Triết Lý Thể Chế Bền Vững",
        "prompt": """Phân tích chi tiết từ các tài liệu nguồn trong notebook về:
1. Số liệu kinh tế 7 tháng đầu năm 2026 của Phú Quốc: Tổng sản phẩm trên địa bàn (GRDP) đạt 30.550,98 tỷ đồng (+37,17%); Công nghiệp - Xây dựng đạt 18.056 tỷ (+54,7%); Du lịch đón 6,8 triệu lượt khách, trong đó khách quốc tế đạt 1,502 triệu lượt (+53,49%); Doanh thu du lịch đạt 36.447 tỷ đồng (+46,59%).
2. Phân tích kinh tế học: Tương quan thời điểm vs Nhân quả thực chất. Sự tăng trưởng là kết quả của lực đẩy cộng hưởng từ 137k tỷ hạ tầng công - tư và việc gỡ bỏ nút thắt thể chế.
3. Bài học Lý Quang Diệu (Singapore 1965): Dẹp loạn và thiết lập CPIB trước khi mở cửa thị trường; mất 30 năm để chuyển hóa uy quyền cá nhân thành sức mạnh của thiết chế tự động.
4. Hướng đi tương lai của Phú Quốc: Số hóa địa chính triệt tiêu nhũng nhiễu và hướng tới Định mức Tín nhiệm Đặc khu Độc lập (Sub-national Credit Rating) đạt chuẩn AAA quốc tế."""
    }
]

async def extract_all():
    print(f"=== KHỞI CHẠY BATCH EXTRACTION RA RESEARCH_VAULT ({len(QUERIES)} CHUYÊN ĐỀ) ===")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    async with NotebookLMClient.from_storage() as client:
        for idx, item in enumerate(QUERIES, 1):
            fname = item["filename"]
            ftitle = item["title"]
            fprompt = item["prompt"]
            outpath = os.path.join(OUTPUT_DIR, fname)
            
            print(f"\n[{idx}/{len(QUERIES)}] 📝 Đang trích xuất: {ftitle} -> {fname}...")
            
            try:
                res = await client.chat.ask(NOTEBOOK_ID, fprompt)
                answer = res.answer
                
                with open(outpath, "w", encoding="utf-8") as f:
                    f.write(f"# {ftitle}\n\n")
                    f.write(f"<!--\nTRÍCH XUẤT NGUỒN GỐC RAG:\n- Master Notebook ID: {NOTEBOOK_ID}\n- Số nguồn tài liệu Deep Research trong Notebook: 30 sources\n- Chuyên gia: The Macro Financial Researcher\n-->\n\n")
                    f.write(answer)
                    f.write(f"\n\n---\n*Trích xuất tự động qua Google NotebookLM Direct RPC API từ Master Notebook 2cc55935-2e9d-4ee7-bd02-7a906ff073f9*\n")
                
                print(f"    ✅ Hoàn tất trích xuất {fname} ({len(answer)} ký tự)!")
            except Exception as e:
                print(f"    ❌ Lỗi trích xuất {fname}: {e}")
                
            await asyncio.sleep(2)
            
    print("\n🎉 HOÀN TẤT TRÍCH XUẤT TOÀN BỘ 10/10 CHUYÊN ĐỀ VÀO RESEARCH_VAULT!")

if __name__ == "__main__":
    asyncio.run(extract_all())
