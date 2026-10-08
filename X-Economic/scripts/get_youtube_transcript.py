import time
import re
from playwright.sync_api import sync_playwright

def main():
    video_url = "https://www.youtube.com/watch?v=gYcsD5hOzjg"
    out_file = "episodes/cuoc-chien-phan-cuc-ai/research_vault/transcript_gYcsD5hOzjg.txt"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        print(f"Loading {video_url}...")
        page.goto(video_url, wait_until="networkidle")
        time.sleep(3)
        
        # Expand description
        page.evaluate("""() => {
            const moreBtn = document.querySelector('#expand, #description #expand, tp-yt-paper-button#expand');
            if (moreBtn) moreBtn.click();
        }""")
        time.sleep(1)
        
        # Click transcript button
        page.evaluate("""() => {
            const btns = Array.from(document.querySelectorAll('button, ytd-button-renderer'));
            const transcriptBtn = btns.find(b => b.innerText && b.innerText.includes('Show transcript'));
            if (transcriptBtn) {
                transcriptBtn.scrollIntoView();
                transcriptBtn.click();
                const innerBtn = transcriptBtn.querySelector('button');
                if (innerBtn) innerBtn.click();
            }
        }""")
        time.sleep(4)
        
        # Find all elements that look like timestamps (e.g., "0:00", "12:34")
        # In YouTube's modern UI, each segment has a timestamp and a text block.
        # Let's extract the transcript using a generic DOM traversal from the panel containing "Search transcript"
        result = page.evaluate("""() => {
            // Find the container with header 'Transcript'
            const allElements = Array.from(document.querySelectorAll('*'));
            const header = allElements.find(el => el.children.length === 0 && el.innerText && el.innerText.trim() === 'Transcript');
            if (!header) return { error: 'Transcript header not found' };
            
            // Find panel ancestor
            let panel = header.parentElement;
            while (panel && panel.querySelectorAll('input').length === 0 && panel !== document.body) {
                panel = panel.parentElement;
            }
            // panel now has Search transcript input
            // Let's get parent of panel or the list container
            const container = panel.parentElement || panel;
            
            // Collect all elements with formatted text
            // Look for timestamp elements matching /^\d+:\d{2}/
            const textNodes = Array.from(container.querySelectorAll('*'))
                .filter(el => el.children.length === 0 && el.innerText && el.innerText.trim().length > 0);
                
            return {
                panelFound: true,
                totalTextNodes: textNodes.length,
                rawTexts: textNodes.slice(0, 100).map(el => el.innerText.trim()),
                entireText: container.innerText
            };
        }""")
        
        if "entireText" in result:
            entire_text = result["entireText"]
            print(f"Captured panel text! Length: {len(entire_text)} chars")
            
            # The entireText starts with "Transcript\n...\n0:00\nText\n0:09\nText..."
            # Let's parse it!
            lines = entire_text.split("\n")
            print(f"Total lines in panel text: {len(lines)}")
            print("First 30 lines:\n", "\n".join(lines[:30]))
            
            # Save raw panel text
            with open("episodes/cuoc-chien-phan-cuc-ai/research_vault/transcript_gYcsD5hOzjg_raw.txt", "w", encoding="utf-8") as f:
                f.write(entire_text)
                
            # Parse into clean format [MM:SS] Text
            parsed_segments = []
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                # Check if line matches timestamp pattern like 0:00, 1:23, 12:34, 1:02:34
                if re.match(r"^\d+:\d{2}(:\d{2})?$", line):
                    timestamp = line
                    # Text usually follows on the next line or lines
                    text_parts = []
                    i += 1
                    while i < len(lines) and not re.match(r"^\d+:\d{2}(:\d{2})?$", lines[i].strip()):
                        txt = lines[i].strip()
                        if txt and txt != "Search transcript" and txt != "Transcript":
                            text_parts.append(txt)
                        i += 1
                    parsed_segments.append(f"[{timestamp}] {' '.join(text_parts)}")
                else:
                    i += 1
                    
            print(f"\nParsed {len(parsed_segments)} structured segments!")
            if parsed_segments:
                with open(out_file, "w", encoding="utf-8") as f:
                    f.write("\n".join(parsed_segments))
                print(f"Saved structured transcript to {out_file}!")
                print("\nFirst 15 structured lines:\n" + "\n".join(parsed_segments[:15]))
                print("\nLast 10 structured lines:\n" + "\n".join(parsed_segments[-10:]))
            else:
                # If parsing regex did not catch, save entire text directly
                with open(out_file, "w", encoding="utf-8") as f:
                    f.write(entire_text)
                print(f"Saved full raw text to {out_file}!")
        else:
            print("Error finding panel:", result)
            
        browser.close()

if __name__ == "__main__":
    main()
