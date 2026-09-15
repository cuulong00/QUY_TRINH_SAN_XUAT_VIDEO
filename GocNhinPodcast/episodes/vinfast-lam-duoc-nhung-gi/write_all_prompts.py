import json
import os

with open('scene_timing_map.json', 'r', encoding='utf-8') as f:
    scene_map = json.load(f)

# Define descriptions for each scene
# Since descriptions are detailed, we can map them systematically.
# We will use the correct descriptions matching the actual sentence text of each scene.

desc_map = {}

# Chapter 1 (SC001 - SC011)
desc_map["SC001"] = {
    "img": "A flat 2D vector graphic of the glowing electric green VinFast V logo positioned in the center, casting a soft green aura. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the glowing V logo, a subtle green lens flare pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC002"] = {
    "img": "A flat 2D vector graphic of various automotive parts, including a green battery pack, a small computer chip, and metal gears, all laid out on a dark gridded surface. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as a thin scanning beam of green light sweeps across the automotive parts, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC003"] = {
    "img": "A flat 2D vector graphic of a fleet of VinFast VF8 electric SUVs driving forward in unison on a highway, green energy lines trailing behind them. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera zoom-in on the fleet of VF8 SUVs as they drive forward smoothly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC004"] = {
    "img": "A flat 2D vector infographic showing a vertical bar chart of market sales in Vietnam, with the tallest bar highlighted in glowing electric green and topped with the letter V. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the bar chart, the tallest bar slowly pulsing with a soft cream glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC005"] = {
    "img": "A flat 2D vector graphic of two large industrial factories, one labeled with the English text \"HAIPHONG\" and the other \"HATINH\", connected by a dotted line. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right from the Haiphong factory to the Hatinh factory along the dotted line, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC006"] = {
    "img": "A flat 2D vector graphic of a sleek electric car, with the glowing green letter \"V\" on the front grille. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a slow spotlight sweeping over the front grille of the electric car, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC007"] = {
    "img": "A flat 2D vector graphic representing layers of a car peeling back, showing first the outer steel chassis, then a glowing battery, then a microchip. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera zoom-in as the chassis layers peel back to reveal the internal battery and microchip, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC008"] = {
    "img": "A flat 2D vector graphic showing the bold English text \"LOCALIZATION RATE\" on a dark screen, with a percentage scale below it. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the screen, the percentage text pulsing with a soft white glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC009"] = {
    "img": "A flat 2D vector graphic of the number \"60%\" in glowing cream, which slowly morphs into the number \"84%\" in glowing electric green. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the cream \"60%\" digits morph and transition into the green \"84%\" digits, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC010"] = {
    "img": "A flat 2D vector graphic of a classic dictionary book open on a wooden table, the word \"DEFINITION\" highlighted in glowing green. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the open dictionary book, a soft spotlight focusing on the highlighted word, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC011"] = {
    "img": "A flat 2D vector graphic of three cars from different brands with the English logos \"TOYOTA\", \"HONDA\", and \"FORD\" parked in a row. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the Toyota, Honda, and Ford cars in the row, preserving the details of the reference image, 8-second continuous documentary video"
}

