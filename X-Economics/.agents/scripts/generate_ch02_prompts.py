from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_prompts = ep_dir / "prompts_chapter_02.txt"
out_visual = ep_dir / "chapter_02_visual.md"

# Master aesthetic style parameters for Chapter 2: The Fall of Detroit & Wolfsburg
# Warm, Deep, Subdued, Industrial Decay with High Prestige & Gravitas
STYLE = "A 2D warm cinematic editorial illustration in high-prestige industrial noir luxury aesthetic. Deep mahogany slate tones (#231C18), weathered industrial rust charcoal (#2C2724), and brushed titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH02_SC001
add_scene(
    f"{STYLE}. An autumn afternoon in Wolfsburg Germany. A lone black executive sedan driving down a broad, quiet tree-lined boulevard bordering the Mittelland Canal. Amber-tinted autumn leaves blowing across clean asphalt, towering industrial brick structures in the soft-focus background under a calm dusk sky.",
    "Slow tracking shot gliding parallel with the dark sedan moving along the canal road, warm autumn sunlight catching the polished vehicle roof"
)

# CH02_SC002
add_scene(
    f"{STYLE}. An expansive pedestrian plaza outside an industrial administrative center in Wolfsburg. Empty stone benches, fallen brown leaves, and quiet glass office pavilions. Soft atmospheric evening haze hangs in the air, illuminated by warm amber streetlights.",
    "Slow smooth camera pan across the silent city plaza toward the imposing glass-and-steel automotive corporate towers"
)

# CH02_SC003
add_scene(
    f"{STYLE}. The monumental headquarters complex of Volkswagen in Wolfsburg. The historic red-brick thermal power plant with its four iconic towering smokestacks rising against an indigo twilight sky. Warm golden lights glow from administrative windows along the canal water.",
    "Low-angle slow tracking shot looking up at the historic brick towers reflected in the still canal water, majestic solemn scale"
)

# CH02_SC004
add_scene(
    f"{STYLE}. An archival museum gallery wall displaying framed sepia and monochrome photographs of post-war German automotive reconstruction. Pristine classic Beetles rolling off clean assembly lines in the nineteen-fifties, illuminated by warm museum picture lights.",
    "Slow camera push-in dolly shot toward the framed historical factory photographs, warm lighting accentuating historic craftsmanship"
)

# CH02_SC005
add_scene(
    f"{STYLE}. A vintage German automotive engineering workshop from the late twentieth century. Senior master machinists in grey aprons meticulously calibrating an all-metal precision gearbox on a heavy cast-iron bench under warm overhead tungsten lamps.",
    "Slow tracking shot across the master machinist hands adjusting the metallic gears with calipers, tactile precision mechanical detail"
)

