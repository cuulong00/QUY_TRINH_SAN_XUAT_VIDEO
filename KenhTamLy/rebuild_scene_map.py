#!/usr/bin/env python3
"""
Rebuild scene_map.json with hand-crafted visual_summaries.
Each summary follows the 5-layer Doctrine from build_scene_map SKILL:
  1. Chủ thể / không gian nhìn thấy được
  2. Trạng thái cảm xúc chính
  3. Tension hoặc meaning
  4. Hình ảnh / hành động cốt lõi giúp render
  5. Cú lật / contradiction / behavioral mechanism (nếu có)
"""
import json, re, os

EPISODE_DIR = "episodes/nghich-ly-ma-sat-thoi-quen"

# ── Read and split each chapter ──
def split_sentences(text):
    text = re.sub(r"#{1,3}\s+.*", "", text)
    text = re.sub(r"\*\*|\*|_", "", text)
    text = text.strip()
    sents = [s.strip() for s in re.split(r'(?<=[.!?""*])\s+', text) if s.strip() and len(s.strip()) > 5]
    return sents

chapters = {}
for i in range(1, 9):
    path = os.path.join(EPISODE_DIR, f"chapter_{i:02d}.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            chapters[i] = split_sentences(f.read())

# ── Hand-crafted visual_summary maps ──
# Key: (chapter, sentence_group_index) → visual_summary
# These are written by The Visual Architect persona reading each sentence group

VS = {}

# ═══════════════════════════════════════
# CHAPTER 1 — HOOK (1 câu = 1 ảnh)
# ═══════════════════════════════════════
ch1 = chapters[1]
ch1_summaries = [
    # Sent 0: Có một sự thật cực kỳ điên rồ... buổi nhậu nhẹt bí tỉ... kế hoạch mang tên "Mục tiêu nhậu"
    "Một bàn nhậu lộn xộn dưới biển hiệu neon đỏ mờ ám: lon bia đổ tràn, gạt tàn đầy ắp, tờ giấy A4 trắng sạch nằm ngay giữa bàn ghi 'KẾ HOẠCH NHẬU' — sự đối lập phi lý giữa buông thả và kỷ luật.",
    # Sent 1: Và bạn cũng sẽ không bao giờ nhìn thấy... nghiện mua sắm... chuông báo thức... Shopee săn sale
    "Cận cảnh một chiếc điện thoại trên đầu giường lúc nửa đêm, màn hình sáng rực hiển thị app mua sắm sale off, bên cạnh là đồng hồ báo thức đặt ở 10:00 PM — sự vô lý của việc 'lên lịch' cho thói quen xấu.",
    # Sent 2: Nghe có vẻ lố bịch... Chúng ta chưa bao giờ cần... kỷ luật... làm việc tàn phá bản thân... vô thức, say mê
    "Bóng người ngả lưng trên sofa trong ánh sáng TV nhấp nháy xanh lè, tay cầm remote, bàn đầy vỏ bim bim — sự buông thả hoàn toàn không tốn một chút nỗ lực, trôi tuột vào vô thức.",
    # Sent 3: Nhưng hãy nhìn lại... đọc 5 trang sách... thức dậy 5h30... cả bầu trời nỗ lực... vấp ngã... kéo chăn qua đầu... ghê tởm... phản bội lời hứa
    "Chiếc giường lớn trong căn phòng tối tờ mờ sáng 5h30, chăn kéo quá nửa đầu, đôi giày chạy bộ mới tinh nằm chỏng chơ ở góc phòng — cuốn sổ planner mở dở trên tủ đầu giường với những dòng kế hoạch bị gạch xóa đỏ.",
    # Sent 4: Chào bạn, đây là kênh Tâm Lý Học Hành Vi... dao mổ, lật tung cấu trúc hành vi... sự thật tàn nhẫn nhưng giải thoát
    "Góc quay phẳng nhìn xuống một mặt bàn thí nghiệm lạnh lẽo: dao mổ phẫu thuật sáng bóng nằm cạnh mô hình não bộ bằng nhựa trong suốt, ánh đèn spot chiếu thẳng — tâm thế bác sĩ giải phẫu.",
    # Sent 5: Sự thật đầu tiên... hắt gáo nước lạnh... Sự vấp ngã KHÔNG HỀ liên quan đến việc bạn kém cỏi, lười biếng hay thiếu ý chí
    "Cận cảnh nửa khuôn mặt phía trong bóng tối, nửa kia bị lộ ra bởi một tia sáng gắt — đôi mắt nhíu lại đau đớn nhưng ánh nhìn bắt đầu bừng tỉnh, như vừa nghe được một sự thật chưa từng biết.",
    # Sent 6: Khoan đã! Đừng vội phản bác... nhớ lại... đây có phải lần đầu không?
    "Bàn tay giơ lên ra dấu 'dừng lại' trước ống kính, ngón trỏ chỉ thẳng vào người xem, ánh sáng đánh cạnh mép tay tạo bóng sắc nét trên nền tối — cử chỉ thách thức và yêu cầu thành thật.",
    # Sent 7: Có bao nhiêu cuốn sổ Planner tuyệt đẹp mua về, viết 3 trang rồi quăng ngăn kéo?
    "Một chiếc ngăn kéo bàn hé mở, bên trong lộ ra ba bốn cuốn sổ planner bìa da đắt tiền chồng lên nhau, bụi bám, chỉ có vài trang đầu có chữ viết — phần còn lại trắng tinh như chưa từng chạm tay.",
    # Sent 8: Có bao nhiêu thẻ tập Gym... cà thẻ roẹt... số lần đến đếm trên đầu ngón tay?
    "Cận cảnh một chiếc thẻ tập gym nhựa cứng nằm tréo trên ví tiền, bên cạnh một tờ hóa đơn thanh toán cả năm — mặt thẻ bóng loáng cho thấy gần như chưa được quẹt bao giờ.",
    # Sent 9: Có bao nhiêu ứng dụng theo dõi thói quen, học tiếng Anh, học lập trình... nằm đóng bụi trên màn hình?
    "Góc chụp thẳng từ trên xuống màn hình điện thoại: trang cuối cùng đầy ứng dụng đủ màu sắc — Duolingo, Habit Tracker, Coding App — nhưng badge thông báo đều hiện '0 ngày streak', biểu tượng mờ xám như bị lãng quên.",
    # Sent 10: Chúng ta đang sống trong kỷ nguyên mà sự 'chuẩn bị' được lên ngôi
    "Góc rộng quay một kệ sách self-help sặc sỡ chất đầy trong hiệu sách, ánh đèn trắng chiếu rực rỡ nhưng không ai đứng đọc — sự phồn thịnh bề mặt của 'ngành công nghiệp động lực'.",
    # Sent 11: Ngành công nghiệp self-help tiêm niềm tin độc hại: cần động lực vĩ đại, công cụ xịn xò
    "Cận cảnh một chiếc bàn làm việc 'aesthetic' hoàn hảo đến ám ảnh: đèn Lofi vàng ấm, cốc trà hoa cúc bốc khói, tai nghe đắt tiền, cuốn sách mới cứng — nhưng chiếc ghế hoàn toàn trống, không ai ngồi.",
    # Sent 12: Nếu bạn muốn đọc sách... phải tìm đèn bảo vệ mắt... ly trà hoa cúc... playlist Lofi... bàn làm việc aesthetic
    "Một đôi tay nâng niu xếp đặt ly nến thơm cạnh cuốn sách trên bàn, trong khi phía sau lưng người đó, màn hình điện thoại đã tự sáng lên với thông báo — 'sự chuẩn bị' che đậy cho procrastination.",
    # Sent 13: Đủ mọi bước thiết lập. Hoàn hảo đến từng centimet.
    "Macro shot cực gần vào một centimet trên thước đo, đặt nghiêng cạnh cuốn sổ ghi chép được kẻ vạch thẳng tắp — sự kỹ tính ám ảnh dồn vào khâu râu ria thay vì hành động thật sự.",
    # Sent 14: Nhưng rồi, mất 45 phút sắp xếp... mở sách ra... não đặc quánh... 10 phút sau... Ting... lướt Tóp Tóp 2.5h
    "Góc quay nghiêng qua vai: cuốn sách mở úp xuống bàn, bên cạnh là chiếc điện thoại phát sáng xanh lạnh với video ngắn đang tự chạy, cốc trà nguội ngắt — cuốn sách trở thành nhân chứng hờ hững cho thất bại.",
    # Sent 15: Trong khi cuốn sách nằm lăn lóc bên cạnh như một nhân chứng hờ hững cho sự thất bại của bạn.
    "Cận cảnh cuốn sách nằm dưới sàn nhà, mở úp, gáy cong vênh, bên cạnh sợi dây sạc điện thoại rủ xuống — ánh sáng duy nhất hắt từ màn hình smartphone phía trên.",
    # Sent 16: Tại sao chúng ta có thể lướt Tóp Tóp 3 tiếng... cày Netflix nửa đêm tới sáng... không cần động lực?
    "Bóng người nằm trên giường trong bóng tối hoàn toàn, chỉ có ánh sáng xanh điện thoại hắt lên khuôn mặt — đồng hồ treo tường phía sau chỉ 3:00 AM, mắt mở to nhưng vô hồn.",
    # Sent 17: Trong khi đó, đọc 5 trang sách, chạy bộ 15 phút giống như tảng đá 500kg trên ngực?
    "Ký họa ẩn dụ: Bóng người nằm ngửa trên nền sàn lạnh, một khối bê tông ghi chữ 'ĐỌC SÁCH 5 TRANG' đặt nặng trĩu trên ngực — tay chân bất lực buông thõng hai bên.",
    # Sent 18: Một số người gọi đó là hỏng hóc đạo đức. Số khác gọi thói cả thèm chóng chán.
    "Hai bàn tay khác nhau chỉ trỏ về phía nhân vật ngồi cúi đầu: một tay cầm bảng 'LƯỜI BIẾNG', tay kia cầm 'VÔ KỶ LUẬT' — ánh sáng spot chiếu gay gắt từ trên xuống như phiên tòa xét xử.",
    # Sent 19: Nhưng tâm lý học thần kinh gọi nó bằng cái tên hoàn toàn khác. Bài toán năng lượng... não 2.5 triệu năm tuổi.
    "Cận cảnh mặt cắt mô hình não bộ đặt trên bàn, bên cạnh đồng hồ đo điện với kim chỉ vạch đỏ 'LOW' — ánh đèn phòng thí nghiệm lạnh lẽo chiếu gắt, gợi lên cuộc điều tra khoa học.",
    # Sent 20: Thói quen xấu sống dai dẳng... bạn đang vác vũ khí tệ hại nhất... Ý Chí.
    "Bóng người trong tư thế chiến đấu mệt mỏi cầm một thanh kiếm gỉ sét gãy đôi, đối diện một bóng đen khổng lồ vô hình — ánh sáng hắt từ sau lưng bóng đen, nhân vật nhỏ bé và kiệt sức.",
    # Sent 21: Bạn đã dùng sai vũ khí ngay từ đầu. Vậy vũ khí thực sự là gì?
    "Cận cảnh thanh kiếm gỉ sét nằm dưới sàn, phía trên là bóng tay đang với tới một chiếc chìa khóa kim loại nhỏ phát sáng nhẹ treo lơ lửng — sự lựa chọn giữa sức mạnh thô và trí tuệ tinh vi.",
    # Sent 22: Trả lời được câu hỏi này, bạn sẽ nắm được bản đồ để hack lại cỗ máy trong hộp sọ mình.
    "Góc rộng: một bản vẽ kỹ thuật phức tạp của bộ não trải trên bàn, đè bởi một chiếc bút bi và cốc cà phê — ánh sáng ấm từ đèn bàn hắt lên những đường nét blueprint mảnh mai.",
]

# ═══════════════════════════════════════
# CHAPTER 2 — EGO DEPLETION (3 câu = 1 ảnh)
# ═══════════════════════════════════════
ch2_summaries = [
    # G0: Ngành công nghiệp truyền cảm hứng... Ý Chí giống cơ bắp... chiến binh bất khả chiến bại
    "Một bức tượng chiến binh cẩm thạch trắng gồng cơ bắp cuồn cuộn trong bảo tàng tối tăm, ánh đèn spot chiếu gắt từ dưới lên — nhưng những vết nứt li ti đang lan dần trên bề mặt, lớp sơn hoàn hảo bắt đầu bong tróc.",
    # G1: Họ nói 'Chỉ cần quyết tâm đủ lớn, không gì là không thể'. Bạn đã bao giờ tin? Đó là lý do bạn thấy tồi tệ mỗi khi thất bại trước cái chăn ấm.
    "Cận cảnh nửa khuôn mặt nhắm nghiền trên gối trắng lúc 5h sáng, một giọt mồ hôi lạnh chảy dọc thái dương — bức poster 'JUST DO IT' trên tường phía sau bị bóng tối nuốt gần hết, chỉ còn thấy chữ 'DO' nhạt nhòa.",
    # G2: Nhưng nếu tôi nói sự thật khoa học đã bị bẻ cong hoàn toàn?
    "Macro shot: Một viên đá cẩm thạch trắng bị bàn tay bóp nát vụn thành bụi phite — ánh sáng chói từ bên trái lộ ra rõ ràng khoảnh khắc sụp đổ, contrast cực mạnh.",
    # G3: Roy Baumeister... thí nghiệm... mô hình khác... không giống chiến binh cơ bắp
    "Chân dung mờ ảo của một người đàn ông trung niên đeo kính trong phòng lab trắng, tay cầm bảng ghi 'EGO DEPLETION' bằng mực đỏ — ánh đèn huỳnh quang nhợt nhạt chiếu xuống những chồng giấy nghiên cứu.",
    # G4: Ego Depletion... Ý chí không phải cơ bắp... bình xăng = Tài Khoản Ngân Hàng có hạn mức
    "Macro shot cận cảnh: Một chiếc bình thủy tinh lớn chứa chất lỏng vàng ánh đang rỉ rỉ chảy qua vết nứt ở đáy — phía dưới là khoảng trống đen thui, giọt cuối cùng sắp rơi.",
    # G5: Sự thật tàn nhẫn: Mỗi sáng não cấp số dư nhất định... bất kỳ suy nghĩ, quyết định, kiềm chế nào đều bị trừ tiền
    "Góc trên cao nhìn xuống một chiếc máy ATM cũ kỹ trong con hẻm tối. Màn hình sáng đỏ nhấp nháy dòng chữ 'SỐ DƯ: ĐANG GIẢM...' — bàn tay run rẩy đang ấn nút rút tiền.",
    # G6: Hãy nhìn lại một ngày làm việc. Đứng trước tủ quần áo 5 phút phân vân... Ting — trừ ý chí.
    "Bóng người đứng bất động trước tủ quần áo hé mở trong bóng tối buổi sáng. Hai bàn tay cầm hai chiếc áo sơ mi — một đen, một trắng — tư thế đông cứng như robot hết pin.",
    # G7: Kẹt xe, xe máy tạt đầu, nén cục tức xuống ngực, tiếp tục vặn ga. Ting — trừ khoản lớn.
    "Góc quay qua vai nhìn ra dải đèn hậu đỏ rực kẹt xe trong mưa rào. Hai bàn tay nắm chặt tay ga xe máy, gân nổi cuồn cuộn, mặt kính chiếu hậu phản chiếu khuôn mặt cắn chặt răng kiềm nén.",
    # G8: Đồng nghiệp mang bánh quy sô-cô-la. Giảm cân. Quay mặt đi uống nước lọc. Ting — lại trừ tiền.
    "Cận cảnh bàn tay siết chặt ly nước lọc sóng sánh, đối diện là hộp bánh quy socola nâu bóng loáng, ánh đèn vàng ấm chiếu gợi tình — cuộc đấu tranh thầm lặng trong góc phòng nghỉ.",
    # G9: Email khủng hoảng, nụ cười công nghiệp giả tạo với sếp, đống việc lặt vặt tốn não.
    "Cận cảnh khuôn mặt nhân viên văn phòng dưới ánh sáng xanh lè của màn hình — nụ cười gượng ép khô cứng trên môi, mắt mệt mỏi nhìn chằm chằm vào inbox chất đống, tay gõ phím liên tục.",
    # G10: 6 giờ tối quẹt thẻ ra khỏi công ty. Tài Khoản Ý Chí = 0. Ego Depletion hoàn tất chu kỳ.
    "Bàn tay rã rời quẹt chiếc thẻ nhân viên qua máy chấm công, ánh LED xanh nhấp nháy 'CHECK OUT 18:00'. Phía sau, hành lang văn phòng dài hun hút tối dần — ánh sáng tự nhiên cuối cùng lụi tàn.",
    # G11: Nghịch lý: Nhịn ăn sáng xuất sắc, từ chối bánh ngọt... nhưng 11h đêm xé gói mì tôm... ánh sáng tờ mờ tủ lạnh.
    "Ánh sáng lờ mờ duy nhất rỉ ra từ cửa tủ lạnh hé mở lúc 11 giờ đêm. Đôi gối khuỵu xuống nền gạch lạnh, đôi tay run rẩy xé toạc gói mì tôm — toàn bộ phòng bếp chìm trong bóng tối nặng nề.",
    # G12: Sự thật: 11h đêm Ý Chí cháy rụi. Não rệu rã. Tê liệt phân tích. Chỉ muốn ĐƯỜNG và sự dễ chịu tức thời.
    "Cận cảnh chiếc bình thủy tinh từ đầu chương, lần này khô cong hoàn toàn, rỗng tuếch. Một vệt cặn vàng bám đáy bình — ánh sáng hẹp chiếu xuyên qua bình cho thấy sự trống rỗng tuyệt đối.",
    # G13: Dùng ý chí đấu thói quen xấu = giao phó sinh mạng cho bình xăng luôn rỉ rớt. Nhưng ng thành công...?
    "Một tay cầm chiếc bình nứt rỉ chảy, tay kia trỏ về phía chân trời nơi bóng người xa xa đang chạy bộ bình thản lúc 5h sáng — ánh bình minh nhạt hắt lên bóng lưng họ, câu hỏi treo lơ lửng.",
    # G14: Hay não bộ loài người còn che giấu hệ thống bí mật nào khác? Gã Luật Sư và Ông Chủ lười biếng.
    "Góc rộng: Hai cái bóng đen khổng lồ hắt song song trên bức tường trắng — một bóng ngồi ung dung lười nhác, bóng kia đứng nghiêm áo vest tay cầm cặp — đang giằng co một tay lái xe vô hình.",
]

# ═══════════════════════════════════════
# CHAPTER 3 — HỆ THỐNG 1 & 2
# ═══════════════════════════════════════
ch3_summaries = [
    # G0: Cuốn sách Thinking Fast and Slow... Kahneman... Hệ thống 1 & 2... Ông Chủ Lười Biếng & Gã Luật Sư
    "Cuốn sách 'Thinking, Fast and Slow' nằm lật dở trên bàn gỗ tối, phủ bụi mỏng, ánh đèn vệt hẹp highlight lên tựa đề — bên cạnh là hai con cờ vua: quân vua đen (lười biếng) nằm nghiêng và quân mã trắng (logic) đứng thẳng.",
    # G1: Hệ thống 1: Ông Chủ Lười Biếng. Khối óc cổ đại. 95% hành vi vô thức. Đạp ga, bẻ vô lăng tự động.
    "Đôi chân sải bước vô thức trên vỉa hè bê tông lúc chiều muộn, bóng dài đổ trải — ánh mắt chủ nhân nhìn xa xăm, nghĩ chuyện khác, chân tự động né ổ gà quen thuộc. Tự động đến mức máy móc.",
    # G2: Tiến hóa: loài người nguyên thủy đối mặt nguy cơ chết đói. Não bộ tiết kiệm calo. 'Làm giống hôm qua đi'.
    "Ngọn lửa nguyên thủy leo lét cháy trên than tàn trong hang động u tối. Bóng người co ro bên đống lửa — xen lẫn là ánh sáng yếu ớt từ laptop hiện đại phát ra phía counter-shot, hai thế giới giao thoa.",
    # G3: Hệ thống 2: Gã Luật Sư. Ý thức, tập trung, logic. Kế hoạch: 'Giảm 5 ký', 'Đọc xong 1 cuốn sách'.
    "Bóng người mặc áo vest chỉn chu ngồi thẳng lưng ở bàn kính, trước mặt là bảng kế hoạch to-do list ghi bằng mực đen chỉn chu — nhưng trán lấm tấm mồ hôi, cổ áo hơi lỏng, gương mặt gồng cứng.",
    # G4: Gã Luật Sư mắc căn bệnh: Đốt glucose khổng lồ. Mỗi khi muốn làm MỚI hoặc KIỀM CHẾ... Tải Trọng Nhận Thức.
    "Macro shot: Viên đường trắng tinh đang bị nung chảy dần dưới luồng nhiệt, tan rã thành caramel sẫm — nền đen hoàn toàn, ánh lửa duy nhất phản chiếu sự thiêu đốt năng lượng não bộ.",
    # G5: Cuộc chiến bên trong hộp sọ: Ông chủ đi lối mòn tiết kiệm điện vs Gã luật sư leo dốc đá với bình xăng nhỏ. Sáng: Luật Sư mạnh mồm.
    "Hai bóng mờ ảo khổng lồ hắt lên bức tường xám, giằng co giành bẻ vô-lăng ô tô trong sương mờ — một bóng ung dung ngả lưng, bóng kia gồng căng đẩy tay lái.",
    # G6: Buổi sáng: 'Ăn salad thôi!'. Ông Chủ nhượng bộ. Sau 8 tiếng làm việc: Luật Sư kiệt sức gục bàn.
    "Phân đôi khung hình: Bên trái — buổi sáng, hộp salad xanh mướt trên bàn dưới ánh nắng. Bên phải — 10 giờ đêm, Gã Luật Sư kiệt sức gục xuống bàn đầy giấy tờ, bóng tối nuốt chửng ánh sáng.",
    # G7: Ai giành quyền kiểm soát buổi tối? Ông Chủ Lười Biếng. Mục tiêu: TỐN ÍT NĂNG LƯỢNG NHẤT, THỎA MÃN NHANH NHẤT.
    "Bóng đen to lớn của Ông Chủ Lười Biếng trỗi dậy từ chiếc ghế, vươn tay với đầy tham lam về phía chiếc điện thoại sáng rực trên bàn — Gã Luật Sư nằm bẹp dưới sàn, bất lực.",
    # G8: Tờ A4 'Đọc sách 30 phút mỗi tối' = ngôn ngữ ngoài hành tinh. Đọc sách cần Luật Sư ← đã sập nguồn.
    "Tờ giấy A4 dán trên tường ghi 'ĐỌC SÁCH 30 PHÚT MỖI TỐI', chữ nhàu nát, mờ dần dưới bóng đèn ngủ héo úa — ánh sáng duy nhất rực rỡ là từ màn hình TV phía sau phát video ngắn.",
    # G9: Tay mò mẫm vô thức... Bấm nút. Màn hình sáng. Vuốt. Video ngắn hài hước.
    "Cận cảnh ngón tay cái đang vô thức vuốt lên trên màn hình điện thoại trong bóng tối, ánh sáng video ngắn nhảy múa trên khuôn mặt ngây dại — không có sự lựa chọn nào ở đây, chỉ là phản xạ.",
    # G10: Dopamine bắn! Ngọt ngào. Phê pha. KHÔNG CẦN SỨC LỰC NÀO. Zero năng lượng.
    "Cận cảnh con ngươi giãn nở phản chiếu ánh sáng xanh màn hình — khuôn mặt thư giãn tê liệt, miệng hé mở, hoàn toàn đầu hàng trước sự dễ chịu tức thời trong bóng tối.",
    # G11: Bạn lướt ĐT vì đó là cách DUY NHẤT não cạn kiệt sống sót. Thói quen xấu thắng vì luật chơi não bộ.
    "Góc rộng toàn cảnh: người nằm cuộn tròn trên giường giữa căn phòng chật chội, ánh điện thoại xanh là nguồn sáng duy nhất — dây sạc nối từ ổ điện đến tay như một sợi dây rốn nuôi sống.",
]

# ═══════════════════════════════════════
# CHAPTER 4 — MA SÁT NHẬN THỨC
# ═══════════════════════════════════════
ch4_summaries = [
    # G0: Bạn đã hiểu HT1 & HT2, ý chí cạn kiệt. Nhưng tại sao lười biếng luôn thắng áp đảo? Lướt video 3h vs đọc sách = đá 500kg.
    "Phân đôi khung hình bất đối xứng: bên trái — đường trượt nước siêu trơn dốc đứng, bóng loáng mỡ, người lao xuống vô tư. Bên phải — dốc đá gồ ghề, người bé nhỏ cõng tảng đá khổng lồ loạng choạng leo.",
    # G1: Đến lăng kính Ma Sát (Friction). Ma sát nhận thức = năng lượng phải vứt ra để bắt đầu một hành vi.
    "Macro shot: Một viên bi kim loại lăn tự do trên mặt kính trơn — đột ngột gặp một đoạn đường bê tông thô ráp và dừng sựng lại, ma sát hiện diện hữu hình trong vệt xước dài.",
    # G2: Mạng xã hội: Thiết bị điện thoại là kiệt tác tâm lý học khai thác. Kỹ sư Silicon thiết kế Độ Ma Sát = 0.
    "Cận cảnh chiếc điện thoại phát sáng lạnh lẽo trên nền vải đen, thiết kế trau chuốt mịn màng — phản chiếu trên mặt kính là bóng mờ khuôn mặt người dùng đang chìm vào, như bị hút qua gương.",
    # G3: Đếm ma sát: 1-Với tay (=0), 2-Face ID tự mở (=0), 3-App mở sẵn (=0), 4-Video tự play (=0), 5-Vuốt 1/10 calo (=0).
    "Infographic ký họa: 5 khung hình xếp dọc như thang máy — mỗi khung vẽ một bước (tay với, Face ID, app, play, vuốt) kèm nhãn 'MA SÁT = 0' bằng mực đỏ, mũi tên liên tục trôi xuống.",
    # G4: Đường đi thói quen xấu = cầu trượt nước bôi mỡ. Lực cản duy nhất = vuốt ngón tay. HT2 hoàn toàn bị gạt rìa.
    "Ký họa phóng đại: Đường trượt nước dốc đứng bóng nhẫy phủ mỡ, nhìn từ trên xuống vào vực sâu đen kịt — một bàn tay bé xíu đang vuốt cái smartphone như thể đang trượt sóng.",
    # G5: Ma Sát = 0 → thời gian mất hình khối. HT1 chỉ biết 'Vuốt-Có Thưởng-Vuốt Tiếp'. Trượt xuống đáy hồ vô thức.
    "Góc rộng: Hình ảnh ẩn dụ đầm hồ tĩnh lặng tối đen, mặt nước không gợn sóng, ánh trăng phản chiếu — một bóng người đang từ từ chìm xuống, mắt vẫn mở nhìn lên, tư thế buông bỏ.",
    # G6: 'Tôi phải dặn lòng hạn chế bấm điện thoại' = cầm tăm đánh nhau với xe tăng. Ý chí gãy vụn giây đầu tiên.
    "Cận cảnh bàn tay run rẩy cầm một que tăm gỗ mảnh mai, đối diện là bóng thép khổng lồ mờ ảo của một cỗ máy — ánh sáng backlight lóe lên phía sau cỗ máy, nhấn chìm que tăm trong bóng tối.",
    # G7: Bi kịch không chỉ dừng ở thói quen xấu quá dễ. Ác mộng thực sự = cách ta đối xử ước mơ tốt đẹp.
    "Một bông hoa nhỏ mọc lên từ kẽ bê tông trong ngõ tối — nhưng xung quanh nó, ai đó đã vô tình quấn dây kẽm gai dày đặc, cản bông hoa vươn ra ánh sáng.",
    # G8: Thay vì bôi trơn như Silicon, ta tự đóng đinh, quấn kẽm gai, trải chông nhọn lên đường đến thói quen tốt. Giết ước mơ bằng 'Sự hoàn hảo dở hơi'.
    "Ký họa đối chiếu mạnh: Một con đường rẽ đôi — ngã rẽ trái trơn bóng dẫn xuống vực tối (thói quen xấu), ngã rẽ phải đầy đinh nhọn kẽm gai dốc lên (thói quen tốt), bàn chân trần đứng ở ngã ba.",
    # G9: Hãy cùng lật tiếp chương sau, xem bạn đã vô ý tàn sát thói quen tốt bằng cách nào.
    "Bàn tay từ từ lật một trang sách dày, phía dưới trang mới lộ ra dòng chữ viết tay 'CHƯƠNG 5' — ánh sáng hắt nghiêng tạo bóng kịch tính, gợi sự tò mò về bi kịch tiếp theo.",
]

# ═══════════════════════════════════════
# CHAPTER 5 — QUÁ NHIỀU MA SÁT CHO THÓI QUEN TỐT
# ═══════════════════════════════════════
ch5_summaries = [
    # G0: Đường đi thói quen xấu = trượt nước vô ma sát. Thói quen tốt = vác quả tạ 50kg lên đồi đá sắc nhọn.
    "Bóng người cong lưng dưới tảng đá khổng lồ, loạng choạng leo lên sườn dốc đá lởm chởm sắc nhọn, bầu trời xám xịt — mồ hôi và đất bám bụi trên lưng trần, hơi thở nặng nề hữu hình.",
    # G1: Quay lại 5h30 sáng. Dặn lòng chạy bộ 15 phút. Đơn giản? Không. Não thấy CÔNG TRÌNH XÂY DỰNG hàng chục bước.
    "Căn phòng ngủ tối tăm lúc 5h30. Trên tường chiếu sáng là một sơ đồ flow-chart phức tạp với 6 ô vuông nối nhau bằng mũi tên — mỗi ô là một bước chuẩn bị: 'CHĂN', 'TẤT', 'GIÀY', 'NƯỚC', 'NHẠC', 'ÁO KHOÁC'.",
    # G2: Ma sát 1-2-3: Tung chăn (mất nhiệt), tìm tất (gầm tủ), lôi giày (thắt dây tỉ mỉ).
    "Đống đồ lộn xộn dưới ánh sáng mờ buổi sáng: chiếc tất thể thao cuộn tròn lăn lóc gầm giường, dây giày bung bét nằm cạnh đôi giày chạy bộ để sát góc tường tối — sự hỗn loạn nhỏ mà não coi là núi.",
    # G3: Ma sát 4-5-6: Tìm bình nước, cắm tai nghe chọn playlist, tìm áo khoác gió. → Bình xăng ý chí cạn kiệt mà chân CHƯA BƯỚC RA CỬA.
    "Macro shot bàn tay mân mê tai nghe bluetooth chưa kết nối, bên cạnh là bình nước nhựa rỗng — phía sau mờ ảo, cánh cửa phòng vẫn đóng chặt, ánh sáng mới ngày chưa lọt vào nổi.",
    # G4: Não 2.5 triệu năm kết luận: 'Quá rườm rà. Ôm chăn ngủ tiếp. An toàn là trên hết.' → Kết thúc.
    "Bàn tay kéo mạnh chiếc chăn trắng lên quá đầu, chỉ còn thấy mớ tóc rối. Đôi giày chạy bộ vẫn nằm yên bất động ở góc phòng — ánh sáng sớm mai chầm chậm lùi ra, cánh cửa sổ đóng.",
    # G5: Chủ Nghĩa Hoàn Hảo = hung thủ. Phải Gym xịn, thẻ hội viên, băng đô. Đọc sách phải bàn gỗ, cà phê, nhạc.
    "Chiếc bàn làm việc aesthetic hoàn hảo đến mức giả tạo: laptop sạch bóng, ly cà phê khói bay, cây nến, cuốn sổ mở — nhưng ghế trống hoàn toàn, không ai ngồi. 'Procrastination in Disguise'.",
    # G6: Procrastination in Disguise. 45 phút dọn bàn = hình thức tinh vi để não lảng tránh việc MỞ SÁCH RA ĐỌC.
    "Đôi tay nâng niu lau chùi chiếc cốc cà phê trên bàn sạch bóng — nhưng cuốn sách nằm nguyên xi chưa mở, bìa sách phản chiếu bóng người đang loay hoay câu giờ.",
    # G7: Glucose đốt cháy vào khâu râu ria. Bàn đẹp xong → bình xăng vạch đỏ. Kiệt sức. Lôi ĐT ra → mất 3h.
    "Chiếc đồng hồ cát nhỏ trên bàn làm việc đã cạn sạch cát. Bên cạnh: cuốn sách mở trang đầu tiên, nhưng chiếc điện thoại đang sáng rực với video đang chạy — cuộc chiến đã thua từ đầu.",
    # G8: Phân cực tàn bạo: Gỡ ma sát cho thứ độc hại ⇔ rào gai cho thứ tốt đẹp. Nhưng bạn đã qua Tầng Đau Khổ, đến Tầng Nhận Thức.
    "Ký họa hai cánh cửa đối diện: Cửa trái mở toang trơn trượt, dẫn vào vực tối. Cửa phải khóa chặt bởi 5 ổ khóa và dây xích — phía sau cửa phải, ánh sáng ấm áp rực rỡ rò rỉ qua kẽ hở.",
    # G9: Chìa khóa nằm ở 20 giây sinh tử. Con số thần kỳ. Chương trao quyền lực tối hậu. Đừng bỏ lỡ.
    "Cận cảnh bàn tay giơ lên, ngón cái và ngón trỏ cầm chiếc đồng hồ bấm giờ nhỏ hiện số 00:20 — nền tối hoàn toàn, ánh đèn spot chiếu vào mặt đồng hồ như báu vật thiêng liêng.",
]

# ═══════════════════════════════════════
# CHAPTER 6 — LUẬT 20 GIÂY
# ═══════════════════════════════════════
ch6_summaries = [
    # G0: Hít sâu. 2 sự thật: ý chí = bình cạn dần. Não trượt theo đường ít ma sát nhất.
    "Góc rộng: Bóng người ngồi thiền trên sàn gạch lạnh giữa căn phòng trống tối, hai tay đặt trên gối — hít vào, lồng ngực phồng lên, khoảnh khắc tĩnh lặng trước bão giông.",
    # G1: Đừng tuyệt vọng. Hiểu cách cỗ máy hoạt động = trở thành người thợ máy. Sắp xếp lại con đường cho não phải đi qua thói quen tốt.
    "Đôi tay đeo găng kỹ sư đang mở nắp một hộp cơ khí phức tạp, bên trong là bánh răng và dây cáp — ánh đèn bàn hắt lên khuôn mặt tập trung, tư thế thợ máy đang tháo lắp.",
    # G2: Luật 20 Giây (The 20-second Rule) — Shawn Achor. Thao túng tuyệt đối Ông Chủ Lười Biếng. Thói quen xấu +20s, thói quen tốt -20s.
    "Chiếc đồng hồ bấm giờ hiện số '20' đặt giữa bàn, hai bên là hai con đường thu nhỏ mô hình: đường trái bôi keo dính (thêm ma sát), đường phải trơn trượt bóng loáng (giảm ma sát).",
    # G3: HT1 ám ảnh sự ngay lập tức. Gặp 20s vật cản → 'Phiền phức quá, bỏ đi'. Phép màu xuất hiện.
    "Cận cảnh khuôn mặt Ông Chủ Lười Biếng (biểu cảm uể oải) nhìn vào một thanh chắn nhỏ xíu trước mặt, nhăn mặt ghê tởm — thanh chắn chỉ cao 5cm nhưng trong mắt hắn nó giống bức tường thành.",
    # G4: Áp dụng vào thói quen xấu: Nghiện ĐT. Không dặn lòng — vô giá trị khi Luật Sư cạn. Tạo cục ma sát chà bá.
    "Chiếc điện thoại bị nhét sâu vào ngăn kéo khóa chặt ở phòng khác — chìa khóa treo lủng lẳng trên móc xa xôi, sợi dây buộc chặt. Giường ngủ trống trơn, không có ánh sáng xanh nào.",
    # G5: Để ĐT sang phòng khác. Muốn lướt? → 'Phải lật chăn, chạm gạch lạnh, đi bộ sang phòng... mất 20s. Thôi ngủ luôn.'
    "Cận cảnh bàn chân trần do dự trên mép giường, bên dưới là nền gạch lạnh lẽo phát sáng hơi xanh — con đường dẫn sang ngăn kéo xa xa tối mờ, quá dài để Ông Chủ Lười Biếng bận tâm.",
    # G6: Không đánh bằng ý chí mà tấn công bằng CƠ CHẾ LƯỜI BIẾNG. Hãy để não LƯỜI LƯỚT ĐT luôn!
    "Ký họa nhân vật Ông Chủ Lười Biếng nằm ngửa trên sofa, tay với sang phải tìm điện thoại — nhưng chỉ có khoảng trống. Tay phải rụt lại, quay người sang bên và ngủ tiếp.",
    # G7: Thói quen tốt: Triệt tiêu rào cản = 0. Tập thể dục 5h30: Mặc sẵn đồ tập lúc đi ngủ. Giày chặn BĂNG QUA CỬA.
    "Đôi giày thể thao đặt chắn ngang ngưỡng cửa phòng ngủ, tất cuộn gọn nhét bên trong. Bình nước đầy để cạnh. Bộ đồ tập mặc sẵn trên người đang nằm ngủ — mọi thứ giảm ma sát về 0.",
    # G8: Sáng chuông reo. Ông Chủ bật dậy: quần áo sẵn, giày trước mặt. Cởi đồ tốn MA SÁT hơn chạy ra! Auto-pilot bật.
    "Ánh sáng mới len qua rèm. Bàn chân tự động xỏ vào giày đặt ngay mép giường — cánh cửa phòng hé mở, con đường ra ngoài trơn trượt không chướng ngại, bóng người bước ra trong tư thế auto-pilot.",
    # G9: Giới tinh hoa = Kiến Trúc Sư Môi Trường. Thao túng không gian. Bóc gỡ cục đá cản đường.
    "Bóng người điềm đạm mặc áo sơ mi đứng giữa phòng, tay cầm bản vẽ thiết kế nhà, mắt lạnh lùng — xung quanh, căn phòng đã được bố trí tỉ mỉ như bẫy chuột ngược: mọi đường dẫn đều chỉ về thói quen tốt.",
    # G10: Trò chơi cấy ghép Ma Sát. Nhưng còn câu hỏi quyết định: Thời điểm tung chiêu. Chiến trường Ban Đêm.
    "Cửa sổ phòng ngủ nhìn ra bầu trời đêm. Đồng hồ treo tường chỉ 10:00 PM. Bàn tay sắp đặt những vật dụng: chìa khóa vào ngăn kéo, điện thoại sang phòng khác — sự tĩnh lặng trước trận cuối.",
]

# ═══════════════════════════════════════
# CHAPTER 7 — CÚ CẮT TRIGGER
# ═══════════════════════════════════════
ch7_summaries = [
    # G0: Bộ khung lý thuyết hoàn hảo. Nhưng sai thời điểm → sụp đổ. Self-help sai: kháng cự đúng MẮT BÃO. Bất khả thi thần kinh học.
    "Bóng người bé nhỏ đứng giữa cuồng phong đêm tối, tay cầm cuốn sách self-help bay tung tóe — tờ giấy trắng xé toạc trong gió. Mắt bão quay vần phía trên, ánh chớp lật lóa.",
    # G1: Phải chọn chiến trường TRƯỚC KHI kẻ địch thức. Chiến trường = buổi tối đêm hôm trước. 10h đêm. Cú Cắt Trigger.
    "Căn phòng ngủ tĩnh lặng lúc 10 giờ tối. Bóng người ngồi trên mép giường, tay rút dây cắm WiFi Router — ánh đèn LED trên router chớp lần cuối rồi tắt hẳn. Khuôn mặt điềm tĩnh, chủ động.",
    # G2: Trigger = tiếng súng mồi đánh thức HT1 kiếm dopamine. Ánh sáng xanh nhấp nháy, icon Netflix, thông báo đỏ Zalo.
    "Macro shot: Ba biểu tượng ứng dụng — Netflix đỏ, Zalo xanh với badge '99+', TikTok đen — phát sáng neon rực rỡ trên nền đen, như ba viên đạn dopamine sẵn sàng khai hỏa.",
    # G3: 10h tối: Ý chí cạn kiệt. Đừng cố đọc sách hay cự tuyệt MXH. Chỉ cần 1% sức tàn ĐÁNH PHẬP CÁI TRIGGER!
    "Bàn tay mệt mỏi nhưng kiên quyết ấn nút power-off trên chiếc điện thoại cho đến khi màn hình tắt đen — trong bóng tối, chỉ còn ánh sáng đèn đọc sách nhẹ nhàng từ góc phòng.",
    # G4: Rút dây Router, cất ngăn kéo, chốt phòng. Hoặc hẹn giờ chặn internet từ 10h30. Lúc 10h35...
    "Chiếc Router WiFi nằm trong ngăn kéo khóa kín, dây điện cuộn gọn cạnh chìa khóa — trên mặt tủ, chiếc đồng hồ đếm ngược hiện 10:35 PM, phòng tối im lìm.",
    # G5: Cơn nghiện ngứa ngáy. Điện thoại bật lên. Không có mạng. Ông Chủ tính: leo giường, bới chìa, cắm Router, đợi 3 phút... Ma sát khủng!
    "Cận cảnh khuôn mặt Ông Chủ Lười Biếng nhăn nhó cáu kỉnh trước màn hình 'Không có kết nối Internet' — trong đầu ông ta, một danh sách 5 bước chiếu mờ phía trên như bong bóng suy nghĩ nặng nề.",
    # G6: HT1 đầu hàng. Không vì bạn giỏi — vì trò Ma Sát mưu manh quá. Chặn đứt cám dỗ từ gốc mà không tốn nỗ lực lúc cơn nghiện đến.
    "Ông Chủ Lười Biếng buông tay rã rời, quay lưng lại chiếc điện thoại tối đen, kéo chăn lên — gương mặt không phẫn nộ, chỉ lười. Phía xa, chiếc Router vẫn nằm yên trong ngăn kéo khóa.",
    # G7: Quyền lực cao nhất = thiết kế môi trường sao cho cám dỗ không có cơ hội tồn tại. Thói quen tốt: 10h tối dọn đường cho sáng mai.
    "Đôi tay tỉ mỉ xếp bộ đồ tập gấp gọn trên mép giường, bình protein lắc sẵn để cạnh tủ lạnh, tai nghe cắm sẵn vào điện thoại — 10h tối, Kiến Trúc Sư đang lót đường băng cho 6h sáng.",
    # G8: Hãy coi bạn 10h tối = Kiến trúc sư mài vũ khí, chuẩn bị Bẫy Ma Sát cho bạn 6h sáng yếu đuối. Đừng hứa — hãy thiết kế vạch vấp ngã.
    "Phân đôi thời gian: Bên trái — bóng người tỉnh táo lúc đêm đang bày ra dụng cụ chiến đấu (giày, quần áo, bình nước). Bên phải — cùng bóng người đó lúc sáng, mơ màng xỏ chân vào giày đã để sẵn.",
    # G9: Khi làm được → không gồng khổ hạnh. Tiến đến chương cuối: Tự do khỏi sự phán xét bản thân.
    "Bóng người bước ra khỏi cửa trong ánh sáng bình minh hồng nhạt, tay không vác tảng đá nào — bước chân nhẹ nhàng trên con đường đã được dọn sạch chướng ngại từ đêm hôm trước.",
]

# ═══════════════════════════════════════
# CHAPTER 8 — GIẢI PHÓNG
# ═══════════════════════════════════════
ch8_summaries = [
    # G0: Đã đi suốt chặng đường dài: ý chí cạn kiệt, HT1 vs HT2, 20 giây cắt trigger. Nhưng trước khi đóng màn: nhìn lại khối tự trách khổng lồ.
    "Bóng người ngồi bó gối trên mép giường trong bóng tối, lưng tựa tường, đầu cúi — phía trên đỉnh đầu, một đám mây đen nặng nề treo lơ lửng ghi chữ mờ 'THẤT BẠI', 'VÔ KỶ LUẬT'.",
    # G1: Bạn đang xem video một mình. Bên ngoài đi làm, nói cười. Bên trong, dằn vặt kế hoạch dang dở. Không ai nghe thấy.
    "Phân đôi khung hình: Bên ngoài — khuôn mặt cười xã giao trong ánh sáng văn phòng. Bên trong — cùng khuôn mặt đó nhưng nhắm mắt trong bóng tối, tay ôm ngực, vết thương âm ỉ không ai thấy.",
    # G2: Bạn tin mình mang gen 'hỏng', lười biếng hơn người khác.
    "Cận cảnh gương soi vỡ nứt trên tường. Phản chiếu bên trong: khuôn mặt bị méo mó bởi vết nứt — nhưng phía sau gương, ánh sáng ấm đang len lỏi, chờ đợi được nhìn thấy.",
    # G3: Bí mật lớn nhất: Không dạy bạn thành siêu nhân. Chân lý giải phóng: Bạn là con người, loài người tiến hóa để lười biếng sinh học.
    "Bàn tay nhẹ nhàng đặt chiếc mặt nạ 'SIÊU NHÂN Ý CHÍ' xuống bàn — lộ ra phía dưới khuôn mặt thật: bình thường, mệt mỏi, nhưng đôi mắt sáng lên vì vừa hiểu được sự thật.",
    # G4: Não bộ = tác phẩm vĩ đại giữ bạn sống sót. Không quan tâm 6 pack hay 100 cuốn sách. Thói quen xấu = cơ chế phòng vệ sinh tồn.
    "Mô hình não bộ đặt trên bệ cao trong phòng tối, ánh đèn spot chiếu sáng trang trọng như tượng đài — phía dưới chân bệ, vụn vỡ của cuốn sách self-help nằm rải rác.",
    # G5: Vứt bỏ từ điển self-help nhồi chữ 'Ý Chí'. Không thể thắng cỗ máy 2.5 triệu năm bằng khẩu hiệu buổi sáng. Cạn kiệt là đương nhiên.
    "Bàn tay kiên quyết đẩy chồng sách tự lực vang dội xuống mép bàn — sách rơi tung tóe, các bìa sách lóe lên những tiêu đề hào nhoáng 'NEVER GIVE UP', 'THINK BIG'. Phía sau, một tờ giấy trắng sạch sẽ nằm yên.",
    # G6: Đừng tự trừng phạt. Hãy trở nên điềm tĩnh, lạnh lùng, khôn ngoan như nhà thiết kế không gian. Sắp xếp lại các khối gạch.
    "Bóng người đứng bình thản giữa căn phòng, tay cầm bản vẽ thiết kế nội thất — ánh sáng ấm từ cửa sổ chiếu vào lưng, tư thế kiến trúc sư đang định hình lại không gian sống của chính mình.",
    # G7: Đừng cắn răng chống lại. Hãy lấy đi con mồi: Sự vô ma sát. Dịch ĐT xa 2m. Sạc phòng khách. Giấu chìa khóa tivi.
    "Close-up: Ba vật thể nằm cách xa nhau trong căn phòng — điện thoại ở phòng khách, sạc ở góc xa, remote TV trong ngăn kéo. Sợi dây vô hình nối chúng bị cắt đứt.",
    # G8: Bỏ đói thói quen xấu bằng Ma Sát. Ông Chủ Lười Biếng thấy tốn kém → chìm vào giấc ngủ không kêu gào.
    "Ông Chủ Lười Biếng ngả lưng trên sofa, tay buông thõng, mắt nhắm — xung quanh, mọi 'chất gây nghiện' (ĐT, TV, snack) đã bị dời đi xa, trong tầm tay chỉ có cuốn sách và bình nước.",
    # G9: Chúc mừng. Dành lại quyền làm chủ. Không bằng cú đập ý chí mà bằng cái búng tay tĩnh lặng. Ngày mai bắt đầu từ tối nay.
    "Góc rộng: Bóng người đứng ở ban công nhìn ra thành phố lúc bình minh, tay cầm ly cà phê, gió nhẹ — phía sau lưng, căn phòng đã được sắp đặt hoàn hảo. Ánh sáng ấm tràn ngập. Tự do.",
    # G10: Hẹn gặp lại. Kênh Tâm Lý Học Hành Vi. Đừng cố gắng — hãy sắp xếp lại. Chúc buổi tối thiết kế xuất sắc.
    "Fade out: Logo kênh 'TÂM LÝ HỌC HÀNH VI' hiện lên trên nền đen, bên dưới dòng chữ nhỏ 'Đừng cố gắng — hãy sắp xếp lại.' — ánh sáng ấm vàng viền quanh các chữ cái, tĩnh lặng và uy quyền.",
]

# ── Build scenes ──
scenes = []
scene_id = 1

for ch_num in range(1, 9):
    sents = chapters[ch_num]
    group_size = 1 if ch_num == 1 else 3
    
    if ch_num == 1: summaries = ch1_summaries
    elif ch_num == 2: summaries = ch2_summaries
    elif ch_num == 3: summaries = ch3_summaries
    elif ch_num == 4: summaries = ch4_summaries
    elif ch_num == 5: summaries = ch5_summaries
    elif ch_num == 6: summaries = ch6_summaries
    elif ch_num == 7: summaries = ch7_summaries
    elif ch_num == 8: summaries = ch8_summaries
    
    group_idx = 0
    for i in range(0, len(sents), group_size):
        group = sents[i:i+group_size]
        sc = len(group)
        
        # Get the hand-crafted summary or fallback
        if group_idx < len(summaries):
            vs = summaries[group_idx]
        else:
            vs = f"[CẢNH BỔ SUNG Ch{ch_num}] Tiếp nối dòng chảy cảm xúc từ các cảnh trước, ánh sáng chiaroscuro, không gian tâm lý nặng nề."
        
        scenes.append({
            "id": f"scene_{scene_id:03d}",
            "chapter": ch_num,
            "sentence_count": sc,
            "duration_sec": sc * 5,
            "visual_summary": vs
        })
        scene_id += 1
        group_idx += 1

# ── Write output ──
output_path = os.path.join(EPISODE_DIR, "scene_map.json")
with open(output_path, "w") as f:
    json.dump(scenes, f, indent=2, ensure_ascii=False)

# Stats
total = len(scenes)
fallback_count = sum(1 for s in scenes if s["visual_summary"].startswith("[CẢNH BỔ SUNG"))
print(f"✅ Rebuilt scene_map.json: {total} scenes total")
print(f"   Hand-crafted: {total - fallback_count}")
print(f"   Fallback (cần bổ sung): {fallback_count}")
for ch in range(1, 9):
    ch_scenes = [s for s in scenes if s["chapter"] == ch]
    print(f"   Ch{ch}: {len(ch_scenes)} scenes")