# Chapter 2 (SC012 - SC043)
desc_map["SC012"] = {
    "img": "A flat 2D vector graphic showing the bold English text \"DEFINITION GAME\" on a dark screen overlaying a grid pattern. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the text, the letters pulsing with a soft white glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC013"] = {
    "img": "A flat 2D vector graphic of stairs labeled with different car brands, with the top step labeled \"30% LOCALIZATION\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning up the stairs to the top \"30%\" label step, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC014"] = {
    "img": "A flat 2D vector graphic of a Toyota car outline with the logo \"TOYOTA\" glowing under a spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight sweeping over the glowing Toyota car outline, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC015"] = {
    "img": "A flat 2D vector graphic of a Honda car outline with the logo \"HONDA\" glowing under a spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight sweeping over the glowing Honda car outline, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC016"] = {
    "img": "A flat 2D vector graphic of a Ford car outline with the logo \"FORD\" glowing under a spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight sweeping over the glowing Ford car outline, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC017"] = {
    "img": "A flat 2D vector graphic of a shipping container opening to reveal rows of wooden crates stamped with \"CKD PARTS\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the container door slides open under the spotlight, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC018"] = {
    "img": "A flat 2D vector graphic showing the silhouette of a worker in loose working clothes fastening a car door panel on an assembly line. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the worker fastens the panel, sparks glinting softly under cleanroom light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC019"] = {
    "img": "A flat 2D vector graphic of a hand holding a stamp and stamping \"MADE IN VIETNAM\" in bold cream text on a document. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the stamp presses down, leaving a glowing print on the document, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC020"] = {
    "img": "A flat 2D vector graphic of a single metallic screw sitting on a dark surface under a bright spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the screw under the spotlight, a slow rotation effect on the shadow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC021"] = {
    "img": "A flat 2D vector graphic of a timeline diagram showing key dates \"1995\", \"2005\", and \"2015\" marked with green circles. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the dates on the timeline diagram, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC022"] = {
    "img": "A flat 2D vector graphic of a document labeled \"LOCALIZATION 60%\" under a red skeptical light beam. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the document, the red light beam pulsing gently, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC023"] = {
    "img": "A flat 2D vector graphic of a balance scale with empty plates swaying slowly under a soft spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the balance scale, the plates slowly swaying, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC024"] = {
    "img": "A flat 2D vector graphic of an official document titled \"DECISION 28/2004\" lying on a dark wooden table. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a slow zoom-in on the document title, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC025"] = {
    "img": "A flat 2D vector infographic showing a scoring grid with labels \"10 pts\" and \"15 pts\" highlighted in glowing cream. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the scoring grid, the point values pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC026"] = {
    "img": "A flat 2D vector graphic of a car chassis frame highlighted in copper metallic lines on a dark background. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a green scanning beam moving along the highlighted chassis frame, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC027"] = {
    "img": "A flat 2D vector graphic of a blank microchip with a red cross over a LiDAR sensor icon. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the red cross over the LiDAR icon slowly pulsing, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC028"] = {
    "img": "A flat 2D vector graphic of a calendar page with \"OCTOBER 2022\" glowing in white text under a spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the calendar page, the date text glowing softly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC029"] = {
    "img": "A flat 2D vector graphic of a red stamp with the text \"ANNULLED\" stamped over the \"DECISION 28/2004\" document. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the annulled stamp presses down onto the document, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC030"] = {
    "img": "A flat 2D vector blueprint showing calculations labeled \"VALUE ADDED METHOD\" in cream font. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the blueprint, the text and lines pulsing softly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC031"] = {
    "img": "A flat 2D vector graphic of a car silhouette partitioned into green (domestic) and grey (imported) segments. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a slow highlight sweep across the green domestic segment, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC032"] = {
    "img": "A flat 2D vector graphic of a minimalist globe showing trade routes highlighted in soft cyan lines. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the globe rotating slowly on its axis, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC033"] = {
    "img": "A flat 2D vector graphic of an official document titled \"ORIGIN CERTIFICATE\" with a gold seal in the corner. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight slowly shifting to highlight the gold seal, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC034"] = {
    "img": "A flat 2D vector graphic of the number \"60%\" glowing green over a VinFast VF8 car dashboard screen. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the dashboard display digits pulsing with a soft green light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC035"] = {
    "img": "A flat 2D vector graphic of a battery pack with a cost label showing \"30%-40% COST\" in glowing cream. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the cost label glowing and pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC036"] = {
    "img": "A flat 2D vector graphic of a box filled with raw silicon wafers, labeled with the text \"IMPORTED\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight sweeping over the imported silicon wafer box, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC037"] = {
    "img": "A flat 2D vector graphic of a robotic assembly arm sealing a battery pack case stamped with the logo \"VinES\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the robot arm moving in sync to seal the case, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC038"] = {
    "img": "A flat 2D vector graphic of a PMSM motor outline, a car interior chassis, and green BMS code lanes connected to each other. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, green light pulses flowing along the connection lanes, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC039"] = {
    "img": "A flat 2D vector graphic of dark cell blocks and microchip outlines labeled with the text \"NOT SELF-SUFFICIENT\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the outlines, the text pulsing with a soft warning light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC040"] = {
    "img": "A flat 2D vector graphic of a wooden desk holding plates of food next to a bag of raw rice labeled \"EXTERNAL PURCHASE\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a slow spotlight sweeping over the raw rice bag, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC041"] = {
    "img": "A flat 2D vector graphic showing a growth line graph starting at a 60% mark and pointing upwards. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the growth line slowly draws upwards from the 60% point, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC042"] = {
    "img": "A flat 2D vector graphic of the numbers \"84%\" and \"2026\" glowing green under a spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the glowing numbers, a soft green lens flare pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC043"] = {
    "img": "A flat 2D vector graphic of a large balance scale, the left plate holding \"30 Years CKD\" and the right plate holding \"VinFast 84%\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the scale, the right plate containing VinFast dipping lower and glowing green, preserving the details of the reference image, 8-second continuous documentary video"
}

# Chapter 3 (SC044 - SC063)
desc_map["SC044"] = {
    "img": "A flat 2D vector blueprint showing the layout of a factory complex labeled \"HAIPHONG - 335 HECTARES\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the blueprint layout, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC045"] = {
    "img": "A flat 2D vector graphic of a modern factory building entrance with the English text \"STAMPING SHOP\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the stamping shop entrance, a soft green light pulsing around the text, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC046"] = {
    "img": "A flat 2D vector graphic of a massive roll of steel sheet, with a digital caliper measuring its thickness as \"0.7mm\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a slow highlight beam sweeping across the roll of steel, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC047"] = {
    "img": "A flat 2D vector graphic of a steel sheet passing through a giant hydraulic press machine. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the hydraulic press slides down and presses the steel sheet, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC048"] = {
    "img": "A flat 2D vector graphic of a giant metal servo press machine labeled with the English text \"SCHULER GERMANY\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the press machine, the brand text pulsing with a soft white glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC049"] = {
    "img": "A flat 2D vector graphic of stamped car door panels being lifted by an automated robotic arm. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the robot arm moving in sync to lift and stack the door panels, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC050"] = {
    "img": "A flat 2D vector graphic of a digital telemetry screen displaying the text \"15 PARTS / MIN\" in glowing cream. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the telemetry screen, the digits pulsing with a soft glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC051"] = {
    "img": "A flat 2D vector graphic of orange robotic arms welding a car frame, casting glowing orange sparks. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the orange robotic arms as they weld, sparks pulsing and flying outward slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC052"] = {
    "img": "A flat 2D vector graphic showing schematic laser scanners sweeping along joints, displaying \"100% AUTOMATED\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the laser scan lines sweeping back and forth over the joints, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC053"] = {
    "img": "A flat 2D vector graphic of a completed car frame rolling off a conveyor, with a digital display showing \"102 SEC\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the frame rolling forward, the timer display digits glowing softly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC054"] = {
    "img": "A flat 2D vector infographic chart showing \"35 CARS / HOUR\", with a crossed-out label \"NO CKD\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the chart, the text pulsing with a soft white glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC055"] = {
    "img": "A flat 2D vector graphic of an empty wooden crate, showing zero loose fasteners or bolts inside. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight slowly sweeping across the empty wooden crate, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC056"] = {
    "img": "A flat 2D vector graphic showing a complete closed production cycle diagram, with the VinFast V logo in the center. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, green light pulses flowing along the cycle diagram path, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC057"] = {
    "img": "A flat 2D vector graphic of a Vietnamese engineer in loose working clothes observing a robot arm with three glowing question marks. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the question marks slowly pulsing with a soft cream light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC058"] = {
    "img": "A flat 2D vector graphic comparing two cargo boxes side-by-side: one labeled \"PRODUCTION TOOLS\", the other \"FINISHED PARTS\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight alternating between the two cargo boxes, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC059"] = {
    "img": "A flat 2D vector graphic comparing a Tesla factory with \"KUKA\" robot arms to a Hyundai factory with \"FANUC\" robot arms. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the Tesla and Hyundai comparison frames, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC060"] = {
    "img": "A flat 2D vector graphic of a standard engineering design manual titled \"TESLA STANDARD\" lying on a dark table. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a slow zoom-in on the design manual title, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC061"] = {
    "img": "A flat 2D vector graphic of the VinFast letter V enclosing the chassis design lines of an electric SUV. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the V logo and chassis lines glowing with a soft green light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC062"] = {
    "img": "A flat 2D vector graphic of a mechanical architect in loose clothes rolling out blueprints marked \"OWNED BLUEPRINT\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the blueprints roll out, the owned blueprint text highlighted in cream, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC063"] = {
    "img": "A flat 2D vector graphic of a VinFast VF8 safety steel cage frame shining with a soft silver outline in the dark. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the silver outline of the safety cage frame pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video"
}

