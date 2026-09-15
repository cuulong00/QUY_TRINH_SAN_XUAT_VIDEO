import json
import urllib.request
import urllib.error
import ssl
import time
import os

API_KEY = "AIzaSyB60CuKiFCCUkN3GYMr8xqzYitMXcTULLs"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
BASE_DIR = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/vinfast-vien-trinh"
JSON_FILE = os.path.join(BASE_DIR, "scene_timing_map.json")
OUT_FILE = os.path.join(BASE_DIR, "video_prompts.txt")

SYSTEM_INSTRUCTION = """
Bạn là The Visual Storyteller (Đạo diễn Hình Ảnh Phác Họa).
Nhiệm vụ: Viết Prompt tiếng Anh để TẠO VIDEO (AI Video Generation) từ một loạt các Visual Summary.

Quy định BẮT BUỘC (ANTI-BYPASS PROTOCOL):
1. Bạn sẽ nhận được 1 danh sách các scenes (id, visual_summary, góc máy bắt buộc).
2. YÊU CẦU ĐỊNH DẠNG: TRẢ VỀ kết quả dưới dạng text, MỖI PROMPT NẰM TRÊN ĐÚNG 1 DÒNG DUY NHẤT. Cấu trúc là "SCENE_ID: [Prompt]". Không có markdown thừa, không giải thích.
3. VIDEO THỰC TẾ (PHOTOREALISTIC): NGHIÊM CẤM TẠO HOẠT HÌNH HAY 2D/3D ANIMATION. Các video phải trông như phim tài liệu điện ảnh quay bằng máy quay thật (Cinematic live-action documentary footage).
4. BỐI CẢNH & NHÂN VẬT: Nhân vật chính chủ yếu là NGƯỜI VIỆT NAM (hoặc có nét Châu Á - Asian features) trừ khi nói về thị trường ngoại/chuyên gia Mỹ. Bối cảnh phải phù hợp tuyệt đối với nội dung video (Nhà máy VinFast khổng lồ, xe điện VF 8, VF 3, VF 5, taxi Xanh SM, trạm sạc V-Green, thị trường chứng khoán Mỹ, đại lý xe tại Indonesia/Ấn Độ, đường phố Việt Nam). Phải giữ sự chân thực về ngành công nghiệp ô tô và khía cạnh tài chính.
5. CHUYỂN ĐỘNG (MOTION): Prompt video BẮT BUỘC phải mô tả sự di chuyển/hành động. Ví dụ: "Cinematic drone shot flying over...", "Slow motion tracking shot of...", "Handheld camera moving towards...".
6. CÔNG THỨC PROMPT BẮT BUỘC:
   [Camera Movement/Angle] showing [SUBJECT in ACTION] in [ENVIRONMENT]. [LIGHTING & COLOR]. Highly realistic documentary footage, 8k resolution, cinematic color grading, culturally authentic elements, photorealistic --ar 16:9
7. Mỗi prompt cách nhau bởi 1 dòng trống.

Ví dụ Output:
SC001: Cinematic drone shot flying over a massive, ultra-modern VinFast automobile factory in Hai Phong at sunrise. Dozens of robotic arms are actively welding car frames. Highly realistic documentary footage, 8k resolution, cinematic color grading, culturally authentic elements, photorealistic --ar 16:9

SC002: Slow motion tracking shot of a worried Vietnamese car owner standing next to a sleek VF 8 electric vehicle, looking at a fluctuating digital stock chart on a tablet. Highly realistic documentary footage, 8k resolution, cinematic color grading, culturally authentic Vietnamese elements, photorealistic --ar 16:9
"""

def get_angle(index):
    angles = [
        "Cinematic drone shot flying over",
        "Slow motion tracking shot of",
        "Handheld camera moving towards",
        "Smooth panning shot across"
    ]
    return angles[index % 4]

def call_gemini(batch_text):
    data = {
        "contents": [{"parts": [{"text": batch_text}]}],
        "systemInstruction": {"parts": [{"text": SYSTEM_INSTRUCTION}]},
        "generationConfig": {"temperature": 0.4}
    }
    req = urllib.request.Request(URL, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(req, context=ctx) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data['candidates'][0]['content']['parts'][0]['text']
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    if not os.path.exists(JSON_FILE):
        print(f"File not found: {JSON_FILE}")
        return

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        scenes = json.load(f)
    
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write("") # Clear file
    
    batch_size = 5 # Reduced batch size for Gemini 1.5 Pro to handle complex reasoning better
    for i in range(0, len(scenes), batch_size):
        batch = scenes[i:i+batch_size]
        prompt_input = "Hãy tạo prompt video cho các scenes sau, đảm bảo bối cảnh Việt Nam/Quốc tế và tính chân thực:\n"
        for idx, scene in enumerate(batch):
            global_idx = i + idx
            angle = get_angle(global_idx)
            prompt_input += f"- ID: {scene.get('id', f'SC{global_idx+1:03d}')} | Camera Movement: {angle} | Visual Summary: {scene.get('visual_summary', '')}\n"
        
        print(f"Processing scenes {i+1} to {i+len(batch)}...")
        result = call_gemini(prompt_input)
        if result:
            with open(OUT_FILE, 'a', encoding='utf-8') as f:
                f.write(result.strip() + "\n\n")
            print("Success.")
        else:
            print("Failed.")
        time.sleep(4) # rate limit protection for Pro model

    print(f"All done! Output saved to {OUT_FILE}")

if __name__ == "__main__":
    main()
