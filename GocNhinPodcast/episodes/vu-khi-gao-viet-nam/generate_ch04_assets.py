"""
Script to generate both chapter_04_visual.md and prompts_chapter_04.txt
for Episode 'Vũ Khí Lúa Gạo Việt Nam' - Chapter 04.
Strictly adheres to:
- Flow Batch Studio syntax
- Warm Luminous Editorial Palette (#FAF7EE, #F59E0B, #EA580C)
- Selective Lower-Left 25% Rule (~20% text overlay)
- Canonical references: @irri_los_banos_gate.jpg, @marcos_jr.jpg
- Steady camera and static text preservation in video prompts
"""

import re
import json

scenes_data = [
    {
        "id": "CH04_SC001",
        "dur": "5.77s",
        "words": 19,
        "text": "Nửa thế kỷ trước, Philippines từng là kinh đô của khoa học lúa gạo châu Á. Tại vùng Los Baños yên bình",
        "anatomy": {
            "tier1": "Khuôn viên xanh mát của thị trấn học thuật Los Baños dưới chân núi Makiling rực rỡ ánh nắng ban mai ấm áp.",
            "tier2": "Các thửa ruộng thí nghiệm kiểu mẫu với những hàng lúa xanh tốt được đánh số cẩn thận, biểu trưng cho cái nôi nông nghiệp châu Á.",
            "tier3": "Cú máy bay chậm từ sườn núi Makiling xuống thung lũng viện nghiên cứu Los Baños (Slow aerial glide down toward Los Baños agronomy valley)."
        },
        "overlay": None,
        "ref": "irri_los_banos_gate.jpg",
        "subj": "the historic entrance gate and green academic campus of the International Rice Research Institute (IRRI) in Los Baños surrounded by lush palm trees and sunny research paddies",
        "setting": "the peaceful academic valley of Los Baños near Mount Makiling in the morning golden sunlight",
        "motion": "Slow aerial glide down toward the entrance of the agricultural institute bathed in golden morning light"
    },
    {
        "id": "CH04_SC002",
        "dur": "6.04s",
        "words": 23,
        "text": "Viện Nghiên cứu Lúa Quốc tế IRRI được thành lập và trở thành cái nôi khai sinh ra giống lúa thần nông IR8.",
        "anatomy": {
            "tier1": "Cổng chính và tòa nhà viện nghiên cứu IRRI Los Baños xây bằng đá sáng màu mang phong cách kiến trúc thập niên 1960 thanh lịch.",
            "tier2": "Biển tên Viện Nghiên cứu Lúa Quốc tế IRRI bằng đồng sáng loáng, các nhà khoa học nông nghiệp quốc tế áo blouse trắng đang thảo luận bên khay lúa giống.",
            "tier3": "Cú máy tĩnh trực diện vào cổng viện IRRI và bảng tên thành lập thập niên 1960 (Steady shot on IRRI entrance and establishment landmark) cùng text overlay góc trái dưới."
        },
        "overlay": "IRRI - LOS BAÑOS, 1960s",
        "ref": "irri_los_banos_gate.jpg",
        "subj": "the classical 1960s modernist concrete and stone facade of the International Rice Research Institute (IRRI) entrance building with international agricultural scientists in white coats discussing beside sample trays",
        "setting": "the main courtyard of IRRI Los Baños under warm amber tropical sunlight",
        "motion": "Steady camera shot framing the historic agricultural research institute entrance"
    },
    {
        "id": "CH04_SC003",
        "dur": "6.3s",
        "words": 24,
        "text": "Giống lúa kỳ diệu ấy đã tạo nên cuộc cách mạng xanh, cứu hàng trăm triệu người khắp châu lục thoát khỏi nạn đói.",
        "anatomy": {
            "tier1": "Thửa ruộng thí nghiệm trĩu bông lúa giống IR8 đầu tiên với thân lúa thấp cứng cáp, bông dày đặc hạt căng mẩy.",
            "tier2": "Nhà nông học đang nhẹ nhàng nâng bông lúa thần nông IR8 vàng óng, ánh sáng kỳ diệu của cuộc Cách mạng Xanh lan tỏa khắp cánh đồng châu Á.",
            "tier3": "Cú máy tĩnh trực diện vào bông lúa thần nông IR8 đột phá năng suất (Steady shot on Miracle Rice IR8 golden panicle) cùng text overlay góc trái dưới."
        },
        "overlay": "GIỐNG LÚA THẦN NÔNG IR8",
        "ref": None,
        "subj": "a botanical close-up of the legendary Miracle Rice IR8 variety with thick sturdy semi-dwarf stalks and dense golden panicles held gently by an Asian agronomist in field attire",
        "setting": "an IRRI experimental paddy field in Los Baños during the golden Green Revolution era under warm morning sun",
        "motion": "Steady camera shot focusing on the sturdy golden panicle of miracle rice IR8"
    },
    {
        "id": "CH04_SC004",
        "dur": "4.72s",
        "words": 18,
        "text": "Thời điểm đó, các kỹ sư nông nghiệp từ khắp nơi, kể cả Việt Nam hay Thái Lan",
        "anatomy": {
            "tier1": "Giảng đường nông nghiệp ngoài trời rợp bóng cây cổ thụ tại IRRI Los Baños.",
            "tier2": "Đoàn kỹ sư nông nghiệp trẻ từ Việt Nam, Thái Lan và các nước Đông Nam Á chăm chú ghi chép sổ tay nông học.",
            "tier3": "Cú máy trượt ngang qua hàng ghế các kỹ sư nông nghiệp Đông Nam Á đang học tập (Horizontal tracking shot past Asian agronomy trainees)."
        },
        "overlay": None,
        "ref": None,
        "subj": "young Southeast Asian agricultural engineers and agronomists holding field notebooks and magnifying glasses inspecting rice seedlings outdoors",
        "setting": "an open-air IRRI agronomy training pavilion surrounded by lush tropical greenery in warm sunny daylight",
        "motion": "Slow horizontal tracking shot past enthusiastic young agricultural trainees"
    },
    {
        "id": "CH04_SC005",
        "dur": "5.25s",
        "words": 20,
        "text": "đều từng sang Philippines học hỏi kỹ thuật gieo trồng. Thế nhưng, khi bước vào kỷ nguyên hiện đại hóa",
        "anatomy": {
            "tier1": "Thư viện lưu trữ học liệu nông nghiệp IRRI với các dãy kệ sách kỹ thuật canh tác lúa gạo bằng gỗ nâu ấm.",
            "tier2": "Các thế hệ chuyên gia Đông Nam Á chào tạm biệt người thầy Philippines để trở về phát triển quê hương, trong khi chân trời Manila dần chuyển mình sang thập kỷ mới.",
            "tier3": "Cú máy lùi chậm từ hành lang thư viện hướng ra chân trời Manila đang lên đèn ấm áp (Slow pull-back shot toward evolving Manila skyline)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the classical wooden library hallway of IRRI with agronomists carrying research folios looking out toward the distant skyline of expanding Manila under a warm amber sky",
        "setting": "the arched veranda of an academic institute overlooking lush valley and distant city lights at sunset",
        "motion": "Slow pull-back camera shot from the serene academic veranda toward the distant growing metropolis"
    },
    {
        "id": "CH04_SC006",
        "dur": "6.82s",
        "words": 26,
        "text": "Manila lại đưa ra một lựa chọn chiến lược làm thay đổi toàn bộ vận mệnh đất nước. Họ quyết định chọn một lối đi tắt.",
        "anatomy": {
            "tier1": "Bàn hội nghị quy hoạch chiến lược kinh tế quốc gia tại Manila với các bản đồ phát triển đô thị dịch vụ.",
            "tier2": "Các nhà kỹ trị Manila trong trang phục công sở chỉ tay về phía bản đồ quy hoạch khu tài chính dịch vụ, đánh dấu ngã rẽ tách rời nông nghiệp truyền thống.",
            "tier3": "Cú máy đẩy chậm vào mô hình quy hoạch dịch vụ hiện đại trên bàn hội nghị (Slow push-in toward service economy strategic masterplan)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a high-level economic planning boardroom in Manila with government technocrats in barong tagalog shirts reviewing urban development blueprints and financial sector charts",
        "setting": "a prestigious mahogany conference room with large windows overlooking Manila Bay under warm late afternoon sunlight",
        "motion": "Slow cinematic push-in toward the boardroom table showcasing urban transition plans"
    },
    {
        "id": "CH04_SC007",
        "dur": "6.3s",
        "words": 24,
        "text": "Thay vì kiên trì đầu tư cho thủy lợi và đồng ruộng, Philippines dồn toàn lực cho dịch vụ và gia công lắp ráp.",
        "anatomy": {
            "tier1": "Bố cục đối lập chia đôi khung hình: Bên trái là con mương thủy lợi nông thôn khô cạn thiếu bảo dưỡng; Bên phải là khu công nghiệp lắp ráp linh kiện bóng bẩy.",
            "tier2": "Dòng vốn đầu tư công chuyển hướng mạnh mẽ sang các khu chế xuất điện tử và tòa tháp văn phòng dịch vụ.",
            "tier3": "Cú máy trượt ngang từ cánh đồng nông thôn bị bỏ quên sang khu gia công công nghiệp (Horizontal pan from neglected irrigation canal to electronics assembly plant)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a conceptual diptych composition showing a weathered dry rural irrigation gate on one side transitioning into an active high-tech electronics assembly park on the other",
        "setting": "contrasting landscapes of neglected Luzon farmland and thriving metropolitan export processing zones under warm ambient light",
        "motion": "Smooth horizontal tracking pan showing the transition of capital from rural soil to industrial manufacturing"
    },
    {
        "id": "CH04_SC008",
        "dur": "3.15s",
        "words": 12,
        "text": "Họ mở rộng các trung tâm dịch vụ khách hàng từ xa",
        "anatomy": {
            "tier1": "Sàn văn phòng trung tâm chăm sóc khách hàng (BPO Call Center) hiện đại, sáng sủa tại Bonifacio Global City (BGC) hoặc Makati.",
            "tier2": "Hàng trăm nhân viên trẻ Philippines đeo tai nghe headset chuyên nghiệp, chăm chỉ trả lời các cuộc gọi dịch vụ toàn cầu.",
            "tier3": "Cú máy tĩnh trực diện vào sàn văn phòng BPO nhộn nhịp (Steady shot on bustling modern BPO call center floor) cùng text overlay góc trái dưới."
        },
        "overlay": "DỊCH VỤ BPO & KIỀU HỐI",
        "ref": None,
        "subj": "a vast modern business process outsourcing (BPO) call center floor filled with rows of young Filipino operators with headsets speaking into microphones before computer monitors",
        "setting": "a brightly lit corporate high-rise office in Bonifacio Global City Manila with warm ambient interior lighting",
        "motion": "Steady camera shot framing the bustling floor of a major business process outsourcing center"
    },
    {
        "id": "CH04_SC009",
        "dur": "4.46s",
        "words": 17,
        "text": "đẩy mạnh xuất khẩu lao động để thu kiều hối và lắp ráp linh kiện điện tử.",
        "anatomy": {
            "tier1": "Quầy giao dịch kiều hối và ngoại tệ nhộn nhịp tại khu thương mại Manila, kết hợp với dây chuyền lắp ráp vi mạch điện tử.",
            "tier2": "Gia đình người dân vui mừng nhận các tờ kiều hối USD được gửi về từ lao động hải ngoại OFW (Overseas Filipino Workers).",
            "tier3": "Cú máy trượt ngang qua quầy nhận kiều hối và dây chuyền lắp ráp linh kiện (Horizontal tracking shot past remittance counter and microchip assembly lines)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a montage scene featuring a busy Western Union and remittance exchange counter in Manila where families receive remittance envelopes, alongside sterile cleanroom microchip assembly workers",
        "setting": "a lively commercial arcade in Manila filled with warm street-level tropical light",
        "motion": "Slow horizontal tracking shot past family remittance transactions and electronics manufacturing"
    },
    {
        "id": "CH04_SC010",
        "dur": "5.77s",
        "words": 22,
        "text": "Trong tư duy của các nhà kỹ trị thời bấy giờ, trồng trọt là một ngành có giá trị gia tăng thấp.",
        "anatomy": {
            "tier1": "Bàn làm việc của chuyên viên kinh tế với các biểu đồ so sánh biên lợi nhuận GDP giữa dịch vụ BPO và trồng trọt lúa nước.",
            "tier2": "Cây bút đỏ khoanh tròn cột giá trị gia tăng dịch vụ cao gấp nhiều lần so với ngành trồng lúa truyền thống.",
            "tier3": "Cú máy đẩy chậm vào biểu đồ so sánh tỷ suất lợi nhuận ngành (Slow push-in on sector value-added economic chart)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an economic analysis report on a polished desk displaying comparative bar charts showing high margin service revenue towering over low margin agricultural rice yields",
        "setting": "a government ministry office overlooking Manila financial district under warm golden afternoon light",
        "motion": "Slow push-in toward the comparative economic report highlighting sector profit margins"
    },
    {
        "id": "CH04_SC011",
        "dur": "4.72s",
        "words": 18,
        "text": "Họ tin rằng trong một thế giới phẳng, đất nước chỉ cần kiếm ngoại tệ từ dịch vụ",
        "anatomy": {
            "tier1": "Văn phòng thương mại toàn cầu nhìn ra toàn cảnh vịnh Manila với những cánh buồm và tàu buôn tấp nập.",
            "tier2": "Các nhà kinh tế học thời kỳ toàn cầu hóa nhìn vào quả địa cầu và dòng chảy kiều hối ngoại tệ đô la dồi dào.",
            "tier3": "Cú máy lia góc rộng từ quả địa cầu hướng ra chân trời vịnh Manila ngập tràn ánh nắng (Wide cinematic pan from desk globe toward sunlit Manila Bay)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a panoramic view of a modern Manila executive office with a vintage brass desk globe in foreground and floor-to-ceiling glass windows framing Manila Bay cargo ships",
        "setting": "a high-rise corner office in Manila bathed in luminous warm afternoon sun",
        "motion": "Slow pan from the brass desktop globe toward the busy harbor shipping lanes"
    },
    {
        "id": "CH04_SC012",
        "dur": "3.41s",
        "words": 13,
        "text": "rồi dùng số tiền đó để mua gạo giá rẻ từ láng giềng.",
        "anatomy": {
            "tier1": "Cầu cảng hàng hóa Manila với những bao tải gạo nhập khẩu từ các nước láng giềng Đông Nam Á xếp gọn trên pallet gỗ.",
            "tier2": "Tập hóa đơn tín dụng ngoại thương USD thanh toán cho các chuyến tàu chở gạo giá rẻ cập bến.",
            "tier3": "Cú máy nâng chậm từ hóa đơn thương mại lên cần cẩu bốc dỡ bao gạo (Slow tilt-up from trade invoice to dockside cargo crane)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a commercial dockside scene at the Port of Manila with stacks of woven burlap rice sacks being unloaded from a regional cargo vessel beside commercial trade manifests",
        "setting": "the bustling Port of Manila pier under warm amber afternoon skies",
        "motion": "Slow upward tilt from cargo trade invoices toward dockside cranes lifting rice pallets"
    },
    {
        "id": "CH04_SC013",
        "dur": "5.25s",
        "words": 20,
        "text": "Đó là một giả định nghe có vẻ rất hợp lý trên các bản vẽ kinh tế học bàn giấy.",
        "anatomy": {
            "tier1": "Mặt bàn kính hiện đại với bản vẽ mô hình cân đối vĩ mô hoàn hảo: Kiều hối và dịch vụ bù đắp hoàn toàn nhập khẩu lương thực.",
            "tier2": "Mô hình lý thuyết trông vô cùng mượt mà và thuyết phục trên các trang giấy phân tích kinh tế vĩ mô.",
            "tier3": "Cú máy đẩy chậm vào các đường cong cung cầu lý thuyết hoàn hảo trên giấy (Slow push-in on clean theoretical supply-demand curves)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a clean theoretical macroeconomic blueprint and textbook diagrams illustrating comparative advantage and frictionless global food imports on a sleek glass conference table",
        "setting": "an academic seminar room in Manila in soft warm ambient morning light",
        "motion": "Slow push-in shot framing the pristine theoretical economic diagrams on paper"
    },
    {
        "id": "CH04_SC014",
        "dur": "3.41s",
        "words": 13,
        "text": "Thế nhưng, các quy luật phát triển chưa bao giờ dung thứ cho",
        "anatomy": {
            "tier1": "Bức tường gạch rêu phong của một trạm bơm thủy lợi cũ kỹ ở vùng nông thôn đảo Luzon nứt nẻ qua năm tháng.",
            "tier2": "Bánh đà cơ khí hoen gỉ nằm im lìm giữa kênh dẫn nước cạn đáy, cảnh báo sự nghiệt ngã của quy luật kinh tế vật chất.",
            "tier3": "Cú máy trượt ngang qua những vết rạn nứt trên trạm bơm thủy lợi cũ (Horizontal tracking shot past cracked concrete of neglected pump house)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a weathered rustic concrete irrigation pump house in rural Luzon with rusted metal gears and cracked dried canal beds overgrown with tropical weeds",
        "setting": "a forgotten agricultural countryside in Central Luzon under warm dry late-day sunlight",
        "motion": "Slow tracking shot across the weathered cracks of the silent concrete irrigation gate"
    },
    {
        "id": "CH04_SC015",
        "dur": "3.67s",
        "words": 14,
        "text": "những nền kinh tế bỏ quên nền móng sản xuất vật chất cốt lõi.",
        "anatomy": {
            "tier1": "Một cánh đồng lúa Luzon khô cằn nứt nẻ vì thiếu nước tưới tiêu trong mùa khô.",
            "tier2": "Chiếc cày gỗ và đôi ủng cao su của người nông dân đặt trơ trọi bên bờ ruộng hoang vắng.",
            "tier3": "Cú máy hạ thấp góc nhìn sát mặt đất nứt nẻ nhìn về phía xa (Low-angle slow tracking shot along parched cracked paddy soil)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a desolate cracked clay rice field during the dry season with an abandoned wooden plow standing solitary against a vast warm hazy horizon",
        "setting": "drought-affected rural farmland in northern Philippines under warm dusty afternoon light",
        "motion": "Low-angle slow pan across the parched soil toward the lonely wooden plow"
    },
    {
        "id": "CH04_SC016",
        "dur": "3.94s",
        "words": 15,
        "text": "Khái niệm kinh tế học gọi đây là chiếc bẫy phi công nghiệp hóa non.",
        "anatomy": {
            "tier1": "Màn hình đồ họa nghiên cứu phát triển kinh tế tại Viện Nghiên cứu Phát triển Philippines (PIDS).",
            "tier2": "Sơ đồ chiếc bẫy: Bỏ qua nấc thang tích lũy nông nghiệp và công nghiệp chế tạo nền tảng để nhảy vọt sang dịch vụ.",
            "tier3": "Cú máy tĩnh trực diện vào sơ đồ Bẫy Phi Công Nghiệp Hóa Non (Steady shot on Premature Deindustrialization trap diagram) cùng text overlay góc trái dưới."
        },
        "overlay": "BẪY PHI CÔNG NGHIỆP HÓA NON",
        "ref": None,
        "subj": "an analytical graphic flowchart showing the structural trap of premature deindustrialization: skipping agricultural foundation and core manufacturing directly into consumer services",
        "setting": "an economic research institute briefing room under warm neutral ambient lighting",
        "motion": "Steady camera shot framing the Premature Deindustrialization structural trap infographic"
    },
    {
        "id": "CH04_SC017",
        "dur": "6.82s",
        "words": 26,
        "text": "Công nghiệp chế tạo nội địa chưa kịp hình thành chuỗi cung ứng phụ trợ, thì nông nghiệp đã bị rút cạn nguồn lực đầu tư.",
        "anatomy": {
            "tier1": "Một xưởng cơ khí chế tạo máy nông cụ nhỏ vắng bóng đơn hàng tại ngoại ô Manila.",
            "tier2": "Người thợ cơ khí nhìn dãy máy tiện đứng yên, trong khi ngân sách đầu tư công cho nông nghiệp bị cắt giảm qua các thời kỳ.",
            "tier3": "Cú máy trượt ngang qua những cỗ máy tiện nằm bất động trong xưởng cơ khí (Horizontal tracking shot past idle lathes in mechanical workshop)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a quiet small-scale mechanical tool and machine workshop on the outskirts of Manila with idle metal lathes, spare tractor parts, and empty tool racks",
        "setting": "an industrial workshop interior lit by warm golden rays streaming through clerestory windows",
        "motion": "Slow horizontal tracking shot past silent mechanical machinery and dusty tractor spare parts"
    },
    {
        "id": "CH04_SC018",
        "dur": "6.04s",
        "words": 23,
        "text": "Hạ tầng thủy lợi nông thôn bị tư nhân hóa và xuống cấp nghiêm trọng qua nhiều thập kỷ thiếu vốn ngân sách.",
        "anatomy": {
            "tier1": "Một con kênh thủy lợi bằng bê tông đúc thời kỳ 1970 tại vùng Tarlac hoặc Nueva Ecija bị bồi lắng phù sa và cỏ dại phủ kín.",
            "tier2": "Trạm điều tiết nước tư nhân hóa với biển thu phí dịch vụ hoen gỉ, cống xả nước bị kẹt van không thể vận hành bình thường.",
            "tier3": "Cú máy đẩy chậm dọc theo lòng kênh bê tông cũ nứt nẻ và bồi lắng (Slow push-in along weathered cracked concrete irrigation canal)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dilapidated concrete rural canal system in Nueva Ecija choked with silt, tropical grass, and weathered rusty manual sluice gates",
        "setting": "a neglected provincial irrigation branch in Central Luzon under warm hazy tropical daylight",
        "motion": "Slow forward tracking shot along the silted concrete canal toward the jammed sluice gate"
    },
    {
        "id": "CH04_SC019",
        "dur": "6.56s",
        "words": 25,
        "text": "Đất đai canh tác bị phân mảnh manh mún, khiến người nông dân hoàn toàn bất lực trong việc đưa máy móc vào đồng ruộng.",
        "anatomy": {
            "tier1": "Cánh đồng lúa nhìn từ trên cao bị chia cắt thành hàng ngàn ô ruộng nhỏ xíu, bờ bao ngoằn ngoèo manh mún.",
            "tier2": "Người nông dân Philippines dắt trâu cày thủ công trên ô ruộng hẹp, không thể đưa máy cày lớn hay máy gặt đập liên hợp vào làm việc.",
            "tier3": "Cú máy bay góc cao (high-angle pan) cho thấy sự phân mảnh manh mún của ruộng đồng (High-angle pan over fragmented puzzle-like smallholder rice plots)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a high-angle view of severely fragmented smallholder rice paddies forming an irregular patchwork of tiny plots divided by narrow earthen dikes, where a solitary farmer works with a water buffalo",
        "setting": "a fragmented farming valley in the Philippine provinces under warm morning sun",
        "motion": "High-angle slow pan showing the patchwork of tiny fragmented family farm plots"
    },
    {
        "id": "CH04_SC020",
        "dur": "4.99s",
        "words": 19,
        "text": "Năng suất lúa của Philippines giẫm chân tại chỗ dưới bốn tấn trên một héc ta suốt nhiều năm",
        "anatomy": {
            "tier1": "Bảng thống kê năng suất lúa bình quân các vụ mùa của Cục Thống kê Philippines (PSA).",
            "tier2": "Đường đồ thị biểu diễn năng suất nằm ngang phẳng lì dưới mức 4.0 tấn/ha qua nhiều thập kỷ.",
            "tier3": "Cú máy tĩnh trực diện vào con số năng suất dưới 4 tấn/ha giẫm chân tại chỗ (Steady shot on < 4.0 tons/ha yield stagnation indicator) cùng text overlay góc trái dưới."
        },
        "overlay": "NĂNG SUẤT LÚA: < 4 TẤN/HA",
        "ref": None,
        "subj": "an agronomic performance chart from the Philippine Statistics Authority showing an unmoving flat line of average palay rice yields hovering stubbornly below 4.0 metric tons per hectare",
        "setting": "an agricultural data review office under warm ambient indoor lighting",
        "motion": "Steady camera shot framing the stagnant agricultural yield data display"
    },
    {
        "id": "CH04_SC021",
        "dur": "2.62s",
        "words": 10,
        "text": "chỉ bằng hơn một nửa các cánh đồng miền Tây.",
        "anatomy": {
            "tier1": "Biểu đồ so sánh trực quan cột kép: Cột năng suất lúa Philippines (dưới 4 tấn/ha) đặt cạnh cột năng suất lúa ĐBSCL Việt Nam (hơn 7 tấn/ha).",
            "tier2": "Khoảng chênh lệch năng suất gần gấp đôi thể hiện sự vượt trội của hệ thống canh tác cơ giới hóa và đê bao khép kín.",
            "tier3": "Cú máy trượt ngang so sánh hai cột năng suất lúa (Horizontal tracking pan comparing comparative yield pillars)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a comparative agronomic dual-bar chart showing Philippine rice productivity at 3.9 tons/ha directly beside Vietnam Mekong Delta peak harvest yield at 7.5 tons/ha",
        "setting": "a modern comparative agricultural research workspace lit by warm morning rays",
        "motion": "Smooth horizontal pan across the dual-pillar productivity comparison"
    },
    {
        "id": "CH04_SC022",
        "dur": "6.56s",
        "words": 25,
        "text": "Trong khi năng lực sản xuất đứng yên, quy mô dân số của họ lại tăng vọt lên hơn một trăm mười lăm triệu người.",
        "anatomy": {
            "tier1": "Quang cảnh đại lộ EDSA hoặc ngã tư đô thị sầm uất tại vùng đô thị Metro Manila với dòng người và xe jeepney đông đúc.",
            "tier2": "Biểu đồ đường dốc đứng thể hiện quy mô dân số Philippines vượt mốc 115 triệu người, tạo nên áp lực tiêu thụ lương thực khổng lồ.",
            "tier3": "Cú máy tĩnh trực diện vào con số dân số vượt 115 triệu người trên nền đô thị Manila sôi động (Steady shot on >115 million population milestone) cùng text overlay góc trái dưới."
        },
        "overlay": "DÂN SỐ: > 115 TRIỆU NGƯỜI",
        "ref": None,
        "subj": "a vibrant panoramic street scene of Metro Manila along EDSA filled with colorful jeepneys, commuters, and pedestrian footbridges set against high-rise residential towers",
        "setting": "the bustling urban core of Metro Manila under bright warm tropical midday sun",
        "motion": "Steady camera shot capturing the dense urban vibrancy of Metro Manila"
    },
    {
        "id": "CH04_SC023",
        "dur": "6.3s",
        "words": 24,
        "text": "Khoảng cách giữa sản lượng nội địa và nhu cầu tiêu thụ thực tế ngày càng giãn rộng như một vết nứt không đáy.",
        "anatomy": {
            "tier1": "Mô hình đồ họa phân tích cân đối cung cầu lương thực quốc gia với hai đường đồ thị tách xa nhau.",
            "tier2": "Đường cầu tiêu thụ tăng vọt trong khi đường cung nội địa đi ngang, tạo ra một hố sâu thâm hụt hàng triệu tấn gạo mỗi năm.",
            "tier3": "Cú máy đẩy chậm vào khoảng trống chênh lệch cung cầu lương thực (Slow push-in on widening food deficit gap)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a macroeconomic balance graphic showing the widening gap between domestic palay harvest volume and skyrocketing national rice consumption demand",
        "setting": "a national food logistics dashboard interface in warm amber and warm ivory colors",
        "motion": "Slow push-in camera movement toward the widening food deficit divergence"
    },
    {
        "id": "CH04_SC024",
        "dur": "6.04s",
        "words": 23,
        "text": "Và điều gì phải đến đã đến. Philippines dần trượt dài và biến thành quốc gia nhập khẩu gạo lớn nhất hành tinh.",
        "anatomy": {
            "tier1": "Bản đồ thương mại hàng hải quốc tế với các hải trình nhập khẩu ngũ cốc toàn cầu hướng về quần đảo Philippines.",
            "tier2": "Biểu tượng cờ Philippines nằm ở vị trí số một trên bảng xếp hạng các nước nhập khẩu gạo thế giới của Bộ Nông nghiệp Hoa Kỳ (USDA).",
            "tier3": "Cú máy tĩnh trực diện vào bảng xếp hạng quốc gia nhập khẩu gạo số 1 thế giới (Steady shot on World No. 1 Rice Importer ranking)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a global maritime agricultural trade map with glowing shipping routes converging from major Asian river deltas into the Philippine archipelago, highlighting its status as the top global buyer",
        "setting": "an international grain trade monitoring terminal in warm editorial amber tones",
        "motion": "Slow cinematic glide across the global maritime grain trade convergence map"
    },
    {
        "id": "CH04_SC025",
        "dur": "3.67s",
        "words": 14,
        "text": "Mỗi năm, chính phủ nước này phải gom từ ba phẩy tám đến gần",
        "anatomy": {
            "tier1": "Khu cảng quốc tế Manila với dãy cần cẩu bốc dỡ hoạt động liên tục đón các tàu chở hàng lớn cập bến.",
            "tier2": "Các sĩ quan hải quan và kiểm dịch thực vật Philippines kiểm tra vận đơn các lô hàng gạo nhập khẩu quy mô hàng triệu tấn.",
            "tier3": "Cú máy trượt ngang qua mép cảng biển với các tàu chở hàng đang neo đậu (Horizontal tracking shot along busy commercial pier)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the commercial quayside of Manila Harbor with harbor tugs guiding a massive bulk carrier loaded with bagged rice toward the unloading berth",
        "setting": "Manila South Harbor waters bathed in warm golden afternoon reflection",
        "motion": "Smooth horizontal tracking shot along the quayside observing inbound bulk cargo ships"
    },
    {
        "id": "CH04_SC026",
        "dur": "3.67s",
        "words": 14,
        "text": "bốn phẩy năm triệu tấn gạo ngoại để bù đắp khoảng trống thiếu hụt.",
        "anatomy": {
            "tier1": "Bên trong kho ngoại quan cảng biển Manila với những chồng bao tải gạo nhập khẩu cao ngất tới trần nhà.",
            "tier2": "Bảng tổng kết nhập khẩu thường niên xác nhận con số khổng lồ từ 3.8 đến 4.5 triệu tấn gạo mỗi năm để nuôi sống người dân.",
            "tier3": "Cú máy tĩnh trực diện vào con số nhập khẩu 3.8 - 4.5 triệu tấn/năm (Steady shot on 3.8 - 4.5 million tons import figure) cùng text overlay góc trái dưới."
        },
        "overlay": "NHẬP KHẨU: 3,8 - 4,5 TRIỆU TẤN/NĂM",
        "ref": None,
        "subj": "a towering wall of stacked white woven rice bags inside a vast bonded port warehouse in Manila with forklift operators transporting wooden pallets of imported grain",
        "setting": "a cavernous port logistics warehouse illuminated by warm ambient skylights",
        "motion": "Steady camera shot framing the massive stacks of imported rice sacks"
    },
    {
        "id": "CH04_SC027",
        "dur": "6.04s",
        "words": 23,
        "text": "Trong số đó, hơn tám mươi phần trăm tổng lượng gạo nhập khẩu đều phải mua từ các cánh đồng của Việt Nam.",
        "anatomy": {
            "tier1": "Các bao gạo xuất khẩu in thương hiệu Việt Nam (Vietnamese White Rice 5% Broken / Jasmine Rice) xếp tràn ngập cầu cảng Manila.",
            "tier2": "Biểu đồ tròn cơ cấu nguồn cung gạo của Philippines hiển thị thị phần áp đảo trên 80% thuộc về Việt Nam.",
            "tier3": "Cú máy tĩnh trực diện vào con số thị phần >80% gạo nhập từ Việt Nam (Steady shot on >80% import share from Vietnam) cùng text overlay góc trái dưới."
        },
        "overlay": "> 80% NHẬP TỪ VIỆT NAM",
        "ref": None,
        "subj": "a focused view of stacked 50kg rice bags clearly stenciled with Vietnamese agricultural export marks being inspected by Manila port authorities beside an editorial pie chart showing over 80 percent Vietnam supply share",
        "setting": "the cargo distribution apron of Manila Harbor under warm sunny skies",
        "motion": "Steady camera shot framing the Vietnamese rice sacks and dominant market share graphic"
    },
    {
        "id": "CH04_SC028",
        "dur": "2.89s",
        "words": 11,
        "text": "Từ một người thầy dạy cả châu Á cách trồng lúa",
        "anatomy": {
            "tier1": "Bức ảnh kỷ niệm lịch sử thập niên 1960 của IRRI Los Baños lồng trong khung gỗ trang trọng treo trên tường.",
            "tier2": "Hình ảnh nhà khoa học Philippines từng hướng dẫn kỹ thuật canh tác cho bạn bè quốc tế trong thời hoàng kim của nông nghiệp.",
            "tier3": "Cú máy đẩy chậm vào bức tranh lịch sử người thầy lúa gạo châu Á (Slow push-in on archival portrait of Asian agricultural leadership)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a framed vintage black-and-white archival photograph hanging on a warm paneled wall depicting Filipino agronomists in the 1960s teaching visiting Asian scholars in a lush test paddy",
        "setting": "an executive heritage gallery inside an agronomic institution under warm gallery spot lighting",
        "motion": "Slow push-in toward the historic framed photograph of agricultural mentorship"
    },
    {
        "id": "CH04_SC029",
        "dur": "4.46s",
        "words": 17,
        "text": "Philippines đã biến thành con nợ lương thực phụ thuộc hoàn toàn vào nguồn cung bên ngoài.",
        "anatomy": {
            "tier1": "Cửa biển Manila với bóng con tàu hàng chở gạo nước ngoài lừng lững tiến vào luồng hàng hải.",
            "tier2": "Bóng dáng vịnh Manila lúc hoàng hôn với hình ảnh ẩn dụ về sự lệ thuộc hoàn toàn vào chuỗi logistics đường biển của láng giềng.",
            "tier3": "Cú máy lùi chậm từ bờ kè đá hướng ra con tàu chở gạo đang tiến vào cảng (Slow pull-back from harbor sea wall toward inbound foreign rice ship)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a silhouette of a massive cargo freighter carrying foreign rice entering the Manila breakwater against a glowing amber and dusty rose sunset sky",
        "setting": "the maritime entrance of Manila Bay with gentle ocean swells in warm sunset hues",
        "motion": "Slow pull-back camera shot framing the solitary foreign grain freighter entering the harbor"
    },
    {
        "id": "CH04_SC030",
        "dur": "6.3s",
        "words": 24,
        "text": "Ảo tưởng về việc dùng ngoại tệ dịch vụ để mua sự no ấm đã chính thức sụp đổ vào mùa hè năm 2023.",
        "anatomy": {
            "tier1": "Mặt đường phố Manila bốc hơi nóng mùa hè tháng 7 năm 2023 dưới ánh nắng chói chang.",
            "tier2": "Các tờ nhật báo Philippines giật tít lớn về cuộc khủng hoảng giá lương thực toàn cầu và nguy cơ đứt gãy nguồn cung lúa gạo.",
            "tier3": "Cú máy hạ thấp lia qua sạp báo với những dòng tít khủng hoảng lương thực (Low-angle tracking pan across Manila newspaper kiosk headlines)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a sidewalk newspaper stand in downtown Manila displaying prominent local headlines about the 2023 global food crisis and escalating rice prices under a warm sunlit awning",
        "setting": "a busy street corner in Quiapo Manila with warm tropical daylight",
        "motion": "Low-angle smooth tracking pan across the urgent front-page newspaper headlines"
    },
    {
        "id": "CH04_SC031",
        "dur": "2.89s",
        "words": 11,
        "text": "Khi Ấn Độ bất ngờ ban hành lệnh cấm xuất khẩu",
        "anatomy": {
            "tier1": "Bản công điện khẩn của Tổng cục Ngoại thương Ấn Độ (DGFT) ban hành ngày 20/7/2023 cấm xuất khẩu gạo trắng non-basmati.",
            "tier2": "Dấu mộc đỏ thông tri cấm xuất khẩu lập tức làm đóng băng các cảng xuất khẩu gạo lớn của Ấn Độ.",
            "tier3": "Cú máy đẩy nhanh vào văn bản cấm xuất khẩu của Ấn Độ (Dynamic push-in on Indian rice export restriction decree)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an official government gazette document with red circular seal from India Directorate General of Foreign Trade declaring an immediate export ban on non-basmati white rice",
        "setting": "an international commodity trade desk illuminated by warm desk lamps",
        "motion": "Dynamic push-in shot focusing on the urgent official export prohibition decree"
    },
    {
        "id": "CH04_SC032",
        "dur": "6.82s",
        "words": 26,
        "text": "thị trường lúa gạo thế giới lập tức rơi vào một cơn địa chấn khan hiếm. Giá gạo quốc tế tăng vọt lên mức đỉnh điểm",
        "anatomy": {
            "tier1": "Sàn giao dịch ngũ cốc quốc tế với bảng điện tử giá gạo thế giới nhảy vọt dựng đứng.",
            "tier2": "Chỉ số giá gạo quốc tế vượt mốc 650 USD/tấn, cao nhất trong vòng 15 năm, tạo nên làn sóng chấn động toàn cầu.",
            "tier3": "Cú máy trượt nhanh theo đường cong giá gạo tăng dựng đứng (Dynamic upward tilt tracking skyrocketing global rice price curve)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dynamic international grain trading screen displaying a steep vertical price surge curve for 5% broken white rice climbing past 650 USD per metric ton amid flashing ticker numbers",
        "setting": "a modern financial market trading floor in warm amber and cream tones",
        "motion": "Dynamic upward tilt tracking the steep ascent of the global rice commodity price chart"
    },
    {
        "id": "CH04_SC033",
        "dur": "4.46s",
        "words": 17,
        "text": "dội thẳng làn sóng lạm phát thực phẩm vượt ngưỡng tám phần trăm vào xã hội Philippines.",
        "anatomy": {
            "tier1": "Chợ dân sinh truyền thống Divisoria tại Manila với bảng giá gạo tăng vọt từng ngày.",
            "tier2": "Biểu đồ lạm phát lương thực của Philippines vượt ngưỡng 8% đè nặng lên chi tiêu hàng ngày của các hộ gia đình bình dân.",
            "tier3": "Cú máy tĩnh trực diện vào con số lạm phát thực phẩm vượt 8% (Steady shot on food inflation >8% economic metric) cùng text overlay góc trái dưới."
        },
        "overlay": "LẠM PHÁT THỰC PHẨM > 8%",
        "ref": None,
        "subj": "a bustling public wet market in Divisoria Manila where chalk price boards on rice bins show sharp price increases beside an editorial infographic indicating national food inflation exceeding 8 percent",
        "setting": "a lively traditional market arcade in Manila under warm diffused tropical light",
        "motion": "Steady camera shot framing the market grain stalls and inflation metric display"
    },
    {
        "id": "CH04_SC034",
        "dur": "3.67s",
        "words": 14,
        "text": "Toàn bộ thặng dư ngoại tệ mà hàng triệu lao động gửi về từ",
        "anatomy": {
            "tier1": "Bàn làm việc của một gia đình Manila với phong bì tiền kiều hối gửi về từ Trung Đông hoặc châu Âu.",
            "tier2": "Số tiền kiều hối mồ hôi nước mắt của người thân ở nước ngoài được trải trên bàn cùng các hóa đơn chi tiêu sinh hoạt.",
            "tier3": "Cú máy cận cảnh phong bì kiều hối OFW bên cạnh cuốn sổ chi tiêu gia đình (Close-up shot of remittance envelope beside household ledger)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a wooden dining table in a modest Manila home with an Overseas Filipino Worker (OFW) remittance envelope, foreign bank notes, and a handwritten household grocery ledger",
        "setting": "a cozy Filipino living room bathed in warm afternoon sunlight through louvered windows",
        "motion": "Slow push-in toward the remittance envelope and family budget records"
    },
    {
        "id": "CH04_SC035",
        "dur": "3.67s",
        "words": 14,
        "text": "nước ngoài bị thiêu rụi bởi hóa đơn nhập khẩu lương thực đắt đỏ.",
        "anatomy": {
            "tier1": "Hóa đơn thanh toán nhập khẩu gạo quốc gia bằng đồng USD với những con số chi phí tăng gấp rưỡi.",
            "tier2": "Hình ảnh ẩn dụ: Dòng kiều hối ngoại tệ bị ngốn trọn bởi chi phí mua gạo đắt đỏ từ thị trường quốc tế.",
            "tier3": "Cú máy đẩy chậm vào con số chi phí nhập khẩu lương thực khổng lồ (Slow push-in on surging national food import expenditure)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a government central bank ledger showing foreign exchange reserves being drawn down heavily to pay for soaring international food import invoices",
        "setting": "a treasury accounting office under warm interior desk lighting",
        "motion": "Slow push-in shot framing the steep food import billing balances"
    },
    {
        "id": "CH04_SC036",
        "dur": "6.82s",
        "words": 26,
        "text": "Tại thủ đô Manila, người dân nghèo phải xếp hàng dài dưới nắng gắt chỉ để chờ mua từng túi gạo trợ giá của chính phủ.",
        "anatomy": {
            "tier1": "Đường phố ngoại ô Manila dưới ánh nắng trưa vàng rực, bóng các mái tôn che nắng đơn sơ.",
            "tier2": "Hàng trăm người dân kiên nhẫn cầm túi vải và thẻ căn cước xếp hàng dài chờ đến lượt mua gạo trợ giá của Cơ quan Lương thực Quốc gia (NFA).",
            "tier3": "Cú máy trượt ngang chậm theo dòng người xếp hàng mua gạo trợ giá (Slow horizontal tracking shot along queue of citizens waiting for subsidized rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a long orderly queue of local Manila residents holding cloth bags and national ID cards waiting patiently under a sunlit covered street canopy outside a National Food Authority subsidized rice depot",
        "setting": "a sunlit community plaza in suburban Manila under warm bright midday sun",
        "motion": "Slow horizontal tracking shot along the patient queue of citizens at the rice depot"
    },
    {
        "id": "CH04_SC037",
        "dur": "5.77s",
        "words": 22,
        "text": "Các kệ hàng trong siêu thị bị vét rỗng, giới tiểu thương đóng cửa vì không thể chịu nổi đà tăng giá.",
        "anatomy": {
            "tier1": "Dãy kệ để gạo trong một siêu thị hoặc cửa hàng bách hóa Manila với các thùng chứa gạo trống trơn.",
            "tier2": "Tấm biển thông báo hết hàng tạm thời bằng tiếng Anh và Tagalog; bên ngoài các cửa hàng gạo nhỏ hạ cửa cuốn vì giá nhập quá cao.",
            "tier3": "Cú máy trượt ngang qua dãy kệ gạo trống trơn trong siêu thị (Horizontal tracking shot past empty grocery store rice shelves)."
        },
        "overlay": None,
        "ref": None,
        "subj": "empty wooden display shelves and cleared plastic grain bins inside a neighborhood Manila grocery with small polite signs reading 'Out of Stock' under warm retail lighting",
        "setting": "a neighborhood convenience grocery interior in Manila with warm ambient lamps",
        "motion": "Smooth horizontal tracking shot past empty store shelves and out-of-stock signs"
    },
    {
        "id": "CH04_SC038",
        "dur": "4.99s",
        "words": 19,
        "text": "Tổng thống Philippines phải ban hành Sắc lệnh khẩn cấp số 39 để áp giá trần bán lẻ gạo",
        "anatomy": {
            "tier1": "Phòng khánh tiết trang trọng của Cung điện Malacañang với rèm lụa và quốc kỳ Philippines.",
            "tier2": "Tổng thống Ferdinand Marcos Jr. ký ban hành Sắc lệnh khẩn cấp số 39 áp giá trần bán lẻ gạo (Executive Order No. 39).",
            "tier3": "Cú máy tĩnh trực diện vào Tổng thống Marcos Jr. ký Sắc lệnh số 39 (Steady shot on President Marcos Jr. signing Executive Order No. 39) cùng text overlay góc trái dưới."
        },
        "overlay": "SẮC LỆNH KHẨN CẤP SỐ 39",
        "ref": "marcos_jr.jpg",
        "subj": "Philippine President Ferdinand Marcos Jr. seated at an executive mahogany desk in Malacañang Palace signing official documents for Executive Order No. 39 on rice price ceilings beside government officials",
        "setting": "the state conference hall of Malacañang Palace Manila with rich warm wood paneling and warm interior chandelier light",
        "motion": "Steady camera shot framing the President signing the executive price ceiling order"
    },
    {
        "id": "CH04_SC039",
        "dur": "2.89s",
        "words": 11,
        "text": "nhằm ngăn chặn nguy cơ bùng phát bất ổn xã hội.",
        "anatomy": {
            "tier1": "Tấm áp phích thông báo giá trần gạo 41-45 peso/kg dán tại các quầy chợ Manila do chính quyền niêm yết.",
            "tier2": "Lực lượng thanh tra thương mại kiểm tra việc niêm yết giá bán, giữ gìn trật tự và ổn định tâm lý thị trường.",
            "tier3": "Cú máy trượt ngang qua tấm áp phích giá trần chính phủ niêm yết (Horizontal tracking shot past official price cap notice board)."
        },
        "overlay": None,
        "ref": "marcos_jr.jpg",
        "subj": "government market inspection officers in formal uniforms verifying official retail price ceiling notices posted at commercial grain stalls to ensure social stability",
        "setting": "a sunlit public marketplace in Metro Manila under warm morning canopy light",
        "motion": "Slow horizontal tracking shot past official price cap inspection in the market"
    },
    {
        "id": "CH04_SC040",
        "dur": "6.82s",
        "words": 26,
        "text": "Không một tòa nhà văn phòng hiện đại nào có thể che chở cho một quốc gia khi nguồn lương thực thiết yếu bị gián đoạn.",
        "anatomy": {
            "tier1": "Góc nhìn ngước nhìn lên các tòa tháp chọc trời bọc kính tráng lệ tại Bonifacio Global City (BGC) hoặc Makati dưới bầu trời chiều vàng rực.",
            "tier2": "Dưới chân tòa tháp hiện đại là nhịp sống thực tế của người dân đang lo toan từng bữa ăn, khắc họa rõ nét chân lý về an ninh lương thực.",
            "tier3": "Cú máy ngước lên (low-angle upward tilt) từ mặt đường lên đỉnh các tòa tháp kính tài chính (Low-angle upward tilt from street level to gleaming financial skyscrapers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic low-angle perspective looking up at gleaming modern glass-and-steel skyscrapers of Bonifacio Global City Manila reflecting warm amber sunset light, with bustling city life at street level below",
        "setting": "the financial district of Bonifacio Global City Manila during warm golden hour",
        "motion": "Slow low-angle upward tilt from pedestrian street level to soaring modern skyscrapers"
    },
    {
        "id": "CH04_SC041",
        "dur": "6.82s",
        "words": 26,
        "text": "Ngay trong những ngày tháng căng thẳng nhất ấy, các phái đoàn đàm phán cấp cao của Manila đã phải khẩn cấp bay sang Hà Nội.",
        "anatomy": {
            "tier1": "Phòng khánh tiết Nhà khách Chính phủ hoặc Bộ Nông nghiệp tại Hà Nội với cờ hai nước Việt Nam và Philippines.",
            "tier2": "Phái đoàn đàm phán cấp cao của Manila bước vào phòng họp bắt tay các đại diện chính phủ Việt Nam trong không khí khẩn trương, hữu nghị.",
            "tier3": "Cú máy trượt ngang qua bàn đàm phán ngoại giao giữa hai phái đoàn (Horizontal tracking shot past bilateral government negotiation table)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a formal bilateral diplomatic meeting room in Hanoi with national flags of Vietnam and the Philippines, where senior Philippine trade delegates shake hands warmly with Vietnamese government counterparts",
        "setting": "the grand state guest hall in Hanoi illuminated by warm chandeliers and elegant cream curtains",
        "motion": "Slow horizontal tracking shot past the bilateral government negotiation table"
    },
    {
        "id": "CH04_SC042",
        "dur": "3.94s",
        "words": 15,
        "text": "Họ cần một thỏa thuận liên chính phủ kéo dài năm năm để bảo đảm",
        "anatomy": {
            "tier1": "Văn bản Thỏa thuận Hợp tác Thương mại Lúa gạo Liên chính phủ 5 năm (Intergovernmental Rice Agreement) đặt trên bàn đàm phán.",
            "tier2": "Hai bên mở các trang văn bản hợp tác chiến lược dài hạn 2024 - 2028 với điều khoản cam kết nguồn cung ổn định.",
            "tier3": "Cú máy tĩnh trực diện vào văn bản Hiệp định Liên chính phủ 5 năm (Steady shot on 5-Year Intergovernmental Rice Supply Agreement) cùng text overlay góc trái dưới."
        },
        "overlay": "HIỆP ĐỊNH LIÊN CHÍNH PHỦ 5 NĂM",
        "ref": None,
        "subj": "a pristine leather-bound bilateral memorandum of understanding titled 'Five-Year Intergovernmental Rice Trade Cooperation Agreement' open on a polished conference desk with gold embossed lettering",
        "setting": "the formal treaty signing chamber in Hanoi under warm dignified indoor lighting",
        "motion": "Steady camera shot framing the historic bilateral government rice agreement document"
    },
    {
        "id": "CH04_SC043",
        "dur": "6.04s",
        "words": 23,
        "text": "Việt Nam cam kết cung cấp nguồn gạo ổn định cho đất nước của họ. Một dân tộc từng dẫn đầu nông nghiệp",
        "anatomy": {
            "tier1": "Cầu cảng xuất khẩu gạo Việt Nam với các sà lan và tàu biển đang nhận những bao gạo trắng thơm chuyển sang Philippines.",
            "tier2": "Bắt tay hữu nghị giữa đại diện thương mại hai nước, khẳng định vai trò trụ cột bảo đảm an ninh lương thực của Việt Nam đối với khu vực.",
            "tier3": "Cú máy góc rộng từ boong tàu hàng Việt Nam nhìn về phía biển khơi (Wide shot from cargo deck looking toward open sea)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a view of a modern Vietnamese grain terminal where a merchant vessel is being systematically loaded with bags of high-grade export rice destined for Manila, framed by warm morning sun",
        "setting": "a peaceful river port export pier in southern Vietnam under warm radiant sunrise",
        "motion": "Slow wide tracking shot along the grain loading conveyor toward the moored cargo vessel"
    },
    {
        "id": "CH04_SC044",
        "dur": "5.25s",
        "words": 20,
        "text": "nay phải gửi gắm sự ổn định xã hội vào năng lực sản xuất của một quốc gia láng giềng.",
        "anatomy": {
            "tier1": "Hình ảnh tương phản tinh tế: Một gia đình Philippines quây quần ăn bữa cơm tối no ấm bên ánh đèn gia đình.",
            "tier2": "Bát cơm trắng dẻo thơm trên bàn ăn của họ có nguồn gốc từ những cánh đồng phù sa màu mỡ của đồng bằng sông Cửu Long.",
            "tier3": "Cú máy đẩy chậm vào mâm cơm gia đình ấm cúng tại Manila (Slow push-in toward warm family dinner table in Manila)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a heartwarming scene of a Filipino family gathered around a modest wooden dinner table sharing steaming bowls of fragrant white rice and local adobo under warm pendant lamps",
        "setting": "a cozy urban home in Manila with warm domestic lighting and peaceful ambiance",
        "motion": "Slow push-in shot toward the warm family dinner table sharing steaming rice"
    },
    {
        "id": "CH04_SC045",
        "dur": "5.51s",
        "words": 21,
        "text": "Bài học từ Philippines là một lời cảnh tỉnh sâu sắc cho bất kỳ nền kinh tế đang phát triển nào.",
        "anatomy": {
            "tier1": "Phòng hội thảo chiến lược phát triển kinh tế vĩ mô với các chuyên gia phân tích chính sách.",
            "tier2": "Hình ảnh bài học thực tiễn được đúc kết trên bảng báo cáo chiến lược: Không bao giờ được xem nhẹ nền tảng nông nghiệp tự chủ.",
            "tier3": "Cú máy đẩy chậm vào bảng đúc kết bài học chiến lược an ninh lương thực (Slow push-in on policy lesson board)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an editorial policy think-tank conference room where senior development economists analyze comparative Southeast Asian food security case studies on presentation boards",
        "setting": "a distinguished academic seminar hall in warm ivory cream and amber tones",
        "motion": "Slow push-in camera shot framing the policy study presentation on economic resilience"
    },
    {
        "id": "CH04_SC046",
        "dur": "6.3s",
        "words": 24,
        "text": "Một quốc gia có thể xây dựng những tòa tháp chọc trời hay sở hữu doanh thu dịch vụ hàng chục tỷ đô la.",
        "anatomy": {
            "tier1": "Toàn cảnh đường chân trời rực rỡ của các khu đô thị tài chính hiện đại Đông Nam Á trong ánh hoàng hôn vàng cam.",
            "tier2": "Những tòa tháp tài chính cao vút biểu trưng cho doanh thu hàng chục tỷ USD từ các ngành dịch vụ công nghệ cao.",
            "tier3": "Cú máy bay ngang (panoramic aerial glide) bao quát vẻ tráng lệ của các tòa nhà chọc trời (Panoramic aerial glide across modern financial skyline)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a breathtaking panoramic view of modern glass skyscrapers and illuminated financial towers in Southeast Asia reflecting golden sunset light",
        "setting": "a sprawling modern Asian metropolitan center at golden hour under warm amber skies",
        "motion": "Panoramic aerial glide across the gleaming golden skyline of financial high-rises"
    },
    {
        "id": "CH04_SC047",
        "dur": "3.15s",
        "words": 12,
        "text": "Thế nhưng, nếu tự tay bẻ gãy chiếc xương sống nông nghiệp",
        "anatomy": {
            "tier1": "Hình ảnh biểu tượng: Những lưỡi cày và bánh xe máy nông nghiệp bị lãng quên bên bờ ruộng cỏ lau dưới ánh chiều tà.",
            "tier2": "Mảnh đất canh tác màu mỡ bị bỏ hoang hoặc san lấp làm dự án dang dở, ẩn dụ cho sự tổn thương của chiếc xương sống nông nghiệp.",
            "tier3": "Cú máy trượt ngang qua cánh đồng hoang phế trong ánh chiều muộn (Horizontal tracking shot past neglected rural fields at dusk)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an evocative rustic visual of a retired metal plow standing in an overgrown fallow field under an amber twilight sky, symbolizing neglected agricultural roots",
        "setting": "a quiet rural pasture at golden twilight with warm wind blowing through tall grass",
        "motion": "Slow horizontal tracking shot past the solitary rustic plow at twilight"
    },
    {
        "id": "CH04_SC048",
        "dur": "4.46s",
        "words": 17,
        "text": "mọi thành quả kinh tế đều sẽ trở nên mong manh trước biến động địa chính trị.",
        "anatomy": {
            "tier1": "Bàn cờ kinh tế toàn cầu với các tuyến vận tải biển bị xáo trộn bởi lệnh cấm xuất khẩu và xung đột thời tiết.",
            "tier2": "Hình ảnh chuỗi cung ứng mong manh khi biến động bên ngoài có thể lập tức làm lung lay sự ổn định của một quốc gia thiếu tự chủ.",
            "tier3": "Cú máy đẩy chậm vào mạng lưới chuỗi cung ứng toàn cầu chịu áp lực (Slow push-in on geopolitical supply chain tension display)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a global geopolitical risk dashboard illustrating volatile international trade lanes, weather disruption icons, and fragile cross-border food logistics",
        "setting": "a strategic analysis room under warm ambient amber console lights",
        "motion": "Slow push-in shot framing the geopolitical vulnerability analytics map"
    },
    {
        "id": "CH04_SC049",
        "dur": "6.3s",
        "words": 24,
        "text": "Tự chủ lương thực không phải là câu chuyện bảo thủ, mà là tấm lá chắn sinh tồn bảo vệ độc lập dân tộc.",
        "anatomy": {
            "tier1": "Bức tranh hùng vĩ của cánh đồng lúa xanh ngắt ngút ngàn của Việt Nam dưới bầu trời xanh ngập tràn ánh nắng ấm.",
            "tier2": "Người nông dân và kỹ sư nông nghiệp đứng hiên ngang trên bờ kênh thủy lợi kiên cố, biểu tượng cho tấm lá chắn an ninh lương thực quốc gia vững chắc.",
            "tier3": "Cú máy góc rộng nâng cao bao quát cánh đồng lúa phì nhiêu trù phú (Wide upward crane shot over vibrant thriving rice fields)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a majestic wide-angle panorama of boundless emerald and golden rice fields flanked by sturdy concrete irrigation channels under a glorious warm morning sun, symbolizing national food sovereignty",
        "setting": "the vast productive plains of the Vietnamese delta under bright warm clear skies",
        "motion": "Smooth ascending crane shot showcasing the majestic expanse of productive farmland"
    },
    {
        "id": "CH04_SC050",
        "dur": "6.04s",
        "words": 23,
        "text": "Thế nhưng, khi nhìn vào vị thế cường quốc xuất khẩu gạo của Việt Nam, một câu hỏi bất ngờ lại xuất hiện.",
        "anatomy": {
            "tier1": "Bàn làm việc của biên tập viên phân tích kinh tế với các tài liệu hải quan và xuất nhập khẩu mới nhất.",
            "tier2": "Một dấu hỏi lớn màu hổ phách ấm áp xuất hiện bên cạnh biểu đồ xuất khẩu gạo kỷ lục hơn 8 triệu tấn của Việt Nam.",
            "tier3": "Cú máy đẩy chậm vào dấu hỏi chiến lược trên bàn tài liệu kinh tế (Slow push-in toward strategic question mark on economic desk)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an editorial research desk with an open analytical dossier showing booming Vietnamese rice export statistics beside a subtle question mark notebook tab",
        "setting": "a warm scholarly study room lit by natural warm morning window light",
        "motion": "Slow push-in shot toward the open research dossier on Vietnamese rice trade"
    },
    {
        "id": "CH04_SC051",
        "dur": "3.41s",
        "words": 13,
        "text": "Nếu chúng ta nắm nguồn lương thực dồi dào để nuôi láng giềng",
        "anatomy": {
            "tier1": "Hình ảnh kho lúa đầy ắp hạt vàng óng của Việt Nam và đoàn tàu hàng đang bốc gạo xuất khẩu đi các nước láng giềng.",
            "tier2": "Nguồn lương thực dồi dào minh chứng cho sức mạnh sản xuất phi thường của nền nông nghiệp nước nhà.",
            "tier3": "Cú máy góc rộng quay kho lúa tràn trề và hoạt động xuất khẩu nhộn nhịp (Wide cinematic shot of overflowing grain granaries and active port berths)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an expansive high-capacity Vietnamese grain storage terminal filled with abundant golden rice silos with loading conveyor belts active beside transport barges",
        "setting": "a busy inland agricultural port hub under warm golden sunlight",
        "motion": "Slow wide tracking shot along the brimming rice grain storage silos"
    },
    {
        "id": "CH04_SC052",
        "dur": "6.3s",
        "words": 24,
        "text": "tại sao mỗi năm Việt Nam vẫn nhập khẩu hàng triệu tấn lúa gạo ngoại? Đằng sau sự thật tưởng chừng mâu thuẫn ấy",
        "anatomy": {
            "tier1": "Cửa khẩu biên giới đường thủy hoặc đường bộ Tây Nam với đoàn ghe thuyền chở lúa gạo từ Campuchia sang Việt Nam.",
            "tier2": "Con số thống kê nhập khẩu hàng triệu tấn lúa tươi từ Campuchia hiện lên trên tờ khai hải quan kiểm dịch.",
            "tier3": "Cú máy đẩy chậm vào hình ảnh đoàn ghe chở lúa ngoại nhập qua cửa khẩu Tây Nam (Slow push-in on cross-border rice transport boats)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a vibrant cross-border river checkpoint in the Southwest frontier where wooden cargo boats laden with raw paddy from Cambodia glide across border waterways toward Vietnamese milling centers",
        "setting": "a bustling Mekong river border crossing in early morning warm sunlight",
        "motion": "Slow push-in camera shot tracking the inbound cross-border raw paddy boats"
    },
    {
        "id": "CH04_SC053",
        "dur": "5.25s",
        "words": 20,
        "text": "là một nước cờ kinh tế tinh vi về sự phân công lao động mà ít người để ý tới.",
        "anatomy": {
            "tier1": "Sơ đồ mạng lưới phân công lao động quốc tế giữa Việt Nam và Campuchia hiển thị trên bản đồ kinh tế khu vực.",
            "tier2": "Mô hình chế biến gia tăng giá trị: Nhập lúa thô $\rightarrow$ Xay xát công nghệ cao $\rightarrow$ Xuất khẩu gạo phẩm cấp cao, tạo bước đệm hoàn hảo sang Chương 5.",
            "tier3": "Cú máy trượt ngang qua sơ đồ phân công chuỗi giá trị gạo khu vực (Horizontal tracking shot across regional rice value-chain division map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an intricate regional economic flowchart illustrating the strategic division of labor: raw paddy intake from regional neighbors, high-tech industrial milling in Vietnam, and premium global export distribution",
        "setting": "a modern economic strategy boardroom display in warm ivory cream and amber tones",
        "motion": "Slow horizontal tracking shot across the regional agricultural division of labor diagram"
    }
]

# Generate Markdown Storyboard
md_lines = [
    "# chapter_04_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 4: Chiếc Bẫy Công Nghiệp Rỗng Ruột: Bài Học Từ Philippines",
    "## Phong cách chủ đạo: Luminous Warm Editorial Illustration (Minh họa báo chí cao cấp, ánh sáng trong trẻo rực rỡ, 100% không gian vật lý đời thực, triệt tiêu hoàn toàn siêu thực và màu đen u ám)",
    "",
    "### 🎨 Hệ màu 60-30-10 (Tuyệt Đối Ấm Áp — Chống Lạnh Lẽo):",
    "- **60% Tông màu nền chủ đạo:** Warm Ivory Cream (`#FAF7EE`), Warm Tropical Manila Daylight (`#FFFBEB`), Warm Amber Sunlit Haze (`#F3E5AB`). Tuyệt đối không dùng nền xám lạnh, xanh cyan buốt giá hay đen kịt.",
    "- **30% Đường nét & Chủ thể:** Ripe Golden Amber (`#F59E0B`), Terracotta Brick & Manila Clay (`#EA580C`), Classical Mahogany & Barong Wood (`#2D241E`), Deep Amber Foliage Green (`#059669`).",
    "- **10% Điểm nhấn dẫn mắt:** Luminous Warm Golden Sunrise Rays (`#D97706`), Warm Chandelier Glow in Malacañang, Glowing Golden Amber Data Badges.",
    "",
    "---",
    "",
    "### 🛡️ Quy Tắc Kiểm Soát Tuyệt Đối:",
    "1. **Scene ID chuẩn theo chương:** `CH04_SC001` đến `CH04_SC053` (Khớp 100% với `scene_timing_map.json`).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Viện IRRI Los Baños, văn phòng BPO tại Bonifacio Global City/Makati, Cung điện Malacañang, cảng biển Manila Harbor, chợ Divisoria, Nhà khách Chính phủ Hà Nội, cửa khẩu đường thủy Tây Nam.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc đúng 11/53 phân cảnh (20.75%) có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. 42 phân cảnh còn lại để `[TEXT OVERLAY]: Không`.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Ảnh Tham Chiếu Nhân Vật / Địa Danh:**",
    "   - `@irri_los_banos_gate.jpg` sử dụng tại `CH04_SC001` & `CH04_SC002` (Viện Lúa Quốc tế IRRI).",
    "   - `@marcos_jr.jpg` sử dụng tại `CH04_SC038` & `CH04_SC039` (Tổng thống Ferdinand Marcos Jr. ký Sắc lệnh số 39).",
    "   - Nhân vật dân sự (người dân, công nhân BPO, kỹ sư): Tuyệt đối KHÔNG dùng ảnh tham chiếu nhân tạo, mô tả trực tiếp trong prompt.",
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

# Save chapter_04_visual.md
with open("episodes/vu-khi-gao-viet-nam/chapter_04_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_04_visual.md ({len(scenes_data)} scenes)")

# Generate prompts_chapter_04.txt
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

with open("episodes/vu-khi-gao-viet-nam/prompts_chapter_04.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompt_lines).strip() + "\n")

print(f"✅ Generated prompts_chapter_04.txt ({len(scenes_data)} scenes)")
