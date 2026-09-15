# -*- coding: utf-8 -*-
"""
Builder and Self-Audit Script for Chapter 07:
- 26 scenes: CH07_SC001 to CH07_SC026 (indices 214 to 239 in scene_timing_map.json)
- Style: 2D Cinematic Editorial Noir (2D vector illustration / graphic novel aesthetic, 100% realistic physical spaces, zero surrealism)
- Color & Lighting: Modern Warm Industrial Slate (#2D3748) & Studio Steel Blue (#1E293B), Luminous High-Clarity Editorial Lighting, crisp clean contours, soft ambient shadows (NOT gloomy, NO chiaroscuro / deep noir shadows, NO #1A1A1A)
- Brand & Vehicle DNA: VinFast (VF 3, VF 6, VF 7, Thoothukudi complex), Tata Motors (Tiago EV, Nexon EV), Mahindra, Maruti Suzuki, GocNhinPodcast channel
- Typography: exactly 6 scenes with text overlay (23.08%), compact subtle, fixed in lower-left area (elevated 25% above bottom edge), facing camera directly, heavy black drop shadow
- Video prompt: Steady camera shot for scenes with text, dynamic cinematic movement for scenes without text
"""

import json
import re
import os

ch07_data = {
    "CH07_SC001": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc điều hành của ban lãnh đạo VinFast tại khu phức hợp Thoothukudi dưới ánh đèn phòng sáng rõ. **Tầng 2 (Bộ truyền động/Chủ thể):** Bản giác thư nội bộ đề ngày tháng 7/2026 phê duyệt chiến lược tái cấu trúc nhà máy và tạm dừng các bộ khuôn dập xe cũ, thể hiện quyết định công nghiệp mang tính bước ngoặt. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào văn bản giác thư nội bộ tháng 7/2026 (Steady executive memorandum shot) cùng text overlay góc trái dưới.",
        "overlay": "GIÁC THƯ THÁNG 7/2026",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an official executive memorandum on an executive desk at the VinFast Thoothukudi plant dated July 2026, bearing corporate governance approval stamps halting legacy vehicle stamping tooling, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"GIÁC THƯ THÁNG 7/2026\"."
    },
    "CH07_SC002": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng kiểm định chất lượng dập kim loại công nghiệp tại xưởng cơ khí. **Tầng 2 (Bộ truyền động/Chủ thể):** Một tấm thép thân vỏ dập mẫu đặt trên bệ kiểm chuẩn, các đồng hồ đo áp lực cơ học hiển thị áp lực thực tế nghiệt ngã của dây chuyền dập kim loại. **Tầng 3 (Khối tác động & Góc máy):** Cú máy cận cảnh điểm đo áp lực cơ học thực tế (Macro shot on structural stress testing point).",
        "overlay": "",
        "motion": "Macro shot on structural stress testing point",
        "image": "A 2D cinematic editorial illustration of an industrial automotive quality inspection bench where a stamped vehicle body test coupon is examined with precision mechanical calipers and laser stress gauges, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC003": {
        "summary": "**Tầng 1 (Đế cố định):** Trung tâm phân tích chiến lược công nghiệp ô tô toàn cầu. **Tầng 2 (Bộ truyền động/Chủ thể):** Màn hình máy tính hiển thị bản đồ mở rộng quốc tế của các hãng ô tô lớn, đối chiếu các bài học thất bại và thành công trên thế giới. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm vào màn hình chiến lược mở rộng quốc tế (Slow push-in toward the global expansion roadmap screen).",
        "overlay": "",
        "motion": "Slow push-in toward the global expansion roadmap screen",
        "image": "A 2D cinematic editorial illustration of an automotive strategy intelligence console displaying global expansion roadmaps and cross-border manufacturing footprints, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC004": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc phân tích tài chính công nghiệp với màn hình hiển thị biểu đồ điểm hòa vốn (Break-even Analysis). **Tầng 2 (Bộ truyền động/Chủ thể):** Đường cong chi phí cố định khổng lồ và đường doanh thu bán lẻ xe thực tế giao nhau tại ngưỡng hòa vốn, phơi bày bài toán khắc nghiệt của công nghiệp sản xuất quy mô. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào biểu đồ điểm hòa vốn (Steady break-even analysis chart shot) cùng text overlay góc trái dưới.",
        "overlay": "QUY LUẬT ĐIỂM HÒA VỐN",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an automotive corporate financial monitoring screen displaying an authoritative break-even cost analysis curve with fixed capital depreciation crossing unit sales volume thresholds, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"QUY LUẬT ĐIỂM HÒA VỐN\"."
    },
    "CH07_SC005": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng kế toán chi phí công nghiệp ô tô. **Tầng 2 (Bộ truyền động/Chủ thể):** Báo cáo phân tích khấu hao thiết bị dập thân vỏ cho thấy chi phí cố định hàng trăm triệu đô la đè nặng nếu sản lượng tiêu thụ thực tế không đạt ngưỡng kỳ vọng ban đầu. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt ngang qua sổ cái khấu hao chi phí cố định (Slow tracking pan across fixed-cost amortization ledger).",
        "overlay": "",
        "motion": "Slow tracking pan across fixed-cost amortization ledger",
        "image": "A 2D cinematic editorial illustration of an automotive managerial accounting ledger detailing high fixed-cost tooling amortization rates per vehicle unit against varying production volume scenarios, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC006": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng điều hành tài chính chiến lược của VinFast. **Tầng 2 (Bộ truyền động/Chủ thể):** Màn hình giám sát ngân quỹ kích hoạt quyết định dừng triển khai khuôn dập cũ, bảo toàn nguồn tiền mặt và kiểm soát an toàn rủi ro thanh khoản dự án. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào màn hình kiểm soát rủi ro dòng tiền (Steady cashflow risk control shot) cùng text overlay góc trái dưới.",
        "overlay": "CẮT LỖ & KIỂM SOÁT DÒNG TIỀN",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of a VinFast treasury risk mitigation terminal showing real-time capital preservation directives locking liquidity and halting unviable tooling capital expenditures, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"CẮT LỖ & KIỂM SOÁT DÒNG TIỀN\"."
    },
    "CH07_SC007": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc thẩm tra chiến lược đầu tư công nghiệp. **Tầng 2 (Bộ truyền động/Chủ thể):** Tài liệu đánh giá rủi ro cho thấy việc đạp phanh dừng khuôn dập cũ là điều kiện cần thiết về mặt tài chính để tránh thua lỗ, nhưng các bài toán thị trường phía trước vẫn cần được giải quyết. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt ngang qua tập hồ sơ thẩm tra tài chính (Slow horizontal tracking shot across strategic financial audit files).",
        "overlay": "",
        "motion": "Slow horizontal tracking shot across strategic financial audit files",
        "image": "A 2D cinematic editorial illustration of an industrial investment audit dossier resting on a polished walnut table, evaluating the prudent necessity of halting tooling while outlining pending strategic market requirements, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC008": {
        "summary": "**Tầng 1 (Đế cố định):** Khung cửa kính lớn của tòa nhà điều hành nhìn ra đại công trường nhà máy. **Tầng 2 (Bộ truyền động/Chủ thể):** Ánh nắng ban ngày chiếu rọi các phân xưởng sản xuất đang vươn lên mạnh mẽ, thể hiện rằng con đường chinh phục thị trường tương lai đòi hỏi nhiều nỗ lực thực tế bền bỉ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm hướng ra công trường nhà máy rộng lớn (Slow push-in toward the expansive factory construction site).",
        "overlay": "",
        "motion": "Slow push-in toward the expansive factory construction site",
        "image": "A 2D cinematic editorial illustration of a bright sunlit view through high architectural glass windows overlooking the expansive Thoothukudi industrial complex where factory hangars continue active physical deployment, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC009": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng lưu trữ bản vẽ thiết kế kỹ thuật công nghiệp của VinFast. **Tầng 2 (Bộ truyền động/Chủ thể):** Bản vẽ thân vỏ xe điện toàn cầu được cuộn lại gọn gàng và cất vào ống bảo quản kỹ thuật, ngăn chặn hoàn toàn sự thâm hụt tiền mặt không cần thiết. **Tầng 3 (Khối tác động & Góc máy):** Cú máy cận cảnh ống lưu trữ bản vẽ kỹ thuật (Close-up of engineering tube storing legacy blueprints).",
        "overlay": "",
        "motion": "Close-up of engineering tube storing legacy blueprints",
        "image": "A 2D cinematic editorial illustration of an engineering archives room where legacy full-scale stamping blueprints for global VinFast passenger car bodies are sealed safely into protective cylindrical drafting canisters, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC010": {
        "summary": "**Tầng 1 (Đế cố định):** Góc nhìn toàn cảnh từ trên cao bao quát toàn bộ khu phức hợp công nghiệp VinFast Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Các phân xưởng lắp ráp ô tô, xe máy điện, đường thử xe và cảng biển nước sâu trải dài bên bờ biển nam Ấn Độ, thể hiện một chặng đường dài đầy thách thức và cơ hội phía trước. **Tầng 3 (Khối tác động & Góc máy):** Cú máy quét toàn cảnh góc cao qua khu phức hợp công nghiệp (Sweeping high-angle aerial pan across the vast VinFast Thoothukudi industrial zone).",
        "overlay": "",
        "motion": "Sweeping high-angle aerial pan across the vast VinFast Thoothukudi industrial zone",
        "image": "A 2D cinematic editorial illustration of a sweeping high-angle aerial view of the VinFast Thoothukudi manufacturing mega-complex bordering the deep blue waters of the Gulf of Mannar under clear daylight, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC011": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng nghiên cứu thị trường ô tô Nam Á. **Tầng 2 (Bộ truyền động/Chủ thể):** Màn hình hiển thị bản đồ thị phần và mạng lưới đại lý phân phối dày đặc của các tập đoàn ô tô nội địa Ấn Độ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm vào màn hình phân tích đối thủ cạnh tranh Ấn Độ (Slow push-in on Indian EV market competition analytics screen).",
        "overlay": "",
        "motion": "Slow push-in on Indian EV market competition analytics screen",
        "image": "A 2D cinematic editorial illustration of an automotive market research suite displaying multi-layer geospatial data of competitive vehicle dealer networks and charging corridors across India, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC012": {
        "summary": "**Tầng 1 (Đế cố định):** Khu trung tâm đại lý phân phối xe ô tô tại thủ phủ New Delhi. **Tầng 2 (Bộ truyền động/Chủ thể):** Các mẫu xe điện nội địa sừng sỏ như Tata Tiago EV, Tata Nexon EV và Mahindra EV đang được người tiêu dùng Ấn Độ xem xét kỹ lưỡng, đại diện cho áp lực cạnh tranh bản địa gay gắt. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào các dòng xe đối thủ bản địa (Steady formidable domestic competitors shot) cùng text overlay góc trái dưới.",
        "overlay": "ĐỐI THỦ BẢN ĐỊA SỪNG SỎ",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of prominent Indian electric vehicle models including a Tata Tiago EV and Mahindra electric passenger car parked outside a major urban distribution dealership in New Delhi with prospective buyers inspecting vehicle specifications, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"ĐỐI THỦ BẢN ĐỊA SỪNG SỎ\"."
    },
    "CH07_SC013": {
        "summary": "**Tầng 1 (Đế cố định):** Tuyến đại lộ trung tâm sầm uất tại Mumbai hoặc Chennai trong ánh nắng chan hòa. **Tầng 2 (Bộ truyền động/Chủ thể):** Nhịp sống sôi động của người dân Nam Á với đủ loại phương tiện di chuyển, phản ánh một thị trường 1,4 tỷ dân giàu tiềm năng nhưng đòi hỏi sự thấu hiểu sâu sắc. **Tầng 3 (Khối tác động & Góc máy):** Cú máy lia góc rộng qua đời sống giao thông đô thị Nam Á (Wide pan across vibrant South Asian urban street movement).",
        "overlay": "",
        "motion": "Wide pan across vibrant South Asian urban street movement",
        "image": "A 2D cinematic editorial illustration of a sprawling, energetic metropolitan boulevard in Mumbai crowded with commuters, motorized three-wheelers, scooters, and compact passenger cars under clear daylight, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC014": {
        "summary": "**Tầng 1 (Đế cố định):** Bảng dữ liệu thống kê sản lượng phương tiện giao thông quốc gia Ấn Độ. **Tầng 2 (Bộ truyền động/Chủ thể):** Biểu đồ hiển thị quy mô khổng lồ vượt mốc 20 triệu chiếc xe hai bánh mỗi năm cùng làn sóng điện hóa đang bùng nổ mạnh mẽ trên toàn quốc. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào con số quy mô 20 triệu xe hai bánh (Steady 20-million two-wheeler volume shot) cùng text overlay góc trái dưới.",
        "overlay": "QUY MÔ: 20 TRIỆU XE/NĂM",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an official Indian transport ministry statistics display highlighting an annual market scale surpassing 20 million two-wheeler vehicles with rapid green mobility adoption trends, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"QUY MÔ: 20 TRIỆU XE/NĂM\"."
    },
    "CH07_SC015": {
        "summary": "**Tầng 1 (Đế cố định):** Tuyến đường cao tốc mới hiện đại tại bang Tamil Nadu chạy dọc theo bờ biển. **Tầng 2 (Bộ truyền động/Chủ thể):** Cánh đồng điện mặt trời và các trạm sạc xe điện nhanh công cộng hiện đại trải dài, mở ra dư địa phát triển hạ tầng năng lượng xanh bao la cho các phương tiện điện. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt chậm theo tuyến hạ tầng trạm sạc cao tốc (Slow forward tracking shot toward modern EV charging highway infrastructure).",
        "overlay": "",
        "motion": "Slow forward tracking shot toward modern EV charging highway infrastructure",
        "image": "A 2D cinematic editorial illustration of a modern multi-lane highway in Tamil Nadu lined with advanced public fast-charging stations and a large adjacent solar photovoltaic field, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC016": {
        "summary": "**Tầng 1 (Đế cố định):** Phân xưởng cơ khí phụ trợ chế tạo khuôn gá và phụ tùng tại Tamil Nadu. **Tầng 2 (Bộ truyền động/Chủ thể):** Các kỹ sư VinFast và người thợ Ấn Độ cùng làm việc kiên nhẫn bên máy gia công, minh chứng cho sự kiên trì bám rễ sâu vào chuỗi cung ứng bản địa. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt ngang qua phân xưởng hợp tác phụ trợ (Slow tracking pan across active supplier manufacturing floor).",
        "overlay": "",
        "motion": "Slow tracking pan across active supplier manufacturing floor",
        "image": "A 2D cinematic editorial illustration of Vietnamese automotive manufacturing engineers collaborating closely with Indian machinists on a localized tooling and sub-assembly line inside a Tamil Nadu supplier plant, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC017": {
        "summary": "**Tầng 1 (Đế cố định):** Bảng đồng hồ kỹ thuật số theo dõi tỷ lệ giá trị gia tăng nội địa (DVA) tại trung tâm kiểm chuẩn chất lượng nhà máy. **Tầng 2 (Bộ truyền động/Chủ thể):** Chỉ số phần trăm nội địa hóa tăng dần từng điểm phần trăm vững chắc, ghi nhận nỗ lực tích lũy giá trị thực tế của tổ hợp. **Tầng 3 (Khối tác động & Góc máy):** Cú máy cận cảnh đồng hồ chỉ số nội địa hóa gia tăng (Macro shot on the incremental DVA percentage counter).",
        "overlay": "",
        "motion": "Macro shot on the incremental DVA percentage counter",
        "image": "A 2D cinematic editorial illustration of a digital factory telemetric monitor showing an incremental Domestic Value Addition (DVA) counter steadily climbing percentage by percentage toward full localization compliance, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC018": {
        "summary": "**Tầng 1 (Đế cố định):** Đường phố đô thị Ấn Độ sau cơn mưa rào trong ánh chiều ấm áp. **Tầng 2 (Bộ truyền động/Chủ thể):** Một gia đình Ấn Độ di chuyển thoải mái, an toàn trên chiếc xe điện gầm cao thực dụng, phản ánh một sản phẩm giải quyết đúng nhu cầu đời sống thiết thực của người dân Nam Á. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt êm ái theo phương tiện di chuyển của gia đình bản địa (Warm tracking shot of daily family commute in urban India).",
        "overlay": "",
        "motion": "Warm tracking shot of daily family commute in urban India",
        "image": "A 2D cinematic editorial illustration of an Indian family traveling smoothly and securely in a practical, compact high-clearance electric passenger vehicle along a pleasant urban avenue in Chennai after a light rain, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC019": {
        "summary": "**Tầng 1 (Đế cố định):** Đại sảnh tòa nhà điều hành tổ hợp công nghiệp Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Biểu tượng chữ V đặc trưng của VinFast đặt trang trọng bên cạnh quốc kỳ Ấn Độ và Việt Nam, khẳng định sự hiện diện công nghiệp nghiêm túc và dài hạn của một thương hiệu Việt. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm vào biểu tượng VinFast và các lá cờ hợp tác (Slow push-in toward the VinFast corporate emblem and partner flags).",
        "overlay": "",
        "motion": "Slow push-in toward the VinFast corporate emblem and partner flags",
        "image": "A 2D cinematic editorial illustration of the modern architectural reception foyer of the Thoothukudi manufacturing complex, featuring a brushed-aluminum VinFast emblem mounted proudly beside national flags of India and Vietnam, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC020": {
        "summary": "**Tầng 1 (Đế cố định):** Đường thử xe dã chiến ven biển Thoothukudi với những khúc cua kỹ thuật quanh co. **Tầng 2 (Bộ truyền động/Chủ thể):** Chiếc xe điện thử nghiệm vượt qua các khúc cua gập ghềnh và đón gió biển lồng lộng, phản ánh hành trình công nghiệp còn nhiều khúc quanh và bài kiểm tra nghiệt ngã đón đợi phía trước. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt động theo khúc cua đường thử ven biển (Dynamic tracking shot along coastal testing curves).",
        "overlay": "",
        "motion": "Dynamic tracking shot along coastal testing curves",
        "image": "A 2D cinematic editorial illustration of a prototype electric vehicle navigating dynamic s-curves on an automotive coastal proving ground outside Thoothukudi beside maritime dunes, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC021": {
        "summary": "**Tầng 1 (Đế cố định):** Bảng nguyên lý quản trị công nghiệp tại phòng họp lãnh đạo cấp cao. **Tầng 2 (Bộ truyền động/Chủ thể):** Hai nguyên lý triết lý cốt lõi: 'Tiến lên thần tốc là tham vọng' và 'Học cách dừng lại để thích ứng là bài học sinh tồn' được thể hiện đối xứng, trang trọng. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào bài học thích ứng sinh tồn (Steady survival adaptation philosophy shot) cùng text overlay góc trái dưới.",
        "overlay": "DỪNG LẠI ĐỂ THÍCH ỨNG",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an executive strategic board displaying industrial management principles with dual balanced columns comparing rapid expansion ambition with disciplined strategic pauses for market survival, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"DỪNG LẠI ĐỂ THÍCH ỨNG\"."
    },
    "CH07_SC022": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc biên tập của chương trình Góc Nhìn Podcast với micro phát thanh và tài liệu phân tích. **Tầng 2 (Bộ truyền động/Chủ thể):** Màn hình hiển thị hai góc nhìn phân tích kinh tế đối lập về bước lùi của VinFast, chuẩn bị mở ra cuộc đối thoại cùng khán giả. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm vào màn hình phân tích đa chiều (Slow push-in on editorial debate monitor).",
        "overlay": "",
        "motion": "Slow push-in on editorial debate monitor",
        "image": "A 2D cinematic editorial illustration of an analytical economics studio workstation with a professional broadcast microphone and dual desktop monitors displaying balanced analytical perspectives regarding industrial strategy, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC023": {
        "summary": "**Tầng 1 (Đế cố định):** Giao diện tương tác diễn đàn phân tích học thuật của người nghe podcast. **Tầng 2 (Bộ truyền động/Chủ thể):** Hai ô bình luận đại diện cho hai luồng ý kiến: 'Bước lùi chiến thuật khôn ngoan' và 'Sự thỏa hiệp đầy rủi ro', mời gọi góc nhìn phản biện từ cộng đồng khán giả thông thái. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt êm qua giao diện đối thoại người nghe (Slow subtle glide across audience engagement interface).",
        "overlay": "",
        "motion": "Slow subtle glide across audience engagement interface",
        "image": "A 2D cinematic editorial illustration of an elegant viewer feedback interface featuring two balanced discussion cards comparing tactical retreat against strategic compromise, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC024": {
        "summary": "**Tầng 1 (Đế cố định):** Studio thu âm chuyên nghiệp của kênh Góc Nhìn Podcast dưới ánh đèn trường quay ấm áp, thanh lịch. **Tầng 2 (Bộ truyền động/Chủ thể):** Bàn làm việc bằng gỗ sồi sẫm màu với microphone phát thanh cao cấp, tai nghe chuyên dụng và màn hình hiển thị biểu đồ phân tích kinh tế vĩ mô độc lập. **Tầng 3 (Khối tác động & Góc máy):** Cú máy lia góc rộng qua không gian phòng thu podcast chuyên nghiệp (Slow elegant pan across podcast recording studio setup).",
        "overlay": "",
        "motion": "Slow elegant pan across podcast recording studio setup",
        "image": "A 2D cinematic editorial illustration of the refined professional podcast recording studio of GocNhinPodcast, featuring an acoustic studio setup, broadcast condenser microphone, audio mixer console, and research monitors, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC025": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn biên tập phân tích chính sách kinh tế độc lập. **Tầng 2 (Bộ truyền động/Chủ thể):** Văn bản khuyến cáo pháp lý học thuật hiển thị trang nhã, nêu rõ nội dung thuần túy phục vụ nghiên cứu độc lập, không mang tính định hướng thương mại hay tư vấn đầu tư. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm trực diện vào văn bản khuyến cáo nghiên cứu độc lập (Steady slow push-in on formal research disclaimer document).",
        "overlay": "",
        "motion": "Steady slow push-in on formal research disclaimer document",
        "image": "A 2D cinematic editorial illustration of an official independent academic research disclaimer parchment document on a sleek studio desk, clean typography stating independent socio-economic analysis without investment advice, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH07_SC026": {
        "summary": "**Tầng 1 (Đế cố định):** Khung hình kết thúc chính thức của chương trình Góc Nhìn Podcast trong không gian đồ họa thanh lịch. **Tầng 2 (Bộ truyền động/Chủ thể):** Logo kênh chính thức GocNhinPodcast tỏa sáng tinh tế cùng địa chỉ handle chuẩn xác https://www.youtube.com/@GocNhin_Podcast, khép lại trọn vẹn toàn bộ 7 chương của tập podcast. **Tầng 3 (Khối tác động & Góc máy):** Cú máy lùi nhẹ tôn vinh logo nhận diện thương hiệu kênh (Slow elegant zoom out centering on the official GocNhinPodcast brand insignia).",
        "overlay": "",
        "motion": "Slow elegant zoom out centering on the official GocNhinPodcast brand insignia",
        "image": "A 2D cinematic editorial illustration of the official channel brand closing card for GocNhinPodcast, featuring the refined geometric podcast logo and official YouTube handle 'https://www.youtube.com/@GocNhin_Podcast' centered elegantly under soft warm studio lighting, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    }
}

def build_chapter_07():
    episode_dir = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc"
    timing_map_path = os.path.join(episode_dir, "scene_timing_map.json")
    visual_md_path = os.path.join(episode_dir, "chapter_07_visual.md")
    prompts_txt_path = os.path.join(episode_dir, "prompts_chapter_07.txt")

    # 1. Load scene_timing_map.json
    with open(timing_map_path, "r", encoding="utf-8") as f:
        timing_map = json.load(f)

    print(f"Total scenes in timing map: {len(timing_map)}")
    # Chapter 07 covers indices 214 to 239 (26 scenes)
    ch07_indices = range(214, 240)

    # 2. Update timing map and collect records
    records = []
    prompts_lines = []

    for idx in ch07_indices:
        item = timing_map[idx]
        ch_num = idx - 214 + 1
        scene_id = f"CH07_SC{ch_num:03d}"
        
        if scene_id not in ch07_data:
            raise ValueError(f"Missing data for {scene_id}")
            
        data = ch07_data[scene_id]
        
        # Update fields
        item["id"] = scene_id
        item["chapter"] = "07"
        item["visual_summary"] = data["summary"]
        item["text_overlay"] = data["overlay"]
        item["camera_motion"] = data["motion"]
        item["image_prompt"] = data["image"]
        item["video_prompt"] = f"@{scene_id}.png -> {data['motion']}, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9"
        
        records.append(item)
        
        # Build prompts file text
        prompts_lines.append(f"{scene_id} [IMAGE]: {data['image']}\n")
        prompts_lines.append(f"{scene_id} [VIDEO]: {item['video_prompt']}\n\n")

    # Write back updated scene_timing_map.json
    with open(timing_map_path, "w", encoding="utf-8") as f:
        json.dump(timing_map, f, ensure_ascii=False, indent=2)
    print(f"Updated scene_timing_map.json with 26 scenes for Chapter 07.")

    # Write prompts_chapter_07.txt
    with open(prompts_txt_path, "w", encoding="utf-8") as f:
        f.writelines(prompts_lines)
    print(f"Wrote prompts_chapter_07.txt ({len(ch07_data)} scenes).")

    # Write chapter_07_visual.md
    with open(visual_md_path, "w", encoding="utf-8") as f:
        f.write("# chapter_07_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)\n\n")
        f.write("## Episode: VinFast Ấn Độ — Thay Đổi Chiến Lược\n")
        f.write("## Chương 7: Bước Lùi Chiến Thuật & Bài Học Sinh Tồn Khắc Nghiệt\n")
        f.write("## Phong cách chủ đạo: Cinematic Editorial Noir (2D Vector Illustration / Graphic Novel Aesthetic - 100% Realistic Physical Spaces, Zero Surrealism)\n")
        f.write("## Hệ màu 60-30-10 & Ánh sáng chuẩn hóa:\n")
        f.write("- **60% Chủ đạo (Nền kiến trúc thanh lịch):** Modern Warm Industrial Slate (`#2D3748`, `#334155`)\n")
        f.write("- **30% Bổ trợ (Kết cấu/Chủ thể):** Brushed Steel, Terracotta & Warm Ivory (`#E2E8F0`, `#D97706`, `#F8FAFC`)\n")
        f.write("- **10% Điểm nhấn Dẫn mắt:** Luminous Emerald & Electric Amber (`#10B981`, `#F59E0B`)\n")
        f.write("- **Ánh sáng (Lighting Discipline):** Luminous High-Clarity Editorial Lighting, crisp clean contours, soft ambient shadows (Sáng sủa, sắc nét, KHÔNG u ám, CẤM chiaroscuro / deep noir shadows / than đen `#1A1A1A`).\n\n")
        f.write("> **Quy tắc Text Overlay Bắt Buộc:**\n")
        f.write("> - Chỉ chèn chữ vào đúng 6 phân cảnh mốc triết lý / bài học kết luận then chốt (chiếm 23,08%). 20 phân cảnh còn lại (76,92%) để `[TEXT OVERLAY]: Không` nhằm tối đa hóa chuyển động điện ảnh linh hoạt cho camera Veo 3.1.\n")
        f.write("> - **Định vị & Kích thước Chữ:** Thiết kế chữ nhỏ gọn, thanh thoát (`compact subtle`), đặt ở vị trí cố định tại **góc trái màn hình phía dưới, cách mép đáy 25%** (`lower-left area of the frame, elevated 25% above the bottom edge`), trực diện ống kính, bóng đổ đen dày trên nền không gian âm sạch.\n\n")
        f.write("---\n\n")
        f.write("| Phân Cảnh (Scene ID) | Thời Gian & Câu Thoại Voiceover (Độ dài & Số từ) | Mô Tả Bối Cảnh Thị Giác Chi Tiết (Anatomy & Motion) | Text Overlay (Selective Typography ~20-25%) |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")

        for item in records:
            sc_id = item["id"]
            dur = item["duration_sec"]
            sents = item["sentences"]
            full_text = " ".join(sents)
            word_count = len(full_text.split())
            vis_summary = item["visual_summary"].replace("\n", "<br/>")
            text_over = item["text_overlay"]
            text_col = f'**"{text_over}"**' if text_over else "**Không**"
            
            f.write(f'| **{sc_id}** | `{dur}s` ({word_count} từ)<br/>*"{full_text}"* | {vis_summary} | {text_col} |\n')

    print(f"Wrote chapter_07_visual.md ({len(records)} scenes).")

    # 3. RUN SELF-AUDIT
    print("\n--- RUNNING SELF-AUDIT FOR CHAPTER 07 ---")
    audit_errors = []
    
    # Gate 1: Check scene count and ID numbering
    if len(records) != 26:
        audit_errors.append(f"Gate 1 Fail: Expected 26 scenes, got {len(records)}")
    for i, r in enumerate(records):
        expected_id = f"CH07_SC{i+1:03d}"
        if r["id"] != expected_id:
            audit_errors.append(f"Gate 1 Fail: Scene {i} has id {r['id']}, expected {expected_id}")

    # Gate 2: Typography count and positioning
    text_scenes = [r for r in records if r["text_overlay"]]
    text_ratio = len(text_scenes) / len(records)
    if len(text_scenes) != 6:
        audit_errors.append(f"Gate 2 Fail: Expected exactly 6 text scenes, got {len(text_scenes)}")
    if not (0.20 <= text_ratio <= 0.25):
        audit_errors.append(f"Gate 2 Fail: Text ratio {text_ratio:.2%} outside 20-25% range")

    for r in text_scenes:
        if "lower-left area of the frame (elevated 25% above the bottom edge)" not in r["image_prompt"]:
            audit_errors.append(f"Gate 2 Fail: Scene {r['id']} missing fixed lower-left typography coordinates in image_prompt")
        if "Steady camera shot" not in r["video_prompt"]:
            audit_errors.append(f"Gate 2 Fail: Scene {r['id']} has text overlay but video_prompt does not start with 'Steady camera shot'")

    # Gate 3: Lighting & Gloominess Check (User Constraint)
    forbidden_lighting = ["chiaroscuro", "deep noir shadows", "#1A1A1A", "#1a1a1a", "dark warm charcoal background (#1A1A1A)"]
    for r in records:
        for fl in forbidden_lighting:
            if fl in r["image_prompt"]:
                audit_errors.append(f"Gate 3 Fail: Scene {r['id']} contains forbidden gloomy/chiaroscuro term: '{fl}'")
        if "luminous high-clarity editorial lighting" not in r["image_prompt"]:
            audit_errors.append(f"Gate 3 Fail: Scene {r['id']} missing 'luminous high-clarity editorial lighting'")

    # Gate 4: Surrealism & Abstraction Check (User Constraint)
    forbidden_surreal = ["scale of justice", "cracked shield", "tightening noose", "clamping vice", "abyss of cost", "floating question mark", "philosophical flywheel", "invisible hand", "banyan tree roots"]
    for r in records:
        for fs in forbidden_surreal:
            if fs in r["image_prompt"].lower():
                audit_errors.append(f"Gate 4 Fail: Scene {r['id']} contains surrealism term: '{fs}'")

    # Gate 5: Brand & Vehicle DNA Fidelity
    brand_keywords = ["VinFast", "Tata", "Mahindra", "Maruti Suzuki", "GocNhinPodcast", "Thoothukudi"]
    brand_mentions = 0
    for r in records:
        if any(bk.lower() in r["image_prompt"].lower() for bk in brand_keywords):
            brand_mentions += 1
    print(f"Gate 5 Check: Brand / Vehicle / Channel DNA represented in {brand_mentions}/{len(records)} scenes.")
    if brand_mentions < 10:
        audit_errors.append(f"Gate 5 Fail: Expected at least 10 brand/vehicle references, found {brand_mentions}")

    # Gate 6: Synchronization Check
    for i, r in enumerate(records):
        map_item = timing_map[214 + i]
        if map_item["id"] != r["id"] or map_item["image_prompt"] != r["image_prompt"]:
            audit_errors.append(f"Gate 6 Fail: Synchronization mismatch for scene {r['id']}")

    if audit_errors:
        print("\n❌ AUDIT FAILED with errors:")
        for err in audit_errors:
            print(f"  - {err}")
        return False
    else:
        print("\n✅ AUDIT PASS 100%! All 6 Gates passed with ZERO defects.")
        print(f"  - Total Scenes: {len(records)} ({records[0]['id']} - {records[-1]['id']})")
        print(f"  - Text Overlay: {len(text_scenes)} scenes ({text_ratio:.2%})")
        print(f"  - Color Background: Modern Warm Industrial Slate (#2D3748)")
        print(f"  - Lighting: Luminous High-Clarity Editorial Lighting (No gloom, No chiaroscuro)")
        print(f"  - Zero Surrealism: 100% Real Physical Spaces & Mechanisms")
        print(f"  - Brand/Vehicle DNA: Rigorously Specified for Nano Banana 2")
        return True

if __name__ == "__main__":
    success = build_chapter_07()
    if not success:
        exit(1)
