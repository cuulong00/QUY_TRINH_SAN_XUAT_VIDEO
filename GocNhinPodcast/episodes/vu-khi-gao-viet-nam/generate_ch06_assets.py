"""
Script to generate both chapter_06_visual.md and prompts_chapter_06.txt
for Episode 'Vũ Khí Lúa Gạo Việt Nam' - Chapter 06.
Strictly adheres to:
- Flow Batch Studio syntax
- Warm Luminous Editorial Palette (#FAF7EE, #F59E0B, #EA580C)
- Selective Lower-Left 25% Rule (~20% text overlay)
- Canonical references: @modi_india.jpg for CH06_SC008, CH06_SC019, CH06_SC021
- Steady camera and static text preservation in video prompts
"""

import re
import json

scenes_data = [
    {
        "id": "CH06_SC001",
        "dur": "6.82s",
        "words": 26,
        "text": "Nhìn lại chu kỳ phát triển những năm qua, ngành lúa gạo Việt Nam đã trải qua những khúc cua địa kinh tế đầy kịch tính.",
        "anatomy": {
            "tier1": "Bàn làm việc của chuyên gia địa kinh tế với các bản đồ động thái thương mại ngũ cốc châu Á qua các thời kỳ.",
            "tier2": "Đường cong chu kỳ kinh tế biểu diễn các đỉnh cao và khúc cua lịch sử của ngành gạo Việt Nam hiển thị sắc nét dưới ánh đèn bàn ấm áp.",
            "tier3": "Cú máy trượt ngang dọc theo đường cong chu kỳ địa kinh tế lúa gạo (Horizontal tracking shot along geo-economic cycle curve)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a high-level geo-economic analytical desk with dynamic multi-year commodity trade cycles, historical supply curves, and regional agricultural maps",
        "setting": "a prestigious strategic policy office illuminated by warm morning sunbeams and ambient reading lamps",
        "motion": "Slow horizontal tracking shot along the undulating geo-economic trade cycle chart"
    },
    {
        "id": "CH06_SC002",
        "dur": "5.51s",
        "words": 21,
        "text": "Đỉnh cao lịch sử năm 2024 từng mang lại cảm giác thăng hoa tột độ cho toàn bộ nền nông nghiệp.",
        "anatomy": {
            "tier1": "Cầu cảng container Cát Lái hoặc Cái Mép rộn rã tiếng còi tàu xuất khẩu dưới ánh nắng ban mai rực rỡ.",
            "tier2": "Các chuyên gia thương mại, doanh nghiệp và nông dân cùng nâng ly trong hội nghị tổng kết năm thắng lợi rực rỡ của hạt gạo Việt Nam.",
            "tier3": "Cú máy nâng chậm từ mặt boong tàu container lên bầu trời xanh rực rỡ nắng ấm (Slow upward tilt from container deck toward sunny morning sky)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a sun-drenched deep-water export port in southern Vietnam with towering container cranes loading grain ships against a glorious morning sky, celebrating the historic 2024 pinnacle",
        "setting": "a bustling maritime container terminal under bright golden morning daylight",
        "motion": "Slow upward tilt from ship cargo containers toward the triumphant morning sky"
    },
    {
        "id": "CH06_SC003",
        "dur": "6.3s",
        "words": 24,
        "text": "Khi đó, hơn chín triệu tấn gạo xuất khẩu đã mang về nguồn ngoại tệ kỷ lục hơn năm phẩy bảy tỷ đô la.",
        "anatomy": {
            "tier1": "Mặt tiền trụ sở Bộ Nông nghiệp và Phát triển Nông thôn với bảng thông báo thành tựu xuất khẩu quốc gia.",
            "tier2": "Biểu đồ cột mốc lịch sử hiển thị con số xuất khẩu trên 9 triệu tấn gạo đạt doanh thu kỷ lục trên 5.7 tỷ USD rực rỡ màu vàng hổ phách.",
            "tier3": "Cú máy tĩnh trực diện vào con số kỷ lục 9 triệu tấn và 5.7 tỷ USD (Steady shot on historic 9M tons and $5.7B landmark) cùng text overlay góc trái dưới."
        },
        "overlay": "ĐỈNH CAO 2024: > 9M TẤN (~5,7 TỶ USD)",
        "ref": None,
        "subj": "an impressive state agricultural exhibition board displaying the monumental national export achievement: over 9 million metric tons and 5.7 billion USD in foreign exchange revenue",
        "setting": "a grand government ministry foyer under warm ambient chandelier illumination",
        "motion": "Steady camera shot framing the historic agricultural milestone display"
    },
    {
        "id": "CH06_SC004",
        "dur": "4.72s",
        "words": 18,
        "text": "Giá gạo bình quân có thời điểm chạm mốc sáu trăm hai mươi bảy đô la một tấn.",
        "anatomy": {
            "tier1": "Bảng điện tử sàn giao dịch hàng hóa quốc tế tại TP.HCM với đồ thị giá gạo xuất khẩu Việt Nam.",
            "tier2": "Cột mốc giá bình quân chạm đỉnh 627 USD/tấn tỏa sáng rực rỡ, vượt qua mọi đối thủ cạnh tranh trong khu vực.",
            "tier3": "Cú máy tĩnh trực diện vào mức giá đỉnh 627 USD/tấn (Steady shot on peak export price of 627 USD/ton) cùng text overlay góc trái dưới."
        },
        "overlay": "GIÁ ĐỈNH: 627 USD/TẤN",
        "ref": None,
        "subj": "a financial trading terminal display showing the soaring export price index for Vietnamese 5% broken rice reaching a historic peak of 627 USD per metric ton",
        "setting": "a commodity trading room in warm amber and warm ivory interior light",
        "motion": "Steady camera shot framing the peak price commodity ticker"
    },
    {
        "id": "CH06_SC005",
        "dur": "5.25s",
        "words": 20,
        "text": "Việt Nam được quốc tế ca ngợi như một chiếc mỏ neo an ninh lương thực không thể thay thế.",
        "anatomy": {
            "tier1": "Hội trường hội nghị thượng đỉnh an ninh lương thực toàn cầu của FAO tại Rome với đại diện hàng trăm quốc gia.",
            "tier2": "Trưởng phái đoàn quốc tế vỗ tay chúc mừng bài phát biểu của đại diện Việt Nam, khẳng định vai trò mỏ neo an ninh lương thực toàn cầu.",
            "tier3": "Cú máy trượt ngang qua hội trường quốc tế đang vỗ tay ca ngợi Việt Nam (Horizontal tracking shot past international delegates applauding)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a prestigious plenary session of an international food security summit with multinational delegates applauding the Vietnamese delegation, symbolizing global food leadership",
        "setting": "a grand international conference hall under warm architectural lighting",
        "motion": "Slow horizontal tracking shot past respectful international diplomatic delegations"
    },
    {
        "id": "CH06_SC006",
        "dur": "6.3s",
        "words": 24,
        "text": "Thế nhưng, trong thế giới của thương mại hàng hóa phái sinh, mọi đỉnh cao đều tiềm ẩn những đợt sóng ngầm đảo chiều.",
        "anatomy": {
            "tier1": "Sàn giao dịch phái sinh hàng hóa với các đường nến giá bắt đầu xuất hiện những nhịp rung lắc kỹ thuật.",
            "tier2": "Hình ảnh ẩn dụ: Cơn sóng ngầm dưới làn nước biển hoàng hôn vàng cam, báo trước một chu kỳ điều chỉnh khốc liệt.",
            "tier3": "Cú máy đẩy chậm vào mô hình sóng ngầm phái sinh hàng hóa (Slow push-in on commodity derivative oscillation chart)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a stylized graphic depicting cyclical commodity price waves shifting beneath a serene surface, with fluctuating candlestick patterns warning of an impending market reversal",
        "setting": "a commodity market intelligence console in warm amber and cream tones",
        "motion": "Slow push-in shot toward the cyclical market reversal candlestick indicator"
    },
    {
        "id": "CH06_SC007",
        "dur": "3.67s",
        "words": 14,
        "text": "Và cơn địa chấn tiếp theo không đến từ thiên tai hay hạn mặn.",
        "anatomy": {
            "tier1": "Cánh đồng mẫu lớn ĐBSCL vẫn êm đềm xanh tốt, hệ thống cống đập ngăn mặn kiên cố giữ nước ngọt an toàn.",
            "tier2": "Sự bình yên trên đồng ruộng đối lập với cơn địa chấn chính sách đang hình thành từ cách xa hàng ngàn cây số.",
            "tier3": "Cú máy lùi chậm từ dòng kênh ngọt ra chân trời hoàng hôn tĩnh lặng (Slow pull-back shot from calm freshwater canal toward sunset)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a tranquil Mekong Delta rice paddy canal with water flowing calmly through concrete sluice gates, showing nature and irrigation in complete peaceful harmony",
        "setting": "peaceful countryside in southern Vietnam bathed in late afternoon golden light",
        "motion": "Slow pull-back shot from the serene canal reflecting the calm golden sky"
    },
    {
        "id": "CH06_SC008",
        "dur": "5.51s",
        "words": 21,
        "text": "Nó đến từ quyết định mở kho xả hàng của người khổng lồ nông nghiệp lớn nhất hành tinh: Ấn Độ.",
        "anatomy": {
            "tier1": "Tòa nhà Dinh Thủ tướng tại New Delhi nhìn từ thảm cỏ xanh mướt dưới ánh chiều tà ấm áp.",
            "tier2": "Thủ tướng Ấn Độ Narendra Modi xuất hiện trong phòng hội nghị chính phủ, chuẩn bị đưa ra quyết định thay đổi cán cân cung cầu toàn cầu.",
            "tier3": "Cú máy đẩy chậm vào Thủ tướng Narendra Modi và bản đồ xuất khẩu nông sản Ấn Độ (Slow push-in on Prime Minister Narendra Modi and India export map)."
        },
        "overlay": None,
        "ref": "modi_india.jpg",
        "subj": "Indian Prime Minister Narendra Modi in official attire presiding over a high-level economic council meeting in New Delhi with national grain export maps displayed behind him",
        "setting": "the prestigious cabinet conference room in New Delhi under warm ambient lamplight",
        "motion": "Slow push-in shot toward Prime Minister Narendra Modi during the strategic meeting"
    },
    {
        "id": "CH06_SC009",
        "dur": "4.2s",
        "words": 16,
        "text": "Sau hơn một năm đóng chặt van xuất khẩu để kiềm chế lạm phát trong nước",
        "anatomy": {
            "tier1": "Cổng cảng xuất khẩu ngũ cốc Jawaharlal Nehru (Nhava Sheva) tại Ấn Độ từng đóng chặt then cài trong giai đoạn cấm xuất khẩu.",
            "tier2": "Tấm biển thông tri cấm xuất khẩu lúa gạo giai đoạn 2023 - 2024 để giữ giá lương thực nội địa cho người dân Ấn Độ.",
            "tier3": "Cú máy trượt ngang qua cổng cảng từng bị đóng chặt van xuất khẩu (Horizontal tracking shot past locked port security gates)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the quiet commercial perimeter of an Indian grain export terminal with padlocked gates and dormant loading gantries from the export restriction period under warm midday sun",
        "setting": "a major industrial port terminal in western India under warm dusty daylight",
        "motion": "Slow horizontal tracking shot past the historic closed export gates"
    },
    {
        "id": "CH06_SC010",
        "dur": "3.41s",
        "words": 13,
        "text": "bức tranh mùa màng tại Ấn Độ bước sang một bước ngoặt lớn.",
        "anatomy": {
            "tier1": "Bản đồ thời tiết khí hậu Nam Á với những dải mây gió mùa Tây Nam cuồn cuộn mang mưa lớn.",
            "tier2": "Những đám mây mưa màu vàng cam tưới tắm khắp các bang nông nghiệp trọng điểm Punjab, Haryana và Tây Bengal.",
            "tier3": "Cú máy trượt ngang qua bản đồ gió mùa Ấn Độ (Horizontal tracking shot across Indian monsoon weather map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a meteorological satellite map of the Indian subcontinent displaying vibrant Southwest monsoon moisture bands sweeping beneficially across agricultural heartlands",
        "setting": "an agro-meteorological forecasting center under warm ambient screen glow",
        "motion": "Smooth horizontal tracking shot following monsoon rain bands over northern India"
    },
    {
        "id": "CH06_SC011",
        "dur": "5.51s",
        "words": 21,
        "text": "Mùa mưa gió mùa năm 2024 đến sớm và tưới tắm cho các vùng đồng bằng trù phú ven sông Hằng.",
        "anatomy": {
            "tier1": "Đồng bằng sông Hằng bát ngát trĩu hạt lúa nước dưới cơn mưa gió mùa ấm áp.",
            "tier2": "Người nông dân Ấn Độ vui mừng đón những cơn mưa rào tưới đẫm hàng triệu héc ta lúa xanh tốt mơn mởn.",
            "tier3": "Cú máy bay chậm dọc theo bờ sông Hằng mùa vụ bội thu (Slow aerial glide along Ganges river basin fertile paddies)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an expansive view of the fertile Ganges river plains in Uttar Pradesh lush with healthy green paddy stalks refreshed by gentle monsoon rains under warm golden sunlight",
        "setting": "the vast agricultural river basin of northern India under warm humid morning skies",
        "motion": "Slow aerial glide across the lush monsoon-watered rice plains along the Ganges"
    },
    {
        "id": "CH06_SC012",
        "dur": "4.46s",
        "words": 17,
        "text": "Sản lượng thu hoạch lúa của đất nước này vọt lên mức kỷ lục chưa từng có",
        "anatomy": {
            "tier1": "Các cánh đồng Punjab ngập tràn sắc vàng lúa chín, hàng ngàn máy gặt liên hợp dồn dập thu hoạch vụ mùa bội thu.",
            "tier2": "Núi thóc vàng ươm chất cao tại các chợ nông sản Mandi, báo hiệu một vụ mùa lịch sử vượt xa mọi dự báo.",
            "tier3": "Cú máy nâng chậm từ bãi thóc khổng lồ lên bầu trời rực nắng ấm (Slow upward tilt from massive grain mounds to sunny sky)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a vast rural grain Mandi market in Punjab with colossal golden mounds of harvested paddy being heaped by modern tractors and cooperative workers under bright sunny skies",
        "setting": "a sprawling agricultural wholesale market in northern India under warm bright sun",
        "motion": "Slow upward tilt from towering golden paddy mounds toward the sunny sky"
    },
    {
        "id": "CH06_SC013",
        "dur": "2.62s",
        "words": 10,
        "text": "vượt qua mốc một trăm ba mươi tám triệu tấn.",
        "anatomy": {
            "tier1": "Báo cáo thống kê sản lượng thu hoạch nông nghiệp của Bộ Nông nghiệp Ấn Độ.",
            "tier2": "Con số kỷ lục lịch sử vượt mốc 138 triệu tấn gạo hiển thị rực rỡ trên bảng điện tử điều hành.",
            "tier3": "Cú máy tĩnh trực diện vào con số sản lượng vượt 138 triệu tấn (Steady shot on historic >138 million tons harvest milestone) cùng text overlay góc trái dưới."
        },
        "overlay": "SẢN LƯỢNG ẤN ĐỘ: > 138M TẤN",
        "ref": None,
        "subj": "an official agricultural bulletin from the Ministry of Agriculture of India highlighting the historic national production record of over 138 million metric tons of milled rice",
        "setting": "a national statistical bureau briefing room in warm ambient lighting",
        "motion": "Steady camera shot framing the historic 138 million tons production figure"
    },
    {
        "id": "CH06_SC014",
        "dur": "5.51s",
        "words": 21,
        "text": "Vấn đề của New Delhi lúc này không còn là thiếu lương thực, mà là thừa mứa ở mức báo động.",
        "anatomy": {
            "tier1": "Bàn hội nghị kinh tế tại New Delhi với các báo cáo tài chính cảnh báo khủng hoảng thừa lương thực.",
            "tier2": "Biểu đồ kho bãi báo động đỏ: Chi phí lưu kho và rủi ro hư hỏng gạo tăng vọt theo từng ngày.",
            "tier3": "Cú máy đẩy chậm vào biểu đồ cảnh báo khủng hoảng thừa lương thực (Slow push-in on surplus grain crisis ledger)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an economic crisis dashboard in New Delhi with urgent analytical reports highlighting severe grain oversupply, escalating storage subsidies, and overflowing state silos",
        "setting": "a government ministry economic planning office in warm amber tones",
        "motion": "Slow push-in shot toward the grain surplus crisis documentation"
    },
    {
        "id": "CH06_SC015",
        "dur": "6.04s",
        "words": 23,
        "text": "Hệ thống kho dự trữ công cộng của Tổng công ty Lương thực Ấn Độ rơi vào tình trạng quá tải nghiêm trọng.",
        "anatomy": {
            "tier1": "Khu liên hợp kho chứa ngũ cốc khổng lồ của Tổng công ty Lương thực Ấn Độ (FCI) tại Haryana hoặc Punjab.",
            "tier2": "Các dãy nhà kho bê tông đóng kín cửa đã chật cứng tới nóc, đoàn xe tải chở lúa mới vẫn ùn tắc kéo dài bên ngoài chờ nhập kho.",
            "tier3": "Cú máy bay chậm trên cao bao quát khu phức hợp kho FCI quá tải (Slow aerial glide over overflowing FCI grain depot)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a colossal grain storage complex of the Food Corporation of India (FCI) with endless rows of concrete silos and brick godowns overflowing, with long lines of grain trucks waiting outside",
        "setting": "a massive government logistics depot in northern India under warm hazy afternoon sun",
        "motion": "Slow aerial glide across the crowded FCI grain storage complex and truck queues"
    },
    {
        "id": "CH06_SC016",
        "dur": "6.56s",
        "words": 25,
        "text": "Lượng lúa gạo tồn kho chạm ngưỡng gần năm mươi triệu tấn, cao gấp bốn lần mức dự trữ an toàn quốc gia quy định.",
        "anatomy": {
            "tier1": "Bảng kiểm toán dự trữ lương thực quốc gia của Ấn Độ hiển thị con số tồn kho kỷ lục gần 50 triệu tấn.",
            "tier2": "Biểu đồ so sánh trực quan: Lượng gạo tồn kho thực tế chạm 50 triệu tấn, cao gấp 4 lần mức đệm an toàn tối thiểu theo luật định.",
            "tier3": "Cú máy tĩnh trực diện vào con số tồn kho 50 triệu tấn gấp 4 lần định mức (Steady shot on 50M tons reserve inventory - 4x safety threshold) cùng text overlay góc trái dưới."
        },
        "overlay": "KHO DỰ TRỮ FCI: ~50M TẤN (GẤP 4 LẦN)",
        "ref": None,
        "subj": "a state audit visualization chart showing the colossal Food Corporation of India rice reserve inventory reaching nearly 50 million metric tons, four times higher than statutory national buffer norms",
        "setting": "a national grain audit headquarters in warm neutral lighting",
        "motion": "Steady camera shot framing the 50 million ton reserve data graphic"
    },
    {
        "id": "CH06_SC017",
        "dur": "5.77s",
        "words": 22,
        "text": "Các nhà kho không còn chỗ chứa, hàng triệu tấn ngũ cốc vụ mới có nguy cơ mục nát dưới mưa nắng.",
        "anatomy": {
            "tier1": "Khu vực lưu trữ ngũ cốc ngoài trời (CAP storage) của Ấn Độ với hàng triệu bao thóc được phủ bạt nhựa tạm bợ.",
            "tier2": "Mưa nắng nhiệt đới đe dọa làm ẩm mốc và mục nát các đống thóc khổng lồ ngoài trời, tạo sức ép khủng khiếp lên ngân sách.",
            "tier3": "Cú máy trượt ngang qua những đống bao lúa phủ bạt ngoài trời (Horizontal tracking shot past tarpaulin-covered grain stacks)."
        },
        "overlay": None,
        "ref": None,
        "subj": "vast open-air grain storage depots (Cover and Plinth - CAP) in rural India with millions of burlap rice bags stacked on wooden plinths beneath black and blue tarpaulins under direct sunlight",
        "setting": "an open storage yard in central India under warm dusty afternoon light",
        "motion": "Slow horizontal tracking shot past the endless tarpaulin-covered grain stacks"
    },
    {
        "id": "CH06_SC018",
        "dur": "4.2s",
        "words": 16,
        "text": "Trước áp lực giải phóng kho bãi và cứu vãn chi phí lưu kho khổng lồ",
        "anatomy": {
            "tier1": "Phòng họp Bộ Tài chính và Bộ Lương thực Ấn Độ với các bảng tính chi phí trợ cấp lưu kho hàng tỷ rupee mỗi tháng.",
            "tier2": "Các quan chức kỹ trị New Delhi đồng thuận phương án khẩn cấp: Mở van xuất khẩu để giải phóng dòng tiền và kho bãi.",
            "tier3": "Cú máy đẩy chậm vào quyết định dỡ bỏ van xuất khẩu trên bàn họp (Slow push-in on export deregulation policy decree)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a high-level policy deliberation in New Delhi where finance and food ministry officials review urgent deregulation orders to release grain carrying costs",
        "setting": "a government ministry conference chamber in warm ambient lamplight",
        "motion": "Slow push-in shot toward the deregulation order draft on the conference table"
    },
    {
        "id": "CH06_SC019",
        "dur": "3.41s",
        "words": 13,
        "text": "New Delhi buộc phải kích hoạt chiếc van xả lũ ra thế giới.",
        "anatomy": {
            "tier1": "Bàn làm việc của Thủ tướng Ấn Độ Narendra Modi với sắc lệnh chính thức mở cửa xuất khẩu lương thực.",
            "tier2": "Hình ảnh ẩn dụ: Cánh cổng van đập nước khổng lồ bằng thép mở tung, phóng thích dòng chảy ngũ cốc ra đại dương.",
            "tier3": "Cú máy nâng nhanh theo cánh cổng mở van xả lũ lương thực (Dynamic upward tilt as grain floodgate swings open)."
        },
        "overlay": None,
        "ref": "modi_india.jpg",
        "subj": "an evocative visual of Indian government export authorization documents alongside the metaphorical opening of massive steel port floodgates releasing grain freighters into international waters",
        "setting": "a grand maritime port control tower overlooking warm ocean waters",
        "motion": "Dynamic upward tilt as port gates open toward the open sea"
    },
    {
        "id": "CH06_SC020",
        "dur": "4.99s",
        "words": 19,
        "text": "Từ cuối tháng 9 năm 2024, lộ trình mở cửa diễn ra dồn dập với tốc độ chóng mặt.",
        "anatomy": {
            "tier1": "Lịch trình công báo chính sách kinh tế Ấn Độ cuối tháng 9 năm 2024 với hàng loạt công điện khẩn.",
            "tier2": "Các hãng thông tấn quốc tế Reuters, Bloomberg liên tục phát tin nóng về việc Ấn Độ đảo chiều chính sách xuất khẩu gạo.",
            "tier3": "Cú máy trượt nhanh qua dòng tin tức Breaking News mở cửa xuất khẩu (Dynamic tracking pan across Breaking News headlines)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an international news monitoring room displaying urgent Breaking News flashes on Reuters and Bloomberg screens announcing India abrupt removal of rice export restrictions in late September 2024",
        "setting": "a newsroom terminal in warm amber glow and rapid headline tickers",
        "motion": "Fast horizontal tracking pan across the urgent global trade news tickers"
    },
    {
        "id": "CH06_SC021",
        "dur": "3.15s",
        "words": 12,
        "text": "Chính phủ Ấn Độ lần lượt bãi bỏ giá sàn xuất khẩu",
        "anatomy": {
            "tier1": "Công văn của Tổng cục Ngoại thương Ấn Độ (DGFT) thông báo bãi bỏ mức giá sàn xuất khẩu (MEP - Minimum Export Price).",
            "tier2": "Dấu mộc bãi bỏ rào cản giá sàn được đóng lên văn bản, cho phép doanh nghiệp tự do chào giá cạnh tranh trên thị trường.",
            "tier3": "Cú máy cận cảnh dấu mộc bãi bỏ giá sàn xuất khẩu (Close-up shot on abolition of Minimum Export Price decree)."
        },
        "overlay": None,
        "ref": "modi_india.jpg",
        "subj": "an official decree from the Directorate General of Foreign Trade of India officially removing the Minimum Export Price (MEP) floor, signed under the administration in New Delhi",
        "setting": "a formal government trade desk under warm desk lamplight",
        "motion": "Close-up push-in shot on the official document removing minimum export price floors"
    },
    {
        "id": "CH06_SC022",
        "dur": "5.25s",
        "words": 20,
        "text": "hạ thuế gạo đồ về mức không phần trăm và dỡ bỏ toàn bộ lệnh cấm xuất khẩu gạo trắng.",
        "anatomy": {
            "tier1": "Bảng thuế quan hải quan Ấn Độ với mức thuế xuất khẩu gạo đồ (parboiled rice) hạ thẳng về 0%.",
            "tier2": "Lệnh cấm xuất khẩu gạo trắng non-basmati chính thức được gỡ bỏ hoàn toàn sau hơn một năm đóng băng.",
            "tier3": "Cú máy tĩnh trực diện vào thông báo dỡ bỏ lệnh cấm và thuế 0% (Steady shot on zero tariff and export ban repeal announcement) cùng text overlay góc trái dưới."
        },
        "overlay": "ẤN ĐỘ DỠ BỎ CẤM XUẤT KHẨU",
        "ref": None,
        "subj": "a customs tariff schedule display showing the export duty on parboiled rice slashed to zero percent alongside the complete revocation of the non-basmati white rice export embargo",
        "setting": "an Indian customs authority administrative hall in warm ambient lighting",
        "motion": "Steady camera shot framing the zero export duty and ban repeal notice"
    },
    {
        "id": "CH06_SC023",
        "dur": "3.41s",
        "words": 13,
        "text": "Hàng chục triệu tấn gạo giá rẻ từ các kho dự trữ khổng",
        "anatomy": {
            "tier1": "Khu cảng biển Kakinada và Kandla tại Ấn Độ với hàng trăm đoàn xe tải chở gạo nối đuôi nhau vào cầu cảng.",
            "tier2": "Hàng vạn bao gạo trắng giá rẻ được bốc xếp hối hả lên các con tàu viễn dương để chuẩn bị rời bến.",
            "tier3": "Cú máy trượt ngang qua đoàn xe tải chở gạo vào cảng biển (Horizontal tracking shot past grain trucks entering seaport)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the commercial quayside of Kakinada Port in India with endless convoys of trucks transferring millions of tons of stored white rice into the holds of awaiting international bulk cargo ships",
        "setting": "a sprawling Indian commercial port under warm sunny skies",
        "motion": "Slow horizontal tracking shot past the bustling truck convoys and dockside loading"
    },
    {
        "id": "CH06_SC024",
        "dur": "3.67s",
        "words": 14,
        "text": "lồ của Ấn Độ lập tức tràn ngập các tuyến hàng hải quốc tế.",
        "anatomy": {
            "tier1": "Bản đồ hàng hải quốc tế với các hải trình từ Ấn Độ tỏa đi khắp châu Phi, Trung Đông và Đông Nam Á.",
            "tier2": "Những con tàu hàng rời chở đầy gạo giá rẻ của Ấn Độ đồng loạt rẽ sóng trên Ấn Độ Dương.",
            "tier3": "Cú máy góc rộng quay tàu hàng Ấn Độ vượt sóng ra khơi (Wide cinematic shot of Indian grain freighter cutting through ocean swells)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a panoramic view of a massive ocean freighter loaded with Indian grain cutting through open waters in the Indian Ocean under warm golden sunlight",
        "setting": "the vast open waters of the Indian Ocean during golden hour",
        "motion": "Wide cinematic tracking shot following the bulk freighter slicing through warm ocean swells"
    },
    {
        "id": "CH06_SC025",
        "dur": "4.2s",
        "words": 16,
        "text": "Một cơn bão cung ứng hình thành, đè nặng lên mặt bằng giá cả toàn cầu.",
        "anatomy": {
            "tier1": "Biểu đồ đường cong cung cầu thế giới với mũi tên cung ứng (Supply Surge) lao dốc đè nặng lên trục giá cả.",
            "tier2": "Làn sóng hàng chục triệu tấn gạo giá rẻ dội thẳng vào thị trường, làm sụp đổ kỳ vọng giá cao của các nhà buôn quốc tế.",
            "tier3": "Cú máy đẩy chậm vào đường cong áp lực giá toàn cầu (Slow push-in on global commodity price pressure curve)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a global commodity analytics graphic showing a massive supply shockwave symbol exerting heavy downward downward pressure onto international grain price indices",
        "setting": "a global trade monitoring console in warm amber tones",
        "motion": "Slow push-in shot framing the heavy downward price pressure vector"
    },
    {
        "id": "CH06_SC026",
        "dur": "6.3s",
        "words": 24,
        "text": "Chỉ số giá gạo thế giới do FAO công bố lập tức rơi tự do tới hai mươi chín phần trăm trong năm 2025.",
        "anatomy": {
            "tier1": "Báo cáo Chỉ số Giá Lương thực (Food Price Index) của Tổ chức Lương thực và Nông nghiệp Liên Hợp Quốc (FAO).",
            "tier2": "Đồ thị chỉ số giá gạo toàn cầu cắm đầu rơi tự do tới 29% trong năm 2025, phản ánh sự biến động địa chấn của thị trường.",
            "tier3": "Cú máy tĩnh trực diện vào con số giá gạo thế giới rơi tự do 29% (Steady shot on FAO Rice Price Index 29% plunge) cùng text overlay góc trái dưới."
        },
        "overlay": "CHỈ SỐ GIÁ FAO: GIẢM 29% (2025)",
        "ref": None,
        "subj": "the official Food and Agriculture Organization (FAO) Rice Price Index report displaying a steep red decline curve plunging 29 percent year-over-year in 2025",
        "setting": "a United Nations agency statistical briefing room under warm neutral lighting",
        "motion": "Steady camera shot framing the dramatic 29 percent price decline index"
    },
    {
        "id": "CH06_SC027",
        "dur": "2.1s",
        "words": 8,
        "text": "Từ mức đỉnh hơn sáu trăm đô la",
        "anatomy": {
            "tier1": "Bảng điện tử giá gạo kỳ hạn quốc tế với cột mốc đỉnh cũ 650 USD/tấn trong quá khứ.",
            "tier2": "Vạch kẻ màu vàng hổ phách ghi nhớ đỉnh giá lịch sử đã từng thống trị thị trường suốt hơn một năm.",
            "tier3": "Cú máy tĩnh trực diện vào đỉnh giá cũ trên 600 USD (Steady shot on past peak price >600 USD)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a commodity trading screen displaying the historic golden peak line above 600 USD per metric ton before the market descent",
        "setting": "a financial trading terminal in warm amber lighting",
        "motion": "Steady camera shot focusing on the former 600 USD peak price level"
    },
    {
        "id": "CH06_SC028",
        "dur": "5.25s",
        "words": 20,
        "text": "giá gạo trắng tiêu chuẩn trên thị trường quốc tế lao dốc xuống dưới năm trăm đô la một tấn.",
        "anatomy": {
            "tier1": "Đồ thị giá gạo trắng 5% tấm thế giới trượt dốc xuống dưới ngưỡng 500 USD/tấn.",
            "tier2": "Mức giá 470 - 490 USD/tấn xuất hiện liên tiếp trên các hợp đồng mua bán ngũ cốc quốc tế mới.",
            "tier3": "Cú máy tĩnh trực diện vào mức giá gạo thế giới lao dốc dưới 500 USD/tấn (Steady shot on sub-500 USD/ton global price level) cùng text overlay góc trái dưới."
        },
        "overlay": "GIÁ GẠO THẾ GIỚI: < 500 USD/TẤN",
        "ref": None,
        "subj": "a real-time international commodity trading monitor showing standard 5% broken white rice benchmark plunging below 500 USD per metric ton amid continuous sell orders",
        "setting": "an international trade exchange floor under warm ambient desk light",
        "motion": "Steady camera shot framing the commodity price descent below 500 USD"
    },
    {
        "id": "CH06_SC029",
        "dur": "3.67s",
        "words": 14,
        "text": "Nhiều thị trường nhập khẩu lớn bắt đầu có những động thái phòng thủ.",
        "anatomy": {
            "tier1": "Phòng họp các bộ thương mại và nông nghiệp của các quốc gia Đông Nam Á (Philippines, Indonesia).",
            "tier2": "Các nhà hoạch định chính sách thảo luận giải pháp bảo vệ thị trường lúa gạo nội địa trước làn sóng bán phá giá.",
            "tier3": "Cú máy trượt ngang qua bàn họp chính sách phòng vệ thương mại (Horizontal tracking shot past import defense policy meeting)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a government trade committee meeting in Southeast Asia where officials review trade defense measures, tariff adjustments, and import quota moratoriums",
        "setting": "a formal government boardroom under warm natural window light",
        "motion": "Slow horizontal tracking shot past trade policy committee members"
    },
    {
        "id": "CH06_SC030",
        "dur": "4.99s",
        "words": 19,
        "text": "Điển hình như Philippines, để bảo vệ người trồng lúa trong nước trước làn sóng gạo ngoại giá rẻ",
        "anatomy": {
            "tier1": "Cánh đồng lúa tại vùng Luzon (Philippines) nơi người nông dân đang thu hoạch vụ mùa trong sự lo âu về giá.",
            "tier2": "Biển thông báo chính sách của Bộ Nông nghiệp Philippines bảo vệ giá thu mua lúa tươi (palay) cho người dân bản địa.",
            "tier3": "Cú máy trượt ngang qua cánh đồng nông dân Philippines (Horizontal tracking shot past Filipino farmer harvesting palay)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a rural rice farm in Central Luzon where Filipino farmers harvest local palay crops beside a government notice board advocating domestic farmer protection against cheap grain inflows",
        "setting": "a sunlit provincial farmland in the Philippines under warm tropical morning skies",
        "motion": "Slow horizontal tracking shot past local farmers gathering palay bundles"
    },
    {
        "id": "CH06_SC031",
        "dur": "6.82s",
        "words": 26,
        "text": "họ đã tạm ngừng nhập khẩu trong bốn tháng. Ngay lập tức, áp lực dội thẳng vào ngành xuất khẩu gạo Việt Nam trong năm 2025.",
        "anatomy": {
            "tier1": "Văn bản quyết định tạm hoãn cấp phép nhập khẩu gạo trong 4 tháng của Cơ quan Quản lý Philippines đặt trên bàn giao dịch.",
            "tier2": "Bàn làm việc của giám đốc doanh nghiệp xuất khẩu gạo tại TP.HCM đối mặt với áp lực hủy hoặc hoãn giao các hợp đồng thương mại.",
            "tier3": "Cú máy đẩy chậm vào bàn làm việc căng thẳng của doanh nghiệp xuất khẩu (Slow push-in on executive desk under trade pressure)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an executive trade office in Ho Chi Minh City with commercial manifests showing delayed shipments to Manila beside an official Philippine four-month import moratorium advisory",
        "setting": "a corporate export executive office illuminated by warm morning desk lamps",
        "motion": "Slow push-in shot toward the commercial shipping documents affected by import delays"
    },
    {
        "id": "CH06_SC032",
        "dur": "5.77s",
        "words": 22,
        "text": "Sau một năm lập đỉnh, kim ngạch xuất khẩu của chúng ta giảm xuống còn khoảng bốn phẩy một tỷ đô la.",
        "anatomy": {
            "tier1": "Báo cáo thường niên của Tổng cục Hải quan Việt Nam tổng kết kim ngạch xuất nhập khẩu năm 2025.",
            "tier2": "Biểu đồ cột kim ngạch xuất khẩu lúa gạo năm 2025 dừng lại ở mức khoảng 4.1 tỷ USD sau năm đỉnh cao.",
            "tier3": "Cú máy tĩnh trực diện vào con số kim ngạch xuất khẩu ~4.1 tỷ USD năm 2025 (Steady shot on 2025 export turnover ~4.1 billion USD) cùng text overlay góc trái dưới."
        },
        "overlay": "VIỆT NAM 2025: ~4,1 TỶ USD",
        "ref": None,
        "subj": "an analytical annual trade performance chart showing Vietnam rice export value settling at approximately 4.1 billion USD in 2025 following the previous peak year",
        "setting": "a national customs economic briefing hall in warm neutral ambient tones",
        "motion": "Steady camera shot framing the 2025 export revenue metric"
    },
    {
        "id": "CH06_SC033",
        "dur": "4.46s",
        "words": 17,
        "text": "Sản lượng xuất khẩu giảm hơn mười phần trăm, dừng lại ở mức hơn tám triệu tấn.",
        "anatomy": {
            "tier1": "Khu cảng sông Cái Bè hoặc Thốt Nốt với các sà lan vận chuyển gạo xuất khẩu được sắp xếp nhịp nhàng.",
            "tier2": "Sản lượng xuất khẩu thực tế của Việt Nam vẫn duy trì ở mức cao ấn tượng trên 8 triệu tấn, dù giảm nhẹ hơn 10% so với năm kỷ lục.",
            "tier3": "Cú máy nâng chậm từ bến sà lan lên bảng điện tử cảng xuất khẩu (Slow upward tilt from barge berth to port output board)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a southern river export terminal where steel barges and dock cranes maintain steady loading operations, achieving over 8 million metric tons of annual export volume",
        "setting": "a river shipping port along the Tien River under warm golden afternoon light",
        "motion": "Slow upward tilt from loaded river barges toward the bustling quayside cranes"
    },
    {
        "id": "CH06_SC034",
        "dur": "3.67s",
        "words": 14,
        "text": "Giá xuất khẩu bình quân của gạo Việt Nam tụt từ sáu trăm hai",
        "anatomy": {
            "tier1": "Bảng đối chiếu giá xuất khẩu hàng tháng của Hiệp hội Lương thực Việt Nam (VFA).",
            "tier2": "Mốc giá cũ 627 USD/tấn được đánh dấu làm mốc xuất phát cho chu kỳ điều chỉnh theo xu hướng toàn cầu.",
            "tier3": "Cú máy trượt ngang qua bảng đối chiếu giá xuất khẩu (Horizontal tracking shot past export price timeline)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a chronological commodity pricing timeline chart showing the previous peak benchmark of 627 USD per metric ton transitioning downward across successive monthly contracts",
        "setting": "an agricultural trade intelligence desk in warm amber lighting",
        "motion": "Slow horizontal tracking shot following the monthly pricing timeline"
    },
    {
        "id": "CH06_SC035",
        "dur": "3.67s",
        "words": 14,
        "text": "mươi bảy đô la xuống còn năm trăm lẻ chín đô la một tấn.",
        "anatomy": {
            "tier1": "Hợp đồng xuất khẩu gạo giao dịch thực tế năm 2025 với mức giá bình quân 509 USD/tấn.",
            "tier2": "Con số 509 USD/tấn dù thấp hơn đỉnh cũ nhưng vẫn cao hơn đáng kể so với mức giá gạo thường của các đối thủ quốc tế.",
            "tier3": "Cú máy tĩnh trực diện vào mức giá bình quân 509 USD/tấn năm 2025 (Steady shot on average export price of 509 USD/ton) cùng text overlay góc trái dưới."
        },
        "overlay": "GIÁ BÌNH QUÂN: 509 USD/TẤN",
        "ref": None,
        "subj": "an export contract price index confirming Vietnam stabilized average rice export price at 509 USD per metric ton, maintaining a premium above international commodity baselines",
        "setting": "an agricultural export negotiation office in warm ambient light",
        "motion": "Steady camera shot framing the 509 USD/ton average price contract metric"
    },
    {
        "id": "CH06_SC036",
        "dur": "6.04s",
        "words": 23,
        "text": "Nhiều người bắt đầu lo lắng: Liệu ngành gạo Việt Nam có bị cuốn vào một vòng xoáy giảm giá không lối thoát?",
        "anatomy": {
            "tier1": "Quán cà phê thương lái nông sản ven sông Tiền với những ánh mắt âu lo nhìn vào biểu đồ giá lúa trên điện thoại.",
            "tier2": "Dấu hỏi lớn về tương lai ngành lúa gạo khi phải cạnh tranh với làn sóng gạo giá rẻ từ Ấn Độ.",
            "tier3": "Cú máy đẩy chậm vào khuôn mặt suy tư của thương lái và doanh nhân nông nghiệp (Slow push-in on thoughtful agricultural trader)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a contemplative agricultural trader sitting by a riverside cafe in the Mekong Delta reviewing global commodity tickers on a digital tablet with a thoughtful expression",
        "setting": "a rustic riverside veranda overlooking a tranquil southern canal at sunset",
        "motion": "Slow push-in shot toward the reflective trader and the digital commodity display"
    },
    {
        "id": "CH06_SC037",
        "dur": "4.2s",
        "words": 16,
        "text": "Thế nhưng, nếu nhìn sâu vào bức tranh thực tế, câu chuyện lại hoàn toàn khác.",
        "anatomy": {
            "tier1": "Phòng nghiên cứu chiến lược kinh tế nông nghiệp với kính lúp soi chiếu từng phân khúc thị trường lúa gạo.",
            "tier2": "Sự phân tầng rõ rệt: Gạo giá rẻ Ấn Độ đánh chiếm phân khúc phổ thông châu Phi; Trong khi gạo thơm Việt Nam làm chủ phân khúc ẩm thực cao cấp châu Á.",
            "tier3": "Cú máy nâng chậm từ kính lúp lên bản đồ phân tầng thị trường (Slow upward tilt from magnifying glass to segmented market map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an analytical market segmentation diagram showing clear bifurcation: cheap Indian grain commanding low-end African markets while Vietnamese fragrant rice dominates premium Asian dining tables",
        "setting": "a strategic market research laboratory in warm amber tones",
        "motion": "Slow upward tilt revealing the segmented global consumer demand landscape"
    },
    {
        "id": "CH06_SC038",
        "dur": "6.56s",
        "words": 25,
        "text": "Việt Nam giảm về kim ngạch do mặt bằng giá chung của thế giới đi xuống, nhưng chúng ta không hề mất đi thị trường.",
        "anatomy": {
            "tier1": "Bản đồ thị phần xuất khẩu gạo tại các thị trường truyền thống: Philippines, Indonesia, Malaysia, Trung Quốc vẫn phủ kín cờ Việt Nam.",
            "tier2": "Các đơn đặt hàng gạo thơm dài hạn từ các đối tác quốc tế vẫn đều đặn cập bến các doanh nghiệp Việt Nam.",
            "tier3": "Cú máy trượt ngang qua bản đồ thị phần vững vàng của gạo Việt Nam (Horizontal tracking shot across stable market share map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an international trade market share breakdown confirming that while total value dipped with global indices, Vietnam retained its foundational import quotas across ASEAN and East Asia",
        "setting": "an international marketing strategy room under warm natural lighting",
        "motion": "Smooth horizontal tracking shot past steady Asian market share indicators"
    },
    {
        "id": "CH06_SC039",
        "dur": "6.04s",
        "words": 23,
        "text": "Chúng ta vẫn bán được hơn tám triệu tấn gạo và giữ vững vị thế của một cường quốc xuất khẩu hàng đầu.",
        "anatomy": {
            "tier1": "Cầu cảng xuất khẩu gạo Thốt Nốt nhộn nhịp tàu hàng cập bến nhận gạo đóng bao xuất khẩu dưới ánh ban mai.",
            "tier2": "Hàng trăm công nhân và cần cẩu bốc xếp liên tục, sản lượng hơn 8 triệu tấn khẳng định bản lĩnh kiên cường của nền nông nghiệp.",
            "tier3": "Cú máy góc rộng quay toàn cảnh cảng xuất khẩu gạo nhộn nhịp (Wide cinematic shot of bustling river export port)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a grand wide-angle cinematic view of a bustling grain export terminal in Thot Not Can Tho with multiple merchant vessels being loaded under bright warm morning daylight",
        "setting": "the thriving industrial riverfront of Can Tho in radiant morning sun",
        "motion": "Wide cinematic tracking shot showcasing the vibrant rhythm of grain export loading"
    },
    {
        "id": "CH06_SC040",
        "dur": "3.41s",
        "words": 13,
        "text": "Điều kỳ diệu ấy bắt nguồn từ một cuộc đào thoát ngoạn mục",
        "anatomy": {
            "tier1": "Cánh đồng lúa ĐBSCL rực rỡ sắc vàng nắng ấm, từng luống lúa thơm dập dờn như sóng biển.",
            "tier2": "Người nông dân vung tay rải giống lúa thơm mới, biểu trưng cho sự chủ động thoát hiểm khỏi bẫy cạnh tranh giá rẻ.",
            "tier3": "Cú máy hạ thấp lướt trên ngọn lúa thơm đang trổ bông (Low-angle tracking shot over fragrant rice panicles)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dynamic low-angle tracking shot over golden fragrant rice stalks swaying gently in the warm delta breeze, symbolizing the visionary escape from generic commodity traps",
        "setting": "a pristine agricultural field in southern Vietnam under glorious warm sunshine",
        "motion": "Low-angle smooth tracking shot skimming over healthy fragrant rice panicles"
    },
    {
        "id": "CH06_SC041",
        "dur": "3.67s",
        "words": 14,
        "text": "khỏi chiếc bẫy gạo giá rẻ đã được chuẩn bị từ nhiều năm trước.",
        "anatomy": {
            "tier1": "Khuôn viên Viện Lúa ĐBSCL với các nhà khoa học đang chọn lọc các thế hệ giống lúa thuần chất lượng cao.",
            "tier2": "Chiếc bẫy gạo giá rẻ (The Low-Price Commodity Trap) đã bị phá vỡ nhờ chiến lược chủ động chuyển đổi cơ cấu giống từ một thập kỷ trước.",
            "tier3": "Cú máy trượt ngang qua phòng thí nghiệm chọn tạo giống lúa (Horizontal tracking shot past rice breeding laboratory)."
        },
        "overlay": None,
        "ref": None,
        "subj": "agricultural geneticists at the Cuu Long Delta Rice Research Institute meticulously cataloging new fragrant breeding lines in sunlit glasshouses, showing long-term strategic foresight",
        "setting": "an agronomic research institute greenhouse in warm natural morning light",
        "motion": "Slow horizontal tracking shot past scientists inspecting robust fragrant rice strains"
    },
    {
        "id": "CH06_SC042",
        "dur": "5.77s",
        "words": 22,
        "text": "Hãy hình dung điều gì sẽ xảy ra nếu Việt Nam vẫn giữ cơ cấu giống lúa của mười lăm năm trước.",
        "anatomy": {
            "tier1": "Bức ảnh tư liệu lịch sử 15 năm trước: Cánh đồng ĐBSCL thời kỳ độc canh giống lúa IR50404 hạt bạc bụng.",
            "tier2": "Người nông dân thời bấy giờ vất vả gánh từng bao thóc giá rẻ, bấp bênh phụ thuộc hoàn toàn vào thương lái mua xô.",
            "tier3": "Cú máy đẩy chậm vào bức tranh tư liệu nông thôn 15 năm trước (Slow push-in on historical farming photograph from 15 years ago)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a framed vintage photograph of Mekong Delta farming 15 years ago showing manual harvesting of old chalky-bellied IR50404 grain under harsh sun, illustrating past vulnerability",
        "setting": "an agricultural museum gallery under warm focused gallery spotlighting",
        "motion": "Slow push-in shot toward the historical photograph of early low-grade rice farming"
    },
    {
        "id": "CH06_SC043",
        "dur": "5.51s",
        "words": 21,
        "text": "Ngày đó, các cánh đồng miền Tây chủ yếu trồng giống lúa phẩm cấp thấp, hạt khô xốp và bạc bụng.",
        "anatomy": {
            "tier1": "Khay mẫu hạt lúa giống cũ IR50404 với đặc điểm hạt tròn ngắn, bụng hạt đục trắng (bạc bụng) và tỷ lệ gãy cao khi xay xát.",
            "tier2": "Bát cơm nấu từ giống lúa cũ hạt khô ráo, xốp và thiếu hương thơm tự nhiên, chỉ phù hợp cho phân khúc tiêu thụ thấp.",
            "tier3": "Cú máy cận cảnh khay hạt lúa bạc bụng cũ (Close-up shot of old chalky-bellied rice grain sample)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a detailed macro still life of old chalky-bellied generic white rice grains in an antique wooden bowl, showing dry brittle texture and high chalkiness",
        "setting": "an agronomic archive table under soft warm ambient lighting",
        "motion": "Macro close-up slow pan across the chalky-bellied generic rice grains"
    },
    {
        "id": "CH06_SC044",
        "dur": "1.57s",
        "words": 6,
        "text": "Nếu vẫn giữ mô hình cũ",
        "anatomy": {
            "tier1": "Bản mô phỏng kịch bản kinh tế giả định (Simulation Scenario) trên màn hình máy tính.",
            "tier2": "Kịch bản nếu giữ mô hình cũ: Đường doanh thu và xuất khẩu của Việt Nam rơi tự do không có điểm tựa.",
            "tier3": "Cú máy đẩy nhanh vào kịch bản mô phỏng khủng hoảng giả định (Dynamic push-in on crisis simulation chart)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a hypothetical economic modeling screen running a simulation graph showing steep financial collapse if past low-value varieties had been maintained",
        "setting": "an economic computing lab in warm ambient monitor light",
        "motion": "Dynamic push-in shot toward the simulation scenario screen"
    },
    {
        "id": "CH06_SC045",
        "dur": "6.56s",
        "words": 25,
        "text": "hạt gạo của chúng ta chắc chắn sẽ mất hoàn toàn sức cạnh tranh trước những đợt gạo xả kho giá rẻ của Ấn Độ.",
        "anatomy": {
            "tier1": "Hình ảnh tương phản trên thị trường: Bao gạo trắng Ấn Độ giá siêu rẻ lấn át hoàn toàn các bao gạo phẩm cấp thấp của các nước khác.",
            "tier2": "Nếu chỉ bán gạo thường, Việt Nam sẽ bị đánh bạt khỏi thị trường vì không thể đọ nổi mức giá xả kho trợ giá của New Delhi.",
            "tier3": "Cú máy trượt ngang qua cảnh tượng cạnh tranh khốc liệt phân khúc giá rẻ (Horizontal tracking shot past low-cost price war scene)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a conceptual marketplace diptych showing low-cost Indian grain sacks heavily undercutting generic commodity competitors on international trading floors",
        "setting": "an international trade exchange floor under warm dramatic lighting",
        "motion": "Slow horizontal tracking shot illustrating the harsh price undercutting dynamic"
    },
    {
        "id": "CH06_SC046",
        "dur": "6.82s",
        "words": 26,
        "text": "Bởi vì Ấn Độ sở hữu hơn bốn mươi bốn triệu héc ta đất lúa, gấp mười một lần toàn bộ diện tích của Việt Nam.",
        "anatomy": {
            "tier1": "Bản đồ so sánh quy mô diện tích đất lúa: Toàn bộ diện tích đất trồng lúa của Ấn Độ (hơn 44 triệu ha) đặt cạnh diện tích lúa Việt Nam (khoảng 3.9 triệu ha gieo trồng).",
            "tier2": "Quy mô khổng lồ gấp 11 lần của Ấn Độ thể hiện ưu thế áp đảo tuyệt đối về diện tích đất đai và tài nguyên canh tác.",
            "tier3": "Cú máy tĩnh trực diện vào con số diện tích đất lúa Ấn Độ >44 triệu ha gấp 11 lần Việt Nam (Steady shot on India >44M ha rice acreage - 11x Vietnam) cùng text overlay góc trái dưới."
        },
        "overlay": "ĐẤT LÚA ẤN ĐỘ: > 44M HA (GẤP 11 LẦN)",
        "ref": None,
        "subj": "a comparative geospatial infographic displaying India colossal 44 million hectares of dedicated rice land dwarfing Vietnam cultivated acreage by a staggering factor of 11 to 1",
        "setting": "a geographic information system (GIS) analysis room under warm amber console lighting",
        "motion": "Steady camera shot framing the 11-to-1 land scale disparity infographic"
    },
    {
        "id": "CH06_SC047",
        "dur": "4.2s",
        "words": 16,
        "text": "Chạy đua về số lượng và bán phá giá với một quốc gia có quy mô",
        "anatomy": {
            "tier1": "Đồ thị lý thuyết trò chơi kinh tế học (Game Theory) mô phỏng cuộc đua xuống đáy về giá cả (Race to the Bottom).",
            "tier2": "Hai đường giá giảm dần triệt tiêu lợi nhuận của người sản xuất, cảnh báo sự tự sát kinh tế nếu chọn đối đầu số lượng.",
            "tier3": "Cú máy trượt dọc theo đường đua xuống đáy về giá bán (Tracking shot along race-to-the-bottom pricing vector)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an economic game theory chart illustrating the destructive 'race to the bottom' where commodity volume competition against an infinite landmass leads to zero profit margins",
        "setting": "an economics lecture hall under warm morning sunlight",
        "motion": "Slow tracking shot along the downward price spiral vector"
    },
    {
        "id": "CH06_SC048",
        "dur": "4.2s",
        "words": 16,
        "text": "đất đai vô tận như vậy là một bài toán kinh tế nắm chắc phần thua.",
        "anatomy": {
            "tier1": "Bàn cờ chiến lược với một quân tốt nhỏ bé đứng trước bàn cờ mênh mông vô tận của đối thủ khổng lồ.",
            "tier2": "Nhà chiến lược khẽ mỉm cười gạt bàn cờ số lượng, mở ra một chiến lược ngách chất lượng cao hoàn toàn mới.",
            "tier3": "Cú máy nâng chậm từ bàn cờ số lượng sang giải pháp chiến lược ngách (Slow upward tilt from volume board toward niche quality solution)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a symbolic visual of an elegant chess piece gracefully pivoting away from a crowded unwinnable volume confrontation toward an open high-ground square",
        "setting": "a quiet executive study under warm library lamp illumination",
        "motion": "Slow upward tilt following the strategic pivot toward high-ground positioning"
    },
    {
        "id": "CH06_SC049",
        "dur": "4.72s",
        "words": 18,
        "text": "Thế nhưng, người nông dân và các nhà khoa học Việt Nam đã chọn một con đường khác.",
        "anatomy": {
            "tier1": "Cánh đồng lúa Sóc Trăng rực rỡ ánh bình minh, người nông dân và nhà khoa học cùng đứng bên nhau bên ruộng lúa ST25 trĩu hạt.",
            "tier2": "Bàn tay chai sần của nông dân và bàn tay nhà khoa học cùng nâng niu bông lúa thơm dẻo, minh chứng cho sự đồng lòng đổi mới.",
            "tier3": "Cú máy nâng chậm từ bông lúa thơm lên ánh mắt kiên định của người nông dân và nhà khoa học (Slow tilt-up from fragrant paddy to determined faces)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a Vietnamese agronomist in field coat standing shoulder-to-shoulder with an experienced local farmer in conical hat in a sunlit fragrant rice field in Soc Trang, smiling with quiet confidence",
        "setting": "a thriving Mekong Delta rice paddy under glorious morning sunrise",
        "motion": "Slow tilt-up from golden drooping panicles to the smiling, determined faces in the morning light"
    },
    {
        "id": "CH06_SC050",
        "dur": "6.82s",
        "words": 26,
        "text": "Hơn tám mươi phần trăm sản lượng xuất khẩu của chúng ta hiện nay là các dòng gạo thơm chất lượng cao và gạo đặc sản.",
        "anatomy": {
            "tier1": "Kho xuất khẩu gạo hiện đại với hàng ngàn bao gạo thương hiệu ST24, ST25, Đài Thơm 8, Nàng Hoa đóng gói bao bì cao cấp.",
            "tier2": "Biểu đồ cơ cấu xuất khẩu gạo Việt Nam khẳng định tỷ trọng áp đảo trên 80% thuộc về các dòng gạo thơm chất lượng cao.",
            "tier3": "Cú máy tĩnh trực diện vào cơ cấu >80% gạo thơm xuất khẩu chất lượng cao (Steady shot on >80% high-grade fragrant export share) cùng text overlay góc trái dưới."
        },
        "overlay": "> 80% XUẤT KHẨU: GẠO THƠM CAO CẤP",
        "ref": None,
        "subj": "a state-of-the-art export grain terminal stacked with neatly palletized branded cartons and sacks of ST25, Jasmine, and specialty fragrant rice beside an editorial chart showing over 80 percent premium export share",
        "setting": "a pristine export warehouse under warm ambient natural lighting",
        "motion": "Steady camera shot framing the premium packaged rice and the 80% export share metric"
    },
    {
        "id": "CH06_SC051",
        "dur": "2.62s",
        "words": 10,
        "text": "Người tiêu dùng tại các đô thị ở Manila, Jakarta",
        "anatomy": {
            "tier1": "Khu ẩm thực nhà hàng gia đình tại Manila hoặc Jakarta trong giờ cơm tối ấm cúng.",
            "tier2": "Những gia đình trung lưu đô thị thưởng thức bữa cơm dẻo thơm, ấm áp bên ánh đèn vàng dịu nhẹ.",
            "tier3": "Cú máy trượt ngang qua bàn ăn các gia đình đô thị tại Manila và Jakarta (Horizontal tracking shot past urban dining tables in Manila and Jakarta)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an upscale family restaurant in Manila or Jakarta where urban diners savor steaming bowls of fragrant white rice with local dishes under warm ambient dining lights",
        "setting": "a contemporary Southeast Asian dining hall in warm amber tones",
        "motion": "Slow horizontal tracking shot past happy families enjoying steaming rice bowls"
    },
    {
        "id": "CH06_SC052",
        "dur": "4.72s",
        "words": 18,
        "text": "Kuala Lumpur hay Trung Quốc đã quen với hạt cơm mềm, dẻo và thơm ngát của Việt Nam.",
        "anatomy": {
            "tier1": "Quầy gạo thương hiệu cao cấp tại siêu thị ở Kuala Lumpur hoặc Thượng Hải đông đúc người mua sắm.",
            "tier2": "Khách hàng quốc tế chọn mua các túi gạo thơm Việt Nam, quen thuộc với hương vị dẻo mềm không thể thay thế.",
            "tier3": "Cú máy đẩy chậm vào khách hàng chọn mua gạo thơm Việt Nam (Slow push-in on international shoppers choosing Vietnamese rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an international supermarket aisle in Kuala Lumpur or Shanghai where discerning Asian consumers choose premium bags of Vietnamese fragrant Jasmine and ST25 rice from display shelves",
        "setting": "a brightly lit modern gourmet supermarket under warm retail lighting",
        "motion": "Slow push-in toward shoppers inspecting premium Vietnamese rice packaging"
    },
    {
        "id": "CH06_SC053",
        "dur": "3.94s",
        "words": 15,
        "text": "Họ sẵn sàng trả giá cao hơn để duy trì trải nghiệm ẩm thực đó",
        "anatomy": {
            "tier1": "Hóa đơn thanh toán siêu thị cao cấp hiển thị giá mua gạo thơm Việt Nam cao hơn các loại gạo thường.",
            "tier2": "Người tiêu dùng vui vẻ quẹt thẻ thanh toán, chấp nhận mức giá cao để có được chất lượng bữa ăn gia đình hoàn hảo.",
            "tier3": "Cú máy cận cảnh thao tác thanh toán quẹt thẻ tại quầy thu ngân (Close-up shot of card payment for premium rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a customer at an upscale grocery checkout counter happily paying for premium Vietnamese packaged rice, demonstrating consumer price insensitivity for superior taste and texture",
        "setting": "a modern grocery checkout counter under warm ambient lighting",
        "motion": "Smooth push-in shot toward the checkout payment transaction for premium rice"
    },
    {
        "id": "CH06_SC054",
        "dur": "6.56s",
        "words": 25,
        "text": "chứ không quay lại ăn những loại gạo khô xốp giá rẻ. Thương hiệu và chất lượng đã trở thành một chiếc áo giáp bảo",
        "anatomy": {
            "tier1": "Bát cơm trắng tinh khôi từ hạt gạo thơm Việt Nam óng ả, mềm dẻo tỏa hương lá dứa tự nhiên.",
            "tier2": "Hình ảnh ẩn dụ: Chiếc áo giáp bảo hộ bằng ánh sáng vàng óng bao bọc lấy hạt gạo Việt Nam trước những đợt sóng gió thị trường.",
            "tier3": "Cú máy trượt chậm quanh bát cơm dẻo thơm bóng bẩy (Slow cinematic pan around steaming bowl of premium cooked rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a stunning cinematic close-up of a steaming ceramic bowl of cooked Vietnamese ST25 rice, each grain glistening, tender, and distinct, exuding natural pandan aroma under soft warm lighting",
        "setting": "a gourmet culinary presentation table in warm ivory cream and natural wood tones",
        "motion": "Slow cinematic orbital pan around the glistening steaming bowl of premium rice"
    },
    {
        "id": "CH06_SC055",
        "dur": "3.67s",
        "words": 14,
        "text": "vệ hạt gạo Việt Nam vượt qua cơn chấn động giá cả toàn cầu.",
        "anatomy": {
            "tier1": "Biểu đồ giá xuất khẩu gạo Việt Nam luôn duy trì khoảng cách cao hơn 50 - 100 USD/tấn so với gạo Ấn Độ và Pakistan.",
            "tier2": "Chiếc áo giáp thương hiệu và chất lượng giúp hạt gạo Việt Nam hiên ngang đứng vững trước cơn chấn động giá cả thế giới năm 2025.",
            "tier3": "Cú máy tĩnh trực diện vào chiếc áo giáp thương hiệu & chất lượng (Steady shot on Brand & Quality Armor resilience display) cùng text overlay góc trái dưới."
        },
        "overlay": "ÁO GIÁP THƯƠNG HIỆU & CHẤT LƯỢNG",
        "ref": None,
        "subj": "an analytical market resilience graphic demonstrating how the quality premium spread of 50 to 100 USD/ton shielded Vietnamese rice exports from collapsing during the 2025 global commodity shock",
        "setting": "a strategic commodity analytics room in warm amber hues",
        "motion": "Steady camera shot framing the Brand and Quality Armor resilience graph"
    },
    {
        "id": "CH06_SC056",
        "dur": "3.41s",
        "words": 13,
        "text": "Sóng gió của năm 2025 là một phép thử vô cùng đắt giá.",
        "anatomy": {
            "tier1": "Bàn làm việc của các nhà hoạch định chính sách nông nghiệp với báo cáo tổng kết bài học kinh nghiệm năm 2025.",
            "tier2": "Phép thử địa kinh tế khẳng định sức bền nội sinh và khả năng chống chịu phi thường của nền nông nghiệp Việt Nam.",
            "tier3": "Cú máy đẩy chậm vào báo cáo bài học kinh nghiệm năm 2025 (Slow push-in on 2025 policy review dossier)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a strategic policy review dossier titled '2025 Geopolitical Stress Test & Agricultural Resilience' on a polished conference desk in warm morning light",
        "setting": "a government think-tank library in warm ivory and walnut tones",
        "motion": "Slow push-in shot toward the strategic policy review dossier"
    },
    {
        "id": "CH06_SC057",
        "dur": "6.82s",
        "words": 26,
        "text": "Nó khẳng định rằng con đường phát triển nông nghiệp sinh thái, chất lượng cao và giảm phát thải là hướng đi đúng đắn duy nhất.",
        "anatomy": {
            "tier1": "Cánh đồng mẫu lớn ĐBSCL áp dụng quy trình canh tác sinh thái 1 triệu héc ta chất lượng cao, giảm phát thải khí nhà kính.",
            "tier2": "Nông dân và kỹ sư vận hành máy sạ hàng kết hợp vùi phân, cảm biến đo mực nước thông minh trên đồng ruộng xanh tươi rực nắng ấm.",
            "tier3": "Cú máy bay chậm trên cao bao quát cánh đồng sinh thái hiện đại (Slow aerial sweep over high-quality low-emission eco-farms)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an inspiring aerial sweep over an expansive 1-million-hectare high-quality low-emission rice project farm in the Mekong Delta with smart water sensors and alternate wetting-and-drying channels",
        "setting": "the lush sun-drenched plains of southern Vietnam under clear blue morning skies",
        "motion": "Slow panoramic aerial sweep over the sustainable low-carbon rice farmlands"
    },
    {
        "id": "CH06_SC058",
        "dur": "5.25s",
        "words": 20,
        "text": "Thế nhưng, thị trường quốc tế dù biến động đến đâu cũng chỉ là những cơn sóng trên mặt nước.",
        "anatomy": {
            "tier1": "Đại dương mênh mông với những đợt sóng bạc đầu tan biến trên bờ cát dưới ánh hoàng hôn vàng cam.",
            "tier2": "Hình ảnh ẩn dụ: Những biến động giá cả trên sàn giao dịch chỉ là hiện tượng bề mặt, còn nền tảng sống còn nằm ở nguồn nước và đất đai.",
            "tier3": "Cú máy nâng chậm từ mặt sóng biển lên bầu trời hoàng hôn ấm áp (Slow upward tilt from ocean surf toward warm evening sky)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a serene coastal shoreline at golden hour with gentle ocean ripples breaking peacefully on warm sand, symbolizing fleeting market fluctuations on the surface",
        "setting": "a southern coastal shoreline under a rich terracotta and amber evening sky",
        "motion": "Slow upward tilt from foaming gentle shoreline ripples toward the vast evening horizon"
    },
    {
        "id": "CH06_SC059",
        "dur": "6.3s",
        "words": 24,
        "text": "Thách thức sinh tử lớn nhất của vựa lúa miền Tây không nằm ở các sàn giao dịch hàng hóa New Delhi hay Chicago.",
        "anatomy": {
            "tier1": "Hình ảnh màn hình sàn giao dịch hàng hóa Chicago Board of Trade (CBOT) mờ dần vào hậu cảnh.",
            "tier2": "Ống kính chuyển dịch hướng về dòng sông mẹ Mekong mênh mang sóng nước, nơi quyết định sinh mệnh thực sự của toàn bộ vựa lúa.",
            "tier3": "Cú máy chuyển nét (rack focus) từ sàn giao dịch sang dòng chảy tự nhiên của sông Mekong (Rack focus from trading screens to natural Mekong river)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a cinematic transition from soft-focused commodity market ticker screens in the foreground shifting focus to a magnificent wide view of the mighty Mekong River in the background",
        "setting": "a strategic observation veranda overlooking the broad Mekong waterway at golden hour",
        "motion": "Smooth rack focus from digital market screens to the majestic physical expanse of the Mekong River"
    },
    {
        "id": "CH06_SC060",
        "dur": "2.62s",
        "words": 10,
        "text": "Nó đang diễn ra ngay trên dòng sông mẹ Mekong",
        "anatomy": {
            "tier1": "Ngã ba sông Mekong hùng vĩ cuồn cuộn dòng nước đỏ nặng phù sa trĩu hạt dưới ánh hoàng hôn rực rỡ.",
            "tier2": "Dòng sông mẹ ngàn năm nuôi nấng đồng bằng sông Cửu Long đang phải gánh chịu những vết nứt thủy văn từ thượng nguồn.",
            "tier3": "Cú máy bay chậm dọc theo dòng sông Mekong đỏ nặng phù sa (Slow aerial glide along sediment-rich red Mekong waters)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a breathtaking aerial panorama of the mighty Mekong River flowing with rich red-brown alluvium water through lush delta shores under warm evening skies",
        "setting": "the grand waterways of the Mekong River at sunset in southern Vietnam",
        "motion": "Slow cinematic aerial glide following the majestic alluvium-rich river channel"
    },
    {
        "id": "CH06_SC061",
        "dur": "4.72s",
        "words": 18,
        "text": "nơi gọng kìm thủy văn và cuộc chiến nội vùng đe dọa trực tiếp cội nguồn sản xuất.",
        "anatomy": {
            "tier1": "Sơ đồ thủy văn toàn lưu vực sông Mekong hiển thị các chuỗi đập thủy điện thượng nguồn và các kênh đào nhân tạo chuyển dòng.",
            "tier2": "Gọng kìm thủy văn siết chặt dần vào hạ lưu ĐBSCL, báo hiệu trận chiến sinh tử bảo vệ nguồn nước và phù sa trong Chương 7.",
            "tier3": "Cú máy trượt ngang dọc theo chuỗi đập thủy văn Mekong thượng nguồn xuống hạ lưu (Horizontal tracking shot from upstream dams down to the delta)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic basin-wide hydrological schematic of the Mekong River showing upstream cascade mega-dams and diversion canals constricting downstream sediment and freshwater flows into the delta",
        "setting": "a regional transboundary hydrological monitoring center in warm amber and terracotta lighting",
        "motion": "Slow horizontal tracking shot following the hydrological constriction from upstream dams to the delta"
    }
]

# Generate Markdown Storyboard
md_lines = [
    "# chapter_06_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 6: Khúc Cua Địa Kinh Tế: Cú Xả Hàng Của Gã Khổng Lồ Ấn Độ Và Phép Thử 2025",
    "## Phong cách chủ đạo: Luminous Warm Editorial Illustration (Minh họa báo chí cao cấp, ánh sáng trong trẻo rực rỡ, 100% không gian vật lý đời thực, triệt tiêu hoàn toàn siêu thực và màu đen u ám)",
    "",
    "### 🎨 Hệ màu 60-30-10 (Tuyệt Đối Ấm Áp — Chống Lạnh Lẽo):",
    "- **60% Tông màu nền chủ đạo:** Warm Ivory Cream (`#FAF7EE`), Warm Sunset Amber Sky (`#FFFBEB`), Warm River Ganges & Mekong Alluvium Water (`#F3E5AB`). Tuyệt đối không dùng nền xám lạnh, xanh cyan buốt giá hay đen kịt.",
    "- **30% Đường nét & Chủ thể:** Ripe Golden Amber (`#F59E0B`), Terracotta Brick & Delta Clay (`#EA580C`), Classical Teak & Mahogany Wood (`#2D241E`), Export Container Crimson Red (`#DC2626`).",
    "- **10% Điểm nhấn dẫn mắt:** Luminous Warm Golden Sunrise Rays (`#D97706`), Warm Interior Chandelier Glow in New Delhi & Hanoi, Glowing Golden Amber Data Badges.",
    "",
    "---",
    "",
    "### 🛡️ Quy Tắc Kiểm Soát Tuyệt Đối:",
    "1. **Scene ID chuẩn theo chương:** `CH06_SC001` đến `CH06_SC061` (Khớp 100% với `scene_timing_map.json`).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Dinh New Delhi, khu kho dự trữ lương thực FCI (Ấn Độ), cảng Kakinada, cảng Cát Lái/Cái Mép, trụ sở FAO, đồng bằng sông Hằng, Viện Lúa ĐBSCL, đồng ruộng Sóc Trăng, siêu thị Kuala Lumpur/Thượng Hải, dòng sông Mekong.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc đúng 12/61 phân cảnh (19.67%) có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. 49 phân cảnh còn lại để `[TEXT OVERLAY]: Không`.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Ảnh Tham Chiếu Nhân Vật / Địa Danh:**",
    "   - `@modi_india.jpg` sử dụng tại `CH06_SC008`, `CH06_SC019`, `CH06_SC021` (Thủ tướng Ấn Độ Narendra Modi).",
    "   - Nhân vật dân sự (nông dân, thương lái, kỹ sư, người tiêu dùng): Tuyệt đối KHÔNG dùng ảnh tham chiếu nhân tạo, mô tả trực tiếp trong prompt.",
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

# Save chapter_06_visual.md
with open("episodes/vu-khi-gao-viet-nam/chapter_06_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_06_visual.md ({len(scenes_data)} scenes)")

# Generate prompts_chapter_06.txt
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

with open("episodes/vu-khi-gao-viet-nam/prompts_chapter_06.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompt_lines).strip() + "\n")

print(f"✅ Generated prompts_chapter_06.txt ({len(scenes_data)} scenes)")
