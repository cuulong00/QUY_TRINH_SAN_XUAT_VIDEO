#!/usr/bin/env python3
"""
Gemini TTS Recorder for HieuBietHon
===================================
Thu âm voiceover cho episode bằng Gemini API TTS.
Sử dụng giọng nam cao cấp sinh bởi mô hình Gemini 3.1 Flash.

Usage:
    python3 scripts/tts/gemini_tts_record.py <episode_slug> [--voice <voice_name>] [--key <api_key>] [--model <model_name>]
    
Example:
    python3 scripts/tts/gemini_tts_record.py walmart-quyen-luc --voice Algenib
"""

import sys
import os
import glob
import wave
import time
import json
import re
import argparse
import base64
import httpx

# ============================================================
# CẤU HÌNH MẶC ĐỊNH
# ============================================================
DEFAULT_API_KEY = "AQ.Ab8RN6IEVMCQ9JKi9S12-Ev-Q79kYcjRiCrhEGz-qxZ9dEGG9A"
DEFAULT_API_KEYS = [
    "AQ.Ab8RN6IEVMCQ9JKi9S12-Ev-Q79kYcjRiCrhEGz-qxZ9dEGG9A", # Key 5
    "AQ.Ab8RN6K8CDU7qKZdXHFcmRn7xYYNdFp1KpIsu5hjTvy1H53BSg"  # Key 6
]
DEFAULT_MODEL = "gemini-3.1-flash-tts-preview"
DEFAULT_VOICE = "Algenib"

# Thư mục gốc của project
BASE_DIR = "/Users/pro16/Documents/VideoProject/HieuBietHon"

# ============================================================
# HÀM TIỆN ÍCH
# ============================================================

def read_chapters(episode_slug: str) -> list[dict]:
    """Đọc tất cả chapter_XX.md theo thứ tự, trả về list[{number, text}]."""
    episode_dir = os.path.join(BASE_DIR, "episodes", episode_slug)
    pattern = os.path.join(episode_dir, "chapter_[0-9][0-9].md")
    files = sorted(glob.glob(pattern))
    
    if not files:
        print(f"❌ Không tìm thấy chapter nào trong {episode_dir}")
        sys.exit(1)
    
    chapters = []
    for f in files:
        basename = os.path.basename(f)
        # Lấy số chapter từ tên file (chapter_01.md -> 01)
        match = re.search(r'chapter_(\d+)\.md', basename)
        if not match:
            continue
        chapter_num = match.group(1)
        
        with open(f, 'r', encoding='utf-8') as fh:
            text = fh.read().strip()
        
        # Loại bỏ metadata YAML nếu có
        if text.startswith('---'):
            parts = text.split('---', 2)
            if len(parts) >= 3:
                text = parts[2].strip()
        
        if text:
            chapters.append({
                "number": chapter_num,
                "file": basename,
                "text": text
            })
    
    return chapters


def split_text_into_chunks(text: str, max_chars: int = 4000) -> list[str]:
    """
    Tách văn bản thành các đoạn nhỏ hơn max_chars ký tự.
    Tách theo đoạn văn (2 newline) trước, nếu vẫn dài thì tách theo câu.
    """
    # Nếu text đã ngắn đủ, trả về nguyên
    if len(text) <= max_chars:
        return [text]
    
    # Tách theo đoạn văn
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        if len(current_chunk) + len(para) + 2 <= max_chars:
            current_chunk += ("\n\n" + para) if current_chunk else para
        else:
            if current_chunk:
                chunks.append(current_chunk)
            
            # Nếu một paragraph đơn lẻ vẫn dài hơn max_chars
            if len(para) > max_chars:
                # Tách theo câu
                sentences = re.split(r'(?<=[.!?])\s+', para)
                sub_chunk = ""
                for sent in sentences:
                    if len(sub_chunk) + len(sent) + 1 <= max_chars:
                        sub_chunk += (" " + sent) if sub_chunk else sent
                    else:
                        if sub_chunk:
                            chunks.append(sub_chunk)
                        sub_chunk = sent
                if sub_chunk:
                    current_chunk = sub_chunk
                else:
                    current_chunk = ""
            else:
                current_chunk = para
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks


