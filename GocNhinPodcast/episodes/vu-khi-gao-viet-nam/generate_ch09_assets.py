"""
Script to generate both chapter_09_visual.md and prompts_chapter_09.txt
for Episode 'Vũ Khí Lúa Gạo Việt Nam' - Chapter 09.
Strictly adheres to:
- Flow Batch Studio syntax
- Warm Luminous Editorial Palette (#FAF7EE, #F59E0B, #EA580C)
- Selective Lower-Left 25% Rule (~20% text overlay)
- Canonical references: @gs_vo_tong_xuan.jpg, @cuba_president_diaz_canel.jpg
- Steady camera and static text preservation in video prompts
"""

import re
import json

scenes_data = [
    {
        "id": "CH09_SC001",
        "dur": "3.94s",
        "words": 15,
        "text": "Sức mạnh đích thực của một cường quốc lương thực không đo bằng việc tích",
        "anatomy": {
            "tier1": "Một kho lúa dự trữ quốc gia đồ sộ nhưng mở rộng cửa đón ánh bình minh rạng rỡ thay vì khóa chặt cửa.",
            "tier2": "Hình ảnh biểu tượng: Sự thịnh vượng được tạo ra để sẻ chia chứ không phải để tích trữ vị kỷ hay phong tỏa.",
            "tier3": "Cú máy trượt ngang chậm qua kho lúa mở rộng cửa đón nắng mai (Slow horizontal tracking shot past open granary doors)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a grand rustic grain storehouse with open wooden doors welcoming bright morning sunlight over golden paddy sacks, symbolizing generosity rather than self-serving hoarding",
        "setting": "a sunny agricultural granary courtyard under warm amber morning skies",
        "motion": "Slow horizontal tracking shot past the open storehouse doors welcoming morning sunlight"
    },
    {
        "id": "CH09_SC002",
        "dur": "3.94s",
        "words": 15,
        "text": "trữ của cải hay dùng cái đói để áp đặt quyền lực lên kẻ khác.",
        "anatomy": {
            "tier1": "Bàn cờ địa chính trị thế giới với các biểu tượng phong tỏa lương thực mờ dần và bị xóa bỏ.",
            "tier2": "Đôi bàn tay ấm áp nâng niu hạt lúa giống, từ chối việc vũ khí hóa cái đói để áp đặt quyền lực.",
            "tier3": "Cú máy nâng chậm từ bàn cờ quyền lực lên đôi bàn tay nâng niu hạt giống (Slow upward tilt from geopolitical board to caring hands)."
        },
        "overlay": None,
        "ref": None,
        "subj": "warm hands gently cupping a handful of golden rice seeds, turning away from cold geopolitical trade embargo markers in the background, symbolizing humane ethics",
        "setting": "an editorial study room in warm ivory cream and golden ambient light",
        "motion": "Slow upward tilt from the table to the warm hands holding the golden seeds of life"
    },
    {
        "id": "CH09_SC003",
        "dur": "6.3s",
        "words": 24,
        "text": "Với người Việt Nam, hạt gạo sinh ra từ bùn đất và mồ hôi còn mang theo một sứ mệnh nhân văn cao đẹp.",
        "anatomy": {
            "tier1": "Cánh đồng lúa Việt Nam màu mỡ phù sa son rực rỡ dưới ánh bình minh, người nông dân lưng áo ướt đẫm mồ hôi.",
            "tier2": "Bông lúa vàng trĩu hạt nảy mầm từ bùn đất và giọt mồ hôi nhọc nhằn, kết tinh thành biểu tượng của tình người và đức hy sinh.",
            "tier3": "Cú máy hạ thấp lướt trên bùn đất phù sa nâng lên bông lúa trĩu hạt (Low-angle slow tracking shot from rich muddy alluvium up to golden grain)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a hardworking Vietnamese farmer in conical hat standing knee-deep in rich muddy delta alluvium holding a heavy golden sheaf of newly harvested rice, radiant under morning sunlight",
        "setting": "a fertile rice paddy in southern Vietnam under glorious golden dawn light",
        "motion": "Low-angle smooth tracking shot from the fertile muddy water up to the golden rice sheaf"
    },
    {
        "id": "CH09_SC004",
        "dur": "3.67s",
        "words": 14,
        "text": "Đó là sự đồng cam cộng khổ và triết lý sẻ chia chén cơm",
        "anatomy": {
            "tier1": "Hình ảnh mâm cơm gia đình mộc mạc bên chiếc bàn gỗ nâu ấm cúng dưới mái nhà tranh truyền thống.",
            "tier2": "Bát cơm trắng nóng hổi được xới đôi, chia sẻ thân tình giữa những người bạn trong thời khắc khó khăn.",
            "tier3": "Cú máy đẩy chậm vào bát cơm trắng bốc khói sẻ chia thân tình (Slow push-in on steaming bowl of shared rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a heartwarming editorial scene of a shared modest wooden meal table where a steaming bowl of fresh white rice is being generously shared between friends",
        "setting": "a rustic sunlit veranda in warm morning ambient light",
        "motion": "Slow push-in shot toward the steaming bowl of rice being shared across the table"
    },
    {
        "id": "CH09_SC005",
        "dur": "3.67s",
        "words": 14,
        "text": "manh áo với bạn bè quốc tế trong những thời khắc gian nan nhất.",
        "anatomy": {
            "tier1": "Bức ảnh kỷ niệm tình bạn quốc tế thủy chung treo trang trọng trong phòng truyền thống đối ngoại.",
            "tier2": "Hình ảnh đại diện Việt Nam và bạn bè châu Phi, Mỹ Latinh siết chặt tay nhau trong những năm tháng gian nan.",
            "tier3": "Cú máy trượt ngang qua những bức ảnh tư liệu tình bạn quốc tế (Horizontal tracking shot past diplomatic archival photos)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a heritage gallery wall of framed archival photographs depicting Vietnamese agricultural missions embracing African and Latin American brothers in solidarity",
        "setting": "a diplomatic friendship gallery under warm museum spotlights",
        "motion": "Slow horizontal tracking shot past the historic photographs of international solidarity"
    },
    {
        "id": "CH09_SC006",
        "dur": "5.51s",
        "words": 21,
        "text": "Nhiều cường quốc trên thế giới thường viện trợ lương thực bằng cách chở ngũ cốc dư thừa sang phân phát.",
        "anatomy": {
            "tier1": "Một bến cảng ở nước đang phát triển với tàu hàng lớn thả những bao tải ngũ cốc dư thừa xuống cầu cảng.",
            "tier2": "Đoàn xe phân phát hàng viện trợ ngũ cốc nước ngoài xếp hàng dài, tạo tâm lý thụ động phụ thuộc.",
            "tier3": "Cú máy góc rộng quay cảnh phân phát ngũ cốc viện trợ dư thừa (Wide cinematic shot of surplus grain aid distribution)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a distant industrial seaport where foreign cargo freighters drop off generic bags of surplus grain aid onto trucks in an African port, illustrating conventional food relief models",
        "setting": "a dusty coastal port terminal under warm bright midday sun",
        "motion": "Wide cinematic tracking shot observing the mechanized unloading of foreign surplus grain"
    },
    {
        "id": "CH09_SC007",
        "dur": "2.62s",
        "words": 10,
        "text": "Cách làm ấy chỉ xoa dịu cơn đói tức thời",
        "anatomy": {
            "tier1": "Người dân địa phương nhận từng túi ngũ cốc viện trợ ngắn hạn tại một điểm phân phát ven đường.",
            "tier2": "Bữa ăn tạm bợ qua ngày, giải quyết cơn đói trước mắt nhưng không tạo ra sinh kế lâu dài.",
            "tier3": "Cú máy trượt ngang qua điểm phân phát lương thực tạm thời (Horizontal tracking shot past temporary aid distribution station)."
        },
        "overlay": None,
        "ref": None,
        "subj": "local villagers receiving daily grain ration bags at a roadside distribution tent under the hot sun, providing immediate temporary relief",
        "setting": "a rural village center in eastern Africa under warm dusty daylight",
        "motion": "Slow horizontal tracking shot past the daily grain relief line"
    },
    {
        "id": "CH09_SC008",
        "dur": "4.72s",
        "words": 18,
        "text": "nhưng lại vô tình bóp chết nền nông nghiệp bản địa vì giá nông sản ngoại rẻ mạt.",
        "anatomy": {
            "tier1": "Khu chợ nông sản địa phương châu Phi nơi các sạp nông sản của nông dân bản địa vắng tanh không người mua.",
            "tier2": "Cánh đồng nông thôn bản xứ bị bỏ hoang vì không thể cạnh tranh nổi với nguồn ngũ cốc viện trợ giá rẻ mạt tràn ngập thị trường.",
            "tier3": "Cú máy lùi chậm từ cánh đồng bị bỏ hoang hướng ra khu chợ vắng vẻ (Slow pull-back shot from abandoned field toward empty market)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an abandoned local grain stall in an African village market beside fallow overgrown fields, where domestic smallholders could not compete against cheap dumping of foreign surplus food",
        "setting": "a quiet provincial African market square under warm afternoon light",
        "motion": "Slow pull-back camera shot from the silent field to the empty local grain market"
    },
    {
        "id": "CH09_SC009",
        "dur": "6.82s",
        "words": 26,
        "text": "Người Việt Nam lựa chọn một con đường hoàn toàn khác biệt: trao chiếc cần câu sinh kế bằng cách chuyển giao tri thức canh tác.",
        "anatomy": {
            "tier1": "Một lớp học nông nghiệp thực nghiệm ngoài đồng ruộng tại châu Phi rợp bóng cây keo và nắng ấm.",
            "tier2": "Chuyên gia nông nghiệp Việt Nam tận tình hướng dẫn nông dân địa phương cách ủ mầm lúa, ngâm hạt giống và chuẩn bị làm đất.",
            "tier3": "Cú máy tĩnh trực diện vào triết lý Trao Cần Câu Sinh Kế Nông Nghiệp (Steady shot on 'Giving the Fishing Rod' agronomic philosophy) cùng text overlay góc trái dưới."
        },
        "overlay": "TRAO CẦN CÂU SINH KẾ NÔNG NGHIỆP",
        "ref": None,
        "subj": "a passionate Vietnamese agricultural specialist in field khakis kneeling beside African local farmers demonstrating seed germination techniques in warm fertile soil under an acacia tree",
        "setting": "an open-air agronomy training field in rural Africa under warm sunny skies",
        "motion": "Steady camera shot framing the Vietnamese expert transferring practical rice cultivation skills"
    },
    {
        "id": "CH09_SC010",
        "dur": "3.94s",
        "words": 15,
        "text": "Chuyên gia của chúng ta đã có mặt tại hơn mười quốc gia châu Phi",
        "anatomy": {
            "tier1": "Bản đồ lục địa châu Phi với những đốm sáng vàng cam đánh dấu các dự án hợp tác nông nghiệp của Việt Nam.",
            "tier2": "Hơn 10 quốc gia từ Tây Phi sang Đông Phi tỏa sáng các biểu tượng bông lúa hợp tác Nam - Nam.",
            "tier3": "Cú máy bay chậm trên cao bao quát bản đồ các dự án nông nghiệp châu Phi (Slow aerial sweep across African agricultural project map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an illuminated geopolitical map of the African continent highlighting over ten partner nations from West to East Africa with golden glowing seedling icons representing Vietnamese South-South cooperation",
        "setting": "an international development agency command display in warm amber tones",
        "motion": "Slow cinematic glide across the African partnership map"
    },
    {
        "id": "CH09_SC011",
        "dur": "3.41s",
        "words": 13,
        "text": "từ thung lũng Zambezi ở Mozambique đến rìa sa mạc Sahara tại Senegal.",
        "anatomy": {
            "tier1": "Khung cảnh đối lập: Thung lũng sông Zambezi màu mỡ (Mozambique) và những cánh đồng ven rìa sa mạc Sahara (Senegal).",
            "tier2": "Màu xanh của những ruộng lúa giống Việt Nam vươn lên kiêu hãnh trên đất châu Phi dưới bàn tay chuyên gia nước nhà.",
            "tier3": "Cú máy trượt ngang qua hai miền đất Zambezi và Senegal (Horizontal tracking shot past Zambezi valley and Senegal dunes)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic diptych landscape showing emerald green rice fields flourishing along the Zambezi River valley in Mozambique on one side and irrigated rice terraces against Senegal golden dunes on the other",
        "setting": "diverse African agricultural landscapes under warm golden sun",
        "motion": "Smooth horizontal tracking shot across the thriving rice crops across the two African regions"
    },
    {
        "id": "CH09_SC012",
        "dur": "3.67s",
        "words": 14,
        "text": "Hình ảnh cố Giáo sư Võ Tòng Xuân mang đôi dép rọ lội bùn",
        "anatomy": {
            "tier1": "Thửa ruộng đầm lầy tại Sierra Leone bùn ngập đến bắp chân dưới ánh nắng ban mai rạng rỡ.",
            "tier2": "Cố Giáo sư Võ Tòng Xuân trong bộ quần áo kaki giản dị, chân đi đôi dép rọ cao su quen thuộc, lội bùn hướng dẫn bà con nông dân.",
            "tier3": "Cú máy tĩnh trực diện vào hình ảnh Giáo sư Võ Tòng Xuân tại Sierra Leone (Steady shot on Prof. Vo Tong Xuan in Sierra Leone) cùng text overlay góc trái dưới."
        },
        "overlay": "GS. VÕ TÒNG XUÂN (SIERRA LEONE)",
        "ref": "gs_vo_tong_xuan.jpg",
        "subj": "renowned Vietnamese agronomist Professor Vo Tong Xuan in his signature field attire and humble rubber sandals wading knee-deep in mud in an African wetland rice field",
        "setting": "a muddy demonstration paddy in rural Sierra Leone under warm tropical morning sun",
        "motion": "Steady camera shot framing Professor Vo Tong Xuan wading through the experimental paddy"
    },
    {
        "id": "CH09_SC013",
        "dur": "3.67s",
        "words": 14,
        "text": "tại Sierra Leone đã trở thành biểu tượng sống động cho tinh thần ấy.",
        "anatomy": {
            "tier1": "Bức ảnh chân dung tài liệu lịch sử của Giáo sư Võ Tòng Xuân mỉm cười đôn hậu giữa những người nông dân Sierra Leone.",
            "tier2": "Bà con nông dân châu Phi vây quanh Giáo sư với ánh mắt kính trọng, xem ông như người cha, người thầy khai sinh mùa vụ mới.",
            "tier3": "Cú máy đẩy chậm vào nụ cười ấm áp của Giáo sư Võ Tòng Xuân giữa bà con (Slow push-in on Prof. Vo Tong Xuan warm smile among farmers)."
        },
        "overlay": None,
        "ref": "gs_vo_tong_xuan.jpg",
        "subj": "Professor Vo Tong Xuan smiling warmly surrounded by grateful African rice farmers, holding a cluster of healthy rice panicles together under a broad shady tree",
        "setting": "a joyful agricultural community gathering in Sierra Leone in warm golden sunlight",
        "motion": "Slow push-in shot toward Professor Vo Tong Xuan smiling warmly with local farmers"
    },
    {
        "id": "CH09_SC014",
        "dur": "2.36s",
        "words": 9,
        "text": "Ông không giảng giải lý thuyết trên bục giảng",
        "anatomy": {
            "tier1": "Bục giảng và giảng đường đại học để trống, ánh nắng chiếu qua cửa sổ vào những trang sách giáo trình.",
            "tier2": "Giáo sư chọn đồng ruộng làm giảng đường thực tế, nơi lý thuyết hòa cùng hơi thở đất đai và cuộc sống cần lao.",
            "tier3": "Cú máy nâng chậm từ giảng đường hướng ra cánh đồng mênh mông ngoài cửa sổ (Slow upward tilt from empty lecture podium toward outdoor fields)."
        },
        "overlay": None,
        "ref": "gs_vo_tong_xuan.jpg",
        "subj": "an empty academic lecture podium in foreground while broad windows reveal the true classroom outside: an active sunny rice paddy full of practical field work",
        "setting": "an agricultural training institute overlooking expansive fields in warm sunlight",
        "motion": "Slow upward tilt from the empty podium toward the sunlit fields beyond the window"
    },
    {
        "id": "CH09_SC015",
        "dur": "4.99s",
        "words": 19,
        "text": "mà trực tiếp xắn quần cùng nông dân bản địa cày bừa, ủ mầm và cấy mạ thẳng hàng.",
        "anatomy": {
            "tier1": "Ruộng lúa nước ngập bùn phù sa ấm nơi Giáo sư và nông dân châu Phi xắn quần quá gối cùng cấy từng hàng mạ non xanh biếc.",
            "tier2": "Những dây cấy mạ thẳng tắp căng ngang mặt ruộng, kỹ thuật cấy mạ một tép kiểu miền Tây được truyền dạy trực quan, sống động.",
            "tier3": "Cú máy trượt ngang dọc theo hàng mạ non cấy thẳng tắp (Horizontal tracking shot along straight green seedling rows)."
        },
        "overlay": None,
        "ref": "gs_vo_tong_xuan.jpg",
        "subj": "Professor Vo Tong Xuan and local African farmers with rolled-up trousers transplanting neat straight rows of vibrant green rice seedlings into flooded mud along guiding string lines",
        "setting": "a community test paddy in West Africa under warm bright sunshine",
        "motion": "Slow horizontal tracking shot past the straight rows of newly planted green seedlings"
    },
    {
        "id": "CH09_SC016",
        "dur": "4.72s",
        "words": 18,
        "text": "Năng suất lúa tại các vùng đầm lầy nghèo khó vọt lên gần năm tấn một héc ta",
        "anatomy": {
            "tier1": "Cánh đồng lúa vàng óng ả bội thu tại vùng đầm lầy Mange Bureh (Sierra Leone) từng một thời cằn cỗi đói kém.",
            "tier2": "Bảng cân đo năng suất ruộng báo đạt gần 5 tấn/ha, cao gấp ba lần năng suất truyền thống của địa phương.",
            "tier3": "Cú máy nâng chậm từ bông lúa trĩu hạt lên nụ cười mừng rỡ của nông dân (Slow tilt-up from heavy golden rice heads to cheering farmers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a bountiful golden rice harvest in the former wetlands of Sierra Leone with local farmers joyfully celebrating average yields surging to nearly 5 metric tons per hectare",
        "setting": "a sun-drenched golden harvest field in Sierra Leone under warm blue skies",
        "motion": "Slow tilt-up from overflowing baskets of golden paddy to cheering local families"
    },
    {
        "id": "CH09_SC017",
        "dur": "3.67s",
        "words": 14,
        "text": "mở đường cho dự án năm triệu đô la được ký kết cùng FAO.",
        "anatomy": {
            "tier1": "Phòng họp ngoại giao của Tổ chức Lương thực và Nông nghiệp Liên Hợp Quốc (FAO) với quốc kỳ Việt Nam và Sierra Leone.",
            "tier2": "Lễ ký kết dự án hợp tác ba bên trị giá 5 triệu USD chuyển giao công nghệ lúa gạo Việt Nam cho châu Phi.",
            "tier3": "Cú máy tĩnh trực diện vào văn bản dự án hợp tác FAO 5 triệu USD (Steady shot on $5M FAO Tripartite Cooperation Agreement) cùng text overlay góc trái dưới."
        },
        "overlay": "DỰ ÁN HỢP TÁC FAO: 5 TRIỆU USD",
        "ref": None,
        "subj": "the formal tripartite signing ceremony involving the Food and Agriculture Organization (FAO), Vietnam, and Sierra Leone for a 5 million USD rice development partnership project",
        "setting": "an international treaty chamber under warm dignified chandelier lighting",
        "motion": "Steady camera shot framing the 5 million USD FAO tripartite agreement signing"
    },
    {
        "id": "CH09_SC018",
        "dur": "3.67s",
        "words": 14,
        "text": "Nhưng có lẽ, câu chuyện cảm động và sâu sắc nhất chính là hành",
        "anatomy": {
            "tier1": "Bức tường lưu niệm quan hệ đặc biệt Việt Nam - Cuba với các hình ảnh lãnh tụ hai nước qua nhiều thập kỷ.",
            "tier2": "Bản đồ đường hàng hải và hàng không nối liền Hà Nội và La Habana qua nửa vòng Trái Đất.",
            "tier3": "Cú máy đẩy chậm vào hình ảnh Chủ tịch Hồ Chí Minh và Chủ tịch Fidel Castro (Slow push-in on archival portrait of President Ho Chi Minh and Fidel Castro)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a historic friendship hall displaying timeless portraits of Cuban and Vietnamese historic leaders alongside archival documents of mutual fraternal support",
        "setting": "a diplomatic memorial gallery under warm golden ambient lighting",
        "motion": "Slow push-in shot toward the archival historic photographs of fraternal solidarity"
    },
    {
        "id": "CH09_SC019",
        "dur": "3.94s",
        "words": 15,
        "text": "trình hơn hai mươi năm sát cánh cùng nhân dân Cuba qua năm giai đoạn.",
        "anatomy": {
            "tier1": "Bảng tổng kết 5 giai đoạn Dự án Hợp tác Phát triển Lúa gạo Việt Nam - Cuba kéo dài hơn 20 năm.",
            "tier2": "Từ những năm 2002 đến nay, các đoàn chuyên gia lúa gạo Việt Nam kiên trì bám trụ trên các cánh đồng Cuba qua mọi thăng trầm.",
            "tier3": "Cú máy trượt ngang qua biểu đồ 5 giai đoạn hợp tác nông nghiệp (Horizontal tracking shot past 5-phase cooperation timeline)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an analytical timeline chart outlining the five continuous phases of the 20-year Vietnam-Cuba Rice Development Cooperation Project stretching from 2002 to the present",
        "setting": "a bilateral cooperation ministry office in warm amber tones",
        "motion": "Slow horizontal tracking shot tracing the 20-year bilateral timeline"
    },
    {
        "id": "CH09_SC020",
        "dur": "4.72s",
        "words": 18,
        "text": "Nghĩa cử ấy nhắc chúng ta nhớ đến lời khẳng định bất hủ của Chủ tịch Fidel Castro",
        "anatomy": {
            "tier1": "Quảng trường Cách mạng tại La Habana với bức phù điêu lịch sử hào hùng dưới ánh nắng nhiệt đới Caribe rực rỡ.",
            "tier2": "Hình ảnh Chủ tịch Fidel Castro giơ cao lá cờ bách chiến bách thắng của Mặt trận Giải phóng miền Nam tại Quảng Trị năm 1973.",
            "tier3": "Cú máy tĩnh trực diện vào câu nói bất hủ của Chủ tịch Fidel Castro (Steady shot on historic Fidel Castro quotation landmark) cùng text overlay góc trái dưới."
        },
        "overlay": "VÌ VIỆT NAM, CUBA SẴN SÀNG HIẾN DÂNG CẢ MÁU",
        "ref": "cuba_president_diaz_canel.jpg",
        "subj": "the majestic Plaza de la Revolucion in Havana with historic monumental relief under warm Caribbean sunshine, evoking the legendary solidarity of Fidel Castro",
        "setting": "the grand Plaza de la Revolucion in Havana Cuba under warm radiant tropical skies",
        "motion": "Steady camera shot framing the iconic Havana revolutionary square"
    },
    {
        "id": "CH09_SC021",
        "dur": "3.15s",
        "words": 12,
        "text": "Vì Việt Nam, Cuba sẵn sàng hiến dâng cả máu của mình.",
        "anatomy": {
            "tier1": "Bức tượng đài tình hữu nghị Việt Nam - Cuba khắc sâu dòng chữ bất hủ bằng hai thứ tiếng Việt và Tây Ban Nha.",
            "tier2": "Những bông hoa dâm bụt đỏ thắm và nhành lúa vàng đặt trang trọng dưới chân tượng đài, biểu tượng cho ân tình son sắt.",
            "tier3": "Cú máy đẩy chậm vào dòng chữ khắc ghi ân tình Cuba - Việt Nam (Slow push-in on bronze inscription of fraternal pledge)."
        },
        "overlay": None,
        "ref": "cuba_president_diaz_canel.jpg",
        "subj": "a commemorative bronze monument inscribed with the immortal words 'For Vietnam, Cuba is ready to give even its own blood' in Vietnamese and Spanish with red flowers at its base",
        "setting": "a sunlit peaceful memorial park in warm morning light",
        "motion": "Slow push-in shot toward the golden inscribed bronze plaque"
    },
    {
        "id": "CH09_SC022",
        "dur": "2.1s",
        "words": 8,
        "text": "Để đáp lại ân tình thủy chung đó",
        "anatomy": {
            "tier1": "Phòng chuẩn bị hạt giống của Viện Cây lương thực và Cây thực phẩm Việt Nam.",
            "tier2": "Các nhà khoa học nông nghiệp cẩn thận đóng gói những túi hạt giống lúa thuần chủng tốt nhất để chuyển sang Cuba.",
            "tier3": "Cú máy cận cảnh niêm phong những gói hạt giống lúa thuần tặng nhân dân Cuba (Close-up shot of sealing pure rice seed packets for Cuba)."
        },
        "overlay": None,
        "ref": None,
        "subj": "dedicated Vietnamese agronomy researchers carefully inspecting and sealing bags of pure certified rice seed varieties labeled for transfer to Cuba",
        "setting": "an agronomic seed bank facility in warm natural lighting",
        "motion": "Close-up slow push-in shot on the labeled certified rice seed bags"
    },
    {
        "id": "CH09_SC023",
        "dur": "5.51s",
        "words": 21,
        "text": "các nhà khoa học Việt Nam đã mang những giống lúa tốt nhất bay nửa vòng Trái Đất sang giúp bạn.",
        "anatomy": {
            "tier1": "Cánh đồng lúa tại tỉnh Matanzas hoặc Pinar del Río (Cuba) dưới bầu trời Caribe xanh ngắt nắng ấm.",
            "tier2": "Đoàn chuyên gia nông nghiệp Việt Nam cùng các kỹ sư Cuba đang hướng dẫn nông dân địa phương kỹ thuật gieo sạ và tưới tiêu.",
            "tier3": "Cú máy bay chậm dọc theo cánh đồng lúa xanh mướt tại Cuba (Slow aerial glide across lush green Cuban rice paddies)."
        },
        "overlay": None,
        "ref": None,
        "subj": "Vietnamese rice agronomists working side by side with Cuban farmers in straw hats in vast emerald rice paddies in Pinar del Rio under the warm Caribbean sun",
        "setting": "a sweeping irrigated rice valley in western Cuba under bright tropical skies",
        "motion": "Slow aerial glide across the flourishing Cuban rice fields with Vietnamese experts"
    },
    {
        "id": "CH09_SC024",
        "dur": "3.41s",
        "words": 13,
        "text": "Năng suất lúa tại các vùng dự án tăng gấp gần ba lần",
        "anatomy": {
            "tier1": "Sân phơi thóc của nông trường Cuba vàng rực lúa mới thu hoạch dưới nắng ấm.",
            "tier2": "Biểu đồ so sánh năng suất: Từ mức 1.8 - 2.0 tấn/ha truyền thống nhảy vọt lên gần gấp 3 lần nhờ quy trình canh tác Việt Nam.",
            "tier3": "Cú máy nâng chậm từ đống thóc vàng lên bảng thống kê năng suất tăng gấp 3 (Slow upward tilt from golden grain to 3x yield chart)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a bustling Cuban cooperative drying yard filled with golden grain mounds where local farmers and technicians celebrate yields multiplying nearly three-fold",
        "setting": "a provincial agricultural cooperative in Cuba under warm sunny skies",
        "motion": "Slow upward tilt from piles of golden paddy toward the joyful cooperative workers"
    },
    {
        "id": "CH09_SC025",
        "dur": "4.72s",
        "words": 18,
        "text": "đạt tới năm phẩy năm tấn một héc ta trên diện tích gần năm mươi nghìn héc ta.",
        "anatomy": {
            "tier1": "Toàn cảnh cánh đồng dự án rộng gần 50.000 héc ta tại Cuba trĩu hạt vàng rực.",
            "tier2": "Báo cáo kiểm toán nông nghiệp khẳng định con số năng suất ấn tượng đạt 5.5 tấn/ha phủ khắp gần 50.000 ha canh tác.",
            "tier3": "Cú máy tĩnh trực diện vào năng suất 5.5 tấn/ha trên gần 50.000 ha tại Cuba (Steady shot on 5.5 tons/ha across ~50,000 ha milestone) cùng text overlay góc trái dưới."
        },
        "overlay": "NĂNG SUẤT TẠI CUBA: 5,5 TẤN/HA (~50.000 HA)",
        "ref": None,
        "subj": "an expansive view of a massive 50,000-hectare agricultural project zone in Cuba teeming with golden ripe paddy, backed by an editorial metric indicating 5.5 metric tons per hectare yield",
        "setting": "a grand agricultural plain in central Cuba under bright warm afternoon sunlight",
        "motion": "Steady camera shot framing the sweeping golden fields and productivity metric"
    },
    {
        "id": "CH09_SC026",
        "dur": "5.51s",
        "words": 21,
        "text": "Tháng 6 năm 2025, Bộ Nông nghiệp Cuba đã chính thức công nhận bốn giống lúa thuần mang tên dòng VIBA",
        "anatomy": {
            "tier1": "Hội trường Bộ Nông nghiệp Cuba tại La Habana trong buổi lễ công nhận giống lúa quốc gia.",
            "tier2": "Chủ tịch Cuba Miguel Díaz-Canel và Bộ trưởng Nông nghiệp trao chứng nhận quốc gia công nhận 4 giống lúa thuần mang tên dòng VIBA.",
            "tier3": "Cú máy tĩnh trực diện vào chứng nhận 4 giống lúa thuần dòng VIBA (Steady shot on VIBA rice certification ceremony) cùng text overlay góc trái dưới."
        },
        "overlay": "DÒNG LÚA THUẦN VIBA (VIỆT NAM - CUBA)",
        "ref": "cuba_president_diaz_canel.jpg",
        "subj": "Cuban President Miguel Diaz-Canel presiding over the official Ministry of Agriculture ceremony in Havana formally certifying four pure rice varieties of the VIBA strain",
        "setting": "the executive hall of the Ministry of Agriculture in Havana under warm interior lighting",
        "motion": "Steady camera shot framing President Miguel Diaz-Canel and the official VIBA certification"
    },
    {
        "id": "CH09_SC027",
        "dur": "2.36s",
        "words": 9,
        "text": "biểu tượng cho hai chữ Việt Nam và Cuba.",
        "anatomy": {
            "tier1": "Bao giống lúa in logo 'VIBA' với hình ảnh hai lá cờ Việt Nam và Cuba đan cài vào nhau quanh nhánh lúa vàng.",
            "tier2": "Hạt lúa VIBA chắc mẩy, biểu tượng trường tồn cho tình anh em thủy chung son sắt giữa hai dân tộc.",
            "tier3": "Cú máy cận cảnh bao giống lúa VIBA với biểu tượng hai quốc kỳ (Close-up shot of VIBA certified seed bag with entwined flags)."
        },
        "overlay": None,
        "ref": "cuba_president_diaz_canel.jpg",
        "subj": "an elegant close-up of a certified seed bag prominently printed with the golden brand mark 'VIBA' featuring the intertwined national flags of Vietnam and Cuba",
        "setting": "an agricultural exhibition showroom under soft warm spotlighting",
        "motion": "Slow close-up push-in shot on the VIBA seed brand mark and entwined flags"
    },
    {
        "id": "CH09_SC028",
        "dur": "3.41s",
        "words": 13,
        "text": "Tại quê nhà, doanh nghiệp Việt dành hơn hai nghìn héc ta ruộng",
        "anatomy": {
            "tier1": "Cánh đồng sản xuất giống lúa rộng lớn tại Nam Định thẳng tắp bờ đê trong nắng sớm đồng bằng Bắc Bộ.",
            "tier2": "Hơn 2.000 héc ta đất lúa được các doanh nghiệp Việt Nam dành riêng với quy trình canh tác nghiêm ngặt nhất.",
            "tier3": "Cú máy bay chậm trên cao bao quát vùng ruộng giống 2.000 ha tại Nam Định (Slow aerial glide over 2,000-ha seed paddy in Nam Dinh)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a vast pristine 2,000-hectare specialized seed multiplication farmland in Nam Dinh northern Vietnam, organized with meticulous precision under warm morning sunlight",
        "setting": "the fertile Red River Delta plains in Nam Dinh under clear skies",
        "motion": "Slow aerial glide over the vast organized seed breeding paddies"
    },
    {
        "id": "CH09_SC029",
        "dur": "3.67s",
        "words": 14,
        "text": "giống ở Nam Định để nhân hạt lai F1 CT16 chuyển sang cho bạn.",
        "anatomy": {
            "tier1": "Nhà máy chế biến hạt giống hiện đại tại Nam Định với các máy sấy và đóng gói hạt giống lúa lai F1 CT16.",
            "tier2": "Các thùng hạt giống lai F1 CT16 đạt tiêu chuẩn kiểm dịch quốc tế được xếp lên pallet chuẩn bị xuất sang Cuba.",
            "tier3": "Cú máy trượt ngang qua dây chuyền đóng gói hạt giống lai F1 CT16 (Horizontal tracking shot past F1 CT16 hybrid seed packaging line)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an automated seed processing plant in Nam Dinh where high-purity F1 CT16 hybrid rice seeds are packaged and palletized in branded containers for air shipment to Cuba",
        "setting": "a high-tech agricultural seed processing facility in warm ambient lighting",
        "motion": "Slow horizontal tracking shot past the automated packaging line for F1 CT16 seeds"
    },
    {
        "id": "CH09_SC030",
        "dur": "6.82s",
        "words": 26,
        "text": "Đó là sự chung tay đầy trách nhiệm giữa các viện nghiên cứu và doanh nghiệp tư nhân vì một tình nghĩa quốc tế thiêng liêng.",
        "anatomy": {
            "tier1": "Bàn ký kết hợp tác giữa Viện Cây lương thực và các tập đoàn nông nghiệp tư nhân Việt Nam.",
            "tier2": "Các nhà khoa học và doanh nhân bắt tay nhau, chung sức đồng lòng vì sứ mệnh ngoại giao nhân văn của đất nước.",
            "tier3": "Cú máy trượt ngang qua lễ ký kết phối hợp công tư vì tình nghĩa quốc tế (Horizontal tracking shot past public-private partnership signing)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a public-private partnership signing ceremony bringing together state agronomic institutes and private agricultural enterprises dedicated to international solidarity initiatives",
        "setting": "a formal institutional conference room under warm ambient chandelier light",
        "motion": "Slow horizontal tracking shot past scientists and business executives uniting for the mission"
    },
    {
        "id": "CH09_SC031",
        "dur": "2.36s",
        "words": 9,
        "text": "Không dừng lại ở việc hỗ trợ kỹ thuật",
        "anatomy": {
            "tier1": "Văn phòng dự án đầu tư nông nghiệp Việt Nam tại La Habana với các bản vẽ quy hoạch đại điền.",
            "tier2": "Các doanh nhân Việt Nam mở rộng sang mô hình đầu tư trực tiếp, mang máy móc công nghệ cao sang đất bạn.",
            "tier3": "Cú máy đẩy chậm vào mô hình đầu tư trực tiếp tại Cuba (Slow push-in on direct agricultural investment model in Cuba)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a business briefing table in Havana displaying foreign direct investment blueprints for modern mechanized agro-industrial rice complexes across Cuban provinces",
        "setting": "an investment planning office in Havana under warm morning natural light",
        "motion": "Slow push-in shot toward the modern Cuban agricultural investment masterplan"
    },
    {
        "id": "CH09_SC032",
        "dur": "5.51s",
        "words": 21,
        "text": "các doanh nghiệp Việt Nam đã trực tiếp đầu tư xây dựng những đại điền công nghệ cao trên đất bạn.",
        "anatomy": {
            "tier1": "Đại điền công nghệ cao của doanh nghiệp Việt Nam tại Cuba với máy cày bánh xích và hệ thống tưới tiêu tự động.",
            "tier2": "Đội ngũ kỹ sư Việt Nam cùng công nhân Cuba vận hành dây chuyền canh tác quy mô lớn hiện đại.",
            "tier3": "Cú máy nâng chậm theo dàn máy móc nông nghiệp hiện đại trên đồng ruộng Cuba (Slow upward tilt along modern agricultural machinery in Cuba)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a sprawling modern commercial rice estate in western Cuba operated by Vietnamese agribusiness, featuring fleets of modern red tractors and combine harvesters",
        "setting": "a sunny agricultural plain in Cuba under warm radiant skies",
        "motion": "Slow upward tilt along a modern harvester operating in vast golden fields"
    },
    {
        "id": "CH09_SC033",
        "dur": "6.82s",
        "words": 26,
        "text": "Công ty Agri VMA trở thành doanh nghiệp nước ngoài đầu tiên được thuê một nghìn héc ta đất canh tác tại tỉnh Pinar del Río.",
        "anatomy": {
            "tier1": "Trụ sở điều hành và cổng vào dự án nông nghiệp của Công ty Agri VMA tại tỉnh Pinar del Río (Cuba).",
            "tier2": "Cánh đồng mẫu lớn 1.000 héc ta thẳng cánh cò bay do doanh nghiệp Việt Nam trực tiếp thuê và canh tác hiện đại.",
            "tier3": "Cú máy tĩnh trực diện vào dự án Agri VMA 1.000 ha tại Pinar del Río (Steady shot on Agri VMA 1,000 ha project) cùng text overlay góc trái dưới."
        },
        "overlay": "DỰ ÁN AGRI VMA: 1.000 HA (PINAR DEL RÍO)",
        "ref": None,
        "subj": "the entrance gate and administrative center of the Agri VMA agricultural enterprise in Pinar del Rio Cuba overlooking an expansive 1,000-hectare leased modern rice estate",
        "setting": "the agricultural heartland of Pinar del Rio Cuba under warm sunny skies",
        "motion": "Steady camera shot framing the Agri VMA project entrance and vast 1,000-hectare estate"
    },
    {
        "id": "CH09_SC034",
        "dur": "2.36s",
        "words": 9,
        "text": "Nhờ đưa máy móc hiện đại sang vận hành",
        "anatomy": {
            "tier1": "Dàn máy gặt đập liên hợp và máy cấy cơ giới hóa do Việt Nam mang sang đang chạy rộn rã trên đồng ruộng Cuba.",
            "tier2": "Kỹ sư cơ khí Việt Nam hướng dẫn thanh niên Cuba bảo trì và điều khiển máy nông nghiệp công suất lớn.",
            "tier3": "Cú máy trượt ngang theo dàn máy gặt đập liên hợp hoạt động trên đồng (Horizontal tracking shot past active combine harvesters)."
        },
        "overlay": None,
        "ref": None,
        "subj": "modern combine harvesters imported from Vietnam cutting clean swathes through heavy golden Cuban paddies, driven by trained local Cuban operators",
        "setting": "a sunny rice farm in Pinar del Rio in warm afternoon sun",
        "motion": "Slow horizontal tracking shot following the combine harvester cutting golden paddy"
    },
    {
        "id": "CH09_SC035",
        "dur": "6.04s",
        "words": 23,
        "text": "họ đạt năng suất chín tấn một héc ta và bàn giao hai nghìn bốn trăm tấn gạo sạch cho nhân dân Cuba.",
        "anatomy": {
            "tier1": "Kho chứa ngũ cốc của dự án Agri VMA đầy ắp các bao gạo sạch trắng muốt đóng gói tiêu chuẩn cao.",
            "tier2": "Lễ bàn giao 2.400 tấn gạo sạch đạt năng suất kỷ lục 9 tấn/ha cho đại diện chính quyền và nhân dân Cuba trong niềm hân hoan.",
            "tier3": "Cú máy tĩnh trực diện vào con số năng suất 9 tấn/ha và bàn giao 2.400 tấn gạo (Steady shot on 9 tons/ha yield & 2,400 tons handover) cùng text overlay góc trái dưới."
        },
        "overlay": "NĂNG SUẤT ĐẠT 9 TẤN/HA (BÀN GIAO 2.400 TẤN)",
        "ref": None,
        "subj": "a ceremonial handover ceremony in Cuba where Vietnamese project leaders formally present pallets of 2,400 metric tons of milled clean rice to Cuban provincial food authorities, celebrating a record 9 tons/ha yield",
        "setting": "a sunlit grain warehouse in Cuba under warm ambient lighting",
        "motion": "Steady camera shot framing the massive stacks of rice bags and the official handover"
    },
    {
        "id": "CH09_SC036",
        "dur": "6.3s",
        "words": 24,
        "text": "Cùng với đó, tập đoàn TBAGRI cũng đã chế biến và bàn giao bốn trăm bảy mươi tấn gạo thương phẩm tại tỉnh Granma.",
        "anatomy": {
            "tier1": "Nhà máy chế biến lúa gạo của tập đoàn TBAGRI tại tỉnh Granma (Cuba) rực rỡ dưới nắng ấm.",
            "tier2": "Đoàn xe tải chở 470 tấn gạo thương phẩm chất lượng cao chuẩn bị tỏa đi phục vụ các bếp ăn bệnh viện, trường học của người dân Cuba.",
            "tier3": "Cú máy trượt ngang qua đoàn xe chở gạo TBAGRI tại tỉnh Granma (Horizontal tracking shot past TBAGRI rice distribution trucks)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the modern grain processing facility of TBAGRI in Granma province Cuba with clean transport trucks departing loaded with 470 metric tons of packaged commercial rice for hospitals and schools",
        "setting": "an agro-processing compound in eastern Cuba under warm morning sun",
        "motion": "Slow horizontal tracking shot following loaded rice delivery trucks departing the facility"
    },
    {
        "id": "CH09_SC037",
        "dur": "3.15s",
        "words": 12,
        "text": "Từng đi qua nỗi đau tột cùng của nạn đói năm 1945",
        "anatomy": {
            "tier1": "Bức tranh phù điêu hoặc ảnh tư liệu lịch sử tưởng niệm nạn đói Ất Dậu 1945 trong Bảo tàng Lịch sử Quốc gia.",
            "tier2": "Ánh mắt đau đáu của người xưa, bài học lịch sử xương máu nhắc nhở thế hệ hôm nay về giá trị thiêng liêng của sự sống.",
            "tier3": "Cú máy đẩy chậm vào bức phù điêu lịch sử tưởng niệm nạn đói 1945 (Slow push-in on memorial relief commemorating 1945 famine)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a solemn bronze memorial relief in the National Museum of History depicting the profound historic memory of the 1945 famine, reminding generations of the precious value of life",
        "setting": "a solemn museum exhibition hall under warm focused gallery light",
        "motion": "Slow push-in shot toward the evocative bronze historical memorial relief"
    },
    {
        "id": "CH09_SC038",
        "dur": "4.99s",
        "words": 19,
        "text": "người Việt thấu hiểu sâu sắc hơn ai hết giá trị sinh tồn của từng bát cơm no ấm.",
        "anatomy": {
            "tier1": "Bát cơm trắng tinh khôi, dẻo thơm trên bàn thờ gia tiên hoặc mâm cơm gia đình Việt Nam.",
            "tier2": "Hình ảnh thế hệ con cháu nâng niu từng hạt cơm no ấm với lòng biết ơn cội nguồn sâu sắc.",
            "tier3": "Cú máy nâng chậm từ bát cơm trắng lên ánh mắt biết ơn của con người (Slow upward tilt from bowl of white rice to grateful eyes)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a simple ceramic bowl of pristine steaming white rice resting on an ancestral wooden table in soft warm morning light, symbolizing survival, gratitude, and dignity",
        "setting": "a tranquil traditional Vietnamese home under warm gentle morning rays",
        "motion": "Slow upward tilt from the glistening bowl of rice toward the tranquil morning window"
    },
    {
        "id": "CH09_SC039",
        "dur": "4.46s",
        "words": 17,
        "text": "Chúng ta bước ra thế giới không phải bằng sự áp đặt hay toan tính vị kỷ",
        "anatomy": {
            "tier1": "Cầu cảng xuất khẩu quốc tế với hình ảnh các con tàu Việt Nam chở lúa giống và tri thức sang bạn bè quốc tế.",
            "tier2": "Những nụ cười thân thiện và cái bắt tay bình đẳng, không hề có sự áp đặt hay toan tính bá quyền.",
            "tier3": "Cú máy trượt ngang qua bến cảng hữu nghị quốc tế (Horizontal tracking shot past international friendship dock)."
        },
        "overlay": None,
        "ref": None,
        "subj": "Vietnamese agricultural diplomats and technicians shaking hands warmly with international counterparts on equal terms beside grain freighters in a peaceful port",
        "setting": "a sunny international harbor under warm morning daylight",
        "motion": "Smooth horizontal tracking shot past the respectful diplomatic handshakes"
    },
    {
        "id": "CH09_SC040",
        "dur": "3.41s",
        "words": 13,
        "text": "mà bằng hạt giống sự sống và tấm lòng nhân ái bao la.",
        "anatomy": {
            "tier1": "Một mầm lúa xanh non vươn lên mạnh mẽ từ lớp đất nâu ấm áp trong lòng bàn tay.",
            "tier2": "Ánh sáng ban mai chiếu rọi vào mầm lúa, tượng trưng cho hạt giống sự sống và tình nhân ái của người Việt lan tỏa khắp năm châu.",
            "tier3": "Cú máy cận cảnh mầm lúa xanh non vươn lên trong nắng sớm (Close-up shot of green seedling sprouting in cupped hands)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a tender green rice sprout emerging from fertile dark earth cupped gently within caring open hands, illuminated by a warm radiant golden sunbeam",
        "setting": "a sunlit peaceful natural environment in warm morning light",
        "motion": "Slow close-up tilt up toward the radiant green sprout glistening in the morning light"
    },
    {
        "id": "CH09_SC041",
        "dur": "6.82s",
        "words": 26,
        "text": "Đó là thứ quyền lực mềm chân chính, nảy mầm từ lòng trắc ẩn và sự đồng cảm giữa những con người cùng chung cảnh ngộ.",
        "anatomy": {
            "tier1": "Hình ảnh những cánh đồng lúa xanh tốt tại Việt Nam, Cuba và châu Phi cùng đan cài vào nhau trong một bức tranh toàn cảnh rộng lớn.",
            "tier2": "Nụ cười rạng rỡ của những người nông dân các màu da khác nhau cùng chia sẻ mùa màng bội thu, biểu trưng cho quyền lực mềm đích thực.",
            "tier3": "Cú máy bay chậm trên cao (slow aerial glide) bao quát sự kết nối nhân văn toàn cầu (Slow aerial glide connecting global harvest panoramas)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an inspiring composite panorama showing golden thriving rice fields in Vietnam, Cuba, and Africa connected by radiant warm sunlight, celebrating genuine soft power born of empathy and compassion",
        "setting": "a grand global agricultural tapestry under warm golden skies",
        "motion": "Slow majestic aerial glide across the interconnected global harvest fields"
    },
    {
        "id": "CH09_SC042",
        "dur": "6.56s",
        "words": 25,
        "text": "Hạt gạo Việt Nam không chỉ là sức mạnh kinh tế, mà đã trở thành sứ giả của hòa bình và nhân phẩm dân tộc.",
        "anatomy": {
            "tier1": "Hình ảnh biểu tượng đỉnh cao: Một bông lúa vàng óng ả uốn cong duyên dáng trên nền quốc kỳ Việt Nam và chim bồ câu hòa bình bay lượn.",
            "tier2": "Hạt gạo Việt Nam tỏa sáng rực rỡ, hoàn tất sứ mệnh cao quý của một sứ giả hòa bình, nhân phẩm và lòng nhân ái của dân tộc.",
            "tier3": "Cú máy tĩnh trực diện vào biểu tượng Sứ Giả Hòa Bình & Nhân Phẩm Dân Tộc (Steady shot on Ambassador of Peace & National Dignity emblem) cùng text overlay góc trái dưới."
        },
        "overlay": "SỨ GIẢ HÒA BÌNH & NHÂN PHẨM DÂN TỘC",
        "ref": None,
        "subj": "a breathtaking, dignified editorial artistic composition of a graceful golden rice panicle curving upward beside a peaceful white dove in flight against a glowing warm sunrise, symbolizing peace and human dignity",
        "setting": "a magnificent patriotic dawn horizon in warm ivory cream, golden amber, and soft alluvium hues",
        "motion": "Steady camera shot framing the majestic golden rice panicle and peaceful horizon"
    }
]

# Generate Markdown Storyboard
md_lines = [
    "# chapter_09_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 9: Ngoại Giao Cây Lúa Và Sứ Mệnh Nhân Văn Của Người Việt",
    "## Phong cách chủ đạo: Luminous Warm Editorial Illustration (Minh họa báo chí cao cấp, ánh sáng trong trẻo rực rỡ, 100% không gian vật lý đời thực, triệt tiêu hoàn toàn siêu thực và màu đen u ám)",
    "",
    "### 🎨 Hệ màu 60-30-10 (Tuyệt Đối Ấm Áp — Chống Lạnh Lẽo):",
    "- **60% Tông màu nền chủ đạo:** Warm Ivory Cream (`#FAF7EE`), Warm Caribbean & African Dawn (`#FFFBEB`), Warm Alluvium Clay (`#F3E5AB`). Tuyệt đối không dùng nền xám lạnh, xanh cyan buốt giá hay đen kịt.",
    "- **30% Đường nét & Chủ thể:** Ripe Golden Amber (`#F59E0B`), Terracotta Red Soil (`#EA580C`), Resilient Seedling Green (`#10B981`), Fraternal Red & Blue Ribbons (`#DC2626`).",
    "- **10% Điểm nhấn dẫn mắt:** Luminous Warm Golden Sunrise Rays (`#D97706`), Warm Spotlight in Friendship Galleries, Glowing Golden Amber Data Badges.",
    "",
    "---",
    "",
    "### 🛡️ Quy Tắc Kiểm Soát Tuyệt Đối:",
    "1. **Scene ID chuẩn theo chương:** `CH09_SC001` đến `CH09_SC042` (Khớp 100% với phân rã thời gian tự nhiên).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Đầm lầy Sierra Leone, thung lũng Zambezi (Mozambique), đồng bằng Senegal, Quảng trường Cách mạng La Habana, cánh đồng Pinar del Río & Granma (Cuba), ruộng giống Nam Định, Bảo tàng Lịch sử Quốc gia.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc đúng 9/42 phân cảnh (21.4%) có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. 33 phân cảnh còn lại để `[TEXT OVERLAY]: Không`.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Ảnh Tham Chiếu Nhân Vật / Địa Danh:**",
    "   - `@gs_vo_tong_xuan.jpg` sử dụng tại `CH09_SC012`, `CH09_SC013`, `CH09_SC014`, `CH09_SC015` (Cố Giáo sư Võ Tòng Xuân tại Sierra Leone).",
    "   - `@cuba_president_diaz_canel.jpg` sử dụng tại `CH09_SC020`, `CH09_SC021`, `CH09_SC026`, `CH09_SC027` (Chủ tịch Miguel Díaz-Canel và Fidel Castro).",
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

# Save chapter_09_visual.md
with open("episodes/vu-khi-gao-viet-nam/chapter_09_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_09_visual.md ({len(scenes_data)} scenes)")

# Generate prompts_chapter_09.txt
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

with open("episodes/vu-khi-gao-viet-nam/prompts_chapter_09.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompt_lines).strip() + "\n")

print(f"✅ Generated prompts_chapter_09.txt ({len(scenes_data)} scenes)")
