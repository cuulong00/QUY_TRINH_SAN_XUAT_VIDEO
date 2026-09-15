import os
import csv
import time
import io
from google import genai
from google.genai import types

# ----------------------------------------------------------------------
# Authentication Configuration
# ----------------------------------------------------------------------
# Prioritize standard Google AI Studio (Gemini API Key)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Fallback to Vertex AI (GCP Project Credentials)
GCP_PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT", "")
GCP_LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

KEYFRAMES_DIR = "episodes/chi-trich-con-cai/keyframes"
VIDEOS_DIR = "episodes/chi-trich-con-cai/videos"

os.makedirs(KEYFRAMES_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

# ----------------------------------------------------------------------
# Initialize Client
# ----------------------------------------------------------------------
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
    print("🤖 Initialized Client: Google AI Studio (Gemini API)")
    is_vertex = False
else:
    if GCP_PROJECT:
        client = genai.Client(vertexai=True, project=GCP_PROJECT, location=GCP_LOCATION)
        print(f"🤖 Initialized Client: Google Cloud Vertex AI (Project: {GCP_PROJECT}, Location: {GCP_LOCATION})")
        is_vertex = True
    else:
        client = None
        print("⚠️ Warning: Neither GEMINI_API_KEY nor GOOGLE_CLOUD_PROJECT is set.")
        print("Please export GEMINI_API_KEY before running this script.")

# ----------------------------------------------------------------------
# Style definitions for 2D Animation
# ----------------------------------------------------------------------
STYLE_TAG = "2D minimalist vector illustration, earthy pastel color palette, terracotta, olive green, warm cream, rough paper texture overlay, flat design, modern editorial illustration style, soft flat shadows"

def generate_keyframe_imagen(prompt_text, output_path):
    """Generates a high-quality keyframe image using Imagen 3."""
    import PIL.Image
    
    full_prompt = f"{prompt_text}, {STYLE_TAG}"
    print(f"  [Imagen] Generating image for: '{prompt_text}'...")
    
    response = client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=full_prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="16:9",
            output_mime_type="image/png"
        )
    )
    
    generated_image = response.generated_images[0]
    image = PIL.Image.open(io.BytesIO(generated_image.image.image_bytes))
    image.save(output_path)
    print(f"  [Imagen] Saved keyframe: {output_path}")

def generate_video_veo(keyframe_path, motion_style, output_path):
    """Animates the keyframe image into a video using Google Veo 3.1."""
    motion_prompt = f"{motion_style}, slow movement, subtle camera motion, ambient motion loop, high quality 2D animation"
    
    # 1. Upload local keyframe to Google Files API (only for AI Studio mode)
    print(f"  [Veo] Uploading keyframe file to Google Files API...")
    uploaded_file = client.files.upload(file=keyframe_path)
    print(f"  [Veo] File uploaded successfully (URI: {uploaded_file.uri})")
    
    try:
        # 2. Trigger Veo video generation
        print(f"  [Veo] Triggering Veo 3.1 video generation...")
        operation = client.models.generate_videos(
            model="veo-3.1-generate-preview",
            prompt=motion_prompt,
            config=types.GenerateVideosConfig(
                aspect_ratio="16:9",
                duration_seconds=5.0, # Generates a 5s loopable segment
                fps=24.0,
                reference_images=[
                    types.VideoGenerationReferenceImage(
                        image=types.Image(
                            uri=uploaded_file.uri,
                            mime_type="image/png"
                        )
                    )
                ]
            ),
        )
        
        # 3. Poll for Long Running Operation completion
        print(f"  [Veo] Task submitted (Operation ID: {operation.name}). Polling for render completion...")
        while not operation.done:
            print("  [Veo] Rendering video... (waiting 20 seconds)")
            time.sleep(20)
            operation = client.operations.get(operation)
            
        # 4. Download and save the video
        print("  [Veo] Rendering complete! Downloading video...")
        generated_video = operation.response.generated_videos[0]
        client.files.download(file=generated_video.video).save(output_path)
        print(f"  [Veo] Saved video clip: {output_path}")
        
    finally:
        # 5. Cleanup the uploaded file from Google Files storage to prevent quota leakage
        print(f"  [Veo] Cleaning up uploaded file '{uploaded_file.name}' from storage...")
        client.files.delete(name=uploaded_file.name)

def run_pipeline(csv_path):
    if not client:
        print("❌ Error: Client is not initialized. Please set GEMINI_API_KEY environment variable.")
        return

    print("=== STARTING GOOGLE VEO 3 / GOOGLE FLOW PIPELINE ===")
    
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row or not row.get('segment_id'):
                continue
            segment_id = row['segment_id']
            visual_motifs = row['visual_motifs']
            motion_style = row['motion_style']
            
            keyframe_file = os.path.join(KEYFRAMES_DIR, f"{segment_id}.png")
            video_file = os.path.join(VIDEOS_DIR, f"{segment_id}.mp4")
            
            # Check if final video already exists
            if os.path.exists(video_file):
                print(f"⏩ Segment {segment_id} video already exists. Skipping.")
                continue
                
            print(f"\n🎬 Processing Segment: {segment_id}")
            try:
                # Step 1: Generate Keyframe Image via Imagen 3 if not already generated
                if not os.path.exists(keyframe_file):
                    generate_keyframe_imagen(visual_motifs, keyframe_file)
                else:
                    print(f"  [Imagen] Keyframe image already exists. Reusing.")
                
                # Step 2: Animate Keyframe via Veo 3.1
                generate_video_veo(keyframe_file, motion_style, video_file)
                
            except Exception as e:
                print(f"❌ Error rendering segment {segment_id} in Google Flow: {str(e)}")
                # Continue processing next segment instead of halting
                continue

if __name__ == "__main__":
    csv_file = "episodes/chi-trich-con-cai/visual_map.csv"
    
    # Pre-checks for required dependencies
    try:
        import PIL.Image
    except ImportError:
        print("⚠️ Module 'Pillow' is missing. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "Pillow"])
        
    run_pipeline(csv_file)
