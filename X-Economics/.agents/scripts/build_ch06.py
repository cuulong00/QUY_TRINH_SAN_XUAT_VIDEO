import json

scenes_data = [
    (
        "CH06_SC001", 6.25,
        "Beyond the Indian Ocean lies the world's most congested maritime chokepoint: the Strait of Malacca.",
        "Toàn cảnh eo biển Malacca nhìn từ trên cao, hàng trăm tàu chở hàng viễn dương và tàu dầu nối đuôi nhau ken đặc trên mặt nước màu lam ngọc giữa Sumatra và bán đảo Mã Lai.",
        "THE STRAIT OF MALACCA", "T2V",
        "A 2D warm cinematic editorial illustration of a breathtaking high-altitude aerial view over the Strait of Malacca. Dense nautical convoys of international container ships and crude oil supertankers steam tightly between the lush coastline of Sumatra and the Malay Peninsula under humid tropical clouds. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, maritime slate blue (#1E293B) and emerald tropical waters (#26A69A), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing emerald green 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THE STRAIT OF MALACCA\", no watermarks, 16:9",
        "@CH06_SC001.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow forward aerial drift over the crowded maritime strait, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC002", 4.58,
        "Stretching between the Indonesian island of Sumatra and the Malay Peninsula",
        "Hải đồ vệ tinh chi tiết thể hiện hành lang biển hẹp dài 800 km kẹp giữa bờ biển rừng rậm Sumatra (Indonesia) và dải bờ biển công nghiệp của Malaysia.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a cartographic satellite relief map depicting the 800-kilometer corridor of the Strait of Malacca flanked by the dense forests of Sumatra, Indonesia to the southwest and the bustling ports of the Malay Peninsula to the northeast. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, humid maritime slate (#334155) and warm ivory cream parchment (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC002.png -> Slow camera pan following the length of the narrow sea passage southeastward, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC003", 5.42,
        "this narrow corridor carries over twenty-five percent of all traded goods on earth.",
        "Đồ thị tỷ trọng thương mại toàn cầu: Hơn 25% tổng lượng hàng hóa thương mại thế giới dồn vào chiếc phễu eo biển Malacca.",
        "> 25% OF GLOBAL TRADE", "T2V",
        "A 2D warm cinematic editorial illustration of a global maritime trade chart highlighting the Strait of Malacca. A glowing emerald vector ring indicates that over twenty-five percent of all seaborne traded merchandise on earth passes through this single funnel. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime slate (#1E293B) and luminous emerald green data rings (#26A69A), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing emerald green 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"> 25% OF GLOBAL TRADE\", no watermarks, 16:9",
        "@CH06_SC003.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow subtle zoom in on the global trade percentage, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC004", 6.67,
        "More critically, it carries between fifteen and sixteen million barrels of crude oil every single day.",
        "Đoàn tàu chở dầu nối đuôi nhau qua Malacca, đồng hồ lưu lượng hiển thị 15 đến 16 triệu thùng dầu thô mỗi ngày tiến về Đông Á.",
        "15 - 16M BPD CRUDE OIL", "T2V",
        "A 2D warm cinematic editorial illustration of giant crude oil tankers transiting in close formation through the southern waters of the Malacca Strait. A crisp analytical digital readout indicates an immense daily throughput between fifteen and sixteen million barrels of crude oil bound for East Asian industrial powerhouses. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep oceanic teal (#0F172A), red ship hulls, and glowing amber metrics, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"15 - 16M BPD CRUDE OIL\", no watermarks, 16:9",
        "@CH06_SC004.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow lateral pan tracking the loaded tankers steaming forward, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC005", 4.17,
        "At its narrowest juncture, the Phillips Channel south of Singapore",
        "Kênh Phillips ở phía nam Singapore, nơi các bãi cạn san hô và luồng hàng hải thu hẹp nghẹt thở chỉ còn 1.5 hải lý.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the narrow Phillips Channel south of Singapore. Shallow sandbanks and coral reefs constrict the maritime transit corridor, forcing colossal container ships and crude supertankers to navigate in strict single-file precision under intense tropical sun. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, tropical turquoise shallows and deep blue channel slate (#1E293B), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC005.png -> Slow high-angle push-in toward the narrowest sea constriction between the navigation buoys, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC006", 5.42,
        "the shipping lane narrows to just 1.5 nautical miles, barely 2.8 kilometers across.",
        "Thước đo radar điện tử trên đài quan sát Singapore hiển thị bề rộng luồng tàu chỉ vỏn vẹn 1.5 hải lý (2.8 km), tương đương vài thân tàu chở dầu.",
        "PHILLIPS CHANNEL: 1.5 NM", "T2V",
        "A 2D warm cinematic editorial illustration of an electronic maritime navigation radar display centered on the Phillips Channel south of Singapore. Calibrated range brackets measure the extreme 1.5-nautical-mile (2.8 kilometer) bottleneck, framed by the distant gleaming skyscrapers of the Singapore financial district. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal command slate (#0F172A) with sharp emerald distance brackets (#26A69A), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing emerald green 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"PHILLIPS CHANNEL: 1.5 NM\", no watermarks, 16:9",
        "@CH06_SC006.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow zoom into the 1.5 NM distance readout, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC007", 5.42,
        "For the People's Republic of China, this passage represents an acute existential vulnerability.",
        "Phòng tình huống quân sự tại Bắc Kinh, các sĩ quan cấp cao đứng quanh sa bàn điện tử tập trung ánh mắt vào eo biển Malacca như một tử huyệt địa chiến lược.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside a senior strategic command room in Beijing, China. Chinese military strategists in dark uniforms stand around a glowing digital relief table intently studying the maritime bottleneck of Malacca, recognizing it as an acute existential vulnerability to national survival. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, formal command slate (#1E293B) and amber-red strategic boundary vectors, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC007.png -> Slow push-in dolly shot toward the illuminated situation table over the shoulders of the planners, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC008", 4.58,
        "Chinese strategists have long termed this strategic anxiety the Malacca Dilemma.",
        "Bản đồ chiến lược mang tên 'Thế lưỡng nan Malacca' với chiếc cùm sắt địa kinh tế khóa chặt tuyến vận tải năng lượng hướng về bờ biển Trung Quốc.",
        "THE MALACCA DILEMMA", "T2V",
        "A 2D warm cinematic editorial illustration of an analytical geopolitical map illustrating the famous 'Malacca Dilemma'. A stylized glowing metallic restraint encircles the narrow strait south of Singapore, tethering all maritime energy routes supplying the industrial factories of southern China. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark strategic slate (#1E293B) and warning amber coordinate lines (#F59E0B), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warning amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THE MALACCA DILEMMA\", no watermarks, 16:9",
        "@CH06_SC008.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward focus pull onto the Malacca pinch point, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC009", 5.83,
        "Nearly eighty percent of China's maritime crude oil imports must pass through this single",
        "Đoàn tàu siêu trọng tải chở dầu thô từ Trung Đông và Tây Phi đổ dồn về lối vào eo biển Malacca, chiếm gần 80% dầu nhập khẩu của Trung Quốc.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a dense convergence of crude oil supertankers steaming from the Indian Ocean into the western entrance of the Malacca Strait, visually funneling nearly eighty percent of China's seaborne energy supply into a single narrow throat. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, maritime slate blue (#1E293B) and iron-red tanker hulls, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC009.png -> Slow high-angle aerial tracking shot capturing the convergence of multiple supertankers into the single sea lane, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC010", 1.25,
        "highly concentrated bottleneck.",
        "Cận cảnh mũi tàu chở dầu rẽ sóng luồn qua khe nước hẹp kẹp giữa các ngọn hải đăng cảnh báo.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the bulbous steel bow of a colossal crude carrier cleaving heavy ocean spray directly past an offshore navigation lighthouse in the tightest passage of the strait. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep teal-slate water (#0F172A) and bright white bow wave, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC010.png -> Quick dramatic low-angle push-in toward the towering steel bow cutting through the water, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC011", 6.67,
        "The United States Navy's Seventh Fleet, operating from bases in Japan and logistic facilities in Singapore",
        "Soái hạm USS Blue Ridge (LCC-19) của Hạm đội 7 Hải quân Mỹ tại căn cứ Yokosuka (Nhật Bản) và cơ sở hậu cần Changi tại Singapore.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the United States Navy Seventh Fleet command presence in the Indo-Pacific. The command ship USS Blue Ridge (LCC-19) sits moored beside naval piers at Yokosuka Naval Base in Japan, alongside a split-screen architectural view of naval logistics facilities at Changi Naval Base in Singapore. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, naval haze gray (#1E293B), warm ivory cream stone (#FAF7EE), and calm harbor waters, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC011.png -> Slow lateral camera pan left across the naval command vessels berthed at Yokosuka, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC012", 5.42,
        "exercises dominant maritime influence over these waters. If a major geopolitical conflict erupted",
        "Tàu tuần dương mang tên lửa dẫn đường lớp Ticonderoga và tàu khu trục lớp Arleigh Burke diễn tập phong tỏa trên vùng biển Đông Nam Á.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an American naval surface action group, led by a guided-missile cruiser and destroyers, executing precision tactical maneuvers across Southeast Asian waters, exerting undisputed maritime dominance over regional trade routes. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep oceanic slate (#1E293B) and clean white wake lines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC012.png -> Slow forward tracking shot parallel to the warship formation cutting through ocean swell, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC013", 6.25,
        "the United States possesses the physical capacity to cut China's seaborne energy supply at will.",
        "Mô phỏng kịch bản phong tỏa vật lý: Chiến hạm Mỹ chốt chặn cửa ngõ Malacca, van cung cấp dầu trên biển bị ngắt dứt khoát.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration simulating a maritime naval interdiction scenario. American warships establish a distant naval blockade line across the eastern exit of the Malacca Strait, effectively intercepting seaborne energy cargoes destined for northern ports under clear dawn skies. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, cool naval slate blue (#1E293B) and sharp dawn amber sky highlights, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC013.png -> Slow push-in dolly shot toward the naval blockade picket line spanning the horizon, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC014", 3.75,
        "Yet maintaining global dominance across two separate oceanic theatres",
        "Bản đồ hai đại dương: Căng thẳng dàn trải đồng thời tại Trung Đông (Vịnh Ba Tư / Biển Đỏ) và Tây Thái Bình Dương.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a global dual-theatre maritime map. Luminous blue deployment rings highlight simultaneous high-intensity naval commitments in the Persian Gulf and Red Sea on the left, and the Western Pacific on the right. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep geopolitical slate (#1E293B) and dual illuminated naval hubs, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC014.png -> Slow pull-back orbital shot revealing the vast distance separating the two operational theatres, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC015", 3.75,
        "has exposed a fatal vulnerability in America's military posture.",
        "Vết nứt trên biểu tượng huy hiệu hải quân Lầu Năm Góc, bộc lộ điểm yếu chết người trong thế bố phòng quân sự toàn cầu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a stylized bronze United States Department of Defense seal displaying subtle structural stress fractures radiating across its surface, illuminated under somber, analytical lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep defense navy slate (#0F172A) and aged bronze accents, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC015.png -> Slow push-in dolly shot toward the fine stress lines on the bronze military seal, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC016", 3.33,
        "That vulnerability is not a shortage of dollars.",
        "Tập ngân sách quốc phòng Mỹ khổng lồ 850 tỷ USD nằm trên bàn họp Quốc hội, tiền bạc in ra không thiếu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a towering stack of United States federal defense budget authorization volumes totaling eight hundred and fifty billion dollars lying on a Capitol Hill committee table. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, formal legislative slate (#2A323D) and warm ivory cream pages (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC016.png -> Slow upward tilt shot up the imposing height of the printed defense budget documents, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC017", 4.58,
        "It is a severe physical crisis in the defense industrial base.",
        "Bên trong nhà máy chế tạo tên lửa vắng vẻ, dây chuyền lắp ráp cơ khí chính xác đối mặt tình trạng thiếu hụt phôi đạn và công nhân lành nghề.",
        "DEFENSE INDUSTRIAL CRISIS", "T2V",
        "A 2D warm cinematic editorial illustration inside an aerospace defense manufacturing facility in Tucson, Arizona. Automated precision tooling machines sit idle beside half-completed missile fuselage casings on clean industrial factory floors, illustrating physical production bottlenecks. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial steel slate (#1E293B) and clean factory white, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warning coral red 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"DEFENSE INDUSTRIAL CRISIS\", no watermarks, 16:9",
        "@CH06_SC017.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow lateral track past the empty missile assembly jigs, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC018", 5.0,
        "In recent naval operations across the Red Sea and the Persian Gulf",
        "Bầu trời đêm Biển Đỏ rực sáng pháo sáng và vệt tên lửa, tàu khu trục Mỹ cơ động đánh chặn bảo vệ luồng hàng hải thương mại qua eo Bab el-Mandeb.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a nighttime naval engagement in the southern Red Sea near the Bab el-Mandeb strait. An American guided-missile destroyer maneuvers at high speed, illuminated by parachute illumination flares and ballistic exhaust trails reflecting off choppy nocturnal waters. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep midnight ocean slate (#0B0F19) and fiery missile exhaust orange (#F59E0B), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC018.png -> Low-angle tracking shot beside the destroyer as its hull cuts through nighttime swells under flare light, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC019", 4.17,
        "American warships have faced a punishing arithmetic of asymmetric attrition.",
        "Biểu đồ toán học tiêu hao bất đối xứng: Cán cân chi phí giữa vũ khí tấn công rẻ tiền và tên lửa phòng thủ đắt đỏ lệch hẳn một bên.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a mathematical cost-exchange balance scale displaying punishing asymmetric attrition. A massive defensive missile cost weight crashes downward against tiny low-cost drone attack tokens, skewing economic parity under analytical warning lights. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark institutional slate (#1E293B) and contrasting crimson and amber weights, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC019.png -> Slow push-in dolly shot toward the skewed balance scale as the cost disparity settles, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC020", 4.58,
        "Hostile non-state actors and regional adversaries deploy low-cost drones and anti",
        "Máy bay không người lái cánh tam giác Shahed-136 giá rẻ bay là là sát mặt biển đêm, động cơ cánh quạt gầm rú tiến về mục tiêu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a delta-wing one-way attack drone (Shahed-136 type) cruising low over dark ocean swells at night, its simple propeller engine buzzing beneath an overcast moonlit sky. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark matte charcoal slate (#1E293B) and silver sea reflections, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC020.png -> Dynamic camera tracking shot flying alongside the low-flying attack drone over the water, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC021", 5.0,
        "ship cruise missiles costing between two thousand and twenty thousand dollars apiece.",
        "Tên lửa hành trình chống hạm phóng từ xe tải cơ động trên bờ biển sa mạc, chi phí sản xuất chỉ vỏn vẹn 2.000 đến 20.000 USD mỗi quả.",
        "DRONES: $2,000 - $20,000", "T2V",
        "A 2D warm cinematic editorial illustration of a mobile coastal missile truck launcher firing a low-cost anti-ship cruise missile from a rugged desert shoreline into the night sky, billows of white rocket smoke illuminating the sandy terrain. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal desert slate (#0F172A) and fiery rocket exhaust crimson (#EF5350), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing coral red 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"DRONES: $2,000 - $20,000\", no watermarks, 16:9",
        "@CH06_SC021.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward tilt following the missile trajectory away from the launcher, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC022", 6.67,
        "To intercept those low-cost threats and protect commercial shipping, American destroyers must fire Standard Missile interceptors",
        "Hầm phóng tên lửa thẳng đứng Mk 41 VLS trên boong tàu khu trục Mỹ khai hỏa, tên lửa Standard Missile phóng vút lên trời đêm để đánh chặn.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a forward Mk 41 Vertical Launching System (VLS) cell popping open on the bow deck of an American guided-missile destroyer, unleashing a high-velocity Standard Missile interceptor into the night sky in a burst of brilliant white fire and smoke. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark naval steel slate (#0B0F19) and blinding rocket plume illumination, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC022.png -> Dynamic low-angle tracking shot capturing the missile roaring upward out of the deck canister, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC023", 6.25,
        "including the SM-2 and SM-6, costing between 1.8 million and 4.3 million dollars per shot.",
        "So sánh giá thành nghẹt thở: Tên lửa SM-2 và SM-6 có giá từ 1.8 đến 4.3 triệu USD mỗi lần bóp cò đánh chặn mục tiêu giá vài nghìn đô-la.",
        "SM-2 / SM-6: $2M - $4.3M", "T2V",
        "A 2D warm cinematic editorial illustration of a high-tech naval defense procurement infographic. Crisp technical cross-section blueprints of the Raytheon SM-2 and SM-6 interceptor missiles display price tags ranging from 1.8 million to 4.3 million dollars per shot under clean analytical lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, sophisticated military slate (#1E293B) and sharp glowing amber missile schematics (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"SM-2 / SM-6: $2M - $4.3M\", no watermarks, 16:9",
        "@CH06_SC023.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow macro pan along the length of the missile schematic, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC024", 4.58,
        "Money is not the primary bottleneck. Time and manufacturing capacity are.",
        "Chiếc đồng hồ cát công nghiệp bằng đồng thau đặt cạnh dây chuyền đúc phôi kim loại nguội lạnh, thời gian và năng lực sản xuất mới là điểm nghẽn thực sự.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a heavy brass industrial hourglass resting on a factory inspection workbench beside precision titanium components. Sand trickles slowly through the glass, visually emphasizing that manufacturing throughput and specialized time cannot be rushed by money alone. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark factory slate (#1E293B) and polished brass reflections, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC024.png -> Slow macro push-in on the falling sand particles inside the industrial hourglass, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC025", 5.0,
        "According to defense research from the Center for Strategic and International Studies",
        "Báo cáo nghiên cứu công nghiệp quốc phòng của Trung tâm Nghiên cứu Chiến lược và Quốc tế (CSIS) tại Washington D.C. mở trên bàn phân tích.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the research library at the Center for Strategic and International Studies (CSIS) in Washington D.C. An open analytical defense report titled 'Empty Bins in a Wartime Environment' lies on a study table under focused brass lamp illumination. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, distinguished research slate (#2A323D) and warm ivory cream parchment (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC025.png -> Slow push-in dolly shot toward the open CSIS defense research report, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC026", 3.75,
        "American defense contractors produce only forty to fifty SM",
        "Xưởng sản xuất tên lửa SM-3 với sản lượng nhỏ giọt: Cả nước Mỹ chỉ xuất xưởng 40 đến 50 quả mỗi năm.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside a specialized missile assembly cleanroom. A sparse row of finished SM-3 interceptor missile bodies rests on padded assembly cradles under bright sterile white lights, highlighting an extremely limited annual production rate. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, clean aerospace slate (#1E293B) and sterile white cleanroom walls, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC026.png -> Slow lateral camera track past the few missile airframes on the assembly line, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC027", 4.58,
        "3 interceptors and twenty to thirty THAAD interceptor rounds per year.",
        "Biểu đồ sản lượng thường niên đáng báo động: Chỉ 40-50 quả SM-3 và 20-30 đạn đánh chặn THAAD được chế tạo mỗi năm.",
        "SM-3: 40-50 / THAAD: 20-30 YR", "T2V",
        "A 2D warm cinematic editorial illustration of a defense industrial output bar chart. Narrow numerical bars indicate the startlingly low annual production quotas: only 40 to 50 SM-3 interceptors and 20 to 30 THAAD rounds manufactured per year across the entire United States defense industry. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern dark slate (#1E293B) and sharp contrasting amber and white data columns, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"SM-3: 40-50 / THAAD: 20-30 YR\", no watermarks, 16:9",
        "@CH06_SC027.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward tilt emphasizing the tiny production figures, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC028", 4.58,
        "A single naval skirmish lasting a few weeks can consume months",
        "Các ống phóng rỗng trên tàu khu trục sau đợt tác chiến kéo dài vài tuần trên Biển Đỏ, khói thuốc súng còn vương trên boong.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the weather-beaten bow of an American guided-missile destroyer returning from intense combat operations. Empty, scorched VLS missile cell hatches stand open, with soot staining the gray steel deck under a pale morning sun. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, scorched naval steel gray (#1E293B) and sea salt encrustations, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC028.png -> Slow downward tracking shot across the row of empty, blackened missile canister hatches, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC029", 5.83,
        "or even years, of specialized domestic weapons production. These interceptors cannot be rapidly mass-produced.",
        "Biểu đồ thời gian cho thấy vài tuần giao tranh tiêu hao sạch số đạn dược sản xuất trong cả năm trời; vũ khí tối tân không thể sản xuất hàng loạt nhanh chóng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an analytical timeline comparison chart showing a brief three-week naval combat spike consuming an entire eighteen months of national weapons production stockpiles under sharp warning lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark institutional slate (#1E293B) and stark crimson depletion curves (#EF5350), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC029.png -> Slow horizontal camera pan along the steep depletion curve on the timeline, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC030", 3.75,
        "They require complex solid-fuel rocket motors, rare earth alloys",
        "Bên trong xưởng đúc động cơ nhiên liệu rắn: Cánh tay robot kiểm tra từng lớp hợp kim đất hiếm và phôi nhiên liệu composite đa tầng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside an advanced solid-fuel rocket motor manufacturing cell. A high-precision robotic arm performs ultrasonic flaw inspection on an intricate carbon-fiber motor casing filled with specialized solid chemical propellant under sterile lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial carbon slate (#1E293B) and high-tech amber laser scan lines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC030.png -> Slow macro push-in on the laser scanning head inspecting the rocket motor surface, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC031", 4.17,
        "and precision microelectronics that depend on fragile global supply chains.",
        "Kính hiển vi phóng đại chip radar dẫn đường sóng milimet phức tạp, kết nối các mắt xích cung ứng mong manh xuyên Thái Bình Dương.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a microelectronics inspection microscope focusing on a complex radar guidance seeker microchip. A delicate global supply chain schematic connects cleanroom fabrication in East Asia to defense integration plants in North America. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, high-tech silicon slate (#1E293B) and glowing golden circuit pathways, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC031.png -> Slow focus pull from the microscopic silicon wafer traces to the global supply chain map on a screen behind, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC032", 6.25,
        "By expending hundreds of multi-million-dollar interceptors to protect commercial shipping corridors in the Middle East",
        "Hàng trăm tên lửa đắt đỏ phóng đi tại Biển Đỏ để che chắn cho tàu chở hàng thương mại quốc tế, rút cạn kho dự trữ phòng thủ.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of multiple surface-to-air missile streaks crisscrossing the night sky above a convoy of commercial container freighters in the Red Sea, illustrating the massive expenditure of sovereign munitions to protect private commercial transit. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal ocean slate (#0B0F19) and brilliant white missile exhaust arcs, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC032.png -> Slow upward tilt following the dual missile exhaust trails climbing into the night sky, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC033", 5.83,
        "the Pentagon is actively draining the sovereign weapons stockpiles intended for the Indo-Pacific theatre.",
        "Kho vũ khí chiến lược tại Guam và Hawaii trống trải dần, đạn dược dự phòng cho mặt trận Ấn Độ Dương - Thái Bình Dương bị tiêu hao.",
        "STOCKPILES DRAINING (INDO-PACIFIC)", "T2V",
        "A 2D warm cinematic editorial illustration inside a massive fortified munitions storage bunker at Naval Base Guam in the Pacific. Long rows of heavy industrial weapons racks sit partially emptied, with logistics clerks in military fatigues noting depleted inventory levels intended for Indo-Pacific deterrence. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, cavernous concrete bunker slate (#1E293B) and warning amber inventory tags, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warning coral red 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"STOCKPILES DRAINING (INDO-PACIFIC)\", no watermarks, 16:9",
        "@CH06_SC033.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow push-in dolly down the aisle of empty weapons racks, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC034", 4.58,
        "Allies in Tokyo and Seoul observe this dynamic with quiet dread.",
        "Bộ Quốc phòng Nhật Bản tại Tokyo (Ichigaya) và Bộ Quốc phòng Hàn Quốc tại Seoul (Yongsan), các tướng lĩnh đồng minh trầm ngâm lo âu trước màn hình kho đạn.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside the Ministry of Defense in Tokyo, Japan. Senior Japanese defense officials stand in quiet contemplation alongside South Korean defense liaison officers, looking upon joint regional missile defense readiness maps under subdued briefing room lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dignified institutional slate (#2A323D) and warm ivory cream stone (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC034.png -> Slow lateral camera track past the solemn faces of allied defense planners, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC035", 3.75,
        "They rely on American missile defense umbrellas for deterrence.",
        "Chiếc ô lá chắn tên lửa Aegis của Hải quân Mỹ bao phủ trên bản đồ Đông Á, đang đối mặt nguy cơ thủng lưới vì thiếu đạn.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a symbolic glowing missile defense dome extending over the maritime approaches of Japan and the Korean Peninsula, anchored by American Aegis destroyers stationed in the East China Sea. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime indigo slate (#0F172A) and glowing azure shield arcs, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC035.png -> Slow push-in dolly shot toward the glowing Aegis defensive dome over the Sea of Japan, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC036", 6.67,
        "But they recognize that America's physical industrial capacity cannot sustain high-intensity operations across two oceans simultaneously.",
        "Thực tế phũ phàng: Năng lực công nghiệp vật lý của Mỹ không thể cáng đáng nổi các cuộc tác chiến cường độ cao cùng lúc trên hai đại dương.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a split-screen geopolitical reality. On one side, American warships expend interceptors in the Red Sea; on the other, vast empty naval drydocks in North American shipyards sit overburdened by repair backlogs under cold overcast skies. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, somber industrial slate (#1E293B) and weathered concrete tones, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC036.png -> Slow continuous zoom out revealing the stark contrast between intense combat consumption and lagging shipyard capacity, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC037", 5.83,
        "Washington can print trillions of digital currency units at the click of a button.",
        "Trụ sở Cục Dự trữ Liên bang Mỹ tại Washington, phím bấm máy tính tạo ra hàng nghìn tỷ đô-la tín dụng số trong chớp mắt.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a financial operator's finger pressing an 'EXECUTE LIQUIDITY' key on an institutional banking keyboard inside the Federal Reserve Eccles Building in Washington D.C. Trillions of digital currency numbers stream effortlessly across multiple glowing monitors. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep digital slate (#1E293B) and glowing currency green figures, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC037.png -> Macro push-in on the mechanical keystroke triggering endless digital currency flows, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC038", 5.0,
        "But it cannot print advanced missile propellant or precision radar guidance chips.",
        "Sự đối lập tàn khốc: Máy in tiền không thể in ra phôi nhiên liệu tên lửa rắn hay chip bán dẫn quét mảng pha chính xác cao.",
        "MONEY CANNOT PRINT MISSILES", "T2V",
        "A 2D warm cinematic editorial illustration presenting a stark physical contradiction. Stacks of printed United States currency sit utterly powerless beside an empty robotic CNC lathe attempting to machine an exotic titanium missile guidance housing. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial steel slate (#1E293B), currency green, and cold machined titanium (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warning coral red 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"MONEY CANNOT PRINT MISSILES\", no watermarks, 16:9",
        "@CH06_SC038.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow pan from the paper currency to the cold unfinished metal part, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC039", 5.0,
        "Seeing this imperial overstretch and the finite limits of American naval deterrence",
        "Phòng tình huống tác chiến của các cường quốc đối thủ, các nhà chiến lược phát hiện điểm yếu dàn mỏng lực lượng của đế chế.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside a non-Western strategic maritime intelligence center. Analysts study global naval tracking feeds showing American carrier strike groups stretched thin across global maritime commitments, identifying a historic strategic window. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep tactical slate (#1E293B) and glowing amber radar vectors, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC039.png -> Slow push-in dolly shot toward the global naval tracking screen over analysts' shoulders, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC040", 2.5,
        "America's adversaries recognized a historic opening.",
        "Góc nhìn cận cảnh đôi mắt sắc bén của nhà hoạch định chiến lược đối thủ nhìn thẳng vào bản đồ luồng hàng hải quốc tế.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a focused geopolitical strategist in a dimly lit command room, sharp observant gaze fixed upon a glowing maritime map of alternate trade routes. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, shadow slate (#0F172A) and amber screen reflections, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC040.png -> Slow macro push-in on the strategist's observant expression reflected in the glass map, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC041", 4.58,
        "They did not attempt to defeat the United States Navy head-on.",
        "Không đối đầu trực diện: Tàu ngầm và tàu tuần tra đối thủ lặng lẽ tránh các cụm tàu sân bay Mỹ trên biển mở.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of naval asymmetry. Instead of confronting an American carrier strike group in open combat, naval vessels of regional adversaries disperse quietly into coastal archipelagos and sovereign territorial waters under sea mist. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep ocean slate (#1E293B) and soft coastal fog, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC041.png -> Slow horizontal camera pan across the misty coastal waters as ships disperse out of view, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH06_SC042", 5.83,
        "Instead, they built an invisible, parallel maritime network designed to bypass the rules entirely.",
        "Sự trỗi dậy của mạng lưới hàng hải song song vô hình: Những con tàu bóng ma tắt định vị AIS lướt đi trong bóng đêm vượt ra ngoài luật chơi quốc tế.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an unflagged shadow crude oil tanker gliding silently through international waters under a moonless night sky, its navigation lights dimmed and AIS tracking transponders switched completely off, initiating an invisible parallel maritime trade network. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal ocean slate (#0B0F19), rusted hull textures, and cold silver moonlight ripples, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH06_SC042.png -> Slow lateral tracking shot following the dark unlit tanker cutting silently through the night sea, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    )
]

# Write chapter_06_visual.md
md_lines = [
    "<!--",
    "DOCUMENT PROVENANCE & EXECUTION LINEAGE:",
    "- Output Document: episodes/the-petrodollar-paradox/chapter_06_visual.md",
    "- Activated Persona: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)",
    "- Activated Skill: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)",
    "- Source Documents Consulted:",
    "  * episodes/the-petrodollar-paradox/chapter_06.md",
    "  * episodes/the-petrodollar-paradox/scene_timing_map.json",
    "  * episodes/the-petrodollar-paradox/visual_storyboard_blueprint.md",
    "- Execution Timestamp: 2026-09-10 13:20",
    "-->",
    "",
    "# Chapter 06 Visual Script — The Malacca Dilemma & Asymmetric Attrition",
    "",
    "Bản kịch bản phân đoạn thị giác 3 tầng giải phẫu cho Chương 6 (The Malacca Dilemma & The Industrial Attrition Trap), đồng bộ toán học 1-1 với 42 phân cảnh trong `scene_timing_map.json`.",
    "",
    "- **Vũ trụ Mỹ thuật:** Geopolitical Noir & Maritime Attrition.",
    "- **Bảng màu Sâu lắng & Sang trọng:** Humid Maritime Grey-Slate (`#334155`, `#1E293B`), Emerald Transit Green (`#26A69A`), Missile Burn Crimson (`#EF5350`), Warm Ivory Cream (`#FAF7EE`), Luminous High-Clarity Editorial Lighting.",
    "- **Độ chuẩn xác Địa danh & Khí tài:** Nêu đích danh địa danh thực tế (Eo biển Malacca, Kênh Phillips phía nam Singapore, Cảng Keppel & Pasir Panjang Singapore, Căn cứ Hải quân Yokosuka Nhật Bản, Căn cứ Hải quân Changi, Biển Đỏ & Eo biển Bab el-Mandeb, Nhà máy tên lửa Tucson Arizona, Căn cứ Hải quân Guam, Bộ Quốc phòng Ichigaya Tokyo, Bộ Quốc phòng Yongsan Seoul) và trang thiết bị khí tài (Soái hạm USS Blue Ridge LCC-19, Tàu khu trục Arleigh Burke, Bệ phóng thẳng đứng Mk 41 VLS, Tên lửa đánh chặn RIM-66 SM-2 & RIM-174 SM-6 & RIM-161 SM-3, Khí tài THAAD, Máy bay không người lái tự sát Shahed-136, Tên lửa hành trình di động ven biển, Động cơ tên lửa nhiên liệu rắn, Chip vi mạch bán dẫn radar mảng pha).",
    "- **Tỷ lệ Typography:** 9/42 cảnh có chữ (21.4%), định vị góc dưới bên trái cách mép đáy 25%.",
    "- **Nhân vật & Quần chúng:** Sĩ quan tác chiến Hạm đội 7, kỹ sư chế tạo tên lửa, tướng lĩnh đồng minh Nhật - Hàn, hoa tiêu tàu dầu quốc tế.",
    "",
    "---",
    "",
    "| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường, Địa Danh & Khí Tài Chuẩn Xác | Text Overlay (Selective Lower-Left 25%) | Luồng Tạo Hình |",
    "| :---: | :---: | :--- | :--- | :---: | :---: |"
]

for s in scenes_data:
    sc_id, dur, spoken, summary, overlay, flow, img, vid = s
    overlay_text = f"`{overlay}`" if overlay else "`Không`"
    md_lines.append(f"| **{sc_id}** | {dur}s | {spoken} | {summary} | {overlay_text} | **{flow}** |")

with open('episodes/the-petrodollar-paradox/chapter_06_visual.md', 'w') as f:
    f.write('\n'.join(md_lines) + '\n')

print("Created chapter_06_visual.md")

# Write prompts_chapter_06.txt
txt_blocks = []
for s in scenes_data:
    sc_id, dur, spoken, summary, overlay, flow, img, vid = s
    block = f"{sc_id} [IMAGE]: {img}\n{sc_id} [VIDEO]: {vid}"
    txt_blocks.append(block)

with open('episodes/the-petrodollar-paradox/prompts_chapter_06.txt', 'w') as f:
    f.write('\n\n'.join(txt_blocks) + '\n')

print("Created prompts_chapter_06.txt")
