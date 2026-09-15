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

def remove_emojis_and_symbols(text):
    """Loại bỏ các emoji và ký hiệu đặc biệt có thể gây lỗi hệ thống cho Google AI."""
    import re
    # Loại bỏ các ký tự trong dải Emoji/Symbol (SMP - Supplementary Multilingual Plane)
    cleaned = re.sub(r'[\U00010000-\U0010ffff]', '', text)
    # Loại bỏ một số ký hiệu đặc biệt dạng chữ
    special_symbols = ['✅', '⛔', '🔴', '🟡', '❌', '➔', '➖', '🛑', '➔']
    for sym in special_symbols:
        cleaned = cleaned.replace(sym, '')
    return cleaned

def is_port_active(port):
    """Kiểm tra xem một cổng TCP cụ thể có đang mở (active) hay không."""
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def launch_chrome_with_cdp(port, user_data_dir):
    """Khởi chạy Google Chrome thực tế trên macOS với cổng gỡ lỗi từ xa (CDP)."""
    import subprocess
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if not os.path.exists(chrome_path):
        return False
        
    cmd = [
        chrome_path,
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir}",
        "--no-first-run",
        "--no-default-browser-check"
    ]
    print(f"[INFO] Khởi chạy Chrome gỡ lỗi trên cổng {port}...")
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3) # Đợi 3 giây để trình duyệt mở lên hoàn tất
    return True


def clean_research_map_to_plain_text(content):
    """Chuyển đổi bảng markdown phức tạp của Research Map thành plain text có cấu trúc để tránh lỗi parser/safety của Google AI."""
    if not (content.strip().startswith("# Research Map") or "Research Map" in content.split('\n')[0]):
        return content
        
    lines = content.split('\n')
    output = []
    
    current_section = ""
    in_table = False
    headers = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Phát hiện Section mới
        if stripped.startswith("## "):
            current_section = stripped.replace("## ", "")
            output.append(f"\n=== {current_section.upper()} ===")
            in_table = False
            continue
            
        if stripped.startswith("---") or stripped.startswith("# "):
            if not stripped.startswith("# "):
                output.append("\n" + "="*40)
            continue
            
        # Xử lý bảng markdown
        if stripped.startswith("|"):
            # Bỏ qua dòng separator |---|---|
            if "---|---" in stripped or "-|-" in stripped:
                continue
                
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            
            # Lưu headers của bảng
            if not in_table:
                headers = cells
                in_table = True
                continue
                
            # Xử lý dòng dữ liệu trong bảng
            if in_table and len(cells) >= 2:
                # Nếu là bảng Thesis Data
                if "Thesis Data" in current_section or "Luận đề" in current_section:
                    num = cells[0]
                    thesis = cells[1]
                    stats = cells[2] if len(cells) > 2 else ""
                    source = cells[3] if len(cells) > 3 else ""
                    year = cells[4] if len(cells) > 4 else ""
                    notes = cells[7] if len(cells) > 7 else ""
                    
                    output.append(f"\nLuận điểm {num}: {thesis}")
                    if stats: output.append(f"  - Con số cụ thể: {stats}")
                    if source or year: output.append(f"  - Nguồn trích dẫn: {source} ({year})")
                    if notes and notes != "—" and notes != "": output.append(f"  - Ghi chú: {notes}")
                    
                # Nếu là bảng Counter-Thesis Data
                elif "Counter-Thesis" in current_section or "phản biện" in current_section:
                    num = cells[0]
                    risk = cells[1]
                    stats = cells[2] if len(cells) > 2 else ""
                    source = cells[3] if len(cells) > 3 else ""
                    year = cells[4] if len(cells) > 4 else ""
                    notes = cells[6] if len(cells) > 6 else ""
                    
                    output.append(f"\nDữ liệu phản biện {num}: {risk}")
                    if stats: output.append(f"  - Con số cụ thể: {stats}")
                    if source or year: output.append(f"  - Nguồn trích dẫn: {source} ({year})")
                    if notes and notes != "—" and notes != "": output.append(f"  - Ghi chú: {notes}")
                    
                # Nếu là bảng Cơ Chế Vĩ Mô
                elif "Cơ Chế" in current_section or "Mechanisms" in current_section:
                    num = cells[0]
                    name = cells[1]
                    desc = cells[2] if len(cells) > 2 else ""
                    output.append(f"\nCơ chế {num} - {name}:")
                    if desc: output.append(f"  - Chi tiết vận hành: {desc}")
                    
                # Nếu là bảng Điểm mù & Giả định
                elif "Điểm mù" in current_section or "Giả định" in current_section:
                    num = cells[0]
                    assumption = cells[1]
                    fail_cond = cells[2] if len(cells) > 2 else ""
                    consequence = cells[3] if len(cells) > 3 else ""
                    output.append(f"\nGiả định {num}: {assumption}")
                    if fail_cond: output.append(f"  - Có thể sai khi: {fail_cond}")
                    if consequence: output.append(f"  - Hệ quả nếu sai: {consequence}")
                    
                # Nếu là bảng Case Studies
                elif "Case Studies" in current_section or "Thực chứng" in current_section:
                    num = cells[0]
                    name = cells[1]
                    country = cells[2] if len(cells) > 2 else ""
                    event = cells[3] if len(cells) > 3 else ""
                    result = cells[4] if len(cells) > 4 else ""
                    relevance = cells[6] if len(cells) > 6 else ""
                    
                    output.append(f"\nCase Study {num}: {name} ({country})")
                    if event: output.append(f"  - Sự kiện thực tế: {event}")
                    if result: output.append(f"  - Kết quả đạt được: {result}")
                    if relevance and relevance != "—" and relevance != "": output.append(f"  - Liên hệ Việt Nam / Payoff: {relevance}")
                    
                # Các bảng khác (bỏ qua Vault Index)
                elif "Vault Index" in current_section:
                    continue
        else:
            in_table = False
            # Giữ lại các dòng không phải bảng (ví dụ: bullet points trong Data Gaps hay Nguồn đầy đủ)
            if not current_section.lower().startswith("vault index"):
                output.append(stripped)
                
    return "\n".join(output)

