import json

with open("scene_timing_map.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

angles = [
    "A WIDE STILL SHOT of",
    "An EXTREME CLOSE-UP of",
    "A LOW ANGLE SHOT of",
    "A SYMMETRICAL COMPOSITION of"
]

suffix = "modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic --ar 16:9"

# Pre-defined creative concepts mapping to the 8 chapters roughly
concepts = [
    # Ch 1 (Hook)
    "a massive glowing neon sign shaped like a mythical dragon intertwined with a high-speed train in a bustling Vietnamese night metropolis. Deep cinematic lighting.",
    "a determined Vietnamese businessman shaking hands with a giant mechanical robotic arm holding a car chassis. Stark shadows.",
    "two towering skyscrapers, one marked with Samsung's blue hue and the other with a red Vietnamese star, standing side by side. Gloomy storm clouds above.",
    "a heavy chessboard with metallic pieces shaped like factories and electric vehicles, a Vietnamese man pondering a move. High contrast lighting.",
    
    # Ch 2 (People/Stakes)
    "a tired but resilient Vietnamese factory owner in his 30s looking at a massive glowing red contract on a desk. Dim warm warehouse lighting.",
    "a glowing electric vehicle assembly line stretching into the distance with hundreds of silent workers in uniform. Cool blue neon lighting.",
    "a modern glowing cityscape reflecting on the eyeglasses of a worried Vietnamese citizen holding a bunch of debt papers. Neon reflections.",
    "a giant hourglass where dropping sand turns into golden coins raining onto a small fragile wooden house. Golden hour dramatic shadows.",

    # Ch 3 (History)
    "a retro 1960s Asian general in uniform pointing a glowing baton at a tiny computer chip that radiates power. Vintage cinematic sepia tones.",
    "a stern Asian statesman from Singapore standing atop a mountain of gold bars with a glowing shield. Crisp, clean lighting.",
    "a massive red dragon made of steel pipelines wrapping around a modern bullet train. High contrast neon backlighting.",
    "a group of four colossal stone statues representing the Asian economic tigers towering over a vast ocean. Mystic foggy lighting.",

    # Ch 4 (Vingroup)
    "a gigantic glowing octopus with tentacles grasping an electric car, a bullet train, a wind turbine, and a modern hospital. Surreal neon lighting.",
    "a massive glowing red negative balance sheet burning on a huge wooden boardroom table. Intense fiery orange lighting.",
    "a Vietnamese executive in a dark suit standing calmly inside a hurricane of soaring golden stock arrows. High contrast dramatic shadows.",
    "a massive cargo ship carrying hundreds of electric cars sailing under a gigantic glowing Nasdaq sign. Cool ocean blue lighting.",

    # Ch 5 (Timeline)
    "a giant marble calendar with pages flying away, revealing glowing red governmental seals underneath. Dynamic action frozen in time.",
    "a glowing high-speed bullet train crossing a massive bridge made entirely of stacks of paper contracts. Sunset golden lighting.",
    "a massive wind turbine spinning over a sprawling Vietnamese coastal city, casting dramatic long shadows. Stark sunlight.",
    "two hands gripping a glowing neon contract over a dark table with a map of India. Cyberpunk neon pink and blue lighting.",

    # Ch 6 (Daewoo risks)
    "a colossal crumbling retro television screen showing a 1990s Asian businessman fleeing in the rain. Gritty noir lighting.",
    "a giant house of cards built from glowing stock certificates collapsing in slow motion. High contrast dynamic lighting.",
    "a massive tangled web of glowing red strings connecting dozens of opaque corporate buildings. Dark, mysterious shadows.",
    "a deep green mangrove forest being slowly engulfed by a massive, imposing concrete wall. Moody, ominous lighting.",
    "a divided crowd of Vietnamese citizens, half cheering with glowing lights, half standing in deep shadow looking worried. Contrast split lighting.",

    # Ch 7 (Discipline)
    "a giant glowing padlock sealing a massive vault of gold, with a stern inspector standing guard. Stark spotlight from above.",
    "a massive scales of justice made of glowing blue energy balancing a car factory and a group of citizens. Ethereal lighting.",
    "a pair of giant mechanical eyes looming over a tiny glowing city. High contrast dark shadows.",
    "a sturdy concrete dam holding back a turbulent ocean of gold coins, starting to show tiny cracks. Dramatic stormy lighting.",

    # Ch 8 (Conclusion)
    "a Vietnamese man standing at a misty crossroads, one path paved with glowing gold, the other littered with broken gears. Misty teal lighting.",
    "a giant glowing golden dragon clutching a heavy iron chain, struggling to fly upwards. Epic heroic lighting.",
    "a colossal hourglass running out of time, with an electric vehicle trapped inside the bottom glass. High contrast moody shadows.",
    "a solitary silhouette of a Vietnamese businessman looking out over an endless ocean of glowing neon metropolis. Calm, dawn lighting."
]

out = []
for i, scene in enumerate(scenes):
    angle = angles[i % 4]
    
    # Pick concept safely
    if i < len(concepts):
        concept = concepts[i]
    else:
        concept = concepts[-1] # fallback
        
    prompt = f"{i+1}. {angle} {concept} {suffix}"
    out.append(prompt)

with open("image_prompts.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(out))

print(f"Generated {len(scenes)} prompts in image_prompts.txt")
