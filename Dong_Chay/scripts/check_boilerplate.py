#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dòng Chảy Visual Prompts Linter & Quality Audit Engine (S-Grade)
Tự động rà soát 6 Trụ Cột Chất Lượng của tệp prompt I2V:
1. Demographic & Geographic Anchor Gate (Chống Tây hóa nhân vật & sai địa lý)
2. Anti-Abstract Realism Gate (Triệt tiêu 100% biểu tượng trừu tượng vô hồn)
3. Language, Currency & Cinema Typography Gate (Cấm dấu tiếng Việt, cấm ký hiệu VND)
4. Dual-Line I2V Consistency & Action-Only Gate (Đúng cú pháp I2V, không lặp tả nhân vật ở video)
5. Boilerplate & Repetition Gate (Chống lặp từ rác, chống đứt gãy camera)
6. Mathematical Scene Density Gate (Chống gộp ẩu: N_scenes >= Words / 26)
"""

import os
import sys
import re
from collections import Counter

# Danh sách từ cấm trừu tượng
FORBIDDEN_ABSTRACT_METAPHORS = [
    r'\bchessboard\b', r'\bchess piece[s]?\b', r'\bbàn cờ\b',
    r'\b(?:financial|balance|weighing)\s+scale[s]?\b', r'\bcán cân\b',
    r'\bsafety razor\b', r'\brazor blade[s]?\b', r'\bdao cạo\b',
    r'\b(?:ceremonial|two-edged|double-edged)\s+sword[s]?\b', r'\bthanh kiếm\b',
    r'\binvisible\s+(?:wall|fortress|barrier)[s]?\b', r'\btường vô hình\b',
    r'\b(?:demand|product|sales|marketing|capital)\s+funnel[s]?\b', r'\bphễu\b',
    r'\bshattered stone barrier\b', r'\bfloating\s+(?:money|cash|dollar[s]?|currency)\b',
    r'\bburning\s+(?:money|cash|dollar[s]?)\b', r'\b(?:floating|flying|spinning)\s+gear[s]?\b',
    r'\bpuzzle\s+piece[s]?\b', r'\bjigsaw\b', r'\bfloating\s+pyramid\b',
    r'\bglowing\s+(?:floating\s+)?orb[s]?\b', r'\bfloating\s+crystal[s]?\b',
    r'\bmetaphoric\s+void\b', r'\bneon\s+glowing\s+matrix\b', r'\babstract\s+floating\b',
    r'\bglowing\s+floating\s+graph[s]?\b', r'\bpie\s+chart\s+floating\b'
]

# Danh sách từ cấm quân sự thô trong phân tích kinh tế
FORBIDDEN_MILITARY_WORDS = [
    r'\bbattlefield\b', r'\bbattleground\b', r'\bwarfare\b',
    r'\bwar\s+zone\b', r'\bsoldier[s]?\b', r'\barmy\b', r'\bcombat\b'
]

# Danh sách từ cấm vi phạm chủ quyền biển đảo (Đường lưỡi bò / Nine-dash line)
FORBIDDEN_SOVEREIGNTY_VIOLATIONS = [
    r'\bnine[\s-]?dash\s+line\b', r'\b9[\s-]?dash\s+line\b',
    r'\bten[\s-]?dash\s+line\b', r'\b10[\s-]?dash\s+line\b',
    r'\bu[\s-]?shaped\s+line\b', r'\bcow\s+tongue\s+line\b',
    r'\blưỡi\s+bò\b', r'\bđường\s+9\s+đoạn\b', r'\bđường\s+chín\s+đoạn\b'
]

# Danh sách từ chỉ nhân vật chung chung (nếu thiếu định danh chủng tộc sẽ cảnh báo)
GENERIC_PERSON_KEYWORDS = [
    r'\ba\s+man\b', r'\ba\s+woman\b', r'\ba\s+person\b', r'\bpeople\b',
    r'\ba\s+businessman\b', r'\ba\s+businesswoman\b', r'\ba\s+worker\b',
    r'\ban\s+engineer\b', r'\ban\s+executive\b', r'\ban\s+official\b',
    r'\ba\s+leader\b', r'\ba\s+driver\b', r'\ban\s+analyst\b', r'\ba\s+customer\b'
]

# Danh sách từ khóa định danh chủng tộc hợp lệ
VALID_ETHNICITY_KEYWORDS = [
    r'\bvietnamese\b', r'\bsoutheast asian\b', r'\beast asian\b',
    r'\basian\b', r'\bchinese\b', r'\bindian\b', r'\bjapanese\b',
    r'\bkorean\b', r'\binternational\b', r'\bcaucasian\b', r'\bwestern\b',
    r'\bdepicted in the reference image\b', r'\breference photo\b', r'\breference image\b'
]

def check_vietnamese_characters(text):
    """Phát hiện ký tự tiếng Việt có dấu trong prompt"""
    vn_chars_pattern = r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ]'
    return re.findall(vn_chars_pattern, text)

def analyze_prompts(file_path, chapter_script_path=None):
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' does not exist.")
        return False, {}

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    if not lines:
        print(f"❌ Error: File '{file_path}' is empty.")
        return False, {}

    total_lines = len(lines)
    print(f"📊 Đang rà soát kiểm toán {total_lines} dòng trong {os.path.basename(file_path)}...")

    descriptions = []
    ids = []
    
    # Error buckets
    demographic_errors = []
    environment_anchor_errors = []
    abstract_metaphor_errors = []
    military_errors = []
    typography_currency_errors = []
    vietnamese_char_errors = []
    action_only_video_errors = []
    id_rendering_errors = []
    mapping_errors = []
    transition_errors = []
    
    images_seen = set()
    videos_seen = set()

    for line in lines:
        # Match ID prefix: CHXX_SCYYY [IMAGE]: or CHXX_SCYYY [VIDEO]:
        match_id = re.match(r'^([A-Za-z0-9_]+)\s*(?:\[(IMAGE|VIDEO)\])?\s*:\s*(.*)', line)
        if not match_id:
            id_rendering_errors.append(("UNKNOWN", f"Dòng không đúng chuẩn tiền tố ID: '{line[:60]}...'"))
            continue

        current_id = match_id.group(1)
        mode = match_id.group(2) # "IMAGE" or "VIDEO"
        remaining_content = match_id.group(3).strip()
        
        full_key = f"{current_id}_{mode}" if mode else current_id
        ids.append(full_key)

        if mode == "IMAGE":
            images_seen.add(current_id)
            
            # Support character reference asset prefix: @ref.jpg -> desc
            match_img_ref = re.match(r'^@(?:reference_images/)?(\S+?)\s*->\s*(.*)', remaining_content, re.IGNORECASE)
            if match_img_ref:
                ref_img_file = match_img_ref.group(1).strip()
                desc_clean = match_img_ref.group(2).strip()
            else:
                desc_clean = remaining_content
            
            # 1. Trụ Cột 1A: Kiểm tra Environment Anchor Lock cho IMAGE
            # Hỗ trợ cả các từ khóa không gian kiến trúc/địa điểm thực chứng tự nhiên
            env_pattern = r'\b(?:set\s+(?:inside|at|in|on)|featuring|inside\s+a|inside|located\s+at|seated\s+at|standing\s+inside|positioned\s+beside|overlooking|facility|boardroom|cleanroom|headquarters|hall|venue|auditorium|office|factory|port|terminal|plant|center|corridor|room|lab|studio|warehouse)\b'
            if not re.search(env_pattern, desc_clean, re.IGNORECASE):
                environment_anchor_errors.append((current_id, f"IMAGE prompt thiếu Environment Anchor Lock ('set at...', 'set inside...', 'standing inside...', 'cleanroom...'). Dễ bị AI vẽ bối cảnh chung chung."))

            # 2. Trụ Cột 1B: Kiểm tra Demographic & Ethnicity Lock (Chống Tây hóa khi tả người)
            has_generic_person = any(re.search(pat, desc_clean, re.IGNORECASE) for pat in GENERIC_PERSON_KEYWORDS)
            has_ethnicity = any(re.search(pat, desc_clean, re.IGNORECASE) for pat in VALID_ETHNICITY_KEYWORDS)
            if has_generic_person and not has_ethnicity:
                demographic_errors.append((current_id, f"Mô tả nhân vật chung chung không có từ khóa nhân chủng học (thiếu 'Vietnamese', 'Southeast Asian', 'East Asian'...). Nguy cơ cao AI tự động sinh người Tây phương!"))

        elif mode == "VIDEO":
            videos_seen.add(current_id)
            
            # 3. Trụ Cột 4: Kiểm tra Action-Only & Tham chiếu cho VIDEO
            match_i2v = re.match(r'^@(?:reference_images/)?(\S+?)\s*->\s*(.*)', remaining_content, re.IGNORECASE)
            if not match_i2v:
                mapping_errors.append((current_id, f"VIDEO prompt thiếu cú pháp tham chiếu I2V '@{current_id}.png ->'"))
                desc_clean = remaining_content
            else:
                img_filename = match_i2v.group(1).strip()
                action_content = match_i2v.group(2).strip()
                # Clean trailing generation flags like --ar 16:9 --dur 8s
                desc_clean = re.sub(r'--(?:ar|dur)\s+\S+', '', action_content, flags=re.IGNORECASE).strip()
                img_id = os.path.splitext(img_filename)[0]
                if img_id.lower() != current_id.lower():
                    mapping_errors.append((current_id, f"ID ảnh tham chiếu '{img_id}' không khớp ID dòng '{current_id}'!"))
                
                # Kiểm tra lặp mô tả nhân vật chi tiết trong Video prompt
                if re.search(r'\b(?:A Vietnamese|A Southeast Asian|An East Asian|A Chinese|An Indian)\s+(?:man|woman|worker|engineer|official|executive|leader)\s+(?:wearing|in his|in her)\b', action_content, re.IGNORECASE):
                    action_only_video_errors.append((current_id, f"VIDEO prompt vi phạm quy tắc Action-Only (tự ý miêu tả lại nhân vật/trang phục thay vì gọi 'The man in the image' / 'The engineer')."))
        else:
            desc_clean = remaining_content

        # 4. Trụ Cột 2: Triệt tiêu Ẩn Dụ Trừu Tượng
        found_abstract = []
        for pat in FORBIDDEN_ABSTRACT_METAPHORS:
            m = re.findall(pat, desc_clean, re.IGNORECASE)
            if m:
                found_abstract.extend(m)
        if found_abstract:
            abstract_metaphor_errors.append((current_id, f"Chứa biểu tượng trừu tượng cấm {found_abstract}! Bắt buộc quy đổi sang bối cảnh thực chứng ngoài đời."))

        # Kiểm tra từ quân sự thô
        found_mil = []
        for pat in FORBIDDEN_MILITARY_WORDS:
            m = re.findall(pat, desc_clean, re.IGNORECASE)
            if m:
                found_mil.extend(m)
        if found_mil:
            military_errors.append((current_id, f"Chứa từ ẩn dụ quân sự thô {found_mil}. Hãy thay bằng 'commercial market', 'strategic arena'."))

        # Kiểm tra vi phạm chủ quyền biển đảo (Đường lưỡi bò)
        for pat in FORBIDDEN_SOVEREIGNTY_VIOLATIONS:
            m = re.findall(pat, desc_clean, re.IGNORECASE)
            if m:
                typography_currency_errors.append((current_id, f"VI PHẠM NGHIÊM TRỌNG CHỦ QUYỀN BIỂN ĐẢO: Chứa cụm từ {m}! TUYỆT ĐỐI CẤM nhắc đến hoặc tạo ra đường lưỡi bò."))

        # 5. Trụ Cột 3: Tiếng Việt có dấu & Ký hiệu VND
        vn_chars = check_vietnamese_characters(desc_clean)
        if vn_chars:
            vietnamese_char_errors.append((current_id, f"Chứa ký tự tiếng Việt có dấu: {set(vn_chars)}"))

        if re.search(r'\b(?:VND|VNĐ)\b', desc_clean):
            typography_currency_errors.append((current_id, f"Chứa ký hiệu tiền tệ 'VND'/'VNĐ'. Phải dùng số thuần túy hoặc 'local currency'/'USD'."))

        # Check raw ID inside text
        raw_id_matches = re.findall(r'\b(?:CH\d+_SC\d+[a-z0-9_]*|SC\d+[a-z0-9_]*)\b', desc_clean, re.IGNORECASE)
        raw_id_matches = [m for m in raw_id_matches if m.lower() != current_id.lower()]
        if raw_id_matches:
            id_rendering_errors.append((current_id, f"Chứa mã ID {raw_id_matches} trong phần tả cảnh, AI sẽ vẽ nhầm mã lên video!"))

        # Check meta words
        meta_matches = re.findall(r'\b(?:previous scene|next scene|former scene|cảnh trước|cảnh sau)\b', desc_clean, re.IGNORECASE)
        if meta_matches:
            id_rendering_errors.append((current_id, f"Chứa từ tham chiếu phi vật lý {meta_matches}."))

        # Clean camera movements for duplicate check
        desc_dup_check = re.sub(
            r'^(?:Starting with[^,]+,\s*)?(?:Starting from[^,]+,\s*)?(?:slow camera panning right showing|steady shot showing|subtle slow zoom-in showing|steady medium shot showing|the camera pans right showing|camera slowly zooms out|the camera pans down|a slow camera panning showing)\s+',
            '', desc_clean, flags=re.IGNORECASE
        ).strip()
        descriptions.append((full_key, desc_dup_check))

    # Verify I2V Pairing
    for img_id in images_seen:
        if img_id not in videos_seen:
            mapping_errors.append((img_id, f"Có prompt [IMAGE] nhưng thiếu prompt [VIDEO] tương ứng."))
    for vid_id in videos_seen:
        if vid_id not in images_seen:
            mapping_errors.append((vid_id, f"Có prompt [VIDEO] nhưng thiếu prompt [IMAGE] tương ứng."))

    # Duplicates & Boilerplate Check
    desc_only = [item[1] for item in descriptions]
    desc_counter = Counter(desc_only)
    duplicates = {k: v for k, v in desc_counter.items() if v > 1}

    boilerplates = [
        "representing the shadow financial system",
        "in a dark space representing",
        "glowing digital paths representing",
        "transaction flows on a dark grid",
        "massive brick bank vault door"
    ]
    boilerplate_counts = {}
    for bp in boilerplates:
        count = sum(1 for line in lines if bp.lower() in line.lower())
        boilerplate_counts[bp] = (count, round(count / max(total_lines, 1) * 100, 1))

    severe_duplicates = any(v > 2 for v in duplicates.values())
    severe_boilerplate = any(pct > 10.0 for _, (_, pct) in boilerplate_counts.items())

    # Check Scene Density against original script
    script_density_error = False
    word_count = 0
    unique_scenes_count = len(images_seen | videos_seen)
    min_required_scenes = 0

    if not chapter_script_path and len(sys.argv) >= 3:
        chapter_script_path = sys.argv[2]
    elif not chapter_script_path:
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        match_ch = re.search(r'prompts_(?:ch|chapter_)?(\d+)\.txt', base_name, re.IGNORECASE)
        if match_ch:
            ch_num = match_ch.group(1).zfill(2)
            candidate = os.path.join(dir_name, f"chapter_{ch_num}.md")
            if not os.path.exists(candidate):
                candidate = os.path.join(dir_name, f"chapter_{match_ch.group(1)}.md")
            if os.path.exists(candidate):
                chapter_script_path = candidate

    if chapter_script_path and os.path.exists(chapter_script_path):
        with open(chapter_script_path, "r", encoding="utf-8") as sf:
            script_text = sf.read()
        script_text_clean = re.sub(r'#.*', '', script_text)
        words = script_text_clean.split()
        word_count = len(words)
        min_required_scenes = int(word_count / 26.0)
        if unique_scenes_count < min_required_scenes:
            script_density_error = True

    # Build Audit Scorecard Matrix
    pillars = [
        {
            "id": 1,
            "name": "Demographic & Geographic Anchor",
            "desc": "Khóa nhân chủng học (Vietnamese/Asian) & Khóa địa danh môi trường (set at...)",
            "errors": len(demographic_errors) + len(environment_anchor_errors),
            "details": demographic_errors + environment_anchor_errors
        },
        {
            "id": 2,
            "name": "Anti-Abstract Realism",
            "desc": "Triệt tiêu 100% biểu tượng trừu tượng (bàn cờ, cán cân, phễu, bánh răng trôi nổi)",
            "errors": len(abstract_metaphor_errors) + len(military_errors),
            "details": abstract_metaphor_errors + military_errors
        },
        {
            "id": 3,
            "name": "Language & Cinema Typography",
            "desc": "100% Tiếng Anh, không dấu tiếng Việt, không ký hiệu VND, text định vị rõ",
            "errors": len(vietnamese_char_errors) + len(typography_currency_errors) + len(id_rendering_errors),
            "details": vietnamese_char_errors + typography_currency_errors + id_rendering_errors
        },
        {
            "id": 4,
            "name": "Dual-Line I2V Consistency",
            "desc": "Cặp đôi [IMAGE] & [VIDEO], Action-only video motion, ID đồng bộ 100%",
            "errors": len(mapping_errors) + len(action_only_video_errors),
            "details": mapping_errors + action_only_video_errors
        },
        {
            "id": 5,
            "name": "Boilerplate & Camera Continuity",
            "desc": "Không lặp cụm từ rác, camera matched movement mượt mà không gãy đoạn",
            "errors": (1 if severe_duplicates else 0) + (1 if severe_boilerplate else 0),
            "details": [("DUPLICATE", "Lặp mô tả quá 2 lần")] if severe_duplicates else []
        },
        {
            "id": 6,
            "name": "Mathematical Scene Density",
            "desc": f"Mật độ cảnh chuẩn xác N_scenes ({unique_scenes_count}) >= Words/26 ({min_required_scenes})",
            "errors": 1 if script_density_error else 0,
            "details": [(f"DENSITY_FAIL", f"Cần tối thiểu {min_required_scenes} cảnh, chỉ có {unique_scenes_count} cảnh")] if script_density_error else []
        }
    ]

    total_errors = sum(p["errors"] for p in pillars)
    is_valid = (total_errors == 0)

    print("\n" + "="*80)
    print("📋 BẢNG ĐÁNH GIÁ KIỂM TOÁN CHẤT LƯỢNG PROMPT (6-PILLAR AUDIT SCORECARD)")
    print("="*80)
    print(f"| {'Trụ Cột Kiểm Toán':<35} | {'Tiêu Chuẩn Đạt Chuẩn':<25} | {'Lỗi':<5} | {'Kết Quả':<10} |")
    print("|" + "-"*37 + "|" + "-"*27 + "|" + "-"*7 + "|" + "-"*12 + "|")
    for p in pillars:
        status_str = "✅ PASS" if p["errors"] == 0 else f"❌ FAIL ({p['errors']})"
        print(f"| {p['name']:<35} | {p['desc'][:25]:<25} | {p['errors']:<5} | {status_str:<10} |")
    print("="*80)

    if not is_valid:
        print("\n🔍 CHI TIẾT CÁC LỖI CẦN SỬA ĐỔI:")
        for p in pillars:
            if p["errors"] > 0:
                print(f"\n👉 Trụ Cột {p['id']}: {p['name']}")
                for scene_id, msg in p["details"][:10]:
                    print(f"   • [{scene_id}]: {msg}")
        print("\n⚠️ YÊU CẦU: Tinh chỉnh lại các prompt bị lỗi trước khi bàn giao!")
    else:
        print("\n🎉 TUYỆT VỜI! Tệp prompt đạt chuẩn 100% PASS — KHÔNG CÒN BẤT KỲ LỖI NÀO!")
        print("Tất cả nhân vật đã được khóa nhân chủng học, bối cảnh thực chứng 100%, không trừu tượng, I2V chuẩn xác.")

    return is_valid, {
        "pillars": pillars,
        "total_errors": total_errors,
        "unique_scenes_count": unique_scenes_count,
        "min_required_scenes": min_required_scenes,
        "word_count": word_count
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python3 check_boilerplate.py <đường_dẫn_prompts_chXX.txt> [đường_dẫn_chapter_XX.md]")
        sys.exit(1)
        
    target_file = sys.argv[1]
    script_file = sys.argv[2] if len(sys.argv) >= 3 else None
    success, stats = analyze_prompts(target_file, script_file)
    if not success:
        sys.exit(1)
    sys.exit(0)
