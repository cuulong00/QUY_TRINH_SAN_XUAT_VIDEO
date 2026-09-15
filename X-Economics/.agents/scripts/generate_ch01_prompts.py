from pathlib import Path
import re

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_file = ep_dir / "prompts_chapter_01.txt"

# Master aesthetic style parameters (Warm, Deep, Subdued, Luxurious, High-Prestige)
STYLE = "A 2D warm cinematic editorial illustration in high-prestige corporate noir luxury aesthetic. Deep rich walnut tones (#1C1917), dark mahogany slate (#231C18), and brushed titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

# Helper to add scene
def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH01_SC001
add_scene(
    f"{STYLE}. An expansive corporate boardroom at dusk overlooking a glowing metropolis. On a polished dark walnut table sits a luxury brass document stand holding an open leather-bound economic ledger. Subtle gold embossed typography fixed in the lower-left area 25% above the bottom edge reading 'GLOBAL AUTO SECTOR: $4 TRILLION'. Elegant, authoritative documentary visual.",
    "Steady camera shot with subtle imperceptible push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH01_SC002
add_scene(
    f"{STYLE}. An immense modern automotive assembly hall during shift change. Hundreds of industrial technicians in navy blue uniforms and yellow safety helmets walking methodically along clean polished concrete walkways between towering robotic stamping presses. Warm tungsten overhead lamps cast golden directional light beams through soft atmospheric haze.",
    "Slow tracking shot moving forward along the factory floor walkway as technicians move in steady formation, maintaining crisp contours and velvety contrast"
)

# CH01_SC003
add_scene(
    f"{STYLE}. An imposing boardroom wall in an American automotive headquarters displaying framed historic monochrome archival portraits of 20th-century industrial executives in dark mahogany frames. The dark wood-paneled room is illuminated by a warm brass desk lamp casting a rich golden glow across a polished mahogany conference table.",
    "Slow smooth panning shot from left to right across the framed executive portraits, camera moving steadily with rich warm rim lighting"
)

# CH01_SC004
add_scene(
    f"{STYLE}. A forensic macroeconomist in a dark charcoal vest examining industrial supply-chain blueprints in a dim mahogany study at night. On the table, large printed technical schematics lie partially unrolled, illuminated by a warm brass desk lamp. The analyst touches a critical node highlighted in deep crimson bordeaux (#8B0000).",
    "Slow camera push-in dolly shot toward the blueprints on the desk, warm shadows deepening as the camera glides closer with smooth focus"
)

# CH01_SC005
add_scene(
    f"{STYLE}. The historic red-brick exterior of an automotive factory complex in Wolfsburg Germany under an overcast twilight sky. Cool blue-grey dusk sky contrasted with the warm amber glow from massive industrial windows. A cluster of German autoworkers in dark coats confer quietly near an iron perimeter gate.",
    "Slow camera pull-back dolly shot revealing the vast silent factory facade and iron gates, atmospheric dusk lighting maintaining quiet gravity"
)

# CH01_SC006
add_scene(
    f"{STYLE}. An executive corner office high above Detroit Michigan looking out through floor-to-ceiling glass onto the Detroit River. On a heavy dark walnut credenza, an open leather audit binder displays financial line items highlighted with deep crimson ink. Warm tungsten interior lamps reflect softly against the glass.",
    "Slow panning shot across the executive desk toward the riverfront skyline outside, soft directional amber lighting catching the brass desk fittings"
)

# CH01_SC007
add_scene(
    f"{STYLE}. A formal press conference room in Tokyo Japan. Two senior Japanese automotive executives in bespoke dark charcoal suits bow respectfully before rows of press photographers on an elevated wooden stage. The backdrop is a minimalist dark cedar panel wall with warm indirect architectural lighting.",
    "Slow camera push-in shot toward the executives on the stage, flash reflections gently pulsing while retaining dignified, composed posture"
)

# CH01_SC008
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and round eyeglasses directly from the reference photo. The subject is seated calmly at the head of a massive dark mahogany conference table in Nagoya, wearing a tailored dark suit, exuding quiet authority in luminous low-key warm lighting.",
    "Slow camera push-in dolly shot toward the subject, maintaining their composed facial expression and all details of the reference image exactly"
)

# CH01_SC009
add_scene(
    f"{STYLE}. An advanced operations command room at an automotive headquarters in Shenzhen China at dusk. Chinese engineers in tailored dark suits observe an immense curved wall display showing oceanic shipping routes and battery manufacturing metrics. Warm tungsten and amber LED light accents illuminate the dark slate interior (#1E242B).",
    "Slow forward tracking shot between the control desks toward the panoramic digital display wall, smooth measured cinematic motion"
)

