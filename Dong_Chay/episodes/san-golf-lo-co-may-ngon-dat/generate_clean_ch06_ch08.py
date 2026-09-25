#!/usr/bin/env python3
"""
Generate Chapters 06, 07, 08 with exact sentence matching and full I2V+ compliance.
Splits sentences with 27w into a1 and a2 so all scenes <= 25w.
"""

from build_full_i2vplus_pipeline import get_sentences, write_and_export

def generate_ch06():
    raw = get_sentences(6)
    scenes = [
        {
            "sid": "CH06_SC001", "thoai": raw[0], "mod": "VEO_AI",
            "boi_canh": "Tòa nhà trụ sở cơ quan quản lý vĩ mô nhà nước với hàng cột đá cẩm thạch uy nghiêm dưới bầu trời trong xanh, cán bộ quản lý bước vào sảnh lớn.",
            "chu_the": "Phong thái đĩnh đạc, kỷ luật hành chính nghiêm cẩn của cơ quan quản lý nhà nước.",
            "camera": "Cinematic slow tilt up từ bậc thềm lên hàng cột đá uy nghi, ánh sáng ban mai trong trẻo.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC002", "thoai": raw[1], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Market-Based Regulatory Mechanism Card",
            "du_lieu": "Can thiệp bằng công cụ thị trường: MARKET-BASED FISCAL MECHANISMS. Buộc dự án trả đúng giá thị trường của tài nguyên đất đai.",
            "bo_cuc": "Nền Slate #1E293B, hai cột đối xứng rõ nét, viền vàng hổ phách #F59E0B.",
            "mau_sac": "Điểm nhấn vàng hổ phách và xanh lục.",
            "overlay": "BOTTOM LEFT | MARKET-BASED REGULATORY TOOLS"
        },
        {
            "sid": "CH06_SC003", "thoai": raw[2], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cổng thông tin điện tử Chính phủ: Bản chụp trang đầu Nghị định số 52/2020/NĐ-CP về kinh doanh sân golf, chữ ký của Thủ tướng và dấu mộc đỏ.",
            "query": "Decree 52 2020 ND-CP golf course business Vietnam government portal",
            "source": "Cổng TTĐT Chính phủ / TTXVN",
            "overlay": "BOTTOM LEFT | DECREE 52/2020/ND-CP"
        },
        {
            "sid": "CH06_SC004", "thoai": raw[3], "mod": "VEO_AI",
            "boi_canh": "Cuốn sổ văn bản quy phạm pháp luật mở ra trên bàn làm việc, hai vạch kẻ ranh giới màu đỏ son sắc lẹm được kẻ song song trên trang giấy.",
            "chu_the": "Ngòi bút dạ quang vàng champagne highlight hai điều khoản trọng yếu của nghị định.",
            "camera": "Steady camera shot cận cảnh ngòi bút vạch ranh giới, ánh sáng ngà kem #FAF7EE ấm áp.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC005", "thoai": raw[4], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cánh đồng lúa hai vụ trĩu hạt vàng óng ả tại đồng bằng Bắc Bộ đang vào mùa gặt, người nông dân lái máy gặt đập liên hợp thu hoạch lúa.",
            "query": "paddy rice field harvest combine harvester protected forest Vietnam",
            "source": "VTV Nông nghiệp Archive",
            "overlay": "BOTTOM LEFT | STRICT BAN: PADDY RICE & FORESTS"
        },
        {
            "sid": "CH06_SC006", "thoai": raw[5], "mod": "VEO_AI",
            "boi_canh": "Bản đồ quy hoạch 1/500 trên bàn làm việc của Sở Quy hoạch - Kiến trúc, một đường ranh giới đỏ kiên cố được vẽ chia tách rạch ròi hai phân khu.",
            "chu_the": "Kiến trúc sư dùng thước kẻ khóa chặt ranh giới phân tách quy hoạch.",
            "camera": "Cinematic slow dolly in, ánh sáng phòng quy hoạch xám đá slate #2A323D.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC007", "thoai": raw[6], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Independent Planning Card",
            "du_lieu": "Khóa chặt phân tách quy hoạch: STANDALONE GOLF PROJECT MANDATE. Sân golf phải lập dự án độc lập, không kèm dự án nhà ở.",
            "bo_cuc": "Nền Slate #1E293B, viền xanh ngọc bích #10B981 vững chãi bao quanh khu thể thao.",
            "mau_sac": "Điểm nhấn xanh ngọc và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | STANDALONE GOLF MANDATE"
        },
        {
            "sid": "CH06_SC008", "thoai": raw[7], "mod": "B_ROLL_REAL",
            "tu_lieu": "Biển cảnh báo quy hoạch tại một dự án sân golf: CẤM XÂY DỰNG NHÀ Ở THƯƠNG MẠI TRONG PHẠM VI SÂN GOLF THEO NGHỊ ĐỊNH 52/2020/NĐ-CP.",
            "query": "construction inspection golf project commercial housing ban Vietnam",
            "source": "Báo Xây Dựng / VTV",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC009", "thoai": raw[8], "mod": "VEO_AI",
            "boi_canh": "Lưỡi kéo kim loại biểu tượng sắc lẹm cắt đứt sợi dây nối giữa tấm biển 'Sân Golf Thể Thao' và bản vẽ phân lô bán nền bất động sản.",
            "chu_the": "Ẩn dụ hành động thể chế dứt khoát chấm dứt việc lợi dụng chính sách.",
            "camera": "Steady camera shot, ánh sáng tông Slate lạnh #1E293B, âm hưởng dứt khoát.",
            "overlay": "BOTTOM LEFT | CUTTING OFF SPECULATION PATH"
        },
        {
            "sid": "CH06_SC010", "thoai": raw[9], "mod": "B_ROLL_REAL",
            "tu_lieu": "Hội trường Diên Hồng Nhà Quốc hội: Bảng điện tử biểu quyết hiển thị kết quả thông qua Luật Đất đai (sửa đổi) năm 2024 với tỷ lệ tán thành áp đảo.",
            "query": "National Assembly passes Land Law 2024 voting electronic board Vietnam",
            "source": "Truyền hình Quốc hội (2024)",
            "overlay": "BOTTOM LEFT | LAND LAW 2024 PASSED"
        },
        {
            "sid": "CH06_SC011", "thoai": raw[10], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Article 159 Abolition Card",
            "du_lieu": "Điều 159 Luật Đất đai 2024: ABOLITION OF GOVERNMENT LAND PRICE FRAMEWORK (BÃI BỎ KHUNG GIÁ ĐẤT CŨ). Xây dựng bảng giá đất thị trường.",
            "bo_cuc": "Nền Slate #2A323D, văn bản luật bôi vàng kiểu Vox trên nền ngà kem #FAF7EE.",
            "mau_sac": "Dấu gạch chéo đỏ đè lên khung giá cũ.",
            "overlay": "BOTTOM LEFT | ARTICLE 159: ABOLISHING PRICE FRAMEWORK"
        },
        {
            "sid": "CH06_SC012", "thoai": raw[11], "mod": "VEO_AI",
            "boi_canh": "Phòng thẩm định giá đất cấp tỉnh: Các chuyên gia đối chiếu bản đồ giá đất giao dịch thực tế trên thị trường số hóa với bảng giá đất địa phương mới.",
            "chu_the": "Cán bộ thẩm định nhập các dữ liệu thị trường thực chứng vào phần mềm định giá.",
            "camera": "Cinematic slow dolly in, ánh sáng phòng họp minh bạch nghiêm túc.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC013", "thoai": raw[12], "mod": "VEO_AI",
            "boi_canh": "Bàn làm việc của giám đốc tài chính doanh nghiệp sân golf, bức thư thông báo tạm nộp tiền thuê đất mới của cơ quan thuế gửi đến bàn làm việc.",
            "chu_the": "Nét mặt trầm ngâm, lo lắng trước cú sốc chi phí tiền thuê đất.",
            "camera": "Steady camera shot cận cảnh nét mặt và bức thư thông báo thuế, ánh sáng vàng lạnh.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC014", "thoai": raw[13], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Old Land Rent Baseline Card",
            "du_lieu": "Tiền thuê đất cũ theo khung giá hành chính: PRE-2024 LAND RENT: 2 - 5 BILLION VND / YEAR cho 100 ha sân golf.",
            "bo_cuc": "Nền Slate #1E293B, cột chi phí màu xanh ngọc bích nhỏ gọn ở góc.",
            "mau_sac": "Điểm nhấn ngà kem và xanh lục.",
            "overlay": "BOTTOM LEFT | OLD RENT: 2 - 5 BILLION VND/YEAR"
        },
        {
            "sid": "CH06_SC015", "thoai": raw[14], "mod": "VEO_AI",
            "boi_canh": "Đại cảnh sân golf 100 ha ngút ngàn, một đồng xu nhỏ tượng trưng cho vài tỷ tiền thuê đất cũ đặt lọt thỏm giữa thảm cỏ bao la.",
            "chu_the": "Hình tượng tương phản trực quan về sự bao cấp ngầm của tài nguyên đất đai giá rẻ trong quá khứ.",
            "camera": "Cinematic slow aerial pan shot, ánh sáng nắng ban mai.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC016", "thoai": raw[15], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Surge to 15-35 Billion Card",
            "du_lieu": "Cú sốc tiền thuê đất mới: NEW LAND RENT (LAND LAW 2024): 15 - 35 BILLION VND / YEAR (TĂNG GẤP 3 ĐẾN 5 LẦN).",
            "bo_cuc": "Nền Slate #2A323D, cột chi phí mới vươn cao với viền đỏ san hô rực rỡ #EF5350.",
            "mau_sac": "Cột chi phí đỏ dựng đứng tạo cú sốc ngân sách.",
            "overlay": "BOTTOM LEFT | NEW RENT: 15 - 35 BILLION VND/YEAR"
        },
        {
            "sid": "CH06_SC017", "thoai": raw[16], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Revenue Erosion Share Pie",
            "du_lieu": "Ăn mòn doanh thu: EATS 30% - 50% TOTAL ANNUAL REVENUE OF AVERAGE GOLF COURSE.",
            "bo_cuc": "Nền Slate #1E293B, bánh tròn doanh thu bị mảng đỏ san hô #EF5350 chiếm trọn một nửa.",
            "mau_sac": "Mảng đỏ phình to nuốt chửng phần doanh thu.",
            "overlay": "BOTTOM LEFT | EATS 30% - 50% OF TOTAL REVENUE"
        },
        {
            "sid": "CH06_SC018", "thoai": raw[17], "mod": "VEO_AI",
            "boi_canh": "Chiếc đồng hồ cát bằng đồng thau đặt trên bản đồ quy hoạch dự án, cát chảy xuống với tốc độ chóng mặt cuốn trôi các đồng tiền vàng đặt bên dưới.",
            "chu_the": "Ẩn dụ kinh tế học về chi phí giữ đất (holding cost) gia tăng đột biến.",
            "camera": "Steady camera shot cận cảnh cát rơi, ánh sáng đèn bàn xám slate.",
            "overlay": "BOTTOM LEFT | HOLDING COST SURGE"
        },
        {
            "sid": "CH06_SC019", "thoai": raw[18], "mod": "B_ROLL_REAL",
            "tu_lieu": "Đoàn thanh tra liên ngành của Ủy ban nhân dân tỉnh đi rà soát các dự án chậm tiến độ: Cán bộ cắm mốc đo đạc và lập biên bản xử phạt.",
            "query": "provincial inspection team reviewing delayed land projects Vietnam",
            "source": "Báo Đầu Tư / VTV",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC020", "thoai": raw[19], "mod": "VEO_AI",
            "boi_canh": "Bảng cân đối kế toán với dòng tiền mặt lưu chuyển thuần chuyển dần từ màu xanh sang màu đỏ san hô rực lửa, các cột dự trữ tiền mặt hạ thấp dần.",
            "chu_the": "Giám đốc tài chính gõ bút xuống bàn đầy bất lực trước áp lực tiền thuê đất hàng năm.",
            "camera": "Cinematic slow dolly in, ánh sáng màn hình máy tính phản chiếu sự cạn kiệt thanh khoản.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC021", "thoai": raw[20], "mod": "VEO_AI",
            "boi_canh": "Cuốn sách Luật Đất đai 2024 đặt trang trọng trên bục gỗ sồi dưới ánh sáng mặt trời ấm áp rực rỡ, bên cạnh là một quả bóng golf màu trắng tinh khiết.",
            "chu_the": "Sự tôn trọng tuyệt đối luật chơi của nền kinh tế thị trường minh bạch.",
            "camera": "Steady camera shot, bố cục cân đối trang nghiêm, viền mực thanh thoát.",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC022", "thoai": raw[21], "mod": "B_ROLL_REAL",
            "tu_lieu": "Phiên đấu giá quyền sử dụng đất công khai tại hội trường thành phố: Các nhà đầu tư giơ biển đấu giá công khai, màn hình điện tử hiển thị giá trúng minh bạch.",
            "query": "public land auction auctioneer gavel bidding screen Vietnam",
            "source": "Báo Pháp Luật / VTV Khớp lệnh",
            "overlay": "BOTTOM LEFT | PAYING TRUE MARKET VALUE"
        },
        {
            "sid": "CH06_SC023a1", "thoai": "Chỉ những sân golf tạo ra giá trị dịch vụ thật,", "mod": "VEO_AI",
            "boi_canh": "Sân golf du lịch ven biển miền Trung đón khách quốc tế tấp nập, thảm cỏ xanh mướt và clubhouse sang trọng phục vụ du khách chuyên nghiệp.",
            "chu_the": "Du khách quốc tế vui vẻ phát bóng, caddie hỗ trợ nhiệt tình chu đáo.",
            "camera": "Cinematic slow pan shot, ánh sáng rực rỡ nhiệt đới.",
            "overlay": "BOTTOM LEFT | AUTHENTIC SERVICE VALUE"
        },
        {
            "sid": "CH06_SC023a2", "thoai": "hoặc nằm trong đại đô thị có sức hấp thụ thật mới có thể tồn tại.", "mod": "VEO_AI",
            "boi_canh": "Đại đô thị sinh thái xanh mát có cư dân sinh sống đông vui, gia đình trẻ dạo bộ ven hồ nước nhìn ra sân golf 18 lỗ ở trung tâm.",
            "chu_the": "Sức hấp thụ thật của thị trường bảo đảm sự tồn tại bền vững cho dự án.",
            "camera": "Cinematic slow tracking shot lướt qua hàng biệt thự sinh thái.",
            "overlay": "BOTTOM LEFT | REAL MARKET ABSORPTION"
        },
        {
            "sid": "CH06_SC024", "thoai": raw[23], "mod": "VEO_AI",
            "boi_canh": "Bộ lọc bằng lưới kim loại sáng bóng biểu trưng cho thể chế đang lọc sạch các viên sỏi rác đầu cơ ra khỏi dòng nước chảy trong vắt của nền kinh tế.",
            "chu_the": "Ẩn dụ trực quan tinh tế về vai trò kiến tạo và thanh lọc của pháp luật.",
            "camera": "Steady camera shot, ánh sáng ngà kem và xám slate đĩnh đạc.",
            "overlay": "BOTTOM LEFT | NATURAL MARKET FILTER"
        },
        {
            "sid": "CH06_SC025", "thoai": raw[24], "mod": "B_ROLL_REAL",
            "tu_lieu": "Người nông dân địa phương đứng bên bờ mương nước ngắm nhìn về phía thảm cỏ sân golf xanh mướt bên kia hàng rào, dòng nước tưới chảy qua cánh đồng.",
            "query": "farmer standing near irrigation canal looking at golf course boundary",
            "source": "Truyền hình Nông thôn / VTV Cần Thơ",
            "overlay": "Không."
        },
        {
            "sid": "CH06_SC026", "thoai": raw[25], "mod": "VEO_AI",
            "boi_canh": "Chiếc bàn cân cổ điển bằng đồng đặt giữa phòng nghiên cứu kinh tế: Một bên là nắm đất màu mỡ và bông lúa vàng, một bên là quả bóng golf trắng và xấp tiền ngoại tệ, tạo cầu nối sang CH07.",
            "chu_the": "Hai đĩa cân dao động nhẹ nhàng rồi tìm điểm thăng bằng khách quan.",
            "camera": "Cinematic slow dolly in cận cảnh trục cân thăng bằng, ánh sáng vàng ấm rọi từ trên cao.",
            "overlay": "BOTTOM LEFT | OPPORTUNITY COST SCALE"
        }
    ]
    write_and_export(6, scenes, "CHƯƠNG 6", "BƯỚC NGOẶT LUẬT ĐẤT ĐAI 2024: KHAI TỬ ĐẦU CƠ ĐẤT RẺ")

