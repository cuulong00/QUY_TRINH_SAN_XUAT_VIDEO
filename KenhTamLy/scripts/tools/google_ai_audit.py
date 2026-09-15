#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import urllib.parse
import argparse
from playwright.sync_api import sync_playwright

def copy_to_clipboard(text):
    """Sao chép văn bản vào clipboard trên macOS bằng lệnh pbcopy."""
    try:
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(text.encode('utf-8'))
        return True
    except Exception as e:
        print(f"[LỖI] Không thể sao chép vào clipboard: {e}")
        return False

def get_chapters(episode_dir):
    """Lấy danh sách các file chapter_XX.md (XX là số) trong thư mục."""
    chapters = []
    for f in sorted(os.listdir(episode_dir)):
        if f.startswith("chapter_") and f.endswith(".md"):
            # Lọc chỉ lấy các file có đuôi số (ví dụ: chapter_01.md), bỏ qua chapter_template.md
            num_part = f.replace("chapter_", "").replace(".md", "")
            if num_part.isdigit():
                chapters.append(f)
    return chapters

def select_chapter_interactive(episode_dir, chapters):
    """Yêu cầu người dùng chọn chương bằng cách nhập số trong terminal."""
    print("\n=== DANH SÁCH CÁC CHƯƠNG CÓ THỂ AUDIT ===")
    for idx, ch in enumerate(chapters, 1):
        with open(os.path.join(episode_dir, ch), "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            desc = first_line[:60] + "..." if len(first_line) > 60 else first_line
        print(f"[{idx}] {ch} - {desc}")
        
    while True:
        try:
            choice = input(f"\nChọn số thứ tự chương muốn audit (1-{len(chapters)}): ").strip()
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(chapters):
                return chapters[choice_idx]
            else:
                print(f"Vui lòng chọn số trong khoảng từ 1 đến {len(chapters)}")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

def check_input_visible_js(page):
    """Sử dụng JS để kiểm tra xem ô nhập liệu Hỏi thêm đã xuất hiện chưa."""
    js_code = """
    () => {
        const candidates = Array.from(document.querySelectorAll('textarea, input, [contenteditable="true"]'));
        const visibleCandidates = candidates.filter(el => {
            const rect = el.getBoundingClientRect();
            return rect.width > 0 && rect.height > 0 && window.getComputedStyle(el).display !== 'none';
        });
        return visibleCandidates.length > 0;
    }
    """
    try:
        return page.evaluate(js_code)
    except Exception:
        return False

def auto_paste_and_submit(page, text_to_paste):
    """Tìm ô nhập liệu, chèn văn bản tức thời qua Playwright keyboard, và gửi đi."""
    # Tìm selector của ô nhập liệu bằng JS
    input_selector = page.evaluate("""() => {
        const candidates = Array.from(document.querySelectorAll('textarea, input, [contenteditable="true"]'));
        const visible = candidates.filter(el => {
            const rect = el.getBoundingClientRect();
            return rect.width > 0 && rect.height > 0 && window.getComputedStyle(el).display !== 'none';
        });
        if (visible.length === 0) return null;
        visible.sort((a, b) => b.getBoundingClientRect().top - a.getBoundingClientRect().top);
        const el = visible[0];
        
        if (el.id) return `#${el.id}`;
        let selector = el.tagName.toLowerCase();
        if (el.className) {
            selector += '.' + Array.from(el.classList).join('.');
        }
        return selector;
    }""")
    
    if not input_selector:
        print("[LỖI] Không tìm thấy ô nhập liệu bằng JS.")
        return False
        
    try:
        # Focus và click vào ô nhập liệu
        page.focus(input_selector)
        page.click(input_selector)
        
        # Xóa nội dung cũ nếu có
        page.keyboard.press("Meta+A") # macOS
        page.keyboard.press("Backspace")
        
        # Chèn văn bản tức thời (nhanh như dán)
        page.keyboard.insert_text(text_to_paste)
        time.sleep(1) # Đợi 1 giây để UI cập nhật
        
        # Tìm và click nút Gửi
        sent = page.evaluate("""() => {
            const target = document.activeElement;
            if (!target) return false;
            let parent = target.parentElement;
            let sendBtn = null;
            for (let i = 0; i < 5; i++) {
                if (!parent) break;
                const buttons = Array.from(parent.querySelectorAll('button'));
                sendBtn = buttons.find(btn => {
                    const rect = btn.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0 && window.getComputedStyle(btn).display !== 'none';
                });
                if (sendBtn) break;
                parent = parent.parentElement;
            }
            if (sendBtn) {
                sendBtn.click();
                return true;
            }
            return false;
        }""")
        
        if sent:
            print("[INFO] Đã click nút Gửi thành công!")
        else:
            print("[INFO] Không tìm thấy nút gửi, sử dụng bàn phím Enter...")
            page.keyboard.press("Enter")
            
        return True
    except Exception as e:
        print(f"[LỖI] Thất bại khi gửi kịch bản: {e}")
        return False

def wait_for_new_container(page, num_before, timeout_sec=90):
    """Chờ container phản hồi mới xuất hiện và hoàn tất sinh chữ."""
    print(f"[INFO] Đang chờ container phản hồi thứ {num_before + 1} xuất hiện...")
    
    # 1. Chờ container mới xuất hiện
    start_time = time.time()
    container_appeared = False
    while time.time() - start_time < 15:
        try:
            num_now = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
            if num_now > num_before:
                container_appeared = True
                break
        except Exception:
            pass
        time.sleep(1)
        
    if not container_appeared:
        print("[CẢNH BÁO] Không thấy container mới. Đang thử gửi Enter dự phòng...")
        try:
            page.keyboard.press("Enter")
        except Exception:
            pass
        time.sleep(5)
        try:
            num_now = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
            if num_now > num_before:
                container_appeared = True
        except Exception:
            pass
            
    if not container_appeared:
        print("[LỖI] Hết thời gian chờ AI phản hồi.")
        return False
        
    # 2. Chờ độ dài văn bản trong container mới ổn định
    print("[INFO] Đang theo dõi tiến trình sinh chữ của AI...")
    container_index = num_before
    js_get_len = f"() => {{ const el = document.querySelectorAll('div.Zkbeff, div.mZJni')[{container_index}]; return el ? el.innerText.length : 0; }}"
    
    prev_len = 0
    stable_count = 0
    start_time = time.time()
    
    while time.time() - start_time < timeout_sec:
        try:
            curr_len = page.evaluate(js_get_len)
        except Exception:
            curr_len = 0
            
        if curr_len > 0 and curr_len == prev_len:
            stable_count += 1
            if stable_count >= 3: # Ổn định trong 6 giây (3 * 2s)
                print(f"[INFO] AI đã sinh xong phản hồi (Độ dài: {curr_len} ký tự).")
                return True
        else:
            stable_count = 0
            
        prev_len = curr_len
        time.sleep(2)
        
    print("[CẢNH BÁO] Hết thời gian chờ sinh phản hồi ổn định (timeout).")
    return True

def extract_cleaned_response(page, index):
    """Trích xuất và làm sạch hoàn toàn nội dung câu trả lời của AI tại container chỉ định."""
    js_extract = r"""
    (idx) => {
        const containers = document.querySelectorAll('div.Zkbeff, div.mZJni');
        if (idx >= containers.length) return "Không tìm thấy container câu trả lời tương ứng.";
        
        const container = containers[idx];
        const clone = container.cloneNode(true);
        
        // 1. Loại bỏ các inline citation badge dạng số như +1, +2
        clone.querySelectorAll('span, div').forEach(el => {
            const text = el.innerText.trim();
            if (/^\+\d+$/.test(text)) {
                el.remove();
            }
        });

        // 2. Loại bỏ các class rác (nguồn, card liên quan, disclaimers, footer, các liên kết phụ)
        const junkClasses = [
            'yuRUbf', 'V17ozd', 'rTjBgd', 'C2a53d', 'TbwUpd', 
            'QRnEfb', 'v4bSkd', 'ofHStc', 'wDa0n', 'HWMcu', 
            'W94uae', 'lQfa5', 'c0nryc', 'DBd2Wb', 'sge-rp',
            'OkUHJe', 'WBgIic', 'Wg1cdb', 'NMq1me', 'S9OuHf',
            'dNwgB', 'QNca8b', 'vDOt8c', 'oy7Apc', 'qu4n2c',
            'H23r4e'
        ];
        junkClasses.forEach(cls => {
            clone.querySelectorAll(`.${cls}`).forEach(el => el.remove());
        });

        // 3. Loại bỏ các element chứa text rác phổ biến
        clone.querySelectorAll('div, span, p, a, button').forEach(el => {
            const txt = el.innerText.trim();
            if (txt.includes('AI có thể mắc sai sót') || 
                txt.includes('xác minh câu trả lời') || 
                txt.includes('Chính sách quyền riêng tư') || 
                txt.includes('Điều khoản dịch vụ') ||
                txt.includes('gửi yêu cầu gỡ bỏ') ||
                /^\d+ trang web$/.test(txt)) {
                el.remove();
            }
        });

        // 4. Lấy innerText và làm sạch khoảng trắng thừa
        let cleaned = clone.innerText.trim();
        
        // 5. Loại bỏ các dòng trống thừa hoặc định dạng rác còn sót lại
        cleaned = cleaned.split('\n')
            .map(line => line.trim())
            .filter(line => {
                if (!line) return false;
                if (/^\d+ trang web$/.test(line)) return false;
                if (line.includes('AI có thể mắc sai sót') || line.includes('xác minh câu trả lời')) return false;
                return true;
            })
            .join('\n');
            
        return cleaned;
    }
    """
    try:
        cleaned_text = page.evaluate(js_extract, index)
        if cleaned_text:
            return cleaned_text
    except Exception as e:
        print(f"[CẢNH BÁO] Lỗi khi trích xuất và làm sạch qua JS: {e}")
        
    # Fallback
    try:
        return page.evaluate(f"() => {{ const el = document.querySelectorAll('div.Zkbeff, div.mZJni')[{index}]; return el ? el.innerText : ''; }}")
    except Exception:
        return "Không thể trích xuất văn bản từ trang."

def run_audit_session(page, target_chapters, args):
    """Thực thi quy trình audit cho toàn bộ các chương được chọn trong cùng một tab/session."""
    # 1. Thiết lập vai trò Auditor chuyên sâu qua prompt đầu tiên
    setup_prompt = (
        "Tôi muốn bạn đóng vai trò là một chuyên gia phản biện khoa học (Scientific Auditor) "
        "chuyên ngành tâm lý học lâm sàng và khoa học thần kinh. Tôi sẽ gửi cho bạn từng chương "
        "của kịch bản video để bạn kiểm chứng. Đối với mỗi chương, bạn bắt buộc phải thực hiện "
        "tìm kiếm internet để đối chiếu các nghiên cứu, số liệu lâm sàng, cơ chế thần kinh học mới nhất và chỉ ra:\n"
        "1. Các thông tin, số liệu, tên nhà nghiên cứu/thí nghiệm bị sai lệch hoặc không chính xác.\n"
        "2. Các lỗi giải thích sai cơ chế sinh học thần kinh (ví dụ: nhầm lẫn dlPFC/amygdala/insula, sai lệch hệ thần kinh tự chủ...).\n"
        "3. Gợi ý sửa đổi chính xác kèm tên nghiên cứu/nguồn tham khảo cụ thể từ nguồn uy tín (PubMed, Nature, APA...).\n"
        "Hãy phản hồi 'SẴN SÀNG' nếu bạn đã hiểu rõ nhiệm vụ."
    )
    
    encoded_prompt = urllib.parse.quote(setup_prompt)
    google_search_url = f"https://www.google.com/search?q={encoded_prompt}&udm=50"
    
    print(f"[INFO] Khởi tạo phiên kiểm định khoa học trên Google Search AI Mode...")
    page.goto(google_search_url)
    
    # Đợi ô chat "Hỏi thêm" xuất hiện (có thể gặp CAPTCHA)
    input_ready = False
    for i in range(5):
        if check_input_visible_js(page):
            input_ready = True
            break
        time.sleep(1)
        
    if not input_ready:
        print("\n" + "!"*70)
        print(" [CẢNH BÁO CAPTCHA / ĐĂNG NHẬP PHÁT HIỆN]")
        print(" Google đang yêu cầu xác thực người dùng hoặc hiển thị CAPTCHA.")
        print(" Vui lòng hoàn thành giải CAPTCHA trên trình duyệt Chrome đang hiển thị.")
        print(" Hệ thống sẽ tự động phát hiện và tiếp tục sau khi bạn hoàn tất.")
        print("!"*70 + "\n")
        
        for i in range(300):
            if check_input_visible_js(page):
                input_ready = True
                print("[INFO] Đã xác thực thành công! Tiếp tục thiết lập session...")
                break
            time.sleep(1)
            
    if not input_ready:
        print("[LỖI] Hết thời gian chờ xác thực khởi tạo session. Dừng quy trình.")
        return False
        
    # Lấy số container trước khi gửi setup prompt (sẽ là 0)
    num_before = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
    
    # Đợi AI phản hồi xong prompt khởi tạo
    wait_for_new_container(page, num_before)
    
    # 2. Lặp qua từng chương để tiến hành gửi nội dung audit
    for idx, ch_file in enumerate(target_chapters, 1):
        ch_num = ch_file.replace("chapter_", "").replace(".md", "")
        try:
            ch_num_int = int(ch_num)
            ch_label = f"chương {ch_num_int}"
        except ValueError:
            ch_label = ch_file
            
        print(f"\n" + "="*50)
        print(f" TIẾN HÀNH AUDIT: {ch_file} ({idx}/{len(target_chapters)})")
        print("="*50)
        
        # Đọc nội dung chương kịch bản
        ch_path = os.path.join(args.episode_dir, ch_file)
        with open(ch_path, "r", encoding="utf-8") as f:
            ch_content = f.read()
            
        # Copy nội dung kịch bản gốc vào clipboard làm phương án dự phòng
        copy_to_clipboard(ch_content)
        print(f"[INFO] Đã sao chép nội dung {ch_file} vào Clipboard hệ thống.")
        
        # Tạo prompt chi tiết cho chương
        chapter_prompt = (
            f"Hãy tiến hành tìm kiếm và audit nội dung của {ch_label} dưới đây "
            f"dựa trên các dữ liệu thực tế mới nhất trên mạng:\n\n{ch_content}"
        )
        
        if args.auto:
            print(f"[INFO] TỰ ĐỘNG: Đang dán và gửi nội dung {ch_file} vào luồng hội thoại...")
            
            # Lấy số container trước khi gửi chương
            num_before = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
            
            success = auto_paste_and_submit(page, chapter_prompt)
            if success:
                # Chờ container mới sinh xong
                wait_for_new_container(page, num_before)
                
                # Trích xuất phản hồi sạch của container vừa sinh ra
                latest_resp = extract_cleaned_response(page, num_before)
                
                # Lưu kết quả audit chương đơn lẻ
                output_path = os.path.join(args.episode_dir, f"google_ai_audit_{ch_num}.md")
                with open(output_path, "w", encoding="utf-8") as out_f:
                    out_f.write(f"# Kết quả Audit từ Google Search AI Mode - {ch_label.upper()}\n\n")
                    out_f.write(f"- **File nguồn:** `{ch_file}`\n")
                    out_f.write(f"- **Thời gian audit:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    out_f.write("## Phản hồi từ Google AI:\n\n")
                    out_f.write(latest_resp)
                    
                print(f"[SUCCESS] Đã lưu kết quả của {ch_file} tại: {output_path}")
                
                # Chụp ảnh màn hình kết quả cuối để đối chiếu trực quan
                screenshot_path = os.path.join(args.episode_dir, f"google_ai_audit_final_{ch_num}.png")
                page.screenshot(path=screenshot_path)
            else:
                print(f"[LỖI] Không thể tự động gửi kịch bản {ch_file}.")
        else:
            # Chế độ tương tác từng bước
            print("\n" + "="*70)
            print(f" HƯỚNG DẪN TRÊN TRÌNH DUYỆT ({ch_file}):")
            print(" 1. Nội dung chương đã được lưu trong Clipboard của bạn.")
            print(" 2. Hãy dán (Cmd+V) vào ô chat 'Hỏi thêm' trên trình duyệt và gửi đi.")
            print(" 3. Khi Google AI đã phản hồi xong:")
            print("    - Quay lại terminal này và nhấn [ENTER] để tiếp tục.")
            print("======================================================================\n")
            
            # Lấy số container trước khi người dùng gửi
            num_before = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
            
            input(f"Nhấn [ENTER] sau khi hoàn thành audit {ch_file} trên trình duyệt...")
            
            # Chờ thêm 3 giây để đảm bảo UI ổn định
            time.sleep(3)
            
            # Trích xuất phản hồi sạch
            latest_resp = extract_cleaned_response(page, num_before)
            
            output_path = os.path.join(args.episode_dir, f"google_ai_audit_{ch_num}.md")
            with open(output_path, "w", encoding="utf-8") as out_f:
                out_f.write(f"# Kết quả Audit từ Google Search AI Mode - {ch_label.upper()}\n\n")
                out_f.write(f"- **File nguồn:** `{ch_file}`\n")
                out_f.write(f"- **Thời gian audit:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                out_f.write("## Phản hồi từ Google AI:\n\n")
                out_f.write(latest_resp)
                
            print(f"[SUCCESS] Đã lưu kết quả tại: {output_path}")
            
    return True

def compile_all_results(episode_dir, chapters):
    """Gộp tất cả các file kết quả audit chương đơn lẻ thành file google_ai_audit_results.md tổng quan."""
    combined_path = os.path.join(episode_dir, "google_ai_audit_results.md")
    print(f"\n[INFO] Đang tổng hợp kết quả của tất cả các chương vào: {combined_path}")
    
    with open(combined_path, "w", encoding="utf-8") as combined_f:
        combined_f.write("# Tổng Hợp Kết Quả Audit Kịch Bản - Google Search AI Mode\n\n")
        combined_f.write(f"- **Thư mục kịch bản:** `{os.path.basename(episode_dir)}`\n")
        combined_f.write(f"- **Thời gian tổng hợp:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        combined_f.write("## Mục Lục Kết Quả\n\n")
        
        # Tạo danh mục liên kết nhanh
        for ch in chapters:
            num = ch.replace("chapter_", "").replace(".md", "")
            combined_f.write(f"- [Chương {int(num)} - Kết quả chi tiết](#chương-{int(num)}-kết-quả-chi-tiết)\n")
            
        combined_f.write("\n---\n\n")
        
        # Đọc và ghi nội dung từng file
        for ch in chapters:
            num = ch.replace("chapter_", "").replace(".md", "")
            individual_path = os.path.join(episode_dir, f"google_ai_audit_{num}.md")
            
            if os.path.exists(individual_path):
                with open(individual_path, "r", encoding="utf-8") as ind_f:
                    content = ind_f.read()
                combined_f.write(f"## Chương {int(num)} - Kết quả chi tiết\n\n")
                lines = content.split('\n')
                if lines and lines[0].startswith('# '):
                    lines = lines[1:]
                combined_f.write('\n'.join(lines))
                combined_f.write("\n\n---\n\n")
            else:
                combined_f.write(f"## Chương {int(num)} - Kết quả chi tiết\n\n*Lỗi: Không tìm thấy file kết quả {f'google_ai_audit_{num}.md'}*\n\n---\n\n")
                
    print("[SUCCESS] Đã tổng hợp tất cả kết quả thành công!")

def main():
    default_episode_dir = "/Users/pro16/Documents/VideoProject/KenhTamLy/episodes/bong-toi-triet-ly"
    
    parser = argparse.ArgumentParser(description="Audit kịch bản bằng Google Search AI Mode")
    parser.add_argument("episode_dir", nargs="?", default=default_episode_dir, help="Thư mục tập video")
    parser.add_argument("--chapter", help="Tên file chương hoặc số chương (ví dụ: chapter_01.md hoặc 1)")
    parser.add_argument("--all", action="store_true", help="Audit toàn bộ các chương trong thư mục")
    parser.add_argument("--auto", action="store_true", help="Chạy ở chế độ tự động hoàn toàn (không tương tác terminal)")
    parser.add_argument("--headless", action="store_true", help="Chạy trình duyệt ẩn (headless)")
    parser.add_argument("--output", help="Đường dẫn lưu kết quả audit dưới dạng Markdown (chỉ áp dụng khi chạy chương đơn lẻ)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.episode_dir):
        print(f"[LỖI] Thư mục episode không tồn tại: {args.episode_dir}")
        sys.exit(1)
        
    chapters = get_chapters(args.episode_dir)
    if not chapters:
        print(f"[LỖI] Không tìm thấy file chapter_*.md nào trong thư mục {args.episode_dir}")
        sys.exit(1)
        
    # Xác định danh sách chapter cần audit
    target_chapters = []
    if args.all:
        target_chapters = chapters
        print(f"[INFO] Đã chọn chế độ audit TOÀN BỘ ({len(target_chapters)} chương).")
    elif args.chapter:
        selected_chapter = None
        if args.chapter.endswith(".md"):
            if args.chapter in chapters:
                selected_chapter = args.chapter
        else:
            try:
                num = int(args.chapter)
                target_name = f"chapter_{num:02d}.md"
                if target_name in chapters:
                    selected_chapter = target_name
            except ValueError:
                pass
                
        if not selected_chapter:
            for ch in chapters:
                if args.chapter in ch:
                    selected_chapter = ch
                    break
                    
        if not selected_chapter:
            print(f"[LỖI] Không xác định được chương từ đối số: {args.chapter}")
            sys.exit(1)
        target_chapters = [selected_chapter]
    else:
        if args.auto:
            target_chapters = [chapters[0]]
        else:
            selected = select_chapter_interactive(args.episode_dir, chapters)
            target_chapters = [selected]
            
    print(f"\n[INFO] Khởi chạy trình duyệt (headless={args.headless})...")
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(
                headless=args.headless,
                channel="chrome",
                args=[
                    "--start-maximized",
                    "--disable-blink-features=AutomationControlled"
                ]
            )
        except Exception:
            print("[INFO] Không khởi chạy được Google Chrome cài đặt, dùng Chromium mặc định...")
            browser = p.chromium.launch(
                headless=args.headless,
                args=[
                    "--start-maximized",
                    "--disable-blink-features=AutomationControlled"
                ]
            )
            
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            locale="vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
            timezone_id="Asia/Ho_Chi_Minh"
        )
        page = context.new_page()
        page.add_init_script("delete navigator.__proto__.webdriver")
        
        # Chạy quy trình audit trong cùng một tab/session hội thoại
        run_audit_session(page, target_chapters, args)
            
        context.close()
        browser.close()
        print("\n[INFO] Đã đóng trình duyệt sạch sẽ.")
        
    # Nếu chạy nhiều chương, tiến hành gộp kết quả
    if len(target_chapters) > 1:
        compile_all_results(args.episode_dir, target_chapters)
        
    print("\n[INFO] Quy trình audit toàn bộ hoàn tất.")

if __name__ == "__main__":
    main()