# CH01_SC010
add_scene(
    f"{STYLE}. An architectural conceptual cartography map of North America depicted as an elevated, walled industrial citadel surrounded by dark stone barriers. Outside the perimeter, vibrant amber trade corridors and commercial shipping lanes flow past the continent into the southern hemisphere. High-prestige editorial cartography in warm walnut and brushed titanium tones.",
    "Slow high-angle panning shot tracking the bright amber shipping lines flowing past the walled perimeter into open waters"
)

# CH01_SC011
add_scene(
    f"{STYLE}. The massive bow of a modern custom roll-on roll-off automotive transport vessel cutting through deep ocean waters at golden hour sunset. Neatly arranged rows of newly built passenger vehicles are secured on illuminated staging decks. Warm golden sunlight reflects off the dark sea and steel hull.",
    "Low-angle tracking shot moving parallel with the cargo ship as bow waves curl into amber sunset water, epic cinematic scale"
)

# CH01_SC012
add_scene(
    f"{STYLE}. The expansive entrance gate of an automotive manufacturing complex in Bahia Brazil. A modern industrial entrance gate stands over refurbished glass-and-steel guard pavilions, replacing weathered old signage. Warm tropical late-afternoon sun casts long amber shadows across clean black asphalt.",
    "Slow smooth panning shot across the modernized entrance gate, vibrant warm tropical sunlight illuminating the architectural transformation"
)

# CH01_SC013
add_scene(
    f"{STYLE}. A precision engineering cutaway of an advanced plug-in hybrid electric powertrain mounted on an illuminated test bench in a dark slate laboratory. Polished metal cylinders, electric motor coils, and a sleek blade battery enclosure radiate a soft golden-amber glow (#F59E0B) through intricate heat-dissipation fins.",
    "Slow circular camera orbital shot around the illuminated hybrid engine cutaway, warm metallic reflections highlighting precision engineering tolerances"
)

# CH01_SC014
add_scene(
    f"{STYLE}. A dark, sophisticated economic globe crafted from polished dark walnut wood and brushed brass in a high-ranking think-tank office. Eighty-two percent of the world landmass outside North America is illuminated with a continuous network of warm amber and champagne gold logistics corridors.",
    "Slow rotating camera shot gliding over the illuminated continents of Southeast Asia, Latin America, and Africa on the globe"
)

# CH01_SC015
add_scene(
    f"{STYLE}. A dramatic side-by-side conceptual split composition in a prestigious automotive pavilion. On the left, the dark polished front grille of a classic Toyota Hilux under warm studio spotlight; on the right, the razor-sharp LED light bar of a sleek BYD Shark pickup under matching amber tungsten illumination. Deep velvety slate background.",
    "Slow symmetric push-in dolly shot toward the center divide between the two vehicles, dramatic high-contrast lighting accentuating the metal contours"
)

# CH01_SC016
add_scene(
    f"{STYLE}. An international economic press conference hall. A gallery of international financial journalists and photographers holding recording devices and broadcast microphones, their faces illuminated by warm directional stage spotlights against a dark auditorium backdrop.",
    "Slow tracking shot across the press corps as cameras click, warm directional light cutting through atmospheric auditorium haze"
)

# CH01_SC017
add_scene(
    f"{STYLE}. Close-up macro shot of a sleek broadcast microphone resting on a polished dark wood podium, flanked by international media outlet logos. In the soft-focused background, the silhouettes of assembled journalists sit attentively in warm tungsten illumination.",
    "Steady camera shot with subtle rack focus from the microphone grill to the attentive audience silhouettes in the background"
)

# CH01_SC018
add_scene(
    f"{STYLE}. A prestigious corporate press briefing stage. A formal executive nameplate crafted from brushed brass and dark walnut rests on the dais. Behind the podium, a large minimalist dark presentation screen radiates a subtle warm amber glow.",
    "Slow smooth push-in dolly shot toward the executive dais, warm stage lighting creating crisp elegant contours"
)

# CH01_SC019
add_scene(
    f"@evp_byd_stellali.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and business attire directly from the reference photo. The subject is seated before international press microphones on an executive panel stage bathed in warm luminous directional lighting, offering a calm, composed, knowing smile.",
    "Slow camera push-in dolly shot toward the subject, maintaining their composed facial expression and all details of the reference image exactly"
)

