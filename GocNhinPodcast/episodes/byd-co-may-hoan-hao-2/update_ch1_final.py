import os
import re

base_dir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/byd-co-may-hoan-hao-2'
ch1_file = os.path.join(base_dir, 'chapter_01.md')
vis_file = os.path.join(base_dir, 'chapter_01_visual.md')
prompt_file = os.path.join(base_dir, 'prompts_chapter_01.txt')

# 1. Update chapter_01.md
with open(ch1_file, 'r', encoding='utf-8') as f:
    text = f.read()

old_text = 'Tại đại hội cổ đông tháng sáu năm hai nghìn không trăm hai mươi sáu, một nhà đầu tư đã bật khóc khi chứng kiến giá cổ phiếu bốc hơi gần một nửa. Đối diện sự phẫn nộ, Chủ tịch Wang Chuanfu thẳng thắn gọi quý vừa qua là "thời khắc đen tối nhất" do trợ cấp bị cắt giảm. Nhưng đó không phải là một lời đầu hàng. Ngay lập tức, ông tái khẳng định mục tiêu vượt mặt Toyota trong năm năm tới. Khi một cỗ máy khổng lồ mất đi bầu sữa trợ cấp, nó không thể thu mình lại. Nó buộc phải đạp ga tối đa, tràn ra toàn cầu để bù đắp dòng tiền. Động lực sinh tồn khốc liệt đó mới là tín hiệu cảnh báo thực sự, vượt xa mọi con số trên bảng cân đối.'
new_text = 'Tại đại hội cổ đông tháng sáu năm hai nghìn không trăm hai mươi sáu, một nhà đầu tư đã bật khóc khi chứng kiến giá cổ phiếu bốc hơi gần một nửa. Đối diện sự phẫn nộ, Chủ tịch Wang Chuanfu thẳng thắn gọi quý vừa qua là "thời khắc đen tối nhất" do trợ cấp bị cắt giảm. Nhưng ngay sau đó, ông vẫn tái khẳng định tham vọng vượt Toyota trong năm năm tới. Khó khăn hiện tại chỉ là phép thử ngắn hạn trước khi B Y D tăng tốc bành trướng ra toàn cầu.'
text = text.replace(old_text, new_text)

with open(ch1_file, 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Update chapter_01_visual.md
with open(vis_file, 'r', encoding='utf-8') as f:
    vis_content = f.read()

old_vis_pattern = r'### CH01_SC026\n.*?### CH01_SC033\n'

new_vis_block = '''### CH01_SC026
- **[THOẠI]:** Tại đại hội cổ đông tháng 6 năm 2026,
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Sảnh lớn của đại hội cổ đông BYD, hàng ghế chật cứng nhà đầu tư với bầu không khí căng thẳng.
- **[TEXT OVERLAY]:** Không

### CH01_SC027
- **[THOẠI]:** một nhà đầu tư đã bật khóc khi chứng kiến giá cổ phiếu bốc hơi gần một nửa.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Cận cảnh một nhà đầu tư nam trung niên tháo kính, lấy tay lau nước mắt, phía sau là màn hình biểu đồ chứng khoán đỏ rực lao dốc.
- **[TEXT OVERLAY]:** "-45% STOCK VALUE"

### CH01_SC028
- **[THOẠI]:** Đối diện sự phẫn nộ, Chủ tịch Wang Chuanfu thẳng thắn gọi quý vừa qua là "thời khắc đen tối nhất" do trợ cấp bị cắt giảm.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Wang Chuanfu đứng trên bục, ánh mắt sắc lẹm không hề né tránh, tay cầm chiếc micro phát biểu mạnh mẽ dù đèn sân khấu đánh khối bóng tối lên mặt.
- **[TEXT OVERLAY]:** "THE DARKEST HOUR"

### CH01_SC029
- **[THOẠI]:** Nhưng ngay sau đó, ông vẫn tái khẳng định tham vọng vượt Toyota trong 5 năm tới.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Wang Chuanfu trên bục phát biểu, giơ tay chỉ thẳng về phía trước đầy quyết đoán. Bảng điện tử sau lưng ông chuyển từ màu đỏ của chứng khoán sang bản đồ thế giới màu xanh lam.
- **[TEXT OVERLAY]:** "OVERTAKE TOYOTA BY 2030"

### CH01_SC030
- **[THOẠI]:** Khó khăn hiện tại chỉ là phép thử ngắn hạn trước khi BYD tăng tốc bành trướng ra toàn cầu.
- **[BỐI CẢNH TỔNG THỂ & HÀNH ĐỘNG]:** Hàng dài vô tận những chiếc xe điện BYD đang nối đuôi nhau chạy lên một con tàu vận tải Ro-Ro khổng lồ tại cảng biển quốc tế sầm uất.
- **[TEXT OVERLAY]:** Không

### CH01_SC031\n'''

vis_content = re.sub(old_vis_pattern, new_vis_block, vis_content, flags=re.DOTALL)

# Renumber
new_vis_lines = []
for line in vis_content.splitlines():
    match = re.match(r'### CH01_SC(\d{3})', line)
    if match:
        old_num = int(match.group(1))
        if old_num >= 33:
            new_num = old_num - 2
            line = f'### CH01_SC{new_num:03d}'
    new_vis_lines.append(line)

with open(vis_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_vis_lines) + '\n')

