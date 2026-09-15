"""
Script to generate both chapter_05_visual.md and prompts_chapter_05.txt
for Episode 'Vũ Khí Lúa Gạo Việt Nam' - Chapter 05.
Strictly adheres to:
- Flow Batch Studio syntax
- Warm Luminous Editorial Palette (#FAF7EE, #F59E0B, #EA580C)
- Selective Lower-Left 25% Rule (~20% text overlay)
- Canonical references: @modi_india.jpg for CH05_SC052/053
- Steady camera and static text preservation in video prompts
"""

import re
import json

scenes_data = [
    {
        "id": "CH05_SC001",
        "dur": "6.04s",
        "words": 23,
        "text": "Nếu theo dõi các bản tin kinh tế, bạn sẽ bắt gặp một nghịch lý thương mại thoạt nhìn vô cùng khó hiểu.",
        "anatomy": {
            "tier1": "Bàn làm việc của chuyên gia phân tích kinh tế thương mại nông sản với các bản đồ xuất nhập khẩu Đông Nam Á.",
            "tier2": "Hai chồng hồ sơ hải quan đối lập đặt song song: Một bên là giấy tờ xuất khẩu gạo kỷ lục, một bên là tờ khai nhập khẩu lúa ngoại.",
            "tier3": "Cú máy đẩy chậm vào cặp hồ sơ xuất nhập khẩu đặt cạnh nhau (Slow push-in toward contrasting import-export trade dossiers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a polished editorial economic research desk with comparative international agricultural trade dossiers and customs declaration charts placed side by side under warm desk lighting",
        "setting": "a modern economic trade research office illuminated by warm morning sunbeams through sheer curtains",
        "motion": "Slow push-in toward the contrasting agricultural trade balance dossiers"
    },
    {
        "id": "CH05_SC002",
        "dur": "6.82s",
        "words": 26,
        "text": "Năm 2024, Việt Nam lập kỷ lục lịch sử khi xuất khẩu hơn chín triệu tấn gạo, mang về hơn năm phẩy bảy tỷ đô la.",
        "anatomy": {
            "tier1": "Cầu cảng xuất khẩu quốc tế sầm uất tại Cái Mép hoặc Cát Lái với các tàu container và tàu hàng rời tải trọng lớn.",
            "tier2": "Bảng điện tử báo cáo thống kê hiển thị con số kỷ lục xuất khẩu hơn 9 triệu tấn gạo đạt kim ngạch trên 5.7 tỷ USD rực rỡ dưới nắng ấm.",
            "tier3": "Cú máy tĩnh trực diện vào con số kỷ lục >9 triệu tấn và >5.7 tỷ USD (Steady shot on historic >9M tons and >$5.7B export record) cùng text overlay góc trái dưới."
        },
        "overlay": "XUẤT KHẨU: > 9 TRIỆU TẤN (~5,7 TỶ USD)",
        "ref": None,
        "subj": "a busy international export terminal with dockside container cranes systematically loading grain cargo vessels beside an editorial data badge displaying over 9 million metric tons and 5.7 billion USD in export revenue",
        "setting": "a vibrant deep-water international port in southern Vietnam under warm radiant morning sunlight",
        "motion": "Steady camera shot framing the bustling export port and historic revenue milestone"
    },
    {
        "id": "CH05_SC003",
        "dur": "6.82s",
        "words": 26,
        "text": "Chúng ta vững vàng ở vị thế cường quốc lương thực hàng đầu, cung cấp hạt gạo nuôi sống hàng chục triệu người khắp thế giới.",
        "anatomy": {
            "tier1": "Bản đồ hải trình vận tải biển toàn cầu với các tuyến tàu hàng xuất phát từ Việt Nam vươn ra Philippines, Indonesia, châu Phi và châu Âu.",
            "tier2": "Hình ảnh những bao gạo mang thương hiệu Việt Nam cập cảng khắp năm châu, nuôi sống hàng chục triệu bữa ăn mỗi ngày.",
            "tier3": "Cú máy bay ngang qua bản đồ hải trình phân phối gạo toàn cầu (Panoramic glide across global rice distribution routes)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a global maritime food security map showing illuminated trade routes radiating from southern Vietnam across Southeast Asia, Africa, and the Middle East, symbolizing agricultural strength",
        "setting": "an international food supply command center display in warm amber and cream tones",
        "motion": "Smooth panoramic glide across the global maritime food distribution network"
    },
    {
        "id": "CH05_SC004",
        "dur": "6.56s",
        "words": 25,
        "text": "Thế nhưng trong chính giai đoạn ấy, mỗi năm chúng ta lại bỏ ra hàng trăm triệu đô la để nhập khẩu lúa gạo ngoại.",
        "anatomy": {
            "tier1": "Cửa khẩu đường sông biên giới Tây Nam với dòng sà lan vận tải chở đầy lúa thô nối đuôi nhau vào Việt Nam.",
            "tier2": "Các hóa đơn thanh toán ngoại tệ ngân hàng cho các lô hàng lúa gạo nhập khẩu từ các nước láng giềng.",
            "tier3": "Cú máy trượt ngang qua đoàn sà lan chở lúa ngoại nhập (Horizontal tracking shot past inbound raw grain barges)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a line of heavy steel river barges laden with raw harvested paddy floating down a broad sunlit Mekong border canal into southern Vietnam, viewed alongside foreign bank trade payment vouchers",
        "setting": "a busy riverway border customs checkpoint under warm golden morning light",
        "motion": "Slow horizontal tracking shot past the line of inbound foreign grain barges"
    },
    {
        "id": "CH05_SC005",
        "dur": "5.25s",
        "words": 20,
        "text": "Con số nhập khẩu thực tế lên tới từ một phẩy năm đến hai phẩy năm triệu tấn mỗi năm.",
        "anatomy": {
            "tier1": "Bảng tổng hợp cán cân thương mại lúa gạo tại Cục Xuất nhập khẩu (Bộ Công Thương).",
            "tier2": "Con số thống kê nhập khẩu hàng năm dao động từ 1.5 đến 2.5 triệu tấn lúa gạo thô hiển thị rõ ràng trên biểu đồ.",
            "tier3": "Cú máy tĩnh trực diện vào con số nhập khẩu 1.5 - 2.5 triệu tấn/năm (Steady shot on 1.5 - 2.5 million tons annual import metric) cùng text overlay góc trái dưới."
        },
        "overlay": "NHẬP KHẨU: 1,5 - 2,5 TRIỆU TẤN/NĂM",
        "ref": None,
        "subj": "an analytical trade balance chart displaying annual incoming volume statistics confirming 1.5 to 2.5 million metric tons of raw paddy and white rice imports per year",
        "setting": "a government trade statistical bureau office under warm neutral ambient lighting",
        "motion": "Steady camera shot framing the annual agricultural import volume statistics"
    },
    {
        "id": "CH05_SC006",
        "dur": "5.77s",
        "words": 22,
        "text": "Hàng vạn tấn lúa tươi từ Campuchia đều đặn xuôi sà lan qua các cửa khẩu biên giới An Giang, Đồng Tháp.",
        "anatomy": {
            "tier1": "Cửa khẩu quốc tế đường thủy Vĩnh Xương (An Giang) hoặc Thường Phước (Đồng Tháp) tấp nập thuyền bè.",
            "tier2": "Những chiếc sà lan và ghe gỗ tải trọng hàng trăm tấn chở đầy ắp lúa tươi vàng ươm từ đồng ruộng Campuchia đang làm thủ tục thông quan vào miền Tây.",
            "tier3": "Cú máy bay chậm dọc theo dòng sông biên giới theo sau đoàn ghe chở lúa tươi (Slow aerial glide following raw paddy boats along border river)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a scenic border river crossing at Vinh Xuong An Giang with traditional wooden cargo boats and modern steel barges brimming with golden raw paddy crossing from Cambodia into Vietnam",
        "setting": "a sun-drenched Mekong river border channel lined with green palm banks in early morning light",
        "motion": "Slow aerial glide along the river following the golden raw grain transport barges"
    },
    {
        "id": "CH05_SC007",
        "dur": "6.56s",
        "words": 25,
        "text": "Cùng lúc đó, các chuyến tàu chở gạo trắng tấm giá rẻ từ Ấn Độ hay Pakistan liên tục cập các cảng biển phía Nam.",
        "anatomy": {
            "tier1": "Khu bến cảng hàng hải phía Nam với tàu hàng viễn dương treo cờ quốc tế cập cầu cảng.",
            "tier2": "Cần cẩu bờ bốc dỡ các pallet bao gạo tấm 100% broken và gạo trắng giá rẻ từ Ấn Độ và Pakistan đưa vào kho cảng trung chuyển.",
            "tier3": "Cú máy nâng chậm từ khoang tàu hàng lên cần cẩu bốc bao gạo tấm (Slow tilt-up from ship cargo hold to quayside unloading crane)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a commercial seaport pier in southern Vietnam with dockside gantry cranes unloading bulk pallets of white broken rice sacks from an ocean freighter originating from South Asia",
        "setting": "a coastal industrial shipping berth under warm late-afternoon skies",
        "motion": "Slow upward tilt from ship cargo hold to quayside cranes unloading grain sacks"
    },
    {
        "id": "CH05_SC008",
        "dur": "3.41s",
        "words": 13,
        "text": "Nhiều người khi nghe đến con số này đã không khỏi giật mình.",
        "anatomy": {
            "tier1": "Quán cà phê sáng trên đường phố Việt Nam nơi người dân đang đọc báo hoặc lướt tin tức trên điện thoại.",
            "tier2": "Khuôn mặt ngạc nhiên của người độc giả trước nghịch lý: Xuất khẩu gạo hàng đầu nhưng lại nhập khẩu hàng triệu tấn lúa ngoại.",
            "tier3": "Cú máy đẩy chậm vào màn hình tin tức trên bàn cà phê buổi sáng (Slow push-in toward news article on morning coffee table)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a morning sidewalk cafe table in Ho Chi Minh City with an open newspaper and smartphone displaying an economic headline about simultaneous rice exports and imports",
        "setting": "a tranquil urban morning cafe under dappled golden sunlight through tamarind leaves",
        "motion": "Slow push-in toward the coffee table newspaper framing the paradoxical headline"
    },
    {
        "id": "CH05_SC009",
        "dur": "6.3s",
        "words": 24,
        "text": "Tại sao một đất nước xuất khẩu thừa mứa gạo lại phải đi mua hàng triệu tấn lúa gạo của các nước láng giềng?",
        "anatomy": {
            "tier1": "Hình ảnh tương phản tinh tế: Bên trái là kho lúa xuất khẩu ngút ngàn của ĐBSCL; Bên phải là đoàn thuyền chở lúa ngoại nhập bến.",
            "tier2": "Dấu hỏi lớn màu vàng hổ phách nối giữa hai luồng vật chất xuất khẩu và nhập khẩu, đặt ra câu hỏi bản chất cho toàn bộ chuỗi cung ứng.",
            "tier3": "Cú máy trượt ngang qua hai khối hình ảnh đối xứng (Horizontal tracking shot past symmetrical economic visuals)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a conceptual diptych illustration showing vast domestic Mekong export silos on the left and arriving foreign raw grain riverboats on the right, connected by a subtle golden query mark",
        "setting": "an editorial analytical background in warm ivory and amber tones",
        "motion": "Smooth horizontal tracking shot across the contrasting dual flows of export and import"
    },
    {
        "id": "CH05_SC010",
        "dur": "6.82s",
        "words": 26,
        "text": "Liệu có phải vựa lúa miền Tây đang thiếu hụt nguồn cung? Câu trả lời của các nhà kinh tế thương mại là hoàn toàn không.",
        "anatomy": {
            "tier1": "Cánh đồng lúa bạt ngàn An Giang trĩu hạt vàng rực dưới ánh nắng mặt trời rực rỡ, máy gặt đập liên hợp đang chạy phăng phăng.",
            "tier2": "Kho lúa dự trữ quốc gia và kho doanh nghiệp luôn đầy ắp thóc vàng, khẳng định nguồn cung nội địa luôn dồi dào, vững như bàn thạch.",
            "tier3": "Cú máy bay góc cao lướt trên cánh đồng lúa bội thu (High-angle aerial sweep over thriving bountiful harvest)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a grand high-angle panoramic sweep over an endless golden Mekong Delta rice paddy in An Giang teeming with modern red combine harvesters, proving overflowing domestic abundance",
        "setting": "the vast agricultural heartland of southern Vietnam under brilliant warm sunshine",
        "motion": "High-angle cinematic aerial sweep over the sunlit bountiful rice fields"
    },
    {
        "id": "CH05_SC011",
        "dur": "4.2s",
        "words": 16,
        "text": "Hiện tượng này không phản ánh sự yếu kém hay thiếu hụt của nền nông nghiệp.",
        "anatomy": {
            "tier1": "Phòng điều hành Trung tâm Xúc tiến Thương mại Nông nghiệp với các màn hình số liệu tăng trưởng nông sản.",
            "tier2": "Biểu đồ sức khỏe ngành lúa gạo với các chỉ số thặng dư thương mại luôn duy trì mức dương rất lớn.",
            "tier3": "Cú máy đẩy chậm vào biểu đồ thặng dư thương mại nông nghiệp (Slow push-in on positive agricultural trade balance)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an agronomic trade dashboard displaying glowing positive green metrics and upward growth vectors confirming robust agricultural stability and massive net trade surplus",
        "setting": "a modern trade intelligence command center in warm amber hues",
        "motion": "Slow push-in shot framing the strong agricultural net surplus analytics"
    },
    {
        "id": "CH05_SC012",
        "dur": "6.56s",
        "words": 25,
        "text": "Ngược lại, nó là kết quả của một nước cờ tối ưu hóa chuỗi giá trị và phân công lao động ở cấp độ cao.",
        "anatomy": {
            "tier1": "Bàn cờ kinh tế học vĩ mô với các quân cờ đại diện cho từng mắt xích: Gieo trồng cao cấp, chế biến công nghệ cao và logistics khu vực.",
            "tier2": "Bàn tay của nhà chiến lược dịch chuyển quân cờ nâng cấp chuỗi giá trị lên nấc thang tinh tế hơn.",
            "tier3": "Cú máy cận cảnh quân cờ chiến lược lướt trên bàn cờ kinh tế (Close-up tracking shot on economic chess move across value-chain board)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a metaphorical polished wooden chessboard where stylized miniature pieces representing high-tech milling, specialty aromatic grain, and regional logistics are strategically repositioned",
        "setting": "an executive strategic analysis study under warm lamp lighting",
        "motion": "Close-up slow tracking shot following the repositioning of value-chain pieces"
    },
    {
        "id": "CH05_SC013",
        "dur": "4.99s",
        "words": 19,
        "text": "Hãy bắt đầu từ sự chuyển dịch kỳ diệu ngay trên các cánh đồng đồng bằng sông Cửu Long.",
        "anatomy": {
            "tier1": "Cánh đồng mẫu lớn tại Sóc Trăng hoặc Bạc Liêu trong ánh nắng sớm tinh khôi.",
            "tier2": "Những người nông dân tiến bộ đang cùng cán bộ khuyến nông kiểm tra từng nhánh lúa thơm giống mới hạt thon dài óng mượt.",
            "tier3": "Cú máy trượt ngang qua hàng lúa giống mới thẳng tắp (Horizontal tracking shot past premium aromatic paddy rows)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a scenic morning view of a certified high-quality seed demonstration farm in Soc Trang where modern farmers and agricultural extension officers inspect slender aromatic rice stalks",
        "setting": "the lush green-and-gold plains of Soc Trang under warm morning skies",
        "motion": "Slow horizontal tracking shot past modern farmers inspecting fragrant rice panicles"
    },
    {
        "id": "CH05_SC014",
        "dur": "5.51s",
        "words": 21,
        "text": "Trong suốt một thập kỷ qua, nông dân miền Tây đã chủ động bỏ rơi phân khúc lúa phẩm cấp thấp.",
        "anatomy": {
            "tier1": "Khuôn viên hợp tác xã nông nghiệp với bảng tổng kết chuyển đổi cơ cấu giống lúa qua 10 năm.",
            "tier2": "Đồ thị diện tích giống lúa cấp thấp IR50404 giảm mạnh dần về 0, nhường chỗ cho các giống lúa chất lượng cao.",
            "tier3": "Cú máy hạ chậm dọc theo đồ thị suy giảm của lúa phẩm cấp thấp (Slow downward tilt along phasing-out low-grade grain curve)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an agricultural cooperative planning board showing the historical 10-year decline of old low-grade commercial rice varieties like IR50404 replaced by modern fragrant strains",
        "setting": "a rural agricultural cooperative hall in southern Vietnam in warm natural light",
        "motion": "Slow downward tilt along the chart showing the deliberate phase-out of low-grade varieties"
    },
    {
        "id": "CH05_SC015",
        "dur": "1.57s",
        "words": 6,
        "text": "Nhờ những đột phá về giống",
        "anatomy": {
            "tier1": "Phòng thí nghiệm di truyền và chọn tạo giống lúa của Viện Lúa Đồng bằng sông Cửu Long.",
            "tier2": "Các nhà khoa học nông nghiệp quan sát chuỗi gen và các mẫu lúa lai đột phá trong ống nghiệm tinh khiết.",
            "tier3": "Cú máy đẩy nhanh vào cụm ống nghiệm giống lúa lai đột phá (Dynamic push-in on genetic breeding test tubes)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a high-precision agronomic genetics laboratory with clean glassware, petri dishes with germinated rice seeds, and genetic hybridization charts",
        "setting": "the Mekong Rice Research Institute laboratory under warm clean scientific lighting",
        "motion": "Dynamic push-in shot toward the germinated hybrid rice seedling petri dishes"
    },
    {
        "id": "CH05_SC016",
        "dur": "5.51s",
        "words": 21,
        "text": "hơn tám mươi phần trăm diện tích canh tác hiện nay đã chuyển sang các giống lúa thơm chất lượng cao.",
        "anatomy": {
            "tier1": "Toàn cảnh cánh đồng ĐBSCL nhìn từ trên cao ngút ngàn tầm mắt, rực sáng sắc vàng thơm ngát.",
            "tier2": "Biểu đồ cơ cấu mùa vụ hiển thị hơn 80% tổng diện tích canh tác chuyên canh các giống lúa thơm cao cấp.",
            "tier3": "Cú máy tĩnh trực diện vào con số >80% diện tích lúa thơm cao cấp (Steady shot on >80% premium fragrant rice acreage) cùng text overlay góc trái dưới."
        },
        "overlay": "> 80% DIỆN TÍCH: GẠO THƠM CAO CẤP",
        "ref": None,
        "subj": "a vast aerial panorama of golden aromatic rice paddies in the Mekong Delta with an editorial data infographic highlighting over 80 percent total cultivated area dedicated to premium fragrant varieties",
        "setting": "the sunlit delta plains stretching to the horizon under warm amber skies",
        "motion": "Steady camera shot framing the vast fragrant rice fields and acreage milestone"
    },
    {
        "id": "CH05_SC017",
        "dur": "5.77s",
        "words": 22,
        "text": "Những cái tên như ST24, ST25, Đài Thơm 8 hay OM18 cho cơm mềm, dẻo và giữ trọn hương thơm tự nhiên.",
        "anatomy": {
            "tier1": "Bàn trưng bày nông sản xuất sắc với các khay đựng gạo thuần chủng ST24, ST25, Đài Thơm 8 và OM18 hạt thon dài trong suốt.",
            "tier2": "Bát cơm trắng nấu từ gạo ST25 bốc hơi nghi ngút, hạt cơm bóng bẩy, dẻo thơm hương lá dứa tự nhiên.",
            "tier3": "Cú máy cận cảnh bát cơm ST25 dẻo thơm bốc khói mềm mại (Close-up shot of steaming bowl of fragrant ST25 rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an elegant presentation of premium Vietnamese rice varieties: labeled wooden trays of slender translucent ST25, Dai Thom 8, and OM18 grains beside a steaming ceramic bowl of cooked fragrant white rice",
        "setting": "a culinary exhibition pavilion in warm ivory cream and golden ambient lighting",
        "motion": "Slow close-up panning shot over the slender fragrant raw grains to steaming cooked rice"
    },
    {
        "id": "CH05_SC018",
        "dur": "3.41s",
        "words": 13,
        "text": "Họ xuất khẩu những dòng gạo này sang các thị trường khó tính",
        "anatomy": {
            "tier1": "Kệ hàng siêu thị cao cấp tại Tokyo, Paris hoặc California với các bao gạo thơm ST25 đóng túi hút chân không trang nhã.",
            "tier2": "Người tiêu dùng quốc tế chọn mua gạo thơm Việt Nam với tem chứng nhận tiêu chuẩn an toàn thực phẩm khắt khe.",
            "tier3": "Cú máy trượt ngang qua kệ hàng siêu thị cao cấp quốc tế (Horizontal tracking shot past gourmet international grocery shelves)."
        },
        "overlay": None,
        "ref": None,
        "subj": "shelves of a high-end gourmet supermarket in Tokyo or Paris displaying elegantly branded vacuum-packed bags of Vietnamese ST25 Jasmine and fragrant rice",
        "setting": "a sophisticated upscale international grocery interior under warm boutique spotlights",
        "motion": "Smooth horizontal tracking shot past the premium packaged Vietnamese rice bags"
    },
    {
        "id": "CH05_SC019",
        "dur": "3.67s",
        "words": 14,
        "text": "với mức giá từ sáu trăm đến gần chín trăm đô la một tấn.",
        "anatomy": {
            "tier1": "Hợp đồng ngoại thương xuất khẩu gạo thơm đóng mộc giao dịch quốc tế.",
            "tier2": "Mức giá xuất khẩu ấn tượng từ 600 USD đến gần 900 USD/tấn khẳng định giá trị vượt trội của hạt gạo thơm Việt Nam.",
            "tier3": "Cú máy tĩnh trực diện vào khung giá xuất khẩu 600 - 900 USD/tấn (Steady shot on $600 - $900/ton export price tier) cùng text overlay góc trái dưới."
        },
        "overlay": "GIÁ XUẤT KHẨU: 600 - 900 USD/TẤN",
        "ref": None,
        "subj": "an export sales invoice and commodity trade index showing premium pricing tiers for Vietnamese fragrant rice ranging from 600 to nearly 900 USD per metric ton",
        "setting": "an agricultural export sales office in warm amber tones",
        "motion": "Steady camera shot framing the premium export pricing contracts"
    },
    {
        "id": "CH05_SC020",
        "dur": "3.94s",
        "words": 15,
        "text": "Lý do rất đơn giản: Cùng một công chăm sóc và chi phí phân bón",
        "anatomy": {
            "tier1": "Bảng hạch toán chi phí canh tác của nông hộ: Chi phí phân bón, thuốc bảo vệ thực vật và công lao động trên 1 ha.",
            "tier2": "Chi phí đầu vào canh tác giữa lúa thường và lúa thơm cao cấp gần như tương đương nhau.",
            "tier3": "Cú máy đẩy chậm vào bảng so sánh chi phí canh tác đầu vào (Slow push-in on agricultural input cost ledger)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a farmer financial ledger on a wooden farm table showing identical input costs for fertilizer, irrigation, and field labor per hectare",
        "setting": "a comfortable farmhouse veranda overlooking lush green rice fields in warm afternoon sun",
        "motion": "Slow push-in shot toward the input cost calculation ledger"
    },
    {
        "id": "CH05_SC021",
        "dur": "4.46s",
        "words": 17,
        "text": "nếu trồng các giống lúa khô xốp giá rẻ, người nông dân hầu như không có lời.",
        "anatomy": {
            "tier1": "Bao lúa giống khô xốp truyền thống giá rẻ với mức giá thương lái thu mua tại ruộng rất thấp.",
            "tier2": "Biểu đồ lợi nhuận ròng của nông dân khi trồng giống cũ mỏng dính, biên lợi nhuận bấp bênh chỉ vài phần trăm.",
            "tier3": "Cú máy trượt ngang qua bao thóc khô xốp giá rẻ (Horizontal tracking shot past low-margin commercial grain sacks)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a humble sack of old generic low-yield commercial grain with a small profit margin margin indicator showing near-zero net farmer earnings",
        "setting": "a rustic farm storage shed in warm natural light",
        "motion": "Slow horizontal tracking shot past the low-return grain bags"
    },
    {
        "id": "CH05_SC022",
        "dur": "3.15s",
        "words": 12,
        "text": "Thay vào đó, khi chuyển sang các giống lúa thơm cao cấp",
        "anatomy": {
            "tier1": "Ruộng lúa thơm ST25 trĩu hạt vàng rực, bông lúa uốn cong hình lưỡi liềm đẹp như tranh vẽ.",
            "tier2": "Nụ cười rạng rỡ của người nông dân miền Tây bên chiếc máy gặt đập đang dỡ lúa thơm bán thẳng cho doanh nghiệp bao tiêu.",
            "tier3": "Cú máy nâng chậm từ bông lúa thơm lên nụ cười phấn khởi của người nông dân (Slow tilt-up from fragrant rice stalk to happy farmer)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a sunlit field of golden premium ST25 fragrant rice being harvested by a modern red combine while a local farmer in conical hat smiles proudly beside full grain hoppers",
        "setting": "a prosperous rural Mekong farm in Soc Trang under glorious morning sun",
        "motion": "Slow tilt-up from heavy golden rice panicles to the beaming farmer in the sunlight"
    },
    {
        "id": "CH05_SC023",
        "dur": "4.99s",
        "words": 19,
        "text": "họ bán được giá cao hơn rất nhiều, tối ưu hóa thu nhập trên mỗi héc ta canh tác.",
        "anatomy": {
            "tier1": "Bàn thanh toán hợp đồng bao tiêu lúa giữa doanh nghiệp xuất khẩu và hợp tác xã nông nghiệp.",
            "tier2": "Người nông dân nhận tiền bán lúa thơm với lợi nhuận ròng gấp rưỡi, gấp đôi so với trước kia.",
            "tier3": "Cú máy trượt ngang qua bàn giao tiền và hợp đồng bao tiêu được ký kết (Horizontal tracking shot past contract settlement table)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an agricultural cooperative payout session where farmer cooperative members receive premium purchase receipts and revenue disbursements from export enterprise representatives",
        "setting": "a clean sunlit cooperative community center in warm golden morning light",
        "motion": "Horizontal tracking shot past contract settlements and farmer payment ledgers"
    },
    {
        "id": "CH05_SC024",
        "dur": "5.25s",
        "words": 20,
        "text": "Thế nhưng, chính sự nâng cấp đó lại tạo ra một khoảng trống lớn ngay tại thị trường nội địa.",
        "anatomy": {
            "tier1": "Sơ đồ cung cầu nông sản quốc gia với một bên là phân khúc gạo thơm xuất khẩu tràn đầy, một bên là ô trống thiếu hụt nguyên liệu chế biến.",
            "tier2": "Biểu tượng khoảng trống thị trường (Market Gap) xuất hiện giữa nhu cầu chế biến ẩm thực và nguồn cung lúa thơm cao cấp.",
            "tier3": "Cú máy đẩy chậm vào khoảng trống thị trường nguyên liệu chế biến (Slow push-in on industrial raw material supply gap)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an infographic showing domestic market divergence: abundant high-end fragrant rice dedicated to export creating an empty supply void for everyday industrial food processing",
        "setting": "an economic research analysis display in warm amber tones",
        "motion": "Slow push-in shot highlighting the domestic industrial processing supply gap"
    },
    {
        "id": "CH05_SC025",
        "dur": "3.67s",
        "words": 14,
        "text": "Ẩm thực Việt Nam là một nền văn hóa gắn liền với hạt gạo.",
        "anatomy": {
            "tier1": "Một mâm cỗ truyền thống Việt Nam với các món ăn tinh hoa chế biến từ hạt gạo thơm ngon.",
            "tier2": "Bánh chưng xanh, bánh tét, bánh tráng nướng, xôi gấc và những món ăn truyền thống thấm đẫm văn hóa lúa nước.",
            "tier3": "Cú máy trượt tròn chậm quanh mâm ẩm thực lúa gạo truyền thống (Slow orbital shot around traditional Vietnamese rice-based culinary banquet)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an artistic overhead arrangement of traditional Vietnamese cuisine celebrating the heritage of rice: steaming bowls of pho, fresh bun noodles, spring rolls, and regional rice delicacies on ceramic tableware",
        "setting": "a warm wooden heritage dining room in warm candlelight and soft morning sunlight",
        "motion": "Slow circular orbit shot around the vibrant Vietnamese rice gastronomy feast"
    },
    {
        "id": "CH05_SC026",
        "dur": "4.46s",
        "words": 17,
        "text": "Mỗi ngày, một trăm triệu người dân không chỉ ăn cơm trắng trong bữa ăn gia đình.",
        "anatomy": {
            "tier1": "Đại lộ ẩm thực buổi sáng tấp nập tại Hà Nội, Đà Nẵng hay TP.HCM ngập tràn hương vị ẩm thực đường phố.",
            "tier2": "Các quán phở, quán bún bò, quán hủ tiếu đông đúc thực khách thưởng thức bữa sáng nóng hổi trước giờ làm việc.",
            "tier3": "Cú máy trượt ngang qua dãy quán ăn sáng đường phố nhộn nhịp (Horizontal tracking shot past bustling breakfast street eateries)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a vibrant morning street scene in a Vietnamese city where customers gather at lively street noodle stalls enjoying steaming bowls of pho and bun under colorful awnings",
        "setting": "a sunlit urban boulevard lined with green trees in warm golden morning light",
        "motion": "Smooth horizontal tracking shot past lively breakfast noodle restaurants"
    },
    {
        "id": "CH05_SC027",
        "dur": "5.25s",
        "words": 20,
        "text": "Chúng ta tiêu thụ một khối lượng khổng lồ bún tươi, bánh phở, hủ tiếu, bánh tráng và bánh cuốn.",
        "anatomy": {
            "tier1": "Xưởng sản xuất bún sợi và bánh phở truyền thống với những vỉ phơi bánh tráng trắng tinh tươm thẳng tắp dưới nắng sớm.",
            "tier2": "Những rổ bún tươi trắng muốt, xấp bánh phở dẻo dai và chồng bánh tráng mỏng tang được vận chuyển đi phân phối khắp các chợ.",
            "tier3": "Cú máy tĩnh trực diện vào dây chuyền sản xuất bún phở bánh tráng (Steady shot on noodle and rice paper processing craft) cùng text overlay góc trái dưới."
        },
        "overlay": "TIÊU THỤ: BÚN, PHỞ, BÁNH TRÁNG, HỦ TIẾU",
        "ref": None,
        "subj": "a traditional artisanal Vietnamese rice processing workshop with woven bamboo racks of drying translucent rice paper and fresh white rice noodles (bun and pho) drying in clean morning sunshine",
        "setting": "a sun-drenched rural artisan village courtyard in southern Vietnam",
        "motion": "Steady camera shot framing the drying rice paper racks and noodle baskets"
    },
    {
        "id": "CH05_SC028",
        "dur": "3.41s",
        "words": 13,
        "text": "Bên cạnh đó là nhu cầu nguyên liệu của các nhà máy bia",
        "anatomy": {
            "tier1": "Nhà máy bia hiện đại công suất lớn với các bồn lên men bằng thép không gỉ sáng bóng.",
            "tier2": "Dây chuyền tiếp nhận gạo tấm làm nguyên liệu phụ trợ lên men giúp tạo nên vị bia trong và thanh nhẹ.",
            "tier3": "Cú máy nâng chậm theo thân các bồn lên men bia khổng lồ (Slow upward tilt along towering stainless steel brewing vats)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the gleaming industrial fermentation hall of a modern commercial brewery with towering stainless steel brewing vats where broken rice is utilized as an adjunct brewing ingredient",
        "setting": "a high-tech beverage manufacturing facility illuminated by warm architectural lights",
        "motion": "Slow upward tilt along the gleaming industrial beer fermentation tanks"
    },
    {
        "id": "CH05_SC029",
        "dur": "3.94s",
        "words": 15,
        "text": "nhà máy cồn thực phẩm và các tập đoàn sản xuất thức ăn chăn nuôi.",
        "anatomy": {
            "tier1": "Khu công nghiệp chế biến thức ăn gia súc và cồn thực phẩm với các xi-lô nạp nguyên liệu hạt ngũ cốc.",
            "tier2": "Băng tải tự động vận chuyển hàng ngàn tấn gạo tấm giá rẻ vào máy nghiền phối trộn cám công nghiệp.",
            "tier3": "Cú máy trượt ngang theo băng chuyền nguyên liệu thức ăn chăn nuôi (Horizontal tracking shot along animal feed grain conveyor)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an automated industrial feed milling and ethanol processing complex with conveyor belts moving bulk broken grain into mixing hoppers for livestock feed production",
        "setting": "a modern agro-industrial plant under warm ambient daylight",
        "motion": "Slow horizontal tracking shot following bulk grain along industrial conveyor lines"
    },
    {
        "id": "CH05_SC030",
        "dur": "3.67s",
        "words": 14,
        "text": "Ở đây xuất hiện một nguyên lý hóa sinh thực phẩm rất thú vị.",
        "anatomy": {
            "tier1": "Phòng thí nghiệm công nghệ thực phẩm với kính hiển vi phân tích cấu trúc tinh bột hạt gạo.",
            "tier2": "Mô hình cấu trúc phân tử tinh bột hạt gạo: Phân tử amylose dạng mạch thẳng so sánh với amylopectin dạng mạch nhánh.",
            "tier3": "Cú máy đẩy chậm vào mô hình phân tử tinh bột hạt gạo (Slow push-in on starch molecular structure model)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a food science biochemistry laboratory with an analytical monitor displaying the 3D molecular structure of rice starch, showing linear amylose chains versus branched amylopectin",
        "setting": "a food technology research lab in warm cream and amber interior lighting",
        "motion": "Slow push-in shot toward the food biochemistry molecular model of rice starch"
    },
    {
        "id": "CH05_SC031",
        "dur": "4.46s",
        "words": 17,
        "text": "Để sợi bún dai ngon, sợi phở không bị nát hay bánh tráng không bị dính bết",
        "anatomy": {
            "tier1": "Bếp làm bánh cuốn và bún tươi truyền thống nơi người thợ khéo léo tráng từng mẻ bánh mỏng tang trên nồi hơi.",
            "tier2": "Sợi bún tươi kéo dài dai ngon, sợi phở trong vắt không bị gãy vụn, chứng minh vai trò cốt tử của loại bột gạo chuẩn.",
            "tier3": "Cú máy trượt ngang theo sợi bún tươi trắng dẻo dai nhấc khỏi khuôn (Horizontal tracking shot following resilient rice noodles lifted from extruder)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an artisanal noodle master inspecting fresh steamed rice noodles, gently lifting clean white resilient strands that remain intact and non-sticky",
        "setting": "a traditional clean noodle kitchen filled with soft warm steam and morning sun",
        "motion": "Smooth horizontal tracking shot following the resilient rice noodles lifted from cooling racks"
    },
    {
        "id": "CH05_SC032",
        "dur": "6.56s",
        "words": 25,
        "text": "thợ làm nghề bắt buộc phải dùng gạo có hàm lượng amylose cao. Đó phải là loại gạo khô, nở xốp và hút ít nước.",
        "anatomy": {
            "tier1": "Bảng phân tích hóa lý ngũ cốc tại Viện Công nghệ Thực phẩm: Chỉ số Amylose > 25% là tiêu chuẩn vàng cho sợi bún bánh.",
            "tier2": "Nắm gạo khô nở xốp (như IR50404 hoặc lúa Campuchia) rơi qua kẽ tay, hạt gạo cứng cáp, hút ít nước và cho bột ráo.",
            "tier3": "Cú máy tĩnh trực diện vào chỉ số Amylose >25% và hạt gạo khô xốp (Steady shot on High Amylose >25% biochemical standard) cùng text overlay góc trái dưới."
        },
        "overlay": "HÓA SINH: GẠO AMYLOSE CAO (> 25%)",
        "ref": None,
        "subj": "a grain testing tray with high-amylose white rice grains falling through fingers beside a biochemical lab report reading 'Amylose Content > 25%' for optimal noodle and wrapper firmness",
        "setting": "a cereal testing laboratory in warm analytical light",
        "motion": "Steady camera shot framing the falling high-amylose grains and scientific threshold badge"
    },
    {
        "id": "CH05_SC033",
        "dur": "4.2s",
        "words": 16,
        "text": "Nếu lấy gạo thơm dẻo như ST25 đem đi làm bún, sợi bánh sẽ nhão nát",
        "anatomy": {
            "tier1": "Nồi hấp bánh thử nghiệm trong phòng nghiên cứu chế biến món ăn.",
            "tier2": "Mẻ bột làm từ gạo thơm dẻo bị nhão dính, sợi bún bị đứt gãy và bánh tráng dính bết vào vỉ hấp, không thể tạo hình.",
            "tier3": "Cú máy cận cảnh mẻ bánh bị dính nát do dùng sai loại gạo thơm dẻo (Close-up shot of over-sticky disintegrated noodle dough)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a culinary processing trial showing an unsuccessful noodle batch made from sticky ST25 fragrant rice: the noodles are overly soft, sticky, and clumping together on the bamboo mesh",
        "setting": "a food processing experimental kitchen under warm lighting",
        "motion": "Close-up slow pan over the clumping sticky noodle mixture illustrating the culinary error"
    },
    {
        "id": "CH05_SC034",
        "dur": "6.82s",
        "words": 26,
        "text": "dính bết và chi phí nguyên liệu sẽ đội lên gấp đôi. Bài toán kinh tế học xuất hiện một khoảng trống cung cầu rõ rệt.",
        "anatomy": {
            "tier1": "Bảng tính toán giá thành của xưởng bún: Dùng gạo ST25 đắt gấp đôi gạo thường sẽ đẩy giá bát bún, bát phở lên trời.",
            "tier2": "Chủ lò bún lắc đầu trước bài toán chi phí bất khả thi, khẳng định sự cần thiết phải có nguồn gạo khô xốp giá rẻ.",
            "tier3": "Cú máy đẩy chậm vào bảng so sánh chi phí nguyên liệu đội lên gấp đôi (Slow push-in on doubled raw material cost calculation)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a cost accounting ledger for an artisanal noodle factory showing that using expensive fragrant rice doubles raw material expenditures, causing commercial unviability",
        "setting": "a workshop office in a craft village in warm ambient desk lighting",
        "motion": "Slow push-in shot framing the cost divergence ledger of noodle manufacturing"
    },
    {
        "id": "CH05_SC035",
        "dur": "5.77s",
        "words": 22,
        "text": "Thị trường chế biến nội địa khát gạo khô xốp, nhưng nông dân trong nước lại chỉ trồng gạo thơm cao cấp.",
        "anatomy": {
            "tier1": "Sơ đồ đối lập hai cực kinh tế: Một bên là hàng vạn lò bún phở cần gạo khô xốp giá rẻ; Một bên là cánh đồng miền Tây chỉ thu hoạch gạo thơm xuất khẩu.",
            "tier2": "Nghịch lý cung cầu hiện lên rõ nét: Khát nguyên liệu thô tại chỗ trong khi hạt gạo làm ra lại hướng trọn ra thế giới.",
            "tier3": "Cú máy tĩnh trực diện vào sơ đồ nghịch lý cung cầu chế biến (Steady shot on processing supply-demand paradox diagram) cùng text overlay góc trái dưới."
        },
        "overlay": "NGHỊCH LÝ CUNG - CẦU CHẾ BIẾN",
        "ref": None,
        "subj": "an editorial balance graphic illustrating the domestic supply mismatch: high demand for dry high-amylose grain by domestic food artisans versus local farmers dedicated solely to premium export jasmine varieties",
        "setting": "an agricultural economics seminar screen in warm amber tones",
        "motion": "Steady camera shot framing the domestic processing supply-demand dilemma"
    },
    {
        "id": "CH05_SC036",
        "dur": "3.94s",
        "words": 15,
        "text": "Và đó chính là lúc năng lực thương mại quốc tế phát huy tác dụng.",
        "anatomy": {
            "tier1": "Trung tâm điều hành thương mại nông sản quốc tế với các tuyến giao thương đường thủy kết nối Mekong.",
            "tier2": "Các chuyên gia thương mại nông nghiệp điều phối dòng chảy lúa gạo đa chiều giữa xuất khẩu và nhập khẩu.",
            "tier3": "Cú máy trượt ngang qua sơ đồ dòng chảy thương mại đa chiều (Horizontal tracking shot across multi-directional trade flow display)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an international commodity trade desk with maritime route monitors showing inbound raw grain barges intersecting with outbound high-grade container ships",
        "setting": "a contemporary commercial trading floor illuminated by warm amber data screens",
        "motion": "Slow horizontal tracking shot across the dynamic cross-border commodity flow monitors"
    },
    {
        "id": "CH05_SC037",
        "dur": "3.15s",
        "words": 12,
        "text": "Chúng ta xuất khẩu gạo thơm sang thế giới với giá cao",
        "anatomy": {
            "tier1": "Tàu viễn dương chở gạo thơm đóng bao xuất khẩu rời cảng Cát Lái ra khơi trong ánh ban mai rạng rỡ.",
            "tier2": "Các container gạo ST25 và Jasmine được xuất khẩu với mức giá cao 700 - 900 USD/tấn đem lại thặng dư ngoại tệ lớn.",
            "tier3": "Cú máy nâng chậm từ boong tàu lên cánh buồm và bầu trời trong xanh (Slow upward tilt along ship hull toward sunlit morning sky)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a modern ocean cargo vessel loaded with containers of premium Vietnamese jasmine rice departing a southern port terminal into sunlit open waters",
        "setting": "the open shipping channel of Soai Rap river under bright warm morning daylight",
        "motion": "Slow upward tilt from ship bow toward the sunlit horizon and departing cargo vessel"
    },
    {
        "id": "CH05_SC038",
        "dur": "4.46s",
        "words": 17,
        "text": "rồi nhập khẩu lúa thô từ Campuchia hay gạo Ấn Độ với giá chỉ bằng một nửa.",
        "anatomy": {
            "tier1": "Bến sông bốc dỡ lúa tươi Campuchia tại An Giang với các ghe gỗ chở lúa thô cập bến.",
            "tier2": "Biểu đồ so sánh giá: Nhập lúa thô và gạo tấm với giá rẻ chỉ bằng một nửa (300 - 400 USD/tấn) so với giá gạo thơm xuất khẩu.",
            "tier3": "Cú máy tĩnh trực diện vào con số chênh lệch giá nhập rẻ hơn 50% (Steady shot on 50% cheaper raw import price margin) cùng text overlay góc trái dưới."
        },
        "overlay": "CHÊNH LỆCH GIÁ: GẠO THÔ RẺ HƠN 50%",
        "ref": None,
        "subj": "a lively river unloading jetty where golden raw unhusked paddy from Cambodian riverboats is unloaded by conveyor belts beside a comparative price metric showing raw grain priced at 50 percent of export value",
        "setting": "a bustling Mekong river wharf in An Giang bathed in warm morning sunshine",
        "motion": "Steady camera shot framing the riverboat grain unloading and price differential badge"
    },
    {
        "id": "CH05_SC039",
        "dur": "6.3s",
        "words": 24,
        "text": "Nông dân Campuchia có diện tích đất rộng lớn nhưng thiếu hệ thống máy móc xay xát và công nghệ chế biến hiện đại.",
        "anatomy": {
            "tier1": "Cánh đồng lúa mênh mông bát ngát tại tỉnh Takeo hoặc Prey Veng (Campuchia) với những rặng thốt nốt đặc trưng.",
            "tier2": "Nông dân Campuchia thu hoạch lúa thủ công hoặc bằng máy nhỏ, chất lúa lên xe bò hoặc xe kéo ra bờ kênh nhưng thiếu nhà máy sấy lúa hiện đại.",
            "tier3": "Cú máy góc rộng lia qua cánh đồng thốt nốt Campuchia (Wide cinematic pan across Cambodian sugar palm rice plain)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an expansive rural rice plain in Cambodia dotted with iconic sugar palm trees under warm sun, where farmers harvest ample raw paddy but lack localized large-scale drying and automated milling facilities",
        "setting": "a tranquil countryside in Takeo province Cambodia under warm morning sun",
        "motion": "Slow wide cinematic pan across the boundless sugar palm landscape and raw paddy fields"
    },
    {
        "id": "CH05_SC040",
        "dur": "3.94s",
        "words": 15,
        "text": "Việt Nam tận dụng hạ tầng logistics và các cụm nhà máy xay xát khổng",
        "anatomy": {
            "tier1": "Toàn cảnh cụm nhà máy chế biến lúa gạo hiện đại ven sông Hậu tại Thốt Nốt (Cần Thơ).",
            "tier2": "Dãy xi-lô sấy lúa khổng lồ và hệ thống cầu cảng tiếp nhận sà lan nước sâu hoạt động ngày đêm.",
            "tier3": "Cú máy bay chậm dọc theo cụm công nghiệp xay xát Thốt Nốt ven sông Hậu (Slow aerial glide along Thot Not rice processing cluster)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a grand industrial view of a state-of-the-art rice processing and milling conglomerate along the Hau River with banks of steel drying silos and deep-water barge berths",
        "setting": "the industrial riverside district of Thot Not Can Tho under warm afternoon sunshine",
        "motion": "Slow aerial glide along the modern riverfront industrial milling silos"
    },
    {
        "id": "CH05_SC041",
        "dur": "3.94s",
        "words": 15,
        "text": "lồ tại Thốt Nốt hay Cái Bè để thu mua lúa thô về tinh chế.",
        "anatomy": {
            "tier1": "Bên trong nhà máy xay xát Cái Bè (Tiền Giang) với các dàn máy bóc vỏ, tách màu quang học tự động.",
            "tier2": "Hàng ngàn tấn lúa tươi nhập khẩu được sấy khô, xay xát và phân loại thành phẩm nhanh chóng, chính xác.",
            "tier3": "Cú máy tĩnh trực diện vào cụm nhà máy Thốt Nốt & Cái Bè (Steady shot on Thot Not & Cai Be milling complexes) cùng text overlay góc trái dưới."
        },
        "overlay": "TRUNG TÂM XAY XÁT: THỐT NỐT & CÁI BÈ",
        "ref": None,
        "subj": "the interior of an automated high-capacity rice milling factory in Cai Be with rows of vibrating sorters, optical color-sorting machines, and packaging belts processing raw grain",
        "setting": "a modern well-lit industrial processing hall in warm ambient lighting",
        "motion": "Steady camera shot framing the automated color sorting machinery in action"
    },
    {
        "id": "CH05_SC042",
        "dur": "3.67s",
        "words": 14,
        "text": "Dòng lúa nhập khẩu đó giải quyết trọn vẹn bài toán nguyên liệu cho",
        "anatomy": {
            "tier1": "Kho chứa bột gạo công nghiệp của nhà máy chế biến thực phẩm tại Long An hoặc Bình Dương.",
            "tier2": "Các bao bột gạo khô xốp xay từ lúa nhập khẩu xếp ngay ngắn, sẵn sàng cấp cho các dây chuyền sản xuất.",
            "tier3": "Cú máy trượt ngang qua kho nguyên liệu bột gạo dồi dào (Horizontal tracking shot past plentiful processed flour bags)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a clean commercial storage hall stacked neatly with pallets of uniform white rice flour sacks designated for domestic food manufacturers",
        "setting": "a modern food ingredient logistics warehouse in warm natural light",
        "motion": "Slow horizontal tracking shot past neatly stacked processed rice flour pallets"
    },
    {
        "id": "CH05_SC043",
        "dur": "3.67s",
        "words": 14,
        "text": "các làng nghề bún phở và nhà máy chế biến thực phẩm trong nước.",
        "anatomy": {
            "tier1": "Một làng nghề làm bún phở truyền thống lâu đời tại miền Tây hoặc miền Bắc rộn rã tiếng cười và hơi nước ấm áp.",
            "tier2": "Các lò bún phở nhận nguồn nguyên liệu bột gạo khô xốp ổn định, giá rẻ, cho ra lò những mẻ bún phở thơm ngon phục vụ người dân.",
            "tier3": "Cú máy trượt ngang qua làng nghề bún phở nhộn nhịp sản xuất (Horizontal tracking shot past bustling traditional noodle craft village)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a bustling traditional craft village dedicated to fresh pho noodle and wrapper production, with family workshops busily packing fresh noodles for morning deliveries",
        "setting": "a sunlit village lane lined with brick cottages and bamboo drying racks under warm morning light",
        "motion": "Slow horizontal tracking shot along the vibrant craft village workshops"
    },
    {
        "id": "CH05_SC044",
        "dur": "6.3s",
        "words": 24,
        "text": "Đồng thời, nó giải phóng toàn bộ đất đai miền Tây để tập trung sản xuất các dòng gạo xuất khẩu giá trị cao.",
        "anatomy": {
            "tier1": "Cánh đồng mẫu lớn ĐBSCL thẳng cánh cò bay, toàn bộ diện tích được phủ kín bởi lúa thơm ST25 và Đài Thơm 8.",
            "tier2": "Đất đai màu mỡ được giải phóng khỏi lúa phẩm cấp thấp, tối đa hóa giá trị gia tăng và doanh thu xuất khẩu ngoại tệ.",
            "tier3": "Cú máy bay cao lướt trên cánh đồng lúa thơm bạt ngàn (Panoramic aerial glide over high-value export rice acreage)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a breathtaking aerial glide across sweeping Mekong Delta farmland entirely dedicated to high-value fragrant rice crops, symbolizing optimized agricultural land allocation",
        "setting": "the sunlit fertile plains of the southern delta under warm golden skies",
        "motion": "Breathtaking panoramic aerial glide over the vast high-value agricultural paddies"
    },
    {
        "id": "CH05_SC045",
        "dur": "5.77s",
        "words": 22,
        "text": "Đây chính là dấu hiệu của một quốc gia đã bước lên nấc thang cao hơn trong chuỗi giá trị nông nghiệp.",
        "anatomy": {
            "tier1": "Biểu đồ nấc thang giá trị gia tăng kinh tế học (Agricultural Smile Curve) trên màn hình phân tích.",
            "tier2": "Việt Nam vươn lên hai đầu nấc thang giá trị: Đầu nghiên cứu giống lúa cao cấp và đầu chế biến tinh chế thương hiệu, thay vì chỉ ở đáy bán thô.",
            "tier3": "Cú máy đẩy chậm vào nấc thang chuỗi giá trị nông nghiệp (Slow push-in on agricultural value-chain smile curve)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an analytical economic presentation displaying the agricultural value-added 'Smile Curve', highlighting Vietnam rising from raw cultivation into advanced processing, branding, and regional trade",
        "setting": "a strategic policy boardroom in warm amber and cream tones",
        "motion": "Slow push-in shot toward the ascending value-chain smile curve diagram"
    },
    {
        "id": "CH05_SC046",
        "dur": "3.94s",
        "words": 15,
        "text": "Việt Nam không còn là nơi chỉ biết bán thô những gì mình trồng được.",
        "anatomy": {
            "tier1": "Hình ảnh tương phản lịch sử: Thập niên trước bán gạo thô xá trong bao gai; Ngày nay đóng gói chân không thương hiệu cao cấp.",
            "tier2": "Sự chuyển mình từ người nông dân thuần túy bán thô sang nhà kinh doanh nông nghiệp am hiểu thị trường toàn cầu.",
            "tier3": "Cú máy trượt ngang qua hai thế hệ bao bì hạt gạo Việt Nam (Horizontal tracking shot past historical packaging evolution)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a side-by-side conceptual display of vintage generic burlap grain sacks from past decades beside modern sleek premium branded vacuum-pack rice cartons",
        "setting": "an agricultural heritage exhibition room in warm diffused lighting",
        "motion": "Slow horizontal tracking shot showing the evolution from raw bulk commodity to refined consumer brand"
    },
    {
        "id": "CH05_SC047",
        "dur": "6.56s",
        "words": 25,
        "text": "Chúng ta đang âm thầm vận hành như một trung tâm điều phối và tinh chế lương thực cho toàn bộ tiểu vùng sông Mekong.",
        "anatomy": {
            "tier1": "Bản đồ tiểu vùng sông Mekong (Việt Nam, Campuchia, Lào) với mạng lưới sông ngòi và các cụm cảng chế biến hạt gạo.",
            "tier2": "Đồng bằng sông Cửu Long tỏa sáng như trái tim điều phối: Nhập lúa thô, tinh chế công nghệ cao và xuất khẩu đi toàn cầu.",
            "tier3": "Cú máy tĩnh trực diện vào bản đồ Trung tâm Tinh chế Tiểu vùng Mekong (Steady shot on Mekong Subregion Refining Hub map) cùng text overlay góc trái dưới."
        },
        "overlay": "TRUNG TÂM TINH CHẾ TIỂU VÙNG MEKONG",
        "ref": None,
        "subj": "a comprehensive regional map of the Lower Mekong Basin highlighting the southern delta of Vietnam as the central processing, refining, and maritime logistics hub for neighboring nations",
        "setting": "a regional geopolitical and agronomic monitoring room in warm amber hues",
        "motion": "Steady camera shot framing the regional Mekong refining hub master diagram"
    },
    {
        "id": "CH05_SC048",
        "dur": "6.82s",
        "words": 26,
        "text": "Chúng ta bán sự tinh xảo, bán thương hiệu cao cấp, và nhập khẩu nguyên liệu thô cơ bản để phục vụ chế biến công nghiệp.",
        "anatomy": {
            "tier1": "Hình ảnh biểu tượng: Một bên là hộp gạo ST25 mạ vàng xuất khẩu sang châu Âu; Một bên là dòng bột gạo công nghiệp trắng ngần phục vụ ẩm thực nội địa.",
            "tier2": "Sự phân công lao động hoàn hảo: Xuất khẩu tinh hoa thu ngoại tệ cao, nhập khẩu nguyên liệu cơ bản nuôi dưỡng chuỗi chế biến trong nước.",
            "tier3": "Cú máy trượt ngang qua hai dòng sản phẩm tinh xảo và cơ bản (Horizontal tracking shot past premium export and industrial food staples)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a beautiful editorial still life featuring an award-winning premium ST25 gift box beside pure white rice flour and artisan noodle bundles under soft warm sunlight",
        "setting": "a culinary design studio in warm ivory and walnut wood tones",
        "motion": "Slow horizontal tracking shot past the dual pillars of premium branding and industrial staple processing"
    },
    {
        "id": "CH05_SC049",
        "dur": "3.41s",
        "words": 13,
        "text": "Thế nhưng, một bài toán cân não khác lại lập tức xuất hiện.",
        "anatomy": {
            "tier1": "Phòng phân tích thị trường nông sản quốc tế khi đồng hồ chuyển sang phiên giao dịch mới đầy căng thẳng.",
            "tier2": "Biểu đồ biến động giá ngũ cốc quốc tế bắt đầu xuất hiện những tín hiệu đảo chiều bất thường.",
            "tier3": "Cú máy đẩy chậm vào màn hình thị trường tài chính hàng hóa (Slow push-in toward market volatility ticker screen)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a commodity market terminal displaying sudden price volatility alerts and flashing international trade signals in warm amber tones",
        "setting": "an agricultural export analytics desk in early evening warm lamplight",
        "motion": "Slow push-in shot toward the market volatility alert on the monitor"
    },
    {
        "id": "CH05_SC050",
        "dur": "4.72s",
        "words": 18,
        "text": "Khi chúng ta tự tin đứng trên đỉnh cao kỷ lục xuất khẩu gần sáu tỷ đô la",
        "anatomy": {
            "tier1": "Hội nghị thường niên Hiệp hội Lương thực Việt Nam (VFA) chúc mừng cột mốc kỷ lục xuất khẩu gạo gần 6 tỷ USD.",
            "tier2": "Các doanh nghiệp xuất khẩu vui mừng nâng ly chúc mừng thắng lợi lịch sử dưới ánh đèn chùm rực rỡ.",
            "tier3": "Cú máy trượt ngang qua lễ vinh danh kỷ lục xuất khẩu gần 6 tỷ USD (Horizontal tracking shot past celebratory export milestone gala)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a celebratory gala event of the Vietnam Food Association with corporate leaders gathering beside an elegant golden ice sculpture and banner celebrating nearly 6 billion USD in rice exports",
        "setting": "a grand conference ballroom in warm champagne and golden chandelier lighting",
        "motion": "Slow horizontal tracking shot past the celebratory export achievement banner"
    },
    {
        "id": "CH05_SC051",
        "dur": "4.99s",
        "words": 19,
        "text": "thị trường quốc tế không bao giờ là một dòng sông phẳng lặng. Vào giai đoạn 2024 đến 2025",
        "anatomy": {
            "tier1": "Cửa biển mở ra đại dương bao la với những đợt sóng ngầm cuồn cuộn dưới ánh hoàng hôn vàng cam pha sắc đỏ.",
            "tier2": "Hình ảnh ẩn dụ về thị trường lúa gạo quốc tế tiềm ẩn những cơn sóng thần địa chính trị bất ngờ.",
            "tier3": "Cú máy hạ thấp lướt trên mặt sóng biển hoàng hôn (Low-angle tracking shot over ocean waves at sunset)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic wide seascape of ocean swells reflecting deep amber and copper sunset light, symbolizing the volatile geopolitical undercurrents of the global food market",
        "setting": "the open ocean off the southern coast at sunset under warm golden-hour skies",
        "motion": "Low-angle smooth tracking shot skimming over warm ocean swells into the sunset"
    },
    {
        "id": "CH05_SC052",
        "dur": "3.41s",
        "words": 13,
        "text": "gã khổng lồ Ấn Độ sau hai năm đóng cửa đã bất ngờ",
        "anatomy": {
            "tier1": "Dinh Thủ tướng hoặc Tòa nhà Quốc hội Ấn Độ tại New Delhi dưới ánh nắng chiều vàng ấm.",
            "tier2": "Thủ tướng Ấn Độ Narendra Modi chủ trì phiên họp chính sách kinh tế đối ngoại, chuẩn bị dỡ bỏ các rào cản xuất khẩu gạo.",
            "tier3": "Cú máy đẩy chậm vào Thủ tướng Narendra Modi trong phòng họp nội các New Delhi (Slow push-in on Prime Minister Narendra Modi in New Delhi cabinet hall)."
        },
        "overlay": None,
        "ref": "modi_india.jpg",
        "subj": "Indian Prime Minister Narendra Modi seated at the head of a formal government cabinet table in New Delhi reviewing trade decrees, preparing to dismantle rice export bans",
        "setting": "the official cabinet meeting room in New Delhi with rich warm wood paneling and warm interior lighting",
        "motion": "Slow push-in shot toward Prime Minister Narendra Modi during the strategic cabinet briefing"
    },
    {
        "id": "CH05_SC053",
        "dur": "3.67s",
        "words": 14,
        "text": "mở toang các kho dự trữ khổng lồ để xả hàng ra thế giới.",
        "anatomy": {
            "tier1": "Khu kho dự trữ lương thực khổng lồ của Tổng công ty Lương thực Ấn Độ (FCI) mở toang các cánh cửa thép.",
            "tier2": "Hàng chục triệu tấn gạo dự trữ ùa ra cảng biển Kandla và Kakinada, sẵn sàng tràn ngập thị trường thế giới với giá rẻ.",
            "tier3": "Cú máy tĩnh trực diện vào kho thóc mở toang và làn sóng xả hàng của Ấn Độ (Steady shot on India reopening strategic grain reserves) cùng text overlay góc trái dưới."
        },
        "overlay": "ẤN ĐỘ XẢ KHO DỰ TRỮ (2024 - 2025)",
        "ref": "modi_india.jpg",
        "subj": "the towering steel doors of massive Food Corporation of India grain warehouses opening wide with fleets of trucks moving millions of tons of stored rice toward export docks under warm dusty sunlight",
        "setting": "a colossal grain logistics depot in India under warm golden-hour daylight",
        "motion": "Steady camera shot framing the massive grain warehouse doors opening to global markets"
    },
    {
        "id": "CH05_SC054",
        "dur": "4.2s",
        "words": 16,
        "text": "Cơn bão giá ngược dòng đó đã dội vào ngành gạo Việt Nam như thế nào?",
        "anatomy": {
            "tier1": "Cảng xuất khẩu gạo Việt Nam lúc hoàng hôn với bóng các cần cẩu đứng sừng sững trước những con sóng biển.",
            "tier2": "Người thuyền trưởng và giám đốc doanh nghiệp xuất khẩu nhìn ra đường chân trời, chuẩn bị đối đầu với cơn bão giá đảo chiều từ Ấn Độ.",
            "tier3": "Cú máy nâng chậm từ mặt nước cảng biển lên chân trời hoàng hôn rực sắc cam ấm áp (Slow upward tilt from harbor waters toward warm twilight horizon)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an export dock in southern Vietnam at twilight with silhouettes of cranes and an executive looking out over the harbor, anticipating the oncoming international price war",
        "setting": "a quiet seaport quay under a glowing terracotta and amber evening sky",
        "motion": "Slow upward tilt from harbor reflection toward the dramatic warm evening horizon"
    }
]

# Generate Markdown Storyboard
md_lines = [
    "# chapter_05_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 5: Nghịch Lý Thương Mại: Tại Sao Cường Quốc Xuất Khẩu Lại Đi Mua Gạo Ngoại?",
    "## Phong cách chủ đạo: Luminous Warm Editorial Illustration (Minh họa báo chí cao cấp, ánh sáng trong trẻo rực rỡ, 100% không gian vật lý đời thực, triệt tiêu hoàn toàn siêu thực và màu đen u ám)",
    "",
    "### 🎨 Hệ màu 60-30-10 (Tuyệt Đối Ấm Áp — Chống Lạnh Lẽo):",
    "- **60% Tông màu nền chủ đạo:** Warm Ivory Cream (`#FAF7EE`), Warm Mekong Morning Glow (`#FFFBEB`), Warm Golden Amber Water (`#F3E5AB`). Tuyệt đối không dùng nền xám lạnh, xanh cyan buốt giá hay đen kịt.",
    "- **30% Đường nét & Chủ thể:** Ripe Jasmine Golden Amber (`#F59E0B`), Terracotta Brick & River Alluvium (`#EA580C`), Fresh Spring Paddy Green (`#10B981`), Polished Industrial Stainless Steel (`#D1D5DB`).",
    "- **10% Điểm nhấn dẫn mắt:** Luminous Warm Golden Sunrise Rays (`#D97706`), Steaming Noodle Craft Mist, Glowing Golden Amber Data Badges.",
    "",
    "---",
    "",
    "### 🛡️ Quy Tắc Kiểm Soát Tuyệt Đối:",
    "1. **Scene ID chuẩn theo chương:** `CH05_SC001` đến `CH05_SC054` (Khớp 100% với `scene_timing_map.json`).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Cửa khẩu đường thủy Vĩnh Xương/Thường Phước, cụm xay xát Thốt Nốt & Cái Bè, cánh đồng Sóc Trăng, làng nghề bún phở truyền thống, nhà máy bia, kho cảng Cái Mép/Cát Lái, cánh đồng thốt nốt Campuchia, Dinh New Delhi.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc đúng 11/54 phân cảnh (20.37%) có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. 43 phân cảnh còn lại để `[TEXT OVERLAY]: Không`.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Ảnh Tham Chiếu Nhân Vật / Địa Danh:**",
    "   - `@modi_india.jpg` sử dụng tại `CH05_SC052` & `CH05_SC053` (Thủ tướng Narendra Modi xả kho dự trữ Ấn Độ).",
    "   - Nhân vật dân sự (nông dân, thợ làm bún, kỹ sư): Tuyệt đối KHÔNG dùng ảnh tham chiếu nhân tạo, mô tả trực tiếp trong prompt.",
    "",
    "---",
    "",
    "| Phân Cảnh (Scene ID) | Thời Gian & Câu Thoại Voiceover | Mô Tả Bối Cảnh Thị Giác Chi Tiết (3-Tier Physical Anatomy) | Text Overlay (Selective Lower-Left 25%) |",
    "| :--- | :--- | :--- | :--- |"
]

for sc in scenes_data:
    sc_id = sc["id"]
    dur = sc["dur"]
    w = sc["words"]
    txt = sc["text"]
    t1 = sc["anatomy"]["tier1"]
    t2 = sc["anatomy"]["tier2"]
    t3 = sc["anatomy"]["tier3"]
    overlay = f'**"{sc["overlay"]}"**' if sc["overlay"] else "**Không**"
    ref_note = f"<br/>*(Tham chiếu: `@{sc['ref']}`)*" if sc.get("ref") else ""
    
    row = f'| **{sc_id}** | `{dur}` ({w} từ)<br/>*"{txt}"* | **Tầng 1 (Đế cố định):** {t1}<br/>**Tầng 2 (Chủ thể):** {t2}<br/>**Tầng 3 (Góc máy):** {t3}{ref_note} | {overlay} |'
    md_lines.append(row)

# Save chapter_05_visual.md
with open("episodes/vu-khi-gao-viet-nam/chapter_05_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_05_visual.md ({len(scenes_data)} scenes)")

# Generate prompts_chapter_05.txt
prompt_lines = []
for sc in scenes_data:
    sc_id = sc["id"]
    ref_tag = sc.get("ref")
    subj = sc["subj"]
    setting = sc["setting"]
    overlay = sc["overlay"]
    motion = sc["motion"]
    
    if ref_tag:
        img_prompt = f"{sc_id} [IMAGE]: @{ref_tag} -> A 2D warm cinematic editorial illustration of {subj}, set in {setting}, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ambient tone (#FAF7EE), luminous warm golden daylight, soft ambient shadows"
    else:
        img_prompt = f"{sc_id} [IMAGE]: A 2D warm cinematic editorial illustration of {subj}, set in {setting}, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ambient tone (#FAF7EE), luminous warm golden daylight, soft ambient shadows"
        
    if overlay:
        img_prompt += f', compact subtle glowing golden amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading "{overlay}"'
        
    img_prompt += ", no watermarks, 16:9"
    
    if overlay:
        vid_prompt = f"{sc_id} [VIDEO]: @{sc_id}.png -> {motion}, preserving the 2D vector graphic novel aesthetic, clean ink outlines, and all static graphic layers of the reference image exactly without any character morphing or alterations, 8-second continuous documentary video --ar 16:9 --dur 8s"
    else:
        vid_prompt = f"{sc_id} [VIDEO]: @{sc_id}.png -> {motion}, preserving the 2D vector graphic novel aesthetic, clean ink outlines, and all details of the reference image exactly, 8-second continuous documentary video --ar 16:9 --dur 8s"
        
    prompt_lines.append(img_prompt)
    prompt_lines.append(vid_prompt)
    prompt_lines.append("")

with open("episodes/vu-khi-gao-viet-nam/prompts_chapter_05.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompt_lines).strip() + "\n")

print(f"✅ Generated prompts_chapter_05.txt ({len(scenes_data)} scenes)")
