# -*- coding: utf-8 -*-
"""
Script generating prompts_chapter_02.txt for Google Flow Batch Studio
Episode: vu-khi-gao-viet-nam | Chapter 02 (60 scenes)
Art Direction: Luminous Warm Editorial Illustration (Warm Ivory Cream #FAF7EE, Ripe Golden Amber #F59E0B)
"""

import os

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam'
output_path = os.path.join(EPISODE_DIR, 'prompts_chapter_02.txt')

scenes = [
    {
        "id": "CH02_SC001",
        "subject": "an authentic Asian economics professor turning the pages of a classic development economics treatise on a solid oak desk surrounded by research monographs",
        "setting": "a distinguished university faculty study under the warm glow of a brass banker lamp",
        "text": None,
        "motion": "Slow push-in shot toward the open pages of the economic development treatise"
    },
    {
        "id": "CH02_SC002",
        "subject": "the sprawling construction grounds of a modern industrial manufacturing park with rising structural steel factory bays and landscaped internal avenues",
        "setting": "an expanding industrial development zone under radiant warm morning sunlight",
        "text": None,
        "motion": "Cinematic wide camera tilt-up gliding smoothly along rising structural steel factory frames"
    },
    {
        "id": "CH02_SC003",
        "subject": "international corporate investors in dark suits shaking hands and signing foreign direct investment memorandum binders on an executive podium",
        "setting": "a prestigious international investment promotion gala hall under warm chandelier light",
        "text": None,
        "motion": "Horizontal camera tracking shot past the formal FDI signing ceremony"
    },
    {
        "id": "CH02_SC004",
        "subject": "an official corporate income tax incentive statutory binder detailing statutory multi-year tax holidays, resting beside an architectural miniature model of a smart factory",
        "setting": "a corporate legal advisory boardroom with warm oak walls under recessed warm spotlights",
        "text": None,
        "motion": "Slow push-in shot toward the corporate tax exemption statute binder"
    },
    {
        "id": "CH02_SC005",
        "subject": "an analytical cost-breakdown spreadsheet diagram displayed on a monitor, an analyst pen circling the core labor reproduction cost equation",
        "setting": "an industrial engineering cost-management office under warm ambient desk light",
        "text": None,
        "motion": "Steady camera shot focusing on the industrial labor reproduction cost formula"
    },
    {
        "id": "CH02_SC006",
        "subject": "a steady stream of authentic young Vietnamese factory shift workers in neat navy-blue and grey company uniforms walking briskly past security gates",
        "setting": "the main gate boulevard of VSIP Binh Duong industrial park under warm dawn sunlight",
        "text": None,
        "motion": "Horizontal camera tracking shot following the shift workers entering the industrial zone"
    },
    {
        "id": "CH02_SC007",
        "subject": "a printed monthly factory worker payroll payslip showing an authentic total monthly net earnings breakdown ranging between seven and nine million dong",
        "setting": "the human resources payroll desk of a precision electronics factory under warm fluorescent lamps",
        "text": "LUONG CONG NHAN: 7 - 9 TRIEU DONG",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the monthly payslip"
    },
    {
        "id": "CH02_SC008",
        "subject": "automated high-speed surface-mount technology robot arms precision-placing microchips onto green circuit boards, a focused female Vietnamese technician inspecting output",
        "setting": "a spotless high-tech electronic component manufacturing bay under warm diffuse lighting",
        "text": None,
        "motion": "Slow tracking shot gliding along the high-speed automated circuit board placement line"
    },
    {
        "id": "CH02_SC009",
        "subject": "hundreds of focused Vietnamese textile workers operating industrial sewing machines, stitching high-quality export garments under bright natural daylight streaming through tall factory windows",
        "setting": "a spacious and clean modern garment manufacturing floor under warm natural sunlight",
        "text": None,
        "motion": "Wide cinematic tracking shot gliding across the bustling and organized garment manufacturing floor"
    },
    {
        "id": "CH02_SC010",
        "subject": "a young authentic Vietnamese worker sitting quietly at a simple wooden table in a tidy rented room, carefully balancing household expenses in a small notebook",
        "setting": "a humble yet clean residential workers quarter near an industrial zone bathed in warm evening lamplight",
        "text": None,
        "motion": "Slow push-in shot toward the handwritten household budget notebook"
    },
    {
        "id": "CH02_SC011",
        "subject": "a tidy row of modern worker rental boarding rooms with tiled roofs and a shared sunny courtyard with clean laundry hanging on lines under clear skies",
        "setting": "a well-maintained worker residential community near an export processing zone in warm daylight",
        "text": None,
        "motion": "Horizontal camera tracking pan past the quiet and clean residential rental rooms"
    },
    {
        "id": "CH02_SC012",
        "subject": "a young authentic Vietnamese female factory worker smiling gently as she remits savings back home to her rural parents using a digital banking phone app",
        "setting": "a sunny neighborhood cafe terrace near the industrial park under warm morning sun",
        "text": None,
        "motion": "Subtle push-in shot highlighting the reassuring and content smile of the worker"
    },
    {
        "id": "CH02_SC013",
        "subject": "a traditional glazed ceramic earthenware rice urn filled to the brim with polished white rice, standing in a sunny rustic kitchen beside cooking oil and fish sauce bottles",
        "setting": "a humble Vietnamese home kitchen bathed in warm morning sunbeams",
        "text": None,
        "motion": "Steady camera shot focusing on the brim-filled ceramic rice urn reflecting warm sunbeams"
    },
    {
        "id": "CH02_SC014",
        "subject": "a generous hearty workers lunch plate loaded with steaming hot white rice, savory braised pork, sautéed morning glory, and a warm soup bowl resting on a stainless-steel table",
        "setting": "a bustling friendly streetside workers eatery outside the industrial gate under dappled sunlight",
        "text": "BAT COM BINH DAN: 35.000 DONG",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the steaming 35K lunch plate"
    },
    {
        "id": "CH02_SC015",
        "subject": "a macroeconomic policy diagram illustrating the direct causal transmission from stable staple food prices to anchored core inflation rates on an interactive display",
        "setting": "a national economic research institute conference room under warm ceiling spotlights",
        "text": None,
        "motion": "Slow push-in shot toward the macroeconomic core inflation stabilization model"
    },
    {
        "id": "CH02_SC016",
        "subject": "a traditional neighborhood grocery store lined with open woven jute sacks brimming with various fragrant white rice varieties, customers purchasing bags calmly",
        "setting": "a clean and cozy neighborhood street market in Vietnam under warm golden sunlight",
        "text": None,
        "motion": "Horizontal pan gliding across the bountiful open sacks of polished white rice"
    },
    {
        "id": "CH02_SC017",
        "subject": "an official electronic national economic dashboard displaying the annual Consumer Price Index trajectory comfortably anchored well below the statutory ceiling of four percent",
        "setting": "the economic monitoring room at the National Statistics Information Center under warm ambient light",
        "text": "LAM PHAT MUC TIEU: < 4%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the anchored sub-4% CPI curve"
    },
    {
        "id": "CH02_SC018",
        "subject": "authentic Vietnamese factory workers after their work shift smiling and browsing fresh vegetables and groceries at a bustling open-air market without financial stress",
        "setting": "a vibrant neighborhood market near the industrial park bathed in warm late-afternoon golden hour light",
        "text": None,
        "motion": "Horizontal camera tracking shot following workers carrying baskets of fresh groceries"
    },
    {
        "id": "CH02_SC019",
        "subject": "an industrial factory executive board meeting where management and labor union representatives reach a harmonious and predictable annual wage schedule agreement",
        "setting": "a sunlit executive conference room in a precision manufacturing plant under warm interior lighting",
        "text": None,
        "motion": "Slow tracking shot across the management and union negotiation conference table"
    },
    {
        "id": "CH02_SC020",
        "subject": "international executive corporate leaders standing beside panoramic glass windows overlooking a sprawling high-tech industrial complex, reviewing economic stability reports",
        "setting": "a top-floor executive suite overlooking an expansive industrial park under clear sunny skies",
        "text": None,
        "motion": "Wide cinematic tracking shot from the executive boardroom looking over the manufacturing zone"
    },
    {
        "id": "CH02_SC021",
        "subject": "a comparative macroeconomic infographic chart showing Vietnam living and staple food costs significantly more affordable and stable than neighboring regional hubs",
        "setting": "a regional economic analysis workstation under warm library lamp illumination",
        "text": None,
        "motion": "Slow push-in shot focusing on the regional staple food affordability benchmark chart"
    },
    {
        "id": "CH02_SC022",
        "subject": "a spacious and brightly lit company cafeteria with hundreds of Vietnamese workers in clean uniforms dining comfortably together, eating nourishing warm rice meals",
        "setting": "a modern factory employee dining hall bathed in warm daylight from floor-to-ceiling windows",
        "text": None,
        "motion": "Slow sweeping tracking shot past rows of seated workers enjoying their factory lunch"
    },
    {
        "id": "CH02_SC023",
        "subject": "an intimate close-up shot of a steaming hot bowl of fragrant white rice resting beside clean bamboo chopsticks on a sunny dining table, a delicate warm vapor curling into the air",
        "setting": "a cozy dining room table illuminated by soft warm midday sunlight",
        "text": None,
        "motion": "Subtle slow zoom-in centering on the gentle warm steam rising from the fresh white rice bowl"
    },
    {
        "id": "CH02_SC024",
        "subject": "a macroeconomic mechanical balance diagram showing how affordable staple food absorbs inflationary pressure and preserves net industrial manufacturing margins",
        "setting": "a policy think-tank research board under warm architectural track spotlights",
        "text": "CHIEC LO XO GIAM XOC VI MO",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the macroeconomic shock-absorber model"
    },
    {
        "id": "CH02_SC025",
        "subject": "a polished mirror-like silicon wafer reflecting yellow cleanroom lighting laid out on a dark velvet cloth directly beside a handful of ripe golden Mekong paddy grains",
        "setting": "an economic auditing desktop under directional warm spotlighting creating striking physical contrast",
        "text": None,
        "motion": "Cinematic macro tracking shot gliding across the gleaming silicon wafer to the rustic golden paddy grains"
    },
    {
        "id": "CH02_SC026",
        "subject": "heavy automated air-cargo container pallets packed with branded high-tech consumer electronics being loaded into the cargo hold of an international freight jet under morning sun",
        "setting": "the international air-cargo logistics apron at Noi Bai Airport under bright warm morning daylight",
        "text": "XUAT KHAU CONG NGHE: 10 TY USD",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the ten-billion-dollar export cargo"
    },
    {
        "id": "CH02_SC027",
        "subject": "an analytical corporate cost accountant scrutinizing imported component procurement invoices, highlighting massive payments sent abroad for foreign parts",
        "setting": "a corporate supply-chain auditing desk under focused warm desk lamp illumination",
        "text": None,
        "motion": "Slow push-in shot toward the highlighted foreign component procurement invoices"
    },
    {
        "id": "CH02_SC028",
        "subject": "an automated high-bay factory warehouse where electric forklifts maneuver heavy crates of imported microprocessors and silicon wafers marked with East Asian origin labels",
        "setting": "an advanced electronic component bonded warehouse under warm industrial lighting",
        "text": None,
        "motion": "Horizontal camera tracking shot following the electric forklift moving imported microchip crates"
    },
    {
        "id": "CH02_SC029",
        "subject": "an infographic chart on an economic research blackboard dissecting the domestic value added versus foreign input share of assembled electronics",
        "setting": "an industrial economics research classroom under warm ceiling light",
        "text": None,
        "motion": "Subtle slow push-in toward the value-added domestic retention graph"
    },
    {
        "id": "CH02_SC030",
        "subject": "an official macroeconomic statistical display confirming the actual domestic retained value added of the consumer electronics assembly sector anchored at ten to fifteen percent",
        "setting": "the industrial data analysis desk at the Central Institute for Economic Management",
        "text": "GIA TRI NOI DIA BAN DAN: 10% - 15%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 10-15 percent DVA metric"
    },
    {
        "id": "CH02_SC031",
        "subject": "a factory utility auditing ledger showing that retained domestic value primarily pays for assembly labor payroll and high-voltage factory electrical power bills",
        "setting": "an industrial utility management office with views of the plant substation outside",
        "text": None,
        "motion": "Slow vertical camera tilt down the electricity utility bills and worker assembly payroll ledgers"
    },
    {
        "id": "CH02_SC032",
        "subject": "a traditional woven bamboo winnowing basket filled with pristine white polished rice grains basking under clear warm morning sunlight on a countryside porch",
        "setting": "a tranquil traditional rural Southern Vietnamese homestead veranda under warm golden sun",
        "text": None,
        "motion": "Close-up macro shot of glistening white rice grains resting on the natural bamboo winnowing tray"
    },
    {
        "id": "CH02_SC033",
        "subject": "a national export milestone graph at the Ministry of Industry and Trade celebrating the historic record peak of nearly six billion dollars in national rice export turnover",
        "setting": "the trade promotion hall of the Ministry of Industry and Trade in Hanoi under warm gallery lighting",
        "text": None,
        "motion": "Steady camera shot gliding toward the historic six-billion-dollar national rice export peak"
    },
    {
        "id": "CH02_SC034",
        "subject": "ocean freighters moored along the Hau River international port wharf, automated conveyor belts continuously pouring white rice into deep cargo holds under radiant sunshine",
        "setting": "the bustling deepwater agrarian river terminal in Can Tho under clear sunny skies",
        "text": "XUAT KHAU GAO: 4 - 6 TY USD",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the grain freighters"
    },
    {
        "id": "CH02_SC035",
        "subject": "a comparative macroeconomic diagram highlighting that rice exports retain a staggering seventy-five to eighty percent net domestic value added within the country",
        "setting": "an agricultural economics policy institute gallery under warm interior spotlights",
        "text": "GIA TRI NOI DIA GAO (DVA): 75% - 80%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 75-80% DVA chart"
    },
    {
        "id": "CH02_SC036",
        "subject": "an authentic Vietnamese farmer cradling a handful of fertile alluvial silt soil beside strong deep-rooted rice plants glistening with fresh morning dew",
        "setting": "a lush fertile riverside paddy field along the Tien River under golden dawn sunlight",
        "text": None,
        "motion": "Slow upward tilt from rich fertile silt soil up along the strong green rice stems"
    },
    {
        "id": "CH02_SC037",
        "subject": "an authentic Vietnamese farmer in rural attire smiling happily as he receives payment for his paddy harvest from a local agricultural bank branch teller",
        "setting": "a bright and welcoming Agribank rural branch office in the Mekong Delta under warm daylight",
        "text": None,
        "motion": "Subtle push-in shot capturing the genuine happiness of the farmer receiving his harvest earnings"
    },
    {
        "id": "CH02_SC038",
        "subject": "a prosperous rural hamlet in the Mekong Delta with newly built brick-roof houses, solar street lamps, and school children riding bicycles along paved concrete dikes",
        "setting": "a flourishing agrarian rural village in Dong Thap under bright warm afternoon sunshine",
        "text": None,
        "motion": "Horizontal camera tracking shot gliding past prosperous new houses in the rural rice farming village"
    },
    {
        "id": "CH02_SC039",
        "subject": "a modern rural byproduct processing plant converting rice husks into clean energy briquettes and extracting refined rice bran oil without any imported parts",
        "setting": "a local agro-industrial byproduct processing factory in An Giang under warm sunlight",
        "text": None,
        "motion": "Slow upward tilt following the automated conveyor processing rice husks into biofuel briquettes"
    },
    {
        "id": "CH02_SC040",
        "subject": "an official agrarian production status map displaying national annual paddy output steadfastly holding above forty-three million metric tons year after year",
        "setting": "the central command situation room of the Department of Crop Production under warm interior lighting",
        "text": "SAN LUONG LUA: > 43 TRIEU TAN",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the national output map"
    },
    {
        "id": "CH02_SC041",
        "subject": "an agricultural test plot signboard standing amidst a sea of dense ripe golden rice panicles confirming a harvest yield of six point one to over seven metric tons per hectare",
        "setting": "a vast high-yield demonstration paddy field in Thoai Son An Giang under warm golden sunshine",
        "text": "NANG SUAT DBSCL: 6.1 - 7.2 TAN/HA",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the harvest yield signboard"
    },
    {
        "id": "CH02_SC042",
        "subject": "a Food and Agriculture Organization global benchmark bar chart showing Vietnam at the very top of worldwide rice yield productivity per hectare",
        "setting": "an international agricultural agronomy conference display under warm architectural illumination",
        "text": None,
        "motion": "Slow upward tilt following Vietnam top-tier ranking on the FAO global rice yield leaderboard"
    },
    {
        "id": "CH02_SC043",
        "subject": "a massive international bulk cargo ship loaded with sacks of Vietnamese rice slowly departing the river port for foreign destinations under bright blue skies",
        "setting": "the navigation channel of the Hau River in Can Tho bathed in radiant golden morning sun",
        "text": "XUAT KHAU: 8 - 9 TRIEU TAN GAO",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the departing bulk freighter"
    },
    {
        "id": "CH02_SC044",
        "subject": "an authentic senior Vietnamese agricultural scientist resting his hands on a cup of warm lotus tea, looking thoughtfully through a window over the boundless rice fields",
        "setting": "an agrarian research institute office in the Mekong Delta at sunset under warm amber horizon light",
        "text": None,
        "motion": "Slow pull-back shot framing the thoughtful senior agricultural researcher looking over the fields"
    },
    {
        "id": "CH02_SC045",
        "subject": "an authentic Vietnamese rice farmer wiping sweat from his weathered brow, his focused eyes reflecting both pride and quiet concern for the harvest",
        "setting": "the edge of an An Giang rice paddy during harvest under warm golden afternoon light",
        "text": None,
        "motion": "Slow push-in shot focusing on the determined and resilient expression of the rice farmer"
    },
    {
        "id": "CH02_SC046",
        "subject": "rows of heavy sacks of freshly harvested moist paddy rice stacked along a canal embankment, farmers and grain brokers weighing sacks on a mechanical scale",
        "setting": "a rural canal dike in Dong Thap during peak harvest season under bright warm daylight",
        "text": None,
        "motion": "Horizontal camera tracking shot past stacks of freshly harvested moist paddy on the canal bank"
    },
    {
        "id": "CH02_SC047",
        "subject": "a small concrete drying courtyard in front of a rural house where a family turns harvested paddy manually using a traditional wooden grain rake",
        "setting": "a humble countryside household drying yard under pale afternoon sunshine",
        "text": None,
        "motion": "Subtle push-in shot toward the rustic wooden grain rake turning drying paddy on the concrete yard"
    },
    {
        "id": "CH02_SC048",
        "subject": "a field of heavily bent ripe golden rice stalks ready for harvest swaying gently, a farmer looking anxiously at gathering dark rain clouds on the distant horizon",
        "setting": "a ripe Mekong rice field during the urgent three-to-five day harvest window under dramatic warm sunlight",
        "text": None,
        "motion": "Dynamic sweeping pan across the heavily laden golden rice stalks bowing under their own weight"
    },
    {
        "id": "CH02_SC049",
        "subject": "a grain merchant counting cash notes inside a wooden river barge cabin while concluding a spot price agreement with a farmer standing on the wooden jetty",
        "setting": "a busy trading wharf on a Mekong canal in warm afternoon sunlight",
        "text": None,
        "motion": "Slow tracking shot gliding past the canal-side cash transaction between merchant and farmer"
    },
    {
        "id": "CH02_SC050",
        "subject": "a rural agricultural input supply depot stacked high with commercial chemical fertilizer sacks, the store manager updating a printed price board showing higher prices",
        "setting": "a busy farm supply shop in a rural district town under warm natural daylight",
        "text": None,
        "motion": "Slow push-in shot toward the updated chemical fertilizer retail price board"
    },
    {
        "id": "CH02_SC051",
        "subject": "a financial monitor screen displaying international crude oil and natural gas price surges, linking directly to imported urea fertilizer cost spikes",
        "setting": "an agricultural commodity market analysis desk under soft warm monitor lighting",
        "text": None,
        "motion": "Horizontal camera pan across the volatile global energy and fertilizer feedstock cost curve"
    },
    {
        "id": "CH02_SC052",
        "subject": "a comprehensive agricultural cost-accounting audit report showing that fertilizer, pesticides, and mechanical harvesting rentals consume up to eighty-five percent of crop revenue",
        "setting": "an agricultural economics research desk in Hanoi under focused warm reading light",
        "text": None,
        "motion": "Slow push-in shot toward the agrarian production input expenditure breakdown chart"
    },
    {
        "id": "CH02_SC053",
        "subject": "a farmer seasonal accounting ledger confirming a modest final net profit margin of only ten to fifteen percent remaining after deducting all machine rentals and input supplies",
        "setting": "a rustic farmstead wooden table under warm morning window light",
        "text": "BIEN LOI NHUAN NONG DAN: 10% - 15%",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 10-15% profit audit"
    },
    {
        "id": "CH02_SC054",
        "subject": "a serene and bustling morning market in a Mekong Delta town, where abundant baskets of fresh food and warm bowls of rice bring peace and security to everyday families",
        "setting": "a picturesque riverside market town in Southern Vietnam under gentle warm morning sunlight",
        "text": None,
        "motion": "Wide cinematic shot gliding smoothly across the peaceful everyday market life in the delta"
    },
    {
        "id": "CH02_SC055",
        "subject": "an agricultural policy roundtable bringing together rice farmers, mill owners, and government planners to map out an equitable rice value-chain distribution model",
        "setting": "a formal agricultural development symposium hall under warm ceiling lighting",
        "text": None,
        "motion": "Horizontal camera tracking shot past delegates reviewing the rice value-chain diagram"
    },
    {
        "id": "CH02_SC056",
        "subject": "an expansive lush green rice paddy stretching out into the distance, serving as a solid natural bedrock in the foreground with modern clean industrial plants on the horizon",
        "setting": "the harmonious boundary between agricultural fields and modern industrial parks under dawn sunlight",
        "text": None,
        "motion": "Slow upward tilt from heavy golden rice ears up to the rising industrial horizon"
    },
    {
        "id": "CH02_SC057",
        "subject": "an elevated agro-hydrological observation station overlooking the boundless canal grid and fertile green paddies of the Mekong Delta stretching to the horizon",
        "setting": "an observation tower in the Plain of Reeds under brilliant warm golden morning sunshine",
        "text": None,
        "motion": "Slow forward camera glide looking out from the observation tower across the vast delta"
    },
    {
        "id": "CH02_SC058",
        "subject": "a flotilla of large steel freight barges laden with golden paddy cutting white bow waves as they cruise in formation down the wide red-silt Mekong River waters",
        "setting": "the vast confluence of the Tien and Hau rivers under warm golden afternoon light",
        "text": None,
        "motion": "Epic panoramic aerial gliding shot following the continuous convoy of rice barges on the river"
    },
    {
        "id": "CH02_SC059",
        "subject": "a rural meteorological observation station with spinning anemometer cups and rain gauges under a dynamic tropical sky shifting between bright sun and passing clouds",
        "setting": "an agricultural weather research outpost surrounded by green rice paddies under warm sunlight",
        "text": None,
        "motion": "Slow horizontal camera pan across the spinning meteorological weather instruments"
    },
    {
        "id": "CH02_SC060",
        "subject": "a panoramic landscape showing three adjacent paddies in continuous cycle: one field being harvested of golden rice, one field lush with green seedlings, and one field flooded with rich silt",
        "setting": "a high-altitude overview of the Mekong Delta three-crop continuous agrarian biological cycle under golden sunrise",
        "text": "CO MAY SINH HOC 3 VU (365 NGAY)",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and the 3-crop rolling biological cycle"
    }
]

lines = []
for sc in scenes:
    sc_id = sc["id"]
    subj = sc["subject"]
    setting = sc["setting"]
    text_overlay = sc["text"]
    motion = sc["motion"]
    
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
