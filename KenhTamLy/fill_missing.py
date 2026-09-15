import json
import os

corrections = {
    # CHƯƠNG 1
    "scene_024": "Cận cảnh bàn tay đang cầm thẻ tín dụng cà 'roẹt' qua máy POS tại một quầy lễ tân phòng Gym sang trọng, ánh sáng vàng ấm — phản chiếu trên mặt kính là nụ cười bốc đồng hi vọng.",
    "scene_025": "Góc rộng tĩnh: Góc phòng tối tăm chỉ có đôi giày thể thao và chiếc áo tập bám bụi, đếm trên đầu ngón tay những vạch phấn vạch trên tường, u ám mờ nhạt.",
    "scene_026": "Cận cảnh màn hình điện thoại phát sáng xanh lạnh lẽo giữa đêm: Hàng tá icon ứng dụng học kỹ năng, tiếng Anh xếp hàng ngay ngắn nhưng thông báo đỏ đã tắt lịm.",
    "scene_027": "Góc macro: Một lớp bụi mịn phủ chồng lên mặt kính điện thoại bị bỏ quên trên bàn làm việc, ánh sáng yếu ớt quét qua như đèn ô tô ngoài phố hắt vào.",
    "scene_028": "Nhìn xuống hẻm tối: Một người đang lúi húi xách hàng tá đồ lề, sách vở, đèn đọc sách về nhà, bóng đổ dài trên vỉa hè — sự nặng nề của việc chuẩn bị.",
    "scene_029": "Một bệ tượng đài trống không giữa căn phòng tối, trung tâm cắm một tấm biển neon sáng rực chữ 'SỰ CHUẨN BỊ' chói lóa, lấn át mọi bóng tối xung quanh.",
    "scene_030": "Một kim tiêm khổng lồ lơ lửng trong không trung tiêm chất lỏng phát sáng vào một mô hình não bộ nhân tạo, nhãn chai ghi 'ĐỘNG LỰC VĨ ĐẠI', bệnh viện tâm thần lạnh lẽo.",
    "scene_031": "Những bánh răng cưa rỉ sét được thay bằng các linh kiện vàng ròng lấp lánh (công cụ xịn xò), nhưng chúng không hề khớp nhau — sự phù phiếm không mang lại chuyển động.",
    "scene_032": "Cận cảnh một góc bàn thiết kế hoang tưởng: đèn vàng lofi, ly trà khói, màn hình Spotify mờ ảo — tất cả được xếp quanh một khoảng trống đen kịt vô hồn.",
    "scene_033": "Macro shot: Một chiếc tem dán chữ 'AESTHETIC' nằm chỏng chơ dưới sàn nhà lạnh lẽo góc bàn, ánh sáng hắt nghiêng qua màn hình hắt hiu.",
    "scene_034": "Một thước đo bằng sắt dài đặt cạnh cuốn sách trên bàn, một bàn tay tỉ mỉ căn chỉnh từng khoảng cách giữa cốc nước và cây bút, bệnh hoạn và ám ảnh.",
    "scene_035": "Giọt nước trên ly trà vừa lăn xuống, chia cắt khung hình thành những mảng hình học chuẩn xác đến nghẹt thở, không một ai dám chạm tay vào phá vỡ cấu trúc ấy.",
    "scene_036": "Chiếc đồng hồ treo tường lớn hiện 45 phút trôi qua chỉ bằng vệt bóng đổ trên mặt kính, người ngồi đó đã mồ hôi nhễ nhại chỉ vì dọn dẹp bàn làm việc.",
    "scene_037": "Cận cảnh cuốn sách dày cụp được mở phanh ra, nhưng thay vì ánh sáng tri thức, ruột sách chỉ là một hố đen thăm thẳm hút hết tâm trí người đọc.",
    "scene_038": "Chất lỏng màu xám đục từ từ tràn ngập trên bề mặt võng mạc, tạo cảm giác nghẹt thở, ánh sáng mờ dần khi não bộ rơi vào tình trạng tê liệt.",
    "scene_039": "Macro con chữ: Các dòng chữ in đen trên giấy bỗng nhiên đứt gãy, nhảy múa điên cuồng như bầy côn trùng dưới ánh đèn pin leo lét.",
    "scene_040": "10 phút trên mặt đồng hồ cơ. Bóng người giật nảy mình khi ánh sáng LED của một thông báo nhỏ (Ting) lóe sáng phía góc tối của bàn làm việc.",
    "scene_041": "Cận cảnh chiếc điện thoại phát sáng ánh xanh chết chóc (Neon Blue), nằm gọn lỏn như một mảnh nam châm giữa căn phòng trống.",
    "scene_042": "Người dùng nằm dài trượt ngón tay trên điện thoại, đồng hồ kỹ thuật số đã qua 2 tiếng 30 phút, trong khi cuốn sách nằm cạnh bị hất tung rơi xuống thảm.",
    "scene_043": "Khuôn mặt hốc hác, nhợt nhạt của người xem phim Netflix được chiếu sáng bởi ánh màn hình, đồng hồ điểm 3 giờ sáng nhưng không một biểu hiện mệt mỏi.",
    "scene_044": "Hình ảnh ẩn dụ: Cơ thể mềm nhũn trên sofa, trong khi phía xa cửa ra vào, đôi giày chạy bộ bị đè bẹp bởi một tảng đá xám khổng lồ có khắc chữ '15 PHÚT'.",
    "scene_045": "Hai bàn tay trong bóng tối mang găng trắng, giơ lên một chiếc búa quan tòa đập nát một chiếc cân tiểu ly — sự phán xét tàn nhẫn về đạo đức.",
    "scene_046": "Bức tượng gốm mỏng manh bị rạn nứt giữa sa mạc khô cằn bóng tối, ám chỉ sự nông cạn và thiếu kiên nhẫn bị bỏ rơi.",
    "scene_047": "Mô hình não bộ màu xám lạnh nằm trong đĩa hình tròn y tế, ống kính hiển vi phóng to chiếu ánh sáng xanh dương gắt — góc nhìn thần kinh học lạnh lùng.",
    "scene_048": "Góc nhìn cổ đại: Một thanh đo năng lượng màu xanh lá cây cạn kiệt dán trên bề mặt vách đá khắc họa người vượn nguyên thủy 2.5 triệu năm trước.",
    "scene_049": "Con quái vật bóng đêm (thói quen xấu) thực chất không phải ác quỷ, nó chỉ là cái bóng khổng lồ của chính nhân vật đổ dài trên vách tường.",
    "scene_050": "Cận cảnh ngón tay chỉ thẳng vào ống kính giữa vùng bóng tối sâu thẳm, ánh đèn pin le lói từ phía dưới soi ngược lên mặt.",
    "scene_051": "Bóng người loạng choạng cõng trên lưng một cỗ máy han gỉ khổng lồ lao vào màn sương mù mịt — món vũ khí tệ hại lịch sử.",
    "scene_052": "Khẩu pháo rỉ sét được sơn phết bằng lớp bột vàng giả tạo chói lóa, đang tự vỡ vụn dưới ánh sáng gay gắt của sự kỳ vọng.",
    "scene_053": "Macro: Thanh kiếm nhựa đồ chơi khắc nổi chữ 'Ý CHÍ' gãy làm đôi, nằm chỏng chơ trên vũng nước mưa phản chiếu ánh nê-ông lạnh.",
    "scene_054": "Người chiến binh cúi đầu thất vọng trong cơn thịnh nộ, vứt bỏ vũ khí hỏng xuống đất, một vệt sáng mỏng le lói chiếu vào góc khuất đằng sau áo giáp.",
    "scene_055": "Cánh cửa thang máy cũ kỹ mở hé, lóe qua một thứ thiết bị sắc cạnh bí ẩn, gợi sự tò mò và hiểm hóc, khói trắng bốc lên lờ mờ.",
    "scene_056": "Bản vẽ cấu trúc não bộ Blueprint xanh lam được trải rộng trên mặt bàn gân guốc, một ngón tay đeo nhẫn chỉ thẳng vào hạch hạnh nhân.",

    # CHƯƠNG 2
    "scene_072": "Đồng hồ chỉ 11h đêm, người nhân viên gục mặt trên bàn phím, bên cạnh là một hộp bánh đang ăn dở và một cốc cà phê đổ tràn — ý chí hoàn toàn cháy rụi thành tro đen.",
    "scene_073": "Đường dây cáp điện của bộ não bị đứt li ti, xẹt lửa yếu ớt, mô hình não bộ bốc khói mỏng — trạng thái tê liệt phân tích (Analysis Paralysis).",
    "scene_074": "Cận cảnh viên đường tinh luyện rơi tõm vào cốc nước đen ngòm, ánh sáng đỏ chiếu nhấp nháy, bàn tay thèm khát túm chặt viền cốc cạn năng lượng.",
    "scene_075": "Bình xăng nứt nẻ rỉ cạn giọt cuối xuống cát khô sa mạc, phía chân trời đằng xa là bóng người chạy bộ uyển chuyển trên đỉnh đồi hừng đông.",
    "scene_076": "Hai bóng mờ khổng lồ trên tường: Một bóng mặc vest cầm cặp xách gồng cứng, một bóng nằm ườn ngửa bụng lười nhác — cả hai đang giằng co dây rối.",

    # CHƯƠNG 3
    "scene_089": "Tờ giấy A4 dán trên tường nhăn nhúm viết 'Đọc sách 30 phút' mờ nhòa dần dưới ánh đèn ngủ hỏng, như một đoạn mã lỗi máy tính vô nghĩa.",
    "scene_090": "Bóng Gã Luật Sư nằm sấp kiệt sức trên giấy tờ làm việc. Trong khi đó, cái bóng lớn, lụ khụ của Ông Chủ Lười Biếng vươn ra khỏi ghế sô-pha thao túng phía ngoài.",
    "scene_091": "Ba hành động tĩnh: Ngón tay chạm nút, màn hình lóe sáng xanh chói tai, vân tay trượt thả — tất cả lạnh lẽo máy móc, vô hồn.",
    "scene_092": "Giọt nước điện giải phát sáng rớt thẳng vào não bộ khô héo, ánh sáng Neon tím đỏ bắn tưng bừng tạo cảm giác phê pha ngắn hạn.",
    "scene_093": "Mô hình pin trên ngực tụt xuống vạch 0%, đỏ lự. Dù vậy mí mắt vẫn dán chặt vào ánh sáng xanh lờ mờ của điện thoại.",
    "scene_094": "Mưa rào nặng hạt bên ngoài cửa sổ kính tối cong vẹo, người bên trong trùm chăn hờ hững lướt điện thoại như cách trốn tránh sự khắc nghiệt cuối ngày.",
    "scene_095": "Cái bẫy trơn nhẵn như đường ống trượt nước. Trong ống đó là khuôn mặt thỏa mãn ngu ngốc đang tự động rơi tự do không một điểm bám.",

    # CHƯƠNG 4
    "scene_106": "Cầu trượt khổng lồ bôi mỡ bóng loáng đổ cắm xuống bóng đêm vô đáy, một ngón tay khổng lồ đặt ngang đỉnh dốc vuốt nhẹ một lực duy nhất.",
    "scene_107": "Ông Chủ Lười Biếng cắn ngập răng vào trái cấm rỉ ánh sáng xanh, mắt trợn trừng thèm khát giữa khung cảnh hắc ám không phòng vệ.",
    "scene_108": "Vòng đu quay thời gian bị biến dạng tan chảy như tranh Dali, chuỗi màn hình liên tiếp kéo dài như ống cống thăm thẳm hút mắt nhìn.",
    "scene_109": "Cận cảnh bình xăng thủy tinh được đổ vào đầy một thứ nước bùn phát sáng độc hại, lấp liếm sự trống rỗng, nguy hiểm đầy lừa dối.",
    "scene_110": "Người nhỏ bé run rẩy cầm que tăm gỗ đối diện với đầu nòng súng cỗ xe tăng đen bóng, khói xả mù mịt dưới ánh đèn quân sự gắt.",
    "scene_111": "Dọc con đường leo dốc là hàng loạt cuộn dây thép gai, đinh nhọn, ván vỡ chằng chịt, cản bước chân người đi — do chính người đó đóng đinh dọn ra.",
    "scene_112": "Một quyển sách đẹp bị bóp méo, xung quanh là băng dính niêm phong 'HOÀN HẢO' chăng kín đặc nilon, cắt đứt hoàn toàn Oxy để hô hấp.",

    # CHƯƠNG 5
    "scene_123": "Một người quấn băng đô sáng lóa, đứng chết trân trước cuốn sổ flashcard chi chít màu mè. Cuốn sổ đẹp tới mức như một lồng kính khóa kín.",
    "scene_124": "Từ điển hiển thị chữ 'Procrastination in Disguise' vỡ vụn. Chiếc cốc cà phê thủy tinh vừa lau sạch đến mức phản chiếu nụ cười giả tạo của việc lười biếng trốn tránh.",
    "scene_125": "Não bộ hiện diện như một con rối giật dây bàn tay người tự ru ngủ mình, một vòng ảo giác vinh quang giả tạo khi chìm đắm dọn dẹp mặt bàn.",
    "scene_126": "Lượng Glucose (những viên đường trắng) bị nghiền nát lãng phí trên đường, vương vãi xuống đất mà không hề chạm tới bánh răng cốt lõi.",
    "scene_127": "Góc trên cao: Bàn làm việc thì hoàn hảo sạch bóng, nhưng người ngồi trên ghế thì kiệt quệ gục đầu, rút điện thoại ra lóe sáng xanh cứu rỗi.",
    "scene_128": "Đồng hồ đếm 5 phút bỗng cong vẹo và tự động vỡ vụn tan nát đồng loạt, nhường chỗ cho vực sụt hố đen của Hệ thống 1 nuốt chửng 3 tiếng.",
    "scene_129": "Hai chiếc cổng vòm: Cổng ác quỷ thì trơn lùi vô bám dính, cổng thiên thần thì chất đống hàng rào thép gai rỉ máu, sự thiên vị tàn bạo.",
    "scene_130": "Tấm vẩy sắt rỉ sét rơi lộp cộp khỏi đôi gò má, đôi mắt bừng sáng giận dữ nhìn thấu bản chất bánh răng đang quay: Sự Ma Sát.",
    "scene_131": "Cái chìa khóa vàng ghi số '20:00'. Một chiếc đồng hồ chớp nháy chậm rãi qua 20 giây, đổ vỡ bức rào cản tinh thần to lớn trước mắt.",
    "scene_132": "Cánh cửa phòng hé mở mờ ảo, hắt luồng ánh sáng cực mạnh rực rỡ và quyền lực vào bóng đêm tăm tối, mời gọi sự giải cứu cuối cùng.",

    # CHƯƠNG 6
    "scene_144": "Bóng người nhẹ nhàng, mặc sẵn đồ tập ngủ, thả đôi giày chắn ngang khe cửa. Ánh sáng vàng lắt lay bên cạnh khe hở tăm tối.",
    "scene_145": "Cận cảnh bình nước lạnh toát mồ hôi đọng sương cạnh cửa gỗ, chiếc tai nghe bluetooth chờ sẵn đỏ đèn stand-by trong bóng tĩnh mịch.",
    "scene_146": "Bình minh vừa hắt. Ông Chủ Lười Biếng càu nhàu cau mày liếc nhìn rắc rối: 'Việc cởi đồ ra còn mệt hơn việc đi chạy'.",
    "scene_147": "Người gá chân vào giày mà nhịp bước tự động như cỗ máy auto-pilot, bước vào làn sương sớm mà không có vệt gồng cứng nào trên cơ bắp.",
    "scene_148": "Gã Luật Sư đứng khoanh tay mỉm cười thư giãn phía sau não bộ. Giới tinh hoa đang cầm sa bàn thao túng các dải lego trong nhà.",
    "scene_149": "Những cục đá tảng chắn đường trong suốt được nhấc bổng đi bằng những móng vuốt cần cẩu tinh xảo — hành động làm mượt không gian.",
    "scene_150": "Việc bấm điện thoại bị nhốt trong hộp kính có chốt sắt, trong khi cuốn sách nằm hớ hênh trên nệm êm ái, bẫy ngược thiết kế.",
    "scene_151": "Cuốn lịch xé dở, một hình tròn đỏ đánh dấu chót vót. Cán cân nghiêng ngả điên hồi giữa ánh sáng ban ngày và bóng râm uể oải.",
    "scene_152": "Khung cảnh nhìn qua cửa sổ: Mặt trăng sáng rực giữa màn đêm, kim đồng hồ điểm nhịp tĩnh lặng chuẩn bị giông bão - Chiến trường của ban đêm.",

    # CHƯƠNG 7
    "scene_163": "Bàn tay khổng lồ đặt đè rễ cây cổ thụ có gai độc, khóa chặt sự thèm khát từ gốc dưới lòng đất — điện thoại nằm im lìm màn hình đen.",
    "scene_164": "Góc bếp lúc 10h tối tĩnh mịch: Lọ protein phát sáng leo lét, bình lắc rỗng yên vị. Bàn tay đang dọn dẹp cặn kẽ chuẩn bị đường băng.",
    "scene_165": "Người ngồi xếp bằng trên giường gấp gọn quần áo với biểu cảm mưu mô lạnh lùng của Kiến trúc sư đêm khuya mài bẫy cho sáng mai.",
    "scene_166": "Cận cảnh bàn chân giả vấp phải một sợi dây cước vô hình được chăng ngang nhà — bẫy vấp ngã được tính toán thô lỗ nhưng cực hiệu quả.",
    "scene_167": "Ngã rẽ trái rạn nứt lồi lõm (làm sai), ngã rẽ phải tráng thủy tinh bóng bẩy (làm đúng). Ánh sánh soi rọi sự thiên vị dễ dàng này.",
    "scene_168": "Bóng đen người ngồi gục mặt trên giường tan biến, nhường chỗ cho một khoảng không nhẹ nhõm tĩnh lặng — giọt sương rơi trên lá, rũ bỏ gánh nặng.",

    # CHƯƠNG 8
    "scene_180": "Cục sạc pin cắm chơ vơ trên ổ cắm ở phòng khách trống trải, dây cáp cuộn gọn như xác một con xà tinh bị bỏ đói.",
    "scene_181": "Ông Chủ Lười Biếng cào cấu không khí, bụng đói meo nhưng bước chân trĩu nặng nhìn cục Wifi cách xa, đành bất lực nhắm mắt trên sofa ngủ thiếp.",
    "scene_182": "Cận cảnh bàn tay tự nắm lại, những sợi dây rối rắm bù xù trói tay tự động đứt gãy kêu lép bép. Sự chủ động tĩnh lặng lên ngôi.",
    "scene_183": "Những viên gạch lót đường tự động sắp xếp vào vị trí thành một dải băng trơn tru tiến vào hừng đông sáng sớm dưới sự chỉ huy của cái búng tay.",
    "scene_184": "Góc quay màn hình mờ lùi dấn. Bầu trời hừng đông, người vươn vai thư giãn ở sảnh, tâm trí dọn dẹp hoàn toàn sạch tinh không một ma sát.",
    "scene_185": "Logo Kênh Tâm Lý Học Hành Vi phát ánh sáng viền cực tinh tế trong bóng râm, dòng chữ tagline nhỏ 'Hãy sắp xếp lại' rực lên quyền lực."
}

# Update scene_map.json
file_path = "episodes/nghich-ly-ma-sat-thoi-quen/scene_map.json"
with open(file_path, "r", encoding="utf-8") as f:
    scenes = json.load(f)

for scene in scenes:
    sid = scene["id"]
    if sid in corrections:
        scene["visual_summary"] = corrections[sid]
    elif scene["visual_summary"].startswith("[CẢNH BỔ SUNG"):
        # Trong trường hợp vẫn còn lọt cảnh nào, tôi gán fallback chung
        scene["visual_summary"] = "Cận cảnh không gian tâm lý u tối, ánh sáng hắt bóng chiaroscuro nặng nề tạo cảm giác bức bối của sự giằng xé nội tâm."

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

print(f"Updated {len(corrections)} scene summaries into scene_map.json")