def clean_text_for_tts(text: str) -> str:
    """Chuẩn hóa viết tắt và số để Gemini đọc tự nhiên hơn."""
    # Loại bỏ các tag markdown và ký tự lạ
    text = text.replace("&", "và").replace("<", "").replace(">", "").replace('"', "").replace("'", "")
    
    # Mở rộng các từ viết tắt phổ biến
    text = text.replace("TP. Hồ Chí Minh", "Thành phố Hồ Chí Minh")
    text = text.replace("TP. HCM", "Thành phố Hồ Chí Minh")
    text = text.replace("quý I", "quý một")
    text = text.replace("quý 1", "quý một")
    text = text.replace("USD", "đô la Mỹ")
    text = text.replace("HieuBietHon", "Éch Ê cô nô mích")
    
    # Phiên âm thương hiệu, dòng xe và các từ viết tắt chuyên ngành
    text = text.replace("VF MPV 7", "vê ép em pi vi bẩy")
    text = text.replace("VF MPV", "vê ép em pi vi")
    text = text.replace("GSM", "gi ét em")
    text = text.replace("Xanh SM", "xanh ét em")
    text = text.replace("Green SM", "green ét em")
    text = text.replace("VF", "vê ép")
    text = text.replace("MPV", "em pi vi")
    text = text.replace("LFP", "el ép bê")
    text = text.replace("ARAI", "a rai")
    text = text.replace("IPO", "ai bi o")
    text = text.replace("VIC", "vê i cê")
    text = text.replace("VFS", "vê ép ét")
    text = text.replace("GDP", "gờ đê bê")
    text = text.replace("M&A", "em và a")
    text = text.replace("CBU", "xê bê u")
    text = text.replace("DVA", "đê vê a")
    text = text.replace("PM E-DRIVE", "bê em e đrai vơ")
    text = text.replace("Delhi-NCR", "đen hi en xê e")
    
    # Phiên âm thương hiệu bất động sản
    text = text.replace("Batdongsan.com.vn", "bất động sản chấm com chấm vi en")
    text = text.replace("batdongsan.com.vn", "bất động sản chấm com chấm vi en")
    text = text.replace("Phongtro123", "phòng trọ một hai ba")
    text = text.replace("phongtro123", "phòng trọ một hai ba")
    
    # Chuẩn hóa phát âm từ AI để tránh bị đọc nhầm thành từ "ai" tiếng Việt
    text = re.sub(r'\bAI\b', 'Ây Ai', text)
    
    return text


