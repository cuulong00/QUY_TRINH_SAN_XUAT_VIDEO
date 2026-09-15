from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_prompts = ep_dir / "prompts_chapter_08.txt"
out_visual = ep_dir / "chapter_08_visual.md"

STYLE = "A 2D warm cinematic editorial illustration in high-prestige corporate noir and urban documentary aesthetic. Rainy midnight asphalt tones (#12151B), deep Bangkok indigo slate (#151B24), and polished wet chrome textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH08_SC001
add_scene(
    f"{STYLE}. An expansive panoramic perspective of a major multi-lane urban intersection in central Bangkok at dusk during a heavy tropical downpour. Wet asphalt mirrors vibrant amber streetlights, glowing red traffic signals, and neon commercial signage under a deep twilight sky. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BANGKOK, THAILAND: THE EPICENTER'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC002
add_scene(
    f"{STYLE}. Dense evening rush hour traffic in Bangkok under relentless tropical rain. Sheets of water stream down windshields, glowing taillights stretch into the distance, and overhead expressways cast deep moody shadows across the wet roadways.",
    "Slow cinematic tracking shot gliding through the rain-soaked urban congestion as headlights blur into warm bokeh"
)

# CH08_SC003
add_scene(
    f"{STYLE}. A weathered, sturdy charcoal-grey Toyota Hilux pickup truck inching forward in the center lane. Wet water droplets bead across its robust steel hood, the tough metallic silhouette cutting through the downpour with resolute mechanical endurance.",
    "Slow tracking shot moving parallel to the sturdy Hilux pickup as it moves forward through the heavy rain"
)

# CH08_SC004
add_scene(
    f"{STYLE}. Close-up of the rugged Toyota Hilux body panels. Authentic work-site red dust caked along the wheel arches and lower door sills, contrasted against gleaming rivulets of rainwater washing over the tough steel under warm streetlamps.",
    "Slow macro camera pan along the weathered, mud-dusted steel body panels of the dependable utility truck"
)

# CH08_SC005
add_scene(
    f"{STYLE}. The front grille and vibrating steel hood of the Toyota Hilux. The legendary diesel engine purrs steadily underneath, emitting a rhythmic, reassuring hum under warm amber headlights piercing the tropical gloom.",
    "Slow camera push-in shot toward the iconic front emblem and idling diesel engine vibrating in steady mechanical harmony"
)

# CH08_SC006
add_scene(
    f"{STYLE}. Pulling back slightly to reveal the adjacent lane: pulling up alongside the Hilux is a pristine, brand-new dark obsidian BYD Shark super hybrid pickup truck. Its ultra-modern aerodynamic silhouette gleams with deep wet reflections.",
    "Slow tracking shot gliding sideways between the two trucks as the sleek modern hybrid comes to a halt"
)

# CH08_SC007
add_scene(
    f"{STYLE}. A dramatic low-angle shot of the modern hybrid pickup. Its continuous horizontal full-width LED ambient light bar cuts sharply through the falling rain with a cool luminous glow, water streaming smoothly over sleek sculpted composite body panels.",
    "Slow upward tilt from the wet asphalt toward the glowing full-width LED light bar piercing the rain"
)

# CH08_SC008
add_scene(
    f"{STYLE}. Looking through the rain-slicked side glass into the high-tech digital cockpit of the modern hybrid pickup. A large rotating central touchscreen illuminates the driver in soft amber and ivory light as the truck rolls to a stop in eerie electric silence.",
    "Slow camera push-in shot toward the glowing digital cabin interior through the streaming rain on the side window"
)

# CH08_SC009
add_scene(
    f"{STYLE}. A dramatic frontal symmetrical composition of the two pickup trucks idling side by side at a red traffic signal. On the left sits the rugged, dusty diesel Hilux; on the right sits the sleek, illuminated hybrid Shark. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'PARALLEL WORLDS: MECHANICAL VS DIGITAL'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC010
add_scene(
    f"{STYLE}. A symbolic close-up capturing the narrow strip of wet asphalt between the two vehicles. Rainwater cascades down the gap, reflecting the glowing red overhead stoplight on dark pavement, separating two irreconcilable industrial eras.",
    "Slow low-angle tracking shot gliding along the rain-slicked asphalt divide between the two idling vehicles"
)

# CH08_SC011
add_scene(
    f"{STYLE}. A focused visual tribute to twentieth-century mechanical engineering: a precision cross-section of a durable cast-iron diesel engine block with forged pistons and timing gears, gleaming under warm golden industrial museum lighting.",
    "Slow camera push-in dolly shot toward the precision forged mechanical components of the classic diesel engine"
)

# CH08_SC012
add_scene(
    f"{STYLE}. A contrasting visual tribute to twenty-first-century software and battery architecture: a sleek integrated electric powertrain skateboard chassis with prismatic battery cells and smart computing motherboards glowing in luminous amber.",
    "Slow camera tracking shot gliding over the illuminated solid-state and smart computing automotive skateboard architecture"
)

# CH08_SC013
add_scene(
    f"@evp_byd_stellali.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The senior executive in a tailored dark corporate suit sits in a prestigious international conference studio, delivering a decisive strategic interview with composed authority in warm directional lighting.",
    "Steady camera shot focusing on the executive delivering her strategic statement, maintaining all details of the reference image exactly"
)

# CH08_SC014
add_scene(
    f"{STYLE}. An international news broadcast control room at dusk. Editorial screens replay the televised press announcement from early twenty twenty-four. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'STELLA LI: \"WE ARE NOT COMING TO THE US\"'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC015
add_scene(
    f"{STYLE}. A Western financial media newsroom in New York or London. Journalists and market commentators gather around monitors analyzing automotive trade headlines under cool overhead office lighting.",
    "Slow tracking shot across the busy financial newsroom as analysts debate global automotive headlines"
)

# CH08_SC016
add_scene(
    f"{STYLE}. A financial newspaper front page laid out on a dark polished desk. Opinion columns and editorial commentary interpret the Chinese automaker's statement as a defensive retreat from North America.",
    "Slow camera push-in dolly shot toward the printed financial newspaper resting beside a pair of reading glasses"
)

# CH08_SC017
add_scene(
    f"{STYLE}. A symbolic industrial border checkpoint along the American frontier. A monumental steel barrier wall stands tall beneath a storm-swept sky, marked with official tariff decrees. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'WESTERN TARIFF WALL: 100% IMPORT DUTY'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC018
add_scene(
    f"{STYLE}. A high-level geoeconomic strategy chamber at night. Senior macroeconomic analysts examine a massive illuminated world globe where trade flow arrows bypass North America and surge directly into the Global South.",
    "Slow camera push-in dolly shot toward the illuminated globe revealing the southward pivot of international trade"
)

# CH08_SC019
add_scene(
    f"{STYLE}. A majestic shipping lane at dusk. An enormous specialized vehicle carrier vessel glides purposefully across open ocean waters toward Latin America and Southeast Asia, silhouetted against a brilliant amber and crimson horizon.",
    "Slow cinematic crane shot tracking alongside the massive vehicle carrier vessel navigating open global waters"
)

# CH08_SC020
add_scene(
    f"{STYLE}. A global macroeconomic visualization on dark architectural slate. A monumental golden ring representing the four-trillion-dollar global automotive market fracturing into two distinct tectonic plates. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'GLOBAL AUTO MARKET: $4 TRILLION BIFURCATION'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC021
add_scene(
    f"{STYLE}. An abstract physical map of the world dividing into two parallel illuminated spheres on a dark glass table, one shaded in cool defensive blue and the other in vibrant expansive warm amber.",
    "Slow tracking shot gliding across the dark glass map illustrating the emerging two-sphere global economic architecture"
)

# CH08_SC022
add_scene(
    f"{STYLE}. An exclusive automotive dealership in suburban North America at dusk. Polished luxury SUVs and oversized trucks sit under bright glass showrooms behind tall ornamental wrought-iron fences.",
    "Slow camera push-in dolly shot toward the quiet, protected domestic dealership pavilion"
)

# CH08_SC023
add_scene(
    f"{STYLE}. A formal government trade commission hearing chamber in Washington. Officials in dark suits sit behind a raised mahogany dais, gavel resting on wood beneath the seal of trade protection.",
    "Slow cinematic tracking shot along the formal government trade dais under warm courtroom chandeliers"
)

# CH08_SC024
add_scene(
    f"{STYLE}. An executive boardroom of an American automaker in Detroit. Executives examine market share reports showing domestic dominance preserved at eighteen percent of global volume. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'INDUSTRIAL SANCTUARY: PROTECTING 18% SHARE'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC025
add_scene(
    f"{STYLE}. An American suburban driveway at dusk. An ordinary middle-class buyer reviews a retail vehicle purchase contract stamped with high monthly finance payments under a porch lamp.",
    "Slow camera push-in shot toward the finance agreement showing steep retail vehicle transaction prices"
)

# CH08_SC026
add_scene(
    f"{STYLE}. A dealership pricing window sticker on a modern American family vehicle. High retail figures highlighted in gold and crimson ink. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'AVERAGE US CAR PRICE: $47,870 USD'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC027
add_scene(
    f"{STYLE}. An everyday consumer looking out through an airport departure lounge window toward foreign city streets bustling with diverse, compact, affordable electric cars beyond the domestic border.",
    "Slow tracking shot moving past the traveler looking out toward the vibrant global vehicle landscape outside"
)

# CH08_SC028
add_scene(
    f"{STYLE}. An expansive geopolitical map highlighting Southeast Asia, Latin America, the Middle East, and Africa glowing in warm golden amber on dark wood. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'THE 82% WORLD: THE GLOBAL SOUTH ARENA'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC029
add_scene(
    f"{STYLE}. A bustling port terminal in South America where newly arrived Asian vehicles roll off transport ships into waiting transport corridors under bright tropical sunshine.",
    "Slow crane shot descending over the busy maritime vehicle processing terminal in a major developing market"
)

# CH08_SC030
add_scene(
    f"{STYLE}. An energetic metropolitan showroom in Sao Paulo or Jakarta. Young families and commercial fleet operators eagerly inspecting new hybrid and electric utility models under bright showroom spotlights.",
    "Slow tracking shot moving through the active showroom floor as prospective buyers examine vehicle interiors"
)

# CH08_SC031
add_scene(
    f"{STYLE}. A forensic cost-engineering breakdown displayed on a titanium plaque. An industrial metric reveals a thirty-five percent lower baseline manufacturing cost structure. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BYD ADVANTAGE: -35% COST / 75% INTEGRATION'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC032
add_scene(
    f"{STYLE}. A high-speed industrial assembly hall in China: vertically integrated production lines where stamped chassis, battery packs, and electric motors converge on unified automated overhead carriers under amber bay lights.",
    "Slow tracking shot gliding alongside the unified vertical manufacturing conveyor line"
)

# CH08_SC033
add_scene(
    f"{STYLE}. A stark economic balance visualization: on one side, an immense workforce payroll ledger representing nearly one million employees; on the other, a steep red graph representing secondary market vehicle depreciation.",
    "Slow camera push-in dolly shot toward the dual challenges of workforce scale and secondary market valuation"
)

# CH08_SC034
add_scene(
    f"{STYLE}. A panoramic view of the global headquarters of Toyota in Japan at sunrise. Golden morning light illuminates modern corporate towers and vast, immaculate manufacturing facilities humming with quiet precision.",
    "Slow majestic drone shot rising above the expansive Toyota manufacturing complex at dawn"
)

# CH08_SC035
add_scene(
    f"{STYLE}. A monumental corporate achievement monument engraved on dark slate. Global delivery statistics exceed eleven million vehicles annually alongside liquid cash reserves. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TOYOTA SCALE: 11.2M UNITS / $34B CASH FORTRESS'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC036
add_scene(
    f"{STYLE}. An executive technology vault displaying solid-state battery patents bound in gold leather beside advanced chemical prototypes glowing with subtle platinum-gold luminescence.",
    "Slow camera push-in dolly shot toward the solid-state patent folio and gleaming prototype cells on dark cedar"
)

# CH08_SC037
add_scene(
    f"{STYLE}. A cinematic standoff composition: the logos and emblems of the two titans positioned at opposite ends of a long dark polished conference table under dramatic directional lighting.",
    "Slow steady camera tracking shot down the center of the executive conference table between the two corporate emblems"
)

# CH08_SC038
add_scene(
    f"{STYLE}. An elegant documentary channel title card on dark brushed titanium with warm amber backlighting: 'X-ECONOMICS: INVESTIGATIVE MACRO & INDUSTRIAL STRATEGY', subtle subscribe button icon resting on dark slate.",
    "Slow camera push-in dolly shot toward the refined channel identity card illuminated in warm editorial tones"
)

# CH08_SC039
add_scene(
    f"{STYLE}. A high-angle view of a monumental concrete border tariff wall stretching across an arid landscape, long sunset shadows stretching toward the horizon under a brooding sky.",
    "Slow tracking shot gliding along the crest of the concrete industrial trade barrier at dusk"
)

# CH08_SC040
add_scene(
    f"{STYLE}. A conceptual physics visualization on a chalkboard in an industrial economics university. Mathematical equations of gravity and market scale pulling down protective trade walls. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'ECONOMIC GRAVITY: TARIFFS CANNOT STOP SCALE'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH08_SC041
add_scene(
    f"{STYLE}. Back at the Bangkok intersection at night. The overhead red traffic signal clicks and transitions to a vivid, luminous emerald green, reflecting sharply across the rain-slicked asphalt.",
    "Slow low-angle camera push-in toward the green traffic signal glowing brightly against the night rain"
)

# CH08_SC042
add_scene(
    f"{STYLE}. Side-by-side ground-level view of the two trucks as the light turns green. Both vehicles accelerate simultaneously, water spraying from wide rear tires onto the glistening street under amber streetlights.",
    "Slow tracking shot moving alongside both pickup trucks as they accelerate in tandem through the intersection"
)

# CH08_SC043
add_scene(
    f"{STYLE}. Interior view of the Toyota Hilux cab. A middle-aged Southeast Asian driver with steady, weathered hands on the worn leather steering wheel, glancing forward with calm, quiet trust as the diesel engine hums smoothly.",
    "Slow camera pan from the driver's calm expression to the dashboard odometer showing hundreds of thousands of dependable kilometers"
)

# CH08_SC044
add_scene(
    f"{STYLE}. The rear profile of the reliable diesel Hilux moving forward into the night, its red taillights glowing warm and steady as it navigates the rain-swept Bangkok avenue.",
    "Slow camera pull-back following the sturdy Hilux as it glides steadily into the urban rain"
)

# CH08_SC045
add_scene(
    f"{STYLE}. Interior view of the modern BYD Shark cab. A young Southeast Asian tech professional smiling gently, navigating smoothly via the glowing touchscreen in peaceful electric tranquility amidst the storm.",
    "Slow push-in shot toward the driver enjoying modern digital comfort and quiet electric propulsion in the dark cabin"
)

# CH08_SC046
add_scene(
    f"{STYLE}. A high-angle aerial view of the two vehicles driving forward side by side down the multi-lane Bangkok boulevard, their red taillights leaving twin trails of crimson reflection on the wet asphalt.",
    "Slow cinematic crane shot ascending as both trucks move together into the sprawling, illuminated city night"
)

# CH08_SC047
add_scene(
    f"{STYLE}. An expansive view of Bangkok at midnight from a high rooftop. Billions of city lights glittering through mist and rain, highways curling like glowing golden arteries across the urban landscape.",
    "Slow cinematic tracking shot drifting above the midnight skyline of the Southeast Asian metropolis"
)

# CH08_SC048
add_scene(
    f"{STYLE}. A breathtaking cinematic view of planet Earth from orbit at twilight. Continents illuminated by networks of city lights, divided into two glowing economic hemispheres beneath the stars. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'THE FINAL QUESTION: SHARED PROGRESS OR ISOLATION?'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# Write prompts file
out_prompts.write_text("\n\n".join(prompts) + "\n", encoding="utf-8")
print(f"Generated {len(prompts)} scenes in {out_prompts.name}")

# Now generate chapter_08_visual.md
with open(ep_dir / "scene_timing_map.json") as f:
    timing_data = json.load(f)

ch08_scenes = [s for s in timing_data if s.get("chapter") == "08"]

visual_header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_08_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_08.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_08.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-13 19:48
-->

# Chapter 08 Visual Script — The Bangkok Intersection

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 8 (The Bangkok Intersection: The Grand Finale and the Fate of Global Mobility), đồng bộ toán học 1-1 với 48 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_08.txt`.

- **Vũ trụ Mỹ thuật:** Urban Monsoon Noir & Geopolitical Macroeconomic Climax.
- **Bảng màu Sâu lắng & Sang trọng:** Rainy Midnight Asphalt (`#12151B`), Bangkok Indigo Slate (`#151B24`), Wet Chrome (`#64748B`), Weathered Dust Terracotta (`#5C4033`), Dual Amber (`#F59E0B`), Crimson (`#EF5350` / `#B71C1C`), Imperial Champagne Gold (`#D4AF37`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Soft Golden Tungsten Rim Lights, Anamorphic Rain Streaks, Atmospheric Bokeh reflections, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~25% cảnh mấu chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :--- :---: | :---: |
"""

text_overlays_ch08 = {
    "CH08_SC001": "BANGKOK, THAILAND: THE EPICENTER",
    "CH08_SC009": "PARALLEL WORLDS: MECHANICAL VS DIGITAL",
    "CH08_SC014": "STELLA LI: \"WE ARE NOT COMING TO THE US\"",
    "CH08_SC017": "WESTERN TARIFF WALL: 100% IMPORT DUTY",
    "CH08_SC020": "GLOBAL AUTO MARKET: $4 TRILLION BIFURCATION",
    "CH08_SC024": "INDUSTRIAL SANCTUARY: PROTECTING 18% SHARE",
    "CH08_SC026": "AVERAGE US CAR PRICE: $47,870 USD",
    "CH08_SC028": "THE 82% WORLD: THE GLOBAL SOUTH ARENA",
    "CH08_SC031": "BYD ADVANTAGE: -35% COST / 75% INTEGRATION",
    "CH08_SC035": "TOYOTA SCALE: 11.2M UNITS / $34B CASH FORTRESS",
    "CH08_SC040": "ECONOMIC GRAVITY: TARIFFS CANNOT STOP SCALE",
    "CH08_SC048": "THE FINAL QUESTION: SHARED PROGRESS OR ISOLATION?"
}

visual_descs_ch08 = {
    "CH08_SC001": "Toàn cảnh ngã tư sầm uất tại trung tâm Bangkok lúc chạng vạng trong cơn mưa rào nhiệt đới, mặt đường ướt phản chiếu ánh đèn neon rực rỡ.",
    "CH08_SC002": "Dòng xe cộ đông đúc giờ tan tầm tại Bangkok, mưa xối xả làm nhòe ánh đèn pha và đèn hậu đỏ rực kéo dài bất tận.",
    "CH08_SC003": "Chiếc xe bán tải Toyota Hilux màu xám kim loại cũ kỹ nhích từng mét trên làn đường trung tâm, dáng vẻ vững chãi bất chấp thời gian.",
    "CH08_SC004": "Cận cảnh thân xe Hilux bám đầy bụi đỏ công trường khô khốc, những giọt nước mưa rửa trôi từng vệt bụi trên lớp thép dày.",
    "CH08_SC005": "Khối động cơ diesel của chiếc Hilux rung nhẹ đều đặn, tiếng nổ trầm chắc quen thuộc của cỗ máy đã bền bỉ phục vụ suốt một thập kỷ.",
    "CH08_SC006": "Chiếc xe bán tải siêu hybrid BYD Shark màu đen bóng mới tinh từ từ tiến lên đỗ song song ngay bên cạnh chiếc Hilux.",
    "CH08_SC007": "Dải đèn LED ban ngày vắt ngang đầu xe BYD Shark phát sáng sắc lẹm xé toang màn mưa, thân xe bóng loáng không một vết xước.",
    "CH08_SC008": "Khoang lái kỹ thuật số hiện đại của chiếc xe hybrid phát sáng êm dịu qua lớp kính ướt, màn hình cảm ứng xoay trung tâm phản chiếu gương mặt tài xế.",
    "CH08_SC009": "Góc quay trực diện hai chiếc bán tải đỗ cạnh nhau trước cột đèn đỏ: một bên là biểu tượng cơ khí thế kỷ 20, một bên là biểu tượng công nghệ thế kỷ 21.",
    "CH08_SC010": "Mặt đường nhựa ướt sũng nằm giữa hai bánh xe, phản chiếu ánh đèn giao thông màu đỏ, phân tách hai thế giới công nghiệp hoàn toàn đối lập.",
    "CH08_SC011": "Hình ảnh giải phẫu động cơ diesel đúc bằng gang với các piston và trục cam cơ học rèn thép sáng bóng dưới ánh đèn vàng bảo tàng công nghiệp.",
    "CH08_SC012": "Hình ảnh giải phẫu khung gầm trượt điện tử thông minh tích hợp pin lưỡi dao và bo mạch điều khiển buồng lái phát sáng ánh vàng hổ phách.",
    "CH08_SC013": "Phó Chủ tịch điều hành Stella Li trong bộ vest tối màu trang trọng, ngồi đĩnh đạc trả lời phỏng vấn quốc tế với phong thái tự tin và sắc sảo.",
    "CH08_SC014": "Phòng điều khiển tin tức quốc tế phát lại tuyên bố lịch sử đầu năm 2024: BYD chính thức tuyên bố không có kế hoạch vào thị trường Mỹ.",
    "CH08_SC015": "Văn phòng tin tức tài chính phương Tây tại New York, các nhà phân tích kinh tế xôn xao bàn tán trước màn hình thị trường xe hơi quốc tế.",
    "CH08_SC016": "Trang nhất tờ báo tài chính quốc tế đặt trên bàn làm việc, các bài xã luận đồng loạt nhận định đây là bước thoái lui trước hàng rào thuế quan.",
    "CH08_SC017": "Hàng rào thuế quan 100% đồ sộ ngăn cách biên giới công nghiệp Bắc Mỹ, bầu trời xám giông bão bao trùm lên các rào cản thương mại.",
    "CH08_SC018": "Phòng tác chiến địa kinh tế ban đêm, quả địa cầu khổng lồ phát sáng các tuyến dòng chảy thương mại bỏ qua Bắc Mỹ để đổ thẳng về Nam Bán Cầu.",
    "CH08_SC019": "Siêu tàu chở ô tô viễn dương rẽ sóng biển sâu lúc hoàng hôn, chở theo hàng ngàn xe điện hướng về thị trường Nam Mỹ và Đông Nam Á.",
    "CH08_SC020": "Đồ thị vĩ mô mô phỏng thị trường xe hơi toàn cầu trị giá 4 nghìn tỷ USD bị nứt đôi thành hai mảng kiến tạo kinh tế song song.",
    "CH08_SC021": "Bản đồ thế giới phân tách thành hai bán cầu phát sáng trên bàn kính: bán cầu phòng thủ phương Tây và bán cầu mở rộng của Nam Bán Cầu.",
    "CH08_SC022": "Khu đại lý ô tô sang trọng tại ngoại ô Mỹ lúc chạng vạng, các mẫu SUV cỡ lớn và bán tải đắt tiền đỗ sau hàng rào bảo vệ vững chắc.",
    "CH08_SC023": "Phòng điều trần ủy ban thương mại tại Washington, chiếc búa thẩm phán gõ xuống bàn gỗ khẳng định chính sách bảo hộ công nghiệp nội địa.",
    "CH08_SC024": "Phòng họp lãnh đạo Detroit, các giám đốc điều hành thở phào khi bức tường thuế quan tạm thời bảo vệ 18% thị phần của trật tự cũ.",
    "CH08_SC025": "Hợp đồng mua xe của một người tiêu dùng gia đình Mỹ đặt trên bàn, các con số trả góp hàng tháng tăng vọt dưới ánh đèn hiên nhà.",
    "CH08_SC026": "Bảng giá niêm yết xe mới tại đại lý Mỹ hiển thị con số giá bán trung bình chạm ngưỡng kỷ lục gần 48.000 USD dưới ánh đèn rọi.",
    "CH08_SC027": "Người tiêu dùng phương Tây nhìn qua cửa sổ kính phòng chờ sân bay, ngắm nhìn các dòng xe điện thông minh giá cả phải chăng lăn bánh ở nước ngoài.",
    "CH08_SC028": "Bản đồ thế giới 82% gồm Đông Nam Á, Nam Mỹ, Trung Đông và châu Phi sáng bừng ánh vàng ấm, nơi các quy tắc thị trường mới đang được viết nên.",
    "CH08_SC029": "Cảng biển nhộn nhịp tại Nam Mỹ, các lô xe mới xuất xưởng từ châu Á lăn bánh xuống cầu cảng trong nắng nhiệt đới rực rỡ.",
    "CH08_SC030": "Showroom ô tô đông đúc tại Jakarta hoặc São Paulo, các gia đình trẻ hào hứng trải nghiệm mẫu xe hybrid mới với chi phí hợp lý.",
    "CH08_SC031": "Bảng phân tích kiểm toán chi phí sản xuất: Lợi thế cấu trúc chi phí thấp hơn 35% và tỷ lệ tự chủ linh kiện lên tới 75% của BYD.",
    "CH08_SC032": "Dây chuyền sản xuất tích hợp dọc quy mô khổng lồ, nơi khung xe, pin và động cơ điện được chế tạo đồng bộ trong cùng một đại tổ hợp.",
    "CH08_SC033": "Bố cục đối chiếu thử thách: áp lực quỹ lương gần 1 triệu lao động đặt cạnh đồ thị mất giá nhanh chóng của xe điện đã qua sử dụng.",
    "CH08_SC034": "Trụ sở tập đoàn Toyota tại Nhật Bản lúc bình minh, ánh nắng sớm chiếu rọi lên các tòa tháp điều hành và các trung tâm nghiên cứu hiện đại.",
    "CH08_SC035": "Tượng đài khắc số liệu công nghiệp: Sản lượng giao xe kỷ lục vượt 11,2 triệu xe mỗi năm cùng pháo đài tiền mặt 34 tỷ USD của Toyota.",
    "CH08_SC036": "Kho lưu trữ bằng sáng chế pin thể rắn bọc da gáy vàng đặt cạnh các mẫu pin thử nghiệm phát sáng ánh bạch kim tinh khiết trên bàn gỗ tuyết tùng.",
    "CH08_SC037": "Bố cục đối đầu thế kỷ: Biểu tượng hai tập đoàn xe hơi hàng đầu đặt ở hai đầu chiếc bàn họp dài dưới ánh đèn chiếu điểm kịch tính.",
    "CH08_SC038": "Thẻ nhận diện kênh tài liệu X-Economics trên nền titan xước sang trọng với ánh sáng vàng ấm, biểu tượng đăng ký kênh trang nhã.",
    "CH08_SC039": "Góc nhìn flycam bức tường thuế quan bê tông khổng lồ kéo dài tít tắp giữa sa mạc, bóng chiều tà đổ dài trên mặt đất cằn cỗi.",
    "CH08_SC040": "Bảng viết phương trình kinh tế học tại trường đại học: quy luật trọng lực kinh tế và quy mô công nghiệp vượt qua mọi rào cản nhân tạo.",
    "CH08_SC041": "Cận cảnh cột đèn giao thông tại ngã tư Bangkok chuyển từ màu đỏ sang màu xanh lục rực rỡ, ánh sáng xanh loang trên mặt đường mưa ướt.",
    "CH08_SC042": "Hai chiếc xe bán tải Hilux và Shark cùng lúc nhấn ga tăng tốc, bánh xe cuộn nước mưa bắn tung tóe dưới ánh đèn đường vàng rực.",
    "CH08_SC043": "Bên trong cabin chiếc Hilux, người tài xế trung niên tay cầm vô lăng vững chãi, ánh mắt bình thản tin cậy cỗ máy đã nuôi sống gia đình 10 năm.",
    "CH08_SC044": "Đuôi chiếc xe Toyota Hilux lướt đi trong đêm mưa, đèn hậu đỏ ấm áp hòa vào dòng xe cộ bền bỉ trên đại lộ Bangkok.",
    "CH08_SC045": "Bên trong cabin chiếc BYD Shark, người lái xe trẻ tuổi mỉm cười thư thái, tận hưởng không gian yên tĩnh và tiện nghi số giữa cơn bão nhiệt đới.",
    "CH08_SC046": "Góc nhìn flycam trên cao hai chiếc xe song hành lao vút về phía trước, để lại hai vệt ánh sáng đỏ phản chiếu trên mặt đường mưa ướt.",
    "CH08_SC047": "Đường chân trời Bangkok nửa đêm nhìn từ tầng thượng tòa nhà chọc trời, hàng triệu đốm sáng lung linh xuyên qua màn sương mưa mờ ảo.",
    "CH08_SC048": "Góc nhìn tráng lệ toàn cảnh Trái Đất từ quỹ đạo ban đêm, các lục địa rực sáng mạng lưới đèn đô thị phân chia thành hai bán cầu kinh tế huyền ảo."
}

rows_ch08 = []
for s in ch08_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descs_ch08.get(sid, "Bối cảnh công nghiệp thực tế đời thường.")
    overlay = text_overlays_ch08.get(sid, "Không")
    stream = "I2V" if (sid in ["CH08_SC013"]) else "T2V"
    rows_ch08.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

visual_content = visual_header + "\n".join(rows_ch08) + "\n"
out_visual.write_text(visual_content, encoding="utf-8")
print(f"Generated {len(rows_ch08)} table rows in {out_visual.name}")
