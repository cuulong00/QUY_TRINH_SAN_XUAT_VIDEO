#!/usr/bin/env python3
import os
import wave
import time
from google import genai
from google.genai import types

# Cấu hình
API_KEY = "AQ.Ab8RN6IEVMCQ9JKi9S12-Ev-Q79kYcjRiCrhEGz-qxZ9dEGG9A"
MODEL_NAME = "gemini-3.1-flash-tts-preview"
VOICES = ["Charon"]

CHAPTER_FILE = "/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/chinh-sach-nha-cho-thue/chapter_01.md"
OUTPUT_DIR = "/Users/pro16/.gemini/antigravity/brain/4ca1dc12-20e1-4033-a8e0-b6c4e6eae513/scratch"

def clean_text_for_tts(text: str) -> str:
    # Loại bỏ các tag markdown và ký tự lạ
    text = text.replace("&", "và").replace("<", "").replace(">", "").replace('"', "").replace("'", "")
    
    # Mở rộng các từ viết tắt phổ biến
    text = text.replace("TP. Hồ Chí Minh", "Thành phố Hồ Chí Minh")
    text = text.replace("TP. HCM", "Thành phố Hồ Chí Minh")
    text = text.replace("quý I", "quý một")
    text = text.replace("quý 1", "quý một")
    text = text.replace("USD", "đô la Mỹ")
    text = text.replace("HieuBietHon", "Ít Ế cô nô míc")
    
    return text

def main():
    print("🚀 Khởi chạy sinh thử nghiệm Chương 1 bằng 5 giọng với prompt mới...")
    
    with open(CHAPTER_FILE, "r", encoding="utf-8") as f:
        raw_text = f.read().strip()
        
    # Loại bỏ YAML metadata nếu có
    if raw_text.startswith("---"):
        parts = raw_text.split("---", 2)
        if len(parts) >= 3:
            raw_text = parts[2].strip()
            
    cleaned_text = clean_text_for_tts(raw_text)
    
    # Cấu trúc prompt đơn giản ban đầu (restored)
    prompt_instruction = (
        "Read the following Vietnamese text with a professional, serious, and deep economic news anchor voice. "
        "Keep a calm, slow pace. Add natural pauses. Do not say anything else, only read the text:\n\n" + cleaned_text
    )
    
    client = genai.Client(api_key=API_KEY)
    
    for voice in VOICES:
        print(f"\n🎙️ Đang sinh audio cho giọng: {voice}...")
        output_file = os.path.join(OUTPUT_DIR, f"ch01_restored_prompt_{voice.lower()}.wav")
        
        config = types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice
                    )
                )
            )
        )
        
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt_instruction,
                config=config
            )
            
            # Trích xuất audio data
            found_audio = False
            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    audio_bytes = part.inline_data.data
                    
                    with wave.open(output_file, "wb") as wav_file:
                        wav_file.setnchannels(1)      # Mono
                        wav_file.setsampwidth(2)       # 16-bit
                        wav_file.setframerate(24000)   # 24kHz
                        wav_file.writeframes(audio_bytes)
                    
                    print(f"✅ Thành công! Đã lưu: {output_file} ({len(audio_bytes)} bytes)")
                    found_audio = True
                    break
            
            if not found_audio:
                print(f"⚠️ Thất bại cho giọng {voice}: Response không chứa audio data")
                
        except Exception as e:
            print(f"❌ Lỗi khi sinh giọng {voice}: {e}")
            
        # Nghỉ để tránh Rate Limit
        print("Chờ 5 giây tránh Rate Limit...")
        time.sleep(5)
        
    print("\n🎉 Hoàn thành sinh thử nghiệm cả 5 giọng!")

if __name__ == "__main__":
    main()
