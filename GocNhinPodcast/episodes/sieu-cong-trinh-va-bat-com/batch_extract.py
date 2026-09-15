import subprocess
import os
import json

NOTEBOOK_ID = "6fa782f3-fc2c-4709-ac76-58c66932be51"
HOME_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
CLI_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
VAULT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/sieu-cong-trinh-va-bat-com/research_vault"

os.makedirs(VAULT_DIR, exist_ok=True)

QUERIES = [
    {
        "filename": "01_market_making_public_goods.md",
        "title": "Bản chất Hàng hóa công cộng và Khởi tạo thị trường",
        "prompt": """Phân tích bản chất kinh tế học của Hàng hóa công cộng (Public Goods) và cơ chế Khởi tạo thị trường (Market-Making) của đầu tư công:
1. Tại sao khu vực tư nhân không thể và không bao giờ tự đứng ra đầu tư vào các siêu công trình hạ tầng mạng lưới cơ bản (đường sắt cao tốc, hệ thống đê biển, đường dây truyền tải điện quốc gia, siêu cảng)? Giải thích qua bài toán thời gian hoàn vốn 30-50 năm, tỷ suất sinh lời tài chính âm và ngoại ứng tích cực (positive externalities) không thể tư nhân hóa.
2. Vai trò "vốn mồi" và tích lũy tư bản cố định của Nhà nước: Đầu tư công tạo ra nền tảng hạ tầng như thế nào để toàn bộ khu vực kinh tế tư nhân, hộ kinh doanh và doanh nghiệp FDI sinh sôi nảy nở?
3. Phân biệt rõ: Đầu tư công tạo ra sân chơi vs đầu tư công lấn át tư nhân (Crowding-in vs Crowding-out). Cung cấp các nghiên cứu và số liệu tại Việt Nam về hệ số lan tỏa của đầu tư công."""
    },
    {
        "filename": "02_spatial_economics_decentralization.md",
        "title": "Kinh tế học không gian và Hiện tượng Ly nông bất ly hương",
        "prompt": """Phân tích lý thuyết Kinh tế học không gian (Spatial Economics) và tác động phân bổ lại lực lượng sản xuất của hạ tầng giao thông tại Việt Nam:
1. Khoảng cách địa lý vs khoảng cách kinh tế (chi phí và thời gian di chuyển): Hệ thống cao tốc Bắc - Nam và các trục cao tốc miền Tây (Cần Thơ - Cà Mau, Châu Đốc - Cần Thơ - Sóc Trăng) đang thay đổi bản đồ kinh tế ra sao?
2. Hiện tượng 'Ly nông bất ly hương': Hạ tầng đưa các khu công nghiệp, cụm công nghiệp về các vùng nông thôn nghèo (miền Trung, miền Tây) như thế nào để người dân có việc làm phi nông nghiệp tại quê nhà, chấm dứt làn sóng di cư tự phát lên các siêu đô thị ngột ngạt?
3. Phân tích mặt trái: Nguy cơ 'Hiệu ứng hút chân không' (Straw Effect) - khi hạ tầng kết nối quá nhanh có thể hút cạn nhân lực trẻ và dòng vốn từ các tỉnh nhỏ về đại đô thị trung tâm nếu địa phương không có chính sách công nghiệp phù hợp."""
    },
    {
        "filename": "03_middle_income_trap_fdi_upgrading.md",
        "title": "Siêu hạ tầng và Bài toán Thoát bẫy thu nhập trung bình",
        "prompt": """Phân tích mối quan hệ giữa siêu hạ tầng chiến lược và nỗ lực thoát bẫy thu nhập trung bình của Việt Nam:
1. Giới hạn của mô hình gia công giá rẻ (lương công nhân 6-8 triệu/tháng) và nguy cơ mất lợi thế cạnh tranh vào tay các nước như Bangladesh, Ấn Độ, Indonesia.
2. Sân bay Quốc tế Long Thành (16 tỷ USD), Siêu cảng Cần Giờ, Cảng Lạch Huyện: Các siêu công trình này giải quyết những điểm nghẽn sống còn nào của chuỗi cung ứng công nghệ cao (bán dẫn, AI, trung tâm dữ liệu, dược phẩm)?
3. Tỷ lệ giá trị gia tăng nội địa (DVA) và sự tham gia của các doanh nghiệp cơ khí, luyện kim, xây dựng Việt Nam: Làm sao để siêu công trình tạo ra năng lực tự chủ công nghệ thay vì chỉ là thị trường tiêu thụ máy móc chìa khóa trao tay của nước ngoài?"""
    },
    {
        "filename": "04_energy_lifeline_500kv_nuclear.md",
        "title": "Hạ tầng Năng lượng nền tảng: 500kV mạch 3 và Điện hạt nhân",
        "prompt": """Phân tích hạ tầng năng lượng như một 'bình oxy' sống còn cho nền kinh tế và bát cơm của người lao động:
1. Bài học xương máu từ cuộc khủng hoảng thiếu điện tại miền Bắc vào mùa hè năm 2023: Tác động cụ thể đến hoạt động sản xuất của các nhà máy công nghiệp (Samsung, Foxconn, Canon...), việc làm của công nhân và thiệt hại kinh tế.
2. Kỳ tích thi công thần tốc Đường dây 500kV mạch 3 (Quảng Trạch - Phố Nối): Vai trò giải tỏa công suất, cân đối nguồn điện liên vùng và bài học quản trị huy động nguồn lực quốc gia.
3. Quy hoạch Điện VIII và chiến lược tái khởi động Điện hạt nhân Ninh Thuận: Tại sao các ngành công nghệ cao như sản xuất chip bán dẫn và AI bắt buộc phải có nguồn điện nền (Baseload) ổn định tuyệt đối 24/7/365 không thể phụ thuộc vào điện mặt trời hay điện gió biến động?"""
    },
    {
        "filename": "05_mekong_water_security_phunam.md",
        "title": "An ninh Sinh thái và Bát cơm ĐBSCL trước Kênh Phù Nam Techo",
        "prompt": """Phân tích các siêu công trình thủy lợi, sinh thái bảo vệ vựa lúa, vựa trái cây Đồng bằng sông Cửu Long (ĐBSCL):
1. Thách thức sinh tồn: Hiện tượng biến đổi khí hậu, nước biển dâng, sụt lún đất và xâm nhập mặn ngày càng khốc liệt tại ĐBSCL tác động thế nào đến diện tích trồng trọt và sinh kế hàng triệu nông dân?
2. Tác động tiềm tàng của Dự án Kênh đào Phù Nam Techo (Campuchia) đối với lưu lượng dòng chảy sông Mekong về hạ nguồn Việt Nam.
3. Các siêu dự án hạ tầng cống ngăn mặn (như hệ thống thủy lợi Cái Lớn - Cái Bé), các hồ trữ ngọt và quy hoạch phân vùng 'thuận thiên' theo Nghị quyết 120/NQ-CP: Ý nghĩa sống còn trong việc bảo vệ 'bát cơm' hạt gạo của Việt Nam và an ninh lương thực toàn cầu."""
    },
    {
        "filename": "06_logistics_reduction_16pct_gdp.md",
        "title": "Giải phẫu Chi phí Logistics 16.8% GDP và Giá cả Tiêu dùng",
        "prompt": """Phân tích chi tiết cơ cấu chi phí logistics tại Việt Nam và tác động đến chi phí sinh hoạt của người dân:
1. Chi phí logistics chiếm 16% - 17% GDP: So sánh với mức trung bình thế giới (10-12%), Singapore (8%), Nhật Bản (11%). Tại sao chi phí logistics Việt Nam lại cao như vậy (sự phụ thuộc vào đường bộ hơn 77-80%, thiếu kết nối đa phương thức đường sắt - cảng biển)?
2. Chi phí logistics cấu thành bao nhiêu % trong giá thành 1 kg gạo, rau quả, thủy hải sản từ đồng ruộng ĐBSCL/Tây Nguyên về chợ dân sinh Hà Nội, TP.HCM (ước tính 20-30%)?
3. Khi hệ thống cao tốc và đường sắt hàng hóa hoàn thành, chi phí logistics dự kiến giảm xuống 10-12% GDP sẽ hạ nhiệt giá cả tiêu dùng và tăng thu nhập cho nông dân ra sao? Phân tích bài toán đánh đổi giữa chi phí tiết kiệm nhiên liệu/thời gian vs chi phí phí BOT."""
    },
    {
        "filename": "07_money_multiplier_m2_liquidity.md",
        "title": "Cơ chế Truyền dẫn Tiền tệ và Chu trình Kho bạc Nhà nước",
        "prompt": """Phân tích cơ chế truyền dẫn tiền tệ và tác động vĩ mô khi giải ngân 700.000 - 800.000 tỷ đồng đầu tư công mỗi năm:
1. Chu trình tiền tệ từ Kho bạc Nhà nước sang hệ thống ngân hàng thương mại (đặc biệt là Big 4: Vietcombank, BIDV, VietinBank, Agribank): Tiền giải ngân tác động thế nào đến thanh khoản hệ thống, lãi suất liên ngân hàng và lãi suất cho vay nền kinh tế?
2. Hệ số nhân tiền tệ (Money Multiplier - m) và Cung tiền M2: Một đồng tiền cơ sở (M0) từ đầu tư công khi được bơm vào hệ thống ngân hàng sẽ khuếch đại tổng phương tiện thanh toán như thế nào qua hoạt động tín dụng?
3. Tác động trước mắt (6-24 tháng): Đóng vai trò 'người mua hàng cuối cùng' (Buyer of Last Resort) kích thích tổng cầu AD, tăng tốc vòng quay tiền (Velocity of Money) vs rủi ro lạm phát chi phí đẩy và lạm phát cầu kéo."""
    },
    {
        "filename": "08_fiscal_debt_railway_67b.md",
        "title": "Hồ sơ Tài chính Đường sắt 67.34 tỷ USD và Kỷ luật Tài khóa",
        "prompt": """Phân tích phương án tài chính và áp lực nợ công của Dự án Đường sắt tốc độ cao Bắc - Nam (67,34 tỷ USD):
1. Phương án huy động vốn: Tỷ trọng ngân sách trung ương, phát hành trái phiếu chính phủ, thu hồi từ quỹ đất TOD và vốn vay ODA (chủ trương hạn chế phụ thuộc vốn vay nước ngoài để tránh bẫy nợ). Phân kỳ đầu tư 12 năm (khoảng 5,6 tỷ USD/năm).
2. Tác động đến các chỉ tiêu an toàn nợ công: Trần nợ công 60% GDP, chỉ tiêu bội chi ngân sách (mục tiêu 3% vs dự kiến 4.1% GDP), và nghĩa vụ trả nợ trực tiếp của Chính phủ (trần 25% tổng thu ngân sách).
3. Bài toán chi phí vận hành và bảo dưỡng (O&M) sau năm 2035 (ước tính trên 1 tỷ USD/năm): Bài học bù lỗ từ các tuyến metro đô thị (Cát Linh - Hà Đông, Nhổn - Ga Hà Nội, Bến Thành - Suối Tiên) và phương án tài chính để tránh biến dự án thành gánh nặng thuế cho người dân."""
    },
    {
        "filename": "09_cantillon_effect_land_inequality.md",
        "title": "Hiệu ứng Cantillon và Bất bình đẳng Đất đai Ven Đô",
        "prompt": """Phân tích tác động xã hội học và bất bình đẳng của dòng tiền đầu tư công qua Hiệu ứng Cantillon (Cantillon Effect):
1. Hiện tượng dòng tiền phân bổ bất đối xứng: Ai là người tiếp cận dòng tiền đầu tư công và thông tin quy hoạch đầu tiên (nhà thầu lớn, giới đầu cơ đất đai)? Khi tiền chảy đến tay người lao động nghèo thì giá cả tài sản đã tăng đến mức nào?
2. Cơn sốt đất ven các nút giao cao tốc, đường vành đai 3, vành đai 4: Tỷ lệ tăng giá đất nền so với tốc độ tăng thu nhập thực tế của người dân đô thị. Giấc mơ sở hữu nhà ở của lao động trẻ và giá thuê phòng trọ bị đẩy lên ra sao?
3. Khảo sát sinh kế của nông dân sau khi nhận tiền đền bù đất: Bao nhiêu % tái đầu tư vào sản xuất kinh doanh vs bao nhiêu % gửi tiết kiệm hoặc tiêu dùng mua sắm? Nguy cơ mất tư liệu sản xuất và rơi vào bẫy nghèo đói sau khi hết tiền đền bù."""
    },
    {
        "filename": "10_sand_crisis_civil_construction.md",
        "title": "Khủng hoảng Cát san lấp và Bão giá Vật liệu Xây dựng Dân sinh",
        "prompt": """Phân tích cuộc khủng hoảng cát san lấp, đất đắp và tác động đè bẹp nhu cầu xây dựng dân sự:
1. Quy mô nhu cầu cát san lấp, đá xây dựng của các tuyến cao tốc Bắc - Nam và cao tốc miền Nam giai đoạn 2024-2026 (hàng chục đến hàng trăm triệu m3).
2. Hiện tượng 'vĩ mô hút cạn tài nguyên dân sinh': Giá cát xây dựng, cát san lấp trên thị trường tự do tăng 50% - 150%. Người dân xây nhà cấp 4, sửa nhà chịu ảnh hưởng thế nào? Các nhà thầu xây dựng dân dụng vừa và nhỏ đối mặt nguy cơ phá sản ra sao?
3. Giải pháp cát biển thay thế: Những thách thức kỹ thuật về độ mặn, rỉ sét bê tông, giá thành tuyển rửa và rào cản pháp lý mỏ vật liệu."""
    },
    {
        "filename": "11_tod_land_value_capture.md",
        "title": "Mô hình TOD và Công bằng trong Thu hồi Địa tô Chênh lệch",
        "prompt": """Phân tích mô hình Phát triển Đô thị theo định hướng giao thông (TOD - Transit Oriented Development) và cơ chế Thu hồi giá trị đất (Land Value Capture):
1. Khái niệm Land Value Capture: Khi Nhà nước bỏ tiền thuế của toàn dân ra làm đường sắt cao tốc hay đường vành đai, giá đất hai bên đường tăng gấp 5-10 lần. Địa tô chênh lệch đó thuộc về ai?
2. Cơ chế để Nhà nước thu hồi phần lớn giá trị địa tô gia tăng quanh các nhà ga, nút giao để tái đầu tư vào ngân sách an sinh xã hội, giáo dục, y tế và bù đắp chi phí xây dựng hạ tầng thay vì để giới đầu cơ tư nhân đút túi.
3. Bài học kinh nghiệm quốc tế: Mô hình MTR của Hồng Kông ('Rail plus Property' - Đường sắt kết hợp Bất động sản) hay kinh nghiệm của Tokyo (Nhật Bản) trong việc tự chủ tài chính cho hạ tầng đường sắt đô thị."""
    },
    {
        "filename": "12_global_precedents_gyeongbu_vs_debt.md",
        "title": "Bài học Lịch sử: Kỳ tích Hóa rồng vs Cạm bẫy Nợ nần Phù hoa",
        "prompt": """Phân tích so sánh lịch sử thế giới về các quốc gia triển khai đại dự án hạ tầng:
1. Nhóm thành công cất cánh kinh tế:
   - Hàn Quốc thập niên 1970: Quyết định lịch sử xây dựng Cao tốc Gyeongbu (Seoul - Busan) kết nối các khu công nghiệp luyện kim Pohang, đóng tàu Ulsan, tạo đòn bẩy cho kỳ tích sông Hàn.
   - Nhật Bản năm 1964: Tuyến tàu Tokaido Shinkansen kết nối Tokyo - Nagoya - Osaka trước thềm Olympic Tokyo, trở thành huyết mạch kinh tế của đất nước mặt trời mọc.
2. Nhóm cạm bẫy nợ nần và voi trắng:
   - Sri Lanka: Vay nợ quốc tế xây dựng Cảng Hambantota và Sân bay quốc tế Mattala giữa rừng vắng khách, dẫn đến mất khả năng trả nợ và khủng hoảng kinh tế chính trị 2022.
   - Hy Lạp: Chi tiêu công ồ ạt cho các công trình Thế vận hội Olympic Athens 2004 không có khả năng khai thác thương mại, mở đầu cho cuộc khủng hoảng nợ công suýt làm sụp đổ Eurozone.
   - Trung Quốc: Tập đoàn Đường sắt Trung Quốc (China Railway) tích tụ khối nợ hơn 850 tỷ USD với nhiều tuyến cao tốc chạy qua các vùng thưa dân bị lỗ nặng nề.
3. Ranh giới thể chế: Đâu là bài học sống còn cho Việt Nam để các siêu công trình hạ tầng trở thành đòn bẩy hóa rồng bền vững thay vì gánh nợ cho thế hệ mai sau?"""
    }
]

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = HOME_DIR

print(f"[*] Starting Batch Extraction for 12 Queries to {VAULT_DIR}...")

for idx, item in enumerate(QUERIES, 1):
    filepath = os.path.join(VAULT_DIR, item["filename"])
    print(f"\n[{idx}/12] Extracting: {item['title']} -> {item['filename']}...")
    cmd = [
        CLI_PATH,
        "ask",
        item["prompt"],
        "-n", NOTEBOOK_ID,
        "--save-as-note",
        "-t", item["title"],
        "--json"
    ]
    try:
        res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=240)
        if res.returncode == 0:
            try:
                data = json.loads(res.stdout)
                content = data.get("answer", "")
            except Exception:
                content = res.stdout
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {item['title']}\n\n{content}\n")
            print(f"[✓] Saved {item['filename']} ({len(content)} chars)")
        else:
            print(f"[✗] Error extracting {item['filename']}: {res.stderr}")
    except Exception as e:
        print(f"[!] Exception for {item['filename']}: {e}")

print("\n=======================================================")
print("[✓] Batch Extraction to Vault Completed Successfully!")
print("=======================================================\n")
