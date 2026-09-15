from pathlib import Path
import json

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
out_prompts = ep_dir / "prompts_chapter_06.txt"
out_visual = ep_dir / "chapter_06_visual.md"

STYLE = "A 2D warm cinematic editorial illustration in high-prestige corporate noir luxury aesthetic. Somber raw slate tones (#1E2229), dark industrial charcoal (#252A34), and brushed titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field"

prompts = []

def add_scene(img_prompt, vid_prompt):
    prompts.append(f"[IMAGE] {img_prompt.strip()}\n[VIDEO] {vid_prompt.strip()} --ar 16:9 --dur 8s")

# CH06_SC001
add_scene(
    f"{STYLE}. An expansive automotive showroom at night. Polished dark obsidian floor, elegant dark walnut paneling, and warm directional ceiling spotlights gleaming softly off luxury vehicle contours. Outside the floor-to-ceiling glass windows lies an industrial city silhouette under a moody twilight.",
    "Slow tracking shot gliding past the polished flanks of display vehicles toward the dark window overlooking the industrial district"
)

# CH06_SC002
add_scene(
    f"{STYLE}. A heavy dark mahogany desk in a financial audit archive. A heavy brass desk clock rests beside an open leather-bound corporate audit ledger stamped with official corporate seals, illuminated by a warm brass desk lamp casting long velvety shadows.",
    "Slow camera push-in dolly shot toward the open leather audit ledger resting under the warm desk lamp"
)

# CH06_SC003
add_scene(
    f"{STYLE}. A dimly lit corporate intelligence office at night. A senior economic analyst in a dark charcoal waistcoat turns away from glowing wall monitors displaying chaotic social media feeds to open a thick physical corporate filing on a dark oak credenza.",
    "Slow camera pan across the dimly lit research office as the analyst reaches for a thick printed corporate file"
)

# CH06_SC004
add_scene(
    f"{STYLE}. A dramatic visual transition from forensic paperwork to industrial reality. In the crisp foreground rests an open audited balance sheet with detailed financial columns, while the background reveals a vast automotive assembly plant with warm high-bay lights cutting through light atmospheric haze.",
    "Slow focus pull shifting smoothly from the crisp lines of the audited financial binder in the foreground to the vast factory floor in the background"
)

# CH06_SC005
add_scene(
    f"{STYLE}. A vast manufacturing campus in Shenzhen at dawn. Towering multi-story employee dormitory buildings flanking wide industrial avenues under amber morning mist, silhouetted against a deep slate morning sky.",
    "Slow high-angle crane shot descending over the vast corporate manufacturing campus as dawn light breaks through the haze"
)