# Chapter 4 (SC064 - SC084)
desc_map["SC064"] = {
    "img": "A flat 2D vector graphic of a vehicle chassis, with the central motor module highlighted in glowing green under the floor. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the highlighted motor module pulsing with a soft green glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC065"] = {
    "img": "A flat 2D vector graphic of a motor assembly housing labeled with the English text \"PMSM MOTOR\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the housing, the text \"PMSM MOTOR\" glowing softly under a spotlight, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC066"] = {
    "img": "A flat 2D vector graphic of a sleek electric car chassis, with the engine and gearbox modules grayed out and crossed out. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight sweeping over the electric car chassis, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC067"] = {
    "img": "A flat 2D vector graphic of a motor assembly line in Vietnam, showing cylindrical rotors passing through a cleanroom. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the assembly line, the rotors glinting under cleanroom light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC068"] = {
    "img": "A flat 2D vector graphic of automated machines labeled with the European brands \"GROB\" and \"THYSSENKRUPP\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the GROB and ThyssenKrupp machines, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC069"] = {
    "img": "A flat 2D vector graphic of an assembly testbed labeled with the English text \"AVL LIST\" and \"EISENMANN\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning left across the AVL List and Eisenmann equipment, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC070"] = {
    "img": "A flat 2D vector graphic displaying three steps of motor manufacturing: stator winding, rotor insertion, and dyno test. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, split-screen panels highlighting the three manufacturing steps in sequence, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC071"] = {
    "img": "A close-up 2D flat vector graphic of a cylindrical rotor displaying Neodymium earth magnets inside. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the internal Neodymium magnets pulse with a soft orange glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC072"] = {
    "img": "A flat 2D vector graphic of high quality copper wire spools labeled \"IMPORTED COPPER\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight slowly sweeping over the copper wire spools, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC073"] = {
    "img": "A flat 2D vector graphic of a crossed-out metal refinery, representing the absence of local metallurgy. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the refinery outline, the red cross slowly pulsing, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC074"] = {
    "img": "A flat 2D vector graphic of a VinFast electric bus outline labeled \"EB12\" with the drive axle highlighted. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the bus outline, the drive axle pulsing with a soft cream glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC075"] = {
    "img": "A flat 2D vector graphic of a drive axle module labeled with the English text \"ZF AXTRAX 2 GERMANY\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a slow zoom-in on the AxTrax 2 brand text, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC076"] = {
    "img": "A flat 2D vector graphic of a factory floor assembling motor systems under the VinFast logo V. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, conveyor belts moving motor housings smoothly under the logo, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC077"] = {
    "img": "A flat 2D vector graphic of import shipping crates labeled \"NEODYMIUM MAGNETS\" and \"COPPER COILS\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the shipping crates on the loading dock, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC078"] = {
    "img": "A flat 2D vector graphic of the Tesla logo with a mining truck in the background, crossed-out with a red line. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the red cross line over the mining truck pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC079"] = {
    "img": "A flat 2D vector graphic of the Toyota logo next to shipping boxes labeled \"NEODYMIUM FROM CHINA\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight slowly shifting to highlight the shipping boxes, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC080"] = {
    "img": "A flat 2D vector graphic of a balance scale, the left plate labeled \"RAW MATERIAL\" and the right plate \"PROCESS CONTROL\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the balance scale, the plates slowly swaying under the spotlight, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC081"] = {
    "img": "A flat 2D vector industrial diagram showing raw minerals converting to a finished motor package. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, green light pulses tracing the transformation path on the diagram, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC082"] = {
    "img": "A flat 2D vector graphic of a computer screen displaying a large green \"SUBSCRIBE\" button next to the YouTube icon. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the screen, the green button slowly pulsing with light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC083"] = {
    "img": "A flat 2D vector graphic of a large balance scale, the left plate labeled \"CHASSIS & MOTOR\" and the right plate \"BATTERY PACK\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the scale, the right plate containing the battery pack dipping lower, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC084"] = {
    "img": "A flat 2D vector graphic of a foggy landscape with a road splitting into two paths, representing complexity. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right along the split path, the fog drifting slowly, preserving the details of the reference image, 8-second continuous documentary video"
}

