from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_prompts = ep_dir / "prompts_chapter_03.txt"
out_visual = ep_dir / "chapter_03_visual.md"

STYLE = "A 2D warm cinematic editorial illustration in high-prestige corporate noir luxury aesthetic. Polished imperial slate tones (#1A202C), rich dark walnut wood (#1C1917), and brushed titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH03_SC001
add_scene(
    f"{STYLE}. An aerial twilight view over Nagoya Japan. The modern industrial metropolis stretches toward the darkened mountains under a deep blue-grey evening sky, warm amber streetlights and automotive logistics arteries glowing softly across the city.",
    "Slow smooth cinematic tracking shot gliding over the illuminated skyline of Nagoya at dusk, warm city lights reflecting on the river"
)

# CH03_SC002
add_scene(
    f"{STYLE}. A collection of prominent Western financial business magazines and newspapers neatly arranged on a dark mahogany credenza. Bold headlines and opinion editorials criticizing conservative corporate strategy in crisp typography beside a warm brass reading lamp.",
    "Slow camera push-in dolly shot toward the international financial headlines on the dark wooden credenza"
)

# CH03_SC003
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and round eyeglasses directly from the reference photo. The subject stands tall in an executive conference room in Nagoya wearing a tailored dark suit, exuding quiet, immovable corporate authority in luminous warm directional light.",
    "Steady camera shot focusing on the subject with a subtle slow push-in, maintaining their composed facial expression and all details of the reference image exactly"
)

# CH03_SC004
add_scene(
    f"{STYLE}. Wall Street trading floor illuminated by bright cyan and white LED displays. Crowds of financial traders in crisp shirts conferring excitedly around glowing speculative equity charts during the electric vehicle market boom.",
    "Slow tracking shot through the bustling trading floor, dynamic light reflections shimmering on computer monitors"
)

# CH03_SC005
add_scene(
    f"{STYLE}. A towering digital stock valuation comparison displayed on an immense electronic billboard in lower Manhattan. An astronomical market capitalization bar towering over traditional automakers in bright neon green against a deep slate midnight sky.",
    "Slow upward tilt shot from the street level toward the towering financial valuation display, vibrant market figures glowing"
)

# CH03_SC006
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and round eyeglasses directly from the reference photo. The subject is seated at the head of a dark walnut boardroom table in Nagoya, listening thoughtfully with folded hands, unswayed by outside market frenzy in warm directional lighting.",
    "Slow camera push-in dolly shot toward the subject, maintaining their calm, resolute facial expression and all details of the reference image exactly"
)

# CH03_SC007
add_scene(
    f"{STYLE}. An advanced engineering boardroom in Japan. An executive automotive blueprint displaying a multi-pathway powertrain portfolio, incorporating hybrid, hydrogen, and clean combustion technology alongside electric concepts, laid out on a dark slate surface.",
    "Slow smooth camera pan across the diversified powertrain blueprints on the boardroom table, warm brass lamplight accentuating fine lines"
)

# CH03_SC008
add_scene(
    f"{STYLE}. An official international automotive summit stage in Tokyo. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BEV GLOBAL SHARE PROJECTION: MAX 30%'. A minimalist Japanese stage with warm indirect architectural lighting.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC009
add_scene(
    f"{STYLE}. Inside a state-of-the-art hybrid engine engineering center in Japan. Robotic arms and master technicians assemble high-efficiency hybrid planetary transaxles under warm overhead inspection spotlights in a clean, sophisticated facility.",
    "Slow tracking shot moving parallel with the hybrid engine assembly line, precision metal components reflecting warm golden highlights"
)

# CH03_SC010
add_scene(
    f"{STYLE}. An international investor briefing room in London. Western fund managers in bespoke navy suits raising critical hands during an aggressive shareholder question-and-answer session beneath modern recessed downlights.",
    "Slow tracking shot across the skeptical investor audience, capturing intense analytical scrutiny in warm executive shadows"
)

# CH03_SC011
add_scene(
    f"{STYLE}. A solemn corporate boardroom in Wolfsburg Germany at twilight. Stacks of unread quarterly financial earnings sheets and red deficit warnings scattered across a dark conference table, capturing the toll of hasty strategic bets.",
    "Slow camera pull-back dolly shot revealing the quiet, darkened boardroom overlooking a rainy industrial courtyard"
)

# CH03_SC012
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and round eyeglasses directly from the reference photo. The subject gazes out through floor-to-ceiling glass of a high-rise office overlooking Nagoya at dusk, a subtle, knowing smile on his face, hands resting in pockets in warm golden-hour light.",
    "Slow camera push-in shot toward the subject from the side profile, maintaining their quiet, serene expression and all details of the reference image exactly"
)

