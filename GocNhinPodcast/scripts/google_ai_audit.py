#!/usr/bin/env python3
import os
import sys
import time
import argparse
import urllib.parse
import subprocess
import platform
import re
from playwright.sync_api import sync_playwright

def copy_to_clipboard(text):
    """
    Copies text to the system clipboard.
    Supports macOS via pbcopy, Windows via clip, and Linux via xclip/xsel.
    """
    system = platform.system()
    try:
        if system == "Darwin":
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            process.communicate(input=text.encode('utf-8'))
            print("ℹ️ Đã sao chép nội dung vào clipboard hệ thống (pbcopy).")
        elif system == "Windows":
            process = subprocess.Popen(['clip'], stdin=subprocess.PIPE, shell=True)
            process.communicate(input=text.encode('utf-8'))
            print("ℹ️ Đã sao chép nội dung vào clipboard hệ thống (clip).")
        else: # Linux and others
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
                print("ℹ️ Đã sao chép nội dung vào clipboard hệ thống (xclip).")
            except FileNotFoundError:
                process = subprocess.Popen(['xsel', '--clipboard', '--input'], stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
                print("ℹ️ Đã sao chép nội dung vào clipboard hệ thống (xsel).")
    except Exception as e:
        print(f"⚠️ Cảnh báo: Không thể sao chép vào clipboard: {e}")

def get_followup_input(page):
    """
    Finds the SGE/AI Overview 'Ask a follow-up' / 'Hỏi thêm' input field.
    Excludes the main search query input (name='q').
    Uses multiple selectors and a JavaScript-based fallback.
    """
    selectors = [
        "textarea[placeholder*='Hỏi thêm']",
        "textarea[placeholder*='Ask a follow-up']",
        "textarea[placeholder*='Hỏi bất cứ điều gì']",
        "textarea[aria-label*='Hỏi thêm']",
        "textarea[aria-label*='Ask a follow-up']",
        "textarea[aria-label*='Hỏi bất cứ điều gì']",
        "div[role='combobox'] textarea",
        "div[class*='sge'] textarea",
        "textarea:not([name='q'])"
    ]
    
    for sel in selectors:
        try:
            el = page.locator(sel)
            if el.count() > 0:
                for idx in range(el.count()):
                    item = el.nth(idx)
                    if item.is_visible() and item.is_enabled():
                        # Exclude main search input just to be safe
                        name = item.get_attribute("name")
                        title = item.get_attribute("title")
                        if name != "q" and title != "Tìm kiếm" and title != "Search":
                            return item
        except Exception:
            continue
            
    # JavaScript fallback to search all visible textareas except name='q'
    try:
        js_find = """() => {
            const textareas = Array.from(document.querySelectorAll('textarea'));
            const target = textareas.find(ta => {
                const name = ta.getAttribute('name');
                const title = ta.getAttribute('title');
                const isSearchInput = name === 'q' || title === 'Search' || title === 'Tìm kiếm';
                const rect = ta.getBoundingClientRect();
                const isVisible = rect.width > 0 && rect.height > 0 && window.getComputedStyle(ta).display !== 'none';
                return !isSearchInput && isVisible;
            });
            return target ? true : false;
        }"""
        if page.evaluate(js_find):
            # If found via JS, let's locate any visible textarea
            el = page.locator("textarea")
            for idx in range(el.count()):
                item = el.nth(idx)
                if item.is_visible():
                    name = item.get_attribute("name")
                    if name != "q":
                        return item
    except Exception:
        pass
        
    return None

def wait_for_ready(page):
    """
    Checks if the SGE input is ready. If blocked by CAPTCHA or Login,
    displays a warning and waits until resolved by the user.
    """
    print("⏳ Đang kiểm tra trạng thái trang và chờ ô nhập liệu SGE 'Hỏi thêm' xuất hiện...")
    last_status = None
    while True:
        input_el = get_followup_input(page)
        if input_el:
            print("✅ Đã phát hiện ô nhập liệu SGE. Bắt đầu phiên làm việc...")
            time.sleep(1) # Give it a second to settle
            return input_el
        
        # Check for CAPTCHA or Traffic warnings
        is_captcha = page.locator("iframe[src*='recaptcha'], #captcha-form, [id*='captcha'], :text('unusual traffic'), :text('lượng truy cập bất thường')").count() > 0
        # Check for Google Sign-in screen (if SGE is blocked due to no login)
        is_login = page.locator(":text('Đăng nhập'), :text('Sign in')").count() > 0 and page.locator("textarea").count() == 0
        
        status = None
        if is_captcha:
            status = "captcha"
            if last_status != status:
                print("\n🚨 CẢNH BÁO: Phát hiện CAPTCHA của Google! Vui lòng tự giải CAPTCHA trực quan trên trình duyệt để tiếp tục.")
        elif is_login:
            status = "login"
            if last_status != status:
                print("\n🚨 CẢNH BÁO: Google yêu cầu đăng nhập tài khoản để sử dụng AI Overview! Vui lòng đăng nhập.")
        else:
            status = "loading"
            if last_status != status:
                print("\n⏳ Ô nhập liệu 'Hỏi thêm' chưa xuất hiện. Có thể AI Overview chưa tải xong hoặc từ khóa tìm kiếm không kích hoạt SGE.")
                print("👉 Hướng dẫn: Đảm bảo tài khoản đã kích hoạt Search Labs/AI Overview, và từ khóa tìm kiếm kích hoạt được AI Overview.")
                
        last_status = status
        time.sleep(3)

def upload_file_and_submit_prompt(page, input_el, file_path, prompt_text, auto=True):
    """
    Uploads a chapter file using the native file input in Google AI Mode,
    then enters the prompt and submits.
    """
    abs_path = os.path.abspath(file_path)
    file_name = os.path.basename(abs_path)
    
    # 1. Ensure file inputs exist (click "Thêm tệp" if not visible/present)
    file_inputs = page.locator('input[type="file"]')
    if file_inputs.count() < 2:
        add_btn = page.locator('button[aria-label*="Thêm tệp"]').first
        if add_btn.is_visible():
            add_btn.click()
            page.wait_for_timeout(1000)
            
    file_inputs = page.locator('input[type="file"]')
    if file_inputs.count() > 0:
        # FileInput index 1 accepts document/markdown files; fallback to index 0 if only 1
        target_fi = file_inputs.nth(1) if file_inputs.count() > 1 else file_inputs.first
        print(f"📎 Đang upload file kịch bản: {file_name}...")
        target_fi.set_input_files(abs_path)
        time.sleep(2)
        print(f"✅ Đã đính kèm tệp {file_name} vào khung nhập liệu.")
    else:
        print(f"⚠️ Cảnh báo: Không tìm thấy ô tải tệp. Fallback về chế độ nhập liệu...")
        
    # 2. Enter the prompt
    copy_to_clipboard(prompt_text)
    if not auto:
        print("ℹ️ Chế độ thủ công bật. Vui lòng tự dán kịch bản và gửi trên màn hình trình duyệt...")
        return
        
    print(f"✍️ Đang nhập lệnh audit cho {file_name}...")
    target_ta = get_followup_input(page) or input_el
    target_ta.focus()
    target_ta.fill(prompt_text)
    time.sleep(1)
    
    # 3. Submit
    submit_selectors = [
        "button[aria-label*='Gửi']",
        "button[aria-label*='Submit']",
        "button[aria-label*='Send']",
        "button[type='submit']",
        "div[role='button'][aria-label*='Gửi']",
        "div[role='button'][aria-label*='Submit']",
        "button[aria-label*='Tìm kiếm']"
    ]
    
    submitted = False
    for sel in submit_selectors:
        try:
            btn = page.locator(sel)
            for idx in range(btn.count()):
                b = btn.nth(idx)
                if b.is_visible() and b.is_enabled():
                    b.click()
                    print("🚀 Đã nhấn nút gửi AI Mode.")
                    submitted = True
                    break
            if submitted:
                break
        except Exception:
            continue
            
    if not submitted:
        print("🚀 Không tìm thấy nút gửi cụ thể. Thực hiện nhấn Enter...")
        page.keyboard.press("Enter")

def submit_prompt(page, input_el, prompt_text, auto=True):
    """
    Copies prompt to clipboard, fills the SGE input, and submits it.
    """
    copy_to_clipboard(prompt_text)
    
    if not auto:
        print("ℹ️ Chế độ thủ công bật. Vui lòng tự dán kịch bản và gửi trên màn hình trình duyệt...")
        return
        
    try:
        print("✍️ Đang nhập kịch bản vào ô nhập liệu...")
        input_el.focus()
        input_el.fill(prompt_text)
        time.sleep(1)
        
        # Search for a submit button close to the textarea
        submit_selectors = [
            "button[aria-label*='Gửi']",
            "button[aria-label*='Submit']",
            "button[aria-label*='Send']",
            "button[type='submit']",
            "div[role='button'][aria-label*='Gửi']",
            "div[role='button'][aria-label*='Submit']",
            "button[aria-label*='Tìm kiếm']"
        ]
        
        submitted = False
        for sel in submit_selectors:
            try:
                btn = page.locator(sel)
                for idx in range(btn.count()):
                    b = btn.nth(idx)
                    if b.is_visible() and b.is_enabled():
                        b.click()
                        print("🚀 Đã nhấn nút gửi AI Mode.")
                        submitted = True
                        break
                if submitted:
                    break
            except Exception:
                continue
                
        if not submitted:
            print("🚀 Không tìm thấy nút gửi cụ thể. Thực hiện nhấn Enter...")
            input_el.press("Enter")
            
    except Exception as e:
        print(f"⚠️ Lỗi khi gửi dữ liệu tự động: {e}. Vui lòng tự nhấn Gửi nếu cần.")

def wait_for_response_stabilization(page, pre_length, interval=2.0, min_stable_checks=4, timeout_sec=180):
    """
    Dynamic Stabilization Check. Monitors body text length.
    Ensures response generation has actually started streaming content and then stabilizes.
    """
    print("⏳ Chờ đợi AI bắt đầu phản hồi...")
    start_time = time.time()
    
    # Phase 1: Wait for generation to start and surpass the initial "thinking" placeholder
    # The thinking indicator is usually ~50 chars: "Chế độ AI đang suy nghĩ..."
    while True:
        curr_text = page.evaluate("document.body.innerText")
        curr_len = len(curr_text)
        diff = curr_text[pre_length:].strip()
        is_thinking = ("đang suy nghĩ" in diff or "is thinking" in diff.lower() or "suy nghĩ để trả lời" in diff) and len(diff) < 250
        
        if len(diff) > 250 and not is_thinking:
            print(f"📈 Phát hiện AI bắt đầu sinh nội dung (đã sinh {len(diff)} ký tự)...")
            break
            
        if time.time() - start_time > 60:
            print("⚠️ Đã quá 60s chờ sinh nội dung. Bắt đầu kiểm tra ổn định ngay...")
            break
        time.sleep(2)
        
    # Phase 2: Wait for streaming to finish and text length to stabilize
    stable_count = 0
    last_length = -1
    check_start = time.time()
    
    print("⏳ Giám sát độ ổn định của văn bản phản hồi...")
    while True:
        curr_text = page.evaluate("document.body.innerText")
        curr_len = len(curr_text)
        diff = curr_text[pre_length:].strip()
        is_thinking = ("đang suy nghĩ" in diff[-200:] or "is thinking" in diff[-200:].lower() or "suy nghĩ để trả lời" in diff[-200:]) and len(diff) < 300
        
        print(f"  └─ Độ dài hiện tại: {curr_len} ký tự (Lần trước: {last_length}) | diff: {len(diff)} ký tự")
        
        # Only consider stable if length hasn't changed, diff is meaningful (> 250 chars), and not currently in thinking state
        if curr_len == last_length and curr_len > 0 and not is_thinking and len(diff) > 250:
            stable_count += 1
            if stable_count >= min_stable_checks:
                print("✅ Phản hồi AI đã hoàn tất và ổn định.")
                break
        else:
            stable_count = 0
            last_length = curr_len
            
        if time.time() - check_start > timeout_sec:
            print(f"⚠️ Cảnh báo: Vượt quá thời gian chờ ổn định ({timeout_sec}s). Tiếp tục xử lý...")
            break
            
        time.sleep(interval)

def extract_text_diff(text_before, text_after):
    """
    Extracts text that was appended to the page by finding the difference.
    """
    min_len = min(len(text_before), len(text_after))
    diff_index = 0
    for i in range(min_len):
        if text_before[i] != text_after[i]:
            diff_index = i
            break
    else:
        diff_index = min_len
        
    return text_after[diff_index:].strip()

def extract_latest_response(page, text_before, text_after):
    """
    Extracts the latest response by trying to find the SGE container first,
    falling back to text difference.
    """
    selectors = [
        "div[data-component-name='SGE_CARD']",
        "div[class*='sge-card']",
        "div[class*='sge-container']",
        "div.O944Te",
        "div[class*='LhN']",
        "div[class*='ai-overview']",
        "div[role='region'][aria-label*='AI Overview']"
    ]
    
    for sel in selectors:
        try:
            els = page.locator(sel)
            count = els.count()
            if count > 0:
                last_el = els.nth(count - 1)
                text = last_el.inner_text().strip()
                if text:
                    print(f"🎯 Trích xuất thành công bằng selector '{sel}'.")
                    return text
        except Exception:
            continue
            
    print("⚠️ Không tìm thấy block AI Overview bằng selector. Sử dụng phương pháp vi sai văn bản...")
    return extract_text_diff(text_before, text_after)

def clean_extracted_response(text, prompt_text):
    """
    Cleans up the extracted AI response to remove search elements,
    buttons, and the prompt itself if it was included.
    """
    # Remove the prompt if it somehow leaked into the response text
    if prompt_text in text:
        text = text.replace(prompt_text, "")
        
    lines = text.split("\n")
    cleaned_lines = []
    
    # Skip common Google search boilerplate lines
    skip_keywords = [
        "Mọi người cũng hỏi", "Tìm kiếm có liên quan", "Xem thêm",
        "Gửi phản hồi", "Bảo mật", "Điều khoản", "Hỏi thêm", "Ask a follow-up"
    ]
    
    for line in lines:
        line_strip = line.strip()
        if not line_strip:
            cleaned_lines.append("")
            continue
        if any(kw in line_strip for kw in skip_keywords):
            continue
        cleaned_lines.append(line)
        
    return "\n".join(cleaned_lines).strip()

def run_audit(episode_dir, all_chapters=False, target_chapter=None, domain=None, auto=True, headless=False, no_screenshot=False):
    """
    Orchestrates the entire audit workflow using Playwright.
    """
    if not os.path.exists(episode_dir):
        print(f"❌ Sai đường dẫn: Thư mục episode '{episode_dir}' không tồn tại.")
        sys.exit(1)
        
    # Find chapters
    chapter_files = []
    if all_chapters:
        for f in os.listdir(episode_dir):
            if f.startswith("chapter_") and f.endswith(".md"):
                chapter_files.append(f)
        chapter_files.sort()
    elif target_chapter:
        # Match names like 1, 01, chapter_01, chapter_01.md
        target = str(target_chapter)
        if not target.startswith("chapter_"):
            if target.isdigit():
                target = f"chapter_{int(target):02d}"
            else:
                target = f"chapter_{target}"
        if not target.endswith(".md"):
            target = f"{target}.md"
            
        target_path = os.path.join(episode_dir, target)
        if os.path.exists(target_path):
            chapter_files = [target]
        else:
            print(f"❌ Không tìm thấy file chương '{target}' trong thư mục {episode_dir}.")
            sys.exit(1)
    else:
        print("❌ Vui lòng chọn --all hoặc chỉ định một chương bằng --chapter <số/tên>.")
        sys.exit(1)
        
    if not chapter_files:
        print(f"⚠️ Không tìm thấy file kịch bản dạng chapter_XX.md nào trong thư mục {episode_dir}.")
        return
        
    print(f"📚 Phát hiện {len(chapter_files)} chương cần audit: {', '.join(chapter_files)}")
    
    # Setup prompt
    if not domain:
        domain = "phân tích xã hội, kinh tế và chính sách công"
        
    topic_title = ""
    topic_summary = ""
    
    # Try reading 01_topic_qualification.md
    qualification_path = os.path.join(episode_dir, "01_topic_qualification.md")
    brief_path = os.path.join(episode_dir, "03_brief.md")
    
    if os.path.exists(qualification_path):
        try:
            with open(qualification_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Find raw_topic or Tên đề tài
                match_topic = re.search(r"raw_topic:\s*(.*?)\n", content)
                if not match_topic:
                    match_topic = re.search(r"\*\s*\*\*Tên đề tài[^:]*:\*\*\s*(.*?)\n", content)
                if match_topic:
                    topic_title = match_topic.group(1).strip()
                # Find topic_summary_one_line
                match_summary = re.search(r"topic_summary_one_line:\s*(.*?)\n", content)
                if match_summary:
                    topic_summary = match_summary.group(1).strip()
        except Exception as e:
            print(f"⚠️ Cảnh báo: Không thể parse 01_topic_qualification.md: {e}")
            
    if not topic_title and os.path.exists(brief_path):
        try:
            with open(brief_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Try finding Episode title first
                match_episode = re.search(r"##\s*(?:EPISODE|ĐỀ TÀI):\s*(.*?)\n", content, re.IGNORECASE)
                if match_episode:
                    topic_title = match_episode.group(1).strip()
                else:
                    match_title = re.search(r"^#\s*(.*?)\n", content)
                    if match_title:
                        topic_title = match_title.group(1).strip()
        except Exception as e:
            print(f"⚠️ Cảnh báo: Không thể parse 03_brief.md: {e}")

    if topic_title:
        print(f"🎯 Đã nhận diện chủ đề kiểm chứng: '{topic_title}'")
        summary_part = f" (Mô tả: {topic_summary})" if topic_summary else ""
        setup_prompt = (
            f"Tôi muốn bạn đóng vai trò là một chuyên gia phản biện khoa học, chính sách công và kinh tế độc lập (Scientific, Policy and Financial Auditor) chuyên ngành {domain}. "
            f"Tôi sẽ gửi cho bạn từng chương kịch bản thuộc chủ đề '{topic_title}'{summary_part} để kiểm chứng nghiêm ngặt tính chính xác của dữ liệu thực tế thời điểm HIỆN TẠI (giữa năm 2026). "
            f"Bạn BẮT BUỘC phải thực hiện tìm kiếm internet thời gian thực với các từ khóa cập nhật nhất năm 2026 để đối chiếu với: "
            f"các số liệu thống kê vĩ mô, các nghiên cứu thực nghiệm, các quyết định lập pháp, nghị định chính sách, sự kiện thực tế, "
            f"và các mô hình tính toán kinh tế liên quan đến chủ đề này. "
            f"Hãy chỉ ra: (1) các thông tin bị sai lệch, thiếu sót hoặc đã lỗi thời, (2) các số liệu thực tế đắt giá mới nhất trong năm 2026 có thể bổ sung, "
            f"và (3) gợi ý cách sửa đổi tối ưu kèm nguồn đối chiếu cụ thể. Hãy phản hồi 'SẴN SÀNG' nếu bạn đã hiểu rõ nhiệm vụ."
        )
    else:
        # Fallback chung sạch sẽ
        setup_prompt = (
            f"Tôi muốn bạn đóng vai trò là một chuyên gia phản biện khoa học, chính sách công và kinh tế độc lập (Scientific, Policy and Financial Auditor) chuyên ngành {domain}. "
            f"Tôi sẽ gửi cho bạn từng chương kịch bản để kiểm chứng nghiêm ngặt tính chính xác của dữ liệu thực tế thời điểm HIỆN TẠI (giữa năm 2026). "
            f"Bạn BẮT BUỘC phải thực hiện tìm kiếm internet thời gian thực với các từ khóa cập nhật nhất năm 2026 để đối chiếu với: "
            f"các số liệu thống kê vĩ mô, các nghiên cứu thực nghiệm, các quyết định lập pháp, nghị định chính sách, sự kiện thực tế, "
            f"và các mô hình tính toán kinh tế liên quan. "
            f"Hãy chỉ ra: (1) các thông tin bị sai lệch, thiếu sót hoặc đã lỗi thời, (2) các số liệu thực tế đắt giá mới nhất trong năm 2026 có thể bổ sung, "
            f"và (3) gợi ý cách sửa đổi tối ưu kèm nguồn đối chiếu cụ thể. Hãy phản hồi 'SẴN SÀNG' nếu bạn đã hiểu rõ nhiệm vụ."
        )
        
    encoded_setup = urllib.parse.quote(setup_prompt)
    init_url = f"https://www.google.com/search?q={encoded_setup}&udm=50"
    
    results = []
    
    with sync_playwright() as playwright:
        browser = None
        is_cdp = False
        try:
            # First try connecting to dedicated Chrome Canary via CDP port 9222
            print("🚀 Đang kiểm tra kết nối trình duyệt chuyên dụng (Chrome Canary CDP 9222)...")
            for cdp_url in ["http://[::1]:9222", "http://127.0.0.1:9222"]:
                try:
                    browser = playwright.chromium.connect_over_cdp(cdp_url)
                    context = browser.contexts[0]
                    is_cdp = True
                    print(f"✅ Đã kết nối với Chrome Canary qua {cdp_url}.")
                    break
                except Exception:
                    continue
                    
            if not is_cdp:
                print("ℹ️ Không có phiên CDP 9222. Khởi chạy trình duyệt mới...")
                try:
                    browser = playwright.chromium.launch(
                        headless=headless,
                        channel="chrome",
                        args=["--disable-blink-features=AutomationControlled"]
                    )
                except Exception as e:
                    print(f"ℹ️ Không thể mở Chrome hệ thống ({e}). Sử dụng Chromium đi kèm Playwright...")
                    browser = playwright.chromium.launch(
                        headless=headless,
                        args=["--disable-blink-features=AutomationControlled"]
                    )
                    
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    locale="vi-VN",
                    timezone_id="Asia/Ho_Chi_Minh",
                    viewport={"width": 1280, "height": 800}
                )
                context.add_init_script("delete navigator.__proto__.webdriver")
            
            page = context.new_page()
            
            print(f"🌐 Đang điều hướng đến Google AI Search...")
            page.goto(init_url)
            
            # Step 2: Handle CAPTCHA / Login
            input_el = wait_for_ready(page)
            
            # First submit requires waiting for stabilization of setup prompt response
            pre_len = page.evaluate("document.body.innerText.length")
            # We already searched for the setup prompt as query parameter 'q', 
            # so SGE should have already started generating. Let's wait for it to stabilize.
            wait_for_response_stabilization(page, pre_len, min_stable_checks=3)
            print("✅ AI đã phản hồi SẴN SÀNG.")
            
            # Step 3: Send chapters sequentially
            for chapter_file in chapter_files:
                chapter_path = os.path.join(episode_dir, chapter_file)
                chapter_num = re.findall(r"\d+", chapter_file)
                chapter_num = chapter_num[0] if chapter_num else "XX"
                
                print(f"\n────────────────────────────────────────\n📝 Bắt đầu audit Chương {chapter_num}: {chapter_file}")
                
                with open(chapter_path, "r", encoding="utf-8") as f:
                    chapter_content = f.read()
                    
                chapter_prompt = (
                    f"Hãy tiến hành tìm kiếm thời gian thực năm 2026 và audit chi tiết nội dung của tệp kịch bản Chương {chapter_num} ({chapter_file}) vừa tải lên. "
                    f"Bạn hãy đối chiếu nghiêm ngặt mọi số liệu, tuyên bố, chính sách, và logic kỹ thuật cơ khí chế tạo, chuỗi cung ứng và tài chính trong văn bản với thực tế cập nhật mới nhất tính đến thời điểm hiện tại năm 2026 tại Việt Nam và quốc tế. "
                    f"Hãy chỉ ra: (1) các thông tin bị sai lệch, thiếu sót hoặc lỗi thời, (2) các số liệu thực tế đắt giá mới nhất trong năm 2026 có thể bổ sung, "
                    f"và (3) gợi ý cách sửa đổi tối ưu kèm nguồn đối chiếu cụ thể."
                )
                
                # Make sure the input element is ready
                input_el = wait_for_ready(page)
                
                # Capture text before submitting
                text_before = page.evaluate("document.body.innerText")
                pre_len = len(text_before)
                
                # Upload chapter file and submit audit prompt
                upload_file_and_submit_prompt(page, input_el, chapter_path, chapter_prompt, auto=auto)
                
                # Wait for stabilization
                wait_for_response_stabilization(page, pre_len)
                
                # Capture text after stabilization
                text_after = page.evaluate("document.body.innerText")
                
                # Extract response
                raw_response = extract_latest_response(page, text_before, text_after)
                cleaned_response = clean_extracted_response(raw_response, chapter_prompt)
                
                # Double check if AI was still generating
                if len(cleaned_response) < 200 or "đang suy nghĩ" in cleaned_response:
                    print("⚠️ Phản hồi có vẻ chưa hoàn tất (dưới 200 ký tự hoặc dính trạng thái suy nghĩ). Đang đợi thêm 15 giây...")
                    time.sleep(15)
                    text_after = page.evaluate("document.body.innerText")
                    raw_response = extract_latest_response(page, text_before, text_after)
                    cleaned_response = clean_extracted_response(raw_response, chapter_prompt)
                
                # Save chapter report
                audit_filename = f"google_ai_audit_{chapter_num}.md"
                audit_path = os.path.join(episode_dir, audit_filename)
                
                # Construct Markdown content
                md_content = (
                    f"# Google AI Search Mode Audit - Chương {chapter_num}\n\n"
                    f"- **Nguồn kiểm chứng:** Google Search AI Mode (udm=50)\n"
                    f"- **Thời gian audit:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"- **File kịch bản:** [{chapter_file}](file://{os.path.abspath(chapter_path)})\n\n"
                    f"## Kết quả phản biện & Đối chiếu nguồn tin:\n\n"
                    f"{cleaned_response}\n\n"
                )
                
                # Screenshot
                screenshot_filename = f"google_ai_audit_{chapter_num}.png"
                screenshot_path = os.path.join(episode_dir, screenshot_filename)
                if not no_screenshot:
                    md_content += f"## Ảnh chụp màn hình đối chiếu:\n\n![Ảnh đối chiếu]({screenshot_filename})\n"
                    try:
                        page.screenshot(path=screenshot_path, full_page=False)
                        print(f"📸 Đã lưu ảnh chụp đối chiếu: {screenshot_path}")
                    except Exception as e:
                        print(f"⚠️ Không thể chụp ảnh màn hình: {e}")
                
                # Write to file
                with open(audit_path, "w", encoding="utf-8") as out_f:
                    out_f.write(md_content)
                    
                print(f"💾 Đã lưu báo cáo Chương {chapter_num}: {audit_path}")
                results.append((chapter_num, chapter_file, audit_filename, screenshot_filename if not no_screenshot else None))
                
                # Short break between chapters to mimic human behavior
                time.sleep(2)
                
            # Compile aggregate report
            if results:
                compile_results_report(episode_dir, results)
                
        finally:
            if is_cdp:
                if 'page' in locals() and page:
                    try:
                        page.close()
                    except Exception:
                        pass
            elif browser:
                print("\n🔌 Đóng trình duyệt...")
                browser.close()

def compile_results_report(episode_dir, results):
    """
    Compiles all individual audit files into a single master report.
    """
    master_path = os.path.join(episode_dir, "google_ai_audit_results.md")
    print(f"\n📊 Đang tổng hợp toàn bộ kết quả vào: {master_path}")
    
    # Count variables
    total_chapters = len(results)
    
    md_report = (
        f"# Báo Cáo Tổng Hợp Kiểm Chứng Thông Tin (Google AI Audit Report)\n\n"
        f"- **Dự án:** {os.path.basename(os.path.abspath(episode_dir))}\n"
        f"- **Thời gian tổng hợp:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"- **Tổng số chương đã kiểm chứng:** {total_chapters}\n\n"
        f"## 📋 Mục lục & Trạng thái các chương\n\n"
    )
    
    # Table of contents
    md_report += "| Chương | Tên File Kịch Bản | Báo Cáo Chi Tiết | Ảnh Đối Chiếu |\n"
    md_report += "|:---:|---|---|---|\n"
    for num, file, audit_file, screenshot in results:
        screenshot_link = f"[Xem ảnh]({screenshot})" if screenshot else "Không có"
        md_report += f"| {num} | [{file}](file://{os.path.abspath(os.path.join(episode_dir, file))}) | [{audit_file}]({audit_file}) | {screenshot_link} |\n"
        
    md_report += "\n---\n\n## 📝 Tóm tắt ý kiến phản biện của AI\n\n"
    
    # Append summaries of each chapter audit
    for num, file, audit_file, _ in results:
        audit_path = os.path.join(episode_dir, audit_file)
        md_report += f"### 🔍 Chương {num}\n\n"
        
        if os.path.exists(audit_path):
            with open(audit_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Extract only the "Kết quả phản biện" section to keep summary clean
            match = re.search(r"## Kết quả phản biện & Đối chiếu nguồn tin:\n\n(.*?)(\n## Ảnh chụp|$)", content, re.DOTALL)
            if match:
                section_content = match.group(1).strip()
                # Take first 10 lines as summary or full text if short
                lines = section_content.split("\n")
                if len(lines) > 15:
                    md_report += "\n".join(lines[:15]) + "\n\n*(Xem thêm chi tiết tại báo cáo chương...)*\n\n"
                else:
                    md_report += section_content + "\n\n"
            else:
                md_report += f"*Xem chi tiết tại [{audit_file}]({audit_file})*\n\n"
        else:
            md_report += f"*Báo cáo không khả dụng.*\n\n"
            
    md_report += "\n---\n"
    md_report += "> [!IMPORTANT]\n"
    md_report += "> **Lưu ý biên tập:** Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng. Vui lòng đối chiếu các điểm cảnh báo của AI để cập nhật dữ liệu/số liệu chính xác nhất vào kịch bản trước khi thực hiện thu âm voiceover.\n"
    
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(md_report)
        
    print(f"🎉 Hoàn thành tổng hợp báo cáo! File được lưu tại: {master_path}")

def main():
    parser = argparse.ArgumentParser(description="Công cụ tự động audit kịch bản bằng Google Search AI Mode (udm=50).")
    parser.add_argument("episode_dir", help="Thư mục chứa các file markdown kịch bản cần audit (ví dụ: episodes/green-sm-an-do).")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="Audit tất cả các chương kịch bản dạng chapter_XX.md có trong thư mục.")
    group.add_argument("--chapter", help="Chỉ định một chương cụ thể cần audit (ví dụ: 1, 01, chapter_01.md).")
    
    parser.add_argument("--domain", help="Chuyên ngành phản biện khoa học (mặc định: phân tích xã hội, kinh tế và chính sách công).")
    parser.add_argument("--no-auto", action="store_false", dest="auto", help="Tắt tự động dán và submit. Cho phép người dùng tự dán thủ công.")
    parser.add_argument("--headless", action="store_true", help="Chạy ẩn trình duyệt (không khuyến khích do dễ bị CAPTCHA chặn).")
    parser.add_argument("--no-screenshot", action="store_true", help="Không chụp ảnh màn hình đối chiếu của từng chương.")
    
    args = parser.parse_args()
    
    run_audit(
        episode_dir=args.episode_dir,
        all_chapters=args.all,
        target_chapter=args.chapter,
        domain=args.domain,
        auto=args.auto,
        headless=args.headless,
        no_screenshot=args.no_screenshot
    )

if __name__ == "__main__":
    main()