# Chapter 5 (SC085 - SC126)
desc_map["SC085"] = {
    "img": "A flat 2D vector graphic of a large electric battery pack inside a car silhouette, with a cost tag showing \"30% - 40% COST\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows, --ar 16:9",
    "vid": "steady shot of the battery pack, the cost tag pulsing with a soft cream glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC086"] = {
    "img": "A flat 2D vector graphic of a balance scale, one side holding a heavy battery pack block, the other side holding a car chassis frame. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot of the scale, the plates slowly swaying, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC087"] = {
    "img": "A flat 2D vector graphic of a battery pack splitting vertically into 3 distinct highlighted layers under a spotlight. Dark charcoal grey background, warm cream outlines,",
    "vid": "slow camera zoom-in on the 3 highlighted layers of the battery pack, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC088"] = {
    "img": "A close-up 2D flat vector graphic of a single cylindrical battery cell showing lithium ions moving between anode and cathode. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot as the lithium ions pulse and move slowly between the electrodes, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC089"] = {
    "img": "A flat 2D vector graphic of orange robot arms assembling rows of cylindrical cells into a heavy aluminum housing block. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot, the robot arms moving in sync to position the battery cells, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC090"] = {
    "img": "A flat 2D vector graphic of a battery pack layout, showing routing of blue cooling tubes and a green protective circuit board. Dark charcoal grey background,",
    "vid": "steady shot, blue liquid animating along the cooling tube channels, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC091"] = {
    "img": "A flat 2D vector graphic of a digital dashboard displaying battery statistics with green check marks next to \"TEMP\" and \"SPEED\". Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot, the dashboard screen stats pulsing with a soft light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC092"] = {
    "img": "A flat 2D vector graphic of the 3-layer battery diagram, with the top two layers glowing in electric green, and the bottom layer grayed out. Dark charcoal grey background,",
    "vid": "steady shot, a slow highlight light sweep across the top two green layers, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC093"] = {
    "img": "A flat 2D vector graphic showing the logo \"VinES\" morphing and dissolving into the main \"VINFAST\" logo with a bright green glow. Dark charcoal grey background,",
    "vid": "steady shot as the two logos blend together, the green light slowly spreading, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC094"] = {
    "img": "A flat 2D vector infographic organizational chart showing \"VINGROUP\" at the top, branching down to \"VinES\" and \"VINFAST\", then merging. Dark charcoal grey background,",
    "vid": "steady shot, green connection arrows slowly tracing the path from VinES to VinFast, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC095"] = {
    "img": "A flat 2D vector graphic of three incoming data streams labeled \"R&D\", \"PROD\", and \"COMMERCE\" merging into a central battery icon. Dark charcoal grey background,",
    "vid": "steady shot as the streams pulse and flow into the battery icon, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC096"] = {
    "img": "A flat 2D vector graphic of a large modern factory facade under a spotlight, with the English text \"VUNG ANG BATTERY PLANT\". Dark charcoal grey background,",
    "vid": "slow camera panning right across the facade of the Vung Ang battery plant, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC097"] = {
    "img": "A flat 2D vector graphic of a mechanical engineer in loose working clothes viewing a CAD model of a battery pack on a screen. Dark charcoal grey background,",
    "vid": "steady shot, the CAD model on the screen slowly rotating, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC098"] = {
    "img": "A flat 2D vector graphic of a shipping crate filled with raw battery cells stamped with the logo \"CATL\". Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot, a slow spotlight sweeping across the CATL cell shipping crate, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC099"] = {
    "img": "A flat 2D vector graphic of cargo boxes labeled \"CATL\" and \"GOTION HIGH-TECH\" sitting on a dark warehouse shelf. Dark charcoal grey background,",
    "vid": "slow camera panning left across the CATL and Gotion cargo boxes on the shelf, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC100"] = {
    "img": "A flat 2D vector graphic showing a contract document signed by VinES and Gotion, with Gotion holding a 51% share pie chart segment. Dark charcoal grey background,",
    "vid": "steady shot of the document, the \"51%\" share marker slowly highlighted in soft orange, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC101"] = {
    "img": "A flat 2D vector graphic of a conveyor belt carrying newly manufactured cylindrical cells out of a cleanroom machine. Dark charcoal grey background,",
    "vid": "steady shot of the conveyor belt moving, cell casings glinting in cleanroom light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC102"] = {
    "img": "A flat 2D vector graphic of a digital LED display counter in a cleanroom showing \"5 GWh / YEAR\" in glowing orange text. Dark charcoal grey background,",
    "vid": "steady shot of the display counter as the digits pulse gently, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC103"] = {
    "img": "A flat 2D vector graphic of a corporate building showing logos of \"GOTION\" (dominant) and \"VinES\" side-by-side, under a dark sky. Dark charcoal grey background,",
    "vid": "slow camera zoom-in on the Gotion and VinES logos, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC104"] = {
    "img": "A flat 2D vector graphic of a balance scale weighing a single battery cell under a spotlight, representing evaluation. Dark charcoal grey background,",
    "vid": "steady shot of the scale, the plates slowly settling under the spotlight, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC105"] = {
    "img": "A flat 2D vector graphic of a large balance scale comparing the logo \"VINFAST\" against \"TESLA\" and \"BYD\" under spotlights. Dark charcoal grey background,",
    "vid": "steady shot of the balance scale, the plates slowly swaying, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC106"] = {
    "img": "A flat 2D vector graphic of a large hourglass with sand falling slowly, casting a long shadow on a dark table. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot as sand grains trickle down the hourglass, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC107"] = {
    "img": "A flat 2D vector graphic showing the bold English text \"TESLA 2003\" displayed on a dark background. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot of the text \"TESLA 2003\" glowing with a soft white light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC108"] = {
    "img": "A flat 2D vector graphic of a timeline chart highlighting \"BYD 1995 (BATTERY)\" and \"BYD 2003 (CAR)\" in glowing orange. Dark charcoal grey background,",
    "vid": "steady shot of the timeline chart, the two dates pulsing with orange light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC109"] = {
    "img": "A flat 2D vector graphic of a VinFast VF e34 electric car parked under a spotlight, with the text \"VINFAST EV 2021\" glowing above it. Dark charcoal grey background,",
    "vid": "steady shot of the VF e34 car under the spotlight, the text \"2021\" glowing softly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC110"] = {
    "img": "A flat 2D vector graphic of a silhouette of a small child holding a green letter V next to two massive adult silhouettes (Tesla, BYD). Dark charcoal grey background,",
    "vid": "steady shot of the child and the giant silhouettes, a slow light beam sweeping and casting long shadows, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC111"] = {
    "img": "A flat 2D vector graphic of the child silhouette growing larger, with green speed streaks running past the background. Dark charcoal grey background,",
    "vid": "steady shot of the expanding silhouette, speed lines zooming past, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC112"] = {
    "img": "A flat 2D vector graphic of a target board with a green arrow hit directly on the \"60% LOCALIZATION\" ring. Dark charcoal grey background,",
    "vid": "steady shot as the arrow in the target board pulses with a soft green light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC113"] = {
    "img": "A flat 2D vector graphic of a modern factory complex with smoking cooling towers and truck fleets. Dark charcoal grey background, warm cream outlines,",
    "vid": "slow camera panning right across the factory complex and truck fleets, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC114"] = {
    "img": "A flat 2D vector graphic of a gold medal engraved with the VinFast V logo sitting on a velvet surface. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot, a spotlight slowly shifting to highlight the engraved V logo, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC115"] = {
    "img": "A flat 2D vector graphic showing split screen comparing factory footprints of VinFast, Tesla, and BYD. Dark charcoal grey background,",
    "vid": "slow camera zoom-out showing the three comparison frames, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC116"] = {
    "img": "A flat 2D vector graphic of a vertical supply chain tree of BYD, showing lithium mines at the roots and a battery pack at the top. Dark charcoal grey background,",
    "vid": "slow camera panning up from the roots to the top battery pack of the BYD tree, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC117"] = {
    "img": "A flat 2D vector graphic of a mining excavator digging lithium ore, connected to an assembly line showing battery cell packages. Dark charcoal grey background,",
    "vid": "steady shot of the excavator, the assembly line in the background active, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC118"] = {
    "img": "A flat 2D vector graphic of a giant question mark silhouette over a Tesla factory blueprint. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot, the question mark silhouette pulsing with a soft white glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC119"] = {
    "img": "A flat 2D vector graphic showing a Tesla Model 3 car being fitted with a battery pack labeled \"CATL LFP CELL\". Dark charcoal grey background,",
    "vid": "steady shot as the battery pack slides under the Model 3 chassis, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC120"] = {
    "img": "A flat 2D vector graphic of a shipping container filled with battery cells labeled with the logo \"CATL\". Dark charcoal grey background,",
    "vid": "steady shot as the container door slides open under a spotlight, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC121"] = {
    "img": "A flat 2D vector graphic of Tesla Model Y and Model 3 cars parked near cargo boxes stamped with \"CATL LFP CELL\". Dark charcoal grey background,",
    "vid": "slow camera panning right across the Tesla cars and CATL cargo boxes, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC122"] = {
    "img": "A flat 2D vector graphic showing two parallel boxes labeled \"TESLA MODEL\" and \"VINFAST MODEL\" receiving identical cell battery inputs. Dark charcoal grey background,",
    "vid": "steady shot as the battery inputs slide into the parallel boxes, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC123"] = {
    "img": "A flat 2D vector graphic of hands assembling battery packs under a spotlight, with a BMS coding screen in the background. Dark charcoal grey background,",
    "vid": "steady shot, the green BMS code lines scrolling in the background, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC124"] = {
    "img": "A flat 2D vector graphic of a split screen comparing two identical battery cells, with different glowing software patterns overlaying them. Dark charcoal grey background,",
    "vid": "steady shot, the software patterns on the split cells pulsing in sequence, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC125"] = {
    "img": "A flat 2D vector graphic of glowing green network lines wrapping around a battery cell block, showing temperature nodes. Dark charcoal grey background,",
    "vid": "steady shot of the battery block, green light pulses flowing along the network lines, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC126"] = {
    "img": "A flat 2D vector graphic of an engineer's hands typing code on a keyboard, the monitor reflecting glowing green software lines. Dark charcoal grey background,",
    "vid": "steady shot of the monitor, lines of code scrolling down the screen, preserving the details of the reference image, 8-second continuous documentary video"
}