def generate_ch07():
    raw = get_sentences(7)
    scenes = [
        {
            "sid": "CH07_SC001a1", "thoai": "Gạt bỏ lớp vỏ tài chính, câu hỏi còn lại là:", "mod": "VEO_AI",
            "boi_canh": "Phòng hội thảo kinh tế học phúc lợi xã hội: Nhà nghiên cứu đứng bên chiếc bảng đen viết dòng chữ phấn trắng: 'SOCIAL COST-BENEFIT ANALYSIS'.",
            "chu_the": "Phong thái học thuật đĩnh đạc, tìm kiếm câu trả lời khách quan First-Principles.",
            "camera": "Cinematic slow dolly in, ánh sáng phòng hội thảo ấm áp ngà kem #FAF7EE.",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC001a2", "thoai": "Một sân golf thực sự mang lại gì và lấy đi những gì của xã hội?", "mod": "VEO_AI",
            "boi_canh": "Chiếc bàn cân kinh tế phúc lợi với hai đĩa cân đối xứng, chuẩn bị cân đo giữa giá trị việc làm ngoại tệ và chi phí tài nguyên môi trường.",
            "chu_the": "Nhà nghiên cứu đặt các thẻ dữ liệu thực chứng lên hai đĩa cân.",
            "camera": "Steady camera shot, ánh sáng trang trọng minh bạch.",
            "overlay": "BOTTOM LEFT | WHAT DOES A GOLF COURSE COST & BRING?"
        },
        {
            "sid": "CH07_SC002", "thoai": raw[1], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Welfare Economics Balance Card",
            "du_lieu": "Bài toán kinh tế phúc lợi: WELFARE ECONOMICS COST-BENEFIT MATRIX. Cân đối giữa ngoại ứng tích cực (việc làm, ngoại tệ) và ngoại ứng tiêu cực (nước, đất).",
            "bo_cuc": "Nền Slate #1E293B, sơ đồ cân bằng hai cột đối xứng rõ nét.",
            "mau_sac": "Điểm nhấn xanh ngọc và cam cảnh báo.",
            "overlay": "BOTTOM LEFT | WELFARE ECONOMICS MATRIX"
        },
        {
            "sid": "CH07_SC003", "thoai": raw[2], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Direct Job Creation Card",
            "du_lieu": "Tạo việc làm trực tiếp: 300 - 500 LOCAL JOBS / 18-HOLE COURSE. Caddie, bảo dưỡng cỏ, lễ tân, ẩm thực.",
            "bo_cuc": "Nền Slate #2A323D, các icon nhân sự màu xanh lục #10B981 xếp hàng ngay ngắn.",
            "mau_sac": "Điểm nhấn xanh lục và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | 300 - 500 LOCAL WORKERS / COURSE"
        },
        {
            "sid": "CH07_SC004", "thoai": raw[3], "mod": "B_ROLL_REAL",
            "tu_lieu": "Lớp tập huấn nghiệp vụ caddie và tiếng Anh giao tiếp cho các thanh niên nông thôn tại trung tâm văn hóa do doanh nghiệp tổ chức.",
            "query": "caddie vocational training English class rural youth Vietnam golf",
            "source": "Truyền hình Đà Nẵng / VTV",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC005", "thoai": raw[4], "mod": "VEO_AI",
            "boi_canh": "@caddie_vietnam_working.jpg -> Hình ảnh nữ caddie người Việt Nam trong trang phục bảo hộ chuyên dụng màu xanh ngọc, nón rộng vành, nụ cười thân thiện đồng hành cùng golfer trên fairway đầy nắng.",
            "chu_the": "Cử chỉ chuyên nghiệp, niềm nở, am hiểu hướng gió và khoảng cách gậy.",
            "camera": "Steady camera shot, ánh nắng ban mai rực rỡ chiếu trên thảm cỏ xanh.",
            "overlay": "BOTTOM LEFT | CADDIE INCOME: 12 - 20 MILLION VND/MONTH"
        },
        {
            "sid": "CH07_SC006", "thoai": raw[5], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Income Surge Multiplier Card",
            "du_lieu": "So sánh thu nhập hàng tháng: NÔNG NGHIỆP TRUYỀN THỐNG (3 - 5M) vs NGHỀ CADDIE (12 - 20M VND/THÁNG). GẤP 3 ĐẾN 4 LẦN.",
            "bo_cuc": "Nền Slate #1E293B, hai cột thu nhập đối xứng trực quan, tỷ lệ 3X - 4X nổi bật.",
            "mau_sac": "Cột thu nhập caddie vươn cao màu xanh lục Emerald #10B981.",
            "overlay": "BOTTOM LEFT | INCOME: 3X - 4X TRADITIONAL FARMING"
        },
        {
            "sid": "CH07_SC007", "thoai": raw[6], "mod": "B_ROLL_REAL",
            "tu_lieu": "Ngôi nhà khang trang mới xây của gia đình caddie ở vùng ven biển: Xe máy mới dựng trước sân, bữa cơm gia đình đầm ấm rộn rã.",
            "query": "newly built rural house Vietnam family dinner improved livelihood",
            "source": "Báo Nông Thôn Ngày Nay / VTV",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC008", "thoai": raw[7], "mod": "VEO_AI",
            "boi_canh": "Buổi giao ban đầu giờ sáng tại phòng sinh hoạt caddie: Phòng ốc sạch sẽ khang trang, nhân viên nhận thẻ bảo hiểm y tế và lịch phân ca chuyên nghiệp.",
            "chu_the": "Môi trường làm việc văn minh, kỷ luật và bảo đảm quyền lợi người lao động.",
            "camera": "Cinematic slow dolly in, ánh sáng phòng sáng sủa và ấm cúng.",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC009", "thoai": raw[8], "mod": "VEO_AI",
            "boi_canh": "Đồng hồ đo nước tưới công nghiệp xoay vòng liên tục với lưu lượng hàng nghìn mét khối nước dưới cái nắng gay gắt trưa hè.",
            "chu_the": "Khung cảnh tĩnh lặng nhưng cảnh báo về áp lực thâm dụng tài nguyên nước.",
            "camera": "Steady camera shot cận cảnh mặt đồng hồ đo nước, ánh sáng tương phản gắt.",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC010", "thoai": raw[9], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Daily Water Consumption Card",
            "du_lieu": "Tiêu thụ tài nguyên nước: WATER USE: 2,000 - 3,500 M3 / DAY (TƯƠNG ĐƯƠNG 15,000 HỘ DÂN SINH HOẠT).",
            "bo_cuc": "Nền Slate #1E293B, con số tiêu thụ hiển thị to bản sắc nét kèm icon giọt nước khổng lồ.",
            "mau_sac": "Điểm nhấn cam cảnh báo #FF7043 và đỏ san hô.",
            "overlay": "BOTTOM LEFT | WATER USE: 2,000 - 3,500 M3/DAY"
        },
        {
            "sid": "CH07_SC011", "thoai": raw[10], "mod": "B_ROLL_REAL",
            "tu_lieu": "Giếng khoan khô cạn trơ đáy tại một ngôi làng nông thôn ven dự án golf, người dân kéo dây gàu lên chỉ có cát khô.",
            "query": "dry well water shortage underground water depletion rural Vietnam",
            "source": "VTV Môi trường / Báo Tuổi Trẻ",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC012", "thoai": raw[11], "mod": "VEO_AI",
            "boi_canh": "Hệ thống hồ sinh học tuần hoàn rộng lớn bên trong sân golf hiện đại: Bờ kè đá tự nhiên và hoa sen hoa súng, các đường ống ngầm thu gom nước mưa.",
            "chu_the": "Giải pháp công nghệ tuần hoàn nước mặt thông minh thân thiện môi trường.",
            "camera": "Cinematic slow aerial pan shot, mặt nước hồ phẳng lặng phản chiếu mây trời.",
            "overlay": "BOTTOM LEFT | CLOSED-LOOP RECIRCULATION PONDS"
        },
        {
            "sid": "CH07_SC013", "thoai": raw[12], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Closed-Loop Rainwater Flowchart",
            "du_lieu": "Quy trình tuần hoàn nước mưa khép kín: MÙA MƯA: THU GOM 100% NƯỚC MẶT -> HỒ LẮNG TÍCH TRỮ -> MÙA KHÔ: TƯỚI TIÊU (0% NƯỚC NGẦM).",
            "bo_cuc": "Nền Slate #2A323D, mũi tên tuần hoàn màu xanh ngọc bích #10B981 khép kín.",
            "mau_sac": "Dòng nước tuần hoàn khép kín nhịp nhàng.",
            "overlay": "BOTTOM LEFT | 100% RAINWATER RECYCLING"
        },
        {
            "sid": "CH07_SC014", "thoai": raw[13], "mod": "VEO_AI",
            "boi_canh": "Mặt cắt địa chất 3D của lớp đất dưới thảm cỏ fairway: Lớp cỏ paspalum -> lớp cát thạch anh mịn -> màng lọc địa kỹ thuật sinh học phân hủy phân bón an toàn.",
            "chu_the": "Mô phỏng công nghệ xử lý vi sinh bảo vệ tầng nước ngầm tuyệt đối.",
            "camera": "Steady camera shot góc nhìn mặt cắt ngang khoa học, ánh sáng dịu mắt.",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC015", "thoai": raw[14], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Barren Sand Benefit Equation",
            "du_lieu": "Lợi ích vượt trội trên đất cát cằn cỗi: ĐẤT CÁT + HỒ TUẦN HOÀN -> NET BENEFIT: DÒNG NGOẠI TỆ & VIỆC LÀM ÁP ĐẢO CHI PHÍ MÔI TRƯỜNG.",
            "bo_cuc": "Nền Slate #1E293B, biểu thức màu xanh lục Emerald #10B981 rực rỡ.",
            "mau_sac": "Điểm nhấn xanh lục và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | NET BENEFIT ON BARREN SAND: POSITIVE"
        },
        {
            "sid": "CH07_SC016a1", "thoai": "Nhưng nếu lấy đất trồng trọt màu mỡ để làm sân cỏ,", "mod": "B_ROLL_REAL",
            "tu_lieu": "Cảnh vườn cây ăn trái phù sa màu mỡ bạt ngàn bị máy ủi san phẳng để lấy mặt bằng làm dự án sân golf, đất đai trơ trọi cát bụi.",
            "query": "fertile fruit orchard cleared bulldozed for golf development Vietnam",
            "source": "Báo Nông Nghiệp Việt Nam / VTV",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC016a2", "thoai": "chi phí cơ hội xã hội sẽ là một tổn thất lớn cho đất nước.", "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Social Opportunity Loss Card",
            "du_lieu": "Tổn thất chi phí cơ hội xã hội: LOSS OF FERTILE PADDY LAND = MASSIVE SOCIAL OPPORTUNITY COST.",
            "bo_cuc": "Nền Slate #2A323D, dấu chấm than đỏ san hô #EF5350 cảnh báo nghiêm khắc.",
            "mau_sac": "Điểm nhấn đỏ san hô và cam cảnh báo.",
            "overlay": "BOTTOM LEFT | SOCIAL OPPORTUNITY COST LOSS"
        },
        {
            "sid": "CH07_SC017", "thoai": raw[16], "mod": "VEO_AI",
            "boi_canh": "Quả địa cầu 3D xoay chậm trên bàn nghiên cứu địa kinh tế, ánh sáng mặt trời chiếu sáng từ châu Á sang Bắc Mỹ, phản chiếu sự chuyển dịch công năng đất đai.",
            "chu_the": "Góc nhìn toàn cầu sâu sắc về sự vận động và tối ưu hóa tài nguyên đất đai.",
            "camera": "Cinematic slow tracking shot quanh quả địa cầu, ánh sáng ngà kem #FAF7EE.",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC018", "thoai": raw[17], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "US Course Closures Stat Card",
            "du_lieu": "Thống kê đóng cửa sân golf tại Mỹ sau 2008: US GOLF COURSE CLOSURES: > 1,200 COURSES PERMANENTLY CLOSED (POST-2008).",
            "bo_cuc": "Nền Slate #1E293B, bản đồ nước Mỹ với các chấm đỏ đóng cửa co cụm lại.",
            "mau_sac": "Điểm nhấn đỏ san hô #EF5350 biểu thị sự thoái trào tự nhiên.",
            "overlay": "BOTTOM LEFT | USA: >1,200 GOLF COURSES CLOSED"
        },
        {
            "sid": "CH07_SC019", "thoai": raw[18], "mod": "B_ROLL_REAL",
            "tu_lieu": "Nhóm bạn trẻ thế hệ Gen Z tại Mỹ lướt smartphone trong quán cà phê hiện đại, bận rộn với nhịp sống đô thị nhanh, không mặn mà với 5 tiếng trên sân cỏ.",
            "query": "young millennials smartphone cafe busy urban lifestyle USA",
            "source": "Bloomberg Quicktake / CNBC",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC020", "thoai": raw[19], "mod": "VEO_AI",
            "boi_canh": "Phòng họp quỹ đầu tư bất động sản tại New York: Các nhà quản lý quỹ thảo luận bản vẽ quy hoạch chuyển đổi công năng (adaptive reuse) các sân golf đóng cửa.",
            "chu_the": "Thảo luận chuyên nghiệp, quyết đoán về việc tái phân bổ tài sản đất đai.",
            "camera": "Cinematic slow dolly in, ánh sáng kính văn phòng Phố Wall đĩnh đạc.",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC021", "thoai": raw[20], "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam khu dân cư sinh thái mới tại California xây dựng trên nền sân golf cũ: Các dãy nhà phố xinh đẹp bao quanh công viên cây xanh và hồ nước.",
            "query": "former golf course converted to residential housing community California",
            "source": "US Real Estate Media / ABC News",
            "overlay": "BOTTOM LEFT | CONVERTED TO RESIDENTIAL PARKS"
        },
        {
            "sid": "CH07_SC022", "thoai": raw[21], "mod": "VEO_AI",
            "boi_canh": "Đại bản doanh trung tâm dữ liệu AI hiện đại mọc lên trên sườn đồi từng là sân golf cũ: Các khối nhà thép kiên cố màu xám bạc #2A323D, làm mát bằng hồ nước tuần hoàn.",
            "chu_the": "Biểu tượng công nghệ cao thay thế mô hình thể thao thâm dụng đất đai.",
            "camera": "Cinematic slow aerial pan shot, ánh sáng hoàng hôn rọi trên bề mặt kim loại sáng bóng.",
            "overlay": "BOTTOM LEFT | GOLF COURSES -> AI DATA CENTERS"
        },
        {
            "sid": "CH07_SC023", "thoai": raw[22], "mod": "B_ROLL_REAL",
            "tu_lieu": "Bên trong trung tâm dữ liệu AI quy mô khổng lồ: Hàng nghìn tủ rack máy chủ nhấp nháy đèn LED xanh lam, hệ thống làm mát hiện đại hoạt động liên tục.",
            "query": "hyperscale data center server racks glowing blue LED cooling infrastructure",
            "source": "Bloomberg Technology Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC024", "thoai": raw[23], "mod": "VEO_AI",
            "boi_canh": "@kyocera_mega_solar_farm.jpg -> Đại cảnh các sườn đồi bậc thang tại tỉnh Kyoto từng là các hố golf bỏ hoang, nay được phủ kín bởi hàng vạn tấm pin năng lượng mặt trời Kyocera.",
            "chu_the": "Khung cảnh tái sinh tài nguyên đất đai ngoạn mục sang năng lượng tái tạo sạch.",
            "camera": "Cinematic slow crane up góc rộng, ánh nắng rực rỡ phản chiếu trên mặt pin mặt trời.",
            "overlay": "BOTTOM LEFT | KYOCERA KYOTO: MEGA SOLAR ON GOLF LAND"
        },
        {
            "sid": "CH07_SC025", "thoai": raw[24], "mod": "VEO_AI",
            "boi_canh": "Hình ảnh mầm cây xanh vươn mình đâm chồi nảy lộc từ lớp đất nâu ẩm ướt dưới ánh bình minh ấm áp, biểu thị sự vận động không ngừng của tài nguyên.",
            "chu_the": "Ẩn dụ quy luật tái sinh tự nhiên không ngừng nghỉ của tài nguyên đất đai.",
            "camera": "Cinematic macro slow tilt up, ánh sáng ban mai vàng ấm #F59E0B.",
            "overlay": "Không."
        },
        {
            "sid": "CH07_SC026", "thoai": raw[25], "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam chuyển dịch công năng đất đai: Từ các thảm cỏ hoang tàn sang các công trình năng lượng xanh và công viên công cộng phục vụ xã hội.",
            "query": "land reallocation urban park solar farm sustainable development drone",
            "source": "NHK World / Reuters Land Trends",
            "overlay": "BOTTOM LEFT | NATURAL MARKET REALLOCATION"
        },
        {
            "sid": "CH07_SC027", "thoai": raw[26], "mod": "VEO_AI",
            "boi_canh": "Quả bóng golf đặt trên bàn phát bóng công nghệ phát sáng vòng tròn neon màu xanh ngọc Cyan #00C2CB, phía sau là màn hình mô phỏng 3D, tạo cầu nối sang CH08.",
            "chu_the": "Sự bứt phá của công nghệ tháo gỡ rào cản tài nguyên đất đai.",
            "camera": "Cinematic slow dolly in cận cảnh quả bóng gắn chip vi cảm biến, ánh sáng neon rực rỡ.",
            "overlay": "BOTTOM LEFT | CREATIVE DESTRUCTION REVOLUTION"
        }
    ]
    write_and_export(7, scenes, "CHƯƠNG 7", "CHI PHÍ CƠ HỘI CỦA ĐẤT NƯỚC: NƯỚC, VIỆC LÀM VÀ SỰ TÁI SINH")

