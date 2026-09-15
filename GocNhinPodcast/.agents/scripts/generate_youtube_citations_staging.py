import os
import re
from difflib import SequenceMatcher

EPISODES_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes"
AUDIT_FILE = os.path.join(EPISODES_DIR, "youtube_ymyl_audit_report.md")
STAGING_FILE = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/youtube_citations_staging.md"

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_audit_videos():
    videos = []
    with open(AUDIT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for line in content.split('\n'):
        if '| **' in line and 'youtube.com' in line:
            parts = line.split('|')
            vid = parts[2].strip().replace('`', '').strip()
            title_part = parts[3].strip()
            match = re.search(r'\[(.*?)\]', title_part)
            if match:
                title = match.group(1)
                videos.append({'id': vid, 'title': title})
    return videos

def find_all_episodes():
    episodes = []
    for entry in os.scandir(EPISODES_DIR):
        if entry.is_dir() and not entry.name.startswith('.'):
            # Try to read 09_youtube_metadata.md for title
            yt_meta_path = os.path.join(entry.path, '09_youtube_metadata.md')
            title = entry.name
            if os.path.exists(yt_meta_path):
                with open(yt_meta_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith('# YouTube Metadata'):
                            title = line.replace('# YouTube Metadata —', '').strip()
                            break
                        if line.startswith('1. **'):
                            title = line.replace('1. **', '').replace('**', '').strip()
                            break
                            
            # Check for sources in 02_research_map.md
            map_path = os.path.join(entry.path, '02_research_map.md')
            syn_path = os.path.join(entry.path, '02_research_synthesis.md')
            sources = []
            
            source_file = None
            if os.path.exists(map_path):
                source_file = map_path
            elif os.path.exists(syn_path):
                source_file = syn_path
                
            if source_file:
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find section "Nguồn" or "Tài liệu"
                    match = re.search(r'(#{2,3}\s*(?:\d+\.\s*)?(?:Nguồn|Tài liệu).*?)(?=#{2,3}|\Z)', content, re.DOTALL | re.IGNORECASE)
                    if match:
                        section = match.group(1)
                        for line in section.split('\n'):
                            line = line.strip()
                            # Match list items like "1. ", "- ", etc.
                            if re.match(r'^(\d+\.|-|\*)\s+', line):
                                text = re.sub(r'^(\d+\.|-|\*)\s+', '', line).strip()
                                # Reputability Filter: exclude weak social media
                                lower_text = text.lower()
                                if not any(bad in lower_text for bad in ['facebook', 'voz', 'reddit', 'tiktok', 'blog']):
                                    sources.append(text)
            
            episodes.append({
                'dir': entry.name,
                'title': title,
                'sources': sources
            })
    return episodes

def main():
    print("Extracting videos from audit report...")
    videos = get_audit_videos()
    print(f"Found {len(videos)} videos.")
    
    print("Extracting local episodes and sources...")
    episodes = find_all_episodes()
    print(f"Found {len(episodes)} episodes with/without sources.")
    
    staging_content = "# YMYL Citations Staging File\n\n"
    staging_content += "Vui lòng rà soát danh sách nguồn bên dưới. Bạn có thể xóa hoặc sửa bất kỳ dòng nào. Những video nào bạn KHÔNG muốn cập nhật, hãy xóa toàn bộ phần block của video đó.\n\n"
    
    mapped_count = 0
    for v in videos:
        # Find best match
        best_match = None
        best_score = 0
        for ep in episodes:
            score1 = similar(v['title'].lower(), ep['title'].lower())
            score2 = similar(v['title'].lower(), ep['dir'].lower().replace('-', ' '))
            score = max(score1, score2)
            if score > best_score:
                best_score = score
                best_match = ep
                
        if best_match and best_score > 0.4:
            mapped_count += 1
            staging_content += f"## VIDEO: {v['title']}\n"
            staging_content += f"- **ID**: {v['id']}\n"
            staging_content += f"- **Local Folder**: {best_match['dir']} (Match score: {best_score:.2f})\n"
            staging_content += "- **Citations To Add**:\n"
            if best_match['sources']:
                for s in best_match['sources']:
                    staging_content += f"  - {s}\n"
            else:
                staging_content += "  - (Không tìm thấy nguồn trong tệp research_map)\n"
            staging_content += "\n---\n\n"
        else:
            print(f"WARNING: Could not map video '{v['title']}' to a local folder.")

    with open(STAGING_FILE, 'w', encoding='utf-8') as f:
        f.write(staging_content)
        
    print(f"\nDone! Mapped {mapped_count}/{len(videos)} videos.")
    print(f"Please review the staging file at: {STAGING_FILE}")

if __name__ == '__main__':
    main()
