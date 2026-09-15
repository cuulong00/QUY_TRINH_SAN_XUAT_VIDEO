from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_prompts = ep_dir / "prompts_chapter_07.txt"
out_visual = ep_dir / "chapter_07_visual.md"

STYLE = "A 2D warm cinematic editorial illustration in high-prestige corporate and high-tech industrial noir aesthetic. High-tech ceramic charcoal tones (#181D24), dark polished cedar (#25201B), and brushed platinum titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH07_SC001
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The chairman in a dark bespoke business suit stands in a contemplative, dignified posture beside floor-to-ceiling glass windows of an executive office in Nagoya at twilight, calm and resolute against soft golden interior lamplight.",
    "Steady camera shot focusing on the chairman's composed posture, maintaining all details of the reference image exactly"
)

# CH07_SC002
add_scene(
    f"{STYLE}. An executive mahogany desk in an automotive boardroom. A sleek tablet displays international financial technology articles with critical headlines in sharp typography, illuminated by a warm brass reading lamp. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'WESTERN CRITIQUE: \"THE NOKIA OF AUTO\"'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC003
add_scene(
    f"{STYLE}. An analytical comparison chart displayed in an automotive strategy room. A stark visual graphic comparing historic telecommunications market shifts alongside modern automotive volume trends, bathed in warm amber and deep slate shadows.",
    "Slow camera push-in dolly shot toward the comparative market transition graphic on the display panel"
)

# CH07_SC004
add_scene(
    f"{STYLE}. A traditional Japanese executive conference room in Nagoya. Polished dark cedar table, minimalist shoji-inspired architectural lines, and senior automotive board members seated in quiet deliberation under soft, indirect architectural lighting.",
    "Slow tracking shot gliding along the serene conference room as senior executives deliberate with disciplined gravity"
)

# CH07_SC005
add_scene(
    f"{STYLE}. A high-angle view of a competitive automotive exhibition floor. Across the hall, colorful neon banners advertise aggressive price cuts and discount wars, while the quiet executive pavilion in the foreground remains elegant and untangled from the fray.",
    "Slow cinematic crane shot drifting across the bustling auto show floor toward the quiet executive pavilion"
)

# CH07_SC006
add_scene(
    f"{STYLE}. An advanced industrial strategy war room. A massive dark wood table covered with long-range decadal manufacturing blueprints and high-precision technical schematics illuminated by focused overhead halogen task lighting.",
    "Slow camera push-in dolly shot gliding over the unrolled decadal industrial blueprints on the dark table"
)

# CH07_SC007
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The chairman stands beside an executive presentation easel explaining a multi-pathway vehicle architecture diagram showing hybrid, electric, and hydrogen platforms in warm directional light. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'MULTI-PATHWAY DOCTRINE: HYBRIDS + EV + H2'.",
    "Steady camera shot focusing on the chairman presenting the multi-pathway strategy, maintaining all details of the reference image exactly"
)

# CH07_SC008
add_scene(
    f"{STYLE}. An immense modern automotive assembly hall in Toyota City. A disciplined production line assembling high-efficiency hybrid sedans and crossovers on automated precision carriers under warm, luminous factory bay lighting.",
    "Slow tracking shot moving parallel to the hybrid assembly line as robotic tools install precision engine components"
)

# CH07_SC009
add_scene(
    f"{STYLE}. A global maritime container terminal at sunset. Thousands of newly built hybrid vehicles parked in immaculate formation awaiting export, warm evening sunlight glinting off metallic silver and dark charcoal paintwork.",
    "Slow cinematic drone shot tracking across the vast array of hybrid vehicles awaiting global shipment"
)