# CH01_SC020
add_scene(
    f"@evp_byd_stellali.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and business attire directly from the reference photo. The subject is speaking with measured confidence into the podium microphone, gesturing gracefully, set against a dark walnut backdrop with warm golden rim lighting.",
    "Steady camera shot focusing on the subject speaking with poised authority, maintaining all details of the reference image exactly"
)

# CH01_SC021
add_scene(
    f"{STYLE}. Wide-angle view of the executive press briefing from the rear of the auditorium. The female executive on the illuminated warm stage addresses dozens of international reporters, with large digital presentation displays on either side showing global market logistics maps.",
    "Slow crane shot drifting gently downward toward the auditorium floor, warm stage lights casting a golden aura across the dark hall"
)

# CH01_SC022
add_scene(
    f"{STYLE}. An expansive digital presentation screen on stage displaying a glowing geographic infographic of global automotive demand. The map highlights massive growth corridors across Latin America, Southeast Asia, and Europe in luminous champagne gold, while North America remains a subdued grey outline.",
    "Slow panning shot across the digital market map, bright amber logistics lines pulsing gently across the emerging markets"
)

# CH01_SC023
add_scene(
    f"{STYLE}. A bustling financial trading floor in lower Manhattan at mid-morning. Wall Street analysts in tailored dark vests and ties conferring around multi-screen Bloomberg terminals displaying sudden automotive earnings alerts and divergent stock tickers. Warm interior lighting contrasted with cool slate shadows.",
    "Slow tracking shot moving between trading desks as analysts gesture toward glowing market charts, maintaining serious analytical urgency"
)

# CH01_SC024
add_scene(
    f"{STYLE}. A classic mid-century American suburban automobile dealership on Route 66 at twilight. Chrome-trimmed vintage convertibles and station wagons gleam under warm neon sign glow and incandescent festoon lights. Polished asphalt reflecting the warm nostalgic sunset.",
    "Slow cinematic tracking shot along the vintage showroom glass, warm nostalgic lights reflecting across the polished asphalt"
)

# CH01_SC025
add_scene(
    f"{STYLE}. An American middle-class family in the nineteen-eighties standing outside an authorized Japanese car dealership showroom, inspecting a reliable Japanese compact sedan. Warm late-afternoon sunlight illuminates clean showroom glass and chrome door handles.",
    "Slow camera push-in shot toward the family and the vehicle, capturing the nostalgic transition of American consumer preference"
)

# CH01_SC026
add_scene(
    f"{STYLE}. The neoclassical stone facade and towering dome of the United States Capitol in Washington DC at sunset. Golden-hour tungsten sunlight strikes the marble colonnades against a dramatic dark slate storm sky, projecting an aura of immense sovereign legislative power.",
    "Slow upward tilt shot from the Capitol plaza toward the grand dome, golden sunlight illuminating the marble columns against dark clouds"
)

