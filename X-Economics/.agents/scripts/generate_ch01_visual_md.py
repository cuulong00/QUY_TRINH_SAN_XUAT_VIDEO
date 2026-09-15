from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
scene_file = ep_dir / "scene_timing_map.json"
out_file = ep_dir / "chapter_01_visual.md"

with open(scene_file, "r", encoding="utf-8") as f:
    scenes = json.load(f)

ch01_scenes = [s for s in scenes if s.get("chapter") == "01"]

header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_01_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_01.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_01.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-12 22:33
-->

# Chapter 01 Visual Script — The Trap at the Border

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 1 (The Hook & Grand Scale Introduction), đồng bộ toán học 1-1 với 54 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_01.txt`.

- **Vũ trụ Mỹ thuật:** The Geoeconomic Chessboard & Industrial Noir Luxury.
- **Bảng màu Sâu lắng & Sang trọng:** Deep Warm Walnut (`#1C1917`), Dark Mahogany Slate (`#231C18`), Deep Polished Slate (`#1E242B`), Brushed Titanium, Imperial Warm Champagne Gold (`#D4AF37`), Luminous Amber (`#F59E0B`), Deep Crimson Bordeaux (`#8B0000`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Directional Warm Tungsten Rim Lights, Velvety Deep Shadows, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~20% cảnh mấu chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :---: | :---: |
"""

# Text overlays for specific scenes
text_overlays = {
    "CH01_SC001": "GLOBAL AUTO SECTOR: $4 TRILLION",
    "CH01_SC002": "14,000,000+ WORKERS",
    "CH01_SC027": "SECTION 301 TARIFF: 100%",
    "CH01_SC028": "INFLATION REDUCTION ACT",
    "CH01_SC030": "SOFTWARE BAN: 2027 | HARDWARE: 2030",
    "CH01_SC036": "US AVERAGE TRANSACTION PRICE: $48,000",
    "CH01_SC039": "US MARKET: 15-16M CARS/YEAR",
    "CH01_SC040": "GLOBAL PRODUCTION: ~90M CARS",
    "CH01_SC041": "US MARKET: 18% | GLOBAL SOUTH: 82%",
    "CH01_SC042": "CHINA DOMESTIC: 30M+ CARS/YEAR",
    "CH01_SC044": "THE 82% WORLD: 74M+ VEHICLES",
}

# Physical descriptions in Vietnamese
visual_descriptions = {
    "CH01_SC001": "Phòng họp hội đồng quản trị nhìn ra đại đô thị rực sáng lúc hoàng hôn. Sổ cái kinh tế da thuộc đặt trên giá đồng thau sang trọng.",
    "CH01_SC002": "Xưởng dập vỏ xe hiện đại giờ đổi ca. Hàng trăm kỹ sư mặc đồng phục xanh sẫm và mũ bảo hộ bước đi nghiêm cẩn giữa hàng dập robot khổng lồ.",
    "CH01_SC003": "Bức tường phòng họp tập đoàn xe Mỹ treo các bức ảnh chân dung tài phiệt công nghiệp thế kỷ 20 trong khung gỗ mahogany cổ kính.",
    "CH01_SC004": "Chuyên gia kinh tế vĩ mô lật giở bản đồ chuỗi cung ứng in trên giấy dày trong thư phòng gỗ ấm, chạm ngón tay vào điểm gãy màu đỏ bordeaux.",
    "CH01_SC005": "Nhà máy gạch đỏ lịch sử của Volkswagen tại Wolfsburg dưới trời chiều muộn, công nhân Đức mặc áo khoác dạ đứng bàn tán trầm ngâm ngoài cổng sắt.",
    "CH01_SC006": "Văn phòng lãnh đạo nhìn ra sông Detroit, cuốn sổ cái kiểm toán mở trên bàn làm việc hiển thị các khoản lỗ đậm màu mực đỏ bầm.",
    "CH01_SC007": "Phòng họp báo Tokyo, hai lãnh đạo cấp cao Nissan và Honda mặc vest tối màu cúi chào trang trọng trước ánh đèn flash của phóng viên.",
    "CH01_SC008": "Chủ tịch Akio Toyoda ngồi điềm tĩnh ở đầu bàn họp gỗ sồi lớn tại Nagoya, toát lên uy quyền của một cựu vương công nghiệp trước biến động.",
    "CH01_SC009": "Trung tâm điều hành tối tân tại Thâm Quyến, các kỹ sư quan sát màn hình cong hiển thị tuyến vận tải biển và chỉ số sản xuất pin.",
    "CH01_SC010": "Bản đồ phối cảnh kiến trúc khắc họa Bắc Mỹ như một pháo đài tường thành khép kín, các tuyến thương mại màu hổ phách rẽ nhánh xuống Nam bán cầu.",
    "CH01_SC011": "Mũi siêu tàu chở ô tô BYD Explorer No. 1 rẽ sóng đại dương lúc hoàng hôn, hàng ngàn chiếc xe xếp ngay ngắn trên các tầng boong mở rực sáng.",
    "CH01_SC012": "Cổng vào khu công nghiệp Camaçari tại Bahia Brazil được khoác áo mới hiện đại, nắng chiều nhiệt đới rọi bóng dài qua cổng gác kính thép.",
    "CH01_SC013": "Mô hình cắt bổ động cơ siêu lai DM-i trên bàn thử nghiệm phòng lab slate tối, khối pin Blade và lõi đồng phát sáng ánh vàng hổ phách tinh xảo.",
    "CH01_SC014": "Quả địa cầu kinh tế chế tác từ gỗ óc chó và đồng thau, 82% diện tích địa cầu bên ngoài Bắc Mỹ rực sáng mạng lưới hành lang logistics màu vàng.",
    "CH01_SC015": "Cảnh phân đôi ấn tượng: Nửa trái là mặt ca-lăng Hilux cơ khí cổ điển; nửa phải là dải đèn LED xe Shark siêu lai, đối đầu nghẹt thở trong studio tối.",
    "CH01_SC016": "Khán phòng họp báo quốc tế chật kín phóng viên tài chính giơ micro ghi âm dưới ánh đèn rọi sân khấu ấm áp.",
    "CH01_SC017": "Cận cảnh đầu micro truyền hình đặt trên bục gỗ sẫm màu, phía sau là bóng các nhà báo quốc tế đang chăm chú lắng nghe.",
    "CH01_SC018": "Bục phát biểu trang trọng gắn biển tên chức vụ bằng đồng thau và gỗ óc chó, màn hình phía sau phát tỏa ánh sáng hổ phách êm dịu.",
    "CH01_SC019": "Phó Chủ tịch Stella Li mỉm cười điềm tĩnh, tự tin trước micro báo giới quốc tế, toát lên phong thái ngoại giao kinh tế sắc sảo.",
    "CH01_SC020": "Bà Stella Li phát biểu với phong thái đĩnh đạc, cử chỉ tay dứt khoát trên nền gỗ óc chó tối và ánh sáng viền vàng ấm.",
    "CH01_SC021": "Toàn cảnh góc rộng khán phòng từ phía sau, vị nữ lãnh đạo đứng trên bục sáng rực trước hàng chục phóng viên quốc tế.",
    "CH01_SC022": "Màn hình số trên sân khấu hiển thị bản đồ nhu cầu xe toàn cầu, nổi bật các thị trường Nam Mỹ, Đông Nam Á và châu Âu rực rỡ sắc vàng kim.",
    "CH01_SC023": "Sàn giao dịch Phố Wall nhộn nhịp, các chuyên viên tài chính đứng quanh màn hình Bloomberg với nét mặt trầm ngâm, lo âu.",
    "CH01_SC024": "Đại lý ô tô ven đường Route 66 nước Mỹ những năm 1960 dưới ánh đèn neon vàng ấm hoài niệm phản chiếu trên mặt đường nhựa.",
    "CH01_SC025": "Gia đình người Mỹ thập niên 1980 hào hứng xem một chiếc sedan Nhật Bản bền bỉ bên ngoài showroom kính trong nắng chiều.",
    "CH01_SC026": "Mặt tiền đá cẩm thạch và mái vòm Điện Capitol tại Washington DC rực sáng dưới ánh nắng chiều tà tương phản với mây giông xám.",
    "CH01_SC027": "Văn bản sắc lệnh thuế quan Mục 301 đặt trên bàn làm việc Quốc hội dưới ánh đèn bàn đồng, con dấu sáp màu đỏ bordeaux nổi bật.",
    "CH01_SC028": "Tập luật Đạo luật Giảm lạm phát (IRA) đóng bìa da sang trọng với quốc huy dập nổi đặt trên bàn thư viện gỗ óc chó.",
    "CH01_SC029": "Lối vào tòa nhà Bộ Thương mại Mỹ tại Washington DC, biển đồng uy nghiêm sáng bóng dưới đèn hắt kiến trúc ấm áp.",
    "CH01_SC030": "Cận cảnh kiểm tra vi mạch điều khiển viễn thông trên xe hơi, tia laser chẩn đoán quét qua chip và đường mạch vi điện tử.",
    "CH01_SC031": "Trạm kiểm soát cửa khẩu thương mại biên giới Mỹ - Mexico rực sáng đèn cao áp ban đêm, xe container nối đuôi qua cổng quét an ninh.",
    "CH01_SC032": "Dàn xe vận chuyển ô tô chuyên dụng đỗ ngay ngắn tại bãi tập kết đường sắt biên giới, ánh đèn an ninh rọi bóng dài trên kim loại xe.",
    "CH01_SC033": "Phòng điều trần ủy ban Quốc hội Mỹ, các nghị sĩ ngồi sau dãy bàn gỗ cong nâng cao đang xem hồ sơ với vẻ mặt nghiêm nghị.",
    "CH01_SC034": "Khách hàng Mỹ đứng bên bàn tư vấn đại lý ô tô, xem xét kỹ lưỡng bản ước tính chi phí trả góp hàng tháng với vẻ mặt đăm chiêu.",
    "CH01_SC035": "Hàng xe bán tải khổng lồ và SUV đắt tiền xếp san sát nhau trên bãi đại lý ngoại ô, lưới tản nhiệt mạ crôm đồ sộ lóa nắng chiều.",
    "CH01_SC036": "Tem giá dán trên cửa sổ chiếc SUV cỡ lớn tại đại lý, phản chiếu không gian showroom sang trọng qua lớp kính xe.",
    "CH01_SC037": "Chiếc xe hơi đơn độc chạy trên cao tốc Mỹ lúc chập tối, hai bên là hàng rào tường chắn âm bê tông cao vút cô lập với thế giới.",
    "CH01_SC038": "Hai chuyên gia chiến lược cấp cao tại phòng tác chiến Thâm Quyến đứng trước bàn vẽ kính phát sáng, phân tích công thức thị phần toàn cầu.",
    "CH01_SC039": "Góc nhìn từ trên cao xuống bãi tập kết xe hơi khổng lồ tại Mỹ, hàng ngàn chiếc xe xếp thành lưới hình học phẳng phiu trong sương sớm.",
    "CH01_SC040": "Cảng biển nước sâu quốc tế nhộn nhịp, cần cẩu bốc dỡ hàng trăm container ô tô lên tàu viễn dương dưới ánh đèn vàng ấm áp.",
    "CH01_SC041": "Biểu đồ phân bổ hình tròn khắc chìm bằng vàng trên tường đá phiến phòng họp, thể hiện tỷ lệ 18% nước Mỹ và 82% thế giới đang phát triển.",
    "CH01_SC042": "Trung tâm giao xe quy mô lớn tại Thượng Hải, các gia đình vui mừng nhận chìa khóa xe điện thông minh mới trong không gian ấm cúng.",
    "CH01_SC043": "Biểu đồ so sánh sản lượng cột đôi trên màn hình titan: Cột vàng 30 triệu xe Trung Quốc sừng sững bên cạnh cột xám 16 triệu xe Mỹ.",
    "CH01_SC044": "Bức tranh toàn cảnh đô thị ven biển Nam Mỹ lúc hoàng hôn, các tuyến cầu cạn cao tốc uốn lượn với dòng xe cộ tấp nập trong nắng vàng.",
    "CH01_SC045": "Góc phố sầm uất tại Bangkok với đường tàu điện trên cao và dòng xe hơi, xe máy nhộn nhịp dưới ánh đèn đường và biển hiệu lung linh.",
    "CH01_SC046": "Dòng người đi làm và gia đình trung lưu chờ đợi tại trạm trung chuyển giao thông hiện đại ở Đông Nam Á, nét mặt tập trung, cần mẫn.",
    "CH01_SC047": "Chiếc xe bán tải cơ bắp Mỹ đỗ lừng lững trước hiên nhà ngoại ô nhỏ hẹp, tem giá đại lý đắt đỏ lấp lánh dưới nắng trưa.",
    "CH01_SC048": "Chiếc xe hatchback hybrid 5 cửa hiện đại, nhỏ gọn đỗ trước quán cafe khu phố nắng ấm, đôi vợ chồng trẻ dỡ đồ đạc dễ dàng.",
    "CH01_SC049": "Bến bãi đường sắt liên vận quốc tế, cẩu giàn cẩu thùng hàng mang logo hãng xe đặt lên toa tàu hàng chuẩn bị xuất phát xuyên lục địa.",
    "CH01_SC050": "Bản đồ thế giới bằng gỗ óc chó trên tường phòng họp, các đường cáp quang màu vàng rực rỡ tỏa đi từ Thâm Quyến đến Nam Mỹ và châu Âu.",
    "CH01_SC051": "Bức tường chắn thuế quan bê tông sừng sững giữa sa mạc lúc hoàng hôn, phủ bóng đen dài qua dải đường cao tốc hoang vắng.",
    "CH01_SC052": "Trụ sở Ủy ban Châu Âu Berlaymont tại Brussels dưới cơn mưa mùa thu, ánh đèn vàng từ các văn phòng phản chiếu lung linh trên sân đá ướt.",
    "CH01_SC053": "Cuộc họp khẩn cấp của các lãnh đạo tập đoàn công nghiệp Đức, vẻ mặt căng thẳng bên cạnh các tập báo cáo khủng hoảng tài chính dày cộp.",
    "CH01_SC054": "Toàn cảnh tổ hợp nhà máy khổng lồ của Volkswagen tại Wolfsburg trong sương mù chiều muộn, ống khói gạch đỏ và logo VW phát sáng mờ ảo."
}

rows = []
for s in ch01_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descriptions.get(sid, "Bối cảnh vật lý công nghiệp thực tế đời thường.")
    overlay = text_overlays.get(sid, "Không")
    stream = "I2V" if (sid in ["CH01_SC008", "CH01_SC019", "CH01_SC020"]) else "T2V"
    
    rows.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

full_content = header + "\n".join(rows) + "\n"
out_file.write_text(full_content, encoding="utf-8")
print(f"Generated {len(rows)} table rows in {out_file.name}")