# Chapter 6 (SC127 - SC145)
desc_map["SC127"] = {
    "img": "A flat 2D vector graphic of a giant 96-story building made of glowing cylindrical battery cell bricks. Dark charcoal grey background, warm cream outlines,",
    "vid": "slow camera panning up from the base to the top of the 96-story battery brick building, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC128"] = {
    "img": "A flat 2D vector graphic of a single brick labeled \"CELL\" sitting on a dark surface under a spotlight. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot of the cell brick, the spotlight slowly shifting angle, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC129"] = {
    "img": "A flat 2D vector graphic of an architect's blueprint showing the structural beams of the 96-story cell brick building. Dark charcoal grey background,",
    "vid": "steady shot as the structural outlines of the blueprint glow with a bright green light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC130"] = {
    "img": "A flat 2D vector graphic of a microchip labeled \"BMS\" sending green data wires across the 96-story cell building. Dark charcoal grey background,",
    "vid": "steady shot as green data pulses flow along the wires from the BMS chip across the building, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC131"] = {
    "img": "A flat 2D vector graphic of a grid of battery cells showing different thermal states, some glowing red and others blue. Dark charcoal grey background,",
    "vid": "steady shot as the red cells slowly cool down and turn blue, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC132"] = {
    "img": "A flat 2D vector graphic of a telemetry screen showing real-time graphs monitoring battery cell status. Dark charcoal grey background,",
    "vid": "steady shot, the telemetry graphs slowly scrolling across the screen, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC133"] = {
    "img": "A flat 2D vector graphic of a vehicle dashboard display showing a battery percentage meter going from 100% down to 20%. Dark charcoal grey background,",
    "vid": "steady shot as the percentage digits and bar drop smoothly down on the display, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC134"] = {
    "img": "A flat 2D vector graphic of a schematic diagram of voltage balancing circuits, leveling out power bars across cell nodes. Dark charcoal grey background,",
    "vid": "steady shot, the cell power bars adjusting and balancing out, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC135"] = {
    "img": "A flat 2D vector graphic showing schematic blue liquid flowing through cooling channels between hot battery cell packs. Dark charcoal grey background,",
    "vid": "steady shot, the blue liquid flow animating through the channel network, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC136"] = {
    "img": "A flat 2D vector graphic of three icons representing an hourglass (battery life), a lightning bolt (charging speed), and a shield (safety). Dark charcoal grey background,",
    "vid": "steady shot as the hourglass, lightning, and shield icons light up in sequence in green, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC137"] = {
    "img": "A flat 2D vector graphic of a laptop displaying lines of code next to a VinFast battery module under a spotlight. Dark charcoal grey background,",
    "vid": "steady shot as green code lines scroll down the laptop screen, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC138"] = {
    "img": "A flat 2D vector graphic of a VinFast VF5 car plugged into a V-GREEN charger at a station under a dark night sky. Dark charcoal grey background,",
    "vid": "steady shot of the VinFast VF5 car, green energy pulses flowing from the charger to the car body, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC139"] = {
    "img": "A flat 2D vector graphic showing glowing green data waves running along a charging cable from V-GREEN charger to a battery bay. Dark charcoal grey background,",
    "vid": "steady shot as green data waves pulse along the cable, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC140"] = {
    "img": "A flat 2D vector graphic of a conceptual road paving the way to future battery technologies under a starry sky. Dark charcoal grey background,",
    "vid": "slow camera panning right along the conceptual technology road, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC141"] = {
    "img": "A flat 2D vector graphic of a battery pack stamped with the logo \"StoreDot XFC\" under a green spotlight. Dark charcoal grey background,",
    "vid": "steady shot, a digital timer on the battery pack counting down from 10:00 to 0:00, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC142"] = {
    "img": "A flat 2D vector graphic of a digital display showing 10% to 80% charging progress in 10 minutes. Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot as the percentage bar rises rapidly to 80%, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC143"] = {
    "img": "A flat 2D vector graphic showing a solid-state battery cell blueprint branded with the logo \"ProLogium\". Dark charcoal grey background, warm cream outlines,",
    "vid": "steady shot, the internal solid layers of the blueprint lighting up with a soft silver glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC144"] = {
    "img": "A flat 2D vector graphic of a cargo shelf holding boxes of raw silicon wafers, copper wire spools, and rare earth bags. Dark charcoal grey background,",
    "vid": "steady shot, a slow light beam panning across the cargo shelf, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC145"] = {
    "img": "A flat 2D vector graphic of a screen displaying software code with the glowing green letter V. Dark charcoal grey background,",
    "vid": "steady shot, lines of code scrolling down the screen, casting a green reflection, preserving the details of the reference image, 8-second continuous documentary video"
}

