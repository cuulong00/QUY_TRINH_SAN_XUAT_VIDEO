import os
from playwright.sync_api import sync_playwright
from PIL import Image

def render_logos():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 2000, "height": 600})
        
        # 1. Anthropic
        with open("scratch/anthropic_logo.svg", "r", encoding="utf-8") as f:
            svg_an = f.read()
        # Force all fills to white
        svg_an_white = svg_an.replace("#1f1f1e", "#FFFFFF")
        html_an = f"""
        <!DOCTYPE html>
        <html><body style="margin:0; padding:40px; background:transparent;">
        <div id="an" style="display:inline-block; width:1024px; height:115px;">
            {svg_an_white}
        </div>
        </body></html>
        """
        page.set_content(html_an)
        page.locator("#an").screenshot(path="scratch/anthropic_clean_white.png", omit_background=True)
        print("Rendered Anthropic clean white!")

        # 2. OpenAI
        # Let's render OpenAI swirl + text in crisp white
        with open("scratch/openai_logo.svg", "r", encoding="utf-8") as f:
            svg_oa = f.read()
        # Invert black to white with CSS filter
        html_oa = f"""
        <!DOCTYPE html>
        <html><body style="margin:0; padding:40px; background:transparent;">
        <div id="oa" style="display:inline-block; transform: scale(4); transform-origin: top left; filter: invert(1) brightness(2);">
            {svg_oa}
        </div>
        </body></html>
        """
        page.set_content(html_oa)
        page.locator("#oa").screenshot(path="scratch/openai_clean_white.png", omit_background=True)
        print("Rendered OpenAI clean white!")

        browser.close()

if __name__ == "__main__":
    render_logos()
