#!/usr/bin/env python3
"""
Generate Chapters 02 and 03 with exact sentence matching and full I2V+ compliance.
"""

from build_full_i2vplus_pipeline import get_sentences, write_and_export

def generate_ch02():
    raw = get_sentences(2)
    scenes = [
        {
            "sid": "CH02_SC001", "thoai": raw[0], "mod": "VEO_AI",
            "boi_canh": "@david_ricardo_portrait.jpg -> A 2D warm cinematic editorial illustration of David Ricardo seated in a classical 19th-century study room with antique leather-bound books on a mahogany desk.",
            "chu_the": "Nhà kinh tế học ngồi trầm ngâm bên bàn nghiên cứu, ánh mắt sâu sắc nhìn về phía trước.",
            "camera": "Steady camera shot, ánh sáng vàng ấm cổ điển, viền mực thanh thoát trang nhã.",
            "overlay": "BOTTOM LEFT | DAVID RICARDO: LAND RENT"
        },
        {
            "sid": "CH02_SC002", "thoai": raw[1], "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam bay qua vùng đất cằn cỗi ngoại ô ven đô chưa phát triển, lau sậy thưa thớt bên đường đất.",
            "query": "barren rural land outskirts Hanoi Saigon agricultural plot drone",
            "source": "TTXVN / Rural Land Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC003", "thoai": raw[2], "mod": "VEO_AI",
            "boi_canh": "@ban_do_quy_hoach_biet_thu_golf.jpg -> Bản vẽ quy hoạch 1/500 đại đô thị trải rộng trên bàn làm việc, các dải biệt thự viền vàng hổ phách ôm trọn lõi sân golf màu xanh ngọc.",
            "chu_the": "Kiến trúc sư dùng bút chì vạch đường kết nối cảnh quan trực diện từ biệt thự ra fairway.",
            "camera": "Cinematic slow dolly in từ trên cao nhìn xuống bản vẽ, ánh sáng ngà kem #FAF7EE sắc nét.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC004", "thoai": raw[3], "mod": "B_ROLL_REAL",
            "tu_lieu": "Phòng họp tập đoàn bất động sản lớn: Ban lãnh đạo thảo luận căng thẳng trước màn hình trình chiếu sa bàn đại đô thị 200 ha.",
            "query": "corporate real estate board meeting Vietnam mega project master plan",
            "source": "Forbes Vietnam / Báo Đầu Tư",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC005", "thoai": raw[4], "mod": "VEO_AI",
            "boi_canh": "Góc nhìn từ ban công kính một căn biệt thự mẫu nhìn ra bãi đất trống, câu hỏi định giá treo lơ lửng trong tâm trí nhà đầu tư.",
            "chu_the": "Nhà đầu tư đứng khoanh tay trầm ngâm nhìn về phía chân trời đô thị.",
            "camera": "Cinematic slow dolly forward, ánh nắng chiều dịu nhẹ.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC006", "thoai": raw[5], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Amenity Anchor Conceptual Card",
            "du_lieu": "Thẻ mỏ neo cảnh quan: GOLF COURSE AS AN AMENITY ANCHOR. Sân golf 18 lỗ ở lõi nâng trần giá trị cho toàn bộ khu đô thị vệ tinh.",
            "bo_cuc": "Nền Slate #1E293B, biểu tượng mỏ neo vàng hổ phách #F59E0B tỏa ánh sáng xanh sang các khối nhà xung quanh.",
            "mau_sac": "Điểm nhấn vàng hổ phách và xanh lục Emerald #10B981.",
            "overlay": "BOTTOM LEFT | AMENITY ANCHOR INFRASTRUCTURE"
        },
        {
            "sid": "CH02_SC007", "thoai": raw[6], "mod": "VEO_AI",
            "boi_canh": "Đại cảnh flycam 80 ha thảm cỏ fairway xanh ngắt uốn lượn u tịch, tuyệt đối không có bất kỳ khối bê tông nhà ở nào bên trong ranh giới sân.",
            "chu_the": "Xe điện golf cart di chuyển chậm rãi trên đường nội bộ, bảo tồn 100% không gian mở.",
            "camera": "Cinematic slow aerial pan, ánh nắng ban mai rọi trên thảm cỏ xanh mướt.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC008", "thoai": raw[7], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "CapEx vs Operating Loss Card",
            "du_lieu": "Thẻ chi phí chấp nhận đánh đổi: CapEx xây sân: 1,000 - 1,200 tỷ VND; Lỗ vận hành: vài tỷ VND/năm.",
            "bo_cuc": "Nền Slate #2A323D, hai cột chi phí màu đỏ san hô #EF5350 được đặt trong khung kiểm soát.",
            "mau_sac": "Điểm nhấn đỏ san hô và xám slate.",
            "overlay": "BOTTOM LEFT | CAPEX: 1,000B - 1,200B VND"
        },
        {
            "sid": "CH02_SC009", "thoai": raw[8], "mod": "VEO_AI",
            "boi_canh": "Góc nhìn từ phòng khách biệt thự sang trọng qua vách kính panorama ra thảm cỏ fairway xanh ngút ngàn, tạo cảm giác một công viên tư gia vĩnh cửu.",
            "chu_the": "Cư dân thảnh thơi thưởng trà sáng bên khung cửa kính trong suốt.",
            "camera": "Steady camera shot, ánh sáng ngà kem #FAF7EE ngập tràn phòng khách.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC010", "thoai": raw[9], "mod": "B_ROLL_REAL",
            "tu_lieu": "Hội thảo báo cáo thị trường bất động sản của Savills & CBRE tại khách sạn 5 sao, chuyên gia quốc tế phân tích dữ liệu trên màn hình lớn.",
            "query": "Savills CBRE real estate presentation luxury villas Vietnam",
            "source": "Savills Vietnam Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC011", "thoai": raw[10], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Golf Premium Price Surge Chart",
            "du_lieu": "Biểu đồ cột so sánh: Biệt thự thường (100%) vs Biệt thự view sân golf (+20% đến +50% GOLF PREMIUM).",
            "bo_cuc": "Nền Slate #1E293B, cột giá golf view vươn cao với dải thặng dư màu vàng hổ phách #F59E0B.",
            "mau_sac": "Điểm nhấn vàng hổ phách và xanh lục.",
            "overlay": "BOTTOM LEFT | GOLF PREMIUM: +20% TO +50%"
        },
        {
            "sid": "CH02_SC012", "thoai": raw[11], "mod": "VEO_AI",
            "boi_canh": "Chuyên gia tài chính bất động sản đứng trước bảng phân tích đồ thị, ngón tay chỉ vào khoảng chênh lệch giá trị mang tên 'Golf Premium'.",
            "chu_the": "Phong thái chuyên gia đĩnh đạc, phân tích dòng tiền lạnh lùng và minh bạch.",
            "camera": "Cinematic slow dolly in, ánh sáng phòng nghiên cứu sang trọng.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC013", "thoai": raw[12], "mod": "VEO_AI",
            "boi_canh": "Bàn làm việc với máy tính hiển thị mô hình tài chính 200 ha đại đô thị, con số diện tích và doanh thu hiện rõ trên màn hình.",
            "chu_the": "Chuyên viên phân tích nhập các tham số diện tích sàn và giá bán vào bảng tính.",
            "camera": "Steady camera shot cận cảnh màn hình và các công thức toán tài chính.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC014", "thoai": raw[13], "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam toàn cảnh đại đô thị sinh thái ven sông đang xây dựng: 120 ha phân khu nhà ở biệt thự bao quanh lõi công viên hồ nước và sân golf.",
            "query": "aerial view master planned community villas construction Vietnam",
            "source": "Vietnam Property Media",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC015", "thoai": raw[14], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Baseline Price Comparison Card",
            "du_lieu": "Giá bán cơ sở khi không có sân golf: BASELINE PRICE: 40 MILLION VND / M2.",
            "bo_cuc": "Nền Slate #2A323D, thanh đo giá ngang màu xám bạc chuẩn mực.",
            "mau_sac": "Điểm nhấn xám slate và ngà kem #FAF7EE.",
            "overlay": "BOTTOM LEFT | BASELINE: 40 MILLION VND/M2"
        },
        {
            "sid": "CH02_SC016", "thoai": raw[15], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Golf Premium Surge Card",
            "du_lieu": "Giá bán tăng thêm khi có sân golf: +30% SURGE -> 52 MILLION VND / M2. Thặng dư +12 triệu VND trên mỗi mét vuông sàn.",
            "bo_cuc": "Nền Slate #1E293B, cột giá vọt lên 52 triệu VND phát sáng màu xanh lục #10B981.",
            "mau_sac": "Điểm nhấn xanh lục và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | GOLF VIEW: 52 MILLION VND/M2 (+30%)"
        },
        {
            "sid": "CH02_SC017", "thoai": raw[16], "mod": "B_ROLL_REAL",
            "tu_lieu": "Lễ mở bán đại đô thị golf tại trung tâm hội nghị: Bảng điện tử thông báo số lượng căn đặt cọc và tổng giá trị giao dịch bùng nổ.",
            "query": "luxury real estate launch event sales volume electronic board Vietnam",
            "source": "Bất Động Sản TV / VTV",
            "overlay": "BOTTOM LEFT | REVENUE SURPLUS: +3,600 BILLION VND"
        },
        {
            "sid": "CH02_SC018", "thoai": raw[17], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "CapEx Absorption Balance Scale",
            "du_lieu": "Cán cân thặng dư nuốt trọn CapEx: Thặng dư BĐS +3,600 tỷ VND đè bẹp chi phí xây sân 1,200 tỷ VND. Thặng dư ròng +2,400 tỷ VND.",
            "bo_cuc": "Nền Slate #1E293B, hai đĩa cân so sánh trực quan, số liệu minh bạch 100%.",
            "mau_sac": "Thặng dư xanh lục #10B981 áp đảo hoàn toàn chi phí xây sân đỏ san hô.",
            "overlay": "BOTTOM LEFT | SURPLUS ABSORBS 100% CAPEX"
        },
        {
            "sid": "CH02_SC019", "thoai": raw[18], "mod": "VEO_AI",
            "boi_canh": "Báo cáo tài chính hợp nhất của tập đoàn mẹ mở ra trang kết quả kinh doanh với dòng lợi nhuận thặng dư hơn 2.000 tỷ đồng được khoanh tròn xanh.",
            "chu_the": "Giám đốc tài chính mỉm cười nhẹ đóng tập hồ sơ trong sự thỏa mãn của bài toán kinh tế học địa tô.",
            "camera": "Cinematic slow dolly in, ánh sáng ngà kem #FAF7EE sang trọng.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC020", "thoai": raw[19], "mod": "VEO_AI",
            "boi_canh": "Dàn máy cắt cỏ tự động 5 lưỡi xoay đang cắt tỉa thảm cỏ fairway lúc bình minh, một hóa đơn chi phí bảo dưỡng vài tỷ nhỏ bé đặt cạnh biểu đồ thặng dư nghìn tỷ.",
            "chu_the": "Hoạt động chăm sóc mặt cỏ diễn ra nhịp nhàng, coi chi phí bảo dưỡng như hạt cát trong đại dương lợi nhuận.",
            "camera": "Cinematic slow tracking shot theo hướng di chuyển của dàn máy cắt cỏ.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC021", "thoai": raw[20], "mod": "B_ROLL_REAL",
            "tu_lieu": "Đội ngũ nhân viên cảnh quan và vệ sinh đô thị đang chăm sóc cây xanh, cắt cỏ công viên và quét dọn đường nội khu đại đô thị.",
            "query": "landscape maintenance workers tending urban park lawns Vietnam",
            "source": "Urban Living Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC022", "thoai": raw[21], "mod": "VEO_AI",
            "boi_canh": "Quầy vé green fee tại sảnh clubhouse yên ắng, không khí không hề có áp lực phải bán vé bằng mọi giá để bù đắp chi phí vốn.",
            "chu_the": "Nhân viên lễ tân thảnh thơi kiểm tra máy tính trong không gian sang trọng tĩnh lặng.",
            "camera": "Steady camera shot, ánh sáng sảnh đá cẩm thạch dịu mắt.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC023", "thoai": raw[22], "mod": "VEO_AI",
            "boi_canh": "Biểu tượng chiếc mỏ neo lớn bằng đồng thau sáng bóng đặt trước sa bàn quy hoạch đại đô thị, phản chiếu ánh đèn vàng ấm áp.",
            "chu_the": "Biểu tượng tĩnh lặng đĩnh đạc khẳng định vai trò hạ tầng cảnh quan giữ nhịp.",
            "camera": "Steady camera shot cận cảnh biểu tượng mỏ neo trên nền đá slate.",
            "overlay": "BOTTOM LEFT | VALUE-GENERATING COST CENTER"
        },
        {
            "sid": "CH02_SC024a1", "thoai": "Nếu chỉ nhìn vào bảng lỗ của công ty quản lý sân,", "mod": "B_ROLL_REAL",
            "tu_lieu": "Cận cảnh trang báo cáo tài chính công ty con vận hành sân golf với dòng lợi nhuận âm màu đỏ trên bàn kiểm toán.",
            "query": "financial audit report paper negative operating income red ink",
            "source": "Vietnam Audit News",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC024a2", "thoai": "chúng ta sẽ bỏ lỡ cỗ máy sinh lời thực sự của tập đoàn mẹ.", "mod": "B_ROLL_REAL",
            "tu_lieu": "Tòa tháp trụ sở tập đoàn bất động sản mẹ cao chọc trời rực rỡ ánh đèn kính về đêm tại trung tâm tài chính.",
            "query": "corporate skyscraper headquarters modern glass tower night Vietnam",
            "source": "Vietnam Financial Center Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC025", "thoai": raw[24], "mod": "VEO_AI",
            "boi_canh": "Bảng điện tử thị trường bất động sản với các thanh đo thanh khoản giao dịch, phản chiếu sự phụ thuộc vào sức mua của nền kinh tế.",
            "chu_the": "Nhà đầu tư theo dõi nhịp đập thanh khoản thị trường với ánh mắt tỉnh táo.",
            "camera": "Cinematic slow dolly in, ánh sáng màn hình điện tử hiện đại.",
            "overlay": "Không."
        },
        {
            "sid": "CH02_SC026", "thoai": raw[25], "mod": "VEO_AI",
            "boi_canh": "Bàn thẩm định tín dụng với ánh đèn huỳnh quang lạnh, tập hồ sơ 'Dự Án Sân Golf Vùng Xa' đặt cạnh hợp đồng thế chấp đất, tạo cầu nối sang CH03.",
            "chu_the": "Cán bộ thẩm định đóng dấu đỏ dứt khoát lên tập hồ sơ tín dụng.",
            "camera": "Cinematic slow tilt up từ con dấu đỏ lên ánh mắt nghiêm nghị của người thẩm định.",
            "overlay": "Không."
        }
    ]
    write_and_export(2, scenes, "CHƯƠNG 2", "CỖ MÁY MỎ NEO ĐỊA TÔ: THÁO NGÒI NỔ LỖ BẰNG BIỆT THỰ")