# Chapter 7 (SC146 - SC182)
desc_map["SC146"] = {
    "img": "A flat 2D vector graphic of a glowing green brain shape hovering inside an electric SUV cabin. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the brain shape pulsing slowly with green light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC147"] = {
    "img": "A flat 2D vector graphic of a hand holding a glowing green module labeled with the English text \"CORE CONTROL\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the hand holding the module, which rises slowly in a light cone, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC148"] = {
    "img": "A flat 2D vector graphic of a VinFast VF8 driving on a digital road with front radar and camera sensors scanning the lane. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the VF8, the sensor beams glowing softly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC149"] = {
    "img": "A flat 2D vector graphic of a VinFast VF8 chassis with 7 highlighted camera paths scanning the road, with the English logo of \"AUTOBRAINS\" glowing in green. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the chassis, a slow scanning beam of green light moving from front to back, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC150"] = {
    "img": "A flat 2D vector graphic of a digital roadmap, with a large red X over a LiDAR scanner icon. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the roadmap, the LiDAR icon slowly dissolving, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC151"] = {
    "img": "A flat 2D vector graphic showing the side profiles of a VinFast VF8 and a VF9 driving parallel on a road. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as both SUVs move smoothly forward in parallel, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC152"] = {
    "img": "A flat 2D vector graphic of a barrier splitting a road, one side labeled \"L2++ VISION\" and the other \"L4 AUTONOMOUS\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the road barrier to the L4 side, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC153"] = {
    "img": "A flat 2D vector graphic of the logo \"COMPUTEX 2026\" displayed on a large dark stage screen. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the screen, the text \"COMPUTEX 2026\" glowing with a soft blue light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC154"] = {
    "img": "A flat 2D vector graphic of three logos merging: \"VINFAST\", \"NVIDIA\", and \"AUTOBRAINS\" in a cyan light beam. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the three logos rotate slowly together in the light beam, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC155"] = {
    "img": "A flat 2D vector graphic of a vehicle frame fitted with a central processing unit labeled \"NVIDIA DRIVE HYPERION 10\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, green circuit pulses moving outward from the Hyperion chip across the frame, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC156"] = {
    "img": "A flat 2D vector graphic of a brain outline containing gears and circuit nodes, labeled with the English text \"AGENTIC AI\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the brain outline, the circuit nodes blinking rhythmically, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC157"] = {
    "img": "A flat 2D vector graphic of a glowing green microphone icon in the center of a Vietnam map, labeled \"ViVi\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, soundwave ripples expanding from the microphone icon across the map, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC158"] = {
    "img": "A flat 2D vector graphic of a center console display in a car showing a voice waveform, with text bubbles \"HUE\", \"NGHE AN\", \"CAN THO\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the waveform ripples undulating across the console display, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC159"] = {
    "img": "A flat 2D vector graphic of a large building with the sign \"R&D SYSTEM\" under a glowing green spotlight. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the building, a light beam slowly sweeping across the facade, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC160"] = {
    "img": "A flat 2D vector graphic of a Toyota and a Hyundai car parked next to a dark, unlit research lab building. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning left from the cars to the dark building, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC161"] = {
    "img": "A flat 2D vector graphic of a car dashboard screen showing the virtual assistant avatar ViVi with the tag \"ViGPT 3.0\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, mock dialogue text lines fading in on the dashboard screen, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC162"] = {
    "img": "A flat 2D vector graphic of a passenger in loose clothes talking to the illuminated center dashboard screen. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the screen glowing brighter as the passenger speaks, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC163"] = {
    "img": "A flat 2D vector graphic of the building branded with the logo \"VinAI\", casting a green light. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the VinAI building, the green light pulsing slowly from the windows, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC164"] = {
    "img": "A flat 2D vector graphic of an infotainment screen displaying \"Jellyview 360\" transparent chassis view, showing the road underneath. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the road graphics under the transparent car outline moving slowly backward, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC165"] = {
    "img": "A flat 2D vector graphic of a car mirror adjusting itself automatically, next to a Qualcomm Snapdragon chip icon. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the mirror tilting slowly as a green laser beam sweeps across, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC166"] = {
    "img": "A flat 2D vector graphic of a golden trophy cup with the English text \"CES 2024 INNOVATION AWARD\" engraved on the base. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the trophy cup, a spotlight slowly shifting to highlight the engraving, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC167"] = {
    "img": "A flat 2D vector graphic of a driver monitored by an infrared camera path, showing warning lines over the driver outline. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the warning lines flashing soft orange as the driver outline moves, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC168"] = {
    "img": "A flat 2D vector graphic of an electric car receiving wireless signal beams from a cloud icon labeled \"OTA\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the signal beams pulsing from the cloud down to the car roof, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC169"] = {
    "img": "A flat 2D vector graphic of a balance scale comparing the logo \"VINFAST\" to the logos \"TESLA\" and \"BYD\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the balance scale, the plates slowly tilting, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC170"] = {
    "img": "A flat 2D vector graphic of a computer chip labeled \"TESLA SOFTWARE\" resting on a velvet pillow under a golden crown. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight slowly sweeping across the chip on the pillow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC171"] = {
    "img": "A flat 2D vector graphic of a massive server room with scrolling green code lines, labeled \"FSD DATA\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the server room, data lights on the racks blinking rapidly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC172"] = {
    "img": "A flat 2D vector graphic of a computer chip split from any external connections, glowing in isolation. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the isolated chip, a soft blue energy field surrounding it, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC173"] = {
    "img": "A flat 2D vector graphic of a BYD car grille next to a mechanical gear icon. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the grille, the gear icon slowly rotating in the shadow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC174"] = {
    "img": "A flat 2D vector graphic of a BYD dashboard display showing a outdated map interface, crossed out with a red X. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the display, the red X slowly pulsing with warning light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC175"] = {
    "img": "A flat 2D vector graphic of a BYD car receiving a software disk labeled \"DJI SOFTWARE\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the disk slowly sliding into the car body slot, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC176"] = {
    "img": "A flat 2D vector graphic of a VinFast VF8 under a spotlight, its internal systems glowing with green code. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the VF8, the green code glowing brighter over the chassis, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC177"] = {
    "img": "A flat 2D vector graphic of a VinFast VF8 driving on a highway paved with logos of Qualcomm, NVIDIA, and Bosch. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the car moving smoothly forward along the paved road, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC178"] = {
    "img": "A flat 2D vector graphic of a Qualcomm Snapdragon chip package labeled \"INFOTAINMENT CHIP\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a blue pulse of light tracing the border of the Snapdragon chip, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC179"] = {
    "img": "A flat 2D vector graphic of five semiconductor chips labeled with the English text \"QUALCOMM\", \"NVIDIA\", \"NXP\", \"BOSCH\", and \"RENESAS\". Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the five labeled chips, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC180"] = {
    "img": "A flat 2D vector graphic of a hand holding a green sheet music next to a row of silver musical instruments. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a spotlight highlighting the green score sheet while the instruments remain in shadow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC181"] = {
    "img": "A flat 2D vector graphic of a puzzle board, with the final piece showing the green VinFast V logo sliding into the center slot. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the V logo puzzle piece fits perfectly into the board, glowing green upon locking, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC182"] = {
    "img": "A flat 2D vector graphic comparing two columns: one labeled \"OWNED\" containing software codes, the other \"IMPORTED\" containing raw chips. Dark slate blue background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the columns, the \"OWNED\" column lighting up in green, preserving the details of the reference image, 8-second continuous documentary video"
}

