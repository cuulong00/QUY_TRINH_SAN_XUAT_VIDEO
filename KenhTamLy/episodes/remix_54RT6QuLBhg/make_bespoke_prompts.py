import json
import os

os.chdir('/Users/pro16/Documents/VideoProject/KenhTamLy/episodes/remix_54RT6QuLBhg')

# THE MASTER DICTIONARY OF BESPOKE PROMPTS BY EXPERT "THE VISUAL ARCHITECT"
expert_prompts = [
    # CH 1 (SC1-13)
    "A towering mountain of crumpled to-do lists and planners, a tiny figure standing at the bottom looking up, 2D sketch illustration, vivid red and blue colors, psychological tension", # 8% stats
    "A bright red pen violently scratching out complex diagrams on a thick notebook, 2D sketch illustration, expressive chaotic lines, vibrant colors, harsh lighting", 
    "Silhouette of a person pressing their hand against a rainy neon-lit window, gazing at a vibrant city skyline, 2D sketch illustration, atmospheric longing",
    "A single drop of dark coffee rippling in a cup, reflecting a bloodshot eye twitching from exhaustion, 2D sketch illustration, macro shot, vivid colors",
    "An unlit modern gas stove with a small cold spark, juxtaposed against a primal fire burning inside a cave, 2D sketch illustration, vibrant contrast",
    "A heavy iron anchor dragging a person down into a comfortable but claustrophobic armchair, 2D sketch illustration, vivid surrealism, psychological weight",
    "A ticking analog clock melting over a heavy calendar, heavy charcoal shading, vibrant neon red hands, 2D sketch illustration", # amygdala
    "Two hands holding the same unfinished email draft, one hand relaxed, the other pale and gripping the mouse tightly, 2D sketch illustration, vivid glowing screen",
    "A glowing crimson almond shape hidden deep inside a mess of chaotic electrical wires, 2D sketch illustration, mechanical vs biological, vibrant colors",
    "A massive, terrifying shadow of a lion cast by a small glowing red deadline on a calendar, 2D sketch illustration, chiaroscuro, vivid colors",
    "A syringe injecting vibrant liquid adrenaline into a mechanical gear, 2D sketch illustration, close up, psychological concept",
    "A massive neon emergency siren spinning in a small empty dark room, 2D sketch illustration, loud visual noise, vivid lighting",
    "A padlock snapping shut on an old wooden chest in the background, out of focus, 2D sketch illustration, atmospheric shading",

    # CH 2 (SC14-27)
    "An intense fMRI scan of a brain where the fear center is exploding in vibrant, chaotic red and orange sketch lines, 2D sketch illustration", # fMRI
    "A snake made of glowing green neon tubing coiled around a laptop, 2D sketch illustration, modern psychological thriller",
    "A person stuck inside a glass hourglass, desperately clawing at the walls as colorful sand buries them, 2D sketch illustration",
    "A young child standing at a crossroads, one path glowing with bright warm light, the other dark and intimidating, 2D sketch illustration",
    "Two report cards, one marked with a glowing golden 'A+' and the other with a heavy red 'Try Harder', 2D sketch illustration, societal pressure", # Carol Dweck
    "A giant percentage pie chart slicing a person into fragments, vivid abstract coloring, 2D sketch illustration, psychological statistics",
    "A scale weighing a glowing lightbulb of 'Intelligence' against a heavy iron anvil of 'Failure', 2D sketch illustration",
    "A fragile porcelain plate with beautiful painted patterns, cracking under a tiny drop of water, 2D sketch illustration, vulnerability",
    "A massive, heavy turtle shell strapped to a person's back, glowing with defensive neon patterns, 2D sketch illustration", # Narcissistic Defense
    "A mirror reflecting a giant armored knight, while a small vulnerable figure stands before it, 2D sketch illustration, vibrant colors",
    "A sturdy brick wall hastily built with brightly colored children's blocks, full of gaps, 2D sketch illustration",
    "A small seed trying to sprout through thick, neon-lit concrete, 2D sketch illustration, environmental storytelling",
    "A circuit breaker tripping violently in a colorful burst of sparks, 2D sketch illustration, mechanical failure metaphor",
    "A person sinking slowly into a plush, brightly colored sofa that has eyes watching them, 2D sketch illustration, comfort zone trap",

    # CH 3 (SC28-40)
    "A beautifully framed empty canvas, untouched, illuminated by a warm but intimidating gallery spotlight, 2D sketch illustration",
    "A colorful glowing syringe marked 'Dopamine' hovering just out of reach, 2D sketch illustration",
    "A person running on a treadmill that powers a massive, glowing projector displaying a hero fighting a dragon, 2D sketch illustration, fantasy substitution",
    "A brain split in two halves, one half colorful and dreaming, the other gray and chained to a desk, 2D sketch illustration",
    "A majestic crown hovering over a person's head, but drawn entirely with chaotic, anxious scribbles, 2D sketch illustration", # Grandiose fantasy
    "A coffee cup on a cafe table, the coffee ripples reflecting a grandiose fantasy of a neon-lit stage, 2D sketch illustration",
    "A massive pile of shiny gold coins that are actually just plastic tokens, glowing under a cheap light, 2D sketch illustration",
    "A dark path through a forest, lined with glowing, dangerous neon thorn bushes, 2D sketch illustration, environmental storytelling",
    "A heavy iron shield marked 'Perfection' blocking an entire doorway, glowing intensely, 2D sketch illustration", # Perfectionism
    "A dusty research file from Brown University opening up, glowing colorful statistics spilling out, 2D sketch illustration",
    "A tightrope walker frozen midway, overwhelmed by chaotic, bright neon arrows pointing in all directions, 2D sketch illustration",
    "A perfect, unblemished apple sitting inside a bulletproof glass case, vibrant red, 2D sketch illustration",
    "A magnifying glass focusing intensely on a tiny, vividly colored scratch on an otherwise perfect surface, 2D sketch illustration",

    # CH 4 (SC41-61)
    "A pendulum violently swinging between a glowing golden crown and a dark, heavy iron shackle, 2D sketch illustration, Kernberg cycle",
    "A person watching a beautiful television broadcast of themselves, sitting in a dark empty room, 2D sketch illustration",
    "A sudden burst of a bright neon balloon, leaving only dark tangled strings, 2D sketch illustration, psychological burst",
    "A heavy wave of dark, chaotic charcoal lines crashing over a small, colorful boat, 2D sketch illustration, shame cycle",
    "A door with thousands of tiny, colorful locks, completely barricaded, 2D sketch illustration, narcissistic defense",
    "A cycle of gears, some glowing brightly, others rusted and jamming, 2D sketch illustration",
    "A child looking into a tall mirror that distorts their reflection into a massive superhero, vibrant colors, 2D sketch illustration", # Mirroring
    "A mother figure holding a distorted funhouse mirror towards a child, glowing eerie colors, 2D sketch illustration, mirroring concept",
    "A tiny pedestal balancing a massive, impossibly heavy golden trophy, swaying dangerously, 2D sketch illustration",
    "A dark room where a small glowing ember is completely ignored, 2D sketch illustration, emotional neglect",
    "A mask with an exaggerated bright smile cracking down the middle, revealing nothing but shadow behind it, 2D sketch illustration",
    "A cracked theater stage illuminated by a single harsh spotlight, surrounded by colorful but broken props, 2D sketch illustration",
    "A heavy stone slab slowly pushing a colorful butterfly into the dirt, 2D sketch illustration",
    "A winding staircase leading nowhere, the steps glowing with neon frustration, 2D sketch illustration",
    "A bright red 'Warning' sign sinking in quicksand, 2D sketch illustration",
    "A puppet with tangled strings cutting itself loose but falling into a vibrant abyss, 2D sketch illustration",
    "A person wearing an oversized, brightly colored coat of armor that drags them down, 2D sketch illustration",
    "A locked diary glowing with internal, colorful light, vibrating with trapped energy, 2D sketch illustration",
    "An overgrown garden choking a beautiful, brightly colored flower, 2D sketch illustration",
    "A single bright star struggling to shine through a thick, heavy smog, 2D sketch illustration",
    "A broken compass spinning wildly on top of a colorful map, 2D sketch illustration",

    # CH 5 (SC62-79)
    "A bottle of expired, brightly colored pills sitting on a dark dusty shelf, 2D sketch illustration, failed coping mechanisms",
    "A heavy metal cage wrapped tightly in brightly colored silk ribbons, 2D sketch illustration, discipline trap",
    "A glowing red thermometer bursting under pressure, colored mercury spilling out, 2D sketch illustration",
    "A person forcing themselves to sprint on a treadmill that's rapidly catching fire, vibrant flames, 2D sketch illustration",
    "Cortisol represented as a dark, toxic purple slime suffocating a glowing brain, 2D sketch illustration", 
    "A bright neon 'Stop' sign ignored as a car speeds towards a cliff, 2D sketch illustration",
    "A person floating elegantly away in a hot air balloon, leaving chaotic red fire below, 2D sketch illustration, Spiritual Bypassing",
    "A zen garden covered in dead, dark leaves, violently raked into perfect circles, 2D sketch illustration",
    "An incense stick burning next to a mountain of unpaid, vividly colored bills, 2D sketch illustration",
    "A halo made of bright neon tubes short-circuiting and sparking dangerously, 2D sketch illustration",
    "A person meditating calmly inside an exploding building, vibrant colors, 2D sketch illustration",
    "A bridge made of glowing colorful light that suddenly cuts off over a dark chasm, 2D sketch illustration",
    "A map leading to a glowing treasure chest that is actually a painted wall, 2D sketch illustration",
    "A shield of beautiful stained glass shattering spectacularly under a small stone, 2D sketch illustration",
    "A book titled 'Healing' sinking into dark water, 2D sketch illustration",
    "A vibrant lotus flower blooming out of a toxic, glowing green waste pipe, 2D sketch illustration",
    "A person looking at a compass pointing deeply inwards, glowing with warm light, 2D sketch illustration",
    "A massive, ancient door slowly being pushed open by a tiny streak of colorful light, 2D sketch illustration",

    # CH 6 (SC80-94)
    "A bright white polar bear fading in and out of existence in a chaotic dark room, 2D sketch illustration, psychological experiment", # White Bear
    "A person violently trying to hold a door shut against a glowing, colorful monster, 2D sketch illustration", 
    "A label maker printing a bright neon sticker reading 'FEAR', attached to a scary shadow to make it small, 2D sketch illustration",
    "A chaotic red storm cloud being neatly put into a glowing glass jar, 2D sketch illustration",
    "A messy, colorful desk where a single sticky note glows warmly with purpose, 2D sketch illustration",
    "A person carefully stepping onto a bridge of light over a chasm, 2D sketch illustration",
    "A computer 'Send' button glowing red hot, a trembling finger hovering over it, 2D sketch illustration, exposure therapy",
    "An unfinished email floating in space, glowing softly, completely harmless, 2D sketch illustration",
    "A person dropping a heavy shield and standing naked but bathed in warm, beautiful light, 2D sketch illustration",
    "A cracked, imperfect ceramic mug holding beautiful, warm glowing coffee, 2D sketch illustration, wabi-sabi",
    "A small seedling breaking through a hard, brightly colored shell, 2D sketch illustration",
    "A shadowy figure stepping out into bright, vivid sunlight, squinting, 2D sketch illustration",
    "A colorful bird taking its first clumsy flight from a dark nest, 2D sketch illustration",
    "A pair of hands dirty with clay, molding something beautiful and imperfect, 2D sketch illustration",
    "A marathon runner stumbling but catching themselves with a bright splash of color, 2D sketch illustration",

    # CH 7 (SC95-108)
    "A massive, final explosion of a dying star in vibrant colors right before turning into a steady sun, 2D sketch illustration, extinction burst",
    "A heavy rusted chain breaking spectacularly under tension, bright sparks flying, 2D sketch illustration",
    "A person standing firm against incredibly strong, colorful wind, pushing forward, 2D sketch illustration",
    "A beautiful dawn breaking over a city built of crumpled paper, 2D sketch illustration",
    "A percentage graphic where the 8% glows intensely with warm, inviting light, 2D sketch illustration",
    "A mirror reflecting not a giant knight, but the person themselves, bathed in soft colorful light, 2D sketch illustration",
    "A lock finally clicking open, releasing a flood of vibrant colors, 2D sketch illustration",
    "A deep cave where a torch is newly lit, throwing colorful shadows, 2D sketch illustration",
    "A map of the mind, with new, brightly colored pathways beginning to form over dark chasms, 2D sketch illustration",
    "Carl Jung's quote carved into glowing neon stone, 2D sketch illustration",
    "A heavy fog clearing to reveal a bright, clear, vivid path ahead, 2D sketch illustration",
    "A small spark igniting a massive, vibrant forest of new growth, 2D sketch illustration",
    "A wall crumbling down, letting in blindingly beautiful colors, 2D sketch illustration",
    "A journaling pen resting peacefully on a finished page bathed in warm, sunset colors, 2D sketch illustration"
]