# CH03_SC013
add_scene(
    f"{STYLE}. An executive leather-bound audited financial dossier stamped with gold leaf lettering resting on a polished dark mahogany table. Immaculate white financial ledger pages open to a certified balance sheet under a warm brass desk lamp.",
    "Slow camera push-in dolly shot toward the open audited balance sheet, warm golden light glinting on crisp financial columns"
)

# CH03_SC014
add_scene(
    f"{STYLE}. A massive world map engraved on a dark slate wall in Toyota global headquarters. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'GLOBAL ANNUAL SALES: 11,090,000 VEHICLES'. A glowing champagne gold tally illuminates the world number one position.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC015
add_scene(
    f"{STYLE}. A prestigious corporate trophy case in Nagoya displaying four consecutive annual global manufacturing championship awards. Polished crystal and brushed brass trophies gleaming under warm directional museum spotlights against dark cedar panels.",
    "Slow tracking shot gliding past the row of four golden automotive manufacturing awards, rich warm reflections throughout"
)

# CH03_SC016
add_scene(
    f"{STYLE}. A comparative industrial volume bar chart displayed on an executive monitor in Tokyo. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'VOLUME LEAD OVER BYD: +6,500,000 CARS'. A towering golden bar dwarfs the competitor volume.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC017
add_scene(
    f"{STYLE}. An executive boardroom presentation slide in Nagoya. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'ANNUAL REVENUE: $300,000,000,000+'. A golden highlighted milestone on dark slate beneath warm architectural spotlights.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC018
add_scene(
    f"{STYLE}. Close-up macro view of the bottom line of an audited corporate balance sheet. Crisp black ink on textured cotton bond paper, an accountant pen poised above the historic net profit line item in warm tungsten illumination.",
    "Slow smooth camera push-in toward the net income line item, warm directional lighting highlighting the texture of the paper"
)

# CH03_SC019
add_scene(
    f"{STYLE}. The executive boardroom at Toyota headquarters in Nagoya. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'RECORD NET PROFIT: $34,500,000,000'. Golden financial figures glow brightly upon a dark walnut presentation wall.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC020
add_scene(
    f"{STYLE}. A clean historical profit trajectory chart rendered in polished champagne gold on dark slate. The profit line surges upward by over one hundred percent in a single fiscal year, illuminated by a warm focused gallery spotlight.",
    "Slow camera push-in shot tracking the steep upward golden curve of operating profit, clean mathematical elegance"
)

# CH03_SC021
add_scene(
    f"{STYLE}. An expansive aerial view of the financial district of Frankfurt and European automotive headquarters. Towering glass banking skyscrapers bathed in cool evening mist, contrasted with warm golden office windows in deep slate surroundings.",
    "Slow cinematic crane shot descending slowly toward the Frankfurt financial skyline as twilight deepens into dark blue"
)

# CH03_SC022
add_scene(
    f"{STYLE}. A macro comparative economic bar chart etched in brushed brass. A single solid gold bar for Toyota net profit visibly surpasses the combined height of all European automotive competitor bars. Warm ambient lighting.",
    "Slow camera orbital shot around the comparative brass financial chart, warm highlights glinting along the polished edges"
)

# CH03_SC023
add_scene(
    f"{STYLE}. A financial analyst desk in Tokyo comparing annual financial reports. Two leather-bound audit dossiers lying side by side on a polished mahogany surface under a warm banker lamp, one bearing Toyota crest and the other BYD logo.",
    "Slow camera push-in dolly shot toward the two contrasting corporate annual reports on the wooden desk"
)

# CH03_SC024
add_scene(
    f"{STYLE}. An executive boardroom presentation slide. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TOYOTA NET PROFIT: 8X BYD'. A comparative graphic in champagne gold and dark slate under warm downlights.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC025
add_scene(
    f"{STYLE}. A high-angle view looking down at a brand-new hybrid vehicle rolling slowly off a final factory conveyor onto a polished concrete floor. A technician in dark blue uniform stamps the final quality inspection certificate under warm directional inspection lights.",
    "Slow camera tracking shot following the vehicle as it exits the assembly hall into the distribution yard"
)

# CH03_SC026
add_scene(
    f"{STYLE}. An accountant cash ledger on a wooden desk. A fountain pen calculates unit economics for each vehicle delivered, with net cash margins highlighted in warm gold against dark slate paper.",
    "Slow push-in shot toward the handwritten unit margin calculations on the ledger, warm tungsten illumination"
)

# CH03_SC027
add_scene(
    f"{STYLE}. A bustling automotive retail district in Chengdu China. Competing dealership glass showrooms lined up along a crowded urban avenue, adorned with bright red discount banners and promotional price slash signage under evening streetlights.",
    "Slow tracking shot along the competitive dealership avenue, capturing the relentless commercial intensity of the domestic price war"
)

# CH03_SC028
add_scene(
    f"{STYLE}. A price tag on an electric compact sedan inside a Chinese dealership showroom displaying a sub-fifteen-thousand dollar sticker price. Young sales associates conferring urgently with cost calculators in bright modern surroundings.",
    "Slow camera push-in shot toward the aggressive promotional price display on the showroom vehicle windshield"
)

# CH03_SC029
add_scene(
    f"{STYLE}. An automotive financial accounting room in Shenzhen. Cost accountants reviewing razor-thin net margin projections on large digital spreadsheets under warm fluorescent ceiling fixtures.",
    "Slow tracking shot across the busy financial accounting desks, analysts highlighting modest net margin totals"
)

# CH03_SC030
add_scene(
    f"{STYLE}. An executive financial slide in Shenzhen. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BYD NET PROFIT PER CAR: ~$1,250'. A minimalist bar graphic in warm amber and slate grey.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC031
add_scene(
    f"{STYLE}. An engineering cutaway of a modern Toyota hybrid powertrain on an exhibition stand in Nagoya. The polished alloy internal combustion engine seamlessly integrated with twin electric motor-generators and an epicyclic planetary gearset, glowing with subtle golden light.",
    "Slow orbital shot around the immaculate hybrid transaxle mechanism, warm directional light highlighting precision engineering"
)

# CH03_SC032
add_scene(
    f"{STYLE}. A worldwide vehicle distribution infographic on dark slate. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'GLOBAL HYBRID MIX: >37%'. Golden percentage arcs highlight surging hybrid deliveries worldwide.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC033
add_scene(
    f"{STYLE}. A premier Toyota dealership showroom in Sydney Australia at sunset. Discerning middle-class buyers inspecting a sleek new Camry hybrid sedan, touching the premium leather steering wheel under warm showroom spotlights.",
    "Slow tracking shot gliding past the showroom glass, warm golden sunset light reflecting on the deep metallic vehicle paint"
)

# CH03_SC034
add_scene(
    f"{STYLE}. A modern suburban family loading luggage into the rear trunk of a pristine Corolla hybrid sedan outside a clean modern home. Warm afternoon sunlight illuminates the durable vehicle design and happy family expressions.",
    "Slow camera push-in shot toward the family and the vehicle, capturing enduring consumer confidence in proven mechanical reliability"
)

# CH03_SC035
add_scene(
    f"{STYLE}. A brand-new Toyota hybrid SUV driving off an authorized dealership ramp onto a public roadway, the dealership sales manager in a dark suit shaking hands warmly with the new owner in the background.",
    "Slow tracking shot following the vehicle as it enters traffic, dealership glass reflecting warm late-afternoon sun"
)

# CH03_SC036
add_scene(
    f"{STYLE}. An executive financial presentation slide in Nagoya. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TOYOTA NET PROFIT PER CAR: ~$3,500'. A towering golden bar indicator on dark slate.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC037
add_scene(
    f"{STYLE}. A side-by-side unit profit comparison chart on dark polished slate: A tall champagne gold pillar representing Toyota thirty-five hundred dollar profit per car standing beside a modest amber bar representing BYD twelve hundred and fifty dollar profit.",
    "Slow smooth push-in dolly shot toward the comparative profit pillars, warm directional lighting highlighting the threefold margin gap"
)

# CH03_SC038
add_scene(
    f"{STYLE}. The heavy steel door of a sovereign corporate bank vault in Tokyo slowly swinging open, revealing safe deposit lockers and certified sovereign bond portfolios bathed in warm amber security lighting.",
    "Slow camera push-in dolly shot through the open bank vault doorway, metallic vault gears reflecting warm golden light"
)

# CH03_SC039
add_scene(
    f"{STYLE}. An executive financial fortress slide in Nagoya. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CASH WAR CHEST: $60,000,000,000+'. An impenetrable armored balance sheet graphic in dark slate and champagne gold.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC040
add_scene(
    f"{STYLE}. A conceptual artistic visual of an armored corporate citadel with thick polished stone walls withstanding stormy turbulent ocean waves at night. Golden beacon light from the fortress tower pierces the darkness, conveying absolute financial resilience.",
    "Slow cinematic crane shot rising above the stone citadel ramparts, warm golden beacon shining through the coastal storm"
)

# CH03_SC041
add_scene(
    f"{STYLE}. An archival photo wall in Nagoya documenting six decades of global dealership expansion. Historic photographs of Toyota service centers opening across Africa, Southeast Asia, South America, and Europe from nineteen-sixty to present.",
    "Slow tracking shot along the gallery of historical dealership opening photographs in rich warm sepia and amber tones"
)

# CH03_SC042
add_scene(
    f"{STYLE}. An expansive global network map displayed on dark wood panels. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'GLOBAL FOOTPRINT: 170+ COUNTRIES'. Glowing golden nodal points illuminate over ten thousand authorized dealer service bays worldwide.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC043
add_scene(
    f"{STYLE}. An authentic desert landscape in the Sahara at golden hour sunset. A dusty, rugged white Toyota Land Cruiser carrying supplies driving steadily across sweeping red-gold sand dunes, kicking up a dramatic dust trail in warm sunlight.",
    "Slow cinematic aerial tracking shot following the rugged Land Cruiser navigating the vast desert dunes, majestic adventurous scale"
)

# CH03_SC044
add_scene(
    f"{STYLE}. A dense tropical rainforest road in the Amazon basin during a downpour. A durable Toyota Hilux pickup navigating a muddy unpaved trail with effortless mechanical traction, heavy rain beating down on its rugged cab under dense canopy shadows.",
    "Low-angle tracking shot moving with the Hilux wheels churning through muddy terrain, authentic rugged durability"
)

# CH03_SC045
add_scene(
    f"{STYLE}. An expansive automotive parts warehouse in Toyota City Japan. Immense automated shelving systems rising to the ceiling holding millions of certified OEM spare parts, illuminated by warm high-bay sodium lamps.",
    "Slow crane shot gliding down the towering warehouse aisles between endless rows of precision replacement parts"
)

# CH03_SC046
add_scene(
    f"{STYLE}. An architectural stone wall of an ancient fortress at dusk. A subtle, hairline diagonal crack slowly appearing in the mortar, illuminated by a sharp raking beam of warm amber light, foreshadowing hidden structural strain.",
    "Slow macro push-in shot toward the fine hairline fracture in the stone surface, dramatic high-contrast low-key lighting"
)

# CH03_SC047
add_scene(
    f"{STYLE}. The sprawling North American headquarters campus of Toyota in Plano Texas at dusk. Sleek modern glass-and-limestone corporate buildings reflected in a quiet landscaped pond under an expansive Texas twilight sky.",
    "Slow tracking shot across the illuminated headquarters campus grounds, warm lights glowing behind architectural glass"
)

# CH03_SC048
add_scene(
    f"{STYLE}. An executive regional earnings slide in Texas. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'NORTH AMERICA OPERATING PROFIT: -78.5%'. A stark warning red down-arrow across quarterly regional figures.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH03_SC049
add_scene(
    f"{STYLE}. An automotive service bay in an American dealership. Technicians performing warranty inspections on vehicles, surrounded by warranty claim paperwork stamped with rising dealer compensation costs under warm workshop lighting.",
    "Slow tracking shot through the busy service bay, tools clinking as technicians inspect engine bays under warm work lights"
)

# CH03_SC050
add_scene(
    f"{STYLE}. An authentic middle-class family in a suburban neighborhood of an emerging market looking through the window of a luxury hybrid SUV at a dealership. The sixty-thousand-dollar sticker price is clearly beyond their household budget.",
    "Slow push-in shot toward the family, capturing a thoughtful, resigned expression as they turn toward more affordable alternatives"
)

# CH03_SC051
add_scene(
    f"{STYLE}. A busy emerging market intersection at dusk. Long lines of older vehicles waiting at a traffic light while sleek modern affordable electric vehicles quietly glide past them into adjacent lanes, marking a shifting competitive frontier.",
    "Slow panning shot across the dusk traffic, capturing the contrast between legacy combustion cars and agile new competitors"
)

# CH03_SC052
add_scene(
    f"{STYLE}. A low-angle view of a modern automotive corporate tower in Nagoya at night. Sleek glass architecture illuminated from within, standing resolute and unyielding against dark night clouds.",
    "Slow upward tilt shot toward the illuminated glass tower, capturing an impression of monumental industrial endurance"
)

# CH03_SC053
add_scene(
    f"{STYLE}. An immaculate Toyota manufacturing assembly floor in Japan operating under the Kanban lean manufacturing protocol. Perfectly synchronized conveyor carts, clean white floor lines, and workers performing standardized tasks with surgical precision.",
    "Slow tracking shot gliding along the pristine lean assembly line, harmonious mechanical rhythm and immaculate cleanliness"
)

# CH03_SC054
add_scene(
    f"{STYLE}. An executive boardroom in Nagoya overlooking the factory grounds. A massive mahogany conference table surrounded by leather chairs, with charts displaying eleven million vehicles delivered and thirty-four billion dollars banked.",
    "Slow camera push-in dolly shot toward the head of the boardroom table, warm golden light casting long shadows across the wood"
)

# CH03_SC055
add_scene(
    f"{STYLE}. A macro view of an intricate industrial chessboard made of polished dark walnut and brushed titanium. A heavy golden king piece representing Toyota stands securely at the center of the board, surrounded by defensive fortresses.",
    "Slow orbital shot around the golden king chess piece, warm lighting highlighting the heavy metallic crown"
)

# CH03_SC056
add_scene(
    f"{STYLE}. An aerial satellite view of the Pacific Ocean at dusk. Golden shipping lanes trace paths from Asia toward Latin America, Africa, and Southeast Asia, deliberately bypassing the North American landmass.",
    "Slow high-angle tracking shot gliding over the illuminated oceanic routes bypassing the darkened silhouette of North America"
)

# CH03_SC057
add_scene(
    f"{STYLE}. A high-tech materials engineering laboratory in Shenzhen China. Advanced robotic laser cutting machines slicing high-strength steel chassis panels with surgical precision, orange sparks showering in deep slate shadows.",
    "Slow tracking shot moving close to the laser cutting gantry, bright sparks creating dramatic warm contrast against dark machinery"
)

# CH03_SC058
add_scene(
    f"{STYLE}. An economics research amphitheater at a top university. A senior industrial economist lecturing before a large chalkboard covered in complex cost integration formulas and supply chain equations under warm lecture hall downlights.",
    "Slow camera push-in dolly shot toward the chalkboard formulas, capturing rigorous academic inquiry into unconventional cost physics"
)

# CH03_SC059
add_scene(
    f"{STYLE}. A sterile engineering teardown workshop. An electric vehicle stripped down to its bare metal monocoque chassis, with hundreds of subcomponents, wire harnesses, and structural stampings neatly arranged on white grids on the floor.",
    "Slow high-angle crane shot descending over the meticulously disassembled vehicle components, clinical forensic precision"
)

# CH03_SC060
add_scene(
    f"{STYLE}. The exterior of a premier Swiss technical engineering laboratory in Zurich at dusk. Sleek glass-and-granite architecture reflecting twilight skies, interior test bays glowing with warm precision inspection lighting.",
    "Slow tracking shot along the facade of the Swiss research institute toward the illuminated engineering bay windows"
)

# CH03_SC061
add_scene(
    f"{STYLE}. Inside the Swiss laboratory, senior automotive teardown engineers in clean white lab coats systematically unscrewing fasteners from an exposed BYD Seal battery pack. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'SWISS UBS TEARDOWN LAB: BYD SEAL'. Clinical warm lighting.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# Write prompts file
content_prompts = "\n\n".join(prompts) + "\n"
out_prompts.write_text(content_prompts, encoding="utf-8")
print(f"Successfully generated {len(prompts)} scenes in {out_prompts.name}")

# Now generate chapter_03_visual.md
with open(ep_dir / "scene_timing_map.json", "r", encoding="utf-8") as f:
    all_scenes = json.load(f)

ch03_scenes = [s for s in all_scenes if s.get("chapter") == "03"]

visual_header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_03_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_03.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_03.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-12 22:50
-->

# Chapter 03 Visual Script — The Thirty-Four Billion Dollar Fortress

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 3 (The Thirty-Four Billion Dollar Fortress), đồng bộ toán học 1-1 với 61 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_03.txt`.

- **Vũ trụ Mỹ thuật:** Supreme Corporate Fortress & Unmatched Capital Discipline.
- **Bảng màu Sâu lắng & Sang trọng:** Polished Imperial Slate (`#1A202C`), Rich Dark Walnut (`#1C1917`), Brushed Titanium, Imperial Warm Champagne Gold (`#D4AF37`), Luminous Amber (`#F59E0B`), Warning Bordeaux (`#8B0000`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Directional Warm Tungsten Highlights, Velvety Deep Shadows, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~20% cảnh mấu chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :---: | :---: |
"""

text_overlays_ch03 = {
    "CH03_SC008": "BEV GLOBAL SHARE PROJECTION: MAX 30%",
    "CH03_SC014": "GLOBAL ANNUAL SALES: 11,090,000 VEHICLES",
    "CH03_SC016": "VOLUME LEAD OVER BYD: +6,500,000 CARS",
    "CH03_SC017": "ANNUAL REVENUE: $300,000,000,000+",
    "CH03_SC019": "RECORD NET PROFIT: $34,500,000,000",
    "CH03_SC024": "TOYOTA NET PROFIT: 8X BYD",
    "CH03_SC030": "BYD NET PROFIT PER CAR: ~$1,250",
    "CH03_SC032": "GLOBAL HYBRID MIX: >37%",
    "CH03_SC036": "TOYOTA NET PROFIT PER CAR: ~$3,500",
    "CH03_SC039": "CASH WAR CHEST: $60,000,000,000+",
    "CH03_SC042": "GLOBAL FOOTPRINT: 170+ COUNTRIES",
    "CH03_SC048": "NORTH AMERICA OPERATING PROFIT: -78.5%",
    "CH03_SC061": "SWISS UBS TEARDOWN LAB: BYD SEAL",
}

visual_descs_ch03 = {
    "CH03_SC001": "Toàn cảnh thành phố Nagoya lúc chập tối, dòng xe cộ nối đuôi qua các cây cầu cảng biển dưới ánh đèn vàng ấm áp.",
    "CH03_SC002": "Các tờ tạp chí kinh tế tài chính phương Tây xếp ngay ngắn trên bàn gỗ sồi, dòng tít chỉ trích sự bảo thủ công nghiệp.",
    "CH03_SC003": "Chủ tịch Akio Toyoda đứng đĩnh đạc trong phòng họp Nagoya, vest tối màu trang trọng, ánh mắt điềm đạm, uy quyền tuyệt đối.",
    "CH03_SC004": "Sàn giao dịch Phố Wall sáng rực các màn hình chứng khoán, đám đông chuyên viên tài chính bàn luận sôi nổi quanh đồ thị xe điện.",
    "CH03_SC005": "Bảng điện tử khổng lồ tại Manhattan hiển thị giá trị vốn hóa của Tesla vượt qua tổng vốn hóa toàn bộ ngành công nghiệp ô tô cộng lại.",
    "CH03_SC006": "Chủ tịch Akio Toyoda ngồi trầm ngâm ở đầu bàn họp gỗ óc chó lớn tại Nagoya, kiên định với tầm nhìn ngược dòng nước.",
    "CH03_SC007": "Bản vẽ thiết kế chiến lược đa lộ trình trên bàn làm việc: kết hợp xe lai hybrid, động cơ đốt trong cải tiến và pin thể rắn.",
    "CH03_SC008": "Hội nghị thượng đỉnh công nghiệp Tokyo, bục phát biểu tối giản công bố dự báo xe điện thuần túy không vượt quá 30% thị phần.",
    "CH03_SC009": "Phân xưởng sản xuất động cơ hybrid tiên tiến tại Nhật Bản, các cánh tay robot và kỹ sư tinh chỉnh bộ truyền động chính xác.",
    "CH03_SC010": "Khán phòng đại hội cổ đông tại London, các nhà đầu tư phương Tây giơ tay đặt câu hỏi gay gắt về lộ trình điện hóa.",
    "CH03_SC011": "Phòng họp hội đồng quản trị u buồn tại Wolfsburg lúc hoàng hôn, các tập báo cáo thua lỗ xe điện nằm ngổn ngang.",
    "CH03_SC012": "Chủ tịch Akio Toyoda đứng bên cửa sổ kính tầng cao nhìn xuống Nagoya lúc hoàng hôn, nụ cười kín đáo, thanh thản trước sóng gió.",
    "CH03_SC013": "Cuốn sổ cái kiểm toán đóng bìa da sang trọng in chữ mạ vàng, mở trang báo cáo tài chính được chứng thực dưới đèn bàn đồng.",
    "CH03_SC014": "Bản đồ thế giới khắc trên đá phiến tối trong trụ sở Toyota, con số kỷ lục 11,09 triệu xe bán ra toàn cầu phát sáng vàng kim.",
    "CH03_SC015": "Tủ kính lưu niệm tại Nagoya trưng bày bốn chiếc cúp vàng vô địch sản lượng ô tô thế giới bốn năm liên tiếp sáng rực.",
    "CH03_SC016": "Biểu đồ so sánh sản lượng trên màn hình phòng họp, cột sản lượng Toyota cao hơn đối thủ BYD tới gần 6,5 triệu chiếc xe.",
    "CH03_SC017": "Màn hình thuyết trình tài chính tại Nagoya hiển thị cột mốc doanh thu kỷ lục vượt 300 tỷ USD sáng rực sắc vàng champagne.",
    "CH03_SC018": "Cận cảnh dòng đáy của bảng cân đối kế toán, ngòi bút mực vàng đặt trên con số lợi nhuận ròng dưới ánh đèn rọi ấm áp.",
    "CH03_SC019": "Phòng họp hội đồng quản trị Nagoya hiển thị con số lợi nhuận ròng kỷ lục lịch sử 34,5 tỷ USD trên tường gỗ óc chó sẫm màu.",
    "CH03_SC020": "Đồ thị đường cong lợi nhuận ròng tăng vọt hơn 100% chỉ sau một năm tài khóa được khắc bằng đường viền vàng nổi khối.",
    "CH03_SC021": "Toàn cảnh các tòa tháp ngân hàng trung tâm tài chính Frankfurt nước Đức trong sương chiều, đối chiếu quy mô lợi nhuận.",
    "CH03_SC022": "Biểu đồ cột kim loại mạ vàng chứng minh lợi nhuận Toyota lớn hơn tổng lợi nhuận toàn bộ các hãng ô tô châu Âu gộp lại.",
    "CH03_SC023": "Bàn làm việc của chuyên gia tài chính đối chiếu hai cuốn báo cáo tài chính của Toyota và BYD dưới đèn bàn ấm áp.",
    "CH03_SC024": "Biểu đồ so sánh lợi nhuận ròng hiển thị Toyota gấp hơn 8 lần tổng lợi nhuận ròng 4,16 tỷ USD của tập đoàn BYD.",
    "CH03_SC025": "Góc nhìn từ trên cao xuống chiếc xe hybrid mới tinh lăn bánh khỏi dây chuyền sản xuất, kỹ sư đóng dấu kiểm định chất lượng xuất xưởng.",
    "CH03_SC026": "Bảng tính chi phí đơn vị trên bàn làm việc, ngòi bút tính toán dòng tiền lãi thu về trên từng chiếc xe lăn bánh khỏi đại lý.",
    "CH03_SC027": "Khu phố đại lý ô tô sầm uất tại Thành Đô Trung Quốc với hàng loạt băng rôn đỏ hạ giá xe rực rỡ dưới ánh đèn đường ban đêm.",
    "CH03_SC028": "Tem giá trên kính chắn gió chiếc sedan điện tại đại lý Trung Quốc hạ xuống dưới 15.000 USD, nhân viên tính toán căng thẳng.",
    "CH03_SC029": "Phòng kế toán chi phí tại Thâm Quyến, các kiểm toán viên rà soát biên lợi nhuận ròng mỏng manh trên từng mẫu xe bán ra.",
    "CH03_SC030": "Màn hình tài chính hiển thị mức lợi nhuận ròng ước tính chỉ vỏn vẹn khoảng 1.250 USD trên mỗi chiếc xe bán ra của BYD.",
    "CH03_SC031": "Mô hình cắt bổ động cơ hybrid của Toyota trên bục trưng bày tại Nagoya, các bánh răng hành tinh và mô-tơ phát sáng ánh vàng.",
    "CH03_SC032": "Đồ thị tỷ trọng xe hybrid toàn cầu chiếm hơn 37% tổng sản lượng của Toyota, các đường cong sắc vàng nổi bật trên nền slate.",
    "CH03_SC033": "Showroom Toyota sang trọng tại Sydney Úc lúc hoàng hôn, khách hàng trung lưu ưng ý ngắm nhìn chiếc Camry hybrid bền bỉ.",
    "CH03_SC034": "Gia đình hiện đại dỡ đồ đạc từ cốp chiếc Corolla hybrid đỗ trước hiên nhà trong nắng chiều ấm áp, niềm tin vào sự bền bỉ.",
    "CH03_SC035": "Chiếc xe hybrid mới tinh lăn bánh rời khỏi dốc đại lý ra đường lớn, giám đốc bán hàng bắt tay khách hàng hài lòng.",
    "CH03_SC036": "Màn hình thuyết trình tài chính tại Nagoya hiển thị mức lợi nhuận ròng trung bình 3.500 USD trên mỗi chiếc xe bán ra của Toyota.",
    "CH03_SC037": "Biểu đồ cột so sánh trực quan mức lợi nhuận 3.500 USD của Toyota cao gấp gần ba lần mức 1.250 USD của đối thủ cạnh tranh.",
    "CH03_SC038": "Cánh cửa thép nặng của kho tiền ngân hàng tại Tokyo mở ra, bên trong là các ngăn an toàn chứa danh mục đầu tư tài chính.",
    "CH03_SC039": "Màn hình hiển thị pháo đài tài chính với kho dự trữ tiền mặt và đầu tư ngắn hạn vượt 60 tỷ USD trên nền đá phiến tối.",
    "CH03_SC040": "Hình tượng nghệ thuật pháo đài đá kiên cố sừng sững bên bờ biển chống chọi những đợt sóng bão lớn, ngọn hải đăng vàng rọi sáng.",
    "CH03_SC041": "Bức tường ảnh lưu niệm tại Nagoya ghi dấu 60 năm xây dựng mạng lưới đại lý phủ khắp các châu lục từ thập niên 1960.",
    "CH03_SC042": "Bản đồ mạng lưới đại lý toàn cầu hiển thị các chấm vàng kết nối hơn 170 quốc gia với hơn mười ngàn xưởng dịch vụ ủy quyền.",
    "CH03_SC043": "Sa mạc Sahara lúc hoàng hôn, chiếc Toyota Land Cruiser trắng dũng mãnh băng qua những cồn cát đỏ rực, bụi cát bay cuốn theo gió.",
    "CH03_SC044": "Rừng rậm nhiệt đới Amazon dưới cơn mưa như trút nước, chiếc bán tải Hilux vượt qua đoạn đường bùn lầy lội đầy vững chãi.",
    "CH03_SC045": "Kho phụ tùng khổng lồ tại Toyota City Nhật Bản với hệ thống giá kệ tự động cao ngút tầm mắt chứa hàng triệu linh kiện chính hãng.",
    "CH03_SC046": "Bức tường đá của pháo đài lúc chập tối xuất hiện một vết rạn nứt nhỏ mảnh như sợi tóc dưới tia sáng rọi nghiêng màu hổ phách.",
    "CH03_SC047": "Khuôn viên trụ sở Toyota Bắc Mỹ tại Plano Texas lúc hoàng hôn, các tòa nhà kính hiện đại soi bóng xuống hồ nước tĩnh lặng.",
    "CH03_SC048": "Màn hình kết quả kinh doanh khu vực Bắc Mỹ hiển thị lợi nhuận hoạt động quý sụt giảm kinh hoàng 78,5% với mũi tên đỏ cảnh báo.",
    "CH03_SC049": "Xưởng dịch vụ đại lý tại Mỹ, các kỹ sư kiểm tra bảo hành xe bên cạnh chồng hồ sơ chi phí khuyến mại và bảo hành tăng vọt.",
    "CH03_SC050": "Gia đình người dân tại thị trường đang phát triển đứng nhìn chiếc SUV hybrid đắt đỏ trong showroom với vẻ mặt đăm chiêu.",
    "CH03_SC051": "Ngã tư đường phố thị trường mới nổi lúc chập tối, dòng xe cũ kiên nhẫn nhích từng mét trong khi các mẫu xe điện giá rẻ lướt qua.",
    "CH03_SC052": "Tòa tháp hành chính Toyota tại Nagoya ban đêm, kiến trúc kính thép sáng rực ánh đèn, toát lên sự kiên cường của một đế chế.",
    "CH03_SC053": "Phân xưởng lắp ráp tinh gọn Kanban tại Nhật Bản, công nhân thao tác nhịp nhàng, chính xác tuyệt đối trên sàn nhà máy sạch bong.",
    "CH03_SC054": "Bàn họp hội đồng quản trị lớn tại Nagoya nhìn ra toàn cảnh nhà máy, các bản số liệu 11 triệu xe và 34 tỷ USD lợi nhuận mở rộng.",
    "CH03_SC055": "Bàn cờ thế công nghiệp bằng gỗ óc chó và titan, quân vua vàng Toyota đứng vững vàng ở trung tâm được bao bọc bởi các pháo đài.",
    "CH03_SC056": "Góc nhìn vệ tinh Thái Bình Dương lúc chập tối, các tuyến đường biển thương mại rẽ nhánh đi Nam Mỹ và Đông Nam Á tránh nước Mỹ.",
    "CH03_SC057": "Xưởng cơ khí công nghệ cao tại Thâm Quyến, máy cắt laser tự động cắt các tấm thép dập khung xe với độ chính xác cao.",
    "CH03_SC058": "Giảng đường kinh tế học quốc tế, giáo sư phân tích các phương trình chi phí cơ học và vật lý công nghiệp trên bảng đen lớn.",
    "CH03_SC059": "Xưởng mổ xẻ kỹ thuật vô trùng, chiếc xe điện được tháo dỡ thành hàng ngàn chi tiết cơ học và bảng mạch sắp ngay ngắn trên sàn.",
    "CH03_SC060": "Mặt tiền viện nghiên cứu kỹ thuật Thụy Sĩ tại Zurich trong sương chiều, ánh đèn kiểm toán rọi sáng qua khung cửa kính phòng lab.",
    "CH03_SC061": "Bên trong phòng lab Thụy Sĩ, các kỹ sư UBS tháo dỡ khối pin Blade của chiếc BYD Seal dưới ánh đèn mổ xẻ rọi từ trên cao."
}

rows_ch03 = []
for s in ch03_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descs_ch03.get(sid, "Bối cảnh công nghiệp thực tế đời thường.")
    overlay = text_overlays_ch03.get(sid, "Không")
    stream = "I2V" if (sid in ["CH03_SC003", "CH03_SC006", "CH03_SC012"]) else "T2V"
    rows_ch03.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

visual_content = visual_header + "\n".join(rows_ch03) + "\n"
out_visual.write_text(visual_content, encoding="utf-8")
print(f"Generated {len(rows_ch03)} table rows in {out_visual.name}")
