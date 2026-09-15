#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.error
import argparse

# Cấu hình đối số dòng lệnh
parser = argparse.ArgumentParser(description="PM Planner - AI Project Manager Lập Kế Hoạch Học Tập & Phát Triển")
parser.add_argument("--model", type=str, default="gemini-2.5-flash", help="Model Gemini sử dụng")
args = parser.parse_args()

# Thư mục gốc dự án
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
PERSONAS_DIR = os.path.join(BASE_DIR, "personas")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

# Đảm bảo thư mục outputs tồn tại
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# Lấy API Key
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    env_path = os.path.join(PROJECT_DIR, ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    API_KEY = line.strip().split("=", 1)[1].strip('"').strip("'")
                    break

# Hàm gọi Gemini API với cơ chế tự động thử lại thông minh (Retry với Cooldown)
def call_gemini(system_instruction, prompt, model=args.model, max_retries=5):
    import time
    if not API_KEY:
        print("\n[LỖI] Không tìm thấy GEMINI_API_KEY trong môi trường hoặc tệp .env.")
        print("Vui lòng cấu hình API Key: export GEMINI_API_KEY=\"your_key_here\"")
        sys.exit(1)

    # Thêm độ trễ nhỏ giữa các lần gọi để tránh rate limit của API key
    time.sleep(2)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}"
    payload = {
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        },
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.2
        }
    }
    
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode("utf-8"), 
        headers=headers, 
        method="POST"
    )
    
    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                return res_data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            # Xác định mã lỗi HTTP
            status_code = getattr(e, "code", None)
            
            if attempt == max_retries:
                print(f"\n[Lỗi kết nối sau {max_retries} lần thử]: {str(e)}")
                sys.exit(1)
                
            if status_code == 429:
                wait_time = attempt * 20  # Đợi lâu hơn khi bị chặn tốc độ (429)
                print(f" -> [Rate Limit 429] Quá nhiều yêu cầu. Đang nghỉ giải nhiệt {wait_time} giây trước khi thử lại lần {attempt+1}/{max_retries}...")
            elif status_code == 503:
                wait_time = attempt * 10  # Đợi trung bình khi server bận (503)
                print(f" -> [Server Busy 503] Server bận. Đang đợi {wait_time} giây trước khi thử lại lần {attempt+1}/{max_retries}...")
            else:
                wait_time = attempt * 5   # Lỗi kết nối thông thường
                print(f" -> [Cảnh báo] Lỗi kết nối ({str(e)}). Đang đợi {wait_time} giây trước khi thử lại lần {attempt+1}/{max_retries}...")
                
            time.sleep(wait_time)

# Hàm đọc thông tin dự án
def get_project_context():
    context = []
    
    # 1. Đọc prompt.md nếu có
    prompt_path = os.path.join(PROJECT_DIR, "prompt.md")
    if os.path.exists(prompt_path):
        with open(prompt_path, "r", encoding="utf-8") as f:
            context.append(f"### YÊU CẦU BAN ĐẦU (prompt.md):\n{f.read()}\n")
            
    # 2. Đọc walkthrough.md từ thư mục dự án nếu có
    wt_path = os.path.join(PROJECT_DIR, "walkthrough.md")
    if os.path.exists(wt_path):
        with open(wt_path, "r", encoding="utf-8") as f:
            context.append(f"### TRẠNG THÁI HIỆN TẠI (walkthrough.md):\n{f.read()}\n")
            
    # 3. Đọc cấu trúc thư mục dự án
    project_structure = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        # Bỏ qua các thư mục ẩn và node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules' and d != 'venv']
        for file in files:
            if not file.startswith('.'):
                rel_path = os.path.relpath(os.path.join(root, file), PROJECT_DIR)
                project_structure.append(f"- {rel_path}")
                
    context.append(f"### CẤU TRÚC MÃ NGUỒN HIỆN TẠI:\n" + "\n".join(project_structure) + "\n")
    
    return "\n".join(context)

def main():
    print("=" * 60)
    print(" KHỞI CHẠY PM PLANNER (PROJECT MANAGER)")
    print("=" * 60)
    
    # Đọc persona PM
    pm_persona_path = os.path.join(PERSONAS_DIR, "ProjectManager.md")
    if not os.path.exists(pm_persona_path):
        print(f"[LỖI] Không tìm thấy persona ProjectManager tại {pm_persona_path}")
        sys.exit(1)
        
    with open(pm_persona_path, "r", encoding="utf-8") as f:
        si_pm = f.read()

    # Thu nhập ngữ cảnh dự án
    print("Đang quét cấu trúc thư mục và trạng thái mã nguồn...")
    project_context = get_project_context()
    
    # Tạo prompt lập kế hoạch
    prompt = f"""Dưới đây là ngữ cảnh trạng thái hiện tại của dự án Active Recall & Spaced Repetition Study Manager:

{project_context}

Hãy đóng vai trò là Project Manager (PM), thực hiện các nhiệm vụ sau:
1. Đánh giá xem dự án đã hoàn thành những gì và đang ở Phase mấy của Lộ trình học tập & phát triển tổng thể.
2. Xác định các thiếu sót, rủi ro kỹ thuật hoặc rủi ro sư phạm ở thời điểm hiện tại.
3. Đề xuất Kế hoạch Hành động tiếp theo (Backlog) được phân chia rõ ràng dưới dạng các TICKET công việc cho BA, Developer, QA và Education Specialist.
4. Tạo Bảng Quyết định/Phê duyệt của Phụ huynh (Parent's Decision Table) để Phụ huynh có thể tích chọn:
   - Duyệt (Đồng ý làm bước tiếp theo)
   - Từ chối
   - Yêu cầu sửa đổi

Hãy định dạng kết quả dưới dạng Markdown đẹp mắt, chuẩn chỉ và lưu trữ rõ ràng để trình bày cho Phụ huynh.
"""

    print("Đang gọi PM Agent qua Gemini API để phân tích lập kế hoạch...")
    plan_output = call_gemini(si_pm, prompt)
    
    # Ghi tệp kế hoạch đầu ra
    output_path = os.path.join(OUTPUTS_DIR, "next_action_plan.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(plan_output)
        
    print("=" * 60)
    print(" TẠO KẾ HOẠCH THÀNH CÔNG!")
    print(f" Kế hoạch hành động tiếp theo đã được ghi nhận tại:")
    print(f" {output_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()
