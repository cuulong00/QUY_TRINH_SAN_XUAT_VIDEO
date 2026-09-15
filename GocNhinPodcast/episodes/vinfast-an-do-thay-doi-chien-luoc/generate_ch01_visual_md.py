# -*- coding: utf-8 -*-
import json
import os

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'
map_path = os.path.join(EPISODE_DIR, 'scene_timing_map.json')

with open(map_path, 'r', encoding='utf-8') as f:
    scenes = json.load(f)

ch01_scenes = [s for s in scenes if s['chapter'] == '01']

# Define 3-tier anatomy for each of the 40 scenes of Chapter 01
# Only ~20-25% have text overlay (around 9-10 scenes), rest is "Không"
scenes_detail = {
    "SC001": {
        "t1": "Phân xưởng dập cơ khí công nghiệp ô tô Ấn Độ chìm trong không gian noir u tối.",
        "t2": "Cỗ máy dập khổng lồ với các bánh răng thép hạng nặng quay chậm rãi, tia lửa cam lóe sáng giữa các khớp răng thép lạnh lẽo.",
        "t3": "Cú máy đẩy chậm đầy kịch tính vào hệ bánh răng cơ khí (Slow dramatic push-in shot), ánh sáng chiaroscuro tương phản cao.",
        "overlay": "Không"
    },
    "SC002": {
        "t1": "Không gian hải quan biên giới kinh tế với bức tường đá hoa cương sừng sững.",
        "t2": "Bức tường thuế quan khổng lồ đổ bóng đen dày đặc xuống sàn nhà xưởng, biểu thị mức thuế trừng phạt nghiệt ngã.",
        "t3": "Cú máy tĩnh trực diện (Steady camera shot) tập trung vào bức tường đá uy nghi và dòng chữ nổi bật.",
        "overlay": "\"THUẾ QUAN 70% - 100%\""
    },
    "SC003": {
        "t1": "Chân bức tường thuế quan trong góc tối nhà máy bị bỏ hoang.",
        "t2": "Những chiếc xe sedan cổ điển của Ford và General Motors bị phủ bạt bám bụi dày, nằm bất động như những chứng tích thất bại.",
        "t3": "Cú máy trượt ngang chậm sang phải (Slow horizontal tracking pan), bắt trọn đường nét hoang tàn của những chiếc xe bị phủ bạt.",
        "overlay": "Không"
    },
    "SC004": {
        "t1": "Khu bến cảng công nghiệp nhập khẩu ô tô với bầu trời xám xịt.",
        "t2": "Các thùng container ô tô nguyên chiếc (CBU) bị quấn xích sắt đỏ niêm phong chặt, phản ánh cái chết thương mại của xe nhập khẩu.",
        "t3": "Cú máy zoom cận cảnh chậm rãi vào ổ khóa xích sắt (Slow subtle zoom-in), toát lên sự bế tắc kinh tế.",
        "overlay": "Không"
    },
    "SC005": {
        "t1": "Cổng vòm đá sa thạch uy nghiêm của cơ quan chính phủ New Delhi.",
        "t2": "Cánh cổng chính sách mở hé, một luồng ánh sáng vàng ấm rọi qua khe cửa vào bóng tối của thị trường ô tô.",
        "t3": "Cú máy lướt tới chậm rãi về phía khe cửa ánh sáng (Slow forward camera glide), mở ra kỳ vọng chính sách mới.",
        "overlay": "Không"
    },
    "SC006": {
        "t1": "Phòng hội nghị chính sách công nghiệp New Delhi với bàn gỗ mahogany tối màu.",
        "t2": "Văn bản hiệp định đầu tư chính thức với cam kết rót vốn tối thiểu 500 triệu đô la được chiếu sáng dưới đèn bàn rọi.",
        "t3": "Cú máy tĩnh cận cảnh hồ sơ thỏa thuận (Steady macro document shot), nhấn mạnh cam kết tài chính lớn.",
        "overlay": "\"CAM KẾT: 500 TRIỆU USD\""
    },
    "SC007": {
        "t1": "Bàn thẩm định thuế của Bộ Tài chính Ấn Độ.",
        "t2": "Văn bản nghị định ưu đãi thuế được đóng dấu ấn đỏ pháp lý, cho phép hạ thuế nhập khẩu xuống mức sàn 15% cho nhà đầu tư đạt chuẩn.",
        "t3": "Cú máy tĩnh khóa chặt văn bản pháp lý (Steady decree shot), thể hiện cánh cửa ưu đãi hấp dẫn.",
        "overlay": "\"ƯU ĐÃI THUẾ: 15%\""
    },
    "SC008": {
        "t1": "Không gian bàn đàm phán thể chế với bóng đen của các khung cửa sổ sắt.",
        "t2": "Hình tượng sợi dây cáp thép thắt nút thể chế bao quanh tập hồ sơ điều kiện nội địa hóa, tạo cảm giác áp lực pháp lý siết chặt.",
        "t3": "Cú máy lùi chậm (Subtle slow zoom-out) làm lộ rõ sợi cáp thép căng cứng cuốn quanh chồng tài liệu quy hoạch.",
        "overlay": "Không"
    },
    "SC009": {
        "t1": "Bảng kiểm toán kỹ thuật trên tường phòng điều hành.",
        "t2": "Biểu đồ cột chỉ tiêu tỷ lệ nội địa hóa tăng gắt gao theo từng năm với các vạch kiểm toán đỏ nghiêm ngặt của chính phủ Ấn Độ.",
        "t3": "Cú máy nghiêng góc ngước nhìn lên (Slow upward tilt), nhấn mạnh độ dốc khắc nghiệt của lộ trình nội địa hóa.",
        "overlay": "Không"
    },
    "SC010": {
        "t1": "Kho lưu trữ hồ sơ thanh tra thuế với chiếc két sắt nặng nề bằng sắt đúc.",
        "t2": "Két sắt mở hé để lộ lệnh truy thu thuế toàn bộ kèm theo con dấu niêm phong màu đỏ thẫm của chính phủ Ấn Độ.",
        "t3": "Cú máy tĩnh trực diện vào cánh cửa két sắt và lệnh chế tài (Steady audit safe shot), cảnh báo rủi ro sống còn.",
        "overlay": "\"TRUY THU THUẾ TOÀN BỘ\""
    },
    "SC011": {
        "t1": "Bàn làm việc pháp lý của cố vấn thể chế độc lập.",
        "t2": "Chiếc cán cân công lý bằng đồng thau đặt trên bàn: Một bên là quyền lợi thuế ưu đãi nhẹ bẫng, một bên là mệnh lệnh nội địa hóa nặng trĩu.",
        "t3": "Cú máy trượt ngang chậm rãi qua chiếc cán cân bị lệch (Slow tracking shot), khắc họa tính chất pháp lý bắt buộc.",
        "overlay": "Không"
    },
    "SC012": {
        "t1": "Khu phức hợp công nghiệp ven biển Thoothukudi, bang Tamil Nadu.",
        "t2": "Toàn cảnh nhà máy VinFast hiện đại với các phân xưởng mái phẳng trải dài trên nền đất quy hoạch bên bờ biển.",
        "t3": "Cú máy toàn cảnh góc cao nhìn xuống (High-angle establishing wide shot), phác họa quy mô dự án 500 triệu USD.",
        "overlay": "\"THOOTHUKUDI: 500 TRIỆU USD\""
    },
    "SC013": {
        "t1": "Trung tâm điều hành sản xuất thông minh của nhà máy Thoothukudi.",
        "t2": "Bảng hiển thị kỹ thuật số phát sáng màu xanh ngọc hiển thị thông số công suất thiết kế 50.000 xe mỗi năm.",
        "t3": "Cú máy trượt ngang trên bảng điều khiển kỹ thuật số (Horizontal telemetry tracking shot), thể hiện mục tiêu sản xuất.",
        "overlay": "Không"
    },
    "SC014": {
        "t1": "Bàn vẽ kiến trúc công trình của ban quản lý dự án.",
        "t2": "Bản vẽ sơ đồ mặt bằng tổng thể Giai đoạn 1 được mở rộng, các phân xưởng được phân ô ranh giới rõ ràng bằng nét vẽ màu kem.",
        "t3": "Cú máy lướt chéo qua bản vẽ quy hoạch (Diagonal drafting pan shot), bóc tách cấu trúc thực tế của nhà máy.",
        "overlay": "Không"
    },
    "SC015": {
        "t1": "Phân xưởng hàn thân vỏ ô tô (Body Shop) tại Thoothukudi.",
        "t2": "Hàng chục cánh tay robot công nghiệp màu cam thực hiện các đường hàn điểm chính xác, bắn ra những chùm tia lửa màu cam rực rỡ.",
        "t3": "Cú máy trượt dọc theo dây chuyền hàn robot (Robotic line tracking shot), làm nổi bật năng lực gia công cơ khí.",
        "overlay": "Không"
    },
    "SC016": {
        "t1": "Dây chuyền buồng sơn tự động (Paint Shop) cách ly tiêu chuẩn cao.",
        "t2": "Các robot phun sơn tự động phủ lớp sơn bóng bẩy lên thân vỏ xe dưới dàn đèn sấy hồng ngoại màu vàng cam ấm.",
        "t3": "Cú máy trượt mượt mà theo thân xe chuyển động qua buồng sơn (Fluid paint-booth tracking shot).",
        "overlay": "Không"
    },
    "SC017": {
        "t1": "Dây chuyền lắp ráp hoàn thiện (General Assembly Shop).",
        "t2": "Các kỹ sư và công nhân phối hợp nhịp nhàng trên sàn thao tác công thái học, lắp ráp các chi tiết nội thất và hệ truyền động.",
        "t3": "Cú máy góc rộng trượt dọc băng chuyền hoàn thiện (Wide assembly conveyor tracking shot).",
        "overlay": "Không"
    },
    "SC018": {
        "t1": "Bản vẽ kỹ thuật tổng thể nhà máy với một ô quy hoạch bị bỏ trống.",
        "t2": "Khu vực đánh dấu bằng nét đứt mờ trên bản vẽ chỉ ra sự vắng mặt hoàn toàn của xưởng dập tấm vỏ kim loại tại chỗ.",
        "t3": "Cú máy đẩy chậm vào khoảng trống trên bản vẽ (Slow push-in on the missing stamping shop area).",
        "overlay": "Không"
    },
    "SC019": {
        "t1": "Sơ đồ luồng công nghệ sản xuất hệ thống pin xe điện.",
        "t2": "Vị trí của dây chuyền chế tạo tế bào pin (cell pin) hoàn toàn bị gạch chéo, khẳng định nhà máy không sản xuất pin tại Ấn Độ.",
        "t3": "Cú máy quét ngang sơ đồ luồng công nghệ pin (Flowchart horizontal pan shot), xác nhận giới hạn lắp ráp thuần túy.",
        "overlay": "Không"
    },
    "SC020": {
        "t1": "Khu bến cảng nước sâu Cát Hải, Hải Phòng tại Việt Nam.",
        "t2": "Các kiện hàng linh kiện CKD đóng thùng gỗ công nghiệp mang nhãn xuất khẩu VinFast được cẩu lên boong tàu hàng hướng sang Ấn Độ.",
        "t3": "Cú máy tĩnh trực diện tại cầu cảng xuất khẩu CKD (Steady export quay shot), định vị nguồn gốc linh kiện.",
        "overlay": "\"LINH KIỆN CKD CÁT HẢI\""
    },
    "SC021": {
        "t1": "Khu vực kiểm tra chất lượng xuất xưởng cuối dây chuyền Thoothukudi.",
        "t2": "Chiếc xe điện VinFast hoàn thiện đầu tiên lăn bánh dưới dàn đèn kiểm tra ánh sáng trắng, logo chữ V mạ crom sáng bóng.",
        "t3": "Cú máy đẩy chậm vào lưới tản nhiệt và logo chữ V (Slow push-in to glowing V-badge), khẳng định xe đã xuất xưởng.",
        "overlay": "Không"
    },
    "SC022": {
        "t1": "Phòng chỉ đạo sản xuất với các màn hình phân tích chuỗi cung ứng.",
        "t2": "Kỹ sư trưởng VinFast trong đồng phục kỹ thuật màu xanh navy cùng các cộng sự đánh giá giới hạn của mô hình CKD thuần túy.",
        "t3": "Cú máy lia ngang qua nhóm kỹ sư đang nghiên cứu biểu đồ (Horizontal panning shot across engineers).",
        "overlay": "Không"
    },
    "SC023": {
        "t1": "Bản đồ mạng lưới công nghiệp phụ trợ trên màn hình điều hành.",
        "t2": "Mạng lưới kết nối số hóa trừu tượng tỏa sáng từ Thoothukudi kết nối tới hơn ba trăm xưởng cơ khí phụ trợ trên khắp các bang Ấn Độ.",
        "t3": "Cú máy tĩnh bao quát mạng lưới liên kết phụ trợ (Steady network map shot) làm nổi bật quy mô tiếp xúc rộng lớn.",
        "overlay": "\"300+ XƯỞNG CƠ KHÍ BẢN ĐỊA\""
    },
    "SC024": {
        "t1": "Bàn thiết kế kiểu dáng công nghiệp với ba màn hình hiển thị đồ họa CAD.",
        "t2": "Hình ảnh khung vỏ 3D của ba dòng xe chiến lược: Chiếc mini VF 3, chiếc crossover đô thị VF 6 và chiếc SUV thể thao VF 7.",
        "t3": "Cú máy trượt ngang qua ba bản vẽ CAD xe hơi (Slow panning shot across 3 CAD models), giới thiệu bộ ba sản phẩm.",
        "overlay": "Không"
    },
    "SC025": {
        "t1": "Xưởng cơ khí chính xác của một đối tác phụ trợ tại miền nam Ấn Độ.",
        "t2": "Người chủ xưởng cơ khí Ấn Độ cùng kỹ sư kiểm tra khối khuôn dập thử nghiệm phay CNC bằng thước kẹp điện tử.",
        "t3": "Cú máy cận cảnh thao tác kiểm tra kích thước khuôn (Macro inspection shot), phản ánh giai đoạn thử nghiệm ban đầu.",
        "overlay": "Không"
    },
    "SC026": {
        "t1": "Khu vực gia công cơ khí nặng với máy phay CNC tốc độ cao.",
        "t2": "Đầu mũi phay kim cương đang gọt giũa khối phôi thép khuôn dập thử nghiệm, bụi kim loại và tia lửa li ti bắn ra dưới vòi làm mát.",
        "t3": "Cú máy cận cảnh chuyển động gọt thép của máy CNC (Close-up CNC milling motion), khẳng định dự án mới ở khâu khuôn mẫu.",
        "overlay": "Không"
    },
    "SC027": {
        "t1": "Bàn kỹ thuật với tập hồ sơ quy trình chế tạo khuôn mẫu thử nghiệm.",
        "t2": "Tập tài liệu kỹ thuật có nhãn 'PROTO-TOOLING PHASE' nằm cạnh các mẫu phôi dập thử nghiệm ban đầu của thân vỏ.",
        "t3": "Cú máy trượt chậm trên tập hồ sơ thử nghiệm (Slow tracking shot on proto-tooling dossier), chứng minh chưa sản xuất hàng loạt.",
        "overlay": "Không"
    },
    "SC028": {
        "t1": "Bàn làm việc với tờ lịch thời sự bước sang mốc đầu tháng 9 năm 2026.",
        "t2": "Tờ lịch lật qua mốc tháng 9/2026 trong khi các màn hình máy tính phía sau bắt đầu nhảy tin tức thời sự kinh tế dồn dập.",
        "t3": "Cú máy đẩy nhẹ vào tờ lịch tháng 9 (Subtle push-in on the calendar turn), tạo nhịp chuyển biến cố.",
        "overlay": "Không"
    },
    "SC029": {
        "t1": "Bức tường màn hình tin tức báo chí quốc tế và Ấn Độ.",
        "t2": "Các dòng tít báo lớn xuất hiện đồng loạt đưa tin về quyết định bất ngờ của VinFast đối với chuỗi cung ứng linh kiện nội địa.",
        "t3": "Cú máy lùi chậm làm lộ ra hàng loạt dòng tiêu đề báo chí (Slow pull-back revealing overlapping headlines).",
        "overlay": "Không"
    },
    "SC030": {
        "t1": "Bàn làm việc điều hành với văn bản giác thư nội bộ chính thức.",
        "t2": "Văn bản thông báo phát lệnh tạm dừng toàn bộ chương trình phát triển linh kiện nội địa cho VF 3, VF 6 và VF 7 trên giấy tiêu đề công ty.",
        "t3": "Cú máy tĩnh khóa chặt văn bản giác thư nội bộ (Steady memo shot) nhấn mạnh sức nặng của quyết định đạp phanh.",
        "overlay": "\"TẠM DỪNG NỘI ĐỊA HÓA\""
    },
    "SC031": {
        "t1": "Bàn kiểm toán tài chính công nghiệp với các bảng kê chi phí gia công.",
        "t2": "Các bảng kê khai chi phí khuôn dập và công sức kỹ thuật phát sinh từ hơn 300 đối tác Ấn Độ được tập hợp để đối soát.",
        "t3": "Cú máy trượt ngang qua các tập chứng từ kê khai chi phí tooling (Slow tracking shot across tooling expense forms).",
        "overlay": "Không"
    },
    "SC032": {
        "t1": "Phòng đàm phán tài chính với tập chứng từ cam kết thanh toán bồi thường.",
        "t2": "Tập hồ sơ bồi thường chi phí thực tế được đóng dấu xác nhận thanh toán sòng phẳng, thể hiện trách nhiệm pháp lý của hãng xe.",
        "t3": "Cú máy đẩy chậm vào chứng từ cam kết bồi thường (Slow push-in on settlement voucher), giải tỏa nghi vấn xù nợ.",
        "overlay": "Không"
    },
    "SC033": {
        "t1": "Bản đồ phối cảnh tổ hợp 500 triệu USD trong không gian u tối.",
        "t2": "Bóng tối bao trùm bản đồ dự án Thoothukudi cùng những câu hỏi hoài nghi của thị trường về số phận khoản đầu tư khổng lồ.",
        "t3": "Cú máy trượt chậm qua bản đồ dự án trong bóng đêm (Slow mysterious tracking shot across the site plan).",
        "overlay": "Không"
    },
    "SC034": {
        "t1": "Toàn cảnh ngoại thất nhà máy Thoothukudi lúc nửa đêm.",
        "t2": "Các dãy nhà xưởng lắp ráp vẫn sáng rực ánh đèn vàng ấm, khói trắng nhẹ bốc lên từ hệ thống thông gió, chứng minh nhà máy không hề dừng lại.",
        "t3": "Cú máy trượt ngang toàn cảnh nhà máy sáng đèn về đêm (Wide nocturnal exterior pan shot), đập tan tin đồn đóng cửa.",
        "overlay": "Không"
    },
    "SC035": {
        "t1": "Bên trong xưởng lắp ráp Thoothukudi dưới ánh đèn công nghiệp.",
        "t2": "Dây chuyền lắp ráp xe từ các bộ linh kiện CKD chuyển từ Việt Nam sang vẫn vận hành nhịp nhàng, công nhân liên tục hoàn thiện xe.",
        "t3": "Cú máy trượt theo các cụm linh kiện CKD trên giá đẩy kỹ thuật (Tracking shot following CKD assembly flow).",
        "overlay": "Không"
    },
    "SC036": {
        "t1": "Màn hình cơ sở dữ liệu đăng ký phương tiện quốc gia Vahan của Ấn Độ.",
        "t2": "Giao diện hệ thống Vahan tháng 8/2026 hiển thị con số đăng ký xe mới của VinFast tăng vọt lên gần 2.200 chiếc.",
        "t3": "Cú máy trượt chậm qua bảng dữ liệu Vahan (Slow analytical dashboard scan shot), ghi nhận con số thực chứng.",
        "overlay": "Không"
    },
    "SC037": {
        "t1": "Bảng xếp hạng thị phần ô tô điện toàn Ấn Độ tháng 8 năm 2026.",
        "t2": "Cột xếp hạng của VinFast vươn lên đứng thứ 4 toàn quốc, vượt qua nhiều tên tuổi lớn trong phân khúc xe điện.",
        "t3": "Cú máy tĩnh trực diện vào bục xếp hạng thị phần (Steady market podium shot) tôn vinh vị thế Top 4.",
        "overlay": "\"TOP 4 THỊ PHẦN (8/2026)\""
    },
    "SC038": {
        "t1": "Bãi bàn giao xe thành phẩm ngoài trời tại tổ hợp Thoothukudi.",
        "t2": "Hàng trăm chiếc xe VF 6 và VF 7 màu sắc đa dạng xếp hàng ngay ngắn, sẵn sàng lên xe chuyên dụng chuyển tới các đại lý toàn quốc.",
        "t3": "Cú máy góc rộng trượt ngang qua đoàn xe điện thành phẩm (Sweeping wide pan across finished EV fleet).",
        "overlay": "Không"
    },
    "SC039": {
        "t1": "Góc khuất u tối bên trong một xưởng cơ khí chế tạo khuôn dập nặng.",
        "t2": "Cận cảnh khối khuôn dập thép khổng lồ nặng hàng chục tấn với các rãnh cắt sắc lạnh phản chiếu ánh sáng directional spotlight.",
        "t3": "Cú máy đẩy chậm đầy bí ẩn vào khối khuôn thép nguyên khối (Slow dramatic push-in toward giant steel die block).",
        "overlay": "Không"
    },
    "SC040": {
        "t1": "Bề mặt thép mạ lạnh của khối khuôn dập ô tô với các phương trình kinh tế.",
        "t2": "Công thức toán học khấu hao chi phí cố định hiện lên trên mặt khối thép, phơi bày cơ chế trực tiếp định đoạt giá thành xuất xưởng.",
        "t3": "Cú máy tĩnh khóa chặt bề mặt khối thép và công thức khấu hao (Steady macro die face shot) mở ra bài toán của Chương 2.",
        "overlay": "\"BÀI TOÁN KHẤU HAO KHUÔN DẬP\""
    }
}

