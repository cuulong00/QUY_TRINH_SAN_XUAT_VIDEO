import os

base_dir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/byd-co-may-hoan-hao-2'
ch4_file = os.path.join(base_dir, 'chapter_04.md')
vis_file = os.path.join(base_dir, 'chapter_04_visual.md')
prompt_file = os.path.join(base_dir, 'prompts_chapter_04.txt')

# 1. Write chapter_04.md
ch4_text = '''# chapter_04.md

Lời giải thích cho sự bất lực đó nằm ở một sự mỉa mai của lịch sử. Châu Âu và nhiều quốc gia đang bị trói chặt bởi chiếc áo nịt ngực thương mại tự do do chính họ dệt nên, cùng một mạng lưới mâu thuẫn lợi ích không thể tháo gỡ.

Dưới luật Tối huệ quốc của Tổ chức Thương mại Thế giới, bạn không thể tùy tiện đóng sập cửa biên giới với một sản phẩm đạt chuẩn an toàn năm sao Euro NCAP và không vi phạm bất kỳ bộ luật khí thải nào. Nhưng thứ làm phương Tây khiếp sợ hơn cả luật pháp, là nỗi sợ bị trả đũa cực đoan. Mỗi khi Brussels rục rịch giáng đòn vào B Y D, Bắc Kinh lập tức phát đi tín hiệu cảnh báo nhắm thẳng vào điểm yếu gót chân Achilles của châu Âu: hàng triệu chiếc ô tô của Volkswagen, B M W hay Mercedes đang lăn bánh tại thị trường Trung Quốc, cùng hàng loạt nông sản chủ lực của Pháp.

Sự bất lực đó còn bị xới tung bởi cuộc giằng xé ngay trong nội bộ chính phủ sở tại. Bộ Môi trường ra sức ủng hộ những chiếc xe điện B Y D giá hai mươi nghìn đô để hoàn thành cam kết Net Zero. Trong khi đó, Bộ Công thương lại đau đầu tìm cách áp thuế để cứu các hãng xe nội địa. Ngay cả người dân — những cử tri đang thắt lưng buộc bụng vì lạm phát — cũng phẫn nộ nếu chính phủ cấm một sản phẩm vừa rẻ vừa an toàn chỉ để bảo hộ lợi nhuận cho các tập đoàn ô tô cũ. Sự rạn nứt lên đến đỉnh điểm khi ngay trong nội bộ Liên minh châu Âu, Đức quyết liệt bỏ phiếu chống áp thuế B Y D vì sợ Trung Quốc trả đũa ngược, đối đầu gay gắt với phe ủng hộ của Pháp.

Nhận diện rất rõ điểm yếu này, B Y D không bao giờ đi một mình. Họ bắt tay với các tài phiệt phân phối quyền lực nhất tại địa phương, biến các doanh nghiệp bản địa thành một tấm khiên pháp lý. Khi chính quyền muốn trừng phạt B Y D, họ nhận ra mình sẽ đập vỡ nồi cơm và đẩy hàng ngàn lao động bán hàng tại quê nhà vào cảnh mất việc.

Và khi các rào cản hành chính bị giăng ra, cỗ máy này chứng minh khả năng lách luật hoàn hảo. Tháng mười năm hai nghìn không trăm hai mươi tư, khi E U áp thuế chống trợ cấp mười bảy phần trăm, đẩy tổng thuế lên hai mươi bảy phần trăm đối với xe thuần điện, B Y D lập tức bơm hàng loạt mẫu xe lai điện cắm sạc P H E V sang châu Âu — dòng xe chỉ phải chịu mức thuế mười phần trăm thông thường.

Khi kẽ hở bị siết lại, họ dùng tiền đè bẹp điều kiện nội địa hóa. B Y D giải ngân nhanh bốn tỷ euro xây đại tổ hợp sản xuất tại Hungary, và cam kết thêm một tỷ đô la tại Indonesia. Những chiếc xe xuất xưởng từ đây sẽ mang nhãn Made in Europe với mức thuế nội khối bằng không. Họ củng cố sự bất khả xâm phạm đó bằng hạm đội tàu biển tự đóng trị giá sáu trăm chín mươi triệu đô la, tự làm chủ mọi tuyến hàng hải.

Chỉ duy nhất một nơi trên thế giới dám sử dụng bạo lực pháp lý cực đoan để chặn đứng cỗ máy này: Nước Mỹ. Washington không đàm phán. Họ dựng lên bức tường lửa một trăm phần trăm thuế quan, đi kèm Đạo luật An ninh Xe Kết nối, cấm tiệt mọi phần mềm và phần cứng Trung Quốc. Mỹ chấp nhận xé bỏ mọi nguyên tắc thương mại tự do để bảo vệ sự tồn vong của ngành công nghiệp ô tô nội địa.

Nhưng thế giới không phải ai cũng là nước Mỹ. Ở những thị trường mà cỗ máy đó đã thâm nhập sâu rộng, phía sau mức giá siêu rẻ, những hệ lụy chìm bắt đầu xuất hiện.
'''

