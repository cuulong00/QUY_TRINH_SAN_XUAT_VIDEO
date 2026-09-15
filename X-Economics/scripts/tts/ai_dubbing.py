#!/usr/bin/env python3
"""
GocNhinPodcast AI Dubbing Engine
Version: 1.0.0
Description: Tự động hóa quy trình lồng tiếng (AI Dubbing) chất lượng cao cho video.
Sử dụng mốc thời gian chuẩn từ phụ đề SRT, tích hợp bộ dọn dẹp phụ đề cuộn (rolling caption),
giọng đọc cao cấp Google Chirp3-HD (Generative AI) và thuật toán đồng bộ tốc độ một chiều.
"""

import os
import sys
import re
import json
import time
import shutil
import asyncio
import argparse
import subprocess
import base64
import urllib.request
from pydub import AudioSegment

# API Key mặc định (có thể được nạp từ env)
DEFAULT_API_KEY = "AIzaSyCKA0rR2E9swQoF0DEN6YTOYSiNmbprWdY"
API_KEY = os.environ.get("GOOGLE_API_KEY", os.environ.get("GEMINI_API_KEY", DEFAULT_API_KEY))

# Ngưỡng an toàn chống vượt hạn mức Google Cloud TTS miễn phí (950k ký tự/tháng)
SAFE_LIMIT = 950000

# ============================================================
# UTILS & SUBPROCESS COMMANDS
# ============================================================

def run_command(cmd, desc="Running command"):
    print(f"⏳ {desc}...")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"❌ Lỗi: {result.stderr}")
        raise RuntimeError(result.stderr)
    return result.stdout

# ============================================================
# BƯỚC 1: PARSE PHỤ ĐỀ SRT & TÁI THIẾT LẬP CÂU (ROLLING CAPTION CLEANER)
# ============================================================

def parse_time(time_str):
    time_str = time_str.replace(',', '.')
    parts = time_str.split(':')
    sec_parts = parts[-1].split('.')
    sec = float(sec_parts[0]) + float(sec_parts[1]) / 1000.0
    if len(parts) == 3:
        sec += int(parts[0]) * 3600 + int(parts[1]) * 60
    elif len(parts) == 2:
        sec += int(parts[0]) * 60
    return sec