# Build Markdown Table Content
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
    "> **Quy tắc Text Overlay:** Chỉ chèn chữ vào đúng 10 phân cảnh mốc thông số then chốt (chiếm 25%). 30 phân cảnh còn lại (75%) để `[TEXT OVERLAY]: Không` nhằm tối đa hóa chuyển động điện ảnh linh hoạt cho camera Veo 3.1.",
    "",
    "---",
    "",
    "| Phân Cảnh (Scene ID) | Thời Gian & Câu Thoại Voiceover (Độ dài & Số từ) | Mô Tả Bối Cảnh Thị Giác Chi Tiết (Anatomy & Motion) | Text Overlay (Selective Typography ~20%) |",
    "| :--- | :--- | :--- | :--- |"
]

for s in ch01_scenes:
    sc_id = s['id']
    dur = s['duration_sec']
    text = ' '.join(s['sentences'])
    words = len(text.split())
    d = scenes_detail[sc_id]
    
    col1 = f"**{sc_id}**"
    col2 = f"`{dur}s` ({words} từ)<br/>*\"{text}\"*"
    col3 = f"**Tầng 1 (Đế cố định):** {d['t1']}<br/>**Tầng 2 (Bộ truyền động/Chủ thể):** {d['t2']}<br/>**Tầng 3 (Khối tác động & Góc máy):** {d['t3']}"
    col4 = f"**{d['overlay']}**"
    
    md_lines.append(f"| {col1} | {col2} | {col3} | {col4} |")

out_file = os.path.join(EPISODE_DIR, 'chapter_01_visual.md')
with open(out_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"Successfully created {out_file} with {len(ch01_scenes)} scenes in 3-tier anatomy table!")
