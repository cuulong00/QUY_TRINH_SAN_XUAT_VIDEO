#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_infographic_reduction.py
=============================================================================
Execute the reduction of static infographics from 120 down to ~56 across all
7 chapters of 'tu-chu-duong-sat-cao-toc-bac-nam', converting concept slides
into dynamic B-Roll, Veo AI, and Forensic Callouts.
=============================================================================
"""

import os
import json
import re

EPISODE_DIR = "episodes/tu-chu-duong-sat-cao-toc-bac-nam"

# 1. Load audit entries
with open('audit_step_661.md', encoding='utf-8') as f:
    audit_text = f.read()

parsed_audit = {}
for l in audit_text.split('\n'):
    if l.startswith('| `CH') or l.startswith('| `'):
        parts = [p.strip() for p in l.split('|')]
        if len(parts) >= 6:
            sc_id = parts[1].strip('` ')
            dialogue = parts[2].strip('"\t ')
            curr_content = parts[3].strip()
            eval_type = parts[4].strip()
            proposal = parts[5].strip()
            
            action = 'KEEP'
            if 'B-ROLL' in proposal:
                action = 'TO_BROLL'
            elif 'VEO' in proposal:
                action = 'TO_VEO'
            elif 'FORENSIC' in proposal:
                action = 'TO_FORENSIC'
            elif 'HỢP NHẤT' in proposal:
                action = 'MERGE'
            else:
                action = 'KEEP'
                
            parsed_audit[sc_id] = {
                'dialogue': dialogue,
                'eval_type': eval_type,
                'proposal': proposal,
                'action': action
            }

# Manual overrides for Chapter 1 and 2 to match exact manifest IDs
ch1_map = {
    'CH01_SC003': ('KEEP', 'Đồng hồ đếm ngược tiến độ 9 tháng đàm phán'),
    'CH01_SC009': ('TO_BROLL', 'Flycam tuyến ven biển Hạ Long - Quảng Ninh và Cần Giờ'),
    'CH01_SC012': ('KEEP', 'Bản đồ 3D trục Bắc Nam 1.541 km tốc độ 350 km/h'),
    'CH01_SC013': ('MERGE', 'Hợp nhất số liệu 67,34 tỷ USD vào bản đồ SC012'),
    'CH01_SC014': ('TO_BROLL', 'Công trường thi công cẩu dầm bê tông đúc sẵn, tiến độ 2035'),
    'CH01_SC017': ('TO_VEO', 'Cận cảnh ánh mắt chiêm nghiệm của chuyên gia kiểm toán dưới ánh đèn bàn'),
    'CH01_SC019': ('TO_BROLL', 'Khung cảnh hội trường lễ ký kết hợp đồng, quan khách bắt tay'),
    'CH01_SC022': ('TO_BROLL', 'Hành khách lên xuống khoang tàu cao tốc êm ái, tiếp viên đường sắt'),
    'CH01_SC026': ('KEEP', 'Sơ đồ vòng đời công nghệ 50 năm: chuỗi phụ tùng và tương thích tín hiệu'),
    'CH01_SC028': ('TO_VEO', 'Sa bàn chiến lược với mô hình đoàn tàu và bản vẽ quy hoạch')
}

ch2_map = {
    'CH02_SC002': ('KEEP', 'Split-screen so sánh Nhà nước 67 tỷ USD vs Tư nhân VinSpeed'),
    'CH02_SC004': ('KEEP', 'Ma trận 4 ô vuông phân loại 4 mô hình tự chủ'),
    'CH02_SC006': ('TO_FORENSIC', 'Báo cáo nghiên cứu tiền khả thi của Chính phủ trình Quốc hội, mộc đỏ'),
    'CH02_SC011': ('TO_VEO', 'Mô hình đoàn tàu đặt trên bàn đàm phán cạnh tập tài liệu dày'),
    'CH02_SC014': ('TO_BROLL', 'Bản đồ quy hoạch đô thị ven biển và cảng biển hiện đại'),
    'CH02_SC019': ('TO_FORENSIC', 'Thỏa thuận hợp tác chiến lược THACO - Hyundai Rotem'),
    'CH02_SC022': ('TO_BROLL', 'Trụ sở Tổng công ty Đường sắt Việt Nam, 118 Lê Duẩn Hà Nội'),
    'CH02_SC024': ('KEEP', 'Bản đồ tuyến ray liên vận khổ 1.435mm Lào Cai - Hải Phòng'),
    'CH02_SC028': ('TO_BROLL', 'Đoàn tàu SE chạy qua đèo Hải Vân hoặc cầu Long Biên'),
    'CH02_SC029': ('KEEP', 'Sơ đồ nguy cơ phân mảnh tiêu chuẩn kỹ thuật 4 khối đường sắt'),
    'CH02_SC031': ('TO_BROLL', 'Kỹ sư làm việc tại xưởng Chu Lai, kèm Lower-third subscribe'),
    'CH02_SC033': ('TO_VEO', 'Bàn cờ chiến lược với 4 biểu tượng đại diện 4 mô hình')
}

master_mapping = {}
for k, v in ch1_map.items():
    master_mapping[k] = {'action': v[0], 'proposal': v[1]}
for k, v in ch2_map.items():
    master_mapping[k] = {'action': v[0], 'proposal': v[1]}
for k, v in parsed_audit.items():
    if any(k.startswith(f"CH{ch:02d}") for ch in range(3, 8)):
        master_mapping[k] = {'action': v['action'], 'proposal': v['proposal']}

print(f"Master mapping built for {len(master_mapping)} scenes.")

# Process chapter by chapter
for ch in range(1, 8):
    ch_str = f"{ch:02d}"
    print(f"\nProcessing Chapter {ch_str}...")
    
    # 1. Update infographics manifest
    info_path = os.path.join(EPISODE_DIR, f"infographics_manifest_chapter_{ch_str}.json")
    with open(info_path, encoding='utf-8') as f:
        old_info = json.load(f)
        
    new_info = []
    converted_to_broll = []
    converted_to_veo = []
    converted_to_forensic = []
    merged_items = []
    
    for item in old_info:
        sc_id = item['id']
        mapping = master_mapping.get(sc_id, {'action': 'KEEP', 'proposal': ''})
        action = mapping['action']
        proposal = mapping['proposal']
        
        if action == 'KEEP':
            # Mark it clearly as dynamic motion HUD so it is not a dead static slide!
            item['motion_type'] = 'dynamic_motion_hud_overlay'
            item['camera_drift'] = 'cinematic_drift_1.00x_to_1.03x'
            new_info.append(item)
        elif action == 'TO_BROLL':
            converted_to_broll.append((item, proposal))
        elif action == 'TO_VEO':
            converted_to_veo.append((item, proposal))
        elif action == 'TO_FORENSIC':
            converted_to_forensic.append((item, proposal))
        elif action == 'MERGE':
            merged_items.append((item, proposal))
            
    print(f"  Infographics: {len(old_info)} -> {len(new_info)} (kept). Converted: B-Roll={len(converted_to_broll)}, Veo={len(converted_to_veo)}, Forensic={len(converted_to_forensic)}, Merged={len(merged_items)}")
    
    # Save trimmed infographics manifest
    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(new_info, f, ensure_ascii=False, indent=2)
        
    # 2. Update B-Roll manifest
    broll_path = os.path.join(EPISODE_DIR, f"broll_manifest_chapter_{ch_str}.json")
    with open(broll_path, encoding='utf-8') as f:
        broll_data = json.load(f)
    existing_broll_ids = {x['id'] for x in broll_data}
    
    for it, prop in converted_to_broll:
        if it['id'] not in existing_broll_ids:
            broll_data.append({
                "id": it['id'],
                "text": it['text'],
                "duration": it.get('duration', "3.5s - 4.5s"),
                "core_visual_intent": prop,
                "target_channels": ["VTV24", "Truyền hình Nhân Dân", "Thaco Group", "Hoa Phat Group"],
                "flexible_search_terms": [
                    f"{prop} VTV24",
                    "Đường sắt tốc độ cao Bắc Nam thi công thực tế",
                    "Nhà máy cơ khí luyện kim Việt Nam"
                ],
                "visual_alternatives": [
                    f"Cảnh quay hiện trường thực tế: {prop}",
                    "Kỹ sư và công nhân làm việc tại phân xưởng"
                ],
                "forensic_fallback": f"Tư liệu thời sự báo chí về {prop}",
                "fair_use_transforms": "Cắt micro-cut 3.5s - 5.0s, scale 100%, áp Warm Documentary LUT, loại bỏ 100% audio gốc (-an), dán nhãn nguồn tư liệu"
            })
    with open(broll_path, 'w', encoding='utf-8') as f:
        json.dump(broll_data, f, ensure_ascii=False, indent=2)
        
    # 3. Update Forensic manifest
    forensic_path = os.path.join(EPISODE_DIR, f"forensic_manifest_chapter_{ch_str}.json")
    with open(forensic_path, encoding='utf-8') as f:
        forensic_data = json.load(f)
    existing_for_ids = {x['scene_id'] for x in forensic_data}
    
    for it, prop in converted_to_forensic:
        if it['id'] not in existing_for_ids:
            forensic_data.append({
                "scene_id": it['id'],
                "voiceover_quote": it['text'],
                "publication_source": "Văn bản Chính phủ / Báo Đầu Tư / CafeF",
                "article_headline_target": prop,
                "highlight_exact_text": it['text'],
                "highlight_style": "underline",
                "highlight_color": "#DC2626",
                "start_highlight_sec": 1.0,
                "end_highlight_sec": 3.5,
                "blur_editorial_photos": True,
                "sfx_path": "audio/sfx/paper_slide.wav"
            })
    with open(forensic_path, 'w', encoding='utf-8') as f:
        json.dump(forensic_data, f, ensure_ascii=False, indent=2)
        
    # 4. Update Veo Prompts text file
    veo_path = os.path.join(EPISODE_DIR, f"prompts_chapter_{ch_str}_veo.txt")
    with open(veo_path, encoding='utf-8') as f:
        veo_content = f.read()
        
    for it, prop in converted_to_veo:
        sc_id = it['id']
        if sc_id not in veo_content:
            veo_prompt_block = (
                f"\n\n{sc_id} [IMAGE]: sophisticated 2D cinematic editorial illustration, warm muted color palette, "
                f"luxurious deep slate and rich warm ivory cream tones (#F5F0E6, #1E293B), soft ambient amber glow, "
                f"burnished bronze accents, clean refined ink outlines, luminous high-clarity institutional lighting, "
                f"grounded human-centric warmth, dignified and authoritative atmosphere, approachable documentary aesthetic, "
                f"{prop}, 16:9\n"
                f"{sc_id} [VIDEO]: @{sc_id}.png -> preserving the warm muted cinematic palette, deep slate tones, "
                f"and refined editorial illustration style exactly, slow subtle cinematic camera movement, "
                f"soft ambient atmospheric dust motes, 8-second continuous video --ar 16:9 --dur 8s"
            )
            veo_content += veo_prompt_block
            
    with open(veo_path, 'w', encoding='utf-8') as f:
        f.write(veo_content.strip() + '\n')
        
    # 5. Update chapter_XX_visual_plus.md
    v_path = os.path.join(EPISODE_DIR, f"chapter_{ch_str}_visual_plus.md")
    with open(v_path, encoding='utf-8') as f:
        v_lines = f.readlines()
        
    new_v_lines = []
    for line in v_lines:
        new_line = line
        for it, prop in converted_to_broll:
            sc_id = it['id']
            if f"`{sc_id}`" in line or f"**{sc_id}**" in line:
                new_line = re.sub(r'`INFOGRAPHIC_DATA`', '`BROLL_REALITY`', new_line)
                new_line = re.sub(r'\*\*\[MODALITY\]:\*\* `INFOGRAPHIC_DATA`', '**[MODALITY]:** `BROLL_REALITY`', new_line)
        for it, prop in converted_to_veo:
            sc_id = it['id']
            if f"`{sc_id}`" in line or f"**{sc_id}**" in line:
                new_line = re.sub(r'`INFOGRAPHIC_DATA`', '`VEO_CINEMATIC`', new_line)
                new_line = re.sub(r'\*\*\[MODALITY\]:\*\* `INFOGRAPHIC_DATA`', '**[MODALITY]:** `VEO_CINEMATIC`', new_line)
        for it, prop in converted_to_forensic:
            sc_id = it['id']
            if f"`{sc_id}`" in line or f"**{sc_id}**" in line:
                new_line = re.sub(r'`INFOGRAPHIC_DATA`', '`FORENSIC_CALLOUT`', new_line)
                new_line = re.sub(r'\*\*\[MODALITY\]:\*\* `INFOGRAPHIC_DATA`', '**[MODALITY]:** `FORENSIC_CALLOUT`', new_line)
        for it, prop in merged_items:
            sc_id = it['id']
            if f"`{sc_id}`" in line or f"**{sc_id}**" in line:
                new_line = re.sub(r'`INFOGRAPHIC_DATA`', '`BROLL_INFRASTRUCTURE`', new_line)
                new_line = re.sub(r'\*\*\[MODALITY\]:\*\* `INFOGRAPHIC_DATA`', '**[MODALITY]:** `BROLL_INFRASTRUCTURE`', new_line)
        new_v_lines.append(new_line)
        
    with open(v_path, 'w', encoding='utf-8') as f:
        f.writelines(new_v_lines)

print("\nAll manifests and visual scripts updated successfully!")