# 3. Update prompts_chapter_01.txt
with open(prompt_file, 'r', encoding='utf-8') as f:
    prompt_content = f.read()

old_prompt_pattern = r'CH01_SC026 \[IMAGE\].*?CH01_SC032 \[VIDEO\].*?--ar 16:9'
new_prompts = '''CH01_SC026 [IMAGE]: Cinematic Editorial Noir, Wide Shot, a large shareholder meeting hall of BYD, rows of seats packed with investors, tense and heavy atmosphere, realistic lighting.
CH01_SC026 [VIDEO]: @CH01_SC026.png -> steady wide shot, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9

CH01_SC027 [IMAGE]: Cinematic Editorial Noir, Close-up Shot, a middle-aged male investor taking off his glasses, wiping tears with his hand, behind him is a glowing red stock market chart plummeting downwards, "-45% STOCK VALUE" text overlay.
CH01_SC027 [VIDEO]: @CH01_SC027.png -> steady shot on the crying man, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC028 [IMAGE]: Cinematic Editorial Noir, Low-Angle Medium Shot, Chairman Wang Chuanfu standing at a podium holding a microphone, speaking powerfully with a sharp and unevading gaze, dramatic chiaroscuro lighting casting deep shadows on his face, "THE DARKEST HOUR" text overlay.
CH01_SC028 [VIDEO]: @CH01_SC028.png -> steady shot on Wang Chuanfu speaking, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC029 [IMAGE]: Cinematic Editorial Noir, Medium Shot, Wang Chuanfu on stage pointing forward decisively, behind him the digital screen transitions from red financial charts to a glowing blue world map, "OVERTAKE TOYOTA BY 2030" text overlay.
CH01_SC029 [VIDEO]: @CH01_SC029.png -> steady shot on Wang Chuanfu, preserving the details of the reference image and static text overlay, 8-second continuous documentary video --ar 16:9

CH01_SC030 [IMAGE]: Cinematic Editorial Noir, Wide Shot, an endless line of brand new BYD electric cars driving in a row onto a colossal Ro-Ro cargo ship at a busy international seaport, twilight sky.
CH01_SC030 [VIDEO]: @CH01_SC030.png -> steady wide shot of the cars moving, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9'''

prompt_content = re.sub(old_prompt_pattern, new_prompts, prompt_content, flags=re.DOTALL)

prompt_blocks = re.split(r'\n\s*\n', prompt_content.strip())
new_prompt_blocks = []
for block in prompt_blocks:
    lines = block.split('\n')
    new_lines = []
    for l in lines:
        match = re.search(r'CH01_SC(\d{3})', l)
        if match:
            old_num = int(match.group(1))
            if old_num >= 33:
                new_num = old_num - 2
                l = re.sub(r'CH01_SC\d{3}', f'CH01_SC{new_num:03d}', l)
        new_lines.append(l)
    new_prompt_blocks.append('\n'.join(new_lines))

with open(prompt_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(new_prompt_blocks) + '\n\n')

print("Update complete")
