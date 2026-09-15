import os
import re

base_dir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/byd-co-may-hoan-hao-2'
ch1_file = os.path.join(base_dir, 'chapter_01.md')
vis_file = os.path.join(base_dir, 'chapter_01_visual.md')
prompt_file = os.path.join(base_dir, 'prompts_chapter_01.txt')

# 1. Update chapter_01.md
new_ch1_content = '''# chapter_01.md

"Chúng tôi sẽ vượt Toyota trong năm năm. Và chúng tôi không cần thị trường Mỹ." Đó là lời Phó Chủ tịch B Y D, bà Stella Li, tuyên bố trước hàng trăm nhà đầu tư tại Hội nghị Ô tô hai nghìn không trăm hai mươi sáu. Tự tin. Dõng dạc. Như thể tương lai đã được viết sẵn.

Và nếu chỉ nhìn vào năng lực sản xuất, lời tuyên bố đó không hề vô căn cứ. B Y D sản xuất bốn phẩy sáu triệu xe năm hai nghìn không trăm hai mươi lăm, nhiều hơn bất kỳ hãng xe điện nào trên hành tinh. Tự chế tạo bảy mươi lăm phần trăm linh kiện, từ viên pin Blade đến chip công suất I G B T, thứ được gọi là bộ não năng lượng của xe điện. Ngân hàng Thụy Sĩ U B S từng tháo tung một chiếc xe B Y D ra để nghiên cứu và đưa ra kết luận chấn động: Nếu cùng sản xuất một mẫu xe, chi phí chế tạo của B Y D sẽ rẻ hơn Tesla mười lăm phần trăm, và rẻ hơn Volkswagen tới ba mươi lăm phần trăm.

Tự đóng cả tàu biển chở xe riêng, sức chứa chín nghìn hai trăm chiếc mỗi chuyến. Không thuê ai. Không phụ thuộc ai.

Trên giấy tờ, đây là cỗ máy hoàn hảo.

Nhưng quý một năm hai nghìn không trăm hai mươi sáu, bức tranh tài chính kể một câu chuyện khác.

Nợ ngắn hạn của B Y D nhảy lên chín phẩy một tỷ đô, tăng bảy mươi hai phần trăm chỉ trong một quý. Đây không phải sự cố nhất thời. Năm hai nghìn không trăm hai mươi tư, con số đó là hai tỷ. Năm hai nghìn không trăm hai mươi lăm, nhảy lên năm phẩy ba tỷ. Bây giờ, chín phẩy một tỷ. Một đường cong tăng tốc, không phải dao động theo mùa. Hối phiếu phải trả tăng một trăm mười sáu phần trăm, lên gần sáu phẩy bảy tỷ đô. Thâm hụt vốn lưu động vượt ngưỡng mười sáu tỷ đô.

Lợi nhuận ròng bốc hơi năm mươi lăm phần trăm, chỉ còn năm trăm sáu mươi ba triệu đô trên doanh thu hơn hai mươi tỷ đô. Hàng tồn kho chất đống hai mươi hai tỷ đô, xe nằm bãi trung bình bảy mươi hai ngày trước khi tìm được người mua. Dòng tiền hoạt động sụt giảm gần sáu mươi tám phần trăm.

Có người sẽ nói: B Y D vẫn có mười bốn đến mười lăm tỷ đô tiền mặt trong két. Vẫn dương dòng tiền. Điều đó đúng. Nhưng dòng tiền dương đó đang teo lại với tốc độ sáu mươi tám phần trăm mỗi quý, trong khi nợ ngắn hạn tăng bảy mươi hai phần trăm. Hai đường cong này, nếu tiếp tục, sẽ cắt nhau trong vòng vài quý tới.

Tại đại hội cổ đông tháng sáu năm hai nghìn không trăm hai mươi sáu, một nhà đầu tư đã bật khóc khi chứng kiến giá cổ phiếu bốc hơi gần một nửa. Đối diện sự phẫn nộ, Chủ tịch Wang Chuanfu thẳng thắn gọi đây là "thời khắc đen tối nhất" khi trợ cấp nội địa bị cắt giảm.

Nhưng ngay sau đó, ông vẫn khẳng định B Y D sẽ vượt Toyota trong năm năm tới. Nghe có vẻ mâu thuẫn: Làm sao một cỗ máy đang chảy máu tài chính lại đòi chiếm ngôi vương thế giới?

Câu trả lời nằm ở áp lực sinh tồn. Với khối tồn kho hai mươi hai tỷ đô và khoản nợ chín tỷ đô đang đè nặng, B Y D không thể dừng nhà máy. Lối thoát duy nhất để tự cứu mình là phải đẩy hàng triệu chiếc xe thừa tràn ra thị trường quốc tế. Tuyên bố vượt Toyota, thực chất, chính là mệnh lệnh bắt buộc phải bành trướng ra toàn cầu để tìm dòng tiền.

Câu hỏi là: điều gì bên trong cỗ máy đó đang gãy? Và những nước nào sẽ phải chịu hệ lụy khi dòng nước này tràn đến?

Đây là Góc Nhìn Podcast. Và hôm nay, chúng ta sẽ mổ xẻ cỗ máy sản xuất xe điện lớn nhất hành tinh, từ cơ chế tài chính ẩn khiến nó rẻ bất thường, đến lý do vì sao nó đang bị xua đuổi khắp nơi, và liệu bức tường phòng thủ tại Việt Nam có đủ vững.
'''