# Chapter 8 (SC183 - SC212)
desc_map["SC183"] = {
    "img": "A flat 2D vector graphic of a car frame chassis, a battery package, and a software screen glowing green. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the car frame, battery, and screen slowly align and stack vertically, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC184"] = {
    "img": "A flat 2D vector graphic of raw lithium ore rocks, a bare copper coil, and a generic chip labeled \"IMPORTED\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the imported minerals and chip, the label \"IMPORTED\" pulsing with a soft warning red light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC185"] = {
    "img": "A flat 2D vector graphic of a generic electric car chassis with highlight tags showing zero factory ownership on battery cells. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the car chassis, the highlights pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC186"] = {
    "img": "A flat 2D vector graphic of a complex global shipping network map showing cargo ships and planes transporting parts. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the network map, white trace lines slowly moving along the shipping lanes, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC187"] = {
    "img": "A flat 2D vector graphic of a BYD Seal car parked next to a high-tech cleanroom facility with the text \"TSMC FOUNDRY\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the BYD car, the TSMC facility in the background glowing with soft blue cleanroom lighting, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC188"] = {
    "img": "A close-up 2D flat vector graphic of a raw silicon wafer under a laser cutter, labeled \"FABRICATION\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the silicon wafer, the laser beam drawing a square pattern slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC189"] = {
    "img": "A flat 2D vector graphic of a world map with shipping routes converging on a single electric car outline. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the routes on the map slowly pulsing with soft white light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC190"] = {
    "img": "A flat 2D vector graphic of a global supply chain web, with lines connecting multiple factory icons to a central vehicle. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the supply chain web, data nodes moving slowly along the connecting lines, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC191"] = {
    "img": "A flat 2D vector graphic of a small child silhouette standing next to a massive gear wheel, holding a green glowing letter V. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the child, the green V logo casting a bright light onto the surface of the giant gear wheel, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC192"] = {
    "img": "A flat 2D vector graphic of a giant runner outline overtaking competitors on a dark running track. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a light beam sweeping from left to right along the track, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC193"] = {
    "img": "A flat 2D vector graphic of a large balance scale, the left side holding the text \"HOW MUCH WE MAKE?\", the right side holding \"WHAT WE CONTROL?\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the balance scale, the right side plate containing \"WHAT WE CONTROL\" dipping lower and glowing green, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC194"] = {
    "img": "A flat 2D vector graphic of a car outline with three highlighted green cores: the chassis, the BMS board, and the screen code. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the three green cores on the car outline pulse in sync, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC195"] = {
    "img": "A close-up 2D flat vector graphic of a computer monitor displaying code, with the green VinFast letter V in the background. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the monitor, lines of code scrolling down the screen, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC196"] = {
    "img": "A flat 2D vector graphic of a single semiconductor chip branded with \"QUALCOMM\" next to a battery pack branded \"CATL\", under a green spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the spotlight sweeps across the Qualcomm chip and CATL battery pack, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC197"] = {
    "img": "A flat 2D vector graphic comparing a Tesla car next to a VinFast car, both charging at a station labeled \"POWERED BY CATL\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right from the Tesla car to the VinFast car, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC198"] = {
    "img": "A flat 2D vector graphic of cargo boxes filled with identical microchips, labeled \"STANDARDIZED SILICON\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the boxes, a slow zoom-in on the chips, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC199"] = {
    "img": "A flat 2D vector graphic showing the text \"WHO CONTROLS THE ENGINE?\" written in bold electric green font, under a spotlight. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the green text, which slowly flashes with a bright electric green glow, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC200"] = {
    "img": "A flat 2D vector graphic showing the question text \"MADE IN VIETNAM?\" written in bold cream font, crossed out with a thin silver line. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the text, a slow panning light beam revealing the texture of the background screen, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC201"] = {
    "img": "A flat 2D vector graphic showing a driver in loose clothes holding a steering wheel, with the green V logo glowing in the center. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the green V logo pulsing with a soft glow as the hands grip the steering wheel, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC202"] = {
    "img": "A flat 2D vector graphic of a computer screen displaying a large green \"SUBSCRIBE\" button next to the YouTube icon. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the screen, the green \"SUBSCRIBE\" button slowly pulses with light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC203"] = {
    "img": "A flat 2D vector graphic showing two silhouettes of viewers watching a screen glowing green. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the green glow on the viewers' silhouettes gently pulsing, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC204"] = {
    "img": "A flat 2D vector graphic of a large question mark silhouette, which slowly dissolves into the green VinFast logo \"V\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the question mark fades away and the green V logo brightens, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC205"] = {
    "img": "A flat 2D vector graphic of a clock with hands spinning backward, showing the text \"OUTDATED PERSPECTIVE\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the clock hands spin backwards, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC206"] = {
    "img": "A flat 2D vector graphic of an automated factory floor with moving conveyors and robot arms. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "slow camera panning right across the control deck, showing the factory floor active below, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC207"] = {
    "img": "A flat 2D vector graphic of a control deck overlooking an automated factory floor. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the control deck, green screens displaying factory telemetry, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC208"] = {
    "img": "A flat 2D vector graphic of the green VinFast logo V stamped onto a metal plate, representing a seal of authority. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the metal plate, the green V logo glowing with a bright light from the edges, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC209"] = {
    "img": "A flat 2D vector graphic of a large seal of authority bearing the letter \"V\" stamped onto a global supply chain map. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot as the seal glows with a bright green light, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC210"] = {
    "img": "A flat 2D vector graphic of a generic electric car chassis floating above a network of global suppliers' icons. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot of the floating chassis, the supplier network icons below blinking slowly, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC211"] = {
    "img": "A flat 2D vector graphic of an electric car silhouette facing a split path, one path labeled \"RISK\" in red, the other \"REWARD\" in green. Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, a light beam sweeping from the car silhouette towards the split path ahead, preserving the details of the reference image, 8-second continuous documentary video"
}
desc_map["SC212"] = {
    "img": "A flat 2D vector graphic of a viewer sitting in front of a screen displaying a comment box with the text \"YOUR OPINION?\". Dark charcoal grey background, warm cream outlines, dramatic chiaroscuro lighting, deep noir shadows",
    "vid": "steady shot, the comment box pulsing with a soft white glow, preserving the details of the reference image, 8-second continuous documentary video"
}