with open(ch4_file, 'w', encoding='utf-8') as f:
    f.write(ch4_text)

# 2. Write chapter_04_visual.md
vis_text = '''# chapter_04_visual.md

### CH04_SC001
- **[THOẠI]:** Lời giải thích cho sự bất lực đó nằm ở một sự mỉa mai của lịch sử.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Góc quay rộng hội trường Berlaymont tại Brussels, các chính khách Châu Âu đứng lặng yên dưới ánh đèn chiaroscuro trầm mặc.
- **[TEXT OVERLAY]:** Không

### CH04_SC002
- **[THOẠI]:** Châu Âu và nhiều quốc gia đang bị trói chặt bởi chiếc áo nịt ngực thương mại tự do do chính họ dệt nên,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cận cảnh cuốn sách Hiệp định Thương mại Tự do bọc da mạ vàng nằm trên bàn, bên trên là một sợi dây thừng xích sắt siết chặt lấy bìa sách.
- **[TEXT OVERLAY]:** "FREE TRADE BOUND"

### CH04_SC003
- **[THOẠI]:** cùng một mạng lưới mâu thuẫn lợi ích không thể tháo gỡ.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Mô hình đồ họa 3D gồm các bánh răng chính trị và kinh tế Châu Âu bị kẹt cứng, không thể xoay chuyển.
- **[TEXT OVERLAY]:** Không

### CH04_SC004
- **[THOẠI]:** Dưới luật Tối huệ quốc của Tổ chức Thương mại Thế giới,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Trụ sở WTO tại Geneva với lá cờ phát sáng, phía trước là chiếc cân công lý đại diện cho nguyên tắc MFN (Most Favored Nation).
- **[TEXT OVERLAY]:** "WTO MFN PRINCIPLE"

### CH04_SC005
- **[THOẠI]:** bạn không thể tùy tiện đóng sập cửa biên giới với một sản phẩm đạt chuẩn an toàn 5 sao Euro NCAP
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Chiếc xe BYD Seal thực hiện bài kiểm tra va chạm (Crash test) tại phòng thí nghiệm Euro NCAP, kết quả hiển thị 5 ngôi sao vàng phát sáng tuyệt đối.
- **[TEXT OVERLAY]:** "EURO NCAP 5-STAR SAFETY"

### CH04_SC006
- **[THOẠI]:** và không vi phạm bất kỳ bộ luật khí thải nào.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bảng điện tử đo nồng độ khí thải báo chỉ số 0.00 g/km màu xanh lá cây an toàn.
- **[TEXT OVERLAY]:** "ZERO EMISSION COMPLIANT"

### CH04_SC007
- **[THOẠI]:** Nhưng thứ làm phương Tây khiếp sợ hơn cả luật pháp, là nỗi sợ bị trả đũa cực đoan.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Phòng họp kín tại Berlin với các quan chức Đức đang thảo luận căng thẳng dưới bầu không khí u uất.
- **[TEXT OVERLAY]:** "FEAR OF RETALIATION"

### CH04_SC008
- **[THOẠI]:** Mỗi khi Brussels rục rịch giáng đòn vào BYD,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Tòa nhà Ủy ban Châu Âu EU tại Brussels với các bóng đèn sáng tối dồn dập.
- **[TEXT OVERLAY]:** Không

### CH04_SC009
- **[THOẠI]:** Bắc Kinh lập tức phát đi tín hiệu cảnh báo nhắm thẳng vào điểm yếu gót chân Achilles của châu Âu:
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Tòa nhà Bộ Thương mại tại Bắc Kinh, bóng của quan chức phát đi thông điệp đe dọa thương mại.
- **[TEXT OVERLAY]:** Không

### CH04_SC010
- **[THOẠI]:** hàng triệu chiếc ô tô của Volkswagen, BMW hay Mercedes đang lăn bánh tại thị trường Trung Quốc,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đại lộ sầm uất tại Thượng Hải kẹt cứng những chiếc xe Volkswagen, BMW, Mercedes mang biển số Trung Quốc.
- **[TEXT OVERLAY]:** "GERMAN AUTO EXPOSURE IN CHINA"

### CH04_SC011
- **[THOẠI]:** cùng hàng loạt nông sản chủ lực của Pháp.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cảng xuất khẩu Pháp với hàng ngàn thùng rượu vang Cognac và nông sản đang chờ xếp hàng đi Trung Quốc.
- **[TEXT OVERLAY]:** "FRENCH AGRICULTURAL EXPORTS"

### CH04_SC012
- **[THOẠI]:** Sự bất lực đó còn bị xới tung bởi cuộc giằng xé ngay trong nội bộ chính phủ sở tại.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hành lang Nghị viện Châu Âu chia đôi làm hai luồng ánh sáng đối lập: Xanh lục và Đỏ.
- **[TEXT OVERLAY]:** INTERNAL GOVERNMENT SPLIT

### CH04_SC013
- **[THOẠI]:** Bộ Môi trường ra sức ủng hộ những chiếc xe điện BYD giá 20.000 đô để hoàn thành cam kết Net Zero.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Quan chức Bộ Môi trường chỉ tay vào biểu đồ chỉ tiêu khí thải Net Zero 2030 cạnh chiếc xe BYD Dolphin giá $20,000.
- **[TEXT OVERLAY]:** "NET ZERO 2030 TARGET ($20,000 EV)"

### CH04_SC014
- **[THOẠI]:** Trong khi đó, Bộ Công thương lại đau đầu tìm cách áp thuế để cứu các hãng xe nội địa.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Quan chức Bộ Công thương ôm đầu bên đống hồ sơ báo cáo sụt giảm doanh thu của các hãng xe truyền thống Châu Âu.
- **[TEXT OVERLAY]:** "DOMESTIC INDUSTRY PROTECTION"

### CH04_SC015
- **[THOẠI]:** Ngay cả người dân — những cử tri đang thắt lưng buộc bụng vì lạm phát —
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Người dân Châu Âu đi siêu thị thắt lưng buộc bụng, nhìn vào hóa đơn lạm phát với ánh mắt lo âu.
- **[TEXT OVERLAY]:** Không

### CH04_SC016
- **[THOẠI]:** cũng phẫn nộ nếu chính phủ cấm một sản phẩm vừa rẻ vừa an toàn chỉ để bảo hộ lợi nhuận cho các tập đoàn ô tô cũ.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Nhóm cử tri đứng trước đại lý xe BYD giơ biểu ngữ phản đối việc chính phủ tăng thuế xe giá rẻ.
- **[TEXT OVERLAY]:** "VOTER BACKLASH ON TARIFFS"

### CH04_SC017
- **[THOẠI]:** Sự rạn nứt lên đến đỉnh điểm khi ngay trong nội bộ Liên minh châu Âu,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bản đồ Liên minh Châu Âu EU bị nứt đôi ở đường biên giới giữa Đức và Pháp.
- **[TEXT OVERLAY]:** "EU MEMBER STATE FRACTURE"

### CH04_SC018
- **[THOẠI]:** Đức quyết liệt bỏ phiếu chống áp thuế BYD vì sợ Trung Quốc trả đũa ngược,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đại diện nước Đức tại Brussels bấm nút VOTE NO đỏ chói trong cuộc bỏ phiếu áp thuế xe điện Trung Quốc.
- **[TEXT OVERLAY]:** "GERMANY: VOTE NO ON TARIFFS"

### CH04_SC019
- **[THOẠI]:** đối đầu gay gắt với phe ủng hộ của Pháp.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đại diện nước Pháp bấm nút VOTE YES xanh lục, ánh mắt đối đầu gay gắt với phía Đức.
- **[TEXT OVERLAY]:** "FRANCE: VOTE YES"

### CH04_SC020
- **[THOẠI]:** Nhận diện rất rõ điểm yếu này, BYD không bao giờ đi một mình.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Lãnh đạo BYD mỉm cười bắt tay với các tài phiệt phân phối Châu Âu trong một phòng tiệc sang trọng.
- **[TEXT OVERLAY]:** Không

### CH04_SC021
- **[THOẠI]:** Họ bắt tay với các tài phiệt phân phối quyền lực nhất tại địa phương,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Tòa nhà trụ sở tập đoàn phân phối Hedin Mobility tại Châu Âu với các biển hiệu đại lý BYD hoành tráng.
- **[TEXT OVERLAY]:** "LOCAL DISTRIBUTOR ALLIANCE"

### CH04_SC022
- **[THOẠI]:** biến các doanh nghiệp bản địa thành một tấm khiên pháp lý.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đồ họa 3D hiển thị chiếc khiên thủy tinh bảo vệ BYD, dán nhãn logo của tập đoàn phân phối bản địa.
- **[TEXT OVERLAY]:** "LOCAL LEGAL SHIELD"

### CH04_SC023
- **[THOẠI]:** Khi chính quyền muốn trừng phạt BYD, họ nhận ra mình sẽ đập vỡ nồi cơm
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bộ trưởng Pháp lý Châu Âu dừng tay cầm búa thẩm phán, nhìn xuống bản đồ hàng ngàn đại lý bản địa.
- **[TEXT OVERLAY]:** Không

### CH04_SC024
- **[THOẠI]:** và đẩy hàng ngàn lao động bán hàng tại quê nhà vào cảnh mất việc.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Nhân viên bán hàng bản địa người Châu Âu lo lắng đứng trong showroom BYD vắng khách.
- **[TEXT OVERLAY]:** "LOCAL JOBS AT RISK"

### CH04_SC025
- **[THOẠI]:** Và khi các rào cản hành chính bị giăng ra, cỗ máy này chứng minh khả năng lách luật hoàn hảo.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Mô hình xe BYD luồn lách qua các thanh rào chắn thuế quan màu đỏ.
- **[TEXT OVERLAY]:** Không

### CH04_SC026
- **[THOẠI]:** Tháng 10 năm 2024, khi EU áp thuế chống trợ cấp 17%,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Văn bản nghị định của EU áp thuế 17% Anti-Subsidy Duty được đóng dấu đỏ.
- **[TEXT OVERLAY]:** "OCT 2024: EU 17% ANTI-SUBSIDY TARIFF"

### CH04_SC027
- **[THOẠI]:** đẩy tổng thuế lên 27% đối với xe thuần điện,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đồ họa hiển thị phép tính: 10% Base Tariff + 17% Anti-Subsidy = 27% Total Tariff trên xe BEV.
- **[TEXT OVERLAY]:** "TOTAL BEV TARIFF: 27%"

### CH04_SC028
- **[THOẠI]:** BYD lập tức bơm hàng loạt mẫu xe lai điện cắm sạc PHEV sang châu Âu
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Mẫu xe BYD Seal U DM-i Super Hybrid (PHEV) chạy lướt qua ranh giới cảng biển Châu Âu.
- **[TEXT OVERLAY]:** "PHEV SUPER HYBRID PUSH"

### CH04_SC029
- **[THOẠI]:** — dòng xe chỉ phải chịu mức thuế 10% thông thường.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bảng thuế quan hiển thị dòng chữ "PHEV IMPORT DUTY: ONLY 10%" phát sáng xanh an toàn.
- **[TEXT OVERLAY]:** "PHEV TARIFF: ONLY 10%"

### CH04_SC030
- **[THOẠI]:** Khi kẽ hở bị siết lại, họ dùng tiền đè bẹp điều kiện nội địa hóa.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Tệp hồ sơ quy định Tỷ lệ Nội địa hóa (Local Content Rule) bị đè nát bởi một cọc tiền Euro khổng lồ.
- **[TEXT OVERLAY]:** "LOCALIZATION BYPASS"

### CH04_SC031
- **[THOẠI]:** BYD giải ngân nhanh 4 tỷ euro xây đại tổ hợp sản xuất tại Hungary,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Công trường xây dựng nhà máy khổng lồ của BYD tại Szeged, Hungary với các cần cẩu hoạt động nhộn nhịp.
- **[TEXT OVERLAY]:** "HUNGARY PLANT (€4 BILLION)"

### CH04_SC032
- **[THOẠI]:** và cam kết thêm 1 tỷ đô la tại Indonesia.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Lễ ký kết dự án nhà máy BYD tại Tây Java, Indonesia với số vốn $1 Billion.
- **[TEXT OVERLAY]:** "INDONESIA PLANT ($1 BILLION)"

### CH04_SC033
- **[THOẠI]:** Những chiếc xe xuất xưởng từ đây sẽ mang nhãn Made in Europe với mức thuế nội khối bằng không.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cận cảnh logo "MADE IN EUROPE" được gắn vào đuôi xe BYD vừa xuất xưởng tại nhà máy Hungary.
- **[TEXT OVERLAY]:** "MADE IN EUROPE (0% INTRA-EU TARIFF)"

### CH04_SC034
- **[THOẠI]:** Họ củng cố sự bất khả xâm phạm đó bằng hạm đội tàu biển tự đóng trị giá 690 triệu đô la,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hạm đội 8 tàu vận tải Ro-Ro khổng lồ của BYD rẽ sóng tiến vào các hải cảng thế giới.
- **[TEXT OVERLAY]:** "$690M OWNED FLEET"

### CH04_SC035
- **[THOẠI]:** tự làm chủ mọi tuyến hàng hải.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Thuyền trưởng BYD cầm lái tàu vận tải trên nền hải đồ toàn cầu phát sáng.
- **[TEXT OVERLAY]:** Không

### CH04_SC036
- **[THOẠI]:** Chỉ duy nhất một nơi trên thế giới dám sử dụng bạo lực pháp lý cực đoan để chặn đứng cỗ máy này: Nước Mỹ.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Tòa nhà Quốc hội Mỹ tại Washington DC sừng sững dưới ánh sáng đỏ chói gay gắt.
- **[TEXT OVERLAY]:** "USA DEFENSIVE WALL"

### CH04_SC037
- **[THOẠI]:** Washington không đàm phán. Họ dựng lên bức tường lửa 100% thuế quan,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bức tường lửa cao vút hiển thị con số "100% TARIFF WALL" ngăn chặn hoàn toàn xe điện Trung Quốc.
- **[TEXT OVERLAY]:** "100% TARIFF WALL"

### CH04_SC038
- **[THOẠI]:** đi kèm Đạo luật An ninh Xe Kết nối, cấm tiệt mọi phần mềm và phần cứng Trung Quốc.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Văn bản "CONNECTED VEHICLE SECURITY ACT" bị đóng dấu BANRED (CẤM) lên toàn bộ vi chip và phần mềm.
- **[TEXT OVERLAY]:** "CONNECTED VEHICLE SECURITY ACT"

### CH04_SC039
- **[THOẠI]:** Mỹ chấp nhận xé bỏ mọi nguyên tắc thương mại tự do để bảo vệ sự tồn vong của ngành công nghiệp ô tô nội địa.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Các biểu tượng của Detroit Ford, GM được bảo vệ phía sau bức tường an ninh quốc gia Mỹ.
- **[TEXT OVERLAY]:** "PROTECTING DETROIT"

### CH04_SC040
- **[THOẠI]:** Nhưng thế giới không phải ai cũng là nước Mỹ.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Quả địa cầu tự quay, ngoại trừ vùng nước Mỹ bị tô đỏ phong tỏa, các khu vực còn lại đều tô xanh mở cửa.
- **[TEXT OVERLAY]:** Không

### CH04_SC041
- **[THOẠI]:** Ở những thị trường mà cỗ máy đó đã thâm nhập sâu rộng,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đường phố Đông Nam Á và Châu Âu ngập tràn những chiếc xe BYD đang lưu thông.
- **[TEXT OVERLAY]:** Không

### CH04_SC042
- **[THOẠI]:** phía sau mức giá siêu rẻ, những hệ lụy chìm bắt đầu xuất hiện.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Chiếc xe BYD nằm trong bãi đỗ với cái bóng đổ dài xuống mặt đường, phát sáng những gợn sóng hệ lụy.
- **[TEXT OVERLAY]:** Không
'''