# CH02_SC006
add_scene(
    f"{STYLE}. Front page of a prestigious German business broadsheet newspaper resting on a polished dark mahogany cafe table. Bold German headlines announcing industrial restructuring in crisp typography, beside a steaming porcelain cup of black coffee in morning sunlight.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC007
add_scene(
    f"{STYLE}. An official corporate press auditorium in Germany. A senior European automotive executive in a tailored charcoal suit standing behind a minimalist dark lectern, hands resting solemnly on a leather announcement binder under warm directional downlights.",
    "Slow camera push-in dolly shot toward the executive at the podium, maintaining a grave, dignified posture in warm stage shadows"
)

# CH02_SC008
add_scene(
    f"{STYLE}. An architectural site schematic of German vehicle assembly plants laid out across a dark slate conference table. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'PROPOSED PLANT CLOSURES: 2-3 GERMAN FACTORIES'. Red translucent boundary markers indicate targeted sites.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC009
add_scene(
    f"{STYLE}. A formal legal conference room. A thick, leather-bound collective bargaining agreement resting on a dark walnut table, an executive fountain pen laid beside it beneath the warm cone of a brass banker lamp.",
    "Slow camera push-in dolly shot toward the leather binder and gold-nibbed fountain pen resting under the warm desk lamp"
)

# CH02_SC010
add_scene(
    f"{STYLE}. An official labor pact document bearing official union seals resting on a conference table, stamped with a bold crimson cancellation marker. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'IG METALL PACT: TERMINATED'. Deep crimson bordeaux accents.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC011
add_scene(
    f"{STYLE}. Thousands of German autoworkers gathered outside an assembly plant gate in Wolfsburg for a peaceful union assembly. High-visibility orange vests and dark wool coats, serious determined expressions in cool autumn twilight under amber industrial security lights.",
    "Slow panning shot across the sea of determined autoworker faces gathered near the brick factory gates, solemn solidarity"
)

# CH02_SC012
add_scene(
    f"{STYLE}. An executive boardroom in Wolfsburg at night. Senior automotive directors huddled over financial audit books around a massive dark oak table, the room wrapped in deep velvety shadows with warm amber downlights focusing on audit reports.",
    "Slow tracking shot around the perimeter of the boardroom table, capturing deep contemplation and serious analytical focus"
)

# CH02_SC013
add_scene(
    f"{STYLE}. A macroeconomic diagnostic dashboard displayed on a brushed-titanium monitor in a financial office. Downward-trending red indicator lines tracing structural cost inflations and declining factory utilization rates in high-contrast slate tones.",
    "Slow camera push-in shot toward the downward financial trajectory curves on the illuminated monitor"
)

# CH02_SC014
add_scene(
    f"{STYLE}. An industrial energy terminal in northern Germany. Massive closed steel gas valves and frost-covered high-pressure pipeline manifolds standing silent at dusk. In the background, high-voltage electrical transformer towers hum under dramatic golden twilight clouds.",
    "Slow camera tilt-up shot from the cold steel gas pipelines toward the towering electrical transmission pylons in the twilight sky"
)

# CH02_SC015
add_scene(
    f"{STYLE}. A modern European automotive assembly line operating with reduced staffing. Robotic arms weld vehicle chassis in measured cadence, while German manufacturing technicians in grey uniforms review automated diagnostic terminals under warm pendant lamps.",
    "Slow tracking shot moving alongside the robotic assembly line, sparks briefly glinting against deep velvety industrial shadows"
)

# CH02_SC016
add_scene(
    f"{STYLE}. A stack of official European Union regulatory binders labeled with environmental emissions directives resting on an executive desk in Brussels. Brass measuring instruments and balance scales rest nearby on polished dark wood.",
    "Slow camera push-in shot toward the regulatory binders, warm directional light catching the European embossed seals"
)

# CH02_SC017
add_scene(
    f"{STYLE}. A conceptual split-screen composition showing an industrial factory in Germany in cold slate dusk on the left, and a sprawling, brightly lit automotive manufacturing complex in Shanghai China on the right, connected by a fractured golden financial pipeline.",
    "Slow smooth push-in shot toward the central fracture point, golden light shimmering across the dark slate background"
)

# CH02_SC018
add_scene(
    f"{STYLE}. A prestigious German corporate annual report open to a financial breakdown page. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CHINA PROFIT SHARE: >40%'. A golden highlighted bar graph indicates the historic overseas earnings pillar.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC019
add_scene(
    f"{STYLE}. A prestigious automotive showroom in Beijing in the early two-thousands. An affluent Chinese family admiring a pristine black Passat sedan under warm crystal chandeliers, chrome details gleaming with middle-class aspiration.",
    "Slow camera push-in shot toward the classic sedan, nostalgic warm lighting evoking the golden era of European automotive prestige"
)

# CH02_SC020
add_scene(
    f"{STYLE}. Close-up macro shot of the iconic chrome round automotive badge mounted on a dark metallic car grille, reflecting the neon streetscapes and bustling skyscrapers of modern Shanghai at night.",
    "Slow smooth rack focus from the polished chrome badge to the glittering neon urban skyline reflected in the vehicle paint"
)

# CH02_SC021
add_scene(
    f"{STYLE}. A high-tech automotive showroom in Shenzhen China today. Young Chinese tech-savvy consumers testing the rotating digital touchscreens and voice-controlled interfaces of sleek domestically built new energy vehicles under bright architectural lighting.",
    "Slow tracking shot through the modern showroom, capturing young buyers interacting enthusiastically with interactive digital displays"
)

# CH02_SC022
add_scene(
    f"{STYLE}. An electronic market share chart on a trading desk screen in Hong Kong. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'GERMAN MARKET SHARE IN CHINA: 20% -> <14%'. A sharp red descending slope across a dark slate background.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC023
add_scene(
    f"{STYLE}. Close-up of a classic German car door shutting in a quiet showroom. The heavy solid steel door latches with precision into its frame, but the interior analog dials remain dark and unappealing compared to modern digital cockpits.",
    "Slow camera pan from the heavy mechanical door latch into the darkened interior cabin, emphasizing mechanical obsolescence"
)

# CH02_SC024
add_scene(
    f"{STYLE}. A technical cutaway illustration of a dual-clutch transmission assembly on a display pedestal. Intricate gear teeth, polished synchronizer rings, and hydraulic valves illuminated by a warm amber spotlight on a dark slate floor.",
    "Slow camera orbital shot around the complex mechanical gearbox, precision steel surfaces reflecting warm directional light"
)

# CH02_SC025
add_scene(
    f"{STYLE}. The futuristic interior of a next-generation Chinese smart electric vehicle at night. An ultra-wide panoramic digital display screen spans the dashboard, glowing with fluid navigation maps, ambient LED cabin light bars in warm amber, and minimalist haptic controls.",
    "Slow camera push-in dolly shot into the glowing digital cockpit, seamless software animations and ambient warm lighting"
)

# CH02_SC026
add_scene(
    f"{STYLE}. German automotive software engineers in Wolfsburg conferring in an open-plan design studio at dusk. Multiple computer screens display intricate software code and diagnostic error logs, their faces reflecting cool screen glow against warm office shadows.",
    "Slow tracking shot past the focused engineers staring at complex code architectures, capturing intense problem-solving gravity"
)

# CH02_SC027
add_scene(
    f"{STYLE}. An aerial twilight view of the Rhine-Ruhr industrial corridor in Germany. Intersecting rail lines, dark steel mills, and silent automotive parts warehouses stretching toward the horizon under a brooding indigo sky.",
    "Smooth slow high-angle tracking shot gliding over the European industrial landscape as scattered amber factory lights flicker on"
)

# CH02_SC028
add_scene(
    f"{STYLE}. The skyline of Detroit Michigan at dusk viewed from across the Detroit River. The iconic glass towers of Renaissance Center rise darkly against a deep amber sunset, surrounded by vast industrial flatlands and highway loops.",
    "Slow cinematic panning shot across the Detroit waterfront, water reflecting golden twilight and dark urban silhouettes"
)

# CH02_SC029
add_scene(
    f"{STYLE}. An advanced electric vehicle assembly line inside an American automotive plant in Michigan. Sparkling clean white floors, yellow safety barriers, and robotic gantries assembling large aluminum battery trays under bright industrial lights.",
    "Slow tracking shot alongside the battery tray assembly line, automated tools lowering heavy structural components in rhythm"
)

# CH02_SC030
add_scene(
    f"{STYLE}. A corporate financial audit report from an American automaker open on a mahogany desk. Financial columns highlighted in warning crimson ink indicate massive recurring quarterly capital deficits. Warm desk lamp illumination.",
    "Slow camera push-in dolly shot toward the crimson highlighted balance sheet columns, warm light glinting off glossy paper"
)

# CH02_SC031
add_scene(
    f"{STYLE}. An executive boardroom in Dearborn Michigan at sunset. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'FORD MODEL E LOSSES: >$10 BILLION'. A large digital presentation chart reveals cumulative ten-billion-dollar operating deficits.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC032
add_scene(
    f"{STYLE}. An electric pickup truck rolling slowly off the final inspection turntable in an American assembly plant. Technicians in dark uniforms inspect panel gaps under bright fluorescent inspection arches in a quiet, solemn factory hall.",
    "Slow tracking shot following the electric pickup as it rolls onto the factory holding ramp, gleaming paint under inspection lamps"
)

# CH02_SC033
add_scene(
    f"{STYLE}. A financial analyst calculating unit economics in an automotive engineering office. On his calculator screen and ledger, unit production costs far exceed retail MSRP. Red ink notations mark severe negative margins.",
    "Slow push-in shot toward the analyst hands and calculator, capturing the tension of unsustainable cost equations"
)

# CH02_SC034
add_scene(
    f"{STYLE}. A brand-new electric pickup truck parked in an executive holding lot at dusk. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'LOSS PER EV DELIVERED: -$40,000 TO -$100,000'. Amber dusk light reflects on the hood.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC035
add_scene(
    f"{STYLE}. Senior executives of an American automaker gathered around a conference table in Detroit, their expressions solemn as they review a strategic retrenchment memo titled Operational Realignment. Dark mahogany surroundings.",
    "Slow panning shot across the solemn faces of the American automotive leadership, warm tungsten downlights casting deep shadows"
)

# CH02_SC036
add_scene(
    f"{STYLE}. An uncompleted electric battery gigafactory construction site in the American Midwest at sunset. Exposed steel girders and concrete foundations stand partially paused under long amber shadows, cranes idle against the evening sky.",
    "Slow pull-back shot revealing the immense scale of the paused battery factory site, dramatic sunset clouds overhead"
)

# CH02_SC037
add_scene(
    f"{STYLE}. An American suburban automotive dealership lot filled exclusively with high-margin, full-size gasoline pickup trucks and large SUVs. Chrome grilles gleam brightly under morning sunlight, commercial vehicle transport trailers arriving in background.",
    "Slow tracking shot through the dense rows of shiny gasoline trucks, celebrating traditional domestic cash generators"
)

# CH02_SC038
add_scene(
    f"{STYLE}. A towering symbolic tariff wall constructed of thick steel plates and concrete barriers encircling an American automotive complex. Warm golden sunlight glints on the steel wall, providing an impenetrable defensive perimeter.",
    "Low-angle slow tracking shot moving along the base of the massive tariff barrier, reinforcing themes of protected isolation"
)

# CH02_SC039
add_scene(
    f"{STYLE}. An expansive showroom of a premier American truck dealership. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'US AVERAGE RETAIL TRUCK: $80,000'. A top-trim luxury pickup truck displayed on a turntable.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC040
add_scene(
    f"{STYLE}. A historic industrial foundry in northern France at dusk. Weathered brick facades and silent cooling towers surrounded by rail spurs, reflecting the broader contraction of European legacy manufacturing.",
    "Slow cinematic crane shot drifting across the weathered brick industrial buildings as evening lights warm the cool twilight"
)

# CH02_SC041
add_scene(
    f"{STYLE}. A financial earnings slide on a presentation screen in Paris. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'STELLANTIS NET PROFIT: -50%'. A sharp downward red arrow beside consolidated financial totals.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC042
add_scene(
    f"{STYLE}. Italian and French autoworkers exiting a shuttered engine manufacturing plant in Turin Italy at dusk. Long shadows stretch across cobblestone streets as workers carry toolboxes toward home under dim streetlights.",
    "Slow tracking shot following the footsteps of departing autoworkers, capturing melancholy industrial quietude"
)

# CH02_SC043
add_scene(
    f"{STYLE}. The global headquarters tower of Nissan in Yokohama Japan at dusk. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'NISSAN GLOBAL LAYOFFS: 9,000 WORKERS'. The modern glass facade reflects the grey waters of Tokyo Bay.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC044
add_scene(
    f"{STYLE}. Two historic Japanese corporate logos displayed side by side on a minimalist cedar podium in Tokyo. Traditional architectural wooden screens frame the ceremonial dais under warm indirect lighting.",
    "Slow camera push-in dolly shot toward the joint corporate presentation dais, warm ceremonial lighting highlighting fine wood grains"
)

# CH02_SC045
add_scene(
    f"{STYLE}. Senior executives of Nissan and Honda seated side by side at a joint memorandum signing ceremony in Tokyo. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'NISSAN-HONDA EMERGENCY ALLIANCE'. Dark suits, dignified bows.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC046
add_scene(
    f"{STYLE}. A conceptual artistic tableau representing the twentieth-century automotive order. Heavy iron cogwheels and brass mechanical gears resting in solemn stillness on a polished dark walnut surface, warm amber light glinting on steel teeth.",
    "Slow orbital camera shot around the still mechanical gears, warm lighting creating rich golden highlights on dark cast iron"
)

# CH02_SC047
add_scene(
    f"{STYLE}. An executive boardroom table with empty high-back leather chairs in a historic American automotive headquarters. Stacks of unread operational reports and cold coffee cups in the twilight, a sense of an empire in retreat.",
    "Slow tracking shot past the empty boardroom chairs toward the large window overlooking the darkened city skyline"
)

# CH02_SC048
add_scene(
    f"{STYLE}. A panoramic dusk view overlooking an expansive automotive assembly complex in the American Rust Belt. Steam slowly billows from ventilation stacks, warm amber perimeter lights illuminating vast fields of empty asphalt.",
    "Slow smooth aerial tracking shot over the silent industrial complex, golden twilight deepening into velvet blue"
)

# CH02_SC049
add_scene(
    f"{STYLE}. Automotive corporate executives in Brussels and Detroit conferring via secure teleconference screens in dim walnut offices, their expressions anxious and fragmented as they coordinate defensive tariff strategies.",
    "Slow push-in shot toward the glowing teleconference display, capturing the fractured, reactive posture of legacy giants"
)

# CH02_SC050
add_scene(
    f"{STYLE}. A sophisticated investigative research studio with multiple monitors analyzing macroeconomic supply chain flows. An open leather dossier and a fountain pen rest on a warm mahogany desk, embodying rigorous, independent investigative journalism.",
    "Slow camera push-in dolly shot toward the investigative desk and open dossier, warm tungsten light creating an inviting intellectual atmosphere"
)

# CH02_SC051
add_scene(
    f"{STYLE}. A clean, elegant subscriber appreciation card crafted in embossed champagne gold on dark slate resting beside an analyst desk. Subtle gold lettering on the desk displays 'X-ECONOMICS INVESTIGATIVE DESK'. Warm amber lighting.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH02_SC052
add_scene(
    f"{STYLE}. A solitary, majestic stone fortress perched atop a misty mountain ridge at dawn, symbolizing an impregnable industrial citadel. Golden sunrise rays illuminate the ancient fortress walls while storm clouds gather in the valley below.",
    "Slow cinematic crane shot rising above the fortress ramparts, warm dawn sunlight piercing through dramatic dark clouds"
)

# CH02_SC053
add_scene(
    f"{STYLE}. Inside a pristine automotive engineering laboratory in Japan. A reliable hybrid internal combustion engine and planetary gearset gleaming under precision warm spotlights, completely separated from volatile battery hype.",
    "Slow tracking shot around the immaculate hybrid engine assembly, golden highlights dancing on machined aluminum"
)

# CH02_SC054
add_scene(
    f"{STYLE}. A secure vault chamber lined with dark steel safety deposit boxes and audited balance sheet ledgers inside a Japanese financial institution. Piles of investment-grade sovereign bonds and cash reserves bathed in warm amber security glow.",
    "Slow forward dolly shot down the vault corridor, warm directional light reflecting off polished steel vault doors"
)

# CH02_SC055
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and round eyeglasses directly from the reference photo. The subject stands tall in a bespoke dark suit beside a gleaming hybrid vehicle in an executive boardroom, gazing forward with calm, unshakable authority. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'THE LAST TITAN: TOYOTA'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# Write prompts file
content_prompts = "\n\n".join(prompts) + "\n"
out_prompts.write_text(content_prompts, encoding="utf-8")
print(f"Successfully generated {len(prompts)} scenes in {out_prompts.name}")

# Now generate chapter_02_visual.md
with open(ep_dir / "scene_timing_map.json", "r", encoding="utf-8") as f:
    all_scenes = json.load(f)

ch02_scenes = [s for s in all_scenes if s.get("chapter") == "02"]

visual_header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_02_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_02.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_02.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-12 22:45
-->

# Chapter 02 Visual Script — The Fall of Detroit & Wolfsburg

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 2 (The Fall of Detroit & Wolfsburg), đồng bộ toán học 1-1 với 55 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_02.txt`.

- **Vũ trụ Mỹ thuật:** The Fall of Industrial Empires & Legacy Reckoning.
- **Bảng màu Sâu lắng & Sang trọng:** Deep Mahogany Slate (`#231C18`), Weathered Rust Charcoal (`#2C2724`), Deep Industrial Slate (`#1E242B`), Brushed Titanium, Warning Crimson Bordeaux (`#8B0000`), Warm Ivory Cream (`#FAF7EE`), Imperial Champagne Gold (`#D4AF37`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Directional Warm Tungsten Rim Lights, Deep Velvety Shadows, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~20% cảnh then chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :---: | :---: |
"""

text_overlays_ch02 = {
    "CH02_SC008": "PROPOSED PLANT CLOSURES: 2-3 GERMAN FACTORIES",
    "CH02_SC010": "IG METALL PACT: TERMINATED",
    "CH02_SC018": "CHINA PROFIT SHARE: >40%",
    "CH02_SC022": "GERMAN MARKET SHARE IN CHINA: 20% -> <14%",
    "CH02_SC031": "FORD MODEL E LOSSES: >$10 BILLION",
    "CH02_SC034": "LOSS PER EV DELIVERED: -$40,000 TO -$100,000",
    "CH02_SC039": "US AVERAGE RETAIL TRUCK: $80,000",
    "CH02_SC041": "STELLANTIS NET PROFIT: -50%",
    "CH02_SC043": "NISSAN GLOBAL LAYOFFS: 9,000 WORKERS",
    "CH02_SC045": "NISSAN-HONDA EMERGENCY ALLIANCE",
    "CH02_SC055": "THE LAST TITAN: TOYOTA",
}

visual_descs_ch02 = {
    "CH02_SC001": "Buổi chiều thu vắng lặng tại Wolfsburg, chiếc sedan đen chạy dọc đại lộ ven kênh Mittelland dưới hàng cây lá vàng rụng.",
    "CH02_SC002": "Quảng trường vắng vẻ trước tòa nhà hành chính Volkswagen, lá rụng trên ghế đá và sương chiều bảng lảng dưới ánh đèn vàng ấm.",
    "CH02_SC003": "Nhà máy nhiệt điện gạch đỏ lịch sử với bốn ống khói khổng lồ sừng sững bên bờ kênh soi bóng trong ánh hoàng hôn tím thẫm.",
    "CH02_SC004": "Bức tường phòng truyền thống trưng bày các bức ảnh đen trắng thời kỳ phục hưng công nghiệp Đức sau chiến tranh với dòng xe Beetle huyền thoại.",
    "CH02_SC005": "Xưởng cơ khí chính xác thế kỷ 20, các kỹ sư bậc thầy Đức cẩn trọng hiệu chỉnh hộp số kim loại dưới ánh đèn bàn tungsten ấm.",
    "CH02_SC006": "Trang nhất tờ báo kinh tế Đức Handelsblatt đặt trên bàn cafe gỗ tối, dòng tít in đậm về cuộc khủng hoảng tái cơ cấu sản xuất.",
    "CH02_SC007": "Lãnh đạo Volkswagen đứng sau bục phát biểu tối giản trong khán phòng báo chí, vẻ mặt nghiêm trang, trầm lắng dưới đèn rọi.",
    "CH02_SC008": "Bản đồ quy hoạch các nhà máy lắp ráp xe hơi trên đất Đức, các điểm khoanh vùng đỏ đánh dấu 2-3 nhà máy đối diện nguy cơ đóng cửa.",
    "CH02_SC009": "Thỏa thuận bảo đảm việc làm lịch sử đóng bìa da trên bàn hội nghị, cây bút máy đặt bên cạnh dưới ánh đèn bàn chụp đồng.",
    "CH02_SC010": "Văn bản thỏa thuận 30 năm với công đoàn IG Metall bị đóng dấu hủy bỏ màu đỏ bordeaux, đánh dấu bước ngoặt chấn động nước Đức.",
    "CH02_SC011": "Hàng ngàn công nhân mặc áo phản quang cam và áo khoác dạ tụ họp ngoài cổng nhà máy Wolfsburg trong trật tự, ánh mắt cương nghị.",
    "CH02_SC012": "Phòng họp hội đồng quản trị ban đêm tại Wolfsburg, các giám đốc trầm ngâm xem báo cáo tài chính dày cộp dưới ánh đèn hắt trần.",
    "CH02_SC013": "Màn hình titan hiển thị đồ thị chi phí năng lượng và tỷ lệ sử dụng công suất nhà máy dốc đứng xuống đáy trong gam màu slate.",
    "CH02_SC014": "Trạm van khí đốt công nghiệp đóng kín trong sương chiều, đối lập với cột điện cao thế vươn cao trên bầu trời giông bão hoàng hôn.",
    "CH02_SC015": "Dây chuyền lắp ráp tự động vận hành với lượng công nhân tinh giảm, tia lửa hàn robot lóe sáng trong bóng tối phân xưởng có chiều sâu.",
    "CH02_SC016": "Chồng tài liệu pháp quy về tiêu chuẩn khí thải Euro của Ủy ban Châu Âu đặt trên bàn làm việc tại Brussels cùng thước đo kim loại.",
    "CH02_SC017": "Khung hình phân đôi ẩn dụ: Nhà máy Wolfsburg trong sương xám bên trái và tổ hợp sản xuất rực sáng tại Thượng Hải bên phải bị rạn nứt kết nối.",
    "CH02_SC018": "Báo cáo thường niên mở trang phân bổ lợi nhuận, cột mốc Trung Quốc đóng góp trên 40% lợi nhuận toàn cầu nổi bật sắc vàng kim.",
    "CH02_SC019": "Showroom ô tô tại Bắc Kinh đầu những năm 2000, gia đình trung lưu hân hoan bên chiếc Passat đen bóng dưới ánh đèn chùm ấm áp.",
    "CH02_SC020": "Cận cảnh logo VW mạ crôm sáng bóng trên lưới tản nhiệt xe, phản chiếu ánh đèn neon của các tòa nhà chọc trời Thượng Hải.",
    "CH02_SC021": "Showroom xe điện thông minh tại Thâm Quyến, giới trẻ trải nghiệm màn hình xoay mượt mà và giao diện số trong ánh sáng hiện đại.",
    "CH02_SC022": "Màn hình giao dịch tài chính Hồng Kông hiển thị thị phần xe Đức tại Trung Quốc rơi tự do từ trên 20% xuống dưới 14%.",
    "CH02_SC023": "Cận cảnh tiếng đóng cửa xe đầm chắc của chiếc Passat trong showroom vắng, nhưng khoang lái cơ học cổ điển đã mất sức hút.",
    "CH02_SC024": "Mô hình cắt bổ hộp số ly hợp kép phức tạp với hàng trăm bánh răng thép sáng bóng đặt trên bệ trưng bày phòng lab.",
    "CH02_SC025": "Khoang lái kỹ thuật số tương lai của xe điện Trung Quốc trong đêm, màn hình trải dài phát sáng bản đồ động và đèn viền hổ phách.",
    "CH02_SC026": "Các kỹ sư phần mềm Đức tại Wolfsburg tập trung trước màn hình máy tính hiển thị mã nguồn và nhật ký lỗi phần mềm buồng lái.",
    "CH02_SC027": "Góc máy trên cao nhìn xuống vùng công nghiệp Rhine-Ruhr, mạng lưới đường sắt và các nhà kho linh kiện trầm mặc lúc chập tối.",
    "CH02_SC028": "Đường chân trời Detroit bên sông lúc hoàng hôn, tòa tháp Renaissance Center sừng sững in bóng đen trên nền trời cam cháy.",
    "CH02_SC029": "Phân xưởng lắp ráp xe điện hiện đại của Ford tại Michigan, sàn epoxy trắng tinh và cánh tay robot nâng khung pin nhôm lớn.",
    "CH02_SC030": "Báo cáo tài chính nội bộ với các dòng số liệu thâm hụt hoạt động hàng tỷ USD của mảng xe điện được đánh dấu bằng bút dạ đỏ.",
    "CH02_SC031": "Phòng họp lãnh đạo tại Dearborn Michigan, màn hình hiển thị con số lỗ lũy kế vượt mốc 10 tỷ USD của bộ phận Model e.",
    "CH02_SC032": "Chiếc xe bán tải điện F-150 Lightning lăn bánh chậm rãi khỏi bệ kiểm tra cuối cùng trong nhà máy vắng lặng, ánh sơn lấp lánh.",
    "CH02_SC033": "Chuyên gia kế toán chi phí tại Detroit tính toán biên lợi nhuận, chi phí linh kiện vượt xa giá niêm yết bán lẻ xe.",
    "CH02_SC034": "Chiếc xe bán tải điện đỗ trên bãi xuất xưởng lúc hoàng hôn, tem hiển thị mức lỗ 40.000 đến 100.000 USD trên mỗi xe giao đến tay khách.",
    "CH02_SC035": "Ban lãnh đạo Detroit ngồi quanh bàn hội nghị gỗ mahogany, nét mặt trầm trọng xem bản ghi nhớ thu hẹp quy mô sản xuất điện hóa.",
    "CH02_SC036": "Công trường xây dựng nhà máy pin dở dang tại vùng Trung Tây nước Mỹ lúc hoàng hôn, khung thép và cần cẩu đứng im dưới bóng chiều.",
    "CH02_SC037": "Bãi đại lý ô tô ngoại ô ngập tràn các mẫu xe bán tải chạy xăng và SUV cỡ lớn mạ crôm bóng loáng dưới nắng sớm.",
    "CH02_SC038": "Bức tường chắn thuế quan tượng trưng bằng thép dày và bê tông bao quanh tổ hợp sản xuất Mỹ, ánh nắng hoàng hôn rọi bóng dài.",
    "CH02_SC039": "Showroom xe bán tải cao cấp của Mỹ, chiếc bán tải cỡ lớn giá 80.000 USD đỗ kiêu hãnh trên bục quay dưới ánh đèn rực rỡ.",
    "CH02_SC040": "Xưởng đúc công nghiệp lịch sử tại miền bắc nước Pháp lúc hoàng hôn, ống khói nguội lạnh phản ánh sự thu hẹp công nghiệp cựu lục địa.",
    "CH02_SC041": "Màn hình thuyết trình kết quả kinh doanh tại Paris, mũi tên đỏ chỉ lợi nhuận ròng tập đoàn Stellantis sụt giảm 50%.",
    "CH02_SC042": "Công nhân cơ khí Pháp và Ý xách hộp đồ nghề rời khỏi nhà máy đóng cửa tại Turin trong bóng chiều tà trên đường lát đá cổ kính.",
    "CH02_SC043": "Tòa tháp trụ sở Nissan tại Yokohama soi bóng xuống vịnh Tokyo xám tro, thông báo cắt giảm 9.000 việc làm toàn cầu.",
    "CH02_SC044": "Hai biểu tượng thương hiệu Nissan và Honda đặt cạnh nhau trên bục gỗ tuyết tùng tối giản trong phòng họp truyền thống Tokyo.",
    "CH02_SC045": "Lãnh đạo Nissan và Honda ngồi cạnh nhau ký thỏa thuận liên minh sinh tồn khẩn cấp, hai bên cúi chào tôn trọng nhau.",
    "CH02_SC046": "Hình tượng nghệ thuật ẩn dụ: Các bánh răng cơ khí kim loại nặng thế kỷ 20 nằm bất động trên mặt bàn gỗ óc chó sẫm màu.",
    "CH02_SC047": "Bàn họp hội đồng quản trị vắng bóng người với các ghế da cao cấp và tách cà phê nguội lúc chập tối trong văn phòng Mỹ.",
    "CH02_SC048": "Góc nhìn toàn cảnh trên cao xuống tổ hợp nhà máy lắp ráp xe hơi tại Vành đai Rỉ sét nước Mỹ, hơi nước bốc chậm từ ống thông gió.",
    "CH02_SC049": "Các lãnh đạo công nghiệp tại Brussels và Detroit hội đàm trực tuyến qua màn hình trong phòng tối, vẻ mặt lo âu về chính sách.",
    "CH02_SC050": "Bàn làm việc của nhóm điều tra X-Economics với tập hồ sơ da thuộc, bút máy và màn hình phân tích chuỗi cung ứng vĩ mô.",
    "CH02_SC051": "Thẻ tri ân người đăng ký kênh X-Economics chế tác bằng vàng champagne dập nổi trên nền đá phiến tối, ánh sáng vàng ấm.",
    "CH02_SC052": "Pháo đài đá uy nghiêm sừng sững trên đỉnh núi sương mù lúc bình minh, ánh nắng vàng ban mai xuyên qua mây đen thung lũng.",
    "CH02_SC053": "Bên trong phòng thí nghiệm động cơ tại Nhật Bản, khối động cơ hybrid và bộ truyền động hành tinh sáng bóng dưới đèn rọi.",
    "CH02_SC054": "Hành lang kho tiền kiên cố với các két sắt thép đen và sổ cái kiểm toán của tập đoàn tài chính Nhật Bản dưới ánh đèn bảo an vàng ấm.",
    "CH02_SC055": "Chủ tịch Akio Toyoda đứng đĩnh đạc bên chiếc xe hybrid sang trọng trong phòng họp lớn tại Nagoya, phong thái bất khả chiến bại."
}

rows_ch02 = []
for s in ch02_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descs_ch02.get(sid, "Bối cảnh công nghiệp thực tế đời thường.")
    overlay = text_overlays_ch02.get(sid, "Không")
    stream = "I2V" if (sid == "CH02_SC055") else "T2V"
    rows_ch02.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

visual_content = visual_header + "\n".join(rows_ch02) + "\n"
out_visual.write_text(visual_content, encoding="utf-8")
print(f"Generated {len(rows_ch02)} table rows in {out_visual.name}")
