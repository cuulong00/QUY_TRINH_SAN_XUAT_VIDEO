"""
Script to generate both chapter_08_visual.md and prompts_chapter_08.txt
for Episode 'Vũ Khí Lúa Gạo Việt Nam' - Chapter 08.
Strictly adheres to:
- Flow Batch Studio syntax
- Warm Luminous Editorial Palette (#FAF7EE, #F59E0B, #EA580C)
- Selective Lower-Left 25% Rule (~20% text overlay)
- Canonical references: @cong_cai_lon.jpg, @thutuong_chinh.jpg, @bo_truong_le_minh_hoan.jpg
- Steady camera and static text preservation in video prompts
"""

import re
import json

scenes_data = [
    {
        "id": "CH08_SC001",
        "dur": "6.04s",
        "words": 23,
        "text": "Đứng trước bờ vực của những giới hạn sinh thái, Việt Nam đã không lựa chọn con đường đối đầu với tự nhiên.",
        "anatomy": {
            "tier1": "Toàn cảnh ngã ba sông nước miền Tây lúc rạng đông với dòng nước lững lờ trôi giữa hai bờ kênh xanh mát.",
            "tier2": "Bàn làm việc của nhà hoạch định chiến lược quốc gia với tài liệu tổng kết những giới hạn sinh thái của mô hình cũ.",
            "tier3": "Cú máy bay chậm trên cao (slow aerial glide) bao quát vùng sông nước rạng đông (Slow aerial glide over serene delta waterways at dawn)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a peaceful sunrise aerial panorama over the sprawling waterways of the Mekong Delta, where morning mist rises gently over tranquil channels, symbolizing the turning away from environmental confrontation",
        "setting": "the vast agricultural river plains of southern Vietnam under warm golden dawn light",
        "motion": "Slow aerial glide across the tranquil morning river channels bathed in golden sunrise"
    },
    {
        "id": "CH08_SC002",
        "dur": "6.82s",
        "words": 26,
        "text": "Bước ngoặt lịch sử mở ra từ Nghị quyết một trăm hai mươi của Chính phủ về phát triển bền vững đồng bằng sông Cửu Long.",
        "anatomy": {
            "tier1": "Phòng họp Diên Hồng hoặc Trung tâm Hội nghị Quốc tế nơi diễn ra Hội nghị toàn quốc về phát triển bền vững ĐBSCL.",
            "tier2": "Bản Nghị quyết số 120/NQ-CP của Chính phủ được ban hành trang trọng, đánh dấu bước ngoặt chiến lược lịch sử cho toàn vùng châu thổ.",
            "tier3": "Cú máy tĩnh trực diện vào văn bản Nghị quyết 120/NQ-CP của Chính phủ (Steady shot on Resolution 120 Government decree) cùng text overlay góc trái dưới."
        },
        "overlay": "NGHỊ QUYẾT 120/NQ-CP: PHÁT TRIỂN THUẬN THIÊN",
        "ref": None,
        "subj": "the official leather-bound government policy document of Government Resolution 120 on Sustainable and Climate-Resilient Development of the Mekong Delta open on a mahogany conference table under warm chandelier light",
        "setting": "a grand government plenary hall in Hanoi under warm dignified indoor lighting",
        "motion": "Steady camera shot framing the historic Resolution 120 state policy document"
    },
    {
        "id": "CH08_SC003",
        "dur": "5.25s",
        "words": 20,
        "text": "Văn bản này đã khai sinh ra một triết lý hành động mang tính cách mạng: phát triển thuận thiên.",
        "anatomy": {
            "tier1": "Bức tranh sơn mài hoặc đồ họa nghệ thuật tôn vinh triết lý 'Thuận thiên' (Nature-based living) với hình tượng con người hòa hợp cùng sông nước.",
            "tier2": "Dòng chữ triết lý phát triển thuận thiên tỏa sáng rực rỡ, khẳng định tôn trọng quy luật tự nhiên là chìa khóa sinh tồn.",
            "tier3": "Cú máy nâng chậm theo bức tranh nghệ thuật triết lý thuận thiên (Slow upward tilt along Nature-Based philosophy mural)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an evocative artistic editorial mural illustrating the revolutionary concept of 'Thuan Thien' (Nature-Based Adaptation), showing harmonious co-existence between human agriculture and cyclical river tides",
        "setting": "a national cultural and policy gallery under warm golden spotlighting",
        "motion": "Slow upward tilt revealing the inspiring nature-based development philosophy artwork"
    },
    {
        "id": "CH08_SC004",
        "dur": "4.99s",
        "words": 19,
        "text": "Thay vì coi nước mặn là hiểm họa cần tiêu diệt, Nhà nước chính thức công nhận nước ngọt",
        "anatomy": {
            "tier1": "Sơ đồ thủy văn mới của châu thổ hiển thị ba nguồn tài nguyên nước bình đẳng và hòa quyện.",
            "tier2": "Hình ảnh giọt nước ngọt phù sa trong lành bên cạnh dòng nước mặn biển cả, xóa bỏ định kiến nước mặn là kẻ thù.",
            "tier3": "Cú máy trượt ngang qua sơ đồ tài nguyên nước (Horizontal tracking shot across water resource matrix)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a conceptual balance illustration placing a crystal freshwater droplet beside an azure marine saltwater droplet, officially recognizing both as equally valuable natural economic endowments",
        "setting": "a hydrological science exhibition hall in warm amber and ivory tones",
        "motion": "Smooth horizontal tracking shot across the dual water endowment display"
    },
    {
        "id": "CH08_SC005",
        "dur": "3.41s",
        "words": 13,
        "text": "nước lợ và nước mặn đều là tài nguyên kinh tế vô giá.",
        "anatomy": {
            "tier1": "Bản đồ phân vùng 3 hệ sinh thái nước ngọt, nước lợ và nước mặn của toàn bộ bán đảo Cà Mau và ĐBSCL.",
            "tier2": "Ba sắc màu hài hòa: Nước ngọt màu vàng phù sa, nước lợ màu xanh lục và nước mặn màu lam biển, tạo nên giá trị kinh tế đa tầng.",
            "tier3": "Cú máy đẩy chậm vào bản đồ ba vùng sinh thái nước (Slow push-in on tri-zone water economy map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an analytical regional map illustrating the tri-zone economic division: fresh water, brackish water, and saline water zones harmoniously mapped across the southern delta",
        "setting": "a regional development planning office under warm ambient desk light",
        "motion": "Slow push-in shot toward the tri-zone ecological resource mapping"
    },
    {
        "id": "CH08_SC006",
        "dur": "4.72s",
        "words": 18,
        "text": "Tư duy ngọt hóa cưỡng bức được thay thế bằng quy hoạch ba vùng sinh thái rõ rệt.",
        "anatomy": {
            "tier1": "Phòng họp quy hoạch tích hợp ĐBSCL thời kỳ 2021 - 2030 tầm nhìn 2050.",
            "tier2": "Các nhà khoa học và lãnh đạo chính phủ cùng rà soát quy hoạch ba vùng sinh thái: Vùng ngọt thượng lưu, vùng lợ chuyển tiếp và vùng mặn ven biển.",
            "tier3": "Cú máy trượt ngang qua bàn họp quy hoạch sinh thái ba vùng (Horizontal tracking shot past tri-zone ecological planning table)."
        },
        "overlay": None,
        "ref": None,
        "subj": "senior government spatial planners and environmental scientists reviewing the Master Spatial Plan for the Mekong Delta, replacing rigid forced-freshening with three organic agro-ecological zones",
        "setting": "a state spatial planning chamber in warm ivory cream and amber tones",
        "motion": "Slow horizontal tracking shot past planners reviewing the integrated spatial masterplan"
    },
    {
        "id": "CH08_SC007",
        "dur": "6.04s",
        "words": 23,
        "text": "Mô hình luân canh lúa tôm ra đời, biến mảnh đất từng xảy ra xung đột thành không gian cộng sinh trù phú.",
        "anatomy": {
            "tier1": "Cánh đồng luân canh lúa - tôm kiểu mẫu tại Bạc Liêu hoặc Cà Mau trong nắng sớm rạng rỡ.",
            "tier2": "Mùa mưa trồng lúa sạch hữu cơ hút bớt độc chất phèn mặn; Mùa khô lấy nước mặn vào nuôi tôm sú tự nhiên, tạo nên vòng tròn cộng sinh hoàn hảo.",
            "tier3": "Cú máy nâng chậm từ mặt nước vuông tôm lên ruộng lúa trổ bông vàng óng (Slow tilt-up from shrimp water to golden rice stalks)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a prosperous integrated rice-shrimp rotational farm in Bac Lieu where clean organic rice thrives in the wet season followed by organic tiger shrimp aquaculture in the dry season, in harmonious symbiotic balance",
        "setting": "a sunlit agro-ecological farm in southern Vietnam under glorious morning sun",
        "motion": "Slow tilt-up from the clean water canal with swimming shrimp to the golden rice stalks above"
    },
    {
        "id": "CH08_SC008",
        "dur": "5.77s",
        "words": 22,
        "text": "Mỗi héc ta lúa tôm mang lại nguồn thu nhập từ tám mươi đến một trăm hai mươi triệu đồng mỗi năm",
        "anatomy": {
            "tier1": "Sân nhà khang trang của hộ nông dân làm mô hình lúa - tôm tại Kiên Giang hoặc Cà Mau.",
            "tier2": "Gia đình nông dân phấn khởi thu hoạch cả tôm sú thương phẩm to tròn và những bao lúa sạch chất lượng cao.",
            "tier3": "Cú máy tĩnh trực diện vào con số thu nhập 80 - 120 triệu đồng/ha/năm (Steady shot on 80 - 120M VND/ha revenue landmark) cùng text overlay góc trái dưới."
        },
        "overlay": "LÚA - TÔM: 80 - 120 TRIỆU ĐỒNG/HA",
        "ref": None,
        "subj": "a prosperous local farming family in conical hats sorting large fresh tiger shrimp into baskets beside freshly harvested bags of organic rice, radiating joy and economic success",
        "setting": "a sunny farmhouse courtyard beside a lush rice-shrimp field in warm morning light",
        "motion": "Steady camera shot framing the farmer family and their abundant rice and shrimp harvest"
    },
    {
        "id": "CH08_SC009",
        "dur": "2.62s",
        "words": 10,
        "text": "cao gấp ba lần so với độc canh cây lúa.",
        "anatomy": {
            "tier1": "Biểu đồ so sánh hiệu quả kinh tế cột đôi: Thu nhập mô hình lúa - tôm cao gấp 3 lần so với độc canh lúa 3 vụ truyền thống.",
            "tier2": "Mô hình không chỉ giúp bà con làm giàu bền vững mà còn bảo vệ đất đai không bị kiệt quệ dinh dưỡng.",
            "tier3": "Cú máy trượt ngang so sánh hai cột thu nhập nông nghiệp (Horizontal tracking shot comparing dual income pillars)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a comparative economic bar chart displaying the 3x net income multiplier of the organic rice-shrimp model towering over traditional three-crop rice monoculture",
        "setting": "an agricultural extension office in warm amber tones",
        "motion": "Smooth horizontal tracking shot across the 3x revenue superiority comparison"
    },
    {
        "id": "CH08_SC010",
        "dur": "4.2s",
        "words": 16,
        "text": "Hiện thân rõ nét nhất cho triết lý thích ứng này là siêu công trình thủy",
        "anatomy": {
            "tier1": "Toàn cảnh cụm cống Cái Lớn nhìn từ trên cao vắt ngang qua dòng sông Cái Lớn mênh mông sóng nước.",
            "tier2": "Kiến trúc hiện đại với các trụ tháp bê tông trắng và các dầm cầu giao thông kết nối đôi bờ Kiên Giang.",
            "tier3": "Cú máy bay chậm trên cao (slow aerial glide) bao quát toàn cảnh cống Cái Lớn (Slow aerial glide over Cai Lon sluice gate complex)."
        },
        "overlay": None,
        "ref": "cong_cai_lon.jpg",
        "subj": "an impressive high-angle panoramic view of the monumental Cai Lon hydraulic sluice gate complex spanning the wide Cai Lon river with its rhythmic concrete pylons and roadway deck",
        "setting": "the vast waters of the Cai Lon river in Kien Giang under bright morning sunshine",
        "motion": "Slow aerial glide across the imposing architectural superstructure of the Cai Lon sluice"
    },
    {
        "id": "CH08_SC011",
        "dur": "4.46s",
        "words": 17,
        "text": "lợi Cái Lớn Cái Bé với tổng vốn đầu tư hơn ba nghìn ba trăm tỷ đồng.",
        "anatomy": {
            "tier1": "Biển tên công trình thủy lợi Cái Lớn - Cái Bé bằng đá hoa cương sáng bóng với quốc huy Việt Nam.",
            "tier2": "Thông số dự án khẳng định quy mô siêu công trình kiểm soát nguồn nước lớn nhất Đông Nam Á với tổng mức đầu tư hơn 3.300 tỷ đồng.",
            "tier3": "Cú máy tĩnh trực diện vào biển tên Siêu Thủy Lợi Cái Lớn - Cái Bé (Steady shot on Cai Lon - Cai Be Landmark) cùng text overlay góc trái dưới."
        },
        "overlay": "SIÊU THỦY LỢI CÁI LỚN - CÁI BÉ",
        "ref": "cong_cai_lon.jpg",
        "subj": "the polished stone commemorative landmark plaque of the Cai Lon - Cai Be Water Resources Project surrounded by lush landscaping and the grand sluice gates in the background",
        "setting": "the operational administration plaza of the Cai Lon project in warm golden morning light",
        "motion": "Steady camera shot framing the official project monument and background sluice gates"
    },
    {
        "id": "CH08_SC012",
        "dur": "2.1s",
        "words": 8,
        "text": "Khác với đê bao ngăn mặn cứng nhắc",
        "anatomy": {
            "tier1": "Hình ảnh so sánh: Một bên là bờ đê bê tông cũ thô ráp; Một bên là cụm cống công nghệ cao đóng mở linh hoạt.",
            "tier2": "Sự khác biệt mang tính cách mạng giữa tư duy chặn nước thụ động và tư duy điều tiết nước chủ động, thông minh.",
            "tier3": "Cú máy trượt ngang qua sự tương phản công nghệ điều tiết nước (Horizontal tracking shot past technological contrast)."
        },
        "overlay": None,
        "ref": "cong_cai_lon.jpg",
        "subj": "a conceptual juxtaposition contrasting rigid cracked concrete dykes from past decades with the sleek, dynamic engineered steel radial gates of the modern sluice",
        "setting": "a hydraulic engineering exhibit in warm ambient lighting",
        "motion": "Slow horizontal tracking shot showing the technological leap from passive to active water control"
    },
    {
        "id": "CH08_SC013",
        "dur": "5.25s",
        "words": 20,
        "text": "cụm mười một cửa van thép khổng lồ được điều khiển tự động bằng hệ thống cảm biến hiện đại.",
        "anatomy": {
            "tier1": "Dãy 11 cửa van cung bằng thép không gỉ khổng lồ nặng hàng trăm tấn tại cống Cái Lớn.",
            "tier2": "Xy-lanh thủy lực khổng lồ vận hành êm ái, kết nối trực tiếp với trung tâm điều khiển tự động hóa SCADA bằng cảm biến đo mặn.",
            "tier3": "Cú máy nâng chậm theo thân cửa van thép khổng lồ (Slow upward tilt along massive steel radial gate)."
        },
        "overlay": None,
        "ref": "cong_cai_lon.jpg",
        "subj": "a dramatic close-up view of the 11 massive curved steel radial gates and powerful hydraulic pistons of the Cai Lon sluice operating automatically in clean sparkling river waters",
        "setting": "the active river barrage of Cai Lon Kien Giang under warm midday sun",
        "motion": "Slow upward tilt along the massive curved steel gate rising smoothly above the water"
    },
    {
        "id": "CH08_SC014",
        "dur": "6.56s",
        "words": 25,
        "text": "Vào mùa khô hạn gay gắt, các cửa van hạ xuống để ngăn mặn và bảo vệ gần bốn trăm nghìn héc ta đồng ruộng.",
        "anatomy": {
            "tier1": "Cửa van cống Cái Lớn từ từ hạ xuống đáy sông ngăn chặn dòng nước biển xâm nhập trong mùa khô hạn.",
            "tier2": "Vùng ngọt hóa bên trong được bảo vệ an toàn tuyệt đối, phủ xanh gần 400.000 héc ta cánh đồng lúa và vườn cây ăn trái của 5 tỉnh.",
            "tier3": "Cú máy tĩnh trực diện vào cống Cái Lớn hạ van bảo vệ gần 400.000 ha (Steady shot on Cai Lon gate lowering to protect 400,000 ha) cùng text overlay góc trái dưới."
        },
        "overlay": "BẢO VỆ GẦN 400.000 HA ĐỒNG RUỘNG",
        "ref": "cong_cai_lon.jpg",
        "subj": "the massive steel radial gates descending smoothly into the river channel to block saline intrusion while upstream endless green rice paddies and orchards remain safely nourished",
        "setting": "the Cai Lon river sluice during the dry season under warm clear skies",
        "motion": "Steady camera shot framing the lowered gate barriers and the vast protected agricultural hinterland"
    },
    {
        "id": "CH08_SC015",
        "dur": "6.3s",
        "words": 24,
        "text": "Thế nhưng khi thủy triều rút, hệ thống lại mở hé để đón dòng nước lợ phục vụ các vùng nuôi tôm ven biển.",
        "anatomy": {
            "tier1": "Cửa van cống mở hé nhấc khỏi mặt nước, tạo luồng nước lợ tự nhiên lưu thông êm ả qua thân cống.",
            "tier2": "Dòng nước lợ giàu khoáng chất từ từ chảy vào hệ thống kênh dẫn của các vùng nuôi tôm ven biển, đáp ứng trọn vẹn sinh kế của cả hai giới nông dân.",
            "tier3": "Cú máy trượt ngang theo dòng nước lợ êm đềm chảy qua cửa cống mở hé (Horizontal tracking shot along brackish water flowing through partially opened gate)."
        },
        "overlay": None,
        "ref": "cong_cai_lon.jpg",
        "subj": "the steel radial gates slightly elevated above the river surface allowing a controlled volume of fresh and brackish water to flow through to replenish downstream coastal shrimp ponds",
        "setting": "the Cai Lon sluice at high tide in warm late-afternoon sunlight",
        "motion": "Slow horizontal tracking shot following the swirling brackish water passing under the gate"
    },
    {
        "id": "CH08_SC016",
        "dur": "2.36s",
        "words": 9,
        "text": "Không chỉ tái cấu trúc không gian sinh thái",
        "anatomy": {
            "tier1": "Bản đồ sinh thái đồng bằng sông Cửu Long tỏa sáng hài hòa giữa các gam màu xanh lá, vàng óng và lam biển.",
            "tier2": "Nhà lãnh đạo chính phủ và các chuyên gia nông nghiệp chuẩn bị công bố bước đột phá mang tầm vóc toàn cầu.",
            "tier3": "Cú máy nâng chậm từ bản đồ sinh thái lên chân trời phát triển mới (Slow upward tilt from ecological map toward new horizon)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a visionary digital map of the ecologically balanced Mekong Delta glowing with integrated green and blue agro-zones under warm study lighting",
        "setting": "a high-level policy strategy room in warm ambient light",
        "motion": "Slow upward tilt from the harmonized map toward the bright window view"
    },
    {
        "id": "CH08_SC017",
        "dur": "4.72s",
        "words": 18,
        "text": "Việt Nam còn tạo nên một bước đột phá chấn động trên bản đồ nông nghiệp thế giới.",
        "anatomy": {
            "tier1": "Quả địa cầu quay chậm với hình ảnh Việt Nam nổi bật như ngọn cờ đầu của nền nông nghiệp xanh bền vững.",
            "tier2": "Hội nghị thượng đỉnh khí hậu COP28 tại Dubai nơi thế giới hướng sự chú ý về cam kết tiên phong của Việt Nam.",
            "tier3": "Cú máy đẩy chậm vào quả địa cầu và biểu tượng nông nghiệp xanh Việt Nam (Slow push-in on global green agriculture emblem)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a global stage presentation at the COP28 climate summit where international delegates witness Vietnam pioneering green transformation in wet rice cultivation",
        "setting": "an international climate summit plenary hall in warm architectural lighting",
        "motion": "Slow push-in shot toward the international presentation screen displaying Vietnam green commitment"
    },
    {
        "id": "CH08_SC018",
        "dur": "3.15s",
        "words": 12,
        "text": "Theo Quyết định một nghìn bốn trăm chín mươi của Thủ tướng",
        "anatomy": {
            "tier1": "Phòng khánh tiết Văn phòng Chính phủ tại Hà Nội trang trọng với quốc kỳ và huy hiệu.",
            "tier2": "Thủ tướng Chính phủ Phạm Minh Chính ký ban hành Quyết định số 1490/QĐ-TTg phê duyệt Đề án 1 triệu héc ta lúa.",
            "tier3": "Cú máy đẩy chậm vào Thủ tướng Phạm Minh Chính ký quyết định lịch sử (Slow push-in on Prime Minister Pham Minh Chinh signing Decision 1490)."
        },
        "overlay": None,
        "ref": "thutuong_chinh.jpg",
        "subj": "Vietnamese Prime Minister Pham Minh Chinh seated formally at an executive desk in the Government Headquarters signing the landmark Decision 1490/QD-TTg beside official advisors",
        "setting": "the state conference hall of the Government Headquarters in Hanoi under warm dignified chandelier lighting",
        "motion": "Slow push-in shot toward Prime Minister Pham Minh Chinh signing the historic decree"
    },
    {
        "id": "CH08_SC019",
        "dur": "4.72s",
        "words": 18,
        "text": "Đề án một triệu héc ta lúa chất lượng cao và phát thải thấp chính thức ra đời.",
        "anatomy": {
            "tier1": "Lễ phát động Đề án 1 triệu ha lúa chất lượng cao và phát thải thấp tại Hậu Giang hoặc Cần Thơ.",
            "tier2": "Biểu tượng đề án với bông lúa vàng bao quanh giọt nước xanh và mầm sống giảm phát thải tỏa sáng rực rỡ.",
            "tier3": "Cú máy tĩnh trực diện vào Lễ phát động Đề án 1 triệu ha lúa phát thải thấp (Steady shot on 1-Million-Ha Low-Emission Rice launch) cùng text overlay góc trái dưới."
        },
        "overlay": "ĐỀ ÁN 1 TRIỆU HA LÚA PHÁT THẢI THẤP",
        "ref": "thutuong_chinh.jpg",
        "subj": "the grand launch ceremony of the National Project for 1 Million Hectares of High-Quality and Low-Emission Rice in the Mekong Delta with official green banners and ceremonial displays",
        "setting": "a grand agricultural convention hall in Can Tho under warm festive stage lighting",
        "motion": "Steady camera shot framing the 1-Million-Hectare Low-Emission Rice project banner"
    },
    {
        "id": "CH08_SC020",
        "dur": "3.41s",
        "words": 13,
        "text": "Đây là chương trình quốc gia đầu tiên trên toàn cầu đưa quy",
        "anatomy": {
            "tier1": "Cánh đồng lúa thí điểm tại Cần Thơ với các chuyên gia Ngân hàng Thế giới và Bộ Nông nghiệp trực tiếp kiểm tra.",
            "tier2": "Bộ trưởng Bộ Nông nghiệp Lê Minh Hoan trao đổi thân tình cùng bà con nông dân và chuyên gia quốc tế ngay trên bờ ruộng.",
            "tier3": "Cú máy trượt ngang qua cánh đồng thí điểm lúa phát thải thấp (Horizontal tracking shot past pilot low-emission paddy)."
        },
        "overlay": None,
        "ref": "bo_truong_le_minh_hoan.jpg",
        "subj": "Minister of Agriculture Le Minh Hoan in casual field shirt conversing warmly with local farmers and World Bank agronomy specialists on an earthen canal bank",
        "setting": "a pilot sustainable rice demonstration farm in Can Tho under bright warm morning sun",
        "motion": "Slow horizontal tracking shot past Minister Le Minh Hoan talking with farmers on the ridge"
    },
    {
        "id": "CH08_SC021",
        "dur": "3.67s",
        "words": 14,
        "text": "trình sản xuất lúa nước tiến thẳng tới mục tiêu giảm phát thải ròng.",
        "anatomy": {
            "tier1": "Thửa ruộng mẫu với các thiết bị đo phát thải khí nhà kính (metan và N2O) bằng buồng kín tự động.",
            "tier2": "Bộ trưởng Lê Minh Hoan chỉ tay về phía cánh đồng xanh tốt, biểu tượng cho lời cam kết Net Zero nông nghiệp của Việt Nam.",
            "tier3": "Cú máy nâng chậm từ buồng đo phát thải lên Bộ trưởng và cánh đồng bao la (Slow upward tilt from emission sensor to Minister and fields)."
        },
        "overlay": None,
        "ref": "bo_truong_le_minh_hoan.jpg",
        "subj": "Minister of Agriculture Le Minh Hoan standing beside automated solar-powered greenhouse gas flux chambers measuring methane reduction in thriving green paddies",
        "setting": "an advanced agronomic climate research station in the delta under warm sunny skies",
        "motion": "Slow upward tilt from scientific gas sensors toward the Minister looking over the expansive green paddies"
    },
    {
        "id": "CH08_SC022",
        "dur": "5.77s",
        "words": 22,
        "text": "Quy trình tưới ngập khô xen kẽ giúp tiết kiệm nước ngọt và giảm trên mười phần trăm lượng khí nhà kính.",
        "anatomy": {
            "tier1": "Ống đo mực nước nông lộ phơi (Alternate Wetting and Drying - AWD) cắm trong ruộng lúa với vạch chia centimet rõ ràng.",
            "tier2": "Mặt ruộng khô ráo nứt chân chim nhẹ, rễ lúa ăn sâu hút dinh dưỡng, tiết kiệm 30% nước tưới và cắt giảm mạnh khí metan.",
            "tier3": "Cú máy tĩnh trực diện vào quy trình tưới ngập khô xen kẽ AWD (Steady shot on Alternate Wetting and Drying AWD technology) cùng text overlay góc trái dưới."
        },
        "overlay": "TƯỚI NGẬP KHÔ XEN KẼ (AWD)",
        "ref": None,
        "subj": "a demonstration of Alternate Wetting and Drying (AWD) water management with a perforated field water pipe showing water level beneath the soil surface in healthy aerated rice roots",
        "setting": "a sustainable rice paddy plot in southern Vietnam under warm morning sunshine",
        "motion": "Steady camera shot framing the perforated AWD monitoring pipe and healthy soil"
    },
    {
        "id": "CH08_SC023",
        "dur": "1.57s",
        "words": 6,
        "text": "Lần đầu tiên trong lịch sử",
        "anatomy": {
            "tier1": "Khuôn viên hợp tác xã nông nghiệp kiểu mới với bảng niêm yết chứng chỉ phát thải xanh quốc tế.",
            "tier2": "Người nông dân cầm chứng chỉ tín chỉ carbon đầu tiên, ánh mắt ngập tràn niềm tự hào.",
            "tier3": "Cú máy đẩy nhanh vào chứng chỉ tín chỉ carbon trên tay người nông dân (Dynamic push-in on carbon credit certificate)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a modern Vietnamese cooperative farmer proudly holding an embossed international green carbon offset certificate in a sunlit cooperative hall",
        "setting": "a modern agricultural cooperative office in warm morning light",
        "motion": "Dynamic push-in shot toward the official carbon offset certificate"
    },
    {
        "id": "CH08_SC024",
        "dur": "6.04s",
        "words": 23,
        "text": "người nông dân Việt Nam không chỉ bán hạt gạo mà còn có thêm nguồn thu nhập từ việc bán tín chỉ carbon.",
        "anatomy": {
            "tier1": "Sàn giao dịch tín chỉ carbon nông nghiệp quốc tế với giao dịch thanh toán đầu tiên cho các hợp tác xã miền Tây.",
            "tier2": "Dòng tiền từ thị trường carbon thế giới đổ về tận tay bà con nông dân sản xuất lúa phát thải thấp.",
            "tier3": "Cú máy tĩnh trực diện vào doanh thu bán tín chỉ carbon nông nghiệp (Steady shot on Agricultural Carbon Credit Revenue display) cùng text overlay góc trái dưới."
        },
        "overlay": "BÁN TÍN CHỈ CARBON NÔNG NGHIỆP",
        "ref": None,
        "subj": "a modern agricultural trade terminal interface displaying verified carbon credit sales disbursements credited directly to Vietnamese farmer cooperative bank accounts",
        "setting": "a green fintech and agricultural banking room in warm amber tones",
        "motion": "Steady camera shot framing the agricultural carbon credit revenue transfer interface"
    },
    {
        "id": "CH08_SC025",
        "dur": "2.62s",
        "words": 10,
        "text": "Cùng với bước nhảy vọt về công nghệ sinh thái",
        "anatomy": {
            "tier1": "Cửa biển Trần Đề (Sóc Trăng) nơi dòng sông Hậu hòa vào biển Đông trong ánh ban mai rực rỡ.",
            "tier2": "Bản vẽ phối cảnh đại cảng nước sâu Trần Đề trải rộng trên bàn làm việc của các kỹ sư hàng hải.",
            "tier3": "Cú máy bay chậm từ cửa biển Trần Đề hướng ra biển khơi (Slow aerial glide from Tran De estuary toward open ocean)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an expansive aerial view of the Tran De estuary in Soc Trang where the Hau River meets the East Sea under a glorious golden morning sky",
        "setting": "the vast coastal waters of Tran De Soc Trang in early morning light",
        "motion": "Slow aerial glide from the coastal river mouth toward the open sea"
    },
    {
        "id": "CH08_SC026",
        "dur": "4.72s",
        "words": 18,
        "text": "nút thắt hạ tầng logistics hàng chục năm qua cũng tìm thấy lời giải mang tính thế kỷ.",
        "anatomy": {
            "tier1": "Phối cảnh 3D siêu cảng nước sâu cửa ngõ Trần Đề với cầu dẫn vượt biển dài hàng chục cây số.",
            "tier2": "Hệ thống bến cảng ngoài khơi đón những con tàu mẹ viễn dương khổng lồ, phá vỡ thế cô lập logistics của miền Tây.",
            "tier3": "Cú máy nâng chậm theo thân cầu dẫn vượt biển hướng ra bến cảng ngoài khơi (Slow upward tilt along offshore port access bridge)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a breathtaking 3D masterplan architectural rendering of the Tran De deep-sea offshore gateway port with an offshore bridge spanning toward deep water berths",
        "setting": "a maritime infrastructure planning studio under warm dramatic lighting",
        "motion": "Slow upward tilt along the offshore access trestle toward the deep-water container island"
    },
    {
        "id": "CH08_SC027",
        "dur": "6.04s",
        "words": 23,
        "text": "Đó là quy hoạch đại cảng nước sâu cửa ngõ Trần Đề với quy mô đầu tư khoảng năm mươi nghìn tỷ đồng.",
        "anatomy": {
            "tier1": "Mô hình quy hoạch tổng thể Đại cảng nước sâu Trần Đề với tổng vốn đầu tư khoảng 50.000 tỷ đồng.",
            "tier2": "Khu bến cảng ngoài khơi tiếp nhận tàu mẹ container và hàng rời quy mô lớn nhất vùng đồng bằng sông Cửu Long.",
            "tier3": "Cú máy tĩnh trực diện vào quy hoạch Đại cảng Trần Đề 50.000 tỷ đồng (Steady shot on Tran De Deep-Sea Port ~50,000B VND plan) cùng text overlay góc trái dưới."
        },
        "overlay": "ĐẠI CẢNG NƯỚC SÂU TRẦN ĐỀ: ~50.000 TỶ",
        "ref": None,
        "subj": "an impressive scale model and blueprint of the Tran De deep-sea port master plan highlighting the 50,000 billion VND investment scale and strategic offshore berths",
        "setting": "a national maritime transport exhibition hall under warm ambient spotlights",
        "motion": "Steady camera shot framing the architectural scale model of the Tran De gateway port"
    },
    {
        "id": "CH08_SC028",
        "dur": "3.67s",
        "words": 14,
        "text": "Luồng hàng hải tự nhiên sâu thẳm sẽ cho phép đón những con tàu",
        "anatomy": {
            "tier1": "Mặt cắt độ sâu luồng hàng hải Trần Đề ngoài khơi đạt độ sâu tự nhiên từ âm 14 đến âm 16 mét nước.",
            "tier2": "Luồng tàu tự nhiên sâu thẳm không bị bồi lắng, cho phép các siêu tàu vận tải biển quốc tế ra vào tự do.",
            "tier3": "Cú máy trượt ngang qua biểu đồ độ sâu luồng hàng hải tự nhiên (Horizontal tracking shot past deep bathymetric profile)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a nautical hydrographic chart showing natural deep-water channels reaching 15 meters draught offshore at Tran De, free from estuarine siltation",
        "setting": "a port authority navigation room in warm ambient lighting",
        "motion": "Slow horizontal tracking shot across the offshore deep-water sounding charts"
    },
    {
        "id": "CH08_SC029",
        "dur": "3.67s",
        "words": 14,
        "text": "mẹ quốc tế có tải trọng lên tới một trăm nghìn tấn cập bến.",
        "anatomy": {
            "tier1": "Siêu tàu mẹ container viễn dương tải trọng 100.000 tấn cập cầu cảng ngoài khơi Trần Đề.",
            "tier2": "Cần cẩu bờ STS bốc dỡ các container gạo thơm Việt Nam trực tiếp lên tàu mẹ viễn dương dưới ánh nắng rực rỡ.",
            "tier3": "Cú máy góc rộng quay siêu tàu mẹ cập bến cảng nước sâu (Wide cinematic shot of 100,000 DWT mother vessel moored at quayside)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a magnificent ultra-large international 100,000 DWT container mother ship docked alongside the offshore Tran De berths with giant ship-to-shore gantry cranes loading cargo",
        "setting": "the open-sea deep-water terminal at golden sunrise",
        "motion": "Wide cinematic tracking shot following the sleek hull of the 100,000-ton mother ship"
    },
    {
        "id": "CH08_SC030",
        "dur": "3.67s",
        "words": 14,
        "text": "Hạt gạo miền Tây sẽ được đóng container và bốc thẳng sang bờ bên",
        "anatomy": {
            "tier1": "Băng chuyền tự động đóng thùng container gạo chất lượng cao tại bến cảng Trần Đề.",
            "tier2": "Các thùng container mang thương hiệu gạo Việt Nam được niêm phong chì hải quan, sẵn sàng thẳng tiến ra hải trình xuyên đại dương.",
            "tier3": "Cú máy trượt ngang theo các thùng container gạo chuẩn bị xuất khẩu (Horizontal tracking shot past export rice containers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "clean branded shipping containers filled with high-grade Vietnamese rice being sealed and hoisted directly onto trans-oceanic container stacks",
        "setting": "a busy automated container staging yard at Tran De port in warm daylight",
        "motion": "Slow horizontal tracking shot past neatly stacked export rice containers"
    },
    {
        "id": "CH08_SC031",
        "dur": "3.67s",
        "words": 14,
        "text": "kia đại dương mà không cần trung chuyển qua Thành phố Hồ Chí Minh.",
        "anatomy": {
            "tier1": "Hải trình xuất khẩu trực tiếp: Tuyến hàng hải vẽ đường thẳng từ cảng Trần Đề sang châu Âu và Bắc Mỹ.",
            "tier2": "Bỏ qua hoàn toàn chặng đường trung chuyển 200 km đường sông lên TP.HCM, tiết kiệm hàng tuần lễ thời gian logistics.",
            "tier3": "Cú máy nâng chậm theo hải trình đường thẳng vượt đại dương (Slow upward tilt along direct trans-oceanic route)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a global shipping route map showing direct maritime transit lines connecting the Tran De deep-sea hub straight to North America and Europe, completely bypassing domestic river detours",
        "setting": "a global logistics intelligence command console in warm amber tones",
        "motion": "Slow upward tilt following the direct trans-oceanic shipping lane"
    },
    {
        "id": "CH08_SC032",
        "dur": "3.41s",
        "words": 13,
        "text": "Chi phí vận tải sẽ được cắt giảm tới ba mươi phần trăm",
        "anatomy": {
            "tier1": "Bảng phân tích tài chính logistics so sánh chi phí xuất khẩu qua cảng Trần Đề so với tuyến trung chuyển cũ.",
            "tier2": "Con số cắt giảm tới 30% chi phí vận tải hiển thị rõ ràng, giúp nông sản Việt Nam tăng mạnh năng lực cạnh tranh quốc tế.",
            "tier3": "Cú máy tĩnh trực diện vào con số cắt giảm 30% chi phí vận tải (Steady shot on 30% Logistics Cost Reduction metric) cùng text overlay góc trái dưới."
        },
        "overlay": "CẮT GIẢM 30% CHI PHÍ LOGISTICS",
        "ref": None,
        "subj": "a comparative transport cost ledger showing a dramatic 30 percent reduction in overall logistics expenditures achieved by direct deep-water port access",
        "setting": "an agricultural economics study office under warm natural desk light",
        "motion": "Steady camera shot framing the 30 percent cost reduction calculation graph"
    },
    {
        "id": "CH08_SC033",
        "dur": "4.46s",
        "words": 17,
        "text": "phá tan điểm nghẽn từng bào mòn sức cạnh tranh của nông sản suốt nhiều thập kỷ.",
        "anatomy": {
            "tier1": "Hình ảnh biểu tượng: Nút thắt cổ chai logistics cũ bằng đá sụp đổ, mở ra đại lộ thênh thang cho nông sản miền Tây vươn xa.",
            "tier2": "Đoàn xe container và sà lan rẽ sóng tiến thẳng ra đại cảng nước sâu trong không khí rộn rã, tưng bừng.",
            "tier3": "Cú máy đẩy nhanh theo đoàn xe container tiến ra đại cảng (Dynamic push-in following container trucks toward deep-water port)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dynamic visual of container trucks smoothly crossing modern access bridges toward the deep-water port terminal, symbolizing the definitive elimination of decades-old logistics bottlenecks",
        "setting": "a newly paved coastal highway approach in Soc Trang under bright morning sun",
        "motion": "Dynamic push-in shot following the flow of agricultural freight vehicles toward the port"
    },
    {
        "id": "CH08_SC034",
        "dur": "3.94s",
        "words": 15,
        "text": "Thế nhưng, mọi công trình kỹ thuật sẽ trở nên vô nghĩa nếu không có",
        "anatomy": {
            "tier1": "Bản vẽ thiết kế kỹ thuật các công trình đập cống và cảng biển đặt trên bàn hội thảo lập pháp.",
            "tier2": "Bàn tay nhà làm luật đặt cuốn sách Luật Đất đai bên cạnh các bản vẽ công trình, khẳng định vai trò tối thượng của thể chế.",
            "tier3": "Cú máy đẩy chậm vào cuốn sách Luật Đất đai đặt cạnh bản vẽ kỹ thuật (Slow push-in toward the Land Law book beside engineering blueprints)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an open red leather-bound volume of the National Land Law placed solemnly beside infrastructure engineering blueprints on an oak parliamentary committee table",
        "setting": "a legislative committee conference room in warm amber and mahogany tones",
        "motion": "Slow push-in shot toward the statutory legal code book"
    },
    {
        "id": "CH08_SC035",
        "dur": "3.94s",
        "words": 15,
        "text": "một bệ phóng thể chế đủ rộng lớn để khơi thông nguồn lực xã hội.",
        "anatomy": {
            "tier1": "Hội trường Quốc hội Việt Nam tại Nhà Quốc hội Ba Đình rực rỡ ánh đèn trong phiên biểu quyết thông qua luật mới.",
            "tier2": "Các đại biểu Quốc hội bấm nút biểu quyết với tỷ lệ tán thành áp đảo, khơi thông bệ phóng thể chế cho nền nông nghiệp hiện đại.",
            "tier3": "Cú máy góc rộng quay toàn cảnh hội trường Quốc hội biểu quyết (Wide cinematic shot of National Assembly voting session)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the grand plenary hall of the National Assembly of Vietnam in Hanoi with parliamentary delegates voting on institutional reform legislation under warm state chandeliers",
        "setting": "the National Assembly Hall in Ba Dinh Hanoi under dignified state illumination",
        "motion": "Wide cinematic tracking shot across the illuminated plenary hall"
    },
    {
        "id": "CH08_SC036",
        "dur": "3.67s",
        "words": 14,
        "text": "Luật Đất đai năm 2024 đã tạo ra một cuộc cách mạng thực sự",
        "anatomy": {
            "tier1": "Bìa cuốn sách Luật Đất đai năm 2024 mạ chữ vàng trang trọng.",
            "tier2": "Văn bản luật chính thức có hiệu lực, mang lại niềm tin và sinh khí mới cho các doanh nghiệp và nông dân cả nước.",
            "tier3": "Cú máy cận cảnh cuốn sách Luật Đất đai năm 2024 (Close-up shot of 2024 Land Law volume)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a formal close-up of the official publication of the 2024 Land Law with gold embossed lettering and the national emblem of Vietnam",
        "setting": "a legal repository library under warm ambient desk light",
        "motion": "Slow close-up push-in shot on the 2024 Land Law publication"
    },
    {
        "id": "CH08_SC037",
        "dur": "3.94s",
        "words": 15,
        "text": "khi nới hạn mức nhận chuyển nhượng đất nông nghiệp lên gấp mười lăm lần.",
        "anatomy": {
            "tier1": "Điều khoản nới hạn mức đất nông nghiệp trong Luật Đất đai 2024 hiển thị rõ nét trên trang văn bản.",
            "tier2": "Chỉ số hạn mức chuyển nhượng đất nông nghiệp tăng vọt từ 3 ha lên gấp 15 lần (đạt 45 ha), phá tan rào cản manh mún đất đai kéo dài nhiều thập kỷ.",
            "tier3": "Cú máy tĩnh trực diện vào quy định nới hạn mức đất lên gấp 15 lần (Steady shot on 15x Land Accumulation Limit increase) cùng text overlay góc trái dưới."
        },
        "overlay": "LUẬT ĐẤT ĐAI 2024: NỚI HẠN MỨC 15 LẦN",
        "ref": None,
        "subj": "an analytical legislative graphic showing the expansion of agricultural land transfer limits multiplied 15-fold from historical baseline restrictions up to 45 hectares per individual",
        "setting": "a legal research briefing room in warm ambient tones",
        "motion": "Steady camera shot framing the 15x land limit expansion legal infographic"
    },
    {
        "id": "CH08_SC038",
        "dur": "6.82s",
        "words": 26,
        "text": "Mỗi cá nhân giờ đây có thể tích tụ tới bốn mươi lăm héc ta đất canh tác để hình thành những đại điền hiện đại.",
        "anatomy": {
            "tier1": "Cánh đồng mẫu lớn đại điền rộng 45 héc ta thẳng cánh cò bay tại An Giang hoặc Đồng Tháp.",
            "tier2": "Dàn máy cày lớn và máy bay nông nghiệp không người lái (drone) sải cánh phun thuốc, gieo sạ tự động trên cánh đồng liền khoảnh không bờ ngăn.",
            "tier3": "Cú máy bay chậm trên cao (slow aerial glide) bao quát đại điền 45 ha cơ giới hóa (Slow aerial glide over 45-hectare modern consolidated paddy)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a grand sweeping aerial view of a contiguous 45-hectare consolidated modern rice estate in the delta, where agricultural drones and combine harvesters operate seamlessly across boundless open fields",
        "setting": "an expansive consolidated mega-farm in An Giang under warm morning sunlight",
        "motion": "Slow aerial glide across the seamless 45-hectare consolidated rice farmland"
    },
    {
        "id": "CH08_SC039",
        "dur": "4.2s",
        "words": 16,
        "text": "Đồng thời, việc bãi bỏ quy định xác nhận hộ nông dân đã mở toang cánh",
        "anatomy": {
            "tier1": "Bàn ký kết hợp đồng đầu tư nông nghiệp giữa doanh nghiệp công nghệ cao và hợp tác xã nông nghiệp.",
            "tier2": "Rào cản thủ tục hành chính cũ được bãi bỏ hoàn toàn, tạo hành lang thông thoáng cho các nhà đầu tư lớn.",
            "tier3": "Cú máy trượt ngang qua bàn ký kết hợp đồng đầu tư nông nghiệp (Horizontal tracking shot past agricultural investment signing table)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a business partnership signing event where high-tech corporate investors shake hands with rural agricultural cooperative leaders, celebrating the deregulation of farming status barriers",
        "setting": "a sunlit provincial trade conference room in warm ambient lighting",
        "motion": "Slow horizontal tracking shot past corporate and farming leaders signing contracts"
    },
    {
        "id": "CH08_SC040",
        "dur": "4.2s",
        "words": 16,
        "text": "cửa cho các doanh nghiệp mang vốn lớn và công nghệ cao đổ về đồng bằng.",
        "anatomy": {
            "tier1": "Khu nông nghiệp công nghệ cao với các trung tâm phân tích dữ liệu đồng ruộng và phòng máy chủ IoT.",
            "tier2": "Dòng vốn đầu tư hàng ngàn tỷ đồng của các tập đoàn lớn đổ về miền Tây, xây dựng các chuỗi giá trị nông sản khép kín.",
            "tier3": "Cú máy nâng chậm từ màn hình điều hành IoT lên toàn cảnh khu nông nghiệp công nghệ cao (Slow upward tilt from IoT console to high-tech farm)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a cutting-edge agricultural technology center in the Mekong Delta equipped with IoT soil sensors, automated irrigation monitors, and fleets of modern agricultural machinery funded by major corporate investment",
        "setting": "a high-tech agro-industrial research park under bright sunny skies",
        "motion": "Slow upward tilt from digital sensor displays toward modern agricultural facilities"
    },
    {
        "id": "CH08_SC041",
        "dur": "6.82s",
        "words": 26,
        "text": "Những quyết sách lịch sử từ thể chế, công nghệ đến hạ tầng đã biến nghịch cảnh địa hình thành bàn đạp phát triển tự cường.",
        "anatomy": {
            "tier1": "Bức tranh toàn cảnh đồng bằng sông Cửu Long mới: Cống Cái Lớn điều tiết nước, đại điền lúa phát thải thấp và cảng biển Trần Đề vươn khơi.",
            "tier2": "Sự kết hợp hoàn hảo giữa thể chế thông thoáng, công nghệ sinh thái và hạ tầng hiện đại tạo nên sức mạnh tự cường bền vững.",
            "tier3": "Cú máy bay cao (epic aerial glide) bao quát toàn bộ diện mạo mới của đồng bằng (Epic aerial glide over the transformed, resilient delta landscape)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an epic composite aerial panorama showcasing the transformed Mekong Delta: modern automated sluice gates regulating waters, vast low-emission rice fields, and deep-sea container ports thriving in harmony",
        "setting": "the vast sunlit plains of the southern delta under radiant morning sunshine",
        "motion": "Epic cinematic aerial glide capturing the thriving, resilient landscape of the modern delta"
    },
    {
        "id": "CH08_SC042",
        "dur": "3.41s",
        "words": 13,
        "text": "Việt Nam đã chứng minh cho thế giới thấy bản lĩnh của một",
        "anatomy": {
            "tier1": "Hội trường hội nghị nông nghiệp quốc tế với các đại biểu các nước đang chăm chú theo dõi bài học thành công của Việt Nam.",
            "tier2": "Biểu tượng bản lĩnh và trí tuệ Việt Nam trong việc biến thách thức biến đổi khí hậu thành cơ hội tái cơ cấu nông nghiệp.",
            "tier3": "Cú máy đẩy chậm vào bài trình bày mô hình phát triển bền vững của Việt Nam (Slow push-in on Vietnam sustainable development presentation)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an international agronomic symposium where global delegates applaud a keynote presentation on Vietnam climate-adaptive agricultural master model",
        "setting": "a prestigious international conference hall under warm architectural lighting",
        "motion": "Slow push-in shot toward the keynote presentation screen"
    },
    {
        "id": "CH08_SC043",
        "dur": "3.67s",
        "words": 14,
        "text": "quốc gia biết thích ứng linh hoạt và làm chủ vận mệnh sinh tồn.",
        "anatomy": {
            "tier1": "Người nông dân và kỹ sư nông nghiệp Việt Nam đứng hiên ngang trên bờ đê kênh Cái Lớn trong ánh bình minh rạng rỡ.",
            "tier2": "Nụ cười tự tin và ánh mắt kiên định của thế hệ người làm nông nghiệp làm chủ công nghệ, làm chủ thiên nhiên và làm chủ vận mệnh đất nước.",
            "tier3": "Cú máy nâng chậm từ mặt nước sông lên nụ cười tự hào của nông dân và kỹ sư (Slow tilt-up from water to proud smiling faces)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a Vietnamese agricultural engineer and veteran delta farmer standing proudly side by side on a modern riverbank revetment, looking out with confidence under a brilliant golden sunrise",
        "setting": "a reinforced riverbank along the Hau River under glorious morning skies",
        "motion": "Slow tilt-up from sparkling river water to the smiling, confident faces in the sunrise"
    },
    {
        "id": "CH08_SC044",
        "dur": "5.25s",
        "words": 20,
        "text": "Thế nhưng, câu chuyện của hạt gạo Việt Nam không dừng lại ở những thành tựu kinh tế trong nước.",
        "anatomy": {
            "tier1": "Bàn làm việc của nhà ngoại giao nông nghiệp với các bức ảnh hợp tác quốc tế giữa Việt Nam và bạn bè năm châu.",
            "tier2": "Hình ảnh những bao hạt giống lúa Việt Nam được chuẩn bị chuyển lên chuyên cơ ngoại giao vượt đại dương.",
            "tier3": "Cú máy đẩy chậm vào những bao hạt giống lúa ngoại giao (Slow push-in on diplomatic rice seed bags)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a diplomatic desk displaying archival photographs of Vietnamese agricultural delegations abroad beside specially sealed bags of certified Vietnamese rice seeds destined for international cooperation",
        "setting": "a diplomatic study room in warm ivory and walnut tones",
        "motion": "Slow push-in shot toward the certified diplomatic seed packages"
    },
    {
        "id": "CH08_SC045",
        "dur": "6.56s",
        "words": 25,
        "text": "Từ mảnh đất quê hương, những người làm nông nghiệp bắt đầu mang hạt giống no ấm vượt đại dương sang bên kia bán cầu.",
        "anatomy": {
            "tier1": "Đường băng sân bay quốc tế Nội Bài hoặc Tân Sơn Nhất lúc hoàng hôn rực rỡ với chuyên cơ chuẩn bị cất cánh.",
            "tier2": "Đoàn chuyên gia nông nghiệp Việt Nam vẫy tay chào tạm biệt quê hương, mang theo giống lúa và kỹ thuật canh tác sang Cuba và châu Phi, mở đầu cho Chương 9.",
            "tier3": "Cú máy nâng cao theo bóng chiếc máy bay cất cánh vào bầu trời hoàng hôn vàng cam (Ascending crane shot following aircraft taking off into warm sunset sky)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an evocative sunset view of an international passenger aircraft climbing smoothly into golden twilight skies above the Mekong Delta, carrying Vietnamese agricultural experts and seeds to distant continents",
        "setting": "the open skies above southern Vietnam at golden hour",
        "motion": "Smooth ascending crane shot following the aircraft climbing into the glowing amber twilight"
    }
]

# Generate Markdown Storyboard
md_lines = [
    "# chapter_08_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 8: Cuộc Cách Mạng Thuận Thiên Và Bàn Cờ Đại Đối Sách Của Nhà Nước",
    "## Phong cách chủ đạo: Luminous Warm Editorial Illustration (Minh họa báo chí cao cấp, ánh sáng trong trẻo rực rỡ, 100% không gian vật lý đời thực, triệt tiêu hoàn toàn siêu thực và màu đen u ám)",
    "",
    "### 🎨 Hệ màu 60-30-10 (Tuyệt Đối Ấm Áp — Chống Lạnh Lẽo):",
    "- **60% Tông màu nền chủ đạo:** Warm Ivory Cream (`#FAF7EE`), Warm Mekong Sunrise Sky (`#FFFBEB`), Warm Fresh River & Estuary Water (`#F3E5AB`). Tuyệt đối không dùng nền xám lạnh, xanh cyan buốt giá hay đen kịt.",
    "- **30% Đường nét & Chủ thể:** Ripe Golden Amber (`#F59E0B`), Terracotta Alluvium & Brick (`#EA580C`), Organic Rice-Shrimp Emerald Green (`#10B981`), Clean Architectural White Concrete (`#E5E7EB`).",
    "- **10% Điểm nhấn dẫn mắt:** Luminous Warm Golden Sunrise Rays (`#D97706`), Warm Chandelier Glow in Government Halls, Glowing Golden Amber Data Badges.",
    "",
    "---",
    "",
    "### 🛡️ Quy Tắc Kiểm Soát Tuyệt Đối:",
    "1. **Scene ID chuẩn theo chương:** `CH08_SC001` đến `CH08_SC045` (Khớp 100% với phân rã thời gian tự nhiên).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Văn phòng Chính phủ Hà Nội, Nhà Quốc hội Ba Đình, cống Cái Lớn - Cái Bé, mô hình lúa tôm Bạc Liêu/Cà Mau, đề án 1 triệu ha Cần Thơ, luồng hàng hải và đại cảng Trần Đề, đại điền An Giang.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc đúng 10/45 phân cảnh (22.2%) có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. 35 phân cảnh còn lại để `[TEXT OVERLAY]: Không`.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Ảnh Tham Chiếu Nhân Vật / Địa Danh:**",
    "   - `@cong_cai_lon.jpg` sử dụng tại `CH08_SC010`, `CH08_SC011`, `CH08_SC013`, `CH08_SC014`, `CH08_SC015` (Cống Cái Lớn - Cái Bé).",
    "   - `@thutuong_chinh.jpg` sử dụng tại `CH08_SC018`, `CH08_SC019` (Thủ tướng Phạm Minh Chính ký Quyết định 1490).",
    "   - `@bo_truong_le_minh_hoan.jpg` sử dụng tại `CH08_SC020`, `CH08_SC021` (Bộ trưởng Lê Minh Hoan trên đồng ruộng lúa phát thải thấp).",
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

# Save chapter_08_visual.md
with open("episodes/vu-khi-gao-viet-nam/chapter_08_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_08_visual.md ({len(scenes_data)} scenes)")

# Generate prompts_chapter_08.txt
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

with open("episodes/vu-khi-gao-viet-nam/prompts_chapter_08.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompt_lines).strip() + "\n")

print(f"✅ Generated prompts_chapter_08.txt ({len(scenes_data)} scenes)")
