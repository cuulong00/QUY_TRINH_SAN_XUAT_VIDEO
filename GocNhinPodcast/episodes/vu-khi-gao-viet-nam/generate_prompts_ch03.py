# -*- coding: utf-8 -*-
"""
Script generating prompts_chapter_03.txt for Google Flow Batch Studio
Episode: vu-khi-gao-viet-nam | Chapter 03 (55 scenes)
Art Direction: Luminous Warm Editorial Illustration (Warm Ivory Cream #FAF7EE, Ripe Golden Amber #F59E0B)
"""

import os

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam'
output_path = os.path.join(EPISODE_DIR, 'prompts_chapter_03.txt')

scenes = [
    {
        "id": "CH03_SC001",
        "ref": None,
        "subject": "a charming traditional wooden tourist sampan boat gliding gently across the serene waters of the Tien River under warm golden morning light",
        "setting": "a tranquil river channel in the Mekong Delta shaded by lush water coconut palms",
        "text": None,
        "motion": "Horizontal camera tracking shot following the wooden sampan boat cruising the peaceful river"
    },
    {
        "id": "CH03_SC002",
        "subject": "authentic local Vietnamese villagers in conical hats paddling small wooden canoes laden with tropical fruits along a tranquil shade-dappled canal",
        "setting": "a scenic countryside canal in Ben Tre under gentle warm morning sunshine",
        "text": None,
        "motion": "Cinematic wide camera pan gliding smoothly along the shaded rural canal and fruit canoes"
    },
    {
        "id": "CH03_SC003",
        "subject": "an authentic Vietnamese systems agronomist in a light work shirt using a stylus pen on an interactive GIS touchscreen displaying regional satellite crop data",
        "setting": "an agro-hydrological data operations office under warm directional desk lamp illumination",
        "text": None,
        "motion": "Slow push-in shot toward the interactive satellite agronomic GIS console"
    },
    {
        "id": "CH03_SC004",
        "subject": "an epic high-altitude overview revealing the boundless network of crisscrossing canals connecting thousands of geometric green and gold rice plots",
        "setting": "the vast territory of the thirteen Mekong Delta provinces stretching to the horizon under clear skies",
        "text": None,
        "motion": "Epic panoramic aerial glide soaring over the boundless canal grid and fertile rice paddies"
    },
    {
        "id": "CH03_SC005",
        "subject": "heavy agricultural tractor plows overturning dark fertile alluvial soil, automated seeders, and motorized water pump gates operating continuously in parallel",
        "setting": "an expansive agrarian production zone in the Mekong Delta bathed in radiant golden dawn light",
        "text": None,
        "motion": "Slow upward tilt from fresh furrowed rich soil up to the rising golden morning sun"
    },
    {
        "id": "CH03_SC006",
        "subject": "an official national land-use master plan chart delineating the vital core of one point five million hectares of strictly protected dedicated rice paddies in glowing amber",
        "setting": "the agricultural planning exhibition hall at the Ministry of Natural Resources and Environment in Hanoi",
        "text": "DAT CHUYEN CANH LUA: 1.5M HA",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 1.5M hectare land boundary"
    },
    {
        "id": "CH03_SC007",
        "subject": "an official agrarian statistics dashboard confirming that the annual cumulative harvested area surges to nearly three point nine million hectares through seasonal crop rotation",
        "setting": "the statistical command room of the General Statistics Office under warm ambient light",
        "text": "DIEN TICH GIEO TRONG: ~3.9M HA",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 3.9M hectare metric"
    },
    {
        "id": "CH03_SC008",
        "subject": "an agro-economic formula diagram on a presentation blackboard demonstrating the powerful land-use intensification multiplier of two point four rotations per year",
        "setting": "the agronomy lecture amphitheater at Can Tho University under warm ceiling lighting",
        "text": "HE SO QUAY VONG: 2.4 LAN",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 2.4x land coefficient"
    },
    {
        "id": "CH03_SC009",
        "subject": "an ornate carved wooden circular agrarian calendar displaying the seamless three-season cyclical rotation of Winter-Spring, Summer-Autumn, and Autumn-Winter crops",
        "setting": "the central meeting hall of an advanced agricultural cooperative in Dong Thap under warm light",
        "text": "3 VU: DONG XUAN - HE THU - THU DONG",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 3-crop rotational calendar"
    },
    {
        "id": "CH03_SC010",
        "subject": "high-capacity red combine harvesters pouring a golden torrent of freshly threshed paddy into waiting transport trucks, a field banner confirming a high yield of seven to eight tons per hectare",
        "setting": "a vast golden Winter-Spring harvest field in An Giang under brilliant warm morning sunlight",
        "text": "NANG SUAT DONG XUAN: 7 - 8 TAN/HA",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 7-8 ton harvest banner"
    },
    {
        "id": "CH03_SC011",
        "subject": "an automated agricultural drone flying low over a flooded nursery field, precision-broadcasting pristine OM5451 certified rice seeds into muddy silt beds",
        "setting": "a downstream paddy field along the Tien River under soft morning sunlight",
        "text": None,
        "motion": "Smooth camera tracking shot following the low-flying agricultural seeder drone over the field"
    },
    {
        "id": "CH03_SC012",
        "subject": "three neatly stacked burlap sample bags displaying certified high-yield purebred rice varieties OM5451, OM18, and Dai Thom 8, marked with a ninety to one hundred day growing cycle",
        "setting": "the seed research and testing agronomy station of the Cuu Long Rice Research Institute",
        "text": "GIONG LUA NGAN NGAY: 90 - 100 NGAY",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the certified rice seed bags"
    },
    {
        "id": "CH03_SC013",
        "subject": "the rotating mechanical reel of a modern combine harvester smoothly cutting through heavy golden ripe rice panicles, golden chaff floating in warm sunbeams",
        "setting": "a dense ripe paddy field in the Mekong Delta under bright morning sunshine",
        "text": None,
        "motion": "Close-up horizontal tracking shot following the harvester cutting reel slicing through ripe paddy"
    },
    {
        "id": "CH03_SC014",
        "subject": "a powerful tractor with steel disc plows cutting deep into dark moist alluvial soil right after harvesting, turning over earth to prepare for the next crop",
        "setting": "a newly harvested delta field with stubble rows under warm afternoon sun",
        "text": None,
        "motion": "Slow push-in camera motion moving behind the heavy tractor plowing the rich alluvial soil"
    },
    {
        "id": "CH03_SC015",
        "subject": "an international grain trade strategist laying out comparative agricultural production maps of Vietnam, Thailand, and India on a dark mahogany conference table",
        "setting": "a regional agricultural policy briefing room under warm brass pendant lights",
        "text": None,
        "motion": "Slow push-in shot toward the comparative Asian rice production maps on the table"
    },
    {
        "id": "CH03_SC016",
        "subject": "a high-resolution triptych digital monitor display presenting the three distinct farming landscapes of the Mekong Delta, the Ganges River basin, and the Chao Phraya plains",
        "setting": "an agro-economic intelligence center workstation under warm ambient lighting",
        "text": None,
        "motion": "Horizontal camera tracking shot scanning across the tripartite Asian agrarian display"
    },
    {
        "id": "CH03_SC017",
        "subject": "an expansive parched agrarian plain in Central India or Northeast Thailand awaiting the annual monsoon, with an infographic confirming their reliance on a single primary crop per year",
        "setting": "a vast rural landscape under a dramatic cloudy monsoon sky with warm sunlight breaking through",
        "text": "AN DO & THAI LAN: 1 VU CHINH/NAM",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the single-crop monsoon plains"
    },
    {
        "id": "CH03_SC018",
        "subject": "a sprawling state-run concrete grain silo complex in Northern India or Central Thailand, with long lines of heavy flatbed trucks unloading millions of tons into closed storage",
        "setting": "a colossal strategic grain reserve depot under bright warm daylight",
        "text": None,
        "motion": "Wide panoramic cinematic shot gliding past the towering enclosed strategic grain silos"
    },
    {
        "id": "CH03_SC019",
        "subject": "an industrial warehouse auditing spreadsheet detailing massive multi-million dollar annual expenditures for facility air cooling, ventilation, and mechanical conveyor maintenance",
        "setting": "a grain silo management administrative office under warm focused desk lamp light",
        "text": None,
        "motion": "Slow push-in shot toward the highlighted grain warehouse operational expenditure ledgers"
    },
    {
        "id": "CH03_SC020",
        "subject": "protective hazmat workers conducting chemical fumigation inside a dimly lit cavernous grain warehouse, towering stacks of bagged rice immobilizing billions in capital for twelve months",
        "setting": "a massive enclosed state grain storage depot under warm industrial safety lamps",
        "text": None,
        "motion": "Slow horizontal tracking shot gliding past immense stacks of immobilized long-term grain stocks"
    },
    {
        "id": "CH03_SC021",
        "subject": "a dynamic logistical supply-chain process flow diagram illustrating the seamless continuous rolling cycle: Field Harvest to River Barge to Modern Mill to Ocean Port",
        "setting": "an executive supply-chain command room under warm recessed lighting",
        "text": "CHUOI CUNG UNG CUON TRON (ROLLING)",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the rolling logistics model"
    },
    {
        "id": "CH03_SC022",
        "subject": "a color-coded thermal calendar map of the Mekong Delta displaying staggered harvest timeframes alternating harmoniously week by week across different provinces",
        "setting": "the agricultural planning division of the Department of Agriculture in Can Tho",
        "text": None,
        "motion": "Horizontal tracking shot past the staggered provincial harvest schedule map"
    },
    {
        "id": "CH03_SC023",
        "subject": "a collaborative consultation room where regional hydrologists and agronomists align crop planting schedules with natural river flood peaks and tidal cycles",
        "setting": "the Southern Institute of Water Resources Planning conference room in warm interior light",
        "text": None,
        "motion": "Slow push-in shot toward the agro-hydrological seasonal synchronization chart"
    },
    {
        "id": "CH03_SC024",
        "subject": "authentic Vietnamese farm workers carrying freshly harvested sacks of golden moist paddy from a sunny field dike directly down to a waiting wooden river boat",
        "setting": "a busy canal embankment in An Giang at high noon under bright warm sunshine",
        "text": None,
        "motion": "Dynamic camera tracking shot following the workers loading fresh paddy sacks into the river boat"
    },
    {
        "id": "CH03_SC025",
        "subject": "large steel freight barges piled high with golden fresh paddy cutting white water wakes as they cruise down the wide Cho Gao canal toward industrial mills at sunset",
        "setting": "the busy Cho Gao navigation canal in Tien Giang under a glowing warm golden-orange sunset",
        "text": None,
        "motion": "Wide cinematic tracking shot following the convoy of rice barges cruising into the sunset"
    },
    {
        "id": "CH03_SC026",
        "subject": "a modern automated rice processing mill interior with high-speed fluidized-bed dryers, color sorters, and robotic fifty-kilo bagging stations operating within forty-eight hours",
        "setting": "a high-tech rice milling complex in Thot Not Can Tho under warm industrial factory lighting",
        "text": "XAY XAT & DONG BAO: 48 GIO",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 48-hour automated milling line"
    },
    {
        "id": "CH03_SC027",
        "subject": "an official stamped international rice export sales agreement lying on an executive desk, a desktop calendar showing a rapid fourteen-day fulfillment window countdown",
        "setting": "the export commercial office of a leading Vietnamese grain corporation in Ho Chi Minh City",
        "text": None,
        "motion": "Slow dynamic push-in shot toward the signed fourteen-day export sales contract"
    },
    {
        "id": "CH03_SC028",
        "subject": "a towering dockside gantry crane hoisting heavy shipping containers filled with newly harvested rice onto a colossal ocean freighter under radiant morning sun",
        "setting": "the deepwater container terminal at Cai Mep Port under clear bright blue skies",
        "text": None,
        "motion": "Slow upward tilt following the container crane lifting export rice onto the container vessel"
    },
    {
        "id": "CH03_SC029",
        "subject": "a comparative logistics cost audit chart displaying Vietnam dramatically lower warehousing overhead compared to conventional long-term grain hoarding competitors",
        "setting": "an agricultural logistics research institute office under warm reading lamps",
        "text": None,
        "motion": "Slow camera glide along the comparative grain logistics expenditure chart"
    },
    {
        "id": "CH03_SC030",
        "subject": "an official certified supply-chain performance report highlighting that the continuous rolling model slashes long-term storage and warehousing costs by forty to fifty percent",
        "setting": "the trade economics audit desk at the Vietnam Food Association in Ho Chi Minh City",
        "text": "TIET KIEM LUU KHO: 40% - 50%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 40-50% cost savings ledger"
    },
    {
        "id": "CH03_SC031",
        "subject": "an export enterprise financial ledger confirming rapid working capital turnover, eliminating burdensome interest payments on long-term idle grain inventory loans",
        "setting": "a corporate financial director office overlooking the Can Tho riverfront in warm morning light",
        "text": None,
        "motion": "Slow push-in shot toward the financial ledger demonstrating rapid working capital velocity"
    },
    {
        "id": "CH03_SC032",
        "subject": "an international grain quality inspector in a white laboratory coat smiling approvingly as he inspects a handful of fragrant freshly milled Jasmine rice grains",
        "setting": "an import cargo receiving inspection laboratory at the Port of Manila under warm lighting",
        "text": None,
        "motion": "Close-up macro shot of fragrant pristine white rice grains held in the inspector hands"
    },
    {
        "id": "CH03_SC033",
        "subject": "a global maritime trade map illustrating rapid direct shipping corridors from Vietnam ports radiating across Southeast Asia, Africa, and the Americas in luminous amber",
        "setting": "an international maritime logistics coordination center under warm ambient display glow",
        "text": None,
        "motion": "Horizontal camera tracking shot scanning across the agile global rice logistics route map"
    },
    {
        "id": "CH03_SC034",
        "subject": "an official national agro-export contribution infographic at the Ministry of Agriculture showing the Mekong Delta commanding over ninety percent of all Vietnamese rice exports",
        "setting": "the central exhibition foyer of the Ministry of Agriculture and Rural Development in Hanoi",
        "text": "DBSCL: > 90% GAO XUAT KHAU",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the Mekong Delta >90% share map"
    },
    {
        "id": "CH03_SC035",
        "subject": "a bustling deepwater river wharf with ocean freighters moored under gantry cranes, an illuminated harbor telemetry board confirming annual export volume exceeding eight million tons",
        "setting": "the international export grain wharf at Cai Cui Port in Can Tho under bright sunny skies",
        "text": "XUAT KHAU: > 8 TRIEU TAN GAO/NAM",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the grain freighters loading"
    },
    {
        "id": "CH03_SC036",
        "subject": "the State Treasury and central banking archives documenting steady annual foreign exchange inflows generated by agricultural exports, strengthening the national sovereign reserve",
        "setting": "the macro-monetary research library at the State Bank of Vietnam under warm reading lights",
        "text": None,
        "motion": "Slow push-in shot toward the macroeconomic foreign reserve growth report"
    },
    {
        "id": "CH03_SC037",
        "subject": "a close-up perspective of compacted alluvial soil along an intensively farmed paddy dike, reflecting decades of continuous triple-cropping under a quiet brass sunset",
        "setting": "a high-intensity farming plot in the upper delta during the brief inter-crop window",
        "text": None,
        "motion": "Slow tracking macro shot across the dry compacted soil surface showing heavy cultivation wear"
    },
    {
        "id": "CH03_SC038",
        "subject": "authentic Vietnamese soil scientists analyzing core soil samples in an agro-chemistry laboratory, an analytical monitor warning of declining natural organic humus content",
        "setting": "the College of Agriculture soil science laboratory at Can Tho University under warm clean light",
        "text": None,
        "motion": "Slow push-in shot toward the soil organic carbon depletion warning chart"
    },
    {
        "id": "CH03_SC039",
        "subject": "a colossal upstream hydroelectric mega-dam on the upper Mekong River blocking downstream water flow, its massive reservoir trapping millions of tons of rich fine alluvial silt",
        "setting": "the mountainous canyon of the upper Mekong River under cool atmospheric haze with warm sunlight breaking through",
        "text": None,
        "motion": "Wide cinematic aerial shot revealing the massive upstream hydroelectric dam trapping river sediment"
    },
    {
        "id": "CH03_SC040",
        "subject": "an authentic Vietnamese farmer standing beside an eroded earthen riverbank, looking thoughtfully at the clearer river water lacking its traditional reddish alluvial silt color",
        "setting": "a riverbank along the Tien River during high water season under warm morning sun",
        "text": None,
        "motion": "Horizontal camera tracking shot past the farmer looking over the sediment-deprived river"
    },
    {
        "id": "CH03_SC041",
        "subject": "an authentic Vietnamese farmer wearing a conical hat scattering mineral NPK fertilizer grains across green rice shoots to sustain high crop yields",
        "setting": "an intensively cultivated rice field in An Giang under the warm rays of early morning sunlight",
        "text": None,
        "motion": "Slow tracking shot following the farmer rhythmically broadcasting fertilizer across the field"
    },
    {
        "id": "CH03_SC042",
        "subject": "a small wooden table in a rural farmer home covered with printed commercial fertilizer invoices and pesticide receipts, reflecting mounting seasonal input expenditures",
        "setting": "a humble countryside farmstead room under warm sunlight streaming through an open window",
        "text": None,
        "motion": "Slow push-in shot toward the stack of agricultural chemical input receipts"
    },
    {
        "id": "CH03_SC043",
        "subject": "a distinguished panel of regional scientists, agronomists, and provincial planners actively debating climate-adaptive structural transformations for the Mekong Delta",
        "setting": "a regional climate change adaptation conference hall in Can Tho under warm interior lighting",
        "text": None,
        "motion": "Horizontal camera tracking shot across the multidisciplinary policy roundtable"
    },
    {
        "id": "CH03_SC044",
        "subject": "a breathtaking panoramic view over boundless golden ripe rice panicles swaying gently in the morning breeze, glowing with vibrant warmth and natural resilience",
        "setting": "an expansive high-yield rice landscape in the Mekong Delta under luminous golden morning sunlight",
        "text": None,
        "motion": "Slow majestic aerial glide over the glistening sea of heavy ripe golden rice canopies"
    },
    {
        "id": "CH03_SC045",
        "subject": "an automated coastal tidal sluice gate facility with motorized hydraulic steel radial gates operating based on automated digital salinity sensor telemetry",
        "setting": "a modern salinity intrusion prevention water-control structure along the delta coast in warm sunlight",
        "text": None,
        "motion": "Slow push-in shot toward the automated hydraulic sluice gate control console"
    },
    {
        "id": "CH03_SC046",
        "subject": "a modern botanical research greenhouse where young authentic Vietnamese female geneticists meticulously perform manual cross-pollination on experimental salt-tolerant rice plants",
        "setting": "a high-tech plant breeding nursery greenhouse under bright natural sunlight",
        "text": None,
        "motion": "Macro close-up shot focusing on the delicate scientific manual cross-pollination of rice flowers"
    },
    {
        "id": "CH03_SC047",
        "subject": "a regional smart water-grid and agrarian supply-chain control room with wall-sized digital telemetry screens tracking real-time barge locations and canal river gauge levels",
        "setting": "the Mekong Delta Integrated Water and Grain Coordination Center under warm ambient light",
        "text": None,
        "motion": "Wide cinematic tracking shot across the computerized regional command and telemetry center"
    },
    {
        "id": "CH03_SC048",
        "subject": "a bustling riverside grain transfer depot with multiple automated conveyors pouring clean polished rice into river freight vessels and regional distribution trucks under bright morning sun",
        "setting": "a central grain logistics port hub on the Hau River under warm golden daylight",
        "text": None,
        "motion": "Horizontal camera tracking shot past bustling grain conveyors and loading river barges"
    },
    {
        "id": "CH03_SC049",
        "subject": "a peaceful sunlit morning street in Hanoi or Ho Chi Minh City with citizens enjoying traditional beef noodle soup and broken rice at street eateries before work",
        "setting": "a bustling and prosperous urban boulevard in Vietnam bathed in gentle warm morning daylight",
        "text": None,
        "motion": "Smooth wide cinematic glide over the tranquil and vibrant everyday urban morning street life"
    },
    {
        "id": "CH03_SC050",
        "subject": "an authentic Vietnamese family dinner table with parents and children sharing a steaming hot porcelain bowl of fragrant freshly cooked white rice under a warm dining lamp",
        "setting": "a warm and loving family dining room in a Vietnamese home under gentle amber lighting",
        "text": None,
        "motion": "Slow gentle push-in shot centering on the steaming warm bowl of fragrant white rice on the table"
    },
    {
        "id": "CH03_SC051",
        "subject": "an international trade research analyst in an academic study reviewing comparative research volumes documenting regional grain dependence and food security crises",
        "setting": "an international diplomatic research library under the warm illumination of reading lamps",
        "text": None,
        "motion": "Subtle camera glide across the comparative regional food security analytical dossiers"
    },
    {
        "id": "CH03_SC052",
        "subject": "a detailed geopolitical cartographic map of Southeast Asia with the Philippine archipelago highlighted prominently in luminous amber between the South China Sea and the Pacific",
        "setting": "a strategic regional geopolitical conference hall under warm architectural spotlighting",
        "text": None,
        "motion": "Slow forward camera glide toward the highlighted archipelago of the Philippines on the map"
    },
    {
        "id": "CH03_SC053",
        "ref": "irri_los_banos_gate.jpg",
        "subject": "the landmark entrance archway and institutional grounds of the International Rice Research Institute depicted in the reference photo, surrounded by lush tropical vegetation under warm afternoon sunlight",
        "setting": "the International Rice Research Institute campus in Los Baños Laguna Philippines",
        "text": "CAI NOI LUA GAO CHAU A (IRRI)",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the landmark IRRI gate"
    },
    {
        "id": "CH03_SC054",
        "subject": "an elevated urban highway overpass in Metro Manila overlooking former agricultural green paddies now backfilled with concrete debris for abandoned speculative housing developments",
        "setting": "an urbanized industrial periphery in Metro Manila under hazy warm afternoon sunshine",
        "text": None,
        "motion": "Slow camera tracking shot past abandoned speculative construction plots on former rice fields"
    },
    {
        "id": "CH03_SC055",
        "subject": "a commercial cargo vessel laden with bags of foreign imported rice unloading at Manila Harbor under a deep amber and crimson sunset sky",
        "setting": "the commercial piers of the Port of Manila looking out over Manila Bay at sunset",
        "text": None,
        "motion": "Slow pull-back camera shot framing the solitary imported rice cargo ship docked at sunset"
    }
]

