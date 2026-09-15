import json

# Full 64 scenes for Chapter 4
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
        "overlay": "IRRI - LOS BANOS, 1960s",
        "ref": "irri_los_banos_gate.jpg",
        "subj": "the classical 1960s modernist concrete and stone facade of the International Rice Research Institute (IRRI) entrance building with international agricultural scientists in white coats discussing beside sample trays",
        "setting": "the main courtyard of IRRI Los Baños under warm amber tropical sunlight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the institutional IRRI entrance"
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
        "overlay": "MIRACLE RICE IR8",
        "ref": None,
        "subj": "a botanical close-up of the legendary Miracle Rice IR8 variety with thick sturdy semi-dwarf stalks and dense golden panicles held gently by an Asian agronomist in field attire",
        "setting": "a sunny experimental agronomy paddy bathed in warm morning light",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the golden IR8 panicle"
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
        "subj": "a group of diverse Southeast Asian agricultural engineers and students wearing lightweight field shirts earnestly sketching and taking notes on clipboards",
        "setting": "an open-air research pavilion shaded by tropical acacia trees at IRRI Los Baños under warm morning sun",
        "motion": "Slow horizontal tracking shot past the focused agricultural trainees"
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
        "subj": "an open library veranda at the research institute overlooking tropical palm groves toward a distant hazy urban skyline in the golden evening light",
        "setting": "an academic library portico with warm mahogany wood furniture in soft sunset light",
        "motion": "Slow pull-back camera motion from the library portico toward the distant glowing horizon"
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
        "subj": "Filipino economic planners in Barong Tagalog shirts gathered around a large boardroom conference table studying a glowing master plan of modern urban services and financial districts",
        "setting": "a high-level government ministry planning hall in Manila under warm ambient architectural downlights",
        "motion": "Slow push-in camera shot toward the strategic economic development blueprint"
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
        "subj": "a stark visual transition: a dusty neglected earthen irrigation canal on the left leading directly into a gleaming export processing zone with modern electronics factories on the right",
        "setting": "the rural-urban fringe of Laguna and Cavite under bright tropical daylight",
        "motion": "Slow horizontal tracking pan across the structural economic divide"
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
        "overlay": "BPO SERVICES & REMITTANCES",
        "ref": None,
        "subj": "an expansive illuminated modern call center floor filled with hundreds of young Filipino customer support agents wearing telephone headsets typing diligently on computer terminals",
        "setting": "a high-density modern BPO office tower in Bonifacio Global City Manila under warm ambient indoor lighting",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the bustling call center floor"
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
        "subj": "a busy foreign exchange remittance counter in Manila where local families collect overseas worker remittances beside cleanroom electronics assembly benches",
        "setting": "a lively commercial district in Metro Manila bathed in warm natural afternoon sunlight",
        "motion": "Slow horizontal tracking shot past the remittance service window and assembly technicians"
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
        "subj": "an economic research desk with open spreadsheets and bar charts showing high service sector profit margins contrasted against low primary agrarian yields",
        "setting": "a minimalist economic consultancy office with warm oak paneling under soft overhead downlights",
        "motion": "Slow push-in shot toward the sectoral GDP comparison chart"
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
        "subj": "a grand executive office window overlooking Manila Bay filled with passing cargo ships and sailboats under a radiant tropical sky, framing a desk with financial ledgers",
        "setting": "a high-floor waterfront executive suite in Manila in warm midday daylight",
        "motion": "Wide cinematic pan from the desk globe out across the sun-drenched waters of Manila Bay"
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
        "subj": "neatly stacked pallets of imported white rice bags on a concrete wharf beside foreign cargo bills of lading stamped in US dollars",
        "setting": "a busy commercial cargo pier at the Port of Manila under warm golden daylight",
        "motion": "Slow tilt-up shot from the foreign trade invoices to the looming dockside crane"
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
        "subj": "an elegant macroeconomic textbook illustration showing clean balanced equilibrium lines where export services smoothly finance cheap food imports",
        "setting": "an academic study hall with polished glass desks under warm ambient daylight",
        "motion": "Slow push-in shot framing the pristine theoretical economic diagrams"
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
        "subj": "a weathered brick and rusted metal irrigation sluice gate with dry cracked mud at the bottom of an abandoned canal in rural Luzon",
        "setting": "a neglected provincial countryside pumping station under warm dusty sunlight",
        "motion": "Slow horizontal tracking shot past the cracked concrete and rusted iron wheel"
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
        "subj": "a parched agricultural field crisscrossed by deep fissures in the dry clay, with a solitary wooden hand plow resting beside an uncultivated ridge",
        "setting": "an arid rural farming valley in Central Luzon under a warm hazy afternoon sky",
        "motion": "Low-angle tracking shot gliding along the dry cracked fissures of the parched earth"
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
        "overlay": "PREMATURE DEINDUSTRIALIZATION TRAP",
        "ref": None,
        "subj": "an analytical development economics diagram mapping the structural trap of premature deindustrialization: skipping agrarian modernization straight into low-tier services",
        "setting": "an economic research institute conference room with warm ivory and terracotta decor",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the structural economics chart"
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
        "subj": "a quiet mechanical fabrication workshop with idle industrial metal lathes and unassembled agricultural harvester gears gathering warm golden dust",
        "setting": "a small machinery plant on the outskirts of Manila in warm afternoon light",
        "motion": "Slow horizontal tracking shot past the dormant fabrication machinery"
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
        "subj": "a long weathered concrete irrigation canal choked with silt and wild reeds, flanked by rusted toll fee signs and inoperable private water gates",
        "setting": "rural agricultural lands in Nueva Ecija under warm midday tropical sun",
        "motion": "Slow push-in camera shot along the overgrown silted irrigation channel"
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
        "subj": "an aerial high-angle view of severely fragmented smallholder rice paddies divided into irregular patchwork plots where an Asian farmer leads a carabao water buffalo through deep mud",
        "setting": "a fragmented countryside plain in the Philippines under warm golden daylight",
        "motion": "Smooth high-angle pan showing the mosaic of fragmented puzzle-like rice plots"
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
        "overlay": "RICE YIELD: < 4 TONS/HA",
        "ref": None,
        "subj": "an official agrarian statistics ledger showing a flat horizontal yield line stagnating strictly below four metric tons per hectare across several decades",
        "setting": "a statistical records office with warm wooden desks and archival folders under natural light",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the flat yield curve"
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
        "subj": "a clean comparative agricultural chart contrasting a modest 3.8 tons/ha bar for the Philippines against a towering 7.2 tons/ha bar representing the fertile Mekong Delta",
        "setting": "a modern economic consultancy studio under warm ambient amber light",
        "motion": "Horizontal camera glide panning across the two comparative yield pillars"
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
        "overlay": "POPULATION: > 115 MILLION",
        "ref": None,
        "subj": "a dynamic urban intersection along EDSA boulevard in Metro Manila packed with iconic colorful jeepneys and dense crowds of commuters under a blazing tropical sun",
        "setting": "a bustling central thoroughfare in Metro Manila during peak daytime traffic",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the bustling Manila traffic"
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
        "subj": "a stark supply-and-demand graph on a digital screen where the steep rising red curve of national rice consumption pulls far away from the stagnant domestic harvest line, creating a deep deficit chasm",
        "setting": "a food security analysis command room under warm amber display lights",
        "motion": "Slow push-in shot highlighting the expanding structural deficit gap between supply and demand"
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
        "subj": "a global maritime shipping map showing shipping lanes converging from across Asia directly toward the Philippine archipelago, highlighting its status as the world's premier rice importer",
        "setting": "an international trade analytics observatory with warm ivory console finishes",
        "motion": "Wide cinematic tracking shot across the converging ocean shipping routes toward Manila"
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
        "subj": "a line of heavy dockside container cranes actively unloading cargo ships anchored along the bustling deepwater commercial quays of Manila South Harbor",
        "setting": "the industrial waterfront of Manila Port bathed in warm morning daylight",
        "motion": "Slow horizontal tracking shot along the busy commercial docks"
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
        "overlay": "IMPORTS: 3.8 - 4.5M TONS/YEAR",
        "ref": None,
        "subj": "a massive bonded transit warehouse filled with towering stacks of woven polypropylene rice bags reaching nearly to the high steel ceiling beams",
        "setting": "a high-capacity port storage terminal in Manila under warm industrial interior floodlights",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the towering rice sack stacks"
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
        "overlay": "> 80% IMPORTS FROM VIETNAM",
        "ref": None,
        "subj": "clean wooden pallets loaded with bags marked Premium Vietnamese Jasmine Rice being transferred across the wharf beside a pie chart showing Vietnam holding over eighty percent import share",
        "setting": "an open-air cargo handling pier in Manila under bright warm tropical sunlight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the Vietnamese rice pallets"
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
        "subj": "a framed sepia photograph from 1966 showing pioneering Filipino agronomists lecturing international delegates beside fertile experimental paddies",
        "setting": "a distinguished academic boardroom wall lit by warm gallery spotlights",
        "motion": "Slow push-in camera shot toward the historical framed photograph"
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
        "subj": "a solitary silhouetted commercial grain freighter slowly navigating into Manila Bay under a deep amber and warm crimson sunset, symbolizing complete maritime food dependence",
        "setting": "the breakwaters of Manila Bay at dusk with warm ocean reflections",
        "motion": "Slow pull-back camera motion from the breakwater toward the inbound cargo vessel"
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
        "subj": "a sidewalk newspaper kiosk in Manila displaying front-page newspaper headlines in English and Tagalog shouting about skyrocketing rice prices and global food supply threats",
        "setting": "a sunbaked downtown sidewalk in Manila in July 2023 under harsh warm midday sun",
        "motion": "Low-angle horizontal tracking shot past the urgent newspaper headlines"
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
        "subj": "an official diplomatic decree bearing the emblem of the Directorate General of Foreign Trade of India stamped with a prominent red export prohibition seal over Non-Basmati White Rice",
        "setting": "a foreign trade advisory desk under warm focused overhead lamps",
        "motion": "Dynamic push-in camera shot toward the red official trade ban decree"
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
        "subj": "a global commodities exchange electronic board showing the price graph of export rice shooting upward into steep red territory past 650 USD per metric ton",
        "setting": "a high-energy commodities trading room under warm ambient console illumination",
        "motion": "Smooth ascending camera motion tracking the soaring commodities price curve"
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
        "overlay": "FOOD INFLATION: > 8%",
        "ref": None,
        "subj": "a bustling covered wet market in Divisoria Manila where chalk price boards show sharp daily price hikes on staple rice sacks beside distressed shoppers",
        "setting": "a crowded traditional retail marketplace in Manila bathed in warm natural light",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the market rice price boards"
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
        "subj": "a family dining table in Manila where an overseas worker remittance envelope stamped with foreign postal marks lies open beside utility bills and receipts",
        "setting": "a modest urban apartment living room in Manila under warm lamplight",
        "motion": "Slow close-up tracking shot past the open remittance envelope and household receipts"
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
        "subj": "an evocative ledger comparison showing surging dollar import invoices completely consuming hard-earned remittance reserves in a state trade account",
        "setting": "a government central bank accounting office under warm morning lighting",
        "motion": "Slow push-in shot highlighting the surging food import expenditures on the ledger"
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
        "subj": "hundreds of everyday Filipino citizens carrying cloth bags and identification cards waiting patiently in a winding outdoor queue under the bright midday sun outside an NFA subsidized rice distribution depot",
        "setting": "a residential neighborhood street in suburban Manila under warm tropical sunlight",
        "motion": "Slow horizontal tracking shot along the patient queue of residents waiting for staple rice"
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
        "subj": "completely empty wooden and steel display bins in a Manila supermarket labeled Out of Stock beside closed shutter doors of small local grain retail shops",
        "setting": "an urban grocery store aisle under warm fluorescent lights",
        "motion": "Slow horizontal tracking shot past the bare empty rice shelves and out-of-stock signs"
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
        "overlay": "EXECUTIVE ORDER NO. 39",
        "ref": "marcos_jr.jpg",
        "subj": "President Ferdinand Marcos Jr. wearing an embroidered white formal Barong Tagalog seated at a polished mahogany presidential desk signing official Executive Order No. 39 imposing mandatory rice price ceilings",
        "setting": "the ceremonial signing room of Malacañang Palace in Manila adorned with national flags and warm chandelier light",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and President Marcos Jr. signing the executive decree"
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
        "subj": "market trade inspection officers in uniform politely posting official government price ceiling notices reading Regular Milled Rice 41 Pesos on a market stall post",
        "setting": "a busy public market pavilion in Manila under warm amber morning daylight",
        "motion": "Slow horizontal tracking shot past the newly posted price ceiling decree"
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
        "subj": "a dramatic upward-looking street view from ground level showing gleaming modern glass corporate skyscrapers soaring into an amber twilight sky above ordinary citizens walking past food stalls",
        "setting": "the financial district of Bonifacio Global City Taguig in warm golden evening light",
        "motion": "Low-angle upward tilt gliding smoothly along the glass facade of the financial corporate towers"
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
        "subj": "high-ranking Philippine trade diplomats in dark suits entering an official state guest hall in Hanoi to shake hands warmly with Vietnamese government counterparts",
        "setting": "an elegant diplomatic reception room in Hanoi with yellow lacquer walls and warm chandelier lighting",
        "motion": "Slow horizontal tracking shot along the bilateral diplomatic negotiation table"
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
        "overlay": "5-YEAR BILATERAL RICE AGREEMENT",
        "ref": None,
        "subj": "a leather-bound diplomatic treaty folder resting on a polished conference table with dual state seals embossed in gold, opened to terms of a 5-year bilateral grain supply framework",
        "setting": "a formal bilateral conference hall bathed in warm morning light",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the bilateral treaty documents"
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
        "subj": "an active Vietnamese export grain terminal where cranes transfer pallets of rice onto international transport ships bound for Manila under bright warm sunshine",
        "setting": "a bustling deepwater export terminal in Southern Vietnam in luminous morning light",
        "motion": "Wide cinematic tracking shot across the busy cargo berths loaded with outbound rice pallets"
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
        "subj": "a warm, intimate portrait of a multi-generational Filipino family gathered peacefully around an evening dinner table sharing steaming bowls of fragrant white rice",
        "setting": "a cozy family dining room in Manila filled with warm amber lamplight",
        "motion": "Slow push-in camera motion toward the family dinner table and steaming rice bowls"
    },
    # NEW NORTH KOREA & GEOSTRATEGIC AID SECTION
    {
        "id": "CH04_SC045",
        "dur": "5.25s",
        "words": 20,
        "text": "Thế nhưng, bàn cờ địa chính trị của hạt gạo Việt Nam không chỉ dừng lại ở Đông Nam Á.",
        "anatomy": {
            "tier1": "Mặt bàn gỗ gụ sang trọng trong thư viện phân tích địa chiến lược quốc tế, dưới ánh đèn vàng ấm áp.",
            "tier2": "Bản đồ địa chính trị châu Á trải rộng, một bàn tay nghiên cứu xoay nhẹ quả địa cầu từ khu vực Đông Nam Á hướng lên phía Bắc.",
            "tier3": "Cú máy trượt ngang từ bản đồ Đông Nam Á hướng lên Đông Bắc Á (Slow horizontal camera glide across Asian geopolitical map from Southeast toward Northeast Asia)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a distinguished mahogany conference table with an open geopolitical map of Asia and an antique brass globe bathed in warm golden ambient light",
        "setting": "a strategic international affairs library illuminated by a warm banker lamp glow",
        "motion": "Slow horizontal tracking shot across the open geopolitical map of Asia from Southeast toward Northeast Asia"
    },
    {
        "id": "CH04_SC046",
        "dur": "4.46s",
        "words": 17,
        "text": "Nhìn sang Đông Bắc Á, một quốc gia sở hữu kho vũ khí hạt nhân và tên lửa đạn đạo như Triều Tiên",
        "anatomy": {
            "tier1": "Quảng trường Kim Nhật Thành rộng lớn tại Bình Nhưỡng trong ánh chiều tà vàng nhạt, các tòa nhà kiến trúc tân cổ điển hoành tráng.",
            "tier2": "Đoàn xe vận tải quân sự hạng nặng di chuyển trang nghiêm trong buổi diễu binh, biểu trưng cho sức mạnh hạt nhân và tên lửa đạn đạo.",
            "tier3": "Cú máy góc rộng trượt chậm qua quảng trường Bình Nhưỡng (Wide cinematic tracking shot across Pyongyang grand square)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the monumental grand square of Pyongyang with imposing neoclassical granite government facades and a military parade convoy under a pale warm late afternoon sky",
        "setting": "the historic ceremonial center of Pyongyang North Korea in calm warm golden twilight",
        "motion": "Wide cinematic tracking shot gliding slowly across the monumental grand square of Pyongyang"
    },
    {
        "id": "CH04_SC047",
        "dur": "4.72s",
        "words": 18,
        "text": "cũng luôn đặt hạt gạo ở vị trí an ninh tối thượng.",
        "anatomy": {
            "tier1": "Bên trong một kho dự trữ ngũ cốc chiến lược quốc gia kiên cố tại Triều Tiên với kết cấu bê tông vững chãi.",
            "tier2": "Những chồng bao thóc dự trữ chiến lược được bảo quản cẩn mật, khẳng định vị trí sống còn của hạt gạo đối với an ninh quốc gia.",
            "tier3": "Cú máy tĩnh trực diện vào các khối bao ngũ cốc dự trữ chiến lược (Steady shot on strategic grain reserve stacks) cùng text overlay góc trái dưới."
        },
        "overlay": "STRATEGIC GRAIN SECURITY",
        "ref": None,
        "subj": "a fortified national strategic grain reserve warehouse in North Korea with orderly towering stacks of sealed jute grain sacks under warm amber ceiling lamps",
        "setting": "a high-security national food reserve depository under warm industrial lighting",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the strategic grain reserve stacks"
    },
    {
        "id": "CH04_SC048",
        "dur": "6.83s",
        "words": 26,
        "text": "Suốt nhiều thập kỷ, khẩu hiệu sinh tồn được khắc sâu trong đời sống chính trị của họ là: Gạo chính là chủ nghĩa xã hội.",
        "anatomy": {
            "tier1": "Đại lộ lớn tại Bình Nhưỡng với hàng cây liễu rủ bóng bên dòng sông Taedong dưới ánh nắng ban mai ấm áp.",
            "tier2": "Tấm biển pano cổ động chính trị lớn màu đỏ thắm viền vàng với hình tượng bông lúa vàng trĩu hạt và dòng khẩu hiệu kinh điển của Triều Tiên.",
            "tier3": "Cú máy tĩnh trực diện vào tấm pano khẩu hiệu nông nghiệp lịch sử (Steady shot on historic agricultural propaganda billboard) cùng text overlay góc trái dưới."
        },
        "overlay": "RICE IS SOCIALISM",
        "ref": None,
        "subj": "a prominent monumental socialist realism propaganda billboard painted in rich crimson and warm golden amber depicting ripe golden rice panicles and working farmers beside a tranquil tree-lined avenue",
        "setting": "a wide boulevard in Pyongyang overlooking the Taedong River under warm morning sunlight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the socialist realism rice billboard"
    },
    {
        "id": "CH04_SC049",
        "dur": "7.09s",
        "words": 27,
        "text": "Một đất nước có thể chế tạo đầu đạn hạt nhân, nhưng không thể dùng vũ khí để xua đi cơn đói khi đồng ruộng thất bát.",
        "anatomy": {
            "tier1": "Cánh đồng bậc thang ngoại ô vùng nông thôn Triều Tiên trong một đợt khô hạn khốc liệt, đất đai khô nứt nẻ.",
            "tier2": "Một chiếc máy kéo cũ kỹ đứng im lìm bên bờ ruộng khô cháy, tương phản sâu sắc giữa sức mạnh vũ khí và sự bất lực trước thiên tai mất mùa.",
            "tier3": "Cú máy hạ thấp trượt chậm qua mặt đất nứt nẻ của cánh đồng hạn hán (Low-angle slow tracking shot past cracked parched paddy ground)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a drought-stricken hillside terraced paddy field in rural North Korea with parched cracked earth and an idle weathered tractor under an arid warm amber sky",
        "setting": "a drought-affected rural farming province in North Korea during a severe dry spell in warm dusty sunlight",
        "motion": "Low-angle slow tracking shot gliding smoothly across the cracked dry earth of the fallow paddy fields"
    },
    {
        "id": "CH04_SC050",
        "dur": "3.94s",
        "words": 15,
        "text": "Trong những thời khắc khốn cùng nhất của nạn đói thập niên 1990,",
        "anatomy": {
            "tier1": "Khung cảnh lịch sử tái hiện giai đoạn \"Gian khổ\" (Arduous March) giữa thập niên 1990 tại Triều Tiên.",
            "tier2": "Những con đường làng và thị trấn miền núi yên ắng trong màn sương mờ sầu lắng, bóng người dân co ro bước đi trong gió lạnh tìm kiếm thức ăn.",
            "tier3": "Cú máy đẩy chậm vào con đường làng miền núi vắng lặng (Slow push-in shot along the quiet misty mountain road)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an evocative historical scene of a quiet North Korean rural village during the harsh 1990s period with modest stone cottages and solitary villagers walking along a chilly mountain path under pale morning sun",
        "setting": "a remote rural township in North Korea during the 1990s under soft muted golden daylight",
        "motion": "Slow push-in camera shot gliding down the quiet rural mountain road under pale morning sunlight"
    },
    {
        "id": "CH04_SC051",
        "dur": "4.99s",
        "words": 19,
        "text": "chính Việt Nam đã lập tức xuất kho mười ba nghìn tấn gạo không hoàn lại để cứu giúp nước bạn.",
        "anatomy": {
            "tier1": "Cầu cảng xuất nhập khẩu Hải Phòng hoặc Sài Gòn năm 1997 dưới ánh nắng rực rỡ của thời kỳ đầu Đổi Mới.",
            "tier2": "Công nhân cảng hối hả bốc vác các bao gạo trắng viện trợ không hoàn lại 13.000 tấn lên boong tàu hàng Việt Nam sang giúp Triều Tiên.",
            "tier3": "Cú máy tĩnh trực diện vào con số 13.000 tấn gạo viện trợ và nhịp bốc dỡ khẩn trương (Steady shot on 13,000 tons emergency food aid loading) cùng text overlay góc trái dưới."
        },
        "overlay": "VIETNAM AID: 13,000 TONS (1997)",
        "ref": None,
        "subj": "a busy maritime seaport pier in Vietnam in 1997 where docker workers and dockside cranes rapidly load pallets of white rice sacks marked with diplomatic aid stencils onto a vintage cargo vessel",
        "setting": "a commercial shipping dock in Vietnam in 1997 bathed in warm bright morning sun",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the active ship loading cranes"
    },
    {
        "id": "CH04_SC052",
        "dur": "3.94s",
        "words": 15,
        "text": "Các cường quốc thường chỉ viện trợ khi trong kho đã dư thừa của cải.",
        "anatomy": {
            "tier1": "Khu tổ hợp hậu cần khổng lồ của một cường quốc phương Tây với hàng ngàn container và nhà kho tự động hiện đại.",
            "tier2": "Những kiện hàng viện trợ chỉ được xuất đi khi các kho thóc quốc gia đã chất đầy tràn trề thặng dư của cải tích lũy.",
            "tier3": "Cú máy trượt ngang qua dãy kho chứa hàng khổng lồ (Horizontal tracking pan past massive high-tech grain logistics warehouses)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a colossal international grain storage terminal of a wealthy superpower packed with towering metallic grain silos and automated export conveyors operating at full capacity",
        "setting": "a sprawling modern industrial export port terminal under bright midday sun",
        "motion": "Slow horizontal tracking pan past the colossal grain elevators and automated export silos"
    },
    {
        "id": "CH04_SC053",
        "dur": "6.83s",
        "words": 26,
        "text": "Nhưng với người Việt Nam, chúng ta sẵn sàng nhường cơm sẻ áo ngay khi bản thân mình còn đang muôn vàn cơ hàn, thiếu thốn.",
        "anatomy": {
            "tier1": "Gian nhà ba gian mộc mạc của một gia đình nông dân Việt Nam những năm 1990, vách đất mái ngói rêu phong.",
            "tier2": "Người mẹ và các con quây quần bên mâm cơm gỗ đơn sơ, ánh mắt chan chứa tình người và sự sẻ chia nhường cơm sẻ áo dù bản thân còn thiếu thốn.",
            "tier3": "Cú máy lùi chậm từ mâm cơm mộc mạc tỏa khói ấm ra toàn cảnh gian nhà (Slow pull-back shot from modest dinner tray)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an authentic Vietnamese rural wooden home interior in the late 1990s where a family shares a modest meal of steaming white rice and homegrown greens around a simple wooden tray under the warm glow of an oil lantern",
        "setting": "a humble traditional Vietnamese countryside household filled with warm cozy ambient light",
        "motion": "Slow pull-back camera shot centering on the humble family sharing their warm modest meal"
    },
    {
        "id": "CH04_SC054",
        "dur": "5.25s",
        "words": 20,
        "text": "Năm 1997, đất nước vừa bước qua Đổi Mới chưa lâu, mâm cơm người Việt còn bộn bề gian khó.",
        "anatomy": {
            "tier1": "Cánh đồng lúa làng quê Việt Nam năm 1997 trong mùa gặt, những bó lúa vàng tươi được gánh trên đôi vai gầy guộc.",
            "tier2": "Người nông dân chân lội bùn, mồ hôi ướt đẫm lưng áo nhưng ánh mắt rạng ngời niềm tin, mâm cơm còn nhiều gian khó thời kỳ đầu mở cửa.",
            "tier3": "Cú máy trượt ngang qua người nông dân đang gánh lúa trên bờ đê (Horizontal tracking shot past farmers carrying rice sheaves on earthen dike)."
        },
        "overlay": None,
        "ref": None,
        "subj": "hardworking Vietnamese farmers in conical hats and rolled-up trousers carrying heavy golden rice sheaves on bamboo shoulder poles along a rural earthen dike in 1997",
        "setting": "a rustic Vietnamese rice village during the 1997 harvest under golden late afternoon sunlight",
        "motion": "Slow horizontal tracking shot following the farmers carrying golden rice sheaves along the village dike"
    },
    {
        "id": "CH04_SC055",
        "dur": "7.09s",
        "words": 27,
        "text": "Thế nhưng, đứng trước cơn hoạn nạn của bạn bè, chúng ta sẵn sàng bớt đi bát cơm của mình mà không hề tính toán thiệt hơn.",
        "anatomy": {
            "tier1": "Mũi con tàu chở hàng Việt Nam rẽ sóng Biển Đông tiến về hướng Bắc, lá cờ đỏ sao vàng tung bay phần phật trong gió biển.",
            "tier2": "Dưới khoang tàu là hàng ngàn tấn gạo nghĩa tình chắt chiu từ mồ hôi nước mắt của người nông dân Việt Nam gửi tặng nhân dân Triều Tiên.",
            "tier3": "Cú máy góc rộng từ boong tàu nhìn ra biển lớn mênh mông trong ánh bình minh vàng rực (Cinematic wide shot looking forward from the ship bow into open ocean)."
        },
        "overlay": None,
        "ref": None,
        "subj": "the bow of a Vietnamese cargo freighter cleaving ocean waves toward the open sea under a magnificent warm golden sunrise, carrying tons of humanitarian rice bags in its hold",
        "setting": "the open maritime sea lanes of East Asia bathed in luminous golden sunrise light",
        "motion": "Dynamic forward tracking shot mounted on the cargo ship bow gliding over calm ocean swells"
    },
    {
        "id": "CH04_SC056",
        "dur": "5.51s",
        "words": 21,
        "text": "Đến năm 2019, năm nghìn tấn gạo nghĩa tình lại tiếp tục cập cảng Nampo giữa đợt hạn hán khốc liệt.",
        "anatomy": {
            "tier1": "Cảng biển Nampo của Triều Tiên bên cửa sông Taedong dưới ánh nắng mùa hè năm 2019.",
            "tier2": "Tàu chở 5.000 tấn gạo viện trợ của Việt Nam cập bến, cần cẩu cảng bốc dỡ những pallet gạo trắng nghĩa tình trong niềm xúc động của các công nhân cảng Triều Tiên.",
            "tier3": "Cú máy tĩnh trực diện vào con tàu viện trợ 5.000 tấn gạo cập cảng Nampo (Steady shot on Vietnamese 5,000-ton relief vessel berthing at Nampo Port) cùng text overlay góc trái dưới."
        },
        "overlay": "NAMPO PORT: 5,000 TONS AID (2019)",
        "ref": None,
        "subj": "the commercial harbor piers of Nampo Port in North Korea where a large Vietnamese cargo ship docks beside gantry cranes unloading white bags of 5,000 tons emergency food aid",
        "setting": "the industrial seaport of Nampo North Korea under warm bright summer sunshine",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the dockside cargo vessel at Nampo Port"
    },
    {
        "id": "CH04_SC057",
        "dur": "7.88s",
        "words": 30,
        "text": "Các nhà khoa học Việt Nam đã chuyển giao mười bảy giống lúa ngắn ngày chịu hạn và chịu rét sang Triều Tiên để giúp bạn tự chủ nguồn cung.",
        "anatomy": {
            "tier1": "Nhà kính nghiên cứu nông học hiện đại tại ngoại ô Bình Nhưỡng với các giàn ươm giống lúa xanh tươi tốt.",
            "tier2": "Nhà khoa học nông nghiệp Việt Nam và các đồng nghiệp Triều Tiên kiểm tra khay 17 giống lúa ngắn ngày chịu hạn, chịu rét vượt trội.",
            "tier3": "Cú máy tĩnh trực diện vào khay giống lúa chuyển giao 17 giống chịu hạn rét (Steady shot on 17 drought-and-cold resilient rice varieties) cùng text overlay góc trái dưới."
        },
        "overlay": "17 CLIMATE-RESILIENT RICE VARIETIES",
        "ref": None,
        "subj": "Vietnamese and North Korean agronomists in white research coats collaboratively inspecting thriving green seedlings of drought-and-cold resilient rice varieties arranged in scientific testing trays inside an agronomy greenhouse",
        "setting": "an agricultural research greenhouse near Pyongyang illuminated by warm natural daylight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the experimental rice nursery trays"
    },
    {
        "id": "CH04_SC058",
        "dur": "5.78s",
        "words": 22,
        "text": "Từ Manila đến Bình Nhưỡng, hạt gạo Việt Nam đã vượt xa ý nghĩa của một món hàng thương mại thông thường.",
        "anatomy": {
            "tier1": "Bản đồ địa chính trị Đông Á và Đông Nam Á phát sáng trên bàn hội nghị bằng gỗ sồi ấm áp.",
            "tier2": "Hai tuyến hải trình lúa gạo tỏa sáng từ vựa lúa Việt Nam: một tuyến hướng sang Manila, một tuyến vươn dài tới Bình Nhưỡng, khẳng định tầm vóc vượt bậc của hạt gạo Việt.",
            "tier3": "Cú máy bay lùi chậm bao quát toàn bộ mạng lưới hai tuyến hải trình lương thực (Slow aerial pull-back showing dual food maritime routes)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an illuminated strategic map of East and Southeast Asia highlighting luminous warm golden maritime shipping arcs radiating from Vietnam toward Manila Bay and the Port of Nampo",
        "setting": "a modern geopolitical strategy chamber with warm ambient oak paneling and soft spotlights",
        "motion": "Slow aerial pull-back revealing the dual maritime food security corridors connecting Vietnam to Manila and Pyongyang"
    },
    {
        "id": "CH04_SC059",
        "dur": "7.35s",
        "words": 28,
        "text": "Nó đã trở thành chiếc van an ninh sinh tồn, nắm giữ sự ổn định chính trị và quyền lực bảo vệ hòa bình cho cả khu vực.",
        "anatomy": {
            "tier1": "Biểu tượng nghệ thuật tả thực: Một van điều tiết an ninh bằng đồng thau sáng bóng đặt cạnh biểu đồ ổn định địa chính trị khu vực.",
            "tier2": "Dòng chảy hạt gạo vàng óng chảy qua chiếc van an ninh, biểu trưng cho quyền lực giữ gìn sự cân bằng và hòa bình cho hàng trăm triệu con người.",
            "tier3": "Cú máy tĩnh trực diện vào biểu tượng chiếc van an ninh sinh tồn (Steady shot on symbolic regional security pressure valve) cùng text overlay góc trái dưới."
        },
        "overlay": "REGIONAL SECURITY VALVE",
        "ref": None,
        "subj": "a powerful symbolic still-life composition of an antique polished brass pressure valve resting beside an intricate geopolitical stability matrix with golden rice grains flowing smoothly around it",
        "setting": "a prestigious international policy boardroom in warm amber lighting",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the brass security valve centerpiece"
    },
    {
        "id": "CH04_SC060",
        "dur": "6.56s",
        "words": 25,
        "text": "Đó là thứ vũ khí phòng thủ tối thượng được sinh ra từ chính mồ hôi và lòng kiên định của những người làm ruộng.",
        "anatomy": {
            "tier1": "Cánh đồng lúa chín vàng trĩu hạt trải dài tít tắp đến tận chân trời của đồng bằng sông Cửu Long dưới ánh bình minh rực rỡ.",
            "tier2": "Đôi bàn tay rám nắng chai sần của người nông dân nâng niu những bông lúa chín vàng ươm, tỏa ra vẻ đẹp kiên cường và lòng kiêu hãnh của người làm ruộng.",
            "tier3": "Cú máy cận cảnh nâng chậm từ đôi bàn tay người nông dân lên chân trời cánh đồng lúa bao la (Slow tilt-up from weathered hands holding golden rice panicles to radiant horizon)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an evocative close-up of weathered, hardworking Vietnamese farmer hands tenderly cupping a heavy cluster of ripe golden rice panicles against an endless golden horizon",
        "setting": "the boundless fertile rice plains of the Mekong Delta under glorious warm morning sunlight",
        "motion": "Slow upward tilt from the weathered hands cupping golden rice panicles toward the glowing warm horizon"
    },
    {
        "id": "CH04_SC061",
        "dur": "7.35s",
        "words": 28,
        "text": "Thế nhưng, ngay tại thời điểm vị thế của hạt gạo Việt Nam vươn lên đỉnh cao quyền lực đó, một câu hỏi bất ngờ lại xuất hiện.",
        "anatomy": {
            "tier1": "Bàn làm việc của chuyên gia nghiên cứu kinh tế vĩ mô với các tập báo cáo xuất nhập khẩu nông sản và sổ tay phân tích.",
            "tier2": "Một biểu tượng dấu hỏi lớn màu vàng hổ phách ấm áp phát sáng tinh tế bên cạnh biểu đồ xuất khẩu gạo kỷ lục hơn 8 triệu tấn của Việt Nam.",
            "tier3": "Cú máy đẩy chậm vào dấu hỏi chiến lược trên bàn nghiên cứu (Slow push-in toward glowing golden question mark on economic desk)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an analytical research desk with an open trade report displaying booming Vietnamese rice export records beside an elegant glowing amber question mark tab",
        "setting": "a warm scholarly library study room illuminated by soft morning sunlight",
        "motion": "Slow push-in shot toward the open research trade report and the subtle amber question mark"
    },
    {
        "id": "CH04_SC062",
        "dur": "4.46s",
        "words": 17,
        "text": "Nếu chúng ta nắm giữ nguồn lương thực dồi dào đến mức nuôi sống các nước láng giềng,",
        "anatomy": {
            "tier1": "Cụm tổng kho lương thực và nhà máy xay xát lúa gạo hiện đại bậc nhất ven sông Tiền / sông Hậu ngập tràn ánh nắng ấm.",
            "tier2": "Những tháp silo chứa thóc cao vút bằng kim loại sáng loáng, các sà lan đầy ắp lúa vàng tấp nập cập bến bốc dỡ vào hệ thống sấy công nghệ cao.",
            "tier3": "Cú máy góc rộng trượt ngang qua cụm silo dự trữ thóc khổng lồ (Wide cinematic tracking shot past massive grain storage silos and river barges)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an expansive modern agricultural processing hub with gleaming industrial rice storage silos and transport barges unloading raw grain at a river port",
        "setting": "a thriving industrial river port in the Vietnamese delta under bright warm golden sunlight",
        "motion": "Wide cinematic tracking shot gliding past the brimming grain storage silos and river cargo barges"
    },
    {
        "id": "CH04_SC063",
        "dur": "4.20s",
        "words": 16,
        "text": "tại sao mỗi năm Việt Nam vẫn nhập khẩu hàng triệu tấn lúa gạo ngoại?",
        "anatomy": {
            "tier1": "Cửa khẩu đường thủy quốc tế Vĩnh Xương hoặc Bình Hiệp tại biên giới Tây Nam dưới ánh nắng sớm ấm áp.",
            "tier2": "Đoàn ghe gỗ mũi đỏ chở đầy ắp lúa tươi vàng ươm từ Campuchia xếp hàng làm thủ tục kiểm dịch để vào các nhà máy chế biến Việt Nam.",
            "tier3": "Cú máy tĩnh trực diện vào đoàn ghe lúa ngoại nhập và dòng chữ câu hỏi chiến lược (Steady shot on cross-border raw paddy boats arriving at frontier) cùng text overlay góc trái dưới."
        },
        "overlay": "MILLIONS OF TONS IMPORTED?",
        "ref": None,
        "subj": "a bustling border river checkpoint in the Southwest frontier where wooden transport boats loaded with raw paddy from Cambodia glide through inspection checkpoints into Vietnam",
        "setting": "a vibrant border riverway at the Vietnam-Cambodia border under warm morning daylight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the inbound river cargo boats"
    },
    {
        "id": "CH04_SC064",
        "dur": "7.61s",
        "words": 29,
        "text": "Đằng sau sự thật tưởng chừng mâu thuẫn ấy, là một nước cờ kinh tế tinh vi về sự phân công lao động mà ít người để ý tới.",
        "anatomy": {
            "tier1": "Phòng điều hành chiến lược chuỗi cung ứng với màn hình hiển thị sơ đồ phân công lao động khu vực hạ lưu sông Mekong.",
            "tier2": "Sơ đồ dòng chảy giá trị: Nhập lúa thô Campuchia -> Chế biến & tinh chế công nghệ cao tại Việt Nam -> Xuất khẩu gạo cao cấp toàn cầu, mở ra chiếc chìa khóa dẫn thẳng vào Chương 5.",
            "tier3": "Cú máy trượt ngang chậm qua sơ đồ chuỗi giá trị phân công lao động Mekong (Slow horizontal tracking pan across Mekong value chain division map)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a high-tech supply chain operations screen displaying a luminous flowchart of the regional division of labor: raw paddy from Cambodia entering automated high-yield Vietnamese mills and exiting as premium certified export rice",
        "setting": "a sleek modern agribusiness headquarters briefing room under warm amber ceiling downlights",
        "motion": "Slow horizontal tracking pan across the luminous regional division of labor value-chain schematic"
    }
]

print(f"Total scenes to generate for Chapter 4: {len(scenes_data)}")

# 1. Generate Markdown Storyboard
md_lines = [
    "# chapter_04_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 4: Chiếc Bẫy Công Nghiệp Rỗng Ruột: Bài Học Từ Philippines & Lá Chắn An Ninh Bình Nhưỡng",
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
    f"1. **Scene ID chuẩn theo chương:** `CH04_SC001` đến `CH04_SC064` (Khớp 100% với `chapter_04.md` mới cập nhật).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Viện IRRI Los Baños, văn phòng BPO tại Bonifacio Global City/Makati, Cung điện Malacañang, cảng biển Manila Harbor, chợ Divisoria, Nhà khách Chính phủ Hà Nội, Đại lộ Bình Nhưỡng, Cảng Nampo, cửa khẩu đường thủy Tây Nam.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc 18/64 phân cảnh có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. Tất cả 100% bằng Tiếng Anh chuẩn, viết hoa, thuần ASCII.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Ảnh Tham Chiếu Nhân Vật / Địa Danh:**",
    "   - `@irri_los_banos_gate.jpg` sử dụng tại `CH04_SC001` & `CH04_SC002` (Viện Lúa Quốc tế IRRI).",
    "   - `@marcos_jr.jpg` sử dụng tại `CH04_SC038` & `CH04_SC039` (Tổng thống Ferdinand Marcos Jr. ký Sắc lệnh số 39).",
    "   - Bối cảnh Triều Tiên (Quảng trường Bình Nhưỡng, Cảng Nampo, Viện Nông học): Tả thực bằng ngôn ngữ prompt chính xác, không dùng ảnh nhân vật dân sự giả tạo.",
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

with open("episodes/vu-khi-gao-viet-nam/chapter_04_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_04_visual.md ({len(scenes_data)} scenes)")

# 2. Generate prompts_chapter_04.txt
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

# 3. Update scene_timing_map.json
with open("episodes/vu-khi-gao-viet-nam/scene_timing_map.json", "r", encoding="utf-8") as f:
    map_data = json.load(f)

# Keep all scenes from other chapters
other_scenes = [s for s in map_data if s.get("chapter") != "04"]

new_ch04_map = []
for sc in scenes_data:
    entry = {
        "id": sc["id"],
        "chapter": "04",
        "duration_sec": float(sc["dur"].replace("s", "")),
        "text_overlay": sc["overlay"] if sc["overlay"] else "None",
        "sentences": [sc["text"]],
        "visual_summary": f"Tier 1: {sc['anatomy']['tier1']} | Tier 2: {sc['anatomy']['tier2']} | Tier 3: {sc['anatomy']['tier3']}"
    }
    new_ch04_map.append(entry)

# Sort all scenes properly by chapter and id
full_map = other_scenes + new_ch04_map
full_map.sort(key=lambda s: (s.get("chapter", "00"), s.get("id", "")))

with open("episodes/vu-khi-gao-viet-nam/scene_timing_map.json", "w", encoding="utf-8") as f:
    json.dump(full_map, f, ensure_ascii=False, indent=2)

print(f"✅ Synchronized scene_timing_map.json (Total scenes now: {len(full_map)})")
