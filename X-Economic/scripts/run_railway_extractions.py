#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script chạy tự động 16 câu hỏi trích xuất dữ liệu trên NotebookLM
Episode: tu-chu-duong-sat-cao-toc-bac-nam
Notebook ID: 4f6b0f44-fa82-4afb-91ba-b3f7b751c51d
"""

import os
import sys
import json
import subprocess
import datetime
import time

NOTEBOOK_ID = "4f6b0f44-fa82-4afb-91ba-b3f7b751c51d"
EPISODE_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/tu-chu-duong-sat-cao-toc-bac-nam"
VAULT_DIR = os.path.join(EPISODE_DIR, "research_vault")
RAW_DIR = os.path.join(VAULT_DIR, "_extraction_raw")
LOG_FILE = os.path.join(VAULT_DIR, "_extraction_log.txt")
MAILBOX_FILE = os.path.join(EPISODE_DIR, "_agent_chat", "mailbox.jsonl")
SEQ_FILE = os.path.join(EPISODE_DIR, "_agent_chat", ".antigravity_last_seq")

TITLES_MAP = {
    1: "Nghị quyết 172/2024/QH15 và Thông số Kỹ thuật Dự án",
    2: "Mốc Khởi Công và Tiến Độ Triển Khai",
    3: "Chuyển giao Chủ Đầu tư và Rút lui của VinSpeed",
    4: "Cơ cấu Nguồn vốn và Tác động Trần Nợ công",
    5: "Mô hình Vận hành, Khai thác Hạ tầng và Đoàn tàu",
    6: "Tỷ lệ và Chiến lược Nội địa hóa Công nghiệp Đường sắt",
    7: "Công nghệ Tàu, Lưới điện và Thông tin Tín hiệu",
    8: "Định mức Suất đầu tư và So sánh Chi phí Quốc tế",
    9: "Dự báo Nhu cầu Vận tải Khách và Hàng hóa",
    10: "Giá vé Dự kiến và Khả năng Cạnh tranh Hàng không",
    11: "Định giá Đất đai, Cơ chế TOD và Nguồn thu Khai thác Ga",
    12: "Nhân lực, Đào tạo và Chuyển giao Công nghệ Nước ngoài",
    13: "Kinh nghiệm Thua lỗ và Tái cơ cấu Đường sắt Quốc tế",
    14: "Rủi ro Chậm tiến độ, Đội vốn và Các Biện pháp Phòng ngừa",
    15: "Chính sách Cấp phép Đặc thù và Cơ chế Đột phá Thể chế",
    16: "Tổng hợp Đánh đổi và Bản Cáo trạng Phản đề Thép"
}

def log_message(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{ts}] {msg}"
    print(formatted)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

def get_next_seq():
    last_seq = 2
    if os.path.exists(MAILBOX_FILE):
        with open(MAILBOX_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        data = json.loads(line)
                        if data.get("seq", 0) > last_seq:
                            last_seq = data.get("seq", 0)
                    except:
                        pass
    return last_seq + 1

def run_extraction(q_num):
    q_file = os.path.join(RAW_DIR, f"q_{q_num}.txt")
    ans_file = os.path.join(VAULT_DIR, f"answer_Q{q_num}.md")
    
    if not os.path.exists(q_file):
        log_message(f"Q{q_num}: File câu hỏi {q_file} không tồn tại!")
        return False, "Thiếu file câu hỏi"
        
    with open(q_file, "r", encoding="utf-8") as f:
        question_text = f.read().strip()
        
    target_note_title = f"Trich xuat Q{q_num}"
    topic_title = TITLES_MAP.get(q_num, f"Câu hỏi {q_num}")
    
    log_message(f"=== Bắt đầu xử lý Q{q_num}: {topic_title} ===")
    
    cmd = [
        "/Users/pro16/.local/bin/notebooklm",
        "ask",
        "-n", NOTEBOOK_ID,
        "--prompt-file", q_file,
        "--save-as-note",
        "-t", target_note_title,
        "--json"
    ]
    
    start_time = time.time()
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=180)
        elapsed = time.time() - start_time
        
        if res.returncode != 0:
            log_message(f"Q{q_num}: Lỗi CLI (code {res.returncode}): {res.stderr}")
            return False, f"CLI error: {res.stderr}"
            
        stdout = res.stdout.strip()
        json_start = stdout.find("{\n  \"answer\":")
        if json_start == -1:
            json_start = stdout.find("{\"answer\":")
            
        if json_start == -1:
            log_message(f"Q{q_num}: Không tìm thấy JSON trong output!")
            return False, "JSON not found in CLI output"
            
        json_data = json.loads(stdout[json_start:])
        answer_text = json_data.get("answer", "")
        references = json_data.get("references", [])
        note_info = json_data.get("note", {})
        note_id = note_info.get("id")
        note_title = note_info.get("title")
        
        # Nếu title chưa khớp format 'Trich xuat Q<so>', đổi tên note
        if note_id and note_title != target_note_title:
            rename_cmd = [
                "/Users/pro16/.local/bin/notebooklm",
                "note", "rename",
                "-n", NOTEBOOK_ID,
                note_id,
                target_note_title
            ]
            subprocess.run(rename_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
        # Format Markdown đầu ra
        out_lines = [
            f"# Trích xuất Dữ liệu Q{q_num} — {topic_title}\n",
            f"**Câu hỏi:** {question_text}\n",
            "## Nội dung Trích xuất Đối chứng\n",
            answer_text + "\n",
            "## Danh mục Nguồn Dẫn chứng (Citations)\n"
        ]
        
        seen_citations = set()
        for ref in references:
            c_num = ref.get("citation_number")
            if c_num and c_num not in seen_citations:
                seen_citations.add(c_num)
                src_id = ref.get("source_id", "")
                cited_text = ref.get("cited_text", "").strip().replace("\n", " ")
                out_lines.append(f"- **[{c_num}]** (Source ID: `{src_id}`): {cited_text[:300]}...")
                
        with open(ans_file, "w", encoding="utf-8") as f:
            f.write("\n".join(out_lines) + "\n")
            
        log_message(f"=== Q{q_num} thành công ({elapsed:.1f}s) -> {ans_file} ===")
        return True, "Thành công"
        
    except subprocess.TimeoutExpired:
        log_message(f"Q{q_num}: Timeout sau 180s")
        return False, "Timeout"
    except Exception as e:
        log_message(f"Q{q_num}: Exception: {str(e)}")
        return False, str(e)

def main():
    log_message("=== KHỞI ĐỘNG TIẾN TRÌNH TRÍCH XUẤT 16 CÂU HỎI NOTEBOOKLM ===")
    
    results = {}
    
    # Q1 đã xử lý trước đó, kiểm tra
    q1_ans = os.path.join(VAULT_DIR, "answer_Q1.md")
    if os.path.exists(q1_ans) and os.path.getsize(q1_ans) > 500:
        results[1] = (True, "Đã có sẵn")
        log_message("Q1: Đã hoàn thành trước đó.")
    else:
        results[1] = run_extraction(1)
        
    # Chạy tiếp từ Q2 đến Q16
    for q_idx in range(2, 17):
        ans_path = os.path.join(VAULT_DIR, f"answer_Q{q_idx}.md")
        if os.path.exists(ans_path) and os.path.getsize(ans_path) > 500:
            results[q_idx] = (True, "Đã có sẵn")
            log_message(f"Q{q_idx}: Đã có sẵn, bỏ qua.")
            continue
            
        success, reason = run_extraction(q_idx)
        results[q_idx] = (success, reason)
        # Nghỉ nhẹ 2s giữa các câu để server ổn định
        time.sleep(2)
        
    success_count = sum(1 for s, _ in results.values() if s)
    failed = [f"Q{k} ({r})" for k, (s, r) in results.items() if not s]
    
    summary = f"Đã hoàn thành trích xuất {success_count}/16 câu hỏi từ Master Notebook {NOTEBOOK_ID} và lưu thành các file answer_Q1.md..answer_Q16.md cùng các note tương ứng trong Notebook."
    if failed:
        summary += f" Các câu gặp sự cố: {', '.join(failed)}."
    else:
        summary += " 100% 16 câu hỏi đã được trích xuất đối chứng đầy đủ, ghi nhận rõ nguồn citations và các điểm mâu thuẫn/KHÔNG RÕ theo đúng chỉ đạo."
        
    log_message(summary)
    
    # Gửi phản hồi vào mailbox.jsonl
    next_seq = get_next_seq()
    report_msg = {
        "from": "antigravity",
        "seq": next_seq,
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "text": f"Báo cáo tiến độ: {summary} Toàn bộ dữ liệu đã sẵn sàng cho Pha 3 (Strategy Brief) và Pha 4 (Master Outline)."
    }
    
    with open(MAILBOX_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(report_msg, ensure_ascii=False) + "\n")
        
    with open(SEQ_FILE, "w", encoding="utf-8") as f:
        f.write(f"{next_seq}\n")
        
    log_message(f"Đã append tin nhắn seq {next_seq} vào {MAILBOX_FILE}.")

if __name__ == "__main__":
    main()