with open(ch1_file, 'w', encoding='utf-8') as f:
    f.write(new_ch1_content)

# 2. Update chapter_01_visual.md
new_vis_content = '''# chapter_01_visual.md

### CH01_SC001
- **[THOẠI]:** "Chúng tôi sẽ vượt Toyota trong 5 năm. Và chúng tôi không cần thị trường Mỹ."
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hội nghị Ô tô. Cận cảnh Stella Li đứng trên bục phát biểu, ánh sáng spotlight chiếu rọi. Bà giơ tay chỉ thẳng về phía trước đầy tự tin. Phía sau là bóng tối (Deep Noir).
- **[TEXT OVERLAY]:** "BEAT TOYOTA IN 5 YEARS"

### CH01_SC002
- **[THOẠI]:** Đó là lời Phó Chủ tịch BYD, bà Stella Li, tuyên bố trước hàng trăm nhà đầu tư tại Hội nghị Ô tô 2026.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Góc máy rộng (Wide shot) nhìn từ sau lưng khán giả hướng lên sân khấu. Hàng trăm nhà đầu tư ngồi dưới hội trường tối, hướng mắt về bóng hình Stella Li tỏa sáng trên bục.
- **[TEXT OVERLAY]:** Không

### CH01_SC003
- **[THOẠI]:** Tự tin. Dõng dạc. Như thể tương lai đã được viết sẵn.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Stella Li mỉm cười tự tin, bước lùi lại khi màn hình lớn phía sau hiển thị logo BYD phát sáng mạ vàng cứng cáp.
- **[TEXT OVERLAY]:** Không

### CH01_SC004
- **[THOẠI]:** Và nếu chỉ nhìn vào năng lực sản xuất, lời tuyên bố đó không hề vô căn cứ.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Toàn cảnh nhà máy lắp ráp BYD hoạt động hết công suất. Hàng nghìn cánh tay robot hàn tia lửa điện chính xác.
- **[TEXT OVERLAY]:** Không

### CH01_SC005
- **[THOẠI]:** BYD sản xuất 4,6 triệu xe năm 2025, nhiều hơn bất kỳ hãng xe điện nào trên hành tinh.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bãi chứa xe thành phẩm rộng mênh mông kéo dài đến tận chân trời, hàng vạn chiếc xe mới tinh xếp hàng thẳng tắp.
- **[TEXT OVERLAY]:** "4.6 MILLION VEHICLES"

### CH01_SC006
- **[THOẠI]:** Tự chế tạo 75% linh kiện, từ viên pin Blade đến chip công suất IGBT, thứ được gọi là bộ não năng lượng của xe điện.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cận cảnh một viên pin Blade mỏng như lưỡi kiếm được lắp vào bộ khung gầm xe, các vi mạch điện tử phát sáng luồng dữ liệu xanh lục.
- **[TEXT OVERLAY]:** "75% IN-HOUSE COMPONENTS"

### CH01_SC007
- **[THOẠI]:** Ngân hàng Thụy Sĩ UBS từng tháo tung một chiếc xe BYD ra để nghiên cứu và đưa ra kết luận chấn động:
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Kỹ sư của UBS mặc áo blouse trắng đứng trong phòng thí nghiệm hiện đại, xung quanh là chiếc xe BYD Seal đã bị tháo rải rác từng linh kiện ra bàn.
- **[TEXT OVERLAY]:** "UBS TEARDOWN REPORT"

### CH01_SC008
- **[THOẠI]:** Nếu cùng sản xuất một mẫu xe, chi phí chế tạo của BYD sẽ rẻ hơn Tesla 15%, và rẻ hơn Volkswagen tới 35%.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đồ họa 3D hiển thị 3 cột chi phí sản xuất: Cột BYD thấp nhất phát sáng xanh, cột Tesla cao hơn 15%, cột VW cao hơn 35%.
- **[TEXT OVERLAY]:** "-15% VS TESLA | -35% VS VW"

### CH01_SC009
- **[THOẠI]:** Tự đóng cả tàu biển chở xe riêng, sức chứa 9.200 chiếc mỗi chuyến.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Con tàu vận tải khổng lồ mang tên BYD EXPLORER 01 đang rẽ sóng trên biển khơi, boong tàu chất đầy hàng ngàn xe điện.
- **[TEXT OVERLAY]:** "9,200 CARS / SHIP"

### CH01_SC010
- **[THOẠI]:** Không thuê ai. Không phụ thuộc ai.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cần cẩu khổng lồ cẩu nốt container cuối cùng mang logo BYD lên boong tàu. Không có bất kỳ logo của công ty vận tải ngoài nào xuất hiện ở cảng.
- **[TEXT OVERLAY]:** Không

### CH01_SC011
- **[THOẠI]:** Trên giấy tờ, đây là cỗ máy hoàn hảo.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Tập hồ sơ báo cáo thường niên đóng bìa cứng hoàn hảo, phẳng phiu, nằm trên chiếc bàn gỗ lớn trong phòng họp vắng người.
- **[TEXT OVERLAY]:** Không

### CH01_SC012
- **[THOẠI]:** Nhưng quý 1 năm 2026, bức tranh tài chính kể một câu chuyện khác.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Tập hồ sơ báo cáo tài chính trên bàn bắt đầu xuất hiện những vết nứt phát sáng màu đỏ máu dọc theo các trang giấy.
- **[TEXT OVERLAY]:** "Q1 2026 FINANCIAL REALITY"

### CH01_SC013
- **[THOẠI]:** Nợ ngắn hạn của BYD nhảy lên 9,1 tỷ đô, tăng 72% chỉ trong một quý.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Biểu đồ cột nợ ngắn hạn tăng dựng đứng từ 2 tỷ (2024) lên 5,3 tỷ (2025) và vọt lên 9,1 tỷ (Q1 2026) với ánh đỏ cảnh báo.
- **[TEXT OVERLAY]:** "$9.1B SHORT-TERM DEBT (+72%)"

### CH01_SC014
- **[THOẠI]:** Đây không phải sự cố nhất thời. Năm 2024, con số đó là 2 tỷ. Năm 2025, nhảy lên 5,3 tỷ. Bây giờ, 9,1 tỷ.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Một đường cong màu đỏ rực lao lên dốc đứng xuyên qua các mốc thời gian trên bảng điện tử tài chính.
- **[TEXT OVERLAY]:** Không

### CH01_SC015
- **[THOẠI]:** Một đường cong tăng tốc, không phải dao động theo mùa.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đường cong nợ cắt ngang qua các vạch giới hạn an toàn màu trắng, biến toàn bộ màn hình thành màu đỏ rực.
- **[TEXT OVERLAY]:** Không

### CH01_SC016
- **[THOẠI]:** Hối phiếu phải trả tăng 116%, lên gần 6,7 tỷ đô. Thâm hụt vốn lưu động vượt ngưỡng 16 tỷ đô.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đập nước bằng bê tông tích tụ hàng núi hối phiếu tài chính đang căng đét, xuất hiện các nứt nẻ rò rỉ nước áp lực cao.
- **[TEXT OVERLAY]:** "PAYABLE NOTES: $6.7B | WORKING CAPITAL DEFICIT: $16B"

### CH01_SC017
- **[THOẠI]:** Lợi nhuận ròng bốc hơi 55%, chỉ còn 563 triệu đô trên doanh thu hơn 20 tỷ đô.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cột lợi nhuận ròng màu xanh bị gọt lẹm hơn một nửa, biến thành một vạch mỏng dính màu xám dưới chân cột doanh thu khổng lồ.
- **[TEXT OVERLAY]:** "NET PROFIT -55% ($563M / $20B REV)"

### CH01_SC018
- **[THOẠI]:** Hàng tồn kho chất đống 22 tỷ đô, xe nằm bãi trung bình 72 ngày trước khi tìm được người mua.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bãi xe tồn kho khổng lồ dưới trời mưa xám xịt, đồng hồ cát rải rác trên các nóc xe với cát chảy chậm chạp ghi số 72 ngày.
- **[TEXT OVERLAY]:** "INVENTORY: $22B | 72 DAYS ON LOT"

### CH01_SC019
- **[THOẠI]:** Dòng tiền hoạt động sụt giảm gần 68%.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Dòng nước tài chính đang chảy cuồn cuộn qua đường ống bỗng nhiên bị thu hẹp lại thành một dòng chảy nhỏ giọt yếu ớt.
- **[TEXT OVERLAY]:** "OPERATING CASH FLOW -68%"

### CH01_SC020
- **[THOẠI]:** Có người sẽ nói: BYD vẫn có 14 đến 15 tỷ đô tiền mặt trong két. Vẫn dương dòng tiền. Điều đó đúng.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Két sắt ngân hàng khổng lồ mở ra hiển thị các cọc tiền USD xếp chồng cao ngất, phát sáng ánh vàng an toàn.
- **[TEXT OVERLAY]:** "CASH RESERVES: $14B-$15B"

### CH01_SC021
- **[THOẠI]:** Nhưng dòng tiền dương đó đang teo lại với tốc độ 68% mỗi quý, trong khi nợ ngắn hạn tăng 72%.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hai đường biểu đồ: Đường dòng tiền xanh dương đang cắm đầu xuống, đường nợ ngắn hạn màu đỏ đang lao ngược lên.
- **[TEXT OVERLAY]:** Không

### CH01_SC022
- **[THOẠI]:** Hai đường cong này, nếu tiếp tục, sẽ cắt nhau trong vòng vài quý tới.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hai đường cong màu đỏ và xanh giao nhau tạo thành một dấu X phát sáng đỏ chói, báo hiệu điểm bùng nổ khủng hoảng.
- **[TEXT OVERLAY]:** "CRITICAL CROSSOVER POINT"

### CH01_SC023
- **[THOẠI]:** Tại đại hội cổ đông tháng 6 năm 2026, một nhà đầu tư đã bật khóc khi chứng kiến giá cổ phiếu bốc hơi gần một nửa.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cận cảnh một nhà đầu tư tháo kính lau nước mắt trước màn hình bảng điện tử hiển thị chỉ số cổ phiếu BYD lao dốc -45%.
- **[TEXT OVERLAY]:** "-45% STOCK VALUE"

### CH01_SC024
- **[THOẠI]:** Đối diện sự phẫn nộ, Chủ tịch Wang Chuanfu thẳng thắn gọi đây là "thời khắc đen tối nhất" khi trợ cấp nội địa bị cắt giảm.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Wang Chuanfu đứng trên bục phát biểu, sắc mặt trầm lặng trong ánh sáng Noir, micro thu âm phát ra tiếng thở dài kiên định.
- **[TEXT OVERLAY]:** "THE DARKEST HOUR"

### CH01_SC025
- **[THOẠI]:** Nhưng ngay sau đó, ông vẫn khẳng định BYD sẽ vượt Toyota trong 5 năm tới.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Wang Chuanfu giơ tay chỉ thẳng về phía trước, đằng sau màn hình chuyển sang bản đồ thế giới màu xanh lục với tham vọng vượt Toyota.
- **[TEXT OVERLAY]:** "OVERTAKE TOYOTA BY 2030"

### CH01_SC026
- **[THOẠI]:** Nghe có vẻ mâu thuẫn: Làm sao một cỗ máy đang chảy máu tài chính lại đòi chiếm ngôi vương thế giới?
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hai nửa màn hình: Một bên là nợ nần chảy máu màu đỏ, một bên là chiếc vương miện Toyota. Một dấu hỏi chấm lớn hiện lên ở giữa.
- **[TEXT OVERLAY]:** "THE PARADOX"

### CH01_SC027
- **[THOẠI]:** Câu trả lời nằm ở áp lực sinh tồn. Với khối tồn kho 22 tỷ đô và khoản nợ 9 tỷ đô đang đè nặng, BYD không thể dừng nhà máy.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Toàn cảnh bãi xe tồn kho 22 tỷ đô nghẹt thở, các bánh răng nhà máy vẫn quay xối xả không thể dừng lại.
- **[TEXT OVERLAY]:** "$22B INVENTORY / $9B DEBT"

### CH01_SC028
- **[THOẠI]:** Lối thoát duy nhất để tự cứu mình là phải đẩy hàng triệu chiếc xe thừa tràn ra thị trường quốc tế.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hàng dài xe BYD rầm rộ chạy lên các tàu vận tải biển khổng lồ đang chờ sẵn tại cảng xuất khẩu.
- **[TEXT OVERLAY]:** Không

### CH01_SC029
- **[THOẠI]:** Tuyên bố vượt Toyota, thực chất, chính là mệnh lệnh bắt buộc phải bành trướng ra toàn cầu để tìm dòng tiền.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Bản đồ thế giới xuất hiện các luồng mũi tên màu đỏ tỏa ra từ Trung Quốc đánh chiếm các thị trường Đông Nam Á, Châu Âu, Nam Mỹ.
- **[TEXT OVERLAY]:** "GLOBAL EXPANSION MANDATE"

### CH01_SC030
- **[THOẠI]:** Câu hỏi là: điều gì bên trong cỗ máy đó đang gãy? Và những nước nào sẽ phải chịu hệ lụy khi dòng nước này tràn đến?
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Mô hình 3D cỗ máy BYD phát sáng rạn nứt từ bên trong, luồng sóng đỏ tràn qua bản đồ các quốc gia láng giềng.
- **[TEXT OVERLAY]:** Không

### CH01_SC031
- **[THOẠI]:** Đây là Góc Nhìn Podcast. Và hôm nay, chúng ta sẽ mổ xẻ cỗ máy sản xuất xe điện lớn nhất hành tinh,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Màn hình hiển thị biểu tượng Góc Nhìn Podcast phát sáng mạ đồng trên nền nhung đen sâu thẩm (Deep Noir).
- **[TEXT OVERLAY]:** "GOC NHIN PODCAST"

### CH01_SC032
- **[THOẠI]:** từ cơ chế tài chính ẩn khiến nó rẻ bất thường, đến lý do vì sao nó đang bị xua đuổi khắp nơi, và liệu bức tường phòng thủ tại Việt Nam có đủ vững.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Đồ họa 3 lá chắn: Cơ chế tài chính, Bức tường bảo hộ quốc tế, và Bản đồ Việt Nam phát sáng kiên cố.
- **[TEXT OVERLAY]:** "BYD: THE UNSTOPPABLE MACHINE?"
'''

