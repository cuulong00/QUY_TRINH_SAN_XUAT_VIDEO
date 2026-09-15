import json

scenes_data = [
    (
        "CH07_SC001", 5.83,
        "Every night on commercial satellite radars, phantom shapes move silently across the high seas.",
        "Màn hình radar vệ tinh thương mại hiển thị các vệt sáng tàu bè không tên di chuyển bí ẩn trong bóng đêm trên các vùng biển quốc tế.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a commercial synthetic aperture radar (SAR) satellite display in a dark maritime monitoring room. Unidentified phantom ship signatures glow as faint amber contacts moving silently across deep ocean blackness, unlinked to any registered vessel tracking database. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal radar slate (#0B0F19) and glowing amber satellite blips, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC001.png -> Slow push-in dolly shot toward the dark satellite radar screen as unflagged ship blips drift across open waters, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC002", 3.75,
        "Giant oil tankers, rusting and stripped of corporate logos",
        "Thân vỏ gỉ sét của một siêu tàu chở dầu 18 năm tuổi, tên tàu và logo doanh nghiệp bị cạo xóa sơn đè lem luốc.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the weathered, rust-streaked steel hull of an aging crude oil tanker. Former corporate shipping logos and previous vessel names have been crudely painted over in thick matte black primer, cutting slowly through dark ocean swells under gray coastal skies. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, weathered steel rust tones, deep maritime slate (#1E293B), and seawater froth, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC002.png -> Slow macro tracking shot along the rusted, freshly painted-over ship hull plates, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC003", 6.67,
        "glide through international waters with their automatic identification transponders switched off. This is the Shadow Fleet.",
        "Đài chỉ huy tối om của tàu dầu bóng ma, bàn tay thuyền trưởng gạt công tắc tắt hệ thống nhận dạng tự động AIS; Hạm đội Bóng tối lộ diện.",
        "THE SHADOW FLEET", "T2V",
        "A 2D warm cinematic editorial illustration inside the darkened wheelhouse of a clandestine crude carrier. A ship officer's hand switches off the red toggle switch of the Automatic Identification System (AIS) transponder, plunging the vessel into electronic invisibility as the giant dark silhouette sails through international waters. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal bridge slate (#0B0F19) and red instrument console glow, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing warning coral red 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THE SHADOW FLEET\", no watermarks, 16:9",
        "@CH07_SC003.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward focus on the dark unmonitored instrument panel, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC004", 3.33,
        "According to maritime data from Lloyd's List Intelligence",
        "Trung tâm tình báo hàng hải Lloyd's List Intelligence tại London, các chuyên viên phân tích theo dõi bản đồ di biến động tàu bóng ma toàn cầu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside the maritime intelligence research suite of Lloyd's List Intelligence in London. Senior maritime analysts review global vessel tracking databases and vessel ownership networks on wide multi-screen displays under sophisticated office lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, distinguished British research slate (#2A323D) and warm ivory cream parchment (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC004.png -> Slow push-in dolly shot toward the glowing global fleet tracking console, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC005", 4.58,
        "this clandestine armada has swelled to between 650 and 850 vessels.",
        "Hạm đội bóng ma ngầm đã phình to lên từ 650 đến 850 tàu, tạo thành một đạo quân hàng hải ngầm khổng lồ trên khắp đại dương.",
        "650 - 850 VESSELS (LLOYD'S)", "T2V",
        "A 2D warm cinematic editorial illustration of a global maritime tracking heat map. Hundreds of orange and red vessel icons, representing an armada of 650 to 850 clandestine shadow tankers, scatter across international shipping routes outside Western control. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep oceanic slate (#1E293B) and glowing orange fleet clusters (#F59E0B), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"650 - 850 VESSELS (LLOYD'S)\", no watermarks, 16:9",
        "@CH07_SC005.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow orbital drift revealing the global dispersion of the shadow fleet, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC006", 5.42,
        "It represents more than eleven percent of the world's entire crude tanker capacity.",
        "Biểu đồ trọng tải tàu dầu thế giới: Hạm đội bóng ma chiếm hơn 11% tổng trọng tải tàu chở dầu thô toàn cầu.",
        "> 11% OF GLOBAL TANKER FLEET", "T2V",
        "A 2D warm cinematic editorial illustration of an analytical maritime tonnage bar chart. A substantial dark iron-red column representing more than eleven percent of the entire global crude tanker fleet capacity is highlighted in stark contrast to compliant Western fleets. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark institutional slate (#1E293B) and contrasting amber-gold data markers (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"> 11% OF GLOBAL TANKER FLEET\", no watermarks, 16:9",
        "@CH07_SC006.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward tilt emphasizing the scale of the eleven percent fleet segment, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC007", 6.25,
        "These ships are corporate ghosts. They average more than fifteen to eighteen years of age",
        "Những con tàu 'bóng ma doanh nghiệp' già cỗi 15 đến 18 năm tuổi, máy móc rệu rã nhưng vẫn chạy hết công suất ngoài khơi xa.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an aging Aframax crude tanker plowing through heavy seas at twilight. Deep rust stains streak down its high black steel freeboard, and worn deck machinery displays the signs of nearly two decades of continuous commercial service. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, weathered maritime iron slate (#1E293B) and frothy ocean waves (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC007.png -> Slow low-angle tracking shot beside the rusted bow cutting through the choppy swell, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC008", 3.75,
        "far beyond the retirement threshold of Western shipping companies.",
        "Vượt xa ngưỡng thanh lý của các hãng tàu phương Tây, các con tàu cũ kỹ được tân trang tạm bợ để chở dầu né trừng phạt.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the worn engine room control console and auxiliary machinery aboard a decommissioned-era tanker, where analog gauges tremble at high pressure under flickering maintenance lights. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial engine slate (#1E293B) and brass pressure gauges, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC008.png -> Slow push-in dolly shot toward the vibrating analog pressure gauges, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC009", 5.42,
        "They register under flags of convenience in nations like Gabon, Panama, and Liberia.",
        "Chứng chỉ đăng ký tàu treo cờ tiện lợi của Gabon, Panama và Liberia đặt trên bàn luật sư hàng hải, che giấu chủ sở hữu thực sự.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of official maritime registry certificates stamped under flags of convenience: the maritime administrations of Gabon, Panama, and Liberia lying open on a mahogany desk alongside brass ship seals, concealing beneficial ownership. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream registry paper (#FAF7EE) and rich mahogany wood, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC009.png -> Slow macro pan across the stamped flag-of-convenience seals and official registry certificates, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC010", 5.42,
        "They operate entirely without Western maritime insurance, Western financing, or Western tracking systems.",
        "Tàu bóng ma hoạt động hoàn toàn độc lập: Không bảo hiểm P&I phương Tây, không tài chính ngân hàng Mỹ-Âu, không thiết bị giám sát phương Tây.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an unflagged tanker sailing through open ocean under heavy gray clouds, accompanied by three stylized severed connection icons representing the absence of Western P&I insurance, Western bank financing, and Western GPS tracking. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, cold oceanic slate (#0F172A) and stark white vector outlines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC010.png -> Slow forward camera drift above the autonomous tanker cutting cleanly through gray waters, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC011", 2.92,
        "Their primary operational technique is ship-to-ship transfer.",
        "Kỹ thuật tác chiến cốt lõi: Sang mạn dầu giữa biển khơi (Ship-to-Ship Transfer - STS), hai siêu tàu áp sát mạn nhau.",
        "SHIP-TO-SHIP (STS) TRANSFER", "T2V",
        "A 2D warm cinematic editorial illustration of a nighttime Ship-to-Ship (STS) crude oil transfer operation on the high seas. Two colossal oil supertankers are moored directly alongside each other, separated by massive pneumatic rubber Yokohama fenders floating in calm black water. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, nocturnal ocean slate (#0B0F19), industrial red hulls, and yellow deck floodlights, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"SHIP-TO-SHIP (STS) TRANSFER\", no watermarks, 16:9",
        "@CH07_SC011.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow push-in dolly toward the two hulls moored together, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC012", 4.17,
        "In the international waters of the Laconian Gulf off Greece",
        "Vùng biển quốc tế vịnh Laconian ngoài khơi bán đảo Peloponnese, Hy Lạp: Nơi các tàu dầu bóng ma thường xuyên sang mạn dầu Nga.",
        "LACONIAN GULF, GREECE", "T2V",
        "A 2D warm cinematic editorial illustration of the sheltered international waters of the Laconian Gulf off the coast of the Peloponnese peninsula in Greece. The rugged Mediterranean coastline rises in the dusk background as pairs of dark oil tankers anchor offshore under tranquil twilight skies. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, Mediterranean twilight slate (#1E293B) and warm ivory cream sky tones (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"LACONIAN GULF, GREECE\", no watermarks, 16:9",
        "@CH07_SC012.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow high-angle aerial drift over the quiet gulf waters, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC013", 6.67,
        "and along the outer approaches to the Strait of Malacca these tankers moor side-by-side in darkness.",
        "Cửa ngõ ngoài khơi eo biển Malacca gần quần đảo Riau, các tàu dầu áp sát mạn nhau trong bóng đêm dày đặc để chuyển dầu.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of dark shadow tankers anchored side-by-side in the outer maritime approaches to the Strait of Malacca near the Indonesian Riau Islands under dense tropical midnight darkness, their work lights casting pale yellow reflections on calm equatorial waters. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep tropical midnight slate (#0B0F19) and muted yellow deck lights, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC013.png -> Slow lateral camera pan past the two darkened ship hulls linked by mooring lines, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC014", 5.42,
        "They pump millions of barrels of sanctioned Russian and Iranian crude between hulls",
        "Đường ống cao su công nghiệp áp lực cao bơm hàng triệu thùng dầu thô Nga và Iran từ tàu này sang tàu khác dưới ánh đèn boong.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of heavy industrial flexible rubber transfer hoses suspended between the midship manifolds of two tankers. High-pressure pumps pulse rhythmically as millions of barrels of dark sanctioned crude oil are transferred from one ship's holds to another. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial deck slate (#1E293B) and glistening petroleum black hues, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC014.png -> Slow macro push-in on the thick pulsing oil transfer hoses connected between the ship manifolds, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC015", 4.58,
        "blending origins and falsifying paperwork before docking at refineries in Asia.",
        "Tập vận đơn giả mạo được đóng dấu thay đổi nguồn gốc xuất xứ tại Singapore/Malaysia trước khi tàu cập cảng lọc dầu Sơn Đông, Trung Quốc.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a shipping agent's desk where a falsified bill of lading is stamped with official-looking customs seals falsely claiming blended Malaysian or Oman origin, prepared for delivery to independent coastal refineries in Shandong, China. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream parchment (#FAF7EE) and dark emerald customs ink, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC015.png -> Slow downward focus pull onto the stamped false origin clause on the shipping document, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC016", 6.25,
        "To settle these transactions, buyers and sellers abandoned Western clearinghouses. They built alternative financial rails.",
        "Từ bỏ các trung tâm thanh toán phương Tây, mạng lưới đường ray tài chính ngầm kết nối Moscow, Bắc Kinh, New Delhi và Dubai được kích hoạt.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an alternative global financial clearing network. Luminous non-Western financial rails bypass traditional New York and London correspondent banking hubs, establishing direct monetary links between Moscow, Beijing, New Delhi, and Dubai. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep geopolitical slate (#1E293B) and glowing amber financial conduits, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC016.png -> Slow orbital drift tracing the glowing alternative payment routes bypassing the Atlantic, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC017", 4.17,
        "China expanded its Cross-Border Interbank Payment System, known as CIPS.",
        "Trung tâm vận hành Hệ thống Thanh toán Liên ngân hàng Xuyên biên giới CIPS tại Thượng Hải, các máy chủ thanh toán bù trừ Nhân dân tệ sáng đèn liên tục.",
        "CIPS (SHANGHAI)", "T2V",
        "A 2D warm cinematic editorial illustration inside the main operations center of the Cross-Border Interbank Payment System (CIPS) in Shanghai, China. Modern multi-screen trading desks process real-time cross-border settlements in Chinese Yuan, bypassing the SWIFT messaging system. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, sophisticated Asian financial slate (#1E293B) and jade green digital telemetry lines (#26A69A), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing emerald green 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"CIPS (SHANGHAI)\", no watermarks, 16:9",
        "@CH07_SC017.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow camera pan across the digital settlement monitors, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC018", 4.58,
        "Central banks experimented with mBridge, a multi-central bank digital currency platform.",
        "Giao diện nền tảng tiền kỹ thuật số đa ngân hàng trung ương mBridge (BIS Innovation Hub), thanh toán trực tiếp giữa các đồng tiền số.",
        "mBRIDGE PLATFORM", "T2V",
        "A 2D warm cinematic editorial illustration of the mBridge multi-central bank digital currency platform interface. Interlocking digital currency nodes representing the central banks of China, Thailand, the UAE, and Hong Kong settle cross-border trade transactions instantaneously without intermediating through the US dollar. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, high-tech fintech slate (#0F172A) and glowing cyan and amber circuit lines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"mBRIDGE PLATFORM\", no watermarks, 16:9",
        "@CH07_SC018.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow zoom into the central cross-border transaction node, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC019", 5.0,
        "Oil contracts were settled in Chinese yuan, Russian roubles, and Indian rupees.",
        "Hợp đồng mua bán dầu thô đa tiền tệ: Các xấp tiền Nhân dân tệ, Rúp Nga và Rupee Ấn Độ đặt cạnh nhau trên bàn thương thảo dầu mỏ.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a multi-currency energy sales agreement lying upon an executive trading desk. Bound contracts are flanked by neat bundles of Chinese Yuan, Russian Roubles, and Indian Rupees, representing the emergence of non-dollar bilateral oil trade. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, rich walnut desk, warm ivory cream contract paper (#FAF7EE), and colorful sovereign banknotes, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC019.png -> Slow macro tracking shot across the three national currency stacks and the signed petroleum contract, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC020", 6.67,
        "For advocates of rapid de-dollarization, this was heralded as the beginning of a post-American monetary order.",
        "Hội nghị thượng đỉnh BRICS tại Johannesburg hoặc Kazan, các nhà lãnh đạo nâng ly chúc mừng trật tự tiền tệ đa cực trên khán đài quốc tế.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an international summit hall during a BRICS economic forum in Kazan or Johannesburg. Delegations from non-aligned nations gather before a massive multimedia backdrop proclaiming multipolar monetary sovereignty under triumphant warm golden stage lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, distinguished conference slate (#2A323D) and warm celebratory amber (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC020.png -> Slow push-in dolly shot toward the illuminated international summit stage, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC021", 5.42,
        "But beneath the rhetoric, this parallel system collided with an immovable financial barrier.",
        "Phía sau ánh hào quang tuyên truyền: Hệ thống song phương đụng phải một bức tường đá kiên cố sừng sững không thể vượt qua.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration depicting the harsh friction beneath the geopolitical rhetoric. Flowing alternative currency streams crash abruptly against a massive, immovable granite financial retaining wall under somber, analytical lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark institutional granite slate (#1E293B) and cold stone textures, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC021.png -> Slow forward camera push-in halting right at the imposing face of the granite barrier, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC022", 2.5,
        "Economists call this the Non-Convertibility Wall.",
        "Khái niệm cốt lõi: 'Bức Tường Bất Khả Chuyển Đổi' được khắc sâu trên phiến đá cẩm thạch đen tại một viện nghiên cứu kinh tế học.",
        "THE NON-CONVERTIBILITY WALL", "T2V",
        "A 2D warm cinematic editorial illustration of a monumental black marble architectural monolith engraved with the economic principle 'THE NON-CONVERTIBILITY WALL', illuminated by a sharp, focused beam of white overhead gallery light. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, polished black granite slate (#0F172A) and crisp engraved white stone lettering, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"THE NON-CONVERTIBILITY WALL\", no watermarks, 16:9",
        "@CH07_SC022.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward focus on the engraved stone title, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC023", 5.0,
        "When India purchased hundreds of millions of barrels of discounted Russian crude",
        "Cảng dầu Vadinar tại Gujarat, Ấn Độ tiếp nhận các siêu tàu chở dầu thô Urals giá rẻ từ Nga cập cầu cảng dỡ hàng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the industrial crude oil import terminal at Vadinar in Gujarat, India. Colossal tankers discharge discounted Russian Urals crude oil through heavy dockside pipes into coastal storage tank farms under a warm tropical sun. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep maritime slate (#1E293B), storage tank white (#FAF7EE), and sunlit coastal waters, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC023.png -> Slow high-angle aerial crane shot gliding past the storage tanks toward the docked tankers, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC024", 6.67,
        "it insisted on paying in Indian rupees. Within months, Russian oil exporters accumulated tens of billions",
        "Ấn Độ kiên quyết thanh toán bằng đồng Rupee; sau vài tháng, các nhà xuất khẩu dầu Nga tích lũy hàng chục tỷ USD giá trị tiền Rupee.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside the foreign exchange department of an Indian commercial bank in Mumbai. Bank ledgers and digital account statements record tens of billions of dollars worth of Indian Rupees accumulating in specialized corporate accounts held by Russian energy exporters. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, distinguished banking slate (#2A323D) and warm ivory cream paper (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC024.png -> Slow push-in dolly shot toward the digital bank ledger showing the soaring Rupee balance, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC025", 4.17,
        "of dollars worth of rupees parked inside Indian commercial banks.",
        "Các tài khoản Vostro đặc biệt tại các ngân hàng thương mại Ấn Độ đầy ắp tiền Rupee nhưng không thể rút ra nước ngoài.",
        "FROZEN RUPEE VOSTRO ACCOUNTS", "T2V",
        "A 2D warm cinematic editorial illustration of an official Special Rupee Vostro Account (SRVA) register inside an Indian commercial bank. Stacks of bound transaction ledgers stamped with Reserve Bank of India regulatory notices display stranded liquidity locked inside domestic accounts. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ledger paper (#FAF7EE) and rich mahogany furniture, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"FROZEN RUPEE VOSTRO ACCOUNTS\", no watermarks, 16:9",
        "@CH07_SC025.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward focus on the regulatory Vostro seal, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC026", 6.25,
        "Under Indian capital controls, those rupees could not be converted into dollars, euros, or gold.",
        "Hàng rào kiểm soát vốn của Ngân hàng Dự trữ Ấn Độ (RBI): Đồng Rupee không được phép đổi sang USD, Euro hay vàng vật chất.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration illustrating strict national capital controls. An official regulatory document from the Reserve Bank of India in Mumbai sits beneath a heavy brass seal, with red rejection lines barring the conversion of rupee deposits into United States dollars, euros, or gold bullion. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, institutional slate (#1E293B), warm cream paper (#FAF7EE), and sharp coral red regulatory stamps (#EF5350), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC026.png -> Slow macro push-in on the red rejection stamp barring foreign currency conversion, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC027", 3.75,
        "They could not even be transferred back to Moscow.",
        "Các lệnh chuyển tiền hồi hương về Moscow bị phong tỏa kỹ thuật số ngay tại biên giới ngân hàng Ấn Độ.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a computer banking terminal displaying an outbound wire transfer request to Moscow blocked by capital account restrictions, showing an error dialog reading 'FOREIGN REMITTANCE RESTRICTED UNDER CAPITAL CONTROLS'. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark terminal slate (#0F172A) and emergency amber text, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC027.png -> Macro push-in on the flashing remittance restriction alert on the computer monitor, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC028", 4.17,
        "Russia was left holding massive piles of currency that could",
        "Két sắt ngân hàng chứa đầy các cọc tiền 500 Rupee Ấn Độ, tài sản khổng lồ trên danh nghĩa nhưng bị khóa chặt trong biên giới nội địa.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside a fortified commercial bank vault in New Delhi. Stacks upon stacks of colorful 500-rupee banknotes fill heavy metal storage cages to the ceiling, representing immense nominal wealth completely immobilized within domestic borders. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, secure vault slate (#1E293B) and colorful Indian currency tones, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC028.png -> Slow tracking shot along the wire mesh cages filled with immobilized rupee banknotes, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC029", 4.58,
        "only be spent buying Indian pharmaceutical goods or domestic manufacturing machinery.",
        "Đoàn xe tải chở thuốc tân dược và máy móc nông nghiệp xuất xưởng từ Ấn Độ sang Nga, lựa chọn chi tiêu hạn hẹp duy nhất.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of export warehouses at an industrial park near Mumbai, India. Forklifts load export crates of generic pharmaceuticals and heavy agricultural tractors onto transport carriers bound for Russian markets, illustrating the narrow purchasing options for trapped rupees. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, industrial warehouse slate (#1E293B) and shipping crate wood (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC029.png -> Slow lateral tracking shot past the loaded pharmaceutical cargo containers, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC030", 3.33,
        "A currency that cannot be freely converted or",
        "Bức tranh ẩn dụ: Đồng tiền bị đóng khung sau tấm kính bảo vệ có khóa xích kim loại, không thể lưu thông tự do ra thế giới.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a currency banknote encased behind heavy reinforced glass bound by a metallic padlock, symbolizing the inability of a non-convertible currency to circulate freely across global markets. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep shadow slate (#1E293B) and brass lock reflections, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC030.png -> Slow push-in dolly shot toward the padlocked currency display, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC031", 6.25,
        "spent across global markets is not a reserve currency. It is an illiquid trade coupon.",
        "Phán quyết kinh tế học sắc bén: Một đồng tiền không thể chuyển đổi tự do không phải là tiền tệ dự trữ, nó chỉ là một 'phiếu đổi hàng kém thanh khoản'.",
        "TRADE COUPON VS RESERVE CURRENCY", "T2V",
        "A 2D warm cinematic editorial illustration contrasting a sovereign reserve currency against a trade voucher. On the left, an unconvertible national banknote is visually stamped with the degrading label 'ILLIQUID TRADE COUPON'; on the right, a global reserve asset glows with universal liquidity under clean museum lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, sophisticated dark slate background (#1E293B), warm ivory cream (#FAF7EE), and sharp amber typography, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"TRADE COUPON VS RESERVE CURRENCY\", no watermarks, 16:9",
        "@CH07_SC031.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow pan from the stamped coupon to the reserve asset, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC032", 2.08,
        "China faces a similar dilemma.",
        "Trụ sở Cục Quản lý Ngoại hối Nhà nước Trung Quốc (SAFE) tại Bắc Kinh, đối mặt thế lưỡng nan tương tự về kiểm soát vốn.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of the monumental headquarters of the State Administration of Foreign Exchange (SAFE) in Beijing, China under crisp afternoon daylight, its classical stone columns symbolizing strict state management over national capital borders. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, imposing government slate (#2A323D) and warm ivory cream stone (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC032.png -> Slow upward tilt shot up the grand neoclassical facade of the SAFE building, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC033", 6.25,
        "While Beijing promotes the internationalization of the renminbi, it refuses to liberalize its capital account.",
        "Thế khó của Bắc Kinh: Vừa muốn quốc tế hóa đồng Nhân dân tệ, vừa kiên quyết không mở cửa tài khoản vốn vì sợ bất ổn định.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration depicting China's monetary policy paradox. An illustrated scale shows the promotion of cross-border Yuan trade settlement on one side, held firmly in check by a heavy state security lock preventing open capital outflows on the other. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark institutional slate (#1E293B) and red-and-gold Chinese policy accents, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC033.png -> Slow push-in dolly shot toward the policy balance scale, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC034", 5.83,
        "Chinese leaders understand that opening their capital borders would trigger massive domestic capital flight.",
        "Phòng họp Ngân hàng Nhân dân Trung Quốc, các nhà hoạch định chính sách nhận thức rõ việc mở cửa vốn sẽ châm ngòi cho làn sóng tháo chạy vốn khổng lồ.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration inside a senior monetary policy conference room in Beijing. Chinese financial regulators sit before digital economic models forecasting severe domestic capital flight scenarios if capital borders were fully liberalized, choosing stability over global currency hegemony. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, formal executive slate (#1E293B) and warm amber chart lines, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC034.png -> Slow lateral camera track past the solemn faces of Chinese central bankers, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC035", 6.25,
        "According to SWIFT data, the renminbi's share of global payments remains hovering under five percent",
        "Dữ liệu chính thức từ SWIFT: Tỷ trọng đồng Nhân dân tệ trong thanh toán toàn cầu vẫn giậm chân tại chỗ dưới mức 5%.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an official SWIFT global payment transaction share dashboard. A modest crimson bar representing the Chinese Renminbi hovers quietly below five percent under rigorous international data auditing. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, modern dark financial slate (#1E293B) and crisp crimson data bars (#EF5350), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC035.png -> Slow push-in dolly shot toward the sub-five percent Renminbi transaction figure on the screen, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC036", 5.83,
        "while the United States dollar still anchors nearly forty-seven percent of international transaction volume.",
        "Trong khi đó, đồng USD vẫn sừng sững chiếm gần 47% tổng khối lượng giao dịch thanh toán quốc tế qua mạng SWIFT.",
        "SWIFT: USD 47% VS RMB < 5%", "T2V",
        "A 2D warm cinematic editorial illustration of a grand comparative international transaction volume display. A towering United States dollar column commands nearly forty-seven percent of total global SWIFT payment volume, dramatically overshadowing the modest sub-five percent share of the Renminbi. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark banking slate (#1E293B), dominant navy blue, and warm champagne gold highlights (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, compact subtle glowing amber gold 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading \"SWIFT: USD 47% VS RMB < 5%\", no watermarks, 16:9",
        "@CH07_SC036.png -> Steady camera shot preserving the 2D graphic novel aesthetic, clean ink outlines, and static typography text overlay exactly without any character morphing, slow downward tilt comparing the towering dollar column against the small rival bar, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC037", 2.92,
        "Evading Western sanctions has proven relatively easy.",
        "Đoàn tàu bóng ma lướt qua màn đêm, luồn lách qua các lệnh cấm vận kỹ thuật số một cách dễ dàng.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an unflagged oil tanker slipping effortlessly through an offshore archipelago at night, leaving paper sanctions orders trailing harmlessly in its wake spray. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep midnight slate (#0B0F19) and moonlit sea foam, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC037.png -> Slow tracking shot beside the tanker navigating smoothly through coastal islands, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC038", 5.83,
        "But creating a replacement for the dollar's twenty-seven-trillion-dollar liquidity ocean has proven nearly impossible.",
        "Nhưng việc tạo ra một thứ thay thế cho đại dương thanh khoản 27 nghìn tỷ USD của Trái phiếu Mỹ gần như là điều bất khả thi.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration presenting a profound visual metaphor of liquidity. A tiny, shallow puddle representing bilateral local-currency swap arrangements sits beside a colossal, fathomless deep-ocean reservoir representing the twenty-seven-trillion-dollar United States Treasury market. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, deep oceanic navy slate (#0F172A) and glowing gold liquidity depth markers (#C5A059), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC038.png -> Slow pull-back crane shot revealing the sheer, overwhelming scale of the 27-trillion-dollar liquidity ocean, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC039", 3.75,
        "The world has not found a new monetary king.",
        "Ngai vàng tiền tệ quốc tế vẫn để trống, không có đồng tiền nào đủ sức bước lên thay thế vị trí của đồng USD.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of an imposing, vacant marble throne in a grand international monetary hall, illuminated by a solitary spotlight under high neoclassical vaulted ceilings. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dignified stone slate (#1E293B) and warm ivory cream highlights (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC039.png -> Slow push-in dolly shot down the central aisle toward the empty sovereign throne, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC040", 3.75,
        "Instead, it has fractured into a high-friction economic standoff.",
        "Thế giới kinh tế phân mảnh thành các khối thương mại ma sát cao, chi phí giao dịch và rủi ro tỷ giá đội lên từng ngày.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a fractured global economic map. Deep fault lines split the continents into high-friction trading blocs separated by currency barriers, insurance surcharges, and maritime patrol perimeters under stark tension lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark fragmented slate (#1E293B) and glowing amber-red fault vectors, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC040.png -> Slow camera pan across the jagged fracture lines dividing international commerce, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC041", 4.17,
        "And this standoff is leading both Washington and its rivals",
        "Thế bế tắc địa chiến lược đẩy cả Washington và các cường quốc đối thủ tiến sát vào bờ vực của một cái bẫy lịch sử.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of two opposing diplomatic figures in sharp business silhouettes standing at the edge of a vast geopolitical chessboard, staring intently across the board under dramatic low-angle lighting. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, high-contrast silhouette slate (#0F172A) and warm amber chessboard tiles, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC041.png -> Slow tracking shot across the surface of the chessboard between the two standing figures, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    ),
    (
        "CH07_SC042", 4.17,
        "into the most dangerous geopolitical trap of the twenty-first century.",
        "Khung cảnh hoàng hôn rực lửa buông xuống trên eo biển quốc tế, dẫn nhập vào Cái Bẫy Kindleberger định mệnh của thế kỷ 21.",
        "", "T2V",
        "A 2D warm cinematic editorial illustration of a dramatic, blood-orange sunset over the industrial maritime horizon of an international strait. Dark silhouettes of battleships and tankers steam into gathering dusk, entering the most perilous geopolitical trap of modern history. Minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, fiery sunset amber (#F59E0B), deep silhouette slate (#0B0F19), and dark reflective sea, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9",
        "@CH07_SC042.png -> Slow cinematic tracking pan into the fading light of the sunset horizon, preserving all details of the reference image, 8-second continuous documentary video --ar 16:9 --dur 8s"
    )
]

# Write chapter_07_visual.md
md_lines = [
    "<!--",
    "DOCUMENT PROVENANCE & EXECUTION LINEAGE:",
    "- Output Document: episodes/the-petrodollar-paradox/chapter_07_visual.md",
    "- Activated Persona: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)",
    "- Activated Skill: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)",
    "- Source Documents Consulted:",
    "  * episodes/the-petrodollar-paradox/chapter_07.md",
    "  * episodes/the-petrodollar-paradox/scene_timing_map.json",
    "  * episodes/the-petrodollar-paradox/visual_storyboard_blueprint.md",
    "- Execution Timestamp: 2026-09-10 13:25",
    "-->",
    "",
    "# Chapter 07 Visual Script — The Shadow Fleet & The Non-Convertibility Wall",
    "",
    "Bản kịch bản phân đoạn thị giác 3 tầng giải phẫu cho Chương 7 (The Shadow Fleet & Financial Standoff), đồng bộ toán học 1-1 với 42 phân cảnh trong `scene_timing_map.json`.",
    "",
    "- **Vũ trụ Mỹ thuật:** Geopolitical Noir & Clandestine Maritime Logistics.",
    "- **Bảng màu Sâu lắng & Sang trọng:** Nocturnal Deep Navy-Slate (`#0B0F19`, `#1E293B`), Weathered Steel Rust, Warning Coral Red (`#EF5350`), Muted Champagne Gold (`#C5A059`), Warm Ivory Cream (`#FAF7EE`), Luminous High-Clarity Editorial Lighting.",
    "- **Độ chuẩn xác Địa danh & Khí tài:** Nêu đích danh địa danh thực tế (Vịnh Laconian Hy Lạp, Quần đảo Riau & Lối vào Malacca, Cảng Vadinar Gujarat Ấn Độ, Ngân hàng Dự trữ Ấn Độ RBI Mumbai, Trung tâm CIPS Thượng Hải, Trụ sở SAFE Bắc Kinh, Trung tâm Lloyd's List Intelligence London) và trang thiết bị khí tài (Radar khẩu độ tổng hợp SAR, Siêu tàu chở dầu Aframax/Suezmax 15-18 năm tuổi tắt định vị AIS, Phao cao su giảm chấn Yokohama chuyển dầu STS, Đường ống áp lực cao bơm dầu thô Urals, Tài khoản Vostro đặc biệt SRVA, Tháp chưng cất nhà máy lọc dầu Sơn Đông, Bảng thanh toán SWIFT).",
    "- **Tỷ lệ Typography:** 9/42 cảnh có chữ (21.4%), định vị góc dưới bên trái cách mép đáy 25%.",
    "- **Nhân vật & Quần chúng:** Thuyền trưởng tàu bóng ma, chuyên viên phân tích Lloyd's List, nhà giao dịch ngoại hối Mumbai, quan chức quản lý ngoại hối Trung Quốc.",
    "",
    "---",
    "",
    "| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường, Địa Danh & Khí Tài Chuẩn Xác | Text Overlay (Selective Lower-Left 25%) | Luồng Tạo Hình |",
    "| :---: | :---: | :--- | :--- | :---: | :---: |"
]

for s in scenes_data:
    sc_id, dur, spoken, summary, overlay, flow, img, vid = s
    overlay_text = f"`{overlay}`" if overlay else "`Không`"
    md_lines.append(f"| **{sc_id}** | {dur}s | {spoken} | {summary} | {overlay_text} | **{flow}** |")

with open('episodes/the-petrodollar-paradox/chapter_07_visual.md', 'w') as f:
    f.write('\n'.join(md_lines) + '\n')

print("Created chapter_07_visual.md")

# Write prompts_chapter_07.txt
txt_blocks = []
for s in scenes_data:
    sc_id, dur, spoken, summary, overlay, flow, img, vid = s
    block = f"{sc_id} [IMAGE]: {img}\n{sc_id} [VIDEO]: {vid}"
    txt_blocks.append(block)

with open('episodes/the-petrodollar-paradox/prompts_chapter_07.txt', 'w') as f:
    f.write('\n\n'.join(txt_blocks) + '\n')

print("Created prompts_chapter_07.txt")
