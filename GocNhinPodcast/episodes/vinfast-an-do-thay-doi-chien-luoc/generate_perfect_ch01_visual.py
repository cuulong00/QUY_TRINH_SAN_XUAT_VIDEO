# -*- coding: utf-8 -*-
import json
import os

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'

ch01_matrix = [
    {
        "id": "SC001",
        "dur": 6.3,
        "words": 24,
        "text": "Trong giới sản xuất ô tô toàn cầu, thị trường Ấn Độ từ lâu đã được ví như một chiếc cối xay khổng lồ.",
        "t1": "Phân xưởng dập cơ khí công nghiệp ô tô Ấn Độ chìm trong không gian noir u tối.",
        "t2": "Cỗ máy dập khổng lồ với các bánh răng thép hạng nặng quay chậm rãi, tia lửa cam lóe sáng giữa các khớp răng thép lạnh lẽo.",
        "t3": "Cú máy đẩy chậm đầy kịch tính vào hệ bánh răng cơ khí (Slow dramatic push-in shot), ánh sáng chiaroscuro tương phản cao.",
        "overlay": "Không"
    },
    {
        "id": "SC002",
        "dur": 3.67,
        "words": 14,
        "text": "Đó là nơi bức tường thuế quan trừng phạt từ bảy mươi đến hơn",
        "t1": "Không gian hải quan biên giới kinh tế với bức tường đá hoa cương sừng sững.",
        "t2": "Bức tường thuế quan khổng lồ đổ bóng đen dày đặc xuống sàn nhà xưởng, biểu thị mức thuế trừng phạt nghiệt ngã.",
        "t3": "Cú máy tĩnh trực diện (Steady camera shot) tập trung vào bức tường đá uy nghi và dòng chữ nổi bật.",
        "overlay": "\"THUẾ QUAN 70% - 100%\""
    },
    {
        "id": "SC003",
        "dur": 3.67,
        "words": 14,
        "text": "một trăm phần trăm từng nghiền nát tham vọng của Ford hay General Motors.",
        "t1": "Chân bức tường thuế quan trong góc tối nhà máy bị bỏ hoang.",
        "t2": "Những chiếc xe sedan cổ điển của Ford và General Motors bị phủ bạt bám bụi dày, nằm bất động như những chứng tích thất bại.",
        "t3": "Cú máy trượt ngang chậm sang phải (Slow horizontal tracking pan), bắt trọn đường nét hoang tàn của những chiếc xe bị phủ bạt.",
        "overlay": "Không"
    },
    {
        "id": "SC004",
        "dur": 4.72,
        "words": 18,
        "text": "Tại đây, nhập khẩu xe nguyên chiếc là con đường ngắn nhất dẫn đến cái chết thương mại.",
        "t1": "Khu bến cảng công nghiệp nhập khẩu ô tô với bầu trời xám xịt.",
        "t2": "Các thùng container ô tô nguyên chiếc (CBU) bị quấn xích sắt đỏ niêm phong chặt, phản ánh cái chết thương mại của xe nhập khẩu.",
        "t3": "Cú máy zoom cận cảnh chậm rãi vào ổ khóa xích sắt (Slow subtle zoom-in), toát lên sự bế tắc kinh tế.",
        "overlay": "Không"
    },
    {
        "id": "SC005",
        "dur": 5.77,
        "words": 22,
        "text": "Để thu hút các hãng xe điện toàn cầu, New Delhi vừa mở ra một cánh cửa ưu đãi đầy hấp dẫn",
        "t1": "Cổng vòm đá sa thạch uy nghiêm của cơ quan chính phủ New Delhi.",
        "t2": "Cánh cổng chính sách mở hé, một luồng ánh sáng vàng ấm rọi qua khe cửa vào bóng tối của thị trường ô tô.",
        "t3": "Cú máy lướt tới chậm rãi về phía khe cửa ánh sáng (Slow forward camera glide), mở ra kỳ vọng chính sách mới.",
        "overlay": "Không"
    },
    {
        "id": "SC006",
        "dur": 3.41,
        "words": 13,
        "text": "Cho phép hạ thuế nhập khẩu xuống mức sàn mười lăm phần trăm",
        "t1": "Bàn thẩm định thuế của Bộ Tài chính Ấn Độ trong phòng họp gỗ tối.",
        "t2": "Văn bản nghị định ưu đãi thuế được đóng dấu ấn đỏ pháp lý, cho phép hạ thuế nhập khẩu xuống mức sàn mười lăm phần trăm.",
        "t3": "Cú máy tĩnh khóa chặt văn bản pháp lý (Steady decree shot), thể hiện cánh cửa ưu đãi hấp dẫn.",
        "overlay": "\"ƯU ĐÃI THUẾ: 15%\""
    },
    {
        "id": "SC007",
        "dur": 3.67,
        "words": 14,
        "text": "cho những ai cam kết đầu tư tối thiểu năm trăm triệu đô la.",
        "t1": "Phòng hội nghị chính sách công nghiệp New Delhi.",
        "t2": "Văn bản hiệp định đầu tư chính thức với cam kết rót vốn tối thiểu 500 triệu đô la được chiếu sáng dưới đèn rọi.",
        "t3": "Cú máy tĩnh cận cảnh hồ sơ thỏa thuận (Steady macro document shot), nhấn mạnh cam kết tài chính lớn.",
        "overlay": "\"CAM KẾT: 500 TRIỆU USD\""
    },
    {
        "id": "SC008",
        "dur": 4.46,
        "words": 17,
        "text": "Nhưng cánh cửa ưu đãi thuế ấy đi kèm một chiếc thòng lọng thể chế khắc nghiệt.",
        "t1": "Không gian bàn đàm phán thể chế với bóng đen của các khung cửa sổ sắt.",
        "t2": "Hình tượng sợi dây cáp thép thắt nút thể chế bao quanh tập hồ sơ điều kiện nội địa hóa, tạo cảm giác áp lực pháp lý siết chặt.",
        "t3": "Cú máy lùi chậm (Subtle slow zoom-out) làm lộ rõ sợi cáp thép căng cứng cuốn quanh chồng tài liệu quy hoạch.",
        "overlay": "Không"
    },
    {
        "id": "SC009",
        "dur": 6.56,
        "words": 25,
        "text": "Để giữ được mức thuế ưu đãi, hãng xe bắt buộc phải cam kết một lộ trình nội địa hóa gắt gao theo thời gian.",
        "t1": "Bảng kiểm toán kỹ thuật trên tường phòng điều hành.",
        "t2": "Biểu đồ cột chỉ tiêu tỷ lệ nội địa hóa tăng gắt gao theo từng năm với các vạch kiểm toán đỏ nghiêm ngặt của chính phủ Ấn Độ.",
        "t3": "Cú máy nghiêng góc ngước nhìn lên (Slow upward tilt), nhấn mạnh độ dốc khắc nghiệt của lộ trình nội địa hóa.",
        "overlay": "Không"
    },
    {
        "id": "SC010",
        "dur": 4.99,
        "words": 19,
        "text": "Nếu không đạt chuẩn, toàn bộ số thuế ưu đãi sẽ bị chính phủ truy thu không thương tiếc.",
        "t1": "Kho lưu trữ hồ sơ thanh tra thuế với chiếc két sắt nặng nề bằng sắt đúc.",
        "t2": "Két sắt mở hé để lộ lệnh truy thu thuế toàn bộ kèm theo con dấu niêm phong màu đỏ thẫm của chính phủ Ấn Độ.",
        "t3": "Cú máy tĩnh trực diện vào cánh cửa két sắt và lệnh chế tài (Steady audit safe shot), cảnh báo rủi ro sống còn.",
        "overlay": "\"TRUY THU THUẾ TOÀN BỘ\""
    },
    {
        "id": "SC011",
        "dur": 6.3,
        "words": 24,
        "text": "Nội địa hóa tại Ấn Độ vì thế không phải là việc thích thì làm, mà là một mệnh lệnh pháp lý sống còn.",
        "t1": "Bàn làm việc pháp lý của cố vấn thể chế độc lập.",
        "t2": "Chiếc cán cân công lý bằng đồng thau đặt trên bàn: Một bên là quyền lợi thuế ưu đãi nhẹ bẫng, một bên là mệnh lệnh nội địa hóa nặng trĩu.",
        "t3": "Cú máy trượt ngang chậm rãi qua chiếc cán cân bị lệch (Slow tracking shot), khắc họa tính chất pháp lý bắt buộc.",
        "overlay": "Không"
    },
    {
        "id": "SC012",
        "dur": 6.3,
        "words": 24,
        "text": "Để đón đầu chính sách đó, VinFast cam kết đầu tư năm trăm triệu đô la vào tổ hợp Thoothukudi tại bang Tamil Nadu",
        "t1": "Khu phức hợp công nghiệp ven biển Thoothukudi, bang Tamil Nadu.",
        "t2": "Toàn cảnh nhà máy VinFast hiện đại với các phân xưởng mái phẳng trải dài trên nền đất quy hoạch bên bờ biển.",
        "t3": "Cú máy toàn cảnh góc cao nhìn xuống (High-angle establishing wide shot), phác họa quy mô dự án 500 triệu USD.",
        "overlay": "\"THOOTHUKUDI: 50.000 XE/NĂM\""
    },
    {
        "id": "SC013",
        "dur": 2.89,
        "words": 11,
        "text": "với công suất thiết kế năm mươi ngàn xe mỗi năm.",
        "t1": "Trung tâm điều hành sản xuất thông minh của nhà máy Thoothukudi.",
        "t2": "Bảng hiển thị kỹ thuật số phát sáng màu xanh ngọc hiển thị thông số công suất thiết kế 50.000 xe mỗi năm.",
        "t3": "Cú máy trượt ngang trên bảng điều khiển kỹ thuật số (Horizontal telemetry tracking shot), thể hiện mục tiêu sản xuất.",
        "overlay": "Không"
    },
    {
        "id": "SC014",
        "dur": 6.3,
        "words": 24,
        "text": "Thế nhưng theo hồ sơ quy hoạch được phê duyệt cho Giai đoạn một, đây đơn thuần chỉ là một nhà máy lắp ráp.",
        "t1": "Bàn vẽ kiến trúc công trình của ban quản lý dự án.",
        "t2": "Bản vẽ sơ đồ mặt bằng tổng thể Giai đoạn 1 được mở rộng, các phân xưởng được phân ô ranh giới rõ ràng bằng nét vẽ màu kem.",
        "t3": "Cú máy lướt chéo qua bản vẽ quy hoạch (Diagonal drafting pan shot), bóc tách cấu trúc thực tế của nhà máy.",
        "overlay": "Không"
    },
    {
        "id": "SC015",
        "dur": 5.25,
        "words": 20,
        "text": "Tổ hợp chỉ có ba phân xưởng chính: Xưởng hàn thân vỏ, xưởng sơn và xưởng lắp ráp hoàn thiện.",
        "t1": "Phân xưởng hàn thân vỏ ô tô (Body Shop) tại Thoothukudi.",
        "t2": "Hàng chục cánh tay robot công nghiệp màu cam thực hiện các đường hàn điểm chính xác, bắn ra những chùm tia lửa màu cam rực rỡ.",
        "t3": "Cú máy trượt dọc theo dây chuyền hàn robot (Robotic line tracking shot), làm nổi bật năng lực gia công cơ khí.",
        "overlay": "Không"
    },
    {
        "id": "SC016",
        "dur": 4.72,
        "words": 18,
        "text": "Họ hoàn toàn không có xưởng dập tấm vỏ và xưởng sản xuất tế bào pin tại chỗ.",
        "t1": "Khuôn viên nhà máy với các phân xưởng sơn và lắp ráp kế cận.",
        "t2": "Khoảng đất trống và bản vẽ kỹ thuật gạch chéo vị trí xưởng dập thân vỏ lớn và xưởng sản xuất cell pin, xác nhận sự vắng mặt tại chỗ.",
        "t3": "Cú máy quét ngang khoảng trống trên bản đồ mặt bằng (Pan across vacant factory zoning), khẳng định thiếu hụt 2 xưởng cốt lõi.",
        "overlay": "Không"
    },
    {
        "id": "SC017",
        "dur": 4.46,
        "words": 17,
        "text": "Chính vì vậy, toàn bộ những chiếc xe VinFast bán tại Ấn Độ từ trước đến nay",
        "t1": "Bãi tập kết xe thành phẩm phía trước tòa nhà điều hành Thoothukudi.",
        "t2": "Những chiếc crossover điện VF 6 và VF 7 bóng bẩy đậu thành hàng dưới ánh nắng miền nam Ấn Độ.",
        "t3": "Cú máy trượt ngang chậm rãi qua hàng xe thành phẩm (Slow tracking shot along the vehicle fleet).",
        "overlay": "Không"
    },
    {
        "id": "SC018",
        "dur": 4.46,
        "words": 17,
        "text": "đều được lắp ráp từ các bộ linh kiện CKD nhập khẩu từ Cát Hải, Hải Phòng.",
        "t1": "Khu bến cảng nước sâu Cát Hải, Hải Phòng tại Việt Nam.",
        "t2": "Các kiện hàng linh kiện CKD đóng thùng gỗ tiêu chuẩn mang nhãn Cát Hải - Thoothukudi được cẩu lên tàu hàng chuyên dụng.",
        "t3": "Cú máy tĩnh trực diện tại cầu cảng xuất khẩu CKD (Steady export quay shot), định vị nguồn gốc linh kiện.",
        "overlay": "\"LINH KIỆN CKD CÁT HẢI\""
    },
    {
        "id": "SC019",
        "dur": 2.89,
        "words": 11,
        "text": "Lắp ráp linh kiện nhập khẩu giúp xe sớm ra lò",
        "t1": "Dây chuyền lắp ráp hoàn thiện tại Thoothukudi.",
        "t2": "Các bộ linh kiện CKD được khui thùng gỗ và lắp ráp nhanh chóng vào khung xe, giúp xe lăn bánh sớm ra thị trường.",
        "t3": "Cú máy trượt theo nhịp lắp ráp linh kiện (Tracking shot following component assembly flow).",
        "overlay": "Không"
    },
    {
        "id": "SC020",
        "dur": 5.51,
        "words": 21,
        "text": "nhưng để đạt mục tiêu nội địa hóa theo cam kết thể chế, VinFast không thể dựa vào CKD mãi mãi.",
        "t1": "Phòng họp chiến lược với đồ thị phân tích giá trị gia tăng nội địa DVA.",
        "t2": "Kỹ sư trưởng VinFast nhìn vào biểu đồ DVA của xe CKD bị chặn đứng ở mức thấp, không thể đáp ứng lộ trình dài hạn.",
        "t3": "Cú máy đẩy chậm vào ánh mắt suy tư của kỹ sư trưởng trước biểu đồ DVA (Slow push-in toward lead engineer).",
        "overlay": "Không"
    },
    {
        "id": "SC021",
        "dur": 4.2,
        "words": 16,
        "text": "Đó là lý do họ bắt tay với hơn ba trăm xưởng cơ khí bản địa",
        "t1": "Hội trường hội thảo tiếp xúc nhà cung cấp phụ trợ tại Chennai.",
        "t2": "Kỹ sư VinFast bắt tay và làm việc cùng đại diện hơn 300 xưởng gia công cơ khí bản địa Ấn Độ xung quanh các bàn mẫu linh kiện.",
        "t3": "Cú máy tĩnh bao quát hội trường tiếp xúc nhà cung ứng (Steady supplier conference shot) với dòng chữ nổi bật.",
        "overlay": "\"300+ XƯỞNG CƠ KHÍ BẢN ĐỊA\""
    },
    {
        "id": "SC022",
        "dur": 5.77,
        "words": 22,
        "text": "lên kế hoạch thuê ngoài dập vỏ và làm linh kiện cho ba dòng xe: VF 3, VF 6 và VF 7.",
        "t1": "Bàn kỹ thuật với các bản vẽ CAD chi tiết thân vỏ.",
        "t2": "Sơ đồ phân rã linh kiện thuê ngoài dập vỏ thép cho 3 dòng xe: VF 3 mini, VF 6 và VF 7 trải rộng trên bàn làm việc chung.",
        "t3": "Cú máy lướt chéo qua các bản vẽ chi tiết tấm vỏ ô tô (Diagonal tracking pan across stamping schematics).",
        "overlay": "Không"
    },
    {
        "id": "SC023",
        "dur": 5.51,
        "words": 21,
        "text": "Tuy nhiên, dự án này mới chỉ dừng lại ở giai đoạn thiết kế và chế tạo khuôn mẫu thử nghiệm.",
        "t1": "Xưởng cơ khí chính xác của đối tác phụ trợ Ấn Độ.",
        "t2": "Khối khuôn dập thử nghiệm đơn lẻ nằm trên bệ máy phay CNC, kỹ sư đang đo đạc thông số kỹ thuật phôi thép ban đầu.",
        "t3": "Cú máy cận cảnh kiểm tra kích thước khuôn mẫu thử nghiệm (Close-up inspection of prototype tooling die).",
        "overlay": "Không"
    },
    {
        "id": "SC024",
        "dur": 5.25,
        "words": 20,
        "text": "Thế rồi đầu tháng 9 năm 2026, các mặt báo đồng loạt đưa tin về một quyết định bất ngờ",
        "t1": "Bức tường màn hình tin tức báo chí kinh tế quốc tế và Ấn Độ.",
        "t2": "Các dòng tít báo lớn xuất hiện dồn dập đưa tin về quyết định bất ngờ của VinFast đối với chuỗi cung ứng bản địa.",
        "t3": "Cú máy lùi chậm làm lộ ra hàng loạt dòng tiêu đề báo chí chớp nháy (Slow pull-back revealing multiple breaking headlines).",
        "overlay": "Không"
    },
    {
        "id": "SC025",
        "dur": 4.99,
        "words": 19,
        "text": "VinFast phát lệnh tạm dừng toàn bộ kế hoạch nội địa hóa đối với cả ba dòng xe này.",
        "t1": "Bàn làm việc điều hành với văn bản giác thư nội bộ chính thức.",
        "t2": "Văn bản thông báo phát lệnh tạm dừng toàn bộ chương trình phát triển linh kiện nội địa cho VF 3, VF 6 và VF 7 trên giấy tiêu đề công ty.",
        "t3": "Cú máy tĩnh khóa chặt văn bản giác thư nội bộ (Steady memo shot) nhấn mạnh sức nặng của quyết định đạp phanh.",
        "overlay": "\"TẠM DỪNG NỘI ĐỊA HÓA\""
    },
    {
        "id": "SC026",
        "dur": 3.67,
        "words": 14,
        "text": "Hãng yêu cầu hơn ba trăm đối tác kê khai chi phí khuôn dập",
        "t1": "Bàn kiểm toán tài chính công nghiệp.",
        "t2": "Các bảng biểu kê khai chi phí khuôn dập (tooling cost) gửi về từ hơn 300 đối tác cơ khí được xếp ngay ngắn để kiểm toán.",
        "t3": "Cú máy trượt ngang qua các tập hồ sơ kê khai chi phí khuôn dập (Slow tracking shot across tooling expense forms).",
        "overlay": "Không"
    },
    {
        "id": "SC027",
        "dur": 3.94,
        "words": 15,
        "text": "và kỹ thuật đã phát sinh để tiến hành bồi thường chi phí thực tế.",
        "t1": "Phòng đàm phán tài chính của VinFast tại Ấn Độ.",
        "t2": "Tập chứng từ cam kết thanh toán bồi thường chi phí thực tế cho đối tác được đóng dấu xác nhận, thể hiện sự sòng phẳng.",
        "t3": "Cú máy đẩy chậm vào chứng từ cam kết bồi thường (Slow push-in on settlement voucher).",
        "overlay": "Không"
    },
    {
        "id": "SC028",
        "dur": 3.41,
        "words": 13,
        "text": "Quyết định rút chân đột ngột làm dấy lên sự bất ngờ và",
        "t1": "Phòng giao dịch tài chính và bàn làm việc của các nhà phân tích ô tô.",
        "t2": "Các nhà phân tích và báo giới bàn tán sôi nổi trước màn hình thị trường, ngạc nhiên trước bước đi đột ngột.",
        "t3": "Cú máy trượt ngang qua bóng dáng các nhà phân tích đang thảo luận (Panning shot across discussing analysts).",
        "overlay": "Không"
    },
    {
        "id": "SC029",
        "dur": 3.67,
        "words": 14,
        "text": "không ít hoài nghi về số phận dự án năm trăm triệu đô la.",
        "t1": "Bản đồ quy hoạch tổng thể nhà máy Thoothukudi trong ánh sáng mờ ảo.",
        "t2": "Dấu chấm hỏi lớn bằng đồ họa noir bao trùm bản đồ dự án 500 triệu USD, phản ánh sự hoài nghi của dư luận.",
        "t3": "Cú máy đẩy chậm vào dấu chấm hỏi trên bản đồ dự án (Slow subtle push-in on the question mark over plant schematic).",
        "overlay": "Không"
    },
    {
        "id": "SC030",
        "dur": 4.2,
        "words": 16,
        "text": "Thế nhưng trên thực tế, dây chuyền tại Thoothukudi không hề dừng lại một ngày nào.",
        "t1": "Toàn cảnh nhà xưởng Thoothukudi nhìn từ bên ngoài lúc hoàng hôn.",
        "t2": "Các dãy nhà xưởng vẫn sáng rực ánh đèn vàng ấm, các xe nâng và công nhân liên tục di chuyển, chứng minh hoạt động không ngừng nghỉ.",
        "t3": "Cú máy trượt ngang toàn cảnh nhà máy hoạt động bình thường (Wide exterior tracking shot), đập tan tin đồn đóng cửa.",
        "overlay": "Không"
    },
    {
        "id": "SC031",
        "dur": 4.99,
        "words": 19,
        "text": "Nhà máy vẫn tiếp tục sáng đèn lắp ráp xe từ linh kiện CKD chuyển sang từ Việt Nam.",
        "t1": "Bên trong xưởng lắp ráp hoàn thiện của Thoothukudi.",
        "t2": "Băng chuyền vẫn nhịp nhàng lắp ráp các cụm linh kiện CKD chuyển từ Cát Hải sang, tạo thành những chiếc xe hoàn chỉnh.",
        "t3": "Cú máy theo sát dây chuyền lắp ráp CKD chuyển động liên tục (Tracking shot along running CKD assembly line).",
        "overlay": "Không"
    },
    {
        "id": "SC032",
        "dur": 4.2,
        "words": 16,
        "text": "Dữ liệu đăng ký xe Vahan vào tháng 8 năm 2026 xác nhận họ vẫn vươn",
        "t1": "Màn hình trung tâm dữ liệu đăng ký phương tiện quốc gia Vahan của Ấn Độ.",
        "t2": "Giao diện hệ thống Vahan tháng 8/2026 hiển thị biểu đồ số lượng đăng ký xe mới của VinFast tăng vọt.",
        "t3": "Cú máy lướt chậm trên giao diện dữ liệu Vahan (Slow analytical dashboard scan shot).",
        "overlay": "Không"
    },
    {
        "id": "SC033",
        "dur": 4.2,
        "words": 16,
        "text": "lên vị trí top 4 thương hiệu dẫn đầu thị phần xe điện toàn Ấn Độ",
        "t1": "Bảng xếp hạng thị phần xe điện Ấn Độ tháng 8/2026.",
        "t2": "Cột xếp hạng của VinFast vươn lên đứng thứ 4 toàn quốc, vượt qua nhiều tên tuổi lớn trong phân khúc xe điện.",
        "t3": "Cú máy tĩnh trực diện vào bục xếp hạng thị phần (Steady market podium shot) tôn vinh vị thế Top 4.",
        "overlay": "\"TOP 4 THỊ PHẦN (8/2026)\""
    },
    {
        "id": "SC034",
        "dur": 3.15,
        "words": 12,
        "text": "với gần hai ngàn hai trăm xe giao đến tay khách hàng.",
        "t1": "Bãi bàn giao xe trước đại lý VinFast tại một thành phố lớn của Ấn Độ.",
        "t2": "Hàng trăm chiếc xe VF 6 và VF 7 hoàn thiện được nhân viên đại lý bàn giao chìa khóa cho các khách hàng Ấn Độ.",
        "t3": "Cú máy trượt ngang qua những chiếc xe được bàn giao (Slow panning shot across delivered vehicles).",
        "overlay": "Không"
    },
    {
        "id": "SC035",
        "dur": 4.99,
        "words": 19,
        "text": "Dây chuyền CKD nhập khẩu giúp họ giữ vững nhịp sản xuất và bảo vệ thị trường trước mắt.",
        "t1": "Khu vực xuất xưởng và điều phối vận tải tại nhà máy Thoothukudi.",
        "t2": "Xe lồng chuyên dụng liên tục nhận xe từ dây chuyền CKD xuất xưởng, tỏa đi các đại lý, giữ vững thị phần trước mắt.",
        "t3": "Cú máy góc rộng trượt theo đoàn xe vận chuyển rời nhà máy (Wide tracking shot following transporter trucks).",
        "overlay": "Không"
    },
    {
        "id": "SC036",
        "dur": 3.41,
        "words": 13,
        "text": "Nhưng ai cũng hiểu, dựa vào linh kiện ngoại nhập sẽ không thể",
        "t1": "Bàn làm việc của nhà phân tích chính sách công nghiệp.",
        "t2": "Biểu đồ chi phí vận tải biển và thuế quan linh kiện nhập khẩu hiển thị dấu hiệu cảnh báo áp lực chi phí dài hạn.",
        "t3": "Cú máy đẩy nhẹ vào biểu đồ chi phí nhập khẩu (Subtle push-in on import cost graph).",
        "overlay": "Không"
    },
    {
        "id": "SC037",
        "dur": 3.67,
        "words": 14,
        "text": "giúp họ né được chiếc thòng lọng thuế quan của Ấn Độ dài hạn.",
        "t1": "Cổng hải quan cảng biển trong màn sương mờ ảo.",
        "t2": "Hình tượng sợi dây cáp thuế quan thể chế của Ấn Độ lơ lửng phía trên những kiện hàng nhập khẩu, thể hiện chiếc thòng lọng dài hạn.",
        "t3": "Cú máy ngước nhìn lên sợi dây cáp thuế quan (Low-angle upward tilt toward the symbolic tariff noose).",
        "overlay": "Không"
    },
    {
        "id": "SC038",
        "dur": 6.82,
        "words": 26,
        "text": "Vậy điều gì khủng khiếp đến mức buộc VinFast phải chấp nhận chi tiền bồi thường, để đạp phanh một kế hoạch mang tính sống còn?",
        "t1": "Phòng họp kín của ban lãnh đạo với ánh sáng chiaroscuro kịch tính.",
        "t2": "Văn bản lệnh bồi thường chi phí tooling nằm giữa bàn, xung quanh là những dấu hỏi lớn về động lực thực sự đằng sau cú đạp phanh.",
        "t3": "Cú máy đẩy chậm đầy căng thẳng vào trung tâm bàn họp (Slow tense push-in toward the center of the boardroom table).",
        "overlay": "Không"
    },
    {
        "id": "SC039",
        "dur": 3.15,
        "words": 12,
        "text": "Câu trả lời nằm sâu bên trong những khối khuôn dập thép",
        "t1": "Góc xưởng gia công cơ khí nặng trong bóng tối sâu thẳm.",
        "t2": "Khối khuôn dập thép khổng lồ bằng hợp kim nguyên khối lấp lánh dưới chùm ánh sáng rọi từ trên cao, toát lên vẻ lạnh lùng cơ khí.",
        "t3": "Cú máy đẩy chậm kịch tính vào khối khuôn thép nguyên khối (Dramatic slow push-in toward giant steel die block).",
        "overlay": "Không"
    },
    {
        "id": "SC040",
        "dur": 4.72,
        "words": 18,
        "text": "Nơi bài toán khấu hao đang trực tiếp định đoạt giá thành của từng chiếc xe xuất xưởng.",
        "t1": "Bề mặt thép sắc bén của khối khuôn dập ô tô với các phương trình kinh tế.",
        "t2": "Công thức toán học khấu hao chi phí cố định (CAPEX amortization) hiện lên trên mặt khối thép, phơi bày cơ chế quyết định giá thành xe.",
        "t3": "Cú máy tĩnh trực diện khóa chặt bề mặt khối thép và công thức khấu hao (Steady macro die face shot) mở ra bài toán của Chương 2.",
        "overlay": "\"BÀI TOÁN KHẤU HAO KHUÔN DẬP\""
    }
]