def synthesize_chunk(api_key: str, text: str, chunk_id: str, output_path: str, voice_name: str, model_name: str) -> bool:
    """
    Gọi Gemini TTS REST API trực tiếp để tổng hợp giọng nói cho một đoạn text.
    Trả về True nếu thành công.
    """
    cleaned_text = clean_text_for_tts(text)
    
    # Thiết lập prompt hướng dẫn giọng đọc chuyên nghiệp và chèn các khoảng dừng logic
    prompt_instruction = (
        "Read the following Vietnamese text in a clear, natural, and confident voice of a professional male news presenter. "
        "Speak clearly and articulately with standard Northern Vietnamese pronunciation (Giọng miền Bắc chuẩn). "
        "Avoid whispering, gasping, or overly dramatic pauses. Keep a steady, natural narration pace. "
        "Only read the text, do not add anything else:\n\n" + cleaned_text
    )
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt_instruction
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {
                    "prebuiltVoiceConfig": {
                        "voiceName": voice_name
                    }
                }
            }
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    
    try:
        # Tắt HTTP/2 bằng cách sử dụng httpx Client thuần với http2=False để tránh lỗi SSL handshake trên macOS
        with httpx.Client(http2=False, timeout=45.0) as client:
            response = client.post(url, json=payload, headers=headers)
        
        if response.status_code != 200:
            print(f"  ❌ {chunk_id}: Lỗi API REST (Status {response.status_code}) — {response.text}")
            return False
            
        res_data = response.json()
        candidates = res_data.get("candidates", [])
        if not candidates:
            print(f"  ⚠️ {chunk_id}: Response không chứa candidates — {res_data}")
            return False
            
        parts = candidates[0].get("content", {}).get("parts", [])
        for part in parts:
            inline_data = part.get("inlineData")
            if inline_data:
                base64_data = inline_data.get("data")
                audio_bytes = base64.b64decode(base64_data)
                
                # Lưu file WAV
                with wave.open(output_path, "wb") as wav_file:
                    wav_file.setnchannels(1)      # Mono
                    wav_file.setsampwidth(2)       # 16-bit
                    wav_file.setframerate(24000)   # 24kHz (chuẩn Gemini)
                    wav_file.writeframes(audio_bytes)
                
                print(f"  ✅ {chunk_id} → {output_path} ({len(audio_bytes)} bytes)")
                return True
                
        print(f"  ⚠️ {chunk_id}: Response không chứa inlineData")
        return False
        
    except Exception as e:
        print(f"  ❌ {chunk_id}: Lỗi kết nối API — {e}")
        return False


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Gemini TTS Recorder for HieuBietHon")
    parser.add_argument("episode_slug", help="Slug của episode cần thu âm")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help="Tên giọng đọc Gemini (ví dụ: Algenib, Fenrir, Alnilam, Puck, Charon)")
    parser.add_argument("--key", default=DEFAULT_API_KEY, help="API Key Google AI Studio")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model tên (mặc định: gemini-3.1-flash-tts-preview)")
    parser.add_argument("--chapter", default=None, help="Chỉ thu âm chapter cụ thể (ví dụ: 02)")
    
    args = parser.parse_args()
    
    slug = args.episode_slug
    voice_name = args.voice
    api_key = args.key
    model_name = args.model
    
    audio_dir = os.path.join(BASE_DIR, "episodes", slug, "audio", voice_name)
    os.makedirs(audio_dir, exist_ok=True)
    
    print(f"🎙️  Gemini TTS Recorder — HieuBietHon")
    print(f"📂  Episode: {slug}")
    print(f"🔊  Voice: {voice_name}")
    print(f"🤖  Model: {model_name}")
    print(f"=" * 60)
    
    # Đọc chapters
    chapters = read_chapters(slug)
    print(f"\n📖  Tìm thấy {len(chapters)} chương:")
    for ch in chapters:
        print(f"   • {ch['file']} ({len(ch['text'])} ký tự)")
    
    # Phân tách api keys từ tham số hoặc mặc định
    if api_key == DEFAULT_API_KEY:
        api_keys = DEFAULT_API_KEYS
    else:
        api_keys = [k.strip() for k in api_key.split(",")]
        
    current_key_idx = 0
    
    # Report
    report = {
        "episode": slug,
        "model": model_name,
        "voice": voice_name,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "chapters": []
    }
    
    total_chunks = 0
    success_count = 0
    fail_count = 0
    
    for ch in chapters:
        chapter_num = ch["number"]
        if args.chapter and chapter_num != args.chapter:
            continue
        print(f"\n{'='*60}")
        print(f"🎬  Đang thu âm Chương {chapter_num} ({ch['file']})")
        print(f"{'='*60}")
        
        # Tách thành chunks ngắn dưới 3000 ký tự tránh tràn giới hạn API và timeout
        chunks = split_text_into_chunks(ch["text"], max_chars=3000)
        print(f"   Tách thành {len(chunks)} phần")
        
        chapter_report = {
            "chapter": chapter_num,
            "file": ch["file"],
            "chunks": len(chunks),
            "results": []
        }
        
        for i, chunk_text in enumerate(chunks):
            chunk_id = f"ch{chapter_num}_part{i+1:02d}"
            output_file = os.path.join(audio_dir, f"{chunk_id}.wav")
            
            # Bỏ qua nếu file đã tồn tại và hợp lệ
            if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                print(f"  ⏭️  {chunk_id} đã tồn tại, bỏ qua")
                chapter_report["results"].append({"chunk": chunk_id, "status": "skipped"})
                success_count += 1
                total_chunks += 1
                continue
            
            total_chunks += 1
            
            # Cơ chế xoay vòng API Keys tự động khi gặp lỗi
            ok = False
            for attempt in range(len(api_keys)):
                key_to_use = api_keys[current_key_idx]
                
                print(f"  🎙️ Đang gọi REST API với Key Index {current_key_idx} (Đuôi: ...{key_to_use[-6:]})")
                ok = synthesize_chunk(key_to_use, chunk_text, chunk_id, output_file, voice_name, model_name)
                
                if ok:
                    break
                else:
                    # Xoay vòng key và thử lại ngay lập tức
                    current_key_idx = (current_key_idx + 1) % len(api_keys)
                    print(f"  🔄 Gặp lỗi, tự động xoay sang API Key Index {current_key_idx}")
                    time.sleep(3) # Nghỉ 3 giây trước khi thử key mới
            
            if ok:
                success_count += 1
                chapter_report["results"].append({"chunk": chunk_id, "status": "success"})
            else:
                fail_count += 1
                chapter_report["results"].append({"chunk": chunk_id, "status": "failed"})
            
            # Tránh giới hạn tần suất (Rate Limit) cho gói free (3 RPM)
            time.sleep(22)
        
        report["chapters"].append(chapter_report)
    
    # Lưu report
    report_path = os.path.join(audio_dir, "recording_report.json")
    report["summary"] = {
        "total_chunks": total_chunks,
        "success": success_count,
        "failed": fail_count
    }
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print(f"📊  KẾT QUẢ THU ÂM")
    print(f"{'='*60}")
    print(f"   Tổng chunks: {total_chunks}")
    print(f"   Thành công:  {success_count}")
    print(f"   Thất bại:    {fail_count}")
    print(f"   Report:      {report_path}")
    
    if fail_count > 0:
        print(f"\n⚠️  Có {fail_count} chunk bị lỗi. Chạy lại script để retry (file đã thành công sẽ được bỏ qua).")
    else:
        print(f"\n🎉  Thu âm hoàn tất! Tất cả file audio nằm tại: {audio_dir}/")
 

if __name__ == "__main__":
    main()
