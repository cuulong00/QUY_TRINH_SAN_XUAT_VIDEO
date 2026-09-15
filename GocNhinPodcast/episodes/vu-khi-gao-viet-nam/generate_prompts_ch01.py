# -*- coding: utf-8 -*-
"""
Script generating prompts_chapter_01.txt for Google Flow Batch Studio
Episode: vu-khi-gao-viet-nam | Chapter 01 (51 scenes)
Art Direction: Luminous Warm Editorial Illustration (Warm Ivory Cream #FAF7EE, Golden Amber #F59E0B)
"""

import os
import re

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam'
output_path = os.path.join(EPISODE_DIR, 'prompts_chapter_01.txt')

scenes = [
    {
        "id": "CH01_SC001",
        "ref": None,
        "subject": "an authentic Asian semiconductor engineer wearing a white cleanroom bunny suit and safety goggles carefully inspecting a rack of gleaming circular silicon wafers reflecting warm amber cleanroom light",
        "setting": "a state-of-the-art semiconductor cleanroom lithography bay under warm ambient yellow safelight",
        "text": None,
        "motion": "Slow steady push-in shot toward the polished silicon wafers reflecting warm yellow cleanroom lights"
    },
    {
        "id": "CH01_SC002",
        "ref": None,
        "subject": "a massive industrial overhead gantry crane slowly lifting a red-hot incandescent cylindrical steel forged ingot, warm amber sparks showering across the floor",
        "setting": "the sprawling casting hall of a heavy engineering plant under a warm golden furnace glow",
        "text": None,
        "motion": "Slow horizontal tracking pan past the glowing red-hot steel forging and showering sparks"
    },
    {
        "id": "CH01_SC003",
        "ref": None,
        "subject": "an elderly Southeast Asian farmer with authentic demographics and weathered skin, wearing rolled-up work trousers, planting individual green rice seedlings by hand in a traditional muddy paddy field",
        "setting": "a rustic muddy countryside paddy dike at golden hour under soft afternoon sunlight",
        "text": None,
        "motion": "Slow pull-back camera motion revealing the solitary farmer working peacefully in the muddy rice field"
    },
    {
        "id": "CH01_SC004",
        "ref": None,
        "subject": "a wall-mounted digital projector screen displaying a macroeconomic GDP transition chart showing a declining primary agrarian sector arrow pointing toward advanced tech services",
        "setting": "a sleek modern economic consulting boardroom with warm oak wood paneling under warm ceiling spotlights",
        "text": None,
        "motion": "Slow horizontal camera glide across the macroeconomic GDP structural transition diagram"
    },
    {
        "id": "CH01_SC005",
        "ref": None,
        "subject": "an elegant antique brass desk globe and a thick hardcover global food security white paper report lying open on a solid dark mahogany conference table",
        "setting": "a distinguished geopolitical strategy briefing library illuminated by a warm banker lamp glow",
        "text": None,
        "motion": "Slow subtle zoom-in toward the open food security treaty report on the mahogany table"
    },
    {
        "id": "CH01_SC006",
        "ref": None,
        "subject": "a full parliamentary assembly hall with distinguished lawmakers seated in curved rows of leather benches, actively discussing agrarian subsidy ledgers under natural daylight",
        "setting": "a grand European parliamentary chamber with warm carved oak woodwork and arched glass skylights",
        "text": None,
        "motion": "Wide cinematic tracking shot gliding smoothly across the parliamentary debating chamber"
    },
    {
        "id": "CH01_SC007",
        "ref": None,
        "subject": "an official embossed United States Farm Bill legislative statute binder stamped with golden governmental seals, resting beside federal budget ledgers",
        "setting": "the United States Senate Agriculture Committee hearing room in Washington DC under warm morning sunlight",
        "text": "US FARM BILL: ~1.000 TY USD",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and federal statute binder"
    },
    {
        "id": "CH01_SC008",
        "ref": None,
        "subject": "an official European Union Common Agricultural Policy annual financial report displaying a clear colorful pie chart allocating thirty-three percent of the entire union budget to farmer subsidies",
        "setting": "the European Commission executive council chamber in Brussels with warm interior architectural lighting",
        "text": "EU: 1/3 TOAN BO NGAN SACH",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the one-third subsidy pie chart"
    },
    {
        "id": "CH01_SC009",
        "ref": None,
        "subject": "a Japanese agricultural policy director in a formal dark charcoal suit bowing respectfully before a wall-mounted topographic agrarian map of Niigata paddy terraces",
        "setting": "the Ministry of Agriculture Forestry and Fisheries executive headquarters in Tokyo with warm cedar wood interior",
        "text": None,
        "motion": "Subtle slow push-in toward the traditional Japanese rice terrace topographic map"
    },
    {
        "id": "CH01_SC010",
        "ref": None,
        "subject": "an official Japanese customs tariff decree folder bearing a bold red vermilion administrative stamp, resting beside a ceramic bowl of steaming Japanese Koshihikari white rice",
        "setting": "the customs declaration office at the maritime port of Yokohama bathed in warm golden afternoon light",
        "text": "THUE GAO NHAT: 778%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the red tariff decree stamp"
    },
    {
        "id": "CH01_SC011",
        "ref": None,
        "subject": "a massive industrial grain storage silo interior with a heavy mechanical screw conveyor continuously pouring golden wheat grains into a colossal storage mountain under warm floodlights",
        "setting": "a state strategic grain reserve facility filled with warm ambient golden dust",
        "text": None,
        "motion": "Slow upward tilt following the mechanical conveyor chute pouring thousands of golden grains"
    },
    {
        "id": "CH01_SC012",
        "ref": None,
        "subject": "a digital situation room displaying illuminated maritime shipping corridors and grain freight choke points across the Malacca Strait and Suez Canal on a warm wooden console",
        "setting": "a national food security operations center under warm amber ambient terminal glow",
        "text": None,
        "motion": "Slow horizontal tracking pan across the illuminated global grain freight trade corridors"
    },
    {
        "id": "CH01_SC013",
        "ref": None,
        "subject": "a completely empty glazed ceramic rice bowl sitting on an empty dinner table, resting beside a sleek modern smartphone displaying red stock market drops under dim sunset light",
        "setting": "a modern metropolitan dining room in an Asian high-rise apartment bathed in soft golden dusk",
        "text": None,
        "motion": "Slow subtle push-in shot centering on the stark empty ceramic bowl on the table"
    },
    {
        "id": "CH01_SC014",
        "ref": None,
        "subject": "a row of massive bulk grain freight ships anchored motionless off an obstructed seaport breakwater, motionless gantry cranes silhouetted against a warm amber evening horizon",
        "setting": "a quiet coastal shipping anchorage at sunset under a warm golden horizon",
        "text": None,
        "motion": "Wide cinematic tracking shot across the idle ocean bulk grain freighters waiting off the harbor"
    },
    {
        "id": "CH01_SC015",
        "ref": None,
        "subject": "the sprawling tropical waterfront of Manila Bay with palm trees and a prominent roadside geographic landmark signpost reading Welcome to Manila in English and Tagalog",
        "setting": "a busy coastal avenue in Manila Philippines under bright warm tropical midday sun",
        "text": None,
        "motion": "Slow horizontal pan from Manila Bay waterfront across the busy palm-lined coastal boulevard"
    },
    {
        "id": "CH01_SC016",
        "ref": None,
        "subject": "a framed vintage color photograph from the 1960s showing international agronomists in light cotton shirts examining experimental lush green rice terraces in Laguna",
        "setting": "a classic wooden academic library desk surrounded by archived agricultural agronomy journals",
        "text": None,
        "motion": "Slow push-in shot toward the framed vintage agrarian photograph under soft desk lamp lighting"
    },
    {
        "id": "CH01_SC017",
        "ref": "irri_los_banos_gate.jpg",
        "subject": "the iconic entrance archway and institutional building of the International Rice Research Institute depicted in the reference image, surrounded by lush experimental green rice paddies and tropical palm trees under warm morning sunlight",
        "setting": "the campus of the International Rice Research Institute in Los Baños Laguna Philippines",
        "text": "VIEN LUA IRRI (LOS BANOS)",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the institutional IRRI entrance"
    },
    {
        "id": "CH01_SC018",
        "ref": None,
        "subject": "the gleaming modern glass and chrome skyscrapers of Bonifacio Global City rising into a clear warm sky, luxury sedans and taxis cruising along landscaped wide avenues",
        "setting": "the modern financial district of Bonifacio Global City Taguig Metro Manila under bright sunlight",
        "text": None,
        "motion": "Slow upward tilt gliding along the soaring glass and steel facade of the modern Manila corporate towers"
    },
    {
        "id": "CH01_SC019",
        "ref": None,
        "subject": "a busy business process outsourcing call center floor packed with hundreds of young Filipino operators wearing telephone headsets typing on computers under bright warm fluorescent lamps",
        "setting": "a high-density modern business process outsourcing office floor in Metro Manila",
        "text": None,
        "motion": "Slow continuous tracking shot gliding smoothly past rows of focused call center agents"
    },
    {
        "id": "CH01_SC020",
        "ref": None,
        "subject": "a dockside container crane lowering heavy wooden cargo pallets loaded with woven white polypropylene bags of imported rice onto the bed of a waiting flatbed truck",
        "setting": "the South Harbor commercial cargo terminal of Manila under bright tropical morning sun",
        "text": None,
        "motion": "Slow downward crane tilt tracking the pallet of imported rice bags landing on the truck bed"
    },
    {
        "id": "CH01_SC021",
        "ref": None,
        "subject": "a desktop spiral paper calendar turned to July 2023 with a warm golden sunbeam slicing across the page, resting beside a half-empty coffee mug and a fountain pen",
        "setting": "an economic research desk inside a quiet office during the intense summer of 2023",
        "text": "MUA HE NAM 2023",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the July 2023 calendar page"
    },
    {
        "id": "CH01_SC022",
        "ref": "modi_india.jpg",
        "subject": "the senior government leader depicted in the reference photo presiding over an official cabinet meeting, an authentic Directorate General of Foreign Trade export ban notification stamped with red wax on the desk",
        "setting": "an executive conference hall in New Delhi India featuring polished wood paneling under warm interior chandelier lighting",
        "text": "AN DO CAM XUAT KHAU (20/07/2023)",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the official export decree"
    },
    {
        "id": "CH01_SC023",
        "ref": None,
        "subject": "a digital agrarian commodity trading terminal screen showing a sudden sharp drop in global export tonnage and flashing amber alerts across Asian trade corridors",
        "setting": "an international grain futures trading office desk under warm ambient monitor lighting",
        "text": "AN DO: 40% NGUON CUNG",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the dropping supply graph"
    },
    {
        "id": "CH01_SC024",
        "ref": None,
        "subject": "a dual financial monitor setup displaying the historic fifteen-year price spike of five percent broken export rice rocketing straight up to six hundred and fifty dollars per metric ton",
        "setting": "the market telemetry desk of an international grain brokerage firm under warm overhead halogen lighting",
        "text": "DINH GIA: 650 USD/TAN",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the historic price spike chart"
    },
    {
        "id": "CH01_SC025",
        "ref": None,
        "subject": "Filipino market vendors and local shoppers gathered in front of a rustic wooden rice stall, staring with anxious expressions at a handwritten chalkboard rice price sign in Divisoria",
        "setting": "a bustling crowded traditional public market in Divisoria Manila under warm morning sun",
        "text": None,
        "motion": "Quick sweeping pan across the concerned faces of vendors and shoppers at the rice stall"
    },
    {
        "id": "CH01_SC026",
        "ref": None,
        "subject": "an official monthly economic bulletin published by the Philippine Statistics Authority with a bold printed headline highlighting the national food inflation rate surging past eight percent",
        "setting": "the statistical analysis desk at a Manila financial institution under warm library lamp light",
        "text": "LAM PHAT THUC PHAM: > 8%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 8 percent inflation report"
    },
    {
        "id": "CH01_SC027",
        "ref": None,
        "subject": "a long continuous queue of hundreds of everyday Filipino citizens standing patiently under intense midday sun outside a government National Food Authority subsidized rice distribution center, clutching small ticket vouchers",
        "setting": "an urban neighborhood street in Metro Manila under harsh bright tropical sunshine",
        "text": None,
        "motion": "Slow dramatic tracking shot gliding along the endless queue of citizens waiting for subsidized rice"
    },
    {
        "id": "CH01_SC028",
        "ref": None,
        "subject": "a high-angle contrasting view looking from the towering glass facade of a luxury Makati financial skyscraper down to the crowded street level where hundreds of people wait in a food queue",
        "setting": "the Ayala Avenue financial canyon in Makati Metro Manila under bright afternoon daylight",
        "text": None,
        "motion": "Dramatic slow downward tilt from the glass skyscraper spire down to the street level food line"
    },
    {
        "id": "CH01_SC029",
        "ref": "marcos_jr.jpg",
        "subject": "the national president depicted in the reference photo signing an official stamped legislative decree labeled Executive Order Number 39 imposing mandatory retail rice price ceilings on a dark polished desk",
        "setting": "the formal ceremonial cabinet room of Malacanang Palace in Manila under warm architectural lighting",
        "text": "SAC LENH GIA TRAN: EO 39",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the signed executive order"
    },
    {
        "id": "CH01_SC030",
        "ref": None,
        "subject": "a distinguished senior Philippine diplomatic and trade delegation in dark formal business barong tagalog and suits carrying leather briefing binders as they arrive at the diplomatic reception terminal",
        "setting": "the international VIP arrivals terminal at Noi Bai International Airport in Hanoi under bright warm morning daylight",
        "text": None,
        "motion": "Slow forward tracking shot following the Philippine delegation walking briskly into the airport terminal"
    },
    {
        "id": "CH01_SC031",
        "ref": None,
        "subject": "a peaceful historic river trading hub on the Tien River with dozens of traditional wooden freight barges laden with raw paddy rice moored along vibrant wooden stilt docks under golden morning sunrise",
        "setting": "the vibrant riverbank wharf of Sa Dec Dong Thap in the Mekong Delta Vietnam under warm golden sunlight",
        "text": None,
        "motion": "Cinematic wide panning shot across the tranquil Mekong Delta river hub with rice barges at dawn"
    },
    {
        "id": "CH01_SC032",
        "ref": None,
        "subject": "an authentic Vietnamese grain export executive in a white collared shirt on the phone inside a bustling riverfront export office, multiple computer screens displaying incoming international purchase orders",
        "setting": "a busy rice export trading company headquarters in Can Tho under warm natural morning lighting",
        "text": None,
        "motion": "Horizontal camera tracking shot past bustling desks covered in export contracts and ringing phones"
    },
    {
        "id": "CH01_SC033",
        "ref": None,
        "subject": "an authentic Vietnamese male farmer in a conical hat and an independent grain broker standing beside a lush golden ripe rice field, holding freshly cut golden stalks while checking a digital calculator",
        "setting": "an earthen canal dike in An Giang province under warm radiant morning sun",
        "text": None,
        "motion": "Slow push-in shot focusing on the farmer holding ripe golden rice panicles beside the broker"
    },
    {
        "id": "CH01_SC034",
        "ref": None,
        "subject": "a bustling riverside rice milling factory with multiple large wooden cargo barges docked at the intake chute, workers unloading jute bags while gentle white steam rises from the grain dryer chimney",
        "setting": "a large-scale industrial rice milling and polishing complex along the Hau River under warm daylight",
        "text": None,
        "motion": "Slow horizontal tracking shot along the bustling factory wharf packed with loaded rice barges"
    },
    {
        "id": "CH01_SC035",
        "ref": None,
        "subject": "three modern red and orange combine harvesters operating in parallel across a vast sea of golden ripe rice paddies, kicking up gentle warm dust plumes under brilliant sunrise rays",
        "setting": "an expansive high-tech large-scale demonstration rice field in the Mekong Delta under warm golden morning light",
        "text": None,
        "motion": "Epic high-angle aerial gliding shot smoothly following the three combine harvesters cutting golden rice"
    },
    {
        "id": "CH01_SC036",
        "ref": None,
        "subject": "a large architectural infographic chart on an exhibition wall presenting the solid national annual paddy harvest milestone of forty-three point four million metric tons guaranteeing total domestic food security",
        "setting": "the agrarian statistics gallery of the Institute of Policy and Strategy for Agriculture in Hanoi under warm gallery lighting",
        "text": "SAN LUONG: 43.4 TRIEU TAN LUA",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the national harvest data"
    },
    {
        "id": "CH01_SC037",
        "ref": None,
        "subject": "a colossal ocean-going deepwater bulk carrier berthed at a river port wharf, automated enclosed conveyor loading booms pouring polished white rice into the ship hold under a bright clear sky",
        "setting": "the international deepwater maritime terminal on the Hau River in Can Tho under radiant morning sunlight",
        "text": "XUAT KHAU: 8.1 - 8.3 TRIEU TAN",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the ocean freighter loading rice"
    },
    {
        "id": "CH01_SC038",
        "ref": "thutuong_chinh.jpg",
        "subject": "the senior government leader depicted in the reference photo presiding over an urgent ministerial cabinet conference on a large oval wooden table, an official governmental directive folder labeled Directive 24 on the desk",
        "setting": "the primary cabinet meeting room of the Government Headquarters in Hanoi under warm dignified interior lighting",
        "text": "CHI THI 24/CT-TTg",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the national cabinet session"
    },
    {
        "id": "CH01_SC039",
        "ref": None,
        "subject": "the cavernous interior of a spotless national strategic food reserve warehouse with thousands of neatly stacked pallets of rice bags stretching into the distance under warm overhead industrial lighting",
        "setting": "a state strategic food reserve facility in Vietnam under warm clean ambient warehouse light",
        "text": None,
        "motion": "Slow horizontal tracking shot gliding down the clean central corridor between towering stacks of rice"
    },
    {
        "id": "CH01_SC040",
        "ref": None,
        "subject": "a clean dual-line comparison graph displayed on a trading screen with the top orange line showing global rice prices jumping thirty percent while the lower line remains steady",
        "setting": "an analytical macroeconomic monitor station under soft warm desk lamp illumination",
        "text": "GIA THE GIOI: +30%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the surging international price line"
    },
    {
        "id": "CH01_SC041",
        "ref": None,
        "subject": "a neat traditional neighborhood rice shop with woven wooden bins displaying gleaming white rice varieties, a small rustic wooden chalkboard sign reading fifteen to sixteen thousand dong per kilo",
        "setting": "a clean cozy street market storefront in Hanoi or Ho Chi Minh City under warm morning sunlight",
        "text": "GAO TE: 15.000 - 16.000 D/KG",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the traditional rice storefront"
    },
    {
        "id": "CH01_SC042",
        "ref": None,
        "subject": "an authentic Vietnamese factory worker in a dark blue work uniform smiling warmly as he receives a generous steaming hot plate of white rice with pork and vegetables at a shaded street canteen",
        "setting": "a bustling friendly streetside workers eatery near an industrial park under warm midday dappled sunlight",
        "text": "BAT COM BINH DAN: 35.000 D",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the steaming worker lunch plate"
    },
    {
        "id": "CH01_SC043",
        "ref": None,
        "subject": "an official annual macroeconomic performance report published by the General Statistics Office of Vietnam showing the stable nationwide Consumer Price Index confirmed at three point twenty-five percent",
        "setting": "the statistical library desk at the Ministry of Planning and Investment under warm reading lamps",
        "text": "LAM PHAT 2023: 3.25%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the official CPI audit binder"
    },
    {
        "id": "CH01_SC044",
        "ref": None,
        "subject": "historical hand-drawn parchment cartographic maps and engineering blueprints of early canal excavation and salinity dyke systems across the Mekong Delta laid out on a weathered solid wood drafting table",
        "setting": "an agrarian engineering historical archive under warm brass study lamps",
        "text": None,
        "motion": "Slow horizontal tracking pan across the vintage canal excavation blueprints and historical maps"
    },
    {
        "id": "CH01_SC045",
        "ref": None,
        "subject": "an intricate vast network of interconnected river canals with dozens of steel and wooden barges transporting golden paddy, automated irrigation pump stations and sluice gates operating harmoniously like a living biological machine",
        "setting": "the wide hydraulic canal network of the Mekong Delta under breathtaking golden morning horizon",
        "text": None,
        "motion": "Epic high-altitude panoramic aerial glide revealing the boundless canal grid and cruising rice barges"
    },
    {
        "id": "CH01_SC046",
        "ref": None,
        "subject": "a warm intimate evening family dinner table in Vietnam with three generations smiling together around a large steaming porcelain bowl of fragrant white rice and humble savory dishes",
        "setting": "a cozy traditional Vietnamese dining room illuminated by warm glowing amber interior lamps",
        "text": None,
        "motion": "Slow gentle push-in shot focusing on the steaming fragrant white rice bowl at the center of the table"
    },
    {
        "id": "CH01_SC047",
        "ref": None,
        "subject": "thousands of energetic Vietnamese factory workers in clean manufacturing uniforms walking into a modern industrial manufacturing park at dawn, company shuttle buses lined up under a glowing golden sunrise",
        "setting": "the landscaped entrance boulevard of a modern industrial manufacturing zone under radiant morning sun",
        "text": None,
        "motion": "Horizontal tracking shot following the steady stream of optimistic workers entering the factory gates"
    },
    {
        "id": "CH01_SC048",
        "ref": None,
        "subject": "an authentic vintage paper food rationing coupon booklet from the historical subsidy era resting on a rustic weathered wooden table beside a vintage brass scale under soft warm window light",
        "setting": "a historical archive exhibit room dedicated to Vietnam post-war economic history under warm amber lighting",
        "text": None,
        "motion": "Slow subtle push-in toward the historic paper food rationing coupon booklet"
    },
    {
        "id": "CH01_SC049",
        "ref": None,
        "subject": "a massive modern container and bulk freight vessel flying the red flag with yellow star cruising out to open sea, parting calm ocean waves under bright warm morning sunlight",
        "setting": "the deepwater maritime shipping channel of Vung Tau looking out toward the East Sea under golden sunbeams",
        "text": None,
        "motion": "Wide majestic cinematic shot tracking the Vietnamese vessel sailing into the expansive open ocean"
    },
    {
        "id": "CH01_SC050",
        "ref": None,
        "subject": "an extreme macro close-up shot of weathered calloused hands of an authentic Vietnamese rice farmer gently cradling a handful of pristine golden ripe rice grains, morning sunlight illuminating the golden husks",
        "setting": "the edge of an An Giang paddy field under luminous golden morning daylight",
        "text": None,
        "motion": "Slow subtle push-in shot highlighting the glistening golden rice grains in the weathered farmer hands"
    },
    {
        "id": "CH01_SC051",
        "ref": None,
        "subject": "an expansive high-level geopolitical maritime map of the Indo-Pacific region laid out on a polished dark wood boardroom table, with Vietnam glowing like a warm golden beacon at the center of Asian rice corridors",
        "setting": "an executive strategic conference hall illuminated by warm directional architectural spotlights",
        "text": "VI THE BAN CO DIA KINH TE",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the glowing regional map"
    }
]

