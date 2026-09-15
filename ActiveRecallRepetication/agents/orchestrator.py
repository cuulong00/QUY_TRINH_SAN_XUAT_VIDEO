#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.error
import argparse

# Khởi tạo argparse để nhận đầu vào từ CLI
parser = argparse.ArgumentParser(description="Mô phỏng quy trình làm việc Multi-Agent cho Active Recall Study App")
parser.add_argument("--task", type=str, required=True, help="Yêu cầu hoặc tính năng cần triển khai")
parser.add_argument("--model", type=str, default="gemini-1.5-flash", help="Model Gemini sử dụng")
parser.add_argument("--mock", action="store_true", help="Chạy ở chế độ mô phỏng dữ liệu mẫu để tránh rate limit")
args = parser.parse_args()

# Thư mục chứa các tệp
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PERSONAS_DIR = os.path.join(BASE_DIR, "personas")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

# Tạo thư mục đầu ra nếu chưa có
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# Lấy API Key từ môi trường
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY and not args.mock:
    # Thử tìm trong file .env ở gốc dự án
    env_path = os.path.join(os.path.dirname(BASE_DIR), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    API_KEY = line.strip().split("=", 1)[1].strip('"').strip("'")
                    break

# Biến đếm toàn cục để theo dõi số lần gọi của từng Agent trong chế độ mock
mock_call_counts = {
    "Business Analyst": 0,
    "Education Specialist": 0,
    "Developer": 0,
    "QA Engineer": 0
}

# Hàm gọi Gemini API qua urllib với cơ chế tự động thử lại thông minh (Retry với Cooldown)
def call_gemini(system_instruction, prompt, model=args.model, max_retries=8):
    import time
    if args.mock:
        time.sleep(1) # Độ trễ nhỏ giả lập thực tế
        if "Business Analyst" in system_instruction:
            mock_call_counts["Business Analyst"] += 1
            if mock_call_counts["Business Analyst"] == 1:
                return """## PRD: Lập Lịch Ôn Tập Từ Vựng Tiếng Anh Lớp 5 (V1)
- **Tính năng**: Tự động nhắc nhở ôn tập từ vựng tiếng Anh.
- **Chu kỳ ôn tập**: Lặp lại sau mỗi 1 giờ (Mặc định).
- **Luồng học tập**: Hệ thống hiển thị từ vựng dạng flashcard để bé xem đi xem lại liên tục mỗi giờ.
- **Tiêu chí nghiệm thu**: Bé mở app là thấy từ vựng ôn tập cũ sau 1 giờ."""
            else:
                return """## PRD: Lập Lịch Ôn Tập Từ Vựng Tiếng Anh Lớp 5 (V2 - Đã sửa đổi)
- **Tính năng**: Tự động nhắc nhắc học từ vựng tiếng Anh chủ động (Active Recall).
- **Chu kỳ ôn tập**: Áp dụng Spaced Repetition (Lặp lại ngắt quãng: ngày 1, ngày 3, ngày 7, ngày 14, ngày 30).
- **Giới hạn nhận thức**: Cấu hình tối đa 20 thẻ từ vựng mới mỗi ngày để tránh trẻ bị quá tải.
- **Tiêu chí nghiệm thu**: Thẻ từ vựng được tự động xếp lịch ôn tập dài ra nếu trẻ đánh giá mức độ nhớ là Dễ."""
        elif "Education Specialist" in system_instruction:
            mock_call_counts["Education Specialist"] += 1
            if mock_call_counts["Education Specialist"] == 1:
                return """[CẢNH BÁO SƯ PHẠM]
Khoảng cách ôn tập từ vựng 1 giờ là phản sư phạm và không mang lại hiệu quả ghi nhớ dài hạn (Spaced Repetition). Lặp lại quá dồn dập sẽ làm trẻ mệt mỏi, nhàm chán và gây quá tải nhận thức. Khoảng cách tối thiểu phải bắt đầu từ 1 ngày, sau đó giãn dần.
Đồng thời, việc chỉ hiển thị từ vựng để trẻ đọc đi đọc lại là phương pháp học thụ động. Cần chuyển sang phương pháp chủ động nhớ lại (Active Recall) bằng cách ẩn nghĩa của từ hoặc từ khóa còn thiếu để trẻ tự suy nghĩ trước khi lật thẻ."""
            else:
                return """[ĐỒNG Ý SƯ PHẠM]
Bản PRD V2 đã cập nhật chính xác thuật toán lặp khoảng cách Spaced Repetition khoa học (1, 3, 7, 14, 30 ngày) và tích hợp cơ chế chủ động nhớ lại (Active Recall) cho flashcard, kèm theo giới hạn 20 thẻ mới/ngày giúp bảo vệ sức khỏe học tập của trẻ."""
        elif "QA Engineer" in system_instruction:
            mock_call_counts["QA Engineer"] += 1
            if mock_call_counts["QA Engineer"] == 1:
                return """[QA REJECTED]
Phát hiện lỗi bảo mật nghiêm trọng: GEMINI_API_KEY được lập trình viên lưu trực tiếp ở file client side index.js để gọi API sinh câu hỏi tự động. Học sinh hoặc bên thứ ba có thể dễ dàng kiểm tra nguồn trang để lấy cắp key. Yêu cầu chuyển sang lưu trữ an toàn ở Backend Edge Function.
Ngoài ra, các nút bấm chọn mức độ nhớ (Dễ/Khó) trên màn hình điện thoại chỉ có kích thước 30x30px, quá nhỏ cho ngón tay trẻ em thao tác, vi phạm chuẩn accessibility (a11y) tối thiểu 48x48px."""
            else:
                return """[QA APPROVED]
Phương án lập trình V2 đã chuyển API Key lên Edge Function an toàn, sử dụng IndexedDB lưu dữ liệu local-first, và thiết kế các nút bấm tương tác lớn hơn 48x48px đạt chuẩn UI trẻ em. QA ký duyệt chất lượng."""
        elif "Developer" in system_instruction:
            mock_call_counts["Developer"] += 1
            if mock_call_counts["Developer"] == 1:
                return """## Phương án kỹ thuật Developer (V1)
- **Giao diện**: Hiển thị flashcard từ vựng, nút bấm "Đã hiểu" kích thước 30x30px.
- **Lưu trữ**: Gọi API Gemini trực tiếp từ client (nhúng API key ở client index.js) để sinh câu hỏi flashcard.
- **Database**: Lưu trữ lịch sử ôn tập bằng localStorage cục bộ."""
            else:
                return """## Phương án kỹ thuật Developer (V2 - Bảo mật & Trải nghiệm trẻ em)
- **Giao diện**: Thiết kế lại vùng bấm nút phản hồi nhớ bài tối thiểu 48x48px để trẻ dễ thao tác trên iPad/Mobile.
- **Bảo mật**: Định tuyến việc gọi Gemini sinh câu hỏi qua Backend Node.js Server để che giấu API Key hoàn toàn.
- **Database**: Sử dụng IndexedDB hỗ trợ lưu trữ local-first mượt mà, đồng bộ ngầm khi phát hiện có mạng trở lại."""

    if not API_KEY:
        print("\n[LỖI] Không tìm thấy GEMINI_API_KEY trong môi trường hoặc tệp .env.")
        print("Vui lòng cấu hình API Key: export GEMINI_API_KEY=\"your_key_here\" hoặc chạy với tham số --mock")
        sys.exit(1)

    # Thêm độ trễ lớn hơn giữa các lần gọi để tránh rate limit của API key (phù hợp với free tier RPM)
    time.sleep(8)

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
            status_code = getattr(e, "code", None)
            
            if attempt == max_retries:
                print(f"\n[Lỗi kết nối sau {max_retries} lần thử]: {str(e)}")
                sys.exit(1)
                
            if status_code == 429:
                wait_time = attempt * 30  # Đợi lâu hơn hẳn khi bị chặn tốc độ (429)
                print(f" -> [Rate Limit 429] Quá nhiều yêu cầu. Đang nghỉ giải nhiệt {wait_time} giây trước khi thử lại lần {attempt+1}/{max_retries}...")
            elif status_code == 503:
                wait_time = attempt * 15  # Đợi trung bình khi server bận (503)
                print(f" -> [Server Busy 503] Server bận. Đang đợi {wait_time} giây trước khi thử lại lần {attempt+1}/{max_retries}...")
            else:
                wait_time = attempt * 10   # Lỗi kết nối thông thường
                print(f" -> [Cảnh báo] Lỗi kết nối ({str(e)}). Đang đợi {wait_time} giây trước khi thử lại lần {attempt+1}/{max_retries}...")
                
            time.sleep(wait_time)

# Đọc file system instruction của từng Agent
def read_persona(filename):
    path = os.path.join(PERSONAS_DIR, filename)
    if not os.path.exists(path):
        print(f"[CẢNH BÁO] Không tìm thấy tệp persona tại {path}. Dùng cấu hình trống.")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    print("=" * 60)
    print(" KHỞI CHẠY QUY TRÌNH MULTI-AGENT COLLABORATION (SOP)")
    print("=" * 60)
    print(f"Yêu cầu đầu vào: '{args.task}'\n")

    # Đọc chỉ dẫn hệ thống cho từng vai trò
    si_ba = read_persona("BusinessAnalyst.md")
    si_es = read_persona("EducationSpecialist.md")
    si_dev = read_persona("Developer.md")
    si_qa = read_persona("QATester.md")

    # -------------------------------------------------------------
    # VÒNG LẶP BA <-> EDUCATION SPECIALIST (Phản biện Sư phạm)
    # -------------------------------------------------------------
    print("--- [BẮT ĐẦU VÒNG LẶP PHẢN BIỆN: BA & EDUCATION SPECIALIST] ---")
    prd_output = ""
    pedagogical_review = ""
    max_loops = 3
    
    for loop in range(1, max_loops + 1):
        print(f"\n[Vòng {loop}] BA Agent đang soạn thảo đặc tả PRD...")
        if loop == 1:
            # Cố tình đưa lỗi sư phạm ở vòng 1 để chứng minh vòng lặp hoạt động
            prompt_ba = (
                f"Hãy đóng vai trò BA, tiếp nhận yêu cầu sau từ Phụ huynh: '{args.task}'. "
                f"Phân tích và viết đặc tả PRD chi tiết (user flow, data schema, AC). "
                f"LƯU Ý: Về khoảng cách ôn tập lặp lại, hãy thiết lập mặc định trong PRD là học lại sau mỗi 1 giờ ôn liên tục để nhớ nhanh."
            )
        else:
            prompt_ba = (
                f"Đọc lại đặc tả PRD cũ của bạn và sửa đổi lỗi dựa trên phản hồi của Chuyên gia Giáo dục.\n"
                f"Phản hồi từ Chuyên gia Giáo dục:\n{pedagogical_review}\n\n"
                f"Hãy sửa lại chu kỳ ôn tập Spaced Repetition về đúng chuẩn (ngày 1, 3, 7, 14, 30) và thiết lập flashcard theo dạng Active Recall chủ động, giới hạn tối đa 20 thẻ mới/ngày."
            )
            
        prd_output = call_gemini(si_ba, prompt_ba)
        print(f" -> BA đã tạo xong PRD Vòng {loop}.")
        
        print(f"[Vòng {loop}] Education Specialist Agent đang thẩm định sư phạm...")
        prompt_es = (
            f"Đọc kỹ yêu cầu ban đầu: '{args.task}' và bản đặc tả PRD của BA:\n\n{prd_output}\n\n"
            f"Đóng vai trò Education Specialist, hãy rà soát tính chính xác sư phạm (độ khó bài học ôn thi lớp 6, chu kỳ lặp khoảng cách, phương pháp nhớ chủ động, tránh quá tải trí óc). "
            f"BẮT BUỘC bắt đầu câu trả lời bằng cờ '[CẢNH BÁO SƯ PHẠM]' ở dòng đầu tiên nếu phát hiện lỗi sai phương pháp sư phạm (như lặp lại sau mỗi 1 giờ - gây mệt mỏi và phản khoa học), "
            f"hoặc '[ĐỒNG Ý SƯ PHẠM]' nếu giáo án học tập đã hoàn toàn tối ưu và phù hợp với sự phát triển trí óc của bé."
        )
        pedagogical_review = call_gemini(si_es, prompt_es)
        first_line = pedagogical_review.splitlines()[0] if pedagogical_review.splitlines() else ""
        print(f" -> Kết quả thẩm định: {first_line}")
        
        if "[ĐỒNG Ý SƯ PHẠM]" in first_line or "[ĐỒNG Ý SƯ PHẠM]" in pedagogical_review[:100]:
            print(">>> [PHÊ DUYỆT SƯ PHẠM] Chuyển sang bước tiếp theo.")
            break
        else:
            print(">>> [TỪ CHỐI SƯ PHẠM] Phát hiện lỗi sư phạm. Kích hoạt phản hồi sửa đổi...")

    # -------------------------------------------------------------
    # VÒNG LẶP DEVELOPER <-> QA/TESTER (Phản biện Kỹ thuật)
    # -------------------------------------------------------------
    print("\n--- [BẮT ĐẦU VÒNG LẶP PHẢN BIỆN: DEVELOPER & QA TESTER] ---")
    dev_plan = ""
    qa_report = ""
    
    for loop in range(1, max_loops + 1):
        print(f"\n[Vòng {loop}] Developer Agent đang thiết kế phương án lập trình...")
        if loop == 1:
            # Cố tình đưa lỗi bảo mật ở vòng 1 để chứng minh vòng lặp hoạt động
            prompt_dev = (
                f"Đọc kỹ PRD đã duyệt:\n{prd_output}\n\nvà báo cáo sư phạm:\n{pedagogical_review}\n\n"
                f"Hãy đóng vai trò Developer, lên phương án kỹ thuật (DB local-first, UI, API sinh câu hỏi). "
                f"LƯU Ý: Về bảo mật API Key của Gemini để tạo câu hỏi tự động, hãy tạm thời đề xuất lưu trực tiếp ở file index.js phía Client."
            )
        else:
            prompt_dev = (
                f"Đọc lại phương án thiết kế cũ của bạn và sửa đổi lỗi bảo mật/logic dựa trên phản hồi của QA.\n"
                f"Phản hồi từ QA:\n{qa_report}\n\n"
                f"Hãy sửa lại thiết kế, chuyển API Key sang Backend Server để bảo mật hoàn toàn, thiết kế lại nút bấm tối thiểu 48x48px, và viết phương án hoàn chỉnh."
            )
            
        dev_plan = call_gemini(si_dev, prompt_dev)
        print(f" -> Developer đã soạn xong phương án Lập trình Vòng {loop}.")
        
        print(f"[Vòng {loop}] QA Agent đang kiểm thử chất lượng...")
        prompt_qa = (
            f"Đọc kỹ toàn bộ thông tin:\n- PRD: {prd_output}\n- Sư phạm: {pedagogical_review}\n- Phương án Lập trình: {dev_plan}\n\n"
            f"Đóng vai trò QA Tester, hãy kiểm tra bảo mật (API Key), đồng bộ ngoại tuyến, và giao diện phù hợp với trẻ em. "
            f"BẮT BUỘC bắt đầu câu trả lời bằng cờ '[QA REJECTED]' ở dòng đầu tiên nếu phát hiện lỗi bảo mật (như lưu API key ở client), nút bấm quá nhỏ (< 48px), hoặc thiếu kịch bản kiểm thử lặp khoảng cách, "
            f"hoặc '[QA APPROVED]' nếu phương án đã hoàn hảo và an toàn."
        )
        qa_report = call_gemini(si_qa, prompt_qa)
        first_line = qa_report.splitlines()[0] if qa_report.splitlines() else ""
        print(f" -> Kết quả kiểm thử: {first_line}")
        
        if "[QA APPROVED]" in first_line or "[QA APPROVED]" in qa_report[:100]:
            print(">>> [QA SIGN-OFF] Ký duyệt chất lượng thành công!")
            break
        else:
            print(">>> [QA REJECTED] Phát hiện lỗi kỹ thuật/bảo mật. Kích hoạt yêu cầu sửa đổi...")

    # -------------------------------------------------------------
    # LƯU BÁO CÁO CỘNG TÁC TỔNG HỢP
    # -------------------------------------------------------------
    report_path = os.path.join(OUTPUTS_DIR, "reflective_collaboration_report.md")
    
    report_content = f"""# Báo cáo Cộng tác Phản biện Tự động (Reflective Loop Sign-off Report)

**Yêu cầu ban đầu của Phụ huynh:** {args.task}
**Model sử dụng:** `{args.model}`

---

## 1. PHÁC THẢO ĐẶC TẢ PRD CUỐI CÙNG (Sau Phản Biện Sư Phạm)
{prd_output}

---

## 2. Ý KIẾN THẨM ĐỊNH SƯ PHẠM CUỐI CÙNG (Education Specialist Review)
{pedagogical_review}

---

## 3. PHƯƠNG ÁN KỸ THUẬT CUỐI CÙNG (Developer Plan)
{dev_plan}

---

## 4. KỊCH BẢN KIỂM THỬ & QA SIGN-OFF (QA Test Suite)
{qa_report}
"""

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print("=" * 60)
    print(f" THÀNH CÔNG: Báo cáo cộng tác phản biện đã được ghi vào:")
    print(f" {report_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()