with open(vis_file, 'w', encoding='utf-8') as f:
    f.write(new_vis_content)

# 3. Update prompts_chapter_01.txt
new_prompts_content = '''CH01_SC001 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, Stella Li standing at a podium under a bright spotlight, pointing forward with supreme confidence, dark shadows surrounding the stage, "BEAT TOYOTA IN 5 YEARS" text overlay.
CH01_SC001 [VIDEO]: @CH01_SC001.png -> steady shot on Stella Li, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC002 [IMAGE]: Cinematic Editorial Noir, Wide Shot, viewed from behind the dark auditorium audience looking up at Stella Li shining on stage at the 2026 Auto Conference.
CH01_SC002 [VIDEO]: @CH01_SC002.png -> steady wide shot, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC003 [IMAGE]: Cinematic Editorial Noir, Medium Shot, Stella Li smiling confidently as a massive golden BYD logo glows on the screen behind her.
CH01_SC003 [VIDEO]: @CH01_SC003.png -> slow push in on Stella Li, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC004 [IMAGE]: Cinematic Editorial Noir, Wide Shot, a bustling automated BYD assembly plant operating at maximum capacity with robotic arms sparking precise welds.
CH01_SC004 [VIDEO]: @CH01_SC004.png -> slow panning shot across the factory floor, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC005 [IMAGE]: Cinematic Editorial Noir, High Angle Wide Shot, a vast parking lot of finished new BYD electric vehicles stretching to the horizon, "4.6 MILLION VEHICLES" text overlay.
CH01_SC005 [VIDEO]: @CH01_SC005.png -> steady wide shot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC006 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, a ultra-thin Blade Battery being installed into a car chassis, green data circuits glowing, "75% IN-HOUSE COMPONENTS" text overlay.
CH01_SC006 [VIDEO]: @CH01_SC006.png -> steady shot on the battery insertion, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC007 [IMAGE]: Cinematic Editorial Noir, Medium Shot, UBS engineers in white lab coats dismantling a BYD Seal car into individual parts on tables, "UBS TEARDOWN REPORT" text overlay.
CH01_SC007 [VIDEO]: @CH01_SC007.png -> steady shot on engineers inspecting components, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC008 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, 3 cost pillars comparing BYD (lowest, green glow), Tesla (+15%), and Volkswagen (+35%), "-15% VS TESLA | -35% VS VW" text overlay.
CH01_SC008 [VIDEO]: @CH01_SC008.png -> steady graphic display, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC009 [IMAGE]: Cinematic Editorial Noir, Wide Shot, colossal cargo vessel 'BYD EXPLORER 01' slicing through ocean waves loaded with thousands of EV cars, "9,200 CARS / SHIP" text overlay.
CH01_SC009 [VIDEO]: @CH01_SC009.png -> steady tracking shot of ship, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC010 [IMAGE]: Cinematic Editorial Noir, Medium Shot, massive harbor crane lifting a BYD container onto a ship, pristine port with zero third-party logistics logos.
CH01_SC010 [VIDEO]: @CH01_SC010.png -> steady shot of crane lowering container, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC011 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, an immaculate leather-bound annual financial report resting on a polished dark mahogany boardroom table.
CH01_SC011 [VIDEO]: @CH01_SC011.png -> slow push in on report, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC012 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, financial document on table developing glowing red cracks along its pages, "Q1 2026 FINANCIAL REALITY" text overlay.
CH01_SC012 [VIDEO]: @CH01_SC012.png -> steady shot on cracking document, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC013 [IMAGE]: Cinematic Editorial Noir, 3D Financial Chart, short term debt spiking up to 9.1B USD in red glow, "$9.1B SHORT-TERM DEBT (+72%)" text overlay.
CH01_SC013 [VIDEO]: @CH01_SC013.png -> steady chart display, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC014 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, steep red trend line rushing upwards through timestamps 2024 (2B), 2025 (5.3B), and 2026 (9.1B).
CH01_SC014 [VIDEO]: @CH01_SC014.png -> steady graphic shot, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC015 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, red debt curve crossing white safety threshold lines turning the whole screen crimson.
CH01_SC015 [VIDEO]: @CH01_SC015.png -> steady graphic shot, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC016 [IMAGE]: Cinematic Editorial Noir, Visual Metaphor, a concrete dam buckling under a mountain of financial notes with high pressure water leaking out, "PAYABLE NOTES: $6.7B | WORKING CAPITAL DEFICIT: $16B" text overlay.
CH01_SC016 [VIDEO]: @CH01_SC016.png -> steady shot on cracking dam, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC017 [IMAGE]: Cinematic Editorial Noir, 3D Chart, net profit column shrinking by 55% to a sliver under a massive 20B revenue pillar, "NET PROFIT -55% ($563M / $20B REV)" text overlay.
CH01_SC017 [VIDEO]: @CH01_SC017.png -> steady graphic shot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC018 [IMAGE]: Cinematic Editorial Noir, Wide Shot, vast vehicle storage lot under gray rain, hourglasses resting on car roofs showing '72 DAYS', "INVENTORY: $22B | 72 DAYS ON LOT" text overlay.
CH01_SC018 [VIDEO]: @CH01_SC018.png -> steady shot on rain-soaked lot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC019 [IMAGE]: Cinematic Editorial Noir, Visual Metaphor, a thick pipe of cash flow constricting into a weak trickle, "OPERATING CASH FLOW -68%" text overlay.
CH01_SC019 [VIDEO]: @CH01_SC019.png -> steady shot on pipe, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC020 [IMAGE]: Cinematic Editorial Noir, Medium Shot, massive bank vault opening to reveal stacks of gold-glowing US dollar cash, "CASH RESERVES: $14B-$15B" text overlay.
CH01_SC020 [VIDEO]: @CH01_SC020.png -> slow dolly in on cash vault, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC021 [IMAGE]: Cinematic Editorial Noir, 3D Graph, blue cash flow curve falling fast while red debt curve climbs sharply.
CH01_SC021 [VIDEO]: @CH01_SC021.png -> steady graphic display, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC022 [IMAGE]: Cinematic Editorial Noir, 3D Graph, red and blue curves intersecting into a glowing red X mark, "CRITICAL CROSSOVER POINT" text overlay.
CH01_SC022 [VIDEO]: @CH01_SC022.png -> steady graphic shot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC023 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, middle-aged male investor taking off glasses to wipe tears in front of a stock ticker showing BYD down -45%, "-45% STOCK VALUE" text overlay.
CH01_SC023 [VIDEO]: @CH01_SC023.png -> steady shot on investor, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC024 [IMAGE]: Cinematic Editorial Noir, Low Angle Shot, Wang Chuanfu speaking at podium with sombre expression under dark chiaroscuro lighting, "THE DARKEST HOUR" text overlay.
CH01_SC024 [VIDEO]: @CH01_SC024.png -> steady shot on Wang Chuanfu, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC025 [IMAGE]: Cinematic Editorial Noir, Medium Shot, Wang Chuanfu pointing forward decisively, background screen shifting to a glowing blue world map, "OVERTAKE TOYOTA BY 2030" text overlay.
CH01_SC025 [VIDEO]: @CH01_SC025.png -> steady shot on Wang Chuanfu, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC026 [IMAGE]: Cinematic Editorial Noir, Split Screen Graphic, left side bleeding red debt, right side Toyota crown, big glowing question mark in the center, "THE PARADOX" text overlay.
CH01_SC026 [VIDEO]: @CH01_SC026.png -> steady graphic display, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC027 [IMAGE]: Cinematic Editorial Noir, High Angle Wide Shot, suffocating 22B inventory lot with factory gears churning relentlessly in background, "$22B INVENTORY / $9B DEBT" text overlay.
CH01_SC027 [VIDEO]: @CH01_SC027.png -> steady wide shot, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC028 [IMAGE]: Cinematic Editorial Noir, Wide Shot, endless line of BYD cars driving onto colossal ocean Ro-Ro transport ships at twilight seaport.
CH01_SC028 [VIDEO]: @CH01_SC028.png -> steady wide shot of cars boarding ship, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC029 [IMAGE]: Cinematic Editorial Noir, 3D Map, global map showing glowing red arrows expanding from China into Southeast Asia, Europe, and Latin America, "GLOBAL EXPANSION MANDATE" text overlay.
CH01_SC029 [VIDEO]: @CH01_SC029.png -> steady map graphic display, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC030 [IMAGE]: Cinematic Editorial Noir, 3D Model, BYD machine cracking from within, emitting red shockwaves spilling over neighboring country maps.
CH01_SC030 [VIDEO]: @CH01_SC030.png -> steady shot on cracking machine, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC031 [IMAGE]: Cinematic Editorial Noir, Logo Shot, glowing metallic copper Goc Nhin Podcast logo on a deep dark velvet background, "GOC NHIN PODCAST" text overlay.
CH01_SC031 [VIDEO]: @CH01_SC031.png -> steady logo display, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC032 [IMAGE]: Cinematic Editorial Noir, 3D Graphic, three glowing shields representing Financial Mechanics, Global Tariffs, and Vietnam Defensive Wall, "BYD: THE UNSTOPPABLE MACHINE?" text overlay.
CH01_SC032 [VIDEO]: @CH01_SC032.png -> steady graphic display, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9
'''

with open(prompt_file, 'w', encoding='utf-8') as f:
    f.write(new_prompts_content)

print("PARADOX FIX COMPLETE!")
