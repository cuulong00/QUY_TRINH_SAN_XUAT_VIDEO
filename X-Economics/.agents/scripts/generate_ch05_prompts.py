from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_prompts = ep_dir / "prompts_chapter_05.txt"
out_visual = ep_dir / "chapter_05_visual.md"

STYLE = "A 2D warm cinematic editorial illustration in high-prestige maritime and industrial noir aesthetic. Deep harbor slate tones (#1B263B), warm sunset terracotta (#2A1D1A), and polished dark titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH05_SC001
add_scene(
    f"{STYLE}. An expansive high-angle panorama of the industrial manufacturing complex of Camaçari in Bahia Brazil at golden hour. Sprawling factory roofs, rail lines, and shipping roads stretching across the lush tropical landscape under warm amber skies.",
    "Slow cinematic crane shot descending slowly toward the industrial park as late-afternoon tropical sunlight casts long golden shadows"
)

# CH05_SC002
add_scene(
    f"{STYLE}. The monumental main entrance of the Camaçari automotive manufacturing complex. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CAMAÇARI COMPLEX: BAHIA, BRAZIL'. Tall palm trees flank the entrance under warm afternoon light.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC003
add_scene(
    f"{STYLE}. An executive boardroom in Dearborn Michigan in twenty twenty-one. An American corporate resolution document stamped with official red seals resting on a polished mahogany table beneath a warm brass reading lamp.",
    "Slow camera push-in dolly shot toward the formal corporate closure decree resting on the dark wooden table"
)

# CH05_SC004
add_scene(
    f"{STYLE}. An archival museum gallery wall in São Paulo displaying black-and-white photographs of a century of American automotive assembly in Brazil. Classic vintage trucks rolling off Brazilian assembly lines under warm gallery lights.",
    "Slow tracking shot gliding along the historical photographs, nostalgic warm lighting highlighting industrial heritage"
)

# CH05_SC005
add_scene(
    f"{STYLE}. The silent, darkened assembly hall of the abandoned Camaçari automotive plant. Disconnected assembly conveyors, motionless cranes, and dust motes drifting through long shafts of golden sunlight streaming through high warehouse skylights.",
    "Slow camera pull-back dolly shot down the silent central factory aisle, atmospheric golden light cutting through dusty shadows"
)

# CH05_SC006
add_scene(
    f"{STYLE}. A group of Brazilian autoworkers in worn industrial shirts standing outside the chained factory gates at dusk, looking through the fence with solemn, stoic expressions. The warm glow of a tropical twilight fades into indigo.",
    "Slow panning shot across the weathered, resilient faces of the Brazilian autoworkers in twilight shadows"
)

# CH05_SC007
add_scene(
    f"{STYLE}. An aerial view of the shuttered industrial facility at sunset. Miles of empty employee parking lots with wild grass growing through asphalt cracks, silhouetted against a dramatic crimson and amber evening sky.",
    "Slow majestic drone pull-away shot revealing the silent monumental scale of the shuttered industrial park"
)

# CH05_SC008
add_scene(
    f"{STYLE}. The main gate of the Camaçari complex three years later. Construction crews in bright safety vests, mobile cranes hoisting fresh architectural steel beams, and bright amber floodlights illuminating a major modernization project.",
    "Slow camera push-in shot toward the bustling renovated entrance, vibrant warm sunlight celebrating industrial rebirth"
)

# CH05_SC009
add_scene(
    f"{STYLE}. An executive delegation of Chinese automotive directors in dark tailored suits and Brazilian engineering leads arriving at the Camaçari complex, reviewing digital blueprints on tablets under warm morning sunlight.",
    "Slow tracking shot moving alongside the executive delegation as they walk purposefully toward the modernized plant pavilion"
)

# CH05_SC010
add_scene(
    f"{STYLE}. An official commercial investment protocol on an executive desk in Brasília. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'ACQUISITION INVESTMENT: 5.5B REAIS ($1.0B+ USD)'. A golden signed treaty on dark slate.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC011
add_scene(
    f"{STYLE}. Inside the newly renovated Camaçari stamping and welding hall. Modern robotic arms being calibrated by Brazilian technicians in clean blue uniforms, warm overhead amber task lighting illuminating polished concrete floors.",
    "Slow tracking shot gliding alongside the new robotic welding fixtures, bright sparks briefly glinting against deep slate shadows"
)

# CH05_SC012
add_scene(
    f"@president_brazil_lula.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, beard, hairstyle, and attire directly from the reference photo. The subject is warmly shaking hands with visiting automotive executives during an official state reception in Bahia, exuding presidential gravitas in warm directional lighting.",
    "Steady camera shot focusing on the cordial handshake and warm, dignified presidential reception, maintaining all details of the reference image exactly"
)

# CH05_SC013
add_scene(
    f"{STYLE}. A dramatic wide-angle shot of the Camaçari manufacturing hall. Above the entrance, a new modern industrial brand emblem shines brightly over the historic brick structure once built by Detroit, symbolizing a global power handover.",
    "Slow upward crane shot revealing the modern emblem mounted proudly over the historic industrial pavilion"
)

# CH05_SC014
add_scene(
    f"{STYLE}. A conceptual artistic visual showing the transformation of an industrial landscape. Weathered industrial rust on the left peeling away to reveal polished brushed titanium and modern automated production on the right under warm golden light.",
    "Slow smooth panning shot from the weathered industrial left to the gleaming modernized right, seamless cinematic flow"
)

# CH05_SC015
add_scene(
    f"{STYLE}. A high-altitude cartographic map of Latin America illuminated by warm golden trade corridors connecting Bahia to regional shipping hubs, set against deep navy oceanic waters in sophisticated editorial style.",
    "Slow camera push-in dolly shot toward the glowing trade corridors across Brazil and the Southern Cone"
)

# CH05_SC016
add_scene(
    f"{STYLE}. A grand strategic chessboard carved from dark mahogany and polished stone. Handcrafted automotive chess pieces representing emerging market production hubs positioned in calculated tactical formation under a warm banker lamp.",
    "Slow orbital shot around the dark mahogany chessboard, warm lighting catching the polished stone pieces"
)

# CH05_SC017
add_scene(
    f"{STYLE}. An official Brazilian Ministry of Finance tariff decree on dark slate. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BRAZIL EV IMPORT TARIFF: 35%'. Official green and gold federal ribbon and stamp.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC018
add_scene(
    f"{STYLE}. An automotive corporate war room in Shenzhen. Senior logistics planners quietly reviewing supply-chain integration schedules around a dark glass table, maintaining complete analytical calm beneath recessed downlights.",
    "Slow tracking shot across the composed strategists studying regional trade diagrams, deep professional discipline"
)

# CH05_SC019
add_scene(
    f"{STYLE}. An automotive component sourcing audit slide in Bahia. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'LOCAL CONTENT RATIO: >50%'. A glowing golden gauge indicates local Brazilian parts sourcing.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC020
add_scene(
    f"{STYLE}. An official Mercosur customs treaty certificate bearing Latin American flags resting on a dark walnut desk. A golden stamp certifies regional origin compliance under warm directional reading lamp illumination.",
    "Slow camera push-in dolly shot toward the certified regional trade treaty, gold-embossed text reflecting warm lamplight"
)

# CH05_SC021
add_scene(
    f"{STYLE}. Car transporter railcars carrying newly assembled vehicles crossing an international border bridge in South America. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'MERCOSUR TARIFF TO MEXICO & ARGENTINA: 0%'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC022
add_scene(
    f"{STYLE}. An international trade corridor map showing free-trade automotive shipments flowing from Brazil into Argentina and Mexico with zero percent tariffs, while a split view reveals European manufacturing expansion.",
    "Slow panning shot tracking the golden trade vectors across Latin America before transitioning to European maps"
)

# CH05_SC023
add_scene(
    f"{STYLE}. The European Commission building in Brussels under dark slate skies, juxtaposed against an illuminated map of Central Europe where Hungary is highlighted in glowing warm amber, representing an alternative gateway.",
    "Slow camera push-in dolly shot toward the glowing borders of Hungary on the European economic map"
)

# CH05_SC024
add_scene(
    f"{STYLE}. An expansive construction groundbreaking site in Szeged Hungary at golden hour. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'EUROPEAN HUB: SZEGED, HUNGARY'. Heavy earthmovers preparing foundations.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC025
add_scene(
    f"@pm_hungary_viktororban.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The subject is seated at an official governmental press desk in Budapest, signing an industrial investment protocol with quiet diplomatic confidence in warm directional light.",
    "Steady camera shot focusing on the subject signing the protocol, maintaining their composed expression and all details of the reference image exactly"
)

# CH05_SC026
add_scene(
    f"{STYLE}. A sleek red double-decker electric municipal bus gliding smoothly across Westminster Bridge in London at twilight. Big Ben illuminated in the warm background, the zero-emission bus leaving clean air in its wake.",
    "Slow tracking shot moving alongside the electric double-decker bus crossing the bridge, warm London streetlights reflecting on wet tarmac"
)

# CH05_SC027
add_scene(
    f"{STYLE}. A modern electric city bus turning through a vibrant neon-lit boulevard in Shinjuku Tokyo at night. Pedestrians on sidewalks, clean modern urban backdrop bathed in warm tungsten and soft neon reflections.",
    "Slow camera pan following the electric transit bus as it glides past illuminated Japanese storefronts in quiet motion"
)

# CH05_SC028
add_scene(
    f"{STYLE}. An illuminated global transit route map on a dark slate wall. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'GLOBAL ELECTRIC BUS FLEET: 100,000+ IN 400 CITIES'. Golden nodal points glow across major world capitals.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC029
add_scene(
    f"{STYLE}. A municipal bus depot in a European city at night. Dozens of electric buses connected to high-voltage overhead pantograph charging stations, green battery indicator lights glowing under warm depot floodlights.",
    "Slow tracking shot gliding down the row of charging electric buses in the depot, orderly industrial rhythm"
)

# CH05_SC030
add_scene(
    f"{STYLE}. A meeting room in a municipal city hall. Local transit commissioners in business suits reviewing electric bus fleet operational telemetry reports alongside international engineering liaisons under warm pendant lamps.",
    "Slow camera push-in dolly shot toward the municipal commissioners reviewing fleet efficiency reports"
)

# CH05_SC031
add_scene(
    f"{STYLE}. An ocean shipping container terminal in Singapore at dusk. Massive commercial car carrier ships docked along deep-water wharves, towering container cranes silhouetted against a dramatic golden-orange horizon.",
    "Slow cinematic panning shot across the bustling maritime harbor, container cranes operating in synchronized harmony"
)

# CH05_SC032
add_scene(
    f"{STYLE}. A maritime freight brokerage monitor in London displaying international car carrier daily charter rates. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CAR CARRIER CHARTER RATE: $115,000/DAY'. A sharp upward red spike.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC033
add_scene(
    f"{STYLE}. An executive naval engineering office in Shenzhen. A senior corporate strategist stamps an official shipbuilding commission document with red ink, greenlighting sovereign maritime fleet construction.",
    "Steady camera shot with subtle slow push-in on the naval construction contract as the official stamp lands firmly"
)

# CH05_SC034
add_scene(
    f"{STYLE}. A massive modern commercial shipyard in Yantai China. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'RO-RO ARMADA: 8 CUSTOM CARRIERS (5B YUAN)'. The enormous red-and-white hull of a purpose-built car carrier.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC035
add_scene(
    f"{STYLE}. The majestic bow of the giant car carrier BYD Explorer Number One cutting through ocean swells at golden hour sunset. Pristine white and blue hull, towering vehicle loading decks, and calm wake stretching into the dusk.",
    "Low-angle cinematic tracking shot parallel with the massive hull as ocean spray catches warm golden sunset light"
)

# CH05_SC036
add_scene(
    f"{STYLE}. Inside the cavernous internal vehicle deck of an ocean-going car carrier. Thousands of brand-new vehicles parked bumper-to-bumper in pristine geometric alignment under warm fluorescent safety lighting.",
    "Slow smooth tracking shot down the illuminated vehicle deck between endless rows of precision-parked new cars"
)

# CH05_SC037
add_scene(
    f"{STYLE}. An executive maritime logistics slide in Shenzhen. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'ANNUAL SOVEREIGN EXPORT CAPACITY: 1,000,000+ VEHICLES'. A glowing golden armada diagram.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC038
add_scene(
    f"{STYLE}. A global maritime navigation chart tracking continuous oceanic shipping lanes from Shenzhen through the Malacca Strait, Suez Canal, and Atlantic Ocean toward Rotterdam and Santos in warm glowing amber lines.",
    "Slow high-angle tracking shot along the illuminated maritime shipping corridors across the world ocean"
)

# CH05_SC039
add_scene(
    f"{STYLE}. The newly opened automotive manufacturing plant in Rayong Thailand. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'RAYONG PLANT THAILAND: 18B BAHT'. Modern glass administration building in tropical afternoon sun.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC040
add_scene(
    f"{STYLE}. An automotive retail showroom in Bangkok. A traditional Japanese sedan on one side looking conservative next to a sleek, feature-packed Chinese electric vehicle on the other, surrounded by enthusiastic Thai buyers.",
    "Slow tracking shot between the competing vehicles in the Bangkok showroom, capturing the shifting customer interest"
)

# CH05_SC041
add_scene(
    f"{STYLE}. An economic market share chart for Thailand passenger vehicle sales. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CHINESE EV SHARE IN THAILAND: 47%'. A rapid golden ascent on dark slate.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC042
add_scene(
    f"{STYLE}. An aerial view of a rural highway in the Global South at dusk. Mountain roads winding through lush tropical terrain where commercial electric vehicle charging plugs are completely non-existent.",
    "Slow cinematic tracking shot along the winding rural highway as twilight settles over the mountains"
)

# CH05_SC043
add_scene(
    f"{STYLE}. An authentic rural town square in Southeast Asia. Wooden utility poles carry tangled electrical distribution wires, motorcycles and utility pickup trucks parked outside local shops under warm sunset light.",
    "Slow panning shot across the authentic street scene, capturing the real-world infrastructure conditions of developing markets"
)

# CH05_SC044
add_scene(
    f"{STYLE}. A closed, weathered rural electrical transformer station behind chain-link fences under a hot afternoon sun, emphasizing electrical grid constraints in remote emerging market regions.",
    "Slow push-in shot toward the weathered transformer fence, heat waves shimmering over dry soil"
)

# CH05_SC045
add_scene(
    f"{STYLE}. A rugged, dusty Toyota Hilux pickup navigating a remote gravel mountain pass effortlessly, kicking up dust in warm golden sunlight, illustrating its long-standing dominance in off-grid terrain.",
    "Low-angle tracking shot moving with the Hilux wheels as it conquers the rugged unpaved mountain road"
)

# CH05_SC046
add_scene(
    f"{STYLE}. A high-tech automotive exhibition stand unveiling the fifth-generation DM-i super hybrid platform. An illuminated cutaway engine and battery transaxle glowing with intricate mechanical components under warm gallery downlights.",
    "Slow camera push-in dolly shot toward the hybrid transaxle cutaway, warm metallic reflections highlighting advanced engineering"
)

# CH05_SC047
add_scene(
    f"{STYLE}. An engineering dynamometer test cell displaying engine telemetry. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'ENGINE THERMAL EFFICIENCY: 46.06%'. A glowing golden thermodynamic efficiency curve on dark slate.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC048
add_scene(
    f"{STYLE}. An open desert highway stretching toward distant mountains at golden hour sunset. A sleek super hybrid sedan driving smoothly at highway speed, passing a remote closed fuel depot without needing to stop.",
    "Slow tracking shot alongside the hybrid sedan as golden sunset light reflects off its aerodynamic hood"
)

# CH05_SC049
add_scene(
    f"{STYLE}. A driver dashboard digital trip computer display. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'REAL-WORLD RANGE: 1,500 - 1,800 KM'. An amber digital fuel gauge indicates over three-quarters tank remaining.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH05_SC050
add_scene(
    f"{STYLE}. A comparative driving range infographic on dark polished slate. A towering golden bar for the super hybrid at eighteen hundred kilometers stands double the height of traditional gasoline and hybrid benchmarks.",
    "Slow smooth push-in dolly shot toward the comparative range bars, warm directional lighting highlighting the distance gap"
)

# CH05_SC051
add_scene(
    f"{STYLE}. An emerging market commuter driving home from an office district in Bangkok at dusk. The digital fuel range indicator shows abundant range after weeks of driving, passing busy roadside petrol stations with calm ease.",
    "Slow tracking shot from inside the passenger cabin looking past the driver toward the illuminated city street"
)

# CH05_SC052
add_scene(
    f"{STYLE}. A residential driveway of an emerging market family home at night. The family vehicle parked safely outside without requiring any charging cable or specialized home wallbox, ready for daily commuting.",
    "Slow camera push-in shot toward the vehicle resting under the warm porch light, quiet domestic peace"
)

# CH05_SC053
add_scene(
    f"{STYLE}. A monthly household budget spreadsheet on a kitchen table. A fuel expense column highlighted in green showing significant monthly savings compared to traditional gasoline and hybrid Japanese competitors.",
    "Slow push-in shot toward the handwritten budget ledger, warm overhead kitchen lamp creating an intimate domestic mood"
)

# CH05_SC054
add_scene(
    f"{STYLE}. A panoramic global collage: The Camaçari plant, electric transit buses in London, the Ro-Ro vessel at sea, and the super hybrid on rural highways, unified by golden trade corridors sweeping across the eighty-two percent world.",
    "Slow sweeping cinematic pan across the multifaceted elements of global conquest, warm harmonious golden hour illumination"
)

# CH05_SC055
add_scene(
    f"{STYLE}. The apex of a high-rise executive headquarters at night looking out over an illuminated metropolis, celebrating seemingly unstoppable global market expansion in warm tungsten and amber light.",
    "Slow camera push-in dolly shot toward the expansive glass window overlooking the glowing global city"
)

# CH05_SC056
add_scene(
    f"{STYLE}. A macro view of an intricate industrial mechanical foundation constructed of heavy steel plates. Deep hairline stress fractures spidering across the polished metal surface under high-tension loads in low-key lighting.",
    "Slow macro push-in shot toward the spreading hairline fractures in the metal foundation, dramatic raking warm light"
)

# CH05_SC057
add_scene(
    f"{STYLE}. An immense factory shift change in Shenzhen. An endless sea of tens of thousands of autoworkers in blue uniforms pouring out of factory gates into company streets under dusky evening skies.",
    "Slow high-angle tracking shot over the colossal crowd of autoworkers, capturing the staggering human scale of the workforce"
)

# CH05_SC058
add_scene(
    f"{STYLE}. An open corporate accounting ledger showing ballooning supplier payables and inventory holding costs, juxtaposed with an outdoor holding lot of depreciating used electric vehicles under grey rain.",
    "Slow camera push-in dolly shot toward the audit ledger, warm lamp light revealing stark financial liabilities"
)

# CH05_SC059
add_scene(
    f"{STYLE}. A dimly lit forensic economics study at night. A senior investigator opens a thick confidential dossier stamped with red audit seals, leaning forward under a single warm tungsten banker lamp.",
    "Slow camera push-in dolly shot toward the investigator hands opening the confidential audit dossier"
)

# CH05_SC060
add_scene(
    f"{STYLE}. An imposing industrial steel vault slowly opening in deep velvety shadows, revealing structural engineering blueprints marked with critical failure thresholds in warning crimson (#8B0000).",
    "Slow forward dolly shot through the heavy steel vault doors, dramatic low-key lighting illuminating structural blueprints"
)

# Write prompts file
content_prompts = "\n\n".join(prompts) + "\n"
out_prompts.write_text(content_prompts, encoding="utf-8")
print(f"Successfully generated {len(prompts)} scenes in {out_prompts.name}")

# Now generate chapter_05_visual.md
with open(ep_dir / "scene_timing_map.json", "r", encoding="utf-8") as f:
    all_scenes = json.load(f)

ch05_scenes = [s for s in all_scenes if s.get("chapter") == "05"]

visual_header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_05_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_05.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_05.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-12 23:00
-->

# Chapter 05 Visual Script — Reverse Colonization

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 5 (Reverse Colonization), đồng bộ toán học 1-1 với 60 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_05.txt`.

- **Vũ trụ Mỹ thuật:** Global Maritime Expansion & Industrial Revitalization.
- **Bảng màu Sâu lắng & Sang trọng:** Deep Harbor Slate (`#1B263B`), Warm Sunset Terracotta (`#2A1D1A`), Polished Dark Slate (`#1A202C`), Cargo Navy (`#0D1B2A`), Emerald Maritime (`#26A69A`), Warm Golden Amber (`#F59E0B`), Imperial Champagne Gold (`#D4AF37`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Directional Warm Tungsten Rim Lights, Velvety Deep Shadows, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~20% cảnh mấu chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :---: | :---: |
"""

text_overlays_ch05 = {
    "CH05_SC002": "CAMAÇARI COMPLEX: BAHIA, BRAZIL",
    "CH05_SC010": "ACQUISITION INVESTMENT: 5.5B REAIS ($1.0B+ USD)",
    "CH05_SC017": "BRAZIL EV IMPORT TARIFF: 35%",
    "CH05_SC019": "LOCAL CONTENT RATIO: >50%",
    "CH05_SC021": "MERCOSUR TARIFF TO MEXICO & ARGENTINA: 0%",
    "CH05_SC024": "EUROPEAN HUB: SZEGED, HUNGARY",
    "CH05_SC028": "GLOBAL ELECTRIC BUS FLEET: 100,000+ IN 400 CITIES",
    "CH05_SC032": "CAR CARRIER CHARTER RATE: $115,000/DAY",
    "CH05_SC034": "RO-RO ARMADA: 8 CUSTOM CARRIERS (5B YUAN)",
    "CH05_SC037": "ANNUAL SOVEREIGN EXPORT CAPACITY: 1,000,000+ VEHICLES",
    "CH05_SC039": "RAYONG PLANT THAILAND: 18B BAHT",
    "CH05_SC041": "CHINESE EV SHARE IN THAILAND: 47%",
    "CH05_SC047": "ENGINE THERMAL EFFICIENCY: 46.06%",
    "CH05_SC049": "REAL-WORLD RANGE: 1,500 - 1,800 KM",
}

visual_descs_ch05 = {
    "CH05_SC001": "Góc nhìn toàn cảnh trên cao xuống tổ hợp nhà máy Camaçari tại bang Bahia Brazil lúc hoàng hôn nhiệt đới trong nắng vàng ấm.",
    "CH05_SC002": "Cổng vào hoành tráng của khu công nghiệp Camaçari, hàng cây cọ nhiệt đới vươn cao trong nắng chiều rọi bóng dài.",
    "CH05_SC003": "Nghị quyết hội đồng quản trị của Ford năm 2021 đóng dấu đỏ trên bàn họp mahogany tại Dearborn dưới ánh đèn bàn đồng.",
    "CH05_SC004": "Bức tường phòng truyền thống trưng bày các bức ảnh đen trắng ghi dấu hơn một thế kỷ Ford sản xuất ô tô trên đất Brazil.",
    "CH05_SC005": "Nhà xưởng lắp ráp khổng lồ của Camaçari bị bỏ hoang, băng chuyền nguội lạnh và các vệt nắng bụi xuyên qua mái tôn thủng.",
    "CH05_SC006": "Hàng vạn công nhân luyện kim Brazil đứng ngoài hàng rào sắt nhà máy lúc chập tối, vẻ mặt trầm ngâm trước cảnh mất việc làm.",
    "CH05_SC007": "Bãi đỗ xe nhân viên rộng thênh thang bỏ hoang, cỏ dại mọc xuyên qua kẽ nứt nhựa đường dưới bầu trời hoàng hôn đỏ ối.",
    "CH05_SC008": "Ba năm sau, cổng nhà máy Camaçari bừng sáng trở lại với cần cẩu thi công và công nhân tấp nập trong công cuộc đại tu.",
    "CH05_SC009": "Đoàn lãnh đạo tập đoàn BYD trong trang phục vest tối màu bước vào cổng nhà máy cùng các kỹ sư Brazil dưới nắng sớm.",
    "CH05_SC010": "Văn bản cam kết đầu tư 5,5 tỷ Real (hơn 1 tỷ USD) đặt trên bàn làm việc tại thủ đô Brasília với quốc huy dập nổi sang trọng.",
    "CH05_SC011": "Phân xưởng hàn dập Camaçari được hiện đại hóa, các cánh tay robot mới tinh được kỹ sư hiệu chỉnh dưới ánh đèn ấm áp.",
    "CH05_SC012": "Tổng thống Brazil Lula da Silva bắt tay thân mật ban lãnh đạo BYD tại lễ đón tiếp ngoại giao kinh tế trang trọng tại Bahia.",
    "CH05_SC013": "Khung cảnh lịch sử: Hãng xe Trung Quốc tiếp quản chính tổ hợp sản xuất bị bỏ hoang của người Mỹ ngay tại sân sau Washington.",
    "CH05_SC014": "Hình ảnh chuyển giao công nghiệp: Mảng tường gạch cũ kỹ bong tróc nhường chỗ cho vách kính và khung thép titan sáng loáng.",
    "CH05_SC015": "Bản đồ vệ tinh Nam Mỹ với các tuyến vận tải màu vàng kim tỏa đi từ Bahia đến các trung tâm kinh tế khu vực.",
    "CH05_SC016": "Bàn cờ thế công nghiệp bằng gỗ óc chó và đá phiến, các quân cờ đại diện cho nhà máy vệ tinh được sắp đặt chiến lược.",
    "CH05_SC017": "Sắc lệnh tái áp thuế nhập khẩu xe điện 35% của Bộ Tài chính Brazil đặt trên bàn làm việc với dải ruy băng quốc kỳ.",
    "CH05_SC018": "Phòng tác chiến Thâm Quyến, các nhà hoạch định chiến lược điềm tĩnh vạch ra lộ trình tăng tốc nội địa hóa linh kiện.",
    "CH05_SC019": "Màn hình kiểm toán hiển thị tỷ lệ nội địa hóa linh kiện tại nhà máy Camaçari nhanh chóng vượt mốc 50% với biểu đồ vàng.",
    "CH05_SC020": "Chứng nhận quy tắc xuất xứ khối Mercosur đặt trên bàn làm việc, chứng nhận xe lắp ráp tại Brazil đạt chuẩn xe nội khối.",
    "CH05_SC021": "Đoàn tàu hỏa chở đầy xe ô tô hoàn thiện vượt qua cầu biên giới Nam Mỹ sang Argentina và Mexico với thuế suất 0%.",
    "CH05_SC022": "Bản đồ tuyến thương mại tự do vô hiệu hóa hàng rào thuế quan bảo hộ tại Nam Mỹ, chuyển tiếp sang bản đồ châu Âu.",
    "CH05_SC023": "Trụ sở Ủy ban Châu Âu tại Brussels mây xám, đối lập với vùng đất Hungary được tô sáng ánh vàng hổ phách trên bản đồ.",
    "CH05_SC024": "Công trường khởi công siêu tổ hợp sản xuất xe du lịch tại thành phố Szeged Hungary lúc hoàng hôn, máy xúc san ủi nền móng.",
    "CH05_SC025": "Thủ tướng Hungary Viktor Orbán ngồi tại bàn làm việc trang trọng tại Budapest, ký kết biên bản ghi nhớ hợp tác công nghiệp.",
    "CH05_SC026": "Chiếc xe buýt điện hai tầng màu đỏ lướt êm ái qua cầu Westminster tại London lúc hoàng hôn, tháp Big Ben rực sáng phía sau.",
    "CH05_SC027": "Chiếc xe buýt điện công cộng rẽ qua đại lộ rực rỡ ánh đèn neon tại Shinjuku Tokyo trong đêm, lướt đi trong tĩnh lặng.",
    "CH05_SC028": "Bản đồ mạng lưới xe buýt điện toàn cầu phát sáng hơn 100.000 xe lăn bánh qua 400 thành phố lớn tại châu Âu, Mỹ và châu Á.",
    "CH05_SC029": "Bến xe buýt đô thị ban đêm tại châu Âu, hàng chục xe buýt điện cắm sạc tại trạm sạc trên cao với đèn chỉ báo xanh lục.",
    "CH05_SC030": "Phòng họp tòa thị chính thành phố, các quan chức giao thông địa phương duyệt báo cáo vận hành xe buýt điện không phát thải.",
    "CH05_SC031": "Cảng biển container nước sâu Singapore lúc chập tối, các siêu tàu chở ô tô viễn dương neo đậu dọc cầu cảng rực rỡ ánh đèn.",
    "CH05_SC032": "Màn hình môi giới hàng hải London hiển thị giá cước thuê tàu chở xe tăng vọt lên mức kỷ lục 115.000 USD một ngày.",
    "CH05_SC033": "Văn phòng kỹ thuật hàng hải tại Thâm Quyến, hợp đồng đóng riêng 8 siêu tàu chở ô tô được lãnh đạo ký phê duyệt dứt khoát.",
    "CH05_SC034": "Xưởng đóng tàu khổng lồ tại Sơn Đông, thân tàu khổng lồ của siêu tàu Ro-Ro chuyên dụng đang được hàn lắp trong ụ cẩu khô.",
    "CH05_SC035": "Mũi siêu tàu BYD Explorer Số Một rẽ sóng đại dương lúc hoàng hôn, thân tàu trắng xanh đồ sộ phản chiếu ánh nắng chiều tà.",
    "CH05_SC036": "Bên trong khoang boong chứa xe khổng lồ của tàu biển, hàng ngàn chiếc xe mới tinh đỗ thẳng tắp như bàn cờ dưới đèn bảo an.",
    "CH05_SC037": "Màn hình logistics hàng hải hiển thị năng lực tự vận tải biển vượt mốc một triệu xe mỗi năm với biểu đồ hạm đội tàu.",
    "CH05_SC038": "Hải trình hàng hải trên hải đồ số, các tuyến tàu nối thông suốt từ Thâm Quyến qua eo Malacca đến cảng Rotterdam và Santos.",
    "CH05_SC039": "Nhà máy sản xuất Rayong 18 tỷ Baht tại Thái Lan trong nắng chiều nhiệt đới, xe mới xuất xưởng xếp hàng ngay ngắn.",
    "CH05_SC040": "Showroom ô tô tại Bangkok, khách hàng Thái Lan hào hứng trải nghiệm mẫu xe điện mới, đối lập với xe xăng truyền thống.",
    "CH05_SC041": "Biểu đồ thị phần xe điện Trung Quốc tại Thái Lan tăng vọt lên mức kỷ lục 47%, giáng đòn chí mạng vào thế độc tôn của xe Nhật.",
    "CH05_SC042": "Con đường cao tốc ven biển tại Đông Nam Á lúc hoàng hôn, nơi lưới điện nông thôn thô sơ và không có trạm sạc nhanh.",
    "CH05_SC043": "Góc phố thị trấn đang phát triển, cột điện chằng chịt dây nối và xe máy, xe bán tải đỗ bên đường trong nắng chiều.",
    "CH05_SC044": "Trạm biến áp điện nông thôn cũ kỹ sau hàng rào sắt, minh chứng cho sự thiếu thốn hạ tầng trạm sạc tại các vùng sâu vùng xa.",
    "CH05_SC045": "Chiếc bán tải Hilux bụi bặm vượt qua đoạn đường đèo sỏi đá lầy lội đầy dũng mãnh, biểu tượng cho sự bền bỉ ngoài vùng phủ lưới.",
    "CH05_SC046": "Bục trưng bày công nghệ siêu lai DM-i thế hệ thứ năm, khối động cơ và pin điện phát sáng ánh vàng hổ phách tinh xảo.",
    "CH05_SC047": "Màn hình đo kiểm nhiệt động cơ hiển thị con số hiệu suất kỷ lục 46,06% với đồ thị nhiệt động lực học sắc nét.",
    "CH05_SC048": "Chiếc sedan siêu hybrid chạy băng băng qua vùng bán sa mạc lúc hoàng hôn, lướt qua trạm xăng đóng cửa mà không cần dừng lại.",
    "CH05_SC049": "Màn hình đồng hồ kỹ thuật số táp-lô hiển thị tầm hoạt động thực tế đạt 1.500 đến 1.800 km chỉ sau một lần đổ đầy bình xăng.",
    "CH05_SC050": "Biểu đồ so sánh cự ly di chuyển: Cột mốc 1.800 km của động cơ siêu lai cao gấp đôi cự ly của xe xăng và hybrid truyền thống.",
    "CH05_SC051": "Người lái xe tại Bangkok đi làm hàng ngày trong giờ tan tầm, kim xăng vẫn báo đầy sau cả tuần di chuyển trong thành phố.",
    "CH05_SC052": "Sân nhà một gia đình trung lưu Đông Nam Á ban đêm, chiếc xe đỗ gọn gàng dưới đèn hiên mà không cần dây sạc phức tạp.",
    "CH05_SC053": "Bảng kê chi phí nhiên liệu hàng tháng trên bàn ăn gia đình, chi phí xăng tiết kiệm vượt trội so với các dòng xe đối thủ.",
    "CH05_SC054": "Bức tranh toàn cảnh kết hợp 4 trụ cột: Nhà máy tiếp quản, xe buýt điện, hạm đội tàu biển và động cơ siêu lai 2.100 km.",
    "CH05_SC055": "Tầng thượng tòa nhà trụ sở tập đoàn trong đêm nhìn ra vịnh biển rực rỡ, vẻ bề ngoài tưởng như đã nắm chắc ngai vàng thế giới.",
    "CH05_SC056": "Cận cảnh móng thép của cỗ máy công nghiệp khổng lồ xuất hiện những vết nứt rạn li ti dưới áp lực tải trọng quá lớn.",
    "CH05_SC057": "Dòng người công nhân gần 1 triệu người tan ca tại Thâm Quyến, biển người đông đúc phản ánh áp lực quỹ lương khổng lồ.",
    "CH05_SC058": "Bảng cân đối kế toán với các khoản công nợ nhà cung cấp kéo dài, bên cạnh bãi tập kết xe cũ mất giá dưới màn mưa phùn.",
    "CH05_SC059": "Bàn làm việc của chuyên gia điều tra kinh tế ban đêm, bàn tay lật mở tập hồ sơ kiểm toán bước vào phần phân tích đỉnh cao trào.",
    "CH05_SC060": "Cánh cửa sắt của pháo đài công nghiệp từ từ mở ra, bên trong là những bản thiết kế phân tích các tử huyệt cấu trúc nguy hiểm."
}

rows_ch05 = []
for s in ch05_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descs_ch05.get(sid, "Bối cảnh công nghiệp thực tế đời thường.")
    overlay = text_overlays_ch05.get(sid, "Không")
    stream = "I2V" if (sid in ["CH05_SC012", "CH05_SC025"]) else "T2V"
    rows_ch05.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

visual_content = visual_header + "\n".join(rows_ch05) + "\n"
out_visual.write_text(visual_content, encoding="utf-8")
print(f"Generated {len(rows_ch05)} table rows in {out_visual.name}")
