#!/usr/bin/env python3
"""
Tri-Track Manifest Exporter for I2V+ Multimodal Pipeline (Dong Chay)
Parses chapter_XX_visual_plus.md and generates:
1. prompts_chapter_XX_veo.txt (Google Flow / Veo 3.1 Lite)
2. broll_manifest_chapter_XX.json (FootageHunter Fair Use)
3. infographics_manifest_chapter_XX.json (AutoCapCut / Motion Graphics)
"""

import os
import re
import json
import sys

def parse_and_export(ch_num, episode_dir):
    ch_str = f"{ch_num:02d}"
    vis_path = os.path.join(episode_dir, f"chapter_{ch_str}_visual_plus.md")
    
    if not os.path.exists(vis_path):
        print(f"File not found: {vis_path}")
        return False
        
    with open(vis_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Split by scenes: "### [CHXX_SCYYY]" or "### [CHXX_SCYYYa1]"
    blocks = re.split(r"(?=###\s*\[CH\d+_SC\d+[a-z0-9]*\])", content)
    
    veo_prompts = []
    broll_manifest = []
    infographics_manifest = []
    info_prompts = []
    
    for b in blocks:
        b = b.strip()
        if not b.startswith("### ["):
            continue
            
        m_id = re.search(r"###\s*\[(CH\d+_SC\d+[a-z0-9]*)\]", b)
        if not m_id:
            continue
        sid = m_id.group(1)
        
        m_thoai = re.search(r"-\s*\*\*Thoại:\*\*\s*\"?([^\n\"]+)\"?", b)
        m_mod = re.search(r"-\s*\*\*Modality:\*\*\s*`\[([A-Z_]+)\]`", b)
        m_overlay = re.search(r"-\s*\*\*Text Overlay:\*\*\s*([^\n]+)", b)
        
        thoai = m_thoai.group(1).strip() if m_thoai else ""
        modality = m_mod.group(1).strip() if m_mod else "VEO_AI"
        overlay = m_overlay.group(1).strip() if m_overlay else "Không"
        
        if modality == "VEO_AI":
            m_boi = re.search(r"-\s*\*\*Bối cảnh đời thực:\*\*\s*([^\n]+)", b)
            m_chu = re.search(r"-\s*\*\*Chủ thể & Hành động an toàn:\*\*\s*([^\n]+)", b)
            m_cam = re.search(r"-\s*\*\*Camera & Điện ảnh:\*\*\s*([^\n]+)", b)
            
            bdesc = m_boi.group(1).strip() if m_boi else ""
            cact = m_chu.group(1).strip() if m_chu else ""
            cam = m_cam.group(1).strip() if m_cam else "Cinematic slow camera movement."
            
            # Format Veo image & video prompt
            # Check text overlay rule: If overlay present, ensure Steady camera shot in video
            has_overlay = overlay.strip(" .`'\"").lower() not in ["không", "khong", "none", "no", ""]
            steady_cam = "Steady camera shot with gentle subtle motion" if has_overlay else cam
            
            # English translation / synthesis for prompt
            img_prompt = f"A 2D warm cinematic editorial illustration. {bdesc} {cact} Color palette: warm ivory cream ambient tone (#FAF7EE), sophisticated modern slate (#1E293B, #2A323D), accented with emerald green (#10B981) and amber (#F59E0B). Clean bold ink outlines, stylized flat vector textures, luminous high-clarity editorial lighting."
            if has_overlay:
                clean_text = overlay.replace("BOTTOM LEFT | ", "").strip(" .`'\"")
                img_prompt += f' Bold graphic text "{clean_text}" positioned fixedly in the lower-left area of the frame, elevated 25% above the bottom edge, facing camera directly, perfectly horizontal.'
                
            vid_prompt = f"{steady_cam}, smooth subtle motion, maintaining clean editorial outlines, stable lighting, crisp atmospheric depth."
            
            veo_prompts.append(f"{sid} [IMAGE]: {img_prompt}")
            veo_prompts.append(f"{sid} [VIDEO]: {vid_prompt}\n")
            
        elif modality == "B_ROLL_REAL":
            m_tu = re.search(r"-\s*\*\*Tư liệu thời sự / Lịch sử:\*\*\s*([^\n]+)", b)
            m_q = re.search(r"-\s*\*\*Từ khóa tìm kiếm \(Search Query\):\*\*\s*\"?([^\n\"]+)\"?", b)
            m_src = re.search(r"-\s*\*\*Nguồn báo chí uy tín \(Source\):\*\*\s*([^\n]+)", b)
            m_req = re.search(r"-\s*\*\*Yêu cầu xử lý Fair Use:\*\*\s*([^\n]+)", b)
            
            broll_manifest.append({
                "scene_id": sid,
                "thoai": thoai,
                "description": m_tu.group(1).strip() if m_tu else "",
                "search_query": m_q.group(1).strip() if m_q else "",
                "source_recommendation": m_src.group(1).strip() if m_src else "",
                "fair_use_processing": m_req.group(1).strip() if m_req else "Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn.",
                "text_overlay": overlay
            })
            
        elif modality == "INFOGRAPHIC_DATA":
            m_type = re.search(r"-\s*\*\*Loại đồ họa \(Chart Type\):\*\*\s*([^\n]+)", b)
            m_title = re.search(r"-\s*\*\*Tiêu đề & Dữ liệu cốt lõi:\*\*\s*([^\n]+)", b)
            m_layout = re.search(r"-\s*\*\*Cấu trúc phân tầng & Bố cục:\*\*\s*([^\n]+)", b)
            m_pal = re.search(r"-\s*\*\*Bảng màu & Hiệu ứng chuyển động:\*\*\s*([^\n]+)", b)
            
            infographics_manifest.append({
                "scene_id": sid,
                "thoai": thoai,
                "chart_type": m_type.group(1).strip() if m_type else "",
                "core_data_and_title": m_title.group(1).strip() if m_title else "",
                "layout_hierarchy": m_layout.group(1).strip() if m_layout else "",
                "palette_and_animation": m_pal.group(1).strip() if m_pal else "",
                "text_overlay": overlay
            })
            
            # Format prompt for Google Flow Nano Banana 2
            ctype = m_type.group(1).strip() if m_type else "Financial Data Card"
            cdesc = m_title.group(1).strip() if m_title else ""
            clayout = m_layout.group(1).strip() if m_layout else ""
            has_overlay = overlay.strip(" .`'\"").lower() not in ["không", "khong", "none", "no", ""]
            clean_text = overlay.replace("BOTTOM LEFT | ", "").strip(" .`'\"") if has_overlay else ""
            
            info_prompt = f"A 2D high-clarity technical financial infographic card depicting a {ctype}. Visualizing key macroeconomic and land-rent data ({cdesc}). Layout structure: {clayout}. Color palette: Canonical Slate (#1E293B, #2A323D), Warm Ivory (#FAF7EE), Glowing Amber (#F59E0B), Emerald Green (#10B981), Coral Red (#EF5350). Minimalist graphic novel aesthetic, clean bold ink outlines, crisp typography, luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows, no watermarks, 16:9"
            if has_overlay and clean_text:
                info_prompt += f' Bold graphic text "{clean_text}" positioned fixedly in the lower-left area of the frame, elevated 25% above the bottom edge, facing camera directly, perfectly horizontal.'
            
            info_prompts.append(f"{sid} [IMAGE]: {info_prompt}\n")
            
    # Write output files
    veo_out = os.path.join(episode_dir, f"prompts_chapter_{ch_str}_veo.txt")
    broll_out = os.path.join(episode_dir, f"broll_manifest_chapter_{ch_str}.json")
    info_out = os.path.join(episode_dir, f"infographics_manifest_chapter_{ch_str}.json")
    info_txt_out = os.path.join(episode_dir, f"prompts_chapter_{ch_str}_infographics.txt")
    
    with open(veo_out, "w", encoding="utf-8") as f:
        f.write("\n".join(veo_prompts) + "\n")
        
    with open(broll_out, "w", encoding="utf-8") as f:
        json.dump(broll_manifest, f, ensure_ascii=False, indent=2)
        
    with open(info_out, "w", encoding="utf-8") as f:
        json.dump(infographics_manifest, f, ensure_ascii=False, indent=2)

    with open(info_txt_out, "w", encoding="utf-8") as f:
        f.write(f"# DANH MỤC ĐẶC TẢ ĐỒ HỌA SỐ LIỆU & INFOGRAPHICS (FLOW IMAGE-ONLY) — CHƯƠNG {ch_str}\n")
        f.write(f"# TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ (DÒNG CHẢY)\n")
        f.write("# BẢNG MÀU: Nền Slate (#1E293B, #2A323D) | Nền Ngà Kem (#FAF7EE) | Hổ Phách (#F59E0B) | Xanh Lục Ngọc (#10B981) | Đỏ San Hô (#EF5350) | 16:9\n\n")
        f.write("\n".join(info_prompts) + "\n")
        
    print(f"Exported Chapter {ch_str}:")
    print(f"  - Veo Prompts: {len(veo_prompts)//2} scenes -> {veo_out}")
    print(f"  - B-Roll Manifest: {len(broll_manifest)} items -> {broll_out}")
    print(f"  - Infographics Manifest: {len(infographics_manifest)} items -> {info_out}")
    print(f"  - Infographics Prompts: {len(info_prompts)} scenes -> {info_txt_out}")
    return True

if __name__ == "__main__":
    ep_dir = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/san-golf-lo-co-may-ngon-dat"
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        parse_and_export(int(sys.argv[1]), ep_dir)
    else:
        for c in range(1, 9):
            parse_and_export(c, ep_dir)
