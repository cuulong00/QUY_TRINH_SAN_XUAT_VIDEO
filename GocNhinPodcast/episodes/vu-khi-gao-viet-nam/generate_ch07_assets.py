"""
Script to generate both chapter_07_visual.md and prompts_chapter_07.txt
for Episode 'Vũ Khí Lúa Gạo Việt Nam' - Chapter 07.
Strictly adheres to:
- Flow Batch Studio syntax
- Warm Luminous Editorial Palette (#FAF7EE, #F59E0B, #EA580C)
- Selective Lower-Left 25% Rule (~20% text overlay)
- No artificial reference images for ordinary people
- Steady camera and static text preservation in video prompts
"""

import re
import json

scenes_data = [
    {
        "id": "CH07_SC001",
        "dur": "3.67s",
        "words": 14,
        "text": "Khi vượt qua những cơn biến động giá cả trên thị trường quốc tế",
        "anatomy": {
            "tier1": "Cầu cảng xuất khẩu gạo miền Tây lúc bình minh với mặt nước sông Tiền lấp lánh ánh vàng ấm áp.",
            "tier2": "Doanh nhân nông nghiệp đứng bên lan can cảng nhìn những chiếc sà lan chở gạo đã hoàn tất giao hàng quốc tế.",
            "tier3": "Cú máy trượt ngang chậm theo mặt nước sông Tiền buổi sớm (Slow horizontal tracking shot along river port waters)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an agricultural export executive standing on a wooden riverside pier at sunrise looking out at departed grain barges under a warm golden morning sky",
        "setting": "a tranquil river export terminal along the Tien River in southern Vietnam",
        "motion": "Slow horizontal tracking shot along the peaceful river surface reflecting morning sunrise"
    },
    {
        "id": "CH07_SC002",
        "dur": "3.94s",
        "words": 15,
        "text": "chúng ta thường nghĩ rằng mối đe dọa lớn nhất đã lùi lại phía sau.",
        "anatomy": {
            "tier1": "Bàn làm việc của chuyên gia với các bản báo cáo tài chính thị trường lúa gạo quốc tế đã hạ nhiệt.",
            "tier2": "Tập hồ sơ biến động giá cả được gấp lại, tạo cảm giác an tâm tạm thời cho giới quan sát kinh tế.",
            "tier3": "Cú máy đẩy chậm vào tập hồ sơ thị trường vừa được khép lại (Slow push-in toward closed market report dossier)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a desk in an analytical study with closed international price volatility binders and a peaceful view of green rice paddies outside the window",
        "setting": "a rural research retreat study in warm natural daylight",
        "motion": "Slow push-in shot toward the closed trade dossier on the desk"
    },
    {
        "id": "CH07_SC003",
        "dur": "6.3s",
        "words": 24,
        "text": "Thế nhưng, thử thách sinh tử thực sự của vựa lúa miền Tây không nằm ở các sàn giao dịch hàng hóa nước ngoài.",
        "anatomy": {
            "tier1": "Màn hình giao dịch hàng hóa Chicago và London mờ dần vào hậu cảnh.",
            "tier2": "Hình ảnh dòng sông Mekong hùng vĩ hiện lên rõ nét ở tiền cảnh, nơi cội nguồn sinh tử thực sự của hạt gạo.",
            "tier3": "Cú máy chuyển nét (rack focus) từ sàn giao dịch sang dòng sông Mekong rộng lớn (Rack focus from market tickers to vast river basin)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a cinematic transition shifting visual focus from soft-lit digital trading screens to an expansive, majestic aerial view of the great Mekong River channel",
        "setting": "an observation lounge overlooking the Mekong waterway under warm amber daylight",
        "motion": "Smooth rack focus from digital market terminals to the sweeping natural river channel"
    },
    {
        "id": "CH07_SC004",
        "dur": "6.04s",
        "words": 23,
        "text": "Nó đang âm thầm tích tụ ngay trên dòng sông mẹ Mekong, mạch máu nuôi dưỡng toàn bộ nền nông nghiệp đồng bằng.",
        "anatomy": {
            "tier1": "Dòng sông Mekong đỏ nặng phù sa trôi lững lờ qua các dải cù lao xanh mướt của vùng đồng bằng châu thổ.",
            "tier2": "Mạng lưới kênh rạch chằng chịt như hệ tuần hoàn mạch máu tưới tắm cho hàng triệu thửa ruộng lúa nước phì nhiêu.",
            "tier3": "Cú máy bay chậm trên cao (slow aerial glide) bao quát dòng sông mẹ và hệ thống kênh rạch (Slow aerial glide over Mekong arterial waterways)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a breathtaking aerial panorama of the mighty Mekong River splitting into dense networks of natural distributary canals that nourish endless emerald rice fields",
        "setting": "the vast agricultural delta of southern Vietnam in radiant warm morning sun",
        "motion": "Slow aerial glide across the sprawling arterial canal networks of the delta"
    },
    {
        "id": "CH07_SC005",
        "dur": "5.77s",
        "words": 22,
        "text": "Hàng ngàn năm qua, dòng sông Mekong bồi đắp cho miền Nam một vùng châu thổ trù phú bậc nhất hành tinh.",
        "anatomy": {
            "tier1": "Mặt cắt địa chất đồng bằng châu thổ sông Cửu Long với các lớp phù sa màu mỡ lắng đọng qua hàng ngàn năm lịch sử.",
            "tier2": "Đất phù sa son mịn màng trù phú nuôi dưỡng những vụ mùa bội thu nuôi sống hàng chục triệu con người.",
            "tier3": "Cú máy trượt ngang qua mặt cắt địa chất phù sa nghìn năm (Horizontal tracking shot past alluvium geological cross-section)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a conceptual geological and topographical cross-section illustration showing millennia of rich sediment and fertile alluvium layers forming the deep productive soil of the delta",
        "setting": "a natural science exhibition hall in warm natural amber tones",
        "motion": "Slow horizontal tracking shot illustrating the deep alluvium soil strata of the delta"
    },
    {
        "id": "CH07_SC006",
        "dur": "4.2s",
        "words": 16,
        "text": "Dòng sông ấy từng vận hành theo một nhịp thở tự nhiên vô cùng hoàn hảo.",
        "anatomy": {
            "tier1": "Bức tranh toàn cảnh mùa nước nổi lịch sử của miền Tây với nhịp điệu sinh thái hiền hòa, trù phú.",
            "tier2": "Những đàn cá linh non bơi lội, những bông điên điển vàng rực ven bờ và những cánh đồng ngập tràn nước ngọt phù sa.",
            "tier3": "Cú máy trượt chậm trên mặt nước mùa nổi hiền hòa (Slow tracking shot skimming over tranquil seasonal floodwaters)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a lyrical visual of the traditional historical Mekong flood season with blooming yellow sesbania flowers, calm inundation waters carrying schools of small fish across fertile floodplains",
        "setting": "the tranquil Dong Thap Muoi wetlands in early morning golden light",
        "motion": "Slow tracking shot skimming gently over the peaceful alluvium floodwaters"
    },
    {
        "id": "CH07_SC007",
        "dur": "6.3s",
        "words": 24,
        "text": "Mùa mưa mang lũ về cùng hàng trăm triệu tấn phù sa màu mỡ và nguồn thủy sản phong phú tràn qua biên giới.",
        "anatomy": {
            "tier1": "Cửa khẩu biên giới Đồng Tháp và An Giang khi dòng lũ đẹp tràn đồng mang theo dòng phù sa đỏ au cuồn cuộn.",
            "tier2": "Người dân miền Tây quăng chài bắt cá linh, nụ cười rạng rỡ đón nhận nguồn tài nguyên thiên nhiên hào phóng của dòng sông mẹ.",
            "tier3": "Cú máy góc rộng quay cảnh quăng chài trên cánh đồng ngập tràn phù sa (Wide cinematic shot of fisherman casting net over silt-rich waters)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a traditional Vietnamese delta fisherman casting a broad circular fishing net from a wooden sampan boat over vast silt-rich reddish floodwaters under warm morning sunlight",
        "setting": "the boundless open waters of An Giang floodplains during peak inundation season",
        "motion": "Wide cinematic tracking shot as the circular fishing net opens gracefully over the water"
    },
    {
        "id": "CH07_SC008",
        "dur": "5.51s",
        "words": 21,
        "text": "Dòng nước ngọt cuồn cuộn đổ ra biển Đông, tạo thành một bức tường áp lực đẩy lùi mặn xâm nhập.",
        "anatomy": {
            "tier1": "Chín cửa sông Cửu Long đổ ra biển Đông với dòng nước ngọt màu phù sa đỏ son cuồn cuộn.",
            "tier2": "Áp lực thủy lực tự nhiên khổng lồ của dòng chảy sông Tiền và sông Hậu đẩy lùi các lưỡi mặn biển Đông ra xa bờ hàng chục hải lý.",
            "tier3": "Cú máy bay cao từ cửa sông nhìn ra biển Đông rực nắng (High-angle aerial glide from river estuaries toward open East Sea)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a majestic high-angle view of the broad Mekong estuaries pouring powerful red sediment-rich freshwater plumes into the azure sea, naturally forcing seawater kilometers away from delta shores",
        "setting": "the coastal estuaries of southern Vietnam under radiant warm sunshine",
        "motion": "High-angle cinematic glide following the massive freshwater plume pushing out to sea"
    },
    {
        "id": "CH07_SC009",
        "dur": "3.67s",
        "words": 14,
        "text": "Thế nhưng ngày nay, nhịp thở ngàn năm ấy đã bị đứt gãy bởi",
        "anatomy": {
            "tier1": "Bản đồ lưu vực sông Mekong thượng nguồn bắt đầu xuất hiện những rào chắn cơ học khổng lồ.",
            "tier2": "Dòng chảy tự nhiên bị chia cắt, nhịp thở ngàn năm của dòng sông mẹ bị gián đoạn đột ngột.",
            "tier3": "Cú máy trượt dọc theo dòng sông thượng nguồn bị ngăn cắt (Tracking shot along fragmented upstream river course)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a transboundary map of the Upper Mekong (Lancang) River showing natural river flow interrupted by stylized concrete cross-sections and industrial barriers",
        "setting": "a transboundary river basin monitoring room in warm amber and cream tones",
        "motion": "Slow tracking shot following the upstream river path encountering concrete obstructions"
    },
    {
        "id": "CH07_SC010",
        "dur": "3.67s",
        "words": 14,
        "text": "chuỗi hơn mười một con đập thủy điện bậc thang trên dòng chính Mekong.",
        "anatomy": {
            "tier1": "Thân đập thủy điện bê tông trọng lực khổng lồ sừng sững chắn ngang hẻm núi hẹp trên dòng chính Mekong ở thượng nguồn.",
            "tier2": "Hồ chứa nước mênh mông bị khóa chặt phía sau bức tường bê tông xám cao hàng trăm mét, biểu tượng của chuỗi 11+ đập bậc thang.",
            "tier3": "Cú máy tĩnh trực diện vào chuỗi đập thủy điện bậc thang trên dòng chính Mekong (Steady shot on cascade mega-dams on Mekong mainstream) cùng text overlay góc trái dưới."
        },
        "overlay": "11+ ĐẬP THỦY ĐIỆN BẬC THANG MEKONG",
        "ref": None,
        "subj": "a colossal concrete gravity mega-dam spanning a steep mountain gorge on the upper Mekong River mainstream, holding back an immense reservoir under warm dramatic mountain light",
        "setting": "a rugged mountainous canyon on the upper Mekong mainstream in early morning sun",
        "motion": "Steady camera shot framing the monumental concrete dam wall and massive reservoir"
    },
    {
        "id": "CH07_SC011",
        "dur": "6.82s",
        "words": 26,
        "text": "Những công trình này tích nước phát điện theo nhu cầu công nghiệp của các quốc gia thượng nguồn, chứ không theo quy luật sinh học.",
        "anatomy": {
            "tier1": "Phòng điều khiển trung tâm nhà máy thủy điện thượng nguồn với các bảng điều khiển tuabin phát điện cao thế.",
            "tier2": "Quy trình đóng mở van xả nước phụ thuộc hoàn toàn vào phụ tải lưới điện công nghiệp và giá điện giờ cao điểm, đảo lộn hoàn toàn chu kỳ sinh thái tự nhiên.",
            "tier3": "Cú máy trượt ngang qua phòng điều khiển tuabin thủy điện (Horizontal tracking shot past industrial hydropower control consoles)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the high-tech control room of an upstream mega-dam with operators monitoring power grid telemetry screens, regulating water turbines to match industrial electrical peak demand rather than natural river rhythms",
        "setting": "an industrial hydropower station control room with warm console lighting",
        "motion": "Slow horizontal tracking shot past illuminated hydroelectric turbine monitors"
    },
    {
        "id": "CH07_SC012",
        "dur": "4.2s",
        "words": 16,
        "text": "Hệ quả là từ năm mươi đến bảy mươi phần trăm lượng bùn cát và phù",
        "anatomy": {
            "tier1": "Lòng hồ chứa thủy điện thượng nguồn nơi các lớp bùn cát nặng và phù sa mịn lắng đọng dày đặc dưới đáy hồ.",
            "tier2": "Bản đồ mặt cắt hồ chứa cho thấy hàng trăm triệu tấn phù sa bị giữ lại vĩnh viễn không thể trôi về hạ lưu.",
            "tier3": "Cú máy đẩy chậm vào lớp bùn phù sa bị chặn đáy hồ chứa (Slow push-in on sediment trapped behind reservoir bed)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an analytical scientific graphic showing the reservoir floor of an upstream dam choked with deep layers of captured geological sediment and rich fine silt that cannot flow downstream",
        "setting": "a scientific sedimentology research lab in warm amber tones",
        "motion": "Slow push-in shot toward the reservoir sediment trap schematic"
    },
    {
        "id": "CH07_SC013",
        "dur": "4.2s",
        "words": 16,
        "text": "sa mịn lịch sử đã bị giữ lại vĩnh viễn sau các thân đập khổng lồ.",
        "anatomy": {
            "tier1": "Báo cáo nghiên cứu phù sa lưu vực của Ủy hội Sông Mê Công (MRC) hiển thị tỷ lệ thất thoát phù sa lịch sử.",
            "tier2": "Con số giật mình: 50% đến 70% tổng lượng phù sa đã bị chặn lại sau các thân đập thủy điện, khiến hạ lưu kiệt quệ dinh dưỡng.",
            "tier3": "Cú máy tĩnh trực diện vào con số 50% - 70% phù sa bị chặn lại (Steady shot on 50% - 70% trapped sediment metric) cùng text overlay góc trái dưới."
        },
        "overlay": "50% - 70% PHÙ SA BỊ CHẶN LẠI",
        "ref": None,
        "subj": "an authoritative Mekong River Commission scientific audit report confirming that 50 to 70 percent of historical annual sediment and nutrient silt is permanently trapped behind upstream dams",
        "setting": "an environmental research conference room under warm neutral lighting",
        "motion": "Steady camera shot framing the sediment deficit data infographic"
    },
    {
        "id": "CH07_SC014",
        "dur": "6.82s",
        "words": 26,
        "text": "Dòng nước xả xuống hạ lưu trở thành dòng nước đói phù sa, mang năng lượng cơ học lớn và sẵn sàng gặm nhấm lòng sông.",
        "anatomy": {
            "tier1": "Cửa xả đáy của đập thủy điện tuôn ra dòng nước trong veo nhưng chảy xiết với tốc độ và động năng cực lớn.",
            "tier2": "Khái niệm thủy văn học 'Nước đói phù sa' (Hungry Water): Dòng nước thiếu bùn cát sẽ tự động cào xới và bào mòn lòng sông hạ du để bù đắp.",
            "tier3": "Cú máy tĩnh trực diện vào hiện tượng Nước Đói Phù Sa bào mòn lòng sông (Steady shot on 'Hungry Water' hydraulic phenomenon) cùng text overlay góc trái dưới."
        },
        "overlay": "HIỆN TƯỢNG 'NƯỚC ĐÓI PHÙ SA'",
        "ref": None,
        "subj": "a dramatic hydraulic visualization of high-velocity clear water discharged from dam sluices, illustrating the 'hungry water' phenomenon as turbulent currents aggressively scour downstream riverbeds",
        "setting": "a river hydraulics research laboratory simulation display in warm amber lighting",
        "motion": "Steady camera shot framing the hungry water hydraulic scouring illustration"
    },
    {
        "id": "CH07_SC015",
        "dur": "3.67s",
        "words": 14,
        "text": "Sạt lở bờ sông Tiền và sông Hậu diễn ra ngày càng dữ dội",
        "anatomy": {
            "tier1": "Một khúc bờ sông Tiền hoặc sông Hậu tại An Giang hoặc Đồng Tháp với những vết nứt toác kéo dài trên mặt đất.",
            "tier2": "Từng tảng đất phù sa và rặng cây ăn trái ven bờ sụp đổ xuống dòng sông chảy xiết dưới ánh nắng chiều vàng ấm.",
            "tier3": "Cú máy trượt ngang qua vệt bờ sông đang bị sạt lở nghiêm trọng (Horizontal tracking shot past crumbling riverbank erosion)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic riverbank erosion site along the Tien River in Dong Thap with deep ground fissures and large blocks of fertile alluvium soil sliding into the swift river currents",
        "setting": "a river shoreline in the Mekong Delta under warm late-afternoon sun",
        "motion": "Slow horizontal tracking shot along the fractured crumbling riverbank"
    },
    {
        "id": "CH07_SC016",
        "dur": "3.67s",
        "words": 14,
        "text": "cuốn trôi nhiều bờ bao và đất canh tác lâu đời của người dân.",
        "anatomy": {
            "tier1": "Thửa vườn cây ăn trái và bờ bao trồng lúa lâu đời của người dân bị mép nước khoét sâu vào tận gốc cây.",
            "tier2": "Người nông dân đứng nhìn đoạn đê bao vừa bị sạt lở, xót xa trước mảnh đất cha ông gìn giữ đang bị dòng sông nuốt chửng.",
            "tier3": "Cú máy nâng chậm từ vết sạt lở lên ánh mắt ưu tư của người nông dân (Slow tilt-up from eroded riverbank to concerned farmer)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a worried elderly Vietnamese farmer standing beside a reinforced bamboo stake barrier watching eroded chunks of ancestral orchard garden soil falling into the river",
        "setting": "a rural riverbank orchard in southern Vietnam under warm afternoon light",
        "motion": "Slow tilt-up from the broken earthen dike to the concerned farmer in the sunlight"
    },
    {
        "id": "CH07_SC017",
        "dur": "6.3s",
        "words": 24,
        "text": "Không dừng lại ở các đập thủy điện, tấm bản đồ thủy văn khu vực tiếp tục xuất hiện thêm những ẩn số mới.",
        "anatomy": {
            "tier1": "Bàn làm việc của Viện Quy hoạch Thủy lợi Miền Nam với bản đồ viễn thám lưu vực hạ lưu sông Mekong.",
            "tier2": "Các nhà khoa học dùng bút laser khoanh vùng các dự án công trình nhân tạo mới xuất hiện trên lãnh thổ láng giềng.",
            "tier3": "Cú máy đẩy chậm vào vùng biên giới hạ lưu trên bản đồ viễn thám (Slow push-in toward Lower Mekong transboundary satellite map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a high-resolution satellite cartography console displaying transboundary river networks in Cambodia and Vietnam with new artificial canal routes traced in glowing amber vectors",
        "setting": "a Southern Institute of Water Resources Planning research office in warm ambient light",
        "motion": "Slow push-in shot toward the new artificial waterway alignments on the regional map"
    },
    {
        "id": "CH07_SC018",
        "dur": "3.94s",
        "words": 15,
        "text": "Dự án Kênh đào Phù Nam Techo với chiều dài một trăm tám mươi cây",
        "anatomy": {
            "tier1": "Bản đồ tuyến kênh đào Phù Nam Techo (Funan Techo Canal) vạch dài 180 km từ sông Bassac hướng ra biển Kép.",
            "tier2": "Quy mô công trình nhân tạo vắt ngang qua 4 tỉnh của Campuchia hiển thị sắc nét trên nền bản đồ địa hình ấm áp.",
            "tier3": "Cú máy trượt dọc theo tuyến kênh đào dài 180 km (Horizontal tracking shot along the 180-kilometer canal alignment)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an architectural route map of the 180-kilometer Funan Techo Canal stretching across southern Cambodia from the Bassac River toward the Gulf of Thailand coast",
        "setting": "a regional infrastructure intelligence room in warm amber and cream tones",
        "motion": "Slow horizontal tracking shot tracing the 180 km proposed canal corridor"
    },
    {
        "id": "CH07_SC019",
        "dur": "4.2s",
        "words": 16,
        "text": "số và tổng vốn một phẩy bảy tỷ đô la đang được triển khai tại Campuchia.",
        "anatomy": {
            "tier1": "Công trường khởi công nạo vét kênh đào tại Campuchia với các dàn máy xúc gầu ngoạm và sà lan công trình lớn.",
            "tier2": "Tấm biển thông tin dự án khẳng định quy mô tổng vốn đầu tư 1.7 tỷ USD với chiều dài 180 km đang được xúc tiến ráo riết.",
            "tier3": "Cú máy tĩnh trực diện vào thông số Kênh Phù Nam Techo 180 km và 1.7 tỷ USD (Steady shot on Funan Techo Canal 180km & $1.7B specs) cùng text overlay góc trái dưới."
        },
        "overlay": "KÊNH PHÙ NAM TECHO: 180 KM (~1,7 TỶ USD)",
        "ref": None,
        "subj": "a grand civil engineering project site with heavy hydraulic excavators breaking ground along an engineered canal segment under bright tropical sunshine beside an informational project plaque",
        "setting": "an expansive infrastructure construction site in southern Cambodia under warm morning sun",
        "motion": "Steady camera shot framing the massive earthmoving equipment and project milestone plaque"
    },
    {
        "id": "CH07_SC020",
        "dur": "4.72s",
        "words": 18,
        "text": "Tuyến kênh này dự kiến kết nối sông Bassac, tức dòng sông Hậu, thẳng ra vịnh Thái Lan.",
        "anatomy": {
            "tier1": "Ngã rẽ thủy văn nơi tuyến kênh nhân tạo tách dòng từ sông Bassac (nhánh thượng lưu của sông Hậu) hướng về phía biển.",
            "tier2": "Mô hình thủy lực 3D mô phỏng sự chuyển hướng dòng nước mặt từ lưu vực sông Mekong sang vịnh Thái Lan.",
            "tier3": "Cú máy bay chậm theo hướng dòng chảy phân lưu ra vịnh Thái Lan (Slow aerial glide along diversion canal toward Gulf of Thailand)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dynamic 3D hydrological model showing the divergence of surface water from the Bassac River entering the engineered navigation canal flowing southwest toward the Gulf of Thailand",
        "setting": "a water resources engineering laboratory in warm amber lighting",
        "motion": "Slow aerial glide following the simulated water diversion path toward the gulf"
    },
    {
        "id": "CH07_SC021",
        "dur": "5.25s",
        "words": 20,
        "text": "Về mặt khoa học thủy văn, dòng chảy sông Hậu là nguồn nước ngọt huyết mạch cho vùng Châu Đốc",
        "anatomy": {
            "tier1": "Ngã ba sông Châu Đốc (An Giang) nơi dòng sông Hậu hiền hòa đổ vào đất Việt với nguồn nước ngọt trong lành.",
            "tier2": "Cánh đồng lúa và các trạm bơm nước ngọt Châu Đốc đang hút nước phục vụ hàng vạn hộ nông dân trong mùa khô.",
            "tier3": "Cú máy góc rộng quay toàn cảnh sông Hậu tại ngã ba Châu Đốc (Wide cinematic shot of Hau River entrance at Chau Doc)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a tranquil wide-angle view of the Hau River at the Chau Doc border junction in An Giang with fresh river water pumping stations irrigating lush green paddies under warm morning skies",
        "setting": "the border river junction at Chau Doc southern Vietnam in radiant morning sun",
        "motion": "Wide cinematic tracking shot across the vital freshwater junction at Chau Doc"
    },
    {
        "id": "CH07_SC022",
        "dur": "6.04s",
        "words": 23,
        "text": "An Giang và Cần Thơ trong mùa kiệt. Nếu một phần lưu lượng nước bị phân lưu trong các tháng mùa khô hạn",
        "anatomy": {
            "tier1": "Bản đồ lưu lượng dòng chảy mùa kiệt của sông Hậu qua các đô thị Long Xuyên, Cần Thơ.",
            "tier2": "Các nhà thủy văn học đo đạc mực nước kiệt, cảnh báo nguy cơ thiếu hụt nước tưới tiêu và sinh hoạt cho các đô thị lớn.",
            "tier3": "Cú máy trượt dọc theo dòng sông Hậu qua Cần Thơ (Horizontal tracking shot along Hau River flowing past Can Tho)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a hydrological chart monitoring low-season discharge rates along the Hau River passing through Long Xuyen and Can Tho with water level gauge sticks showing sensitive low marks",
        "setting": "a regional hydrological monitoring station in warm natural light",
        "motion": "Slow horizontal tracking shot along the Hau River low-season discharge monitoring chart"
    },
    {
        "id": "CH07_SC023",
        "dur": "3.94s",
        "words": 15,
        "text": "dòng chảy tự nhiên về phía hạ lưu sẽ chịu thêm áp lực suy giảm.",
        "anatomy": {
            "tier1": "Cọc tiêu đo mực nước sông Hậu trong mùa khô hiển thị mức nước rút cạn sát đáy bùn.",
            "tier2": "Dòng nước chảy chậm chạp, thiếu hụt lưu lượng cơ bản để duy trì cột nước đẩy mặn tự nhiên.",
            "tier3": "Cú máy hạ chậm dọc theo cọc tiêu đo mực nước (Slow downward tilt along hydrological water gauge stick)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a wooden hydrological water level gauge standing in shallow river waters showing receding dry-season levels, with sandbars emerging along the river channel",
        "setting": "a rural riverbank in the lower delta under warm dry afternoon sun",
        "motion": "Slow downward tilt along the river gauge stick revealing emerging sandbars"
    },
    {
        "id": "CH07_SC024",
        "dur": "5.51s",
        "words": 21,
        "text": "Khi áp lực nước ngọt từ thượng nguồn yếu đi, nước biển lập tức thừa cơ lấn sâu vào đất liền.",
        "anatomy": {
            "tier1": "Cửa biển sông Tiền và sông Hậu trong những ngày triều cường mùa khô.",
            "tier2": "Làn nước biển xanh mặn chát với áp lực sóng lớn lấn ngược dòng chảy nước ngọt yếu ớt, cuộn sâu vào các nhánh sông nội đồng.",
            "tier3": "Cú máy đẩy nhanh từ cửa biển ngược vào dòng sông nội đồng (Dynamic push-in from estuary moving inland against weak river currents)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic visualization of oceanic tidal surges pushing deep inland through coastal river mouths as weakening upstream river freshwater pressure fails to hold back the sea",
        "setting": "a coastal river estuary in southern Vietnam under warm afternoon sun",
        "motion": "Dynamic push-in shot following the relentless saline tidal wave surging upriver"
    },
    {
        "id": "CH07_SC025",
        "dur": "2.36s",
        "words": 9,
        "text": "Trong những mùa khô hạn khốc liệt gần đây",
        "anatomy": {
            "tier1": "Cánh đồng Bến Tre hoặc Tiền Giang trong đợt hạn mặn lịch sử 2016 và 2020 dưới ánh nắng chói chang.",
            "tier2": "Mặt đất bờ kênh nứt nẻ, những bãi cỏ vàng úa vì thiếu nước ngọt sinh hoạt và tưới tiêu.",
            "tier3": "Cú máy hạ thấp góc nhìn sát mặt đất nứt nẻ (Low-angle tracking shot along dry cracked soil)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a parched rural canal bank in Ben Tre during severe seasonal drought with dry cracked clay soil under a bright blazing tropical sun",
        "setting": "a drought-affected rural orchard lane in southern Vietnam",
        "motion": "Low-angle smooth tracking shot across the sun-baked cracked earth"
    },
    {
        "id": "CH07_SC026",
        "dur": "5.25s",
        "words": 20,
        "text": "ranh mặn bốn phần nghìn đã ăn sâu từ sáu mươi đến chín mươi lăm cây số vào nội đồng.",
        "anatomy": {
            "tier1": "Bản đồ viễn thám đo độ mặn của Viện Khoa học Thủy lợi Miền Nam với các vệt màu đỏ tím thể hiện ranh mặn 4‰.",
            "tier2": "Ranh giới mặn 4 gram/lít ăn sâu kỷ lục từ 60 đến 95 km vào tận các huyện nội đồng của Tiền Giang, Bến Tre và Sóc Trăng.",
            "tier3": "Cú máy tĩnh trực diện vào con số ranh mặn 4‰ ăn sâu 60 - 95 km (Steady shot on 4‰ salinity intrusion line reaching 60 - 95 km) cùng text overlay góc trái dưới."
        },
        "overlay": "RANH MẶN 4‰: ĂN SÂU 60 - 95 KM",
        "ref": None,
        "subj": "an agronomic salinity intrusion map displaying the alarming purple and amber contour lines of the critical 4 parts-per-thousand (4‰) salinity frontier penetrating 60 to 95 kilometers deep into the delta interior",
        "setting": "a water resources GIS laboratory under warm ambient monitor lighting",
        "motion": "Steady camera shot framing the transboundary salinity intrusion contour map"
    },
    {
        "id": "CH07_SC027",
        "dur": "6.82s",
        "words": 26,
        "text": "Nước mặn len lỏi vào từng con rạch, bủa vây các cánh đồng lúa và đe dọa trực tiếp các vườn cây ăn trái đặc sản.",
        "anatomy": {
            "tier1": "Vườn sầu riêng và bưởi da xanh đặc sản tại Chợ Lách (Bến Tre) hoặc Cái Bè (Tiền Giang) lá bắt đầu héo úa.",
            "tier2": "Dòng nước trong mương vườn đã nhiễm mặn, người nông dân cầm bút đo độ mặn lắc đầu bất lực nhìn rễ cây bị xót mặn.",
            "tier3": "Cú máy trượt ngang qua những hàng cây ăn trái đang khô lá vì nước mặn (Horizontal tracking shot past salinity-stressed fruit orchards)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a lush durian and pomelo specialty orchard in Cho Lach Ben Tre where irrigation ditches are fouled with salty brackish water, with an agronomist using a digital salinity meter beside curling yellow leaves",
        "setting": "a premium fruit orchard in the Mekong Delta under warm sunny skies",
        "motion": "Slow horizontal tracking shot past the yellowing leaves and brackish orchard ditches"
    },
    {
        "id": "CH07_SC028",
        "dur": "6.04s",
        "words": 23,
        "text": "Để tự cứu lấy mùa màng, nhiều người dân buộc phải khoan sâu vào lòng đất để khai thác nước ngầm tầng sâu.",
        "anatomy": {
            "tier1": "Góc vườn nông thôn với chiếc giàn khoan giếng thủ công đang khoan sâu hàng trăm mét vào lòng đất.",
            "tier2": "Máy bơm điện hoạt động hết công suất hút từng dòng nước ngầm ngọt mát lên tưới giải khát khẩn cấp cho cây trồng.",
            "tier3": "Cú máy nâng chậm từ miệng giếng khoan sâu lên máy bơm nước ngầm (Slow upward tilt from deep borehole well up to active electric pump)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a deep artisanal groundwater well drill in a rural orchard pumping valuable fresh groundwater from hundreds of meters below into storage ponds to rescue parched crops",
        "setting": "a rural homestead garden in southern Vietnam under warm afternoon sun",
        "motion": "Slow upward tilt from the vibrating groundwater pipe to the active pump motor"
    },
    {
        "id": "CH07_SC029",
        "dur": "2.36s",
        "words": 9,
        "text": "Nhưng cái giá phải trả vô cùng đắt đỏ.",
        "anatomy": {
            "tier1": "Mặt đất xung quanh giếng khoan xuất hiện những vết rạn nứt sụt lún địa chất.",
            "tier2": "Móng nhà và cống thủy lợi bị nứt toác, báo hiệu hiểm họa ngầm nghiêm trọng từ việc cạn kiệt tầng ngậm nước.",
            "tier3": "Cú máy cận cảnh vết nứt sụt lún địa tầng ven giếng khoan (Close-up shot on geological subsidence crack near wellhead)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a detailed geological close-up of structural foundation cracks along a concrete wall near a cluster of exhausted groundwater wells, symbolizing underground depletion",
        "setting": "a rural delta homestead under warm late-day sun",
        "motion": "Close-up slow tracking shot following structural fissures in the sinking soil"
    },
    {
        "id": "CH07_SC030",
        "dur": "6.3s",
        "words": 24,
        "text": "Mỗi năm, đồng bằng đang sụt lún từ một đến ba xăng ti mét, nhanh hơn gấp nhiều lần tốc độ nước biển dâng.",
        "anatomy": {
            "tier1": "Bản đồ vệ tinh đo độ sụt lún địa chất bằng công nghệ radar giao thoa (InSAR) của các viện nghiên cứu quốc tế.",
            "tier2": "Biểu đồ cảnh báo sụt lún địa tầng từ 1 đến 3 cm/năm, nhanh gấp 3 đến 5 lần tốc độ nước biển dâng do biến đổi khí hậu.",
            "tier3": "Cú máy tĩnh trực diện vào con số sụt lún đồng bằng 1 - 3 cm/năm (Steady shot on delta land subsidence rate of 1 - 3 cm/year) cùng text overlay góc trái dưới."
        },
        "overlay": "SỤT LÚN ĐỒNG BẰNG: 1 - 3 CM/NĂM",
        "ref": None,
        "subj": "a scientific satellite radar interferometry (InSAR) map displaying delta-wide land subsidence rates in striking amber and crimson heatmaps confirming ground sinking of 1 to 3 centimeters per year",
        "setting": "a geological remote sensing laboratory under warm ambient console lights",
        "motion": "Steady camera shot framing the 1 - 3 cm/year land subsidence InSAR analysis"
    },
    {
        "id": "CH07_SC031",
        "dur": "5.77s",
        "words": 22,
        "text": "Vựa lúa lớn nhất đất nước đang chìm dần xuống dưới mực nước biển trước sự ngỡ ngàng của giới khoa học.",
        "anatomy": {
            "tier1": "Cột mốc cao độ quốc gia cắm ven bờ kênh rạch với vạch đo cao độ bị nước triều ngập cao hơn bình thường.",
            "tier2": "Hình ảnh ẩn dụ: Đồng bằng trù phú đang chìm dần một cách âm thầm, đặt tương lai vựa lúa vào tình thế ngàn cân treo sợi tóc.",
            "tier3": "Cú máy hạ chậm theo cột mốc đo cao độ ngập nước triều (Slow downward tilt along submerged elevation benchmark pillar)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic conceptual visual of a geodetic delta elevation benchmark pillar partially submerged by rising daily tides, symbolizing the gradual sinking of the agricultural delta",
        "setting": "a coastal delta waterway at high tide in warm amber evening light",
        "motion": "Slow downward tilt along the partially submerged elevation marker"
    },
    {
        "id": "CH07_SC032",
        "dur": "3.67s",
        "words": 14,
        "text": "Thế nhưng, bi kịch thủy văn không chỉ đến từ bên ngoài biên giới.",
        "anatomy": {
            "tier1": "Một khúc sông nội đồng chia cắt hai vùng sản xuất nông nghiệp đặc thù của miền Tây.",
            "tier2": "Bên trái là cánh đồng lúa xanh mướt, bên phải là những vuông tôm sú ven biển rợp bóng quạt nước.",
            "tier3": "Cú máy bay chậm dọc theo con kênh ranh giới giữa lúa và tôm (Slow aerial glide along dividing boundary canal between rice and shrimp)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an aerial view of a dividing river canal in the lower peninsula where lush green freshwater rice paddies lie on one bank while saline shrimp aquaculture ponds lie on the other",
        "setting": "the transitional peninsula of southern Vietnam under warm morning sunlight",
        "motion": "Slow aerial glide along the dividing canal separating two conflicting agricultural worlds"
    },
    {
        "id": "CH07_SC033",
        "dur": "6.82s",
        "words": 26,
        "text": "Nó bùng nổ ngay trong chính lòng đồng bằng qua một cuộc xung đột sinh thái sâu sắc giữa người trồng lúa và người nuôi tôm.",
        "anatomy": {
            "tier1": "Cụm cống ngăn mặn bê tông chia cắt hai cộng đồng dân cư: Người nông dân trồng lúa bên trong cống và người nuôi tôm bên ngoài cống.",
            "tier2": "Ánh mắt căng thẳng của hai nhóm nông dân nhìn qua cánh cổng ngăn mặn, thể hiện cuộc chiến sinh thái gay gắt vì nguồn nước.",
            "tier3": "Cú máy trượt ngang qua cánh cống ngăn mặn chia đôi hai vùng sinh thái (Horizontal tracking shot past concrete sluice separating ecology)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a heavy concrete sluice gate creating a stark dividing line: upstream rice farmers with irrigation pumps on one side and downstream shrimp farmers operating aerator wheels on the other",
        "setting": "a canal junction in Bac Lieu or Ca Mau under warm bright morning sun",
        "motion": "Slow horizontal tracking shot past the rigid concrete sluice gate dividing the landscape"
    },
    {
        "id": "CH07_SC034",
        "dur": "6.3s",
        "words": 24,
        "text": "Tại vùng bán đảo Cà Mau, thiên nhiên tạo ra một vùng chuyển tiếp độc đáo giữa hai vùng nước ngọt và nước mặn.",
        "anatomy": {
            "tier1": "Bức tranh thiên nhiên tuyệt mỹ của bán đảo Cà Mau với rừng ngập mặn đan xen với các lung nước ngọt và đồng bưng.",
            "tier2": "Hệ sinh thái tự nhiên uyển chuyển thích nghi theo mùa: Mùa mưa ngọt ngào, mùa khô mặn mòi, tạo nên đa dạng sinh học trù phú.",
            "tier3": "Cú máy bay ngang bao quát vùng chuyển tiếp sinh thái bán đảo Cà Mau (Panoramic aerial glide over Ca Mau transitional ecotone)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a stunning panoramic aerial view of the Ca Mau peninsula where natural mangrove creeks transition seamlessly into brackish wetlands and freshwater peat forests under glorious golden daylight",
        "setting": "the pristine coastal tip of Ca Mau under warm golden morning skies",
        "motion": "Panoramic aerial glide showcasing the natural gradient between freshwater and coastal tides"
    },
    {
        "id": "CH07_SC035",
        "dur": "5.25s",
        "words": 20,
        "text": "Nhưng trong nhiều thập kỷ, tư duy thủy lợi cũ từng cố gắng ngọt hóa cưỡng bức bằng mọi giá.",
        "anatomy": {
            "tier1": "Bản đồ quy hoạch thủy lợi thời kỳ bao cấp với các đường kẻ đỏ bao bọc toàn bộ bán đảo để 'ngọt hóa'.",
            "tier2": "Các kỹ sư thủy lợi thời kỳ cũ cầm thước kẻ cứng nhắc ép thiên nhiên phải theo ý chí chủ quan của con người.",
            "tier3": "Cú máy đẩy chậm vào các khẩu hiệu 'Ngọt hóa bán đảo Cà Mau' trên bản vẽ cũ (Slow push-in on historical forced freshwater zoning blueprints)."
        },
        "overlay": None,
        "ref": None,
        "subj": "historical engineering blueprints from the 1980s displaying ambitious linear dike networks designed to artificially freshen the entire coastal peninsula, viewed in an archival office",
        "setting": "an archival engineering office under warm table lamp illumination",
        "motion": "Slow push-in shot toward the vintage 'forced freshwater conversion' regional masterplan"
    },
    {
        "id": "CH07_SC036",
        "dur": "3.94s",
        "words": 15,
        "text": "Hàng loạt tuyến đê bao khép kín và cống ngăn mặn được dựng lên với",
        "anatomy": {
            "tier1": "Những tuyến đê bao bằng đất và đá kiên cố dựng lên dọc theo bờ biển và các cửa kênh rạch.",
            "tier2": "Hàng loạt cống ngăn mặn bằng bê tông cốt thép đóng sập cánh van sắt, ngăn chặn tuyệt đối nước biển tràn vào.",
            "tier3": "Cú máy trượt ngang qua dãy cống ngăn mặn bê tông kiên cố (Horizontal tracking shot past massive concrete salinity gates)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a line of heavy concrete salinity barriers and reinforced earthen dikes constructed along coastal waterways, with heavy iron gates lowered into the water under warm sunlight",
        "setting": "a coastal irrigation branch in southern Vietnam in warm morning light",
        "motion": "Slow horizontal tracking shot past the closed concrete salinity barrier gates"
    },
    {
        "id": "CH07_SC037",
        "dur": "3.94s",
        "words": 15,
        "text": "mục tiêu duy nhất là bảo vệ tối đa những cánh đồng ba vụ lúa.",
        "anatomy": {
            "tier1": "Bên trong đê bao: Những cánh đồng lúa ba vụ gượng gạo sinh trưởng trên nền đất nhiễm phèn mặn tiềm tàng.",
            "tier2": "Khẩu hiệu 'Thâm canh ba vụ lúa' kẻ bằng sơn đỏ trên tường trạm bơm thủy lợi cũ, phản ánh tư duy duy ý chí.",
            "tier3": "Cú máy tĩnh trực diện vào tư duy ngọt hóa cưỡng bức bảo vệ 3 vụ lúa (Steady shot on 'Forced Freshwater Conversion' policy paradigm) cùng text overlay góc trái dưới."
        },
        "overlay": "TƯ DUY 'NGỌT HÓA CƯỠNG BỨC'",
        "ref": None,
        "subj": "a rural irrigation station with a faded painted slogan 'Protecting Three-Crop Rice' overlooking interior paddies enclosed behind rigid dikes, under warm dusty midday sun",
        "setting": "a provincial irrigation compound in Bac Lieu under warm ambient daylight",
        "motion": "Steady camera shot framing the irrigation pump house and the enclosed three-crop paddy"
    },
    {
        "id": "CH07_SC038",
        "dur": "5.25s",
        "words": 20,
        "text": "Mục tiêu ấy đã vô tình đẩy hàng trăm ngàn hộ nuôi tôm vùng ven biển vào cảnh khốn cùng.",
        "anatomy": {
            "tier1": "Bên ngoài cống đê bao: Các vuông nuôi tôm của người dân Cà Mau và Bạc Liêu trong cảnh cạn kiệt nguồn nước mặn sạch.",
            "tier2": "Gia đình người nuôi tôm bần thần nhìn đầm tôm đứng quạt nước, đối mặt với nguy cơ phá sản vì nguồn nước bị ngọt hóa.",
            "tier3": "Cú máy đẩy chậm vào khuôn mặt âu lo của người nuôi tôm bên bờ vuông (Slow push-in on worried shrimp farmer beside aquaculture pond)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a distressed Vietnamese shrimp farmer standing beside an idle aquaculture pond in Ca Mau, looking with despair at brackish water ponds deprived of clean tidal sea inflows",
        "setting": "a coastal aquaculture farm in Bac Lieu under warm afternoon sunlight",
        "motion": "Slow push-in shot toward the shrimp farmer gazing over the stagnant ponds"
    },
    {
        "id": "CH07_SC039",
        "dur": "2.89s",
        "words": 11,
        "text": "Người trồng lúa ở thượng nguồn cần nước ngọt tuyệt đối",
        "anatomy": {
            "tier1": "Ruộng lúa trĩu đòng xanh mướt ở thượng lưu cần nguồn nước ngọt hoàn toàn tinh khiết để làm đòng và nuôi hạt.",
            "tier2": "Nông dân chăm sóc kênh dẫn nước ngọt, kiểm tra từng giọt nước tưới tiêu trong lành.",
            "tier3": "Cú máy hạ thấp góc nhìn sát ngọn lúa xanh tươi đón dòng nước ngọt (Low-angle tracking shot along freshwater paddy canal)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an upstream rice farmer bending down to inspect healthy green rice stalks thriving in pure freshwater flowing gently through an earthen canal",
        "setting": "a fertile freshwater paddy field in southern Vietnam under warm morning light",
        "motion": "Low-angle smooth tracking shot along the clean freshwater paddy furrow"
    },
    {
        "id": "CH07_SC040",
        "dur": "4.72s",
        "words": 18,
        "text": "bởi chỉ cần nước mặn vượt ngưỡng hai phần nghìn là lúa sẽ cháy lá và lép hạt.",
        "anatomy": {
            "tier1": "Một vạt lúa bị nước mặn xâm nhập nhẹ với những chiếc lá bắt đầu cuộn tròn và cháy vàng từ chóp lá.",
            "tier2": "Bút đo độ mặn hiển thị con số 2.1‰: Ngưỡng tử thần khiến bông lúa bị nghẹn đòng, hạt lúa bị lép trắng trơ trọi.",
            "tier3": "Cú máy tĩnh trực diện vào ngưỡng chịu mặn của lúa < 2‰ (Steady shot on Rice Salinity Threshold < 2‰) cùng text overlay góc trái dưới."
        },
        "overlay": "LÚA: CHỊU MẶN < 2‰",
        "ref": None,
        "subj": "a close-up demonstration of a digital refractometer meter reading 2.1‰ beside withered yellow-tipped rice leaves that have succumbed to saline burn",
        "setting": "an agronomy field testing station in warm natural daylight",
        "motion": "Steady camera shot framing the salinity meter reading and the damaged rice leaves"
    },
    {
        "id": "CH07_SC041",
        "dur": "3.41s",
        "words": 13,
        "text": "Nhưng người nuôi tôm ở hạ lưu lại cần nước mặn từ mười",
        "anatomy": {
            "tier1": "Vuông tôm sú ven biển Cà Mau với các guồng quạt nước quay tròn tạo bọt trắng xóa dưới nắng sớm.",
            "tier2": "Người nuôi tôm kiểm tra độ mặn lý tưởng để thả giống tôm sú và tôm thẻ chân trắng.",
            "tier3": "Cú máy trượt ngang qua guồng quạt nước vuông tôm (Horizontal tracking shot past spinning paddlewheel aerator)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a vibrant coastal black tiger shrimp pond in Ca Mau with electric paddlewheel aerators spinning furiously, spraying sparkling white foam across the sunlit brackish water",
        "setting": "a thriving coastal shrimp farm in southern Ca Mau under warm bright morning sun",
        "motion": "Slow horizontal tracking shot past the spinning aerator spray in the brackish pond"
    },
    {
        "id": "CH07_SC042",
        "dur": "3.67s",
        "words": 14,
        "text": "đến hai mươi lăm phần nghìn để tôm sú và tôm thẻ sinh trưởng.",
        "anatomy": {
            "tier1": "Khay kiểm tra tôm sú khỏe mạnh với lớp vỏ bóng bẩy và râu tôm dài thẳng trong nước mặn đạt chuẩn.",
            "tier2": "Bút đo độ mặn trong vuông tôm hiển thị dải độ mặn tối ưu từ 10‰ đến 25‰ giúp tôm lột xác và tăng trưởng nhanh.",
            "tier3": "Cú máy tĩnh trực diện vào ngưỡng độ mặn nuôi tôm 10 - 25‰ (Steady shot on Shrimp Salinity Requirement 10 - 25‰) cùng text overlay góc trái dưới."
        },
        "overlay": "TÔM: CẦN MẶN 10 - 25‰",
        "ref": None,
        "subj": "a clear testing basin displaying robust black tiger shrimp swimming vigorously in healthy water beside a digital water quality meter indicating 18‰ salinity",
        "setting": "an aquaculture research laboratory in warm ambient lighting",
        "motion": "Steady camera shot framing the active shrimp and the 10 - 25‰ optimal salinity range metric"
    },
    {
        "id": "CH07_SC043",
        "dur": "3.67s",
        "words": 14,
        "text": "Khi các cửa cống bị đóng chặt quanh năm để giữ ngọt cho lúa",
        "anatomy": {
            "tier1": "Cửa cống ngăn mặn bằng thép nặng hàng chục tấn đóng sập xuống lòng kênh, rêu bám phong trần.",
            "tier2": "Dòng nước biển sạch bị chặn đứng hoàn toàn ngoài sông lớn, không thể dẫn vào hệ thống kênh dẫn của các vuông tôm.",
            "tier3": "Cú máy hạ chậm dọc theo cánh van sắt cống ngăn mặn đóng chặt (Slow downward tilt along locked steel sluice gate)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a massive steel sluice gate firmly lowered into the riverbed, blocking tidal seawater flow with heavy iron winches and padlocks under warm afternoon sunlight",
        "setting": "a provincial coastal salinity barrier gate in southern Vietnam",
        "motion": "Slow downward tilt along the imposing closed steel sluice gate"
    },
    {
        "id": "CH07_SC044",
        "dur": "4.72s",
        "words": 18,
        "text": "vuông tôm của các hộ dân phía dưới bị thiếu mặn, tôm chết hàng loạt vì sốc nước.",
        "anatomy": {
            "tier1": "Đầm tôm hạ lưu nước bị ngọt hóa và tù đọng do không có nước biển lưu thông trong mùa nắng.",
            "tier2": "Tôm nuôi bị sốc nước ngọt nổi đầu và chết dạt vào bờ ao, người nông dân vớt tôm chết trong nước mắt xót xa.",
            "tier3": "Cú máy cận cảnh tôm chết dạt góc ao và ánh mắt bất lực của người nuôi (Close-up shot of dead shrimp floating along pond bank)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a heartbreaking scene at a shrimp farm where juvenile shrimp float lifelessly along the pond edge due to stagnant freshwater shock, with a farmer kneeling in grief",
        "setting": "a parched coastal aquaculture farm in Ca Mau in late afternoon warm light",
        "motion": "Slow close-up tilt from the dead shrimp along the bank to the grieving farmer"
    },
    {
        "id": "CH07_SC045",
        "dur": "6.82s",
        "words": 26,
        "text": "Một cuộc chiến sinh kế âm ỉ nhưng vô cùng gay gắt đã nổ ra giữa hai nhóm nông dân sống chung trên một dòng sông.",
        "anatomy": {
            "tier1": "Bến đò chia cắt hai xóm: Xóm trồng lúa bên bờ Bắc và Xóm nuôi tôm bên bờ Nam con kênh chung.",
            "tier2": "Những cuộc tranh luận nảy lửa và ánh mắt lạnh nhạt giữa hai nhóm bà con vốn từng là hàng xóm tối lửa tắt đèn có nhau.",
            "tier3": "Cú máy trượt ngang qua con kênh ngăn cách hai cộng đồng sinh kế (Horizontal tracking shot along canal dividing farming communities)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a tense social scene along a shared village canal where rice farming neighbors on one bank and shrimp farming neighbors on the other stare silently across the water",
        "setting": "a rural delta village divided by a communal waterway under warm afternoon sun",
        "motion": "Slow horizontal tracking shot along the communal canal capturing the palpable tension"
    },
    {
        "id": "CH07_SC046",
        "dur": "6.82s",
        "words": 26,
        "text": "Đã có những giai đoạn căng thẳng đến mức người nuôi tôm phải lén lút mang xà beng cạy khóa cống ngăn mặn trong đêm tối.",
        "anatomy": {
            "tier1": "Cống ngăn mặn trong đêm trăng sáng vằng vặc với ánh đèn bão vàng cam ấm áp lập lòe.",
            "tier2": "Nhóm người nuôi tôm vì đường cùng mang xà beng và búa sắt đến cạy ổ khóa cống để cứu đầm tôm đang chết khát mặn.",
            "tier3": "Cú máy tĩnh trực diện vào cuộc chiến sinh thái gay gắt lúa - tôm trong đêm (Steady shot on historic midnight Rice vs Shrimp conflict) cùng text overlay góc trái dưới."
        },
        "overlay": "XUNG ĐỘT SINH KẾ LÚA - TÔM",
        "ref": None,
        "subj": "a dramatic historical nocturnal scene at a remote coastal concrete sluice gate under a warm amber full moon, where desperate shrimp farmers use iron crowbars to force open the gate winches",
        "setting": "a secluded canal sluice gate in southern Vietnam at night under warm amber moonlight and lantern glow",
        "motion": "Steady camera shot capturing the dramatic tension of the midnight sluice gate breach"
    },
    {
        "id": "CH07_SC047",
        "dur": "4.72s",
        "words": 18,
        "text": "Họ mở cửa cống để cứu vãn cả cơ nghiệp đang nằm dưới vuông tôm khát nước mặn.",
        "anatomy": {
            "tier1": "Cánh van cống ngăn mặn được nhấc bổng lên trong tiếng xích sắt va đập giòn giã.",
            "tier2": "Làn nước biển mặn chát cuồn cuộn tràn qua khe cống, mang theo nguồn sống cứu vãn cả cơ nghiệp đầm tôm của bà con.",
            "tier3": "Cú máy nâng chậm theo dòng nước biển cuồn cuộn tràn qua cống mở (Slow upward tilt along swirling saline water rushing through opened gate)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the heavy iron gate of the sluice being winched upward as dark, turbulent tidal saltwater rushes with great force through the concrete culvert into the dry canal",
        "setting": "the open sluice culvert under warm amber lantern illumination and moonlight",
        "motion": "Slow upward tilt following the rushing flood of seawater surging through the culvert"
    },
    {
        "id": "CH07_SC048",
        "dur": "3.41s",
        "words": 13,
        "text": "Thế nhưng, dòng nước biển mặn chát tràn qua lập tức làm cháy",
        "anatomy": {
            "tier1": "Nước mặn tràn ngược vào các kênh dẫn nội đồng của vùng lúa thượng lưu trong buổi sáng sớm.",
            "tier2": "Mặt ruộng lúa bắt đầu biến màu, những gốc lúa non ngâm trong nước mặn bị thối rễ và xót ngọn.",
            "tier3": "Cú máy trượt nhanh theo dòng nước mặn len lỏi vào các thửa ruộng lúa (Dynamic tracking pan following saltwater into rice furrows)."
        },
        "overlay": None,
        "ref": None,
        "subj": "early morning view of swirling brackish water infiltrating upstream rice irrigation canals, with saline foam spreading into emerald paddy furrows",
        "setting": "upstream rural paddy furrows under early morning warm sunlight",
        "motion": "Smooth horizontal tracking shot following the spreading saline tide into the rice fields"
    },
    {
        "id": "CH07_SC049",
        "dur": "6.3s",
        "words": 24,
        "text": "rụi những ruộng lúa xanh non của những người hàng xóm bên kia cống. Mâu thuẫn ấy cho thấy một chân lý rõ ràng",
        "anatomy": {
            "tier1": "Cánh đồng lúa bên kia cống cháy rụi, biến thành màu nâu xám xơ xác vì nhiễm mặn đột ngột.",
            "tier2": "Người nông dân trồng lúa bàng hoàng đứng nhìn ruộng lúa cả vụ mùa tan thành mây khói, thể hiện bi kịch xung đột sinh thái sâu sắc.",
            "tier3": "Cú máy lùi chậm bao quát cánh đồng lúa bị cháy rụi bên cạnh con cống (Slow pull-back shot across the scorched paddy field beside the sluice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a ruined expanse of green rice paddy scorched brown and brittle from sudden saltwater intrusion, with a devastated farmer standing in the center under warm morning sun",
        "setting": "a damaged agricultural field in the coastal delta under warm clear skies",
        "motion": "Slow pull-back camera shot revealing the wide expanse of scorched rice crops"
    },
    {
        "id": "CH07_SC050",
        "dur": "5.25s",
        "words": 20,
        "text": "không thể áp đặt một mệnh lệnh hành chính cứng nhắc lên một hệ sinh thái tự nhiên đa dạng.",
        "anatomy": {
            "tier1": "Bàn hội thảo khoa học môi trường ĐBSCL với các chuyên gia sinh thái học và nhà quy hoạch chính sách.",
            "tier2": "Các nhà khoa học chỉ rõ: Không thể dùng mệnh lệnh hành chính cứng nhắc bắt thiên nhiên tuân theo một khuôn mẫu độc canh duy nhất.",
            "tier3": "Cú máy đẩy chậm vào bản đúc kết triết lý thuận thiên sinh thái (Slow push-in on ecological nature-based adaptation report)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an ecological symposium hall where senior environmental scientists review comparative ecosystem diagrams, pointing out the failure of rigid administrative command over natural hydrological diversity",
        "setting": "an academic conference hall in warm ivory cream and amber tones",
        "motion": "Slow push-in shot toward the nature-based ecological transition presentation"
    },
    {
        "id": "CH07_SC051",
        "dur": "2.36s",
        "words": 9,
        "text": "Bên cạnh gọng kìm thủy văn và sinh thái",
        "anatomy": {
            "tier1": "Hình ảnh biểu tượng tổng hợp: Một bên là đập thủy điện thượng nguồn, một bên là cống ngăn mặn sạt lở và sụt lún.",
            "tier2": "Hai gọng kìm khổng lồ siết chặt lấy sự sinh tồn của đồng bằng sông Cửu Long.",
            "tier3": "Cú máy trượt ngang qua hai gọng kìm thủy văn và sinh thái (Horizontal tracking shot past dual hydrological-ecological pincers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a conceptual diptych diagram synthesizing the dual pressures: upstream mega-dams constricting freshwater and internal ecological clashes destabilizing soil and water",
        "setting": "a strategic policy dashboard display in warm amber tones",
        "motion": "Slow horizontal tracking shot across the dual stress indicators"
    },
    {
        "id": "CH07_SC052",
        "dur": "5.25s",
        "words": 20,
        "text": "vựa lúa miền Tây còn phải đối mặt với một bức tường chi phí khổng lồ từ hệ thống logistics.",
        "anatomy": {
            "tier1": "Một con kênh thủy nội địa miền Tây với hàng đoàn sà lan và ghe chở lúa ùn ứ chờ bốc dỡ.",
            "tier2": "Bức tường chi phí vận tải đường thủy nội địa đè nặng lên giá thành hạt gạo khi xuất khẩu ra thị trường quốc tế.",
            "tier3": "Cú máy nâng chậm từ khoang sà lan lúa lên bảng tính toán chi phí vận chuyển (Slow upward tilt from barge hold to freight calculation ledger)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a crowded delta canal waterway jammed with lines of wooden rice sampans and heavy steel barges waiting at a bottleneck river intersection under warm afternoon sun",
        "setting": "a bustling canal crossroads in the Mekong Delta under warm sunny skies",
        "motion": "Slow upward tilt from the loaded grain barges toward the congested river crossing"
    },
    {
        "id": "CH07_SC053",
        "dur": "6.56s",
        "words": 25,
        "text": "Hiện nay, chi phí logistics đang chiếm tới hai mươi lăm đến ba mươi phần trăm trong cơ cấu giá thành xuất khẩu hạt gạo.",
        "anatomy": {
            "tier1": "Báo cáo kiểm toán chuỗi logistics nông sản ĐBSCL của Ngân hàng Thế giới (World Bank).",
            "tier2": "Biểu đồ tròn cơ cấu giá thành xuất khẩu: Chi phí logistics chiếm tỷ trọng khổng lồ từ 25% đến 30% giá bán hạt gạo.",
            "tier3": "Cú máy tĩnh trực diện vào con số chi phí logistics 25% - 30% giá thành (Steady shot on Logistics Cost 25% - 30% export breakdown) cùng text overlay góc trái dưới."
        },
        "overlay": "CHI PHÍ LOGISTICS: 25% - 30%",
        "ref": None,
        "subj": "a World Bank agricultural supply chain report displaying an analytical pie chart showing logistics expenditures consuming an excessive 25 to 30 percent of total export rice costs",
        "setting": "a logistics research office in warm neutral lighting",
        "motion": "Steady camera shot framing the 25 - 30 percent logistics cost burden pie chart"
    },
    {
        "id": "CH07_SC054",
        "dur": "4.72s",
        "words": 18,
        "text": "Nguyên nhân cốt lõi là do luồng Định An ở cửa sông Hậu thường xuyên bị bồi lắng",
        "anatomy": {
            "tier1": "Cửa biển Định An tại Trà Vinh nơi dòng sông Hậu đổ ra biển Đông với những bãi cát ngầm bồi lắng trắng xóa.",
            "tier2": "Tàu cuốc nạo vét luồng hàng hải hoạt động liên tục nhưng cát biển và phù sa lập tức bồi lắng trở lại sau mỗi con sóng.",
            "tier3": "Cú máy bay chậm trên cao bao quát cửa biển Định An bị bồi lắng (Slow aerial glide over silted Dinh An river mouth)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an expansive aerial view of the Dinh An estuary at the mouth of the Hau River in Tra Vinh, where heavy marine sandbars and siltation create shallow treacherous navigation shoals",
        "setting": "the vast coastal river mouth of Dinh An under bright warm morning sun",
        "motion": "Slow aerial glide across the shallow sandbars choking the Dinh An estuary channel"
    },
    {
        "id": "CH07_SC055",
        "dur": "3.41s",
        "words": 13,
        "text": "đáy luồng rất cạn nên các tàu biển lớn không thể cập bến.",
        "anatomy": {
            "tier1": "Mặt cắt đáy luồng tàu Định An với độ sâu luồng chỉ đạt 3 - 4 mét nước trong mùa cạn.",
            "tier2": "Con tàu viễn dương tải trọng 20.000 tấn đành phải neo đậu ngoài khơi xa, hoàn toàn bất lực không thể tiến vào cảng Cần Thơ.",
            "tier3": "Cú máy tĩnh trực diện vào điểm nghẽn luồng Định An bị bồi lắng cạn đáy (Steady shot on Dinh An navigation bottleneck) cùng text overlay góc trái dưới."
        },
        "overlay": "ĐIỂM NGHẼN: LUỒNG ĐỊNH AN BỒI LẮNG",
        "ref": None,
        "subj": "a marine navigational chart showing shallow 3-meter bathymetric soundings at the Dinh An bar beside an offshore view of a large international cargo vessel forced to anchor outside",
        "setting": "a maritime navigation tower overlooking the Tra Vinh coastline in warm daylight",
        "motion": "Steady camera shot framing the nautical chart soundings and stranded cargo vessel"
    },
    {
        "id": "CH07_SC056",
        "dur": "6.3s",
        "words": 24,
        "text": "Hậu quả là có tới bảy mươi đến tám mươi phần trăm lượng hàng hóa của đồng bằng không thể xuất khẩu trực tiếp.",
        "anatomy": {
            "tier1": "Cảng quốc tế Cần Thơ vắng bóng tàu viễn dương lớn do vướng điểm nghẽn luồng Định An.",
            "tier2": "Biểu đồ thống kê 70% đến 80% tổng sản lượng gạo của 13 tỉnh miền Tây phải đi đường vòng, không thể thông quan xuất khẩu tại chỗ.",
            "tier3": "Cú máy trượt ngang qua cầu cảng Cần Thơ thiếu vắng tàu lớn (Horizontal tracking shot past Can Tho quayside lacking deep-draft ships)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a quiet riverside wharf at Can Tho Port under-utilized by deep-sea vessels beside an infographic showing 70 to 80 percent of regional cargo unable to export directly from the delta",
        "setting": "the riverfront port of Can Tho under warm afternoon sunshine",
        "motion": "Slow horizontal tracking shot past empty deep-water quayside berths"
    },
    {
        "id": "CH07_SC057",
        "dur": "3.94s",
        "words": 15,
        "text": "Nông sản phải bốc dỡ qua nhiều khâu trung chuyển bằng ghe nhỏ hoặc sà",
        "anatomy": {
            "tier1": "Bến chuyển tải nông sản ven sông với cảnh bốc xếp thủ công tốn kém thời gian và công sức.",
            "tier2": "Từng bao gạo được bốc từ nhà máy xuống ghe nhỏ, rồi từ ghe nhỏ lại bốc sang sà lan lớn, qua vô số khâu trung gian.",
            "tier3": "Cú máy nâng chậm theo công nhân bốc vác gạo lên sà lan trung chuyển (Slow upward tilt along workers loading rice onto river barge)."
        },
        "overlay": None,
        "ref": None,
        "subj": "dock workers and portable conveyor belts repeatedly transshipping 50kg rice sacks from small wooden riverboats onto mid-sized river barges at an inland transfer jetty",
        "setting": "a busy river transfer jetty in southern Vietnam in warm morning light",
        "motion": "Slow upward tilt following the conveyor loading bags into the barge hold"
    },
    {
        "id": "CH07_SC058",
        "dur": "4.2s",
        "words": 16,
        "text": "lan rồi chở ngược về các cảng tại Thành phố Hồ Chí Minh và Cái Mép.",
        "anatomy": {
            "tier1": "Tuyến kênh Chợ Gạo nhộn nhịp sà lan nối đuôi nhau chở gạo ngược về TP.HCM và cảng Cái Mép (Bà Rịa - Vũng Tàu).",
            "tier2": "Đoàn sà lan thép chở hàng vạn tấn gạo rẽ sóng vượt hành trình đường thủy dài ngày để về cụm cảng nước sâu xuất khẩu.",
            "tier3": "Cú máy bay chậm dọc theo kênh Chợ Gạo theo sau đoàn sà lan (Slow aerial glide following rice barges along Cho Gao canal)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an active aerial view of the Cho Gao canal artery where endless lines of motorized steel barges transport rice northward toward Ho Chi Minh City and Cai Mep international seaport",
        "setting": "the bustling Cho Gao canal corridor in Tien Giang under warm afternoon sun",
        "motion": "Slow aerial glide tracking the northbound rice barge convoys along the canal"
    },
    {
        "id": "CH07_SC059",
        "dur": "3.41s",
        "words": 13,
        "text": "Chặng đường trung chuyển chỉ khoảng hai trăm cây số này đã làm",
        "anatomy": {
            "tier1": "Bản đồ hải trình vận tải nội địa dài 200 km nối từ Cần Thơ về cụm cảng Cái Mép Thị Vải.",
            "tier2": "Quãng đường 200 km đường thủy tiêu tốn thêm nhiên liệu, thời gian neo đậu và hao hụt bốc xếp.",
            "tier3": "Cú máy trượt dọc theo lộ trình 200 km vận chuyển trung chuyển (Tracking shot along 200km transshipment route)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a nautical route map showing the 200-kilometer inland water transport detour from Mekong Delta mills to Cai Mep container terminals with time and fuel metrics displayed",
        "setting": "a marine logistics planning terminal in warm amber lighting",
        "motion": "Slow tracking shot tracing the 200 km detour route on the digital map"
    },
    {
        "id": "CH07_SC060",
        "dur": "3.67s",
        "words": 14,
        "text": "đội thêm từ bảy đến mười đô la cho mỗi tấn gạo xuất khẩu.",
        "anatomy": {
            "tier1": "Hóa đơn chi phí logistics xuất khẩu với dòng phụ phí trung chuyển đường thủy nội địa.",
            "tier2": "Con số đội thêm từ 7 đến 10 USD cho mỗi tấn gạo xuất khẩu hiển thị rõ ràng, làm xói mòn lợi nhuận của doanh nghiệp và nông dân.",
            "tier3": "Cú máy tĩnh trực diện vào con số chi phí đội thêm 7 - 10 USD/tấn (Steady shot on $7 - $10/ton added transshipment cost) cùng text overlay góc trái dưới."
        },
        "overlay": "CHI PHÍ PHÁT SINH: 7 - 10 USD/TẤN",
        "ref": None,
        "subj": "a freight accounting invoice highlighting an additional deadweight cost penalty of 7 to 10 USD per metric ton incurred strictly from multi-step river transshipment detours",
        "setting": "an export freight documentation office in warm natural desk light",
        "motion": "Steady camera shot framing the $7 - $10/ton extra cost line on the invoice"
    },
    {
        "id": "CH07_SC061",
        "dur": "6.56s",
        "words": 25,
        "text": "Vừa chịu sức ép suy giảm dòng chảy từ thượng nguồn, vừa đối mặt với nguy cơ mặn xâm nhập và sụt lún địa chất.",
        "anatomy": {
            "tier1": "Mô hình tổng hợp 3D về các rủi ro vĩ mô của ĐBSCL: Dòng chảy thượng nguồn suy giảm, mặn xâm nhập từ biển và mặt đất lún sụt.",
            "tier2": "Đồng bằng sông Cửu Long nằm ở trung tâm của những lực ép đa chiều từ cả thượng nguồn, hạ lưu và lòng đất.",
            "tier3": "Cú máy xoay chậm 3D bao quát toàn bộ áp lực địa chấn thủy văn (Slow 3D rotational pan around systemic multi-hazard model)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a comprehensive multi-hazard 3D geological model of the Mekong Delta illustrating simultaneous upstream flow reduction, marine salinity intrusion, and underground ground subsidence",
        "setting": "a climate resilience research center in warm amber and terracotta lighting",
        "motion": "Slow 3D rotational pan visualizing the compounding ecological pressures on the delta"
    },
    {
        "id": "CH07_SC062",
        "dur": "6.04s",
        "words": 23,
        "text": "Lại thêm xung đột sinh thái gay gắt ngay trong nội bộ và điểm nghẽn logistics làm suy yếu năng lực cạnh tranh.",
        "anatomy": {
            "tier1": "Hình ảnh tương phản: Bờ đê chia cắt xung đột sinh thái bên cạnh các con tàu kẹt đáy tại luồng sông cạn.",
            "tier2": "Sự kết hợp giữa xung đột nội tại và rào cản hạ tầng khiến nền nông nghiệp lúa gạo truyền thống đứng trước thử thách lịch sử.",
            "tier3": "Cú máy trượt ngang qua bức tranh xung đột và điểm nghẽn hạ tầng (Horizontal tracking shot past ecological conflict and logistics friction)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a compelling editorial collage depicting the dual internal bottlenecks: community water conflict at locked sluices and commercial vessels constrained by shallow estuarine sandbars",
        "setting": "a strategic regional planning display in warm amber tones",
        "motion": "Slow horizontal tracking shot past the dual bottlenecks of ecology and logistics"
    },
    {
        "id": "CH07_SC063",
        "dur": "5.77s",
        "words": 22,
        "text": "Vựa lúa miền Tây dường như đã chạm tới giới hạn chịu đựng cuối cùng của mô hình phát triển truyền thống.",
        "anatomy": {
            "tier1": "Cánh đồng mẫu lớn ĐBSCL lúc hoàng hôn buông xuống với những vệt rạ khô và dòng kênh tĩnh lặng phản chiếu sắc cam đậm.",
            "tier2": "Mô hình thâm canh tăng vụ truyền thống bằng đê bao khép kín đã chạm tới giới hạn chịu đựng sinh thái tối đa.",
            "tier3": "Cú máy bay góc cao bao quát cánh đồng hoàng hôn chạm giới hạn phát triển (High-angle aerial pan over dusk-lit farmland reaching systemic limits)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic wide aerial view of the vast Mekong Delta plains at sunset bathed in deep terracotta and amber light, symbolizing an agricultural model reaching its ultimate ecological limits",
        "setting": "the wide horizon of southern delta farmland under dramatic dusk skies",
        "motion": "High-angle slow aerial pan across the vast dusk-lit agricultural horizon"
    },
    {
        "id": "CH07_SC064",
        "dur": "5.77s",
        "words": 22,
        "text": "Chúng ta không thể tiếp tục dùng những chiếc đê bê tông khô cứng để chống lại quy luật của tự nhiên.",
        "anatomy": {
            "tier1": "Bức tường đê bê tông nứt nẻ đứng trơ trọi bên bờ biển sóng vỗ, chứng minh sự bất lực trước sức mạnh tự nhiên.",
            "tier2": "Những con sóng biển xô bờ, lời nhắc nhở sâu sắc rằng không thể dùng công trình bê tông khô cứng để cưỡng bức quy luật trời đất.",
            "tier3": "Cú máy nâng chậm từ bờ đê bê tông nứt nẻ lên mặt biển bao la (Slow upward tilt from cracked concrete sea-dike toward boundless ocean)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a weathered cracked concrete sea-wall standing solitary against relentless coastal ocean waves, symbolizing the futile attempt to control natural ecological forces with rigid concrete",
        "setting": "a rugged delta shoreline at sunset under warm amber and terracotta light",
        "motion": "Slow upward tilt from the cracked sea-wall toward the boundless ocean horizon"
    },
    {
        "id": "CH07_SC065",
        "dur": "5.51s",
        "words": 21,
        "text": "Càng không thể ép người nông dân phải triệt tiêu sinh kế của nhau vì một mục tiêu duy ý chí.",
        "anatomy": {
            "tier1": "Hình ảnh người nông dân trồng lúa và người nuôi tôm cùng ngồi uống trà trên bờ kênh lúc xế chiều.",
            "tier2": "Ánh mắt chia sẻ và sự thấu hiểu dần thay thế những xung đột cũ, khao khát một mô hình phát triển chung sống hòa thuận.",
            "tier3": "Cú máy đẩy chậm vào cuộc trò chuyện thân tình giữa người trồng lúa và người nuôi tôm (Slow push-in on peaceful tea dialogue between farmers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a peaceful scene of reconciliation where a veteran rice farmer and a shrimp farmer share a pot of hot green tea together on a wooden canal bench at sunset, talking with mutual empathy",
        "setting": "a rustic canal-side veranda in southern Vietnam under warm sunset glow",
        "motion": "Slow push-in shot toward the two farmers sharing tea and mutual understanding"
    },
    {
        "id": "CH07_SC066",
        "dur": "2.89s",
        "words": 11,
        "text": "Một bài toán sinh tử được đặt lên bàn nghị sự",
        "anatomy": {
            "tier1": "Bàn hội nghị cấp cao của Chính phủ với tập hồ sơ quy hoạch phát triển bền vững đồng bằng sông Cửu Long.",
            "tier2": "Bút ký và các tài liệu chiến lược chuyển đổi xanh được đặt trang trọng dưới ánh đèn phòng họp ấm áp.",
            "tier3": "Cú máy đẩy nhanh vào bản tài liệu chiến lược trên bàn hội nghị (Dynamic push-in on government strategic decision dossier)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a prestigious government state room conference table with a prime ministerial dossier titled 'Sustainable & Resilient Development Strategy for the Mekong Delta' open under warm ambient lamps",
        "setting": "a government executive conference room in warm ivory cream and mahogany tones",
        "motion": "Dynamic push-in shot toward the strategic state planning dossier"
    },
    {
        "id": "CH07_SC067",
        "dur": "4.99s",
        "words": 19,
        "text": "Làm sao để giữ vững an ninh lương thực mà không hủy hoại chính mảnh đất nuôi dưỡng mình?",
        "anatomy": {
            "tier1": "Toàn cảnh đồng bằng sông Cửu Long xanh ngút ngàn chân trời, nơi đất trời và dòng sông hòa quyện làm một.",
            "tier2": "Hình ảnh mầm lúa xanh vươn lên từ lớp phù sa màu mỡ dưới ánh nắng bình minh rực rỡ, biểu tượng cho lời giải thuận thiên trong Chương 8.",
            "tier3": "Cú máy bay cao hướng về bình minh rạng rỡ trên đồng bằng sông Cửu Long (Epic upward aerial crane shot toward radiant sunrise over the delta)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a magnificent cinematic aerial sunrise over the vast breathing Mekong Delta, where freshwater channels, lush rice fields, and coastal mangroves coexist harmoniously under golden morning skies",
        "setting": "the glorious expansive delta landscape of southern Vietnam at golden dawn",
        "motion": "Epic ascending aerial crane shot toward the brilliant morning sun over the vast delta"
    }
]

# Generate Markdown Storyboard
md_lines = [
    "# chapter_07_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 7: Gọng Kìm Thủy Văn Và Xung Đột Sinh Thái: Khi Dòng Sông Mẹ Bị Chia Cắt",
    "## Phong cách chủ đạo: Luminous Warm Editorial Illustration (Minh họa báo chí cao cấp, ánh sáng trong trẻo rực rỡ, 100% không gian vật lý đời thực, triệt tiêu hoàn toàn siêu thực và màu đen u ám)",
    "",
    "### 🎨 Hệ màu 60-30-10 (Tuyệt Đối Ấm Áp — Chống Lạnh Lẽo):",
    "- **60% Tông màu nền chủ đạo:** Warm Ivory Cream (`#FAF7EE`), Warm Mekong Dawn & Dusk (`#FFFBEB`), Warm Red Alluvium River Water (`#F3E5AB`). Tuyệt đối không dùng nền xám lạnh, xanh cyan buốt giá hay đen kịt.",
    "- **30% Đường nét & Chủ thể:** Terracotta River Alluvium (`#EA580C`), Ripe Golden Amber (`#F59E0B`), Deep Mangrove Foliage Green (`#047857`), Classical Concrete & Weathered Sluice Wood (`#4B5563`).",
    "- **10% Điểm nhấn dẫn mắt:** Luminous Warm Golden Sunrise Rays (`#D97706`), Warm Moonlight & Lantern Glow at Sluice Gates, Glowing Golden Amber Data Badges.",
    "",
    "---",
    "",
    "### 🛡️ Quy Tắc Kiểm Soát Tuyệt Đối:",
    "1. **Scene ID chuẩn theo chương:** `CH07_SC001` đến `CH07_SC067` (Khớp 100% với `scene_timing_map.json`).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Dòng chính Mekong thượng nguồn, đập thủy điện bậc thang, công trường kênh Phù Nam Techo, ngã ba sông Châu Đốc, bờ sạt lở sông Tiền/Hậu, vườn cây ăn trái Chợ Lách/Cái Bè, vuông tôm bán đảo Cà Mau, cống ngăn mặn Bạc Liêu, cửa biển Định An, kênh Chợ Gạo.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc đúng 13/67 phân cảnh (19.4%) có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. 54 phân cảnh còn lại để `[TEXT OVERLAY]: Không`.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Nhân Vật Dân Sự:**",
    "   - Nông dân trồng lúa, người nuôi tôm, công nhân bốc vác, kỹ sư thủy lợi: Tuyệt đối KHÔNG dùng ảnh tham chiếu nhân tạo, mô tả trực tiếp chân thực trong prompt với nhân chủng học Đông Nam Á.",
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

# Save chapter_07_visual.md
with open("episodes/vu-khi-gao-viet-nam/chapter_07_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_07_visual.md ({len(scenes_data)} scenes)")

# Generate prompts_chapter_07.txt
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

with open("episodes/vu-khi-gao-viet-nam/prompts_chapter_07.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompt_lines).strip() + "\n")

print(f"✅ Generated prompts_chapter_07.txt ({len(scenes_data)} scenes)")
