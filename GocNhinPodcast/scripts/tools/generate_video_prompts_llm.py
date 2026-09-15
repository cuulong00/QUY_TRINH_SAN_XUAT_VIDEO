#!/usr/bin/env python3
import os
import json
import time
import httpx

API_KEY = "AQ.Ab8RN6IEVMCQ9JKi9S12-Ev-Q79kYcjRiCrhEGz-qxZ9dEGG9A"
MODEL_NAME = "gemini-2.5-flash"

BASE_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast"
EPISODE_SLUG = "musk-tien-te-tuong-lai"

def generate_visual_prompt_via_llm(api_key: str, scene_id: str, sentences: str, base_prompt: str, prev_prompt: str = "") -> str:
    system_instruction = """
    You are the S-Grade Visual Director for GocNhinPodcast, a prestigious social and macro-economic analysis channel.
    Your mission is to translate a Vietnamese voiceover sentence and its core visual idea into a single, high-quality English video prompt (for models like Runway Gen-3, Luma, or Veo 3.1).
    
    You must choose between exactly two brand styles depending on the scene content to ensure visual consistency and minimize video generation errors:
    
    Style 1: Flat 2D Vector Art Style (For abstract/machinery scenes)
    - Use for: databases, server racks, CPU microchips, bar charts, line graphs, network flowcharts, checks, money dissolving, world maps, digital interfaces, abstract geometry.
    - Suffix must be: "flat 2D vector illustration style, clean bold outlines, flat colors, vibrant color palette, cinematic lighting, 8-second continuous documentary video --ar 16:9"
    
    Style 2: Minimalist Graphic Novel Ink Style (For human/realistic scenes)
    - Use for: human silhouettes, groups of people, realistic office workers, historical figures, crowds, street views, factories, landscapes (dams, solar panels, stormy seas).
    - Suffix must be: "minimalist graphic novel ink style, high contrast, bold outlines, flat colors, vibrant color palette, cinematic lighting, 8-second continuous documentary video --ar 16:9"
    
    Rules for prompt construction:
    1. The prompt must be entirely in English.
    2. Do NOT use motion words like "zoom", "pan", "panning", "track", "zoom-in". The camera movement is handled separately. Start the prompt with the camera behavior directly, e.g., "A steady shot showing...", "A slow camera panning showing...", "A subtle slow zoom-in showing...".
    3. Typography & Text: All text displayed on the screen must be in ENGLISH only (e.g. "ENERGY", "DEBT", "AI ERA"). Never output Vietnamese diacritics on screen. Specify text position, e.g., "with the English text 'ENERGY' displayed in a clean bold minimal sans-serif font centered in the upper third."
    4. Vietnamese names/locations: Must be completely accentless (e.g., "Ha Noi", "Ho Chi Minh", "Nguyen", "VinFast").
    5. Avoid 3D, photorealistic, hyperrealistic, or render-related terms in the body of the prompt.
    6. Continuity: If the scene ID has a letter suffix (like SC097a, SC097b), it belongs to a sequence. You must maintain identical descriptions of characters, clothing, and background environment, and only change the action or camera angle.
    7. No Real-World Names: Do not use names like "Elon Musk". Use terms like "a charismatic tech billionaire silhouette" or "a visionary billionaire businessman".
    
    Output Format:
    Return ONLY the final, complete video prompt on a single line. Do not include any explanations, Markdown formatting, quotes, or JSON.
    """

    user_prompt = f"""
    Scene ID: {scene_id}
    Vietnamese Voiceover Sentences: "{sentences}"
    Suggested Core Visual Concept: "{base_prompt}"
    Previous Scene Prompt (for continuity check, if any): "{prev_prompt}"
    
    Create the S-Grade English Video Prompt now. Choose the correct style suffix (Flat 2D Vector or Graphic Novel Ink) based on the rules.
    """
    
    payload = {
        "contents": [{"parts": [{"text": user_prompt}]}],
        "systemInstruction": {"parts": [{"text": system_instruction}]}
    }
    headers = {"Content-Type": "application/json"}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={api_key}"
    
    for attempt in range(3):
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                res_json = response.json()
                text = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
                # Clean up quotes and markdown block if returned
                text = text.replace("```", "").strip()
                if text.startswith('"') and text.endswith('"'):
                    text = text[1:-1].strip()
                return text
        except Exception as e:
            print(f"    Warning: API attempt {attempt+1} failed: {e}")
            time.sleep(2)
            
    # Fallback
    return f"A steady shot showing a flat 2D vector representation of: {sentences}, flat 2D vector illustration style, clean bold outlines, flat colors, vibrant color palette, cinematic lighting, 8-second continuous documentary video --ar 16:9"

def main():
    json_path = os.path.join(BASE_DIR, "episodes", EPISODE_SLUG, "scene_timing_map.json")
    output_path = os.path.join(BASE_DIR, "episodes", EPISODE_SLUG, "video_prompts.txt")
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return
        
    with open(json_path, "r", encoding="utf-8") as f:
        scenes = json.load(f)
        
    print(f"📖 Loaded {len(scenes)} scenes from scene map.")
    print("🚀 Starting S-Grade prompt generation with LLM (No hardcoded stitching)...")
    
    prompts = []
    prev_prompt = ""
    
    for idx, scene in enumerate(scenes):
        scene_id = scene["id"]
        sentences = " ".join(scene["sentences"])
        base_prompt = scene.get("base_english_prompt", "")
        
        print(f"  [{idx+1}/{len(scenes)}] Generating prompt for {scene_id} via LLM...")
        full_prompt = generate_visual_prompt_via_llm(API_KEY, scene_id, sentences, base_prompt, prev_prompt)
        
        # Ensure it is on a single line and matches structure
        full_prompt = " ".join(full_prompt.split())
        
        # Format: SC[scene_id]: [prompt]
        formatted_line = f"{scene_id}: {full_prompt}"
        prompts.append(formatted_line)
        prev_prompt = full_prompt
        
        time.sleep(1.5) # Safe rate limit padding
        
    # Write to file separated by exactly one blank line
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(prompts))
        
    print(f"✅ Success! Created {output_path} with {len(scenes)} prompts.")

if __name__ == "__main__":
    main()