with open('b_scenes.json', 'r') as f:
    scenes = json.load(f)

scene_timing_map = []
visual_prompts = []
fallback_prompt = "A psychological, evocative 2D sketch illustration with vibrant colors and heavy emotional shading"

for i, s in enumerate(scenes):
    prompt_base = expert_prompts[i] if i < len(expert_prompts) else fallback_prompt
    
    # generate a derived summary based on the prompt
    summary_parts = prompt_base.split(', 2D')
    summary = summary_parts[0].strip().capitalize()
    
    count = s.get('sentence_count', 1)
    dur = count * 5
    
    sc_id = f"SC{i+1:03d}"
    
    scene_timing_map.append({
        "id": sc_id,
        "sentence_count": count,
        "duration_sec": dur,
        "visual_summary": summary + " - 2D sketch illustration, vivid thematic depth."
    })
    
    visual_prompts.append(f"[{sc_id}] {prompt_base} --ar 16:9 --v 6.0 --stylize 50")

with open('scene_timing_map.json', 'w') as f:
    json.dump(scene_timing_map, f, ensure_ascii=False, indent=4)

with open('visual_prompts.txt', 'w') as f:
    f.write('\n'.join(visual_prompts))

print(f"Generated {len(scene_timing_map)} BESPOKE scenes written by the expert.")
