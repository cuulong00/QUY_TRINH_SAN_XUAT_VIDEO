# -*- coding: utf-8 -*-
import json
import os
import re

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'
visual_md_path = os.path.join(EPISODE_DIR, 'chapter_01_visual.md')
map_path = os.path.join(EPISODE_DIR, 'scene_timing_map.json')
out_txt = os.path.join(EPISODE_DIR, 'prompts_chapter_01.txt')

# English descriptions carefully translated from Chapter 01 3-tier matrix
english_scenes = {
    "SC001": {
        "subject": "a massive industrial automotive stamping mill with heavy steel gears slowly turning, amber sparks flying from cold metal teeth",
        "setting": "a shadowy industrial press shop hall",
        "motion": "Slow dramatic push-in shot toward the heavy steel gears of the stamping mill"
    },
    "SC002": {
        "subject": "a towering monumental stone customs barrier wall casting deep shadows across the factory floor, symbolizing punitive tariffs",
        "setting": "an imposing economic border checkpoint",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC003": {
        "subject": "abandoned classic American sedan silhouettes covered in thick dusty canvas tarps, resting motionless in the shadows",
        "setting": "the deserted foot of the customs wall inside an old warehouse",
        "motion": "Slow horizontal tracking pan across the draped automotive silhouettes"
    },
    "SC004": {
        "subject": "imported completely-built-up (CBU) shipping containers wrapped in heavy crimson security chains and padlocks, signifying commercial death",
        "setting": "a misty industrial cargo port under a slate sky",
        "motion": "Slow subtle zoom-in on the chained container locks"
    },
    "SC005": {
        "subject": "a grand ceremonial stone archway in New Delhi opening slightly, a beam of warm golden light cutting through the doorway into the dark market",
        "setting": "an imposing Indian government secretariat facade",
        "motion": "Slow forward camera glide toward the illuminated governmental doorway"
    },
    "SC006": {
        "subject": "an official stamped tax decree folder permitting import tariff reduction to a minimum floor of 15 percent",
        "setting": "the tax assessment chamber of the Indian Ministry of Finance",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC007": {
        "subject": "an official governmental foreign investment agreement binder committing a minimum capital expenditure of 500 million dollars",
        "setting": "an executive conference room in New Delhi under warm spotlight",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC008": {
        "subject": "thick tensioned steel cables coiling around institutional compliance dossiers on an iron desk, symbolizing severe regulatory constraints",
        "setting": "a formal institutional negotiation room",
        "motion": "Subtle slow zoom-out revealing the taut steel cable coiling around the policy ledgers"
    },
    "SC009": {
        "subject": "a vertical bar chart on an engineering blackboard showing steep escalating annual localization milestones marked with red audit lines",
        "setting": "a factory compliance control room",
        "motion": "Slow upward tilt revealing the escalating compliance bar graph"
    },
    "SC010": {
        "subject": "a heavy cast-iron audit safe open revealing a red statutory tax clawback order stamped with institutional seals",
        "setting": "a dimly lit government revenue audit archive",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC011": {
        "subject": "an antique brass balance scale resting on a dark walnut desk, tilted with light tax incentives on one side and a heavy localization mandate on the other",
        "setting": "an executive legal counsel office",
        "motion": "Slow tracking shot across the unbalanced brass scale of justice"
    },
    "SC012": {
        "subject": "the expansive modern automotive manufacturing complex of Thoothukudi with sleek flat-roofed assembly halls beside the coastal perimeter",
        "setting": "the industrial coastal plains of Tamil Nadu",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC013": {
        "subject": "an industrial digital monitoring terminal glowing in cyan indicating a planned manufacturing capacity of 50,000 electric vehicles per year",
        "setting": "the intelligent plant control room at Thoothukudi",
        "motion": "Horizontal telemetry tracking shot across the digital console"
    },
    "SC014": {
        "subject": "an architectural masterplan blueprint spread wide on a drafting table, demarcating Phase One as an assembly-only facility",
        "setting": "the project engineering office",
        "motion": "Diagonal drafting pan shot across the architectural masterplan"
    },
    "SC015": {
        "subject": "industrial robotic welding arms in an automotive body shop striking precise welding arcs with bright terracotta sparks",
        "setting": "the Thoothukudi body shop line",
        "motion": "Robotic line tracking shot along the active welding bay"
    },
    "SC016": {
        "subject": "an empty factory zoning sector on a drafting schematic marked with dashed lines, highlighting the absence of in-house body stamping and battery cell shops",
        "setting": "the industrial site planning table",
        "motion": "Slow pan across the vacant factory zoning diagram"
    },
    "SC017": {
        "subject": "a fleet of sleek finished VF 6 and VF 7 electric crossovers parked in neat rows under the southern Indian sun",
        "setting": "the exterior vehicle dispatch yard of Thoothukudi",
        "motion": "Slow tracking shot along the glistening vehicle fleet"
    },
    "SC018": {
        "subject": "industrial wooden crates containing CKD component kits stamped with Cat Hai shipping tags loaded at the deepwater port",
        "setting": "the maritime export terminal at Cat Hai port in Hai Phong",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC019": {
        "subject": "technicians unboxing imported CKD kits and rapidly assembling them onto unibody frames along the line",
        "setting": "the final assembly conveyor hall at Thoothukudi",
        "motion": "Tracking shot following the active CKD component assembly flow"
    },
    "SC020": {
        "subject": "a Vietnamese automotive engineer looking thoughtfully at a value-addition chart plateauing below statutory localization targets",
        "setting": "a strategy briefing room",
        "motion": "Slow push-in toward the lead engineer studying the localization plateau"
    },
    "SC021": {
        "subject": "Vietnamese engineering leads shaking hands and conferring with over three hundred local Indian precision tooling suppliers around display tables",
        "setting": "a grand automotive supplier summit in Chennai",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC022": {
        "subject": "detailed CAD blueprints of outer body panels for three vehicle models: the mini VF 3, VF 6 crossover, and VF 7 SUV spread across workbenches",
        "setting": "an automotive collaborative engineering center",
        "motion": "Diagonal tracking pan across stamping schematics"
    },
    "SC023": {
        "subject": "an Indian precision tooling specialist using digital calipers to measure a prototype body stamping die block on a granite surface",
        "setting": "a specialized machine shop in southern India",
        "motion": "Close-up inspection of prototype tooling die"
    },
    "SC024": {
        "subject": "a high-speed CNC milling machine head carving contours into a prototype steel die block with fine coolant spray and sparks",
        "setting": "a heavy precision tool-and-die workshop",
        "motion": "Slow camera glide alongside the precision CNC cutter"
    },
    "SC025": {
        "subject": "a formal corporate executive memorandum on company letterhead ordering the immediate suspension of localization programs for all three car platforms",
        "setting": "an executive mahogany desk under focused desk lamp",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC026": {
        "subject": "audited engineering tooling expense ledgers and prototype development receipts sent from hundreds of local machine shops stacked neatly",
        "setting": "an industrial financial auditing department",
        "motion": "Slow tracking shot across tooling expense forms"
    },
    "SC027": {
        "subject": "formal financial settlement vouchers stamped with banking verification for actual incurred tooling costs, proving responsible compensation",
        "setting": "a corporate finance meeting room in India",
        "motion": "Slow push-in on the sealed settlement voucher"
    },
    "SC028": {
        "subject": "automotive market analysts and journalists conversing intensely before illuminated trading and news monitors over the unexpected withdrawal",
        "setting": "a financial newsroom and market desk",
        "motion": "Panning shot across discussing market analysts"
    },
    "SC029": {
        "subject": "a large noir graphic question mark superimposed over the architectural layout of the 500 million dollar Thoothukudi plant",
        "setting": "the darkened project schematic board",
        "motion": "Slow subtle push-in on the question mark over the plant layout"
    },
    "SC030": {
        "subject": "the Thoothukudi manufacturing plant glowing warmly with bright factory windows at night, with active forklifts and workers moving steadily",
        "setting": "an exterior wide panoramic view of the plant at dusk",
        "motion": "Wide exterior tracking shot showing uninterrupted nighttime operations"
    },
    "SC031": {
        "subject": "the active final assembly conveyor running smoothly as workers seamlessly assemble electric SUVs from imported CKD modules",
        "setting": "inside the brightly lit Thoothukudi assembly shop",
        "motion": "Tracking shot following the uninterrupted CKD vehicle line"
    },
    "SC032": {
        "subject": "the Indian government's official Vahan vehicle registry digital interface displaying a sharp surge in VinFast registrations for August 2026",
        "setting": "a national transport database telemetry screen",
        "motion": "Slow analytical dashboard scan shot across registration data"
    },
    "SC033": {
        "subject": "an Indian electric vehicle market ranking podium showing VinFast climbing solidly into the Top 4 brand position",
        "setting": "an industry statistical leaderboard display",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    },
    "SC034": {
        "subject": "dealership staff in southern India handing over vehicle keys of newly delivered VF 6 and VF 7 SUVs to Indian customers outside an illuminated showroom",
        "setting": "the exterior of a modern dealership at dusk",
        "motion": "Slow panning shot across newly delivered electric vehicles"
    },
    "SC035": {
        "subject": "multi-car transporter trucks loaded with newly assembled electric SUVs driving out of the factory dispatch gate toward national highways",
        "setting": "the plant transport gate at Thoothukudi",
        "motion": "Wide tracking shot following transporter trucks exiting the complex"
    },
    "SC036": {
        "subject": "a financial graph on a tablet screen showing long-term freight tariffs and customs duties escalating over time if relying solely on imports",
        "setting": "an industrial economist's workstation",
        "motion": "Subtle push-in on the escalating tariff trajectory"
    },
    "SC037": {
        "subject": "a symbolic tensioned customs cable hovering high above a container ship, representing India's inescapable long-term tariff trap",
        "setting": "the misty entrance of an industrial harbor",
        "motion": "Low-angle upward tilt toward the symbolic tariff cable"
    },
    "SC038": {
        "subject": "an executive conference table with the tooling reimbursement decree at the center, surrounded by intense chiaroscuro shadows and analytical dossiers",
        "setting": "a closed boardroom in dramatic noir lighting",
        "motion": "Slow tense push-in toward the center of the boardroom table"
    },
    "SC039": {
        "subject": "an enormous solid alloy steel automotive stamping die block glistening under harsh directional spotlight, cold and menacing",
        "setting": "a shadowy heavy tool-and-die fabrication bay",
        "motion": "Dramatic slow push-in toward the giant steel die block"
    },
    "SC040": {
        "subject": "glowing mathematical fixed-cost amortization formulas etched directly across the mirror-polished face of the giant steel stamping die",
        "setting": "the surface of the automotive die block",
        "motion": "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
    }
}

