from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_prompts = ep_dir / "prompts_chapter_04.txt"
out_visual = ep_dir / "chapter_04_visual.md"

STYLE = "A 2D warm cinematic editorial illustration in high-prestige industrial precision aesthetic. Cleanroom charcoal tones (#20242C), polished dark slate (#1A202C), and brushed titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH04_SC001
add_scene(
    f"{STYLE}. The sleek glass-and-granite entrance of an international investment bank research headquarters in Zurich Switzerland on a crisp autumn morning. Senior Swiss financial analysts in dark tailored overcoats carrying briefcases enter the modern security turnstiles under warm architectural downlights.",
    "Slow tracking shot gliding toward the glass revolving doors of the Zurich financial research facility in early morning light"
)

# CH04_SC002
add_scene(
    f"{STYLE}. Inside a state-of-the-art engineering teardown hangar in Switzerland. A brand-new metallic grey electric sedan rests on an illuminated hydraulic inspection lift, surrounded by laser measuring rigs and diagnostic workstations in clean polished surroundings.",
    "Slow circular camera orbital shot around the lifted electric sedan, warm directional inspection lights reflecting off pristine metallic paint"
)

# CH04_SC003
add_scene(
    f"{STYLE}. Senior automotive teardown engineers in clean white lab coats and nitrile gloves systematically disassembling the electric vehicle. Pneumatic wrenches loosening chassis bolts, wiring harnesses labeled on organizing tables, and lithium battery cells laid out on protective foam trays.",
    "Slow tracking shot moving along the component sorting benches as engineers catalog disassembled parts with clinical precision"
)