with open(vis_file, 'w', encoding='utf-8') as f:
    f.write(vis_text)

# 3. Write prompts_chapter_04.txt
prompt_text = '''CH04_SC001 [IMAGE]: Cinematic Editorial Noir, Wide Shot, the grand Berlaymont hall in Brussels, European politicians standing silently under dramatic chiaroscuro lighting, heavy moody atmosphere.
CH04_SC001 [VIDEO]: @CH04_SC001.png -> steady wide shot, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC002 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, a gold-embossed Free Trade Agreement book on a desk bound tightly with heavy iron ropes, "FREE TRADE BOUND" text overlay.
CH04_SC002 [VIDEO]: @CH04_SC002.png -> steady shot on the bound book, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC003 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, complex European political and economic gears jammed and frozen solid, unable to turn.
CH04_SC003 [VIDEO]: @CH04_SC003.png -> steady graphic display, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC004 [IMAGE]: Cinematic Editorial Noir, Medium Shot, WTO Headquarters building in Geneva with glowing flags, in front is the scales of justice representing MFN principles, "WTO MFN PRINCIPLE" text overlay.
CH04_SC004 [VIDEO]: @CH04_SC004.png -> steady shot on the WTO building and scales, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC005 [IMAGE]: Cinematic Editorial Noir, Medium Shot, a BYD Seal undergoing crash test at Euro NCAP lab, 5 glowing golden stars illuminated above it, "EURO NCAP 5-STAR SAFETY" text overlay.
CH04_SC005 [VIDEO]: @CH04_SC005.png -> steady shot on the crash test vehicle, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC006 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, a digital emissions scanner displaying a glowing green "0.00 g/km" reading, "ZERO EMISSION COMPLIANT" text overlay.
CH04_SC006 [VIDEO]: @CH04_SC006.png -> steady shot on the emissions scanner, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC007 [IMAGE]: Cinematic Editorial Noir, Wide Shot, a dark boardroom in Berlin with German government officials in deep tense discussion, somber chiaroscuro lighting, "FEAR OF RETALIATION" text overlay.
CH04_SC007 [VIDEO]: @CH04_SC007.png -> steady wide shot of officials, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC008 [IMAGE]: Cinematic Editorial Noir, Wide Shot, European Commission Berlaymont building in Brussels with flashing window lights under stormy skies.
CH04_SC008 [VIDEO]: @CH04_SC008.png -> steady shot of building exterior, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC009 [IMAGE]: Cinematic Editorial Noir, Low Angle Shot, Ministry of Commerce building in Beijing, silhouette of official giving a stern press statement.
CH04_SC009 [VIDEO]: @CH04_SC009.png -> steady shot on the official, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC010 [IMAGE]: Cinematic Editorial Noir, Wide Shot, a crowded avenue in Shanghai packed with Volkswagen, BMW, and Mercedes cars bearing Chinese license plates, "GERMAN AUTO EXPOSURE IN CHINA" text overlay.
CH04_SC010 [VIDEO]: @CH04_SC010.png -> steady wide shot of traffic, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC011 [IMAGE]: Cinematic Editorial Noir, Wide Shot, French export seaport with thousands of Cognac crates and agricultural goods awaiting shipment to China, "FRENCH AGRICULTURAL EXPORTS" text overlay.
CH04_SC011 [VIDEO]: @CH04_SC011.png -> steady wide shot of port cargo, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC012 [IMAGE]: Cinematic Editorial Noir, Medium Shot, European Parliament corridor split visually into two opposing light beams: green and red, "INTERNAL GOVERNMENT SPLIT" text overlay.
CH04_SC012 [VIDEO]: @CH04_SC012.png -> steady shot of the split corridor, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC013 [IMAGE]: Cinematic Editorial Noir, Medium Shot, Environment Ministry official pointing to Net Zero 2030 target chart next to a $20,000 BYD Dolphin EV, "NET ZERO 2030 TARGET ($20,000 EV)" text overlay.
CH04_SC013 [VIDEO]: @CH04_SC013.png -> steady shot on official, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC014 [IMAGE]: Cinematic Editorial Noir, Medium Shot, Industry Ministry official holding head in hands over reports of declining European automaker revenues, "DOMESTIC INDUSTRY PROTECTION" text overlay.
CH04_SC014 [VIDEO]: @CH04_SC014.png -> steady shot on official, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC015 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, European citizen tightening belt at a supermarket checkout, looking nervously at an inflation bill.
CH04_SC015 [VIDEO]: @CH04_SC015.png -> steady shot on citizen, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC016 [IMAGE]: Cinematic Editorial Noir, Wide Shot, voters holding protest signs outside a BYD dealership objecting to government tariff increases, "VOTER BACKLASH ON TARIFFS" text overlay.
CH04_SC016 [VIDEO]: @CH04_SC016.png -> steady wide shot of protesters, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC017 [IMAGE]: Cinematic Editorial Noir, 3D Map, map of European Union with a glowing red fracture line along the border between Germany and France, "EU MEMBER STATE FRACTURE" text overlay.
CH04_SC017 [VIDEO]: @CH04_SC017.png -> steady map graphic, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC018 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, German delegate in Brussels pressing a red 'VOTE NO' button during EU tariff vote, "GERMANY: VOTE NO ON TARIFFS" text overlay.
CH04_SC018 [VIDEO]: @CH04_SC018.png -> steady shot on button press, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC019 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, French delegate pressing a green 'VOTE YES' button, glaring sternly across at German delegates, "FRANCE: VOTE YES" text overlay.
CH04_SC019 [VIDEO]: @CH04_SC019.png -> steady shot on button press, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC020 [IMAGE]: Cinematic Editorial Noir, Medium Shot, BYD executive smiling and shaking hands with prominent European dealership tycoons in a luxury banquet room.
CH04_SC020 [VIDEO]: @CH04_SC020.png -> steady shot on handshake, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC021 [IMAGE]: Cinematic Editorial Noir, Wide Shot, headquarters building of Hedin Mobility Group in Europe featuring prominent BYD dealership branding, "LOCAL DISTRIBUTOR ALLIANCE" text overlay.
CH04_SC021 [VIDEO]: @CH04_SC021.png -> steady wide shot of building, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC022 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, a glass protective shield labeled with local distributor logo sheltering a BYD vehicle, "LOCAL LEGAL SHIELD" text overlay.
CH04_SC022 [VIDEO]: @CH04_SC022.png -> steady graphic shot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC023 [IMAGE]: Cinematic Editorial Noir, Medium Shot, European legal minister pausing with gavel in hand, looking down at a map of local dealerships.
CH04_SC023 [VIDEO]: @CH04_SC023.png -> steady shot on minister, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC024 [IMAGE]: Cinematic Editorial Noir, Medium Shot, local European car dealership salesperson standing anxiously inside an empty BYD showroom, "LOCAL JOBS AT RISK" text overlay.
CH04_SC024 [VIDEO]: @CH04_SC024.png -> steady shot on salesperson, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC025 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, BYD car maneuverably driving past red administrative tariff barrier gates.
CH04_SC025 [VIDEO]: @CH04_SC025.png -> steady shot of car moving, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC026 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, official EU document stamped in red '17% Anti-Subsidy Duty', "OCT 2024: EU 17% ANTI-SUBSIDY TARIFF" text overlay.
CH04_SC026 [VIDEO]: @CH04_SC026.png -> steady shot on stamped document, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC027 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, calculation showing 10% Base + 17% Anti-Subsidy = 27% Total BEV Tariff, "TOTAL BEV TARIFF: 27%" text overlay.
CH04_SC027 [VIDEO]: @CH04_SC027.png -> steady graphic display, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC028 [IMAGE]: Cinematic Editorial Noir, Medium Shot, BYD Seal U DM-i Super Hybrid (PHEV) gliding past European seaport customs check, "PHEV SUPER HYBRID PUSH" text overlay.
CH04_SC028 [VIDEO]: @CH04_SC028.png -> steady tracking shot of vehicle, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC029 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, tariff table showing 'PHEV IMPORT DUTY: ONLY 10%' glowing green, "PHEV TARIFF: ONLY 10%" text overlay.
CH04_SC029 [VIDEO]: @CH04_SC029.png -> steady graphic shot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC030 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, 'Local Content Requirement' document crushed under a stack of Euro currency notes, "LOCALIZATION BYPASS" text overlay.
CH04_SC030 [VIDEO]: @CH04_SC030.png -> steady shot on crushed document, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC031 [IMAGE]: Cinematic Editorial Noir, Wide Shot, massive BYD factory construction site in Szeged, Hungary with active cranes, "HUNGARY PLANT (€4 BILLION)" text overlay.
CH04_SC031 [VIDEO]: @CH04_SC031.png -> steady wide shot of construction, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC032 [IMAGE]: Cinematic Editorial Noir, Medium Shot, signing ceremony for BYD $1 Billion plant in West Java, Indonesia, "INDONESIA PLANT ($1 BILLION)" text overlay.
CH04_SC032 [VIDEO]: @CH04_SC032.png -> steady shot on signing ceremony, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC033 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, 'MADE IN EUROPE' badge being fitted onto a BYD vehicle at Hungary plant, "MADE IN EUROPE (0% INTRA-EU TARIFF)" text overlay.
CH04_SC033 [VIDEO]: @CH04_SC033.png -> steady shot on badge fitting, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC034 [IMAGE]: Cinematic Editorial Noir, Wide Shot, fleet of 8 massive BYD Ro-Ro transport ships sailing into international ports, "$690M OWNED FLEET" text overlay.
CH04_SC034 [VIDEO]: @CH04_SC034.png -> steady wide tracking shot of fleet, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC035 [IMAGE]: Cinematic Editorial Noir, Medium Shot, BYD captain holding ship wheel overlooking glowing nautical map.
CH04_SC035 [VIDEO]: @CH04_SC035.png -> steady shot on captain, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC036 [IMAGE]: Cinematic Editorial Noir, Wide Shot, US Capitol building in Washington DC glowing under intense crimson light, "USA DEFENSIVE WALL" text overlay.
CH04_SC036 [VIDEO]: @CH04_SC036.png -> steady wide shot of Capitol, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC037 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, towering firewall displaying '100% TARIFF WALL' blocking Chinese EVs completely, "100% TARIFF WALL" text overlay.
CH04_SC037 [VIDEO]: @CH04_SC037.png -> steady graphic shot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC038 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, 'CONNECTED VEHICLE SECURITY ACT' document stamped BANRED over microchips, "CONNECTED VEHICLE SECURITY ACT" text overlay.
CH04_SC038 [VIDEO]: @CH04_SC038.png -> steady shot on stamped document, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC039 [IMAGE]: Cinematic Editorial Noir, Wide Shot, Detroit auto logos Ford and GM protected behind US national security firewall, "PROTECTING DETROIT" text overlay.
CH04_SC039 [VIDEO]: @CH04_SC039.png -> steady shot on logos, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH04_SC040 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, rotating globe with USA shaded red (blocked) while all other regions are shaded green (open).
CH04_SC040 [VIDEO]: @CH04_SC040.png -> steady globe graphic, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC041 [IMAGE]: Cinematic Editorial Noir, Wide Shot, European and Southeast Asian city streets crowded with BYD vehicles driving.
CH04_SC041 [VIDEO]: @CH04_SC041.png -> steady wide shot of traffic, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH04_SC042 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, parked BYD car casting a long shadow with glowing ripples of hidden consequences underneath.
CH04_SC042 [VIDEO]: @CH04_SC042.png -> steady shot on parked car, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9
'''

with open(prompt_file, 'w', encoding='utf-8') as f:
    f.write(prompt_text)

print("CHAPTER 4 FULL REGEN COMPLETE! Total scenes: 42.")
