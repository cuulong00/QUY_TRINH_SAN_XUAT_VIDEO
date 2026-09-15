#!/usr/bin/env python3
import os

def main():
    video_prompts_path = "/Users/pro16/Documents/VideoProject/Dòng Chảy/episodes/showbiz_drugs_economics/video_prompts.txt"
    master_prompts_path = "/Users/pro16/Documents/VideoProject/Dòng Chảy/episodes/showbiz_drugs_economics/prompts_master.txt"
    
    # 1. Read existing video prompts
    if not os.path.exists(video_prompts_path):
        print(f"Error: {video_prompts_path} not found.")
        return
        
    with open(video_prompts_path, "r", encoding="utf-8") as f:
        video_prompts_content = f.read()
        
    # 2. Define high-quality image prompts (5-layer Dòng Chảy Comic style)
    image_prompts_header = """================================================================================
🎨 DÒNG CHẢY IMAGE PROMPTS (PROMPT TẠO ẢNH TĨNH - INFOGRAPHICS & METAPHORS)
================================================================================
Sử dụng các prompt dưới đây trên Midjourney, Grok, Imagen 4 hoặc DALL-E 3 để tạo ảnh tĩnh 16:9.
Mọi prompt đã được tối ưu hóa theo Phong cách Hoạt hình 2D Hiện đại / Editorial Cartoon của kênh.

--------------------------------------------------------------------------------
1. PHÉP SO SÁNH ĐỘC BẢN (Nhà máy vs Ngôi sao - Chapter 1)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a split-screen infographic. On the left side: a busy modern factory with smoke coming from chimneys and a bright green arrow pointing upwards. On the right side: a torn advertising poster of a celebrity star face crossed out with a red 'X', and a bright red arrow pointing downwards to zero. Clean minimalist tech office background. Bright studio lighting with high contrast. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
2. SƠ ĐỒ TAM GIÁC BẤT ĐỐI XỨNG THÔNG TIN (Chapter 1)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a triangular flowchart network on a dark digital screen. The vertices of the triangle represent 'Nhãn hàng' (Brand), 'Nghệ sĩ' (Celebrity), and 'Người tiêu dùng' (Consumer) with glowing text labels in Vietnamese. A jagged, broken red line representing 'Thông tin bất đối xứng' (Information Asymmetry) splits the center of the triangle. Neon amber ambient light. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
3. BẢNG HIỆU NGƯỜI ĐẠI DIỆN BỊ XÓA BỎ TRÊN PHỐ (Chapter 2)
--------------------------------------------------------------------------------
Prompt:
A WIDE STILL SHOT showing a busy Vietnamese street scene in front of a modern fashion store. A customer with Asian features stands outside, looking up at a giant billboard sign showing a celebrity's face covered with a large red 'X'. Pedestrians walk past. Sunny day lighting with sharp shadows. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
4. BIỂU ĐỒ CHỨNG KHOÁN - PHẢN ỨNG 24H-48H (Chapter 2)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a large dark digital screen displaying two line charts. A bright green line rises sharply and is labeled '+2.10% (Stabilized at 24h-48h)' in clean sans-serif text. A bright red line plunges downwards and is labeled '-1.88% (Delayed reaction)' in clean red text. Clean corporate boardroom background. Neon green and red ambient glow. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
5. CÁN CÂN PROPOFOL ĐỐI XỨNG (70 triệu vs 10 tỷ Won - Chapter 3)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a large retro mechanical balance scale. On the left pan of the scale sits a small single glass ampoule of propofol with a light green label marked '70M Won', while on the right pan of the scale sits a massive towering pile of glowing gold bricks and glass ampoules of propofol with a large red label marked '10B Won' tipping the scale heavily downwards on the right side. Dark minimalist digital abstract space with glowing neon green grid lines on the floor. Dramatic chiaroscuro lighting with sharp cyan and amber rim lights casting long shadows. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
6. VÒNG XOÁY ÁP LỰC Q-SCORE (Chapter 3)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a circular neon feedback loop flow chart. The flow chart has four circular nodes with Vietnamese text labels: 'Áp lực Q-Score' (Q-Score Pressure), 'Chất kích thích' (Substances), 'Rủi ro pháp lý' (Legal Risks), and 'Suy giảm Q-Score' (Declining Q-Score). Arrows connect them in a toxic spiral loop. Dark background with a faint glowing grid. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
7. SO SÁNH ĐIỀU KHOẢN ĐẠO ĐỨC TRƯỚC / SAU (Chapter 4)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a comparison table on a screen. The left column is labeled 'Morals Clause Cũ' (Old Morals Clause) in faded white text and describes vague moral rules. The right column is labeled 'Morals Clause Mới' (New Morals Clause) in glowing green text and lists objective triggers: Q-Score thresholds and automatic termination clauses. Clean corporate background. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
8. TIMELINE CƠ CHẾ THU HỒI CLAWBACK (Chapter 4)
--------------------------------------------------------------------------------
Prompt:
A WIDE STILL SHOT showing a horizontal 12-month contract timeline bar. At the 6-month mark, a red lightning bolt symbol labeled 'Scandal' strikes. A large red arrow curves backward from the end, wrapping around the timeline, labeled 'Clawback (100% Thu hồi)' in clean bold text. Dark digital office background. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
9. BỘ LỌC KÉP - BA MŨI NHỌN PHONG SÁT (Chapter 5)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing three glowing digital screens. The left screen shows a theater stage crossed out with a large red 'X'. The middle screen shows a television broadcast crossed out with a large red 'X'. The right screen shows a smartphone with social media icons locked behind a large metal padlock. Dark tech room background. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
10. TIMELINE LEO THANG PHÁP LÝ - VỤ MIU LÊ (Chapter 5)
--------------------------------------------------------------------------------
Prompt:
A WIDE STILL SHOT showing a step-by-step upward staircase timeline. The first step is labeled 'Ngày 10/5: Xử phạt hành chính' in warning yellow. The second step is higher and labeled 'Ngày 16/5: Khởi tố & Bắt tạm giam' in critical red. A steep downward arrow labeled 'Dòng tiền quảng cáo = 0' drops off the edge. Dark room background. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
11. ĐƯỜNG ĐỐI CHIẾU HỒI PHỤC PHƯƠNG TÂY VS VIỆT NAM (Chapter 5)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing two parallel horizontal timelines. The top timeline is labeled 'Western Market' (Thị trường phương Tây) and shows a curve of recovery: Scandal -> Boycott -> Recovery (2-5 years) in green. The bottom timeline is labeled 'Vietnam Market' (Thị trường Việt Nam) and shows a straight drop to a question mark symbol '???' in red. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
12. VIRTUAL INFLUENCER TRONG STUDIO (Chapter 6)
--------------------------------------------------------------------------------
Prompt:
A MID SHOT showing a beautiful female virtual influencer with Vietnamese features posing inside a high-tech photo studio. She is surrounded by floating holographic screens displaying code, green data charts, and digital pixels. Professional camera gear stands in front of her. Bright ring light lighting. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
13. BIỂU ĐỒ PHÁ SẢN THƯƠNG HIỆU NGÔI SAO & VỤ KIỆN MIKE TYSON (Chapter 6)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION split in two halves. On the left side: a digital pie chart showing 46% of celebrity brands marked in bright red as 'Phá sản' (Bankrupt). On the right side: a stylized editorial portrait of Mike Tyson looking frustrated next to a glowing document labeled '$50M Lawsuit' in red. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
14. MA TRẬN ĐÁNH ĐỔI - TIN CẬY VS RỦI RO (Chapter 6)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a 2x2 grid matrix chart. The horizontal axis is labeled 'Rủi ro hành vi' (Behavioral Risk) from low to high. The vertical axis is labeled 'Lòng tin công chúng' (Public Trust) from low to high. In the low-risk/low-trust quadrant sits a glowing robotic avatar icon. In the high-risk/high-trust quadrant sits a human celebrity icon. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
15. BA TRỤ CỘT RECAP (Chapter 7)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing three vertical columns on a dark screen. The first column shows 'Lời hứa' (Promises) pointing to 'Objective Triggers' with a green arrow. The second column shows 'Niềm tin' (Trust) pointing to 'Clawback Clauses' with a green arrow. The third column shows 'Con người' (Human) pointing to 'AI Avatars' with a green arrow. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9

--------------------------------------------------------------------------------
16. KHUNG HÌNH KẾT - CÁN CÂN NGƯỜI & MÁY (Chapter 7)
--------------------------------------------------------------------------------
Prompt:
A SYMMETRICAL COMPOSITION showing a modern balance scale with two hands. On the left pan: a warm, detailed human hand with Vietnamese/Asian skin tone, palm up. On the right pan: a sleek, metallic robotic hand with glowing blue data circuits, palm up. The scale is perfectly balanced. Dark abstract digital workspace background with faint glowing grid lines. Dramatic rim lighting casting long shadows. modern comic book style, clean bold line art, flat coloring, subtle halftone Ben Day dots, high contrast, graphic novel aesthetic, Vietnamese aesthetic --ar 16:9


================================================================================
🎬 DÒNG CHẢY VIDEO PROMPTS (PROMPT TẠO VIDEO CLIPS - 16:9)
================================================================================
Sử dụng các prompt dưới đây trên Runway Gen-2/Gen-3, Luma Dream Machine, Kling AI, Pika, hoặc Veo.
Các prompt mô tả chuyển động camera và các hành động động của cảnh.

"""
    
    full_content = image_prompts_header + video_prompts_content
    
    with open(master_prompts_path, "w", encoding="utf-8") as f:
        f.write(full_content)
        
    print(f"✅ Success! Master prompts file created at: {master_prompts_path}")
    print(f"File size: {os.path.getsize(master_prompts_path)} bytes")

if __name__ == "__main__":
    main()
