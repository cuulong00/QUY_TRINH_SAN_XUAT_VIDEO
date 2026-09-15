import json

custom_scenes = {
  "SC001": "A towering mountain of crumpled to-do lists and planners, a tiny figure standing at the bottom looking up, 2D sketch illustration, vivid red and blue colors, psychological tension",
  "SC002": "A bright red pen violently scratching out complex diagrams on a thick notebook, 2D sketch illustration, expressive chaotic lines, vibrant colors, harsh lighting",
  "SC003": "Silhouette of a person pressing their hand against a rainy neon-lit window, gazing at a vibrant city skyline, 2D sketch illustration, atmospheric longing",
  "SC004": "A single drop of dark coffee rippling in a cup, reflecting a bloodshot eye twitching from exhaustion, 2D sketch illustration, macro shot, vivid colors",
  "SC005": "An unlit modern gas stove with a small, cold spark, juxtaposed against a primal fire burning inside a cave, 2D sketch illustration, vibrant contrast",
  "SC006": "A heavy iron anchor dragging a person down into a comfortable but claustrophobic armchair, 2D sketch illustration, vivid surrealism, psychological weight",
  "SC007": "A ticking analog clock melting over a heavy calendar, heavy charcoal shading, vibrant neon red hands, 2D sketch illustration",
  "SC008": "Two hands holding the same unfinished email draft, one hand relaxed, the other pale and gripping the mouse tightly, 2D sketch illustration, vivid glowing screen",
  "SC009": "A glowing crimson almond shape hidden deep inside a mess of chaotic electrical wires, 2D sketch illustration, mechanical vs biological, vibrant colors",
  "SC010": "A massive, terrifying shadow of a lion cast by a small, glowing red deadline on a calendar, 2D sketch illustration, chiaroscuro, vivid colors",
  "SC011": "A syringe injecting vibrant liquid dopamine into a mechanical gear, 2D sketch illustration, close up, psychological concept",
  "SC012": "A massive neon red emergency siren spinning in a small, empty, dark room, 2D sketch illustration, loud visual noise, vivid lighting",
  "SC013": "A padlock snapping shut on an old wooden chest in the background, out of focus, 2D sketch illustration, atmospheric shading",
  "SC014": "A beautiful, immaculate glass shield protecting a very fragile, glowing ember, 2D sketch illustration, vibrant contrast of glass and fire",
  "SC015": "Carl Jung sitting in a shadowy study, surrounded by floating, colorful glowing archetypal symbols, 2D sketch illustration, vivid historical portrait",
  "SC016": "A golden pendulum swinging between a bright neon 'Consciousness' sign and a dark abyssal pit, 2D sketch illustration, dynamic shading",
  "SC017": "An intense fMRI scan of a brain where the fear center is exploding in vibrant, chaotic red and orange sketch lines, 2D sketch illustration",
  "SC018": "A snake made of glowing green neon tubing coiled around a laptop, 2D sketch illustration, modern psychological thriller",
  "SC019": "A person stuck inside a glass hourglass, desperately clawing at the walls as colorful sand buries them, 2D sketch illustration",
  "SC020": "A young child standing at a crossroads, one path glowing with bright warm light, the other dark and intimidating, 2D sketch illustration",
  "SC021": "Two report cards, one marked with a glowing golden 'A+' and the other with a heavy red 'Try Harder', 2D sketch illustration, societal pressure",
  "SC022": "A giant percentage pie chart slicing a person into fragments, vivid abstract coloring, 2D sketch illustration, psychological statistics",
  "SC023": "A scale weighing a glowing lightbulb of 'Intelligence' against a heavy iron anvil of 'Failure', 2D sketch illustration",
  "SC024": "A fragile porcelain plate with beautiful painted patterns, cracking under a tiny drop of water, 2D sketch illustration, vulnerability",
  "SC025": "A massive, heavy turtle shell strapped to a person's back, glowing with defensive neon patterns, 2D sketch illustration",
  "SC026": "A narcissistic mirror reflecting a giant armored knight, while a small vulnerable figure stands before it, 2D sketch illustration, vibrant colors",
  "SC027": "A small seed trying to sprout through thick, neon-lit concrete, 2D sketch illustration, environmental storytelling",
  "SC028": "A circuit breaker tripping violently in a colorful burst of sparks, 2D sketch illustration, mechanical failure metaphor",
  "SC029": "A person sinking slowly into a plush, brightly colored sofa that has eyes watching them, 2D sketch illustration, comfort zone trap",
  "SC030": "A beautifully framed empty canvas, untouched, illuminated by a warm but intimidating gallery spotlight, 2D sketch illustration",
  "SC031": "A colorful glowing syringe marked 'Dopamine' hovering just out of reach, 2D sketch illustration",
  "SC032": "A person running on a treadmill that powers a massive, glowing projector displaying a hero fighting a dragon, 2D sketch illustration, fantasy substitution",
  "SC033": "A brain split in two halves, one half colorful and dreaming, the other gray and chained to a desk, 2D sketch illustration",
  "SC034": "A majestic crown hovering over a person's head, but drawn entirely with chaotic, anxious scribbles, 2D sketch illustration",
  "SC035": "A coffee cup on a cafe table, the coffee ripples reflecting a grandiose fantasy of a neon-lit stage, 2D sketch illustration",
  "SC036": "A massive pile of shiny gold coins that are actually just plastic tokens, glowing under a cheap light, 2D sketch illustration",
  "SC037": "A dark path through a forest, lined with glowing, dangerous neon thorn bushes, 2D sketch illustration, environmental storytelling",
  "SC038": "A heavy iron shield marked 'Perfection' blocking an entire doorway, glowing intensely, 2D sketch illustration",
  "SC039": "A dusty research file from Brown University opening up, glowing colorful statistics spilling out, 2D sketch illustration",
  "SC040": "A tightrope walker frozen midway, overwhelmed by chaotic, bright neon arrows pointing in all directions, 2D sketch illustration",
  "SC041": "A perfect, unblemished apple sitting inside a bulletproof glass case, vibrant red, 2D sketch illustration",
  "SC042": "A pendulum violently swinging between a glowing golden crown and a dark, heavy iron shackle, 2D sketch illustration, Kernberg cycle",
  "SC043": "A person watching a beautiful television broadcast of themselves, sitting in a dark, empty room, 2D sketch illustration",
  "SC044": "A sudden burst of a bright neon balloon, leaving only dark tangled strings, 2D sketch illustration, psychological burst",
  "SC045": "A heavy wave of dark, chaotic charcoal lines crashing over a small, colorful boat, 2D sketch illustration, shame cycle",
  "SC046": "A door with thousands of tiny, colorful locks, completely barricaded, 2D sketch illustration, narcissistic defense",
  "SC047": "A cycle of gears, some glowing brightly, others rusted and jamming, 2D sketch illustration",
  "SC048": "A child looking into a tall mirror that distorts their reflection into a massive superhero, vibrant colors, 2D sketch illustration",
  "SC049": "A mother figure holding a distorted funhouse mirror towards a child, glowing eerie colors, 2D sketch illustration, mirroring concept",
  "SC050": "A tiny pedestal balancing a massive, impossibly heavy golden trophy, swaying dangerously, 2D sketch illustration",
  "SC051": "A dark room where a small glowing ember is completely ignored, 2D sketch illustration, emotional neglect",
  "SC052": "A mask with an exaggerated bright smile cracking down the middle, revealing nothing but shadow behind it, 2D sketch illustration",
  "SC053": "A bottle of expired, brightly colored pills sitting on a dark dusty shelf, 2D sketch illustration, failed coping mechanisms"
}

import json
with open('b_scenes.json') as f:
    scenes = json.load(f)

for s in scenes:
    sc = s['id']
    if sc in custom_scenes:
        s['visual_summary'] = custom_scenes[sc]
    else:
        s['visual_summary'] = ""

with open('b_scenes_temp.json', 'w') as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)
print("Saved 53 customized Prompts")