# CH07_SC010
add_scene(
    f"{STYLE}. An executive treasury report on polished dark cedar. Gold-embossed financial tables display global annual operating profit surpassing thirty-four billion US dollars, illuminated by warm amber desk lamplight. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'HYBRID CASH ENGINE: $34B+ ANNUAL PROFIT'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC011
add_scene(
    f"{STYLE}. An advanced confidential battery research center in Higashi-Fuji Japan. Cleanroom engineers in white protective suits work alongside high-precision robotic micro-manipulators examining thin-film chemical layers under clean golden-white task lighting.",
    "Slow camera push-in dolly shot toward the cleanroom workstations as engineers handle delicate experimental battery layers"
)

# CH07_SC012
add_scene(
    f"{STYLE}. An industrial showroom floor displaying low-cost commercial battery cells arranged in high-volume packs, contrasting with high-precision laboratory testing equipment in the foreground.",
    "Slow tracking shot past commercial battery cell displays toward precision laboratory diagnostic equipment"
)

# CH07_SC013
add_scene(
    f"{STYLE}. An intellectual property archive room in Tokyo. Tall dark mahogany patent archive cabinets displaying rows of leather patent registry folios with gold spine lettering. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'SOLID-STATE PATENTS: >1,000 IP FILINGS (WORLD #1)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC014
add_scene(
    f"{STYLE}. A global intellectual property distribution graph on a dark glass matrix screen. A towering golden column indicates over one thousand solid-state battery patents held by the Japanese automaker, far outstripping all international rivals.",
    "Slow camera push-in dolly shot toward the glowing patent leadership column on the dark glass matrix"
)

# CH07_SC015
add_scene(
    f"{STYLE}. A ceremonial corporate signing room in Tokyo in late twenty twenty-three. Two Japanese corporate chairmen in bespoke dark suits sign a formal strategic alliance agreement on a dark polished oak table beneath warm architectural spotlighting.",
    "Slow cinematic tracking shot gliding toward the formal corporate partnership agreement resting on the polished table"
)

# CH07_SC016
add_scene(
    f"{STYLE}. A high-tech chemical pilot synthesis facility. Stainless steel reactors and specialized gloveboxes synthesizing sulfide solid-state electrolytes under pure warm lighting. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TOYOTA x IDEMITSU: 2027 SULFIDE PILOT'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC017
add_scene(
    f"{STYLE}. An electrochemical diagnostic lab. A macro view of an advanced solid-state battery cell test fixture mounted on an insulated testing platform, subtle platinum-gold status indicators glowing softly.",
    "Slow macro camera push-in toward the solid-state cell prototype resting on the precision diagnostic bench"
)

# CH07_SC018
add_scene(
    f"{STYLE}. A high-resolution physics schematic displayed on a dark glass monitor in an engineering lab. A detailed atomic diagram illustrating lithium ion migration through a solid ceramic lattice versus a liquid electrolyte path.",
    "Slow camera push-in shot toward the atomic transport schematic displayed on the dark glass monitor"
)

# CH07_SC019
add_scene(
    f"{STYLE}. A cleanroom laboratory workbench displaying an elongated Lithium Iron Phosphate Blade Battery cell. The polished metallic prism cell rests on dark matte composite under warm directional task lighting.",
    "Slow tracking shot moving along the length of the elongated prismatic battery cell on the laboratory table"
)

# CH07_SC020
add_scene(
    f"{STYLE}. An industrial battery manufacturing line in China. Automated robotic conveyors stacking thousands of blue-wrapped prismatic LFP cells in rapid rhythmic sequence under warm factory lighting.",
    "Slow lateral camera tracking shot alongside the high-speed battery cell packaging conveyor"
)

# CH07_SC021
add_scene(
    f"{STYLE}. An engineering technical diagram on a dark slate tablet. A chemical energy density curve reaching an impassable horizontal ceiling marked in deep warning red under laboratory lamps.",
    "Slow push-in dolly shot toward the energy density ceiling graph on the engineer's tablet"
)

# CH07_SC022
add_scene(
    f"{STYLE}. A comparative laboratory scale displaying an LFP battery cell alongside a digital readout showing two hundred forty watt-hours per kilogram. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'LFP DENSITY CEILING: 200 - 250 WH/KG'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC023
add_scene(
    f"{STYLE}. An electric car cruising along a scenic coastal highway at dusk, its headlights casting long warm beams along the asphalt under an amber-indigo sky.",
    "Slow tracking shot moving alongside the electric car cruising smoothly along the coastal highway"
)

# CH07_SC024
add_scene(
    f"{STYLE}. An automotive engineering service bay. A heavy industrial crane hoist slowly lowering a massive encased battery pack weighing six hundred kilograms into a vehicle chassis fixture. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading '500KM LFP PACK WEIGHT: >500 KG (HALF A TON)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC025
add_scene(
    f"{STYLE}. A forensic vehicle chassis stress test platform. Heavy mechanical actuators exerting cyclic loads on suspension springs and worn tire treads, highlighted by directional amber inspection lamps.",
    "Slow low-angle tracking shot gliding past the vehicle suspension and tire stress test rig"
)

# CH07_SC026
add_scene(
    f"{STYLE}. A pristine high-tech R&D cleanroom. A scientist in protective gloves holds a compact, ultra-dense solid-state battery cell prototype glowing with subtle platinum-gold highlights. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'SOLID-STATE TARGET: 500 WH/KG (2X DENSITY)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC027
add_scene(
    f"{STYLE}. A side-by-side engineering comparison on a dark granite inspection slab. On the left sits a bulky conventional battery block; on the right sits a slender solid-state module of half the size and double the stored energy.",
    "Slow camera pan gliding smoothly from the bulky conventional battery block across to the sleek solid-state module"
)

# CH07_SC028
add_scene(
    f"{STYLE}. A sleek prototype sedan cruising effortlessly across a vast desert highway at golden hour, sweeping past mountain silhouettes under an expansive amber sky. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'ESTIMATED RANGE: 1,000 - 1,200 KM'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC029
add_scene(
    f"{STYLE}. The digital instrument cluster of the prototype sedan glowing softly in warm amber and ivory, showing the odometer reading over one thousand kilometers on a single charge.",
    "Slow push-in shot toward the glowing digital dashboard showing extraordinary driving range"
)

# CH07_SC030
add_scene(
    f"{STYLE}. An ultra-fast high-power charging station at night. A driver plugs a sleek liquid-cooled charging connector into the vehicle charge port, a digital countdown displaying a rapid ten-minute charge. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'FAST CHARGE: 10 MINUTES (10% TO 80%)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC031
add_scene(
    f"{STYLE}. A side-by-side temporal visual comparison. On the left, a driver fueling a conventional car at a warm brass-trimmed gasoline pump; on the right, the solid-state vehicle completing its ten-minute charge in identical time.",
    "Slow steady camera pan comparing the traditional fueling time with the ultra-fast solid-state charging cycle"
)

# CH07_SC032
add_scene(
    f"{STYLE}. A specialized chemical laboratory testing bench. A technician conducts nail penetration and puncture safety tests on a solid-state cell with zero smoke, zero sparks, and absolute structural stability. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'ZERO LIQUID ELECTROLYTE: 100% NON-FLAMMABLE'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC033
add_scene(
    f"{STYLE}. An automotive safety demonstration chamber. An impact test shows the complete absence of fire or thermal runaway, providing serene consumer reassurance in warm directional lighting.",
    "Slow tracking shot moving past the intact battery test module after the severe safety test"
)

# CH07_SC034
add_scene(
    f"{STYLE}. A dramatic architectural view of an immense industrial manufacturing estate at dusk. Smoke plumes and steam rising against deep charcoal clouds, casting long shadows across sprawling steel structures.",
    "Slow camera pull-back dolly shot revealing the monumental scale of heavy industrial battery infrastructure"
)

# CH07_SC035
add_scene(
    f"{STYLE}. A vast liquid-electrolyte battery gigafactory complex in China at dusk. Miles of automated coating lines, slurry mixing towers, and chemical storage tanks under an amber-tinted industrial sky.",
    "Slow cinematic crane shot descending across the endless roofs of the liquid battery gigafactory complex"
)

# CH07_SC036
add_scene(
    f"{STYLE}. Inside a colossal battery cell production hall. Hundreds of industrial operators in protective suits maintaining wet-chemical coating machines and calendering rollers in disciplined rows under bright factory lamps.",
    "Slow tracking shot gliding down the central walkway of the vast wet-cell battery production floor"
)

# CH07_SC037
add_scene(
    f"{STYLE}. An industrial economics boardroom. An audit binder highlights capital expenditure line items with red depreciation brackets, showing older gigafactory machinery facing premature technological obsolescence. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'EARLY CAPITAL RISK: STRANDED GIGAFACTORIES'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC038
add_scene(
    f"{STYLE}. An automotive engineering prototyping facility. Senior metallurgical engineers and chemists examining microscopic sulfide electrolyte cross-sections on a high-powered electron microscope screen.",
    "Slow camera push-in dolly shot toward the microstructural electron microscope display in the lab"
)

# CH07_SC039
add_scene(
    f"{STYLE}. An exclusive luxury automotive studio in Nagoya. A bespoke concept Lexus grand tourer in dark platinum finish resting under warm studio spotlights, embodying high-end solid-state commercialization. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading '2027 DEBUT: LUXURY LEXUS PILOT ONLY'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC040
add_scene(
    f"{STYLE}. A long-range industrial timeline engraved on a dark slate wall. Milestones highlight initial luxury introduction in twenty twenty-seven and broader mass-market deployment by twenty thirty. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'MASS AFFORDABLE SCALE: 2030 HORIZON'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH07_SC041
add_scene(
    f"{STYLE}. A dynamic battery development laboratory in Shenzhen. Chinese chemical researchers testing manganese-doped lithium cells and liquid-cooled ultra-fast charging packs on active test benches under bright task lights.",
    "Slow lateral camera tracking shot across the active battery testing benches in the Shenzhen laboratory"
)

# CH07_SC042
add_scene(
    f"{STYLE}. An executive corner study overlooking a calm Japanese stone garden in autumn. Warm cedar finishes, a quiet tea setting, and an open corporate strategy manuscript resting on a low wooden table.",
    "Slow camera push-in dolly shot toward the open strategy manuscript resting beside the peaceful garden view"
)

# CH07_SC043
add_scene(
    f"{STYLE}. An automotive corporate finance ledger on dark polished oak. A healthy liquid balance sheet with low debt ratios and strong cash reserves highlighted under the warm glow of an executive desk lamp.",
    "Slow tracking shot across the pristine financial balance sheet displaying prudent cash management"
)

# CH07_SC044
add_scene(
    f"{STYLE}. An aerial perspective of an extensive commercial charging highway plaza at night. Multiple brands of charging pylons installed by competitors, bathed in ambient neon, while traffic flows smoothly past.",
    "Slow cinematic crane shot descending over the commercial highway charging infrastructure"
)

# CH07_SC045
add_scene(
    f"{STYLE}. A vast global dealership network map illuminated on a boardroom wall. Thousands of glowing nodes across North America, Southeast Asia, Europe, and Latin America connecting back to an integrated supply chain.",
    "Slow camera push-in dolly shot toward the glowing global dealership network map"
)

# CH07_SC046
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The chairman in a tailored dark suit stands calmly beside a concept vehicle chassis in an advanced design center, looking forward with patient strategic foresight in warm directional lighting.",
    "Steady camera shot focusing on the chairman's composed posture, maintaining all details of the reference image exactly"
)

# CH07_SC047
add_scene(
    f"{STYLE}. An executive boardroom overlooking the Tokyo skyline at dusk. A senior strategy executive looks toward the horizon where golden sunset transitions into deep indigo, symbolizing the long-term decadal contest.",
    "Slow tracking shot moving past the boardroom table toward the panoramic dusk skyline of Tokyo"
)

# CH07_SC048
add_scene(
    f"{STYLE}. A dramatic global geopolitical map etched on dark glass. Golden and crimson maritime trade routes spanning the Pacific and Atlantic, crisscrossed by symbolic tariff barriers and regulatory frontiers.",
    "Slow camera push-in dolly shot gliding over the illuminated geopolitical shipping routes on the glass map"
)

# CH07_SC049
add_scene(
    f"{STYLE}. A monumental corporate boardroom at night overlooking a sprawling metropolis. In the center of the dark walnut table sits a glowing four-trillion-dollar economic balance marker under warm directional spotlighting.",
    "Slow cinematic crane shot descending toward the central economic ledger on the dark walnut table"
)

# CH07_SC050
add_scene(
    f"{STYLE}. A powerful geopolitical visual metaphor: a world map bifurcating into two distinct economic hemispheres, one anchored by Western tariff protectionism and Japanese hybrid-solid state technology, the other by Global South supply chains. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'THE BIFURCATION: A FRACTURED GLOBAL ORDER'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# Write prompts file
out_prompts.write_text("\n\n".join(prompts) + "\n", encoding="utf-8")
print(f"Generated {len(prompts)} scenes in {out_prompts.name}")

# Now generate chapter_07_visual.md
with open(ep_dir / "scene_timing_map.json") as f:
    timing_data = json.load(f)

ch07_scenes = [s for s in timing_data if s.get("chapter") == "07"]

visual_header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_07_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_07.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_07.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-13 18:45
-->

# Chapter 07 Visual Script — The Solid-State Counter-Strike

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 7 (The Solid-State Counter-Strike: Toyota's Cash Mountain and the Ultimate Tech Pivot), đồng bộ toán học 1-1 với 50 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_07.txt`.

- **Vũ trụ Mỹ thuật:** High-Tech Battery Science & Patient Japanese Counter-Strategy.
- **Bảng màu Sâu lắng & Sang trọng:** High-Tech Ceramic Charcoal (`#181D24`), Dark Polished Cedar (`#25201B`), Sulfide White-Grey (`#E2E8F0`), Brilliant Platinum Gold (`#E6C687` / `#D4AF37`), Electric Amber (`#F59E0B`), Deep Warning Red (`#B71C1C`), Warm Ivory Cream (`#FAF7EE`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Directional Warm Tungsten Rim Lights, Precision Cleanroom Directional Illumination, Velvety Deep Shadows, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~25-30% cảnh mấu chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :--- :---: | :---: |
"""

text_overlays_ch07 = {
    "CH07_SC002": "WESTERN CRITIQUE: \"THE NOKIA OF AUTO\"",
    "CH07_SC007": "MULTI-PATHWAY DOCTRINE: HYBRIDS + EV + H2",
    "CH07_SC010": "HYBRID CASH ENGINE: $34B+ ANNUAL PROFIT",
    "CH07_SC013": "SOLID-STATE PATENTS: >1,000 IP FILINGS (WORLD #1)",
    "CH07_SC016": "TOYOTA x IDEMITSU: 2027 SULFIDE PILOT",
    "CH07_SC022": "LFP DENSITY CEILING: 200 - 250 WH/KG",
    "CH07_SC024": "500KM LFP PACK WEIGHT: >500 KG (HALF A TON)",
    "CH07_SC026": "SOLID-STATE TARGET: 500 WH/KG (2X DENSITY)",
    "CH07_SC028": "ESTIMATED RANGE: 1,000 - 1,200 KM",
    "CH07_SC030": "FAST CHARGE: 10 MINUTES (10% TO 80%)",
    "CH07_SC032": "ZERO LIQUID ELECTROLYTE: 100% NON-FLAMMABLE",
    "CH07_SC037": "EARLY CAPITAL RISK: STRANDED GIGAFACTORIES",
    "CH07_SC039": "2027 DEBUT: LUXURY LEXUS PILOT ONLY",
    "CH07_SC040": "MASS AFFORDABLE SCALE: 2030 HORIZON",
    "CH07_SC050": "THE BIFURCATION: A FRACTURED GLOBAL ORDER"
}

visual_descs_ch07 = {
    "CH07_SC001": "Chủ tịch Akio Toyoda trong bộ vest may đo cao cấp đứng đĩnh đạc bên cửa sổ kính tầng cao tại Nagoya lúc chạng vạng, ánh nhìn điềm tĩnh kiên định.",
    "CH07_SC002": "Chiếc máy tính bảng trên bàn làm việc mahogany hiển thị các bài báo công nghệ phương Tây với tiêu đề chỉ trích gay gắt dưới ánh đèn bàn đồng.",
    "CH07_SC003": "Biểu đồ phân tích thị trường trong phòng chiến lược so sánh sự sụp đổ lịch sử của Nokia với sự dịch chuyển công nghiệp ô tô hiện đại.",
    "CH07_SC004": "Phòng họp hội đồng quản trị truyền thống Nhật Bản tại Nagoya, các lãnh đạo cấp cao trầm ngâm thảo luận với kỷ luật và bản lĩnh thép.",
    "CH07_SC005": "Góc nhìn từ trên cao xuống sàn triển lãm ô tô náo nhiệt đầy khẩu hiệu giảm giá sốc, đối lập với gian phòng điều hành tĩnh lặng của Toyota.",
    "CH07_SC006": "Bàn làm việc phòng tác chiến chiến lược trải các bản vẽ thiết kế công nghiệp dài hạn cho cả thập kỷ tới dưới ánh đèn halogen hội tụ.",
    "CH07_SC007": "Chủ tịch Akio Toyoda đứng cạnh giá thuyết trình phân tích sơ đồ kiến trúc đa lộ trình (Multi-Pathway) kết hợp hybrid, EV và hydrogen.",
    "CH07_SC008": "Dây chuyền lắp ráp tự động tại Thành phố Toyota, robot lắp đặt các cụm động cơ hybrid độ chính xác cực cao dưới ánh đèn xưởng ấm áp.",
    "CH07_SC009": "Cảng xuất khẩu quốc tế lúc hoàng hôn, hàng ngàn chiếc xe hybrid mới tinh xếp hàng ngay ngắn chuẩn bị lên tàu viễn dương đi khắp thế giới.",
    "CH07_SC010": "Báo cáo tài chính trên bàn gỗ tuyết tùng tối màu, hiển thị lợi nhuận hoạt động kỷ lục vượt mốc 34 tỷ USD từ cỗ máy xe hybrid toàn cầu.",
    "CH07_SC011": "Trung tâm R&D bảo mật cao tại Higashi-Fuji Nhật Bản, các kỹ sư mặc đồ phòng sạch sử dụng cánh tay robot thao tác với các lớp màng pin mỏng.",
    "CH07_SC012": "Sàn trưng bày pin công nghiệp giá rẻ thương mại số lượng lớn, đối lập với thiết bị đo kiểm độ chính xác cao trong phòng thí nghiệm tiền cảnh.",
    "CH07_SC013": "Phòng lưu trữ hồ sơ sở hữu trí tuệ tại Tokyo, các tủ gỗ mahogany lưu giữ các tập văn bằng sáng chế pin thể rắn đóng gáy vàng trang trọng.",
    "CH07_SC014": "Đồ thị phân bổ sáng chế toàn cầu trên màn hình kính tối màu: Cột sáng vàng của Toyota vượt mốc 1.000 bằng sáng chế pin thể rắn, đứng số 1 thế giới.",
    "CH07_SC015": "Lễ ký kết liên minh chiến lược tại Tokyo cuối năm 2023, hai nhà lãnh đạo tập đoàn ký kết biên bản hợp tác thương mại hóa pin thể rắn.",
    "CH07_SC016": "Nhà máy thí nghiệm hóa chất công nghệ cao với lò phản ứng thép không gỉ, tổng hợp chất điện phân rắn gốc sulfide dưới ánh sáng vàng ấm.",
    "CH07_SC017": "Cận cảnh mô-đun pin thể rắn mẫu thử nghiệm gắn trên bàn đo kiểm điện hóa, các đèn chỉ báo trạng thái màu bạch kim phát sáng tinh xảo.",
    "CH07_SC018": "Sơ đồ vật lý lượng tử trên màn hình kính đen, mô phỏng quá trình ion lithium di chuyển qua mạng tinh thể gốm rắn thay vì chất lỏng truyền thống.",
    "CH07_SC019": "Bàn thao tác phòng lab đặt thanh pin Blade LFP dạng lăng trụ dài bọc kim loại sáng loáng dưới ánh đèn bàn kỹ thuật ấm áp.",
    "CH07_SC020": "Dây chuyền sản xuất pin khổng lồ tại Trung Quốc, các cánh tay robot xếp hàng ngàn cell pin LFP lăng trụ vào khay với tốc độ chóng mặt.",
    "CH07_SC021": "Đồ thị kỹ thuật trên máy tính bảng hiển thị đường cong mật độ năng lượng pin LFP chạm vào trần giới hạn vật lý màu đỏ cảnh báo.",
    "CH07_SC022": "Cân đo đạc phòng lab so sánh cell pin LFP với màn hình kỹ thuật số hiển thị mật độ năng lượng đạt trần ở mức 240 Wh/kg.",
    "CH07_SC023": "Chiếc xe điện lướt êm ái trên đường cao tốc ven biển lúc hoàng hôn, ánh đèn pha rọi dài trên mặt đường nhựa dưới bầu trời tím hổ phách.",
    "CH07_SC024": "Cẩu trục cơ khí trong xưởng dịch vụ từ từ hạ khối pin LFP khổng lồ nặng hơn nửa tấn (600 kg) lắp vào khung gầm xe điện.",
    "CH07_SC025": "Bàn thử nghiệm độ bền khung gầm và hệ thống treo xe hơi, các kích thủy lực tạo tải trọng kiểm tra sự hao mòn lốp và giảm xóc do pin quá nặng.",
    "CH07_SC026": "Nhà khoa học trong phòng sạch đeo găng tay nâng niu mẫu pin thể rắn nhỏ gọn, phát sáng ánh bạch kim với mật độ năng lượng kỷ lục 500 Wh/kg.",
    "CH07_SC027": "Bố cục đối chiếu: bên trái là khối pin lỏng cồng kềnh nặng nề, bên phải là mô-đun pin thể rắn kích thước chỉ bằng một nửa nhưng năng lượng gấp đôi.",
    "CH07_SC028": "Chiếc sedan nguyên mẫu lướt nhẹ băng qua đường cao tốc bán sa mạc lúc hoàng hôn, cự ly hoạt động thực tế đạt 1.000 đến 1.200 km chỉ sau một lần sạc.",
    "CH07_SC029": "Đồng hồ kỹ thuật số trên bảng điều khiển xe phát sáng êm dịu, kim đồng hồ báo quãng đường đã đi vượt 1.000 km mà vẫn còn điện.",
    "CH07_SC030": "Trạm sạc siêu nhanh ban đêm, người lái cắm đầu sạc làm mát bằng chất lỏng vào xe, màn hình kỹ thuật số đếm ngược thời gian sạc đầy 10 phút.",
    "CH07_SC031": "Bố cục đối chiếu thời gian thực: thời gian sạc 10 phút của pin thể rắn tương đương chính xác thời gian đổ đầy một bình xăng truyền thống.",
    "CH07_SC032": "Bàn thử nghiệm an toàn cơ điện: thanh đinh thép đâm xuyên qua cell pin thể rắn mà không hề bốc khói, không tia lửa, hoàn toàn chống cháy nổ.",
    "CH07_SC033": "Buồng thử nghiệm an toàn va chạm ô tô, mô-đun pin vẫn nguyên vẹn sau thử nghiệm khắc nghiệt, xóa tan nỗi sợ hãi cháy nổ của người mua xe.",
    "CH07_SC034": "Góc nhìn flycam trên cao khu phức hợp công nghiệp sản xuất pin lúc chập tối, hơi nước bốc lên từ các tháp làm mát dưới bầu trời mây xám.",
    "CH07_SC035": "Tổ hợp siêu nhà máy gigafactory sản xuất pin lỏng rộng lớn tại Trung Quốc, các dây chuyền trộn hóa chất và phủ cực trải dài ngút tầm mắt.",
    "CH07_SC036": "Hàng trăm công nhân mặc đồ bảo hộ vận hành các máy cán ép và dây chuyền phủ hóa chất lỏng trong xưởng sản xuất pin ướt khổng lồ.",
    "CH07_SC037": "Hồ sơ kiểm toán tài chính công nghiệp làm nổi bật các khoản chi phí vốn khổng lồ có nguy cơ trở thành tài sản mắc kẹt khi công nghệ đổi dòng.",
    "CH07_SC038": "Kỹ sư luyện kim và chuyên gia hóa học soi kính hiển vi điện tử quét kiểm tra cấu trúc vi mô của lớp điện phân rắn gốc sulfide trong phòng lab.",
    "CH07_SC039": "Studio xe sang tại Nagoya, chiếc xe Lexus phong cách grand tourer màu bạch kim tối đỗ dưới ánh đèn spotlight, đại diện cho giai đoạn ra mắt 2027.",
    "CH07_SC040": "Dòng thời gian công nghiệp khắc trên tường đá phiến: cột mốc xe sang Lexus thử nghiệm năm 2027 và thương mại hóa đại trà hướng tới 2030.",
    "CH07_SC041": "Phòng lab pin năng động tại Thâm Quyến, các nhà nghiên cứu thử nghiệm công nghệ sạc siêu nhanh 5C và pin cải tiến mangan để phòng thủ thị trường.",
    "CH07_SC042": "Góc phòng làm việc thanh tịnh nhìn ra vườn đá Nhật Bản mùa thu, tách trà ấm và tập bản thảo chiến lược doanh nghiệp trên bàn gỗ tuyết tùng.",
    "CH07_SC043": "Bảng cân đối kế toán tài chính vững chắc, tỷ lệ đòn bẩy nợ thấp và lượng tiền mặt dồi dào dưới ánh sáng đèn bàn lãnh đạo ấm áp.",
    "CH07_SC044": "Góc nhìn flycam trạm sạc cao tốc ban đêm, hạ tầng trạm sạc do các đối thủ bỏ vốn đầu tư tốn kém đang phục vụ dòng xe lưu thông.",
    "CH07_SC045": "Bản đồ mạng lưới đại lý toàn cầu rực sáng hàng ngàn điểm kết nối khắp Bắc Mỹ, Đông Nam Á, Châu Âu và Mỹ Latinh trên tường phòng họp.",
    "CH07_SC046": "Chủ tịch Akio Toyoda đứng đĩnh đạc bên khung gầm xe ý tưởng tại trung tâm thiết kế tiên tiến, ánh mắt nhìn về phía trước với tầm nhìn chiến lược.",
    "CH07_SC047": "Phòng họp điều hành nhìn ra đường chân trời Tokyo lúc hoàng hôn chuyển dần sang màu chàm, biểu tượng cho cuộc đua marathon của thập kỷ tới.",
    "CH07_SC048": "Bản đồ địa chính trị toàn cầu khắc trên kính tối màu, các tuyến thương mại hàng hải Thái Bình Dương và Đại Tây Dương đan xen các rào cản thuế quan.",
    "CH07_SC049": "Bàn họp phòng khánh tiết hội đồng quản trị ban đêm, ở giữa bàn là chiếc sổ cái kinh tế biểu trưng cho cuộc tranh đoạt trị giá 4 nghìn tỷ USD.",
    "CH07_SC050": "Bản đồ thế giới phân cực thành hai bán cầu kinh tế: một bên là bảo hộ thuế quan phương Tây và công nghệ Nhật Bản, một bên là chuỗi cung ứng phương Nam."
}

rows_ch07 = []
for s in ch07_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descs_ch07.get(sid, "Bối cảnh công nghiệp thực tế đời thường.")
    overlay = text_overlays_ch07.get(sid, "Không")
    stream = "I2V" if (sid in ["CH07_SC001", "CH07_SC007", "CH07_SC046"]) else "T2V"
    rows_ch07.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

visual_content = visual_header + "\n".join(rows_ch07) + "\n"
out_visual.write_text(visual_content, encoding="utf-8")
print(f"Generated {len(rows_ch07)} table rows in {out_visual.name}")