# 10 Selected Overlays (exactly 25% of 40 scenes)
overlays = {
    "SC002": "THUẾ QUAN 70% - 100%",
    "SC006": "ƯU ĐÃI THUẾ: 15%",
    "SC007": "CAM KẾT: 500 TRIỆU USD",
    "SC010": "TRUY THU THUẾ TOÀN BỘ",
    "SC012": "THOOTHUKUDI: 50.000 XE/NĂM",
    "SC018": "LINH KIỆN CKD CÁT HẢI",
    "SC021": "300+ XƯỞNG CƠ KHÍ BẢN ĐỊA",
    "SC025": "TẠM DỪNG NỘI ĐỊA HÓA",
    "SC033": "TOP 4 THỊ PHẦN (8/2026)",
    "SC040": "BÀI TOÁN KHẤU HAO KHUÔN DẬP"
}

# Update scene_timing_map.json and build prompts_chapter_01.txt
with open(map_path, 'r', encoding='utf-8') as f:
    scenes = json.load(f)

prompt_lines = []
for s in scenes:
    if s['chapter'] == '01':
        sc_id = s['id']
        eng = english_scenes[sc_id]
        ov = overlays.get(sc_id, "")
        
        s['text_overlay'] = ov
        
        if ov:
            # User specification:
            # "chữ nhỏ thôi nhé, đừng quá lớn, và đặt ở vị trí cố định góc trái màn hình phía dưới, cách bottom 25%"
            overlay_clause = (
                f', compact subtle glowing terracotta orange 3D typography text overlay '
                f'positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), '
                f'facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading "{ov}"'
            )
            motion = "Steady camera shot maintaining perfect focus on the lower-left typography and subject"
        else:
            overlay_clause = ""
            motion = eng['motion']
            
        img_prompt = (
            f"A 2D cinematic editorial noir illustration of {eng['subject']}, "
            f"set in {eng['setting']}, minimalist graphic novel aesthetic, clean bold ink outlines, "
            f"stylized flat vector textures, dark warm charcoal background (#1A1A1A), "
            f"dramatic chiaroscuro lighting, deep noir shadows{overlay_clause}."
        )
        
        vid_prompt = (
            f"@{sc_id}.png -> {motion}, "
            f"preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, "
            f"8-second continuous documentary video --ar 16:9"
        )
        
        s['image_prompt'] = img_prompt
        s['video_prompt'] = vid_prompt
        s['camera_motion'] = motion
        
        prompt_lines.append(f"{sc_id} [IMAGE]: {img_prompt}")
        prompt_lines.append(f"{sc_id} [VIDEO]: {vid_prompt}\n")

with open(map_path, 'w', encoding='utf-8') as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

with open(out_txt, 'w', encoding='utf-8') as f:
    f.write('\n'.join(prompt_lines))

print("Successfully generated 100% English prompt descriptions with small lower-left (25% from bottom) typography for Chapter 01!")
