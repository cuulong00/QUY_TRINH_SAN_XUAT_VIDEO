#!/usr/bin/env python3
import os
import sys
import re

def check_sentences(file_path, max_len=150):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split sentences by .?! followed by space, or followed by quote then space, or newlines
    sentences = re.split(r'(?<=[.?!])\s+|(?<=[.?!]["\'])\s+|\n+', content)
    
    long_sentences = []
    for s in sentences:
        s_clean = s.strip()
        # Remove markdown headers and comments if they are not spoken
        if s_clean.startswith("#") or (s_clean.startswith("<!--") and s_clean.endswith("-->")):
            continue
        if not s_clean:
            continue
        if len(s_clean) > max_len:
            long_sentences.append(s_clean)
            
    return long_sentences

def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = os.getcwd()
        
    print(f"Checking sentence lengths (Max: 150 chars) in: {target}\n")
    
    files_to_check = []
    if os.path.isdir(target):
        # Scan for chapter files and final_voiceover
        for file_name in sorted(os.listdir(target)):
            if (file_name.startswith("chapter_") and file_name.endswith(".md")) or file_name == "final_voiceover.md":
                files_to_check.append(os.path.join(target, file_name))
    elif os.path.isfile(target):
        files_to_check.append(target)
        
    if not files_to_check:
        print("No chapter markdown files or final_voiceover.md found.")
        sys.exit(0)
        
    total_violations = 0
    for file_path in files_to_check:
        file_name = os.path.basename(file_path)
        long_sents = check_sentences(file_path)
        if long_sents:
            total_violations += len(long_sents)
            print(f"=== {file_name} has {len(long_sents)} sentences exceeding limit ===")
            for s in long_sents:
                print(f"- ({len(s)} chars): {s}\n")
        else:
            print(f"✓ {file_name} is clean (all sentences <= 150 chars).")
            
    if total_violations > 0:
        print(f"\nAudit FAILED: Found {total_violations} long sentence(s) in total.")
        sys.exit(1)
    else:
        print("\nAudit PASSED: All sentences are under 150 characters.")
        sys.exit(0)

if __name__ == "__main__":
    main()