lines = []
for sc in scenes:
    sc_id = sc["id"]
    ref_tag = sc["ref"]
    subj = sc["subject"]
    setting = sc["setting"]
    text_overlay = sc["text"]
    motion = sc["motion"]
    
    # 1. Build IMAGE line
    if ref_tag:
        if "irri" in ref_tag:
            img_prompt = f"{sc_id} [IMAGE]: @{ref_tag} -> A 2D warm cinematic editorial illustration of {subj}, set at {setting}, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ambient tone (#FAF7EE), luminous warm golden daylight, soft ambient shadows"
        else:
            img_prompt = f"{sc_id} [IMAGE]: @{ref_tag} -> A 2D warm cinematic editorial illustration of the person depicted in the reference photo, faithfully preserving their facial features, bone structure, hairstyle, and attire. The subject is {subj}, set in {setting}. Elegant graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ambient tone (#FAF7EE), luminous warm interior lighting, soft ambient shadows"
    else:
        img_prompt = f"{sc_id} [IMAGE]: A 2D warm cinematic editorial illustration of {subj}, set in {setting}, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, warm ivory cream ambient tone (#FAF7EE), luminous warm golden daylight, soft ambient shadows"
        
    if text_overlay:
        img_prompt += f', compact subtle glowing golden amber 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading "{text_overlay}"'
        
    img_prompt += ", no watermarks, 16:9"
    
    # 2. Build VIDEO line
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
