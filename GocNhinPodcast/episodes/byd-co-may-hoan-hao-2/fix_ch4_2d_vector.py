import os, re

base_dir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/byd-co-may-hoan-hao-2'
vis_file = os.path.join(base_dir, 'chapter_04_visual.md')
prompt_file = os.path.join(base_dir, 'prompts_chapter_04.txt')

# 1. Update chapter_04_visual.md to reflect 2D Vector Graphic Noir style in visual context descriptions
with open(vis_file, 'r', encoding='utf-8') as f:
    vis_content = f.read()

# Make sure visual context descriptions mention 2D Flat Vector Noir style
vis_content = vis_content.replace('Góc quay rộng', 'Đồ họa 2D vector phẳng, góc quay rộng')
vis_content = vis_content.replace('Cận cảnh', 'Đồ họa 2D vector phẳng, cận cảnh')
vis_content = vis_content.replace('Mô hình', 'Đồ họa 2D vector phẳng, mô hình')

with open(vis_file, 'w', encoding='utf-8') as f:
    f.write(vis_content)

# 2. Write 100% compliant 2D Flat Vector Noir Prompts for prompts_chapter_04.txt
scenes_data = [
    ("CH04_SC001", "A flat 2D vector illustration of European politicians standing silently inside the grand Berlaymont hall in Brussels, dark silhouettes", None, "steady wide shot"),
    ("CH04_SC002", "A flat 2D vector illustration of a gold-embossed Free Trade Agreement document resting on a desk bound tightly with heavy iron ropes", "FREE TRADE BOUND", "steady shot on the bound document"),
    ("CH04_SC003", "A flat 2D vector graphic of complex European political and economic gears jammed and frozen solid, unable to turn", None, "steady graphic shot"),
    ("CH04_SC004", "A flat 2D vector illustration of the WTO Headquarters building in Geneva with glowing flags and the scales of justice", "WTO MFN PRINCIPLE", "steady shot on the WTO building"),
    ("CH04_SC005", "A flat 2D vector illustration of a BYD Seal undergoing a crash test in a Euro NCAP laboratory with 5 glowing golden stars above", "EURO NCAP 5-STAR SAFETY", "steady shot on the vehicle"),
    ("CH04_SC006", "A flat 2D vector illustration of a digital emissions scanner displaying a glowing green 0.00 g/km reading", "ZERO EMISSION COMPLIANT", "steady shot on the scanner"),
    ("CH04_SC007", "A flat 2D vector illustration of a dark boardroom in Berlin with German government officials in tense discussion", "FEAR OF RETALIATION", "steady wide shot of officials"),
    ("CH04_SC008", "A flat 2D vector illustration of the European Commission Berlaymont building exterior under dark stormy skies", None, "steady shot of the building"),
    ("CH04_SC009", "A flat 2D vector silhouette of the Ministry of Commerce building in Beijing with an official giving a stern press statement", None, "steady shot on the official"),
    ("CH04_SC010", "A flat 2D vector illustration of a crowded avenue in Shanghai packed with Volkswagen, BMW, and Mercedes cars", "GERMAN AUTO EXPOSURE IN CHINA", "steady wide shot of traffic"),
    ("CH04_SC011", "A flat 2D vector illustration of a French export seaport with crates of Cognac and agricultural produce bound for China", "FRENCH AGRICULTURAL EXPORTS", "steady wide shot of cargo"),
    ("CH04_SC012", "A flat 2D vector illustration of a European Parliament corridor split visually into two opposing light beams of green and red", "INTERNAL GOVERNMENT SPLIT", "steady shot of the corridor"),
    ("CH04_SC013", "A flat 2D vector illustration of an Environment Ministry official pointing to a Net Zero 2030 target chart next to a $20,000 BYD Dolphin EV", "NET ZERO 2030 TARGET ($20,000 EV)", "steady shot on the official"),
    ("CH04_SC014", "A flat 2D vector illustration of an Industry Ministry official holding head in hands over reports of declining European automaker revenues", "DOMESTIC INDUSTRY PROTECTION", "steady shot on the official"),
    ("CH04_SC015", "A flat 2D vector illustration of a European citizen tightening a belt at a supermarket checkout, looking anxiously at a bill", None, "steady shot on the citizen"),
    ("CH04_SC016", "A flat 2D vector illustration of voters holding protest signs outside a BYD dealership objecting to government tariff increases", "VOTER BACKLASH ON TARIFFS", "steady wide shot of protesters"),
    ("CH04_SC017", "A flat 2D vector graphic map of the European Union with a glowing red fracture line along the border between Germany and France", "EU MEMBER STATE FRACTURE", "steady map graphic display"),
    ("CH04_SC018", "A flat 2D vector illustration of a German delegate in Brussels pressing a glowing red VOTE NO button during the EU tariff vote", "GERMANY: VOTE NO ON TARIFFS", "steady shot on the button press"),
    ("CH04_SC019", "A flat 2D vector illustration of a French delegate pressing a glowing green VOTE YES button, glaring sternly across at German delegates", "FRANCE: VOTE YES", "steady shot on the button press"),
    ("CH04_SC020", "A flat 2D vector illustration of a BYD executive shaking hands with European dealership tycoons in a dimly lit banquet room", None, "steady shot on the handshake"),
    ("CH04_SC021", "A flat 2D vector illustration of the Hedin Mobility Group headquarters building in Europe with BYD dealership branding", "LOCAL DISTRIBUTOR ALLIANCE", "steady wide shot of building"),
    ("CH04_SC022", "A flat 2D vector graphic of a glass protective shield labeled with a local distributor logo sheltering a BYD vehicle", "LOCAL LEGAL SHIELD", "steady graphic shot"),
    ("CH04_SC023", "A flat 2D vector illustration of a European legal minister pausing with gavel in hand while looking down at a map of local dealerships", None, "steady shot on the minister"),
    ("CH04_SC024", "A flat 2D vector illustration of a local European car dealership salesperson standing anxiously inside an empty BYD showroom", "LOCAL JOBS AT RISK", "steady shot on the salesperson"),
    ("CH04_SC025", "A flat 2D vector illustration of a BYD car maneuverably driving past red administrative tariff barrier gates", None, "steady tracking shot of car"),
    ("CH04_SC026", "A flat 2D vector illustration of an official EU document stamped in red 17% Anti-Subsidy Duty", "OCT 2024: EU 17% ANTI-SUBSIDY TARIFF", "steady shot on the document"),
    ("CH04_SC027", "A flat 2D vector graphic calculation showing 10% Base + 17% Anti-Subsidy = 27% Total BEV Tariff", "TOTAL BEV TARIFF: 27%", "steady graphic display"),
    ("CH04_SC028", "A flat 2D vector illustration of a BYD Seal U DM-i Super Hybrid (PHEV) gliding past European seaport customs check", "PHEV SUPER HYBRID PUSH", "steady tracking shot of vehicle"),
    ("CH04_SC029", "A flat 2D vector graphic tariff table showing PHEV IMPORT DUTY: ONLY 10% glowing in green", "PHEV TARIFF: ONLY 10%", "steady graphic display"),
    ("CH04_SC030", "A flat 2D vector illustration of a Local Content Requirement document crushed under a stack of Euro currency notes", "LOCALIZATION BYPASS", "steady shot on the document"),
    ("CH04_SC031", "A flat 2D vector illustration of a massive BYD factory construction site in Szeged, Hungary with active cranes", "HUNGARY PLANT (€4 BILLION)", "steady wide shot of construction"),
    ("CH04_SC032", "A flat 2D vector illustration of a signing ceremony for a BYD $1 Billion plant in West Java, Indonesia", "INDONESIA PLANT ($1 BILLION)", "steady shot on signing ceremony"),
    ("CH04_SC033", "A flat 2D vector illustration of a MADE IN EUROPE badge being fitted onto a BYD vehicle at the Hungary plant", "MADE IN EUROPE (0% INTRA-EU TARIFF)", "steady shot on badge fitting"),
    ("CH04_SC034", "A flat 2D vector illustration of a fleet of 8 massive BYD Ro-Ro transport ships sailing into international ports", "$690M OWNED FLEET", "steady wide tracking shot"),
    ("CH04_SC035", "A flat 2D vector illustration of a BYD captain holding the ship wheel while looking at a glowing nautical map", None, "steady shot on captain"),
    ("CH04_SC036", "A flat 2D vector illustration of the US Capitol building in Washington DC glowing under intense crimson light", "USA DEFENSIVE WALL", "steady wide shot of Capitol"),
    ("CH04_SC037", "A flat 2D vector graphic of a towering firewall displaying 100% TARIFF WALL blocking Chinese EVs", "100% TARIFF WALL", "steady graphic display"),
    ("CH04_SC038", "A flat 2D vector illustration of a CONNECTED VEHICLE SECURITY ACT document stamped BANRED over microchips", "CONNECTED VEHICLE SECURITY ACT", "steady shot on stamped document"),
    ("CH04_SC039", "A flat 2D vector illustration of Detroit auto logos Ford and GM protected behind a US national security firewall", "PROTECTING DETROIT", "steady shot on logos"),
    ("CH04_SC040", "A flat 2D vector graphic of a rotating globe with the USA shaded red and all other regions shaded green", None, "steady globe graphic display"),
    ("CH04_SC041", "A flat 2D vector illustration of European and Southeast Asian city streets crowded with BYD vehicles driving", None, "steady wide shot of traffic"),
    ("CH04_SC042", "A flat 2D vector illustration of a parked BYD car casting a long shadow with glowing ripples of hidden consequences underneath", None, "steady shot on parked car")
]

prompt_lines = []
suffix_img = ", clean bold outlines, flat colors, in a minimalist graphic novel aesthetic, dramatic chiaroscuro lighting, deep noir shadows."

for sc_id, desc, text_overlay, motion in scenes_data:
    if text_overlay:
        img_line = f'{sc_id} [IMAGE]: {desc}, "{text_overlay}" text overlay{suffix_img}'
    else:
        img_line = f'{sc_id} [IMAGE]: {desc}{suffix_img}'
    
    vid_line = f'{sc_id} [VIDEO]: @{sc_id}.png -> {motion}, preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations, 8-second continuous documentary video --ar 16:9'
    
    prompt_lines.append(img_line)
    prompt_lines.append(vid_line)
    prompt_lines.append('')

with open(prompt_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(prompt_lines) + '\n')

print("2D Flat Vector Graphic Noir Prompts written successfully!")
