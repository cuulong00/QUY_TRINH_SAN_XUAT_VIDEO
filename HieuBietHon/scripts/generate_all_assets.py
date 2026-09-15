#!/usr/bin/env python3
"""
HieuBietHon Asset Generator
===========================
Script to generate high-quality visual assets using the Google GenAI SDK and Imagen 4.

Usage:
    python3 scripts/generate_all_assets.py <episode_slug> [--api-key YOUR_API_KEY]
"""

import os
import sys
import argparse
from google import genai
from google.genai import types

# Standard HieuBietHon API Key (Free tier - requires upgrade for Imagen 3/4)
DEFAULT_API_KEY = "AIzaSyBOpJFS43_WRvO3S1XdZUTIhkhAD-wVU38"
MODEL = "imagen-4.0-generate-001"

# The key visual assets to generate for 'showbiz_drugs_economics'
ASSETS = {
    "factory_vs_star": {
        "id": 2,
        "filename": "factory_vs_star.png",
        "prompt": (
            "A SYMMETRICAL COMPOSITION showing a split-screen infographic. "
            "On the left side: a busy modern factory with smoke coming from chimneys and a bright green arrow pointing upwards. "
            "On the right side: a torn advertising poster of a celebrity star face crossed out with a red 'X', and a bright red arrow pointing downwards to zero. "
            "Clean minimalist tech office background. Bright studio lighting with high contrast. "
            "modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic"
        )
    },
    "stock_chart_comparison": {
        "id": 5,
        "filename": "stock_chart_comparison.png",
        "prompt": (
            "A SYMMETRICAL COMPOSITION showing a large dark digital screen displaying two line charts. "
            "A bright green line rises sharply and is labeled '+2.10% (Stabilized at 24h-48h)' in clean sans-serif text. "
            "A bright red line plunges downwards and is labeled '-1.88% (Delayed reaction)' in clean red text. "
            "Clean corporate boardroom background. Neon green and red ambient glow. "
            "modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic"
        )
    },
    "propofol_scale_comparison": {
        "id": 7,
        "filename": "propofol_scale_comparison.png",
        "prompt": (
            "A SYMMETRICAL COMPOSITION showing a large retro mechanical balance scale. "
            "On the left pan of the scale sits a small single glass ampoule of propofol with a light green label marked '70M Won', "
            "while on the right pan of the scale sits a massive towering pile of glowing gold bricks and glass ampoules of propofol "
            "with a large red label marked '10B Won' tipping the scale heavily downwards on the right side. "
            "Dark minimalist digital abstract space with glowing neon green grid lines on the floor. "
            "Dramatic chiaroscuro lighting with sharp cyan and amber rim lights casting long shadows. "
            "modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic"
        )
    },
    "storefront_billboard": {
        "id": 4,
        "filename": "storefront_billboard.png",
        "prompt": (
            "A WIDE STILL SHOT showing a busy Vietnamese street scene in front of a modern fashion store. "
            "A customer with Asian features stands outside, looking up at a giant billboard sign showing a celebrity's face covered with a large red 'X'. "
            "Pedestrians walk past. Sunny day lighting with sharp shadows. "
            "modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic"
        )
    },
    "virtual_influencer_studio": {
        "id": 16,
        "filename": "virtual_influencer_studio.png",
        "prompt": (
            "A MID SHOT showing a beautiful female virtual influencer with Vietnamese features posing inside a high-tech photo studio. "
            "She is surrounded by floating holographic screens displaying code, green data charts, and digital pixels. "
            "Professional camera gear stands in front of her. Bright ring light lighting. "
            "modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic"
        )
    },
    "closing_shot": {
        "id": 21,
        "filename": "closing_shot.png",
        "prompt": (
            "A SYMMETRICAL COMPOSITION showing a modern balance scale with two hands. "
            "On the left pan: a warm, detailed human hand with Vietnamese/Asian skin tone, palm up. "
            "On the right pan: a sleek, metallic robotic hand with glowing blue data circuits, palm up. "
            "The scale is perfectly balanced. Dark abstract digital workspace background with faint glowing grid lines. "
            "Dramatic rim lighting casting long shadows. "
            "modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic"
        )
    }
}

def generate_asset(client, slug, asset_name, asset_info):
    save_dir = f"/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/{slug}/images"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, asset_info["filename"])
    
    print(f"\n🎨 Generating Asset #{asset_info['id']} ({asset_name}) -> {save_path}...")
    print(f"Prompt: {asset_info['prompt']}")
    
    try:
        response = client.models.generate_images(
            model=MODEL,
            prompt=asset_info["prompt"],
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                output_mime_type="image/png"
            )
        )
        
        if not response.generated_images:
            print("❌ No images returned from Gemini API.")
            return False
            
        generated_image = response.generated_images[0]
        image_bytes = generated_image.image.image_bytes
        
        with open(save_path, "wb") as f:
            f.write(image_bytes)
            
        print(f"✅ Success! Generated image saved to: {save_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error during generation: {e}")
        if "paid plans" in str(e):
            print("\n⚠️ WARNING: This API key is on the FREE plan and does not have access to Imagen.")
            print("Please upgrade your billing at https://aistudio.google.com/ or https://ai.dev/projects.")
        return False

def main():
    parser = argparse.ArgumentParser(description="Generate HieuBietHon episode image assets using Gemini API.")
    parser.add_argument("slug", help="The episode slug (e.g. showbiz_drugs_economics)")
    parser.add_argument("--api-key", default=DEFAULT_API_KEY, help="Gemini API key")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🚀 GOCNHINPODCAST IMAGE ASSET GENERATOR")
    print(f"Model: {MODEL}")
    print(f"Episode: {args.slug}")
    print("=" * 60)
    
    client = genai.Client(api_key=args.api_key)
    
    success_count = 0
    for name, info in ASSETS.items():
        if generate_asset(client, args.slug, name, info):
            success_count += 1
            
    print("\n" + "=" * 60)
    print(f"🎉 Asset generation finished. Successfully generated {success_count}/{len(ASSETS)} assets.")
    print("=" * 60)

if __name__ == "__main__":
    main()
