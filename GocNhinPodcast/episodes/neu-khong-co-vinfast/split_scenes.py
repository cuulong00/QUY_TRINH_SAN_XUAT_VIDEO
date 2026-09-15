import os
import re

def split_into_scenes(text, max_words=26):
    # Split by sentence boundaries (. ? !)
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    scenes = []
    
    for sentence in sentences:
        if not sentence.strip():
            continue
        words = sentence.split()
        if len(words) <= max_words:
            scenes.append(sentence)
        else:
            # If a single sentence is > 26 words, we must split it into chunks
            # We'll split by comma if possible, or just split evenly
            chunks = []
            parts = re.split(r'(?<=[,;])\s+', sentence)
            current_chunk = []
            for part in parts:
                part_words = part.split()
                if len(current_chunk) + len(part_words) <= max_words:
                    current_chunk.extend(part_words)
                else:
                    if current_chunk:
                        chunks.append(" ".join(current_chunk))
                    current_chunk = part_words
            if current_chunk:
                chunks.append(" ".join(current_chunk))
            
            # If any chunk is still > 26 words, just split it mathematically
            final_chunks = []
            for chunk in chunks:
                chunk_words = chunk.split()
                if len(chunk_words) > max_words:
                    k = (len(chunk_words) + max_words - 1) // max_words
                    chunk_size = (len(chunk_words) + k - 1) // k
                    for i in range(k):
                        final_chunks.append(" ".join(chunk_words[i*chunk_size:(i+1)*chunk_size]))
                else:
                    final_chunks.append(chunk)
            
            scenes.extend(final_chunks)
            
    return scenes

for ch in range(1, 10):
    filename = f"/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/neu-khong-co-vinfast/chapter_0{ch}.md"
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            # remove headers like # chapter_xx.md
            text = re.sub(r'#.*?\n', '', text)
            scenes = split_into_scenes(text)
            print(f"--- CHAPTER {ch:02d} ---")
            for i, scene in enumerate(scenes):
                print(f"SC{i+1:03d} ({len(scene.split())} words): {scene}")
