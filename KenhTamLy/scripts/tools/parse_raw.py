import os
import sys
import time
from playwright.sync_api import sync_playwright

def main():
    abs_path = os.path.abspath("ai_response_raw.html")
    file_url = f"file://{abs_path}"
    print(f"Loading local HTML file: {file_url}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(file_url)
        
        # Run JS to find 'Tuổi trẻ' elements
        js_inspect = """
        () => {
            const results = [];
            const containers = document.querySelectorAll('div.Zkbeff, div.mZJni');
            containers.forEach((container, cIdx) => {
                const elements = [];
                container.querySelectorAll('*').forEach(el => {
                    const txt = (el.innerText || '').trim();
                    if (txt === 'Tuổi trẻ' || txt === 'Báo Tuổi Trẻ') {
                        elements.push({
                            tag: el.tagName.toLowerCase(),
                            className: el.className,
                            parentTag: el.parentElement ? el.parentElement.tagName.toLowerCase() : '',
                            parentClass: el.parentElement ? el.parentElement.className : ''
                        });
                    }
                });
                results.push({ containerIndex: cIdx, elements });
            });
            return results;
        }
        """
        data = page.evaluate(js_inspect)
        for item in data:
            print(f"Container {item['containerIndex']} elements with 'Tuổi trẻ':")
            for el in item['elements']:
                print(f"  <{el['tag']} class='{el['className']}'> inside <{el['parentTag']} class='{el['parentClass']}'>")
            
        browser.close()

if __name__ == "__main__":
    main()