def split_content_to_chunks(text):
    """Tách văn bản dựa trên dòng tiêu đề bắt đầu bằng '===' hoặc '##' để gửi các phần nhỏ hơn lên AI."""
    lines = text.split('\n')
    chunks = []
    current_chunk = []
    
    for line in lines:
        stripped = line.strip()
        # Nếu gặp tiêu đề phân đoạn mới và chunk hiện tại đã đủ lớn
        if (stripped.startswith("===") or stripped.startswith("## ")) and len("\n".join(current_chunk)) > 1000:
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []
        current_chunk.append(line)
        
    if current_chunk:
        chunks.append("\n".join(current_chunk))
        
    return chunks

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
            // Thử cách 1: Tìm trong parent của activeElement
            const target = document.activeElement;
            if (target) {
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
            }
            
            // Thử cách 2: Tìm tất cả các button trên trang có label liên quan hoặc chứa icon gửi
            const allButtons = Array.from(document.querySelectorAll('button'));
            const globalSendBtn = allButtons.find(b => {
                const label = (b.getAttribute('aria-label') || '').toLowerCase();
                const text = (b.innerText || '').toLowerCase();
                const isVisible = b.getBoundingClientRect().width > 0 && b.getBoundingClientRect().height > 0 && window.getComputedStyle(b).display !== 'none';
                return isVisible && (label.includes('gửi') || label.includes('send') || text.includes('gửi') || text.includes('send') || b.querySelector('svg') || b.querySelector('i'));
            });
            if (globalSendBtn) {
                globalSendBtn.click();
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

def wait_for_new_container(page, num_before, timeout_sec=120):
    """Chờ container phản hồi mới xuất hiện và hoàn tất sinh chữ."""
    print(f"[INFO] Đang chờ container phản hồi thứ {num_before + 1} xuất hiện...")
    
    start_time = time.time()
    container_appeared = False
    while time.time() - start_time < 20:
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
    # Quyết định setup_prompt dựa trên loại file
    first_file = target_chapters[0] if target_chapters else ""
    is_data_audit = "research" in first_file or "vault" in first_file
    
    if is_data_audit:
        print("[INFO] Thiết lập chế độ: KIỂM TOÁN DỮ LIỆU NGUỒN (Pre-writing Data Audit)...")
        setup_prompt = (
            "Tôi muốn bạn đóng vai trò là một chuyên gia kiểm toán tài chính và phân tích dữ liệu vĩ mô (Macroeconomic & Financial Data Auditor) cho kênh Dòng Chảy. "
            "Tôi sẽ gửi cho bạn bản đồ nghiên cứu dữ liệu (Research Map) thô để bạn fact-check chéo với Internet thời gian thực (ưu tiên cập nhật mới nhất 2025-2026). "
            "Nhiệm vụ của bạn:\n"
            "1. Xác minh số liệu: Đối chiếu chéo các con số kinh tế vĩ mô, công suất dự án, vốn điều lệ doanh nghiệp, tên báo cáo với các nguồn gốc uy tín (IEA, BloombergNEF, IMF, Tổng cục Thống kê, v.v.). Chỉ ra chính xác con số nào sai, lệch hoặc không nhất quán.\n"
            "2. Xác minh pháp lý: Đối chiếu các mốc thời gian, số hiệu văn bản pháp luật, nội dung chính sách tại Việt Nam (Nghị định 57/2025, Quyết định 768/QD-TTg,...) xem có chính xác và đúng bản chất không.\n"
            "3. Phân loại độ tin cậy: Đóng dấu phân loại từng điểm dữ liệu theo 4 cấp độ: [verified_data], [market_analysis], [opinion_commentary], hoặc [⛔ UNVERIFIED] (cần loại bỏ).\n"
            "4. Phát hiện giả định ẩn & Điểm mù: Nêu rõ những dữ liệu nào đang bị thiếu (Data Gaps) hoặc suy diễn logic một chiều để biên tập viên bổ sung.\n"
            "LƯU Ý: Tuyệt đối không thay đổi cấu trúc bảng, không chỉnh sửa câu văn theo giới hạn ký tự đọc TTS. Hãy tập trung 100% vào tính chính xác của dữ liệu.\n"
            "Hãy phản hồi 'SẴN SÀNG' nếu bạn đã hiểu rõ nhiệm vụ."
        )
    else:
        print("[INFO] Thiết lập chế độ: KIỂM TOÁN KỊCH BẢN (Post-writing Script Audit)...")
        setup_prompt = (
            "Tôi muốn bạn đóng vai trò là một chuyên gia kiểm toán tài chính vĩ mô và đối chiếu dữ liệu thực tế (Senior Financial & Macroeconomic Auditor) cho kênh Dòng Chảy. "
            "Tôi sẽ gửi cho bạn từng chương kịch bản để bạn kiểm toán toàn diện về số liệu, sự kiện, các kết luận thực tế, các quy luật kinh tế hành vi và các rủi ro pháp lý/an toàn tài chính. "
            "Nhiệm vụ của bạn:\n"
            "1. CHỈ TẬP TRUNG KIỂM TOÁN SỐ LIỆU, SỰ KIỆN VÀ PHÁP LÝ: Đối chiếu chéo các con số tài chính, giá đất đền bù, số liệu đấu giá, các tỷ lệ phần trăm và các mốc thời gian sự kiện. Phát hiện và gắn cờ đỏ (🔴) các tuyên bố sai sự thật, sai số liệu hoặc thiếu nguồn kiểm chứng.\n"
            "2. TUYỆT ĐỐI KHÔNG KIỂM TOÁN HOẶC CHỈNH SỬA VỀ VĂN PHONG, NGHỆ THUẬT: Tôn trọng hoàn toàn văn phong kể chuyện, giọng điệu, các phép so sánh ẩn dụ kịch tính (ví dụ: con cá mập, cái ao, say độ cao sức mua, bẫy tài sản tĩnh,...) của kịch bản. Không nhận xét hay sửa đổi cấu trúc câu thoại.\n"
            "3. YÊU CẦU BẮT BUỘC VỀ SỐ LIỆU MỚI NHẤT (ĐẾN NĂM 2026): Bạn phải luôn tìm kiếm và đối chiếu với các dữ liệu thực tế và thông tin thời sự mới nhất cập nhật đến năm 2026 (ví dụ: thực tiễn bỏ cọc đấu giá đất Thanh Oai năm 2024-2026, bảng giá đất mới áp dụng từ năm 2026, các cảnh báo gần đây nhất của GS. Đặng Hùng Võ về rủi ro tái nghèo,...). Nghiêm cấm sử dụng các số liệu cũ hoặc lỗi thời khi đã có dữ liệu mới hơn.\n"
            "Hãy phản hồi 'SẴN SÀNG' nếu bạn đã hiểu rõ nhiệm vụ và cam kết tuân thủ đúng các yêu cầu trên."
        )
    
    # Loại bỏ các emoji và ký hiệu đặc biệt trong setup_prompt để tránh bị Google AI chặn/lỗi parser
    setup_prompt = remove_emojis_and_symbols(setup_prompt)
    encoded_prompt = urllib.parse.quote(setup_prompt)
    google_search_url = f"https://www.google.com/search?q={encoded_prompt}&udm=50"
    
    print(f"[INFO] Khởi tạo phiên kiểm định tài chính vĩ mô trên Google Search AI Mode...")
    page.goto(google_search_url)
    
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
        
    num_before = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
    wait_for_new_container(page, num_before)
    
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
        
        ch_path = os.path.join(args.episode_dir, ch_file)
        with open(ch_path, "r", encoding="utf-8") as f:
            ch_content = f.read()
            
        # Chuyển đổi thành plain text có cấu trúc nếu là Research Map để tránh bị Google AI chặn/lỗi parser
        ch_content_cleaned = clean_research_map_to_plain_text(ch_content)
        
        # Làm sạch nốt các link file:/// cục bộ nếu còn sót lại
        import re
        ch_content_cleaned = re.sub(r'\[([^\]]+)\]\(file:///[^\)]+\)', r'[\1]', ch_content_cleaned)
        
        # Loại bỏ các emoji và ký tự đặc biệt có thể gây lỗi hệ thống Google AI
        ch_content_cleaned = remove_emojis_and_symbols(ch_content_cleaned)
            
        # Tách nhỏ nội dung thành các phân đoạn (chunks) nếu file quá dài
        chunks = split_content_to_chunks(ch_content_cleaned)
        print(f"[INFO] Nội dung {ch_file} được chia thành {len(chunks)} phân đoạn để audit tránh quá tải Google AI.")
        
        all_chunk_responses = []
        for c_idx, chunk in enumerate(chunks, 1):
            print(f"\n[INFO] Đang xử lý phân đoạn {c_idx}/{len(chunks)}...")
            copy_to_clipboard(chunk)
            
            chunk_prompt = (
                f"Hãy tiến hành tìm kiếm, đối chiếu và audit toàn diện nội dung của phân đoạn {c_idx}/{len(chunks)} thuộc {ch_label} dưới đây "
                f"dựa trên các dữ liệu thực tế vĩ mô và tài chính mới nhất (ưu tiên 2025-2026):\n\n{chunk}"
            )
            
            if args.auto:
                print(f"[INFO] TỰ ĐỘNG: Đang dán và gửi phân đoạn {c_idx}/{len(chunks)} vào luồng hội thoại...")
                num_before = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
                
                success = auto_paste_and_submit(page, chunk_prompt)
                if success:
                    wait_for_new_container(page, num_before)
                    latest_resp = extract_cleaned_response(page, num_before)
                    all_chunk_responses.append(f"### Phân đoạn {c_idx}/{len(chunks)}:\n\n{latest_resp}\n")
                    
                    if c_idx == len(chunks):
                        screenshot_path = os.path.join(args.episode_dir, f"google_ai_audit_final_{ch_num}.png")
                        page.screenshot(path=screenshot_path)
                else:
                    print(f"[LỖI] Không thể tự động gửi phân đoạn {c_idx}.")
                    all_chunk_responses.append(f"### Phân đoạn {c_idx}/{len(chunks)}:\n\n*LỖI: Không thể tự động gửi phân đoạn này.*\n")
            else:
                print("\n" + "="*70)
                print(f" HƯỚNG DẪN TRÊN TRÌNH DUYỆT (Phân đoạn {c_idx}/{len(chunks)} - {ch_file}):")
                print(" 1. Nội dung phân đoạn đã được lưu trong Clipboard của bạn.")
                print(" 2. Hãy dán (Cmd+V) vào ô chat 'Hỏi thêm' trên trình duyệt và gửi đi.")
                print(" 3. Khi Google AI đã phản hồi xong:")
                print("    - Quay lại terminal này và nhấn [ENTER] để tiếp tục.")
                print("======================================================================\n")
                
                num_before = page.evaluate("() => document.querySelectorAll('div.Zkbeff, div.mZJni').length")
                input(f"Nhấn [ENTER] sau khi hoàn thành audit phân đoạn {c_idx}/{len(chunks)} trên trình duyệt...")
                
                time.sleep(3)
                latest_resp = extract_cleaned_response(page, num_before)
                all_chunk_responses.append(f"### Phân đoạn {c_idx}/{len(chunks)}:\n\n{latest_resp}\n")
                
        output_path = os.path.join(args.episode_dir, f"google_ai_audit_{ch_num}.md")
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write(f"# Kết quả Audit từ Google Search AI Mode - {ch_label.upper()}\n\n")
            out_f.write(f"- **File nguồn:** `{ch_file}`\n")
            out_f.write(f"- **Thời gian audit:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            out_f.write("## Phản hồi từ Google AI:\n\n")
            out_f.write("\n".join(all_chunk_responses))
            
        print(f"[SUCCESS] Đã lưu kết quả hoàn chỉnh tại: {output_path}")
            
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
        
        for ch in chapters:
            num = ch.replace("chapter_", "").replace(".md", "")
            combined_f.write(f"- [Chương {int(num)} - Kết quả chi tiết](#chương-{int(num)}-kết-quả-chi-tiết)\n")
            
        combined_f.write("\n---\n\n")
        
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
    # Mặc định sử dụng tập phim Long Thành hiện tại trong Dòng Chảy
    default_episode_dir = "/Users/pro16/Documents/VideoProject/Dòng Chảy/episodes/thu-tuong-di-long-thanh"
    
    parser = argparse.ArgumentParser(description="Audit kịch bản Dòng Chảy bằng Google Search AI Mode")
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
    
    target_chapters = []
    if args.all:
        if not chapters:
            print(f"[LỖI] Không tìm thấy file chapter_*.md nào để audit toàn bộ.")
            sys.exit(1)
        target_chapters = chapters
        print(f"[INFO] Đã chọn chế độ audit TOÀN BỘ ({len(target_chapters)} chương).")
    elif args.chapter:
        selected_chapter = None
        # 1. Kiểm tra trực tiếp xem file có tồn tại trong thư mục không
        full_path = os.path.join(args.episode_dir, args.chapter)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            selected_chapter = args.chapter
        # 2. Khớp theo đuôi .md trong danh sách chapters
        elif args.chapter.endswith(".md"):
            if args.chapter in chapters:
                selected_chapter = args.chapter
        # 3. Khớp theo số chương
        else:
            try:
                num = int(args.chapter)
                target_name = f"chapter_{num:02d}.md"
                if target_name in chapters:
                    selected_chapter = target_name
            except ValueError:
                pass
                
        # 4. Khớp chứa từ khóa
        if not selected_chapter:
            for ch in chapters:
                if args.chapter in ch:
                    selected_chapter = ch
                    break
                    
        if not selected_chapter:
            print(f"[LỖI] Không xác định được file cần audit từ đối số: {args.chapter}")
            sys.exit(1)
        target_chapters = [selected_chapter]
    else:
        if not chapters:
            print(f"[LỖI] Không tìm thấy file chapter_*.md nào trong thư mục {args.episode_dir}")
            sys.exit(1)
        if args.auto:
            target_chapters = [chapters[0]]
        else:
            selected = select_chapter_interactive(args.episode_dir, chapters)
            target_chapters = [selected]
            
    port = 9222
    user_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scratch", "playwright_profile")
    
    # Đảm bảo thư mục tồn tại
    os.makedirs(user_data_dir, exist_ok=True)
    
    with sync_playwright() as p:
        connected = False
        browser = None
        context = None
        
        # Thử kết nối tới trình duyệt đang chạy qua CDP nếu có sẵn
        if is_port_active(port):
            try:
                print(f"[INFO] Đang kết nối tới trình duyệt Chrome đang mở tại cổng {port}...")
                browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
                connected = True
            except Exception as e:
                print(f"[CẢNH BÁO] Lỗi khi kết nối CDP: {e}. Sẽ chuyển sang chế độ khởi chạy trực tiếp.")
                
        if not connected:
            print(f"\n[INFO] Khởi chạy trình duyệt có profile lưu trữ (headless={args.headless})...")
            try:
                context = p.chromium.launch_persistent_context(
                    user_data_dir,
                    headless=args.headless,
                    channel="chrome",
                    args=[
                        "--start-maximized",
                        "--disable-blink-features=AutomationControlled"
                    ],
                    viewport={"width": 1280, "height": 800},
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    locale="vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
                    timezone_id="Asia/Ho_Chi_Minh"
                )
            except Exception:
                print("[INFO] Không khởi chạy được Google Chrome cài đặt, dùng Chromium mặc định...")
                context = p.chromium.launch_persistent_context(
                    user_data_dir,
                    headless=args.headless,
                    args=[
                        "--start-maximized",
                        "--disable-blink-features=AutomationControlled"
                    ],
                    viewport={"width": 1280, "height": 800},
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    locale="vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
                    timezone_id="Asia/Ho_Chi_Minh"
                )
                
        if connected:
            # Lấy context mặc định của trình duyệt được kết nối qua CDP để tránh lỗi Browser context management is not supported
            default_context = browser.contexts[0]
            page = default_context.new_page()
        else:
            page = context.pages[0] if context.pages else context.new_page()
            
        page.add_init_script("delete navigator.__proto__.webdriver")
        
        run_audit_session(page, target_chapters, args)
        
        # Nếu kết nối CDP, chỉ đóng tab/trang audit, không đóng browser
        if connected:
            page.close()
            print("[INFO] Đã đóng tab audit. Trình duyệt Chrome vẫn được giữ mở trên màn hình.")
        else:
            context.close()
            print("\n[INFO] Đã đóng trình duyệt và lưu lại profile.")
        
    if len(target_chapters) > 1:
        compile_all_results(args.episode_dir, target_chapters)
        
    print("\n[INFO] Quy trình audit hoàn tất.")

if __name__ == "__main__":
    main()
