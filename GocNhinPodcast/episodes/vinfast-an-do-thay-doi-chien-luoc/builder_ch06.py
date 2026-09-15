# -*- coding: utf-8 -*-
"""
Builder and Self-Audit Script for Chapter 06:
- 34 scenes: CH06_SC001 to CH06_SC034 (indices 180 to 213 in scene_timing_map.json)
- Style: 2D Cinematic Editorial Noir (2D vector illustration / graphic novel aesthetic, 100% realistic physical spaces, zero surrealism)
- Color & Lighting: Modern Warm Industrial Slate (#2D3748) & Terracotta Ochre (#D97706), Luminous High-Clarity Editorial Lighting, crisp clean contours, soft ambient shadows (NOT gloomy, NO chiaroscuro / deep noir shadows, NO #1A1A1A)
- Brand & Vehicle DNA: Ford, General Motors, Maruti Suzuki (800 / Swift), VinFast VF 6 & VF 7, Bespoke Indian LFP EV
- Typography: exactly 8 scenes with text overlay (23.53%), compact subtle, fixed in lower-left area (elevated 25% above bottom edge), facing camera directly, heavy black drop shadow
- Video prompt: Steady camera shot for scenes with text, dynamic cinematic movement for scenes without text
"""

import json
import re
import os

ch06_data = {
    "CH06_SC001": {
        "summary": "**Tầng 1 (Đế cố định):** Khuôn viên nhà máy lắp ráp ô tô bỏ hoang của các tập đoàn phương Tây (như General Motors tại Halol hay Ford tại Maraimalai Nagar) tại vùng ngoại ô công nghiệp Ấn Độ dưới bầu trời sáng rõ. **Tầng 2 (Bộ truyền động/Chủ thể):** Những khối nhà xưởng kết cấu thép cũ kỹ bạc màu và sân bãi trống trải phủ lớp bụi đất, minh chứng thực tế cho các tượng đài ô tô ngoại quốc từng thất bại. **Tầng 3 (Khối tác động & Góc máy):** Cú máy quét góc thấp qua khu nhà xưởng cũ (Slow tracking pan across abandoned plant remnants).",
        "overlay": "",
        "motion": "Slow tracking pan across abandoned plant remnants",
        "image": "A 2D cinematic editorial illustration of an expansive abandoned Western automotive assembly plant complex such as General Motors or Ford in an Indian industrial suburb under a clear bright sky, faded steel-frame hangars and empty staging tarmac with dust drifts, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC002": {
        "summary": "**Tầng 1 (Đế cố định):** Showroom đại lý ô tô phương Tây tại một thành phố lớn của Ấn Độ. **Tầng 2 (Bộ truyền động/Chủ thể):** Những chiếc xe SUV Ford Endeavour và sedan Chevrolet Cruze nhập khẩu nguyên bản cồng kềnh đứng bên trong kính, hoàn toàn không tương thích với những ngõ phố đông đúc và đường gồ ghề bên ngoài. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt ngang qua những chiếc xe toàn cầu cồng kềnh (Horizontal tracking pan framing out-of-place Western cars).",
        "overlay": "",
        "motion": "Horizontal tracking pan framing out-of-place Western cars",
        "image": "A 2D cinematic editorial illustration of a polished automotive showroom in an Indian metropolis displaying bulky Western global models including a large Ford Endeavour SUV and a Chevrolet Cruze sedan behind glass windows, visually contrasted with crowded bustling streets outside, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC003": {
        "summary": "**Tầng 1 (Đế cố định):** Cổng chính nhà máy sản xuất ô tô Ford tại Sanand, bang Gujarat. **Tầng 2 (Bộ truyền động/Chủ thể):** Cánh cổng sắt công nghiệp đóng kín có dán thông báo ngừng hoạt động và chuyển giao tài sản sau những khoản lỗ hàng tỷ đô la của Ford. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào cổng nhà máy đóng kín (Steady shot on locked factory gates) cùng text overlay góc trái dưới.",
        "overlay": "RÚT LUI: MẤT HÀNG TỶ USD",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of the closed main security gate of the Ford automotive manufacturing plant in Sanand Gujarat, featuring an official decommissioning handover notice mounted on industrial iron gates, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"RÚT LUI: MẤT HÀNG TỶ USD\"."
    },
    "CH06_SC004": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng họp ban điều hành chiến lược của các tập đoàn ô tô đa quốc gia phương Tây như Ford và General Motors. **Tầng 2 (Bộ truyền động/Chủ thể):** Các nhà điều hành phương Tây đứng cạnh bản vẽ xe toàn cầu, hoàn toàn tách biệt khỏi các báo cáo thực địa về hạ tầng giao thông và sức mua khắt khe của Ấn Độ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm từ phía sau các nhà điều hành hướng vào tấm bản đồ (Slow push-in on boardroom executives).",
        "overlay": "",
        "motion": "Slow push-in on boardroom executives",
        "image": "A 2D cinematic editorial illustration of a multinational automotive executive boardroom for Ford and General Motors executives reviewing global car engineering blueprints while overlooking actual topographic transport maps of India, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC005": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc kỹ thuật ô tô với cuốn cẩm nang thông số xe tiêu chuẩn thị trường Mỹ và Châu Âu của Ford và GM. **Tầng 2 (Bộ truyền động/Chủ thể):** Báo cáo thực nghiệm hỏng hóc hệ thống giảm xóc và quá nhiệt động cơ đặt cạnh cuốn cẩm nang, phơi bày sự không tương thích của các mẫu xe toàn cầu. **Tầng 3 (Khối tác động & Góc máy):** Cú máy cận cảnh cuốn cẩm nang và báo cáo thực nghiệm bản địa (Macro shot on Western specifications manual and local road test report).",
        "overlay": "",
        "motion": "Macro shot on Western specifications manual and local road test report",
        "image": "A 2D cinematic editorial illustration of an automotive engineering desk displaying a standard American and European vehicle specification catalog from Ford and General Motors alongside local field engineering durability test reports detailing chassis stress and engine heat dissipation under harsh Indian road conditions, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC006": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng phân tích dữ liệu ngành công nghiệp ô tô Ấn Độ (SIAM). **Tầng 2 (Bộ truyền động/Chủ thể):** Bảng số liệu thị phần quốc gia hiển thị cột mốc áp đảo trên 40% thị phần thuộc về liên doanh Maruti Suzuki suốt nhiều thập kỷ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào biểu đồ thị phần 40% (Steady national market share dominance shot) cùng text overlay góc trái dưới.",
        "overlay": "MARUTI SUZUKI: > 40% THỊ PHẦN",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an Indian automotive market analytics room featuring an illuminated national market share chart where Maruti Suzuki commands an overwhelming market share column exceeding 40 percent, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"MARUTI SUZUKI: > 40% THỊ PHẦN\"."
    },
    "CH06_SC007": {
        "summary": "**Tầng 1 (Đế cố định):** Tuyến đại lộ đô thị sôi động của Ấn Độ trong ánh ban mai rực rỡ. **Tầng 2 (Bộ truyền động/Chủ thể):** Dòng xe hatchback Maruti Suzuki 800 và Maruti Suzuki Swift nhỏ gọn, thực dụng di chuyển bền bỉ trên khắp các ngả đường như biểu tượng ô tô quốc dân. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt mượt mà theo dòng xe Maruti Suzuki (Smooth tracking shot following the iconic national car).",
        "overlay": "",
        "motion": "Smooth tracking shot following the iconic national car",
        "image": "A 2D cinematic editorial illustration of a sunlit Indian metropolitan thoroughfare filled with resilient, practical Maruti Suzuki 800 and Maruti Suzuki Swift hatchback cars smoothly navigating city traffic as the undisputed national car icon, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC008": {
        "summary": "**Tầng 1 (Đế cố định):** Bức tường biên niên sử công nghiệp tại nhà máy Maruti Suzuki. **Tầng 2 (Bộ truyền động/Chủ thể):** Mốc thời gian bốn thập kỷ kiên nhẫn bám rễ (1983 - 2023) được khắc trên tấm kim loại công nghiệp của Maruti Suzuki, ghi dấu hành trình xây dựng chuỗi cung ứng bản địa sâu rộng. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh khóa chặt mốc lịch sử 40 năm (Steady four-decade historical inscription shot) cùng text overlay góc trái dưới.",
        "overlay": "BÀI HỌC: 40 NĂM BÁM RỄ",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an industrial chronicle wall at a historic Maruti Suzuki automobile plant displaying an engraved steel milestone marking four decades of patient localization from 1983 to 2023, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"BÀI HỌC: 40 NĂM BÁM RỄ\"."
    },
    "CH06_SC009": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc kỹ thuật cơ khí Maruti Suzuki với các tập tài liệu máy móc tự động hóa phức tạp của Suzuki Tokyo được xếp gọn gàng sang một bên. **Tầng 2 (Bộ truyền động/Chủ thể):** Các kỹ sư Suzuki quyết định không nhập khẩu nguyên si dây chuyền công nghệ đắt đỏ từ Tokyo, mà tìm kiếm giải pháp cơ khí thực dụng có thể bảo dưỡng tại chỗ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy lùi nhẹ khỏi các bản thiết kế phức tạp (Slow pull-back leaving complex foreign machines aside).",
        "overlay": "",
        "motion": "Slow pull-back leaving complex foreign machines aside",
        "image": "A 2D cinematic editorial illustration of a Maruti Suzuki engineering planning desk where overly intricate automated robotics schematics from Suzuki Tokyo headquarters are neatly filed away in favor of practical local manufacturing equipment, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC010": {
        "summary": "**Tầng 1 (Đế cố định):** Không gian xưởng cơ khí gia công phụ tùng địa phương tại vùng ngoại ô Ấn Độ. **Tầng 2 (Bộ truyền động/Chủ thể):** Một kỹ sư cơ khí người Nhật của Suzuki trong trang phục bảo hộ cùng người thợ Ấn Độ đứng cạnh máy tiện kim loại, cẩn thận đo đạc và hướng dẫn căn chỉnh từng thông số gá đặt linh kiện. **Tầng 3 (Khối tác động & Góc máy):** Cú máy cận cảnh người cố vấn và thợ máy địa phương cùng làm việc (Close-up of mentor and local mechanic working side-by-side).",
        "overlay": "",
        "motion": "Close-up of mentor and local mechanic working side-by-side",
        "image": "A 2D cinematic editorial illustration of a Japanese Suzuki automotive engineering mentor in clean workwear working alongside an experienced Indian machinist beside a conventional metal lathe in a suburban component workshop, calibrating tooling fixtures together, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC011": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn thiết kế xe hơi Maruti Suzuki tích hợp năng lực chuỗi cung ứng bản địa. **Tầng 2 (Bộ truyền động/Chủ thể):** Các chi tiết linh kiện cơ khí giá rẻ sản xuất nội địa được các kỹ sư Suzuki đo đạc và đưa trực tiếp vào bản vẽ kỹ thuật của chiếc xe, tối ưu hóa theo năng lực chuỗi cung ứng sẵn có. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt ngang qua các chi tiết phụ trợ bản địa (Slow tracking pan along low-cost local components).",
        "overlay": "",
        "motion": "Slow tracking pan along low-cost local components",
        "image": "A 2D cinematic editorial illustration of a Maruti Suzuki vehicle drafting table where affordable locally fabricated steel brackets, stamped linkages, and wiring connectors are measured and integrated directly into the vehicle chassis CAD drawing, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC012": {
        "summary": "**Tầng 1 (Đế cố định):** Bản vẽ mặt cắt kỹ thuật hệ thống gầm và hệ thống treo của xe Maruti Suzuki. **Tầng 2 (Bộ truyền động/Chủ thể):** Khoảng sáng gầm xe được thiết kế nâng cao rõ rệt với lò xo chịu tải dày dặn, giúp xe dễ dàng vượt qua các cung đường gồ ghề và ngập nước. **Tầng 3 (Khối tác động & Góc máy):** Cú máy nâng góc cận cảnh vào khoảng sáng gầm xe (Macro tilt-up on high ground clearance chassis).",
        "overlay": "",
        "motion": "Macro tilt-up on high ground clearance chassis",
        "image": "A 2D cinematic editorial illustration of a technical cutaway blueprint of a Maruti Suzuki vehicle suspension and reinforced ladder chassis showing high ground clearance and heavy-duty load-bearing coil springs tailored for rough terrain, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC013": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng thử nghiệm linh kiện xe nhiệt đới hóa của Maruti Suzuki. **Tầng 2 (Bộ truyền động/Chủ thể):** Cụm lốp xe gai dày chịu đường xấu đặt cạnh cụm dàn điều hòa công suất cực mạnh đang thổi luồng khí mát, sẵn sàng đối mặt với cái nóng mùa hè 50 độ C. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt từ cụm lốp sang lốc điều hòa công suất lớn (Pan from rugged tires to high-power climate blower).",
        "overlay": "",
        "motion": "Pan from rugged tires to high-power climate blower",
        "image": "A 2D cinematic editorial illustration of a Maruti Suzuki automotive climate adaptation test chamber, showcasing heavy-tread rugged tires beside an oversized automotive air-conditioning compressor blowing crisp cooling air, designed to withstand intense 50-degree-Celsius heat, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC014": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc ban lãnh đạo dự án VinFast tại văn phòng điều hành. **Tầng 2 (Bộ truyền động/Chủ thể):** Cuốn cẩm nang phân tích bài học 40 năm nội địa hóa của Maruti Suzuki được mở ra, trở thành kim chỉ nam chiến lược cho các quyết định công nghiệp của VinFast. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm vào tập tài liệu bài học Suzuki (Slow push-in on the Suzuki industrial lesson dossier).",
        "overlay": "",
        "motion": "Slow push-in on the Suzuki industrial lesson dossier",
        "image": "A 2D cinematic editorial illustration of a VinFast corporate strategy desk where an analytical case study dossier titled 'Four Decades of Maruti Suzuki Localization in India' lies open under bright office illumination, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC015": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc điều hành dự án VinFast tháng 7 năm 2026. **Tầng 2 (Bộ truyền động/Chủ thể):** Văn bản nội bộ chính thức của VinFast phê duyệt việc tạm dừng triển khai bộ khuôn dập xe điện cũ (cho VF 6 và VF 7), kịp thời đạp phanh để tránh lãng phí nguồn vốn khổng lồ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào quyết định tạm dừng khuôn dập (Steady strategic brake-tap order shot) cùng text overlay góc trái dưới.",
        "overlay": "QUYẾT ĐỊNH ĐẠP PHANH (07/2026)",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an official VinFast executive memorandum dated July 2026 formally approving the strategic halt of vehicle stamping die fabrication for VF 6 and VF 7, stamped with executive corporate approval on a clean executive desk, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"QUYẾT ĐỊNH ĐẠP PHANH (07/2026)\"."
    },
    "CH06_SC016": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn vẽ thiết kế kỹ thuật ô tô công nghiệp của VinFast. **Tầng 2 (Bộ truyền động/Chủ thể):** Bản vẽ thiết kế thân vỏ khuôn dập cũ của VinFast VF 6 và VF 7 không phù hợp được cất vào ống lưu trữ hồ sơ, mở ra một bản vẽ kỹ thuật mới để bắt đầu thiết kế lại từ đầu cho thị trường Ấn Độ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy dứt khoát chuyển sang tờ giấy thiết kế mới (Decisive pan to fresh drafting paper).",
        "overlay": "",
        "motion": "Decisive pan to fresh drafting paper",
        "image": "A 2D cinematic editorial illustration of a VinFast automotive engineering drafting table where global body stamping blueprints for VinFast VF 6 and VF 7 are rolled up and stored away, making room for a clean fresh blueprint sheet ready for ground-up Indian market redesign, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC017": {
        "summary": "**Tầng 1 (Đế cố định):** Phòng hội thảo chiến lược kỹ thuật của VinFast tại tổ hợp Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Màn hình hiển thị lộ trình chuyển dịch mang tính sống còn: Từ bỏ việc mang nguyên mẫu xe toàn cầu sang bán, chuyển sang thiết kế xe VinFast may đo theo thực tế thị trường Ấn Độ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm vào màn hình chiến lược chuyển đổi (Slow forward tracking shot toward strategic roadmap screen).",
        "overlay": "",
        "motion": "Slow forward tracking shot toward strategic roadmap screen",
        "image": "A 2D cinematic editorial illustration of a technical design conference room at the VinFast Thoothukudi complex, where an illuminated digital roadmap screen outlines the vital operational shift from rigid global models to locally adapted VinFast electric vehicles, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC018": {
        "summary": "**Tầng 1 (Đế cố định):** Studio thiết kế tạo dáng xe hơi của VinFast. **Tầng 2 (Bộ truyền động/Chủ thể):** Các nhà thiết kế tạo hình mô hình đất sét của một mẫu xe điện VinFast nhỏ gọn gầm cao, mang các đường nét khí động học tối giản và đặc trưng thẩm mỹ phù hợp với người dùng Nam Á. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm vào mẫu xe đất sét đang thành hình (Slow push-in on bespoke Indian EV clay model).",
        "overlay": "",
        "motion": "Slow push-in on bespoke Indian EV clay model",
        "image": "A 2D cinematic editorial illustration of a VinFast automotive styling studio where automotive designers sculpt a 1:5 clay scale model of a bespoke compact high-ground-clearance VinFast electric SUV tailored for Indian city streets, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC019": {
        "summary": "**Tầng 1 (Đế cố định):** Bảng thuyết trình nguyên lý công nghiệp hiện đại: Design-for-Supply-Chain. **Tầng 2 (Bộ truyền động/Chủ thể):** Sơ đồ chuỗi cung ứng phụ trợ địa phương kết nối đồng bộ trực tiếp với từng cụm chi tiết trên khung gầm xe VinFast, thể hiện triết lý thiết kế dựa trên chuỗi cung ứng. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào triết lý thiết kế chuỗi cung ứng (Steady supply-chain design philosophy shot) cùng text overlay góc trái dưới.",
        "overlay": "THIẾT KẾ THEO CHUỖI CUNG ỨNG",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an industrial engineering presentation wall displaying the methodology 'Design-for-Supply-Chain', linking local tier-1 Indian supplier component nodes directly into modular VinFast vehicle frame assemblies, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THIẾT KẾ THEO CHUỖI CUNG ỨNG\"."
    },
    "CH06_SC020": {
        "summary": "**Tầng 1 (Đế cố định):** Phân xưởng cơ khí phụ trợ gia công kim loại bản địa tại Tamil Nadu. **Tầng 2 (Bộ truyền động/Chủ thể):** Các xưởng cơ khí vận hành máy chấn tôn và máy phay kim loại thông dụng, không còn bị đè nặng bởi những bản vẽ đòi hỏi dung sai siêu phức tạp vượt ngoài tầm máy móc sẵn có. **Tầng 3 (Khối tác động & Góc máy):** Cú máy lùi nhẹ giải tỏa áp lực máy móc (Slow pull-back easing mechanical pressure).",
        "overlay": "",
        "motion": "Slow pull-back easing mechanical pressure",
        "image": "A 2D cinematic editorial illustration of an active Indian Tier-2 sheet metal stamping and machining shop in Tamil Nadu operating standard press brakes and CNC milling tools reliably for VinFast structural parts without unmanageable micro-tolerance demands, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC021": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc quản lý chi phí của xưởng phụ trợ địa phương hợp tác cùng VinFast. **Tầng 2 (Bộ truyền động/Chủ thể):** Báo cáo kế hoạch tài chính cho thấy các xưởng không phải gánh rủi ro vốn khổng lồ cho những bộ khuôn dập thân vỏ mới đắt đỏ, tạo sự an tâm gắn kết dài lâu. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt ngang qua bảng cân đối vốn được giải tỏa (Horizontal glide across relieved capital risk sheet).",
        "overlay": "",
        "motion": "Horizontal glide across relieved capital risk sheet",
        "image": "A 2D cinematic editorial illustration of an Indian supplier financial balance sheet showing zero heavy capital debt expenditure for massive customized VinFast tooling dies, stamped with approval in a Tamil Nadu manufacturing plant office, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC022": {
        "summary": "**Tầng 1 (Đế cố định):** Dây chuyền gia công cơ khí của các đối tác sản xuất bản địa. **Tầng 2 (Bộ truyền động/Chủ thể):** Các máy dập uốn và máy cắt laser sẵn có của đối tác Ấn Độ vận hành mượt mà tạo ra các chi tiết kết cấu thép cho chiếc xe VinFast tương lai mà không cần đầu tư máy mới. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt theo các chi tiết thép được gia công dễ dàng (Smooth tracking pan along locally fabricated steel parts).",
        "overlay": "",
        "motion": "Smooth tracking pan along locally fabricated steel parts",
        "image": "A 2D cinematic editorial illustration of an Indian supplier manufacturing line smoothly forming modular steel subframes and stamped panels for a VinFast electric car using existing laser cutters and hydraulic presses, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC023": {
        "summary": "**Tầng 1 (Đế cố định):** Đường thử xe thực địa đa địa hình quanh khu phức hợp Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Mẫu xe điện VinFast thử nghiệm ngụy trang di chuyển chắc chắn trên đường sỏi đá gập ghềnh, chứng minh sự tối ưu hóa vượt trội cho điều kiện vận hành thực tế. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm theo bước tiến của chiếc xe mẫu (Slow forward tracking shot of prototype).",
        "overlay": "",
        "motion": "Slow forward tracking shot of prototype",
        "image": "A 2D cinematic editorial illustration of a camouflaged VinFast electric passenger prototype vehicle navigating a rugged gravel and undulating test road outside Thoothukudi with ease, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC024": {
        "summary": "**Tầng 1 (Đế cố định):** Buồng thử nghiệm nhiệt độ cực đoan trong phòng lab R&D ô tô VinFast. **Tầng 2 (Bộ truyền động/Chủ thể):** Khối pin LFP (Lithium Iron Phosphate) hoạt động ổn định trong môi trường nhiệt độ lên tới 50 độ C, các thông số kỹ thuật và nhiệt kế buồng sấy hiển thị an toàn tuyệt đối. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào khối pin LFP và nhiệt kế 50°C (Steady thermal resilience shot) cùng text overlay góc trái dưới.",
        "overlay": "PIN LFP: CHỊU NHIỆT 50°C",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of a heavy-duty VinFast Lithium Iron Phosphate (LFP) battery pack undergoing stress testing inside a specialized environmental thermal chamber calibrated at 50 degrees Celsius, with digital telemetry screens indicating complete thermal stability, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"PIN LFP: CHỊU NHIỆT 50°C\"."
    },
    "CH06_SC025": {
        "summary": "**Tầng 1 (Đế cố định):** Bể thử lội nước sâu mô phỏng mùa mưa bão ngập lụt Monsoon tại Ấn Độ. **Tầng 2 (Bộ truyền động/Chủ thể):** Mẫu xe SUV điện VinFast với khoảng sáng gầm cao và khối pin đạt chuẩn kín nước IP67 lướt băng băng qua làn nước ngập sâu an toàn mà không hề chập điện. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh khóa góc nhìn vào chiếc xe lội nước dũng mãnh (Steady water-wading test shot) cùng text overlay góc trái dưới.",
        "overlay": "GẦM CAO & KÍN NƯỚC: CHỐNG LỤT",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of a VinFast electric SUV with high ground clearance and an IP67 waterproof sealed battery compartment powering steadily through a deep water-wading test trough simulating Indian monsoon floods, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"GẦM CAO & KÍN NƯỚC: CHỐNG LỤT\"."
    },
    "CH06_SC026": {
        "summary": "**Tầng 1 (Đế cố định):** Bảng tính toán phân tích chi phí sản xuất xe VinFast may đo theo chuỗi cung ứng. **Tầng 2 (Bộ truyền động/Chủ thể):** Đường cong đơn giá sản xuất tụt giảm mạnh xuống mức cực kỳ cạnh tranh nhờ tối đa hóa linh kiện giá rẻ sẵn có từ các đối tác Ấn Độ. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy nhanh vào mức giá thành sản xuất tối ưu (Dynamic push-in on ultra-competitive production cost tag).",
        "overlay": "",
        "motion": "Dynamic push-in on ultra-competitive production cost tag",
        "image": "A 2D cinematic editorial illustration of a VinFast industrial cost breakdown dashboard showing unit manufacturing costs dropping sharply under supply-chain-tailored architecture, achieving peak price competitiveness, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC027": {
        "summary": "**Tầng 1 (Đế cố định):** Văn phòng thẩm định tiêu chuẩn công nghiệp của chính phủ Ấn Độ. **Tầng 2 (Bộ truyền động/Chủ thể):** Hồ sơ chứng nhận tỷ lệ nội địa hóa (DVA) của VinFast đạt chuẩn theo các quy định khắt khe của New Delhi, mở đường cho các ưu đãi sản xuất trong nước. **Tầng 3 (Khối tác động & Góc máy):** Cú máy nâng nhẹ từ giấy chứng nhận ra toàn cảnh nhà xưởng (Tilt-up from certificate to factory floor).",
        "overlay": "",
        "motion": "Tilt-up from certificate to factory floor",
        "image": "A 2D cinematic editorial illustration of an official domestic value addition (DVA) certification document for VinFast bearing official government compliance stamps resting on a desk with the active Thoothukudi factory floor visible through the window, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC028": {
        "summary": "**Tầng 1 (Đế cố định):** Tầng cao nhất của tòa nhà điều hành nhà máy VinFast Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Khung cửa kính lớn nhìn ra toàn cảnh bến cảng nước sâu quốc tế và biển Ấn Độ Dương bao la, mở ra một tầm nhìn chiến lược vượt khỏi biên giới quốc gia. **Tầng 3 (Khối tác động & Góc máy):** Cú máy đẩy chậm từ sau lưng hướng ra đường chân trời biển khơi (Slow forward tracking shot toward oceanic horizon).",
        "overlay": "",
        "motion": "Slow forward tracking shot toward oceanic horizon",
        "image": "A 2D cinematic editorial illustration of an executive planning suite on the upper floor of the VinFast Thoothukudi plant overlooking the nearby international deep-water seaport and the vast sunlit expanse of the Indian Ocean, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC029": {
        "summary": "**Tầng 1 (Đế cố định):** Vùng duyên hải Thoothukudi với những cánh đồng điện gió khổng lồ của bang Tamil Nadu. **Tầng 2 (Bộ truyền động/Chủ thể):** Các tua-bin gió trắng muốt quay đều trong gió biển, cung cấp nguồn năng lượng sạch dồi dào trực tiếp vào tổ hợp nhà máy VinFast bên cạnh cảng nước sâu quốc tế V.O. Chidambaranar. **Tầng 3 (Khối tác động & Góc máy):** Cú máy lia góc rộng từ cánh đồng điện gió sang bến cảng nước sâu (Wide sweeping pan from coastal wind farm to deep-water port).",
        "overlay": "",
        "motion": "Wide sweeping pan from coastal wind farm to deep-water port",
        "image": "A 2D cinematic editorial illustration of a sweeping coastal landscape in Thoothukudi Tamil Nadu, showing towering white offshore wind turbines spinning gracefully under bright skies, feeding clean electricity to the adjacent VinFast portside manufacturing complex, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC030": {
        "summary": "**Tầng 1 (Đế cố định):** Cầu cảng chuyên dụng xuất khẩu xe điện (Ro-Ro terminal) tại cảng Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Biển hiệu đại bản doanh ghi nhận tổ hợp là Cứ điểm Xuất khẩu Xanh (Green Export Hub), các xe điện VinFast sản xuất tại chỗ xếp hàng ngay ngắn chuẩn bị lên tàu hàng hải. **Tầng 3 (Khối tác động & Góc máy):** Cú máy tĩnh trực diện vào biển hiệu cứ điểm xuất khẩu xanh (Steady green export hub terminal shot) cùng text overlay góc trái dưới.",
        "overlay": "CỨ ĐIỂM XUẤT KHẨU XANH",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject",
        "image": "A 2D cinematic editorial illustration of an active automotive roll-on/roll-off (Ro-Ro) maritime export terminal at Thoothukudi port with an official architectural signage reading 'VinFast Green Export Logistics Hub', VinFast electric vehicles staged neatly beside an ocean carrier, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warm amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"CỨ ĐIỂM XUẤT KHẨU XANH\"."
    },
    "CH06_SC031": {
        "summary": "**Tầng 1 (Đế cố định):** Trung tâm điều hành logistics xuất khẩu tại tổ hợp VinFast Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Màn hình hiển thị bản đồ thị trường nội địa 1,4 tỷ dân Ấn Độ với hàng trăm tuyến phân phối xe điện VinFast tỏa đi khắp các bang. **Tầng 3 (Khối tác động & Góc máy):** Cú máy quét qua bản đồ thị trường nội địa 1,4 tỷ dân (Slow pan across vast domestic market map).",
        "overlay": "",
        "motion": "Slow pan across vast domestic market map",
        "image": "A 2D cinematic editorial illustration of a VinFast export logistics control room displaying an illuminated map of the vast 1.4-billion-population domestic Indian consumer market, tracing distribution conduits connecting Thoothukudi to northern and western states, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC032": {
        "summary": "**Tầng 1 (Đế cố định):** Tuyến luồng hàng hải quốc tế khởi hành từ cảng Thoothukudi. **Tầng 2 (Bộ truyền động/Chủ thể):** Tàu chở xe chuyên dụng rẽ sóng chở các xe điện VinFast hướng về các thị trường đang phát triển tại Nam Á, Trung Đông và Châu Phi, hiện thực hóa chiến lược xuất khẩu toàn cầu. **Tầng 3 (Khối tác động & Góc máy):** Cú máy trượt ngang theo các tuyến hải trình xuất khẩu quốc tế (Horizontal tracking pan across maritime export routes).",
        "overlay": "",
        "motion": "Horizontal tracking pan across maritime export routes",
        "image": "A 2D cinematic editorial illustration of a modern automotive car-carrier ship sailing smoothly from Thoothukudi into deep blue waters carrying VinFast vehicles, tracing navigational maritime shipping routes toward South Asia, the Middle East, and East Africa, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC033": {
        "summary": "**Tầng 1 (Đế cố định):** Bàn làm việc chiến lược công nghiệp của VinFast với bản đồ quy hoạch và bản vẽ thiết kế trên giấy. **Tầng 2 (Bộ truyền động/Chủ thể):** Luồng gió biển thổi nhẹ góc giấy bản vẽ, bên ngoài cửa sổ là khung cảnh công trường nhộn nhịp, nhắc nhở rằng vẽ viễn cảnh trên giấy luôn dễ hơn chinh phục thực tế nghiệt ngã. **Tầng 3 (Khối tác động & Góc máy):** Cú máy cận cảnh góc giấy bản vẽ bay nhẹ trong gió (Macro shot of blueprint fluttering in sea breeze).",
        "overlay": "",
        "motion": "Macro shot of blueprint fluttering in sea breeze",
        "image": "A 2D cinematic editorial illustration of a VinFast industrial strategy desk where paper blueprints and export masterplans rest beside an open window, sea breeze gently rustling the paper edges with the bustling coastal port and factory site visible outside, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    },
    "CH06_SC034": {
        "summary": "**Tầng 1 (Đế cố định):** Bến cảng công nghiệp Thoothukudi bên cạnh nhà máy VinFast trong ráng chiều hoàng hôn buông xuống. **Tầng 2 (Bộ truyền động/Chủ thể):** Ánh đèn ngọn hải đăng quét nhịp nhàng qua mặt nước biển Ấn Độ Dương, đặt ra câu hỏi lớn mở đường bước vào khúc vĩ thanh Chương 7. **Tầng 3 (Khối tác động & Góc máy):** Cú máy ngước nhìn luồng sáng ngọn hải đăng cảng biển (Slow upward tilt to sweeping lighthouse beam).",
        "overlay": "",
        "motion": "Slow upward tilt to sweeping lighthouse beam",
        "image": "A 2D cinematic editorial illustration of the Thoothukudi coastal harbor adjacent to the VinFast complex at dusk, a harbor lighthouse beam sweeping rhythmically across the darkening ocean waters, setting an evocative, reflective visual mood for the final chapter, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern warm industrial slate background (#2D3748), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows."
    }
}

def build_chapter_06():
    episode_dir = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc"
    timing_map_path = os.path.join(episode_dir, "scene_timing_map.json")
    visual_md_path = os.path.join(episode_dir, "chapter_06_visual.md")
    prompts_txt_path = os.path.join(episode_dir, "prompts_chapter_06.txt")

    # 1. Load scene_timing_map.json
    with open(timing_map_path, "r", encoding="utf-8") as f:
        timing_map = json.load(f)

    print(f"Total scenes in timing map: {len(timing_map)}")
    # Chapter 06 covers indices 180 to 213 (34 scenes)
    ch06_indices = range(180, 214)

    # 2. Update timing map and collect records
    records = []
    prompts_lines = []

    for idx in ch06_indices:
        item = timing_map[idx]
        ch_num = idx - 180 + 1
        scene_id = f"CH06_SC{ch_num:03d}"
        
        if scene_id not in ch06_data:
            raise ValueError(f"Missing data for {scene_id}")
            
        data = ch06_data[scene_id]
        
        # Update fields
        item["id"] = scene_id
        item["chapter"] = "06"
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
    print(f"Updated scene_timing_map.json with 34 scenes for Chapter 06.")

    # Write prompts_chapter_06.txt
    with open(prompts_txt_path, "w", encoding="utf-8") as f:
        f.writelines(prompts_lines)
    print(f"Wrote prompts_chapter_06.txt ({len(ch06_data)} scenes).")

    # Write chapter_06_visual.md
    with open(visual_md_path, "w", encoding="utf-8") as f:
        f.write("# chapter_06_visual.md — KỊCH BẢN THỊ GIÁC TRUNG GIAN (STORYBOARD MATRIX)\n\n")
        f.write("## Episode: VinFast Ấn Độ — Thay Đổi Chiến Lược\n")
        f.write("## Chương 6: Bài Học 40 Năm Maruti Suzuki: May Đo Chuỗi Cung Ứng & Cứ Điểm Xuất Khẩu Xanh\n")
        f.write("## Phong cách chủ đạo: Cinematic Editorial Noir (2D Vector Illustration / Graphic Novel Aesthetic - 100% Realistic Physical Spaces, Zero Surrealism)\n")
        f.write("## Hệ màu 60-30-10 & Ánh sáng chuẩn hóa:\n")
        f.write("- **60% Chủ đạo (Nền kiến trúc thanh lịch):** Modern Warm Industrial Slate (`#2D3748`, `#334155`)\n")
        f.write("- **30% Bổ trợ (Kết cấu/Chủ thể):** Terracotta Ochre & Industrial Steel (`#D97706`, `#E2E8F0`)\n")
        f.write("- **10% Điểm nhấn Dẫn mắt:** Luminous Emerald & Electric Amber (`#10B981`, `#F59E0B`)\n")
        f.write("- **Ánh sáng (Lighting Discipline):** Luminous High-Clarity Editorial Lighting, crisp clean contours, soft ambient shadows (Sáng sủa, sắc nét, KHÔNG u ám, CẤM chiaroscuro / deep noir shadows / than đen `#1A1A1A`).\n\n")
        f.write("> **Quy tắc Text Overlay Bắt Buộc:**\n")
        f.write("> - Chỉ chèn chữ vào đúng 8 phân cảnh mốc triết lý / bài học then chốt (chiếm 23,53%). 26 phân cảnh còn lại (76,47%) để `[TEXT OVERLAY]: Không` nhằm tối đa hóa chuyển động điện ảnh linh hoạt cho camera Veo 3.1.\n")
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

    print(f"Wrote chapter_06_visual.md ({len(records)} scenes).")

    # 3. RUN SELF-AUDIT
    print("\n--- RUNNING SELF-AUDIT FOR CHAPTER 06 ---")
    audit_errors = []
    
    # Gate 1: Check scene count and ID numbering
    if len(records) != 34:
        audit_errors.append(f"Gate 1 Fail: Expected 34 scenes, got {len(records)}")
    for i, r in enumerate(records):
        expected_id = f"CH06_SC{i+1:03d}"
        if r["id"] != expected_id:
            audit_errors.append(f"Gate 1 Fail: Scene {i} has id {r['id']}, expected {expected_id}")

    # Gate 2: Typography count and positioning
    text_scenes = [r for r in records if r["text_overlay"]]
    text_ratio = len(text_scenes) / len(records)
    if len(text_scenes) != 8:
        audit_errors.append(f"Gate 2 Fail: Expected exactly 8 text scenes, got {len(text_scenes)}")
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
    brand_keywords = ["Ford", "General Motors", "Chevrolet", "Maruti Suzuki", "VinFast", "LFP"]
    brand_mentions = 0
    for r in records:
        if any(bk.lower() in r["image_prompt"].lower() for bk in brand_keywords):
            brand_mentions += 1
    print(f"Gate 5 Check: Brand / Vehicle DNA represented in {brand_mentions}/{len(records)} scenes.")
    if brand_mentions < 10:
        audit_errors.append(f"Gate 5 Fail: Expected at least 10 brand/vehicle references, found {brand_mentions}")

    # Gate 6: Synchronization Check
    for i, r in enumerate(records):
        map_item = timing_map[180 + i]
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
    success = build_chapter_06()
    if not success:
        exit(1)
