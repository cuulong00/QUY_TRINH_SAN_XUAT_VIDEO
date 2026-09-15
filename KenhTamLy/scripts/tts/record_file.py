#!/usr/bin/env python3
import json
import urllib.request
import urllib.error
import sys
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def vbee_tts(text, output_file):
    config = load_config()
    
    url = f"{config['api_base']}/v1/tts"
    headers = {
        'Content-Type': 'application/json',
        'app-id': config['app_id'],
        'Authorization': f"Bearer {config['token']}"
    }
    
    data = {
        'app_id': config['app_id'],
        'input_text': text,
        'voice_code': config['voice_code'],
        'audio_type': config.get('audio_type', 'mp3'),
        'bitrate': config.get('bitrate', 128),
        'speed_rate': config.get('speed_rate', 1.0),
        'response_type': 'direct'
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as res:
            res_data = json.loads(res.read().decode('utf-8'))
            print("API Response:", res_data)
            
            result = res_data.get('result', {})
            audio_link = result.get('audio_link') or result.get('audio_url')
            
            if not audio_link:
                print("Lỗi: Không tìm thấy link audio từ API.")
                return
            
            print(f"Đang tải file từ {audio_link}...")
            urllib.request.urlretrieve(audio_link, output_file)
            print(f"✅ Đã lưu file audio tại: {output_file}")
            
    except urllib.error.HTTPError as e:
        print(f"Lỗi HTTP: {e.code} - {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Sử dụng: python3 record_file.py <path_to_markdown>")
        sys.exit(1)
        
    md_file = sys.argv[1]
    
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read().strip()
        
    if not text:
        print("Lỗi: File rỗng")
        sys.exit(1)
        
    out_file = os.path.splitext(md_file)[0] + '.mp3'
    print(f"🎙️ Gửi {len(text)} ký tự cho Vbee TTS...")
    vbee_tts(text, out_file)
