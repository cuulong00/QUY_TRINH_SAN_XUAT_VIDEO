#!/usr/bin/env python3
"""
Generate Chapters 04 and 05 with exact sentence matching and full I2V+ compliance.
Splits 4 sentences with 27w in CH04 into a1 and a2 so all scenes <= 25w.
"""

from build_full_i2vplus_pipeline import get_sentences, write_and_export

def generate_ch04():
    raw = get_sentences(4)
    scenes = [
        {
            "sid": "CH04_SC001", "thoai": raw[0], "mod": "VEO_AI",
            "boi_canh": "Bức tường gạch sẫm màu với ánh sáng đèn chiếu hắt lên các bài báo và định kiến dư luận về sân golf, một người nghiên cứu đang quan sát với ánh mắt điềm tĩnh.",
            "chu_the": "Người nghiên cứu bước qua bức tường định kiến để tiến về phía bản đồ kinh tế toàn cầu.",
            "camera": "Cinematic slow tracking shot, ánh sáng xám slate chuyển dần sang ấm áp.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC002", "thoai": raw[1], "mod": "B_ROLL_REAL",
            "tu_lieu": "Bản tin truyền hình tranh luận về việc cấp phép sân golf và những ý kiến trái chiều của dư luận về hiệu quả sử dụng đất.",
            "query": "television news debate golf course land use criticism public opinion Vietnam",
            "source": "VTV Thời sự Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC003", "thoai": raw[2], "mod": "VEO_AI",
            "boi_canh": "Một mô hình biệt thự phân lô bằng nhựa đặt trơ trọi trên bãi cỏ, biểu thị định kiến coi bất động sản là chiếc phao cứu sinh duy nhất của sân golf.",
            "chu_the": "Hình tượng trực quan về định kiến phân lô bán nền trong tâm thức công chúng.",
            "camera": "Steady camera shot cận cảnh mô hình biệt thự trên cỏ.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC004", "thoai": raw[3], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Fallacy Refutation Card",
            "du_lieu": "Bác bỏ ngụy biện bù nhìn rơm: STRAWMAN FALLACY REFUTATION. Không phải mọi sân golf đều cần bất động sản để tồn tại.",
            "bo_cuc": "Nền Slate #1E293B, dấu gạch chéo đỏ san hô #EF5350 đè lên định kiến một chiều.",
            "mau_sac": "Điểm nhấn đỏ san hô và xanh ngọc.",
            "overlay": "BOTTOM LEFT | STRAWMAN FALLACY REFUTED"
        },
        {
            "sid": "CH04_SC005", "thoai": raw[4], "mod": "VEO_AI",
            "boi_canh": "Bản đồ kinh tế Đông Nam Á dạng vector 2D trên nền Slate #1E293B: Đường bay phát sáng màu vàng hổ phách #F59E0B nối từ Việt Nam sang Thái Lan.",
            "chu_the": "Góc nhìn địa kinh tế mở rộng, khám phá mô hình thành công thực chứng của quốc gia láng giềng.",
            "camera": "Cinematic slow zoom into Thailand region, ánh sáng ngà kem #FAF7EE.",
            "overlay": "BOTTOM LEFT | REGIONAL TOURISM CLUSTERS"
        },
        {
            "sid": "CH04_SC006a1", "thoai": "Có những sân golf không hề bán một mét vuông đất ở nào,", "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam sân golf quốc tế Black Mountain tại Hua Hin (Thái Lan): Thảm cỏ fairway trải dài tự nhiên ôm trọn sườn đồi, 100% không có nhà ở phân lô.",
            "query": "Black Mountain golf club Hua Hin Thailand aerial drone no villas pure golf",
            "source": "Amazing Thailand / TAT",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC006a2", "thoai": "nhưng vẫn tự nuôi sống bộ máy và tạo ra lợi nhuận khổng lồ.", "mod": "VEO_AI",
            "boi_canh": "Bàn làm việc của giám đốc điều hành sân golf quốc tế: Báo cáo tài chính kiểm toán với dòng EBITDA dương màu xanh lá cây rực rỡ, bên ngoài cửa sổ là khung cảnh sân golf tấp nập golfer phát bóng.",
            "chu_the": "Vị giám đốc mỉm cười tự tin ký tên duyệt báo cáo lợi nhuận vận hành.",
            "camera": "Cinematic slow dolly in, ánh sáng phòng làm việc sang trọng và đĩnh đạc.",
            "overlay": "BOTTOM LEFT | OPERATIONAL SELF-SUFFICIENCY"
        },
        {
            "sid": "CH04_SC007", "thoai": raw[6], "mod": "B_ROLL_REAL",
            "tu_lieu": "Biểu tượng du lịch Thái Lan 'Amazing Thailand' và hình ảnh các giải đấu golf quốc tế Asian Tour tổ chức tại Bangkok và Phuket.",
            "query": "Amazing Thailand golf tourism campaign Asian Tour international event",
            "source": "TAT Tourism Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC008", "thoai": raw[7], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Thailand National Golf Footprint Card",
            "du_lieu": "Thống kê Tổng cục Du lịch Thái Lan (TAT): THAILAND: >300 CHAMPIONSHIP GOLF COURSES đang hoạt động nhộn nhịp.",
            "bo_cuc": "Nền Slate #1E293B, con số 300+ hiển thị to rõ nét viền vàng hổ phách #F59E0B.",
            "mau_sac": "Điểm nhấn vàng hổ phách và xanh lục.",
            "overlay": "BOTTOM LEFT | THAILAND: >300 GOLF COURSES"
        },
        {
            "sid": "CH04_SC009", "thoai": raw[8], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Foreign Currency Revenue Card",
            "du_lieu": "Nguồn thu ngoại tệ quốc gia: THAILAND GOLF TOURISM REVENUE: ~ $2.0 BILLION USD / YEAR.",
            "bo_cuc": "Nền Slate #2A323D, con số $2.0 BILLION USD màu xanh lục Emerald #10B981 phát sáng rực rỡ.",
            "mau_sac": "Điểm nhấn xanh lục và vàng champagne.",
            "overlay": "BOTTOM LEFT | THAILAND: ~ $2.0 BILLION USD/YEAR"
        },
        {
            "sid": "CH04_SC010", "thoai": raw[9], "mod": "VEO_AI",
            "boi_canh": "Các đồng tiền đô la Mỹ và ngoại tệ mạnh xếp lớp trên khay thanh toán tại sảnh clubhouse quốc tế, phản chiếu ánh sáng đèn chùm sang trọng.",
            "chu_the": "Dòng ngoại tệ thực chất từ du khách quốc tế mang lại giá trị gia tăng thực cho đất nước.",
            "camera": "Steady camera shot cận cảnh ngoại tệ và hóa đơn dịch vụ.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC011", "thoai": raw[10], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Mass Tourist Spending Card",
            "du_lieu": "Mức chi tiêu khách du lịch thông thường (IAGTO data): MASS TOURIST DAILY SPENDING: ~ $130 USD / DAY.",
            "bo_cuc": "Nền Slate #1E293B, cột chi tiêu phổ thông màu xám bạc làm mốc so sánh.",
            "mau_sac": "Điểm nhấn xám slate và ngà kem #FAF7EE.",
            "overlay": "BOTTOM LEFT | MASS TOURIST: $130 USD/DAY"
        },
        {
            "sid": "CH04_SC012", "thoai": raw[11], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Golfer Spending Surge Card",
            "du_lieu": "Chi tiêu của du khách chơi golf quốc tế: GOLFER DAILY SPENDING: $400 USD / DAY (GẤP 3 LẦN KHÁCH PHỔ THÔNG).",
            "bo_cuc": "Nền Slate #2A323D, cột chi tiêu golfer cao vút màu xanh lục Emerald #10B981.",
            "mau_sac": "Điểm nhấn xanh lục và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | GOLFER SPENDING: $400 USD/DAY (3X)"
        },
        {
            "sid": "CH04_SC013", "thoai": raw[12], "mod": "VEO_AI",
            "boi_canh": "Golfer quốc tế thanh toán hóa đơn thẻ tín dụng bằng máy POS tại quầy proshop, mua sắm trang phục và đồ lưu niệm cao cấp.",
            "chu_the": "Du khách vui vẻ tương tác với nhân viên thu ngân trong không gian mua sắm hiện đại.",
            "camera": "Cinematic slow dolly in, ánh sáng vàng ấm phản chiếu từ sảnh proshop.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC014", "thoai": raw[13], "mod": "B_ROLL_REAL",
            "tu_lieu": "Lịch trình tour du lịch golf 7–10 ngày của công ty lữ hành quốc tế: Bảng lịch trình chi tiết khám phá các sân golf khác nhau và các điểm du lịch.",
            "query": "golf tour itinerary 7 days brochure tourists travel agency Asia",
            "source": "Golfasian Travel Media",
            "overlay": "BOTTOM LEFT | LENGTH OF STAY: 7 - 10 DAYS"
        },
        {
            "sid": "CH04_SC015", "thoai": raw[14], "mod": "VEO_AI",
            "boi_canh": "Chiếc xe van limousine đưa đón golfer quốc tế rời khỏi sân golf tiến về phía trung tâm thành phố biển về đêm rực rỡ ánh đèn.",
            "chu_the": "Dòng tiền tiếp tục lan tỏa từ sân cỏ ra toàn bộ chuỗi cung ứng dịch vụ đô thị.",
            "camera": "Cinematic slow tracking shot theo đuôi xe limousine trên đại lộ ven biển.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC016", "thoai": raw[15], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cắt ghép 4 khung hình nhịp nhàng: Sảnh khách sạn 5 sao tấp nập khách check-in -> Nhà hàng hải sản cao cấp -> Chuyến bay cất cánh -> Phố mua sắm.",
            "query": "5-star luxury hotel lobby seafood restaurant flight take off montage",
            "source": "Hospitality & Travel Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC017", "thoai": raw[16], "mod": "VEO_AI",
            "boi_canh": "Bản đồ quy hoạch cụm du lịch golf Thái Lan: Các chấm xanh tập trung thành cụm dày đặc quanh các vịnh biển, kết nối cao tốc thông suốt.",
            "chu_the": "Sự quy hoạch tập trung khoa học, triệt tiêu hoàn toàn sự manh mún đơn lẻ.",
            "camera": "Steady camera shot, ánh sáng bản đồ địa kinh tế sắc nét.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC018", "thoai": raw[17], "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam cụm sân golf tại Pattaya và Hua Hin: Các sân golf nằm san sát nhau trong bán kính 20–30km quanh bờ biển.",
            "query": "Pattaya Hua Hin golf cluster aerial highway connectivity Thailand",
            "source": "TAT Media Archive",
            "overlay": "BOTTOM LEFT | TOURISM CLUSTERS: PATTAYA, HUA HIN"
        },
        {
            "sid": "CH04_SC019", "thoai": raw[18], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Michael Porter Cluster Theory Card",
            "du_lieu": "Lý thuyết cụm ngành Michael Porter: PORTER'S CLUSTER THEORY. Sự liên kết địa lý giữa các doanh nghiệp tạo ra sức cạnh tranh toàn cầu.",
            "bo_cuc": "Nền Slate #1E293B, sơ đồ kim cương liên kết 4 đỉnh phát sáng màu xanh lục #10B981.",
            "mau_sac": "Điểm nhấn xanh ngọc và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | MICHAEL PORTER: CLUSTER THEORY"
        },
        {
            "sid": "CH04_SC020", "thoai": raw[19], "mod": "VEO_AI",
            "boi_canh": "Mô hình mạng lưới 5–10 sân golf kết nối xoay quanh một sân bay quốc tế, các đường truyền sáng liên kết nhịp nhàng.",
            "chu_the": "Tính kinh tế theo quy mô bên ngoài (External Economies of Scale) tạo ra sức hút vượt trội.",
            "camera": "Cinematic slow aerial pan shot trên sa bàn mạng lưới cụm.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC021", "thoai": raw[20], "mod": "B_ROLL_REAL",
            "tu_lieu": "Nhóm golfer quốc tế tươi cười thảo luận trước bảng danh mục các sân golf trong khu vực, chuẩn bị xuất phát sang sân tiếp theo.",
            "query": "happy golfers clubhouse patio international tourists morning round",
            "source": "Asian Tour Lifestyle Media",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC022", "thoai": raw[21], "mod": "VEO_AI",
            "boi_canh": "Dải bờ biển duyên hải miền Trung Việt Nam trải dài ngút ngàn dưới ánh nắng ban mai rạng rỡ, làn sóng biển Đông xanh ngọc vỗ về cồn cát trắng.",
            "chu_the": "Hình mẫu thành công thực chứng tại Việt Nam bừng sáng.",
            "camera": "Cinematic epic slow crane up, ánh sáng ban mai nhiệt đới trong trẻo.",
            "overlay": "BOTTOM LEFT | CENTRAL VIETNAM GOLF SUCCESS"
        },
        {
            "sid": "CH04_SC023", "thoai": raw[22], "mod": "B_ROLL_REAL",
            "tu_lieu": "Biển chào đón và logo liên minh du lịch: VIETNAM GOLF COAST khắc trên đá tự nhiên tại các sân golf miền Trung.",
            "query": "Vietnam Golf Coast stone signage Danang coastal golf courses",
            "source": "Vietnam Golf Coast Archive",
            "overlay": "BOTTOM LEFT | VIETNAM GOLF COAST"
        },
        {
            "sid": "CH04_SC024", "thoai": raw[23], "mod": "VEO_AI",
            "boi_canh": "@golf_course_aerial_links.jpg -> Cụm sân golf đẳng cấp thế giới Hoiana Shores, BRG Đà Nẵng, Montgomerie Links và Laguna Lăng Cô nối tiếp nhau dọc bờ biển miền Trung.",
            "chu_the": "Cụm điểm đến du lịch golf đẳng cấp quốc tế vươn tầm thế giới.",
            "camera": "Cinematic slow aerial pan, thảm cỏ fairway uốn lượn cạnh cồn cát tự nhiên.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC025", "thoai": raw[24], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "International Customer Dominance Pie",
            "du_lieu": "Cơ cấu khách hàng Vietnam Golf Coast: 60% - 75% KHÁCH QUỐC TẾ (HÀN QUỐC, NHẬT BẢN, ĐÀI LOAN).",
            "bo_cuc": "Nền Slate #2A323D, mảng khách quốc tế áp đảo màu xanh lục Emerald #10B981.",
            "mau_sac": "Điểm nhấn xanh lục và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | 60% - 75% INTERNATIONAL GOLFERS"
        },
        {
            "sid": "CH04_SC026", "thoai": raw[25], "mod": "B_ROLL_REAL",
            "tu_lieu": "Đoàn golfer người Hàn Quốc và Nhật Bản tươi cười chụp ảnh lưu niệm tại hố golf par-3 nhìn thẳng ra biển Đông xanh ngắt.",
            "query": "Korean Japanese golfers posing smiling coastal golf hole Danang",
            "source": "Danang Tourism Promotion Center",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC027", "thoai": raw[26], "mod": "B_ROLL_REAL",
            "tu_lieu": "Sân golf tại Seoul và Tokyo bị đóng băng dưới tuyết trắng dày đặc, cọc cờ lỗ golf đóng băng và sân ngừng hoạt động trong mùa đông.",
            "query": "golf course covered in heavy snow winter freeze Seoul Tokyo shutdown",
            "source": "KBS / NHK News Archive",
            "overlay": "BOTTOM LEFT | NORTHEAST ASIA WINTER FREEZE"
        },
        {
            "sid": "CH04_SC028", "thoai": raw[27], "mod": "B_ROLL_REAL",
            "tu_lieu": "Các chuyến bay quốc tế từ Seoul và Tokyo liên tục hạ cánh xuống đường băng sân bay quốc tế Đà Nẵng, hành khách mang túi golf ra sảnh đến.",
            "query": "Danang airport terminal Korean arrivals golf bags conveyor belt",
            "source": "Danang International Terminal Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC029", "thoai": raw[28], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "International Round Pricing Card",
            "du_lieu": "Giá dịch vụ vòng chơi quốc tế: INTERNATIONAL ROUND FEE: $120 - $180 USD / ROUND (3.0 - 4.5 triệu VND/vòng chơi).",
            "bo_cuc": "Nền Slate #1E293B, số tiền to rõ ràng kèm icon tiền tệ.",
            "mau_sac": "Điểm nhấn xanh lục và ngà kem #FAF7EE.",
            "overlay": "BOTTOM LEFT | $120 - $180 USD / ROUND"
        },
        {
            "sid": "CH04_SC030", "thoai": raw[29], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Annual Revenue per Course Card",
            "du_lieu": "Doanh thu thường niên mỗi sân miền Trung: ANNUAL REVENUE: 80 - 140 BILLION VND / YEAR nhờ công suất lấp đầy quanh năm.",
            "bo_cuc": "Nền Slate #2A323D, con số doanh thu màu xanh ngọc bích #10B981 phát sáng vững chắc.",
            "mau_sac": "Điểm nhấn xanh ngọc và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | REVENUE: 80 - 140 BILLION VND/YEAR"
        },
        {
            "sid": "CH04_SC031a1", "thoai": "Trừ đi toàn bộ chi phí vận hành,", "mod": "VEO_AI",
            "boi_canh": "Bàn tính kế toán với bảng hạch toán OpEx duy tu cỏ và lương nhân sự được khấu trừ đầy đủ, dòng tiền còn lại vẫn thặng dư lớn.",
            "chu_the": "Kế toán trưởng gạch chân dòng chi phí vận hành đã được thanh toán sòng phẳng.",
            "camera": "Steady camera shot cận cảnh sổ kế toán.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC031a2", "thoai": "mỗi sân tại đây tạo ra dòng tiền dương từ ba mươi đến bảy mươi tỷ đồng mỗi năm.", "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Positive Cash Flow Card",
            "du_lieu": "Dòng tiền vận hành dương tự chủ: POSITIVE OPERATING CASH FLOW: +30 TO +70 BILLION VND / YEAR.",
            "bo_cuc": "Nền Slate #1E293B, con số EBITDA dương màu xanh lục Emerald #10B981 phát sáng rực rỡ.",
            "mau_sac": "Điểm nhấn xanh lục và vàng champagne.",
            "overlay": "BOTTOM LEFT | NET CASH FLOW: +30 TO +70B VND"
        },
        {
            "sid": "CH04_SC032a1", "thoai": "Dòng tiền này đủ để tự trang trải bộ máy,", "mod": "VEO_AI",
            "boi_canh": "Sảnh clubhouse rực rỡ ánh đèn vàng ấm áp, đội ngũ nhân viên và caddie nhận lương thưởng đầy đủ, bộ máy vận hành trơn tru tự chủ.",
            "chu_the": "Không khí làm việc văn minh, tự chủ tài chính không cần bầu sữa ngân sách hay bất động sản.",
            "camera": "Cinematic slow dolly in, ánh sáng ngà kem sang trọng.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC032a2", "thoai": "và hoàn trả vốn đầu tư ban đầu mà không cần dựa dẫm vào bất động sản.", "mod": "VEO_AI",
            "boi_canh": "Đại cảnh hoàng hôn trên sân golf links miền Trung: Thảm cỏ fairway trải dài uốn lượn cạnh bờ biển sóng vỗ thanh bình, độc lập hoàn toàn với các dự án phân lô.",
            "chu_the": "Sự trường tồn của một mô hình kinh tế dịch vụ chân chính.",
            "camera": "Cinematic slow crane up góc rộng, ánh hoàng hôn vàng cam #F59E0B phản chiếu trên biển.",
            "overlay": "BOTTOM LEFT | ZERO REAL ESTATE RELIANCE"
        },
        {
            "sid": "CH04_SC033", "thoai": raw[32], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cận cảnh những dải cồn cát trắng ven biển miền Trung khô cằn trước khi xây sân golf: Cỏ dại xơ xác dưới nắng gió lào bỏng rát.",
            "query": "barren coastal white sand dunes harsh climate Central Vietnam",
            "source": "Vietnam Geography Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC034", "thoai": raw[33], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Land Utility Transformation Card",
            "du_lieu": "Chuyển hóa giá trị đất cát: NÔNG NGHIỆP TRỒNG TRỌT = 0 -> SÂN GOLF LINKS QUỐC TẾ = HÀNG TRIỆU USD NGOẠI TỆ.",
            "bo_cuc": "Nền Slate #1E293B, mũi tên chuyển đổi giá trị màu xanh lục Emerald #10B981.",
            "mau_sac": "Điểm nhấn xanh lục và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | BARREN SAND -> SERVICE EXPORT ENGINE"
        },
        {
            "sid": "CH04_SC035", "thoai": raw[34], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cơn mưa nhiệt đới trút xuống mặt cỏ sân links ven biển, nước mưa thấm nhanh qua lớp cát tự nhiên, mặt sân khô ráo ngay tức thì.",
            "query": "natural sand base drainage heavy rain golf course absorption",
            "source": "USGA Green Section Archive",
            "overlay": "BOTTOM LEFT | -40% LEVELING & DRAINAGE COST"
        },
        {
            "sid": "CH04_SC036", "thoai": raw[35], "mod": "VEO_AI",
            "boi_canh": "Người điều hành đứng trên đỉnh đồi cát ngắm nhìn thảm cỏ xanh mướt trải dài hướng biển, khẳng định tính đúng đắn của quy luật kinh tế.",
            "chu_the": "Phong thái đĩnh đạc của người làm kinh tế thị trường thực chứng.",
            "camera": "Cinematic slow dolly in từ sau lưng chủ thể.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC037", "thoai": raw[36], "mod": "VEO_AI",
            "boi_canh": "Lá cờ quốc tế của các nước và cờ giải đấu World Golf Awards tung bay hiên ngang trước bục vinh danh bên bờ biển miền Trung.",
            "chu_the": "Biểu tượng của ngành xuất khẩu dịch vụ tại chỗ bền vững và uy tín.",
            "camera": "Steady camera shot góc ngước lên nền trời xanh rực rỡ.",
            "overlay": "BOTTOM LEFT | SUSTAINABLE SERVICE EXPORT"
        },
        {
            "sid": "CH04_SC038", "thoai": raw[37], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Location & Model Fit Matrix",
            "du_lieu": "Ma trận phù hợp mô hình & tọa độ: RIGHT MODEL AT RIGHT LOCATION. Sân links ven biển + Sân bay quốc tế + Khí hậu mùa đông ấm áp.",
            "bo_cuc": "Nền Slate #2A323D, điểm giao thoa tối ưu phát sáng màu xanh lục #10B981.",
            "mau_sac": "Điểm nhấn xanh lục và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | RIGHT MODEL AT RIGHT LOCATION"
        },
        {
            "sid": "CH04_SC039", "thoai": raw[38], "mod": "VEO_AI",
            "boi_canh": "Bức tranh đối lập chia đôi màn hình: Một bên là bờ biển nhiệt đới rực rỡ nắng vàng và khách quốc tế; Một bên là dự án sân golf vùng xa heo hút dưới trời u ám xám xịt.",
            "chu_the": "Cú va đập nhận thức sâu sắc giữa mô hình tự chủ thực chất và mô hình đòn bẩy tài chính ảo.",
            "camera": "Cinematic slow pan từ bên sáng sang bên tối, chuẩn bị bước vào Đỉnh cao trào Chương 5.",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC040a1", "thoai": "Không có dòng khách ngoại tệ cứu cánh,", "mod": "B_ROLL_REAL",
            "tu_lieu": "Cổng một dự án sân golf vùng xa khóa xích hoen rỉ, đường đất sạt lở không một bóng người qua lại.",
            "query": "abandoned golf resort gate locked chain remote area Vietnam",
            "source": "Vietnam Investigative News",
            "overlay": "Không."
        },
        {
            "sid": "CH04_SC040a2", "thoai": "những dự án nợ nần ở vùng xa xôi buộc phải đối diện với quy luật chi phí vốn.", "mod": "VEO_AI",
            "boi_canh": "Bảng cân đối kế toán nợ nần với các khoản vay ngân hàng và trái phiếu đến hạn, bánh răng chi phí vốn bắt đầu nghiền nát dự án, mở màn cho Đỉnh cao trào CH05.",
            "chu_the": "Áp lực thời gian và chi phí vốn đè nặng trong không gian xám lạnh.",
            "camera": "Cinematic slow dolly in cận cảnh các hợp đồng nợ đến hạn, ánh sáng xám slate buốt lạnh.",
            "overlay": "BOTTOM LEFT | FACING COST OF CAPITAL REALITY"
        }
    ]
    write_and_export(4, scenes, "CHƯƠNG 4", "THE DEVIL'S CHAPTER: KHI SÂN GOLF TỰ CHỦ NGOẠI TỆ RỰC RỠ")