# CH01_SC027
add_scene(
    f"{STYLE}. A printed official federal proclamation document resting on a polished mahogany committee desk beneath a warm brass banker lamp. Clean bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'SECTION 301 TARIFF: 100%'. Deep crimson bordeaux wax seal visible on the document.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH01_SC028
add_scene(
    f"{STYLE}. An official hardbound legislative ledger of the Inflation Reduction Act resting on a dark walnut library table in the Library of Congress. Warm directional spotlight illuminates the gold-embossed lettering on the leather spine and crisp white statute pages.",
    "Slow camera push-in dolly shot toward the open legislative binder, warm tungsten light casting soft velvet shadows across the table"
)

# CH01_SC029
add_scene(
    f"{STYLE}. The imposing limestone entrance of the Herbert C. Hoover Department of Commerce building in Washington DC. A polished bronze official seal and department plaque gleam under warm architectural downlights at dusk.",
    "Slow upward crane shot revealing the grand bronze plaque and neoclassical limestone pillars, dignified governmental atmosphere"
)

# CH01_SC030
add_scene(
    f"{STYLE}. A macro technical inspection of a connected vehicle telematics control unit motherboard. Polished silicon chips, microprocessors, and circuit traces illuminated by a warm amber diagnostic laser. Digital security grid lines highlighted in warning crimson (#8B0000).",
    "Slow tracking macro shot across the illuminated microcircuitry, precision diagnostic light glinting off solder joints and copper traces"
)

# CH01_SC031
add_scene(
    f"{STYLE}. A busy industrial commercial border crossing between the United States and Mexico at night. Heavy steel security gates, surveillance cameras, and tall inspection gantries illuminated by warm amber floodlights against a deep midnight sky.",
    "Slow high-angle tracking shot over the border inspection lanes as cargo trucks pass through security scanners in measured order"
)

# CH01_SC032
add_scene(
    f"{STYLE}. Specialized multi-level car transporter trailer trucks loaded with newly assembled vehicles parked in an expansive logistics holding yard near a border rail depot. Floodlights cast long amber beams across rows of vehicles in deep slate shadows.",
    "Slow panning shot along the row of loaded car transporter trailers, metallic vehicle bodies reflecting warm overhead security lights"
)

# CH01_SC033
add_scene(
    f"{STYLE}. A congressional committee hearing room on Capitol Hill. Lawmakers in dark suits seated behind an elevated curved mahogany dais, listening intently to testimony under warm recessed chandelier lighting. Heavy dark drapes and brass railings frame the scene.",
    "Slow tracking shot across the congressional dais, lawmakers reviewing printed hearing dossiers in solemn deliberation"
)

# CH01_SC034
add_scene(
    f"{STYLE}. An American consumer in his early 40s standing at an automotive dealership sales desk, looking thoughtfully at a multi-page vehicle purchase contract. In the background through showroom glass, rows of full-size trucks sit under bright dealership lights.",
    "Slow push-in shot toward the consumer, capturing a pensive, calculating expression as he reviews the monthly payment figures"
)

# CH01_SC035
add_scene(
    f"{STYLE}. Rows of massive, heavy-duty American pickup trucks and full-size luxury SUVs parked tightly across a vast suburban dealership lot. Chrome front grilles and high hoods gleam under warm golden-hour sunset light in deep slate surroundings.",
    "Slow low-angle tracking shot moving along the towering front bumpers of the oversized trucks, emphasizing immense physical mass"
)

# CH01_SC036
add_scene(
    f"{STYLE}. A dealership window price sticker affixed to the side window of a brand-new full-size American SUV. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'US AVERAGE TRANSACTION PRICE: $48,000'. Dark showroom reflection visible in the glass.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH01_SC037
add_scene(
    f"{STYLE}. A solitary modern automobile driving along a wide American interstate highway at dusk, flanked by towering concrete noise barriers and tall protective fences. Warm amber taillights illuminate the empty road, creating a mood of an expensive, isolated industrial sanctuary.",
    "Slow tracking shot behind the vehicle moving down the walled highway corridor, golden twilight sky deepening into dark indigo"
)

# CH01_SC038
add_scene(
    f"{STYLE}. Two senior Chinese automotive strategists in a high-rise executive war room in Shenzhen late at night. They stand before a large illuminated glass drafting table displaying global automotive volume formulas and market distribution models in warm amber lines.",
    "Slow camera push-in dolly shot toward the strategists as they analyze the glowing market calculations on the glass table"
)

# CH01_SC039
add_scene(
    f"{STYLE}. High-angle aerial view of a massive automotive distribution holding lot in the United States. Thousands of newly built vehicles arranged in meticulous geometric grids, reflecting warm morning sunlight across dark asphalt in quiet, motionless order.",
    "Smooth high-angle crane shot descending slowly over the geometric vehicle grid, clean architectural symmetry and warm lighting"
)

# CH01_SC040
add_scene(
    f"{STYLE}. An immense global deep-water container terminal bustling with round-the-clock activity at dusk. Towering gantry cranes hoisting shipping containers onto massive container vessels under warm amber floodlights against a deep blue-grey ocean.",
    "Slow panning shot across the bustling seaport terminal, cranes operating in synchronized motion with warm amber lights glowing"
)

# CH01_SC041
add_scene(
    f"{STYLE}. A sophisticated circular market distribution infographic etched in brushed gold upon a dark polished slate wall in an executive boardroom. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'US MARKET: 18% | GLOBAL SOUTH: 82%'. Warm directional spotlight.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH01_SC042
add_scene(
    f"{STYLE}. A vast modern automotive delivery center in Shanghai bathed in warm architectural lighting. Dozens of Chinese families taking delivery of new electric vehicles, smiling and inspecting interiors in a bright, clean, premium delivery pavilion.",
    "Slow tracking shot gliding through the spacious delivery center, capturing the vibrant atmosphere of high-volume vehicle handovers"
)

# CH01_SC043
add_scene(
    f"{STYLE}. A side-by-side volume comparison bar chart displayed on a large brushed-titanium presentation monitor. A towering golden bar representing China thirty-million annual volume stands beside a smaller slate-grey bar for the United States sixteen-million volume. Warm studio lighting.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH01_SC044
add_scene(
    f"{STYLE}. An expansive aerial panorama of a major Latin American coastal metropolis at golden hour. Multiple elevated highway expressways curve gracefully through urban districts filled with flowing evening vehicle traffic in warm amber sunlight.",
    "Slow cinematic aerial tracking shot curving over the sprawling city highway system as sunset glints off vehicle windshields"
)

# CH01_SC045
add_scene(
    f"{STYLE}. An authentic evening street scene in an emerging market capital like Bangkok. Modern elevated skytrain viaducts above, vibrant boulevard traffic below filled with motorcycles, taxis, and family cars under warm streetlights and neon shopfront signs.",
    "Slow tracking shot at street level capturing the dynamic energy of bustling emerging-market urban mobility in warm evening tones"
)

# CH01_SC046
add_scene(
    f"{STYLE}. A diverse crowd of commuters and families waiting at a modern multimodal transit interchange in Southeast Asia. Thoughtful, hardworking citizens going about their evening commutes, surrounded by clean architectural glass and warm overhead lighting.",
    "Slow panning shot across the diverse commuter faces, natural warm lighting creating an authentic, dignified documentary portrait"
)

# CH01_SC047
add_scene(
    f"{STYLE}. An enormous American heavy-duty pickup truck parked in a modest suburban driveway, its towering hood and oversized chrome grille dominating the small front yard. An expensive dealer window price sticker glints in the midday sun.",
    "Slow upward tilt shot from the truck tire to its massive hood, emphasizing disproportionate scale and excessive vehicle bulk"
)

# CH01_SC048
add_scene(
    f"{STYLE}. A sleek, highly functional compact five-door modern hybrid hatchback parked neatly outside a charming neighborhood cafe in a sunny emerging market street. A young couple loads groceries into the rear hatch with ease under warm morning sunlight.",
    "Slow camera push-in shot toward the practical family hatchback, highlighting sensible urban dimensions and modern design"
)

# CH01_SC049
add_scene(
    f"{STYLE}. An international intermodal freight terminal where heavy container gantries load standardized shipping containers bearing industrial manufacturer emblems onto long freight trains. Warm golden-hour sunset reflecting off steel rails and container sides.",
    "Slow tracking shot moving parallel with the freight train as the crane lowers a container smoothly into place on the flatbed"
)

# CH01_SC050
add_scene(
    f"{STYLE}. A large physical world map mounted on a dark walnut boardroom wall, illuminated from beneath by warm golden fiber-optic lines. The trade routes radiate from Shenzhen across Southeast Asia, South America, and Central Europe, completely bypassing North America.",
    "Slow camera push-in dolly shot toward the glowing trade routes on the wooden wall map, golden lines tracing expansive global reach"
)

# CH01_SC051
add_scene(
    f"{STYLE}. A massive concrete tariff wall barrier stretching across a desert landscape at dusk, casting a long dark shadow across an empty highway. In the distance beyond the wall, warm golden twilight lingers over open horizon.",
    "Slow camera pull-back shot along the base of the towering concrete wall, dramatic low-key lighting accentuating physical isolation"
)

# CH01_SC052
add_scene(
    f"{STYLE}. The European Commission Berlaymont headquarters building in Brussels Belgium on a rainy autumn evening. Reflections of glowing amber office windows shimmer on wet stone plazas while diplomats with dark umbrellas hurry between security entrances.",
    "Slow tracking shot across the wet Brussels plaza toward the illuminated governmental facade, cool rain balanced by warm interior lights"
)

# CH01_SC053
add_scene(
    f"{STYLE}. An emergency corporate boardroom meeting of senior German industrial executives in dark tailored wool suits. Strained expressions, hands clasped on dark mahogany tables around thick financial crisis reports under warm focused downlights.",
    "Slow camera push-in dolly shot toward the solemn executives around the boardroom table, quiet tension palpable in the warm shadows"
)

# CH01_SC054
add_scene(
    f"{STYLE}. A high-angle cinematic view of the immense Volkswagen factory complex in Wolfsburg Germany at dusk. Towering red-brick industrial power chimneys rise into misty twilight, the illuminated round corporate emblem glowing softly in the evening haze.",
    "Slow dramatic aerial crane shot drifting upward past the historic brick chimneys as evening lights switch on across the complex"
)

# Write to file
content = "\n\n".join(prompts) + "\n"
out_file.write_text(content, encoding="utf-8")
print(f"Successfully generated {len(prompts)} scenes in {out_file.name}")