# Save logic
part1 = []
part2 = []
part3 = []
part4 = []

for item in scene_map:
    sc_id = item['id']
    ch = int(item['chapter'])
    
    desc = desc_map.get(sc_id, {"img": "", "vid": ""})
    if not desc["img"]:
        print(f"ERROR: Missing description for {sc_id}")
        continue
        
    ch_id = f"CH{ch:02d}_{sc_id}"
    img_line = f"{ch_id} [IMAGE]: {desc['img']}\n"
    vid_line = f"{ch_id} [VIDEO]: @{ch_id}.png -> {desc['vid']} --ar 16:9\n"
    
    block = f"{img_line}{vid_line}\n"
    
    if ch in [1, 2]:
        part1.append(block)
    elif ch in [3, 4]:
        part2.append(block)
    elif ch in [5, 6]:
        part3.append(block)
    elif ch in [7, 8]:
        part4.append(block)

# Write files
with open('prompts_part1.txt', 'w', encoding='utf-8') as f:
    f.writelines(part1)
with open('prompts_part2.txt', 'w', encoding='utf-8') as f:
    f.writelines(part2)
with open('prompts_part3.txt', 'w', encoding='utf-8') as f:
    f.writelines(part3)
with open('prompts_part4.txt', 'w', encoding='utf-8') as f:
    f.writelines(part4)

print("Split prompts written successfully into 4 parts!")

