import os
import sys
import time
from playwright.sync_api import sync_playwright

def main():
    print("Launching browser to inspect Google Search AI Mode response DOM...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            locale="vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
        )
        page = context.new_page()
        page.add_init_script("delete navigator.__proto__.webdriver")
        
        # Navigate to a query that will trigger AI Overview
        url = "https://www.google.com/search?q=Einstein+nói+gì+về+Phật+giáo&udm=50"
        print(f"Navigating to: {url}")
        page.goto(url)
        
        # Wait 10 seconds for AI Overview to generate completely
        print("Waiting for generation...")
        time.sleep(10)
        
        # Save page source for deeper inspection if needed
        html = page.content()
        with open("ai_response_raw.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved raw HTML to ai_response_raw.html")
        
        # Analyze the container using JS
        js_analyze = """
        () => {
            const containers = document.querySelectorAll('div.Zkbeff, div.mZJni, div[class*="sge"]');
            const results = [];
            for (let i = 0; i < containers.length; i++) {
                const el = containers[i];
                // Clone the container to avoid mutating the live page
                const clone = el.cloneNode(true);
                
                // Let's list some child tags and classes inside this container
                const childrenInfo = [];
                clone.querySelectorAll('*').forEach(child => {
                    if (child.className) {
                        childrenInfo.push({
                            tag: child.tagName.toLowerCase(),
                            class: child.className,
                            textSnippet: (child.innerText || '').substring(0, 50).trim()
                        });
                    }
                });
                
                results.push({
                    index: i,
                    class: el.className,
                    htmlSnippet: el.outerHTML.substring(0, 1000),
                    childrenCount: clone.querySelectorAll('*').length,
                    childrenInfo: childrenInfo.slice(0, 30) // first 30 children
                });
            }
            return results;
        }
        """
        data = page.evaluate(js_analyze)
        print(f"\nFound {len(data)} AI containers.")
        for item in data:
            print(f"\n--- Container {item['index']} ---")
            print(f"Class: {item['class']}")
            print(f"Total children: {item['childrenCount']}")
            print("First 30 children info (tag, class, snippet):")
            for c in item['childrenInfo']:
                if c['textSnippet']:
                    print(f"  - <{c['tag']} class='{c['class']}'>: {c['textSnippet']}")
        
        browser.close()

if __name__ == "__main__":
    main()