# CH06_SC006
add_scene(
    f"{STYLE}. An immense shift change at the Pingshan Shenzhen industrial complex. Hundreds of industrial technicians in dark blue company uniforms and safety badges walking methodically through security turnstiles under warm sodium lights. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'GLOBAL HEADCOUNT: 968,900 EMPLOYEES'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC007
add_scene(
    f"{STYLE}. A large comparative industrial chart engraved on a dark slate wall inside a corporate conference suite. Outlines of Toyota, General Motors, and Ford employee counts combined against a single massive workforce column highlighted in warm golden amber. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'HEADCOUNT: BYD > TOYOTA + GM + FORD'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC008
add_scene(
    f"@ceo_byd_wangchuanfu.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The subject is dressed in dark executive business attire and wire-rimmed glasses, standing beside an engineering assembly station and observing technicians with focused leadership.",
    "Steady camera shot focusing on the founder observing the production line, maintaining their composed facial expression and all details of the reference image exactly"
)

# CH06_SC009
add_scene(
    f"{STYLE}. Inside a dense automotive electrical wiring assembly station. Long rows of skilled technicians in clean blue work coats meticulously routing wiring harnesses and battery module connections by hand on precision wooden jigs under warm tungsten task lamps.",
    "Slow tracking shot gliding along the manual assembly benches as technicians perform precision mechanical wiring with deft movements"
)

# CH06_SC010
add_scene(
    f"{STYLE}. An executive briefing room with dual high-resolution data monitors displaying labor productivity metrics. Polished dark walnut conference table, warm recessed spotlights, and an economist reviewing comparative revenue per worker curves.",
    "Slow camera push-in dolly shot toward the central financial display in the executive briefing suite"
)

# CH06_SC011
add_scene(
    f"{STYLE}. A stark financial comparison chart on a brushed titanium plaque on a mahogany wall. Two vertical columns comparing annual revenue generated per employee, showing Toyota at eight hundred fifty thousand dollars and the challenger at one hundred forty thousand dollars. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'REVENUE PER EMPLOYEE: BYD (1/6) VS TOYOTA'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC012
add_scene(
    f"{STYLE}. A bustling domestic automotive manufacturing floor in Guangdong circa twenty fifteen. Dense lines of assembly operators working in close rhythm alongside overhead chain hoists under warm industrial bay lighting.",
    "Slow lateral tracking shot alongside the busy domestic production line under warm industrial lighting"
)

# CH06_SC013
add_scene(
    f"{STYLE}. An executive boardroom table covered with international labor agreements and foreign currency ledgers. Corporate red ink circles international wage rates and mandatory statutory pension costs on cream ledger paper under a brass reading lamp.",
    "Slow camera push-in dolly shot toward the international operating cost ledger on the polished wood table"
)

# CH06_SC014
add_scene(
    f"{STYLE}. A bright modern administrative office in Western Europe. A European corporate HR director in a charcoal blazer reviewing statutory social benefit schedules and collective wage tables spread across a clean desk under soft daylight.",
    "Slow camera pan across the desk displaying European labor compliance documentation"
)

# CH06_SC015
add_scene(
    f"{STYLE}. A formal labor negotiation room in a European automotive assembly plant. Local trade union representatives in dark suits seated across the table, maintaining resolute postures while pointing to an official shift roster ending strictly at four thirty in the afternoon.",
    "Steady camera shot capturing the solemn negotiation table with union delegates standing firm on working hour limits"
)

# CH06_SC016
add_scene(
    f"{STYLE}. A massive industrial stamping die resting on heavy steel skids inside an overseas satellite assembly hall. Heavy polished steel press tools highlighted by sharp directional golden lighting against quiet factory shadows.",
    "Slow low-angle tracking shot gliding past the monumental steel stamping die resting in the quiet overseas factory hall"
)

# CH06_SC017
add_scene(
    f"{STYLE}. An immense automotive stamping and body plant in China. Hundreds of stamped white vehicle bodies moving continuously on overhead conveyor tracks extending toward the horizon under bright amber factory lights. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CHINA SCALE: MILLIONS OF UNITS / SPREAD TOOLING'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC018
add_scene(
    f"{STYLE}. An overseas assembly facility in Brazil or Hungary. A quiet, orderly workshop with only a modest line of vehicle bodies on rolling floor dollies under clean warm overhead lighting, revealing limited local production volume.",
    "Slow camera tracking shot down the sparse assembly line in the overseas satellite facility"
)

# CH06_SC019
add_scene(
    f"{STYLE}. An executive cost accounting ledger displayed on a dark glass computer screen. A unit depreciation curve rises steeply as production volume decreases, showing fixed tooling amortization per vehicle ballooning sharply. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TOOLING DEPRECIATION: SURGING PER OVERSEAS UNIT'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC020
add_scene(
    f"{STYLE}. An executive corner office at dusk. A corporate chief risk officer in a dark suit stands beside a floor-to-ceiling glass window, holding an audited cash statement marked with red ink, looking out over an industrial city skyline in deep contemplation.",
    "Slow push-in dolly shot toward the executive silhouetted against the amber city dusk"
)

# CH06_SC021
add_scene(
    f"{STYLE}. A dimly lit corporate records archive. Rows of tall industrial shelving holding thick black binders labeled Supplier Acceptance Notes and Commercial Payables, illuminated by warm amber corridor lighting cutting through soft dust motes.",
    "Slow tracking shot moving through the archive corridor past rows of commercial payable binders"
)

# CH06_SC022
add_scene(
    f"{STYLE}. A forensic financial accounting chart on a clipboard resting on a dark slate conference table. A horizontal timeline graph highlights Days Payable Outstanding extended to one hundred and fifty-five days in deep warning red. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'DAYS PAYABLE OUTSTANDING: 155 DAYS'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC023
add_scene(
    f"{STYLE}. A tidy, disciplined accounts office in Toyota City. An official supplier remittance advice on clean ivory paper stamped with a formal red corporate seal indicating payment settlement in forty-five days. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TOYOTA PAYMENT CYCLE: ~45 DAYS'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC024
add_scene(
    f"{STYLE}. An expansive automotive supply chain industrial park in Jiangsu. The exterior facades of component manufacturing plants producing steering racks, brake calipers, and stamped brackets under late evening industrial amber lamps.",
    "Slow cinematic tracking shot gliding past the exterior facades of specialized auto component vendor factories"
)

# CH06_SC025
add_scene(
    f"{STYLE}. A side-by-side analytical composition on a dark walnut table. On the left, an open vendor invoice ledger with ninety-day and one-hundred-twenty-day deferred payment notes; on the right, glossy consumer brochures advertising aggressive retail cash discounts on electric vehicles.",
    "Slow camera pan from the supplier invoice ledger across to the retail discount showroom brochures"
)

# CH06_SC026
add_scene(
    f"{STYLE}. A formal government regulatory council chamber in Beijing. Senior financial regulators in dark tailored business suits seated along a dark mahogany table, reviewing printed industrial market stability directives under warm recessed ceiling lighting.",
    "Slow camera push-in dolly shot toward the formal regulatory directive on the mahogany council table"
)

# CH06_SC027
add_scene(
    f"{STYLE}. An official printed regulatory decree from Chinese industrial authorities on heavy cream paper bearing an official red governmental seal. Crisp black characters set forth a strict sixty-day limit on enterprise supplier payment settlement. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'MANDATORY REGULATORY CAP: 60-DAY SUPPLIER PAYMENT'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC028
add_scene(
    f"{STYLE}. A treasury trading room in a commercial banking tower. Multiple dual-monitor workstations displaying corporate cash flow indicators and liquidity metrics turning downward under focused desk lighting.",
    "Slow camera push-in shot toward the treasury management monitor displaying liquidity adjustments"
)

# CH06_SC029
add_scene(
    f"{STYLE}. A corporate financial cash flow chart displayed on an executive tablet. A large column indicates operating cash flow reaching eighty-two billion yuan in early twenty twenty-three highlighted in warm amber. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'H1 OPERATING CASH FLOW: 82B YUAN ($11.4B)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC030
add_scene(
    f"{STYLE}. The same corporate cash flow chart showing operating cash flow plummeting to just fourteen billion yuan in early twenty twenty-four, highlighted in deep warning crimson. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'CASH FLOW PLUNGE: TO 14B YUAN (-83%)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC031
add_scene(
    f"{STYLE}. A colossal vehicle storage marshalling yard at dusk. Tens of thousands of newly manufactured electric cars parked in vast, disciplined rows stretching to the horizon under an overcast slate-grey sky. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'RECORD INVENTORY: >160 BILLION YUAN ($22B+)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC032
add_scene(
    f"{STYLE}. A senior automotive executive seated at a dark desk late at night, reviewing vehicle retail price sheets alongside the official government supplier payment decree. A warm desk lamp reflects off the executive's furrowed brow.",
    "Slow camera push-in dolly shot toward the executive caught between price-war demands and cash constraints"
)

# CH06_SC033
add_scene(
    f"{STYLE}. A global maritime and trade logistics map spread across an executive boardroom table. Amber trade corridors across the Pacific and Atlantic marked with red hazard symbols indicating trade restrictions and port delays.",
    "Slow camera tracking shot across the strategic supply chain map on the boardroom table"
)

# CH06_SC034
add_scene(
    f"{STYLE}. A cleanroom semiconductor engineering workstation. A technician in a dark anti-static coat uses a digital microscope to inspect an advanced automotive computing chip mounted on a printed circuit board, illuminated by warm amber fiber-optic lights.",
    "Slow macro push-in camera shot toward the central semiconductor processor mounted on the automotive circuit board"
)

# CH06_SC035
add_scene(
    f"{STYLE}. An undeveloped industrial plot in Nuevo Leon Mexico at dusk. A solitary surveyor tripod stands among desert scrub on dry ground, silhouetted against a dramatic crimson and amber evening sky. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'MEXICO PLANT: SHELVED INDEFINITELY'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC036
add_scene(
    f"{STYLE}. An after-sales customer service counter at an automotive dealership in suburban Europe. Stacks of pending work orders and vehicle repair logs arranged on a dark counter under soft commercial lighting.",
    "Slow tracking shot along the dealership service counter displaying pending customer repair tickets"
)

# CH06_SC037
add_scene(
    f"{STYLE}. A dealership mechanical workshop where a modern electric car rests elevated on a hydraulic hoist with its front bumper and headlight removed, awaiting replacement components. A wall calendar shows circled dates marking ninety days. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'PARTS WAIT TIME: 2-3 MONTHS FROM SHENZHEN'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC038
add_scene(
    f"{STYLE}. An insurance underwriting desk in London. A commercial auto risk assessment file stamped with red ink indicating steep premium increases and policy exclusions for battery electric vehicles resting on a polished oak desk under a warm lamp.",
    "Slow camera push-in dolly shot toward the formal insurance risk assessment report"
)

# CH06_SC039
add_scene(
    f"{STYLE}. An expansive pre-owned automotive sales lot at twilight. Rows of late-model electric vehicles parked under tall amber yard floodlights, wet asphalt reflecting rich amber and charcoal shadows.",
    "Slow camera dolly glide between rows of parked used vehicles under amber dealership floodlights"
)

# CH06_SC040
add_scene(
    f"{STYLE}. The glass window of a pre-owned car showroom displaying marked-down price banners with downward red arrows indicating severe secondary market price drops on recent electric vehicle models.",
    "Slow tracking shot past dealership window price tags showing steep secondary market discounts"
)

# CH06_SC041
add_scene(
    f"{STYLE}. A three-year-old electric sedan parked along a quiet tree-lined suburban street at dusk, raindrops glistening across its hood under the warm golden glow of a streetlamp.",
    "Slow cinematic pan along the sleek profile of the three-year-old electric vehicle in twilight rain"
)

# CH06_SC042
add_scene(
    f"{STYLE}. A formal vehicle valuation certificate on a clipboard on a dealer desk. A graph illustrates vehicle value plunging by forty-five percent over thirty-six months. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'EV RESALE VALUE: -40% TO -50% IN 3 YEARS'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC043
add_scene(
    f"{STYLE}. A sturdy charcoal metallic Toyota Hilux pickup truck parked solidly on an elevated gravel ridge at sunset. An appraisal graphic confirms high residual value retention. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'TOYOTA HILUX RESALE: 75% - 80% RETAINED'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC044
add_scene(
    f"{STYLE}. An automotive diagnostic facility. A large high-voltage lithium battery pack removed from an electric vehicle sits on an insulated hydraulic lift table, illuminated by sharp overhead tungsten inspection lamps.",
    "Slow low-angle tracking shot moving past the exposed modular battery enclosure on the hydraulic lift"
)

# CH06_SC045
add_scene(
    f"{STYLE}. An official manufacturer warranty handbook resting on a dark wood table, open to the final limitation page marked with a red expiration stamp, beside vehicle keys and an ownership title.",
    "Slow camera push-in dolly shot toward the expired warranty document and brass stamp"
)

# CH06_SC046
add_scene(
    f"{STYLE}. A formal dealership service estimate invoice on clean paper. A highlighted line item displays a replacement battery pack quoted at twelve thousand five hundred dollars against a total vehicle value of twenty-five thousand dollars. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'BATTERY REPLACEMENT: UP TO 50% OF CAR VALUE'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC047
add_scene(
    f"{STYLE}. An independent used car dealer proprietor standing outside his sales office at dusk, shaking his head and politely declining a customer seeking to trade in an out-of-warranty electric car.",
    "Steady medium shot capturing the independent dealer declining the used electric vehicle trade-in"
)

# CH06_SC048
add_scene(
    f"{STYLE}. A family kitchen table late in the evening. A homeowner in a warm knitted sweater sits with a calculator, a notepad, and utility bills under a soft overhead pendant light, carefully totaling monthly household transport expenses.",
    "Slow camera push-in shot toward the family kitchen table as the homeowner reviews handwritten fuel savings versus resale losses"
)

# CH06_SC049
add_scene(
    f"{STYLE}. Close-up of the homeowner's handwritten calculations on a notepad under the warm pendant lamp. A neat entry records monthly fuel savings of one hundred and twenty dollars. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'FUEL SAVINGS: ~$120 / MONTH'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC050
add_scene(
    f"{STYLE}. The homeowner's financial ledger displaying a side-by-side calculation. Three years of accumulated fuel savings totaling four thousand three hundred dollars compared against a fourteen thousand dollar resale depreciation loss highlighted in red ink. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'RESALE LOSS: $14,000 > FUEL SAVINGS: $4,300'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC051
add_scene(
    f"{STYLE}. An analytical macro risk matrix on a dark obsidian glass wall in a financial think-tank. Four highlighted risk vectors: Workforce Payroll, Supplier Credit Cap, Silicon Dependence, and Resale Depreciation, glowing softly in warning crimson.",
    "Slow camera push-in shot toward the four convergent risk nodes on the dark glass matrix"
)

# CH06_SC052
add_scene(
    f"{STYLE}. An aerial twilight vista of an immense automotive factory complex. Long dramatic shadows stretch across sprawling industrial roofs, while a single warm light burns in the top-floor executive suite.",
    "Slow cinematic drone shot pulling back from the industrial headquarters tower into the darkening twilight"
)

# CH06_SC053
add_scene(
    f"{STYLE}. A cinematic visual composition contrasting industrial momentum with financial liability. An ultra-fast assembly line with robotic arms in motion balanced against a heavy steel filing cabinet overflowing with deferred supplier accounts.",
    "Slow steady camera glide across the dual realities of rapid production speed and deferred financial obligations"
)

# CH06_SC054
add_scene(
    f"{STYLE}. A quiet commercial vehicle storage compound at sunset. Rows of depreciated electric cars resting quietly with dust on their windscreens under a moody violet-slate evening sky.",
    "Slow camera tracking shot skimming low past the line of depreciated electric cars parked in the quiet lot"
)

# CH06_SC055
add_scene(
    f"{STYLE}. A powerful architectural documentary visual. Massive concrete foundation pillars of an industrial complex anchored in shifting desert sand dunes under a dramatic setting sun, representing structural vulnerability beneath immense scale.",
    "Slow camera tilt-up from the shifting sand at the base to the towering concrete industrial pillars above"
)

# CH06_SC056
add_scene(
    f"@chairman_toyota_akiotoyoda.jpg -> {STYLE}. The person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The chairman is dressed in a dark bespoke business suit, standing in a serene, dignified posture in an executive suite overlooking Nagoya at dusk, exuding patient strategic confidence.",
    "Steady camera shot focusing on the chairman's composed posture, maintaining all details of the reference image exactly"
)

# CH06_SC057
add_scene(
    f"{STYLE}. A private executive boardroom and treasury suite in Toyota City. An official financial report on dark polished cedar displays liquid reserves totaling five point three trillion yen, equivalent to thirty-four billion US dollars. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'LIQUID CASH MOUNTAIN: $34 BILLION USD (5.3T YEN)'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# CH06_SC058
add_scene(
    f"{STYLE}. A high-tech confidential R&D laboratory in Higashi-Fuji Japan. Japanese automotive research engineers in white cleanroom suits and protective eyewear examine an advanced solid-state battery cell prototype resting under precision golden-white laboratory spotlights.",
    "Slow camera push-in dolly shot toward the scientists examining the solid-state battery cell prototype under cleanroom lights"
)

# CH06_SC059
add_scene(
    f"{STYLE}. A dramatic visual juxtaposition. In the crisp foreground, a compact solid-state battery module gleams with sophisticated platinum-gold illumination; in the distant moody background, silhouettes of sprawling liquid-battery gigafactories stand beneath a stormy twilight sky. Bold typography positioned fixedly in the lower-left area 25% above the bottom edge reading 'NEXT: THE SOLID-STATE COUNTER-STRIKE'.",
    "Steady camera shot with subtle slow push-in, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations"
)

# Write prompts file
out_prompts.write_text("\n\n".join(prompts) + "\n", encoding="utf-8")
print(f"Generated {len(prompts)} scenes in {out_prompts.name}")

# Now generate chapter_06_visual.md
with open(ep_dir / "scene_timing_map.json") as f:
    timing_data = json.load(f)

ch06_scenes = [s for s in timing_data if s.get("chapter") == "06"]

visual_header = """<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/byd-vs-toyota-no-america-strategy/chapter_06_visual.md
- Activated Personas: The Master Cinematic Visual Director (.agents/personas/the_visual_storyteller.md) & The Scene Architect (.agents/personas/the_scene_architect.md)
- Activated Skills: visual-prompter (.agents/skills/visual_prompter/SKILL.md) & scene-timing-builder (.agents/skills/scene_timing_builder/SKILL.md)
- Source Documents Consulted:
  * episodes/byd-vs-toyota-no-america-strategy/chapter_06.md
  * episodes/byd-vs-toyota-no-america-strategy/scene_timing_map.json
  * episodes/byd-vs-toyota-no-america-strategy/visual_storyboard_blueprint.md
  * episodes/byd-vs-toyota-no-america-strategy/prompts_chapter_06.txt
- Art Direction Mandate: "Màu sắc ấm, trầm, sâu, và có tính sang trọng uy tín cao" (User-Directed Aesthetic)
- Execution Timestamp: 2026-09-13 10:45
-->

# Chapter 06 Visual Script — The One-Million Worker Dilemma

Bản kịch bản phân đoạn thị giác chi tiết cho Chương 6 (The One-Million Worker Dilemma: Efficiency, Exploitation, and the Brutal Mechanics of Scale), đồng bộ toán học 1-1 với 59 phân cảnh trong `scene_timing_map.json` và tệp prompt `prompts_chapter_06.txt`.

- **Vũ trụ Mỹ thuật:** Forensic Economic Audit & Industrial Scale Vulnerability.
- **Bảng màu Sâu lắng & Sang trọng:** Somber Raw Slate (`#1E2229`), Dark Industrial Charcoal (`#252A34`), Weathered Industrial Grey (`#4A505A`), Deep Warning Red (`#B71C1C` / `#8B0000`), Luminous Amber (`#F59E0B`), Imperial Champagne Gold (`#D4AF37`), Warm Ivory Cream (`#FAF7EE`).
- **Ánh sáng:** Luminous Low-Key Editorial Lighting, Directional Warm Tungsten Rim Lights, Velvety Deep Shadows, 35mm Film Grain.
- **Quy tắc Typography:** Chỉ xuất hiện ở ~20-30% cảnh mấu chốt, định vị góc dưới bên trái cách mép đáy 25%.

---

| Mã Scene | Thời Lượng | Câu Thoại Tiếng Anh Gốc | Bối Cảnh Vật Lý Đời Thường & Hành Động Điện Ảnh | Text Overlay (Lower-Left 25%) | Luồng Tạo Hình |
| :---: | :---: | :--- | :--- | :--- :---: | :---: |
"""

text_overlays_ch06 = {
    "CH06_SC006": "GLOBAL HEADCOUNT: 968,900 EMPLOYEES",
    "CH06_SC007": "HEADCOUNT: BYD > TOYOTA + GM + FORD",
    "CH06_SC011": "REVENUE PER EMPLOYEE: BYD (1/6) VS TOYOTA",
    "CH06_SC017": "CHINA SCALE: MILLIONS OF UNITS / SPREAD TOOLING",
    "CH06_SC019": "TOOLING DEPRECIATION: SURGING PER OVERSEAS UNIT",
    "CH06_SC022": "DAYS PAYABLE OUTSTANDING: 155 DAYS",
    "CH06_SC023": "TOYOTA PAYMENT CYCLE: ~45 DAYS",
    "CH06_SC027": "MANDATORY REGULATORY CAP: 60-DAY SUPPLIER PAYMENT",
    "CH06_SC029": "H1 OPERATING CASH FLOW: 82B YUAN ($11.4B)",
    "CH06_SC030": "CASH FLOW PLUNGE: TO 14B YUAN (-83%)",
    "CH06_SC031": "RECORD INVENTORY: >160 BILLION YUAN ($22B+)",
    "CH06_SC035": "MEXICO PLANT: SHELVED INDEFINITELY",
    "CH06_SC037": "PARTS WAIT TIME: 2-3 MONTHS FROM SHENZHEN",
    "CH06_SC042": "EV RESALE VALUE: -40% TO -50% IN 3 YEARS",
    "CH06_SC043": "TOYOTA HILUX RESALE: 75% - 80% RETAINED",
    "CH06_SC046": "BATTERY REPLACEMENT: UP TO 50% OF CAR VALUE",
    "CH06_SC049": "FUEL SAVINGS: ~$120 / MONTH",
    "CH06_SC050": "RESALE LOSS: $14,000 > FUEL SAVINGS: $4,300",
    "CH06_SC057": "LIQUID CASH MOUNTAIN: $34 BILLION USD (5.3T YEN)",
    "CH06_SC059": "NEXT: THE SOLID-STATE COUNTER-STRIKE"
}

visual_descs_ch06 = {
    "CH06_SC001": "Showroom ô tô sang trọng rực rỡ lúc nửa đêm, ánh đèn spotlight vàng ấm hắt lên thân xe, đối lập với bóng tối khu công nghiệp bên ngoài cửa kính.",
    "CH06_SC002": "Bàn làm việc mahogany nặng trịch tại văn phòng kiểm toán, chiếc đồng hồ để bàn bằng đồng tích tắc bên cạnh cuốn sổ cái đóng dấu niêm phong đỏ.",
    "CH06_SC003": "Văn phòng phân tích tài chính mờ tối ban đêm, chuyên gia quay lưng lại với màn hình mạng xã hội để mở tập hồ sơ kiểm toán in giấy dày cộp.",
    "CH06_SC004": "Sự chuyển tiếp từ trang giấy sang nhà xưởng: tiền cảnh là bảng cân đối kế toán được kiểm toán, hậu cảnh mở ra sàn lắp ráp cơ khí rộng lớn.",
    "CH06_SC005": "Toàn cảnh trên cao đại tổ hợp sản xuất tại Thâm Quyến trong sương sớm, các dãy ký túc xá nhiều tầng trải dài dọc các đại lộ công nghiệp.",
    "CH06_SC006": "Dòng người công nhân gần 1 triệu người tan ca tại tổ hợp Bình Sơn Thâm Quyến, đồng phục xanh bước qua cổng kiểm soát an ninh dưới ánh đèn vàng.",
    "CH06_SC007": "Biểu đồ so sánh nhân sự khắc trên tường đá phiến phòng họp: Quy mô lao động của BYD vượt qua tổng nhân sự của cả Toyota, GM và Ford cộng lại.",
    "CH06_SC008": "Nhà sáng lập Vương Truyền Phúc trong trang phục vest tối màu và kính cận, đứng cạnh bàn thao tác cơ khí quan sát dây chuyền sản xuất với vẻ tập trung.",
    "CH06_SC009": "Xưởng lắp ráp dây dẫn điện tử thủ công, các kỹ sư lành nghề dùng tay đi dây và đấu nối cụm pin cẩn trọng trên bàn gá gỗ dưới đèn bàn ấm.",
    "CH06_SC010": "Phòng họp điều hành với màn hình hiển thị nghịch lý năng suất: phân tích đồ thị doanh thu trên mỗi đầu người giữa các hãng xe.",
    "CH06_SC011": "Biểu đồ doanh thu trên mỗi nhân viên: Toyota đạt 850.000 USD/người, trong khi BYD chỉ đạt 140.000 USD/người (tương đương 1/6 mức của đối thủ).",
    "CH06_SC012": "Nhà xưởng sản xuất tại Quảng Đông giai đoạn 2015, mật độ công nhân dày đặc làm việc nhịp nhàng, minh chứng cho lợi thế nhân công giá rẻ nội địa.",
    "CH06_SC013": "Bàn họp quốc tế trải các văn bản luật lao động nước ngoài, mực đỏ khoanh vùng chi phí lương và bảo hiểm xã hội tăng vọt khi mở rộng ra nước ngoài.",
    "CH06_SC014": "Văn phòng hành chính hiện đại tại Tây Âu, giám đốc nhân sự châu Âu duyệt bảng thang bảng lương tối thiểu và các chế độ phúc lợi bắt buộc.",
    "CH06_SC015": "Phòng đàm phán thỏa ước lao động tại châu Âu, đại diện công đoàn địa phương giữ vẻ mặt kiên quyết, chỉ vào chiếc đồng hồ chỉ đúng 16h30 hết ca.",
    "CH06_SC016": "Khuôn dập thép cơ khí khổng lồ đặt trên bệ đỡ nhà máy vệ tinh ở nước ngoài, khối thép bóng loáng nằm im lìm trong ánh đèn vàng tĩnh lặng.",
    "CH06_SC017": "Dây chuyền dập hàng triệu vỏ xe tại Trung Quốc chạy liên tục trên ray treo trên cao, chi phí khấu hao khuôn dập được dàn phẳng trên quy mô khổng lồ.",
    "CH06_SC018": "Xưởng lắp ráp vệ tinh tại Brazil hoặc Hungary, sản lượng khiêm tốn khiến chỉ có vài thân xe nằm rải rác trên sàn lắp ráp dưới ánh đèn LED sạch sẽ.",
    "CH06_SC019": "Màn hình hạch toán chi phí khấu hao khuôn dập trên mỗi đầu xe tăng vọt từ 300 USD tại Trung Quốc lên hơn 2.500 USD tại nhà máy nước ngoài.",
    "CH06_SC020": "Góc văn phòng lãnh đạo lúc hoàng hôn, giám đốc quản trị rủi ro đứng trầm ngâm nhìn qua cửa kính xuống thành phố với bản báo cáo tài chính trên tay.",
    "CH06_SC021": "Hành lang kho lưu trữ hồ sơ công nợ, các kệ sắt xếp đầy các tập chứng từ chấp nhận thanh toán và hóa đơn nhà cung cấp mờ ảo trong ánh đèn hành lang.",
    "CH06_SC022": "Biểu đồ kiểm toán tài chính làm nổi bật số ngày phải trả nhà cung cấp (DPO) bị kéo giãn lên mức kỷ lục 155 ngày bằng đường nét đỏ cảnh báo.",
    "CH06_SC023": "Bàn làm việc kế toán ngăn nắp tại Thành phố Toyota, chứng từ chuyển tiền cho nhà cung cấp đóng dấu xác nhận thanh toán gọn gàng trong 45 ngày.",
    "CH06_SC024": "Khu công nghiệp phụ trợ tại Giang Tô, các nhà máy gia công linh kiện phanh, dập thân vỏ và dây điện sáng đèn tăng ca trong sự căng thẳng công nợ.",
    "CH06_SC025": "Bố cục đối chiếu: bên trái là sổ công nợ nhà cung cấp bị hoãn thanh toán, bên phải là tờ rơi quảng cáo giảm giá sốc kích cầu người mua xe.",
    "CH06_SC026": "Phòng họp hội đồng quản lý thị trường tại Bắc Kinh, các quan chức cơ quan điều hành duyệt văn bản chấn chỉnh kỷ luật thanh toán doanh nghiệp.",
    "CH06_SC027": "Văn bản quy định bắt buộc đóng dấu đỏ của cơ quan quản lý Trung Quốc, áp trần thời hạn thanh toán cho nhà cung cấp không quá 60 ngày.",
    "CH06_SC028": "Sàn giao dịch ngân quỹ doanh nghiệp, các màn hình theo dõi dòng tiền thanh khoản hiển thị các chỉ số tài chính sụt giảm đột ngột.",
    "CH06_SC029": "Biểu đồ dòng tiền hoạt động nửa đầu năm 2023 đạt mức gần 82 tỷ nhân dân tệ (khoảng 11,4 tỷ USD) với cột biểu đồ màu vàng hổ phách.",
    "CH06_SC030": "Cột dòng tiền hoạt động nửa đầu năm 2024 lao dốc thẳng đứng xuống chỉ còn 14 tỷ nhân dân tệ (giảm hơn 80%) hiển thị trong sắc đỏ cảnh báo.",
    "CH06_SC031": "Bãi tập kết logistics mênh mông chứa hàng chục ngàn xe điện mới xuất xưởng nằm chờ giao, phản ánh lượng hàng tồn kho kỷ lục vượt 160 tỷ nhân dân tệ.",
    "CH06_SC032": "Lãnh đạo doanh nghiệp ngồi trước bàn làm việc đêm muộn, kẹt giữa áp lực giảm giá cạnh tranh và lệnh siết chặt hạn mức tín dụng nhà cung cấp.",
    "CH06_SC033": "Bản đồ chuỗi cung ứng toàn cầu trải trên bàn họp, các tuyến vận tải biển và đường bộ xuất hiện các biểu tượng cảnh báo hàng rào thuế quan.",
    "CH06_SC034": "Phòng lab kiểm thử vi mạch, kỹ sư soi kính hiển vi kiểm tra chip xử lý buồng lái thông minh do phương Tây sản xuất gắn trên bo mạch điện tử.",
    "CH06_SC035": "Khu đất dự án nhà máy tại Nuevo León Mexico lúc hoàng hôn, chân máy đo đạc trắc địa cô đơn đứng giữa bãi đất hoang vì dự án bị đình chỉ vô thời hạn.",
    "CH06_SC036": "Quầy tiếp nhận dịch vụ sau bán hàng tại đại lý hải ngoại, các tập hồ sơ xe chờ sửa chữa và phụ tùng thay thế xếp chồng dưới ánh đèn thương mại.",
    "CH06_SC037": "Xưởng sửa chữa đại lý, chiếc xe điện nằm nâng trên cầu nâng thủy lực tháo rời cản trước, chờ đợi phụ tùng chuyển từ Thâm Quyến trong 2-3 tháng.",
    "CH06_SC038": "Bàn thẩm định bảo hiểm tại London, hồ sơ đánh giá rủi ro xe điện bị đóng dấu đỏ từ chối cấp đơn bảo hiểm hoặc tăng phí bảo hiểm ngất ngưởng.",
    "CH06_SC039": "Bãi xe ô tô cũ thương mại lúc chập tối, hàng dài xe điện đã qua sử dụng đỗ im lìm dưới ánh đèn cao áp phản chiếu mặt nhựa đường ướt.",
    "CH06_SC040": "Cửa kính showroom đại lý xe cũ dán biển giảm giá sâu kèm mũi tên đỏ chỉ xuống, phản ánh làn sóng mất giá của xe điện đã qua sử dụng.",
    "CH06_SC041": "Chiếc xe điện 3 năm tuổi đỗ bên lề đường khu đô thị lúc chạng vạng trong màn mưa phùn, nước mưa đọng trên nắp ca-pô dưới ánh đèn đường.",
    "CH06_SC042": "Chứng thư định giá xe cũ trên bàn thẩm định, đồ thị giá trị xe sụt giảm 40% đến 50% chỉ sau 2 đến 3 năm lăn bánh.",
    "CH06_SC043": "Chiếc bán tải Toyota Hilux màu xám kim loại đỗ vững chãi trên mỏm đồi đá dăm lúc hoàng hôn, bảng định giá giữ lại 75% đến 80% giá trị ban đầu.",
    "CH06_SC044": "Xưởng kỹ thuật cơ điện, khối pin lithium cao áp được tháo rời khỏi khung gầm xe, đặt trên bàn nâng thủy lực cách điện dưới ánh đèn soi kiểm tra.",
    "CH06_SC045": "Cuốn sổ tay bảo hành chính hãng mở ra trang cuối cùng đóng dấu hết hạn bảo hiểm pin, đặt cạnh chìa khóa xe trên bàn làm việc gỗ tối màu.",
    "CH06_SC046": "Hóa đơn báo giá thay cụm pin mới của đại lý chính hãng, con số chi phí thay pin lên tới 12.500 USD, chiếm gần một nửa giá trị chiếc xe mới.",
    "CH06_SC047": "Chủ salon xe cũ độc lập đứng trước văn phòng lúc hoàng hôn, xua tay từ chối mua lại chiếc xe điện đã hết hạn bảo hành vì rủi ro chai pin.",
    "CH06_SC048": "Bàn ăn gia đình trung lưu ban đêm, người chủ xe ngồi bấm máy tính và đối chiếu hóa đơn điện, xăng dưới ánh đèn thả ấm áp.",
    "CH06_SC049": "Cận cảnh trang giấy ghi chép chi phí sinh hoạt của chủ xe, con số tiết kiệm nhiên liệu hàng tháng khoảng 120 USD dưới ánh đèn bàn.",
    "CH06_SC050": "Bảng tính so sánh thực tế: khoản tiết kiệm xăng 4.300 USD trong 3 năm bị xóa sạch hoàn toàn bởi khoản lỗ mất giá xe cũ lên tới 14.000 USD.",
    "CH06_SC051": "Bức tường kính hiển thị ma trận rủi ro vĩ mô: 4 mắt xích rủi ro hội tụ (Quỹ lương khổng lồ, Siết công nợ, Rủi ro chip, Vực thẳm xe cũ) phát sáng đỏ.",
    "CH06_SC052": "Góc nhìn flycam trên cao toàn cảnh khu công nghiệp lúc chập tối, bóng tối bao trùm các mái nhà xưởng rộng lớn, chỉ còn ánh đèn phòng điều hành.",
    "CH06_SC053": "Bố cục điện ảnh đối lập: dây chuyền robot tăng tốc lắp ráp chóng mặt đặt cạnh chiếc tủ thép chứa hồ sơ công nợ nhà cung cấp ngày càng dày thêm.",
    "CH06_SC054": "Bãi tập kết xe cũ tịch mịch lúc hoàng hôn, hàng chục chiếc xe điện phủ bụi mịn nằm bất động dưới bầu trời tím xám u trầm.",
    "CH06_SC055": "Hình ảnh tài liệu mang tính ẩn dụ vật lý: những cột trụ bê tông móng nhà máy đồ sộ cắm sâu trên đụn cát khô cằn dưới nắng chiều tà.",
    "CH06_SC056": "Chủ tịch Akio Toyoda trong bộ vest may đo trang trọng, đứng đĩnh đạc trong phòng họp nhìn ra thành phố Nagoya lúc chạng vạng với phong thái tự tin.",
    "CH06_SC057": "Phòng ngân quỹ điều hành tại Thành phố Toyota, báo cáo tài chính hiển thị khối tiền mặt và tài sản thanh khoản khổng lồ 5.300 tỷ Yên (34 tỷ USD).",
    "CH06_SC058": "Phòng lab nghiên cứu bảo mật cao tại Higashi-Fuji Nhật Bản, các nhà khoa học mặc đồ phòng sạch kiểm tra tấm điện phân pin thể rắn phát sáng vàng trắng.",
    "CH06_SC059": "Sự đối đầu thế kỷ: tiền cảnh là mô-đun pin thể rắn phát sáng ánh bạch kim tinh khiết, hậu cảnh xa xa là các đại công xưởng pin lỏng chìm trong giông bão."
}

rows_ch06 = []
for s in ch06_scenes:
    sid = s["id"]
    dur = f"{s['duration_sec']}s"
    text = " ".join(s["sentences"])
    desc = visual_descs_ch06.get(sid, "Bối cảnh công nghiệp thực tế đời thường.")
    overlay = text_overlays_ch06.get(sid, "Không")
    stream = "I2V" if (sid in ["CH06_SC008", "CH06_SC056"]) else "T2V"
    rows_ch06.append(f"| **{sid}** | {dur} | {text} | {desc} | `{overlay}` | **{stream}** |")

visual_content = visual_header + "\n".join(rows_ch06) + "\n"
out_visual.write_text(visual_content, encoding="utf-8")
print(f"Generated {len(rows_ch06)} table rows in {out_visual.name}")
