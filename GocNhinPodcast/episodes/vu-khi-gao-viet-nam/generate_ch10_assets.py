import json

scenes_data = [
    {
        "id": "CH10_SC001",
        "dur": "5.25s",
        "words": 20,
        "text": "Bây giờ, hãy quay trở lại với buổi trưa bình dị tại một quán ăn ven đường ở Việt Nam.",
        "anatomy": {
            "tier1": "Không gian hiên quán ăn bình dân ven đường tại TP.HCM hoặc Hà Nội trong buổi trưa rực rỡ nắng ấm.",
            "tier2": "Bàn ghế inox sáng bóng phản chiếu ánh nắng, quạt trần quay đều, không khí tấp nập, thân thuộc và ấm cúng.",
            "tier3": "Cú máy trượt ngang từ hè phố nhộn nhịp vào bên trong quán ăn bình dân (Horizontal tracking shot from sunny sidewalk into modest diner)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a charming sunlit Vietnamese roadside street eatery with gleaming stainless steel tables, wooden stools, and gentle overhead fans under warm midday sunlight",
        "setting": "a lively sidewalk lunch diner in an everyday Vietnamese city neighborhood in warm golden sunlight",
        "motion": "Slow horizontal tracking shot gliding from the sunny bustling street into the welcoming diner"
    },
    {
        "id": "CH10_SC002",
        "dur": "5.78s",
        "words": 22,
        "text": "Trước mặt bạn vẫn là một bát cơm trắng dẻo thơm, bốc khói nghi ngút bên cạnh đĩa thức ăn quen thuộc.",
        "anatomy": {
            "tier1": "Mặt bàn inox phản chiếu ánh nắng vàng ấm áp của quán ăn trưa.",
            "tier2": "Bát cơm trắng đầy đặn, từng hạt cơm dẻo thơm bóng bẩy, hơi nước bốc lên nghi ngút bên cạnh đĩa thức ăn dân dã quen thuộc.",
            "tier3": "Cú máy đẩy chậm cận cảnh vào bát cơm trắng bốc khói dẻo thơm (Slow push-in close-up toward steaming bowl of fragrant white rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an evocative close-up of a generous glazed ceramic bowl of steaming hot fragrant white rice with glistening plump grains resting beside a traditional home-style savory lunch plate",
        "setting": "a clean stainless steel table in a warm roadside diner filled with golden midday rays",
        "motion": "Slow push-in shot centering on the delicate steam rising from the hot bowl of fragrant rice"
    },
    {
        "id": "CH10_SC003",
        "dur": "3.15s",
        "words": 12,
        "text": "Giá của bữa ăn ấy vẫn là ba mươi lăm nghìn đồng.",
        "anatomy": {
            "tier1": "Góc bàn ăn với chiếc ví da giản dị và tờ tiền polyme thanh toán bữa trưa.",
            "tier2": "Hóa đơn giấy mộc mạc ghi mức giá 35.000 đồng cho một bữa ăn trưa no nê, dinh dưỡng.",
            "tier3": "Cú máy tĩnh trực diện vào con số 35.000 VND (Steady shot on 35,000 VND meal price tag) cùng text overlay góc trái dưới."
        },
        "overlay": "STAPLE MEAL: 35,000 VND",
        "ref": None,
        "subj": "a modest paper receipt and bank note resting beside a ceramic bowl of rice indicating the remarkably accessible price of thirty-five thousand Vietnamese Dong",
        "setting": "a cozy street dining table in warm ambient daylight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the meal receipt"
    },
    {
        "id": "CH10_SC004",
        "dur": "6.83s",
        "words": 26,
        "text": "Hàng chục triệu người lao động mỗi ngày vẫn bước vào quán ăn, trả tiền, rồi vội vã quay trở lại với guồng quay công việc.",
        "anatomy": {
            "tier1": "Quang cảnh toàn khu phố ẩm thực bình dân nhộn nhịp vào giờ nghỉ trưa dưới hàng cây xanh mát.",
            "tier2": "Công nhân, nhân viên văn phòng, tài xế công nghệ và tiểu thương bước vào ăn trưa no ấm rồi hối hả trở lại nhịp sống sản xuất.",
            "tier3": "Cú máy trượt ngang bao quát nhịp sống giờ trưa nhộn nhịp của người lao động (Wide tracking shot past busy lunch crowds returning to work)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a vibrant mid-day street scene showing diverse Vietnamese working people—office staff, factory technicians, and delivery drivers—enjoying lunchtime meals and stepping briskly back into daily work",
        "setting": "a lively tree-lined dining alley in a bustling Vietnamese metropolis under warm sun",
        "motion": "Slow horizontal tracking shot following the flow of workers finishing lunch and resuming their duties"
    },
    {
        "id": "CH10_SC005",
        "dur": "6.56s",
        "words": 25,
        "text": "Với hầu hết chúng ta, sự rẻ mạt và sẵn có của bữa ăn trưa là một điều hiển nhiên như không khí để thở.",
        "anatomy": {
            "tier1": "Một quán cơm bình dân ngập tràn tiếng cười nói thân mật, ánh nắng xuyên qua kẽ lá rọi xuống hiên nhà.",
            "tier2": "Những nụ cười thư thái của người lao động bên mâm cơm trưa no ấm, cảm nhận sự đủ đầy như một phần tự nhiên của cuộc sống.",
            "tier3": "Cú máy lùi chậm từ nụ cười của người lao động ra toàn cảnh quán ăn (Slow pull-back shot revealing relaxed dining atmosphere)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a heartwarming cinematic view of hardworking people dining peacefully together in a sunlit urban food stall, embodying the effortless natural abundance of daily staple food",
        "setting": "a breezy open-air diner porch shaded by tropical canopy in warm afternoon daylight",
        "motion": "Slow pull-back camera motion framing the relaxed, peaceful lunch atmosphere"
    },
    {
        "id": "CH10_SC006",
        "dur": "7.61s",
        "words": 29,
        "text": "Thế nhưng, sau tất cả những gì chúng ta vừa cùng nhau đi qua, hy vọng bạn đã nhìn bát cơm ấy bằng một đôi mắt hoàn toàn khác.",
        "anatomy": {
            "tier1": "Không gian tĩnh lặng, ánh sáng vàng ấm áp bao trùm mặt bàn ăn với bát cơm trắng ở vị trí trung tâm.",
            "tier2": "Bát cơm trắng bắt đầu tỏa ra ánh hào quang vàng hổ phách nhẹ nhàng, như một viên ngọc quý chứa đựng vận mệnh sinh tồn của cả một dân tộc.",
            "tier3": "Cú máy đẩy chậm và nâng nhẹ góc nhìn, biến bát cơm bình dị thành tâm điểm đầy chiều sâu tư duy (Slow push-in and slight elevation on glowing rice bowl)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a striking visual elevation where the humble ceramic bowl of white rice is subtly bathed in an ethereal warm golden amber glow, symbolizing deep geoeconomic meaning",
        "setting": "a serene, beautifully lit dining tabletop in warm ivory cream and golden ambient tones",
        "motion": "Slow subtle push-in shot elevating the visual stature of the humble rice bowl"
    },
    {
        "id": "CH10_SC007",
        "dur": "4.99s",
        "words": 19,
        "text": "Đó không đơn thuần là vài lạng tinh bột giá vài nghìn đồng trên một hóa đơn thanh toán.",
        "anatomy": {
            "tier1": "Bàn làm việc phân tích kinh tế vĩ mô với các tập báo cáo chỉ số giá cả và hóa đơn sinh hoạt.",
            "tier2": "Hình ảnh hóa đơn thanh toán vài nghìn đồng tiền gạo được đặt cạnh mô hình cân bằng kinh tế vĩ mô quốc gia.",
            "tier3": "Cú máy trượt ngang qua hóa đơn thanh toán sang biểu đồ kinh tế (Horizontal tracking shot past receipt to macroeconomic charts)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an analytical comparison on a research desk contrasting a trivial retail lunch invoice with a grand national economic balance sheet",
        "setting": "a modern economic research studio under warm focused desk illumination",
        "motion": "Slow horizontal tracking shot past the humble receipt toward the macroeconomic ledgers"
    },
    {
        "id": "CH10_SC008",
        "dur": "5.51s",
        "words": 21,
        "text": "Đó là chiếc mỏ neo giữ cho chỉ số giá tiêu dùng không bùng phát thành những cơn bão lạm phát.",
        "anatomy": {
            "tier1": "Biểu đồ đường chỉ số giá tiêu dùng (CPI) quốc gia hiển thị trên màn hình dữ liệu kinh tế vĩ mô.",
            "tier2": "Hình ảnh biểu tượng chiếc mỏ neo vàng óng giữ chặt lấy đường cong CPI, ngăn không cho làn sóng lạm phát bùng nổ.",
            "tier3": "Cú máy tĩnh trực diện vào con số mỏ neo CPI ổn định lạm phát (Steady shot on Consumer Price Index macroeconomic anchor) cùng text overlay góc trái dưới."
        },
        "overlay": "MACROECONOMIC CPI ANCHOR",
        "ref": None,
        "subj": "a polished golden brass maritime anchor resting securely across a fluctuating Consumer Price Index graph, visually holding national inflation tightly in check",
        "setting": "a national economic data observation chamber under warm amber console lighting",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the symbolic anchor"
    },
    {
        "id": "CH10_SC009",
        "dur": "5.51s",
        "words": 21,
        "text": "Đó là chiếc lò xo giảm xốc vĩ mô âm thầm bảo vệ sức mua của từng đồng lương còi cọc.",
        "anatomy": {
            "tier1": "Mặt bàn kính làm việc với mô hình chiếc lò xo cơ khí bằng kim loại mạ đồng sáng bóng.",
            "tier2": "Chiếc lò xo chịu lực nén hấp thụ toàn bộ các chấn động tăng giá quốc tế, bảo vệ giỏ hàng sinh hoạt của người lao động.",
            "tier3": "Cú máy tĩnh trực diện vào chiếc lò xo giảm xốc vĩ mô (Steady shot on macroeconomic shock absorber mechanism) cùng text overlay góc trái dưới."
        },
        "overlay": "INFLATION SHOCK ABSORBER",
        "ref": None,
        "subj": "an industrial brass suspension shock spring smoothly absorbing turbulent downward price shockwaves, shielding a household grocery basket below",
        "setting": "a high-precision economic analysis laboratory in warm ambient illumination",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the shock absorber spring"
    },
    {
        "id": "CH10_SC010",
        "dur": "5.25s",
        "words": 20,
        "text": "Không có bát cơm ấy, chi phí sinh hoạt sẽ tăng vọt và tiền lương công nhân sẽ bốc hơi.",
        "anatomy": {
            "tier1": "Quang cảnh một khu xóm trọ công nhân gần khu công nghiệp trong ánh hoàng hôn vàng cam.",
            "tier2": "Hình ảnh người công nhân nhìn vào bảng chi tiêu gia đình, nơi tiền lương ít ỏi có nguy cơ bị bào mòn nếu lương thực tăng phi mã.",
            "tier3": "Cú máy đẩy chậm vào người công nhân cầm phong bì lương bên bàn ăn (Slow push-in on worker holding pay slip beside family table)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an authentic residential street in an industrial worker community at dusk where an Asian factory worker examines a modest wage envelope beside a small grocery bag",
        "setting": "a clean, peaceful industrial residential enclave under warm sunset glow",
        "motion": "Slow push-in camera shot toward the worker's family dining space"
    },
    {
        "id": "CH10_SC011",
        "dur": "3.94s",
        "words": 15,
        "text": "Chiếc bẫy rỗng ruột của các nước láng giềng sẽ ập đến ngay lập tức.",
        "anatomy": {
            "tier1": "Hình ảnh ký ức gợi nhớ về cuộc khủng hoảng giá gạo tại Manila với các dãy kệ siêu thị trống rỗng.",
            "tier2": "Bóng đen của chiếc bẫy phụ thuộc lương thực đe dọa các nền kinh tế lơ là nền tảng nông nghiệp.",
            "tier3": "Cú máy trượt ngang cảnh báo bài học từ các nước láng giềng (Horizontal tracking shot past empty market stalls). "
        },
        "overlay": None,
        "ref": None,
        "subj": "an evocative reminder of regional vulnerability: empty grain shelves in a foreign supermarket contrasting with the abundance of domestic grain stores",
        "setting": "a dim trading warehouse transitioning into warm daylight",
        "motion": "Slow horizontal tracking shot past the cautionary foreign market shelves"
    },
    {
        "id": "CH10_SC012",
        "dur": "4.20s",
        "words": 16,
        "text": "Chúng ta đang sống trong một thời đại mà thế giới say sưa nói về trí tuệ nhân tạo, về chip bán dẫn",
        "anatomy": {
            "tier1": "Phòng fab bán dẫn công nghệ cao với ánh sáng vàng ấm và các bảng mạch vi xử lý AI phát sáng tinh thể.",
            "tier2": "Kỹ sư và robot tự động hóa lắp ráp các cụm máy chủ trí tuệ nhân tạo và wafer bán dẫn hiện đại.",
            "tier3": "Cú máy lướt nhanh qua dàn máy chủ vi xử lý AI (Dynamic tracking glide past glowing AI semiconductor servers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a state-of-the-art semiconductor lithography fab and glowing artificial intelligence server racks reflecting amber cleanroom safelight",
        "setting": "a cutting-edge tech innovation facility under warm ambient cleanroom lighting",
        "motion": "Smooth horizontal camera glide past the gleaming semiconductor processors"
    },
    {
        "id": "CH10_SC013",
        "dur": "3.94s",
        "words": 15,
        "text": "và những tòa tháp tài chính chọc trời.",
        "anatomy": {
            "tier1": "Góc nhìn từ mặt đất ngước lên các tòa tháp tài chính cao vút bọc kính tráng lệ dưới bầu trời hoàng hôn vàng cam.",
            "tier2": "Các tòa tháp biểu trưng cho sự thịnh vượng công nghệ cao và dòng vốn tài chính toàn cầu.",
            "tier3": "Cú máy ngước lên (low-angle tilt-up) lướt theo chiều cao của các tòa nhà chọc trời (Low-angle upward tilt along soaring financial skyscrapers)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a dramatic upward-looking street view of gleaming glass and steel financial towers soaring into a glorious warm golden sunset sky",
        "setting": "a prestigious modern metropolitan financial district bathed in amber twilight",
        "motion": "Low-angle smooth upward tilt tracking along the soaring skyscraper facades"
    },
    {
        "id": "CH10_SC014",
        "dur": "3.94s",
        "words": 15,
        "text": "Người ta dễ dàng tôn sùng những thứ lấp lánh ở đỉnh tháp công nghệ,",
        "anatomy": {
            "tier1": "Đại sảnh triển lãm công nghệ tương lai với các mô hình hologram phát sáng và máy tính lượng tử.",
            "tier2": "Khách tham quan say mê chiêm ngưỡng những công nghệ đột phá tại đỉnh tháp văn minh.",
            "tier3": "Cú máy trượt ngang qua các gian trưng bày công nghệ hào nhoáng (Horizontal tracking shot past futuristic tech pavilions)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a grand international tech expo hall where visitors admire glowing quantum computing holographic displays on polished podiums",
        "setting": "a sleek modern exhibition center under warm ambient spotlighting",
        "motion": "Slow horizontal tracking shot past the dazzling technological exhibits"
    },
    {
        "id": "CH10_SC015",
        "dur": "4.46s",
        "words": 17,
        "text": "mà quên mất rằng nền tảng sinh tồn của nhân loại vẫn nằm ở đáy tháp Maslow.",
        "anatomy": {
            "tier1": "Mô hình kim tự tháp nhu cầu Maslow bằng đồng và thủy tinh trong suốt đặt trên bàn phân tích triết học xã hội.",
            "tier2": "Tầng đáy sinh tồn cơ bản (Lương thực & Nước sạch) rực sáng sắc vàng hổ phách làm bệ đỡ vững chắc cho toàn bộ đỉnh tháp bên trên.",
            "tier3": "Cú máy tĩnh trực diện vào tầng đáy sinh tồn tháp Maslow (Steady shot on Maslow's base survival tier) cùng text overlay góc trái dưới."
        },
        "overlay": "MASLOW'S BASE: SURVIVAL FOUNDATION",
        "ref": None,
        "subj": "an architectural 3D model of Maslow's Hierarchy of Needs pyramid where the broad foundational base layer representing Food and Water glows brightly in solid amber gold, supporting the delicate tiers above",
        "setting": "a scholarly philosophical library desk under warm natural daylight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the glowing pyramid base"
    },
    {
        "id": "CH10_SC016",
        "dur": "7.35s",
        "words": 28,
        "text": "Một quốc gia có thể sở hữu những siêu máy tính mạnh nhất, nhưng một lập trình viên không thể ăn các dòng mã để sống qua ngày.",
        "anatomy": {
            "tier1": "Góc làm việc hiện đại của một lập trình viên với ba màn hình máy tính hiển thị các dòng mã code thuật toán phức tạp.",
            "tier2": "Bên cạnh bàn phím cơ là bát cơm trắng dẻo thơm đang bốc khói, khắc họa chân lý: Trí tuệ máy móc không thể thay thế năng lượng của hạt gạo.",
            "tier3": "Cú máy đẩy chậm từ màn hình hiển thị code sang bát cơm thơm trên bàn làm việc (Slow push-in from code screens to steaming rice bowl)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a thoughtful juxtaposition on a modern software engineer's oak desk: glowing multi-monitor displays filled with complex software code sitting beside a hot ceramic bowl of steaming white rice and chopsticks",
        "setting": "a creative technology studio in warm cozy ambient light",
        "motion": "Slow push-in camera shot panning gently from the glowing code lines to the warm bowl of rice"
    },
    {
        "id": "CH10_SC017",
        "dur": "3.41s",
        "words": 13,
        "text": "Một dân tộc có thể chế tạo đầu đạn hạt nhân,",
        "anatomy": {
            "tier1": "Khu liên hợp quốc phòng kiên cố với các bệ phóng khí tài quân sự sừng sững dưới bầu trời chiều.",
            "tier2": "Hình ảnh vũ khí tối tân đại diện cho sức mạnh răn đe quân sự nhưng hoàn toàn bất lực trước nhu cầu dinh dưỡng sinh học.",
            "tier3": "Cú máy góc rộng trượt ngang qua hàng khí tài quân sự (Wide cinematic tracking shot past defense installations)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an imposing fortified military facility with silhouetted strategic hardware standing beneath an amber and copper twilight sky",
        "setting": "a high-security defense compound in solemn late afternoon light",
        "motion": "Wide cinematic tracking shot gliding past the heavy defense perimeter"
    },
    {
        "id": "CH10_SC018",
        "dur": "5.51s",
        "words": 21,
        "text": "nhưng không một loại vũ khí nào có thể xua đi nỗi sợ hãi khi những kệ hàng lương thực bị vét rỗng.",
        "anatomy": {
            "tier1": "Bên trong một siêu thị lớn với những kệ hàng ngũ cốc trống trơn trong thời kỳ khủng hoảng.",
            "tier2": "Ánh mắt lo âu của người dân khi đối diện với sự gián đoạn nguồn cung lương thực thiết yếu.",
            "tier3": "Cú máy trượt ngang chậm qua dãy kệ hàng lương thực trống rỗng (Slow horizontal tracking shot past barren food shelves)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a stark perspective along empty supermarket aisles where barren wire shelves emphasize the visceral anxiety of food shortages",
        "setting": "a quiet grocery store interior in warm soft lighting",
        "motion": "Slow horizontal tracking shot emphasizing the empty food shelves"
    },
    {
        "id": "CH10_SC019",
        "dur": "3.94s",
        "words": 15,
        "text": "Sức mạnh thực sự của một dân tộc không nằm ở những điều hoa mỹ.",
        "anatomy": {
            "tier1": "Quang cảnh làng quê sông nước êm đềm của đồng bằng sông Cửu Long lúc bình minh.",
            "tier2": "Mặt nước sông lấp lánh ánh vàng, rặng dừa nước nghiêng mình, vẻ đẹp mộc mạc không hoa mỹ nhưng tiềm ẩn sức sống phi thường.",
            "tier3": "Cú máy lướt chậm trên mặt nước sông Tiền sông Hậu (Slow glide across tranquil river surface at sunrise)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a peaceful, unpretentious sunrise over the wide waters of the Mekong river with water palms and wooden boats silhouetted against pure morning gold",
        "setting": "the timeless riverways of the Mekong Delta in tranquil morning light",
        "motion": "Slow lyrical glide across the calm golden river waters"
    },
    {
        "id": "CH10_SC020",
        "dur": "5.78s",
        "words": 22,
        "text": "Nó nằm ở năng lực bảo đảm chén cơm no ấm cho nhân dân mình trong mọi hoàn cảnh ngặt nghèo nhất.",
        "anatomy": {
            "tier1": "Gian bếp gia đình nông thôn Việt Nam rực sáng ánh lửa rơm ấm cúng.",
            "tier2": "Người mẹ múc từng muôi cơm trắng nóng hổi cho cả gia đình, nụ cười hạnh phúc của trẻ thơ và người già trong sự no ấm vững bền.",
            "tier3": "Cú máy đẩy chậm vào nồi cơm gang thơm lừng tỏa khói (Slow push-in toward steaming traditional cast-iron rice pot)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a heartwarming scene in a rural Vietnamese kitchen where a caring mother serves fluffy white rice from a steaming cast-iron pot to smiling family members",
        "setting": "a traditional rural home filled with the warm amber glow of a cooking hearth",
        "motion": "Slow push-in camera shot centering on the comforting steaming pot of rice"
    },
    {
        "id": "CH10_SC021",
        "dur": "2.89s",
        "words": 11,
        "text": "Đằng sau bát cơm ba mươi lăm nghìn đồng ấy,",
        "anatomy": {
            "tier1": "Bát cơm trắng 35K đặt trang trọng trên mặt bàn gỗ mộc.",
            "tier2": "Hạt cơm trắng ngần phản chiếu ánh sáng ban mai, mở ra cánh cửa dẫn vào cội nguồn sức lao động của người nông dân.",
            "tier3": "Cú máy cận cảnh cực đại (extreme close-up) vào từng hạt cơm trắng ngần (Extreme close-up on glistening cooked rice grains)."
        },
        "overlay": None,
        "ref": None,
        "subj": "an extreme macro close-up of a porcelain bowl filled with plump, perfectly steamed grains of white rice, catching the warm morning light",
        "setting": "a rustic wooden dining table in bright morning sunlight",
        "motion": "Slow macro glide over the glistening texture of the steaming rice grains"
    },
    {
        "id": "CH10_SC022",
        "dur": "5.25s",
        "words": 20,
        "text": "là giọt mồ hôi ba vụ một năm của hàng triệu nông dân chân lấm tay bùn nơi hạ nguồn Mekong.",
        "anatomy": {
            "tier1": "Cánh đồng mẫu lớn ngút ngàn của đồng bằng sông Cửu Long trong mùa thu hoạch vàng rực rỡ.",
            "tier2": "Những người nông dân kiên cường mồ hôi ướt đẫm lưng áo, nụ cười rạng rỡ bên máy gặt đập liên hợp đang gặt những luống lúa trĩu hạt.",
            "tier3": "Cú máy bay góc cao lướt qua đoàn máy gặt trên cánh đồng vàng rực (High-angle aerial sweep over harvesters on golden paddies)."
        },
        "overlay": None,
        "ref": None,
        "subj": "Vietnamese farmers in conical hats and sturdy field clothes smiling warmly beside modern combine harvesters working across boundless golden rice fields in the Mekong Delta",
        "setting": "the vast productive rice bowl of Southern Vietnam under radiant sunshine",
        "motion": "Smooth high-angle aerial sweep showcasing the expansive golden harvest"
    },
    {
        "id": "CH10_SC023",
        "dur": "7.09s",
        "words": 27,
        "text": "Đó là cuộc chiến kiên cường giành giật từng giọt nước ngọt trước mười một con đập thượng nguồn và ranh mặn chín mươi lăm cây số.",
        "anatomy": {
            "tier1": "Bản đồ thủy văn sông Mekong hiển thị chuỗi 11 đập thủy điện thượng nguồn và ranh giới mặn 95km đang xâm nhập.",
            "tier2": "Hệ thống kênh mương thủy lợi nội đồng của miền Tây kiên cường điều tiết dòng nước ngọt quý giá cứu sống ruộng đồng.",
            "tier3": "Cú máy tĩnh trực diện vào con số 11 đập và ranh mặn 95km (Steady shot on 11 upstream dams and 95km salinity barrier) cùng text overlay góc trái dưới."
        },
        "overlay": "11 DAMS & 95 KM SALINITY FRONTIER",
        "ref": None,
        "subj": "a dramatic hydrological map of the Mekong River basin showing the 11 upstream mega-dams and the critical 95-kilometer inland salinity intrusion frontier held back by coastal sluice systems",
        "setting": "a water resources GIS command observatory under warm amber displays",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the hydrological defense map"
    },
    {
        "id": "CH10_SC024",
        "dur": "4.73s",
        "words": 18,
        "text": "Đó là bản lĩnh của những cống ngăn mặn khổng lồ và các đại đối sách thuận thiên.",
        "anatomy": {
            "tier1": "Đại công trình Siêu cống Cái Lớn - Cái Bé sừng sững giữa dòng sông lớn dưới ánh bình minh rực rỡ.",
            "tier2": "Các cửa van thép khổng lồ đóng mở nhịp nhàng điều tiết nguồn nước ngọt - mặn theo triết lý Nghị quyết 120 thuận thiên.",
            "tier3": "Cú máy góc rộng từ trên cao bao quát toàn cảnh siêu cống Cái Lớn (Wide aerial shot of Cái Lớn - Cái Bé mega sluice gates) cùng text overlay góc trái dưới."
        },
        "overlay": "MEGA SLUICE GATES & RESOLUTION 120",
        "ref": "cong_cai_lon.jpg",
        "subj": "the monumental engineering architecture of the Cai Lon - Cai Be mega water control sluice gates depicted in the reference image, with massive steel radial gates spanning the wide river under a golden morning sky",
        "setting": "the vast estuarine waters of Kien Giang in bright warm morning sunlight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the monumental sluice gates"
    },
    {
        "id": "CH10_SC025",
        "dur": "4.73s",
        "words": 18,
        "text": "Đó là những nhà khoa học mang dép rọ lội bùn chia sẻ sự sống cho nhân loại.",
        "anatomy": {
            "tier1": "Ruộng lúa thí nghiệm với bùn đất phù sa màu mỡ dưới ánh nắng ban mai ấm áp.",
            "tier2": "Hình ảnh nhà khoa học nông nghiệp Việt Nam mang đôi dép rọ cao su giản dị, lội bùn nâng niu từng nhánh lúa giống chuyển giao cho bạn bè quốc tế.",
            "tier3": "Cú máy đẩy chậm tôn vinh hình ảnh nhà khoa học nông nghiệp lội bùn (Slow push-in honoring barefoot agronomy scientists). "
        },
        "overlay": None,
        "ref": "gs_vo_tong_xuan.jpg",
        "subj": "a revered senior Vietnamese agronomist with warm gentle smile wearing field clothes and iconic rubber strap sandals, stepping barefoot into fertile paddy mud to examine experimental rice panicles",
        "setting": "an experimental research paddy in the Mekong Delta under bright morning light",
        "motion": "Slow respectful push-in camera shot framing the dedicated agricultural scientist"
    },
    {
        "id": "CH10_SC026",
        "dur": "3.68s",
        "words": 14,
        "text": "Hạt gạo Việt Nam đã nuôi dưỡng vững chắc một trăm triệu đồng bào.",
        "anatomy": {
            "tier1": "Toàn cảnh đất nước Việt Nam nhìn từ không gian hoặc bản đồ địa hình ba miền trù phú ngập tràn ánh nắng ấm.",
            "tier2": "Những cánh đồng lúa nối dài từ đồng bằng Bắc Bộ đến vựa lúa Cửu Long, nuôi dưỡng vững chắc 100 triệu người dân Việt Nam.",
            "tier3": "Cú máy tĩnh trực diện vào con số nuôi dưỡng 100 triệu đồng bào (Steady shot on feeding 100 million citizens) cùng text overlay góc trái dưới."
        },
        "overlay": "FEEDING 100 MILLION CITIZENS",
        "ref": None,
        "subj": "a glorious sunlit panoramic landscape connecting the green terraced paddies of the north, the coastal plains, and the sprawling Mekong delta, symbolizing complete food self-sufficiency for 100 million people",
        "setting": "a majestic national landscape under radiant golden daylight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the national agricultural panorama"
    },
    {
        "id": "CH10_SC027",
        "dur": "6.83s",
        "words": 26,
        "text": "Hơn thế nữa, nó trở thành chiếc van an ninh sinh tồn của cả khu vực và là sứ giả hòa bình trên trường quốc tế.",
        "anatomy": {
            "tier1": "Quả địa cầu và bản đồ hải trình quốc tế tỏa sáng rực rỡ từ Việt Nam vươn ra khắp các đại dương.",
            "tier2": "Những chuyến tàu chở gạo mang lá cờ Việt Nam cập cảng Philippines, Indonesia, Cuba, châu Phi... mang lại sự no ấm và hòa bình.",
            "tier3": "Cú máy bay lùi bao quát mạng lưới hòa bình và an ninh lương thực toàn cầu (Slow aerial pull-back over global peace and food security network) cùng text overlay góc trái dưới."
        },
        "overlay": "REGIONAL PEACE & SECURITY VALVE",
        "ref": None,
        "subj": "an illuminated geopolitical globe showing luminous golden maritime trade arcs radiating outward from Vietnam across Asia, Africa, and the Caribbean, carrying rice as an ambassador of peace",
        "setting": "a grand international strategy rotunda under warm amber gallery downlights",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the global maritime food routes"
    },
    {
        "id": "CH10_SC028",
        "dur": "7.35s",
        "words": 28,
        "text": "Vũ khí tối thượng của chúng ta chưa bao giờ nằm trong những hầm ngầm bê tông cốt thép hay những kho khí tài quân sự tối tân.",
        "anatomy": {
            "tier1": "Khu công sự bê tông cốt thép kiên cố và kho khí tài quân sự ngập trong ánh hoàng hôn sâu lắng.",
            "tier2": "Hình ảnh chuyển dịch góc nhìn: Vũ khí đích thực bảo vệ một dân tộc không phải là súng đạn hay hầm ngầm bê tông.",
            "tier3": "Cú máy trượt ngang từ công trình bê tông lạnh sang cánh đồng lúa ấm áp (Horizontal pan from cold concrete bunker toward sunlit living fields)."
        },
        "overlay": None,
        "ref": None,
        "subj": "a solemn visual transition from a cold reinforced concrete bunker and defensive steel redoubt smoothly transitioning into warm, living golden farmland",
        "setting": "a twilight landscape transitioning from concrete fortifications to warm agrarian earth",
        "motion": "Slow horizontal tracking shot transitioning from concrete redoubts toward fertile green paddies"
    },
    {
        "id": "CH10_SC029",
        "dur": "7.88s",
        "words": 30,
        "text": "Nó đang hiện diện ngay trên bàn ăn của mỗi gia đình, bình dị, khiêm nhường nhưng nắm giữ quyền lực định đoạt sự sống còn của cả dân tộc.",
        "anatomy": {
            "tier1": "Bàn ăn gia đình ấm cúng của một mái ấm Việt Nam dưới ánh đèn vàng êm dịu.",
            "tier2": "Mọi thế hệ quây quần bên bát cơm trắng dẻo thơm, mộc mạc khiêm nhường nhưng là biểu tượng của chủ quyền và sinh mệnh dân tộc.",
            "tier3": "Cú máy tĩnh trực diện vào mâm cơm gia đình và thông điệp quyền lực sinh tồn (Steady shot on sovereign family dining table) cùng text overlay góc trái dưới."
        },
        "overlay": "SOVEREIGNTY ON THE DINING TABLE",
        "ref": None,
        "subj": "a multi-generational Vietnamese family—grandparents, parents, and children—seated harmoniously around an evening dining table, sharing steaming bowls of rice in warm golden lamplight",
        "setting": "a loving, peaceful Vietnamese family dining room filled with warm cozy ambient tones",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the multi-generational family dinner"
    },
    {
        "id": "CH10_SC030",
        "dur": "4.73s",
        "words": 18,
        "text": "Lần tới, khi bạn cầm trên tay một bát cơm dẻo thơm, bạn sẽ nhìn thấy điều gì?",
        "anatomy": {
            "tier1": "Bàn ăn mộc mạc bên khung cửa sổ ngập tràn ánh nắng ban mai trong trẻo.",
            "tier2": "Đôi bàn tay nâng niu bát cơm sứ trắng tỏa khói thơm lừng, ánh mắt chiêm nghiệm nhìn sâu vào từng hạt ngọc thực.",
            "tier3": "Cú máy đẩy chậm cận cảnh vào đôi bàn tay đang nâng bát cơm thơm (Slow push-in on hands holding the steaming bowl of rice)."
        },
        "overlay": None,
        "ref": None,
        "subj": "two gentle hands tenderly lifting a steaming ceramic bowl of pure white rice into the soft warm morning light beside an open window",
        "setting": "a peaceful dining room by an open window overlooking green garden foliage in morning sun",
        "motion": "Slow push-in shot centering on the hands lifting the steaming bowl of white rice"
    },
    {
        "id": "CH10_SC031",
        "dur": "6.3s",
        "words": 24,
        "text": "Chỉ là một bữa ăn trưa bình thường, hay là sự tự tôn và độc lập vững chắc của một đất nước kiên cường?",
        "anatomy": {
            "tier1": "Khung cảnh cánh đồng lúa bạt ngàn của đất nước Việt Nam hòa quyện với chân trời rạng đông rực rỡ sắc vàng kim.",
            "tier2": "Bát cơm trắng tỏa khói vàng ấm áp hòa vào toàn cảnh giang sơn gấm vóc, khẳng định bản lĩnh tự tôn và độc lập vững bền của dân tộc.",
            "tier3": "Cú máy lùi xa và nâng cao (grand ascending crane shot) bao quát non sông gấm vóc (Grand ascending crane shot over radiant national homeland) cùng text overlay góc trái dưới kết bài."
        },
        "overlay": "FOOD INDEPENDENCE & NATIONAL SOVEREIGNTY",
        "ref": None,
        "subj": "a breathtaking, majestic cinematic panorama of boundless golden and emerald rice plains stretching toward the glowing sunrise horizon, embodying the resilient pride and unshakeable sovereignty of Vietnam",
        "setting": "the vast glorious delta landscape of Vietnam bathed in magnificent golden sunrise rays",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the majestic sunrise rice plains"
    }
]

print(f"Total scenes for Chapter 10: {len(scenes_data)}")

# 1. Generate chapter_10_visual.md
md_lines = [
    "# chapter_10_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: Vũ Khí Lúa Gạo Việt Nam (`episodes/vu-khi-gao-viet-nam`)",
    "## Chương 10: Sức Mạnh Định Đoạt Bàn Cờ Và Bát Cơm Tương Lai (Grand Finale)",
    "## Phong cách chủ đạo: Luminous Warm Editorial Illustration (Minh họa báo chí cao cấp, ánh sáng trong trẻo rực rỡ, 100% không gian vật lý đời thực, triệt tiêu hoàn toàn siêu thực và màu đen u ám)",
    "",
    "### 🎨 Hệ màu 60-30-10 (Tuyệt Đối Ấm Áp — Chống Lạnh Lẽo):",
    "- **60% Tông màu nền chủ đạo:** Warm Ivory Cream (`#FAF7EE`), Warm Golden Daylight (`#FFFBEB`), Luminous Sunlight Haze (`#F3E5AB`). Tuyệt đối không dùng nền xám lạnh, xanh cyan buốt giá hay đen kịt.",
    "- **30% Đường nét & Chủ thể:** Ripe Golden Amber (`#F59E0B`), Terracotta & Warm Wood (`#EA580C`), Classical Teak Wood (`#2D241E`), Deep Emerald Foliage Green (`#059669`).",
    "- **10% Điểm nhấn dẫn mắt:** Luminous Warm Golden Sunrise Rays (`#D97706`), Steaming Rice Amber Particles, Glowing Golden Data Badges.",
    "",
    "---",
    "",
    "### 🛡️ Quy Tắc Kiểm Soát Tuyệt Đối:",
    f"1. **Scene ID chuẩn theo chương:** `CH10_SC001` đến `CH10_SC031` (Khớp 100% với `chapter_10.md`).",
    "2. **100% Không gian vật lý đời thực (Zero Surrealism):** Quán ăn bình dân hè phố, bàn ăn gia đình, cánh đồng lúa miền Tây, đại công trình cống Cái Lớn, phòng GIS tài nguyên nước, thư viện triết học kinh tế.",
    "3. **Quy tắc Text Overlay (Selective Lower-Left 25% Rule):** Chọn lọc 9/31 phân cảnh có Text Overlay đặt tại góc dưới bên trái cách đáy 25%. Tất cả 100% bằng Tiếng Anh chuẩn, viết hoa, thuần ASCII.",
    "4. **Khóa tĩnh Chữ ở Dòng Video:** Mọi cảnh có text overlay bắt buộc dùng cú máy `Steady camera shot` để chống giật chữ và méo font.",
    "5. **Giao thức Ảnh Tham Chiếu Nhân Vật / Địa Danh:**",
    "   - `@cong_cai_lon.jpg` sử dụng tại `CH10_SC024` (Siêu cống Cái Lớn - Cái Bé).",
    "   - `@gs_vo_tong_xuan.jpg` sử dụng tại `CH10_SC025` (Hình ảnh biểu tượng GS Võ Tòng Xuân mang dép rọ lội bùn).",
    "   - Nhân vật dân sự (người dân ăn cơm, gia đình, nông dân): Tả thực bằng ngôn ngữ prompt chính xác, không dùng ảnh nhân tạo.",
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

with open("episodes/vu-khi-gao-viet-nam/chapter_10_visual.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"✅ Generated chapter_10_visual.md ({len(scenes_data)} scenes)")

# 2. Generate prompts_chapter_10.txt
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

with open("episodes/vu-khi-gao-viet-nam/prompts_chapter_10.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompt_lines).strip() + "\n")

print(f"✅ Generated prompts_chapter_10.txt ({len(scenes_data)} scenes)")

# 3. Synchronize scene_timing_map.json with Chapter 10
with open("episodes/vu-khi-gao-viet-nam/scene_timing_map.json", "r", encoding="utf-8") as f:
    map_data = json.load(f)

other_scenes = [s for s in map_data if s.get("chapter") != "10"]

new_ch10_map = []
for sc in scenes_data:
    entry = {
        "id": sc["id"],
        "chapter": "10",
        "duration_sec": float(sc["dur"].replace("s", "")),
        "text_overlay": sc["overlay"] if sc["overlay"] else "None",
        "sentences": [sc["text"]],
        "visual_summary": f"Tier 1: {sc['anatomy']['tier1']} | Tier 2: {sc['anatomy']['tier2']} | Tier 3: {sc['anatomy']['tier3']}"
    }
    new_ch10_map.append(entry)

full_map = other_scenes + new_ch10_map
full_map.sort(key=lambda s: (s.get("chapter", "00"), s.get("id", "")))

with open("episodes/vu-khi-gao-viet-nam/scene_timing_map.json", "w", encoding="utf-8") as f:
    json.dump(full_map, f, ensure_ascii=False, indent=2)

print(f"✅ Synchronized scene_timing_map.json with Chapter 10 (Total scenes now: {len(full_map)})")
