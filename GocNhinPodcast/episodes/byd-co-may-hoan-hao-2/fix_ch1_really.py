import os

base_dir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/byd-co-may-hoan-hao-2'
ch1_file = os.path.join(base_dir, 'chapter_01.md')

with open(ch1_file, 'r', encoding='utf-8') as f:
    text = f.read()

old_text = 'Tại đại hội cổ đông tháng sáu năm hai nghìn không trăm hai mươi sáu, một nhà đầu tư đã bật khóc khi chứng kiến giá cổ phiếu bốc hơi gần một nửa. Đối diện sự phẫn nộ, Chủ tịch Wang Chuanfu thẳng thắn gọi quý vừa qua là "thời khắc đen tối nhất" do trợ cấp bị cắt giảm. Đó là lời thừa nhận đầy toan tính của một ông trùm vừa nếm đòn đau. Nhưng đó không phải là một lời đầu hàng. Ngay lập tức, ông tái khẳng định mục tiêu vượt mặt Toyota trong năm năm tới. Khi một cỗ máy khổng lồ mất đi bầu sữa trợ cấp, nó không thể thu mình lại. Nó buộc phải đạp ga tối đa, tràn ra toàn cầu để bù đắp dòng tiền. Động lực sinh tồn khốc liệt đó mới là tín hiệu cảnh báo thực sự, vượt xa mọi con số trên bảng cân đối.'
new_text = 'Tại đại hội cổ đông tháng sáu năm hai nghìn không trăm hai mươi sáu, một nhà đầu tư đã bật khóc khi chứng kiến giá cổ phiếu bốc hơi gần một nửa. Đối diện sự phẫn nộ, Chủ tịch Wang Chuanfu thẳng thắn gọi quý vừa qua là "thời khắc đen tối nhất" do trợ cấp bị cắt giảm. Nhưng ngay sau đó, ông vẫn tái khẳng định tham vọng vượt Toyota trong năm năm tới. Khó khăn hiện tại chỉ là phép thử ngắn hạn trước khi B Y D tăng tốc bành trướng ra toàn cầu.'

if old_text in text:
    print("Found old text. Replacing...")
    text = text.replace(old_text, new_text)
    with open(ch1_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced.")
else:
    print("Could not find exact old text!")