lines = []
for sc in scenes:
    sc_id = sc["id"]
    ref_tag = sc.get("ref")
    subj = sc["subject"]
    setting = sc["setting"]
    text_overlay = sc["text"]
    motion = sc["motion"]
    
    if ref_tag:
        img_prompt = f"{sc_id} [IMAGE]: @{ref_tag} -> A 2D warm cinematic editorial illustration of {subj}, set in {setting}, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ambient tone (#FAF7EE), luminous warm golden daylight, soft ambient shadows"
    else:
        img_prompt = f"{sc_id} [IMAGE]: A 2D warm cinematic editorial illustration of {subj}, set in {setting}, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ambient tone (#FAF7EE), luminous warm golden daylight, soft ambient shadows"
        
    if text_overlay:
        img_prompt += f', compact subtle glowing golden amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading "{text_overlay}"'
        
    img_prompt += ", no watermarks, 16:9"
    
    if text_overlay:
        vid_prompt = f"{sc_id} [VIDEO]: @{sc_id}.png -> {motion}, preserving the 2D vector graphic novel aesthetic, clean ink outlines, and all static graphic layers of the reference image exactly without any character morphing or alterations, 8-second continuous documentary video --ar 16:9 --dur 8s"
    else:
        vid_prompt = f"{sc_id} [VIDEO]: @{sc_id}.png -> {motion}, preserving the 2D vector graphic novel aesthetic, clean ink outlines, and all details of the reference image exactly, 8-second continuous documentary video --ar 16:9 --dur 8s"
        
    lines.append(img_prompt)
    lines.append(vid_prompt)
    lines.append("") # single blank line between scenes

content = "\n".join(lines).strip() + "\n"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Generated {len(scenes)} scenes to: {output_path}")
