import os
import csv
import time
import requests
from lumaai import LumaAI

# Config API Keys from Environment Variables
IMAGINEAPI_KEY = os.environ.get("IMAGINEAPI_KEY", "")
LUMAAI_API_KEY = os.environ.get("LUMAAI_API_KEY", "")
OUTPUT_DIR = "episodes/chi-trich-con-cai/videos"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize Luma client if API key is provided
luma_client = LumaAI(auth_token=LUMAAI_API_KEY) if LUMAAI_API_KEY else None

STYLE_TAG = "2D minimalist vector illustration, earthy pastel color palette, terracotta, olive green, warm cream, rough paper texture overlay, flat design, modern editorial illustration style, soft flat shadows"

def generate_midjourney_image(prompt_text):
    """Sends imagine request to Midjourney via ImagineAPI and polls for result."""
    if not IMAGINEAPI_KEY:
        raise ValueError("IMAGINEAPI_KEY is not set. Please set the environment variable.")
        
    headers = {"Authorization": f"Bearer {IMAGINEAPI_KEY}", "Content-Type": "application/json"}
    payload = {
        "prompt": f"{prompt_text}, {STYLE_TAG} --ar 16:9 --v 6.0"
    }
    
    print(f"  [MJ] Sending imagine request for: '{prompt_text}'...")
    response = requests.post("https://cl.imagineapi.dev/items/images", json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    task_id = data["data"]["id"]
    
    print(f"  [MJ] Image generation started (Task ID: {task_id}). Polling status...")
    while True:
        status_resp = requests.get(f"https://cl.imagineapi.dev/items/images/{task_id}", headers=headers)
        status_resp.raise_for_status()
        status_data = status_resp.json()
        status = status_data["data"]["status"]
        
        if status == "completed":
            # Return the first high-res output URL
            return status_data["data"]["url"]
        elif status == "failed":
            raise Exception("Midjourney image generation failed on ImagineAPI!")
            
        time.sleep(10)

def generate_luma_video(image_url, motion_style):
    """Sends image URL and motion prompt to Luma Ray-2 API and polls for video result."""
    if not luma_client:
        raise ValueError("LUMAAI_API_KEY is not set. Please set the environment variable.")
        
    motion_prompt = f"{motion_style}, slow panning shot, subtle parallax depth movement, subtle ambient movement, dust motes drifting slowly, high quality 2D animation"
    
    print(f"  [Luma] Submitting Image-to-Video task with motion style: '{motion_style}'...")
    generation = luma_client.generations.create(
        prompt=motion_prompt,
        model="ray-2",
        keyframes={
            "frame0": {
                "type": "image",
                "url": image_url
            }
        }
    )
    
    print(f"  [Luma] Video task created (ID: {generation.id}). Polling status...")
    while True:
        status_data = luma_client.generations.get(id=generation.id)
        if status_data.state == "completed":
            return status_data.assets.video
        elif status_data.state == "failed":
            raise Exception(f"Luma Ray-2 generation failed: {status_data.failure_reason}")
            
        print("  [Luma] Rendering video... (waiting 10 seconds)")
        time.sleep(10)

def download_file(url, local_filename):
    """Downloads the rendered video clip to local storage."""
    print(f"  [Downloader] Downloading video from {url}...")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"  [Downloader] Download complete: {local_filename}")

def run_pipeline(csv_path):
    if not IMAGINEAPI_KEY or not LUMAAI_API_KEY:
        print("⚠️ Warning: IMAGINEAPI_KEY or LUMAAI_API_KEY environment variables are missing.")
        print("Please export them before running: export IMAGINEAPI_KEY='...' LUMAAI_API_KEY='...'")
        return

    print("=== STARTING CLOUD VIDEO GENERATION PIPELINE ===")
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row or not row.get('segment_id'):
                continue
            segment_id = row['segment_id']
            visual_motifs = row['visual_motifs']
            motion_style = row['motion_style']
            output_file = os.path.join(OUTPUT_DIR, f"{segment_id}.mp4")
            
            # Skip if file already exists to save API credits
            if os.path.exists(output_file):
                print(f"⏩ Segment {segment_id} already exists. Skipping.")
                continue
                
            print(f"\n🎬 Processing Segment: {segment_id}")
            try:
                # 1. Generate Keyframe Image
                image_url = generate_midjourney_image(visual_motifs)
                print(f"  [MJ Success] Image generated at: {image_url}")
                
                # 2. Animate Image using Luma Ray-2 Image-to-Video
                video_url = generate_luma_video(image_url, motion_style)
                
                # 3. Download final video clip
                download_file(video_url, output_file)
                
            except Exception as e:
                print(f"❌ Error rendering segment {segment_id}: {str(e)}")
                # Continue with next scene instead of crashing
                continue

if __name__ == "__main__":
    csv_file = "episodes/chi-trich-con-cai/visual_map.csv"
    run_pipeline(csv_file)