def generate_ch03():
    raw = get_sentences(3)
    scenes = [
        {
            "sid": "CH03_SC001", "thoai": raw[0], "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam góc rộng bay qua một thung lũng đồi núi hẻo lánh xa xôi, đất đai cằn cỗi hoàn toàn không có đường nhựa hay khu dân cư cao cấp.",
            "query": "remote barren mountainous valley rural landscape Vietnam undeveloped",
            "source": "TTXVN / Geography Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC002", "thoai": raw[1], "mod": "VEO_AI",
            "boi_canh": "Ngôi làng miền núi đơn sơ với những mái nhà ngói cũ và người dân địa phương đang làm nương rẫy, không hề có nhu cầu hay khả năng mua biệt thự nghỉ dưỡng.",
            "chu_the": "Người dân canh tác nương rẫy bình dị, đối lập hoàn toàn với lối sống xa hoa.",
            "camera": "Cinematic slow tracking shot ngang qua sườn đồi, ánh nắng ban mai dịu mát.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC003", "thoai": raw[2], "mod": "VEO_AI",
            "boi_canh": "Phòng họp ban lãnh đạo doanh nghiệp tài chính: Bản đồ quy hoạch sân golf 18 lỗ ở vùng sâu được trải rộng, không có bất kỳ căn biệt thự nào trên bản vẽ.",
            "chu_the": "Chủ tịch doanh nghiệp ngồi suy tư gõ nhẹ ngón tay lên xấp hồ sơ dự án.",
            "camera": "Cinematic slow dolly in, ánh sáng phòng họp xám slate #1E293B đĩnh đạc.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC004", "thoai": raw[3], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Collateral Mechanism Diagram",
            "du_lieu": "Cơ chế tài sản bảo đảm: BANK COLLATERAL ASSET MECHANISM. Biến quyền sử dụng đất dự án thành hạn mức tín dụng ngân hàng.",
            "bo_cuc": "Nền Slate #1E293B, biểu tượng két sắt ngân hàng và quyền tài sản kết nối bằng mũi tên vàng hổ phách #F59E0B.",
            "mau_sac": "Điểm nhấn vàng hổ phách và xanh lục.",
            "overlay": "BOTTOM LEFT | BANK COLLATERAL MECHANISM"
        },
        {
            "sid": "CH03_SC005", "thoai": raw[4], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cận cảnh mảnh đất nông nghiệp bạc màu ở vùng sâu, cọc mốc ranh giới bằng bê tông đơn sơ cắm giữa cỏ tranh.",
            "query": "rural agricultural land plot concrete boundary marker Vietnam",
            "source": "Vietnam Land News",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC006", "thoai": raw[5], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Raw Land Valuation Card",
            "du_lieu": "Giá trị đất thô nông nghiệp 100 ha: RAW LAND VALUE: ~300 - 400 BILLION VND.",
            "bo_cuc": "Nền Slate #2A323D, cột giá trị nhỏ gọn ở mức đáy bảng.",
            "mau_sac": "Điểm nhấn xám slate và ngà kem #FAF7EE.",
            "overlay": "BOTTOM LEFT | RAW LAND VALUE: ~400 BILLION VND"
        },
        {
            "sid": "CH03_SC007", "thoai": raw[6], "mod": "VEO_AI",
            "boi_canh": "Quầy thẩm định tín dụng ngân hàng: Cán bộ ngân hàng lật giở cuốn sổ đỏ đất nông nghiệp và chỉ tay vào hạn mức cho vay tối đa chỉ hơn 200 tỷ đồng.",
            "chu_the": "Thẩm định viên giữ nguyên tắc an toàn tín dụng nghiêm ngặt đối với đất nông nghiệp.",
            "camera": "Steady camera shot, ánh sáng văn phòng hành chính minh bạch.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC008", "thoai": raw[7], "mod": "VEO_AI",
            "boi_canh": "Bàn làm việc của chuyên gia kỹ thuật tài chính (Financial Engineer): Bút dạ quang và máy tính bảng hiển thị các mô hình định giá dự án phức tạp.",
            "chu_the": "Chuyên gia mỉm cười tự tin khởi động phần mềm mô phỏng dòng tiền chiết khấu.",
            "camera": "Cinematic slow dolly in cận cảnh bàn tay và máy tính bảng.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC009", "thoai": raw[8], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "DCF Formula Card",
            "du_lieu": "Mô hình chiết khấu dòng tiền tương lai: DISCOUNTED CASH FLOW (DCF) MODEL. Chiết khấu tổng dòng tiền 50 năm về giá trị hiện tại ròng.",
            "bo_cuc": "Nền Slate #1E293B, công thức toán tài chính và các tham số chiết khấu hiển thị sắc nét.",
            "mau_sac": "Điểm nhấn xanh ngọc Cyan #00C2CB và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | DCF VALUATION MODEL"
        },
        {
            "sid": "CH03_SC010", "thoai": raw[9], "mod": "B_ROLL_REAL",
            "tu_lieu": "Văn bản quyết định chủ trương đầu tư dự án sân golf thời hạn 50 năm đóng dấu đỏ của Ủy ban nhân dân tỉnh.",
            "query": "official investment approval document red seal provincial committee Vietnam",
            "source": "Government Legal Archive",
            "overlay": "BOTTOM LEFT | 50-YEAR INVESTMENT LICENSE"
        },
        {
            "sid": "CH03_SC011", "thoai": raw[10], "mod": "VEO_AI",
            "boi_canh": "Tập hồ sơ thẩm định giá dày hàng trăm trang với các biểu đồ dự báo doanh thu tăng trưởng đều đặn suốt 50 năm.",
            "chu_the": "Chuyên viên thẩm định lật từng trang với các tham số giả định màu hồng.",
            "camera": "Cinematic slow dolly in cận cảnh các dòng số liệu dự phóng.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC012", "thoai": raw[11], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Perpetual 100% Occupancy Assumption Card",
            "du_lieu": "Giả định công suất tối đa: ASSUMPTION 1: 100% CAPACITY (360 DAYS/YEAR FOR 50 YEARS).",
            "bo_cuc": "Nền Slate #2A323D, thanh đo công suất kịch kim màu vàng hổ phách #F59E0B.",
            "mau_sac": "Điểm nhấn vàng hổ phách và cam cảnh báo.",
            "overlay": "BOTTOM LEFT | ASSUMPTION: 100% CAPACITY (50 YEARS)"
        },
        {
            "sid": "CH03_SC013", "thoai": raw[12], "mod": "B_ROLL_REAL",
            "tu_lieu": "Lễ công bố bán thẻ hội viên danh dự VIP của sân golf: Tấm thẻ mạ vàng sáng bóng được trao cho khách hàng trong ánh đèn flash rực rỡ.",
            "query": "VIP golf club membership card launch gala event Vietnam",
            "source": "Vietnam Golf Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC014", "thoai": raw[13], "mod": "VEO_AI",
            "boi_canh": "Màn hình máy tính hiển thị biểu đồ dòng tiền kỳ vọng được thổi phồng lên mức dốc đứng, màu xanh ngọc rực rỡ.",
            "chu_the": "Cử chỉ kéo chuột điều chỉnh tham số khiến tổng dòng tiền tương lai tăng vọt.",
            "camera": "Steady camera shot cận cảnh màn hình máy tính.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC015", "thoai": raw[14], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Valuation Inflation Waterfall",
            "du_lieu": "Thổi phồng định giá: ĐẤT THÔ 400 TỶ VND -> ĐỊNH GIÁ DCF 50 NĂM: 3,000 TỶ VND (TĂNG GẤP 7.5 LẦN).",
            "bo_cuc": "Nền Slate #1E293B, cột định giá 3.000 tỷ vọt cao với viền cam cảnh báo #FF7043.",
            "mau_sac": "Điểm nhấn cam cảnh báo và xanh ngọc.",
            "overlay": "BOTTOM LEFT | VALUATION SURGE: 400B -> 3,000B VND"
        },
        {
            "sid": "CH03_SC016", "thoai": raw[15], "mod": "B_ROLL_REAL",
            "tu_lieu": "Trụ sở ngân hàng thương mại lớn: Khách hàng doanh nghiệp ký kết hợp đồng tín dụng hạn mức 1.800 tỷ đồng tại phòng họp VIP.",
            "query": "corporate bank credit contract signing ceremony headquarters Vietnam",
            "source": "Banking News Archive",
            "overlay": "BOTTOM LEFT | BANK DEBT CREDIT: 1,800 BILLION VND"
        },
        {
            "sid": "CH03_SC017", "thoai": raw[16], "mod": "VEO_AI",
            "boi_canh": "Kho tiền ngân hàng với các cọc tiền mặt lớn niêm phong được đóng gói, đối chiếu với công trường tạo hình sân cỏ chỉ tốn một phần nhỏ kinh phí.",
            "chu_the": "Sự chênh lệch khổng lồ giữa tiền giải ngân và chi phí thi công thực tế.",
            "camera": "Cinematic slow dolly out, ánh sáng tương phản giữa vàng kim tiền mặt và xám đất công trường.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC018", "thoai": raw[17], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Capital Diversion Flowchart",
            "du_lieu": "Dòng vốn thặng dư chuyển dịch: VAY 1,800 TỶ -> THI CÔNG SÂN 300 TỶ -> ĐIỀU CHUYỂN MẢNG KHÁC 1,500 TỶ VND.",
            "bo_cuc": "Nền Slate #2A323D, mũi tên điều chuyển vốn màu vàng hổ phách #F59E0B chia sang các công ty con.",
            "mau_sac": "Điểm nhấn vàng hổ phách và xanh lục.",
            "overlay": "BOTTOM LEFT | CAPITAL DIVERSION: 1,500 BILLION VND"
        },
        {
            "sid": "CH03_SC019", "thoai": raw[18], "mod": "VEO_AI",
            "boi_canh": "Chiếc đòn bẩy tài chính bằng thép sáng bóng đặt trên bản đồ quy hoạch dự án, nâng bổng khối tiền mặt khổng lồ từ ngân hàng.",
            "chu_the": "Ẩn dụ hoàn thành xuất sắc vai trò đòn bẩy rút vốn của dự án sân golf.",
            "camera": "Steady camera shot, ánh sáng tông Slate hiện đại.",
            "overlay": "BOTTOM LEFT | FINANCIAL LEVERAGE ENGINE"
        },
        {
            "sid": "CH03_SC020", "thoai": raw[19], "mod": "B_ROLL_REAL",
            "tu_lieu": "Bản cáo bạch phát hành trái phiếu doanh nghiệp riêng lẻ với tài sản bảo đảm là quyền tài sản dự án sân golf.",
            "query": "corporate bond prospectus collateral golf project private placement Vietnam",
            "source": "HNX / Bond Market Media",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC021", "thoai": raw[20], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "High-Yield Bond Coupon Card",
            "du_lieu": "Lãi suất trái phiếu huy động: COUPON RATE: 11% - 12% / YEAR. Quy mô hàng nghìn tỷ đồng.",
            "bo_cuc": "Nền Slate #1E293B, con số 11% - 12% phát sáng màu cam cảnh báo #FF7043.",
            "mau_sac": "Điểm nhấn cam cảnh báo và đỏ san hô.",
            "overlay": "BOTTOM LEFT | BOND COUPON: 11% - 12%/YEAR"
        },
        {
            "sid": "CH03_SC022", "thoai": raw[21], "mod": "VEO_AI",
            "boi_canh": "Đồng hồ cơ khí tính lãi suất đếm từng giây, các cọc tiền lãi tích tụ dần thành gánh nặng tài chính đè nặng lên bảng cân đối.",
            "chu_the": "Nét mặt căng thẳng của giám đốc tài chính khi nhìn vào lịch thanh toán nợ gốc lãi.",
            "camera": "Cinematic slow dolly in cận cảnh đồng hồ tính lãi.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC023", "thoai": raw[22], "mod": "INFOGRAPHIC_DATA",
            "chart_type": "Annual Debt Service Pressure Card",
            "du_lieu": "Áp lực nghĩa vụ trả nợ hàng năm: ANNUAL DEBT SERVICE: ~200 BILLION VND / YEAR (NỢ GỐC & LÃI VAY).",
            "bo_cuc": "Nền Slate #2A323D, con số 200 tỷ màu đỏ san hô #EF5350 to rõ nét.",
            "mau_sac": "Điểm nhấn đỏ san hô và vàng hổ phách.",
            "overlay": "BOTTOM LEFT | DEBT PRESSURE: ~200 BILLION VND/YEAR"
        },
        {
            "sid": "CH03_SC024", "thoai": raw[23], "mod": "B_ROLL_REAL",
            "tu_lieu": "Cảnh nhân viên nhặt bóng golf trên sân tập vắng khách, máy gom bóng chạy lọc cọc gom vài chục quả bóng golf dưới nắng trưa hè.",
            "query": "golf ball picker machine empty driving range golf course Vietnam",
            "source": "Golf Life Archive",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC025", "thoai": raw[24], "mod": "VEO_AI",
            "boi_canh": "Bàn kế toán với các dòng tiền bù chéo từ bán bất động sản dự án khác chuyển sang nuôi sân golf, nhưng các dòng tiền bù chéo đang cạn dần.",
            "chu_the": "Kế toán viên gõ máy tính với nét mặt lo lắng khi quỹ tiền mặt dự phòng gần chạm đáy.",
            "camera": "Steady camera shot, ánh sáng xám tro lạnh lẽo.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC026", "thoai": raw[25], "mod": "B_ROLL_REAL",
            "tu_lieu": "Thị trường bất động sản đóng băng: Sàn giao dịch treo biển đóng cửa, công trường xây dựng vắng tanh, cần cẩu bất động im lìm.",
            "query": "frozen real estate market idle tower cranes empty construction site Vietnam",
            "source": "VTV Thời sự / Báo Thanh Niên",
            "overlay": "BOTTOM LEFT | LIQUIDITY TRAP FREEZE"
        },
        {
            "sid": "CH03_SC027", "thoai": raw[26], "mod": "VEO_AI",
            "boi_canh": "Chiếc bẫy kim loại tài chính sập mạnh xuống trên bàn cân đối kế toán, kẹp chặt dòng tiền mặt của tập đoàn.",
            "chu_the": "Ẩn dụ trực quan về bẫy thanh khoản siết nghẹt doanh nghiệp đòn bẩy.",
            "camera": "Cinematic slow dolly in cận cảnh chiếc bẫy kim loại, ánh sáng xám slate lạnh buốt.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC028", "thoai": raw[27], "mod": "VEO_AI",
            "boi_canh": "Người dẫn chuyện đứng trước bức tường kính lớn nhìn ra bầu trời giông bão, suy tư về những rủi ro của ván cược tài chính đòn bẩy.",
            "chu_the": "Phong thái điềm tĩnh, đặt câu hỏi phản biện sâu sắc.",
            "camera": "Cinematic slow dolly forward từ sau lưng người dẫn chuyện.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC029", "thoai": raw[28], "mod": "VEO_AI",
            "boi_canh": "Khung hình chuyển dần từ bầu trời xám giông sang ánh bình minh rạng rỡ của bờ biển miền Trung nhiệt đới.",
            "chu_the": "Sự chuyển dịch nhận thức từ hoài nghi sang khám phá sự thật khách quan.",
            "camera": "Cinematic slow pan shot từ vùng u tối sang vùng ngập tràn ánh sáng.",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC030", "thoai": raw[29], "mod": "B_ROLL_REAL",
            "tu_lieu": "Flycam bay dọc bờ biển miền Trung tuyệt đẹp với làn sóng xanh ngọc và những dải cồn cát trắng tự nhiên uốn lượn.",
            "query": "Central Vietnam coastline turquoise ocean waves white sand dunes aerial",
            "source": "VTV Travel / Danang Media",
            "overlay": "Không."
        },
        {
            "sid": "CH03_SC031", "thoai": raw[30], "mod": "VEO_AI",
            "boi_canh": "@golf_course_aerial_links.jpg -> Đại cảnh sân golf links ven biển miền Trung bừng sáng dưới ánh bình minh, thảm cỏ xanh mướt tự thân tạo ra dòng tiền ngoại tệ rực rỡ, mở màn cho CH04.",
            "chu_the": "Cảnh quan thiên nhiên tráng lệ, không bóng dáng phân lô bán nền.",
            "camera": "Cinematic epic slow crane up góc rộng, đón ánh mặt trời rạng ngời trên biển.",
            "overlay": "BOTTOM LEFT | TOURISM CLUSTER EXPORT ENGINE"
        }
    ]
    write_and_export(3, scenes, "CHƯƠNG 3", "ẢO ẢNH ĐỊNH GIÁ DCF 50 NĂM VÀ BẪY ĐÒN BẨY TRÁI PHIẾU")

if __name__ == "__main__":
    generate_ch02()
    generate_ch03()
