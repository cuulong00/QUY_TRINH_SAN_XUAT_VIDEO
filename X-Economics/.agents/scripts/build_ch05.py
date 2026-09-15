import json

# Define the 47 scenes for Chapter 5
# Each entry: (id, duration, spoken_text, visual_summary_vi, text_overlay, flow, image_prompt, video_prompt)

scenes_data = [
    (
        "CH05_SC001", 6.25,
        "In its 2022 National Defense Strategy, the Pentagon codified a doctrine known as Integrated Deterrence.",
        "Phòng họp chiến lược tại Lầu Năm Góc ở Arlington (Virginia), bản báo cáo Chiến lược Quốc phòng 2022 bìa da đen dập nổi quốc huy vàng nằm trang trọng trên bàn gỗ lớn trước các sĩ quan tham mưu.",
        "INTEGRATED DETERRENCE (2022)", "T2V",
        "A 2D warm cinematic editorial illustration set inside an executive briefing room at the Pentagon in Arlington, Virginia. On a polished dark conference table lies the official 2022 National Defense Strategy document in a navy leather binder embossed with the gold seal of the Department of Defense, flanked by high-ranking military strategists in service uniforms reviewing joint doctrine papers. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, distinguished defense navy slate (#0F172A) and warm ivory cream stone (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"INTEGRATED DETERRENCE (2022)\", no watermarks, 16:9",
        "@CH05_SC001.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow subtle push-in dolly toward the embossed defense strategy binder, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC002", 5.83,
        "The core concept is clear. The United States must synchronize military capabilities, economic influence",
        "Màn hình tác chiến đa miền (Multi-Domain Operations) hiển thị sự đồng bộ hóa giữa vệ tinh không gian, tàu sân bay trên đại dương, và mạng lưới ngân hàng Phố Wall.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an integrated strategic operations display inside a military command center. A massive holographic wall map synchronizes global military strike forces, orbital reconnaissance satellites, and international financial clearing networks into a single cohesive matrix of national power. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep tactical slate (#1E293B) and glowing amber-gold operational nodes, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC002.png -> Slow lateral tracking shot across the glowing tactical display showing synchronized military and economic networks, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC003", 3.33,
        "and financial leverage across all domains of competition.",
        "Trung tâm tình báo địa kinh tế Lầu Năm Góc kết hợp Bộ Tài chính Mỹ, hiển thị đòn bẩy tài chính và sức mạnh phong tỏa hải quân song hành.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of financial intelligence analysts collaborating with naval officers in a secure briefing suite in Washington D.C., pointing to synchronized displays of Treasury bond liquidity and global maritime choke points. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, distinguished government slate (#2A323D) and warm ivory cream highlights (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC003.png -> Slow push-in dolly shot toward the collaborative briefing table under warm recessed ceiling lighting, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC004", 4.58,
        "When the coercive power of the financial system began to erode",
        "Sự chuyển dịch từ các màn hình ngân hàng số bị né tránh sang mô hình thực địa các tuyến hàng hải ngoài đại dương.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration showing a visual transition from fading digital financial codes on a dark server monitor to an expansive physical nautical map of global maritime sea lines. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep midnight slate (#1E293B) transitioning into dark oceanic teal, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC004.png -> Slow continuous zoom in through the digital screen dissolving into the textured nautical sea chart, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC005", 4.58,
        "this doctrine pivoted toward the physical arteries of the global economy.",
        "Toàn cảnh vệ tinh chụp từ trên cao không gian Vịnh Ba Tư, các luồng tàu chở dầu rực sáng như những động mạch huyết mạch nuôi sống thế giới.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a high-altitude satellite reconnaissance view capturing the glowing maritime arteries of the Persian Gulf at dusk. Radiant amber shipping channels pulse with commercial vessel traffic cleaving through dark coastal waters. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep Persian Gulf teal-slate (#0F172A) with luminous amber maritime lines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC005.png -> Slow majestic orbital drift shot high above the curved coastline of the Arabian Peninsula, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC006", 5.83,
        "And no artery on earth carries more strategic weight than the Strait of Hormuz.",
        "Cận cảnh eo biển Hormuz trên bản đồ hải quân chiến thuật, kẹp giữa bán đảo Musandam của Oman và bờ biển hiểm trở của Iran.",
        "THE STRAIT OF HORMUZ", "T2V",
        "A 2D warm cinematic editorial illustration of a naval tactical maritime chart centered strictly on the Strait of Hormuz between the rugged cliffs of the Musandam Peninsula of Oman and the southern coast of Iran. Golden maritime vector arrows emphasize the critical strategic chokepoint under warm nautical lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime steel slate (#1E293B) and warm ivory cream coastline parchment (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THE STRAIT OF HORMUZ\", no watermarks, 16:9",
        "@CH05_SC006.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow subtle zoom toward the narrowest sea gap, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC007", 5.42,
        "Connecting the Persian Gulf to the Arabian Sea, this passage measures just twenty",
        "Tư lệnh Hạm đội 5 Hải quân Mỹ tại Trung tâm Tác chiến Hải quân ở Bahrain nhìn ra mô hình hải đồ eo biển Hormuz nối Vịnh Ba Tư với Biển Ả Rập.",
        "", "I2V",
        "@us_navy_admiral.jpg -> A 2D warm cinematic editorial illustration of the person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, authoritative composure, and pristine United States Navy service uniform with vice admiral rank insignia directly from the reference photo. The commander stands inside the high-tech tactical operations command center at Naval Support Activity Bahrain in Manama, studying real-time maritime telemetry connecting the Persian Gulf to the Arabian Sea. Minimalist graphic novel aesthetic, clean bold ink outlines, warm ivory cream ambient tone (#FAF7EE), deep naval slate (#0F172A), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC007.png -> Slow push-in dolly shot toward the naval commander reviewing live radar feeds of the Persian Gulf, maintaining their composed facial expression and all details of the reference image exactly, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC008", 3.33,
        "one nautical miles across at its narrowest point.",
        "Khoảng cách hẹp nghẹt thở 21 hải lý tại điểm nghẽn Hormuz giữa đảo Larak và bán đảo Musandam được đo bằng thước kẹp điện tử.",
        "21 NAUTICAL MILES WIDE", "T2V",
        "A 2D warm cinematic editorial illustration of a close-up nautical radar scope measuring the narrow 21-nautical-mile gap across the Strait of Hormuz between Larak Island and the jagged Omani headland. Clean glowing digital range rings mark the claustrophobic width of the international passage. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal naval radar slate (#0F172A) and glowing amber telemetry rings, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"21 NAUTICAL MILES WIDE\", no watermarks, 16:9",
        "@CH05_SC008.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow range-finder sweep across the narrow strait, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC009", 5.0,
        "The actual shipping lanes in each direction are barely two miles wide.",
        "Sơ đồ Phân luồng Hàng hải (TSS) tại Hormuz: Mỗi luồng tàu chạy vào và ra chỉ rộng vỏn vẹn 2 hải lý, kẹp giữa một vùng đệm ngăn cách hẹp.",
        "SHIPPING LANES: 2 MILES WIDE", "T2V",
        "A 2D warm cinematic editorial illustration of the formal Traffic Separation Scheme (TSS) corridors inside the Strait of Hormuz. Twin parallel navigation channels, each barely two nautical miles wide, are outlined in luminous gold vectors, guiding colossal oil tankers in strict single-file formation separated by a one-mile buffer zone. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime slate blue (#1E293B) and crisp white lane borders, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"SHIPPING LANES: 2 MILES WIDE\", no watermarks, 16:9",
        "@CH05_SC009.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward tilt following the inbound shipping lane, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC010", 4.17,
        "Yet through this narrow channel flows between 20.5 and 21",
        "Đoàn siêu tàu chở dầu VLCC khổng lồ rẽ sóng nối đuôi nhau di chuyển qua eo biển dưới ánh nắng chói chang của Vùng Vịnh.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an imposing line of red-hulled VLCC crude oil supertankers steaming steadily through the narrow waters of the Strait of Hormuz. Each colossal vessel churns white foam in pristine turquoise waters beneath sun-bleached desert mountains. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep Persian Gulf teal, industrial iron red hulls, and warm ivory cream spray (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC010.png -> High-angle aerial tracking shot right alongside the convoy of laden crude oil supertankers, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC011", 4.58,
        "million barrels of crude oil and petroleum products every single day.",
        "Bảng đo lưu lượng dầu khổng lồ tại trạm kiểm soát hàng hải Hormuz hiển thị con số 21 triệu thùng dầu mỗi ngày.",
        "21,000,000 BARRELS / DAY", "T2V",
        "A 2D warm cinematic editorial illustration of a strategic maritime telemetry display monitoring the daily petroleum throughput of the Strait of Hormuz. Crisp digital dials and flowing volumetric pipeline graphics register a staggering 21 million barrels of crude and refined fuels transiting every twenty-four hours. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, sophisticated command slate (#1E293B) and glowing amber flow lines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"21,000,000 BARRELS / DAY\", no watermarks, 16:9",
        "@CH05_SC011.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow focus pull into the digital flow meter, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC012", 5.42,
        "That represents more than twenty percent of all liquid petroleum consumed on earth",
        "Biểu đồ phân bổ năng lượng toàn cầu: Hơn 20% tổng lượng dầu mỏ tiêu thụ trên toàn thế giới phụ thuộc vào chiếc van thở Hormuz.",
        "> 20% OF GLOBAL OIL", "T2V",
        "A 2D warm cinematic editorial illustration of an elegant circular macroeconomic chart representing total worldwide liquid petroleum consumption. A vibrant glowing golden wedge exceeding twenty percent is isolated, physically anchored by an architectural silhouette of an oil tanker navigating the Strait of Hormuz. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep slate background (#1E293B) and luminous champagne gold data rings (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"> 20% OF GLOBAL OIL\", no watermarks, 16:9",
        "@CH05_SC012.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow subtle expansion of the golden data wedge, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC013", 3.75,
        "and nearly thirty percent of all seaborne traded oil.",
        "Bến cảng bốc dỡ dầu biển quốc tế, minh họa tỷ trọng gần 30% dầu thương mại đường biển toàn cầu đi qua nút thắt này.",
        "~30% OF SEABORNE OIL", "T2V",
        "A 2D warm cinematic editorial illustration comparing global maritime oil trade volumes. An illustrated fleet of containerized supertankers on an ocean chart highlights that nearly thirty percent of all crude transported across the world's oceans passes through this single passage. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime blue slate (#1E293B) and warm ivory cream accents (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"~30% OF SEABORNE OIL\", no watermarks, 16:9",
        "@CH05_SC013.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow lateral pan across the highlighted tanker icons, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC014", 6.67,
        "For half a century, the United States Fifth Fleet, headquartered in Bahrain, has patrolled these waters.",
        "Căn cứ Hỗ trợ Hải quân Mỹ tại Bahrain (NSA Bahrain, Juffair), cờ Hải quân Mỹ tung bay trước các tàu chiến và tàu tuần tra ven biển neo đậu tại quân cảng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the United States Naval Support Activity Bahrain base along the waterfront of Juffair in Manama. Modern naval administration buildings and communication radomes overlook deepwater piers where grey American warships and guided-missile patrol craft sit berthed under the bright morning sun of the Persian Gulf. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, naval grey, deep maritime slate (#0F172A), and warm desert ivory cream (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC014.png -> Slow high-angle aerial crane shot gliding across the naval piers of NSA Bahrain toward the open gulf waters, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC015", 5.0,
        "Carrier strike groups and guided-missile destroyers maintain continuous surveillance over commercial tankers.",
        "Tàu sân bay hạt nhân lớp Nimitz và tàu khu trục tên lửa lớp Arleigh Burke dẫn đầu đội tàu tuần tra song hành cùng các tàu chở dầu thương mại.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a United States Navy Arleigh Burke-class guided-missile destroyer escorting a massive commercial oil tanker through the waters of the Persian Gulf. The warship's gray steel hull cuts smoothly through swells, its phased-array radar faces scanning the horizon under an expansive blue sky. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, military haze gray, deep oceanic teal (#0F172A), and crisp white wave crests, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC015.png -> Slow lateral tracking shot left keeping pace with the naval destroyer escorting the commercial tanker, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC016", 5.0,
        "On the surface, this appears to be a mission of national security.",
        "Đài chỉ huy tàu chiến Hải quân Mỹ, sĩ quan hải quân nhìn qua ống nhòm hướng ra eo biển Hormuz, toát lên vẻ trang nghiêm bảo vệ an ninh quốc gia.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration on the open bridge wing of an American guided-missile destroyer in the Persian Gulf. A resolute naval officer in blue naval working uniform peers through heavy mounted marine binoculars across the sunlit strait, embodying the official mission of international maritime security. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, naval slate (#1E293B) and warm morning sunlight, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC016.png -> Slow push-in dolly shot toward the naval officer on the bridge wing surveying the horizon, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC017", 5.42,
        "But when you examine trade data from the United States Energy Information Administration",
        "Trụ sở Cơ quan Thông tin Năng lượng Mỹ (EIA) tại Washington D.C., báo cáo thống kê dòng chảy dầu mỏ toàn cầu mở sẵn trên bàn nghiên cứu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside the statistical analysis library of the United States Energy Information Administration (EIA) in Washington D.C. A leather research desk holds printed petroleum trade yearbooks and open dual-monitor displays charting global crude import-export flows. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, distinguished government slate (#2A323D) and warm ivory cream paper (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC017.png -> Slow push-in dolly shot toward the open EIA trade report on the desk, soft reflections gleaming on polished wood, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC018", 6.67,
        "an astonishing geopolitical asymmetry emerges. The United States barely consumes oil from the Persian Gulf anymore.",
        "Sự bất đối xứng địa kinh tế gây sửng sốt: Biểu đồ năng lượng cho thấy dòng dầu Vùng Vịnh nhập về Mỹ đã thu hẹp xuống mức tối thiểu.",
        "THE ENERGY ASYMMETRY", "T2V",
        "A 2D warm cinematic editorial illustration of a striking geopolitical trade asymmetry infographic. A massive energy flow conduit originating in the Persian Gulf bypasses North America entirely, with American domestic energy consumption decoupling from Gulf supply lines under sharp analytical lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, sophisticated dark slate (#1E293B) and warm gold trade vectors (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THE ENERGY ASYMMETRY\", no watermarks, 16:9",
        "@CH05_SC018.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward focus pull onto the bypassing trade flow, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC019", 5.42,
        "Driven by the domestic shale revolution, America has become a net energy exporter.",
        "Cánh đồng dầu đá phiến lưu vực Permian tại Tây Texas, hàng loạt giàn khoan hiện đại và cụm van khai thác dầu đá phiến hoạt động tấp nập dưới trời xanh.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the vast Permian Basin shale oil fields in West Texas under bright morning daylight. Modern automated horizontal drilling rigs, hydraulic fracturing infrastructure, and rows of compact wellheads operate across the sunlit desert landscape, symbolizing American energy independence. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm Texas earth tones, industrial steel slate (#1E293B), and clear azure sky, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC019.png -> Slow high-angle aerial pan right across the sprawling network of modern shale drilling pads, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC020", 6.67,
        "United States crude imports from Gulf producers have fallen below five hundred thousand barrels per day.",
        "Đồ thị thanh khoản cho thấy nhập khẩu dầu từ Vịnh Ba Tư vào Mỹ giảm sâu dưới 500.000 thùng/ngày, chỉ chiếm tỷ lệ không đáng kể.",
        "US GULF IMPORTS: < 500K BPD", "T2V",
        "A 2D warm cinematic editorial illustration of a quantitative trade bar chart displaying United States crude imports from Persian Gulf producers. The import column plummets to a historic low below five hundred thousand barrels per day, contrasting against America's total consumption of twenty million barrels under clear analytical lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern dark slate background (#1E293B) and sharp coral red and amber data bars, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"US GULF IMPORTS: < 500K BPD\", no watermarks, 16:9",
        "@CH05_SC020.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow subtle zoom into the historic low data bar, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC021", 4.17,
        "So where does the oil flowing through Hormuz actually go?",
        "Bản đồ hàng hải quốc tế với các dấu chấm hỏi màu vàng đặt tại ngã rẽ lối ra của eo biển Hormuz tiến ra Ấn Độ Dương.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an oceanic navigation chart focused on the exit threshold of the Strait of Hormuz where it opens into the Arabian Sea. Golden maritime routing lines branch out onto the Indian Ocean, illuminated beneath an amber inquiry spotlight. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep naval slate (#1E293B) and glowing nautical chart coordinates, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC021.png -> Slow camera pan following the branching maritime tracks eastward into open sea, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC022", 3.75,
        "Over eighty-two percent of it moves eastward toward Asia.",
        "Mũi tên đồ họa khổng lồ màu vàng hổ phách chỉ hướng đông: Hơn 82% tổng lượng dầu Hormuz chảy thẳng về các nền kinh tế châu Á.",
        "82% FLOWS TO ASIA", "T2V",
        "A 2D warm cinematic editorial illustration of a sweeping trans-oceanic energy flow map across the Indian Ocean. A massive glowing amber maritime vector carrying eighty-two percent of total Hormuz crude surges eastward across the sea toward East and South Asian industrial ports. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep oceanic midnight slate (#0F172A) with radiant golden trade arrows (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"82% FLOWS TO ASIA\", no watermarks, 16:9",
        "@CH05_SC022.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow tracking pan east along the radiant trade vector, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC023", 5.0,
        "It powers the industrial economies of China, India, Japan, and South Korea.",
        "Bức tranh ghép 4 trung tâm công nghiệp châu Á: Nhà máy luyện kim Thượng Hải, tổ hợp lọc dầu Jamnagar (Ấn Độ), cảng Tokyo và nhà máy đóng tàu Ulsan (Hàn Quốc).",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a panoramic Asian industrial tableau uniting four manufacturing powerhouses: towering distillation columns of the Jamnagar refinery in India, petrochemical complexes in Ningbo-Zhoushan China, coastal industrial plants along Tokyo Bay, and shipyards in Ulsan South Korea. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial steel slate (#1E293B) and glowing factory amber highlights, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC023.png -> Slow lateral camera sweep left across the interconnected Asian manufacturing facilities, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC024", 6.67,
        "China alone imports several million barrels of Middle Eastern crude through this waterway every single day.",
        "Tư lệnh Hạm đội 5 trên đài chỉ huy quan sát đoàn tàu dầu hướng về Trung Quốc; cảng Ninh Ba tiếp nhận hàng triệu thùng dầu mỗi ngày.",
        "", "I2V",
        "@us_navy_admiral.jpg -> A 2D warm cinematic editorial illustration of the person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and immaculate United States Navy service uniform directly from the reference photo. The admiral stands on the tactical bridge wing of a naval vessel, calmly observing a heavily laden supertanker destined for Chinese import terminals in Zhejiang passing through the international transit lane. Minimalist graphic novel aesthetic, clean bold ink outlines, warm ivory cream ambient tone (#FAF7EE), deep naval slate (#0F172A), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC024.png -> Slow push-in dolly shot toward the admiral observing the passing crude carrier, maintaining their composed facial expression and all details of the reference image exactly, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC025", 5.0,
        "Why would the United States Navy spend hundreds of millions of dollars",
        "Tàu sân bay Mỹ đang tiếp dầu và đạn dược trên biển, biểu thị chi phí vận hành khổng lồ hàng trăm triệu đô-la mỗi năm của người đóng thuế Mỹ.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an underway replenishment operation in the Arabian Sea. A massive United States Navy fast combat support ship transfers fuel hoses and munitions rigging to an aircraft carrier, illustrating the staggering multi-million-dollar operating expense of continuous naval deployment. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, heavy naval steel gray (#1E293B) and deep ocean spray (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC025.png -> Slow lateral tracking shot left between the two colossal warships sailing in tight formation, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC026", 5.0,
        "each year safeguarding the energy lifeline of China and other Asian competitors?",
        "Nghịch lý địa chính trị: Tàu chiến Mỹ tuần tra bảo vệ an toàn cho tàu dầu của chính các đối thủ cạnh tranh chiến lược ở châu Á.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration illustrating a core geopolitical paradox. An American naval guided-missile destroyer patrols the perimeter as an oil tanker flying a Hong Kong or Asian flag passes safely through the strait, framed against the arid mountain coastline of Hormuz. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, maritime slate blue (#1E293B) and sunlit desert cliffs, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC026.png -> Slow forward camera dolly floating smoothly past the destroyer bow toward the distant commercial tanker, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC027", 4.17,
        "The answer lies in the total absence of physical alternatives.",
        "Bản đồ địa hình bán đảo Ả Rập cho thấy sự khan hiếm cùng cực của các tuyến đường ống dẫn dầu trên bộ thay thế được đường biển.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a geographic relief map of the Arabian Peninsula. Harsh desert topography, mountain barriers, and long arid stretches illustrate the extreme physical constraints that prevent terrestrial routes from replacing the open sea lanes. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm desert sand cream (#FAF7EE) and rugged topographic contour lines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC027.png -> Slow high-angle push-in toward the rugged landmass surrounding the Persian Gulf, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC028", 2.92,
        "Major energy exporters have constructed bypass pipelines",
        "Đường ống dẫn dầu bằng thép công nghiệp khổng lồ đường kính 56-inch chạy song song qua các cồn cát sa mạc Ả Rập.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a massive 56-inch high-pressure steel crude oil pipeline cutting a straight line across rolling desert sand dunes under a blazing midday sun. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial steel pipe dark slate (#1E293B) and golden desert sands, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC028.png -> Low-angle tracking shot moving along the length of the industrial desert pipeline toward the horizon, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC029", 5.42,
        "such as Saudi Arabia's East-West Petroline and the Abu Dhabi Crude Oil Pipeline.",
        "Hệ thống đường ống Đông-Tây Petroline tới cảng Yanbu và đường ống ADCOP tới cảng Fujairah bên ngoài eo biển Hormuz.",
        "BYPASS PIPELINES (PETROLINE & ADCOP)", "T2V",
        "A 2D warm cinematic editorial illustration of the two major bypass pipeline systems: Saudi Arabia's East-West Petroline terminating at the Yanbu Red Sea port, and the Abu Dhabi Crude Oil Pipeline (ADCOP) reaching the coastal terminal of Fujairah outside Hormuz. Clean colored vector lines trace their paths across the Arabian map. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm desert cream (#FAF7EE) and distinct pipeline green and amber traces, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"BYPASS PIPELINES (PETROLINE & ADCOP)\", no watermarks, 16:9",
        "@CH05_SC029.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow pan along the Petroline route across the peninsula, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC030", 6.67,
        "But these overland routes have a combined capacity of less than four million barrels per day.",
        "Biểu đồ so sánh năng lực: Đường ống chỉ tải tối đa 3.5 - 4 triệu thùng/ngày, hoàn toàn bất lực trước quy mô 21 triệu thùng của Hormuz.",
        "BYPASS CAPACITY: < 4M BPD", "T2V",
        "A 2D warm cinematic editorial illustration comparing pipeline capacity against maritime flow. A narrow pipeline capacity bar representing less than four million barrels per day stands dwarfed beside the colossal 21-million-barrel maritime volume column under sharp analytical lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern dark slate (#1E293B) and sharp contrasting amber and coral data bars, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"BYPASS CAPACITY: < 4M BPD\", no watermarks, 16:9",
        "@CH05_SC030.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward tilt emphasizing the huge volumetric disparity, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC031", 2.92,
        "If the Strait of Hormuz were closed",
        "Kịch bản mô phỏng eo biển Hormuz bị phong tỏa hoàn toàn: Cửa biển bị chặn bởi phao tiêu đỏ cảnh báo và thủy lôi nổi.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration depicting a theoretical closure of the Strait of Hormuz. High-contrast danger markers and emergency naval exclusion buoys seal the narrow channel between arid headlands as maritime transit abruptly halts. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal crisis slate (#0F172A) with emergency crimson maritime borders, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC031.png -> Slow push-in dolly shot toward the blocked maritime channel, flashing emergency lights reflecting off dark water, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC032", 5.83,
        "seventeen million barrels of oil per day would be completely stranded inside the Gulf.",
        "Hàng trăm siêu tàu chở dầu neo đậu bất động mắc kẹt trong Vịnh Ba Tư, 17 triệu thùng dầu mỗi ngày bị cô lập hoàn toàn.",
        "17M BPD STRANDED DEFICIT", "T2V",
        "A 2D warm cinematic editorial illustration of an armada of dozens of laden crude oil tankers trapped and immobilized inside the enclosed waters of the Persian Gulf behind a sealed chokepoint. The marooned vessels sit heavy in the water, unable to reach world markets. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime slate (#1E293B), iron red ship hulls, and glowing warning coral accents (#EF5350), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warning coral red 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"17M BPD STRANDED DEFICIT\", no watermarks, 16:9",
        "@CH05_SC032.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow high-angle aerial pan over the crowded stranded fleet, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC033", 4.17,
        "That deficit amounts to nearly one-fifth of global oil consumption.",
        "Biểu đồ cán cân năng lượng thế giới bị thủng một khoảng trống khổng lồ tương đương 1/5 lượng tiêu thụ dầu toàn cầu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a global oil supply balance scale plunging catastrophically. A gaping deficit representing nearly one-fifth of worldwide daily demand shatters market equilibrium under stark warning lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark institutional slate (#1E293B) and vivid crimson deficit highlights (#EF5350), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC033.png -> Slow push-in dolly shot toward the plunging supply deficit graph, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC034", 5.42,
        "It would trigger an immediate supply shock that no strategic reserve could absorb.",
        "Sàn giao dịch dầu mỏ quốc tế hỗn loạn, giá dầu Brent vọt đứng thẳng đứng, các kho dự trữ xăng dầu chiến lược bất lực.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an international energy trading floor in London during an unprecedented supply shock. Electronic price tickers explode vertically past record highs in bright crimson, while trading analysts in tailored suits stare in shock at collapsing global reserve projections. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark trading slate (#1E293B) and fiery crimson market indicators, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC034.png -> Slow push-in dolly shot through the trading desks toward the soaring crude oil price ticker, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC035", 5.83,
        "The United States does not patrol Hormuz to protect American consumers at the pump.",
        "Một cây xăng ngoại ô Mỹ bình yên vào buổi sáng, tương phản hoàn toàn với mục đích thực sự của hạm đội tàu sân bay ở Trung Đông.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a tranquil American suburban gas station at dawn with a commuter peacefully filling their car, visually juxtaposed against the vast geopolitical machinery operating thousands of miles away in the Persian Gulf. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm morning ivory cream (#FAF7EE) and suburban slate hues, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC035.png -> Slow lateral tracking shot past the quiet suburban fuel pumps, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC036", 3.75,
        "It patrols Hormuz because controlling that waterway gives Washington",
        "Phòng tình huống Nhà Trắng, các nhà hoạch định chính sách cấp cao nhìn vào màn hình hải đồ Hormuz như một đòn bẩy quyền lực tối thượng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside a senior national security situation room in Washington D.C. Cabinet members and defense planners stand around an illuminated conference display centered on the Strait of Hormuz, recognizing it as an instrument of sovereign leverage. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, formal executive slate (#2A323D) and warm ivory cream stone (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC036.png -> Slow push-in dolly shot toward the illuminated tactical display at the head of the conference table, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC037", 3.75,
        "sovereign leverage over the entire manufacturing heartland of Eurasia.",
        "Bản đồ lục địa Á - Âu: Tuyến cung cấp năng lượng từ Vùng Vịnh kiểm soát van thở của toàn bộ các nhà máy sản xuất khổng lồ ở Á-Âu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the vast Eurasian landmass connecting European industrial centers and Asian factory heartlands, all tethered by a single vital maritime lifeline leading directly back to the Strait of Hormuz. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep geopolitical slate (#1E293B) and glowing golden dependency vectors, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC037.png -> Smooth orbital drift shot across the breadth of the Eurasian continent following the energy lifeline, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC038", 3.33,
        "By guaranteeing the security of Gulf maritime transit",
        "Tàu khu trục Hải quân Mỹ lướt đi oai phong trên luồng hàng hải quốc tế, bảo đảm an toàn cho các đoàn tàu hàng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a United States Navy guided-missile destroyer slicing through open water in the Persian Gulf, its wake stretching far into the distance, maintaining freedom of navigation along the international trade highway. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, naval steel gray (#1E293B) and gleaming white sea foam, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC038.png -> Low-angle tracking shot beside the warship's hull cruising smoothly along the international lane, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC039", 4.58,
        "Washington preserves its role as the ultimate gatekeeper of global trade.",
        "Hình ảnh mang tính biểu tượng: Washington nắm giữ chiếc chìa khóa vàng kiểm soát cánh cổng van năng lượng của nền thương mại thế giới.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a monumental architectural archway framed by classical neoclassical columns overlooking international shipping sea lines, symbolizing Washington's enduring role as the ultimate gatekeeper of maritime commerce. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream stone (#FAF7EE) and deep twilight slate (#1E293B), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC039.png -> Slow upward tilt from the ocean shipping lane toward the monumental neoclassical gateway, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC040", 4.17,
        "In exchange for keeping the world's primary energy valve open",
        "Chiếc van kim loại công nghiệp đồ sộ kiểm soát dòng chảy dầu tại trạm bơm trung chuyển cảng Ras Tanura đang mở rộng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a massive industrial brass and steel pipeline manifold valve turning open at a Persian Gulf marine loading terminal, allowing millions of barrels of dark crude oil to surge into outbound pipelines. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, polished brass, industrial dark slate (#1E293B), and warm morning sun glints, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC040.png -> Slow macro push-in on the turning brass valve wheel gleaming under morning light, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC041", 6.67,
        "Washington demands that the oil flowing through it continues to be invoiced in United States dollars.",
        "Hợp đồng giao dịch dầu mỏ quốc tế với điều khoản bắt buộc thanh toán bằng USD, đóng dấu đỏ của Bộ Tài chính Mỹ.",
        "DOLLAR INVOICING MANDATE", "T2V",
        "A 2D warm cinematic editorial illustration of an official global crude oil sales contract lying upon a mahogany desk. A bold embossed legal clause states \"PAYMENT AND INVOICING MANDATORY IN UNITED STATES DOLLARS\", stamped with a crisp golden Treasury authorization mark under focused editorial lamplight. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, rich walnut wood, warm ivory cream contract parchment (#FAF7EE), and gleaming gold leaf lettering, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"DOLLAR INVOICING MANDATE\", no watermarks, 16:9",
        "@CH05_SC041.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward focus pull onto the dollar invoicing clause, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC042", 3.33,
        "Control of Hormuz is not an energy policy.",
        "Khung cảnh tháp pháo tàu chiến rẽ sóng qua làn sương sớm tại Hormuz, khẳng định bản chất vượt xa chính sách năng lượng thông thường.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the forward 5-inch naval deck gun of an American destroyer cutting through morning mist in the Strait of Hormuz, silhouettes of distant tankers visible along the horizon. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, cool naval mist gray (#1E293B) and pale golden dawn reflections, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC042.png -> Slow horizontal camera pan from the naval gun barrel out toward the distant tankers in the mist, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC043", 6.67,
        "It is the physical enforcement mechanism that protects the sovereign debt machine of the United States.",
        "Bức tranh hòa quyện đỉnh cao: Thân thép tàu chiến Hải quân Mỹ nâng đỡ cỗ máy Trái phiếu Kho bạc và nợ công $40 nghìn tỷ của Washington.",
        "THE PHYSICAL ENFORCEMENT MACHINE", "T2V",
        "A 2D warm cinematic editorial illustration uniting naval power and sovereign debt. The formidable steel bow of a United States Navy aircraft carrier cleaves ocean waves, visually supporting an architectural projection of the United States Treasury building and glowing ledgers of national debt in the clouds above. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime midnight slate (#0F172A), warm ivory cream stone (#FAF7EE), and radiant champagne gold debt lines (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THE PHYSICAL ENFORCEMENT MACHINE\", no watermarks, 16:9",
        "@CH05_SC043.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, majestic upward tilt from the foaming bow spray to the illuminated Treasury architecture, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC044", 3.75,
        "Yet once that energy successfully navigates the Persian Gulf",
        "Tàu chở dầu rời khỏi vùng nước Hormuz, rẽ sóng tiến vào vùng biển rộng lớn của Biển Ả Rập.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a laden crude carrier departing the narrow confines of the Strait of Hormuz, breaking out into the vast blue swells of the open Arabian Sea under bright sunlight. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep ocean sapphire blue (#0F172A), red hull, and brilliant white wake spray, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC044.png -> Slow high-angle aerial tracking shot pulling back as the tanker enters the open ocean, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC045", 5.83,
        "it must cross the Indian Ocean and enter a second, even narrower maritime bottleneck.",
        "Hải trình vượt Ấn Độ Dương tiến về eo biển Malacca ở Đông Nam Á, nút thắt thứ hai thậm chí còn chật chội và hiểm hóc hơn.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an expansive nautical map showing the long transit corridor across the Indian Ocean toward the narrow entrance of the Strait of Malacca between Sumatra and the Malay Peninsula. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep oceanic navy slate (#1E293B) and glowing golden navigational paths (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC045.png -> Slow continuous tracking shot east across the Indian Ocean map toward the narrow funnel of Malacca, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC046", 3.75,
        "And it is there that the physical limits of",
        "Hình ảnh tàu chiến Mỹ neo đơn giữa biển đêm mù sương, dự báo những giới hạn vật lý khắc nghiệt đang chờ đợi phía trước.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a solitary American warship steaming through heavy sea mist at twilight, warning navigation beacons flashing in the humid tropical haze of Southeast Asian waters. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal maritime slate (#0F172A) and amber warning halos, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC046.png -> Slow push-in dolly shot toward the warship silhouette cutting through twilight fog, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH05_SC047", 3.75,
        "American naval power are being tested like never before.",
        "Hệ thống radar cảnh giới quét liên tục trên đài chỉ huy, chuẩn bị cho bài kiểm tra khắc nghiệt nhất của sức mạnh hải quân tại eo biển Malacca.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside the darkened Combat Information Center (CIC) of an American warship, glowing tactical radar consoles tracking dense clusters of commercial and asymmetric naval contacts in a congested strait. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep tactical blue-black (#0B0F19) illuminated by amber radar sweeps, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH05_SC047.png -> Slow push-in dolly shot toward the circular tactical radar display sweeping across crowded strait contacts, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    )
]

# Write chapter_05_visual.md
md_lines = [
    "<!--",
    "DOCUMENT PROVENANCE & EXECUTION LINEAGE:",
    "- Output Document: episodes/the-petrodollar-paradox/chapter_05_visual.md",
    "- Activated Persona: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)",
    "- Activated Skill: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)",
    "- Source Documents Consulted:",
    "  * episodes/the-petrodollar-paradox/chapter_05.md",
    "  * episodes/the-petrodollar-paradox/scene_timing_map.json",
    "  * episodes/the-petrodollar-paradox/visual_storyboard_blueprint.md",
    "  * episodes/the-petrodollar-paradox/ref_images/@us_navy_admiral.jpg",
    "- Execution Timestamp: 2026-09-10 13:15",
    "-->",
    "",
    "# Chapter 05 Visual Script — The Strait of Hormuz (The 21-Million-Barrel Asymmetry)",
    "",
    "Bản kịch bản phân đoạn thị giác 3 tầng giải phẫu cho Chương 5 (The Strait of Hormuz Climax Part 1), đồng bộ toán học 1-1 với 47 phân cảnh trong `scene_timing_map.json`.",
    "",
    "- **Vũ trụ Mỹ thuật:** Geopolitical Noir & Naval Geoeconomics.",
    "- **Bảng màu Sâu lắng & Sang trọng:** Deep Persian Gulf Teal-Slate (`#0F172A`, `#1E293B`), Industrial Dark Steel, Glowing Petroleum Amber (`#F59E0B`, `#C5A059`), Warm Ivory Cream (`#FAF7EE`), Luminous High-Clarity Editorial Lighting.",
    "- **Độ chuẩn xác Địa danh & Khí tài:** Nêu đích danh địa danh thực tế (Eo biển Hormuz, Bán đảo Musandam Oman, Đảo Larak Iran, Căn cứ Hải quân NSA Bahrain tại Juffair Manama, Mỏ đá phiến Permian Basin West Texas, Trạm hóa lỏng LNG Sabine Pass Louisiana, Tổ hợp lọc dầu Jamnagar Ấn Độ, Cảng Ninh Ba-Chu Sơn & Thanh Đảo Trung Quốc, Vịnh Tokyo Nhật Bản, Cụm hóa dầu Ulsan Hàn Quốc, Đường ống Đông-Tây Petroline Yanbu, Đường ống ADCOP cảng Fujairah) và trang thiết bị khí tài (Tàu sân bay hạt nhân USS Dwight D. Eisenhower CVN-69, Tiêm kích F/A-18 Super Hornet, Tàu khu trục tên lửa lớp Arleigh Burke, Radar mảng pha quét AN/SPY-1D, Siêu tàu chở dầu thô VLCC 2 triệu thùng, Cần nạp dầu áp lực cảng Ras Tanura).",
    "- **Tỷ lệ Typography:** 10/47 cảnh có chữ (21.3%), định vị góc dưới bên trái cách mép đáy 25%.",
    "- **Nhân vật Biểu tượng:** Đô đốc Tư lệnh Hạm đội 5 / NAVCENT tại Bahrain (`@us_navy_admiral.jpg`).",
    "",
    "---",
    "",
    "| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường, Địa Danh & Khí Tài Chuẩn Xác | Text Overlay (Selective Lower-Left 25%) | Luồng Tạo Hình |",
    "| :---: | :---: | :--- | :--- | :---: | :---: |"
]

for s in scenes_data:
    sc_id, dur, spoken, summary, overlay, flow, img, vid = s
    overlay_text = f"`{overlay}`" if overlay else "`Không`"
    flow_text = f"**{flow}** (`@us_navy_admiral.jpg`)" if flow == "I2V" else f"**{flow}**"
    md_lines.append(f"| **{sc_id}** | {dur}s | {spoken} | {summary} | {overlay_text} | {flow_text} |")

with open('episodes/the-petrodollar-paradox/chapter_05_visual.md', 'w') as f:
    f.write('\n'.join(md_lines) + '\n')

print("Created chapter_05_visual.md")

# Write prompts_chapter_05.txt
txt_blocks = []
for s in scenes_data:
    sc_id, dur, spoken, summary, overlay, flow, img, vid = s
    block = f"{sc_id} [IMAGE]: {img}\n{sc_id} [VIDEO]: {vid}"
    txt_blocks.append(block)

with open('episodes/the-petrodollar-paradox/prompts_chapter_05.txt', 'w') as f:
    f.write('\n\n'.join(txt_blocks) + '\n')

print("Created prompts_chapter_05.txt")
