#!/usr/bin/env python3
"""
Google Cloud TTS Recorder for HieuBietHon
========================================
Thu âm voiceover cho episode bằng Google Cloud Text-to-Speech API (Chirp 3 HD).
Hỗ trợ giọng đọc chất lượng cao, nhất quán và miễn phí hạn mức 1 triệu ký tự/tháng.

Usage:
    python3 scripts/tts/google_cloud_tts_record.py <episode_slug> [--voice <voice_name>] [--key <api_key>]
    
Example:
    python3 scripts/tts/google_cloud_tts_record.py chinh-sach-nha-cho-thue --voice vi-VN-Chirp3-HD-Puck
"""

import sys
import os
import glob
import time
import json
import re
import argparse
import urllib.request
import base64

# ============================================================
# CẤU HÌNH MẶC ĐỊNH
# ============================================================
DEFAULT_API_KEY = "AIzaSyA4G5cv35N4PcjslJ5Ngq7c83Akl2T0dHE"  # Key 2 GCP đã kích hoạt TTS
DEFAULT_VOICE = "vi-VN-Chirp3-HD-Enceladus"


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


def split_text_into_chunks(text: str, max_chars: int = 3500) -> list[str]:
    """
    Tách văn bản thành các đoạn nhỏ hơn max_chars ký tự.
    """
    if len(text) <= max_chars:
        return [text]
    
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
            
            if len(para) > max_chars:
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
    """Chuẩn hóa viết tắt và số để đọc tự nhiên hơn."""
    text = text.replace("&", "và").replace("<", "").replace(">", "").replace('"', "").replace("'", "")
    
    text = text.replace("TP. Hồ Chí Minh", "Thành phố Hồ Chí Minh")
    text = text.replace("TP. HCM", "Thành phố Hồ Chí Minh")
    text = text.replace("quý I", "quý một")
    text = text.replace("quý 1", "quý một")
    text = text.replace("USD", "đô la Mỹ")
    text = text.replace("HieuBietHon", "Éch Ê cô nô mích")
    
    # Chuẩn hóa viết tắt xăng dầu
    text = text.replace("E100", "E một trăm")
    text = text.replace("E10", "E mười")
    text = text.replace("E5", "E năm")
    text = text.replace("RON 95", "Ron chín mươi lăm")
    text = text.replace("RON 92", "Ron chín mươi hai")
    
    # Chuẩn hóa thuật ngữ kinh tế, thương mại
    text = text.replace("CBAM", "Xê Bam")
    text = text.replace("EU", "Ê U")
    text = text.replace("VAT", "Vê A Tê")
    text = text.replace("Net Zero", "Nét Di-rô")
    text = text.replace("Scope 3", "Scốp ba")
    text = text.replace("FDI", "Ép Đê I")
    
    # Chuẩn hóa phát âm từ AI để tránh bị đọc nhầm thành từ "ai" tiếng Việt
    text = re.sub(r'\bAI\b', 'Ây Ai', text)
    
    return text


def synthesize_chunk(api_key: str, text: str, chunk_id: str, output_path: str, voice_name: str) -> bool:
    """
    Gọi Google Cloud Text-to-Speech API để tổng hợp giọng nói.
    """
    cleaned_text = clean_text_for_tts(text)
    
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}"
    data = {
        "input": {"text": cleaned_text},
        "voice": {
            "languageCode": "vi-VN",
            "name": voice_name
        },
        "audioConfig": {
            "audioEncoding": "LINEAR16"  # File WAV chất lượng cao
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            audio_bytes = base64.b64decode(res_data["audioContent"])
            
            with open(output_path, "wb") as f:
                f.write(audio_bytes)
                
            print(f"  ✅ {chunk_id} → {output_path} ({len(audio_bytes)} bytes)")
            return True
            
    except Exception as e:
        print(f"  ❌ {chunk_id}: Lỗi API — {e}")
        if hasattr(e, 'read'):
            try:
                print(f"     Chi tiết lỗi: {e.read().decode('utf-8')}")
            except:
                pass
        return False


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Google Cloud TTS Recorder for HieuBietHon")
    parser.add_argument("episode_slug", help="Slug của episode cần thu âm")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help="Tên giọng đọc (mặc định: vi-VN-Chirp3-HD-Puck)")
    parser.add_argument("--key", default=DEFAULT_API_KEY, help="API Key Google Cloud")
    parser.add_argument("--chapter", default=None, help="Chỉ thu âm chapter cụ thể (ví dụ: 02)")
    
    args = parser.parse_args()
    
    start_time = time.time()  # Track the start of the current run session
    slug = args.episode_slug
    voice_name = args.voice
    api_key = args.key
    
    audio_dir = os.path.join(BASE_DIR, "episodes", slug, "audio", voice_name)
    os.makedirs(audio_dir, exist_ok=True)
    
    print(f"🎙️  Google Cloud TTS Recorder (Chirp 3 HD) — HieuBietHon")
    print(f"📂  Episode: {slug}")
    print(f"🔊  Voice: {voice_name}")
    print(f"=" * 60)
    
    # Đọc chapters
    chapters = read_chapters(slug)
    print(f"\n📖  Tìm thấy {len(chapters)} chương:")
    for ch in chapters:
        print(f"   • {ch['file']} ({len(ch['text'])} ký tự)")
    
    # Report
    report = {
        "episode": slug,
        "engine": "google_cloud_tts",
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
        
        chunks = split_text_into_chunks(ch["text"], max_chars=3500)
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
            
            # Bỏ qua nếu file đã tồn tại và được tạo trong chính lượt chạy này
            if os.path.exists(output_file) and os.path.getsize(output_file) > 1000 and os.path.getmtime(output_file) > start_time:
                print(f"  ⏭️  {chunk_id} đã được tạo trong lượt chạy này, bỏ qua")
                chapter_report["results"].append({"chunk": chunk_id, "status": "skipped"})
                success_count += 1
                total_chunks += 1
                continue
                
            total_chunks += 1
            
            ok = synthesize_chunk(api_key, chunk_text, chunk_id, output_file, voice_name)
            
            if ok:
                success_count += 1
                chapter_report["results"].append({"chunk": chunk_id, "status": "success"})
            else:
                fail_count += 1
                chapter_report["results"].append({"chunk": chunk_id, "status": "failed"})
            
            # Rate limit của Google Cloud TTS rất rộng, chỉ cần sleep 1 giây để tránh nghẽn
            time.sleep(1.0)
        
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
    print(f"📊  KẾT QUẢ THU ÂM (GOOGLE CLOUD TTS)")
    print(f"{'='*60}")
    print(f"   Tổng chunks: {total_chunks}")
    print(f"   Thành công:  {success_count}")
    print(f"   Thất bại:    {fail_count}")
    print(f"   Report:      {report_path}")
    
    if fail_count > 0:
        print(f"\n⚠️  Có {fail_count} chunk bị lỗi. Chạy lại script để retry.")
    else:
        print(f"\n🎉  Thu âm hoàn tất! Tất cả file audio đã được lưu tại: {audio_dir}/")
 

if __name__ == "__main__":
    main()
