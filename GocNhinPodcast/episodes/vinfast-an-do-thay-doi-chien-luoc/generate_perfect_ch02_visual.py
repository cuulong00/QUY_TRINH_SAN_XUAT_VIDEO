# -*- coding: utf-8 -*-
import json
import os

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'

ch02_matrix = [
    {
        "id": "SC041",
        "dur": 6.82,
        "words": 26,
        "text": "Để hiểu được bài toán khấu hao nghiệt ngã đó, trước hết cần bước vào bên trong hơn ba trăm xưởng cơ khí tại Ấn Độ.",
        "t1": "Cổng vào xưởng cơ khí phụ trợ gia công kim loại tại miền nam Ấn Độ.",
        "t2": "Kỹ sư trưởng và chuyên gia kinh tế công nghiệp bước qua ngưỡng cửa nhà xưởng, ánh sáng mặt trời rọi qua khe mái tôn xuống sàn bê tông.",
        "t3": "Cú máy đẩy chậm theo bước chân nhân vật bước vào bên trong xưởng (Slow forward tracking shot entering workshop).",
        "overlay": "Không",
        "subject": "an automotive engineer in dark work attire stepping through the roll-up door into a shadowy Indian precision machine shop, shafts of daylight piercing through corrugated roofing",
        "setting": "an active precision fabrication workshop in southern India",
        "motion": "Slow forward tracking shot following footsteps entering the industrial workshop"
    },
    {
        "id": "SC042",
        "dur": 4.46,
        "words": 17,
        "text": "Trong mạng lưới phụ trợ này, các nhóm linh kiện có sự phân hóa rất rõ rệt.",
        "t1": "Bảng phân loại linh kiện kỹ thuật trên tường xưởng cơ khí.",
        "t2": "Sơ đồ chia đôi linh kiện ô tô thành hai nhóm: Phía trái là phụ tùng tiêu chuẩn phổ thông, phía phải là cụm chi tiết dập khuôn riêng biệt.",
        "t3": "Cú máy trượt ngang qua bảng phân loại linh kiện (Horizontal scan across component taxonomy board).",
        "overlay": "Không",
        "subject": "a technical wall schematic dividing automotive components into generic off-the-shelf parts and specialized custom-tooled stampings",
        "setting": "the engineering control office inside the machine shop",
        "motion": "Slow horizontal tracking pan across the component classification chart"
    },
    {
        "id": "SC043",
        "dur": 6.56,
        "words": 25,
        "text": "Những chi tiết thông thường như lốp xe, kính, ghế ngồi hay dây điện là những thứ ngành phụ trợ bản địa đã có sẵn",
        "t1": "Khu vực kho chứa linh kiện tiêu chuẩn của xưởng phụ trợ.",
        "t2": "Các dãy lốp cao su, kính an toàn cường lực, ghế bọc da và các cuộn dây điện được xếp ngăn nắp trên kệ kim loại cao.",
        "t3": "Cú máy trượt ngang qua các kệ linh kiện phổ thông có sẵn (Slow tracking shot along warehouse shelving of standard parts).",
        "overlay": "Không",
        "subject": "stacked industrial automotive tires, tempered safety glass panels, seats, and bundled copper wire harnesses stored neatly on warehouse racks",
        "setting": "a local automotive supplier inventory warehouse",
        "motion": "Slow cinematic horizontal tracking pan across standard parts inventory"
    },
    {
        "id": "SC044",
        "dur": 3.15,
        "words": 12,
        "text": "chi phí thích ứng sản xuất không phải rào cản quá lớn.",
        "t1": "Bàn lắp ráp linh kiện phụ trợ thông thường.",
        "t2": "Công nhân địa phương bó gọn các cuộn dây điện và kiểm tra kích thước với dụng cụ đơn giản, chi phí khuôn mẫu không đáng kể.",
        "t3": "Cú máy cận cảnh thao tác lắp ráp đơn giản (Close-up of low-adaptation component assembly).",
        "overlay": "Không",
        "subject": "Indian assembly technicians neatly securing standard electrical harnesses on a wooden worktable with minimal tooling overhead",
        "setting": "a local auxiliary component workshop bench",
        "motion": "Slow subtle zoom-in on the low-overhead assembly process"
    },
    {
        "id": "SC045",
        "dur": 4.72,
        "words": 18,
        "text": "Nhưng điểm nghẽn chí mạng lại nằm ở các chi tiết đòi hỏi khuôn mẫu chế tạo riêng",
        "t1": "Khu vực phân xưởng dập cơ khí nặng tách biệt phía sau lớp lưới thép bảo vệ.",
        "t2": "Cánh cửa lưới thép nặng nề hé mở, để lộ không gian tĩnh lặng của khu vực chế tạo khuôn mẫu chuyên dụng chi phí đắt đỏ.",
        "t3": "Cú máy đẩy chậm qua cánh cửa lưới thép vào phân xưởng nặng (Slow push-in past heavy safety wire gate).",
        "overlay": "Không",
        "subject": "a heavy industrial safety wire mesh partition swinging open into a dimly lit high-tonnage pressing bay, highlighting a capital bottleneck",
        "setting": "the entrance to the specialized tooling fabrication hall",
        "motion": "Slow dramatic push-in shot past the wire security gate"
    },
    {
        "id": "SC046",
        "dur": 2.62,
        "words": 10,
        "text": "Vỏ xe, khung gầm và các tấm thép định hình.",
        "t1": "Bệ gia công chi tiết thân vỏ lớn trong xưởng dập.",
        "t2": "Các tấm thép định hình khổ lớn, khung gầm chịu lực và tấm vỏ hông xe phản chiếu ánh sáng sắc lạnh của kim loại chưa sơn.",
        "t3": "Cú máy tĩnh trực diện khóa chặt các tấm thép định hình lớn (Steady shot on structural body stampings) và text overlay.",
        "overlay": "\"VỎ XE & KHUNG GẦM\"",
        "subject": "massive formed automotive body side panels and chassis structural steel components gleaming under focused industrial lights",
        "setting": "the heavy body-stamping staging bay",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC047",
        "dur": 4.99,
        "words": 19,
        "text": "Mỗi bộ khuôn dập chuyên dụng như vậy tiêu tốn từ hàng trăm ngàn đến cả triệu đô la.",
        "t1": "Bệ máy phay khuôn dập hợp kim nguyên khối nặng hàng chục tấn.",
        "t2": "Khối khuôn dập khổng lồ với bề mặt chạm khắc chính xác đường cong xe hơi, phản chiếu mức giá đắt đỏ từ hàng trăm ngàn đến cả triệu USD.",
        "t3": "Cú máy tĩnh trực diện vào khối khuôn dập triệu đô (Steady macro shot of the high-value die tooling block).",
        "overlay": "\"KHUÔN DẬP: HÀNG TRIỆU USD\"",
        "subject": "an immense solid alloy steel automotive stamping die block mounted on an industrial milling bed, reflecting immense capital value",
        "setting": "the heavy die fabrication shop",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC048",
        "dur": 4.46,
        "words": 17,
        "text": "Khoản đầu tư cố định khổng lồ đó tạo ra một quy luật toán học nghiệt ngã",
        "t1": "Bàn tính toán chi phí tài chính công nghiệp.",
        "t2": "Đồ thị toán học mô tả đường cong chi phí cố định (CAPEX) dốc đứng, đè nặng lên từng đơn vị sản phẩm khi sản lượng ở mức thấp.",
        "t3": "Cú máy đẩy chậm vào đường cong chi phí cố định (Slow push-in on the steep fixed-cost amortization curve).",
        "overlay": "Không",
        "subject": "a steep mathematical fixed-cost amortization curve drawn in glowing white ink on an industrial drafting board",
        "setting": "an industrial engineering cost-accounting room",
        "motion": "Slow dramatic push-in shot toward the steep amortization curve"
    },
    {
        "id": "SC049",
        "dur": 5.25,
        "words": 20,
        "text": "Các xưởng cơ khí Ấn Độ không thể tự bỏ tiền làm khuôn nếu không nhìn thấy điểm hòa vốn.",
        "t1": "Văn phòng điều hành xưởng cơ khí bản địa tại Tamil Nadu.",
        "t2": "Chủ xưởng cơ khí Ấn Độ trong trang phục sơ mi xám đứng trầm ngâm khoanh tay trước máy tính, không dám mạo hiểm vốn tự có.",
        "t3": "Cú máy đẩy nhẹ vào vẻ mặt đăm chiêu tính toán của chủ xưởng (Subtle push-in toward the cautious Indian supplier).",
        "overlay": "Không",
        "subject": "a South Asian Indian precision tooling industrialist in his 50s standing with folded arms in deep contemplation beside blueprints",
        "setting": "a private workshop management office",
        "motion": "Slow subtle push-in toward the calculating machine shop owner"
    },
    {
        "id": "SC050",
        "dur": 6.82,
        "words": 26,
        "text": "Họ đặt ra một lằn ranh kỹ thuật bắt buộc: Mỗi dòng xe phải đạt sản lượng tối thiểu hai mươi lăm ngàn chiếc mỗi năm.",
        "t1": "Bảng tiêu chuẩn kỹ thuật trên bàn đàm phán cung ứng.",
        "t2": "Lằn ranh đỏ bắt buộc hiển thị mốc sản lượng tối thiểu 25.000 xe mỗi năm cho từng mẫu xe để xưởng đồng ý mở khuôn dập.",
        "t3": "Cú máy tĩnh khóa chặt lằn ranh kỹ thuật 25.000 xe (Steady threshold line shot) cùng text overlay nổi bật.",
        "overlay": "\"ĐIỂM HÒA VỐN: 25.000 XE/NĂM\"",
        "subject": "a technical break-even chart highlighting a rigid minimum volume threshold line marked at twenty-five thousand units per year",
        "setting": "a formal automotive supply procurement table",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC051",
        "dur": 6.04,
        "words": 23,
        "text": "Ở quy mô đó, tiền chế tạo khuôn mới được chia nhỏ ra từng chi tiết để có được mức giá cạnh tranh.",
        "t1": "Mô phỏng toán học phân bổ chi phí khuôn trên dây chuyền sản xuất lớn.",
        "t2": "Hàng ngàn tấm thép dập thành phẩm liên tục lăn qua băng chuyền, chia nhỏ chi phí cố định triệu đô thành những phần rất nhỏ.",
        "t3": "Cú máy trượt dọc theo dòng linh kiện dập chạy liên tục (Tracking shot following mass-stamped steel panels).",
        "overlay": "Không",
        "subject": "stamped automotive steel panels flowing continuously along an automated roller line, diluting fixed tooling expense into minimal unit cost",
        "setting": "a high-volume automated pressing bay",
        "motion": "Slow cinematic horizontal tracking pan across the mass stamping line"
    },
    {
        "id": "SC052",
        "dur": 3.94,
        "words": 15,
        "text": "Thoạt nhìn, con số gần hai ngàn hai trăm xe đăng ký trong tháng 8",
        "t1": "Màn hình dữ liệu thị trường ô tô Ấn Độ.",
        "t2": "Biểu đồ cột doanh số tháng 8/2026 vươn cao với con số gần 2.200 xe được chiếu sáng dưới ánh đèn neon.",
        "t3": "Cú máy đẩy chậm vào con số 2.200 xe đăng ký mới (Subtle push-in toward the monthly sales figure).",
        "overlay": "Không",
        "subject": "an illuminated automotive monthly registration chart displaying a vibrant bar reaching nearly two thousand two hundred vehicles",
        "setting": "an automotive market data analytics terminal",
        "motion": "Slow dramatic push-in shot toward the monthly sales graph"
    },
    {
        "id": "SC053",
        "dur": 5.77,
        "words": 22,
        "text": "đưa VinFast lọt vào top 4 thương hiệu dẫn đầu phân khúc xe điện — là một đà tăng trưởng ấn tượng.",
        "t1": "Bục vinh danh thị phần phân khúc xe điện toàn Ấn Độ.",
        "t2": "Biểu tượng chữ V của VinFast tỏa sáng ở vị trí Top 4 thương hiệu dẫn đầu phân khúc xe điện trên bảng xếp hạng thị trường.",
        "t3": "Cú máy góc thấp ngước nhìn bục xếp hạng Top 4 (Low-angle leaderboard reveal shot).",
        "overlay": "Không",
        "subject": "an illuminated industry ranking leaderboard showing the winged V-logo positioned proudly in the Top 4 electric vehicle manufacturer tier",
        "setting": "a prestigious automotive market summit hall",
        "motion": "Slow upward tilt revealing the industry market leaderboard"
    },
    {
        "id": "SC054",
        "dur": 3.94,
        "words": 15,
        "text": "Thế nhưng, con số đó là tổng lượng xe của cả thương hiệu gộp lại.",
        "t1": "Bàn phân tích số liệu kiểm toán chi tiết.",
        "t2": "Cột số liệu 2.200 xe được bóc tách và phân rã thành các cấu phần riêng lẻ, làm lộ ra bản chất gộp chung của toàn bộ danh mục xe.",
        "t3": "Cú máy lùi chậm làm lộ ra các nhánh phân rã số liệu (Slow pull-back revealing disaggregated sales lines).",
        "overlay": "Không",
        "subject": "an aggregate corporate sales total decomposing into separate individual vehicle line contributions on an audit glass screen",
        "setting": "a financial analysis war room",
        "motion": "Slow subtle zoom-out revealing the component breakdown"
    },
    {
        "id": "SC055",
        "dur": 5.51,
        "words": 21,
        "text": "Khi chia đều cho hai dòng xe đang bán là VF 6 và VF 7, sự thật lập tức hiện rõ",
        "t1": "Hình ảnh đối chiếu kỹ thuật giữa hai dòng xe đang bán tại Ấn Độ.",
        "t2": "Hai mô hình xe VF 6 và VF 7 đặt cạnh nhau trên bàn phân tích, chia đôi tổng sản lượng hàng tháng thành hai nửa bằng nhau.",
        "t3": "Cú máy trượt ngang qua hai hình bóng xe điện (Horizontal pan framing the two vehicle profiles).",
        "overlay": "Không",
        "subject": "side-by-side profile silhouettes of VF 6 and VF 7 electric SUVs split across a mathematical division line",
        "setting": "an automotive design and commercial planning studio",
        "motion": "Slow cinematic horizontal tracking pan across both vehicle profiles"
    },
    {
        "id": "SC056",
        "dur": 6.56,
        "words": 25,
        "text": "Mỗi mẫu xe chỉ đạt trung bình chưa đầy một ngàn chiếc mỗi tháng, tương đương khoảng mười đến mười hai ngàn xe mỗi năm.",
        "t1": "Đồng hồ đo nhịp sản xuất hàng tháng của từng dòng xe.",
        "t2": "Kim đồng hồ sản lượng dừng lại ở mức chưa đầy 1.000 chiếc/tháng, tương đương 10.000 đến 12.000 xe mỗi năm cho từng mẫu.",
        "t3": "Cú máy tĩnh khóa chặt đồng hồ sản lượng và con số thực tế (Steady production dial shot) cùng text overlay.",
        "overlay": "\"< 1.000 XE/THÁNG / MẪU\"",
        "subject": "a mechanical factory production output gauge needle resting below one thousand monthly units, translating to 10,000 annual cars",
        "setting": "the plant production metrics telemetry panel",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC057",
        "dur": 5.77,
        "words": 22,
        "text": "Quy mô này chưa bằng một nửa ngưỡng hòa vốn hai mươi lăm ngàn xe mà một bộ khuôn dập yêu cầu.",
        "t1": "Biểu đồ so sánh quy mô thực tế và điểm hòa vốn khuôn dập.",
        "t2": "Cột sản lượng 11.000 xe đứng lọt thỏm dưới lằn ranh 25.000 xe, phơi bày khoảng thâm hụt sản lượng hơn 50% so với yêu cầu hoàn vốn.",
        "t3": "Cú máy tĩnh trực diện vào biểu đồ thâm hụt sản lượng (Steady deficit comparative chart shot) cùng text overlay.",
        "overlay": "\"CHƯA ĐẠT 1/2 NGƯỠNG HÒA VỐN\"",
        "subject": "a stark comparative bar graph showing actual model output standing at less than half of the towering twenty-five thousand unit break-even mark",
        "setting": "an industrial capital audit presentation wall",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC058",
        "dur": 6.56,
        "words": 25,
        "text": "Đáng chú ý, trong hơn ba trăm đối tác tiếp xúc các dự án linh kiện nội địa cho ba mẫu xe này mới chỉ",
        "t1": "Bản đồ lưu trữ tiến độ dự án của hơn 300 đối tác cơ khí.",
        "t2": "Danh mục các hợp đồng với 300 nhà xưởng phụ trợ đều dừng lại ở giai đoạn thiết kế kỹ thuật ban đầu, chưa bước sang hợp đồng thương mại.",
        "t3": "Cú máy trượt chậm qua các tập hồ sơ dự án phụ trợ (Slow tracking shot across supplier partnership files).",
        "overlay": "Không",
        "subject": "hundreds of supplier engagement contract binders organized neatly, all tagged at initial engineering feasibility status",
        "setting": "the supplier procurement archives",
        "motion": "Slow cinematic horizontal tracking pan across project binders"
    },
    {
        "id": "SC059",
        "dur": 3.67,
        "words": 14,
        "text": "dừng ở khâu thiết kế kỹ thuật và gia công khuôn mẫu thử nghiệm.",
        "t1": "Màn hình CAD 3D và bàn phôi khuôn dập thử nghiệm.",
        "t2": "Bản vẽ 3D chi tiết khuôn dập hiển thị trên máy tính kỹ thuật bên cạnh mẫu phôi thử nghiệm chưa qua xử lý nhiệt.",
        "t3": "Cú máy cận cảnh màn hình CAD và phôi khuôn mẫu thử (Close-up of CAD workstation and prototype die billet).",
        "overlay": "Không",
        "subject": "a 3D CAD stamping tool simulation on a computer monitor beside an unfinished rough steel prototype die billet",
        "setting": "a tooling design and development laboratory",
        "motion": "Slow subtle zoom-in on the 3D CAD mold simulation"
    },
    {
        "id": "SC060",
        "dur": 3.41,
        "words": 13,
        "text": "Các xưởng cơ khí chưa hề bước vào giai đoạn dập hàng loạt",
        "t1": "Dàn máy dập công nghiệp lớn trong trạng thái dừng hoạt động.",
        "t2": "Dây chuyền máy dập dập thân vỏ công suất lớn đứng im lìm không hoạt động, không có dải phôi thép cuộn nào được nạp vào máy.",
        "t3": "Cú máy lướt chậm qua dàn máy dập đứng yên (Slow pan along idle industrial stamping press line).",
        "overlay": "Không",
        "subject": "massive automated hydraulic stamping presses sitting idle under amber maintenance lights with no active steel coils fed",
        "setting": "a heavy automotive press shop floor",
        "motion": "Slow cinematic horizontal tracking pan across idle stamping presses"
    },
    {
        "id": "SC061",
        "dur": 3.67,
        "words": 14,
        "text": "và chưa bàn giao bất kỳ linh kiện thương mại nào cho nhà máy.",
        "t1": "Khu vực kho xuất hàng linh kiện của các xưởng cơ khí bản địa.",
        "t2": "Các giá để hàng rỗng trơn không có chi tiết dập thành phẩm nào được đóng gói hay bàn giao cho xe thương mại Thoothukudi.",
        "t3": "Cú máy góc rộng quay kho hàng rỗng (Wide pan across empty delivery staging racks).",
        "overlay": "Không",
        "subject": "empty industrial dispatch racks and clean loading bays with zero commercial body panels delivered to assembly plants",
        "setting": "a machine shop dispatch bay",
        "motion": "Slow cinematic horizontal tracking pan across empty racks"
    },
    {
        "id": "SC062",
        "dur": 3.94,
        "words": 15,
        "text": "Riêng với VF 3, mẫu xe này chưa từng được mở bán tại Ấn Độ",
        "t1": "Showroom xe điện VinFast với các mẫu xe VF 6 và VF 7 đang trưng bày.",
        "t2": "Mẫu xe mini VF 3 hoàn toàn vắng bóng tại các đại lý và phòng trưng bày, khẳng định xe chưa từng được mở bán thương mại.",
        "t3": "Cú máy tĩnh khóa góc nhìn vào không gian đại lý (Steady showroom frame) cùng text overlay xác nhận.",
        "overlay": "\"VF 3: CHƯA TỪNG MỞ BÁN\"",
        "subject": "a pristine modern Indian automotive showroom featuring VF 6 and VF 7 crossovers, with the mini VF 3 entirely absent from floor displays",
        "setting": "an urban flagship electric car dealership",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC063",
        "dur": 3.15,
        "words": 12,
        "text": "nên hoàn toàn chưa phát sinh giao dịch linh kiện thành phẩm.",
        "t1": "Sổ cái kế toán theo dõi giao dịch linh kiện phụ trợ.",
        "t2": "Trang sổ theo dõi linh kiện của VF 3 trắng trơn không một dòng ghi nợ, xác nhận không có bất kỳ giao dịch thương mại thành phẩm nào.",
        "t3": "Cú máy cận cảnh sổ cái kế toán không có giao dịch (Macro shot of blank component transaction ledger).",
        "overlay": "Không",
        "subject": "an official commercial accounting ledger for the VF 3 platform showing blank entries and zero transaction debits",
        "setting": "an industrial purchasing audit desk",
        "motion": "Slow subtle zoom-in on the pristine blank transaction ledger"
    },
    {
        "id": "SC064",
        "dur": 4.99,
        "words": 19,
        "text": "Khi đối tác hoàn thiện khuôn thử nghiệm và báo giá, bài toán kinh tế lập tức gãy đổ.",
        "t1": "Bàn đàm phán hợp đồng giữa VinFast và đại diện xưởng cơ khí Ấn Độ.",
        "t2": "Bản báo giá chính thức đặt xuống bàn với các con số đơn giá phát nổ, sơ đồ hiệu quả tài chính bị gãy gập.",
        "t3": "Cú máy đẩy chậm vào bảng báo giá bị gãy đổ tính khả thi (Slow dramatic push-in on the collapsing cost quotation).",
        "overlay": "Không",
        "subject": "a formal component price quotation sheet arriving on an executive desk, revealing unviable unit costs that shatter feasibility models",
        "setting": "a corporate procurement conference room",
        "motion": "Slow dramatic push-in shot toward the commercial price quotation"
    },
    {
        "id": "SC065",
        "dur": 6.04,
        "words": 23,
        "text": "Do sản lượng quá thấp, xưởng cơ khí buộc phải cộng dồn toàn bộ tiền làm khuôn vào đơn giá từng linh kiện.",
        "t1": "Mô phỏng phép cộng dồn chi phí trên bảng tính chi phí kỹ thuật.",
        "t2": "Khối tiền làm khuôn dập khổng lồ được dồn toàn bộ vào một vài linh kiện ít ỏi, đẩy đơn giá của từng tấm vỏ xe vọt xà.",
        "t3": "Cú máy trượt dọc theo bảng tính cộng dồn chi phí khuôn (Tracking shot along tooling surcharge calculation).",
        "overlay": "Không",
        "subject": "a visual calculation stack showing heavy tooling capital expenditure being compressed into a tiny volume of individual body stampings",
        "setting": "a supplier cost engineering workstation",
        "motion": "Slow cinematic horizontal tracking pan across the surcharge calculation"
    },
    {
        "id": "SC066",
        "dur": 2.1,
        "words": 8,
        "text": "Phụ phí khấu hao dội ngược trở lại",
        "t1": "Đồ thị biến động đơn giá linh kiện.",
        "t2": "Mũi tên đồ họa màu đỏ cong ngược trở lại dội thẳng vào đơn giá linh kiện xuất xưởng, tạo áp lực chi phí khổng lồ.",
        "t3": "Cú máy đẩy nhanh vào mũi tên phụ phí dội ngược (Dynamic push-in on the rebounding surcharge vector).",
        "overlay": "Không",
        "subject": "a glowing red economic rebound arrow looping backward into the component pricing curve, illustrating tooling surcharge backlash",
        "setting": "an analytical cost telemetry display",
        "motion": "Slow dramatic push-in shot toward the rebounding surcharge arrow"
    },
    {
        "id": "SC067",
        "dur": 5.25,
        "words": 20,
        "text": "khiến chi phí dập tại chỗ đắt hơn rất nhiều so với linh kiện dập tại nhà máy Cát Hải",
        "t1": "Cán cân so sánh chi phí dập vỏ xe giữa hai nhà máy.",
        "t2": "Chiếc cân lệch hẳn: Phía dập tại chỗ ở Ấn Độ nặng trĩu chi phí đắt đỏ, trong khi phía linh kiện dập Cát Hải nhẹ nhàng tối ưu.",
        "t3": "Cú máy tĩnh trực diện vào chiếc cân chi phí bị lệch (Steady cost comparison scale shot) cùng text overlay.",
        "overlay": "\"DẬP TẠI CHỖ: ĐẮT HƠN NHIỀU\"",
        "subject": "an industrial comparison balance scale heavily tilted by the exorbitant cost of localized Indian stamping versus Hai Phong production",
        "setting": "an executive cost auditing boardroom",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC068",
        "dur": 4.46,
        "words": 17,
        "text": "nơi dàn khuôn đã được khấu hao trên quy mô hàng trăm ngàn chiếc xe toàn cầu.",
        "t1": "Dây chuyền dập tự động tốc độ cao tại tổ hợp Cát Hải, Hải Phòng.",
        "t2": "Dàn máy dập Schuler hiện đại dập liên tục hàng trăm ngàn chi tiết cho thị trường toàn cầu, chi phí khuôn đã được khấu hao trọn vẹn.",
        "t3": "Cú máy trượt dọc dây chuyền dập tự động tại Hải Phòng (Smooth tracking shot along Hai Phong high-speed stamping line).",
        "overlay": "Không",
        "subject": "the world-class automated Schuler stamping line operating seamlessly in Hai Phong, amortized across hundreds of thousands of global cars",
        "setting": "the flagship Cat Hai manufacturing complex",
        "motion": "Slow cinematic horizontal tracking pan across high-speed press line"
    },
    {
        "id": "SC069",
        "dur": 4.72,
        "words": 18,
        "text": "Thà chấp nhận chi tiền bồi thường để cắt lỗ chi phí chìm ngay tại khâu thử nghiệm",
        "t1": "Bàn ký kết văn bản điều hành tài chính chiến lược.",
        "t2": "Bàn tay lãnh đạo ký duyệt lệnh chi trả bồi thường để dứt khoát cắt đứt chi phí chìm ngay tại giai đoạn thử nghiệm ban đầu.",
        "t3": "Cú máy tĩnh khóa chặt văn bản lệnh cắt lỗ chi phí chìm (Steady settlement signing shot) cùng text overlay.",
        "overlay": "\"CẮT LỖ CHI PHÍ CHÌM\"",
        "subject": "an executive fountain pen signing a formal sunk-cost settlement and termination agreement on dark parchment paper",
        "setting": "an executive leadership office",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    {
        "id": "SC070",
        "dur": 4.46,
        "words": 17,
        "text": "còn hơn để những linh kiện đắt đỏ bóp nghẹt giá bán khi bước ra thị trường.",
        "t1": "Hình tượng bàn cân giá bán xe trên thị trường bán lẻ.",
        "t2": "Hình ảnh chiếc xe điện hoàn thiện thoát khỏi gánh nặng chi phí linh kiện đắt đỏ, giữ được mức giá bán lẻ cạnh tranh khi ra đại lý.",
        "t3": "Cú máy đẩy chậm vào mức giá xe được bảo vệ (Slow push-in toward the protected competitive retail price tag).",
        "overlay": "Không",
        "subject": "a sleek electric crossover silhouette liberating itself from a heavy anchor of inflated tooling surcharges, preserving competitive showroom pricing",
        "setting": "a minimalist retail automotive concept space",
        "motion": "Slow dramatic push-in shot toward the protected retail pricing"
    },
    {
        "id": "SC071",
        "dur": 5.25,
        "words": 20,
        "text": "Trong ngắn hạn, VinFast tiếp tục duy trì việc lắp ráp các bộ linh kiện CKD chuyển từ Cát Hải",
        "t1": "Bến cảng dỡ hàng Thoothukudi và kho tiếp nhận linh kiện CKD.",
        "t2": "Các xe nâng vận chuyển những kiện linh kiện CKD Cát Hải vào xưởng lắp ráp hoàn thiện, giữ nhịp độ sản xuất đều đặn.",
        "t3": "Cú máy trượt theo xe nâng chở linh kiện CKD (Tracking shot following forklift carrying CKD modules).",
        "overlay": "Không",
        "subject": "industrial forklifts transferring sea-freight CKD component crates from Cat Hai into the active assembly staging bays at Thoothukudi",
        "setting": "the inbound logistics warehouse of Thoothukudi",
        "motion": "Slow cinematic horizontal tracking pan following inbound CKD freight"
    },
    {
        "id": "SC072",
        "dur": 5.25,
        "words": 20,
        "text": "sang cho VF 6 và VF 7 để nuôi sống nhà máy Thoothukudi và bảo vệ mạng lưới đại lý.",
        "t1": "Dây chuyền lắp ráp xe VF 6 và VF 7 hoạt động liên tục.",
        "t2": "Các kỹ sư hoàn thiện từng chiếc SUV điện giao cho các xe tải vận chuyển, duy trì dòng máu nuôi sống nhà máy và hơn 60 đại lý.",
        "t3": "Cú máy trượt ngang qua những chiếc xe hoàn thiện rời dây chuyền (Slow pan across completed crossovers rolling off line).",
        "overlay": "Không",
        "subject": "finished VF 6 and VF 7 electric crossovers rolling off the assembly line into carrier bays to sustain plant operations and national dealerships",
        "setting": "the final inspection and transport yard",
        "motion": "Slow cinematic horizontal tracking pan across rolling finished vehicles"
    },
    {
        "id": "SC073",
        "dur": 5.77,
        "words": 22,
        "text": "Nhưng giải pháp dùng tàu biển chở linh kiện từ Hải Phòng liệu có thực sự là một bến đỗ an toàn?",
        "t1": "Con tàu container chở hàng CKD giữa biển đêm Ấn Độ Dương.",
        "t2": "Tàu hàng rẽ sóng trên vùng biển xanh thẫm, các thùng hàng container lắc lư nhẹ dưới bầu trời đêm u tối đầy trăn trở.",
        "t3": "Cú máy góc rộng theo dõi con tàu container lẻ loi giữa biển đêm (Wide oceanic tracking shot of cargo ship).",
        "overlay": "Không",
        "subject": "a solitary container vessel cutting through dark oceanic swells at dusk carrying maritime freight under heavy clouds",
        "setting": "the vast Indian Ocean shipping lane",
        "motion": "Slow wide tracking shot following the container freighter on dark ocean waters"
    },
    {
        "id": "SC074",
        "dur": 6.56,
        "words": 25,
        "text": "Hải trình ba ngàn hải lý này liệu có giúp họ vượt qua được chiếc thòng lọng thể chế SMEC đang đếm ngược từng ngày?",
        "t1": "Phòng nghiên cứu thể chế với đồng hồ cát SMEC và văn bản pháp luật.",
        "t2": "Đồng hồ cát thể chế SMEC bằng đồng thau với những hạt cát đỏ đang chảy xiết, đặt cạnh bản đồ hải trình 3.000 hải lý.",
        "t3": "Cú máy tĩnh trực diện vào đồng hồ cát SMEC và bản đồ hải trình (Steady macro hourglass shot) mở ra cao trào Chương 3.",
        "overlay": "Không",
        "subject": "a heavy antique brass hourglass filled with crimson sand running steadily beside an institutional SMEC treaty map and nautical route",
        "setting": "an institutional regulatory council chamber",
        "motion": "Slow dramatic push-in shot toward the running hourglass and policy treaty"
    }
]

# Write chapter_02_visual.md
md_lines = [
    "# chapter_02_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)",
    "",
    "## Episode: VinFast Ấn Độ — Thay Đổi Chiến Lược",
    "## Chương 2: Bài Toán 25.000 Xe: Cơ Chế Bóp Nghẹt Của Toán Học Khuôn Dập",
    "## Phong cách chủ đạo: Cinematic Editorial Noir (2D Vector Illustration / Graphic Novel Aesthetic - 100% Realistic Physical Spaces, No Surrealism)",
    "## Hệ màu 60-30-10:",
    "- **60% Chủ đạo (Nền/Bóng tối):** Deep Industrial Slate Grey (`#1E2522`) & Dark Charcoal (`#1A1A1A`)",
    "- **30% Bổ trợ (Kết cấu/Chủ thể):** Light Silver Grey (`#D1D5DB`) & Industrial Chrome",
    "- **10% Điểm nhấn Dẫn mắt:** Glowing Crimson Coral Red (`#EF5350`) & Neon Amber (`#F59E0B`)",
    "",
    "> **Quy tắc Text Overlay:** Chỉ chèn chữ vào đúng 8 phân cảnh mốc thông số then chốt (chiếm 23,5%). 26 phân cảnh còn lại (76,5%) để `[TEXT OVERLAY]: Không` nhằm tối đa hóa chuyển động điện ảnh linh hoạt cho camera Veo 3.1. Chữ nhỏ gọn, đặt ở vị trí cố định góc trái màn hình phía dưới, cách mép đáy 25%.",
    "",
    "---",
    "",
    "| Phân Cảnh (Scene ID) | Thời Gian & Câu Thoại Voiceover (Độ dài & Số từ) | Mô Tả Bối Cảnh Thị Giác Chi Tiết (Anatomy & Motion) | Text Overlay (Selective Typography ~20%) |",
    "| :--- | :--- | :--- | :--- |"
]

for item in ch02_matrix:
    col1 = f"**{item['id']}**"
    col2 = f"`{item['dur']}s` ({item['words']} từ)<br/>*\"{item['text']}\"*"
    col3 = f"**Tầng 1 (Đế cố định):** {item['t1']}<br/>**Tầng 2 (Bộ truyền động/Chủ thể):** {item['t2']}<br/>**Tầng 3 (Khối tác động & Góc máy):** {item['t3']}"
    col4 = f"**{item['overlay']}**"
    md_lines.append(f"| {col1} | {col2} | {col3} | {col4} |")

out_file = os.path.join(EPISODE_DIR, 'chapter_02_visual.md')
with open(out_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"Successfully generated {out_file} with {len(ch02_matrix)} scenes and exactly 8 overlays (23.5%)!")

# Now update scene_timing_map.json and build prompts_chapter_02.txt
map_path = os.path.join(EPISODE_DIR, 'scene_timing_map.json')
with open(map_path, 'r', encoding='utf-8') as f:
    scenes = json.load(f)

prompt_lines = []
ch02_dict = {item['id']: item for item in ch02_matrix}

for s in scenes:
    if s['chapter'] == '02':
        sc_id = s['id']
        item = ch02_dict[sc_id]
        ov = "" if item['overlay'] == "Không" else item['overlay'].replace('"', '').strip()
        
        s['visual_summary'] = f"{item['t1']} {item['t2']} {item['t3']}"
        s['text_overlay'] = ov
        
        if ov:
            overlay_clause = (
                f', compact subtle glowing crimson coral 3D typography text overlay '
                f'positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), '
                f'facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading "{ov}"'
            )
            motion = "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
        else:
            overlay_clause = ""
            motion = item['motion']
            
        img_prompt = (
            f"A 2D cinematic editorial noir illustration of {item['subject']}, "
            f"set in {item['setting']}, minimalist graphic novel aesthetic, clean bold ink outlines, "
            f"stylized flat vector textures, deep industrial slate grey background (#1E2522), "
            f"dramatic chiaroscuro lighting, deep noir shadows{overlay_clause}."
        )
        
        vid_prompt = (
            f"@{sc_id}.png -> {motion}, "
            f"preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, "
            f"8-second continuous documentary video --ar 16:9"
        )
        
        s['image_prompt'] = img_prompt
        s['video_prompt'] = vid_prompt
        s['camera_motion'] = motion
        
        prompt_lines.append(f"{sc_id} [IMAGE]: {img_prompt}")
        prompt_lines.append(f"{sc_id} [VIDEO]: {vid_prompt}\n")

with open(map_path, 'w', encoding='utf-8') as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

out_txt = os.path.join(EPISODE_DIR, 'prompts_chapter_02.txt')
with open(out_txt, 'w', encoding='utf-8') as f:
    f.write('\n'.join(prompt_lines))

print(f"Successfully generated prompts_chapter_02.txt with {len(prompt_lines)//2} scenes and synced scene_timing_map.json!")