def generate_ch05():
    raw = get_sentences(5)
    scenes = [
        {
            "sid": "CH05_SC001", "thoai": raw[0], "mod": "VEO_AI",
            "boi_canh": "Sảnh sàn giao dịch tài chính thời kỳ tiền rẻ: Ánh đèn chùm pha lê rực rỡ, dòng người cười nói nâng ly rượu vang, các bảng điện tử nhảy số màu xanh tăng giá liên tục.",
            "chu_the": "Không khí lễ hội tài chính hào nhoáng che giấu các lỗ hổng dòng tiền bên dưới.",
            "camera": "Cinematic slow tracking shot qua đám đông ăn mừng, ánh sáng vàng kim sang trọng nhưng chao đảo nhẹ.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC002", "thoai": raw[1], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Debt Rollover Spiral Card",
            "du_lieu": "Vòng tròn đảo nợ trái phiếu: NEW BOND TRANCHE -> PAY COUPON ON OLD BOND. Vòng xoáy nợ phình to theo cấp số nhân.",
            "bo_cuc": "Nền Slate #1E293B, vòng tròn mũi tên màu cam cảnh báo #FF7043 xoay tròn liên tục.",
            "mau_sac": "Điểm nhấn cam cảnh báo và đỏ san hô #EF5350.",
            "overlay": "BOTTOM LEFT | DEBT ROLLOVER SPIRAL"
        },
        {
            "sid": "CH05_SC003", "thoai": raw[2], "mod": "VEO_AI",
            "boi_canh": "Két sắt tài chính mở toang, bàn tay thủ quỹ lấy các cọc tiền mặt lớn từ dự án nhà ở chuyển sang phong bì chi phí duy tu mặt cỏ sân golf.",
            "chu_the": "Cử chỉ vội vã lo âu của nhân viên kế toán trước sự cạn kiệt của dòng tiền bù chéo.",
            "camera": "Cinematic slow dolly in cận cảnh bàn tay chuyển tiền, ánh sáng đèn bàn xám lạnh.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC004", "thoai": raw[3], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Monetary Cycle Swing Card",
            "du_lieu": "Con lắc chu kỳ tiền tệ vĩ mô: CHEAP MONEY & LOW RATES -> MONETARY TIGHTENING & RATE HIKES.",
            "bo_cuc": "Nền Slate #2A323D, con lắc dao động mạnh mẽ, vạch đo lãi suất tăng dốc đứng.",
            "mau_sac": "Chuyển dịch từ xanh lục sang đỏ san hô #EF5350.",
            "overlay": "BOTTOM LEFT | MONETARY CYCLE REVERSAL"
        },
        {
            "sid": "CH05_SC005", "thoai": raw[4], "mod": "B_ROLL_REAL",
            "tu_lieu": "Họp báo điều hành chính sách tiền tệ của Ngân hàng Trung ương: Thống đốc bước lên bục phát biểu tuyên bố nâng lãi suất điều hành để kiểm soát lạm phát.",
            "query": "central bank press conference interest rate hike governor podium announcement",
            "source": "VTV Thời sự / Bloomberg TV",
            "overlay": "BOTTOM LEFT | RATE HIKES & CREDIT TIGHTENING"
        },
        {
            "sid": "CH05_SC006", "thoai": raw[5], "mod": "VEO_AI",
            "boi_canh": "Bánh răng đồng hồ cơ khí khổng lồ bằng kim loại xước biểu trưng cho chi phí vốn đang quay nghiền nát những tờ hợp đồng tài chính mỏng manh trên nền gạch slate.",
            "chu_the": "Ẩn dụ hiện thực vật lý về sức ép thời gian và lãi suất tích lũy từng giây.",
            "camera": "Cinematic slow dolly in cận cảnh bánh răng quay chậm, tia lửa ma sát nhỏ tóe ra sắc lạnh.",
            "overlay": "BOTTOM LEFT | COST OF CAPITAL PRESSURE"
        },
        {
            "sid": "CH05_SC007", "thoai": raw[6], "mod": "VEO_AI",
            "boi_canh": "Bàn làm việc của giám đốc xử lý nợ xấu ngân hàng: Tập hồ sơ 'Dự Án Sân Golf Độc Lập' dán nhãn niêm phong đỏ, máy tính hiển thị dòng tiền âm kéo dài.",
            "chu_the": "Vị giám đốc khoanh tay nhìn vào tập hồ sơ với nét mặt đăm chiêu.",
            "camera": "Steady camera shot, ánh sáng xám slate #2A323D lạnh lùng nghiêm nghị.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC008", "thoai": raw[7], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Operating Cost Drain Card",
            "du_lieu": "Chi phí duy tu và nhân sự cố định: MAINTENANCE & PAYROLL OPEX: -40 BILLION VND / YEAR. Nước tưới, phân bón, lương 300 lao động.",
            "bo_cuc": "Nền Slate #1E293B, số tiền màu đỏ san hô #EF5350 kèm icon chi phí rõ nét.",
            "mau_sac": "Điểm nhấn đỏ san hô trên nền kem ngà.",
            "overlay": "BOTTOM LEFT | ANNUAL OPEX: -40 BILLION VND"
        },
        {
            "sid": "CH05_SC009", "thoai": raw[8], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Debt Service Obligation Card",
            "du_lieu": "Nghĩa vụ nợ trái phiếu nghìn tỷ: BOND DEBT SERVICE: -160 BILLION VND / YEAR. Lãi coupon 12% trên dư nợ trái phiếu.",
            "bo_cuc": "Nền Slate #2A323D, thanh chi phí nợ cao gấp 4 lần chi phí vận hành.",
            "mau_sac": "Cột nợ phát sáng màu cam cảnh báo #FF7043.",
            "overlay": "BOTTOM LEFT | DEBT SERVICE: -160 BILLION VND"
        },
        {
            "sid": "CH05_SC010", "thoai": raw[9], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Total Cash Drain Equation Card",
            "du_lieu": "Chiếc bẫy tiền mặt thiêu đốt thanh khoản: -40B OPEX + (-160B DEBT) = -200 BILLION VND CASH DRAIN / YEAR (~550 triệu VND/ngày).",
            "bo_cuc": "Nền Slate #1E293B, biểu thức toán học màu đỏ rực rỡ #EF5350.",
            "mau_sac": "Con số -200 tỷ phát sáng chớp nhẹ tạo áp lực kịch tính.",
            "overlay": "BOTTOM LEFT | CASH DRAIN: -200 BILLION VND/YEAR"
        },
        {
            "sid": "CH05_SC011", "thoai": raw[10], "mod": "VEO_AI",
            "boi_canh": "Quầy thu ngân sảnh sân golf vắng bóng người vào buổi trưa: Máy in hóa đơn in ra tờ biên lai mỏng manh vài triệu đồng, đặt cạnh đống hóa đơn nợ chưa trả.",
            "chu_the": "Thu ngân ngồi chống cằm thở dài trong không gian im ắng.",
            "camera": "Cinematic slow dolly in cận cảnh tờ biên lai lẻ loi, ánh sáng dịu buồn.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC012", "thoai": raw[11], "mod": "B_ROLL_REAL",
            "tu_lieu": "Sàn giao dịch bất động sản đại đô thị cửa đóng then cài, các tấm biển quảng cáo mở bán bị bong tróc, văn phòng giao dịch vắng tanh.",
            "query": "frozen real estate market closed real estate office empty showroom Vietnam",
            "source": "VTV Tài chính Kinh doanh / Báo Thanh Niên",
            "overlay": "BOTTOM LEFT | REAL ESTATE MARKET FREEZE"
        },
        {
            "sid": "CH05_SC013", "thoai": raw[12], "mod": "B_ROLL_REAL",
            "tu_lieu": "Bản tin truyền hình tài chính về khủng hoảng thanh khoản trái phiếu doanh nghiệp, khối lượng phát hành mới rơi tự do về mức 0.",
            "query": "corporate bond market freeze default news report investor meeting",
            "source": "VTV Khớp lệnh / Vietnamnet",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC014", "thoai": raw[13], "mod": "VEO_AI",
            "boi_canh": "Đồ thị mô phỏng giải phẫu tài chính doanh nghiệp: Thảm cỏ sân golf bị bao bọc bởi các đường viền nứt nẻ màu đỏ san hô #EF5350, hút cạn dần dòng tiền dự trữ.",
            "chu_the": "Ẩn dụ trực quan về khối u di căn thanh khoản hút cạn tiền mặt doanh nghiệp.",
            "camera": "Cinematic slow zoom in, ánh sáng đỏ cảnh báo nhấp nháy trên nền Slate đen sẫm.",
            "overlay": "BOTTOM LEFT | LIQUIDITY DRAIN CANCER"
        },
        {
            "sid": "CH05_SC015", "thoai": raw[14], "mod": "VEO_AI",
            "boi_canh": "Dàn vòi phun nước tự động vẫn phun xoay tròn trên mặt cỏ sân golf vắng người dưới trời hoàng hôn xám chì, đồng hồ nợ điện tử góc màn hình nhảy số nợ liên tục.",
            "chu_the": "Không gian tĩnh mịch đối lập với tiếng tích tắc dồn dập của đồng hồ nợ vay.",
            "camera": "Steady camera shot, góc máy thấp sát mặt cỏ ướt sũng.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC016", "thoai": raw[15], "mod": "VEO_AI",
            "boi_canh": "Bức ảnh tư liệu lịch sử đen trắng chuyển hóa sang đồ họa editorial 2D: Con phố Ginza sầm uất ngập tràn ánh đèn neon và các tòa tháp tài chính Tokyo năm 1989.",
            "chu_the": "Doanh nhân Nhật Bản trong âu phục sang trọng vẫy xe taxi bằng những tờ tiền 10.000 Yên.",
            "camera": "Cinematic slow tracking shot lướt qua phố Ginza ban đêm, ánh sáng hoài niệm lịch sử.",
            "overlay": "BOTTOM LEFT | JAPAN ASSET BUBBLE (1989 - 1991)"
        },
        {
            "sid": "CH05_SC017", "thoai": raw[16], "mod": "B_ROLL_REAL",
            "tu_lieu": "Thước phim tư liệu đài truyền hình NHK năm 1989: Sàn giao dịch thẻ hội viên golf Tokyo náo nhiệt như sàn chứng khoán, nhân viên môi giới gào thét vào điện thoại.",
            "query": "Tokyo golf membership exchange floor trading frenzy 1989 NHK archive",
            "source": "NHK Japan Historical Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC018", "thoai": raw[17], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Koganei Peak Valuation Card",
            "du_lieu": "Đỉnh cao bong bóng thẻ golf Koganei (Tokyo): KOGANEI GOLF MEMBERSHIP PEAK: 400 MILLION YEN (~$3.0 MILLION USD IN 1989).",
            "bo_cuc": "Nền Slate #1E293B, con số 400 triệu Yên mạ vàng kim rực rỡ #F8D469.",
            "mau_sac": "Điểm nhấn vàng kim lấp lánh rồi chững lại ở đỉnh dốc.",
            "overlay": "BOTTOM LEFT | KOGANEI: 400M YEN ($3M USD) IN 1989"
        },
        {
            "sid": "CH05_SC019", "thoai": raw[18], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cổng vào cổ kính sang trọng của câu lạc bộ golf Koganei Country Club tại Tokyo, những chiếc xe sang cổ điển nối đuôi nhau vào sân.",
            "query": "Koganei country club Tokyo entrance luxury vintage cars Japan 1989",
            "source": "Kyodo News Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC020", "thoai": raw[19], "mod": "VEO_AI",
            "boi_canh": "Quầy giao dịch tín dụng ngân hàng lớn tại Tokyo năm 1989: Tấm thẻ hội viên golf mạ vàng đặt trang trọng bên cạnh hợp đồng vay nợ hàng trăm tỷ Yên.",
            "chu_the": "Cán bộ ngân hàng cúi đầu chào khách hàng vay nợ đầy tôn kính.",
            "camera": "Steady camera shot, ánh sáng vàng ấm phản chiếu từ tấm thẻ mạ vàng.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC021", "thoai": raw[20], "mod": "B_ROLL_REAL",
            "tu_lieu": "Thống đốc Ngân hàng Trung ương Nhật Bản Yasushi Mieno xuất hiện trên truyền hình tuyên bố tăng lãi suất chiết khấu mạnh tay để dập tắt bong bóng năm 1990.",
            "query": "Bank of Japan governor Yasushi Mieno interest rate hike announcement 1990",
            "source": "Bank of Japan / NHK Archive",
            "overlay": "BOTTOM LEFT | BOJ TIGHTENING: BUBBLE BURSTS"
        },
        {
            "sid": "CH05_SC022", "thoai": raw[21], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Nikkei Golf Membership Collapse Chart",
            "du_lieu": "@nikkei_bubble_golf_chart.jpg -> Đồ thị chỉ số giá thẻ golf Nikkei 1989–1995: NIKKEI GOLF INDEX COLLAPSE: -90% TO -95% DROP.",
            "bo_cuc": "Nền Slate sẫm #0F172A, đường line đỏ san hô #EF5350 cắm thẳng đứng xuống đáy.",
            "mau_sac": "Đường line đỏ rơi dồn dập kèm vệt khói tan biến.",
            "overlay": "BOTTOM LEFT | NIKKEI GOLF INDEX: -95% COLLAPSE"
        },
        {
            "sid": "CH05_SC023", "thoai": raw[22], "mod": "VEO_AI",
            "boi_canh": "Tấm thẻ hội viên mạ vàng từng có giá triệu USD nằm rơi trên sàn nhà phủ đầy bụi bặm trong một văn phòng phá sản bị niêm phong.",
            "chu_the": "Hình ảnh tĩnh vật gợi sự sụp đổ bẽ bàng của các ván cược tài chính ảo.",
            "camera": "Cinematic slow dolly in sát mặt sàn, ánh sáng xám tro hiu hắt.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC024", "thoai": raw[23], "mod": "B_ROLL_REAL",
            "tu_lieu": "Tòa án Tokyo thụ lý các đơn xin phá sản của doanh nghiệp sân golf đầu thập niên 1990, luật sư và chủ nợ bước ra với nét mặt nặng trĩu.",
            "query": "Tokyo district court bankruptcy filing golf course operators 1990s",
            "source": "Kyodo News / NHK",
            "overlay": "BOTTOM LEFT | HUNDREDS OF OPERATORS BANKRUPT"
        },
        {
            "sid": "CH05_SC025", "thoai": raw[24], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Banking Non-Performing Loans Shock Card",
            "du_lieu": "Nợ xấu ngân hàng Nhật Bản: JAPANESE BANKING BAD DEBT: > $100 BILLION USD xuất phát từ tài sản bảo đảm sân golf và bất động sản.",
            "bo_cuc": "Nền Slate #1E293B, con số $100 BILLION USD hiển thị to bản viền đỏ rực rỡ #EF5350.",
            "mau_sac": "Cảnh báo khủng hoảng hệ thống tài chính kéo dài.",
            "overlay": "BOTTOM LEFT | GOLF BAD DEBT: > $100 BILLION USD"
        },
        {
            "sid": "CH05_SC026", "thoai": raw[25], "mod": "B_ROLL_REAL",
            "tu_lieu": "Thước phim tài liệu cảnh các sân golf bị bỏ hoang tại vùng ngoại ô Nhật Bản: Máy cắt cỏ hoen rỉ trong kho ẩm mốc, cỏ dại mọc cao quá đầu người.",
            "query": "abandoned golf course Japan overgrown grass rusty machinery documentary",
            "source": "NHK Special Documentary",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC027", "thoai": raw[26], "mod": "VEO_AI",
            "boi_canh": "Cây cờ golf rách tã bay phần phật trong cơn gió bão trên đỉnh đồi trơ trọi, mặt trời xám xịt chìm vào đám mây đen giông bão phía chân trời.",
            "chu_the": "Hình tượng tĩnh lặng phản chiếu bài học quy luật muôn đời của tài chính.",
            "camera": "Cinematic slow tracking shot góc thấp, gió thổi bụi cát bay nhẹ.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC028", "thoai": raw[27], "mod": "VEO_AI",
            "boi_canh": "Chiếc cúp vô địch bằng pha lê sáng lấp lánh đặt trước bức tường kính phản chiếu toàn cảnh một đại đô thị rực rỡ phồn hoa.",
            "chu_the": "Biểu tượng của sự hào nhoáng trong chu kỳ tăng trưởng tiền rẻ.",
            "camera": "Steady camera shot cận cảnh pha lê phản chiếu ánh đèn vàng ấm.",
            "overlay": "BOTTOM LEFT | CHEAP MONEY: GLAMOROUS COLLATERAL"
        },
        {
            "sid": "CH05_SC029", "thoai": raw[28], "mod": "B_ROLL_REAL",
            "tu_lieu": "Phát mại tài sản thế chấp tại trung tâm đấu giá nợ xấu: Danh sách các dự án sân golf bị đấu giá nhiều lần với giá khởi điểm giảm sâu nhưng không có người mua.",
            "query": "debt auction bank foreclosed property auction floor no bidders Vietnam",
            "source": "Asset Liquidation Archive",
            "overlay": "BOTTOM LEFT | WORST LIQUIDATION ASSET"
        },
        {
            "sid": "CH05_SC030", "thoai": raw[29], "mod": "VEO_AI",
            "boi_canh": "Phòng họp của một quỹ đầu tư cơ hội: Các nhà quản lý quỹ lướt qua hồ sơ dự án sân golf bị siết nợ, đồng loạt lắc đầu và gạt sang một bên.",
            "chu_the": "Quyết định dứt khoát từ chối mua lại cỗ máy ngốn tiền mặt OpEx.",
            "camera": "Cinematic slow dolly out, ánh sáng phòng họp xám slate #1E293B lạnh lùng thực dụng.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC031", "thoai": raw[30], "mod": "VEO_AI",
            "boi_canh": "Chiếc chuông đồng lớn đặt trên nóc tòa nhà cơ quan quản lý nhà nước ngân vang từng hồi chuông trầm hùng, chim bồ câu tung cánh bay lên bầu trời.",
            "chu_the": "Ẩn dụ thời khắc tỉnh thức của thể chế quản lý nhà nước.",
            "camera": "Cinematic slow tilt up từ thân chuông lên nền trời xanh, ánh sáng mặt trời rọi qua.",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC032", "thoai": raw[31], "mod": "B_ROLL_REAL",
            "tu_lieu": "Phiên chất vấn sôi nổi tại nghị trường Quốc hội: Đại biểu Quốc hội bày tỏ lo ngại sâu sắc về tình trạng dự án treo, ôm đất đai hoang hóa gây lãng phí nguồn lực.",
            "query": "National Assembly questioning session land use waste debate Vietnam",
            "source": "Truyền hình Quốc hội / VTV1",
            "overlay": "Không."
        },
        {
            "sid": "CH05_SC033", "thoai": raw[32], "mod": "VEO_AI",
            "boi_canh": "Bàn làm việc của các nhà lập pháp với dự thảo Luật Đất đai mới dày cộp, chiếc bút ký kim loại sẵn sàng đặt cạnh văn bản, tạo cầu nối sang CH06.",
            "chu_the": "Sự chuyển dịch dứt khoát của pháp luật sang kỷ nguyên minh bạch sòng phẳng.",
            "camera": "Cinematic slow dolly in cận cảnh trang bìa Luật Đất Đai mới, ánh sáng ngà kem #FAF7EE nghiêm cẩn.",
            "overlay": "BOTTOM LEFT | INSTITUTIONAL RESTRUCTURING"
        }
    ]
    write_and_export(5, scenes, "CHƯƠNG 5", "⚡ ĐỈNH CAO TRÀO: TỬ HUYỆT THANH KHOẢN VÀ VẾT XE ĐỔ NHẬT BẢN")

if __name__ == "__main__":
    generate_ch04()
    generate_ch05()
