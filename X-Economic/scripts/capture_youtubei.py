import time
import json
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        
        youtubei_responses = []
        def on_response(response):
            url = response.url
            if "youtubei/v1" in url or "timedtext" in url:
                try:
                    text = response.text()
                    youtubei_responses.append({"url": url, "len": len(text), "text": text})
                except Exception:
                    pass
                    
        page.on("response", on_response)
        print("Navigating...")
        page.goto("https://www.youtube.com/watch?v=gYcsD5hOzjg", wait_until="networkidle")
        time.sleep(2)
        
        # Expand description and click transcript
        page.evaluate("""() => {
            const moreBtn = document.querySelector('#expand, #description #expand, tp-yt-paper-button#expand');
            if (moreBtn) moreBtn.click();
        }""")
        time.sleep(1)
        page.evaluate("""() => {
            const btns = Array.from(document.querySelectorAll('button, ytd-button-renderer'));
            const transcriptBtn = btns.find(b => b.innerText && b.innerText.includes('Show transcript'));
            if (transcriptBtn) transcriptBtn.click();
        }""")
        time.sleep(5)
        
        print(f"Captured {len(youtubei_responses)} responses!")
        found = False
        for i, r in enumerate(youtubei_responses):
            u = r["url"].split("?")[0]
            l = r["len"]
            print(f"[{i}] {u} (len: {l})")
            if "tầm nhìn" in r["text"]:
                print(f"===> MATCH FOUND IN [{i}] {u}!")
                out_json = "episodes/cuoc-chien-phan-cuc-ai/research_vault/transcript_youtubei_matched.json"
                with open(out_json, "w", encoding="utf-8") as f:
                    f.write(r["text"])
                found = True
                
        if not found:
            print("String 'tầm nhìn' not found in captured responses.")
            # Check for English text or any segments
            for i, r in enumerate(youtubei_responses):
                if "transcriptRenderer" in r["text"] or "transcriptSegmentRenderer" in r["text"] or "initialSegments" in r["text"]:
                    print(f"===> Transcript structure found in [{i}] {r['url']}!")
                    with open("episodes/cuoc-chien-phan-cuc-ai/research_vault/transcript_struct.json", "w", encoding="utf-8") as f:
                        f.write(r["text"])
                    found = True
                    break
                    
        browser.close()

if __name__ == "__main__":
    main()
