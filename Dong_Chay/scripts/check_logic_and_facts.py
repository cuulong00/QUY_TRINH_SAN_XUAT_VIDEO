#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_logic_and_facts.py — Script Kiểm Toán Tự Động: Độ Dài Câu, Từ Ngữ Hàn Lâm & Khóa Dữ Liệu
Kiểm tra kịch bản kịch bản thoại (chapter_XX.md) theo chuẩn DNA Mới của Dòng Chảy:
1. Độ dài câu thoại: Tối đa 120 ký tự (lý tưởng 80-100 ký tự).
2. Từ ngữ hàn lâm / dịch máy bị cấm: Triệt tiêu ngôn từ sáo rỗng.
3. Nguyên tắc Analogy: Kiểm tra các thuật ngữ chuyên ngành có kèm giải thích dân dã không.
"""

import sys
import os
import re

FORBIDDEN_JARGON = [
    "sự bất cân xứng của cơ chế",
    "cơ chế điều tiết mang tính",
    "hệ quả tất yếu của quá trình",
    "suy thoái cấu trúc tính toán",
    "đây là phần quan trọng nhất",
    "người quan sát cho rằng",
    "giới chuyên gia nhận định rằng",
    "những cái mà",
    "nhằm mục đích để",
]

FORBIDDEN_ENDING_ANNOUNCES = [
    "câu trả lời nằm ở",
    "đó là căn bệnh",
    "đó là một căn bệnh",
    "đó là cơn bão",
    "đó là ngành",
    "đó là canh bạc",
    "chúng ta sẽ tìm hiểu",
    "sẽ được giải mã ở chương sau",
    "hãy cùng đón xem",
]

FORBIDDEN_OPENING_PATTERNS = [
    "để hiểu được",
    "để đánh giá đúng",
    "như chúng ta đã thấy",
    "như đã phân tích",
    "như đã nói ở trên",
    "như đã trình bày",
]

MANDATORY_ANALOGY_TERMS = {
    "bẫy thanh khoản": ["két sắt", "thừa tiền", "không chảy", "ngân hàng thừa", "tiền rẻ"],
    "suy thoái bảng cân đối": ["trả nợ", "co cụm", "không dám vay", "hầu bao"],
    "điều 75": ["75%", "cắt lương", "nghỉ luân phiên", "tắt đèn"],
    "nợ nhóm 2": ["nguy cơ", "ngấp nghé", "trễ hạn", "lo sợ"],
    "tfr": ["sinh con", "trẻ em", "kết hôn", "con/phụ nữ"],
}

def check_chapter(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File không tồn tại: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = [line.strip() for line in content.split("\n") if line.strip()]
    
    print(f"\n" + "="*80)
    print(f"🔍 KIỂM TOÁN CHẤT LƯỢNG DNA VĂN PHONG: {os.path.basename(file_path)}")
    print("="*80)

    # 1. Kiểm tra tiêu đề / visual cue cấm
    forbidden_markers = ["# chapter", "[visual cue]", "[sound cue]", "toàn cảnh video", "tuyên bố sẵn sàng"]
    marker_errors = []
    for line_idx, line in enumerate(lines, 1):
        for marker in forbidden_markers:
            if marker in line.lower():
                marker_errors.append(f"Dòng {line_idx}: Chứa nhãn vận hành cấm '{marker}'")

    # 2. Tách câu và kiểm tra độ dài câu (< 120 ký tự)
    # Tách bằng dấu chấm, chấm hỏi, chấm than theo sau là khoảng trắng hoặc cuối dòng
    sentences = re.split(r'(?<=[.?!])\s+', content)
    long_sentences = []
    for s_idx, sentence in enumerate(sentences, 1):
        s_clean = sentence.strip().replace("\n", " ")
        if len(s_clean) > 120:
            long_sentences.append((len(s_clean), s_clean))

    # 3. Kiểm tra từ ngữ hàn lâm / dịch máy cấm
    jargon_errors = []
    content_lower = content.lower()
    for jargon in FORBIDDEN_JARGON:
        if jargon in content_lower:
            jargon_errors.append(f"Chứa từ ngữ hàn lâm/sáo rỗng: '{jargon}'")

    # 4. Kiểm tra quy tắc Analogy cho thuật ngữ chuyên môn
    missing_analogies = []
    for term, keywords in MANDATORY_ANALOGY_TERMS.items():
        if term in content_lower:
            has_analogy = any(kw in content_lower for kw in keywords)
            if not has_analogy:
                missing_analogies.append(f"Xuất hiện thuật ngữ '{term}' nhưng thiếu câu ví von / giải thích dân dã đi kèm.")

    # 5. Kiểm tra quy chuẩn Đóng - Mở chương (Chapter Boundary & Anti-Announce)
    boundary_errors = []
    if len(sentences) >= 2:
        last_two = " ".join([s.lower() for s in sentences[-2:]])
        for phrase in FORBIDDEN_ENDING_ANNOUNCES:
            if phrase in last_two:
                boundary_errors.append(f"Cuối chương mắc bệnh Báo đề: chứa cụm từ thông báo cấm '{phrase}'")
        
        first_two = " ".join([s.lower() for s in sentences[:2]])
        for phrase in FORBIDDEN_OPENING_PATTERNS:
            if phrase in first_two:
                boundary_errors.append(f"Đầu chương mở đầu kiểu hành chính: chứa cụm từ cấm '{phrase}'")

    # In kết quả kiểm toán
    total_sentences = len(sentences)
    failed = False

    print(f"\n📊 1. KIỂM SOÁT ĐỘ DÀI CÂU THOẠI (Ngưỡng tối đa: 120 ký tự)")
    print(f"   • Tổng số câu thoại: {total_sentences}")
    if long_sentences:
        print(f"   ⚠️ Phát hiện {len(long_sentences)} câu dài vượt 120 ký tự:")
        for length, s in long_sentences[:5]:
            print(f"     - [{length} ký tự]: \"{s[:80]}...\"")
        if len(long_sentences) > 5:
            print(f"     ... và {len(long_sentences) - 5} câu khác.")
        failed = True
    else:
        print(f"   ✅ 100% câu thoại thỏa mãn chuẩn < 120 ký tự (Đạt chuẩn nghe bằng tai tối thượng)!")

    print(f"\n📚 2. KIỂM SOÁT TỪ NGỮ HÀN LÂM / DỊCH MÁY")
    if jargon_errors:
        for err in jargon_errors:
            print(f"   ❌ {err}")
        failed = True
    else:
        print(f"   ✅ Không phát hiện từ ngữ hàn lâm sáo rỗng. Văn phong thuần Việt, sắc bén!")

    print(f"\n💡 3. KIỂM TRA NGUYÊN TẮC ANALOGY (Đại chúng hóa thuật ngữ)")
    if missing_analogies:
        for err in missing_analogies:
            print(f"   ⚠️ {err}")
        failed = True
    else:
        print(f"   ✅ Các thuật ngữ phức tạp đều có phép ví von / diễn giải đời thường đi kèm!")

    print(f"\n🎬 4. KIỂM SOÁT ĐÓNG - MỞ CHƯƠNG & CHỐNG BÁO ĐỀ (Boundary Architecture)")
    if boundary_errors:
        for err in boundary_errors:
            print(f"   ❌ {err}")
        failed = True
    else:
        print(f"   ✅ Đóng - mở chương chuẩn điện ảnh: Không báo đề, không lặp đề, mở đầu trực diện!")

    print(f"\n🛡️ 5. KIỂM SOÁT NHÃN VẬN HÀNH & KỊCH BẢN THOẠI SẠCH")
    if marker_errors:
        for err in marker_errors:
            print(f"   ❌ {err}")
        failed = True
    else:
        print(f"   ✅ Kịch bản thoại sạch 100%, không lẫn tiêu đề hay cues hình ảnh!")

    print("\n" + "="*80)
    if failed:
        print(f"🚨 KẾT QUẢ KIỂM TOÁN: FAILED — Cần chỉnh sửa lại câu dài hoặc từ ngữ trước khi bàn giao.")
        print("="*80 + "\n")
        return False
    else:
        print(f"🏆 KẾT QUẢ KIỂM TOÁN: 100% PASS — ĐẠT CHUẨN BIÊN KỊCH QUÁI KIỆT & GURU DNA!")
        print("="*80 + "\n")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python3 scripts/check_logic_and_facts.py <đường_dẫn_chapter_XX.md>")
        sys.exit(1)
    check_chapter(sys.argv[1])