# CH04_SC004
add_scene(
    f"{STYLE}. A thick, spiral-bound technical teardown report resting on an executive mahogany boardroom table in Frankfurt. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'UBS EVIDENCE LAB: BYD SEAL TEARDOWN'. Warm tungsten reading lamp casts a rich golden cone over the document.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC005
add_scene(
    f"{STYLE}. Close-up macro inspection of an electric vehicle structural aluminum casting. Laser-guided precision calipers verifying flawless structural tolerances, smooth stamped edges, and integrated mounting points, proving world-class industrial manufacturing quality.",
    "Slow smooth rack focus from the digital caliper display across the smooth machined metal casting surface, precision metallic luster"
)

# CH04_SC006
add_scene(
    f"{STYLE}. A complex architectural concept blueprint of a fully vertically integrated mega-factory. Raw molten aluminum and chemical feedstocks enter one side of the vast facility, and finished smart automobiles roll out the other, rendered in warm glowing amber and dark slate.",
    "Slow camera push-in dolly shot toward the glowing industrial integration diagram, intricate manufacturing flows pulsing softly"
)

# CH04_SC007
add_scene(
    f"{STYLE}. An archival visual of a mid-century automotive assembly plant in Detroit or Wolfsburg. A single moving assembly line where workers attach pre-assembled subcomponents delivered from external supplier crates, classic industrial atmosphere in warm sepia tones.",
    "Slow tracking shot moving parallel with the vintage assembly line, conveying a century of traditional automotive assembly logic"
)

# CH04_SC008
add_scene(
    f"{STYLE}. A traditional automotive component sourcing pie chart displayed on a dark slate boardroom wall. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'LEGACY IN-HOUSE SOURCING: 30-35%'. A modest gold arc represents internal manufacturing while external suppliers dominate.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC009
add_scene(
    f"{STYLE}. An expansive logistics loading dock of a legacy German automotive factory. Dozens of delivery trucks from external tier-one component suppliers backing into bays, unloading crates of wiring, brakes, and instrument panels in evening mist.",
    "Slow panning shot along the row of supply trucks and logistics docks, warehouse floodlights casting warm amber pools across damp concrete"
)

# CH04_SC010
add_scene(
    f"{STYLE}. An aerial view of an ultra-modern automotive gigafactory in Fremont California at dawn. Sleek industrial glass, rooftop solar arrays, and high-tech vehicle staging lots illuminated by golden sunrise light against the California hills.",
    "Slow cinematic crane shot descending over the California electric vehicle factory complex as dawn sun warms the glass facades"
)

# CH04_SC011
add_scene(
    f"{STYLE}. A corporate component sourcing slide for a leading American electric vehicle maker. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TESLA MODEL 3 IN-HOUSE: 68%'. A glowing percentage dial in warm champagne gold on dark titanium.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC012
add_scene(
    f"{STYLE}. A team of Swiss automotive teardown engineers in white coats gathered around a large digital audit spreadsheet in a Zurich laboratory. Shocked, admiring expressions on their faces as consolidated internal sourcing ratios calculate on screen.",
    "Slow camera push-in shot toward the engineers conferring around the glowing terminal, warm laboratory lighting"
)

# CH04_SC013
add_scene(
    f"{STYLE}. An executive teardown breakdown diagram displayed on dark slate in Zurich. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BYD IN-HOUSE INTEGRATION: 75%'. A massive glowing golden bar towers over Western benchmarks.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC014
add_scene(
    f"{STYLE}. An economic map of China etched in brushed gold upon a dark walnut panel in a boardroom. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'DOMESTIC VALUE ADDED: 90%'. Luminous supply chain lines crisscross the mainland.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC015
add_scene(
    f"{STYLE}. Inside a high-precision automotive optical manufacturing workshop in Shenzhen. Automated injection-molding presses and robotic arms casting crystal-clear polycarbonate automotive headlight lenses with laser-guided precision under warm cleanroom illumination.",
    "Slow tracking shot following the robotic arm as it places a freshly cast automotive headlight assembly onto a velvet conveyor"
)

# CH04_SC016
add_scene(
    f"{STYLE}. A specialized precision machining facility in China. Computerized CNC lathes milling automotive air conditioning compressor housings from solid blocks of aircraft-grade aluminum, coolant mist catching warm overhead amber downlights.",
    "Slow macro tracking shot across the rotating CNC drill bit carving intricate compressor scroll channels with micron accuracy"
)

# CH04_SC017
add_scene(
    f"{STYLE}. A spacious automotive interior manufacturing facility. Automated polyurethane foam molding lines producing ergonomic car seats alongside robotic cleanroom lines assembling high-definition automotive digital touchscreens under warm inspection lamps.",
    "Slow panning shot from the seat foaming carousel across to the touchscreen calibration benches, demonstrating vast internal manufacturing breadth"
)

# CH04_SC018
add_scene(
    f"{STYLE}. Inside a modern battery gigafactory operated by FinDreams. Clean automated conveyor systems transporting long, slender Blade Battery cells in gleaming aluminum casings through precision laser-welding stations in deep velvety slate surroundings.",
    "Slow tracking shot gliding parallel with the row of polished Blade Battery cells moving through the automated assembly line"
)

# CH04_SC019
add_scene(
    f"{STYLE}. A forensic cost breakdown infographic of a modern electric vehicle. A full vehicle silhouette rendered in dark slate, with the structural floor battery pack glowing in warm electric amber, highlighting its thirty-five to forty percent share of total bill of materials.",
    "Slow camera push-in dolly shot toward the glowing battery enclosure beneath the vehicle silhouette"
)

# CH04_SC020
add_scene(
    f"{STYLE}. An automotive procurement contract on a European executive desk. High-voltage lithium battery supply line items marked with third-party supplier markups and wholesale packaging fees under warm office lamp illumination.",
    "Slow push-in shot toward the procurement contract figures, warm tungsten light catching the edge of a gold executive fountain pen"
)

# CH04_SC021
add_scene(
    f"{STYLE}. A European battery cell procurement invoice open on a desk in Wolfsburg. Line items displaying battery cell purchase prices of one hundred and ten to one hundred and thirty dollars per kilowatt-hour, stamped with external vendor logos.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC022
add_scene(
    f"{STYLE}. An industrial shipping warehouse in Europe. Crates of imported lithium-ion battery modules stacked on wooden pallets, bearing shipping manifests with high international logistics tariffs under sodium security lighting.",
    "Slow tracking shot past the stacked battery shipping crates, warm ambient lighting highlighting external logistics overhead"
)

# CH04_SC023
add_scene(
    f"{STYLE}. An executive financial audit slide from the Swiss teardown. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BLADE BATTERY PACK: $55/kWh'. A golden benchmark marker on dark slate beneath warm gallery spotlights.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC024
add_scene(
    f"{STYLE}. A side-by-side battery manufacturing cost comparison chart displayed on an engineering monitor. A golden bar for BYD Blade battery at fifty-five dollars stands thirty-six percent below the commercial benchmark of battery giant CATL. Warm studio lighting.",
    "Slow smooth push-in dolly shot toward the comparative cost bars, warm directional lighting highlighting the substantial cost chasm"
)

# CH04_SC025
add_scene(
    f"{STYLE}. A mechanical engineering exhibition stand displaying the integrated eight-in-one electric powertrain. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'INTEGRATED 8-IN-1 POWERTRAIN'. A compact, polished aluminum module glowing softly under warm spotlights.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC026
add_scene(
    f"{STYLE}. A traditional electric drive assembly disassembled on a laboratory floor. Separate electric motor, inverter box, onboard charger, gearbox, and thick copper wiring harnesses sprawling out with dozens of complex mechanical fasteners.",
    "Slow high-angle tracking shot over the cluttered traditional component layout, emphasizing excess bulk and complex connections"
)

# CH04_SC027
add_scene(
    f"{STYLE}. The compact single-piece aluminum casing of the eight-in-one electric drive unit. Seamless cast surfaces, minimal exterior wiring, and precision integrated cooling channels, representing a masterwork of mechanical consolidation.",
    "Slow circular orbital shot around the sleek unified powertrain module, warm golden highlights dancing across polished metal surfaces"
)

# CH04_SC028
add_scene(
    f"{STYLE}. An engineering scale in an automotive laboratory measuring the eight-in-one powertrain. The digital indicator shows a twenty percent weight reduction, while calipers confirm a fifteen percent space-saving volume reduction in warm cleanroom light.",
    "Slow push-in shot toward the digital scale and compact powertrain dimensions, clean analytical precision"
)

# CH04_SC029
add_scene(
    f"{STYLE}. A full-size vehicle chassis frame being assembled on a robotic line using Cell-to-Body architecture. Robotic grippers lower the structural battery pack directly into the vehicle monocoque, where it becomes the primary structural floorpan.",
    "Slow tracking shot moving with the robotic gantry as the battery housing locks seamlessly into the chassis floor"
)

# CH04_SC030
add_scene(
    f"{STYLE}. A technical cutaway illustration of Cell-to-Body vehicle architecture. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CELL-TO-BODY (CTB) ARCHITECTURE'. The battery pack housing serves directly as the load-bearing passenger cabin floor.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC031
add_scene(
    f"{STYLE}. A comparison of vehicle underbodies in a design studio. On one side, heavy redundant steel crossmembers of a traditional platform; on the other, the clean, uncluttered flush floor of the Cell-to-Body platform illuminated by warm raking light.",
    "Slow panning shot from the cluttered traditional frame across to the sleek integrated floor, highlighting structural elegance"
)

# CH04_SC032
add_scene(
    f"{STYLE}. An industrial economist writing cost equations on a large dark blackboard in an automotive engineering boardroom. Mathematical formulas linking vertical integration ratios to unit bill of materials in crisp chalk under warm tungsten lighting.",
    "Slow camera push-in dolly shot toward the blackboard formulas, capturing the rigorous mathematical foundation of manufacturing dominance"
)

# CH04_SC033
add_scene(
    f"{STYLE}. The complete Bill of Materials cost ledger of the BYD Seal lying open on an executive desk next to the teardown report of the German Volkswagen ID.4. Highlighting pens mark structural component cost discrepancies in warm amber light.",
    "Slow camera push-in dolly shot toward the open side-by-side cost spreadsheets on the dark wood desk"
)

# CH04_SC034
add_scene(
    f"{STYLE}. An executive boardroom presentation slide in Zurich. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BILL OF MATERIALS: -35% VS VW ID.4'. Comparative vehicle silhouettes with cost discrepancy callouts.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC035
add_scene(
    f"{STYLE}. A comparative manufacturing cost slide. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BILL OF MATERIALS: -15% VS TESLA MODEL 3'. An economic bar graph showing cost advantages even against Gigafactory Shanghai.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC036
add_scene(
    f"{STYLE}. An artistic visual of two balance scales resting on a dark walnut table. On one side sits razor-thin domestic profit margins; on the other, thick golden stacks representing export profits under warm directional banker lamp illumination.",
    "Slow smooth camera pan across the two sides of the executive scale, golden reflections shimmering on polished wood"
)

# CH04_SC037
add_scene(
    f"{STYLE}. A crowded automotive dealership showroom in a Chinese tier-two city during a holiday sales promotion. Crowds of budget-conscious shoppers surrounding heavily discounted compact vehicles, sales banners in crimson under bright fluorescent fixtures.",
    "Slow tracking shot through the bustling showroom floor, capturing the intense commercial pressure of the domestic price war"
)

# CH04_SC038
add_scene(
    f"{STYLE}. An expansive deep-water automotive export terminal in Shenzhen at golden hour sunset. Thousands of newly built electric cars driving in synchronized convoys up loading ramps into the belly of an immense ocean-going car carrier vessel.",
    "Slow cinematic aerial tracking shot over the loading ramp as hundreds of vehicles embark on the ocean transport vessel"
)

# CH04_SC039
add_scene(
    f"{STYLE}. A prestigious European automotive dealership showroom in Munich Germany. The imported Chinese electric sedan displayed on an illuminated turntable with an overseas sticker price fifty to eighty percent higher than its domestic Chinese price tag.",
    "Slow circular camera orbital shot around the sleek sedan in the European showroom, warm architectural spotlights highlighting metallic contours"
)

# CH04_SC040
add_scene(
    f"{STYLE}. An ocean-going cargo vessel sailing across open seas at dusk. Freight customs clearance documents and international maritime bills of lading laid out on a captain desk in warm cabin lighting.",
    "Slow camera push-in shot toward the maritime freight documents, ocean horizon visible through cabin windows"
)

# CH04_SC041
add_scene(
    f"{STYLE}. An executive financial export slide in Shenzhen. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'OVERSEAS NET PROFIT PER CAR: ~$2,900'. A towering golden export profit pillar in champagne gold on dark slate.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC042
add_scene(
    f"{STYLE}. A side-by-side unit profitability graphic: A modest one-thousand-dollar domestic margin bar contrasted with an immense twenty-nine hundred dollar overseas export profit bar in warm champagne gold on polished dark slate.",
    "Slow smooth push-in dolly shot toward the comparative profit pillars, warm directional lighting highlighting the threefold export advantage"
)

# CH04_SC043
add_scene(
    f"{STYLE}. A conceptual artistic visual of an oxygen tank crafted of brushed brass and dark titanium, pumping golden luminous liquid into an industrial manufacturing engine in a dark slate chamber, symbolizing export profits feeding domestic expansion.",
    "Slow orbital shot around the glowing brass oxygen reservoir, warm amber light radiating into velvety dark shadows"
)

# CH04_SC044
add_scene(
    f"{STYLE}. Swiss teardown engineers in a Zurich laboratory using high-magnification digital inspection microscopes to examine a disassembled central autonomous computing module. Focused analytical expressions under cool diagnostic ring lights.",
    "Slow tracking shot past the engineers observing magnified circuit traces on large diagnostic monitors"
)

# CH04_SC045
add_scene(
    f"{STYLE}. Close-up macro view of an exposed central computing circuit board. Laser diagnostic light traces silicon microchips, highlighting semiconductor packaging labels from Western chipmakers in warm raking light.",
    "Slow smooth rack focus across the rows of microprocessors, diagnostic laser beam illuminating silicon dies and gold bonding wires"
)

# CH04_SC046
add_scene(
    f"{STYLE}. Inside the luxurious cockpit of a premium Chinese electric SUV at night. The curved digital instrument cluster and central infotainment screen glowing with high-resolution graphics, responsive haptic controls under soft ambient amber cabin lighting.",
    "Slow camera push-in dolly shot toward the illuminated high-definition cockpit displays, smooth graphic animations and warm ambient glow"
)

# CH04_SC047
add_scene(
    f"{STYLE}. An engineering schematic of a vehicle computing architecture on dark slate. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'COCKPIT CHIP DEPENDENCE: QUALCOMM & NVIDIA'. Microprocessor silicon dies highlighted in warning crimson (#8B0000).",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH04_SC048
add_scene(
    f"{STYLE}. An automotive semiconductor research and development center in Beijing. Chinese chip engineers conferring around test benches evaluating domestic Horizon Robotics processor chips in high-tech cleanroom surroundings.",
    "Slow tracking shot through the semiconductor testing lab, engineers inspecting silicon wafer test fixtures under warm downlights"
)

# CH04_SC049
add_scene(
    f"{STYLE}. A geopolitical supply chain risk map displayed on a dark glass monitor in an executive office. Semiconductor trade export restriction corridors traced in deep warning red between California and Asia in low-key lighting.",
    "Slow camera push-in shot toward the highlighted trade restriction lines across the Pacific, serious strategic atmosphere"
)

# CH04_SC050
add_scene(
    f"{STYLE}. An expansive panoramic view of a massive automotive manufacturing complex in Shenzhen at sunset. Tens of thousands of workers, automated logistics trains, and towering stamping halls humming in synchronized industrial harmony.",
    "Slow majestic aerial tracking shot over the vast Shenzhen manufacturing campus, golden twilight illuminating the industrial roofs"
)

# CH04_SC051
add_scene(
    f"{STYLE}. A bustling modern automotive showroom floor in Southeast Asia where foreign buyers enthusiastically test-drive new electric cars. Warm architectural lighting, polished showroom tiles, and bustling commercial momentum.",
    "Slow tracking shot gliding through the showroom, capturing lively commercial engagement and competitive retail pricing"
)

# CH04_SC052
add_scene(
    f"{STYLE}. An executive boardroom in Shenzhen at night. Senior strategists standing before a dark panoramic glass window looking out over the illuminated city, reviewing oceanic logistics routes on glowing tablet computers.",
    "Slow camera push-in dolly shot toward the silhouettes of the executives overlooking the glowing metropolis"
)

# CH04_SC053
add_scene(
    f"{STYLE}. An immense physical globe in an international strategy office. Warm amber trade arteries sweep outward from Shenzhen across the Indian Ocean toward Southeast Asia, the Middle East, Latin America, and Europe, bypassing North America.",
    "Slow cinematic orbital shot gliding over the illuminated trade routes encircling the southern hemisphere"
)

# CH04_SC054
add_scene(
    f"{STYLE}. An emerging market highway in Southeast Asia during a tropical sunset. Modest suburban electrical grid wires and utility poles line the road, where highway fast-charging stations are completely absent under a warm golden sky.",
    "Slow tracking shot along the roadside utility poles, capturing the infrastructure bottleneck of rural emerging markets"
)

# CH04_SC055
add_scene(
    f"{STYLE}. A high-ranking corporate strategy war room. Automotive directors reviewing large topographical maps of developing nations, formulating an expansion strategy tailored for emerging infrastructure realities in warm low-key lighting.",
    "Slow push-in shot toward the strategic maps on the conference table, warm tungsten downlights casting deep velvety shadows"
)

# CH04_SC056
add_scene(
    f"{STYLE}. A dynamic montage of global industrial expansion: Deep-sea cargo vessels at port, overseas manufacturing plant construction sites, and municipal electric buses navigating European city streets in warm golden hour light.",
    "Slow smooth panning shot sweeping across the multifaceted visual elements of rapid international expansion"
)

# CH04_SC057
add_scene(
    f"{STYLE}. The historic entrance of an abandoned American automotive assembly plant in South America, its rusted gates pushed wide open as modern construction cranes and new industrial signage arrive in warm morning sunlight.",
    "Slow camera push-in shot through the newly opened gates toward the revitalized industrial complex beyond"
)

# CH04_SC058
add_scene(
    f"{STYLE}. An advanced fifth-generation super hybrid sedan driving along an open desert highway at sunset. Sleek aerodynamic bodywork reflecting the warm golden hour sky as it glides effortlessly past a remote, closed gasoline service station.",
    "Slow low-angle tracking shot alongside the hybrid vehicle cruising steadily down the empty highway into the sunset"
)

# CH04_SC059
add_scene(
    f"{STYLE}. The digital dashboard display of the super hybrid sedan illuminated at night. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'DM-I SUPER HYBRID: 2,100 KM RANGE'. The digital fuel and battery range indicator glows in warm amber.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# Write prompts file
content_prompts = "\n\n".join(prompts) + "\n"
out_prompts.write_text(content_prompts, encoding="utf-8")
print(f"Successfully generated {len(prompts)} scenes in {out_prompts.name}")

# Now generate chapter_04_visual.md
with open(ep_dir / "scene_timing_map.json", "r", encoding="utf-8") as f:
    all_scenes = json.load(f)

ch04_scenes = [s for s in all_scenes if s.get("chapter") == "04"]

visual_header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_04_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_04.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_04.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-12 22:52
-->

# Chapter 04 Visual Script — The Seventy-Five Percent Machine

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 4 (The Seventy-Five Percent Machine), đồng bộ toán học 1-1 với 59 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_04.txt`.

- **Vũ trụ Mỹ thuật:** High-Precision Cleanroom & Industrial Mastery.
- **Bảng màu Sâu lắng & Sang trọng:** Precision Cleanroom Charcoal (`#20242C`), Polished Dark Slate (`#1A202C`), Brushed Titanium, Electric Amber (`#F59E0B`), Imperial Champagne Gold (`#D4AF37`), Warning Crimson (`#8B0000`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Directional Warm Tungsten Rim Lights, Deep Velvety Shadows, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~20% cảnh mấu chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :---: | :---: |
"""

text_overlays_ch04 = {
    "CH04_SC004": "UBS EVIDENCE LAB: BYD SEAL TEARDOWN",
    "CH04_SC008": "LEGACY IN-HOUSE SOURCING: 30-35%",
    "CH04_SC011": "TESLA MODEL 3 IN-HOUSE: 68%",
    "CH04_SC013": "BYD IN-HOUSE INTEGRATION: 75%",
    "CH04_SC014": "DOMESTIC VALUE ADDED: 90%",
    "CH04_SC023": "BLADE BATTERY PACK: $55/kWh",
    "CH04_SC025": "INTEGRATED 8-IN-1 POWERTRAIN",
    "CH04_SC030": "CELL-TO-BODY (CTB) ARCHITECTURE",
    "CH04_SC034": "BILL OF MATERIALS: -35% VS VW ID.4",
    "CH04_SC035": "BILL OF MATERIALS: -15% VS TESLA MODEL 3",
    "CH04_SC041": "OVERSEAS NET PROFIT PER CAR: ~$2,900",
    "CH04_SC047": "COCKPIT CHIP DEPENDENCE: QUALCOMM & NVIDIA",
    "CH04_SC059": "DM-I SUPER HYBRID: 2,100 KM RANGE",
}

visual_descs_ch04 = {
    "CH04_SC001": "Lối vào tòa nhà nghiên cứu tài chính của ngân hàng Thụy Sĩ tại Zurich trong sương sớm, các chuyên gia xách cặp tài liệu bước vào.",
    "CH04_SC002": "Bên trong hangar mổ xẻ kỹ thuật Thụy Sĩ, chiếc sedan điện BYD Seal màu xám titan đặt trên cầu nâng thủy lực sáng bóng dưới đèn rọi.",
    "CH04_SC003": "Các kỹ sư Thụy Sĩ mặc áo lab trắng và găng tay tháo rời từng con ốc, bảng mạch và cell pin Blade sắp xếp ngăn nắp trên bàn phân loại.",
    "CH04_SC004": "Báo cáo mổ xẻ kỹ thuật dày cộp của UBS đặt trên bàn họp gỗ mahogany tại Frankfurt, bìa da đóng gáy xoắn dưới đèn bàn đồng thau.",
    "CH04_SC005": "Cận cảnh kiểm tra khớp nối nhôm đúc nguyên khối của thân xe bằng thước cặp điện tử, độ chính xác cơ khí đạt chuẩn quốc tế.",
    "CH04_SC006": "Bản vẽ phối cảnh kiến trúc siêu nhà máy tích hợp: Kim loại thô và hóa chất đi vào một đầu, xe hoàn thiện lăn bánh ra đầu kia.",
    "CH04_SC007": "Dây chuyền lắp ráp truyền thống thế kỷ 20 tại Detroit, công nhân chỉ đóng vai trò lắp ráp các cụm linh kiện do nhà thầu phụ giao đến.",
    "CH04_SC008": "Biểu đồ tỷ lệ tự chủ linh kiện của các hãng xe truyền thống trên tường đá phiến, tỷ lệ tự sản xuất nội bộ chỉ chiếm khiêm tốn 30-35%.",
    "CH04_SC009": "Cầu cảng tiếp nhận linh kiện của nhà máy Đức lúc chập tối, hàng chục xe tải từ Bosch và Continental lùi vào cửa kho giao hàng.",
    "CH04_SC010": "Góc nhìn từ trên cao xuống siêu nhà máy xe điện tại Fremont California lúc bình minh, biểu tượng đổi mới Thung lũng Silicon.",
    "CH04_SC011": "Biểu đồ tỷ lệ tự chủ linh kiện trên chiếc Tesla Model 3 hiển thị con số 68% trên màn hình titan trong phòng họp thiết kế.",
    "CH04_SC012": "Nhóm kỹ sư Thụy Sĩ tại phòng lab Zurich ngạc nhiên và thán phục khi bảng tính chi phí hiển thị tỷ lệ tự chủ vượt bậc của chiếc Seal.",
    "CH04_SC013": "Màn hình kiểm toán hiển thị con số chấn động: 75% toàn bộ linh kiện của chiếc BYD Seal do chính hãng tự sản xuất nội bộ.",
    "CH04_SC014": "Bản đồ kinh tế Trung Quốc khắc bằng vàng hiển thị 90% tổng giá trị gia tăng của chiếc xe được tạo ra ngay trên đất Trung Quốc.",
    "CH04_SC015": "Phân xưởng đúc quang học chính xác tại Thâm Quyến, cánh tay robot gắp cụm đèn pha vừa được đúc nguyên khối đặt lên băng chuyền.",
    "CH04_SC016": "Xưởng cơ khí tiện CNC chính xác, máy tiện tự động gia công lốc máy nén khí điều hòa từ phôi nhôm nguyên khối dưới tia dầu làm mát.",
    "CH04_SC017": "Phân xưởng đúc nệm ghế mút xốp tự động bên cạnh dây chuyền phòng sạch lắp ráp màn hình cảm ứng xoay trong cùng tổ hợp.",
    "CH04_SC018": "Bên trong siêu nhà máy pin FinDreams, băng chuyền tự động vận chuyển các thanh pin Blade mỏng dài qua trạm hàn laser chính xác.",
    "CH04_SC019": "Biểu đồ phân phẫu chi phí xe điện, khối pin nằm dưới sàn xe phát sáng ánh vàng hổ phách, chiếm tới 35-40% tổng giá thành chiếc xe.",
    "CH04_SC020": "Hợp đồng mua bán pin điện trên bàn giám đốc tập đoàn xe phương Tây, chi phí mua ngoài đội lên bởi biên lợi nhuận nhà cung cấp.",
    "CH04_SC021": "Hóa đơn mua cell pin của các hãng xe châu Âu hiển thị mức giá mua sỉ đắt đỏ từ 110 đến 130 USD trên mỗi kilowatt giờ.",
    "CH04_SC022": "Kho bãi lưu trữ các khối pin nhập khẩu tại cảng biển châu Âu, hàng ngàn pallet pin chịu thêm chi phí cước biển và thuế nhập khẩu.",
    "CH04_SC023": "Màn hình kiểm toán Thụy Sĩ hiển thị con số kỷ lục: Chi phí sản xuất khối pin Blade của BYD chỉ ở mức 55 USD một kilowatt giờ.",
    "CH04_SC024": "Biểu đồ so sánh chi phí pin: Mức giá 55 USD của BYD rẻ hơn 36% so với cả gã khổng lồ pin số một thế giới CATL trên màn hình lab.",
    "CH04_SC025": "Bục trưng bày hệ thống truyền động tích hợp tám-trong-một bằng nhôm đúc sáng bóng, các bộ phận lồng ghép hoàn hảo trong một khối.",
    "CH04_SC026": "Hệ thống truyền động điện truyền thống rời rạc: Mô-tơ, biến tần và hộp số nối với nhau bằng hàng chục dây cáp cam to bản phức tạp.",
    "CH04_SC027": "Cận cảnh khối đúc tích hợp tám-trong-một của BYD, loại bỏ toàn bộ các khớp nối kim loại và dây dẫn trung gian rườm rà.",
    "CH04_SC028": "Cân kỹ thuật công nghiệp hiển thị khối truyền động giảm 20% trọng lượng và tiết kiệm 15% không gian đóng gói trong khoang máy.",
    "CH04_SC029": "Dây chuyền lắp ráp khung gầm Cell-to-Body, robot đặt khối pin trực tiếp vào vị trí sàn chịu lực xe thay cho dầm ngang kim loại.",
    "CH04_SC030": "Mô hình cắt bổ công nghệ Cell-to-Body (CTB), vỏ cụm pin đóng vai trò chính là sàn xe chịu lực vững chắc cho toàn bộ thân xe.",
    "CH04_SC031": "So sánh hai khung gầm xe: Khung gầm truyền thống nhiều giằng thép cồng kềnh đối lập với khung gầm CTB phẳng phiu, tối giản.",
    "CH04_SC032": "Nhà kinh tế học công nghiệp viết phương trình chi phí sản xuất lên bảng đen, phân tích cấu trúc giá thành cạnh tranh không có đối thủ.",
    "CH04_SC033": "Hai tập hồ sơ bóc tách chi phí linh kiện của chiếc BYD Seal và Volkswagen ID.4 đặt song song trên bàn gỗ tối dưới ánh đèn bàn ấm.",
    "CH04_SC034": "Màn hình thuyết trình kết quả mổ xẻ UBS: Tổng chi phí vật liệu chế tạo chiếc BYD Seal rẻ hơn 35% so với chiếc Volkswagen ID.4.",
    "CH04_SC035": "Biểu đồ so sánh chi phí chứng minh chiếc BYD Seal thậm chí còn rẻ hơn 15% so với chiếc Tesla Model 3 lắp ráp ngay tại Thượng Hải.",
    "CH04_SC036": "Hình ảnh ẩn dụ chiếc cân cơ học đặt trên bàn gỗ: Một bên là lợi nhuận nội địa mỏng manh, một bên là lợi nhuận xuất khẩu dồi dào.",
    "CH04_SC037": "Showroom bán xe ô tô đông đúc tại một thành phố cấp hai Trung Quốc, khách hàng vây quanh những chiếc xe giảm giá dưới 15.000 USD.",
    "CH04_SC038": "Bến cảng xuất khẩu ô tô Thâm Quyến lúc hoàng hôn, hàng ngàn chiếc xe mới nối đuôi nhau lăn bánh lên tàu viễn dương đi khắp thế giới.",
    "CH04_SC039": "Showroom ô tô sang trọng tại Munich nước Đức, chiếc sedan Seal nhập khẩu được niêm yết giá bán cao hơn từ 50 đến 80% so với trong nước.",
    "CH04_SC040": "Tàu chở xe viễn dương rẽ sóng trên biển khơi lúc hoàng hôn, tập chứng từ hải quan và thuế quan nằm ngay ngắn trong cabin thuyền trưởng.",
    "CH04_SC041": "Màn hình tài chính hiển thị mức lợi nhuận ròng xuất khẩu đạt xấp xỉ 2.900 USD trên mỗi chiếc xe bán ra ở thị trường nước ngoài.",
    "CH04_SC042": "Biểu đồ so sánh trực quan mức lợi nhuận ròng xuất khẩu 2.900 USD cao gấp gần ba lần mức lợi nhuận 1.000 USD khi bán ở thị trường nội địa.",
    "CH04_SC043": "Hình ảnh ẩn dụ bình dưỡng khí bằng đồng và titan bơm dòng dưỡng chất vàng nuôi dưỡng cỗ máy sản xuất trong phòng tối sâu lắng.",
    "CH04_SC044": "Kỹ sư Thụy Sĩ dùng kính hiển vi điện tử soi vào bảng mạch điều khiển trung tâm của chiếc xe, phát hiện các chip tính toán cao cấp.",
    "CH04_SC045": "Cận cảnh bảng vi mạch viễn thông buồng lái, các con chip tính toán tự lái mang nhãn hiệu các hãng bán dẫn hàng đầu phương Tây.",
    "CH04_SC046": "Khoang lái hạng sang của chiếc SUV điện cao cấp trong đêm, màn hình kép hiển thị đồ họa sắc nét dưới đèn viền nội thất màu hổ phách.",
    "CH04_SC047": "Sơ đồ kiến trúc bán dẫn buồng lái và tự lái hiển thị sự phụ thuộc vào các dòng chip tính toán Qualcomm và Nvidia với vệt đỏ cảnh báo.",
    "CH04_SC048": "Trung tâm nghiên cứu bán dẫn ô tô tại Bắc Kinh, các kỹ sư kiểm tra các dòng chip nội địa Horizon Robotics trên bàn thử nghiệm.",
    "CH04_SC049": "Bản đồ rủi ro chuỗi cung ứng bán dẫn toàn cầu với các tuyến kiểm soát xuất khẩu công nghệ cao được khoanh vùng đỏ qua Thái Bình Dương.",
    "CH04_SC050": "Góc nhìn toàn cảnh trên cao xuống tổ hợp đại bản doanh Thâm Quyến lúc hoàng hôn, hàng ngàn công nhân và nhà xưởng vận hành nhịp nhàng.",
    "CH04_SC051": "Showroom ô tô tại Đông Nam Á tấp nập khách hàng chạy thử xe điện mới, ánh sáng ấm áp phản chiếu trên sàn gạch men bóng lộn.",
    "CH04_SC052": "Phòng họp hội đồng quản trị Thâm Quyến ban đêm, các giám đốc đứng nhìn ra cửa sổ kính lớn, toát lên tham vọng bành trướng toàn cầu.",
    "CH04_SC053": "Quả địa cầu trong phòng chiến lược, các tuyến thương mại màu vàng tỏa đi Nam Mỹ, Trung Đông, Đông Nam Á tránh xa Bắc Mỹ.",
    "CH04_SC054": "Tuyến đường quốc lộ ven biển Đông Nam Á dưới ánh hoàng hôn nhiệt đới, mạng lưới cột điện dân sinh thô sơ và không có trạm sạc cao tốc.",
    "CH04_SC055": "Phòng tác chiến chiến lược, các nhà hoạch định thảo luận trước tấm bản đồ địa lý các nước đang phát triển dưới ánh đèn ấm áp.",
    "CH04_SC056": "Hình ảnh tổng hợp chiến dịch bành trướng: Tàu biển rời bến, nhà máy tiếp quản ở nước ngoài và xe buýt điện chạy trên phố châu Âu.",
    "CH04_SC057": "Cổng nhà máy hoang phế của Ford tại Nam Mỹ mở toang, cần cẩu và biển hiệu mới của hãng xe Trung Quốc được đưa vào lắp đặt.",
    "CH04_SC058": "Chiếc xe siêu lai chạy bon bon trên con đường sa mạc lúc hoàng hôn, lướt qua trạm xăng đóng cửa mà không cần dừng lại sạc điện.",
    "CH04_SC059": "Màn hình đồng hồ kỹ thuật số trên táp-lô hiển thị tầm hoạt động lý thuyết 2.100 km của động cơ siêu lai DM-i phát sáng màu hổ phách."
}

rows_ch04 = []
for s in ch04_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descs_ch04.get(sid, "Bối cảnh công nghiệp thực tế đời thường.")
    overlay = text_overlays_ch04.get(sid, "Không")
    stream = "T2V"
    rows_ch04.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

visual_content = visual_header + "\n".join(rows_ch04) + "\n"
out_visual.write_text(visual_content, encoding="utf-8")
print(f"Generated {len(rows_ch04)} table rows in {out_visual.name}")