def clean_text_line(text):
    text = text.replace('\n', ' ').strip()
    text = re.sub(r'^>>\s*', '', text)
    text = re.sub(r'<<\s*', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def parse_and_reconstruct_srt(srt_path, start_limit=0.0, end_limit=300.0):
    if not os.path.exists(srt_path):
        raise FileNotFoundError(f"Không tìm thấy file phụ đề SRT tại: {srt_path}")
        
    with open(srt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex nhận dạng các khối SRT
    pattern = re.compile(
        r'(\d+)\n(\d{2}:\d{2}:\d{2}[,\.]\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}[,\.]\d{3})\n(.*?)(?=\n\n|\Z)',
        re.DOTALL
    )
    matches = pattern.findall(content)

    raw_entries = []
    for num, start_str, end_str, text in matches:
        start_sec = parse_time(start_str)
        end_sec = parse_time(end_str)
        clean_text = clean_text_line(text)
        if clean_text and not clean_text.startswith('[') and clean_text.strip() != "":
            raw_entries.append({
                "start": start_sec,
                "end": end_sec,
                "text": clean_text
            })

    # Thuật toán Word-level overlap để dọn dẹp rolling caption
    timed_words = []
    for entry in raw_entries:
        words = entry["text"].split()
        if not words:
            continue
        
        max_check = min(len(timed_words), len(words))
        best_overlap = 0
        for i in range(1, max_check + 1):
            prev_slice = [tw["word"] for tw in timed_words[-i:]]
            curr_slice = words[:i]
            
            prev_clean = [re.sub(r'[^\w]', '', w.lower()) for w in prev_slice]
            curr_clean = [re.sub(r'[^\w]', '', w.lower()) for w in curr_slice]
            
            if prev_clean == curr_clean:
                best_overlap = i
                
        new_words = words[best_overlap:]
        for w in new_words:
            timed_words.append({
                "word": w,
                "time": entry["start"],
                "end_time_estimate": entry["end"]
            })

    # Gom nhóm các từ thành câu
    raw_sentences = []
    current_sentence_words = []

    for idx, tw in enumerate(timed_words):
        current_sentence_words.append(tw)
        word = tw["word"]
        
        is_sentence_end = word[-1] in ('.', '?', '!') or (
            (word.endswith('"') or word.endswith("'")) and len(word) > 1 and word[-2] in ('.', '?', '!')
        )
        
        is_time_gap = False
        if idx < len(timed_words) - 1:
            next_tw = timed_words[idx + 1]
            if next_tw["time"] - tw["time"] > 2.0:
                is_time_gap = True
                
        if is_sentence_end or is_time_gap or len(current_sentence_words) >= 25:
            text = " ".join([w["word"] for w in current_sentence_words])
            start_time = current_sentence_words[0]["time"]
            end_time = current_sentence_words[-1]["end_time_estimate"]
            
            if idx < len(timed_words) - 1:
                next_start = timed_words[idx + 1]["time"]
                if next_start > start_time:
                    end_time = min(end_time, next_start)
                    
            raw_sentences.append({
                "start": start_time,
                "end": end_time,
                "text": text
            })
            current_sentence_words = []

    if current_sentence_words:
        text = " ".join([w["word"] for w in current_sentence_words])
        start_time = current_sentence_words[0]["time"]
        end_time = current_sentence_words[-1]["end_time_estimate"]
        raw_sentences.append({
            "start": start_time,
            "end": end_time,
            "text": text
        })

    # Ghép các câu siêu ngắn ở gần nhau
    merged_sentences = []
    for s in raw_sentences:
        # Lọc theo khung start/end limit
        if s["start"] < start_limit or s["start"] > end_limit:
            continue
        s["end"] = min(s["end"], end_limit)
        
        if not merged_sentences:
            merged_sentences.append(s)
            continue
            
        prev = merged_sentences[-1]
        prev_len = len(prev["text"].split())
        curr_len = len(s["text"].split())
        gap = s["start"] - prev["end"]
        combined_duration = s["end"] - prev["start"]
        
        if combined_duration < 15.0 and gap < 1.5 and (prev_len < 6 or curr_len < 4 or gap < 0.5):
            prev["text"] += " " + s["text"]
            prev["end"] = s["end"]
        else:
            merged_sentences.append(s)

    # Đảm bảo các phân đoạn hoàn toàn không chồng lấn (Strict Non-Overlapping)
    for i in range(len(merged_sentences) - 1):
        if merged_sentences[i]["end"] > merged_sentences[i+1]["start"]:
            merged_sentences[i]["end"] = merged_sentences[i+1]["start"]
            
    for s in merged_sentences:
        s["duration_sec"] = round(s["end"] - s["start"], 2)

    return merged_sentences

# ============================================================
# BƯỚC 2: QUẢN LÝ DỊCH THUẬT (TRANSLATION CACHE & FALLBACK)
# ============================================================

def try_gemini_translation(english_segments):
    """
    Thử dịch thuật ngữ cảnh qua Gemini API.
    Nếu API Key bị chặn/lỗi, trả về None để gọi luồng biên tập thủ công.
    """
    from google import genai
    from google.genai import types
    
    try:
        client = genai.Client(api_key=API_KEY)
        prompt = f"""
        Bạn là biên dịch viên kịch bản tài chính - kinh tế của kênh GocNhinPodcast.
        Dịch toàn bộ trường 'text_en' sang tiếng Việt và lưu vào trường 'text_vi'.
        Bản dịch phải súc tích để đọc lên không vượt quá 'duration_sec'. Không dùng dấu nháy kép (").
        Giữ nguyên cấu trúc JSON.
        JSON đầu vào:
        {json.dumps({"segments": english_segments}, ensure_ascii=False)}
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"⚠️ Dịch thuật tự động qua Gemini thất bại (Có thể do API Key bị giới hạn): {e}")
        return None

def manage_translation(segments, draft_json_path):
    """
    Xử lý bản dịch. Nếu đã có file nháp đã dịch, nạp lại.
    Nếu chưa, thử dịch tự động, nếu lỗi thì lưu nháp trống và yêu cầu điền tay.
    """
    if os.path.exists(draft_json_path):
        print(f"📖 Tìm thấy file dịch nháp hiện có tại: {draft_json_path}")
        with open(draft_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Kiểm tra xem đã dịch chưa
            all_translated = all("text_vi" in s and s["text_vi"].strip() != "" for s in data.get("segments", []))
            if all_translated:
                print("✅ Bản dịch đã đầy đủ. Sẵn sàng tổng hợp giọng nói.")
                return data
            else:
                print("⚠️ Bản dịch nháp chưa được dịch hoàn chỉnh hoặc chứa dòng trống.")
                print(f"👉 Vui lòng mở file và điền bản dịch tiếng Việt vào trường 'text_vi' rồi chạy lại script.")
                sys.exit(0)

    # Chuyển đổi định dạng cho dịch thuật
    draft_segments = []
    for idx, s in enumerate(segments):
        draft_segments.append({
            "id": idx + 1,
            "start_time": s["start"],
            "end_time": s["end"],
            "duration_sec": s["duration_sec"],
            "text_en": s["text"],
            "text_vi": ""
        })

    print("🤖 Đang thử dịch thuật ngữ cảnh tự động qua Gemini API...")
    auto_data = try_gemini_translation(draft_segments)
    if auto_data and "segments" in auto_data:
        print("✅ Dịch tự động hoàn tất thành công.")
        with open(draft_json_path, 'w', encoding='utf-8') as f:
            json.dump(auto_data, f, ensure_ascii=False, indent=2)
        return auto_data
    else:
        # Ghi file nháp trống để người dùng tự dịch
        print("📝 Đang tạo tệp nháp dịch thuật cục bộ...")
        with open(draft_json_path, 'w', encoding='utf-8') as f:
            json.dump({"segments": draft_segments}, f, ensure_ascii=False, indent=2)
        print(f"\n🛑 ĐÃ TẠO TỆP DỊCH THUẬT NHÁP TẠI: {draft_json_path}")
        print(f"👉 Hãy mở tệp này ra và điền lời thoại dịch tiếng Việt vào trường 'text_vi' của các câu.")
        print(f"👉 Sau khi dịch xong, hãy chạy lại lệnh này để hoàn thành lồng tiếng.")
        sys.exit(0)

# ============================================================
# BƯỚC 3: KIỂM SOÁT QUOTA AN TOÀN & GOOGLE CLOUD TTS SYNTHESIS
# ============================================================

def check_and_update_quota(text_list, usage_file_path):
    current_month = time.strftime("%Y-%m")
    total_chars_in_run = sum(len(text) for text in text_list)
    
    usage_data = {"month": current_month, "accumulated_chars": 0}
    if os.path.exists(usage_file_path):
        try:
            with open(usage_file_path, "r") as f:
                data = json.load(f)
                if data.get("month") == current_month:
                    usage_data = data
        except:
            pass
            
    projected_usage = usage_data["accumulated_chars"] + total_chars_in_run
    
    if projected_usage > SAFE_LIMIT:
        print(f"\n⚠️ CẢNH BÁO HẠN MỨC QUOTA GOOGLE CLOUD TTS ({projected_usage:,} / {SAFE_LIMIT:,} ký tự)")
        print(f"👉 Đã dùng trong tháng: {usage_data['accumulated_chars']:,} ký tự.")
        print(f"👉 Lượt chạy này cần: {total_chars_in_run:,} ký tự.")
        print(f"👉 Tự động chuyển sang sử dụng Edge TTS miễn phí để bảo toàn chi phí.")
        return False
        
    usage_data["accumulated_chars"] = projected_usage
    with open(usage_file_path, "w") as f:
        json.dump(usage_data, f)
        
    print(f"📊 [Google TTS Quota] Tháng này đã tích lũy: {projected_usage:,} / {SAFE_LIMIT:,} ký tự miễn phí.")
    return True

async def synthesize_single_google(text, output_path, voice_name, semaphore):
    async with semaphore:
        url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"
        data = {
            "input": {"text": text},
            "voice": {
                "languageCode": "vi-VN",
                "name": voice_name
            },
            "audioConfig": {
                "audioEncoding": "MP3"
            }
        }
        
        for attempt in range(3):
            try:
                if os.path.exists(output_path):
                    try: os.remove(output_path)
                    except: pass
                
                def do_post():
                    req = urllib.request.Request(
                        url,
                        data=json.dumps(data).encode("utf-8"),
                        headers={"Content-Type": "application/json"}
                    )
                    with urllib.request.urlopen(req, timeout=20.0) as response:
                        return json.loads(response.read().decode("utf-8"))
                        
                res_data = await asyncio.to_thread(do_post)
                audio_data = base64.b64decode(res_data["audioContent"])
                with open(output_path, "wb") as f:
                    f.write(audio_data)
                
                if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                    return True
            except Exception as e:
                print(f"  ⚠️ Thử lần {attempt+1} Google TTS thất bại cho dòng: {text[:20]}... Lỗi: {e}")
                await asyncio.sleep(1.5 * (attempt + 1))
        return False

async def synthesize_single_edge(text, output_path, voice_name, semaphore):
    async with semaphore:
        # Edge TTS free fallback
        import edge_tts
        for attempt in range(4):
            try:
                if os.path.exists(output_path):
                    try: os.remove(output_path)
                    except: pass
                communicate = edge_tts.Communicate(text, voice=voice_name)
                await asyncio.wait_for(communicate.save(output_path), timeout=25.0)
                if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                    return True
            except Exception as e:
                print(f"  ⚠️ Thử lần {attempt+1} Edge TTS thất bại: {e}")
                await asyncio.sleep(2.0 * (attempt + 1))
        return False

async def generate_voiceover_async(translated_data, output_dir, use_google, google_voice, usage_file_path):
    segments = translated_data.get("segments", [])
    os.makedirs(output_dir, exist_ok=True)
    
    # Chuẩn bị dọn dẹp văn bản đặc biệt
    text_list = []
    for s in segments:
        text_vi = s["text_vi"]
        text_clean = text_vi.replace("&", "và").replace("<", "").replace(">", "").replace('"', "").replace("'", "")
        text_list.append(text_clean)
        
    is_google_allowed = False
    if use_google:
        is_google_allowed = check_and_update_quota(text_list, usage_file_path)

    semaphore = asyncio.Semaphore(10 if is_google_allowed else 4)
    tasks = []
    
    if is_google_allowed:
        print(f"🎙️ Bắt đầu gọi hàng đợi Google Cloud TTS API ({google_voice})...")
        for idx, text in enumerate(text_list):
            out_file = os.path.join(output_dir, f"chunk_{idx+1:03d}.mp3")
            tasks.append(synthesize_single_google(text, out_file, google_voice, semaphore))
    else:
        # Dùng Edge TTS Free
        print(f"🎙️ Bắt đầu gọi hàng đợi Microsoft Edge TTS (vi-VN-NamMinhNeural - MIỄN PHÍ)...")
        edge_voice = "vi-VN-NamMinhNeural"
        for idx, text in enumerate(text_list):
            out_file = os.path.join(output_dir, f"chunk_{idx+1:03d}.mp3")
            tasks.append(synthesize_single_edge(text, out_file, edge_voice, semaphore))

    await asyncio.gather(*tasks)
    
    # Kiểm tra và sửa lỗi các tệp hỏng (Healing Loop)
    for idx, s in enumerate(segments):
        chunk_file = os.path.join(output_dir, f"chunk_{idx+1:03d}.mp3")
        if not os.path.exists(chunk_file) or os.path.getsize(chunk_file) == 0:
            print(f"⚠️ Segment {idx+1} bị rỗng hoặc lỗi. Đang khởi tạo tệp silent fallback.")
            if os.path.exists(chunk_file):
                try: os.remove(chunk_file)
                except: pass
            duration_ms = int(s["duration_sec"] * 1000)
            silent = AudioSegment.silent(duration=duration_ms, frame_rate=24000)
            silent.export(chunk_file, format="mp3")

# ============================================================
# BƯỚC 4: ALIGNMENT & TIME-STRETCHING MỘT CHIỀU & GHÉP NỐI
# ============================================================

def align_and_assemble(translated_data, chunk_dir, output_audio_path, duration_limit_sec):
    print("⏳ Đồng bộ và co giãn thời gian (Selective Speed-up)...")
    final_audio = AudioSegment.silent(duration=duration_limit_sec * 1000, frame_rate=24000)
    
    for segment in translated_data.get("segments", []):
        seg_id = segment["id"]
        start_ms = int(segment["start_time"] * 1000)
        duration_target = segment["duration_sec"]
        
        chunk_file = os.path.join(chunk_dir, f"chunk_{seg_id:03d}.mp3")
        aligned_chunk_file = os.path.join(chunk_dir, f"chunk_{seg_id:03d}_aligned.wav")
        
        if not os.path.exists(chunk_file):
            continue
            
        audio_chunk = AudioSegment.from_file(chunk_file, format="mp3")
        duration_actual = len(audio_chunk) / 1000.0
        
        ratio = duration_actual / duration_target
        print(f"  Câu {seg_id}: Target={duration_target:.2f}s, Actual={duration_actual:.2f}s -> Tỷ lệ={ratio:.2f}")
        
        # Chỉ tăng tốc khi câu thuyết minh tiếng Việt dài hơn thời gian cho phép (Ratio > 1.10)
        if ratio > 1.10:
            speed = min(ratio, 1.35)  # Cap tối đa 1.35x tránh bị méo tiếng quá nặng
            cmd_stretch = [
                "ffmpeg", "-y", "-i", chunk_file,
                "-filter:a", f"atempo={speed}",
                aligned_chunk_file
            ]
            subprocess.run(cmd_stretch, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            # Dư thời gian hoặc xấp xỉ khớp -> Giữ nguyên 1.0x, tự động để khoảng lặng
            aligned_chunk_file = chunk_file
            
        aligned_chunk = AudioSegment.from_file(aligned_chunk_file)
        final_audio = final_audio.overlay(aligned_chunk, position=start_ms)
        
    final_audio.export(output_audio_path, format="wav")
    print(f"🎉 Lưu âm thanh lồng tiếng hoàn thiện: {output_audio_path}")

# ============================================================
# BƯỚC 5: GHÉP AUDIO VÀO VIDEO
# ============================================================

def merge_audio_video(video_in, audio_in, video_out):
    print("🎬 Đang tiến hành ghép audio tiếng Việt mới vào video gốc...")
    cmd_merge = [
        "ffmpeg", "-y",
        "-i", video_in,
        "-i", audio_in,
        "-c:v", "copy",     # Sao chép trực tiếp luồng hình không nén lại
        "-c:a", "aac",      # Nén luồng tiếng sang định dạng AAC chuẩn
        "-map", "0:v:0",
        "-map", "1:a:0",
        video_out
    ]
    run_command(cmd_merge, "Ghép Audio lồng tiếng vào Video")
    print(f"🚀 Thành phẩm lồng tiếng thành công! File xuất ra: {video_out}")

# ============================================================
# ORCHESTRATOR
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="GocNhinPodcast Dubbing Pipeline CLI")
    parser.add_argument("--slug", required=True, help="Slug của episode, e.g. e01_macro_war")
    parser.add_argument("--srt-path", required=True, help="Đường dẫn file phụ đề tiếng Anh SRT")
    parser.add_argument("--video-in", required=True, help="Đường dẫn file video gốc đầu vào")
    parser.add_argument("--voice", default="vi-VN-Chirp3-HD-Alnilam", help="Tên giọng nam Google Cloud TTS")
    parser.add_argument("--start", type=float, default=0.0, help="Thời điểm bắt đầu (giây)")
    parser.add_argument("--end", type=float, default=300.0, help="Thời điểm kết thúc (giây)")
    parser.add_argument("--use-edge", action="store_true", help="Bắt buộc dùng Edge TTS miễn phí")
    
    args = parser.parse_args()
    
    # Định vị các thư mục đầu ra trong cấu trúc tập phim
    episode_dir = os.path.dirname(args.srt_path) if "/" in args.srt_path else "."
    
    draft_json_path = os.path.join(episode_dir, "dubbing_draft.json")
    chunk_dir = os.path.join(episode_dir, "dubbing_chunks")
    output_audio = os.path.join(episode_dir, "dubbed_audio.wav")
    output_video = os.path.join(episode_dir, "dubbed_video_final.mp4")
    usage_file_path = os.path.expanduser("~/.gemini/antigravity/brain/google_tts_usage.json")
    os.makedirs(os.path.dirname(usage_file_path), exist_ok=True)
    
    if os.path.exists(chunk_dir):
        shutil.rmtree(chunk_dir)
    os.makedirs(chunk_dir, exist_ok=True)
    
    print("\n[Bước 1] Phân tích phụ đề và dọn dẹp rolling captions...")
    raw_segments = parse_and_reconstruct_srt(args.srt_path, args.start, args.end)
    
    print("\n[Bước 2] Dịch thuật và quản lý bản dịch nháp...")
    translated_data = manage_translation(raw_segments, draft_json_path)
    
    print("\n[Bước 3] Đang gọi tổng hợp giọng nói tiếng Việt...")
    use_google = not args.use_edge
    asyncio.run(
        generate_voiceover_async(
            translated_data, chunk_dir, use_google, args.voice, usage_file_path
        )
    )
    
    print("\n[Bước 4] Đồng bộ thời gian và ráp nối âm thanh...")
    duration_limit = int(args.end - args.start)
    align_and_assemble(translated_data, chunk_dir, output_audio, duration_limit)
    
    print("\n[Bước 5] Ghép luồng âm thanh mới vào video...")
    merge_audio_video(args.video_in, output_audio, output_video)
    
    print("\n✨ PIPELINE DUBBING HOÀN TẤT THÀNH CÔNG! ✨")

if __name__ == "__main__":
    main()