# Generate Markdown
md_lines = [
    "# chapter_01_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: VinFast Ấn Độ — Thay Đổi Chiến Lược",
    "## Chương 1: Phát Súng Tháng 7/2026: Quả Bom Nội Bộ & Thực Tế Trần Trụi",
    "## Phong cách chủ đạo: Cinematic Editorial Noir (2D Vector Illustration / Graphic Novel Aesthetic - 100% Realistic Physical Spaces, No Surrealism)",
    "## Hệ màu 60-30-10:",
    "- **60% Chủ đạo (Nền/Bóng tối):** Dark Warm Charcoal (`#1A1A1A`) & Deep Industrial Slate (`#1E2522`)",
    "- **30% Bổ trợ (Kết cấu/Chủ thể):** Warm Cream Outlines (`#FFFDF0`) & Steel Silver Grey (`#D1D5DB`)",
    "- **10% Điểm nhấn Dẫn mắt:** Glowing Terracotta Orange (`#FF7043`), Glowing Crimson Coral (`#EF5350`), Electric Turquoise (`#26A69A`)",
    "",
    "> **Quy tắc Text Overlay:** Chỉ chèn chữ vào đúng 10 phân cảnh mốc thông số then chốt (chiếm 25,0%). 30 phân cảnh còn lại (75,0%) để `[TEXT OVERLAY]: Không` nhằm tối đa hóa chuyển động điện ảnh linh hoạt cho camera Veo 3.1.",
    "",
    "---",
    "",
    "| Phân Cảnh (Scene ID) | Thời Gian & Câu Thoại Voiceover (Độ dài & Số từ) | Mô Tả Bối Cảnh Thị Giác Chi Tiết (Anatomy & Motion) | Text Overlay (Selective Typography ~20%) |",
    "| :--- | :--- | :--- | :--- |"
]

for item in ch01_matrix:
    col1 = f"**{item['id']}**"
    col2 = f"`{item['dur']}s` ({item['words']} từ)<br/>*\"{item['text']}\"*"
    col3 = f"**Tầng 1 (Đế cố định):** {item['t1']}<br/>**Tầng 2 (Bộ truyền động/Chủ thể):** {item['t2']}<br/>**Tầng 3 (Khối tác động & Góc máy):** {item['t3']}"
    col4 = f"**{item['overlay']}**"
    md_lines.append(f"| {col1} | {col2} | {col3} | {col4} |")

out_file = os.path.join(EPISODE_DIR, 'chapter_01_visual.md')
with open(out_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"Successfully generated perfect {out_file} with 40 scenes and exactly 10 overlays!")