def generate_ch08():
    raw = get_sentences(8)
    scenes = [
        {
            "sid": "CH08_SC001", "thoai": raw[0], "mod": "VEO_AI",
            "boi_canh": "Chiếc gậy golf cổ điển bằng gỗ hickory và quả bóng golf da cổ đầu thế kỷ 20 đặt trong tủ kính trưng bày của bảo tàng thể thao.",
            "chu_the": "Tĩnh vật cổ điển thể hiện sự bảo thủ lịch sử kéo dài hàng trăm năm của bộ môn golf.",
            "camera": "Cinematic slow dolly in cận cảnh chiếc gậy gỗ cổ, tông màu ngà kem #FAF7EE thanh lịch.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC002", "thoai": raw[1], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cổng sắt đúc hoa văn mạ vàng đóng kín của một câu lạc bộ golf quý tộc lâu đời tại Anh: Biển báo 'MEMBERS ONLY', hàng rào cao ngất ngăn cách thế giới bên ngoài.",
            "query": "exclusive private golf club gates members only sign luxury historical",
            "source": "BBC Documentary / Golf Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC003", "thoai": raw[2], "mod": "VEO_AI",
            "boi_canh": "@joseph_schumpeter_portrait.jpg -> Chân dung học thuật kinh tế gia Joseph Schumpeter trong âu phục len cổ điển, ngồi trong giảng đường Harvard với bảng đen vẽ sơ đồ tiến hóa tư bản.",
            "chu_the": "Nhà kinh tế học nhìn thẳng về phía trước với ánh mắt thông tuệ và sâu sắc.",
            "camera": "Steady camera shot, ánh sáng phòng học thuật trang nhã, viền mực đậm nét đĩnh đạc.",
            "overlay": "BOTTOM LEFT | JOSEPH SCHUMPETER (1883 - 1950)"
        },
        {
            "sid": "CH08_SC004a1", "thoai": "Khi những rào cản về đất đai và chi phí trở nên quá ngột ngạt,", "mod": "VEO_AI",
            "boi_canh": "Bức tường bê tông cao biểu trưng cho rào cản đất đai và chi phí nứt toác ra dưới áp lực của nhu cầu đại chúng hóa thể thao.",
            "chu_the": "Sự bức bối của mô hình truyền thống trước sức ép xã hội.",
            "camera": "Cinematic slow dolly in, ánh sáng tương phản gắt gao.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC004a2", "thoai": "công nghệ đã mở ra một lối thoát mang tính cách mạng.", "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Creative Destruction Paradigm Shift Card",
            "du_lieu": "Bước ngoặt phá hủy sáng tạo: CREATIVE DESTRUCTION IN SPORTS. Công nghệ mô phỏng và Sportainment giải phóng bộ môn golf.",
            "bo_cuc": "Nền Slate #1E293B, biểu tượng tia sét công nghệ phá vỡ rào cản cũ.",
            "mau_sac": "Điểm nhấn xanh ngọc Cyan #00C2CB và vàng hổ phách #F59E0B.",
            "overlay": "BOTTOM LEFT | CREATIVE DESTRUCTION IN SPORTS"
        },
        {
            "sid": "CH08_SC005", "thoai": raw[4], "mod": "B_ROLL_REAL",
            "tu_lieu": "Trang bìa Báo cáo thường niên 2024 của Hiệp hội Golf Quốc gia Mỹ (National Golf Foundation - NGF) công bố biểu đồ số liệu tại hội nghị thường niên.",
            "query": "National Golf Foundation annual report 2024 presentation conference",
            "source": "National Golf Foundation (2024)",
            "overlay": "BOTTOM LEFT | NGF 2024 HISTORIC REPORT"
        },
        {
            "sid": "CH08_SC006", "thoai": raw[5], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Off-Course Participation Card",
            "du_lieu": "Số người chơi ngoài sân cỏ tại Mỹ: OFF-COURSE GOLF PARTICIPATION: 32.9 MILLION PLAYERS.",
            "bo_cuc": "Nền Slate #2A323D, con số 32.9 triệu người phát sáng màu xanh ngọc bích #10B981.",
            "mau_sac": "Điểm nhấn xanh ngọc và vàng champagne.",
            "overlay": "BOTTOM LEFT | OFF-COURSE GOLF: 32.9M PLAYERS"
        },
        {
            "sid": "CH08_SC007", "thoai": raw[6], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Historic Crossover Chart",
            "du_lieu": "Giao cắt lịch sử: OFF-COURSE (32.9M PLAYERS) CHÍNH THỨC VƯỢT ON-COURSE TRADITIONAL (26.6M PLAYERS).",
            "bo_cuc": "Nền Slate #1E293B, điểm giao cắt (Crossover Point) phát sáng chớp nhẹ.",
            "mau_sac": "Đường xanh ngọc bứt phá dũng mãnh.",
            "overlay": "BOTTOM LEFT | HISTORIC CROSSOVER: 32.9M VS 26.6M"
        },
        {
            "sid": "CH08_SC008", "thoai": raw[7], "mod": "VEO_AI",
            "boi_canh": "@topgolf_venue_night.jpg -> Đại cảnh tổ hợp giải trí Topgolf 3 tầng hình vòng cung rực rỡ ánh đèn LED nhiều màu trong đêm đô thị, các tầng phát bóng đông nghẹt người chơi.",
            "chu_the": "Không gian thể thao giải trí Sportainment năng động, hiện đại và tràn đầy sức sống.",
            "camera": "Cinematic slow aerial pan shot, ánh sáng rực rỡ sắc màu trong màn đêm đô thị.",
            "overlay": "BOTTOM LEFT | TOPGOLF SPORTAINMENT REVOLUTION"
        },
        {
            "sid": "CH08_SC009", "thoai": raw[8], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Urban Footprint Efficiency Card",
            "du_lieu": "Hiệu quả diện tích đất: SÂN CỎ TRUYỀN THỐNG (80 - 100 HA) vs TỔ HỢP TOPGOLF ĐÔ THỊ (5 HA). TIẾT KIỆM 95% ĐẤT.",
            "bo_cuc": "Nền Slate #2A323D, hai khối hộp diện tích tương phản 20:1 trực quan.",
            "mau_sac": "Khối 5 ha nhỏ gọn phát sáng hiệu quả cao.",
            "overlay": "BOTTOM LEFT | 5 HA URBAN FOOTPRINT (95% LAND SAVED)"
        },
        {
            "sid": "CH08_SC010", "thoai": raw[9], "mod": "VEO_AI",
            "boi_canh": "Người chơi vung gậy đánh bóng, quả bóng bay vào không gian đêm, màn hình Toptracer gắn cạnh vịnh phát bóng vẽ nên đường cong quỹ đạo bay 3D phát sáng neon rực rỡ.",
            "chu_the": "Nhóm bạn trẻ vỗ tay reo mừng phấn khích trước cú đánh đạt điểm cao.",
            "camera": "Cinematic slow motion tracking shot từ quả bóng chuyển sang màn hình đồ họa 3D.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC011", "thoai": raw[10], "mod": "B_ROLL_REAL",
            "tu_lieu": "Không khí tiệc tùng sôi động tại một vịnh phát bóng Topgolf ban đêm: Nhóm bạn trẻ vừa trò chuyện vừa thưởng thức đồ ăn nhẹ và đồ uống trong tiếng nhạc sôi động.",
            "query": "Topgolf party night food drinks friends smiling hitting balls",
            "source": "Topgolf Media Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC012", "thoai": raw[11], "mod": "VEO_AI",
            "boi_canh": "Quầy bar trung tâm của tổ hợp thể thao công nghệ: Bartender điêu luyện pha chế đồ uống dưới ánh đèn ấm áp, bàn tiệc đầy ắp món ăn và nụ cười rạng rỡ của thực khách.",
            "chu_the": "Không gian giao lưu văn hóa và ẩm thực văn minh, sôi nổi.",
            "camera": "Cinematic slow tracking shot lướt qua quầy bar sang trọng, ánh sáng vàng ấm và cyan ngọc.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC013", "thoai": raw[12], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Topgolf Margin Breakdown Card",
            "du_lieu": "Cơ cấu doanh thu Topgolf: F&B ẨM THỰC (52%), GAMEPLAY VÉ TẬP (36%), EVENTS (12%). BIÊN EBITDA: 30% - 34%.",
            "bo_cuc": "Nền Slate #1E293B, biểu đồ tròn kết hợp thẻ biên lợi nhuận rực sáng màu xanh lục #10B981.",
            "mau_sac": "Biên EBITDA 30–34% phát sáng khẳng định tính hiệu quả vượt trội.",
            "overlay": "BOTTOM LEFT | TOPGOLF EBITDA MARGIN: 30% - 34%"
        },
        {
            "sid": "CH08_SC014", "thoai": raw[13], "mod": "VEO_AI",
            "boi_canh": "Mô hình so sánh biểu trưng: Một bên là cuốn sổ kế toán sân cỏ truyền thống với dòng lỗ mờ nhạt, một bên là màn hình cảm ứng của tổ hợp công nghệ với dòng lợi nhuận tăng dốc đứng.",
            "chu_the": "Sự áp đảo của mô hình kinh doanh dịch vụ thông minh nhẹ vốn.",
            "camera": "Cinematic slow dolly in, ánh sáng tương phản rõ nét giữa cũ và mới.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC015", "thoai": raw[14], "mod": "B_ROLL_REAL",
            "tu_lieu": "Phố Gangnam sầm uất tại Seoul về đêm: Hàng loạt biển hiệu phát sáng logo 'GOLFZON SCREEN GOLF' tại các tòa nhà văn phòng và trung tâm thương mại.",
            "query": "Seoul Gangnam night streets Golfzon screen golf neon sign South Korea",
            "source": "Yonhap News / KBS World",
            "overlay": "BOTTOM LEFT | GOLFZON SCREEN GOLF (KOREA)"
        },
        {
            "sid": "CH08_SC016", "thoai": raw[15], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Golfzon Massive Scale Card",
            "du_lieu": "Mạng lưới Golfzon tại Hàn Quốc: 5,000+ CENTERS -> 60 MILLION ROUNDS / YEAR. ĐẤT TỰ NHIÊN TIÊU TỐN: 0 HECTARES.",
            "bo_cuc": "Nền Slate #2A323D, con số 60 triệu lượt chơi hiển thị to bản sắc nét viền xanh ngọc Cyan #00C2CB.",
            "mau_sac": "Con số nhảy tăng tốc mạnh mẽ.",
            "overlay": "BOTTOM LEFT | 5,000 CENTERS: 60M ROUNDS/YEAR"
        },
        {
            "sid": "CH08_SC017", "thoai": raw[16], "mod": "VEO_AI",
            "boi_canh": "@screengolf_indoor_simulator.jpg -> Không gian phòng chơi golf mô phỏng 3D hiện đại tại Seoul: Người chơi trong trang phục công sở thoải mái vung gậy trước màn hình cong 3D cỡ lớn siêu thực.",
            "chu_the": "Không khí giải trí đại chúng thân mật, thư thái sau giờ làm việc.",
            "camera": "Steady camera shot, ánh sáng phòng dịu mắt, màn hình 3D phản chiếu màu cỏ xanh mướt.",
            "overlay": "BOTTOM LEFT | MASS ACCESSIBILITY: ~$25 / SESSION"
        },
        {
            "sid": "CH08_SC018", "thoai": raw[17], "mod": "VEO_AI",
            "boi_canh": "Bức tường kính trong suốt nối giữa thế giới mô phỏng 3D và thế giới tự nhiên: Một cậu bé và một người lớn tuổi cùng chạm tay vào quả bóng golf ảo trên màn hình.",
            "chu_the": "Biểu tượng của sự xóa bỏ rào cản thế hệ và tầng lớp xã hội trong thể thao.",
            "camera": "Cinematic slow dolly in, ánh sáng ngà kem và xanh ngọc Cyan rực rỡ.",
            "overlay": "BOTTOM LEFT | DEMOCRATIZATION OF GOLF"
        },
        {
            "sid": "CH08_SC019", "thoai": raw[18], "mod": "VEO_AI",
            "boi_canh": "Chiếc gông xích biểu tượng bằng kim loại rỉ sét buộc quanh quả bóng golf tự động mở khóa bung ra, quả bóng bay vút lên bầu trời tự do trong xanh ngát.",
            "chu_the": "Ẩn dụ sự giải phóng bộ môn thể thao khỏi sự trói buộc của ván cược đất đai.",
            "camera": "Cinematic slow motion tracking shot quả bóng bay tự do, ánh bình minh chan hòa.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC020", "thoai": raw[19], "mod": "B_ROLL_REAL",
            "tu_lieu": "Nụ cười rạng rỡ của những người trẻ tuổi đang tập swing trong phòng golf 3D tại Hà Nội hoặc TP.HCM, đối chiếu với cánh đồng lúa thanh bình bên ngoài thành phố.",
            "query": "young Vietnamese golfers indoor 3D simulator smiling swing urban lifestyle",
            "source": "Vietnam Golf Magazine / VTV",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC021", "thoai": raw[20], "mod": "VEO_AI",
            "boi_canh": "Không gian thư viện học thuật vĩ mô, người dẫn chuyện đứng bên cửa sổ nhìn ra toàn cảnh một thành phố hiện đại với những dòng xe lưu thông nhộn nhịp.",
            "chu_the": "Phong thái trầm tư, sâu sắc, điềm tĩnh đúc kết bài học lớn cho khán giả.",
            "camera": "Cinematic slow dolly in từ sau lưng người dẫn chuyện, ánh sáng ngà kem #FAF7EE bao trùm không gian.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC022", "thoai": raw[21], "mod": "VEO_AI",
            "boi_canh": "Hình ảnh hai bàn tay nâng niu quả bóng golf màu trắng tinh khiết dưới ánh nắng mặt trời buổi sớm, thảm cỏ xanh mướt phía dưới trải dài bình yên.",
            "chu_the": "Sự tôn trọng trọn vẹn đối với đam mê thể thao chân chính của con người.",
            "camera": "Steady camera shot cận cảnh đôi bàn tay và quả bóng, ánh sáng ban mai vàng ấm rạng rỡ.",
            "overlay": "Không."
        },
        {
            "sid": "CH08_SC023", "thoai": raw[22], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "National Resource Allocation Pillars Card",
            "du_lieu": "3 Trụ cột First-Principles tối thượng: (1) MINH BẠCH CHI PHÍ CƠ HỘI, (2) KỶ LUẬT THỊ TRƯỜNG & PHÁP LUẬT, (3) HIỆU QUẢ SỬ DỤNG TÀI NGUYÊN.",
            "bo_cuc": "Nền Slate #1E293B, 3 cột trụ đá cẩm thạch đỡ lấy biểu tượng sự thịnh vượng quốc gia.",
            "mau_sac": "3 cột trụ phát sáng màu xanh lục và vàng hổ phách vững chãi.",
            "overlay": "BOTTOM LEFT | RESOURCE ALLOCATION EFFICIENCY"
        },
        {
            "sid": "CH08_SC024", "thoai": raw[23], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cổng Tòa nhà Quốc hội và Tòa án Nhân dân Tối cao uy nghiêm dưới nắng hè, đối chiếu với sàn giao dịch bất động sản minh bạch công khai giá đất.",
            "query": "National Assembly building Vietnam modern institutional governance transparency",
            "source": "TTXVN / Truyền hình Quốc hội",
            "overlay": "BOTTOM LEFT | SPECULATION ERA OFFICIALLY ENDS"
        },
        {
            "sid": "CH08_SC025", "thoai": raw[24], "mod": "VEO_AI",
            "boi_canh": "Hai golfer trẻ tuổi người Việt Nam tươi cười bắt tay nhau trên thảm cỏ fairway ven biển dưới ánh nắng hoàng hôn tuyệt đẹp.",
            "chu_the": "Tinh thần thể thao cao thượng, văn minh và hướng tới sự phát triển bền vững.",
            "camera": "Cinematic slow dolly in, ánh sáng hoàng hôn vàng cam ấm áp bao trùm khung hình.",
            "overlay": "BOTTOM LEFT | THE FUTURE OF AUTHENTIC VALUE"
        },
        {
            "sid": "CH08_SC026", "thoai": raw[25], "mod": "VEO_AI",
            "boi_canh": "Đại cảnh flycam bay vút từ mặt cỏ xanh mướt lên bầu trời bao la, thu trọn toàn cảnh non sông Việt Nam với bờ biển xanh ngắt và các thành phố rực rỡ, khép lại trọn vẹn tập phim.",
            "chu_the": "Tầm nhìn vĩ mô bao quát, tráng lệ và trường tồn.",
            "camera": "Cinematic epic crane up and backward tilt, ánh bình minh chan hòa trên dải đất nước, kết thúc tuyệt mỹ chuẩn điện ảnh Dòng Chảy.",
            "overlay": "BOTTOM LEFT | LAND SERVING SOCIETY"
        }
    ]
    write_and_export(8, scenes, "CHƯƠNG 8", "SỰ PHÁ HỦY SÁNG TẠO: OFF-COURSE GOLF VÀ CUỘC CÁCH MẠNG DÂN CHỦ HÓA")

if __name__ == "__main__":
    generate_ch06()
    generate_ch07()
    generate_ch08()
