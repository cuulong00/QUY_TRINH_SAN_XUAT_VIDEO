import os
import csv
import json
import urllib.request
import urllib.parse
import uuid

# Configuration parameters
COMFYUI_ADDRESS = "127.0.0.1:8188"
CLIENT_ID = str(uuid.uuid4())
OUTPUT_DIR = "episodes/chi-trich-con-cai/videos"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def queue_prompt(prompt_workflow):
    """Queues a prompt workflow to ComfyUI's REST API endpoint."""
    p = {"prompt": prompt_workflow, "client_id": CLIENT_ID}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(f"http://{COMFYUI_ADDRESS}/prompt", data=data)
    response = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(response)

def wait_for_execution(prompt_id):
    """
    Connects to ComfyUI websocket server to track node execution progress
    and blocks until the queued video rendering completes.
    """
    import websocket # Needs pip install websocket-client
    ws = websocket.WebSocket()
    ws.connect(f"ws://{COMFYUI_ADDRESS}/ws?clientId={CLIENT_ID}")
    
    print(f"  [ComfyUI] Processing workflow job (ID: {prompt_id})...")
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    print("  [ComfyUI] Job execution completed successfully.")
                    break
        else:
            continue
    ws.close()

def run_local_pipeline(csv_path, workflow_json_path):
    if not os.path.exists(workflow_json_path):
        print(f"⚠️ Error: ComfyUI workflow JSON '{workflow_json_path}' not found.")
        print("Please save your ComfyUI workflow in API format to this path.")
        return

    # Load the template workflow API JSON
    with open(workflow_json_path, 'r', encoding='utf-8') as f:
        workflow = json.load(f)
        
    print("=== STARTING LOCAL COMFYUI AUTOMATION PIPELINE ===")
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row or not row.get('segment_id'):
                continue
            segment_id = row['segment_id']
            visual_motifs = row['visual_motifs']
            motion_style = row['motion_style']
            
            output_file = os.path.join(OUTPUT_DIR, f"{segment_id}.mp4")
            
            # Skip if video clip already exists
            if os.path.exists(output_file):
                print(f"⏩ Segment {segment_id} already exists. Skipping.")
                continue
                
            print(f"\n🎬 Queueing Segment: {segment_id}")
            try:
                # UPDATE CORRESPONDING WORKFLOW NODES WITH CSV DATA
                # IMPORTANT: Replace these node IDs ("6", "12", "15") with your actual workflow node IDs!
                
                # 1. Update text prompt for Flux.1/SDXL image generation
                workflow["6"]["inputs"]["text"] = f"{visual_motifs}, 2D anime style, chiaroscuro, cinematic lighting"
                
                # 2. Update movement settings/prompts for Image-to-Video node (e.g. SVD/CogVideo)
                workflow["12"]["inputs"]["text"] = f"{motion_style}, slow movement, drifting camera, ambient loop"
                
                # 3. Update output filename prefix in the Save Video node
                workflow["15"]["inputs"]["filename_prefix"] = f"{segment_id}"
                
                # Queue job
                response = queue_prompt(workflow)
                prompt_id = response['prompt_id']
                
                # Wait until current segment is done before queueing next
                wait_for_execution(prompt_id)
                
            except Exception as e:
                print(f"❌ Error queueing segment {segment_id} to ComfyUI: {str(e)}")
                # Continue processing other scenes
                continue

if __name__ == "__main__":
    csv_file = "episodes/chi-trich-con-cai/visual_map.csv"
    workflow_json = "episodes/chi-trich-con-cai/workflow_api.json"
    
    # Check if websocket client package is available
    try:
        import websocket
    except ImportError:
        print("⚠️ Module 'websocket-client' is missing. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "websocket-client"])
        
    run_local_pipeline(csv_file, workflow_json)
